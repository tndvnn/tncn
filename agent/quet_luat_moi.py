#!/usr/bin/env python3
"""Agent quét luật thuế mới hằng ngày cho skill tncn (github.com/tndvnn/tncn).

Bốn việc, chỉ dùng nguồn chính chủ:
1. vbpl.vn: văn bản trung ương mới ban hành trong cửa sổ N ngày khớp từ khóa thuế/lương.
2. vbpl.vn: trạng thái hiệu lực của danh sách văn bản skill đang dựa vào (watchlist) —
   đổi trạng thái hoặc có văn bản mới sửa/thay là tín hiệu phải update skill.
3. portal.mof.gov.vn/hoidapcstc: câu hỏi đáp mới về thuế TNCN đã được Bộ Tài chính trả lời
   (kể cả câu cũ nay mới có trả lời).
4. gdt.gov.vn: công văn hướng dẫn mới của Cục Thuế (danh sách theo tháng) khớp từ khóa thuế.

Kết quả: reports/YYYY-MM-DD.md + .json; exit 10 nếu có phát hiện mới, 0 nếu không, 1 nếu lỗi.
State lưu trong state/ để không báo trùng.
"""
from __future__ import annotations

import html
import json
import re
import sys
import time
from datetime import date, datetime, timedelta
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
from crawl_vbpl_client import LoiVbpl, VbplClient  # noqa: E402

GOC = Path(__file__).resolve().parent
STATE = GOC / "state"
REPORTS = GOC / "reports"
STATE.mkdir(exist_ok=True)
REPORTS.mkdir(exist_ok=True)

CUA_SO_NGAY = 10  # quét lùi 10 ngày để không lọt văn bản đăng muộn
TU_KHOA_TIEU_DE = re.compile(
    r"thu nhập cá nhân|quản lý thuế|giá trị gia tăng|hộ kinh doanh|cá nhân kinh doanh|"
    r"hóa đơn|chứng từ|thuế thu nhập|bảo hiểm xã hội|lương tối thiểu|lương cơ sở|"
    r"giảm trừ|nhà thầu nước ngoài|hiệp định.*thuế|tránh đánh thuế|thương mại điện tử|"
    r"nền tảng số|tài sản mã hóa|tài sản số|xử phạt.*thuế|đăng ký thuế|kê khai thuế|"
    r"giao dịch điện tử.*thuế|chuyển nhượng bất động sản|thuế thu nhập doanh nghiệp",
    re.I,
)
# Văn bản skill đang dựa vào — đổi trạng thái hoặc bị sửa/thay là phải update skill
WATCHLIST = [
    "109/2025/QH15", "09/2026/QH16", "108/2025/QH15", "48/2024/QH15", "198/2025/QH15",
    "43/2026/QH16", "253/2026/NĐ-CP", "252/2026/NĐ-CP", "68/2026/NĐ-CP", "141/2026/NĐ-CP",
    "245/2026/NĐ-CP", "181/2025/NĐ-CP", "125/2020/NĐ-CP", "310/2025/NĐ-CP", "291/2026/NĐ-CP",
    "161/2026/NĐ-CP", "293/2025/NĐ-CP", "137/2026/NĐ-CP", "284/2026/NĐ-CP", "283/2026/NĐ-CP",
    "103/2026/NĐ-CP", "87/2026/TT-BTC", "89/2026/TT-BTC", "90/2026/TT-BTC", "95/2026/TT-BTC",
    "18/2026/TT-BTC", "50/2026/TT-BTC", "94/2026/TT-BTC", "254/2026/NĐ-CP", "91/2026/TT-BTC",
]
RE_SO_HIEU_WATCH = re.compile("|".join(re.escape(w) for w in WATCHLIST))  # so cả số + năm + loại, tránh khớp 109/2026/QĐ-UBND
RE_DIA_PHUONG = re.compile(r"UBND|HĐND|Hội đồng nhân dân|Ủy ban nhân dân|Uỷ ban nhân dân", re.I)
LOAI_TRUNG_UONG = re.compile(r"^(Luật|Bộ luật|Nghị quyết|Pháp lệnh|Nghị định|Quyết định|Thông tư|Văn bản hợp nhất)", re.I)

