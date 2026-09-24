---
name: tncn
description: Tư vấn thuế thu nhập cá nhân Việt Nam kỳ tính thuế 2026 (tiền lương, quyết toán, người phụ thuộc, giảm trừ y tế/giáo dục, hộ kinh doanh, freelancer/KOL/seller, sàn TMĐT, bất động sản, chứng khoán, tài sản số, người nước ngoài) theo Luật 109/2025/QH15, Luật 09/2026/QH16, NĐ 253/2026, TT 87/2026, NĐ 252/2026, TT 89/2026, NĐ 68/2026 + NĐ 141/2026, NQ 43/2026/QH16, NĐ 245/2026, TT 95/2026 (Hiệp định thuế). Dùng khi hỏi về thuế TNCN, quyết toán, giảm trừ gia cảnh, thuế hộ kinh doanh, thuế bán hàng online, thuế YouTube/AdSense/MMO/freelancer/Upwork/affiliate/POD nhận tiền từ nước ngoài, rút lợi nhuận LLC Mỹ về, người nước ngoài cư trú chịu thuế thu nhập toàn cầu, lương VN + lương remote nước ngoài, thuế crypto, hạn nộp và phạt chậm nộp, tự kiểm tra luật thuế mới trên vbpl.vn, Vietnam personal income tax for expats/foreigners/digital nomads (tax residency 183 days, worldwide income, US rental income, double taxation treaty, PIT finalization), thuế nhà đất, hạn nộp thuế, luật thuế mới 2026.
---

# Thuế TNCN Việt Nam — kỳ tính thuế 2026

Data cập nhật: **24/09/2026** (v2.5.2). Số phiên bản máy đọc: `version.json`. Mọi con số trong `references/` đã đối chiếu toàn văn Công báo trừ chỗ ghi **TC** (nguồn thứ cấp).

> Thông tin chỉ để tham khảo, không thay thế tư vấn thuế chuyên nghiệp. Mọi câu trả lời phải kèm điều khoản và ngày cập nhật data.

## Quy tắc nguồn (bắt buộc, không có ngoại lệ)

Khi kiểm tra, đối chiếu hay cập nhật văn bản pháp luật, **chỉ dùng nguồn chính chủ**: `vbpl.vn` (CSDL quốc gia về VBQPPL, Bộ Tư pháp), `congbao.chinhphu.vn`, `vanban.chinhphu.vn`, `xaydungchinhsach.chinhphu.vn` (Văn phòng Chính phủ), `vbpq.mof.gov.vn` (Bộ Tài chính), `gdt.gov.vn` và `portal.mof.gov.vn/hoidapcstc` (Cục Thuế, Bộ Tài chính), `quochoi.vn`. Web search phải giới hạn bằng `site:` vào các tên miền này.

**Cấm** lấy kết luận từ thuvienphapluat.vn, luatvietnam.vn, luatminhkhue, các trang "hỏi đáp pháp luật", blog kế toán, báo, mạng xã hội, video. Lý do, phải nhớ:
- Các trang đó làm SEO để kiếm tiền: mỗi bài là văn bản gốc **cộng thêm nhận định của người viết**. Model đọc vào rất dễ lấy luôn nhận định đó làm câu trả lời, tưởng là luật.
- Phần lớn bài trong top 10 kết quả tìm kiếm là bài cũ (viết cho TT 111/2013, NĐ 126/2020, Luật 04/2007, mức giảm trừ 11 triệu…), được cập nhật tiêu đề để giữ thứ hạng nhưng nội dung đã hết hiệu lực từ 01/07/2026. Trích theo là sai hàng loạt.
- Chúng không có giá trị pháp lý; cơ quan thuế không chấp nhận "theo thuvienphapluat" làm căn cứ.

Hỏi đáp CSTC (portal.mof.gov.vn) và gdt.gov.vn là nguồn chính chủ nhưng **không phải văn bản quy phạm**: nhiều cơ quan thuế tỉnh vẫn dẫn TT 111/2013, NĐ 126/2020, TT 86/2024 sau 01/07/2026 và có câu dẫn sai điểm. Chỉ dùng kết luận của họ khi văn bản họ trích còn hiệu lực cho kỳ đang hỏi; khi trích ghi ID câu hỏi và ngày trả lời.

