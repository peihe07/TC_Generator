#!/usr/bin/env python3
"""T22 —— 語料 v2 與其重跑（下放包 09 §五）。

語料 v2（A-SU4 處分 §二，**凍結**）：
  需求物件語料 = 該物件自身之全文（以**任一 `[Artifact Type:…]` 宣告**
  為停界，故不含被吞併之 Description）＋ T12 對照表所歸屬之
  Description 全文（45 個）。歸章節之 Description（92）不入。

Usage:
    python3 scripts/corpus_v2.py 22a          # 語料 v2 + 雙重閉合
    python3 scripts/corpus_v2.py 22b 22c      # 重跑 / 回測
    python3 scripts/corpus_v2.py 22d          # 擴充材料
"""

import random
import re
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anchor_table import (CFTS, C_ID, C_TITLE, C_DESC, C_CAT, C_SUB, C_SRC,  # noqa: E402
                          A03, a03_rows, TfIdf)

HEAD, TOC = {"1", "2", "3", "4", "5"}, {"10", "20", "30", "40", "50"}
DECL_ANY = re.compile(r"^\s*(\d{7}):\s*\[Artifact Type:([^\]]*)\]")


def _paras():
    raw = zipfile.ZipFile(CFTS).read("word/document.xml").decode("utf8", "replace")
    out = []
    for p in re.findall(r"<w:p[ >].*?</w:p>", raw, re.S):
        m = re.search(r'<w:pStyle w:val="([^"]+)"', p)
        out.append(((m.group(1) if m else ""), re.sub(r"<[^>]+>", "", p)))
    return out


def corpus_v2():
    """回傳 (objs, descs, merges)。

    停界為**任一** Artifact Type 宣告或標題段 —— 這是 v2 之核心更正。
    Description 之歸屬沿 T12 之判準（文件序雙游標，跨章清空需求游標），
    與 `ANCHOR_POOL.md` §六 同源，故 45／92 之分割可對得上。
    """
    paras = _paras()
    idx = []
    for i, (st, t) in enumerate(paras):
        if st in TOC:
            continue
        if st in HEAD:
            m = re.search(r"^\s*([\d.]+)\s+(.*?)\s*\{(\d{7})\}", t)
            if m:
                idx.append(("H", i, m.group(1), m.group(2), None))
                continue
        m = DECL_ANY.match(t)
        if m:
            kind = "R" if m.group(2).strip() == "Subsystem Functional Requirement" else "D"
            idx.append((kind, i, m.group(1), None, m.group(2).strip()))

    objs, descs, seen = [], [], set()
    cur_chap, cur_req = None, None
    for k, (kind, i, oid, title, at) in enumerate(idx):
        if kind == "H":
            cur_chap, cur_req = {"num": oid, "title": title}, None   # 跨章清空（T12 同法）
            continue
        stop = idx[k + 1][1] if k + 1 < len(idx) else len(paras)
        body = " ".join(paras[j][1].strip() for j in range(i + 1, stop)
                        if paras[j][0] not in TOC and paras[j][1].strip())
        body = re.sub(r"\s+", " ", body).strip()
        if oid in seen:
            continue
        seen.add(oid)
        rec = dict(oid=oid, chap=cur_chap["num"] if cur_chap else "?",
                   chap_title=cur_chap["title"] if cur_chap else "?", own=body)
        if kind == "R":
            cur_req = oid
            objs.append(rec)
        else:
            rec["owner"] = cur_req                    # None → 歸章節
            descs.append(rec)

    by_oid = {o["oid"]: o for o in objs}
    merges = []
    for d in descs:
        if d["owner"] and d["owner"] in by_oid:
            merges.append((d["oid"], d["owner"], d["chap"], len(d["own"])))
    for o in objs:
        add = [d["own"] for d in descs if d.get("owner") == o["oid"]]
        o["text"] = re.sub(r"\s+", " ", (o["own"] + " " + " ".join(add))).strip()
    return objs, descs, merges


