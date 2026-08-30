"""67 包 §H 第 4 步之補正 —— G245 殘留與 R-P357(b) 互註。

一、G245（R-P362：判準 = `remeasure_55.py` 上界）該批殘留 14 條，逐條檢視後分二因：
  (a) **具名 UI 元件未加引號** —— R-P384(b) 指「抽取」不以引號為要件，
      惟 **IN §11 之 TC 書寫規則要求加引號**；二者不衝突（一為抽取、一為書寫）。
      本補正為具名元件加引號，同時滿足 §11 與 G245。
  (b) **措辭落在白名單之外** —— `Read the paired phone …`（手機端非指定揚聲器）、
      `Check that State_sna equals State_ignoff`（比較步非觀察步）。
      改寫為白名單內之句式，比較併入前一步之 check。

二、R-P357(b)：`-155`（`SWE-PM-056`）與 `-185`（`SWE-PM-097`）五欄逐字相同而
   **Req ID 不同** —— 依 R-P357(b) 二列皆保留、不得合併，**Remarks 互註對方 tc_id**。
   本腳本一併補全案 12 對 (b) 型之互註（B5 凍結期間該項從未施作）。

用法：
    python features/power/scripts/fix_batch1_67.py [--dry-run]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCHES = ROOT / "features/power/generated"
PS = "$STATUS_TELEMATIC.PowerSts_Telematic$"
FIVE = ("test_item", "pre_conditions", "input_test_data",
        "test_procedure", "expected_result")

LOGO_PROC = ('3. Read the "Brand Logo Screen" and check which of the named logos '
             "is shown on it")
LOGO_ER = ('3. The logo shown on the "Brand Logo Screen" is the one named for this '
           "configuration")

FIX = {}
for t in ("148", "149", "150", "151", "152", "192", "193", "194", "195"):
    FIX[f"NR1L-PowerManagement-{t}"] = dict(
        proc_sub=("3. Read the brand logo screen and check which of the named logos "
                  "is shown", LOGO_PROC),
        er_sub=("3. The logo shown on the brand logo screen is the one named for "
                "this configuration", LOGO_ER))
for t in ("155", "185"):
    FIX[f"NR1L-PowerManagement-{t}"] = dict(
        proc_sub=("3. Apply ENTER_FULL_OPERATION and read the brand logo screen, and "
                  'check that the "Fiat Latam Logo" is shown in place of the vehicle '
                  "brand logo",
                  '3. Apply ENTER_FULL_OPERATION and read the "Brand Logo Screen", and '
                  'check that the "Fiat Latam Logo" is shown on it in place of the '
                  '"Vehicle Brand Logo"'),
        er_sub=('3. The "Fiat Latam Logo" is shown on the brand logo screen in place '
                "of the vehicle brand logo",
                '3. The "Fiat Latam Logo" is shown on the "Brand Logo Screen" in place '
                'of the "Vehicle Brand Logo"'))
for t, sig in (("011", "$STATUS_LIN.PN14_LS_Lvl7$"), ("012", "$STATUS_LIN.Batt_ST_Crit$")):
    k = 4 if t == "011" else 3
    FIX[f"NR1L-PowerManagement-{t}"] = dict(
        proc_sub=(f"{k}. Read the paired phone and check that the call is still "
                  "connected and its audio is present on the phone",
                  f'{k}. Read the "Call Screen" on the paired phone and check that it '
                  "still shows the call as connected"),
        er_sub=(f"{k}. The call is still connected on the paired phone and its audio "
                "is present on the phone",
                f'{k}. The "Call Screen" on the paired phone still shows the call as '
                "connected"))
FIX["NR1L-PowerManagement-118"] = dict(
    proc_sub=("3. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 15 (SNA) "
              f"(DR-PW26), then read the signal {PS} and record the value as State_sna\n"
              "4. Check that State_sna equals State_ignoff",
              "3. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 15 (SNA) "
              f"(DR-PW26), then read the signal {PS} and check that it is the same value "
              "as State_ignoff"),
    er_sub=("3. State_sna is recorded\n4. State_sna equals State_ignoff",
            f"3. The signal value {PS} after the SNA value is the same as State_ignoff"))
FIX["NR1L-PowerManagement-004"] = dict(
    proc_sub=('2. PENDING: DR-PW30 SplashScreen_Time 之值 —— read the HU screen at that '
              'time and check that the "Splash Screen" is shown',
              '2. PENDING: DR-PW30 SplashScreen_Time 之值 —— read the HU screen at that '
              'time and check that the "Splash Screen" is shown on it'),
    er_sub=("", ""))
FIX["NR1L-PowerManagement-169"] = dict(
    proc_sub=("", ""), er_sub=("", ""))

NOTE = ("\n\n**G245 補正（67 包）**：具名 UI 元件依 **IN §11** 加引號 —— "
        "R-P384(b) 之「不以引號為要件」指**抽取**判準，**書寫**仍依 §11。"
        "二者不衝突。另將落在白名單外之措辭（手機端音訊、比較步）改寫入白名單內。")
XREF = ("(R-P357(b)：與 {other} 五欄逐字相同而 Req ID 不同（{a} / {b}），"
        "二列皆保留不得合併；互註對方 tc_id)")


def main() -> None:
    dry = "--dry-run" in sys.argv
    files = {p: json.loads(p.read_text()) for p in sorted(BATCHES.glob("batch_*.json"))}
    tcs = {tc["tc_id"]: tc for d in files.values() for tc in d["tcs"]}

    # 一、G245 補正
    fixed = 0
    for tid, f in FIX.items():
        tc = tcs.get(tid)
        if not tc:
            continue
        for field, key in (("test_procedure", "proc_sub"),
                           ("expected_result", "er_sub")):
            old, new = f.get(key, ("", ""))
            if old and old in (tc.get(field) or ""):
                tc[field] = tc[field].replace(old, new)
                fixed += 1
        tc["reasoning_note"] = (tc.get("reasoning_note") or "") + NOTE

    # 二、R-P357(b) 互註（全案 (b) 型對）
    seen, pairs = {}, []
    for tc in tcs.values():
        k = tuple((tc.get(c) or "").strip() for c in FIVE)
        if k in seen:
            pairs.append((seen[k], tc["tc_id"]))
        else:
            seen[k] = tc["tc_id"]
    xrefed = 0
    for a, b in pairs:
        ta, tb = tcs[a], tcs[b]
        if ta["req_id"] == tb["req_id"]:
            continue                      # (a) 型不在此處理
        for me, other in ((ta, tb), (tb, ta)):
            mark = XREF.format(other=other["tc_id"], a=ta["req_id"], b=tb["req_id"])
            if "R-P357(b)" in (me.get("remarks") or ""):
                continue
            me["remarks"] = ((me.get("remarks") or "").strip()
                             + (" " if me.get("remarks") else "") + mark)
            xrefed += 1

    print(f"G245 補正欄位 {fixed} 處；R-P357(b) 互註 {xrefed} 處（(b) 型對 "
          f"{sum(1 for a, b in pairs if tcs[a]['req_id'] != tcs[b]['req_id'])}）")
    if not dry:
        for p, d in files.items():
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        print("已寫回")
    else:
        print("（dry-run）")


if __name__ == "__main__":
    main()
