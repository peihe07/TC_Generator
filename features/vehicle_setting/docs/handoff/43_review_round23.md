# 43 下放包 — 23 輪覆核：VF664 才是共同錨點、閘之宣告粒度、24 輪指令

分析層寫入，2026-08-22。對象：`docs/upstream/21_proxi_hunt.md`。

**覆核結論：接受。** W-65 之搜尋設計（5,304 檔、餘數具名、界線自陳）是本
feature 迄今最完整的一次搜尋；W-66(3) 之閘測**測出閘沒擋**，正是該測之目的。

---

## 1. A-VS77 —— **這不是跨車型代入，共同錨點是 VF664**

執行層以「他車型之表」為由不採用，**謹慎正確**。
但分析層讀其三項佐證後認為**其性質被低估了**：

| 佐證 | 執行層之讀法 | 分析層之讀法 |
|---|---|---|
| 兩份獨立表逐字一致 | 兩車型碰巧相同 | **二者皆為同一上游文件之轉錄** |
| `Heated_Seat_Levels` 僅引 `VF664_V2`／`VF664_V3` | 他車型之 VF 引用 | **VF664 是該參數定義之所在** |
| **R1LR 自身之 LID 欄 20 逐字為 `664`** | 旁證 | **R1LR 自己說：本參數之定義在 VF664** |

**即：R1LR 之 LID 與 DT27／HDCC27 之 PROXI 表，指向同一份文件 —— `VF664`。**

**這不是「拿他車型的值來用」，是「三份文件都說值在 VF664，其中兩份轉錄了它」。**

**但我方仍未持有 VF664 本身**，現有的是**兩份獨立轉錄**。
兩份獨立轉錄逐字一致，是相當強的證據，**但仍是轉錄**。

### 1.1 決定性事實：客戶目錄之頂層有 `VF`

執行層 §1.1 列頂層目錄為
`CPAA_spec`／`Development Docs`／`R1LR SR26 ATL-H`／**`VF`**。

**VF664 可能就在那裡。** 而 W-65 之檔名掃描只查了 `*proxi*`／`*664*`／
`*R1L*+*config*` —— **`*664*` 有查**，但其結果未單獨列出
（只列了 `proxi` 之 30 筆）。

→ **W-68 之第一項即此。取得 VF664 原件，本案即由「推定」變為「查得」。**

```
分析層裁定 2026-08-22（暫行處置，俟 W-68）
在 VF664 原件到手前：
(1) **不採用**他車型 PROXI 表之值域寫入 TC
(2) **DR-22′ 暫緩送出**
(3) 其三項佐證記入 `writability.tsv` 之 `evidence_note` 欄，
    標 `VF664-inferred`，**不改 `writable` 之判定**

若 W-68 取得 VF664 且其四參數值域與兩份轉錄一致 →
**該四參數由「未解」改為「查得」，79 個 leaf 之阻塞解除**，
且**不需任何 DR**。

若 W-68 未取得 → DR-22′ 改以**是非題**送出（執行層 §2.1 之建議，採之）：
「R1LR 之 `Cooled_Seats`／`Heated_Seats`／`Heated_Seat_Levels`／
`Heated_Steering_Wheel` 四參數，其值域是否即 VF664_V2／V3 之定義？
（我方 LID v1.76 之 `VFs` 欄逐字為 `664`）」
—— 是非題之前置時間遠短於「請提供文件」。
```

---

## 2. A-VS78 —— **閘之宣告粒度，是我的設計缺陷**

R-VS44 之實作以 `(token 集合, 值之正則, 狀態)` 宣告未結 DR 之範圍，
該粒度由 42 包 §3.1 之措辭（「以一個已知會撞的輸入去測它」）暗示為值級。

**但 DR-15 問的是訊號之編碼本身**（1 bit 或承載階數），
**其標的涵蓋該五個 token 之全部值**。把 `Pressed` 對映為 `1 (Pressed)`
即預設了「1 bit」那個答案 —— **正是 R-VS44 所要禁止者。**

