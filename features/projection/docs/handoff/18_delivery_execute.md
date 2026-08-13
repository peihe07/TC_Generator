# 下放包 — Projection：交付形式裁定與送達執行

> 交付對象：Claude Code
> 觸發：Pei 裁定交付物為 `NR1L_GEN1(HDCC)_Ver_20260813.xlsx` 本身
> 授權層級：Tier 1（`output/` 落地）+ Tier 3 已授權（送達）
> 日期：2026-08-12

---

## 0. 裁定

> **R-P92｜交付形式**
> 本 feature 之交付物為 **`NR1L_GEN1(HDCC)_Ver_20260813.xlsx` 本身**，不轉為 FM-WI-FSM-036 表單。
>
> 依據：Pei 裁定（2026-08-12）。
>
> **連帶認定**：
> 1. profile §6 所記「本專案之 workbook 並非 FM-WI-FSM-036 表單實例（欄位配置自 F 欄起與其他 feature 差一格）」為**事實記載**，不構成交付障礙。本 feature 之交付形式與其他 feature 不同，屬 `FULL_REFINE` 型 feature 之特性——修訂既有工作簿者，其交付形式即該工作簿之形式。
> 2. 客戶審查目錄內之 `FM-WI-FSM-036-A01 …_SWQT_Projection_20260623.xlsx`（369 KB）為**不同文件，不在本專案範圍內**，任何步驟皆不得觸及（R-P91）。
> 3. 檔名維持 `NR1L_GEN1(HDCC)_Ver_20260813.xlsx` 不變——版本識別由 SHA256 承擔，不由檔名承擔。

---

## 1. 送達為兩步

### 步驟 1｜`output/` 落地（Tier 1，逕行）

比照 AMFM 前例（`output/FM-WI-FSM-036-A01 …_SWQT_CFTS024_Radio_20260129.xlsx` + `.sha256` 成對）。

```
來源  /Users/peihe/Work_Projects/TC_Generator/features/projection/inputs/NR1L_GEN1(HDCC)_Ver_20260813.xlsx
目標  /Users/peihe/Work_Projects/TC_Generator/output/NR1L_GEN1(HDCC)_Ver_20260813.xlsx
旁檔  /Users/peihe/Work_Projects/TC_Generator/output/NR1L_GEN1(HDCC)_Ver_20260813.sha256
```

**旁檔格式須與 AMFM 前例一致**——先讀 `output/FM-WI-FSM-036-A01 …_Radio_20260129.sha256`（193 B）確認其格式（檔名欄位、是否含額外欄位、換行慣例），**逐字比照**，不自訂格式。

驗證：
```
output/ 之 xlsx SHA256 == b16debb7bc609e39…
output/ 之 xlsx size   == 574,700 bytes
旁檔內容與實測 hash 相符
```

> **R-P93｜交付物之 hash 旁檔**
> 交付物一律成對產出 `<檔名>.sha256` 旁檔。
> 依據：`inputs/` 與 `output/` 皆受 `.gitignore` 排除（客戶檔案政策），交付檔本身不入版本歷史；**旁檔為文字檔，可入庫，是交付版本與版本歷史之間唯一的可追溯連結**。
> 旁檔須入庫，`.gitignore` 之排除規則須確認不涵蓋 `*.sha256`（AMFM 前例中該旁檔存在於 `output/`，須確認其追蹤狀態）。

### 步驟 2｜送達客戶審查目錄（Tier 3，Pei 已授權）

前置驗證已於前包通過：交付位置現有檔案 SHA256 `11579c9b3b8e56eb…` == Phase 0 基準，未被他人修改。

