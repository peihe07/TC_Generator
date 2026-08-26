#!/usr/bin/env python3
"""34 包 §三：TC 寫回 036（XML 外科式，R-VC2 同款）。

**輸出到 `features/display/output/`，`inputs/` 之母本一字不動。**
理由：`inputs/` 之母本為客戶素材且受 `reference:` 綁定（`workbook_master`，
sha `6372fb6be02f48dc…`）。就地覆寫會 (i) 毀去唯一一份原件、
(ii) 使 R-G23 之綁定檢查由 13/13 轉為 12/13。
他 feature 之慣例亦為 `output/`（`time_management`／`user_profiles`）。
下放包 34 §3.1 稱標的為「repo 內部複本」，本作法即產生該複本。

**不用 openpyxl 存檔** —— openpyxl 重寫整份工作簿，會丟失
`x14:dataValidation`、drawing 關聯等其未完整支援之部件。本腳本直接改
`xl/worksheets/sheetN.xml` 之目標儲存格，其餘部件**逐 byte 原樣重打包**。
"""
import json
import re
import sys
import zipfile
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
SHEET_NAME = "Test Case Specification 測試用例規範"
HEADER_ROW = 9
BATCHES = ("pilot-01", "rvc-01", "ops-01")
TC_PREFIX = "TC-DM-"
MASTER = ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA "
          "Test Case Specification & Result_SWQT_20260817_ext.xlsx")
OUT_NAME = ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA "
            "Test Case Specification & Result_SWQT_Display_20260826.xlsx")


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _set_row(sx, row, vals):
    """把 vals 寫入指定列；inlineStr 形態，不動 sharedStrings。"""
    mrow = re.search(r'(<row[^>]*\br="%d"[^>]*>)(.*?)(</row>)' % row, sx, re.S)
    cells = {}
    if mrow:
        for mc in re.finditer(r'<c\b[^>]*\br="([A-Z]+)%d"[^>]*?(?:/>|>.*?</c>)' % row,
                              mrow.group(2), re.S):
            cells[mc.group(1)] = mc.group(0)
    for col, v in vals.items():
        cells[col] = (f'<c r="{col}{row}" t="inlineStr">'
                      f'<is><t xml:space="preserve">{esc("" if v is None else v)}</t></is></c>')
    ordered = "".join(cells[c] for c in sorted(cells, key=lambda x: (len(x), x)))
    newrow = f'<row r="{row}">{ordered}</row>'
    if mrow:
        return sx[:mrow.start()] + newrow + sx[mrow.end():]
    m = re.search(r'</sheetData>', sx)
    return sx[:m.start()] + newrow + sx[m.start():]


def main() -> int:
    src = FEAT / "inputs" / MASTER
    outdir = FEAT / "output"
    outdir.mkdir(exist_ok=True)
    out = outdir / OUT_NAME

    cfg = (FEAT / "feature.yaml").read_text(encoding="utf-8")
    m = re.search(r'author_value:\s*"([^"]+)"', cfg)
    author = m.group(1) if m else "PeiPYHsu"

    tcs = []
    for b in BATCHES:
        d = json.loads((FEAT / "generated" / f"{b}.json").read_text(encoding="utf-8"))
        tcs += [(b, t) for t in d["tcs"]]

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    COLS = {"B": None, "D": "leaf_id", "F": None, "G": "test_group", "H": "test_set",
            "I": "test_item", "J": "pre_conditions", "K": "input_test_data",
            "L": "test_procedure", "M": "expected_result",
            "N": "specification_reference", "O": None, "P": "priority",
            "R": "design_method", "S": "functional_safety", "AA": None}

    written = []
    for i, (batch, t) in enumerate(tcs):
        r = HEADER_ROW + 1 + i
        vals = {}
        for c, key in COLS.items():
            if c == "B":
                vals[c] = str(i + 1)
            elif c == "F":
                vals[c] = f"{TC_PREFIX}{i + 1:03d}"
            elif c == "O":
                vals[c] = "NEW"
            elif c == "AA":
                vals[c] = author
            else:
                vals[c] = t[key]
        written.append((r, vals["F"], t["leaf_id"], batch))
        sx = _set_row(sx, r, vals)

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)

    print("# 寫回 036（XML 外科式）")
    print(f"來源（不動）: inputs/{MASTER[:60]}…")
    print(f"輸出        : output/{OUT_NAME[:60]}…")
    print(f"sheet xml   : {sheet_path}")
    print(f"author      : {author}")
    print(f"寫入列      : {written[0][0]} … {written[-1][0]}（{len(written)} 列）")
    print()
    print("| 列 | TC ID | leaf | 批次 |")
    print("|---|---|---|---|")
    for r, tid, leaf, b in written:
        print(f"| {r} | `{tid}` | `{leaf}` | {b} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
