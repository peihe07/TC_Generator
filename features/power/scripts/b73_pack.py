"""72 包 §H 第 2 步 —— `sandbox/b73/pm_73.xlsx` ＋ `data/reviewed_287_73.md`。

R-P397(a)：站④ 之標的為全 287 條。
寫入路徑為 `backend/xlsx_surgical.surgical_save()`（同 27 包之方法），
**全域無 `Workbook.save()`**；來源為 `inputs/` 之原始工作簿，**位元組複製後才寫**。
**不複製至 `delivered/`**（R-P397 / §I）。

用法：
    python features/power/scripts/b72_pack.py
"""

from __future__ import annotations

import hashlib
import re
import shutil
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
FEATURE = ROOT / "features/power"
OUTDIR = FEATURE / "sandbox/b73"
OUT = OUTDIR / "pm_73.xlsx"
MD = FEATURE / "data/reviewed_287_73.md"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dryrun_write_back import (HEADER_ROW, FIRST_DATA_ROW, load_cfg,  # noqa: E402
                               row_values, sha256)
from dryrun_full_write_back import BLANK_LEAF, ordered_tcs  # noqa: E402

FIVE = ("test_item", "pre_conditions", "input_test_data",
        "test_procedure", "expected_result")
LABEL = {"test_item": "Test Item", "pre_conditions": "Pre-Conditions",
         "input_test_data": "Input Test Data", "test_procedure": "Test procedure",
         "expected_result": "Expected Result"}


def main() -> None:
    cfg = load_cfg()
    src = FEATURE / cfg["paths"]["workbook"]
    if not src.exists():
        raise SystemExit(f"來源工作簿不存在：{src}")

    OUTDIR.mkdir(parents=True, exist_ok=True)
    work = OUTDIR / "pm_73_src.xlsx"
    shutil.copyfile(src, work)                      # 位元組複製，來源唯讀
    assert sha256(work) == sha256(src), "來源副本非位元組相同"

    tcs = ordered_tcs()
    blank = {k: "" for k in
             ("tc_id", "tc_title", "test_item", "pre_conditions", "input_test_data",
              "test_procedure", "expected_result", "specification_reference",
              "priority", "design_method", "split_flag", "split_reason",
              "functional_safety", "estimated_test_time", "remarks")}
    blank |= {"req_id": BLANK_LEAF, "split_index": 1}   # R-P141 留白列
    pos = next((i for i, t in enumerate(tcs)
                if int(re.match(r"SWE-PM-(\d+)", t["req_id"]).group(1)) > 89), len(tcs))
    rows = tcs[:pos] + [blank] + tcs[pos:]

    sys.path.insert(0, str(ROOT / "backend"))
    from xlsx_surgical import surgical_save
    wb = openpyxl.load_workbook(work)
    ws = wb[cfg["workbook"]["sheet"]]
    for i, tc in enumerate(rows):
        r = FIRST_DATA_ROW + i
        for letter, value in row_values(tc, cfg, r).items():
            ws[f"{letter}{r}"] = value
    surgical_save(wb, work, OUT)                    # **不呼叫 wb.save()**
    work.unlink()

    print(f"pm_72.xlsx  列 {len(rows)}（TC {len(tcs)} ＋ 留白 1）"
          f"  bytes {OUT.stat().st_size}  sha256 {sha256(OUT)[:16]}…")

    # ── 目視包 ──
    md = ["# 站④ 目視包 —— 全 287 條（72 包 / R-P397(a)）", "",
          "> **逐字，不判定、不摘要。** 取代 `reviewed_75_69.md`。",
          f"> 工作簿：`features/power/sandbox/b73/pm_73.xlsx`"
          f"（{len(rows)} 列 = TC {len(tcs)} ＋ `SWE-PM-089` 留白 1，R-P141）。",
          "> **未複製至 `delivered/`**（R-P397 / §I）；Excel GUI 開啟驗證為 Pei 之手動項。",
          "",
          "| # | tc_id | req_id | Remarks |", "|---|---|---|---|"]
    for i, t in enumerate(sorted(tcs, key=lambda x: x["tc_id"]), 1):
        md.append(f"| {i} | `{t['tc_id']}` | `{t['req_id']}` | "
                  f"{(t.get('remarks') or '').strip()} |")
    md.append("")
    for t in sorted(tcs, key=lambda x: x["tc_id"]):
        md += [f"## `{t['tc_id']}`　`{t['req_id']}`　{t.get('tc_title', '')}", ""]
        for f in FIVE:
            md += [f"**{LABEL[f]}**", "", "```",
                   (t.get(f) or "").replace("\xa0", " "), "```", ""]
        md += ["**Remarks**", "", "```", (t.get("remarks") or "").strip(), "```", ""]
    MD.write_text("\n".join(md))
    print(f"目視包 {len(tcs)} 條  bytes {MD.stat().st_size}  → {MD.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
