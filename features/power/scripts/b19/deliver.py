#!/usr/bin/env python3
"""PM 送達：`pm_19.xlsx` → 客戶目錄，覆蓋 `…_20260821.xlsx`。

Pei 於 2026-08-21 逐字「授權」，並指定覆蓋同名檔（8.1e／8.1f 之作法）。
送達前先備份客戶目錄現有 xlsx（R-P228）；送達為**位元組複製**，
不重新存檔 —— `pm_19.xlsx` 本身即由 `surgical_save()` 產出
（R16／R-G3：`surgical_save` 為唯一寫回路徑，全域無 `Workbook.save()`）。
"""

from __future__ import annotations

import datetime as dt
import hashlib
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "scripts"))

SRC = ROOT / "features/power/sandbox/b19/pm_19.xlsx"
DEST_DIR = Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing"
                "/00_TestCase/ASW-R2/Power Management")
DEST = DEST_DIR / ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA "
                   "Test Case Specification & Result_SWQT_PowerManagement_20260821.xlsx")
BACKUP_ROOT = ROOT / "features/power/sandbox/delivery_backup"


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    assert SRC.is_file() and DEST.is_file() and DEST_DIR.is_dir()

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup = BACKUP_ROOT / stamp
    backup.mkdir(parents=True)
    for f in sorted(DEST_DIR.glob("*.xlsx")):
        shutil.copy2(f, backup / f.name)
        print(f"  備份 {f.name}  {sha256(f)[:16]}")
    print(f"送達前備份 → {backup.relative_to(ROOT)}")

    before = sha256(DEST)
    shutil.copyfile(SRC, DEST)
    after, src = sha256(DEST), sha256(SRC)

    print(f"\n來源   {SRC.name}  {src[:32]}  {SRC.stat().st_size:,} bytes")
    print(f"目的地 覆蓋前 {before[:32]}")
    print(f"目的地 覆蓋後 {after[:32]}  {DEST.stat().st_size:,} bytes")
    print("位元組相同:", "PASS" if after == src else "FAIL")


if __name__ == "__main__":
    main()
