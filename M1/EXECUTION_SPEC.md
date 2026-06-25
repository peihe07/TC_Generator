# TC Generator — 執行規格(第 1 批:Phase 0 / Stage 7 / Stage 2.5)

> 本檔是 **執行層**,與 `PIPELINE_DESIGN.md`(設計層)分離,用 Stage 編號互相對照。
> 目的:讓 Claude Code 拿了能**無歧義開工**——每張規格明確列出「動/建哪些檔、介面 signature/schema、完成定義(acceptance)、pytest、相依」。
> 範圍:落地順序第 1 批(低風險純前置)。其餘 stage 等這批驗證過再逐一補。
> 文件狀態:草案 · 2026-06-25

---

## 全域慣例(三張規格共用)

- Python ≥ 3.10;命名 snake_case(類別 PascalCase);型別標註用現代語法(`X | None`、`list[dict]`)。
- 程式碼註解 / docstring 用英文。
- 錯誤處理:讓錯誤自然拋出,不過度包 try-catch;只在「要轉成使用者可讀訊息」的邊界(CLI / API)接住。
- 測試:pytest;新模組各自 `tests/test_<module>.py`;**現有 528 backend tests 必須維持 green(回歸閘)**。
- 輸出檔放 `output/`;設定放 `config/`;檔名英文、無空格。
- 金鑰一律走環境變數;`.gitignore` 需排除 `output/`、`.env`、任何含 key 的檔(`config/budget.json` 不含 key,可進 git)。
- 每張規格獨立可交付;建議順序 **M0 → M1 → M2**(見末段里程碑),但三者相依度低、可並行。

---

# 規格 1 — Phase 0:Provider 解耦

**對應:** PIPELINE_DESIGN § Phase 0
**一句話:** 把 `generator.py::_chat` 抽成 `LLMProvider` interface,讓 OpenAI / Anthropic 後端可插拔、usage 統一、能 A/B 比較深度。

### 設計邊界(先讀,避免做錯方向)

- Provider interface 只負責**程式化後端**(OpenAI API、Anthropic API)——即 **headless** 路徑與 OpenAI→Claude 遷移。
- **「互動式」不是一個 provider。** 互動式跑在 Claude Code 內、由你驅動 subagent,**完全不經過 `_chat`**。不要建 `InteractiveProvider` 去打 API(那會反而計費,違背初衷)。
- 所以本規格的產物服務於:① headless 批量 ② A/B 比較 ③ 把預設後端從 OpenAI 換成 Anthropic。

### 動 / 建檔

| 檔案 | 動作 | 內容 |
|---|---|---|
| `backend/providers/base.py` | 建 | `LLMProvider` ABC + `LLMResponse` / `LLMUsage` dataclass |
| `backend/providers/openai_provider.py` | 建 | 把 `generator.py` 內現有 OpenAI 呼叫 / 回應解析搬進來 |
| `backend/providers/anthropic_provider.py` | 建 | Claude API(`anthropic` SDK);解析 content blocks + usage |
| `backend/providers/__init__.py` | 建 | `make_provider(backend, **cfg)` factory |
| `backend/generator.py` | 改 | `_chat` 改為委派 `self.provider.chat(...)`;成本追蹤讀 `response.usage` |
| `backend/_budget.py` | 改 | 支援 `limit_usd=None`(訂閱 / 不計費);`charge()` 在 `cost_usd is None` 時 no-op |
| `requirements.txt` | 改 | 加 `anthropic>=0.40` |

### 介面契約

```python
# backend/providers/base.py
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class LLMUsage:
    input_tokens: int = 0
    output_tokens: int = 0
    cached_input_tokens: int = 0
    request_count: int = 1
    cost_usd: float | None = None   # None when not API-priced (subscription / interactive)


@dataclass
class LLMResponse:
    text: str
    usage: LLMUsage
    model: str
    stop_reason: str | None = None
    raw: Any = None                 # provider-native payload, for debugging only


class LLMProvider(ABC):
    name: str

    @abstractmethod
    def chat(
        self,
        messages: list[dict],
        model: str,
        *,
        max_tokens: int = 4096,
        temperature: float = 0.0,
        cache_prefix: str | None = None,   # stable prefix to mark for prompt caching
        timeout: float = 180.0,
        **kwargs: Any,
    ) -> LLMResponse:
        ...
```

```python
# backend/providers/__init__.py
def make_provider(backend: str, **cfg) -> LLMProvider:
    """backend: 'openai' | 'anthropic'. Raises ValueError on unknown backend."""
```

