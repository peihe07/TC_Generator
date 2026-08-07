# TC Generator — 端到端 Pipeline 設計(互動式為主)

> 目標:把現有「OpenAI API 批次生成」改造成「深拆 + domain 接地 + spec 核查 + 自動 review + KPI 量化」的 pipeline。
> **主路徑用互動式 Claude Code(訂閱額度,邊際成本 0)**,Python 處理確定性工作,人工只審「疑慮」而非逐條。
> 自動化 / 大量無人值守再走 API(按量計費)。

文件狀態:設計草案 · 最後更新 2026-06-25

---

## 設計原則(先讀這段)

0. **互動式為主。** 主要工作流是「你坐在 Claude Code 互動式 session 裡,用 subagent 驅動深拆 / 生成 / review」——這部分算進你的 Max 訂閱額度、不額外計費。**腳本 / headless(`claude -p`、Agent SDK)自 2026/6/15 起按 API 費率計費**,只在真的需要無人值守大量產出時才用。
1. **確定性的歸 Python,需要判斷的才給 LLM。** Excel 進出、ID、traceability、欄位完整性 → Python;深拆、生成、語意 review → agent。
2. **LLM backend 解耦。** 所有 LLM 呼叫走同一個 provider interface(現集中在 `generator.py::_chat`),底下可插 互動式 session / Claude API / OpenAI。
3. **domain knowledge 做成「審一次、重複用」的 artifact**,不要每條 TC 讓模型重猜。
4. **retrieval 已經有了**(`spec_matcher`:PDM → Jaccard → embedding),不重做。
5. **review 要 spec 接地、domain 感知**,而不是只比格式(見 Stage 6)。
6. **人工只在兩個 gate 介入**:① domain pack 審查(早期、便宜)② 最終疑慮 report(只看被標記的)。

---

## 運行模式與成本(互動式為主)

### 兩種運行模式

| | 互動式 Claude Code(主路徑) | Headless / API(備援) |
|---|---|---|
| 怎麼跑 | 你在 `claude` session 裡驅動 subagent | `claude -p` 腳本 / Agent SDK / 直接 Anthropic API |
| 計費 | 算進 **Max 訂閱額度**,邊際成本 0 | **按 API token 計費**(6/15 後 headless 亦然) |
| 限制 | 5 小時滾動 + 每週上限;**需你在場** | 無硬上限,可無人值守、高併發 |
| 用在 | 深拆 / 生成 / review / Gate ① 的人在迴圈階段 | 真正大量、排程、自動跑的批次 |

> 重點:**「跑腳本」= API 計費**。要用訂閱免費額度,流程必須是互動式、你親自推進。

### Token 量(用真實檔案估)

進 prompt 的固定成本:ASPICE 規則 ~7k tokens、Review spec ~6.5k、Domain pack(新)~10k。
這些都應做成**快取前綴**(cache 讀取只算 10% 價格),是最大省法。

**新版深拆 + 獨立 review,每個需求約 35k–70k tokens(典型 ~50k)**,換算每條 TC ~10k——
比現行批次版(~2.3k/TC)重 4–8 倍。**這是「深度」的必然代價**:深讀 spec + domain + 獨立稽核。

### 一次 run 估算(可換成你的真實需求數)

| 需求數 | 總 token | 互動式 Max 5x(Sonnet) | Headless/API(Sonnet,開快取) | Opus |
|---|---|---|---|---|
| 100 | ~5M | $0 額外(Sonnet 在 Max 5x 近乎用不完) | ~$15–25 | ~$27 |
| 200 | ~10M | 可能撞 5 小時窗,需分批 | ~$30–50 | ~$54 |

- 開 **Batch API** 可再砍一半(非即時,24h 內回)。
- **深拆用 Sonnet,必要時局部用 Opus**:Max 5x 的 Sonnet 一般工作量用不完,但 Opus 每週僅約 50–75 小時,會明顯吃額度。
- 估算為 order-of-magnitude;實際取決於需求數、每需求 match 多少 spec、每需求產幾條 TC。

### 降 token 的槓桿

1. 規則 / Review spec / Domain pack 當**快取前綴**(讀取算 10%)。
2. review **逐需求批次**送,不逐 TC(共用同一份 spec 切片)。
3. 機械填充階段(Stage 4)可用便宜模型;深拆(Stage 3)才用較強模型。

> 價格基準(2026-06):Sonnet 4.6 $3/$15、Opus 4.8 $5/$25、Haiku 4.5 $1/$5(input/output 每 M token);cache hit = input 價 10%;Batch = 50% off。

---

## Pipeline 總覽

