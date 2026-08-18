# 15 下放包 — 052f67d 之處置（與 14 包同輪下放）

## 裁決條文（Pei 2026-08-18 裁定，逐字）

```text
R-U55 052f67d —— 採案 1（留著），不動歷史
      不執行 reset／rebase／force push。
      log 歸屬不準之狀態予以接受並留檔：
      以 `git log -- features/user_profiles/` 追 03 輪，
      會落在 message 為 `feat(power): round 09 …` 之 052f67d 上；
      該 commit 夾帶 user_profiles 之 8 檔（BASELINE.sha256、
      DECISIONS.md、RECON.md、data/recon_leaf_to_section.tsv、
      docs/INDEX.md、docs/handoff/03_recon_start.md、
      docs/upstream/03_recon.md、feature.yaml），內容完整，
      **非「不該進版控之物進了版控」，是歸屬不準**。
      裁定依據：本輪實測該 commit 已推送、其後已有 5 個提交；
      案 2／3 之收益為一句 message 之歸屬，
      成本為 rebase 5 個提交 ＋ force push 一條已推送分支。
      前例併記：本為第二次（前有 645e55f → cc04aa1）。

R-G12 git commit 一律帶 pathspec（全域，Pei 2026-08-18 裁定升格）
      所有 session、所有 feature 之執行層，準備 git commit 指令時
      一律帶 pathspec：`git commit -- <pathspec>`；
      **不得使用不帶 pathspec 之 `git commit`**。
      理由：不帶 pathspec 之 commit 提交整個 index，
      而 index 可能已含另一 session 置入之檔案。
      052f67d 與 645e55f → cc04aa1 為同一成因之兩次發生 ——
      **兩次皆非疏忽，是該作法本身會產生此結果。**
      `git add` 亦同：一律帶明確路徑，不用 `git add .` 或 `git add -A`。
      執行層仍只準備不執行（R-G5）。
```

**本包產生之新條文清單（自檢）**：R-U55 ✓　R-G12 ✓（皆以區塊形式出現）

## 作業

1. **條文入庫** — R-U55、R-G12 逐字追加；R-G12 併全域段。
   `ANOMALIES.md` 之相關項改記為 **ACCEPTED（非 RESOLVED）**
   —— 狀態未改變，是被接受；並照錄其「第二次發生」之事實。

2. **待執行之 git 指令清單** — 依 R-G12 重寫（全部帶 pathspec），
   合併 10–14 輪之累積項，回報完整清單供 Pei 執行。
   **執行層不執行**（R-G5）。

3. **R-G12 之跨 feature 通知** — 於 `docs/fw036/FEATURE_ONBOARDING.md`
   之全域條文段寫入 R-G12，使其他 session 讀得到。
   **不寫入他 feature 之 RULINGS.md**（R-U24／R-U30／R-U44 之界線不變）。

## 與 14 包之關係

14 包（pilot 覆核之 D-1～D-3 阻塞項、D-4 補閘、D-5／S-1／N-1～N-3）
與本包**同輪下放**，無先後依賴。
上繳合併為 `docs/upstream/14_pilot_fixes.md`，本包之項目另立一節。
