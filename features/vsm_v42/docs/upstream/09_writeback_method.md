# 上繳包 09 — vsm_v42：寫回工法查證（**只查證與提案，未寫回**）

日期：2026-09-02　執行層：Claude Code　對應下放包：`docs/handoff/09_writeback_method.md`

## 結果分類

| 分類 | 內容 |
|---|---|
| 改對了 | W-1 盤點；W-2 三件試驗（含 surgical 對照件）；W-3 列對應表落檔；W-4 lint **本線首跑** |
| 核實無誤 | **E69–E72 全過**；`sandbox/base/` sha256 前後相同；b1 實內容對 lint 新增判準之唯讀預檢 **12 項全 0** |
| 正確地不動 | **未寫回**（`delivered/` 未建、`sandbox/base/` 未動）；試驗件全落 `sandbox/wb_trial/`；b1 凍結件一位元未動 |

**總判：工法已有定案級證據 —— `surgical_save` 可行、openpyxl 直寫不可行。單一建議案見第 4 節。**

---

## 1. W-1 存量工法盤點

### 全庫呼叫 `openpyxl` `save()` 之腳本（20 件，摘要）

| 路徑 | 出件方式 | 備註 |
|---|---|---|
| `features/amfm/scripts/write_back.py` | `wb.save()` | **歷史損毀源**（見下） |
| `features/home/scripts/write_back.py`、`features/media/scripts/write_back.py`、`features/driver_distraction/scripts/write_back.py` | `wb.save()` | privacy 之 R20-3 將該四件列為**隔離**（quarantined），明令不得複製 |
| `features/bed_lowering/scripts/write_back.py` | **`backend.xlsx_surgical.surgical_save`** | openpyxl 僅為計算層 |
| `features/privacy/scripts/write_back.py` | **`surgical_save`**（R20-5：自第一行即建於其上） | BLANK 簿；含 BLOCKED 列之寫入紀律 |
| `features/popup/scripts/gen_delivery.py` | **`shutil.copy2` ＋ sha256 相等** | 不改任何格之情形下，位元複製強於再跑一次 surgical |
| `features/power/scripts/{write_back_47,dryrun_write_back,dryrun_full_write_back,verify_writeback_path}.py`、`b02/apply*.py`、`b19/deliver.py`、`b72_pack.py`、`b73_pack.py` | 混用 | PM 線之多批工具 |
| `scripts/translate_xlsx.py`、`features/{home,media}/scripts/split_spec.py`、`features/power_moding/scripts/check_write_back.py` | `save()` | 非交付簿之工具 |

**`scripts/` 頂層無任何 `writeback*`／`export*` 之共用件** —— 寫回工具皆為 feature 私有。

### 損毀紀錄（各線 ANOMALIES 之 `x14`／`dataValidation`／`下拉` 命中數）

privacy 12／popup 10／user_profiles 8／power_moding 7／sxm 6／power 5／
audio_mgmt 3／home 3／amfm 2／comfort 2／projection 2／time_management 2／
media 1／ics_management 1／vehicle_setting 1／**vsm_v43 0**。

**具名之源頭**（`backend/xlsx_surgical.py` docstring 逐字）：
> 「Measured on the AMFM delivery (R16 §2): **21 zip members lost, 10 added,
> all six `x14:dataValidation` elements gone** — while the row contents were
> correct and lint was green, which is exactly why the loss went unseen.」

**canon 之禁令**：**R-G3**（`FEATURE_ONBOARDING.md:719／761`，源 A-UP09）
—— `framework.md` 範例禁用 `openpyxl` + `wb.save()`；
另 `:1074` 明載「`sandbox/<tag>/` 為 xlsx 唯一可改之處」。

**本線之相關性**：`feature.yaml` 之 `design_method` 欄為 **R 欄**，
其下拉正是 x14 擴充（R-G1 註／A-UP09）。**寫回若走 openpyxl `save()`，該下拉必失。**

---

## 2. W-2 x14 DV 保全實測（**E69**）

