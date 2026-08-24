# INDEX — FW036 Power Moding

執行層於每次上繳時更新（canon §8.7）。分析層不寫此檔。

feature 之交付夾為 `ASW-R2/Disclaimer screen/`（FROP 標籤），
身分為 `Power Moding`（規格標題模組名）—— R-PMH2，Comfort R-C6 同型。

| NN | 日期 | 主題 | 下放 | 上繳 | 新條文 | 新 anomaly | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-22 | 開案：骨架、裁決落檔、Phase 0 intake 實測 | [handoff/01_intake.md](handoff/01_intake.md) | [upstream/01_intake.md](upstream/01_intake.md) | R-PMH1–R-PMH6（分析層，逐字抄錄 6/6 相符） | A-PMH01–A-PMH05 | **步驟 1–8 全數執行；停止條件 2、4 觸發，已停於待裁** |
| 02 | 2026-08-23 | 母本改定、`workbook_state` 改判、Phase 1 前置 | [handoff/02_baseline_switch.md](handoff/02_baseline_switch.md) | [upstream/02_baseline_switch.md](upstream/02_baseline_switch.md) | R-PMH7–R-PMH12（逐字抄錄 6/6 相符） | A-PMH06–A-PMH08；A-PMH01／A-PMH05 → RESOLVED | **步驟 1–10 全數執行；九條停止條件全未觸發** |
| 03 | 2026-08-23 | Test Group 欄值改判、DV 列舉值實測、Phase 1 recon | [handoff/03_testgroup_and_dv.md](handoff/03_testgroup_and_dv.md) ＋ [03a_pei_rulings.md](handoff/03a_pei_rulings.md) | [upstream/03_testgroup_and_dv.md](upstream/03_testgroup_and_dv.md) | R-PMH13–R-PMH18（逐字抄錄 7/7 相符） | A-PMH09、A-PMH10；A-PMH06（附 PENDING-CANON）／A-PMH07 → RESOLVED | **步驟 1–8 全數執行；九條停止條件全未觸發** |
| 04 | 2026-08-23 | R-PMH10 證據基礎更正、母體判準、機器檢查補實 | [handoff/04_corpus_and_assertions.md](handoff/04_corpus_and_assertions.md) | [upstream/04_corpus_and_assertions.md](upstream/04_corpus_and_assertions.md) | R-PMH19–R-PMH23（逐字抄錄 5/5 相符） | A-PMH11／A-PMH12；A-PMH09 → RESOLVED、A-PMH10 證據更正 | **步驟 1–7 全數執行；九條停止條件全未觸發** |
| 05 | 2026-08-24 | 母體判準修正、Q3 完整語料、Phase 3 前置 | [handoff/05_corpus_fix_and_framework_prep.md](handoff/05_corpus_fix_and_framework_prep.md) | [upstream/05_corpus_fix_and_framework_prep.md](upstream/05_corpus_fix_and_framework_prep.md) | R-PMH24／R-PMH25（逐字抄錄 2/2 相符） | （未立新 A-PMH —— 新發現皆為停止條件之回報） | **步驟 1–6 全數執行；停止條件 7、8 觸發，已查明並回報** |

## 01 輪要點

**相符者**
- 037 `Functional Requirement` = **48**、`Heading` = **8**、
  R-G10 餘數 = **0**（56 − 48 − 8）
- 037 `HMI Source ID` 文件 stem 相異 = **1**
- 036 非空欄集合 `{B,D,G,H,I,L,M,N}` 各 48、`F`/`AB` 各 0、
  `L` 具編號步驟 0、5 個合併範圍、`D5` 空白、10 分頁 —— 逐項與下放包相符
- 素材四份 `shasum -c` 全 OK，搬入前後與來源複測三次雜湊一致

**不符者（一項）**
- 037 `FROP` 相異值：下放包 **13**／實測 **12**。成因為對全 56 列取
  `set()` 未排除 8 個 Heading 列之空值 → **A-PMH01**。
  下放包自身之分布明細即為 12 項且逐項相符。R-PMH6 之引用數待更正。