```
[Phase 0] Provider 解耦 (前置改造,一次性)
     │
     ▼
Stage 0  Spec Intake & Inventory        ── Python ── 已有索引基礎
     │
     ▼
Stage 1  Domain Knowledge Pack  ★新     ── 互動式 agent ── ▶ 人工 Gate ①
     │
     ▼
Stage 2  Requirement Scan & Context     ── Python(spec_matcher)── 已有
     │
     ▼
Stage 3  Deep Decompose          ★改造  ── 互動式 agent(Sonnet,深讀)
     │
     ▼
Stage 4  TC Generation                  ── agent / 便宜模型 ── 改造
     │
     ▼
Stage 5  Completeness Check             ── Python(validator)── 已有,不用 AI
     │
     ▼
Stage 6  Review Agent  ★強化            ── 獨立 agent(spec 接地 + domain)+ regex
     │
     ▼
Stage 7  Report + KPI Scorecard  ★新    ── Python 組裝
     │
     ▼
Stage 8  Human Review                   ── 人 ── ▶ 人工 Gate ②
     │
     ▼
Stage 9  Export                         ── Python(writer)── 已有
     │
     └──────── KPI 未達標 → 退回 Stage 3/4 重生成(feedback loop)
```

---

## Phase 0 — Provider 解耦(前置,一次性)

| 項目 | 內容 |
|---|---|
| 目的 | 把 `_chat` 抽成 `LLMProvider` interface,可插互動式 session / Claude API / OpenAI,並能 A/B 比較深度 |
| 輸入 | messages、model、參數 |
| 輸出 | 統一 response + usage(互動式模式 usage 退化為 request/額度計數) |
| 引擎 | — |
| 狀態 | **改造**(`_chat` 已是唯一呼叫點,工作量小) |
| 備註 | `_budget.py` 的「美金預算」在互動式模式改成「rate-limit 排隊 / 每窗請求數」;注意 `ANTHROPIC_API_KEY` 環境變數會讓 Claude Code 改走 API 計費 |

---

## Stage 0 — Spec Intake & Inventory

| 項目 | 內容 |
|---|---|
| 目的 | 盤點本次專案所有來源文件,確認都已建索引 |
| 輸入 | SYS1 / spec PDF·DOCX·XLSX、需求 workbook |
| 輸出 | spec 清單 + 索引狀態(`spec-index/manifest.json`) |
| 引擎 | Python |
| 狀態 | **已有**(`scripts/build_spec_index.py`、embedding 索引已建 200+ 條) |
| KPI hook | 來源文件覆蓋率(已索引 / 應索引) |

---

## Stage 1 — Domain Knowledge Pack ★新(最關鍵的新增)

| 項目 | 內容 |
|---|---|
| 目的 | 萃取穩定的 domain 背景,解決「background 不夠 → 拆解淺」的根因 |
| 輸入 | 全部 spec(透過索引)+ 需求總覽 |
| 輸出 | 一份持久化 artifact(見下方 schema),**人工審一次後重複用** |
| 引擎 | 互動式 agent(深讀整包) |
| 狀態 | **新增** |
| 人工 Gate | **Gate ①** — 在生成任何 TC 前先審「模型對 domain 的理解對不對」 |
| KPI hook | open-questions 數量、人工修正數(理解品質的早期指標) |

**Domain Pack schema(草案,可調):**
- `glossary` — 術語 / 縮寫對照(HFP、A2DP、BLE… 的定義與行為)
- `feature_model` — 各 feature 的正常 / 異常 / 邊界行為摘要
- `interactions` — 跨 feature 互動與互斥(哪些狀態會互相影響)
- `boundaries` — 已知數值邊界、列舉值、上下限
- `traceability_hints` — 需求 ↔ spec 的對應線索(補 `spec_matcher` 的語意缺口)
- `open_questions` — 規格不清、需人工澄清的點(Gate ① 的審查清單)

> 原則:每個欄位都要被下游 Stage 3/4/6 真的消費到,否則不寫。不做「抽象地理解 domain」。

---

## Stage 2 — Requirement Scan & Context Assembly

| 項目 | 內容 |
|---|---|
| 目的 | 逐需求抓出相關 spec 切片,組成該需求的生成 context |
| 輸入 | 需求列、domain pack、spec 索引 |
| 輸出 | 每需求一包 context(相關 spec 段落 + 對應的 domain pack 片段) |
| 引擎 | Python(`spec_matcher`:PDM 精確 → Jaccard → embedding cosine) |
| 狀態 | **已有** |
| KPI hook | 每需求 retrieval 命中數、traceability 完整度 |

---

## Stage 3 — Deep Decompose ★改造重點

| 項目 | 內容 |
|---|---|
| 目的 | 像手動那樣深拆:**一需求一支 subagent**,自己深讀切片 + domain pack 再拆 |
| 輸入 | 單需求 context 包 |
| 輸出 | 該需求的拆解計畫(情境 / 分支 / 邊界 / 列舉,尚未填欄位) |
| 引擎 | 互動式 agent(Sonnet 為主,深讀;必要時局部 Opus);ASPICE 規則打包成 skill 自動載入 |
| 狀態 | **改造**(`build_decompose_prompt` 已存在,但目前被塞進批次,需改成單需求 agent 扇出) |
| KPI hook | 平均拆解步數 / 需求(對抗「不夠深」) |

