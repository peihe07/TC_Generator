# 上繳包 14 — 窗口式解凍：同一物、發收方向、綁定三件量測（2026-08-30）

對應下放包：`docs/handoff/14_signal_identity_and_direction.md`
**開工時重測之 sha256（R-ICS17(e)）＝ `adaaad22e0287127021e4305bdc9a0af4c60d218eab299c5d261fcdabdf544c1`**
—— 與執行層自身記錄相符，未停。

**本包 git 執行次數 0**（含唯讀；主實例與一並行實例皆然）。
**E25 觸發**（作業 A）。**E22／E23／E24／E1／E9／E18 皆未觸發** —— 惟 E22 之字面涵蓋不到之
一件範圍事項已具名呈報（§3-5）。

---

## §1 裁決指紋＋前提驗證＋圍籬 diff

### 1.1 前提驗證 —— P1～P3 相符，**P4 不符**

| # | 前提 | 實測 | 判 |
|---|---|---|---|
| P1 | 相異 44、錨點 51；無重複 | **相異 44、錨點 51**；無 DUPLICATE | 相符（**E18 未觸發**）|
| P2 | A-ICS 至 90、相異 90、無缺口；DR 21／21 | **A-ICS90**／90／無缺口；**DR 21**／21／無缺口 | 相符 |
| P3 | `holder: analysis-A`、`released: null` | 同 | 相符 |
| P4 | 圍籬 diff **新增 `R-ICS44` 一條**、刪除 0 | **新增 `R-ICS43` 與 `R-ICS44` 二條**、刪除 0 | **不符 —— 二條非一條** |

**P4 之不符不需調和**：`R-ICS43`（凍結）為 b13 完工後所落，b13 快照攝於其前，
故本次 diff 必然含二條。**以實測為準，未停工。**

### 1.2 圍籬 diff（對 `13_rulings_snapshot.md`，未動用 git）

| 項 | 實測 |
|---|---|
| 快照自證 | 檔頭載 `a10e25e21d1010ec` ＝ 本文實算，**相同** |
| diff | **新增 95 行、刪除 0 行** |
| 新增 `##` 標題 | **`R-ICS43`、`R-ICS44`** |
| 刪除 `##` 標題 | **無** |

---

## §2 作業 A — 同一物（`docs/reports/14_signal_identity.md`）

### 2-1 【E25 觸發】repo 內 dbc 為**四支**，且 R1／R4／R5 世代錯配

| 代號 | 路徑 | 綁定 | 世代 | `BU_` 含 `LTM` |
|---|---|---|---|---|
| **A** | `forms/PDT27_E2A_R1_BHCAN2.dbc` | **未綁**（Pei 裁定之台架匯流排）| **R1** | **是** |
| B | `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc` | 已綁 | R4 | **否** |
| C | `features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc` | 已綁 | R5 | 是 |
| **D** | **`forms/PDT27_E2A_R1_FDCAN8.dbc`** | **未綁** | **R1** | 是 |

D 為下放包未列之第四支，含相關訊號（`DISP_STAT`／`Telematic` 命中 11）→ **E25 觸發**。
**D 非 C 之複本**：sha256 不同（`2a86c4bf…` vs `51c8fd60…`）、`SG_` 總數 1916 vs 2037。

**本 DUT 為 R1L，而已綁之二支為 R4／R5，未綁之二支為 R1。**
（就本作業之 11 個相關訊號，D 與 C 之發收方與位元佈局逐項相同，
故納入候選集不改變判定；具名以免被讀成「四支各有一套答案」。）

### 2-2 R-17(c) 三項判定表 —— **二訊號皆判「同一物」，惟三項中二項不可比**

**先報二項確定之查無**：CFTS020 全文**不載任何 CAN 訊息名**
（`TELEMATIC_DISPLAY2`／`STATUS_TELEMATIC`／`DIS_CENTERSTACK`／`RADIO_B2` 命中**各 0**），
亦不載位元位置與長度。故 **項① 與項② 對本二訊號皆為「不可比」**。

