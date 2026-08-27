#!/usr/bin/env python3
"""T25 —— 低分偵測器回測、無編號平行式普查、#7 分數矩陣（下放包 12 §五）。

Usage: python3 scripts/detector_backtest.py 25a 25b 25c
"""

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus_v2 import corpus_v2, TRUTH, _rows_desc     # noqa: E402
from anchor_table import C_ID, TfIdf                    # noqa: E402
from block_anchor import TRUTH2                         # noqa: E402

# GT-A 28 列 = 下放包 09 之 17 + 11 之 10 + 12 §4.2 之 `292`
GT_A = {**TRUTH, **TRUTH2, "292": ["4907460", "4907403"]}


def _cand(top=20):
    objs = corpus_v2()[0]
    tf = TfIdf([o["text"] for o in objs])
    rows, d = _rows_desc()
    return objs, tf, rows, d, {str(r[C_ID]).strip():
                               [(s, objs[j]) for s, j in tf.query(d[str(r[C_ID]).strip()], top=top)]
                               for r in rows}


def t25a():
    objs, tf, rows, d, cand = _cand(20)
    idmap = {i.rsplit("-", 1)[1]: i for i in cand}
    tops = sorted(v[0][0] for v in cand.values() if v)
    n = len(tops)
    pct = {p: tops[int(n * p / 100)] for p in (10, 15, 20, 25)}

    print("## T25a —— 低分偵測器之回測（GT-A 28 列）\n")
    print(f"母體首選分數之百分位（語料 v2，n={n}）：")
    print("| 百分位 | 門檻 | 全母體攔下之列數 |")
    print("|---:|---:|---:|")
    for p, th in pct.items():
        print(f"| 第 {p} | **{th:.3f}** | {sum(1 for v in cand.values() if v and v[0][0] < th)} |")

    # 缺口列 = 其正解未被 N=5 完整涵蓋者（R-SU14 v3 之常態 N）
    gap, ok = [], []
    for k, v in GT_A.items():
        i = idmap[k]
        top5 = {o["oid"] for _, o in cand[i][:5]}
        (gap if not set(v) <= top5 else ok).append((k, i, cand[i][0][0], set(v) - top5))
    print(f"\n### 缺口之定義：其正解未被 **N=5** 完整涵蓋者\n")
    print(f"GT-A 28 列中，**缺口 {len(gap)} 列**、無缺口 {len(ok)} 列。\n")
    print("| 037 列 | 首選分 | N=5 未涵蓋之正解 |")
    print("|---|---:|---|")
    for k, i, s, miss in sorted(gap, key=lambda x: x[2]):
        print(f"| `SWE1-FOTA-{k}` | **{s:.3f}** | {', '.join('`'+m+'`' for m in sorted(miss))} |")

    print("\n### 各門檻之回測\n")
    print("| 門檻（百分位） | 值 | 攔下之缺口 | 缺口召回 | 誤報（攔下但無缺口） | 誤報率 |")
    print("|---|---:|---:|---:|---:|---:|")
    for p, th in pct.items():
        hit = [k for k, i, s, _ in gap if s < th]
        fp = [k for k, i, s, _ in ok if s < th]
        print(f"| 第 {p} 百分位 | {th:.3f} | {len(hit)}/{len(gap)} | "
              f"**{len(hit)/len(gap)*100:.0f}%** | {len(fp)}/{len(ok)} | "
              f"{len(fp)/len(ok)*100:.0f}% |")

    i = idmap["292"]
    s = cand[i][0][0]
    caught = [p for p, th in pct.items() if s < th]
    missed = [p for p, th in pct.items() if s >= th]
    print("\n### ⚠ `292` —— 缺口成因與分數無關\n")
    print(f"- 首選分 **{s:.3f}**；其主錨 `4907460` 排名第 **7**"
          f" —— **N=5 截斷，非召回失敗**")
    print(f"- 第 {'／'.join(str(x) for x in missed)} 百分位**攔不下**它；"
          f"第 {'／'.join(str(x) for x in caught)} 百分位**攔得下**")
    print(f"- ⚠ 但這是**巧合，不是機制**：其分 {s:.3f} 與第 15 百分位"
          f" {pct[15]:.3f} 僅差 **{s-pct[15]:+.3f}** —— 門檻挪動一點點即翻面。")
    print(f"- **其缺口成因為「正解排第 6–20 名」，與首選分數高低無因果關係**。"
          f"低分偵測器攔到它是因為它**恰好**也偏低，不是因為偵測器看得見這種缺口。")
    return gap, ok, pct, cand, idmap


# ── T25b —— 無編號平行式之普查 ────────────────────────────────────────
ENUM = re.compile(r"^\s*(\d{1,2})[.)]\s+")


def skeleton(t, k=4):
    """句首骨架 = 去編號後之前 k 個詞（小寫）。"""
    s = ENUM.sub("", t.strip())
    return tuple(w.lower() for w in re.findall(r"[A-Za-z']+", s)[:k])


