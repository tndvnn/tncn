# agent/ — quét luật thuế mới hằng ngày cho skill tncn

Chạy trên VPS riêng (Ubuntu 24.04, Python 3.12 + `requests`), cron 07:30 hằng ngày.

- `quet_luat_moi.py`: (1) vbpl.vn — văn bản trung ương ban hành trong 10 ngày gần nhất khớp từ khóa thuế/lương/hóa đơn/BHXH; (2) trạng thái hiệu lực của 28 văn bản trong `WATCHLIST` (đổi trạng thái = cảnh báo ưu tiên); (3) portal.mof.gov.vn/hoidapcstc — câu hỏi TNCN mới được Bộ Tài chính trả lời, kể cả câu cũ nay mới có trả lời. Ghi `reports/YYYY-MM-DD.md|.json`, state trong `state/`; exit 10 nếu có gì mới.
- `chay_hang_ngay.sh`: gọi script trên, có gì mới thì gửi email qua `msmtp` (cần `~/.msmtprc`), log vào `logs/`.
- `crawl_vbpl_client.py`: client gọi Server Action của vbpl.vn (site chặn headless browser nhưng cho requests), tự dò lại hash khi site deploy bản mới.

Cài: `sudo mkdir -p /opt/thue-tncn-agent && sudo chown $USER /opt/thue-tncn-agent && cp agent/* /opt/thue-tncn-agent/ && (crontab -l; echo "30 7 * * * /opt/thue-tncn-agent/chay_hang_ngay.sh") | crontab -`. Thêm văn bản mới vào skill thì thêm số hiệu đầy đủ (vd `253/2026/NĐ-CP`) vào `WATCHLIST`.

Chỉ dùng nguồn chính chủ; không quét thuvienphapluat hay báo chí.
