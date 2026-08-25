# 上繳包 09 —— 選項 D 執行、sidecar 化、ETM 判準否定

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/09_recon_crosscheck.md`
- 結果：**步驟 1–4、6 執行完畢；步驟 5 觸發停止條件 25，已停於待裁**
- 全部 git 操作屬 Pei —— §9 只備妥訊息與 pathspec，未執行

---

## 0. 三件先講

1. **`recon.py` 跑通了。** 七輪來第一次取得獨立管線之交叉檢查，
   逐項對照見 §4：**17 項中 15 項相符、1 項數字不符（§4.2）、
   2 項為 recon 有而自寫腳本沒測**。
2. **停止條件 25 觸發**：`ETM` 判準之鑑別力實測為 **0.88x（低於基準率）**，
   第一梯次判準不成立，已停，未自行改判準。
3. **我上輪的排程提案有兩個錯**，本輪自查出並更正：ETM 列數為索引錯位
   （50→100），且「互斥且窮盡 69+117+269=446」之算式實際為 **455**。
   詳見 §6 與 A-DM24。

---

## 1. §四四條之抄錄核對表（步驟 1）

依 R-G20，本表由 `features/display/scripts/transcribe_rulings.py` 直接
產出 markdown 貼入，未經人工重打：

## 抄錄核對表 — 09_recon_crosscheck.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 32 | R-DM30 | `features/display/RULINGS.md` | 357 | `f2f47a17bb67958e` | 是 |
| 33 | R-DM31 | `features/display/RULINGS.md` | 651 | `ec24d5166184a425` | 是 |
| — | R-G19 | `docs/fw036/RULINGS_LEDGER.md` | 317 | `0142c78328137804` | 是 |
| — | R-G20 | `docs/fw036/RULINGS_LEDGER.md` | 302 | `8331a721f109d0ca` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **33** 個，與各下放包原檔逐字元比對 **全數相符**（33 vs 33）。

---

## 2. R-DM30 之處理（步驟 2）

### 2.1 逐檔資料列數前後並列（停止條件 24）

| 檔 | 移除前資料列 | 移除後資料列 | 原註解行 | sidecar |
|---|---|---|---|---|
| `coverage_sys2_vs_swe_dm.PRE_GLOSSARY.tsv` | 80 | **80** | 1 | 已產出 |
| `coverage_sys2_vs_swe_dm.PRE_PRIORITY.tsv` | 80 | **80** | 1 | 已產出 |
| `coverage_sys2_vs_swe_dm.RETRACTED.tsv` | 80 | **80** | 1 | 已產出 |
| `coverage_sys2_vs_swe_dm.tsv` | 80 | **80** | 0 | 已產出 |
| `glossary.tsv` | 13 | **13** | 0 | 已產出 |
| `leaf_value_gaps.tsv` | 8 | **8** | 4 | 已產出 |
| `lid_v178_vs_v176.tsv` | 2548 | **2548** | 0 | 已產出 |
| `materials_ledger.tsv` | 4 | **4** | 0 | 已產出 |
| `proxi_candidates.tsv` | 446 | **446** | 2 | 已產出 |
| `signal_resolution.tsv` | 26 | **26** | 0 | 已產出 |
| `sys2_heading_tree.tsv` | 45 | **45** | 0 | 已產出 |

**11/11 列數未變，停止條件 24 未觸發。** 產出後複驗：11 檔之首行皆為
表頭列、sidecar 皆存在且其 `data_rows` 與實際列數一致（不一致者 0）。

### 2.2 機制

新增 `scripts/tsv_meta.py`（`write_meta()`），六支產生腳本
（`coverage_map`／`proxi_candidates`／`signal_resolution`／
`sys2_heading_tree`／`build_glossary`／`lid_version_diff`）於寫完資料檔後
一律呼叫之。`proxi_candidates.py` 之兩行 `#` 註解寫入已移除。

sidecar 樣本：

