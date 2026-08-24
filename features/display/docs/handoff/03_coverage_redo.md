# 下放包 03 —— 上繳 02 之覆核，覆蓋對照重做

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`display`
- 對應上繳：`features/display/docs/upstream/03_coverage_redo.md`
- 前一包：`02_source_correction.md`；覆核標的為上繳包 `02_intake_recon.md`

---

## 一、覆核結論

**核可，惟 §9 覆蓋對照表退回重做。** 其餘各節（台帳、抄錄、037／SYS2
重算、036 欄位、`workbook_state`、spec_mode、`feature.yaml`）全數採認。

§11 之自我判斷（8 項該驗未驗）品質高，其中第 3 項「文字依據是啟發式」
自陳為正確，但**低估了嚴重性** —— 該啟發式不只是精度不足，它產出的
兩個結論方向相反地錯了（見 §三）。

### 1.1 分析層之獨立複驗（採認之依據）

| 標的 | 分析層獨立量測 | 與上繳相符 |
|---|---|---|
| 036 母本表頭 r9 全欄 | B…AH 逐欄讀出 | **相符**。`design_method=R`／`functional_safety=S`／`author=AA` 三項更正正確；Q 欄確為 `Estimated Test Time (mins)`、Z 欄確為 `Fastack (376) Atl-Mi` |
| `workbook_state` | r10–r1411 掃描，I 欄或 O 欄非空 = **0**；AA 欄非空 = **0** | **相符**，`BLANK` 成立 |
| `下拉選單` 分頁 | 9 個值逐字讀出 | **相符** |
| SYS2 FR 母體 | `Category` 正規化 = `functional requirement` → **80** | **相符** |

量測條件：`openpyxl`、`data_only=True`；036 為非唯讀（未存回），
SYS2 為唯讀；判空為 `str(v).strip()==""`。

---

## 二、上繳包之三處報告缺陷（須更正，不影響結論）

### 2.1 §6.4 之 `15/15` 與正文之 `12/15` 為不同基準，機器輸出未載明

程式碼區塊之表題為「column mapping — declared vs header-derived」，
`match count: 15/15`；而同節正文寫「匹配數 12/15」，`DECISIONS.md`
亦記 12/15。

兩者皆為真，但**基準不同**：15/15 是更正後之 `feature.yaml` 對母本
之複驗；12/15 是 scaffold 模板對母本之原始比對。機器輸出未載明其
`declared` 欄取自何者，讀者見 15/15 會得出「模板無誤」之相反結論 ——
而模板有誤正是 A-DM7 之全部內容。

**處置**：`probe_036.py` 之輸出須同時列印兩個基準之比對，各自標名
（`template-declared` / `effective-declared`），不得只印其一。

### 2.2 §6.4 之 036 表頭標為 `(raw)`，實際已正規化

上繳所印為 `B: 'No.# 序號'`。分析層以 `repr` 讀出之實際值為
`'No.#\n序號'` —— 分隔符為換行，非空格。三十三欄皆然
（如 `'Test Case Design \nMethods\n測試用例設計方法'`）。

此與 A-DM5（037 表頭不規則空白）為同一類缺陷，而該節恰恰是登記
該缺陷之處。標 `(raw)` 卻印正規化值，會使下一個讀者以為 036 表頭乾淨。

**處置**：改印 `repr`。A-DM5 之適用範圍擴及 036 母本表頭，於
`ANOMALIES.md` 補述。

### 2.3 `No.#`（B 欄）完全未報告 —— 且其為公式

分析層實測（`data_only=False`）：B10–B1411 全為

```
=IF(ISBLANK($D10),"",ROW()-9)
```

即 B 欄依 D 欄（`req_id`）是否為空自動編號。`data_only=True` 讀 B10
得快取值 `1`。

上繳包 §7 之 `workbook_state` 判定以 I／O 欄為據，判 `BLANK` 正確
（canon §2 step 1 之判準即為 Test Item 或 TC ID）；但 B 欄之存在與其
公式**在整份上繳包中一次未提**。寫回時若對 B 欄賦值，將摧毀 1402 列
之公式。

**處置**：`feature.yaml` 增註「B 欄為公式欄，寫回一律不觸碰」；
以 **A-DM12** 登記（非錯誤，是遺漏之工作簿事實）。

---

## 三、§9 覆蓋對照表 —— 退回重做

### 3.1 已證之錯誤

上繳 §9 與 A-DM11 之結論「`SWE-DM-004`（Thermal Management）、
`SWE-DM-005`（Thermal Protection）、`SWE-DM-007`（RVC Management）
之命中列數均為 0」**為誤**。

