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
| 04 | 2026-08-17 | 記載更正、十一條入庫、四項實質查證（三閘反向驗證／Service 22 條／14 節帶圖／R-G4 前置） | [handoff/04a_rulings.md](handoff/04a_rulings.md)＋[04b_rulings.md](handoff/04b_rulings.md)＋[04c_tasks.md](handoff/04c_tasks.md) | [upstream/04_verification.md](upstream/04_verification.md) | R-U13 ~ R-U20；**R-G4／R-G5／R-G6（全域）** | A-UP04 **RESOLVED**；A-UP09 維持 PENDING（R-U14 定其解除條件）| **作業 1–7 全部完成。三閘反向驗證 6/6；`Service` 22 條無一符合 R-C38；14 節帶圖 = 不依賴 8／部分 5／完全 1；R-G4 已實作＋反向驗證 5/5。本輪未執行任何 git** |
| 05 | 2026-08-17 | 跨 feature 掃描（唯讀）／home 讀者實驗／抽圖能力／PLP 表／framework 草案 | [handoff/05a_rulings.md](handoff/05a_rulings.md)＋[05b_tasks.md](handoff/05b_tasks.md) | [upstream/05_framework_draft.md](upstream/05_framework_draft.md) | R-U21 ~ R-U24；**R-G7（全域）** | A-UP02 之性質重估待裁（spec 有而 SWE 未涵蓋）| **作業 1–6 完成。無污染；危害由推導變觀察（chapter 6 種→1 種 `SWE`）；**圖在 PDF 不在 xlsx**，6 節中 5 節改判、完全依賴歸零；PLP 表可讀；framework 草案落檔** |
| 06 | 2026-08-17 | 基線稽核：169 條逐節比對 xlsx vs PDF；PLP3；PU id 擴充；R-U27／R-U28 落地 | [handoff/06a_rulings.md](handoff/06a_rulings.md)＋[06b_tasks.md](handoff/06b_tasks.md) | [upstream/06_baseline_audit.md](upstream/06_baseline_audit.md) | R-U25 ~ R-U30；**R-G4-1**（R-G4 之修訂，原文保留）| A-UP02 性質重估落地；**N-XF01 跨 feature note 新開** | **判定系統性掉句 → 停手上報，未重建 outline_map.json。掉句率三個數：17.1%（上界）／9.3%（加頁界）／**2.9% 真掉句**。PLP3 可讀且不需抽圖。framework 未定稿** |
| 07 | 2026-08-17 | 基線稽核（二）：跨頁反向驗證／29 無標籤節／outline_map 增欄與補句表／Service 22 條 PDF 複查 | [handoff/07a_rulings.md](handoff/07a_rulings.md)＋[07b_tasks.md](handoff/07b_tasks.md) | [upstream/07_baseline_audit_2.md](upstream/07_baseline_audit_2.md) | R-U31 ~ R-U34；**R-G8（全域）** | —（無新開；補句表登記 7 條）| **0 個跨頁條款 → 2.9% 不再是下界。對照向揪出 06 輪之定位器缺陷（重複標籤 `PRACC7.` 被兩節共用）。三比率重報 17.1%／9.3%／**3.6%**。Service 22 條 0 條改變 → R-U21 維持。framework 仍未定稿** |

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

### 第七輪已完成（2026-08-17）

- **R-U34：0 個跨頁條款。** 兩種互不相關之方法皆為負 ——
  尾句探針（次頁命中 1 節，經查為定位錯非跨頁）＋ 與 xlsx 無關之盲點檢查
  （頁末斷句＋次頁小寫續起，**0 / 20 個頁界**）。
  **故 2.9% 不再是下界**；訂正後之 C 為 **3.6% 節數／2.1% 字元**。
- **對照向揪出 06 輪之定位器缺陷** —— `PRACC7.` 被 `4.7`（p6）與 `5.1`（p7）
  **共用**，06 輪取第一個命中，於是把 `5.1` 對到了另一條條文。
  140 個標籤中 3 個重複。已加兩道修正（行首比對＋相似度消歧）。
  **這不是任何一條指示要找的東西，是對照向的副產品。**
