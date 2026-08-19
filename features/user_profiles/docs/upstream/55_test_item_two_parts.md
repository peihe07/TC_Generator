# 55 上繳 — Test Item 之兩段結構：規格、閘、ENTRY 003

- 產出層：執行層｜2026-08-19｜對象：分析層
- 來源包：`docs/handoff/55_test_item_two_parts.md`
- **git 未執行**；**未送客戶目錄**；**對 comfort／Home 唯讀**

## 0. 一頁摘要

| 作業 | 結果 |
|---|---|
| §二 立閘 | **TI-1／TI-2／TI-3** 入 `audit_delivery_fields`；**首跑對 ENTRY 002 之現況 189 列全紅**（輸出見 §2.1）|
| §一 規格 | 189 條之 `Test Item` 改為兩段；第二段逐條落 `data/test_item_part2.tsv`（**以 `tc_id` 為鍵**）|
| §三 跨 feature | **Comfort 465／466、Home 180／201 皆有第二段** → **本 feature 為唯一漏者**；而**三份之形態各不相同**（§3）|
| §三 查證 | 該規格**不在 repo 之任何文字內**；canon §4.3 反而**把 Test Item 與 tc_title 視為同一物**（§3.3）|
| §四 ENTRY 003 | 已產出；**九項**交付前自檢全綠（新增第 i 項）；`shasum -c` 三個 ENTRY 皆 OK |
| 未做 | `TC-165` 之覆核結果本輪未收到；`TC-167` 之 Tutorials 引用仍缺（PDF 仍不在 `inputs/`）|

---

## 1. §一 —— 規格之落地

```
<tc_title>
(<一句：本條在測什麼>)
```

**第二段之來源為各條 `reasoning` 之「驗證目標」句改寫為英文**（§1.2），
逐條落於 `data/test_item_part2.tsv`。

**以 `tc_id` 為鍵，不以 `req_id`** —— §7 之配對造者與其正向**共用同一個
`req_id`**（`017`／`074` 皆為 `SWE1-HMI-PROF-085`；`013`／`044`／`076` 皆為
`111`）。以 `req_id` 為鍵會把兩條併成一條，**而首版正是這樣寫的**，
在對照 189 條時發現並改正。

實作：`scripts/test_item_part2.py`（查表，**查不到即停**）＋
`gen_pilot`／`gen_batch01._rec` 兩處組裝。
**G3 之判準隨之改一次**：由 `test_item == tc_title` 改為
**`test_item` 之首行 == `tc_title`**，第二段交由 TI-1～TI-3 管。

---

## 2. §二 —— 立閘與首跑

### 2.1 **首跑之紅色輸出**（對 ENTRY 002 之現況）

```
語料 189 條 × 交付欄位 14 欄 = 2646 格；詞表 5 英 ＋ 5 中 ＋ 1 標記

違規 189
  TI-1 NR1L-UserProfiles-001: `test_item` **無第二段** —— 須為 `<tc_title>` 換行
       `(<一句：本條在測什麼>)` → 現值「Profile-linked preferences stored and recalled」
  TI-1 NR1L-UserProfiles-067: … 現值「Go button greyed out until four digits are ent」
  TI-1 NR1L-UserProfiles-068: … 現值「Numeric buttons greyed out once four digits ar」
  …（共 189 列，逐列 TI-1）
```

**189 列全紅**，即 55 包 §二所要求之紅向。**修正後違規 0。**

### 2.2 十六個方向性案例（**16 / 16**）

| 向 | 案例 | 結果 |
|---|---|---|
| **紅** | ENTRY 002 之現況（`test_item` 只有 tc_title） | 紅 |
| 綠 | 兩段齊備 | 綠 |
| **範圍** | 第二段僅一詞 | 紅 |
| **範圍** | 第二段與首段**逐字相同** | 紅 |
| 紅 | 第二段含 modal／含中文／有行尾句點 | 各紅 |
| 護欄 | 第二段剛好 25 詞 | 綠 |
| 紅 | 第二段 26 詞 | 紅 |

（另有 DF-1／DF-2 之七案例，合計 16。）

### 2.3 一處連帶修正

`audit()` 原把 DF 與 TI 併在一起，於是 **DF 之方向性案例（其假列只帶一個欄位）
被 TI-1 判成「首段為空」而全紅** —— **那是案例被另一項檢查誤傷，不是案例錯**。
已拆為 `audit_wording()`（DF）與 `audit_test_item()`（TI），
`audit()` 為兩者之和。