> 把 `ASPICE_SWE6_AI_Instruction.md`、`TEST_CASE_DESIGN_METHOD.md`、`TEST_CASE_PRIORITY.md` 打包成 skill,每支 agent 自動載入 → 解決 background 不夠。

---

## Stage 4 — TC Generation

| 項目 | 內容 |
|---|---|
| 目的 | 把拆解計畫的每一項填成完整 TC 欄位 |
| 輸入 | Stage 3 拆解計畫 |
| 輸出 | TC 草稿(tc_title / pre_conditions / input_test_data / test_procedure / expected_result / design_method / priority / split_flag / split_reason) |
| 引擎 | 機械填充,互動式或便宜模型;Test Set 分類維持便宜模型 |
| 狀態 | **改造**(沿用 `prompt_builder` 既有欄位契約與 hard constraints) |
| KPI hook | 生成數量、單需求 TC 數 |

---

## Stage 5 — Completeness Check(確定性,不用 AI)

| 項目 | 內容 |
|---|---|
| 目的 | 檢查「所有欄位有沒有填好、格式對不對」——純規則 |
| 輸入 | TC 草稿 |
| 輸出 | 缺漏 / 格式違規清單(structural errors) |
| 引擎 | **Python**(`validator.py` regex pre-pass) |
| 狀態 | **已有** |
| KPI hook | 欄位完整率、格式合規率 |

> 重要:這步**不要用 agent**。「有沒有填」是確定性問題,Python 做零成本零誤差。與 Stage 6 的「填得對不對」分流。

---

## Stage 6 — Review Agent ★強化(spec 接地 + domain 感知)

**為什麼要強化:** 現行 `review_engine` 的可執行性檢查(§8.3.x)多是 regex 形狀檢查,驗的是**格式**不是**真能不能執行**;
Tier 2 雖錨到 Req spec句,但只餵一行句子,看不出「步驟和實際行為的落差」。要解決你擔心的「步驟不夠明確執行、和實際有落差」,review 要做四件事:

| 強化點 | 內容 |
|---|---|
| 1. 同等 grounding | 把 `spec_matcher` 抓到的**完整 spec 切片** + **domain pack** 餵進 review context,而不是只給一行 Req spec句 |
| 2. spec fidelity / reality-gap 規則(新) | 逐 TC 比對 `test_procedure` + `expected_result` 與 spec 實際行為,標出:(a) 步驟假設了 spec 沒定義的行為、(b) expected_result 對不到具體 spec 結果、(c) 漏掉 spec 定義的分支 |
| 3. 可執行性改語意檢查 | 用一支「只拿 spec + domain、拿不到 generator 推理」的 agent 照步驟**心智執行一遍**,卡住的地方(誰執行不明 / 缺前置 / 無可觀察結果)就標記 |
| 4. 獨立稽核 + 證據引用 | reviewer **看不到 generator 的推理**,只看 TC + spec + domain,才抓得到隱藏假設;每個 flag 必須引用支持/牴觸它的 **spec 原句**(擴充現有 `evidence` 欄位,連 spec 來源一起引) |

| 項目 | 內容 |
|---|---|
| 目的 | 語意層稽核:步驟能不能確實執行、內容和實際 spec 有無落差、是否違反 ASPICE SWE.6 |
| 輸入 | 通過完整性檢查的 TC + 完整 spec 切片 + domain pack |
| 輸出 | §9 schema findings(rule_ref / severity / tier / spec evidence / 建議修正) |
| 引擎 | hybrid:20 條 regex + 11 條 LLM,**新增 reality-gap / 可執行性語意規則**;獨立 agent |
| 狀態 | **強化**(`review_engine.py` + `review_prompt_builder.py` 既有,新增 grounding 與規則) |
| KPI hook | 各 rule 違反次數、severity 分佈、reality-gap flag 數 |

> 核心:把 review 從「規則比對」升級成「spec 接地、domain 感知的稽核」——reviewer 拿著 spec 原文證據說話,而不是只比格式。

---

## Stage 7 — Report + KPI Scorecard ★新

| 項目 | 內容 |
|---|---|
| 目的 | 把完整性 + findings 彙整成人工只需看「疑慮」的 report,並算 KPI |
| 輸入 | Stage 5 結構錯誤 + Stage 6 findings |
| 輸出 | `findings_report.md`(已有)+ **KPI scorecard(新)** |
| 引擎 | Python 組裝(幾乎不花 AI 成本) |
| 狀態 | **新增 scorecard**(report 本體已有) |

