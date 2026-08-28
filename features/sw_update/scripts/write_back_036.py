#!/usr/bin/env python3
"""T30e —— 036 之 XML 外科式寫回（自 `features/display/scripts/write_back_036.py` 移植）。

**只移植不改行為**（下放包 17 §六 T30e）。逐字移植者：`esc()`、`_set_row()`、
zip 逐 byte 重打包之迴圈 —— 三者為外科式之本體。
本 feature 專屬者：母本檔名、sheet 名、`COLS`（依 `feature.yaml` §workbook）、
以及 **`--empty` 空寫回模式**（寫 0 列，供 T30e 之前後比對）。

**不用 openpyxl 存檔**（R-SU2）：openpyxl 重寫整份工作簿，會摧毀 R 欄之
`x14:dataValidation`（`下拉選單!$A$1:$A$9`）。本腳本直接改
`xl/worksheets/sheetN.xml` 之目標儲存格，其餘部件**逐 byte 原樣重打包**。

**輸出到 `output/`，`inputs/` 之母本一字不動**（沿 display 之慣例；
`output/` 於 `.gitignore` 內）。

Usage:
    python3 scripts/write_back_036.py --empty     # 空寫回 + 前後比對
"""
import hashlib
import re
import sys
import zipfile
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
SHEET_NAME = "Test Case Specification 測試用例規範"
HEADER_ROW = 9                      # feature.yaml §workbook.header_row
MASTER = ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA "
          "Test Case Specification & Result_SWQT_20260817_ext.xlsx")
OUT_NAME = ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA "
            "Test Case Specification & Result_SWQT_SWUpdate_EMPTY_20260828.xlsx")

# feature.yaml §workbook.columns（B 欄不寫 —— 共用公式之宿主，同 R-DM15 之理由）
COLS = {"D": "req_id", "G": "test_group", "H": "test_set", "I": "test_item",
        "J": "pre_conditions", "K": "input_test_data", "L": "test_procedure",
        "M": "expected_result", "N": "spec_reference", "O": "tc_ref_id",
        "P": "priority", "R": "design_method", "S": "functional_safety",
        "AA": "author", "AH": "remarks"}

# R-SU2 令前後比對之各項 + 上繳包 15 §4.4 之基線
BASELINE = {"zip 部件總數": 48, "worksheet 數": 9,
            "<dataValidation （sheet6，標準）": 3,
            "<x14:dataValidation （sheet6）": 1, "<extLst>（sheet6）": 1,
            "<conditionalFormatting（全簿）": 0, "printerSettings": 5,
            "media": 2, "drawing 相關部件": 13, 't="shared"': 1401}


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _set_row(sx, row, vals):
    """把 vals 寫入指定列；inlineStr 形態，不動 sharedStrings。

    保留原 `<row>` 之屬性（`spans`／`s`／`customFormat`／`ht`）與各儲存格
    原有之 `s=` 樣式索引；未列於 vals 之儲存格逐 byte 原樣留存。
    """
    mrow = re.search(r'(<row[^>]*\br="%d"[^>]*>)(.*?)(</row>)' % row, sx, re.S)
    open_tag = f'<row r="{row}">'
    cells = {}
    styles = {}
    if mrow:
        open_tag = mrow.group(1)
        for mc in re.finditer(r'<c\b[^>]*\br="([A-Z]+)%d"[^>]*?(?:/>|>.*?</c>)' % row,
                              mrow.group(2), re.S):
            cells[mc.group(1)] = mc.group(0)
            ms = re.search(r'\bs="(\d+)"', mc.group(0))
            if ms:
                styles[mc.group(1)] = ms.group(1)
    for col, v in vals.items():
        st = f' s="{styles[col]}"' if col in styles else ""
        cells[col] = (f'<c r="{col}{row}"{st} t="inlineStr">'
                      f'<is><t xml:space="preserve">{esc("" if v is None else v)}</t></is></c>')
    ordered = "".join(cells[c] for c in sorted(cells, key=lambda x: (len(x), x)))
    newrow = f'{open_tag}{ordered}</row>'
    if mrow:
        return sx[:mrow.start()] + newrow + sx[mrow.end():]
    m = re.search(r'</sheetData>', sx)
    return sx[:m.start()] + newrow + sx[m.start():]




