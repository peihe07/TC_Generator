# 37 下放包 — RD-1 送件文（合併八項）與狀態更新

分析層寫入，2026-08-20。Pei 指示送出 DR-15／17／18／19／20。

---

## 1. 建議：**八項一次送，不是五項**

現行未結 DR 共八項。Pei 指示之五項外，另有三項亦已具備可回答之形式：

| DR | 阻塞？ | leaf | 定稿於 | 現況 |
|---|---|---:|---|---|
| DR-15 | **阻塞** | 160 | 17 包 §2.3（18 包更正引用） | 待送 |
| DR-17 | **阻塞** | 14 | 30 包 §2 | 待送 |
| DR-19 | **阻塞** | 3 | 35 包 §3 | 待送 |
| DR-20 | **阻塞** | 1 | 35 包 §3 | 待送 |
| **DR-14′** | **阻塞** | **16** | **14 包 §2** | **未列於 Pei 之五項** |
| DR-18 | 確認型 | 160 | 32 包 §3 | 待送 |
| DR-8 | 不阻塞 | 8 引用 | 00G §5 | 早輪未結 |
| DR-12 | 不阻塞 | — | 29 包 §1.2 | 早輪未結 |

**DR-14′ 阻塞 16 個 leaf，與 DR-17（14 個）同量級，遺漏它會使
Third Row Headrest Dump 之 21 個 leaf 中之相關者第二次卡住。**
DR-8／DR-12 不阻塞，但其邊際成本為同一封信之兩段文字。

**分析層建議八項一次送。** 若 Pei 仍只送五項，DR-14′／DR-8／DR-12
維持未送狀態，執行層據此記載。

---

## 2. 送件文（可直接複製）

> **【執行層記載，19 輪 D-10】**
> **Pei 於 2026-08-22 送出本文之第 1–5 項**（阻塞項全數）：
> 第 1 項 = DR-15、第 2 項 = DR-17、第 3 項 = DR-14′、
> 第 4 項 = DR-19、第 5 項 = DR-20。**五項皆轉為「待覆」。**
> **第 6–8 項（確認項）未送**：第 6 項 = DR-18 維持待送；
> 第 7 項（`$VC_VEH_LINE$` 車型碼）與第 8 項（`$PowerMode$` 之 `IGN_OFF_ACC`）
> **於 `DATA_REQUESTS.md` 中無對應之 DR 編號**，見上繳 17 §2。
> 本項依 D-8 之「未送者維持待送，**不得推定**」記載，未作任何推定。

> **收件**：CFTS044 / Comfort HMI / Vehicle Controls 規格擁有者
> **來源**：SWQT — R1LR Atlantis-H，Vehicle Setting（CFTS044 Vehicle Controls）
> **日期**：2026-08-20
> **基線**：
> CFTS044 `R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_044_Vehicle Controls_SR26_20250909-1816.docx`
> ／SYS2 `…20250815-1022_20260324_Version3_Released.xlsx`
> ／SWRA 037 四本（Common Features／HeatedSeat／VentedSeat／Heated Steering Wheel）
> ／`Logical Identifiers and CAN Mapping v1.76`
> ／`PDT27_E2A_R4_BHCAN.dbc`（VersionYear 25／VersionWeek 50）
> ／`PDT27_E2A_R5_FDCAN8.dbc`（同上，BusType = CAN FD）
>
> 下列八項為測試用例撰寫過程中，於規格與 CAN 資料庫之間發現之不一致或
> 未具名引用。前五項阻塞用例撰寫，後三項為確認。
> 每項皆附我方之實測依據與影響範圍。

### 阻塞項

**1. 請求訊號承載階數或為單一位元（影響 160 個 SWE leaf）**

CFTS044 條文 `4858325`／`4858355`／`4858385`／`4858416`
（`[EE Architecture:Atlantis High]`）定義請求訊號依目前座椅狀態送出
循環降階值：High→Medium、Medium→Low、Low→Off、Off→High。

