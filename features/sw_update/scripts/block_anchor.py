#!/usr/bin/env python3
"""T24 —— 召回重估、列舉區塊普查、缺陷語形掃描（下放包 11 §五）。

Usage: python3 scripts/block_anchor.py 24a 24b 24c 24d
"""

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus_v2 import corpus_v2, TRUTH, _rows_desc          # noqa: E402
from anchor_table import C_ID, C_TITLE, TfIdf, A03           # noqa: E402

# 下放包 11 §三 —— 分析層第二批裁定（11 列）。`292` 與 `217` 未裁，不入。
TRUTH2 = {
    "317": ["4907669"], "318": ["4907670"], "319": ["4907671"],
    "320": ["4907672"], "321": ["4907673"], "322": ["4907676"],
    "323": ["4907677"], "324": ["4907679"], "215": ["4907281"],
    "216": ["4907279"],
}
ALL_TRUTH = {**TRUTH, **TRUTH2}          # 累計 27 列（313 等已在 TRUTH）


def _setup(top=20):
    objs = corpus_v2()[0]
    tf = TfIdf([o["text"] for o in objs])
    rows, d = _rows_desc()
    cand = {}
    for r in rows:
        i = str(r[C_ID]).strip()
        cand[i] = [(s, objs[j]) for s, j in tf.query(d[i], top=top)]
    return objs, tf, rows, d, cand


def t24b():
    objs, tf, rows, d, cand = _setup(20)
    idmap = {i.rsplit("-", 1)[1]: i for i in cand}
    print("## T24b —— 召回之重估（前 20 候選）\n")
    print(f"累計地面真值 **{len(ALL_TRUTH)} 列**"
          f"（下放包 09 之 17 + 下放包 11 之 10；`292`／`217` 未裁不計）。\n")
    print("| N | 召回（≥1 正解在前 N） | 涵蓋（全部正解在前 N） |")
    print("|---:|---|---|")
    for N in (5, 10, 15, 20):
        rec = cov = 0
        for k, v in ALL_TRUTH.items():
            got = {o["oid"] for _, o in cand[idmap[k]][:N]}
            if set(v) & got:
                rec += 1
            if set(v) <= got:
                cov += 1
        print(f"| {N} | **{rec}/{len(ALL_TRUTH)}（{rec/len(ALL_TRUTH)*100:.0f}%）** "
              f"| {cov}/{len(ALL_TRUTH)}（{cov/len(ALL_TRUTH)*100:.0f}%） |")

    print("\n### 正解之排名分布（逐列）\n")
    print("| 037 列 | 正解數 | 各正解之排名（`—` = 不在前 20） |")
    print("|---|---:|---|")
    never = []
    for k in sorted(ALL_TRUTH, key=lambda x: int(x)):
        v = ALL_TRUTH[k]
        order = [o["oid"] for _, o in cand[idmap[k]]]
        rk = [(str(order.index(x) + 1) if x in order else "—") for x in v]
        if all(r == "—" for r in rk):
            never.append(k)
        print(f"| `SWE1-FOTA-{k}` | {len(v)} | {', '.join(rk)} |")
    print(f"\n**前 20 內完全無正解者**：{[f'`{x}`' for x in never] or '無'}")

    print("\n### `SWE1-FOTA-292` 之前 20 候選全表\n")
    i = idmap["292"]
    print(f"Description：\n\n> {d[i]}\n")
    tgt = "4907460"
    print("| # | ObjectID | 章 | 分 | 首句 |")
    print("|---:|---|---|---:|---|")
    rank = None
    for n, (s, o) in enumerate(cand[i], 1):
        mk = " ⬅ **§3.3 所指之 `4907460`**" if o["oid"] == tgt else ""
        if o["oid"] == tgt:
            rank = n
        print(f"| {n} | `{o['oid']}` | {o['chap']} | {s:.3f} | {o['text'][:90]}…{mk} |")
    if rank:
        print(f"\n**`4907460` 排名第 {rank}**（分 {cand[i][rank-1][0]:.3f}）。")
    else:
        q = tf.query(d[i], top=len(objs))
        pos = next((n for n, (s, j) in enumerate(q, 1) if objs[j]["oid"] == tgt), None)
        sc = next((s for s, j in q if objs[j]["oid"] == tgt), 0.0)
        print(f"\n**`4907460` 不在前 20** —— 全母體排名第 **{pos if pos else '無分數'}"
              f"/{len(objs)}**，分 **{sc:.3f}**（首選 {cand[i][0][0]:.3f}）。")
    return cand


