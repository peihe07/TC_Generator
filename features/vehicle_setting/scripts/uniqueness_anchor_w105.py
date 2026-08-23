"""W-105 之 Sibling Rows 唯一性掃描（附 R-VS54 錨點）。

判準：同一 TC 之三個可編輯欄（`pre_conditions`／`test_procedure`／
`expected_result`）三者全同者，即為不可分辨之列 ——
§8.2.2「一 leaf 得對多 TC，反向不可」之反面：兩個 leaf 得到同一份 TC。

**錨點（必命中）**：`HeatedSteeringWheel-015/021` 與 `-016/-022` 兩組
（其來源條文僅差 `[On]` vs `[1h: On]`，見 A-VS119）——
掃描若對其回報「無重複」，即該掃描已失效。
"""
from __future__ import annotations

import collections
import json
import re
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
ANCHOR = [{"SWE1-VC-HeatedSteeringWheel-016", "SWE1-VC-HeatedSteeringWheel-022"},
          {"SWE1-VC-HeatedSteeringWheel-021", "SWE1-VC-HeatedSteeringWheel-015"}]


def latest_files() -> list[Path]:
    groups: dict[str, list[tuple[int, Path]]] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            groups[m.group(1)].append((int(m.group(2) or 1), f))
    return [max(v)[1] for v in groups.values()]


def main() -> None:
    key: dict[tuple, list[tuple[str, str]]] = collections.defaultdict(list)
    n = 0
    for f in latest_files():
        for tc in json.loads(f.read_text(encoding="utf-8"))["tcs"]:
            n += 1
            key[(tc["pre_conditions"], tc["test_procedure"], tc["expected_result"])].append(
                (f.stem, tc["leaf_id"]))
    dups = [v for v in key.values() if len(v) > 1]
    print(f"TC 合計 {n}；三欄全同之組 {len(dups)}")
    found = []
    for grp in dups:
        leaves = {leaf for _, leaf in grp}
        found.append(leaves)
        print("  重複：", ", ".join(f"{b}/{l}" for b, l in grp))
    hit = [a for a in ANCHOR if a in found]
    print(f"\n錨點（必命中）{len(ANCHOR)} 組 —— 命中 {len(hit)} 組   "
          f"{'PASS，可失敗' if len(hit) == len(ANCHOR) else '⚠ 未命中，掃描已失效'}")
    new = [g for g in found if g not in ANCHOR]
    print(f"錨點以外之重複組：{len(new)}   {'PASS' if not new else '⚠ 本輪新增之不可分辨列'}")
    for g in new:
        print("   ", sorted(g))
    if len(hit) != len(ANCHOR) or new:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