MOF_URL = "https://portal.mof.gov.vn/hoidapcstc/home/cthoidap/{}"
MOF_KW = re.compile(r"thu nhập cá nhân|TNCN|giảm trừ gia cảnh|người phụ thuộc|quyết toán thuế|253/2026|109/2025|hộ kinh doanh|cá nhân kinh doanh", re.I)
UA = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) Chrome/140.0"}


def doc_state(ten: str, mac_dinh):
    p = STATE / ten
    if p.exists():
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            pass
    return mac_dinh


def ghi_state(ten: str, du_lieu) -> None:
    (STATE / ten).write_text(json.dumps(du_lieu, ensure_ascii=False, indent=1), encoding="utf-8")


def ngay(v: str | None) -> str:
    return (v or "")[:10]


# ---------- 1 + 2: vbpl.vn ----------

def quet_vbpl(client: VbplClient) -> tuple[list[dict], list[dict], list[str]]:
    loi: list[str] = []
    da_thay: dict = doc_state("vbpl_da_thay.json", {})
    tu = (date.today() - timedelta(days=CUA_SO_NGAY)).isoformat()
    moi: list[dict] = []
    try:
        for muc, _tong in client.duyet_tat_ca({"issueDateFrom": f"{tu}T00:00:00"}, co_trang=100, gioi_han=600):
            tieu_de = (muc.get("title") or "").strip()
            co_quan = (muc.get("agencyName") or "").strip()
            so_hieu = (muc.get("docNum") or "").strip()
            loai = ((muc.get("docType") or {}).get("name") or "").strip()
            # chỉ văn bản trung ương: bỏ UBND/HĐND và số hiệu kiểu QĐ-UBND
            if RE_DIA_PHUONG.search(co_quan) or "UBND" in so_hieu or "HĐND" in so_hieu or not LOAI_TRUNG_UONG.search(loai):
                continue
            cham = bool(RE_SO_HIEU_WATCH.search(tieu_de) or so_hieu in WATCHLIST)
            if not TU_KHOA_TIEU_DE.search(tieu_de) and not cham:
                continue
            mid = str(muc.get("id"))
            if mid in da_thay:
                continue
            vb = {
                "id": mid,
                "so_hieu": so_hieu,
                "tieu_de": tieu_de,
                "loai": loai,
                "co_quan": ", ".join(dict.fromkeys(x.strip() for x in co_quan.split(",") if x.strip())),
                "ban_hanh": ngay(muc.get("issueDate")),
                "hieu_luc": ngay(muc.get("effFrom")),
                "trang_thai": ((muc.get("effStatus") or {}).get("name") or "").strip(),
                "url": f"https://vbpl.vn/van-ban/chi-tiet/{mid}",
                "cham_watchlist": cham,
            }
            moi.append(vb)
            da_thay[mid] = {"so_hieu": vb["so_hieu"], "ngay": date.today().isoformat()}
    except LoiVbpl as e:
        loi.append(f"vbpl danh sách: {e}")
    ghi_state("vbpl_da_thay.json", da_thay)

    # Trạng thái hiệu lực watchlist
    trang_thai_cu: dict = doc_state("watchlist_trang_thai.json", {})
    doi: list[dict] = []
    for so in WATCHLIST:
        try:
            goi = client.danh_sach({"keyword": so}, 0, 10)
        except LoiVbpl as e:
            loi.append(f"vbpl watchlist {so}: {e}")
            continue
        khop = [m for m in (goi.get("items") or []) if (m.get("docNum") or "").strip() == so]
        if not khop:
            continue
        m = khop[0]
        tt = ((m.get("effStatus") or {}).get("name") or "").strip()
        het = ngay(m.get("effTo"))
        cu = trang_thai_cu.get(so)
        if cu is not None and (cu.get("trang_thai") != tt or cu.get("het_hieu_luc") != het):
            doi.append({"so_hieu": so, "cu": cu, "moi": {"trang_thai": tt, "het_hieu_luc": het},
                        "url": f"https://vbpl.vn/van-ban/chi-tiet/{m.get('id')}"})
        trang_thai_cu[so] = {"trang_thai": tt, "het_hieu_luc": het, "id": str(m.get("id"))}
        time.sleep(0.6)
    ghi_state("watchlist_trang_thai.json", trang_thai_cu)
    return moi, doi, loi


