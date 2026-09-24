"""Client gọi Next.js Server Actions của CSDL quốc gia về pháp luật (vbpl.vn).

Bối cảnh: từ 23/04/2026 cổng chuyển từ vbpl.moj.gov.vn sang vbpl.vn, dựng lại
bằng Next.js App Router. Site KHÔNG có REST API công khai; dữ liệu đi qua
Server Actions (POST kèm header `Next-Action: <hash>`). Hash gắn với từng bản
build nên module này tự dò lại hash khi bản hardcode hết hiệu lực.

Ghi chú vận hành:
- Chrome headless bị lớp chống bot (_fec_sbu) trả 403; curl/requests với
  User-Agent trình duyệt thường thì qua. Vì vậy dùng requests, không dùng browser.
"""
from __future__ import annotations

import json
import re
import time

import requests

BASE = "https://vbpl.vn"
UA = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0 Safari/537.36"
)
# Hash của build tại 08/09/2026. Nếu site deploy lại, dò_hash() sẽ tìm hash mới.
HASH_DANH_SACH = "c529d164f28418e5898a834422629e64c6816af1"
HASH_CHI_TIET = "0fb12b3561faa05adec51a82efb3e4f4f427f07b"

TRANG_DANH_SACH = f"{BASE}/van-ban/trung-uong"
# ID mẫu (NĐ 320/2025) dùng làm ca kiểm thử khi dò lại hash chi tiết.
ID_MAU_CHI_TIET = "186493"


class LoiVbpl(RuntimeError):
    pass