試驗件全落 `features/vsm_v42/sandbox/wb_trial/`，來源為 `sandbox/base/` 副本之複本。

| 件 | 作法 | zip members | `x14:dataValidation` | classic `dataValidation` |
|---|---|---|---|---|
| `trial_src.xlsx` | 來源（＝base 之位元複本） | **48** | **1** | 4 |
| `trial_A_nochange.xlsx` | openpyxl load → **不改任何值** → `save()` | **47**（−1） | **0**（−1） | 4 |
| `trial_B_written.xlsx` | openpyxl 寫 D10／I10/R10 → `save()` | **47**（−1） | **0**（−1） | 4 |
| **`trial_C_surgical.xlsx`** | openpyxl 計算層 ＋ **`surgical_save`** | **48** | **1** | 4 |

> **試驗 A 之意義**：**連一格都不改，只是開啟再存檔，x14 就沒了。**
> 損失不繫於「改了什麼」，而繫於「用什麼出件」。

### x14 節點之 XML 逐字斷言（非計數）

| 件 | `xl/worksheets/sheet6.xml` 之 x14 節點 |
|---|---|
| 來源 | `<x14:dataValidation type="list" allowBlank="1" showInputMessage="1" showErrorMessage="1" xr:uid="{069AE546-9178-46EB-A5DA-0FFC0CFAB1E5}"><x14:formula1><xm:f>下拉選單!$A$1:$A$9</xm:f></x14:formula1><xm:sqref>R10:R1411</xm:sqref></x14:dataValidation>` |
| **surgical** | **逐字相同**（含 `xr:uid` 之 GUID、`sqref` 之 `R10:R1411`） |
| openpyxl | **無 `x14:dataValidation` 節點** |

即 R 欄 design_method 之下拉在 surgical 出件中**連 GUID 與範圍都原樣保留**；
openpyxl 出件中該節點**不存在**（下拉不可用）。

### 檔案大小之差（補查，良性 —— 上繳後複驗所見，據實補記）

| 項 | `trial_src.xlsx` | `trial_C_surgical.xlsx` | 差 |
|---|---|---|---|
| **檔案大小** | 200,650 | **169,013** | **−31,637（−15.8%）** |
| 壓縮後總和 | 192,550 | 162,745 | −29,805 |
| **解壓後總和** | 1,289,942 | **1,290,181** | **+239** |
| 解壓內容逐 member 不同者 | — | `xl/worksheets/sheet6.xml` **一個** | — |
| `compress_type` 之集合 | `{0, 8}`（STORED＋DEFLATE 混用） | `{0, 8}`（相同） | — |

**判讀**：**解壓後之內容只有目標分頁不同**，且其增量 **+239 bytes** 恰為寫入三格所增；
檔案小 31 KB 純為**壓縮率差異**（`zipfile` 重封時之 deflate 參數與原產出工具不同），
`compress_type` 之混用型態則相同。**不影響任何內容不變量。**

> **據實記明**：此差在上繳初稿未列 —— 初稿只比了 member 集合與逐 member 內容，
> 未比檔案大小。15.8% 之落差是覆核者必問之項，補查後為良性，補記於此。
> **寫回包之驗證清單應含「解壓後總和 ＋ 逐 member 內容」而非檔案大小** ——
> 以檔案大小為不變量會誤判。

### 來源 ↔ surgical 之 zip member 逐一比對

| 項 | 結果 |
|---|---|
| member 集合相同 | **True**（只在來源 0／只在出件 0） |
| **逐位元不同之 member** | **`xl/worksheets/sheet6.xml` 一個**（即被改之目標分頁） |

`surgical_save` 之回報：
`{'sheets_patched': {'Test Case Specification 測試用例規範': 3}, 'members_patched': ['xl/worksheets/sheet6.xml'], 'members': 48, 'differing': ['xl/worksheets/sheet6.xml'], 'dv_counts': {'xl/worksheets/sheet5.xml': (1, 0), 'xl/worksheets/sheet6.xml': (3, 1)}}`

