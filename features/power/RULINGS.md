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

## 第三輪 — 下放包 03（`docs/handoff/03_framework_inputs.md` §A）

```
[R-P15] 主章節判定規則：
        （a）解析至單一章節之 leaf —— 自動歸屬該章節。
        （b）解析至多個相異章節之 leaf —— **不以任何演算法決定**。
             逐條列出其章節集合，逐條由 Pei 裁定，記入 RULINGS.md。
        禁止以出現次數、章節深度、token 順序、章節號大小
        或任何 tie-break 自動指派。
        理由：此為判斷而非計算；02 包之不符即源於將判斷
        隱藏於未書面化之 tie-break。
        裁決者 Pei，逐字依據：「都照你建議」（回應 Q1(a)）。
```
**執行層回報：已落實。** 11 個跨章節 leaf 之素材見 `data/multi_chapter_leaves.md`
（B1），未附任何建議歸屬。單章節之 103 個 leaf 依 (a) 自動歸屬。
**待 Pei 逐條裁定 11 條。**

```
[R-P16] §E Layer 3 之 CFTS009 §1.8.1 刪除。實測 0 leaf 落點，
        係分析層轉抄時多寫。
        裁決者 Pei，逐字依據：「都照你建議」（回應 Q1(c)）。
```
**執行層回報：已落實於 §E，但前提須複核。** 「實測 0 leaf 落點」僅在
02 包之主章節規則下成立。實測 `SWE-PM-057` 之章節集合含
**CFTS009 §1.8.1.1.1（ID 1 Description）**，出現 3 次，與其他兩章節同票。
即 §1.8.1 並非無 leaf 觸及，而是在該規則下未勝出。
依 R-P15(b)，`SWE-PM-057` 之歸屬尚待裁定 —— 若裁定為 §1.8.1.1.1，
則 R-P16 之刪除前提不成立。**登記為 A-PW14，待 Q1 裁定後回頭確認。**

```
[R-P17] 文字層定義追認為條文：
        每段同時產出 plain 與 bold 兩種序列化；
        §C rule 1（章節錨點）套用於 plain，
        §C rule 2（需求錨點）套用於 bold，兩者依段落索引對齊。
        理據：CFTS009 標題以段落樣式 pStyle 1–8 表達（run 層無粗體），
        CFTS010 標題為 run 層粗體；單一序列化不可能同時滿足兩條正則。
        佐證：該定義下 CFTS009 得 196 章節錨點，196 項全部具
        heading pStyle 1–8 無一例外。
        併同追認：G8 章節錨點期望值 172 → **196**（172 為衍生物漏算）。
        裁決者 Pei，逐字依據：「都照你建議」（回應 Q2）。
```
**執行層回報：已落實。** G8 = 904 / 196、G9 = 148 / 92，皆 PASS。
定義已寫入 `scripts/extract_textlayer.py` 之 docstring。
**附帶發現**：本定義套用於 SYS3 SYSAD 時 rule 1 匹配數為 **0**（G16）——
該文件之標題不含字面章節號（Word 自動編號），非序列化問題。見 B3。

```
[R-P18] G6 拆為兩閘，並訂正 §C 座標：
        G6a = 錨點鏈第一段，SYS2 CFTS009 欄內 token 可抽取率
        G6b = 錨點鏈第三段，該 token 可解析至 CFTS 章節之比率
        §C 之 SYS2 CFTS009 讀取座標改為 r2–**r339**，
        並註明 r339（NRL-142587）為無 Feature-ID 之 Heading 列。
        01/02 包之 G6「336/337」係將第一段與第三段混為一談，作廢。
        裁決者 Pei，逐字依據：「都照你建議」（回應 Q3）。
```
**執行層回報：已落實，且診斷獲得實測確證。**
G6a = **337 / 338**（r339 唯一無 token 者）。r339 之 `Type` 欄實測為
`Heading`，`Sys-RA-Feature-ID` 欄為空 —— 與條文描述完全相符。
G6b = 列層 **336 / 337**，唯一失敗者 `Sys-RA-PM-0334`（`4942087`）。
**此數精確還原 01 包之「336/337 失敗者 Sys-RA-PM-0334」** ——
證實該數量的是第三段而非第一段，R-P18 之診斷正確。
token 層 438 / 439；其中 81 個 token 係經**章節錨點 id** 路徑解析
（Sys-RA 直接指向章節而非需求錨點），見 A-PW15。

