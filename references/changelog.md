# Changelog

## 15/09/2026 — v2.0.0 — viết lại toàn bộ

Kế thừa cấu trúc từ `dotanminh/thue-tncn-vietnam` v1.11.0 (MIT), đối chiếu từng con số với toàn văn Công báo: Luật 109/2025, NĐ 253/2026, TT 87/2026, NĐ 252/2026, TT 89/2026, NĐ 68/2026, NĐ 141/2026, Luật 09/2026, NQ 198/2025, NĐ 161/2026, NĐ 293/2025, NĐ 137/2026, NĐ 245/2026, NQ 43/2026/QH16.

Sửa so với bản gốc:
- Mốc áp dụng: quy định lương/kinh doanh áp dụng cả kỳ 2026, không phải từ 01/07/2026 (chỉ ăn ca 1,2tr từ 01/07).
- Thêm quy tắc bắt buộc tự quyết toán khi khai giảm trừ y tế/giáo dục (NĐ 253 Đ.51.3).
- Sửa ví dụ giảm trừ y tế/giáo dục: bậc 1 năm là 120tr, tiết kiệm 1,95tr (bản gốc tính 2,54tr).
- Sửa điều kiện NPT vợ/chồng trong tuổi lao động (không có khả năng lao động + thu nhập ≤3tr).
- HKD tính % trên phần doanh thu vượt 1 tỷ, không phải toàn bộ (Luật 109 Đ.7.3.a); thêm mức 1% kinh doanh khác, 5% cho thuê; GTGT hộ là phương pháp trực tiếp, không phải khấu trừ.
- Tách thu nhập tiền công vãng lai (khấu trừ 10%) khỏi doanh thu kinh doanh.
- Người không cư trú: chuyển nhượng vốn 20%/2% (0,1% chỉ với chứng khoán); ngưỡng trúng thưởng, thừa kế 20tr.
- Trích dẫn: biểu thuế là Luật 109 Đ.9 (không phải Đ.22); môn bài là NQ 198/2025 Đ.10.7 (Luật 109 không có Đ.35); ngưỡng 5tr và 15tr là NĐ 253 Đ.50–51.
- Bỏ dẫn chiếu TT 80/2021, NĐ 117/2025, TT 111/2013 (hết hiệu lực 01/07/2026); mẫu biểu theo TT 89/2026.
- Thêm NQ 43/2026/QH16 (giảm 30% TNCN kinh doanh 2026–2027), NĐ 245/2026 (gia hạn), NĐ 284/2026 (crypto, 01/09), NĐ 283/2026 (BHXH, 10/09), TT 110/2026 (12/09), timeline đến 30/04/2027 và các dự thảo.
- Bỏ phần BHXH rút 1 lần và trợ cấp thất nghiệp của bản gốc (ngoài phạm vi TNCN, chưa đối chiếu toàn văn Luật BHXH 2024/Luật Việc làm 2025).

## 15/09/2026 — v2.0.1

- Thêm ranh giới NĐ 253 Đ.8.2.c: thù lao dịch vụ của cá nhân chưa đăng ký thuế kinh doanh là tiền lương, tiền công; sửa câu "freelancer/KOL đều là thu nhập kinh doanh".
- Thêm NĐ 253 Đ.67.4.a: tổ chức không khấu trừ thu nhập kinh doanh của cá nhân cư trú, trừ sàn/hợp tác KD/đại lý/môi giới.
- Thêm mục 5a: Shopee affiliate khấu trừ 5% TNCN + 5% GTGT từ 01/10/2026 (nguồn email Shopee, TC), phân tích thuế suất 2% vs 5% theo Phụ lục NĐ 253, hoàn thuế cuối năm; bác tin "nâng ngưỡng lên 10 tỷ".
- FAQ thêm câu 20 về affiliate.

## 15/09/2026 — v2.1.0