- **三比率重報，各附分子定義**（R-G8）：
  **A 無頁界 17.1%／16.3%**、**B 加頁界 9.3%／6.2%**、**C 真掉句 3.6%／2.1%**。
  C 由 06 輪之 4 節改為 5 節 —— **計數單位不同**（`11.4`／`11.5` 分計），非計算錯誤。
- **29 個無標籤節**：26 命中、3 查無。其中 **`2.1` 是唯一一節 xlsx 比 PDF 完整者**
  （其參考文件表於 PDF 為圖）—— R-U25 之「xlsx 結構／PDF 內文」分工於此有例外。
- **R-U31 落地**：`outline_map.json` 增 `pdf_text`／`divergence`，**`text` 逐字未動**；
  補句表 7 列；`**` 註記全量 **10 條、6 有 4 無**（與下放包相符，惟條數隨 pattern 而變，
  另一 pattern 得 12 —— 檔頭已載明 pattern）。
- **R-U32：Service 22 條 0 條分群改變 → R-U21 維持。**
  **惟其地位變了** —— 06 包列為「未量之邊」，本輪把那條邊量了。
  結論相同、依據面不同，記錄上須分開。
- **作業 6 只清點未改**：`expected_cited_sections.tsv` 與
  `generation_sections.tsv` 各有 **9 列**之 `chars` 欄受影響。

### 第六輪已完成（2026-08-17）

- **169 條全掃（不抽樣）**，分母為標籤可定位之 **140** 節；
  逐節結果落 `data/xlsx_pdf_audit.tsv`。R-G7 對照向 PASS。
- **掉句率三個數，差六倍，資料同一份**：
  **17.1%**（第一版切段，把下一頁之頁首／圖說／表格算進條文，**高估**）→
  **9.3% 節數比／6.3% 字元比**（加頁界）→ **2.9%（4 節）真掉句**
  （逐條讀完，把切段殘留剔除）。
- **判定為系統性 → 依 06b 作業 3 停手上報，未重建 `outline_map.json`。**
  理由不在百分比：掉的是**變體覆寫註記**（決定適用範圍）、**表格內容**
  （決定 ER 列舉）、**含 PU id 之整句行為條文**；且 `9.8` 掉的是**純段落句**，
  **指不出一個「不會掉」的節型**。`****` 註記 10 條中 6 進 4 不進 ——
  **同形態時有時無，比整類都掉更難防**。
- **04／05 輪判讀之依據面已逐列標示**；要緊者為 **`Service` 22 條全部讀 xlsx**，
  而本輪證明 xlsx 可能少句 —— R-U21 之裁定因而有一個未量之邊。
- **PLP3 可讀，且不需 `pdfimages`** —— 一直在文字層；05 輪未定位到是因
  五表並排使其排在標籤**之前**。死路已記錄：**不是抽圖能力問題，是切段方向問題**。
- **`spec_popup_ids.tsv` 20 → 32**，加 `source` 欄；原 20 列記載未改。
- **DR #4 降 MEDIUM 並收窄**（spec 已載觸發條件，缺的只是 popup 內文）；
  **DR #3 性質改為上游覆蓋缺口**；`PROF-002-03` 解除阻斷。
- **N-XF01**：comfort 孤兒檔登為跨 feature note，**comfort 一個檔都沒動**。

### 第五輪已完成（2026-08-17）

- **跨 feature 掃描（唯讀）：無污染。** comfort 為 recon 形態**而非被污染**
  —— 它從無 `build_outline_map.py`，四份文件一致記載為「403 leaf 查表」，
  且無任何讀者。sxm／amfm／projection **無此檔**。
  **惟 R-G4 給 comfort 留下一個孤兒檔之連帶，待裁。**
  另更正 04 輪之漏數：home 之讀者是 **三個**（`extract_exemplars.py` 亦讀）。
- **home 實跑做不到** —— 其 `inputs/` 不存在（R-G2 條文自身所記）。
  改以「直接餵兩形態給三個讀者」，**危害由推導變為觀察**：
  chapter 集合由 `{BSP HS HSD HSS SNS SW}` **退化為 `{SWE}`**。
  含 R-G7 之兩個對照向，兩者一致。**`lint_tcs` 那一半仍是推導**（§2.3）。
