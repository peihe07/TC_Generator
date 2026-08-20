# 上繳包 01 — Time Management：036 母本落地、feature.yaml 更正、Phase 1 Recon

執行層 → 分析層。對應下放包 `docs/handoff/01_recon.md`。2026-08-20。
**止於 recon 上繳，未進入 Phase 3。**

## 0. 與下放包之偏離（先講）

**§5 之指令字面不可執行。** 下放包給：

```bash
python scripts/recon.py time_management
```

實測 `recon.py` 之 argparse 為 `--feature`（required），且該值取**相對
root 之路徑**而非 feature 名（`feature_dir = Path(args.root) / args.feature`，
`scripts/recon.py:1087`）。故正確指令為：

```bash
python scripts/recon.py --feature features/time_management
```

兩次失敗依序為 `error: the following arguments are required: --feature`
與 `FileNotFoundError: .../TC_Generator/time_management/feature.yaml`。
屬 CLI 字面之技術性選擇（R-TM3 同型），逕行修正並回報，未升 Tier 2。

**另有一項前置阻斷**：`popup_list` 仍為佔位符 `"inputs/<Pop Up List xlsx>"`
時，recon 以 `input not found` 中止。依 §5(7) 設為 `null` 後通過 ——
此為 fail-loud，屬正確行為，記錄之。

## 1. §2 —— `feature.yaml` 更正逐項對照

全部照抄 `forms/FORMS.md` 之 rev C 實測值，未自行推導。

| 鍵 | 改前（模板 rev A/B） | 改後（母本 rev C） | recon 表頭文字複驗 |
|---|---|---|---|
| `workbook` | `"inputs/<FW036 xlsx>"` | 母本複本路徑（見 §3） | — |
| `workbook.sheet` | `"Test Case Specification&Result"` | `"Test Case Specification 測試用例規範"` | 命中 |
| `workbook.header_row` | `9` | `9`（不變） | 命中 |
| `columns.design_method` | `"Q"` | **`"R"`** | 命中 |
| `columns.functional_safety` | `"R"` | **`"S"`** | 命中 |
| `columns.author` | `"Z"` | **`"AA"`** | 命中 |
| `columns.remarks` | `"AH"` | `"AH"`（不變） | 命中 |
| `columns.req_id`…`priority`（D–P） | 不變 | 不變 | 全數命中 |
| `done_region.detection` | `"author"` | **`"none"`** ＋ 註記 | §2.1 |
| `done_region.author_value` | `"Arif"` | **註解掉**，非留值 | §2.1 |
| `write_back.fill_test_group_set` | `false` | **`true`** | §2.2 |
| `popup_list` | `"inputs/<Pop Up List xlsx>"` | **`null`** ＋ 實測依據 | §5(7) |

**recon 回報 `feature.yaml column conflicts: (none)`** —— 即上表之更正與
表頭文字解析結果**完全一致，零衝突**。`Q` 欄經 recon 獨立解析為
`estimated_test_time`，與 FORMS.md 相符。

## 2. §5(2) —— 表頭文字命中數 33/33

**須先分辨兩個不同的量**，下放包 §5(2) 指的是後者：

- recon 之 `column mapping: 15 fields resolved` —— 這是**欄位對映數**
  （15 個具名 field），非表頭格數
- **表頭列 9 之非空表頭格 = 33**，A 欄無表頭

執行層獨立實測（openpyxl read_only，未 save）：列 9 非空格 **33** 個，
首格 `B = 'No.#\n序號'`，末格 `AH = 'Remarks\n備註'`，`A9` 為 `None`。
**與 FORMS.md 期望之 33 相符，不足即停之條件未觸發。**

## 3. §2.3 —— 母本複本與雙 SHA256

母本未就地使用，已複製一份進 `inputs/`：

| | SHA256 | bytes |
|---|---|---|
| 母本 `forms/…_SWQT_20260817_ext.xlsx` | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` | 200,650 |
| 複本 `inputs/…_SWQT_20260817_ext.xlsx` | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` | 200,650 |

**兩值相等**，且 `cmp` 逐位元組比對 `identical`。與 01 包 §2.3 及
FORMS.md 所載之期望值相符。

### 3.1 §2.4 openpyxl 禁令 —— 已遵守，並以三重證據證明

`recon.py` 三處開檔全為 `load_workbook(..., read_only=True)`
（行 161 / 408 / 560），**全檔無任何 `.save()` 呼叫**（已 grep 確認）。

