"""R-VS54：§9 自檢之錨點執行器。

被檢輸入（本輪新版）與錨點（改寫前之舊版，已知應失敗）**同批執行**，
兩者結果並列回報。錨點若回報 0 項，即該檢查已失效 —— 以 exit code 2 停下。
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import json

from selfcheck_w53 import check  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]

# (被檢輸入, 錨點) —— 錨點為同一 batch 之改寫前版本
PAIRS = [
    ("generated/batch01_v6.json", "generated/batch01_v5.json"),
    ("generated/batch02_v4.json", "generated/batch02_v3.json"),
    ("generated/batch03_v5.json", "generated/batch03_v4.json"),
    ("generated/batch04_v6.json", "generated/batch04_v5.json"),
    ("generated/batch05_v4.json", "generated/batch05_v3.json"),
    ("generated/batch06_v4.json", "generated/batch06_v3.json"),
    ("generated/batch07_v4.json", "generated/batch07_v3.json"),
    ("generated/batch08_v5.json", "generated/batch08_v4.json"),
    ("generated/batch10_v4.json", "generated/batch10_v3.json"),
    ("generated/batch11_v4.json", "generated/batch11_v3.json"),
    ("generated/batch12_v4.json", "generated/batch12_v3.json"),
    # batch13 為首版，無「改寫前之舊版」可用 —— 依 R-VS54(1) 改以
    # 刻意違規之樣本為錨點（四處植入，見該檔之 `revision`）。
    ("generated/batch13_v2.json", "generated/_batch13_anchor.json"),
    ("generated/batch14.json", "generated/_batch14_anchor.json"),
]


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
