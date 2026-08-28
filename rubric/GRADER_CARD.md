# Grader Card — Day 26 Operating Dashboard

## Trạng thái phát hành

Repo public hiện có:

- structural validator chạy offline;
- rubric máy đọc và bản rubric cho người đọc;
- model profiles và schema output chuẩn;
- unit tests cho validator và tính toàn vẹn rubric.

Repo **chưa phát hành một semantic AI grader được coi là authoritative**. Vì
vậy `PASS` từ `scripts/validate_submission.py` chỉ có nghĩa là bài đạt minimum
bar về cấu trúc và traceability, không phải điểm cuối.

## Kiến trúc chấm dự kiến

1. **Deterministic preflight** — kiểm tra section, số hàng, ID, ngày, URL, tag
   nguồn, gate decision và placeholder.
2. **Source verification** — mở URL `[BM]`, xác nhận claim và ngày truy cập;
   `[MH]` được tính lại từ input; `[TB]` được kiểm tra kế hoạch baseline.
3. **Semantic scoring** — chấm đúng item ID trong `rubric-v2.json`, bắt buộc
   evidence anchor và output theo `grader-output.schema.json`.
4. **Policy layer** — áp override, cap, grade band và human-review trigger bằng
   code quyết định, không để model tự cộng/trừ tùy ý.
5. **Human review** — xử lý `UNCERTAIN`, source lỗi, cap, điểm sát ranh giới và
   chênh lệch lớn giữa hai lượt chấm.

## Ranh giới public/private

Public để học viên biết chính xác mình được chấm thế nào:

- rubric, trọng số, công thức, cap và override;
- model profiles;
- output schema;
- validator cấu trúc và tests không chứa đáp án;
- ví dụ cấu trúc.

Không đưa vào repo public:

- system prompt vận hành production grader;
- gold labels dùng hiệu chỉnh và holdout/adversarial submissions;
- khóa API, log chấm có dữ liệu cá nhân;
- cơ chế chống gian lận chi tiết có thể làm mất tác dụng của kiểm tra.

Phần private không được chứa tiêu chí mới làm thay đổi điểm. Nó chỉ được triển
khai, hiệu chỉnh và kiểm thử hợp đồng public.

## Fairness và khả năng tái lập

- Chấm trên artifact đã ẩn tên/mã học viên nếu quy trình cho phép.
- Lưu rubric version, hash bài nộp, grader version, timestamp và run ID.
- Temperature/cấu hình model phải được cố định trong một cohort.
- Dùng ít nhất hai lượt độc lập khi điểm có hậu quả cao; chênh >8 điểm phải review.
- Không dùng lịch sử điểm, nhân khẩu học hoặc thông tin ngoài artifact.
- Không biến lỗi format nhỏ thành đánh giá năng lực kinh doanh; structural FAIL
  vẫn có thể được human review nếu artifact đọc được.

## Bảo mật dữ liệu

Bài lab không được chứa dữ liệu khách hàng, secret, hợp đồng chưa redacted hoặc
export nội bộ nhạy cảm. Source verifier chỉ mở URL public. Artifact private chỉ
được gửi tới dịch vụ AI khi tổ chức và học viên đã có cơ sở xử lý dữ liệu phù hợp.

## Appeal và thay đổi rubric

Feedback phải nêu item ID, điểm, evidence đã dùng và lý do. Học viên appeal bằng
cách chỉ ra evidence hoặc nguồn bị bỏ sót, không phải đoán prompt của grader.
Rubric có thay đổi ảnh hưởng điểm phải tăng version và không áp hồi tố cho cohort
đã bắt đầu, trừ khi lớp được thông báo và chấm lại toàn bộ theo cùng version.
