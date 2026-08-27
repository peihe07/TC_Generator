#!/usr/bin/env python3
"""T21a–d —— 地面真值建置（下放包 08 §三）。

R-SU13 v2「一」限定探針來源：不得取自任何自動比對之產物。本檔只做
**來源文件自身寫出之對應**（自證錨）之搜尋，與供人裁之材料傾印。
執行層不作任何對應判斷。

Usage:
    python3 scripts/ground_truth.py 21a
    python3 scripts/ground_truth.py 21a 21b 21c 21d
"""

import random
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anchor_table import (C_ID, C_TITLE, C_DESC, C_CAT, C_SUB, C_SRC,   # noqa: E402
                          a03_rows, cfts_objects, TfIdf)

ROOT = Path(__file__).resolve().parent.parent


def desc(r):
    return re.sub(r"\s+", " ", str(r[C_DESC] or "")).strip()


def rid(r):
    return str(r[C_ID]).strip()


# ── T21a —— 自證錨之四式 ─────────────────────────────────────────────
# 每式之 regex 逐一揭露；命中附原句摘錄。偽陽性風險逐式標註。
PATTERNS = [
    # 式 1：`490xxxx` 形 ObjectID。CFTS_57 之物件 id 皆為 490xxxx。
    ("式1 ObjectID", r"(?<!\d)(490\d{4})(?!\d)",
     "CFTS_57 之 7 位 Polarion id 全部以 490 起始（ANCHOR_POOL 實測 574/574）"),
    # 式 2：CFTS 章節號。限 4 層以內、首段為 1–9，避免命中版本號與日期。
    ("式2 章節號", r"(?<![\d.])([1-9](?:\.\d{1,2}){1,3})(?![\d.])",
     "形如 4.10.2；**偽陽性風險最高之一式**，須逐句人工複核"),
    # 式 3：`CFTS` 字樣及其後號碼。
    ("式3 CFTS 字樣", r"CFTS[_\s-]?0?(\d{2,3})(?:[_\s-]?(\d+(?:\.\d+)*))?",
     "如 CFTS057、CFTS_57 4.10；含他 CFTS 之引用（非本件者為偽陽性）"),
    # 式 4：引號內文字，事後與 87 個 CFTS 章節標題逐字比對。
    ("式4 引號內章節標題", r"[\"“']([^\"”']{6,80})[\"”']",
     "只有與 87 個章節標題**逐字相同**者才算命中，其餘為一般引號"),
]


def t21a():
    rows = a03_rows()
    objs, _ = cfts_objects()
    oid_set = {o["oid"] for o in objs}
    oid2chap = {o["oid"]: o["chap"] for o in objs}
    chaps = {o["chap"] for o in objs}
    titles = {}
    for o in objs:
        titles.setdefault(o["chap_title"].strip().lower(), o["chap"])

    print("## T21a —— 自證錨之全面搜尋\n")
    print("掃描範圍：311 個 in-scope 列之 `Requirement Description` 全文。\n")
    print("### 各式之 regex 與偽陽性風險（逐式揭露）\n")
    print("| 式 | regex | 依據／偽陽性風險 |")
    print("|---|---|---|")
    for name, pat, note in PATTERNS:
        print(f"| {name} | `{pat}` | {note} |")

    found = {name: [] for name, _, _ in PATTERNS}
    for r in rows:
        d = desc(r)
        if not d:
            continue
        for name, pat, _ in PATTERNS:
            for m in re.finditer(pat, d):
                tok = m.group(1)
                s, e = max(0, m.start() - 70), min(len(d), m.end() + 70)
                quote = ("…" if s else "") + d[s:e] + ("…" if e < len(d) else "")
                # 逐式之「是否真為自引」判定 —— 只用可驗之集合，不臆斷
                if name == "式1 ObjectID":
                    ok, tgt = tok in oid_set, oid2chap.get(tok)
                elif name == "式2 章節號":
                    ok, tgt = tok in chaps, tok
                elif name == "式3 CFTS 字樣":
                    ok, tgt = tok in ("57", "057"), (m.group(2) or "—")
                else:
                    key = tok.strip().lower()
                    ok, tgt = key in titles, titles.get(key)
                found[name].append(dict(id=rid(r), tok=tok, ok=ok, tgt=tgt, quote=quote))

    for name, _, _ in PATTERNS:
        hits = found[name]
        real = [h for h in hits if h["ok"]]
        print(f"\n### {name} —— 命中 {len(hits)}，**可驗為自引 {len(real)}**，"
              f"偽陽性 {len(hits)-len(real)}\n")
        if not real:
            print("（無可驗命中）")
        else:
            print("| 037 列 | token | 所指 | 原句摘錄 |")
            print("|---|---|---|---|")
            for h in real:
                print(f"| `{h['id']}` | `{h['tok']}` | **{h['tgt']}** | {h['quote'][:150]} |")
        fp = [h for h in hits if not h["ok"]]
        if fp:
            c = Counter(h["tok"] for h in fp)
            print(f"\n偽陽性 token 前 10：{c.most_common(10)}")
    return found


