"""65 包 §H 第 2 步 —— 六名七條依 R-P383 / 65 包 §0 表改寫。

§0 表為分析層人讀之結論：**六名皆為 TC 措辭問題，查無 0**。
本腳本依該表之「觀察量（白名單類）」與結構改寫七條；
步驟措辭依 R-1 v3 / IN §11 定稿（§0 明示「本節給觀察量與結構，不給逐字」）。

每一觀察量引其錨點 ObjectID（R-P383）。錨點自 `data/layer3_full.tsv`
之 `leaf → item_ids` 取，另加 §0 表所指名者。

用法：
    python features/power/scripts/apply_r_p383_65.py [--dry-run]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCHES = ROOT / "features/power/generated"

EDITS = {
    # -027：去話／來話各給可觀察面；TLM 態走訊號
    "NR1L-PowerManagement-027": dict(
        test_procedure=(
            "1. Place an outgoing bluetooth call from the paired phone through the TLM\n"
            "2. Read the paired phone screen and check that it shows the call as connected, "
            "and check that the call audio is present on the HU speakers\n"
            "3. End that call and let the paired phone place an incoming call to the HU\n"
            '4. Read the HU screen and check that the incoming call pop-up is shown, then answer it\n'
            "5. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)"),
        expected_result=(
            "1. The outgoing call is placed from the paired phone\n"
            "2. The paired phone shows the call as connected and the call audio is present on the HU speakers\n"
            "3. The incoming call reaches the HU\n"
            "4. The incoming call pop-up is shown on the HU screen and the call is answered\n"
            "5. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received"),
        note=("**R-P383 改寫（65 包）**：原步 3 之 `call audio routing and the TLM state` "
              "為 TC 自造之複合名詞，非可觀察量。依 65 包 §0 拆為三個白名單量 —— "
              "去話以手機端顯示 ＋ HU 揚聲器通話音訊 (iii)、來話以 HU 來電 pop-up (ii)、"
              "TLM 態以 `$STATUS_TELEMATIC.PowerSts_Telematic$` (i)。"
              "⚠ 錨點 `CFTS009-4941715` 為導言句（`according to following logics`），"
              "實質規則在 `4941716` 以後之各 Case；**本條與 `SWE-PM-064` / `SWE-PM-065` "
              "之 Case TC 有 IN §8.2.1 重疊之虞，記明不刪**（RD 單位屬上游）。"),
    ),
    # -031：第二通來話；Timeout1 由 ENTER_TIMED ＋ Comfort_Enable_Time 建立
    "NR1L-PowerManagement-031": dict(
        pre_conditions=(
            "1. A paired bluetooth phone is available on the bench\n"
            "2. Apply ENTER_TIMED\n"
            "3. $BCM_FD_27.Comfort_Enable_Time$ is at a value other than 0 (DR-PW26)\n"
            "4. One call has already ended before that value has elapsed"),
        test_procedure=(
            "1. Place a second bluetooth call from the paired phone while "
            "$BCM_FD_27.Comfort_Enable_Time$ has not yet elapsed\n"
            "2. Answer the call and check that the call audio is present on the HU speakers\n"
            "3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)"),
        expected_result=(
            "1. The second bluetooth call reaches the HU before "
            "$BCM_FD_27.Comfort_Enable_Time$ has elapsed\n"
            "2. The call is answered and the call audio is present on the HU speakers\n"
            "3. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received"),
        note=("**R-P383 改寫（65 包）**：原步 2 之 `call audio routing and the TLM state` 拆為 "
              "HU 揚聲器通話音訊 (iii) 與 `$STATUS_TELEMATIC.PowerSts_Telematic$` (i)。"
              "`Timeout1 still running` 之前置改由 `ENTER_TIMED` ＋ "
              "`$BCM_FD_27.Comfort_Enable_Time$` 值建立（R-P371）。錨點 "
              "`CFTS009-4941720` / `CFTS009-4941721`。"),
    ),
    # -117：TLM 態走訊號；RemStartFail 維持 PENDING；ITD 內聯（家族 K）
    "NR1L-PowerManagement-117": dict(
        input_test_data="NA",
        test_procedure=(
            "1. PENDING: DR-PW23 PhoneCall.Info 之驅動方法（使其轉為 \"not Active\"）\n"
            "2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)\n"
            "3. PENDING: DR-PW23 RemStartFail 之觀察方法"),
        expected_result=(
            "1. PENDING: DR-PW23 PhoneCall.Info\n"
            "2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby) is received\n"
            "3. PENDING: DR-PW23 RemStartFail"),
        note=("**R-P383 改寫（65 包）**：原步 2 之 `remote start outcome flag and the TLM state` "
              "拆為二 —— TLM 態以 `$STATUS_TELEMATIC.PowerSts_Telematic$` (i)；"
              "`RemStartFail` 讀值**維持 `PENDING: DR-PW23`**。"
              "原步 1 `Send the value listed in Input Test Data` 為家族 K，依 R-P366 內聯後 ITD 改 `NA`；"
              "惟其值為 `PhoneCall.Info`（內部變數），內聯後仍落 PENDING。"
              "⚠ **本條之因（`PhoneCall.Info` 轉 `Not_Active`）為內部變數，"
              "不符 R-P376(a)(ii)，不適用丁案**。錨點 `CFTS009-4941655`。"),
    ),
    # -172：主 CPU / CAN micro 各給觀察面；ER 2 依 §8.2.1 移除
    "NR1L-PowerManagement-172": dict(
        input_test_data="NA",
        test_procedure=(
            '1. Press and hold the H/K "Power" button for 10 seconds consecutively\n'
            "2. Read the HU screen and check that it goes dark and then shows the "
            '"Splash Screen" again\n'
            "3. Read the bus trace and check that the $STATUS_TELEMATIC$ message stops "
            "being transmitted and then resumes"),
        expected_result=(
            '1. The H/K "Power" button is held for 10 seconds consecutively\n'
            '2. The HU screen goes dark and then shows the "Splash Screen" again\n'
            "3. The $STATUS_TELEMATIC$ message stops being transmitted on the bus trace "
            "and then resumes"),
        note=("**R-P383 改寫（65 包）**：原步 2 之 `HU behavior and the stored logs`、"
              "步 3 之 `both processors` 皆非可觀察量。依 65 包 §0 —— "
              "主 CPU 重置以畫面熄滅後重新顯示 `\"Splash Screen\"` (ii)；"
              "CAN micro 重置以 bus trace 上 `$STATUS_TELEMATIC$` 訊息中斷後恢復 (iv)。"
              "觸發改逐字引 `CFTS009-4941858`（`$ICSPowerButton$ = [Pressed]` 10 秒）。"
              "⚠ **原 ER 2「collects and saves logs」屬 `CFTS009-4941860`，"
              "非本條 `test_item` 所本之 `CFTS009-4941861`，依 IN §8.2.1 移除** —— "
              "該項由 `4941860` 之 TC 承擔。原 ER 1「performs a radio reset」屬 `4941858`，"
              "同理僅作觸發步之 ER，不另立驗證項。"),
    ),
    # -224：觀察面為畫面文字；具體文字 PENDING DR-PW27；PROXI 三值入前置
    "NR1L-PowerManagement-224": dict(
        pre_conditions=(
            "1. A LIN and CAN simulation tool is connected\n"
            "2. The screen size is other than 7 inch\n"
            "3. PROXI VC_VEH_BRAND = a value other than \"Maserati\"\n"
            "4. PROXI TBM_Present = \"Present\"\n"
            "5. PROXI Country_Code = a market that requires geolocation and SOS in the disclaimer"),
        test_procedure=(
            "1. Apply ENTER_FULL_OPERATION and let the HU reach the disclaimer presentation\n"
            '2. Read the HU screen and check whether the "Disclaimer" screen or the '
            'geolocation pop-up is shown\n'
            "3. PENDING: DR-PW27 HMI disclaimer wording（ADAS ＋ SOS 之逐字文字）"),
        expected_result=(
            "1. The HU reaches the disclaimer presentation\n"
            '2. Either the "Disclaimer" screen or the geolocation pop-up is shown\n'
            "3. PENDING: DR-PW27 HMI disclaimer wording"),
        note=("**R-P383 改寫（65 包）**：原步 2 之 `shown wording` 非具名觀察量。"
              "依 65 包 §0 —— 觀察面為 `\"Disclaimer\"` 畫面／geolocation pop-up 之文字內容 (ii)；"
              "**具體文字規格寫「See HMI」而 HMI 文件不在 G0 台帳，開 `DR-PW27`**（未尋獲文件型）。"
              "Pre-Condition 之三個 `$…$` 改為 `PROXI <Param>`（R-1 v3 (c)）。"
              "⚠ ER 1 之「pop-up **or** disclaimer」二擇一判準未載，即 **DR-PW22** 所問者，"
              "本次不另開 DR，二問同情境。錨點 `CFTS009-4941968`。"),
    ),
    # -262：五值逐一（家族 K (c) 類）；功能可用之代理量為音源持續播放
    "NR1L-PowerManagement-262": dict(
        test_procedure=(
            "1. Apply each ignition working condition listed in Input Test Data in turn "
            "by sending $STATUS_BH_BCM1.OperationalModeSts$ (DR-PW26)\n"
            "2. After each one, read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and "
            "check that it is 4 (Full_Operation)\n"
            "3. After each one, check that the audio active source keeps playing on the HU speakers"),
        expected_result=(
            "1. Each listed ignition working condition is registered without a bus error\n"
            "2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) "
            "is received after each one\n"
            "3. The audio active source keeps playing on the HU speakers after each one"),
        note=("**R-P383 改寫（65 包）**：原步 2 之 `TLM_Status.Info after each one` "
              "改為 `$STATUS_TELEMATIC.PowerSts_Telematic$` (i)；"
              "原 ER 2 之「all TLM, AMP, ICS and DTV functionalities available」"
              "改以**代理量**「音源持續播放」(iii) —— 依 `CFTS009-4941453` 之表，"
              "Full-Operation 列載 `TLM plays the audio active source`。"
              "⚠ **本條為家族 K (c) 類**（一步多值、值間並列），"
              "依 R-P366(c) / R-P373(a) **ITD 保留不改 `NA`**，ER 逐值對齊。"),
    ),
    # -271：進入態→保持→到期後轉態，全走訊號；步 1 之複合名改訊號＋音源
    "NR1L-PowerManagement-271": dict(
        pre_conditions=(
            "1. A LIN and CAN simulation tool is connected\n"
            "2. $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) (DR-PW26)\n"
            "3. Apply ENTER_TIMED"),
        test_procedure=(
            "1. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed), "
            "and check that the audio active source keeps playing on the HU speakers\n"
            "2. Hold for the $BCM_FD_27.Comfort_Enable_Time$ value with no phone call active\n"
            "3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)"),
        expected_result=(
            "1. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received "
            "and the audio active source keeps playing on the HU speakers\n"
            "2. The $BCM_FD_27.Comfort_Enable_Time$ value elapses with no phone call active\n"
            "3. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby) is received"),
        note=("**R-P383 改寫（65 包）**：原步 2 之 `TLM state again after Timeout1 has elapsed` "
              "改為三段 —— 進入時 `= 2 (Timed)`、`Hold for $BCM_FD_27.Comfort_Enable_Time$`"
              "（R-1 v3 (e)，值依 R-P371 之候選）、之後 `= 1 (Standby)`，皆 (i) 類。"
              "原步 1 之 `TLM power indication and the AMP, ICS and DTV states` "
              "改為訊號 ＋ 音源持續播放 (iii)。"
              "⚠ **與 Timeout1 到期轉態之 TC 有重疊之虞，記明不刪**（IN §8.2.1，RD 單位屬上游）。"
              "錨點 `CFTS009-4941402` / `CFTS009-4941404` / `CFTS009-4941453`。"),
    ),
}


def main() -> None:
    dry = "--dry-run" in sys.argv
    done = []
    for path in sorted(BATCHES.glob("batch_*.json")):
        data = json.loads(path.read_text())
        touched = False
        for tc in data["tcs"]:
            e = EDITS.get(tc["tc_id"])
            if not e:
                continue
            touched = True
            done.append(tc["tc_id"])
            note = e.pop("note")
            tc.update(e)
            tc["reasoning_note"] = (tc.get("reasoning_note") or "") + "\n\n" + note
            tc["remarks"] = ((tc.get("remarks") or "").strip()
                             + (" " if tc.get("remarks") else "") + "(R-P383)")
            print(f"### {tc['tc_id']}")
            for f in ("pre_conditions", "input_test_data",
                      "test_procedure", "expected_result"):
                print(f"  {f}: {(tc.get(f) or '').replace(chr(10), ' | ')[:200]}")
        if touched and not dry:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            print(f"→ 寫回 {path.relative_to(ROOT)}")
    missing = set(EDITS) - set(done)
    print(f"\n改寫 {len(done)} / 7；未命中 {sorted(missing) if missing else '無'}")
    if dry:
        print("（dry-run，未寫回）")


if __name__ == "__main__":
    main()
