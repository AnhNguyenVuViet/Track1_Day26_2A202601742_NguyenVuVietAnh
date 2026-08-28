# Operating Dashboard — SupportPilot AI

> Ví dụ trang 1 rút gọn từ `b2b-supportpilot-example.md`; sản phẩm và số liệu đều hư cấu.

**Model:** B2B · **Cập nhật:** 2026-08-28 · **Owner phiên họp:** Product Operations

**Chẩn đoán:** Doanh nghiệp trả phí theo ticket; nhân viên support của doanh
nghiệp vận hành; SupportPilot không có quan hệ sản phẩm độc lập với khách cuối.

**North Star:** Median time-to-first-value · hiện tại 11 ngày · mục tiêu ≤7 ngày · 🟡

## Cây đèn 3 tầng

| Tầng · ID | Metric và định nghĩa ngắn | Hiện tại · 🟢 / 🟡 / 🔴 · Nguồn | Nhịp · Owner | Báo trước cho · Luật |
|---|---|---|---|---|
| L · L-01 | Median ngày kickoff → 20 ticket thật đạt QA | 11d · ≤7 / 8–14 / >14 · `[TB]` | Tuần · Product Ops | Activation + renewal · R-01 |
| L · L-02 | Champion có ≥2 action cấu hình/tuần ÷ champion active | 43% · ≥65 / 40–64 / <40 · `[TB]` | Tuần · Customer Success | TTFV · R-02 |
| O · O-01 | Pilot có 100 ticket thật/30d ÷ pilot go-live | 50% · ≥70 / 45–69 / <45 · `[MH]` | Tuần · Product Ops | POC→paid · R-03 |
| O · O-02 | Token + inference cost ÷ ticket đạt QA | 7.200đ · ≤6k / 6.001–8k / >8k · `[MH]` | Tuần · FinOps | GM · R-04 |
| O · O-03 | POC ký paid ÷ POC kết thúc | 40% · ≥55 / 35–54 / <35 · `[BM]` | Tháng · Revenue Ops | New ARR · R-03 |
| G · G-01 | (Revenue − variable cost) ÷ revenue | 47% · ≥55 / 45–54 / <45 · `[MH]` | Tháng · Finance | Runway + payback · R-04 |
| G · G-02 | Ending cohort revenue ÷ starting cohort revenue | 96% · ≥105 / 95–104 / <95 · `[TB]` | Quý · Finance | LTV · R-05 |

## Luật quyết định

| ID | NẾU · TRONG · VÀ | THÌ | KHÔNG THÌ | Dừng? |
|---|---|---|---|---|
| R-01 | TTFV >14d · 2 cohort · ≥5 pilot/cohort | Dừng pilot mới 14d; cắt onboarding còn 1 workflow | Không giảm giá để bù TTFV | CÓ |
| R-02 | Champion action <40% · 3 tuần · ≥8 champion | Product owner shadow 5 phiên onboarding | Không gửi email nhắc hàng loạt | KHÔNG |
| R-03 | Activation <45% · 2 cohort · ≥10 pilot | Đóng băng outbound; sửa checklist 1 sprint | Không tăng POC để bù tỷ lệ | CÓ |
| R-04 | AI cost >8.000đ · 2 tuần · ≥1.000 ticket QA | Giới hạn context, đổi model tier, đàm phán quota | Không bỏ QA để làm đẹp cost | KHÔNG |
| R-05 | NRR <95% · 2 quý · ≥12 account | Chuyển roadmap sang 3 churn cause có evidence | Không tính pipeline mới vào NRR | KHÔNG |

## Cổng 90 ngày

| Ngày | Một metric · ngưỡng | Evidence | Đạt / Trượt |
|---:|---|---|---|
| 30 | Champion xác nhận pain · ≥8/10 | Biên bản interview redacted | GO / FIX |
| 60 | Pilot activation · ≥45% trên ≥10 pilot | Cohort report từ event log | GO / PIVOT |
| 90 | GM sau AI cost · ≥45% trên ≥10.000 ticket | Billing export + QA report | GO / KILL |

**Kill criteria:** KILL ngày 90 nếu GM <45% sau hai vòng tối ưu model và không có
hợp đồng chấp nhận giá sàn 20.000đ/ticket.

**Chưa đo được:** Quyền thay đổi workflow của champion · cần câu hỏi kickoff và
audit 8 pilot · owner Product Operations · có số ngày 2026-09-11.
