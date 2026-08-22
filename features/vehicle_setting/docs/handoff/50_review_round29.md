# 50 下放包 — 「79」是我的錯、真正瓶頸是 `*_Cmd_Tlm`、30 輪

分析層寫入，2026-08-22。**產能再度為 0，但其解已具名且規模為 7.6 倍。**

---

## 1. 「DR-22′ 影響 79 leaf」是我的錯，且我用它排了三輪優先序

執行層追因：全母體引用該四參數者 **8 條**，非 79。
「79」來自 21 輪之 `quoted_form_risk` 標記 —— **該標記涵蓋引號形態下
全部未解 token 所影響之 leaf**，而其中僅 8 條涉及 PROXI 參數。

**我在 24／25／26 三包稱「DR-22′ 為單一最大解鎖」，並據此**：
- 42 包令 W-65 以其為最高優先（搜遍 5,304 檔）
- 43 包令 W-68 為其擴掃 1,994 檔之內容
- 44／45／46／47／48 五包每包以其為「單一最大」列於待 Pei

**該數自 21 輪起未曾回查其組成。** 這是 R-VS34 之形態（以推測代替實測），
犯者為分析層，且**連續八包未察**。

```
R-VS50（來源數字之回查，分析層裁定 2026-08-22；本輪唯一新條文）
凡以某一數字作為**優先序之依據**者（如「影響 N 個 leaf」「阻塞 N 條」），
於其**首次被引用為決策依據時**，須回查其組成並列出：

  (1) 該數之產生輪次與判準
  (2) 其組成之逐項分解（依 token／條文／類別）
  (3) 與當前待決事項之交集

未回查即引用者，該優先序記為「未驗」，**不得據以排定作業順序**。

理由：「79」為 21 輪之 `quoted_form_risk` 計數，其涵蓋全部未解 token；
分析層自 24 包起連續八包以之為「單一最大解鎖」而未回查其組成，
實際涉及 PROXI 參數者僅 **8 條**。
兩輪之搜尋作業（W-65 掃 5,304 檔、W-68 擴掃 1,994 檔）因而排在
實際規模為其 7.6 倍之標的之前。
```

---

## 2. 真正之瓶頸：`*_Cmd_Tlm` 四者，**61 leaf**

| token | leaf |
|---|---:|
| `FL_HS_Cmd_Tlm` | 17 |
| `FR_HS_Cmd_Tlm` | 16 |
| `FL_VS_Cmd_Tlm` | 14 |
| `FR_VS_Cmd_Tlm` | 14 |
| **合計** | **61** |

其於 `can_signal_map.tsv` 記為 `NOT_IN_DBC`
（`TELEMATIC_CLIMATE_SETUP.FL_HS_Cmd_Tlm_Req` 等）。

**但 `NOT_IN_DBC` 是早輪之記載，其 LID 原表未回查。**
PROXI 四參數之前例已證：**LID 之 `Format` 欄可能為 `See Proxi Table` 之轉指，
而非「不存在」**。

→ **W-86。其規模為 DR-22′ 之 7.6 倍，且與 DR-22′ 同型（可能是轉指而非缺件）。**

---

## 3. A-VS96 —— W0 可能虛高，須量

四條適用性前言（`Following requirements are valid only if …`）
**值可解但無可測內容**，與 13 輪判為 (c) 之 `4859399`／`4859463` 同型，
亦與 A-VS76（B4 偵測盲區）同源。

**執行層未為湊足 batch11 之數而撰寫它們 —— 正確。**

→ **W-87：全量掃同型，修正 W0。**

---

## 4. 30 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/50_review_round29.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/28_cmd_tlm.md，六節先留空。
D-2  逐字轉錄 50 包 §1 之 **R-VS50** 入 RULINGS.md。
D-3  `DATA_REQUESTS.md`：**DR-21 之影響範圍以 W-86 之結果重估並改寫**；
     其現載之範圍（B2 類）須列出逐 token 之 leaf 數。
