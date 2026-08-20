# 下放包 01 — Time Management：036 母本落地、feature.yaml 版面更正、Phase 1 Recon

分析層 → 執行層。往返編號 `01`；對應上繳包
`features/time_management/docs/upstream/01_recon.md`。

前置：`00` 往返已結案（`docs/handoff/00Z_closure.md`）。

---

## 1. 本包生效之裁決

執行層須將本節整段逐字複製進 `RULINGS.md`，並於 `DECISIONS.md` 建
`[PEI]` 條目引用。

```
R-TM5（Pei, 2026-08-20）—— 036 工作簿以母本為之

本 feature 不索取客戶預填之 036 工作簿。036 以 R-G1 之全域母本
forms/FM-WI-FSM-036-A01 …_SWQT_20260817_ext.xlsx 為之。

直接後果：workbook_state = BLANK。
A-TM07（036 缺件 → workbook_state 無法判定）由本條解消，轉 RESOLVED。
```

```
R-TM6（Pei, 2026-08-20）—— 覆蓋稽核分母，並分拆 A-TM02

1. 覆蓋稽核之分母取 SYS2 之 Functional Requirement 全集 = 126，
   不取 SWE leaf 數 22。取 22 會得出「已全覆蓋」之假象。

2. A-TM02 拆為兩條，各自獨立處置：
   A-TM02a（版本身分）— SWE1_Secure_Date&Time.xlsx 是否為權威 037。
                        Tier 3，隨 RD-1 上問。
   A-TM09（內容缺口）— 48 筆 SYS2 FR 無對應 SWE leaf。
                        縱使 A-TM02a 裁定手上這件即權威 037，本缺口依然存在。

3. 48 筆缺口之處置為「宣告」，非「補生成」：
   TC 生成單位仍為 037 之 22 筆 SWE leaf。48 筆既無 leaf，
   即不得為其自行創設 leaf 或自行分解 SYS2 條文以湊覆蓋 ——
   §8.2「TC 作者不得重新分解、合併或發明 RD 項目」，
   §8.4.1「不得捏造來源未述之值」。
   缺口以 RD-1 上問，並於交付件之覆蓋稽核中明列。
```

---

## 2. R-TM5 之連鎖後果 —— **現行 `feature.yaml` 之 workbook 段是錯的**

`feature.yaml` 之 `workbook` 段目前仍為 scaffold 模板值，該模板寫的是
**rev A/B 版面**；而 R-G1 母本為 **rev C 版面**（Q 欄插入 Estimated Test
Time，其後各欄整體右移一格）。兩者不相容。

依據：`forms/FORMS.md` §`…_SWQT_20260817_ext.xlsx —— 現行 036 母本`
（2026-08-17 於 `forms/` 唯讀實測，含逐欄表頭文字對映）。

須更正之項（**照抄 FORMS.md 之實測值，不得自行推導**）：

| 鍵 | 現值（模板，rev A/B） | 應改為（母本，rev C） |
|---|---|---|
| `workbook.sheet` | `"Test Case Specification&Result"` | `"Test Case Specification 測試用例規範"` |
| `workbook.header_row` | `9` | `9`（不變）|
| `columns.design_method` | `"Q"` | `"R"` |
| `columns.functional_safety` | `"R"` | `"S"` |
| `columns.author` | `"Z"` | `"AA"` |
| `columns.remarks` | `"AH"` | `"AH"`（不變 —— 但現值之「正確」是巧合，模板註解稱其待驗，母本實測確為 AH）|
| `columns.req_id` … `priority`（D–P） | 不變 | 不變 |

**`Q` 欄在母本為 `Estimated Test Time (mins)`，不是 design_method。**
沿用模板值會把設計方法寫進工時欄，且 lint 之 design_method 詞彙比對會
在錯欄上跑 —— 靜默失效之第六例形態。

