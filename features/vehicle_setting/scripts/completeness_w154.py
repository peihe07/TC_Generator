"""W-154（82 包 §1，R-VS76）—— 完整性檢查。

**以母體為輸入**，非以產物為輸入：237 leaf 逐一歸入三類，其和須為 237。
  有 TC ／ held_out（附條文逐字與理由）／`generatable = no`
任一 leaf 未歸類即為漏，停下回報。
"""
from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from writeback_036 import latest_batches  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]


def classify() -> dict:
    gen = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}
    with_tc: dict[str, int] = {}
    for f in latest_batches():
        for tc in json.loads(f.read_text(encoding="utf-8"))["tcs"]:
            with_tc[tc["leaf_id"]] = with_tc.get(tc["leaf_id"], 0) + 1

    # held_out 亦只取**現行版**之批（與產物同一選取式），
    # 否則舊版之 held_out 會把已生成或已入 W2 池者拉回本類。
    held: dict[str, dict] = {}
    for f in latest_batches():
        d = json.loads(f.read_text(encoding="utf-8"))
        for h in (d.get("held_out") or []):
            held[h["leaf_id"]] = {**h, "batch": f.name}

    buckets = {"has_tc": [], "held_out": [], "not_generatable": [], "unclassified": []}
    for leaf in gen:
        # 歸類之優先序（82 包 §2 之三類定義）：
        #   有 TC > `generatable = no`（W2 池）> held_out
        # `generatable = no` 置於 held_out 之前 —— 其為分級所定之池，
        # 而 held_out 為生成時之個別判定；二者重疊時以前者為準。
        if leaf in with_tc:
            buckets["has_tc"].append(leaf)
        elif gen[leaf]["generatable"] == "no":
            buckets["not_generatable"].append(leaf)
        elif leaf in held:
            buckets["held_out"].append(leaf)
        else:
            buckets["unclassified"].append(leaf)

    # held_out 之理由須逐條具備（R-VS76：「附條文逐字與不生成之理由」）
    # R-VS76 令 held_out「附條文逐字與不生成之理由」——
    # 逐字之判準為 reason 內含反引號括起之來源節錄。
    thin = [l for l in buckets["held_out"]
            if not (held[l].get("reason") or "").strip()
            or "`" not in (held[l].get("reason") or "")]
    return {"gen": gen, "with_tc": with_tc, "held": held,
            "buckets": buckets, "thin": thin}


def main() -> int:
    r = classify()
    b, gen = r["buckets"], r["gen"]
    n = {k: len(v) for k, v in b.items()}
    total = n["has_tc"] + n["held_out"] + n["not_generatable"]
    print("R-VS76 完整性檢查 —— 以母體為輸入")
    print(f"  母體（generatable.tsv）        {len(gen)}")
    print(f"  有 TC                          {n['has_tc']} leaf ／ "
          f"{sum(r['with_tc'].values())} TC")
    print(f"  held_out                       {n['held_out']}")
    print(f"  generatable = no               {n['not_generatable']}")
    print(f"  ── 三類之和                    {total}")
    print(f"  未歸類                          {n['unclassified']}")
    for l in b["unclassified"]:
        print(f"      ⚠ {l}  generatable={gen[l]['generatable']}  "
              f"writable={gen[l].get('writable', '')}")
    if r["thin"]:
        print(f"  held_out 理由不全              {len(r['thin'])}")
        for l in r["thin"]:
            print(f"      ⚠ {l}")
    ok = total == len(gen) and not b["unclassified"] and not r["thin"]
    print("  判定：", "PASS" if ok else "**FAIL —— 停下回報**")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
