#!/usr/bin/env python3
"""交付候選（SEC-06 §3.2／§3.3）—— `security_v02.xlsx` ＋ 封面類填值。

**只填量測顯示為「逐文件之後設資料」之格**；不新增格、不改版面。
下列三類**不填**，理由見上繳包：
  1. `Reference` sheet —— 實為 Test Case Design Methods 說明表（兩本逐格相同，屬模板）。
  2. `ChangeHistory 修訂履歷` —— 其 A5~A7 三列（A／B／C）兩本逐格相同，屬**表單**之修訂史。
  3. `Cover` 之 `D7` 核准者／`D8` 審查者 —— 填入他人姓名等同代為簽核，不得造。
"""
from __future__ import annotations

import shutil
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from backend.xlsx_surgical import surgical_save          # noqa: E402

SRC = ROOT / "features/security/sandbox/merged/security_v04.xlsx"
OUT_DIR = ROOT / "features/security/sandbox/delivery"
# 檔名式（量測 SWC 0708／Home 0809 逐字）：
#   FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_<Feature>_<YYYYMMDD>.xlsx
NAME = ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
        "STLA Test Case Specification & Result_SWQT_Security_20260917.xlsx")
OUT = OUT_DIR / NAME

# (sheet, cell, value, 依據)
FILL = [
    ("Cover 封面", "D6", "A",
     "首版；ChangeHistory 之版本序為 A／B／C（量測），故首版為 `A`"),
    ("Cover 封面", "G7", "2026-09-17", "本包產出日"),
    ("Cover 封面", "D9", "PeiPYHsu",
     "作者；量測之署名式為 `<中文姓名> <EnglishName>`，中文姓名未見於任何 repo 產物，只填英文名"),
    ("Cover 封面", "G9", "2026-09-17", "作者日期，與 D9 同列"),
    ("Product Document 記錄封面頁", "B3", "NR1L", "SWC `NR1L`／Home `new R1L` → 以 SWC 為準"),
    ("Product Document 記錄封面頁", "B5", "V1.0", "兩本皆 `V1.0`"),
    ("Product Document 記錄封面頁", "B6", "SW Testing", "兩本皆同"),
    ("Product Document 記錄封面頁", "B7", "Confidential", "兩本皆同"),
    ("Product Document 記錄封面頁", "A13", "1", "SWC `1`／Home `V1.0` → 以 SWC 為準"),
    ("Product Document 記錄封面頁", "B13", "初版發佈", "SWC 逐字；Home 為 `Initial Release 初版發布`"),
    ("Product Document 記錄封面頁", "D13", "2026-09-17", "SWC 該格有值（2026-03-02），型態為日期"),
]


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    wb = openpyxl.load_workbook(SRC)
    for sheet, cell, value, _why in FILL:
        ws = wb[sheet]
        ws[cell] = value
    report = surgical_save(wb, SRC, OUT)
    print(f"交付候選 → {OUT.relative_to(ROOT)}")
    print(f"  填值 {len(FILL)} 格")
    print("  surgical:", {k: v for k, v in report.items() if k != "members_patched"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
