"""PROXI 表之**值域**快取（W-VF70，供 B9 判準與值域來源鏈第 3 段用）。

`proxi_known()`（W-VF44）只取參數**名**，不取其值 ——
故「參數在表內」被當成「其值已解」，二者不同。
本檔補取 `Format` 分頁之 `Table` 欄（形如 ` 0 = Absent \\n 1 = Present`）。
"""
import json
import re
from pathlib import Path

import openpyxl

FEAT = Path(__file__).resolve().parent.parent
BOOK = FEAT / "inputs" / "PROXI_HDCC27_R3_20250424.xlsx"
OUT = FEAT / "data" / "_vf230_proxi_values.json"

VAL_LINE = re.compile(r"([0-9A-Fa-f]+)\s*=\s*([A-Za-z][A-Za-z0-9_ /()\-]*)")


def build() -> dict[str, dict[str, str]]:
    wb = openpyxl.load_workbook(BOOK, read_only=True, data_only=True)
    out: dict[str, dict[str, str]] = {}
    # 讀全表（該分頁實有 1060 列）—— 不設上限，見 A-VF27
    for r in wb["Format"].iter_rows(values_only=True):
        name = str(r[5] or "").strip()
        tbl = str(r[8] or "").strip()
        if not name or not tbl:
            continue
        vals = {raw: lab.strip() for raw, lab in VAL_LINE.findall(tbl)}
        if vals:
            out.setdefault(name, {}).update(vals)
    wb.close()
    return out


def main() -> None:
    v = build()
    OUT.write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"PROXI 表有值域之參數 {len(v)} 個 → {OUT.relative_to(FEAT)}")
    # 以正規化名查 —— 表內有 `FOA _Presence`（名中多一空格）
    nv = {re.sub(r"[^a-z0-9]", "", k.lower()): (k, d) for k, d in v.items()}
    for k in ("FOA_Presence", "Hybrid_Type", "AUX_Switch_Types", "Country_Code"):
        hit = nv.get(re.sub(r"[^a-z0-9]", "", k.lower()))
        print(f"  {k:20} {sorted(hit[1].values())[:4] if hit else '**表內無值域**'}"
              + (f"   （表內逐字名 `{hit[0]}`）" if hit and hit[0] != k else ""))


if __name__ == "__main__":
    main()
