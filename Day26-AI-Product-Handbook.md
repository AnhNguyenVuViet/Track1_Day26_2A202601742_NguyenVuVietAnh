# Day 26 — Sổ tay học viên

## Đèn nào bật trước?

### Vận hành theo loại mô hình — B2C · B2B · B2B2C

> **Startup không chết vì thiếu metric. Startup chết vì canh nhầm metric.**
> Mỗi loại mô hình có một cái đèn bật trước tiên. Canh nhầm đèn thì lúc biết đã quá muộn để cứu.

---

## 0. Cách dùng sổ tay này

Sổ tay này **không phải để đọc hết một lượt**. §2 đọc trước Lab 10 phút. §3 chỉ đọc **đúng một phần** — phần của loại mô hình bạn đang làm. §4 mở ra khi bắt đầu Lab.

| Khi bạn cần… | Mở phần… |
|---|---|
| Hiểu mạch logic tổng thể của Day 26 | §1 |
| Học hệ chẩn đoán (3 tầng · thẻ đèn · ngưỡng · luật quyết định) | §2 |
| **Lấy bảng điều khiển của riêng loại mình** | §3.1 (B2C) · §3.2 (B2B) · §3.3 (B2B2C) |
| Làm bài — 5 trạm, có bấm giờ | §4 |
| Chạy AI phản biện dashboard của mình | §5 |
| Biết output nào phải có ở mỗi mốc | §6 |
| Xem tiêu chí chấm điểm & cách nộp | §7 |
| Tra nguồn của mọi con số trong tài liệu | §8 |

**Quy ước ngôn ngữ.** Tiếng Việt ưu tiên. Các **term, công thức, prompt** giữ tiếng Anh để chuẩn ngành và không lệch nghĩa khi làm việc với AI.

**Quy ước số liệu.** Mọi benchmark trong sổ tay đều **có nguồn ở §8**, **chốt ngày 27/08/2026**. Mục có ⏳ là số liệu thay đổi nhanh — kiểm tra lại trước khi dùng. Mục có ⚠️ là số liệu **mình cố ý không tin hoàn toàn** và có ghi rõ lý do.

**Không có file Excel.** §3 in sẵn khung bảng để bạn copy sang Google Sheets / Excel / giấy. Đây là chủ ý: Day 24 và Day 25 đã luyện Excel đủ rồi. Day 26 luyện thứ khác — **đọc tín hiệu và ra quyết định**.

**Repo thực hành.** Template nguồn, mẫu dashboard một trang, validator và rubric
công khai nằm tại https://github.com/TuNM17421/Day26-Operating-Dashboard-Lab.
Worksheet nguồn giữ đủ evidence để chấm; chỉ bản rút gọn mới được ép vào trang 1 PDF.

**Một điều cần nói trước.** Sổ tay này có ba bảng điều khiển. Bạn **chỉ dùng một**. Đừng đọc cả ba rồi trộn lại — dashboard trộn ba loại là dashboard không dùng được cho loại nào.

---

## 1. Mạch logic Day 26

### Bạn đang ở đâu

| Buổi | Cho bạn cái gì |
|---|---|
| **Day 24** | Mô hình tài chính: LTV, CAC, LTV/CAC, CAC payback, NPV, IRR, 3 scenario |
| **Day 25** | Value Metric, Cost/Job, giá sàn/trần, 1 kênh, Pain Moment, Evidence Pack |
| **Day 26** | **Bộ đồng hồ để lái cái mô hình đó — và luật để biết khi nào phải bẻ lái** |

### Sự thật khó chịu về Day 24

Mở lại file Excel Day 24 của bạn và nhìn danh sách chỉ số: **LTV · CAC · LTV/CAC · Gross Margin · NPV · IRR · Payback**.

Bảy chỉ số. **Cả bảy đều là chỉ số kết quả.** Chúng chỉ đúng khi mọi chuyện đã xảy ra xong.

- LTV cần khách ở lại đủ lâu mới tính được → biết sau **6–12 tháng**
- CAC payback cần đủ một chu kỳ hoàn vốn → biết sau **nhiều tháng**
- NPV/IRR là kết quả của cả dự án → biết sau **nhiều năm**

Không có gì sai với những chỉ số đó. Chúng là **bảng điểm**. Vấn đề là bạn **không lái xe bằng bảng điểm** — bảng điểm nói bạn đã thắng hay thua, không nói bạn nên rẽ trái hay phải trong ba tuần tới.

> **Day 26 bổ sung đúng chỗ đó: những chiếc đèn bật *trước*, và luật để biết phải làm gì khi đèn đỏ.**

### Ba câu hỏi Day 26 trả lời

```
Câu 1: ĐÈN NÀO?      → loại mô hình của tôi phải canh những chỉ số nào,
                        ngoài những gì Day 24–25 đã dạy?
            ↓
Câu 2: NGƯỠNG NÀO?   → bao nhiêu là tốt, bao nhiêu là báo động,
                        bao nhiêu là đang chết? Dựa vào đâu mà nói vậy?
            ↓
Câu 3: RỒI SAO?      → đèn đỏ thì làm gì — và quan trọng hơn,
                        KHÔNG được làm gì?
```

**Và câu thứ tư, dành cho 90 ngày tới:** cổng gác nào ở ngày 30, 60, 90 — và ở mỗi cổng, tiếp tục hay dừng?

### Bốn khối và đầu ra

| Khối | Nội dung | Output của bạn |
|---|---|---|
| **1. Hệ chẩn đoán** | 3 tầng tín hiệu · thẻ đèn · nguồn của ngưỡng · cấu trúc luật quyết định | Hiểu cách đọc bất kỳ dashboard nào |
| **2. Bảng điều khiển theo loại** | B2C · B2B · B2B2C — mỗi loại một bộ đèn riêng | Bộ đèn của **riêng bạn** |
| **3. Luật quyết định** | Viết luật dạng NẾU–TRONG–THÌ–KHÔNG THÌ | 5 luật dùng được ngay |
| **4. 90 ngày & cổng gác** | Trận đánh đầu tiên khác nhau theo loại | 3 cổng gác + kill criteria |

**Đầu ra cuối cùng: `Operating Dashboard` — 1 trang.** Đủ để dán lên tường và họp tuần nhìn vào đó.

---

## 2. Hệ chẩn đoán

Năm khái niệm. Đọc lướt 10 phút trước Lab, quay lại tra khi làm bài.

---

### 2.1 Ba tầng tín hiệu

Mọi chỉ số của một sản phẩm đều rơi vào một trong ba tầng, phân biệt bằng **độ trễ** — khoảng cách giữa lúc thực tế thay đổi và lúc con số phản ánh điều đó.

```
TẦNG 1 · LEADING     đổi theo NGÀY / TUẦN
         ĐÈN BÁO SỚM  báo trước 1–3 tháng · ít người đo · đây là chỗ Day 26 tập trung
              │
              ▼
TẦNG 2 · OPERATING   đổi theo TUẦN / THÁNG
         ĐÈN VẬN HÀNH đây là thứ bạn thực sự KÉO được · đòn bẩy nằm ở đây
              │
              ▼
TẦNG 3 · LAGGING     đổi theo THÁNG / QUÝ / NĂM
         ĐÈN KẾT QUẢ  LTV · CAC payback · NPV · IRR — Day 24 dạy toàn tầng này
```

**Quy tắc đọc:** một chỉ số ở tầng trên **luôn** báo trước cho một chỉ số cụ thể ở tầng dưới. Nếu bạn không chỉ được ra "đèn này báo trước cho đèn nào", thì đó không phải leading indicator — đó chỉ là **một con số bạn thích nhìn**.

| | Leading | Operating | Lagging |
|---|---|---|---|
| **Ví dụ (B2C)** | Activation rate | Trial→paid | LTV |
| **Ví dụ (B2B)** | Time-to-first-value | Sales cycle | NRR |
| **Ví dụ (B2B2C)** | Partner activation | Volume/partner | GM sau rev-share |
| **Đo được sau** | vài ngày | vài tuần | vài quý |
| **Sửa được không** | Rất dễ | Được, tốn công | Gần như không — chỉ chờ |
| **Ai nhìn** | Bạn, hằng ngày | Đội, hằng tuần | Sếp/nhà đầu tư, hằng quý |

> **Bẫy phổ biến nhất trong lớp này:** dashboard toàn đèn tầng 3. Nhìn rất chuyên nghiệp, hoàn toàn vô dụng để lái. Nếu dashboard của bạn chỉ có doanh thu, LTV/CAC và GM — bạn đang lái xe bằng gương chiếu hậu.

---

### 2.2 Thẻ đèn — cấu trúc một chỉ số dùng được

Một chỉ số chỉ dùng được khi có đủ **6 trường**. Thiếu bất kỳ trường nào thì nó là *thông tin*, không phải *công cụ*.

| # | Trường | Câu hỏi kiểm tra |
|---|---|---|
| 1 | **Tên & định nghĩa chặt** | Đếm cái gì? Và **không** đếm cái gì? |
| 2 | **Công thức** | Tử số, mẫu số chính xác là gì? |
| 3 | **Nhịp đo** | Ngày / tuần / tháng? Ai lấy số? |
| 4 | **Ngưỡng 🟢 🟡 🔴** | Bao nhiêu là ổn, cảnh báo, nguy? **Dựa vào đâu?** |
| 5 | **Báo trước cho đèn nào** | Đèn tầng dưới nào sẽ xấu theo? |
| 6 | **Đỏ thì làm gì** | Link tới một luật quyết định cụ thể |

**Ví dụ một thẻ đèn hoàn chỉnh:**

| Trường | Nội dung |
|---|---|
| Tên | **Partner Activation Rate** |
| Định nghĩa | % partner đã ký hợp đồng mà có **≥1 end-user thật** phát sinh trong 30 ngày kể từ ngày go-live. **Không** tính user test nội bộ của partner. |
| Công thức | (Số partner có ≥1 end-user thật) ÷ (Số partner đã go-live) |
| Nhịp đo | Hằng tuần · Product Operations |
| Ngưỡng | 🟢 ≥60% · 🟡 30–60% · 🔴 <30% |
| Báo trước cho | Doanh thu/partner (tầng 2) → GM sau rev-share (tầng 3) |
| Đỏ thì làm gì | Luật B2B2C-1: dừng ký partner mới |

> **Trường số 1 quan trọng hơn bạn nghĩ.** Day 25 đã chỉ ra Intercom và Zendesk bỏ rất nhiều công sức để định nghĩa chính xác *cái gì được tính là một resolution*. Cùng logic: "user hoạt động" nghĩa là gì — mở app? làm xong một việc? quay lại lần hai? Ba định nghĩa cho ba con số khác nhau, và bạn sẽ ra ba quyết định khác nhau.

---

### 2.3 Ngưỡng đến từ đâu

Đây là phần bị làm ẩu nhiều nhất. Một ngưỡng chỉ hợp lệ khi đến từ **một trong ba nguồn**:

| # | Nguồn | Dùng khi | Ví dụ |
|---|---|---|---|
| **1** | **Benchmark có nguồn công bố** | Có dữ liệu ngành đáng tin | Retention M12 của app AI = **21,1%** (RevenueCat, 03/2026) |
| **2** | **Số lịch sử của chính bạn** | Đã chạy được ≥2 chu kỳ | "Baseline activation của tôi là 34%, mục tiêu quý này 45%" |
| **3** | **Suy ra từ mô hình Day 24–25** | Chưa có dữ liệu, nhưng có mô hình | "CAC payback phải <12 tháng → với ARPU và GM này, CAC tối đa là X" |

Và **một nguồn không hợp lệ**: cảm giác. *"Chắc 20% là ổn"* không phải là ngưỡng — đó là một điều ước.

> **Ngưỡng suy từ mô hình là nguồn mạnh nhất mà ít người dùng.** Bạn đã có Cost/Job (Day 25) và LTV/CAC (Day 24). Từ đó suy ngược ra được ngưỡng cho gần như mọi đèn tầng 1 và tầng 2. Ví dụ: nếu mô hình chỉ sống khi khách ở lại ≥10 tháng, thì retention M3 phải ≥ một mức nhất định — mức đó **tính ra được**, không cần đoán.

**Ba mức màu, và ý nghĩa hành động của chúng:**

| Màu | Ý nghĩa | Hành động |
|---|---|---|
| 🟢 **Xanh** | Đang ổn | Không làm gì. Đừng sửa cái đang chạy. |
| 🟡 **Vàng** | Chưa chết nhưng xu hướng xấu | Điều tra. Đặt hạn: 2 tuần sau phải có câu trả lời. |
| 🔴 **Đỏ** | Luật quyết định kích hoạt | Làm đúng cái đã viết sẵn. **Không** bàn lại từ đầu. |

