"""67 包 §H 第 4 步 —— R-P391(a) 第一批改寫（37 條相異 tc_id）。

依 66 包 §1 表之「觀察量／觸發與前置／PENDING·DR」三欄施作。
`$VC_*$` 依 **R-P389(c)** 保留規格原名（不加 `$`、不加 `PROXI`）＋ `(DR-PW28)`。
家族 K 之 ITD 依 R-P366(a) 內聯；(c) 類保留。

**不動 `test_item` 上半 verbatim**（R-6 / R-P343 / R-P347）；
括號下半為驗證標的之宣告，隨觀察量改寫。

用法：
    python features/power/scripts/apply_batch1_67.py [--dry-run]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCHES = ROOT / "features/power/generated"
TOOL = "1. A LIN and CAN simulation tool is connected"
PS = "$STATUS_TELEMATIC.PowerSts_Telematic$"


def n(tag: str) -> str:
    return f"NR1L-PowerManagement-{tag}"


E: dict[str, dict] = {}


def put(tag, note, **kw):
    E[n(tag)] = dict(note=note, **kw)


# ── 音訊類：call audio routing（觀察量 = 音訊自 HU 揚聲器消失、通話續於手機）──
for tag, itd, trig in (
    ("011", ["$STATUS_LIN.PN14_LS_Actv$ = 1 (Active)",
             "$STATUS_LIN.PN14_LS_Lvl7$ = 1 (Active)"],
     "Send the signal $STATUS_LIN.PN14_LS_Actv$ = 1 (Active)\n"
     "2. Send the signal $STATUS_LIN.PN14_LS_Lvl7$ = 1 (Active)"),
    ("012", ["$STATUS_LIN.Batt_ST_Crit$ = 1 (True)"],
     "Send the signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True)"),
):
    k = 2 if tag == "011" else 1
    put(tag,
        "**R-P386 改寫（67 包，第一批）**：原 `call audio routing` 為 TC 自造之複合名詞。"
        "依 66 包 §1 表，觀察量拆為二個 (iii) 類可量測音訊 —— "
        "通話音訊自 HU 揚聲器**消失**、手機端通話**持續**且音訊在手機端。"
        "ITD 之 LIN 訊號依 R-P373(d) 內聯（`[1h]` 改 `= 1 (<VAL_ 標籤>)`），ITD 改 `NA`。",
        input_test_data="NA",
        test_procedure=(f"1. {trig}\n"
                        f"{k+1}. Read the HU speakers and check that the call audio is "
                        f"no longer present on them\n"
                        f"{k+2}. Read the paired phone and check that the call is still "
                        f"connected and its audio is present on the phone"),
        expected_result=("1. The TLM accepts the signal without a bus error\n"
                         + ("2. The TLM accepts the second signal without a bus error\n"
                            if tag == "011" else "")
                         + f"{k+1}. The call audio is no longer present on the HU speakers\n"
                         f"{k+2}. The call is still connected on the paired phone and its "
                         f"audio is present on the phone"))

# ── Timeout1 群（-100/101/103/104、-119/120）──
TIMEOUT_NOTE = (
    "**R-P386 改寫（67 包，第一批）**：`Timeout1` 為 HU 內部參數，不可直接讀。"
    "依 66 包 §1 表，**以狀態持續時間為代理** —— "
    f"`{PS} = 2 (Timed)` 持續 `PROXI Switch_Off_Time` 之值後轉 `= 1 (Standby)`。"
    "`Hold for <值> ms` 依 R-1 v3 (e)。"
    "⚠ 前置 `SwitchOff_Timeout_Setting.Req = 00 min` 之 UI 設定名未查得，"
    "維持 `PENDING: DR-PW23`（R-P380(a)：運行時用法不撤）。")
for tag in ("100", "101", "103", "104"):
    hold = ("$BCM_FD_27.Comfort_Enable_Time$ (DR-PW26)" if tag == "104"
            else 'PROXI Switch_Off_Time')
    extra = ("\n4. PENDING: DR-PW23 Antitheft_Result.Info 之觀察方法（antitheft 成功）"
             if tag in ("100", "101") else "")
    xe = ("\n4. PENDING: DR-PW23 Antitheft_Result.Info"
          if tag in ("100", "101") else "")
    put(tag, TIMEOUT_NOTE,
        input_test_data="NA",
        test_procedure=(f"1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法"
                        f'（設為 "00 min"）\n'
                        f"2. Apply ENTER_TIMED and read the signal {PS} and check that it "
                        f"is 2 (Timed)\n"
                        f"3. Hold for the {hold} value, then read the signal {PS} and check "
                        f"that it is 1 (Standby)" + extra),
        expected_result=("1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req\n"
                         f"2. The signal value {PS} = 2 (Timed) is received\n"
                         f"3. The signal value {PS} = 1 (Standby) is received after the "
                         f"{hold} value has elapsed" + xe))
for tag in ("119", "120"):
    put(tag, TIMEOUT_NOTE,
        input_test_data="NA",
        test_procedure=("1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req 之設定方法\n"
                        "2. Apply ENTER_FULL_OPERATION\n"
                        "3. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 "
                        "(Ignition_Off) (DR-PW26)\n"
                        f"4. Read the signal {PS} and check that it is 2 (Timed), then hold "
                        f"for the PROXI Switch_Off_Time value and check that it is 1 (Standby)"),
        expected_result=("1. PENDING: DR-PW23 SwitchOff_Timeout_Setting.Req\n"
                         "2. The HU is in Full-Operation\n"
                         "3. The signal value $STATUS_BH_BCM1.OperationalModeSts$ = 2 "
                         "(Ignition_Off) is received\n"
                         f"4. The signal value {PS} = 2 (Timed) is received, and {PS} = 1 "
                         f"(Standby) is received after the PROXI Switch_Off_Time value has elapsed"))

# ── -118：baseline (f) 基線比較 ──
put("118",
    "**R-P386 改寫（67 包）**：原 `TLM state against the operative state management rules` "
    "非可觀察量。依 66 包 §1 表以**基線比較**落實「behaves as」—— "
    "先送 `Ignition_Off` 記其態為基線，復位後送 `SNA`，比對二者相同。"
    "二次讀值皆為 (i) 類，比較本身不引入新判準。",
    input_test_data="NA",
    test_procedure=("1. Apply ENTER_FULL_OPERATION, send the signal "
                    "$STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) (DR-PW26), "
                    f"then read the signal {PS} and record the value as State_ignoff\n"
                    "2. Apply ENTER_FULL_OPERATION again\n"
                    "3. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 15 (SNA) "
                    f"(DR-PW26), then read the signal {PS} and record the value as State_sna\n"
                    "4. Check that State_sna equals State_ignoff"),
    expected_result=("1. State_ignoff is recorded\n2. The HU is in Full-Operation again\n"
                     "3. State_sna is recorded\n4. State_sna equals State_ignoff"))

# ── -123：FUNC_STATE_STANDBY ──
put("123",
    "**R-P386 / R-P387(b) 改寫（67 包）**：原 `FPDM, AMP, ICS and DTV functions` 為 A1 家族。"
    "依 R-P387(b) **直接取 `CFTS009-4941453` 之 `Standby` 列**，不另造代理量："
    "Source OFF → 無音訊 (iii)；AMP OFF → 無放大輸出 (iii)；Display OFF (**) → 畫面關閉，"
    "**惟 `(**)`（`CFTS009-4941457`）例外：HMI Antitheft Screens**；"
    "BoosterOUT／天線 OFF → (v) 類，**位準值規格未載 → `PENDING: DR-PW27`**；MCU OFF → (iii)。"
    "另加態確認 (i)。片段全文見 `data/func_state_66.md` 之 `FUNC_STATE_STANDBY`。",
    input_test_data="NA",
    test_procedure=("1. Apply ENTER_STANDBY\n"
                    f"2. Read the signal {PS} and check that it is 1 (Standby)\n"
                    "3. Apply FUNC_STATE_STANDBY and check each of its sub-items"),
    expected_result=(f"1. The HU is in Standby\n2. The signal value {PS} = 1 (Standby) is received\n"
                     "3. FUNC_STATE_STANDBY holds:\n"
                     "   a. No audio source is playing on the HU speakers\n"
                     "   b. No amplifier output is present on the HU speakers\n"
                     "   c. The HU display is off, except for the HMI Antitheft Screens "
                     "(CFTS009-4941457)\n"
                     "   d. PENDING: DR-PW27 BoosterOUT / antenna supply OFF 位準值\n"
                     "   e. A USB device inserted on the bench is not enumerated and the AUX "
                     "input does not play on the HU speakers"))

# ── -169：FOTA pop-up 停留後轉 Standby ──
put("169",
    "**R-P386 改寫（67 包）**：原 `HU mode after the idle period` 非可觀察量。"
    "依 66 包 §1 表 —— pop-up 停留以 `\"FOTA update available\"` pop-up (ii)、"
    "`Hold for 60000 ms`（R-1 v3 (e)）、之後 `PowerSts_Telematic = 1 (Standby)` (i)。"
    "⚠ **FOTA 可用之建立方法規格指 CFTS057，該文件在 G0 台帳外** → `PENDING: DR-PW27`。"
    "⚠ §1 表另記「三個離開條件各一 TC（IN §8.3），現行只測 1 分鐘」—— "
    "**拆分未做**，見 67 包回報 §6。",
    input_test_data="NA",
    test_procedure=("1. PENDING: DR-PW27 CFTS057 —— FOTA update available 之建立方法\n"
                    "2. Apply ENTER_TIMED\n"
                    '3. Read the HU screen and check that the "FOTA update available" pop-up '
                    "is shown\n"
                    "4. Hold for 60000 ms with no user interaction, and check that the "
                    'pop-up stays on the HU screen\n'
                    f"5. Read the signal {PS} and check that it is 1 (Standby)"),
    expected_result=("1. PENDING: DR-PW27 CFTS057\n2. The HU is in Timed\n"
                     '3. The "FOTA update available" pop-up is shown on the HU screen\n'
                     "4. The pop-up stays on the HU screen for 60000 ms with no user interaction\n"
                     f"5. The signal value {PS} = 1 (Standby) is received"))

# ── -218：31 個點火循環之 disclaimer 計數（家族 K (c) 類）──
put("218",
    "**R-P386 改寫（67 包）**：原 `screen across the cycles` 非可觀察量。"
    "依 66 包 §1 表 —— 觀察量為 `\"Disclaimer\"` 畫面於連續 31 個點火循環中之**出現次數** (ii)，"
    "期望為 2（第 1 與第 31 次）。寫法依家族 K (c) 類：`Repeat … 31 times`，ER 逐輪對齊以計數。"
    "⚠ ITD 保留（(c) 類，R-P366(c) / R-P373(a)）。",
    input_test_data="Ignition cycles: 31 consecutive Ignition Off -> Ignition On cycles",
    test_procedure=("1. Repeat the ignition cycle listed in Input Test Data 31 times, sending "
                    "$STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) then = 4 "
                    "(Ignition_On) (DR-PW26)\n"
                    '2. After each cycle, read the HU screen and record whether the '
                    '"Disclaimer" screen is shown\n'
                    '3. Count the cycles in which the "Disclaimer" screen was shown'),
    expected_result=("1. All 31 ignition cycles are registered without a bus error\n"
                     '2. The presence of the "Disclaimer" screen is recorded for each of the '
                     "31 cycles\n"
                     '3. The "Disclaimer" screen was shown in exactly 2 cycles: cycle 1 and '
                     "cycle 31"))

# ── -005：只剩最終態 ──
put("005",
    "**R-P386 改寫（67 包）**：依 66 包 §1 表 —— 「event log」規格無、"
    "「buffered count」不可觀察，**二者刪**；只留最終態："
    f"開機完成後 `{PS}` = 開機中所注入之最後一個 `OperationalModeSts` 值所對應之態 (i)。"
    "⚠ ITD 保留（(c) 類：一步多值、值間並列）。",
    test_procedure=("1. Start the TLM boot sequence and send each ignition value listed in "
                    "Input Test Data in turn while the boot is still completing "
                    "($STATUS_BH_BCM1.OperationalModeSts$, DR-PW26)\n"
                    "2. Let the boot complete\n"
                    f"3. Read the signal {PS} and check that it corresponds to the last "
                    "ignition value that was sent"),
    input_test_data=("Ignition values during boot: 2 (Ignition_Off), 4 (Ignition_On), "
                     "2 (Ignition_Off)"),
    expected_result=("1. Each ignition value is registered without a bus error while the boot "
                     "is still completing\n2. The boot completes\n"
                     f"3. The signal value {PS} corresponds to the last ignition value that "
                     "was sent"))

# ── -050：電池重接後第一幀 ──
put("050",
    "**R-P386 改寫（67 包）**：原 `TLM_Status.Info and the state machine` 非可觀察量。"
    "依 66 包 §1 表 —— 以 bus 上 `STATUS_TELEMATIC` 之**第一幀**落實 INIT 之退出，"
    f"`{PS} = 0 (Sleep)`。**不需 `ENTER_INIT`**（其確認步 PENDING DR-PW26），"
    "本條以第一幀取代之。",
    input_test_data="NA",
    test_procedure=("1. Disconnect the battery from the HU\n2. Reconnect the battery\n"
                    "3. Read the bus trace and check that the first $STATUS_TELEMATIC$ frame "
                    f"transmitted after the reconnection carries {PS} = 0 (Sleep)"),
    expected_result=("1. The battery is disconnected\n2. The battery is reconnected\n"
                     "3. The first $STATUS_TELEMATIC$ frame after the reconnection carries "
                     f"{PS} = 0 (Sleep)"))

# ── -049：三個儲存變數 ──
put("049",
    "**R-P386 改寫（67 包）**：原 `three stored variables` 三者皆內部變數。依 66 包 §1 表 —— "
    "`VPLastStatus` 以「Ignition On 後之態與斷電前相同」為代理（baseline (f)，(i) 類）；"
    "二個 `.Req` 設定值以 UI 讀，其設定項名未查得 → `PENDING: DR-PW23 / DR-PW25`。"
    "⚠ `Recall_Last` 之邏輯屬 `CFTS009-4941610`，依 IN §8.2.1 **不擴入本條**。",
    input_test_data="NA",
    test_procedure=("1. Apply ENTER_FULL_OPERATION and read the signal "
                    f"{PS}, recording the value as State_before\n"
                    "2. Disconnect the battery from the HU, then reconnect it\n"
                    "3. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 4 (Ignition_On) "
                    f"(DR-PW26), then read the signal {PS} and check that it equals State_before\n"
                    "4. PENDING: DR-PW25 SwitchOffSetting.Req 與 Auto_SwitchOn_Setting.Req 之"
                    "設定項名與讀取方法"),
    expected_result=("1. State_before is recorded\n2. The battery is disconnected and reconnected\n"
                     f"3. The signal value {PS} equals State_before\n"
                     "4. PENDING: DR-PW25 SwitchOffSetting.Req / Auto_SwitchOn_Setting.Req"))

# ── -004：SplashScreen_Time / StandardScreen_Time ──
put("004",
    "**R-P386 改寫（67 包）**：觀察量為 `\"Splash Screen\"` 與標準畫面之有無 (ii)，以錄影時間戳判。"
    "⚠ **二時間參數之值全案未載** —— `SplashScreen_Time` / `StandardScreen_Time` 僅出現於 "
    "`CFTS010-4942337` 一處且無數值定義（三份文字層逐字掃描）。**開 `DR-PW30`**，"
    "時間點以 `PENDING: DR-PW30` 佔位；**觀察量本身已定，非 PENDING**。",
    input_test_data="NA",
    test_procedure=("1. Start the suspend-resume boot sequence with video recording running\n"
                    "2. PENDING: DR-PW30 SplashScreen_Time 之值 —— read the HU screen at that "
                    'time and check that the "Splash Screen" is shown\n'
                    "3. PENDING: DR-PW30 StandardScreen_Time 之值 —— read the HU screen before "
                    "and after that time and check that the standard screen is shown only after it"),
    expected_result=("1. The boot sequence is recorded\n"
                     "2. PENDING: DR-PW30 SplashScreen_Time\n"
                     "3. PENDING: DR-PW30 StandardScreen_Time"))

# ── 設定與選單類：PENDING DR-PW25 群 ──
MENU_NOTE = ("**R-P386 改寫（67 包）**：觀察量為設定頁所列項目之數與名 (ii)，"
             "**惟設定項名為 DR-PW25 之未決項** —— 依 R-P377(b)「弱候選不入 TC」，"
             "該項 `PENDING: DR-PW25`。⚠ `-017` / `-018` / `-019` 之名於 55 包可及性報告"
             "被截斷至 50 字元（A-PW366），本包以原名重取，三條併入本群同法處理。")
for tag in ("017", "018", "019", "020", "021", "143", "156"):
    put(tag, MENU_NOTE,
        test_procedure=("1. PENDING: DR-PW25 —— TLM 選單中該設定項之名稱與進入路徑\n"
                        "2. PENDING: DR-PW25 —— 讀該設定項所列之可選值（數與名）"),
        expected_result=("1. PENDING: DR-PW25\n2. PENDING: DR-PW25"))

# ── -121：Timed 態 Settings 可用項目 ──
put("121",
    "**R-P386 改寫（67 包）**：觀察量為 Timed 態 Settings 中 vehicle setup 類項目"
    "之不可用（灰化／不存在）(ii)；**項目清單在 TLM HMI documents，該文件在 G0 台帳外** "
    "→ `PENDING: DR-PW27`。",
    input_test_data="NA",
    test_procedure=("1. Apply ENTER_TIMED\n"
                    "2. PENDING: DR-PW27 TLM HMI documents —— 該態下應不可用之 vehicle setup "
                    "項目清單"),
    expected_result=("1. The HU is in Timed\n2. PENDING: DR-PW27 TLM HMI documents"))

# ── -216 / -217：disclaimer 之 SOS / Help（規格自給 token）──
for tag, tok, neg in (("216", '"SOS"', ""), ("217", '"Help"', ' and does not contain "SOS"')):
    put(tag,
        "**R-P386 改寫（67 包）**：原 `disclaimer wording` 非具名觀察量。"
        f"依 66 包 §1 表 —— **規格自給 token**，觀察量為 disclaimer 文字含 {tok}{neg} (ii)，"
        "**ER 不 PENDING**（與 `-222`／`-223` 之 ADAS 文字不同，後者繫 DR-PW27）。"
        "前置之 `$VC_VEH_BRAND$` / `$TBM_Present$` 依 **R-P389(c)** 保留規格原名。",
        input_test_data="NA",
        pre_conditions=(f"{TOOL}\n"
                        "2. Set VC_VEH_BRAND = a value other than \"Maserati\" (DR-PW28)\n"
                        "3. Set TBM_Present = \"Present\" (DR-PW28)\n"
                        "4. PROXI Ecall_Button_Variant = the variant for this market"),
        test_procedure=("1. Apply ENTER_FULL_OPERATION and let the HU reach the disclaimer "
                        "presentation\n"
                        f'2. Read the "Disclaimer" screen text and check that it contains {tok}{neg}'),
        expected_result=("1. The HU reaches the disclaimer presentation\n"
                         f'2. The "Disclaimer" screen text contains {tok}{neg}'))

# ── 品牌視覺：logo 群（-148、-149~152、-192~195、-155、-185）──
LOGO_NOTE = ("**R-P386 改寫（67 包）**：原 `shown logos` / `shown logo against …` 之觀察量為"
             "**規格指名之元件** (ii)（R-P384(b)：具名不以引號為要件）。"
             "前置之 `$VC_*$` 依 **R-P389(c)** 保留規格原名不加 `$`、不加 `PROXI`，附 `(DR-PW28)`；"
             "PROXI 已查得者（`Brand_Configuration_2` r566、`SDARS_Presence` r542、"
             "`Audio_Brand` r597）以 `PROXI <Param>` 寫。ITD 依 R-P366(a) 內聯。")
for tag in ("148", "149", "150", "151", "152", "192", "193", "194", "195"):
    put(tag, LOGO_NOTE,
        input_test_data="NA",
        test_procedure=("1. Set VC_VEH_BRAND = the brand under test (DR-PW28)\n"
                        "2. Apply ENTER_FULL_OPERATION and let the brand logo screen be shown\n"
                        "3. Read the brand logo screen and check which of the named logos is "
                        "shown"),
        expected_result=("1. The brand configuration is applied\n"
                         "2. The brand logo screen is shown\n"
                         "3. The logo shown on the brand logo screen is the one named for this "
                         "configuration"))
for tag in ("155", "185"):
    put(tag,
        LOGO_NOTE + " 本條之觸發為 DID 診斷寫入（`Startup Animation Selection`），"
        "**HMI Settings List 查無該條目**（67 包 §H 第 2 步實測），"
        "依 R-1 v3 (d) 保留來源名不加 `$`。",
        input_test_data="NA",
        test_procedure=("1. Write the DID Startup Animation Selection = Fiat Latam\n"
                        "2. Set VC_VEH_BRAND = a value other than Fiat (DR-PW28)\n"
                        "3. Apply ENTER_FULL_OPERATION and read the brand logo screen, and "
                        'check that the "Fiat Latam Logo" is shown in place of the vehicle '
                        "brand logo"),
        expected_result=("1. The DID is written\n2. The brand configuration is applied\n"
                         '3. The "Fiat Latam Logo" is shown on the brand logo screen in place '
                         "of the vehicle brand logo"))


def main() -> None:
    dry = "--dry-run" in sys.argv
    done = []
    for path in sorted(BATCHES.glob("batch_*.json")):
        data = json.loads(path.read_text())
        touched = False
        for tc in data["tcs"]:
            e = E.get(tc["tc_id"])
            if not e:
                continue
            touched = True
            done.append(tc["tc_id"])
            note = e.pop("note")
            tc.update(e)
            tc["reasoning_note"] = (tc.get("reasoning_note") or "") + "\n\n" + note
            tc["remarks"] = ((tc.get("remarks") or "").strip()
                             + (" " if tc.get("remarks") else "") + "(R-P386 第一批)")
        if touched and not dry:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            print(f"→ 寫回 {path.relative_to(ROOT)}")
    missing = sorted(set(E) - set(done))
    print(f"\n改寫 {len(done)} / {len(E)}；未命中 {missing or '無'}")
    if dry:
        print("（dry-run）")


if __name__ == "__main__":
    main()
