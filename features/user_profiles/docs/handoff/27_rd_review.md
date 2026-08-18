# 27 下放包 — RD 查詢單之三處修正（寄出前）

**本包無裁決條文。** 26 輪上繳**核可**，惟 `26_rd_queries.md` 為**對外文件**，
其精確度之標準高於內部包 —— 以下三處須改後方可送 Pei 寄出。

## 先記兩處做得好的

1. **送出門檻**：執行層把「為何續送」由「leaf 存在」收緊為
   **「答案會改變已生成之內容」** —— 這是可檢驗的門檻，
   比「這題重要」穩固得多。我 26 包沒寫到這一層。
2. **A-UP02 不逕行關閉記載之理由**：若日後 037 補上那些 leaf，
   這份實測（內容存在、可讀、位置已定）就是現成對照 ——
   **關掉它等於把量過的東西再量一次**。

## 對外文件之三處修正

### X-1（必改）附錄之 seven 與表列 4 條不符

附錄開頭寫 `**seven** leaves ... have Title values that are displaced`，
其下表只列 **4 條**（`125-03`／`125-04`／`126-01`／`126-02`）。

收件者會數到 4 而讀到 seven。**對外文件內兩處數字不符，會被讀成我方沒查清楚。**

**改**：列出全部七條，或明寫 `four of the seven are shown below`
並具名其餘三條之 leaf id。**擇一，不得留現狀。**

### X-2（必改）`shifted by one position` 是未經證明之模式描述

附錄寫 `the titles appear **shifted by one position** across the group`。

而其下四列之對應關係並非一致之 +1 位移：

| leaf | Description 之主題 | 其 Title 所述 |
|---|---|---|
| `125-03` | 狀態列互動限制 | 手套箱**提示**（= `126-01` 之 Description）|
| `125-04` | 全部不可互動項變灰 | 手套箱按鈕**變灰**（= `126-02` 之 Description）|
| `126-01` | PU0832 提示 | 鎖定特定選單區（≈ `125-02` 之 Description）|
| `126-02` | 手套箱按鈕變灰 | 狀態列限制與變灰（≈ `125-03` 之 Description）|

**這是錯置，未必是等距位移。** 主張一個模式而未證明它，
若對方逐條核對後發現不是位移，整份附錄的可信度會一起掉。

**改**：刪去 `shifted by one position`，改為中性之
`displaced relative to their descriptions`（事實），
**模式之描述若要保留，須先以七條全量證明其為位移**。

### X-3（建議）文件識別應同時給檔名與 Source ID

現寫 `Personal Account HMI Logic and Flow **R1L-R (February 10 2023)**`。

而 037 全篇引用之 Source ID namespace 為
`Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_**CR24798_(October_03_2023)**`。

**同一份文件，兩個識別**（R-U3 已裁其為同一 namespace）。
收件者多半以 CR 號與日期認件；只給檔名之 R1L-R／Feb 2023，
可能被誤讀為**我方拿的是舊版**，而那正是本 feature 01–03 輪花了三輪釐清的事。

**改**：兩個識別並列一次，並註明其為同一 artifact
（如 `filename: … R1L-R (February 10 2023); SYSRE_HMI Source ID namespace:
… CR24798 (October 03 2023)`）。

## 作業

1. X-1／X-2 依上改；X-3 依建議改（不採則具名理由）
2. 改後之 `26_rd_queries.md` 重出，**版本標於檔首**
3. **ch4 第三批取樣清單** —— 25 包作業 B、26 包作業 6 所列。
   本層讀至 `26_scope.md` §4 未見；若已在該檔之後段，指明節次即可，
   **未出則本輪補出**（先回報，不生成）
4. 全閘重跑不需重做，僅回報改動之檔

## 不在本包授權範圍

- 任何寫入性 git（R-G5／R-G12）
- 寄出 RD 查詢單 —— **Tier 3，屬 Pei**
- 寫回工作簿（R-U14）
- 第三批之生成 —— 待取樣清單覆核

## 上繳

`docs/upstream/27_rd_queries_v2.md`（改後之對外文件）
＋ `docs/upstream/27_batch03_sample.md`（若 ch4 清單尚未出），
更新 `docs/INDEX.md`，附獨立判斷。