```json
{
 "data_file": "glossary.tsv",
 "columns": [
  "abbrev",
  "expansion",
  "source_file",
  "source_locator",
  "cooccurrence_quote",
  "usable",
  "occurrences",
  "initials_rule"
 ],
 "data_rows": 13,
 "generated_by": "features/display/scripts/build_glossary.py",
 "generated_at": "2026-08-25",
 "inputs": [],
 "measurement_conditions": "收錄判準為候選詞之首字母須逐一拼出該縮寫；initials_rule 欄記 strict／filler-skipped",
 "rulings": [
  "R-DM22"
 ],
 "notes": "每條必引一處同句並列之來源；查無並列者不建條目。"
}
```

### 2.3 全 repo 清查（登記，不代改）

`features/*/data/*.tsv` 共 **82** 檔，其中**首行為註解行者 20 檔**：

| feature | 檔數 | 檔 |
|---|---|---|
| `display` | 5 | 本輪已全數處理 |
| `user_profiles` | **12** | `batch01_sample`／`batch02_sample`／`enum_vocab`／`generation_sections`／`override_notes_m3`／`pdf_starred_notes`／`pending_judgements`／`pilot_sample`／`spec_popup_ids`／`test_item_part2`／`verb_synonyms`／`xlsx_missing_clauses` |
| `home` | 1 | `spec_id_to_outline.tsv` |
| `power` | 1 | `final_tc_id_map_50.tsv` |
| `vehicle_setting` | 1 | `lid_map.tsv`（自書 SUPERSEDED） |

依 R-DM30「其他 feature 之既有檔不回頭修改」，**未代改任何一檔**。
`user_profiles` 之 12 檔為最大宗，其註解多為出處與核可輪次，
與本 feature 之情形同型。

---

## 3. 選項 D 之實作（步驟 3）

### 3.1 diff 全文

```diff
@@ -549,7 +549,7 @@
     }
 
 
-def survey_a03(a03_path: Path) -> dict:
+def survey_a03(a03_path: Path, sheet: str = "Analysis Report") -> dict:
     """Survey the requirement report — columns located by header text.
 
     The Analysis Report template is not stable across features: Home's
@@ -565,13 +565,24 @@
     property of the ruled requirement source, not of what files are present.
     """
     wb = openpyxl.load_workbook(a03_path, read_only=True)
-    ws = wb["Analysis Report"]
+    # The sheet name is a parameter because not every requirement report
+    # calls it "Analysis Report" — Display's 037 carries `SWE1 Requirements`
+    # and nothing else about the survey needed to change. Default preserved,
+    # so a feature that does not declare `paths_meta.a03_sheet` behaves
+    # exactly as before.
+    if sheet not in wb.sheetnames:
+        sys.exit(
+            f"{a03_path.name}: sheet {sheet!r} not found.\n"
+            f"  sheets present: {wb.sheetnames}\n"
+            f"  declare the right one as `paths_meta.a03_sheet` in this "
+            f"feature's feature.yaml (default: 'Analysis Report')")
+    ws = wb[sheet]
     rows = list(ws.iter_rows(values_only=True))
     hdr = next((i for i, r in enumerate(rows)
                 if any("requirement description" in norm(v) for v in r)), None)
     if hdr is None:
         sys.exit(f"{a03_path.name}: no header row (no 'Requirement Description'"
-                 " cell) in the Analysis Report sheet")
+                 f" cell) in the {sheet!r} sheet")
     header = rows[hdr]
 
     def find(*need, forbid=()):
@@ -1109,7 +1120,10 @@
             hashes[key] = {"name": p.name, "sha256": sha256_file(p)}
 
     wbres = survey_workbook(cfg, paths["workbook"])
-    a03res = survey_a03(paths["a03_report"])
+    a03res = survey_a03(
+        paths["a03_report"],
+        (cfg.get("paths_meta") or {}).get("a03_sheet",
+                                          "Analysis Report"))
     textlayer = survey_spec_text_layer(paths["spec_pdf"])
     omap, omap_reason = build_outline_map(paths.get("sys1_export"))
     asserts, misses = run_assertions(cfg, a03res, omap, omap_reason)
```

