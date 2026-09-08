#!/usr/bin/env python3
"""VS-CF-04 —— CFTS044 交付：封面／記錄封面頁補欄 ＋ 檔案搬移 ＋ MANIFEST。

來源：`docs/fw036/handoff/down/20260908_VS-CF-04.md`（Pei 裁「出貨」2026-09-08）。

輸入 `sandbox/cfts044/cfts044_20260819_Revise2.xlsx`（sha256 949fa81e…），
**`Test Case Specification 測試用例規範` 分頁一格不動**；只寫
`Cover 封面`（sheet3）與 `Product Document 記錄封面頁`（sheet5）四格。
`ChangeHistory 修訂履歷`（sheet4）依 §一.2 **不寫**。

落檔一律 `backend.xlsx_surgical.surgical_save()`，全域無 `wb.save()`（R16／R-G3）。
"""

from __future__ import annotations

import csv
import shutil
import subprocess
import sys
import warnings
import zipfile
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "backend"))
from xlsx_surgical import surgical_save  # noqa: E402

warnings.filterwarnings("ignore")

FEAT = ROOT / "features/vehicle_setting"
SRC = FEAT / "sandbox/cfts044/cfts044_20260819_Revise2.xlsx"
SRC_SHA = "949fa81e4cd5a5a4b193357de23410ae79b5322f584682189b647d98f71c9db4"
STAGE = FEAT / "sandbox/cfts044/_vs_cf04_stage.xlsx"

MASTER_DIR = Path("/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/"
                  "ASW-R2/Vehicle Settings/CFTS044")
DELIVER_NAME = ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
                "Specification & Result_SWQT_CFTS044_Vehicle Controls_"
                "20260908.xlsx")
OUT_DIR = FEAT / "output"
DELIVERED = FEAT / "delivered"
REMAP_SRC = FEAT / "reports/cfts044_tcid_remap.tsv"
REMAP_DST = DELIVERED / "cfts044_tcid_remap_20260908.tsv"

TC_SHEET = "Test Case Specification 測試用例規範"
COVER = "Cover 封面"
PRODDOC = "Product Document 記錄封面頁"
CHANGEHIST = "ChangeHistory 修訂履歷"

AUTHOR = "PeiPYHsu"
REV_DATE = "2026-09-08"

# §一 之四格。位址皆由合併範圍實測而定（見上繳 §2）。
EDITS = {
    COVER: {"D9": AUTHOR,        # 作者 Author（D9:F9 合併，值欄）
            "G9": REV_DATE},     # 修訂日期之值欄（G6:H6 為欄頭，G9:H9 為作者列）
    PRODDOC: {"B8": REV_DATE,    # 日期 Date（B8:D8 合併）
              "C13": AUTHOR},    # 作者 Author（V1.0 列）
}


def sha256(p: Path) -> str:
    return subprocess.run(["shasum", "-a", "256", str(p)],
                          capture_output=True, text=True,
                          check=True).stdout.split()[0]


def sheet_map(p: Path) -> dict[str, str]:
    """分頁名 -> zip member，經 workbook.xml.rels 解析（不臆測編號）。"""
    import re
    z = zipfile.ZipFile(p)
    rels = z.read("xl/_rels/workbook.xml.rels").decode()
    rid = {m.group(1): m.group(2) for m in
           re.finditer(r'Id="([^"]+)"[^>]*Target="([^"]+)"', rels)}
    out = {}
    for m in re.finditer(r'<sheet[^>]*name="([^"]+)"[^>]*r:id="([^"]+)"',
                         z.read("xl/workbook.xml").decode()):
        out[m.group(1)] = "xl/" + rid[m.group(2)].lstrip("/")
    return out


def merged_of(ws, coord: str) -> str:
    for rng in ws.merged_cells.ranges:
        if coord in rng:
            return str(rng)
    return "(未合併)"


