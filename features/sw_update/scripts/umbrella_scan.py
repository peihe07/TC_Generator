#!/usr/bin/env python3
"""T23a / T23c —— 統攝型語形普查與受併宿主之可回測性檢查（下放包 10 §五）。

R-SU15(e)：全母體語形掃描，不得只處理已發現之一列。
**執行層只分類語形，不裁定該列是否為統攝型**（判定屬分析層）。

Usage:
    python3 scripts/umbrella_scan.py 23a
    python3 scripts/umbrella_scan.py 23c
"""

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpus_v2 import corpus_v2, TRUTH, _rows_desc   # noqa: E402
from anchor_table import C_ID, TfIdf                  # noqa: E402

# 每式 regex 逐一揭露。式名對應 R-SU15 之 (b)/(c) 兩群：
#   有 id 群 —— 命中處鄰近有 490xxxx 列舉
#   無 id 群 —— 只指涉節號／表號／「以下」
FORMS = [
    ("式A defined in System Requirement(s)",
     r"defined\s+in\s+(?:the\s+)?System\s+Requirements?\b",
     "R-SU15(a) 之典型語形，313/315/316 即此式"),
    ("式B defined in <section/table>",
     r"defined\s+in\s+(?:the\s+)?(?!System\s+Requirement)"
     r"(?:section|clause|chapter|table|figure|appendix)\b",
     "指涉節/表號而不列 id → (c) 群候選"),
    ("式C as listed in / listed below / as follows",
     r"\b(?:as\s+listed\s+in|listed\s+below|as\s+follows|following\s+(?:table|list))\b",
     "列舉引導語；其後之列舉未必為 id"),
    ("式D the <conditions|errors|requirements|steps> in/of",
     r"\bthe\s+(?:conditions?|errors?|requirements?|steps?|scenarios?|states?)\s+"
     r"(?:defined|described|specified|listed)?\s*(?:in|of|per)\b",
     "指涉類語形，涵蓋 R-SU15(a) 所舉之 `the conditions in <節>`"),
    ("式E described/specified in <ref>",
     r"\b(?:described|specified|referenced|detailed)\s+in\b",
     "式B/D 之補集：其他「見某處」語形"),
    ("式F 純 id 列舉（≥3 個 490xxxx）",
     r"(?:(?<!\d)490\d{4}(?!\d)\D{0,12}){3,}",
     "無統攝動詞但密集列舉 id 者 —— 語形之外的結構線索"),
]


# 反向探測 —— 用以檢定「某式 0 命中」是語料真的沒有，還是 regex 太嚴。
# **不改上列六式**（改式即為看著結果轉旋鈕）；本節之發現另列為「漏網」。
PROBES = ["listed", "as follows", "following", "defined in", "described in",
          "specified in", "refer to", r"\bsee\b", r"\bsection\b", r"\btable\b",
          r"\bchapter\b", r"\bper the\b", "in accordance", r"\babove\b",
          r"\bbelow\b", "respectiv", r"\bmentioned\b", r"\bshall\b"]


def reverse_probe(d):
    print("\n### 反向探測 —— 檢定「0 命中」之真偽\n")
    print("> 六式中式B／式C／式D 皆 0 命中。0 可能是**語料真的沒有**，"
          "也可能是**regex 太嚴**。以下用更寬鬆之裸字串探測區辨。"
          "**六式不因本節而修改** —— 改式即為看著結果轉旋鈕。\n")
    print("| 裸字串探測 | 命中列 |")
    print("|---|---:|")
    for p in PROBES:
        k = sum(1 for i in d if re.search(p, d[i], re.I))
        print(f"| `{p}` | {k} |")


