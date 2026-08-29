#!/usr/bin/env python3
"""佔位普查（下放包 05 作業 C；A-ICS31 之口徑統一）。

**掃描條件**：對 b01~b04 之每條 TC 之六欄
（`pre_conditions`／`input_test_data`／`test_procedure`／`expected_result`／
`test_item`／`specification_reference`）套
`re.findall(r'PENDING: (DR-ICS\\d+) <([^>]+)>')`。
**禁人工列舉**（下放包 05 §4）—— 本檔即該禁令之工具面。

用法：
  python3 features/ics_management/scripts/pending_census.py          # 印表
  python3 features/ics_management/scripts/pending_census.py --write  # 併寫回四份 manifest
"""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BATCHES = ["b01", "b02", "b03", "b04", "b05", "b06"]
FIELDS = ["pre_conditions", "input_test_data", "test_procedure",
          "expected_result", "test_item", "specification_reference"]
PAT = re.compile(r"PENDING: (DR-ICS\d+) <([^>]+)>")


def census() -> tuple[dict, dict, dict]:
    per_batch: dict[str, int] = {}
    per_dr: dict[str, list[tuple[str, str, str, str]]] = defaultdict(list)
    per_tc: dict[str, int] = defaultdict(int)
    for b in BATCHES:
        p = ROOT / "generated" / b / f"{b}_tcs.json"
        n = 0
        for t in json.loads(p.read_text())["tcs"]:
            for f in FIELDS:
                for dr, item in PAT.findall(t[f]):
                    per_dr[dr].append((b, t["tc_title"], f, item))
                    per_tc[t["tc_title"]] += 1
                    n += 1
        per_batch[b] = n
    return per_batch, dict(per_dr), dict(per_tc)


def main() -> int:
    per_batch, per_dr, per_tc = census()
    total = sum(per_batch.values())
    print("== 逐批 ==")
    for b, n in per_batch.items():
        print(f"  {b}  佔位 {n}")
    print(f"  合計 **{total}** 處，涉 **{len(per_tc)}** 條 TC")
    print("\n== 逐 DR（阻幾處佔位、涉幾條 TC）==")
    print("| DR | 佔位處數 | 涉 TC 數 | 缺件（相異）| 涉及之 TC |")
    print("|---|---|---|---|---|")
    for dr in sorted(per_dr, key=lambda s: int(s.split("ICS")[1])):
        rows = per_dr[dr]
        tcs = sorted({r[1] for r in rows})
        items = sorted({r[3] for r in rows})
        print(f"| {dr} | {len(rows)} | {len(tcs)} | {'；'.join(items)} | {'、'.join(tcs)} |")
    if "--write" in sys.argv:
        for b, n in per_batch.items():
            mp = ROOT / "generated" / b / "manifest.json"
            m = json.loads(mp.read_text())
            m.setdefault("counts", {})["pending_placeholders"] = n
            m["counts"]["pending_source"] = (
                "scripts/pending_census.py 腳本計數（A-ICS31 之口徑統一，禁人工列舉）")
            mp.write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n")
            print(f"\n寫回 {b}/manifest.json：pending_placeholders = {n}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
