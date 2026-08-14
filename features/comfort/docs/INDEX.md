# Comfort — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-14（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-14 | Phase 0 intake（開案） | [handoff/01_phase0_intake.md](handoff/01_phase0_intake.md) | [upstream/01_phase0_intake.md](upstream/01_phase0_intake.md) | R-C1 ~ R-C5 | A-CF01 ~ A-CF07 | PASS |
| — | 2026-08-14 | R-C6・R-C7 裁決補遺 | [handoff/02_rulings_addendum.md](handoff/02_rulings_addendum.md) | （併入上繳 01） | R-C6、R-C7 | — | PASS |

**編號說明**：下放包 02 為 01 之補遺（補其 open PENDING P-C1／P-C2），
兩者於同一次往返內處理，故上繳只有一份，02 不另編往返序。

---

## 2. 現況

| 項目 | 值 |
|---|---|
| Phase | 1 完成，Phase 2 可進場 |
| workbook_state | `BLANK` |
| spec_mode | `A`（SYS1 export） |
| baseline | SR24 CR24879（R-C1；SR25 out of scope） |
| leaves | 403 |
| open PENDING | **無** |
| open anomaly | A-CF02、A-CF04、A-CF06、A-CF07（皆不阻塞 Phase 2） |

---

## 3. 權威在哪裡

| 檔案 | 內容 |
|---|---|
| `RULINGS.md` | R-C1 ~ R-C7 逐字，加執行層落實回報 |
| `DECISIONS.md` | Phase 1 決策表（recon 預填，**待 Pei 簽署**） |
| `RECON.md` | Phase 1 survey + assertion 實測值 |
| `ANOMALIES.md` | A-CF01 ~ A-CF07 |
| `DATA_REQUESTS.md` | #1 ~ #4 + standing rule |
| `feature.yaml` | pipeline 常數與裁決常數（`recon_assertions`） |
| `data/spec_id_to_outline.tsv` | 403 leaf → SR24 outline 之查表（追蹤入版控） |
| `RUNBOOK.md` | feature 事實之權威 |
| `PLAYBOOK.md` | 狀態板 |

`docs/handoff/` 為分析層下放包，`docs/upstream/` 為執行層上繳包，
兩側皆不改對方之檔。