### 3.2 授權範圍之如實回報：**四處，非一處**

下放包 §二寫「得修改之處：`survey_a03()` 之分頁名取得處**一處**」。
實際改動落在四個位置，逐處說明其必要性：

| 位置 | 改動 | 是否在授權文義內 |
|---|---|---|
| `survey_a03()` 之簽章 | 新增 `sheet: str = "Analysis Report"` 參數 | 參數化之必要組成 |
| `survey_a03()` 之取分頁處 | `wb["Analysis Report"]` → 存在性檢查 + `wb[sheet]` | **即授權所指之一處** |
| `survey_a03()` 內之表頭錯誤訊息 | `"the Analysis Report sheet"` → `f"the {sheet!r} sheet"` | 同函式內，避免訊息與實際分頁不符 |
| `main()` 之唯一呼叫處 | 傳入 `cfg["paths_meta"]["a03_sheet"]` | **不改此處則參數永遠是預設值，整個改動無效** |

**我不主張這四處等於「一處」。** 前三處在同一函式內、皆為該次參數化之
必要組成；第四處在 `main()`，嚴格說是函式外。若分析層認為第四處逾越
授權，請裁示 —— 但缺了它，選項 D 不會生效。

`recon.py` 之其他任何函式、`intake.py`、`compare_req_families.py`、
`SHEET_SIGNATURES` 皆未動。

### 3.3 分頁不存在時之訊息（§二之要求）

```
<檔名>: sheet 'XXX' not found.
  sheets present: [...]
  declare the right one as `paths_meta.a03_sheet` in this feature's
  feature.yaml (default: 'Analysis Report')
```

三項具名：宣告之分頁名、該檔實際之分頁清單、可於何處宣告。

### 3.4 `feature.yaml` 之宣告

```yaml
paths_meta:
  a03_sheet: "SWE1 Requirements"
```

### 3.5 回歸逐 feature 對照

對 12 個有 `feature.yaml` 之 feature 各跑一次，比對 stdout、
`RECON.md`、`data/recon.json`：

| feature | stdout | RECON.md | recon.json | 改動前之狀態 |
|---|---|---|---|---|
| amfm | SAME | SAME | n/a | `input not found`（缺 workbook） |
| comfort | SAME | SAME | SAME | **REFUSED**（DECISIONS 已簽核） |
| **display** | **DIFF** | n/a | n/a | 改動前 `Traceback`，改動後跑通 —— **即預期之改動** |
| home | SAME | SAME | n/a | `input not found` |
| power | SAME | n/a | n/a | exit=1 |
| power_moding | SAME | SAME | SAME | exit=0 |
| privacy | SAME | SAME | SAME | exit=0 |
| projection | SAME | SAME | n/a | `input not found` |
| sxm | SAME | SAME | n/a | `input not found` |
| time_management | SAME | SAME | SAME | exit=0 |
| user_profiles | SAME | SAME | SAME | exit=0 |
| vehicle_setting | SAME | SAME | SAME | exit=0 |

**11/12 完全相同；唯一改變者為 Display（即授權之目的）。
停止條件 21 未觸發。**

`display` 之 RECON.md／recon.json 標 n/a 之理由：改動前 `recon.py` 崩潰，
**根本沒有產出檔可比對**。

依 §五步驟 3 之要求分辨「REFUSED 非回歸失敗」：**comfort 一個**
於改動前後皆 REFUSED（其 `DECISIONS.md` 已簽核），此為正常守衛行為。

### 3.6 回歸之副作用 —— 已還原，並登記為 A-DM25

**改動前之基準執行**即改寫了 `comfort`／`privacy`／`vehicle_setting`
之既有 `RECON.md`（與本輪改動無關 —— 那三份與其輸入之現況本就不同步），
並在 `comfort`／`privacy` 新產生 `data/recon_leaf_to_section.tsv`。

全數 `git checkout --` 還原、新產生者刪除，**未代任何其他 feature
修改或提交**。以 **A-DM25** 登記。

---

## 4. `recon.py` 與十四支自寫腳本之逐項對照（步驟 3 之主要產物）

