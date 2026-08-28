# Rubric công khai v2.0 — Day 26 Operating Dashboard

File này là bản dễ đọc của rubric chấm bài. Nguồn máy đọc chính thức là
[`rubric-v2.json`](rubric-v2.json); hai file phải cùng version `2.0.0`.
Không có tiêu chí bí mật làm thay đổi điểm.

## Cách tính điểm

- Tổng: **100 điểm**, làm tròn theo bước **0,5 điểm**.
- Validator cấu trúc chạy trước nhưng `PASS` không đồng nghĩa với đạt 100 điểm.
- Mỗi item được chấm từ đúng evidence trong bài, không từ ấn tượng chung.
- Nếu item không có công thức riêng: `MET = toàn bộ điểm`, `NOT_MET = 0`,
  `UNCERTAIN = chuyển người chấm`, chưa tự đoán điểm.
- Override được áp dụng ở cấp item trước; cap được áp dụng ở cấp tiêu chí sau.
  Một lỗi không bị trừ hai lần ngoài cơ chế này.

Mỗi kết luận phải ghi đủ `section`, `row_id`, `field` và một trích đoạn ngắn
`quote`. Kết luận `NOT_MET` phải nêu vị trí đã kiểm tra và bằng chứng còn thiếu.

## 1. Tier Discipline — 20 điểm

| ID | Điểm | Điều kiện và cách chấm |
|---|---:|---|
| `TD-01` | 4 | Chẩn đoán model nhất quán từ **ai trả tiền / ai dùng / có chạm end-user không**. Đủ và nhất quán: 4; không suy ra được model: 0. |
| `TD-02` | 4 | North Star có mục tiêu và là “đèn bật trước” của model profile, hoặc proxy tương đương có lập luận. Đủ: 4; đúng metric nhưng thiếu mục tiêu/lập luận: 2; lagging không biện minh: 0. |
| `TD-03` | 6 | Có ≥2 Leading: 2 điểm. Cộng `4 × tỷ lệ Leading có downstream + chuỗi nhân quả hợp lý`, làm tròn 0,5. |
| `TD-04` | 4 | `4 × tỷ lệ metric đủ định nghĩa/formula + nhịp + owner`, làm tròn 0,5. |
| `TD-05` | 2 | Có metric chi phí AI/token/inference trực tiếp: 2; chỉ có GM hoặc không có: 0. |

Model profile chính thức nằm ở
[`model-profiles.json`](model-profiles.json). “Đèn bật trước” mặc định:

- B2C: đường cong retention có phẳng không;
- B2B: time-to-first-value;
- B2B2C: partner activation rate.

Học viên có thể dùng proxy khác nếu chỉ ra được metric downstream và chuỗi nhân
quả phù hợp; AI grader không được ép khớp từ khóa.

## 2. Threshold Quality — 30 điểm

| ID | Điểm | Điều kiện và cách chấm |
|---|---:|---|
| `TQ-01` | 4 | `4 × tỷ lệ metric` có ba vùng khác nhau, không chồng lấn và đúng chiều tốt/xấu. |
| `TQ-02` | 4 | `4 × tỷ lệ metric` có đúng một tag `[BM]`/`[MH]`/`[TB]` và một câu lý do. |
| `TQ-03` | 6 | `6 × tỷ lệ metric` truy vết đúng theo loại nguồn: `[BM]` có tên + URL trực tiếp + ngày; `[MH]` trỏ phép tính; `[TB]` nêu kế hoạch baseline. |
| `TQ-04` | 4 | `MH-01`: input có đơn vị 1đ; số học tái lập và đúng 2đ; kết quả khớp dashboard 1đ. |
| `TQ-05` | 4 | `MH-02`: input có đơn vị và độc lập với MH-01 1đ; số học tái lập và đúng 2đ; kết quả khớp dashboard 1đ. |
| `TQ-06` | 8 | `8 × tỷ lệ metric` có lý do ngưỡng đứng được và liên kết tới hành động. |

Quy tắc nguồn:

- `[BM]`: benchmark bên ngoài; phải ghi tên nguồn, URL trực tiếp hỗ trợ claim và
  ngày kiểm tra ISO `YYYY-MM-DD`.
- `[MH]`: suy từ mô hình Day 24–25; phải có ID `MH-xx` và phép tính tái lập.
- `[TB]`: team baseline; phải nói rõ cách đo, số chu kỳ và ngày dự kiến có số.

Không chấm một ngưỡng cao chỉ vì con số giống handbook. Chấm khả năng truy vết,
tính đúng phép tính và logic hành động.

## 3. Decision Rule Quality — 30 điểm

Năm item `DR-01`, `DR-02`, `DR-03`, `DR-04`, `DR-05` lần lượt chấm các luật
`R-01` đến `R-05`, mỗi luật tối đa 5 điểm:

| Thành phần | 1 điểm khi |
|---|---|
| NẾU | Chỉ rõ metric, toán tử và ngưỡng số |
| TRONG | Có window chống phản ứng với nhiễu |
| VÀ | Có mẫu tối thiểu hoặc điều kiện xác nhận |
| THÌ | Là hành động cụ thể đội có thể bắt đầu trong tuần tới |
| KHÔNG THÌ | Cấm một phản xạ sai có liên quan tới trigger |

`DR-06` tối đa 5 điểm: mỗi luật dừng hợp lệ được 2,5 điểm, tối đa hai luật.
Luật dừng phải ngừng một hành vi/khoản đầu tư đang diễn ra, không chỉ đổi tên
thành “theo dõi thêm”.

## 4. 90-Day Gates — 15 điểm

| ID | Điểm | Điều kiện và cách chấm |
|---|---:|---|
| `GT-30` | 4 | 1đ đúng một learning/validation metric; 1đ ngưỡng số; 1đ evidence vật lý; 1đ `GO` nếu đạt và `FIX/PIVOT/KILL` nếu trượt. |
| `GT-60` | 4 | Tương tự, nhưng metric chính phải là operating metric. |
| `GT-90` | 4 | Tương tự, nhưng metric chính phải là model/economics metric. |
| `GT-KILL` | 3 | Điều kiện đo được 1đ; có số 1đ; có mốc thời gian và tuyên bố dừng 1đ. |

Mỗi cổng chỉ có **một metric gác cổng**. Có thể ghi sample size trong ngưỡng;
không ghép nhiều metric bằng “và/hoặc” nếu chưa định nghĩa một công thức composite.

## 5. Honesty — 5 điểm

Mỗi item đạt được 1 điểm:

- `HO-01`: nêu ít nhất một đèn/giả định thật sự chưa đo được;
- `HO-02`: nêu artifact, log, data, interview hoặc hợp đồng cần để đo;
- `HO-03`: có owner theo vai trò;
- `HO-04`: có ngày ISO hợp lệ để khoảng trống trở thành số;
- `HO-05`: trạng thái nhất quán giữa inventory, dashboard và mục chưa đo được;
  không bịa evidence để lấp ô.

## Cap và override

Cap chỉ giới hạn điểm của **một tiêu chí**, không giới hạn tổng điểm toàn bài:

| ID | Hiệu lực |
|---|---|
| `CAP-TD-WRONG-MODEL` | Chọn sai model rõ ràng → Tier Discipline tối đa 10/20. |
| `CAP-TD-LAGGING-MAJORITY` | Hơn 50% metric ở tầng Lagging → Tier Discipline tối đa 8/20. |
| `CAP-TQ-UNTRACEABLE` | Dùng claim nguồn ngoài không truy vết được để biện minh ngưỡng → Threshold Quality tối đa 10/30. |

Nếu nhiều cap cùng áp dụng, dùng cap thấp nhất. Override:

| ID | Hiệu lực |
|---|---|
| `OVR-DR-VAGUE-THEN` | THÌ chỉ là “xem xét/cân nhắc/theo dõi thêm/đánh giá lại” → luật đó 0 điểm. |
| `OVR-DR-MISSING-FORBIDDEN` | Thiếu hoặc viết sai KHÔNG THÌ → luật đó tối đa 2,5/5. |
| `OVR-GT30-REVENUE` | Metric chính ngày 30 là doanh thu → `GT-30` bằng 0. |
| `OVR-GT-VAGUE` | Cổng không có ngưỡng đo được, ví dụ “có traction tốt” → cổng đó 0. |

## Grade bands

| Band | Điểm |
|---|---:|
| Outstanding | 90–100 |
| Strong | 75–89,5 |
| Pass | 60–74,5 |
| Needs rework | 40–59,5 |
| Fail | 0–39,5 |

## Khi nào bắt buộc human review

- Có ít nhất một verdict `UNCERTAIN`.
- Nguồn không truy cập được hoặc mâu thuẫn với claim.
- Có cap được kích hoạt.
- Tổng cách ranh giới grade band không quá 2 điểm.
- Hai lượt chấm độc lập lệch nhau trên 8 điểm.

Học viên có thể appeal theo **item ID** và chỉ ra evidence anchor hoặc nguồn bị
bỏ sót. Tên và lịch sử điểm không được đưa cho semantic grader nếu có thể chấm
ẩn danh.

## Versioning

Điểm phải lưu kèm rubric version và hash của bài nộp. Nếu rubric thay đổi sau
khi học viên bắt đầu làm bài, lớp tiếp tục dùng version đã công bố cho cohort đó,
trừ khi thay đổi chỉ sửa lỗi không ảnh hưởng điểm.