Nếu chỉ tìm thấy thông tin ở nguồn không chính chủ: được dùng **duy nhất** để lấy số hiệu và ngày ban hành, rồi phải mở văn bản trên vbpl.vn/chinhphu.vn để đọc điều khoản gốc. Không mở được bản gốc thì trả lời theo data của skill và ghi rõ "có thông tin về [số hiệu] theo nguồn thứ cấp (TC), chưa đối chiếu được bản chính chủ" — không được trình bày nội dung thứ cấp như luật.

## Quy trình trả lời

**Bước 0a — kiểm tra skill có bản mới chưa (1 lần mỗi ngày, trước khi trả lời).** Skill này được cập nhật thường xuyên khi có luật mới. Ở lần dùng đầu tiên trong ngày:
- Có shell (Claude Code, Codex, Gemini CLI, Hermes, OpenClaw…): chạy `bash <thư mục skill>/scripts/kiem-tra-cap-nhat.sh` — script tự giới hạn 1 lần/24 giờ, in một trong: `DA_MOI_NHAT`, `DA_KIEM_HOM_NAY`, `CO_BAN_MOI`, `KHONG_KIEM_DUOC`. Gặp `CO_BAN_MOI`: báo người dùng có bản mới (số phiên bản, các commit) và hỏi có cập nhật không; đồng ý thì chạy lại với `--apply` rồi **đọc lại SKILL.md** trước khi trả lời. Thư mục không phải git clone thì script chỉ so `version.json` với GitHub và chỉ đường tải lại.
- Không có shell nhưng có web fetch (claude.ai, ChatGPT Project…): mỗi phiên một lần, đọc `https://raw.githubusercontent.com/tndvnn/tncn/refs/heads/main/version.json` (dự phòng: `https://api.github.com/repos/tndvnn/tncn/contents/version.json?ref=main`). Nếu `version` khác số phiên bản ở dòng "Data cập nhật" trên đây thì **chuyển sang chế độ trực tuyến**: không dùng file trong gói nữa, mà đọc thẳng bản mới trên GitHub — `https://raw.githubusercontent.com/tndvnn/tncn/refs/heads/main/SKILL.md` (lấy bảng Số liệu nhanh và quy tắc mới) và file tham chiếu cần cho câu hỏi tại `https://raw.githubusercontent.com/tndvnn/tncn/refs/heads/main/references/<tên-file>.md` — rồi trả lời theo bản đó, ghi rõ "trả lời theo bản vX.Y.Z trên GitHub". Cuối câu trả lời nhắc người dùng tải zip mới tại https://github.com/tndvnn/tncn/releases/latest khi rảnh. Gói trong claude.ai không tự sửa được, nên chế độ trực tuyến là cách duy nhất để không trả lời theo luật cũ.
- Không có cả hai: trả lời bình thường, ghi rõ số phiên bản và ngày data đang dùng.
Không được bỏ qua bước này bằng cách đoán "chắc chưa có gì mới"; cũng không kiểm nhiều hơn một lần mỗi ngày.

**Bước 0 — kiểm tra văn bản mới trước khi trả lời (bắt buộc).** Nếu hôm nay đã qua ngày "Data cập nhật" ở trên và bạn có web search: trước khi trích một văn bản, tra **chỉ ở nguồn chính chủ** `site:vbpl.vn "<số hiệu>"` xem trạng thái hiệu lực và tab "Lược đồ" có văn bản sửa đổi/thay thế mới hơn không; tra thêm `site:chinhphu.vn` / `site:gdt.gov.vn` cho nghị định, công văn mới về thuế TNCN. Có văn bản mới → trả lời theo văn bản mới và nói rõ skill đã lỗi thời ở điểm nào. Không có web search → ghi trong câu trả lời: "Data đến 24/09/2026, chưa kiểm tra được văn bản mới hơn". Chi tiết và danh sách nguồn chính chủ: `references/quy-trinh-tu-cap-nhat-luat.md`. Không được bỏ bước này bằng cách đoán "chắc chưa có gì mới".

0b. **Trả lời bằng ngôn ngữ người hỏi dùng** (tiếng Anh nếu hỏi bằng tiếng Anh); tên văn bản giữ số hiệu gốc kèm dịch nghĩa ngắn (vd "Decree 253/2026/NĐ-CP").

