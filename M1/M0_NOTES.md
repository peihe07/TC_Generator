# M0 — Phase 0 Provider 解耦:執行筆記

> 對應 `EXECUTION_SPEC.md` 規格 1。日期 2026-06-25。分支 `feat/m1-stage7-scorecard`。

## 實作策略(與 spec 的偏差,先讀)

勘查後發現 spec 兩處與實際碼不符,且風險被低估:

1. **`backend/_budget.py` 的 `Budget` class 不存在。** 實際 `backend/tools/_budget.py` 是另一個 `needs_confirmation` 小工具。→ 新的 `Budget` 改放 `backend/providers/budget.py`,**不動** legacy 檔。
2. **`_chat` 與既有測試緊耦合 OpenAI 回應形狀**(`.choices`、`_usage_tokens`),25+ 測試直接 build OpenAI-shaped mock。直接把 `_chat` 改成回 `LLMResponse` 會一次打爆它們。

因此採**加法式、不破壞**路線:新增 `providers/` 抽象層 + 在 `generator` 加**可選委派 seam**(預設走原 OpenAI 路徑→既有測試全綠;`set_provider()` 後才委派)。

## 建檔 / 改檔

| 檔案 | 動作 | 內容 |
|---|---|---|
| `backend/providers/base.py` | 建 | `LLMProvider` ABC + `LLMResponse` / `LLMUsage` |
| `backend/providers/openai_provider.py` | 建 | OpenAI 後端(client 建立 / retry / 正規化 / 計價走 `generator.calculate_cost`) |
| `backend/providers/anthropic_provider.py` | 建 | Claude 後端(只取 `type=="text"` block;usage 映射;`ANTHROPIC_PRICING`;`cache_control`) |
| `backend/providers/budget.py` | 建 | `Budget(limit_usd=None)`,`charge` 在 `cost_usd is None` 時 no-op |
| `backend/providers/__init__.py` | 建 | `make_provider('openai'|'anthropic')` factory,未知拋 `ValueError` |
| `backend/generator.py` | 改(加法) | `set_provider` / `get_provider` / `_ACTIVE_PROVIDER` + `LLMResponse→OpenAI-shape` adapter;`_chat` 開頭委派 |
| `pyproject.toml` | 改 | deps 加 `anthropic>=0.40`;packaging 加 `providers` 套件與 `scorecard` |
| `tests/test_providers.py` | 建 | 6 個 mock 測試 |

## Acceptance 狀態

- [x] `make_provider('openai')` / `('anthropic')` 回對應型別;未知拋 `ValueError`。
- [x] `LLMResponse.usage` 兩後端正確;訂閱情境 `cost_usd is None` 且 `Budget.charge` no-op。
- [x] OpenAI 路徑行為一致 —— **全套 556 tests green**(原 550 + 6)。
- [x] `_chat` 在 `set_provider` 後確實委派(`test_generator_delegates_to_provider`)。
- [x] 「切換預設後端只需一個設定點」:`TC_LLM_BACKEND` env(預設 `openai`)決定預設 provider;另可 `set_provider()` 覆寫。
- [x] **「`generator.py` 不再 import openai」已達成**(見下方 M0b)。

## M0b — 已收尾(2026-06-25)

把 OpenAI 完全從 `generator` 拔除,全程走 provider:

1. 呼叫點 `response.choices[0].message.content` → `response.text`(generator 9 處 + `review_engine` + `review_assistant`)。
2. `_usage_tokens` 改吃 `LLMUsage`;`_chat` 回 `LLMResponse`、錯誤統一包成 `GenerationError`。
3. 移除 `generator._client`、內嵌 retry、`import openai` / `import_module` / `TYPE_CHECKING`;client/timeout/retry 全移到 `OpenAIProvider`。
4. 啟動點:`_default_provider()` 讀 `TC_LLM_BACKEND`。
5. 既有測試 mock 形狀改 `LLMResponse`(`test_generator` / `test_review_engine` / `test_review_assistant`);`_client` 與 retry 測試移到 `test_providers`(新增 4 個)。

**驗收:全套 555 tests green;`grep openai backend/generator.py` = 0。** acceptance 全數打勾。
