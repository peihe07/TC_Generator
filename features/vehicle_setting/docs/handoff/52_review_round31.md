# 52 下放包 — A-VS98 裁定（R-VS20 之排除早已縮限）、32 輪

分析層寫入，2026-08-22。

---

## 0. 先認一件事：51 包 §0 之狀態誤述

我寫「D-2～D-5 與 W-86／87／88 全部未執行」。
實況為 **D-2 已於 30 輪完成**（R-VS50 在 `RULINGS.md:1063`）、
**W-86(1)(2)(3) 亦已執行並口頭回報，惟未落檔**。

執行層之判斷正確：**「已執行未落檔」與「未執行」在交付物上不可區分。**
其自行提出之驗法（每輪結束前以骨架之 ⬜／✅ 對照實際節內容，
空節而標 ✅ 者為不一致）**採用，列為每輪之 D 項**。

---

## 1. A-VS98 —— **不是條文矛盾，是我引用了已被取代的條文**

執行層引 R-VS20 之「他架構條文（CUSW／PowerNet／**Atlantis Mid**）之值域
一律不取用」而判 `*_Cmd_Tlm` 不可取用。

**該段已於 33 包被 R-VS19″(a) 取代**，其逐字為：

> R-VS19 之「他架構條文之值域一律不取用」**縮限為 `CUSW`／`PowerNet`
> 專屬者**；`Atlantis Mid` **不再排除**。

**即 R-VS20 之排除清單自 33 包起即不含 `Atlantis Mid`。**
執行層引之為現行文字，是因 `RULINGS.md` 之 R-VS20 條目**未加註其被縮限**
—— 而 33 包 D-2 只令標註 R-VS19，未及於 R-VS20。**該疏漏在我。**

```
R-VS51（架構對應之欄組，分析層裁定 2026-08-22；本輪唯一新條文）

(1) **R-VS20 之排除清單依 R-VS19″(a) 為 `CUSW`／`PowerNet` 專屬者。**
    `Atlantis Mid` 之條文既在母體內（R-VS19″），其值域**得取用**。
    `RULINGS.md` 之 R-VS20 條目須加註「排除清單經 R-VS19″(a) 縮限」。

(2) **值域與訊號對映之欄組，依該條文之 `EE Architecture` 決定**：
      條文標 `Atlantis High`（或 `All`） → LID 之 `Atlantis High` 欄組
      條文標 `Atlantis Mid`             → LID 之 **`Atlantis` 欄組**
      條文同時標二者                    → 取 `Atlantis High` 欄組
    R-VS9(1)′ 之「`CAN Mapping` → Atlantis High 欄組」為**預設**，
    非唯一；本條為其按條文架構之分流。

(3) **例外（R-VS44 優先）**：凡該 (token, 值) 落在未結 DR 之範圍內者，
    **仍由 `guard()` 攔下**，不因本條而放行。
    具體：DR-15 之 token 級範圍含 `FL_VS_RQ_TGW` 等五者 ——
    其值域不因本條而解。

理由：R-VS19″ 依 `Radio`＋`ECU` 判適用性並將 `Atlantis Mid` 納入母體
（13 輪實測：Mid 條文之章節自稱 `applicable for R1 Low`，
三屬性與非 Mid 組 100% 一致）。
既納入母體而不許取其值域，則該批 leaf 恆在範圍卻恆不可寫 ——
**該狀態非任何一條之本意，而是 R-VS20 之文字未隨 R-VS19″ 更新。**
```

---

## 2. 一項發現須寫入 DR-15，**但不得用以作答**

LID 列 769 之同一 LID（`FL_VS_RQ_TGW`）：

| 欄組 | Signal | 值域 |
|---|---|---|
| **Atlantis** | `TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm` | **2 bit，四階**（Off／Low／Medium／High） |
| **Atlantis High** | `TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm` | **1 bit**（Not_Pressed／Pressed） |

**同一個邏輯識別碼，在兩個架構下對映到位元寬不同之訊號。**

DR-15 所問者正是「請求訊號為 1 bit 或承載階數」——
**本發現指出兩者皆為真，只是分屬不同架構**，
且 CFTS044 描述循環降階之條文（`4858325` 等）標為 `Atlantis High`，
**其內容卻與 `Atlantis` 欄組之四階值域相符** ——
**疑為自 Atlantis Mid 遷入時未改架構標籤。**

```
分析層裁定
**不得以本發現作答 DR-15**（R-VS44）。
改為**補入 DR-15 之提問文**作為我方之觀察，供上游確認：

  「我方於 LID v1.76 列 769 觀察到：同一 LID `FL_VS_RQ_TGW` 於
   `Atlantis` 欄組對映至 `TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm`
   （2 bit、四階），於 `Atlantis High` 欄組對映至
   `TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm`（1 bit、Not_Pressed/Pressed）。
   而 CFTS044 描述循環降階之條文（4858325／4858355／4858385／4858416）
   標記為 `[EE Architecture:Atlantis High]`。
   請確認該等條文之架構標記是否正確，或其所述行為是否屬 Atlantis Mid。」

DR-15 仍為待覆，其 `guard()` 範圍不變。
```

