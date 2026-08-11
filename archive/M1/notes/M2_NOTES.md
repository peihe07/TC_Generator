# M2 — Stage 2.5 Pre-flight Budget Checkpoint:執行筆記

> 對應 `EXECUTION_SPEC.md` 規格 3。日期 2026-06-25。分支 `feat/m1-stage7-scorecard`。純 Python、零 API。

## 建檔 / 改檔

| 檔案 | 動作 | 內容 |
|---|---|---|
| `backend/budget_planner.py` | 建 | `BudgetConfig` + `load/save_budget` + `fit_batch` / `fit_mixed` / `record_calibration` |
| `config/budget.json` | 建 | 雙峰 `per_req_pct`(初始 null)+ `safety=0.7` |
| `backend/main.py` | 改 | 加 `--preflight` 與 `--calibrate` 兩子流程(人工輸入剩餘 %),零 API |
| `pyproject.toml` | 改 | py-modules 加 `budget_planner` |
| `tests/test_budget_planner.py` | 建 | 6 測試 |

## 介面(照 spec,單位一律 0..1 小數)

- `fit_batch(remaining_pct, per_req_pct, safety=0.7)`:`usable = max(0, remaining - (1-safety))`;`int(usable // per_req_pct)`。per_req 為 0/None 不除零回 0。
- `fit_mixed(remaining_pct, n_light, n_deep, cfg)`:`projected = n_light*light + n_deep*deep`;`fits = projected <= remaining-(1-safety)`;回 `{fits, projected_pct, decision: go|shrink|wait, max_light, max_deep}`。未校準 → `wait`、不崩。
- `record_calibration(start_pct, end_pct, n_probe, regime)`:`per_req = (start-end)/n_probe`,寫回對應峰 + `calibrated_at`。

## CLI

```bash
# 開跑前評估(先在 Claude Code 跑 /usage 看剩餘 %)
python backend/main.py --preflight --remaining-pct 0.65 --n-light 30 --n-deep 8
# 第一次真實 run 後校準(執行期)
python backend/main.py --calibrate --start-pct 1.0 --end-pct 0.88 --n-probe 10 --regime deep
```

## Acceptance

- [x] `fit_batch` 數學正確(邊界:剩餘 ≤ 1−safety 回 0;整除/浮點 floor 正確)。
- [x] `fit_mixed` 雙峰加權;未校準回 `wait` + CLI 清楚提示。
- [x] `record_calibration` 寫讀 round-trip 正確;非法 regime / n_probe≤0 拋 `ValueError`。
- [x] `--preflight` / `--calibrate` 零 API、零額度。
- [x] incremental 續跑回歸:`_filter_rows(..., "incremental")` 只回未完成(無 tc_id)的 row。

## 注意

- `config/budget.json` 的雙峰值**規劃期留 null**,需第一次真實 probe run 後 `--calibrate` 才有(屬執行期)。
- 浮點 floor:`fit_batch` 用 `//` 對 float,邊界值可能少 1(spec 公式即如此),測試已鎖住實際輸出。

## 驗收

全套 **561 tests green**(M1 8 + M0 提供者 10 + M2 6 + 既有)。