# ---------- 3: Hỏi đáp CSTC ----------

def tach_hoi_dap(s: str) -> dict | None:
    t = re.sub(r"<script.*?</script>|<style.*?</style>", "", s, flags=re.S)
    t = html.unescape(re.sub("<[^>]+>", "\n", t))
    t = re.sub(r"[ \t ]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    q0, a0 = t.find("Hỏi:"), t.find("Trả lời:")
    if q0 < 0 or a0 < 0:
        return None
    hoi = t[q0 + 4:a0].strip()
    tra_loi = t[a0 + 8:].split("Văn bản quy phạm, điều luật liên quan")[0].strip()
    m = re.findall(r"(\d{2}/\d{2}/\d{4})", t[max(0, a0 - 200):a0])
    return {"hoi": hoi, "tra_loi": tra_loi, "ngay": m[-1] if m else "", "da_tra_loi": len(tra_loi) >= 200}


def quet_mof() -> tuple[list[dict], list[str]]:
    loi: list[str] = []
    st = doc_state("mof.json", {"id_cuoi": 165900, "cho_tra_loi": {}, "da_bao": []})
    ss = requests.Session()
    ss.headers.update(UA)
    ket_qua: list[dict] = []

    def lay(i: int) -> dict | None:
        try:
            r = ss.get(MOF_URL.format(i), timeout=40)
            if r.status_code != 200:
                return None
            return tach_hoi_dap(r.text)
        except requests.RequestException as e:
            loi.append(f"mof {i}: {e}")
            return None

    # a) câu đang chờ trả lời (đã có câu hỏi TNCN, chưa có trả lời) — kiểm lại, bỏ sau 90 ngày
    cho = st["cho_tra_loi"]
    for sid in list(cho):
        if (date.today() - date.fromisoformat(cho[sid])).days > 90:
            del cho[sid]
            continue
        d = lay(int(sid))
        if d and d["da_tra_loi"]:
            ket_qua.append({"id": int(sid), **d, "url": MOF_URL.format(sid)})
            del cho[sid]
        time.sleep(0.4)
    # b) ID mới sau id_cuoi, dừng khi 40 ID liên tiếp không có trang
    i, trong = st["id_cuoi"] + 1, 0
    while trong < 40 and i < st["id_cuoi"] + 800:
        d = lay(i)
        if d is None:
            trong += 1
        else:
            trong = 0
            st["id_cuoi"] = i
            if MOF_KW.search(d["hoi"]):
                if d["da_tra_loi"]:
                    ket_qua.append({"id": i, **d, "url": MOF_URL.format(i)})
                else:
                    cho[str(i)] = date.today().isoformat()
        i += 1
        time.sleep(0.4)
    for k in ket_qua:
        st["da_bao"].append(k["id"])
    st["da_bao"] = st["da_bao"][-2000:]
    ghi_state("mof.json", st)
    return ket_qua, loi


# ---------- 4: gdt.gov.vn — Văn bản hướng dẫn của Cục Thuế ----------
# Trang chi tiết nạp bằng JS, nhưng danh sách theo tháng có sẵn trong HTML tĩnh (17 mục mới nhất).
GDT_THANG = "https://web.gdt.gov.vn/wps/portal?1dmy&page=Z6_CQKCVKV0009520IMEVDLA60O10&urile=wcm%3apath%3a%2Fgdt%2Bcontent%2Fsa_gdt%2Fsa_vanban%2Fvbhd%2Fvbhd_tct%2F{mm}-{yyyy}"
GDT_KW = re.compile(r"thu nhập cá nhân|TNCN|cá nhân|hộ kinh doanh|chính sách thuế|khai thuế|giá trị gia tăng|GTGT|hóa đơn|quyết toán|nhà thầu|thương mại điện tử|nền tảng|giảm trừ|khấu trừ|người phụ thuộc", re.I)
RE_GDT_ITEM = re.compile(r'<a[^>]+href="([^"]*vbhd_tct[^"]*)"[^>]*>\s*([^<]{10,300}?)\s*</a>\s*(?:<[^>]+>\s*)*\((\d{2}/\d{2}/\d{4})\)')


CHROME = Path.home() / "chromium" / "chrome"
PDF_DIR = REPORTS / "cv-cuc-thue"
CV_KW = re.compile(r"thu nhập cá nhân|TNCN|hộ kinh doanh|cá nhân kinh doanh|giảm trừ|người phụ thuộc|quyết toán thuế thu nhập cá nhân|nền tảng thương mại điện tử|sàn thương mại", re.I)


def trich_ket_luan(txt: str) -> str:
    """Lấy dòng V/v + phần sau 'có ý kiến như sau' để tóm tắt, bỏ phần đầu công văn."""
    vv = re.search(r"V/v[^\n]{0,160}", txt)
    txt = re.sub(r"\s+", " ", txt)  # pdftotext ngắt dòng giữa cụm "có ý kiến\nnhư sau"
    body = re.split(r"có ý kiến như sau[:\.]?", txt, maxsplit=1)
    phan = body[1] if len(body) > 1 else txt
    phan = re.sub(r"\s+", " ", phan).strip()
    return ((vv.group(0).strip() + " | ") if vv else "") + phan[:1200]


def tai_pdf_cong_van(url: str, so_hieu: str, ss: requests.Session) -> tuple[str, str]:
    """Render trang chi tiết bằng headless Chromium, tìm link /wps/wcm/connect/...pdf, tải và trích text.
    Trả (đường dẫn pdf, text 3000 ký tự đầu); chuỗi rỗng nếu không lấy được."""
    if not CHROME.exists():
        return "", ""
    PDF_DIR.mkdir(exist_ok=True)
    import subprocess
    try:
        dom = subprocess.run([str(CHROME), "--headless=new", "--no-sandbox", "--disable-gpu",
                              "--virtual-time-budget=15000", "--dump-dom", url],
                             capture_output=True, text=True, timeout=120).stdout
    except (subprocess.SubprocessError, OSError):
        return "", ""
    m = re.search(r'href="(/wps/wcm/connect/[^"]+\.pdf[^"]*)"', dom, re.I)
    if not m:
        return "", ""
    link = "https://web.gdt.gov.vn" + html.unescape(m.group(1))  # host gdt.gov.vn chặn curl/requests
    ten = re.sub(r"[^0-9A-Za-z]+", "-", so_hieu or "cv").strip("-") or "cv"
    pdf = PDF_DIR / f"{ten}.pdf"
    try:
        r = ss.get(link, timeout=90)
        r.raise_for_status()
        pdf.write_bytes(r.content)
        txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, timeout=60).stdout
    except (requests.RequestException, subprocess.SubprocessError, OSError):
        return "", ""
    txt = re.sub(r"[ \t]+", " ", txt)
    (PDF_DIR / f"{ten}.txt").write_text(txt, encoding="utf-8")
    return str(pdf), txt[:3000]