```python
# backend/_budget.py
class Budget:
    def __init__(self, limit_usd: float | None):   # None => unlimited (subscription)
        ...

    def charge(self, usage: LLMUsage) -> None:      # no-op when usage.cost_usd is None
        ...

    def remaining(self) -> float | None:            # None when unlimited
        ...
```

- `AnthropicProvider.chat` 必須**只取 `type == "text"` 的 block** 串成 `text`,並把 `usage.input_tokens / output_tokens / cache_read_input_tokens` 映到 `LLMUsage`;`cost_usd` 由 model 單價算(API 模式)或留 `None`。
- `cache_prefix` 對 OpenAI 對映 ≥1024 token prefix 快取;對 Anthropic 對映 `cache_control`。介面層只傳遞,實作各自處理。
- **環境變數 gotcha:** `ANTHROPIC_API_KEY` 存在時 Claude Code 會走 API 計費。`AnthropicProvider` 預期它存在(headless 才用);啟動時 log 一行提示目前後端與是否計費。

### 完成定義(acceptance)

- [ ] `generator.py` 不再直接 import openai;所有 LLM 呼叫經 `self.provider.chat`。
- [ ] `make_provider('openai')` 與 `make_provider('anthropic')` 都回傳可用 provider;未知字串拋 `ValueError`。
- [ ] OpenAI 路徑行為與改造前一致(回歸:**528 tests 全 green**)。
- [ ] `LLMResponse.usage` 對兩種後端都正確填值;訂閱情境 `cost_usd is None` 且 `Budget.charge` 不爆。
- [ ] 切換預設後端只需改一個設定點(env 或 config),不需動 `generator.py`。

### pytest(`tests/test_providers.py`)

| 測試 | 驗什麼 |
|---|---|
| `test_make_provider_known` | openai / anthropic 各回對應型別 |
| `test_make_provider_unknown_raises` | 未知 backend 拋 ValueError |
| `test_openai_provider_normalizes_response` | mock SDK → 回正規化 `LLMResponse` |
| `test_anthropic_provider_parses_text_blocks` | mock 多 block 回應 → 只串 text、usage 正確 |
| `test_usage_cost_none_in_subscription` | 無單價時 cost_usd is None、budget no-op |
| `test_generator_delegates_to_provider` | `_chat` 確實呼叫 provider(用 fake provider) |

> 所有測試 **mock SDK,不打真實 API**。

### 相依

- 阻擋:Stage 3/4/6 的 headless 變體、A/B 比較。
- 被阻擋:無(可最先做)。

---

# 規格 2 — Stage 7:KPI Scorecard

**對應:** PIPELINE_DESIGN § Stage 7
**一句話:** 把 Stage 5 結構錯誤 + Stage 6 findings 聚合成 7 項 KPI,輸出 `scorecard.json` + `scorecard.md`,驅動 Feedback Loop。純 Python、零 AI。

> **最快見效:** 本規格讀**現有** `findings.json` 即可算,不需 provider、不需新生成——能立刻對現行系統拿到 **baseline KPI**,也是驗證「深度改造值不值得」的對照點。

### 動 / 建檔

| 檔案 | 動作 | 內容 |
|---|---|---|
| `backend/scorecard.py` | 建 | `compute_scorecard()` + `write_scorecard()` |
| `backend/main.py` | 改 | `--review` 流程末端自動寫 scorecard;另加獨立 `--scorecard --findings <path>` |
| `config/kpi_thresholds.json` | 建 | KPI 門檻(可調) |

### KPI 計算規則(分子 / 分母,寫死、可被測)

| KPI | 分子 | 分母 | gate 門檻(預設) |
|---|---|---|---|
| 一次通過率 | 無 Critical/Major finding 的 TC 數 | 總 TC 數 | **0.80** |
| 需求覆蓋率 | 有產 ≥1 TC 的需求數 | 總需求數 | 1.00 |
| Traceability 完整度 | 有對到 spec 的 TC 數 | 總 TC 數 | 0.95 |
| Design method 正確率 | method 符合規則的 TC 數 | 總 TC 數 | 不 gate(僅報) |
| 平均拆解深度 | Σ 每需求拆解步數 | 總需求數 | 不 gate(僅報) |
| 欄位完整率 | 通過 Stage 5 的 TC 數 | 總 TC 數 | 0.98 |
| Reality-gap 率 | 被 Stage 6 標 reality-gap 的 TC 數 | 總 TC 數 | 不 gate(越低越好,僅報) |

### 介面契約

