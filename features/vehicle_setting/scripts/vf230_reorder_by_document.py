"""VF230：457 列之**再重排** —— 依「**037 分報告（文件）→ 該文件內之編號**」。

**其為 W-VF92 之更正，非其延續。** W-VF92 依 `R-G32` 之字面
（「family 名依字母序，數字尾碼依數值序」）以 **D 欄整字串**為鍵，
**而該鍵之模型為假**：

    `SWE1-VC-BlindSpotAlert-002`  之 `-002` **不是「BlindSpotAlert 的第 2 條」**，
    **是該條在其 037 分報告內之行號**。實測：11 份分報告，
    每一份之編號皆自 **002** 起跑至該份長度（如 `Trailer_Name - Max_Power_Level`
    131 條為 002–138）。上游列號與之平行遞增：

        SYS-RA-VF230_V1-672 | SWE1-VC-BlindSpotAlert-002
        SYS-RA-VF230_V1-673 | SWE1-VC-BlindSpotAlert-003
        SYS-RA-VF230_V1-679 | SWE1-VC-PassiveEntry-009   ← 同一份文件，編號接著跑

**故 `BlindSpotAlert` 與 `PassiveEntry` 為同一份文件內之相鄰需求，
而依名字排序把它們拆到 B 區與 P 區去了。**
**實測其後果**：11 份文件被切成 **74 段**（平均每份散在 6.7 處），
**文件內編號之逆序 43 處**。

**Pei 之指正（2026-08-25）**：「同一份文件的排在一起照數字順序去排」。

---

**排序鍵（二層）**：

    第一層  **文件名**（`data/vf230_leaves.tsv` 之 `family` 欄，即 037 分報告）
            **字母序（ASCII，大寫先於小寫）** —— Pei 於選項預覽中所擇之序，
            其一處可注意：`STLA_SWITCH_1_Type…` 排在 `STLA_Suspension…` **之前**
            （`W` < `u`）。若欲不分大小寫，改 `DOC_KEY` 一處即可。
    第二層  **該條之編號**（`swe_id` 之結尾數字，**不論有無連字號**）
            —— 17 條之連字號缺漏為 `DR-29` 之標的，本檔以
            `(\\d+)$` 取之故不受影響。
    stable sort —— 同鍵者保持前一輪之相對序。

**B 欄**依重排後之位置全部重寫，**自實測起點（244）連續** ——
`R-VF83`／`V73 §1`，**不自 001 起**。

---

**對照表為三段式** —— 本輪為第二次重排，**若只記本輪則第一次之舊 B 斷鏈**：

    data/vf230_id_remap.tsv
      b_orig    W-VF92 之前（量產原序，pilot／DR／隔離表所引者）
      b_wvf92   W-VF92 之後（依 D 字串排；曾短暫送達交付路徑）
      b_final   本輪之後（依 文件 → 編號）
      req_id    D 欄

---

**工法與閘沿用 `vf230_wvf92_reorder.py`**（直接 import 其函式，不複製）：
XML 手術式、openpyxl 不存檔、`xlsx_surgical.verify_structure` 為結構不變式。

**新增一閘**（取代 W-VF92 之「D 欄非降序」，其於本鍵下不再成立）：
    **逐列之 (文件, 編號) 非降序，且每一份文件恰一段** —— 違者即停。
"""
from __future__ import annotations

import collections
import csv
import re
import shutil
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
REPO = FEAT.parents[1]
sys.path.insert(0, str(REPO))
sys.path.insert(0, str(FEAT / "scripts"))
from backend import xlsx_surgical as SURG            # noqa: E402
import vf230_wvf77_dryrun as DRY                     # noqa: E402
import vf230_wvf84_writeback as WB                   # noqa: E402  probe_x14
import vf230_wvf92_reorder as R1                     # noqa: E402  復用其工法與閘

LEAVES = FEAT / "data/vf230_leaves.tsv"
REMAP = FEAT / "data/vf230_id_remap.tsv"
BACKUP = FEAT / "inputs/_vf230_036_docsort_backup.xlsx"

# **文件名之字母序** —— Pei 所擇（ASCII）。不分大小寫者改為 `s.lower()`。
def DOC_KEY(s: str) -> str:
    return s


def leaf_doc() -> dict[str, str]:
    """`swe_id` → 其 037 分報告名。**單一權威為 `vf230_leaves.tsv`。**"""
    return {r["swe_id"]: r["family"]
            for r in csv.DictReader(LEAVES.open(encoding="utf-8"), delimiter="\t")}


