# 下放包 11 — Bed Lowering Mode：B3 批（Lowering Operation，33 leaf）

日期：2026-08-27
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01–10，取 11
對象：執行層（Tier 1）
依據：R-BLM15(3)。下放包 03–10 其餘條款繼續有效。
**B2 複審通過（2026-08-27），無 A 類項，R-G14 計數 = 1。**
007-03 定義型需求之可測性處置繫於 DR-1，維持 PENDING 不另裁。

---

## 〇、B2 收尾一項（本包順帶）

A-BLM11 處置落地：006-03／006-05／020-03／020-05 四條加 per-TC 鏡映註
（句型：本條與 {對應 leaf} 之步驟逐字相同，鏡映 037 之 006／020 兩群
自身重複；依 §8.2.1/§8.2.2 不合併、不製造差異）。batch json 與
manifest 重 stamp。TC 本文不動，不重驗全批。

## 一、B3 範圍

Test Set = `Lowering Operation`，母號 001／002／003／021／035／040／041，
**33 leaf（HMI 18／Service 15）**，`test_set_map.tsv` 整組取用。
req_id 集合與 context 對帳 assert（沿 B2）。

## 二、本批已知形狀

1. **車型變體軸首用 PROXI**（001 = DT 前升後降；002／041 = DJ/D2 僅後降）：
   - 先自 PROXI 工作簿（`PROXI_HDCC27_R3_20250424.xlsx`，已綁）預查
     車型配置參數之實名與值域（Vehicle Line／Body Style 類），
     查有 → `PROXI <Param> = <值>` 式（IN §8.7.5(c)，**不加 `$`**）；
     查無 → 停下回報，不造參數名
   - DT 與 DJ/D2 之 TC 已由上游 leaf 拆開，**不另拆**；車型建立
     寫入 Pre-Condition（配置狀態）或 Procedure 首步（PROXI 設定），
     擇一，全批一致
2. **前升後降之觀察**：DT 之前軸抬升需前角落訊號——`FL_Lvl`／`FR_Lvl`
   是否存在於 `ASCM_FD_1` 先預查；查無記「查無」，該斷言改以可觀察物
   承載或具名回報
3. **040（air suspension LED 全滅）**：LED 為實體指示。先查 LID/DBC
   有無 LED 狀態訊號；查無則以實體觀察句式寫（`Check that the air
   suspension LED indicators are off`），不造訊號
4. **021 速度類**：DR-1 命中逐列確認（影響清單載 021-04/05），
   照 PENDING 落法；暫定車速值入 `provisional_inputs`
5. **入口紀律**沿 B1/B2：ASCM 側訊號僅觀察；lowering 之觸發走 HU 按鍵
6. **035（既有氣壓懸吊路徑）**：與 001/002 之界線先讀鄰居（§8.2.1）
7. 「偵測／接收」型依既定次序：先 (c) 後 (a)；per-TC reasoning 僅委派
   ／鏡映條有

## 三、流程與停點

沿 B2 全流程。生成完成停，上繳包 11 交分析層複審。
**本批為 R-G14 計數第 2 批候選。**

## 四、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行；021 群將再命中。結案動作清單已更新為「各批 provisional_inputs 全數複驗」 |
