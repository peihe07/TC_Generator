# 上繳包 33 —— 正向轉換謂詞、050 裁定與不可再生產物

> 對應下放包：`features/power/docs/handoff/33_positive_predicate.md`
> 執行層：Claude（TC_Generator）
>
> **§J 自檢二次皆一致（R-P200(c)）**：開工時與抄錄條文前皆為
> §A block **5** / §J 列數 **5** / §H 步驟 9「**五條**」；
> 檔案 **11994 bytes、mtime 08-18 17:17:51 均未變**。
>
> **§H 步驟 3 之明令已守：B3 保護先行，保護就位前未執行任何會寫入 (c) 型產物之腳本。**
> 本包**未執行任何 git 子命令**（含自造損壞之還原，見 §三）；
> **未放寬 `ROW3_RE`**；**未變更任何 `design_method` 或 `priority` 之值**。

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**
**編號查核（R-P147）**：R-P 最大 **230**、A-PW 最大 **169**、DR-PW 最大 **15**、閘門最大 **G157**。
本包新號：**R-P231–R-P235**、**A-PW170–A-PW175**、**G158–G162**。**DR 無新增**。

---

## 一、B3 —— 不可再生產物保護（R-P233 / G160）**先行**

### 1.1 腳本 → (c) 型產物之對照（掃全部 `scripts/`，區分讀／寫）

| 腳本 | 寫入之 (c) 型產物 |
|---|---|
| `build_b4_material.py` | `b4_material.md` |
| `build_b5_material.py` | `b5_material.md` |
| `assign_final_tc_id.py` | `final_tc_id_map.tsv` |
| `dryrun_write_back.py` | `b3_dryrun.json` |
| `verify_writeback_path.py` | `b2b3_writeback_path.json` |
| `check_edit_integrity.py --update-baseline` | `edit_integrity_baseline.json` |

其餘 6 個提及 (c) 型產物之腳本（`reverse_coverage.py` / `or_branch_coverage.py` /
`build_er_restatement.py` / `build_final_step.py` / `classify_products.py` /
`backup_before_rewrite.py`）**皆為讀取**，已逐一查證。

### 1.2 寫入保護與重設紀錄

`scripts/protect_products.py` —— (c) 型 **12 份**全數受保護；
已存在且未帶 `--overwrite-protected` 者**拒寫並回報**。

**fixture 四案如期**：(c) 已存在無參數 → 拒寫；(c) 已存在帶參數 → 放行；
(c) 不存在（首次產生）→ 放行；非 (c) 已存在 → 放行。

**實測**：重跑 `build_b4_material.py` **遭拒**，`b4_material.md` 維持 **231 行**未動。

`edit_integrity_baseline.json` 另加一層 —— `--update-baseline` 現須先過
`guard_write`，寫入後 append `data/edit_integrity_reset_log.tsv`
（UTC 時點、重設前後之 SHA256、note）。實測：無覆寫參數之更新**遭拒**。

### 1.3 一項自造損壞之揭露

套用保護時，執行層之自動插入將 import 誤置於 `load_ok()` **函式體內**，
致 `check_edit_integrity.py` 縮排錯誤而無法載入。
**依 R-P149（自造損壞不得以 git 修復）以逐處編輯還原**，未動 git；
還原後 `ast.parse` 通過、**G108 7 / 7**。

**與 A-PW111（20 包之過寬切片）同型 —— 以正則定位插入點之第二次。**

---

## 二、B4 —— 備份擴充（R-P234 / G161）

| 版 | 範圍 | 檔數 | 耗時 |
|---|---|---|---|
| 32 包 | `data/` | 68 | — |
| **33 包** | **`data/` ＋ `generated/` ＋ `scripts/`** | **131 → 133** | **0.05 – 0.08 秒** |

**耗時可忽略** —— 32 包所持二理由既被否決，其成本亦不構成不做之理由。
`--verify` / `--restore` 已同步支援三目錄之相對路徑。

**實測**：改寫前備份 → 改寫後 `--verify` 得 **3 檔相異**
（`g155` / `g156` / **`scripts/rejudge_design_method.py`**）—— 含 `scripts/`，擴充生效。

---

## 三、B1 —— 正向轉換謂詞與全批重判（R-P231 / G158）

### 3.1 詞彙自語料導出

