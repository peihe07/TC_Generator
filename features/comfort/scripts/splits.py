#!/usr/bin/env python3
"""Enumerated-trigger splits (handoff 75 §1 / 76 §2).

One place for every leaf whose clause **lists its triggers word for word**.
75 §1's criterion: N triggers named in the requirement -> N test cases; a
general phrase plus samples of our own choosing -> one test case, the samples
being interaction data. The quote below each leaf is what makes the split
auditable — if the criterion is ever revised, the quote is what gets re-read.

Each entry holds:
    quote    the clause's enumeration, verbatim (goes into split_reason)
    why      one sentence on how the triggers fail independently
    variants [0] replaces the leaf's existing TC, [1:] are new rows.
             Each variant carries its own title / procedure / expected_result;
             everything else (pre_conditions, spec_ref, EMEA review) is
             inherited from the existing TC, because a split shares the leaf's
             context and differs only in what is pressed.
             `extra_pc` adds a pre_condition line where the split's own
             trigger needs equipment the base TC did not (R-C28 Q1, 76 §2.1).

Late tc_ids: assigned from FIRST_N upward in a fixed order, so existing rows
never renumber (65 §1) and re-runs are stable.

FIRST_N is a boundary value, and R-C43 says boundary values are to be replaced
by identity. It stays, for two reasons, and 77 §2 認可 both:

  1. It does not decide membership — the SPLITS keys do. It decides only where
     new numbers start, and its failure mode (a collision) is caught loudly by
     the `tc-id-sequence` gate. R-C43 guards against SILENT failure.
  2. **The stronger reason (77 §2):** deriving the start from `max(tc_id)` in
     the corpus would make tc_ids depend on GENERATION ORDER — running A then B
     would number differently from B then A. A tc_id must be deterministic, and
     a fixed start plus a loud collision check is more deterministic than one
     derived from the corpus.

Usage (in a generator, right before writing the doc):
    from splits import apply_splits
    tcs = apply_splits(tcs)
"""

FIRST_N = 386
TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"

REASON = ("§8.2.2 之拆分，依 75 §1 之判準（**條文列舉之項即拆分之維度**）："
          "本節之條文逐字列舉其觸發 —— 「{quote}」—— 故一觸發一條。{why} "
          "（**判準之反面**：條文以泛稱表述而由作者挑樣者不拆，其樣本為 "
          "interaction data，§4.5。）")