**KPI 定義(公司要的量化):**
- **一次通過率** = 零 Critical/Major finding 的 TC 數 / 總 TC 數 ← 最重要的品質指標
- **需求覆蓋率** = 有產 TC 的需求 / 總需求
- **Traceability 完整度** = 有對到 spec 的 TC / 總 TC
- **Design method 正確率** = 設計方法符合規則的 TC 比例
- **平均拆解深度** = 平均每需求拆解步數
- **欄位完整率** = 通過 Stage 5 的 TC 比例
- **Reality-gap 率** = 被 Stage 6 標出落差的 TC 比例(你擔心的「和實際有落差」的量化)

---

## Stage 8 — Human Review(Gate ②)

| 項目 | 內容 |
|---|---|
| 目的 | 人工只審被標記為疑慮的 TC,不逐條看 |
| 輸入 | KPI scorecard + 被標記的 findings |
| 輸出 | 確認 / 退回(退回觸發 feedback loop) |
| 引擎 | 人 |
| 狀態 | 流程定義 |

---

## Stage 9 — Export

| 項目 | 內容 |
|---|---|
| 目的 | 寫回 Excel(原 workbook 格式) |
| 輸入 | 確認後的 TC |
| 輸出 | 輸出 workbook |
| 引擎 | Python(`writer.py`) |
| 狀態 | **已有** |

---

## Feedback Loop(KPI 驅動的改進)

```
Stage 7 KPI 未達門檻(例如一次通過率 < 80%)
   → 分析 findings 集中在哪幾條 rule
   → 調整 skill / decompose prompt / domain pack
   → 退回 Stage 3/4 重生成被標記的需求
   → 重新量 KPI
門檻穩定後 → 才放大批量(才知道一個 run 能穩定吃多少量)
```

---

## 既有 / 改造 / 新增 一覽

| 狀態 | 項目 |
|---|---|
| **已有(沿用)** | spec 索引、`spec_matcher`、`validator`、`review_engine`、`writer`、`prompt_builder` 欄位契約 |
| **改造** | `_chat` → provider 解耦、`decompose` → 單需求 agent 扇出、生成填充層 |
| **強化** | Review(Stage 6)→ spec 接地 + domain 感知 + 可執行性語意檢查 + 獨立稽核 |
| **新增** | Domain Knowledge Pack(Stage 1)、KPI Scorecard + Reality-gap 指標(Stage 7) |

---

## 建議落地順序

1. **Phase 0 解耦** + **Stage 7 scorecard**(都低風險、馬上有用:能比較引擎、拿到 baseline KPI)
2. **Stage 1 Domain Pack** schema + 單專案試做 + Gate ① 流程
3. **Stage 3 深拆 PoC**:單需求互動式 agent,對比現行 gpt-5 批次的深度
4. **Stage 6 review 強化**:接 spec 切片 + domain pack,加 reality-gap / 可執行性語意規則
5. KPI 穩定後,決定 Stage 4 填充層要不要混便宜模型 / 是否值得做 headless 批量(API 計費)放大量

---

## 決策紀錄(本次討論結論)

- **主路徑定為互動式 Claude Code**(訂閱額度、邊際成本 0);headless/API 僅作大量無人值守的備援。
- **沒有「agent 訂閱」這種獨立產品**;subagent 是 Claude Code 功能。但 2026/6/15 起 headless / Agent SDK 按 API 費率計費,訂閱免費只在互動式成立。
- **review 是重點疑慮**:必須 spec 接地、domain 感知、能查核可執行性,並做獨立稽核(reviewer 看不到 generator 推理)。
- **深度有成本**:深拆 + 獨立 review 約 50k tokens/需求(~10k/TC),互動式 Sonnet 下一次 100 需求 run 基本算進 Max 5x 方案內、不另計費,代價是需你在場且受 rate-limit。

---

# 附錄:現有 TC Generator 系統全貌(供細部規劃用)

> 這一整段把現有 codebase 的資訊萃取進來,讓本文件 self-contained。
> 之後可整份丟給 Claude chat 做細部規劃,再交給 Claude Code 開發。
> 資料萃取自 backend 原始碼、`docs/`、`backend/rules/review_rules.yaml`(2026-06-25)。

## A. 系統概觀

- 用途:ASPICE SWE.6 自動測試案例(TC)生成與審核工具。
- 兩個工作面:① Python backend + CLI(parse / generate / validate / review / export)② Next.js 桌面前端(Win95 風格單頁 desktop,另有獨立 `frontend-modern/` 變體)。
- 技術棧:Python ≥3.10、FastAPI、Next.js、SQLite job store(`output/jobs.db`)、OpenAI(目前 gpt-5 系列)。
- Python 依賴:`openai>=1.50`、`fastapi`、`openpyxl`、`pdfplumber`、`python-docx`、`python-dotenv`、`pyyaml`、`uvicorn`;dev:`httpx`、`pytest`、`pytest-cov`。
- 前後端邊界:瀏覽器只打 same-origin `/api/*`(Next.js proxy),再轉 Python backend(`PYTHON_API_BASE`)。

## B. Backend 模組地圖

