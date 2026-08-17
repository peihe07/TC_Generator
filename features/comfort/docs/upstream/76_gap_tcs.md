# 上繳 76 — Comfort HMI / 97 §5 之補產（31 條）

- 產出層：執行層｜2026-08-17｜對象：分析層
- 下放包：`97_gap_tcs.md`（判準訂正與逐項）＋ `98_six_questions.md`（A～F 之裁定）
- 併裁：Pei，2026-08-17 —— **Maserati (Seat & Wheel) 不在 R1LR ATL-H 交付範圍**

---

## 1. 結果

**31 條全數產出，`tc_id` 435–465，語料 434 → 465，57 / 57 gate PASS、0 finding。**

| 節 | leaf | 條 | tc_id | owner |
|---|---|---|---|---|
| `2.1` | `001-01` ×3、`001-02` | 4 | 435–438 | `gen_batch3.py` |
| `2.5` | `006-04` | 1 | 439 | `gen_batch9.py` |
| `2.12` | `016-01` ×4、`-02`、`-03` | 6 | 440–445 | **`gen_batch17.py`** |
| `2.12.2` | `018-01` ×5、`-02`、`-03`、`-04` ×3、`-05`、`-06` | 12 | 446–457 | **`gen_batch17.py`** |
| `2.13` | `019-02` | 1 | 458 | `gen_batch9.py` |
| `9.1` | `039` | 1 | 459 | **`gen_batch17.py`** |
| `10.4` | `047`（第二條） | 1 | 460 | `gen_batch5.py` |
| `14.15` | `099` | 1 | 461 | **`gen_batch17.py`** |
| `16.16` | `122-02` | 1 | 462 | `gen_batch6.py` |
| `18.1` | `129-01`／`-02`／`-03` | 3 | 463–465 | **`gen_batch17.py`** |
| | | **31** | | |

**`019-03` 維持不產**（其列為 96 §1 之留空列），**`072` 維持 `[BLOCKED-SPEC]`**。

### 1.1 實測之數

| 量 | 值 |
|---|---|
| TC 總數 | **465**，`tc_id` 001–465 **連續無洞**（實測） |
| 有列之 leaf | **402 / 403** —— 缺者僅 `019-03` |
| 工作簿列數 | **466**（465 TC ＋ 1 留空列），與 98 §1 相符 |
| marker 列 | 4（`080-02`／`081-02`／`072` 之 `[BLOCKED-SPEC]`、`044-02` 之 `[BLOCKED-NON-HMI]`），未變 |
| 生成之節 | **129 / 129** —— 本包之後，129 節全數有列 |

**既有 434 列一列都未重編**（65 §1）：新 `tc_id` 明寫於 `gap_tcs.py`（R-C43），
依 req_id 遞增指派。

---

## 2. 三件本包才看得見的事

### 2.1 反向驗證因為語料變完整而停止運作

`verify_provisional_gate.py` 之否定側案例取自語料 ——
`next(o for o in SECTION_TEST_SET if o not in generated)`。
**本包使 129 節全數生成，該式即拋 `StopIteration`。**

> **一個反向驗證，在語料變完整的那一刻停止運作** ——
> 而那正是它最不該停的時候。

已改以一個**不存在於語料**之節次（`99.99`）充當否定側，並加 assertion
釘住「否定側必須是未生成者」。六向全 PASS。

**其一般性值得記**：凡以「語料中找一個不滿足條件者」建立否定側之反向驗證，
其否定側會隨語料完備而消失。`R-C43`（以身分取代邊界值）管的是同一類問題之
另一面 —— 此處是**否定側之來源**，不是邊界值。

### 2.2 `17.1` ↔ `18.1` —— 候選產生器構造上到不了的那一對

`equivalence-in-sibling-table` gate 於本輪抓到：`124-01/-02/-03` 與
`129-01/-02/-03` 之 `test_item`／`test_procedure`／`expected_result`
**三欄逐字相同**。

**而該對不在候選表內，且不可能在**：兩節之 full_text 皆為
`W0.) The Comfort widget will have two screens: Comfort and Seats.`，
其中**無任何 `VOCAB` token** → 詞彙重疊為空、階層亦不連。

