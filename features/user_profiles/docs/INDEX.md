# User Profiles — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-17（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-17 | Phase 0 intake（開案）：scaffold／R-G1 R-G2 R-U7 form 處置／recon／outline map／framework 草案 | [handoff/01_intake.md](handoff/01_intake.md)＋[01a_rulings.md](handoff/01a_rulings.md)＋[01b_tasks.md](handoff/01b_tasks.md) | [upstream/01_intake.md](upstream/01_intake.md) | R-G1、R-G2（全域，本包首次落檔）；R-U1 ~ R-U7（本 feature） | A-UP01 ~ A-UP03（下放包播種，A-UP03 本輪 RESOLVED）；**A-UP04 ~ A-UP09 新開** | **作業項 1／2／4(spec 側)／5(草案)／6 完成；作業項 3 停下 —— 037 不在 repo（A-UP04）＋ 預期值單位不一致（A-UP07）。相符 18／不符 4／未實測 12（4 項待裁）** |
| 02 | 2026-08-17 | 02a 裁決之落地：R-U8 三閘／R-U9 PU 涵蓋驗證／R-G3＋R-U10 canon 修補／R-U12 歸檔雜湊／異常狀態 | [handoff/02a_rulings.md](handoff/02a_rulings.md)＋[02b_tasks.md](handoff/02b_tasks.md) | [upstream/02_rulings_execution.md](upstream/02_rulings_execution.md) | R-U8、R-U9、**R-G3（全域）**、R-U10、R-U11、R-U12 | A-UP05／07／08 **RESOLVED**；A-UP09 修補完成待覆核；**A-UP06 不結案** | **作業 1–5 完成；6–8 未執行（DR #1）。R-U9 涵蓋率 18/20 → 不採用、開 DR #4** |
| 03 | 2026-08-17 | Recon 開工（DR #1 到齊）：037 採認前置／R-U8 三閘／037 側複驗／BASELINE／spec 同一性／Layer 2 草案二版 | [handoff/03_recon_start.md](handoff/03_recon_start.md) | [upstream/03_recon.md](upstream/03_recon.md) | （未產生新裁決；R-U13 ~ R-U17 仍待裁）| A-UP02 於 **037 側首次證實**；A-UP04 解除條件已滿足**待裁** | **作業 1–6 全部完成。三閘 180／25／2 相符；集合對集合 135＝135 差集皆空；BASELINE 6/6 OK；兩份 spec SHA 相同（未處置）** |

---

## 2. 現況

### 已完成

- **Scaffold**：`features/user_profiles/` 全套就位；下放包三檔未被覆寫。
  `RULINGS.md` 含 R-G1／R-G2／R-U1 ~ R-U7 **逐字**；
  `ANOMALIES.md` 含 A-UP01 ~ A-UP09。
- **036 母本處置（R-G1／R-G2／R-U7）**：三份舊檔以 `mv` 移入
  `archive/forms_superseded/`（**未刪除**），移前移後 SHA256 一致；
  `forms/` 僅餘 `…_SWQT_20260817_ext.xlsx`。母本結構探測六項全完成並寫入
  `forms/FORMS.md`；R-G1 亦寫入 `docs/fw036/FEATURE_ONBOARDING.md` §0。
  母本未被覆寫（**openpyxl save 全 repo 未執行**）。
- **BASELINE.sha256**：4 筆（inputs/ 1 ＋ spec-index Personal Account 3），
  `shasum -c` **4/4 OK**。
- **spec 側 outline map**：169 條，單一 stem、0 unparsed、0 重複、
  `Outline Number` 169/169 一致。候選被引集合 135 條已落檔。
  spec 全文唯一 PU id **20 個**（與下放包相符）。
- **workbook_state = BLANK**：獨立實測佐證 R-U6（A–AH 全欄非空格 0）。

### 第三輪已完成（2026-08-17）

- **037 已到齊並落錨**：SHA `9d176dde…` 首次進 BASELINE。Phase 0 之 037 側
  數字係在 **Project 附件副本**上量得且未比雜湊，本輪全部重測 ——
  **不是複驗，是取代**（該副本不在 repo，無從對它算雜湊）。
- **R-U8 三閘全數相符**：`Functional Requirement` **180**／`Heading` **25**／
  `Out of scope` **2**，合計 207 = 資料列數。未調整任何判準。
- **對照輸出 182 = 180 ＋ 2 Out of scope** —— A-UP07 之診斷由資料證實。
  另記 `recon.py` 之第三個數（被禁判準會選 **72**）：三個數並列，
  使日後無人再把其中兩個相減。
- **集合對集合 135 = 135，兩側差集皆空**；並查明 `recon.py` 之 133 與 135
  之分野 —— `4.7`／`5.11` **只被兩個 Out of scope leaf 引用**。
- **表頭列實得 row 7**；FROP 欄 `User Profiles` **182** 列，R-U1 首次複驗成立。
- **A-UP02 之 8 條於 037 側首次證實**（未被引之 34 條中含 `10.1`／`11.1`／
  `11.2` 與 `3.1`–`3.5`）。
- **BASELINE 4 列 → 6 列，`shasum -c` 6/6 OK**。
- **兩份 spec SHA256 相同**（`368d5874…`）—— **只驗未處置**，
  未刪未搬未改引用路徑；兩份皆列入 BASELINE 各自受檢。
