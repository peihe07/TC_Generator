#!/usr/bin/env python3
"""T15 之逐條自檢 —— 下放包 09 §6.2 八項拘束，逐條機器可查。

**只讀，不改產物。** 任一項不過即 exit 1。
"""
import json
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
TCS = json.loads((ROOT / "generated" / "pilot_group3.json").read_text("utf-8"))
A03 = ROOT / "inputs" / "DD_SWE1_0807_EN.xlsx"
ROW = {"009": 17, "010": 18, "011": 19, "012": 20}
FOUR = ["pre_conditions", "input_test_data", "test_procedure", "expected_result"]

wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
rows = [list(r) for r in wb["Analysis Report"].iter_rows(values_only=True)]
wb.close()

res = []


def chk(no, name, ok, detail):
    res.append((no, name, ok, detail))


# --- 1 來源：上半為 037 c3 之子串；token ≤ 50；同源下半不逐字相同 ---
sub_ok, tok_ok, det = True, True, []
for tc in TCS:
    leaf = tc["req_id"][-3:]
    up = tc["test_item"].split("\n(")[0]
    src = rows[ROW[leaf] - 1][3]
    s = up in src
    n = len(up.split())
    sub_ok &= s
    tok_ok &= (n <= 50)
    det.append(f"{leaf}: 子串 {'✓' if s else '✗'} / {n} token")
chk(1, "來源：上半 verbatim 子串 ＋ token ≤ 50", sub_ok and tok_ok, "；".join(det))

by_req = {}
for tc in TCS:
    by_req.setdefault(tc["spec_reference"], []).append(tc["test_item"].split("\n", 1)[-1])
dup = [k for k, v in by_req.items() if len(v) != len(set(v))]
chk(1.1, "同一 Requirement ID 衍生之列下半不逐字相同", not dup,
    "無重複" if not dup else f"重複於 {dup}")

# --- 2 spec_reference：一行一 ObjectID，值域正確 ---
want = {"009": "CFTS022-4915108", "010": "CFTS022-4915108",
        "011": "CFTS022-4915109", "012": "CFTS022-4915109"}
ok2 = all(tc["spec_reference"] == want[tc["req_id"][-3:]] for tc in TCS)
ok2 &= all("\n" not in tc["spec_reference"] and not re.search(r"[,、;]", tc["spec_reference"])
           for tc in TCS)
chk(2, "spec_reference：值正確、一行一 ObjectID、無串接", ok2,
    "／".join(f"{tc['req_id'][-3:]}={tc['spec_reference']}" for tc in TCS))

# --- 3 ER 錨：四詞不得出現於 ER；觀察面具名或逐字 popup ---
BAN = ["RESTRICTED", "NOT_RESTRICTED", "Locked", "Unlocked"]
hits = [(tc["tc_id"], w) for tc in TCS for w in BAN if w in tc["expected_result"]]
chk(3, "ER 不含 RESTRICTED／NOT_RESTRICTED／Locked／Unlocked", not hits,
    "0 命中" if not hits else str(hits))
POPUP = "Feature not available while the vehicle is in motion."
named = all(('"Pairing (1st time)"' in tc["expected_result"]
             or '"Reconfigurable menu bar"' in tc["expected_result"]
             or POPUP in tc["expected_result"]) for tc in TCS)
vague = [tc["tc_id"] for tc in TCS
         if re.search(r"some restricted feature|a locked-out feature|the restricted feature\b",
                      tc["expected_result"], re.I)]
chk(3.1, "觀察面 A 取樣具名／觀察面 B 字串逐字；無泛稱", named and not vague,
    f"具名 {named}；泛稱命中 {vague or '無'}")

# --- 4 訊號寫法 ＋ A-DD6 標記 ---
form = all(re.search(r"\$STATUS_CCAN3\.VehicleSpeedVSOSig\$", tc["test_procedure"])
           for tc in TCS)
raw129 = [tc["req_id"][-3:] for tc in TCS if "= 129 (8.0625 km/h)" in tc["test_procedure"]]
mark = [tc["req_id"][-3:] for tc in TCS if "[ASSUMPTION A-DD6]" in tc["expected_result"]]
chk(4, "訊號寫法 profile §3；用及 §3.1 raw 者標 [ASSUMPTION A-DD6]",
    form and set(raw129) == {"009", "011"} and set(mark) == {"009", "011"},
    f"raw129 於 {raw129}；A-DD6 標於 {mark}")