recon 執行時出現預期中之警告：

```
UserWarning: Data Validation extension is not supported and will be removed
```

此即 §2.4 所述之 x14 DV。**警告僅發生於讀取，未存回。** recon 後複驗：

| 檢查項 | recon 前 | recon 後 | 損壞時之預期值 |
|---|---|---|---|
| 複本 SHA256 | `6372fb6b…` | **`6372fb6b…`（不變）** | 會改變 |
| zip members | 48 | **48** | 47 |
| 母本 SHA256 | `6372fb6b…` | **`6372fb6b…`（不變）** | — |

三項皆未變動，R 欄 x14 下拉未被摧毀。

## 4. §5 —— 1 至 8 逐項

### (1) `workbook_state` = **BLANK** ✅

與 R-TM5 之直接後果一致。recon 另報 `form layout revision: C`。

### (2) 表頭文字命中數 = **33/33** ✅

見 §2。

### (3) leaf 全集 —— 22 筆，依 R-TM4 逐筆列出

```
SWE-RA-TIME&DATE-001  -002  -003  -004  -005  -006  -007  -008
                -009  -010  -011  -012  -013  -014  -015  -016
                -017  -018  -019  -020  -021  -022
```

連續無缺號。`leaves` == `regen_targets` == `uncovered`，三集合經程式比對
**完全相同**（BLANK 之必然結果，非缺陷）。headings = 0。

leaf 判準：`Categorization == Functional`，分佈 `{'Functional': 22}`。

### (4) 037 之 header row 與 Categorization 欄位置 —— **屬第二形態**

實測：**header row = 8**，**Categorization = `AE` = col 31**。

對照 FORMS.md 所載三種 037 變體：

| 形態 | header row | Categorization | 本件 |
|---|---|---|---|
| Home 型 | 7 | col 7 | — |
| **AM/FM 型** | **8** | **col 31** | **✅ 相符** |
| 第三型 | 7 | 缺席 | — |

**與既知形態相符，§6 之升級條件未觸發。**

**`recon.py` 之 header row 規則在本件命中 —— 但初驗時曾誤判為未命中。**
該規則為「含 `requirement description` 之列」（`recon.py:562`），比對前
先過 `norm()`（小寫化 + `\s+` 折疊）。本件之表頭格為：

```
D8 = 'Requirement  Description'      ← 兩個空格
```

執行層首次以精確字串 `"Requirement Description" in v` 檢查，**因雙空格而
未命中**，一度以為觸發 §6。經改用 `recon.py` 之 `norm()` 重驗，命中
`hdr index = 7`（1-based 列 8），與 recon 自身結果一致。

**記錄此事之理由**：若當時逕以首次結果上報，會誤報一個不存在的升級條件。
驗證他人之規則時，須用**該規則自身之比對函式**，不得以外觀相近之自製
比對代替 —— 與 A-TM09 §D 之教訓同型（代理判準不得凌駕實質判準）。

### (5) ASIL / FTTI —— **ABSENT** ✅

`has_safety_columns: False`，`asil_distribution: {}`。

依 FORMS.md，其在受裁需求來源中之缺席正是把 SYS2/SYSRA 安全層排除於
trace chain 之依據。recon 之措辭已將此界定得很準：缺席**僅表示受裁來源
未主張其安全相關**，不表示需求非安全相關。

**對 R-TM6 分母論述之影響：不需補述。** 分母 126 取自 SYS2 之
`Category == Functional Requirement`，該欄與 ASIL 無關；ASIL 缺席影響的
是 trace chain 是否納入安全層，與分母之取法正交。

### (6) spec_id → outline 映射 —— **0 筆，已登記 A-TM12**

`sections: {}`、`distinct_sections: []`、`outline_misses: []`，
`data/recon_leaf_to_section.tsv` 僅存表頭列。

原因：`recon.py` 之 `build_outline_map()` **只接受 `sys1_export`**，
其 docstring 自陳用途為 spec_mode **A**。本 feature 為 spec_mode **D**，
下放包 §5(6) 明訂應以 `spec_pdf` 之 CFTS docx 為之，**但工具無此路徑**。
逕以 SYS2 export 為源，而該檔無 `Outline Number` 欄，故回空 map。

