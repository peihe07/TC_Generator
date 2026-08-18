#!/usr/bin/env python3
"""寫回工作簿（42 包作業 2）。**本輪不得產出交付件** —— 見 §未決 1 之閘。

## 三條硬約束（41 包 §二，本檔逐條落實）

1. **不呼叫 `diff_cells()`。** 走「直接給定 edits → `patch_sheet_xml` →
   逐 member 複寫」。實測：`diff_cells` 對本母本之 TC 分頁逾 100 秒未完成，
   封裝路徑 0.04 秒。**我方本就知道要寫哪些格 —— 求差異是在解一個我們沒有的問題。**
2. **母本永不被寫入。** 讀 `inputs/…_ext.xlsx`（SHA 6372fb6b…，
   `BASELINE.sha256` 保護），寫 `output/` 之新檔。
3. **寫回後必跑 `verify_dv_integrity`**，四項全綠，任一不綠即不留下檔案。

## 未決 1 之閘（42 包 §一）

T:Z 七個車型欄之填值**無依據**：填了是編造，不填則該七欄不在 DV 涵蓋內。
**故 `--write` 在 `--vehicle-columns` 未給定時拒絕執行**，
且該拒絕**不是可用旗標關掉的**（沒有 `--force`）。
`--self-test` 寫的是 scratchpad 之暫存檔，不落 `output/`，不入台帳 ——
**那是驗證本程式，不是產出交付件**。

## 參數化之四項（42 包 §一之處置）

| 參數 | 預設 | 依據 |
|---|---|---|
| `vehicle_columns` | `None` → **T:Z 不寫入** | 未決 1，待 Pei |
| `author_value` | `None` → **AA 不寫入** | Comfort 交付件實測 AA 為空（未決 3 之同類） |
| `tc_ref_id_value` | `None` → **O 不寫入** | 同上，Comfort 實測 O 為空 |
| `row_order` | `"req_id"` | Comfort 96 §1（Pei 裁定）：列序依 leaf id 遞增 |

**`row_order` 之預設與我 41 輪之設計草案不同**（草案寫 `tc_id` 序）——
理由與其代價見上繳 42 §2.3，**已具名待確認**。

Usage:
    python3 scripts/write_back.py                      # dry-run（預設）
    python3 scripts/write_back.py --self-test          # 方向性案例（scratchpad）
    python3 scripts/write_back.py --write --vehicle-columns '{"T":"1"}'
"""

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from backend.xlsx_surgical import (patch_sheet_xml,            # noqa: E402
                                   sheet_members, col_to_idx)
import verify_dv_integrity as DV                               # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
SRC = FEATURE / "inputs" / ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
                            "STLA Test Case Specification & Result_SWQT_"
                            "20260817_ext.xlsx")
SRC_SHA = "6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2"
SHEET = "Test Case Specification 測試用例規範"
FIRST_ROW = 10
CAPACITY_LAST_ROW = 1411          # B 欄公式與各 DV 之實測上界

# feature.yaml §workbook.columns（rev C；本輪以 header 探測複驗）
COLS = {
    "D": "req_id", "F": "tc_id", "G": "test_group", "H": "test_set",
    "I": "test_item", "J": "pre_conditions", "K": "input_test_data",
    "L": "test_procedure", "M": "expected_result",
    "N": "specification_reference", "P": "priority", "R": "design_method",
    "S": "functional_safety", "AH": "remarks",
}
# 一律不寫。**逐欄之理由見上繳 42 §2.2** —— 此處只留一句最要緊的：
# B 帶母本自己的序號公式（shared formula），寫入即破壞其共用主格。
NEVER_WRITE = ["B", "C", "E", "Q", "T", "U", "V", "W", "X", "Y", "Z",
               "AB", "AC", "AD", "AE", "AF", "AG"]
# 條件寫入 —— 其值由參數給定，未給定即不寫
OPTIONAL = {"O": "tc_ref_id_value", "AA": "author_value"}

