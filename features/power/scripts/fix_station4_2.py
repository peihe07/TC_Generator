"""站④-2 —— 15 條 `<STATE>` 之逐條指定（Pei 2026-08-30 授權執行層直接處置）。

每一條之依據**取自該條自身之 `test_item` 上半 verbatim 或既有裁決**，不另造判準：

  `-198`–`-201`  `SWE-PM-103`：`test_item` 逐字為 `CFTS009-4941365`（§1.6.2.1.2 **Idle**）
                 之段落（「This status is related to TLM audio is OFF. TLM shall allow only
                 Splash Screen visualization…」）→ `<STATE>` = `Idle`（raw 3）
  `-105/-106`    觀察標的為 `"Splash Screen"` 本身（`test_item`：「TLM has to show a proper
                 Splash Screen」），非某一態之全組子項 → 改直接具名元件檢查（白名單 (ii)）
  `-135/-136`    觀察標的為 rear view camera 影像（`test_item`：「rear view camera images
                 shall be provided」）→ 同上
  `-178/-179/-180` 觀察標的為 `"Start-up Animation"` 之取消 → 同上
  `-184/-270`    期望值非固定常數（「behave following the state diagram」／「shall not enter
                 stolen vehicle mode under any condition」）→ 用既有之 **baseline (f)** 型式
                 （同 `-118` 之先例）：先記基線值，再比對
  `-122`         Suspend-to-RAM 對應之 `PowerSts_Telematic` 值規格未載 →
                 `PENDING: DR-PW26`（與該條既有之 DR-PW26 佔位同源）
  `-279`         `INIT` **不在 `VAL_ 1470`**（A-PW350 / R-P363(c)）→ `PENDING: DR-PW26 INIT 觀察量`

用法：
    python features/power/scripts/fix_station4_2.py [--dry-run]
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCHES = ROOT / "features/power/generated"
PS = "$STATUS_TELEMATIC.PowerSts_Telematic$"
FUNC = "Apply FUNC_STATE_<STATE> and check its Display sub-item"
READ_PH = f"Read the signal {PS} and check that it is the expected <raw> (<STATE>)"


def n(t):
    return f"NR1L-PowerManagement-{t}"


# tc → (待換文字, 換成, 依據)
EDITS: dict[str, list[tuple[str, str, str]]] = {}
for t in ("198", "199", "200", "201"):
    EDITS[n(t)] = [(FUNC, "Apply FUNC_STATE_IDLE and check its Display sub-item",
                    "`test_item` 逐字為 `CFTS009-4941365`（§1.6.2.1.2 Idle）之段落"),
                   (READ_PH, f"Read the signal {PS} and check that it is 3 (Idle)",
                    "同上")]
for t in ("105", "106"):
    EDITS[n(t)] = [(FUNC,
                    'Read the HU screen and check that the "Splash Screen" is shown on it',
                    "`test_item`：「TLM has to show a proper Splash Screen」——"
                    "觀察標的為該具名元件本身，非某一態之全組子項")]
for t in ("135", "136"):
    EDITS[n(t)] = [(FUNC,
                    'Read the HU screen and check that the "Rear View Camera" video '
                    "is shown on it",
                    "`test_item`：「rear view camera images shall be provided」")]
for t in ("178", "179", "180"):
    EDITS[n(t)] = [(FUNC,
                    'Read the HU screen and check that the "Start-up Animation" '
                    "is no longer played on it",
                    "`test_item`：動畫之取消為本條之驗證標的")]
EDITS[n("184")] = [
    (READ_PH,
     f"Read the signal {PS} and check that it is the same value as State_before",
     "期望值非固定常數（「behave following the state diagram」）——"
     "用既有 baseline (f) 型式，同 `-118` 之先例")]
EDITS[n("270")] = [
    (READ_PH,
     f"Read the signal {PS} and check that it is the same value as State_before",
     "「shall not enter stolen vehicle mode under any condition」——"
     "`VAL_ 1470` 無 stolen vehicle 值，故以基線不變落實")]
EDITS[n("122")] = [
    (READ_PH,
     "PENDING: DR-PW26 Suspend-to-RAM 對應之 PowerSts_Telematic 值",
     "規格未載其對應值；與本條既有之 DR-PW26 佔位同源")]
EDITS[n("279")] = [
    (READ_PH,
     "PENDING: DR-PW26 INIT 觀察量",
     "`INIT` 不在 `VAL_ 1470`（A-PW350 / R-P363(c)）")]

# baseline 型式需先記基線 —— 於步 1 前插入
BASELINE = {n("184"), n("270")}


def main() -> None:
    dry = "--dry-run" in sys.argv
    files = {p: json.loads(p.read_text()) for p in sorted(BATCHES.glob("batch_*.json"))}
    done = []
    for p, d in files.items():
        hit = False
        for tc in d["tcs"]:
            eds = EDITS.get(tc["tc_id"])
            if not eds:
                continue
            why = []
            for old, new, note in eds:
                for f in ("test_procedure", "expected_result"):
                    v = tc.get(f) or ""
                    if old in v:
                        tc[f] = v.replace(old, new)
                        hit = True
                # ER 之鏡像句（`The signal value … is received` 型）同步
                if "<STATE>" in (tc.get("expected_result") or ""):
                    er = tc["expected_result"]
                    if "Idle" in new:
                        er = er.replace("the expected <raw> (<STATE>)", "3 (Idle)")
                    er = re.sub(r"FUNC_STATE_<STATE>", "FUNC_STATE_IDLE", er) \
                        if "FUNC_STATE_IDLE" in new else er
                    tc["expected_result"] = er
                why.append(note)
            if tc["tc_id"] in BASELINE:
                ps = [re.sub(r"^\s*\d+\.\s*", "", l).strip()
                      for l in (tc.get("test_procedure") or "").splitlines()
                      if re.match(r"^\s*\d+\.", l)]
                es = [re.sub(r"^\s*\d+\.\s*", "", l).strip()
                      for l in (tc.get("expected_result") or "").splitlines()
                      if re.match(r"^\s*\d+\.", l)]
                ps.insert(0, f"Read the signal {PS} and record the value as State_before")
                es.insert(0, "State_before is recorded")
                tc["test_procedure"] = "\n".join(f"{i}. {x}" for i, x in enumerate(ps, 1))
                tc["expected_result"] = "\n".join(f"{i}. {x}" for i, x in enumerate(es, 1))
                hit = True
            tc["remarks"] = re.sub(r"\s*\(站④-2：[^)]*\)", "",
                                   tc.get("remarks") or "").strip()
            tc["reasoning_note"] = (tc.get("reasoning_note") or "") + (
                "\n\n**站④-2 之處置（Pei 2026-08-30 授權執行層直接處置）**："
                + "；".join(dict.fromkeys(why)) + "。**依據取自本條 `test_item` 上半 verbatim "
                "或既有裁決，未另造判準。**")
            done.append(tc["tc_id"])
        if hit and not dry:
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
    print(f"站④-2 處置 {len(done)} / {len(EDITS)} 條；未命中 "
          f"{sorted(set(EDITS) - set(done)) or '無'}")
    if dry:
        print("（dry-run）")


if __name__ == "__main__":
    main()
