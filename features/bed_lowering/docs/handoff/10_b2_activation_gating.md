# 下放包 10 — Bed Lowering Mode：B2 批（Activation Gating，28 leaf）

日期：2026-08-26
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01–09，取 10
對象：執行層（Tier 1）
依據：R-BLM15(3)（順序已准）、R-BLM16 末段（B2 起分析層逐包下放）。
下放包 03–09 其餘條款繼續有效。B1 已定版（分析層複審 2026-08-26 通過）。

---

## 〇、B1 收尾一項（本包順帶，先做）

`batches/B1/b1_tcs.json` 批次層 `reasoning` 第二句仍載改寫前之入口方式
（`先以 $ASCM_FD_2.BDL_Enbl$ = 1 (TRUE) 進入降床`），與九條現行內容矛盾。
改為 HU 按鍵入口之描述，manifest 重 stamp。一句話，不重驗全批。

## 一、B2 範圍

Test Set = `Activation Gating`，母號 005／006／007／020／024／042，
**28 leaf（HMI 7／Service 21）**，以 `test_set_map.tsv` 過濾整組取用。

## 二、本批已知形狀（生成前讀）

1. **DR-1 命中群**：BLM-007 之速度類 leaf（DR-1 影響清單載 007-01~04）
   照 B1 落法——`PENDING: DR-1`、含 PENDING 者不寫回。逐列確認實際命中數，
   回報（DR-1 之「約 13」在本批消掉一塊估算）
2. **入口紀律（B1 教訓，全批適用）**：不得對 DUT 側自發訊息注入。
   進入／觸發一律走真實路徑（HU 按鍵、可注入之他節點訊號如車速、
   ignition）；ASCM 側訊號只作觀察。ignition／engine 狀態之訊號
   （`OperationalModeSts` 類）先預查 DBC/LID 定實名，查有/查無入 manifest
3. **Service 21 條**：「偵測／接收」型再現時依既定次序——先 R-BLM13(c)
   trigger 區分，無可分再 (a)；per-TC reasoning 僅委派條有
4. **042（Telematics/遠端類，若涉）**：觸發通道若非 HU 亦非已綁 DBC
   可注入者，依 §8.7.5(d)/(g) 保留來源名，不造訊號；台架不可執行者
   具名回報，不硬寫
5. **sibling 注意**：005/006/007 之間 gating 條件相鄰（ignition／
   engine／速度／檔位），§8.2.1 先讀鄰居再定界；tc_title 括號下半
   之區分 token 逐對自查
6. 兩欄留空紀律已入 `write_back.py`（CONST 空字典），本批不回填

## 三、流程與停點

沿 B1 全流程（預查 → 生成 → 機檢+lint → 寫回無 PENDING 者 → 上繳）。
生成完成停，上繳包 10 交分析層複審。**本批為 R-G14 計數第 1 批候選**：
複審無 A 類 → 計 1；連續 3 批 → 自動續批，Pei 抽查。

## 四、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行；B2 之 007 群將再命中，同 PENDING 落法 |