```
R-VS44′（宣告粒度之更正，分析層裁定 2026-08-22；本輪唯一新條文）
未結 DR 之範圍宣告，其粒度須與**該 DR 所問之對象**一致，得為三級：

  **token 級**  該 DR 問的是某訊號之編碼、位元寬、或其存在與否
                → 該 token 之**任何值**皆在範圍內
  **值級**      該 DR 問的是某幾個特定值之對應
                → 僅該等值在範圍內
  **條文級**    該 DR 問的是某條文之引用或語意
                → 該條文所涉之全部 token 與值皆在範圍內

宣告時**須具名其級別**；未具名者預設為**最寬之級別**（條文級）。

**DR-15 更正為 token 級**，其 token 集合為
`FL_HS_RQ`／`FR_HS_RQ`／`FL_VS_RQ_TGW`／`FR_VS_RQ_TGW`／`HSW_RQ_TGW`，
**值樣式為 `.`（全部）**。

理由：以值樣式宣告，會使同一 DR 之未列舉值逃過檢查。
23 輪實測：補極性表後新增之 4 組 derivable 全屬 `Pressed` 型，
**閘 0 攔截**，而其正落在 DR-15 之標的上。

**驗收**：以該 4 組為輸入重跑，須全數輸出 `DR-CONFLICT: DR-15`；
移除交叉檢查後須判回 `derivable`（可失敗性）。
```

---

## 3. 三項裁定（適用既有政策）

### 3.1 DR-24 併入 `<Tdisplay>`（A-VS79）

```
DR-24′（取代 42 包 §3.2 之 DR-24；型 A）
CFTS044 使用兩個時間符號而未給其具體值：

    `<Tsend>`     15 次引用
    `<Tdisplay>`  28 次引用
    去重後涉及 **43 個 SWE leaf**

canon §8.7.1 要求門檻須為具體值，故二者皆無法作為 ER 之通過條件。

請提供 `<Tsend>` 與 `<Tdisplay>` 之具體時值（含單位與量測起訖點）。

我方之暫行處置：procedure 保留符號原樣（來源逐字），
ER 改寫為可觀察之終態，不以時限為通過條件。
```

### 3.2 §6-4 `SNA` 不得作為 invalid state 之注入值

`4858517` 之 `All other states shall be considered invalid` ——
其 `states` 指該訊號之狀態編碼；**`SNA` 是 DBC 中已定義之編碼**，
語意為「訊號不可用」，**非「無效狀態」**。

```
分析層裁定
`SNA` 不得作為「invalid state」之注入值。
無效值之注入須取 **DBC 中未定義之編碼**；
該訊號之編碼若已全數定義，則**無可注入之無效值** ——
該 TC 標 `PENDING: DR-{n}` 或改以他條文所載之配置相依無效值
（如 `4858307` 之二階配置下 `medium` 為無效）。

`batch04` 之 `HeatedSteeringWheel-006` 依此重檢：
`HSW_Stat_2`（`Tri_Level_HSW_StatSts`）之 DBC 編碼為
`0/1/2/3` ＋ `7 SNA` —— **4／5／6 為未定義**，得取其一為注入值。
```

### 3.3 型 B 之其餘三筆 —— 併入 W-68 一次搜尋

R-VS45(1) 令型 B 先搜尋。本輪只搜了 DR-22′。
**DR-20／DR-23（`TLM HMI Document`，影響 17 leaf）與 DR-8 未搜。**

**且 W-65 之內容掃描只涵蓋 xlsx/xlsm/docx，未涵蓋 pdf 898／xls 494／
doc 242／rtf 360（合計 1,994 檔）** —— 其中 `TLM HMI Document`
極可能是 pdf 或 doc。**該界線正是 00D 之教訓**（`Core HMI Logic and Flow`
之文字層須旋轉 180° OCR 方可讀）。

---

## 4. 24 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/43_review_round23.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/22_vf664_hunt.md，六節先留空。
D-2  逐字轉錄 43 包 §2 之 **R-VS44′** 入 RULINGS.md；
     `dr_conflict.py` 之 `OPEN_DR` 逐筆標級別，**未具名者預設條文級**。