分析層以關鍵字直查 SYS2 `Basic Report` 之 `Description` 欄，實測：

| SYS2 列 | Sys-RA-Feature-ID | Category | 內容（節錄） |
|---|---|---|---|
| r30 | SYS-RA-DM-029 | Heading | `Multi-stage' DCSD Display Hot Algorithm` |
| r31 | SYS-RA-DM-030 | Functional Requirement | `$DCSD_DISP_STAT$ <> [DISP_HOT]` → `= [DISP_HOT]` 時，HU 顯示 Display Hot State 警告畫面 |
| r32 | SYS-RA-DM-031 | Functional Requirement | `[DISP_HOT]` → `[DISP_OFF]` 時，HU 送 `$TGW_DISP_STAT$ = [DISP_OFF]`、`$RQ_DISP_INTS$ = [0% Intensity]` |
| r33 | SYS-RA-DM-032 | Functional Requirement | DCSD 仍在 Hot 而 HU 需暫時點亮時之行為 |
| r34 | SYS-RA-DM-033 | Functional Requirement | `[DISP_HOT]` → `[DISP_ON]` 序列後恢復正常顯示 |

r30 之標題即 **DCSD Display Hot Algorithm**，正是 `SWE-DM-004`／`005`
之 Requirement Title 所稱之 `Hot Algorithm`。**逐字同名。**

而上繳 §9 之表將 r31／r32 判給 `SWE-DM-001`（依據 token
`['dcsd','send','transition']`）、r34 判給 `SWE-DM-003`（依據
`['normal','resume','screen','sequence']`），r33 判為「無」。

即：**該啟發式同時產生了偽陰性（004／005 = 0）與偽陽性（001／003
收到不屬於它們的列）**，且兩者互為因果 —— 同一批列被錯配到相鄰 leaf，
於是被搶走的 leaf 顯示 0。

`SWE-DM-008` 收到 11 列，其依據全部是同一組 token
`['camera','rear','screen','view']`；`SWE-DM-002` 收到 6 列，依據多為
`['dcsd','touch']` 之變體。這種依據無鑑別力。

### 3.2 由此推翻之下游主張

| 出處 | 主張 | 覆核 |
|---|---|---|
| A-DM11 | 004／005／007 文字依據命中 0 列 | **撤回** |
| `DECISIONS.md` §3 | 同上 | **撤回** |
| 上繳 §9 | 「依據別統計 text: 22 / none: 57」 | 數字本身無誤（是該腳本之輸出），但**不得作為覆蓋量級之陳述** |
| 上繳 §9 | 「80 列中 58 列無對應」 | **降格**：僅得表述為「以 id 為據之對應為 0 列」；58 這個數字須撤回 |

**id 依據 0 列（A-DM2）是本輪唯一站得住的覆蓋陳述**，因為它是逐字比對，
不是啟發式。

### 3.3 重做之方法（取代 bag-of-words）

不要再調門檻或停用詞表 —— 問題不在參數。改用**結構性錨點**，逐列標記
其可用之錨，無錨者標無錨，不猜：

錨之優先序（先到先得，記其種類）：

1. **`$Signal$` token** —— SYS2 之 FR 列以 `$NAME$` 標記訊號。分析層
   實測：80 個 FR 列中 **43 列含 `$signal$`**，相異訊號名 **15 個**，
   出現次數前三為 `TGW_DISP_STAT`(33)、`RQ_DISP_INTS`(28)、
   `DCSD_DISP_STAT`(9)。
2. **`[VALUE]` token** —— 相異 **9 個**：`DISP_OFF`(15)、
   `DISP_NORMAL`(12)、`DISP_REAR_CAMERA`(5)、`DISP_HOT`(4)、
   `DISP_ON`(1)、`RR_CMRA`(1)、`OFF`(1)、`ON_BLANK`(1)、`SNA`(1)。
3. **SYS2 之 Heading 從屬** —— 該 FR 列上方最近之 `Category = Heading`
   列，其 `Description` 即該段之章節標題（如 r30 之
   `Multi-stage' DCSD Display Hot Algorithm`）。Heading 名與 037 之
   `Requirement Title`／`Sub Categorization` 之比對，**比整列文字重疊
   可靠得多**，因為兩邊都是人寫的標題。
4. **Melco ID** —— 已用於排除項（R-DM4）。
5. **無錨** —— 明白標示。

輸出欄位改為：

```
sys2_row | sys_ra_id | category | swhw | heading_ancestor | signals | values | melco | anchor_kind | candidate_leaf | note
```

