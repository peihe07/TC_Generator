#!/usr/bin/env python3
"""R-G33(c) 之雙向檢查（R-G33(d)(2)），乙案實作（R-DM54）。

`deferred` 陣列自 R-DM54 起**只增不減**：項之解除不刪除該物件，
改增 `lifted` / `lifted_at` / `lifted_by` 三鍵。兩向據此定義：

  MISSING —— **未解除項**之 token 不見於其 leaf 各 TC 之括號下半
  STALE   —— **已解除項**之 token 仍見於其 leaf 任一 TC 之括號下半
             （另含跨 leaf 誤置：他 leaf 之 token 出現於本 leaf）

原實作之 STALE 候選集自當前陣列建，被整個移出陣列之 token 從此
無人檢查 —— **它抓得到的，正好不是 R-G33(d) 要防的那一種**
（上繳 26 §5.2）。乙案把「解除」變成一次寫入，token 永遠在候選集內。

`token` 取自 `deferred` 項之 `token` 鍵（R-DM53）。**本檢查為純字串
比對，無對譯、無判斷成分。**

feature 自有腳本；接入共用 `lint036` 屬 Tier 2（BACKLOG B10）。
"""
import argparse
import json
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]


def lower_half(test_item: str) -> str:
    """test_item 之括號下半（R-S4 兩段式，以空行分隔）。"""
    parts = test_item.split("\n\n", 1)
    return parts[1] if len(parts) > 1 else ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("batch", nargs="?", default="generated/pilot-01.json")
    args = ap.parse_args()

    data = json.loads((FEAT / args.batch).read_text(encoding="utf-8"))
    tcs = data["tcs"]
    deferred = data.get("deferred", [])

    if deferred and not isinstance(deferred[0], dict):
        print("deferred 陣列尚未依 R-DM53 物件化，本檢查不適用", file=sys.stderr)
        return 2

    active, lifted = {}, {}
    for item in deferred:
        bucket = lifted if item.get("lifted") else active
        bucket.setdefault(item["leaf_id"], []).append(item["token"])
    all_tokens = {i["token"] for i in deferred}

    print("# R-G33(c) 雙向檢查（R-G33(d)(2)；乙案 R-DM54）")
    print(f"batch: {args.batch}")
    print(f"tcs: {len(tcs)}   deferred entries: {len(deferred)}"
          f"   （未解除 {sum(len(v) for v in active.values())}"
          f" / 已解除 {sum(len(v) for v in lifted.values())}）")
    print()

    missing, stale = [], []
    print("| TC | leaf | token | 項之狀態 | 方向 | 判定 |")
    print("|---|---|---|---|---|---|")
    for n, tc in enumerate(tcs, 1):
        leaf = tc["leaf_id"]
        low = lower_half(tc["test_item"]).lower()
        own = set(active.get(leaf, [])) | set(lifted.get(leaf, []))

        for tok in active.get(leaf, []):
            ok = tok.lower() in low
            if not ok:
                missing.append((n, leaf, tok, "未解除項之 token 不見於括號下半"))
            print(f"| #{n} | {leaf} | `{tok}` | 未解除 | MISSING | "
                  f"{'含' if ok else '**不含**'} |")

        for tok in lifted.get(leaf, []):
            bad = tok.lower() in low
            if bad:
                stale.append((n, leaf, tok, "項已解除而括號下半仍載其 token"))
            print(f"| #{n} | {leaf} | `{tok}` | **已解除** | STALE | "
                  f"{'**仍含**' if bad else '已移除'} |")

        for tok in sorted(all_tokens - own):
            if tok.lower() in low:
                stale.append((n, leaf, tok, "他 leaf 之 token 誤置於本 leaf"))
                print(f"| #{n} | {leaf} | `{tok}` | 他 leaf | STALE | "
                      f"**含（非本 leaf 之項）** |")

    print()
    print(f"MISSING = {len(missing)}   STALE = {len(stale)}")
    for n, leaf, tok, why in missing:
        print(f"  MISSING  TC#{n} {leaf} token {tok!r} —— {why}")
    for n, leaf, tok, why in stale:
        print(f"  STALE    TC#{n} {leaf} token {tok!r} —— {why}")
    return 1 if (missing or stale) else 0


if __name__ == "__main__":
    sys.exit(main())