---

## 3. §三 —— 跨 feature 之量測（唯讀）

### 3.1 三份交付件，三種形態

| | 資料列 | 具第二段 | 第一段 | 第二段 |
|---|---|---|---|---|
| **Comfort**（`…_Comfort_20260817_rowsort.xlsx`）| 466 | **465** | **spec 條文原文逐字**（含 `R1C1.)` 之條號）| `(<動作> -> <預期>)`，半形箭號 |
| **Home**（`…_SWQT_Home_20260809.xlsx`，Arif 手寫）| 201 | **180** | **需求敘述**（`The system shall …`）| `(<情境> → <預期>)`，全形箭號 |
| **本 feature**（ENTRY 002）| 189 | **0** | `tc_title` | —— |

**故：本 feature 為唯一完全沒有第二段者。**

### 3.2 Comfort 之第二段是**可重算的**（意外之發現）

逐列比對：`括號內容 == lower1(procedure 最末步) + " -> " + ER 最末行`
之**逐字相符為 459／465**。

其餘 6 條：4 條為 `[BLOCKED-…]` 之無 TC 列（括號改寫為「為何沒有測試用例」），
2 條（`313`／`314`）為**手工改寫**成更貼近意圖之自然語言。

**即：Comfort 之第二段是「最末步 → 最末 ER」之機械衍生，而人可以覆寫它。**
本 feature 依 55 包 §1.2 採**另一種來源**（`reasoning` 之驗證目標句），
**兩者不同，且我方之來源不可由其他欄重算** —— 具名此差異。

### 3.3 **該規格不在 repo 之任何文字內**（54 包第 0 項之事後查證）

搜尋 `docs/**` 與 `features/*/`（`.md`／`.yaml`／`.py`），
關鍵詞 `Test Item`／`test_item`／測項／標題／簡短說明／括號（**中文詞未用 `\b`**，G-I）：

**命中皆為他用**（`ASPICE_SWE6_AI_Review.md` 之審查規則、
`TCGEN_*` 之欄位對映）。**無一處描述兩段結構。**

**而 canon 反向明文**：`ASPICE_SWE6_AI_Instruction.md` §4.3 之標題逐字為

> `### 4.3 Test Item / tc_title — three acceptable shapes`
> `Length **2–14 words**.`

**canon 把 Test Item 與 tc_title 視為同一物**，而本 feature 之 `R-U6` 與
`G3` 據此把二者綁定。

**故三種結果中落在第二種**（「僅在他 feature 之交付件中體現，repo 無文字」）：

> **規則只存在於產物，不存在於文字。**
> 我方嚴格照 canon 做了，而 canon 與交付慣例不一致。

**這不是「規則在檔而未被執行」** —— 55 包 §三預期之最壞情形未發生。

---

## 4. §四 —— ENTRY 003

### 4.1 九項交付前自檢（**新增第 i 項**）

```
a) 189 列：非空 189／相異 189／缺號 []／重號 []；row199 D=None
b) 列序依 Requirement ID 遞增：True
c) 必填 13 欄 × 189 = 2457 格空值 0；priority ⊆P0–P3 True；design_method ⊆ 下拉九條 True
d) 多行格 753；含 CR 之格 0；<t> 內 &#13; 0
e) emoji 0 格；方括號 {'[username]': 3}
f) 行尾句點（J–M）0／受檢 1804 行
g) zip members 48→48（集合相同 True）；x14 節點 1→1；sqref ['R10:R1411']；
   legacy 4→4；verify() 違規 0
h) 內部字樣 30 欄 × 189 = 5670 格，命中 0
i) **Test Item 兩段：合格 189／189；違規 0**
   留空欄：O 0／Q 0／T 0／AA 0／AB 0／AH 0
```

**多行格由 564 增為 753**（＋189）—— 即 `I` 欄全部成為兩行。

### 4.2 台帳

```
…_20260819_full.xlsx: OK        （ENTRY 001）
…_20260819_noremarks.xlsx: OK   （ENTRY 002）
…_20260819_testitem.xlsx: OK    （ENTRY 003，**現行**）
```

### 4.3 未做之兩項

