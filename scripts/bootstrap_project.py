#!/usr/bin/env python3
"""Create the standard Courseware-AI directory structure.

Usage:
    python scripts/bootstrap_project.py --root .
"""
from __future__ import annotations

import argparse
from pathlib import Path

COURSES = [
    "电路与电子技术基础",
    "人体生理信号采集与分析",
    "智能体育装备概论",
]
SUBDIRS = [
    "input",
    "source_cards",
    "lesson_plans",
    "ppt",
    "handouts",
    "review_reports",
    "output",
]


def touch_gitkeep(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    gitkeep = path / ".gitkeep"
    if not gitkeep.exists():
        gitkeep.write_text("", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="Project root directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    for name in ["prompts", "skills", "templates", "schemas", "scripts", "docs", "checklists", "examples", "workflows"]:
        touch_gitkeep(root / name)

    for course in COURSES:
        for sub in SUBDIRS:
            touch_gitkeep(root / "courses" / course / sub)

    print(f"Created Courseware-AI structure under: {root}")


if __name__ == "__main__":
    main()