def t23a():
    rows, d = _rows_desc()
    ids = [str(r[C_ID]).strip() for r in rows]
    print("## T23a —— 統攝型語形之全母體普查（311 列）\n")
    print("> **執行層只分類語形，不裁定該列是否為統攝型**（R-SU15 之判定屬分析層）。\n")
    print("### 各式之 regex（逐一揭露）\n")
    print("| 式 | regex | 說明 |")
    print("|---|---|---|")
    for n, p, note in FORMS:
        print(f"| {n} | `{p}` | {note} |")

    hit = defaultdict(list)
    for i in ids:
        txt = d[i]
        for n, p, _ in FORMS:
            for m in re.finditer(p, txt, re.I):
                s, e = max(0, m.start() - 90), min(len(txt), m.end() + 110)
                hit[n].append((i, ("…" if s else "") + txt[s:e] + ("…" if e < len(txt) else "")))

    print("\n### 命中總覽\n")
    print("| 式 | 命中次數 | 相異列 |")
    print("|---|---:|---:|")
    for n, _, _ in FORMS:
        print(f"| {n} | {len(hit[n])} | **{len({i for i,_ in hit[n]})}** |")
    allrows = {i for n, _, _ in FORMS for i, _ in hit[n]}
    print(f"| **聯集** | — | **{len(allrows)} / 311（{len(allrows)/311*100:.1f}%）** |")

    # (b)/(c) 分群：命中列之 Description 內是否有 490xxxx
    has_id = {i for i in allrows if re.search(r"(?<!\d)490\d{4}(?!\d)", d[i])}
    print(f"\n### R-SU15 之兩群分類（依命中列自身是否列舉 490xxxx）\n")
    print(f"- **(b) 有 id 群**：**{len(has_id)}** 列 —— {sorted(has_id)}")
    print(f"- **(c) 無 id 群**：**{len(allrows)-len(has_id)}** 列")

    reverse_probe(d)

    for n, _, _ in FORMS:
        rs = sorted({i for i, _ in hit[n]})
        print(f"\n### {n} —— {len(rs)} 列\n")
        if not rs:
            print("（無命中）")
            continue
        print("| 037 列 | 群 | 原句摘錄 |")
        print("|---|---|---|")
        seen = set()
        for i, q in hit[n]:
            if i in seen:
                continue
            seen.add(i)
            g = "**(b) 有 id**" if i in has_id else "(c) 無 id"
            print(f"| `{i}` | {g} | {q[:190]} |")
    return allrows, has_id


def t23c():
    objs, descs, merges = corpus_v2()
    hosts = {o for _, o, _, _ in merges}
    tf = TfIdf([o["text"] for o in objs])
    rows, d = _rows_desc()
    # 30 列擴充樣本 —— 與 corpus_v2.t22d 同一取樣碼
    import random
    by = {str(r[C_ID]).strip(): r for r in rows}
    num = lambda i: int(i.rsplit("-", 1)[1])
    grp = lambda lo, hi: [i for i in by if lo <= num(i) <= hi]
    done = {f"SWE1-FOTA-{k}" for k in TRUTH}
    pick = ["SWE1-FOTA-292"] + [i for i in sorted(grp(310, 383)) if i not in done][:8]
    pick += [i for i in sorted(grp(215, 250)) if i not in done][:6]
    pick += [i for i in sorted(grp(138, 167)) if i not in done][:6]
    pick += [i for i in sorted(grp(111, 136)) if i not in done][:3]
    rng = random.Random(2)
    pool = sorted(i for i in by if i not in done and i not in pick)
    pick += rng.sample(pool, 30 - len(pick))

    print("\n## T23c —— 受併宿主於 30 列擴充樣本候選中之出現檢查\n")
    print(f"受併宿主共 **{len(hosts)}** 個（A-SU4 所指之同一批）。")
    print("> **只檢查候選內出現與否，不預判其正解**（下放包 10 §五 T23c）。\n")
    found = []
    for i in pick:
        for k, (s, j) in enumerate(tf.query(d[i], top=5), 1):
            if objs[j]["oid"] in hosts:
                found.append((i, objs[j]["oid"], objs[j]["chap"], k, s))
    if not found:
        print("**候選內未出現任何受併宿主 —— 30 列樣本仍不足以回測虛高效應。**")
    else:
        print("| 037 列 | 受併宿主 | 章 | 名次 | 分 |")
        print("|---|---|---|---:|---:|")
        for i, o, c, k, s in found:
            print(f"| `{i}` | `{o}` | {c} | {k} | {s:.3f} |")
        print(f"\n**{len({i for i,*_ in found})} / 30 列**之候選內出現受併宿主，"
              f"共 {len(found)} 次。")
    # 全母體對照，供判斷 30 列是否為特例
    allhit = set()
    for i in d:
        for _, j in tf.query(d[i], top=5):
            if objs[j]["oid"] in hosts:
                allhit.add(i)
                break
    print(f"\n全母體對照：**{len(allhit)} / 311 列**（{len(allhit)/311*100:.1f}%）"
          f"之前 5 候選內含受併宿主。")
    return found


if __name__ == "__main__":
    want = set(sys.argv[1:]) or {"23a"}
    if "23a" in want:
        t23a()
    if "23c" in want:
        t23c()