```
1. 備份交付位置現有檔案
   目標 features/projection/backup/NR1L_GEN1(HDCC)_Ver_20260813.delivery-target.<ISO8601>.bak.xlsx
   驗證 備份 SHA256 == 11579c9b3b8e56eb… ，size == 572,672

2. 以逐字絕對路徑複製（R-P91）
   來源 /Users/peihe/Work_Projects/TC_Generator/features/projection/inputs/NR1L_GEN1(HDCC)_Ver_20260813.xlsx
   目標 /Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/CP:AA:iPod/NR1L_GEN1(HDCC)_Ver_20260813.xlsx

3. 驗證交付位置
   SHA256 == b16debb7bc609e39…
   size   == 574,700 bytes

4. 不符即以第 1 步備份還原，驗證還原後 SHA256 == 11579c9b3b8e56eb…，回報
```

⚠️ **目標路徑逐字比對後方得執行**（R-P91）。同目錄之 `FM-WI-FSM-036-A01 …_SWQT_Projection_20260623.xlsx` 與 `~$FM-WI-FSM-036-A01 …_20260511.xlsx` 皆不得觸及。

⚠️ **執行前確認該檔未被 Excel 開啟**（同目錄存在鎖定殘留檔 `~$…`，顯示該目錄曾有開啟中之檔案）。若目標檔正被開啟，複製可能失敗或產生損毀檔——**先檢查是否存在 `~$NR1L_GEN1(HDCC)_Ver_20260813.xlsx`，存在即停下回報**。

---

## 2. 送達後之驗證

送達完成後，**四處之 SHA256 須一致**：

| 位置 | 期望 SHA256 |
|---|---|
| `features/projection/inputs/` | `b16debb7bc609e39…` |
| `output/` | `b16debb7bc609e39…` |
| `output/*.sha256` 旁檔內容 | `b16debb7bc609e39…` |
| 客戶審查目錄 | `b16debb7bc609e39…` |

任一不符即停下回報，不自行調和。

---

## 3. tag annotation 定稿

`fw036-projection-refine-v1`，annotation 全文須含：

```
Projection FULL_REFINE delivery

交付檔    NR1L_GEN1(HDCC)_Ver_20260813.xlsx
SHA256    b16debb7bc609e39044803760171cf1d2b583fd1…
size      574,700 bytes
基準檔    11579c9b3b8e56eb…（Phase 0 落地版本）

交付位置
  output/NR1L_GEN1(HDCC)_Ver_20260813.xlsx
  /Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/CP:AA:iPod/NR1L_GEN1(HDCC)_Ver_20260813.xlsx

交付檔不在版本歷史中（inputs/ 與 output/ 依客戶原始檔政策排除）。
本 tag 之樹不含交付檔；交付版本以上列 SHA256 綁定，
並以 output/NR1L_GEN1(HDCC)_Ver_20260813.sha256 旁檔入庫追溯。

內容
  資料列   559 → 565（刪 r562、補 7 條）
  覆蓋     165/171 leaf
  變更     既有 63 列 + 授權例外 76 列（ER 6 / Author 40 / Remarks 30）
  裁決     R-P1 ~ R-P93
  異常     A-PJ01 ~ A-PJ74
  OPEN DR  #1 #2 #8 #9 #10 #11 #12 #13 #15 #16 #17 #18 #19
```

OPEN DR 清單須自 `DATA_REQUESTS.md` 之現行記載取得，**不得沿用本包之列舉**（canon §5a 第十五條）。

**tag 由 Pei 執行。**

---

## 4. 上繳要求

1. AMFM 旁檔格式之逐字確認結果
2. 步驟 1 之 `output/` 落地驗證（xlsx SHA256、size、旁檔內容）
3. 步驟 2 之送達驗證（備份路徑與 SHA256、送達後 SHA256 與 size）
4. §2 之四處 SHA256 一致性驗證
5. `.gitignore` 是否涵蓋 `output/*.sha256` 之確認（R-P93）
6. tag annotation 全文（OPEN DR 自 repo 取得）
7. 前包 §9 第 2~6、8 項之產出（若尚未完成）

---

## 5. 本包產生之新條文清單（A-PJ53 要求）

| 編號 | 形式 | 位置 |
|---|---|---|
| R-P92 | 可貼區塊 | §0 |
| R-P93 | 可貼區塊 | §1 |

落檔：R-P92 / R-P93 → `DECISIONS.md §0.26`。

**不 commit。**