| 訊號 | 候選 | ① `BO_` | ② 位元／長度 | ③ `VAL_` | 判 |
|---|---|---|---|---|---|
| `$TGW_DISP_STAT$` | `TGW_DISP_STATSts`（`BO_ 1500`）| 不可比 | 不可比 | **相符** | **同一物** |
| `$Telematic_Power$` | `PowerSts_Telematic`（`BO_ 1470`）| 不可比 | 不可比 | **相符** | **同一物** |

**項③ 之逐項對應**（`$TGW_DISP_STAT$`）：規格側五值全部有對應，無落空 ——
`[DISP_OFF]`→`0 "Display_off"`、`[DISP_NORMAL]`→`2 "Normal_mode"`、
`[ON_BLANK]`→`8 "On_blanked_screen"`、`[DISP_REAR_CAMERA]`→`7 "Rear_Camera_Display"`、
`[SNA]`／`[Fh: sna]`→`15 "SNA"`。

`$Telematic_Power$`：`[Idle]`→`3 "Idle"`、`[Full_Operation]`→`4 "Full_Operation"` 相符；
`[BO_OFF_TGW_OFF]` **無對應**，但其唯一出處 `4820075` 為 **v2 不適用**，
故不入可比集 —— **具名不隱去**，該物件適用性若改判則項③ 須重評。

**候選可分辨**：A 檔另三個 `*DISP_STAT*`（`DCSD_`／`FPDM_`／`TGW_FPDM_`）之 `VAL_` 皆為
六值集（`OFF/ON/BLANK/…/SNA`），與規格值集不符，**由項③ 清楚分辨**。

**【E23 未觸發】** —— 不落入 R-17(d) 三情形之任一。
**但本判定僅繫於三項中之一項**；若日後取得載訊息名或位元佈局之規格件，須重驗。

### 2-3 `BHCAN2` 在規格中查無

CFTS020 載 **`BH-CAN`（54 個物件）**，例 `4819370` 逐字
`The ICS will send signals on the BH-CAN to communicate the status of the mechanical push buttons.`；
**`BHCAN2`／`CAN2` 命中各 0 —— 確定之查無**。
`BH-CAN` 與 `BHCAN2` 是否同一條匯流排，規格內無可判依據，**不調和**。

---

## §3 作業 B — 發收方向（`docs/reports/14_signal_direction.md`）

### 3-1 A-ICS87 之疑慮**成立**，且規格與 DBC 二側獨立同指

**DBC 側**：A 檔共 **14 條** `BO_TX_BU_`，**每一條之值皆為 `ETM,LTM`，無一例外**。
故其語意**不是逐訊息客製之「追加發送方」，而是一致之發送方替代集**
（該訊息由 `ETM` 或 `LTM` 發送）。佐證數 14，遠多於下放包所要之 3。

**規格側**（獨立於 DBC）：

| 物件 | 逐字 |
|---|---|
| `4819564` | `... the HU shall send the signal $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ = [current non-zero value] ...` |
| `4819459` | `... the HU shall send $TGW_DISP_STAT$ = [DISP_OFF].` |
| `4819344` | `When the HU has a loss of communication condition with the ICS, the HU shall set TGW_DISP_STAT = [Fh: sna].` |

**`$TGW_DISP_STAT$` 由 HU（本 DUT）發出** —— 二側獨立同指。

### 3-2 三 dbc 方向矩陣（自檔案重算，非轉抄）

| 訊號 | **A：BHCAN2** | B：R4（已綁）| C：R5_FDCAN8（已綁）| D：R1_FDCAN8 |
|---|---|---|---|---|
| `TGW_DISP_STATSts` | `BO_1500` `ETM`→`SGW`；`BO_TX_BU_`＝`ETM,LTM` | `BO_1500` `SGW`→`DCSD` | `BO_1427` `ETM`→`Vector__XXX` | 同 C |
| `PowerSts_Telematic` | `BO_1470` `ETM`→`FPDM,SGW`；`BO_TX_BU_`＝`ETM,LTM` | `BO_1470` `SGW`→**`AMP,ANC,DCSD,ICS`** | `BO_1427` `ETM`→`TBM` | 同 C |
| `DCSD_DISP_STAT` | `BO_1445` `SGW`→**`ETM,LTM`** | `BO_1445` `DCSD`→`SGW` | 未載 | 未載 |