Lý do phải viết luật **trước khi** đèn đỏ: lúc đèn đỏ là lúc bạn hoảng, và người hoảng thì ra quyết định tệ.

---

### 2.4 Luật quyết định

Đây là sản phẩm chính của Day 26. Một luật quyết định có **năm phần**:

```
NẾU        <đèn>  <toán tử>  <ngưỡng>
TRONG      <khoảng thời gian>            ← chống phản ứng với nhiễu
VÀ         <điều kiện mẫu đủ lớn>        ← chống kết luận từ 3 data point
THÌ        <hành động cụ thể>            ← động từ, không phải "xem xét"
KHÔNG THÌ  <hành động bị cấm>            ← chống phản xạ sai
```

**Ví dụ đạt:**

> **NẾU** đường cong retention chưa phẳng sau D30
> **TRONG** 2 cohort liên tiếp
> **VÀ** mỗi cohort ≥200 user
> **THÌ** đóng băng toàn bộ chi tiêu acquisition, cả đội quay về làm activation trong 3 tuần
> **KHÔNG THÌ** không được tăng ngân sách ads để bù churn

**Ví dụ không đạt:**

> *"Nếu retention thấp thì xem xét lại sản phẩm."*

Sai ở bốn chỗ: "thấp" là bao nhiêu, "xem xét lại" là làm gì, đo trong bao lâu, và không cấm phản xạ sai nào cả.

#### Vì sao bắt buộc phải có vế "KHÔNG THÌ"

Vì phản xạ đầu tiên của con người khi thấy số xấu **thường là phản xạ sai** — và nó sai theo cách rất dự đoán được:

| Loại | Đèn đỏ | Phản xạ tự nhiên | Vì sao sai |
|---|---|---|---|
| **B2C** | Retention rớt | Đổ thêm tiền ads | Đổ nước vào thùng thủng — CAC tăng, LTV không đổi, chết nhanh hơn |
| **B2B** | Pipeline mỏng | Giảm giá | Deal B2B hiếm khi chết vì giá; nó chết vì khách không thấy giá trị đủ nhanh |
| **B2B2C** | Doanh thu chững | Ký thêm partner | Partner cũ còn chưa activate; thêm partner = thêm chi phí, không thêm doanh thu |

> **Trong Lab, ít nhất 2 trong 5 luật của bạn phải là luật *dừng làm gì đó*.** Luật khó viết nhất và có giá trị nhất luôn là luật bảo bạn **ngừng** một việc đang làm.

---

### 2.5 Đèn nào bật trước — theo loại

Đây là bản lề của cả buổi học. Mỗi loại mô hình có **một** đèn bật trước tất cả những đèn khác. Không phải vì các đèn kia không quan trọng, mà vì đèn này **sai thì mọi đèn khác đều vô nghĩa**.

| Loại | Đèn bật trước | Vì sao là nó | Nếu bỏ qua |
|---|---|---|---|
| **B2C** | **Đường cong retention có phẳng không** | Chi phí biên của AI không về 0 (Day 25 §2.1) → mỗi user giữ lại phải **tự trả tiền token của mình**. Không phẳng ⇒ không có LTV ⇒ mọi số Day 24 là ảo | Bạn sẽ tăng trưởng user rất đẹp trong 6 tháng rồi phát hiện không có ai ở lại |
| **B2B** | **Time-to-first-value (TTFV)** | Deal B2B hiếm khi chết ở bàn đàm phán giá. Nó chết ở **khoảng trống giữa lúc ký và lúc khách thấy giá trị** | Bạn sẽ có logo đẹp trên website và churn năm đầu rất cao |
| **B2B2C** | **Partner activation rate** | **Ký hợp đồng không phải là thắng.** Partner "ký cho có" là cái chết chậm — bạn báo cáo 12 partner, doanh thu thật đến từ 2 | Bạn sẽ đếm partner thay vì đếm doanh thu, trong 2 quý liền |

> Ba câu này là ba câu cần nhớ nếu bạn quên hết mọi thứ khác của Day 26.

**Cách xác định bạn thuộc loại nào** — ba câu hỏi, trả lời theo **thực tế hôm nay**, không theo kế hoạch năm sau:

1. **Ai trả tiền cho bạn?** Cá nhân → B2C. Doanh nghiệp → B2B hoặc B2B2C.
2. **Ai dùng sản phẩm?** Chính người trả tiền → B2B. Khách hàng *của* người trả tiền → B2B2C.
3. **Nếu là B2B2C: bạn có chạm được người dùng cuối không?** Không chạm được, không có dữ liệu của họ, không có thương hiệu trước mặt họ → bạn đang là **nhà cung cấp cho một doanh nghiệp**, dùng bảng B2B. Đó không phải hạ cấp — đó là chẩn đoán đúng.

---

### 2.6 Nhịp vận hành — ai nhìn cái gì, bao lâu một lần

Dashboard không có nhịp là dashboard chết. Bốn nhịp:

| Nhịp | Nhìn tầng nào | Ai | Câu hỏi |
|---|---|---|---|
| **Hằng ngày** (5 phút) | 1–2 đèn leading | Bạn | Có gì gãy đột ngột không? |
| **Hằng tuần** (30 phút) | Toàn bộ leading + operating | Cả đội | Đèn nào chuyển màu? Luật nào kích hoạt? |
| **Hằng tháng** | Operating + lagging | Đội + cố vấn | Giả định nào trong mô hình Day 24 đã sai? |
| **Mỗi 30 ngày** | Cổng gác (§2.7) | Bạn + người ngoài | Go / Fix / Pivot / Kill? |

> **Quy tắc chống tự lừa:** người báo cáo con số không nên là người đặt ngưỡng cho con số đó. Nếu đội chỉ có bạn, hãy nhờ **một người ngoài** dự cuộc họp cổng gác — Day 25 đã dạy rằng bằng chứng viết ra mới có giá trị; điều đó cũng đúng khi người đọc bằng chứng là chính bạn.

---

### 2.7 Cổng gác 90 ngày

Mỗi 30 ngày là một cổng. Ở mỗi cổng có **đúng bốn** lựa chọn — không có lựa chọn "cứ để thêm một tháng nữa xem sao":

| Quyết định | Khi nào | Nghĩa là |
|---|---|---|
| **GO** | Metric gác cổng đạt ngưỡng | Sang chặng sau, tăng đầu tư |
| **FIX** | Chưa đạt nhưng **biết rõ vì sao** | Ở lại chặng này thêm 30 ngày, sửa đúng một thứ |
| **PIVOT** | Chưa đạt và **giả định gốc đã sai** | Đổi phân khúc / đổi loại mô hình / đổi value metric (Day 25) |
| **KILL** | Chưa đạt, đã FIX một lần, vẫn không nhúc nhích | Dừng. Tiền và thời gian còn lại đem đi chỗ khác |

**FIX chỉ được dùng một lần cho cùng một vấn đề.** FIX lần thứ hai cho cùng một metric chính là PIVOT đang giả trang.

---

### 2.8 Ba lời cảnh báo về số liệu

Giữ đúng thói quen Day 25: nói rõ cái gì có nguồn, cái gì không.

**① Không tồn tại bộ benchmark nào chia theo loại mô hình.** Mình đã rà ICONIQ, Bessemer, Benchmarkit, Menlo, a16z. Tất cả đều chia theo **quy mô doanh thu** hoặc **tốc độ tăng trưởng** — **không ai chia theo B2C / B2B / B2B2C**. Nghĩa là: các ngưỡng trong §3 là **tổng hợp từ nhiều nguồn khác nhau**, không phải một bảng chuẩn có sẵn. Ai đưa cho bạn một bảng "benchmark theo archetype" trọn gói thì gần như chắc chắn họ đang bịa.

**② Benchmark ngành là điểm bắt đầu, không phải mục tiêu.** Retention M12 của app AI là 21,1% — đó là **trung vị của một ngành đang chật vật**, không phải mức bạn nên nhắm tới. Dùng nó để biết mình đang ở đâu so với mặt bằng, rồi đặt mục tiêu riêng.

**③ Ba con số bạn sẽ nghe rất nhiều và nên cẩn thận** — chi tiết ở §8.4: *"95% pilot AI thất bại"* · *"OpenAI lỗ trên gói $200"* · *"gross margin công ty AI là 50–60%"*.

---
## 3. Ba bảng điều khiển

**Chỉ đọc phần của bạn.** Nếu chưa chắc mình thuộc loại nào, quay lại §2.5 trả lời ba câu hỏi trước.

**Ký hiệu nguồn của ngưỡng** — dùng thống nhất trong cả ba bảng:

| Ký hiệu | Nghĩa | Bạn phải làm gì |
|---|---|---|
| **[BM]** | Benchmark có nguồn công bố (§8) | Dùng được ngay, nhưng ghi ngày kiểm tra |
| **[MH]** | Suy ra từ mô hình Day 24–25 của bạn | **Tự tính lại bằng số của bạn** — con số ở đây chỉ là ví dụ |
| **[TB]** | Chưa có chuẩn ngành — tự đặt baseline | Đo 2 chu kỳ, lấy đó làm mốc, rồi đặt mục tiêu cải thiện |

---

### 3.1 B2C — trận đánh **giữ chân**

> **Trận đánh đầu tiên của bạn không phải là tăng trưởng. Là giữ chân.**
> Với sản phẩm AI, mỗi user ở lại đều **tốn tiền token mỗi tháng**. Một user không trả tiền mà dùng nhiều là một khoản lỗ định kỳ, không phải một "tiềm năng".

#### Ba biến Day 24–25 chưa bắt bạn tính

| # | Biến | Vì sao Day 24 bỏ sót | Ảnh hưởng |
|---|---|---|---|
| **1** | **Chi phí inference của user KHÔNG trả tiền** | Day 24 tính COGS trên khách trả tiền. B2C AI đốt token cho **toàn bộ** free tier | Free tier không có trần = lỗ tăng tuyến tính theo tăng trưởng |
| **2** | **Đuôi power user (p95, không phải trung bình)** | Day 25 đã kể "câu chuyện buffet" nhưng chưa bắt đo | 5–10% user nặng có thể ăn hết biên của 90% còn lại |
| **3** | **Hình dạng đường cong retention** | Day 24 giả định "số tháng ở lại" là một con số | Nếu đường cong **không phẳng**, không tồn tại "số tháng ở lại" — LTV là hư cấu |

> **Biến số 3 là biến quan trọng nhất trong cả Day 26 nếu bạn làm B2C.** LTV trong Excel Day 24 của bạn được tính bằng `ARPU × GM × số tháng ở lại`. Công thức đó **chỉ có nghĩa khi đường cong retention phẳng ra ở một mức nào đó**. Nếu nó vẫn đang dốc xuống ở tháng thứ 6, thì "số tháng ở lại" không hội tụ, và LTV bạn điền vào ô đó là một con số bạn tự nghĩ ra.

#### Bảng đèn B2C

| Tầng | Đèn | Công thức / định nghĩa | Nhịp | 🟢 | 🟡 | 🔴 | Nguồn |
|---|---|---|---|---|---|---|---|
| **L** | **Đường cong retention có phẳng không** ⭐ | % user cohort còn hoạt động ở D1 / D7 / D30 / D60 — vẽ thành đường | Tuần | Phẳng từ D30 | Phẳng từ D60 | Chưa phẳng ở D60 | [TB] |
| **L** | **Activation rate** | % user chạm "aha moment" trong 24h đầu. Bạn phải tự định nghĩa aha moment là hành động nào | Ngày | ≥ baseline +30% | quanh baseline | < baseline | [TB] |
| **L** | **p95 cost/user/tháng ÷ ARPU** | Lấy user ở phân vị 95 về chi phí, không lấy trung bình | Tuần | <0,30 | 0,30–0,60 | >0,60 | [MH] |
| **O** | **Trial → paid** | % user dùng thử chuyển sang trả tiền | Tháng | ≥8,5% | 5–8,5% | <5% | [BM] app AI = **8,5%**; non-AI 5,6% |
| **O** | **Retention M12** | % user còn trả tiền sau 12 tháng | Tháng | ≥30% | 21–30% | <21% | [BM] app AI = **21,1%**; non-AI 30,7% |
| **O** | **Chi phí free tier ÷ tổng COGS** | Tổng token đốt cho user miễn phí | Tháng | <20% | 20–40% | >40% | [MH] |
| **O** | **Tỷ lệ refund** | | Tháng | <3,5% | 3,5–4,2% | >4,2% | [BM] app AI = **4,2%** |
| **G** | LTV/CAC · CAC payback · GM | Day 24 | Quý | ≥3 · <12 tháng | | <3 · >12 tháng | Day 24 |

