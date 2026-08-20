# 00E 待辦總表 — 缺什麼、等誰、何時回報

分析層寫入，2026-08-20，同一往返（NN = 00）。
00／00A／00B／00C／00D 五篇之結論在數處互相修正，**本篇為現行有效之
單一清單**；與前四篇衝突時以本篇為準，前四篇保留作為證據與追溯。

---

## 1. 還缺的文件 —— 只剩一項半

| 項 | 內容 | 誰 | 沒有它會怎樣 |
|---|---|---|---|
| **5-A** | `Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf` 自 `…/26PI2.5/HMI/` 複製入 `features/vehicle_setting/inputs/` | **Pei（Tier 3：素材補入）** | 16 個 leaf 之按鍵循環、LED 數、highlight 狀態寫不出可觀察 ER |
| **5-B** | 失效彈窗內容 + 加熱方向盤圖示之左右駕鏡像 | **上游（RD-1，Tier 3 送出）** | 該部分 ER 只寫到訊號層，畫面層標 BLOCKED |

**其餘全部到位**：CFTS044 原始二進位、SYS3 原始二進位、四份 037、SYS2、
036 母本、兩份 DBC —— 共 12 檔已在 `inputs/`（00C §1）。

**已作廢之請求**（曾列而經實測撤回，留痕以免重提）：

- ~~CAN 訊號字典~~ —— 29/30 個 `$var$` 之值域在 CFTS044 內，餘一由 DBC 給出
- ~~`$HSW_StatFailSts$` 外部來源~~ —— 誤判，見 00B §0
- ~~Pop Up List／HMI Settings List／Market Configuration~~ —— CFTS044 不引用
- ~~PDO 圖形（已入之兩檔）~~ —— 內容不符，見 00C §3

---

## 2. 等 Pei 裁的 —— 四項，都不是文件問題

| 編號 | 待裁 | 阻塞範圍 | 分析層建議 |
|---|---|---|---|
| **R-VS7** | Comfort 之 43 個重疊 leaf 之委派界線（三選項見 00A §3） | 座椅／方向盤加熱之全部 TC | (a) 分層委派 |
| **R-VS8** | **基線 DBC**：`PDT27_E2A_R4_BHCAN` 或 `R5_FDCAN8`。`HSW_StatFailSts` **只存在於 R4** | 16 個 leaf 之訊號斷言 | R4 為主、R5 為 FD 補充；兩份並存並於 profile 載明分工 |
| **R-VS9** | **CAN 訊號之書寫形式**：`$HSW_Stat$` 在匯流排上實為 `HSW_StatSts`、`$PowerMode$` 實為 `PowerModeSts` | 全部含訊號之 Procedure／ER | 引用訊號時以 DBC 逐字 signal 名 + message 名為準；`$var$` 僅出現於 test_item 上半段之來源逐字 |
| **R-VS10** | **Pop Up List 基線版本**：26PI 版較 Comfort／User Profiles 交付所用之 SR24 Post 2A (Dec 15 2023) 新（A-VS09） | popup 文字一致性 | 本 feature 條文不引 Pop Up List，暫不採用；若 5-B 有答覆再議 |

**R-VS7 與 R-VS8 阻塞生成**；R-VS9 阻塞 lint 規則定稿；R-VS10 目前不阻塞。

---

## 3. 已可解除之阻塞

| 原阻塞 | 狀態 |
|---|---|
| R-VS2(c)：`specification_reference` 之末段形式 PENDING | **解除** —— 章節號自 CFTS044 樣式階層取得，245/271 leaf 已解析（00C §2.2） |
| DR-1／DR-3：原始二進位與素材落地 | **關閉** |
| DR-4／DR-4b：變數值域與訊號讀取途徑 | **關閉** |

---

## 4. 回報契約 —— 什麼會停下來問，什麼不會

### 4.1 會停下來、升級 chat 覆核（`00` 包 §7 之現行版）

1. 實測與下放包 §5.2 之預期數字**任一項不符**（不自行調和）
2. 錨鏈（leaf → SYS-RA → SYS2 → 7 位數 → 章節）在**任一 leaf 上不成立**
3. W-9 之 43 個重疊 leaf 逐條清單完成 → **必停**，等 R-VS7
4. 撞到 §8.4.1 之編造壓力（來源未述之值、門檻、時間、順序）
5. 需要判斷而 canon／profile／本包皆無條文
6. write-back invariant 違反（本階段尚未到寫回，但條列保留）
7. 036 母本結構與 `forms/…_SWQT_20260817_ext.xlsx` 不一致

### 4.2 不問，逕行執行並於上繳包揭露（Tier 0／1）

- 量測與掃描條件之技術選擇（`zipfile` vs `openpyxl`、正則 vs 詞庫）
  —— **惟選擇改變結論時，該改變本身升級**
- 批次邊界與排序、anomaly 之登記與分類（**登記不等於裁定**）
- 衍生檔重建（outline map、leaf 表、sibling map、batch context）
- 工作簿欄位字串與 framework 表之逐字照抄

### 4.3 節奏

- **一批一上繳，前批未覆核不得開下批**
- 每次上繳必附「**本包是否仍有該驗而未驗者**」之獨立判斷
- 四道 gate 依序：recon → pilot → coverage audit → DV。
  **pilot 是唯一必須人工的那道**（canon §1.1）

---

## 5. 接下來三步

| 步 | 動作 | 誰 | 前置 |
|---|---|---|---|
| 1 | `new_feature.py "Vehicle Setting" --adopt-existing`；`INPUTS.sha256`；W-2～W-8、W-12 | 執行層 | 無（12 檔已到位） |
| 2 | W-9：43 個重疊 leaf 逐條對照表 → **停，等 R-VS7** | 執行層 → Pei | 步驟 1 |
| 3 | **W-13**（00D §6 新增）：對 `…/26PI2.5/HMI/` 全部 PDF／XLSX 跑 `Fail_Present`／`STATFailSts`／`Heated Steering Wheel Icon` 全文掃描，以餘數驗證「失效彈窗不在該目錄」之結論（R-G10） | 執行層 | 無，可與步驟 1 並行 |

**步驟 1 與 3 可並行**，不必等任何裁定。
**步驟 2 之後才會出現第一批 TC。**

W-13 之意義：00D 只逐份開了 4 檔、另有 108 檔未開，該結論目前是
**「已知未查」而非「已查為綠」**。W-13 把它轉成後者，或推翻它 ——
兩種結果都比現在好。