```python
# backend/scorecard.py
from dataclasses import dataclass


@dataclass
class KPI:
    name: str
    numerator: int
    denominator: int
    value: float | None      # None when denominator == 0
    threshold: float | None  # None when not gated
    passed: bool | None      # value >= threshold, or None when not gated / no value


@dataclass
class Scorecard:
    kpis: dict[str, KPI]
    total_tcs: int
    total_requirements: int
    gate_passed: bool        # True only if every gated KPI passed


def compute_scorecard(
    findings: dict,                    # §9 findings.json (parsed)
    validation: dict,                  # Stage 5 per-TC structural result
    traceability: dict,                # per-TC spec-match status
    decompose_meta: dict | None = None,  # per-req step counts (Stage 3); optional
    thresholds: dict | None = None,    # overrides config/kpi_thresholds.json
) -> Scorecard:
    ...


def write_scorecard(sc: Scorecard, out_dir: str) -> None:
    """Write scorecard.json and scorecard.md into out_dir."""
```

- `decompose_meta is None` → 「平均拆解深度」的 `value = None`、`passed = None`,不讓整體 gate 爆(Stage 3 尚未提供步數時的優雅退化)。
- `denominator == 0`(空輸入)→ `value = None`,不可除零。
- `scorecard.json` 為穩定 schema(欄位順序固定),供之後 dashboard / 趨勢比較。

### 完成定義(acceptance)

- [ ] 餵合成 findings + validation,7 項 KPI 數值正確。
- [ ] `gate_passed` 僅在所有「有門檻」KPI 通過時為 True。
- [ ] 空輸入 / 缺 decompose_meta 不崩、回 None 而非 0 或例外。
- [ ] `--review` 跑完同時產出 `findings_report.md`(原有)+ `scorecard.{json,md}`(新)。
- [ ] 獨立 `--scorecard --findings findings.json` 能對既有輸出重算(baseline 用)。

### pytest(`tests/test_scorecard.py`)

| 測試 | 驗什麼 |
|---|---|
| `test_first_pass_rate` | Critical/Major 計入、Minor/Info 不計 |
| `test_requirement_coverage` | 無 TC 的需求拉低覆蓋率 |
| `test_traceability_ratio` | 對到 spec / 未對到 的比例 |
| `test_missing_decompose_meta_degrades` | 深度 KPI = None、不影響 gate |
| `test_zero_division_guard` | 空輸入回 None |
| `test_gate_passed_logic` | 任一 gated KPI 未過 → gate_passed False |
| `test_scorecard_json_schema_stable` | 輸出 JSON 欄位 / 型別固定 |

### 相依

- 阻擋:Feedback Loop 的門檻判斷、之後的 KPI dashboard。
- 被阻擋:「平均拆解深度」需 Stage 3 提供 `decompose_meta`(可後補,先優雅退化)。

---

# 規格 3 — Stage 2.5:Pre-flight Budget Checkpoint

**對應:** PIPELINE_DESIGN § Stage 2.5
**一句話:** 開跑前用 `fit_batch` 估這批塞不塞得進當前五小時窗(人工讀 `/usage` 餵剩餘 %),不足就縮批 / 等重置;搭配 incremental 續跑讓截斷無痛。

> **單位約定(消除歧義):** 所有 `*_pct` 一律用 **0.0–1.0 的小數**。`remaining_pct=0.65` 表示還剩 65%;`per_req_pct=0.012` 表示每需求約吃 1.2% 的窗。`safety=0.7` 表示保留 30% headroom。

### 動 / 建檔

| 檔案 | 動作 | 內容 |
|---|---|---|
| `backend/budget_planner.py` | 建 | `fit_batch` / `fit_mixed` / 校準 / budget.json IO |
| `config/budget.json` | 建 | 雙峰 `per_req_pct` + safety(初始 null,待校準) |
| `backend/main.py` | 改 | 加 `--preflight` 與 `--calibrate` 兩個子流程(人工輸入剩餘 %) |

### 介面契約

```python
# backend/budget_planner.py
from dataclasses import dataclass


@dataclass
class BudgetConfig:
    per_req_pct_light: float | None = None   # calibrated; fraction 0..1
    per_req_pct_deep: float | None = None
    safety: float = 0.7
    calibrated_at: str | None = None         # ISO timestamp


def load_budget(path: str = "config/budget.json") -> BudgetConfig: ...
def save_budget(cfg: BudgetConfig, path: str = "config/budget.json") -> None: ...


def fit_batch(remaining_pct: float, per_req_pct: float, safety: float = 0.7) -> int:
    """How many requirements safely fit the current 5h window, with margin."""
    usable = max(0.0, remaining_pct - (1 - safety))  # leave headroom
    return int(usable // per_req_pct)


def fit_mixed(remaining_pct: float, n_light: int, n_deep: int, cfg: BudgetConfig) -> dict:
    """Mixed batch: weight light/deep by their calibrated per_req_pct.
    Returns {'fits': bool, 'projected_pct': float, 'decision': 'go'|'shrink'|'wait',
             'max_light': int, 'max_deep': int}.
    """


def record_calibration(
    start_pct: float, end_pct: float, n_probe: int, regime: str,
    path: str = "config/budget.json",
) -> BudgetConfig:
    """regime: 'light' | 'deep'. per_req_pct = (start_pct - end_pct) / n_probe.
    Updates the matching field and calibrated_at, then saves.
    """
```

