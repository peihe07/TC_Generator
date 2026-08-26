# 下放包 07 — Bed Lowering Mode：pilot 寫回 + 工程債收斂 + 續批計畫

日期：2026-08-26
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01–06，取 07
對象：執行層（Tier 1）
依據：R-BLM14（pilot 退出通過、寫回授權、reasoning 定式、工程債收期）。
下放包 03–06 其餘條款繼續有效。

---

## 一、寫回前之兩處小修

1. 038-04 Pre-Condition 6 改寫（R-BLM14(3)）：
   `The SYS1 normalised text of NRL-193702 is available to the tester as the wording baseline`
2. manifest 重 stamp（逐源）

## 二、pilot 13 條寫回工作簿

1. **XML 外科式**（R-BLM3）：zip 開檔 → 僅改目標儲存格 XML → 原樣重打包。
   任何路徑不得經 openpyxl 存檔
2. 寫回欄位依 canon：BLANK → FILL（test_group `Bed Lowering Mode`、
   test_set `Fault Handling`）、author `PeiPYHsu`、tc_ref_id `NEW`、
   TC ID `{project}-BLM-001` 起連續 13 號（project 前綴依 feature.yaml）、
   N 欄 = R-BLM5 單行常數
3. 寫回前後保全計數比對（R-G1 計數清單，legacy 與 x14 分開計 ——
   上繳 02 之口徑）：不符即停
4. 寫回後自工作簿**讀回** 13 列與 `pilot_tcs.json` 逐欄比對（round-trip 驗證），
   差異為 0 方為完成；工作簿 sha256 回報
5. reasoning 不入工作簿（profile §4）

## 三、工程債收斂（R-BLM14(4)：續批開工前須收，本包收）

1. **generator 實跑**：以 pilot context 走一次 `backend/prompt_builder.py` →
   `backend/generator.py` 之組 prompt 路徑（可 dry-run 不呼叫模型），
   回報組出之 prompt 結構是否完整含 rows／rules_text／signal_candidates。
   組不出來 → 停下回報，那是續批的生成路徑，不能再靠 session 手寫
2. **`scripts/lint_tcs.py`（本 feature 版）**：自最近之 feature lint 移植，
   檢查面至少含：括號下半存在＋語言、尾句號、引號式、N 欄值、
   禁用主動詞（**含句中形態**，上繳 05 之教訓）、ER 情態動詞、
   §10.1 十鍵齊備。pilot 13 條過 lint 回報
3. **`recon.py` 實跑**：配置已追認（R-BLM8），R-G4 之顧慮解除。
   跑後與 `data/*.tsv` 對帳，差異回報（預期 0）

## 四、續批計畫（提案，Pei 認可順序後逐批下放）

母體：176 − 13 = **163 leaf**。分批依 Test Set 整組取用（不手挑，pilot 慣例），
順序提案（小→大暖機、訊號密集群靠前以早暴露 DBC 缺口）：

| 批 | Test Set | leaf | 備註 |
|---|---|---|---|
| B1 | Restore And Exit | 9 | 小組暖機；含超速退出（DR-1 速度門檻**必然命中**，PENDING 落法首驗）|
| B2 | Activation Gating | 28 | Service 21 條密集；車速/ignition 訊號預查量大 |
| B3 | Lowering Operation | 33 | DT vs DJ/D2 變體軸（PROXI 首用）|
| B4 | Cluster Feedback | 13 | chime 可執行性議題 |
| B5 | HU Feedback | 20 | status bar 圖示 |
| B6 | Feature Entry | 31 | |
| B7 | Display Legibility + Access Ergonomics | 29 | 人因群，R-BLM2 之 gap disclosure 在此批落地 |

每批流程沿 pilot：訊號預查（查有/查無入 manifest）→ 生成 → 機檢+lint →
上繳交審 → 審過寫回。**R-G14 綠色通道**：連續 3 批乾淨（分析層審無 A 類項）
後自動續批，僅上繳留檔，Pei 抽查即可。

## 五、停點

§一～§三完成後停，上繳包 07（含寫回 round-trip 證據、三件工程債收斂結果、
續批 B1 之訊號預查先行結果）。**B1 生成不在本包**——待 Pei 認可 §四順序。

## 六、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 已登記，未送出。B1 將首驗其 PENDING 落法；**建議此時送出**，由 Pei 決 |