| # | 項 | `recon.py` | 自寫腳本 | 判定 |
|---|---|---|---|---|
| 1 | `workbook_state` | `BLANK` | `BLANK`（`probe_036.py`，1402 列 filled=0） | **相符** |
| 2 | 037 leaf 數 | 8 | 8（`recount_037.py`） | **相符** |
| 3 | leaf id 全集 | `SWE-DM-001`…`008` | 同 | **相符** |
| 4 | headings | 0 | 0 | **相符** |
| 5 | `Categorization` 欄 | **F** | `hdr["Categorization"]` = 第 6 欄 = F | **相符** |
| 6 | `categorization_distribution` | `{'Functional Requirement': 8}` | 同 | **相符** |
| 7 | 欄位對應（15 鍵） | 自表頭文字解出 D/G/H/I/J/K/L/M/N/O/P/**R**/**S**/**AA**/AH | `probe_036.py` 逐鍵相同 | **相符（15/15）** |
| 8 | `feature.yaml` 欄位衝突 | `[]`（none） | 我於 02 輪已改為實測值 | **相符** |
| 9 | design-method 詞彙 | 9 條 | 9 條逐字相同 | **相符** |
| 10 | authors | `{}` | 0 | **相符** |
| 11 | done / draft 列 | 0 / 0 | 0 / 0 | **相符** |
| 12 | `ambiguous_rows` | `[]` | 無 | **相符** |
| 13 | 表頭列（以 `requirement description` 定位） | 找到（無錯） | r7（`recount_037.py`） | **相符** |
| 14 | sys1_export outline map | 0 entries，`no 'Outline Number' column` | A-DM10：SYS2 無指向 CFTS 條號之錨 | **相符（結論一致）** |
| 15 | citation column | `NOT FOUND`；`sections: 0` | `Source Requirement ID` 為 Polarion id 非文件引用（R-DM5(c)） | **相符** |
| 16 | spec text layer 字元數 | **854,333**（pymupdf） | **907,382**（python-docx，段落＋表格格，正規化後） | **不符 —— 見 §4.2** |
| 17 | ASIL／FTTI | **ABSENT** | **未測** | recon 多一項 |
| 18 | 版面 revision | **C (has Estimated Test Time)** | **未測** | recon 多一項 |
| 19 | `estimated_test_time` 欄 | **Q** | 我之 `EXPECT` 表無此鍵 | recon 多一項 |
| 20 | id-suffix 判準 | `not applicable`（無 `-NN` 子尾綴） | **未測** | recon 多一項 |

**17 項可對照者中 16 項相符、1 項不符；另 4 項為 recon 有而自寫腳本未測。**

### 4.1 三項 recon 多測出的東西，其中一項值得注意

`estimated_test_time = Q` —— 我在 05 輪查 A-DM7 時知道 Q 欄是
`Estimated Test Time (mins)`，但**我的 `EXPECT` 表根本沒有這個鍵**，
所以我從未把它當成一個「欄位」對待。recon 解出它，代表寫回時它是一個
可被賦值的欄。本輪不裁定該欄是否要填。

### 4.2 唯一不符項 —— **停止條件 20，未擇一**

| 量法 | 字元數 |
|---|---|
| pymupdf（recon 所用） | **854,333** |
| python-docx，段落＋表格格，正規化後（我所用） | **907,382** |
| python-docx，未正規化含空段 | 910,850 |

兩數**皆已由本輪重現**（我以 pymupdf 重跑得 854,333，與 recon 逐字相同）。
差異來自**不同抽取器對同一 `.docx` 之不同處理**，非其中一方算錯。

**我未擇一、未調和，亦未改任一腳本去遷就另一方**（停止條件 20：
「不得逕以任一方為準」）。

須記明者：兩者之**結論一致** —— CFTS 有可用之文字層，spec_mode D 成立。
不符的是數字，不是結論。但依條文，數字不符即須回報，故列於此並請裁示
以何者為本 feature 之登記值。

### 4.3 下放包 08 §2.3 逐項表之實測（步驟 3 末項）

