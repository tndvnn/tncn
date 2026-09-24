# AGENTS.md — hướng dẫn cho Codex, Gemini CLI, Cursor và agent khác

Thư mục này là một **skill tư vấn thuế thu nhập cá nhân Việt Nam kỳ 2026**, viết theo chuẩn Agent Skills (SKILL.md + references/). Nếu agent của bạn không tự nạp skill, làm theo thứ tự:

1. Đọc trọn `SKILL.md` trước khi trả lời bất kỳ câu hỏi thuế nào. File này chứa quy trình trả lời, số liệu nhanh, quy tắc chống sai và disclaimer bắt buộc.
2. Chọn file trong `references/` theo bảng "File tham chiếu" trong SKILL.md rồi đọc đúng file đó. Không đọc cả thư mục một lượt; không trả lời từ trí nhớ khi file có sẵn.
3. Trả lời theo mẫu trong `references/vi-du-hoi-dap-mau.md`: kết luận → cách tính → điều khoản → việc phải làm và hạn → disclaimer.
4. Trước khi khẳng định một quy định, kiểm tra hiệu lực trong `references/van-ban-va-hieu-luc-2026.md`. Mục D là dự thảo, mục E đã hết hiệu lực.
5. Nếu hôm nay đã qua ngày "Data cập nhật" trong SKILL.md và agent có web search: làm theo `references/quy-trinh-tu-cap-nhat-luat.md` để tra văn bản mới ở nguồn chính chủ. Không có web search thì nói rõ data đến ngày nào.
6. Mỗi câu trả lời phải nhắc hạn kê khai sắp tới hoặc đã quá hạn liên quan đến người hỏi, theo `references/lich-han-nop-2026-2027.md`.

Quy tắc cứng: không bịa số, không suy từ luật cũ (TT 111/2013, Luật 04/2007), không trích văn bản mục E, thiếu căn cứ thì nói "chưa có căn cứ trong văn bản, cần hỏi cơ quan thuế". Trả lời bằng ngôn ngữ người hỏi dùng.

Skill không có script; không cần cài gì. Không sửa các file trong `references/` khi đang trả lời người dùng.
