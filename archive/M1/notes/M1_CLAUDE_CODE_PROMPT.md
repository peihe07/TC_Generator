# Claude Code 任務:M1 — Stage 7 KPI Scorecard

## 背景與範圍

在現有 TC Generator backend 實作 KPI Scorecard。
- 完整規格:`EXECUTION_SPEC.md` →「規格 2 — Stage 7:KPI Scorecard」。
- 架構背景:`PIPELINE_DESIGN.md`(Stage 7、附錄 C 資料模型、附錄 E review 輸出、附錄 I endpoint)。
- 本任務 = 該規格的 **M1**。

### 硬性邊界(務必遵守)

- 只讀**現有**的 `findings.json`。**不要跑新的 review、不要做任何 LLM / API 呼叫。** M1 是純 Python、零花費。
- **不得破壞現有測試**(528 backend tests 必須維持 green)。
- 慣例:Python ≥ 3.10、snake_case、英文註解 / docstring、錯誤自然拋出(只在 CLI 邊界轉成可讀訊息)、輸出進 `output/`、設定進 `config/`。

---

## 第一步:先勘查,不要急著寫

動工前先讀真實資料形狀,別照規格憑空假設:

1. 找出並讀一份現有 `findings.json`(看 `output/` 或 job 輸出),記下**實際** schema。
2. 讀 `review_engine.py` 的 §9 輸出 schema、`validator.py` 的結構檢查結果形狀、`spec_matcher` 的對應結果形狀。
3. 對照規格 2 的 7 項 KPI,**逐項確認來源資料是否真的存在於現有產物**:
   - first_pass_rate、field_completeness → 多半在 findings / validation,應算得出。
   - requirement_coverage、traceability_completeness → 確認 findings.json 是否帶得到「需求清單」與「per-TC spec 對應狀態」。
   - design_method_accuracy → 確認有無 method 正確性訊號。
   - avg_decompose_depth → **預期算不出**(需 Stage 3 的 decompose_meta,尚未存在)→ 退化 None。
   - reality_gap_rate → 確認 Stage 6 是否已有 reality-gap 標記;沒有就退化 None。
4. **若某 KPI 的來源資料不存在,不要捏造**——該 KPI `value=None` 並在報告標明「無法計算 / 缺來源」。

→ **這步結束請停下來,把「勘查結果 + 哪些 KPI 算得出 / 算不出 + 你打算怎麼對映」回報我,等我確認後再進實作。**

---

## 第二步:實作(我確認後才做)

### 建 / 改檔

| 檔案 | 動作 | 內容 |
|---|---|---|
| `backend/scorecard.py` | 建 | `compute_scorecard()`、`write_scorecard()`、`KPI` / `Scorecard` dataclass |
| `config/kpi_thresholds.json` | 建 | 門檻(見下) |
| `backend/main.py` | 改 | `--review` 末端自動寫 scorecard;另加獨立 `--scorecard --findings <path>` |

### 介面契約(照規格 2,勿自行更名)

```python
@dataclass
class KPI:
    name: str
    numerator: int
    denominator: int
    value: float | None      # None when denominator == 0 or source missing
    threshold: float | None  # None when not gated
    passed: bool | None      # value >= threshold, else None

@dataclass
class Scorecard:
    kpis: dict[str, KPI]
    total_tcs: int
    total_requirements: int
    gate_passed: bool        # True only if every gated KPI passed

def compute_scorecard(findings, validation, traceability,
                      decompose_meta=None, thresholds=None) -> Scorecard: ...
def write_scorecard(sc, out_dir: str) -> None: ...   # writes scorecard.json + scorecard.md
```

### KPI 規則

分子 / 分母照規格 2 的表格。`denominator == 0` 或來源缺 → `value=None`,**不可除零、不 gate**。

`config/kpi_thresholds.json`(只有這幾項 gate,其餘僅報):

```json
{
  "first_pass_rate": 0.80,
  "requirement_coverage": 1.00,
  "traceability_completeness": 0.95,
  "field_completeness": 0.98
}
```

KPI key 命名:`first_pass_rate`、`requirement_coverage`、`traceability_completeness`、`design_method_accuracy`、`avg_decompose_depth`、`field_completeness`、`reality_gap_rate`。

`scorecard.json` 欄位順序固定(供日後趨勢比較);`scorecard.md` 為人類可讀摘要,標出每項數值、分子/分母、是否 gate、pass/fail,以及「無法計算」的項目。

---

## 第三步:測試與驗收

- 寫 `tests/test_scorecard.py`,涵蓋規格 2 列的 7 個測試:
  `test_first_pass_rate`、`test_requirement_coverage`、`test_traceability_ratio`、
  `test_missing_decompose_meta_degrades`、`test_zero_division_guard`、
  `test_gate_passed_logic`、`test_scorecard_json_schema_stable`。
- `pytest` 全綠,且**現有測試不破**。
- acceptance 對齊規格 2 的勾選清單。

---

## 交付

實作完成後,對一份**現有** `findings.json` 跑:

```bash
python backend/main.py --scorecard --findings <現有findings.json路徑> --output-dir output
```

把產出的 `output/scorecard.md`(7 項 baseline KPI 數字,含「無法計算」標註)貼回來。