*(L = Leading · O = Operating · G = Lagging)*

#### Hai cái đèn gần như không ai bật

**① p95, không phải trung bình.** Nếu bạn chỉ nhìn chi phí trung bình mỗi user, bạn sẽ không bao giờ thấy được cái làm bạn lỗ. Phân phối chi phí trong sản phẩm AI **lệch rất mạnh**: phần lớn user dùng ít, một nhóm nhỏ dùng gấp 20–50 lần. Trung bình có thể trông rất đẹp trong khi 5% user nặng đang ăn sạch biên.

Đây chính là điều Sam Altman mô tả khi nói OpenAI **lỗ trên gói $200/tháng** vì *"người ta dùng nhiều hơn chúng tôi tưởng rất nhiều"* (01/2025 — xem cảnh báo ở §8.4 về việc con số này đã cũ). Và đó cũng là lý do GitHub Copilot bỏ mô hình cũ để chuyển sang AI Credits đo theo token từ 01/06/2026 (Day 25 §2.3).

Hành động khi đèn này đỏ **không phải** tăng giá đại trà — mà là **tách gói** hoặc **đặt trần usage**, đúng như Day 25 đã dạy về Hybrid pricing.

**② Trần chuyển đổi thật sự là bao nhiêu.** Nhiều mô hình tài chính B2C giả định 15–20% người dùng sẽ trả tiền. Đối chiếu thực tế:

| Mốc | Con số | Nguồn |
|---|---|---|
| Toàn thị trường AI tiêu dùng | **~3%** người dùng trả tiền | Menlo, 06/2025 |
| ChatGPT | **~5%** weekly active → paid | Menlo (ước tính), 06/2025 |
| **Duolingo** — best-in-class có kiểm toán | **9,0%** (12,7M paid / 140,6M MAU) | Báo cáo Q2 2026, 05/08/2026 |

> **Nếu mô hình Day 24 của bạn giả định conversion cao hơn 9%, bạn đang giả định mình giỏi hơn Duolingo.** Có thể đúng — nhưng phải viết ra lý do.

#### Năm luật quyết định B2C

> **B2C-1 · Luật dừng** — NẾU đường cong retention chưa phẳng sau D30, TRONG 2 cohort liên tiếp, VÀ mỗi cohort ≥200 user, THÌ **đóng băng toàn bộ chi tiêu acquisition trong 3 tuần và cả đội quay về làm activation**. KHÔNG THÌ **không được tăng ngân sách ads để bù churn**.

> **B2C-2** — NẾU p95 cost/user > 60% ARPU, TRONG 1 tháng, THÌ **đặt trần usage cho gói hiện tại hoặc tách một gói riêng cho power user** (Day 25 §2.4 — Hybrid). KHÔNG THÌ **không tăng giá đại trà** — bạn sẽ mất 90% user nhẹ để cứu biên do 10% user nặng gây ra.

> **B2C-3** — NẾU trial→paid < 5%, TRONG 3 lần lặp paywall khác nhau, THÌ **vấn đề nằm ở activation hoặc value metric, không nằm ở giá** → quay lại Day 25 §2.3 chọn lại đơn vị tính tiền. KHÔNG THÌ **không giảm giá** — giảm giá trên một sản phẩm chưa tạo được thói quen chỉ làm hỏng luôn cả neo giá.

> **B2C-4 · Luật dừng** — NẾU chi phí free tier > 40% tổng COGS, TRONG 2 tháng, THÌ **giới hạn free tier ngay trong sprint tới** (giảm quota, hạ model, hoặc yêu cầu đăng nhập). KHÔNG THÌ **không mở rộng free tier để tăng trưởng nhanh hơn**.

> **B2C-5 · Luật chuyển hướng** — NẾU retention M12 < 21% VÀ LTV/CAC < 2, SAU 2 quý đã FIX một lần, THÌ **cân nhắc bán cho tổ chức thay vì cá nhân** — trường học, doanh nghiệp, hiệp hội (xem "đường thoát" bên dưới). KHÔNG THÌ **không chạy thêm một vòng tối ưu funnel nữa** — funnel không cứu được sản phẩm không có thói quen.

#### Chiến lược B2C

**Đòn bẩy duy nhất thật sự là `retention × chi phí biên`.** Mọi thứ khác — CAC, viral, paywall — chỉ khuếch đại kết quả của hai biến này. Retention tốt + chi phí biên thấp thì mọi việc khác dễ. Ngược lại thì không có chiến thuật acquisition nào cứu được.

**Ba đường thoát khi đường cong không chịu phẳng:**

| Đường thoát | Làm gì | Đánh đổi | Có thật ai làm chưa |
|---|---|---|---|
| **Thu hẹp** | Cắt use case đến đúng chỗ có thói quen sẵn — mỗi ngày, không phải mỗi tháng | Thị trường nhỏ lại | Rất phổ biến, ít ai kể |
| **Đổi người trả tiền** | Vẫn phục vụ người dùng đó, nhưng bán cho **tổ chức** của họ | Chu kỳ bán dài hơn, cần Evidence Pack (Day 25) | **ELSA Speak**: từ app cá nhân → bán cho trường học và doanh nghiệp (IDP, YOLA, Kimberly-Clark, Intel) · **Grammarly** → business |
| **Đổi đơn vị tính tiền** | Từ thuê bao cố định → usage/credit, để chi phí đi cùng doanh thu | Doanh thu khó dự đoán hơn | **GitHub Copilot** chuyển sang AI Credits (06/2026) · **Notion** thêm lớp credits |

> **Đổi hướng không phải thất bại.** OpenAI vào năm 2026 với tỷ lệ doanh thu 60 consumer / 40 enterprise; đến **08/2026 doanh thu enterprise đã vượt consumer** — sớm hơn dự báo của chính họ hai quý. Công ty tiêu dùng AI lớn nhất thế giới cũng đang dịch chuyển về phía tổ chức.

#### Cổng gác 90 ngày — B2C

| Cổng | Metric gác cổng | Ngưỡng qua cổng |
|---|---|---|
| **Ngày 30** | Đã định nghĩa xong aha moment + có baseline activation + cohort đầu tiên đủ mẫu | Có số, không phải có kế hoạch lấy số |
| **Ngày 60** | Đường cong retention D30 | Phẳng, hoặc dốc giảm rõ rệt so với cohort trước |
| **Ngày 90** | Trial→paid ≥5% **và** p95 cost/ARPU <0,6 | Cả hai, không phải một |

---
### 3.2 B2B — trận đánh **rút ngắn đường tới giá trị**

> **Deal B2B hiếm khi chết ở bàn đàm phán giá. Nó chết ở khoảng trống giữa lúc ký và lúc khách thấy giá trị.**
> Ký được là phần dễ. Làm cho khách dùng thật, trong 30 ngày, mới là phần quyết định bạn có năm thứ hai hay không.

#### Ba biến Day 24–25 chưa bắt bạn tính

| # | Biến | Vì sao Day 24 bỏ sót | Ảnh hưởng |
|---|---|---|---|
| **1** | **Chi phí triển khai mỗi khách** | Day 24 gộp vào "R&D & Salaries" | Đây là cục **không scale**. Mỗi khách mới tốn lại gần như đúng chừng đó công |
| **2** | **Ai gánh hoá đơn token** | Day 25 §2.4 có nhắc, chưa bắt đo | ICONIQ 2026: **84%** công ty đẩy ít nhất một phần hoá đơn token sang khách; chỉ **15%** tự gánh 100%. Nếu bạn ở nhóm 15%, **GM của bạn phụ thuộc hành vi của khách**, không phụ thuộc bạn |
| **3** | **Chu kỳ bán so với runway** | Day 24 tính runway; Day 25 tính CAC — nhưng không ai ghép hai cái lại | Chu kỳ bán **~19 tuần** nghĩa là tiền mặt về sau ~5 tháng kể từ lúc bắt đầu bán. Runway 6 tháng + chu kỳ bán 5 tháng = bạn **không có** 6 tháng, bạn có 1 |

> **Ghép biến 3 với Day 24 ngay hôm nay.** Mở lại ô Runway trong Excel Day 24 của bạn và trừ đi độ dài chu kỳ bán. Con số còn lại mới là thời gian bạn thực sự có để chứng minh mô hình.

#### Bảng đèn B2B

| Tầng | Đèn | Công thức / định nghĩa | Nhịp | 🟢 | 🟡 | 🔴 | Nguồn |
|---|---|---|---|---|---|---|---|
| **L** | **Time-to-first-value (TTFV)** ⭐ | Số ngày từ ký hợp đồng đến lần đầu khách nhận **giá trị đo được** (không phải "đã cài xong") | Mỗi khách | <30 ngày | 30–60 | >60 | [TB] tự đặt, xem ghi chú |
| **L** | **Pipeline coverage** | Giá trị pipeline ÷ target quý | Tuần | ≥3× | 2–3× | <2× | [TB] quy ước ngành ⚠️ |
| **L** | **% deal chết ở khâu security/procurement** | | Tháng | <10% | 10–20% | >20% | [TB] |
| **O** | **POC → paid** | % pilot/POC chuyển thành hợp đồng trả tiền | Quý | ≥50% | 35–50% | <35% | [BM] **~50%** (2026), ~36% (2025) |
| **O** | **Sales cycle (ngày)** | Từ cơ hội đủ điều kiện → chữ ký | Quý | <19 tuần | 19–24 tuần | >24 tuần | [BM] TB **~19 tuần**; deal $100K+ ~**24 tuần** |
| **O** | **Usage depth trong tài khoản** | % seat / workflow đã mua thực sự hoạt động hằng tuần | Tuần | ≥60% | 30–60% | <30% | [TB] |
| **O** | **Chi phí triển khai ÷ ACV** | | Mỗi khách | <15% | 15–30% | >30% | [MH] |
| **O** | **Tập trung doanh thu** | % doanh thu từ khách lớn nhất | Tháng | <20% | 20–30% | >30% | [TB] |
| **G** | **NRR** | Net Revenue Retention | Quý | ≥110% | 100–110% | <100% | [BM] trung vị SaaS **101%**, GRR 88% |
| **G** | **Gross Margin** | | Quý | ≥55% | 45–55% | <45% | [BM] AI-native **45%** (2025) → **53%** (2026E) |
| **G** | CAC payback | Day 24 | Quý | SMB<12 · MM<18 · ENT<24 tháng | | vượt ngưỡng phân khúc | [BM] |

> ⚠️ **Về ngưỡng pipeline coverage 3×:** đây là **quy ước rất phổ biến trong nghề sales**, nhưng mình **không tìm được một nguồn công bố chuẩn** cho con số này. Dùng nó như điểm khởi đầu, rồi thay bằng win rate thật của bạn: `coverage cần thiết = 1 ÷ win rate`. Win rate 25% → cần 4×, không phải 3×.

#### Hai cái đèn gần như không ai bật

**① TTFV — đèn báo trước cả win rate lẫn churn năm đầu.**

Hầu hết đội B2B đo *sales cycle* (trước khi ký) và *churn* (sau một năm) nhưng bỏ trống khoảng ở giữa. Đó lại đúng là chỗ deal chết.

TTFV báo trước **hai** thứ khác nhau:
- **Ngược lên trên:** khách đang trong POC nói chuyện với nhau. Nếu triển khai của bạn nổi tiếng là chậm, win rate của những deal sau sẽ giảm mà bạn không biết vì sao.
- **Xuôi xuống dưới:** khách không thấy giá trị trong 60 ngày đầu thì gần như chắc chắn không gia hạn — và bạn chỉ phát hiện điều đó **11 tháng sau**.

Với sản phẩm AI, TTFV có xu hướng **dài hơn** SaaS truyền thống vì cần dữ liệu của khách, cần tích hợp, cần một vòng tinh chỉnh chất lượng. Đó là lý do bạn phải đo nó chứ không giả định nó giống SaaS.

**Cách rút ngắn TTFV không phải làm nhanh hơn — mà là cắt phạm vi pilot nhỏ lại.** Đây chính là kỹ năng "thin slice" từ Day 16–17: một use case, một đội, một chỉ số. Pilot toàn công ty nghe hoành tráng và chết ở tháng thứ ba.

**② Chi phí triển khai ÷ ACV — đèn nói bạn là công ty sản phẩm hay công ty dịch vụ.**