> **一個產生器到不了的對，正是沒有人會注意到的那一對。**

已補入 `pending_sibling.tsv`（verdict `sibling`、`source =
identical-TC (產生器到不了)`），`duplicate_of` **不填**（037 對同一句條文在
兩章各產出三個 leaf，§8.2.2 禁本層合併）。

**其後果須向上游講明**：**於 10.25" 之車上，測試員會把同一個測試做兩次。**
形態同 `16.2` ↔ `16.6`（DR #42），惟本對兩側**分屬兩章**且其區辨僅在章標題。

### 2.3 `9.1` 之列補上後，一個候選之 reach 少算了一節

`9.2`／`9.3`／`9.4`／`9.4.1` 之七條**以 `9.1` 之句子為 PC**，
而 `9.1` 自身之 leaf 此前無列 —— **七條引一個在工作簿上不存在的條件**
（97 §2.5 已指出）。

本包補列後，`axis-candidate-registered` gate 立刻紅：profile 之
`pending-axis` 宣告 `sections: 9.2 | 9.3 | 9.4 | 9.4.1`，而語料實測為
**含 `9.1` 之五節**。已更正並記其由來。

> **候選之 reach 是量出來的，不是記得的** —— 而它少算的那一節，
> 正是那個條件的出處本身。

---

## 3. 六問之落地 —— 逐項對照 98

| 問 | 98 之裁定 | 落地處 |
|---|---|---|
| **A／B** | 依 **R-C33**（單位歸 037、內容歸 spec）取 4 tabs、順序含 Massage | `PC_TABS_4/3/2` 與 `438` 之 ER；`reasoning` 具名 A-CF21，**未另立新 RD 項** |
| **C** | 不借掛 `016-01`，登 R-C16 缺口 | profile §5.4 **第六項成員**（§4.1）；`016` 之 `reasoning` 具名 |
| **D** | `018-04` 拆 3，依 §5.7 校正其組成 | `453`（彈窗出現＋不跳轉，**同一觸發併一條**）／`454`（3 秒）／`455`（他鍵）；`SPLIT_018_04` 逐字寫其判準 |
| **E** | `018-01` 之 Defrost 另立 1 條（§7 之 `ALWAYS`） | `450`，走完整個迴圈驗 Defrost 自始至終不出現 |
| **F** | `016-02` 不展開 | `444` 一條；`reasoning` 具名 §10.6 之近重複 |

### 3.1 Maserati —— 已依 Pei 2026-08-17 之裁定落地

- `2.1` 維持 **4 條**，**不增變體標籤 TC**（§8.7.3 於本交付不適用）
- tab 名稱一律寫 `Seats`；`test_item` 上半為條文原文逐字（95 §1），
  故 `Seats (WS or R1 Low) or Seat & Wheel (Maserati)` 仍出現於該欄上半 ——
  98 §2 已裁此為兩欄各司其職，非規則衝突
- **profile 之市場／變體軸已記註**（§4.2），使日後不需重問

---

## 4. 落檔清單

### 4.1 profile（`docs/runtime/profiles/FW036_R1L_Comfort_Profile.md`）

| § | 改動 |
|---|---|
| **§5.4** | **新增第六項成員** —— `2.12` 之四模式列舉與其順序；**形態與既有五者分記**（見下）；並如實記其被涵蓋之程度 |
| §3.2 之三個 `axis-values` 區塊 | `negation-users` 依語料重算：軸 13 → 444、EMEA → 298、軸 9 → 366 |
| §3.2.1 之 `pending-axis`（ch9 變體） | `sections` 加 `9.1`，並記其少算之由來（§2.3） |
| §3.2 之市場／變體軸 | 記「Maserati 不在本交付範圍（Pei 2026-08-17）」 |

**§5.4 第六成員之形態，與既有者分記**：

| 成員 | 形態 |
|---|---|
| `16.1`／`18.2`／`18.3`／`18.4` | 整節未被 037 引用 |
| `15.1` 之圖表部分 | 節被引用，而節內之**一張圖表**未被引用 |
| **`2.12` 之四模式列舉與其順序** | 節被引用、**其行為亦有 leaf**，而該節之**一項列舉**未成為任何 leaf |

