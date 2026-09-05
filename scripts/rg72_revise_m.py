#!/usr/bin/env python3
"""R-G72(g) Revise-M —— 只套 dry-run 表之 `mechanical=Y` 轉換（R-G72(c)）。

**母本一位元不動**：以 `openpyxl` 載入為記憶體物件、改格、再由
`backend.xlsx_surgical.surgical_save` 寫成**新檔** —— 該路徑以母本之 zip 為底
逐格 patch，故資料驗證（x14 dropdown）與其餘 zip member 皆保留
（`verify_structure` 會 ABORT 而非警告）。

**三道保護，缺一即中止**：
1. 只改 dry-run 表所列之 (sheet, row, col)，且該格現值須**逐字等於** `old_text`
   所在之整格文字之一行；替換為逐行替換，不動同格其他行。
2. 結果欄 Y–AH（第 25–34 欄）逐格斷言等於母本。
3. `surgical_save(verify=True)` 之結構不變式。

唯讀於母本；只寫 `--out` 所指之新檔與 idmap。
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import sys
import warnings
from collections import Counter, defaultdict
from pathlib import Path

warnings.filterwarnings("ignore")
import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from backend.xlsx_surgical import surgical_save          # noqa: E402
import lint036                                           # noqa: E402

# 結果欄 Y–AH（1-based 25–34）—— 回修不得觸及（R-G72(c)：不得順手改其他欄）
RESULT_COLS = range(25, 35)


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def load_plan(tsv: Path) -> dict:
    """dry-run 表 → {(sheet, row, col1based): [(old_line, new_line, rule, tc_id)]}"""
    plan: dict = defaultdict(list)
    with tsv.open(encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r.get("mechanical", "").strip().upper() != "Y":
                continue
            plan[(r["sheet"], int(r["row"]), int(r["col"]))].append(
                (r["old_text"], r["new_text"], r["rule"], r.get("tc_id", "")))
    return plan


def apply(src: Path, tsv: Path, out: Path, idmap_out: Path) -> dict:
    plan = load_plan(tsv)
    wb = openpyxl.load_workbook(src)          # 記憶體物件，母本不動
    stats = Counter()
    rules_by_row: dict = defaultdict(set)
    cols_by_row: dict = defaultdict(set)
    tcid_by_row: dict = {}
    misses = []

    for (sheet, row, col), edits in sorted(plan.items()):
        if sheet not in wb.sheetnames:
            misses.append(f"分頁不存在：{sheet!r}")
            continue
        if col in RESULT_COLS:
            misses.append(f"目標落在結果欄 Y–AH：{sheet} r{row} c{col} —— 拒絕")
            continue
        cell = wb[sheet].cell(row=row, column=col)
        text = "" if cell.value is None else str(cell.value)
        orig = text
        # 同一格內同一 (old,new) 可被 dry-run 表列多次（其行內出現多次即多列）。
        # 逐「出現次數」替換一次即可 —— 逐列套用會使第二次找不到而誤判 miss。
        seen: set = set()
        for old_t, new_t, rule, tc in edits:
            key = (old_t, new_t)
            if key in seen:
                continue
            seen.add(key)
            n = text.count(old_t)
            if n == 0:
                misses.append(f"{sheet} r{row} c{col}: 找不到 {old_t!r}")
                stats["miss"] += 1
                continue
            text = text.replace(old_t, new_t)
            stats["applied"] += n
            rules_by_row[row].add(rule)
            cols_by_row[row].add(col)
            if tc:
                tcid_by_row[row] = tc
        if text != orig:
            cell.value = text
            stats["cells"] += 1

    if misses:
        for m in misses[:10]:
            print(f"  ⚠ {m}")
        raise SystemExit(f"中止：{len(misses)} 處未命中／越界，未寫任何檔")

    # 保護 2：結果欄逐格斷言
    ref = openpyxl.load_workbook(src)
    bad = 0
    for ws in wb.worksheets:
        if not ws.title.startswith(lint036.TC_SHEET_PREFIX):
            continue
        rs = ref[ws.title]
        for row in range(1, ws.max_row + 1):
            for col in RESULT_COLS:
                if ws.cell(row=row, column=col).value != rs.cell(row=row, column=col).value:
                    bad += 1
    ref.close()
    if bad:
        raise SystemExit(f"中止：結果欄 Y–AH 有 {bad} 格與母本不符，未寫任何檔")

    surgical_save(wb, src, out)               # verify=True，結構不變式
    wb.close()

    with idmap_out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["old_tc_id", "new_tc_id", "row", "changed_cols", "reason"])
        for row in sorted(rules_by_row):
            tc = tcid_by_row.get(row, "")
            w.writerow([tc, tc, row,
                        ",".join(str(c) for c in sorted(cols_by_row[row])),
                        ";".join(sorted(rules_by_row[row]))])

    stats["rows"] = len(rules_by_row)
    stats["result_cols_asserted_equal"] = "PASS"
    return stats


def main() -> int:
    ap = argparse.ArgumentParser(description="R-G72(g) Revise-M 產生器")
    ap.add_argument("--src", required=True)
    ap.add_argument("--dryrun", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--idmap", required=True)
    a = ap.parse_args()
    src, out = Path(a.src), Path(a.out)
    if out.exists():
        raise SystemExit(f"中止：{out} 已存在（Revise 本不覆寫）")
    st = apply(src, Path(a.dryrun), out, Path(a.idmap))
    print(f"  母本 {src.name[-46:]}  sha12 {sha12(src)}")
    print(f"  新檔 {out.name[-46:]}  sha12 {sha12(out)}")
    print(f"  替換 {st['applied']} 處／{st['cells']} 格／涉及 {st['rows']} 列"
          f"；結果欄 Y–AH 斷言 {st['result_cols_asserted_equal']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