- Thêm `thu-nhap-tu-nuoc-ngoai-mmo-youtube-freelancer.md`: phân loại thu nhập từ nước ngoài (Đ.8.2.c), thuế suất theo ngành (YouTube/nội dung số 5%+5%, lập trình 2%+GTGT 0, dịch vụ xuất khẩu 0%, ads rủi ro 5%, affiliate 2%/5%, POD 0,5%), ai khấu trừ/ai tự khai (NĐ 252 Đ.3.5, Đ.43), quy đổi tỷ giá, không phải kiều hối, thuế Mỹ không trừ, rủi ro TT 94, 4 ví dụ, 6 điểm chưa có căn cứ.
- Nguồn thực tiễn: Hỏi đáp CSTC 157922 (10/03/2026) — YouTube/AdSense không phải dịch vụ xuất khẩu 0%; CV 5151/CT-CS (23/07/2026, TC).
- FAQ thêm câu 21; SKILL.md thêm quy tắc về thu nhập từ nước ngoài.

## 17/09/2026 — v2.2.0

- Thêm `dau-tu-ra-nuoc-ngoai-llc-my.md`: thuế TNCN khi rút lợi nhuận từ công ty ở nước ngoài (đầu tư vốn 5% theo NĐ 253 Đ.9.2, thời điểm nhận Đ.52.6, không miễn Đ.39, không trừ thuế Mỹ Đ.6.3, khai 10 ngày); rủi ro xếp lại theo Luật 108 Đ.6.4.a; so sánh 3 kịch bản; phía Mỹ (TC); câu hỏi bắt buộc.
- FAQ thêm câu 22; SKILL.md thêm quy tắc.

## 24/09/2026 — v2.3.0

- Viết lại `nguoi-nuoc-ngoai.md`: sửa số điều cư trú (NĐ 253 **Đ.4**, trước ghi nhầm Đ.6/Đ.6.2); thêm Đ.4.2.a (thẻ tạm trú), Đ.4.2.b (khách sạn, ở nơi làm việc, nhà NSDLĐ thuê), Đ.4.3; mục "bao lâu thì chịu thuế toàn cầu" (Đ.6.2.a, Đ.66.1.a, NĐ 252 Đ.10.5.c); tie-breaker TT 95/2026 Đ.8.4.
- Thêm cách khai lương trả từ nước ngoài: khai quý 02/KK-TNCN (TT 89 Đ.22.1.c.1.2), tự quyết toán bắt buộc (NĐ 253 Đ.51.2), nơi nộp (Đ.22.1.c.3.2), hồ sơ trừ thuế nước ngoài 02/HTQT (TT 89 Đ.34); trừ BHBB nước ngoài (NĐ 253 Đ.46.2.a); trừ bản thân một nơi (Đ.48.1.a); công thức ngày/365 cho không cư trú (Đ.64.3).
- Thêm **TT 95/2026/TT-BTC** (thay TT 205/2013 từ 01/07/2026): khấu trừ thuế nước ngoài Đ.51, miễn 183 ngày Đ.34.2 chỉ cho người cư trú nước kia, trao đổi thông tin Đ.55.
- Mục công nhân/kỹ sư nước ngoài trong KCN + ví dụ lương VN 30tr + remote Hàn 25tr/tháng (nộp thêm 10,98tr khi quyết toán). Không có ưu đãi TNCN riêng cho KCN.
- Mục rà soát thu nhập toàn cầu: căn cứ TT 95 Đ.55, NĐ 291/2026; thực tiễn chỉ có nguồn thứ cấp (Thuế TP.HCM), chưa có văn bản chỉ đạo đợt rà soát riêng.
- Thêm mục 4a: thứ tự tránh đánh thuế hai lần, ưu tiên làm với cơ quan thuế nước sở tại trước (giấy chứng nhận cư trú, ngừng khấu trừ/hoàn), miễn theo TT 95 Đ.34.2 + mẫu 01/HTQT, MAP Đ.54 thời hạn 3 năm.
- Mẫu khai lợi tức từ tổ chức nước ngoài là 04/NNG-TNCN (TT 89 Đ.22.4.c, PL I 7.4.c); nhận vào tài khoản nước ngoài vẫn phải khai (NĐ 253 Đ.6.2.a); thời điểm doanh thu kinh doanh theo NĐ 68 Đ.5.3.
- Audit trước public (24/09): sửa vé máy bay về phép + học phí con expat (NĐ 253 Đ.8.4.e, g — không tính thu nhập chịu thuế); sản phẩm số 0% có mục riêng (Luật 48 Đ.9.1.c, NĐ 181 Đ.17.3.d); nền tảng nước ngoài NĐ 252 Đ.45.1.b; hoàn thuế trên 01/TKN-CNKD; giấy chứng nhận cư trú TT 89 Đ.44.3, hồ sơ miễn theo Hiệp định Đ.76; bỏ chữ "ký túc xá" (không có trong Đ.4.2.b); sửa số điều toàn cục: Đ.8.1.c→Đ.8.2.c, Luật 108 Đ.6.a→Đ.6.4.a, Đ.50.2.c→Đ.50.3.c, NĐ 68 Đ.14.5→Đ.8.5; khai bổ sung không bị phạt (Luật 108 Đ.44.2.a); gắn TC cho Hiệp định VN–Mỹ, Luật Đầu tư, chỉ tiêu 0% mẫu 01/CNKD.
- Mục 5b digital nomad Mỹ: mốc 183 ngày/12 tháng liên tục hồi tố, giai đoạn chưa cư trú (suy luận Đ.21 + Đ.8.2.c), kỳ đầu 12 tháng với freelance 1,8 tỷ (390,9tr tiền công vs 11,2tr nếu đăng ký KD) + nhà cho thuê ở Mỹ 750tr (Luật 109 Đ.7.4, ≤1 tỷ không thuế), timeline khai; FAQ 27.
- FAQ thêm câu 24, 25, 26; `tong-quan-thue.md` sửa Đ.6 → Đ.4; `van-ban-va-hieu-luc-2026.md` thêm TT 95/2026, 112/VBHN-VPQH, đưa TT 205/2013 vào mục E.