def tail_num(s: str) -> int:
    """結尾數字，**不論有無連字號** —— `…-002` 與 `…140` 皆取之（DR-29）。"""
    m = re.search(r"(\d+)$", s)
    if not m:
        raise SystemExit(f"ID 無結尾數字，排序鍵不成立：{s} —— 停")
    return int(m.group(1))


def plan(book: Path) -> tuple[list[dict], int, dict[str, str]]:
    import openpyxl
    from openpyxl.utils import column_index_from_string as ci

    doc = leaf_doc()
    wb = openpyxl.load_workbook(book, read_only=True, data_only=True)
    ws = wb[DRY.SHEET]
    rows = []
    for row in ws.iter_rows(min_row=DRY.FIRST_DATA_ROW):
        b, d = row[1].value, row[3].value
        if b in (None, "") or d in (None, ""):
            continue
        rows.append({"row": row[0].row, "B": int(b), "D": str(d)})
    wb.close()

    # ---- 閘 0 ----
    missing = sorted({r["D"] for r in rows} - doc.keys())
    if missing:
        raise SystemExit(f"D 於 `vf230_leaves.tsv` 查無者 {len(missing)}："
                         f"{missing[:3]} —— 文件歸屬不明，停")
    bs = sorted(r["B"] for r in rows)
    if bs != list(range(bs[0], bs[-1] + 1)):
        raise SystemExit("B 欄非連號，停")
    span = [r["row"] for r in rows]
    if span != list(range(span[0], span[-1] + 1)):
        raise SystemExit("資料列不連續，停")
    for r in rows:
        r["doc"], r["num"] = doc[r["D"]], tail_num(r["D"])

    # **文件內編號不得重複**（同一 D 之拆列除外）——
    # 其若重複，「照編號排」即無定序。
    dup = []
    for k, v in collections.Counter((r["doc"], r["num"]) for r in rows).items():
        if v > 1:
            ds = {r["D"] for r in rows if (r["doc"], r["num"]) == k}
            if len(ds) > 1:
                dup.append((k, sorted(ds)))
    print(f"[閘 0] 資料列 **{len(rows)}**（列 {span[0]}–{span[-1]}）｜"
          f"B {bs[0]}–{bs[-1]} 連號｜文件 **{len({r['doc'] for r in rows})}** 份")
    print(f"       文件內編號撞號而 ID 相異者：**{len(dup)}**")
    if dup:
        raise SystemExit(f"文件內編號撞號：{dup[:2]} —— 排序無定序，停")

    order = sorted(rows, key=lambda r: (DOC_KEY(r["doc"]), r["num"]))
    return order, bs[0], doc


def segs(seq) -> int:
    n, prev = 0, object()
    for v in seq:
        if v != prev:
            n += 1
        prev = v
    return n


def write_remap(order: list[dict], b_start: int) -> tuple[int, int]:
    """三段式對照表 —— **b_orig 自現存之 remap 接續，不得只記本輪。**"""
    prev = {}
    if REMAP.exists():
        for r in csv.DictReader(REMAP.open(encoding="utf-8"), delimiter="\t"):
            if "b_wvf92" in r:                       # 本檔已跑過一次，取其 b_orig
                prev[int(r["b_wvf92"])] = int(r["b_orig"])
            else:                                    # W-VF92 之二欄表
                prev[int(r["new_b"])] = int(r["old_b"])
    if prev and set(prev) != {r["B"] for r in order}:
        raise SystemExit("現存對照表之 new_b 與工作簿之 B 不吻合 —— 鏈已斷，停")
    lines = ["b_orig\tb_wvf92\tb_final\treq_id"]
    for i, r in enumerate(order):
        lines.append(f"{prev.get(r['B'], r['B'])}\t{r['B']}\t{b_start + i}\t{r['D']}")
    REMAP.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return len(order), len(prev)