更正後**必須以 recon 之表頭文字比對複驗**，不得只信本表。復驗方式：
以表頭列 9 之表頭文字解析（`recon.py` 既有之 header-text resolution），
回報命中數（母本為 33 個非空表頭格，A 欄無表頭）。

### 2.1 `done_region` —— BLANK 下無 done region

模板值 `detection: "author"` / `author_value: "Arif"` 對母本命中 **0 列**
（母本資料區非空格為 0）。**須改為明示之空狀態**，不得留 `Arif` ——
留著會使 content-hash invariant 在 0 列上比對而恆真，屬靜默失效。

建議值（執行層逕行，Tier 1）：`detection: "none"`，並於同行註記
`# BLANK per R-TM5；本 feature 無 done region`。

### 2.2 `write_back.fill_test_group_set` —— 應為 `true`

模板值 `false`，其註解自陳 `true only under BLANK per canon §2`。
R-TM5 既定 BLANK，本鍵改 `true`。屬既有條文之機械套用，Tier 1 逕行。

### 2.3 母本不得就地使用

母本為跨 feature 共用檔。須**複製**一份進
`features/time_management/inputs/`，`feature.yaml` 之 `workbook` 指向該複本，
並比照 user_profiles 之作法記錄 SHA256，證明與母本一致
（母本現值 `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`，
200,650 bytes）。複製後對複本實測一次 SHA256，兩值須相等，回報之。

### 2.4 openpyxl 禁令（母本專屬，非通則重述）

母本 `R` 欄之 design_method 下拉為 **x14 擴充**，openpyxl 讀取即丟棄。
**任何以 openpyxl 開啟並存回之操作都會摧毀該下拉，且損壞是選擇性的** ——
工作表數、列數、公式、其他三條 legacy DV 全部不變，zip member 只少 1
（48 → 47），只比對這些項目的檢查會全綠（FORMS.md 已實測，非推論）。

故：**recon 對工作簿一律唯讀，全程不得執行任何 save。** 日後之寫回只走
`backend/xlsx_surgical.py`（R18-3，唯一寫回路徑）。

### 2.5 容量無須處置

母本 B 欄公式與四組 DV 皆已延伸至 row 1411（資料列 1402 列），
遠大於本 feature 之需求。**不得重演 Comfort 之範本擴充處置**（A-CF26）。

---

## 3. R-TM5 之結構性後果 —— **本 feature 缺少第三層品質機制**

canon §1.1 之三層品質結構為：lint（機械漂移）→ pilot 人工閘（判斷漂移）
→ **done region 以證據仲裁爭議**。

BLANK 意味著**第三層在本 feature 不存在**。Home pilot 中該層曾推翻兩項
reviewer 直覺、並定案一項真缺陷；本 feature 無此仲裁者。連帶：canon §1.1
之推論「reviewer 之發現須通過 done-region check 方成為 defect」
在本 feature **無適用對象** —— 不得據此駁回任何 pilot 發現。

**分析層之提議（Tier 2，Pei 裁，非執行層可決）**：以 Home 之 done region
（Arif 144 列）作為跨 feature 樣式參照。此為 canon §0 Tier 2 明列之
boundary case「cross-feature exemplar admissibility」，須明示裁定後方可援引；
未裁前，pilot review 以條文（§4–§12）為唯一判準，不得援引任何他 feature 之
既成樣式。

**執行層本包不處理本節，僅於上繳包確認已知悉。**

---

## 4. 待登記之新 anomaly

**A-TM11 — 母本之 Scope 欄（`D5`）為空**

FORMS.md 實測：母本 `C5` 標籤為 `範圍 Scope：`，值格 `D5` **為空**。
Home 與 AMFM 兩個實例之 Scope 皆為手工維護且**兩者皆錯**
（Home A-H26、AMFM RULINGS C1）。本 feature 因用母本，起點是空而非錯 ——
較佳，但仍須填。

填什麼屬交付件內容，**Tier 2**（範圍界定）。執行層**登記並提案，不得自填**。
提案時附 Home v2 之正確值形態（`…Home-HMI-V0.1`）作為格式參照。

