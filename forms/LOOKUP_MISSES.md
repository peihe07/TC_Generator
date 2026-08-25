# LOOKUP MISSES — 全案查無台帳

依 **R-G14**（Pei 2026-08-24，全域）。本檔為全案唯一之查無台帳，
目的為避免同一個 miss 被各 feature 重複發現、重複向上游提問。
**新 feature 開案時須先讀本檔。**

登記門檻為 **R-G13** 之三要件，缺一不得登記為「查無」，只得記為「未查得」：

1. 查了哪些檔（檔名 + SHA256）
2. 用什麼名字查（LID 名？CAN 訊號名？規格原文名？）
3. 該檔之涵蓋範圍是否本應包含之（匯流排、架構、版次）

登記於本檔之同時，仍須於該 feature 之 `ANOMALIES.md` 登 anomaly、
`DATA_REQUESTS.md` 開 DR —— 三處各有其職，不互相取代：台帳防重複發現，
anomaly 綁該 feature 之批次，DR 綁上游提問。

各檔之涵蓋範圍見 `forms/FORMS.md` 之「參考資料庫（DBC / PROXI / LID）」節。
SHA256 於下表以前 16 碼記，全碼見該節。

---

## 台帳

| # | query | 查詢用之名稱種類 | 查了哪些檔（SHA256 前 16 碼） | 涵蓋範圍是否應含 | 結果 | 發現之 feature | DR 編號 | 狀態 |
|---|---|---|---|---|---|---|---|---|
| M-1 | `RADIO_B4.CCDMF_RQ_DISP_INTS` | CAN 訊號名（由 LID r255 之 Atlantis High 欄解得；SYS2 原文為 `$CCDMF_RQ_DISP_INTS$`） | `PDT27_E2A_R1_BHCAN2.dbc`（`46cb73f3db62ac9f`）、`PDT27_E2A_R1_FDCAN8.dbc`（`2a86c4bf3e670d71`） | **是** —— LID 之 `CAN` 欄為 `CAN-B`，且訊息 `RADIO_B4` 本身**存在於 BHCAN2-R1**，故該訊號本應在其中 | **查無**：兩本 DBC 皆無此 `SG_` | display | DR-DM5 | OPEN |
| M-3 | `Display_OFF_SoftKey_Prsnt` | PROXI 參數名（由 LID `Proxi & Configuration` r63 `DSP_SK_PRSNT` 之 `Atlantis & Atlantis High` 欄組 `Signal Name` 解得） | `PROXI_HDCC27_R3_20250424.xlsx`（`e7c2020f01c3d58d`） | **是** —— 該 `Format` 分頁確實載有同類之 soft-key 參數（r436 `FCW_Soft_Button`、r494 `Rear_View_Camera_Soft_Button`、r692 **`Display_OFF_SoftKey`**、r803 `Glove_Box_Soft_Button`） | **查無**：`Parameter Name` 欄無 `Display_OFF_SoftKey_Prsnt`。r692 之 `Display_OFF_SoftKey` 僅差 `_Prsnt` 尾綴，**但逐字不等，本輪不認定其為同一物**（下放包 05 §六第 14 條）。另試之鍵 `EC_AudTel2-<DSP_SK_PRSNT>`、`DSP_SK_PRSNT` 亦查無 | display | DR-DM6 | OPEN |
| M-2 | `GW_B_5.Mute_Button` | CAN 訊號名（由 LID r1038 `ICSMuteButton` 之 Atlantis High 欄解得，該列三個候選之一） | 同上兩本 | **是** —— LID `CAN` 欄為 `CAN-B`，訊息 `GW_B_5` 存在於 BHCAN2-R1 | **查無**：兩本 DBC 皆無此 `SG_`。惟同列另兩個候選（`CLIMATIC_PANEL.Radio_btn4`、`DIS_CENTERSTACK.DCSD_Mute`）**皆已解得**，故 `ICSMuteButton` 本身不受阻 | display | DR-DM5 | OPEN（低影響） |

## 備註區

### B-1　BHCAN2 取代 BHCAN 對其他 feature 之潛在影響（R-DM19，登記不評估）