Nếu bạn tốn hơn 30% ACV để đưa một khách vào vận hành, và tỷ lệ đó **không giảm** qua từng khách, thì mô hình của bạn đang là **dịch vụ mặc áo sản phẩm**. Điều đó không sai — nhưng nó có nghĩa là bạn không scale được bằng cách tuyển thêm sales, và định giá của bạn phải phản ánh đúng bản chất đó.

Đối chiếu: gross margin AI-native đang ở **~45% (2025) → ~53% (2026E)**, so với trung vị SaaS truyền thống **77%**. Khoảng cách đó phần lớn là inference — chi phí model chiếm **20% (2025) → 23% (2026)** cấu trúc chi phí. Nếu bạn cộng thêm một cục triển khai 30% ACV nữa, biên còn lại rất mỏng.

#### Năm luật quyết định B2B

> **B2B-1 · Luật dừng** — NẾU TTFV > 60 ngày, TRÊN 3 khách gần nhất, THÌ **cắt phạm vi pilot xuống một use case một đội** và không nhận pilot rộng hơn cho đến khi TTFV <30 ngày. KHÔNG THÌ **không tuyển thêm sales** — thêm deal vào một phễu tắc chỉ làm tắc nặng hơn.

> **B2B-2 · Luật dừng** — NẾU >20% deal chết ở khâu security/procurement, TRONG 1 quý, THÌ **dừng bán 2 tuần, hoàn thiện Evidence Pack** (Day 25 §2.8: Eval Results + Risk Checklist + Pilot Report). KHÔNG THÌ **không giảm giá để cứu deal** — deal chết ở procurement không phải deal chết vì giá.

> **B2B-3** — NẾU chi phí triển khai > 30% ACV, TRÊN 3 khách liên tiếp, THÌ **hoặc tăng giá, hoặc chuẩn hoá triển khai thành sản phẩm** (template, self-serve onboarding, connector sẵn). KHÔNG THÌ **không nhận thêm khách mới với cùng mức giá** — mỗi khách mới làm tình hình xấu thêm.

> **B2B-4** — NẾU usage depth < 30%, SAU 60 ngày kể từ go-live, THÌ **coi đây là tín hiệu churn sớm**, cử người vào làm adoption trước khi bàn gia hạn. KHÔNG THÌ **không bán thêm module cho tài khoản đó** — bán thêm vào một tài khoản chưa dùng hết là cách nhanh nhất mất cả hợp đồng.

> **B2B-5** — NẾU một khách > 30% doanh thu, THÌ **mọi mục tiêu tăng trưởng xếp sau việc có khách thứ hai cùng cỡ**. KHÔNG THÌ **không nhận yêu cầu tuỳ biến riêng cho khách đó nữa** — mỗi lần tuỳ biến là một lần khoá chặt mình hơn.

#### Chiến lược B2B

**Đòn bẩy là TTFV và mở rộng trong tài khoản — không phải số logo.**

Trung vị NRR của ngành phần mềm là **101%** (Benchmarkit, dữ liệu FY2024). Nghĩa là **một nửa số công ty gần như không mở rộng được gì** trong các tài khoản đã có. Ai đạt NRR ≥110% thì mỗi năm có thêm 10% doanh thu **mà không cần bán thêm khách mới** — đó là đòn bẩy mạnh nhất của mô hình B2B, và nó bắt đầu từ TTFV.

**Trình tự đúng: chiều sâu trước chiều rộng.**

```
1 khách dùng thật, đo được kết quả
        ↓
Pilot Report có số  →  Evidence Pack (Day 25)
        ↓
Khách thứ 2, 3 trong CÙNG ngành — chu kỳ bán ngắn lại vì đã có case
        ↓
Mở rộng trong từng tài khoản (NRR)  ←  đòn bẩy thật nằm ở đây
```

Một điểm hỗ trợ cho hướng này: doanh nghiệp đang **mua nhiều hơn tự xây** — tỷ lệ build/buy lật từ 47/53 (2024) sang **24/76 (2025)**. Và dự án AI **chuyển từ thử nghiệm sang vận hành thật với tỷ lệ 47%**, so với 25% của phần mềm truyền thống. Cửa đang mở; vấn đề là bạn có đưa được khách qua cửa đủ nhanh không.

#### Cổng gác 90 ngày — B2B

| Cổng | Metric gác cổng | Ngưỡng qua cổng |
|---|---|---|
| **Ngày 30** | 3 pilot đã bắt đầu **và** Evidence Pack v1 đã viết xong | Cả hai |
| **Ngày 60** | TTFV < 30 ngày trên ≥2 khách | Có số ngày cụ thể cho từng khách |
| **Ngày 90** | 1 Pilot Report có số **và** 1 cơ hội mở rộng trong tài khoản cũ | Cả hai |

---
### 3.3 B2B2C — trận đánh **bắt partner thực sự đẩy**

> **Ký được partner không phải là thắng. Đó mới là lúc bắt đầu.**
> Partner "ký cho có" là cái chết chậm: bạn báo cáo 12 partner, doanh thu thật đến từ 2, và bạn mất hai quý mới nhận ra.

#### Vì sao pipeline đẹp mà doanh thu bé — hai tỉ lệ nhân nhau

Trong B2B và B2C, bạn có **một** phễu. Trong B2B2C bạn có **hai**, và chúng **nhân với nhau**:

```
   Bạn ──→ Partner ──→ Người dùng cuối
        │           │
    tỉ lệ ký    tỉ lệ partner
    được       thực sự đẩy       ×  tỉ lệ end-user chấp nhận
```

Ví dụ số dễ hiểu: bạn ký được **10 partner**. Trong đó **4 partner** thực sự triển khai và đẩy. Mỗi partner đó đưa sản phẩm tới **10%** khách của họ. Kết quả: bạn đang phục vụ **4% × cơ sở khách hàng** mà slide gọi vốn của bạn ghi là "tiếp cận 10 partner với 5 triệu người dùng".

**Đây là lý do B2B2C nhìn từ xa rất đẹp và nhìn gần rất khác.** Không phải vì mô hình sai — mà vì hầu hết đội chỉ đo phễu thứ nhất.

> **Một con số đáng dừng lại:** trong khảo sát ICONIQ 01/2026 với ~300 lãnh đạo công ty phần mềm, mô hình go-to-market chia ra **sales-led 38% · PLG 30% · hybrid 29% · channel/partner 3%**.
>
> Chỉ **3%** chạy motion qua kênh. Nếu B2B2C dễ như nó nghe, con số đó đã không nhỏ như vậy. Điều đó **không** có nghĩa là đừng làm B2B2C — nó có nghĩa là bạn phải làm với con mắt mở, và đo đúng chỗ.

#### Ba biến Day 24–25 chưa bắt bạn tính

| # | Biến | Vì sao Day 24–25 bỏ sót | Ảnh hưởng |
|---|---|---|---|
| **1** | **Gross Margin SAU rev-share** | Day 24 tính GM trước khi chia cho partner | GM thật của bạn thấp hơn GM trong Excel Day 24 đúng bằng phần chia. Mốc công khai duy nhất tồn tại: **AWS Marketplace 3% (SaaS) / 20% (server, container, ML)** · **Salesforce AppExchange Checkout 15%** |
| **2** | **Rủi ro inference bất đối xứng** ⭐ | Cost/Job của Day 25 ngầm giả định **bạn kiểm soát volume** | Trong B2B2C, **partner kiểm soát volume nhưng bạn trả tiền token**. Partner chạy một chiến dịch marketing → hoá đơn API của bạn nhân ba, doanh thu của bạn thì theo hợp đồng cũ |
| **3** | **Tập trung & tranh chấp attribution** | Day 25 §2.4 nói Outcome pricing cần Attribution | Trong B2B2C, **partner cũng claim kết quả đó**. Nếu không chốt được ai đo và ai được tính công, bạn **không bán Outcome được** — phải lùi về Usage |

> **Biến số 2 là phần chưa có sách vở nào viết.** Khung B2B2C được trích dẫn nhiều nhất (a16z, Alex Rampell) viết năm **2018** — trước LLM bốn năm. Nó nói rất đúng về quyền sở hữu khách hàng, nhưng không nói gì về việc bạn phải trả tiền suy luận cho lưu lượng người khác điều khiển. Đây là khoảng trống thật của ngành. Cách phòng ở phần "chiến lược" bên dưới là **đề xuất**, không phải chuẩn — hãy phản biện nó.

#### Bảng đèn B2B2C

| Tầng | Đèn | Công thức / định nghĩa | Nhịp | 🟢 | 🟡 | 🔴 | Nguồn |
|---|---|---|---|---|---|---|---|
| **L** | **Partner activation rate** ⭐ | % partner đã go-live có **≥1 end-user thật** trong 30 ngày. Không tính tài khoản test nội bộ | Tuần | ≥60% | 30–60% | <30% | [TB] |
| **L** | **End-user reach trong partner** | % cơ sở khách hàng của partner đó đã chạm sản phẩm | Tuần | ≥15% | 5–15% | <5% sau 60 ngày | [TB] |
| **L** | **Time-to-first-end-user** | Ngày từ ký → end-user thật đầu tiên | Mỗi partner | <30 ngày | 30–60 | >60 | [TB] |
| **O** | **Volume volatility** | Độ lệch chuẩn volume tháng ÷ volume trung bình | Tháng | <20% | 20–40% | >40% | [MH] |
| **O** | **GM sau rev-share** | (Doanh thu − rev-share − COGS) ÷ doanh thu | Tháng | ≥50% | 35–50% | <35% | [MH] neo bằng AI-native ~53% (2026E) |
| **O** | **Chi phí inference ÷ doanh thu — theo TỪNG partner** | Không lấy trung bình toàn bộ | Tháng | <25% | 25–40% | >40% | [MH] |
| **O** | **Tập trung volume** | % volume từ partner lớn nhất | Tháng | <40% | 40–60% | >60% | [TB] |
| **O** | **Chất lượng nhìn từ end-user** | Tỷ lệ hoàn thành / escalate / khiếu nại — đo trên end-user, không trên partner | Tuần | theo SLA đã ký | tiệm cận SLA | vi phạm SLA | [TB] |
| **G** | Doanh thu/partner · partner NRR · GM tổng | | Quý | | | | Day 24 |

#### Ba cái đèn gần như không ai bật

**① "Số partner đã ký" là chỉ số phù phiếm.** Nó tăng đều, nhìn rất đẹp trên slide, và **không tương quan với doanh thu**. Chỉ số thật là *partner activation rate*. Quy tắc đơn giản: **mọi lần bạn định báo cáo số partner, hãy báo cáo kèm số partner đã activate.** Nếu hai con số cách nhau xa, đó là câu chuyện thật của công ty bạn.

**② Volume volatility — vì nó quyết định bạn có dự báo được chi phí không.**

Trong ICONIQ 2026, **92%** công ty AI nói chi phí AI của họ **khó dự đoán**; có workflow được mô hình hoá ở $0,10/lần chạy về sau tốn hơn **$1,50** — sai số **15×**. Đó là khi bạn **tự** kiểm soát lưu lượng. Trong B2B2C, bạn không kiểm soát. Volume volatility >40% nghĩa là bạn **không thể** cam kết một mức giá cố định mà không đánh cược.

**③ GM sau rev-share phải xem theo từng partner, không lấy trung bình.** Trung bình che mất chuyện một partner đang lỗ được bù bởi một partner đang lãi. Trong B2B2C, partner lỗ **thường lại là partner ồn ào nhất** — họ đẩy nhiều volume nhất, đòi nhiều hỗ trợ nhất, và họ chính là lý do bạn nghĩ mình đang tăng trưởng.

#### Bài học Klarna — chất lượng là điều khoản sống còn, không phải chi phí

**Tháng 02/2024:** Klarna công bố trợ lý AI (chạy trên OpenAI) xử lý **2,3 triệu hội thoại = hai phần ba toàn bộ chat** ngay trong tháng đầu, tương đương công việc của **700 nhân viên**; thời gian xử lý từ **11 phút xuống dưới 2 phút**; ước tính cải thiện lợi nhuận **$40 triệu** trong năm 2024.

**Tháng 05/2025:** Klarna **đảo chiều**, tuyển lại nhân viên hỗ trợ. CEO Sebastian Siemiatkowski nói chi phí đã trở thành *"một tiêu chí đánh giá quá lấn át"* và điều đó làm hỏng chất lượng.

> **Bài học cho B2B2C, không phải bài học về AI.** Khi bạn nằm **bên trong thương hiệu của người khác**, sản phẩm của bạn hỏng thì đó là **khủng hoảng của họ**, không phải của bạn — và họ sẽ gỡ bạn ra. Đó là lý do bảng đèn B2B2C có một dòng mà B2B và B2C không có: **chất lượng nhìn từ end-user**. Trong B2B2C, SLA chất lượng không phải điều khoản pháp lý — nó là điều kiện tồn tại của kênh.

