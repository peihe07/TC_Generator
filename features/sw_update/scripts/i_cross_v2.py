#!/usr/bin/env python3
"""T43c —— `I-cross` v2 之實作（R-SU34 v2(b)）。

**v1 為何作廢**：其指標（procedure／ER 之逐行相同比率）經回測與欲測性質
**負相關**（合法 0.60 vs 已知不可區辨 0.00）——`TC-9` 之低分全來自其
`PENDING` 佔位，而佔位存在正因該問題**已被人裁攔下**。詳 `i_cross.py`。

**v2 之指標**（布林條件，**無門檻**）：
    自各 TC 抽取 (i) **觀測窗之起訖點**、(ii) **所檢違例之類別**；
    **窗之起訖相同 且 違例類別有交集者** → `I-cross` 待人裁。

其不受 v1 之反轉所困，因二者皆與 `PENDING` 佔位無關。

---
**⚠ 本檔之判斷有一處不是從文字讀出來的，須明記（R-SU26(d) 之同一精神）**：

`NORMALISE` 表把「未指定之起點」與「until the update finishes」分別正規化為
**可用性查詢**與**版本號改變**。其依據為**下放包 30 §2.1 之裁定**
（靜默更新下唯一可觀測之起點為測試者主動觸發之查詢；
更新完成之唯一外部表徵為版本號改變），**不是 TC 文字本身**。

**故 TC-8 vs TC-1「窗相同」之判定，其效力來自該裁定。**
若日後改裁，本表須同步改，否則本檢查會沉默地沿用一個已失效之前提。
---

Usage: python3 scripts/i_cross_v2.py
"""
import re
import sys
import warnings
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
warnings.filterwarnings("ignore")
from gen_pilot import TCS as PILOT_TCS          # noqa: E402
from gen_batch01 import TCS as BATCH_TCS        # noqa: E402

LABELS = [f"TC-{i}" for i in range(1, 11)]

# ── 窗之起訖點抽取 ──────────────────────────────────────────────
START = [(r"from the availability check", "availability-check"),
         (r"from the start of the session", "session-start")]
END = [(r"until the software version changes", "version-change"),
       (r"until the update finishes", "update-finish")]

# 下放包 30 §2.1 之裁定 —— **非文字所載**，見檔首之警語
NORMALISE = {
    None: "availability-check",      # 未指定起點 → 唯一可觀測之起點
    "update-finish": "version-change",  # 更新完成之唯一外部表徵
}

# ── 違例類別 ──
#
# **粒度即指標本身**（首版之教訓，見 §驗收）：
#   類太粗 → `TC-6`（download confirmation）與 `TC-7`（deployment confirmation）
#            落入同一類而誤報；
#   類太細 → `TC-8` 之概括式 `no confirmation screen` 與二者皆不相交而漏報，
#            **而 TC-8 正是本檢查要抓的那一個**。
#
# 故取**最細之類**，並以**上下位關係**判交集（非集合相等）：
#   `confirmation-screen` ⊃ {`confirmation-screen/download`,
#                            `confirmation-screen/deployment`}
# 概括式與任一子類相交；二子類彼此不相交。
VIOLATION = [
    (r"download confirmation screen", "confirmation-screen/download"),
    (r"deployment confirmation screen", "confirmation-screen/deployment"),
    (r"\bconfirmation screen", "confirmation-screen"),          # 概括式（上位）
    (r"SW Update prompt", "prompt"),
    (r"progress notification", "progress-notification"),
    (r"opt-out control", "opt-out"),
    (r"defer control", "defer"),
]


def subsumes(a: str, b: str) -> bool:
    """a 與 b 是否有上下位或相等關係 —— `x` 涵蓋 `x/...`。"""
    return a == b or a.startswith(b + "/") or b.startswith(a + "/")


def overlap(ca: set, cb: set) -> set:
    """回傳構成交集之類對（以較細者表示），空集即不相交。"""
    return {min(x, y, key=len) if subsumes(x, y) else None
            for x in ca for y in cb if subsumes(x, y)} - {None}