**新增實測（下放包未涵蓋者）**
- **036 版面為 A–AI 共 35 欄**，非 rev C 之 34 欄；`priority` 起每欄較
  rev C 右移一格（priority **Q**／design_method **S**／
  functional_safety **T**／author **AB**／remarks **AI**）。
  **AH 在本版面是 Defect ID** —— 誤用 rev C 之 AH 會寫錯欄。欄位對應 **16/16**。
- **R-PMH5 之機械搬運宣稱經 336 格逐字驗證，48×7 全部相符。**
- 037 之 48 id 與 036 D 欄 48 id **依序逐一相符**（1:1 實證）。
- **`workbook_state`：filled 48／qualifying done 0** → canon §2 四類皆不合，
  依停止條件 2 未自行歸類，記 `PENDING_RULING`。
- **spec_mode 提案 `A+B`**：PDF 文字層產出率 **11/11 = 100%** 但
  **可錨定編號章節 0**（Visio 流程圖冊，無目次）；SYS1 匯出 **52 outline**，
  037 引用之 **29 章節命中 29/29**。依通則 3 指定
  判讀基準 = PDF（內文面）、追溯用 = SYS1 匯出（結構面）。
- **canon §3 之 Home 型漏句於本 feature 未觀察到**：43 則可比對描述中
  **39 則逐字命中 PDF**；4 則之缺口為重排（7.1）、拼字（8）、
  `-layout` 條列再流（9.1／11.1）→ A-PMH03。
- **SYS1 匯出 6 則 outline 為圖片佔位**（2.1/3.1/4.1/5.1/6.1/12.4），
  內容僅存於 PDF p3–p7 流程圖；該六者不在 037 之 29 章節內 → A-PMH04。

**canon 層之衝突（停止條件 4）**
- **A-PMH05** —— scaffold 之 `.gitignore` 以 `inputs/` 整夾排除，
  使通則 9 所要求「須入版控之雜湊檔」被忽略。非本 feature 專屬。
  附帶：`sandbox/` 亦不在 `.gitignore` 內。**本包未動 `.gitignore`。**

**待裁**：Q1（`workbook_state` 新狀態名）／Q2（036 母本身分）／
Q3（`D5` 範圍欄）／A-PMH01（R-PMH6 引用數）／A-PMH05（雜湊檔落點）。

**下一包之首要建議**：讀 036 之 `Test Case Framework` 分頁 —— 其名稱直指
Phase 3 產物，可能已含客戶側之 Test Group／Test Set 期望，會改變 R-PMH6
之輸入集合。詳見上繳 §9（該驗而未驗者六項）。

## 02 輪要點

**基底更換**
- **交付基底改為 R-G1 全域母本**（R-PMH7）。實測 SHA256
  `6372fb6b…6fb825b2` 與條文所載逐字相同；判準（34 欄、
  `Estimated Test Time` 恰一次）**通過**，客戶那份依同一判準判為離群
  （35 欄、兩次）—— 判準有鑑別力。
- **01 包之 16/16 欄位對應作廢**（R-PMH9）。母本重測 16/16，
  `priority` 起五個鍵各左移一格：**P／R／S／AA／AH**。
- **四方交叉佐證通過** —— 母本 ＋ UP 20260820 ＋ Comfort 20260817 ＋
  TM 20260822，r9 表頭 **34/34 逐欄相等**（停止條件 7 未觸發）。
- `workbook_state` → **`BLANK`**（R-PMH8）。母本資料區非空儲存格 **0**。
- `last_capacity_row` = **1411**（B 欄公式與四組 DV 之 sqref 二證同值）。
- **x14 DV 確認存在**：`R10:R1411` → `下拉選單!$A$1:$A$9`。
  全程未以 `openpyxl` 存回（停止條件 9 未觸發）。

**清償 01 包之未驗項**
- `Test Case Framework` 分頁 —— **完全空白**（0 非空儲存格）。Q8 得解，
  R-PMH6 之輸入維持兩項。01 §9 第 6 項（自評風險最高者）**結果為陰性**。
- `下拉選單` vocabulary **9 項全集實測**，母本與客戶那份 A1:A9 逐項相等。
- PDF **圖像抽取能力實測完成**：150 DPI 足供向量流程圖判讀，
  300 DPI 方能辨讀內嵌 UI 截圖之內文。§9.1 通則 6 之跨形式試驗至此完備。