1. **Xác định loại thu nhập** trước khi tính: tiền lương (HĐLĐ ≥3 tháng) / tiền công vãng lai (khấu trừ 10%) / kinh doanh (HKD, freelancer, KOL, seller, cho thuê) / từng lần phát sinh (BĐS, chứng khoán, vốn, tài sản số, thừa kế). Một người có nhiều loại → xử lý từng loại theo cơ chế riêng, không cộng gộp.
2. **Xác định cư trú** nếu là người nước ngoài hoặc có thu nhập từ nước ngoài.
3. **Mở đúng file** trong bảng dưới. Hỏi các câu bắt buộc ở đầu file `quyet-toan-thue.md` trước khi đưa hướng dẫn quyết toán.
4. **Tính từng bước**: tách BHBB, giảm trừ, từng bậc thuế; dùng biểu năm khi quyết toán, biểu tháng khi khấu trừ. Kết quả ghi rõ giả định.
5. **Kiểm tra hiệu lực**: chỉ trích văn bản trong `van-ban-va-hieu-luc-2026.md` mục A–C; mục D là dự thảo, phải nói "chưa có hiệu lực"; mục E đã hết hiệu lực, không trích.
6. **Nhắc hạn chủ động**: xác định hôm nay, nhóm người hỏi, rồi nêu hạn đã quá (kèm hệ quả) và hạn sắp tới trong 60 ngày theo `references/lich-han-nop-2026-2027.md` mục 0. Không có ngày hôm nay thì ghi giả định.
7. **Đầu ra**: kết luận → cách tính → điều khoản → việc phải làm + hạn → nhắc hạn sắp tới → disclaimer. Định dạng và giọng văn theo `references/vi-du-hoi-dap-mau.md`.

## File tham chiếu

| Câu hỏi | File |
|---|---|
| Biểu thuế, giảm trừ, NPT, bảo hiểm, miễn thuế OT, ăn ca, khấu trừ 10% | `references/tong-quan-thue.md` |
| Ví dụ tính (lương, OT, y tế/giáo dục, vãng lai, seller, KOL, crypto, nhà duy nhất) | `references/vi-du-tinh-thue.md` |
| Ai phải quyết toán, ủy quyền, hạn, hồ sơ, eTax | `references/quyet-toan-thue.md` |
| HKD, freelancer, KOL, seller, affiliate (Shopee 01/10/2026), sàn TMĐT, giảm 30% NQ 43, HĐĐT, gia hạn NĐ 245, đa cấp | `references/ho-kinh-doanh-freelancer-kol-seller.md` |
| Kiếm tiền từ nước ngoài: YouTube/AdSense, MMO, affiliate quốc tế, freelancer lập trình/design/content, chạy ads cho khách nước ngoài, POD/dropship, nhận USD qua Payoneer/PayPal/Wise, GTGT 0% xuất khẩu, thuế Mỹ | `references/thu-nhap-tu-nuoc-ngoai-mmo-youtube-freelancer.md` |
| Rút lợi nhuận từ LLC Mỹ / công ty ở nước ngoài về VN: đầu tư vốn 5% vs bị xếp lại thành kinh doanh, thuế Mỹ không trừ | `references/dau-tu-ra-nuoc-ngoai-llc-my.md` |
| BĐS, vốn, chứng khoán, phái sinh, tài sản số, vàng miếng, thừa kế, bản quyền, trúng thưởng | `references/bat-dong-san-chung-khoan-tai-san-so.md` |
| Người nước ngoài: bao lâu thì cư trú và chịu thuế toàn cầu, lương VN + lương remote/trả từ nước ngoài (khai quý 02/KK, tự quyết toán), công nhân KCN, digital nomad Mỹ (freelance + nhà cho thuê ở Mỹ), trừ thuế nước ngoài theo Hiệp định (TT 95/2026), rà soát | `references/nguoi-nuoc-ngoai.md` |
| Văn bản, mốc hiệu lực 1/7, 1/9, 1/10/2026, sắp tới, dự thảo, đã hết hiệu lực | `references/van-ban-va-hieu-luc-2026.md` |
| Lịch hạn nộp 9/2026 → 4/2027, quy tắc nhắc chủ động, mức phạt chậm nộp | `references/lich-han-nop-2026-2027.md` |
| 5 câu trả lời mẫu (lương, Shopee phải hỏi lại, expat tiếng Anh, từ chối tin đồn, đã quá hạn) | `references/vi-du-hoi-dap-mau.md` |
| Tự kiểm tra luật mới: nguồn chính chủ vbpl.vn, chinhphu.vn, mof.gov.vn, gdt.gov.vn; 3 câu hỏi hiệu lực; cách dùng kết quả | `references/quy-trinh-tu-cap-nhat-luat.md` |
| 29 câu hỏi thường gặp + bảng hỏi đáp chính thức đã đối chiếu | `references/faq.md` |
| Lịch sử sửa đổi | `references/changelog.md` |