def quet_gdt() -> tuple[list[dict], list[str]]:
    loi: list[str] = []
    da_thay: dict = doc_state("gdt_da_thay.json", {})
    ss = requests.Session()
    ss.headers.update(UA)
    hom_nay = date.today()
    thang_truoc = (hom_nay.replace(day=1) - timedelta(days=1))
    moi: list[dict] = []
    for d in (hom_nay, thang_truoc):
        url = GDT_THANG.format(mm=f"{d.month:02d}", yyyy=d.year)
        try:
            r = ss.get(url, timeout=60)
            r.raise_for_status()
        except requests.RequestException as e:
            loi.append(f"gdt {d.month:02d}/{d.year}: {e}")
            continue
        for href, tieu_de, ngay_dang in RE_GDT_ITEM.findall(r.text):
            tieu_de = html.unescape(tieu_de).strip()
            khoa = tieu_de[:120]
            if khoa in da_thay or not GDT_KW.search(tieu_de):
                continue
            m = re.search(r"(\d{1,5}/[A-ZĐ-]+(?:-[A-ZĐ]+)*)", tieu_de)
            uuid = re.search(r"([0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})", href)
            link = (f"https://gdt.gov.vn/wps/portal?1dmy&page=Z6_CQKCVKV0009520IMEVDLA60O10&urile=wcm%3apath%3a%2Fgdt%2Bcontent%2Fsa_gdt%2Fsa_vanban%2Fvbhd%2Fvbhd_tct%2F{d.month:02d}-{d.year}%2F{uuid.group(1)}" if uuid else url)
            so_hieu = m.group(1) if m else ""
            pdf, txt = tai_pdf_cong_van(link, so_hieu, ss)
            moi.append({"so_hieu": so_hieu, "tieu_de": tieu_de, "ngay_dang": ngay_dang, "url": link,
                        # công văn nào cũng trích Luật 48/NĐ 252 làm căn cứ, nên "chạm watchlist" chỉ khi kèm sửa/thay/bãi bỏ
                        "cham_watchlist": bool(RE_SO_HIEU_WATCH.search(tieu_de) or re.search(r"(sửa đổi|thay thế|bãi bỏ|hết hiệu lực)[^.]{0,80}(" + RE_SO_HIEU_WATCH.pattern + ")", txt)),
                        "lien_quan_tncn": bool(CV_KW.search(txt)), "pdf": pdf, "trich": trich_ket_luan(txt)})
            da_thay[khoa] = hom_nay.isoformat()
        time.sleep(0.8)
    ghi_state("gdt_da_thay.json", da_thay)
    return moi, loi


