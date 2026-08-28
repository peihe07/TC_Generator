#!/usr/bin/env python3
"""T24e（下放包 18 §四）—— 出貨就緒盤點。**只盤點，不寫回。**

可否出貨之判準**由產物導出**（IN §8.4.3：含 PENDING 之工作簿不得出貨），
非以 leaf 號或批次名硬編（R-DD23(ii)）。
凍結名單同樣不硬編 —— 自 profile §5 之凍結表讀出。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GEN = ROOT / "generated"
PROFILE = ROOT.parent.parent / "docs" / "runtime" / "profiles" / \
    "FW036_R1L_DriverDistraction_Profile.md"
FOUR = ["pre_conditions", "input_test_data", "test_procedure", "expected_result"]
ARTS = ["pilot_group3.json", "batch_b1.json", "batch_b2.json",
        "batch_body_off_init.json"]
TOTAL_LEAF = 28                      # 037 之 28 leaf（framework.md Part I）

rows = []
for a in ARTS:
    for tc in json.loads((GEN / a).read_text("utf-8")):
        body = " ".join(tc[f] for f in FOUR)
        pend = re.findall(r"PENDING: DR-\w+\d+", body)          # IN §8.4.3
        mk = sorted(set(re.findall(r"\[ASSUMPTION (A-DD\d+)\]", body)))
        rows.append({
            "art": a.replace(".json", ""), "tc_id": tc["tc_id"],
            "leaf": tc["req_id"][-3:], "set": tc["test_set"],
            "pri": tc["priority"], "mk": mk, "pend": pend,
            "ship": not pend,
        })
rows.sort(key=lambda r: r["leaf"])

# 凍結 leaf —— 自 profile §5 之凍結列讀出（`-025`~`-028` 等區間記法）
sec5 = PROFILE.read_text("utf-8").split("## §5 凍結與未結")[1].split("\n---")[0]
frozen = set()
for line in sec5.split("\n"):
    if "凍結" in line and "解凍" not in line:
        for m in re.finditer(r"leaf (\d{3})[–-](\d{3})", line):
            frozen |= {f"{n:03d}" for n in range(int(m.group(1)), int(m.group(2)) + 1)}
frozen = sorted(frozen)

gen = {r["leaf"] for r in rows}
ship = [r for r in rows if r["ship"]]
hold = [r for r in rows if not r["ship"]]

W = "=" * 96
print(W); print("T24e —— 出貨就緒盤點（只盤點，不寫回）"); print(W)
print(f"{'tc_id':<16}{'leaf':<6}{'Test Set':<22}{'pri':<5}{'marker':<26}出貨")
print("-" * 96)
for r in rows:
    flag = "可" if r["ship"] else f"**不可**（{'／'.join(r['pend'])}）"
    print(f"{r['tc_id']:<16}{r['leaf']:<6}{r['set']:<22}{r['pri']:<5}"
          f"{'／'.join(r['mk']) or '（無）':<26}{flag}")
print("-" * 96)
print(f"已產出 {len(rows)}　＝　可出貨 {len(ship)} ＋ 不得出貨 {len(hold)}")
print(f"凍結（profile §5 導出）{len(frozen)}：{frozen}")
tot = len(ship) + len(hold) + len(frozen)
print(f"閉合：{len(ship)} ＋ {len(hold)} ＋ {len(frozen)} ＝ {tot}"
      f"　對 28 leaf：{'✅ 閉合' if tot == TOTAL_LEAF else '❌ **不閉合**'}")
overlap = sorted(gen & set(frozen))
missing = sorted({f"{n:03d}" for n in range(1, TOTAL_LEAF + 1)} - gen - set(frozen))
print(f"已產出∩凍結（須為空）：{overlap or '空 ✓'}")
print(f"既未產出亦未凍結（須為空）：{missing or '空 ✓'}")
print(W)
raise SystemExit(0 if tot == TOTAL_LEAF and not overlap and not missing else 1)