# ── T24c —— 列舉區塊普查 ─────────────────────────────────────────────
ENUM = re.compile(r"^\s*(\d{1,2})[.)]\s+(\S)")


def rows_inscope():
    from corpus_v2 import _rows_desc as _rd
    return _rd()[0]


def t24c(cand=None):
    objs = corpus_v2()[0]
    print("\n## T24c —— CFTS 列舉區塊之全母體普查\n")
    print("辨識法：需求物件之**自身文字**以 `n.` 或 `n)` 起首者為列舉項；"
          "同母章內序號連續遞增（+1）且文件序相鄰者聚為一塊。\n")
    seq = []
    for k, o in enumerate(objs):
        m = ENUM.match(o["own"])
        seq.append((k, o, int(m.group(1)) if m else None))
    blocks, cur = [], []
    for k, o, n in seq:
        if n is None:
            if len(cur) >= 2:
                blocks.append(cur)
            cur = []
            continue
        if cur and cur[-1][2] + 1 == n and cur[-1][1]["chap"] == o["chap"]:
            cur.append((k, o, n))
        else:
            if len(cur) >= 2:
                blocks.append(cur)
            cur = [(k, o, n)]
    if len(cur) >= 2:
        blocks.append(cur)
    print(f"**辨識出 {len(blocks)} 個列舉區塊**，涵蓋 "
          f"{sum(len(b) for b in blocks)} 個需求物件。\n")
    print("| # | 母章 | 起訖 ObjectID | 項數 | 各項首句 |")
    print("|---:|---|---|---:|---|")
    for n, blk in enumerate(blocks, 1):
        firsts = " ／ ".join(f"{x[2]}. {x[1]['own'][len(str(x[2]))+2:][:34]}" for x in blk[:6])
        print(f"| {n} | {blk[0][1]['chap']} | `{blk[0][1]['oid']}`–`{blk[-1][1]['oid']}` "
              f"| {len(blk)} | {firsts[:150]} |")

    # 037 側之連續列對位候選 —— **滑動視窗**對位。
    # 初版以「每項之最小 037 列號」判連續，是錯的：一個物件會出現在許多列之
    # 前 20 內，全域 min 取到的不是對位的那一列，致已知之 4.12 區塊亦漏。
    cand = cand or _setup(20)[4]
    order037 = [str(r[C_ID]).strip() for r in rows_inscope()]
    top1 = {i: (cand[i][0][1]["oid"] if cand[i] else None) for i in order037}
    inN = {i: {o["oid"] for _, o in cand[i]} for i in order037}
    print("\n### 對位候選（R-SU16(c)2／(c)3）\n")
    print("以**滑動視窗**對位：對每個區塊（項數 L），逐一嘗試 037 之每個連續 L 列"
          "起點，計其第 t 項物件落在第 t 列之前 20 候選內之數（`in20`）"
          "與其為該列**首選**之數（`top1`）。取 `in20` 最大者為該塊之對位候選。\n")
    print("| 區塊 | 母章 | 起訖 ObjectID | L | 最佳對位之 037 列 | in20 | top1 | 滿足 (d) |")
    print("|---:|---|---|---:|---|---:|---:|:--:|")
    hits = 0
    for n, blk in enumerate(blocks, 1):
        oids = [o["oid"] for _, o, _ in blk]
        L = len(oids)
        best = (0, 0, None)
        for s in range(len(order037) - L + 1):
            win = order037[s:s + L]
            a = sum(1 for t_, i in zip(oids, win) if t_ in inN[i])
            b = sum(1 for t_, i in zip(oids, win) if t_ == top1[i])
            if (a, b) > (best[0], best[1]):
                best = (a, b, win)
        a, b, win = best
        if a < 2:
            print(f"| {n} | {blk[0][1]['chap']} | `{oids[0]}`–`{oids[-1]}` | {L} "
                  f"| — | {a} | {b} | ❌ |")
            continue
        hits += 1
        ok = "✅" if b >= 2 else "❌"
        print(f"| {n} | {blk[0][1]['chap']} | `{oids[0]}`–`{oids[-1]}` | {L} "
              f"| `{win[0]}`–`{win[-1]}` | {a} | **{b}** | {ok} |")
    print(f"\n**連續對位候選 {hits} 組。** 執行層產出候選，**不裁定對位成立**（R-SU16）。")
    return blocks


