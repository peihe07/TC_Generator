# RULINGS — Power (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Power 之裁決權威；
跨 feature 條文承接時註明來源包。

---

## 第一輪 — 下放包 01（`docs/handoff/01_intake.md` §A）

> 01 包之步驟 5（抄入 RULINGS.md）因該包停於步驟 2 而未執行。
> 於 02 包一併補抄，條文逐字照錄，狀態欄反映 02 包之異動。

```
[R-P1] SWE-PM-089 之來源對應先留空。
       不臆測、不套用鄰近 leaf 之來源、不以 SWE1-PM-ANT-008 反查填補。
       該 leaf 仍計入 115 母體，列為 RD-1 待決。
       裁決者 Pei，逐字依據：「那題記得先留空 其他可以繼續」。
```
**狀態：live。** 02 包實測 G3 = 114/115，唯一失敗者即 `SWE-PM-089`
（其 `Source Requirement ID` = `SWE1-PM-ANT-008`，非 SYS2 命名空間）。未填補。

```
[R-P2] 命名。feature 目錄 = features/power；
       workbook Test Group = "Power Management"；
       tc_id 方案 = NR1L-PowerManagement-{NNN}。
       裁決者 Pei，逐字依據：「是繼續」（回應 #5 提案）。
```
**狀態：live。**

```
[R-P3] spec_mode = B（純文字層 + 章節 regex）。
       三份 .docx 經 magic bytes 實測皆非 OOXML 亦非 OLE，
       為 Markdown 純文字轉檔。禁止以 python-docx / olefile /
       zipfile 讀取；一律以 UTF-8 文字讀入。
```
**狀態：撤回（R-P9）。** 事實前提為假 —— 原始檔實測兩份 OOXML、一份 OLE2。
改立 R-P3′，見 R-P9。

```
[R-P4] Power Management 之規格來源為兩份 CFTS：
       CFTS009 Wake-up and Power-up、CFTS010 Power Down。
       任何宣稱「規格來源」之陳述必須同時涵蓋兩份，
       單引一份即為不完整。
```
**狀態：live。** 02 包實測 G4 = 111 / 3 / 1，兩域互斥，證實雙來源。

```
[R-P5] Layer 2 之 `Power State` 與 `Power State Reporting` 合併，
       為單一 Test Set `Power State`，64 leaf。
       Layer 3 隨之合併，含 CFTS009 §1.6.2.1.15
       （`TLM_Status.Info` / `$Telematic_Power$` 訊號上報）。
       裁決者 Pei，逐字依據：「E-1 合併」。
```
**狀態：live，惟 leaf 數待重裁。** 02 包重算 Power State = **62**，非 64。
見 `docs/upstream/02_rebaseline.md` §五。依 §E 末，不逕行改寫。

```
[R-P6] Layer 2 之 `Power Down`（3 leaf）**保留獨立 Test Set**，
       不因低於 §4.1.3 健康門檻而合併。
       裁決者 Pei，逐字依據：「E-2 保留獨立 Test Set」。
```
**狀態：live。** 02 包重算 Power Down = 3，相符。

```
[R-P7] 範圍界定：037 之 115 leaf 為本 feature 唯一驗證母體。
       SYS2 反向缺口（未被 037 引用之 SW/System 需求）
       與 SYS2 匯出之收錄規則（`Sys-RA-PM-0197`–`0206` 斷點、
       CFTS009 本文未被引用之 547 條）**不追、不問、不列 RD-1**。
       DR-PW2 撤回。
       裁決者 Pei，逐字依據：「#1/#3 不需」。
```
**狀態：live。**

```
[R-P8] Priority 之判定來源：依 **TC 實際所寫之測項內容**
       套 §10.2 之 rubric 判定 P0–P3。
       037 `Priority` 欄之 `High` / `Medium`（91 / 24）
       **不具映射權威**，不得以之推導 priority。
       DR-PW4 撤回。
       裁決者 Pei，逐字依據：「#4 依照所寫測項去判定」。
```
**狀態：live。**

---

## 第二輪 — 下放包 02（`docs/handoff/02_rebaseline.md` §A）

