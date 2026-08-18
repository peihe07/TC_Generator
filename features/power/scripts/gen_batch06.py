"""末批產生器（R-P189）—— Branding and Theme。

範圍**取自 G121 對帳表**之「未產出且未受阻斷」全集（R-P177(b) / R-P189），
逐一列出，不以區間表述。

每一 leaf 之 `reasoning` 依 **§10.4 四項順序**撰寫
（驗證目標／關鍵情境條件／為什麼這樣切／未涵蓋·刻意略過），
**非模板套語**（R-P190(ii)）；含適用性條件者依 R-P193 明載其處理，
與他 leaf 重疊者依 R-P196 註明對造 leaf ID。

用法：
    python features/power/scripts/gen_batch06.py
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_tcs import anchor_bodies  # noqa: E402

SPEC = ("R1LR_Atl-H_25PI3.5_Activation and Configuration_"
        "CFTS_009_Wake-up and Power-up_SR26_20250909-1658")
SIM = "A LIN and CAN simulation tool is connected"
START_ID = 231           # 27 包全域重編後之起號（`renumber_tc_ids.py`）
BATCH = "batch_006_branding_theme"

BRAND_SKIP = (
    "刻意略過：本條為 `$VC_VEH_BRAND$` 之值對照表（13 個品牌值），"
    "其結構為同一觸發訊號之值映射。取三值成條 —— 一般品牌值、"
    "`Jeep`（與 R-P193 之品牌適用性問題相關）與標為 `(DEFAULT)` 之 `Fiat`；"
    "**其餘十值未測**，其映射形態與已測者相同，"
    "**惟此為列舉型「只取其一」，已依 R-P192 登記待裁，非宣稱不需測**。")

# leaf -> §10.4 reasoning
REASONING = {
 "SWE-PM-077":
  "驗證目標：`$VC_SpecialPKG$` 是否為 HU 決定主題之依據。"
  "關鍵情境條件：HU 帶一個受支援之 `$VC_SpecialPKG$` 值，讀其所套用之主題。"
  "為什麼這樣切：本條僅一個行為（以該訊號決定主題），一條即足；"
  "值域之定義委由 [PDO Theme Configuration] 文件，非本條所載。"
  "刻意略過：具體值與主題之對應表不在 `source_clause` 內（規格以外部文件承接），"
  "依 §8.4.2 不測本規格未擁有者；未支援值之處置由 `SWE-PM-078` 承接（§8.2.1）。",
 "SWE-PM-078":
  "驗證目標：`$VC_SpecialPKG$` 為 `none` 或不受支援時，是否回落至以 "
  "`$VC_VEH_BRAND$` 為準之預設主題。"
  "關鍵情境條件：分別送入 `none` 與一個 HU 不支援之值。"
  "為什麼這樣切：原文以 `or` 並列二個觸發條件（`none` / 不受支援），"
  "依 §5.7 各自成條，二條；此亦為 G113 之 OR 分支要求。"
  "刻意略過：預設值之具體定義委由 [PDO Theme Configuration]，不在本條可驗範圍。",
 "SWE-PM-079":
  "驗證目標：PDO 品牌化元素之 CAN 訊號值不受支援時，是否採用 PDO 所定之預設值。"
  "關鍵情境條件：對一個品牌化元素送入不受支援之 CAN 值。"
  "為什麼這樣切：本條為單一回落規則，一條即足；元素清單與預設值表在外部文件。"
  "刻意略過：「所列之全部品牌化元素」逐一驗證不可行 —— 清單不在 `source_clause` 內，"
  "依 §8.4.2 不測本規格未擁有者。與 `SWE-PM-078` 之回落規則相鄰，"
  "後者管主題、本條管元素，二者不重疊。",
 "SWE-PM-080":
  "驗證目標：CAN 網路喚醒時 `$Radio_Theme$` 是否送出該主題之 special package 值，"
  "以及主題變更後是否於 Tsend 內更新。"
  "關鍵情境條件：CAN 網路 awake；其後變更主題。"
  "為什麼這樣切：原文含二個可觀察行為（喚醒時送值、變更時於時限內更新），"
  "依 §8.3 之行為維度拆為二條。"
  "刻意略過：Tsend 之數值未載於 `source_clause`，故第二條只驗「有更新且在時限內」，"
  "**不造任何容差值**（比照 R-P97）。"
  "**重疊登記（R-P196）**：本條與 `SWE-PM-086` 之 `source_clause` 逐字相同而錨點不同"
  "（`4941`… 見對帳），二者之處置一致。",
 "SWE-PM-081":
  "驗證目標：HU 是否依 `$VC_VEH_BRAND$` 選用對應之品牌字型。"
  "關鍵情境條件：送入不同之 `$VC_VEH_BRAND$` 值，讀畫面字型。"
  "為什麼這樣切：依 §5.7 之不同輸入值各自成條，取三值。"
  + BRAND_SKIP,
 "SWE-PM-082":
  "驗證目標：HU 是否依 `$VC_VEH_BRAND$` 選用對應之 App icon。"
  "關鍵情境條件：送入不同之 `$VC_VEH_BRAND$` 值，讀 App icon。"
  "為什麼這樣切：依 §5.7 之不同輸入值各自成條，取三值。"
  + BRAND_SKIP +
  "另記：本條與 `SWE-PM-081` 為同一訊號之不同呈現目標（字型 vs icon），"
  "非重複，不併。",
 "SWE-PM-083":
  "驗證目標：HU 是否依 `$VC_VEH_BRAND$` 決定 profile 畫面之品牌 avatar 清單。"
  "關鍵情境條件：送入自有 avatar 之品牌值、`(DEFAULT)` 之 `Fiat`，"
  "以及**映射至 Fiat avatar 之品牌值**（`Abarth`）。"
  "為什麼這樣切：本條之值表與 `081` / `082` 不同 —— "
  "`Abarth` / `Opel` / `Vauxhall` / `Citroen` / `Peugeot` 五值**不映射至自身**而映射至 "
  "`Fiat avatars`，此為本條獨有之規則，故第三條專驗該映射。"
  "刻意略過：其餘品牌值未測，理由同 `081`（列舉型「只取其一」，已依 R-P192 登記待裁）。",
 "SWE-PM-084":
  "驗證目標：HU 是否依車型與車身設定決定 recirc icon。"
  "關鍵情境條件：原文分二個架構路徑 —— `CUSW/AtlLo/AtlMi/AtlHi` 以 `$VC_VEH_LINE$` 加 "
  "`$Car_Shape_Configuration$` / `$Number_of_Doors$` PROXI 參數；`PNET` 以 "
  "`$VC_VEH_LINE$` 加 `$VC_BODY_STYLE$` 訊號。"
  "為什麼這樣切：二路徑之輸入來源不同（PROXI 參數 vs CAN 訊號），依 §5.7 各自成條。"
  "**適用性（R-P193）**：本專案為 **Atlantis High**（見 feature.yaml 之 `spec_reference_template` "
  "與素材檔名 `R1LR_Atl-H`），故第一條為本專案適用路徑；**`PNET` 路徑非本專案架構**，"
  "仍成條以保留追溯，其可執行性依 R-P121 標於 `reasoning` 而非省略。",
 "SWE-PM-085":
  "驗證目標：HU 是否依車型與車身設定決定 settings seat graphic。"
  "關鍵情境條件：同 `SWE-PM-084` 之二架構路徑。"
  "為什麼這樣切：依 §5.7 之不同輸入來源各自成條，二條。"
  "**適用性（R-P193）**：本專案為 Atlantis High，`PNET` 路徑非本專案架構，處置同 `SWE-PM-084`。"
  "**重疊登記（R-P196）**：本條與 `SWE-PM-084` 之句構逐字平行，"
  "差別僅在目標物（recirc icon vs settings seat graphic），**非重複**。",
 "SWE-PM-086":
  "驗證目標：CAN 網路喚醒時 `$Radio_Theme$` 之送出與主題變更後之更新。"
  "關鍵情境條件：CAN 網路 awake；其後變更主題。"
  "為什麼這樣切：二個可觀察行為，依 §8.3 拆為二條，與 `SWE-PM-080` 之拆法一致。"
  "**重疊登記（R-P196）**：本條之 `source_clause` 與 `SWE-PM-080` **逐字相同**"
  "而錨點不同（本條 §1.9.15.1.7.1.1、`080` §1.9.15.1）——"
  "為 A-PW137 之近親形態；依 §8.2.2 **不得代 RD 合併**，故二者各自產出，"
  "其重複追溯係 RD 之決定。"
  "刻意略過：Tsend 之數值未載，同 `SWE-PM-080`，不造容差值。",
 "SWE-PM-087":
  "驗證目標：`$VC_VEH_LINE$` 為 `M240` 與非 `M240` 時，seat graphic 之來源是否切換。"
  "關鍵情境條件：分別送入 `M240` 與其他車型值。"
  "為什麼這樣切：原文為明確之 IF / ELSE 二分支，依 §5.7 各自成條。"
  "刻意略過：非 `M240` 時之品牌對應表由 `SWE-PM-085` 與 `081` 一系承接（§8.2.1），"
  "本條只驗「改以 `$VC_VEH_BRAND$` 決定」這一事實。",
 "SWE-PM-088":
  "驗證目標：HU 是否依 `$VC_VEH_LINE$` 決定 performance gauges。"
  "關鍵情境條件：送入一個 `$VC_VEH_LINE$` 值，讀所顯示之 gauges。"
  "為什麼這樣切：單一映射規則，一條即足。"
  "刻意略過：gauge 之指派表在 HMI release 與 PDO graphics 檔案內，"
  "不在 `source_clause` 內，依 §8.4.2 不測本規格未擁有者。",
 "SWE-PM-090":
  "驗證目標：`Theme Mode` 設為 `Auto` 時，是否以 `$Day_Night_Mode$` 決定主題。"
  "關鍵情境條件：`Theme Mode` = `Auto`，`$Day_Night_Mode$` 分別指向日間與夜間。"
  "為什麼這樣切：本條之可觀察結果隨 `$Day_Night_Mode$` 之值而異，"
  "依 §5.7 之不同輸入值拆為二條 —— 只測其一無法判別 HU 是否真的在跟隨該訊號。"
  "刻意略過：`Theme Mode` 之另二值由 `SWE-PM-091` / `SWE-PM-092` 承接（§8.2.1）。",
 "SWE-PM-091":
  "驗證目標：`Theme Mode` 設為 `Day` 時是否固定採用 Day theme。"
  "關鍵情境條件：`Theme Mode` = `Day`。"
  "為什麼這樣切：單一固定行為，一條即足；"
  "為驗其「固定」，前提刻意置於 `$Day_Night_Mode$` 指向夜間之情境。"
  "刻意略過：`Auto` 與 `Night` 由 `SWE-PM-090` / `SWE-PM-092` 承接（§8.2.1）。",
 "SWE-PM-092":
  "驗證目標：`Theme Mode` 設為 `Night` 時是否固定採用 Night theme。"
  "關鍵情境條件：`Theme Mode` = `Night`。"
  "為什麼這樣切：單一固定行為，一條即足；"
  "前提刻意置於 `$Day_Night_Mode$` 指向日間之情境以驗其「固定」。"
  "刻意略過：`Auto` 與 `Day` 由 `SWE-PM-090` / `SWE-PM-091` 承接（§8.2.1）。",
 "SWE-PM-096":
  "驗證目標：Ignition On 時之季節變更判定，及其對開機動畫之影響。"
  "關鍵情境條件：四個季節起始日（12/21、3/20、6/21、9/23）之跨越，"
  "以及「有變更」與「無變更」二種結果。"
  "為什麼這樣切：原文含二層 —— 季節判定之四個日期界線，"
  "與變更與否之二個後果。依 §8.3 拆為六條（四個界線各一，二個後果各一）；"
  "**四個日期為規格逐字所載之界線值，非取樣**，故全數成條。"
  "刻意略過：新季節動畫與品牌動畫之內容差異在 HMI 檔案內，"
  "本條只驗「播放的是哪一種」，不驗其畫面內容（§8.4.2）。",
}

# leaf -> [(title, pre[], data, proc[], er[], priority, split_reason)]
TCS: dict[str, list[tuple]] = {
 "SWE-PM-077": [
  ("The special package value determines the theme used by the HU",
   [SIM, "The HU carries a supported special package configuration"],
   '$VC_SpecialPKG$: a value defined in the PDO Theme Configuration',
   ["Send the value listed in Input Test Data",
    "Read the applied theme against the configured value to check the source"],
   ["The HU accepts the configuration value",
    "The theme used by the HU is the one associated with $VC_SpecialPKG$"],
   "P0", "本條驗 $VC_SpecialPKG$ 決定主題"),
 ],
 "SWE-PM-078": [
  ("A none special package falls back to the brand default theme",
   [SIM, "The HU carries a configured vehicle brand"],
   '$VC_SpecialPKG$: "none"',
   ["Send the value listed in Input Test Data",
    "Read the applied theme against the brand signal to check the fallback"],
   ["The HU accepts the configuration value",
    "The default theme based on the $VC_VEH_BRAND$ signal is used"],
   "P0", "本條驗 OR 之左支 none"),
  ("An unsupported special package falls back to the brand default theme",
   [SIM, "The HU carries a configured vehicle brand"],
   '$VC_SpecialPKG$: a value that is not supported by the HU',
   ["Send the value listed in Input Test Data",
    "Read the applied theme against the brand signal to check the fallback"],
   ["The HU accepts the configuration value",
    "The default theme based on the $VC_VEH_BRAND$ signal is used"],
   "P0", "本條驗 OR 之右支 不受支援之值"),
 ],
 "SWE-PM-079": [
  ("An unsupported CAN value on a branded element uses the PDO default",
   [SIM, "The HU displays a PDO branded element"],
   "A referenced CAN signal carrying a value that is not supported by the HU",
   ["Send the value listed in Input Test Data",
    "Read the shown element to check which value the HU falls back to"],
   ["The HU accepts the signal value",
    "The default value defined by PDO is used for that branded element"],
   "P0", "本條驗品牌化元素之回落規則"),
 ],
 "SWE-PM-080": [
  ("The theme special package value is sent while the CAN network is awake",
   [SIM, "The CAN network is awake", "A theme is applied on the HU"],
   "NA",
   ["Observe the bus traffic while the CAN network stays awake",
    "Read $Radio_Theme$ against the applied theme to check the sent value"],
   ["The HU sends $Radio_Theme$ on the bus",
    "The value sent in $Radio_Theme$ is the special package value associated with that theme"],
   "P0", "本條驗喚醒時之送值"),
  ("A theme change updates the sent value within the send window",
   [SIM, "The CAN network is awake", "A theme is applied on the HU"],
   '$VC_SpecialPKG$: a second value mapped to a different theme',
   ["Send the value listed in Input Test Data",
    "Read $Radio_Theme$ and its timing to check the update"],
   ["The HU sends the new $Radio_Theme$ value",
    "The new value is sent within Tsend of the theme change"],
   "P1", "本條驗變更後之更新與時限"),
 ],
 "SWE-PM-081": [
  ("The Chrysler brand selects the Chrysler font",
   [SIM, "The HU is displaying branded text"],
   '$VC_VEH_BRAND$: "Chrysler"',
   ["Send the value listed in Input Test Data",
    "Read the displayed font to check which font the HU selects"],
   ["The HU accepts the signal value",
    "The HU displays the Chrysler font"],
   "P0", "本條驗一般品牌值之映射"),
  ("The Jeep brand selects the Jeep font",
   [SIM, "The HU is displaying branded text"],
   '$VC_VEH_BRAND$: "Jeep"',
   ["Send the value listed in Input Test Data",
    "Read the displayed font to check which font the HU selects"],
   ["The HU accepts the signal value",
    "The HU displays the Jeep font"],
   "P0", "本條驗 Jeep 值之映射（與 R-P193 之品牌適用性相關）"),
  ("The Fiat brand selects the default Fiat font",
   [SIM, "The HU is displaying branded text"],
   '$VC_VEH_BRAND$: "Fiat"',
   ["Send the value listed in Input Test Data",
    "Read the displayed font to check which font the HU selects"],
   ["The HU accepts the signal value",
    "The HU displays the Fiat font that the specification marks as DEFAULT"],
   "P1", "本條驗標為 DEFAULT 之值"),
 ],
 "SWE-PM-082": [
  ("The Chrysler brand selects the Chrysler App icon",
   [SIM, "The HU is displaying the App icon"],
   '$VC_VEH_BRAND$: "Chrysler"',
   ["Send the value listed in Input Test Data",
    "Read the displayed App icon to check which icon the HU selects"],
   ["The HU accepts the signal value",
    "The HU displays the Chrysler App icon"],
   "P0", "本條驗一般品牌值之映射"),
  ("The Jeep brand selects the Jeep App icon",
   [SIM, "The HU is displaying the App icon"],
   '$VC_VEH_BRAND$: "Jeep"',
   ["Send the value listed in Input Test Data",
    "Read the displayed App icon to check which icon the HU selects"],
   ["The HU accepts the signal value",
    "The HU displays the Jeep App icon"],
   "P0", "本條驗 Jeep 值之映射"),
  ("The Fiat brand selects the default Fiat App icon",
   [SIM, "The HU is displaying the App icon"],
   '$VC_VEH_BRAND$: "Fiat"',
   ["Send the value listed in Input Test Data",
    "Read the displayed App icon to check which icon the HU selects"],
   ["The HU accepts the signal value",
    "The HU displays the Fiat App icon that the specification marks as DEFAULT"],
   "P1", "本條驗標為 DEFAULT 之值"),
 ],
 "SWE-PM-083": [
  ("The Jeep brand offers the Jeep avatars in the profile screen",
   [SIM, "The profile screen is reachable on the HU"],
   '$VC_VEH_BRAND$: "Jeep"',
   ["Send the value listed in Input Test Data",
    "Read the avatar list in the profile screen to check which set is offered"],
   ["The HU accepts the signal value",
    "The profile screen offers the Jeep avatars"],
   "P0", "本條驗自有 avatar 之品牌值"),
  ("The Fiat brand offers the default Fiat avatars",
   [SIM, "The profile screen is reachable on the HU"],
   '$VC_VEH_BRAND$: "Fiat"',
   ["Send the value listed in Input Test Data",
    "Read the avatar list in the profile screen to check which set is offered"],
   ["The HU accepts the signal value",
    "The profile screen offers the Fiat avatars that the specification marks as DEFAULT"],
   "P1", "本條驗標為 DEFAULT 之值"),
  ("The Abarth brand is mapped to the Fiat avatars",
   [SIM, "The profile screen is reachable on the HU"],
   '$VC_VEH_BRAND$: "Abarth"',
   ["Send the value listed in Input Test Data",
    "Read the avatar list in the profile screen to check which set is offered"],
   ["The HU accepts the signal value",
    "The profile screen offers the Fiat avatars rather than an Abarth set"],
   "P0", "本條驗映射至他品牌 avatar 之規則（本 leaf 獨有）"),
 ],
 "SWE-PM-084": [
  ("The recirc icon follows the PROXI parameters on the Atlantis architecture",
   [SIM, "The HU runs the CUSW or Atlantis architecture",
    "The climate screen showing the recirc icon is reachable"],
   '$VC_VEH_LINE$ with the $Car_Shape_Configuration$ and $Number_of_Doors$ PROXI parameters',
   ["Send the configuration listed in Input Test Data",
    "Read the shown recirc icon to check which assignment the HU applies"],
   ["The HU accepts the configuration",
    "The recirc icon matches the assignment for that vehicle line and car shape"],
   "P0", "本條驗 CUSW / Atlantis 路徑（本專案適用）"),
  ("The recirc icon follows the body style signal on the PowerNet architecture",
   [SIM, "The HU runs the PNET architecture",
    "The climate screen showing the recirc icon is reachable"],
   '$VC_VEH_LINE$ with the $VC_BODY_STYLE$ signal',
   ["Send the configuration listed in Input Test Data",
    "Read the shown recirc icon to check which assignment the HU applies"],
   ["The HU accepts the configuration",
    "The recirc icon matches the assignment for that vehicle line and body style"],
   "P2", "本條驗 PNET 路徑（非本專案架構，成條以保留追溯）"),
 ],
 "SWE-PM-085": [
  ("The settings seat graphic follows the PROXI parameters on the Atlantis architecture",
   [SIM, "The HU runs the CUSW or Atlantis architecture",
    "The seat settings screen is reachable"],
   '$VC_VEH_LINE$ with the $Car_Shape_Configuration$ and $Number_of_Doors$ PROXI parameters',
   ["Send the configuration listed in Input Test Data",
    "Read the shown seat graphic to check which assignment the HU applies"],
   ["The HU accepts the configuration",
    "The settings seat graphic matches the assignment for that vehicle line and car shape"],
   "P0", "本條驗 CUSW / Atlantis 路徑（本專案適用）"),
  ("The settings seat graphic follows the body style signal on the PowerNet architecture",
   [SIM, "The HU runs the PNET architecture", "The seat settings screen is reachable"],
   '$VC_VEH_LINE$ with the $VC_BODY_STYLE$ signal',
   ["Send the configuration listed in Input Test Data",
    "Read the shown seat graphic to check which assignment the HU applies"],
   ["The HU accepts the configuration",
    "The settings seat graphic matches the assignment for that vehicle line and body style"],
   "P2", "本條驗 PNET 路徑（非本專案架構，成條以保留追溯）"),
 ],
 "SWE-PM-086": [
  ("The theme special package value is sent on this chapter while the network is awake",
   [SIM, "The CAN network is awake", "A theme is applied on the HU"],
   "NA",
   ["Observe the bus traffic while the CAN network stays awake",
    "Read $Radio_Theme$ against the applied theme to check the sent value"],
   ["The HU sends $Radio_Theme$ on the bus",
    "The value sent in $Radio_Theme$ is the special package value associated with that theme"],
   "P1", "本條驗喚醒時之送值（與 SWE-PM-080 重疊，見 reasoning）"),
  ("A theme change on this chapter updates the sent value within the send window",
   [SIM, "The CAN network is awake", "A theme is applied on the HU"],
   '$VC_SpecialPKG$: a second value mapped to a different theme',
   ["Send the value listed in Input Test Data",
    "Read $Radio_Theme$ and its timing to check the update"],
   ["The HU sends the new $Radio_Theme$ value",
    "The new value is sent within Tsend of the theme change"],
   "P1", "本條驗變更後之更新與時限（與 SWE-PM-080 重疊）"),
 ],
 "SWE-PM-087": [
  ("The M240 vehicle line uses the M240 seat graphics",
   [SIM, "The seat settings screen is reachable"],
   '$VC_VEH_LINE$: "M240"',
   ["Send the value listed in Input Test Data",
    "Read the shown seat graphic to check which set the HU uses"],
   ["The HU accepts the signal value",
    "The HU uses the M240 seat graphics"],
   "P0", "本條驗 IF 分支 M240"),
  ("A non M240 vehicle line falls back to the brand seat graphic",
   [SIM, "The seat settings screen is reachable",
    "The HU carries a configured vehicle brand"],
   '$VC_VEH_LINE$: a value other than "M240"',
   ["Send the value listed in Input Test Data",
    "Read the shown seat graphic against the brand signal to check the source"],
   ["The HU accepts the signal value",
    "The HU uses $VC_VEH_BRAND$ to determine the settings seat graphic"],
   "P0", "本條驗 ELSE 分支"),
 ],
 "SWE-PM-088": [
  ("The performance gauges follow the vehicle line signal",
   [SIM, "The performance gauges screen is reachable"],
   '$VC_VEH_LINE$: a configured vehicle line value',
   ["Send the value listed in Input Test Data",
    "Read the shown gauges to check which assignment the HU applies"],
   ["The HU accepts the signal value",
    "The performance gauges match the assignment for that vehicle line"],
   "P0", "本條驗 $VC_VEH_LINE$ 決定 gauges"),
 ],
 "SWE-PM-090": [
  ("The auto theme mode follows the day night signal into the day theme",
   [SIM, 'The "Theme Mode" setting reads "Auto"'],
   '$Day_Night_Mode$: the value indicating day',
   ["Send the value listed in Input Test Data",
    "Read the applied theme to check which theme the HU shows"],
   ["The HU accepts the signal value",
    "The HU shows the Day theme"],
   "P0", "本條驗 Auto 跟隨日間值"),
  ("The auto theme mode follows the day night signal into the night theme",
   [SIM, 'The "Theme Mode" setting reads "Auto"'],
   '$Day_Night_Mode$: the value indicating night',
   ["Send the value listed in Input Test Data",
    "Read the applied theme to check which theme the HU shows"],
   ["The HU accepts the signal value",
    "The HU shows the Night theme"],
   "P0", "本條驗 Auto 跟隨夜間值"),
 ],
 "SWE-PM-091": [
  ("The day theme mode keeps the Day theme regardless of the day night signal",
   [SIM, 'The "Theme Mode" setting reads "Day"'],
   '$Day_Night_Mode$: the value indicating night',
   ["Send the value listed in Input Test Data",
    "Read the applied theme to check whether the setting overrides the signal"],
   ["The HU accepts the signal value",
    "The HU uses the Day theme"],
   "P0", "本條驗 Day 設定之固定性"),
 ],
 "SWE-PM-092": [
  ("The night theme mode keeps the Night theme regardless of the day night signal",
   [SIM, 'The "Theme Mode" setting reads "Night"'],
   '$Day_Night_Mode$: the value indicating day',
   ["Send the value listed in Input Test Data",
    "Read the applied theme to check whether the setting overrides the signal"],
   ["The HU accepts the signal value",
    "The HU uses the Night theme"],
   "P0", "本條驗 Night 設定之固定性"),
 ],
 "SWE-PM-096": [
  ("The season changes to Summer at the December date",
   [SIM, "The HU clock is set to the day before the Summer start date"],
   "An Ignition On after the date passes December, 21st",
   ["Bring the HU through the event listed in Input Test Data",
    "Read the season the HU determines to check the boundary"],
   ["The HU determines the season at Ignition On",
    "The HU determines that Summer has started"],
   "P0", "本條驗季節界線一（12/21）"),
  ("The season changes to Fall at the March date",
   [SIM, "The HU clock is set to the day before the Fall start date"],
   "An Ignition On after the date passes March, 20th",
   ["Bring the HU through the event listed in Input Test Data",
    "Read the season the HU determines to check the boundary"],
   ["The HU determines the season at Ignition On",
    "The HU determines that Fall has started"],
   "P0", "本條驗季節界線二（3/20）"),
  ("The season changes to Winter at the June date",
   [SIM, "The HU clock is set to the day before the Winter start date"],
   "An Ignition On after the date passes June, 21st",
   ["Bring the HU through the event listed in Input Test Data",
    "Read the season the HU determines to check the boundary"],
   ["The HU determines the season at Ignition On",
    "The HU determines that Winter has started"],
   "P0", "本條驗季節界線三（6/21）"),
  ("The season changes to Spring at the September date",
   [SIM, "The HU clock is set to the day before the Spring start date"],
   "An Ignition On after the date passes September, 23rd",
   ["Bring the HU through the event listed in Input Test Data",
    "Read the season the HU determines to check the boundary"],
   ["The HU determines the season at Ignition On",
    "The HU determines that Spring has started"],
   "P0", "本條驗季節界線四（9/23）"),
  ("A season change plays the new season startup animation",
   [SIM, "The previous Ignition On was in a different season"],
   "NA",
   ["Bring the HU through an Ignition On",
    "Read the played animation to check which one the HU selects"],
   ["The HU determines that there has been a change in season",
    "The HU plays the new season startup animation"],
   "P0", "本條驗有變更之後果"),
  ("No season change plays the normal brand based startup animation",
   [SIM, "The previous Ignition On was in the same season"],
   "NA",
   ["Bring the HU through an Ignition On",
    "Read the played animation to check which one the HU selects"],
   ["The HU determines that there has not been a change in season",
    "The HU plays the normal Brand based startup animation"],
   "P0", "本條驗無變更之後果"),
 ],
}


def layer3() -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    lines = (DATA / "layer3_full.tsv").read_text(encoding="utf-8").splitlines()
    head = lines[0].split("\t")
    for line in lines[1:]:
        r = dict(zip(head, line.split("\t")))
        out.setdefault(r["leaf"], []).append(r)
    return out


def scope() -> tuple[list[str], list[tuple[str, str, str]]]:
    """自 G121 對帳表取「未產出且未受阻斷」全集；阻斷者列為排除清單。"""
    rows = list((DATA / "leaf_batch_reconciliation.tsv")
                .open(encoding="utf-8"))
    rd = list(csv.DictReader(rows, delimiter="\t"))
    include = [r["leaf"] for r in rd
               if r["batch"] == "未產出" and r["blocking_dr"] == "—"]
    excluded = [(r["leaf"], r["test_set"], r["blocking_dr"]) for r in rd
                if r["batch"] == "未產出" and r["blocking_dr"] != "—"]
    return include, excluded


def numbered(items: list[str]) -> str:
    return "\n".join(f"{i}. {s}" for i, s in enumerate(items, 1))


# **本批之 leaf 全集**（R-P189：逐一列出，不以區間表述）。
# derivation 為 26 包當時之 G121 對帳表之「未產出且未受阻斷」全集（16 leaf）。
# **凍結為明列**，理由同 `gen_batch05.py` —— 產出後自表推導會回傳空集。
INCLUDE = sorted(TCS)


def main() -> None:
    include, excluded = INCLUDE, scope()[1]
    missing = [x for x in include if x not in TCS]
    extra = [x for x in TCS if x not in include]
    assert not missing and not extra, (missing, extra)

    l3, bodies = layer3(), anchor_bodies()
    ts = {r["leaf"]: r["test_set"]
          for r in csv.DictReader(
              (DATA / "leaf_batch_reconciliation.tsv").open(encoding="utf-8"),
              delimiter="\t")}
    leaves, tcs = [], []
    n = START_ID
    for leaf in include:
        rows = l3[leaf]
        anchors = [a for r in rows for a in r["item_ids"].split(",")
                   if a and bodies.get(a)]
        secs = sorted({r["chapter_num"] for r in rows})
        leaves.append({
            "parent": leaf,
            "section": "、".join(secs),
            "source_anchor": ",".join(anchors),
            "source_clause": "\n".join("\n".join(bodies[a]) for a in anchors),
            "reasoning": REASONING[leaf],
        })
        for idx, (title, pre, data, proc, er, prio, reason) in enumerate(TCS[leaf], 1):
            tcs.append({
                "req_id": leaf,
                "tc_id": f"NR1L-PowerManagement-{n:03d}",
                "tc_title": title,
                "test_group": "Power Management",
                "test_set": ts[leaf],
                "test_item": title,
                "pre_conditions": numbered(pre),
                "input_test_data": data,
                "test_procedure": numbered(proc),
                "expected_result": numbered(er),
                "specification_reference": f"{SPEC}_{secs[0]}",
                "priority": prio,
                "design_method": "狀態轉換 (State Transition Testing)",
                "split_flag": len(TCS[leaf]) > 1,
                "split_reason": reason,
                "functional_safety": "NA",
                "estimated_test_time": "",
                "remarks": "",
                "distinguishing_axis": {"axis": "behaviour", "delta": reason},
                "reasoning_note": "",
                "split_index": idx,
            })
            n += 1

    batch = {
        "batch": BATCH,
        "test_group": "Power Management",
        "test_set": "Branding and Theme",
        "tc_id_status": "provisional",
        "tc_id_note": "R-P113(b)：本批之 `tc_id` 為批次內臨時號，接續第五批之末（223）。",
        "scope_note": "範圍**取自 G121 對帳表之「未產出且未受阻斷」全集**"
                      "（R-P177(b) / R-P189，不以 ID 區間表述）。"
                      f"**本批 {len(leaves)} leaf，為 Phase 4 之末批**；"
                      "其完成後全部未阻斷之 leaf 皆已產出 TC。"
                      "排除者為 12 個受阻斷之 leaf，逐一見上繳 §四。",
        "leaves": leaves,
        "tcs": tcs,
    }
    path = GENERATED / f"{BATCH}.json"
    path.write_text(json.dumps(batch, ensure_ascii=False, indent=1) + "\n",
                    encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {len(leaves)} leaf / {len(tcs)} TC "
          f"（{tcs[0]['tc_id']} – {tcs[-1]['tc_id']}）")
    print(f"  排除 {len(excluded)} leaf：" +
          "、".join(f"{a}({c})" for a, b, c in excluded))


if __name__ == "__main__":
    main()
