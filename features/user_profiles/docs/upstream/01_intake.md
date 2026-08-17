# 01 上繳包 — User Profiles Phase 0（執行層，2026-08-17）

對應下放包：`docs/handoff/01_intake.md`、`01a_rulings.md`、`01b_tasks.md`
規則授權：`docs/fw036/FEATURE_ONBOARDING.md`（程序）、
`docs/runtime/ASPICE_SWE6_AI_Instruction.md`（TC 內容）；
衝突時 `01a_rulings.md` 之本 feature 條文優先。

**結論一句話**：作業項 1、2 完成；作業項 4 之 spec 側完成且與下放包完全相符；
**作業項 3 停下**（兩個互相獨立的阻擋：037 不在 repo、預期值單位不一致）；
作業項 5 只出 spec 單邊草案（037 側交集不可取）；作業項 6 即本檔。
git 全程未執行。

---

## 0. 量測條件總則（canon §5a）

凡本檔之數字，除另註明外一律適用：

| 項 | 條件 |
|---|---|
| 列號 | **實體列號**（工作表列號），非 tc_id 尾碼 |
| 計數 | **逐列**；凡逐引用者另行標明「逐引用」 |
| 字元數 | Python `len()`，即 **UTF-8 code point 數**，非 byte 數 |
| 檔案雜湊 | `shasum -a 256`，對**整個檔案位元組流**，非工作表內容雜湊 |
| 檔案大小 | bytes（`stat -f %z`）|
| 大小寫 | 檔名搜尋**不敏感**（`find -iname`）；欄位表頭比對**不敏感**（`norm()` 小寫化）；PU id 抽取實測**敏感與不敏感結果相同** |
| 詞界 | PU id 抽取使用 `PU[\s_]?(\d{3,4})`，**無 `\b` 詞界**（見 §4.3 之自曝缺陷）|
| spec 掃描欄位 | `Basic Report` 之 `ID`／`Outline Number`／`Description`／`SYSRE_HMI_Source ID` 四欄，**以表頭文字定位，非欄位置** |
| 036 掃描欄位 | `Test Case Specification 測試用例規範` 之 **A–AH 全 34 欄** |

---

## 1. 作業項 1 — Scaffold ✅ 完成

`python3 scripts/new_feature.py User_Profiles --adopt-existing`

- `docs/handoff/` 三份下放包檔案**未被刪除、未被覆寫**（腳本之
  `--adopt-existing` 對既存檔一律 skip；執行後逐一確認三檔仍在）。
- 建立之目錄：`inputs/ data/ batches/ generated/ scripts/ docs/`
- 建立之檔案：`RUNBOOK.md ANOMALIES.md RULINGS.md DATA_REQUESTS.md
  DECISIONS.md feature.yaml PLAYBOOK.md .gitignore`
- **播種**：
  - `RULINGS.md` ← `01a_rulings.md`，R-G1／R-G2／R-U1～R-U7 **逐字照錄**
    （R-G1／R-G2 標為全域條文於本包首次落檔），另附執行層回報段落。
  - `ANOMALIES.md` ← `01_intake.md` §Anomalies，A-UP01～A-UP03。
    **marker 前綴改為 `A-UP`**：scaffold 骨架由 feature 名前兩字取得 `A-US`，
    與下放包之 `A-UP` 不符；以下放包為準。
- `feature.yaml` 已填（見 §2.4），**scaffold 之預設欄位字母為 rev A/B 版面，
  與本 feature 之 rev C 母本不符，已全部改為實測值**。

---

## 2. 作業項 2 — R-G1／R-G2／R-U7 form 處置 ✅ 完成

### 2.1 硬約束之遵守聲明

| 約束 | 狀態 | 證據 |
|---|---|---|
| 歸檔一律用 `mv`，不得用 `rm`（R-G2）| **遵守** | 本輪對 `forms/` 之唯一寫入操作為 `mkdir -p archive/forms_superseded` 與三次 `mv`；三檔移後皆存在於新位置且 SHA 未變 |
| 036 母本不得覆寫（R16/R18-3）| **遵守** | 母本僅被 `openpyxl.load_workbook()` 讀取與 `zipfile` 唯讀開啟；母本 SHA 於探測前後一致（`6372fb6b…`）|
| openpyxl save 全 repo 禁用 | **遵守** | 本輪未在任何腳本或指令中出現 `.save(`；`build_outline_map.py` 只讀 spec、只寫 `.tsv`／`.json` |

### 2.2 四份 036 檔之 SHA256 —— 移前 vs 移後

量測條件：`shasum -a 256`，整檔位元組流；移動前後各執行一次。

