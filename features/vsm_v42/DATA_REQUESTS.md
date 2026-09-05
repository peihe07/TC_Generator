# DATA_REQUESTS — Vehicle Setup Management R1 Low（VF665 V42）

DR 送出權屬 Pei（Tier 3）；分析層草擬、登記。每包上繳附未結 DR 清單（IN §8.4.3）。
一 DR 一條目（`## DR-VLn`），表列摘要與條目同步更新（R-ICS29 型教訓：不得雙表）。

> **機讀狀態欄（格式已定，本檔尚未回填）** —— 格式見
> `docs/fw036/templates/DATA_REQUESTS.md`：每一個 `## DR-<n>` 節之首行寫
> `status: open|sent|closed（YYYY-MM-DD）`。**本包只加本段說明，不回填既有節**
> （GC-09 §一-6／GC-12 §二-4）。未取號之草稿節不寫 `status:` ——
> 未送出不佔號（`down/20260901_VS-SL-01_review.md` §2.2）。
> 本檔現況：`## DR-` 節 4 個，具 `status:` 者 0 個。

| DR | 項目 | 阻塞 | 影響 | 狀態 | 送出日 | 回覆日 |
|---|---|---|---|---|---|---|
| DR-VL1 | V42 SYSRA Functional 318 列中 **191** 列無 037 覆蓋（覆蓋揭露） | no | 母體外 191 列 | 已登記，**Pei 裁先不送（2026-09-02）** | | |
| DR-VL2 | 037／SYSRA 標註完整性三面（A-VL5／A-VL6／A-VL7） | no | 母體 1 列、分母 112 列 | 已登記，**Pei 裁先不送（2026-09-02）** | | |
| DR-VL3 | ATL-Mi DBC | ~~yes~~ | 全線 CAN 訊號 | **結案（2026-09-02，Pei 放件 `Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc`，R-VL14）** | | 2026-09-02 |
| DR-VL4 | V42 內部訊號（`X.Req`／`X.Info`／`X.GUI`，未解 92 名：v3 現行之止於段 1 非 CAN 94 扣 PROXI 2）之驅動與觀察對照總表（形制照 DR-PW23／同 DR-VT4） | **yes（P4 起：遭遇即 PENDING）** | 內部訊號實名 | 已登記，**從 Pei「先不送」之既裁，未送出** | | |

---

## DR-VL1 —— V42 SYSRA 未被 037 覆蓋之 Functional 列

- **來源**：intake 實測（2026-09-01）。`FMWIFSM035A02_VF665_V42_…SYSRA_VF665_V42_Released.xlsx`
  `Analysis Report` 分頁 Functional Requirement 318 列；037 兩份之 Source Requirement ID
  （`Sys-RA-VF665_V42_VSM-nnn`）去重後對應 128 列。
- **實數回填（2026-09-01，下放包 02 W-4 跨源對帳）**：037 之 128 個 Functional
  Source ID **128／128 全數命中** SYSRA `Sys-RA-Feature-ID`（E16 相符）；惟其中
  **1 列**（`Sys-RA-VF665_V42_VSM-857`）於 SYSRA 之 `分類 Category` 為 `Heading`
  而非 Functional（A-VL7）。故被 037 覆蓋之 SYSRA **Functional** 列實為 **127**，
  未覆蓋為 **318 − 127 = 191**（原估「約 190」）。
  掃描條件：SYSRA `Analysis Report` 表頭列 5，`分類 Category` 全等
  `Functional Requirement`；037 兩檔表頭列 7／8，`Categorization` 全等
  `Functional Requirement`；比對為 Source ID 逐字。
- **問題**：其餘 **191** 列 Functional 無 SWE1 分析（037），依 R-VL4 不入 TC 範圍。
  請上游確認：(a) 該 190 列是否另有 037 報告在途；(b) 或其為刻意不分析之範圍
  （如 Out of Scope 之漏標）。
- **阻塞**：否。母體 128 之生成不受影響。
- **本地處置**：覆蓋台帳列出該 190 列之 `Sys-RA-Feature-ID` 與 `Chapter for VF`，
  標 `No 037 — out of mother set (R-VL4)`；交付說明揭露。
- **另記（A-VL6）**：該 318 列中 112 列之 `EE Architecture` 與 `Document ID`
  兩欄同時為空，無從判其是否適用本線（ATL-Mi／`VF665_V42_P637MCA`）；
  與本 DR 之交集未另計，不合併。
- **請求動作**：Pei 決定是否送出；送出則向 SWE1 報告作者索取在途清單。

## DR-VL2 —— 037／SYSRA 標註完整性（A-VL5／A-VL6／A-VL7 三面一問）