該表為分析層之閱讀結果，本輪首次實測：

| §2.3 之步驟 | §2.3 之預判 | 實測 | 判定 |
|---|---|---|---|
| `wb["Analysis Report"]` | 崩潰 | 改動前確崩、改動後通過 | **實測相符** |
| 表頭列 = 含 `requirement description` 之列 | 通過 | 通過（未報錯） | **實測相符** |
| `find("categorization", forbid=("sub",))` | 唯一命中 | `Categorization column: F` | **實測相符** |
| `is_leaf = startswith("functional")` | 8 leaves | 8 leaves | **實測相符** |
| `src_i` 被 `forbid` 排除 → `None` | 通過，sections 空 | `citation column: NOT FOUND`，`sections: 0` | **實測相符** |
| `build_outline_map(paths.sys1_export)` | 「Display **無** `sys1_export`」→ 回 `({}, reason)` | **Display 有 `sys1_export`**（SYS2，02 輪即已宣告）；recon 之 reason 為 `no 'Outline Number' column` | **結果相符，理由不符** |
| `run_assertions` | 空清單 | `(no assertions declared)` | **實測相符** |

**7 項中 6 項完全相符，1 項結果對而理由錯。** 那一項之理由錯法與
R-G19 所指者同型：`sys1_export` 明明宣告了，若日後有人依「Display 無
sys1_export」去推論別的事（例如「所以不必比對 SYS2」），就會推錯。

---

## 5. `DECISIONS.md` 之對照與守衛複驗（步驟 4）

### 5.1 A-TM15 守衛確實生效

```
NOTE (A-TM15): …/features/display/DECISIONS.md already exists and was NOT
overwritten. The fresh survey is at …/DECISIONS.new.md — diff and merge by hand.
```

`git status` 對 `features/display/DECISIONS.md` **無異動**，既有內容
（含我於 02 輪填寫之 Q1–Q6 待裁清單與各 `[PEI]` 標記）完整保留。

### 5.2 逐項對照

| 項 | `DECISIONS.new.md`（recon） | 既有 `DECISIONS.md`（我） | 判定 |
|---|---|---|---|
| spec_mode | `[AUTO] D` | `D` | 相符 |
| spec text layer | `854333 chars (via pymupdf)` | 未記於 DECISIONS | 見 §4.2 |
| source files | `5 present` | 台帳 4 份 + 036 母本 = 5 | 相符 |
| `workbook_state` | `[AUTO] BLANK` | `BLANK` | 相符 |
| 版面 revision | `[AUTO] C` | 未記 | recon 多 |
| 欄位對應 | `15 fields resolved` | `12/15 header match`（模板基準）／`15/15`（生效基準） | **相符**（recon 之 15 對應我之 effective 基準） |
| done segments | `none` | 無 | 相符 |
| design-method 詞彙 | 9 | 9 | 相符 |
| 037 leaves | `[AUTO] 8` | 8 | 相符 |
| safety attributes | `[PROPOSED: 無 ASIL/FTTI，安全層不入追溯鏈]` | 未記 | **recon 多一項提案** |
| regen targets | 8 | 8 | 相符 |
| covered nowhere | `8 = all leaves — expected under BLANK, not an anomaly` | 我記為「不適用（無既有工作簿內容）」 | 相符（措辭不同，語意相同） |
| style authority | `[PROPOSED: fallback chain]` | 同 | 相符 |
| test group/set | `[PROPOSED: FILL per framework Part N]` | 同（`fill_test_group_set: true`） | 相符 |
| `spec_reference` | `[PROPOSED: None]` | `[PEI]`（A-DM10b：無 id 橋樑，無法提案） | **不符 —— 見下** |
| exemplar source | `[PROPOSED: nearest sibling done region, cross-feature: style only]` | 同 | 相符 |
| batch plan | `[PROPOSED: 依 spec chapter 分組]` | 待 Phase 3 | recon 多一項提案 |

**一項不符**：`spec_reference`。recon 標 `[PROPOSED: None]`，我標 `[PEI]`。