```
[R-P9]  R-P3 撤回。其事實前提為假 —— 分析層所測之「三份純文字」
        係 Project 附件之轉換產物，非磁碟上之原始文件。
        改立 R-P3′：spec_mode = D（二進位文件抽取）。
        讀取方式依實測 magic bytes 決定：
          50 4B 03 04（OOXML .docx）→ zipfile 或 python-docx
          D0 CF 11 E0（OLE2 .doc）  → macOS 內建 textutil 轉換
        R-P3 對 python-docx / olefile / zipfile 之禁令一併解除。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q1）。
```
**執行層回報：已落實。** CFTS009（`50 4B 03 04`）以 `zipfile` +
`word/document.xml` 抽出；CFTS010（`D0 CF 11 E0`）以 `textutil -convert html`
抽出。SYS3 依 01 包 §B 不讀。

```
[R-P10] 三份純文字衍生物明示為不可得：無版本、無產生紀錄、
        無法重現，一律不得再作為任何量測之來源。
        CFTS 本文相關之一切數字，均須自原始檔重新產生。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q2）。
```
**執行層回報：已落實。** 02 包所有 CFTS 相關數字（G3、G5b、G8、G9、§E 重算）
皆自原始檔重新產生，無一沿用 01 包之值。

```
[R-P11] G8 / G9 四數（CFTS009 需求錨點 904 / 章節錨點 172；
        CFTS010 需求錨點 148 / 章節錨點 92）作廢。
        自原始檔重測後改寫 §D 期望值，不視為停止條件。
        理由：原值非 baseline，係自失效來源量得，
        改寫不構成「自行調參數遷就」。
        此例外僅適用於本次 rebaseline，不得類推。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q3）。
```
**執行層回報：已重測。** G8 = 需求錨點 904 / 章節錨點 **196**；
G9 = 需求錨點 148 / 章節錨點 92。四數中三數與舊值相同；
CFTS009 章節錨點由 172 改為 196，差額 24 項經獨立佐證為真標題
（pStyle 7 ×15、pStyle 8 ×9），舊值 172 係衍生物粗體處理造成之漏算。

```
[R-P12] A-PW07 撤回（「三份 .docx 實為 Markdown 純文字」為假；
        副檔名與內容實為相符）。
        改登 A-PW08：01 下放包 §B 之「真實格式」欄與 bytes 欄
        與原始檔不符，源於以衍生物冒充原始檔。
        另記：CFTS010 之原始檔副檔名為 .doc，非 .docx；
        01 包中「三份 .docx」之表述在檔名層即為錯誤。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q4）。
```
**執行層回報：已落實於 ANOMALIES.md。**

```
[R-P13] 台帳通則（跨 feature 適用，canon 候選）：
        凡經任何轉換之素材，台帳須同時登記
        （a）原始檔之完整路徑、bytes、SHA256 全 64 碼
        （b）衍生物之 bytes、SHA256 全 64 碼
        （c）轉換工具與完整轉換指令
        三者缺一，該素材不得作為量測來源。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q5）。
```
**執行層回報：已落實。** 見 `docs/upstream/02_rebaseline.md` §二（原始檔七份）
與 §三（衍生物三份，含轉換指令）。

```
[R-P14] 閃點表結構修正：
        （a）新增 G0「素材身分驗證」為前置閘 ——
             全部素材之原始檔 SHA256 相符方得進入 G1 以後。
             G0 不通過時，G1 以後一律不執行、不回報。
        （b）G11 移除。其期望值與 §E 同源，
             以 G11 驗 §E 為循環論證，不構成獨立驗證。
        （c）§E 之「已定版」與「本表實際只由單一來源支撐、
             不是交集」並存之張力，維持登記，不由實測覆蓋。
        裁決者 Pei，逐字依據：「照你的建議」（回應 Q6）。
```
**執行層回報：已落實。** G0 = 7/7 通過；G11 未執行、未回報；
§E 之張力維持登記，重算結果僅上繳不改寫（§E 實測 62/24/16/8/3 + 未歸類 1）。

---

## 待裁

- **§E leaf 分布重裁**（R-P5 / R-P6 所定之 64/24/16/7/3 與實測不符）。
  見 `docs/upstream/02_rebaseline.md` §五、§七。
- **§C rule 1 / rule 2 之文字層適用面**（執行層採「rule 1 套未標記文字、
  rule 2 套粗體標記文字」之統一定義，待分析層追認）。見同上 §四。
