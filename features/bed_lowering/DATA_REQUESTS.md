# DATA_REQUESTS — bed_lowering

規則：缺值欄位一律 `PENDING: DR-{n} <item name>`，不留空、不填 NA（IN §8.4.3）。
DR 之登記屬 Tier 1（執行層可自行 register）；草擬與送出決定屬 Pei。
每包上繳附本表未結列。

| DR | 項目 | 影響範圍 | 來源依據 | 狀態 | 送出日 | 結案日 |
|---|---|---|---|---|---|---|
| DR-1 | BLM operating speed threshold value（spec placeholder `*XX MPH`；owner: chassis engineering）| 7 條 PENDING 未寫回：B1 之 022-02/03/04、B2 之 007-03/04、B3 之 021-04/05。另各批 `provisional_inputs` 暫定車速待結案複驗 | SYS1 Outline 3.2.3 / 4.7.2 / 4.7.2.2 / 10.1.5（"Speed threshold to be defined by chassis engineering"）| **送出核准**（R-BLM15(4)）；**Pei 已送出 2026-08-27** | 2026-08-27 | |
| DR-2 | Off-Road 2 與 Easy Entry Mode 對應之 ride-height level 值（`ASCM_FD_1.*_Lvl` 物理值對映；owner: suspension calibration）| 2 條（041-01／041-02）：現以「highest／lowest reported value」書寫，查得對映後可收緊為具體值。**不阻斷交付** | 037 之 041-01/02 原文（`Off-Road 2`、`Easy Entry Mode`）；DBC VAL_ 僅 254/255，無模式列舉（上繳 11 §七-3）| 草案已登記（2026-08-27）；**Pei 已送出 2026-08-27** | 2026-08-27 | |
| DR-3 | Bed Lowering cluster graphics definition（最終圖形；owner: PDO）| 1 條 PENDING（033-04）**＋ 連動 2 條**（033-02／034-02 現以草稿 image5.png 為基準，PDO 完稿後須複驗）| SYS1 NRL-193740 逐字載 "Final graphics to be completed by PDO."；037 之 033-04 同 | 執行層登記（上繳 12）；分析層草擬 2026-08-27；**Pei 已送出 2026-08-27** | 2026-08-27 | |
| DR-4 | 三份 HMI_BP 指引文件：`HMI_BP_W-01`（label）、`HMI_BP_X-01_Hand_Anthropometry_A.Mar-6-2013`（手部人體計測）、`HMI_BP_L-34`（soft button）；owner: HMI 指引文件持有單位 | 4 條 PENDING（016-04／016-05／023-01／023-02）**＋ 連動 1 條**：017-05 引 X-01 但已判 coverage gap，取得指引後仍需人因試驗，不因本 DR 轉為可測 | 三份指引於全 repo 零命中（上繳 13）；037 之 016-04/05、023-01/02 逐字引其文件名 | 執行層登記（上繳 13）；分析層草擬 2026-08-27；**Pei 已送出 2026-08-27** | 2026-08-27 | |

---

## DR-1 結案動作清單（R-BLM16(4)）

門檻值回覆後 ——
1. B1 之 022-02／022-03／022-04、B2 之 007-03／007-04、B3 之 021-04／021-05 共 **7 條**之 PENDING 代入實值，補寫回（單位注意：規格為 MPH，DBC 訊號 `VehicleSpeedVSOSig` 為 Km/h，換算依回覆之單位與值，**不自行預換**）
2. 複驗暫定車速輸入：**各批 manifest 之 `provisional_inputs` 全數**（B1：022-01／027-05 之 5 Km/h；B2：1／2／10／15 Km/h 諸條；後續批同）—— 門檻若 ≤ 任一暫定值，該條語義翻轉，改值並 patch 已寫回列
3. 本表回填結案日

## DR-3 結案動作清單

最終圖形定義到位後 ——
1. 033-04 之 PENDING 代入基準，補寫回
2. **複驗 033-02／034-02**：其現行基準為草稿 image5.png，最終圖形若與草稿不同，該兩條之比對基準隨之改變，patch 已寫回列
3. 本表回填結案日

## DR-4 結案動作清單

三份指引到位後 ——
1. 016-04／016-05（W-01）與 023-01／023-02（L-34）共 4 條之 PENDING 代入具體判準，補寫回
2. **017-05 不因本 DR 而重新分流** —— 其不生成之理由為「取得指引後仍需實車人因試驗」，非「指引不在手」（`COVERAGE_GAPS.md` §判準-1）。若取得後發現 X-01 實為可目視比對之螢幕規則，則該判斷錯誤，需回頭重分流並修 `COVERAGE_GAPS.md`
3. 本表回填結案日

---

## DR-3 草擬（分析層，2026-08-27；送出待 Pei）

> 主旨：Bed Lowering — cluster 最終圖形定義索取
>
> 依據：SYS1 NRL-193740 與 037 之 SWE1-HMI-BLM-033-04 皆載
> "Final graphics to be completed by PDO"，現行文件僅附階段性參考圖
> （image5.png）。
>
> 索取項目：
> 1. Bed Lowering 啟動時 cluster 顯示之最終圖形定義（版本與發行日）
> 2. 該圖形與現行 image5.png 之差異說明（若有）
> 3. 圖形定義之後續變更是否另行通知之管道
>
> 用途：SWE.6 測試案例之比對基準。現階段 033-04 以
> `PENDING: DR-3` 佔位不出貨；033-02／034-02 以現行參考圖為基準，
> 最終圖形到位後將複驗。
>
> owner: PDO

## DR-4 草擬（分析層，2026-08-27；送出待 Pei）

> 主旨：Bed Lowering — HMI 最佳實務指引文件索取（三份）
>
> 依據：037 之 SWE1-HMI-BLM-016-04／016-05／023-01／023-02／017-05
> 逐字引用下列指引作為符合性基準，而該三份文件未隨規格包交付，
> 於本專案全數位存零命中。
>
> 索取項目（含版本與發行日）：
> 1. `HMI_BP_W-01`（label 相關）
> 2. `HMI_BP_X-01_Hand_Anthropometry_A.Mar-6-2013`
> 3. `HMI_BP_L-34`（soft button 相關）
>
> 用途：SWE.6 測試案例之符合性判準。現階段 016-04／016-05／
> 023-01／023-02 四條以 `PENDING: DR-4` 佔位不出貨；
> 017-05 已列為 coverage gap（其驗證屬實車人因試驗，
> 取得指引亦不轉為 HMI 可觀察行為）。
>
> owner: HMI 指引文件持有單位