`forms/PDT27_E2A_R1_BHCAN2.dbc` 與
`features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc` **非版次關係**：
訊號名集合三分為「兩者皆有 310／僅 R4 有 **573**／僅 BHCAN2 有 32」
（實測見 `features/display/data/` 之 dbc_probe 輸出與 A-DM14）。

Display 依 R-DM19 選定 BHCAN2；其 15 個 `$Signal$` 未受影響。
**其他使用 B-CAN 之 feature（vehicle_setting、power、power_moding 等）
若改用 BHCAN2，須逐一複驗其既有訊號** —— 573 個訊號名不在新檔中，
且三個顯示訊號之 tx／rx 節點在兩檔中相反（A-DM14）。

本條為**登記**，不評估、不建議任何 feature 改版。既有交付件依慣例
（同 R-G1）不因新檔而改。

### B-2　LID v1.78 vs v1.76 之差異（2026-08-24 實測）

以 `CAN Mapping` 之 `Atlantis High` 欄組 `Signal Name` 為比對面、
`Logical Identifier` 為鍵：**相異僅 2 個**（相同 2,546；單側有 0）。

| Logical Identifier | 差異 |
|---|---|
| `CallAction` | v1_78 有 `TELEMATIC_VEHICLE_SETUP.CallAction`；v1_76 該格為空 |
| `EngineRPM` | v1_76 多 `ENGINE_FD_2.EngRPM`；v1_78 無 |

**兩者皆未出現於任何 feature 之已交付 TC**（逐字搜尋
`features/*/generated`、`batches`、`output` 之 `CallAction`／`EngineRPM`／
`EngRPM`／`EngineSpeed` 皆 0 命中），故下放包 05 §六第 15 條之停止條件
**未觸發**。

> 惟訊息名 `TELEMATIC_VEHICLE_SETUP` **確實**出現於 vehicle_setting 之
> 多個 batch。相異的是其下之 `CallAction` 訊號，非該訊息本身。

全表見 `features/display/data/lid_v178_vs_v176.tsv`（2,548 列）。

---

## 查詢範圍聲明（本輪）

2026-08-24，Display：以 SYS2 `Basic Report` FR 母體（80 列）之 15 個
`$Signal$` 為查詢集，經 LID `CAN Mapping` 之 `Atlantis High` 欄組解析後
共 26 個 `MESSAGE.Signal` 值，逐一查上列兩本 DBC。

- resolved = Y：**24 / 26**
- resolved = N：**2 / 26**（即上表 M-1、M-2）
- 15 個 `$Signal$` 中，至少解得一列者 **14 / 15**；完全未解者 **1**
  （`CCDMF_RQ_DISP_INTS`）

逐列證據見 `features/display/data/signal_resolution.tsv`。

**R-DM21：上列各數字所止之段** —— 段 1（SYS2 → LID）15/15；
段 2（LID → CAN 名）解出 26 個值；段 3（CAN 名 → DBC）24/26 列、
14/15 個訊號。**「全數解得」只在段 1 成立。**

2026-08-24，Display（PROXI）：以 LID `Proxi & Configuration` 之 446 列為
母體，經其 `Atlantis & Atlantis High` 欄組 `Signal Name` 解出 PROXI 側
參數名後，查 `PROXI_HDCC27_R3_20250424.xlsx` 之 `Format` 分頁
（1,058 個 `Parameter Name` 資料列）。逐字查得定義者 **177/446**。
未查得者多數未逐一登記為 miss —— 其中大部分與本 feature 無關；
僅本 feature 明確追查之 `DSP_SK_PRSNT` 登記為 M-3。

> **未登記 ≠ 已查無。** 其餘 269 列之狀態為「本輪未追查」，
> 不得引為其不存在之證據（R-G13）。

> 下放包 04 §3.4 記「SYS2 之 15 個 `$Signal$` 全數解得」。該陳述在
> **LID 階段**成立（15/15 皆能在 LID 找到列），在 **DBC 階段**不成立
> （`CCDMF_RQ_DISP_INTS` 之 CAN 名不在任一本 DBC 中）。R-DM17 之解析鏈
> 為三段，「解得」須指明止於哪一段。
