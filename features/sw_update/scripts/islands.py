#!/usr/bin/env python3
"""T30a／T30b —— 孤島列之 Description 傾印、Priority／SubCat 空白之實測（下放包 17 §六）。

Usage: python3 scripts/islands.py 30a 30b
"""

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from framework_survey import a03_rows, C_ID, C_TITLE, C_DESC, C_CAT, C_SUB, IN_SCOPE  # noqa: E402

C_PRIO = 15                       # `Priority` —— 037 表頭列 7 實測（T30b）

# §四 之 PROVISIONAL-ROW 五列
PROV = ["338", "357", "359", "360", "361"]
# §六 T30a 所令之比較基準列
BASE = {"312": "Integrity 之基準（GT 正解 `4907514`，章 4.8.3）",
        "321": "Interruption 之基準（近義標題群）",
        "325": "Interruption 之基準（近義標題群）",
        "323": "Concurrent NIA（`359` 之疑似同族）",
        "337": "Deployment Flow Initiation（`338` 之前鄰）"}
NUM = lambda r: int(re.search(r"(\d+)$", str(r[C_ID])).group(1))


def t30a():
    rows = {str(r[C_ID]).strip().rsplit("-", 1)[1]: r
            for r in a03_rows() if r[C_CAT] in IN_SCOPE}
    print("## T30a —— 孤島列與其比較基準列之 Description 全文（9 列）\n")
    print("> **僅全文**（下放包 17 §六）：不附分數、不附候選。"
          "**執行層不裁定其歸屬。**\n")

    print("### 甲 —— 五個 `PROVISIONAL-ROW`\n")
    for k in PROV:
        r = rows[k]
        print(f"\n---\n\n#### `SWE1-FOTA-{k}` — {str(r[C_TITLE] or '').strip()}\n")
        print(f"- 現置 Test Set：{_cur(k)}｜Sub Cat：{r[C_SUB] or '(blank)'}"
              f"｜Priority：{r[C_PRIO] or '**(blank)**'}")
        print("\n**Requirement Description 全文**：\n")
        print("> " + (_desc(r) or "(空)") + "\n")

    print("\n### 乙 —— 五個比較基準列\n")
    for k, why in BASE.items():
        r = rows[k]
        print(f"\n---\n\n#### `SWE1-FOTA-{k}` — {str(r[C_TITLE] or '').strip()}\n")
        print(f"- 用途：{why}｜現置 Test Set：{_cur(k)}"
              f"｜Sub Cat：{r[C_SUB] or '(blank)'}｜Priority：{r[C_PRIO] or '**(blank)**'}")
        print("\n**Requirement Description 全文**：\n")
        print("> " + (_desc(r) or "(空)") + "\n")


def _desc(r):
    return re.sub(r"\s+", " ", str(r[C_DESC] or "")).strip()


def _cur(k):
    from layer2_close import SETS, H
    from framework_survey import group_by_heading
    gmap = {g["id"]: g for g in group_by_heading(a03_rows())[1:]}
    n = int(k)
    for name, items in SETS:
        for it in items:
            if isinstance(it, str):
                if any(NUM(r) == n for r in gmap[H(it)]["rows"]):
                    return f"`{name}`"
            elif it[1] <= n <= it[2]:
                return f"`{name}`"
    return "—"


