# 下放包 08 — Bed Lowering Mode：B1 批（Restore And Exit）+ R-BLM15 落地

日期：2026-08-26
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01–07，取 08
對象：執行層（Tier 1）
依據：R-BLM15。下放包 03–07 其餘條款繼續有效。

---

## 一、R-BLM15 落地（B1 生成前完成）

1. **recon_assertions 兩鍵重宣**（R-BLM15(1)）：
   - `spec_reference_distinct_values`: expected `1`，且值 = R-BLM5 常數
   - `spec_reference_parsed_sections`: expected `0`
   原兩鍵作廢留痕（註解保留，標 superseded by R-BLM15(1)），
   重跑 recon 至全綠、DECISIONS.md 產出，回報
2. **兩常數查錨**（R-BLM15(2)）：讀 AMFM 已交付本（v1 tagged）與
   SWC 0708 之 `functional_safety` 與 `test_version` 兩欄實值分佈，
   逐本回報值域。查得既定值 → 13 列 XML 外科式 patch + round-trip +
   保全計數；查無或兩本不一致 → 停下回報值域，待 Pei 點名
3. DR-1 狀態已改（送出核准，Pei 執行送出）——B1 生成不等回覆

## 二、B1 批：Restore And Exit，9 leaf（母號 022／027）

沿 pilot 全流程，差異與特別點如下：

1. **生成路徑**：本批起走 `prompt_builder`/`generator` 實路徑
   （工程債已收，dry-run 已通）。若模型輸出品質壞（上繳 07 自陳 §六-2
   之未驗項），對照 pilot 之 session 直寫品質回報差異，不靜默修補
2. **訊號預查**：語彙先行已做（上繳 07 §五），本包完成 DBC/LID 逐條
   定位（ride height 四訊號 + `IPC_VEHICLE_SETUP2.Default_Ride_Height`
   已驗有；車速訊號須新查——查有/查無入 manifest）
3. **DR-1 落法（首驗）**：`022-03 Exit Bed Lowering Above Threshold` 等
   涉 `*XX MPH` 者，門檻值一律
   `PENDING: DR-1 BLM operating speed threshold value`，不造值、
   不寫 vague（IN §8.7.1 之具體值要求由 PENDING 佔位承接）。
   含 PENDING 之列**不入寫回**（IN §8.4.3：含 PENDING 之工作簿不得出貨；
   本批寫回範圍 = 9 條中無 PENDING 者，餘者停在 batch 待 DR-1 覆）
4. **022-02 之 Title = `Detect` 單字**：test_item 上半取 Requirement
   Description 摘句（R-3 之 50 token 上限適用），manifest 具名記載
   此一 Title→Description 之取材切換與理由
5. **「偵測／接收」類再現時**：先套 R-BLM13(c) trigger 區分，
   無 trigger 可分再用 (a)；per-TC reasoning 僅委派條有（profile §4）
6. **速度門檻之 Pre-Condition 句式**：IN §8.7.1 之
   `<condition> >= <trigger value>` 形，value 位置放 PENDING 佔位
7. 機檢 + lint（讀工作簿之 16 gate）+ 括號下半語言檢，manifest 逐源
   stamp，上繳含逐 TC 全文

## 三、停點

B1 生成 + 無 PENDING 者寫回完成後停，上繳包 08 交審。
**綠色通道計數自 B1 起算**（R-G14：連續 3 批分析層審無 A 類項
→ 自動續批，Pei 抽查）。

## 四、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行送出；B1 以 PENDING 落法承接 |