`candidate_leaf` 欄名**必須是 candidate**，不得寫 `對應`。任何後續引用
須連同 `anchor_kind` 一併引用，禁止單獨引用 `candidate_leaf`。

> 此處之判準為 canon §5a：**啟發式之輸出不得以結論之語氣命名。**
> 上繳 §9 之欄名為「對應 SWE-DM」，A-DM11 之表頭為「依據」，兩者
> 讀起來都像已認定之事實 —— 縱使正文有免責句，欄名會活得比正文久。

### 3.4 Heading 從屬之附帶要求

產出 SYS2 `Basic Report` 之**章節樹**：以 `Category = Heading` 之 45 列
為節點，其後續非 Heading 列為其子，輸出

```
heading_row | sys_ra_id | heading_text | child_rows | child_FR_count
```

此樹本身即為 Q2 之判斷底稿：它讓「SYS2 有幾個顯示相關之能力群、
037 之 8 個 leaf 落在哪幾群、哪幾群完全沒有 leaf」成為可讀之事實，
而不是 58 這個無錨的數字。

---

## 四、對 R-DM8 與 Q2 之影響（重要）

### 4.1 SYS2 是訊號值域之來源，而 037 不是

r31／r32 之內文載明具體訊號與值：`$DCSD_DISP_STAT$`、`$TGW_DISP_STAT$`、
`$RQ_DISP_INTS$`、`[DISP_HOT]`、`[DISP_OFF]`、`[0% Intensity]`。

R-DM8 列 `SWE-DM-004`／`005` 之缺值為「thermal warning threshold 之門檻值
與單位」「critical 判準與回復條件」。上繳 §14b 之查證只回 CFTS 與 SYS3，
**未查 SYS2** —— 而 SYS2 這四列正是該行為之狀態機定義。

DR-DM1／DR-DM2 之開立**維持不變**（`{CFTS009-722}` 之時段、popup 仲裁
順序表確實不在手上三份素材內，r37 已複驗 `{CFTS009-722}` 為外部引用），
但 004／005 之處置須自「記章節」改為「SYS2 有狀態機定義，CFTS 有行為章節，
二者須併讀後再判是否仍缺值」。

**下一輪須做**：以 §3.3 之錨為索引，將 SYS2 之 hot-behaviour 四列與
CFTS `1.11.2.2 {4820281}` 併列，判定 R-DM8 之四處值是否仍缺。
**仍不得回填任何值** —— 本輪之產出是「缺或不缺」之判定與其證據位置，
不是值本身。

### 4.2 Q2 之性質改變，暫緩裁定

原 Q2 之提法為「8 個 leaf vs SYS2 之 80 個 FR，範圍取何者」。依 §3.1 之
發現，該提法之前提（037 之 leaf 與 SYS2 之 FR 是兩組不同的東西）不成立
—— 037 之 `Hot Algorithm` 與 SYS2 之 `Display Hot Algorithm` 是同一件事
之兩個抽象層級。

**Q2 於 §3.3／§3.4 之產物到齊前不提交 Pei 裁定。** 以無錨之 58 這個數字
去問 Pei「要不要擴大範圍」，是拿錯誤的量級請求裁決。

此為分析層之自我更正：上繳 §9 之表是依分析層下放包 01 R-DM7 所指定之
方法（「Description 文字」列為三種依據之一）產出的。**方法是我指定的，
錯也是我的。** 執行層依指定執行並在 §11 自陳其為啟發式，處置正確。

---

## 五、裁決條文（抄入 `RULINGS.md`）

```
R-DM12（啟發式輸出之命名與引用）
凡以文字相似度、token 重疊、模糊比對等啟發式產出之欄位，其欄名
一律冠 `candidate_` 或等義之未定語，不得使用 `對應`、`mapping`、
`match` 等已認定語氣之名稱。

引用該欄時必須同時引用其依據種類欄（`anchor_kind` 或等義欄），
禁止單獨引用結果欄。

理由：正文之免責敘述與欄名分離後，欄名會被單獨引用。本條為
上繳包 02 §9 之「對應 SWE-DM」欄致誤之防再犯條文。
```

```
R-DM13（覆蓋對照之錨定方法）
SYS2 ↔ 037 之覆蓋對照一律以結構性錨為據，優先序為：
`$Signal$` token → `[VALUE]` token → SYS2 Heading 從屬 → Melco ID →
無錨。bag-of-words 重疊**不得作為錨**，亦不得作為候選之產生方式。

下放包 01 R-DM7 所列之「Description 文字（機械 bag-of-words 重疊）」
一項**廢止**。廢止理由：該方法對 SYS2 之 hot-behaviour 四列
（r31–r34）同時產生偽陰性與偽陽性，致 `SWE-DM-004`/`005` 被誤報為
命中 0 列（詳見下放包 03 §3.1）。R-DM7 之其餘部分（揭露義務、
不得裁定範圍）不受影響。
```

