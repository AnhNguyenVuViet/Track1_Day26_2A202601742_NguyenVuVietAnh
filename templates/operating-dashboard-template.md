# Operating Dashboard — <TÊN SẢN PHẨM>

> Đây là **worksheet nguồn** để validator và rubric truy vết evidence. Sau khi
> hoàn tất, rút gọn phần vận hành sang
> `templates/one-page-dashboard-template.md`; không ép bảng 12 cột này lên một trang.

- Học viên: <HỌ VÀ TÊN>
- Mã học viên: <MÃ HỌC VIÊN>
- Mô hình: <B2C / B2B / B2B2C>
- Cập nhật: <YYYY-MM-DD>
- North Star: <TÊN ĐÈN VÀ GIÁ TRỊ MỤC TIÊU>

## Chẩn đoán mô hình

<Viết một câu: ai trả tiền, ai dùng, bạn có chạm được người dùng cuối hay không, và vì sao chọn loại này.>

| Dữ liệu đầu vào | Trạng thái | Nằm ở đâu hoặc cần gì để đo | Ngày có số |
|---|---|---|---|
| Unit economics Day 24 | <ĐO ĐƯỢC / TRONG 2 TUẦN / CHƯA BIẾT> | <ĐIỀN> | <YYYY-MM-DD> |
| Value Metric và Cost/Job Day 25 | <ĐO ĐƯỢC / TRONG 2 TUẦN / CHƯA BIẾT> | <ĐIỀN> | <YYYY-MM-DD> |

## Kiểm kê đèn ứng viên

<Mở đúng bảng B2C/B2B/B2B2C trong handbook. Copy từng đèn của bảng đó vào đây và đánh dấu đúng một trạng thái ✅/🔧/❌. B2C cần 8 hàng, B2B 11 hàng, B2B2C 9 hàng; xóa hàng thừa.>

| Đèn ứng viên từ handbook | Tầng | Trạng thái | Bằng chứng hiện có hoặc kế hoạch đo |
|---|---|---|---|
| <ĐIỀN> | <L/O/G> | <✅/🔧/❌> | <FILE/LOG hoặc việc cần làm> |
| <ĐIỀN> | <L/O/G> | <✅/🔧/❌> | <FILE/LOG hoặc việc cần làm> |
| <ĐIỀN> | <L/O/G> | <✅/🔧/❌> | <FILE/LOG hoặc việc cần làm> |
| <ĐIỀN> | <L/O/G> | <✅/🔧/❌> | <FILE/LOG hoặc việc cần làm> |
| <ĐIỀN> | <L/O/G> | <✅/🔧/❌> | <FILE/LOG hoặc việc cần làm> |
| <ĐIỀN> | <L/O/G> | <✅/🔧/❌> | <FILE/LOG hoặc việc cần làm> |
| <ĐIỀN> | <L/O/G> | <✅/🔧/❌> | <FILE/LOG hoặc việc cần làm> |
| <ĐIỀN> | <L/O/G> | <✅/🔧/❌> | <FILE/LOG hoặc việc cần làm> |
| <ĐIỀN> | <L/O/G> | <✅/🔧/❌> | <FILE/LOG hoặc việc cần làm> |
| <ĐIỀN> | <L/O/G> | <✅/🔧/❌> | <FILE/LOG hoặc việc cần làm> |
| <ĐIỀN> | <L/O/G> | <✅/🔧/❌> | <FILE/LOG hoặc việc cần làm> |

## Đèn báo sớm

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| L-01 | <ĐIỀN> | <ĐỊNH NGHĨA + CÔNG THỨC> | <TUẦN · PRODUCT OPS> | <SỐ> | <NGƯỠNG> | <NGƯỠNG> | <NGƯỠNG> | <ĐÚNG MỘT TAG + CHI TIẾT: [BM] tên + URL; [MH] MH-xx; hoặc [TB] kế hoạch baseline> | <YYYY-MM-DD> | <METRIC DOWNSTREAM> | R-01 |
| L-02 | <ĐIỀN> | <ĐỊNH NGHĨA + CÔNG THỨC> | <TUẦN · PRODUCT OPS> | <SỐ> | <NGƯỠNG> | <NGƯỠNG> | <NGƯỠNG> | <ĐÚNG MỘT TAG + CHI TIẾT NGUỒN + LÝ DO> | <YYYY-MM-DD> | <METRIC DOWNSTREAM> | R-02 |