**`data/outline_map.json`**
- 48 leaf → outline → PDF 頁次，**0 未解**；**29/29 章節命中重現**。
- **兩種先驗定位方法皆被 fail-loud 攔下**（A-PMH08）：頁首逐字相等法
  21/48 未解；子字串包含法「全解但有錯」（ch7→p3、ch9→p1 皆誤）。
  定案方法為「該節描述首 N 字唯一命中，N 依 80→60→40 遞減」。
- 48 leaf **無一落在 p3–p7 流程圖頁** —— 與 A-PMH04 由另一路徑得出者一致。

**新登記**
- **A-PMH06** —— **R-PMH11 所指定之 `.gitignore` 寫法無效**：git 不遞迴進入
  已排除之目錄，故 `inputs/` ＋ `!inputs/MANIFEST.sha256` 不生效。
  已改為 `inputs/*` ＋ 否定規則並雙向實測通過。**條文未改，須追認。**
- **A-PMH07** —— **R-PMH2 所引之 Comfort R-C6 前例，於交付件上未實現**：
  R-C6 逐字裁「Test Group 欄一律填 Comfort」，而 Comfort 已交付件之
  G 欄 **466 列全為 `Climate Control Interface`**（交付夾名）。
  依交付件類推，本 feature 之 G 欄應為 `Disclaimer screen` —— 與 R-PMH2 相反。
  R-PMH6 已延後 G/H 至 Phase 3，**不阻斷本輪，但 Phase 3 前須裁**。
- A-PMH08 —— 定位方法之兩次失敗，RESOLVED（方法已更換並驗證）。

**已解**
- A-PMH01 → RESOLVED（02 §1.1 採認；R-PMH6 原文 SHA256 `5bb6ebe395b25187`
  未變，勘誤附註置於 fenced block 之外）。
- A-PMH05 → RESOLVED（R-PMH11；實施細節見 A-PMH06）。

**Q7 語料（不提案）**：四份交付件之 `{abbr}` 皆為 `NR1L-{PascalCase}-{NNN}`。
三份之 `{abbr}` = `G` 欄 = 交付夾名 = 檔名 tag；**Comfort 四者互不相同**
（abbr `ComfortHMI`／G `Climate Control Interface`／夾名同 G／tag `Comfort`），
其 abbr 唯一相符者為「規格標題模組名 ＋ HMI」。**語料不足以在
`NR1L-PowerModing-` 與 `NR1L-PowerModingHMI-` 之間判別。**

**下一包之首要建議**：實測母本 `P10:Q1411` 之 DV 列舉值。
`QS Suggestion!B5` 建議 Priority 為「高High／中Medium／低Low／不適用NA」，
而 `user_profiles` 前例記為 `[P0,P1,P2,P3]`，037 實測值為 `High` 形態 ——
三者不一致且本包未判定母本現況。**Phase 4 寫回 P 欄前必須先測**，
否則會寫出逸出 DV 之值。詳見上繳 §11（該驗而未驗者六項）。

## 03 輪要點

**Pei 裁定三項（03a）**
- **R-PMH13 核可** → `test_group` = **`Disclaimer screen`**（交付夾名）。
  R-PMH2 之後半撤回，前半（`feature`／`slug`）維持。H 欄仍待 Phase 3（R-PMH6）。
- **Q7 裁「乙」** → R-PMH16，`tc_id_format` = **`NR1L-DisclaimerScreen-{NNN}`**。
  已知反例（Comfort `ComfortHMI`）隨條保留，**不主張為全案慣例**。
- **A-PMH06 追認** → R-PMH17，RESOLVED。
- **R-PMH18** —— `Disclaimer screen`（小寫 s）與 `DisclaimerScreen`（大寫 S）
  **刻意不同、不得統一**；已以大小寫敏感比對驗二字串逐字相符。

**priority 三方衝突 —— 判定為「不存在」**
- 母本 `P10:Q1411` DV = **`"P0,P1,P2,P3"`**（二證同值），與 canon §10.2 **相同**。
- 四份已交付件 `P` 欄 **998 個非空值全部落在該四值內，逸出 0**。
- 另二方不是同一對象：`QS Suggestion!B5` 是**未落實之改版建議**
  （其標題逐字為「25/10/15 QS確認後建議」）；`High/Medium/Low` 是
  **037 的欄**，不是 036 的 P 欄。**停止條件 7 未觸發。**
