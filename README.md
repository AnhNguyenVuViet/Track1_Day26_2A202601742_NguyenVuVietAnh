# Day 26 — Operating Dashboard Lab

Lab **“Đèn nào bật trước?”** biến mô hình Day 24–25 thành một hệ điều hành có
đèn báo sớm, ngưỡng, luật quyết định và cổng gác 90 ngày. Nội dung gốc và toàn
bộ benchmark nằm trong [`Day26-AI-Product-Handbook.md`](Day26-AI-Product-Handbook.md).

Repo học viên: <https://github.com/TuNM17421/Day26-Operating-Dashboard-Lab>

Đây là bài lab về **đọc tín hiệu và ra quyết định**, không phải bài lập trình.
Python chỉ dùng cho validator offline, không cần package hay API key.

## Đầu ra và hai loại file

Đừng cố ép bảng worksheet 12 cột lên một trang:

1. Copy [`operating-dashboard-template.md`](templates/operating-dashboard-template.md)
   để điền đầy đủ evidence và chạy validator.
2. Rút gọn đúng các giá trị đó sang
   [`one-page-dashboard-template.md`](templates/one-page-dashboard-template.md)
   để xuất **trang 1**.
3. Đưa ít nhất hai phép tính `[MH]` sang phụ lục **trang 2**.

File nộp cuối cùng là `[Tên]_Day26_dashboard.pdf`, tối đa hai trang. Giữ file
Markdown nguồn để sửa bài hoặc appeal theo evidence; không push bài làm/dữ liệu
nội bộ lên repo public.

So sánh [`worksheet example`](examples/b2b-supportpilot-example.md) với
[`one-page example`](examples/b2b-supportpilot-one-page.md) để thấy cách rút gọn
mà không làm mất quyết định vận hành.

## Điều kiện đầu vào

Bạn có thể clone repo và đọc bài trước, nhưng chưa thể hoàn thành/đạt minimum bar
nếu thiếu:

- Day 24: unit economics và các giả định như ARPU, gross margin, CAC/payback;
- Day 25: Value Metric, Cost/Job và cấu trúc chi phí AI.

Hai ngưỡng `[MH]` bắt buộc phải được tính lại từ số của chính bạn.

## Bắt đầu trong 3 phút

macOS/Linux:

```bash
git clone https://github.com/TuNM17421/Day26-Operating-Dashboard-Lab.git
cd Day26-Operating-Dashboard-Lab
mkdir -p "submissions/<MÃ-HỌC-VIÊN>"
cp templates/operating-dashboard-template.md \
  "submissions/<MÃ-HỌC-VIÊN>/operating-dashboard.md"
python3 scripts/validate_submission.py \
  "submissions/<MÃ-HỌC-VIÊN>/operating-dashboard.md"
```

Windows PowerShell:

```powershell
git clone https://github.com/TuNM17421/Day26-Operating-Dashboard-Lab.git
Set-Location Day26-Operating-Dashboard-Lab
New-Item -ItemType Directory -Force "submissions\<MÃ-HỌC-VIÊN>"
Copy-Item "templates\operating-dashboard-template.md" `
  "submissions\<MÃ-HỌC-VIÊN>\operating-dashboard.md"
python scripts\validate_submission.py `
  "submissions\<MÃ-HỌC-VIÊN>\operating-dashboard.md"
```

Lần validate đầu tiên **phải FAIL** vì template còn placeholder. Điền bài theo
luồng 120 phút trong handbook cho đến khi validator trả `PASS`.

## Luồng 120 phút

| Thời gian | Trạm | Đầu ra |
|---:|---|---|
| 0–15 | Chốt loại mô hình | Chẩn đoán + kiểm kê toàn bộ đèn ứng viên ✅/🔧/❌ |
| 15–40 | Dựng cây ba tầng | North Star + 6–8 đèn có nhịp và owner |
| 40–70 | Đặt ngưỡng | Xanh/vàng/đỏ, nguồn, lý do và ≥2 phép tính `[MH]` |
| 70–100 | Viết luật | 5 luật đủ năm vế, trong đó ≥2 luật dừng |
| 100–120 | Cổng 90 ngày | 3 cổng, kill criteria và dashboard một trang |