與 upstream-13 §4-2 **逐項相符**（該報告未列 `BO_TX_BU_` 與 D 檔）。
三訊號首尾相接，SGW 閘道轉發可解釋，**無矛盾**。

### 3-3 【本作業最重】`$Telematic_Power$` 在裁定之匯流排上，本 DUT 收不到

CFTS020 `4819144`／`4820117`（**二者皆 v2 適用**）逐字：

> Regarding Enable Condition 1, when the ICS **receives** $Telematic_Power$ = [Idle] the ICS shall disable all Diagnostics and when the ICS **receives** $Telematic_Power$ = [Full_Operation] the ICS shall enable all Diagnostics.

| 檔 | `PowerSts_Telematic` 收方 | `ICS` 在收方？ | `ICS` 在 `BU_`？ |
|---|---|---|---|
| **A：BHCAN2（Pei 裁定）** | `FPDM,SGW` | **否** | **否**（`BU_: ETM FPDM LTM SGW`）|
| B：R4_BHCAN（未裁定）| `AMP,ANC,DCSD,ICS` | **是** | 是 |

**規格所述之「ICS 接收 `$Telematic_Power$`」在裁定之 BHCAN2 上不成立，
在未被裁定之 R4_BHCAN 上成立。** 且 A 檔 `BO_TX_BU_ 1470 : ETM,LTM` 表示
**本 DUT 在裁定之匯流排上是該訊號之發出者，非接收者**。**不調和。**

### 3-4 對 b03 八條之逐條判定 —— **八條皆「可改寫」，E22 字面未觸發**

八條之步驟一律為 `Read the display status signal on the CAN trace ...`，
ER 一律為 `The display status signal reports the "..." value on the CAN trace (supporting observation)`
—— **無一條斷言「HU 接收該訊號」**。讀 trace 對發／收兩側皆成立。

| # | tc_title | 判 |
|---|---|---|
| 1 | Power hardkey pressed while HU screen on | 可改寫 |
| 2 | Power hardkey pressed at Telematic Power full operation | 可改寫（前提問題見 §3-5）|
| 3 | Power hardkey pressed while HU screen off | 可改寫 |
| 4 | Power hardkey pressed at Telematic Power idle | 可改寫（同上）|
| 5 | Screen off hardkey starts the three second timer | 可改寫 |
| 6 | Screen off hardkey pressed again within three seconds | 可改寫 |
| 7 | Three second period completed after screen off hardkey | 可改寫 |
| 8 | Screen off hardkey pressed while HU screen off | 可改寫 |

**驗證目標皆為「DUT 於受刺激後將顯示狀態驅動至值 V」，方向敘述之改寫不改變之。**

**方向澄清反使八條變強**：DUT 既為發出者，該 ER 即非僅 `supporting observation`，
而是對 DUT 輸出之直接觀察 —— **該標記在方向確立後可能不再正確**。
改標記非本包之事（禁區：零 ER 改寫），**只列不改**。

### 3-5 E22 涵蓋不到之範圍事項 —— 具名呈報

**TC 2 與 TC 4 之前提可能在裁定之匯流排上無法建立。**
二者之前提為 `Telematic Power = Full Operation`／`= Idle`。
依 §3-3，於 BHCAN2 本 DUT 是 `PowerSts_Telematic` 之**發送側**，
`ICS` 既非收方亦不在 `BU_` 內 —— **台架無路在該匯流排上餵給 DUT 此前提值**。

此非「驗證目標改變」（故 E22 字面未觸發），而是「**前提之可建立性**」。
**屬範圍事項，須由 Pei 裁。不調和、不改寫、不推定可行。**

**且同一支 A 檔上刺激面是通的**（`BO_ 1050 CLIMATIC_PANEL` 之 `Radio_btn0` 收方僅 `LTM`）——
**刺激可觀察、前提不可餵**，此不對稱下放包未預料。

---