> **以節為單位掃描找不到它，以「節內有無未引用之圖」掃描也找不到它。**
> 找到它的是**逐句對 leaf** 之比對。

**其被涵蓋之程度如實記**：四模式之**存在**因 `440`–`443` 逐一選取而**間接被驗**，
**其顯示順序未被任何 TC 驗證** —— 兩者分別陳述，不以前者掩蓋後者。
**`ch16_mirror_map.tsv` 之 `16.12 ↔ 2.12` 列已獨立記載同一缺口**
（分界欄逐字寫「未涵蓋：C13 之四模式清單與其順序」）——
**兩個各自建立之記錄指向同一件事，本項因而不是單一判斷之產物。**

### 4.2 新檔

| 檔 | 內容 |
|---|---|
| `scripts/gap_tcs.py` | **31 列之單一來源**，`tc_id` 明寫（同 `external_docs.py` 之形態，R-C43） |
| `scripts/gen_batch17.py` | 五個**此前無檔**之 parent（`016`／`018`／`039`／`099`／`129`，23 條）之 owner |
| `scripts/resolve_pending_98.py` | 86 列 `provisional` 之逐對再確認（§5） |

### 4.3 既有 generator 之改動

| 檔 | 改動 |
|---|---|
| `gen_batch3.py` | `WITHHELD` 清空（`001-01`／`-02`）；2.1 之 doc 接 4 列；算式 16 → 20 TC |
| `gen_batch5.py` | 10.4 接 1 列；**既有之 `NR1L-ComfortHMI-070` 補 `split_flag`／`split_reason`**（§8.2.2：一個拆分要在它產出的每一列上都看得見）；算式 15 → 16 TC |
| `gen_batch6.py` | `WITHHELD` 清空（`122-02`）；16.16 接 1 列；算式 16 → 17 TC |
| `gen_batch8.py`／`gen_batch10.py`／`gen_batch11.py`／`gen_batch14.py` | 其 `WITHHELD` 之對應 leaf 改列 `MOVED_TO_BATCH17`，**仍在算式內** —— 一個搬走之 leaf 不得看起來像一個消失之 leaf |
| `gen_batch9.py` | `WITHHELD` 只留 `019-03`；2.5／2.13 各接 1 列；算式 28 → 30 TC |
| `verify_provisional_gate.py` | 否定側改用不存在之節次（§2.1） |

### 4.4 資料檔

- `data/interface_axis_review.tsv` **＋5 列**（`2.12`／`2.12.2`／`9.1`／`14.15`／`18.1`），
  現 **129 / 129 節**，**無既有列被改動**（實測 diff：5 insertions、0 deletions）
- `data/leaf_clause_sentence.tsv` 434 → **465 列**；重跑兩輪**逐位元組相同**（穩定）
- `data/pending_sibling.tsv` 86 列再確認 ＋1 新列（§5）
- `data/coverage_audit.tsv` 隨語料重算

---

## 5. `pending_sibling` 之 86 列 —— 本包所到期之再確認

`provisional-sibling` gate 於本包落地後立刻紅：**86 列 `provisional=true`
之兩側現皆已生成**。其停下之理由**逐字寫在它們自己的 reason 欄**：

> 兩節皆未生成，現在判無處可用 …… **其所屬組生成之日連同其他候選一併判定。**

**那一天即今日** —— 86 列全數涉及 `2.12` 或 `2.12.2`，而本包正是生成該二節者。

**方法 `[machine]`，與語料既有之 1,861 列同法**（`resolve_pending_98.py`）：
`identical-TC scan` 三欄比對 ＋ `sibling_candidates.py` 之 `VOCAB` 共有語彙。

**實測：86 對之中，三欄逐字相同之對為 0。** 故 86 列全判 `not-sibling`，
`provisional` 改 `false`，`reviewed_at` 記 465。其中 **69 個 `deferred` 與
4 個 `(class)` 換成了逐對之答** —— 兩者依 41 §4／42 §1 永不得為終判，
本輪之作用即在此。

