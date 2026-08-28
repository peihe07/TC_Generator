#!/usr/bin/env python3
"""T26 —— 機制 4 回測、GT-A2 分層隨機取樣、GT-A1 章涵蓋實測（下放包 13 §五）。

Usage: python3 scripts/stratified_gt.py 26a 26b 26c
"""

import random
import re
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus_v2 import corpus_v2, TRUTH, _rows_desc                       # noqa: E402
from anchor_table import CFTS, C_ID, C_TITLE, C_SUB, C_SRC, TfIdf, A03   # noqa: E402
from block_anchor import TRUTH2                                          # noqa: E402

# GT-A1 28 列 = 下放包 09 之 17 + 11 之 10 + 12 §4.2 之 `292`（定向取樣，R-SU17(a)）
GT_A1 = {**TRUTH, **TRUTH2, "292": ["4907460", "4907403"]}

# GT-B 4 列（R-SU16 v2(h)）—— 不入 GT-A2 之抽樣池，其對位已用到路徑 A 之 top1
GT_B = {"030", "031", "328", "329"}

HEAD, TOC = {"1", "2", "3", "4", "5"}, {"10", "20", "30", "40", "50"}


def cfts_chapters():
    """87 個 CFTS 章節物件：章號 → (ObjectID, 標題)，依文件序。"""
    raw = zipfile.ZipFile(CFTS).read("word/document.xml").decode("utf8", "replace")
    out = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", raw, re.S):
        m = re.search(r'<w:pStyle w:val="([^"]+)"', p)
        st = m.group(1) if m else ""
        if st in TOC or st not in HEAD:
            continue
        t = re.sub(r"<[^>]+>", "", p)
        m = re.search(r"^\s*([\d.]+)\s+(.*?)\s*\{(\d{7})\}", t)
        if m:
            out.append((m.group(1), m.group(3), m.group(2)))
    return out


def setup(top=20):
    objs = corpus_v2()[0]
    tf = TfIdf([o["text"] for o in objs])
    rows, d = _rows_desc()
    cand = {str(r[C_ID]).strip(): [(s, objs[j])
                                   for s, j in tf.query(d[str(r[C_ID]).strip()], top=top)]
            for r in rows}
    return objs, tf, rows, d, cand, {i.rsplit("-", 1)[1]: i for i in cand}


# ── 獨立觀測之分組（R-SU17(b)）─────────────────────────────────────────
def clusters(keys, truth):
    """同一區塊鄰域之列合計為 1 個獨立觀測。

    操作型定義（執行層所訂，下放包 13 未給演算法，須經分析層確認）：
    037 列號相鄰（差 ≤ 2）**且**二列之正解物件 id 最近距離 ≤ 6 者連為一組。
    下放包 13 §四(iii) 明列之 `313`／`315`–`324` 須落在同一組，此為其檢核點。
    """
    ks = sorted(keys, key=int)
    groups, cur = [], [ks[0]]
    for a, b in zip(ks, ks[1:]):
        oa = [int(x) for x in truth[a]]
        ob = [int(x) for x in truth[b]]
        near = min(abs(x - y) for x in oa for y in ob)
        if int(b) - int(a) <= 2 and near <= 6:
            cur.append(b)
        else:
            groups.append(cur)
            cur = [b]
    groups.append(cur)
    return groups


def _counts(sel, groups):
    """(列數, 獨立觀測數) —— 獨立觀測數 = 被 sel 觸及之組數。"""
    s = set(sel)
    return len(s), sum(1 for g in groups if s & set(g))


