"""B1(a)(b) —— 第七批 `source_anchor` 補齊與 `source_clause` 重建（R-P328）。

49 包新增 8 個 leaf 時，其 `source_anchor` 僅登記了部分錨點，
而 R-P327 所指之素材層閘門 `G99` 未重跑 —— 缺漏因而未被發現。

本檔依 R-P328(a)(b)：
  (a) 以 `data/layer3_full.tsv` 為準，補齊該 8 leaf 之 `source_anchor` 全集
  (b) 依 §C 之抽取規格重建其 `source_clause`
      —— 即 `"\\n".join(錨點原文)`，錨點依**數值升序**（即文件順序）

**只動 `generated/batch_007_power_state_c.json` 之 `leaves`**；
`tcs` 一字未動 —— TC 內容之重新檢視為 B2，`test_item` 之改寫為 B0，
二者皆不在本檔範圍（R-P334「不得先寫舊格式再改」故本檔不碰 `test_item`）。

用法：
    python features/power/scripts/repair_anchor_51.py --dry-run
    python features/power/scripts/repair_anchor_51.py --apply
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
POWER = ROOT / "features/power"
BATCH7 = POWER / "generated/batch_007_power_state_c.json"
LAYER3 = POWER / "data/layer3_full.tsv"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_tcs import anchor_bodies  # noqa: E402


def layer3_anchors() -> dict[str, set[str]]:
    """leaf -> 其被引用錨點之聯集（跨章節）。與 verify_anchor_set.py 同義。"""
    out: dict[str, set[str]] = {}
    rows = LAYER3.read_text(encoding="utf-8").splitlines()
    header = rows[0].split("\t")
    i_leaf, i_ids = header.index("leaf"), header.index("item_ids")
    for row in rows[1:]:
        if not row.strip():
            continue
        cells = row.split("\t")
        ids = {x.strip() for x in cells[i_ids].split(",") if x.strip()}
        out.setdefault(cells[i_leaf], set()).update(ids)
    return out


def main() -> int:
    apply = "--apply" in sys.argv
    expected = layer3_anchors()
    bodies = anchor_bodies()
    data = json.loads(BATCH7.read_text(encoding="utf-8"))

    added_all: set[str] = set()
    for leaf in data["leaves"]:
        parent = leaf["parent"]
        got = [a.strip() for a in str(leaf["source_anchor"]).split(",") if a.strip()]
        want = expected.get(parent, set())
        missing = want - set(got)
        if not missing:
            print(f"{parent}  已完整（{len(got)} 個），不動")
            continue
        added_all |= missing
        # 數值升序 —— 錨點 id 之升序即 CFTS 本文之出現順序
        full = sorted(want, key=int)
        clause = "\n".join("\n".join(bodies.get(a, [])) for a in full)
        print(f"{parent}  {len(got)} → {len(full)}  補 {len(missing)} 個: "
              f"{sorted(missing, key=int)}")
        print(f"           source_clause {len(leaf['source_clause'])} → {len(clause)} 字元")
        if apply:
            leaf["source_anchor"] = ",".join(full)
            leaf["source_clause"] = clause

    print(f"\n本次補入之相異錨點：{len(added_all)} 個 → {sorted(added_all, key=int)}")
    if apply:
        BATCH7.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8")
        print(f"已寫入 {BATCH7.relative_to(ROOT)}")
    else:
        print("（--dry-run，未寫入）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