class VbplClient:
    def __init__(self, do_tre: float = 0.8, so_lan_thu: int = 3, timeout: int = 90):
        self.do_tre = do_tre
        self.so_lan_thu = so_lan_thu
        self.timeout = timeout
        self.hash_danh_sach = HASH_DANH_SACH
        self.hash_chi_tiet = HASH_CHI_TIET
        self.ss = requests.Session()
        self.ss.headers.update({"User-Agent": UA})

    # ---------- tầng gọi thô ----------

    def _goi_action(self, url: str, hash_action: str, args: list) -> str:
        """POST một Server Action, trả về body dạng RSC flight (text)."""
        loi_cuoi = None
        for lan in range(self.so_lan_thu):
            try:
                r = self.ss.post(
                    url,
                    headers={
                        "Next-Action": hash_action,
                        "Content-Type": "text/plain;charset=UTF-8",
                        "Accept": "text/x-component",
                    },
                    data=json.dumps(args, ensure_ascii=False).encode("utf-8"),
                    timeout=self.timeout,
                )
                if r.status_code == 200:
                    # Server không khai charset -> requests đoán latin-1 làm hỏng
                    # tiếng Việt; ép UTF-8 để "HĐND" không thành "HÄND".
                    r.encoding = "utf-8"
                    time.sleep(self.do_tre)
                    return r.text
                loi_cuoi = f"HTTP {r.status_code}"
            except requests.RequestException as e:  # mạng chập chờn
                loi_cuoi = str(e)
            time.sleep(1.5 * (lan + 1))
        raise LoiVbpl(f"Gọi action thất bại sau {self.so_lan_thu} lần: {loi_cuoi}")

    @staticmethod
    def _tach_json(flight: str) -> dict | None:
        """Lấy chunk JSON đầu tiên trong payload RSC (dòng dạng `1:{...}`)."""
        for m in re.finditer(r"^\d+:(\{.*)$", flight, re.M):
            try:
                return json.loads(m.group(1))
            except json.JSONDecodeError:
                continue
        return None

    @staticmethod
    def _tach_text(flight: str) -> str:
        """Lấy chunk text lớn nhất (dạng `2:T<hexlen>,<nội dung>`) = HTML toàn văn.

        Phải cắt đúng độ dài khai trong `<hexlen>`: sau chunk HTML còn các chunk
        khác (JSON metadata) — lấy tràn thì khối JSON đó lọt vào thân văn bản.
        """
        vt = [m for m in re.finditer(r"^\d+:T([0-9a-f]+),", flight, re.M)]
        if not vt:
            return ""
        m = max(vt, key=lambda x: int(x.group(1), 16))
        # `hexlen` đếm BYTE UTF-8, không phải ký tự: tiếng Việt 2-3 byte/ký tự
        # nên cắt theo ký tự sẽ lấy lố sang chunk sau. Cắt trên bytes rồi decode.
        con_lai = flight[m.end():].encode("utf-8")
        than = con_lai[:int(m.group(1), 16)].decode("utf-8", errors="ignore")
        # Chốt phụ phòng khi độ dài khai sai: cắt tại chunk RSC kế tiếp.
        cat = re.search(r"\n\d+:[\{\[TIE]", than)
        return than[:cat.start()] if cat else than

    # ---------- tự phục hồi khi site đổi build ----------

    def do_lai_hash(self) -> None:
        """Quét JS chunk của trang chi tiết, thử từng hash tới khi ra JSON danh sách.

        Cần khi vbpl.vn deploy bản mới: hash Server Action đổi theo build.
        """
        html = self.ss.get(f"{BASE}/van-ban/chi-tiet/{ID_MAU_CHI_TIET}",
                           timeout=self.timeout).text
        ung_vien: list[str] = []
        for duong_dan in sorted(set(re.findall(r"static/chunks/[\w./%-]+\.js", html))):
            js = self.ss.get(f"{BASE}/_next/{duong_dan}", timeout=self.timeout).text
            if "vbpl-bientap-gateway" not in js and "documents" not in js:
                continue
            ung_vien += re.findall(r'\$\)\("([0-9a-f]{40})"\)', js)
        for h in dict.fromkeys(ung_vien):  # giữ thứ tự, bỏ trùng
            try:
                d = self._tach_json(self._goi_action(
                    TRANG_DANH_SACH, h, [{"pageNumber": 0, "pageSize": 1}]))
            except LoiVbpl:
                continue
            if isinstance(d, dict) and "total" in d and "items" in d:
                self.hash_danh_sach = h
                break
        else:
            raise LoiVbpl("Không dò được hash action danh sách — site đã đổi cấu trúc")
        for h in dict.fromkeys(ung_vien):
            if h == self.hash_danh_sach:
                continue
            try:
                noi_dung = self._tach_text(self._goi_action(
                    f"{BASE}/van-ban/chi-tiet/{ID_MAU_CHI_TIET}", h,
                    [ID_MAU_CHI_TIET]))
            except LoiVbpl:
                continue
            if len(noi_dung) > 5000:
                self.hash_chi_tiet = h
                return
        raise LoiVbpl("Không dò được hash action chi tiết — site đã đổi cấu trúc")

    def tu_kiem_tra(self) -> None:
        """Xác nhận 2 hash còn dùng được, nếu không thì dò lại."""
        try:
            d = self._tach_json(self._goi_action(
                TRANG_DANH_SACH, self.hash_danh_sach,
                [{"pageNumber": 0, "pageSize": 1}]))
            if isinstance(d, dict) and "items" in d:
                return
        except LoiVbpl:
            pass
        self.do_lai_hash()

    # ---------- API mức nghiệp vụ ----------

    def danh_sach(self, bo_loc: dict, trang: int = 0, co_trang: int = 100) -> dict:
        """Một trang kết quả tìm kiếm. `total` là tổng bản ghi khớp bộ lọc."""
        tham_so = {"pageNumber": trang, "pageSize": co_trang, **bo_loc}
        d = self._tach_json(self._goi_action(TRANG_DANH_SACH,
                                             self.hash_danh_sach, [tham_so]))
        if not d or "items" not in d:
            raise LoiVbpl(f"Phản hồi danh sách không hợp lệ: {str(d)[:200]}")
        return d

    def duyet_tat_ca(self, bo_loc: dict, co_trang: int = 100, gioi_han: int = 0):
        """Sinh lần lượt từng bản ghi qua mọi trang, dừng khi hết hoặc đủ `gioi_han`."""
        trang, da_lay = 0, 0
        while True:
            goi = self.danh_sach(bo_loc, trang, co_trang)
            muc = goi.get("items") or []
            if not muc:
                return
            for m in muc:
                yield m, goi.get("total", 0)
                da_lay += 1
                if gioi_han and da_lay >= gioi_han:
                    return
            if (trang + 1) * co_trang >= goi.get("total", 0):
                return
            trang += 1

    def chi_tiet_html(self, ma: str) -> str:
        """HTML toàn văn của một văn bản (chuỗi rỗng nếu văn bản chưa có nội dung)."""
        return self._tach_text(self._goi_action(
            f"{BASE}/van-ban/chi-tiet/{ma}", self.hash_chi_tiet, [str(ma)]))
