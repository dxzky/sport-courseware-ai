#!/usr/bin/env python3
"""Validate slide_blueprint.json.

Usage:
    python scripts/validate_slide_blueprint.py path/to/slide_blueprint.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator


def load_schema() -> dict:
    schema_path = Path(__file__).resolve().parents[1] / "schemas" / "slide_blueprint.schema.json"
    return json.loads(schema_path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("json_path")
    args = parser.parse_args()

    path = Path(args.json_path)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(load_schema())

    errors = [err.message for err in validator.iter_errors(data)]

    slide_numbers = []
    for item in data if isinstance(data, list) else []:
        slide_numbers.append(item.get("slide_no"))
        bullets = item.get("visible_content", {}).get("bullets") or []
        if item.get("layout_type") not in ["title", "section", "references", "summary"] and len(bullets) > 5:
            errors.append(f"slide {item.get('slide_no')}: more than 5 bullets")
        if not item.get("speaker_notes"):
            errors.append(f"slide {item.get('slide_no')}: missing speaker_notes")
        if not item.get("source_ids") and item.get("layout_type") not in ["title", "section"]:
            errors.append(f"slide {item.get('slide_no')}: missing source_ids")

    if len(slide_numbers) != len(set(slide_numbers)):
        errors.append("duplicate slide_no detected")

    if errors:
        print("Validation failed:")
        for e in errors:
            print("-", e)
        raise SystemExit(1)

    print(f"Validation passed. {len(data)} slides checked.")


if __name__ == "__main__":
    main()
