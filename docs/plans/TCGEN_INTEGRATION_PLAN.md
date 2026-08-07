# tcgen 機制回灌 backend — 詳細實作規劃

撰寫日期：2026-08-07
上游文件：`docs/plans/TCGEN_PIPELINE_FEEDBACK.md`（評估與分類）
本文件：把 P0-1 ～ P2-3 展開成可執行的實作計畫 —— 模組設計、檔案改動、測試、驗收、順序。

目標分支建議：自 `feat/m1-stage7-scorecard` 切出 `feat/tcgen-backport`，
每個工作項一個 PR，依相依順序合回。

---

## 全景：四個 Sprint 的相依圖

```text
Sprint 1（品質底盤，不動 LLM）
  W1 rules_registry（規則單一來源）─┬─> W2 tc_lint（硬 gate）
                                    └─> （後續所有 prompt / lint 共用）
  W3 writer invariants + 可重現輸出（獨立，可並行）

Sprint 2（第二個專案的能力）
  W4 project profile schema（workbook 形狀參數化）──> W5 context_builder
  W6 uncertainty markers（blocked/assumption/flags_pending 進 schema）
       └─ 依賴 W2（lint 要認得 marker）、W3（writer 要寫 blocked 列）

Sprint 3（掃描件規格與 checkpoint）
  W7 provider 多模態 ──> W8 spec 圖像管線（render + OCR 索引）
  W9 per-parent 生成 + checkpoint/resume（依賴 W5）

Sprint 4（review 回路）
  W10 anchors store（依賴 W5 注入、review UI）
  W11 scorecard 接 gate（依賴 W2）
  W12 pending-passes 產生器（依賴 W6）
```

估時以「一人專注日」計，含測試。總計約 26–34 天，Sprint 1 約 7–9 天。

---

## Sprint 1 — 品質底盤（先讓輸出可稽核，完全不動 LLM）

### W1 — `backend/rules_registry.py`：規則常數單一來源（1.5 天）

**問題。** 同一套規則現在活在四處：`docs/runtime/ASPICE_SWE6_AI_Instruction.md`
（prompt 注入）、`backend/validator.py`（欄位檢查 + dropdown 常數）、
`tcgen_package/scripts/lint_tcs.py`（gate，反向 import validator）、
`backend/prompt_builder.py`（部分規則內嵌在 f-string）。改一條規則要記得改四處。

**設計。** 新增一個純資料模組，只放「機器要 enforce 的常數」，
不放散文規則（散文留在 instruction doc，那是 prompt 的事）：

```python
# backend/rules_registry.py
@dataclass(frozen=True)
class LintRules:
    valid_priorities: tuple[str, ...]
    valid_design_methods: tuple[str, ...]
    forbidden_main_verbs: tuple[str, ...]      # from lint_tcs FORBIDDEN_MAIN_VERBS
    er_modal_verbs: tuple[str, ...]            # shall/will/should/would
    action_verbs_in_pc: tuple[str, ...]        # from validator ACTION_VERBS
    obvious_states: tuple[str, ...]
    vague_terms: tuple[str, ...]
    min_procedure_steps: int = 2
    # each rule id -> instruction doc section, e.g. "er-modal" -> "§6"
    rule_authority: dict[str, str]

DEFAULT_RULES = LintRules(...)   # values moved from validator.py + lint_tcs.py
```

**改動。**
- `validator.py`：`VALID_DESIGN_METHODS` / `VALID_PRIORITIES` / `ACTION_VERBS` 等
  改為 re-export 自 registry（維持既有 import path，不破壞 618 個測試）
- `lint_tcs.py`：改 import registry，移除 `sys.path.insert` hack
- alias 表（`_DESIGN_METHOD_ALIASES`、`_PRIORITY_ALIAS`）留在 validator ——
  normalize 是 validator 的職責，registry 只管「什麼是合法」

**驗收。** `pytest -q` 全綠；`grep -rn "VALID_DESIGN_METHODS = \[" backend/` 只剩 registry 一處。

---

### W2 — `backend/tc_lint.py`：lint 升為 backend 硬 gate（3 天）

**設計。** 把 `tcgen_package/scripts/lint_tcs.py` 搬進 backend 並去專案化。
tcgen 版留在原地當 thin wrapper（FW036 還在用，不能斷）。