# ---------- báo cáo ----------

def viet_bao_cao(moi, doi, hoi_dap, loi, cv_gdt=None) -> tuple[Path, bool]:
    cv_gdt = cv_gdt or []
    hom_nay = date.today().isoformat()
    co_gi = bool(moi or doi or hoi_dap or cv_gdt)
    dong = [f"# Quét luật thuế mới — {hom_nay}", "",
            f"Nguồn: vbpl.vn (cửa sổ {CUA_SO_NGAY} ngày, văn bản trung ương), watchlist {len(WATCHLIST)} văn bản skill đang dùng, portal.mof.gov.vn/hoidapcstc. "
            f"Skill: https://github.com/tndvnn/tncn", ""]
    uu_tien = [v for v in moi if v["cham_watchlist"]] + doi + [c for c in cv_gdt if c.get("cham_watchlist") or c.get("lien_quan_tncn")]
    if uu_tien:
        dong.append("## ⚠️ ƯU TIÊN — chạm văn bản skill đang dựa vào")
        for v in moi:
            if v["cham_watchlist"]:
                dong.append(f"- **{v['so_hieu']}** ({v['loai']}, {v['co_quan']}, ban hành {v['ban_hanh']}, hiệu lực {v['hieu_luc']}): {v['tieu_de']} — {v['url']}")
        for d in doi:
            dong.append(f"- **{d['so_hieu']}** đổi trạng thái: {d['cu'].get('trang_thai')} (hết {d['cu'].get('het_hieu_luc') or '-'}) → {d['moi']['trang_thai']} (hết {d['moi']['het_hieu_luc'] or '-'}) — {d['url']}")
        dong.append("")
    khac = [v for v in moi if not v["cham_watchlist"]]
    dong.append(f"## Văn bản mới khớp từ khóa thuế ({len(khac)})")
    for v in khac:
        dong.append(f"- {v['so_hieu']} ({v['loai']}, {v['co_quan']}, BH {v['ban_hanh']}, HL {v['hieu_luc']}, {v['trang_thai']}): {v['tieu_de']} — {v['url']}")
    if not khac:
        dong.append("- không có")
    dong.append("")
    dong.append(f"## Công văn hướng dẫn mới của Cục Thuế trên gdt.gov.vn ({len(cv_gdt)})")
    for c in sorted(cv_gdt, key=lambda x: (not x.get("cham_watchlist"), not x.get("lien_quan_tncn"))):
        nhan = ("**[chạm watchlist]** " if c["cham_watchlist"] else "") + ("**[liên quan TNCN/hộ KD]** " if c.get("lien_quan_tncn") else "")
        dong.append(f"- {nhan}{c['tieu_de']} (đăng {c['ngay_dang']}) — {c['url']}")
        if c.get("pdf"):
            dong.append(f"  PDF: `{c['pdf']}` (text cùng tên .txt). Trích: " + re.sub(r"\s+", " ", c.get("trich", ""))[:700])
        else:
            dong.append("  Không tải được PDF tự động — mở link bằng trình duyệt.")
    if not cv_gdt:
        dong.append("- không có")
    dong.append("")
    dong.append(f"## Hỏi đáp CSTC mới về TNCN đã được trả lời ({len(hoi_dap)})")
    for h in hoi_dap:
        dong.append(f"### ID {h['id']} — {h['ngay']} — {h['url']}")
        dong.append("**Hỏi:** " + h["hoi"][:1500].replace("\n", " "))
        dong.append("")
        dong.append("**Trả lời:** " + h["tra_loi"][:4000].replace("\n", " "))
        dong.append("")
    if not hoi_dap:
        dong.append("- không có")
    dong.append("")
    if loi:
        dong.append("## Lỗi khi quét")
        dong += [f"- {x}" for x in loi]
        dong.append("")
    dong.append("## Việc cần làm với skill")
    if co_gi:
        dong.append("1. Đọc toàn văn từng văn bản/câu trả lời ở nguồn chính chủ ở trên (không dùng thuvienphapluat).")
        dong.append("2. Xác định điều nào của skill (references/*.md, SKILL.md bảng Số liệu nhanh) bị ảnh hưởng; ghi vào `references/van-ban-va-hieu-luc-2026.md`.")
        dong.append("3. Sửa, tăng `version` trong version.json, ghi changelog, commit + push lên main.")
    else:
        dong.append("- Không có gì mới. Không cần sửa skill.")
    p = REPORTS / f"{hom_nay}.md"
    p.write_text("\n".join(dong) + "\n", encoding="utf-8")
    (REPORTS / f"{hom_nay}.json").write_text(json.dumps(
        {"ngay": hom_nay, "uu_tien": len(uu_tien), "van_ban_moi": moi, "watchlist_doi": doi, "hoi_dap": hoi_dap, "cv_gdt": cv_gdt, "loi": loi},
        ensure_ascii=False, indent=1), encoding="utf-8")
    return p, co_gi


