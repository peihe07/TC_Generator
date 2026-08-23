# INDEX — FW036 Power Moding

執行層於每次上繳時更新（canon §8.7）。分析層不寫此檔。

feature 之交付夾為 `ASW-R2/Disclaimer screen/`（FROP 標籤），
身分為 `Power Moding`（規格標題模組名）—— R-PMH2，Comfort R-C6 同型。

| NN | 日期 | 主題 | 下放 | 上繳 | 新條文 | 新 anomaly | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-22 | 開案：骨架、裁決落檔、Phase 0 intake 實測 | [handoff/01_intake.md](handoff/01_intake.md) | [upstream/01_intake.md](upstream/01_intake.md) | R-PMH1–R-PMH6（分析層，逐字抄錄 6/6 相符） | A-PMH01–A-PMH05 | **步驟 1–8 全數執行；停止條件 2、4 觸發，已停於待裁** |
| 02 | 2026-08-23 | 母本改定、`workbook_state` 改判、Phase 1 前置 | [handoff/02_baseline_switch.md](handoff/02_baseline_switch.md) | [upstream/02_baseline_switch.md](upstream/02_baseline_switch.md) | R-PMH7–R-PMH12（逐字抄錄 6/6 相符） | A-PMH06–A-PMH08；A-PMH01／A-PMH05 → RESOLVED | **步驟 1–10 全數執行；九條停止條件全未觸發** |
| 03 | 2026-08-23 | Test Group 欄值改判、DV 列舉值實測、Phase 1 recon | [handoff/03_testgroup_and_dv.md](handoff/03_testgroup_and_dv.md) ＋ [03a_pei_rulings.md](handoff/03a_pei_rulings.md) | [upstream/03_testgroup_and_dv.md](upstream/03_testgroup_and_dv.md) | R-PMH13–R-PMH18（逐字抄錄 7/7 相符） | A-PMH09、A-PMH10；A-PMH06（附 PENDING-CANON）／A-PMH07 → RESOLVED | **步驟 1–8 全數執行；九條停止條件全未觸發** |

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
