# DATA REQUESTS — Power (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/power/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

來源：下放包 01 §G、02 §G、06 §G。撤回列不刪、不重編號，保留作為裁決跡證。

| DR | Urgency | 內容 | 阻斷何物 | Anomaly |
|---|---|---|---|---|
| DR-PW1 | **High（live）** | `SWE-PM-089` 之真實上游來源為何？（`SWE1-PM-ANT-008` 非 SYS2 id） | 該 leaf 之 TC 及其 `specification_reference` | A-PW01 |
| DR-PW2 | **撤回** | SYS2 匯出之**收錄規則**為何？—— 包含（a）CFTS009 `Sys-RA-PM-0197`–`0206` 連續十條缺失；（b）CFTS009 本文 904 條需求中未被引用之 547 條內，有 **140 個需求錨點**標 `EE Architecture: Atlantis High/Mid`（`Atlantis High, Atlantis Mid` 73 + `Atlantis Mid, Atlantis High` 67，二者為同一集合之不同排序寫法），似不應被濾掉。**（R-P7 撤回：範圍 = 037 之 115 leaf）** | 已解除 | — |
| DR-PW3 | **Medium（live）** | `Sys-RA-PM-0334` 引用之 `4942087` 屬何文件？ **交叉指引（R-P151，23 包）**：本 DR 與 **A-PW02**、**G103 / G114**（layer3 靜默丟棄）、**DR-PW11**（四個文字層不存在之 item）為同一形態之四處記載。 | A-PW02 | A-PW02、A-PW120 |
| DR-PW4 | **撤回** | 037 `Priority` 之 `High`/`Medium` 如何映射至 FW036 `P0`–`P3`？**（R-P8 撤回：priority 依 TC 測項判定）** | 已解除 | — |
| DR-PW5 | **High（live）** | **CFTS009 §1.6.2.1.4 Stolen Vehicle Mode —— 範圍內而未被涵蓋。** `SWE-PM-003`（Partial Operation）經 `Sys-RA-PM-0031` 引用該章之 `4941400`，其全文為「the R1 HU shall not enter stolen vehicle mode under any condition」（`Radio` 欄含本專案車型 `R1L`，`Model Year` 2021–2025）。而 `SWE-PM-003` 之 Requirement Description 全文為 Partial Operation 之電源政策（Display / audio / BT / Tuner / USB / AUX），**無一字涉及 stolen vehicle mode**。請上游澄清：此否定需求應由哪一個 SWE leaf 承接？或確認其不需 TC。 | `SWE-PM-003` 之 TC 是否須涵蓋該否定需求 | A-PW16、R-P43(c) |
| DR-PW6 | **Medium（已結案，49 包）** | **31 處懸空 `WrapperResource` 參照 —— 請補提供缺漏之**嵌入資源（RTF / 試算表 / Word 文件）**或其等效內容。** CFTS009 16 處、CFTS010 15 處，分布 **16 個章節**。二份文件經實測**皆無任何嵌入物件**（CFTS009 無 `word/embeddings/`、`w:object`/`w:drawing`/`w:pict`/`o:OLEObject` 各 0；CFTS010 之 OLE2 目錄無 `ObjectPool`、無 `\x01Ole`），故該等 `… WrapperResource` 為**純字面之懸空參照**，所指資源未隨文件匯出。**型別實測（07 包 G34）**：`.rtf` 14、`.xls` 15、`.xlsx` 1、`.doc` 1 —— 試算表為多數（原稱「RTF 資源」為誤，見 A-PW32）。**影響面（依 R-P45 先完成 leaf 層交叉）**：31 處中**僅 2 處**落在被引用之錨點下 —— 皆位於 **CFTS009 §1.6.2.1 `TLM algorithm requirements`**（錨點 `4941354` / `4941355`），**觸及 9 個 leaf**（`SWE-PM-001`–`009`），全屬 **Power State**。其餘 29 處落在未被引用之錨點下，依 **R-P42** 不在測試範圍內。 | §1.6.2.1 之 9 個 leaf 其 TC 之 `specification_reference` 無可引之規格文字（B2 v2 判為「無法判定」） | A-PW23、A-PW26、R-P44、R-P45 ｜ **結案（49 包，依 R-P317 / §G）**：Pei 已提供其**阻斷 `SWE-PM-001`–`009` 之二份資源** —— `4942177-_CFTSMV009_CIP_R4_O829_4_inline.rtf`（10,083,195 bytes，SHA256 `a29fe63963192b80…`）與 `4942178-_CFTSMV009_CIP_R4_O1584_5_inline.rtf`（1,048,356 bytes，SHA256 `dede965f228429c6…`），即錨點 `4941354` / `4941355` 之實體。二者皆為 Visio 圖，已轉出 WMF / JPEG 入 `inputs/derived/`，**執行層獨立重跑之輸出與分析層所產位元組相同**（G226）。**其阻斷解除者為 8 個 leaf** —— `SWE-PM-008` 另受 **DR-PW11** 阻斷，仍未產出。⚠ **本 DR 原載之 31 處懸空參照，其餘 29 處未獲提供** —— 依 R-P42（06 包）該 29 處不在測試範圍內，故本 DR 就其阻斷面結案，**非就其全部參照結案** |
| DR-PW7 | **Low（live）** | **`Verification Criteria` 欄品質。** G28 基線實測：VC 單欄不可執行 **2 / 115**、VM 單欄不可執行 **0 / 115**、**二欄合觀不可執行 0 / 115**。兩筆為 `SWE-PM-007`（「Vehicle not equiped with CAN or engineering line is active」）與 `SWE-PM-008`（「Vehicle equiped with CAN」），皆僅為泛稱環境陳述而無可操作條件。二者之 VM 欄均為可執行，故**不阻斷任何 leaf 之 TC 撰寫**。 | 不阻斷。僅影響該二 leaf 之 Pre-Conditions 欄品質 | A-PW28、R-P49 |
| DR-PW8 | **High（live）** | **`4942354` 之 `voltage out of range conditions` 未載電壓門檻值。** 該錨點載「Unless defined otherwise, TLM shall stay in this state until either **voltage out of range conditions are satisfied** or shall go back to normal behavior 10 seconds after `STATUS_LIN.Batt_ST_Crit` becomes [0h]」——**僅載條件之名稱，未載電壓值或其判準**。依 §8.4.1 不得造容差／門檻值，依 R-P42 不得赴其他未被引用之錨點取值。請上游提供該條件之定義（電壓上下界、持續時間、或其所引之文件與章節）。 | `NR1L-PowerManagement-015`（Battery Critical 之第一回復分支）**可撰寫而不可執行** —— 該條已於 `remarks` 標明此狀態，使其於工作簿內可見 | A-PW83、R-P121 |
| DR-PW10 | **Medium（live）** | **`SWE-PM-038` 三對成對錨點之 `Model Year: 2017` / `State: Under Review` 是否適用本案。** `4941728` / `4941730` / `4941736`（含 `RemStartFail` 處置之一側）**全部帶 `Model Year: 2017` 且 `State: Under Review`**，而其對造（`4941727` / `4941729` / `4941735`）或無 `Model Year`、或 `State: New`。二項疑點：（a）`Model Year: 2017` 出現於 25PI3.5 專案，需解釋；（b）`State: Under Review` 非最終狀態，而 SYS2 匯出**無 `State` 欄**（20 §2.1 已證），**故本專案之範圍判定從未看過此欄**。 | 不阻斷撰寫。`037` / `039` / `042` 三條之最終內容（是否保留）待此澄清；三條之 `remarks` 已標記 | A-PW112、R-P153 |
| DR-PW11 | **High（live）** | **`SWE-PM-010` 之被引用錨點 `4941984` 不存在於 CFTS 本文。** 037 之 `Source Requirement ID` 經 SYS2 解析得 8 個 item id，其中 `4941984` **於 CFTS009 / CFTS010 之文字層皆無內文段落、亦無所屬章節**（鄰近之 `4941983` / `4941985` 皆存在）。`layer3_full.tsv` 因其無法解析至章節而**靜默丟棄**該 item，致 `source_anchor` 僅 7 個。請上游確認：該 item 是否應存在於 CFTS009？或 SYS2 之對應有誤？ **（23 包 G114 全量掃描擴大）**：115 leaf 中不相等者共 **2** —— `SWE-PM-010` 缺 `4941984`、**`SWE-PM-008` 缺 `4941425` / `4941430` / `4941433`**；**四個 item 於兩份 CFTS 文字層皆無內文段落**。與 A-PW02 / DR-PW3（`4942087`）同型。 | **`SWE-PM-010` 與 `SWE-PM-008` 之 TC 全部**（其 `source_clause` 無法完整，反向涵蓋於原理上不成立）——二 leaf 皆已自第三批排除 | A-PW113、R-P144、**A-PW120** |
| DR-PW9 | **High（live）** | **SYS2 CFTS009 匯出之 `HARMAN Status` 含 4 列 `Need rework`，而其檔名為 `All_Accepted` —— 檔名與內容不符。** 四列為 `Sys-RA-PM-0021` / `0291` / `0292` / `0293`。（a）該匯出之收錄條件究竟為何？`All_Accepted` 所指者為哪一欄？（b）037 引用其中之 `Sys-RA-PM-0293`（其 `HARMAN Status` 逐字為 `Need rework`、`MD Status` 為空），對應 `SWE-PM-112` —— 該 leaf 是否仍在範圍內？ | **阻斷 `SWE-PM-112` 之 TC 撰寫**（R-P185，26 包修訂）—— 其範圍歸屬未定。立條理由 R-P148 逐字載「Urgency High —— 其影響 `SWE-PM-112` 之 TC 可否撰寫」，**該阻斷意旨原未為本欄之措辭所承接**，致 25 包執行層須以保守解自行排除（25 §十一第 1 項）。**不阻斷其他已產出之 leaf**（該四 token 皆不在其中）| A-PW110、R-P148 |

