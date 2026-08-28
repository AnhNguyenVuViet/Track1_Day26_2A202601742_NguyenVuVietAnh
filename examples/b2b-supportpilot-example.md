# Operating Dashboard — SupportPilot AI

> Ví dụ minh họa cấu trúc validator cho một sản phẩm hư cấu. Không dùng các ngưỡng này cho sản phẩm thật nếu chưa tính lại từ dữ liệu của bạn.
> Đây là worksheet nguồn; bản nộp trang 1 được rút gọn bằng `templates/one-page-dashboard-template.md`.

- Học viên: Nguyễn Minh Anh
- Mã học viên: A0001
- Mô hình: B2B
- Cập nhật: 2026-08-28
- North Star: Median time-to-first-value dưới 7 ngày

## Chẩn đoán mô hình

SupportPilot AI là B2B vì doanh nghiệp trả phí theo số ticket, nhân viên support của chính doanh nghiệp vận hành sản phẩm và công ty chưa có quan hệ trực tiếp độc lập với khách hàng cuối.

| Dữ liệu đầu vào | Trạng thái | Nằm ở đâu hoặc cần gì để đo | Ngày có số |
|---|---|---|---|
| Unit economics Day 24 | Đo được | File mô hình tài chính nội bộ đã loại dữ liệu khách hàng | 2026-08-28 |
| Value Metric và Cost/Job Day 25 | Đo được | Cost per resolved ticket trong evidence pack | 2026-08-28 |

## Kiểm kê đèn ứng viên

| Đèn ứng viên từ handbook | Tầng | Trạng thái | Bằng chứng hiện có hoặc kế hoạch đo |
|---|---|---|---|
| Time-to-first-value (TTFV) | L | ✅ | Event kickoff và QA milestone đã có trong pilot log |
| Pipeline coverage | L | 🔧 | Chuẩn hóa stage và amount trong CRM trước 2026-09-11 |
| % deal chết ở khâu security/procurement | L | 🔧 | Thêm closed-lost reason bắt buộc trong CRM trước 2026-09-11 |
| POC → paid | O | ✅ | Cohort sheet của 10 pilot kết thúc gần nhất |
| Sales cycle (ngày) | O | 🔧 | Backfill ngày qualified opportunity cho 20 deal trước 2026-09-18 |
| Usage depth trong tài khoản | O | ✅ | Weekly active workflow theo account trong event log |
| Chi phí triển khai ÷ ACV | O | 🔧 | Gắn timesheet triển khai với contract ID trước 2026-09-18 |
| Tập trung doanh thu | O | ✅ | Billing export đã redacted theo account |
| NRR | G | 🔧 | Đủ hai cohort quý vào 2027-02-28 |
| Gross Margin | G | ✅ | Billing export ghép token và chi phí QA |
| CAC payback | G | 🔧 | Chuẩn hóa fully-loaded CAC theo quý trước 2026-10-15 |

## Đèn báo sớm

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| L-01 | Time-to-first-value | Số ngày từ kickoff đến khi agent xử lý 20 ticket thật đạt QA; median theo cohort | Tuần · Product Operations | 11 ngày | ≤7 ngày | 8–14 ngày | >14 ngày | [TB] Dùng hai cohort đầu làm tạm chuẩn và chốt baseline sau bốn cohort vào 2026-10-31 | 2026-08-28 | Activation và renewal | R-01 |
| L-02 | Champion weekly action rate | Số champion thực hiện ít nhất 2 hành động cấu hình mỗi tuần chia tổng champion active | Tuần · Customer Success | 43% | ≥65% | 40–64% | <40% | [TB] Đo bốn cohort bằng cùng event rồi chốt baseline vào 2026-10-31 | 2026-08-28 | Time-to-first-value | R-02 |

## Đèn vận hành

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| O-01 | Pilot activation rate | Pilot có 100 ticket thật trong 30 ngày chia tổng pilot go-live | Tuần · Product Operations | 50% | ≥70% | 45–69% | <45% | [MH] MH-02 cần ít nhất 7/10 pilot activate để đạt kế hoạch paid conversion | 2026-08-28 | POC-to-paid | R-03 |
| O-02 | Chi phí AI trên mỗi ticket giải quyết | Tổng token và inference cost chia số ticket đạt QA | Tuần · FinOps | 7.200 đ | ≤6.000 đ | 6.001–8.000 đ | >8.000 đ | [MH] MH-01 suy từ gross margin mục tiêu và chi phí biến đổi khác | 2026-08-28 | Gross margin | R-04 |
| O-03 | POC-to-paid conversion | Số POC ký hợp đồng trả phí chia số POC kết thúc trong kỳ | Tháng · Revenue Operations | 40% | ≥55% | 35–54% | <35% | [BM] ICONIQ State of Go-to-Market 2026 https://www.iconiq.com/growth/reports/state-of-go-to-market-2026; dùng ~50% như mốc tham khảo, không coi là mục tiêu tuyệt đối | 2026-08-28 | New ARR | R-03 |

