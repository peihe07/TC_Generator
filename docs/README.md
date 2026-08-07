# TC Generator Docs

目錄分四類：**runtime**（被 prompt 載入，改動等於改行為）、**開發文件**、
**專案產出**（某個 RD 專案的裁決與待辦）、**計畫**（尚未實作的設計）。

## Runtime — `runtime/`

這些檔案會被 backend 載入 prompt，或直接定義 runtime 行為。**它們是可執行的
設定，不是說明文件** —— 這就是它們獨立成一個目錄的原因。搬動或改名要同步改
`backend/rules_loader.py`、`backend/review_prompt_builder.py` 與相關測試。

- `runtime/ASPICE_SWE6_AI_Instruction.md` — 生成指令，`rules_loader.RULE_FILES`
- `runtime/TEST_CASE_DESIGN_METHOD.md` — design method 規則，`rules_loader.RULE_FILES`
- `runtime/TEST_CASE_PRIORITY.md` — P0–P3 rubric，`rules_loader.RULE_FILES`
- `runtime/ASPICE_SWE6_AI_Review.md` — review prompt，`review_prompt_builder._REVIEW_SPEC_PATH`
- `runtime/TEST_SET_POLICY.md` — Test Set 分群 / hint / override / 匯出政策
- `runtime/profiles/` — 專案 profile overlay，`rules_loader.PROFILES_DIR`
  （以 stem 指定，例如 `FW036_R1L_BT_Profile`）；`PROFILE_INTEGRATION.md` 記五個接線點

`tests/test_generator.py` 有一條測試釘住 instruction doc 的實際路徑與章節標題，
所以改名或改章節會以測試失敗的形式浮現，而不是安靜地退回 fallback。

## Rule Doc Maintenance

`runtime/` 底下的規則文件是單一權威來源 —— 不要另外分叉一份「通用版」，
那只會兩邊各自演化。確認一條規則之後：

- 折進權威文件對應的章節，不要開第二個事實來源
- 章節編號保持連續穩定。prompt builder 以編號引用（`§10`、`§11`、`§12`），
  重編既有章節會打斷這些引用與測試。新規則以子章節附加（`§8.6`、`§8.7`）
- 與功能無關的規則可用 `<placeholder>` 寫法跨功能複用；專案名稱、文件編號、
  市場變體一律留成 placeholder
- Meta / 維護慣例（像這一節）留在這裡，不要寫進 runtime 文件 —— 那會浪費
  prompt token 且對生成沒有幫助

## Developer Docs

- `REPO_LAYOUT.md` — 每個頂層目錄的角色、可重建項目、不可搬動清單
- `CHANGELOG.md` — 架構筆記、歷史、目前的測試基線
- `dev/API_CONTRACT.md` — 前後端 API 契約
- `dev/WORKFLOW_MECHANISM_TABLE.md` — 使用者動作 → 前端 → 後端 → AI/state 對照表
- `dev/PIPELINE_DESIGN.md` — 端到端生成 pipeline 設計（draft）
- `dev/TC_Generator_Architecture_Diagrams.html` — 架構視覺參考
- `design-system/DESIGN_SYSTEM.md` — Win95 風格前端設計系統
- `../M1/PROGRESS.md` — M0–M2 里程碑進度（工作區說明見 `../M1/README.md`）
- `../frontend-modern/README.md` — modern UI 變體的設定、ports、Docker 指令

## Project Artifacts — `fw036/`

FW036 / MediaHMI 這個 RD 專案的產出。**不是通用規則**，換專案要另開一個目錄。

- `fw036/framework.md` — Test Group / Test Set / spec section 三層框架
- `fw036/RD1_questions.md` — 待 RD-1 裁決的問題單
- `fw036/pending_passes.md` — 每個裁決落地後的機械式 rework 工單（含檢索指令與驗收）

生成腳本與資料在 `../tcgen_package/`（RUNBOOK、ANOMALIES、batches、generated）。

## Plans — `plans/`

尚未實作的設計。實作後把結論折回對應的 runtime / dev 文件，
別讓計畫變成第二份事實來源。

- `plans/TCGEN_PIPELINE_FEEDBACK.md` — tcgen 跑法 vs app pipeline 的差異評估與回灌分類
- `plans/TCGEN_INTEGRATION_PLAN.md` — W1–W12 實作規劃（4 個 Sprint）
- `plans/INTAKE_ANALYSIS_DESIGN.md` — Stage 0 Intake 分析（生成前的資料準備診斷）

## Archive

- `archive/` — 歷史筆記與已合併的 patch，**不得**載入 runtime prompt

## Local / Ignored Data

- `test/` 與 `temp/` 是本機樣本 / scratch fixtures，已被 git ignore
- `Report/` — 對外簡報（pptx）與比較表