**列序未動**：重排會使 86 列之實質變更淹沒在 1,400 列之位移裡
（實測 diff：87 insertions、86 deletions）。

> **請分析層覆核之處**：86 列之 verdict 由本層依既有方法判出，
> **其方法可複驗（重跑腳本即得同一結果），其判斷未經分析層裁定**。
> 若 `not-sibling` 之判準應更嚴（例如要求逐條讀 ER 而非只驗三欄逐字），
> 請下裁，本層重跑。

---

## 6. 三處措辭之選擇，請覆核

### 6.1 `18.1` 之 PC 出處為**章標題**

`10.25" Home screen` 出自 SR24 export 之**章標題**，不是條文句子。
批次 8 曾以此為由停下三個 leaf；97 §2.7／98 §1 裁定生成，故本層寫下：

```
2. [spec-derived] The vehicle has the 10.25" head unit screen,
   the screen whose Comfort widget chapter 18 states (18.1)
```

**此為全語料唯一一處 PC 之出處為章標題而非條文句子者**，
已逐字記於 `gap_tcs.py` 之 `PC_1025` 並於 `reasoning` 具名，
**使它日後不被讀成一般用法**。

### 6.2 `450` 之 `test_item` 上半不含 Defrost 一語

`clause_map.py` 之 `sents()` 於 `C13.1` 之括號處斷句，致
`Defrost will not be included in the loop)` 落入 `018-02` 之句而非 `018-01` 之句。
故該負向條之上半為迴圈句，**Defrost 之驗證由其下半與 ER 承載**。

**此為切句工具之界線，非選錯句** —— `clause_map.py` 自陳「括號在本語料裡不是
可靠的句界訊號，故不用」，而那個決定是為了 `7.4` 之九句不被併成四句。
**兩者不可兼得，本層照既有決定，不為一條 TC 改切句規則。**

### 6.3 `460` 之 PC 取軸一之**正向**值

`(AUTO is not shown in MTC configurations)` 為 `2.3`／`16.3` 之逐字括號，
**其為本條之驗證目標而非前提**，故落 ER 而不落 PC ——
寫成否定式 PC 會使它同時是前提與結論，且該否定不對應任何軸值（43 §4，
`axis-value-count` gate 實測攔下第一版）。PC 因而寫
`The climate system is MTC (2.3)`。

**RD-1 第 7 問（not shown 是否等於 not available）不再阻塞此條**，
依 97 §2.6 —— 該判斷屬測試員於實車上之觀察。**RD-1 本包未動**（97 §4）。

---

## 7. 未動者（97 §5 第 4 項）

- **未寫回**：`output/` 三份工作簿與 `DELIVERY.sha256` **未觸及**
- **未動交付夾**
- **未改 RD-1**：`docs/RD1_questions_comfort.md` 未觸及 ——
  其重寫（含第 7 問之移除、第 1／2／3／4／6 問之解除阻塞）依 97 §4 另行處理
- **未改 `DATA_REQUESTS.md`**：DR #31／#32／#38／#41 之**問句皆不撤**
  （它們問的仍是「哪一種配置」，只是不再阻塞生成），其現況記於各條之
  `reasoning`；**DR #41 之 reach 更正已落 profile**（§2.3）。
  若應同步更新 `DATA_REQUESTS.md` 之措辭，請下裁
- **git 未執行**任何寫入指令。惟本層曾以 `git checkout
  features/comfort/data/pending_sibling.tsv` **還原本層自己一次寫壞之排序**
  （該次寫入誤將全表重排）；還原後以不重排之版本重寫。**如實記之。**

---

## 8. 檢查

```
57 / 57 gates PASS; 0 finding(s) across 465 TCs
```

反向驗證八式全 PASS：`verify_b_gates`／`verify_axis_gate`／
`verify_axis_type_gate`／`verify_partn`／`verify_no_tcid_gate`／
`verify_provisional_gate`（改後，6/6）／`verify_equiv_invariant`／
`verify_ledger_gate`。

`clause_map.py` 重跑兩輪，`leaf_clause_sentence.tsv` 逐位元組相同 ——
**新 31 列之上半選句經逐條核對，10 節之選句全部正確，未新增任何 `OVERRIDES`。**