## Đèn kết quả

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| G-01 | Gross margin sau AI cost | Doanh thu trừ toàn bộ chi phí biến đổi chia doanh thu | Tháng · Finance | 47% | ≥55% | 45–54% | <45% | [MH] MH-01 đặt trần AI cost để gross margin không thấp hơn mục tiêu | 2026-08-28 | Runway và payback | R-04 |
| G-02 | Net revenue retention | Doanh thu cohort cuối kỳ chia doanh thu cohort đầu kỳ sau expansion và churn | Quý · Finance | 96% | ≥105% | 95–104% | <95% | [TB] Chưa đủ lịch sử; đo cùng cohort trong hai quý rồi chốt baseline vào 2027-02-28 | 2026-08-28 | LTV | R-05 |

## Luật quyết định

| ID | NẾU | TRONG | VÀ | THÌ | KHÔNG THÌ | Luật dừng? |
|---|---|---|---|---|---|---|
| R-01 | Median TTFV >14 ngày | 2 cohort liên tiếp | Mỗi cohort có ít nhất 5 pilot | Dừng nhận pilot mới trong 14 ngày và cắt onboarding còn một workflow | Không giảm giá để bù chậm thấy giá trị | CÓ |
| R-02 | Champion action rate <40% | 3 tuần liên tiếp | Có ít nhất 8 champion được instrument | Chuyển một product owner sang shadow năm phiên onboarding | Không gửi thêm email nhắc hàng loạt | KHÔNG |
| R-03 | Pilot activation <45% | 2 cohort liên tiếp | Có ít nhất 10 pilot kết thúc | Đóng băng outbound và sửa activation checklist trong một sprint | Không tăng số POC để bù tỷ lệ thấp | CÓ |
| R-04 | AI cost mỗi ticket >8.000 đ | 2 tuần liên tiếp | Có ít nhất 1.000 ticket đạt QA | Giới hạn context, đổi model tier và đàm phán lại quota trước kỳ billing tiếp theo | Không bỏ QA để làm cost trông thấp hơn | KHÔNG |
| R-05 | NRR <95% | 2 quý liên tiếp | Cohort có ít nhất 12 account | Chuyển roadmap quý tới sang ba nguyên nhân churn lớn nhất có evidence | Không tính pipeline mới vào NRR | KHÔNG |

## Cổng gác 90 ngày

| Ngày | Metric gác cổng | Ngưỡng | Bằng chứng vật lý | Nếu đạt | Nếu trượt |
|---:|---|---|---|---|---|
| 30 | Interview xác nhận pain và workflow | 8/10 champion xác nhận cùng pain moment | Biên bản phỏng vấn đã redacted | GO | FIX |
| 60 | Pilot activation rate | ≥45% trên ít nhất 10 pilot | Cohort report từ event log | GO | PIVOT |
| 90 | Gross margin sau AI cost | ≥45% với ít nhất 10.000 ticket | Billing export và QA report | GO | KILL |

## Kill criteria

KILL hướng sản phẩm vào ngày 90 nếu gross margin vẫn dưới 45% sau hai vòng tối ưu model và không có hợp đồng nào chấp nhận mức giá sàn 20.000 đ mỗi ticket.

## Chưa đo được

| Đèn hoặc giả định | Cần gì để đo | Ai chịu trách nhiệm | Ngày có số |
|---|---|---|---|
| Tỷ lệ champion có đủ quyền thay đổi workflow | Thêm một câu hỏi quyền quyết định vào form kickoff và audit tám pilot | Product Operations | 2026-09-11 |

## Phụ lục ngưỡng suy từ mô hình

| ID | Metric | Input Day 24–25 | Phép tính | Kết quả và ngưỡng áp dụng |
|---|---|---|---|---|
| MH-01 | AI cost tối đa mỗi ticket | Giá 20.000 đ; GM mục tiêu 55%; chi phí biến đổi khác 3.000 đ | 20.000 × (1 − 55%) − 3.000 = 6.000 | Xanh khi AI cost ≤6.000 đ/ticket; đỏ trên 8.000 đ sau buffer |
| MH-02 | Pilot activation tối thiểu | Kế hoạch cần 7 account paid; POC-to-paid giả định 100% sau activation; 10 pilot | 7 account ÷ 10 pilot = 70% | Xanh từ 70%; đỏ dưới 45% vì không còn đường đạt kế hoạch ngay cả khi recovery |

## Ghi nhận AI critique

| Phản biện | Chấp nhận hay bác bỏ | Thay đổi đã thực hiện | Lý do |
|---|---|---|---|
| TTFV thiếu định nghĩa giá trị đầu tiên | Chấp nhận | Chốt 20 ticket thật đạt QA | Hai người có thể đo cùng một cách |
| Nên lấy benchmark NRR 101% làm ngưỡng đỏ | Bác bỏ | Giữ baseline theo cohort của chính sản phẩm | Chưa đủ dữ liệu cùng phân khúc để coi benchmark là ngưỡng hành động |
