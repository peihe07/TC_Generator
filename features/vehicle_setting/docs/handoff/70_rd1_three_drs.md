# 70 下放包 — 三份 DR 之送件文（可直接複製寄出）

分析層寫入，2026-08-23。**Pei 指示列出三份 DR 之內容。**

三份合計可解鎖 **43 條**（DR-25′ 23／DR-15′ 13／DR-19 7），
為池空後唯一能再產出 TC 之路徑。

---

## 送件文（以下整段可複製）

> **收件**：CFTS044 Vehicle Controls 規格擁有者
> **來源**：SWQT — R1LR Atlantis-H，Vehicle Setting（CFTS044 Vehicle Controls）
> **日期**：2026-08-23
> **基線**：
> CFTS044 `R1LR_Atl-H_25PI3.5_…CFTS_044_Vehicle Controls_SR26_20250909-1816.docx`
> ／SWRA 037 四本／`Logical Identifiers and CAN Mapping v1.76`
> ／`PDT27_E2A_R4_BHCAN.dbc`／`PDT27_E2A_R5_FDCAN8.dbc`
> （二者 VersionYear 25、VersionWeek 50）
>
> 下列三項於測試用例撰寫中發現，皆為規格與 CAN 資料庫之間之不一致。
> 三項合計影響 **43 個 SWE leaf** 之測試用例。
> 每項皆附我方之實測依據、暫行處置、與影響範圍。

---

### 一、請求訊號承載階數或為單一位元（DR-15′，影響 160 leaf，其中 13 條待生成）

**問題**：加熱／通風座椅之請求訊號，其承載階數或為單一位元？

**證據一 —— CFTS044 之條文（標記 `[EE Architecture:Atlantis High]`）**

條文 `4858325`（`$FL_HS_RQ$`）／`4858355`（`$FR_HS_RQ$`）／
`4858385`（`$FL_VS_RQ_TGW$`）／`4858416`（`$FR_VS_RQ_TGW$`）
令 HU 依座椅**目前狀態**送出循環降階之值：

| 目前狀態 | 送出之值 |
|---|---|
| High | Medium |
| Medium | Low |
| Low | Off |
| Off | High |

即該請求訊號**承載四個階數值**。

**證據二 —— 基線 CAN 資料庫**

`PDT27_E2A_R4_BHCAN.dbc` 之
`TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm`／`FR_HS_Tlm`／`FL_VS_Tlm`／`HSW_Tlm`
皆為 **1 bit**，值表為 `0 = Not_Pressed`／`1 = Pressed`。
即該請求訊號**只有二值**。

**證據三 —— LID v1.76 之同一列（列 769）**

同一個 LID `FL_VS_RQ_TGW` 於兩個欄組對映至不同訊號：

| 欄組 | 訊號 | 值域 |
|---|---|---|
| `Atlantis` | `TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm` | 2 bit，四階（Off／Low／Medium／High） |
| `Atlantis High` | `TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm` | 1 bit（Not_Pressed／Pressed） |

且該表對**請求類** LID 之 `Format` 欄**無位元寬宣告**，
而對**狀態類** LID（如 `HeatedSeatFL`）明載 `2 bit signal`。

**我方之觀察**：三份證據可一致地解釋為 ——
**四階者屬 Atlantis Mid 架構，二值者屬 Atlantis High**；
而 CFTS044 描述循環降階之四條條文標記為 `Atlantis High`，
**其架構標記疑為自 Atlantis Mid 遷入時未更新**。

**請確認（擇一）**

| | |
|---|---|
| **(a)** | 請求訊號為 1 bit，階數之循環由 HU 內部狀態機決定 → 則 `4858325` 等四條之描述應改 |
| **(b)** | 請求訊號承載階數 → 請提供其實際 signal 名、bit 寬、值表 |
| **(c)** | 兩者皆是，依 EE Architecture 分流 → 則 `4858325` 等四條之 `[EE Architecture]` 標記應為 `Atlantis Mid` |

**另請確認**：該行為是否隨 `$Heated_Seat_Levels$`（1／2／3）之配置而不同？

**影響**：Heated Seat 88 ＋ Vented Seat 72 共 160 個 SWE leaf 之測試步驟、
預期結果與測試設計方法（Functional Based vs Decision Table）。
其中**已交付 6 條**之斷言落在該五個 token 上，覆後須逐條複檢；
**尚有 13 條因之未能生成**。

