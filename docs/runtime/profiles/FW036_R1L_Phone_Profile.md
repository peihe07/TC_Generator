# Project Profile — FW036 / R1L SWE1 Phone HMI (Stellantis newR1L)

> **PRECEDENCE: this profile OVERRIDES the generic ASPICE SWE.6 instruction
> wherever the two conflict.** Generic rules stay in force for everything this
> profile does not address. Rules tagged **[OVERRIDE]** replace a specific
> generic rule (the replaced rule is cited); rules tagged **[ADD]** are
> project-specific additions.

> **狀態：骨架（Phase 0–1 產出，下放包 PH-01 §任務 4）。**
> 條文內容待 Phase 3；本檔現階段只固定三件事 —— §0 身分、§1 權威鏈之**缺口**、
> §2 lint 啟用宣告、§5.3 之 PENDING 承接。**空節即空節，不預填。**

## 0. Project identity [ADD]

- Program: Stellantis newR1L；scope `FM-WI-FSM-037-A03-N1L-SWE1-Phone-HMI-V0.1`
- Feature slug: `phone`；author on new rows: `PeiPYHsu`（R-G42@f111d3dc 四）
- **Test Group = `Phone`**（R-PH1，Pei 2026-09-07）
- **TC ID = `NR1L-{ABBR}-{nnn}`；`{ABBR}` 為 `[PEI]`，未定**
  （R-G42 二於本 feature 取不到值，見 `features/phone/DECISIONS.md` §6）
- Requirement IDs: `SWE1-HMI-{nnn}` 與 `SWE1-HMI-{nnn}-{mm}`，自 037 逐字取，
  **不自造、不重編**。`Heading` 157 列之台帳處置沿 `R-POP5` 形態（DECISIONS §3，待簽）。
- workbook_state = **BLANK**；無 done region。Style authority = fallback chain（FO §2.1）。
- 範圍 = **整份 037（911 資料列／754 leaf）**（R-PH2）；不做 Multiphone 子集篩選。

## 1. Requirements authority chain [ADD]

- 鏈：SYS1 Polarion export（Phone HMI Logic and Flow，R1 SR24 Post 2A，June 21 2022）
  → 037 SWRA 分解 → FW036 TC。
- **本節目前有缺口：SYS1 之權威版本未定**（`ANOMALIES.md` A-PH01／`DATA_REQUESTS.md`
  DRAFT-PH-a）。repo 內同檔名兩份匯出之章節號在 `5.17`～`17.5` 錯位一格，
  且**兩份皆非 037 之來源**。裁定前：
  - `feature.yaml` `paths.sys1_export = null`
  - **不得產出任何 `spec_reference`**
  - Phase 2 以後一律不啟動
- 圖面來源：`Phone HMI Logic and Flow R1 SR24 Post 2A (June 21 2022).pdf`
  （Visio 2019，42 頁，有文字層）。
- 26PI 之 `Phone HMI Logic&Flow R1.pdf`（21 頁）之文字層**詞序錯亂**
  （Type 3 Custom 編碼；A-PH02）—— 讀取一律走 `pdfplumber` 之
  `(top, x0)` 重排，**不得用 `pdftotext`**。
- **HFP（CFTS026）不是本 feature 之權威**：其 TC 得作寫法參考，
  其 `spec_reference`（`CFTS026-*`）**不得複製**（R-PH3(a)(d)）。

## 2. Lint 啟用宣告 [ADD]（FO §4 [ADD] 第一項）

- 本 feature 之 lint 一律以 **`--profile phone`** 執行，藉此啟用
  `P`（訊號與參數寫法，**R-G70@c964dfb8 v4.1**；PROXI 採 SWC 式
  `PROXI <Param> = <值>`）與 `X`（導航路徑固定入口檢查，
  **R-G71@72328d57**／IN §5.8，WARN 只報不改）。
- **未加 `--profile` 之全綠不算數**：`P=0`／`X=0` 在未啟用時是沉默，不是核可。

## 3. Design Method [OVERRIDE — restricts IN §12 output strings]

*（待 Phase 3。`下拉選單` 分頁實測 9 個字串，未挑選。）*

## 4. Spec Reference [ADD — clarification, NO override of IN §10.7]

- 形制：`{檔名}_{章節號}`（IN §10.7(b)）。
- `{檔名}` 逐字為 `Phone HMI Logic and Flow R1 SR24 Post 2A (June 21 2022)` ——
  取自 037 `HMI Source ID`（C 欄）之實測前綴，**非 SYS1 之檔名**。
- 037 之 `HMI Source ID` 欄**本身即載完整 `{檔名}_{章節號}`**（213 個相異值），
  故 `spec_reference` 原則上可自 037 直取。
- **但 `{章節號}` 須與所裁定之 SYS1 版本一致方可出簿**（A-PH01）——
  037 引用之 `_5.16.2` 與 `_17.9` 在現有兩份中無一俱全。
  → 本節在 DRAFT-PH-a 未結前**不生效**。

## 5. Fixed entry paths [ADD]（IN §5.3／§5.8）

### 5.3 常數表

| 常數 | 值 | 來源 |
|---|---|---|
| `ENTER_PHONE` | *（待 SYS1 裁定後逐字取；037 `menu bar` 命中 621 列，`Main Category Bar` 之 Phone icon 見 `SWE1-HMI-016`）* | **BLOCKED: DRAFT-PH-a** |
| `ENTER_HOME_SCREEN` | `PENDING: DR-{n} HMI entry path Home Screen` | **承接自 GC-07**（見下） |

### `ENTER_HOME_SCREEN` 之承接（FO §4 [ADD] 第二項）

- 該常數於 `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §5.3 現為 `PENDING`。
  **不複製 PENDING 而不登 DR** —— 本 feature 之承接登記在
  `features/phone/DATA_REQUESTS.md` §2（`DRAFT-PH-c`，未取號）。
- **本 feature 確有標的**：037 `home\s*screen` 命中 7 列
  （`SWE1-HMI-144`、`-144-09`、`SWE1-HMI-199`、`-199-03`、`-199-04`、`-199-05`、
  `SWE1-HMI-204`），第 25 章 Phone Widget 之 setup 以 Home Screen 之 widget 為前提，
  無法只以 Menu Bar 之 `Phone` 入口表達。
- 標記格式依 R-G71(d)：`PENDING: DR-{n} HMI entry path Home Screen`；
  `{n}` 待 Pei 送出時取號（未送出前不佔號）。
- **不阻斷撰寫。**

### 5.8 導航路徑 [ADD]

*（待 Phase 3；`X` 已於 §2 啟用。）*

## 6. Test Set 表（framework Part N）

*（待 Phase 3。第一版切分之候選為 037 之 27 個頂層章，章名逐字須自 SYS1 取
 → **BLOCKED: DRAFT-PH-a**。HFP 之 13 個 Test Set 只作對照，不採用。）*

## 7. Known anomalies register [ADD]

見 `features/phone/ANOMALIES.md`：A-PH01（SYS1 兩版，**阻斷**）、A-PH02（PDF 詞序）、
A-PH03（26PI 日期兩說）、A-PH04（037 機械改寫 704 列）、A-PH05（下放包前提與實測不符）、
A-PH06（Multiphone 子集數不符）、A-PH07（MPA11 與 feature 名方向相反）。