### 回讀（寫入之三格 ＋ 公式欄）

| 格 | 值 |
|---|---|
| `D10` | `'TRIAL-REQ-001'` |
| `I10` | `'trial row'` |
| `R10` | `'功能測試 (Functional based ; no specific technique)'` |
| `B10`（公式欄，應未動） | `=IF(ISBLANK($D10),"",ROW()-9)` **原樣保留** |

**寫得進、讀得出、公式未被值取代。**

### E70 —— `sandbox/base/` 一位元不動

| 時點 | sha256 |
|---|---|
| 本包開始前 | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |
| 本包結束後 | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |

**相同。E70 過。**

---

## 3. W-4 lint 首跑（**E72**，本線史上第一次）

```
$ python3 scripts/lint036.py "features/vsm_v42/sandbox/wb_trial/trial_C_surgical.xlsx" \
      --profile vsm_v42 --report-dir <scratchpad>/lint
trial_C_surgical.xlsx
  -> trial_C_surgical__vsm_v42_17d176bf_20260902.md
  行計 A=0 B=0 C=0 D=0 E=0 F=0 G=1 H=0 I=1 I-sibling=0 J=1 K=0 L=0 M=4
       N=0 P=0 Q=0 R=1 T=0 U=0 V=0 I-cross=1 W=0
```

報告頭：`資料列數 1`／`sheet: Test Case Specification 測試用例規範`（header 第 9 列）／
`L 閾值 50`／`profile: vsm_v42（P 採 R-1 v3；另跑 Q／R／T）`。**總計行計 9。**

### 逐紅歸因（**9 項全為假資料列之產物，非工法或內容缺陷**）

| 檢查 | 行計 | 明細 | 歸因 |
|---|---|---|---|
| G Test Set 空值 | 1 | 列 10 `test_set` 為空 | 試驗件只填 D／I／R 三格，未填 H |
| I test_item 括號下半缺失 | 1 | `trial row` | 假資料無括號下半 |
| J 行首大寫 | 1 | 首字小寫 `'trial'` | 假資料 |
| M 空欄三態 | 4 | `pre`／`proc`／`er`／`spec` 空欄 | 假資料未填 |
| R Pre-Condition 版面 | 1 | — | 空 PC 之衍生 |
| I-cross | 1 | 單列自比 | 警示器非判準（R-SU34 v3(c)） |

**P（訊號寫法 R-1 v3，profile 專屬）= 0、Q = 0、V = 0、K = 0、N = 0、L = 0、T = 0、U = 0。**

### **本次首跑之真正收穫 —— 文字形自檢未涵蓋之檢查清單**

上繳 05–08 之機讀自檢共 14 項；lint 有 **23 項**。**差集逐一列出**：

| lint 檢查 | 文字形自檢是否涵蓋 |
|---|---|
| **J 行首大寫** | **未涵蓋** |
| **K CJK 字元（入簿欄）** | **未涵蓋** |
| **Q 不可見字元（NBSP／全形空格／行尾空白）** | **未涵蓋** |
| **R Pre-Condition 版面（未編號行／多條件並列）** | **未涵蓋** |
| **V 行首空白** | **未涵蓋** |
| **T PENDING 說明非英文** | **未涵蓋** |
| **M 空欄三態** | **未涵蓋** |
| **G Test Set 空值** | 部分（自檢查其與 framework 一致，未查空） |
| **P 訊號寫法 R-1 v3**（profile 專屬） | 部分（E42 只查 `$…$` 是否可回溯解得，未查格式） |
| **I-cross／W** | 未涵蓋（皆為待人裁之警示器，非 FAIL） |
| A／B／C／D／E／F／H／I／I-sibling／L／N／U | 已涵蓋（對應 E39–E45） |

### b1 實內容對上列新增判準之**唯讀預檢**（17 條，非 lint 實跑）