| DR-PW12 | **Medium（live）** | **037 之五對 SWE leaf 引用完全相同之需求錨點 —— 是否為有意之相異需求？** `SWE-PM-097`≡`SWE-PM-056`（`4941680`）、`SWE-PM-101`≡`SWE-PM-054`（`4941673`–`4941676`）、`SWE-PM-102`≡`SWE-PM-055`（`4941678`）、`SWE-PM-114`≡`SWE-PM-068`（`4941876`）、`SWE-PM-115`≡`SWE-PM-070`（`4941878`）—— 五對之 `source_anchor` **完全相同**，`source_clause` 逐字一致。全量掃描：238 個被引用錨點中 **28 個被 >1 個 leaf 引用**。請上游確認：該五對是否為 037 之重複登載，抑或各自代表相異之 SW 需求？ | 五對之其中一側是否應改依 §8.2.1 委由對造承擔（將減少約 9 條 TC）。**不阻斷撰寫** —— 五個 leaf 之 TC 已產出並標記 | A-PW137 | **【39 包增列待答項，R-P270(b)】**：該五對之 TC 內文**逐字全同**（`152`/`196`、`153`/`197`、`154`/`198`、`155`/`199`、`156`/`200`、`157`/`201`、`165`/`229`、`168`/`230` 八組；另 `158`/`189` 僅措詞微差），其中**六組連 `tc_title` 亦逐字相同**。R-P263(a) 原令加區別語，惟二 leaf 之 `section` / `source_anchor` / `source_clause` 三者全同，**無語義材料可資區別** —— 逕加即為造值（§8.4.1）。**故本 DR 之答覆將決定該 8 組標題是否需分化**：若判為相異需求，須由 RD 指出其側重之別；若判為重複登載，則其一應撤除。在此之前，工作簿中將存在 **8 組同標題而不同 Requirement ID 之列**，此為**已知且待答**，非疏漏（已載入交付說明之驗證邊界）。 | **【批 1 覆核增列，05 包 §二】第六對：`SWE-PM-080` ≡ `SWE-PM-086`。**工作簿 rows 210/225（TC `PowerManagement-201`/`216`）與 rows 211/226（TC `-202`/`-217`）之 test_item 上半、括號下半、pre／input／proc／er 四欄**逐字全同**，僅 Requirement ID 與 row 210 之 Priority（P0 vs P1）相異。依 §8.2.1 不得由 TC 側合併或刪列 —— 刪任一側將使該 leaf 失去覆蓋。TC 側維持現狀，待上游答覆。（分析層 04 包覆核；原登記編號 A-PM04 撤銷，併入本 DR。） **【18 包增列第七對：`SWE-PM-070`（row 181）≡ `SWE-PM-115`（row 293）】** 二列之 pre／input／proc／er 逐字全同（軌 C 改寫後仍同），僅 Requirement ID 相異，登記為 **A-PM14**。`SWE-PM-115` 即 A-PM12 所載 037 `Source Requirement ID` 欄空白之該條。依 §8.2.1 TC 側不得合併或刪列，兩列各自寫入。⚠ 執行層註：rows 210/225 之 proc 已於批 2 依 M17 改寫（`Observe` → `Read … and record`），二列改寫後仍逐字相同，重複狀態未因回修而改變。

