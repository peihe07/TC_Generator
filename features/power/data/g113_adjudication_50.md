# B1 —— G113 未覆蓋分支之逐支裁決（R-P325）

> **78 支全數裁決，無一沉默**（R-P118(d)：沉默不算裁決）。
> 產生指令：`python features/power/scripts/adjudicate_g113_50.py`；裁決表 `scripts/g113_verdicts_50.py`。

## ⚠ 二項須先訂正

**（一）78 為全語料合計，非第七批。** 49 §九第 3 項寫成「本批 78 個未覆蓋分支」為誤，R-P325 承襲之。實測逐批：batch_001 **4**、002 **31**、003 **16**、004 **8**、005 **15**、006 **1**、**007 僅 3**。

**（二）桶名之出入。** R-P118(d) 之三桶為 `真缺口` / `規格未給門檻，不可獨立驗證` / **`已由他條涵蓋`**；R-P325 改寫為 **`已由他 leaf 涵蓋`**。二者不同 —— 本批絕大多數為「**同一 leaf 之他 TC** 涵蓋」，依 R-P325 之字面無桶可入。**本檔以 R-P118(d) 之桶為準**，並將「他 leaf」另計為子桶，**不自行改寫任一條之文字**。

## 桶計數

| 桶 | 計數 | 佔 78 |
|---|---|---|
| 已由他條涵蓋（同 leaf 之他 TC） | **65** | 83.3% |
| 已由他 leaf 涵蓋 | **3** | 3.8% |
| 規格未定義該支（門檻／細節不在素材內） | **10** | 12.8% |
| 真缺口 | **0** | 0.0% |

**`真缺口` = 0** —— R-P325 之「真缺口須補測後方得寫回」**未觸發**。

> **此 0 不是目標，是結果。** 其可信度不繫於本數字，而繫於下表 —— **78 支每一支皆附完整理由**（非 R-P325 所要求之 ≥16.7% 抽樣，而是 100%），其中 **42 支**之理由指名一條具體 TC 之標題、ER 逐字內容或 pre_condition（實測），可逐一覆核。

## 逐支裁決（78 / 78）

