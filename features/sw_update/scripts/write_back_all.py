#!/usr/bin/env python3
"""T84c —— 全簿寫回（319 TC），XML 外科式。

**沿用 `write_back_036.py` 之 `_set_row` 與逐 byte 重打包**（R-SU2：不用 openpyxl 存檔）。
其異於既有各批之處：**一次寫入全部 319 列**，輸出至 `delivered/`。

**比對之範圍依下放包 72 §五-4 之查證擴充**：
既有之 48 部件比對**不足以蘊含 Excel 可開** —— `sxm` 之 A-SX28 即
「內容層全綠而 `R` 欄下拉遺失」之先例，`amfm` R17-9 則指出 `calcChain.xml` 之
重建為推論而非實測。**故本腳本另比 `dataValidation` 節點數與 `calcChain` 之存廢。**

Usage: python3 scripts/write_back_all.py
"""
import hashlib
import importlib
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from write_back_036 import (_set_row, _metrics, BASELINE, COLS, FEAT,  # noqa: E402
                            HEADER_ROW, MASTER, SHEET_NAME)

A9_FALLBACK = ""
OUT_NAME = ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA "
            "Test Case Specification & Result_SWQT_SWUpdate_20260830.xlsx")
MODS = ["gen_pilot", "gen_batch01", "gen_batch02a", "gen_batch03", "gen_rov_a",
        "gen_rov_b", "gen_rov_cd", "gen_batch4", "gen_batch5", "gen_batch6",
        "gen_batch7", "gen_batch8", "gen_batch9", "gen_batch10", "gen_batch11",
        "gen_batch12", "gen_batch13", "gen_batch14", "gen_batch15", "gen_batch16",
        "gen_batch17", "gen_batch18", "gen_batch19", "gen_batch20", "gen_batch21",
        "gen_batch22", "gen_batch23"]
TEST_GROUP = "SW Update"
AUTHOR = "PeiPYHsu"


META: dict[int, tuple] = {}


def collect():
    """依既有之批次序取全部 TC —— 其序即 TC ID 之序（R-SU5）。

    早期各批之 TC 不帶 `ts` 鍵（其 Test Set 為模組級常數 `TS`），
    故自模組取其 `TS` 補之 —— **不改既有生成器**（其為已提交之產物）。
    """
    out = []
    for m in MODS:
        mod = importlib.import_module(m)
        ts = getattr(mod, "TS", None) or getattr(mod, "TEST_SET", None)
        dm = getattr(mod, "A9", None)          # batch02a：其 `R` 欄取自 `下拉選單!$A$9`
        for t in mod.TCS:
            META[id(t)] = (ts, dm)
            out.append(t)
    return out


def dv_metrics(path):
    """資料驗證與 calcChain 之量（下放包 72 §五-4 之查證所加）。"""
    z = zipfile.ZipFile(path)
    names = z.namelist()
    dv = x14 = 0
    for n in names:
        if re.match(r"xl/worksheets/sheet\d+\.xml$", n):
            s = z.read(n).decode("utf8", "replace")
            dv += len(re.findall(r"<dataValidation ", s))
            x14 += len(re.findall(r"<x14:dataValidation ", s))
    return {"全簿 <dataValidation": dv, "全簿 <x14:dataValidation": x14,
            "calcChain.xml": int("xl/calcChain.xml" in names),
            "sharedStrings.xml": int("xl/sharedStrings.xml" in names)}