**A-TM07 — 轉 RESOLVED**

處置條文：R-TM5 逐字。狀態改 RESOLVED，索引表同步。

---

## 5. Phase 1 Recon 作業指示

前置：§2 之 `feature.yaml` 更正與 §2.3 之複本落地完成後方可起跑。

```bash
cd /Users/peihe/Work_Projects/TC_Generator
python scripts/recon.py time_management
```

回報須含（缺欄位者本包退回，不予核可）：

1. **`workbook_state`** —— 應為 BLANK。若非，停止並升 Tier 2
2. **欄位對映之表頭文字命中數** —— 母本應為 33/33；不足即停
3. **leaf 全集** —— 037 之 22 筆，逐筆列出 id（R-TM4：不得只給計數）
4. **037 之 header row 與 Categorization 欄位置** —— FORMS.md 記載三種
   037 變體之 header row 分別為 7 / 8 / 7，Categorization 分別在 col 7 /
   col 31 / 缺席。**本件屬何種形態須實測回報**，且須說明 `recon.py` 之
   「header row = 含 `Requirement Description` 之列」規則在本件是否命中
5. **ASIL / FTTI 欄之有無** —— 依 FORMS.md，其在受裁需求來源中之缺席，
   正是把 SYS2/SYSRA 安全層排除於 trace chain 之依據。本件實測結果直接
   影響 R-TM6 之分母論述是否需要補述
6. **spec_id → outline 映射** —— spec_mode D，以 `spec_pdf` 所指之 CFTS
   docx 為之。fail-loud on miss，不得靜默略過
7. **Pop Up List 命中測試** —— 命中 0 則 `popup_list: null` 並註記依據；
   命中非 0 則列為 DATA_REQUESTS 之 High
8. **48 筆缺口之 id 全集** —— 依 R-TM4 公布完整清單，供 RD-1 引用

**不進入 Phase 3（framework）。** 本包止於 recon 上繳。

---

## 6. 升級 chat 覆核之條件

- `workbook_state` 非 BLANK
- 表頭文字命中數 < 33
- 037 之 header row 或 Categorization 欄與 FORMS.md 三種既知形態皆不符
- leaf 數非 22，或 leaf id 非 `SWE-RA-TIME&DATE-001…-022` 連續
- spec_id → outline 有無法解析之項
- 任何步驟需要以 openpyxl 存回工作簿

## 7. 上繳包須包含

1. `RECON.md` 與 `recon.json` 之路徑，`DECISIONS.md` 之 `[PROPOSED]` 清單
2. 更正後之 `feature.yaml` 全文，與 §2 表列之改前／改後逐項對照
3. §2.3 之兩次 SHA256 實測值（母本、複本）
4. §5 之 1–8 逐項
5. A-TM11 登記、A-TM07 轉 RESOLVED 之確認，索引表更新為 11 條
6. §3 已知悉之確認（不處理，僅確認）
7. **本包是否仍有該驗而未驗者之獨立判斷** —— 盤點所用之全集須明列
   （00R 之教訓：只盤已寫入者、未盤該寫而空著者）

## 8. 本包產生之新條文清單（自檢）

| 編號 | 形態 | 已以可貼區塊呈現 |
|---|---|---|
| R-TM5 | 裁決（Pei 已裁） | ✅ §1 |
| R-TM6 | 裁決（Pei 已裁，含 A-TM02 分拆與 48 筆之處置方向） | ✅ §1 |
| A-TM11 | anomaly，PENDING，填值屬 Tier 2 | ✅ §4 |
| A-TM07 | 轉 RESOLVED，處置條文為 R-TM5 | ✅ §4 |
| 跨 feature 樣式參照之可採性 | 提案，待 Pei 裁，未成條文 | 敘述於 §3 |

分析層本包未動 git、未改腳本、未動 `forms/`、未改任何既有檔案。