```python
# backend/tc_lint.py
@dataclass
class LintConfig:
    expected_test_group: str | None      # was hard-coded "MediaHMI"
    test_set_whitelist: set[str]         # injected from framework, not from file probing
    known_leaf_ids: set[str]             # traceability check; empty = skip
    rules: LintRules = DEFAULT_RULES

def lint_tc(tc: dict, cfg: LintConfig, source: str = "") -> list[Finding]
def lint_records(records: Iterable[dict], cfg: LintConfig) -> LintReport
```

移植清單（全部照搬 tcgen 邏輯，僅參數化）：

| tcgen 規則 | 去專案化方式 |
|---|---|
| `EXPECTED_TEST_GROUP = "MediaHMI"` | `cfg.expected_test_group`，None 則跳過 |
| Test Set whitelist（讀 `section_to_testset.json` + `exemplars.json`） | 呼叫端組好 set 傳入；app 端來源 = framework.json |
| `check_req_ids_against_leaves` | `cfg.known_leaf_ids` |
| trailing-period / label-format / br-tag / forbidden-verb / er-modal / er-baseline / step-er-1to1 | 原樣搬，規則常數來自 registry |
| blocked / assumption / flags_pending 解析 | 搬進來，但 schema 正式化留給 W6 |
| A-026 tier label counter | **不搬**——FW036 專屬，留在 tcgen wrapper 以 plugin hook 掛回（見下） |

Wrapper 端保留專案特例的掛點：

```python
# tcgen_package/scripts/lint_tcs.py (after W2)
from tc_lint import lint_records, LintConfig
report = lint_records(load(...), cfg)
report.extras["tier_labels"] = count_tier_labels_fw036(...)   # project-local
```

**接上 export 流程。**
- `main.py`：`--strict-validation` 語意改為「lint gate 擋不擋 export」；
  另加 `--lint-report <path>` 輸出 JSON
- `tools/write.py` / API export route：寫檔前跑 `lint_records`，
  gate 失敗回傳 findings 清單（HTTP 422），不落檔
- 每條 finding 帶 `rule` + `authority`（§ 節號），UI 可連回 instruction doc

**測試。**
- 新 `tests/test_tc_lint.py`：從 `test_lint_tcs.py` 複製案例改用新 API
- **黃金回歸**：把 `tcgen_package/generated/`（gitignore 外的 275+2 檔）當 fixture，
  斷言新 gate 輸出與 committed `lint_report.json` 逐欄相等
  （total=277, failed=0, blocked=2, assumptions=7）
- `test_lint_tcs.py` 保留，證明 wrapper 行為不變

**驗收。** 黃金回歸過；export 路徑上存在一個會真的擋下違規 TC 的測試
（塞一筆 trailing-period TC，斷言 export 回 422 且無檔案產生）。

---

### W3 — `writer.py` invariants + byte 可重現（2.5–3 天）

**設計。** 不改寫 `write_generated_results` 的插列邏輯（review 流程還依賴它），
而是加一層「受控寫回」模式，把 `write_back.py` 的三個 invariant 一般化：

```python
# backend/writer.py additions
@dataclass
class WriteGuard:
    protected_ranges: list[tuple[int, int]]   # e.g. [(10, 332)] — caller decides
    required_req_ids: set[str] | None          # completeness: every id must land
    allowed_req_ids: set[str] | None           # traceability: no id outside this set
    reproducible: bool = True                  # normalize zip timestamps + docProps

class WriteBackError(RuntimeError): ...        # invariant failed -> NO file produced

def write_with_guard(input_path, rows, output_path, guard: WriteGuard, ...):
    # 1. hash protected ranges of the SOURCE
    # 2. assert traceability + completeness BEFORE any cell write
    # 3. write rows (reuse existing row-writing internals)
    # 4. re-hash protected ranges of the OUTPUT; mismatch -> delete + raise
    # 5. if reproducible: normalize_xlsx(output_path)
    # 6. return {"sha256": ..., "protected_sha256": ...}
```

正規化函式獨立成 `backend/xlsx_repro.py`，**直接照抄** `write_back.py` 的實作
（zip entry timestamp + `docProps` dcterms 正則），連同它註解裡記的兩個坑一起搬：
back-reference 防止 created/modified 標籤錯配、`\g<n>` 防止 octal escape。
這兩個坑是花過學費的，丟掉就會再踩。