## 24/09/2026 — v2.4.0

- SKILL.md thêm **Bước 0 bắt buộc**: kiểm tra văn bản sửa đổi/thay thế trên vbpl.vn, chinhphu.vn, gdt.gov.vn trước khi trả lời (có web search), hoặc ghi rõ data đến ngày nào; thêm bước nhắc hạn chủ động.
- Thêm `quy-trinh-tu-cap-nhat-luat.md` (nguồn chính chủ, 3 câu hỏi hiệu lực, cách dùng kết quả, cách gửi PR), `vi-du-hoi-dap-mau.md` (5 mẫu: lương, Shopee hỏi lại, expat tiếng Anh, từ chối tin đồn, đã quá hạn), `AGENTS.md` + `GEMINI.md` cho Codex/Gemini/Cursor.
- Viết lại `lich-han-nop-2026-2027.md`: quy tắc nhắc chủ động, bảng khai quý 02/KK-TNCN cho lương trả từ nước ngoài, thứ trong tuần và ngày lùi (02/11/2026, 01/02/2027), quy tắc suy hạn NĐ 252 Đ.10, mức phạt chậm nộp NĐ 125 Đ.13 (cá nhân bằng một nửa, Đ.5.5), 0,03%/ngày, Luật 108 Đ.44.2.a.
- Đổi tên skill và repo thành `tncn` (github.com/tndvnn/tncn).
- Thêm **Quy tắc nguồn** vào SKILL.md, AGENTS.md, GEMINI.md, README và quy trình tự cập nhật: chỉ kiểm tra luật ở vbpl.vn, chinhphu.vn, mof.gov.vn, gdt.gov.vn, quochoi.vn; cấm lấy kết luận từ thuvienphapluat.vn, luatvietnam.vn và trang SEO pháp luật (chèn nhận định riêng, phần lớn bài top đã lỗi thời); nguồn thứ cấp chỉ dùng lấy số hiệu rồi phải mở bản gốc; thêm portal.mof.gov.vn/hoidapcstc làm nguồn thực tiễn cơ quan thuế.

## Kiểm tra định kỳ

Mỗi tháng: tra vbpl.vn + chinhphu.vn "Tham vấn chính sách" cho: Nghị định hướng dẫn NQ 43; lương tối thiểu vùng 2027; BHYT 5,1%; bất kỳ sửa đổi giảm trừ gia cảnh. Cập nhật `van-ban-va-hieu-luc-2026.md` và dòng "Data cập nhật" trong SKILL.md.
