#!/usr/bin/env python3
"""Optional Windows helper to add speaker notes through PowerPoint COM.

Requirements:
- Windows
- Microsoft PowerPoint installed
- pip install pywin32

This is intentionally separate from generate_pptx_from_blueprint.py because it
requires local PowerPoint automation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pptx", required=True)
    parser.add_argument("--blueprint", required=True)
    args = parser.parse_args()

    try:
        import win32com.client  # type: ignore
    except ImportError as exc:
        raise SystemExit("pywin32 is required: pip install pywin32") from exc

    pptx_path = str(Path(args.pptx).resolve())
    blueprint = json.loads(Path(args.blueprint).read_text(encoding="utf-8"))

    app = win32com.client.Dispatch("PowerPoint.Application")
    app.Visible = True
    presentation = app.Presentations.Open(pptx_path)

    for idx, item in enumerate(blueprint, start=1):
        if idx > presentation.Slides.Count:
            break
        slide = presentation.Slides(idx)
        notes_text = item.get("speaker_notes", "")
        source_ids = item.get("source_ids", [])
        if source_ids:
            notes_text += "\n\n来源：" + ", ".join(source_ids)

        # PowerPoint notes page usually contains placeholders.
        # The second placeholder is commonly the notes body, but layouts can vary.
        try:
            notes_shape = slide.NotesPage.Shapes.Placeholders(2)
            notes_shape.TextFrame.TextRange.Text = notes_text
        except Exception:
            print(f"Could not set notes for slide {idx}; layout may not expose placeholder 2.")

    presentation.Save()
    presentation.Close()
    app.Quit()
    print(f"Updated speaker notes: {pptx_path}")


if __name__ == "__main__":
    main()
