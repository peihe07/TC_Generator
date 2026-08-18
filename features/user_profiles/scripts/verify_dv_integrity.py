#!/usr/bin/env python3
"""A-UP09 之 x14 dataValidation 完整性閘（R-U14 之解除條件，40 包作業 4）。

## R-U14 逐字要求

> 解除條件 = **機器檢查存在且實跑**：對產出檔驗 x14:dataValidation 節點數與
> zip member 集合，比對來源母本（可借 Comfort write_back §3.3 之同型
> assertion）。**該 gate 立起並實跑前，本 feature 之寫回實作不得開工。**

「文字修補不算」是這條裁定的重心 —— 故本檔之價值不在它存在，
而在 `--self-test` 之**注入向確實轉紅**。只貼綠的那一次不予採認。

## 借自 Comfort 者，與不借者

Comfort `features/comfort/scripts/write_back.py` §3.3 之 assertion 問的是
**「每一寫入列是否落在 DV 之涵蓋範圍內」** —— 那是**列 × 範圍**之覆蓋檢查，
其前提是 DV 還在。**A-UP09 之損壞形態不同**：DV 整個節點消失，
於是 `_cover()` 得到空集合、`min(r_rows)` 直接 ValueError ——
**壞得很大聲，但不是這條閘該說的那句話**。

本檔補的是它的前提：**DV 節點是否仍在、其範圍是否仍是原範圍**。
兩者互補，不重複。

## 四項比對（皆逐 worksheet member，非全檔加總）

| # | 項 | 為什麼不能省 |
|---|---|---|
| 1 | zip member 集合相同 | A-UP09 實測 48→47（`xl/worksheets/sheet6.xml` 之 extLst 連帶之部件） |
| 2 | `x14:dataValidation` 節點數相同 | **A-UP09 之本體**：1→0 |
| 3 | `xm:sqref` 之範圍字串相同 | 節點還在而範圍被縮成 `R10:R100` —— 第 2 項全綠，而下拉在第 101 列起失效 |
| 4 | legacy `dataValidation` 節點數相同 | A-UP09 中這三條**存活** —— 只驗它們的閘會對該缺陷全綠（canon §5a-11） |

第 3 項是本檔對 R-U14 逐字要求之**逾額**：裁定只寫「節點數與 member 集合」。
逾額之理由具名於此 —— 節點數守不住範圍，而**範圍失效之交付件與 DV 消失之
交付件，對使用者是同一件事**（第 101 列起沒有下拉可選）。

Usage:
    python3 scripts/verify_dv_integrity.py <produced.xlsx> [--src <master>]
    python3 scripts/verify_dv_integrity.py --self-test
"""

import argparse
import re
import shutil
import sys
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
FEATURE = Path(__file__).resolve().parent.parent
MASTER = next((REPO / "forms").glob("*_SWQT_*_ext.xlsx"))
SCRATCH = Path("/private/tmp/claude-501/-Users-peihe-Work-Projects-TC-Generator/"
               "ba79bc8b-693f-42f0-8b38-fcabad6a3ee9/scratchpad/dvgate")

X14_DV = re.compile(r"<x14:dataValidation[ >]")
LEGACY_DV = re.compile(r"<dataValidation[ >]")
SQREF = re.compile(r"<xm:sqref>([^<]+)</xm:sqref>")
SHEET = re.compile(r"^xl/worksheets/sheet\d+\.xml$")


def profile(path: Path) -> dict:
    """一個 xlsx 之 DV 指紋。**只讀，不解析成 openpyxl 物件**。

    以 openpyxl 讀取本身即會丟棄 x14 擴充（A-UP09 之成因），
    故本檔全程停在 zip ＋ 原始 XML 這一層。
    """
    out = {"members": set(), "x14": {}, "legacy": {}, "sqref": {}}
    with zipfile.ZipFile(path) as z:
        out["members"] = set(z.namelist())
        for m in sorted(out["members"]):
            if not SHEET.match(m):
                continue
            xml = z.read(m).decode("utf-8", errors="ignore")
            out["x14"][m] = len(X14_DV.findall(xml))
            out["legacy"][m] = len(LEGACY_DV.findall(xml))
            out["sqref"][m] = sorted(SQREF.findall(xml))
    return out