- **抽圖能力：圖不在 xlsx，在 PDF。** spec xlsx **0 張內嵌圖**；
  BASELINE 第四列之 PDF 有 21 頁／174 個 Image XObject／有文字層。
  **與 Comfort A-CF23 方向相反 —— 不是缺讀取能力，是找錯檔案。**
- **6 節中 5 節改判，完全依賴歸零**：`8.2` 由**完全依賴**改為**不依賴**
  （流程圖之步驟／PU id／按鈕／分支全可讀），`6.2`／`9.1`／`10.2` 由部分改為
  不依賴；`11.4`／`4.6` 維持部分依賴（`4.6` 之理由改為 **spec 自稱圖示為
  placeholder**）。**04 包 §6.1 之 DR 候選建議撤回。**
- **PLP 表可讀**（R-U22）→ `PROF-001-01` 正常生成；
  **A-UP02 重估為「spec 有而 SWE 未涵蓋」**，形態同 Comfort R-C16。
- **順帶查到**：`spec_popup_ids.tsv` 之 20 個少算，PDF 全文有 **32** 個
  （12 個只出現在圖裡）；且 **`PU1087`／`PU1088` 在 spec 裡有觸發條件**，
  缺的是 Pop Up List 之內文 —— **DR #4 之範圍可能應收窄，待裁**。
- **`framework.md` 草案落檔**，每個數字複驗相符（180 leaf／133 生成 section）。

### 第四輪已完成（2026-08-17）

- **十一條入庫**（R-U13～R-U20、R-G4～R-G6 逐字）；三條全域條文另列。
- **R-G6 記載更正**：03 包 §8 之「git 未執行」改為據實之「執行了一次
  `git checkout`（單一檔案）」；§7.1 未動。R-G5 已追認該次還原，
  並裁定**其作法為錯** —— 遇覆寫事故應兩版並存、上報、停手。
- **A-UP04 → RESOLVED**（R-U18），永久記載限制照錄：
  **Phase 0 之 037 側數字沒有被複驗，也永遠不會被複驗**。
- **三閘反向驗證 6/6** —— 三型注入各自轉紅並報出正確差額；037 原檔雜湊
  前後一致。**含一個「複製＋重存但不改資料」之對照組** ——
  沒有它，另外三向證明不了紅燈來自注入。兩項標「未實測」而非 PASS。
- **`Service` 22 條逐條讀完：無一條符合 `[BLOCKED-NON-HMI]`（R-C38）**。
  該欄標的是「誰執行」而非「看不看得見」；ch4 之 12 條全屬「來回一趟」
  可觀察。**03 輪擔心的一整章返工不會發生。** 另揪出兩條屬別的阻斷
  （`PROF-002-03` 落 R-U15、`PROF-001-01` 依賴 A-UP02 之 PLP 表）。
- **14 節帶圖：不依賴 8／部分依賴 5／完全依賴 1**。
  **`8.2` 全文即「See flow … above」，一個可驗步驟都沒有 → DR 候選。**
- **R-G4 實作＋反向驗證 5/5**。前置查證揪出：home 之檔是**第三種 schema**，
  且 `make_batch_context` 之 `^([A-Z]{2,4})` **會命中 `SWE`** ——
  recon 若落在該檔名上，**每個 outline 之 chapter 都會變成 `"SWE"`**，
  不是崩潰，是安靜的錯答案。
- **R-U19／R-U20 落地**：`data/generation_sections.tsv`（133 列）新建，
  `expected_cited_sections.tsv` 未改；`feature.yaml` 記八組 Layer 2，
  **逐組實測全部相符，合計 180**。

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
| ~~A-UP04~~ | **已 RESOLVED（R-U18）** | — |
| ~~135 vs 133~~ | **已裁（R-U19，兩者分立）**；`data/generation_sections.tsv` 133 列已建 | — |
| ~~`spec_id_to_outline.tsv` 之檔名~~ | **已裁（R-G4）並實作**；recon 改寫 `recon_leaf_to_section.tsv`，另加不得無聲覆寫之前置檢查 | — |
| **A-UP09 之 x14 DV gate** | R-U14 定其為解除條件；**gate 未立前寫回不得開工** | **擋 Phase 6** |
| **其餘四個 feature 之 `spec_id_to_outline.tsv`** | 現況未掃；若已是 recon 形狀則帶著 §7.2 之錯答案 | 不阻擋，未查 |
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
