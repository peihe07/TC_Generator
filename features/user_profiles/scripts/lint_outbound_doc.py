#!/usr/bin/env python3
"""對外文件之最小閘（28 包 R-1）—— **敘述之筆數 vs 表列之列數**。

## 為什麼只做這一項

27 輪自陳：「內部九支閘，對外文件一支都沒有，而它的精確度標準更高」。
其成因具體且可測 —— `26_rd_queries.md` 之附錄寫
`**seven** leaves … are displaced`，其下表只列 **4** 列。
**兩個數字來自兩個地方（一個來自 A-UP11 之範圍句、一個來自 23 輪之掃描結果），
我沒對過。**

**本閘只查這一件事。** 語意之審查留給人工 ——
「這個主張有沒有證據」不可測，「說七條而列四列」可測。
**把不可測的也塞進來，這支閘會開始誤報，然後被關掉。**

## 判準（**v2；v1 對其所為之文件本身誤報兩處**，見 `audit()` 之 docstring）

對每一張 markdown 表格，取其**緊鄰之前一個文字段落**：

1. 找其中形如 `<數字> <複數名詞>` 者（`seven leaves`／`3 conditions`）；
2. **只留「被數之物出現在該表之表頭或首欄」者**（`leaves` → `leaf`）；
3. **若該段內任一數字等於該表之資料列數 → 綠**；否則紅。

第 2、3 步是 v1 實跑後補的 —— **v1 把 `27_rd_queries_v2.md` 判成兩處紅，
而那兩處都是對的**（一段同時寫總數與本表筆數；另一段之 `180 leaves`
根本不是在數那張量測表）。**一支會把正確文件判紅的閘活不過三輪（R-G9）。**

## 盲區（R-G11）

1. **只看緊鄰之前一段。** 若筆數寫在表後、或隔了兩段，本閘看不見。
2. **只認英文數字詞與阿拉伯數字。** 中文「七條」不認 ——
   本閘為**對外（英文）文件**而設；內部文件不在其適用範圍。
3. **數字對得上不代表內容對。** 表列七列而文說七個，
   仍可能是七個錯的東西 —— 那是人工覆核之事。

Usage:
    python3 scripts/lint_outbound_doc.py docs/upstream/27_rd_queries_v2.md
    python3 scripts/lint_outbound_doc.py --self-test
"""

import argparse
import re
import sys
from pathlib import Path

WORD_NUM = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
    "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
}
# `<數字> <複數名詞>` —— 數字得為英文數字詞或阿拉伯數字；
# 名詞須以 s 結尾且長度 ≥ 3（排除 `is`／`as`）。允許中間夾 markdown 之 `**`。
COUNT_RE = re.compile(
    r"\b(?:\*\*)?(" + "|".join(WORD_NUM) + r"|\d{1,3})(?:\*\*)?\s+"
    r"(?:of\s+the\s+)?(?:\*\*)?([a-z][a-z-]{2,}s)\b", re.I)


def _num(tok: str) -> int:
    return int(tok) if tok.isdigit() else WORD_NUM[tok.lower()]


def blocks(md: str) -> list:
    """回傳 [(表格之資料列數, 其前一段落文字)]。"""
    lines = md.splitlines()
    out, i = [], 0
    while i < len(lines):
        if lines[i].lstrip().startswith("|"):
            start = i
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                i += 1
            rows = lines[start:i]
            # 扣表頭與分隔列
            data = [r for r in rows[2:] if r.strip().strip("|").strip()]
            j = start - 1
            while j >= 0 and not lines[j].strip():
                j -= 1
            para = []
            while j >= 0 and lines[j].strip() and \
                    not lines[j].lstrip().startswith(("|", "#")):
                para.append(lines[j])
                j -= 1
            head_cells = rows[0] + " " + " ".join(
                r.split("|")[1] if len(r.split("|")) > 1 else "" for r in data)
            head = {w.lower().rstrip("s") if w.lower() not in
                    ("status",) else w.lower()
                    for w in re.findall(r"[A-Za-z][A-Za-z-]{2,}", head_cells)}
            head |= {w.lower() for w in
                     re.findall(r"[A-Za-z][A-Za-z-]{2,}", head_cells)}
            out.append((len(data), " ".join(reversed(para)), head))
        else:
            i += 1
    return out


# 不規則複數 —— 只列本 feature 之對外文件實際會用到者
IRREGULAR = {"leaves": "leaf", "entries": "entry", "queries": "query"}
ANY_NUM = re.compile(r"\b(" + "|".join(WORD_NUM) + r"|\d{1,3})\b", re.I)


def _singular(w: str) -> str:
    w = w.lower()
    return IRREGULAR.get(w, w[:-1] if w.endswith("s") else w)