- **執行層自我更正**：02 §11 稱此為「最可能造成寫回失敗者」，該評估過高 ——
  成因是把「建議」與「現況」、兩張表的兩個欄並列成三方。

**DV 全量與逸出**
- 母本共 **4 組 DV**：legacy 3（`P10:Q1411`／`T10:Z1411`／`AF10:AF1411`）
  ＋ x14 1（`R10:R1411` → `下拉選單!$A$1:$A$9`）。x14 組 `openpyxl` 讀不到，
  **只有 zip 直讀一證**，已明示。
- **五組 DV × 四份交付件之逸出 = 0**（停止條件 8 未觸發）。
- 新揭表單層瑕疵二項：`AF` 之列舉字串**含前導空白**（` Fail`／` Pending`）；
  `P10:Q1411` **跨 P、Q 兩欄**，使 `Estimated Test Time` 套用 P0–P3 下拉。
  二者因四份交付件該二欄全空而**從未被實際檢驗過**，Phase 6/7 首次填值才會浮現。

**Phase 1 recon**
- `state=BLANK, leaves=48, sections=29, targets=48`；assertion **1/1 PASS**。
  **停止條件 9 未觸發。**
- 對照向：若改用 `-NN` 子項 id 判準只得 **27** leaf，**會漏 21 個父形態但
  自身即為 Functional Requirement 之列** —— R-PMH1 之判準正確，且此對照向
  證明另一個看似合理的判準會漏。
- recon 由**表頭文字**獨立解析所得之 16 欄，與 02 包手測及四方交叉佐證
  **三者一致**，零衝突。
- `DECISIONS.md` 已合併（recon 產出為底 ＋ 8 項 `[RULED]` 補入），
  `DECISIONS.new.md` 已刪除；原檔為未填模板，未丟棄任何內容。

**A-PMH09 —— 客戶那份 036 帶 AMFM feature 血緣（本輪最大意外）**
- 其 `ChangeHistory` **ver C 列已被覆寫**為 AMFM 之寫回註記：字串含
  **`SWE1_AMFM`**，數字為 **143 TC／102 leaf／自 r168 append／既有 158 列**
  —— 與本 feature 之 48 leaf／0 TC／r10–57 **無一相符**；作者 PeiPYHsu，2026-08-10。
- 母本同一格為「新增欄位：預估測試時間(分鐘)」（張愷霏，2026-01-21）。
  即**客戶那份把表單自身之版本沿革覆寫掉了**。
- 這解釋 01／02 包所測之三項離群：35 欄版面、`Cover!D6` 版本為 `A`
  （而其 ChangeHistory 有 A/B/C 三列 —— 檔案自相矛盾）、多出之 `D5:F5` 合併。
- **影響為零**（R-PMH7 已改用母本），但這是 **R-PMH7 之回溯性佐證**：
  **若沿用了它，Phase 7 會把 AMFM 之修訂履歷一併交給客戶。**
- `feature.yaml` 已收緊：客戶那份之**封面三頁不得取用**。

**A-PMH10 —— `組合測試` 字串三處不一致**
- `下拉選單!A6` = `Pairwise / t-wise`；`Reference!C9` 與**表單自身之
  `ChangeHistory` ver A 第 5.g 項**皆為 `Pair-wise / N-wise`。
  三處中兩處一致，不一致者恰是 Excel 實際會驗的那一處。
- 母本與客戶那份**兩檔皆同** → **表單層瑕疵**，非任一 feature 之。
  lint 權威維持 `下拉選單`（實務逸出 0）。

**Layer 2 備料（只列交集與分歧，未擬名、未定 granularity）**
- FROP 與規格章節為**多對多**：3 個 FROP 跨章（`Power Management` 跨 4 章、
  `Disclaimer screen` 與 `Audio Management` 各跨 2 章）；4 個章混 FROP
  （ch10 混 6 個、ch9 混 4 個、ch7 混 3 個、ch12 混 2 個）。
- **兩項輸入單獨任一項都切不出乾淨分割**：只用 FROP 會拆散 ch7／ch10；
  只用章會把 `Disclaimer screen` 之 7 leaf 拆成 5(ch7)+2(ch10) ——
  而本 feature 之交付夾名恰為 `Disclaimer screen`。
