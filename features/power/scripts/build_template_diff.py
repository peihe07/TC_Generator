"""B1 — 範本全屬性比對（R-P79 / G56 / G57）。

R-P73 之結論僅及於 r9 標頭。本腳本比對其餘屬性：
資料驗證（含 x14 擴充）、分頁清單、合併儲存格、條件式格式、
欄寬與凍結窗格、公式。

**全程以 `zipfile` 直讀 `xl/*.xml`，完全不經 openpyxl 之寫入路徑，
不呼叫 `save()`**（11 §I；R-G3 記載 openpyxl + save 會破壞 rev C 之
R 欄 x14 dataValidation）。

用法：
    python features/power/scripts/build_template_diff.py
"""

from __future__ import annotations

import re
import zipfile
from pathlib import Path

import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

NS_MAIN = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
NS_X14 = "{http://schemas.microsoft.com/office/spreadsheetml/2009/9/main}"
NS_REL = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"

BOOKS = {
    "Power": (ROOT / "features/power/inputs/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
                     "STLA Test Case Specification & Result_SWQT_PowerManagement_20260816.xlsx",
              "Test Case Specification&Result"),
    "Comfort": (Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/"
                     "Climate Control Interface/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
                     "STLA Test Case Specification & Result_SWQT_Comfort_20260817.xlsx"),
                "Test Case Specification 測試用例規範"),
    "Privacy": (Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/"
                     "Privacy Mode/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
                     "STLA Test Case Specification & Result_SWQT_Privacy_20260813.xlsx"),
                "Test Case Specification 測試用例規範"),
}

# Power 之欄位語義對應（A-PW40，已由 R-P73 佐證）
POWER_COLUMNS = {
    "D": "req_id", "F": "tc_id", "G": "test_group", "H": "test_set", "I": "test_item",
    "J": "pre_conditions", "K": "input_test_data", "L": "test_procedure",
    "M": "expected_result", "N": "spec_reference", "O": "tc_ref_id",
    "P": "estimated_time(1)", "Q": "priority", "R": "estimated_time(2)",
    "S": "design_method", "T": "functional_safety",
    "U": "vehicle", "V": "vehicle", "W": "vehicle", "X": "vehicle",
    "Y": "vehicle", "Z": "vehicle", "AA": "vehicle",
    "AB": "author", "AI": "remarks",
}
COMFORT_COLUMNS = {
    "P": "priority", "Q": "estimated_time", "R": "design_method",
    "S": "functional_safety",
    "T": "vehicle", "U": "vehicle", "V": "vehicle", "W": "vehicle",
    "X": "vehicle", "Y": "vehicle", "Z": "vehicle",
    "AA": "author", "AH": "remarks",
}

COL_RE = re.compile(r"([A-Z]+)")


def sheet_part(zf: zipfile.ZipFile, sheet_name: str) -> str:
    """由 workbook.xml + rels 找出目標分頁之 XML part 路徑。"""
    wb = ET.fromstring(zf.read("xl/workbook.xml"))
    rels = ET.fromstring(zf.read("xl/_rels/workbook.xml.rels"))
    rid = None
    order = []
    for s in wb.iter(NS_MAIN + "sheet"):
        order.append((s.get("name"), s.get("state") or "visible"))
        if s.get("name") == sheet_name:
            rid = s.get(NS_REL + "id")
    target = next(r.get("Target") for r in rels.iter()
                  if r.get("Id") == rid)
    return ("xl/" + target.lstrip("/")).replace("xl/xl/", "xl/"), order


def cols_of(sqref: str) -> set[str]:
    return {m for ref in sqref.split() for m in COL_RE.findall(ref.split(":")[0])}


def probe(name: str, path: Path, sheet: str) -> dict:
    with zipfile.ZipFile(path) as zf:
        part, order = sheet_part(zf, sheet)
        xml = zf.read(part).decode("utf-8")
        root = ET.fromstring(xml)
        names = zf.namelist()

    dvs = []
    for dv in root.iter(NS_MAIN + "dataValidation"):
        f1 = dv.find(NS_MAIN + "formula1")
        dvs.append({"ns": "main", "sqref": dv.get("sqref") or "",
                    "type": dv.get("type") or "", "f1": (f1.text or "") if f1 is not None else ""})
    for dv in root.iter(NS_X14 + "dataValidation"):
        sq = dv.find("{http://schemas.microsoft.com/office/excel/2006/main}sqref")
        f1 = dv.find(NS_X14 + "formula1")
        text = "".join(f1.itertext()).strip() if f1 is not None else ""
        dvs.append({"ns": "x14", "sqref": (sq.text or "") if sq is not None else "",
                    "type": dv.get("type") or "", "f1": text})

    merges = [m.get("ref") for m in root.iter(NS_MAIN + "mergeCell")]
    cf = [(c.get("sqref"), [r.get("type") for r in c.iter(NS_MAIN + "cfRule")])
          for c in root.iter(NS_MAIN + "conditionalFormatting")]
    panes = [(p.get("topLeftCell"), p.get("state")) for p in root.iter(NS_MAIN + "pane")]
    widths = {c.get("min") + "-" + c.get("max"): c.get("width")
              for c in root.iter(NS_MAIN + "col")}
    formulas = [(c.get("r"), "".join(f.itertext()))
                for c in root.iter(NS_MAIN + "c")
                for f in c.iter(NS_MAIN + "f")]
    return {"part": part, "sheets": order, "dvs": dvs, "merges": merges,
            "cf": cf, "panes": panes, "widths": widths, "formulas": formulas,
            "parts": sorted(n for n in names if n.startswith("xl/"))}


