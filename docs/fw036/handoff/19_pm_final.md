# 下放包 19：PowerModeSts_Telematic 更正回復 ＋ 軌 C 補 4 列 ＋ 三項裁決

## 一、分析層錯誤：`PowerModeSts_Telematic` 之判斷

17 包 §五載「`PowerModeSts_Telematic` 係二者名稱之混合，非 DBC 實有」，
Pei 據此裁定「一律採 `PowerSts_Telematic`」。

**查證 CFTS009-4941562（row 72 之 SWE-PM-022 錨點）原文逐字**：

```
IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation" || "Idle"
AND signal PowerModeSts_Telematic passes from "Standard_Power" to
"Logistic_Mode_On", then TLM has to set TLM_Status.Info to
"Logistic Idle" and $Telematic_Power$ to "Logistic_On" and then it
passes to Logistic Idle state
```

**`PowerModeSts_Telematic` 為規格原文之訊號名，非 036 之筆誤。**
分析層僅查 DBC 未查 CFTS 原文即斷為「名稱混合」，
**此為第七次以片面查證下結論**（前六次見 04／06／A-PM09／
transition_values／16g 統計等）。

執行層所報之兩個後果，**皆為該錯誤裁定之必然結果，非執行瑕疵**：
1. `Standard_Power`／`Logistic_Mode_On` 不在 `PowerSts_Telematic`
   之 VAL_ 內 —— 因二者本為不同訊號
2. 觸發與觀察塌縮為同一訊號，因果驗證降為狀態檢查

### 更正裁決（撤銷 17 包 §五）

~~一律採 `PowerSts_Telematic`；`PowerModeSts` 不使用~~

> **撤銷（2026-08-21）**。原裁定基於分析層之錯誤前提。

```
R-13 規格訊號名與 DBC 不符之處置
規格原文所載之訊號名，即使 DBC 查無同名，一律**保留原文名稱**，
不得代以語意相近之他訊號。DBC 對應缺漏登記 DR 向上游查詢。
理由：以他訊號代入將改變 TC 之驗證對象與因果結構
（row 72 即實例：觸發訊號被觀察訊號取代，因果驗證塌縮）。
```

**row 72 之處置**：回復規格原文寫法。
```
PRE:
1. The TLM is in Full-Operation state
2. LIN and CAN tool is available on HU

PROC:
1. Send the signal PowerModeSts_Telematic = Standard_Power
2. Send the signal PowerModeSts_Telematic = Logistic_Mode_On
3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 5 (Logistic_On)

ER:
1. The signal PowerModeSts_Telematic = Standard_Power is sent
2. The signal PowerModeSts_Telematic = Logistic_Mode_On is registered without a bus error
3. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 5 (Logistic_On) is received
```
`PowerModeSts_Telematic` **不加 `$`**（DBC 無對應，比照 R-1 v3(d)
內部訊號處置）；觀察側之 `$Telematic_Power$` = `Logistic_On`
對應 `PowerSts_Telematic` VAL_ **5**，該對應由 036 原 ER 明載。

**開 DR-PW21**（High）：`PowerModeSts_Telematic` 於 CFTS009-4941562
為規格明載訊號，兩份 DBC（BH-CAN／FD-CAN8）皆查無同名；
請上游確認其 message 歸屬與 VAL_ 定義。

## 二、軌 C 補 rows 271–274（附件 G／H 之遺漏）

分析層附件僅涵蓋 26 列，文末統計誤書 30；執行層停止並回報正確。

來源：`CFTS009-4941950`（splash＋disclaimer，first time each bus
cycle，transitions to **Timed or Full Operation**）／
`CFTS009-4941952`（disclaimer，first time each bus cycle，
transitions **from Idle, Standby, or Partial Operation** to
Timed or Full Operation）
→ row 270／271 為 4941950 之 Timed／Full-Operation 兩分支；
rows 272／273／274 為 4941952 之三個來源狀態分支。