*(Lưu ý nguồn: con số $40 triệu là **ước tính trong thông cáo báo chí của Klarna**, không được kiểm toán, công bố trước IPO. Dùng nó như một câu chuyện, không như một bằng chứng.)*

#### Năm luật quyết định B2B2C

> **B2B2C-1 · Luật dừng** — NẾU partner activation rate < 30%, TRONG 60 ngày, VÀ đã có ≥5 partner go-live, THÌ **dừng ký partner mới, dồn toàn bộ nguồn lực kích hoạt partner đã có**. KHÔNG THÌ **không được dùng "số partner đã ký" làm chỉ số tăng trưởng trong bất kỳ báo cáo nào**.

> **B2B2C-2** — NẾU end-user reach < 5% sau 60 ngày ở một partner, THÌ **vấn đề nằm ở động lực của partner, không nằm ở sản phẩm** → ngồi lại trả lời "partner này được gì" (nguyên tắc Give > Get) và đổi cơ chế khuyến khích. KHÔNG THÌ **không thêm tính năng theo yêu cầu của partner đó** — partner không đẩy sẽ luôn có một tính năng nữa để chờ.

> **B2B2C-3** — NẾU volume volatility > 40%, TRONG 2 tháng, THÌ **đàm phán minimum commitment hoặc chuyển chi phí inference sang pass-through**. KHÔNG THÌ **không cam kết SLA cứng hay giá cố định trên lưu lượng bạn không kiểm soát**.

> **B2B2C-4 · Luật dừng** — NẾU một partner > 60% volume, THÌ **mọi hạng mục roadmap xếp sau việc có partner thứ hai**. KHÔNG THÌ **không nhận điều khoản độc quyền**, dù được đề nghị tăng giá.

> **B2B2C-5** — NẾU GM sau rev-share < 35%, TRÊN 2 quý, THÌ **đàm phán lại tỷ lệ chia hoặc rút khỏi kênh đó**. KHÔNG THÌ **không bù bằng volume** — trong sản phẩm AI, thêm volume ở biên âm là lỗ thêm, không phải quy mô.

#### Chiến lược B2B2C

**Đòn bẩy là partner activation, không phải số partner.** Ba việc, theo đúng thứ tự:

**① Làm cho partner có lợi rõ ràng — "Give > Get".** Nguyên tắc của Rampell (a16z): chỉ được đòi quyền chạm khách hàng cuối khi bạn **mang lại cho partner nhiều hơn thứ bạn lấy đi**. Câu hỏi kiểm tra: *nếu partner bỏ bạn ngày mai, họ mất gì?* Trả lời được bằng một câu cụ thể thì kênh có thật. Không trả lời được thì hợp đồng chỉ là tờ giấy.

**② Giành quyền chạm người dùng cuối — và biết cái giá của nó.** Bốn biến thể B2B2C khác nhau ở đúng điểm này:

| Biến thể | Bạn có chạm end-user? | Đánh đổi |
|---|---|---|
| **Embedded (có thương hiệu)** | Có | Partner khó chịu hơn, đàm phán lâu hơn |
| **White-label** | Không | Dễ ký nhất — và bạn mất thương hiệu, mất flywheel, dễ bị thay |
| **Marketplace** | Một phần | Phí niêm yết rõ ràng (AWS 3%/20%, AppExchange 15%), ít quan hệ |
| **Giới thiệu / phân phối** | Không | Đây **không phải** B2B2C — đây là kênh bán hàng. Dùng bảng B2B |

**Intercom Fin là ví dụ đáng học nhất về cái giá này:** để nhúng được vào helpdesk mà khách **đang dùng sẵn** (Salesforce, HubSpot, Zendesk), Intercom **bỏ hoàn toàn phí seat** — chấp nhận mất một dòng doanh thu để đổi lấy chỗ đứng trong workflow. Họ cũng chấp nhận **xoá bỏ khoảng $60 triệu ARR cũ** để buộc thị trường chuyển sang mô hình tính theo kết quả. Nhúng vào thói quen người khác **có giá**, và người thắng là người dám trả cái giá đó.

**③ Khoá rủi ro volume bằng hợp đồng — trước khi cần đến.** Bốn công cụ, xếp theo thứ tự dễ đàm phán:

| Công cụ | Nội dung | Bảo vệ bạn khỏi |
|---|---|---|
| **Minimum commitment** | Partner cam kết mức volume tối thiểu/tháng | Partner ký rồi không đẩy |
| **Volume cap / bậc thang** | Quá ngưỡng thì đơn giá đổi | Chiến dịch marketing đột ngột của partner |
| **Pass-through chi phí** | Phần token vượt ngưỡng tính lại cho partner | Rủi ro inference bất đối xứng |
| **Điều khoản chất lượng 2 chiều** | SLA của bạn **và** nghĩa vụ của partner (dữ liệu, đào tạo, kênh escalate) | Bài học Klarna |

> ⚠️ **Về tỷ lệ rev-share:** mình đã tìm và **không có nhà cung cấp, marketplace hay khảo sát nào công bố "tỷ lệ chia sẻ doanh thu tiêu chuẩn" cho white-label / OEM trong ngành AI.** ElevenLabs ghi rõ mọi điều khoản thương mại nằm trong hợp đồng riêng. Các con số "thường là X%" bạn đọc trên mạng đều không truy được về nguồn gốc. **Hai mốc duy nhất có thật là phí niêm yết marketplace: AWS 3%/20% và AppExchange 15%.** Hãy dùng chúng làm neo, và tự đàm phán phần còn lại.

#### Ví dụ tham chiếu tại Việt Nam

**FPT.AI** là ví dụ B2B2C quy mô lớn dễ quan sát nhất trong nước: công bố **3.000+ khách hàng doanh nghiệp**, phục vụ **16 triệu+ người dùng cuối**, **200 triệu+ tương tác tự động** — khách trả tiền là ngân hàng và công ty tài chính (MB, BIDV, Sacombank, HDBank, FWD, Home Credit), còn người thực sự nói chuyện với sản phẩm là **khách hàng của những ngân hàng đó**. Đáng chú ý: **họ không công bố giá** — toàn bộ là "liên hệ tư vấn". Với mô hình này, đó tự nó đã là một dữ kiện.

**Zalo ZNS** là ví dụ về một "trạm thu phí" B2B2C: doanh nghiệp trả tiền cho Zalo để chạm tới người tiêu dùng, tính theo từng tin nhắn (khoảng 120–300 ₫/tin tuỳ loại ⚠️ *giá theo bảng của đại lý, không phải trang chính chủ*). Nếu sản phẩm của bạn đi qua một nền tảng như vậy, **phí nền tảng phải nằm trong Cost/Job của Day 25**, không phải nằm ngoài.

#### Cổng gác 90 ngày — B2B2C

| Cổng | Metric gác cổng | Ngưỡng qua cổng |
|---|---|---|
| **Ngày 30** | 1 partner đã ký **và** đường đi tới end-user đã vẽ rõ (ai bấm nút gì, ở màn hình nào) | Cả hai — "sẽ tích hợp" không tính |
| **Ngày 60** | ≥1 partner activate với end-user thật **và** đã đo được chi phí inference của riêng partner đó | Có số |
| **Ngày 90** | End-user reach ≥5% **và** GM sau rev-share ≥ ngưỡng bạn đặt | Cả hai |

---
## 4. LAB — 5 trạm, 120 phút

Đây là phần chính của Day 26. **Bấm giờ từng trạm.** Hết giờ thì chuyển trạm kể cả khi chưa hoàn hảo — bạn quay lại hoàn thiện ở Trạm 5.

| Trạm | Nội dung | Thời gian | Output |
|---|---|---|---|
| **1** | Chốt loại & lấy bảng đèn | 15' | Loại đã chốt + danh sách đèn đo được / chưa đo được |
| **2** | Dựng cây 3 tầng | 25' | 6–8 thẻ đèn đủ 6 trường |
| **3** | **Đặt ngưỡng** | **30'** ⭐ | Mỗi đèn có 🟢🟡🔴 + nguồn + lý do |
| **4** | **Viết luật quyết định** | **30'** ⭐ | 5 luật, ≥2 là luật dừng |
| **5** | Cổng gác 90 ngày & ráp dashboard | 20' | Dashboard 1 trang hoàn chỉnh |
| | **Tổng** | **120'** | |

> **Nguyên tắc xuyên suốt:** mỗi con số bạn viết ra phải trả lời được câu *"dựa vào đâu mà là con số này?"* Ngưỡng không có lý do bị chấm 0 — kể cả khi nó đúng.

---

### Trạm 1 — Chốt loại & lấy bảng đèn · 15 phút

**Mục tiêu.** Biết chắc mình thuộc loại nào, và biết mình đang **thiếu** dữ liệu ở đâu.

**Các bước:**

