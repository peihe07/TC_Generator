# 下放包 07 — vsm_v43：P4 pilot —— Interior Ambient Lighting（10 leaf）暫代生成

日期：2026-09-02
取號：`docs/handoff/` 實測有 00–06，取 07
對象：執行層。00–06 包續有效。台帳不重生；DR 不代發；不寫工作簿、不寫 delivered/。
依據：R-VT18（暫代母體＋重錨條款）、R-VT19（Layer 2 十六組鎖定；pilot 提案未改指即用）。
生成規約**全面沿用 vsm_v42 下放包 05 §零～§二之 W-2 契約**（IN §2–§13＋profile＋R-VL21 覆核教訓），本包只載 V43 差異。

---

## 一、V43 差異條款

1. **母體**：`data/leaves_interim.tsv` 之 `chapter_for_vf = 01.11.01.01.26` **10 列**；一 SYSRA 列＝一需求單位（R-VT18(d)，不分解不合併；§8.2.2 一列得多 TC）。
2. **test_item 上半 verbatim 來源**＝該列 `Description` 逐字（`_x000D_`→空白；>50 token 摘句，R-3）；下半 `(...)` 照 R-S4。
3. **D 欄**＝`Sys-RA-VF665_V43_VSM-{nnn}`；**Remarks 逐列**＝`Provisional: SYSRA-anchored (R-VT18); re-anchor upon 037 (DR-VT1)`（另有他註以 `; ` 續於其後）。
4. **spec_reference**：先做 **W-A 章節對應實測**——自 `sources/raw/vf665_v43_spec_r4` 之 docx 標題（V42 W-8 同法：styles outline）查 `1.11.1.1.26` 一節之標題是否為 Ambient/Interior Ambient Lights；**逐字驗證成立**→每 TC 寫兩行（spec 錨 `Vehicle_Setup_Management_…_VF665_V43_R4_{章節號}` 在前、Sys-RA 錨在後，R-VT19(b)）；不成立→只寫 Sys-RA 錨，對應結果上繳。
5. **訊號**：v5 事實表；解得者 `$…$`＋label 取 `val_tables_v43.tsv`；內部訊號（`Ambient_Lighting_level_Setting.Req`、`TLM_Vehicle_Setup_Menu.Info` 等）→ UI／PROXI 路徑可走者走（R-P375(b)，HMI 錨見 v5 備註），否則 `PENDING: DR-VT4 <名>`。PROXI 條件（`Ambient_Lighting_Function`／`Ambient_Dimmer_Switch`）入 Pre-Condition。
6. **R-VL21 教訓前置適用**：DUT 送出之 ER 用 `is received` 式（bus-error 式限測試員送出步）；回饋型 TC 先建請求態再注入；不可觀察之內部計時不入 ER；UI 名取規格具名（來源入 remarks）。
7. **E 系列**：沿 V42 E38–E45 同判準（編號同名），另加 **E51**：Remarks provisional 註 10/10 齊；**E52**：W-A 對應結果明判（成立／不成立，逐字引標題）。

## 二、W 清單

W-A 章節對應實測（§一-4）→ W-B 生成 10 leaf 至 `generated/b1_ambient/`（md＋json＋INDEX，契約同 V42）→ W-C §9 自檢＋E38–E45／E51／E52 → W-D **E40 詞界重算**（v5 訊號名以詞界比對重掃 295 列之含訊號／含解得二數，取代子串上界；供交付說明之 43% 修正值）。

## 三、上繳（`docs/upstream/07_pilot_ambient.md`）

W-A 逐字證據；b1_ambient 全量；E 逐項；PENDING 清單；§K；W-D 新舊二數並列；獨立判斷；gate_all 歸因。

## 四、升級條件

同 V42 05 包 §五；另：W-A 若需語意猜測方能對應（列不成立，不猜）；任何 TC 之 D 欄非 Sys-RA 實名。

## 五、未結 DR

DR-VT1（Pei 裁送出待發）／DR-VT2（建議併送）／DR-VT3 暫持／DR-VT4（先不送；本批內部訊號 PENDING 錨）。