兩者不矛盾但地位不同：recon 之 `None` 是「`spec_reference_template` 為
null」之機械讀出；我之 `[PEI]` 是「mode D 要求查得，而 leaf → CFTS 條號
之橋樑不存在（A-DM10b），故**無法提案**」。

**我維持 `[PEI]`，未依 recon 改為 `[PROPOSED]`** —— 把一個無法提案之項
標成已提案，會使它在簽核時無聲通過。此差異提請裁示。

`DECISIONS.new.md` 未併入既有 `DECISIONS.md`，兩檔並存待裁。

---

## 6. `ETM` 判準之鑑別力（步驟 5）—— **停止條件 25 觸發，已停**

### 6.1 測法

「與顯示相關」無逐字錨可判（R-DM13／停止條件 14），故改測可測者：
**ETM 群內之 keyword 命中率 vs 群外之基準率**。母體為有 PROXI 定義之
177 列。

| 群 | 列數 | keyword 命中 | 命中率 |
|---|---|---|---|
| `Used by` 含 `ETM` | **100** | 8 | **8.0%** |
| `Used by` 不含 `ETM` | 77 | 7 | **9.1%** |
| 倍率 | | | **0.88x** |

**ETM 群之命中率低於群外。** 其內容以與顯示無關者為主：
`AM_FM1_Antenna_Type`／`AMPPresent`／`Ambient_Lighting_Present`／
`AudioSystemType`／`Autonomy_Level`／`AUX_Presence`／`ANT_TYP` …

ETM 群中 keyword 命中之 8 列（全列）：`DCSD_cfg`／`Displacement`／
`DSP_SK_PRSNT`／`Head_Unit_Screen_Size`／`OFFroad_Camera`／
`RVC_SK_PRSNT`／`Splashscreen_Type`／`SVC_SK_PRSNT`。

> 其中 `Splashscreen_Type`（LID r182 → PROXI r597）與 `SWE-DM-003`
> 之 Splash 主題相鄰。**僅記，未追查**（步驟 5 之授權為測鑑別力，
> 非追查內容）。

### 6.2 停止

依 §六第 25 條：ETM 之 100 列中與顯示相關者遠少於半數，
**第一梯次判準不成立，停並回報，不得逕行改判準續做。**

`docs/proxi_triage_proposal.md` 之 §二以下已標**暫停適用**，
未自行擬新判準。

### 6.3 順帶查出我上輪的兩個錯（A-DM24）

1. **索引錯位**：我以 `{i+1: g[i-1][ui]}` 建 PROXI 列號對照，
   把每一列之 `Used by` 接到下一列。`ETM` 因此報 **50**，正確為 **100**。
2. **「互斥且窮盡：69 + 117 + 269 = 446」不成立** —— 三數相加為 **455**。
   第一梯次之 keyword 條件納入了無 PROXI 定義之列，而那些列同時被算進
   第三梯次。

更正後之互斥分割（`lid_row` 唯一性已驗，四類相加 = 446）：

| 類 | 判準 | 列數 |
|---|---|---|
| A | 有定義 且（ETM ∪ keyword） | 107 |
| B | 有定義 且 皆否 | 70 |
| C | 無定義 但 keyword | 9 |
| D | 無定義 且 無 keyword | 260 |

**這是第六次同型缺陷**，但與前五次有一點不同：**這次錯的是一句我親手
打在表下的斷言**（「互斥且窮盡」），而那句話沒有任何程式在檢查它。
提案：凡報告中出現「互斥」「窮盡」「合計」之斷言，其算式須由腳本輸出
（R-G20 之延伸）。屬 Tier 2。

---

## 7. `compare_req_families.py`（步驟 6 已於上繳 08 §6 完成）

R-DM31 已據上繳 08 §6 將其自 A-DM21 之待處理清單除名。本輪無新增。

---

## 8. 「本包是否仍有該驗而未驗者」—— 執行層之獨立判斷

**有，共 6 項。**