“Đèn bật trước” mặc định theo loại:

- B2C: đường cong retention có phẳng không;
- B2B: time-to-first-value;
- B2B2C: partner activation rate.

Bạn có thể chọn proxy khác nếu giải thích được chuỗi nhân quả tới đèn downstream.

## Rubric công khai

Rubric version `2.0.0` là hợp đồng chấm điểm công khai:

- [`rubric-v2.md`](rubric/rubric-v2.md) — bản học viên đọc;
- [`rubric-v2.json`](rubric/rubric-v2.json) — source-of-truth máy đọc;
- [`model-profiles.json`](rubric/model-profiles.json) — chẩn đoán và đèn bật trước;
- [`grader-output.schema.json`](rubric/grader-output.schema.json) — output bắt
  buộc có item ID, evidence, confidence và human-review status;
- [`GRADER_CARD.md`](rubric/GRADER_CARD.md) — giới hạn và ranh giới public/private.

Trọng số: Tier Discipline 20 · Threshold Quality 30 · Decision Rules 30 ·
90-Day Gates 15 · Honesty 5. Không có tiêu chí bí mật làm thay đổi điểm.

Validator public chỉ kiểm tra **cấu trúc và traceability**. `PASS` không xác nhận
benchmark còn mới, phép tính kinh doanh đúng hay lập luận đủ tốt. Repo hiện chưa
công bố semantic AI grader authoritative; các kết luận không chắc chắn phải qua
human review theo Grader Card.

## Quy tắc nguồn

- `[BM]`: ghi tên nguồn, URL trực tiếp, ngày kiểm tra và lý do dùng.
- `[MH]`: ghi `MH-01`/`MH-02`, input có đơn vị và phép tính tái lập được.
- `[TB]`: ghi cách tạo baseline, số chu kỳ đo và ngày dự kiến có số.
- Mỗi metric dùng đúng **một** loại nguồn.
- Snapshot nguồn trong handbook được chốt ngày `27/08/2026`; nguồn biến động phải
  được kiểm tra lại vào ngày làm bài.

## Quality gate

Kiểm tra package public và example:

```bash
make release-check
```

Hoặc chạy riêng:

```bash
python3 scripts/validate_rubric.py
python3 scripts/validate_submission.py examples/b2b-supportpilot-example.md
python3 -m unittest discover -s tests -v
```

Trước khi xuất PDF:

```bash
python3 scripts/validate_submission.py \
  submissions/<MÃ-HỌC-VIÊN>/operating-dashboard.md
```

## Cấu trúc repo

```text
.
├── Day26-AI-Product-Handbook.md
├── lab.config.json
├── templates/
│   ├── operating-dashboard-template.md
│   └── one-page-dashboard-template.md
├── examples/
│   ├── b2b-supportpilot-example.md
│   └── b2b-supportpilot-one-page.md
├── rubric/
│   ├── rubric-v2.json
│   ├── rubric-v2.md
│   ├── model-profiles.json
│   ├── grader-output.schema.json
│   └── GRADER_CARD.md
├── scripts/
│   ├── validate_submission.py
│   └── validate_rubric.py
├── tests/
└── submissions/                  # Bài làm local, bị Git ignore
```

File `day26-lab-operating-dashboard.md`, production grader prompt, gold labels,
holdout set, secret và log chấm có dữ liệu cá nhân không thuộc bản public.

## Dữ liệu và AI

- Không đưa dữ liệu khách hàng, hợp đồng chưa redacted hoặc secret vào bài/chatbot.
- AI có thể critique; học viên chịu trách nhiệm cuối cùng về nguồn, ngưỡng và luật.
- Repo ignore toàn bộ `submissions/` trừ `.gitkeep` để giảm nguy cơ push nhầm.