**未觸發 §6 之「有無法解析之項」**：037 無 citation 欄
（`citation column: NOT FOUND`），cited sections = 0 —— **無「項」可解析，
非「項」解析失敗**。二者須分辨。`build_outline_map` 之 docstring 已預期
零引用之情形，明言不得因未使用之 lookup 而阻塞。

**但 Phase 4 必撞牆**：`spec_reference_template` 為
`"<Spec Filename>_{outline}"`，`{outline}` 之來源即該 map。recon 全綠而
Phase 4 一定失敗，屬**延遲失效**。已登記 **A-TM12**（Tier 2），並提兩案：
(a) `recon.py` 增 spec_mode D 路徑，自 CFTS docx 解析章節（docx 已有
text layer，recon 實測 106,094 chars via pymupdf，技術可行）；
(b) 若本 feature 之 `spec_reference` 實不採 `{outline}` 形態，則應改
`spec_reference_template`，而非留一個永遠建不起來的 map。

### (7) Pop Up List 命中測試 —— **0 命中**，已設 `null`

執行層對 CFTS docx **全文**掃描（解壓所有 `.xml`、去標籤後比對）：

| 判準 | 命中 |
|---|---|
| PU-number（`PU\d{3,4}`，含分隔符變體，忽略大小寫） | **0** |
| `pop up` / `popup` / `pop-up` 字樣（忽略大小寫） | **0** |

`feature.yaml` 設 `popup_list: null`，行內註記實測依據。
`DATA_REQUESTS #3` 維持 NOT REQUESTED，不升 Urgency。

### (8) 48 筆缺口之 id 全集 —— 依 R-TM4 公布

（`SYS-RA-TIME&DATE-` 前綴省略，皆為 `Functional Requirement`）

```
009 012 016 036 038 040 041 064 065 066 086 087 088 089 091 092 093
099 108 110 111 113 115 117 122 123 124 128 129 130 131 134 135 144
149 151 152 157 170 172 217 220 222 225 226 227 228 229
```

供 RD-1 引用。與 A-TM09 §B 之清單為同一份。

## 5. §7(1) —— 產出路徑與 `[PROPOSED]` 清單

- `RECON.md`（3,518 bytes）
- `data/recon.json`
- `data/recon_leaf_to_section.tsv`（表頭列 only，見 §4(6)）

`DECISIONS.md` §2 / §3 已由 recon 結果填實，其餘 `[PROPOSED]` 項
（§4 樣式綁定、§5 split、§6 framework、§7 執行）**屬 Phase 3 範圍，
本包未動**，維持模板狀態待 framework 階段填。

recon 另發 `WARNING (R-C10)`：`DECISIONS.md` 有 `[PROPOSED]` 項且
Sign-off 區塊未填，故本 feature 之簽核狀態無法自 repo 判定。**Not
blocking**，如實回報。

## 6. §7(5) —— anomaly 登記確認，索引表 **12 條**

| 異動 | 內容 |
|---|---|
| **A-TM07 → RESOLVED** | 處置條文 R-TM5 逐字錄入；PENDING 期間之原始登記保留為軌跡；五項原阻塞逐項交代解除方式；`DATA_REQUESTS #1` 隨之 CLOSED |
| **A-TM02 → A-TM02a** | 依 R-TM6(2) 分拆，僅存版本身分（Tier 3，隨 RD-1 上問）；內容缺口已獨立為 A-TM09 |
| **A-TM11 新登記** | 母本 `D5` Scope 為空；已提案格式參照，**未自填**（Tier 2） |
| **A-TM12 新登記** | 見 §4(6)，執行層自行登記 |

索引表 **12 條**（下放包 §7(5) 預期 11 條，多出者為 A-TM12）。

**A-TM11 之提案（不自填）**：格式參照 Home v2 之 `…Home-HMI-V0.1`，
本 feature 候選為 `Time-Management-HMI-V0.1` 或 `Time-and-Date-HMI-V0.1`。
**二者取捨牽動 R-TM1 之別名體系**（feature 名 vs spec 標題），與 R-TM2 之
`test_group` 屬同一組命名決定，**宜一併裁**。

## 7. §7(6) —— §3 已知悉之確認

已知悉，本包未處理。確認理解如下：

- BLANK ⇒ canon §1.1 三層品質結構之**第三層（done region 證據仲裁）在本
  feature 不存在**
- 連帶：canon §1.1 之「reviewer 之發現須通過 done-region check 方成為
  defect」**在本 feature 無適用對象**，不得據此駁回任何 pilot 發現
