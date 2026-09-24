# Quy trình để AI tự kiểm tra và cập nhật luật mới (dùng khi hôm nay đã qua ngày "Data cập nhật")

Skill này là ảnh chụp pháp luật đến ngày ghi trong SKILL.md. Luật thuế Việt Nam đổi nhiều lần trong năm, nên AI có web search phải tự kiểm tra trước khi khẳng định một con số hay một hạn nộp. AI không có web search phải nói rõ: "Data của tôi đến ngày …, chưa kiểm tra được văn bản mới hơn".

## 1. Chỉ dùng nguồn chính chủ để khẳng định

| Nguồn | Chủ quản | Dùng để | Cách tìm |
|---|---|---|---|
| `vbpl.vn` — Cơ sở dữ liệu quốc gia về văn bản quy phạm pháp luật | Bộ Tư pháp | Tra số hiệu, **trạng thái hiệu lực**, văn bản sửa đổi/thay thế, toàn văn dạng text | Tìm kiếm web với `site:vbpl.vn "253/2026/NĐ-CP"`; trang chi tiết có dạng `vbpl.vn/van-ban/chi-tiet/<id>`, tab "Lược đồ" cho biết văn bản bị sửa bởi gì. Tên miền cũ `vbpl.moj.gov.vn` đã ngừng từ 23/04/2026 |
| `congbao.chinhphu.vn` | Văn phòng Chính phủ | PDF Công báo có chữ ký số — bản đối chiếu chính thức khi trích dẫn | `site:congbao.chinhphu.vn "số hiệu"` |
| `vanban.chinhphu.vn`, `xaydungchinhsach.chinhphu.vn` | Văn phòng Chính phủ | Toàn văn nghị định, luật, nghị quyết mới; dự thảo đang lấy ý kiến | `site:chinhphu.vn "tên văn bản"` |
| `vbpq.mof.gov.vn` | Bộ Tài chính | Thông tư, quyết định của Bộ Tài chính, file gốc .doc/.pdf | `site:mof.gov.vn "87/2026/TT-BTC"` |
| `gdt.gov.vn` (kể cả `thuedientu.gdt.gov.vn`, `canhan.gdt.gov.vn`) | Cục Thuế | Công văn hướng dẫn, hỏi đáp chính sách thuế, danh sách Hiệp định thuế, danh sách nhà cung cấp nước ngoài đã đăng ký, mẫu biểu | `site:gdt.gov.vn "từ khóa"` |
| `quochoi.vn`, `duthaoonline.quochoi.vn` | Quốc hội | Luật, nghị quyết Quốc hội; dự thảo luật | |

Trang tổng hợp thương mại (thuvienphapluat.vn, luatvietnam.vn, thuvienphapluat "hỏi đáp") chỉ dùng để **tìm số hiệu và ngày** rồi bắt buộc quay về nguồn chính chủ đối chiếu toàn văn. Báo chí, blog kế toán, Facebook, TikTok chỉ là gợi ý; nếu dùng phải gắn nhãn **TC** (nguồn thứ cấp) trong câu trả lời.

## 2. Ba câu hỏi phải trả lời trước khi trích một văn bản

1. **Còn hiệu lực không, từ ngày nào?** Xem trạng thái trên vbpl.vn và điều khoản "Hiệu lực thi hành" ở cuối văn bản. Luật thuế TNCN thường có hiệu lực khác với thời điểm áp dụng (ví dụ Luật 109/2025 hiệu lực 01/07/2026 nhưng phần lương, kinh doanh áp dụng cả kỳ 2026, Đ.29.2).
2. **Có bị sửa đổi, thay thế chưa?** Tab "Lược đồ" trên vbpl.vn, hoặc tìm `site:vbpl.vn "sửa đổi" "số hiệu"`. Văn bản mới hơn ưu tiên; nghị định không được trái luật, thông tư không được trái nghị định.
3. **Áp cho kỳ nào?** Giao dịch phát sinh trước ngày hiệu lực dùng văn bản cũ (không hồi tố), trừ khi văn bản mới ghi rõ áp dụng cho cả kỳ.

## 3. Khi nào phải tra trước khi trả lời

- Hôm nay đã qua ngày "Data cập nhật" trong SKILL.md **và** câu hỏi chạm số tiền, thuế suất, hạn nộp, ngưỡng, mẫu biểu.
- Người dùng nhắc đến một văn bản không có trong `van-ban-va-hieu-luc-2026.md`.
- Câu hỏi về mốc "từ 01/01/2027", "năm 2027", lương tối thiểu vùng, mức đóng BHYT, Nghị định hướng dẫn NQ 43/2026 — đây là các điểm được đánh dấu sắp đổi trong mục C và D của file văn bản.

Cách tra nhanh: tìm `site:vbpl.vn "thuế thu nhập cá nhân"` sắp xếp theo ngày ban hành mới nhất; tìm `site:chinhphu.vn "Nghị định" "thuế thu nhập cá nhân" 2027`; tìm `site:gdt.gov.vn "công văn" "thu nhập cá nhân"` cho hướng dẫn thực tiễn.

## 4. Cách dùng kết quả tra được

- Tìm thấy văn bản mới sửa nội dung skill đang dùng: trả lời theo văn bản mới, ghi rõ "văn bản mới hơn data của skill: [số hiệu, ngày hiệu lực, nguồn]", và nêu điểm nào của skill đã lỗi thời.
- Tìm thấy nhưng chỉ có nguồn thứ cấp: trả lời theo skill, thêm câu "có thông tin về [văn bản] theo [nguồn, TC], chưa đối chiếu được bản chính chủ".
- Không tìm thấy gì mới: nói "đã kiểm tra vbpl.vn/chinhphu.vn ngày …, chưa thấy văn bản mới hơn".
- Không được đoán số hiệu, không được suy "chắc đã có nghị định hướng dẫn". Dự thảo chưa phải luật.

## 5. Nếu người dùng muốn cập nhật skill

Sửa `references/van-ban-va-hieu-luc-2026.md` (thêm dòng vào mục A/B/C, chuyển văn bản bị thay vào mục E), sửa con số trong file liên quan và bảng "Số liệu nhanh" của SKILL.md, đổi dòng "Data cập nhật", ghi một mục vào `references/changelog.md`. Mỗi dòng mới phải có nguồn chính chủ và nhãn NV (đã đọc toàn văn) hoặc TC. Gửi pull request về https://github.com/tndvnn/tncn kèm link nguồn.