def verify(src: Path, out_path: Path) -> list:
    """違規清單（空 ＝ 綠）。"""
    a, b = profile(src), profile(out_path)
    bad = []

    lost = sorted(a["members"] - b["members"])
    added = sorted(b["members"] - a["members"])
    if lost or added:
        bad.append(f"DV-1 zip member 集合改變：少 {lost}／多 {added}"
                   f"（母本 {len(a['members'])} → 產出 {len(b['members'])}）")

    for m in sorted(a["x14"]):
        want, got = a["x14"][m], b["x14"].get(m)
        if got is None:
            continue                    # 已由 DV-1 報告
        if want != got:
            bad.append(f"DV-2 {m}：x14:dataValidation 節點數 {want} → {got}"
                       f"（A-UP09 之形態）")

    for m in sorted(a["sqref"]):
        want, got = a["sqref"][m], b["sqref"].get(m, [])
        if want != got:
            bad.append(f"DV-3 {m}：xm:sqref 範圍改變 {want} → {got}")

    for m in sorted(a["legacy"]):
        want, got = a["legacy"][m], b["legacy"].get(m)
        if got is None:
            continue
        if want != got:
            bad.append(f"DV-4 {m}：legacy dataValidation 節點數 {want} → {got}")
    return bad


def _report(src: Path, out_path: Path) -> int:
    p = profile(src)
    tot = sum(p["x14"].values())
    print(f"母本 {src.name}")
    print(f"產出 {out_path.name}")
    print(f"  zip members {len(p['members'])}；x14 DV 節點 {tot}；"
          f"其範圍 {[s for v in p['sqref'].values() for s in v]}")
    bad = verify(src, out_path)
    print(f"\n違規 {len(bad)}")
    for x in bad:
        print(f"  {x}")
    return 1 if bad else 0


# ─────────────────────────────────────────────────────── 方向性案例（R-G7）