def main() -> None:
    write = "--write" in sys.argv
    book = DRY.book()
    part = R1.sheet_part(book)
    print("=== VF230 再重排：文件 → 編號（Pei 裁定 2026-08-25）===")
    print(f"目標：{book.name[:58]}…\n分頁 part：{part}"
          f"{'' if write else '   【空跑，未加 --write】'}\n")

    before = R1.snapshot(book)
    prof_before = R1.parts_profile(book)
    order, b_start, doc = plan(book)
    print(f"       B 之起點取 **{b_start}**（R-VF83／V73 §1，不自 001 起）")

    cur = sorted(before)
    d_by_b = {b: before[b]["D"] for b in cur}
    docs_now = [doc[d_by_b[b]] for b in cur]
    nums_now = collections.defaultdict(list)
    for b in cur:
        nums_now[doc[d_by_b[b]]].append(tail_num(d_by_b[b]))
    inv_now = sum(sum(1 for i in range(len(v) - 1) if v[i] > v[i + 1])
                  for v in nums_now.values())
    print(f"\n[量測] **重排前**：文件段數 **{segs(docs_now)}**"
          f"（{len(set(docs_now))} 份 → 平均散在 {segs(docs_now)/len(set(docs_now)):.1f} 處）"
          f"｜文件內編號逆序 **{inv_now}** 處")
    docs_new = [r["doc"] for r in order]
    nums_new = collections.defaultdict(list)
    for r in order:
        nums_new[r["doc"]].append(r["num"])
    inv_new = sum(sum(1 for i in range(len(v) - 1) if v[i] > v[i + 1])
                  for v in nums_new.values())
    print(f"       **重排後**：文件段數 **{segs(docs_new)}**"
          f"（= 份數即每份恰一段）｜文件內編號逆序 **{inv_new}** 處")
    print("\n       文件之序（本輪所採，字母序）：")
    for i, d in enumerate(dict.fromkeys(docs_new)):
        print(f"         {i+1:2}. {len(nums_new[d]):3} 條  {d[:60]}")

    if not write:
        print("\n**空跑結束，未動任何檔。** 加 --write 施行。")
        return

    n_rows, n_prev = write_remap(order, b_start)
    print(f"\n[對照] {REMAP.name}：**{n_rows} 列**（三段式）｜"
          f"自現存表接續之 b_orig **{n_prev}** 筆")

    shutil.copy2(book, BACKUP)
    print(f"[備份] 本輪重排前之本 → {BACKUP.name}")
    R1.surgery(book, order, b_start, part)

    # ---- 閘 3 ----
    rep = SURG.verify_structure(BACKUP, book, {part})
    print("\n[閘 3a] xlsx_surgical.verify_structure：**通過**")
    print(f"        part 總數 {rep['members']}｜"
          f"內容相異之 part {len(rep['differing'])}：{rep['differing']}")
    prof_after = R1.parts_profile(book)
    bad = [k for k in prof_before if prof_before[k] != prof_after[k]]
    print(f"[閘 3b] part 級對帳：{'**全一致**' if not bad else f'**不一致 {bad}**'}"
          f"（dv {prof_after['dataValidation']}｜x14 {prof_after['x14:dataValidation']}"
          f"｜cf {prof_after['conditionalFormatting']}｜probe {WB.probe_x14(book)}）")
    if bad:
        raise SystemExit(f"part 級對帳不一致：{bad} —— 停")

    # ---- 閘 4 ----
    after = R1.snapshot(book)
    diff = []
    for i, r in enumerate(order):
        newb = b_start + i
        got = after.get(newb)
        if got is None:
            diff.append((newb, "整列缺"))
            continue
        old = before[r["B"]]
        for c in DRY.COLS:
            if c != "B" and old[c].strip() != got[c].strip():
                diff.append((newb, c))
    print(f"[閘 4] 重讀比對 **{len(after)} 列 × {len(DRY.COLS)} 欄**（B 除外）："
          f"差異 **{len(diff)}**")
    for d in diff[:6]:
        print(f"       新 B{d[0]} 欄 {d[1]}")
    if diff or len(after) != len(before):
        raise SystemExit("重讀比對有差異，停")

    # ---- 新閘：(文件, 編號) 非降序 ＋ 每份文件恰一段 ----
    seq = [(DOC_KEY(doc[after[b]["D"]]), tail_num(after[b]["D"]))
           for b in sorted(after)]
    viol = [i for i in range(len(seq) - 1) if seq[i] > seq[i + 1]]
    ds = [doc[after[b]["D"]] for b in sorted(after)]
    print(f"[新閘] (文件, 編號) 逐列非降序：違者 **{len(viol)}**｜"
          f"文件段數 **{segs(ds)}** vs 份數 **{len(set(ds))}**")
    if viol or segs(ds) != len(set(ds)):
        for i in viol[:5]:
            print(f"       位置 {i}：{seq[i]} > {seq[i+1]}")
        raise SystemExit("排序不變式不成立，停")
    print(f"[新閘] B 欄連號：{min(after)}–{max(after)}｜"
          f"{sorted(after) == list(range(min(after), max(after) + 1))}")

    print("\n" + "=" * 66)
    print("**R-VF112／R-VF116：以下為 Pei 之動作**")
    print("  1. 以 Excel 開啟並確認下拉與版面")
    print("  2. 逐字具名檔名複製至交付路徑 VF230_V1_R5/")
    print("     （交付路徑現存者為 W-VF92 之本，**須以本輪之本覆蓋**）")
    print("=" * 66)


if __name__ == "__main__":
    main()