def main() -> int:
    bat_dau = datetime.now()
    loi: list[str] = []
    moi, doi = [], []
    try:
        client = VbplClient(do_tre=0.8)
        client.tu_kiem_tra()
        moi, doi, l1 = quet_vbpl(client)
        loi += l1
    except Exception as e:  # noqa: BLE001 — báo lỗi vào report thay vì chết
        loi.append(f"vbpl: {e!r}")
    try:
        hoi_dap, l2 = quet_mof()
        loi += l2
    except Exception as e:  # noqa: BLE001
        hoi_dap = []
        loi.append(f"mof: {e!r}")
    try:
        cv_gdt, l3 = quet_gdt()
        loi += l3
    except Exception as e:  # noqa: BLE001
        cv_gdt = []
        loi.append(f"gdt: {e!r}")
    p, co_gi = viet_bao_cao(moi, doi, hoi_dap, loi, cv_gdt)
    print(f"{p} | văn bản mới {len(moi)} (ưu tiên {sum(v['cham_watchlist'] for v in moi)}) | watchlist đổi {len(doi)} | hỏi đáp {len(hoi_dap)} | CV Cục Thuế {len(cv_gdt)} | lỗi {len(loi)} | {(datetime.now() - bat_dau).seconds}s")
    if loi and not co_gi:
        return 1
    return 10 if co_gi else 0


if __name__ == "__main__":
    sys.exit(main())
