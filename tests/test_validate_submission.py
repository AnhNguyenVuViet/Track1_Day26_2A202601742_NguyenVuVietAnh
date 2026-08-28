from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_submission.py"
SPEC = importlib.util.spec_from_file_location("validate_submission", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot import validator from {MODULE_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class ValidateSubmissionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.example_text = (ROOT / "examples" / "b2b-supportpilot-example.md").read_text(
            encoding="utf-8"
        )

    def validate_text(self, text: str) -> list[str]:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "submission.md"
            path.write_text(text, encoding="utf-8")
            return VALIDATOR.validate_submission(path)

    def test_complete_example_passes(self) -> None:
        self.assertEqual([], self.validate_text(self.example_text))

    def test_template_fails_on_placeholders(self) -> None:
        errors = VALIDATOR.validate_submission(ROOT / "templates" / "operating-dashboard-template.md")
        self.assertTrue(any("placeholder" in error for error in errors))

    def test_invalid_model_type_is_rejected(self) -> None:
        text = self.example_text.replace("- Mô hình: B2B", "- Mô hình: Marketplace")
        errors = self.validate_text(text)
        self.assertTrue(any("metadata.Mô hình" in error for error in errors))

    def test_metric_count_below_minimum_is_rejected(self) -> None:
        lines = [
            line
            for line in self.example_text.splitlines()
            if not line.startswith("| O-03 ") and not line.startswith("| G-02 ")
        ]
        errors = self.validate_text("\n".join(lines) + "\n")
        self.assertTrue(any("metrics: cần 6–8" in error for error in errors))

    def test_missing_operating_metric_is_rejected(self) -> None:
        lines = [
            line
            for line in self.example_text.splitlines()
            if not line.startswith(("| O-01 ", "| O-02 ", "| O-03 "))
        ]
        errors = self.validate_text("\n".join(lines) + "\n")
        self.assertTrue(any("đèn Operating" in error for error in errors))

    def test_missing_ai_cost_metric_is_rejected(self) -> None:
        text = self.example_text
        for old, new in (
            ("Chi phí AI", "Chi phí xử lý"),
            ("AI cost", "hạ tầng"),
            ("inference", "hạ tầng"),
            ("token", "request"),
        ):
            text = text.replace(old, new)
        errors = self.validate_text(text)
        self.assertTrue(any("chi phí AI" in error for error in errors))

    def test_too_few_model_derived_thresholds_are_rejected(self) -> None:
        text = self.example_text.replace("[MH]", "[TB]")
        errors = self.validate_text(text)
        self.assertTrue(any("ngưỡng [MH]" in error for error in errors))

    def test_vague_then_action_is_rejected(self) -> None:
        text = self.example_text.replace(
            "Dừng nhận pilot mới trong 14 ngày và cắt onboarding còn một workflow",
            "Xem xét lại onboarding",
        )
        errors = self.validate_text(text)
        self.assertTrue(any("hành động mơ hồ" in error for error in errors))

    def test_too_few_stop_rules_are_rejected(self) -> None:
        text = self.example_text.replace("| CÓ |", "| KHÔNG |")
        errors = self.validate_text(text)
        self.assertTrue(any("luật dừng" in error for error in errors))

    def test_missing_day_90_gate_is_rejected(self) -> None:
        lines = [line for line in self.example_text.splitlines() if not line.startswith("| 90 ")]
        errors = self.validate_text("\n".join(lines) + "\n")
        self.assertTrue(any("cần đúng ngày" in error for error in errors))

    def test_duplicate_gate_row_is_rejected(self) -> None:
        gate = (
            "| 30 | Interview xác nhận pain và workflow | 8/10 champion xác nhận cùng pain moment "
            "| Biên bản phỏng vấn đã redacted | GO | FIX |"
        )
        text = self.example_text.replace(gate, f"{gate}\n{gate}")
        errors = self.validate_text(text)
        self.assertTrue(any("cần đúng 3 hàng" in error for error in errors))

    def test_ascii_comparison_is_not_a_placeholder(self) -> None:
        text = self.example_text.replace(
            "≥65% | 40–64% | <40%",
            "< 40% | 40–60% | > 60%",
        )
        errors = self.validate_text(text)
        self.assertFalse(any("placeholder" in error for error in errors))

    def test_missing_unknown_measurement_plan_is_rejected(self) -> None:
        text = self.example_text.replace(
            "| Tỷ lệ champion có đủ quyền thay đổi workflow | Thêm một câu hỏi quyền quyết định vào form kickoff và audit tám pilot | Product Operations | 2026-09-11 |",
            "",
        )
        errors = self.validate_text(text)
        self.assertTrue(any("khoảng trống thật" in error for error in errors))

    def test_appendix_needs_two_calculations(self) -> None:
        lines = [line for line in self.example_text.splitlines() if not line.startswith("| MH-02 ")]
        errors = self.validate_text("\n".join(lines) + "\n")
        self.assertTrue(any("Phụ lục [MH]" in error for error in errors))

    def test_benchmark_without_direct_url_is_rejected(self) -> None:
        text = self.example_text.replace(
            "https://www.iconiq.com/growth/reports/state-of-go-to-market-2026",
            "nguồn xem trong slide nội bộ",
        )
        errors = self.validate_text(text)
        self.assertTrue(any("[BM] phải có URL" in error for error in errors))

    def test_metric_without_owner_is_rejected(self) -> None:
        text = self.example_text.replace(
            "Tuần · Product Operations | 11 ngày",
            "Tuần | 11 ngày",
        )
        errors = self.validate_text(text)
        self.assertTrue(any("Nhịp · Owner" in error for error in errors))

    def test_inventory_must_cover_model_candidate_table(self) -> None:
        line = "| CAC payback | G | 🔧 | Chuẩn hóa fully-loaded CAC theo quý trước 2026-10-15 |"
        errors = self.validate_text(self.example_text.replace(line, ""))
        self.assertTrue(any("cần ít nhất 11 hàng" in error for error in errors))

    def test_invalid_stop_flag_is_rejected(self) -> None:
        text = self.example_text.replace("| CÓ |", "| CÓ THỂ |", 1)
        errors = self.validate_text(text)
        self.assertTrue(any("phải là CÓ hoặc KHÔNG" in error for error in errors))

    def test_gate_pass_branch_must_be_go(self) -> None:
        text = self.example_text.replace(
            "| GO | FIX |",
            "| FIX | PIVOT |",
            1,
        )
        errors = self.validate_text(text)
        self.assertTrue(any("Nếu đạt phải là GO" in error for error in errors))

    def test_gate_fail_branch_cannot_be_go(self) -> None:
        text = self.example_text.replace("| GO | FIX |", "| GO | GO |", 1)
        errors = self.validate_text(text)
        self.assertTrue(any("Nếu trượt phải là" in error for error in errors))

    def test_day_30_revenue_gate_is_rejected(self) -> None:
        text = self.example_text.replace(
            "Interview xác nhận pain và workflow",
            "Doanh thu tháng",
        )
        errors = self.validate_text(text)
        self.assertTrue(any("ngày 30 phải đo learning" in error for error in errors))

    def test_model_threshold_source_must_reference_appendix_id(self) -> None:
        text = self.example_text.replace("[MH] MH-02", "[MH] Phép tính activation", 1)
        errors = self.validate_text(text)
        self.assertTrue(any("phải tham chiếu MH-01" in error for error in errors))

    def test_north_star_requires_numeric_target(self) -> None:
        text = self.example_text.replace(
            "Median time-to-first-value dưới 7 ngày",
            "Median time-to-first-value dưới bảy ngày",
        )
        errors = self.validate_text(text)
        self.assertTrue(any("mục tiêu phải có số" in error for error in errors))

    def test_duplicate_mh_id_is_rejected(self) -> None:
        text = self.example_text.replace("| MH-02 |", "| MH-01 |", 1)
        errors = self.validate_text(text)
        self.assertTrue(any("ID trùng MH-01" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
