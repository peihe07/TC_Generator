# Player CFTS025 — Baseline 判讀(零成本 regex-only)

> 來源:`docs/test/Player/Review/...CFTS025_PlayerFunctions_20260625(done).xlsx`
> 方式:`--review --dry-run`(純 regex,**LLM 規則沒跑**)。日期 2026-06-25。
> 157 TC / 83 Req group。

## KPI(本次能算的)

| KPI | 值 | 說明 |
|---|---|---|
| first_pass_rate | **0.0%** (0/157) | 每條 TC 至少一個 Major |
| design_method_accuracy | **0.0%** (0/157) | 全檔 design_method 欄位空白(已驗證:157/157 真的沒填) |
| 其餘 4 項 | N/A | review-only 路徑沒餵 validation / traceability / decompose_meta(設計如此) |

## Major findings 分布(525 筆,全 Major)

| Rule | 次數 | 真實 or 過度觸發? |
|---|---|---|
| §8.5.2 Design Method 缺失 | 157 | **真實** — 整份沒填 method(系統性、好補) |
| §8.3.5 末步驟無檢查標的 | 152 | **多半真實** — 直接命中你最初的痛點「步驟不夠明確執行」 |
| §8.1.1 Test Item 長度超範圍 | 137 | **部分過度觸發** — 這份 test_item 是 spec 整句式(「When X occurs, the HU shall…」),天生長;規則門檻需為這種風格調整 |
| §8.4.1 ER 用語含糊 | 69 | 待語意確認 |
| §8.1.2 / §8.3.1 | 7 / 3 | 少量 |

Tier 1(§6.x)只有 5 筆(全 §6.6 無英文 spec句),拆解層沒有 Critical。

## 三個關鍵結論

1. **first-pass-rate 有巨大可量化空間(0% → 目標 80%)**,KPI loop 有明確標的。
2. **§8.3.5「末步驟沒讀結果」152/157 = 你說的「步驟不夠明確/和實際有落差」的鐵證**。這正是 Stage 6 reality-gap / 可執行性語意檢查要打的點。
3. **這份 baseline 沒測到語意層**:11 條需 LLM 的規則(§7.x 對齊、§8.5.3、§6.3 等)dry-run 不跑;真正的「TC vs spec 落差」要一次真實 LLM review 才量得到(要花 $,或互動式跑)。

## 資料品質附帶發現(對下游有用)

- 全檔無 `design_method`、無 `pre_conditions`、無 `tc_title`(用 test_item 當標題)。
- §8.1.1 過度觸發 → 之後 Stage 6 要把「spec 整句式 test_item」納入長度規則例外。

## 下一步建議

- Stage 6 強化優先打 §8.3.5(可執行性)+ 補語意層(§7.x 對齊、reality-gap)。
- 若要完整 baseline(含語意對齊 / reality-gap),需跑一次真實 LLM review(Player 157 TC,Sonnet+快取估 < $1)。

---

# 語意 Baseline(真實 LLM review,gpt-4.1)

> 因 bash 45 秒窗 + 推理模型慢,改用「分段取樣」:兩段共 **~22 TC / 13 Req group**(早段 USB 錯誤類 + 中段 Play Controls 類),gpt-4.1。
> 輸出:`archive/M1/baseline_player_llm/`(早段)、`.../mid/`(中段)。**總花費 < $0.10。**

## 最關鍵發現:regex 完全看不到的「拆解不夠深」

語意層的 Tier 1(§6.x Critical)直接量出**枚舉/負向覆蓋不足**——這正是你最初的痛點:

| Req | 規則 | 缺什麼 |
|---|---|---|
| PLA-001 | §6.3 | 不支援檔案格式只測 .txt/.pdf,缺 .exe/.apk/亂碼副檔名 |
| PLA-027 | §6.3 | Play Controls 列了 Skip/Repeat/Shuffle/Progress,只測 Play/Pause |
| PLA-028 | §6.1 | Play/Pause 二元只測正向,缺 Pause 態不顯示 softkey 的負向 |
| PLA-030-01 | §6.3 | 只測 Repeat All,缺 Repeat One / No Repeat |
| PLA-030-02 | §6.1 | 連續循環只測正常切換,缺單曲循環 / 空清單負向 |
| PLA-030-03 | §6.1 | 單曲循環缺播完異常態負向 |

**量化:取樣 13 個 Req group 裡 6 個(~46%)有 Critical 拆解缺口。regex pass 對這些 0 命中。**

## Tier 2 對齊(「和實際 spec 有落差」)

- §7.2:PLA 的 ER 只驗 popup 持續顯示,**漏掉 Req 指定的錯誤訊息格式 `(Device Name) error`** → 真實 spec-fidelity 落差。

## 三個結論

1. **「拆解不夠深」被量化證實**:~46% 需求枚舉/負向覆蓋不足,且**只有語意 review 抓得到**。這同時驗證 Stage 3(深拆)與 Stage 6(語意 review)兩個改造的必要性。
2. **regex baseline 會嚴重低估問題**:它的 525 筆全是寫作層(Tier 3),完全沒碰到上面這些覆蓋缺口。
3. **scorecard 該新增一個 KPI**:`tier1_critical_req_rate`(有 Critical 拆解問題的 Req 比例)——它直接衡量拆解深度,比現有 KPI 更貼合核心目標。

## 方法限制

- 取樣 ~22 TC、gpt-4.1(非最強);完整 157 TC + 更強模型的數字會更穩,但結論方向已非常明確。
- 45 秒窗讓「一次跑完 157」不可行;若要完整,建議你在本機 / 互動式跑 `--review`(分批或背景)。