LEAF_KEY = re.compile(r"SWE1-HMI-PROF-(\d+)(?:-(\d+))?(?:-([a-z]+))?$")


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def records() -> list:
    out = []
    for p in sorted((FEATURE / "generated").glob("*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for t in d["tcs"]:
            out.append(t)
    return out


def _leaf_sort(tc: dict):
    m = LEAF_KEY.search(tc["req_id"])
    if not m:
        return (999, 999, "", tc["tc_id"])
    # 同一 leaf 之多條（`-neg` 等）以 tc_id 續其後
    return (int(m.group(1)), int(m.group(2) or 0), m.group(3) or "",
            tc["tc_id"])


def order(tcs: list, row_order: str) -> list:
    if row_order == "req_id":
        return sorted(tcs, key=_leaf_sort)
    if row_order == "tc_id":
        return sorted(tcs, key=lambda t: t["tc_id"])
    raise SystemExit(f"未知之 row_order：{row_order}")


def build_edits(tcs: list, *, vehicle_columns=None, author_value=None,
                tc_ref_id_value=None, row_order="req_id") -> dict:
    """`{(row, col_idx): value}` —— **不經 `diff_cells`**。"""
    plan = order(tcs, row_order)
    if FIRST_ROW + len(plan) - 1 > CAPACITY_LAST_ROW:
        raise SystemExit(f"{len(plan)} 條超出範本容量（末列 "
                         f"{CAPACITY_LAST_ROW}）")
    opts = {"tc_ref_id_value": tc_ref_id_value, "author_value": author_value}
    edits = {}
    for i, tc in enumerate(plan):
        r = FIRST_ROW + i
        for col, field in COLS.items():
            edits[(r, col_to_idx(col))] = tc.get(field, "")
        for col, key in OPTIONAL.items():
            if opts[key] is not None:
                edits[(r, col_to_idx(col))] = opts[key]
        for col, val in (vehicle_columns or {}).items():
            edits[(r, col_to_idx(col))] = val
    return edits


def splice(src: Path, out: Path, edits: dict) -> None:
    import zipfile
    member = sheet_members(src)[SHEET]
    with zipfile.ZipFile(src) as zin:
        patched = patch_sheet_xml(zin.read(member).decode("utf-8"), edits)
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
            for info in zin.infolist():
                data = (patched.encode("utf-8") if info.filename == member
                        else zin.read(info.filename))
                zout.writestr(info, data)


# ─────────────────────────────────────────────── 寫回後之檢查（六項）

def verify(src: Path, out: Path, n_rows: int) -> list:
    """違規清單（空 ＝ 綠）。**任一不綠即不留下檔案。**"""
    import zipfile
    bad = []

    # WB-1～WB-4 —— DV 完整性（`verify_dv_integrity` 之四項）
    bad += [f"WB-DV {x}" for x in DV.verify(src, out)]

    # WB-5 —— 每一寫入列須落在 R 欄 x14 DV 與 P 欄 DV 之涵蓋範圍內
    #         （Comfort write_back §3.3 之同型；**與 DV 完整性互補**：
    #          前者問「DV 還在嗎」，本項問「它蓋得到我寫的列嗎」）
    member = sheet_members(out)[SHEET]
    with zipfile.ZipFile(out) as z:
        xml = z.read(member).decode("utf-8")

    def cover(sqrefs):
        rows = set()
        for sq in sqrefs:
            for part in sq.split():
                m = re.match(r"([A-Z]+)(\d+)(?::([A-Z]+)(\d+))?$", part)
                if m:
                    rows |= set(range(int(m.group(2)),
                                      int(m.group(4) or m.group(2)) + 1))
        return rows

    written = set(range(FIRST_ROW, FIRST_ROW + n_rows))
    r_rows = cover(re.findall(r"<xm:sqref>([^<]+)</xm:sqref>", xml))
    p_rows = cover([m for m in re.findall(
        r'<dataValidation[^>]*sqref="([^"]+)"', xml) if m.startswith("P")])
    for name, got in (("R 欄 design_method（x14）", r_rows),
                      ("P 欄 priority", p_rows)):
        miss = sorted(written - got)
        if miss:
            bad.append(f"WB-5 {len(miss)} 列不在 {name} 之 DV 涵蓋範圍內"
                       f"（首列 {miss[0]}）")

    # WB-6 —— 換行字元：**LF only**（未決 5 之自裁，寫成可測形式）
    #
    # **判準改過一次（首跑即誤報）。** v1 掃整份 sheet XML，
    # 而母本之 XML 宣告行本身就以 `?>\r\n<worksheet` 結尾 ——
    # 那是**檔案之序列化格式**，不是儲存格內容。v1 遂對一次正確之寫回轉紅。
    # v2 只掃 `<t>` 內之文字（即儲存格值）。
    for txt in re.findall(r"<t[^>]*>(.*?)</t>", xml, re.S):
        if "&#13;" in txt or "\r" in txt:
            bad.append("WB-6 儲存格內容出現 CR —— 多行欄位須為 LF（`\\n`）")
            break
    return bad


# ─────────────────────────────────────────────── 產出（受未決 1 之閘）

def write(out: Path, *, vehicle_columns=None, **kw) -> Path:
    if vehicle_columns is None:
        raise SystemExit(
            "拒絕產出：**未決 1（T:Z 七個車型欄）尚無依據**。\n"
            "  填了是編造，不填則該七欄不在 DV 涵蓋內而 WB-5 會紅。\n"
            "  依 42 包 §一，該項送 Pei；得依據後以 --vehicle-columns 給定。\n"
            "  本閘無 --force —— 可以用旗標關掉的閘不是閘。")
    if sha256(SRC) != SRC_SHA:
        raise SystemExit(f"來源母本之 SHA 不符：{sha256(SRC)[:16]}…")
    tcs = records()
    edits = build_edits(tcs, vehicle_columns=vehicle_columns, **kw)
    out.parent.mkdir(parents=True, exist_ok=True)
    tmp = out.with_suffix(".tmp.xlsx")
    splice(SRC, tmp, edits)
    bad = verify(SRC, tmp, len(tcs))
    if bad:
        tmp.unlink()
        for b in bad:
            print(f"  {b}")
        raise SystemExit(f"寫回後檢查 {len(bad)} 項不綠 —— **未留下檔案**")
    tmp.rename(out)
    return out


def dry_run(row_order="req_id") -> int:
    tcs = records()
    plan = order(tcs, row_order)
    edits = build_edits(tcs, row_order=row_order)
    print(f"來源 {SRC.name}")
    print(f"  SHA {'相符' if sha256(SRC) == SRC_SHA else '**不符**'}"
          f"（{SRC_SHA[:16]}…）")
    print(f"\nTC {len(tcs)} 條 → row {FIRST_ROW}–{FIRST_ROW + len(tcs) - 1}"
          f"（容量末列 {CAPACITY_LAST_ROW}，餘裕 "
          f"{CAPACITY_LAST_ROW - FIRST_ROW - len(tcs) + 1} 列）")
    print(f"列序：{row_order}；首三列 "
          f"{[t['req_id'] for t in plan[:3]]} … 末列 {plan[-1]['req_id']}")
    print(f"\n寫入欄 {len(COLS)}：{' '.join(COLS)}")
    print(f"不寫入欄 {len(NEVER_WRITE)}：{' '.join(NEVER_WRITE)}")
    print(f"條件欄（未給值即不寫）：{' '.join(OPTIONAL)}")
    print(f"\nedits 共 {len(edits)} 格")
    print("\n**未產出檔案** —— 未決 1 未定前，`--write` 拒絕執行。")
    return 0


def self_test() -> int:
    """方向性案例 —— 全程寫 scratchpad，**不落 `output/`、不入台帳**。"""
    scratch = DV.SCRATCH.parent / "writeback"
    scratch.mkdir(parents=True, exist_ok=True)
    tcs = records()
    ok, cases = True, []

    def case(name, fn, expect_red, note=""):
        nonlocal ok
        cases.append(name)
        bad = fn()
        good = bool(bad) == expect_red
        ok &= good
        print(f"  {'PASS' if good else '**FAIL**'} — {name}："
              f"{'紅' if bad else '綠'}，期望 {'紅' if expect_red else '綠'}")
        if note:
            print(f"      note {note}")
        for b in bad[:2]:
            print(f"      └ {b}")

    # ① 正常寫回（T:Z 不寫）→ 六項全綠
    out = scratch / "probe_default.xlsx"
    splice(SRC, out, build_edits(tcs))
    case("預設參數（T:Z／O／AA 皆不寫）→ 綠", lambda: verify(SRC, out, len(tcs)),
         False, f"{len(tcs)} 列，row {FIRST_ROW}–{FIRST_ROW + len(tcs) - 1}")

    # ② 給定 vehicle_columns → 仍綠（參數化未破壞任何檢查）
    out2 = scratch / "probe_vehicles.xlsx"
    splice(SRC, out2, build_edits(tcs, vehicle_columns={"T": "1", "U": "0"}))
    case("給定 `vehicle_columns` → 綠（參數化不改變任何檢查）",
         lambda: verify(SRC, out2, len(tcs)), False)

    # ③ 注入向 —— 寫到 DV 涵蓋範圍之外
    out3 = scratch / "probe_beyond_dv.xlsx"
    ed = {(CAPACITY_LAST_ROW + 5, col_to_idx("R")): "功能測試 (Functional "
          "based ; no specific technique)"}
    splice(SRC, out3, ed)
    case("**注入：寫到 DV 涵蓋範圍之外（row 1416）→ 紅**",
         lambda: verify(SRC, out3, CAPACITY_LAST_ROW + 5 - FIRST_ROW + 1),
         True)

    # ④ 注入向 —— 以 openpyxl 存回（A-UP09 之形態）
    out4 = scratch / "probe_openpyxl.xlsx"
    import openpyxl
    wb = openpyxl.load_workbook(SRC)
    wb.save(out4)
    wb.close()
    case("**注入：以 openpyxl 存回 → 紅**（DV 完整性）",
         lambda: verify(SRC, out4, len(tcs)), True)

    # ⑤ 注入向 —— 多行欄位含 CRLF
    out5 = scratch / "probe_crlf.xlsx"
    splice(SRC, out5, {(FIRST_ROW, col_to_idx("J")): "1. a\r\n2. b"})
    case("**注入：多行欄位以 CRLF 寫入 → 紅**（未決 5 之 LF 自裁）",
         lambda: verify(SRC, out5, 1), True)

    # ⑥ 產出之閘 —— `--write` 而未給 vehicle_columns
    def refuses():
        try:
            write(scratch / "must_not_exist.xlsx")
        except SystemExit as e:
            return [str(e).splitlines()[0]]
        return []
    case("**未決 1 之閘：`--write` 未給 `vehicle_columns` → 拒絕產出**",
         refuses, True)
    assert not (scratch / "must_not_exist.xlsx").exists()

    # ⑦ 護欄 —— 列序兩種皆為全排列且不重不漏
    def order_total():
        bad = []
        for ro in ("req_id", "tc_id"):
            p = order(tcs, ro)
            if len(p) != len(tcs) or {t["tc_id"] for t in p} != \
                    {t["tc_id"] for t in tcs}:
                bad.append(f"row_order={ro} 非全排列")
        return bad
    case("**護欄**：`row_order` 兩種皆為全排列（不重不漏）→ 綠",
         order_total, False)

    n = len(cases)
    print(f"\n{n if ok else '<' + str(n)} / {n} directional cases "
          f"{'PASS' if ok else 'FAIL'}")
    print(f"\n（全程寫 scratchpad `{scratch}`；"
          f"`output/` 未產生任何檔案，台帳未記帳）")
    return 0 if ok else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--vehicle-columns", default=None,
                    help='JSON，如 \'{"T":"1","U":"0"}\'')
    ap.add_argument("--row-order", default="req_id",
                    choices=["req_id", "tc_id"])
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    if a.self_test:
        sys.exit(self_test())
    if not a.write:
        sys.exit(dry_run(a.row_order))
    vc = json.loads(a.vehicle_columns) if a.vehicle_columns else None
    out = Path(a.out) if a.out else (FEATURE / "output" / (
        "FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
        "Specification & Result_SWQT_UserProfiles_full.xlsx"))
    print("寫出", write(out, vehicle_columns=vc, row_order=a.row_order))