# ── T26a —— 機制 4（分差偵測器）之回測 ────────────────────────────────
def t26a():
    objs, tf, rows, d, cand, idmap = setup(20)
    margins = sorted(v[0][0] - v[1][0] for v in cand.values() if len(v) > 1)
    tops = sorted(v[0][0] for v in cand.values() if v)
    n_m, n_t = len(margins), len(tops)
    mpct = {p: margins[int(n_m * p / 100)] for p in (5, 10, 15, 20)}
    th3 = tops[int(n_t * 20 / 100)]          # 機制 3 之現行門檻（R-SU14 v4(c)，第 20 百分位）

    print("## T26a —— 機制 4（分差偵測器）之回測\n")
    print(f"母體首選−次選分差之百分位（語料 v2，有次選者 n={n_m}；"
          f"首選分數 n={n_t}）：\n")
    print("| 百分位 | 門檻（分差） | 全母體攔下之列數 |")
    print("|---:|---:|---:|")
    for p, th in mpct.items():
        hit = sum(1 for v in cand.values() if len(v) > 1 and v[0][0] - v[1][0] < th)
        print(f"| 第 {p} | **{th:.3f}** | {hit} |")
    print(f"\n機制 3 之現行門檻（R-SU14 v4(c)，首選分第 20 百分位）＝ **{th3:.3f}**，"
          f"全母體攔下 **{sum(1 for v in cand.values() if v and v[0][0] < th3)}** 列。\n")

    # 缺口 = 其正解未被 N=5 完整涵蓋者（沿 T25a 之定義）
    gap, ok = [], []
    for k, v in GT_A1.items():
        i = idmap[k]
        top5 = {o["oid"] for _, o in cand[i][:5]}
        m = cand[i][0][0] - cand[i][1][0] if len(cand[i]) > 1 else float("inf")
        rec = (k, cand[i][0][0], m, set(v) - top5)
        (gap if not set(v) <= top5 else ok).append(rec)

    grp_all = clusters(GT_A1, GT_A1)
    grp_gap = [g for g in grp_all if {k for k, *_ in gap} & set(g)]
    grp_ok = [g for g in grp_all if {k for k, *_ in ok} & set(g)]

    print("### 獨立觀測之分組（R-SU17(b)）\n")
    print("操作型定義：037 列號相鄰（差 ≤ 2）**且**正解物件 id 最近距離 ≤ 6 者連為一組。")
    print("**此演算法為執行層所訂**（下放包 13 只給規則不給演算法），"
          "須經分析層確認；檢核點為 §四(iii) 所列之 `313`／`315`–`324` 落在同一組。\n")
    print("| 組 | 037 列 | 列數 |")
    print("|---:|---|---:|")
    for n, g in enumerate(grp_all, 1):
        print(f"| {n} | {'、'.join('`'+x+'`' for x in g)} | {len(g)} |")
    print(f"\nGT-A1 **28 列 → 獨立觀測 {len(grp_all)} 個**"
          f"（缺口組 {len(grp_gap)}、無缺口組 {len(grp_ok)}；"
          f"注意二者之和 {len(grp_gap)+len(grp_ok)} "
          f"{'>' if len(grp_gap)+len(grp_ok) > len(grp_all) else '='} {len(grp_all)}"
          f" —— 同一組內可同時含缺口列與無缺口列）。\n")

    print("### 缺口列之分差\n")
    print("| 037 列 | 首選分 | 首選−次選分差 | N=5 未涵蓋之正解 |")
    print("|---|---:|---:|---|")
    for k, s, m, miss in sorted(gap, key=lambda x: x[2]):
        print(f"| `SWE1-FOTA-{k}` | {s:.3f} | **{m:.3f}** | "
              f"{', '.join('`'+x+'`' for x in sorted(miss))} |")

    print("\n### 機制 4 之各門檻回測\n")
    print("| 門檻（分差百分位） | 值 | 攔下之缺口<br>列／獨立觀測 | 缺口召回<br>（列／獨立） "
          "| 誤報<br>列／獨立 | 誤報率<br>（列／獨立） |")
    print("|---|---:|---:|---:|---:|---:|")
    gl, gi = _counts([k for k, *_ in gap], grp_all)
    ol, oi = _counts([k for k, *_ in ok], grp_all)
    for p, th in mpct.items():
        h = [k for k, s, m, _ in gap if m < th]
        f = [k for k, s, m, _ in ok if m < th]
        hl, hi = _counts(h, grp_all)
        fl, fi = _counts(f, grp_all)
        print(f"| 第 {p} 百分位 | {th:.3f} | {hl}/{gl}／{hi}/{gi} | "
              f"**{hl/gl*100:.0f}%／{hi/gi*100:.0f}%** | {fl}/{ol}／{fi}/{oi} | "
              f"{fl/ol*100:.0f}%／{fi/oi*100:.0f}% |")

    print("\n### 機制 3 ∪ 機制 4（聯集）\n")
    m4 = mpct[10]
    print(f"取機制 3 門檻 {th3:.3f}（首選分第 20 百分位，R-SU14 v4(c) 已裁）"
          f"與機制 4 門檻 {m4:.3f}（分差第 10 百分位，**未裁，此處為試算**）：\n")
    print("| 集合 | 攔下之缺口<br>列／獨立 | 缺口召回<br>（列／獨立） | 誤報<br>列／獨立 | 全母體攔下 |")
    print("|---|---:|---:|---:|---:|")
    sets = {
        "機制 3（首選分低）": (lambda s, m: s < th3),
        "機制 4（分差小）": (lambda s, m: m < m4),
        "**3 ∪ 4**": (lambda s, m: s < th3 or m < m4),
        "3 ∩ 4": (lambda s, m: s < th3 and m < m4),
    }
    for name, fn in sets.items():
        h = [k for k, s, m, _ in gap if fn(s, m)]
        f = [k for k, s, m, _ in ok if fn(s, m)]
        hl, hi = _counts(h, grp_all)
        fl, fi = _counts(f, grp_all)
        pop = sum(1 for v in cand.values()
                  if v and fn(v[0][0], v[0][0] - v[1][0] if len(v) > 1 else float("inf")))
        print(f"| {name} | {hl}/{gl}／{hi}/{gi} | {hl/gl*100:.0f}%／{hi/gi*100:.0f}% "
              f"| {fl}/{ol}／{fi}/{oi} | {pop} 列 |")

    print("\n**缺口列逐列之被攔情形**（○ = 攔下）：\n")
    print("| 037 列 | 首選分 | 分差 | 機制 3 | 機制 4 | 3 ∪ 4 |")
    print("|---|---:|---:|:--:|:--:|:--:|")
    for k, s, m, _ in sorted(gap, key=lambda x: int(x[0])):
        a, b = s < th3, m < m4
        print(f"| `SWE1-FOTA-{k}` | {s:.3f} | {m:.3f} | {'○' if a else '×'} | "
              f"{'○' if b else '×'} | {'○' if a or b else '**×**'} |")

    # `260`（首選錯、正解排第 3）—— R-SU14 v4(e) 所引之第二例
    print("\n### R-SU14 v4(e) 所引二例之覆核\n")
    print("| 037 列 | 首選分 | 次選分 | 分差 | 正解排名 | v4(e) 所載 |")
    print("|---|---:|---:|---:|---:|---|")
    for k in ("292", "260"):
        i = idmap[k]
        rank = {o["oid"]: n for n, (_, o) in enumerate(cand[i], 1)}
        rk = "／".join(str(rank.get(x, "—")) for x in GT_A1[k])
        print(f"| `SWE1-FOTA-{k}` | {cand[i][0][0]:.3f} | {cand[i][1][0]:.3f} | "
              f"**{cand[i][0][0]-cand[i][1][0]:.3f}** | {rk} | "
              f"{'0.257／0.256／0.001' if k=='292' else '0.313／0.305／0.008'} |")
    return cand, idmap, grp_all