惟基線 DBC 之 `TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm`／`FR_HS_Tlm`／
`FL_VS_Tlm`／`HSW_Tlm` 皆為 **1 bit**，值表為 `0 = Not_Pressed`、
`1 = Pressed`；`Logical Identifiers and CAN Mapping v1.76` 之
Atlantis High 欄組亦將該等請求對映至上述 1 bit 訊號，
且其 Format 欄**無位元寬宣告**（狀態訊號則明載 `2 bit signal`）。

請確認：
(a) 請求訊號為 1 bit，階數之循環由 HU 內部狀態機決定；或
(b) 請求訊號承載階數 —— 若是，其實際 signal 名、bit 寬、值表為何？
(c) 該行為是否隨 `$Heated_Seat_Levels$`（1／2／3）之配置而不同？

影響：Heated Seat 與 Vented Seat 兩個測試集之測試步驟、預期結果與
測試設計方法（Functional Based vs Decision Table）。

**2. 單階加熱座椅之畫面行為（影響 14 個 SWE leaf）**

CFTS044 定義單階加熱座椅之配置（`$Heated_Seat_Levels$ = [1]`）。
而 Comfort HMI Logic and Flow（SWE1-HVAC-*，全母體 129 個相異 leaf）中，
所有座椅加熱／通風之畫面行為條文，其開頭皆逐字為
`For Multi-Level Heated/Vented seats`；明示 `Single-Level` 者僅
`SWE1-HVAC-063`，其主詞為加熱方向盤。以 `single-level` ∧ `seat`
交叉查詢命中 0。

請確認單階加熱座椅之畫面行為：
(a) 由 Comfort 之某條文涵蓋而未明示階數？若是，請指明其 leaf id
(b) 單階座椅無彈窗、直接切換，故 Comfort 無對應條文？
(c) 由第三份文件承載？

**3. 第三排頭枕釋放請求之訊號（影響 16 個 SWE leaf）**

`Logical Identifiers and CAN Mapping v1.76` 載 `HdRstRelRq` 之
Atlantis High 對映為 `RADIO_B3.HDRstRelRq_3rdRow`，
但基線 DBC 之 `RADIO_B3` 不含該 signal（其 4 支為 `ManDispCtrl`／
`PowerSideStep_Req`／`RQ_DISP_INTS`／`VR_Blower_Req`）；
兩份 DBC 全域僅有 `Driver_Headrest_Req` 與 `Passenger_Headrest_Req`，
**無第三排**。

請確認第三排頭枕釋放請求之實際 signal 名與所屬 message，
或該功能於本專案是否不落在此二網段。

**4. `EngRun_Stat` 之規格值無匯流排對應（影響 3 個 SWE leaf）**

CFTS044 條文 `4858551`／`4858553`／`4858555`
（`[EE Architecture:Atlantis High]`）以
`$EngRun_Stat$ = [IDLE_STBL]`／`[UNLIMITED]`／`[LIMITED]`／`[RUN]`
為 Stop/Start 開關可用性之判定條件。

惟 LID 表將 `EngRun_Stat` 對映至 `STATUS_CCAN3.EngineSts`，
其 Format 與基線 DBC 之 `VAL_` 皆為 `0 = Engine_Off`／
`1 = Engine_Cranking`／`2 = Engine_On`／`3 = SNA`。
**四個規格值於 LID 與 DBC 中皆無對應。**

請提供該四值之匯流排對應（訊號名、message、值），
或確認其應改用他訊號。

**5. 未具名之 HMI 需求交叉參照（影響 1 個 SWE leaf）**

CFTS044 條文 `4858560`（`[EE Architecture:Atlantis High]`）逐字為
`… the HMI shall be modified as defined by HMI requirements.`
—— 未具名任何文件、章節或需求 ID。

我方已對 26PI2.5/HMI 目錄之全部 107 檔做全文掃描
（含對一份無文字層之 PDF 施以旋轉 180° 後 OCR），未能定位其所指。