ER 全文實測次數：`passes to` **38**、`reaches` 21、`is in <X> state/mode` **12**、
`transitions to` 6、`leaves` 6、`switches to` 4、`transitions from` 4、
`returns to` 4、`transition to` 3、`transitions back` 2、`goes to` 2、
`enters` 1、`starts from` 1。

**`reaches`（21）未全數納入** —— 其多為 `reaches its expiration`（計時器到期，
非狀態轉換），**僅取 `reaches <狀態名> mode/state` 之形態，免以高頻詞灌入第 3 列**。

### 3.2 全批重判（264 條）

| 提案 | 條 |
|---|---|
| 第 3 列 State Transition（**正向確認**）| **81** |
| **第 9 列 Functional Based（落底）** | **173** |
| 第 6 列 Boundary Value Analysis | 7 |
| 第 1 列 Negative / Invalid | 1 |
| 第 2 列 Fault Injection | **0**（依 R-P232）|
| **矛盾（正向與 G154 同時命中）** | **2** |

**「機械無法判定」由 196 降為 0。**
相符現值 **81 / 264 = 30.7%**（32 包之 60 為舊謂詞所得，**二數不可比**）；
入人工裁決 **183**。

### 3.3 矛盾 2 條 —— 皆為正向謂詞之限度

| tc | 命中 | 成因 | 裁定 |
|---|---|---|---|
| `034` | `transition to` ／ `remains in` | 正向詞位於**否定句** `no transition to …` | 第 4 列（維持 32 包裁決）|
| `071` | `passes to` ／ `stays in` | 正向詞之主語為**訊號值**（`Rear_Camera_Enable.Info passes to "False"`）**而非狀態** | 第 9 列（維持 32 包裁決）|

**二例皆由 G154 之對照當場攔下 —— 該對照設計有效。**

---

## 四、B2 —— 第 2 列依 R-P232 重判（G159）

實作：故障詞須見於 `input_test_data` 或 `test_procedure`（**注入之刺激**），
**僅見於 `pre_conditions` 者不命中**。

**`050`**：`disconnect` 出自前提 `The battery is disconnected` → 第 2 列不命中；
續判第 3 列，ER1 逐字為
`The TLM **leaves INIT state** once the voltage is within its thresholds`
→ **正向命中，與現值相符**。**32 包之待裁就此結案。**

**全批第 2 列命中數：1 → 0。** 即本語料中**無任何 TC 以故障為驗證對象**。

**一項須另查者**：現值有 1 條為 `基礎故障注入 (Fault Injection Lite)`
（`SWE-PM-073` 之 Battery Critical）—— 其 `Batt_ST_Crit` 為注入之刺激且被觀察，
**初判成立**，惟**未入本包之抽樣**，據實標明。

---

## 五、B5 —— P0 分布與 §10.2 對照（R-P235 / G162）

### 5.1 逐 Test Set

| Test Set | 條 | P0 | 佔比 |
|---|---|---|---|
| Power State | 128 | 113 | **88.3%** |
| Branding and Theme | 34 | 26 | **76.5%** |
| Startup Display | 59 | 40 | 67.8% |
| Timeout Settings | 26 | 11 | 42.3% |
| **Power Down** | 17 | 3 | **17.6%** |

全批 P0 **193 / 264 = 73.1%**；P1 63、P2 8、**P3 0**。

### 5.2 抽樣對照（34 / 193 = 17.6%，種子 `random.Random(33)`）

**可歸類 21、無法歸類或依據薄弱 13 = 38.2%。**

**明確不屬七類者 8 條**：`101` / `105`（Timeout1 自 PROXI 取值 —— 參數設定）、
`154`（Sirius logo）、`237`（品牌字型）、`240` / `241`（品牌 App icon）、
`257`（日間主題）、`259`（季節判定）——
**後六條皆屬 §10.2 之 P3「cosmetic detail / low-impact customization」**。

**依據薄弱者 5 條**：`110` / `138` / `139`（後視**影像**輸出 ——
§10.2 之 `audio output` 不含 video，七類無「影像輸出」）、
`191`（開機**音效**，非音訊輸出功能）、`088`（拒絕 popup 後**維持** Timed，較近 P1）。

### 5.3 最集中之訊號

