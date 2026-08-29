#!/usr/bin/env python3
"""T49b —— R-SU41(b) 之遮蔽測試（人工複核之候選清單）。

**R-SU41(b)**：遮住 Final Step 以外之全部內容，
二 TC 之 Final Step 是否仍能看出驗的是不同的事？**答否即不合法。**

**本檔為人工清單之產生器，不是機器判準**（R-SU41(e)：本條無機器覆蓋）。
其只做一件事 —— **列出 Final Step 逐字相同、或僅差 `PENDING` 佔位者**，
供人裁。**「不同」不蘊含「足夠不同」**：字面有別而語意同者本檔抓不到，
故其輸出為**下界**。

比對對象為 **ER 之末行**（IN §5.5：Final Step 獨占驗證）。
`PENDING` 佔位以 `<PENDING>` 正規化後再比 —— 二 TC 若僅差佔位，
其判定對象實為同一句（下放包 36 §1.1 之情形）。

Usage: python3 scripts/mask_test.py
"""
import re
import sys
import warnings
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
warnings.filterwarnings("ignore")
from gen_pilot import TCS as P          # noqa: E402
from gen_batch01 import TCS as B        # noqa: E402
from gen_batch02a import TCS as C       # noqa: E402
from gen_batch03 import TCS as D        # noqa: E402
from gen_rov_a import TCS as E          # noqa: E402
from gen_rov_b import TCS as F          # noqa: E402
from gen_rov_cd import TCS as G         # noqa: E402

RE_PEND = re.compile(r"PENDING:[^;]*")
RE_NUM = re.compile(r"^\s*\d+\.\s*")


def norm(s: str) -> str:
    return RE_PEND.sub("<PENDING>", RE_NUM.sub("", s)).strip()


def main():
    tcs = list(P) + list(B) + list(C) + list(D) + list(E) + list(F) + list(G)
    named = [(f"newR1L-SU-{i:03d}", t) for i, t in enumerate(tcs, 1)]
    print("## T49b —— Final Step 遮蔽測試（R-SU41(b)）\n")
    print(f"回測集 **{len(named)} 個 TC**，"
          f"{len(named)*(len(named)-1)//2} 組配對。"
          "比對對象為 **ER 之末行**（IN §5.5）。\n")
    print("> **本表為人工複核之候選，不是判定**（R-SU41(e)：本條無機器覆蓋）。")
    print("> 其只抓**逐字相同或僅差佔位**者 —— "
          "**字面有別而語意相同者本表抓不到，故為下界。**\n")

    print("### 各 TC 之 Final Step（正規化後）\n")
    print("| TC | 037 列 | Final Step（`PENDING` 已正規化） |")
    print("|---|---|---|")
    fs = {}
    for lbl, t in named:
        f = norm(t["er"][-1])
        fs[lbl] = (f, t["req"])
        print(f"| `{lbl}` | `{t['req'][-3:]}` | {f[:96]}{'…' if len(f) > 96 else ''} |")

    exact, pend_only = [], []
    for (a, _), (b, _) in combinations(named, 2):
        fa, ra = fs[a]
        fb, rb = fs[b]
        if fa == fb:
            (pend_only if "<PENDING>" in fa else exact).append((a, b, ra, rb, fa))

    print(f"\n### ❌ Final Step 逐字相同（**{len(exact)}** 組）\n")
    if exact:
        print("| 配對 | 037 列 | Final Step |")
        print("|---|---|---|")
        for a, b, ra, rb, f in exact:
            print(f"| `{a}` vs `{b}` | `{ra[-3:]}`／`{rb[-3:]}` | {f[:80]}… |")
    else:
        print("**無。**")

    print(f"\n### ⚠ 僅差 `PENDING` 佔位者（**{len(pend_only)}** 組）\n")
    if pend_only:
        print("| 配對 | 037 列 | 正規化後之 Final Step |")
        print("|---|---|---|")
        for a, b, ra, rb, f in pend_only:
            print(f"| `{a}` vs `{b}` | `{ra[-3:]}`／`{rb[-3:]}` | {f[:80]}… |")
    else:
        print("**無。**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