| DR-PW13 | **撤回（26 包）** | 原擬詢問本專案之品牌 / 車型 / 螢幕尺寸 / 機型適用性值。**其中品牌一項已由 R-P197 直接裁定為 `Jeep`，該條明令「不開 DR」**，故本 DR 於開立同包內撤回，不送上游。**未被 R-P197 涵蓋之三項**（`$VC_VEH_LINE$` 之 `DT` / `M240`、螢幕尺寸之 `7 inch`、機型之 `LTM High Radio`）**改登記於 A-PW141 待裁**，不另開 DR。 | 無 —— 相關 TC 已產出，各該 leaf 之 `reasoning` 已載其處理 | R-P193、**R-P197** |

| DR-PW14 | **Medium（live）** | **`SWE-PM-094`（CFTS009 §1.9.8 / `4941942`）之「開機動畫與 Splash / 免責畫面分開呈現」是否隨 HU 起始模式而異？** 其 clause 逐字為 `The HU shall display the startup animation separately from the Splash screen and disclaimer screen.` —— **完全未提任何模式**。而開機動畫之播放條件由 `SWE-PM-093`（`4941301` / `4941941`）定義為 `SLEEP MODE`、`STANDBY MODE` 或 `PARTIAL OPERATION MODE` 三者之一加車門關閉。本專案之 TC（`NR1L-PowerManagement-187`）取 `STANDBY MODE` 為起始模式 ——**該選擇之依據為他 leaf 之明文，而「分開呈現」之關係是否隨模式而異，規格一字未載**。請上游確認：（a）該呈現關係於三個模式下是否一致？（b）若否，另二模式是否須各立 TC？ | **不阻斷** —— 該條已產出並依 R-P210 標為待查；**若答案為「隨模式而異」，須補測 `SLEEP` 與 `PARTIAL OPERATION` 二模式** | A-PW152、**R-P210** |