## §4 作業 C — 綁定之影響面（`docs/reports/14_bhcan2_binding_impact.md`）

### 4-1 `FORMS.md` 登錄 —— **另二支 dbc 根本沒有自身登錄**

BHCAN2 登於 `forms/FORMS.md` 行 465–481，使用 feature **唯一為 `display`**（R-DM19），
版次 `R1`，sha 有登，167,226 bytes，登錄值與實測 sha `46cb73f3…1cc60` **相符**。

**主實例已複驗**：`PDT27_E2A_R4_BHCAN.dbc` 與 `PDT27_E2A_R5_FDCAN8.dbc` 在 `FORMS.md` 中
**僅出現於他檔 (e) 取代關係欄**（行 477、494），**無自身登錄**。
故下放包所令之「另三支之登錄」只交付得出一支（FDCAN8-R1）。

### 4-2 `feature.yaml` 需改之鍵

`reference:` 現有 **10 鍵**（10/10 皆有 sha），`paths:` 6 鍵且**無 dbc 鍵**。
加入 BHCAN2 需改 **3 鍵**（新項＋`file`＋`sha256`），另 2 鍵（`dbc_b.file`／`.sha256`）視 A-DM14。
BHCAN2 sha256 ＝ `46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60`。

**sha 機制之實測（主實例已複驗）**：全 repo 只有 `features/display/scripts/` 與
`features/bed_lowering/scripts/` 各有一份 `verify_reference_binding.py`，
**`ics_management/scripts/` 查無** → 本 feature 之 10 個 sha **目前無任何程式比對**。

### 4-3 `display` 使用面與 **E24 未觸發**

| 項 | 實數 |
|---|---|
| 引用 BHCAN2 之檔 | **25 檔**（以完整檔名計 21 行／16 檔）|
| 腳本 | **2 支**（`dbc_probe.py`、`signal_resolution.py`，**皆硬寫絕對路徑，不讀 feature.yaml**）|
| **已交付 TC** | **0 條**（`delivered/MANIFEST.tsv` 只有表頭 1 行）|
| 未交付但已生成 | 23 條（其中帶 BHCAN2 解出訊號名者 15）|
| TC 內文對 `BHCAN2` 字面命中 | **0** |

**E24 未觸發**，三項實測依據：(1) `verify_reference_binding.py` 只讀自身 feature 之 yaml，
全 repo 查無跨 feature 擁有者檢查；(2) 同一實體檔 → 二方宣告值必同，無版本／sha 分歧；
(3) display 腳本硬寫路徑，其產出與任何 yaml 綁定無關，且**無已交付件**。
（綁定後 `FORMS.md` 行 467 之 R-G15 反向記載列須增列 `ics_management`，
但該列不在 `features/display/` 內，不構成 E24。）

### 4-4 A-DM14 之現況

正本於 `features/display/ANOMALIES.md:255–284`，狀態 **`[PENDING]`**。
repo 全域命中 41 行／21 檔，**無任何一方之結案處置**。
查無位置（各 0 命中）：`display/DECISIONS.md`、`BACKLOG.md`、`DATA_REQUESTS.md`、
全案 `docs/` 台帳、`features/vehicle_setting/`。

### 4-5 只量不綁 —— **允許**（非「部分」）

`ics_management` 讀 dbc 之腳本 **6 支**（`crossref_probe_12`／`etm_probe_07`／
`lid_dbc_probe_b04`／`lid_dbc_probe`／`pdt27_probe_13`／`variant_probe_10`）：
**硬寫路徑 6、取自 feature.yaml 0、取自參數 0**（主實例已逐支複驗，`feature_config`／
`feature.yaml` 命中皆 0）。b12／b13 已二次既成事實地讀取未綁定之 BHCAN2。
**唯一限制在條文面（不可採認入 TC），不在工具鏈。**

### 4-6 【作業 C 最重之發現】A-DM14 沒有承載它的流程

A-DM14 被宣告為跨 feature 待裁，卻**只登在 `display/ANOMALIES.md` 一處**；
其對造 `vehicle_setting`（R4 之持有者）樹下對 `A-DM14` 命中 **0**（主實例已複驗）——
**從未被告知此爭點存在**；亦未曾轉為任何 DR 發出，全案 `docs/` 命中 0。