# ── T26c —— GT-A1 之章涵蓋實測 ────────────────────────────────────────
def t26c():
    objs = corpus_v2()[0]
    oid2chap = {o["oid"]: o["chap"] for o in objs}
    chaps = cfts_chapters()
    with_req = {o["chap"] for o in objs}

    hit = defaultdict(list)
    for k, v in sorted(GT_A1.items(), key=lambda x: int(x[0])):
        for x in v:
            hit[oid2chap.get(x, "?")].append(k)

    print("\n## T26c —— GT-A1 之章涵蓋實測\n")
    print(f"CFTS 章節物件 **{len(chaps)}**；其中**轄有需求物件者 "
          f"{len(with_req)} 章**，無需求物件者 {len(chaps)-len(with_req)} 章"
          f"（後者不可能成為任何正解之母章，**故有效分母為 {len(with_req)}**）。\n")
    print(f"### GT-A1 觸及之章（**{len(hit)} 章**）\n")
    print("| 章 | 標題 | 觸及之 037 列 | 列數 |")
    print("|---|---|---|---:|")
    tt = {c[0]: c[2] for c in chaps}
    for c in sorted(hit, key=lambda x: [int(y) for y in x.split(".")]):
        ks = sorted(set(hit[c]), key=int)
        print(f"| **{c}** | {tt.get(c,'—')[:44]} | {'、'.join('`'+k+'`' for k in ks)} | {len(ks)} |")
    print(f"\n上繳包 11 §7.1 稱「約 12 章」—— **精確值為 {len(hit)} 章**。\n")

    miss = [c for c in chaps if c[0] not in hit]
    miss_req = [c for c in miss if c[0] in with_req]
    print(f"### 未觸及之章（全清單，**{len(miss)} 章**；其中轄有需求物件者 "
          f"**{len(miss_req)} 章**）\n")
    print("| # | 章 | ObjectID | 標題 | 轄需求物件 |")
    print("|---:|---|---|---|---:|")
    per = Counter(o["chap"] for o in objs)
    for n, (num, oid, title) in enumerate(miss, 1):
        print(f"| {n} | {num} | `{oid}` | {title[:50]} | {per.get(num,0)} |")
    print(f"\n**閉合**：{len(hit)} + {len(miss)} = {len(hit)+len(miss)}"
          f"（應 {len(chaps)}）{' ✅' if len(hit)+len(miss)==len(chaps) else ' ❌'}｜"
          f"未觸及且轄有需求物件者 {len(miss_req)} 章，"
          f"共 **{sum(per.get(c[0],0) for c in miss_req)}** 個需求物件之錨定表現未測。")
    return hit, miss, with_req


