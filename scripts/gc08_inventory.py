#!/usr/bin/env python3
"""GC-08 盤點：已交付本之 R-G70／R-G71 合規現況（唯讀，只量不改）。

每本一列。「建議」欄只准三值（審閱 §四）：
  `無需回修`         —— 各項數字皆 0
  `機械轉換可回修`   —— 只有 R-G70/71 之機械項
  `需 Pei 內容裁決`  —— 含不可機械決定者（ER 收尾時機、PROXI 之 R-VS86 衝突、
                        HMI 標籤 vs VF 名）
判準寫在輸出之 `判準` 欄，**不留給讀者推測**。
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
import rg70_dryrun as dry

RE_V3 = re.compile(r"\$[A-Z][A-Z0-9_]{2,}\.[A-Za-z][A-Za-z0-9_]*\$")
RE_SEND_CAN = re.compile(r"\bSend CAN:")
RE_PROXI_OLD = re.compile(r"\bPROXI\s+[A-Za-z]")      # 無 `$` —— SWC／R-VS86 式
RE_PROXI_NEW = re.compile(r"\bPROXI\s+\$")            # R-G70(e) 式


def sha12(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:12]


def measure(path: Path) -> dict:
    c = Counter()
    rows = set()
    fields = {}
    for sheet, row, col, ln in dry.scan(path):
        rows.add((sheet, row))
        fields.setdefault((sheet, row), {}).setdefault(col, []).append(ln)
        c["v3"] += len(RE_V3.findall(ln))
        c["send_can"] += len(RE_SEND_CAN.findall(ln))
        c["proxi_old"] += len(RE_PROXI_OLD.findall(ln))
        c["proxi_new"] += len(RE_PROXI_NEW.findall(ln))
        klass, rule, _ = dry.classify(ln)
        if klass != "no_change":
            c[klass] += 1
    # lint X（導航路徑）：以整列為範圍，重用 lint036 之判準
    x = 0
    for (sheet, row), cols in fields.items():
        pre = "\n".join(cols.get("pre", []))
        proc = "\n".join(cols.get("proc", []))
        if lint036.RE_X_ENTRY.search(pre + "\n" + proc):
            continue
        for ln in proc.split("\n"):
            if lint036.RE_X_PENDING.search(ln):
                continue
            if lint036.RE_X_TARGET.search(ln):
                x += 1
    c["X"] = x
    c["rows"] = len(rows)
    return c


def advise(c: Counter) -> tuple[str, str]:
    # 列 0 ＝ 空模板／已清空之工作本，不是「已合規」——不得記為無需回修（G-D）。
    if c["rows"] == 0:
        return "不適用", "TC 分頁 0 資料列（空模板或已清空）"
    if c["needs_ruling"] == 0 and c["mechanical"] == 0 and c["X"] == 0:
        return "無需回修", "v3 式 0、待裁項 0、X 0"
    reasons = []
    if c["needs_ruling"]:
        reasons.append(f"待裁 {c['needs_ruling']}")
    if c["proxi_old"]:
        reasons.append(f"PROXI 舊式 {c['proxi_old']} 行（R-VS86 vs R-G70(e) 未裁）")
    if c["X"]:
        reasons.append(f"X {c['X']} 行（§5.8 無固定入口；改寫須 HMI 來源，查無者開 DR）")
    if reasons:
        return "需 Pei 內容裁決", "；".join(reasons)
    return "機械轉換可回修", f"只有 R-G70 機械項 {c['mechanical']} 行"


def main() -> int:
    ap = argparse.ArgumentParser(description="GC-08 盤點（唯讀）")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["本", "路徑", "sha12", "資料列", "v3式", "SendCAN:",
                    "PROXI舊式", "PROXI新式", "機械項", "待裁項", "lintX",
                    "建議", "判準"])
        for f in sorted(args.files):
            p = Path(f)
            try:
                c = measure(p)
            except Exception as e:                     # 無 TC 分頁等
                w.writerow([p.name, f, sha12(p), "", "", "", "", "", "", "",
                            "", "不適用", f"讀取失敗：{e}"])
                continue
            a, why = advise(c)
            w.writerow([p.name[:60], f, sha12(p), c["rows"], c["v3"],
                        c["send_can"], c["proxi_old"], c["proxi_new"],
                        c["mechanical"], c["needs_ruling"], c["X"], a, why])
            print(f"{a:<16} {p.name[-46:]:<48} 列{c['rows']:>4} v3={c['v3']:<5} "
                  f"機械={c['mechanical']:<5} 待裁={c['needs_ruling']:<5} X={c['X']}")
    print(f"\n寫入 {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