```
R-DM14（訊號值域之來源）
本 feature 之訊號名與值域以 SYS2 `Basic Report` 之 `$Signal$` 與
`[VALUE]` token 為第一來源（實測：80 個 FR 列中 43 列含訊號，
相異訊號名 15、相異值 token 9）。

037 不含訊號層資訊，不得作為值域來源。
CFTS_020 之對應章節為行為敘述，與 SYS2 併讀。

本條僅定來源，不定 TC 之書寫格式；書寫格式依 canon §8.7.5 或本
feature 日後之 profile override，本輪不定。
```

```
R-DM15（036 母本 B 欄）
036 母本 `Test Case Specification 測試用例規範` 分頁之 B 欄
（`No.#`）為公式欄，B10–B1411 逐列為
`=IF(ISBLANK($D{row}),"",ROW()-9)`。

寫回一律不得對 B 欄賦值。序號由 D 欄（`req_id`）之填寫自動產生。
```

---

## 六、作業步驟

1. 抄錄 §五四條入 `RULINGS.md`，附逐條核對表。
2. 依 §2.1 修 `probe_036.py` 之輸出（兩基準並列），重跑，附輸出。
   —— 本項為腳本輸出格式，屬 `features/display/scripts/` 下之自有腳本，
   不受 §五第 9 條（不修 `scripts/` 既有腳本）拘束。
3. 依 §2.2 以 `repr` 重印 036 表頭；`ANOMALIES.md` 之 A-DM5 補述其
   適用範圍及於 036 母本。
4. 登記 **A-DM12**（B 欄公式未報告）；`feature.yaml` 補註 B 欄不觸碰。
5. 依 §3.3 重寫 `coverage_map.py`，重出
   `data/coverage_sys2_vs_swe_dm.tsv`（欄位依 §3.3）。
   **舊檔不刪除**，改名 `data/coverage_sys2_vs_swe_dm.RETRACTED.tsv`
   並於檔頭加一行註明其被 R-DM13 廢止（R-TM13：不刪除，加註保留）。
6. 依 §3.4 產出 SYS2 章節樹 `data/sys2_heading_tree.tsv`。
7. 更正 `ANOMALIES.md` 之 A-DM11：撤回「004/005/007 命中 0」與「58 列
   無對應」，改記 §3.1 之發現與 §3.3 之新方法；狀態維持 PENDING。
8. 更正 `DECISIONS.md` §3 之對應條目，並將 Q2 標為
   **「暫緩 —— 待 §3.3／§3.4 產物」**。
9. 依 §4.1 將 SYS2 hot-behaviour 四列（r31–r34）與 CFTS `1.11.2.2
   {4820281}` 併列，判定 R-DM8 之 004／005 是否仍缺值。
   **不得回填任何值**；產出為「缺／不缺 + 證據位置」。
10. 更新 `docs/INDEX.md`。

---

## 七、停止條件

沿用下放包 01 §五九條，另加：

10. §3.3 之錨定方法若在實作中發現任一錨種類需要「相似度」「近似」
    「模糊」才能運作 → 停並回報。錨必須是逐字比對，不逐字即無錨。

---

## 八、上繳包要求（`docs/upstream/03_coverage_redo.md`）

1. §五四條之抄錄核對表
2. `probe_036.py` 兩基準並列之輸出
3. 036 表頭之 `repr` 全欄
4. 新 `coverage_sys2_vs_swe_dm.tsv` 之欄位與統計（依錨種類分列列數）
5. `sys2_heading_tree.tsv` 全文（45 個 Heading 節點）
6. R-DM8 之 004／005 缺值判定與證據位置
7. `A-DM11` 更正後全文、`A-DM12` 新增全文
8. **「本包是否仍有該驗而未驗者」之獨立判斷**
9. 建議之 commit 訊息與 pathspec（不執行）

---

## 九、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 是否已以可貼區塊出現於 §五 |
|---|---|---|
| R-DM12 | 啟發式輸出之命名與引用拘束 | 是 |
| R-DM13 | 覆蓋對照之錨定方法；R-DM7 之文字依據一項廢止 | 是 |
| R-DM14 | 訊號值域之來源為 SYS2 | 是 |
| R-DM15 | 036 母本 B 欄為公式，寫回不觸碰 | 是 |

四條皆為獨立單一事項。