def t22a():
    objs, descs, merges = corpus_v2()
    print("## T22a —— 語料 v2 重建\n")
    own_empty = [o["oid"] for o in objs if not o["own"].strip()]
    txt_empty = [o["oid"] for o in objs if not o["text"].strip()]
    to_req = [d for d in descs if d.get("owner")]
    to_chap = [d for d in descs if not d.get("owner")]
    print("### 雙重閉合檢查（id 數 **與** 非空文字數，上繳包 06 §3.1 之教訓）\n")
    print("| 檢項 | 實測 | 應為 | |")
    print("|---|---:|---:|:--:|")
    rows = [("需求物件 id 數", len(objs), 487),
            ("需求物件**非空自身文字**數", len(objs) - len(own_empty), 487),
            ("需求物件**非空語料**數", len(objs) - len(txt_empty), 487),
            ("Description id 數", len(descs), 137),
            # ⚠ 應為值改自 T12 之 45／92 —— 見 A-SU5：T12 之游標被文件前置
            # 之 `Requirement ID nnn` 清單移動，致 4907923／4907934 誤歸
            # 4907907。以**宣告段位置**定歸屬之正確值為 43／94。
            ("Description 歸需求者", len(to_req), 43),
            ("Description 歸章節者", len(to_chap), 94)]
    for n, got, want in rows:
        print(f"| {n} | **{got}** | {want} | {'✅' if got == want else '❌'} |")
    if own_empty:
        print(f"\n**空自身文字者 {len(own_empty)}**：{own_empty}")

    lens = sorted(len(o["text"]) for o in objs)
    own = sorted(len(o["own"]) for o in objs)
    print(f"\n### 長度分布\n")
    print("| | 中位數 | 最短 | 最長 |")
    print("|---|---:|---:|---:|")
    print(f"| 自身文字（停界修正後） | {own[len(own)//2]} | {own[0]} | **{own[-1]}** |")
    print(f"| 語料 v2（自身 + 歸屬 Description） | {lens[len(lens)//2]} | {lens[0]} | **{lens[-1]}** |")
    top = max(objs, key=lambda o: len(o["text"]))
    print(f"\n最長者：`{top['oid']}`（章 {top['chap']}），"
          f"自身 {len(top['own'])} + 併入 {len(top['text'])-len(top['own'])} = **{len(top['text'])}** 字元")
    print(f"\n### 併入清單（{len(merges)} 筆：Description id → 宿主需求物件 id）\n")
    print("| Description | 宿主需求物件 | 章 | 併入字元 |")
    print("|---|---|---|---:|")
    for d, o, c, n in sorted(merges, key=lambda x: x[0]):
        print(f"| `{d}` | `{o}` | {c} | {n} |")
    print(f"\n併入總字元：**{sum(n for *_, n in merges):,}**")
    return objs


# ── 地面真值（下放包 09 §三，17 列）—— 分析層人裁，執行層不得改 ──
TRUTH = {
    "310": ["4907509"], "311": ["4907510"], "312": ["4907514"],
    "313": ["4907667", "4907668", "4907669", "4907670", "4907671", "4907672"],
    "315": ["4907667"], "316": ["4907668"],
    "179": ["4907481"], "180": ["4907482"],
    "260": ["4907314"], "261": ["4907315"], "262": ["4907317"],
    "257": ["4907334"], "284": ["4907440"], "034": ["4907457"],
    "176": ["4907476", "4907477"], "347": ["4907579"], "332": ["4907688"],
}


def _rows_desc():
    rows = a03_rows()
    return rows, {str(r[C_ID]).strip(): re.sub(r"\s+", " ", str(r[C_DESC] or "")).strip()
                  for r in rows}


def t22b(objs=None):
    objs = objs or corpus_v2()[0]
    tf = TfIdf([o["text"] for o in objs])
    rows, d = _rows_desc()
    out = {}
    for r in rows:
        i = str(r[C_ID]).strip()
        out[i] = [(s, objs[j]) for s, j in tf.query(d[i], top=5)]
    print("\n## T22b —— 語料 v2 之全面重跑（311 列 × 前 5 候選）\n")
    print("> **舊分數全部作廢**（A-SU4 處分 §三），本節不與其並陳。\n")
    tops = sorted(v[0][0] for v in out.values() if v)
    n = len(tops)
    print(f"- 有候選之列：**{n} / {len(rows)}**")
    print(f"- 首選分數分布：中位數 **{tops[n//2]:.3f}**、第 10 百分位 {tops[n//10]:.3f}、"
          f"最低 {tops[0]:.3f}、最高 {tops[-1]:.3f}")
    gaps = sorted(v[0][0] - v[1][0] for v in out.values() if len(v) > 1)
    m = len(gaps)
    print(f"- 首選與次選分差：中位數 **{gaps[m//2]:.3f}**、第 10 百分位 {gaps[m//10]:.3f}、最大 {gaps[-1]:.3f}")
    chaps = Counter(v[0][1]["chap"] for v in out.values() if v)
    print(f"- 首選之章分布（前 10）：{chaps.most_common(10)}")
    return out


RULES = [
    ("(i) 首選之章", lambda c: c[0][1]["chap"] if c else None),
    ("(ii) 前 3 候選之章眾數", lambda c: Counter(x[1]["chap"] for x in c[:3]).most_common(1)[0][0] if c else None),
    ("(iii) 前 5 候選之章眾數", lambda c: Counter(x[1]["chap"] for x in c).most_common(1)[0][0] if c else None),
    ("(iv) 分數加權之章投票", lambda c: max(
        {ch: sum(s for s, o in c if o["chap"] == ch) for ch in {o["chap"] for _, o in c}}.items(),
        key=lambda kv: kv[1])[0] if c else None),
]