| 模組 | 行數 | 職責 |
|---|---:|---|
| `parser.py` | 127 | 解析 TC spec workbook;預期 sheet `Product Document 記錄封面頁` + `Test Case Specification 測試用例規範`;檔名規則 `*_SWQT_{TestGroup}_YYYYMMDD.xlsx` 取 Test Group |
| `spec_parser.py` | 138 | 解析補充 spec(PDF / DOCX / XLSX)→ 以 PDM code 為 key 的文字段落 |
| `spec_matcher.py` | 550 | 三層 spec 對應:① PDM code regex 精確 ② token Jaccard 模糊 ③ embedding cosine(`text-embedding-3-large`);離線預建索引 |
| `generator.py` | 1149 | LLM 呼叫 / 回應解析 / 成本追蹤;model policy、batch、1:1 enforcement、model escalation、retry、prompt cache、timeout |
| `prompt_builder.py` | 1274 | 生成 prompt;auto-load ASPICE 規則;9 個 `REQUIRED_OUTPUT_KEYS`;decompose / batch / multi-TC / Test Set 分類 prompt |
| `grouper.py` | 116 | Test Set capability 分組 |
| `id_generator.py` | 96 | TC ID `{project}-{abbr}-{NNN}`;segment sanitize;從 CamelCase Test Group 產縮寫 |
| `validator.py` | 445 | **純程式**欄位驗證(無 AI);逐欄 validator + priority/design method 正規化 |
| `writer.py` | 405 | 寫回 Excel;產 `Test Case Framework` sheet;Col I 原文後接 rewrite;Col R reasoning header「AI 需求解讀」;TC ID resequence |
| `job_manager.py` | 165 | review workflow job 狀態管理 |
| `job_store.py` | 210 | SQLite job registry(dict-like),`output/jobs.db` |
| `review_engine.py` | 1195 | 審核管線:parse → group → Tier1/2/3 → 互斥/抑制 → severity ceiling → §9 schema |
| `review_prompt_builder.py` | 234 | 審核 prompt;auto-load Review spec |
| `review_assistant.py` | 151 | 單筆 TC 修正建議(root cause / fields / change / reason) |
| `rules_loader.py` | 81 | runtime 規則載入 |
| `api_server.py` | 2611 | FastAPI server(全部 endpoint) |
| `main.py` | 414 | CLI 入口(generate + review 兩種模式) |

## C. TC 資料模型(output contract)

生成必填 9 欄(snake_case,寫回 workbook 一律英文):
`tc_title`、`pre_conditions`、`input_test_data`、`test_procedure`、`expected_result`、`design_method`、`priority`、`split_flag`、`split_reason`。

附加欄位:`reasoning`(繁中 2–5 句,寫入 Col R「AI 需求解讀」)、`duplicate_of`(sibling 等價列號)、`distinguishing_axis`(`trigger_state | input_data | timing | boundary | mode | none` + delta)。

ID 格式:`{project}-{group_abbr}-{NNN}`(3 碼零補);Priority 嚴格 `P0/P1/P2/P3`。

## D. 生成管線(現行)

`parse`(workbook→rows)→ `group`(Test Set 分類,固定 `gpt-5-mini`)→ `match`(spec_matcher traceability)→ `decompose_requirement`(拆分判斷 + sibling 偵測)→ `generate_tcs_for_row`(產 TC 欄位,batch=5)→ `validator`(程式驗證)→ `writer`(寫回 Excel + resequence ID)。

Sibling-aware:同 Requirement ID 多列時互相注入 test_item,AI 須回 `duplicate_of` + `distinguishing_axis`,backend 做 cross-validation。

## E. Generator 行為細節

- Model policy:`DEFAULT_MODEL = gpt-5`(UI 另有 `gpt-5.4`);`CLASSIFICATION_MODEL = gpt-5-mini`(Test Set 固定、不受使用者 model 影響)。
- `MODEL_PRICING` 內建各 model 單價(含 cached_input);`MODEL_ESCALATION`:1:1 違反重試仍失敗時 `gpt-5-mini→gpt-5`、`gpt-4o→gpt-4.1`。
- Retry:暫時性錯誤 `{500,502,503,504,529}`,首次 + 最多 2 次重試;單次 request timeout 預設 180s。
- 1:1 enforcement:step ↔ ER 數量對齊;違反會重試 / 升級 model。
- Prompt cache:利用 OpenAI ≥1024 token prefix 快取(規則 / spec context 當前綴)。
- 成本:逐 batch persist usage 到 job DB;前端 CostMeter / dashboard 顯示 per-kind / per-model。

## F. Review 系統(31 條規則)

管線:`parse → group by Req ID → Tier1(§6.x) → Tier2(§7.x,跳過 tier1_skipped group) → Tier3(§8.x,永遠跑) → 互斥(§7.4 ⊕ §8.3.6)+ 抑制(§6.4 → §8.1.4) → severity ceiling → §9 schema`。Tier3 嘗試輸出 Critical 會拋 `ReviewEngineError`。
severity ceiling:Tier1 Critical / Tier2 Critical / **Tier3 max Major**。約 20 條 regex、11 條需 LLM(語意比對)。輸出 `findings.json` + `findings_report.md`。

