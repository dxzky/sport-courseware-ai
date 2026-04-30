#!/usr/bin/env python3
"""Validate a source_cards.jsonl file.

Usage:
    python scripts/validate_source_cards.py path/to/source_cards.jsonl
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator

REQUIRED_NON_EMPTY = ["source_id", "course", "source_type", "title", "url_or_path"]


def load_schema() -> dict:
    schema_path = Path(__file__).resolve().parents[1] / "schemas" / "source_card.schema.json"
    return json.loads(schema_path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("jsonl_path")
    args = parser.parse_args()

    path = Path(args.jsonl_path)
    if not path.exists():
        raise SystemExit(f"File not found: {path}")

    schema = load_schema()
    validator = Draft202012Validator(schema)

    seen = set()
    errors = []
    count = 0

    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            count += 1
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                errors.append(f"line {line_no}: invalid JSON: {exc}")
                continue

            for err in validator.iter_errors(obj):
                errors.append(f"line {line_no}: schema error: {err.message}")

            for field in REQUIRED_NON_EMPTY:
                if not str(obj.get(field, "")).strip():
                    errors.append(f"line {line_no}: field '{field}' is empty")

            sid = obj.get("source_id")
            if sid in seen:
                errors.append(f"line {line_no}: duplicate source_id: {sid}")
            seen.add(sid)

            if not obj.get("usable_claims"):
                errors.append(f"line {line_no}: usable_claims is empty")

    if errors:
        print("Validation failed:")
        for e in errors:
            print("-", e)
        raise SystemExit(1)

    print(f"Validation passed. {count} source cards checked.")


if __name__ == "__main__":
    main()