- `fit_mixed` 的 `projected_pct = n_light*per_req_pct_light + n_deep*per_req_pct_deep`;`fits = projected_pct <= remaining_pct - (1 - safety)`。
- 任一所需 `per_req_pct` 為 `None`(未校準)→ 不估,回 `decision='wait'` 並在 CLI 提示「先跑 `--calibrate`」,**不崩**。

### CLI 行為

```bash
# 開跑前評估(人工先在 Claude Code 跑 /usage 看剩餘 %)
python backend/main.py --preflight --remaining-pct 0.65 --n-light 30 --n-deep 8

# 第一次真實 run 後校準(屬執行期,非現在)
python backend/main.py --calibrate --start-pct 1.0 --end-pct 0.88 --n-probe 10 --regime deep
```

`--preflight` 輸出:projected %、go/shrink/wait、若 shrink 則建議的 `--n-light/--n-deep` 上限。

### Resumability(沿用現有機制,本規格只加回歸測試鎖住)

- Stage 4 每需求完成即 persist 到 `job_store`(現有);截斷 = 暫停。
- 下個窗口 `--mode incremental` 從第 K+1 個需求續跑,跳過已 persist 的 row。

### 完成定義(acceptance)

- [ ] `fit_batch` 數學正確(邊界:剩餘 ≤ 1−safety 時回 0;整除邊界正確)。
- [ ] `fit_mixed` 依雙峰加權;未校準回 `wait` 且 CLI 給清楚提示。
- [ ] `record_calibration` 寫入 / 讀回 `budget.json` round-trip 正確。
- [ ] `--preflight` / `--calibrate` 不需任何 API 呼叫、零額度消耗。
- [ ] incremental 續跑:已 persist 的 row 不重生成。

### pytest(`tests/test_budget_planner.py`)

| 測試 | 驗什麼 |
|---|---|
| `test_fit_batch_basic` | 一般情形回正確需求數 |
| `test_fit_batch_below_margin_zero` | 剩餘低於 headroom → 0 |
| `test_fit_mixed_weighted` | light/deep 加權估算 |
| `test_fit_mixed_uncalibrated_waits` | per_req_pct=None → wait + 不崩 |
| `test_record_calibration_roundtrip` | 校準寫讀一致、算式正確 |
| `test_incremental_skips_done_rows` | 回歸:incremental 只生成未完成 row(mock generator) |

### 相依

- 阻擋:大量產出的安全分批。
- 被阻擋:`per_req_pct` 雙峰值需**第一次真實 probe run** 才有(規劃期留 null);混批精度需 Stage 3 的 light/deep 分類器(待辦,先用單一 regime / 手動 `--n-light/--n-deep`)。

---

## 里程碑與建議順序

| 里程碑 | 內容 | 為何這個順序 |
|---|---|---|
| **M1** | 規格 2 Scorecard(對現有 findings.json) | 最快見效:不需 provider，立刻拿到 baseline KPI |
| **M0** | 規格 1 Provider 解耦 + 528 tests 回歸 | 解鎖 headless / A/B / OpenAI→Claude;風險最低的底層 |
| **M2** | 規格 3 budget_planner + preflight CLI + incremental 回歸 | 純 Python，校準延到第一次真實 run |

> M1 與 M0 幾乎可並行(scorecard 不依賴 provider)。三者全綠後,才進第 2 批規格(Stage 1 Domain Pack、Stage 3 分流改造、Stage 6 強化)。
> **本批不含任何需要實際 LLM run 的步驟**——校準與 baseline 量測都讀現有產物或人工輸入,符合「先規劃、不額外花錢」。

---

## 待回填(規劃期留空,執行期補)

- `per_req_pct_light` / `per_req_pct_deep`:第一次真實 probe run 後由 `--calibrate` 寫入。
- `kpi_thresholds.json` 的非一次通過率門檻:拿到 baseline 後依現況調。
- Stage 3 light/deep 分類器規格:列入第 2 批。
