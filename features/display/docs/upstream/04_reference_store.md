# 上繳包 04 —— 參考素材庫建置，訊號三段解析鏈

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/04_reference_store.md`
- 結果：**步驟 1–12 全數執行；十三條停止條件全未觸發**
- 全部 git 操作屬 Pei —— §9 只備妥訊息與 pathspec，未執行

---

## 0. 本輪之兩項偏離與一項條文衝突（先講）

### 0.1 `.gitignore` 改了一行 —— 否則 R-G14 無法執行

下放包 §2 記「`forms/*` 已被 `.gitignore` 排除、`FORMS.md` 已 tracked，
形狀正確，**不需改 `.gitignore`**」。該判斷對那四個資料檔成立，但
**R-G14 要求 `forms/LOOKUP_MISSES.md` 為 tracked**，而
`git check-ignore` 實測其被 `forms/*` 排除。

`.gitignore` 已列於本下放包標題之範圍內，故加一行否定（附理由註解）：

```
forms/*
!forms/FORMS.md
# R-G14 (2026-08-24): the全案 lookup-miss ledger lives in forms/ and must
# be tracked. The reference databases themselves (DBC/PROXI/LID, R-G12)
# stay untracked like every other company document here.
!forms/LOOKUP_MISSES.md
!forms/.gitkeep
```

改後逐檔複驗：`LOOKUP_MISSES.md` **不再被忽略**；三份資料檔
（DBC／LID／PROXI）**仍被忽略**。四份素材皆未入 git。

### 0.2 R-DM16 之 regex 與其所載之數字不一致 —— 依條文照做，兩者並列

R-DM16 指定寬式 `\[([^\]]+)\]`，並記「實測相異 13 個」。**兩者不相容。**
本輪實測（同一母體、同一欄）：

| 定義 | 相異 token | 含 `[value]` 之列數 |
|---|---|---|
| `\[([A-Z0-9_]+)\]`（R-DM14 原引，已撤回） | 9 | — |
| `\[([A-Za-z0-9_%\s]+)\]`（上繳 03 所量，即條文之「13」） | **13** | 34 |
| `\[([^\]]+)\]`（**R-DM16 條文所指定**） | **44** | **54** |

44 之多出者為 Polarion 匯出自身之 metadata：`[State:Approved]`、
`[Market:All]`、`[Radio:R1H]`、`[Artifact Type:Subsystem Functional
Requirement]`、`[EE Architecture:Atlantis High]` 等，**不是訊號值**。

處置：`values` 欄依**條文之 regex** 產出；同時新增 `values_narrow` 欄保留
13-token 定義。兩者並列於 `data/coverage_sys2_vs_swe_dm.tsv`，
**未自行擇一**。請裁示 R-DM16 應以其 regex 為準（44）或以其數字為準（13）。

> 本輪未逕自採用 13 —— 那會是以我上輪的量測去覆蓋一條裁決條文的字面。

### 0.3 步驟 11 之停手條件：逐字未成立，但相鄰性已登記

步驟 11 之觸發為「LID `Proxi & Configuration` 分頁與本 feature 之**訊號**
有關聯」。逐字測試：15 個 SYS2 `$Signal$` 在該分頁 **0 命中** → 條件
未成立，故未停手，且**未做任何 PROXI 解析**。

惟關鍵字掃描命中 23 列，其中 `DSP_SK_PRSNT`（Display off soft key
present）、`RVC_SK_PRSNT`（Rear Camera soft key present）、`DCSD_cfg`
（DCSD Present）三者與 leaf 之前置條件明顯相鄰。以 **A-DM16** 登記並提請
裁示觸發條件是否應放寬。詳見 §6。

---

## 1. §四五條之抄錄核對表（步驟 1）

抄錄方式：機器抽取下放包之 fenced 區塊原樣寫入，未經人工轉錄；
抄畢反向抽取並與原檔逐字元 `==` 比對。

**全域三條 → `docs/fw036/RULINGS_LEDGER.md`**（新節「參考素材庫條文」）：

| 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|
| R-G12 | 528 | `c9fb52dea97b1e7d` | 是 |
| R-G13 | 387 | `a1ba5e165f2ac4a9` | 是 |
| R-G14 | 363 | `0d18b275bc94b0a9` | 是 |

**Display 兩條 → `features/display/RULINGS.md`**：

| # | 條號 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|
| 18 | R-DM16 | 462 | `4ab4b941b20a8fbc` | 是 |
| 19 | R-DM17 | 579 | `c575758943f0dd3e` | 是 |

**5/5 逐字元相符**；Display 累計 **19/19**（01 包 8、02 包 5、03 包 4、
04 包 2）。下放包 04 之另一個 fenced 區塊（§3.1 之四個 FPDM 訊號列表）
為資料非條文，未計入。

R-DM14 之原文依 R-TM13 保留於 `RULINGS.md`，未刪除、未改寫；
R-DM16／R-DM17 對其之修正以核對表下方註記載明。

---

## 2. `FORMS.md` 新節全文（步驟 2）

四檔 × 六項必填欄位，涵蓋範圍(b) 全部為本輪實測（不抄下放包 §3.1）。

```markdown
## 參考資料庫（DBC / PROXI / LID）

依 **R-G12**（Pei 2026-08-24，全域）：DBC、PROXI 表、LID 對照表一律置於
`forms/`，不另立 `reference/`。`forms/*` 已由根 `.gitignore` 排除、
`FORMS.md` 已 tracked，形狀未變更（檔案不入 git，manifest 入 git）。

每檔六項必填欄位：(a) 檔名／SHA256／bytes／mtime　(b) 涵蓋範圍
(c) 版次與其來源　(d) 已知不涵蓋者　(e) 取代關係　(f) 首個採用之 feature
與日期。(b) 為必填之理由見 **R-G13**：無涵蓋範圍之登錄，「查無」不構成發現。

涵蓋範圍(b) 一律為執行層實測所得，量測條件見
`features/display/docs/upstream/04_reference_store.md` §4。

### `PDT27_E2A_R1_BHCAN2.dbc`

- **(a)** SHA256 `46cb73f3db62ac9fba6ad8010d7930661983faf01383c022c52ba3c37de1cc60`
  · 167,226 bytes · mtime 2026-08-24T19:59:45
- **(b) 涵蓋範圍**：B-CAN（BHCAN2）。訊號定義列 **344**（相異訊號名 342）、
  訊息 **63**。編碼非 UTF-8（以 cp1252 解讀）；行尾 CRLF 3,359 + 裸 LF 8
- **(c) 版次**：`R1`（檔名所載，非推定）
- **(d) 已知不涵蓋**：FD-CAN 上之訊號。例：`CM_TCH_STAT` 於本檔 0 命中，
  但 LID r368 載其為 `TELEMATIC_FD_5.CM_TCH_STAT`、`CAN` 欄為 `FD` ——
  **本檔本就不該有，不得記為缺漏**（R-G13 之教案）
- **(e) 取代關係**：與 `PDT27_E2A_R4_BHCAN.dbc`
  （`features/vehicle_setting/inputs/`）**並非版次關係**。訊號名集合
  三分實測：兩者皆有 310、僅 R4 有 **573**、僅 BHCAN2 有 **32**。
  何者適用於本專案**未裁定**（A-DM14）
- **(f) 首個採用**：`display`，2026-08-24

### `PDT27_E2A_R1_FDCAN8.dbc`

- **(a)** SHA256 `2a86c4bf3e670d71b362d430b446d8d157c74b94429e833362f81f4a48f6a22e`
  · 1,106,532 bytes · mtime 2026-08-24T19:59:52
- **(b) 涵蓋範圍**：FD-CAN（FDCAN8）。訊號定義列 **1,916**（相異訊號名
  1,634）、訊息 **318**。cp1252；CRLF 19,805 + 裸 LF 2
- **(c) 版次**：`R1`（檔名所載）
- **(d) 已知不涵蓋**：B-CAN 上之訊號。例：`DCSD_DISP_STAT`、
  `RQ_DISP_INTS` 於本檔 0 命中，二者皆在 B-CAN 上
- **(e) 取代關係**：與 `PDT27_E2A_R5_FDCAN8.dbc`（vehicle_setting）並存；
  R5 有訊號定義列 2,037／訊息 323，較 R1 多。兩者之差異本輪未逐一比對
- **(f) 首個採用**：`display`，2026-08-24

### `Logical Identifiers and CAN Mapping v1_78.xlsx`

- **(a)** SHA256 `a01e1679c706cd454daf82573a732fe5ad5eedb3865083897cb18c970b312433`
  · 623,612 bytes · mtime 2026-08-24T20:02:03
- **(b) 涵蓋範圍**：14 個分頁。主分頁 `CAN Mapping` 為 2,627 列 × 35 欄，
  r1 標題／r2 架構分組／r3 欄名／**資料自 r4 起共 2,624 列**。
  架構欄組七個（r2 所載之起始欄）：`LID Information`(c1)／`Powernet`(c6)／
  `CUSW`(c11)／`Atlantis`(c16)／`Compact`(c21)／**`Atlantis High`(c26)**／
  `Comments`(c31)；`Atlantis High` 之 r3 欄名為
  `Signal Name`／`CAN`／`Format`／`SNA`／`VFs`。
  另 `Proxi & Configuration` 449 列 × 31 欄、`Rev History` 108 列，
  及 10 個車型專屬訊號分頁（3–35 列不等）
- **(c) 版次**：`v1_78`（檔名所載）
- **(d) 已知不涵蓋**：LID 之左欄為 Logical Identifier，**不是 CAN 訊號名**。
  以 LID 名直接查 DBC 必然 0 命中（例 `ICSPowerButton` → 實際 CAN 名為
  `CLIMATIC_PANEL.Radio_btn0`／`DIS_CENTERSTACK.DCSD_Power`）。
  一列可載多個 `MESSAGE.Signal`，本檔不指定何者適用
- **(e) 取代關係**：`features/vehicle_setting/inputs/` 之
  `…v1_76.xlsx` 為較舊版次。**兩版差異本輪未測**；依既有慣例
  （同 R-G1），vehicle_setting 之已交付件不因新版而改
- **(f) 首個採用**：`display`，2026-08-24（R-DM17 之三段解析鏈）

### `PROXI_HDCC27_R3_20250424.xlsx`

- **(a)** SHA256 `e7c2020f01c3d58db431babe7f8a41acbe528c451bd37ef6bb84f1b312be6ff2`
  · 743,785 bytes · mtime 2026-08-24T20:00:27
- **(b) 涵蓋範圍**：13 個分頁。`Format` 1,060 列 × 24 欄（參數主表）、
  `Country Code` 224 列、`Revision Notes` 483 非空列、
  `EPS_Configuration_Families` 50 列、`ANC Table` 23 列、
  `Projection Mode Selection` 11 非空列、`Additional Languages` 10 列、
  `Acoustic Configuration` 12 列、`Allowed Conditions` 6 非空列、
  `Checks` 9 非空列、`Help` 16 列、`Cover` 10 非空列、`Header` 4 非空列
- **(c) 版次**：`R3`，日期碼 `20250424`（檔名所載）
- **(d) 已知不涵蓋**：本輪**未解析其內容**（下放包 04 步驟 11：與本
  feature 之關聯尚未確立，逕行解析屬無據之工）。故其參數與 Display
  之關聯**未知**，不得以本條目為據主張任何 PROXI 參數存在或不存在
- **(e) 取代關係**：`features/vehicle_setting/` 另有其自用之 PROXI 取值
  （`data/_vf230_proxi_values.json`），來源檔非本檔，兩者關係未測
- **(f) 首個採用**：**尚無**。本輪僅登台帳
```

---

## 3. `LOOKUP_MISSES.md` 全文（步驟 3、6）

```markdown
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
```

**未留空表**：本輪有兩筆真查無（M-1、M-2），且已附查詢範圍聲明。
兩筆皆滿足 R-G13 三要件 —— 特別是第 (3) 項：`RADIO_B4` 與 `GW_B_5`
兩個訊息**本身都存在於 BHCAN2-R1**，故該匯流排本應含之，查無成立。

---

## 4. DBC 獨立重算（步驟 4）

### 4.1 量測條件（自行宣告）

- 編碼：四本 DBC **皆非合法 UTF-8**，以 **cp1252** 解讀
- 行尾：CRLF 為主，**每本都夾雜少量裸 LF**（見下表）。以
  `str.splitlines()` 切行，兩種皆視為斷行；裸 LF 數一併列出，
  使讀者看見檔案並不一致
- 訊號定義列：`lstrip()` 以 `SG_ ` 起始之行，**計「列」不計相異名**
  （同一名可在多個訊息中定義）
- 訊息列：行首 `BO_ `
- 發送節點：`BO_` 行之最後一個空白分隔欄位
- 接收節點：`SG_` 行末之節點清單（下放包 §3.2 未列，本輪補測）
- 全程無任何相似度比對

### 4.2 輸出

```
# DBC recount — measurement conditions
encoding=cp1252 (files are not valid UTF-8) | split=str.splitlines()
signal def line = lstrip() startswith 'SG_ ' (counted as LINES)
message line = 'BO_ ' at col 0 | tx node = last field of BO_ line

| 檔 | bytes | CRLF | bare LF | 訊號定義列 | 相異訊號名 | 訊息 |
|---|---|---|---|---|---|---|
| BHCAN2-R1 | 167226 | 3359 | 8 | 344 | 342 | 63 |
| FDCAN8-R1 | 1106532 | 19805 | 2 | 1916 | 1634 | 318 |
| BHCAN-R4 | 442200 | 8576 | 14 | 914 | 883 | 155 |
| FDCAN8-R5 | 1177931 | 20969 | 2 | 2037 | 1755 | 323 |

## BHCAN2-R1 vs BHCAN-R4 —— 訊號名集合三分（相異名，逐字）
  兩者皆有      : 310
  僅 BHCAN-R4 有: 573
  僅 BHCAN2-R1 有: 32
  僅 BHCAN2 有者全列（32）: ['CameraDisplaySts', 'D_RQ_TGW', 'D_RS_TGW', 'FPDM_DISP_STAT', 'FPDM_RQ_DISP_INTS', 'HFPSts', 'Minute1_TLM', 'Minute2_TLM', 'Month1_TLM', 'Month2_TLM', 'Radio_Delete_Request', 'Radio_Profile_Request', 'STIM_Trailer_Info', 'TGW_FPDM_DISP_STATSts', 'TPMLearnHornChirp', 'TrailerDisplayView', 'TrailerHeight_STIM', 'TrailerHeight_TLM', 'TrailerImageDefeatRQSts', 'TrailerLength_STIM', 'TrailerLength_TLM', 'TrailerMoreCamRQSts', 'TrailerType_STIM', 'TrailerType_TLM', 'TrailerViewReq', 'TrailerWidth_STIM', 'TrailerWidth_TLM', 'VRSts', 'Year1_TLM', 'Year2_TLM', 'Year3_TLM', 'Year4_TLM']

## 顯示相關訊號之逐檔定位（訊息 id／發送節點／位元定義／VAL_）

### DCSD_DISP_STAT
  BHCAN2-R1: BO_ 1445 DIS_CENTERSTACK | tx=SGW
      SG_ DCSD_DISP_STAT : 7|3@0+ (1,0) [0|6] "" ETM,LTM
      VAL_ 0 "OFF" 1 "ON" 2 "BLANK" 3 "RR_CMRA" 4 "DISP_HOT" 7 "SNA";
  FDCAN8-R1: 0 命中
  BHCAN-R4: BO_ 1445 DIS_CENTERSTACK | tx=DCSD
      SG_ DCSD_DISP_STAT : 7|3@0+ (1,0) [0|6] "" SGW
      VAL_ 0 "OFF" 1 "ON" 2 "BLANK" 3 "RR_CMRA" 4 "DISP_HOT" 7 "SNA";
  FDCAN8-R5: 0 命中

### RQ_DISP_INTS
  BHCAN2-R1: BO_ 1283 RADIO_B3 | tx=ETM
      SG_ RQ_DISP_INTS : 55|8@0+ (0.5,0) [0|100] "%" SGW
      VAL_ 255 "SNA";
  FDCAN8-R1: 0 命中
  BHCAN-R4: BO_ 1283 RADIO_B3 | tx=SGW
      SG_ RQ_DISP_INTS : 55|8@0+ (0.5,0) [0|100] "%" DCSD
      VAL_ 255 "SNA";
  FDCAN8-R5: 0 命中

### TGW_DISP_STATSts
  BHCAN2-R1: BO_ 1500 TELEMATIC_DISPLAY2 | tx=ETM
      SG_ TGW_DISP_STATSts : 0|4@0+ (1,0) [0|14] "" SGW
      VAL_ 0 "Display_off" 1 "Display_closed" 2 "Normal_mode" 3 "DVD_menu" 4 "DVD_Setup" 5 "DVD_display" 6 "Mode_select_display" 7 "Rear_Camera_Display" 8 "On_blanked_screen" 9 "Splashscreen_Display" 10 "Rear Entertainment HMI" 11 "Rear Entertainment Full Screen Video " 12 "DTV Program Display" 13 "DTV fullscreen Video Display" 14 "DTV Camera Video Display" 15 "SNA";
  FDCAN8-R1: BO_ 1427 TELEMATIC_FD_4 | tx=ETM
      SG_ TGW_DISP_STATSts : 79|4@0+ (1,0) [0|14] "" Vector__XXX
      VAL_ 0 "Display_off" 1 "Display_closed" 2 "Normal_mode" 3 "DVD_menu" 4 "DVD_Setup" 5 "DVD_display" 6 "Mode_select_display" 7 "Rear_Camera_Display" 8 "On_blanked_screen" 9 "Splashscreen_Display" 10 "Rear Entertainment HMI" 11 "Rear Entertainment Full Screen Video " 12 "DTV Program Display" 13 "DTV fullscreen Video Display" 14 "DTV Camera Video Display" 15 "SNA";
  BHCAN-R4: BO_ 1500 TELEMATIC_DISPLAY2 | tx=SGW
      SG_ TGW_DISP_STATSts : 0|4@0+ (1,0) [0|14] "" DCSD
      VAL_ 0 "Display_off" 1 "Display_closed" 2 "Normal_mode" 3 "DVD_menu" 4 "DVD_Setup" 5 "DVD_display" 6 "Mode_select_display" 7 "Rear_Camera_Display" 8 "On_blanked_screen" 9 "Splashscreen_Display" 10 "Rear Entertainment HMI" 11 "Rear Entertainment Full Screen Video " 12 "DTV Program Display" 13 "DTV fullscreen Video Display" 14 "DTV Camera Video Display" 15 "SNA";
  FDCAN8-R5: BO_ 1427 TELEMATIC_FD_4 | tx=ETM
      SG_ TGW_DISP_STATSts : 79|4@0+ (1,0) [0|14] "" Vector__XXX
      VAL_ 0 "Display_off" 1 "Display_closed" 2 "Normal_mode" 3 "DVD_menu" 4 "DVD_Setup" 5 "DVD_display" 6 "Mode_select_display" 7 "Rear_Camera_Display" 8 "On_blanked_screen" 9 "Splashscreen_Display" 10 "Rear Entertainment HMI" 11 "Rear Entertainment Full Screen Video " 12 "DTV Program Display" 13 "DTV fullscreen Video Display" 14 "DTV Camera Video Display" 15 "SNA";

### CM_TCH_STAT
  BHCAN2-R1: 0 命中
  FDCAN8-R1: BO_ 1428 TELEMATIC_FD_5 | tx=ETM
      SG_ CM_TCH_STAT : 74|3@0+ (1,0) [0|6] "" SGW
      VAL_ 0 "TCH_NOT_PSD" 1 "TCH_PSD" 2 "TCH_PS_CAN" 3 "Not_Used" 4 "TCH_CFG_RES" 5 "TCH_CFG_OFFSET" 6 "TCH_CFG_MAX" 7 "SNA";
  BHCAN-R4: BO_ 1498 CM_CTRL | tx=BCM
      SG_ CM_TCH_STAT : 2|3@0+ (1,0) [0|6] "" SGW
      VAL_ 0 "TCH_NOT_PSD" 1 "TCH_PSD" 2 "TCH_PS_CAN" 3 "Not_Used" 4 "TCH_CFG_RES" 5 "TCH_CFG_OFFSET" 6 "TCH_CFG_MAX" 7 "SNA";
  FDCAN8-R5: BO_ 1428 TELEMATIC_FD_5 | tx=ETM
      SG_ CM_TCH_STAT : 74|3@0+ (1,0) [0|6] "" SGW
      VAL_ 0 "TCH_NOT_PSD" 1 "TCH_PSD" 2 "TCH_PS_CAN" 3 "Not_Used" 4 "TCH_CFG_RES" 5 "TCH_CFG_OFFSET" 6 "TCH_CFG_MAX" 7 "SNA";

## §3.1 所列之四個「僅 BHCAN2 有」顯示訊號 —— 逐一複驗

### FPDM_DISP_STAT  (在 BHCAN-R4: 無)
  BO_ 1513 FPDM1 | tx=FPDM
  SG_ FPDM_DISP_STAT : 2|3@0+ (1,0) [0|3] "" ETM
  VAL_ 0 "OFF" 1 "ON" 2 "BLANK" 3 "DISP_HOT" 7 "SNA";

### TGW_FPDM_DISP_STATSts  (在 BHCAN-R4: 無)
  BO_ 1282 RADIO_B2 | tx=ETM
  SG_ TGW_FPDM_DISP_STATSts : 50|3@0+ (1,0) [0|3] "" FPDM
  VAL_ 0 "OFF" 1 "ON" 2 "BLANK" 3 "DISP_HOT" 7 "SNA";

### FPDM_RQ_DISP_INTS  (在 BHCAN-R4: 無)
  BO_ 1282 RADIO_B2 | tx=ETM
  SG_ FPDM_RQ_DISP_INTS : 63|8@0+ (0.5,0) [0|100] "%" FPDM
  VAL_ 255 "SNA";

### CameraDisplaySts  (在 BHCAN-R4: 無)
  BO_ 1283 RADIO_B3 | tx=ETM
  SG_ CameraDisplaySts : 59|3@0+ (1,0) [0|0] "" Vector__XXX
  VAL_ 0 "Default" 1 "View_1" 2 "View_2" 3 "View_3" 4 "View_4" 5 "View_5" 6 "View_6" 7 "View_7";
```

### 4.3 與下放包 §3.1／§3.2 之對照

| 項 | 下放包 | 本輪實測 | 判定 |
|---|---|---|---|
| BHCAN2-R1 訊號定義列／訊息 | 344／63 | 344／63 | 相符 |
| FDCAN8-R1 | 1,916／318 | 1,916／318 | 相符 |
| BHCAN-R4 | 914／155 | 914／155 | 相符 |
| FDCAN8-R5 | 2,037／323 | 2,037／323 | 相符 |
| bytes 四本 | 167,226／1,106,532／442,200／1,177,931 | 同 | 相符 |
| 訊號名三分 | 310／573／32 | 310／573／32 | 相符 |
| 三訊號之 tx 差異 | SGW↔DCSD、ETM↔SGW、ETM↔SGW | 同 | 相符 |
| 位元定義與 `VAL_` 兩本逐字相同 | 是 | 是 | 相符 |
| `CM_TCH_STAT` 於 BHCAN2 為 0 | 是，且非缺漏 | 是 | 相符 |
| 四個 FPDM 訊號僅 BHCAN2 有 | 是 | 是（32 個「僅新有」之全列已列出） | 相符 |

**新查明者（下放包未列）**：

1. **rx 節點亦隨 tx 對調。** `DCSD_DISP_STAT` 在 BHCAN2 為
   tx=`SGW`／rx=`ETM,LTM`，在 BHCAN-R4 為 tx=`DCSD`／rx=`SGW`；
   `RQ_DISP_INTS`、`TGW_DISP_STATSts` 同樣方向一致地對調。
   下放包只列 tx，而 **rx 決定 TC 該在哪個節點觀察**，同等重要。
2. `TGW_DISP_STATSts` 之 `VAL_` 有 16 個列舉，其中
   `9 "Splashscreen_Display"` 與 `7 "Rear_Camera_Display"` 分別對應
   SWE-DM-003（Splash）與 SWE-DM-007／008（RVC）之主題。
   **僅記，不作為對應之依據** —— 那需要另立錨（R-DM13）。
3. `CM_TCH_STAT` 在 BHCAN-R4 位於 `BO_ 1498 CM_CTRL`（tx=BCM），
   在 FDCAN8 兩版皆位於 `BO_ 1428 TELEMATIC_FD_5`（tx=ETM）。
   **同一訊號在新舊架構下換了訊息與匯流排**，非僅換節點。

---

## 5. `signal_resolution.tsv` 與 resolved 比率（步驟 5）

### 5.1 量測條件

- LID：`openpyxl`、`read_only=True`、`data_only=True`；分頁 `CAN Mapping`；
  r1 標題／r2 架構分組／r3 欄名／資料自 r4 起 **2,624 列**
- 架構欄組固定取 **Atlantis High**（c26–c30，沿用 R-VS67）
- 進 LID 之比對為 **`Logical Identifier` 欄之逐字相等**（空白正規化後）；
  無大小寫折疊、無前綴比對、無相似度
- 多值 `Signal Name` 儲存格以**換行**切分，**逐值一列**輸出，不合併不擇一
- 進 DBC 之比對：**先以 `MESSAGE.Signal` 兩半皆相等**選定 DBC；
  兩半皆相等者不存在時，才退為訊號名單獨命中，並在 `note` 明記訊息名不符
- `resolved = Y` 僅在「LID 解出 CAN 名」且「DBC 有該 `SG_`」時成立；
  其餘一律 `N`，**不猜**（停止條件 12）

```
# R-DM17 signal resolution
LID: Logical Identifiers and CAN Mapping v1_78.xlsx
CAN Mapping dims: 2627 rows x 35 cols; data rows r4-r2627 = 2624
architecture groups (r2): {'LID Information': 1, 'Powernet': 6, 'CUSW': 11, 'Atlantis': 16, 'Compact': 21, 'Atlantis High': 26, 'Comments': 31}
Atlantis High group starts at c26; its r3 labels: ['Signal Name', 'CAN', 'Format', 'SNA', 'VFs']

SYS2 $Signal$ tokens in the FR population: 15
  ['Back_Button', 'CCDMF_RQ_DISP_INTS', 'CM_TCH_STAT', 'DCSD_DISP_STAT', 'Enter_Button', 'ICSMuteButton', 'ICSPowerButton', 'ICSScreenOffButton', 'ICS_KNOB1_DIR', 'ICS_KNOB1_VAL', 'ICS_KNOB2_DIR', 'ICS_KNOB2_VAL', 'RQ_DISP_INTS', 'TGW_DISP_STAT', 'Telematic_Power']

## 統計
  輸出列數（多值逐值一列）: 26
  resolved=Y 列: 24 / resolved=N 列: 2
  15 個 $Signal$ 中，至少解得一列者: 14/15
  完全未解者: ['CCDMF_RQ_DISP_INTS']

wrote /Users/peihe/Work_Projects/TC_Generator/features/display/data/signal_resolution.tsv

| sys2_signal | lid_row | atl_high_signal_name | can | dbc_file | dbc_msg_id | resolved | note |
|---|---|---|---|---|---|---|---|
| Back_Button | 131 | CLIMATIC_PANEL.Radio_btn3 | CAN-B | BHCAN2-R1 | 1050 CLIMATIC_PANEL tx=SGW | Y |  |
| CCDMF_RQ_DISP_INTS | 255 | RADIO_B4.CCDMF_RQ_DISP_INTS | CAN-B |  |  | N | LID 解得 CAN 訊號名，但兩本 DBC（BHCAN2-R1／FDCAN8-R1）皆無此 SG_；R-G13(3)：訊息 RADIO_B4 於 BHCAN2-R1 存在 |
| CM_TCH_STAT | 368 | TELEMATIC_FD_5.CM_TCH_STAT | FD | FDCAN8-R1 | 1428 TELEMATIC_FD_5 tx=ETM | Y |  |
| DCSD_DISP_STAT | 420 | DIS_CENTERSTACK.DCSD_DISP_STAT | B-CAN | BHCAN2-R1 | 1445 DIS_CENTERSTACK tx=SGW | Y |  |
| Enter_Button | 666 | CLIMATIC_PANEL.Radio_btn1 | CAN-B | BHCAN2-R1 | 1050 CLIMATIC_PANEL tx=SGW | Y |  |
| Enter_Button | 666 | DIS_CENTERSTACK.DCSD_Enter | CAN-B | BHCAN2-R1 | 1445 DIS_CENTERSTACK tx=SGW | Y |  |
| ICSMuteButton | 1038 | CLIMATIC_PANEL.Radio_btn4 | CAN-B | BHCAN2-R1 | 1050 CLIMATIC_PANEL tx=SGW | Y |  |
| ICSMuteButton | 1038 | GW_B_5.Mute_Button | CAN-B |  |  | N | LID 解得 CAN 訊號名，但兩本 DBC（BHCAN2-R1／FDCAN8-R1）皆無此 SG_；R-G13(3)：訊息 GW_B_5 於 BHCAN2-R1 存在 |
| ICSMuteButton | 1038 | DIS_CENTERSTACK.DCSD_Mute | CAN-B | BHCAN2-R1 | 1445 DIS_CENTERSTACK tx=SGW | Y |  |
| ICSPowerButton | 1039 | CLIMATIC_PANEL.Radio_btn0 | CAN-B | BHCAN2-R1 | 1050 CLIMATIC_PANEL tx=SGW | Y |  |
| ICSPowerButton | 1039 | DIS_CENTERSTACK.DCSD_Power | CAN-B | BHCAN2-R1 | 1445 DIS_CENTERSTACK tx=SGW | Y |  |
| ICSScreenOffButton | 1044 | CLIMATIC_PANEL.Radio_btn2 | CAN-B | BHCAN2-R1 | 1050 CLIMATIC_PANEL tx=SGW | Y |  |
| ICSScreenOffButton | 1044 | DIS_CENTERSTACK.DCSD_Screen_Off | CAN-B | BHCAN2-R1 | 1445 DIS_CENTERSTACK tx=SGW | Y |  |
| ICS_KNOB1_DIR | 1024 | CLIMATIC_PANEL.Radio_Knob1_DIR | CAN-B | BHCAN2-R1 | 1050 CLIMATIC_PANEL tx=SGW | Y |  |
| ICS_KNOB1_DIR | 1024 | DIS_CENTERSTACK.DCSD_VOLKNOB_DIR | CAN-B | BHCAN2-R1 | 1445 DIS_CENTERSTACK tx=SGW | Y |  |
| ICS_KNOB1_VAL | 1025 | CLIMATIC_PANEL.Radio_Knob1_VAL | CAN-B | BHCAN2-R1 | 1050 CLIMATIC_PANEL tx=SGW | Y |  |
| ICS_KNOB1_VAL | 1025 | DIS_CENTERSTACK.DCSD_VOLKNOB_VAL | CAN-B | BHCAN2-R1 | 1445 DIS_CENTERSTACK tx=SGW | Y |  |
| ICS_KNOB2_DIR | 1026 | CLIMATIC_PANEL.Radio_Knob2_DIR | CAN-B | BHCAN2-R1 | 1050 CLIMATIC_PANEL tx=SGW | Y |  |
| ICS_KNOB2_DIR | 1026 | DIS_CENTERSTACK.DCSD_TUNEKNOB_DIR | CAN-B | BHCAN2-R1 | 1445 DIS_CENTERSTACK tx=SGW | Y |  |
| ICS_KNOB2_VAL | 1027 | CLIMATIC_PANEL.Radio_Knob2_VAL | CAN-B | BHCAN2-R1 | 1050 CLIMATIC_PANEL tx=SGW | Y |  |
| ICS_KNOB2_VAL | 1027 | DIS_CENTERSTACK.DCSD_TUNEKNOB_VAL | CAN-B | BHCAN2-R1 | 1445 DIS_CENTERSTACK tx=SGW | Y |  |
| RQ_DISP_INTS | 1626 | RADIO_B3.RQ_DISP_INTS | B-CAN | BHCAN2-R1 | 1283 RADIO_B3 tx=ETM | Y |  |
| TGW_DISP_STAT | 2084 | TELEMATIC_DISPLAY2.TGW_DISP_STATSts | CAN-B CAN-FD | BHCAN2-R1 | 1500 TELEMATIC_DISPLAY2 tx=ETM | Y |  |
| TGW_DISP_STAT | 2084 | TELEMATIC_FD_4.TGW_DISP_STATSts | CAN-B CAN-FD | FDCAN8-R1 | 1427 TELEMATIC_FD_4 tx=ETM | Y |  |
| Telematic_Power | 2069 | TELEMATIC_FD_4.PowerSts_Telematic | CAN_FD CAN-BH | FDCAN8-R1 | 1427 TELEMATIC_FD_4 tx=ETM | Y |  |
| Telematic_Power | 2069 | STATUS_TELEMATIC.PowerSts_Telematic | CAN_FD CAN-BH | BHCAN2-R1 | 1470 STATUS_TELEMATIC tx=ETM | Y |  |
```

### 5.2 resolved 比率與對下放包 §3.4 之限定

| 項 | 實測 |
|---|---|
| FR 母體之 `$Signal$` | 15 |
| 於 LID `Logical Identifier` 欄逐字查得 | **15 / 15** |
| 解出之 `MESSAGE.Signal` 值（逐值一列） | 26 |
| `resolved = Y` | **24 / 26** |
| `resolved = N` | 2 / 26 |
| 至少解得一列之 `$Signal$` | **14 / 15** |

下放包 §3.4 記「SYS2 之 15 個 `$Signal$` **全數解得**」。
**該陳述在 LID 階段成立，在 DBC 階段不成立。** R-DM17 之解析鏈有三段，
「解得」須指明止於哪一段：

- 止於 LID：15/15
- 止於 DBC：14/15（`CCDMF_RQ_DISP_INTS` 之 CAN 名
  `RADIO_B4.CCDMF_RQ_DISP_INTS` 在兩本 DBC 皆無此 `SG_`，
  而訊息 `RADIO_B4` 本身存在 → R-G13 三要件齊備之真查無）

停止條件 12（連續 3 筆以上需猜則停）**未觸發**：`N` 只有 2 筆，
且兩筆都是明確的「查無」而非「猜不出」，無任何一筆以推定填入。

### 5.3 一處實作缺陷之自我更正

首版腳本以 DBC 字典順序取「首個含該訊號名者」，導致
`TELEMATIC_FD_4.TGW_DISP_STATSts` 被接到 BHCAN2 之
`TELEMATIC_DISPLAY2`（訊號名對、訊息名不對），`Telematic_Power` 同樣。
已改為**兩半皆相等優先**後，該二筆各自正確落在 FDCAN8-R1 之
`BO_ 1427 TELEMATIC_FD_4`。

> 這個缺陷若沒抓到，輸出仍會是 `resolved = Y` 且看起來合理 ——
> 錯的是匯流排，而匯流排決定 TC 在哪裡量。與上一輪 58 之教訓同型：
> **看起來成功的輸出最需要對照其定義。**

---

## 6. `A-DM10` 拆條後全文、`A-DM14`／`A-DM15`／`A-DM16` 新增全文（步驟 7–9）

```markdown
## A-DM10 — SYS2 無指向 CFTS 條號之錨，mode D 之 spec_reference 無 id 橋樑  [**拆條**：a 已 RESOLVED／b 仍 PENDING]

canon §3 之 mode D 要求 spec_reference 為**查得**。實測：

- CFTS 本文可抽出 outline id 184 個相異（其中 182 個可由 Heading 樣式
  取得），故 CFTS 側有可用索引
- SYS2 之 `SYS2 文件識別碼 Document ID` 為逐列遞增之 Polarion 文件 id
  （`SR26_20260310-1533` … `-1778`，另 78 列為 `SR26_20250813-1632`），
  **不是 CFTS 條號**
- SYS2 `Melco ID` 之 99 個 token 在 CFTS 本文中逐字命中者僅 1 個，且該
  token 為 `NA`（非 id）
- 加上 A-DM2（037→SYS2 id 0 命中），自 SWE-DM leaf 走到 CFTS 條號的
  三段鏈路每一段都無 id 橋樑

- 證據：`scripts/probe_spec_mode.py`
- 影響：Phase 4 之 spec_reference 目前只能靠文字比對定位條號
- 提案處置：登記；spec_reference 之取得方式屬 Tier 2

---

### 拆條（2026-08-24，下放包 04 §3.4／步驟 7）

以上原文依 R-TM13 保留，不刪除、不改寫。本條實含兩件事，分列處置：

#### A-DM10a — 訊號側之 id 橋樑　**[RESOLVED]**

原條所述「SYS2 之 `$Signal$` 無法接到任何外部定義」一節**已解**。
橋樑為 LID `CAN Mapping` 分頁（R-DM17 之三段解析鏈）。

執行層獨立重算（`scripts/signal_resolution.py`，
`data/signal_resolution.tsv`）：

| 項 | 實測 |
|---|---|
| FR 母體之 `$Signal$` | 15 |
| 於 LID `Logical Identifier` 欄逐字查得者 | **15 / 15** |
| 解出之 `MESSAGE.Signal` 值（多值逐值一列） | 26 |
| 其中於 DBC 查得 `SG_` 者 | **24 / 26** |
| 至少解得一列之 `$Signal$` | **14 / 15** |

**惟下放包 04 §3.4 之「15 個 `$Signal$` 全數解得」須加限定**：該陳述在
**LID 階段**成立（15/15），在 **DBC 階段**不成立 ——
`CCDMF_RQ_DISP_INTS` 之 CAN 名 `RADIO_B4.CCDMF_RQ_DISP_INTS` 在兩本 DBC
皆無此 `SG_`，而訊息 `RADIO_B4` 本身存在於 BHCAN2-R1，故屬 R-G13 三要件
齊備之真查無（`forms/LOOKUP_MISSES.md` M-1、DR-DM5）。

同時撤回之誤讀（依下放包 04 §3.4 第 1、2 點）：
`TGW_DISP_STAT` → `TGW_DISP_STATSts` 之 `Sts` 尾綴**不是規格錯誤**，
`ICS*` 系列在 DBC 0 命中**不是缺漏** —— 二者皆為「以 LID 名查 CAN 名」
之必然結果。

#### A-DM10b — 章節側之 id 橋樑　**[PENDING]**

SWE-DM leaf → CFTS 條號之橋樑**仍不存在**。本輪未有任何進展：
CFTS 側之 184 個 outline id 與 037 之 8 個 leaf 之間，沒有任何逐字錨。
spec_reference 之取得方式仍為 Tier 2 未決，`feature.yaml` 之
`spec_reference_template` 維持 `null`。

## A-DM14 — BHCAN2 與 BHCAN-R4 為不同資料庫，且顯示訊號之收發節點相反  [PENDING]

`forms/PDT27_E2A_R1_BHCAN2.dbc`（`46cb73f3…`）與
`features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc` 之訊號名集合
三分（相異名，逐字，`scripts/dbc_probe.py`）：

| | 數 |
|---|---|
| 兩者皆有 | 310 |
| 僅 BHCAN-R4 有 | **573** |
| 僅 BHCAN2-R1 有 | 32 |

**故二者非版次關係，是不同的資料庫。** 573 個只在舊檔存在之訊號名，其在
新架構下之地位（移除／改名／移至他匯流排）本輪不推定。

三個顯示訊號之位元定義與 `VAL_` 列舉**兩本逐字相同**，但**節點相反**：

| 訊號 | 訊息 | BHCAN2-R1 | BHCAN-R4 |
|---|---|---|---|
| `DCSD_DISP_STAT` | `BO_ 1445 DIS_CENTERSTACK` | tx=**SGW**，rx=`ETM,LTM` | tx=**DCSD**，rx=`SGW` |
| `RQ_DISP_INTS` | `BO_ 1283 RADIO_B3` | tx=**ETM**，rx=`SGW` | tx=**SGW**，rx=`DCSD` |
| `TGW_DISP_STATSts` | `BO_ 1500 TELEMATIC_DISPLAY2` | tx=**ETM**，rx=`SGW` | tx=**SGW**，rx=`DCSD` |

> 下放包 04 §3.2 只列 tx。本輪一併實測 rx（`SG_` 行末之接收節點清單），
> **rx 亦隨之改變**，方向與 tx 一致地對調。

**發送節點決定 TC 該寫「送出」還是「觀察」**，故此差異非中繼資料。

- 提案處置：登記。**何者適用於本專案未裁定** —— 二選一需要專案之
  EE 架構配置為據，不在手上四份素材內

## A-DM15 — BHCAN2 含四個 FPDM 顯示訊號，而 037 與 SYS2 皆未提及 FPDM  [PENDING]

「僅 BHCAN2 有」之 32 個訊號名中，四個與顯示直接相關（逐字複驗，
`scripts/dbc_probe.py`）：

| 訊號 | 訊息 | tx | rx | VAL_ / 格式 |
|---|---|---|---|---|
| `FPDM_DISP_STAT` | `BO_ 1513 FPDM1` | FPDM | ETM | `0 OFF 1 ON 2 BLANK 3 DISP_HOT 7 SNA` |
| `TGW_FPDM_DISP_STATSts` | `BO_ 1282 RADIO_B2` | ETM | FPDM | 同上五值 |
| `FPDM_RQ_DISP_INTS` | `BO_ 1282 RADIO_B2` | ETM | FPDM | `63\|8@0+ (0.5,0) [0\|100] "%"`，`255 SNA` |
| `CameraDisplaySts` | `BO_ 1283 RADIO_B3` | ETM | Vector__XXX | `0 Default 1 View_1 … 7 View_7` |

`FPDM_*` 為 `DCSD_*` 之平行族：值域 `OFF/ON/BLANK/DISP_HOT/SNA` 與
`DCSD_DISP_STAT` 相同（惟 `DCSD_DISP_STAT` 另有 `3 RR_CMRA`，FPDM 族無），
`FPDM_RQ_DISP_INTS` 之格式與 `RQ_DISP_INTS` 逐字相同（`0.5 %/bit`、
`0–100`、`255 SNA`）。四者在 BHCAN-R4 皆不存在。

**037 與 SYS2 皆未提及 FPDM**（兩檔全文逐字查 `FPDM` 為 0）。
這是新素材帶進來的問題，不是既有缺漏。

- 提案處置：登記。**不推定其是否在本 feature 範圍內** —— 若 FPDM 為
  本專案之另一顯示裝置，則 8 個 leaf 之涵蓋面須重議；若非本專案配備，
  則其存在於 DBC 中不生影響。二者皆需專案配置為據

## A-DM16 — LID `Proxi & Configuration` 分頁含顯示相關組態旗標  [PENDING]

下放包 04 步驟 11 之停手觸發條件為「LID `Proxi & Configuration` 分頁與
本 feature 之**訊號**有關聯」。逐字測試：15 個 SYS2 `$Signal$` 在該分頁
**0 命中**，故該條件**未逐字成立**，本輪未停手、未解析 PROXI。

惟以關鍵字（`DISP`／`DCSD`／`RVC`／`Camera`／`Display`）掃描該 449 列分頁，
命中 23 列，其中四列與 Display 之 leaf 明顯相鄰：

| LID 列 | Logical Identifier | Function |
|---|---|---|
| r51 | `DCSD_cfg` | DCSD Present |
| r64 | `DSP_SK_PRSNT` | Display off soft key present |
| r131 | `NetCfg_DCSD` | （無 Function 文字） |
| r170 | `RVC_SK_PRSNT` | Rear Camera soft key present |

`DSP_SK_PRSNT` 對應 SWE-DM-001 之 Screen Off 行為、`RVC_SK_PRSNT` 對應
SWE-DM-007／008 之 RVC 行為、`DCSD_cfg` 決定 DCSD 是否存在 —— 形態上像是
TC 之**前置條件**來源。

- 證據：LID `Proxi & Configuration` 449 列 × 31 欄之逐列 regex 掃描
- **本輪未做任何 PROXI 解析**（步驟 11 明文禁止無據之工），僅登記相鄰性
- 提案處置：請裁示步驟 11 之觸發是否應由「與訊號有關聯」放寬為
  「與 leaf 之前置條件有關聯」。若是，則 PROXI 解析應排入下一輪；
  若否，本條轉為記錄性條目



## A-DM11 — R-DM7 覆蓋落差（**2026-08-24 更正；原結論撤回**）  [PENDING]

### 撤回之內容

本條原載「以 bag-of-words token 重疊為依據，80 列母體中 58 列無對應，
`SWE-DM-004`／`005`／`007` 命中 0 列」。**該結論撤回。**

撤回理由（下放包 03 §3.1，分析層以關鍵字直查 SYS2 `Description` 發現）：
SYS2 r30 之 Heading 為 `Multi-stage' DCSD Display Hot Algorithm`，其子列
r31–r34 為 Display Hot 之狀態機需求，與 `SWE-DM-004`／`005` 之
Requirement Title 所稱之 `Hot Algorithm` **逐字同名**。而原啟發式將
r31／r32 判給 `SWE-DM-001`、r34 判給 `SWE-DM-003`、r33 判為「無」——
**同時產生偽陽性與偽陰性，且兩者互為因果**：列被錯配到相鄰 leaf，
被搶走的 leaf 於是顯示 0。

原方法之產物依 R-TM13 保留於
`data/coverage_sys2_vs_swe_dm.RETRACTED.tsv`（檔頭已加註廢止），不刪除、
不再引用。方法本身由 **R-DM13 廢止**。

> 致誤之方法為下放包 01 R-DM7 所指定（「Description 文字」列為三種依據
> 之一），分析層已於下放包 03 §4.2 自陳「方法是我指定的」。執行層之
> 責任在於：上繳 02 §11 第 3 項雖自陳其為啟發式，**低估了嚴重性** ——
> 只說了精度不足，未察覺它會把結論指向相反方向。

### 更正後之陳述（錨定法，R-DM13）

母體不變：SYS2 `Category` 正規化為 `functional requirement` 之 **80 列**。
錨一律逐字，無錨即記無錨（`scripts/coverage_map.py`，全表見
`data/coverage_sys2_vs_swe_dm.tsv`）：

| anchor_kind（最高優先之現存錨） | 列數 |
|---|---|
| signal（`$NAME$`） | 43 |
| value（`[VALUE]`） | 1 |
| heading | 36 |
| melco | 0 |
| none | 0 |

各錨之存在數（非互斥）：含 `$signal$` 43 列、含 `[value]` **54** 列、
有 heading 祖先 80 列、Melco 命中 037 Excluded 1 列（r54）。

> **`[value]` 之數字更正（2026-08-24，R-DM16）**：原記 34 列，係以
> `\[([A-Za-z0-9_%\s]+)\]` 量得。R-DM16 指定之寬式 `\[([^\]]+)\]` 得
> **54 列**。相異 token 數三種定義分別為：`[A-Z0-9_]+` **9**（R-DM14 原引，
> 已由 R-DM16 撤回）、`[A-Za-z0-9_%\s]+` **13**（R-DM16 條文所載之數）、
> `[^\]]+` **44**（R-DM16 條文所指定之 regex）。
> **R-DM16 之 regex 與其數字不一致** —— 44 之多出者為 Polarion 匯出自身之
> metadata（`[State:Approved]`／`[Radio:R1H]`／`[Artifact Type:…]`），
> 非訊號值。本輪依條文之 regex 產出 `values` 欄，同時保留
> `values_narrow` 欄（13-token 定義），兩者並列於
> `data/coverage_sys2_vs_swe_dm.tsv`，**未自行擇一**。

`candidate_leaf`（**候選，非裁定**；依 R-DM12 引用時須連同 `anchor_kind`）：

| leaf | 候選列數 |
|---|---|
| SWE-DM-004（Thermal Management） | 4（r31–r34） |
| SWE-DM-005（Thermal Protection Management） | 4（r31–r34） |
| 其餘六個 leaf | 0 |
| 有候選之列 / 無候選之列 | 4 / 76 |

r31–r34 之候選依據為 heading 錨逐字含 leaf 片語 `'Hot Algorithm'`；該片語
同時出現於 004 與 005 之 Requirement Title，故兩者並列為候選，不擇一。

### 仍站得住之覆蓋陳述

**只有一句**：以 id 為據之對應為 **0 列**（A-DM2，逐字比對）。
「58 列無對應」已撤回；「76 列無候選」為錨定法之輸出，其意義是
**「無逐字錨可連到 leaf」**，不等於「不屬於本 feature 範圍」。

### 錨定法本身之兩項限制（本輪實測，須併同引用）

1. **heading 錨在 r72 退化。** SYS2 之 45 個 Heading 中，`r72
   2.2 Serializer Touch Interrupt PIN Definition` 一個節點底下掛了 231 列，
   其中 **48 列為 FR —— 佔母體 80 列之 60%**。該 heading 之文字與顯示行為
   無關，故對這 48 列而言 heading 錨存在但無鑑別力。
   （另：r62 為 `2.3 LVDS Interface`、r72 為 `2.2 …`，編號逆序，該匯出之
   Heading 層級疑似已被壓平。）
2. **RVC 之縮寫不逐字。** 037 用 `Display RVC Handling`／`RVC Management`
   （`SWE-DM-007`／`008`），SYS2 之 heading 用 `Rear Camera Events`／
   `Rear Camera Interrupts`。`RVC` → `Rear View Camera` 之展開**不是逐字
   比對**，依下放包 03 §七第 10 條不得作為錨，故二 leaf 之候選為 0。
   **這是方法之界線，不是「SYS2 無 RVC 需求」之發現** —— 兩者不可混同。

- 提案處置：本表為 R-DM7 所要求之揭露。範圍之裁定屬 Tier 2（Q2），
  依下放包 03 §4.2 **於本條之限制 1、2 有處置前不提交裁定**

## A-DM12 — 036 母本 B 欄為公式欄，前輪完全未報告  [PENDING]

036 母本 `Test Case Specification 測試用例規範` 分頁之 B 欄（`No.#\n序號`）
為公式欄。本輪以 `data_only=False` 實測 B10–B1411：

- **1402/1402 逐列符合 `=IF(ISBLANK($D{row}),"",ROW()-9)`**，$D 之列號逐列
  遞增且與所在列一致，不符 0 列
- B 欄為該分頁資料列中**唯一**含公式之欄（全 34 欄逐格掃描）
- `data_only=True` 讀 B10 得快取值 `1`，B11 起為 `None` —— 即快取為
  **陳舊值**：D10 目前為空，公式應回傳 `""`，快取卻仍存 `1`

上繳包 02 全文未提及 B 欄之存在與其公式。`workbook_state` 判 `BLANK`
不受影響（canon §2 step 1 之判準為 Test Item／TC ID，非 B 欄），但寫回時
若對 B 欄賦值，將摧毀 1402 列之公式，序號改為死值。

- 證據：本輪之 `data_only=False` 全欄掃描
- 提案處置：依 **R-DM15**，寫回一律不觸碰 B 欄；`feature.yaml` 已補註。
  另註：因快取陳舊，任何以 `data_only=True` 讀 B 欄判斷「該列是否已填」
  之實作會誤判 r10

## A-DM13 — CFTS_020 引用 8 份外部 CFTS 文件，一份未在手上  [PENDING]

判讀基準 CFTS_020 之本文以 `{CFTSnnn-mmm}` 形式引用外部條號。本輪全文
清點：相異外部文件 **8 份**（`CFTS004`／`009`／`010`／`013`／`019`／
`022`／`033`／`044`；另有指向自身之 `CFTS020-*`）。引用次數較高者：
`CFTS019-723`×12、`CFTS009-722`×9、`CFTS033-2111`×7、`CFTS013-629`×6、
`CFTS013-633`×5、`CFTS013-967`×5、`CFTS044-656`×5、`CFTS013-952`×4。

其中兩份已知直接擋住 R-DM8 之缺值：`CFTS009-722`（Splash/Disclaimer
時段，DR-DM1）與 `CFTS013-629`／`-633`／`-952`（Display Hot 演算法本體，
DR-DM4）。其餘六份之影響本輪**未逐一評估**。

- 證據：`scripts/hot_behaviour_join.py` 之併讀輸出；CFTS_020 本文全文
  regex 清點
- 影響：spec_mode D 之判讀基準本身是一份會外指的文件；BLOCKED 之預估
  不能只看手上四份
- 提案處置：登記；DR-DM4 開立。其餘六份之影響待 Phase 2 逐一評估
```

拆條方式之說明（步驟 7 要求擇一並說明）：**採「於原條分段記載」**，
原文完整保留於條首，其下以 `A-DM10a`／`A-DM10b` 兩個子節分列處置。
理由：a 與 b 之證據互相引用（訊號側之解決正是靠 LID，而章節側之未解
恰恰說明 LID 不涵蓋條號），拆成兩條獨立編號會使讀者只讀到一半。

---

## 7. A-DM11 之 `[VALUE]` 數字更正（步驟 10）

原記「含 `[value]` 34 列」，係以 `\[([A-Za-z0-9_%\s]+)\]` 量得。
依 R-DM16 之 regex `\[([^\]]+)\]` 重量得 **54 列**。

三種定義之相異 token 數：**9**（`[A-Z0-9_]+`，R-DM14 原引，R-DM16 撤回）／
**13**（`[A-Za-z0-9_%\s]+`，R-DM16 條文所載之數）／**44**
（`[^\]]+`，R-DM16 條文所指定之 regex）。

`ANOMALIES.md` 之 A-DM11 已改寫並載明三者與其不一致；
`data/coverage_sys2_vs_swe_dm.tsv` 新增 `values_narrow` 欄。
**`candidate_leaf` 與 `anchor_kind` 之分布不受影響**：值錨在優先序中
排第二，而其上位之 signal 錨已覆蓋 43 列，候選仍為 004／005 各 4 列
（r31–r34），76 列無候選。

---

## 8. 「本包是否仍有該驗而未驗者」—— 執行層之獨立判斷

**有，共 8 項。**

1. **PROXI 一格未讀。** 依步驟 11 未解析，但 A-DM16 已顯示
   `DSP_SK_PRSNT`／`RVC_SK_PRSNT`／`DCSD_cfg` 與 leaf 之前置條件相鄰。
   **現在 TC 之前置條件從哪裡來，是完全空的。**
2. **BHCAN2 vs BHCAN-R4 二選一未解，且我無從解。** A-DM14 登記了差異，
   但「本專案用哪一本」需要專案之 EE 架構配置，四份素材裡沒有。
   **在這件事定案前，`signal_resolution.tsv` 的每一列都掛在
   BHCAN2-R1 這個未經確認的前提上。**
3. **FPDM 是否在範圍內未解**（A-DM15）。若在，8 個 leaf 的涵蓋面要重議。
4. **LID v1.78 vs v1.76 之差異未測。** 下放包 §3.5 明記未測，本輪亦未測。
   vehicle_setting 用 1.76、display 用 1.78，兩者若對同一 LID 給不同的
   CAN 名，跨 feature 的一致性就斷了 —— **沒有任何條文在追這件事**。
5. **FDCAN8-R1 vs R5 之差異未測**（訊號定義列 1,916 vs 2,037，差 121 列）。
   本輪只在 FORMS.md 記其存在。
6. **037 之 `Requirement Description` 全文仍未逐條精讀**（01、03 兩輪皆
   未清）。
7. **SYS2 之 `Polarion`／`_polarion` 兩分頁仍未看**（01、03 兩輪皆未清）。
8. **`recon.py` 仍未跑通**（A-DM8，Q5 未裁）。本 feature 至今全部量測
   出自本輪與前輪自寫之八支腳本，**無一項經 repo 既有管線複核**。

另記本輪**已驗而下放包未要求**者：三個顯示訊號之 rx 節點；
`CM_TCH_STAT` 在新舊架構下換了訊息與匯流排；`TGW_DISP_STATSts` 之 16 個
`VAL_` 列舉；LID `Proxi & Configuration` 之 23 列關鍵字命中；
`.gitignore` 對 `LOOKUP_MISSES.md` 之排除。

---

## 9. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(display): reference store in forms/, three-stage signal resolution

- R-G12/13/14 (global) into docs/fw036/RULINGS_LEDGER.md; R-DM16/17 into
  the feature ledger (5/5 verbatim, 19/19 cumulative)
- FORMS.md: reference-database section, 4 files x 6 mandatory fields,
  coverage measured here rather than copied from the handoff
- forms/LOOKUP_MISSES.md created (R-G14); .gitignore negation added so it
  can be tracked while the DBC/PROXI/LID files stay out
- DBC recount reproduces every handoff figure; rx nodes measured too and
  they flip with tx (A-DM14)
- signal_resolution.tsv: 24/26 rows resolved, 14/15 signals; the handoff's
  "all 15 resolved" holds at the LID stage, not at the DBC stage
- A-DM10 split: signal-side bridge RESOLVED via LID, clause-side PENDING
- A-DM14 (BHCAN2 is a different database), A-DM15 (FPDM signals absent
  from 037/SYS2), A-DM16 (PROXI config flags adjacent to leaves)
- R-DM16's regex and its stated count disagree; both emitted, none picked
```

pathspec：

```
git add .gitignore \
        docs/fw036/RULINGS_LEDGER.md \
        forms/FORMS.md \
        forms/LOOKUP_MISSES.md \
        features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/DATA_REQUESTS.md \
        features/display/scripts/ \
        features/display/data/ \
        features/display/docs/
```

**注意**：本輪首次動到 `features/display/` 以外之檔（`.gitignore`、
`docs/fw036/RULINGS_LEDGER.md`、`forms/`），故 pathspec 不能只帶
feature 目錄。四份參考素材本身不入 git（已逐檔複驗）。
