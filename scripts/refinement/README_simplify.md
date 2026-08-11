# Projection TC Simplifier (OpenAI GPT-5.4)

把 `Projection_tcw.json` 裡的 642 筆 TC 透過 OpenAI GPT-5.4 全量精簡, 修正:
- 步驟過長 (v2 §4.8 步驟長度三層)
- 一步多動作 (v2 §4.3)
- ER 與 Step 不對等 (v2 §5.3)
- Hedge 詞 (`normally`, `properly`, `successfully` ...)
- PC 含命令動詞 (v2 §2.1)
- Final Step 未含驗證意圖 (v2 §4.2)

直接覆寫到輸出 JSON, 原始欄位保留在 `originalSteps` / `originalExpectedResults` / `originalPreConditions` 供 rollback。

---

## Setup

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=sk-...
```

需要 Python 3.10+, openai SDK >= 2.0。

---

## Usage

### 完整執行 (642 筆)

```bash
python simplify_tcs.py Projection_tcw_fixed.json Projection_tcw_simplified.json
```

預估時間: 642 筆 / 5 並行 ≈ 約 15-25 分鐘。
預估成本: 依 GPT-5.4 計價而定, 不使用 prompt cache (OpenAI 自動命中後段 prompt)。

### 先試跑 5 筆驗證

```bash
python simplify_tcs.py Projection_tcw_fixed.json /tmp/test.json --limit 5
```

跑完打開 `/tmp/test.json` 看修訂結果, 確認 AI 沒亂改邏輯, 再跑全量。

### Dry run (只印 prompt 不打 API)

```bash
python simplify_tcs.py Projection_tcw_fixed.json /tmp/preview.json --dry-run --limit 1
```

---

## 輸出檔案

執行 `python simplify_tcs.py X.json out.json` 後:

| 檔案 | 內容 |
|---|---|
| `out.json` | 全量精簡後的 workspace JSON, 可直接 import 回工具 |
| `out.audit.csv` | 每筆 TC 的決策紀錄 (decision / 引用規則 / 結構變更 / 警示) |
| `out.failed.csv` | API 失敗或 lint 嚴重不通過的 TC (這些保留原版未動) |

每筆被修改的 TC 在 JSON 內會新增以下欄位:
- `aiSimplified: true`
- `aiSimplificationMeta`: 含 rulesApplied / structuralChanges / warnings / lintIssues
- `originalPreConditions` / `originalSteps` / `originalExpectedResults`: 原內容備份

未被修改的 TC (AI 判斷已合規) 不會新增欄位。

---

## 安全機制

### 1. Schema validation
AI 回傳必須是合法 JSON, 含全部 9 個必要欄位。schema 不通過會自動重試 (最多 2 次)。OpenAI 已用 `response_format={"type":"json_object"}` 強制 JSON 輸出。

### 2. 邏輯保留檢查 (AI 自我判斷)
AI 必須在每筆回傳 `preservedLogic: true` 才套用修訂。若 AI 認為修改會改變測試邏輯, 會回 `needsRevision: false` 並在 `warnings` 解釋。

### 3. Lint 檢查
修訂後的 step + ER 自動跑規則 lint:
- Step 數 = ER 數 (§5.3 一對一)
- Step 不可有禁用主動詞 (observe / see if)
- Final step 必含 check / confirm / read / record / compare 之一
- ER 不可有 hedge 詞 (normally / properly / successfully ...)

**嚴重問題** (step 數不對等 / 空值) → 回退原版, 標 `lint_failed`。
**輕微問題** (殘留 hedge) → 套用但記錄到 audit log, 之後人工審。

### 4. 原版保留
所有被改動的 TC 都保留原欄位, 隨時可 rollback。

---

## Rollback

若要還原某筆 TC, 在 JSON 裡找該 TC 把 `originalSteps` 等欄位寫回 `steps` 即可:

```python
import json

with open('Projection_tcw_simplified.json') as f:
    data = json.load(f)

for r in data['workspace']['snapshot']['tcRows']:
    if r.get('aiSimplified'):
        r['preConditions'] = r.pop('originalPreConditions', r['preConditions'])
        r['steps'] = r.pop('originalSteps', r['steps'])
        r['expectedResults'] = r.pop('originalExpectedResults', r['expectedResults'])
        del r['aiSimplified']
        del r['aiSimplificationMeta']

with open('rolled_back.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

---

## 調整參數

腳本頂部的常數可改:

```python
MODEL = "gpt-5.4"                # 模型版本
CONCURRENCY = 5                  # 並行數 (太高會 rate-limit)
MAX_RETRIES = 2                  # schema/lint 失敗重試次數
MAX_TOKENS = 2500                # 每筆回應 token 上限
```

並行數建議:
- 試跑 (--limit ≤ 10): 設 3
- 全量: 5 (預設)
- 若遇 429 rate limit: 降到 3 或 2

### 使用 Azure OpenAI 或自訂 endpoint

若是 Azure OpenAI 或代理 endpoint, 修改 `AsyncOpenAI` 初始化:

```python
# Azure OpenAI
from openai import AsyncAzureOpenAI
client = AsyncAzureOpenAI(
    api_key=api_key,
    api_version="2024-10-21",
    azure_endpoint="https://YOUR-RESOURCE.openai.azure.com/"
)

# 自訂 endpoint
client = AsyncOpenAI(api_key=api_key, base_url="https://your-proxy.com/v1")
```

---

## 推薦執行順序

```bash
# Step 1: dry run 看 prompt
python simplify_tcs.py Projection_tcw_fixed.json /tmp/preview.json --dry-run --limit 1

# Step 2: 試跑 5 筆, 打開 JSON 抽看
python simplify_tcs.py Projection_tcw_fixed.json /tmp/test5.json --limit 5

# Step 3: 試跑 30 筆, 看比例
python simplify_tcs.py Projection_tcw_fixed.json /tmp/test30.json --limit 30

# Step 4: 全量
python simplify_tcs.py Projection_tcw_fixed.json Projection_tcw_simplified.json
```
