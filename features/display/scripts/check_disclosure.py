#!/usr/bin/env python3
"""R-G33(c) 之雙向檢查（R-G33(d)(2)）。

方向一 MISSING：`deferred` 陣列有某 leaf 之項，而該 leaf 之 TC
              括號下半未含其 `token` 逐字 → R-G33(b) 之違反。
方向二 STALE  ：括號下半含某 `token`，而 `deferred` 陣列已無該 leaf
              之該項 → R-G33(d) 之違反（deferred 已解除而揭露句未移除）。

`token` 取自 `deferred` 項之 `token` 鍵（R-DM53）。**本檢查為純字串
比對，無對譯、無判斷成分** —— 這正是 R-DM53 把 token 自檢查端移到
宣告端所要買的東西。

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

    path = FEAT / args.batch
    data = json.loads(path.read_text(encoding="utf-8"))
    tcs = data["tcs"]
    deferred = data.get("deferred", [])

    if deferred and not isinstance(deferred[0], dict):
        print("deferred 陣列尚未依 R-DM53 物件化，本檢查不適用", file=sys.stderr)
        return 2

    print(f"# R-G33(c) 雙向檢查（R-G33(d)(2)）")
    print(f"batch: {args.batch}")
    print(f"tcs: {len(tcs)}   deferred entries: {len(deferred)}")
    print()

    tokens = {}                      # leaf -> [token, ...]
    for item in deferred:
        tokens.setdefault(item["leaf_id"], []).append(item["token"])
    all_tokens = {t for v in tokens.values() for t in v}

    missing, stale = [], []
    print("| TC | leaf | token | 方向 | 判定 |")
    print("|---|---|---|---|---|")
    for n, tc in enumerate(tcs, 1):
        leaf = tc["leaf_id"]
        low = lower_half(tc["test_item"]).lower()
        for tok in tokens.get(leaf, []):
            ok = tok.lower() in low
            if not ok:
                missing.append((n, leaf, tok))
            print(f"| #{n} | {leaf} | `{tok}` | MISSING | "
                  f"{'含' if ok else '**不含**'} |")
        for tok in sorted(all_tokens - set(tokens.get(leaf, []))):
            if tok.lower() in low:
                stale.append((n, leaf, tok))
                print(f"| #{n} | {leaf} | `{tok}` | STALE | **含（陣列無）** |")

    print()
    print(f"MISSING = {len(missing)}   STALE = {len(stale)}")
    for n, leaf, tok in missing:
        print(f"  MISSING  TC#{n} {leaf} 缺 token {tok!r}")
    for n, leaf, tok in stale:
        print(f"  STALE    TC#{n} {leaf} 有 token {tok!r} 而 deferred 陣列無此項")
    return 1 if (missing or stale) else 0


if __name__ == "__main__":
    sys.exit(main())
