# 26 — Comfort HMI / 寫回覆核 ＋ 三項待補檢查

- 產出層：分析層｜2026-08-15｜對象：執行層
- 覆核對象：`docs/upstream/16_writeback.md`
- Pei 確認：2026-08-15「xlsx 沒問題」= profile §0.1 四項全數通過
- 判定：**寫回通過，pilot 閉環。**

---

## 1. 覆核 PASS

前置 gate 5 項、寫回後 assertion 9 項全 PASS，且全數自產出檔讀回而非自
記憶體。產出 `…_Comfort_20260815_pilot.xlsx`，SHA256 `b4ad82c2487a38c0…`。

**兩端俱備**：程式層（zip member 48、DV counts 不變、196 格逐欄比對、
B 欄公式原樣、BLOCKED 兩列 L/M 為空）與 Excel 自身之檔案完整性判定。

`DELIVERY.sha256` ENTRY 002 之狀態欄改為
**`Excel-confirmed by Pei 2026-08-15（四項）`**；hash 與內容不得變動
（append-only）。

## 2. 三處自行加嚴，全數採納

- **assertion 3 之 sheet 編號改為解出而非寫死** —— 寫死者於範本改版時會
  無聲通過
- **assertion 4 由 12 欄擴為 14 欄（加 S 與 AH）** —— 診斷正確：AH 原本只受
  assertion 8 覆蓋，而該項只檢 BLOCKED 兩列之首 60 字元，
  **其餘 12 列之 Remarks 全文從未與 JSON 比對過**
- **`--verify-only` 而非放寬 gate 2** —— 「放寬 gate 使重跑無聲可行，
  而重跑之風險正是台帳要防的」判斷正確

## 3. A-CF16 之補登 —— 自報屬實

上繳 14／15 使用該編號而 `ANOMALIES.md` 從未登記。與「A ruling not written
to the repo did not happen」同源：**在往返包裡用了一個編號，與該編號存在，
是兩件事。**

---

## 4. 三項待補之檢查 —— 全數授權

| # | 來源 | 內容 |
|---|---|---|
| 1 | 16 §11.2 | **JSON key 覆蓋**：JSON key 集合減去 `COLS` 值域，須完全落在具名之「不入表」白名單內。現行 `COLS` 是人工清單，漏一欄不會有人喊 |
| 2 | 16 §11.5 | **anomaly 編號登記**：掃 `docs/upstream/*.md` 與 `docs/handoff/*.md` 之 `A-CF\d+`，凡未見於 `ANOMALIES.md` 者即報。R-C13 同源 —— 引用不存在的編號是靜默失敗 |
| 3 | 16 §11.3 | **assertion 9 之掃描窗**由固定 24–35 改為至 `max_row` |

白名單初值（第 1 項）：`tc_title`（canon §4.3 推導用，不入表）、
`estimated_test_time`（無對應欄）、`reasoning`、`keywords`、`duplicate_of`、
`distinguishing_axis`、`split_flag`、`split_reason`。
**增列須經裁定** —— 同 R-C26 之理：可自行增列之白名單等於沒有白名單。

三項皆須反向驗證。

---

## 5. 本包產生之新條文清單（自檢）

無新條文。§4 為既有 §10 與 R-C26 之落實。