D-3  `DATA_REQUESTS.md`：**DR-24 改寫為 DR-24′**（43 包 §3.1，併入
     `<Tdisplay>`，43 leaf），原文保留加註。
D-4  `writability.tsv` 增 `evidence_note` 欄，四個 PROXI 參數標
     `VF664-inferred`，**不改 `writable` 判定**（43 包 §1.1）。
D-5  ANOMALIES.md 依 R-VS35 列兩數（含分析層側：43 包開立 0 anomaly／0 DR）

## 作業（三項，R-VS25）

W-68  **型 B 之一次搜尋**（最高優先）
      於 `/Users/peihe/Work/02_Project_R1LR/1_Customer_Requirement/` 唯讀搜尋，
      **本輪擴及 pdf／xls／doc／rtf（1,994 檔）之內容**，非僅檔名：
      (1) **`VF664`** —— 頂層有 `VF` 目錄；先列該目錄之全部檔名，
          再以 `664` 為鍵；找到者抽出四個 PROXI 參數之值域，
          與兩份轉錄逐字比對
      (2) **`TLM HMI Document`**（DR-20／DR-23，17 leaf）
      (3) **完整車型碼對照**（DR-8：`DT`／`WS`／`HDCC`／`M240`）
      pdf 須先驗文字層產出量；抽不到者依 00D 之法試 OCR
      （含旋轉），仍抽不到者標「未解析」並列其檔名與頁數。
      **唯讀，不複製任何檔案入 `inputs/`。**
      **找不到亦須列已掃之目錄、檔型、檔數**（R-G10）。

W-69  閘之修正與重驗（R-VS44′）
      (1) `OPEN_DR` 之宣告改為三級，逐筆標級別
      (2) **DR-15 改為 token 級**，token 集合五個，值樣式 `.`
      (3) 以 23 輪之 4 組 `Pressed` derivable 為輸入重跑 ——
          **須全數 `DR-CONFLICT: DR-15`**
      (4) **可失敗性**：移除交叉檢查後須判回 `derivable`
      (5) 以現有全部判定結果重跑一次，列出**新增被攔下者**

W-70  batch04 之複檢與 batch05
      (1) `HeatedSteeringWheel-006` 依 43 包 §3.2 改注入值
          （`Tri_Level_HSW_StatSts` 之 4／5／6 未定義編碼之一），
          並重檢 batch01–04 之全部無效值注入是否誤用已定義編碼
      (2) batch05 生成 **10 條**，選 leaf 依逐 Layer 2 輪流；
          套 profile ＋ canon §8.7.5 v3 ＋ R-VS43 ＋ Sibling Rows；
          §9 十七項逐項自檢 ＋ DBC 值表逐字核對
          **ER 不得以 `within <Tsend>`／`<Tdisplay>` 為通過條件**

## 禁區

git 不執行。不寫回工作簿。不代擬條文。v1/v2/v3 保留不刪。
**不得複製任何檔案入 `inputs/`**（W-68 為唯讀）。
**不得採用他車型 PROXI 表之值寫入 TC**（43 包 §1.1，俟 VF664）。

## 升級條件

W-68(1) 找到 VF664（**正向升級** —— 79 leaf 可解，立即回報）；
W-68(2) 找到 TLM HMI Document（**正向升級** —— 17 leaf）；
W-69(3) 有任一組未被攔下；
W-70(1) 之複檢發現 batch01–03 亦有誤用已定義編碼者。
```

---

## 5. 待 Pei

| # | 事項 |
|---|---|
| — | **DR-21（型 A，65 leaf）／DR-23（型 A，3 leaf）／DR-18／DR-8／DR-11 可送** |
| — | **DR-22′ 暫緩**（俟 W-68 之 VF664 搜尋） |
| — | **DR-24′ 暫緩**（本輪改寫，俟 W-68 併同其他型 B 結果一次送） |

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS44′ | 未結 DR 之宣告粒度三級；未具名者預設條文級；DR-15 改 token 級 | 分析層（本輪額度用畢） |
| DR-24′ | 併入 `<Tdisplay>`，43 leaf | 分析層擬 |
| `SNA` 不得作為 invalid 注入值 | 適用既有政策 | 分析層 |