| 判準 | b1 實測 |
|---|---|
| J 行首小寫（四欄逐行） | **0** |
| J test_item 上半／下半首字小寫 | **0**／**0** |
| K CJK 於入簿四欄／`test_item`／`remarks` | **0**／**0**／**0** |
| Q 不可見字元・行尾空白 | **0** |
| V 行首空白 | **0** |
| G Test Set 空 | **0** |
| M 空欄三態 | **0** |
| T PENDING 說明非英文 | **0** |
| R Pre-Condition 多條件並列（`;` 或雙 `and`） | **0** |

**十二項全 0。** 惟此為**執行層以同判準自寫之預檢，非 lint 實跑** ——
`P`／`I-cross`／`W` 三項因需簿內脈絡（跨列、觀測窗）**無法以文字形預檢**，
**須待寫回後之 lint 實跑方能確認**。據實揭露，不以預檢代實測。

---

## 4. 工法提案（**E71**，附可行性實測）

### 單一建議案：**openpyxl 為計算層 ＋ `backend.xlsx_surgical.surgical_save` 出件**

| 要件 | 依據 |
|---|---|
| 可行性 | 本包試驗 C **實測通過**（members 48 保住、x14 節點逐字保住、只有目標分頁 XML 變動、寫入可回讀、B 欄公式未被值取代） |
| 既有先例 | `features/privacy/scripts/write_back.py`（R20-5，BLANK 簿，與本線同型）、`features/bed_lowering/scripts/write_back.py` |
| 內建防線 | `verify_structure` 對「zip member 集合改變／DV 計數改變／非目標 member 有差異」**raise 而非 warn**（模組 docstring 明載，且屬 canon §0 第 3 項之 invariant breach） |
| 與 canon 之相容 | 滿足 **R-G3**（不以 openpyxl `save()` 出件）與 `:1074`（xlsx 只在 `sandbox/<tag>/` 改） |

**實作要點（提案，非本包執行）**：
1. 自 `sandbox/base/` 複製至 `sandbox/b1/`，於該複本上作業；`base/` 全程唯讀。
2. openpyxl 載入 → 依 `data/writeback_map_b1.tsv` 逐列填格 → `surgical_save(wb, src, out)`。
3. 出件後**強制**：`zipfile` 直讀複驗 x14 節點逐字、member 集合、`differing` 只含目標分頁。
4. **回讀驗證**：自出件讀回 17 列，逐欄比對 `generated/b1_epb/*.json`；
   「寫不進去或讀不回來就不算寫」（bed_lowering docstring 之原則）。
5. 交付候選以 **`shutil.copy2` ＋ sha256 相等**產出（popup `gen_delivery.py` 之作法），
   **不再跑一次 surgical** —— 位元相同比「這次也沒壞」強。

**一項須先解之工程事實**：`surgical_save` 於本簿耗時 **119.4 秒**（單次，寫 3 格）。
其成本在 `diff_cells` 之全簿逐格 diff（本簿 `R10:R1411` 之範圍與 9 分頁）。
17 列之寫回預期同量級（diff 成本與改動格數無關）。**可接受，但寫回包應預期單次執行約 2 分鐘**，
不宜置於須反覆重跑之迴圈。

### 備案（**本包不建議，僅備載**）

**XML 手術式（自寫）** —— zip 解包、直接改 `sheet6.xml` 之 `<c>` 節點、原樣回封。
**不建議之理由**：`backend.xlsx_surgical` 已是同一手法之**共用實作**且帶 `verify_structure`；
自寫等同重造，且會失去 `_fix_dimension`／`shift_ref_list`／樣式衍生等既有處理。
**僅在 `surgical_save` 於本簿出現 `StructureError` 時才考慮** —— 本包實測**未出現**。

---

## 5. W-3 列對應與 TC ID 提案

`features/vsm_v42/data/writeback_map_b1.tsv`（**17 列**，8 欄）已落檔。