| leaf | 組.支 | 桶 | 理由 |
|---|---|---|---|
| `SWE-PM-071` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | 並列為「Standby OR Bench」之限定語；二支各有 TC（「No splash screen when TLM passes to Standby」「…to Bench」） |
| `SWE-PM-073` | 1.2 | 已由他條涵蓋（同 leaf 之他 TC） | BODY OFF-TIMED 之 Battery Critical 已有專條 TC；殘差詞為原文措辭（`mimimize` 為規格原文之誤拼） |
| `SWE-PM-073` | 2.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「voltage out of range 即離開」已有 TC「Battery Critical exits on voltage out of range condition」 |
| `SWE-PM-073` | 2.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「10 秒後回復正常」已有 TC「Normal operation resumes 10 seconds after recovery」 |
| `SWE-PM-057` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「user 可選 00 min」—— 三條 TC 之 ER 第 3 項逐字含 `Timeout1 reads "00 min" after the first selection` |
| `SWE-PM-057` | 2.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「Timeout1 等於 00 min」—— 同上，ER 第 3 項涵蓋 |
| `SWE-PM-057` | 2.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「20/60/180 minutes respectively」—— 三條 TC 各對應一個 PROXI 值，ER 第 3 項逐字涵蓋 |
| `SWE-PM-057` | 3.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「user 可選 00 min」—— 三條 TC 之 ER 第 3 項逐字含 `Timeout1 reads "00 min" after the first selection` |
| `SWE-PM-057` | 4.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「Timeout1 等於 00 min」—— 同上，ER 第 3 項涵蓋 |
| `SWE-PM-057` | 4.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「20/60/180 minutes respectively」—— 三條 TC 各對應一個 PROXI 值，ER 第 3 項逐字涵蓋 |
| `SWE-PM-057` | 5.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「user 可選 00 min」—— 三條 TC 之 ER 第 3 項逐字含 `Timeout1 reads "00 min" after the first selection` |
| `SWE-PM-057` | 6.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「Timeout1 等於 00 min」—— 同上，ER 第 3 項涵蓋 |
| `SWE-PM-057` | 6.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「20/60/180 minutes respectively」—— 三條 TC 各對應一個 PROXI 值，ER 第 3 項逐字涵蓋 |
| `SWE-PM-057` | 7.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「LTM High Radio not present」—— **實測**三條 TC 之 pre_condition 第 1 項皆為 `An LTM High Radio is absent from the bench configuration` |
| `SWE-PM-057` | 7.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「值由 PROXI `Switch_Off_Time` 指定」—— 三條 TC 之 pre_condition 第 2 項逐一設定該參數 |
| `SWE-PM-057` | 8.1 | 已由他條涵蓋（同 leaf 之他 TC） | 同組7支1 |
| `SWE-PM-057` | 8.2 | 已由他條涵蓋（同 leaf 之他 TC） | 同組7支2；`IF PROXI == 20 minutes` 即第一條 TC 之前置 |
| `SWE-PM-057` | 9.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「user 可選 00 min」—— 三條 TC 之 ER 第 3 項逐字含 `Timeout1 reads "00 min" after the first selection` |
| `SWE-PM-057` | 10.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「Timeout1 等於 00 min」—— 同上，ER 第 3 項涵蓋 |
| `SWE-PM-057` | 10.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「20/60/180 minutes respectively」—— 三條 TC 各對應一個 PROXI 值，ER 第 3 項逐字涵蓋 |
| `SWE-PM-057` | 11.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「user 可選 00 min」—— 三條 TC 之 ER 第 3 項逐字含 `Timeout1 reads "00 min" after the first selection` |
| `SWE-PM-057` | 12.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「Timeout1 等於 00 min」—— 同上，ER 第 3 項涵蓋 |
| `SWE-PM-057` | 12.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「20/60/180 minutes respectively」—— 三條 TC 各對應一個 PROXI 值，ER 第 3 項逐字涵蓋 |
| `SWE-PM-057` | 13.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「user 可選 00 min」—— 三條 TC 之 ER 第 3 項逐字含 `Timeout1 reads "00 min" after the first selection` |
| `SWE-PM-057` | 14.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「Timeout1 等於 00 min」—— 同上，ER 第 3 項涵蓋 |
| `SWE-PM-057` | 14.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「20/60/180 minutes respectively」—— 三條 TC 各對應一個 PROXI 值，ER 第 3 項逐字涵蓋 |
| `SWE-PM-063` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「one call」由該 leaf 唯一 TC 之去話與來話二情境涵蓋 |
| `SWE-PM-063` | 1.2 | 已由他 leaf 涵蓋 | 「more calls according to following logics that depend on Timeout1」之 logics 即 `SWE-PM-038` 之 Case 1–4，該 leaf 有 11 條 TC 逐案涵蓋 |
| `SWE-PM-065` | 1.1 | 規格未定義該支（門檻／細節不在素材內） | 並列項為說明性舉例（`for example … like … rather than USB OR BT streaming audio`），規格未就 USB 支與 BT 支定義相異行為，無可獨立驗證之判準 |
| `SWE-PM-065` | 1.2 | 規格未定義該支（門檻／細節不在素材內） | 同上，為同一舉例並列之另一支 |
| `SWE-PM-038` | 1.1 | 規格未定義該支（門檻／細節不在素材內） | 與 `SWE-PM-065` 組1 為同一句；並列項為說明性舉例，非行為分支 |
| `SWE-PM-038` | 1.2 | 規格未定義該支（門檻／細節不在素材內） | 同上 |
| `SWE-PM-038` | 2.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「at maximum until MaxCallTimeout expiration」已有 TC「Case 2 exit with RemStartFail cleared on MaxCallTimeout expiry」 |
| `SWE-PM-038` | 5.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「Ignition Off → 進 Timed 並起 MaxCallTimeout」已有 TC「Case 4: ignition off with Timeout1 at 00 min enters Timed state」 |
| `SWE-PM-038` | 6.2 | 已由他條涵蓋（同 leaf 之他 TC） | 與組2支2 同義之重述（`expires.` vs `expiration.`），同一 TC 涵蓋 |
| `SWE-PM-011` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「不要求 audio OR video」三種組合皆有 TC（audio only / video only / neither） |
| `SWE-PM-014` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「Ignition Pre Off OR Ignition Off」二支各有 TC（RemStartFail 於二事件皆置 True） |
| `SWE-PM-014` | 2.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「留在 Timed 直到 Phone_Call.Info 變 Not_Active」已有 TC「Behaviour 1 with an active call passes the TLM to Timed」 |
| `SWE-PM-014` | 2.2 | 已由他 leaf 涵蓋 | MaxCallTimeout 上限之驗證在 `SWE-PM-038`（Case 2 / Case 4 之 MaxCallTimeout 系列） |
| `SWE-PM-014` | 3.1 | 已由他條涵蓋（同 leaf 之他 TC） | ELSE 支（非 Ignition Pre Off / Off）即 Behaviour 2，已有二條 TC |
| `SWE-PM-014` | 4.2 | 已由他條涵蓋（同 leaf 之他 TC） | `RemStActvSts == Remote Start Not Active` 為 Behaviour 系列 TC 之前置，已涵蓋 |
| `SWE-PM-014` | 6.1 | 已由他條涵蓋（同 leaf 之他 TC） | 與組2支1 為 Behaviour 2 之重述，同一 TC 涵蓋 |
| `SWE-PM-014` | 6.2 | 已由他 leaf 涵蓋 | 同組2支2 —— MaxCallTimeout 上限在 `SWE-PM-038` |
| `SWE-PM-018` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「Ignition Pre Off OR Ignition Off」二支各有 TC |
| `SWE-PM-018` | 1.2 | 已由他條涵蓋（同 leaf 之他 TC） | `THEN TLM has to set TLM_Status.Info` 之後果即二條 TC 之 ER（讀 Standby） |
| `SWE-PM-025` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | 按鍵後之 popup 與轉態已有四條 TC（顯示 / 接受 / 拒絕 / 無通話） |
| `SWE-PM-025` | 1.2 | 規格未定義該支（門檻／細節不在素材內） | `refer to TLM HMI Specification` —— 該支之判準在 HMI 規格，**不在本專案素材內** |
| `SWE-PM-025` | 2.1 | 已由他條涵蓋（同 leaf 之他 TC） | `CLIMATIC_PANEL.Radio_Btn0` 之四條 TC 與組1 對稱齊備 |
| `SWE-PM-025` | 2.2 | 規格未定義該支（門檻／細節不在素材內） | 同組1支2 —— 判準在 HMI 規格，不在素材內 |
| `SWE-PM-026` | 2.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「前一內部狀態為 Standby 則留在 Timed」已有 TC「Door open with Standby as the previous state keeps the TLM in Timed」；本支之獨有詞經機械層判定全為書寫變體，區辨實質為零 |
| `SWE-PM-031` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | `Rear_View_Camera PROXI == Present` 為該 TC 之 pre_condition 第 2 項（實測），其後之顯示行為即 TC 之 ER |
| `SWE-PM-033` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「Ignition Pre Off OR Ignition Off」二支各有 TC |
| `SWE-PM-033` | 1.2 | 已由他條涵蓋（同 leaf 之他 TC） | 同上，`valueTHEN` 為黏連之後果引導詞 |
| `SWE-PM-039` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「behave as an Ignition Pre Off」已有 TC「An SNA operational mode is handled as an ignition off event」，其 ER 逐字含二事件 |
| `SWE-PM-039` | 1.2 | 已由他條涵蓋（同 leaf 之他 TC） | 同一 TC 涵蓋；`according to par` 為條號指標，非行為 |
| `SWE-PM-045` | 1.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「Sleep 支 ＋ HMI Antitheft 畫面 ＋ 上限 Timeout1」已有 TC「A failed antitheft keeps the TLM in the original Sleep state」，其 ER 逐字含 at most Timeout1 與 HMI 畫面 |
| `SWE-PM-046` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | `Antitheft_Result.Info == In_Progress` 支已有 TC「…while the antitheft is still in progress」 |
| `SWE-PM-046` | 1.2 | 已由他條涵蓋（同 leaf 之他 TC） | `Not_Successfully` 支已有 TC「…after an unsuccessful antitheft」 |
| `SWE-PM-047` | 1.2 | 規格未定義該支（門檻／細節不在素材內） | `(see VF210)` —— 該支之判準在 VF210，**不在本專案素材內** |
| `SWE-PM-074` | 1.2 | 已由他條涵蓋（同 leaf 之他 TC） | ROV 支已有 TC「A ROV FOTA update at Body OFF brings the HU to Timed for the pop-up」；殘差詞 `cfts057` / `see` 為外部文件指標，非行為 |
| `SWE-PM-093` | 2.5 | 已由他條涵蓋（同 leaf 之他 TC） | 「door ajar OPEN 時略過動畫」已有 TC「An open driver door makes the HU skip the animation on a mode change」 |
| `SWE-PM-093` | 3.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「因 ignition event 改變模式」已有 TC「A mode change cancels a start-up animation in progress」 |
| `SWE-PM-093` | 4.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「播過一次後至下個 CAN wakeup 前不再播」已有 TC「A second start-up animation waits for the wakeup cycle or thirty minutes」 |
| `SWE-PM-093` | 4.2 | 已由他條涵蓋（同 leaf 之他 TC） | 同一 TC 之 ER 逐字含 `or after 30 minutes, whichever is greater` |
| `SWE-PM-093` | 6.5 | 已由他條涵蓋（同 leaf 之他 TC） | 與組2支5 為同一句於原文之重複出現（A-PW 已載 `093` 之錨點重複），同一 TC 涵蓋 |
| `SWE-PM-093` | 7.1 | 已由他條涵蓋（同 leaf 之他 TC） | 與組3支1 同句重複，同一 TC 涵蓋 |
| `SWE-PM-093` | 8.1 | 已由他條涵蓋（同 leaf 之他 TC） | 與組4支1 同句重複，同一 TC 涵蓋 |
| `SWE-PM-093` | 8.2 | 已由他條涵蓋（同 leaf 之他 TC） | 與組4支2 同句重複，同一 TC 涵蓋 |
| `SWE-PM-099` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | 「使用者手動調時 ＋ 跨午夜」二者各有 TC（customer selected date 之變更 / passing midnight） |
| `SWE-PM-104` | 1.2 | 已由他條涵蓋（同 leaf 之他 TC） | Full Operation 支已有 TC「…on the first transition to Full Operation」 |
| `SWE-PM-104` | 2.3 | 已由他條涵蓋（同 leaf 之他 TC） | 同上；殘差詞為切詞產物（`mod` ⊂ `mode`） |
| `SWE-PM-105` | 1.1 | 已由他條涵蓋（同 leaf 之他 TC） | FOTA pop-up 支已有 TC「A FOTA pop up temporarily skips…」，其後之補顯示已有 TC「The skipped screens are displayed at the next transition」 |
| `SWE-PM-105` | 1.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「during that bus cycle」之補顯示即上開 TC 之 ER |
| `SWE-PM-113` | 1.1 | 規格未定義該支（門檻／細節不在素材內） | `See HMI for different startup conditions to determine when to add…` —— **判準明載於 HMI 文件，不在素材內**；本 leaf 僅驗市場條件成立時之加註行為 |
| `SWE-PM-078` | 1.2 | 已由他條涵蓋（同 leaf 之他 TC） | 「不支援之值 → 回落 brand default」已有 TC「An unsupported special package falls back to the brand default theme」 |
| `SWE-PM-009` | 1.1 | 規格未定義該支（門檻／細節不在素材內） | 電壓上限門檻 —— 原文明載 `refer to SIS`，**SIS 不在本專案素材內**（49 包 R-P320(c) 已停並上繳） |
| `SWE-PM-009` | 1.2 | 規格未定義該支（門檻／細節不在素材內） | 電壓下限門檻與 `for a certain time` —— 同上，門檻在 SIS |
| `SWE-PM-009` | 1.3 | 已由他條涵蓋（同 leaf 之他 TC） | 「每次斷電事件」已有 TC「A battery disconnection puts the TLM into the INIT state」 |