def self_test() -> int:
    import openpyxl                                     # noqa: F401
    sys.path.insert(0, str(REPO))
    from backend.xlsx_surgical import (patch_sheet_xml, sheet_members,
                                       copy_unchanged)

    def splice(out_path: Path, edits: dict) -> None:
        """`xlsx_surgical` 之 splice —— **不經 `surgical_save`**。

        `surgical_save()` 先 `diff_cells()` 兩本 openpyxl 工作簿以求出變動格。
        對本母本之 `Test Case Specification` 分頁（1411 × 34，B 欄為
        **shared formula**），該比對在本機**逾 100 秒仍未完成**（實測，
        其餘八個分頁各 < 0.1 秒）—— 成因為 openpyxl 對 shared formula 之
        逐格展開。**此為 Phase 6 寫回實作之已知效能事項，已記於上繳。**

        本閘所要驗的是**splice 之封裝方式保不保得住 x14 DV**，
        而封裝由 `patch_sheet_xml()` ＋ 逐 member 複寫決定，
        與變動格如何求得無關。故直接給定 edits，跳過 `diff_cells`——
        **受檢之程式路徑不變**。
        """
        member = sheet_members(src)["Test Case Specification 測試用例規範"]
        with zipfile.ZipFile(src) as zin:
            patched = patch_sheet_xml(
                zin.read(member).decode("utf-8"), edits)
            with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zout:
                for info in zin.infolist():
                    data = (patched.encode("utf-8")
                            if info.filename == member
                            else zin.read(info.filename))
                    zout.writestr(info, data)

    SCRATCH.mkdir(parents=True, exist_ok=True)
    src = SCRATCH / "master_copy.xlsx"
    shutil.copy(MASTER, src)          # **母本本身全程不被寫入**
    ok, n = True, 0

    def case(name, out_path, expect_red, note=""):
        nonlocal ok, n
        n += 1
        bad = verify(src, out_path)
        good = bool(bad) == expect_red
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}："
              f"{'紅' if bad else '綠'}，期望 {'紅' if expect_red else '綠'}")
        if note:
            print(f"      note {note}")
        for x in bad[:3]:
            print(f"      └ {x}")

    print("## 注入向（R-G7）—— 該壞的必須被抓到\n")

    # ① openpyxl load → save：A-UP09 之原始形態
    inj = SCRATCH / "openpyxl_saved.xlsx"
    wb = openpyxl.load_workbook(src)
    wb.save(inj)
    wb.close()
    pa, pb = profile(src), profile(inj)
    case("openpyxl `load_workbook()` → `save()`", inj, True,
         f"members {len(pa['members'])}→{len(pb['members'])}；"
         f"x14 節點 {sum(pa['x14'].values())}→{sum(pb['x14'].values())}")

    # ② 節點還在而**範圍被縮小** —— 第 2 項全綠，第 3 項須紅
    shrunk = SCRATCH / "sqref_shrunk.xlsx"
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(
            shrunk, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            data = zin.read(info.filename)
            if info.filename == "xl/worksheets/sheet6.xml":
                xml = data.decode("utf-8")
                xml = re.sub(r"<xm:sqref>R10:R\d+</xm:sqref>",
                             "<xm:sqref>R10:R100</xm:sqref>", xml)
                data = xml.encode("utf-8")
            zout.writestr(info, data)
    only23 = [x for x in verify(src, shrunk) if x.startswith("DV-2")]
    case("x14 節點保留而 `xm:sqref` 由 R10:R1411 縮為 R10:R100", shrunk, True,
         f"DV-2（節點數）命中 {len(only23)} 處 —— **節點數守不住範圍**，"
         f"此即第 3 項存在之理由")

    # ③ 移除一個 zip member（模擬重封裝掉件）
    dropped = SCRATCH / "member_dropped.xlsx"
    with zipfile.ZipFile(src) as zin, zipfile.ZipFile(
            dropped, "w", zipfile.ZIP_DEFLATED) as zout:
        for info in zin.infolist():
            if info.filename == "xl/worksheets/sheet9.xml":
                continue              # 下拉選單來源表
            zout.writestr(info, zin.read(info.filename))
    case("重封裝時掉了 `下拉選單` 之 sheet9.xml", dropped, True)

    print("\n## 對照向 —— 該綠的不得被誤殺\n")

    # ④ xlsx_surgical splice 一格（**R-U14 所指之正當寫回途徑**）
    spliced = SCRATCH / "surgical_spliced.xlsx"
    splice(spliced, {(12, 4): "DV gate 對照向之寫入（scratchpad 複本，非交付）"})
    case("`xlsx_surgical` splice 一格（D12）", spliced, False,
         "patched member xl/worksheets/sheet6.xml")

    # ⑤ 多列寫入 —— 範圍向（R-G9）：合法之寫回不得轉紅
    #    **刻意寫 R 欄**（design_method）—— 那正是 A-UP09 所摧毀之下拉所在欄。
    many = SCRATCH / "surgical_many.xlsx"
    edits = {}
    for r in range(12, 42):
        edits[(r, 4)] = f"row {r}"
        edits[(r, 18)] = "功能測試 (Functional based ; no specific technique)"
    splice(many, edits)
    case("splice 30 列（含 R 欄 design_method）—— 合法寫回", many, False,
         "R-G9 之範圍向：閘不得對它所要保護的那個動作轉紅")

    # ⑥ 逐位元組複本
    same = SCRATCH / "byte_copy.xlsx"
    copy_unchanged(src, same)
    case("`copy_unchanged` 逐位元組複本", same, False)

    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"\n（全程於 scratchpad 之母本複本上進行；"
          f"`forms/` 之母本與 `inputs/` 複本未被寫入）")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("produced", nargs="?", help="產出之 xlsx")
    ap.add_argument("--src", default=str(MASTER), help="來源母本")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    if not a.produced:
        ap.error("須給產出檔，或用 --self-test")
    sys.exit(_report(Path(a.src), Path(a.produced)))