請指明該 HMI 需求之文件與章節。

### 確認項（不阻塞）

**6. 座椅值域之書寫問題（四類）**

一、加熱／通風前綴交叉，4 筆：
`4858393`（§1.3.2.1.3.4）、`4858001`（§1.3.1.1.3.4）、
`4860021`（§1.3.4.12.4）、`4860015`（§1.3.4.12.3）
皆將通風座椅之值寫為 `HS_`（加熱前綴）。
對照：同章節內其餘同型條文一律 `VS_`；全文 `VS_OFF` 15 次對 `HS_OFF` 2 次。

二、值退化，1 筆：`4858413` 為 `[ Pressed]`，
其左側對稱條文 `4858382` 為 `[Vented Seat Pressed / VS_PSD]`。

三、同一值之多種大小寫寫法（`VS_LO` / `VS_Lo`；
`Vented Seat Medium` / `Vented seat Medium` / `Vented seat medium` 等），
影響 30 個參數中之 12 個，含與座椅無關之 `$ESS_ENG_ST$`、`$PowerMode$`。

四、參數名 `$Heated_Steats_Levels$`（`Steats`）與 `$Heated_Seats_Levels$` 並存；
前者於 LID 之 2,974 個識別碼中無對應。

**7. `$VC_VEH_LINE$` 之車型碼對照**

CFTS044 使用 `[DT]`／`[WS]`／`[HDCC]`／`[M240]`／`DS or DJ or D2…` 等代號；
LID 表之 `VC_VEH_LINE` 值域列舉為數字車型碼且截斷於 `101 = WL (65 Hex)`，
二者**完全無交集**。請提供完整之車型碼對照。

**8. `$PowerMode$` 之 `IGN_OFF_ACC`**

CFTS044 條文 `4858978`（`[EE Architecture:Atlantis High]`，Second Row
Headrest Dump）以
`$PowerMode$ = [Ign. off & acc. (4 position switch) / IGN_OFF_ACC]`
為軟鍵可選之條件；而 LID 表將 `PowerMode` 對映至
`STATUS_BH_BCM2.CmdIgnSts`，其值域為
`Initialization / IGN_LK / ACC / RUN / START / SNA`，**無 `IGN_OFF_ACC`**。

請確認其對應之訊號值（是否即 `ACC`，或另有他訊號承載四段式開關之
off & acc 狀態）。

---

## 3. 執行層之狀態更新（併入 18 輪文書）

```text
D-8  `DATA_REQUESTS.md`：將 Pei 實際送出之 DR 逐筆標
       `送出日期 2026-08-20`／狀態 `待覆`
     未送出者維持 `待送` 並註明其未列於本次送件之事實。
     **不得將未送者標為已送。**
D-9  `PLAYBOOK.md` §6 狀態板同步：未結 DR 之「待送／待覆」兩態分列。
D-10 於 `docs/handoff/37_rd1_dispatch.md` 記明實際送出之項次
     （由 Pei 回報，執行層不推定）。
```

---

## 4. 送出後之作業安排

**送出不解除任何阻塞** —— 阻塞於答覆到達時方解除。故：

| 群 | leaf | 現可否生成 |
|---|---:|---|
| Common Features 之非阻塞者 | 42 − 4（DR-19／20） = **38** | **可**，18 輪之 W-55 改寫後續批即取自此 |
| Heated Steering Wheel | 31 | **可**（其 20 + 11 之委派已定，無阻塞 DR） |
| Heated Seat／Vented Seat | 160 | **否**（DR-15） |
| OneStageHeatedSeat | 14 | **否**（DR-17，其中 12 pending） |

→ **答覆未到期間之可生成量為 38 + 31 = 69 個 leaf**，
足供 pilot 通過後之連續數批。**產線不必因等待而停。**

---

## 5. 本包產生之新條文清單（自檢）

無新條文。本包為送件文與狀態更新。
