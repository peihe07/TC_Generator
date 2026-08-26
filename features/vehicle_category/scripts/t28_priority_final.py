#!/usr/bin/env python3
"""T28 —— priority 定案版（R-VC13 + R-VC14）。

本腳本**不重做判定** —— 本地預判沿用 T24 之 `LOCAL` 字典（自
`t24_priority_draft.py` 匯入，不複製一份，避免二處各改其一）。
本輪只做兩件事：

  1. **R-VC13** —— 上游約束由 leaf 級改為**章級**：
       037 = High 之章 → 該章 leaf 群中至少一筆定案為 P1 或 P0
       037 = Low  之章 → 該章不得有定案高於 P3 者
       037 = Medium    → 不設約束
     章不滿足時**不得逐筆抬升以求滿足** —— 停並回報（本腳本以
     非零離開碼終止，不自行修補）。
  2. **R-VC14** —— data-loss 之攔阻失效 (a) 為 P0、執行失效 (b) 為 P1。
     即時適用：`SWE1-HMI-VC-036-01` 由 P0 改判 P1。

輸出：`data/priority_final.tsv` ＋ 異動對照 ＋ 章級驗算表。
不寫入任何 TC 欄位。
"""
import csv
import importlib.util
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
A03 = ROOT / "inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1 STLA 報告.xlsx"

_spec = importlib.util.spec_from_file_location(
    "t24", Path(__file__).with_name("t24_priority_draft.py"))
_t24 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_t24)          # 匯入時會重出 T24 之草案，無副作用
LOCAL = _t24.LOCAL
RANK = _t24.RANK

# R-VC14 之即時適用。鍵為 req_id，值為 (新級, 依據)。
RVC14 = {
    "SWE1-HMI-VC-036-01": (
        "P1",
        "R-VC14(b) 執行失效：該清而未清，資料仍在，非 data-loss；"
        "隱私外洩風險依 R-VC11(c) 記於 reasoning"),
}

wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
raw = list(wb["Analysis Report"].iter_rows(values_only=True))
data = [r for r in raw[7:] if r[0] not in (None, "")]
P = re.compile(r"^SWE1-HMI-VC-(\d{3})$")
C = re.compile(r"^SWE1-HMI-VC-(\d{3})-(\d{2})$")
ids = [str(r[0]).strip() for r in data]
pc = {C.match(i).group(1) for i in ids if C.match(i)}
leaves = {i for i in ids
          if C.match(i) or (P.match(i) and P.match(i).group(1) not in pc)}

rows = []
for r in data:
    rid = str(r[0]).strip()
    if rid not in leaves:
        continue
    sec = str(r[2]).split("\n")[0].strip().rsplit("_", 1)[-1]
    ch = int(sec.split(".")[0])
    up = str(r[17]).strip()
    local, why = LOCAL[rid]
    final, note = local, ""
    if rid in RVC14:
        final, note = RVC14[rid]
    rows.append({"req_id": rid, "section": sec, "chapter": ch,
                 "upstream": up, "local_p": local, "final_p": final,
                 "note": note, "basis": why,
                 "title": str(r[3]).strip()})

# ---- R-VC13：章級驗算
by_ch = defaultdict(list)
for x in rows:
    by_ch[x["chapter"]].append(x)

print("R-VC13 章級約束驗算")
print(f"{'章':>3} {'037':>7} {'leaf':>5}  定案分布                 約束      判")
violations = []
for ch in sorted(by_ch):
    grp = by_ch[ch]
    up = grp[0]["upstream"]
    dist = Counter(x["final_p"] for x in grp)
    if up == "High":
        ok = any(RANK[x["final_p"]] <= RANK["P1"] for x in grp)
        rule = "至少一筆 ≥P1"
    elif up == "Low":
        ok = all(RANK[x["final_p"]] >= RANK["P3"] for x in grp)
        rule = "不得高於 P3"
    else:
        ok, rule = True, "不設約束"
    if not ok:
        violations.append((ch, up, dict(dist)))
    print(f"{ch:>3} {up:>7} {len(grp):>5}  {str(dict(dist)):<24} {rule:<12} "
          f"{'滿足' if ok else '**不滿足**'}")

if violations:
    print("\nR-VC13：下列章不滿足其約束。條文明定不得逐筆抬升以求滿足 —— 停並回報。")
    for v in violations:
        print("  ", v)
    sys.exit(1)

# ---- 與 T24 草案之異動對照
draft = {r["req_id"]: r for r in csv.DictReader(
    (ROOT / "data" / "priority_draft.tsv").open(encoding="utf-8"),
    delimiter="\t")}
changes = [(x["req_id"], x["section"], x["upstream"],
            draft[x["req_id"]]["final_p"], x["final_p"],
            "R-VC14" if x["req_id"] in RVC14 else "R-VC13")
           for x in rows if draft[x["req_id"]]["final_p"] != x["final_p"]]

out = ROOT / "data" / "priority_final.tsv"
with out.open("w", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["req_id", "section", "chapter", "037_priority",
                "local_p", "final_p", "note", "basis", "requirement_title"])
    for x in rows:
        w.writerow([x["req_id"], x["section"], x["chapter"], x["upstream"],
                    x["local_p"], x["final_p"], x["note"], x["basis"],
                    x["title"]])

print(f"\nleaf 母體: {len(rows)}")
print("T24 草案定案分布:",
      dict(Counter(draft[x['req_id']]['final_p'] for x in rows)))
print("本輪定案分布   :", dict(Counter(x["final_p"] for x in rows)))
print(f"\n異動 {len(changes)} 筆：")
for c in changes:
    print(f"  {c[0]:<20} §{c[1]:<8} 037={c[2]:<7} {c[3]} -> {c[4]}   依 {c[5]}")
print("\n定案 P0：")
for x in rows:
    if x["final_p"] == "P0":
        print(f"  {x['req_id']:<20} §{x['section']:<8} {x['basis']}")
print(f"\n寫出: {out}")