**Branding and Theme 之抽樣 5 條全數無法歸類（5 / 5）** ——
該 Test Set 之 **26 條 P0（76.5%）幾乎確定應為 P3**。

**本包未改任何 `priority` 值。**

---

## 六、§D 全表自驗

| # | 期望值 | 實測 | 判定 |
|---|---|---|---|
| G158 | 【實測】正向命中 / 落底 / 矛盾 / 相異；矛盾者皆有人工裁決 | 正向 **81** / 落底 **173** / 矛盾 **2**（皆已裁）/ 相異 **183** | **已填** |
| G159 | 【實測】變動數；`050` 已依裁定處置 | 第 2 列命中 **1 → 0**；`050` 續判為第 3 列，**相符現值**，結案 | **已填** |
| G160 | (c) 型 12 份皆有寫入保護；已存在時拒寫並回報；fixture 證明 | **12 / 12** 受保護；fixture **四案如期**；實測拒寫成功 | **PASS** |
| G161 | 涵蓋 `data/` ＋ `generated/` ＋ `scripts/`；回報檔數與耗時 | **133 檔**、**0.05–0.08 秒**；實測捕捉到 `scripts/` 之變更 | **PASS** |
| G162 | 【實測】分布；抽樣之七類歸屬；無法歸類數 | P0 **73.1%**；抽樣 34；**無法歸類或薄弱 13（38.2%）** | **已填** |
| G70 | 全 PASS | 264 TC，阻斷類 PASS，exit=0；self-test exit=0 | **PASS** |

**無 MISMATCH。** 補驗：G0 7/7、G94 / G99 / G103 各 103/103、G108 7/7、
G121 PASS、G129 103/103、G146 PASS。

---

## 七、§F 與 §G

**A-PW170 ~ A-PW175**（A-PW01 – A-PW175 連續無缺）：

| 號 | 摘要 |
|---|---|
| A-PW170 | `ROW3_RE` 放寬已否決；正向謂詞下相符率 **30.7%** |
| A-PW171 | 「機械無法判定」歸零，173 條落底第 9 列；**該解讀為推導，未見反證** |
| A-PW172 | 不可再生產物保護缺如（已實作 G160，12 份全保）|
| A-PW173 | 備份未涵蓋 `generated/` / `scripts/`（已擴充至 133 檔）|
| A-PW174 | P0 73.1% 未經檢驗；抽樣 **38.2%** 無法歸類或薄弱 |
| A-PW175 | **執行層自造損壞：正則定位插入點之第二次**（已逐處還原，未動 git）|

DR-PW9 ~ DR-PW15 沿用，**無新增**。

---

## 八、裁決條文與台帳

**§A 五條逐字抄入 `RULINGS.md`**。現為 **R-P1 – R-P235 連續無缺，經 G146 驗無重複**。
§F 六項已入 `ANOMALIES.md`（A-PW01 – A-PW175）。

---

## 九、執行層自判：本包仍有該驗而未驗者

**有，四項。**

1. **173 條落底第 9 列，而 §K 已預先說那是推導。**
   §12 未明文末列為 catch-all，該解讀由分析層自「first-match ＋ 末列為
   Single feature check」推得。**我照做了，也沒找到反證 —— 但我沒有能力證明它對。**
   若解讀有誤，173 條會一致地落向 Functional Based，
   **與現行 95.8% 偏向狀態轉換是同一種病，只是換了個方向**。

2. **我又一次用正則去改自己的腳本，又一次改壞了。**
   A-PW111 是 20 包的過寬切片，這次是 import 誤置於函式體內。
   **這次是 Python 直接報錯所以我立刻知道；若那個插入沒造成語法錯誤
   而只是語義偏了，G108 也攔不住** —— 它驗的是語法、載入與符號，不是語義。

3. **`SWE-PM-073` 那條 Fault Injection Lite 我沒查。**
   全批第 2 列命中降為 0，而現值仍有一條標為故障注入。
   我初判它成立（`Batt_ST_Crit` 是注入且被觀察），
   **但它沒進抽樣，我是用讀過的印象判的，不是實測。**

4. **211 條取樣覆核仍未讀**（31 包備料至今三包）。
   §K 第 2 項已二度預先要求 34 包若仍未讀須說明 ——
   就執行層而言，**素材一直在，未讀之因不在我這端**。
