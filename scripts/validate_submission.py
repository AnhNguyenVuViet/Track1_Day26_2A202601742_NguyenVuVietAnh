#!/usr/bin/env python3
"""Validate the Markdown source of a Day 26 Operating Dashboard.

The validator intentionally checks only structure and traceability. It cannot
decide whether a benchmark is current, a threshold is commercially sound, or a
decision rule is wise.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "lab.config.json"
PLACEHOLDER_RE = re.compile(
    r"<(?:\[[A-Z]+\]|[A-ZÀ-Ỹ])[^<>\n|]{0,100}>|"
    r"\b(?:TODO|TBD|FIXME)\b|\[\s*\.\.\.\s*\]",
    re.I,
)
DATE_RE = re.compile(r"\b20\d{2}-\d{2}-\d{2}\b")
NUMBER_RE = re.compile(r"\d")
SOURCE_RE = re.compile(r"\[(BM|MH|TB)\]", re.I)
URL_RE = re.compile(r"https?://[^\s|)>]+", re.I)
MH_ID_RE = re.compile(r"\bMH-\d{2}\b", re.I)
VAGUE_ACTION_RE = re.compile(
    r"\b(xem xét|cân nhắc|theo dõi thêm|đánh giá lại|cải thiện sản phẩm|tối ưu thêm)\b",
    re.I,
)
DAY_30_REVENUE_RE = re.compile(r"\b(doanh thu|revenue|arr|mrr)\b", re.I)

REQUIRED_SECTIONS = (
    "Chẩn đoán mô hình",
    "Kiểm kê đèn ứng viên",
    "Đèn báo sớm",
    "Đèn vận hành",
    "Đèn kết quả",
    "Luật quyết định",
    "Cổng gác 90 ngày",
    "Kill criteria",
    "Chưa đo được",
    "Phụ lục ngưỡng suy từ mô hình",
)


def load_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


def parse_sections(text: str) -> dict[str, str]:
    """Return exact H2 title -> body until the next H2."""
    matches = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", text))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections[match.group(1).strip()] = text[match.end() : end].strip()
    return sections


def parse_metadata(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for key, value in re.findall(r"(?m)^-\s+([^:]+):\s*(.+?)\s*$", text):
        fields[key.strip()] = value.strip()
    return fields


def parse_table(section: str) -> list[list[str]]:
    """Parse the first Markdown table in a section, excluding header/separator."""
    raw_rows: list[list[str]] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            if raw_rows:
                break
            continue
        cells = [cell.strip() for cell in stripped[1:-1].split("|")]
        raw_rows.append(cells)
    if len(raw_rows) < 2:
        return []
    return raw_rows[2:]


def require_date(value: str, field: str, errors: list[str]) -> None:
    match = DATE_RE.search(value)
    if match is None:
        errors.append(f"{field}: cần ngày ISO YYYY-MM-DD")
        return
    try:
        date.fromisoformat(match.group(0))
    except ValueError:
        errors.append(f"{field}: ngày không hợp lệ")


def nonempty_cells(row: list[str], expected: int, field: str, errors: list[str]) -> bool:
    if len(row) < expected:
        errors.append(f"{field}: cần ít nhất {expected} cột, hiện có {len(row)}")
        return False
    empty = [str(index + 1) for index, value in enumerate(row[:expected]) if not value.strip()]
    if empty:
        errors.append(f"{field}: cột trống {', '.join(empty)}")
        return False
    return True


def validate_metrics(
    sections: dict[str, str], config: dict, errors: list[str]
) -> tuple[set[str], int, set[str]]:
    groups = (
        ("Đèn báo sớm", "L-", "leading"),
        ("Đèn vận hành", "O-", "operating"),
        ("Đèn kết quả", "G-", "lagging"),
    )
    metric_ids: set[str] = set()
    all_rows: list[list[str]] = []
    mh_count = 0
    mh_refs: set[str] = set()
    group_counts: dict[str, int] = {}

    for section_name, prefix, group_name in groups:
        rows = parse_table(sections.get(section_name, ""))
        group_counts[group_name] = len(rows)
        for row_number, row in enumerate(rows, start=1):
            field = f"{section_name}: hàng {row_number}"
            if not nonempty_cells(row, 12, field, errors):
                continue
            metric_id = row[0]
            if not metric_id.startswith(prefix):
                errors.append(f"{field}: ID phải bắt đầu bằng {prefix}")
            if metric_id in metric_ids:
                errors.append(f"{field}: ID trùng {metric_id}")
            metric_ids.add(metric_id)

            cadence_owner = row[3]
            separator = config["cadence_owner_separator"]
            cadence_parts = [part.strip() for part in cadence_owner.split(separator)]
            if len(cadence_parts) != 2 or not all(cadence_parts):
                errors.append(
                    f"{field}: Nhịp · Owner phải theo dạng TUẦN {separator} PRODUCT OPS"
                )

            thresholds = row[5:8]
            if len(set(thresholds)) < 3:
                errors.append(f"{field}: ba vùng xanh/vàng/đỏ phải khác nhau")

            source_tags = SOURCE_RE.findall(row[8])
            if len(source_tags) != 1:
                errors.append(
                    f"{field}: nguồn phải chứa đúng một tag [BM], [MH] hoặc [TB]"
                )
            else:
                source_type = source_tags[0].upper()
                if source_type == "MH":
                    mh_count += 1
                    refs = {match.upper() for match in MH_ID_RE.findall(row[8])}
                    if not refs:
                        errors.append(f"{field}: nguồn [MH] phải tham chiếu MH-01 hoặc MH-02")
                    mh_refs.update(refs)
                if source_type == "BM":
                    if URL_RE.search(row[8]) is None:
                        errors.append(f"{field}: nguồn [BM] phải có URL http(s) trực tiếp")
                    require_date(row[9], f"{field} ngày kiểm tra benchmark", errors)
            require_date(row[9], f"{field} ngày kiểm tra", errors)
            all_rows.append(row)

    total = len(all_rows)
    if total < config["metric_count_min"] or total > config["metric_count_max"]:
        errors.append(
            "metrics: cần "
            f"{config['metric_count_min']}–{config['metric_count_max']} đèn; hiện có {total}"
        )
    if group_counts.get("leading", 0) < config["leading_metric_min"]:
        errors.append(f"metrics: cần ít nhất {config['leading_metric_min']} đèn Leading")
    if group_counts.get("operating", 0) < config["operating_metric_min"]:
        errors.append(f"metrics: cần ít nhất {config['operating_metric_min']} đèn Operating")
    if group_counts.get("lagging", 0) > config["lagging_metric_max"]:
        errors.append(f"metrics: tối đa {config['lagging_metric_max']} đèn Lagging")
    joined = " ".join(" ".join(row) for row in all_rows).lower()
    if not any(term in joined for term in ("chi phí ai", "ai cost", "inference", "token", "cost/job")):
        errors.append("metrics: cần ít nhất một đèn bắt chi phí AI/token/inference")
    if mh_count < config["model_derived_threshold_min"]:
        errors.append(
            "metrics: cần ít nhất "
            f"{config['model_derived_threshold_min']} ngưỡng [MH]; hiện có {mh_count}"
        )
    return metric_ids, mh_count, mh_refs


def validate_inventory(
    section: str, model_type: str, config: dict, errors: list[str]
) -> None:
    rows = parse_table(section)
    required = config["candidate_light_inventory_min_by_model"].get(model_type)
    if required is not None and len(rows) < required:
        errors.append(
            f"Kiểm kê đèn ứng viên: model {model_type} cần ít nhất {required} hàng; "
            f"hiện có {len(rows)}"
        )
    names: set[str] = set()
    allowed_statuses = set(config["candidate_light_statuses"])
    for row_number, row in enumerate(rows, start=1):
        field = f"Kiểm kê đèn ứng viên: hàng {row_number}"
        if not nonempty_cells(row, 4, field, errors):
            continue
        normalized_name = row[0].strip().casefold()
        if normalized_name in names:
            errors.append(f"{field}: tên đèn ứng viên bị trùng {row[0]!r}")
        names.add(normalized_name)
        if row[1].strip().upper() not in {"L", "O", "G"}:
            errors.append(f"{field}: tầng phải là L, O hoặc G")
        if row[2].strip() not in allowed_statuses:
            errors.append(
                f"{field}: trạng thái phải là một trong {'/'.join(config['candidate_light_statuses'])}"
            )


def validate_model_inputs(section: str, errors: list[str]) -> None:
    rows = parse_table(section)
    if len(rows) < 2:
        errors.append("Chẩn đoán mô hình: cần inventory input của cả Day 24 và Day 25")
    for row_number, row in enumerate(rows, start=1):
        field = f"Chẩn đoán mô hình: input hàng {row_number}"
        if not nonempty_cells(row, 4, field, errors):
            continue
        require_date(row[3], f"{field} ngày có số", errors)


def validate_rules(
    section: str, config: dict, metric_ids: set[str], errors: list[str]
) -> set[str]:
    rows = parse_table(section)
    expected = config["decision_rule_count"]
    if len(rows) != expected:
        errors.append(f"Luật quyết định: cần đúng {expected} luật; hiện có {len(rows)}")
    rule_ids: set[str] = set()
    stop_count = 0
    for row_number, row in enumerate(rows, start=1):
        field = f"Luật quyết định: hàng {row_number}"
        if not nonempty_cells(row, 7, field, errors):
            continue
        rule_id = row[0]
        if not re.fullmatch(r"R-\d{2}", rule_id):
            errors.append(f"{field}: ID phải theo dạng R-01")
        if rule_id in rule_ids:
            errors.append(f"{field}: ID trùng {rule_id}")
        rule_ids.add(rule_id)
        if VAGUE_ACTION_RE.search(row[4]):
            errors.append(f"{field}: vế THÌ còn hành động mơ hồ ({row[4]!r})")
        if not NUMBER_RE.search(row[1]):
            errors.append(f"{field}: vế NẾU cần có ngưỡng số")
        if not NUMBER_RE.search(row[2]):
            errors.append(f"{field}: vế TRONG cần có window định lượng")
        if not NUMBER_RE.search(row[3]):
            errors.append(f"{field}: vế VÀ cần có mẫu tối thiểu hoặc điều kiện định lượng")
        stop_flag = row[6].strip().upper()
        true_flags = {"CÓ", "CO", "YES", "TRUE", "⏹"}
        false_flags = {"KHÔNG", "KHONG", "NO", "FALSE"}
        if stop_flag in true_flags:
            stop_count += 1
        elif stop_flag not in false_flags:
            errors.append(f"{field}: Luật dừng? phải là CÓ hoặc KHÔNG")
    if stop_count < config["stop_rule_min"]:
        errors.append(
            f"Luật quyết định: cần ít nhất {config['stop_rule_min']} luật dừng; hiện có {stop_count}"
        )
    return rule_ids


def validate_metric_rule_refs(sections: dict[str, str], rule_ids: set[str], errors: list[str]) -> None:
    for section_name in ("Đèn báo sớm", "Đèn vận hành", "Đèn kết quả"):
        for row_number, row in enumerate(parse_table(sections.get(section_name, "")), start=1):
            if len(row) >= 12 and row[11] not in rule_ids:
                errors.append(
                    f"{section_name}: hàng {row_number} tham chiếu luật không tồn tại {row[11]!r}"
                )


def validate_gates(section: str, config: dict, errors: list[str]) -> None:
    rows = parse_table(section)
    if len(rows) != len(config["gate_days"]):
        errors.append(
            "Cổng gác 90 ngày: cần đúng "
            f"{len(config['gate_days'])} hàng; hiện có {len(rows)}"
        )
    found_days: set[int] = set()
    allowed = set(config["gate_decisions"])
    pass_decision = config["gate_pass_decision"]
    fail_decisions = set(config["gate_fail_decisions"])
    for row_number, row in enumerate(rows, start=1):
        field = f"Cổng gác 90 ngày: hàng {row_number}"
        if not nonempty_cells(row, 6, field, errors):
            continue
        day_match = re.search(r"\d+", row[0])
        if day_match:
            found_days.add(int(day_match.group(0)))
        if not NUMBER_RE.search(row[2]):
            errors.append(f"{field}: ngưỡng phải có số")
        for decision in row[4:6]:
            if decision.strip().upper() not in allowed:
                errors.append(
                    f"{field}: quyết định {decision!r} phải là {', '.join(sorted(allowed))}"
                )
        achieved = row[4].strip().upper()
        failed = row[5].strip().upper()
        if achieved != pass_decision:
            errors.append(f"{field}: Nếu đạt phải là {pass_decision}")
        if failed not in fail_decisions:
            errors.append(
                f"{field}: Nếu trượt phải là {', '.join(sorted(fail_decisions))}"
            )
        if achieved == failed:
            errors.append(f"{field}: quyết định đạt và trượt không được giống nhau")
        if day_match and int(day_match.group(0)) == 30 and DAY_30_REVENUE_RE.search(row[1]):
            errors.append(f"{field}: ngày 30 phải đo learning/validation, không dùng doanh thu")
    required = set(config["gate_days"])
    if found_days != required:
        errors.append(
            f"Cổng gác 90 ngày: cần đúng ngày {sorted(required)}; hiện có {sorted(found_days)}"
        )


def validate_appendix(section: str, config: dict, errors: list[str]) -> set[str]:
    rows = parse_table(section)
    required = config["model_derived_threshold_min"]
    valid = 0
    mh_ids: set[str] = set()
    metric_names: set[str] = set()
    for row_number, row in enumerate(rows, start=1):
        field = f"Phụ lục [MH]: hàng {row_number}"
        if not nonempty_cells(row, 5, field, errors):
            continue
        if not re.fullmatch(r"MH-\d{2}", row[0]):
            errors.append(f"{field}: ID phải theo dạng MH-01")
        elif row[0] in mh_ids:
            errors.append(f"{field}: ID trùng {row[0]}")
        else:
            mh_ids.add(row[0])
        metric_name = row[1].strip().casefold()
        if metric_name in metric_names:
            errors.append(f"{field}: metric phải độc lập với phép tính còn lại")
        metric_names.add(metric_name)
        if not NUMBER_RE.search(row[2]):
            errors.append(f"{field}: input Day 24–25 cần có số và đơn vị")
        if "=" not in row[3] or not NUMBER_RE.search(row[3]):
            errors.append(f"{field}: phép tính cần có số và dấu =")
        else:
            valid += 1
    if valid < required:
        errors.append(f"Phụ lục [MH]: cần ít nhất {required} phép tính; hiện có {valid}")
    required_ids = {f"MH-{index:02d}" for index in range(1, required + 1)}
    if not required_ids.issubset(mh_ids):
        errors.append(
            f"Phụ lục [MH]: cần ID {sorted(required_ids)}; hiện có {sorted(mh_ids)}"
        )
    return mh_ids


def validate_submission(path: Path) -> list[str]:
    config = load_config()
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"không đọc được file: {exc}"]

    if PLACEHOLDER_RE.search(text):
        return [
            "file còn placeholder TODO/TBD/<...>; hãy thay toàn bộ placeholder rồi validate lại"
        ]

    sections = parse_sections(text)
    for section_name in REQUIRED_SECTIONS:
        if section_name not in sections:
            errors.append(f"thiếu section H2: {section_name}")

    metadata = parse_metadata(text)
    for field in ("Học viên", "Mã học viên", "Mô hình", "Cập nhật", "North Star"):
        if not metadata.get(field):
            errors.append(f"metadata: thiếu {field}")
    model_type = metadata.get("Mô hình", "")
    if model_type not in config["model_types"]:
        errors.append(
            f"metadata.Mô hình: phải là {', '.join(config['model_types'])}; hiện là {model_type!r}"
        )
    if metadata.get("Cập nhật"):
        require_date(metadata["Cập nhật"], "metadata.Cập nhật", errors)
    if len(metadata.get("North Star", "")) < 10:
        errors.append("metadata.North Star: cần tên đèn và mục tiêu cụ thể")
    elif not NUMBER_RE.search(metadata["North Star"]):
        errors.append("metadata.North Star: mục tiêu phải có số")

    diagnosis = sections.get("Chẩn đoán mô hình", "")
    diagnosis_prose = diagnosis.split("|", maxsplit=1)[0].strip()
    if len(diagnosis_prose) < 80:
        errors.append("Chẩn đoán mô hình: cần giải thích người trả tiền, người dùng và lý do")
    validate_model_inputs(diagnosis, errors)
    validate_inventory(
        sections.get("Kiểm kê đèn ứng viên", ""), model_type, config, errors
    )

    metric_ids, _, mh_refs = validate_metrics(sections, config, errors)
    rule_ids = validate_rules(sections.get("Luật quyết định", ""), config, metric_ids, errors)
    validate_metric_rule_refs(sections, rule_ids, errors)
    validate_gates(sections.get("Cổng gác 90 ngày", ""), config, errors)
    mh_ids = validate_appendix(
        sections.get("Phụ lục ngưỡng suy từ mô hình", ""), config, errors
    )
    for mh_ref in sorted(mh_refs - mh_ids):
        errors.append(f"metrics: tham chiếu {mh_ref} nhưng phụ lục không có ID này")

    kill = sections.get("Kill criteria", "").strip()
    if len(kill) < 30 or not NUMBER_RE.search(kill):
        errors.append("Kill criteria: cần một câu có số và mốc thời gian")

    unknown_rows = parse_table(sections.get("Chưa đo được", ""))
    if not unknown_rows:
        errors.append("Chưa đo được: cần ít nhất một khoảng trống thật và kế hoạch đo")
    for row_number, row in enumerate(unknown_rows, start=1):
        nonempty_cells(row, 4, f"Chưa đo được: hàng {row_number}", errors)
        if row and row[0].strip().lower() in {"không", "không có", "none", "n/a"}:
            errors.append("Chưa đo được: không dùng 'không có'; hãy ghi một khoảng trống thật")
        if len(row) >= 4:
            require_date(row[3], f"Chưa đo được: hàng {row_number} ngày có số", errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Day 26 Operating Dashboard Markdown")
    parser.add_argument("submission", type=Path, help="path to operating-dashboard.md")
    args = parser.parse_args()
    errors = validate_submission(args.submission)
    if errors:
        print(f"FAIL: {len(errors)} validation error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {args.submission} meets the structural minimum bar")
    print("NOTE: this is not a benchmark freshness check or business-quality score")
    return 0


if __name__ == "__main__":
    sys.exit(main())
