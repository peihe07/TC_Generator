"""VF230：選池之**對帳**（W-VF91.6；A-VF32 之對治）。

**A-VF32 之成因**：`facts.py` 與 `isolate.py` 之 `body = pool - pilots`
自選池扣除 20 條，**其前提為「pilot 之產出已在交付本內」而該前提從未成立**；
**扣除方（facts／isolate）與納入方（`data/vf230_batches.tsv`）分屬二處而無對帳**，
故該 20 條之缺席於任何檢查之視野中皆不存在 —— **其不呈現為「缺」，而是根本不出現。**

**本檔即該對帳。** 其判準為一條恆等式：

    選池（W0+W1） == 隔離 ∪ 去重 ∪ 清單所載 ∪ 具名之缺口

**任一 leaf 落於四者之外即 FAIL** —— 其為「既未寫入亦不在任何表」之第三類，
**A-VF32 所載之 20 條即其實例。**

**為何不改 `body = pool - pilots` 本身**（V70 §W-VF91.6 之第一選項）：
改讀清單則 `body` 將扣除清單所載之全部 435+ 條，
**facts 遂降至近 0，量產之重製鏈隨之斷裂**（`R-VS53` 同型）。
**故取其第二選項「另立對帳使其差可見」。**

**具名之缺口**：`data/vf230_pool_gap.tsv`（`leaf_id`／`why`／`ruling`）——
**其為白名單，而白名單須逐條有據**；空檔亦須存在，其空即「無缺口」之宣告。
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
MANIFEST = FEAT / "data/vf230_batches.tsv"
GAP = FEAT / "data/vf230_pool_gap.tsv"


def tsv(p: Path) -> list[dict]:
    return list(csv.DictReader(p.open(encoding="utf-8"), delimiter="\t"))


def main() -> int:
    wr = tsv(FEAT / "docs/reports/vf230_writability.tsv")
    pool = {r["leaf_id"] for r in wr if r["writable"] in ("W0", "W1")}
    iso = {r["leaf_id"] for r in tsv(FEAT / "data/vf230_isolated.tsv")}
    ded = {r["dropped"] for r in tsv(FEAT / "data/vf230_dedup_restorable.tsv")}

    listed, missing = set(), []
    for row in tsv(MANIFEST):
        q = FEAT / row["file"]
        if not q.exists():
            missing.append(row["batch"])
            continue
        listed |= {t["leaf_id"] for t in json.loads(q.read_text(encoding="utf-8"))["tcs"]}
    if missing:
        print(f"✋ 清單所載而檔案不存在：{missing} —— 對帳之視野不完整，停")
        return 2

    gap_named = {r["leaf_id"]: r for r in tsv(GAP)} if GAP.exists() else {}

    covered = iso | ded | listed | set(gap_named)
    orphan = sorted(pool - covered)
    outside = sorted(covered - pool - listed)   # 清單得含選池外之條（如 pilot3 之新形態）

    print("=== VF230 選池對帳（W-VF91.6／A-VF32） ===")
    print(f"  選池（W0+W1）      {len(pool)}")
    print(f"  隔離               {len(iso)}")
    print(f"  去重 dropped       {len(ded)}")
    print(f"  清單所載（去重複） {len(listed & pool)}   （清單總計 {len(listed)}）")
    print(f"  具名之缺口         {len(gap_named)}")
    print(f"  —— 四者聯集覆蓋選池 {len(pool & covered)} / {len(pool)}")
    if outside:
        print(f"  （選池外而見於隔離／去重／缺口表者 {len(outside)}：{outside[:5]}）")

    if orphan:
        print(f"\n**FAIL —— 既未寫入亦不在任何表者 {len(orphan)}**")
        for x in orphan:
            print(f"    {x}")
        print("\n其為 A-VF32 之形態。**補入之，或列入 "
              f"`{GAP.relative_to(FEAT)}` 並具其據。**")
        return 1

    print("\n**PASS —— 選池之每一條皆有去處。**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