**ChangeHistory / framework sheet 同步**也一併抽出（`append_history` / `sync_framework_sheet`），
以 opt-in 參數暴露 —— 這兩個是「受控文件」語意，legacy 路徑不強制。

**測試。**
- 移植 `tests/test_write_back.py` 的跨秒 idempotency 測試（sleep 過秒界，兩次 SHA256 相等）
- protected range 被改動時：檔案不存在 + raise
- completeness / traceability 各一個 negative case
- `write_back.py` 之後改為呼叫 `write_with_guard`（tcgen 端瘦身），
  但**先落 backend、跑過 FW036 黃金比對再切**：對同一組 `generated/` 產出的
  xlsx，SHA256 必須等於 `write_back.py` 現在產出的
  `output/FW036_regen.xlsx`

**驗收。** FW036 黃金比對 SHA256 相等；guard negative cases 全過。

---

## Sprint 2 — 讓 app 有能力跑第二個專案

### W4 — Project profile：workbook 形狀參數化（2 天）

**問題。** tcgen 硬編的東西其實分兩類：ASPICE 規則（W1 已收）與
**這個 workbook 的形狀**——column map（D/G/H/I…AH）、保護區 rows 10-332、
9 個 dropdown 字串、`test_group` 值、B/F 欄公式。第二個專案什麼都會不一樣。

**設計。** `config/profiles/<project>.json` + `backend/project_profile.py`：

```jsonc
{
  "name": "FW036-MediaHMI",
  "test_group": "MediaHMI",
  "workbook": {
    "sheet_prefix": "Test Case Specification",
    "column_map": {"req_id": "D", "test_group": "G", "test_set": "H",
                    "test_item": "I", "pre_conditions": "J", "...": "...",
                    "remarks": "AH"},
    "protected_rows": [[10, 332]],
    "formula_columns": ["B", "F"],
    "vehicle_flag_columns": ["T", "Z"]
  },
  "dropdowns": {"design_method_sheet": "下拉選單"},
  "framework_sheet": "Test Case Framework"
}
```

現有的 `docs/runtime/profiles/` + `rules_loader.py` 的 project-profile overlay
（30aec3b 那條 commit 已經在做 prompt 端的 overlay）沿用同一個檔案，
**一個 profile 同時餵 prompt overlay、LintConfig、WriteGuard、writer column map**。

**驗收。** 用 FW036 profile 驅動 W2+W3，黃金比對不變；
再手寫一個假 profile（不同 column map）跑單元測試證明沒有殘留硬編。

---

### W5 — `backend/context_builder.py`：輸入組裝產品化（3–4 天）

**設計。** 以 requirement parent 為單位的組裝器，行為對齊 `make_batch_context.py`：

```python
@dataclass
class GenerationContext:
    parent_id: str
    test_group: str
    test_set: str
    requirements: list[dict]          # leaves under the parent
    siblings: list[dict]
    spec_sections: dict[str, dict]    # section id -> {text, pages}
    spec_page_images: list[str]
    external_refs: dict[str, dict]    # e.g. PU0998 -> popup definition
    exemplars: list[dict]             # curated anchors first, else done-region

def build_context(parent_id, *, spec_index, framework, profile,
                  ref_resolvers: list[RefResolver], anchors: AnchorStore | None,
                  ) -> GenerationContext
```

四個關鍵行為，各自是一個可測單元：

1. **確定性 section 取用優先**：requirement 帶 outline number（SourceID）時
   直接 dict lookup；沒有才 fallback 到 `spec_matcher` 相似度。
   `_get_spec_context` 改為呼叫這層。
2. **Descendant pull（A-001 修正）**：抓 leaf section 的 parent section +
   所有「不屬於其他 leaf 的 descendant section」。照搬
   `make_batch_context.py` 的集合邏輯（`leaf_sections` 排除規則）。
3. **外部參照展開**：`RefResolver` protocol —— `pattern: re.Pattern` +
   `resolve(ref_id) -> dict`。Pop Up List 是第一個實作
   （pattern `\bPU\d{3,4}\b`），之後 CAN signal 表、HMI string 表照樣掛。
   查無此 id 時回 `NOT FOUND` 標記（tcgen 靠這個抓到 A-009 的 PU0996 缺漏
   ——**查不到本身就是重要輸出**，不能 silent skip）。