- 唯一完全一致區：ch8 ↔ `Audio Management`、ch11 ↔ `Steering Wheel Controls`。
- 23 項未引用 outline 恰為「章節層節點 ＋ Assumptions 全章 ＋ 6 個圖片佔位」，
  無一項是帶實質需求文字而被漏引。

**連帶回報**：`features/comfort/ANOMALIES.md` 新增 **A-CF-EXT-02**
（R-C6 條文與其交付件 466/466 不一致，只記事實與證據，不判定成因、
不提案修改該 feature 之條文）。本輪唯一觸及本 feature 目錄以外之檔案。

**PENDING-CANON 一項**：`scripts/new_feature.py` 之 `GITIGNORE` 樣板仍為
`inputs/` 目錄形態，**任何新 feature 照樣板產出者其雜湊檔都會被忽略**。
Pei 之追認就其字面只及於本 feature，**執行層未改樣板**（03a §四）。

**下一包之首要建議**：`data/sr24_uncited_sections.tsv` 未產出（RECON.md 明點），
本 feature 無 `classify_uncited_sections.py`。23 項之組成已人工分析為無實質
遺漏，**但那是我讀出來的結論，不是機器分類的結果**。詳見上繳 §9（五項）。

## 04 輪要點

**R-PMH10 之依據確不成立 → Q3 待 Pei 重裁**
- 依 **R-PMH19** 建立母體：`ASW-R2` 全樹 `**/*036*.xlsx` **28 候選**
  → 排除 (a) 非根層 **14**、(b) 中間態標記 **1**、(c) 同夾舊版 **2**
  → **母體 11**（≥5，停止條件 7 未觸發）。
- 實測：**`D3` 11/11 空、`D4` 11/11 空、`D5` 8 空 / **3 非空****
  —— 原依據句「語料 5/5 無一填寫」不成立。`D3`/`D4` 之結論不受影響。
- 三個非空 `D5`：**AM:FM** 與 **SiriusXM** 指向 **037 SWRA 報告全名**
  （同一模板，僅 feature 縮寫與日期不同）、**Privacy Mode** 指向
  **CFTS 規格條目 id**（`SWE1_CFTS_022-Privacy_Features`）。
- **01 包 Q3 原提案之「規格文件全名」形態，在母體中零個。**
- 未觀察到與 `Cover!D6` 版本或欄數之相關性。**執行層不提案，Q3 屬 Pei。**
- R-PMH10 標 `[PEI-REOPEN]`，原文 SHA256 `885070968235b262` 未變；
  重裁前三欄一律不寫入，**不阻斷**。

**⚠ 母體判準本身之副作用（本輪最該優先處理者）**
- R-PMH19 之 (a)「根層」規則**排除了 5 個 feature 之交付件** ——
  Home、AppDrawer、Notifications HMI、Vehicle Settings(CFTS044)、VF230。
  它們並非中間態，只是交付夾多了一層。**本包照條文執行，未自行放寬。**
- 若 Pei 之意圖是「所有已交付件」，母體應為 16 而非 11，`D5` 比率會變。
  **Q3 重裁前建議先確認此點**，否則會重蹈「母體未定義」之覆轍 ——
  只是這次母體有定義但可能定錯。

**R-PMH22 —— `write_back` 機器檢查已實作並實跑**
- `scripts/check_write_back.py` 三項：blank 前提／起始列來源／列數差。
- **三次故意失敗全部被攔下**（停止條件 8 未觸發）；**範圍向亦通過**（R-G9）。
- (b) 之注入值刻意取 `outline_map.json` 之 `row_036_customer`（44）——
  檢查不僅擋下，還在訊息中指出該值的來源。
- 03 包 §9 第 5 項自陳「目前只是文字修補」，**本輪已轉為實跑之機器檢查**。
- ⚠ 尚未被任何寫回路徑呼叫 —— 要到 Phase 6 實作寫回時才接得上（已知未完成）。

**`data/uncited_sections.tsv` —— 機器分類**
- `scripts/classify_uncited_sections.py`（新寫，未改共用腳本）。
  餘數驗證 `52 − 29 − 23 = 0`，程式內 `assert` 強制。
