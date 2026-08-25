# 上繳包 10 —— DECISIONS 合併、PROXI 需求驅動、Q2／Q3 材料

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/10_decisions_merge.md`
- 結果：**步驟 1–7 全數執行；二十七條停止條件全未觸發**
- 全部 git 操作屬 Pei —— §9 只備妥訊息與 pathspec，未執行

---

## 1. §四五條之抄錄核對表（步驟 1，腳本產出）

## 抄錄核對表 — 10_decisions_merge.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 34 | R-DM32 | `features/display/RULINGS.md` | 613 | `01ba8faa50dccde9` | 是 |
| 35 | R-DM33 | `features/display/RULINGS.md` | 608 | `f1759422cbd1270f` | 是 |
| 36 | R-DM34 | `features/display/RULINGS.md` | 430 | `ddc83466127deb1a` | 是 |
| — | R-G21 | `docs/fw036/RULINGS_LEDGER.md` | 369 | `27b095bdf3ff9f61` | 是 |
| — | R-G22 | `docs/fw036/RULINGS_LEDGER.md` | 356 | `4aa04c2c9abb9cbe` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **36** 個，與各下放包原檔逐字元比對 **全數相符**（36 vs 36）。

`RULINGS.md` 之「廢止與取代之對照」表已補一列：PROXI 之供給側對照
（keyword／heading／ETM 三種嘗試）由 **R-DM33** 取代為需求驅動。

---

## 2. 合併後之 `DECISIONS.md`（步驟 2）

### 2.1 標記齊備性 —— 停止條件 26 **未觸發**

§1–§7 之全部項目行逐行機器檢查（正規式
`\[(AUTO|PROPOSED|PEI|RULED)`）：**未標記者 0**。

合併前有三項未帶標記，已於本次補標並各自說明：

| 項 | 原狀 | 補標後 |
|---|---|---|
| `Ambiguous rows` | 「無」 | `[AUTO]`（**相符** —— recon `[]`／自測 無） |
| `Draft-region disposition` | 「不適用」 | `[AUTO]`（recon done/draft 皆 0，相符） |
| `Parent/child both-leaf duplications` | **「未實測」** | `[AUTO]` → 無。**自「未實測」升為已判定** |

第三項值得記：我原本標「未實測」，理由是 037 之 8 筆皆為 leaf、
無父子結構可測。recon 之 `parent_child_dupes: []` 加上其
`id-suffix criterion: not applicable`（無 leaf id 帶 `-NN` 子尾綴）
與該理由一致 —— **這是交叉檢查把一個「未實測」變成「已判定」的一例**。

### 2.2 `[AUTO]` 之來源自此分兩類

合併後各 `[AUTO]` 項逐項標明其來源：**（recon）**／**（自測）**／
**（相符）**。檔頭已載明此約定。

```markdown
## 1. Intake

- spec_mode: `[AUTO]`（**相符** —— recon `[AUTO] D`／自測 D）→ **D**（CFTS/Word 為判讀基準，
  spec_reference 為查得而非構造）。實測支持見上繳 §8：CFTS 可抽 outline id
  184 相異／182 由標題可達；SYS2 無指向 CFTS 條號之錨；SYS3 標題可達
  outline id 僅 1
- spec text layer: `[AUTO]`（recon）→ **854,333 chars（pymupdf）**。
  自測之 python-docx（段落＋表格格，正規化後）為 907,382；**兩數皆已重現**，
  差異為抽取器不同而非計算錯誤。登記值取 recon 之探針（下放包 10 §2.1），
  自測值保留於 `probe_spec_mode` 之 sidecar。兩者皆遠超「有無文字層」之
  500 字元門檻，導出之結論相同（spec_mode D 成立）
- Source files present: `[AUTO]`（**相符** —— recon 報 5 present）→ 4 份，逐份 SHA256 見
  `data/materials_ledger.tsv`；`shasum -c` 4/4 OK。另 036 母本
  （R-G1）`6372fb6b…825b2`
- Missing referenced specs: `[AUTO]` → **CFTS_009**（CFTS_020 以
  `{CFTS009-722}` 引用，定義 Splash/Disclaimer 時段）→ DR-DM1，
  影響 SWE-DM-003
- Spec release/version pinned: `[AUTO]` → CFTS_020 檔名版次
  `20260310-1533`；SYS2 `20260616 All_HW_System Accepted & Released`；
  037 `FM-WI-FSM-037-A03`；SYS3 `v1.0`

## 2. Workbook survey

- workbook_state: `[AUTO]`（**相符** —— recon `BLANK`／自測 `BLANK`）
  → **BLANK**（1402 資料列中 filled = 0）
- Form layout revision: `[AUTO]`（recon）→ **C (has Estimated Test Time)**
  —— 自測未判定版面 revision，本項為 recon 所增
- Header row index: `[AUTO]`（**相符**）→ **r9**，分頁
  `Test Case Specification 測試用例規範`（模板宣告之分頁名不存在，A-DM7）
- Column mapping: `[AUTO]`（**相符** —— recon 自表頭解出 15 欄，逐鍵與
  自測相同：D/G/H/I/J/K/L/M/N/O/P/R/S/AA/AH）→ 模板基準 **12/15**、
  生效基準 **15/15**；不符 3 鍵已依實測更正
  （`design_method` Q→R、`functional_safety` R→S、`author` Z→AA）。
  recon 另解出 `estimated_test_time = Q`，依 **R-DM34(a)** 為版面
  revision 標記而非管線欄位，**不加入 `workbook.columns`、寫回不觸碰**
- `feature.yaml` column conflicts: `[AUTO]`（recon）→ **none**
  （即生效欄位表與表頭解析一致）
- Done-region segments: `[AUTO]` → 無（BLANK）
- Regen-region segments: `[AUTO]` → 全表（r10 起）
- Ambiguous rows: `[AUTO]`（**相符** —— recon `[]`／自測 無）→ 無
- Draft-region disposition: `[AUTO]` → 不適用（無 draft 列；
  recon 之 done/draft 皆 0，**相符**）
- Design-method vocabulary: `[AUTO]`（**相符** —— recon 9 條／自測 9 條
  逐字相同）→ `下拉選單` 分頁 9 個值，全文見上繳
  §6.4。R 欄之 DV 為 x14 擴充，openpyxl 不可見（R-G1）

## 3. Coverage

- 037 leaf count: `[AUTO]`（**相符** —— recon 8／自測 8，leaf id 全集
  逐項相同）→ **8**（`SWE-DM-001`…`008`，皆 `Functional Requirement`）
- Categorization 欄與分布: `[AUTO]`（**相符** —— recon 欄 F、
  `{'Functional Requirement': 8}`；自測第 6 欄 = F、同分布）
- Safety attributes (ASIL/FTTI): `[PROPOSED]`（recon 所增）→ 受裁之來源
  不帶 ASIL／FTTI 欄，故 SYS2／SYSRA 之安全層**不進入追溯鏈**。
  自測未測此項
- Covered by done region: `[AUTO]` → 0（無 done region）
- Regen targets: `[AUTO]` → 8 leaf 全數
- Leaves covered nowhere: `[AUTO]`（**相符**）→ 8 = 全部 leaf。
  recon 之措辭為「expected under BLANK, not an anomaly；此為 Phase 4 之
  工作清單而非缺口」，與自測之「不適用（無既有工作簿內容）」語意相同
- Parent/child both-leaf duplications: `[AUTO]`（recon `parent_child_dupes:
  []`）→ 無。自測原標「未實測」，理由為 037 之 8 筆皆為 leaf 且
  `Categorization` 無 `Heading`，無父子結構可測。
  recon 另報 `id-suffix criterion: not applicable`（無 leaf id 帶 `-NN`
  子尾綴），與該理由一致 —— **本項自「未實測」升為 `[AUTO]` 無**
- SYS2 覆蓋落差（R-DM7／R-DM13）: `[AUTO]` → **原「58 列無對應」已撤回**
  （A-DM11，方法由 R-DM13 廢止）。改以錨定法：母體 80 列，anchor_kind 為
  signal 43／heading 36／value 1／melco 0／none 0；`candidate_leaf` 僅
  `SWE-DM-004`／`005` 各 4 列（r31–r34，heading 錨逐字含 `'Hot Algorithm'`），
  其餘 76 列無候選。全表見 `data/coverage_sys2_vs_swe_dm.tsv`；
  舊表保留於 `…RETRACTED.tsv`。
  **唯一站得住之覆蓋陳述為「以 id 為據之對應 0 列」（A-DM2）。**
  引用 `candidate_leaf` 須連同 `anchor_kind`（R-DM12）
```

（§4–§7 與待裁清單見檔案全文，本節只列合併改動最集中之 §1–§3。）

---

## 3. 分歧處置表（步驟 2）

### 分歧處置表

| # | 項 | `DECISIONS.new.md`（recon） | 本檔（權威） | 處置與理由 |
|---|---|---|---|---|
| 1 | `spec_reference` | `[PROPOSED: None]` | **`[PEI]`** | **維持 `[PEI]`，拒絕降格**。recon 之值係依 `spec_reference_template` 為 null 之機械讀出；本檔之 `[PEI]` 係因 mode D 要求查得而 leaf → CFTS 條號無 id 橋樑（A-DM10b），**無法提案**。`[PROPOSED]` 未經修改即生效，會使該項在簽核時無聲通過（R-DM32） |
| 2 | spec text layer 字元數 | `854333 chars (via pymupdf)` | 採 **854,333**，並列自測之 907,382 | 依下放包 10 §2.1：登記值取管線探針以維持跨 feature 可比性；兩數皆已重現、差異為抽取器不同；兩者皆遠超 500 字元門檻，**導出之結論相同** |
| 3 | safety attributes | `[PROPOSED: 無 ASIL/FTTI，安全層不入追溯鏈]` | 以 `[PROPOSED]` 併入 | recon 所增而自測未測之項，依 R-DM32 反向規定**不自動升格為 `[PEI]`** |
| 4 | batch plan | `[PROPOSED: 依 spec chapter 分組]` | 以 `[PROPOSED]` 併入 | 同上 |
| 5 | 版面 revision | `[AUTO] C` | 以 `[AUTO]`（recon）併入 | 自測未判定版面 revision；此為 recon 多測出之事實 |
| 6 | `estimated_test_time` | 解出 `= Q` | **不入 `workbook.columns`** | 依 **R-DM34(a)**：為版面 revision 標記而非管線欄位，地位同 B 欄（公式欄，R-DM15）—— 存在、被辨識、不被寫入 |
| 7 | 欄位對應之計數 | `15 fields resolved` | 模板基準 12/15、生效基準 15/15 | 非分歧：兩者之 `declared` 基準不同（A-DM7）。recon 之 15 對應本檔之生效基準 |
| 8 | covered nowhere | `8 = all leaves — expected under BLANK` | 語意相同，措辭併入 | 非分歧 |
| 9 | parent/child dupes | `[]` | 自「未實測」升為 `[AUTO]` 無 | recon 之 `id-suffix criterion: not applicable` 與自測之理由一致，該項已可判定 |

### 3.1 第 1 項是本輪最重要的一次拒絕

`spec_reference`：recon 標 `[PROPOSED: None]`，本檔維持 **`[PEI]`**。

兩者不矛盾但**地位不同**：recon 之值是「`spec_reference_template`
為 null」之機械讀出；`[PEI]` 是「mode D 要求查得，而 leaf → CFTS 條號
之橋樑不存在（A-DM10b），**故無法提案**」。

依 canon §4，`[PROPOSED]` 未經修改即生效 —— 若接受降格，
一個**無法提案**之項會在簽核時無聲通過。已依 R-DM32 拒絕。

反向亦已落實：recon 所增而自測未有之三項（safety attributes、
batch plan、版面 revision）一律以 `[PROPOSED]`／`[AUTO]` 併入，
**未自動升格為 `[PEI]`**。

---

## 4. 字元數處置與 A-DM26（步驟 3）

### 4.1 登記值

| 抽取器 | 字元數 | 登記 |
|---|---|---|
| pymupdf（`recon.py` 之管線探針） | **854,333** | **Y** |
| python-docx（段落＋表格格，正規化後） | 907,382 | N（保留） |
| python-docx（未正規化、含空段） | 910,850 | N（保留） |

三數皆已由執行層重現。差異為抽取器不同而非計算錯誤。
登記值取管線探針，理由依下放包 10 §2.1（用途為判斷有無文字層，
門檻 500 字元；三數皆遠超，**導出之結論相同**；跨 feature 可比性）。

自測值**未作廢**，與登記值並列於新建之 `data/spec_text_layer.tsv`
及其 sidecar 之 `measurement_conditions`。

> `probe_spec_mode.py` 原本**只印不寫檔**，沒有 sidecar 可掛。
> 故本輪新建該資料檔，使兩個數字與其成因有一個可被引用的落點 ——
> 否則「兩數並列」只會存在於一次性的終端輸出裡。

### 4.2 A-DM26 全文

```markdown
## A-DM26 — `paths.spec_pdf` 指向 `.docx`；欄名與內容不符  [PENDING]

`feature.yaml` 之欄位名為 `paths.spec_pdf`，而本 feature 之該欄指向
`R1LR_…CFTS_020 ICS and DCSD _20260310-1533.docx` —— **一份 Word 檔，
不是 PDF**。`recon.py` 之 `survey_spec_text_layer()` 其 docstring 亦以
PDF 為前提（其探針依序試 pymupdf 與 `pdftotext`）。

實際上探針對 `.docx` 可用（pymupdf 讀得 854,333 字元），故**功能無誤**，
誤導的是名稱。

- **不改欄名**（會動到所有 feature 之 `feature.yaml` 與所有讀取者）
- 引用該欄時須知其內容未必為 PDF
- 連帶記明字元數之兩個值：pymupdf **854,333**（登記值）／
  python-docx **907,382**（自測，保留）。兩者皆遠超「有無文字層」之
  500 字元門檻，**導出之結論相同**（spec_mode D 成立）。
  全表見 `data/spec_text_layer.tsv`
- 提案處置：登記。欄名之修正屬全域 Tier 2
```

---

## 5. PROXI 之 R-DM33 處理（步驟 4）

### 5.1 `related_leaf` 停止填寫

```
## anchor_kind 分布
  leaf_phrase: 0
  glossary_phrase: 0
  glossary_phrase_norm: 1
  cfts_usage: 1
  proxi_param: 175
  none: 269
  合計 446

  R-DM33：`related_leaf` 自本輪起不由供給側填寫，故全 446 列皆空，語意一律為 R-DM23 之 **(2) 未追查**。
  錨仍照跑，其結果留在 `note` 欄（本輪 anchor_kind 非 none 者 177 列），供 Phase 2 逐 leaf 查前置條件時參考。

  於 PROXI Format 逐字查得定義者: 177/446
  keyword 命中（僅揭露）: 23
```

- `related_leaf` **非空列數：0**（改動前為 1）
- 全 446 列之語意一律標 R-DM23 之 **(2) 未追查**，並註明
  「R-DM33 起本欄不由供給側填寫；leaf 需要前置條件時再逐一查 PROXI」
- **錨仍照跑**：`anchor_kind` 非 `none` 者 177 列，其結果留在 `note` 欄。
  已量測的東西一項都沒丟掉，只是不再被寫進一個宣稱「這列連到哪個 leaf」
  的欄位
- sidecar 已加註 R-DM33，`rulings` 欄加入該條號

### 5.2 提案撤回

`docs/proxi_triage_proposal.md` 檔首加註全文撤回（引 R-DM33 與其理由），
原文依 R-TM13 保留。`docs/INDEX.md` 已標其為 SUPERSEDED。

> 撤回的是**方法**，不是**已查得的事實**：`DCSD_cfg` → PROXI r37、
> `RVC_SK_PRSNT` → r401／r494、`Splashscreen_Type` → r597 三個線索
> 仍在 `proxi_candidates.tsv` 之 `note` 欄，供 Phase 2 逐 leaf 查前置
> 條件時優先查證。它們**不因此取得 Pre-Condition 之資格**（§8.5）。

---

## 6. `feature.yaml` 之 Q 欄／B 欄註記（步驟 5）

```yaml
  # R-DM34(a)：Q 欄 `Estimated Test Time (mins)` 為版面 revision 標記
  # （有此欄 = rev C），**非管線欄位**。recon.py 會解出 estimated_test_time=Q，
  # 但本表不列它，寫回一律不觸碰。
  #
  # 「辨識但不寫入」之欄共兩個，理由不同，故分列：
  #   B 欄  公式欄（R-DM15）—— 賦值會摧毀 1402 列之 =IF(ISBLANK($D…))
  #   Q 欄  版面標記（R-DM34(a)）—— 賦值會把一個 revision 判準變成資料
```

兩者之理由分列而非合併：B 欄之風險是**摧毀既有內容**，
Q 欄之風險是**把判準變成資料**。混寫會使下一個人以為只有一種顧慮。

---

## 7. `Q2_Q3_briefing.md`（步驟 6，本輪主要交付）

全文見 `features/display/docs/Q2_Q3_briefing.md`。結構與要點：

### 7.1 Q2

- 037 之 8 leaf 全集與 Sub Categorization（recon 與自測兩側逐 id 相符）
- SYS2 FR 母體 **80** 列；另附一項已驗事實：`_polarion` 字典列有
  `Non Functional Requirement` 而主表使用該值之列數為 **0**，
  即 **80 之母體未遺漏 NFR**
- 連結現況：**id 層級 0 列**／heading 錨 4 列（004、005）／
  glossary 錨 12 列（007、008）／glossary_norm 0 列／**無候選 64 列**
- **64 列之語意逐字寫明為 R-DM23 之 (3) 方法之界線**，並列出三種語意
  在本 feature 各自之實例，載明「不等於不屬於本 feature 之範圍」
- 001／002／003／006 候選為 0 之**成因為「無逐字錨」**，
  並附已量測之佐證（含 `DISPLAY_ON` vs `DISP_ON` 之無並列出處）；
  「是否有語意對應列」逐字標 **未量測**
- 選項 A／B 之交付形態與已知代價各自列出，**不含偏好**

### 7.2 Q3

| 分頁 | `SWE-DM-nnn` | `SWE1-DM-nnn` |
|---|---|---|
| `SWE1 Requirements`（需求本體） | **8** | 0 |
| `SYS2 Traceability`（衍生索引） | 0 | **8** |
| `Excluded NRLs (HW-only)` | 0 | 0 |

**兩種寫法在 SYS2／CFTS_020／SYS3 三份素材中皆為 0 次** ——
外部素材對此無偏好可言。此為本輪新測。

另載：D 欄為落點、B 欄之編號公式以 D 欄為條件、TestRail 之 E／F 欄
不受影響；**TestRail／上游是否對形態有既定要求 → 四份素材中無此資訊**。
並記明 **A-DM1 不因裁定而結案**（它記的是上游文件內部不一致）。

### 7.3 停止條件 27 之落實

briefing 末節列 **6 項未涵蓋者**，逐項標「未查證／未量測／非量測問題」，
無一處以推論填補。

### 7.4 撰寫時自查出兩處數字錯誤

依 R-G22，briefing 中之斷言以腳本覆核，查出兩處並更正：

| 處 | 初稿 | 更正 |
|---|---|---|
| r72 底下之 FR 列數 | 同一句內先寫 45 後寫 48 | **48**（機器覆核） |
| `SW` 分類列 | 「r245–r249 五列與 leaf 無連結」 | **7 列（r17／r18／r245–r249）之 `candidate_from` 全部為空** |

第一處是同一句話裡自相矛盾的兩個數字 —— 若沒跑覆核，
它會以一個看起來很具體的形式留在給 Pei 的材料裡。

---

## 8. 「本包是否仍有該驗而未驗者」—— 執行層之獨立判斷

**有，共 5 項。**

1. **`DECISIONS.new.md` 保留但無條文規定其失效時機。** R-DM32 定了
   權威關係，但沒定「下次 recon 重跑時，舊的 `.new.md` 怎麼辦」。
   現在它是一份**帶時間戳的證據**，而檔名看起來像一份待處理的草稿。
2. **合併後之 `DECISIONS.md` 未經 recon 再次比對。** 我依 `.new.md`
   合併，但沒有重跑 recon 去驗證合併後之檔仍與管線一致 ——
   **合併這個動作本身沒有被交叉檢查。**
3. **`spec_text_layer.tsv` 是我新建的檔，不由任何腳本產生。**
   下次有人改了抽取器，這三個數字不會自動更新，而 sidecar 之
   `generated_by` 寫的是「人工登記」。它會過期而不出聲。
4. **Q2 briefing 之「未量測」六項全部仍未量測。** 材料備齊不等於
   問題可答；其中第 1、2 項（64 列是否在範圍外、四個 leaf 是否有
   語意對應）**在現行逐字錨之限制下不可量測**，這一點 briefing 有寫，
   但沒有寫「那要怎麼辦」。
5. **PROXI 改需求驅動後，177 列已查得之值域無人維護。**
   `proxi_candidates.tsv` 保留為索引，但 PROXI 檔若換版，
   沒有任何檢查會發現該索引過期（`feature.yaml` 之 `reference:`
   綁了 sha256，但沒有腳本在比對它）。

另記本輪**已驗而下放包未要求**者：briefing 之兩處數字自查（§7.4）；
`SWE-DM-`／`SWE1-DM-` 在 SYS2／CFTS／SYS3 三份素材中皆 0 次之量測；
合併後 `DECISIONS.md` 之標記齊備性機器掃描。

---

## 9. 建議之 commit 訊息與 pathspec（**未執行**）

```
docs(display): merge DECISIONS, demand-driven PROXI, Q2/Q3 briefing

- R-DM32/33/34 + R-G21/R-G22 verbatim (5/5, 36/36 cumulative)
- DECISIONS.md merged from DECISIONS.new.md, 9 divergences each with a
  disposition and a reason. spec_reference stays [PEI]: recon's
  [PROPOSED: None] would let an item that cannot be proposed pass
  sign-off untouched. Every item in sections 1-7 now carries a marker;
  three that had none were classified, one of them promoted from
  '未實測' to [AUTO] because the cross-check settled it
- spec text layer registered as 854,333 (pymupdf pipeline probe); the
  self-measured 907,382 kept alongside in data/spec_text_layer.tsv, a
  new file because probe_spec_mode.py only ever printed
- A-DM26: paths.spec_pdf points at a .docx in this feature
- R-DM33: PROXI goes demand-driven. related_leaf is no longer filled
  from the supply side (0 of 446), the anchors still run and their
  results stay in note. proxi_triage_proposal.md retracted, text kept
- feature.yaml records column B and column Q as recognised-but-never-
  written, with their two different reasons
- Q2_Q3_briefing.md: measured facts only, six gaps each marked
  未查證/未量測. Two figures in my own draft were wrong and were caught
  by re-running the checks (48 not 45; 7 SW rows not 5)
```

pathspec：

```
git add docs/fw036/RULINGS_LEDGER.md \
        features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/DECISIONS.md \
        features/display/feature.yaml \
        features/display/scripts/ \
        features/display/data/ \
        features/display/docs/
```

本輪**未動共用 `scripts/`**、未動 `forms/`、未動 `.gitignore`。
`DECISIONS.new.md` 已於上輪入版，本輪不改其內容。