4. **Anchor 優先序**：curated anchors > done-region exemplars > profile 指定 fallback。
   Sprint 4 之前 AnchorStore 就是讀一個 json 檔。

**測試。** 用 FW036 資料當 fixture：對 A-001 影響的 10 個 parent
（11.3.1, 14.2, 14.3, 14.3.2, 14.4.3, 16.1, 16.1.4, 16.1.5, 17.1, 23.3），
斷言 `build_context` 產出的 section 集合與 `batches/<parent>.json` 完全一致；
PU 展開對 COM-050（PU 引用密集）逐 id 比對。

**驗收。** 10-parent 黃金比對過；`spec_matcher` fallback 路徑有測試。

---

### W6 — 不確定性 marker 進 schema（2 天）

**設計。** `tools/schemas.py` 加三個型別，契約照抄 lint_tcs 的隱式規則：

```python
class BlockedDecl(TypedDict):
    anomaly: str          # required — no marker without a paper trail
    reason: str           # required
    req_ids: list[str]
    test_set: str         # writer needs it for the blocked row

class AssumptionDecl(TypedDict):
    anomaly: str
    note: str
    req_ids: list[str]    # per-marker scope, NOT per-parent (rework list stays real)

class FlagsPendingDecl(TypedDict):
    anomaly: str
    note: str
```

三處接線：
- **Generator 出口**：`parse_multi_tc_response` 認得 `blocked` / `assumption` 頂層 key，
  malformed（缺 anomaly 或 note）直接 parse error，不是 warning
- **Lint（W2）**：marker 驗證從「隱式 dict 檢查」改為 schema 驗證
- **Writer（W3）**：blocked 宣告寫成真實列 —— Test Item = RD 原句、
  Procedure/ER = `BLOCKED - see Remarks`、P/R 留白、Remarks 欄 = anomaly id + reason。
  **不是跳過**：少一列，稽核就看到一個沒人解釋的缺口
- **Review UI（可後補）**：三類 marker 各自的 badge + anomaly id 顯示

**驗收。** FW036 的 2 blocked + 7 assumption 經新 schema round-trip 後,
write-back 輸出 SHA256 不變。

---

## Sprint 3 — 掃描件規格與 checkpoint

### W7 — Provider 多模態（2 天）

**設計。** `providers/base.py` 的 message content 從 `str` 擴為 block list：

```python
# content: str | list[Block]
# Block = {"type": "text", "text": ...}
#       | {"type": "image", "media_type": "image/png", "data": <base64>}
```

- `anthropic_provider`：直接映射到 Messages API 的 image block
- `openai_provider`：映射到 `image_url` (data URL)
- 純文字呼叫端零改動（`str` 照舊）；`LLMUsage` 不變
- `generator._chat` 加 `images: list[Path] | None` 參數，讀檔轉 base64

**測試。** provider 層用 fake client 斷言 payload 形狀；不打真 API。

### W8 — Spec 圖像管線（2 天）

**設計。** `backend/spec_images.py`，行為對齊 `split_spec.py`：

```python
def render_pdf_pages(pdf: Path, out_dir: Path, dpi: int = 150) -> list[Path]
def build_page_index(pages: list[Path], item_code_res: list[re.Pattern]) -> dict
    # OCR ONLY builds the section->page index; content judgement is the model's job
```

- 依賴 `pymupdf` + `pytesseract`，缺系統 tesseract 時給明確錯誤
- OCR 定位失敗的 section 用 tcgen 驗證過的 fallback：相鄰 item code → 片語比對
- `context_builder`（W5）把 `spec_page_images` 接到 `generator._chat(images=...)`

**驗收。** 對 FW036 的 Media HMI PDF 重建索引，158/158 section 對到頁
（與 `data/page_index.json` 一致）。

### W9 — Per-parent 生成 + checkpoint / resume（2.5 天）

**設計。**
- 生成單位從「N 列一批」改為「一個 parent 一次呼叫」，`--batch-size` 保留給
  無 parent 結構的舊 workbook（fallback）
- 每個 parent 完成即落 `output/<job>/generated/<parent>.json`
  （成為 job 的 durable checkpoint；job_store 記 index 而非內容）
