# 上繳包 10 — vsm_v42：三欄交付本實測 ＋ b1 dry-run lint 實跑

日期：2026-09-02　執行層：Claude Code　對應下放包：`docs/handoff/10_dryrun.md`

## 結果分類

| 分類 | 內容 |
|---|---|
| 改對了 | W-1 五本交付簿三欄實測；W-2 `trial_D_b1.xlsx`（17 條實內容、286 格）；W-3 lint 實跑 |
| 核實無誤 | **E78／E79／E81 全過**；回讀 286 格不符 **0**；x14 逐字存活；`sandbox/base` sha 不變；b1 34 檔 sha8 全相符 |
| 正確地不動 | 未寫 `sandbox/b1/`、未建 `delivered/`；**b1 內容缺陷不自修**（已凍，改須新裁決） |

**總判：E80 = 1（不為 0）→ 尚不可直接請 Pei 授權寫回，須先裁該一項。另有一項與交付慣例相牴觸者見第 5 節。**

---

## 1. W-1 三欄交付本實測（**E78**）

### 樣本之代換（**未照下放包字面，已回報**）

下放包指定 `vehicle_setting`／`popup`／`power` 三本 `delivered/`。**實測**：

| 線 | `delivered/` |
|---|---|
| `vehicle_setting` | **無該目錄** |
| `popup` | **無該目錄**（其交付候選在 `features/popup/output/`） |
| `power` | 有（`pm_29.xlsx`、`pm_73.xlsx`） |

改以**全庫實有之交付本五件**測（`find features -path "*/delivered/*.xlsx"` 得 4 件，
另納 popup 之 `output/` 交付候選 1 件）：
`power/pm_29`（390 列）、`power/pm_73`（288 列）、`ics_management`（31 列）、
`sw_update`（319 列）、`popup(output)`（5 列）—— **合計 1,033 資料列**。

> `power/pm_73` 之版面**整體右移一欄**（Q→R、AA→AB、AB→AC、車型欄 T–Z→U–AA），
> 為不同表單修訂版；本表以各本自身之表頭解析欄位，非以欄字母硬指。

### 三欄之實際值分布（逐本逐欄）

| 本 | 資料列 | Q（Estimated Test Time） | AB（Test Version） | 車型欄 ×7 |
|---|---:|---|---|---|
| `power/pm_29` | 390 | **(空)×390** | **(空)×390** | **七欄各 (空)×390** |
| `power/pm_73` | 288 | **(空)×288** | **(空)×288** | **七欄各 (空)×288** |
| `ics_management` | 31 | **(空)×31** | **(空)×31** | **七欄各 (空)×31** |
| `sw_update` | 319 | **(空)×319** | **(空)×319** | **七欄各 (空)×319** |
| `popup(output)` | 5 | **(空)×5** | **(空)×5** | **七欄各 (空)×5** |

**逐字所見值：無 —— 五本 1,033 列於該三欄（含車型欄七欄，計 9 欄）全部為空，相異非空值 0 個。**

### 結論（逐欄）

| 欄 | 慣例 | b1 之填法 |
|---|---|---|
| **Q** Estimated Test Time | **一致：留空**（1,033／1,033） | **留空** |
| **AB** Test Version | **一致：留空**（1,033／1,033） | **留空** |
| **V** 車型欄 `VF(ProMaster)637 Atl-Mi`（及 T–Z 其餘六欄） | **一致：留空**（1,033／1,033） | **留空** |

上繳 09 第 5 節之三項未裁欄自此依 R-VL24(b) 之硬規則定案為**全部留空**。
`writeback_map_b1.tsv` **無須新增欄**（該三欄不寫入），故該檔**未改**（diff = 0）。

### 順帶實測之其他欄（供寫回包用，非本包受命項）

| 欄 | 實測 | b1 之採用 |
|---|---|---|
| **S** Functional Safety | `NA`×389＋空×1（pm_29）／`NA`×319（sw_update）／`NA`×5（popup）／**空×31（ics_management）** —— 多數本為 `NA`（713／745 列） | **採 `NA`** |
| **E** Test Case ID (TestRail) | **五本全空** | **留空** |
| **C** Requirement or Design ID (Polarion) | **五本全空** | **見第 5 節之牴觸** |

---

## 2. W-2 `trial_D_b1.xlsx` dry-run（**E79**）

`sandbox/wb_trial/trial_D_src.xlsx`（base 之 `copy2` 複本）→ openpyxl 計算層寫入
17 列 × 全欄 → `surgical_save` 出件 `trial_D_b1.xlsx`。**單次 117.4 秒**（與上繳 09 之 119.4 秒同量級，
證其成本與改動格數無關 —— 本次改 286 格，前次 3 格）。

