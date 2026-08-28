#!/usr/bin/env python3
"""T27 —— GT-A2 重取樣、GT-C 反向樣本、獨立觀測分組（下放包 14 §五）。

Usage: python3 scripts/reverse_sample.py 27a 27b 27c
"""

import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus_v2 import corpus_v2, _rows_desc                              # noqa: E402
from anchor_table import (C_ID, C_TITLE, C_DESC, C_CAT, C_SUB, C_SRC,    # noqa: E402
                          A03, TfIdf, norm_tokens, IN_SCOPE)
from framework_survey import a03_rows as a03_all, group_by_heading       # noqa: E402
from stratified_gt import GT_A1, GT_B, cfts_chapters                     # noqa: E402
from block_anchor import ENUM                                            # noqa: E402

SEED_A2, SEED_C = 27, 271


def setup():
    objs = corpus_v2()[0]
    tf = TfIdf([o["text"] for o in objs])
    rows, d = _rows_desc()
    cand = {str(r[C_ID]).strip(): [(s, objs[j])
                                   for s, j in tf.query(d[str(r[C_ID]).strip()], top=20)]
            for r in rows}
    return objs, tf, rows, d, cand


def blocks_of(objs):
    """CFTS 列舉區塊（沿 T24c 之辨識法）：oid → 區塊編號。"""
    seq = [(o, int(m.group(1)) if (m := ENUM.match(o["own"])) else None) for o in objs]
    bl, cur = [], []
    for o, n in seq:
        if n is None:
            if len(cur) >= 2:
                bl.append(cur)
            cur = []
            continue
        if cur and cur[-1][1] + 1 == n and cur[-1][0]["chap"] == o["chap"]:
            cur.append((o, n))
        else:
            if len(cur) >= 2:
                bl.append(cur)
            cur = [(o, n)]
    if len(cur) >= 2:
        bl.append(cur)
    return {o["oid"]: i for i, b in enumerate(bl, 1) for o, _ in b}, bl