---

## 3. A-VS97 —— 依 R-VS38 判為 typo

`FL_VS_Cmd_Tlm`（列 769 `Vented_Seat_*`／列 770 `Heated_seat_*`）與
`FR_VS_Cmd_Tlm`（列 790 `Heated_seat_*`）。

依 **R-VS38** 三項聯合判準：
(a) 對稱側：列 769 為 `Vented_Seat_*`；
(b) 同表內兩形態並存 → **自相矛盾，判 typo**；
(c) 通風訊號用加熱前綴，與 A-VS49 同型（該案已判 typo）。

```
分析層裁定
`FL_VS_Cmd_Tlm`／`FR_VS_Cmd_Tlm` 之值域取 **`Vented_Seat_*`**，
列 770／790 之 `Heated_seat_*` 判為 LID 之轉錄錯誤。
`spec_variables.tsv` 增 `suspect_prefix` 標記（同 A-VS49 之處置），
**不改原值**。併入 **DR-18**（確認型），不另開 DR。
```

---

## 4. 32 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/52_review_round31.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/29_arch_columns.md，六節先留空。
D-2  逐字轉錄 52 包 §1 之 **R-VS51** 入 RULINGS.md；
     **R-VS20 之條目加註「排除清單經 R-VS19″(a) 縮限為 CUSW／PowerNet 專屬者」**。
D-3  `DATA_REQUESTS.md`：DR-15 補入 52 包 §2 之觀察段（**不改其待覆狀態**）；
     A-VS97 併入 DR-18。
D-4  ANOMALIES.md：**A-VS98 依 R-VS51 關閉**；A-VS97 依 52 包 §3 標 typo。
D-5  依 R-VS35 列兩數。
D-6  **本輪結束前**：以本檔首表之 ⬜／✅ 對照各節實際內容，
     空節而標 ✅ 者列為不一致（執行層 28 §6 之自提驗法，本包採用）。

## 作業（三項，R-VS25）

W-90  **依 R-VS51 重跑分級**（最高優先）
      (1) `spec_variables.tsv` 增 `arch_column` 欄：
          逐 (token, 條文) 對，依該條文之 `EE Architecture` 決定其取值欄組
          （Mid → `Atlantis`；High／All → `Atlantis High`；並列 → High）
      (2) 併入 `Atlantis` 欄組之值域（含 `*_Cmd_Tlm` 四者，
          依 52 包 §3 取 `Vented_Seat_*`）
      (3) **逐筆過 `guard()`** —— DR-15 之五個 token 仍須攔下
      (4) 全量重跑分級，列 W0／W1／W2 三數與 **103／2／132** 之對照
      (5) **必列**：因 R-VS51 而由 W2 轉出者之條數，及其中被 `guard()`
          攔下者之條數（二者不可互代）

W-91  batch13 —— **10 條**
      自 W-90 後之池選 leaf，逐 Layer 2 輪流；逐條過 `guard()`；
      套 profile ＋ canon §8.7.5 v3 ＋ R-VS43／R-VS48′／R-VS49／**R-VS51** ＋
      Sibling Rows ＋ 無效值優先序；§9 十七項自檢 ＋ DBC 值表核對。
      **取用 `Atlantis` 欄組之值者，`reasoning` 須記其條文架構與欄組。**
      池不足 10 時取全部並回報。

W-92  batch14 —— **10 條**
      同上。**W-91 完成後不等覆核，逕行 W-92。**

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
**不得以 R-VS51 解掉 DR-15 之標的**（R-VS44 優先）。
不得撰寫適用性前言型條文之 TC。

## 升級條件

W-90(5) 之轉出數 < 20；
W-90(3) 有 DR-15 之 token 未被攔下；
W-91／W-92 交付合計 < 12。
```

---

## 5. 待 Pei

| 項 | 內容 |
|---|---|
| **pilot #2 之裁決** | 51 包 §1 之分類表（pass 10／defect 4／note 1）—— **已修正完成，待覆核** |
| **A-VS62** | `is registered without a bus error` 二選一 —— **懸置七輪** |
| **DR-21** | 已定案（137 leaf／215 次／27 token），**可送** |
| DR-17／DR-20／DR-23／DR-8′／DR-24′／DR-18／DR-11 | 待送 |

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS51 | R-VS20 排除清單依 R-VS19″(a) 縮限；值域欄組依條文架構分流；R-VS44 優先 | 分析層（本輪額度用畢） |
| A-VS97 之裁定 | `*_VS_Cmd_Tlm` 取 `Vented_Seat_*`，`Heated_seat_*` 判 typo | 分析層（適用 R-VS38） |