**row 271**（Full-Operation 分支，餘同附件 G row 270）
```
PRE:
1. The TLM is in Idle state
2. No transition to Timed or Full-Operation has occurred in the current bus cycle
3. LIN and CAN tool is available on HU

PROC:
1. Bring the HU to Full-Operation mode
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
3. Read the TLM screen and check that the splash screen is shown
4. Read the TLM screen and check that the disclaimer screen is shown after the splash screen

ER:
1. The HU reaches Full-Operation mode
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
3. The splash screen is shown on the TLM screen
4. The disclaimer screen is shown on the TLM screen after the splash screen
```

**row 272**（Idle → Timed）
```
PRE:
1. The TLM is in Idle state
2. No transition to Timed or Full-Operation has occurred in the current bus cycle
3. LIN and CAN tool is available on HU

PROC:
1. Bring the HU to Timed mode
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)
3. Read the TLM screen and check that the disclaimer screen is shown

ER:
1. The HU reaches Timed mode
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received
3. The disclaimer screen is shown on the TLM screen
```

**row 273**（Standby → Timed）：同 row 272，
**PRE 1 改** `1. The TLM is in Standby state`。

**row 274**（Partial Operation → Full-Operation）：同 row 272，
**PRE 1 改** `1. The TLM is in Partial_Operation state`；
**PROC 1 改** `1. Bring the HU to Full-Operation mode`；
**PROC 2／ER 2 之值改** `4 (Full_Operation)`；
**ER 1 改** `1. The HU reaches Full-Operation mode`。

⚠ 四列之首步同為抽象動作（觸發訊號原文未載），
與 rows 270／275–282 同一處置，不填推定觸發。

## 三、三項待處理之裁決

**1. row 291 二擇一（geolocation pop-up 或 disclaimer）**
執行層之判斷成立：判準不唯一，未達 R-11(b)。
**裁定**：PROC 2／ER 2 之「或」改標
`PENDING: DR-PW22 geolocation pop-up 與 disclaimer 之擇一判準`，
其餘步驟不動。開 **DR-PW22**（Medium）。

**2. 8 列（270／271／275–282）首步抽象動作**
**裁定**：維持保留，登記為 **A-PM15**（已知限制）：
該 8 列之 PROC 1 不可執行至訊號層，因 CFTS009-4941950／4941952
未載觸發來源。**不標 PENDING** —— 該步驟仍可由測試者以任一
合法途徑達成目標狀態，非缺件；標 PENDING 將阻斷交付而無實益。
若日後上游補明觸發，再行細化。

**3. A-PM13／A-PM14 條文**（分析層補擬，登入 ANOMALIES.md）
```
A-PM13  rows 13／265／266／267／268 五列之 PROC 與 ER 逐字相同，
        均驗證 Idle 狀態下 TLM audio OFF 且僅顯示 Splash Screen
        （CFTS009-4941365）。屬 §10.6 strict equivalence 重複。
        TC 側不合併、不刪列（§8.2.1）；拆併屬 Pei。

A-PM14  row 181（SWE-PM-070）與 row 293（SWE-PM-115）之
        PRE／Input／PROC／ER 逐字全同，僅 Requirement ID 相異，
        與 A-PM04 同型（兩 SWE leaf 指向同一行為）。
        已併入 DR-PW12 第七對。另 SWE-PM-115 即 A-PM12 所載
        037 Source Requirement ID 欄空白之該條，兩異常同指一 leaf。
```

## 四、執行與驗收

基底：`sandbox/b18/pm_18.xlsx`（c61a6d55…）。
改動：row 72（§一）＋ rows 271–274（§二）＋ row 291（§三-1），
合計 6 列。

- `pre_last_not_tool` 與 `read_without_value` 之殘餘 4 筆
  （即 271–274）應歸零
- 十二項驗收全零；lint A–N 全零、E=0
- `test_item`／`spec_reference` 零變動；x14 讀回；壓縮成員 42 未變

上繳 `docs/fw036/upstream/19_pm_final.md`，附
「本包是否仍有該驗而未驗者」獨立判斷。
