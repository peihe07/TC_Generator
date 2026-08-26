#!/usr/bin/env python3
"""T38 —— 依 R-VC15 覆核既有產出之計數是否標註母體。

R-VC15 之四個母體：
    145 列     037 `Analysis Report` 之全部資料列（列 8–152）
    117 leaf   R-VC3 所裁之驗證母體（子需求 ∪ 無子之父）
     66 section 037 `HMI Source ID` 之相異章節號
    108 outline SYS1 `Basic Report` 之有效 `Outline Number`

R-VC15 拘束的是**計數**，不是每一個數字。故本掃描分兩步：

  步驟 1 —— 遮蔽非計數之數字形態，使其不進入判定。
      識別碼（T35／A-VC12／R-VC15／DR-VC7／REV-11／PU0091）、
      章節號（§11.9.3／11.9.1）、雜湊、日期與版本（SR24／26PI／R1）、
      位元組數與 SHA、Markdown 之表格對齊列。
      **遮蔽是本掃描之主要偽陰性來源**，故遮蔽規則逐條列於此，可覆核。

  步驟 2 —— 對倖存之數字，檢查其是否緊鄰一個**母體詞**
      （列／leaf／section／節／outline／筆／個／組 …）。
      未緊鄰者列為「未標母體」；一行內出現二個以上目標計數
      而其母體詞不同或缺一者，另列為「疑似跨母體互援」。

只讀不寫。偽陰性見上繳包 06 §7。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# ---- 步驟 1：遮蔽規則（逐條可覆核）
MASKS = [
    (re.compile(r"\b[0-9a-f]{16,64}\b"), "雜湊"),
    (re.compile(r"\b[TR]-?VC\d+|[TR]\d{1,3}\b"), "任務／裁決識別碼"),
    (re.compile(r"\bA-(?:VC|TM|DM|PMH|H|C|U|G)\d+"), "異常識別碼"),
    (re.compile(r"\bR-(?:VC|TM|DM|PMH|G|C|U)\d+"), "裁決識別碼"),
    (re.compile(r"\bDR-VC\d+|\bREV-\d+"), "DR／修訂識別碼"),
    (re.compile(r"\bPU\d{4}\b"), "彈窗 id"),
    (re.compile(r"SWE1-HMI-VC-\d{3}(?:-\d{2})?"), "需求 id"),
    (re.compile(r"NRL-\d+"), "Polarion id"),
    (re.compile(r"§ ?\d+(?:\.\d+)*"), "章節號（帶 §）"),
    (re.compile(r"(?<![\d])\d+\.\d+(?:\.\d+)*(?![\d])"), "章節號（裸）"),
    (re.compile(r"\bSR\d+|\b\d+PI[\d.]*|\bR1[LH]?\b|\bFM-WI-FSM-\d+"), "版本／文件編號"),
    (re.compile(r"20\d\d[-/年]\d{1,2}[-/月]\d{1,2}|20\d\d-\d\d-\d\d"), "日期"),
    (re.compile(r"\b\d{1,3}(?:,\d{3})+\b"), "位元組數（帶千分位）"),
    (re.compile(r"^\s*\|[\s:|-]+\|\s*$"), "表格對齊列"),
    (re.compile(r"P[0-3]\b|\bU\+00A0|\bx14\b|\bxa0"), "優先級／編碼常數"),
]

TOTALS = {"145": "列", "117": "leaf", "66": "section", "108": "outline"}
SUBS = ["42", "28", "79", "38", "61", "24", "25", "18", "17",
        "16", "22", "12", "103", "88", "128", "15", "30", "13", "9"]

POP_WORD = (r"列|筆|個|leaf|section|節|outline|欄|組|章|rows?|entries|"
            r"leaves|sections|assertion|項|條|檔|頁|份")
# 數字後最多 4 個字元內出現母體詞，或數字前緊接母體詞（如「leaf 數 117」）
NEAR = re.compile(
    r"(?<![\d.\-])(" + "|".join(sorted(set(list(TOTALS) + SUBS),
                                       key=len, reverse=True))
    + r")(?![\d.%])\s*(?:個|筆)?\s*(?:" + POP_WORD + r")")
BARE = re.compile(
    r"(?<![\d.\-])(" + "|".join(sorted(set(list(TOTALS) + SUBS),
                                       key=len, reverse=True))
    + r")(?![\d.%])")

FILES = sorted(
    list((ROOT / "docs" / "handoff").glob("*.md"))
    + list((ROOT / "docs" / "upstream").glob("*.md"))
    + [ROOT / "RULINGS.md", ROOT / "ANOMALIES.md",
       ROOT / "DATA_REQUESTS.md", ROOT / "RUNBOOK.md",
       ROOT / "docs" / "REVISIONS.md",
       ROOT / "docs" / "DECISIONS_signoff_draft.md",
       ROOT / "data" / "tableB_draft.md",
       ROOT / "framework.md"])


def mask(line: str) -> str:
    for pat, _ in MASKS:
        line = pat.sub(lambda m: "�" * len(m.group(0)), line)
    return line


marked, unmarked, cross = 0, [], []
for f in FILES:
    if not f.exists():
        continue
    for i, ln in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        m = mask(ln)
        nums = BARE.findall(m)
        if not nums:
            continue
        near = set(NEAR.findall(m))
        for n in set(nums):
            if n in near:
                marked += 1
            else:
                unmarked.append((f.relative_to(ROOT), i, n, ln.strip()[:104]))
        # 疑似跨母體互援：同一行出現二個以上**不同母體之總數**
        tot = {n for n in set(nums) if n in TOTALS}
        if len(tot) >= 2:
            cross.append((f.relative_to(ROOT), i, sorted(tot),
                          ln.strip()[:104]))

print(f"掃描檔數: {sum(1 for f in FILES if f.exists())}")
print(f"遮蔽規則: {len(MASKS)} 條")
print(f"計數命中（遮蔽後）: {marked + len(unmarked)}")
print(f"  緊鄰母體詞: {marked}")
print(f"  未緊鄰母體詞: {len(unmarked)}")
print(f"同行出現二個以上母體總數（疑似互援，須人工判讀）: {len(cross)}\n")

print("=== A. 疑似跨母體互援")
for c in cross:
    print(f"{c[0]}:{c[1]}  總數 {c[2]}")
    print(f"    {c[3]}")

print("\n=== B. 未緊鄰母體詞之計數（前 40 筆）")
for u in unmarked[:40]:
    print(f"{u[0]}:{u[1]}  [{u[2]}]  {u[3]}")
print(f"\n（共 {len(unmarked)} 筆，全表見執行時之完整輸出）")
sys.exit(0)
