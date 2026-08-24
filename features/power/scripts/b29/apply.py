#!/usr/bin/env python3
"""29 包執行層：依 `plan.json` 套用內容三項至 `b29/pm_29.xlsx`。

不動列數、不動 ID：寫入範圍限 test_item(I)／pre(J)／input(K)／proc(L)／er(M)。
`surgical_save` 單段即足（無插列）。
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
import zipfile
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "backend"))

from xlsx_surgical import StructureError, sheet_members, surgical_save  # noqa: E402

HERE = Path(__file__).resolve().parent
PLAN = HERE / "plan.json"
BASE = ROOT / "features/power/sandbox/b28/pm_28.xlsx"
SANDBOX = ROOT / "features/power/sandbox/b29"
OUT = SANDBOX / "pm_29.xlsx"
ALLOWED = {"I", "J", "K", "L", "M"}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def x14_dropdowns(path: Path, member: str) -> list[str]:
    with zipfile.ZipFile(path) as z:
        xml = z.read(member).decode("utf-8")
    return re.findall(r"<xm:sqref>([^<]*)</xm:sqref>", xml)


def main() -> None:
    plan = json.loads(PLAN.read_text(encoding="utf-8"))
    sheet = plan["sheet"]
    if sha256(BASE) != plan["base_sha256"]:
        raise StructureError(f"基底 sha256 不符：{sha256(BASE)[:20]}")

    member = sheet_members(BASE)[sheet]
    dv_before = x14_dropdowns(BASE, member)

    SANDBOX.mkdir(parents=True, exist_ok=True)
    work = SANDBOX / ".work.xlsx"
    shutil.copyfile(BASE, work)
    wb = openpyxl.load_workbook(work)
    ws = wb[sheet]

    n_cells = 0
    for row, cols in plan["cells"].items():
        for letter, value in cols.items():
            if letter not in ALLOWED:
                raise StructureError(f"計畫觸及非授權欄 {letter}{row}")
            ws[f"{letter}{row}"] = value
            n_cells += 1

    report = surgical_save(wb, work, OUT)
    work.unlink()

    dv_after = x14_dropdowns(OUT, member)
    if dv_before != dv_after:
        raise StructureError(f"x14 讀回不符：{dv_before} → {dv_after}")

    print(f"改寫 {len(plan['cells'])} 列 / {n_cells} 格")
    print(f"x14 讀回 {dv_before} → {dv_after}")
    print("zip 成員", report["members"], "| 差異成員", report["differing"])
    print("out sha256:", sha256(OUT)[:20])


if __name__ == "__main__":
    main()