- `--resume <job>`：跳過已有輸出檔的 parent；`--parents <ids>` 單點重跑
- 失敗語意：單一 parent 失敗記錄後繼續，結尾 exit code 非零並列出失敗清單
  （對齊 tcgen「checkpoint/resume、anomaly 落檔不 silent workaround」的紀律）

**驗收。** 模擬中斷（kill 於第 k 個 parent）後 resume，
輸出集合與一次跑完 byte 相等（依 W3 的可重現性）。

---

## Sprint 4 — Review 回路（把這批的審查變成下批的輸入）

### W10 — Anchors store（2 天）

- `backend/anchor_store.py`：`{test_set: [anchor_tc, ...]}` + metadata
  （`approved_by`、`approved_at`、`bound_anomalies: ["A-011", ...]`）
- Review UI 加「設為此 Test Set 的 anchor」；寫入 store
- **失效機制**：anchor 綁 anomaly id；當 pending pass 標記該 anomaly 已裁決且
  裁決翻盤，anchor 標記 `stale`，`context_builder` 注入時跳過 stale 並警告
  （anchors 是「被審過的判斷」，判斷會過期——這是 anchors.json 註解裡已經發生過的事：
  COM-057-02 就因為 A-系列裁決更新過一次）

### W11 — Scorecard 接 gate（1 天）

- `first_pass_rate` 分子改為「經 W2 gate 一次通過、未經人工修改的 TC 數」，
  資料來源 = lint gate 的 report + review 修改紀錄
- 加 `blocked_rate`、`assumption_rate` 兩個 KPI（tcgen 這輪分別是 2/262 與 7 markers
  ——這兩個數字是「spec 品質」的量測，值得長期追蹤）

### W12 — Pending-passes 產生器（1.5 天）

- `backend/pending_passes.py`：從 W6 markers + anomaly tracker 生成
  `pending_passes.md` 形式的工單，每條含：檢索指令（grep marker 的命令）、
  兩個裁決分支的工作量、acceptance check
- 手寫版（`docs/fw036/pending_passes.md`）是格式範本；產生器輸出對 FW036 資料
  應能重建 P-1 ～ P-4 的骨架（P-5/P-6 是人寫的策略段，不強求）

---

## 橫切關注

### 兩種 schema 的 adapter 要顯性化

Generation contract（`tc_title`, `split_flag`, `split_reason`, `reasoning`…）與
workbook-facing shape（`req_id`, `test_item`, 11 欄）目前靠 tcgen 落檔慣例隱式轉換。
W5/W9 落地時新增 `backend/tc_record.py`：

```python
def to_workbook_record(gen_tc: dict, *, req_id: str, test_group: str,
                       test_set: str) -> dict   # the shape W2 lints and W3 writes
```

單一轉換點，兩邊 schema 各自演化時只改這裡。

### 遷移紀律（照 tcgen 的 P-5 教訓）

- 每個 W 一個 PR，**一次只動一個區域**；黃金比對（lint_report、write-back SHA256、
  10-parent context）是每個 PR 的 CI gate
- tcgen_package 在整個 Sprint 1–2 期間保持可獨立運作（wrapper 模式），
  FW036 的 RD-1 裁決落地時隨時要能重跑 write-back
- backend 測試基線 618 collected 只增不減

### 明確不做的事

- 不把 RD-1 問題單、model 分派（Opus/Sonnet per chapter）、pilot 節奏寫進 code
  ——維持 SOP（理由見上游文件 §3）
- 不動 `prompt_builder.py` 的生成規則本文——這輪回灌的是頭尾，不是中段
- 不在 Sprint 1–3 做 frontend 大改；W6 的 review UI badge 是唯一 UI 觸點

---

## 里程碑驗收總表

| Sprint | 出口條件 |
|---|---|
| 1 | backend gate 對 FW036 generated/ 重現 lint_report.json；writer 黃金 SHA256 比對過；export 路徑會真的擋違規 TC |
| 2 | 假 profile 證明零殘留硬編；10-parent context 黃金比對；blocked/assumption round-trip SHA256 不變 |
| 3 | 158/158 page index 重現；中斷-resume byte 相等；一次帶圖生成 e2e（可用 FW036 任一 parent 手動驗） |
| 4 | anchor 設定→下批注入 e2e；scorecard 新 KPI 有數；產生器重建 P-1～P-4 骨架 |
