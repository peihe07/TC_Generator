# 防堵架構（2026-08-21）— 之後產生的 TC 不再出現同類缺陷

原則：每一類已發現缺陷必須同時存在於四層防線，缺任一層即為
架構缺口。根因回顧：AMFM 51.7% 漏括號 = 規則只活在單輪 prompt
（缺層 1、3）；兩套規則並存 = 層 1 不唯一；BT powered-on 275 列
= 層 3 從未檢查。

## 四層防線

**層 1 規則層（單一權威）**
- canon（docs/runtime/ASPICE_SWE6_AI_Instruction.md）為唯一現行版；
  09_ 目錄 v2 等標 superseded 並置指回連結（S1）
- 衝突收斂：方括號→`"..."`、尾句號→禁（S2）；§10.7 增家族 A；
  新增 §4.3 括號下半（S4）、§8.4.3 缺件佔位（S6）、R-1~R-5 條文
- 每 feature RULINGS_LEDGER.md 台帳；[DEFAULT] 制（S5）

**層 2 生成層（prompt builder 必填鍵，不隨輪次增減）**
固定注入：
- test_item 兩段式（上半摘句依 R-3 長度、下半 `(...)` 必填）
- test_set：closed vocabulary（僅可自 framework.md Layer 2 詞彙表
  選值，禁自由字串）＋ author 欄必填
- spec_reference 格式模板依 spec_mode 分流（R-2 家族 A/B 各一模板）
- 訊號記法卡（R-1 三層記法 + 該 feature DBC 網段清單）
- 缺件指示：無源資料 → `PENDING: DR-{n}`，禁留空禁 NA

**層 3 檢查層（lint 硬 gate，出貨前零違規）**
| 檢 | 內容 | 條文 |
|---|---|---|
| A | 步驟禁用動詞（observe/verify/check whether…） | §5.1 |
| B | ER 情態詞 shall/will/should（引號內原文豁免） | §6 |
| C | test_item hedge 詞 | §4.3 |
| D | PC 系統預設/動作句（powered on…） | §4.4 |
| E | 步驟↔ER 1:1 對齊 | §6 |
| F | 方括號 `[X]`（來源 verbatim 依 profile 豁免） | §11 |
| G | Test Set 空值/詞彙表外值 | §4.2 |
| H | ER 模糊詞（as expected/normal） | §6 |
| I | test_item 末行 `^\(.+\)$`；sibling 括號不得同文 | S4 |
| J | 行首大寫（豁免：技術token/camelCase/引號/$/工具表） | R-4 |
| K | CJK 偵測（配置依 R-5；工作備註型無條件禁） | §1 |
| L | test_item 長度閾值（R-3 裁定值） | R-3 |
| M | 必填欄空白三態（空=FAIL；NA/PENDING 合法；出貨禁 PENDING） | §8.4.3 |
| N | 行尾句號 | §11 |
| O | spec_reference 格式（家族/分隔/排序/檔名 token） | R-2 |
| P | CAN 斷言三件組（signal+message+segment） | R-1 |
豁免表（工具名單、UI 標籤語言、profile OVERRIDE）隨 lint 版控，
增修需記入 RULINGS_LEDGER。

**層 4 覆核層**
- 每包上繳附 lint 報告全文＋「該驗未驗」獨立判斷（既有機制）
- pilot review 依 canon §1.2 分層取樣；lint 通過≠免抽驗
- 驗收條件一律寫「與參照對象在所有可讀屬性一致」，不寫
  「已知幾項正確」

## 生效順序

R/S 裁定 → canon 回寫（層1）→ lint A–P 實作並對 Media 0625 全本
試跑（已知最乾淨本，預期僅 K 或零命中，作為 lint 自身校準）→
prompt builder 模板更新（層2）→ 新 feature（Time Management 起）
全鏈生效 → 回修批次同用此 lint 驗收，新舊同一把尺。