| 檔 | 移前 SHA256 | 移後 SHA256 | 一致 | bytes | mtime | 現位置 |
|---|---|---|---|---|---|---|
| `…_SWQT_20260121.xlsx` | `cd876c202c71e74b0eca92dd7b4454af1879ac9a700744d5fe448687f7a9287d` | 同左 | ✅ | 65,823 | 2026-08-09 22:21:38 | `archive/forms_superseded/` |
| `…_SWQT_20260816_ext.xlsx` | `4b3d447051f914eb41cc9754abaa5ed89bc0f06251baf01681a18bf884b6bcf7` | 同左 | ✅ | 200,654 | 2026-08-17 09:45:54 | `archive/forms_superseded/` |
| `…_SWQT_Home_20260809.xlsx` | `1895fb2a2b44f06c46147e5c24731d2d1adf0f2eea80c7ec6f8900a679f24d72` | 同左 | ✅ | 119,885 | 2026-08-09 22:22:37 | `archive/forms_superseded/` |
| **`…_SWQT_20260817_ext.xlsx`（母本）** | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` | 未移動 | — | 200,650 | 2026-08-17 09:46:09 | **`forms/`** |

`forms/` 移後內容：母本 1 檔 ＋ `FORMS.md` ＋ `.gitkeep`。**符合 R-G2**。

### 2.3 預期值對照 —— 與 FORMS.md 既有記載

| 項 | FORMS.md 原記載 | 實測 | 判定 |
|---|---|---|---|
| `20260121` SHA256 | `cd876c20…` | `cd876c20…` | ✅ 相符 |
| `Home_20260809` SHA256 | `1895fb2a…` | `1895fb2a…` | ✅ 相符 |
| `20260816_ext` SHA256 | `6d53056e…` | **`4b3d4470…`** | ❌ **不符** |
| `20260816_ext` bytes | 123,717 | **200,654** | ❌ **不符** |
| `20260816_ext` B 欄公式範圍 | row 10–**601** | **row 10–1411** | ❌ **不符** |

**不符三項為同一件事**：A-UP03 所報之脫鉤已確認，且比下放包所述更深 ——
不只雜湊與大小不符，**結構容量亦不同（601 vs 1411）**，即磁碟上那份不是
FORMS.md 所描述的那份檔。原 123,717-byte 檔在 repo 內已不存在，xlsx 未入
git，無從還原。**不自行調和**：FORMS.md 之該條目已改為「原記載 vs 實測」
雙欄並列，原記載保留為歷史，並標明「本節結構數值之量測對象已不存在」。
成因未查明，另開 **A-UP05**（Tier 2）。

### 2.4 母本結構探測（R-U7 點名之六項，全部完成）

母本：`forms/…_SWQT_20260817_ext.xlsx`（`6372fb6b…`，200,650 bytes，
zip members 48）。以下全部為 2026-08-17 唯讀實測，完整表格已寫入
`forms/FORMS.md` §`…_SWQT_20260817_ext.xlsx`。

| R-U7 點名項 | 實測結果 |
|---|---|
| sheet 名 | **9 個**：`Cover_old`／`ChangeHistory_old`／`Cover 封面`／`ChangeHistory 修訂履歷`／`Product Document 記錄封面頁`／**`Test Case Specification 測試用例規範`**／`Reference`／`QS Suggestion`／`下拉選單`。`Test Case Framework` 分頁 **absent** |
| header row | **9**（33 個非空表頭格，A 欄無表頭）；資料列起點 **10** |
| A–AH 欄位對映 | **34 欄全部命中**，逐欄見 §2.5。版面 = **revision C**（`ChangeHistory` A/B/**C 2026-01-21**；表單 id 格 `AH5` = `FM-WI-FSM-036-A01`）|
| B 欄公式範圍 | **`B10`–`B1411`**，連續無斷點，1402 格；式樣 `=IF(ISBLANK($D10),"",ROW()-9)` |
| P/R/T–Z/AF 之 DV 範圍 | P：`P10:Q1411`（`"P0,P1,P2,P3"`）／**R：`R10:R1411`（`下拉選單!$A$1:$A$9`，x14 擴充）**／T–Z：`T10:Z1411`（`"0,1"`）／AF：`AF10:AF1411`（`"Pass, Fail, Pending,Block,NA"`）|
| 下拉選單詞彙 9 條 | **9 條逐字命中**（工作表 dimensions 為 `A1:A11`，但 A10／A11 為空；DV 來源已為 `$A$1:$A$9`，不含空選項）|

**未預期之發現（下放包未涵蓋，執行時撞到）**：

1. **R 欄之 DV 是 x14 擴充，openpyxl 讀取即丟棄。** openpyxl 開檔時發出
   `Data Validation extension is not supported and will be removed`，
   `ws.data_validations` 只回 3 條（P／T–Z／AF），R 欄不在其中；其範圍係自
   `xl/worksheets/sheet6.xml` 之 `<x14:dataValidation>` 直接讀出。
   **已以複本實測確認（非推論）**：於 scratchpad（**repo 外**，母本與
   `inputs/` 複本皆未被寫入）對母本之一份複本執行
   `load_workbook()` → `save()`，前後比對 `xl/worksheets/sheet6.xml`：

   | 項 | 存回前 | 存回後 |
   |---|---|---|
   | `<x14:dataValidation>` 節點數 | **1** | **0** |
   | 其 `<xm:sqref>` | `R10:R1411` | **（無）** |
   | legacy DV（P／T–Z／AF）| 3 | 3（**存活**）|
   | zip members | **48** | **47** |
   | 工作表數 | 9 | 9 |
   | B 欄公式末列 | 1411 | 1411 |

   **即：openpyxl 存回會摧毀 R 欄 design_method 下拉，而 P／T–Z／AF 三條
   legacy DV 存活** —— 缺陷是選擇性的，只掉 x14 那一條，
   且 zip member 數只少 1，**表面上像是無害的重新封裝**。
   這是 R16/R18-3 之外**第二個獨立**的禁止覆寫理由，已寫入 `FORMS.md`、
   `FEATURE_ONBOARDING.md` §0 與 `feature.yaml`（`forbid_openpyxl_save: true`），
   並登記為 **A-UP09**（Phase 6 寫回實作之硬約束）。
   母本 SHA 於實測前後一致（`6372fb6b…`）。
   （此項原列為 §8.2 之自認缺口，本輪已補實測 —— canon §5a 第 11 條明文
   「必須以複本實測」，故不以「禁用 save」為由跳過。）
2. **`20260817_ext` 與磁碟上之 `20260816_ext` 逐格差異 0。** 逐格比對
   34 欄 × 1411 列 = **47,974 格**（含公式字串），差異 **0 格**；工作表名稱
   與順序相同、dimensions 兩版皆 `A1:AH1411`、B 欄公式末列皆 1411、
   三條 legacy DV 範圍相同、zip members 48 = 48。差異僅 2 個 zip member：
   `xl/workbook.xml`（Excel `documentId` GUID）與 `docProps/core.xml`
   （`dcterms:modified` 01:45:54Z → 01:46:09Z，相隔 **15 秒**），
   合計 4 bytes。**即新母本是舊檔之一次「另存新檔」，無任何結構或內容變更。**
   意義：R-G1 換母本這件事，就工作簿內容而言是零變更；真正的容量擴充發生在
   更早（相對於 rev C 原範本 `20260121` 之 row 10–59）。
3. **workbook_state = BLANK 已獨立實測佐證 R-U6**：資料區（row ≥ 10）
   除 B 欄公式外之非空格 **0 格**（掃描 A–AH 全 34 欄）；
   Test Item(`I`) 或 Test Case ID(`F`) 非空之列 **0 列**。
   `D5`（範圍 Scope）之值格為**空**（`C5` 標籤 `範圍 Scope：` 存在）——
   即本母本不帶 Home／AMFM 兩例之 Scope 誤值（A-H26 型缺陷不繼承）。
4. **歸檔後之三檔目前不在任何 `BASELINE.sha256` 涵蓋範圍內。** Comfort 之
   baseline 涵蓋的是 `features/comfort/inputs/` 內之另一份 `20260121` 複本
   （同 SHA），非 `forms/` 這一份。故 R-U6 所倚賴之 style authority
   （Home 225 列工作簿）之雜湊目前**只記於 `forms/FORMS.md`**。
   R-G2 之理由段正是為保住此檔而寫，但保住檔案與保住雜湊是兩件事。
   **提議（Tier 2，不自裁）**：於 `archive/forms_superseded/` 建一份
   `BASELINE.sha256`，或將三檔納入某 feature 之 baseline。本輪未建。

### 2.5 母本欄位對映（表頭列 9 實測，rev C）

| Field | Col | Field | Col | Field | Col |
|---|---|---|---|---|---|
| No.# 序號 | B | priority | P | test_version | AB |
| req_id (Polarion) | C | **Estimated Test Time** | **Q** | test_vehicle (Bench) | AC |
| req_id | D | design_method | R | test_period | AD |
| tc_id (TestRail) | E | functional_safety | S | tester | AE |
| tc_id | F | 車型 ×7 | T–Z | test_result | AF |
| test_group | G | author | AA | defect_id | AG |
| test_set | H | | | remarks | AH |
| test_item | I | | | | |
| pre_conditions | J | | | | |
| input_test_data | K | | | | |
| test_procedure | L | | | | |
| expected_result | M | | | | |
| spec_reference | N | | | | |
| tc_ref_id | O | | | | |

車型 7 欄（T–Z）順序與 rev A/B 相同：HDCC27 Atl-Hi／DT27 Atl-Hi／
VF(ProMaster)637 Atl-Mi／Commander (598) Atl-Mi／Regengade (5210) Atl-Mi／
Toro(2261) Atl-Mi／Fastack (376) Atl-Mi。

**與 rev A/B 之差異僅 Q 欄插入**，其後各欄整體右移一格
（design_method Q→**R**、functional_safety R→**S**、author Z→**AA**、
remarks AG→**AH**）。**scaffold 之 `feature.yaml` 預設值為 rev A/B 版面**
（`design_method: Q`、`author: Z`），若不改即為錯欄寫入 —— 已全部改為實測值。

### 2.6 FORMS.md 之更新（條目不刪）

- 新增 §「036 母本條文（R-G1／R-G2）」，兩條**逐字**照錄 ＋ 四檔 SHA 表。
- `Revision C — 20260121` 條目：File 路徑改指 `archive/forms_superseded/`，
  註明「已非母本」，SHA 標「歸檔前後各實測一次，一致」。**條目未刪。**
- `Revision A/B — Home_20260809` 條目：同上，並照錄 R-G2 之理由
  （style authority 唯一載體）。**條目未刪。**
- `20260816_ext` 條目：加 A-UP03／A-UP05 警示框 ＋ 原記載 vs 實測雙欄表。
  **條目未刪。**
- 新增 §`…_SWQT_20260817_ext.xlsx` —— 現行母本之完整結構探測（§2.4／§2.5
  之全部內容 ＋ 逐格比對結果 ＋ 9 條詞彙逐字）。
- R-G1 亦寫入 `docs/fw036/FEATURE_ONBOARDING.md` §0 Tier 0 條列（條文要求）。

### 2.7 母本複本與 BASELINE.sha256

- 複本：`features/user_profiles/inputs/…_SWQT_20260817_ext.xlsx`，
  SHA 與母本**逐字相同**（`6372fb6b…`）→ `cp` 未改變內容。
- `features/user_profiles/BASELINE.sha256` 已建，**4 筆**：

| 檔 | SHA256 |
|---|---|
| `inputs/…_SWQT_20260817_ext.xlsx` | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |
| `../../spec-index/cache/…(February_10_2023).xlsx` | `368d5874aa23e49c007251ece84de8901f873a7f51ab09b788122b164d365b05` |
| `../../spec-index/cache/…(February_10_2023).json` | `920b2cbca378a1c851bb0521711f1b076fdfdb68939337d3faf30c81a869c48e` |
| `../../spec-index/sources/Personal Account HMI Logic and Flow R1L-R (February 10 2023).pdf` | `25553b9b5c63834eb916c82db2f6951982c5e8123410c9a221b46e5da2eb37a7` |

驗證：`shasum -a 256 -c BASELINE.sha256` → **4/4 OK**，exit 0。
涵蓋依 01b 明示之 R-C20 比照（涵蓋以來源為準）。
**037 到齊後須更新本檔** —— 現在它不在，所以它也不在保護範圍內。

---

## 3. 作業項 3 — Recon ⛔ **停下，未執行**

依 01b「與預期不符即停並回報，不得自行調整判準」與 canon §8.5 第 2 條
「不自行調和」。**兩個互相獨立的阻擋**，任一單獨成立即足以停下：

### 3.1 阻擋一 — 037 Analysis Report 不在 repo 內（A-UP04）

下放包 §素材 指名：
`FM-WI-FSM-037-A03 N1L SWE1 Personal Account HMI V0.1 STLA 報告.xlsx`

搜尋條件：repo 全樹 ＋ `~`（深度 6，排除 `Library/`、`.Trash/`）；
比對式 `-iname "*037*Personal*"`、`-iname "*Personal Account*"`、
`-iname "*PROF*.xlsx"`（**檔名比對，大小寫不敏感，非內容比對**）。

實測：**0 個命中**。repo 內既有 037 僅 `features/power/inputs/`、
`features/comfort/inputs/`、`features/sxm/inputs/` 三個他 feature 的。
`features/user_profiles/inputs/` 除本輪置入之 036 母本複本外為空。

`scripts/recon.py` 未執行 —— 其 `survey_a03()` 之第一個動作即
`openpyxl.load_workbook(a03_path)`，無檔即無從開始。
**未執行 ≠ FAIL，亦 ≠ PASS，本項為「未實測」**（canon §5a 第 11 條）。

**因此下列全部無法量測，一律標未實測，不以任何替代來源估算**：
葉節點數、Heading 數、Out of scope 2 列之 id、生成母體、
FROP 欄 182 列之值、Sub Categorization 分布、037 Priority 分布、
Source Requirement ID 唯一值、037 引用之 135 個 id 之實際集合。

### 3.2 阻擋二 — 預期值本身之單位不一致（A-UP07，與阻擋一互相獨立）

**這一項即使 037 到齊也不會消失**，故獨立列出。

01b 之判準（逐字）：`leaf = Categorization 以 Functional 起始者`
01b 之預期值（逐字）：`葉節點 182、扣除 Out of scope 2 後母體 180、Heading 25`

01_intake.md 同時記載兩組數字，**其量測單位不同**：

| 數字 | 量什麼 | 單位 | 出處 |
|---|---|---|---|
| **180** | Categorization 欄值 == `Functional Requirement` | 逐列 | 01_intake.md §實測 第 2 行 |
| **182** | **ID 非任何其他 ID 之前綴** | 逐列 | 01_intake.md §實測 第 3 行 |
| 25 | Categorization 欄值 == `Heading` | 逐列 | 01_intake.md §實測 第 2 行 |
| 2 | Categorization 欄值 == `Out of scope` | 逐列 | 01_intake.md §實測 第 2 行 |

在 01b 所裁定之判準下：`Out of scope` 不以 `Functional` 起始 → 該 2 列本就
不在葉節點集合內 → **葉節點 = 180，且不需再扣除 2**。
故「葉節點 182、扣 2 得 180」在該判準下**不可能成立**：
182 只能以 ID 前綴形態量得，而 01b 沒有授權該判準。
兩條路徑恰好都得到 180，是 canon §5a A-PJ27 型之**單位巧合** ——
數字自洽而不露破綻，正是本紀律存在的理由。

**另據（既有政策，canon §5a 第 17 條）**：Comfort `R-C3` 逐字
「禁止以 tc id 後綴形態（是否具 -NN）判定 leaf」，並要求以 recon assertion
機械強制 Categorization 計數（Comfort 實測該判準漏 34 列，8.4%）。
`scripts/recon.py:568` 之註解亦已把 ID 形態判準標為 "the ID-suffix heuristic
that the ruling BANS"，只作對照輸出，不作閘。**本 feature 之 182 出自同類判準。**

**另一項需一併裁的量測條件**：`recon.py` 把所有非葉節點列入 `headings`
一個桶，故其 `headings` 計數 = 非葉節點全體 = **25 + 2 = 27**，
而 `Categorization == "Heading"` 之逐列計數才是 **25**。
下放包所指之「Heading 25」是後者。assertion 若寫在 `len(headings)` 上會得 27。

**執行層之處置（三不之遵守）**：
- 不代擬條文：`feature.yaml` `recon_assertions.functional_requirement_count`
  與 `heading_count` **留 `TBD`**，未填任何期望值。
- 不自行調和：未改判準、未改預期值、未擇一。
- 不越權補件：未以 spec 側之 135／169 等數字反推 037 側之葉節點數。

**提議（供裁決參考，未寫入任何 assertion）**：三個閘一律用 Categorization
欄之逐列計數（同一單位）—— `functional_requirement_count == 180`、
`heading_count == 25`（欄值等於 `Heading` 者，非 `len(headings)`）、
`out_of_scope_count == 2`；182 改記為「ID 前綴形態之對照值」輸出而不作閘，
即 recon.py 現行對 `naive_leaf_shape` 之處理方式。

### 3.3 已複驗之判準（與 01b 相符者，亦列出）

| 01b 之判準 | `recon.py` 實作 | 判定 |
|---|---|---|
| header row = 含 `Requirement Description` 之列 | `recon.py:509` `any("requirement description" in norm(v) for v in r)`，**大小寫不敏感、子字串比對無詞界** | ✅ 相符 |
| 本件 header row 為第 7 列 | 未實測（無檔）；已填入 `feature.yaml` 待驗 | 未實測 |
| leaf = Categorization 以 `Functional` 起始 | `recon.py:545` `cat.lower().startswith("functional")`，**大小寫不敏感、前綴比對** | ✅ 相符 |
| Categorization 欄之定位 | `recon.py:518` 以表頭文字 `categorization` 定位並 `forbid=("sub",)` 排除 `Sub Categorization` | ✅ 相符 |

---

## 4. 作業項 4 — Outline map ✅ spec 側完成｜037 側未實測

腳本：`features/user_profiles/scripts/build_outline_map.py`（新增，Tier 1）
輸出：`data/spec_id_to_outline.tsv`（tracked）、`data/outline_map.json`、
`data/spec_popup_ids.tsv`、`data/expected_cited_sections.tsv`

### 4.1 預期值對照（相符者亦列出）

量測條件：`Basic Report` 表頭列 1、資料列 2–170（第 171 列全空，不計）；
四欄以表頭文字定位；section id 取 `SYSRE_HMI_Source ID` 之末段 `_{section}`。

| 項 | 下放包預期 | 實測 | 判定 |
|---|---|---|---|
| spec work items | 169 | **169** | ✅ 相符 |
| section id → 正文 對映條數 | 169 | **169** | ✅ 相符 |
| Source ID 欄之 stem 是否單一且屬 CR24798 namespace（R-U3）| 169 列全屬 | **169/169 單一 stem** = `Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)` | ✅ 相符 |
| Source ID 無法解析之列 | （未指定）| **0** | — |
| section id 與 `Outline Number` 欄逐列一致 | （未指定，本執行層加驗）| **169/169 一致，0 mismatch** | — |
| section id 重複 | （未指定，本執行層加驗）| **0**（重複即 `SystemExit`）| — |
| 章節骨架 14 章與其標題 | 下放包 §章節骨架 14 章 | **14 章逐字相符**（1 Assumptions … 14 Valet Mode - Exit）| ✅ 相符 |
| ch1／ch2／ch3 之 section 數 | 12／2／6 | **12／2／6** | ✅ 相符 |
| **037 引用之 135 個 id 全數命中** | 缺漏 0 | **未實測 —— 037 不在 repo（A-UP04）** | ⛔ 未實測 |

`R-U1` 所指定之 `specification_reference` stem 字串，與實測之 169 列唯一
stem **逐字元相符**（含 `(October_03_2023)` 之括號與底線）。
已填入 `feature.yaml` `spec_reference_template`。

### 4.2 spec 側之獨立交叉驗證 —— 135 可自 spec 單邊重建

下放包記「未被 037 引用 34（純章節標題 11、ch1 12、ch2 2、ch3 6、
10.1／11.1／11.2 3）」。純以 spec 側實測重建：

```
169  全部 section
-20  ch1(12) + ch2(2) + ch3(6)                    → 149（ch4–14）
-11  ch4–14 之純章節標題列（"4","5",…,"14"）      → 138
- 3  10.1、11.1、11.2                              → 135
```

**135 —— 與下放包之「引用之唯一 HMI Source ID 135 個」逐數相符。**
候選集合已逐條寫入 `data/expected_cited_sections.tsv`（135 列），
037 到齊後即可與其引用集合做**集合對集合**比對，而非只比計數。

**此為單邊重建，不是命中驗證。** 它證明的是「spec 側扣掉下放包點名的
34 條，恰好剩 135 條」，**不能**證明 037 實際引用的就是這 135 條。
兩者相符之強度僅到「計數一致且扣除規則自洽」。命中驗證仍待 037。

per-chapter（候選 135 之 section 數，逐列）：
4:17　5:28　6:10　7:9　8:20　9:21　10:3　11:4　12:18　13:3　14:2

對照下放包之「葉節點章節分布」4:29　5:41　6:11　7:14　8:25　9:22　10:3
11:6　12:25　13:4　14:2（合計 182）—— **兩組數字單位不同**：
前者是 spec section 數（逐 section），後者是 037 葉節點數（逐列）。
葉節點多於 section，因多個葉節點可引同一 section（182 → 135 唯一）。
**兩者不應相互驗算**，並列於此以免後續誤用。

### 4.3 正文量測（spec 側 169 條全體）

| 項 | 實測 | 條件 |
|---|---|---|
| `Description` 字元數 | n=169，min **10**、median **182**、max **1568** | `len()`，code point；含 `_x000D_` 等原始換行標記 |
| 含 `(image:` 圖片參照之 section | **19** | 子字串比對 `(image:`，大小寫敏感 |
| 唯一 PU id | **20** | 見下 |
| PU id 逐引用次數 | **22** | PU0588、PU1088 各 2 次 |

| 項 | 下放包預期 | 實測 | 判定 |
|---|---|---|---|
| spec 全文唯一 PU id | 20 | **20** | ✅ 相符 |
| 被引 135 條正文長度中位數／最短／最長 | 193／65／728 | **未實測**（本輪之 169 條母體為 182／10／1568，**母體不同，不可比**）| ⛔ 未實測 |
| 含圖片參照 14 條（被引 135 條中）| 14 | **未實測**（169 條母體中為 19，**母體不同，不可比**）| ⛔ 未實測 |

後兩項須先有 037 之引用集合才能圈出「被引 135 條」這個母體。
以 169 條之數字冒充 135 條之數字，即 canon §5a 第 8 條所禁之
「用規則自身的措辭圈出樣本」之同型錯誤，故標未實測而非相符。

20 個唯一 PU id（逐 section 對映見 `data/spec_popup_ids.tsv`，
已填入 `feature.yaml` `lint.popup_ids`）：
PU0091 PU0118 PU0129 PU0394 PU0580 PU0584 PU0585 PU0588 PU0611 PU0626
PU0832 PU0833 PU0841 PU0934 PU1087 PU1088 PU1089 PU1090 PU1091 PU1573

**本執行層之自曝抽取缺陷（canon §5a 第 7／12 條實例）**：
初版比對式 `PU\s?(\d{3,4})` 得 **18** 個唯一 id，與下放包之 20 不符。
追查後確認是**本執行層的漏抽**，非下放包之誤：`PU_0118`（4.1.1）與
`PU_0129`（5.13.2）採**底線分隔**，未被 `\s?` 涵蓋。改為 `PU[\s_]?(\d{3,4})`
後得 20，與下放包相符。**18 與 20 都不觸發任何例外** —— 這正是第 12 條
「抽取式之缺陷不會報錯」。攔下它的不是任何 gate，是下放包的預期值 20
（canon §8.3 第二層之作用）。同型風險已記入 `DATA_REQUESTS.md`，
供後續同類 gate 一併檢查（第 6 條：字串比對缺陷具傳染性）。

### 4.4 R-U5 之 spec 引用複核（核實無誤）

R-U5 之 P0 帶點名「5.13.x Clear Personal Data／刪除全部 profile／回復原廠」。
spec 側實測：**5.13.1 與 5.13.2 存在**；5.13.2 逐字含
`Using the "Clear Personal Data" setting (and confirming from popup PU0626)
will delete all…`，並引 PU0626／PU1089／PU1090／PU1091；
5.13.1 為 `If all Profiles are cleared and the default Profiles are restored,
return to default order`。**R-U5 之引用與 spec 相符，核實無誤，不需改。**
（理由不是「無 gate 命中」，是逐條讀了 5.13.1／5.13.2 的正文。）

---

## 5. 作業項 5 — Framework Part N 草案（Tier 2，不自裁）

### 5.1 Layer 1 — Test Group ✅ 可定（R-U1 已裁）

- Test Group 欄值 = **`User Profiles`**（R-U1 逐字，含空格；
  **不是** `User_Profiles`，亦不是 `UserProfiles`）
- 依 R-U6（BLANK）：Test Group／Test Set 兩欄 = **FILL**
- **未複驗**：R-U1 所據之「037 FROP 欄 182 列實測值」本輪無法複驗（A-UP04）

### 5.2 Layer 3 — spec 章節骨架 ✅ 可定（01b 已裁 ch4–14）

生成範圍 = spec **ch4–14**，共 **149 section**（含 11 個純章節標題列）；
ch1–3 之 20 section 不入生成範圍（見 A-UP02）。Layer 3 為 framework-internal，
**永不寫入工作簿**（framework.md Part I 明文）。

| ch | 標題（spec 逐字）| section 數 | 其中 depth≥3 | 候選被引 |
|---|---|---|---|---|
| 4 | Profile Overview | 18 | 10 | 17 |
| 5 | All Profiles Tab | 29 | 12 | 28 |
| 6 | Default Profiles - No Custom Profiles | 11 | 4 | 10 |
| 7 | Welcome Screen (Custom Profile) | 10 | 4 | 9 |
| 8 | New Profile Setup | 21 | 8 | 20 |
| 9 | Editing a Profile | 22 | 12 | 21 |
| 10 | Profile Info Page | 5 | 1 | 3 |
| 11 | Connected Profile App | 7 | 1 | 4 |
| 12 | Valet Mode | 19 | 8 | 18 |
| 13 | Valet Mode - SPAAK | 4 | 0 | 3 |
| 14 | Valet Mode - Exit | 3 | 0 | 2 |
| | **合計** | **149** | **60** | **135** |

（「候選被引」= 扣除章節標題列與 10.1／11.1／11.2，見 §4.2；
depth≥3 = section id 含兩個以上 `.` 者，逐 section 計。）

### 5.3 Layer 2 — Test Set 邊界：**只出草案，不自裁**

**01b 要求「取 spec 目錄與 037 分群之交集」。037 分群本輪不可得
（A-UP04），故以下草案為 spec 單邊推導 —— 它缺了 01b 所要求的一半輸入。**
下方所引之葉節點載量取自下放包 01_intake.md §葉節點章節分布，
**引自下放包，本輪未複驗**。

granularity 目標：framework.md §4.1.2「~10–50 RD parents per Set」。

#### 草案 A — 7 個 Set（合併小章）

| # | Test Set（草案）| Layer 3 | 葉節點載量（引自下放包）| granularity |
|---|---|---|---|---|
| 1 | Profile Overview | ch4 | 29 | ✅ |
| 2 | All Profiles Tab | ch5 | 41 | ✅ 接近上界 |
| 3 | Welcome & Default Profiles | ch6 + ch7 | 11 + 14 = 25 | ✅ |
| 4 | New Profile Setup | ch8 | 25 | ✅ |
| 5 | Editing a Profile | ch9 | 22 | ✅ |
| 6 | Profile Info & Connected App | ch10 + ch11 | 3 + 6 = 9 | ⚠ 略低於 10 |
| 7 | Valet Mode | ch12 + ch13 + ch14 | 25 + 4 + 2 = 31 | ✅ |
| | 合計 | ch4–14 全覆蓋 | **182** | |

#### 草案 B — 11 個 Set（一章一 Set）

逐章對應，無合併。代價：ch10（3）、ch11（6）、ch13（4）、ch14（2）
四個 Set 遠低於 granularity 下界；ch13/ch14 各只 2–4 條，
Set 粒度與 TC 粒度接近，Test Set 欄失去分群意義。

#### 草案 C — 6 個 Set（草案 A 再合併 ch6/ch7 與 ch4）

把 ch6+ch7 之 welcome 流程併入 `Profile Overview`（54），
其餘同草案 A。代價：第一個 Set 超過上界 50。

#### 執行層之觀察（供裁決參考，不構成建議之外的動作）

- **ch12–14 三章同屬 Valet Mode**（標題逐字 `Valet Mode`／
  `Valet Mode - SPAAK`／`Valet Mode - Exit`），且 13／14 之條文皆以
  `PVALSPK`／`PVALEX` 前綴延續 ch12 之 `PVAL` 家族 —— 合併之依據在 spec 內
  即為明文（同父題名 ＋ 同前綴家族），非本執行層之判斷。
- **ch6 與 ch7 皆為 welcome popup 流程**（`NOPR`／`PRWEL` 前綴），
  差別是「無自訂 profile 時的預設 popup」vs「自訂 profile 的 welcome popup」。
  併或不併都能自 spec 說出理由，**這一項確實是 Tier 2 判斷**。
- **ch10 與 ch11 皆為 Profile Info 之延伸**（`PRINFO`／`CPA` 前綴），
  且 ch11 有 4 條 R1-High/China 限定之不適用註記（10.1／11.1／11.2 已列
  A-UP02，11.2／11.4 另含 `not applicable for R1H` 字樣）。
  合併後仍只 9 條，低於下界；**是否接受低於下界，屬 Tier 2**。
- **037 分群到齊後可能推翻以上任一項** —— 若 037 之 Sub Categorization
  （HMI 160 / Service 22，引自下放包未複驗）與章節不同構，
  交集之結果可能與純章節分組不同。**故本節不進入 framework.md。**

### 5.4 本輪「正確地不動」之項目

| 項 | 依據 |
|---|---|
| 未於 `docs/fw036/framework.md` 附加 Part（User Profiles）| Layer 2 為 Tier 2 未定；附一個 Layer 2 待定之 Part 等同以草案佔位。canon §4：`[PROPOSED]` 未觸即成 binding —— 寫進去就會變成默認通過 |
| 未寫 `docs/runtime/profiles/FW036_R1L_User_Profiles_Profile.md` | Phase 3（Tier 2），非本包授權範圍 |
| 未填 `DECISIONS.md` 之 `[PROPOSED]` 項 | Phase 1 recon 之產物；recon 未跑（§3），無實測可填。**填了就是代擬** |
| 未動 A-UP02 之 8 條無覆蓋條文 | RD-1，Tier 3 由 Pei 送出（01b §未決）|
| 未執行任何 git 操作 | 下放包禁區；canon §8.8「git 一律不在執行層」|
| 未刪除 `forms/` 任何檔 | R-G2「不得刪除」|
| 未存回母本 | R16/R18-3 ＋ x14 DV 之獨立理由（§2.4）|

---

## 6. 作業項 6 — 上繳 ✅

- 本檔：`features/user_profiles/docs/upstream/01_intake.md`
- 索引：`features/user_profiles/docs/INDEX.md` 已建並登記本輪往返
- 新開 anomaly 與 DR **成對**：A-UP04 ↔ DR #1、A-UP06 ↔ DR #2、
  A-UP02 ↔ DR #3。A-UP05、A-UP07、A-UP08、A-UP09 為判準／記載／實作層之項，
  **無對應素材需求**，故無 DR 列 —— 四者皆附「提議處置」段落，
  A-UP08 之 (a) 若裁為需要含該分頁之 rev C 母本，屆時才產生 DR 列。

### 6.1 本輪 anomaly 全表

| id | 狀態 | 一句話 | Tier |
|---|---|---|---|
| A-UP01 | RESOLVED（複驗維持）| SYS1 誤件已更正 | — |
| A-UP02 | PENDING（下放包）| 8 條 spec 條文無 SWE 覆蓋 | 3（RD-1）|
| A-UP03 | **RESOLVED（本輪）** | FORMS.md `20260816_ext` 條目脫鉤 → 已改記實測值 | 1 |
| A-UP04 | **PENDING（新開）** | 037 不在 repo，recon 全停 | 3（索取）|
| A-UP05 | **PENDING（新開）** | `20260816_ext` 記載與磁碟非同源（601 vs 1411）| 2 |
| A-UP06 | **PENDING（新開）** | HMI Pop Up List 未到齊 | 3（索取）|
| A-UP07 | **PENDING（新開）** | 作業項 3 預期值單位不一致（182 vs 180）| 2 |
| A-UP08 | **PENDING（新開）** | 母本無 `Test Case Framework` 分頁，而 framework.md 依賴它 | 2 |
| A-UP09 | **PENDING（新開）** | openpyxl 存回摧毀 R 欄 x14 下拉（已實測）| 1（實作約束）|

---

## 7. 預期值對照總表

| # | 項 | 下放包預期 | 實測 | 判定 |
|---|---|---|---|---|
| 1 | `20260121` SHA256 | `cd876c20…` | `cd876c20…` | ✅ |
| 2 | `Home_20260809` SHA256 | `1895fb2a…` | `1895fb2a…` | ✅ |
| 3 | `20260816_ext` SHA256 | `6d53056e…` | `4b3d4470…` | ❌ A-UP03/05 |
| 4 | `20260816_ext` bytes | 123,717 | 200,654 | ❌ A-UP03/05 |
| 5 | `20260816_ext` B 欄範圍 | 10–601 | 10–1411 | ❌ A-UP05 |
| 6 | 母本 sheet 名 | （待探）| `Test Case Specification 測試用例規範`，9 分頁 | ✅ 已探 |
| 7 | 母本 header row | （待探）| 9 | ✅ 已探 |
| 8 | 母本 A–AH 欄位對映 | （待探）| 34/34 命中，rev C | ✅ 已探 |
| 9 | 母本 B 欄公式範圍 | （待探）| B10–B1411（1402 格）| ✅ 已探 |
| 10 | 母本 P/R/T–Z/AF DV | （待探）| P10:Q1411／R10:R1411(x14)／T10:Z1411／AF10:AF1411 | ✅ 已探 |
| 11 | 下拉選單詞彙 | 9 條 | **9 條逐字** | ✅ |
| 12 | 母本複本 SHA == 母本 | （隱含）| 相同 | ✅ |
| 13 | BASELINE.sha256 驗證 | （隱含）| 4/4 OK | ✅ |
| 14 | **葉節點** | **182** | **未實測**（A-UP04）＋ 判準下不可能成立（A-UP07）| ⛔❌ |
| 15 | **生成母體** | **180** | **未實測**（A-UP04）| ⛔ |
| 16 | **Heading** | **25** | **未實測**（A-UP04）；另 `recon.py` 之 `headings` 桶為 27，單位不同（A-UP07）| ⛔❌ |
| 17 | 037 header row | 7 | 未實測（A-UP04）| ⛔ |
| 18 | spec work items | 169 | **169** | ✅ |
| 19 | outline map 條數 | 169 | **169** | ✅ |
| 20 | Source ID 單一 stem（R-U3）| 169 列全屬 CR24798 | **169/169** | ✅ |
| 21 | 章節骨架 14 章標題 | 下放包 §章節骨架 | **逐字相符** | ✅ |
| 22 | ch1／ch2／ch3 section 數 | 12／2／6 | **12／2／6** | ✅ |
| 23 | 未被引用 34 之扣除自洽性 | 34 | **169−20−11−3 = 135 自洽** | ✅ |
| 24 | 引用之唯一 HMI Source ID | 135，缺漏 0 | 候選集合 **135**（單邊重建）；**實際命中未實測**（A-UP04）| ⛔ 部分 |
| 25 | spec 全文唯一 PU id | 20 | **20** | ✅（初版誤得 18，見 §4.3）|
| 26 | 被引 135 條長度 中位/最短/最長 | 193／65／728 | 未實測（母體不同）| ⛔ |
| 27 | 含圖片參照（被引 135 條中）| 14 | 未實測（母體不同；169 條母體為 19）| ⛔ |
| 28 | FROP 欄 = `User Profiles`（182 列）| 182 列一致 | 未實測（A-UP04）| ⛔ |
| 29 | Sub Categorization HMI 160 / Service 22 | — | 未實測（A-UP04）| ⛔ |
| 30 | 037 Priority High 79/Medium 75/Low 28 | — | 未實測（A-UP04）| ⛔ |
| 31 | Source Requirement ID 唯一值 135 | — | 未實測（A-UP04）| ⛔ |
| 32 | workbook_state = BLANK（R-U6）| BLANK | **BLANK，獨立實測佐證**（非空格 0／filled 列 0）| ✅ |
| 33 | R-U5 之 5.13.x Clear Personal Data 引用 | — | **核實無誤**（5.13.1／5.13.2 存在，PU0626 逐字）| ✅ |
| 34 | R-U1 之 spec_reference stem 字串 | 逐字 | **與 169 列唯一 stem 逐字元相符** | ✅ |

相符 **18** 項｜不符 **4** 項（#3/#4/#5 同一件事 A-UP03/05；#14/#16 之判準面
為 A-UP07）｜未實測 **12** 項（其中 10 項因 A-UP04，2 項因母體不同）。

**lint 全跑 ＋ 基線重現（canon §8.3 第一／三層）：本輪未執行。**
理由：Phase 0 無任何生成列，lint 之對象不存在；`lint_defs.BASELINE`
之全簿基線同理。依 canon §5a 第 11 條，本階段之 lint **不可能 FAIL**，
故標「未實測」而非 PASS —— 標 PASS 會是同義反覆。

---

## 8. 獨立判斷 —— **本包是否仍有該驗而未驗者**

**有。以下 9 項為執行層獨立認定之「該驗而未驗」，不因下放包未點名而免除。**

### 8.1 因 037 缺件而不可驗（7 項，一次到齊即可全解）

1. 作業項 3 之全部三個預期值（葉節點／母體／Heading）
2. 037 header row 是否確為第 7 列
3. R-U1 所據之 FROP 欄 182 列是否全為 `User Profiles`
   —— **R-U1 之 Test Group 值目前只有下放包單一來源**
4. R-U4 點名之 PROF-017／PROF-035 是否確為 Out of scope 兩列
5. 037 引用之 135 個 id 與 `data/expected_cited_sections.tsv` 之
   **集合對集合**比對（現在只比得出計數）
6. 被引 135 條之正文長度分布與圖片參照數（母體須由 037 圈出）
7. Sub Categorization 與 Priority 分布（R-U5 之「037 先驗」之實際內容）

### 8.2 執行層自認之缺口 —— **本輪已補驗，兩項皆已關閉**

兩項最初都被列為「已可驗而本輪未驗」。因 canon §5a 第 11 條明文
「必須以複本實測」、第 14 條要求檢查條件自我完備，兩項於本輪內補完：

8. **x14 DV 之寫入行為** —— **已補實測，見 §2.4 第 1 點之表**。
   結論由「推論」升為「實測」：openpyxl 存回使 `<x14:dataValidation>`
   由 1 → 0、zip members 48 → 47，而三條 legacy DV 存活。
   量測在 scratchpad（repo 外）之複本上進行，母本與 `inputs/` 複本均未被
   寫入，母本 SHA 前後一致 —— **「openpyxl save 全 repo 禁用」之字面範圍
   為 repo，本次寫入不在其內**。已登記 A-UP09。
9. **`Test Case Framework` 分頁 absent 之後果** —— **已查證，確有依賴**。
   `docs/fw036/framework.md` §`Workbook sync`（Part I）明文要求該分頁
   「single column A, values at rows 5–14」須新增 A15／A16 之 Test Set 名，
   即 **Media 之流程確實把 Test Set 清單寫進該分頁**。
   本 feature 之母本（rev C，9 分頁）**無該分頁**；rev A/B（Home 225 列版，
   10 分頁）有。故本 feature 先天缺該載體。已登記 **A-UP08**（Tier 2）。
   附帶發現：該節所示之範例程式碼即 `openpyxl` + `wb.save()`，
   與本 feature 之 A-UP09 直接衝突 —— 照抄該節會摧毀 R 欄下拉。

### 8.3 需 Tier 2 裁決方能繼續者（不是「未驗」，是「不可自裁」）

- **A-UP07**（作業項 3 之預期值單位）—— 未裁則 recon 之 assertion 無期望值，
  Phase 1 無法收尾。**這是目前唯一一個「037 到齊也不會自動解除」的阻擋。**
- **A-UP05**（`20260816_ext` 記載與磁碟非同源之正式處置）
- **A-UP08**（母本無 `Test Case Framework` 分頁，該分頁是否仍為交付要求）
- **Layer 2 Test Set 邊界**（§5.3 三草案）
- **歸檔三檔之雜湊保護歸屬**（§2.4 第 4 點）

### 8.5 尚不可驗，且到齊亦不足者（1 項，執行層提醒）

037 到齊只解除 §8.1；**A-UP07 之判準面不會因此解除**（§3.2 已述）。
兩者若被當成同一件事處理，會出現「037 一到就跑 recon」而 assertion
仍無合法期望值之情形 —— 屆時最省事的做法正是把期望值改成實測值，
那即 canon §8.5 第 2 條所禁之自行調和。**先裁 A-UP07，再跑 recon。**

### 8.4 已檢查並認定不需驗者（附理由，非「沒看」）

- **母本是否含他 feature 殘留值**：已逐格掃 A–AH × row≥10，
  非空格 0；`D5` Scope 空；`D2` = `newR1L`（原範本既有，非 feature 專屬）。
  FORMS.md 對 `20260816_ext` 所記之 5 格 AntiTheft 範例值，本母本**皆為空**。
  → 不需再驗。
- **spec 是否為 A-UP01 之誤件**：`spec-index/cache/` 內 Personal Account
  只有一份，169 列、stem 全為 CR24798 Personal_Account namespace，
  章節標題與下放包骨架逐字相符。Personal Assistant 誤件不在 repo。
  → 不需再驗，A-UP01 維持 RESOLVED。
- **section id 唯一性與 Outline Number 一致性**：169/169 一致、0 重複、
  0 unparsed，且重複會直接 `SystemExit`（不是靜默通過）。→ 不需再驗。

---

## 9. 本輪改動之檔案清單

**新建**

| 檔 | 說明 |
|---|---|
| `features/user_profiles/{RUNBOOK,ANOMALIES,RULINGS,DATA_REQUESTS,DECISIONS,PLAYBOOK}.md` | scaffold ＋ 播種 |
| `features/user_profiles/{feature.yaml,.gitignore}` | scaffold ＋ 實測填寫 |
| `features/user_profiles/BASELINE.sha256` | 4 筆，4/4 OK |
| `features/user_profiles/scripts/build_outline_map.py` | 作業項 4 |
| `features/user_profiles/data/spec_id_to_outline.tsv` | 169 列（tracked）|
| `features/user_profiles/data/outline_map.json` | 169 條全文 |
| `features/user_profiles/data/spec_popup_ids.tsv` | 20 列 |
| `features/user_profiles/data/expected_cited_sections.tsv` | 135 列候選 |
| `features/user_profiles/docs/upstream/01_intake.md` | 本檔 |
| `features/user_profiles/docs/INDEX.md` | 索引 |
| `archive/forms_superseded/` ＋ 三份 036 檔 | R-G2（`mv`，非 `cp`）|
| `features/user_profiles/inputs/…_SWQT_20260817_ext.xlsx` | 母本複本（gitignored）|

**修改**

| 檔 | 改什麼 |
|---|---|
| `forms/FORMS.md` | ＋R-G1/R-G2 條文區塊與四檔 SHA 表；三條目路徑改指 `archive/`（條目未刪）；`20260816_ext` 加 A-UP03/05 警示與雙欄對照；＋母本完整探測節 |
| `docs/fw036/FEATURE_ONBOARDING.md` | §0 Tier 0 ＋R-G1 條列（含 x14 DV 之覆寫實測結果）|
| `features/user_profiles/.gitignore` | ＋`data/outline_map.json`（可重建產物）|
| `features/user_profiles/RUNBOOK.md` | Phase 0／1 狀態與停下理由 |

**本執行層之第二個自曝缺陷**：`.gitignore` 之
`data/outline_map.json` 初版寫成 `data/outline_map.json   # 註解` 同一行。
**git 不剝除行尾註解**，整行被當成字面 pattern，該項因此未被忽略。
以 `git check-ignore -v` 實測才發現（`git status` 只顯示它是未追蹤，
**不會說原因**）。已改為註解自成一行，複測 `git check-ignore` 命中。
與 §4.3 之 PU id 漏抽同型：**兩者都不報錯，只是安靜地不生效**
（canon §5a 第 12 條）。

**未改動（刻意）**：`docs/fw036/framework.md`、
`docs/runtime/profiles/`、`scripts/recon.py`、任何他 feature 之檔案、
git 索引與工作樹狀態（未執行 `git add`／`commit`）。