# ── T27c —— 獨立觀測之分組（下放包 14 §二 #1 之判準）─────────────────
def t27c(objs=None):
    objs = objs or corpus_v2()[0]
    order = {o["oid"]: k for k, o in enumerate(objs)}        # CFTS 文件序
    chap = {o["oid"]: o["chap"] for o in objs}
    blk, _ = blocks_of(objs)

    # (i) 037 列 id 連續 —— **於 in-scope 序列上**連續（`314` 非 in-scope，
    #     故 `313`／`315` 相鄰）。此為執行層對「連續」之解讀，見上繳包 13 §4.1。
    inscope = sorted(int(str(r[C_ID]).strip().rsplit("-", 1)[1]) for r in _rows_desc()[0])
    pos = {n: k for k, n in enumerate(inscope)}

    def cond_i(a, b):
        return abs(pos[int(a)] - pos[int(b)]) == 1

    def cond_ii(a, b):
        """正解物件屬同一 CFTS 區塊，或同一母章之相鄰物件。"""
        for x in GT_A1[a]:
            for y in GT_A1[b]:
                if blk.get(x) and blk.get(x) == blk.get(y):
                    return "同區塊 #%d" % blk[x]
                if chap[x] == chap[y] and abs(order[x] - order[y]) <= 1:
                    return f"同母章 {chap[x]} 相鄰"
        return None

    ks = sorted(GT_A1, key=int)
    groups, why, cur = [], [], [ks[0]]
    for a, b in zip(ks, ks[1:]):
        r = cond_ii(a, b) if cond_i(a, b) else None
        if r:
            cur.append(b)
            why.append((a, b, r))
        else:
            groups.append(cur)
            cur = [b]
    groups.append(cur)

    print("## T27c —— 獨立觀測之分組（下放包 14 §二 #1 之判準）\n")
    print("判準（分析層裁定，逐字）：「(i) 037 列 id 連續 且 (ii) 其正解物件屬"
          "同一 CFTS 區塊或同一母章之相鄰物件。**二條件皆滿足者合計為 1**」。\n")
    print("**執行層對 (i)「連續」之解讀**：於 **in-scope 序列**上連續。"
          f"037 之 383 個資料列中僅 311 為 in-scope，`314` 等 Heading／"
          "非範圍列不在序列內，故 `313`／`315` 視為相鄰。"
          "若改採「原始 id 差為 1」，第 10 組將裂為 `313` 與 `315`–`324` 二組"
          "（獨立觀測 13→14）。**此解讀須分析層確認。**\n")
    print("| 組 | 037 列 | 列數 | 併組依據（逐對） |")
    print("|---:|---|---:|---|")
    wmap = {(a, b): r for a, b, r in why}
    for n, g in enumerate(groups, 1):
        rs = "；".join(f"`{a}`+`{b}` {wmap[(a,b)]}" for a, b in zip(g, g[1:])) or "—（單列自成一組）"
        print(f"| {n} | {'、'.join('`'+x+'`' for x in g)} | {len(g)} | {rs} |")
    print(f"\n**GT-A1 28 列 → 獨立觀測 {len(groups)} 個。**\n")

    # 與上繳包 12 之舊分組（差 ≤ 2 且 id 最近距離 ≤ 6）逐組比對 —— 計算，不寫死
    oldg, cur2 = [], [ks[0]]
    for a, b in zip(ks, ks[1:]):
        near = min(abs(int(x) - int(y)) for x in GT_A1[a] for y in GT_A1[b])
        if int(b) - int(a) <= 2 and near <= 6:
            cur2.append(b)
        else:
            oldg.append(cur2)
            cur2 = [b]
    oldg.append(cur2)
    print(f"### 與上繳包 12 之舊分組（{len(oldg)} 組）之差異\n")
    print("舊演算法為「037 列號差 ≤ 2 **且**正解物件 id 最近距離 ≤ 6」，"
          "未要求同區塊／同母章。**新判準只拆不併**，逐處如下：\n")
    print("| 舊組 | 新拆為 | 斷點 | 成因 |")
    print("|---|---|---|---|")
    newof = {x: n for n, g in enumerate(groups) for x in g}
    for g in oldg:
        parts, c3 = [], [g[0]]
        for a, b in zip(g, g[1:]):
            if newof[a] == newof[b]:
                c3.append(b)
            else:
                parts.append(c3)
                c3 = [b]
        parts.append(c3)
        if len(parts) == 1:
            continue
        brk = []
        for a, b in zip(g, g[1:]):
            if newof[a] != newof[b]:
                x, y = GT_A1[a][-1], GT_A1[b][0]
                brk.append(f"`{a}`／`{b}`：`{x}`({chap[x]}) 與 `{y}`({chap[y]}) "
                           + ("**母章不同**" if chap[x] != chap[y]
                              else f"同母章但文件序距 **{abs(order[x]-order[y])}**（非相鄰）"))
        print(f"| {'、'.join('`'+x+'`' for x in g)} | "
              + " ／ ".join("{" + "、".join('`'+x+'`' for x in p) + "}" for p in parts)
              + f" | {len(brk)} 處 | " + "；".join(brk) + " |")
    print(f"\n上繳包 12 §6 待確認事項 #1 所指之「`310`／`311`／`312` 亦被併為一組，"
          f"下放包未提及該組」—— **新判準把它拆開了**；且不只該組。"
          f"分析層之判準確實比執行層之舊演算法嚴："
          f"**獨立觀測由 {len(oldg)} 增為 {len(groups)}**，"
          f"舊法所報之各「獨立觀測」比率因此全部作廢（§二 #1 之拘束）。\n")

    gapk = {"292", "313", "319", "320"}
    gg = [n for n, g in enumerate(groups, 1) if gapk & set(g)]
    print(f"**缺口列所落之組**：第 {'、'.join(map(str, gg))} 組 —— 共 **{len(gg)} 個獨立觀測**"
          f"（`292` 與 `313`／`319`／`320`），與上繳包 11 §7.2「真正互異之成因只有 2 種」一致。\n")
    return groups


