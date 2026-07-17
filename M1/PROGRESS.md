# TC Generator Pipeline 改造 — 進度總表

> 分支 `feat/m1-stage7-scorecard`（已 push origin，領先 `main` 43 commits）。
> Backend 測試基線 **618 tests collected**。最後更新 2026-06-30。

## 已完成

| 項目 | 內容 | 測試 | commit |
|---|---|---|---|
| **M0** Provider 解耦 | `providers/`(OpenAI+Anthropic+Budget+factory)、`set_provider` seam | | `9d7ac70` |
| **M0b** generator 拔除 openai | `_chat` 全走 provider、`TC_LLM_BACKEND` env | | `c95ac7b` |
| **M1** Stage 7 Scorecard | `scorecard.py` 7+1 KPI、`--scorecard` CLI | | `570d0db` |
| **M2** Budget planner | `budget_planner.py`、`--preflight`/`--calibrate` | | (併入) |
| **KPI** tier1_critical_req_rate | 拆解深度指標 | | `14da502` |
| **Stage 1** Domain Pack | `domain_pack.py` + Player pack(Gate ① 已簽、SWE1 重建) | | `14da502` / `ee0695e` |
| **Stage 3** 深拆接地 | decompose 注入 domain + `build_decompose_meta` | | `0967c3c` |
| **Stage 6** review 強化 | domain 注入 + §7.6 reality-gap + `--domain-pack` | | `4cd6c6d` |
| **§7.6 驗證** | 探針 TC 證實 reality-gap 觸發 | — | `704dfde` |
| **Content traceability** | `req_tracer.py`、`--trace` CLI、req_id_mismatch KPI | | `2a113cf` / `a96dc3d` |
| **L2 spec_coverage KPI** | SPEC behaviours vs SPEC original 覆蓋率 | | `09b73d2` / `3f94639` |
| **Interactive review SOP** | subscription 語意層($0)、`--export-bundle`/`--assemble` | | `8cb2164` |
| **Closed-loop generation** | SPEC-grounded 生成橋接 → team template + house rules → 可再審查 xlsx | | `0a0ccc0` / `4e816c8` / `a7dd35c` |

## 用真實 Player 資料證明的事

1. **拆解誤報 55.6% → 22.2%**(domain pack 接地後,中段樣本 tier1_critical_req_rate)。
2. **糾正 reviewer 幻覺**:把「缺 No Repeat 模式」(spec 沒有)修正為真缺口「缺 Repeat One Track」,並引 spec 出處。
3. **§7.6 reality-gap**:對真矛盾 TC 觸發(reality_gap_rate 100%)、對乾淨 TC 靜默(無誤報)。
4. **Stage 3 深拆示範**:PLA-030 Repeat 覆蓋 ~3 → 11 情境、0 幻覺(`M1/stage3_demo_repeat.md`)。
5. **Closed-loop 生成**:`output/player_gen*/` 三組實驗(all / repeat / shuffle),生成 TC 寫入
   team template 後可再跑 review + scorecard(見各目錄 `audit/` 與 `rereview/`)。

## 產物位置

- 程式:`backend/{scorecard,providers,budget_planner,domain_pack,req_tracer}.py` + `review_engine`/`review_prompt_builder`/`generator`/`main` 改造
- 設定:`config/{kpi_thresholds,budget}.json`
- Player domain pack:`M1/domain_pack_player.json`(Gate ① 簽核)
- Baseline / 驗證:`M1/baseline_player*/`、`M1/stage3_demo_repeat.md`、`M1/spec_coverage_*`
- 生成實驗:`output/player_gen_{all,repeat,shuffle}/`(生成 TC + audit/rereview scorecards)
- 規劃文件:`docs/dev/PIPELINE_DESIGN.md`、`M1/EXECUTION_SPEC.md`、`M1/{M0,M2}_NOTES.md`

## 尚未做(非 blocker,需確認再動)

1. **Stage 3/4 單需求 agent 扇出 orchestration** —— 最大、最險的一塊;目前 decompose 仍是批次。要做無人值守大量生成才需要。
2. **完整 157 TC 的 A/B** —— 建議本機分批跑 `--review --domain-pack` 取得完整數字。
3. **Stage 4 生成填充層接 domain pack**(現只接了 decompose 與 review)。

## 接手提示

- 主路徑互動式:`review_workbook(..., domain_pack_path=...)` 已可用;CLI `python backend/main.py --review --input X.xlsx --domain-pack M1/domain_pack_player.json`。
- 換後端:設 `TC_LLM_BACKEND=anthropic` + `ANTHROPIC_API_KEY`。
- KPI baseline:`python backend/main.py --scorecard --findings <findings.json>`。
- Closed-loop 生成:`--gen-export-bundle`(匯出) → 填答 → `--gen-assemble --gen-template <blank.xlsx>`(寫回 template)。