D-4  依 R-VS35 列兩數。

## 作業（三項，R-VS25）

W-86  **`*_Cmd_Tlm` 四者之 LID 回查**（最高優先，61 leaf）
      (1) 於 `Logical Identifiers and CAN Mapping v1_76.xlsx` 逐列查
          `FL_HS_Cmd_Tlm`／`FR_HS_Cmd_Tlm`／`FL_VS_Cmd_Tlm`／`FR_VS_Cmd_Tlm`
          （**以 R-VS36 三形態試法**：`$X$`／裸名／描述式）
      (2) 逐欄列其 `Atlantis High` 與 `Atlantis & Atlantis High` 欄組之
          `Signal Name`／`CAN`／`Format`／`SNA`
      (3) **判其 `Format` 為實值域、轉指（如 `See Proxi Table`）、或空**
      (4) 若為轉指 → 依 R-VS45 判其型別（型 B），並查所指之表是否已在
          `inputs/`（**PROXI_HDCC27_R3 已入，其 `Format` 分頁須先查**）
      (5) 若為實值域 → 併入 `spec_variables.tsv` 並全量重跑分級
      **必列**：四 token 之 LID 命中列數、其 Format 之逐字內容、
      及重跑後之 W0／W1／W2 與 108／2／127 之對照

W-87  **適用性前言之全量掃描**（A-VS96）
      形態：`Following requirements are valid only if`／
            `The requirements in this section are applicable`／
            `applicable for … only`／`This section applies`
      (1) 掃 237 leaf 所引條文，列同型之總數與逐條 reqid
      (2) 該等 leaf **改判 W2**，`blocker_class` 記 `B4-preamble`
      (3) 列修正後之 W0／W1／W2 —— **W0 之虛高幅度即此**

W-88  batch13 —— **10 條**
      自 W-86／W-87 修正後之池選 leaf；池不足時取全部並回報。
      逐 Layer 2 輪流；逐條過 `guard()`；套 profile ＋ canon §8.7.5 v3 ＋
      R-VS43／R-VS48′／R-VS49 ＋ Sibling Rows ＋ 無效值優先序；
      §9 十七項自檢 ＋ DBC 值表核對。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
**不得撰寫適用性前言型條文之 TC**（W-87 判 W2 者）。
R-VS49 限於該四 PROXI 參數。(b) 路不得自動採用。

## 升級條件

W-86(3) 判四者為實值域（**正向** —— 61 leaf 可解，立即回報）；
W-86(3) 判為轉指且所指之表不在 `inputs/`（則開型 B DR）；
W-87(1) 之同型總數 > 20（則 W0 虛高逾 18%）；
W-88 之交付 < 5。
```

---

## 5. pilot #2 —— 清單已出，分類於次包

`docs/reports/pilot2_sheet.md` **15 條、1,063 行**已產出。

**分析層於次包逐條讀並附建議分類**，與 30 輪並行，不互相等待。

**惟 §2.3 之偏斜須先記明**：`Heated Seat` 佔母體 37%（88/237），
而其於 15 條抽樣中僅 **1** 條。成因為產能分布（該 Layer 2 之可生成者
早已耗盡於 batch01–03）。
**故 pilot #2 之結論不得推論至全母體之品質** —— 其代表性受產能分布所限。

---

## 6. 待 Pei

| 項 | 影響 | 狀態 |
|---|---:|---|
| **DR-21** | **重估中**（`*_Cmd_Tlm` 61 leaf 為其大宗） | 待送 —— **俟 W-86 定案再送，其提問文將改變** |
| DR-17 | 4 leaf | 待送 |
| DR-20／DR-23／DR-8′／DR-24′／DR-18／DR-11 | — | 待送 |
| **pilot #2** | 68 條未 review | 清單已出，**分類次包出** |

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS50 | 作為優先序依據之數字，首次引用時須回查其組成 | 分析層（本輪額度用畢） |
