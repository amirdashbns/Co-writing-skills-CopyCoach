#!/usr/bin/env python3
"""Build Canva Bulk Create row files (TSV + XLSX) from field values."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from openpyxl import Workbook

CANVA_HEADERS = [
    "Title",
    "Body1_Heading", "Body1_P1", "Body1_P2",
    "Body2_Heading", "Body2_P1", "Body2_P2",
    "Body3_Heading", "Body3_P1", "Body3_P2",
    "Body4_Heading", "Body4_P1", "Body4_P2",
    "Body5_Heading", "Body5_P1", "Body5_P2",
    "Body6_Heading", "Body6_P1", "Body6_P2",
    "Body7_Heading", "Body7_P1", "Body7_P2",
    "Takeaway",
    "CTA_Question",
    "CTA_Steps",
]


def values_from_mapping(data: dict[str, str]) -> list[str]:
    missing = [h for h in CANVA_HEADERS if h not in data]
    if missing:
        raise SystemExit(f"Missing fields: {', '.join(missing)}")
    return [data[h] for h in CANVA_HEADERS]


def write_tsv(path: Path, values: list[str]) -> None:
    path.write_text("\t".join(values) + "\n", encoding="utf-8")


def write_xlsx(path: Path, values: list[str]) -> None:
    wb = Workbook()
    ws = wb.active
    ws.title = "Carousel Data"
    ws.append(CANVA_HEADERS)
    ws.append(values)
    wb.save(path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--json",
        type=Path,
        help="JSON object keyed by field name (Title, Body1_Heading, ...)",
    )
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=Path("knowledge/drafts"),
        help="Output directory (default: knowledge/drafts)",
    )
    parser.add_argument(
        "--slug",
        required=True,
        help="Filename slug, e.g. voice-strategy-carousel",
    )
    args = parser.parse_args()

    if not args.json:
        raise SystemExit("--json is required")

    data = json.loads(args.json.read_text(encoding="utf-8"))
    values = values_from_mapping(data)

    args.out_dir.mkdir(parents=True, exist_ok=True)
    tsv_path = args.out_dir / f"{args.slug}-canva-row.tsv"
    xlsx_path = args.out_dir / f"{args.slug}-canva-row.xlsx"

    write_tsv(tsv_path, values)
    write_xlsx(xlsx_path, values)

    print(tsv_path)
    print(xlsx_path)


if __name__ == "__main__":
    main()