def t22c(out=None):
    objs = corpus_v2()[0]
    out = out or t22b(objs)
    oid2chap = {o["oid"]: o["chap"] for o in objs}
    keys = [k for k in TRUTH if any(str(r).endswith(k) for r in out)]
    idmap = {i.rsplit("-", 1)[1]: i for i in out}
    print("\n## T22c —— 章級決策規則之回測（地面真值 17 列）\n")
    print("> ⚠ **回測集僅 17 列，統計效力有限** —— 單一誤判即改變 6 個百分點；"
          "本表只用以排序規則之優劣，不作為絕對準確率之估計。\n")
    truth_chaps = {k: {oid2chap[o] for o in v if o in oid2chap} for k, v in TRUTH.items()}
    print("| 規則 | 命中 | 準確率 | 誤判列 |")
    print("|---|---:|---:|---|")
    detail = {}
    for name, fn in RULES:
        hit, wrong = 0, []
        for k, tc in truth_chaps.items():
            i = idmap.get(k)
            got = fn(out.get(i, []))
            if got in tc:
                hit += 1
            else:
                wrong.append(f"`{k}`(得 {got}／應 {'/'.join(sorted(tc))})")
        detail[name] = (hit, wrong)
        print(f"| {name} | {hit}/17 | **{hit/17*100:.0f}%** | {'；'.join(wrong) if wrong else '—'} |")
    # 召回
    rec = 0
    for k, v in TRUTH.items():
        i = idmap.get(k)
        cand = {o["oid"] for _, o in out.get(i, [])}
        if set(v) & cand:
            rec += 1
    full = sum(1 for k, v in TRUTH.items()
               if set(v) <= {o["oid"] for _, o in out.get(idmap.get(k), [])})
    print(f"\n- **前 5 候選之召回**（正解至少一個在候選內）：**{rec}/17（{rec/17*100:.0f}%）**")
    print(f"- 前 5 候選涵蓋**全部**正解物件者：**{full}/17（{full/17*100:.0f}%）**")
    return detail


def t22d(out=None):
    objs = corpus_v2()[0]
    out = out or t22b(objs)
    rows, d = _rows_desc()
    by = {str(r[C_ID]).strip(): r for r in rows}
    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    allr = [r for r in openpyxl.load_workbook(A03, read_only=True, data_only=True)
            ["AnalysisReport_FULL"].iter_rows(min_row=8, values_only=True)
            if r[C_ID] not in (None, "")]
    head_of, cur = {}, ("—", "(前言)")
    for r in allr:
        if r[C_CAT] == "Heading":
            cur = (str(r[C_ID]).strip(), str(r[C_TITLE] or "").strip())
        else:
            head_of[str(r[C_ID]).strip()] = cur
    num = lambda i: int(i.rsplit("-", 1)[1])
    grp = lambda lo, hi: [i for i in by if lo <= num(i) <= hi]
    done = {f"SWE1-FOTA-{k}" for k in TRUTH}
    pick = ["SWE1-FOTA-292"] + [i for i in sorted(grp(310, 383)) if i not in done][:8]
    pick += [i for i in sorted(grp(215, 250)) if i not in done][:6]
    pick += [i for i in sorted(grp(138, 167)) if i not in done][:6]
    pick += [i for i in sorted(grp(111, 136)) if i not in done][:3]
    rng = random.Random(2)                       # 種子揭露：random.Random(2)
    pool = sorted(i for i in by if i not in done and i not in pick)
    pick += rng.sample(pool, 30 - len(pick))
    print("\n## T22d —— 地面真值擴充材料（30 列）\n")
    print("取樣：`292` 1 列、`309` 群另 8、`214` 群 6、`137` 群 6、`110` 群 3，"
          "其餘自 `random.Random(2).sample(pool, n)`。**執行層不作判斷。**\n")
    for n_, i in enumerate(pick, 1):
        r = by[i]
        h = head_of.get(i, ("—", "—"))
        print(f"\n---\n\n### {n_}. `{i}` — {str(r[C_TITLE] or '').strip()}\n")
        print(f"- Heading：`{h[0]}` {h[1]}｜Sub Cat：{r[C_SUB] or '(blank)'}｜Source：`{r[C_SRC]}`")
        print(f"\n**Requirement Description 全文**：\n\n> {d[i] or '(空)'}\n")
        print("**路徑 A（語料 v2）前 5 候選**：\n")
        for k, (s, o) in enumerate(out.get(i, []), 1):
            print(f"{k}. `{o['oid']}` — 章 **{o['chap']}** {o['chap_title']} — 分 **{s:.3f}**")
            print(f"   > {o['text'][:400]}{'…' if len(o['text'])>400 else ''}\n")
    return pick


if __name__ == "__main__":
    want = set(sys.argv[1:]) or {"22a"}
    objs = corpus_v2()[0]
    if "22a" in want:
        t22a()
    out = t22b(objs) if {"22b", "22c", "22d"} & want else None
    if "22c" in want:
        t22c(out)
    if "22d" in want:
        t22d(out)