# ── T24a / T24d ──────────────────────────────────────────────────────
def t24a():
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    allr = [r for r in openpyxl.load_workbook(A03, read_only=True, data_only=True)
            ["AnalysisReport_FULL"].iter_rows(min_row=8, values_only=True)
            if r[C_ID] not in (None, "")]
    ids = [str(r[C_ID]).strip() for r in allr]
    k = ids.index("SWE1-FOTA-128")
    print("\n## T24a —— `SWE1-FOTA-128` 及其後 8 列之判定材料\n")
    print("> **執行層不裁定** `below mentioned parameters` 所指為何。\n")
    for r in allr[k:k + 9]:
        i = str(r[C_ID]).strip()
        desc = re.sub(r"\s+", " ", str(r[3] or "")).strip()
        print(f"\n### `{i}` — {str(r[C_TITLE] or '').strip()}"
              f"｜Categorization：{r[5] or '(blank)'}\n")
        print(f"> {desc or '(空)'}\n")


DEFECT_FORMS = [
    ("殘句 of/in + 無名詞", r"\b(?:of|in|for|to)\s+(?:condition|state|type|mode|value|parameter|component)\b(?!\s*\w)"),
    ("冠詞後直接接介詞", r"\b(?:the|a|an)\s+(?:of|in|for|to|with|by|from)\b"),
    ("重複冠詞", r"\b(the|a|an)\s+\1\b"),
    ("動詞後直缺受詞", r"\bshall\s+(?:handle|report|provide|send|receive|use)\s+(?:the\s+)?(?:of|in|for|to)\b"),
    ("空括號／佔位", r"[<\[]\s*(?:TBD|XXX|X{2,}|\?+)\s*[>\]]|\(\s*\)"),
    ("句中孤立冠詞結尾", r"\b(?:the|a|an)\s*[.,;]"),
]


def t24d():
    rows, d = _rows_desc()
    print("\n## T24d —— 037 描述缺陷之語形掃描（311 列）\n")
    print("> **執行層只列形態，不裁定何者為缺陷**（下放包 11 §五 T24d）。\n")
    print("| 形態 | regex |")
    print("|---|---|")
    for n, p in DEFECT_FORMS:
        print(f"| {n} | `{p}` |")
    print("\n| 形態 | 037 列 | 原句摘錄 |")
    print("|---|---|---|")
    tot = 0
    for n, p in DEFECT_FORMS:
        for i in sorted(d):
            for m in re.finditer(p, d[i], re.I):
                s, e = max(0, m.start() - 80), min(len(d[i]), m.end() + 80)
                tot += 1
                print(f"| {n} | `{i}` | …{d[i][s:e]}… |")
    print(f"\n**命中合計 {tot} 處。**")


if __name__ == "__main__":
    want = set(sys.argv[1:]) or {"24b"}
    cand = t24b() if "24b" in want else None
    if "24c" in want:
        t24c(cand)
    if "24a" in want:
        t24a()
    if "24d" in want:
        t24d()