| DR-PW15 | **Medium（live）** | **`Theme Mode` 設定與 `$Day_Night_Mode$` 訊號衝突時之行為未定義。** CFTS009 §1.9.17 三條之 clause 逐字為：`SWE-PM-090` `If the "Theme Mode" setting is set to "Auto" the HU shall use the $Day_Night_Mode$ to determine which of the themes to show`；`SWE-PM-091` `If the "Theme Mode" setting is set to "Day" the HU shall use the Day theme`；`SWE-PM-092` 同構之 Night 版。**即：`Auto` 時明文跟隨訊號，而 `Day` / `Night` 時是否無視該訊號，規格一字未載** ——無 `regardless` / `override` / `irrespective` / 優先序一類措詞（已逐詞掃描確認）。請上游確認：`Theme Mode` 設為 `Day` 而 `$Day_Night_Mode$` 指向夜間時，HU 應採何主題？ | **不阻斷** —— `NR1L-PowerManagement-257` / `258` 已依 R-P211 改為僅驗 clause 所載之行為。**惟「設定能否覆蓋訊號」因而無任何 TC 涵蓋** —— 此即 R-P216 所指之「合規修正所留下之涵蓋缺口」，本 DR 即其登記；**若上游確認該覆蓋機制存在，須補測二條** | A-PW157、**R-P211**、**R-P216** |
| DR-PW16 | **Low（live）** | **VF570 未尋獲 —— `AL_OR_Plus` 內部訊號之定義文件。** CFTS009 引用 6 次。本批（批 1）之訊號記法回修全部命中 `02_pm_signal_map.md` 對照表，表外訊號 0 種，故本 DR **不阻塞批 1**。需其定義始能判定該訊號屬內部訊號層抑或 CAN 層（影響 R-1 之三層歸屬）。 | 不阻塞。`AL_OR_Plus` 之 R-1 層級歸屬待定 | — |
| DR-PW17 | **Low（live）** | **VF601 未尋獲 —— LOGISTICS MODE 之定義文件。** CFTS009 引用 6 次；`LTM.doc` 內僅見交叉引用、無章節本體，研判屬 BCM 側 VF 集（分析層研判，執行層未獨立複驗）。本批未觸及其內容。 | 不阻塞批 1 | — |
| DR-PW18 | **Low（live）** | **VF665 未尋獲 —— Customer setting screens 之定義文件。** CFTS009 引用 1 次；`LTM.doc` 內 0 次出現。本批未觸及其內容。 | 不阻塞批 1 | — |
| DR-PW20 | **Medium（live）** | **四列之轉態目標值於 CFTS009／010 原文僅載為類別，未載具體值。** rows 73／74（`LTM_OperationalModeSts.Info has a transition from "Ignition Off" to another value`）、row 245（`becomes different from "SNA" value again`）——「another value」／「different from SNA」各為 `OperationalModeSts` 15 個 VAL_ 中之任一，擇其一即為依情境推定，違 Pei 之路線 (c) 裁定（值一律取自來源）。row 119 之送出值 `15 (SNA)` 明載可填，**惟其結果之 `PowerSts_Telematic` 值未載** —— 原文僅稱「behave as an Ignition Pre Off or Ignition Off event occurs, according to par. TLM Operative state management」，須跨章取值。請上游就四列各指出應驗之具體值（或確認其為「任一非該值」之等價類，此時請指定代表值）。 | **不阻斷撰寫** —— 四列已改寫完成，各餘一格標 `PENDING: DR-PW20`（rows 73／74／119／245，見上繳 16） | — |
| DR-PW21 | **High（live）** | **`PowerModeSts_Telematic` 為規格明載訊號，兩份 DBC 皆查無同名。** `CFTS009-4941562`（`SWE-PM-022` 錨點）逐字載「AND signal PowerModeSts_Telematic passes from "Standard_Power" to "Logistic_Mode_On"」。BH-CAN（sha256 `9ef1ec98…30d0`）與 FD-CAN8（`51c8fd60…1cd2`）皆無此名；相近者為 `STATUS_TELEMATIC.PowerSts_Telematic`（TLM 自身電源狀態）與 `STATUS_BH_BCM1.PowerModeSts`（BCM 側車輛電源模式，VAL_ 0 Standard_Power／1 Logistic_Mode_ON／2 Logistic_Mode_PR／3 LogisticModeON_and_EngineON）——**後者之 VAL_ 與原文之二值逐字相符**。請上游確認 `PowerModeSts_Telematic` 之 message 歸屬與 VAL_ 定義，或確認其是否即 `PowerModeSts`。 | **不阻斷撰寫** —— row 72 依 **R-13** 保留原文名稱（不加 `$`），可撰寫而**不可執行至訊號層** **【20 包 §三 證據補強（分析層實測）】** DBC 實查（BH-CAN sha256 `9ef1ec98…30d0`；FD-CAN8 `51c8fd60…1cd2`）：`VAL_ 854 PowerModeSts 0 "Standard_Power" 1 "Logistic_Mode_ON" 2 "Logistic_Mode_PR" 3 "LogisticModeON_and_EngineON"`。CFTS009-4941562 原文：`signal PowerModeSts_Telematic passes from "Standard_Power" to "Logistic_Mode_On"`。→ **二值逐字相符（僅 ON/On 大小寫）**。研判 `PowerModeSts_Telematic` 即 `STATUS_BH_BCM1.PowerModeSts`（BH-CAN），規格加 `_Telematic` 後綴。**請上游確認。**若確認，row 72 應改：`PROC 1: Send the signal $STATUS_BH_BCM1.PowerModeSts$ = 0 (Standard_Power)`／`PROC 2: … = 1 (Logistic_Mode_ON)`，觸發（BCM 側）與觀察（TLM 側 `PowerSts_Telematic`）之因果結構即回復。⚠ **現行寫法在 R-13 下正確，維持不動** —— 證據強度雖高，「規格名 = DBC 某訊號」之認定屬上游職權，分析層不代為認定（§8.4.1）。 | — |
| DR-PW22 | **Medium（live）** | **`SWE-PM-113`（row 291）之「geolocation pop-up 或 disclaimer」二擇一判準未載。** 原 ER 作二擇一表述，而來源未載何時顯示何者。依 R-11(b)「須寫出應觀察之值」，二擇一即判準不唯一。請上游指出該情境下應顯示者，或指出其擇一條件。 | **不阻斷撰寫** —— row 291 之 PROC 2／ER 2 標 `PENDING: DR-PW22`，其餘三步完整 | — |

