"""第五批產生器（R-P181）。

範圍**取自 G121 對帳表**，依 R-P177(b) 逐一列出 leaf ID 全集，
**不以 ID 區間表述**。`leaves` 之 `section` / `source_anchor` /
`source_clause` 全部機械取得（`build_b5_material.py` 同源）。

TC 內容為人所撰（下表 `TCS`），拆分依 §5.7 / §8.2.2；
`tc_id` 為批次內臨時號（R-P113(b)），接續第四批之末（`157`）。

用法：
    python features/power/scripts/gen_batch05.py
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
from build_b5_material import layer3, scope  # noqa: E402
from lint_tcs import anchor_bodies  # noqa: E402

SPEC = ("R1LR_Atl-H_25PI3.5_Activation and Configuration_"
        "CFTS_009_Wake-up and Power-up_SR26_20250909-1658")
SIM = "A LIN and CAN simulation tool is connected"
START_ID = 158
BATCH = "batch_005_startup_display"

REASONING = {
    'SWE-PM-066':
        '驗證目標：SOS 與 Assist 通話是否被視為「電話通話轉為 active」。關鍵情境條件：HU 處於會對通話 active 起反應之狀態，分別置入 SOS 與 Assist 通話。為什麼這樣切：原文並列二個通話類別，依 §5.7 各自成條 ——二者為不同之通話來源，故障可只存在其一。刻意略過：通話 active 之後續行為由 Power State 一系（`SWE-PM-037` / `038`）承接（§8.2.1）。**重疊登記（R-P196）**：與 `SWE-PM-067` 相似度 0.60，二者為同族之通話類別條文（SOS/Assist vs Projection），非重複。',
    'SWE-PM-067':
        '驗證目標：Projection device 通話是否被視為「電話通話轉為 active」。關鍵情境條件：已配對之 projection device 發起通話。為什麼這樣切：單一通話類別，一條即足。刻意略過：後續行為由他 leaf 承接（§8.2.1）。**重疊登記（R-P196）**：與 `SWE-PM-066` 相似度 0.60，見該 leaf。',
    'SWE-PM-068':
        '驗證目標：來電所致之 IDLE → FULL OPERATION 是否略過尚未顯示之免責畫面。關鍵情境條件：HU 於 IDLE，免責畫面尚未顯示過，發生來電。為什麼這樣切：單一觸發、單一結果，一條即足。刻意略過：免責畫面之補顯時機由 `SWE-PM-070` / `115` 承接（§8.2.1）。**重疊登記（A-PW137）**：本 leaf 與 `SWE-PM-114` 之 `source_anchor` **完全相同**（`4941876`）；依 §8.2.2 不得代 RD 合併，二者各自產出（DR-PW12）。',
    'SWE-PM-069':
        '驗證目標：來電結束且畫面停於電話主畫面或投射通話 UI 時，是否退回 IDLE。關鍵情境條件：二種畫面狀態之一，通話由 active 轉 inactive。為什麼這樣切：原文之 `phone main screen or phone projection call UI` 為 OR 並列，依 §5.7 各自成條 —— 只測其一時另一畫面之失效無法判讀。刻意略過：其他畫面狀態下之行為原文未載，未推定。',
    'SWE-PM-070':
        '驗證目標：為通話而略過之免責畫面，是否於下次進入 FULL OPERATION 時補顯。關鍵情境條件：來電使 HU 離開 IDLE，通話結束後回到 IDLE，再次進入 FULL OPERATION。為什麼這樣切：本條為跨二個時點之單一規則，一條涵蓋（略過與補顯以二個 ER 承接）。刻意略過：略過本身之規則由 `SWE-PM-068` 承接（§8.2.1）。**重疊登記（A-PW137）**：與 `SWE-PM-115` 之錨點完全相同（`4941878`）。',
    'SWE-PM-074':
        '驗證目標：Body OFF 進入 Standby 時若有 FOTA 更新，HU 是否轉入 Timed 顯示彈窗。關鍵情境條件：Radio、TBM 或 ROV 三者之一有可用更新。為什麼這樣切：原文之 `Radio, TBM, or ROV` 為 OR 並列，依 §5.7 各自成條 ——三個更新來源不同，故障可只存在其一。刻意略過：`See HMI for pop-up details` 為交叉參照，彈窗內容依 §8.4.2 不測；`see CFTS057` 為外部文件。此二項於 25 包反向涵蓋透鏡 1 列為「無對應」，已裁為交叉參照而非缺口（25 §6.3）。',
    'SWE-PM-075':
        '驗證目標：因 FOTA 彈窗而進入 Timed 後，三個離開條件是否各自使 HU 轉回 Standby。關鍵情境條件：1 分鐘無互動 / 彈窗被關閉 / `$ACCDlyAct$` 由 active 轉 inactive。為什麼這樣切：原文以項目符號並列三個條件，依 §8.2.2 各拆一條 ——三者可獨立失效，合併後無法判別是哪一個條件沒生效。刻意略過：`CFTS009-1809` 所指之進入條件由 `SWE-PM-074` 承接（§8.2.1）。',
    'SWE-PM-076':
        '驗證目標：長按電源鍵之 radio reset、其 log 保存與重置範圍，及韌體安裝中之例外。關鍵情境條件：`$ICSPowerButton$` 連續按住 10 秒；分別為未安裝韌體與安裝中。為什麼這樣切：四個錨點載三個可獨立失效之事實 ——重置與 log、重置涵蓋二個處理器、安裝中不重置，依 §8.2.2 各拆一條。刻意略過：log 之內容與格式未載於原文，只驗其產生。',
    'SWE-PM-093':
        '驗證目標：駕駛門關閉所觸發之開機動畫、其略過條件、取消條件與再播放間隔。關鍵情境條件：SLEEP / STANDBY / PARTIAL OPERATION 三模式之一；`$Door_Ajar_Status$` 轉 CLOSED；`$DriverDoorOnOffSts$` 為 DOOR_OFF；播放中之模式變更或 IGN_START。為什麼這樣切：三個起始模式為 OR 並列（依 §5.7 各自成條），加上略過、取消（模式變更與 IGN_START 二支）、門開啟時之略過、再播放間隔，共七條。**補測同步（R-P191）**：其中「模式變更至 TIMED MODE 取消動畫」與「門開啟時之模式變更略過動畫」二支為 25 包 G113 分桶所攔下之真缺口，已依 R-P118(d) 補測；本 reasoning 於同一步更新（25 §6.2）。刻意略過：動畫內容依 HMI / PDO 定義，不在本條範圍（§8.4.2）。**變體登載（A-PW138 / R-P188）**：本 leaf 之二錨點（`4941301` §1.3.5、`4941941` §1.9.8）內文逐字相同而屬性相異五欄，`source_clause` 因而含同一段落二次；二者之 ECU 皆含 LTM、Radio 皆涵蓋本專案，適用性未變，**未合併亦未拆分**，裁定於 27 包。',
    'SWE-PM-094':
        '驗證目標：開機動畫是否與 Splash screen、免責畫面分開呈現。關鍵情境條件：HU 走一次會播放動畫之開機流程。為什麼這樣切：單一呈現規則，一條即足。刻意略過：三個畫面之個別內容不在本條範圍；其顯示時機由 `SWE-PM-104` 承接（§8.2.1）。',
    'SWE-PM-095':
        '驗證目標：`LTM_OperationalModeSts.Info` 離開 SNA 後之狀態圖恢復，且不顯示 splash screen。關鍵情境條件：訊號由 SNA 轉為其他值。為什麼這樣切：單一恢復行為，一條即足；「避免顯示 splash screen」為同一步之第二個可觀察結果。刻意略過：進入 SNA 之處置由 `SWE-PM-039` 承接（§8.2.1）。',
    'SWE-PM-097':
        '驗證目標：DID `Startup Animation Selection` 為 Fiat Latam 時之 logo 覆蓋規則。關鍵情境條件：HU 帶已設定之車輛品牌，DID 設為 Fiat Latam。為什麼這樣切：單一覆蓋規則，一條即足；前提保留一個已設定之品牌以驗 regardless。刻意略過：Fiat Latam logo 之圖檔內容不在本條範圍。**重疊登記（A-PW137 / R-P186）**：本 leaf 與 `SWE-PM-056` 之 `source_anchor` **完全相同**（`4941680`），`source_clause` 逐字一致。依 §8.2.2「TC 作者不得代 RD 合併需求單位」，二者各自產出以維持追溯；其重複係 RD 之決定（DR-PW12）。',
    'SWE-PM-098':
        '驗證目標：`Welcome Onboard Sound` 設為 Always 時，開機動畫是否伴隨同時起始之開機音。關鍵情境條件：`$Themed_Sound$` 為 Fiat Latam，設定為 Always。為什麼這樣切：單一設定值、單一結果，一條即足。刻意略過：Once a Day 與 Never 由 `SWE-PM-099` / `100` 承接（§8.2.1）。**重疊登記（R-P196）**：與 `SWE-PM-100` 相似度 0.88 —— 二者為同一設定之不同值（Always vs Never），結果相反，非重複。',
    'SWE-PM-099':
        '驗證目標：Once a Day 設定下之當日首次播放，及「新的一天」之判定。關鍵情境條件：當日尚未播放 / 已播放且客戶選定日期發生變更。為什麼這樣切：原文為二層 —— 播放規則與「新的一天」之定義，後者明列三個成因（手動調整、跨越午夜、時區或日光節約自動調整），依 §8.2.2 各拆一條，共四條。**補測同步（R-P191）**：跨越午夜與時區／DST 二支為 25 包反向涵蓋透鏡 1 所攔下之缺口，已補測；本 reasoning 於同一步更新（25 §6.2）。刻意略過：`CFTS009-2299` 為本 leaf 自身之編號引用，非外部委出。',
    'SWE-PM-100':
        '驗證目標：`Welcome Onboard Sound` 設為 Never 時，開機動畫是否不伴隨開機音。關鍵情境條件：`$Themed_Sound$` 為 Fiat Latam，設定為 Never。為什麼這樣切：單一設定值、單一否定結果，一條即足。刻意略過：其餘二設定值由 `SWE-PM-098` / `099` 承接（§8.2.1）。**重疊登記（R-P196）**：與 `SWE-PM-098` 相似度 0.88，見該 leaf。',
    'SWE-PM-101':
        '驗證目標：`SDARS_Presence` 與 `Audio_Brand` 四種組合下之 logo 呈現。關鍵情境條件：二訊號各二值之四種組合。為什麼這樣切：原文逐條明列四個組合及其互斥結果，依 §8.2.2 各拆一條。刻意略過：logo 圖檔本身之外觀不在本條範圍。**重疊登記（A-PW137 / R-P186）**：本 leaf 與 `SWE-PM-054` 之 `source_anchor` **完全相同**（`4941673`–`4941676`）。依 §8.2.2 不得代 RD 合併，各自產出（DR-PW12）。',
    'SWE-PM-102':
        '驗證目標：Klipsch Splash Screen 之二條設定路徑。關鍵情境條件：`$VC_VEH_LINE$` 為 DT；`$VC_MODEL_YEAR$` 等於或大於 2025。為什麼這樣切：二句之依據訊號與年式條件皆不同，依 §5.7 各自成條。**適用性（R-P193）**：本條限 `$VC_VEH_LINE$ = DT`，本專案車型值無可賴來源，已開 DR-PW13。**重疊登記（A-PW137 / R-P186）**：與 `SWE-PM-055` 之錨點完全相同（`4941678`）。',
    'SWE-PM-103':
        '驗證目標：該點火工作條件下之音訊關閉、畫面限制、ICS 可用性與 DTV 關閉。關鍵情境條件：Ignition On 一系之點火工作條件。為什麼這樣切：四個斷言分為二組可獨立失效之面向（音訊與畫面 / ICS 與 DTV），依 §8.2.2 拆為二條，各以二個 ER 承接。**列舉缺口登記（R-P192 / G131）**：原文以逗號列舉五個點火工作條件（Ignition On、Pre_Start、Start、Cranking、On Engine On），**本 leaf 之二條僅取其中二值，`Pre_Start` / `Start` / `Cranking` 三值未測**。此為逗號型「只取其一」，G113 依定義看不見；已依 R-P192 量測並登記，**是否補測待 27 包裁定，執行層未自行補**。',
    'SWE-PM-104':
        '驗證目標：每個 bus cycle 首次進入 Timed 或 Full Operation 時之 splash 與免責畫面顯示。關鍵情境條件：新 bus cycle；目標模式為 Timed 或 Full Operation；來源模式為 Idle、Standby 或 Partial Operation。為什麼這樣切：第一個錨點之目標模式為 OR 二支，第二個錨點之來源模式為 OR 三支，依 §5.7 共五條 —— 各支之失效彼此獨立。刻意略過：畫面內容不在本條範圍；暫時略過之例外由 `SWE-PM-105` 承接（§8.2.1）。',
    'SWE-PM-105':
        '驗證目標：七類事件下免責與 splash 畫面之暫時略過，及其於同一 bus cycle 之補顯義務。關鍵情境條件：來電／去電／通話中、氣候彈窗、倒車顯影、SOS 與 Assist 通話、FOTA 彈窗。為什麼這樣切：原文以逗號列舉多個例外類別，依 §8.2.2 逐類各拆一條（七條），另一條驗補顯義務，共八條。**補測同步（R-P191）**：初版僅寫通話中與倒車顯影二類，25 包 G113 分桶攔下 FOTA 支之真缺口後補測其餘五類；本 reasoning 於同一步更新（25 §6.2）。刻意略過：`See HMI logic and Flow "Startup" requirements for details` 為交叉參照（§8.4.2），25 包透鏡 1 已裁為非缺口。',
    'SWE-PM-106':
        '驗證目標：`$Ecall_Button_Variant$` 為 SOS 時之免責畫面用字。關鍵情境條件：HU 設定為某一免責畫面變體。為什麼這樣切：單一設定值、單一結果，一條即足。刻意略過：「下列各變體」之清單不在本錨點內（§8.4.2）。**重疊登記（R-P196）**：與 `SWE-PM-107` 相似度 0.78 —— 二者為同一參數之二值（SOS / Help），非重複。',
    'SWE-PM-107':
        '驗證目標：`$Ecall_Button_Variant$` 為 Help 時是否以 Help 取代 SOS 用字。關鍵情境條件：HU 設定為某一免責畫面變體。為什麼這樣切：單一設定值、單一取代結果，一條即足。刻意略過：變體清單不在本錨點內。**重疊登記（R-P196）**：與 `SWE-PM-106` 相似度 0.78，見該 leaf。',
    'SWE-PM-108':
        '驗證目標：非 Maserati 品牌下，核心免責畫面是否每 30 個點火循環才顯示一次。關鍵情境條件：`$VC_VEH_BRAND$` 為 Maserati 以外之值；連續多個點火循環。為什麼這樣切：單一頻率規則，一條即足；首次顯示與其後之間隔以二個 ER 承接。**適用性（R-P193）**：本條之條件為「非 Maserati」，**本專案品牌值無可賴來源** —— 已開 DR-PW13，未自行推定本專案是否落入該分支。刻意略過：Maserati 品牌之行為原文未載，未推定。',
    'SWE-PM-109':
        '驗證目標：GDPR 市場且 TBM 存在時之 GDPR 非 Maserati 開機流程。關鍵情境條件：非 Maserati、`$TBM_Present$` 為 Present、`$Country_Code$` 標記為需 Geolocation 加 SOS 彈窗。為什麼這樣切：三條件之 AND 組合為單一路徑，一條即足。**適用性（R-P193）**：品牌與國別條件皆無可賴來源，併入 DR-PW13。刻意略過：HMI 流程之畫面序列為外部文件（§8.4.2）。**重疊登記（R-P196）**：與 `SWE-PM-110` 相似度 0.88 —— 二者為互補之條件分支（GDPR vs 非 GDPR），結果不同，非重複。',
    'SWE-PM-110':
        '驗證目標：TBM 不存在或國別未標記時之非 GDPR 非 Maserati 開機流程。關鍵情境條件：非 Maserati，且 `$TBM_Present$` 為 Not Present 或 `$Country_Code$` 未標記。為什麼這樣切：原文之括號內為 OR 並列二條件，依 §5.7 各自成條。**補測同步（R-P191）**：25 包 G113 曾就右支之標記名稱標為缺口，查證後為前提措詞未逐字引該標記名（非缺 TC），已補齊措詞（25 §6.2）。**適用性（R-P193）**：同 `SWE-PM-109`，併入 DR-PW13。**重疊登記（R-P196）**：與 `SWE-PM-109` 相似度 0.88，見該 leaf。',
    'SWE-PM-111':
        '驗證目標：非 7 吋螢幕且不需 SOS／Geolocation 時，免責畫面是否加入 ADAS 文字。關鍵情境條件：螢幕非 7 吋；非 Maserati；TBM 不存在或國別不需 SOS 或 Geolocation。為什麼這樣切：括號內為 OR 並列二條件，依 §5.7 各自成條。**適用性（R-P193）**：螢幕尺寸、品牌與國別條件皆無可賴來源，併入 DR-PW13；**7 吋螢幕之行為原文明文排除**，未推定。刻意略過：ADAS 文字之內容為 HMI 所有（§8.4.2）。',
    'SWE-PM-113':
        '驗證目標：需 geolocation 與 SOS 之市場，免責或彈窗是否加入 ADAS 與 SOS。關鍵情境條件：螢幕非 7 吋；非 Maserati；TBM 存在；國別需 geolocation 與 SOS。為什麼這樣切：四條件之 AND 組合為單一路徑，一條即足。刻意略過：`See HMI for different startup conditions` 為交叉參照 ——「加在彈窗或加在免責畫面」之判別委由 HMI，故 ER 寫「二者之一」而不逕指其一（§8.4.2）。**適用性（R-P193）**：同 `SWE-PM-111`，併入 DR-PW13。',
    'SWE-PM-114':
        '驗證目標：來電所致之 IDLE → FULL OPERATION 是否略過尚未顯示之免責畫面。關鍵情境條件：HU 於 IDLE，免責畫面尚未顯示過，發生來電。為什麼這樣切：單一觸發、單一結果，一條即足。**重疊登記（A-PW137 / R-P186）**：本 leaf 與 `SWE-PM-068` 之 `source_anchor` **完全相同**（`4941876`），`source_clause` 逐字一致。依 §8.2.2 不得代 RD 合併需求單位，二者各自產出以維持追溯（DR-PW12）。',
    'SWE-PM-115':
        '驗證目標：為通話而略過之免責畫面，是否於下次進入 FULL OPERATION 時補顯。關鍵情境條件：來電使 HU 離開 IDLE，通話結束後回 IDLE，再次進入 FULL OPERATION。為什麼這樣切：跨二時點之單一規則，一條涵蓋。**重疊登記（A-PW137 / R-P186）**：與 `SWE-PM-070` 之錨點完全相同（`4941878`）；依 §8.2.2 各自產出（DR-PW12）。',
}

# 與他 leaf 共用**全部**錨點者 —— `source_clause` 逐字相同（見上繳 §五）。
DUP_NOTE = {
    "SWE-PM-097": "SWE-PM-056",
    "SWE-PM-101": "SWE-PM-054",
    "SWE-PM-102": "SWE-PM-055",
    "SWE-PM-114": "SWE-PM-068",
    "SWE-PM-115": "SWE-PM-070",
}
NOTES = {
    leaf: (f"**本 leaf 之 `source_anchor` 與 `{other}` 完全相同**，"
           f"`source_clause` 逐字一致。執行層**未合併、未省略**，"
           f"依 037 之 leaf 母體逐一產出以維持追溯；"
           f"是否應改依 §8.2.1 委由 `{other}` 承擔，**呈請裁定於 26 包**。")
    for leaf, other in DUP_NOTE.items()
}
NOTES["SWE-PM-093"] = (
    "**本 leaf 之二錨點（`4941301` §1.3.5 / `4941941` §1.9.8）內文逐字相同，"
    "而屬性相異五欄**（ECU / EE Architecture / Model Year / Radio / State）——"
    "為 R-P136 所定之「屬性相異 → 停並上繳」形態。"
    "二者之 ECU 皆含 `LTM`、Radio 皆涵蓋本專案，故適用性未變，TC 照常產出；"
    "**是否為變體登載，呈請裁定於 26 包**。")

# leaf -> [(title, pre[], data, proc[], er[], priority, split_reason)]
TCS: dict[str, list[tuple]] = {
    "SWE-PM-066": [
        ("An SOS call is treated as a phone call becoming active",
         [SIM, "The HU is in a state that reacts to a phone call becoming active"],
         "An SOS call is placed",
         ["Place the call listed in Input Test Data",
          "Read the HU reaction to check that it treats the call as a phone call"],
         ["The HU registers the call",
          "The HU behaves as for a Phone call becoming active"],
         "P0", "本條驗 SOS call"),
        ("An Assist call is treated as a phone call becoming active",
         [SIM, "The HU is in a state that reacts to a phone call becoming active"],
         "An Assist call is placed",
         ["Place the call listed in Input Test Data",
          "Read the HU reaction to check that it treats the call as a phone call"],
         ["The HU registers the call",
          "The HU behaves as for a Phone call becoming active"],
         "P0", "本條驗 Assist call"),
    ],
    "SWE-PM-067": [
        ("A projection device call is treated as a phone call becoming active",
         [SIM, "A projection device is paired on the bench"],
         "A Projection device call is placed",
         ["Place the call listed in Input Test Data",
          "Read the HU reaction to check that it treats the call as a phone call"],
         ["The HU registers the call",
          "The HU behaves as for a Phone call becoming active"],
         "P0", "本條驗 Projection device call"),
    ],
    "SWE-PM-068": [
        ("An incoming call from IDLE bypasses the disclaimer screen",
         [SIM, "The HU is in IDLE mode", "The disclaimer screen has not yet been shown"],
         "An incoming phone call",
         ["Let the bench place the call listed in Input Test Data",
          "Read the HU mode and the screen to check whether the disclaimer appears"],
         ["The HU transitions from IDLE to FULL OPERATION",
          "The disclaimer screen is bypassed"],
         "P0", "本條驗來電所致之 IDLE → FULL OPERATION 免顯免責畫面"),
    ],
    "SWE-PM-069": [
        ("The HU returns to IDLE when the call ends on the phone main screen",
         [SIM, "The HU is in IDLE mode", "The display is on the phone main screen"],
         "An incoming phone call that then becomes inactive",
         ["Let the bench place and then end the call listed in Input Test Data",
          "Read the HU mode to check the transition after the call ends"],
         ["The HU transitions from IDLE to FULL OPERATION for the call",
          "The HU transitions back to IDLE"],
         "P0", "本條驗 OR 之左支 phone main screen"),
        ("The HU returns to IDLE when the call ends on the phone projection call UI",
         [SIM, "The HU is in IDLE mode", "The display is on the phone projection call UI"],
         "An incoming phone call that then becomes inactive",
         ["Let the bench place and then end the call listed in Input Test Data",
          "Read the HU mode to check the transition after the call ends"],
         ["The HU transitions from IDLE to FULL OPERATION for the call",
          "The HU transitions back to IDLE"],
         "P0", "本條驗 OR 之右支 phone projection call UI"),
    ],
    "SWE-PM-070": [
        ("The bypassed disclaimer is shown at the next transition to FULL OPERATION",
         [SIM, "The HU is in IDLE mode", "The disclaimer has not yet been shown"],
         "An incoming phone call that then becomes inactive",
         ["Let the bench place and then end the call listed in Input Test Data",
          "Bring the HU to FULL OPERATION again and read the screen to check the disclaimer"],
         ["The HU bypasses the disclaimer for the call and returns to IDLE",
          "The disclaimer is shown at the next transition to FULL OPERATION"],
         "P0", "本條驗免責畫面之延後補顯"),
    ],
    "SWE-PM-074": [
        ("A Radio FOTA update at Body OFF brings the HU to Timed for the pop-up",
         [SIM, "The HU transitions to Standby mode as the vehicle enters Body OFF mode"],
         "A FOTA update available for the Radio",
         ["Make available the update listed in Input Test Data",
          "Read the HU mode and the screen to check the resulting presentation"],
         ["The HU transitions to Timed mode",
          "The FOTA update available pop-up is displayed"],
         "P0", "本條驗 OR 之 Radio 支"),
        ("A TBM FOTA update at Body OFF brings the HU to Timed for the pop-up",
         [SIM, "The HU transitions to Standby mode as the vehicle enters Body OFF mode"],
         "A FOTA update available for the TBM",
         ["Make available the update listed in Input Test Data",
          "Read the HU mode and the screen to check the resulting presentation"],
         ["The HU transitions to Timed mode",
          "The FOTA update available pop-up is displayed"],
         "P0", "本條驗 OR 之 TBM 支"),
        ("A ROV FOTA update at Body OFF brings the HU to Timed for the pop-up",
         [SIM, "The HU transitions to Standby mode as the vehicle enters Body OFF mode"],
         "A FOTA update available for the ROV",
         ["Make available the update listed in Input Test Data",
          "Read the HU mode and the screen to check the resulting presentation"],
         ["The HU transitions to Timed mode",
          "The FOTA update available pop-up is displayed"],
         "P0", "本條驗 OR 之 ROV 支"),
    ],
    "SWE-PM-075": [
        ("The HU leaves Timed one minute after the FOTA pop-up is left untouched",
         [SIM, "The HU is in Timed mode due to the condition described in CFTS009-1809"],
         "NA",
         ["Leave the FOTA pop-up without any user interaction",
          "Read the HU mode after the idle period to check the transition"],
         ["The pop-up stays on the screen while no interaction occurs",
          "The HU transitions to Standby mode after 1 minute has passed"],
         "P0", "本條驗條件一 —— 1 分鐘無互動"),
        ("The HU leaves Timed when the FOTA pop-up is dismissed",
         [SIM, "The HU is in Timed mode due to the condition described in CFTS009-1809"],
         "NA",
         ["Dismiss the FOTA pop-up on the screen",
          "Read the HU mode to check the transition after the dismissal"],
         ["The FOTA pop up is dismissed",
          "The HU transitions to Standby mode"],
         "P0", "本條驗條件二 —— pop-up 被關閉"),
        ("The HU leaves Timed when the accessory delay becomes inactive",
         [SIM, "The HU is in Timed mode due to the condition described in CFTS009-1809"],
         "$ACCDlyAct$: active to inactive",
         ["Send the transition listed in Input Test Data",
          "Read the HU mode to check the transition that follows"],
         ["The HU registers the transition without a bus error",
          "The HU transitions to Standby mode"],
         "P0", "本條驗條件三 —— $ACCDlyAct$ 轉為 inactive"),
    ],
    "SWE-PM-076": [
        ("A ten second power button press performs a radio reset and saves logs",
         [SIM, "The HU is not installing a firmware image"],
         "$ICSPowerButton$: Pressed for 10 seconds consecutively",
         ["Send the input listed in Input Test Data",
          "Read the HU behavior and the stored logs to check the reset"],
         ["The HU performs a radio reset",
          "The HU collects and saves logs at the time of the reset"],
         "P0", "本條驗重置本身與 log 保存"),
        ("The power button reset covers both the main CPU and the CAN micro",
         [SIM, "The HU is not installing a firmware image"],
         "$ICSPowerButton$: Pressed for 10 seconds consecutively",
         ["Send the input listed in Input Test Data",
          "Read both processors to check what the reset covers"],
         ["The main CPU resets at the time of the reset",
          "The CAN micro resets at the time of the reset"],
         "P0", "本條驗重置範圍涵蓋二個處理器"),
        ("No power button reset occurs while a firmware image is installing",
         [SIM, "The HU is currently installing a firmware image"],
         "$ICSPowerButton$: Pressed for 10 seconds consecutively",
         ["Send the input listed in Input Test Data",
          "Read the HU behavior to check whether a reset occurs"],
         ["The HU registers the input",
          "The HU does not reset due to a power button reset"],
         "P1", "本條驗韌體安裝中之例外"),
    ],
    "SWE-PM-093": [
        ("Closing the driver door in SLEEP MODE plays the start-up animation",
         [SIM, "The HU is in SLEEP MODE", "A driver door is present for the vehicle"],
         '$Door_Ajar_Status$: changed to CLOSED',
         ["Send the change listed in Input Test Data",
          "Read the screen to check the start-up animation defined per HMI"],
         ["The HU registers the change without a bus error",
          "The HU plays a start-up animation"],
         "P0", "本條驗 OR 之 SLEEP MODE 支"),
        ("Closing the driver door in STANDBY MODE plays the start-up animation",
         [SIM, "The HU is in STANDBY MODE", "A driver door is present for the vehicle"],
         '$Door_Ajar_Status$: changed to CLOSED',
         ["Send the change listed in Input Test Data",
          "Read the screen to check the start-up animation defined per HMI"],
         ["The HU registers the change without a bus error",
          "The HU plays a start-up animation"],
         "P0", "本條驗 OR 之 STANDBY MODE 支"),
        ("Closing the driver door in PARTIAL OPERATION MODE plays the start-up animation",
         [SIM, "The HU is in PARTIAL OPERATION MODE", "A driver door is present for the vehicle"],
         '$Door_Ajar_Status$: changed to CLOSED',
         ["Send the change listed in Input Test Data",
          "Read the screen to check the start-up animation defined per HMI"],
         ["The HU registers the change without a bus error",
          "The HU plays a start-up animation"],
         "P0", "本條驗 OR 之 PARTIAL OPERATION MODE 支"),
        ("A removed driver door makes the HU skip the start-up animation",
         [SIM, "The HU is in STANDBY MODE"],
         '$DriverDoorOnOffSts$: "DOOR_OFF"',
         ["Send the value listed in Input Test Data and close the driver door",
          "Read the screen to check whether an animation is played"],
         ["The HU registers the value without a bus error",
          "The HU skips the start-up animation"],
         "P0", "本條驗 $DriverDoorOnOffSts$ 之略過分支"),
        ("A mode change cancels a start-up animation in progress",
         [SIM, "The HU is playing a start-up animation"],
         "An ignition event that changes the HU power mode to BODY ON",
         ["Send the event listed in Input Test Data during the animation",
          "Read the screen and the power mode to check the cancellation"],
         ["The HU cancels the current start-up animation",
          "The HU switches to the required power mode as defined"],
         "P0", "本條驗播放中之模式變更取消"),
        ("An ignition crank event cancels a start-up animation in progress",
         [SIM, "The HU is playing a start-up animation"],
         '$PowerMode$: "IGN_START"',
         ["Send the value listed in Input Test Data during the animation",
          "Read the screen and the power mode to check the cancellation"],
         ["The HU cancels the current start-up animation",
          "The HU switches to the required power mode as defined"],
         "P0", "本條驗 IGN_START 取消"),
        ("A mode change to TIMED MODE cancels a start-up animation in progress",
         [SIM, "The HU is playing a start-up animation"],
         "An HU power mode status change to TIMED MODE",
         ["Send the change listed in Input Test Data during the animation",
          "Read the screen and the power mode to check the cancellation"],
         ["The HU cancels the current start-up animation",
          "The HU switches to the required power mode as defined"],
         "P0", "本條驗 OR 之 TIMED MODE 支（R-P118(d) 反向涵蓋裁決補測）"),
        ("An open driver door makes the HU skip the animation on a mode change",
         [SIM, "The HU is in STANDBY MODE",
          '$Door_Ajar_Status$ reads OPEN'],
         "An HU power mode status change to BODY ON",
         ["Send the change listed in Input Test Data",
          "Read the screen to check whether an animation is played"],
         ["The HU switches to the required power mode",
          "The HU skips the start-up animation"],
         "P0", "本條驗門開啟時之模式變更略過（R-P118(d) 反向涵蓋裁決補測）"),
        ("A second start-up animation waits for the wakeup cycle or thirty minutes",
         [SIM, "The HU has just played a start-up animation",
          "All other conditions for the animation to play are met"],
         "NA",
         ["Close the driver door again within the same CAN wakeup cycle",
          "Read the screen against the elapsed time to check the replay rule"],
         ["No further start-up animation is played",
          "A start-up animation plays again only at the next CAN wakeup cycle or after 30 minutes, whichever is greater"],
         "P1", "本條驗再播放之間隔規則"),
    ],
    "SWE-PM-094": [
        ("The startup animation is displayed separately from the other startup screens",
         [SIM, "The HU is in STANDBY MODE"],
         "NA",
         ["Bring the HU through a startup that plays the animation",
          "Read the screen sequence to check how the animation is presented"],
         ["The startup animation is displayed",
          "The startup animation is displayed separately from the Splash screen and disclaimer screen"],
         "P1", "本條驗三畫面之分離呈現"),
    ],
    "SWE-PM-095": [
        ("Leaving the SNA value resumes the state diagram without a splash screen",
         [SIM, 'LTM_OperationalModeSts.Info reads "SNA"'],
         'LTM_OperationalModeSts.Info: a value different from "SNA"',
         ["Send the value listed in Input Test Data",
          "Read the TLM state and the screen to check the resumed behavior"],
         ["The TLM follows the state diagram using the updated value",
          "The possible visualization of the splash screen is avoided"],
         "P0", "本條驗離開 SNA 之恢復行為"),
    ],
    "SWE-PM-097": [
        ("The Fiat Latam startup animation selection replaces the vehicle brand logo",
         [SIM, "The HU carries a configured vehicle brand"],
         'DID "Startup Animation Selection": "Fiat Latam"',
         ["Send the value listed in Input Test Data",
          "Read the shown logo against the configured brand to check which logo appears"],
         ["The HU accepts the configuration value",
          "The Fiat Latam Logo replaces the vehicle brand logo regardless of the configured brand"],
         "P1", "本條驗 Fiat Latam 之覆蓋規則"),
    ],
    "SWE-PM-098": [
        ("The always setting plays a startup sound with the animation",
         [SIM, '$Themed_Sound$ reads "Fiat Latam"',
          'The "Welcome Onboard Sound" setting reads "Always"'],
         "NA",
         ["Bring the HU through a startup that plays the animation",
          "Read the audio output against the animation start to check the accompaniment"],
         ["The HU startup animation is played",
          "A startup sound accompanies the animation and begins at the same time"],
         "P0", "本條驗 Always 設定"),
    ],
    "SWE-PM-099": [
        ("The once a day setting plays the startup sound on the first startup of the day",
         [SIM, '$Themed_Sound$ reads "Fiat Latam"',
          'The "Welcome Onboard Sound" setting reads "Once a Day"',
          "The HU has not yet played the startup sound that day"],
         "NA",
         ["Bring the HU through a startup that plays the animation",
          "Read the audio output against the animation start to check the accompaniment"],
         ["The HU startup animation is played",
          "A startup sound accompanies the animation and begins at the same time"],
         "P0", "本條驗 Once a Day 之當日首次"),
        ("A change of the customer selected date allows the sound to play again",
         [SIM, '$Themed_Sound$ reads "Fiat Latam"',
          'The "Welcome Onboard Sound" setting reads "Once a Day"',
          "The HU has already played the startup sound that day"],
         "A manual time adjustment that changes the customer selected date",
         ["Send the adjustment listed in Input Test Data and start the HU again",
          "Read the audio output to check whether a new day is granted"],
         ["The HU startup animation is played",
          "A startup sound accompanies the animation for the new day"],
         "P1", "本條驗「新的一天」之判定 —— 手動調整"),
        ("Passing midnight allows the startup sound to play again",
         [SIM, '$Themed_Sound$ reads "Fiat Latam"',
          'The "Welcome Onboard Sound" setting reads "Once a Day"',
          "The HU has already played the startup sound that day"],
         "NA",
         ["Let the clock pass midnight and start the HU again",
          "Read the audio output to check whether a new day is granted"],
         ["The HU startup animation is played",
          "A startup sound accompanies the animation for the new day"],
         "P1", "本條驗「新的一天」之判定 —— 跨越午夜（R-P118(d) 補測）"),
        ("An automatic time zone adjustment allows the startup sound to play again",
         [SIM, '$Themed_Sound$ reads "Fiat Latam"',
          'The "Welcome Onboard Sound" setting reads "Once a Day"',
          "The HU has already played the startup sound that day"],
         "An automatic adjustment due to time zones or Daylight Savings Time",
         ["Send the adjustment listed in Input Test Data and start the HU again",
          "Read the audio output to check whether a new day is granted"],
         ["The HU startup animation is played",
          "A startup sound accompanies the animation for the new day"],
         "P1", "本條驗「新的一天」之判定 —— 時區／日光節約自動調整（R-P118(d) 補測）"),
    ],
    "SWE-PM-100": [
        ("The never setting plays no startup sound with the animation",
         [SIM, '$Themed_Sound$ reads "Fiat Latam"',
          'The "Welcome Onboard Sound" setting reads "Never"'],
         "NA",
         ["Bring the HU through a startup that plays the animation",
          "Read the audio output against the animation start to check the accompaniment"],
         ["The HU startup animation is played",
          "No startup sound accompanies the animation"],
         "P0", "本條驗 Never 設定"),
    ],
    "SWE-PM-101": [
        ("No audio brand without SDARS shows the vehicle brand logo only",
         [SIM, 'SDARS_Presence reads "Absent"'],
         'Audio_Brand: "No Audio Brand"',
         ["Send the value listed in Input Test Data",
          "Read the shown logos to check the resulting presentation"],
         ["The brand logo screen is presented",
          "The vehicle brand logo that depends on the Brand_Configuration_2 parameter value is shown alone"],
         "P0", "本條驗組合一（Absent ＋ No Audio Brand）"),
        ("Beats brand white without SDARS adds the Beats logo",
         [SIM, 'SDARS_Presence reads "Absent"'],
         'Audio_Brand: "Beats Brand White"',
         ["Send the value listed in Input Test Data",
          "Read the shown logos to check the resulting presentation"],
         ["The brand logo screen is presented",
          "The Beats Brand White logo is shown in addition to the vehicle brand logo"],
         "P0", "本條驗組合二（Absent ＋ Beats Brand White）"),
        ("SDARS present without audio brand adds the Sirius logo",
         [SIM, 'SDARS_Presence reads "Present"'],
         'Audio_Brand: "No Audio Brand"',
         ["Send the value listed in Input Test Data",
          "Read the shown logos to check the resulting presentation"],
         ["The brand logo screen is presented",
          "The Sirius logo is shown in addition to the vehicle brand logo"],
         "P0", "本條驗組合三（Present ＋ No Audio Brand）"),
        ("SDARS present with beats brand white adds both logos",
         [SIM, 'SDARS_Presence reads "Present"'],
         'Audio_Brand: "Beats Brand White"',
         ["Send the value listed in Input Test Data",
          "Read the shown logos to check the resulting presentation"],
         ["The brand logo screen is presented",
          "Both the Sirius and the Beats logos are shown in addition to the vehicle brand logo"],
         "P0", "本條驗組合四（Present ＋ Beats Brand White）"),
    ],
    "SWE-PM-102": [
        ("The special package drives the Klipsch Splash Screen on the 2025 model year",
         [SIM, 'The ETM carries $VC_MODEL_YEAR$ equal to "2025"',
          'The ETM carries $VC_VEH_LINE$ equal to "DT"'],
         '$VC_SpecialPKG_IC$: "Tungsten (147)"',
         ["Send the value listed in Input Test Data",
          "Read the shown Splash Screen to check which screen the ETM displays"],
         ["The ETM accepts the configuration value",
          "The Klipsch Splash Screen is displayed"],
         "P1", "本條驗 2025 年式之 $VC_SpecialPKG_IC$ 路徑"),
        ("The splash screen type drives the Klipsch Splash Screen after the 2025 model year",
         [SIM, 'The ETM carries $VC_MODEL_YEAR$ greater than "2025"',
          'The ETM carries $VC_VEH_LINE$ equal to "DT"'],
         '$SplashScreen_Type$: "Klipsch (7)"',
         ["Send the value listed in Input Test Data",
          "Read the shown Splash Screen to check which screen the ETM displays"],
         ["The ETM accepts the configuration value",
          "The Klipsch Splash Screen is displayed"],
         "P1", "本條驗 2025 年式之後之 $SplashScreen_Type$ 路徑"),
    ],
    "SWE-PM-103": [
        ("Audio is off and only the Splash Screen is allowed in this status",
         [SIM, "The TLM is in an Ignition On working condition"],
         "NA",
         ["Bring the TLM to the status related to TLM audio is OFF",
          "Read the audio path and the display to check what is allowed"],
         ["The TLM audio is OFF",
          "The TLM allows only Splash Screen visualization on its display"],
         "P0", "本條驗音訊關閉與畫面限制"),
        ("ICS stays available while DTV is off in this status",
         [SIM, "The TLM is in an Ignition On Engine On working condition"],
         "NA",
         ["Bring the TLM to the status related to TLM audio is OFF",
          "Read the ICS functions and the DTV to check their availability"],
         ["ICS functionalities are available",
          "DTV is OFF"],
         "P1", "本條驗 ICS 與 DTV 之可用性"),
    ],
    "SWE-PM-104": [
        ("The splash and disclaimer screens appear on the first transition to Timed",
         [SIM, "A new bus cycle has started",
          "Neither screen has been shown in this bus cycle"],
         "NA",
         ["Bring the HU to Timed mode for the first time in the bus cycle",
          "Read the screen sequence to check both startup screens"],
         ["The splash screen is shown",
          "The disclaimer screen is shown"],
         "P0", "本條驗首次進入 Timed"),
        ("The splash and disclaimer screens appear on the first transition to Full Operation",
         [SIM, "A new bus cycle has started",
          "Neither screen has been shown in this bus cycle"],
         "NA",
         ["Bring the HU to Full Operation mode for the first time in the bus cycle",
          "Read the screen sequence to check both startup screens"],
         ["The splash screen is shown",
          "The disclaimer screen is shown"],
         "P0", "本條驗首次進入 Full Operation"),
        ("The disclaimer appears on the first transition from Idle",
         [SIM, "The HU is in Idle mode", "The disclaimer needs to be shown"],
         "NA",
         ["Bring the HU from Idle to Timed mode for the first time in the bus cycle",
          "Read the screen to check the disclaimer presentation"],
         ["The HU reaches Timed mode",
          "The disclaimer screen is shown"],
         "P0", "本條驗來源狀態 Idle"),
        ("The disclaimer appears on the first transition from Standby",
         [SIM, "The HU is in Standby mode", "The disclaimer needs to be shown"],
         "NA",
         ["Bring the HU from Standby to Timed mode for the first time in the bus cycle",
          "Read the screen to check the disclaimer presentation"],
         ["The HU reaches Timed mode",
          "The disclaimer screen is shown"],
         "P0", "本條驗來源狀態 Standby"),
        ("The disclaimer appears on the first transition from Partial Operation",
         [SIM, "The HU is in Partial Operation mode", "The disclaimer needs to be shown"],
         "NA",
         ["Bring the HU from Partial Operation to Full Operation for the first time",
          "Read the screen to check the disclaimer presentation"],
         ["The HU reaches Full Operation mode",
          "The disclaimer screen is shown"],
         "P0", "本條驗來源狀態 Partial Operation"),
    ],
    "SWE-PM-105": [
        ("An ongoing call temporarily skips the disclaimer and splash screens",
         [SIM, "A new bus cycle has started"],
         "An ongoing call at the moment of the transition",
         ["Bring the HU to Timed mode while the event listed in Input Test Data holds",
          "Read the screen to check whether the startup screens appear"],
         ["The HU reaches Timed mode",
          "The disclaimer and splash screen are temporarily skipped"],
         "P0", "本條驗通話類之暫時略過"),
        ("A backup camera view temporarily skips the disclaimer and splash screens",
         [SIM, "A new bus cycle has started"],
         "A backup camera view at the moment of the transition",
         ["Bring the HU to Timed mode while the event listed in Input Test Data holds",
          "Read the screen to check whether the startup screens appear"],
         ["The HU reaches Timed mode",
          "The disclaimer and splash screen are temporarily skipped"],
         "P1", "本條驗非通話類之暫時略過"),
        ("An incoming call temporarily skips the disclaimer and splash screens",
         [SIM, "A new bus cycle has started"],
         "An incoming call at the moment of the transition",
         ["Bring the HU to Timed mode while the event listed in Input Test Data holds",
          "Read the screen to check whether the startup screens appear"],
         ["The HU reaches Timed mode",
          "The disclaimer and splash screen are temporarily skipped"],
         "P1", "本條驗 incoming call 支（R-P118(d) 補測）"),
        ("An outgoing call temporarily skips the disclaimer and splash screens",
         [SIM, "A new bus cycle has started"],
         "An outgoing call at the moment of the transition",
         ["Bring the HU to Timed mode while the event listed in Input Test Data holds",
          "Read the screen to check whether the startup screens appear"],
         ["The HU reaches Timed mode",
          "The disclaimer and splash screen are temporarily skipped"],
         "P1", "本條驗 outgoing call 支（R-P118(d) 補測）"),
        ("A climate pop-up temporarily skips the disclaimer and splash screens",
         [SIM, "A new bus cycle has started"],
         "A climate pop-up at the moment of the transition",
         ["Bring the HU to Timed mode while the event listed in Input Test Data holds",
          "Read the screen to check whether the startup screens appear"],
         ["The HU reaches Timed mode",
          "The disclaimer and splash screen are temporarily skipped"],
         "P1", "本條驗 climate pop-ups 支（R-P118(d) 補測）"),
        ("An SOS or Assist call temporarily skips the disclaimer and splash screens",
         [SIM, "A new bus cycle has started"],
         "An SOS or Assist call at the moment of the transition",
         ["Bring the HU to Timed mode while the event listed in Input Test Data holds",
          "Read the screen to check whether the startup screens appear"],
         ["The HU reaches Timed mode",
          "The disclaimer and splash screen are temporarily skipped"],
         "P1", "本條驗 SOS and Assist calls 支（R-P118(d) 補測）"),
        ("A FOTA pop up temporarily skips the disclaimer and splash screens",
         [SIM, "A new bus cycle has started"],
         "A FOTA pop up at the moment of the transition",
         ["Bring the HU to Timed mode while the event listed in Input Test Data holds",
          "Read the screen to check whether the startup screens appear"],
         ["The HU reaches Timed mode",
          "The disclaimer and splash screen are temporarily skipped"],
         "P1", "本條驗 FOTA pop ups 支（R-P118(d) 補測）"),
        ("The skipped screens are displayed at the next transition in the bus cycle",
         [SIM, "The startup screens were skipped earlier in this bus cycle"],
         "NA",
         ["Bring the HU to Full Operation mode again within the same bus cycle",
          "Read the screen to check the deferred presentation"],
         ["The HU reaches Full Operation mode",
          "The skipped screens are displayed at this transition"],
         "P0", "本條驗延後補顯之義務"),
    ],
    "SWE-PM-106": [
        ("The SOS button variant selects the SOS disclaimer text",
         [SIM, "The HU is configured for a disclaimer screen variation"],
         '$Ecall_Button_Variant$: "SOS"',
         ["Send the value listed in Input Test Data",
          "Read the disclaimer wording to check which text the HU uses"],
         ["The HU accepts the configuration value",
          "The HU uses the SOS text for the disclaimer"],
         "P0", "本條驗 SOS 變體"),
    ],
    "SWE-PM-107": [
        ("The help button variant replaces the SOS text in the disclaimer",
         [SIM, "The HU is configured for a disclaimer screen variation"],
         '$Ecall_Button_Variant$: "Help"',
         ["Send the value listed in Input Test Data",
          "Read the disclaimer wording to check which text the HU uses"],
         ["The HU accepts the configuration value",
          'The HU replaces the "SOS" text with the "Help" version of the disclaimer'],
         "P0", "本條驗 Help 變體"),
    ],
    "SWE-PM-108": [
        ("A non Maserati brand shows the core disclaimer once every thirty ignition cycles",
         [SIM, '$VC_VEH_BRAND$ reads a value other than "Maserati"'],
         "NA",
         ["Run the head unit through consecutive ignition cycles",
          "Read the screen across the cycles to check how often the disclaimer appears"],
         ["The core disclaimer screen is shown on the first ignition cycle",
          "The core disclaimer screen is shown only once every 30 ignition cycles"],
         "P0", "本條驗免責畫面之顯示頻率"),
    ],
    "SWE-PM-109": [
        ("A GDPR market with the TBM present follows the GDPR non Maserati startup flow",
         [SIM, '$VC_VEH_BRAND$ reads a value other than "Maserati"',
          '$TBM_Present$ reads "Present"',
          "$Country_Code$ is marked as a country needing the combined Geolocation plus SOS Popup"],
         "NA",
         ["Bring the HU through the startup sequence",
          "Read the startup flow against the HMI to check which flow is followed"],
         ["The HU reaches the startup presentation",
          "The HU follows the GDPR Non-Maserati startup flow in the HMI"],
         "P0", "本條驗 GDPR 流程"),
    ],
    "SWE-PM-110": [
        ("A missing TBM follows the non GDPR non Maserati startup flow",
         [SIM, '$VC_VEH_BRAND$ reads a value other than "Maserati"',
          '$TBM_Present$ reads "Not Present"'],
         "NA",
         ["Bring the HU through the startup sequence",
          "Read the startup flow against the HMI to check which flow is followed"],
         ["The HU reaches the startup presentation",
          "The HU follows the Non-GDPR/Non-Maserati Startup flow in the HMI"],
         "P0", "本條驗 OR 之左支 TBM Not Present"),
        ("An unmarked country follows the non GDPR non Maserati startup flow",
         [SIM, '$VC_VEH_BRAND$ reads a value other than "Maserati"',
          '$TBM_Present$ reads "Present"',
          '$Country_Code$ is not marked as one of the "Countries which need the '
          'combined Geolocation plus SOS Popup" in the Market Configuration Table'],
         "NA",
         ["Bring the HU through the startup sequence",
          "Read the startup flow against the HMI to check which flow is followed"],
         ["The HU reaches the startup presentation",
          "The HU follows the Non-GDPR/Non-Maserati Startup flow in the HMI"],
         "P0", "本條驗 OR 之右支 country 未標記"),
    ],
    "SWE-PM-111": [
        ("A missing TBM adds the ADAS text to the disclaimer",
         [SIM, "The screen size is other than 7 inch",
          '$VC_VEH_BRAND$ reads a value other than "Maserati"',
          '$TBM_Present$ reads "Not Present"'],
         "NA",
         ["Bring the HU to the disclaimer presentation",
          "Read the disclaimer wording to check the added text"],
         ["The disclaimer screen is shown",
          "The HU adds the ADAS text to the disclaimer"],
         "P1", "本條驗 OR 之左支 TBM Not Present"),
        ("A country not requiring SOS or geolocation adds the ADAS text",
         [SIM, "The screen size is other than 7 inch",
          '$VC_VEH_BRAND$ reads a value other than "Maserati"',
          "$Country_Code$ does not require SOS or Geolocation"],
         "NA",
         ["Bring the HU to the disclaimer presentation",
          "Read the disclaimer wording to check the added text"],
         ["The disclaimer screen is shown",
          "The HU adds the ADAS text to the disclaimer"],
         "P1", "本條驗 OR 之右支 country 不需 SOS 或 Geolocation"),
    ],
    "SWE-PM-113": [
        ("A geolocation and SOS market adds the ADAS and SOS text",
         [SIM, "The screen size is other than 7 inch",
          '$VC_VEH_BRAND$ reads a value other than "Maserati"',
          '$TBM_Present$ reads "Present"',
          "$Country_Code$ requires geolocation and SOS in the disclaimer"],
         "NA",
         ["Bring the HU to the disclaimer presentation",
          "Read the shown wording to check what the HU adds"],
         ["The geolocation pop-up or the disclaimer is shown",
          "The HU adds the ADAS and SOS to the geolocation pop-up or disclaimer"],
         "P0", "本條驗 geolocation ＋ SOS 之附加"),
    ],
    "SWE-PM-114": [
        ("An incoming call from IDLE bypasses the not yet shown disclaimer screen",
         [SIM, "The HU is in IDLE mode", "The disclaimer screen has not yet been shown"],
         "An incoming phone call",
         ["Let the bench place the call listed in Input Test Data",
          "Read the HU mode and the screen to check whether the disclaimer appears"],
         ["The HU transitions from IDLE to FULL OPERATION",
          "The disclaimer screen is bypassed"],
         "P0", "本條驗來電所致之 IDLE → FULL OPERATION 免顯免責畫面"),
    ],
    "SWE-PM-115": [
        ("The disclaimer bypassed for a call is shown at the next FULL OPERATION",
         [SIM, "The HU is in IDLE mode", "The disclaimer has not yet been shown"],
         "An incoming phone call that then becomes inactive",
         ["Let the bench place and then end the call listed in Input Test Data",
          "Bring the HU to FULL OPERATION again and read the screen to check the disclaimer"],
         ["The HU bypasses the disclaimer for the call and returns to IDLE",
          "The disclaimer is shown at the next transition to FULL OPERATION"],
         "P0", "本條驗免責畫面之延後補顯"),
    ],
}


def numbered(items: list[str]) -> str:
    return "\n".join(f"{i}. {s}" for i, s in enumerate(items, 1))


# **本批之 leaf 全集**（R-P181(e) / R-P177(b)：逐一列出，不以區間表述）。
# 其derivation 為 25 包當時之 G121 對帳表：Power State 未產出且未受阻斷者 10、
# Startup Display 未產出者 20 扣除撞上 DR-PW9 之 `SWE-PM-112`，共 29。
# **此處凍結為明列**——對帳表於本批產出後即將該 29 leaf 標為「已產出」，
# 若仍自表推導則回傳空集（26 包重跑時實測發現，已於上繳登記）。
INCLUDE = sorted(TCS)


def main() -> None:
    include = INCLUDE
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
                "reasoning_note": NOTES.get(leaf, ""),
                "split_index": idx,
            })
            n += 1

    batch = {
        "batch": BATCH,
        "test_group": "Power Management",
        "test_set": "Startup Display / Power State",
        "tc_id_status": "provisional",
        "tc_id_note": "R-P113(b)：本批之 `tc_id` 為批次內臨時號，接續第四批之末（157）。"
                      "JSON 陣列序維持遞增（§10.3 / G38）；寫回列序另由 "
                      "(SWE-PM ID, split_index) 決定。",
        "scope_note": "範圍**取自 G121 對帳表**（R-P177(b)，不以 ID 區間表述）："
                      f"Power State 未產出且未受阻斷者 ＋ Startup Display 未產出者，"
                      f"扣除撞上 live DR 影響面者（`SWE-PM-112` / DR-PW9，R-P181(c)）"
                      f"與已於第四批產出者（`SWE-PM-053`–`056`，R-P177(a) 不重做）。"
                      f"**本批 {len(leaves)} leaf**，leaf ID 全集見上繳 §四。",
        "leaves": leaves,
        "tcs": tcs,
    }
    path = GENERATED / f"{BATCH}.json"
    path.write_text(json.dumps(batch, ensure_ascii=False, indent=1) + "\n",
                    encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {len(leaves)} leaf / {len(tcs)} TC "
          f"（{tcs[0]['tc_id']} – {tcs[-1]['tc_id']}）")


if __name__ == "__main__":
    main()
