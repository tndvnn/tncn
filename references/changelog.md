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

- Thêm ranh giới NĐ 253 Đ.8.1.c: thù lao dịch vụ của cá nhân chưa đăng ký thuế kinh doanh là tiền lương, tiền công; sửa câu "freelancer/KOL đều là thu nhập kinh doanh".
- Thêm NĐ 253 Đ.67.4.a: tổ chức không khấu trừ thu nhập kinh doanh của cá nhân cư trú, trừ sàn/hợp tác KD/đại lý/môi giới.
- Thêm mục 5a: Shopee affiliate khấu trừ 5% TNCN + 5% GTGT từ 01/10/2026 (nguồn email Shopee, TC), phân tích thuế suất 2% vs 5% theo Phụ lục NĐ 253, hoàn thuế cuối năm; bác tin "nâng ngưỡng lên 10 tỷ".
- FAQ thêm câu 20 về affiliate.

## 15/09/2026 — v2.1.0

- Thêm `thu-nhap-tu-nuoc-ngoai-mmo-youtube-freelancer.md`: phân loại thu nhập từ nước ngoài (Đ.8.1.c), thuế suất theo ngành (YouTube/nội dung số 5%+5%, lập trình 2%+GTGT 0, dịch vụ xuất khẩu 0%, ads rủi ro 5%, affiliate 2%/5%, POD 0,5%), ai khấu trừ/ai tự khai (NĐ 252 Đ.3.5, Đ.43), quy đổi tỷ giá, không phải kiều hối, thuế Mỹ không trừ, rủi ro TT 94, 4 ví dụ, 6 điểm chưa có căn cứ.
- Nguồn thực tiễn: Hỏi đáp CSTC 157922 (10/03/2026) — YouTube/AdSense không phải dịch vụ xuất khẩu 0%; CV 5151/CT-CS (23/07/2026, TC).
- FAQ thêm câu 21; SKILL.md thêm quy tắc về thu nhập từ nước ngoài.

## 17/09/2026 — v2.2.0

- Thêm `dau-tu-ra-nuoc-ngoai-llc-my.md`: thuế TNCN khi rút lợi nhuận từ công ty ở nước ngoài (đầu tư vốn 5% theo NĐ 253 Đ.9.2, thời điểm nhận Đ.52.6, không miễn Đ.39, không trừ thuế Mỹ Đ.6.3, khai 10 ngày); rủi ro xếp lại theo Luật 108 Đ.6.a; so sánh 3 kịch bản; phía Mỹ (TC); câu hỏi bắt buộc.
- FAQ thêm câu 22; SKILL.md thêm quy tắc.

## Kiểm tra định kỳ

Mỗi tháng: tra vbpl.vn + chinhphu.vn "Tham vấn chính sách" cho: Nghị định hướng dẫn NQ 43; lương tối thiểu vùng 2027; BHYT 5,1%; bất kỳ sửa đổi giảm trừ gia cảnh. Cập nhật `van-ban-va-hieu-luc-2026.md` và dòng "Data cập nhật" trong SKILL.md.