| Rule | Tier | Severity | 主旨 |
|---|---|---|---|
| §6.1 | 1 | Critical | 缺 supported/negative 配對 |
| §6.2 | 1 | Critical | 缺 boundary 軸 |
| §6.3 | 1 | Critical(LLM) | 缺列舉覆蓋 |
| §6.4 | 1 | Major | sibling 軸不明 |
| §6.5 | 1 | Critical | sibling 間 spec句 不一致 |
| §6.6 | 1 | Major | Tier1 無 spec句、不可執行 |
| §6.7 | 1 | Major | 單一 TC 多 Req ID |
| §7.1 | 2 | Critical(LLM) | Test Item 結果不在 Req spec句 |
| §7.2 | 2 | Major/Critical(LLM) | ER 未覆蓋 Req 結果元素 |
| §7.3 | 2 | Major(LLM) | Pre-Cond 與 Req trigger 重複/矛盾 |
| §7.4 | 2 | Critical | 捏造數值、無法追溯 Req/spec |
| §7.5 | 2 | Critical | 末步驟啟動工具卻沒讀結果 |
| §8.1.1 | 3 | Major | Test Item 長度超範圍 |
| §8.1.2 | 3 | Major | Test Item 出現 modal/hedge 字眼 |
| §8.1.3 | 3 | Info | 多語言混雜 |
| §8.1.4 | 3 | Major | 缺 sibling 區別 token |
| §8.1.5 | 3 | Critical* | 無 spec句 也無可追溯 Req(*僅 Req ID 也空時) |
| §8.2.1 | 3 | Major | Pre-Cond 出現動作動詞 |
| §8.2.2 | 3 | Major | Pre-Cond 出現驗證動詞 |
| §8.2.3 | 3 | Minor | 系統預設被當成 Pre-Cond |
| §8.2.4 | 3 | Critical(LLM) | 受測功能被當成已就緒 |
| §8.2.5 | 3 | Minor | Pre-Cond 綁特定 instance |
| §8.3.1 | 3 | Major | 禁用動詞 / 猜測語氣 |
| §8.3.2 | 3 | Major | 步驟缺可執行內容 |
| §8.3.3 | 3 | Major | 單步驟流程 |
| §8.3.4 | 3 | Minor | 步驟編號異常 |
| §8.3.5 | 3 | Critical | 末步驟無檢查標的 |
| §8.3.6 | 3 | Major | 捏造數值(Tier2 fallback) |
| §8.4.1 | 3 | Major | ER 結果用語含糊 |
| §8.4.2 | 3 | Major(LLM) | step ↔ ER 數量不符 |
| §8.4.3 | 3 | Minor | ER 編號異常 |
| §8.5.1 | 3 | Major | Priority 不在 P0–P3 |
| §8.5.2 | 3 | Major | Design Method 缺失 |
| §8.5.3 | 3 | Major(LLM) | Design Method 與 Procedure 不一致 |

§9 輸出 schema:top-level shape、per-Req finding(Tier1)、per-TC finding(Tier2+3)、batch summary。

## G. spec-index / retrieval 機制

- 離線:`scripts/build_spec_index.py` 解析 `spec-index/cache/*.xlsx` → `build_spec_index` → `attach_embeddings`(`text-embedding-3-large`)→ 存 `<name>.json` + 更新 `manifest.json`。
- 執行:`load_spec_index` 依名稱載入,`match_spec_references` 對應;有 embedding 走 cosine,否則 fallback Jaccard。
- 現況:`manifest.json` 已索引 200+ 條 SYS1 spec(每條 entry ~150 字元)。

## H. ASPICE 規則文件地圖(auto-load 進 prompt)

- `ASPICE_SWE6_AI_Instruction.md`(19.7k 字元):§0 Purpose / §1 Language / §2 Core Principles / §4 Workflow / §6 Field Rules(6.0 Test Set、6.1 tc_title 三型、6.2 Pre-Cond、6.3 Input Data、6.4 Sibling)/ §7 Step Design(7.1 Executable、7.5 Final Step、7.6 Baseline、7.7 One Objective、7.8 Setup Snippets、7.9 Tooling/CLI、7.10 Step Length)/ §8 Expected Results / §9 False Pass-Fail / §10 Requirement Alignment / §11 Self-Check / §12 Output Contract / §13 Formatting / §15 Design Method / §16 Final Rule。
- `ASPICE_SWE6_AI_Review.md`(25.5k 字元):§3 Three-Tier Model / §4 Severity Rubric / §5 Workflow / §6 Tier1 / §7 Tier2 / §8 Tier3 / §9 Output Contract / §10 Self-Check。
- `TEST_CASE_DESIGN_METHOD.md`:9 種設計方法(Functional based / State Transition / Decision Table / Equivalence Partitioning / Boundary Value / Combinatorial / Scenario / Negative / Fault Injection Lite)+ first-match 快速判斷流程。
- `TEST_CASE_PRIORITY.md`:P0–P3 定義(P0 核心 happy path 預設、P1 次要/邊界、P2 輔助、P3 UI 強化)+ IVI / CAN 範例。
- `TEST_SET_POLICY.md`:Test Set = capability 級分組;命名規則(短英文名詞、不重複 Test Group prefix、禁 `Unclassified`/`Misc`/placeholder)。