# ── T26b —— GT-A2 分層隨機取樣材料 ────────────────────────────────────
SEED = 26


def t26b(cand=None, idmap=None, n_want=30):
    objs, tf, rows, d, cand2, idmap2 = setup(20)
    cand = cand or cand2
    idmap = idmap or idmap2
    hit, miss, with_req = t26c()
    touched = set(hit)

    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    by = {str(r[C_ID]).strip(): r for r in rows}
    allr = [r for r in openpyxl.load_workbook(A03, read_only=True, data_only=True)
            ["AnalysisReport_FULL"].iter_rows(min_row=8, values_only=True)
            if r[C_ID] not in (None, "")]
    head_of, cur = {}, ("—", "(前言)")
    for r in allr:
        if r[5] == "Heading":
            cur = (str(r[C_ID]).strip(), str(r[C_TITLE] or "").strip())
        else:
            head_of[str(r[C_ID]).strip()] = cur

    excl = {f"SWE1-FOTA-{k}" for k in GT_A1} | {f"SWE1-FOTA-{k}" for k in GT_B}
    pool = [i for i in by if i not in excl and cand.get(i)]

    # 分層鍵 = 首選候選之母章（**代理變數**，見上繳包自評）
    strata = defaultdict(list)
    for i in pool:
        strata[cand[i][0][1]["chap"]].append(i)

    rng = random.Random(SEED)
    order = sorted(strata, key=lambda c: [int(y) for y in c.split(".")])
    fresh = [c for c in order if c not in touched]
    old = [c for c in order if c in touched]
    rng.shuffle(fresh)
    rng.shuffle(old)
    seq = fresh + old
    for c in seq:
        strata[c] = rng.sample(strata[c], len(strata[c]))

    pick, taken = [], defaultdict(int)
    for rnd in (0, 1):                        # 每層至多 2 列：先一輪一列，再補第二列
        for c in seq:
            if len(pick) >= n_want:
                break
            if len(strata[c]) > rnd:
                pick.append((c, strata[c][rnd]))
                taken[c] += 1
        if len(pick) >= n_want:
            break

    print("\n## T26b —— GT-A2 分層隨機取樣材料（30 列）\n")
    print(f"- 分層鍵：**首選候選之 CFTS 母章**（R-SU17(a) 之「CFTS 母章」；"
          f"正解之母章在人裁前未知，**此處以路徑 A 之 top1 章為代理**）")
    print(f"- 抽樣池：311 − GT-A1 28 − GT-B 4 − 無候選列 = **{len(pool)}** 列，"
          f"落於 **{len(strata)}** 個層")
    print(f"- 取樣碼：`random.Random({SEED})`；先 `shuffle` 層序"
          f"（**未觸及之章優先於已觸及之章**），再 `sample` 層內全序，"
          f"取每層第 1 列（不足 30 時再取第 2 列）")
    print(f"- 每層至多 2 列（R-SU17(a)）；本批實際每層 "
          f"{'／'.join(f'{v} 列 × {k} 層' for k, v in sorted(Counter(taken.values()).items(), reverse=True))}\n")

    cov = {c for c, _ in pick}
    print("### 章涵蓋對照\n")
    print("| | 章數 | 佔 87 |")
    print("|---|---:|---:|")
    print(f"| GT-A1（定向，28 列） | {len(touched)} | {len(touched)/87*100:.0f}% |")
    print(f"| **GT-A2 本批（30 列）** | **{len(cov)}** | **{len(cov)/87*100:.0f}%** |")
    new = cov - touched
    print(f"| GT-A2 新增之章（GT-A1 未觸及） | {len(new)} | {len(new)/87*100:.0f}% |")
    print(f"| 二者聯集 | {len(touched|cov)} | {len(touched|cov)/87*100:.0f}% |")
    print(f"| 仍未觸及 | {87-len(touched|cov)} | {(87-len(touched|cov))/87*100:.0f}% |")
    print(f"\n> 分母 87 為全部章節物件；轄有需求物件者 {len(with_req)} 章，"
          f"以其為分母則本批涵蓋 {len(cov)/len(with_req)*100:.0f}%、"
          f"聯集 {len(touched|cov)/len(with_req)*100:.0f}%。\n")

    print("### 取樣清單\n")
    print("| # | 037 列 | 分層（首選章） | 該層池內列數 | 層別 |")
    print("|---:|---|---|---:|---|")
    for n, (c, i) in enumerate(pick, 1):
        print(f"| {n} | `{i}` | **{c}** | {len(strata[c])} | "
              f"{'GT-A1 未觸及' if c not in touched else 'GT-A1 已觸及'} |")

    print("\n---\n\n### 人裁材料（格式同 `07a`／`08a`，前 5 候選）\n")
    print("> **執行層不作判斷。** 各列之正解由分析層逐列裁定。\n")
    for n, (c, i) in enumerate(pick, 1):
        r = by[i]
        h = head_of.get(i, ("—", "—"))
        print(f"\n---\n\n#### {n}. `{i}` — {str(r[C_TITLE] or '').strip()}\n")
        print(f"- Heading：`{h[0]}` {h[1]}｜Sub Cat：{r[C_SUB] or '(blank)'}"
              f"｜Source：`{r[C_SRC]}`｜分層：**{c}**")
        print(f"\n**Requirement Description 全文**：\n\n> {d[i] or '(空)'}\n")
        print("**路徑 A（語料 v2）前 5 候選**：\n")
        for k, (s, o) in enumerate(cand.get(i, [])[:5], 1):
            print(f"{k}. `{o['oid']}` — 章 **{o['chap']}** {o['chap_title']} — 分 **{s:.3f}**")
            print(f"   > {o['text'][:400]}{'…' if len(o['text'])>400 else ''}\n")
    return pick


if __name__ == "__main__":
    want = set(sys.argv[1:]) or {"26a"}
    cand = idmap = None
    if "26a" in want:
        cand, idmap, _ = t26a()
    if "26c" in want and "26b" not in want:
        t26c()
    if "26b" in want:
        t26b(cand, idmap)