def t30b():
    rows = [r for r in a03_rows() if r[C_CAT] in IN_SCOPE]
    allr = a03_rows()
    print("\n## T30b —— 驗證母體 311 列中 Priority／Sub Cat 空白之實測\n")

    blank_p = [str(r[C_ID]).strip() for r in rows if r[C_PRIO] in (None, "")]
    blank_s = [str(r[C_ID]).strip() for r in rows if r[C_SUB] in (None, "")]
    from collections import Counter
    c = Counter(r[C_PRIO] or "(blank)" for r in rows)

    print("### Priority 之分布 —— 驗證母體 311 vs 全 383 資料列\n")
    call = Counter(r[C_PRIO] or "(blank)" for r in allr)
    print("| Priority | 驗證母體 311 | 全 383 資料列 | 差（= Heading 等非範圍列） |")
    print("|---|---:|---:|---:|")
    for k in ("High", "Medium", "Low", "(blank)"):
        print(f"| `{k}` | **{c[k]}** | {call[k]} | {call[k]-c[k]} |")
    print(f"| **合計** | **{sum(c.values())}** | {sum(call.values())} | "
          f"{sum(call.values())-sum(c.values())} |")
    print(f"\n> 上繳包 01 §之「空白 72」為**全 383 資料列**之數；"
          f"**驗證母體 311 列中之空白為 {c['(blank)']} 列**（R-SU22.3 所令之實測）。\n")

    print(f"### Priority 空白之列（{len(blank_p)}）\n")
    print("；".join(f"`{i}`" for i in blank_p) if blank_p else "**無**")

    print(f"\n\n### Sub Categorization 空白之列（{len(blank_s)}）\n")
    print("；".join(f"`{i}`" for i in blank_s) if blank_s else "**無**")

    both = sorted(set(blank_p) & set(blank_s))
    print(f"\n\n### 二者是否同列\n")
    print(f"- Priority 空白 ∩ SubCat 空白：**{len(both)}** —— "
          + ("；".join(f"`{i}`" for i in both) if both else "**空集**"))
    print(f"- 僅 Priority 空白：**{len(set(blank_p)-set(blank_s))}**")
    print(f"- 僅 SubCat 空白：**{len(set(blank_s)-set(blank_p))}** —— "
          + ("；".join(f"`{i}`" for i in sorted(set(blank_s)-set(blank_p))) or "—"))
    return blank_p, blank_s




# ── T31b —— pilot 材料傾印（下放包 18 §五）────────────────────────────
PILOT = ["175", "176", "177", "179", "180", "181", "182", "183", "184"]
TH3 = 0.267                      # 機制 3 之門檻（R-SU14 v4(c)，首選分第 20 百分位）