display 線之 R-DM19 明文把跨 feature 面「推出自身範圍」，
ics 線之 R-ICS44(d) 明文「不逕裁」——
**兩線各自合規地把球讓開，而球沒有落在任何人手上。**
**等待 A-DM14 不是等待一個進行中的程序，是等待一個尚未被建立的程序。**

---

## §5 作業 D — 常設自檢集

| 項 | 結果 |
|---|---|
| 圍籬 diff | **+95／−0**；新增 `R-ICS43`、`R-ICS44` 二條（P4 預期一條，**不符已具名**）|
| 候選篩 | 原始 **140**／殘餘 **66**／**殘餘率 47%**（前五包 53／53／43／52／47%）|
| 未錨定斷言 | **3＋6**，不變 |
| `selfcheck_b01.py` | PASS —— 機檢 19 項 FAIL 0 |
| `verify_verbatim_b01.py` | PASS —— **31／31** |
| `pending_census.py` | **18 處／14 條**，不變 |
| `ledger_guard.py` | 開工前／完工後 exit 0，**逐字相同** |
| 四支 gate | 開工前／完工後**逐字相同**，差**皆 0** |
| 禁區自證 | `FORMS.md` `e127ca66…`／`feature.yaml` `ea6ed546…`／BHCAN2 `46cb73f3…` 前後未變 |
| 快照 | `docs/reports/14_rulings_snapshot.md` **已產出（回凍基準）**，51 錨點 |

### 5-1 gate 之一項變化，**與 ICS 無關，本包不碰**

開工前 `gate_all` 為 **5 支紅**（b13 為 4 支）。新紅者為 **`lint_docs036`**，其兩項為：
`features/power/DATA_REQUESTS.md:43` 表格列缺結尾 `|`（`DR-PW23`）、`DR-PW23` 序號跳號。
**成因在 `features/power/`，非 ICS 所致，非本包所致。** 前後差仍為 0。

---

## §6 預期數字對照（下放包 §5，17 項）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | `ledger_guard` 開工前 | exit 0；51（相異 44）、A-ICS 90、DR 21／21 | 全數相符 | 相符 |
| 2 | 圍籬 diff | 新增 `R-ICS44` **一條**、刪除 0 | 新增 **二條**（`R-ICS43`＋`R-ICS44`）、刪除 0 | **不符（§1.1 P4）** |
| 3 | TC 新生／錨變動／佔位回填／步驟或 ER 改寫 | 0／0／0／0 | **0／0／0／0** | 相符 |
| 4 | TC 總數 | 31 | **31** | 相符 |
| 5 | 佔位總數 | 18 處／14 條 | **18 處／14 條** | 相符 |
| 6 | `FORMS.md`／`feature.yaml`／`display/` 變動 | 0 處 | **0 處**（sha 自證）| 相符 |
| 7 | 作業 A 候選集 | 自三支 dbc 重建 | **自四支重建（E25 觸發）** | 相符（**且揭出第四支**）|
| 8 | 作業 A 判定表 | 二訊號 × 三項 | 齊；**二訊號皆同一物**，惟二項不可比 | 相符 |
| 9 | `BO_TX_BU_` 語意佐證 | 至少 3 個 | **14 個（全檔，14/14 一致）** | 相符 |
| 10 | 作業 B 對 b03 八條 | 逐條標記 | **八條皆「可改寫」**；E22 字面未觸發 | 相符 |
| 11 | 作業 C | 五項齊備；`display` 引用面有實數 | 五項齊；25 檔／2 腳本／**已交付 TC 0 條** | 相符 |
| 12 | 候選篩 | 二數並報＋殘餘率 | 140／66／**47%** | 相符 |
| 13 | 未錨定斷言 | 3＋6 | **3＋6** | 相符 |
| 14 | Test Set 相異值 | 5 | **5** | 相符 |
| 15 | 四支 gate | 差皆 0 | **差皆 0**（開工前基線由 4 紅變 5 紅，成因在 `features/power/`）| 相符 |
| 16 | **git 執行次數** | **0** | **0** | 相符 |
| 17 | 快照 | 已產出 | **已產出** | 相符 |

