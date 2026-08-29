#!/usr/bin/env python3
"""T41a —— `I-cross` 之實作與回測（R-SU34(b)）。

**動機**：`lint036.py::check_sibling_parens()` 之分組鍵含 `req_id`，
故跨 `Requirement ID` 之偽通過**在結構上永不觸發**（R-SU34）。
本檔實作 R-SU34(b) 所定義之候選指標並對現有 TC 回測。

R-SU34(b) 之定義：
    「對同一 Test Set 內之任二 TC，計其 `test_procedure` 與
      `expected_result` 之**逐行相同行數比率**；比率逾門檻者列為待人裁。」

回測集（下放包 28 T41a）：現有 10 個 TC（pilot 5 + batch 1 之 5）。
已知之二錨點：
  - **TC-8 vs TC-1**：高相似但**合法**（觀測窗不同，R-SU33(c)）
  - **TC-9 vs TC-1**：**已知之不可區辨**（`179`，已掛 PENDING）
T41a 令門檻須使二者**分屬不同側**；
**若無門檻可使其分開，如實回報，不得挑一個剛好的數字。**

Usage: python3 scripts/i_cross.py
"""
import sys
import warnings
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
warnings.filterwarnings("ignore")
from gen_pilot import TCS as PILOT_TCS          # noqa: E402
from gen_batch01 import TCS as BATCH_TCS        # noqa: E402

# 全部同屬 Test Set `Silent Update`，故兩兩皆為 I-cross 之比對對象
LABELS = [f"TC-{i}" for i in range(1, 11)]


def line_ratio(a: dict, b: dict) -> tuple[float, int, int]:
    """R-SU34(b) 之指標：proc + er 之逐行相同行數 / 較長者之行數。"""
    same = total = 0
    for fld in ("proc", "er"):
        x, y = a[fld], b[fld]
        total += max(len(x), len(y))
        same += sum(1 for p, q in zip(x, y) if p == q)
    return same / total, same, total


def pending_lines(t: dict) -> int:
    return sum(s.count("PENDING:") for s in t["pre"] + t["proc"] + t["er"])


def main():
    tcs = list(PILOT_TCS) + list(BATCH_TCS)
    if len(tcs) != 10:
        sys.exit(f"T41a：回測集應為 10 個 TC，實得 {len(tcs)} —— 停並回報")
    named = list(zip(LABELS, tcs))

    print("## T41a —— `I-cross` 回測（R-SU34(b)）\n")
    print(f"回測集：**{len(tcs)} 個 TC**（pilot 5 + batch 1 之 5），"
          f"皆屬 Test Set `Silent Update`，故 {len(tcs)*(len(tcs)-1)//2} 組配對全數納入。\n")

    pairs = []
    for (na, a), (nb, b) in combinations(named, 2):
        r, s, tot = line_ratio(a, b)
        pairs.append((r, na, nb, a["req"][-3:], b["req"][-3:], s, tot))
    pairs.sort(reverse=True)

    ANCHOR = {("TC-8", "TC-1"): ("**合法**（窗不同，R-SU33(c)）", "低"),
              ("TC-9", "TC-1"): ("**已知不可區辨**（`179`，已掛 PENDING）", "高")}

    print("### 全 45 組配對，依比率降序（前 12 組 + 二錨點）\n")
    print("| # | 配對 | 037 列 | 相同/總行 | **比率** | 已知性質 |")
    print("|---:|---|---|---:|---:|---|")
    shown = 0
    for i, (r, na, nb, ra, rb, s, tot) in enumerate(pairs, 1):
        key = (na, nb) if (na, nb) in ANCHOR else (nb, na)
        note = ANCHOR.get(key, ("", ""))[0]
        if i <= 12 or note:
            print(f"| {i} | {na} vs {nb} | `{ra}`／`{rb}` | {s}/{tot} | "
                  f"**{r:.2f}** | {note} |")
            shown += 1
    print(f"\n（列出 {shown} 組；其餘 {len(pairs)-shown} 組比率皆 ≤ "
          f"{[p[0] for p in pairs][12] if len(pairs)>12 else 0:.2f}）\n")

    # ── 二錨點之判定 ──────────────────────────────────────────────
    def find(x, y):
        for r, na, nb, *_ in pairs:
            if {na, nb} == {x, y}:
                return r
        raise KeyError

    legal = find("TC-8", "TC-1")       # 合法，應在門檻**下**（不被攔）
    illeg = find("TC-9", "TC-1")       # 不可區辨，應在門檻**上**（被攔）

    print("### 二錨點之實測\n")
    print("| 錨點 | 應落之側 | **實測比率** |")
    print("|---|---|---:|")
    print(f"| TC-8 vs TC-1（合法） | 門檻**下**（不攔） | **{legal:.2f}** |")
    print(f"| TC-9 vs TC-1（不可區辨） | 門檻**上**（攔下） | **{illeg:.2f}** |")

    print(f"\n### 判定\n")
    if illeg > legal:
        print(f"存在門檻 `t`（{legal:.2f} < t ≤ {illeg:.2f}）可使二者分屬正確之側。")
        return 0

    print("> ### ❌ **無任何門檻可使二錨點分屬正確之側 —— 指標方向相反**\n")
    print(f"合法之配對得 **{legal:.2f}**，不可區辨之配對得 **{illeg:.2f}**；")
    print(f"**{legal:.2f} > {illeg:.2f}**，故任一門檻皆將**攔下合法者而放行不可區辨者**。")
    print("\n**成因（可由資料直接讀出）**：")
    for lbl, t in named:
        if lbl in ("TC-1", "TC-8", "TC-9"):
            print(f"- `{lbl}`（`{t['req']}`）：proc {len(t['proc'])} 行、er {len(t['er'])} 行、"
                  f"**PENDING {pending_lines(t)} 行**")
    print("""
`TC-9` 之比率為 0，**其全部差異來自那三行 `PENDING` 佔位**；
而佔位之所以存在，正是因為該問題**已由人裁攔下並掛起**。

即：**本指標量的是「這件事有沒有被修過」，不是「這是不是偽通過」。**
一個真正的偽通過 TC，其危險恰恰在於它**長得像正常 TC** —— 它不會有佔位行，
故其比率必然偏高；而已被抓到的那個，因為掛了佔位，比率反而掉到最低。

**依 T41a 之明令「不得挑一個剛好的數字」，本輪不提出門檻值。**""")
    return 3


if __name__ == "__main__":
    sys.exit(main())