NEG = re.compile(r"contains no |no SW Update prompt|no progress notification"
                 r"|no download confirmation|no deployment confirmation"
                 r"|no confirmation screen|no opt-out|no defer")


def window(t):
    txt = " ".join(t["proc"] + t["er"])
    s = next((v for p, v in START if re.search(p, txt)), None)
    e = next((v for p, v in END if re.search(p, txt)), None)
    return NORMALISE.get(s, s), NORMALISE.get(e, e)


def violations(t):
    """僅取**否定式**之 ER 行 —— R-SU33／R-SU36 之射程為否定式。

    同一行同時命中概括式與子類時**只留子類**（取最細）。
    """
    cls = set()
    for ln in t["er"]:
        if not NEG.search(ln):
            continue
        hit = {v for p, v in VIOLATION if re.search(p, ln)}
        # 去上位：若已有 `x/y`，則移除其上位 `x`
        cls |= {v for v in hit
                if not any(o != v and o.startswith(v + "/") for o in hit)}
    return cls


def main():
    tcs = list(PILOT_TCS) + list(BATCH_TCS)
    if len(tcs) != 10:
        sys.exit(f"T43c：回測集應為 10 個 TC，實得 {len(tcs)} —— 停並回報")
    named = list(zip(LABELS, tcs))

    print("## T43c —— `I-cross` v2 回測（R-SU34 v2(b)）\n")
    print("**指標為布林條件，無門檻**：窗之起訖相同 **且** 違例類有交集 → 待人裁。\n")
    print("### 各 TC 之抽取結果\n")
    print("| TC | 037 列 | 窗（起 → 訖） | 否定式違例類（最細） |")
    print("|---|---|---|---|")
    info = {}
    for lbl, t in named:
        w = window(t)
        c = violations(t)
        info[lbl] = (w, c, t["req"])
        print(f"| {lbl} | `{t['req'][-3:]}` | `{w[0] or '—'}` → `{w[1] or '—'}` | "
              + ("／".join(f"`{x}`" for x in sorted(c)) or "—（無否定式 ER）") + " |")

    hits = []
    for (a, _), (b, _) in combinations(named, 2):
        wa, ca, ra = info[a]
        wb, cb, rb = info[b]
        ov = overlap(ca, cb)
        if wa == wb and wa != (None, None) and ov:
            hits.append((a, b, ra, rb, ov))

    print(f"\n### `I-cross` 命中（{len(hits)} 組 / 45）\n")
    print("| 配對 | 037 列 | 共同窗 | **違例類交集（上下位判定）** |")
    print("|---|---|---|---|")
    for a, b, ra, rb, ov in hits:
        print(f"| {a} vs {b} | `{ra[-3:]}`／`{rb[-3:]}` | `{info[a][0][0]}` → `{info[a][0][1]}` | "
              + "／".join(f"`{x}`" for x in sorted(ov)) + " |")

    # ── 二錨點 ──
    def hit(x, y):
        return any({a, b} == {x, y} for a, b, *_ in hits)

    print("\n### 二錨點（下放包 30 T43c 之驗收條件）\n")
    print("| 錨點 | **應** | 實測 | |")
    print("|---|---|---|:--:|")
    e1, g1 = True, hit("TC-8", "TC-1")
    e2, g2 = False, hit("TC-6", "TC-7")
    print(f"| TC-8 vs TC-1（窗經 §2.1 判為同） | 命中 | {'**命中**' if g1 else '未命中'} | "
          f"{'✅' if g1 == e1 else '❌'} |")
    print(f"| TC-6 vs TC-7（違例類不同） | **不**命中 | {'命中' if g2 else '**未命中**'} | "
          f"{'✅' if g2 == e2 else '❌'} |")
    ok = (g1 == e1) and (g2 == e2)
    print(f"\n**驗收：{'✅ 二錨點皆符' if ok else '❌ 有錨點不符 —— 如實回報'}**")
    return 0 if ok else 4


if __name__ == "__main__":
    sys.exit(main())