- 跨 feature 樣式參照（Home 之 Arif 144 列）屬 canon §0 Tier 2 明列之
  boundary case，**須 Pei 明示裁定後方可援引**
- **未裁前，pilot review 以條文（§4–§12）為唯一判準**，不援引任何他
  feature 之既成樣式

## 8. §7(7) —— 該驗而未驗者之獨立判斷

**盤點所用之全集（依 00R 之教訓明列）**，三個全集聯集：

1. `feature.yaml` **全部 12 個可填鍵**（不只已寫入者 —— 此為 00R 所指之
   失誤，本次已改正）
2. 下放包 §5 之 **8 個回報項**，逐項確認有無「回報了但沒實測」者
3. recon 產出之**每一個非零斷言**，逐一問其依據是實測或轉述

### 8.1 依全集 1 —— `feature.yaml` 逐鍵狀態

| 鍵 | 值 | 依據 |
|---|---|---|
| `feature` / `test_group` | 已填 | R-TM1 / R-TM2 |
| `paths.workbook` | 母本複本 | 雙 SHA + cmp 實測 |
| `paths.a03_report` / `sys1_export` / `spec_pdf` | 已填 | SHA256 實測 |
| `paths.popup_list` | **`null`** | §4(7) 全文掃描 0 命中 |
| `spec_mode` | `D` | intake |
| **`spec_reference_template`** | `"<Spec Filename>_{outline}"` | **未驗 —— 見 8.3** |
| `workbook.*`（sheet / header_row / 15 欄） | 已填 | recon 表頭文字解析，零衝突 |
| `done_region.*` | `detection: "none"` | BLANK 實測 |
| `write_back.*` | `author_value` / `tc_ref_id_value` / `fill_test_group_set` | 前二者為模板值，**見 8.3** |
| `lint.design_method_source` | `"dropdown_sheet"` | recon 讀出 9 條詞彙 |
| `lint.popup_ids` / `extra_rules` | `[]` | 空為正確（0 命中 / 無 hook） |

**12 鍵全數有交代。**

### 8.2 仍未驗但屬本包範圍外者（明列，不含糊）

| 項 | 為何未驗 | 建議時機 |
|---|---|---|
| `write_back.author_value: "PeiPYHsu"` | 模板值。BLANK 下無既有 author 可比對，**其正確性無法由本 feature 內部驗證** | 首批寫回前，對照 canon 或他 feature 之慣例確認 |
| `write_back.tc_ref_id_value: "NEW"` | 同上 | 同上 |
| CFTS docx 之**章節結構**（非僅 text layer 長度） | 本包止於 recon；A-TM12 未裁前，解析方式未定 | A-TM12 裁定後 |
| `spec_reference_template` 之實際可行性 | **依賴 A-TM12** | 同上 |

### 8.3 本次盤點新發現者

**`spec_reference_template` 與 `write_back` 之三個模板值，是本包唯一一組
「已寫入 `feature.yaml`、recon 未檢查、且無人聲明過其依據」之值。**

recon 之 `assertions` 區塊為 `(no assertions declared in feature.yaml)` ——
即**本 feature 未宣告任何機械斷言**，故這些值不受任何自動檢查保護。
A-TM12 已涵蓋 `spec_reference_template` 之部分；`write_back` 之兩值
則完全未被任何條文或工具觸及。

**執行層提請**：是否應於 `feature.yaml` 宣告 assertions（recon 支援但本
feature 未用）。屬 Tier 2，本包不自行增設。

### 8.4 判定為「無」者及其全集依據

- **037 leaf 無缺號** —— 22 筆全集列舉，001–022 連續（非抽樣）
- **表頭無衝突** —— recon 對 15 欄逐欄比對 `feature.yaml` 與表頭文字，
  報 `col_conflicts: (none)`；非抽樣
- **PU 編號 0 命中** —— CFTS docx **全部 xml part** 解壓後全文掃描，
  非抽樣
- **母本未被損壞** —— SHA256 + zip member 數 + 母本自身 SHA 三重比對

## 9. 本包未動之事項

未動 git。未改任何腳本（A-TM04 / A-TM05 / A-TM10 / A-TM12 之修法皆
Tier 2，全部未動）。未動 `forms/`（母本 SHA 前後一致，已證）。
未動其他 feature 目錄。未進入 Phase 3。A-TM11 未自填。
