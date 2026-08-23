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
SAMPLES = FEAT / "tests/anchor_samples/selfcheck_anchor.json"


def subjects() -> list[str]:
    """被檢輸入 —— 各 batch 之最新版。"""
    import collections
    g: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            g[m.group(1)].append((int(m.group(2) or 1), f))
    return [f"generated/{max(v)[1].name}" for _, v in sorted(g.items())]


def run(name: str) -> list[str]:
    d = json.loads((FEAT / name).read_text(encoding="utf-8"))
    return [x for tc in d["tcs"] for x in check(tc)]


def main() -> None:
    """W-134（73 包 §2）：錨點改用**固定之刻意違規樣本**，不再以前一版為錨。

    以前一版為錨者，其語意在「本輪使其變差」時反轉 ——
    「檢查失效」與「輸入變差」在計數上不可分辨（46 輪 W-131 之實例，A-VS149）。
    固定樣本之預期恆為「必命中」。
    """
    samples = json.loads(SAMPLES.read_text(encoding="utf-8"))["tcs"]
    miss = [t["_expect"] for t in samples if not check(t)]
    print(f"錨點（固定樣本）{len(samples)} 項 —— 未命中 **{len(miss)}**   "
          f"{'PASS，可失敗' if not miss else '⚠ 檢查已失效'}")
    for m in miss:
        print("    未命中:", m)

    print(f"\n{'batch':16s} 違規")
    total = 0
    for name in subjects():
        d = json.loads((FEAT / name).read_text(encoding="utf-8"))
        errs = [x for tc in d["tcs"] for x in check(tc)]
        total += len(errs)
        print(f"{Path(name).stem:16s} {len(errs)}")
        for x in errs:
            print("    ", x)
    print(f"\n合計：被檢輸入 {total} 項；錨點必命中 {len(samples) - len(miss)}"
          f"／{len(samples)}")
    if miss:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