## I. API Routes(api_server.py)

主要 endpoint(瀏覽器走 `/api/*` proxy):`/api/health`、`/api/spec-library`、`/api/parse`、`/api/group`、`/api/match`、`/api/generate` + `/api/generate/stream`(SSE)、`/api/review/suggest-fix`、`/api/audit`(SWE.6 審核,`dry_run` 預設跳 LLM)、`/api/jobs/{id}/regenerate|rerun/stream`(SSE)、`/api/jobs/{id}/usage|source-status|attach-raw`、`/api/export` + `/api/export/download/{id}`、`/api/quick-generate/stream`、`/api/metrics/aggregate`、`/api/admin/reset`(localhost destructive)。

SSE 事件:generate(`job.started`/`req.split`/`row.completed`/`row.added`/`job.completed`)、regenerate(`regen.started`/`row.regenerated`/`row.regen_failed`)、quick(`decompose.analysis`/`tc.generating`/`tc.completed`)。

## J. 前端架構

- Legacy `frontend/`:Win95 單頁 desktop;modules:Upload / Configure / Generate / Review / Audit / Export / QuickGenerate / Rules / Diagrams(`*Module.tsx`)。
- Zustand stores:`useWindowStore`、`useJobStore`、`useJobHistoryStore`、`useWorkspaceStore`。
- 單一 adapter:`frontend/src/services/jobAdapter.ts`;所有 backend 存取走 `frontend/app/api/*` proxy。
- Modern 變體 `frontend-modern/`:獨立 package、ports(FE 3433 / BE 8013)、自己的 README / Vitest / Playwright / Dockerfile。
- 重要邊界:Agent routes / ChatModule / trace/session store 已移除,不要新增依賴。

## K. CLI(main.py)

生成:`python backend/main.py --input X.xlsx [--sys1 --spec --framework --output-dir --model gpt-5 --batch-size 5 --mode full|incremental|regenerate --rows --dry-run --budget --strict-validation]`。
審核:`python backend/main.py --review --input X.xlsx --output-dir output [--dry-run]` → `findings.json` + `findings_report.md`(與 generate-only flags 互斥)。

## L. 測試 baseline

- backend:26 個 test 檔(`tests/test_*.py`);CHANGELOG 記錄 528 backend tests pass(含 review_engine 20、audit endpoint 2)。
- modern frontend:`npm run test:unit` 20 files / 134 tests pass;另有 Playwright E2E。
- 慣例(依使用者偏好):Python pytest、JS Jest/Vitest。

## M. 現有元件 → 新 Pipeline 對應

| 現有元件 | 對應 Stage | 處置 |
|---|---|---|
| `parser` / `spec_parser` | Stage 0 / 2 | 沿用 |
| `spec_matcher` + spec-index | Stage 2 | 沿用(retrieval 已完成) |
| ASPICE docs + `prompt_builder` | Stage 1 skill / 3 / 4 | 打包成 skill,改 prompt 結構 |
| `generator`(decompose/generate) | Stage 3 / 4 | **改造**:`_chat` provider 解耦 + 單需求 agent 扇出 |
| `validator` | Stage 5 | 沿用(確定性、不用 AI) |
| `review_engine` + rules + `review_prompt_builder` | Stage 6 | **強化**:spec 切片 grounding + domain pack + reality-gap / 可執行性語意規則 |
| `writer` | Stage 9 | 沿用 |
| `job_store` / `job_manager` | orchestration 狀態 | 沿用 / 調整 |
| `api_server` / 前端 | 選用 UI 層 | 視是否保留桌面 UI |

## N. 給 Claude chat 規劃時的已知缺口 / 待決

- ~~Provider 解耦尚未做~~ → **已完成**(`backend/providers/`)。
- ~~Domain Knowledge Pack(Stage 1)~~ → **已完成**(`domain_pack.py` + `M1/domain_pack_*.json`)。
- ~~KPI Scorecard(Stage 7)~~ → **已完成**(`scorecard.py`,9 KPI;trace+validation 已接)。
- ~~Review 強化(Stage 6)~~ → **已完成**(domain pack + content-trace + reality-gap 已餵入)。
- ~~互動式 vs headless 的 orchestration~~ → **已落地**:見下方 SOP。
- 待續:L2 SPEC 覆蓋做成 KPI;Stage 3/4 單需求 agent 扇出;補進度條/Shuffle 缺口測項(見 `M1/spec_coverage_gaps_final.md`)。