def main() -> None:
    data = {n: probe(n, p, s) for n, (p, s) in BOOKS.items()}

    out = ["# B1 — 範本全屬性比對（R-P79 / G56 / G57）\n",
           "\n> 全程以 `zipfile` 直讀 `xl/*.xml`，**未經 openpyxl 寫入路徑、未呼叫 `save()`**"
           "（11 §I；R-G3）。\n",
           "> 產生指令：`python features/power/scripts/build_template_diff.py`\n"]

    # (a) DV
    out.append("\n## (a) 資料驗證（DV）—— G56\n")
    for n in BOOKS:
        d = data[n]
        out.append(f"\n### {n}（part `{d['part']}`，DV {len(d['dvs'])} 條）\n\n")
        if not d["dvs"]:
            out.append("（無 DV）\n")
            continue
        out.append("| ns | sqref | type | formula1 | 涵蓋欄 | 語義 |\n|---|---|---|---|---|---|\n")
        mapping = POWER_COLUMNS if n == "Power" else COMFORT_COLUMNS
        for dv in d["dvs"]:
            cols = sorted(cols_of(dv["sqref"]))
            sem = "、".join(sorted({mapping.get(c, f"?{c}") for c in cols})) or "—"
            out.append(f"| {dv['ns']} | `{dv['sqref']}` | {dv['type']} | "
                       f"`{dv['f1'][:46]}` | {', '.join(cols)} | **{sem}** |\n")

    # (b) 分頁
    out.append("\n## (b) 分頁清單 —— G57\n\n| # | Power | Comfort | Privacy |\n|---|---|---|---|\n")
    m = max(len(data[n]["sheets"]) for n in BOOKS)
    for i in range(m):
        row = []
        for n in BOOKS:
            s = data[n]["sheets"]
            row.append(f"`{s[i][0]}`" + ("（隱藏）" if i < len(s) and s[i][1] != "visible" else "")
                       if i < len(s) else "—")
        out.append(f"| {i+1} | {row[0]} | {row[1]} | {row[2]} |\n")

    # (c)-(f)
    for key, title in [("merges", "(c) 合併儲存格"), ("cf", "(d) 條件式格式"),
                       ("panes", "(e) 凍結窗格"), ("formulas", "(f) 公式")]:
        out.append(f"\n## {title} —— G57\n\n| feature | 筆數 | 內容（前 8 筆）|\n|---|---|---|\n")
        for n in BOOKS:
            v = data[n][key]
            out.append(f"| {n} | **{len(v)}** | `{str(v[:8])[:160]}` |\n")
    out.append("\n## (e2) 欄寬 —— G57\n\n| feature | 定義筆數 |\n|---|---|\n")
    for n in BOOKS:
        out.append(f"| {n} | {len(data[n]['widths'])} |\n")

    path = DATA / "b1_template_diff.md"
    path.write_text("".join(out), encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {path.stat().st_size} bytes\n")
    for n in BOOKS:
        d = data[n]
        print(f"{n:8} part={d['part']:28} DV={len(d['dvs'])} merges={len(d['merges'])} "
              f"cf={len(d['cf'])} panes={len(d['panes'])} formulas={len(d['formulas'])} "
              f"sheets={len(d['sheets'])}")
    print("\nG56 DV 明細：")
    for n in BOOKS:
        mapping = POWER_COLUMNS if n == "Power" else COMFORT_COLUMNS
        for dv in data[n]["dvs"]:
            cols = sorted(cols_of(dv["sqref"]))
            sem = "、".join(sorted({mapping.get(c, f"?{c}") for c in cols}))
            print(f"  {n:8} {dv['ns']:4} {dv['sqref']:24} {dv['type']:8} → {sem}")


if __name__ == "__main__":
    main()
