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
| M-2 | `GW_B_5.Mute_Button` | CAN 訊號名（由 LID r1038 `ICSMuteButton` 之 Atlantis High 欄解得，該列三個候選之一） | 同上兩本 | **是** —— LID `CAN` 欄為 `CAN-B`，訊息 `GW_B_5` 存在於 BHCAN2-R1 | **查無**：兩本 DBC 皆無此 `SG_`。惟同列另兩個候選（`CLIMATIC_PANEL.Radio_btn4`、`DIS_CENTERSTACK.DCSD_Mute`）**皆已解得**，故 `ICSMuteButton` 本身不受阻 | display | DR-DM5 | OPEN（低影響） |

## 查詢範圍聲明（本輪）

2026-08-24，Display：以 SYS2 `Basic Report` FR 母體（80 列）之 15 個
`$Signal$` 為查詢集，經 LID `CAN Mapping` 之 `Atlantis High` 欄組解析後
共 26 個 `MESSAGE.Signal` 值，逐一查上列兩本 DBC。

- resolved = Y：**24 / 26**
- resolved = N：**2 / 26**（即上表 M-1、M-2）
- 15 個 `$Signal$` 中，至少解得一列者 **14 / 15**；完全未解者 **1**
  （`CCDMF_RQ_DISP_INTS`）

逐列證據見 `features/display/data/signal_resolution.tsv`。

> 下放包 04 §3.4 記「SYS2 之 15 個 `$Signal$` 全數解得」。該陳述在
> **LID 階段**成立（15/15 皆能在 LID 找到列），在 **DBC 階段**不成立
> （`CCDMF_RQ_DISP_INTS` 之 CAN 名不在任一本 DBC 中）。R-DM17 之解析鏈
> 為三段，「解得」須指明止於哪一段。