def _metrics(path):
    z = zipfile.ZipFile(path)
    names = z.namelist()
    raw = {n: z.read(n).decode("utf8", "replace")
           for n in names if n.endswith((".xml", ".rels"))}
    s6 = raw.get("xl/worksheets/sheet6.xml", "")
    return {
        "zip 部件總數": len(names),
        "worksheet 數": sum(1 for n in names if re.match(r"xl/worksheets/sheet\d+\.xml$", n)),
        "<dataValidation （sheet6，標準）": len(re.findall(r"<dataValidation ", s6)),
        "<x14:dataValidation （sheet6）": len(re.findall(r"<x14:dataValidation ", s6)),
        "<extLst>（sheet6）": len(re.findall(r"<extLst>", s6)),
        "<conditionalFormatting（全簿）": sum(len(re.findall(r"<conditionalFormatting", v))
                                              for v in raw.values()),
        "printerSettings": sum(1 for n in names if "printerSettings" in n),
        "media": sum(1 for n in names if n.startswith("xl/media/")),
        "drawing 相關部件": sum(1 for n in names if "drawing" in n.lower()),
        't="shared"': sum(len(re.findall(r't="shared"', v)) for v in raw.values()),
    }


def main(empty=False):
    src = FEAT / "inputs" / MASTER
    before = hashlib.sha256(src.read_bytes()).hexdigest()
    outdir = FEAT / "output"
    outdir.mkdir(exist_ok=True)
    out = outdir / OUT_NAME

    with zipfile.ZipFile(src) as z:
        wbxml = z.read("xl/workbook.xml").decode("utf-8")
        rels = z.read("xl/_rels/workbook.xml.rels").decode("utf-8")
        rid = re.search(r'<sheet[^>]*name="%s"[^>]*r:id="([^"]+)"'
                        % re.escape(SHEET_NAME), wbxml).group(1)
        tgt = re.search(r'Id="%s"[^>]*Target="([^"]+)"' % re.escape(rid), rels).group(1)
        sheet_path = "xl/" + tgt.lstrip("/")
        sx = z.read(sheet_path).decode("utf-8")

    tcs = []                                  # T30e：本輪不產出 TC，空寫回
    if not empty:
        sys.exit("本 feature 尚無 TC（generated/ 為空）；"
                 "現階段只支援 `--empty`（T30e 之前後比對）。")
    written = []
    row = HEADER_ROW + 1
    for t in tcs:                             # 空迴圈 —— sx 一字未改
        sx = _set_row(sx, row, {c: t[k] for c, k in COLS.items()})
        written.append(row)
        row += 1

    with zipfile.ZipFile(src) as zin, \
            zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zo:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == sheet_path:
                data = sx.encode("utf-8")
            zo.writestr(item, data)


    after = hashlib.sha256(src.read_bytes()).hexdigest()
    mb, ma = _metrics(src), _metrics(out)

    print("## T30e —— 外科式寫回之空寫回前後比對\n")
    print(f"- 來源（不動）：`inputs/{MASTER[:52]}…`")
    print(f"- 輸出：`output/{OUT_NAME[:52]}…`（`.gitignore` 內）")
    print(f"- sheet xml：`{sheet_path}`｜寫入列數：**{len(written)}**（空寫回）\n")
    print("| 量 | 母本（基線） | 輸出 | 上繳包 15 §4.4 | |")
    print("|---|---:|---:|---:|:--:|")
    ok = True
    for k in BASELINE:
        good = mb[k] == ma[k] == BASELINE[k]
        ok &= good
        note = ""
        if k.startswith("<conditionalFormatting"):
            note = " ⚠"
        print(f"| `{k}` | {mb[k]} | {ma[k]} | {BASELINE[k]} | "
              f"{'✅' if good else '❌'}{note} |")
    same = before == after
    ok &= same
    print(f"| **母本 SHA256 前後** | `{before[:12]}…` | `{after[:12]}…` | 未變 | "
          f"{'✅' if same else '❌'} |")
    print(f"\n> ⚠ **`<conditionalFormatting` 之計數為 0** —— 本母本無條件式格式，"
          f"**該項前後相等恆真通過，在本 feature 不具鑑別力**（上繳包 15 §4.4）。"
          f"R-SU2 令比對故仍跑，但**其通過不得計為證據**。\n")
    print(f"- sheet6 之 XML 是否逐字未變："
          f"**{'是' if zipfile.ZipFile(src).read(sheet_path) == zipfile.ZipFile(out).read(sheet_path) else '否'}**"
          f"（空寫回應為「是」）")
    zi, zo = zipfile.ZipFile(src), zipfile.ZipFile(out)
    diff = [n for n in zi.namelist() if zi.read(n) != zo.read(n)]
    print(f"- 逐部件 byte 比對：**{len(diff)} / {len(zi.namelist())}** 個部件內容相異"
          + (f" —— {diff}" if diff else " ✅"))
    print(f"- 部件名稱與順序：**{'相同' if zi.namelist() == zo.namelist() else '**相異**'}**")
    print(f"\n**空寫回結果：{'全部通過 ✅' if ok and not diff else '**不通過 ❌**'}**")
    return 0 if (ok and not diff) else 1


if __name__ == "__main__":
    sys.exit(main(empty="--empty" in sys.argv))