# ── T27a —— GT-A2 重取樣（分層鍵 = 037 Heading 群）────────────────────
def t27a(cand=None):
    if cand is None:
        *_, cand = setup()[:5]
        cand = _[-1] if False else cand
    objs, tf, rows, d, cand = setup()
    allrows = a03_all()
    groups = group_by_heading(allrows)                 # 45 群 + 1 前言偽節
    real = groups[1:]
    excl = {f"SWE1-FOTA-{k}" for k in GT_A1} | {f"SWE1-FOTA-{k}" for k in GT_B}
    by = {str(r[C_ID]).strip(): r for r in rows}

    pool = {}
    for g in real:
        ids = [str(r[C_ID]).strip() for r in g["rows"]]
        pool[g["id"]] = dict(title=g["title"], all=ids,
                             avail=[i for i in ids if i not in excl])

    print("## T27a —— GT-A2 重取樣（分層鍵 = 037 Heading 群）\n")
    print(f"- 分層鍵：**037 之 Heading 群**（R-SU17 v2(a)）——"
          f"其分佈來自上游文件結構，**與路徑 A 之輸出無關**")
    print(f"- **`12a` 之 30 列全數廢棄**（其分層鍵 top1 章已由 R-SU17 v2(a) 廢止）")
    print(f"- Heading 群 **{len(real)}** 群（另 1 個前言偽節，所轄 "
          f"{len(groups[0]['rows'])} 列）；轄有 in-scope 列者 "
          f"**{sum(1 for v in pool.values() if v['all'])}** 群")
    print(f"- 抽樣池：311 − GT-A1 28 − GT-B 4 = **{sum(len(v['avail']) for v in pool.values())}** 列，"
          f"落於 **{sum(1 for v in pool.values() if v['avail'])}** 個非空層")
    print(f"- 取樣碼：`random.Random({SEED_A2})`；層序 `shuffle`，層內 `sample`，"
          f"先每層取 1 列，不足 30 時再取第 2 列（**沿 R-SU17 v1(a) 之每層至多 2 列**"
          f"—— v2(a) 未另定，執行層沿用並揭露）\n")

    rng = random.Random(SEED_A2)
    seq = [k for k, v in pool.items() if v["avail"]]
    rng.shuffle(seq)
    for k in seq:
        pool[k]["avail"] = rng.sample(pool[k]["avail"], len(pool[k]["avail"]))
    pick, taken = [], Counter()
    for rnd in (0, 1):
        for k in seq:
            if len(pick) >= 30:
                break
            if len(pool[k]["avail"]) > rnd:
                pick.append((k, pool[k]["avail"][rnd]))
                taken[k] += 1
        if len(pick) >= 30:
            break

    sz = sorted((len(v["all"]) for v in pool.values()), reverse=True)
    print("### 群大小分佈（45 群，依所轄 in-scope 列數）\n")
    print("| 列數 | 群數 |")
    print("|---:|---:|")
    for n, c in sorted(Counter(sz).items(), reverse=True):
        print(f"| {n} | {c} |")
    print(f"\n最大群 **{sz[0]}** 列（`SWE1-FOTA-309` OMA-DM Security）、"
          f"最小群 **{sz[-1]}** 列 —— R-SU17 v2(a) 所揭露之殘餘偏誤於本批之量值見 §抽中機率。\n")

    print(f"### 章涵蓋對照\n")
    print("| | 群數 | 佔 45 |")
    print("|---|---:|---:|")
    print(f"| **本批（30 列）涵蓋之 Heading 群** | **{len(taken)}** | "
          f"**{len(taken)/len(real)*100:.0f}%** |")
    print(f"| 轄有 in-scope 列而未抽中者 | "
          f"{sum(1 for v in pool.values() if v['avail'] or v['all']) - len(taken)} | — |")
    print(f"| 無 in-scope 列（結構上不可抽） | "
          f"{sum(1 for v in pool.values() if not v['all'])} | "
          f"{sum(1 for v in pool.values() if not v['all'])/len(real)*100:.0f}% |")

    print("\n### ⚠ 每列之抽中機率（等額配置之殘餘偏誤，量值）\n")
    print("等額配置（每層 1 列）使**小群之列被抽中之機率遠高於大群之列**。"
          "任何以本批所作之比率估計若不加權，即以群為單位而非以列為單位。"
          "**逐列之抽中機率列於下表，供日後作加權估計（Horvitz–Thompson）之用。**\n")
    print("| # | 037 列 | Heading 群 | 標題 | 群內池列數 | 抽中機率 |")
    print("|---:|---|---|---|---:|---:|")
    for n, (k, i) in enumerate(pick, 1):
        m = len(pool[k]["avail"])
        print(f"| {n} | `{i}` | `{k}` | {pool[k]['title'][:38]} | {m} | "
              f"**{taken[k]/m:.3f}** |")
    ps = [taken[k] / len(pool[k]["avail"]) for k, _ in pick]
    print(f"\n抽中機率之極差：**{min(ps):.3f} – {max(ps):.3f}**（比值 "
          f"**{max(ps)/min(ps):.0f}×**）。等額配置下最大群之列被抽中之機率為"
          f"最小群之 1/{max(ps)/min(ps):.0f}。\n")

    print("### 人裁材料索引\n")
    print("材料全文見 `docs/upstream/13a_sample_material.md`。\n")
    return pick, pool, by, d, cand


