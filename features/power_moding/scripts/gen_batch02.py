#!/usr/bin/env python3
"""batch 2 —— `Startup Sounds`（ch 8，6 leaf）之 TC 產出（28 包步驟 5）。

**選批理由三項，皆可查**（28 包 §四步驟 5）：
  1. 章 8 之材料最乾淨 —— 雙向複驗新漏 **0**（17 包）、
     矩陣全對照牴觸 **0**（26 包，30 列全具名）、marker 6/6 全在 SYS1（14 包）；
  2. **不受任何 DR 阻斷**（`DR-PMH5` 阻 ch 9；`DR-PMH6`／`7` 不阻批）；
  3. 其 6 leaf 為 `SSND 1)`～`SSND 3)` 之展開，含明確之三值列舉。

**`tc_id` 續為 provisional**；**零寫回工作簿**。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = "Power Moding HMI Logic and Flow R1 SR24 2A"

FUNC = "功能測試 (Functional based ; no specific technique)"
STATE = "狀態轉換 (State Transition Testing)"
EP = "等價劃分 (Equivalence Partitioning, EP)"
NEG = "負向測試 (Negative / Invalid)"  # 29 §2.2 後本批已無 NEG（`-014` 改 EP）；常數保留備用

# R-PMH50 —— `source_clause` **逐字取自 PDF p8**（非 SYS1）
PDF = {
    "SSND1": ("SSND 1) If start-up sounds are supported, it will start upon driver "
              "door close and sync with the start-up animation. If goodbye sounds "
              "are supported, it shall sync on start with the shut-down animation. "
              "Sounds will sync amongst all supported vehicle displays."),
    "SSND2": ("SSND 2) Start-up and goodbye sounds shall have a setting with "
              "Always/Once a Day/Never options."),
    "SSND2_1": ("SSND 2.1) If the setting is Always, start-up and goodbye sounds "
                "should be played everytime the startup animation is played."),
    "SSND2_2": ("SSND 2.2) If the setting is Once a Day, start-up and goodbye sounds "
                "should be played only once per day (i.e other valid triggers will "
                "not trigger any sound)."),
    "SSND2_3": ("SSND 2.3) If the setting is Never, start-up and goodbye sounds "
                "should not be played on any situation."),
    "SSND3": ("SSND 3) Sound volume level shall match current entertainment sounds "
              "volume. [DCR19385]"),
}

TCS = [
 dict(leaf="SWE1-HMI-PM-012", outline="8.1", src="SSND1", dm=STATE, pri="P1",
   title="Start-up sounds start on driver door close and sync with the animation",
   item=("SSND 1) If start-up sounds are supported, it will start upon driver door "
     "close and sync with the start-up animation.\n\n"
     "(啟動音路徑 —— 與 -010 之告別音路徑成對；跨螢幕同步併入本條之 ER)"),
   pre=["1. Start-up sounds are supported on this vehicle",
        "2. The start-up sound setting is Always",
        "3. The driver door is open and the head unit is off"],
   proc=["1. Do not press the Mute key or the Headunit Mode key",
         "2. Do not change the headunit mode by voice recognition",
         "3. Close the driver door and record the sound output and the animation",
         "4. Read all supported vehicle displays and record their sound output",
         "5. Check that the start-up sound started with the start-up animation"],

   er=["1. No Mute key press and no Headunit Mode key press occurs",
       "2. The headunit mode is not changed by voice recognition",
       "3. The start-up sound starts when the driver door is closed",
       "4. The sound is synchronised amongst all supported vehicle displays",
       "5. The start-up sound is synchronised with the start-up animation"],

   reason=("**P1 —— 主要功能邏輯**（非 P0）：啟動音之失效不阻斷開機，"
     "故不落 boot/recovery 之射程。依 profile §4「不同觸發即拆分」自 leaf 012 拆出 —— "
     "「駕駛門關閉」（本條）與「關機動畫開始」（見 -010）為兩個觸發。"
     "設計方法 STATE —— 標的為門關閉所引發之狀態轉換及其同步。"
     "⚠ **PC2 之來源與必要性（29 包 §2.3 之修正）**：`The start-up sound setting is Always` **不見於 `SSND 1)`** —— 其來源為 `SSND 2.1)`（`Always` → 每次播放，leaf 014）與 `SSND 2.3)`（`Never` → 任何情形皆不播放，leaf 016），**二者皆為他 leaf**。**不加此限定，本條之 ER 於 `Never` 下不成立**（規格明載其不播放），故該限定為使本條之驗證正確所必需，合於 §8.5 與 R-PMH55(c)；**其只出現於 pre_condition，不擴入本條之斷言**。"
     
     "**跨螢幕同步（`Sounds will sync amongst all supported vehicle displays.`）"
     "併入本條之 ER 而不另立一條** —— 依 canon §5.7「同一觸發之多個必然後果不拆」，"
     "其為同一次啟動音播放之必然後果；**該決定據實記載，其亦可讀為獨立之能力。** "
     "⚠ §8.4.1 不造值：**規格未給任何秒數**（`SSND 1)` 只說 `sync`），"
     "故 ER 只斷言「同步」而不斷言任何時間差。"
     "§4.3.1：test_item 上半為 source_clause 之逐字子句。"
     "⚠ **35 包 §4（R-PMH126 之形式要求）之補具名** —— 本條之限定所對之斷言為 **ER3 `The start-up sound starts when the driver door is closed`**。**其陳述於本條為真**（34 包 §7.1 已逐條實查），**故本條只補具名，不重做**。⚠ **R-PMH94／R-PMH95（28 包步驟 6 之掃描）—— 事件層限定二項**：本條之 ER 斷言「聲音有／無播放」，而 State Matrix `r45`（`Mute Button Pressed`）之 `Mute --> Active` **使聲音不可聞**，其欄軸 `Key On, Gear != Reverse` **與本條之相位重疊**，**條件互斥未證 → 牴觸**（R-PMH84）。步驟 1 排除之。`r46`／`r47`（`Headunit Mode Button Pressed`／`… via VR`）之 `Else: Mute Active` **記法未定義**（A-PMH22）—— 依 **R-PMH95** 納入限定以**涵蓋兩讀**，不判讀該歧義。" "source_clause 取自 PDF p8 之 SSND 1)（R-PMH50）。"),
   axis="觸發路徑：駕駛門關閉（對 -010 之關機動畫）"),

 dict(leaf="SWE1-HMI-PM-012", outline="8.1", src="SSND1", dm=STATE, pri="P1",
   title="Goodbye sounds sync on start with the shut-down animation",
   item=("If goodbye sounds are supported, it shall sync on start with the "
     "shut-down animation.\n\n"
     "(告別音路徑 —— 與 -009 之啟動音路徑成對)"),
   pre=["1. Goodbye sounds are supported on this vehicle",
        "2. The goodbye sound setting is Always",
        "3. The head unit is on and the shut-down animation has not started"],
   proc=["1. Do not press the Mute key or the Headunit Mode key",
         "2. Do not change the headunit mode by voice recognition",
         "3. Trigger the shut-down animation and record the sound output",
         "4. Read the start of the goodbye sound and of the animation",
         "5. Check that the goodbye sound started with the shut-down animation"],

   er=["1. No Mute key press and no Headunit Mode key press occurs",
       "2. The headunit mode is not changed by voice recognition",
       "3. The shut-down animation starts",
       "4. The goodbye sound starts at the start of the animation",
       "5. The goodbye sound is synchronised with the shut-down animation"],

   reason=("**P1 —— 主要功能邏輯**（非 P0）：告別音之失效不阻斷關機。"
     "同 leaf 之第二條（profile §4 之不同觸發，見 -009）。"
     "設計方法 STATE —— 標的為關機動畫開始所引發之同步。"
     "⚠ **PC2 之來源與必要性（29 包 §2.3 之修正）**：`The goodbye sound setting is Always` **不見於 `SSND 1)`** —— 其來源為 `SSND 2.1)`（`Always` → 每次播放，leaf 014）與 `SSND 2.3)`（`Never` → 任何情形皆不播放，leaf 016），**二者皆為他 leaf**。**不加此限定，本條之 ER 於 `Never` 下不成立**（規格明載其不播放），故該限定為使本條之驗證正確所必需，合於 §8.5 與 R-PMH55(c)；**其只出現於 pre_condition，不擴入本條之斷言**。"
     
     "⚠ **`sync on start` 之 `on start` 逐字承載於 ER2**（於動畫開始之時），"
     "**不斷言其結束時之行為** —— 規格未言之（§8.4.1 不造值）。"
     "⚠ **關機動畫之觸發條件不在本條射程** —— `SU4.)`（outline 7.5）載其須 "
     "`KEY OFF 與 radio UI shut down` 之組合，**該條屬 `Startup Animation` 組**，"
     "故本條之步驟 1 只說 `Trigger the shut-down animation` 而不重述其條件（§8.5）。"
     "⚠ **35 包 §4（R-PMH126 之形式要求）之補具名** —— 本條之限定所對之斷言為 **ER4 `The goodbye sound starts at the start of the animation`**。**其陳述於本條為真**（34 包 §7.1 已逐條實查），**故本條只補具名，不重做**。⚠ **R-PMH94／R-PMH95（28 包步驟 6 之掃描）—— 事件層限定二項**：本條之 ER 斷言「聲音有／無播放」，而 State Matrix `r45`（`Mute Button Pressed`）之 `Mute --> Active` **使聲音不可聞**，其欄軸 `Key On, Gear != Reverse` **與本條之相位重疊**，**條件互斥未證 → 牴觸**（R-PMH84）。步驟 1 排除之。`r46`／`r47`（`Headunit Mode Button Pressed`／`… via VR`）之 `Else: Mute Active` **記法未定義**（A-PMH22）—— 依 **R-PMH95** 納入限定以**涵蓋兩讀**，不判讀該歧義。" "source_clause 取自 PDF p8 之 SSND 1)（R-PMH50）。"),
   axis="觸發路徑：關機動畫開始（對 -009 之駕駛門關閉）"),

 dict(leaf="SWE1-HMI-PM-013", outline="8.2", src="SSND2", dm=FUNC, pri="P1",
   title="The sound setting offers Always, Once a Day and Never options",
   item=("SSND 2) Start-up and goodbye sounds shall have a setting with "
     "Always/Once a Day/Never options.\n\n"
     "(設定之存在與其三個選項 —— 三值之行為分別由 -012／-013／-014 驗)"),
   pre=["1. The head unit is on and the settings menu is reachable"],
   proc=["1. Open the start-up and goodbye sound setting and record its options",
         "2. Check that the recorded options are Always, Once a Day and Never"],
   er=["1. The start-up and goodbye sound setting is displayed with its options",
       "2. The options are Always, Once a Day and Never"],
   reason=("**P1 —— 主要功能邏輯**（非 P0）：設定之缺失使三值行為皆不可設定，"
     "惟其不阻斷開機。設計方法 FUNC —— 標的為設定項之存在與其選項集合。"
     "**本條只驗選項之存在，不驗其行為** —— 三值之行為由 -012／-013／-014 分別承載"
     "（profile §4 之三值列舉各自成條）。"
     "⚠ §8.4.1 不造值：**規格未給該設定之所在路徑**，"
     "故 pre-condition 只寫「設定選單可達」而不指任何選單層級。"
     "§10.5：拆為 record 與 check 兩步，不以單步交付。"
     "source_clause 取自 PDF p8 之 SSND 2)（R-PMH50）。"),
   axis="設定之存在（對 -012／-013／-014 之三值行為）"),

 dict(leaf="SWE1-HMI-PM-014", outline="8.2.1", src="SSND2_1", dm=EP, pri="P1",
   title="Always plays the sounds every time the startup animation is played",
   item=("SSND 2.1) If the setting is Always, start-up and goodbye sounds should be "
     "played everytime the startup animation is played.\n\n"
     "(三值之第一值 —— 與 -013 之 Once a Day、-014 之 Never 成組)"),
   pre=["1. The start-up and goodbye sound setting is Always",
        "2. Start-up sounds are supported on this vehicle"],
   proc=["1. Do not press the Mute key or the Headunit Mode key",
         "2. Do not change the headunit mode by voice recognition",
         "3. Play the startup animation and record the sound output",
         "4. Play the startup animation a second time and record the sound output",
         "5. Check that the sound was played on both occasions"],

   er=["1. No Mute key press and no Headunit Mode key press occurs",
       "2. The headunit mode is not changed by voice recognition",
       "3. The sound is played the first time the startup animation is played",
       "4. The sound is played the second time the startup animation is played",
       "5. The sound was played every time the startup animation was played"],

   reason=("**P1 —— 主要功能邏輯**（非 P0）。設計方法 EP —— "
     "`Always`／`Once a Day`／`Never` 為設定值之三個等價類，本條驗第一類。"
     "**`everytime` 以「連續兩次播放」承載** —— 兩次為證明「非只一次」之最小次數；"
     "⚠ **不斷言任何次數上限**（規格只說 `everytime`，§8.4.1 不造值）。"
     "⚠ **本條之觸發為「開機動畫播放」而非「駕駛門關閉」** —— `SSND 2.1)` 逐字為 "
     "`everytime the startup animation is played`，與 `SSND 1)` 之門關閉觸發不同；"
     "**故其步驟以動畫之播放為觸發，不重述門之操作**（§8.5）。"
     "⚠ **35 包 §4（R-PMH126 之形式要求）之補具名** —— 本條之限定所對之斷言為 **ER3 `The sound was played on both occasions`**。**其陳述於本條為真**（34 包 §7.1 已逐條實查），**故本條只補具名，不重做**。⚠ **R-PMH94／R-PMH95（28 包步驟 6 之掃描）—— 事件層限定二項**：本條之 ER 斷言「聲音有／無播放」，而 State Matrix `r45`（`Mute Button Pressed`）之 `Mute --> Active` **使聲音不可聞**，其欄軸 `Key On, Gear != Reverse` **與本條之相位重疊**，**條件互斥未證 → 牴觸**（R-PMH84）。步驟 1 排除之。`r46`／`r47`（`Headunit Mode Button Pressed`／`… via VR`）之 `Else: Mute Active` **記法未定義**（A-PMH22）—— 依 **R-PMH95** 納入限定以**涵蓋兩讀**，不判讀該歧義。" "source_clause 取自 PDF p8 之 SSND 2.1)（R-PMH50）。"),
   axis="設定值：Always（對 -013 之 Once a Day、-014 之 Never）"),

 dict(leaf="SWE1-HMI-PM-015", outline="8.2.2", src="SSND2_2", dm=EP, pri="P1",
   title="Once a Day plays the sounds only once per day",
   item=("SSND 2.2) If the setting is Once a Day, start-up and goodbye sounds should "
     "be played only once per day (i.e other valid triggers will not trigger any "
     "sound).\n\n"
     "(三值之第二值 —— 與 -012 之 Always、-014 之 Never 成組)"),
   pre=["1. The start-up and goodbye sound setting is Once a Day",
        "2. No start-up or goodbye sound has been played today"],
   proc=["1. Do not press the Mute key or the Headunit Mode key",
         "2. Do not change the headunit mode by voice recognition",
         "3. Play the startup animation and record the sound output",
         "4. Play the startup animation a second time on the same day",
         "5. Check that the sound was played once and not on the second occasion"],

   er=["1. No Mute key press and no Headunit Mode key press occurs",
       "2. The headunit mode is not changed by voice recognition",
       "3. The sound is played the first time the startup animation is played",
       "4. No sound is played the second time on the same day",
       "5. The sound was played only once on that day"],

   reason=("**P1 —— 主要功能邏輯**（非 P0）。設計方法 EP —— 三個等價類之第二類。"
     "**`only once per day` 以「同日內兩次觸發」承載**，其括號之逐字 "
     "`i.e other valid triggers will not trigger any sound` 由 ER2 承載。"
     "⚠ §8.4.1 不造值：**規格未定義「一日」之起算點**（午夜？點火週期？），"
     "故 pre-condition 只寫「今日尚未播放過」而不指任何時刻，"
     "**步驟亦只說 `on the same day` 而不給任何時間值**。"
     "**該未定義已具名，若上游另有定義則本條之步驟須重寫。**"
     "⚠ **35 包 §4（R-PMH126 之形式要求）之補具名** —— 本條之限定所對之斷言為 **ER4 `The sound was played once and not on the second occasion`**。**其陳述於本條為真**（34 包 §7.1 已逐條實查），**故本條只補具名，不重做**。⚠ **R-PMH94／R-PMH95（28 包步驟 6 之掃描）—— 事件層限定二項**：本條之 ER 斷言「聲音有／無播放」，而 State Matrix `r45`（`Mute Button Pressed`）之 `Mute --> Active` **使聲音不可聞**，其欄軸 `Key On, Gear != Reverse` **與本條之相位重疊**，**條件互斥未證 → 牴觸**（R-PMH84）。步驟 1 排除之。`r46`／`r47`（`Headunit Mode Button Pressed`／`… via VR`）之 `Else: Mute Active` **記法未定義**（A-PMH22）—— 依 **R-PMH95** 納入限定以**涵蓋兩讀**，不判讀該歧義。" "source_clause 取自 PDF p8 之 SSND 2.2)（R-PMH50）。"),
   axis="設定值：Once a Day（對 -012 之 Always、-014 之 Never）"),

 dict(leaf="SWE1-HMI-PM-016", outline="8.2.3", src="SSND2_3", dm=EP, pri="P1",
   title="Never plays no start-up or goodbye sound in any situation",
   item=("SSND 2.3) If the setting is Never, start-up and goodbye sounds should not "
     "be played on any situation.\n\n"
     "(三值之第三值，負向 —— 與 -012 之 Always、-013 之 Once a Day 成組)"),
   pre=["1. The start-up and goodbye sound setting is Never",
        "2. Start-up and goodbye sounds are supported on this vehicle"],
   proc=["1. Do not press the Mute key or the Headunit Mode key",
         "2. Do not change the headunit mode by voice recognition",
         "3. Close the driver door and record the sound output",
         "4. Play the startup animation and record the sound output",
         "5. Trigger the shut-down animation and check that no goodbye sound "
         "is played"],

   er=["1. No Mute key press and no Headunit Mode key press occurs",
       "2. The headunit mode is not changed by voice recognition",
       "3. No start-up sound is played when the driver door is closed",
       "4. No start-up sound is played when the startup animation is played",
       "5. No goodbye sound is played when the shut-down animation is triggered"],

   reason=("**P1 —— 主要功能邏輯**（非 P0）：其失效使使用者無法關閉音效。"
     "⚠ **設計方法 EP（29 包 §2.2 之修正，原標 NEG）** —— `Always`／`Once a Day`／`Never` 為"
     "**同一設定之三個等價類**，`-012`／`-013` 皆標 EP；依 canon §12 之 first-match，"
     "`Negative / Invalid` 之條件為「Invalid input / illegal op」，而 **`Never` 是合法之設定值，"
     "既非無效輸入亦非非法操作**，故其 first-match 落在 `Input partitioned valid / invalid` → **EP**。"
     "**「其標的為不播放」不使其成為負向測試** —— 等價類之預期結果本就可為「不發生」。"
     "**本條仍為 canon §7 所要求之負向配對**（enumerated supported items 須配至少一條 unsupported／否定情形），"
     "**惟其技術為 EP 之第三類** —— **§7 講的是覆蓋，§12 講的是技術，二者不同層**。"
     "同軸三值同技術，合於 R-PMH59（批內依據互不矛盾）。"
     "**`on any situation` 以三個已知觸發承載**（門關閉／開機動畫／關機動畫）——"
     "**該三者為規格於 ch 8 所載之全部觸發**（`SSND 1)` 之二、`SSND 2.1)` 之一）。"
     "⚠ **步驟 5 之檢查範圍（29 包 §2.4 之修正）** —— 原措詞 `check that no sound was played` 讀來涵蓋三次觸發，而 ER5 只斷言第三次；**改為 `no goodbye sound is played`，使步驟與 ER 同範圍**（前兩次已由 ER3／ER4 各自承載）。"
     "⚠ **「any situation」之涵蓋不可窮舉** —— 本條只驗規格所載之三個觸發，"
     "**其餘情境未驗，據實記載**（此為 NEG 之固有限度，非本條之疏漏）。"
     "**與 -012／-013 不同級之判斷**：三者皆 P1 —— 其失效之後果同為「音效行為錯誤」，"
     "無 R-PMH59 意義下之級差（本批八條之 priority 依據互不矛盾）。"
     "⚠ **35 包 §4（R-PMH126 之形式要求）之補具名** —— 本條之限定所對之斷言為 **ER3 `No start-up sound is played when the driver door is closed`（負向）**。**其陳述於本條為真**（34 包 §7.1 已逐條實查），**故本條只補具名，不重做**。⚠ **R-PMH94／R-PMH95（28 包步驟 6 之掃描）—— 事件層限定二項**：本條之 ER 斷言「聲音有／無播放」，而 State Matrix `r45`（`Mute Button Pressed`）之 `Mute --> Active` **使聲音不可聞**，其欄軸 `Key On, Gear != Reverse` **與本條之相位重疊**，**條件互斥未證 → 牴觸**（R-PMH84）。步驟 1 排除之。`r46`／`r47`（`Headunit Mode Button Pressed`／`… via VR`）之 `Else: Mute Active` **記法未定義**（A-PMH22）—— 依 **R-PMH95** 納入限定以**涵蓋兩讀**，不判讀該歧義。 **本條為負向（`Never`）**，其風險形態與正向相反：**靜音會使本條以錯誤之理由通過**（canon §7 之 false pass）——**該限定於本條尤其不可省。**" "source_clause 取自 PDF p8 之 SSND 2.3)（R-PMH50）。"),
   axis="設定值：Never，負向（對 -012 之 Always、-013 之 Once a Day）"),

 dict(leaf="SWE1-HMI-PM-017", outline="8.3", src="SSND3", dm=FUNC, pri="P2",
   title="Sound volume level matches the current entertainment sounds volume",
   item=("SSND 3) Sound volume level shall match current entertainment sounds "
     "volume.\n\n"
     "(音量位準之一致 —— 與 -009 之「是否播放」為不同謂詞)"),
   pre=["1. Start-up sounds are supported and the setting is Always"],
   proc=["1. Do not press the Mute key or the Headunit Mode key",
         "2. Do not change the headunit mode by voice recognition",
         "3. Read the current entertainment sounds volume and record it",
         "4. Play the startup animation and record the start-up sound volume",
         "5. Check that the recorded start-up sound volume matches the recorded "
         "entertainment sounds volume"],

   er=["1. No Mute key press and no Headunit Mode key press occurs",
       "2. The headunit mode is not changed by voice recognition",
       "3. The current entertainment sounds volume is read and recorded",
       "4. The start-up sound is played and its volume level is recorded",
       "5. The recorded start-up sound volume level matches the recorded "
       "entertainment sounds volume"],

   reason=("**P2 —— 次要／支援功能**：音量位準之偏差不使功能缺失，"
     "其後果為音量與預期不符（§10.2 之 P2 定義）。"
     "**與 -009 不同謂詞** —— 該條驗「是否播放與是否同步」，本條驗「音量位準」。"
     "設計方法 FUNC。"
     "⚠ **29 包 §2.1 之修正**：原 PC2 `The current entertainment sounds volume has been recorded` "
     "**含動作而非狀態**（canon §4.4 之自測：`record` → NOT a Pre-Condition），"
     "且本條正為 canon §5.6 之 before／after 比較 —— **記錄移為 procedure 之步驟 3，比較留在 final ER**。"
     "PC 因而只留一項（支援與設定值）。"
     "⚠ §8.4.1 不造值：**規格未給任何音量單位或容差**（只說 `match`），"
     "故 ER 只斷言「相符」而不給任何數值或百分比。"
     "**⚠ 本條為本批唯一之 P2** —— 其依據為「其失效不使任何功能缺失」，"
     "與 -012～-014 之「音效行為錯誤」不同量級（R-PMH59：批內依據互不矛盾）。"
     "⚠ **35 包 §4（R-PMH126 之形式要求）之補具名** —— 本條之限定所對之斷言為 **ER3 `The start-up sound is played and its volume level is recorded`**。**其陳述於本條為真**（34 包 §7.1 已逐條實查），**故本條只補具名，不重做**。⚠ **R-PMH94／R-PMH95（28 包步驟 6 之掃描）—— 事件層限定二項**：本條之 ER 斷言「聲音有／無播放」，而 State Matrix `r45`（`Mute Button Pressed`）之 `Mute --> Active` **使聲音不可聞**，其欄軸 `Key On, Gear != Reverse` **與本條之相位重疊**，**條件互斥未證 → 牴觸**（R-PMH84）。步驟 1 排除之。`r46`／`r47`（`Headunit Mode Button Pressed`／`… via VR`）之 `Else: Mute Active` **記法未定義**（A-PMH22）—— 依 **R-PMH95** 納入限定以**涵蓋兩讀**，不判讀該歧義。" "source_clause 取自 PDF p8 之 SSND 3)（R-PMH50）。"),
   axis="謂詞：音量位準（對 -009 之是否播放與是否同步）"),
]

BASE = 8          # batch 1 用 001–008，本批續 009 起（R-PMH16 之 {NNN}）


# 29 包步驟 4 —— 本批之事件層限定（R-PMH94／R-PMH95 之二項，逐字同 procedure）
LIMIT_TOKENS_B2 = [
    "press the Mute key or the Headunit Mode key",
    "change the headunit mode by voice recognition",
]


def main() -> None:
    out = []
    for n, t in enumerate(TCS, BASE + 1):
        out.append({
            "tc_id": f"NR1L-DisclaimerScreen-{n:03d}",
            "leaf_id": t["leaf"],
            "test_group": "Disclaimer screen",          # R-PMH13，小寫 s（交付夾名）
            "test_set": "Startup Sounds",               # R-PMH36 之 Layer 2 定版 8 組之一
            "tc_title": t["title"],
            "test_item": t["item"],
            "pre_conditions": "\n".join(t["pre"]),
            "input_test_data": "NA",
            "test_procedure": "\n".join(t["proc"]),
            "expected_result": "\n".join(t["er"]),
            "specification_reference": f"{SPEC}_{t['outline']}",
            "design_method": t["dm"],
            "priority": t["pri"],
            "functional_safety": "NA",
            "estimated_test_time": "",
            "vehicle_models": "",
            "remarks": "",
            "reasoning": t["reason"],
            "distinguishing_axis": t["axis"],
            "source_clause": PDF[t["src"]],
            "source_clause_origin": "spec_pdf p8",
        })
    doc = {
        "batch": "batch02",
        "feature": "power_moding",
        "test_group": "Disclaimer screen",
        "test_set": "Startup Sounds",
        "handoff": "docs/handoff/28_batch2.md",
        "profile": "docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md",
        "selection": ("Test Set `Startup Sounds` 之 6 leaf（R-PMH36 之 Layer 2 定版）。"
                      "**7 條 TC** —— `SWE1-HMI-PM-012` 依 profile §4「不同觸發即拆分」"
                      "拆為 2 條（駕駛門關閉／關機動畫開始）。"),
        "tc_id_status": "provisional",
        "leaf_scope": sorted({t["leaf"] for t in TCS}),
        # 29 包步驟 4（R-PMH107(b)）：本批之事件層限定清單（六條各二項，共 12 項）——
        # **既有檢查對新資料之適用，非新增檢查項**（R-PMH107 之判別法）。
        "limits": {tc["tc_id"]: LIMIT_TOKENS_B2 for tc in out
                   if all(k in tc["test_procedure"] for k in LIMIT_TOKENS_B2)},
        "source_clause_basis": ("R-PMH50 —— 逐字取自 spec_pdf p8（判讀基準，通則 3）。"
                                "**章 8 之材料經 17 包雙向複驗新漏 0、26 包矩陣全對照牴觸 0。**"),
        "write_back": "凍結 —— 本批只產出 JSON，不寫回工作簿",
        "tcs": out,
    }
    p = ROOT / "generated" / "batch02.json"
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {p} — {len(out)} TC（自 {len(doc['leaf_scope'])} leaf）")


if __name__ == "__main__":
    main()
