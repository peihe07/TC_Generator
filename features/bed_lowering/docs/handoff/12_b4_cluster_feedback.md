# 下放包 12 — Bed Lowering Mode：B4 批（Cluster Feedback，13 leaf）

日期：2026-08-27
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01–11，取 12
對象：執行層（Tier 1）
依據：R-BLM15(3)。下放包 03–11 其餘條款繼續有效。
**B3 複審通過（2026-08-27），無 A 類項，R-G14 計數 = 2。**

分析層對上繳 11 三題之處置（皆機械，不上升）：
- **PROXI 採選項 1 定案**（全批狀態句）。附註：「DJ/D2 零命中」為字串
  層之查無 —— 值域 33 項多為數字標籤（343、560…），DJ/D2 可能以
  程式碼形式在列，判定需車系代碼對照（同上繳 04 之 ASCM/LID 形態）。
  已向 Pei 提問備查，不阻斷
- **040 LED 目視判定不構成新形態**：EVIC 文案與 highlight 本就目視判定，
  本工作簿為手動測試規範，LED 同類。Tier 2 免議
- **002-04/05 姿態判準**接受為已揭露之操作化詮釋，manifest 承載；
  041-01/02 之模式對映登 DR-2 草案（送否 Pei 決）

---

## 一、B4 範圍

Test Set = `Cluster Feedback`，母號 009／010／012／033／034，
**13 leaf（HMI 11／Service 2）**，`test_set_map.tsv` 整組取用，
req_id 集合對帳 assert。

## 二、本批已知形狀

1. **Cluster 畫面文案**（"Lowering Bed"／"Bed Lowering Complete"）：
   文字基準取 SYS1 正規化文字（該 NRL 列逐字），與 038-04 同紀律；
   引號式 `"..."`，破折號沿 hyphen 裁定
2. **chime（012 群，完成提示音）**：可聽判定與 LED 目視同類，正常寫
   （`Check that the completion chime is played` 型）。**先預查** LID/DBC
   有無 chime 觸發訊號；查有則聲音 + 訊號雙 ER，查無則純可聽判定，
   記 manifest
3. **Cluster vs EVIC 之界線**：EVIC 故障訊息歸 Fault Handling（011/038
   已交付），本批 033/034 之 EVIC in-progress／complete 訊息與其相鄰
   —— §8.2.1 先讀 Fault Handling 已交付之 13 條再定界，勿重測故障文案
4. 入口紀律沿前批；「偵測／接收」型依 (c) 先 (a) 後
5. 觀察通道多為目視／可聽，訊號僅輔助 —— ER 之判定主體寫顯示／聲音，
   訊號確認為輔句，勿倒置

## 三、流程與停點

沿 B3 全流程。生成完成停，上繳包 12 交分析層複審。
**本批為 R-G14 計數第 3 批候選 —— 過則綠色通道成立**，
B5 起自動續批、上繳留檔、Pei 抽查。

## 四、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行；累計 7 條 PENDING 未寫回 |
| DR-2 | Off-Road 2／Easy Entry ride-height 對映 | 草案已登記，送否 Pei 決；不阻斷 |