SPLITS = {
 # ---------------------------------------------------------------- 2.3 / 16.3
 "SWE1-HVAC-003-06": dict(
   quote="Manually selecting A/C, switching to another airflow mode "
         "(including front defrost), or changing fan speeds breaks Auto",
   why="三個觸發各自可失效：A/C 破壞而模式不破壞，是一種失效；反之亦然。",
   variants=[
     ("Pressing A/C breaks AUTO",
      ["1. Turn AUTO on from the climate screen", "2. Press \"A/C\""],
      ["1. The \"AUTO\" button is highlighted",
       "2. The \"AUTO\" button is no longer highlighted"]),
     ("Selecting another airflow mode breaks AUTO",
      ["1. Turn AUTO on from the climate screen",
       "2. Select another airflow mode"],
      ["1. The \"AUTO\" button is highlighted",
       "2. The \"AUTO\" button is no longer highlighted"]),
     ("Changing the fan speed breaks AUTO",
      ["1. Turn AUTO on from the climate screen", "2. Change the fan speed"],
      ["1. The \"AUTO\" button is highlighted",
       "2. The \"AUTO\" button is no longer highlighted"]),
   ]),
 "SWE1-HVAC-107-06": dict(
   quote="Pressing MAX DEF or Max A/C the system goes to that function",
   why="兩個按鍵各自可失效，且其落點不同（MAX A/C 與 MAX DEF 為兩個功能）。",
   variants=[
     ("Pressing MAX A/C takes the system to MAX A/C",
      ["1. Turn AUTO on from the climate screen", "2. Press \"MAX A/C\""],
      ["1. The \"AUTO\" button is highlighted",
       "2. The \"MAX A/C\" button is highlighted and \"AUTO\" is not"]),
     ("Pressing MAX DEF takes the system to MAX DEF",
      ["1. Turn AUTO on from the climate screen", "2. Press \"MAX DEF\""],
      ["1. The \"AUTO\" button is highlighted",
       "2. The \"MAX DEF\" button is highlighted and \"AUTO\" is not"]),
   ]),
 "SWE1-HVAC-107-07": dict(
   quote="Manually changing airflow mode or changing fan speeds breaks Auto",
   why="兩個觸發各自可失效。",
   variants=[
     ("Changing the airflow mode breaks AUTO",
      ["1. Turn AUTO on from the climate screen",
       "2. Select another airflow mode"],
      ["1. The \"AUTO\" button is highlighted",
       "2. The \"AUTO\" button is no longer highlighted"]),
     ("Changing the fan speed breaks AUTO",
      ["1. Turn AUTO on from the climate screen", "2. Change the fan speed"],
      ["1. The \"AUTO\" button is highlighted",
       "2. The \"AUTO\" button is no longer highlighted"]),
   ]),
 # ---------------------------------------------------------------- 2.6 / 7.4 / 16.6
 "SWE1-HVAC-008-02": dict(
   quote="when at the Highest possible position display HI when at the "
         "lowest display LO",
   why="兩個端點各自可失效：HI 正確而 LO 顯示度數，是一種失效。",
   variants=[
     ("HI replaces the degree value at the highest position",
      ["1. Set the temperature to the highest possible position",
       "2. Read the temperature on the climate screen"],
      ["1. The temperature is at its highest possible position",
       "2. The climate screen shows HI instead of a degree value"]),
     ("LO replaces the degree value at the lowest position",
      ["1. Set the temperature to the lowest position",
       "2. Read the temperature on the climate screen"],
      ["1. The temperature is at its lowest position",
       "2. The climate screen shows LO instead of a degree value"]),
   ]),
 "SWE1-HVAC-032-01": dict(
   quote="Temperature will display the current degree … when at the Highest "
         "possible position display HI when at the lowest display LO instead "
         "of a degree value",
   why="三個值域點各自可失效。",
   variants=[
     ("The rear temperature shows the set degree inside the range",
      ["1. Set the rear temperature to a value inside the range",
       "2. Read the rear climate screen"],
      ["1. The rear temperature is set to a value inside the range",
       "2. The rear climate screen shows the set degree value"]),
     ("HI replaces the rear degree value at the highest position",
      ["1. Set the rear temperature to the highest possible position",
       "2. Read the rear climate screen"],
      ["1. The rear temperature is at its highest possible position",
       "2. The rear climate screen shows \"HI\" instead of a degree value"]),
     ("LO replaces the rear degree value at the lowest position",
      ["1. Set the rear temperature to the lowest possible position",
       "2. Read the rear climate screen"],
      ["1. The rear temperature is at its lowest possible position",
       "2. The rear climate screen shows \"LO\" instead of a degree value"]),
   ]),
 "SWE1-HVAC-110-01": dict(
   quote="Temperature ranges: LO, 60-84, HI (English), LO, 16-28, HI (Metric)",
   why="兩個單位制為兩組不同之值域，其換算與顯示各自可失效。",
   variants=[
     ("The English temperature range runs LO, 60 to 84, HI",
      ["1. Set the temperature units to English and open the climate screen",
       "2. Adjust the temperature across its whole range"],
      ["1. The climate screen shows the temperature setting",
       "2. The settings available are LO, 60 to 84, HI"]),
     ("The Metric temperature range runs LO, 16 to 28, HI",
      ["1. Set the temperature units to Metric and open the climate screen",
       "2. Adjust the temperature across its whole range"],
      ["1. The climate screen shows the temperature setting",
       "2. The settings available are LO, 16 to 28, HI"]),
   ]),
 # ---------------------------------------------------------------- 2.6.1 / 16.6.1
 "SWE1-HVAC-009-03": dict(
   quote="move 1 increment up/down per press",
   why="兩個方向各自可失效：上箭頭正確而下箭頭跳兩格，是一種失效。",
   variants=[
     ("The up arrow moves the temperature one increment up",
      ["1. Open the climate screen",
       "2. Press the temperature up arrow once"],
      ["1. The climate screen shows the current temperature",
       "2. The temperature moves up by 1 increment"]),
     ("The down arrow moves the temperature one increment down",
      ["1. Open the climate screen",
       "2. Press the temperature down arrow once"],
      ["1. The climate screen shows the current temperature",
       "2. The temperature moves down by 1 increment"]),
   ]),
 "SWE1-HVAC-009-05": dict(
   quote="The system can jump to a value as well via touching a spot in a "
         "slider bar or voice command",
   why="兩條輸入路徑各自可失效，且其實作不同（觸控 vs 語音）。",
   variants=[
     ("The temperature jumps to a touched spot on the slider",
      ["1. Note the temperature shown on the climate screen",
       "2. Touch a spot in the temperature slider bar"],
      ["1. The climate screen shows the current temperature",
       "2. The temperature jumps to the value at the touched spot"]),
     ("The temperature jumps to a value given by voice",
      ["1. Note the temperature shown on the climate screen",
       "2. Set the temperature to a value by voice command"],
      ["1. The climate screen shows the current temperature",
       "2. The temperature jumps to the value given by voice command"]),
   ]),
 "SWE1-HVAC-009-06": dict(
   quote="User must press slider handle to move temperature slider position; "
         "if user initially presses slider area outside of handle …, ignore "
         "the press",
   why="正向（把手可拖曳）與否定側（把手外之按壓被忽略）各自可失效。",
   variants=[
     ("The slider handle moves the temperature slider position",
      ["1. Note the temperature slider position",
       "2. Press the temperature slider handle and move it"],
      ["1. The climate screen shows the temperature slider",
       "2. The temperature slider position moves"]),
     ("A press outside the slider handle is ignored",
      ["1. Press the slider area to the left of the slider handle",
       "2. Read the temperature slider position"],
      ["1. The press is on the slider area outside the handle",
       "2. The temperature slider position does not change"]),
   ]),
 "SWE1-HVAC-111-03": dict(
   quote="Change temperature on climate screen by using arrows … or slider … "
         "The system can jump to a value as well via … or voice command",
   why="三條輸入路徑各自可失效。",
   variants=[
     ("The arrows move the temperature one increment",
      ["1. Note the temperature shown on the climate screen",
       "2. Press the temperature up arrow on the climate screen"],
      ["1. The climate screen shows the current temperature",
       "2. The temperature moves 1 increment up"]),
     ("The slider moves the temperature and shows the TEMP pop-up",
      ["1. Note the temperature shown on the climate screen",
       "2. Touch the slider handle and drag it to another value"],
      ["1. The climate screen shows the current temperature",
       "2. The temperature follows the slider handle, and a TEMP pop-up is "
       "shown next to the slider"]),
     ("The temperature jumps to a value given by voice",
      ["1. Note the temperature shown on the climate screen",
       "2. Set the temperature to a value by voice command"],
      ["1. The climate screen shows the current temperature",
       "2. The temperature jumps to the value given by voice command"]),
   ]),
 "SWE1-HVAC-111-05": dict(
   quote="User must press slider handle to move temperature slider position; "
         "if user initially presses slider area outside of handle …, ignore "
         "the press",
   why="正向與否定側各自可失效。",
   variants=[
     ("A press outside the slider handle is ignored",
      ["1. Press the slider area to the left of the slider handle",
       "2. Read the temperature slider position"],
      ["1. The press is on the slider area outside the handle",
       "2. The temperature slider position does not move"]),
     ("The slider handle moves the temperature slider position",
      ["1. Note the temperature slider position",
       "2. Press the slider handle and drag it"],
      ["1. The climate screen shows the temperature slider",
       "2. The temperature slider position follows the handle"]),
   ]),
 # ---------------------------------------------------------------- 2.7 / 16.7
 "SWE1-HVAC-010-03": dict(
   quote="user can either use Fan up/down (minus/plus) buttons, directly "
         "touch a fan segment to jump or slide, or use Hard Control",
   why="三條輸入路徑各自可失效（按鍵可用而滑動失效，是一種失效）。",
   variants=[
     ("The fan up button increases the fan speed",
      ["1. Note the fan speed shown on the climate screen",
       "2. Press the fan up button on the climate screen"],
      ["1. The climate screen shows the current fan speed",
       "2. The fan speed increases"]),
     ("Touching a fan segment jumps the fan speed to it",
      ["1. Note the fan speed shown on the climate screen",
       "2. Touch a fan segment on the climate screen"],
      ["1. The climate screen shows the current fan speed",
       "2. The fan speed jumps to the touched segment"]),
     ("Sliding across the fan segments follows the slide",
      ["1. Note the fan speed shown on the climate screen",
       "2. Slide across the fan segments on the climate screen"],
      ["1. The climate screen shows the current fan speed",
       "2. The fan speed follows the slide"]),
   ]),
 "SWE1-HVAC-010-04": dict(
   quote="The user shall not be able to turn the FAN off by using the FAN "
         "controls on the screen or the FAN hard control",
   why="兩個控制面各自可失效：畫面上關不掉而硬控關得掉，是一種失效。",
   variants=[
     ("The screen fan controls cannot turn the fan off",
      ["1. Note the fan speed shown on the climate screen",
       "2. Press the fan down button on the climate screen repeatedly until "
       "the fan speed stops decreasing"],
      ["1. The climate screen shows the current fan speed",
       "2. The fan is not off and one fan bar remains highlighted"]),
     ("The fan hard control cannot turn the fan off",
      ["1. Note the fan speed shown on the climate screen",
       "2. Turn the fan speed hard control down repeatedly until the fan "
       "speed stops decreasing"],
      ["1. The climate screen shows the current fan speed",
       "2. The fan is not off and one fan bar remains highlighted"]),
   ]),
 "SWE1-HVAC-112-04": dict(
   quote="user can either use Fan up/down buttons, directly touch a fan "
         "segment to jump or slide, or use Hard Control",
   why="四條輸入路徑各自可失效。",
   variants=[
     ("The fan up button increases the fan speed",
      ["1. Note the fan speed shown on the climate screen",
       "2. Press the fan up button on the climate screen"],
      ["1. The climate screen shows the current fan speed",
       "2. The fan speed increases"]),
     ("Touching a fan segment jumps the fan speed to it",
      ["1. Note the fan speed shown on the climate screen",
       "2. Touch a fan segment on the climate screen"],
      ["1. The climate screen shows the current fan speed",
       "2. The fan speed jumps to the touched segment"]),
     ("Sliding across the fan segments follows the slide",
      ["1. Note the fan speed shown on the climate screen",
       "2. Slide across the fan segments on the climate screen"],
      ["1. The climate screen shows the current fan speed",
       "2. The fan speed follows the slide"]),
     ("The fan hard control changes the fan speed",
      ["1. Note the fan speed shown on the climate screen",
       "2. Change the fan speed using the fan speed hard control"],
      ["1. The climate screen shows the current fan speed",
       "2. The fan speed follows the hard control"]),
   ]),
 "SWE1-HVAC-112-05": dict(
   quote="The user shall not be able to turn the FAN off by using the FAN "
         "controls on the screen or the FAN hard control",
   why="兩個控制面各自可失效；其唯一例外（關閉 CLIMATE 系統）由同節之另一句所述，見 `112-05` 之第三步原為該例外。",
   variants=[
     ("The screen fan controls cannot turn the fan off",
      ["1. Note the fan speed shown on the climate screen",
       "2. Press the fan down button on the climate screen repeatedly until "
       "the fan speed stops decreasing"],
      ["1. The climate screen shows the current fan speed",
       "2. The fan is not off and one fan bar remains highlighted"]),
     ("The fan hard control cannot turn the fan off",
      ["1. Note the fan speed shown on the climate screen",
       "2. Turn the fan speed hard control down repeatedly until the fan "
       "speed stops decreasing"],
      ["1. The climate screen shows the current fan speed",
       "2. The fan is not off and one fan bar remains highlighted"]),
   ]),
 # ---------------------------------------------------------------- 2.8
 "SWE1-HVAC-012-05": dict(
   quote="Auto turns Defrost off. Turning Defrost on while in Auto will "
         "break Auto and turn it off",
   why="兩個方向各自可失效：AUTO 關得掉 Defrost 而 Defrost 關不掉 AUTO，是一種失效。",
   variants=[
     ("Turning AUTO on turns Defrost off",
      ["1. Turn \"FRONT DEF\" on from the climate screen",
       "2. Turn AUTO on and read the \"FRONT DEF\" button"],
      ["1. The \"FRONT DEF\" button is highlighted",
       "2. The \"FRONT DEF\" button is no longer highlighted"]),
     ("Turning Defrost on while in AUTO breaks AUTO",
      ["1. Turn AUTO on from the climate screen",
       "2. Turn \"FRONT DEF\" on and read the \"AUTO\" button"],
      ["1. The \"AUTO\" button is highlighted",
       "2. The \"AUTO\" button is no longer highlighted"]),
   ]),
 # ---------------------------------------------------------------- 3.1
 "SWE1-HVAC-023-01": dict(
   quote="there are 3 airflow mode buttons (Windshield, Face, Feet) … Each "
         "Mode button can be pressed to individually toggle ON / OFF",
   why="三個鍵各自可失效，且條文明寫 `Each … individually`。",
   variants=[
     ("The Face mode button toggles independently",
      ["1. Open the Tri-Mode Climate screen",
       "2. Press the \"Face\" mode button",
       "3. Press the \"Face\" mode button again"],
      ["1. The Tri-Mode Climate screen shows the \"Windshield\", \"Face\" "
       "and \"Feet\" mode buttons",
       "2. The Face mode is toggled ON and the Windshield and Feet modes are "
       "unchanged",
       "3. The Face mode is toggled OFF and the Windshield and Feet modes "
       "are unchanged"]),
     ("The Feet mode button toggles independently",
      ["1. Open the Tri-Mode Climate screen",
       "2. Press the \"Feet\" mode button",
       "3. Press the \"Feet\" mode button again"],
      ["1. The Tri-Mode Climate screen shows the three mode buttons",
       "2. The Feet mode is toggled ON and the Windshield and Face modes are "
       "unchanged",
       "3. The Feet mode is toggled OFF and the Windshield and Face modes "
       "are unchanged"]),
     ("The Windshield mode button toggles independently",
      ["1. Open the Tri-Mode Climate screen",
       "2. Press the \"Windshield\" mode button",
       "3. Press the \"Windshield\" mode button again"],
      ["1. The Tri-Mode Climate screen shows the three mode buttons",
       "2. The Windshield mode is toggled ON and the Face and Feet modes are "
       "unchanged",
       "3. The Windshield mode is toggled OFF and the Face and Feet modes "
       "are unchanged"]),
   ]),
 "SWE1-HVAC-023-03": dict(
   quote="Toggling UP (or RIGHT) moves forward in the order and toggling "
         "DOWN (or LEFT) moves backwards through the cycle",
   why="兩個方向各自可失效：向前正確而向後跳兩格，是一種失效。",
   variants=[
     ("Toggling the MODE control up moves forward in the order",
      ["1. Toggle the MODE control repeatedly until the Face mode alone is "
       "active",
       "2. Toggle the MODE control UP (or RIGHT)",
       "3. Toggle the MODE control UP (or RIGHT)"],
      ["1. Only the Face mode is active",
       "2. The Face and Feet modes are active",
       "3. Only the Feet mode is active"]),
     ("Toggling the MODE control down moves backwards in the order",
      ["1. Toggle the MODE control repeatedly until the Feet mode alone is "
       "active",
       "2. Toggle the MODE control DOWN (or LEFT)",
       "3. Toggle the MODE control DOWN (or LEFT)"],
      ["1. Only the Feet mode is active",
       "2. The Face and Feet modes are active",
       "3. Only the Face mode is active"]),
   ]),
 # ---------------------------------------------------------------- 7.3 / 7.4
 "SWE1-HVAC-031-01": dict(
   quote="While unlocked = Lock Rear text with unlocked Lock icon, While "
         "locked = Unlock Rear text with the Lock icon",
   why="鎖與解鎖為兩個觸發，其後果相反且各自可失效。",
   variants=[
     ("LOCK REAR locks out the rear climate controls",
      ["1. Press \"LOCK REAR\"", "2. Operate a rear climate control"],
      ["1. The rear climate is locked",
       "2. The rear climate control has no effect"]),
     ("UNLOCK REAR restores the rear climate controls",
      ["1. Press \"LOCK REAR\", then press \"UNLOCK REAR\"",
       "2. Operate a rear climate control"],
      ["1. The rear climate is unlocked",
       "2. The rear climate control takes effect"]),
   ]),
 "SWE1-HVAC-032-04": dict(
   quote="If SYNC is ON, adjusting driver temperature affects passenger "
         "temperatures, adjusting passenger temperatures would break SYNC",
   why="兩個觸發之後果相反（連動 vs 中斷），各自可失效。",
   variants=[
     ("With SYNC on the driver temperature drives the passenger",
      ["1. Turn SYNC on", "2. Change the driver temperature"],
      ["1. The SYNC button is highlighted",
       "2. The passenger temperature follows the driver temperature"]),
     ("Adjusting the passenger temperature breaks SYNC",
      ["1. Turn SYNC on", "2. Change the passenger temperature"],
      ["1. The SYNC button is highlighted",
       "2. SYNC is turned off and the SYNC button is no longer highlighted"]),
   ]),
 "SWE1-HVAC-033-01": dict(
   quote="Fan ranges: Off, 1-7, 15h (denoting to show AUTO instead)",
   why="`1-7` 與 `15h` 為本 leaf 之觸發可達之兩個值域區段，各自可失效；"
       "**`Off` 不在其中** —— 見該條之 reasoning：條文另明寫「使用者不得以畫面上之 "
       "FAN 控制關閉風扇，唯一使全部風速格變暗之途徑為關閉 CLIMATE 系統」，"
       "故 `Off` 之觸發屬 `033-04`（climate off），不在本 leaf 之射程內。"
       "**值域之列舉與觸發之列舉外觀相同而處置相反。**",
   variants=[
     ("The rear fan range covers 1 through 7",
      ["1. Set the rear fan speed to 1", "2. Set the rear fan speed to 7"],
      ["1. The rear fan speed indicator shows 1",
       "2. The rear fan speed indicator shows 7"]),
     ("15h shows AUTO instead of a fan speed",
      ["1. Turn rear AUTO on", "2. Read the rear fan speed indicator"],
      ["1. The rear AUTO button is highlighted",
       "2. The rear fan speed indicator shows AUTO"]),
   ]),
 # ---------------------------------------------------------------- 7.8
 "SWE1-HVAC-036-01": dict(
   quote="The Rear Airflow Modes has 3 states: 1) Feet, 2) Face + Feet, "
         "3) Face",
   why="三個狀態各自可失效（Feet 可選而 Face + Feet 選不到，是一種失效）。",
   variants=[
     ("The rear Feet mode can be selected",
      ["1. Select the rear Feet mode", "2. Read the rear airflow mode"],
      ["1. The rear Feet mode is selected",
       "2. The rear airflow mode is Feet"]),
     ("The rear Face plus Feet mode can be selected",
      ["1. Select the rear Face + Feet mode",
       "2. Read the rear airflow mode"],
      ["1. The rear Face + Feet mode is selected",
       "2. The rear airflow mode is Face + Feet"]),
     ("The rear Face mode can be selected",
      ["1. Select the rear Face mode", "2. Read the rear airflow mode"],
      ["1. The rear Face mode is selected",
       "2. The rear airflow mode is Face"]),
   ]),
 "SWE1-HVAC-036-05": dict(
   quote="If the Rear Mode hard control is pressed the user will be moved to "
         "the next mode available in the loop … press and hold of the control "
         "will only move one mode over, it will not continue to move through "
         "modes",
   why="按壓與長按為兩個輸入，其後果不同（前進一格 vs 只前進一格且不連續）。",
   variants=[
     ("A press of the rear Mode hard control moves one mode on",
      ["1. Press the rear Mode hard control",
       "2. Press the rear Mode hard control again"],
      ["1. The rear airflow mode moves to the next mode available in the loop",
       "2. The rear airflow mode moves to the next mode available in the "
       "loop"]),
     ("A press and hold moves only one mode over",
      ["1. Press and hold the rear Mode hard control",
       "2. Read the rear airflow mode"],
      ["1. The rear Mode hard control is held",
       "2. The rear airflow mode moves one mode over and does not continue "
       "through the modes"]),
   ]),
 # ---------------------------------------------------------------- 14.18
 "SWE1-HVAC-103-02": dict(
   quote="Popup will have a 5 sec timeout and restart with additional presses",
   why="逾時與重計為兩個行為：逾時正確而重計失效，popup 會提早消失。",
   variants=[
     ("The comfort popup times out after five seconds",
      ["1. Press the driver comfort seat icon in the status bar",
       "2. Wait 5 seconds without further interaction"],
      ["1. A popup for the comfort feature is shown",
       "2. The popup is no longer shown"]),
     ("An additional press restarts the popup timeout",
      ["1. Press the driver comfort seat icon in the status bar",
       "2. Press the icon again just before the popup times out",
       "3. Wait 5 seconds without further interaction"],
      ["1. A popup for the comfort feature is shown",
       "2. The popup is still shown",
       "3. The popup is no longer shown"]),
   ]),
 # ---------------------------------------------------------------- 16.8 / 16.13
 "SWE1-HVAC-113-09": dict(
   quote="Changing temperature, recirculation, mode distribution or pressing "
         "again MAX DEF break MAX DEF",
   why="四個觸發各自可失效。",
   variants=[
     ("Changing the temperature breaks MAX DEF",
      ["1. Select a known airflow mode, then press \"MAX DEF\"",
       "2. Change the temperature and read the \"MAX DEF\" button"],
      ["1. The \"MAX DEF\" button is highlighted",
       "2. \"MAX DEF\" is no longer highlighted and the airflow mode is the "
       "one selected in step 1"]),
     ("Changing recirculation breaks MAX DEF",
      ["1. Select a known airflow mode, then press \"MAX DEF\"",
       "2. Change RECIRC and read the \"MAX DEF\" button"],
      ["1. The \"MAX DEF\" button is highlighted",
       "2. \"MAX DEF\" is no longer highlighted and the airflow mode is the "
       "one selected in step 1"]),
     ("Changing the mode distribution breaks MAX DEF",
      ["1. Select a known airflow mode, then press \"MAX DEF\"",
       "2. Select another airflow mode and read the \"MAX DEF\" button"],
      ["1. The \"MAX DEF\" button is highlighted",
       "2. \"MAX DEF\" is no longer highlighted"]),
     ("Pressing MAX DEF again breaks MAX DEF",
      ["1. Press \"MAX DEF\" on the climate screen",
       "2. Press \"MAX DEF\" again and read the button"],
      ["1. The \"MAX DEF\" button is highlighted",
       "2. The \"MAX DEF\" button is no longer highlighted"]),
   ]),
 "SWE1-HVAC-119-08": dict(
   quote="Changing temperature, recirculation, mode distribution, or pressing "
         "MAX A/C again shall turn MAX A/C off",
   why="四個觸發各自可失效。",
   variants=[
     ("Changing the temperature turns MAX A/C off",
      ["1. Press \"MAX A/C\" on the climate screen",
       "2. Change the temperature and read the \"MAX A/C\" button"],
      ["1. The \"MAX A/C\" button is highlighted",
       "2. The \"MAX A/C\" button is no longer highlighted"]),
     ("Changing recirculation turns MAX A/C off",
      ["1. Press \"MAX A/C\" on the climate screen",
       "2. Change RECIRC and read the \"MAX A/C\" button"],
      ["1. The \"MAX A/C\" button is highlighted",
       "2. The \"MAX A/C\" button is no longer highlighted"]),
     ("Changing the mode distribution turns MAX A/C off",
      ["1. Press \"MAX A/C\" on the climate screen",
       "2. Select another airflow mode and read the \"MAX A/C\" button"],
      ["1. The \"MAX A/C\" button is highlighted",
       "2. The \"MAX A/C\" button is no longer highlighted"]),
     ("Pressing MAX A/C again turns MAX A/C off",
      ["1. Press \"MAX A/C\" on the climate screen",
       "2. Press \"MAX A/C\" again and read the button"],
      ["1. The \"MAX A/C\" button is highlighted",
       "2. The \"MAX A/C\" button is no longer highlighted"]),
   ]),
 # ---------------------------------------------------------------- 16.10
 "SWE1-HVAC-115-05": dict(
   quote="Actions on rear defrost, heated/vented seats or heated wheel don t "
         "reactivate climate (climate still off)",
   why="三個控制各自可失效；且三者所需之配備不同，故其 PC 依 R-C28 第一問各自具名。",
   variants=[
     ("Pressing REAR DEFROST leaves the climate system off",
      ["1. Turn the climate system off using the climate power button on the "
       "climate screen",
       "2. Press \"REAR DEFROST\" and read the climate state"],
      ["1. The CLIMATE OFF screen is displayed",
       "2. The climate system is still off"],
      "[spec-derived] The vehicle is equipped with rear defrost, which is "
      "absent on some soft top vehicles (3.4)"),
     ("Operating a heated or vented seat leaves the climate off",
      ["1. Turn the climate system off using the climate power button on the "
       "climate screen",
       "2. Turn the heated seat on and read the climate state"],
      ["1. The CLIMATE OFF screen is displayed",
       "2. The climate system is still off"],
      "[spec-derived] The vehicle is equipped with Comfort features, such as "
      "heated/vented seats and a heated steering wheel (17.3)"),
     ("Operating the heated wheel leaves the climate off",
      ["1. Turn the climate system off using the climate power button on the "
       "climate screen",
       "2. Turn the heated steering wheel on and read the climate state"],
      ["1. The CLIMATE OFF screen is displayed",
       "2. The climate system is still off"],
      "[spec-derived] The vehicle is equipped with Comfort features, such as "
      "heated/vented seats and a heated steering wheel (17.3)"),
   ]),
 # ---------------------------------------------------------------- 16.12.1
 "SWE1-HVAC-118-07": dict(
   quote="timeout after 3 seconds of inactivity or as soon as another button "
         "except Mode HC is pressed",
   why="兩個關閉途徑各自可失效：逾時關得掉而按他鍵關不掉，是一種失效。",
   variants=[
     ("The mode pop-up times out after three seconds",
      ["1. Press the Mode hard control from a screen other than Climate main",
       "2. Wait 3 seconds without further interaction"],
      ["1. A small pop-up is shown above the Climate main category control",
       "2. The pop-up is no longer shown"]),
     ("Pressing another button closes the mode pop-up",
      ["1. Press the Mode hard control from a screen other than Climate main",
       "2. Press the fan speed hard control and read the screen"],
      ["1. A small pop-up is shown above the Climate main category control",
       "2. The pop-up is no longer shown"]),
   ]),
 # ---------------------------------------------------------------- 76 §4 之二新缺口
 # 這兩筆不是「拆分」而是**補上缺席之列舉項與反向側**，故其 reason 另寫。
 "SWE1-HVAC-007-01": dict(
   quote="Some vehicles have a configuration for a 3 state toggle recirc "
         "button: Auto, Manual, Open",
   why="",
   reason="§7 反向配對（76 §4）：條文列舉之三態為**閉集**，而原 TC 只驗其"
          "三態可依序到達，未驗「沒有第四態」。封閉性之失效（第四次按壓落到"
          "別的狀態，或循環不回到 Auto）與三態各自之失效互相獨立，故另立一條。",
   variants=[
     ("The recirc button cycles through its three states",
      ["1. Press the RECIRC button", "2. Press the RECIRC button again",
       "3. Press the RECIRC button again"],
      ["1. RECIRC is in the Auto state", "2. RECIRC is in the Manual state",
       "3. RECIRC is in the Open state"]),
     ("A fourth press returns the recirc button to Auto",
      ["1. Press the RECIRC button until RECIRC is in the Open state",
       "2. Press the RECIRC button again and read the RECIRC state"],
      ["1. RECIRC is in the Open state",
       "2. RECIRC is in the Auto state and no further state is offered"]),
   ]),
 "SWE1-HVAC-040-01": dict(
   quote="The pop up will show the front fan speed status (level number, "
         "AUTO, OFF) and the Rear fan status (level number, AUTO, OFF)",
   why="條文逐字列舉三個可能之狀態值，三者之呈現各自可失效"
       "（數字正確而 AUTO 顯示為 0，是一種失效）。",
   variants=[
     ("The fan pop-up shows the front and rear level numbers",
      ["1. Set the front and rear fan speeds to known level numbers",
       "2. Trigger the fan speed pop up using the hard controls"],
      ["1. The front and rear fan speeds are set to known level numbers",
       "2. The pop up shows the front fan level number and the rear fan "
       "level number"]),
     ("The fan pop-up shows AUTO for a fan in AUTO",
      ["1. Turn AUTO on for the front climate",
       "2. Trigger the fan speed pop up using the hard controls"],
      ["1. The front climate is in AUTO",
       "2. The pop up shows AUTO as the front fan status"]),
     ("The fan pop-up shows OFF for a fan that is off",
      ["1. Turn the rear climate off",
       "2. Trigger the fan speed pop up using the hard controls"],
      ["1. The rear climate is off",
       "2. The pop up shows OFF as the rear fan status"]),
   ]),
}

