# TC Generator — 使用指令手冊

> 本批改造後的實際可用指令。範例以 Player 專案為例,換成你的檔案路徑即可。
> 所有指令在 repo 根目錄執行。

---

## 0. 環境準備(一次性)

1. 安裝依賴:

   ```bash
   pip install -e ".[dev]"
   ```

2. 設定 API key(放 `.env`,不要進 git):

   ```bash
   echo 'OPENAI_API_KEY=sk-...' >> .env
   ```

3. (選用)切換 LLM 後端為 Claude:

   ```bash
   export TC_LLM_BACKEND=anthropic
   echo 'ANTHROPIC_API_KEY=sk-ant-...' >> .env
   ```

> 提醒:`--dry-run`、`--scorecard`、`--preflight`、`--calibrate`、內文 traceability **完全不呼叫 LLM、零花費**;只有 `--review`(非 dry-run)與生成會計費。

---

## 1. 審核既有 TC(主力功能)

### 1a. 零成本結構審核(regex,先看基本問題)

```bash
python backend/main.py --review \
  --input "你的_SWQT_xxx.xlsx" \
  --output-dir output/review \
  --dry-run
```

產出:`output/review/findings.json`、`findings_report.md`、`scorecard.{json,md}`。

### 1b. 完整語意審核 + domain 接地 + 內文錨點(推薦)

```bash
python backend/main.py --review \
  --input "你的_SWQT_xxx.xlsx" \
  --output-dir output/review_full \
  --model gpt-4.1 \
  --domain-pack M1/domain_pack_player.json \
  --swe1-reqs M1/swe1_pla_reqs.json
```

- `--domain-pack`:用 domain 真相接地,擋幻覺、減誤報。
- `--swe1-reqs`:traceability 改用**內文比對**(不靠可能被改過的 req_id)。
- `--model`:`gpt-4.1`(快)/ `gpt-5`(深);157 條約 2–3 分鐘、< $1。

---

## 2. KPI Scorecard(對既有 findings 重算,零成本)

```bash
python backend/main.py --scorecard \
  --findings output/review_full/findings.json \
  --output-dir output/review_full
```

KPI:first_pass_rate、requirement_coverage、traceability_completeness、
design_method_accuracy、avg_decompose_depth、field_completeness、
reality_gap_rate、tier1_critical_req_rate、req_id_mismatch_rate。
(門檻可調 `config/kpi_thresholds.json`)

---

## 3. 內文 traceability(找「換 ID」與「沒覆蓋的需求」,零成本)

```bash
python backend/main.py --trace \
  --input "你的_SWQT_xxx.xlsx" \
  --swe1-reqs M1/swe1_pla_reqs.json \
  --output-dir output/trace
```

產出 `output/trace/traceability.{json,md}`:總覽、**ID 與內文不符的 TC 清單**(換 ID 嫌疑)、內文對不到需求的 TC。

> `M1/swe1_pla_reqs.json` 是從 SWE1 分析報告解析出的需求清單(id/title/desc)。
> 換專案時需重新解析該專案的 SWE1 Analysis Report。

---

## 4. 生成 TC(原功能)

```bash
# 試跑(只估成本,不呼叫 API)
python backend/main.py --input "你的_SWQT_xxx.xlsx" --dry-run

# 實際生成
python backend/main.py \
  --input "你的_SWQT_xxx.xlsx" \
  --sys1 path/to/SYS1.xlsx \
  --spec path/to/spec.docx \
  --output-dir output \
  --model gpt-5 --batch-size 5 --budget 5.0
```

---

## 5. 用量預估 / 校準(Stage 2.5,零成本)

```bash
# 開跑前:先在 Claude Code 跑 /usage 看剩餘 %,再評估這批塞不塞得下
python backend/main.py --preflight --remaining-pct 0.65 --n-light 30 --n-deep 8

# 第一次真實 run 後校準每需求耗用(寫入 config/budget.json)
python backend/main.py --calibrate --start-pct 1.0 --end-pct 0.88 --n-probe 10 --regime deep
```

---

## 6. 一個專案的建議流程

1. 解析該專案 SWE1 Analysis Report → `swe1_pla_reqs.json`(需求母體)。
2. 讀 SWE1 + SPEC + SYS1 → 整理 `domain_pack_<project>.json` → **人工 Gate ① 審核簽核**。
3. 零成本內文 traceability(§3)→ 修掉換 ID / 補沒覆蓋的需求。
4. 完整語意審核(§1b)→ 看 `scorecard.md` 的疑慮 → **人工只審被標記的**。
5. KPI 未達門檻 → 退回修正 → 重審。

---

## 測試

```bash
pytest -q          # 全套(目前 582 passed)
```