1. **(5')** Trả lời 3 câu hỏi §2.5 theo **thực tế hôm nay**, không theo kế hoạch quý sau:
   - Ai trả tiền cho bạn?
   - Ai dùng sản phẩm?
   - Nếu có bên trung gian: bạn có chạm được người dùng cuối không?
2. **(3')** Viết **1 câu** chốt loại kèm lý do. Mẫu: *"Chúng tôi là B2B2C vì tiền đến từ [X], người dùng thật là khách của [X], và chúng tôi chạm được họ qua [bề mặt cụ thể]."*
3. **(7')** Mở đúng bảng đèn của mình ở §3. Với **từng đèn**, đánh dấu một trong ba:
   - ✅ **Đo được hôm nay** — số nằm ở đâu?
   - 🔧 **Chưa đo được nhưng làm được trong 2 tuần** — cần gì? (log, event tracking, câu hỏi thêm trong hợp đồng)
   - ❌ **Chưa đo được và chưa biết cách** — ghi ra, đừng giấu

**✅ Checkpoint 1:** 1 câu chốt loại + bảng đèn đã đánh dấu ✅/🔧/❌ đầy đủ.

**⚠️ Bẫy thường gặp:**
- **Chọn B2B2C vì nghe có đòn bẩy.** Nếu bạn không chạm được người dùng cuối, không có dữ liệu của họ, không có thương hiệu trước mặt họ → bạn đang là nhà cung cấp cho một doanh nghiệp. Dùng bảng B2B. Đây là chẩn đoán đúng, không phải hạ cấp.
- **Chọn theo kế hoạch tương lai.** "Năm sau chúng tôi sẽ mở B2C" không đổi được việc hôm nay bạn phải canh đèn gì.
- **Giấu ô ❌.** Ô ❌ trung thực được điểm cao hơn ô ✅ bịa.

---

### Trạm 2 — Dựng cây 3 tầng · 25 phút

**Mục tiêu.** Có 6–8 đèn, mỗi đèn đủ 6 trường của thẻ đèn (§2.2).

**Các bước:**

1. **(4')** Chọn **1 North Star** — chỉ số duy nhất mà nếu chỉ được nhìn một con số mỗi tuần, bạn nhìn nó. Với hầu hết học viên, đây chính là "đèn bật trước" của loại mình (§2.5).
2. **(12')** Chọn 6–8 đèn từ bảng §3 và điền thẻ. **Bắt buộc:**
   - Ít nhất **2 đèn Leading** — nếu bạn không có, dashboard của bạn là gương chiếu hậu
   - Ít nhất **1 đèn liên quan trực tiếp đến chi phí AI** (token, inference, cost/job)
   - Tối đa **3 đèn Lagging** — Day 24 đã lo phần đó
3. **(5')** Với mỗi đèn, viết trường số 5: **"đèn này báo trước cho đèn nào"**. Nếu không viết được thì **bỏ đèn đó ra** — nó không phải leading indicator, chỉ là một con số bạn thích nhìn.
4. **(4')** Bỏ bớt. Dashboard >8 đèn là dashboard không ai nhìn. Cắt xuống đúng số bạn thật sự sẽ mở mỗi tuần.

**✅ Checkpoint 2:** 1 North Star + 6–8 thẻ đèn đủ trường 1, 2, 3, 5.

**⚠️ Bẫy thường gặp:**
- **Định nghĩa lỏng.** "User hoạt động" nghĩa là gì — mở app? làm xong một việc? quay lại lần hai? Ba định nghĩa, ba con số, ba quyết định khác nhau.
- **Đèn đẹp mà không kéo được.** Nếu bạn không nói được "tuần này tôi làm gì để đèn này tốt lên" thì nó thuộc tầng lagging, xếp đúng chỗ.
- **Copy nguyên bảng §3.** Bảng §3 là thực đơn, không phải suất ăn. Sản phẩm của bạn có thể cần một đèn không có trong bảng — tốt, thêm vào.

**🔁 Nếu bí:** chạy **Prompt 5.1** (Dashboard Tier Audit).

---

### Trạm 3 — Đặt ngưỡng · 30 phút ⭐

**Mục tiêu.** Mỗi đèn có 🟢 🟡 🔴 **và một câu lý do đứng được**.

**Các bước:**

1. **(6') Phân loại nguồn.** Với mỗi đèn, xác định ngưỡng đến từ đâu: **[BM]** benchmark có nguồn · **[MH]** suy từ mô hình Day 24–25 · **[TB]** tự đặt baseline. Ghi ký hiệu vào cạnh ngưỡng.
2. **(8') Với đèn [BM]:** mở §8, lấy con số, **ghi ngày bạn kiểm tra**. Nếu benchmark trong §8 đã cũ hơn 3 tháng so với ngày bạn làm bài, tự mở nguồn gốc và cập nhật. Đây là một phần bài tập.
3. **(10') Với đèn [MH] — phần quan trọng nhất của trạm này.** Mở Excel Day 24 và Cost/Job Day 25, **suy ngược** ra ngưỡng:
   - *Mô hình của tôi chỉ sống khi khách ở lại ≥N tháng → vậy retention tháng thứ 3 tối thiểu phải là bao nhiêu?*
   - *CAC payback phải <12 tháng → với ARPU và GM này, CAC tối đa là bao nhiêu?*
   - *GM mục tiêu 50% → chi phí inference trên mỗi job tối đa là bao nhiêu?*

   **Bắt buộc ít nhất 2 ngưỡng thuộc loại [MH].** Đây là chỗ Day 26 nối vào Day 24–25 chặt nhất.
4. **(6') Với đèn [TB]:** ghi rõ *"chưa có chuẩn, sẽ đo 2 chu kỳ rồi lấy làm baseline"* + ngày dự kiến có số. Đây là câu trả lời hợp lệ và được điểm.

**✅ Checkpoint 3:** 100% đèn có 🟢🟡🔴 + ký hiệu nguồn + 1 câu lý do. Ít nhất 2 ngưỡng [MH].

**⚠️ Bẫy thường gặp:**
- **Lấy benchmark làm mục tiêu.** Retention M12 = 21,1% là **trung vị của một ngành đang chật vật**, không phải đích đến.
- **Ngưỡng tròn trịa đáng ngờ.** 10%, 20%, 50% xuất hiện khắp nơi thường là dấu hiệu của việc đoán. Số suy từ mô hình hiếm khi tròn.
- **Đặt ngưỡng dễ để luôn xanh.** Dashboard toàn xanh là dashboard vô dụng — nó chỉ đang xác nhận điều bạn muốn tin.

**🔁 Nếu bí:** chạy **Prompt 5.2** (Threshold Justification Challenger).

---

### Trạm 4 — Viết luật quyết định · 30 phút ⭐

**Mục tiêu.** 5 luật đúng cấu trúc, dùng được ngay, trong đó **ít nhất 2 luật là luật dừng**.

**Các bước:**

1. **(4')** Chọn 5 đèn quan trọng nhất — mỗi đèn một luật. Ưu tiên đèn Leading.
2. **(14')** Viết đủ 5 phần cho từng luật: **NẾU / TRONG / VÀ / THÌ / KHÔNG THÌ** (§2.4).
   - Vế **THÌ** phải bắt đầu bằng **động từ hành động**: *đóng băng · cắt · dừng · đàm phán lại · chuyển · tuyển*. Không dùng: *xem xét, cân nhắc, đánh giá lại, theo dõi thêm*.
   - Vế **TRONG** chống nhiễu; vế **VÀ** chống kết luận từ mẫu quá nhỏ.
3. **(7') Vế KHÓ NHẤT — "KHÔNG THÌ".** Với mỗi luật, tự hỏi: *khi đèn này đỏ, phản xạ đầu tiên của tôi sẽ là gì?* Viết phản xạ đó vào vế KHÔNG THÌ. Nếu bạn không nghĩ ra phản xạ sai nào, xem lại bảng ba phản xạ kinh điển ở §2.4.
4. **(5') Kiểm tra "luật dừng".** Đếm lại: **ít nhất 2 trong 5 luật** phải bảo bạn **ngừng** một việc đang làm (dừng chi tiêu, dừng ký partner mới, dừng bán, dừng nhận khách). Nếu chưa có đủ, viết lại — vì đây là loại luật khó nhất và cứu bạn nhiều nhất.

**✅ Checkpoint 4:** 5 luật đủ 5 phần, ≥2 luật dừng, không luật nào kết thúc bằng "xem xét lại".

**⚠️ Bẫy thường gặp:**
- **Luật không có chủ ngữ thời gian.** "Nếu retention thấp" — thấp trong bao lâu? Một tuần xấu không phải xu hướng.
- **Hành động quá to để thực hiện.** "Thì pivot toàn bộ sản phẩm" là luật sẽ không bao giờ được thi hành. Hành động phải **vừa đủ nhỏ để bạn thật sự làm**.
- **Không có luật dừng nào.** Dashboard chỉ toàn luật "làm thêm" là dashboard của người chưa bao giờ phải cắt gì.

**🔁 Nếu bí:** chạy **Prompt 5.3** (Decision Rule Red-Team) và **Prompt 5.4** (Wrong-Reflex Finder).

---

### Trạm 5 — Cổng gác 90 ngày & ráp dashboard · 20 phút

**Các bước:**

1. **(10')** Lấy 3 cổng gác gợi ý của loại mình (cuối §3.1 / §3.2 / §3.3), **thay bằng số của bạn**. Mỗi cổng cần: 1 metric · 1 ngưỡng · 1 quyết định trong bốn lựa chọn **GO / FIX / PIVOT / KILL**.
2. **(4')** Viết **kill criteria**: điều kiện nào thì bạn dừng hẳn hướng này. Một câu, có số, có mốc thời gian.
3. **(6')** Ráp tất cả vào **Dashboard 1 trang** theo khung dưới đây. Worksheet
   nguồn 12 cột dùng để truy vết và chạy validator, không phải bảng phải co lại
   nguyên xi. Dùng `templates/one-page-dashboard-template.md` để rút gọn.

**✅ Checkpoint 5:** Dashboard 1 trang hoàn chỉnh, in ra vừa đúng một mặt giấy.

---

### Khung Dashboard 1 trang — copy sang file của bạn

```
════════════════════════════════════════════════════════════
OPERATING DASHBOARD — [Tên sản phẩm]
Loại mô hình: [B2C / B2B / B2B2C]   ·   Cập nhật: [ngày]
NORTH STAR: [tên đèn] — hiện tại [số] — mục tiêu [số]
════════════════════════════════════════════════════════════

▸ ĐÈN BÁO SỚM (leading — nhìn hằng ngày/tuần)
┌──────────────────┬────────┬──────────────┬──────┬──────────┐
│ Đèn              │ Hiện   │ 🟢/🟡/🔴      │ Nguồn│ Báo trước│
├──────────────────┼────────┼──────────────┼──────┼──────────┤
│                  │        │              │ [  ] │          │
└──────────────────┴────────┴──────────────┴──────┴──────────┘

▸ ĐÈN VẬN HÀNH (operating — nhìn hằng tuần/tháng)
   [cùng cấu trúc]

▸ ĐÈN KẾT QUẢ (lagging — nhìn hằng quý, lấy từ Day 24)
   [cùng cấu trúc]

════════════════════════════════════════════════════════════
5 LUẬT QUYẾT ĐỊNH
1. NẾU … TRONG … VÀ … THÌ … KHÔNG THÌ …
2. …                                      [đánh dấu ⏹ luật dừng]
════════════════════════════════════════════════════════════
CỔNG GÁC 90 NGÀY
Ngày 30 │ metric: ……… │ ngưỡng: ……… │ GO / FIX / PIVOT / KILL
Ngày 60 │ …
Ngày 90 │ …

KILL CRITERIA: ………………………………………………………
CHƯA ĐO ĐƯỢC: ……………… (cần gì để đo: ………, khi nào: ………)
════════════════════════════════════════════════════════════
```

---
## 5. Prompts cho AI (English-only)

Giữ nguyên tiếng Anh để không lệch nghĩa. **AI là công cụ phản biện, không phải người viết hộ** — quyết định cuối cùng là của bạn và phải do bạn viết lại bằng lời của mình.

---

### 5.1 Dashboard Tier Audit — *prompt chính*

```
You are a skeptical operating partner at a VC fund, reviewing a founder's metrics dashboard.

MY BUSINESS MODEL TYPE: [B2C / B2B / B2B2C]
MY PRODUCT IN ONE SENTENCE: [...]
MY DASHBOARD:
[paste your 6-8 metrics with definitions and thresholds]

Audit it on five points. Be blunt; I would rather be embarrassed now than wrong later.

1. TIER CLASSIFICATION. For each metric, classify it as LEADING (changes in
   days/weeks, predicts something later), OPERATING (changes in weeks/months,
   I can actively pull this lever), or LAGGING (changes in months/quarters,
   it is a scoreboard). Tell me how many of each I have. If more than half
   are lagging, say so directly: I am steering with a rear-view mirror.

2. PREDICTIVE CHAIN. For each metric I claim is leading, name the specific
   downstream metric it predicts and the realistic lag in weeks. If you
   cannot name one, tell me the metric is decoration and should be cut.

3. DEFINITION TIGHTNESS. Find every metric whose definition could be read
   two different ways ("active user", "resolved", "onboarded", "live").
   Show me the two readings and the different numbers they would produce.

4. MISSING FOR MY TYPE. Given my model type, name up to 3 metrics that
   operators of this exact model type watch and that are ABSENT from my
   dashboard. For each, say what blindness it creates.

5. AI COST EXPOSURE. Do I have at least one metric that would catch my
   inference/token costs getting out of control before it shows up in
   gross margin? If not, propose one and tell me how to instrument it.

Output as a table for points 1-3, prose for 4-5. Do not compliment the dashboard.
```

---

### 5.2 Threshold Justification Challenger

```
You are auditing the thresholds on a startup metrics dashboard.

For each metric below I give you: the metric, my green/yellow/red thresholds,
and my stated justification.

[paste each as: METRIC | GREEN | YELLOW | RED | WHY]

For each one, do the following:

a) Classify my justification as: PUBLISHED BENCHMARK (I cite a real source),
   DERIVED FROM MY OWN MODEL (I computed it from my unit economics),
   OWN HISTORICAL BASELINE (I measured it myself), or VIBES (none of the above).
   Be harsh. "Industry standard" with no source is VIBES.

b) For anything you classify as VIBES, propose how I could DERIVE that
   threshold instead, using this input data:
   [paste your Day 24 unit economics: ARPU, gross margin, CAC, target payback
    period, and your Day 25 Cost/Job]
   Show the arithmetic.

c) Flag any threshold that looks suspiciously round (10%, 20%, 50%) and ask
   me whether it was computed or guessed.

d) Flag any threshold set so loose that the light would almost never turn red.
   A dashboard that is always green is a dashboard that is not measuring anything.

End with the single threshold you think is most likely to be wrong, and why.
```

---

### 5.3 Decision Rule Red-Team

```
You are red-teaming a startup's decision rules. Your job is to find the
situation where following the rule produces a bad outcome.

MY MODEL TYPE: [B2C / B2B / B2B2C]
MY RULES:
[paste your 5 rules in the form IF <metric> <operator> <threshold> FOR <period>
 AND <sample condition> THEN <action> ELSE-NOT <forbidden action>]

For each rule:

1. FALSE POSITIVE. Describe a concrete, realistic scenario where this metric
   crosses the threshold but the underlying business is fine, and firing the
   rule would destroy value. Is my time window long enough to prevent it?

2. FALSE NEGATIVE. Describe a scenario where the business is genuinely
   breaking but this rule never fires. What metric would have caught it?

3. EXECUTABILITY. Is the THEN action small enough that a 3-person team would
   actually do it next Monday? If it requires a heroic reorganisation, it will
   never be executed. Propose a smaller version.

4. GAMEABILITY. If someone on my team wanted to avoid triggering this rule,
   what is the easiest way to do that without improving the business?

5. THE MISSING RULE. After reading all five, name the one decision rule that
   is most conspicuously absent for my model type.

Be specific and concrete. Generic advice is useless to me.
```

---

### 5.4 Wrong-Reflex Finder

```
I run a [B2C / B2B / B2B2C] company. Here is a metric on my dashboard and
its red threshold:

METRIC: [...]
RED THRESHOLD: [...]
CONTEXT: [2-3 sentences about my product and stage]

Answer three questions:

1. When this light turns red, what is the MOST COMMON first reaction of
   founders in my situation? Describe the reflex, not the ideal response.

2. Why is that reflex usually wrong for THIS model type specifically?
   Explain the mechanism, not a platitude.

3. Write the "ELSE-NOT" clause of a decision rule that forbids that reflex,
   in one sentence, phrased as a prohibition I could put on a wall.

Then repeat for the second most common wrong reflex.
```

---

### 5.5 Blind-Spot Finder by Model Type

```
I run a [B2C / B2B / B2B2C] AI product.

PRODUCT: [one paragraph]
HOW I MAKE MONEY: [value metric and price, from my Day 25 work]
WHAT I CURRENTLY MEASURE: [list]
MY COST STRUCTURE: [Cost/Job breakdown from Day 25]

Answer as an operator who has run this exact model type before, not as a
consultant.

1. What are the three things that most often kill companies with THIS model
   type in the first 18 months? Not generic startup failure — failure modes
   specific to this structure.

2. For each, what is the earliest observable signal, and how many weeks or
   months before the damage becomes visible in revenue does it appear?

3. Which of those three signals am I currently blind to?

4. For my model type specifically, name one cost that grows in a way founders
   do not expect, and describe the shape of that growth (linear with users?
   with usage? step function at a scale threshold?).

5. Finally: is there any evidence in what I have told you that I have
   MISCLASSIFIED my own model type? Say so plainly if you see it.
```

---

### 5.6 90-Day Gate Designer

```
Help me design go/no-go gates for the next 90 days.

MODEL TYPE: [B2C / B2B / B2B2C]
CURRENT STATE: [what exists today — users, customers, partners, revenue]
MY NORTH STAR METRIC: [...]
RESOURCES: [team size, months of runway from my Day 24 model]

Design three gates, at day 30, day 60 and day 90. For each gate give me:

- ONE gating metric (not a list — one)
- A specific numeric threshold to pass, and how you derived it
- What evidence must physically exist to prove it (a file, a report, a log)
- The decision if the threshold is missed: FIX (stay another 30 days and fix
  one specific thing), PIVOT (a stated assumption is wrong), or KILL (stop)

Rules for your design:
- Day 30 must be about learning, not revenue. If you propose a revenue target
  at day 30, you have designed it wrong.
- Each gate must be falsifiable. "Good traction" is not a gate.
- Assume FIX may be used only once per problem. A second FIX for the same
  metric is a PIVOT in disguise — build that into the design.

Then state the single kill criterion for the whole 90 days in one sentence,
with a number and a date.
```

---

## 6. Checkpoints — output yêu cầu

| Mốc | Checkpoint | Phải có |
|---|---|---|
| **Phút 15** | **CP1 — Loại & bảng đèn** | 1 câu chốt loại có lý do · bảng đèn §3 đã đánh dấu ✅/🔧/❌ toàn bộ |
| **Phút 40** | **CP2 — Cây 3 tầng** | 1 North Star · 6–8 thẻ đèn có trường 1, 2, 3, 5 · ≥2 đèn Leading · ≥1 đèn về chi phí AI |
| **Phút 70** | **CP3 — Ngưỡng** ⭐ | 100% đèn có 🟢🟡🔴 + ký hiệu [BM]/[MH]/[TB] + 1 câu lý do · **≥2 ngưỡng [MH]** |
| **Phút 100** | **CP4 — Luật quyết định** ⭐ | 5 luật đủ 5 phần · **≥2 luật dừng** · không luật nào kết thúc bằng "xem xét lại" |
| **Phút 120** | **CP5 — Dashboard** | 1 trang hoàn chỉnh · 3 cổng gác có số · kill criteria · mục "chưa đo được" |

### Final checklist — trước khi nộp

- [ ] Dashboard in ra **vừa đúng một mặt giấy**
- [ ] Không có đèn nào thiếu ngưỡng
- [ ] Mỗi ngưỡng có ký hiệu nguồn **và** một câu lý do
- [ ] Ít nhất 2 ngưỡng suy từ mô hình Day 24–25, có phép tính kèm theo
- [ ] Mỗi benchmark có **ngày kiểm tra**
- [ ] Ít nhất 2 luật là luật **dừng**
- [ ] Mỗi luật có vế **KHÔNG THÌ**
- [ ] 3 cổng gác đều có metric + ngưỡng + quyết định
- [ ] Mục "chưa đo được" viết thật, không để trống cho đẹp

---
## 7. Rubric & Submission

### 7.1 Cách nộp bài

| Mục | Yêu cầu |
|---|---|
| Nộp khi nào | Trước buổi tiếp theo |
| Nộp ở đâu | Submit trực tiếp trên LMS |
| Tên file | `[Tên]_Day26_dashboard.pdf` |
| Bao gồm | Dashboard 1 trang · phần phụ lục ≤1 trang cho các phép tính suy ngưỡng [MH] |

### 7.2 Rubric — 100 điểm, 5 tiêu chí

| # | Tiêu chí | Điểm |
|---|---|---|
| 1 | **Tier Discipline** — xếp đúng tầng, có đèn báo sớm thật | 20 |
| 2 | **Threshold Quality** — ngưỡng có nguồn, có lý do, có suy từ mô hình | 30 |
| 3 | **Decision Rule Quality** — luật dùng được, có vế cấm | 30 |
| 4 | **90-Day Gates** — cổng gác falsifiable | 15 |
| 5 | **Honesty** — trung thực về chỗ chưa đo được | 5 |

Rubric vận hành chính thức là
[`rubric/rubric-v2.md`](rubric/rubric-v2.md); bản máy đọc nằm ở
[`rubric/rubric-v2.json`](rubric/rubric-v2.json). Rubric công khai item ID,
công thức điểm, cap, override, evidence contract và điều kiện human review;
không có tiêu chí bí mật làm thay đổi điểm.

Tóm tắt item:

- **Tier Discipline:** `TD-01` đến `TD-05` chấm chẩn đoán model, North Star/
  đèn bật trước, chuỗi Leading, định nghĩa + nhịp + owner và AI cost exposure.
- **Threshold Quality:** `TQ-01` đến `TQ-06` chấm vùng màu, đúng một loại nguồn,
  truy vết nguồn, hai phép tính `MH-01`/`MH-02` và logic ngưỡng → hành động.
- **Decision Rules:** `DR-01` đến `DR-05` chấm từng luật theo năm vế; `DR-06`
  chấm hai luật dừng.
- **90-Day Gates:** `GT-30`, `GT-60`, `GT-90`, `GT-KILL` chấm đúng stage,
  một metric, số, evidence và quyết định đạt/trượt.
- **Honesty:** `HO-01` đến `HO-05` chấm khoảng trống thật, kế hoạch đo, owner,
  ngày có số và tính nhất quán.

Ba cap giữ đúng tinh thần sổ tay: sai model → Tier tối đa 10/20; hơn 50% đèn
Lagging → Tier tối đa 8/20; dùng claim benchmark không truy vết được → Threshold
tối đa 10/30. Hành động mơ hồ hoặc gate mơ hồ được xử lý bằng override cấp item,
không trừ lặp lại cho cùng một lỗi.

Validator chỉ kiểm tra minimum bar về cấu trúc. Semantic grader hoặc người chấm
phải neo từng kết luận vào section/row/field/quote; mọi kết luận `UNCERTAIN`,
nguồn lỗi, cap hoặc điểm sát ranh giới đều phải human review.

### 7.3 Grade bands

| Band | Điểm | Ý nghĩa |
|---|---|---|
| **Outstanding** | 90–100 | Dán lên tường họp tuần được ngay, không cần sửa |
| **Strong** | 75–89,5 | Dùng được, cần siết 1–2 ngưỡng hoặc 1 luật |
| **Pass** | 60–74,5 | Hiểu hệ thống nhưng ngưỡng còn cảm tính |
| **Needs rework** | 40–59,5 | Sai một khái niệm lõi (dashboard toàn lagging, hoặc luật không hành động được) |
| **Fail** | 0–39,5 | Chưa đạt minimum bar |

### 7.4 Lưu ý khi làm bài

- **Đèn ít mà chuẩn hơn đèn nhiều.** 6 đèn bạn thật sự mở mỗi tuần > 15 đèn không ai nhìn.
- **Ngưỡng suy từ mô hình luôn mạnh hơn benchmark đi mượn.** Bạn đã có Day 24 và Day 25 — dùng chúng.
- **Luật khó viết nhất là luật dừng.** Nó cũng là luật cứu bạn nhiều nhất.
- **Ghi ngày cho mọi benchmark.** Số liệu AI đổi theo tháng; một dashboard không ghi ngày là một dashboard không tin được.
- **Đừng trộn ba bảng.** Dashboard trộn B2C + B2B + B2B2C là dashboard không dùng được cho loại nào.
- **AI là công cụ critique, không phải author.** Dùng §5 để stress test — nhưng quyết định cuối cùng do bạn viết bằng lời của mình.

---

## 8. References

Mọi số liệu trong sổ tay được chốt ngày **27/08/2026**. Mục ⏳ thay đổi nhanh — kiểm tra lại trước khi dùng. Mục ⚠️ là nguồn mình **cố ý không tin hoàn toàn**, có ghi rõ lý do.

### 8.1 Benchmark cho B2C

1. **RevenueCat — *State of Subscription Apps 2026*** · https://www.revenuecat.com/blog/growth/subscription-app-trends-benchmarks-2026 · công bố 19/03/2026 (cập nhật 22/04/2026). Bộ dữ liệu **115.000+ ứng dụng**, ~$16 tỷ doanh thu theo dõi — nguồn lớn nhất hiện có về subscription tiêu dùng. Số dùng trong sổ tay: trial→paid **AI 8,5% vs non-AI 5,6%**; **retention 12 tháng 21,1% vs 30,7%**; refund **4,2% vs 3,5%**; RLTV năm **$30,16 vs $21,37**. Bản tóm tắt của TechCrunch (10/03/2026): https://techcrunch.com/2026/03/10/ai-powered-apps-struggle-with-long-term-retention-new-report-shows
2. **Menlo Ventures — *2025: The State of Consumer AI*** · https://menlovc.com/perspective/2025-the-state-of-consumer-ai/ · 26/06/2025. Khảo sát 5.031 người trưởng thành Mỹ cùng Morning Consult. Số dùng: **~3%** người dùng AI trả tiền; ~1,7–1,8 tỷ người dùng; thị trường ~$12 tỷ; ChatGPT ~5% weekly active → paid. ⏳ *Chưa có bản 2026 — đây vẫn là bản mới nhất tại ngày chốt tài liệu.*
3. **Duolingo — báo cáo quý 2/2026** · https://www.globenewswire.com/news-release/2026/08/05/3339653/0/en/Duolingo-Reports-Second-Quarter-2026-Results.html · 05/08/2026. **12,7 triệu thuê bao trả phí / 140,6 triệu MAU = 9,0%**; gross margin ~73%; công ty nêu rõ *"chi phí AI bên thứ ba trên mỗi đơn vị giảm"*. Đây là **con số conversion tiêu dùng tốt nhất có kiểm toán** — dùng làm trần, không dùng làm trung bình.
4. **Sensor Tower — *State of AI 2026*** · 16/06/2026. Doanh thu in-app của ứng dụng AI tiêu dùng **>$4 tỷ trong nửa đầu 2026** (+36% so với nửa cuối 2025); thời gian sử dụng **36 tỷ giờ** nửa đầu 2026 so với 17,2 tỷ cùng kỳ 2025. Phương pháp panel ước lượng.
5. **a16z — *Top 100 Gen AI Consumer Apps*, bản thứ 6** · https://a16z.com/100-gen-ai-apps-6/ · 09/03/2026. Dữ liệu SimilarWeb + Sensor Tower + Yipit — **ước tính bên thứ ba**, không phải số công ty công bố.

### 8.2 Benchmark cho B2B

6. **ICONIQ — *2026 State of AI: Bi-Annual Snapshot*** · 01/2026. ~300 lãnh đạo công ty phần mềm, khảo sát quý 4/2025. Số dùng: **GTM mix sales-led 38% · PLG 30% · hybrid 29% · channel/partner 3%**; gross margin **41% (2024) → 45% (2025) → 52% (2026P)**; chi phí inference **20% → 23%** cấu trúc chi phí.
7. **ICONIQ — *State of AI 2026*** · https://www.iconiq.com/growth/reports/state-of-ai-2026 · 07/2026. Gross margin **45% (2025) → 53% (2026P) → 59% (2027P)**. Cũng là nguồn của các số Day 25 đã dùng: **92%** công ty nói chi phí AI khó dự đoán; **84%** đẩy ít nhất một phần hoá đơn token sang khách, chỉ **15%** tự gánh 100%.
8. **ICONIQ — *State of Go-to-Market 2026*** · https://www.iconiq.com/growth/reports/state-of-go-to-market-2026 · 2026. 150+ lãnh đạo GTM phần mềm B2B. Chu kỳ bán **~19 tuần** (từ ~25 tuần năm 2025); **24 tuần** cho deal $100K+; POC/free-trial → paid **~50%** (từ ~36%).
9. **Menlo Ventures — *2025: The State of Generative AI in the Enterprise*** · https://menlovc.com/perspective/2025-the-state-of-generative-ai-in-the-enterprise/ · 09/12/2025. ~500 người ra quyết định AI tại doanh nghiệp Mỹ. Chi tiêu gen-AI doanh nghiệp **$1,7B (2023) → $11,5B (2024) → $37B (2025)**; buy-vs-build lật **47/53 (2024) → 24/76 (2025)**; dự án AI vào vận hành thật **47%** so với 25% của phần mềm truyền thống.
10. **Benchmarkit — *2025 SaaS Performance Metrics*** · https://www.benchmarkit.ai/2025benchmarks · 2025 (dữ liệu năm tài chính 2024). Trung vị: gross margin **77%**, GRR **88%**, **NRR 101%**, CAC ratio $2,00, tăng trưởng 26%. ⚠️ *Bản miễn phí không công bố cỡ mẫu và không chia theo phân khúc.*
11. **Ngưỡng CAC payback theo phân khúc** (SMB <12 · Mid-market <18 · Enterprise <24 tháng) và **LTV:CAC ≥ 3** — giữ nguyên nguồn đã dùng ở Day 25 §8.3 (Bessemer, *Scaling to $100 Million*; David Skok, *SaaS Metrics 2.0*).

### 8.3 Kênh, marketplace và B2B2C

12. **a16z — *On B2B2C Business Models*** (Alex Rampell) · https://a16z.com/on-b2b2c-business-models/ · 17/05/2018. Khung được trích dẫn nhiều nhất về B2B2C: điều kiện thành công, nguyên tắc "Give > Get", và 4 failure mode (partner không đẩy · khách lẫn lộn thương hiệu · partner nghi ngại dữ liệu · partner đòi white-label). ⚠️ *Viết trước LLM bốn năm — không nói gì về chi phí inference.*
13. **AWS Marketplace — biểu phí niêm yết** · https://docs.aws.amazon.com/marketplace/latest/userguide/listing-fees.html · hiệu lực 05/01/2024. SaaS public offer **3%**; server/AMI/container/ML **20%**; private offer 3% (<$1M) / 2% ($1–10M) / 1,5% (>$10M); gia hạn 1,5%.
14. **Salesforce AppExchange Checkout — tỷ lệ chia sẻ doanh thu** · https://developer.salesforce.com/docs/atlas.en-us.packagingGuide.meta/packagingGuide/appexchange_checkout_rev_share.htm · **15%** cho mọi hình thức thanh toán.
15. **Intercom — trang giá** · https://www.intercom.com/pricing · kiểm tra 27/08/2026. Fin **từ $0,99/resolution**, không tính phí seat khi chạy trên helpdesk bên thứ ba. Bối cảnh tăng trưởng và việc xoá bỏ ~$60 triệu ARR cũ: https://www.mostlymetrics.com/p/how-intercom-reaccelerated-growth-with-outcome-based-pricing (03/03/2026, phân tích bên thứ ba).
16. **Salesforce Agentforce — trang giá** · https://www.salesforce.com/agentforce/pricing/ · trang cập nhật 31/07/2026. **$2/conversation** hoặc Flex Credits **$500 / 100.000** (≈ $0,10/action, $0,15 cho voice action). *Trang này không nói gì về ai chịu chi phí inference hay ai sở hữu dữ liệu — bản thân điều đó là một dữ kiện.*
17. **Klarna — thông cáo báo chí về trợ lý AI** · https://www.prnewswire.com/news-releases/klarna-ai-assistant-handles-two-thirds-of-customer-service-chats-in-its-first-month-302072740.html · 27/02/2024. ⚠️ *Thông cáo báo chí công ty, không kiểm toán, phát hành trước IPO — con số $40 triệu là ước tính của chính Klarna.* Phần đảo chiều 05/2025: https://www.emarketer.com/content/klarna-backtracks-ai-customer-service-plans (08/05/2025, dẫn Bloomberg).

### 8.4 Ba con số bạn sẽ nghe rất nhiều — và nên cẩn thận

Giữ đúng thói quen Day 25: nói rõ cái gì có nguồn, cái gì đã bị lan truyền méo đi.

**① *"95% pilot AI thất bại."*** Báo cáo gốc là MIT Media Lab / Project NANDA, *State of AI in Business 2025* (08/2025), đo **300 dự án AI, 150 phỏng vấn lãnh đạo, 350 khảo sát nhân viên**. Phát hiện thật là 95% **"không đo được tác động lên P&L"** — không giống "thất bại", vì **phần lớn pilot không có baseline trước triển khai**, nên "không đo được" là kết quả mặc định. Báo cáo không qua bình duyệt và bị phê bình về cách chọn mẫu. Phát hiện thật sự hữu ích trong báo cáo đó lại là chuyện khác: **~67% công cụ đi mua thành công, so với ~22% tự xây**. Phân tích: https://agentmodeai.com/the-mit-genai-pilot-failure-claim/

**② *"OpenAI lỗ trên gói $200/tháng."*** Đúng — nhưng là phát biểu của Sam Altman trên X vào **tháng 01/2025** (https://x.com/sama/status/1876104315296968813), *"người ta dùng nhiều hơn chúng tôi tưởng rất nhiều"*. **Chưa từng được cập nhật kể từ đó.** Bằng chứng 2026 đi theo hướng ngược lại: Duolingo công bố **chi phí AI bên thứ ba trên mỗi đơn vị giảm** (08/2026). Nếu bạn dùng con số này khi pitch, hãy nói kèm năm.

**③ *"Gross margin công ty AI là 50–60%."*** Nguồn gốc là a16z, *The New Business of AI* (https://a16z.com/the-new-business-of-ai-and-how-its-different-from-traditional-software/), **16/02/2020** — đã 6 năm. Số đo thực tế hiện nay: **45% (2025) → 53% (2026P) → 59% (2027P)** (ICONIQ). Luận điểm gốc vẫn đúng về hướng, con số thì đã lỗi thời.

**④ Và một điều không tồn tại:** **không có bộ benchmark công bố nào chia CAC / payback / NRR / ACV theo B2C vs B2B vs B2B2C.** Mình đã rà ICONIQ, Bessemer, Benchmarkit, Menlo. Tất cả chia theo quy mô doanh thu hoặc tốc độ tăng trưởng. Ai đưa bạn một bảng "benchmark theo archetype" trọn gói thì gần như chắc chắn là tự tổng hợp mà không nói ra.

**⑤ Tỷ lệ rev-share white-label/OEM trong ngành AI:** **không nhà cung cấp, marketplace hay khảo sát nào công bố.** ElevenLabs ghi rõ mọi điều khoản nằm trong hợp đồng riêng. Hai mốc duy nhất truy được là phí marketplace ở mục 13 và 14.

### 8.5 Tham chiếu Việt Nam

18. **FPT.AI** · https://fpt.ai/ · kiểm tra 27/08/2026. Công bố **3.000+ khách hàng doanh nghiệp**, **16 triệu+ người dùng cuối**, **200 triệu+ tương tác tự động**; khách gồm MB Bank, BIDV, Sacombank, HDBank, FWD, Home Credit. **Không công bố giá.** ⚠️ *Số do chính công ty công bố, không có kiểm chứng độc lập.*
19. **KiotViet — thông báo điều chỉnh giá** · https://www.kiotviet.vn/kiotviet-thong-bao-dieu-chinh-gia-ban-san-pham-phan-mem-quan-ly-ban-hang/ · hiệu lực 01/05/2025. **250.000 / 310.000 / 490.000 ₫/tháng**. Đây là **điểm dữ liệu công khai tốt nhất về mức chi trả phần mềm của SME Việt Nam** — hữu ích khi bạn cần neo giá cho thị trường trong nước.
20. **MISA** · https://www.misa.vn/ · kiểm tra 27/08/2026. 400.000+ doanh nghiệp & hộ kinh doanh; 3,5 triệu+ người dùng cá nhân; AMIS OneAI **từ 500.000 ₫/tháng**.
21. **Zalo ZNS — bảng giá** ⚠️ *nguồn từ đại lý, không phải trang chính chủ*: khoảng **120–300 ₫/tin** tuỳ loại (xác thực / thanh toán / hành chính), tính tiền khi gửi thành công. **Kiểm tra lại với đối tác chính thức trước khi đưa vào mô hình.**
22. **Báo cáo AI Việt Nam 2025** (Viện CNTT, ĐHQG Hà Nội — khảo sát ~500 doanh nghiệp, 07/2025), qua cổng Bộ KH&CN · https://mst.gov.vn/cac-nganh-nao-o-viet-nam-dang-tang-toc-ung-dung-ai-197251122182057807.htm · 24/11/2025. Rào cản lớn nhất: **thiếu nhân lực 45%**, pháp lý chưa rõ 30%, hạ tầng dữ liệu 23%; **50% doanh nghiệp nói khó hoặc không tiếp cận được bộ dữ liệu chuẩn**.

### 8.6 Các case đổi hướng được dẫn trong bài

23. **OpenAI — doanh thu enterprise vượt consumer**, CFO Sarah Friar phát biểu trước cổ đông, CNBC đưa tin **14/08/2026**; công ty vào năm 2026 ở tỷ lệ 60 consumer / 40 enterprise, crossover đến **sớm hơn dự báo của chính họ hai quý**. Bối cảnh nền: **1 triệu khách hàng doanh nghiệp, 7 triệu ghế ChatGPT for Work** (https://openai.com/index/1-million-businesses-putting-ai-to-work/, 05/11/2025).
24. **ELSA Speak — từ B2C sang B2B**: Series B $15 triệu (TechCrunch, 31/01/2021) nêu rõ mục tiêu xây "nền tảng B2B" bán cho trường học và doanh nghiệp — đối tác IDP, IMAP, Speak Up, YOLA, Kimberly-Clark, Intel, ATAD. Series C $23 triệu (09/2023) với 34 triệu+ người dùng. ⚠️ *Con số "50 triệu người dùng" lan truyền trên mạng không truy được về nguồn — số công bố gần nhất là 34 triệu+ (2023).*
25. **Jasper — từ prosumer sang enterprise** · https://research.contrary.com/company/jasper · 02/02/2024. ARR $42,5M (2021) → $80M (2022); định giá $1,5 tỷ (10/2022) bị cắt nội bộ ~20%; chuyển hướng sang đội marketing doanh nghiệp sau cú sốc ChatGPT ra mắt 11/2022.
26. **Grammarly → business** · https://www.businesswire.com/news/home/20250529436291/en/ · 29/05/2025. >$700 triệu doanh thu năm, 40 triệu+ người dùng hằng ngày, **50.000 tổ chức**.

---

## Quick reference — các câu chốt Day 26

> **Day 24 dạy bạn bảng điểm. Day 26 dạy bạn bảng điều khiển. Không ai lái xe bằng bảng điểm.**

> **Startup không chết vì thiếu metric. Chết vì canh nhầm metric.**

> **B2C: đèn bật trước là đường cong retention có phẳng không.**
> **B2B: đèn bật trước là time-to-first-value.**
> **B2B2C: đèn bật trước là partner activation — ký được không phải là thắng.**

> **Nếu bạn không nói được "đèn này báo trước cho đèn nào", đó không phải leading indicator — đó là một con số bạn thích nhìn.**

> **Ngưỡng không có lý do không phải là ngưỡng. Đó là một điều ước.**

> **Viết luật trước khi đèn đỏ — vì lúc đèn đỏ là lúc bạn hoảng, và người hoảng ra quyết định tệ.**

> **Luật khó viết nhất là luật bảo bạn dừng một việc đang làm. Nó cũng là luật cứu bạn nhiều nhất.**

> **Dashboard toàn màu xanh là dashboard không đo gì cả.**

> **FIX chỉ được dùng một lần cho một vấn đề. FIX lần hai là PIVOT đang giả trang.**