- **來源**：上繳 02 第 7 節；分析層裁併為一 DR（同一上游、同一主題）。
- **問題**：(a) 037 Park Sense 檔 `SWE1-VC-IntelligentSpeedLimiterwithConfirmation-051` 之 `Categorization` 空，請確認其為 Functional 或 Information；
  (b) SYSRA Functional 318 列中 112 列 `EE Architecture` 與 `Document ID` 同時空，請確認是否適用 ATL-Mi／`VF665_V42_P637MCA`；
  (c) 037 leaf `SWE1-VC-SurroundCameraGridlines-063` 之 Source ID `Sys-RA-VF665_V42_VSM-857` 於 SYSRA 為 `Heading`，請確認其正確 Source ID。
- **阻塞**：否（(a) 一列先以 UNCATEGORIZED 保留於 leaves.tsv，不入母體也不排除；(c) 一列仍入母體，Remarks 註）。
- **請求動作**：Pei 決定；建議與 DR-VL1 併送。

## DR-VL3 —— ATL-Mi 之 DBC（阻塞 P4）

- **來源**：R-VL12(b)／A-VL10。分析層實測 LID v1_78 `CAN Mapping` 有獨立之 `Atlantis`（P–T）與 `Atlantis High`（Z–AD）欄組，
  本線（ATL-Mi）之規格訊號名對 Atlantis 欄命中率為 Atlantis High 之兩倍，且 Atlantis 欄之 `CAN` 值為 CAN-B／CAN-C。
  forms/ 現有 DBC（`PDT27_E2A_R1_BHCAN2`／`R1_FDCAN8`）為 Atlantis High 之 FD／BH-CAN，非本線所需。
- **問題**：須取得 ATL-Mi（P637 ProMaster；V43 之 P363 同）之 CAN-B／CAN-C DBC（與 LID Atlantis 欄同世代）。
  **先問 Pei 手上有無**（`features/vehicle_setting/inputs/` 之 R4 BHCAN／R5 FDCAN8 仍為 PDT27 家族，預期非此件，待實測）；無則向上游索。
- **阻塞**：是（P4 起）。到件前 CAN 訊號一律「段3待ATL-Mi DBC」，不得寫 `$…$`。
- **本地處置**：段 1 先以 Atlantis 欄解至 `MESSAGE.Signal`（段 2），對 Atlantis High DBC 實查結果併記旁證。
- **請求動作**：Pei 先答「有／無」；無則送出，與 vsm_v43 DR-VT5 同一件。

## DR-VL4 —— V42 內部訊號之驅動與觀察對照總表（P4 PENDING 之錨）

- **來源**：R-P355(c) 之 PENDING 格式需 DR 號可錨；vsm_v43 DR-VT4 之 V42 同型（彼 DR 早已預告「vsm_v42 同型需求於其 W-5 後另登」）。
  v3 現行：內部形未解 92 名（Req 62／Info 28／GUI 2），五輪擴充均零變動，同 DR-VT4 之證。
- **問題**：同 DR-VT4（驅動方法＋可觀察面，形制照 DR-PW23），名單取 v3 類別＝內部且結果＝未解得(止於段1) 之列。
- **阻塞**：P4 起（遭遇即 `PENDING: DR-VL4 <名>`）。pilot EPB 家族內含內部形者同。
- **狀態**：從 Pei「先不送」之既裁，未送出；登錄僅為 PENDING 錨號。

### 執行層結案紀錄（2026-09-02，下放包 03 補遺之 W-5′）

- **到件**：`forms/Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc`
  sha256 `5cac2abcecdf37e2f07991e26dc4cf748fe24874fde93af77a85ea8936d3ed16`
  （425,072 bytes；ISO-8859 text／CRLF —— 解析以 latin-1 讀，R-VL14(a)）。
- **驗收**：`BO_ 139` **相符**、`VAL_ 619` **相符**、`SG_` 實測 **844**
  （條文載 5568 —— **不符，見 A-VL11，不調和**；844 為 `^\s*SG_ ` 訊號定義行數，
  去重 794 名）。R-VL14(b) 之六個爭議訊息（`TELEMATIC_VEHICLE_SETUP2`／
  `IPC_VEHICLE_SETUP2`／`IPC_VEHICLE_SETUP3`／`SERVICE_SETUP`／
  `TELEMATIC_SERVICE_SETUP`／`STATUS_CCAN3` 含 `VehicleSpeedVSOSig`）**逐一複驗全數在內**。
- **重跑結果**（`data/signal_chain_v42_v3.tsv`）：**解得 98**（CAN 95）；
  「訊息名不符(R-13)」由 v2 之 40 降為 **7**；「段3待ATL-Mi DBC」73 名歸零。
- **R-VL14(c) 之 CAN-C 情形**：本線實測 **0 名** —— 9 個「未解得(止於段3)」之
  `Atlantis CAN` 欄皆為空，非 CAN-C。**CAN-C DBC 於本線目前無實據需求，不預開 DR**（Pei 裁先不送）。

