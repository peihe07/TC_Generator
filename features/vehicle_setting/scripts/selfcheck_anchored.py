"""R-VS54：§9 自檢之錨點執行器。

被檢輸入（本輪新版）與錨點（改寫前之舊版，已知應失敗）**同批執行**，
兩者結果並列回報。錨點若回報 0 項，即該檢查已失效 —— 以 exit code 2 停下。
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import json
import re

from selfcheck_w53 import check  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]

# (被檢輸入, 錨點) —— 錨點為同一 batch 之改寫前版本
def _pairs() -> list[tuple[str, str]]:
    """(被檢輸入, 錨點) —— 各 batch 之**最新版**對其**前一版**。

    46 輪起改為自動推導：本輪 W-130／W-131／W-132 三度產出 `_v{n+1}`，
    硬編之清單必然落後（其落後之症狀為「錨點檔不存在」或「錨點即被檢輸入」）。
    無前一版者（首版批次）改以同名之 `_batchNN_anchor.json`（刻意違規之樣本）。
    """
    import collections
    groups: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            groups[m.group(1)].append((int(m.group(2) or 1), f))
    out = []
    for k, v in sorted(groups.items()):
        v.sort()
        subj = v[-1][1]
        if len(v) >= 2:
            anchor = v[-2][1]
        else:
            a = FEAT / "generated" / f"_{k}_anchor.json"
            if not a.exists():
                continue
            anchor = a
        out.append((f"generated/{subj.name}", f"generated/{anchor.name}"))
    return out


PAIRS = _pairs()


def run(name: str) -> list[str]:
    d = json.loads((FEAT / name).read_text(encoding="utf-8"))
    return [x for tc in d["tcs"] for x in check(tc)]


def main() -> None:
    dead, subj_total, anch_total = [], 0, 0
    print(f"{'batch':10s} {'新版':>6s} {'錨點（舊版）':>12s}  判")
    for subj, anchor in PAIRS:
        se, ae = run(subj), run(anchor)
        subj_total += len(se)
        anch_total += len(ae)
        tcs = json.loads((FEAT / subj).read_text(encoding="utf-8"))["tcs"]
        if not tcs:
            verdict = "無 TC，錨點不適用"
        elif not ae:
            verdict = "⚠ 錨點回報通過 —— 檢查已失效"
            dead.append(subj)
        else:
            verdict = "可失敗"
        print(f"{Path(subj).stem:10s} {len(se):6d} {len(ae):12d}  {verdict}")
        for x in se:
            print("    新版:", x)
    print(f"\n合計：新版 {subj_total} 項；錨點 {anch_total} 項")
    if dead:
        print(f"\n⚠ 下列之錨點未命中，依 R-VS54(2) 停下：{dead}")
        raise SystemExit(2)


if __name__ == "__main__":
    main()
