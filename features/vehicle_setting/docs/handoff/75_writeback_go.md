# 75 下放包 — pilot 通過、R-VS69、PDT24 版本裁定、48 輪（貼回實寫）

分析層寫入，2026-08-23。**三道 gate 全過。本輪進實寫。**

---

## 1. 裁決三項

```
pilot #3＋#4（Pei 2026-08-23：**通過**）
74 包所列之七項 defect 全數修畢，九項放行檢查表逐項通過：
  D-1 67→0／D-4 3→0／D-5 5→0／D-7 10→0／D-2 11 條升為可驗／
  D-3 5 條改最弱斷言（§5.5 違規 0）／D-6 44 條訊號名改寫（殘留 0）
  §9 全母體自檢 **0 項**（69→0）；R-VS54 固定錨點 **20/20 必命中**
分析層另抽驗 `batch16_v4.json` 二條，七項修正逐項落實。

**pilot #1 8 ＋ #2 15 ＋ #3/#4 28 ＝ 51 條經人工關卡（143 條之 36%）。**
未抽樣之 28 條不因本次通過而視為已 review。
```

```
R-VS68′（Pei 2026-08-23，版本裁定）
R-VS68 所授權入庫之 PDT24 兩檔，其版本定為執行層於 47 輪量得者：

  PDT24_E2A_R3_3_BHCAN2_20260109.dbc
      sha256 877e4cbbb60b87860867e77fe7bcbf8555f4298810224681911b1064ea5a95f4
  PDT24_E2A_R8_5_FDCAN8_20260520_CR26320.dbc
      sha256 defc65d0874196401f7d82eb8fa223413ee39af1cfc2a58fbd96922a1faabef5

**非** 71 輪聊天所附之 `…_melco.dbc`／`20240703_…_melmb.dbc`
（二組為不同檔，本裁定取前者）。
其 `evidence-only` 之限制不變：**不得作為訊號名、值域、或 message 歸屬之來源**。
補入後 `INPUTS.sha256` 之 Part 1 為 **18** 檔。

**惟其入庫後須複驗**：71 輪之補充證據段（四份 DBC 中 `*_Cmd_Tlm` 與
`SETUP2` 皆不存在、`*_Tlm` 自 2022 年起為 1 bit）係量自 `_melco`／`_melmb` 二檔，
**本裁定所取者為不同檔** —— 該證據須於本輪以新檔重量，不符者具名。
```

```
R-VS69（分析層裁定 2026-08-23）
`screen_pending = yes` 之判準為 **AH 欄載有畫面層之 BLOCKED 註記**，
與其 ER 是否為 `PENDING` **無關**。

  ER 為 `PENDING`                → 畫面層完全未驗
  ER 為最弱斷言 ＋ AH 有 BLOCKED → 畫面層**部分未驗**
  **二者皆入交付揭露**，`delivery_disclosure.md` 分節：
      §A   單一缺值待補
      §B-1 畫面層完全未驗（ER 為 PENDING）
      §B-2 畫面層部分未驗（已驗其變更，樣式／內容待補）

理由：`screen_pending` 由 26 降為 10，其中 16 條之降係 D-2／D-3 之改寫所致，
**非待補之解除**。以 ER 是否 PENDING 為判準，
會使「已驗變更而未驗樣式」者消失於揭露。
```

```
R-VS35 之補充（分析層裁定 2026-08-23）
升級條件命中而中止其後之作業項時，**登記類 D 項（ANOMALIES.md／
DATA_REQUESTS.md 之寫入）不在中止之列**。

理由：登記是對**已發生之事實**之記載，非待辦之作業；
其隨作業一併停下，會使上繳包之 §5 與登記簿分岔一輪（A-VS146～150 即此）。
```

---

## 2. 48 輪指令 —— **貼回實寫**