def main() -> int:
    assert SRC.exists(), f"來源不存在：{SRC}"
    got = sha256(SRC)
    assert got == SRC_SHA, f"Revise2 sha256 {got} ≠ 下放包所載，停手"

    # ---- 檔名式：先讀母本目錄確認（§2.1）
    masters = sorted(p.name for p in MASTER_DIR.glob("*.xlsx"))
    assert len(masters) == 1, f"母本目錄命中 {len(masters)} 個 xlsx，停手：{masters}"
    assert masters[0] == DELIVER_NAME.replace("20260908", "20260819"), (
        f"交付檔名與母本命名式不符：\n  母本 {masters[0]}\n  交付 {DELIVER_NAME}")

    # ---- delivered/ 是否受版控（§2.2）
    probe = subprocess.run(
        ["git", "check-ignore", "-v", str(DELIVERED / DELIVER_NAME)],
        cwd=ROOT, capture_output=True, text=True)
    assert probe.returncode != 0, (
        f"delivered/ 被 gitignore 命中，停手：{probe.stdout.strip()}")

    smap = sheet_map(SRC)
    print("分頁 → zip member（workbook.xml.rels 實測）")
    for k in (COVER, CHANGEHIST, PRODDOC, TC_SHEET):
        print(f"  {k:34} {smap[k]}")

    # ---- 補欄
    shutil.copy2(SRC, STAGE)
    wb = openpyxl.load_workbook(STAGE)
    print("\n合併範圍實測（§一.1 之 ⚠）")
    for sheet, cells in EDITS.items():
        ws = wb[sheet]
        for coord, val in cells.items():
            before = ws[coord].value
            print(f"  {sheet} {coord:4} merged={merged_of(ws, coord):10} "
                  f"before={before!r} -> {val!r}")
            assert before in (None, ""), f"{sheet}!{coord} 非空（{before!r}），停手"
            ws[coord] = val
    out_path = OUT_DIR / DELIVER_NAME
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    report = surgical_save(wb, STAGE, out_path)
    STAGE.unlink()

    # ---- §三 驗證
    print("\n== §三 交付前最後驗證 ==")
    za, zb = zipfile.ZipFile(SRC), zipfile.ZipFile(out_path)
    na, nb = set(za.namelist()), set(zb.namelist())
    assert na == nb, f"zip member 集合相異：{na ^ nb}"
    differing = sorted(n for n in na if za.read(n) != zb.read(n))
    want = sorted({smap[COVER], smap[PRODDOC]})
    print(f"  1. member 數 {len(na)} → {len(nb)}；相異 {differing}")
    assert len(na) == 42, f"member 數 {len(na)} ≠ 42"
    assert differing == want, f"相異 member 應僅 {want}，實得 {differing}"
    for tag, member in (("sheet6/TC", smap[TC_SHEET]),
                        ("sheet4/ChangeHistory", smap[CHANGEHIST])):
        assert za.read(member) == zb.read(member), f"{tag} xml 有 diff，停手"
        print(f"     {tag} xml diff = 0")
    dv_a = za.read(smap[TC_SHEET]).decode().count("<dataValidation ")
    dv_b = zb.read(smap[TC_SHEET]).decode().count("<dataValidation ")
    assert dv_a == dv_b, f"dv 計數 {dv_a} → {dv_b}"
    print(f"     dataValidation {dv_a} → {dv_b}")

    wa = openpyxl.load_workbook(SRC)[TC_SHEET]
    wbk = openpyxl.load_workbook(out_path)
    wbn = wbk[TC_SHEET]
    diff = [(r, c) for r in range(1, wa.max_row + 1)
            for c in range(1, 35) if wa.cell(r, c).value != wbn.cell(r, c).value]
    assert not diff, f"TC 分頁有 {len(diff)} 格相異，停手：{diff[:5]}"
    print(f"  2. TC 分頁逐格 diff = 0（{wa.max_row} × 34）")

    import re
    data = [r for r in range(10, wbn.max_row + 1)
            if str(wbn.cell(r, 6).value or "").strip()]
    blob = lambda r: "\n".join(str(wbn.cell(r, c).value or "")
                               for c in (9, 10, 11, 12, 13, 34))
    reqs = {str(wbn.cell(r, 4).value).strip() for r in data}
    nums = {
        "資料列": len(data),
        "Requirement": len(reqs),
        "未生成": sum(1 for r in data if not str(wbn.cell(r, 9).value or "").strip()),
        "PENDING": sum(1 for r in data if "PENDING" in blob(r)),
        "BLOCKED/撤回 DR": sum(1 for r in data if "BLOCKED" in blob(r) or any(
            x in blob(r) for x in ("DR-15", "DR-21", "DR-24", "DR-25",
                                   "DR-26", "DR-18", "DR-22"))),
        "IMPL_GAP": sum(1 for r in data if "IMPL_GAP" in blob(r)),
    }
    ids = [str(wbn.cell(r, 6).value) for r in data]
    nums["tc_id 連續"] = ids == [f"NR1L-VehicleSetting-{i:03d}"
                                for i in range(1, len(data) + 1)]
    print(f"  3. §〇 七項：{nums}")
    assert nums == {"資料列": 241, "Requirement": 237, "未生成": 0, "PENDING": 0,
                    "BLOCKED/撤回 DR": 0, "IMPL_GAP": 0, "tc_id 連續": True}, \
        "§〇 七項數字有變，停手"

    # ---- 搬移
    DELIVERED.mkdir(parents=True, exist_ok=True)
    del_path = DELIVERED / DELIVER_NAME
    shutil.copy2(out_path, del_path)
    shutil.copy2(REMAP_SRC, REMAP_DST)
    s_out, s_del = sha256(out_path), sha256(del_path)
    assert s_out == s_del, "output/ 與 delivered/ 之 sha 不同，停手"
    print(f"  4. output/ 與 delivered/ sha256 相同：{s_out}")

    # ---- MANIFEST
    rel_src = str(SRC.relative_to(ROOT))
    out_row = [DELIVER_NAME, s_out, rel_src, "VS-CF-04", "delivered",
               "CFTS044 v1；241 列／237 Req；PENDING 0；封面與履歷補齊後之 sha"]
    del_row = [DELIVER_NAME, s_del, rel_src, "VS-CF-04",
               "CFTS044 Vehicle Controls v1；甲-1 採甲案（9 組 19 列並存）；"
               "DR-5-B 39 列為 dr_dependent"]
    remap_row = [REMAP_DST.name, sha256(REMAP_DST),
                 str(REMAP_SRC.relative_to(ROOT)), "VS-CF-04",
                 "TestRail 匯入用；刪 2 重複列後之舊→新 tc_id 對照（243 列）"]
    lines = {}
    for path, rows in ((OUT_DIR / "MANIFEST.tsv", [out_row]),
                       (DELIVERED / "MANIFEST.tsv", [del_row, remap_row])):
        n0 = sum(1 for _ in open(path, encoding="utf-8"))
        with open(path, "a", encoding="utf-8", newline="") as f:
            csv.writer(f, delimiter="\t", lineterminator="\n").writerows(rows)
        lines[str(path.relative_to(ROOT))] = (n0 + 1, n0 + len(rows))

    print("\n== 產出 ==")
    print(f"  surgical_save: {report}")
    print(f"  {out_path.relative_to(ROOT)}")
    print(f"  {del_path.relative_to(ROOT)}")
    print(f"  {REMAP_DST.relative_to(ROOT)}")
    for p, (a, b) in lines.items():
        print(f"  MANIFEST {p} 追加行號 {a}" + (f"–{b}" if b > a else ""))
    print(f"\n  Revise2 sha256（來源，未動） {sha256(SRC)}")
    print(f"  交付本 sha256               {s_out}")
    assert sha256(SRC) == SRC_SHA, "來源 sha 改變，停手"
    return 0


if __name__ == "__main__":
    sys.exit(main())