---

### 二、Mid 網段之命令訊號不在基線資料庫（DR-25′，影響 65 leaf，其中 23 條待生成）

CFTS044 之 SWE leaf 其行為賦值於下列四個訊號，
而該四者於基線 CAN 資料庫中**皆不存在**（`SG_` 命中各 0）：

| 訊號 | 受影響 leaf |
|---|---:|
| `TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm` | 17 |
| `TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm` | 16 |
| `TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm` | 14 |
| `TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm` | 14 |
| **相異 leaf 合計** | **61** |

基線兩檔僅有 `TELEMATIC_VEHICLE_SETUP3`（**無** `SETUP`、**無** `SETUP2`）。
而 `Logical Identifiers and CAN Mapping v1.76` 之 `Atlantis` 欄組
確載其值域（列 763：`0 = Heated_seat_off` … `3 = Heated_seat_high`）。
該等條文之 `EE Architecture` 皆為 `Atlantis Mid`。

**另有一訊號** `HSW_Cmd_Tlm`（4 leaf）：其名見於 CFTS044 條文，
**而其值域於 LID 兩欄組皆為空**，故與上開四者處置不同（我方標為值域無來源）。

**請確認（擇一）**

| | |
|---|---|
| **(a)** | 承載該四訊號之 CAN 資料庫為何？請提供 |
| **(b)** | 該等訊號不適用於 R1LR，其對應之 CFTS044 條文於本專案不需驗證？ |

**我方之暫行處置**：以規格與 037 分析報告所載為主，
訊號名取來源逐字撰寫測試用例，並標記其依賴。
**該等測試用例在現行 CAN 環境上無法執行**，其依賴已逐條標記。
若答覆為 (b)，該 65 leaf 之測試用例逐條撤回。

---

### 三、`$EngRun_Stat$` 之規格值無匯流排對應（DR-19，影響 7 leaf）

CFTS044 條文 `4858551`／`4858553`／`4858555`
（`[EE Architecture:Atlantis High]`）以

```
$EngRun_Stat$ = [IDLE_STBL] ／ [UNLIMITED] ／ [LIMITED] ／ [RUN]
```

為 Stop/Start 開關可用性之判定條件。

惟 `Logical Identifiers and CAN Mapping v1.76` 將 `EngRun_Stat`
對映至 `STATUS_CCAN3.EngineSts`，其 `Format` 與基線 DBC 之 `VAL_` 皆為

```
0 = Engine_Off ／ 1 = Engine_Cranking ／ 2 = Engine_On ／ 3 = SNA
```

**四個規格值於 LID 與 DBC 中皆無對應。**

**請提供**該四值之匯流排對應（訊號名、message、raw 值），
或確認其應改用他訊號。

**我方之暫行處置**：測試用例以來源之逐字值撰寫
（如 `STATUS_CCAN3.EngineSts = IDLE_STBL`），**不附 raw 碼**
—— 推導一個 raw 碼即為造值。覆後補入 raw 碼。

---

> **回覆之優先序（依其對我方之解鎖量）**
>
> | 序 | 項 | 可解鎖之測試用例 |
> |---|---|---:|
> | 1 | 二（Mid 網段命令訊號） | **23** |
> | 2 | 一（請求訊號之階數） | **13**（另 6 條已交付者須複檢） |
> | 3 | 三（`EngRun_Stat`） | **7** |
>
> 我方現已交付 143 條測試用例，母體 237 個 SWE leaf。
> **上開三項為目前唯一能使產出繼續之外部依賴。**

---

## 送出後之處置（分析層備忘，不屬送件文）

| 項 | 處置 |
|---|---|
| 三份標記 | `DATA_REQUESTS.md` 逐筆標「送出 2026-08-23／待覆」 |
| DR-15′ | 已送出者以本文**補送**（其原文較簡） |
| 覆後 | DR-15′ 覆後須複檢已交付 6 條；DR-25′ 覆為 (b) 則撤回 65 條；DR-19 覆後補 raw 碼 |
| 其餘八份 | DR-17／18／20／21／22′／23／24′／26／27 不在本次送件，其解鎖量皆 ≤ 2 或為 0 |