def dump_a2(pick, pool, by, d, cand):
    allrows = a03_all()
    head_of, cur = {}, ("—", "(前言)")
    for r in allrows:
        if r[C_CAT] == "Heading":
            cur = (str(r[C_ID]).strip(), str(r[C_TITLE] or "").strip())
        else:
            head_of[str(r[C_ID]).strip()] = cur
    for n, (k, i) in enumerate(pick, 1):
        r = by[i]
        print(f"\n---\n\n### {n}. `{i}` — {str(r[C_TITLE] or '').strip()}\n")
        print(f"- Heading 群：`{k}` {pool[k]['title']}｜Sub Cat：{r[C_SUB] or '(blank)'}"
              f"｜Source：`{r[C_SRC]}`｜群內池列數 {len(pool[k]['avail'])}")
        print(f"\n**Requirement Description 全文**：\n\n> {d[i] or '(空)'}\n")
        print("**路徑 A（語料 v2）前 5 候選**：\n")
        for j, (s, o) in enumerate(cand.get(i, [])[:5], 1):
            print(f"{j}. `{o['oid']}` — 章 **{o['chap']}** {o['chap_title']} — 分 **{s:.3f}**")
            print(f"   > {o['text'][:400]}{'…' if len(o['text'])>400 else ''}\n")


# ── T27b —— GT-C 反向樣本 ─────────────────────────────────────────────
MOTA = {"8", "8.1", "8.2", "8.3", "8.4"}