`surgical_save` 回報：
`{'sheets_patched': {'Test Case Specification 測試用例規範': 286}, 'members_patched': ['xl/worksheets/sheet6.xml'], 'members': 48, 'differing': ['xl/worksheets/sheet6.xml'], 'dv_counts': {'xl/worksheets/sheet5.xml': (1, 0), 'xl/worksheets/sheet6.xml': (3, 1)}}`

### 強制複驗三斷言（R-VL24(a)）

| # | 斷言 | 實測 |
|---|---|---|
| 1 | **x14 逐字存活** | **True** —— `xl/worksheets/sheet6.xml` 之 `<x14:dataValidation …>` 節點與來源**逐字相同** |
| 2 | **member 集合相同** | **True**（**48** 個，無增無減） |
| 3 | **differing 僅目標分頁** | **`['xl/worksheets/sheet6.xml']`** —— 僅一個 |

解壓後總和 1,289,942 → **1,330,453**（+40,511，即 17 列內容之增量）。

### 回讀 17 列逐欄比對 JSON

| 項 | 實測 |
|---|---|
| 比對格數 | **286**（17 列 × 16–17 欄） |
| **不符** | **0** |
| B 欄公式抽驗（r10／r26） | `=IF(ISBLANK($D10),"",ROW()-9)`／`=IF(ISBLANK($D26),"",ROW()-9)` —— **未被值取代** |

**E79 全過。**

### 寫入之欄位（每列）

`C`／`D`／`F`／`G`／`H`／`I`／`J`／`K`／`L`／`M`／`N`／`O`／`P`／`R`／`S`／`AA`（＋10 列有 `AH`）。
`B`（公式）／`E`／`Q`／`T`–`Z`／`AB`／`AC`–`AG` **不寫**。
多行欄（`J`／`L`／`M`）採 `1. …\n2. …` 編號式，與 `sw_update` 交付本實測之格式一致。

---

## 3. W-3 lint 實跑（**E80**）

```
$ python3 scripts/lint036.py "features/vsm_v42/sandbox/wb_trial/trial_D_b1.xlsx" --profile vsm_v42
trial_D_b1.xlsx
  行計 A=0 B=0 C=1 D=0 E=0 F=0 G=0 H=0 I=0 I-sibling=0 J=0 K=0 L=0 M=0
       N=0 P=23 Q=0 R=0 T=0 U=6 V=0 I-cross=17 W=0
```

**上繳 09 之唯讀預檢在此全數被證實**：`J`／`K`／`Q`／`R`／`V`／`T`／`M`／`G` **八項實跑皆為 0**，
與預檢之 12 項全 0 一致。**預檢有效，但仍不足** —— 以下三項只有實跑才現形。

### 逐紅三分歸因

| 檢查 | 行計 | 分類 | 歸因 |
|---|---|---|---|
| **P** 訊號寫法不合 R-1 v3 | **23** | **已裁項（非缺陷）** | 見下 |
| **U** PENDING 佔位 | **6** | **工法產物（計數用）** | 見下 |
| **I-cross** 跨 req_id | **17** | **工法產物（警示器非判準）** | 見下 |
| **C** hedge（test_item 括號下半） | **1** | **b1 內容缺陷** | 見下 |

#### P = 23 —— **已裁項，非新缺陷**

23 列全為同一訊息：**「賦值缺 DBC `VAL_` 標籤 `(<label>)`（R-1 v3(a)／R-7）」**。
涉及之賦值去重後 **11 個**：

`$IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 2／3／4／5／6／8／9／10／11`（9 個）
＋ `$STATUS_CCAN3.VehicleSpeedVSOSig$ = 64／65`（2 個）

**兩者皆為上繳 05 §K **K-1** 所具名、且已由 **R-VL21(c)** 追認之處置**：
- `EPB_Maintenance_Fdbk` 之 `VAL_ 1486` 只定義 `0 "Initialization"` 與 `31 "SNA"`，
  2–11 **無 label**；依 §8.4.1 不造 label，寫 `= <raw>` 並於 `remarks` 揭露。
- `VehicleSpeedVSOSig` 為**物理量**（13 bit、factor 0.0625、單位 `Km/h`），
  其 `VAL_` 只有 `8191 "SNA"`；64／65 為 raw 值，**本無 label 可取**。

**即 lint 之檢查 P 不知道該裁決之存在** —— 其判準為「凡 `$…$ = <raw>` 必附 `(<label>)`」，
未含「DBC 無該值之 `VAL_` 時免附」之例外。
**本包不自修**（b1 已凍，且修法將是造 label，違 §8.4.1）。
**待裁**：(a) 認列為已裁例外（建議：`lint036` 之檢查 P 加「DBC 無 `VAL_` 者豁免」之判準，
或本線 profile 記入豁免清單）；(b) 或向上游索完整 `VAL_`（§K K-1 之原問）。