# --- 5 priority ---
wantp = {"009": "P0", "010": "P1", "011": "P0", "012": "P1"}
ok5 = all(tc["priority"] == wantp[tc["req_id"][-3:]] for tc in TCS)
chk(5, "priority：009／011 = P0，010／012 = P1", ok5,
    "／".join(f"{tc['req_id'][-3:]}={tc['priority']}" for tc in TCS))

# --- 6 §8.4.2 界線 ---
FORBID = ["seat belt", "seatbelt", "passenger detection", "Are you the passenger",
          "occupant", "ADAS", "Level 3", "per-key-cycle", "key cycle", "Fullscreen"]
leak = [(tc["tc_id"], w) for tc in TCS for w in FORBID
        for f in FOUR + ["test_item"] if w.lower() in tc[f].lower()]
chk(6, "§8.4.2 界線：安全帶／乘客偵測／乘客確認／UF1-2／ADAS 分支 未引入",
    not leak, "0 命中" if not leak else str(leak))

# --- 7 fail-safe 形態逐 leaf 依 037 AC2 原文 ---
det7 = []
ok7 = True
for leaf in ("010", "012"):
    tc = next(t for t in TCS if t["req_id"].endswith(leaf))
    src = rows[ROW[leaf] - 1]
    says_stop = "stops transmitting" in src[3]
    says_to = "timeout" in (src[18] or "").lower()
    used_timeout = "timeout" in tc["test_procedure"].lower()
    used_sna = "8191" in tc["test_procedure"] or "(SNA)" in tc["test_procedure"]
    good = says_stop and says_to and used_timeout and not used_sna
    ok7 &= good
    det7.append(f"{leaf}: 037 書停送 {says_stop}／書 timeout {says_to} → 用逾時 {used_timeout}、未用 SNA {not used_sna}")
chk(7, "fail-safe 形態逐 leaf 依 037 AC2 原文（未統一指定）", ok7, "；".join(det7))

# --- 8 IN §10.5 / §11 ---
steps = {tc["tc_id"]: len(re.findall(r"^\d+\.", tc["test_procedure"], re.M)) for tc in TCS}
ers = {tc["tc_id"]: len(re.findall(r"^\d+\.", tc["expected_result"], re.M)) for tc in TCS}
ok_steps = all(v >= 2 for v in steps.values())
ok_11 = all(steps[t] == ers[t] for t in steps)
period = [(tc["tc_id"], f, ln) for tc in TCS for f in FOUR
          for ln in tc[f].split("\n") if ln.rstrip().endswith(".")]
brack = [(tc["tc_id"], f) for tc in TCS for f in FOUR
         if re.search(r"\[(?!ASSUMPTION)[A-Za-z][^\]]*\]", tc[f])]
modal = [(tc["tc_id"], w) for tc in TCS for w in ("shall", "should", "must", "may ")
         if w in tc["expected_result"].lower()]
chk(8, "IN §10.5 步驟 ≥ 2；§6 Procedure↔ER 1:1", ok_steps and ok_11,
    f"步驟 {steps}／ER {ers}")
chk(8.1, "IN §11 四欄無行尾句號；UI 標籤用雙引號非方括號", not period and not brack,
    f"行尾句號 {period or '無'}；方括號 {brack or '無'}")
chk(8.2, "IN §6 ER 無 modal verb", not modal, f"{modal or '無'}")

# --- 額外：R-DD9 之值寫法 ---
r9 = all(re.search(r"= 129 \(8\.0625 km/h\)", t["test_procedure"]) for t in TCS
         if t["req_id"][-3:] in ("009", "011"))
chk("+", "R-DD9(b) 連續量寫 `= <raw> (<物理值與單位>)`", r9, "009／011 皆合")

print("=" * 78)
print("T15 逐條自檢 —— 下放包 09 §6.2")
print("=" * 78)
bad = 0
for no, name, ok, det in res:
    bad += (not ok)
    print(f"[{'PASS' if ok else 'FAIL'}] §6.2-{no}  {name}")
    print(f"        {det}")
print("=" * 78)
print(f"RESULT: {'ALL PASS' if not bad else f'{bad} FAIL'}  （{len(res)} 檢）")
sys.exit(1 if bad else 0)