def audit(md: str, tables=None) -> list:
    """**判準改過一次（R-U37）。**

    v1 為「段落內之 `<數字> <複數名詞>` 若無一等於表列數即紅」。
    以其所為之文件（`27_rd_queries_v2.md`）實跑，**兩處皆誤報**：

    1. `Sections 12.8 and 12.8.1 are covered by **seven** leaves … In **four**
       of the seven …` ＋ 4 列之表 —— 該段**同時**寫了總數與本表之筆數，
       而 v1 只抓到前者（`four of the seven` 之被數之物不是複數名詞）。
    2. `measured across all **180 leaves** of this feature:` ＋ 4 列之量測表
       —— 那個 180 根本不是在數這張表。

    **一支會把正確文件判紅的閘活不過三輪（R-G9）**，故收兩道：

    - **被數之物須出現在該表之表頭或首欄**（`leaves` → `leaf`）；
      量測表之表頭為 `Measure | Result`，故第 2 例自此不再受檢。
    - **段落內任一數字等於表列數即通過**（不限「數字＋複數名詞」形態）；
      第 1 例之 `four` 因此救回。

    v1 之原始缺陷仍紅：其段落之數字為 7／12.8／037／one，**無一為 4**。
    """
    bad = []
    for n_rows, para, head in (tables if tables is not None else blocks(md)):
        claims = [(_num(m.group(1)), m.group(2))
                  for m in COUNT_RE.finditer(para)]
        # 只留「被數之物出現在表頭或首欄」者
        claims = [c for c in claims if _singular(c[1]) in head]
        if not claims:
            continue
        if any(_num(m.group(1)) == n_rows for m in ANY_NUM.finditer(para)):
            continue
        bad.append(
            f"筆數不符：表列 {n_rows} 列，而其前一段宣告 "
            f"{['%d %s' % c for c in claims]}，段內無一數字為 {n_rows} "
            f"→ 「{para.strip()[:80]}」")
    return bad


def self_test() -> int:
    cases = [
        ("**v1 之原形**：段落說 seven，表列 4 列 → **紅**",
         "In the 037 workbook, seven leaves have Title values that are "
         "displaced.\n\n| Leaf | Title |\n|---|---|\n| a | b |\n| c | d |\n"
         "| e | f |\n| g | h |\n", True),
        ("**v2 之形**：段落說 four，表列 4 列 → 綠",
         "In four of the seven, the Title names another subject.\n\n"
         "| Leaf | Title |\n|---|---|\n| a | b |\n| c | d |\n| e | f |\n"
         "| g | h |\n", False),
        ("段落說 three，表列 3 列 → 綠",
         "The remaining three are consistent.\n\n| Leaf | Note |\n|---|---|\n"
         "| a | b |\n| c | d |\n| e | f |\n", False),
        ("**誤報護欄**：段落只有頁碼與座標，無「數字＋複數名詞」→ 綠",
         "The marker was located on PDF page 14 at x = 101.4.\n\n"
         "| Item | Position |\n|---|---|\n| a | b |\n| c | d |\n", False),
        ("**誤報護欄**：`135 unique section ids` 之數字不指表列 → 綠（表列數相符者存在）",
         "We verified 169 rows and 4 items below.\n\n| Item | V |\n|---|---|\n"
         "| a | b |\n| c | d |\n| e | f |\n| g | h |\n", False),
        # ── 以下兩案取自 `27_rd_queries_v2.md` 之實跑 —— **v1 對它們誤報**
        ("**v1 誤報之一**：同段同時寫總數與本表筆數（seven … four of the seven）→ 綠",
         "Sections 12.8 and 12.8.1 are covered by **seven** leaves in the "
         "037 workbook. In **four** of the seven, the `Title` names a "
         "subject that belongs to a different leaf.\n\n"
         "| Leaf | Section | Title |\n|---|---|---|\n| a | b | c |\n"
         "| d | e | f |\n| g | h | i |\n| j | k | l |\n", False),
        ("**v1 誤報之二**：`180 leaves` 不指該量測表（表頭無 leaf）→ 綠",
         "That decision is evidence-based, measured across all 180 leaves "
         "of this feature:\n\n| Measure | Result |\n|---|---|\n"
         "| a | b |\n| c | d |\n| e | f |\n| g | h |\n", False),
        ("阿拉伯數字亦認：說 3 conditions 而表列 5 列 → **紅**",
         "The clause states 3 conditions.\n\n| Condition | Effect |\n|---|---|\n"
         "| a | b |\n| c | d |\n| e | f |\n| g | h |\n| i | j |\n", True),
    ]
    ok = True
    for name, md, expect in cases:
        bad = audit(md)
        good = bool(bad) == expect
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}: "
              f"{'紅' if bad else '綠'}，期望 {'紅' if expect else '綠'}")
        for b in bad:
            print(f"      └ {b}")
    print(f"\n{len(cases) if ok else '<' + str(len(cases))} / {len(cases)} "
          f"directional cases {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("path", nargs="?")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    if not a.path:
        ap.error("需要檔案路徑，或 --self-test")
    md = Path(a.path).read_text(encoding="utf-8")
    bad = audit(md)
    print(f"{a.path}：表格 {len(blocks(md))} 張，違規 {len(bad)}")
    for b in bad:
        print(f"  {b}")
    sys.exit(1 if bad else 0)