**16 項相符、1 項不符（#2）。** 該不符之成因為快照時點早於 `R-ICS43` 之落地，非量測失準。

---

## §7 未結 DR 清單（21 條）

| DR | 現況 | 本包新事實 |
|---|---|---|
| DR-ICS1／3／11／14／17／19／21 | OPEN | — |
| DR-ICS2 | OPEN | B5 所繫 |
| DR-ICS4 | OPEN | 1 處佔位 |
| DR-ICS5／7／10／15 | 可結 | — |
| DR-ICS6 | OPEN | 5 處佔位 |
| **DR-ICS8** | OPEN | **12 處佔位之訊號實體已定**：`TGW_DISP_STATSts`＠`BO_ 1500 TELEMATIC_DISPLAY2`（同一物，§2-2）|
| DR-ICS9 | OPEN | V1／V2／V3 所繫；**無佔位故不會自行浮出** |
| DR-ICS12 | 追蹤件 | — |
| DR-ICS13 | 分析層已標「可結」 | 執行層未動 |
| **DR-ICS16** | 匯流排軸**已結**（Pei 裁 BHCAN2）| **但 `BHCAN2` 在 CFTS020 中查無（§2-3）；且 `$Telematic_Power$` 在該匯流排上 DUT 收不到（§3-3）** |
| DR-ICS18 | 告知／追認件 | 否認則 009 ＋ 15 條加錨退回 |
| DR-ICS20 | OPEN | G2／G3 效力所繫 |

---

## §8 結果三分法

| 分類 | 項 |
|---|---|
| **改對了** | `14_signal_identity.md`／`14_signal_direction.md`／`14_bhcan2_binding_impact.md` 三份報告；回凍基準快照 |
| **核實無誤** | 二訊號皆同一物（項③ 逐值對應無落空）；`BO_TX_BU_` 14/14 一致；規格與 DBC 二側獨立同指 HU 發送；三 dbc 方向矩陣與 upstream-13 逐項相符；作業 C 之三項主張經主實例複驗（6 支腳本硬寫路徑、`verify_reference_binding.py` 不在本 feature、`vehicle_setting` 對 A-DM14 命中 0、另二支 dbc 無自身登錄）|
| **正確地不動** | 零 TC 新生／零錨變動／零佔位回填／零步驟或 ER 改寫；`FORMS.md`／`feature.yaml`／`features/display/` 一字不改（sha 自證）；BHCAN2 唯讀未複製未改名；未調和 P4 之不符、`BH-CAN` 與 `BHCAN2` 之關係、`$Telematic_Power$` 之收不到、`(supporting observation)` 標記之正確性；未對任何 DR 結案；五簿一字未寫；未碰 `features/power/` 之 gate 紅；**git 0 次** |

---

## §9 建議登錄之 anomaly（編號由分析層取）

1. **【最重】§3-3／§3-5：`$Telematic_Power$` 在裁定之 BHCAN2 上，本 DUT 是發送側而非接收側，
   `ICS` 不在該檔 `BU_` 內** —— 規格所述之「ICS 接收」在裁定之匯流排上不成立，
   TC 2／TC 4 之前提可能無法建立。
2. **【重】§4-6：A-DM14 無承載流程** —— 只登於 `display/ANOMALIES.md` 一處，
   對造 `vehicle_setting` 命中 0，未轉 DR，全案台帳命中 0。
3. **【重】§2-1 E25：repo 內 dbc 為四支，且 R1／R4／R5 世代錯配** ——
   本 DUT 為 R1L，已綁之二支為 R4／R5，未綁之二支為 R1。
4. **§2-2：CFTS020 全文不載任何 CAN 訊息名與位元佈局** ——
   R-17(c) 之項①② 對本語料**結構性地永遠不可比**，三項判準實際只有一項可用。
