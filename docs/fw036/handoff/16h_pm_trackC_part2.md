# 附件 H：軌 C 逐列改寫（2/2）rows 181、275–282、289–291、293

原則同附件 G：值取自 CFTS 原文，註明 object id；
原文未載者標 `PENDING`，不推定（路線 c）。

**本批共通**：rows 275–281 之 Input 欄各載一種「事件」，
係 splash／disclaimer 暫緩之觸發情境，屬 **sibling 軸**
（§8.3 環境／情境軸），內聯後各為一列之情境條件 → **移入 PRE**。
七列之事件依序為：ongoing call（275）／backup camera view（276）／
incoming call（277）／outgoing call（278）／climate pop-up（279）／
SOS or Assist call（280）／FOTA pop up（281）。

**進入 Timed／Full-Operation 之觸發訊號原文未載**
（`CFTS009-4941950`／`4941952` 僅述 "transitions to"，未指定觸發來源），
故 PROC 之首步保留抽象動作，**不填推定觸發**；
與附件 G row 270 同一處置。

---
## row 181 — SWE-PM-070
```
PRE:
1. The HU is in Idle state
2. The disclaimer has not been shown in the current bus cycle
3. An incoming phone call can be placed from the bench
4. LIN and CAN tool is available on HU

PROC:
1. Let the bench place an incoming phone call
2. Read the TLM screen and check that the disclaimer is not shown
3. Let the bench end the call
4. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 3 (Idle)
5. Bring the HU to Full-Operation mode
6. Read the TLM screen and check that the disclaimer is shown

ER:
1. The incoming phone call is placed
2. The disclaimer is not shown during the call
3. The call is ended
4. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 3 (Idle) is received
5. The HU reaches Full-Operation mode
6. The disclaimer is shown on the TLM screen
```

---
## rows 275–281 — SWE-PM-105（七列，事件各異）

**共通骨架**（`<EVENT>` 逐列代入下表）：
```
PRE:
1. A new bus cycle has started
2. <EVENT-PRE>
3. LIN and CAN tool is available on HU

PROC:
1. Bring the HU to Timed mode while <EVENT-COND>
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 2 (Timed)
3. Read the TLM screen and check that the splash screen is not shown
4. Read the TLM screen and check that the disclaimer screen is not shown

ER:
1. The HU reaches Timed mode
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 2 (Timed) is received
3. The splash screen is not shown on the TLM screen
4. The disclaimer screen is not shown on the TLM screen
```

| row | `<EVENT-PRE>` | `<EVENT-COND>` |
|---|---|---|
| 275 | A phone call is ongoing | the call is ongoing |
| 276 | The backup camera view is displayed | the backup camera view is displayed |
| 277 | An incoming call is present | the incoming call is present |
| 278 | An outgoing call is present | the outgoing call is present |
| 279 | A climate pop-up is displayed | the climate pop-up is displayed |
| 280 | An SOS or Assist call is ongoing | the SOS or Assist call is ongoing |
| 281 | A FOTA pop-up is displayed | the FOTA pop-up is displayed |

---
## row 282 — SWE-PM-105（延後顯示）
```
PRE:
1. The startup screens were skipped earlier in the current bus cycle
2. LIN and CAN tool is available on HU

PROC:
1. Bring the HU to Full-Operation mode again within the same bus cycle
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
3. Read the TLM screen and check that the splash screen is shown
4. Read the TLM screen and check that the disclaimer screen is shown

ER:
1. The HU reaches Full-Operation mode
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
3. The splash screen is shown on the TLM screen
4. The disclaimer screen is shown on the TLM screen
```

---
## row 289 — SWE-PM-111（TBM_Present 分支）
來源：`CFTS009-4941964`「For all screen sizes except 7 inch,
If $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Present$ = [Not Present]
OR $Country_Code$ does not require SOS or Geolocation) then the HU
shall add the ADAS text to the disclaimer」
```
PRE:
1. The screen size is other than 7 inch
2. PROXI VC_VEH_BRAND = a value other than Maserati
3. PROXI TBM_Present = Not Present
4. LIN and CAN tool is available on HU

PROC:
1. Bring the HU to the disclaimer presentation
2. Read the TLM screen and check that the disclaimer screen is shown
3. Read the disclaimer wording and check that the ADAS text is added

ER:
1. The disclaimer presentation is reached
2. The disclaimer screen is shown on the TLM screen
3. The ADAS text is added to the disclaimer
```
⚠ PROXI 依 R-1 v3(c) 不加 `$`；原列作 `$VC_VEH_BRAND$`／
`PROXI $TBM_Present$`，統一為 `PROXI <Param> = <值>`。

---
## row 290 — SWE-PM-111（Country_Code 分支）
同 row 289，**PRE 3 改**：
```
3. PROXI Country_Code = a value that does not require SOS or Geolocation
```

---
## row 291 — SWE-PM-113
```
PRE:
1. The screen size is other than 7 inch
2. PROXI VC_VEH_BRAND = a value other than Maserati
3. PROXI TBM_Present = Present
4. PROXI Country_Code = a value that requires geolocation and SOS in the disclaimer
5. LIN and CAN tool is available on HU

PROC:
1. Bring the HU to the disclaimer presentation
2. Read the TLM screen and check that the geolocation pop-up or the disclaimer is shown
3. Read the shown wording and check that the ADAS text is added
4. Read the shown wording and check that the SOS text is added

ER:
1. The disclaimer presentation is reached
2. The geolocation pop-up or the disclaimer is shown on the TLM screen
3. The ADAS text is added
4. The SOS text is added
```
⚠ 「geolocation pop-up **或** disclaimer」為原 ER 之二擇一表述；
原文（SWE-PM-113 對應 object）未載擇一判準，**維持二擇一措辭，
不推定**。若需判準，標 `PENDING: DR-{n}`。

---
## row 293 — SWE-PM-115
與 row 181 逐字相同（PROC／ER 全同）。
⚠ **A-PM14**：row 181（SWE-PM-070）與 row 293（SWE-PM-115）
之 PRE／Input／PROC／ER 逐字全同，僅 Requirement ID 相異。
與 A-PM04（SWE-PM-080 ≡ SWE-PM-086）同型 —— 兩個 SWE leaf 指向
同一行為。依 §8.2.1 TC 側不得合併或刪列，**兩列各自寫入**，
併入 DR-PW12 作為第七對。
另：**SWE-PM-115 即 A-PM12 所載 037 `Source Requirement ID` 欄
空白之該條**，其 spec_reference 現況維持不動。

---
## 軌 C 完成統計

附件 G 14 列 ＋ 附件 H 16 列 = **30 列**，與軌 C 範圍相符。
其中：
- 來源明載值者 22 列（註明 object id）
- 觸發訊號原文未載、保留抽象動作者 8 列
  （270、275–281、282 之首步）
- 標 `PENDING` 者 0 列（rows 73／74／119／245 之 PENDING 屬軌 B，
  已由執行層登記 DR-PW20）
- 新增異常：A-PM13（265–268＋13 五列同文）、A-PM14（181≡293）