#### U = 6 —— 工法產物

`-058`／`-059`／`-060` 三列之 `proc` 與 `er` 各一，共 6，
全為 `PENDING: DR-VL4 <內部訊號名>`。lint 該項自載「**計數用**（A-PM16）」，非 FAIL。
**與上繳 05–08 所報之 PENDING 6 項逐項相符。**

#### I-cross = 17 —— 工法產物（警示器非判準）

17 列全為同一訊息：**「窗未完整宣告 —— 訖點無片語可抽，本列不參與 I-cross 比對
（R-SU33(b)：ER 須明載窗之起訖）」**，例：`起 availability-check → 訖 **未載**`。

即**並非 17 組跨列衝突，而是 17 列各自「未宣告觀測窗」故不參與比對**。
lint 該項自載「警示器非判準（R-SU34 v3(c)）—— 命中一律送人裁，不自動判 FAIL」。
**本線之 TC 不採觀測窗式書寫**（其 ER 為即時可觀察之訊號值與 UI 元件），
故無「窗」可宣告。**待裁**：本線是否需引入觀測窗宣告，或於 profile 記明本檢查對本線不適用。

#### C = 1 —— **b1 內容缺陷（唯一一項）**

| 列 | TC ID | req_id | 欄位 | 說明 | 片段 |
|---|---|---|---|---|---|
| 23 | `NR1L-VSM42-014` | `SWE1-VC-EPBMaintenanceMode-057` | `test_item`（括號下半） | **hedge `'successfully'`** | `(Fdbk = 11: exit completed successfully)` |

**性質**：IN §4.3 明列 hedge（`properly`／`successfully`／`within reasonable time`）為禁用；
本包之括號下半用了 `successfully`。**此為本執行層於上繳 05 生成時所造**，
05–08 四輪之機讀自檢**未含 hedge 檢查**（C 項不在我的 14 項內），故未被攔下。

**修法已備妥（一列，未施行）**：括號下半改為
`(Fdbk = 11: exit process reported as complete)` ——
去 hedge、保留與 `-054`／`-055`／`-056` 之區分度（E39 之括號不同文要求）。

**未施行之理由**：**b1 已凍結（R-VL23(d)：此後任何變更須新裁決）**，且該條不在本包修訂範圍
（本包為 dry-run，下放包明定「內容缺陷者逐列引出交裁，不自修」）。

### E80 判定

| 判準 | 實測 |
|---|---|
| b1 內容缺陷數 | **1** |
| 「0 則直接可請 Pei 授權寫回」 | **不成立** —— 須先裁該一項 |

---

## 4. E78–E81 對照

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| **E78** | W-1 | 三本×三欄之分布表；結論逐欄 | **五本**（樣本代換已報）×**九欄**（Q／AB／車型七欄）；1,033 列**全空**；結論三欄皆**留空** | **過** |
| **E79** | trial_D 複驗 | x14 逐字存活；member 48；differing 僅 sheet6；回讀 17×全欄 = JSON | **四項全中**；回讀 286 格**不符 0** | **過** |
| **E80** | lint | 全文＋逐紅三分歸因；內容缺陷數 | 全文與三分歸因見第 3 節；**內容缺陷 = 1** | **不為 0** |
| **E81** | 禁區 | `sandbox/base/` sha 不變；b1 35 檔 cmp 0 | base sha256 = `6372fb6b…825b2`（**不變**）；b1 凍結檔表 **34 檔複驗不符 0**（第 35 檔 `INDEX.md` 自指不入表，亦未動） | **過** |

---

## 5. **一項與交付慣例直接牴觸者（新發現，須先裁）**

### 實測

| 交付本 | D 欄（`Requirement or Design ID`）首列值 | C 欄（Polarion） |
|---|---|---|
| `power/pm_29` | `'SWE-PM-001'` | **空**×390 |
| `ics_management` | `'SWE-ICS-001'` | **空**×31 |
| `sw_update` | `'SWE1-FOTA-003'` | **空**×319 |
| `popup(output)` | `'SWE1-POP-002-01'` | **空**×5 |

**四本一律：D 欄放 SWE-Requirement ID（037 自身之 ID），C 欄全空。**

### 本線之明文

下放包 05 §一素材表逐字：
> 「`data/leaves.tsv` 之 `test_set = EPB Maintenance Mode` 17 列 ｜
> 母體（**req_id＝`SWE-Requirement ID`，D 欄值＝`Source Requirement ID`**）」

即本線被明令 **D 欄放 `Sys-RA-VF665_V42_VSM-{nnn}`（Source Requirement ID）**，
與四本交付慣例**相反**。

### 本包之處置