- **Layer 2 草案第二版**：037 之 25 個 Heading 與章別分布到齊，
  出 11／8／6 三案，§4.2 三項命名問題逐項提案（Tier 2，不自裁）。
- **本層在本輪犯了一個錯並已處置**：跑 `recon.py` 前未查它會寫哪些檔，
  其產物覆蓋了 01 輪之 `data/spec_id_to_outline.tsv`（**同名而不同物**）。
  已還原，recon 之產物改置 `data/recon_leaf_to_section.tsv`，兩者皆不遺失。
  檔名歸屬屬 Tier 2（`features/home` 亦有讀者）。

### 第二輪已完成（2026-08-17）

- **R-U8 三閘落地**：`recon_assertions` 由 `TBD` 改填 **180／25／2**，
  182 降為對照輸出。**閘未跑** —— 037 仍不在 repo。
- **R-G3＋R-U10 canon 修補**：`docs/fw036/framework.md` §Workbook sync
  加 openpyxl 禁用警示（引 A-UP09 實測表）、範例改 `xlsx_surgical` splice、
  `Test Case Framework` 分頁項標 **rev A/B only**。
- **R-U12**：`archive/forms_superseded/BASELINE.sha256`（3 檔），
  `shasum -c` **3/3 OK、0 警告**。該目錄在此之前**不受任何雜湊保護**。
- **A-UP05／A-UP07／A-UP08 RESOLVED**；A-UP09 修補完成但**狀態變更屬 Tier 2**，
  本層不自裁，標為待覆核。

### 停下待裁 / 待覆核

| 項 | 內容 | 阻擋什麼 |
|---|---|---|
| **A-UP04** | 037 已到齊、三閘已過，**解除條件表面已滿足**；狀態變更屬 Tier 2，本層不自裁 | 不阻擋 |
| **135 vs 133** | 生成相關之被引 section 為 133；`expected_cited_sections.tsv` 仍 135（未改）| Phase 3 之覆蓋率分母 |
| **`spec_id_to_outline.tsv` 之檔名** | 兩個生產者同名而不同物（全域）| 不阻擋；再跑 recon 會再覆蓋一次 |
| **A-UP06** | **R-U9 之涵蓋驗證結果為 18/20**，缺 `PU1087`／`PU1088`（皆出自 spec `4.1.1` Profile Setup）。依 02b 明文不以近似版本替代 | Phase 3 之 popup 詞彙表；**已開 DR #4** |
| A-UP09 | R-G3 之修補已完成，**惟現行防線只是一段散文，無機器檢查** | 不阻擋；建議下一包立 gate（見上繳 02 §6 第 1 項）|
| Layer 2 | Test Set 邊界三草案（7／11／6 個 Set），**037 分群不可得，草案為 spec 單邊**；§4.2 之三項命名問題待併 | Phase 3 framework Part N |

### 阻擋中（素材，Tier 3 由 Pei 送出／取得）

| DR | 檔 | Urgency |
|---|---|---|
| #1 | `FM-WI-FSM-037-A03 N1L SWE1 Personal Account HMI V0.1 STLA 報告.xlsx`（A-UP04）| **BLOCKING** —— recon 全停 |
| #2 | HMI Pop Up List（A-UP06）—— **部分到齊 18/20**，見 #4 | 高（Phase 3 前）|
| #4 | **載有 `PU1087`／`PU1088` 之 Pop Up List 版本**（本輪新開）| 高（Phase 3 前）|
| #3 | A-UP02 之 8 條無覆蓋條文 RD-1 | 中 |

### 實作約束（已實測，非待裁）

- **A-UP09**：openpyxl 存回摧毀母本 R 欄 x14 下拉
  （`<x14:dataValidation>` 1 → 0、zip members 48 → 47，三條 legacy DV 存活）。
  Phase 6 寫回**不得**以 openpyxl 存回。`feature.yaml`
  `write_back.forbid_openpyxl_save: true`。

### 下一包之前置

1. ~~先裁 A-UP07~~ **已裁（R-U8）**，期望值已填。**037 到齊即可跑 recon。**
2. 037 到齊後：跑 `scripts/recon.py`（三閘 180／25／2，182 為對照輸出）、
   更新 `BASELINE.sha256`（**須加入 037**）、以
   `data/expected_cited_sections.tsv` 做 135 條**集合對集合**命中驗證，
   並補 01 輪列為未實測之五項（header row 7、FROP 欄 182 列值、
   PROF-017／035 之 Out of scope 身分、Sub Categorization 與 Priority 分布）。
3. Layer 2 定版後方可附 `docs/fw036/framework.md` Part（仍未附）。
4. **建議立一道 gate 保住 R-G3** —— 現行防線是散文，而 A-UP09 自己說了
   「靜態讀取驗不到只在寫入時才成立的性質」。Comfort `write_back` §3.3 之
   `x14`／zip-member assertion 可直接借用。

---

## 3. 資料產物

| 檔 | 列數 | 說明 |
|---|---|---|
| `data/spec_id_to_outline.tsv` | 169 | section id → outline／polarion id／實體列號／字元數（tracked）|
| `data/outline_map.json` | 169 | 含 Description 全文 |
| `data/expected_cited_sections.tsv` | 135 | 候選被引 section（037 到齊後之比對基準）|
| `data/spec_popup_ids.tsv` | 20 | PU id → 引用次數／section |

腳本：`scripts/build_outline_map.py`
