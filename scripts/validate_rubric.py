#!/usr/bin/env python3
"""Validate consistency of the public Day 26 rubric package."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "lab.config.json"
RUBRIC_PATH = ROOT / "rubric" / "rubric-v2.json"
PROFILES_PATH = ROOT / "rubric" / "model-profiles.json"
SCHEMA_PATH = ROOT / "rubric" / "grader-output.schema.json"
RUBRIC_MD_PATH = ROOT / "rubric" / "rubric-v2.md"
EXPECTED_CRITERIA = {"TD": 20, "TQ": 30, "DR": 30, "GT": 15, "HO": 5}
ALLOWED_EVALUATORS = {"deterministic", "semantic", "hybrid"}


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_documents(
    config: dict[str, Any],
    rubric: dict[str, Any],
    profiles: dict[str, Any],
    schema: dict[str, Any],
    rubric_markdown: str,
) -> list[str]:
    errors: list[str] = []
    version = rubric.get("version")
    if version != config.get("rubric_version"):
        errors.append(
            f"version: rubric={version!r} khác config={config.get('rubric_version')!r}"
        )
    if profiles.get("version") != version:
        errors.append("version: model-profiles.json phải cùng version với rubric")
    schema_version = (
        schema.get("properties", {}).get("rubric_version", {}).get("const")
    )
    if schema_version != version:
        errors.append("version: grader output schema phải khóa đúng rubric version")

    criteria = rubric.get("criteria", [])
    if not isinstance(criteria, list):
        return errors + ["criteria: phải là array"]

    criterion_ids: set[str] = set()
    item_ids: set[str] = set()
    criterion_total = 0.0
    for criterion in criteria:
        criterion_id = criterion.get("id")
        if criterion_id in criterion_ids:
            errors.append(f"criteria: ID trùng {criterion_id}")
        criterion_ids.add(criterion_id)
        expected_max = EXPECTED_CRITERIA.get(criterion_id)
        actual_max = criterion.get("max_points")
        if expected_max is None:
            errors.append(f"criteria: ID không hợp lệ {criterion_id!r}")
        elif actual_max != expected_max:
            errors.append(
                f"{criterion_id}: max_points phải là {expected_max}, hiện là {actual_max}"
            )
        if isinstance(actual_max, (int, float)):
            criterion_total += actual_max

        item_total = 0.0
        items = criterion.get("items", [])
        if not items:
            errors.append(f"{criterion_id}: phải có ít nhất một item")
        for item in items:
            item_id = item.get("id")
            points = item.get("max_points")
            if item_id in item_ids:
                errors.append(f"items: ID trùng {item_id}")
            item_ids.add(item_id)
            if not isinstance(item_id, str) or not item_id.startswith(f"{criterion_id}-"):
                errors.append(f"{criterion_id}: item ID sai namespace {item_id!r}")
            if not isinstance(points, (int, float)) or points <= 0:
                errors.append(f"{item_id}: max_points phải là số dương")
            else:
                item_total += points
            if item.get("evaluator") not in ALLOWED_EVALUATORS:
                errors.append(f"{item_id}: evaluator không hợp lệ")
            if not item.get("condition"):
                errors.append(f"{item_id}: thiếu condition")
        if isinstance(actual_max, (int, float)) and item_total != actual_max:
            errors.append(
                f"{criterion_id}: tổng item {item_total:g} khác max_points {actual_max:g}"
            )

    if criterion_ids != set(EXPECTED_CRITERIA):
        errors.append(
            f"criteria: cần {sorted(EXPECTED_CRITERIA)}, hiện có {sorted(criterion_ids)}"
        )
    if criterion_total != rubric.get("total_points") or criterion_total != 100:
        errors.append(
            f"total_points: tổng criteria={criterion_total:g}, rubric={rubric.get('total_points')}"
        )

    cap_ids: set[str] = set()
    for cap in rubric.get("caps", []):
        cap_id = cap.get("id")
        if cap_id in cap_ids:
            errors.append(f"caps: ID trùng {cap_id}")
        cap_ids.add(cap_id)
        criterion_id = cap.get("criterion_id")
        if criterion_id not in criterion_ids:
            errors.append(f"{cap_id}: criterion_id không tồn tại {criterion_id!r}")
        criterion_max = EXPECTED_CRITERIA.get(criterion_id, 0)
        cap_max = cap.get("max_criterion_points")
        if not isinstance(cap_max, (int, float)) or not 0 <= cap_max <= criterion_max:
            errors.append(f"{cap_id}: max_criterion_points không hợp lệ")

    override_ids: set[str] = set()
    for override in rubric.get("overrides", []):
        override_id = override.get("id")
        if override_id in override_ids:
            errors.append(f"overrides: ID trùng {override_id}")
        override_ids.add(override_id)
        pattern = override.get("target_item_pattern", "")
        try:
            compiled = re.compile(f"^(?:{pattern})$")
        except re.error as exc:
            errors.append(f"{override_id}: target_item_pattern lỗi: {exc}")
            continue
        if not any(compiled.fullmatch(item_id) for item_id in item_ids):
            errors.append(f"{override_id}: target_item_pattern không khớp item nào")

    increment = rubric.get("rounding_increment")
    if increment != 0.5:
        errors.append("rounding_increment: release này phải dùng 0.5")
    bands = rubric.get("grade_bands", [])
    for half_point in range(201):
        score = half_point / 2
        matches = [band for band in bands if band.get("min", 101) <= score <= band.get("max", -1)]
        if len(matches) != 1:
            errors.append(f"grade_bands: điểm {score:g} khớp {len(matches)} band")
            break

    expected_models = set(config.get("model_types", []))
    profile_map = profiles.get("profiles", {})
    if set(profile_map) != expected_models:
        errors.append(
            f"model profiles: cần {sorted(expected_models)}, hiện có {sorted(profile_map)}"
        )
    inventory_minima = config.get("candidate_light_inventory_min_by_model", {})
    for model in expected_models:
        candidate_lights = profile_map.get(model, {}).get("candidate_lights", [])
        expected_count = inventory_minima.get(model)
        if len(candidate_lights) != expected_count:
            errors.append(
                f"{model}: candidate_lights cần {expected_count}, hiện có {len(candidate_lights)}"
            )
        if len(candidate_lights) != len(set(candidate_lights)):
            errors.append(f"{model}: candidate_lights có tên trùng")
        if not profile_map.get(model, {}).get("first_light", {}).get("canonical_name"):
            errors.append(f"{model}: thiếu first_light.canonical_name")

    schema_items = schema.get("properties", {}).get("item_results", {})
    if schema_items.get("minItems") != len(item_ids) or schema_items.get("maxItems") != len(
        item_ids
    ):
        errors.append(
            "grader schema: minItems/maxItems phải bằng số rubric items "
            f"({len(item_ids)})"
        )
    required_output = set(schema.get("required", []))
    for field in ("rubric_version", "submission", "item_results", "total_score", "review"):
        if field not in required_output:
            errors.append(f"grader schema: thiếu required field {field}")

    documented_ids = item_ids | cap_ids | override_ids
    for identifier in sorted(documented_ids):
        if f"`{identifier}`" not in rubric_markdown:
            errors.append(f"rubric-v2.md: chưa mô tả {identifier}")

    return errors


def validate_package(root: Path = ROOT) -> list[str]:
    paths = {
        "config": root / "lab.config.json",
        "rubric": root / "rubric" / "rubric-v2.json",
        "profiles": root / "rubric" / "model-profiles.json",
        "schema": root / "rubric" / "grader-output.schema.json",
        "markdown": root / "rubric" / "rubric-v2.md",
    }
    missing = [str(path.relative_to(root)) for path in paths.values() if not path.is_file()]
    if missing:
        return [f"thiếu file: {path}" for path in missing]
    try:
        return validate_documents(
            read_json(paths["config"]),
            read_json(paths["rubric"]),
            read_json(paths["profiles"]),
            read_json(paths["schema"]),
            paths["markdown"].read_text(encoding="utf-8"),
        )
    except (OSError, json.JSONDecodeError) as exc:
        return [f"không đọc được rubric package: {exc}"]


def main() -> int:
    errors = validate_package()
    if errors:
        print(f"FAIL: {len(errors)} rubric package error(s)")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: public rubric package v2.0.0 is internally consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
