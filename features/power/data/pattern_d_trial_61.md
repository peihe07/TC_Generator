# 丁案試作（61 包 / R-P374(c)）—— `RemStartFail` 一條

> **本檔不入 corpus、不入 batch、不計 G 閘**（R-P374(d)）。僅供 Pei 站④ 目視。
> 依 R-P374(f)，未裁前不得對第二條 TC 施作。

## 0. 選件依據（R-P374(c)）

選 **`NR1L-PowerManagement-057`**（`SWE-PM-014`，
`Remote Start ends at ignition off: RemStartFail is set true`）。

條件：`test_item` 上半含 `RemStartFail`，**且 CFTS009 對其上游事件與下游效果皆有明文**。

本條之錨點 **`CFTS009-4941504`**（1,354 字元）**單一段落內同時載有因與果**：

> IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"
> AND STATUS_BH_BCM2.RemStActvSts has a transition from "Remote Start Active"
> to "Remote Start Not Active" **THEN IF LTM_OperationalModeSts.Info is equal to
> "Ignition Pre Off" OR to "Ignition Off", TLM has to set RemStartFail = "True"**
> THEN **IF Phone_Call.Info == "Not Active", TLM has to set RemStartFail ="False"
> AND TLM_Status.Info and $Telematic_Power$ to "Standby" value and it passes to
> TLM Standby state.** IF Phone_Call.Info == "Active" TLM has to set
> TLM_Status.Info and $Telematic_Power$ to "Timed" value …

**因**（上游 CAN 事件）與**果**（下游可觀察狀態）皆在 `4941504` 內，逐字可引。
14 條含 `RemStartFail` 之 TC 中，**僅本條與 `-065` 具此性質**（同錨點）；
其餘 12 條之因或果須跨段落，依 R-P374(c)「查無明文者不選、不造」不選。

## 1. 並列版

### 左：現行版

現行 corpus 之 `-057`（未經 B5）：

| 欄 | 內容 |
|---|---|
| Pre-Conditions | 1. A LIN and CAN simulation tool is connected<br>2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"<br>3. LTM_OperationalModeSts.Info is at "Ignition Off" |
| Input Test Data | STATUS_BH_BCM2.RemStActvSts: "Remote Start Active" to "Remote Start Not Active" |
| Test procedure | 1. Send the transition listed in Input Test Data<br>2. **Read RemStartFail to check that it follows the transition** |
| Expected Result | 1. The TLM accepts the transition without a bus error<br>2. **RemStartFail reads "True"** |

**B5 於甲案下會產出者**（R-P355(c)）：第 2 步與其 ER 改為
`PENDING: DR-PW23 RemStartFail`，該條**不可執行、不得出貨**。

### 右：丁版

`test_item` **上半 verbatim 一字未改**（R-6 / R-P343 / R-P347）。
括號下半（`(read RemStartFail -> RemStartFail reads "True")`）依丁案改寫。

| 欄 | 內容 |
|---|---|
| Pre-Conditions | 1. A LIN and CAN simulation tool is connected<br>2. `$STATUS_TELEMATIC.PowerSts_Telematic$` = 4 (Full_Operation)<br>3. `$STATUS_BH_BCM2.RemStActvSts$` = 1 (Remote Start Active)<br>4. No phone call is in progress on the bench |
| Input Test Data | NA |
| Test procedure | 1. Send the signal `$STATUS_BH_BCM1.OperationalModeSts$` = 2 (Ignition_Off)　*(CFTS009-4941504, DR-PW26)*<br>2. Send the signal `$STATUS_BH_BCM2.RemStActvSts$` = 0 (Remote Start Not Active)　*(CFTS009-4941504)*<br>3. Read the signal `$STATUS_TELEMATIC.PowerSts_Telematic$` and check that it is 1 (Standby)　*(CFTS009-4941504)* |
| Expected Result | 1. The signal value `$STATUS_BH_BCM1.OperationalModeSts$` = 2 (Ignition_Off) is received<br>2. The signal value `$STATUS_BH_BCM2.RemStActvSts$` = 0 (Remote Start Not Active) is received<br>3. The signal value `$STATUS_TELEMATIC.PowerSts_Telematic$` = 1 (Standby) is received |
| 括號下半 | `(read $STATUS_TELEMATIC.PowerSts_Telematic$ -> The TLM passes to Standby)` |
| Remarks | 丁案改寫：`RemStartFail` 為 HU 內部變數，改以 `CFTS009-4941504` 所載之上游 CAN 事件驅動、下游狀態觀察。原內部變數保留於 Test Item 上半 verbatim。 |

**`RemStartFail` 已自 Procedure / ER 完全移除；ITD 依 R-P366(a) 內聯後改 `NA`。**

## 2. reasoning（§10.4 四項，繁中）

**(1) 選了什麼、為何**　選 `4941504` 之「Remote Start 結束於 Ignition Off」分支。
該段為決策表形態，本 TC 取其 `RemStartFail = "True"` 之路徑。
上游事件二個（點火狀態、遠端啟動狀態）皆為 BH-CAN 訊號，
下游效果（TLM 轉入 Standby）為 `PowerSts_Telematic` 之列舉值，
**三者皆落 R-P353 白名單 (i)**。

