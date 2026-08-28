#!/usr/bin/env python3
"""T32d —— 機制 3 判準由 `<` 改為 `≤`（R-SU23(b)）之落地與影響量測。

R-SU23(a)：凡以母體實測分位為門檻之偵測器，其判準一律取**包含界值之向**
（`score ≤ threshold` 為攔下）。理由：攔下之代價為多送一列人裁，
漏攔之代價為一個缺口未被發現，二者不對稱。

**本檔為機制 3 判準之唯一權威實作**（`caught()`）。
`detector_backtest.py`（T25a）與 `stratified_gt.py`（T26a）之 `<`
**保留不動** —— 其輸出已載於上繳包 11／12，改之則該二包不可重現。
二包所載之數自本包起以本檔之對照表更正。

Usage: python3 scripts/mech3.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus_v2 import corpus_v2, _rows_desc                     # noqa: E402
from anchor_table import C_ID, TfIdf                            # noqa: E402
from stratified_gt import GT_A1                                 # noqa: E402

PCT = 20                          # 機制 3 之門檻百分位（R-SU14 v4(c)）
GAP = {"292", "313", "319", "320"}


def caught(score, threshold):
    """機制 3 之攔下判準（R-SU23(a)）：**含界值**。"""
    return score <= threshold


def setup():
    objs = corpus_v2()[0]
    tf = TfIdf([o["text"] for o in objs])
    rows, d = _rows_desc()
    cand = {str(r[C_ID]).strip(): [(s, objs[j])
                                   for s, j in tf.query(d[str(r[C_ID]).strip()], top=20)]
            for r in rows}
    tops = sorted(v[0][0] for v in cand.values() if v)
    return cand, tops[int(len(tops) * PCT / 100)]


def t32d():
    cand, th = setup()
    idmap = {i.rsplit("-", 1)[1]: i for i in cand}
    lt = {i for i, v in cand.items() if v and v[0][0] < th}
    le = {i for i, v in cand.items() if v and caught(v[0][0], th)}
    added = sorted(le - lt)

    print("## T32d —— 機制 3 判準改 `≤`（R-SU23(b)）\n")
    print(f"門檻（語料 v2 首選分第 {PCT} 百分位）：**{th:.17g}**\n")
    print("| 判準 | 全母體攔下 | 差 |")
    print("|---|---:|---:|")
    print(f"| `< th`（原，上繳包 11 §2） | **{len(lt)}** | — |")
    print(f"| **`≤ th`（現行，R-SU23(b)）** | **{len(le)}** | **+{len(le)-len(lt)}** |")
    print("\n### 新增被攔之列（差集 `≤` − `<`）\n")
    print("| 037 列 | 首選分 | 與門檻之差 | 是否 GT-A1 | 是否缺口列 |")
    print("|---|---:|---:|:--:|:--:|")
    for i in added:
        k = i.rsplit("-", 1)[1]
        s = cand[i][0][0]
        print(f"| `{i}` | {s:.17g} | **{s-th:+.1e}** | "
              f"{'✅' if k in GT_A1 else '—'} | {'⚠ 是' if k in GAP else '否'} |")
    print(f"\n**新增 {len(added)} 列 —— 即 R-SU23 所述「界上恆有一列」之該列。**")
    print("其分數與門檻**相等**（差 0，非近似），因門檻取自母體之實測值。\n")

    print("### 對已載數字之更正對照（R-SU23(c) 之揭露）\n")
    print("| 出處 | 原載（`<`） | 改判準後（`≤`） |")
    print("|---|---:|---:|")
    print(f"| 上繳包 11 §2「第 20 百分位 全母體攔下」 | 62 列 | **{len(le)} 列** |")
    print(f"| 上繳包 12 §2「機制 3 全母體攔下」 | 62 列 | **{len(le)} 列** |")
    print("| 上繳包 17 §T31b「`176` 落入機制 3」 | 否 | **是** |")
    print("\n> `detector_backtest.py`（T25a）與 `stratified_gt.py`（T26a）之 `<` "
          "**保留不動**：其輸出已載於上繳包 11／12，改之則該二包不可重現。"
          "**本表即其更正**，二包之該格自本包起讀本表。\n")

    top5 = {k: {o["oid"] for _, o in cand[idmap[k]][:5]} for k in GT_A1}
    gap = [k for k, v in GT_A1.items() if not set(v) <= top5[k]]
    ok = [k for k in GT_A1 if k not in gap]
    print("### GT-A1 上之缺口召回與誤報\n")
    print("| 判準 | 缺口召回 | 誤報 |")
    print("|---|---:|---:|")
    for lbl, fn in (("`<`（原）", lambda s: s < th), ("**`≤`（現行）**", lambda s: caught(s, th))):
        h = [k for k in gap if fn(cand[idmap[k]][0][0])]
        f = [k for k in ok if fn(cand[idmap[k]][0][0])]
        print(f"| {lbl} | {len(h)}/{len(gap)} | {len(f)}/{len(ok)} |")
    print("\n**缺口召回不變**（新增之列非缺口列）；代價為誤報 +1 列。"
          "此與 R-SU23(a) 之不對稱理由一致：多送一列人裁 vs 漏一個缺口。")
    return len(le), added


if __name__ == "__main__":
    t32d()