5. §2-3：`BHCAN2` 在 CFTS020 中查無，規格只載 `BH-CAN`（54 個物件）。
6. §4-1：`PDT27_E2A_R4_BHCAN.dbc` 與 `PDT27_E2A_R5_FDCAN8.dbc` 在 `FORMS.md` 中**無自身登錄**。
7. §4-2：`ics_management/feature.yaml` 之 10 個 sha **無任何程式比對**
   （`verify_reference_binding.py` 不存在於本 feature）。
8. §3-4：b03 八條之 `(supporting observation)` 標記在方向確立後可能不再正確。
9. §1.1 P4：下放包預期新增一條，實測二條（成因為快照時點早於 `R-ICS43`）。

**本包未產生任何新裁決條文，未自取任何編號。**

---

## §10 獨立判斷

### 10-1 本包是否仍有該驗而未驗者 —— **有，三項**

1. **`$RQ_DISP_INTS$` 之發收方未量。** 它是 b03 八條之另一佐證訊號
   （`4819564` 逐字與 `$TGW_DISP_STAT$` 並列），若其方向亦有問題，八條之判定須重評。
2. **D 檔（R1_FDCAN8）只就 11 個相關訊號與 C 比對，未作全檔差異盤點。**
   R1 與 R5 之差若涉及本線其他已用訊號（如 `CLIMATIC_PANEL` 之九個 ICS LID），
   則前十四包之訊號解析全部建立在 R5 上而 DUT 是 R1。
3. **`BH-CAN` 之 54 個物件未逐一讀。** 其中或有指明匯流排拓樸者，可解 §2-3 之查無。

### 10-2 【下放包 §6 指定】12 處佔位是否已具備回填條件（只建議不裁）

**建議：`$TGW_DISP_STAT$` 之 12 處具備，`$Telematic_Power$` 相關之二條不具備。**

**具備者**：12 處佔位皆為 `<TGW_DISP_STAT CAN signal>`，其缺件是**訊號實名**。
本包已定：`TGW_DISP_STATSts`＠`BO_ 1500 TELEMATIC_DISPLAY2`，起始位元 0、長度 4，
值 `Display_off`(0)／`Normal_mode`(2)。同一物已判、方向已明、匯流排已裁 ——
**三件齊備**。回填規模：ICS 佔位由 **18 處降至 6 處**，涉 TC 由 14 條降至 6 條。

**所需之前置有二**：
1. **值名須依 R-17(a) 改為 DBC 實值**（`DISP_OFF` → `Display_off`、`DISP_NORMAL` → `Normal_mode`）。
   本包依 R-ICS44(e) 只判不寫，**該改寫尚未發生**；回填時必須同時做，
   否則會出現「訊號名用 DBC、值名用規格」之混用。
2. **`(supporting observation)` 標記須複審**（§3-4）。

**不具備者**：TC 2 與 TC 4 雖其 `$TGW_DISP_STAT$` 佔位可填，
但其**前提** `Telematic Power = Full Operation`／`= Idle` 在裁定之匯流排上可能無路建立（§3-5）。
**先填其佔位而不解前提，會產出一條「訊號名正確但跑不起來」的 TC** ——
比留著佔位更難發現。**建議二條連同前提問題一併押後，其餘 6 條先填。**

**仍缺之一件（若要全填）**：`$Telematic_Power$` 之台架餵入路徑 ——
這需要 Pei 就「BHCAN2 之外是否另設一條前提注入路徑」再裁一次，
或確認 `BH-CAN` 與 `BHCAN2` 之關係（§2-3）。

---

## §11 引用清單

R-17(a)~(f)、R-G41(b)（全案，`docs/fw036/RULINGS_LEDGER.md`）；
R-ICS1 ~ R-ICS44（實測錨點 51／相異 44）；
A-ICS16、A-ICS31、A-ICS70、A-ICS72、A-ICS78、A-ICS82、A-ICS87、A-ICS88、A-ICS90；
A-DM14、R-DM19、R-G15；DR-ICS1 ~ DR-ICS21；R-G13、R-G17、R-G18、R-G25；
FO §8.2、FO §8.4、FO §8.5；IN §7、IN §8.7.5、IN §9、IN §10.7。
