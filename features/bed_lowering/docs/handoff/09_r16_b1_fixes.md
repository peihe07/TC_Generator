# 下放包 09 — Bed Lowering Mode：R-BLM16 落地 + B1 三項 A 類修正

日期：2026-08-26
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01–08，取 09
對象：執行層（Tier 1）
依據：R-BLM16。下放包 03–08 其餘條款繼續有效。

---

## 一、R-BLM16 落地

### 1.1 recon.py want 閘控（R-BLM16(1)，全域腳本、預設不變）

- 將 `recon.py:401` 之無條件 assertion 納入 want 閘控，可宣告為期望值
  （本 feature 宣告 `unparsed_citations: 176` 或等效之關閉語意，取
  recon 既有宣告風格一致者）
- **驗收兩跑**：(a) 回歸跑——移除本 feature 宣告，行為須逐字重現現行
  1-FAIL 輸出；(b) 宣告跑——全綠、DECISIONS.md 產出
- 改動 diff 全文入上繳（全域腳本改動之留痕義務）

### 1.2 S／AB 兩欄清空（R-BLM16(2)(3)）

- `bed_lowering_02.xlsx` 現行 19 列（10–28）之 S 欄與 AB 欄 patch 為空
- XML 外科式；round-trip；保全計數；全簿 lint
- **lint 之 [A-empty] 類 gate 須同步確認不誤報**：test_set 空是錯、
  functional_safety 空是裁定——gate 的欄位範圍要分得開，改後跑給證據

### 1.3 暫定值登記（R-BLM16(4)）

manifest 之 B1 節加 `provisional_inputs`：022-01／027-05 之 5 Km/h，
附 DR-1 結案複驗義務之指向（DATA_REQUESTS.md 已載動作清單）。

## 二、B1 三項 A 類修正

### 2.1 022 群入口改 HU 按鍵（022-01～04 四條）

- 現行 `Send $ASCM_FD_2.BDL_Enbl$ = 1` 之入口步一律改為：
  `Send $BRAKE_FD_2.VehicleSpeedVSOSig$ = 0 (0 Km/h)` →
  `Press "Bed Lowering" on the HU Controls tab to enter Bed Lowering Mode` →
  `Read the signal $ASCM_FD_2.BDL_Enbl$ and check that it is 1 (TRUE)`
- 理由（入 manifest）：對 ASCM 自發訊息注入，真件則匯流排衝突、
  模擬則迴路驗證；HU 按鍵為真實路徑，之後 `BDL_Enbl`／`ASCM_Stat`／
  角落高度方為可觀察之 DUT 側輸出。027 群現行寫法即為此型，不動
- 022-02 之「value read in step 1」指涉隨入口改寫自然消除
  （入口第三步即為 Read，後續 change-from 指涉該步）
- 步序重排後 ER 1:1、長度分級、§5.1 主動詞全數複核

### 2.2 027-03 隱藏狀態前置

- Pre-Condition 增：`The active ride height setting is 0 (Normal)`
  （或等效之「active ≠ Aerodynamic」狀態句，取可於台架確立者）
- 無此前置時「回到記錄值」與「回到 default」不可區分（§7 FF）

### 2.3 波及範圍

- 已寫回之列：022-01（入口改）→ patch 該列；027-03（前置補）→ patch 該列
- 未寫回之三條（022-02/03/04）：batch json 內改，維持 PENDING 不寫回
- patch 與 §1.2 之清欄合併為一次寫回操作，round-trip 一次驗

## 三、修訂後義務

機檢 + lint（全簿 19 列）+ 括號下半語言檢；manifest 逐源重 stamp；
修訂 diff 逐 TC 列（引 R-BLM16 與本包 §二條款）。

## 四、停點與後續

修訂完成停，上繳包 09 交**分析層複審**。複審通過後：
- B1 定版（不回計乾淨批數，R-G14 計數自 B2 起）
- **B2（Activation Gating，28 leaf）由分析層逐包下放，不另經 Pei 關卡**
  （R-BLM16 末段）

## 五、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行；結案動作清單見 DATA_REQUESTS.md |
