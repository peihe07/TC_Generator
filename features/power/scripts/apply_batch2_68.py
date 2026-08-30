"""68 包 §H 第 2 步 —— R-P393(b) 第二批改寫 ＋ (c) §8.3 拆分。

依 66 包 §1 表之觀察量；`-055` / `-202` 依 **R-P392**；
未查得之規格 `$X$` 依 **R-P393(a)**（保留原名不加 `$`，附 `(DR-PW28)`，不算 PENDING）；
A1 家族依 **R-P387(b)** 取 `FUNC_STATE_<STATE>`；(v) 類位準值 `PENDING: DR-PW27`。

拆分（R-P393(c)）：`-169` ＋2、`-249` ＋1、`-222`/`-223` ＋2、`-182` ＋1，tc_id 自 284 續號。

用法：
    python features/power/scripts/apply_batch2_68.py [--dry-run]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCHES = ROOT / "features/power/generated"
PS = "$STATUS_TELEMATIC.PowerSts_Telematic$"
TOOL = "1. A LIN and CAN simulation tool is connected"

E: dict[str, dict] = {}
NEW: list[dict] = []


def put(tag, note, **kw):
    E[f"NR1L-PowerManagement-{tag}"] = dict(note=note, **kw)


VC = ("**R-P393(a) / R-P389(c)**：`$VC_*$` 等未查得之規格名保留原名不加 `$`、不加 `PROXI`，"
      "附 `(DR-PW28)`；原名與值皆規格明載，缺的是載體而非資料，**不算 PENDING**。")

# ── -055：Partial Operation（FUNC_STATE）＋ chime 刺激（R-P392(a)）──
put("055",
    "**R-P386 / R-P387(b) / R-P392(a) 改寫（68 包）**：原 `AMP, ICS and DTV power states "
    "and the audio paths` 為 A1 家族。依 R-P387(b) 取 `CFTS009-4941453` 之 "
    "`Partial Operation` 列（Source OFF／AMP OFF／Display OFF `(**)`／BoosterOUT OFF／"
    "天線 ON／MCU OFF）。ANC/ACN/chime 可用之刺激依 **R-P392(a)** 取 "
    "`$PARK_INFO.ChimeActivation_LHF$`（`CM_` 逐字「chime activation request for the "
    "left hand, front audio speaker」，接收 ETM/LTM），ER 為左前喇叭有 chime 聲 (iii)。",
    input_test_data="NA",
    test_procedure=("1. Apply ENTER_PARTIAL_OPERATION\n"
                    f"2. Read the signal {PS} and check that it is 7 (Partial_Operation)\n"
                    "3. Apply FUNC_STATE_PARTIAL_OPERATION and check each of its sub-items\n"
                    "4. Send the signal $PARK_INFO.ChimeActivation_LHF$ = 1 (Active) and "
                    "check that the chime is audible on the left hand front speaker"),
    expected_result=("1. The HU is in Partial Operation\n"
                     f"2. The signal value {PS} = 7 (Partial_Operation) is received\n"
                     "3. FUNC_STATE_PARTIAL_OPERATION holds:\n"
                     "   a. No audio source is playing and no amplifier output is present\n"
                     "   b. The HU display is off, except for the HMI Antitheft Screens "
                     "(CFTS009-4941457)\n"
                     "   c. PENDING: DR-PW27 BoosterOUT OFF / antenna supply ON 位準值\n"
                     "   d. A USB device is not enumerated and the AUX input does not play\n"
                     "4. The chime is audible on the left hand front speaker"))

# ── -202：Idle（FUNC_STATE）＋ ICS 觸控座標（R-P392(b)）──
put("202",
    "**R-P386 / R-P387(b) / R-P392(b) 改寫（68 包）**：原 `ICS functions and the DTV` 為 A1 家族。"
    "依 R-P387(b) 取 `4941453` 之 `Idle` 列 —— Display `OFF (*)`，"
    "**`(*)`（`CFTS009-4941454` / `4941455`）例外含 Splash Screen visualization**，"
    "故畫面僅 `\"Splash Screen\"`；Source OFF → 無音訊 (iii)。"
    "ICS 可用之觀察依 **R-P392(b)** 取觸控座標上線："
    "`$TELEMATIC_FD_5.CM_TCH_STAT$ = 1 (TCH_PSD)` 與 `CM_TCH_X_COORD` / `CM_TCH_Y_COORD` 有值 (i)。"
    "⚠ **ICS 與 DCSD 之等同性不認定**（R-P392(b) / §I）—— 觀察面取自 `4941453` Idle 列之"
    "「DCSD sends touch coordinates」，即規格自給之該態觀察面，非以 ICS 一詞語意擇定；"
    "已併入 DR-PW29 附問。",
    input_test_data="NA",
    test_procedure=("1. Apply ENTER_IDLE\n"
                    f"2. Read the signal {PS} and check that it is 3 (Idle)\n"
                    '3. Read the HU screen and check that only the "Splash Screen" is shown '
                    "on it and no audio source is playing on the HU speakers\n"
                    "4. Touch the screen and read the bus trace, and check that "
                    "$TELEMATIC_FD_5.CM_TCH_STAT$ is 1 (TCH_PSD) and that "
                    "$TELEMATIC_FD_5.CM_TCH_X_COORD$ and $TELEMATIC_FD_5.CM_TCH_Y_COORD$ "
                    "carry the touch coordinates"),
    expected_result=("1. The HU is in Idle\n"
                     f"2. The signal value {PS} = 3 (Idle) is received\n"
                     '3. Only the "Splash Screen" is shown on the HU screen and no audio '
                     "source is playing on the HU speakers\n"
                     "4. The signal value $TELEMATIC_FD_5.CM_TCH_STAT$ = 1 (TCH_PSD) is "
                     "received together with the touch coordinates on "
                     "$TELEMATIC_FD_5.CM_TCH_X_COORD$ and $TELEMATIC_FD_5.CM_TCH_Y_COORD$"))

# ── -125：TLM OFF（FUNC_STATE_SLEEP，繫 ENTER_SLEEP → PENDING DR-PW26）──
put("125",
    "**R-P386 / R-P387(b) 改寫（68 包）**：原 `FPDM, AMP, ICS and DTV functions` 為 A1 家族，"
    "依 R-P387(b) 取 `4941453` 之 `Sleep` 列。"
    "⚠ **`ENTER_SLEEP` 之確認步不可執行**（CAN 睡眠後無法以 CAN 讀值，A-PW351），"
    "依 R-P393(b) 該項維持 `PENDING: DR-PW26`，**其餘欄位照改**。",
    input_test_data="NA",
    test_procedure=("1. Apply ENTER_STANDBY, then stop all bus activity on Body CAN and let "
                    "the network go to sleep\n"
                    "2. PENDING: DR-PW26 Sleep 態之觀察方法（CAN 睡眠後無法以 CAN 讀 "
                    f"{PS}）\n"
                    "3. Apply FUNC_STATE_SLEEP and check each of its sub-items"),
    expected_result=("1. The Body CAN goes to sleep\n"
                     "2. PENDING: DR-PW26 Sleep 態之觀察方法\n"
                     "3. FUNC_STATE_SLEEP holds:\n"
                     "   a. No audio source is playing and no amplifier output is present\n"
                     "   b. The HU display is off, except for the HMI Antitheft Screens "
                     "(CFTS009-4941457)\n"
                     "   c. PENDING: DR-PW27 BoosterOUT / antenna supply OFF 位準值\n"
                     "   d. A USB device is not enumerated and the AUX input does not play"))

# ── -081：Idle 下 rear camera（R-P380 之運行時項維持 PENDING）──
put("081",
    "**R-P386 改寫（68 包）**：原 `TLM_Status.Info and the screen content` 拆為二 —— "
    f"畫面僅 rear view camera video (ii)、`{PS} = 3 (Idle)` 不變 (i)。"
    "前置之 `Rear_View_Camera` 為 **PROXI `Format` r401 查得**（R-P377 中候選），寫 `PROXI Rear_View_Camera`。"
    "⚠ `Rear_Camera_Enable.Info` 之 `False`→`True` 為**運行時用法**，"
    "依 **R-P380(a)** 不撤 PENDING。",
    input_test_data="NA",
    pre_conditions=(f"{TOOL}\n2. Apply ENTER_IDLE\n"
                    '3. PROXI Rear_View_Camera = "Present"'),
    test_procedure=("1. PENDING: DR-PW23 Rear_Camera_Enable.Info 之驅動方法"
                    '（自 "False" 轉 "True"）\n'
                    "2. Read the HU screen and check that the rear view camera video is "
                    "shown on it\n"
                    f"3. Read the signal {PS} and check that it is still 3 (Idle)"),
    expected_result=("1. PENDING: DR-PW23 Rear_Camera_Enable.Info\n"
                     "2. The rear view camera video is shown on the HU screen\n"
                     f"3. The signal value {PS} = 3 (Idle) is still received"))

# ── -186/-187/-191：啟動音（$Themed_Sound$ 未查得 → R-P393(a)）──
for tag, setting, expect in (
    ("186", "Always", "the startup sound starts at the same time as the first frame of the "
                      "animation"),
    ("187", "Once a day", "the startup sound starts at the same time as the first frame of "
                          "the animation on the first startup of the day"),
    ("191", "Never", "no startup sound is played while the animation runs"),
):
    put(tag,
        "**R-P386 / R-P393(a) 改寫（68 包）**：原 `audio output against the animation start` "
        "非可觀察量。依 66 包 §1 表 —— 以**錄音／錄影同步**判，聲音起點與動畫第一幀同時 (iii)。"
        f"{VC} `$Themed_Sound$` 經 R-P368 全鏈與六處查詢皆未查得（止於段 1），"
        "故寫 `Set Themed_Sound = \"Fiat Latam\" (DR-PW28)`。"
        '`"Welcome Onboard Sound"` 為 HMI Settings List `Settings` r41 / r172 **查得**之條目，'
        "依 R-P375(b) 以 UI 元件寫。",
        input_test_data="NA",
        pre_conditions=(f'{TOOL}\n2. Set Themed_Sound = "Fiat Latam" (DR-PW28)\n'
                        f'3. Select "Welcome Onboard Sound" = "{setting}"'),
        test_procedure=("1. Start video and audio recording on the bench\n"
                        "2. Apply ENTER_FULL_OPERATION and let the startup animation play\n"
                        f"3. Read the recording and check that {expect}"),
        expected_result=("1. The recording is running\n2. The startup animation plays\n"
                         f"3. On the recording, {expect}"))

# ── -222/-223/-224 之 TBM_Present 項 ──
for tag, cond, text in (
    ("222", 'Set TBM_Present = "Not Present" (DR-PW28)', "the ADAS text"),
    ("223", "PROXI Country_Code = a market that requires neither SOS nor geolocation",
     "the ADAS text"),
):
    put(tag,
        "**R-P386 / R-P393(a) 改寫（68 包）**：觀察面為 `\"Disclaimer\"` 畫面之文字內容 (ii)。"
        f"{VC} ⚠ **ADAS 文字之逐字定義在 HMI 文件，該文件在 G0 台帳外** → `PENDING: DR-PW27`"
        "（與 `-216`/`-217` 之 `\"SOS\"`/`\"Help\"` 不同 —— 後者規格自給 token，ER 不 PENDING）。",
        input_test_data="NA",
        pre_conditions=(f"{TOOL}\n2. The screen size is other than 7 inch\n"
                        '3. Set VC_VEH_BRAND = a value other than "Maserati" (DR-PW28)\n'
                        f"4. {cond}"),
        test_procedure=("1. Apply ENTER_FULL_OPERATION and let the HU reach the disclaimer "
                        "presentation\n"
                        '2. Read the "Disclaimer" screen text and check the added text\n'
                        f"3. PENDING: DR-PW27 HMI disclaimer wording —— {text} 之逐字定義"),
        expected_result=("1. The HU reaches the disclaimer presentation\n"
                         '2. The "Disclaimer" screen text is read\n'
                         "3. PENDING: DR-PW27 HMI disclaimer wording"))

# ── -224：65 包已依 R-P383 改寫，本包僅訂正其前置之 `PROXI <Param>` 寫法 ──
put("224",
    "**R-P393(a) 訂正（68 包）**：本條於 65 包依 R-P383 改寫時，前置寫成 "
    "`PROXI VC_VEH_BRAND` / `PROXI TBM_Present` —— 其時 66 包 §1 表尚以 PROXI 指定該二名。"
    "67 包實測**四名皆不在 PROXI `Format`**（A-PW367 / A-PW368），"
    f"依 R-P389(c) / R-P393(a) 改為保留規格原名不加 `$`、不加 `PROXI`。{VC} "
    "`Country_Code` 為 PROXI `Format` r468 **查得**，維持 `PROXI` 寫法。",
    pre_conditions=(f"{TOOL}\n2. The screen size is other than 7 inch\n"
                    '3. Set VC_VEH_BRAND = a value other than "Maserati" (DR-PW28)\n'
                    '4. Set TBM_Present = "Present" (DR-PW28)\n'
                    "5. PROXI Country_Code = a market that requires geolocation and SOS "
                    "in the disclaimer"))

# ── 品牌指派類：theme / element / font / App icon / recirc / gauge / seat ──
ASSIGN = ("**R-P386 / R-P388 / R-P393(a) 改寫（68 包）**：觀察量為**規格指名之元件** (ii)"
          "（R-P384(b)：具名不以引號為要件，書寫依 IN §11 加引號）。"
          f"{VC} ")
PEND27 = ("⚠ **指派規則本身在台帳外文件** → 該項 `PENDING: DR-PW27`（R-P388 之分流："
          "指派在該文件者 ER PENDING）。")
NOPEND = ("⚠ **元件已由規格指名，ER 不 PENDING**；辨識參照（PDO graphics）見 DR-PW27，"
          "僅記於 Remarks（R-P388 之分流）。")

for tag, brand in (("233", "Chrysler"), ("234", "Jeep"), ("235", "Fiat")):
    put(tag, ASSIGN + NOPEND,
        input_test_data="NA",
        pre_conditions=f"{TOOL}\n2. The HU is displaying branded text",
        test_procedure=(f"1. Set VC_VEH_BRAND = \"{brand}\" (DR-PW28)\n"
                        f'2. Read the branded text on the HU screen and check that it is '
                        f'rendered in the "{brand} font"'),
        expected_result=("1. The brand configuration is applied\n"
                         f'2. The branded text is rendered in the "{brand} font"'))
for tag, brand in (("236", "Chrysler"), ("237", "Jeep"), ("238", "Fiat")):
    put(tag, ASSIGN + NOPEND,
        input_test_data="NA",
        pre_conditions=f"{TOOL}\n2. The HU is displaying the App icon",
        test_procedure=(f"1. Set VC_VEH_BRAND = \"{brand}\" (DR-PW28)\n"
                        f'2. Read the App Drawer on the HU screen and check that the '
                        f'"{brand} App icon" is shown on it'),
        expected_result=("1. The brand configuration is applied\n"
                         f'2. The "{brand} App icon" is shown in the App Drawer'))
for tag, itd in (("228", 'Set VC_SpecialPKG = "none" (DR-PW28)'),
                 ("229", "Set VC_SpecialPKG = an unsupported value (DR-PW28)")):
    put(tag, ASSIGN + PEND27,
        input_test_data="NA",
        pre_conditions=f"{TOOL}\n2. Set VC_VEH_BRAND = the configured brand (DR-PW28)",
        test_procedure=(f"1. {itd}\n"
                        "2. Read the theme applied on the HU screen\n"
                        "3. PENDING: DR-PW27 [PDO Theme Configuration] —— 該品牌之預設 theme"),
        expected_result=("1. The special package value is applied\n"
                         "2. The applied theme is read from the HU screen\n"
                         "3. PENDING: DR-PW27 [PDO Theme Configuration]"))
put("230", ASSIGN + PEND27,
    input_test_data="NA",
    pre_conditions=f"{TOOL}\n2. The HU is displaying a PDO branded element",
    test_procedure=("1. Send an unsupported CAN value for the branded element\n"
                    "2. Read the shown element on the HU screen\n"
                    "3. PENDING: DR-PW27 [PDO Theme Configuration] —— 該元件之預設值與元件清單"),
    expected_result=("1. The unsupported value is sent\n2. The shown element is read\n"
                     "3. PENDING: DR-PW27 [PDO Theme Configuration]"))
for tag, arch, cfg in (
    ("242", "the CUSW or Atlantis architecture",
     "PROXI Car_Shape_Configuration and PROXI Number_of_Doors"),
    ("243", "the PNET architecture", "Set VC_BODY_STYLE = the body style under test (DR-PW28)"),
):
    put(tag, ASSIGN + PEND27,
        input_test_data="NA",
        pre_conditions=(f"{TOOL}\n2. The HU runs {arch}\n"
                        "3. The climate screen showing the recirc icon is reachable"),
        test_procedure=(f"1. Apply the configuration: {cfg}\n"
                        "2. Read the climate screen and check which recirc icon is shown on it\n"
                        "3. PENDING: DR-PW27 HMI release —— 該組態所對應之 recirc icon 指派"),
        expected_result=("1. The configuration is applied\n"
                         "2. The recirc icon shown on the climate screen is read\n"
                         "3. PENDING: DR-PW27 HMI release"))
put("249", ASSIGN + PEND27 + " 本條為**非 M240** 支；M240 支依 R-P393(c) 另立（IN §8.3）。",
    input_test_data="NA",
    pre_conditions=(f"{TOOL}\n2. The seat settings screen is reachable\n"
                    "3. Set VC_VEH_BRAND = the configured brand (DR-PW28)"),
    test_procedure=("1. Set VC_VEH_LINE = a value other than M240 (DR-PW28)\n"
                    "2. Read the seat settings screen and check which seat graphic is shown\n"
                    "3. PENDING: DR-PW27 —— 非 M240 之 seat graphic 指派"),
    expected_result=("1. The vehicle line is applied\n2. The shown seat graphic is read\n"
                     "3. PENDING: DR-PW27"))
put("250", ASSIGN + PEND27,
    input_test_data="NA",
    pre_conditions=f"{TOOL}\n2. The performance gauges screen is reachable",
    test_procedure=("1. Set VC_VEH_LINE = the vehicle line under test (DR-PW28)\n"
                    "2. Read the performance gauges screen and check which gauges are shown\n"
                    "3. PENDING: DR-PW27 —— 該 vehicle line 之 gauges 指派"),
    expected_result=("1. The vehicle line is applied\n2. The shown gauges are read\n"
                     "3. PENDING: DR-PW27"))

# ── -281：Bench 態（(v) 類）──
put("281",
    "**R-P386 / R-P387(a)(b) 改寫（68 包）**：三個原 `<X>` 皆 A1 家族，依 R-P387(b) 取 "
    "`4941453` 之 `Bench` 列。AMP → 音源播放有聲 (iii)；**BoosterOUT 與天線供電為 (v) 類"
    "電氣量測**，其 ON 位準值規格未載（`4941453` 逐字為 `ON Refer to {CFTS024}…`）→ "
    "`PENDING: DR-PW27`，**不得自造位準**（R-P387(a) / §I）；"
    "USB → 插入後被列舉／可播放 (iii)；AUX → 播放有聲 (iii)。",
    input_test_data="NA",
    test_procedure=("1. Apply ENTER_BENCH\n"
                    f"2. Read the signal {PS} and check that it is 6 (Bench)\n"
                    "3. Read the HU speakers and check that the audio active source is "
                    "playing on them\n"
                    "4. PENDING: DR-PW27 BoosterOUT / analog and digital antenna supply 之 "
                    "ON 位準值 —— measure the voltage at each output and check it against "
                    "that level\n"
                    "5. Insert a USB device and check that it is enumerated and can be "
                    "played, and check that the AUX input plays on the HU speakers"),
    expected_result=("1. The HU is in Bench\n"
                     f"2. The signal value {PS} = 6 (Bench) is received\n"
                     "3. The audio active source is playing on the HU speakers\n"
                     "4. PENDING: DR-PW27 BoosterOUT / antenna supply ON 位準值\n"
                     "5. The USB device is enumerated and can be played, and the AUX input "
                     "plays on the HU speakers"))

# ── -182：30 分鐘支（拆分之保留支）──
put("182",
    "**R-P386 / R-P393(c) 改寫（68 包）**：原 `screen against the elapsed time` 非可觀察量。"
    "依 66 包 §1 表拆二 —— **本條為 30 分鐘支**，下一喚醒週期支另立（IN §8.3）。"
    f"{VC} `$Door_Ajar_Status$` 止於段 2（LID r474 有列而 `Atlantis High` 欄空），"
    "依 R-P393(a) 保留原名。",
    input_test_data="NA",
    pre_conditions=(f"{TOOL}\n2. The HU has just played a start-up animation\n"
                    "3. All other conditions for the animation hold"),
    test_procedure=("1. Set Door_Ajar_Status = \"Open\" then \"Closed\" again within the "
                    "same CAN wakeup cycle (DR-PW28)\n"
                    "2. Read the HU screen and check that no start-up animation is played\n"
                    "3. Hold for 1800000 ms, repeat the door event, then read the HU screen "
                    "and check that the start-up animation is played"),
    expected_result=("1. The door event is registered within the same CAN wakeup cycle\n"
                     "2. No start-up animation is played on the HU screen\n"
                     "3. After 1800000 ms the start-up animation is played on the HU screen"))


def clone(src: dict, new_tag: str, title: str, note: str, **kw) -> dict:
    tc = json.loads(json.dumps(src))
    tc["tc_id"] = f"NR1L-PowerManagement-{new_tag}"
    tc["tc_title"] = title
    tc.update(kw)
    tc["reasoning_note"] = (src.get("reasoning_note") or "") + "\n\n" + note
    tc["remarks"] = "(R-P393(c) §8.3 拆分增列；本條與 " + src["tc_id"] + " 同錨點)"
    return tc


def main() -> None:
    dry = "--dry-run" in sys.argv
    files = {p: json.loads(p.read_text()) for p in sorted(BATCHES.glob("batch_*.json"))}
    idx = {tc["tc_id"]: (p, tc) for p, d in files.items() for tc in d["tcs"]}

    done = []
    for tid, e in E.items():
        if tid not in idx:
            continue
        _, tc = idx[tid]
        note = e.pop("note")
        tc.update(e)
        tc["reasoning_note"] = (tc.get("reasoning_note") or "") + "\n\n" + note
        tc["remarks"] = ((tc.get("remarks") or "").strip()
                         + (" " if tc.get("remarks") else "") + "(R-P386 第二批)")
        done.append(tid)

    # ── §8.3 拆分（R-P393(c)）──
    splits = [
        ("NR1L-PowerManagement-169", "284",
         "A dismissed FOTA pop up passes the TLM to Standby",
         "**R-P393(c) §8.3 拆分**：`-169` 之三個離開條件各一 TC；本條為 "
         "**FOTA pop-up dismissed 支**。",
         dict(test_procedure=("1. PENDING: DR-PW27 CFTS057 —— FOTA update available 之建立方法\n"
                              "2. Apply ENTER_TIMED\n"
                              '3. Read the HU screen and check that the "FOTA update '
                              'available" pop-up is shown\n'
                              "4. Dismiss the pop-up through the HMI, then read the HU screen "
                              "and check that it is no longer shown\n"
                              f"5. Read the signal {PS} and check that it is 1 (Standby)"),
              expected_result=("1. PENDING: DR-PW27 CFTS057\n2. The HU is in Timed\n"
                               '3. The "FOTA update available" pop-up is shown\n'
                               "4. The pop-up is no longer shown on the HU screen\n"
                               f"5. The signal value {PS} = 1 (Standby) is received"))),
        ("NR1L-PowerManagement-169", "285",
         "An accessory delay going inactive passes the TLM to Standby",
         "**R-P393(c) §8.3 拆分**：`-169` 之第三個離開條件 —— "
         "`$ACCDlyAct$` active→inactive 支。該名經 R-P368 段 1 命中 LID r29 `AccDelayAct`，"
         "惟其 `Atlantis High` 欄為 `N/A`（止於段 2）；FD 側同義訊號為 "
         "`$BCM_FD_27.Comfort_Enable_Act$`（`CM_` = `Accessory Delay Active`，R-P371 型證據）。",
         dict(test_procedure=("1. PENDING: DR-PW27 CFTS057 —— FOTA update available 之建立方法\n"
                              "2. Apply ENTER_TIMED with $BCM_FD_27.Comfort_Enable_Act$ = 1 "
                              "(DR-PW26)\n"
                              '3. Read the HU screen and check that the "FOTA update '
                              'available" pop-up is shown\n'
                              "4. Send the signal $BCM_FD_27.Comfort_Enable_Act$ = 0 (DR-PW26)\n"
                              f"5. Read the signal {PS} and check that it is 1 (Standby)"),
              expected_result=("1. PENDING: DR-PW27 CFTS057\n2. The HU is in Timed\n"
                               '3. The "FOTA update available" pop-up is shown\n'
                               "4. The signal value $BCM_FD_27.Comfort_Enable_Act$ = 0 is "
                               "received\n"
                               f"5. The signal value {PS} = 1 (Standby) is received"))),
        ("NR1L-PowerManagement-249", "286",
         "An M240 vehicle line uses the M240 seat graphics",
         "**R-P393(c) §8.3 拆分**：`-249` 之 **M240 支**（原條為非 M240 支）。",
         dict(test_procedure=("1. Set VC_VEH_LINE = \"M240\" (DR-PW28)\n"
                              "2. Read the seat settings screen and check that the "
                              '"M240 seat graphics" are shown on it'),
              expected_result=("1. The vehicle line is applied\n"
                               '2. The "M240 seat graphics" are shown on the seat settings '
                               "screen"))),
        ("NR1L-PowerManagement-182", "287",
         "A start-up animation plays again in the next wakeup cycle",
         "**R-P393(c) §8.3 拆分**：`-182` 之 **下一喚醒週期支**（原條為 30 分鐘支）。"
         "⚠ 喚醒週期須經 `ENTER_SLEEP`，其確認步 `PENDING: DR-PW26`（A-PW351）。",
         dict(test_procedure=("1. Set Door_Ajar_Status = \"Open\" then \"Closed\" again "
                              "within the same CAN wakeup cycle (DR-PW28)\n"
                              "2. Read the HU screen and check that no start-up animation "
                              "is played\n"
                              "3. PENDING: DR-PW26 Sleep 態之觀察方法 —— let the Body CAN go "
                              "to sleep and wake it again to start a new wakeup cycle\n"
                              "4. Repeat the door event and read the HU screen, and check "
                              "that the start-up animation is played"),
              expected_result=("1. The door event is registered within the same CAN wakeup "
                               "cycle\n2. No start-up animation is played\n"
                               "3. PENDING: DR-PW26 Sleep 態之觀察方法\n"
                               "4. The start-up animation is played on the HU screen in the "
                               "new wakeup cycle"))),
    ]
    for src_id, tag, title, note, kw in splits:
        p, src = idx[src_id]
        NEW.append((p, clone(src, tag, title, note, **kw)))

    for p, tc in NEW:
        files[p]["tcs"].append(tc)

    print(f"第二批改寫 {len(done)} / {len(E)}；未命中 "
          f"{sorted(set(E) - set(done)) or '無'}")
    print(f"§8.3 拆分增列 {len(NEW)} 條："
          f"{'、'.join(tc['tc_id'][-3:] for _, tc in NEW)}")
    if not dry:
        for p, d in files.items():
            p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        print("已寫回")
    else:
        print("（dry-run）")


if __name__ == "__main__":
    main()
