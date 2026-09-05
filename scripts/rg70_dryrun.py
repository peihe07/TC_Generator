#!/usr/bin/env python3
"""R-G70（R-1 v4）之轉換 dry-run 與 GC-08 盤點（唯讀，永不寫工作簿）。

v3 → v4 之轉換為**機械替換**，但不是每一行都機械 —— 本工具把每一行分類為
`mechanical`（新文字可自動產生）或 `needs_ruling`（須人裁），
**兩類分開計數**，不把後者混進「可轉換」之數（R-G50：可轉換是全稱斷言）。

輸出 TSV 逐列一行：`file / sheet / row / col / klass / rule / old_text / new_text`。
`new_text` 於 `needs_ruling` 時為空 —— **空欄不是「無需改」，是「本層不決定」**。
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
import warnings
from collections import Counter
from pathlib import Path

warnings.filterwarnings("ignore")
import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import lint036

# --- v3 → v4 之機械式 ---------------------------------------------------------
# 每條：(規則名, 樣式, 取代式)。`$MSG.Sig$` 一律去 `$`（R-G70(c)(d)：訊號名不加 `$`）。
SIG = r"\$(?P<msg>[A-Z][A-Z0-9_]{2,}\.[A-Za-z][A-Za-z0-9_]*)\$"

MECHANICAL: list[tuple[str, re.Pattern, str]] = [
    # (c) CAN 送出
    ("c-send", re.compile(rf"Send the signal\s+{SIG}"), r"Send CAN: \g<msg>"),
    # (d) Procedure 讀取
    ("d-read", re.compile(rf"Read the signal\s+{SIG}"), r"Read \g<msg>"),
    # (d) ER 觀察：`The signal value $X$ = …` → `X = …`
    ("d-er-value", re.compile(rf"The signal value\s+{SIG}"), r"\g<msg>"),
    # ER 送出確認：`The signal $X$ = … is registered…` → `X = … is registered…`
    ("d-er-signal", re.compile(rf"The signal\s+{SIG}"), r"\g<msg>"),
    # 其餘裸露之 `$MSG.Sig$`（觸發式等）
    ("sig-bare", re.compile(SIG), r"\g<msg>"),
]

# `is received` 為 v3 之收尾語；v4(d) 之 ER 收尾為 `is sent <時機>`。
# **時機無法自動產生**，故凡命中者判 needs_ruling。
RE_IS_RECEIVED = re.compile(r"\bis received\b")
# PROXI：R-G70(e) 與 vehicle_setting 之 R-VS86 相衝（GC-08 §留痕），一律不自動轉。
RE_PROXI = re.compile(r"\bPROXI\b")


def classify(line: str) -> tuple[str, str, str]:
    """回傳 (klass, rule, new_text)。"""
    if RE_PROXI.search(line):
        return "needs_ruling", "proxi-R-G70(e)-vs-R-VS86", ""
    if not re.search(SIG, line) and "Send the signal" not in line:
        return "no_change", "", ""
    if RE_IS_RECEIVED.search(line):
        return "needs_ruling", "er-tail-is-received→is sent <時機>", ""
    new, rules = line, []
    for name, pat, rep in MECHANICAL:
        new2 = pat.sub(rep, new)
        if new2 != new:
            rules.append(name)
            new = new2
    if new == line:
        return "no_change", "", ""
    return "mechanical", "+".join(rules), new


def scan(path: Path):
    wb = openpyxl.load_workbook(path, data_only=True)
    for ws in wb.worksheets:
        if not ws.title.startswith(lint036.TC_SHEET_PREFIX):
            continue
        rows = list(ws.iter_rows(values_only=True))
        hr = lint036.find_header_row(ws)
        cols = lint036.build_column_map(list(rows[hr - 1]))
        # 資料列之判準取 `lint036.lint_sheet` 之判準（test_item／proc／er 任一非空），
        # **不用** GC-07 下放包 §一之「`No.#` 非空」——後者非通用：
        # BedLowering 0902 與 VehicleCategory 0902 之 `No.#` 欄整欄為空，
        # 以其為判準會把整本讀成 0 列（GC-08 實測）。
        for off, raw in enumerate(rows[hr:], start=hr + 1):
            def _cell(key: str) -> str:
                i = cols.get(key)
                return "" if i is None or i >= len(raw) or raw[i] is None else str(raw[i])
            if not any(_cell(k).strip() for k in ("test_item", "proc", "er")):
                continue
            for key in lint036.P_FIELDS:
                i = cols.get(key)
                if i is None or i >= len(raw) or raw[i] is None:
                    continue
                for ln in str(raw[i]).split("\n"):
                    if not ln.strip():
                        continue
                    yield ws.title, off, key, ln
    wb.close()


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def main() -> int:
    ap = argparse.ArgumentParser(description="R-G70 轉換 dry-run（唯讀）")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", required=True, help="輸出 tsv")
    args = ap.parse_args()

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    tally: dict[str, Counter] = {}
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["file", "sha12", "sheet", "row", "col", "klass", "rule",
                    "old_text", "new_text"])
        for f in args.files:
            p = Path(f)
            s = sha12(p)
            c = tally.setdefault(p.name, Counter())
            for sheet, row, col, ln in scan(p):
                klass, rule, new = classify(ln)
                if klass == "no_change":
                    continue
                c[klass] += 1
                c[f"rule:{rule}"] += 1
                w.writerow([p.name, s, sheet, row, col, klass, rule, ln, new])
    for name, c in tally.items():
        print(f"{name}")
        print(f"  mechanical   {c['mechanical']}")
        print(f"  needs_ruling {c['needs_ruling']}")
        for k, v in sorted(c.items()):
            if k.startswith("rule:"):
                print(f"    {v:>5}  {k[5:]}")
    print(f"\n寫入 {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
