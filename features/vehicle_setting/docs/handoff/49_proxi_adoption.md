# 49 下放包 — PROXI 值域採用（79 leaf 解鎖）、29 輪指令

分析層寫入，2026-08-22。**`PROXI_HDCC27_R3_20250424.xlsx` 已入 `inputs/`（16 檔）。**

---

## 1. 裁決正文（執行層逐字轉錄入 `RULINGS.md`）

```
R-VS49（分析層裁定 2026-08-22；推翻 44 包 §1；Pei 得推翻）
採用 `PROXI_HDCC27_R3_20250424.xlsx` 之 `Format` 分頁，
作為下列四個 PROXI 參數之值域來源：

    Cooled_Seats           0 = Absent / 1 = Front Seats /
                           2 = Front And Rear Seats / 3 = Not Used
    Heated_Seats           同上
    Heated_Steering_Wheel  0 = Absent / 1 = Present
    Heated_Seat_Levels     0 = 1  Level / 1 = 2 Levels / 2 = 3 Levels

依據（版本層級之對應，非車型層級）：
  該表之 VF 引用欄逐字為 `LTM (VF664_V2); ETM (VF664_V3);`
  （`Heated_Seat_Levels`）；
  R1LR 之 LID v1.76 對同四參數所載 `VFs` 欄逐字為 `664`，
  其 `ECU` 為 `LTM`／`ETM`。
  **二者於 VF 編號、版本、ECU 三項皆一致。**

44 包 §1 之拒絕理由（`VF664_V42_R3`／Toro226 未提及該四參數，
故 VF664 內容隨版本而異）**不成立** ——
Toro226 所引為 `V42`，非 `V2`／`V3`；版本不同即無須提及，
該事實不構成對「V2／V3 定義一致」之反證。

**適用範圍**：限於上開四參數。該表之其餘參數不因本裁定而可援引；
其援引須另行裁定。

**標記要求**：凡取用該四參數值域之 TC，其 `reasoning` 須記
「值域取自 PROXI_HDCC27_R3（VF664_V2/V3，與本專案 LID 之 VFs=664、
ECU=LTM/ETM 一致）」。

A-VS77 關閉。**DR-22′ 撤回，不送出。**
```

```
R-VS39 補充（分析層裁定 2026-08-22）
數詞與阿拉伯數字互為同一值之寫法（`one`↔`1`／`two`↔`2`／`three`↔`3`／
`four`↔`4`／`five`↔`5`），納入 R-VS39 之正規化鍵。
套用後仍須目標唯一方得對映。

本例：`Heated_Seat_Levels` 之 `One Level` → 正規化為 `1 level`，
於值域 {`1  Level`, `2 Levels`, `3 Levels`} 中唯一命中 → **raw = 0**。
```

---

## 2. 三個待解值之定案

| 條文所用之值 | raw | 命中方式 |
|---|---:|---|
| `Front Seats`（`Heated_Seats`／`Cooled_Seats`） | **1** | 逐字 |
| `Present`（`Heated_Steering_Wheel`） | **1** | 逐字 |
| `One Level`（`Heated_Seat_Levels`） | **0** | R-VS39 補充（數詞↔數字），唯一 |

---

## 3. 29 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/48_review_round28.md
  features/vehicle_setting/docs/handoff/49_proxi_adoption.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/27_proxi_and_pilot2.md，六節先留空。
D-2  逐字轉錄 48 包 §1 之 **R-VS48′**、49 包 §1 之 **R-VS49** 與
     **R-VS39 補充** 入 RULINGS.md。
D-3  `INPUTS.sha256` 補入 `PROXI_HDCC27_R3_20250424.xlsx`（**16 檔**），
     並跑 `shasum -c` 全檔驗證。
D-4  A-VS93 依 R-VS48′ 關閉；**A-VS77 依 R-VS49 關閉**；
     `DATA_REQUESTS.md` 之 **DR-22′ 標「撤回，R-VS49」**（原文保留）。
D-5  依 R-VS35 列兩數。

## 作業（三項，R-VS25）

W-83  **R-VS48′ 之複查 ＋ PROXI 值域併入 ＋ 全量重跑**
      (1) 28 輪採用之 15 對逐對標路徑 (a)/(b)/(c)；
          **(b) 路者逐對人讀**，未通過者移出。
          驗收：`IGN_OFF → IGN_LK` 須不在採用表內
      (2) `W2 → W0` 之 8 條逐條人讀，不可寫者退回 W2
      (3) **依 R-VS49 將四參數值域併入 `spec_variables.tsv`**
          （來源標 `PROXI_HDCC27_R3`），
          **依 R-VS39 補充加數詞↔數字之正規化**
      (4) **全量重跑分級**，列 W0／W1／W2 三數與 28 輪之 101／2／134 對照；
          **並列「因 R-VS49 而由 W2 轉出者」之條數**
      (5) 新對逐筆過 `guard()`（DR-22′ 已撤回，其閘須同步移除）

W-84  **pilot #2 之 review sheet**
      依 48 包 §3 之抽法產 `docs/reports/pilot2_sheet.md`，**15 條**
      （12 分層 ＋ 3 必檢）。**列抽樣之交叉格矩陣**使抽法可複現。
      每條含十欄全文 ＋ `dr_dependent` ＋ `dr15_exposed` ＋ 來源條文逐字節錄。

W-85  batch11 ＋ batch12 —— **各 10 條**
      自重跑後之池選 leaf，逐 Layer 2 輪流；逐條過 `guard()`；
      套 profile ＋ canon §8.7.5 v3 ＋ R-VS43／R-VS48′／R-VS49 ＋
      Sibling Rows ＋ 無效值優先序；§9 十七項自檢 ＋ DBC 值表核對。
      取用四參數值域者，`reasoning` 依 R-VS49 記其來源。
      **batch11 完成後不等覆核，逕行 batch12。**
      池不足時取全部並回報。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
**(b) 路之對映不得自動採用**（R-VS48′）。
**R-VS49 限於該四參數**，該 PROXI 表之其餘參數不得援引。

## 升級條件

W-83(1) 之 (b) 路對有半數以上未通過人讀；
W-83(4) 之 W2 轉出數 < 40（則 79 leaf 之解鎖不如預期，須追因）；
W-85 之兩批交付合計 < 12。
```

---

## 4. 待 Pei（**DR-22′ 撤回後剩七份**）

| DR | 型 | 影響 | 狀態 |
|---|---|---:|---|
| **DR-17** | A | 4 leaf（已可寫，卡委派） | 待送 |
| DR-21 | A | B2 類 | 待送 |
| DR-20／DR-23 | B | 17／3 | 待送 |
| DR-8′ | B | 8 引用 | 待送 |
| DR-24′ | A | 43 | 待送 |
| DR-18／DR-11 | A | — | 待送 |
| **pilot #2** | — | 67 條未 review | **清單 29 輪產出，分類次包出** |

---

## 5. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS49 | 採用 HDCC27 PROXI 表之四參數值域；VF664_V2/V3 版本層級一致 | 分析層（本輪額度用畢） |
| R-VS39 補充 | 數詞↔數字納入正規化鍵 | 分析層（同一裁定之配套） |