**依明文施作** —— `trial_D_b1.xlsx` 之 D 欄為 `Sys-RA-VF665_V42_VSM-723`…`-741`，
C 欄為 `SWE1-VC-EPBMaintenanceMode-044`…`-060`（四本慣例為空）。
**不自行調和**（FO 第 8.2 節）。

> **為何須先裁**：D 欄為交付簿之追溯主鍵。若慣例為準，本線 17 列之 D 欄與 C 欄**須對調**；
> 若本線明文為準，則本線之交付本與他線在同一欄放不同層級之 ID。
> **這是寫回一旦執行就會固化的差異**，且 `writeback_map_b1.tsv` 之欄名即依明文命名
> （`req_id_D`／`polarion_C`），改判須連同該檔一併改。
> R-VL24(b) 之「格式權威硬規則」只授權於**未裁**之三欄；D／C 為**已裁**，故不自行套用。

---

## 6. 獨立判斷

1. **一項樣本代換已回報**：`vehicle_setting`／`popup` 無 `delivered/`（第 1 節）。
2. **一項 b1 內容缺陷已具名、修法備妥、未施行**：`-057` 之 hedge（第 3 節 C）。
   **成因與 `-059` 之句內剪接同型** —— 皆為本執行層所造、且皆因**機讀自檢之項目不足**
   而歷經多輪未被攔下。**lint 有 23 項，我的自檢只有 14 項**；
   上繳 09 已列差集，本包是該差集第一次以實跑證實其代價。
3. **一項與交付慣例牴觸者，須先裁**（第 5 節）。
4. **兩項判準性問題交裁**（第 3 節）：lint 檢查 P 對「DBC 無 `VAL_`」無豁免；
   I-cross 對不採觀測窗式之 TC 全列判「窗未宣告」。
   **二者若不裁，本線每一批寫回後之 lint 都會帶著同樣的紅**。
5. **一項未做且指得出理由**：未修 `-057` —— b1 已凍（R-VL23(d)），且下放包明令
   「內容缺陷者逐列引出交裁，**不自修**」。
6. **試驗檔**：`wb_trial/` 現 6 件（`trial_src`／`A`／`B`／`C`／`trial_D_src`／`trial_D_b1`），
   依 R-VL24(d) 保留至寫回執行包結案。

---

## 7. `gate_all.py` 與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 506
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0
```

**(甲) `rulings_hash`** —— 依 R-VL13 記「待 Pei 重生」；R-VL15(c) 判準滿足。
**(乙) `canon_refs`** —— 含 `vsm_v42` 者 3 列，與上繳 02–09 逐字相同。
**(丙) `gates_tsv`** —— 與本線無關，先在。
**(丁) `lint_paths` = 4** —— 與本線無關；本包新增之兩件 xlsx 落 `sandbox/wb_trial/`，
`sandbox` 為合法落點，未新增違規（實測仍為前包之同四筆）。

**無一支肇因於本包之寫入。**

---

## 8. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `sandbox/wb_trial/trial_D_src.xlsx` | 自 `sandbox/base/` `copy2` |
| `sandbox/wb_trial/trial_D_b1.xlsx` | **dry-run 出件**（17 列、286 格、surgical） |
| `features/vsm_v42/docs/upstream/10_dryrun.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**`writeback_map_b1.tsv` 未改**（三欄結論為「留空」，不需新增欄）。

**未動**：**`sandbox/base/`（sha 不變）**、**`generated/b1_epb/` 全 35 檔（凍結件，34 檔 sha8 複驗相符）**、
`sandbox/b1/`（未建）、`delivered/`（未建）、`docs/fw036/RULINGS.sha.tsv`、
`docs/runtime/profiles/`、`scripts/`、`backend/`、`forms/`、`features/vsm_v43/`、
`features/vehicle_setting/`、`sources/`、`features/vsm_v42/` 之其餘檔、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 9. 待 Pei／分析層（**寫回之前提，四項**）

1. **`-057` 之 hedge `successfully`**（第 3 節 C）—— b1 已凍，修法備妥，**須新裁決**。
   **這是 E80 不為 0 的唯一原因。**
2. **D／C 欄與交付慣例之牴觸**（第 5 節）—— 四本交付簿 D 放 SWE ID、C 全空；
   本線明文相反。**寫回一執行即固化。**
3. **lint 檢查 P 之豁免**（第 3 節 P）—— 「DBC 無該值之 `VAL_`」是否豁免；不裁則每批皆紅 23。
4. **I-cross 對本線之適用性**（第 3 節 I-cross）—— 本線不採觀測窗式書寫。

承前未結：§K K-1〜K-6、DR-VL1／VL2／VL4 之送出、b2 批次序、台帳重生、
`wb_trial/` 六件之去留。