def apply_splits(tcs: list, start_n: int = None) -> list:
    """Rewrite split leaves in place and append their extra rows.

    Variant 0 replaces the leaf's existing TC (same tc_id, so nothing
    renumbers); variants 1.. get late ids allocated in a fixed global order.
    """
    order = sorted(SPLITS)
    base_n = FIRST_N if start_n is None else start_n
    offset = {}
    n = base_n
    for leaf in order:
        offset[leaf] = n
        n += len(SPLITS[leaf]["variants"]) - 1

    out = []
    for tc in tcs:
        spec = SPLITS.get(tc["req_id"])
        if not spec:
            out.append(tc)
            continue
        reason = spec.get("reason") or REASON.format(
            quote=spec["quote"], why=spec["why"])
        for i, variant in enumerate(spec["variants"]):
            title, proc, er = variant[0], variant[1], variant[2]
            extra_pc = variant[3] if len(variant) > 3 else None
            row = dict(tc)
            row["tc_title"] = title
            row["test_procedure"] = "\n".join(proc)
            row["expected_result"] = "\n".join(er)
            row["split_flag"] = True
            row["split_reason"] = reason
            if extra_pc:
                lines = [l for l in row["pre_conditions"].split("\n")
                         if l.strip()]
                lines.insert(1, extra_pc)
                row["pre_conditions"] = "\n".join(
                    f"{i2 + 1}. {re_strip(l)}" for i2, l in enumerate(lines))
            if i:
                row["tc_id"] = TC_ID_FMT.format(n=offset[tc["req_id"]] + i - 1)
            out.append(row)
    return out


def re_strip(line: str) -> str:
    import re
    return re.sub(r"^\d+\.\s*", "", line)