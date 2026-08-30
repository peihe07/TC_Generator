# DR-PW23 附表（三度重做）—— forms/ 全檔段 1 重查（62 包 / R-P375）

> **取代 `data/dr_pw23_internal_signals_58.md`**（該檔保留不刪，加標）。
> 58 版之段 1 僅入 LID `CAN Mapping`（R-P368(a) 原文）；R-P375(a) 擴為
> `forms/` 全部參考檔。**命中即「候選」，非認定**（R-P375(d)）。

## 0. 段 1 之入口（G0 參考資料庫段，現 7 / 7）

| 檔 | SHA256 | 本輪讀入非空字串格 |
|---|---|---|
| `Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679…` | 27,330 |
| `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | `41daac00…` | 2,494 |
| `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f…` | 9,358 |
| `SR26 Default Settings and PNet ECU Configuration v1_0.xlsx` | `8f3ae50e…` | 3,690 |
| `SR24 R1 Market Configuration Table v1.6.xlsx` | `7e865d55…` | 7,276 |
| `PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3…` | 段 3 |
| `PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf…` | 段 3 |

後三檔（HMI / SR26 / SR24）原不在 `FORMS.md`，本包依 §H 第 2 步
**補登其六項欄位**（(a)–(f)，涵蓋範圍為執行層實測）。

## 1. 分析層 §0 所列命中之逐格複核

**五筆全部逐格查證屬實**（`openpyxl` 直取該格，非重新搜尋）：

| 規格原名 | 檔／分頁／格 | 實測值 | 符 |
|---|---|---|---|
| `Auto_SwitchOn_Setting.Req` | HMI `Settings` r96 c2 / c4 | `Auto-On Comfort` / `Auto_On_Comfort_Remote` | ✓ |
| 同上 | HMI `Settings` r97 c4 | `Auto_On_Comfort_No_Remote` | ✓ |
| 同上 | PROXI `Format` r354 c6 / r639 c6 | `Auto_On_Comfort_Enable` / `Auto_On_Comfort_Menu` | ✓ |
| `SwitchOff_Timeout_Setting.Req` / `SwitchOffSetting.Req` | PROXI `Format` r510 c6 | `Switch_Off_Time` | ✓ |
| `Rear_Camera_Enable.Info` | PROXI `Format` r401 c6 / r494 c6 | `Rear_View_Camera` / `Rear_View_Camera_Soft_Button` | ✓ |
| 同上 | SR26 `Default Parameters` r14 c12 / r15 c12 | `Rear Camera Present`（c13 = `LTM, ETM`）| ✓ |
| `RemStartFail` | PROXI `Format` r469 c6 / r1013 c6 | `Remote_start` / `Wired_Remote_Start_Presence` | ✓ |

## 2. 候選之強度分級（R-P368(b) 之「比對依據」）

R-P375(e) 令 R-P368(b) 不變 —— **語意跳接仍不許**。
惟 R-P375(b) 又以 `Auto_SwitchOn_Setting.Req` 為 (b) 類之示例。
二者在該名上**張力**：其命中值與規格原名之差異**不只是前後綴**。

本層之處置：**照 R-P375(d) 一律記為「候選」（非認定）**，
並增列**強度**欄，使分析層覆核時看得見差異之性質。**本層不自行取捨。**

| # | 規格原名 | 候選 | 比對依據（欄／列）| 差異之性質 | 強度 |
|---|---|---|---|---|---|
| 1 | `SwitchOff_Timeout_Setting.Req` | `PROXI Switch_Off_Time` | PROXI `Format` r510 c6 | `SwitchOff`↔`Switch_Off`（底線）、`Timeout`↔`Time`（後綴）、`Setting` 無對應 | **強**（純前後綴／底線差異，(b) 明許）|
| 2 | `SwitchOffSetting.Req` | 同上 | 同上 | 同上 | **強** |
| 3 | `Rear_Camera_Enable.Info` | `SR26 Rear Camera Present` | SR26 `Default Parameters` r14–15 c12 | `Rear_Camera` 逐字同；`Enable`↔`Present` | **中**（名之主體逐字同，屬性詞不同）|
| 4 | 同上 | `PROXI Rear_View_Camera` | PROXI `Format` r401 c6 | 中綴多 `View`；`Enable` 無對應 | **中** |
| 5 | `Auto_SwitchOn_Setting.Req` | `HMI Auto-On Comfort` | HMI `Settings` r96–97 c2 | `Auto` 同、`SwitchOn`↔`On`（後綴差）、**`Comfort` 於規格名無對應** | **弱**（新增語意成分）|
| 6 | 同上 | `PROXI Auto_On_Comfort_Enable` | PROXI `Format` r354 c6 | 同上，另多 `Enable` | **弱** |
| 7 | `RemStartFail` | `PROXI Remote_start` | PROXI `Format` r469 c6 | **存在性參數，非失敗狀態** | **非候選**（R-P375(e) 明文）|

⚠ **第 5、6 項之「弱」須特別提請覆核**：`Comfort` 為規格原名所無之語意成分，
此即 R-P368(b) 所禁之「憑語意跳接」之形態。且該識別**正是 DR-PW25 之既有未決問題**
（29 包 B1 以 `auto switch-on setting` 為條目名，**無前例，SYSAD 意譯**）。
本層照 R-P375(b) 記為候選，**但不認為其強度足以撤除 PENDING**，請裁。

## 3. 本層獨立重查之結果（全檔 regex，全詞素同格）

判準：規格原名去 `.Info` / `.Req` 後之詞素**全部**出現於同一格。

| 規格原名 | 命中 | 判讀 |
|---|---|---|
| `Phone_Call.Info` | 4 | **全非候選**。LID r210 c28 為 `Callnum`（`Func` = `The number which user selects on the assist app.`，AH = `GLOB_TLM.Call_Number`）—— **電話號碼選擇，非通話狀態**；HMI r600/612 c5 為音訊類別清單（`Media, Phone Call, Phone Ring, …`）。**與分析層 §0「無可用命中」之判斷一致** |
| `PhoneCall.Info` | 2 | 同上，全非候選 |
| 其餘九名 | **0** | 全詞素同格判準下無命中 |

**本層之獨立重查與分析層 §0 之命中互補而不衝突**：
分析層以**部分詞素**搜得（故有 `Auto-On Comfort` 等），本層以**全詞素**搜（故 0）。
二者之差即 §2 之「強度」—— **命中愈靠部分詞素，強度愈弱**。

## 4. 十三名之現況（三度重做後）

| # | 規格原名 | 段 1 | 段 2 / 3 | 狀態 |
|---|---|---|---|---|
| 1 | `TLM_Status.Info` | LID r2069 `Telematic_Power`（逐字）| `STATUS_TELEMATIC.PowerSts_Telematic`，BHCAN2 ✓ | **解得** |
| 2 | `LTM_OperationalModeSts.Info` | LID r1286（前綴差異）| `STATUS_BH_BCM1.OperationalModeSts`，BHCAN2 ✓ | **解得（附註）** |
| 3 | `SwitchOff_Timeout_Setting.Req` | PROXI r510 c6 | PROXI 路徑，不走 DBC | **候選（強）** |
| 4 | `SwitchOffSetting.Req` | PROXI r510 c6 | 同上 | **候選（強）** |
| 5 | `Rear_Camera_Enable.Info` | SR26 r14–15 c12、PROXI r401/r494 c6 | 存在性參數 → Pre-Condition | **候選（中）**；**運行時狀態仍 PENDING**（R-P375(c) 明文）|
| 6 | `Auto_SwitchOn_Setting.Req` | HMI r96–97 c2/c4、PROXI r354/r639 c6 | UI + PROXI 雙路徑 | **候選（弱）**，見 §2 之提請 |
| 7 | `Phone_Call.Info` | 無可用命中 | — | **PENDING** |
| 8 | `PhoneCall.Info` | 無可用命中 | — | **PENDING** |
| 9 | `Antitheft_Activation.Req` | 無命中 | — | **PENDING** |
| 10 | `Antitheft_Result.Info` | 無命中 | — | **PENDING** |
| 11 | `RemStartFail` | 存在性參數，R-P375(e) 明文非候選 | — | **PENDING** |
| 12 | `Front_Panel_OnOff.Req` | 無命中（LID r1039 之語意跳接前已拒收）| — | **PENDING**（DR-PW24）|
| 13 | `Audio_Data_Exchange.Info` | 無命中 | — | **PENDING** |

**解得 2、候選 4、PENDING 7。**

## 5. PENDING 重算

機讀：`data/pending_recount_62.tsv`。

| 情形 | 條數 | 佔 283 |
|---|---|---|
| 含任一內部訊號 | 131 | 46.3% |
| 58 包重算（僅解得 2 名扣除）| **102** | 36.0% |
| 62 包：**僅強候選**（#3 / #4）撤 PENDING | **98** | 34.6% |
| 62 包：**四候選全撤** PENDING | **79** | 27.9% |

**與 58 包之 −3 相比，本輪之實益顯著**：最保守情形 −4，最寬情形 **−23**。
差額全部落在 `Auto_SwitchOn_Setting.Req`（26 條）與 `Rear_Camera_Enable.Info`（9 條），
**即 §2 中強度為「弱」與「中」之二名** —— 故實益之大小**取決於覆核如何裁強度**，
本層不預設。

### 最保守情形下仍 PENDING 之訊號別

| 訊號 | TC 條數 |
|---|---|
| `Phone_Call.Info` | 32 |
| `Antitheft_Activation.Req` | 26 |
| `Antitheft_Result.Info` | 25 |
| `RemStartFail` | 15 |
| `Front_Panel_OnOff.Req` | 11 |
| `PhoneCall.Info` | 6 |
| `Audio_Data_Exchange.Info` | 1 |

⚠ 即使四候選全撤，**79 條（27.9%）仍帶 PENDING**，
S6 之甲（不出貨）依 R-P374(a) 續為預設。**forms/ 全檔重查未能解消 S6 衝突。**