**本表現存 live 項：DR-PW1（High）、DR-PW5（High）、DR-PW8（High）、**DR-PW9（High）**、**DR-PW11（High）**、DR-PW3（Medium）、DR-PW6（Medium）、**DR-PW10（Medium）**、**DR-PW12（Medium）**、**DR-PW14（Medium）**、**DR-PW15（Medium）**、**DR-PW20（Medium）**、**DR-PW21（High）**、**DR-PW22（Medium）**、DR-PW7（Low）。**
> **⚠ 編號偏離（03 包 §五）**：下放包指定將 VF570／VF601／VF665 登記為
> **DR-PW12／13／14**，但該三號**已被佔用** —— DR-PW12（五對 SWE leaf 引用
> 相同錨點，live）、DR-PW13（品牌值，26 包同包撤回）、DR-PW14（`SWE-PM-094`
> 起始模式，live）。依本檔 standing rule「撤回列不刪、不重編號」，
> 執行層**未覆寫**該三列，改以次一可用號 **DR-PW16／17／18** 登記。
> 三份文件之實質內容照下放包逐字登記，僅編號不同。

19 包新增 **DR-PW21**（R-13 —— `PowerModeSts_Telematic` 之 DBC 對應缺漏）與 **DR-PW22**（row 291 二擇一判準未載）。
16 包（PM 全面改寫）新增 **DR-PW20**（路線 (c) —— 四列轉態目標值原文未載）。
31 包新增 **DR-PW16／17／18**（03 §五 —— VF570／VF601／VF665 三份未尋獲文件）。
30 包新增 **DR-PW15**（R-P216(b) —— 合規修正所留下之涵蓋缺口）。
29 包新增 **DR-PW14**（R-P210(b) —— `SWE-PM-094` 之起始模式無法說明其 (ii)）。
26 包曾開 **DR-PW13** 而於同包內**撤回** —— R-P197 直接裁定本專案品牌為 `Jeep` 並明令不開 DR。
25 包新增 **DR-PW12**（A-PW137 —— 五對 leaf 共用錨點）。
22 包新增 **DR-PW10**（R-P153）與 **DR-PW11**（R-P144 之首次真實命中）。
**`DR-PW9` 已於 23 包補執行 21 包時開立**（R-P164）。
17 包新增 **DR-PW8**（R-P121）—— 首張因「TC 可撰寫而不可執行」而開之 DR。
06 包新增 DR-PW5 / DR-PW6 / DR-PW7（R-P43(c)、R-P44、R-P45、R-P49）。

> 註（02 包）：DR-PW3 之證據描述已於 ANOMALIES A-PW02 訂正 ——
> `Sys-RA-PM-0334` 之 `4942087` **可被 `\d{6,8}` 正常解析**，
> 其缺口在於該 item id 無法解析至任一 CFTS 章節，非 token 缺失。
> DR 本身之問題（`4942087` 屬何文件）不變，仍為 live。
>
> **（06 包更新）§E 已由 R-P35 定版，framework 不再有阻斷項。**
> DR-PW1 阻斷 `SWE-PM-089` 一個 leaf；DR-PW6 影響 `SWE-PM-001`–`009` 九個 leaf 之
> `specification_reference`；DR-PW5 影響 `SWE-PM-003` 一個 leaf 之涵蓋判定；
> DR-PW3、DR-PW7 不阻斷任何 leaf。
