#!/usr/bin/env python3
"""覆寫記法之母體擴掃（23 包 M-3）—— **不限 `**` 起首**。

## 為什麼要擴掃

`data/pdf_starred_notes.tsv` 之 10 條由 `\\*{2,}` pattern 掃出，
V-1（D-UP22-02）之母體再自其中取 `kind == 變體覆寫註記` 者，**現為 4 條**。
兩層過濾，各有其漏：

| 層 | 漏 |
|---|---|
| `\\*{2,}` | **未以 `**` 起首**之覆寫記法整條看不見 |
| `kind` 欄 | **分類本身可能錯** —— 而它是 07 輪人工填的 |

**實測結果：真正的漏在第二層，不在第一層。**
p9 之 `NOPR0.) R1 High` 與 p12 之 `NEWPR0.) R1 High Only: this passage is not
meant to be implemented` 兩條**有** `**`、也**在** TSV 內，
卻被歸為 `圖／表內標籤` —— 於是 V-1 之母體看不到它們。
**擴掃 pattern 不會救到這兩條；重新判 kind 才會。**

## 三分法（22 輪 §3.6 之分野，本輪再細一層）

| 判 | 定義 | 入 V-1 母體？ |
|---|---|---|
| **覆寫** | 依**變體／市場**指定**另一個字面值或另一種適用性** | **是** |
| **適用條件** | 該項在某配置下不顯示，**但未指定替代物** | 否 |
| **狀態條件** | 條件為**執行期狀態**（如達上限）而非變體 | 否 |

第三類為本輪新增：`5.2` 之 `A text will be displayed instead` 確實是替代，
**但其條件是「達到 5 個 profile」—— 那是狀態，不是變體**。
V-1 管的是變體軸；把狀態條件收進來，它會與一般的條件式行為混為一談。

Usage:
    python3 scripts/scan_override_notes.py            # 掃並印出
    python3 scripts/scan_override_notes.py --write    # 寫出 data/override_notes_m3.tsv
    python3 scripts/scan_override_notes.py --check    # 與該檔比對，飄移即紅
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render_spec_region as R                        # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
OUT_TSV = FEATURE / "data" / "override_notes_m3.tsv"

# 語意形態 —— **不含 `*`**，故與 `pdf_starred_notes.tsv` 之 pattern 正交
PATTERNS = {
    "Only:": r"[^\n]{0,90}\bOnly\s*:[^\n]{0,110}",
    "not applicable": r"[^\n]{0,90}not applicable[^\n]{0,110}",
    "replaced with": r"[^\n]{0,90}(?:to be replaced with|replaced by)[^\n]{0,110}",
    "instead": r"[^\n]{0,90}\binstead\b[^\n]{0,110}",
    "(if applicable)": r"[^\n]{0,70}\(if applicable\)[^\n]{0,70}",
    "do not show this": r"[^\n]{0,90}(?:do not show this|does not apply)[^\n]{0,110}",
}

# 逐條判讀（**人工**，本輪 23 包 M-3）。鍵為 (page, 文字前 44 字元之正規化)。
# `axis` 非空者即 V-1 之母體成員。
VERDICTS = {
    ("p9", "Only: this passage is not"):
        ("覆寫", "6.1", "R1 High：CPA 不啟動、改自 Edit Profile 進入 —— "
                        "**TSV 誤歸為「圖／表內標籤」**", "r1h-cpa-6.1"),
    ("p12", '****NEWPR0.) R1 High Only: this passage is n'):
        ("覆寫", "8.1", "R1 High：該段不實作、步驟 4 後直接進 Tutorials —— "
                        "**TSV 誤歸為「圖／表內標籤」**", "r1h-cpa-8.1"),
    ("p14", '****R1 High Only: "Stellantis Account" to'):
        ("覆寫", "9.1", "帳號 label 之替代", "p14-account-label"),
    ("p16", '****R1 High Only: for the "Connected Account'):
        ("覆寫", "10.3.1", "Table PIP1 該列之 Description 替代", "p16-pip1-desc"),
    ("p17", '**R1 High Only: This table (Table CPA2) is n'):
        ("覆寫", "11.4", "整張表不適用", "p17-cpa2-table"),
    ("p17", '****For China market only: do not show this '):
        ("覆寫", "11.4", "Connected Navigation 列不顯示", "p17-china-row"),
    ("p17", 'CPA2.) [This whole note is not applicable fo'):
        ("覆寫", "11.4", "與 `**R1 High Only: This table…` 同一覆寫之另一表達，"
                         "**不另立 axis**", "p17-cpa2-table"),
    ("p7", 'Profile tab and all the other tabs). This lo'):
        ("適用條件", "5.1.2", "7 吋螢幕不適用 —— **未指定替代物**；"
                              "037 之 leaf 標題已載 `Large Screens`", ""),
    ("p7", "he string described in note PRACC7.2 will no"):
        ("狀態條件", "5.2", "達 5 個 profile 上限時改顯示 PU0584 —— "
                            "**條件為狀態非變體**；已由 TC-003 覆蓋", ""),
    ("p13", 'setup Process, the back arrow will take the '):
        ("適用條件", "8.6", "back arrow 之前一步「若有」", ""),
    ("p13", 'One will be highlighted, and if they choose '):
        ("適用條件", "8.8", "選取行為之描述，非覆寫", ""),
    ("p14", "“Memory Seat” (If applicable)"):
        ("適用條件", "9.1", "Table EDPR1 之列項適用條件", ""),
    ("p16", "(if applicable)"):
        ("適用條件", "10.3.1", "Table PIP1 之列項適用條件", ""),
    ("p16", "Navigation (if applicable)"):
        ("適用條件", "10.3.1", "同上", ""),
}


def scan() -> list:
    doc = R.fitz.open(R.SPEC_PDF) if hasattr(R, "fitz") else None
    if doc is None:
        import fitz
        doc = fitz.open(R.SPEC_PDF)
    rows, seen = [], set()
    for kind, pat in PATTERNS.items():
        rx = re.compile(pat, re.I)
        for i, page in enumerate(doc, 1):
            for m in rx.finditer(page.get_text()):
                text = " ".join(m.group(0).split())
                key = (f"p{i}", text[:44])
                if key in seen:
                    continue
                seen.add(key)
                rows.append((f"p{i}", kind, text))
    return sorted(rows, key=lambda r: (int(r[0][1:]), r[1]))


def verdict_of(page: str, text: str) -> tuple:
    return VERDICTS.get((page, text[:44]), ("**未判**", "", "", ""))


def render() -> str:
    out = ["# override_notes_m3.tsv — 23 包 M-3：覆寫記法之母體擴掃（**不限 `**`**）",
           "#",
           "# 由 scripts/scan_override_notes.py 產生。**逐條判讀為人工**，",
           "# 三分法：覆寫／適用條件／狀態條件（詳見該檔 docstring）。",
           "# axis 欄非空者即 V-1（D-UP22-02）之母體成員。",
           "page\tpattern\tverdict\tsection\taxis\tnote\ttext"]
    for page, kind, text in scan():
        v, sec, note, axis = verdict_of(page, text)
        out.append(f"{page}\t{kind}\t{v}\t{sec}\t{axis}\t{note}\t{text}")
    return "\n".join(out) + "\n"


def override_axes() -> list:
    """判為「覆寫」者之 (axis, section, page)。V-1 之母體。"""
    out = []
    for page, _kind, text in scan():
        v, sec, _note, axis = verdict_of(page, text)
        if v == "覆寫" and axis:
            out.append((axis, sec, page))
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    body = render()
    if a.write:
        OUT_TSV.write_text(body, encoding="utf-8")
        print(f"寫出 {OUT_TSV}")
        sys.exit(0)
    if a.check:
        if not OUT_TSV.exists():
            print("**FAIL** — data/override_notes_m3.tsv 不存在")
            sys.exit(1)
        same = OUT_TSV.read_text(encoding="utf-8") == body
        print("掃描結果與 data/override_notes_m3.tsv "
              + ("一致" if same else "**不一致 —— 母體已飄移**"))
        sys.exit(0 if same else 1)
    rows = scan()
    un = [(p, t) for p, _k, t in rows if verdict_of(p, t)[0] == "**未判**"]
    print(f"PDF 全文命中 {len(rows)} 處；未判 {len(un)} 處\n")
    for page, kind, text in rows:
        v, sec, note, axis = verdict_of(page, text)
        mark = {"覆寫": "[覆寫]", "適用條件": "[適用]", "狀態條件": "[狀態]"}.get(v, "[**未判**]")
        print(f"  {mark} {page:4} {sec:8} {text[:82]}")
    print(f"\n入 V-1 母體之 axis：{sorted({a for a, _s, _p in override_axes()})}")
    sys.exit(1 if un else 0)
