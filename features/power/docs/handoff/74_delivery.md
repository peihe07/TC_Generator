# 74 — Pei 裁乙：出貨；DR 發送包

下放包 | 分析層 → 執行層 | 往返 NN = 74

前置：Pei 2026-08-30 逐字「出貨吧 我送」。
分析層讀為：S6 例外由 Pei 開啟（= 59 包 §K-2 之**乙**：整本寫回交付，含 PENDING 之列原樣保留並附清單），
七張 DR 由 Pei 親送。此為 Tier 3 之明文裁定，取代 R-P398(a) 之甲。
73 包 G257 未回報者，本包 §H 第 1 步先完成再出貨。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P399] S6 例外：Pei 裁乙，整本寫回交付，PENDING 列原樣保留並附清單；DR 由 Pei 送。
         （a）R-P398(a) 之甲作廢。工作簿全 287 條寫回交付，`PENDING: DR-PW{n} <名>` 佔位原樣保留，
              **不降轉 NA、不刪列、不隱藏**
         （b）交付附件二份：
              ① `PENDING_LIST.md`：146 條逐列 tc_id／欄位／DR 號／缺件名，依 DR 分組，供上游回覆後逐條結案
              ② `DR_DISPATCH.md`：七張 DR 全文（英文，附影響 tc_id 與 CFTS 錨點），供 Pei 直接發送
         （c）交付說明（Remarks 或 Cover 之 QS Suggestion 分頁）記：「146 列待上游資料，見 PENDING_LIST」；
              丁案三條與 R-P376(d) 之未驗證性質同記
         （d）寫回基底 = 73 包 G257 後之 corpus；三代對照表（含 §8.3 拆分四條）隨附為 TestRail 舊→新 ID 對照
         （e）S6 條文不改；本次為 Pei 明文之個案例外，Remarks 於 Cover 記「S6 例外，Pei 2026-08-30」
         裁決者 Pei，逐字依據：「出貨吧 我送」。
```

## B. 出貨清單（DELIVERY_CHECKLIST 對照）

1. 73 包 G257 全跑歸零，`sandbox/b73/pm_73.xlsx` 生成，六閘＋G256＋G257 表附
2. `lint_docs036` 全 PASS；`ledger_guard` exit 0；`ledger_xref` 無矛盾
3. 位元組複製 `pm_73.xlsx` → `delivered/pm_73.xlsx`；`delivered/MANIFEST.tsv` 新增一列（SHA、來源、`74 包 R-P399`、`S6 例外 Pei`）
4. `PENDING_LIST.md`、`DR_DISPATCH.md`、`tcid_three_gen_73.tsv` 落 `delivered/`
5. 交付檔名：`FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_PowerManagement_20260830.xlsx`，
   目標夾 `10_Reviewing/00_TestCase/ASW-R2/Power Management/`——**複製由 Pei 執行**（Tier 3，git／交付操作）
6. Excel GUI 開啟驗證——Pei 手動項
7. ⚠ 該夾內 `_20260824.xlsx` 為第一代 pm_29（390 列），日期新於第三代 `_20260820.xlsx`；
   **是否移除由 Pei 定**，執行層不動

## H. 作業指示

1. 完成 73 包 §H 全部，出 `73_g257.md` 上繳（可併入本包上繳）
2. 抄 R-P399；R-P398(a) 加註作廢
3. §B 第 1–4 步
4. 上繳 `features/power/docs/upstream/74_delivery.md`，附全閘表、MANIFEST 列、二附件之 `get_file_info`
5. 第 5–7 步交 Pei

## I. 禁區

沿用 73 包 §I，另增列：不得降轉 NA（R-P399(a)）；不得複製至客戶夾（Tier 3）；不得動 `_20260824.xlsx`。

## J. 自檢

一條。對既有 canon：S6 — (e) 明示為 Pei 個案例外，條文不改；R-P374(a)／R-P398(a) — 作廢，加註；R-P349(c) — (d) 三代對照表隨附；R-P376(d) — (c) 代價入交付說明；DELIVERY_CHECKLIST — §B 逐項對照。

## K. 待 Pei

1. §B 第 5–7 步（複製至客戶夾、Excel 驗證、`_20260824` 去留）
2. `DR_DISPATCH.md` 生成後發送七張 DR
