#!/usr/bin/env python3
"""R-G72(h) 殘項清單 —— Revise-M 出貨條件之佐證（GC-13 審閱 一 之 2）。

出貨條件：`P_after` 之每一命中皆可歸入 {bare-$（待 Revise-C）,
已登錄之 Revise-C 殘項} 二類之一，**且無誤報**。
本工具把 P 之每一命中逐一分類並落表；**不可分類者記 `unclassified`**
—— 該值出現即不得出貨（不得以「其餘」含混帶過）。
"""
from __future__ import annotations

import argparse
import csv
import json
from collections import Counter
from pathlib import Path


def classify(detail: str) -> tuple[str, str]:
    if "v3 記法殘留" in detail:
        return "bare-$", "Revise-C：逐 TC 回查 CFTS 原句取 raw (label)，查無登 DR"
    if "缺 `Send CAN:` 前綴" in detail:
        return "ReviseC", "Revise-C：CFTS 回查"
    if "賦值未寫成" in detail:
        return "ReviseC", "Revise-C：CFTS 回查"
    if "PROXI" in detail:
        return "ReviseC", "Revise-C：PROXI 形態人裁"
    return "unclassified", "**未分類 —— 不得出貨**"


def main() -> int:
    ap = argparse.ArgumentParser(description="R-G72(h) 殘項清單")
    ap.add_argument("--report", required=True, help="lint036 之 json 報告")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    d = json.load(open(a.report, encoding="utf-8"))
    rows = []
    tally = Counter()
    for s in d.get("sheets", []):
        for v in s.get("violations", []):
            if v["check"] != "P":
                continue
            klass, dest = classify(v["detail"])
            tally[klass] += 1
            rows.append([s.get("sheet", ""), v["row"], v["field"],
                         v.get("snippet", "")[:160], klass, dest, v["detail"][:90]])
    out = Path(a.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["sheet", "row", "col", "text", "class", "去向", "lint_detail"])
        w.writerows(rows)
    print(f"  {out}  共 {len(rows)} 項：" +
          "／".join(f"{k} {n}" for k, n in sorted(tally.items())))
    if tally["unclassified"]:
        print(f"  ⚠ unclassified {tally['unclassified']} 項 —— 不得出貨")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