| 項 | 提案 |
|---|---|
| 起始列 | **列 10**（header 第 9 列；BLANK 簿，privacy 之先例同） |
| 佔用列 | **10–26**（17 列） |
| TC ID（F 欄） | **`NR1L-VSM42-001` – `NR1L-VSM42-017`**，依 `INDEX.md` 之序（`-044` → 001 … `-060` → 017），依 `feature.yaml` 之 `write_back.tc_id_format`（R-VL7） |
| D 欄 | `Source Requirement ID`（`Sys-RA-VF665_V42_VSM-{nnn}`）—— 下放包 05 §一 明載 |
| C 欄 | `SWE-Requirement ID`（Polarion 側）—— 建議填 `SWE1-VC-EPBMaintenanceMode-{nnn}` |
| **凍結 sha8** | **不記於 Remarks**（依下放包建議）；記於 `writeback_map_b1.tsv` 之 `src_sha8` 欄 |

### 欄位映射（`feature.yaml` columns 21 鍵 → 來源）

| 欄 | 鍵 | 來源 |
|---|---|---|
| B | `no` | **不寫** —— 既有公式 `=IF(ISBLANK($D{r}),"",ROW()-9)` 自動編號（試驗 C 已證公式未被覆蓋） |
| C | `polarion_id` | `req_id`（SWE-Requirement ID） |
| **D** | `req_id` | `Source Requirement ID` |
| E | `testrail_id` | **留空** —— 全為 NEW，無舊 ID（popup §三 之先例） |
| **F** | `tc_id` | `NR1L-VSM42-{n:03d}` |
| **G／H** | `test_group`／`test_set` | `Vehicle Setup Management R1 Low`／`EPB Maintenance Mode`（R-VL8：BLANK 故 `fill_test_group_set: true`） |
| **I–N** | `test_item`／`pre_conditions`／`input_test_data`／`test_procedure`／`expected_result`／`spec_reference` | JSON 十鍵；多行欄以換行接合、逐項編號 |
| O | `tc_ref_id` | `NEW`（`feature.yaml` `write_back.tc_ref_id_value`） |
| **P** | `priority` | JSON `priority` |
| Q | `estimated_test_time` | **留空** —— popup R-POP22 之先例；本線未裁，**提案留空並請分析層確認** |
| **R** | `design_method` | JSON `design_method`（下拉逐字；x14 下拉須存活） |
| S | `functional_safety` | **提案留空** —— DECISIONS §3 已裁「ruled source 無 ASIL/FTTI 欄，安全層不入 trace chain」 |
| **V** | 車型欄 `VF(ProMaster)637 Atl-Mi` | **提案填適用標記** —— 本線 EE = ATL-Mi（profile 身分段）；**填什麼字**未裁，請分析層定 |
| T／U／W–Z | 其餘車型欄 | **留空** |
| **AA** | `author` | `PeiPYHsu`（`write_back.author_value`） |
| AB | `test_version` | **提案留空**，未裁 |
| AC–AG | 執行欄 | **留空**（生成階段不寫） |
| **AH** | `remarks` | JSON `remarks`（10 條有值；含 VAL_ 缺值揭露、UI 元件名來源、`-054` 歸類依據） |

**三項未裁請分析層定**：Q（Estimated Test Time）、V（車型欄之填法）、AB（Test Version）。

---

## 6. 預期數字 E69–E72

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| **E69** | W-2 斷言 | 兩件試驗各附 zip member 數與 x14 節點 XML 證據 | **三件**（另加 surgical 對照件），member 數與 x14 節點 XML **逐字**列於第 2 節 | **過** |
| **E70** | `sandbox/base/` | 一位元不動（cmp） | sha256 前後**相同** | **過** |
| **E71** | 工法提案 | 附可行性實測 | 建議案經**試驗 C 實測通過**；備案附不建議之理由 | **過** |
| **E72** | lint 首跑 | 輸出全文＋逐紅歸因 | 行計全文 ＋ 9 項逐項歸因（**全為假資料產物**）＋ 未涵蓋檢查差集 | **過** |

---

## 7. 獨立判斷

