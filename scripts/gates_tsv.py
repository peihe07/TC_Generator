#!/usr/bin/env python3
"""閘登錄簿 `docs/runtime/GATES.tsv`（R-G17）。

R-G17 令每支 lint 閘登錄 id、判準一句話、來源裁決、生效日、近 10 輪命中數，
並以「連續 10 輪命中 0」為除役候選之判準。本工具自 `scripts/lint036.py`
之閘登錄（`CHECK_TITLES`／`CHECK_STATUS`／`CHECK_GRANULARITY`／
`CHECK_ORDER`／`PROFILE_CHECKS`）生成該簿，命中數自
`docs/fw036/lint_reports/*.json` 回填。

**未知不得以 0 代替**（G-D：一個永遠空的清單與一個壞掉的清單，輸出相同）。
故命中數有三種值，其語意不同：

| 值 | 意義 |
|---|---|
| `<n>` | 該輪實測命中 n 次（n 得為 0，其為**量過而為 0**）|
| `未知` | 該輪之報告未涵蓋此閘（profile 專屬閘於未指定 profile 之報告中）|
| `未知，自本輪起算` | 全部可讀報告皆未涵蓋此閘 —— **其 0 尚不存在** |

**除役候選之判準**：`hit_rounds` ≥ 10 且 `hits_total` == 0。
`未知` 之輪次**不計入** `hit_rounds` —— 未量過不能充當「命中 0」。

`retired` 欄為除役狀態；除役 = 該欄改 `Y` 並於 `lint_defs` 停用，**不刪列**。
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
from pathlib import Path

OUT_DEFAULT = "docs/runtime/GATES.tsv"
REPORT_DIR = "docs/fw036/lint_reports"
RECENT_N = 10
COLUMNS = ["gate_id", "criterion", "source_ruling", "effective_date",
           "granularity", "status", "scope", "hit_rounds", "hits_total",
           "hits_recent", "retire_candidate", "retired"]
# 來源裁決：`CHECK_STATUS` 之括號內載其判準來源（`R-6b`／`A-PM16`／`M15` …）
# 尾端用負向前瞻而非 `\b`：`R-10(a)` 之末字元為 `)`，其後接全形逗號時
# `\b` 不成立，正則遂回溯為 `R-10` —— 子條標記被靜默吃掉（本工具首跑實測）。
RE_RULING = re.compile(
    r"(?<![\w-])(?:R-\d+[a-z]?(?:\([0-9a-z]+\))?|A-[A-Z]{2}\d+|M\d+|S\d+)(?![\w-])"
)


def load_lint036(root: Path):
    spec = importlib.util.spec_from_file_location("l36", root / "scripts" / "lint036.py")
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    sys.modules["l36"] = mod
    spec.loader.exec_module(mod)
    return mod


def recent_reports(root: Path, limit: int) -> list[Path]:
    """近 N 份 lint 報告（依檔名排序，新者在後；取末 N 份）。"""
    files = sorted((root / REPORT_DIR).glob("*.json"))
    return files[-limit:]


def rows(mod, reports: list[Path]) -> list[dict]:
    """閘登錄各列。

    **「近 10 輪」之截斷在此落實**，不倚賴呼叫方先切好 —— 否則該不變量
    只存在於一條呼叫路徑上，而 `hits_recent` 之欄名已宣告它是近 10 輪。
    """
    counts = []
    for p in reports[-RECENT_N:]:
        try:
            counts.append((p.stem, json.loads(p.read_text(encoding="utf-8")).get("counts", {})))
        except (OSError, json.JSONDecodeError):
            continue

    order = list(mod.CHECK_ORDER)
    profile_only = [k for k in mod.PROFILE_CHECKS if k not in order]
    out = []
    for key in order + profile_only:
        status = mod.CHECK_STATUS.get(key, "")
        rulings = sorted(set(RE_RULING.findall(status)))
        seq, hit_rounds, total = [], 0, 0
        for _, c in counts:
            if key in c:
                seq.append(str(c[key]))
                hit_rounds += 1
                total += c[key]
            else:
                seq.append("未知")
        if hit_rounds == 0:
            recent = "未知，自本輪起算"
        else:
            recent = ",".join(seq)
        out.append({
            "gate_id": key,
            "criterion": mod.CHECK_TITLES.get(key, ""),
            "source_ruling": "／".join(rulings) if rulings else "未載明",
            "effective_date": "未載明",
            "granularity": mod.CHECK_GRANULARITY.get(key, ""),
            "status": status,
            "scope": "profile-only" if key in profile_only else "always",
            "hit_rounds": str(hit_rounds),
            "hits_total": str(total) if hit_rounds else "未知",
            "hits_recent": recent,
            "retire_candidate": "Y" if (hit_rounds >= RECENT_N and total == 0) else "N",
            "retired": "N",
        })
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="閘登錄簿（R-G17）")
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default=OUT_DEFAULT)
    ap.add_argument("--check", action="store_true", help="只比對既有檔，不寫入")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    mod = load_lint036(root)
    reports = recent_reports(root, RECENT_N)
    data = rows(mod, reports)

    body = "\n".join(["\t".join(COLUMNS)]
                     + ["\t".join(r[c] for c in COLUMNS) for r in data]) + "\n"
    out_path = root / args.out
    if args.check:
        if not out_path.exists() or out_path.read_text(encoding="utf-8") != body:
            print(f"FAIL: {args.out} 與現行閘登錄不符", file=sys.stderr)
            return 1
        print(f"OK: {args.out} 相符（{len(data)} 閘）")
        return 0

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(body, encoding="utf-8")
    n_unknown = sum(1 for r in data if r["hits_total"] == "未知")
    n_cand = sum(1 for r in data if r["retire_candidate"] == "Y")
    print(f"寫入 {args.out}：{len(data)} 閘，回填來源 {len(reports)} 份報告")
    print(f"  命中數未知者 {n_unknown} 閘（未以 0 代替 —— G-D）")
    print(f"  除役候選（{RECENT_N} 輪皆量過且全 0）{n_cand} 閘")
    return 0


if __name__ == "__main__":
    sys.exit(main())
