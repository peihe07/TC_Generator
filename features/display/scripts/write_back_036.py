#!/usr/bin/env python3
"""34 包 §三：TC 寫回 036（XML 外科式，R-VC2 同款）。

**輸出到 `features/display/output/`，`inputs/` 之母本一字不動。**
理由：`inputs/` 之母本為客戶素材且受 `reference:` 綁定（`workbook_master`，
sha `6372fb6be02f48dc…`）。就地覆寫會 (i) 毀去唯一一份原件、
(ii) 使 R-G23 之綁定檢查由 13/13 轉為 12/13。
他 feature 之慣例亦為 `output/`（`time_management`／`user_profiles`）。
下放包 34 §3.1 稱標的為「repo 內部複本」，本作法即產生該複本。

**列序**（34b，Pei 2026-08-26 裁定「乙」）：交付版面之列序為
**Requirement ID 升冪**，批次序僅為生成時之內部順序，不得出現在交付版面。
無 TC 之需求補一空列（**僅 D 欄**，其餘欄不寫）。

**B 欄不寫**（R-DM15）：母本 B11 為共用公式之宿主
（`<f t="shared" ref="B11:B74" si="0">`），賦值會毀去該宿主，
使 B33–B74 之 `si="0"` 無定義。序號由 D 欄之填寫經公式自動產生。

**樣式保留**：改寫儲存格時保留原 `s=` 屬性，`<row>` 之
`spans`／`s`／`customFormat` 等屬性原樣留存 —— 否則框線、換行、
列高設定會隨寫入而消失。

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


def _leaf_order(tcs):
    """交付列序之需求全集（升冪）。取自 `data/recon.json` 之 leaves，
    前綴以 TC 實際所用者為準（recon 之 `SWE-DM-` 與 TC 之 `SWE1-DM-` 不同）。"""
    prefixes = {re.match(r'^(.*?)(\d+)$', t["leaf_id"]).group(1) for _, t in tcs}
    if len(prefixes) != 1:
        raise SystemExit(f"leaf_id 前綴不唯一：{sorted(prefixes)}")
    prefix = prefixes.pop()
    leaves = json.loads((FEAT / "data" / "recon.json").read_text(encoding="utf-8"))["leaves"]
    order = [prefix + re.match(r'^.*?(\d+)$', x).group(1) for x in leaves]
    order.sort()
    missing = {t["leaf_id"] for _, t in tcs} - set(order)
    if missing:
        raise SystemExit(f"TC 之 leaf 不在需求全集內：{sorted(missing)}")
    return order


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

    # B 欄不列（R-DM15：公式欄，賦值會毀去共用公式之宿主）
    COLS = {"D": "leaf_id", "F": None, "G": "test_group", "H": "test_set",
            "I": "test_item", "J": "pre_conditions", "K": "input_test_data",
            "L": "test_procedure", "M": "expected_result",
            "N": "specification_reference", "O": None, "P": "priority",
            "R": "design_method", "S": "functional_safety", "AA": None}

    # 34b：交付列序 = Requirement ID 升冪；同一需求內維持行為軸序（穩定排序）
    by_leaf = {}
    for batch, t in tcs:
        by_leaf.setdefault(t["leaf_id"], []).append((batch, t))

    written = []
    row = HEADER_ROW + 1
    seq = 0
    for leaf in _leaf_order(tcs):
        if not by_leaf.get(leaf):
            # 無 TC 之需求：僅 D 欄，其餘欄不寫（34b 裁定「乙」）
            sx = _set_row(sx, row, {"D": leaf})
            written.append((row, "", leaf, "（空列）"))
            row += 1
            continue
        for batch, t in by_leaf[leaf]:
            seq += 1
            vals = {}
            for c, key in COLS.items():
                if c == "F":
                    vals[c] = f"{TC_PREFIX}{seq:03d}"
                elif c == "O":
                    vals[c] = "NEW"
                elif c == "AA":
                    vals[c] = author
                else:
                    vals[c] = t[key]
            written.append((row, vals["F"], t["leaf_id"], batch))
            sx = _set_row(sx, row, vals)
            row += 1

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
    print(f"寫入列      : {written[0][0]} … {written[-1][0]}（{len(written)} 列，"
          f"含 {sum(1 for w in written if not w[1])} 空列）")
    print()
    print("| 列 | TC ID | leaf | 批次 |")
    print("|---|---|---|---|")
    for r, tid, leaf, b in written:
        print(f"| {r} | `{tid}` | `{leaf}` | {b} |")
    return 0


if __name__ == "__main__":
    sys.exit(main())
