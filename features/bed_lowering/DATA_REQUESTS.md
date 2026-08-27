# DATA_REQUESTS — bed_lowering

| DR | 項目 | 影響範圍 | 來源依據 | 狀態 | 送出日 | 結案日 |
|---|---|---|---|---|---|---|
| DR-1 | BLM operating speed threshold value (spec placeholder `*XX MPH`; owner: chassis engineering) | 約 13 leaf：BLM-007-01~04、BLM-021-04/05、BLM-022-01~04 等，生成時逐列確認 | SYS1 Outline 3.2.3 / 4.7.2 / 4.7.2.2 / 10.1.5（"Speed threshold to be defined by chassis engineering"） | 送出核准（R-BLM15(4)，2026-08-26）；送出動作由 Pei 執行，送出日由 Pei 回填。B1 之 022-03 直接需要本值，未復前依 IN §8.4.3 落 PENDING | | |
| DR-3 | Bed Lowering cluster graphics definition（最終圖形；owner: PDO）| 1 leaf：BLM-033-04（033-02 以現行參考圖為基準，不受影響）| SYS1 NRL-193740 逐字載 "Final graphics to be completed by PDO."；037 之 033-04 亦寫 "to be completed by PDO" | **執行層登記（上繳 12），草擬與送出待分析層／Pei** | | |

規則：缺值欄位一律 `PENDING: DR-{n} <item name>`，不留空、不填 NA（IN §8.4.3）。DR 由 analysis 層起草，Pei 決定送出。每包上繳附本表未結列。

| DR | 項目 | 影響範圍 | 來源依據 | 狀態 | 送出日 | 結案日 |
|---|---|---|---|---|---|---|
| DR-2 | Off-Road 2 與 Easy Entry Mode 對應之 ride-height level 值（`ASCM_FD_1.*_Lvl` 物理值對映；owner: suspension calibration） | 2 條（041-01／041-02）：現以「highest／lowest reported value」書寫，查得對映後可收緊為具體值；不阻斷交付 | 037 之 041-01/02 原文（`Off-Road 2`、`Easy Entry Mode`）；DBC VAL_ 僅 254/255，無模式列舉（上繳 11 §七-3） | 已登記（草案，2026-08-27），未送出；送否由 Pei 決 | | |

**DR-1 結案動作清單（R-BLM16(4)）**：門檻值回覆後 ——
1. 022-02／022-03／022-04 之 PENDING 代入實值（單位注意：規格為 MPH，DBC 訊號 `VehicleSpeedVSOSig` 為 Km/h，換算依回覆之單位與值，不自行預換），三條補寫回
2. 複驗暫定車速輸入：**各批 manifest 之 `provisional_inputs` 全數**（B1：022-01／027-05 之 5 Km/h；B2：1／2／10／15 Km/h 諸條；後續批同）—— 門檻若 ≤ 任一暫定值，該條語義翻轉，改值並 patch 已寫回列
3. 本表回填結案日