# ── T21b —— 人裁樣本材料傾印 ─────────────────────────────────────────
def t21b():
    rows = a03_rows()
    objs, _ = cfts_objects()
    tfidf = TfIdf([o["text"] for o in objs])
    by_id = {rid(r): r for r in rows}

    # 所屬 Heading（含非 in-scope 之 Heading 列，故重讀全表）
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    from anchor_table import A03
    allrows = [r for r in openpyxl.load_workbook(A03, read_only=True, data_only=True)
               ["AnalysisReport_FULL"].iter_rows(min_row=8, values_only=True)
               if r[C_ID] not in (None, "")]
    head_of, cur = {}, ("—", "(前言)")
    for r in allrows:
        if r[C_CAT] == "Heading":
            cur = (str(r[C_ID]).strip(), str(r[C_TITLE] or "").strip())
        else:
            head_of[str(r[C_ID]).strip()] = cur

    def grp(lo, hi):
        return [rid(r) for r in rows if lo <= int(rid(r).rsplit("-", 1)[1]) <= hi]

    picked = grp(310, 383)[:6] + grp(292, 308)[:3] + grp(179, 184)[:2] + grp(260, 262)
    rng = random.Random(0)                       # 種子揭露：random.seed(0)
    pool = [i for i in by_id if i not in picked]
    picked += rng.sample(sorted(pool), 6)

    print("## T21b —— 人裁樣本材料傾印（20 列）\n")
    print("取樣碼：`309` 群前 6、`291` 群前 3、`178` 群前 2、`259` 群全 3，"
          "其餘 6 列自 `random.Random(0).sample(sorted(pool), 6)`。\n")
    print("**執行層不作任何對應判斷** —— 以下僅為材料。\n")
    for n, i in enumerate(picked, 1):
        r = by_id[i]
        h = head_of.get(i, ("—", "—"))
        print(f"\n---\n\n### {n}. `{i}` — {str(r[C_TITLE] or '').strip()}\n")
        print(f"- 所屬 Heading：`{h[0]}` {h[1]}")
        print(f"- Sub Categorization：{r[C_SUB] or '(blank)'}｜Source Requirement ID：`{r[C_SRC]}`")
        print(f"\n**Requirement Description 全文**：\n\n> {desc(r) or '(空)'}\n")
        print("**路徑 A 前 5 候選**：\n")
        for k, (s, j) in enumerate(tfidf.query(desc(r), top=5), 1):
            o = objs[j]
            print(f"{k}. `{o['oid']}` — 章 **{o['chap']}** {o['chap_title']} — 分 **{s:.3f}**")
            print(f"   > {o['text'][:400]}{'…' if len(o['text'])>400 else ''}\n")
    return picked


# ── T21c —— 序位一致性預備量測 ───────────────────────────────────────
def t21c():
    rows = a03_rows()
    objs, _ = cfts_objects()
    tfidf = TfIdf([o["text"] for o in objs])
    pts = []
    for r in rows:
        q = tfidf.query(desc(r), top=1)
        pts.append((rid(r), q[0][1] if q else None, q[0][0] if q else 0.0))
    ok = [(i, j) for i, j, _ in pts if j is not None]
    print("## T21c —— 序位一致性之預備量測（支柱 2）\n")
    print("> **本步驟明確依賴路徑 A**（以其首選為輸入），**已知非獨立**"
          "——R-SU13 v2「二」已將其定為加諸於 A 之結構約束，非第二來源。\n")
    print(f"- 可判列（A 有首選者）：**{len(ok)} / {len(rows)}**")
    seq = [j for _, j in ok]
    inv = sum(1 for a in range(len(seq)) for b in range(a + 1, len(seq)) if seq[b] < seq[a])
    total = len(seq) * (len(seq) - 1) // 2
    # 最長單調不減子序列
    import bisect
    tails = []
    for x in seq:
        k = bisect.bisect_right(tails, x)
        if k == len(tails):
            tails.append(x)
        else:
            tails[k] = x
    print(f"- 違序對數：**{inv:,}** / {total:,} 對（{inv/total*100:.1f}%）")
    print(f"- 最長單調不減子序列長度：**{len(tails)}** / {len(seq)}"
          f"（{len(tails)/len(seq)*100:.1f}%）")
    print(f"\n### 散點資料（037 列序 → CFTS 物件文件序位）\n")
    print("| # | 037 列 | CFTS 物件序位 | A 首選分 |")
    print("|---:|---|---:|---:|")
    for n, (i, j, s) in enumerate(pts, 1):
        print(f"| {n} | `{i}` | {j if j is not None else '—'} | {s:.3f} |")
    return pts


# ── T21d —— 全文抽取品質抽驗 ─────────────────────────────────────────
def t21d():
    objs, fail = cfts_objects()
    rng = random.Random(1)                       # 種子揭露：random.Random(1)
    sample = rng.sample(range(len(objs)), 15)
    print("## T21d —— T20a 全文抽取品質抽驗（15 / 487）\n")
    print("種子：`random.Random(1).sample(range(487), 15)`。\n")
    print(f"抽取失敗總數：**{len(fail)}**\n")
    lens = sorted(len(o["text"]) for o in objs)
    print(f"全文長度分布：中位數 {lens[len(lens)//2]}、最短 {lens[0]}、最長 {lens[-1]}\n")
    for n, k in enumerate(sorted(sample), 1):
        o = objs[k]
        print(f"\n---\n\n### {n}. `{o['oid']}` — 章 {o['chap']} {o['chap_title']}\n")
        print(f"- 全文長度：{len(o['text'])} 字元\n")
        print(f"> {o['text'][:900]}{'…' if len(o['text'])>900 else ''}\n")
    return objs, sample


if __name__ == "__main__":
    want = set(sys.argv[1:]) or {"21a"}
    if "21a" in want:
        t21a()
    if "21b" in want:
        t21b()
    if "21c" in want:
        t21c()
    if "21d" in want:
        t21d()
