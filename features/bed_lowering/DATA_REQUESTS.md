# DATA_REQUESTS — bed_lowering

| DR | 項目 | 影響範圍 | 來源依據 | 狀態 | 送出日 | 結案日 |
|---|---|---|---|---|---|---|
| DR-1 | BLM operating speed threshold value (spec placeholder `*XX MPH`; owner: chassis engineering) | 約 13 leaf：BLM-007-01~04、BLM-021-04/05、BLM-022-01~04 等，生成時逐列確認 | SYS1 Outline 3.2.3 / 4.7.2 / 4.7.2.2 / 10.1.5（"Speed threshold to be defined by chassis engineering"） | 送出核准（R-BLM15(4)，2026-08-26）；送出動作由 Pei 執行，送出日由 Pei 回填。B1 之 022-03 直接需要本值，未復前依 IN §8.4.3 落 PENDING | | |

規則：缺值欄位一律 `PENDING: DR-{n} <item name>`，不留空、不填 NA（IN §8.4.3）。DR 由 analysis 層起草，Pei 決定送出。每包上繳附本表未結列。