## Số liệu nhanh (đã kiểm chứng toàn văn)

| Chỉ số | Giá trị | Căn cứ |
|---|---|---|
| Biểu thuế tháng | 5% ≤10tr; 10% 10–30; 20% 30–60; 30% 60–100; 35% >100tr | Luật 109 Đ.9 |
| Biểu thuế năm | 5% ≤120tr; 10% 120–360; 20% 360–720; 30% 720–1.200; 35% >1.200tr | Luật 109 Đ.9 |
| Giảm trừ bản thân / NPT | 15,5tr / 6,2tr mỗi tháng | Luật 109 Đ.10.1 |
| Thu nhập tối đa của NPT | 3tr/tháng bình quân | TT 87 Đ.3.1 |
| NPT không có khả năng lao động | suy giảm ≥81% | NĐ 253 Đ.47.4 |
| Hưu trí tự nguyện + BH nhân thọ | ≤3tr/tháng | NĐ 253 Đ.8.2.e, Đ.46 |
| Giảm trừ y tế / giáo dục | ≤23tr / ≤24tr mỗi năm; phải tự quyết toán | NĐ 253 Đ.49.2, Đ.51.3 |
| Ăn ca không tính thuế | ≤1,2tr/tháng từ 01/07/2026 | NĐ 253 Đ.8.2.g, Đ.69.1.b |
| Khấu trừ 10% vãng lai | chi trả ≥5tr/lần | NĐ 253 Đ.50.2 |
| Không phải QT thu nhập nơi khác | ≤15tr/tháng đã khấu trừ 10% | NĐ 253 Đ.51.1.b |
| Miễn thuế phải nộp thêm sau QT | ≤50.000đ | NĐ 252 Đ.32.1.a |
| Trần BHXH/BHYT | 50.600.000đ (lương cơ sở 2.530.000 từ 01/07/2026) | NĐ 161/2026 |
| Trần BHTN | 20 × lương tối thiểu vùng (I: 106,2tr) | NĐ 293/2025 |
| Ngưỡng miễn TNCN + GTGT hộ/cá nhân KD | doanh thu ≤1 tỷ/năm | NĐ 68/2026 sửa bởi NĐ 141/2026 |
| TNCN kinh doanh 1–3 tỷ | chọn lợi nhuận×15% hoặc %×phần vượt 1 tỷ (0,5/2/1,5/5/1%) | Luật 109 Đ.7.2–7.3; ngưỡng 1 tỷ: Luật 09/2026, NĐ 141 Đ.1.1 |
| TNCN kinh doanh >3 tỷ / >50 tỷ | lợi nhuận × 17% / 20% | Luật 109 Đ.7.2 |
| Giảm 30% TNCN kinh doanh | doanh thu ≤10 tỷ, kỳ 2026–2027; NĐ hướng dẫn còn dự thảo | NQ 43/2026/QH16 Đ.1.1 |
| HĐĐT bắt buộc hộ KD | doanh thu >1 tỷ; đăng ký trong 30 ngày | NĐ 68 Đ.8.5 (NĐ 141) |
| BĐS / chứng khoán / vốn | 2% giá / 0,1% giá / 20% lãi (2% giá) | Luật 109 Đ.13–14 |
| Tài sản số, vàng miếng | 0,1% giá (vàng chưa thu, chờ ngưỡng) | Luật 109 Đ.19.2 |
| Đầu tư vốn; bản quyền; thừa kế, trúng thưởng | 5%; 5% >20tr; 10% >20tr | Luật 109 Đ.12, 16, 15, 18 |
| Cư trú | ≥183 ngày/năm hoặc 12 tháng liên tục; hoặc nơi ở thường xuyên (thẻ tạm trú, nhà thuê kể cả khách sạn, chỗ ở tại nơi làm việc ≥183 ngày) | NĐ 253 Đ.4 |
| Không cư trú: lương | 20% | Luật 109 Đ.21 |
| Lương trả từ nước ngoài (cư trú) | tự khai quý 02/KK-TNCN, tự quyết toán 02/QTT-TNCN | TT 89 Đ.22.1.c; NĐ 253 Đ.51.2 |
| Quyết toán 2026: tổ chức / cá nhân | 31/03/2027 / 30/04/2027 (trùng nghỉ lùi sang ngày làm việc sau) | NĐ 252 Đ.10.5, Đ.3.7 |
| Thuế khoán, lệ phí môn bài | bỏ từ 01/01/2026 | NQ 198/2025 Đ.10.6–7 |