def main():
    src = FEAT / "inputs" / MASTER
    before = hashlib.sha256(src.read_bytes()).hexdigest()
    outdir = FEAT / "delivered"
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
        legal = None

    import openpyxl, warnings
    warnings.filterwarnings("ignore")
    wb = openpyxl.load_workbook(src, read_only=True, data_only=True)
    proj = str(wb[SHEET_NAME]["D2"].value).strip()
    legal = [str(wb["下拉選單"].cell(row=r, column=1).value) for r in range(1, 10)]

    global A9_FALLBACK
    A9_FALLBACK = legal[8]          # `下拉選單!$A$9`（batch02a 之值，R-SU40(a) 實測）
    tcs = collect()
    # R-BLM17（Pei 2026-08-27，bed_lowering 立，跨 feature 適用）：
    # 交付本依 `Requirement or Design ID`（D 欄）**升冪重排**，TC ID 隨列重指派。
    # 排序鍵以**數值**排（非字串）；同一 req_id 之多列維持其起草序（穩定排序），
    # 使一列之內的各 facet 不被打散。
    order = sorted(range(len(tcs)),
                   key=lambda i: (int(tcs[i]["req"].rsplit("-", 1)[1]), i))
    draft_pos = {id(tcs[i]): j + 1 for j, i in enumerate(range(len(tcs)))}
    tcs = [tcs[i] for i in order]
    rows = []
    row = HEADER_ROW + 1
    for i, t in enumerate(tcs, 1):
        tcid = f"{proj}-SU-{i:03d}"
        pre = t["pre"] if t["pre"] and re.match(r"^\d+\.", t["pre"][0]) else \
            [f"{k}. {s}" for k, s in enumerate(t["pre"], 1)]
        vals = {"D": t["req"], "F": tcid, "G": TEST_GROUP, "H": t.get("ts") or META[id(t)][0],
                "I": "\n".join(t["item"]), "J": "\n".join(pre),
                "K": "NA", "L": "\n".join(t["proc"]), "M": "\n".join(t["er"]),
                "N": t["spec"], "O": "NEW", "P": t["prio"], "R": t.get("dm") or META[id(t)][1] or A9_FALLBACK,
                "S": "NA", "AA": AUTHOR}
        sx = _set_row(sx, row, vals)
        rows.append((row, tcid, t["req"], vals["R"]))
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
    db, da = dv_metrics(src), dv_metrics(out)

    print("## T84c —— 全簿寫回之前後比對\n")
    print(f"- 來源（不動）：`inputs/…_20260817_ext.xlsx`")
    print(f"- 輸出：`delivered/…_SWUpdate_20260830.xlsx`")
    print(f"- sheet xml：`{sheet_path}`｜**寫入 {len(rows)} 列**"
          f"（列 {rows[0][0]}–{rows[-1][0]}）\n")

    print("### 一、48 部件與結構量（R-SU2 之基線）\n")
    print("| 量 | 母本 | 輸出 | 基線 | |")
    print("|---|---:|---:|---:|:--:|")
    ok = True
    for k in BASELINE:
        good = mb[k] == ma[k] == BASELINE[k]
        ok &= good
        print(f"| `{k}` | {mb[k]} | {ma[k]} | {BASELINE[k]} | {'✅' if good else '❌'} |")
    same = before == after
    ok &= same
    print(f"| **母本 SHA256 前後** | `{before[:12]}…` | `{after[:12]}…` | 未變 | "
          f"{'✅' if same else '❌'} |")

    print("\n### 二、資料驗證與 calcChain（**下放包 72 §五-4 之查證所加**）\n")
    print("| 量 | 母本 | 輸出 | |")
    print("|---|---:|---:|:--:|")
    for k in db:
        good = db[k] == da[k]
        ok &= good
        print(f"| `{k}` | {db[k]} | {da[k]} | {'✅' if good else '❌'} |")

    zi, zo2 = zipfile.ZipFile(src), zipfile.ZipFile(out)
    diff = [n for n in zi.namelist() if zi.read(n) != zo2.read(n)]
    print(f"\n### 三、逐部件 byte 比對\n")
    print(f"- **相異者 {len(diff)} / {len(zi.namelist())}**："
          + (", ".join(f"`{d}`" for d in diff) if diff else "無"))
    print(f"- 部件名稱與順序：**{'相同' if zi.namelist() == zo2.namelist() else '相異'}**")
    print(f"- **預期**：僅 `{sheet_path}` 一個部件相異（其為唯一被寫入者）")
    only_sheet = diff == [sheet_path]
    ok &= only_sheet
    print(f"- 實測：**{'相符 ✅' if only_sheet else '不符 ❌'}**")

    print(f"\n### 四、`R` 欄逐字元核對（R-SU40(a)）\n")
    dms = {d for _, _, _, d in rows}
    bad = dms - set(legal)
    print(f"- 本簿所用之 `design_method`：**{len(dms)} 種**")
    for d in sorted(dms):
        print(f"  - `{d}` —— {'✅ 逐字元見於 `下拉選單!$A$1:$A$9`' if d in legal else '❌ 不在清單'}")
    ok &= not bad
    sm = re.findall(r'<c r="R(\d+)"[^>]*t="inlineStr"><is><t[^>]*>([^<]*)</t>', sx)
    written_r = {v for _, v in sm}
    print(f"- 自輸出之 XML 反讀 `R` 欄之值：**{len(written_r)} 種**，"
          f"**{'與所用者相同 ✅' if written_r == dms else '與所用者相異 ❌'}**")
    ok &= (written_r == dms)

    print(f"\n**寫回結果：{'全部通過 ✅' if ok else '**不通過 ❌**'}**")
    print(f"\n> ⚠ **本比對不蘊含 Excel GUI 可開**（下放包 23 §四 3b 之人工項）——"
          f"`sxm` A-SX28 為「內容層全綠而 `R` 欄下拉遺失」之先例。**該人工項仍必要。**")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
