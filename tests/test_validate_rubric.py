from __future__ import annotations

import copy
import importlib.util
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_rubric.py"
SPEC = importlib.util.spec_from_file_location("validate_rubric", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Cannot import rubric validator from {MODULE_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


class ValidateRubricTests(unittest.TestCase):
    def setUp(self) -> None:
        self.config = load_json(ROOT / "lab.config.json")
        self.rubric = load_json(ROOT / "rubric" / "rubric-v2.json")
        self.profiles = load_json(ROOT / "rubric" / "model-profiles.json")
        self.schema = load_json(ROOT / "rubric" / "grader-output.schema.json")
        self.markdown = (ROOT / "rubric" / "rubric-v2.md").read_text(encoding="utf-8")

    def validate(
        self,
        *,
        config: dict | None = None,
        rubric: dict | None = None,
        profiles: dict | None = None,
        schema: dict | None = None,
        markdown: str | None = None,
    ) -> list[str]:
        return VALIDATOR.validate_documents(
            config or self.config,
            rubric or self.rubric,
            profiles or self.profiles,
            schema or self.schema,
            markdown if markdown is not None else self.markdown,
        )

    def test_public_package_is_consistent(self) -> None:
        self.assertEqual([], self.validate())

    def test_criterion_item_sum_mismatch_is_rejected(self) -> None:
        rubric = copy.deepcopy(self.rubric)
        rubric["criteria"][0]["items"][0]["max_points"] = 5
        errors = self.validate(rubric=rubric)
        self.assertTrue(any("tổng item" in error for error in errors))

    def test_duplicate_item_id_is_rejected(self) -> None:
        rubric = copy.deepcopy(self.rubric)
        rubric["criteria"][1]["items"][0]["id"] = "TD-01"
        errors = self.validate(rubric=rubric)
        self.assertTrue(any("ID trùng TD-01" in error for error in errors))

    def test_model_inventory_count_mismatch_is_rejected(self) -> None:
        profiles = copy.deepcopy(self.profiles)
        profiles["profiles"]["B2C"]["candidate_lights"].pop()
        errors = self.validate(profiles=profiles)
        self.assertTrue(any("B2C: candidate_lights" in error for error in errors))

    def test_schema_item_count_mismatch_is_rejected(self) -> None:
        schema = copy.deepcopy(self.schema)
        schema["properties"]["item_results"]["maxItems"] = 99
        errors = self.validate(schema=schema)
        self.assertTrue(any("minItems/maxItems" in error for error in errors))

    def test_undocumented_public_id_is_rejected(self) -> None:
        errors = self.validate(markdown=self.markdown.replace("`HO-05`", "HO-05"))
        self.assertTrue(any("chưa mô tả HO-05" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
