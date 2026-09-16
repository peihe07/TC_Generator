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