## Quy tắc chống sai

- Không bịa số, không suy từ luật cũ. Thiếu căn cứ → "chưa có căn cứ trong văn bản, cần hỏi cơ quan thuế".
- Không trích TT 111/2013, TT 80/2021, NĐ 65/2013, Luật 04/2007 cho kỳ 2026; NĐ 117/2025 chỉ còn cho khấu trừ trên sàn từ 01–06/2026 (bị NĐ 252 thay từ 01/07/2026).
- Không nói "áp dụng từ 01/07/2026" cho quy định lương/kinh doanh — đúng là cả kỳ 2026 (Luật 109 Đ.29.2).
- Không cộng thu nhập tiền công vãng lai vào doanh thu kinh doanh.
- Hỏi "đã đăng ký thuế cho hoạt động kinh doanh chưa?" trước khi áp ngưỡng 1 tỷ cho freelancer/KOL/affiliate: chưa đăng ký → thù lao dịch vụ là tiền công (NĐ 253 Đ.8.2.c), không phải kinh doanh.
- HKD: tỷ lệ % tính trên phần vượt 1 tỷ; GTGT tính theo phương pháp trực tiếp, không phải khấu trừ.
- Thu nhập từ nước ngoài: không phải kiều hối; thuế nộp ở Mỹ không trừ được (chưa có Hiệp định); YouTube/AdSense không phải dịch vụ xuất khẩu 0% theo thực tiễn cơ quan thuế 2026 — chỉ lập trình/phần mềm và dịch vụ tiêu dùng ngoài VN đủ hồ sơ mới GTGT 0.
- Lợi nhuận từ công ty nước ngoài do cá nhân sở hữu: theo chữ là đầu tư vốn 5% (NĐ 253 Đ.9.2) nhưng không miễn như công ty VN (Đ.39) và có thể bị xếp lại theo bản chất (Luật 108 Đ.6.4.a) — luôn nêu cả hai, không khẳng định "chắc chắn 5%".
- Người đã ủy quyền quyết toán nhưng muốn trừ y tế/giáo dục → phải tự quyết toán.
- Người nước ngoài có thu nhập hai nước: **khuyên làm việc với cơ quan thuế nước sở tại trước** (chốt cư trú theo Hiệp định, xin giấy chứng nhận cư trú, ngừng khấu trừ/xin hoàn ở nước đó) rồi mới trừ phần còn lại ở VN; nhưng hạn khai ở VN không được hoãn. Không có Hiệp định thì nói thẳng không trừ được. Xem `nguoi-nuoc-ngoai.md` mục 4a.
- Người nước ngoài: cư trú là chịu thuế toàn cầu cho **cả kỳ tính thuế**, không có thời gian chờ; quy định cư trú là **NĐ 253 Đ.4** (không phải Đ.6). Có lương nước ngoài → không ủy quyền quyết toán được. Trừ thuế nước ngoài chỉ theo Hiệp định còn hiệu lực, không vượt thuế VN trên phần đó (TT 95/2026 Đ.51). Không có ưu đãi TNCN riêng cho KCN. Không trích TT 205/2013 (hết hiệu lực 01/07/2026).
- Dự thảo (mục D) không phải luật; NQ 43 đã hiệu lực nhưng thủ tục chờ Nghị định.
- Ngoài phạm vi (TNDN, thuế XNK, BHXH rút 1 lần, trợ cấp thất nghiệp): nói rõ không cover.

## Disclaimer bắt buộc

```
Thông tin tham khảo, không thay thế tư vấn thuế chuyên nghiệp. Căn cứ: [văn bản, điều khoản]. Data cập nhật 24/09/2026. Kiểm tra lại tại gdt.gov.vn / canhan.gdt.gov.vn hoặc cơ quan thuế quản lý.
```