def t31b():
    from corpus_v2 import corpus_v2, _rows_desc, TRUTH
    from anchor_table import TfIdf, C_SRC
    from block_anchor import TRUTH2
    from stratified_gt import GT_A1
    from framework_survey import group_by_heading

    objs = corpus_v2()[0]
    tf = TfIdf([o["text"] for o in objs])
    rows_a, d = _rows_desc()
    cand = {str(r[C_ID]).strip(): [(s, objs[j])
                                   for s, j in tf.query(d[str(r[C_ID]).strip()], top=20)]
            for r in rows_a}
    by = {str(r[C_ID]).strip(): r for r in a03_rows() if r[C_CAT] in IN_SCOPE}
    gmap = {g["id"]: g for g in group_by_heading(a03_rows())[1:]}
    head_of = {str(r[C_ID]).strip(): g["id"] for g in gmap.values() for r in g["rows"]}
    # 區塊成員（T24c 之 9 塊）與自證錨
    from reverse_sample import blocks_of
    blk, _ = blocks_of(objs)

    print("\n\n## T31b —— pilot 材料：`Silent Update`（9 列）\n")
    print("- Test Set：**`Silent Update`**｜Layer 3 provisional：**`4.7.3.2` Silent Updates**"
          "（GT 支持：`176`／`179`／`180`）")
    print(f"- 所轄：(`SWE1-FOTA-170`, 175–177) + (`SWE1-FOTA-178`, 全群 179–184)"
          f" —— **跨 2 個 Heading 群**")
    print(f"- 機制 3 之門檻（R-SU14 v4(c)）：首選分 < **{TH3}**\n")

    print("### 概覽\n")
    print("| # | 037 列 | Heading 群 | Sub Cat | Priority | 首選分 | 機制 3 | GT | 標題 |")
    print("|---:|---|---|---|---|---:|:--:|:--:|---|")
    for n, k in enumerate(PILOT, 1):
        i = f"SWE1-FOTA-{k}"
        r, c = by[i], cand[i]
        s = c[0][0] if c else 0.0
        gt = "**✅ GT-A1**" if k in GT_A1 else "—"
        print(f"| {n} | `{i}` | `{head_of[i]}` | {r[C_SUB] or '(blank)'} | "
              f"{r[C_PRIO] or '(blank)'} | {s:.3f} | "
              f"{'**⚠ 攔下**' if s < TH3 else '—'} | {gt} | "
              f"{str(r[C_TITLE] or '').strip()[:38]} |")
    lo = [k for k in PILOT if cand[f"SWE1-FOTA-{k}"][0][0] < TH3]
    print(f"\n- 落入機制 3（低分偵測器）者：**{len(lo)}** 列"
          + (f" —— {'、'.join('`'+x+'`' for x in lo)}（其階段二應出前 20 候選）" if lo else "（無）"))
    print(f"- 有 GT-A1 人裁正解者：**{sum(1 for k in PILOT if k in GT_A1)}** 列 —— "
          + "、".join(f"`{k}`→`{'`,`'.join(GT_A1[k])}`" for k in PILOT if k in GT_A1))
    inblk = [k for k in PILOT if k in GT_A1
             and any(blk.get(o) for o in GT_A1[k])]
    print(f"- 其正解為**列舉區塊成員**者：**{len(inblk)}** 列"
          + (f" —— {'、'.join('`'+x+'`' for x in inblk)}" if inblk else "（無）"))
    print(f"- **自證錨**（R-SU13 v2 支柱 3）：本 9 列中**無**"
          f"（自證錨之已知實例為 `313`，不在本組）")

    print("\n---\n\n### 逐列材料\n")
    print("> **執行層不撰寫 TC、不裁定錨。** 本節為分析層起草 pilot TC 之材料。\n")
    for n, k in enumerate(PILOT, 1):
        i = f"SWE1-FOTA-{k}"
        r, c = by[i], cand[i]
        print(f"\n---\n\n#### {n}. `{i}` — {str(r[C_TITLE] or '').strip()}\n")
        print(f"- Heading 群：`{head_of[i]}` {gmap[head_of[i]]['title']}"
              f"｜Sub Cat：{r[C_SUB] or '(blank)'}｜Priority：{r[C_PRIO] or '(blank)'}"
              f"｜Source：`{r[C_SRC]}`")
        if k in GT_A1:
            print(f"- **GT-A1 已裁正解**：{'、'.join('`'+o+'`' for o in GT_A1[k])}"
                  f"（章 {objs and [o['chap'] for o in objs if o['oid']==GT_A1[k][0]][0]}）")
        s = c[0][0] if c else 0.0
        print(f"- 首選分 **{s:.3f}**"
              + (f" —— **< {TH3}，落入機制 3**，階段二應出前 20 候選" if s < TH3
                 else f" —— ≥ {TH3}，不落入機制 3"))
        print(f"\n**Requirement Description 全文**：\n")
        print("> " + (_desc(r) or "(空)") + "\n")
        print("**路徑 A（語料 v2）前 5 候選**：\n")
        for j, (sc, o) in enumerate(c[:5], 1):
            mark = " ← **GT 正解**" if k in GT_A1 and o["oid"] in GT_A1[k] else ""
            print(f"{j}. `{o['oid']}` — 章 **{o['chap']}** {o['chap_title']} — 分 **{sc:.3f}**{mark}")
            print(f"   > {o['text'][:420]}{'…' if len(o['text'])>420 else ''}\n")


if __name__ == "__main__":
    want = set(sys.argv[1:]) or {"30a", "30b"}
    if "30a" in want:
        t30a()
    if "30b" in want:
        t30b()
    if "31b" in want:
        t31b()