```text
你是 FW036 TC 生成管線之執行層。repo: /Users/peihe/Work_Projects/TC_Generator
本輪為 Vehicle Setting 之第 48 輪：**036 母本之實寫**。

## 先讀

  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/66_writeback_procedure.md  貼回程序
  features/vehicle_setting/docs/handoff/75_writeback_go.md         本輪依據

三道 gate **全過**：
  G1 dry-run  ✅ 47 輪（143 列、四項判準合格、四錨點可失敗）
  G2 pilot    ✅ **Pei 2026-08-23 通過**
  G3 母本備份 ✅ 47 輪（母本／備份／W-123 期望值三者 sha256 全等
                 `ebe5a65f30a0d4bcf9e46b51a43145ce222027ac49ad523fe5c2d2b6566a5089`）

## 禁區

- **git 寫入性操作一律不執行。** 需入庫者備指令給 Pei（帶 pathspec）。
- **母本之實寫僅限本輪、僅限 §3 表所列之欄**；列 1–9、其他分頁、
  表外之欄**一格不動**。
- 不補素材（PDT24 兩檔之複製屬 Pei）、不代擬條文、不自行調和數字。
- 各版保留不刪。**不得為使檢查通過而改動判準。**

## 文書

D-1  依 R-VS18 建 docs/upstream/41_writeback.md，六節先留空。
D-2  逐字轉錄 75 包 §1 之 **R-VS68′**、**R-VS69**、**R-VS35 之補充** 入 RULINGS.md。
D-3  `delivery_disclosure.md` 依 **R-VS69** 重列，分 §A／§B-1／§B-2 三節；
     **必列**：三節之條數與其合計，及與現行 `screen_pending = 10` 之差額。
D-4  ANOMALIES.md：A-VS151／152 標處置；依 R-VS35 分線列兩數。D-6 骨架對照照做。

## 作業（三項）

W-136  **實寫前之最終核對**（**未過不得實寫**）
       (1) 重跑 dry-run，逐項列 66 包 §3 之欄位對映之實測：
             將寫入之列數 ＝ `generated/*_v{max}.json` 之 leaf 聯集數
             I 欄上下段結構 ＝ 列數（兩段皆有）
             K 欄非 `NA` 者 ＝ 0
             R 欄不在受控 9 值內者 ＝ 0
             N 欄多值列之行數分布（一 ObjectID 一行，無 `,`／`;`）
             AH 欄非空者 ＝ `delivery_disclosure.md` 之 §A＋§B-1＋§B-2 合計
             AA 欄 ＝ `PeiPYHsu`
       (2) **母本雜湊複核**：實寫前之母本 sha256 須等於
           `ebe5a65f30a0d4bcf9e46b51a43145ce222027ac49ad523fe5c2d2b6566a5089`；
           **不等即中止**（其表示母本已被他人改動）
       (3) R-VS54 固定錨點 20 項須全數「必命中」

W-137  **實寫**
       母本：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/
             Vehicle Settings/CFTS044/FM-WI-FSM-036-A01 …_20260819.xlsx`
       分頁 `Test Case Specification 測試用例規範`；表頭列 9；資料列 10 起。
       (1) 先清空現有 237 列之 B–AH（R-VS1：效力 BLANK、全欄重生）
       (2) 自列 10 起 append，依 66 包 §3 之欄位對映
       (3) **寫入後重讀驗證**：逐列比對 JSON 與工作簿之十六欄，
           **不符即中止並自 `REF/036_pre_writeback_20260823.xlsx` 還原**
       (4) 實寫後取 sha256，記入上繳包

W-138  **PDT24 兩檔之補列準備**（**不執行複製**）
       依 R-VS68′ 備妥 `INPUTS.sha256` 之補列文字（18 檔）與其核對指令；
       **並以該二新檔重量 71 輪之補充證據**（四份 DBC 中 `*_Cmd_Tlm`／
       `SETUP2` 皆不存在、`*_Tlm` 自 2022 年起為 1 bit），
       **不符者具名**。實際複製屬 Pei。

## 升級條件

W-136(2) 之母本雜湊不等；
W-136(1) 之任一項不符；
W-136(3) 之任一錨點未命中；
W-137(3) 之重讀比對不符（**中止並還原**）；
W-138 之重量結果與 71 輪之補充證據不符。
```

---

## 3. 待 Pei

| # | 事項 |
|---|---|
| 1 | **PDT24 兩檔複製入 `inputs/`**（依 R-VS68′ 之 `20260109`／`20260520_CR26320` 二版） |
| 2 | **`impl_gap` 之 44 條開 issue 予 RD**（R-VS66(a)；訊號不在基線 DBC） |
| 3 | 實寫完成後之入庫與交付（**git 屬你**；`writeback_036.py` 會備指令） |

---

## 4. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| pilot #3＋#4 | **通過** | **Pei** |
| R-VS68′ | PDT24 取 `20260109`／`20260520_CR26320` 二版；補充證據須重量 | **Pei** |
| R-VS69 | `screen_pending` 以 AH 之 BLOCKED 註記為判準；揭露分三節 | 分析層 |
| R-VS35 之補充 | 升級中止不及於登記類 D 項 | 分析層 |