```
[R-P19] 02 下放包 §A 末句與 §H 步驟 8 之「七條」訂正為「六條」。
        §A 實際區塊數為 6（R-P9–R-P14），§J 之「六條」為正確值。
        裁決者 Pei，逐字依據：「都照你建議」（回應 Q4）。
```
**執行層回報：已訂正。** 訂正後重驗：§A fenced block = 6，
全檔「七條」出現 0 次、「六條」3 處一致（§A 末句、§H 步驟 8、§J）。

```
[R-P20] SYS3 SYSAD 納入閱讀範圍。R-P3′ 後技術障礙已消失。
        其 §4.x 元件分解為目前唯一可能提供**獨立**分組來源之文件
        （§E 已自承 037 Requirement Title 無分組價值），
        直接關係 Layer 2 邊界之可交叉驗證性。
        本條僅解除「不讀」之限制，不改變其對 TC 內容不具權威之地位（§8.1）。
        裁決者 Pei，逐字依據：「都照你建議」（回應 Q5）。
```
**執行層回報：已讀。** 見 `data/sys3_chapters.md`（B3）。
47 個 heading（Heading1 ×9、Heading2 ×38），§4「系統架構設計」下
36 個 Heading2。**未據此調整 §E 之任何分組**（B3 禁區）。

```
[R-P21] 037 之 SYS2 Traceability 與 Excluded NRLs (HW-only) 兩分頁
        補入 §C 讀取座標並補設閘門。
        A-PW03 / A-PW04 / A-PW05 三條 anomaly 全部宣稱此二分頁之內容，
        卻自 01 包以來從未經執行層複驗。
        裁決者 Pei，逐字依據：「都照你建議」（回應 Q6）。
```
**執行層回報：已落實。** 座標實測：`SYS2 Traceability` 表頭 r1、資料 r2–r34
（33 列全非空）；`Excluded NRLs (HW-only)` 表頭 r1、資料 r2–r27（26 列全非空）。
三條 anomaly 複驗結果見 `docs/upstream/03_framework_inputs.md` §六：
A-PW03 成立（且應加強）、A-PW04 逐字成立、**A-PW05 描述有誤須修正**。

```
[R-P22] 跨多章節 leaf 之非主章節不得靜默丟棄。
        補設閘門驗證：被丟棄之次章節是否已被其他 leaf 覆蓋。
        未覆蓋者須逐一登記，否則 Layer 3 之涵蓋宣稱不成立。
        裁決者 Pei，逐字依據：「都照你建議」（回應 Q7）。
```
**執行層回報：已落實，結果嚴重。** G14 實測：被丟棄之相異次章節 10 個，
其中 **9 個未被任何 leaf 之主章節覆蓋**，包含 `Stolen Vehicle Mode`、
`Logistic Standby` / `Logistic Sleep` / `Logistic Idle`、
`ICS Wakeup Reasons by POWER Button Pressed` 等實質功能章節。
在現行主章節作法下，這 9 章不會產生任何 TC。登記為 **A-PW16**。

```
[R-P23] R-P13 台帳通則增補第（d）欄：轉換工具之版本與 OS 版本。
        現況 textutil 版本隨 macOS 更新而變，同一指令跨機器
        未必產生同一雜湊；本機 Darwin 25.5.0 之可重現性已驗，
        跨機器未驗。
        裁決者 Pei，逐字依據：「都照你建議」（回應 Q8）。
```
**執行層回報：已落實。** 第（d）欄實測值：
macOS 26.5.2（build 25F84）／Darwin 25.5.0 arm64；
`/usr/bin/textutil` 173,088 B、mtime 2025-06-25（系統二進位，無版本字串）；
Python 3.10.13；openpyxl 3.1.5。見 03 上繳包 §三。

---

## 待裁

- **§E leaf 分布重裁**（R-P5 / R-P6 所定之 64/24/16/7/3 與實測不符）。
  見 `docs/upstream/02_rebaseline.md` §五、§七。
- **§C rule 1 / rule 2 之文字層適用面**（執行層採「rule 1 套未標記文字、
  rule 2 套粗體標記文字」之統一定義，待分析層追認）。見同上 §四。
