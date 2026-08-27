# 下放包 13 — Bed Lowering Mode：綠色通道啟用，B5 → B7 連續執行

日期：2026-08-27
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01–12，取 13
對象：執行層（Tier 1）
依據：R-BLM15(3)、**R-G14（綠色通道成立）**。下放包 03–12 其餘條款繼續有效。

**B4 複審通過（2026-08-27），無 A 類項。R-G14 計數 = 3 → 綠色通道啟用。**

分析層對上繳 12 兩題之處置（皆不構成 A 類）：
- **文案字串**：執行層取來源正式欄（`Truck Bed Lowering In Progress`／
  `Truck Bed Lowered`）而非下放包預期字串，**正確**。下放包之字串為
  分析層依規格 concept screen 之記憶所寫，屬預期非裁定；實測不符即以
  實測為準，錨定原則如此。彎引號→直引號屬 IN §11 排版正規化，非改字
- **DR-3**：登記正確。分析層已完成草擬並補結案動作清單（含 033-02／
  034-02 之連動複驗），送出待 Pei

---

## 一、綠色通道之範圍與界線

自本包起，**B5／B6／B7 三批連續執行，不逐批等分析層複審**：

- 每批仍完整走：預查 → 生成 → 機檢 + lint（讀工作簿）→ 寫回無 PENDING 者
  → 上繳留檔（`docs/upstream/`）
- 上繳包照常寫，但**不停下等回覆**，逕接下一批
- 三批全數完成後停，交分析層總複審 + Pei 抽查

**通道中止條件（任一觸發即停，回逐批模式）**：

1. 出現需 Tier 2 裁定之事項（新 override、範圍界定、上游矛盾之處置擇一）
2. 新缺件 DR 之影響 **≥ 5 條**，或其性質使該 Test Set 過半不可測
3. 機檢或 lint 非 clean 且原因不在本批可修範圍
4. 台架可執行性以外之新形態問題（如 B3 之 PROXI 缺值形態）
5. **執行層自身認為某項判斷不該由自己作** —— 此條優先於前四條，
   不需理由充分，停下即可

## 二、三批範圍

| 批 | Test Set | 母號 | leaf |
|---|---|---|---|
| B5 | HU Feedback | 008／026／031／032／036 | 20（HMI 20／Service 0）|
| B6 | Feature Entry | 004／018／019／025／028／029／030／039 | 31（HMI 31／Service 0）|
| B7 | Display Legibility + Access Ergonomics | 013／014／015／016／017／023 | 29（HMI 29／Service 0）|

三批合計 80 leaf。完成後 176 leaf 全數生成（96 + 80 = 176）。

## 三、各批已知形狀

### B5（HU Feedback）
- status bar truck-lowering 圖示、按鍵 highlight、HU 端顯示
- **與 037-03～05（Fault Handling 之 highlight 群）界線**：那三條驗
  故障時之撤除；本批驗正常態之呈現。先讀已交付 13 條再定界
- 觀察多為目視，訊號輔助；ER 判定主體寫顯示

### B6（Feature Entry）
- 三入口（Apps menu／Controls tab／Home Screen 捷徑）、圖示、選單結構
- **上繳 10 §七-5 之未查證項在此批必須面對**：037 只給入口名稱，
  實際導航路徑未載，且 PDF concept screens 依 R-BLM7 不入語料。
  處置：以名稱書寫，導航細節留給執行者依實機補，**於 manifest 具名**
  該群 TC 之此一限制。不造路徑
- 039（選單可修改性）之可測性先讀 leaf 原文再定

### B7（Display Legibility ＋ Access Ergonomics）
- **R-BLM2 之 coverage gap disclosure 在此批落地**
- 逐 leaf 二分：
  - **可功能化**（日夜模式切換後文字仍可讀、標籤依規定顯示等）→ 生成 TC
  - **純設計驗證**（percentile 人因、手部觸及淨空、實車包裝量測）→
    **不生成**，入 gap disclosure table
- disclosure table 落 `features/bed_lowering/COVERAGE_GAPS.md`，欄位：
  leaf id／037 原文摘句／不生成之理由／建議驗證方式（設計審查／實車量測）
- **二分之判準逐條寫明**，不得只給結論。判準本身若在某條上模稜兩可，
  該條列入 disclosure 並註明「判準模稜」——**寧可揭露過多，不可默默吸收**

## 四、三批完成後之停點

停。上繳包 13（可分 13a/13b/13c 或合一，執行層決）交分析層總複審。
總複審後即進交付準備：COVERAGE_GAPS.md 定稿、PENDING 清單、
交付說明（含 R-BLM5 追溯粒度揭露、A-BLM11 重複揭露、非匯流排可判項統計）。

## 五、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行；7 條 PENDING |
| DR-2 | Off-Road 2／Easy Entry ride-height 對映 | 草案已登記，送否 Pei 決；不阻斷 |
| DR-3 | Bed Lowering cluster graphics definition | 草擬完成，送出待 Pei；1 條 PENDING ＋ 2 條連動 |