## Đèn vận hành

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| O-01 | <ĐIỀN> | <ĐỊNH NGHĨA + CÔNG THỨC> | <TUẦN · PRODUCT OPS> | <SỐ> | <NGƯỠNG> | <NGƯỠNG> | <NGƯỠNG> | <ĐÚNG MỘT TAG + CHI TIẾT NGUỒN + LÝ DO> | <YYYY-MM-DD> | <METRIC DOWNSTREAM> | R-03 |
| O-02 | Chi phí AI trên mỗi job | <TỔNG TOKEN/INFERENCE COST ÷ SỐ JOB THÀNH CÔNG> | <TUẦN · FINOPS> | <SỐ> | <NGƯỠNG> | <NGƯỠNG> | <NGƯỠNG> | [MH] <MH-01/02 + LÝ DO> | <YYYY-MM-DD> | Gross margin | R-04 |

## Đèn kết quả

| ID | Đèn | Định nghĩa và công thức | Nhịp · Owner | Hiện tại | 🟢 | 🟡 | 🔴 | Nguồn | Ngày kiểm tra | Báo trước cho | Luật |
|---|---|---|---|---:|---|---|---|---|---|---|---|
| G-01 | <ĐIỀN> | <ĐỊNH NGHĨA + CÔNG THỨC> | <THÁNG · FINANCE> | <SỐ> | <NGƯỠNG> | <NGƯỠNG> | <NGƯỠNG> | <ĐÚNG MỘT TAG + CHI TIẾT NGUỒN + LÝ DO> | <YYYY-MM-DD> | <KẾT QUẢ CUỐI> | R-05 |
| G-02 | <ĐIỀN> | <ĐỊNH NGHĨA + CÔNG THỨC> | <QUÝ · FOUNDER> | <SỐ> | <NGƯỠNG> | <NGƯỠNG> | <NGƯỠNG> | <ĐÚNG MỘT TAG + CHI TIẾT NGUỒN + LÝ DO> | <YYYY-MM-DD> | <KẾT QUẢ CUỐI> | R-05 |

## Luật quyết định

| ID | NẾU | TRONG | VÀ | THÌ | KHÔNG THÌ | Luật dừng? |
|---|---|---|---|---|---|---|
| R-01 | <ĐÈN + TOÁN TỬ + NGƯỠNG> | <THỜI GIAN> | <MẪU TỐI THIỂU> | <HÀNH ĐỘNG CỤ THỂ> | <PHẢN XẠ BỊ CẤM> | <CÓ/KHÔNG> |
| R-02 | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <CÓ/KHÔNG> |
| R-03 | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <CÓ/KHÔNG> |
| R-04 | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <CÓ/KHÔNG> |
| R-05 | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <ĐIỀN> | <CÓ/KHÔNG> |

## Cổng gác 90 ngày

| Ngày | Metric gác cổng | Ngưỡng | Bằng chứng vật lý | Nếu đạt | Nếu trượt |
|---:|---|---|---|---|---|
| 30 | <ĐÚNG MỘT METRIC HỌC/VALIDATION> | <SỐ> | <FILE/LOG/REPORT> | GO | <FIX/PIVOT/KILL> |
| 60 | <ĐÚNG MỘT METRIC VẬN HÀNH> | <SỐ> | <FILE/LOG/REPORT> | GO | <FIX/PIVOT/KILL> |
| 90 | <ĐÚNG MỘT METRIC MÔ HÌNH> | <SỐ> | <FILE/LOG/REPORT> | GO | <FIX/PIVOT/KILL> |

## Kill criteria

<Một câu có số và mốc thời gian: khi nào dừng hẳn hướng này.>

## Chưa đo được

| Đèn hoặc giả định | Cần gì để đo | Ai chịu trách nhiệm | Ngày có số |
|---|---|---|---|
| <ĐIỀN NỘI DUNG THẬT> | <LOG/DATA/INTERVIEW/HỢP ĐỒNG> | <VAI TRÒ> | <YYYY-MM-DD> |

## Phụ lục ngưỡng suy từ mô hình

| ID | Metric | Input Day 24–25 | Phép tính | Kết quả và ngưỡng áp dụng |
|---|---|---|---|---|
| MH-01 | <ĐIỀN> | <INPUT CÓ ĐƠN VỊ> | <PHÉP TÍNH CÓ SỐ VÀ DẤU BẰNG> | <KẾT QUẢ + ID ĐÈN ÁP DỤNG> |
| MH-02 | <ĐIỀN KHÁC MH-01> | <INPUT CÓ ĐƠN VỊ> | <PHÉP TÍNH CÓ SỐ VÀ DẤU BẰNG> | <KẾT QUẢ + ID ĐÈN ÁP DỤNG> |

## Ghi nhận AI critique

| Phản biện | Chấp nhận hay bác bỏ | Thay đổi đã thực hiện | Lý do |
|---|---|---|---|
| <ĐIỀN TỐI ĐA 3 Ý> | <CHẤP NHẬN/BÁC BỎ> | <ĐIỀN> | <ĐIỀN> |
