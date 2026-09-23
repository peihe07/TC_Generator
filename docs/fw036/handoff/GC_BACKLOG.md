# GC_BACKLOG —— 跨 feature／全域待辦登記簿

各 feature 線在作業中遇到、但**不屬本線職責**（須改 canon、全域 ledger、
全域生成器或他 feature 之檔）之事項登記於此，由 GC 線排程處理。
登記不等於授權：處理仍須各自之下放包。

格式：`| # | 事項 | 來源 | 影響 | 急迫 | 狀態 |`

---

## 由 Camera 線登記（CAM-02／CAM-03，2026-09-16）

| # | 事項 | 來源 | 影響 | 急迫 | 狀態 |
|---|---|---|---|---|---|
| GCB-01 | **`gates_tsv.py` 讀 `FEATURE_CHECKS` ＋ 重生 `docs/runtime/GATES.tsv`** —— `scripts/gates_tsv.py:185-186` 之閘登錄只列舉 `CHECK_ORDER` 與 `PROFILE_CHECKS`，故 CAM-02 新增之 feature 專屬檢查 `Z`（Vehicle Model 七欄 1/0，R-CAM2）不在閘登錄簿內 | CAM-02 上繳 §3.5；CAM-02 審閱 §三-3 | R-G56 之閘登錄不完整；**Camera 交付前必須完成**，Phase 3 生成不受阻 | 中 | OPEN |
| GCB-02 | **`FEATURE_CHECKS` 機制之全域條文** —— 「feature 專屬 lint 代號」之機制目前只存在於 `scripts/lint036.py` 之模組層與 Camera profile §2，無全域條文 | CAM-02 審閱 §三-4（Pei 准，指定補記於 `docs/fw036/RULINGS_LEDGER.md` 待登項） | 他 feature 日後如法炮製時無條文可引 | 中 | OPEN |
| GCB-03 | **9 個既有測試失敗** —— 皆他線，Camera 不動：<br>(a) `tests/test_single_write_path.py` 2 項：15 個腳本直呼 `openpyxl.save` 而未入 grandfather 名單（`features/time_management`／`user_profiles`／`vehicle_category`／`vehicle_setting`）<br>(b) `tests/test_intake_scaffold.py` 6 項：`new_feature.py` 於 pytest tmp dir 以 `--adopt-existing` 執行時 exit 2，夾具問題<br>(c) `tests/test_gates_tsv.py` 1 項：`GATES.tsv` 漂移，唯一差異為 `features/vehicle_setting/scripts/vs_cf01_selfcheck.py`（commit `2c08a48`）未登簿 | CAM-02 上繳 §8；CAM-02 審閱 §五 | 全 repo 測試不綠 | 中 | OPEN |
| GCB-04 | **`docs/fw036/RULINGS.sha.tsv` 未重生** —— 該表為單一全域檔，重生會夾帶他線列 | CAM-01 上繳 §10.2-5 | `R-CAM1`～`R-CAM10` 及 `R-CAM5(c)′` 之指紋未入表 | 中 | OPEN |
| GCB-06 | **R-TM13 之實作備註：修訂段須以「同級錨自立」落檔** —— `scripts/rulings_hash.py` 將同一標題轄下之**多個** fenced block 併雜湊，故把 `(e)` 段之 code block 寫在原條標題下會使原條之 **fenced sha 改變**，與 R-TM13「原句逐字不動」之可驗證性相違。正確作法：修訂段自立為同級 `###` 錨（沿 `features/audio_mgmt/RULINGS.md` 之 `R-AM2′` 前例），原條僅留刪除線引註 —— 如此原條 fenced sha 不變、body sha 變，兩者併記即為證據 | CAM-04 上繳 §1.1；CAM-04 審閱 §一-5 | 全域 —— 他 feature 日後修訂條文時同受影響 | 中 | OPEN |
| GCB-05 | **`sources/MANIFEST.tsv` 重複 doc_id** —— `r1lr_atl_h_25pi3_5_cabin_cfts_020_ics_and_dcsd_20250910_1124` 於 HEAD 即有兩列 | CAM-01 上繳 §10.2-6；CAM-01 審閱 §六 | doc_id 之唯一性不成立 | 低 | OPEN |
| GCB-07 | **lint `J` 改以「逐字」為豁免條件** —— `J`（行首大寫）現以 token 白名單／camelCase／dotted-call 為豁免（`j_exempt()`），未涵蓋「`test_item` 上半為來源逐字而該來源首字即小寫」之情形。Camera batch02a 五列（`-051`／`-052`／`-055`／`-056`／`-070`，來源首字為 `when`／`a)`／`implement`／`a.`）因而必然命中；改大寫即破壞 §4.3.1 之逐字忠實與 `selfcheck_camera.py` 第 4 項之保序子序列判準。**交付語料實測有前例**：`features/*/delivered/` 之 test_item 首行 2223 筆中 10 筆首字小寫（`power`／`vehicle_setting`，兩本皆已交付）。建議 `J` 於 `test_item` 欄增一豁免：上半與其 `source_object_id` 之 SYS2 `Description` 首 token 相同者不判 | CAM-07 上繳 §3-3；CAM-07 審閱 §一-2（Pei 准）| 全域 —— 他 feature 凡遇首字小寫之逐字來源同受影響；Camera 側現以 profile 豁免條 ＋ 逐列 reasoning 具名承接 | 中 | OPEN |
| GCB-08 | **量測主張須附證據，提請入全域 ledger** —— 上繳包中「查無／零命中／全等／逐字相符」之主張須附掃描字串、母體檔名與本數、命令、命中數；無證據者視同未量測。立條之由為 Camera 線之實例：CAM-11 上繳宣稱「`Steering_Ratio_Rack_Pinion_Type` 於 Atl-Hi 三本 PROXI 掃描零命中」，該掃描**實未執行**，CAM-12 重掃即查得（byte 88 bit 0–1，三本 row 410）。Camera 側已立 **R-CAM17** | CAM-12 上繳 §5-1；CAM-12 審閱 §二-1（Pei 准）| 全域 —— 各 feature 之上繳包皆有同型主張，無證據時審閱無從複驗 | **高** | OPEN |
| GCB-09 | **`lint036.py` 無「同檔名拼寫變體」檢查** —— `specification_reference` 之錨依 canon §10.7(b) 為 `{檔名}_{章節號}`，而檔名之 token 化（空格→底線，其餘字元逐字）目前無任何檢查把關；同一份來源文件若在不同列拼成不同變體（`…RVC+PAM_…` 對 `…RVC_PAM_…`、`(February_10th,_2023)` 對 `February_10th_2023`），九本全 0 仍會通過，而 IN §10.7 之「同文件內 ObjectID 升冪」檢查亦因前綴不同而失效。**建議**：加一項全域檢查，把各列 `spec` 欄之檔名前綴正規化（去底線、去標點、casefold）後分群，同群內出現 >1 種原始拼法即判；母體為該 feature 之 `sources/` 實體檔名。Camera 側現以 `b_plan.tsv`／`recon_b_rows.tsv` 之一次性重生達成一致（CAM-14 §1-2），無機械保證 | CAM-13 上繳 §2-2；CAM-13 審閱 §一-2（Pei 准）| 全域 —— 凡 `spec` 欄以檔名為前綴之 feature 皆同受影響；與 GCB 之 GC_BACKLOG 第 1 項（升冪檢查）宜併案 | 中 | OPEN |
| GCB-10 | **沿用既有 DR 而擴其範圍時，須於 `DATA_REQUESTS.md` 明文改題並保留原題** —— 缺件之範圍一旦擴大而只在 TC 側沿用舊 DR 號，該 DR 之題與其實際射程即脫節，送件者無從知道要補幾樣東西，審閱亦無從複驗。立條之由為 Camera 線之兩次實例：**DR-CAM-g** 由「Controls page 之 HMI entry path」擴為「HMI 入口路徑之逐字來源」二項（CAM-15，已明文改題）；**DR-CAM-h** 由「Pop Up List 之 camera out-of-position 條目」擴為「Pop Up List 之 camera 相關缺件」二項 —— CAM-16 當時**沿用而未擴題**，經自報後於 CAM-17 補正。**建議之形制**：改題時保留原題於括號內（`（CAM-nn §x 擴範圍；原題「…」）`），逐項編號，並於「Leaves served」欄補列新受影響之列 | CAM-16 上繳 §4-3（自報）；CAM-17 審閱 §一-2（Pei 准）| 全域 —— 各 feature 線皆有沿用既有 DR 之情形；Camera 側已立 DECISIONS **6-60** 為本線通則 | 中 | OPEN |
