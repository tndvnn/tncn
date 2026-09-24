# Thuế thu nhập cá nhân 2026 — skill AI tính thuế, quyết toán, giảm trừ gia cảnh (Việt Nam)

*English version below.*

**tncn** là skill cho Claude, Claude Code, Antigravity và mọi nền tảng AI đọc được `SKILL.md`. Nạp vào là AI trả lời được các câu hỏi về **thuế thu nhập cá nhân 2026**: cách tính thuế thu nhập cá nhân từ tiền lương, quyết toán thuế TNCN kỳ 2026, hoàn thuế, giảm trừ gia cảnh 15,5 triệu, thuế cá nhân kinh doanh và bán hàng online, thuế chứng khoán, bất động sản, crypto, thuế người nước ngoài và thu nhập từ nước ngoài. Mọi câu trả lời kèm số điều khoản của Luật 109/2025/QH15, Nghị định 253/2026, Thông tư 87/2026 để người dùng tự đối chiếu.

Dành cho người Việt Nam và người nước ngoài đang sống, làm việc, kinh doanh tại Việt Nam. Cập nhật **24/09/2026** (v2.5.1), phủ toàn bộ văn bản có hiệu lực từ 01/01, 01/07, 24/08, 01/09, 12/09/2026 và các mốc đến 30/04/2027.

## Skill trả lời được gì

### Cách tính thuế thu nhập cá nhân 2026 từ tiền lương
Biểu thuế lũy tiến từng phần 5 bậc (5% đến 35%), giảm trừ gia cảnh 2026: 15,5 triệu/tháng cho bản thân, 6,2 triệu/tháng mỗi người phụ thuộc, giảm trừ y tế 23 triệu và giáo dục 24 triệu/năm, bảo hiểm hưu trí 3 triệu/tháng, tiền ăn ca 1,2 triệu, miễn thuế làm thêm giờ, khấu trừ 10% thu nhập vãng lai từ 5 triệu.

### Quyết toán thuế thu nhập cá nhân, hoàn thuế
Ai được ủy quyền cho công ty, ai phải tự quyết toán, hạn 31/03 và 30/04/2027, mẫu 02/QTT-TNCN theo Thông tư 89/2026, điều kiện hoàn thuế thu nhập cá nhân, quyết toán trước khi xuất cảnh.

### Thuế cá nhân kinh doanh, bán hàng online, Shopee, TikTok, YouTube
Ngưỡng doanh thu 1 tỷ không phải nộp thuế, thuế suất theo % doanh thu hoặc 15–20% lợi nhuận, sàn thương mại điện tử khấu trừ (Nghị định 252/2026), giảm 30% thuế theo Nghị quyết 43/2026, hóa đơn điện tử, gia hạn nộp thuế. Thu nhập từ nước ngoài: YouTube/AdSense, Upwork, Fiverr, affiliate, print-on-demand, tiền về Payoneer, rút lợi nhuận từ LLC Mỹ.

### Thuế chứng khoán, bất động sản, crypto, vàng
Chuyển nhượng bất động sản 2%, nhà ở duy nhất, chứng khoán và phái sinh 0,1%, chuyển nhượng vốn 20%, tài sản số 0,1%, vàng miếng, thừa kế, quà tặng, bản quyền, trúng thưởng.

### Thuế thu nhập cá nhân người nước ngoài, hiệp định tránh đánh thuế hai lần
Khi nào thành cá nhân cư trú và chịu thuế thu nhập toàn cầu (183 ngày hoặc nơi ở thường xuyên, kể cả khách sạn và chỗ ở công ty bố trí tại nơi làm việc), lương Việt Nam cộng lương làm remote cho công ty nước ngoài, tự khai quý mẫu 02/KK-TNCN, công nhân khu công nghiệp, digital nomad Mỹ có nhà cho thuê ở Mỹ, trừ thuế đã nộp ở nước ngoài theo Thông tư 95/2026, giấy chứng nhận cư trú, thỏa thuận song phương.

