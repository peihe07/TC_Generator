# M1 — 里程碑工作區（M0 / M1 / M2）

這裡不是產品程式碼，是 M0–M2 那段 pipeline 改造的**工作區**：設計文件、
實驗資料、以及兩支覆蓋率分析腳本。進度總表在 `PROGRESS.md`，
架構結論已折進 `../docs/dev/PIPELINE_DESIGN.md`。

## 內容

| 檔案 / 目錄 | 是什麼 |
|---|---|
| `PROGRESS.md` | 每個 session 的進度日誌（root README 的里程碑表以此為來源） |
| `EXECUTION_SPEC.md` / `PIPELINE_DESIGN.md` | 當時的執行規格與 pipeline 設計（`docs/dev/PIPELINE_DESIGN.md` 是後續版本） |
| `RECON_NOTES.md` | 資料可得性偵察筆記（`backend/scorecard.py` 的 docstring 引用） |
| `USAGE.md` | 當時的 CLI 使用說明 |
| `domain_pack_dealer.json` / `domain_pack_player.json` | Stage 1 domain pack 實測資料 |
| `swe1_deal_reqs.json` / `swe1_pla_reqs.json` | 抽出的 SWE1 需求集 |
| `spec_coverage_*.json` / `*.md` | L2 spec coverage 分析結果 |
| `spec_coverage_analysis.py` / `spec_coverage_verify.py` | 產生上述結果的腳本 |
| `baselines/` | A/B 比較用的基線輸出 |
| `notes/` | M0 / M2 筆記與 review worklist |

## 為什麼沒有搬進 docs/ 或 scripts/

以下路徑被程式碼與文件直接引用，搬動要同步改多處：

- `backend/main.py` — `--spec-coverage` 的說明字串寫著
  `spec_coverage_*.json (from archive/M1/spec_coverage_analysis.py)`
- `backend/scorecard.py` — docstring 指向 `archive/M1/RECON_NOTES.md`
- `docs/dev/PIPELINE_DESIGN.md` — 多段指令範例用
  `archive/M1/domain_pack_<proj>.json`、`archive/M1/swe1_<proj>_reqs.json`、`archive/M1/spec_coverage_<proj>.json`
- `docs/CHANGELOG.md` — 引用 `archive/M1/PROGRESS.md` 與 `archive/M1/domain_pack_player.json`

真要整理，正確順序是：先把 domain pack 收進 `config/domain_packs/`（該目錄已存在），
再一併更新上述四處引用，而不是單純搬檔。