1. **一項超出下放包字面而本包做了，並據實標明**：W-4 除假資料件之 lint 實跑外，
   另以**同判準**對 b1 實內容做**唯讀預檢**（12 項全 0）。
   此非 lint 實跑，不得代之；作用是讓分析層在授權寫回前知道風險面。
2. **三項無法以文字形預檢**：`P`（訊號寫法 R-1 v3）、`I-cross`、`W` ——
   皆需簿內脈絡。**寫回後之 lint 實跑仍可能出紅**，尤以 **P 為 profile 專屬且本線首次適用**。
   **這是 b1 凍結後仍可能被迫回頭改的唯一已知風險**（改須新裁決，R-VL23(d)）。
3. **一項工程事實須入寫回包**：`surgical_save` 於本簿單次 **119.4 秒**。
4. **一項未做且指得出理由**：未以 b1 實內容建試驗簿再跑 lint ——
   下放包 W-4 明定「以 W-2 之假資料試驗件跑」，且該作法等同預演寫回，超出「不寫回」之界。
   **若分析層要在授權前看到 P／I-cross／W 之真實結果，需另行授權建一次 b1 內容之試驗簿。**
   **建議如此** —— 其成本一次 2 分鐘，而其揭露之風險正是第 2 項所指者。
5. **試驗件之去留**：`sandbox/wb_trial/` 四檔（`trial_src`／`A`／`B`／`C`）**保留**作為證據；
   若分析層要求清除，請明示。

---

## 8. `gate_all.py` 與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 506
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0
```

**(甲) `rulings_hash`** —— 依 R-VL13 記「待 Pei 重生」；依 R-VL15(c) 判準滿足。

**(乙) `canon_refs` 506** —— 含 `vsm_v42` 者 3 列，與上繳 02–08 逐字相同。

**(丙) `gates_tsv`** —— 與本線無關，先在。

**(丁) `lint_paths` = 4** —— 與本線無關，四筆與前七包相同。
**惟本包新增 `sandbox/wb_trial/` 之四個 `.xlsx`** ——
`lint_paths` 之合法落點為 `['delivered', 'inputs', 'sandbox']`，
`sandbox/wb_trial/` 在 `sandbox` 之下，**未新增任何一筆違規**（實測 4 筆與前包逐字相同）。

**無一支肇因於本包之寫入。**

---

## 9. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `features/vsm_v42/sandbox/wb_trial/trial_src.xlsx` | 自 `sandbox/base/` 複製（試驗來源） |
| `features/vsm_v42/sandbox/wb_trial/trial_{A_nochange,B_written,C_surgical}.xlsx` | 三件試驗產物 |
| `features/vsm_v42/data/writeback_map_b1.tsv` | **新建**（17 列 × 8 欄） |
| `features/vsm_v42/docs/upstream/09_writeback_method.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：**`sandbox/base/`（sha256 前後相同）**、**`generated/b1_epb/` 全 35 檔（b1 凍結件）**、
`delivered/`（未建）、`docs/fw036/RULINGS.sha.tsv`、`docs/runtime/profiles/`、`scripts/`、
`backend/`、`forms/`、`features/vsm_v43/`、`features/vehicle_setting/`、`sources/`、
`features/vsm_v42/{RULINGS.md, DATA_REQUESTS.md, ANOMALIES.md, DECISIONS.md, feature.yaml,
framework.md, data/ 之其餘}`、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 10. 待 Pei／分析層

1. **授權寫回執行包**：採建議案（openpyxl 計算層 ＋ `surgical_save`）與否。
2. **三個未裁欄位**：Q（Estimated Test Time）、**V（車型欄之填法）**、AB（Test Version）。
3. **是否先建一次 b1 內容之試驗簿跑 lint**（第 7 節第 4 項，**建議做**）——
   `P`／`I-cross`／`W` 三項只有這樣才會現形，而它們是 b1 凍結後被迫回頭改的唯一已知風險。
4. **`sandbox/wb_trial/` 四件試驗檔之去留。**
5. 承前：b2 批次序、§K K-1〜K-6、DR 送出、台帳重生。