### Văn bản pháp luật và mốc hiệu lực
Luật thuế thu nhập cá nhân 2025 (Luật 109/2025/QH15), Nghị định 253/2026, Thông tư 87/2026, lịch hạn nộp đến 30/04/2027, dự thảo đang lấy ý kiến, văn bản đã hết hiệu lực không được trích.

### Tự kiểm tra luật mới ở nguồn chính chủ, nhắc hạn, chạy trên nhiều AI
AI có web search phải tra vbpl.vn, chinhphu.vn, mof.gov.vn, gdt.gov.vn xem văn bản định trích đã bị sửa hay thay thế chưa trước khi trả lời; không có web search thì phải nói rõ data đến ngày nào. Skill **cấm** AI lấy kết luận từ thuvienphapluat.vn, luatvietnam.vn và các trang SEO pháp luật: các trang này chèn nhận định của người viết bên cạnh văn bản, và phần lớn bài trên top tìm kiếm là bài cũ được sửa tiêu đề, nội dung đã hết hiệu lực từ 01/07/2026. AI không bị ép thì sẽ tự tìm đến các trang đó và chép luôn nhận định của họ thành câu trả lời. Mỗi câu trả lời nêu hạn đã quá và hạn sắp tới trong 60 ngày của đúng nhóm người hỏi, kèm mức phạt chậm nộp. Có `AGENTS.md`, `GEMINI.md` và 5 câu trả lời mẫu để Claude, Codex, Gemini CLI, Cursor giữ đúng định dạng.

Không cover: thuế TNDN, thuế xuất nhập khẩu, BHXH rút một lần, trợ cấp thất nghiệp.

## Cài đặt

