# 53 — Comfort HMI / 批次 10 ＋ `Climate Popups` 之解封

- 產出層：分析層｜2026-08-15｜對象：執行層
- 承接：下放包 52（同一次覆核，拆檔）

---

## 1. `Climate Popups` 之阻塞範圍收窄 —— 由整組改為 `14.12` 之 leaf

49 §1 曾指示「`14.12` 之軸未定即生成，將導致大批回溯補 PC，
故須於 `Climate Popups` 生成前有結論」。

**該顧慮之前提已被 35 §2 推翻**：`14.12` 不是缺一個軸，是**該句無法適用**
（「the hard controls」預設整車單一型態，而同一車上各控制型態不同）。

**既非軸，即無「軸未定而生成」之回溯風險。** 故：

- `Climate Popups`（42 leaf）**整組不再阻塞**
- 僅 `14.12` 自身之 leaf 停下，理由記為 DR #37 之三問未答
- 其餘節次照常生成

此為阻塞範圍之收窄，非新授權；**批次順序仍由本包 §2 定**。

---

## 2. 批次 10 —— `Airflow and Defrost`

| 項 | 值 |
|---|---|
| Test Set | `Airflow and Defrost` |
| 節次與各節 leaf 數 | **自 `framework.md` 導出，逐節列出**（48 §2）|
| tc_id | 續編 |

**選此批之理由**：

- **完成 ch2 家族**。`Climate Modes`（26/35）與 `Temperature and Fan`
  （19/19）已成，`Front Climate Anatomy` 14/16；本批完成後 ch2 之 92 leaf
  大致到位，**使 `ch2_ch7_mirror_map` 於其後之 `Rear Climate`（46 leaf）
  達到最大效用** —— 屆時對造多已有 TC，R-C36-1 之 TC 對 TC 比對可全面適用
- DR #31 僅卡其 2 leaf（`2.12`／`2.12.2` 之 PC），其餘不受影響
- 規模 23，小於 `Rear Climate` 之 46 與 `Climate Popups` 之 42

### 2.1 本批之已知交會點

- **`2.12`／`2.12.1`／`2.12.2` 與 `3.1` 為 sibling**（41 §2 所得，tri-mode 軸）
  —— `Tri-Mode Climate` 已成，故兩側皆有 TC，
  `pending-sibling` 之 `provisional` 列將到期，須逐對重新確認
- **第三軸已換為三值氣流模式集合**（32 §3）；DR #31 使 `2.12`／`2.12.2` 之
  PC 無法陳述其值。該二節停下，**不以推論補值**
- **`2.8`／`2.9`（defrost）與 `3.2`／`3.3` 已生成之節有交會** ——
  §8.2.1 之界線須具名，不得移植 3.x 之行為
- **`2.15`（mirror defrost）之條款標籤 `C16.` 與 `16.17` 撞號**
  （A-CF13 第一項）—— 引用一律以 outline 節次為鍵

### 2.2 照舊

R-C34 生成時義務、R-C36-1、R-C28 三問、「入口或操作方式未定義」檢查清單、
「對照關係未定義」檢查（52 §2）、stop-and-report 條件同前。

寫回依 46 §3：照常執行、標「範本容量待擴充」、**不送 Excel 確認**。

---

## 3. 進度與阻塞之現況（供上繳包對照）

| | 數 |
|---|---|
| 驗證單位 | 403 leaf |
| 已生成 | 依上繳 35 為 **139 leaf / 152 TC** |
| 停下 | 分屬 DR #6／#17／#20／#31／#32／#37 等 |
| Test Set 完成 | 6 / 15（`Seat Control Tab`／`Tri-Mode Climate`／`Temperature and Fan`／`ECO HVAC`／`ICS Anatomy`／`ICS Temperature and Fan`）|

**DR #35（範本容量）仍為交付之硬阻塞**，現 152 列而 102 列無下拉；
該項待 Pei 於 Excel 擴充，與生成無關，不阻塞本批。

---

## 4. 執行層作業指示

1. 依 §1 收窄 `Climate Popups` 之阻塞記載（本輪不生成該組）。
2. 執行批次 10（§2），節次與 leaf 數自 `framework.md` 導出。
3. 全批重跑 lint 與 §9 自評；寫回依 46 §3。
4. 上繳 `docs/upstream/36_batch10.md`。git 不執行。

---

## 5. 本包產生之新條文清單（自檢）

無新條文。