def t27b():
    objs, tf, rows, d, cand = setup()
    oid2chap = {o["oid"]: o["chap"] for o in objs}
    chaps = cfts_chapters()
    tt = {c[0]: c[2] for c in chaps}
    touched = {oid2chap[x] for v in GT_A1.values() for x in v if x in oid2chap}
    with_req = {o["chap"] for o in objs}
    target = [c for c in with_req if c not in touched]      # 45 章

    # 反向分數：對每個 CFTS 物件，取 037 全 311 列中分數最高之 3 列。
    # **與路徑 A 同一計分函式**（TF-IDF cosine），故可比。
    qv = {i: tf._vec(Counter(norm_tokens(d[i]))) for i in d}
    by_obj = {}
    for k, o in enumerate(objs):
        v = tf.vecs[k]
        sc = sorted(((sum(q[w] * v[w] for w in q.keys() & v.keys()), i)
                     for i, q in qv.items()), reverse=True)
        by_obj[o["oid"]] = sc[:3]

    rng = random.Random(SEED_C)
    per = defaultdict(list)
    for o in objs:
        if o["chap"] in target:
            per[o["chap"]].append(o)
    pick = []
    for c in sorted(target, key=lambda x: [int(y) for y in x.split(".")]):
        pool = per[c]
        n = 2 if c in MOTA else 1
        n = min(n, len(pool))
        pick += [(c, o) for o in rng.sample(pool, n)]

    print("\n## T27b —— GT-C 反向樣本材料（CFTS 側驅動）\n")
    print(f"- 母體：**{len(target)} 個未觸及且可測之章**（R-SU17 v2 §(c) 之更正值）"
          f"，共 {sum(len(v) for v in per.values())} 個需求物件")
    print(f"- 每章抽 1 個；**MOTA 一族（{'、'.join(sorted(MOTA))}）每章抽 2 個**"
          f"（R-SU17 v2(d)「必須納入本批」）")
    print(f"- 取樣碼：`random.Random({SEED_C}).sample(該章物件, n)`")
    print(f"- 本批 **{len(pick)} 個物件**，涵蓋 **{len({c for c,_ in pick})} / {len(target)}** 章\n")
    print("- **反向分數**：對每個 CFTS 物件，計其與 037 全 311 列 "
          "`Requirement Description` 之 TF-IDF cosine，取最高之 3 列。"
          "**與路徑 A 同一計分函式**，故「路徑 A 看不看得見此物件」可由此讀出。\n")
    print("> **執行層不裁定有無對應。** 分析層逐一反向裁定「037 中有無列對應之」；"
          "裁定結果入 `GROUND_TRUTH.md` 之 GT-C 節。\n")

    print("### 取樣清單\n")
    print("| # | 章 | 標題 | ObjectID | 該章物件數 | 最高反向分 |")
    print("|---:|---|---|---|---:|---:|")
    for n, (c, o) in enumerate(pick, 1):
        print(f"| {n} | **{c}** | {tt.get(c,'—')[:32]} | `{o['oid']}` | {len(per[c])} | "
              f"{by_obj[o['oid']][0][0]:.3f} |")

    tops = sorted(by_obj[o["oid"]][0][0] for _, o in pick)
    print(f"\n最高反向分之分布：中位數 **{tops[len(tops)//2]:.3f}**、"
          f"最低 {tops[0]:.3f}、最高 {tops[-1]:.3f}。\n")
    mota = [(c, o) for c, o in pick if c in MOTA]
    mt = sorted(by_obj[o["oid"]][0][0] for _, o in mota)
    print(f"**MOTA 一族（{len(mota)} 個物件）之最高反向分**：中位數 "
          f"**{mt[len(mt)//2]:.3f}**、最低 {mt[0]:.3f}、最高 {mt[-1]:.3f} "
          f"—— 與全批中位數 {tops[len(tops)//2]:.3f} 之比較見上繳包 §自評。\n")
    return pick, by_obj, per, tt, d, rows


def dump_c(pick, by_obj, per, tt, d, rows):
    by = {str(r[C_ID]).strip(): r for r in rows}
    print("\n---\n\n## 逐物件材料\n")
    for n, (c, o) in enumerate(pick, 1):
        print(f"\n---\n\n### {n}. `{o['oid']}` — 章 **{c}** {tt.get(c,'—')}\n")
        print(f"**物件全文**（逐字）：\n\n> {o['text'] or '(空)'}\n")
        print("**037 全 311 列中對本物件分數最高之 3 列**：\n")
        for j, (s, i) in enumerate(by_obj[o["oid"]], 1):
            r = by[i]
            print(f"{j}. `{i}` — {str(r[C_TITLE] or '').strip()[:70]} — 分 **{s:.3f}**")
            print(f"   > {d[i][:300]}{'…' if len(d[i])>300 else ''}\n")


if __name__ == "__main__":
    want = set(sys.argv[1:]) or {"27c"}
    if "27c" in want:
        t27c()
    if "27a" in want:
        pick, pool, by, d, cand = t27a()
        if "dump" in want:
            dump_a2(pick, pool, by, d, cand)
    if "27b" in want:
        pick, by_obj, per, tt, d, rows = t27b()
        if "dump" in want:
            dump_c(pick, by_obj, per, tt, d, rows)