**(2) 排除了什麼、為何**　排除 `Phone_Call.Info` 之直接設定。
`4941504` 以其為分支條件（`Not Active` → Standby、`Active` → Timed）。
本 TC 取 `Not Active` 分支，改以 **Pre-Condition 之台架事實**
（`No phone call is in progress on the bench`）建立 ——
**不通話是台架的預設狀態，可由不撥號達成，無須讀寫該內部變數**。
若某 TC 須測 `Active` 分支，則須實際撥號（`Place a call from the paired phone`），
仍為物理動作而非內部變數。

**(3) 值之來源**　`2 (Ignition_Off)` 取 `VAL_ 854 OperationalModeSts`；
`0 / 1 (Remote Start Not Active / Active)` 取 `VAL_ 1132 RemStActvSts`；
`1 (Standby)` / `4 (Full_Operation)` 取 `VAL_ 1470 PowerSts_Telematic`。
三者皆 `forms/PDT27_E2A_R1_BHCAN2.dbc`（`46cb73f3…`，G0 參考庫）。
**無一值為推定**。

**(4) 未決者**　`LTM_OperationalModeSts.Info` → `$STATUS_BH_BCM1.OperationalModeSts$`
之等同性屬上游職權（DR-PW26 第 (1) 問），故第 1 步標 `(DR-PW26)`。
上游否認則本條回滾（同 R-P371(c)）。

## 3. 執行層自陳（R-P374(e)）

### (i) 上游事件是否 CFTS 逐字？　**是**

`4941504` 逐字載：
`STATUS_BH_BCM2.RemStActvSts has a transition from "Remote Start Active" to "Remote Start Not Active"`
與 `LTM_OperationalModeSts.Info is equal to "Ignition Pre Off" OR to "Ignition Off"`。
二者為第 2 步與第 1 步之來源。**訊號名逐字取自該段落，值逐字取自 DBC `VAL_`。**

⚠ 一處非逐字：`LTM_OperationalModeSts.Info` 於 TC 寫作
`$STATUS_BH_BCM1.OperationalModeSts$` —— 此為 R-P368 三段鏈之段 2 產物
（LID r1286，前綴差異），**非本試作所新造**，其未決狀態已標 `(DR-PW26)`。

### (ii) 下游效果是否白名單？　**是**

`$STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby)`，落 R-P353 白名單 **(i)
`$MESSAGE.Signal$`**。其 raw 值與 label 取自 `VAL_ 1470`，非自造。

### (iii) 與原版相比，驗證對象是否改變？　**是，改變了。**

**這是丁案最須 Pei 目視之處，本層不淡化。**

| | 原版 | 丁版 |
|---|---|---|
| 所驗證者 | `RemStartFail` **這個內部變數本身**是否被設為 `True` | TLM **是否轉入 Standby 狀態** |
| 對應 `4941504` 之片段 | `TLM has to set RemStartFail = "True"` | `TLM has to set … TLM_Status.Info … to "Standby" value and it passes to TLM Standby state` |

二者是**同一因果鏈上相鄰的兩個環節**，但**不是同一個斷言**：

- **丁版驗不到 `RemStartFail` 之中間值。** 若 HU 未設 `RemStartFail = "True"`
  卻因其他路徑仍轉入 Standby，**丁版會通過而原版會失敗**。
- 反之若 `RemStartFail` 正確設值而 Standby 轉移因他故失敗，
  **原版會通過而丁版會失敗** —— 丁版在此方向**更嚴**。
- 原版之 `test_item` 括號下半原文為 `(read RemStartFail -> RemStartFail reads "True")`，
  丁版改為 `(read $STATUS_TELEMATIC.PowerSts_Telematic$ -> The TLM passes to Standby)`
  —— **括號下半即驗證標的之宣告，其改寫等於改宣告**。

**R-13 之慮成立**：丁案不是把同一個驗證改寫得可執行，
而是**換一個可執行的驗證去代替不可執行的那個**。
其代價為**失去對內部狀態機中間值之覆蓋**；
其收益為**該條由不可出貨變為可出貨**。

### (iv) 附帶記明：本條之涵蓋在丁案下與 `-065` 重疊

`-065`（`Remote Start ends at ignition pre off`）之錨點同為 `4941504`，
其差別僅在點火值 `Ignition Pre Off`（raw 10）對 `Ignition Off`（raw 2）。
原版二條各驗 `RemStartFail`，**丁版二條之下游效果同為「轉入 Standby」** ——
二條之區辨僅剩 ITD 之點火值。**仍為二條相異 TC**（R-P360 五欄鍵下不同），
惟其**驗證強度之差異縮小**。若丁案推廣，此類收斂須逐對重檢。

## 4. 本層之意見（供裁參考，非建議採用）

丁案在**本條**上可行且證據完備，但 §3(iii) 之結論不可迴避：
**驗證對象確實改變。** 14 條 `RemStartFail` TC 中僅 2 條具備
「因與果同段落」之條件；**其餘 12 條若推廣，須跨段落拼接因果，
而跨段落拼接即為 R-P368(b) 所禁之語意跳接之同型風險**。

故本層之觀察為：**丁案不是一個可全推的機制，是一個逐條可用的例外。**
是否推廣、推廣到何處，請 Pei 裁。