---

## O. 互動式 Review SOP(訂閱、$0,主路徑)

> 目標:整條 review 的語意層由 Claude 在互動式 session 裡做,**不打 API、算 Max 訂閱額度**。
> 確定性層(parser / traceability / scorecard / regex 規則)永遠純 Python、$0。

### 三步流程

```bash
# 1) export — 純 Python 產 context 包(regex findings + 每批 prompt),不打 API
python backend/main.py --export-bundle \
  --input "<TC.xlsx>" --output-dir output/X \
  --domain-pack M1/domain_pack_<proj>.json --swe1-reqs M1/swe1_<proj>_reqs.json
#    → output/X/review_bundle.json(N 批,每批含 user_prompt + answer:null)
```

```text
# 2) Claude 在 session 裡:讀 review_bundle.json,逐批讀 batches[i].user_prompt,
#    產出 §9-schema 的 answer JSON 填回 batches[i].answer。← 訂閱額度、$0
#    (可分段做;未填的批在 assemble 時退化為 regex-only,不會壞)
```

```bash
# 3) assemble — 純 Python 把答案併成最終報告 + scorecard,不打 API
python backend/main.py --assemble output/X/review_bundle.json \
  --output-dir output/X --swe1-reqs M1/swe1_<proj>_reqs.json
#    → findings.json / findings_report.md / scorecard.json / scorecard.md
```

### 設計重點

- API 路徑(`--review --model`)與互動橋**共用** `_build_payload_tcs` / `_build_review_batches` / `_accumulate_llm_findings`,兩者 findings 結構完全一致,只差「語意那一步誰做」。
- bundle 是純資料檔(prompt + 答案 + regex findings),可版本控管、可重現、可分段填。
- headless / API 路徑(`--review --model gpt-4.1`)保留為「大量無人值守」備援(計費)。

### 計費對照

| | 互動橋(主路徑) | headless / API(備援) |
|---|---|---|
| 語意層 | Claude in session | 腳本打 gpt-4.1 / Claude API |
| 計費 | **訂閱額度,$0** | API token |
| 適用 | 你在場、逐步、品質可控 | 大量、排程、無人值守 |

---

## P. 互動式生成 SOP(SPEC 接地 + 兩層合規,$0)

> 單需求深拆 + 多 TC 扇出,接地在 **Domain Pack + SPEC 原文 PC + 權威規則**(`load_rules()`:AI Instruction / 判斷規則 / priority)。語意層在 session 做,訂閱 $0。

### 流程(一個 feature 家族一輪)

```bash
# 1) export — 每需求組 SPEC 接地 context;system_prompt 帶權威規則。不打 API
python backend/main.py --gen-export-bundle \
  --swe1-reqs M1/swe1_<proj>_reqs.json --domain-pack M1/domain_pack_<proj>.json \
  --spec-coverage M1/spec_coverage_<proj>.json \
  --req-ids <該家族的 req ids> --output-dir output/gen_<family>
```
```text
# 2) Claude 在 session 裡:每需求填 {decomposition, test_cases}。← 訂閱 $0
#    - 拆解看 SPEC 原文,SPEC-only 行為標 source:"spec-only"
#    - 欄位寫法 / Design Method / Priority 全依 system_prompt 的權威規則
```
```bash
# 3) assemble — 攤平 + 第一層確定性合規閘(method/priority/必填),寫 xlsx
python backend/main.py --gen-assemble output/gen_<family>/gen_bundle.json \
  --output-dir output/gen_<family>
#    → generated_tcs.json / generated_tcs.xlsx(Compliance: ✓ / N off rules)

# 4) 第二層寫作規則稽核 — 把生成的 xlsx 丟回 review(§8.x)
python backend/main.py --review --dry-run \
  --input output/gen_<family>/generated_tcs.xlsx \
  --output-dir output/gen_<family>/audit --swe1-reqs M1/swe1_<proj>_reqs.json
#    → 若 §8.x 有違規(禁用動詞/模糊用語/Final Step),修 procedure/ER 後重跑 3-4
```

### 兩層合規保證

| 層 | 查 | 在哪 |
|---|---|---|
| 確定性閘 | Design Method 控制詞彙、Priority P0–P3、必填欄非空 | `assemble`(`compliance_issues` / `tcs_noncompliant`)|
| 寫作規則稽核 | 禁用動詞(§8.3.1)、模糊用語(§8.4.1)、Final Step(§8.3.5)、欄位契約 | `--review` §8.x |

> 規則單一真實來源 = `load_rules()`(`docs/runtime/ASPICE_SWE6_AI_Instruction.md` + `判斷規則.md` + `TEST_CASE_PRIORITY.md`)。改文件 → 生成與稽核兩端自動跟進。
> 迴圈:**生成 → 兩層合規 → 修 → 再稽核**,直到 §8.x = 0、確定性閘 = ✓。
