# 入庫歸屬更正 —— 21 輪產物

**不改寫歷史；本檔為事後說明（Pei 於 2026-08-22 指定採此處置）。**

## 事實

21 輪（`docs/upstream/19_writability_refined.md`）之全部產物，
**實際入庫於 `1f95205`**，而該 commit 之訊息為：

```
1f95205  feat(time_management): package 09 — single-source tc_id format, DR-8/9/10
```

**訊息與內容不符** —— 該 commit 同時含兩個 feature：

| 範圍 | 檔數 |
|---|---:|
| `features/time_management/` | 7（該 session 自身之工作） |
| **`features/vehicle_setting/`** | **12（21 輪之全部產物）** |

## 21 輪之 12 個檔案（實際落於 `1f95205`）

```
features/vehicle_setting/ANOMALIES.md                          （A-VS69 關閉、A-VS70/71/72 新開）
features/vehicle_setting/RULINGS.md                            （R-VS43 轉錄）
features/vehicle_setting/docs/handoff/40_review_round20.md
features/vehicle_setting/docs/upstream/19_writability_refined.md
features/vehicle_setting/docs/reports/generatable.tsv          （新，237 列）
features/vehicle_setting/docs/reports/writability.tsv          （改，增 derivable / quoted_form_risk 兩欄）
features/vehicle_setting/data/_w59_anchors.json
features/vehicle_setting/data/_w59_rows.json
features/vehicle_setting/data/_w59_rvs43.json
features/vehicle_setting/data/_w59_split.json
features/vehicle_setting/data/_w61_quoteform.json
features/vehicle_setting/data/_w61_still.json
```

**內容完整，未遺失。**

## 成因

執行層之 21 輪 commit **未執行** —— 其 `git add` 完成後、`git commit` 之前，
另一 session（time_management）以**無 pathspec 之 add**（`git add .` 或 `git commit -a`）
將暫存區內之 `features/vehicle_setting/` 檔案一併帶入其 commit。

執行層隨後之 `git commit -- features/vehicle_setting/` 得
`nothing to commit, working tree clean`。

**同型事件先前發生過一次**（Power feature，`tc-generator-6b` 之 `4d623ef`）。

## 處置

Pei 裁定採「**不改寫歷史，補一筆說明**」。
`1f95205` **不動**（其時尚未 push，惟改寫將影響另一 session 之工作）。

## 往後之防護與其界線

執行層之提交一律帶 pathspec（`git commit -- features/vehicle_setting/`），
**惟該措施只約束本 session** ——
**擋不住他 session 之無 pathspec `add`**，因暫存區為 repo 層級共用。

真正之防護須為：各 session 於 `add` 時亦帶 pathspec。**此非執行層可單方保證。**