- 分類：`chapter_node` 12／`image_placeholder` 6／`assumptions` 5／**`other` 0**。
- 與 03 §7.3C 人讀結論**集合完全相同**，`other` = 0 印證「無一項帶實質需求
  文字而被漏引」。唯一差異為 outline `1` 之分類邊界（人讀歸 Assumptions、
  機器規則歸 chapter_node）—— 依下放包以機器產出為準。停止條件 9 未觸發。

**A-PMH11 —— 全簿 DV 實為 5 組，不是 4 組**
- 遺漏者為 `Product Document 記錄封面頁!B7:C7` = `"Confidential, Top Secret"`。
- **不是量錯，是量詞與量測範圍不一致**（分頁層量測寫成全簿結論）→ R-PMH20。
- 03 §2.2 之結論句已依 R-PMH20 改寫為分頁層陳述並另列全簿清單。

**A-PMH10 之證據全面更正（本輪最重要之發現）**
- **兩檔之 x14 DV 指向不同的 source 分頁**：母本 → `下拉選單!$A$1:$A$9`
  （`Pairwise / t-wise`）；客戶那份 → **`Reference!$C$4:$C$12`**
  （`Pair-wise / N-wise`）。九項中八項逐字相同，僅第 6 項不同。
- 03 包「兩檔皆同 → 表單層瑕疵」**不正確** —— 客戶那份之 `下拉選單` 是
  **孤兒分頁**（存在、與母本相同、但無任何 DV 指向它），03 包被它誤導。
- **教訓與 R-PMH20 同型**：比對兩個值之前，先確認兩邊指的是不是同一個東西。
  這與 03 §3 之 priority 假衝突、02 §3.3 之列號位移推算是同一形狀。
- **對本 feature 效力不變**：母本為交付基底，`design_method_vocabulary`
  9 項維持；四份交付件 996 個 R 欄值**無一用過 `Pair-wise / N-wise`**。

**A-PMH12 —— Phase 6／7 之前置阻斷項**
- (1) priority DV 之 sqref `P10:Q1411` **跨兩欄**，使 `Q`（Estimated Test
  Time）套用 `"P0,P1,P2,P3"` —— **任何分鐘數都會被 Excel 擋下**。
- (2) `AF` 列舉逐字 `"Pass, Fail, Pending,Block,NA"` —— ` Fail` 與
  ` Pending` **含前導空白**；寫 `Fail`（無空格）會被擋下，
  任何 `.strip()` 都會產出無法通過 DV 的值。
- 二者因四份交付件該二欄全空而**從未被實際檢驗過**。已標入 `DECISIONS.md`。

**A-PMH09 → RESOLVED（結論更正）**
- 「衍生自 AMFM **交付件**」**不成立** —— 該件 34 欄、`Cover!D6` = `C`、
  履歷未被覆寫、`D5` 已填。成立者為「帶 AMFM **中繼產物**血緣」。
- **AMFM 交付件乾淨，無須回報**；執行層原提案 (c) 不執行。
- R-PMH23 將客戶那份之**封面五頁**列為禁用。

**狀態**：P0 ✅ / P1 ✅ / **P2 待 Pei 簽核** `DECISIONS.md`。
下一步 Phase 2／3（framework），**無阻斷項**。

**下一包之首要建議**：先確認 R-PMH19 (a) 之「根層」是否為預期範圍
（見上「母體判準之副作用」），再進行 Q3 重裁。詳見上繳 §8（五項）。

## 05 輪要點

**母體 17，非分析層所報之 16 —— 停止條件 7 觸發**
- 候選數亦變動：**32**（04 包為 28）。新增 4 檔為併行 session 於
  `Vehicle Settings/CFTS044/REF/` 產生之寫回前備份，依 (a′) 全部排除，
  **不影響母體**。惟顯示 **`ASW-R2` 是活動目錄** —— 以它為母體之比率，
  其分母會隨他人作業變動。**建議 R-PMH19 之揭露義務補入「量測時點」。**
- 差異歸屬：**分析層補測 5 檔時漏了
  `Engineering Mode/App Team Effort/…_CFTS011_EngMode.xlsx`**。
  它與那 5 檔同樣是被原 (a) 深度規則排除、(a′) 生效後回到母體者。

