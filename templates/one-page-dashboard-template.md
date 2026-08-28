# Operating Dashboard — <TÊN SẢN PHẨM>

> Bản rút gọn để xuất trang 1 PDF. Mọi giá trị phải khớp worksheet nguồn; chi
> tiết nguồn và hai phép tính `[MH]` nằm ở phụ lục trang 2.

**Model:** <B2C/B2B/B2B2C> · **Cập nhật:** <YYYY-MM-DD> · **Owner phiên họp:** <VAI TRÒ>

**Chẩn đoán:** <AI TRẢ TIỀN · AI DÙNG · BỀ MẶT END-USER>

**North Star:** <METRIC> · hiện tại <SỐ> · mục tiêu <SỐ> · trạng thái <🟢/🟡/🔴>

## Cây đèn 3 tầng

| Tầng · ID | Metric và định nghĩa ngắn | Hiện tại · 🟢 / 🟡 / 🔴 · Nguồn | Nhịp · Owner | Báo trước cho · Luật |
|---|---|---|---|---|
| L · <L-01> | <ĐIỀN> | <SỐ> · <BA VÙNG> · <[BM]/[MH]/[TB]> | <TUẦN · VAI TRÒ> | <DOWNSTREAM · R-01> |
| L · <L-02> | <ĐIỀN> | <SỐ> · <BA VÙNG> · <[BM]/[MH]/[TB]> | <TUẦN · VAI TRÒ> | <DOWNSTREAM · R-02> |
| O · <O-01> | <ĐIỀN> | <SỐ> · <BA VÙNG> · <[BM]/[MH]/[TB]> | <TUẦN · VAI TRÒ> | <DOWNSTREAM · R-03> |
| O · <O-02> | <CHI PHÍ AI/JOB> | <SỐ> · <BA VÙNG> · <[MH]> | <TUẦN · VAI TRÒ> | <GM · R-04> |
| G · <G-01> | <ĐIỀN> | <SỐ> · <BA VÙNG> · <[BM]/[MH]/[TB]> | <THÁNG · VAI TRÒ> | <KẾT QUẢ · R-05> |
| G · <G-02> | <ĐIỀN> | <SỐ> · <BA VÙNG> · <[BM]/[MH]/[TB]> | <QUÝ · VAI TRÒ> | <KẾT QUẢ · R-05> |

## Luật quyết định

| ID | NẾU · TRONG · VÀ | THÌ | KHÔNG THÌ | Dừng? |
|---|---|---|---|---|
| R-01 | <TRIGGER · WINDOW · MẪU> | <HÀNH ĐỘNG> | <PHẢN XẠ BỊ CẤM> | <CÓ/KHÔNG> |
| R-02 | <TRIGGER · WINDOW · MẪU> | <HÀNH ĐỘNG> | <PHẢN XẠ BỊ CẤM> | <CÓ/KHÔNG> |
| R-03 | <TRIGGER · WINDOW · MẪU> | <HÀNH ĐỘNG> | <PHẢN XẠ BỊ CẤM> | <CÓ/KHÔNG> |
| R-04 | <TRIGGER · WINDOW · MẪU> | <HÀNH ĐỘNG> | <PHẢN XẠ BỊ CẤM> | <CÓ/KHÔNG> |
| R-05 | <TRIGGER · WINDOW · MẪU> | <HÀNH ĐỘNG> | <PHẢN XẠ BỊ CẤM> | <CÓ/KHÔNG> |

## Cổng 90 ngày

| Ngày | Một metric · ngưỡng | Evidence | Đạt / Trượt |
|---:|---|---|---|
| 30 | <LEARNING METRIC · SỐ> | <FILE/LOG/REPORT> | GO / <FIX/PIVOT/KILL> |
| 60 | <OPERATING METRIC · SỐ> | <FILE/LOG/REPORT> | GO / <FIX/PIVOT/KILL> |
| 90 | <MODEL METRIC · SỐ> | <FILE/LOG/REPORT> | GO / <FIX/PIVOT/KILL> |

**Kill criteria:** <ĐIỀU KIỆN CÓ SỐ + MỐC THỜI GIAN + TUYÊN BỐ DỪNG>

**Chưa đo được:** <ĐÈN/GIẢ ĐỊNH> · cần <EVIDENCE> · owner <VAI TRÒ> · có số ngày <YYYY-MM-DD>