- **`TC-165` 之覆核** —— 55 包 §四稱分析層本輪讀畢，**本層執行期間未收到結果**，
  故未併入。若有 defect 須另起 ENTRY 004。
- **`TC-167` 之 `specification_reference`** —— Tutorials L&F 之 PDF
  **仍不在 `inputs/`**（本輪重查，`find -iname '*Tutorial*'` 0 命中）。
  依 G-L 維持具名缺口。

---

## 5. 連帶：四份 pack 全部重出

`test_item` 現為交付欄之實際內容，而**四份 pack 原本只印 `tc_title`** ——
**覆核者看不到實際交付的那一欄**。已將 `test_item`（兩段）加入 pack 之欄位，
四份全部重出為 `55_review_pack_24a／24b／33a／33b`，舊四份加警語保留。

**這一點很重要**：第二段之**中文來源**已由 189 條之覆核背書，
**而其英文措辭本身沒有任何人讀過** —— 那正是它必須進 pack 的理由。

三份靜態轉錄（`27_rd_queries_v2`／`28_provenance4`／`34_provenance5`）
亦因 `test_item` 變動而轉紅，**逐份查對其轉錄內容未受影響後重標**
（其轉錄的是條文與引號字面值，非 `test_item`）。

---

## 6. 全閘（18 支）

```
lint_tcs 64/64（語料 189，違規 0）      audit_consistency 56/56
audit_delivery_fields **16/16**（違規 0）audit_pending 5/5（新命中 0）
audit_enums 7/7   audit_verbs 5/5      audit_variant_pairs 7/7
audit_assignment 6/6                   audit_delegation 8/8（紅 0）
lint_variant_labels 11/11              lint_outbound_doc 8/8
verify_dv_integrity 6/6                build_review_pack 4/4
stamp_static_doc 5/5                   write_back 12/12
```

**現行四份 pack**：`55_24a` 11／0、`55_24b` 11／0、`55_33a` 17／0、`55_33b` 16／0。
**四份靜態轉錄**：皆 0 不符。

---

## 7. 獨立判斷

1. **本輪之發現推翻了 54 包對成因之假設，而方向是好的。**
   54 包擔心「規則在檔而未被執行 —— 連續兩個 feature 未套用」。
   實測：**規則不在檔**，且 **canon §4.3 明文把 Test Item 與 tc_title 視為同一物**。
   我方不是沒讀規則，是**照著讀到的規則做了**。
   **真正的缺口在 canon 與交付慣例之間** —— 而那個缺口只有在
   「有人拿三份交付件並排看」時才會現形。本輪就是那一次。

2. **第二段之英文措辭是本 feature 唯一「產出後沒有第二人讀過」的交付內容。**
   其中文來源（`reasoning` 之驗證目標句）已由 189 條之覆核背書，
   **但翻譯不是搬運** —— 我在 189 句裡做了無數個取捨
   （哪個子句留、哪個詞更精確、25 詞怎麼塞）。
   **故我把 `test_item` 加進了 pack** ——
   若不加，這 189 句會以「已背書」之名直接進交付件。
   **G-E 說品質由人讀承擔；這 189 句是新的、未讀的東西。**

3. **Comfort 之第二段可由其他欄重算（459／465 逐字），我方的不行。**
   這不是誰比較好，是兩種設計：
   Comfort 之括號是**測項之操作定義**（最末步 → 最末 ER），可機械產生亦可人工覆寫；
   我方之括號是**驗證目標之陳述**，來自 `reasoning`，**沒有任何欄位可以重算它**。
   **代價**：我方之第二段一旦與 `reasoning` 分岔，**沒有閘會發現** ——
   TI-3 只驗形式（英文、無 modal、詞數），不驗它與中文來源是否仍相符。
   **具名此缺口**；若要補，需要的是一支「第二段 ↔ 驗證目標句」之對應檢查，
   而那與 AB-1 同屬「兩端是否指同一件事」之類，機械判不了。

4. **「又」字所指的那件事，答案是：它不是我方漏做，是沒有人寫下來。**
   而它能在第 55 輪被發現，是因為 Pei 拿實際交付件看了一眼。
   **十八支閘、九項自檢、四份 pack、三份靜態轉錄，全部綠著** ——
   因為它們檢查的都是「我方寫下來的規則」。
   **這是本 feature 五十五輪最乾淨的一個教訓：
   閘只能守住已知的規格，守不住沒有人寫下來的期待。**