1. **§4.2 之字元數不符未裁。** 兩數皆可重現，成因已定位，但本 feature
   之登記值是哪一個仍未定。`DECISIONS.new.md` 已寫入 854,333，
   而我的 `probe_spec_mode.py` 仍輸出 907,382 —— **兩份產物現在說著
   不同的數字**，這狀態不宜久留。
2. **§5.2 之 `spec_reference` 分歧未裁。** recon 標 `[PROPOSED: None]`、
   我標 `[PEI]`。若日後有人以 recon 之 `DECISIONS.new.md` 為準簽核，
   一個「無法提案」之項會無聲通過。
3. **`DECISIONS.new.md` 與 `DECISIONS.md` 並存且未合併。** 兩檔內容
   大部分重疊、少數分歧，而**沒有任何條文規定哪一份是權威**。
4. **ETM 判準否定後，PROXI 之排程回到零。** keyword 相鄰之 23 列是
   目前唯一還站著的線索，而它自始標為「僅揭露、非錨」——
   即：**現在沒有任何合格的判準可用來排程那 446 列。**
5. **`estimated_test_time`（Q 欄）從未被我當成欄位對待**（§4.1）。
   寫回時它是一個可賦值欄，而我的 `feature.yaml` `columns` 沒有它。
   本輪未裁定是否要填，但也**未確認不填是否安全**。
6. **A-DM25 之三個 feature 之 `RECON.md` 不同步已登記但未處置。**
   我還原了它們，也就是說**它們仍然是不同步的**。

另記本輪**已驗而下放包未要求**者：pymupdf 之 854,333 由我重現以確認
非 recon 之計算問題；下放包 08 §2.3 第 6 列之理由錯（Display 其實有
`sys1_export`）；`Splashscreen_Type` 與 `SWE-DM-003` 之相鄰性；
全 repo 82 個 TSV 中 20 個帶註解行之清查。

---

## 9. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(recon): parameterise the a03 sheet name (option D); display round 09

- R-DM30/31 + R-G19/R-G20 verbatim (4/4, 33/33 cumulative); the check
  table is now emitted by transcribe_rulings.py rather than retyped
- recon.py survey_a03() takes the sheet name from paths_meta.a03_sheet,
  default 'Analysis Report'. Missing sheet now names the declared sheet,
  the sheets present, and where to declare it
- regression over 12 features: 11 identical, only Display changes, which
  is the point. comfort REFUSED both before and after (signed sheet)
- recon.py runs for Display for the first time: BLANK, 8 leaves, 15
  columns, 9 design-method strings — 16 of 17 comparable items agree with
  the hand-written scripts. The one mismatch is the spec text-layer char
  count (854,333 pymupdf vs 907,382 python-docx); both reproduced,
  neither adopted
- handoff 08 §2.3 verified empirically: 6 of 7 rows exact, 1 right for
  the wrong reason (Display does declare sys1_export)
- R-DM30: all 11 data TSVs start with their header; provenance moved to
  .tsv.meta.json sidecars; row counts unchanged 11/11
- ETM triage criterion measured and REJECTED: 8.0% inside vs 9.1%
  outside, 0.88x. Stop condition 25 fired; the proposal is suspended, not
  rewritten
- A-DM24: my own triage table had an off-by-one (ETM 50 -> 100) and an
  arithmetic claim that did not hold (69+117+269 = 455, not 446)
- A-DM25: three features' RECON.md were already out of sync; restored,
  not modified on their behalf
```

pathspec：

```
git add scripts/recon.py \
        docs/fw036/RULINGS_LEDGER.md \
        features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/feature.yaml \
        features/display/RECON.md \
        features/display/DECISIONS.new.md \
        features/display/scripts/ \
        features/display/data/ \
        features/display/docs/
```

**本輪帶入 `scripts/recon.py`**（選項 D 授權範圍，四處改動見 §3.2）。
`features/display/RECON.md` 與 `DECISIONS.new.md` 為 recon 首次產出，
建議一併入版以留下交叉檢查之證據。
`data/recon.json` 由該 feature 之 `.gitignore` 排除，不入版。
其他 feature 之 `RECON.md` 已還原，未帶入。