Skill theo chuẩn mở [Agent Skills](https://agentskills.io): một thư mục có `SKILL.md` + `references/`. Cách chung cho mọi công cụ: clone repo vào đúng thư mục skill của công cụ đó, tên thư mục là `tncn`, rồi khởi động lại công cụ.

```bash
git clone https://github.com/tndvnn/tncn.git
```

| Công cụ | Đặt thư mục `tncn/` ở đâu | Ghi chú |
|---|---|---|
| **Claude Code** | `.claude/skills/tncn/` (theo dự án) hoặc `~/.claude/skills/tncn/` (mọi dự án) | Tự kích hoạt theo `description`; gọi tay bằng `/tncn` |
| **claude.ai** (web, app; gói Pro/Max) | Nén thư mục thành zip, tải lên tại Settings → Capabilities → Skills | Có sẵn zip trong mục Releases |
| **OpenAI Codex CLI** | `.agents/skills/tncn/` trong repo, hoặc `~/.agents/skills/tncn/` (mọi repo; `~/.codex/skills/` cũng được) | Phải là thư mục thật, Codex không đọc symlink. Hoặc trong Codex gõ `$skill-installer install https://github.com/tndvnn/tncn`. Khởi động lại Codex sau khi cài |
| **Gemini CLI** | `.gemini/skills/tncn/` (workspace) hoặc `~/.gemini/skills/tncn/` (user); `.agents/skills/` cũng được nhận | Kiểm tra bằng `/skills list` |
| **OpenClaw** | `openclaw skills install git:tndvnn/tncn` (SKILL.md ở gốc repo nên cài thẳng được) hoặc `openclaw skills install ./tncn` | Lưu tại `~/.openclaw/skills/`; cũng đọc `~/.agents/skills/` |
| **Hermes Agent** (Nous Research) | `hermes skills install https://raw.githubusercontent.com/tndvnn/tncn/main/SKILL.md --name tncn`, hoặc trong chat `/skills install <URL đó> --name tncn`; hoặc copy vào `~/.hermes/skills/tncn/` | Hermes tự tải kèm thư mục `references/`; sau đó gọi bằng `/tncn` |
| **Cursor, Antigravity, agent khác theo chuẩn Agent Skills** | `.agents/skills/tncn/` | Có thêm `AGENTS.md` để agent nào không nạp skill vẫn đọc được hướng dẫn |
| **ChatGPT** (web) | Không có cơ chế skill. Tạo một Project (hoặc Custom GPT), tải lên `SKILL.md` và toàn bộ file trong `references/` làm tài liệu, dán nội dung `AGENTS.md` vào phần Instructions | Nhớ bật web search để làm Bước 0 kiểm tra luật mới |
| Nền tảng khác | Dán `SKILL.md` vào system prompt, đưa `references/` vào knowledge base | |

### Tự kiểm tra cập nhật mỗi ngày

Skill được cập nhật liên tục khi có luật mới, nên SKILL.md bắt AI **kiểm tra bản mới một lần mỗi ngày trước khi trả lời**: có shell thì chạy `scripts/kiem-tra-cap-nhat.sh` (tự giới hạn 24 giờ; so `git fetch` với origin/main, hoặc so `version.json` với GitHub nếu không phải git clone; thêm `--apply` để `git pull` luôn), không có shell thì đọc `version.json` trên GitHub và nhắc người dùng tải zip mới. Chạy tay bất cứ lúc nào: `bash scripts/kiem-tra-cap-nhat.sh --force`. Số phiên bản và ngày data ghi ở đầu `SKILL.md` và trong `version.json`.

Câu hỏi mẫu sau khi cài: "Lương 30 triệu, 1 người phụ thuộc, thuế thu nhập cá nhân 2026 bao nhiêu?", "Tôi bán hàng Shopee doanh thu 1,5 tỷ thì nộp thuế thế nào?", "Người Hàn Quốc làm ở khu công nghiệp có lương remote từ Hàn thì khai thuế ra sao?".

## Agent quét luật mới chạy 24/7 trên VPS riêng

Skill này được cấp một **VPS NVMe riêng** ([TND VPS NVMe cho AI Agent](https://www.tnd.vn/vps-nvme)) chỉ để chạy agent quét luật thuế mới, nên người dùng không phải lo skill lỗi thời. Mỗi ngày agent:

1. Quét **vbpl.vn** (CSDL quốc gia về VBQPPL) lấy văn bản trung ương mới ban hành trong 10 ngày gần nhất khớp từ khóa thuế, lương, hóa đơn, BHXH.
2. Kiểm tra **trạng thái hiệu lực của 28 văn bản skill đang dựa vào** (Luật 109/2025, NĐ 253/2026, TT 87/2026, NĐ 252/2026, TT 89/2026, NĐ 68/2026…): văn bản nào đổi trạng thái hoặc có văn bản mới sửa/thay là cảnh báo ưu tiên.
3. Quét **portal.mof.gov.vn/hoidapcstc** lấy câu hỏi đáp về thuế TNCN mới được Bộ Tài chính trả lời, kể cả câu cũ nay mới có trả lời.

Có gì mới thì agent gửi email cảnh báo cho người bảo trì và lập báo cáo kèm việc phải làm với skill; người bảo trì đọc toàn văn ở nguồn chính chủ, sửa skill, tăng `version.json`, push lên GitHub. Phía người dùng, SKILL.md bắt AI kiểm tra phiên bản mới **một lần mỗi ngày trước khi trả lời** (mục "Tự kiểm tra cập nhật" ở trên), nên chỉ cần cài một lần, skill tự cập nhật. Mã nguồn agent nằm trong thư mục `agent/` của repo này.

## Cấu trúc

```
SKILL.md                                   bộ điều hướng + quy tắc chống sai + số liệu nhanh
references/
  tong-quan-thue.md                        biểu thuế, giảm trừ, bảo hiểm, khấu trừ 10%
  vi-du-tinh-thue.md                       ví dụ tính thuế lương, OT, y tế, seller, KOL, crypto
  quyet-toan-thue.md                       ai phải quyết toán, ủy quyền, hạn, hồ sơ, eTax
  ho-kinh-doanh-freelancer-kol-seller.md   hộ kinh doanh, sàn TMĐT, affiliate, giảm 30%
  thu-nhap-tu-nuoc-ngoai-mmo-youtube-freelancer.md
  dau-tu-ra-nuoc-ngoai-llc-my.md
  bat-dong-san-chung-khoan-tai-san-so.md
  nguoi-nuoc-ngoai.md                      cư trú, thuế toàn cầu, hiệp định, MAP
  van-ban-va-hieu-luc-2026.md              văn bản, hiệu lực, dự thảo, hết hiệu lực
  lich-han-nop-2026-2027.md                hạn nộp, quy tắc nhắc chủ động, phạt chậm nộp
  vi-du-hoi-dap-mau.md                     5 câu trả lời mẫu để model bắt chước
  quy-trinh-tu-cap-nhat-luat.md            AI tự tra luật mới ở nguồn chính chủ trước khi trả lời
  faq.md                                   27 câu hỏi thường gặp
  changelog.md
scripts/kiem-tra-cap-nhat.sh                 kiểm tra bản mới 1 lần/ngày
version.json                               số phiên bản máy đọc
AGENTS.md, GEMINI.md                       hướng dẫn cho Codex, Gemini CLI, Cursor
```

## Nguồn

Toàn văn Công báo, vbpl.vn, chinhphu.vn: Luật 109/2025/QH15, Luật 09/2026/QH16, Luật Quản lý thuế 108/2025, NQ 198/2025, NQ 43/2026/QH16, NĐ 253/2026, NĐ 252/2026, NĐ 68/2026, NĐ 141/2026, NĐ 245/2026, NĐ 161/2026, NĐ 293/2025, NĐ 137/2026, TT 87/2026, TT 89/2026, TT 90/2026, TT 95/2026, TT 50/2026. Mục nào lấy từ nguồn thứ cấp được đánh dấu **TC** trong file. Skill được lệnh không suy diễn: thiếu căn cứ thì trả lời "chưa có căn cứ trong văn bản, cần hỏi cơ quan thuế".

Khởi đầu từ cấu trúc của [dotanminh/thue-tncn-vietnam](https://github.com/dotanminh/thue-tncn-vietnam) (MIT); nội dung đã viết lại và sửa lỗi, xem `references/changelog.md`.

## Đóng góp

Phát hiện sai điều khoản, văn bản mới, công văn hướng dẫn: mở issue kèm số hiệu văn bản và link nguồn chính thống (Công báo, vbpl.vn, chinhphu.vn, gdt.gov.vn). Không nhận nội dung chỉ dựa trên bài báo hoặc mạng xã hội.

## Lưu ý

Thông tin tham khảo, không thay thế tư vấn thuế chuyên nghiệp. Kiểm tra lại tại gdt.gov.vn hoặc cơ quan thuế quản lý.

MIT License — tndvnn.

---

# Vietnam personal income tax 2026 — AI skill for tax rates, PIT finalization and expat tax

**tncn** is a skill for Claude, Claude Code, Antigravity and any AI platform that reads `SKILL.md`. It answers questions on **Vietnam personal income tax (PIT) for tax year 2026**: Vietnam tax rates and brackets, how to calculate salary tax, PIT finalization and refunds, deductions, tax on business and online selling income, securities, real estate and crypto, and **expat tax in Vietnam**: tax residency, worldwide income, foreign salary, double taxation treaties. Every answer cites the article of Law 109/2025/QH15, Decree 253/2026 or Circular 87/2026 so you can verify it.

Built for Vietnamese residents and for foreigners living, working or doing business in Vietnam. Data as of **24 September 2026** (v2.5.1). Reference files are written in Vietnamese; the model answers in the language you ask in.

## What it covers

- **Vietnam income tax rates 2026**: 5-bracket progressive schedule (5% to 35%), personal deduction VND 15.5m/month, VND 6.2m per dependant, medical (23m) and education (24m) deductions, overtime exemption, 10% withholding on casual payments.
- **PIT finalization** for 2026: who may authorize the employer, who must file directly, deadlines 31 March and 30 April 2027, forms under Circular 89/2026, refunds, finalization before leaving Vietnam.
- Household businesses, freelancers, KOLs, online sellers: VND 1bn threshold, e-commerce platform withholding (Decree 252/2026), 30% reduction (Resolution 43/2026), e-invoices. Income from abroad: YouTube/AdSense, Upwork, Fiverr, affiliate, print-on-demand, Payoneer, profit from a US LLC.
- Real estate 2%, securities and derivatives 0.1%, capital transfer 20%, digital assets 0.1%, gold bars, inheritance, royalties.
- **Tax residency and expat tax**: when a foreigner becomes a Vietnamese tax resident taxed on worldwide income (183 days or a permanent place of residence, including hotel stays and housing provided at the workplace, Decree 253/2026 Art. 4), Vietnamese salary plus a remote salary from home, quarterly self-filing on form 02/KK-TNCN and mandatory direct finalization, industrial-zone workers, a US digital nomad with freelance income and a rental property back home, foreign tax credit under tax treaties (Circular 95/2026, in force 1 July 2026), Vietnamese certificate of residence, mutual agreement procedure.
- Timeline of legal documents, drafts and repealed documents.
- **Checks for newer law before answering, official sources only**: an AI with web search must look up vbpl.vn, chinhphu.vn, mof.gov.vn and gdt.gov.vn to see whether a document has been amended or replaced; without web search it must state the data date. The skill **forbids** taking conclusions from thuvienphapluat.vn, luatvietnam.vn and similar legal-SEO sites: they wrap the law in the author's own commentary, and most of their top-ranking pages are old articles with refreshed titles whose content expired on 1 July 2026. Left unconstrained, an AI drifts to those pages and copies their opinions as answers.
- **Proactive deadline reminders**: every answer lists overdue and upcoming (60-day) deadlines for the user's situation, with late-filing penalties.
- Works on Claude, Claude Code, Codex, Gemini CLI and Cursor: `AGENTS.md`, `GEMINI.md` and five model answers keep the output format stable across models.

Not covered: corporate income tax, customs duties, lump-sum social insurance withdrawal, unemployment benefits.

## Foreigners with income in two countries

The skill tells foreign users to **sort things out with their home-country tax authority first**: settle tax residence under the treaty tie-breaker, obtain a Vietnamese certificate of residence (forms 06/HTQT and 07/HTQT, Circular 89/2026), stop home-country withholding on salary for work performed in Vietnam and claim refunds there. Only the remaining treaty-eligible foreign tax is credited in Vietnam, capped at the Vietnamese tax on that income (Circular 95/2026 Art. 51). Vietnamese filing deadlines are not suspended meanwhile. Where no treaty is in force (for example the United States), foreign tax cannot be credited and the skill says so up front.

## Installation

The skill follows the open [Agent Skills](https://agentskills.io) format: one folder with `SKILL.md` + `references/`. Generic recipe for every tool: clone the repo into that tool's skills directory under the name `tncn`, then restart the tool.

```bash
git clone https://github.com/tndvnn/tncn.git
```

| Tool | Where the `tncn/` folder goes | Notes |
|---|---|---|
| **Claude Code** | `.claude/skills/tncn/` (per project) or `~/.claude/skills/tncn/` (all projects) | Auto-triggers from `description`; invoke manually with `/tncn` |
| **claude.ai** (web/app, Pro/Max) | Zip the folder, upload under Settings → Capabilities → Skills | A ready zip is in Releases |
| **OpenAI Codex CLI** | `.agents/skills/tncn/` inside the repo, or `~/.agents/skills/tncn/` for every repo (`~/.codex/skills/` also works) | Must be a real directory, Codex does not follow symlinks. Or inside Codex run `$skill-installer install https://github.com/tndvnn/tncn`. Restart Codex afterwards |
| **Gemini CLI** | `.gemini/skills/tncn/` (workspace) or `~/.gemini/skills/tncn/` (user); `.agents/skills/` is accepted as an alias | Verify with `/skills list` |
| **OpenClaw** | `openclaw skills install git:tndvnn/tncn` (SKILL.md sits at the repo root, so it installs directly) or `openclaw skills install ./tncn` | Stored in `~/.openclaw/skills/`; `~/.agents/skills/` is also read |
| **Hermes Agent** (Nous Research) | `hermes skills install https://raw.githubusercontent.com/tndvnn/tncn/main/SKILL.md --name tncn`, or in chat `/skills install <that URL> --name tncn`; or copy into `~/.hermes/skills/tncn/` | Hermes downloads `references/` along with it; then call `/tncn` |
| **Cursor, Antigravity and other Agent-Skills-compatible agents** | `.agents/skills/tncn/` | `AGENTS.md` is included so agents that do not load skills still get the instructions |
| **ChatGPT** (web) | No skill mechanism. Create a Project (or a Custom GPT), upload `SKILL.md` and every file in `references/` as knowledge, paste `AGENTS.md` into Instructions | Enable web search so Step 0 (check for newer law) can run |
| Other platforms | Paste `SKILL.md` into the system prompt and add `references/` to the knowledge base | |

### Daily self-update check

The skill changes whenever the law does, so SKILL.md instructs the AI to **check for a newer version once a day before answering**: with a shell it runs `scripts/kiem-tra-cap-nhat.sh` (rate-limited to 24h; compares `git fetch` with origin/main, or `version.json` with GitHub when the folder is not a git clone; `--apply` pulls immediately), without a shell it reads `version.json` on GitHub and asks the user to download the latest zip. Run it manually any time: `bash scripts/kiem-tra-cap-nhat.sh --force`. Version and data date are at the top of `SKILL.md` and in `version.json`.

Sample questions: "I earn VND 50m/month in Hanoi with one dependant, what is my 2026 PIT?", "I am a Korean engineer in an industrial zone with a remote salary from Korea, how do I file?", "Is US tax withheld by Google creditable in Vietnam?".

## 24/7 law-watch agent on a dedicated VPS

This skill has its own **dedicated NVMe VPS** ([TND NVMe VPS for AI agents](https://www.tnd.vn/vps-nvme)) that runs a law-watch agent every day, so users never work from stale content. Each day the agent:

1. Scans **vbpl.vn** (the national legal database) for new central-government documents issued in the last 10 days matching tax, payroll, invoice and social-insurance keywords.
2. Checks the **legal status of the 28 documents the skill relies on** (Law 109/2025, Decree 253/2026, Circular 87/2026, Decree 252/2026, Circular 89/2026, Decree 68/2026…); any status change or amending/replacing document raises a priority alert.
3. Scans **portal.mof.gov.vn/hoidapcstc** for newly answered official PIT rulings from the Ministry of Finance, including older questions that have just been answered.

When something new appears, the agent emails the maintainer and writes a report with the required skill changes; the maintainer reads the full text at the official source, updates the skill, bumps `version.json` and pushes to GitHub. On the user side, SKILL.md makes the AI check for a new version **once a day before answering** (see "Daily self-update check"), so you install once and the skill keeps itself current. The agent source lives in this repo's `agent/` folder.

## Sources

Full official texts (Official Gazette, vbpl.vn, chinhphu.vn): Law 109/2025/QH15 on PIT, Law 09/2026/QH16, Law 108/2025 on Tax Administration, Resolutions 198/2025 and 43/2026, Decrees 253/2026, 252/2026, 68/2026, 141/2026, 245/2026, 161/2026, 293/2025, 137/2026, Circulars 87/2026, 89/2026, 90/2026, 95/2026, 50/2026. Anything taken from secondary sources is flagged **TC**. The skill is instructed not to guess: where the law is silent it says so and refers you to the tax office.

## Contributing

Open an issue for wrong citations, new legal documents or official rulings. Include the document number and a link to an official source (Official Gazette, vbpl.vn, chinhphu.vn, gdt.gov.vn). Content based only on news articles or social media is not accepted.

## Disclaimer

For reference only; not professional tax advice. Verify with gdt.gov.vn or your managing tax office.

MIT License — tndvnn.