def t25b():
    objs = corpus_v2()[0]
    print("\n## T25b —— (a2) 無編號平行式之普查\n")
    print("偵測法：同母章內**文件序相鄰**之需求物件，其自身文字之"
          "**句首骨架**（去編號後前 4 個詞）相同者聚為一組；組長 ≥2。\n")

    # ── 種子回測（§1.3 之教訓；未過即停）
    print("### 種子回測（R-SU13 v2 同型要求；未過即停）\n")
    seed = [o for o in objs if "4907667" <= o["oid"] <= "4907672"]
    sk = [skeleton(o["own"]) for o in seed]
    print("| 種子物件 | 去編號後前 4 詞 |")
    print("|---|---|")
    for o, s in zip(seed, sk):
        print(f"| `{o['oid']}` | `{' '.join(s) if s else '(空)'}` |")
    uniq = len(set(sk))
    print(f"\n骨架相異數：**{uniq} / {len(sk)}**")
    if uniq == len(sk):
        print("\n**⚠ 種子回測未過** —— 區塊 #8（已知之列舉區塊）之六項，"
              "其句首骨架**兩兩皆不同**，本偵測器抓不到它。\n")
        print("> 成因：#8 各項為 `Socket read/write error`／`Network loss:…`／"
              "`The end-user deactivates…` —— **各項是不同的名詞短語，不是平行動詞骨架**。"
              "即「編號式」與「無編號平行式」之結構特徵**不同源**："
              "前者靠編號，後者靠骨架，而 #8 只有前者。\n")
        print("> 依下放包 12 §五 T25b「抓不到即停並回報」，"
              "**(a2) 之全母體普查不執行**。")
        return None
    print("\n**種子回測通過**，續跑全母體普查。\n")
    return _a2_survey(objs)


def _a2_survey(objs):
    groups, cur = [], []
    for o in objs:
        s = skeleton(o["own"])
        if cur and cur[-1][1] == s and cur[-1][0]["chap"] == o["chap"] and s:
            cur.append((o, s))
        else:
            if len(cur) >= 2:
                groups.append(cur)
            cur = [(o, s)]
    if len(cur) >= 2:
        groups.append(cur)
    print(f"**辨識出 {len(groups)} 組無編號平行式**，涵蓋 {sum(len(g) for g in groups)} 個物件。\n")
    print("| # | 母章 | 起訖 | 項數 | 骨架 |")
    print("|---:|---|---|---:|---|")
    for n, g in enumerate(groups, 1):
        print(f"| {n} | {g[0][0]['chap']} | `{g[0][0]['oid']}`–`{g[-1][0]['oid']}` "
              f"| {len(g)} | `{' '.join(g[0][1])}` |")
    return groups


# ── T25c —— #7 之 8×6 分數矩陣 ────────────────────────────────────────
def t25c(cand=None, idmap=None):
    objs, tf, rows, d, cand2 = _cand(20)
    cand = cand or cand2
    idmap = idmap or {i.rsplit("-", 1)[1]: i for i in cand}
    blk = [o for o in objs if "4907602" <= o["oid"] <= "4907607"]
    win = [f"{n:03d}" for n in range(133, 141)]
    print("\n## T25c —— 區塊 #7（4.10.5）之 8×6 分數矩陣\n")
    print("窗 `SWE1-FOTA-133`–`140` 跨 8 列而 L=6。逐列對該塊各項之 TF-IDF 分數：\n")
    print("| 037 列 | " + " | ".join(f"`{o['oid']}`<br>{n+1}." for n, o in enumerate(blk))
          + " | 該列首選 |")
    print("|---|" + "---:|" * len(blk) + "---|")
    for k in win:
        i = idmap.get(k)
        if not i:
            print(f"| `SWE1-FOTA-{k}` | " + " | ".join("—" for _ in blk) + " | （非 in-scope 列）|")
            continue
        q = tf._vec(Counter(re.findall(r"[a-z0-9]+", d[i].lower())))
        cells = []
        for o in blk:
            v = tf.vecs[objs.index(o)]
            s = sum(q[w] * v[w] for w in q.keys() & v.keys())
            cells.append(s)
        mx = max(cells)
        top = cand[i][0][1]
        print(f"| `SWE1-FOTA-{k}` | "
              + " | ".join((f"**{c:.3f}**" if c == mx and c > 0 else f"{c:.3f}") for c in cells)
              + f" | `{top['oid']}` ({top['chap']}) {cand[i][0][0]:.3f} |")
    print("\n> **執行層不裁定何者對位**（下放包 12 §五 T25c）。粗體為該列在本塊內之最高分。")


if __name__ == "__main__":
    want = set(sys.argv[1:]) or {"25a"}
    gap = ok = pct = cand = idmap = None
    if "25a" in want:
        gap, ok, pct, cand, idmap = t25a()
    if "25b" in want:
        t25b()
    if "25c" in want:
        t25c(cand, idmap)