**Q3 語料再更新 —— `D5` 空 9 / 非空 8**
- 第 17 檔之 `D5` **非空**：`FM-WI-SW-PSCFTS011-ENGM-A01`，**第六種格式**
  （表單／文件編號，既非 037 報告名亦非 CFTS 條目 id）。
- 四次量測之演進：`5/0` → `8/3` → `9/7` → **`9/8`**。
  **`D3`／`D4` 四次皆全空，留空無爭議；變動者只有 `D5`。**
- 分析層 §五稱「母體最大單一群 9/16」，在 17 之母體下為 **9/17** ——
  相對多數由 56% 降為 53%，**（甲）之語料強度較其所述更弱**。
- 八個非空者用**六種格式**，其中**三者指向物不是規格或報告**
  （他 feature 之報告名／本表單編號／另一份文件編號）。
  若只算「填得對」者，分母為 5，而**五者中仍用了四種排列**。

**停止條件 8 觸發一項 —— `_Rebuilt` 之排除理由不成立**
- `Engineering Mode/` 根層有兩份同日期（20260816）檔案：保留者
  `EngeeringMode_20260816`（**211 列，檔名拼錯多一個 e**）、
  排除者 `EngMode_20260816_Rebuilt`（**527 列，2.5 倍**）。
- (c) 之日期規則對兩者無鑑別力（同日），**實際上是 (b) 之字面比對決定取捨，
  而它選中了資料較少且檔名拼錯的那一份**。
- 另 `(done)` 一項：其字面語意為「完成」，與「中間態」相反 ——
  **理由措辭與事實相反，但結論仍成立**（另有 (c) 之獨立依據）。

**17 檔全簿 DV 掃描（依 R-PMH20，量詞即「這 17 檔」）**
- **`AF`／`AG` 前導空白：具該 DV 者 15/15 全部帶前導空白**
  （` Fail`／` Pending`）；另 2 檔無此 DV。
- **x14 source：`Reference!$C$4:$C$12` 10 檔／`下拉選單!$A$1:$A$9` 4 檔／
  `下拉選單!$A$1:$A$11` 2 檔／無 x14 2 檔。**
  **母本所用之 `下拉選單!$A$1:$A$9` 在這 17 檔中是少數（4/17）** ——
  R-PMH25「不以分頁名認 source、取母本自身實測值」因而更有必要：
  **若以多數定 source 會取到 `Reference`。**
- `$A$1:$A$11` 兩檔之 source 範圍含**兩個空值**（分頁只有 9 個非空）。
- **priority DV 跨欄者 7 檔** —— A-PMH12 (1) 之形態非母本獨有。

**`Product Document!B7:C7`**：DV 17/17 全備且逐字相同；值為
`Confidential` **12 檔**、空 **5 檔**，**無一填 `Top Secret`**。
⚠ **母本為空而客戶那份為 `Confidential`** —— 若交付須填，
本 feature 之寫回範圍不只 `Test Case Specification` 分頁（Phase 7 待決）。

**`data/layer3_sections.tsv` —— 48/48 對應規格自身 section id**
- 停止條件 9 未觸發。章分布 7(19)／8(6)／9(5)／10(10)／11(5)／12(3)；
  FROP 12 值與 03 包逐項相符。**不擬 Layer 2 名、不定 granularity。**
- **首版寫出之 TSV 結構是壞的**（自陳）：`section_title` 含實體換行與
  `_x000D_`，未正規化即寫入，一列被拆成多列。**與 A-PMH08 同族** ——
  把有結構的東西當無結構字串處理。修正後**加寫出後之回讀自檢**
  （48 列 × 7 欄），不以「寫出成功」為通過（R-G7-1）。

**`check_write_back.py` 標 `[KNOWN-INCOMPLETE]`**
- 三項檢查已實作且經故意失敗驗證，**但尚未被任何寫回路徑呼叫**；
  接線為 **Phase 6 交付項**。理由逐字：**「一段未被呼叫的正確程式碼，
  其效力與文字修補相同」**（通則 8）。`feature.yaml` 加 `wired: false`。

**待 Pei 三項**：Q3 之 `D5`（語料已備齊）／`_Rebuilt` 何者為交付態／
`App Team Effort` 是交付夾或工作子目錄（決定母體 17 或 16）。
