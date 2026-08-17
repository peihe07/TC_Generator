# 69 — Comfort HMI / Q7 寫入、全稱否定之全面複核、M6 併入 Q9、換版 SR25

- 產出層：執行層｜2026-08-17｜對象：分析層
- 覆核對象：`docs/handoff/89_rd1_negatives.md`
- **未生成 TC、未動交付夾。**「不寫回」本輪未在指示內 —— 惟本輪之改動**觸及語料**，見 §5。

---

## 0. 供覆核之全文（89 §5.3）

### 0.1 第 9 問（已併入 M6）

> ## 9. Which document defines whether comfort **settings** survive an ignition cycle?
>
> **Units blocked**: 0 — this question stops nothing; it may add work rather
> than unblock it.
>
> **Narrowed since the last version**: the Last Mode Table defines what happens to
> the comfort **screen** across a power cycle — three rows name the COMFORT
> category and give its behaviour ("Return to Comfort Main / Front Comfort
> Screen", "Maintain Mode", "Return to Front Comfort Tab"), and their reference
> column points back at the Comfort HMI Logic and Flow. **That half has an
> owner, so we are not asking about it.**
>
> **What is missing**: the other half. Of the verification units we examined,
> **at most 222 describe a state the user sets** (an upper bound — the count was
> taken by a keyword rule that errs towards including) — AUTO on or off, fan
> speed, airflow mode, seat heating level — **and none of the documents we have
> read states whether any of those values is retained after an ignition cycle or
> a cold boot**. The Last Mode Table restores the screen, not the setting.
>
> **One nearby document does state it, for a different feature.** The Massage
> Seats HMI Logic and Flow says:
>
> > M6.) The Massage feature will be Off after an ignition cycle, regardless of
> > the previous state.
>
> We record this only as a fact about how this family of documents is written:
> the behaviour after an ignition cycle is something these specifications do
> state when it applies. Whether its absence from the Comfort document is an
> omission, a deliberate silence, or a behaviour owned elsewhere is what we are
> asking.
>
> We checked the power-management specifications (CFTS009 Wake-up and Power-up,
> CFTS010 Power Down) before asking. They state that climate pop-ups are shown
> and HVAC controls stay active in certain power states, and they require the
> restoring of *audio and telematics* settings by name — **but they say nothing
> about retaining climate or seat settings**.
>
> **What we have done**: nothing. Writing a test for "the fan speed is still 3
> after a restart" would be inventing a requirement, so we have not written one.
>
> **Once answered**: if the behaviour is owned by another document, we record the
> owner and write nothing. If it belongs to Comfort, this becomes a batch of new
> test cases rather than a correction to existing ones.
>
> ---

### 0.2 第 6 問（其依據經重驗後訂正，見 §2.2）

> ## 6. What distinguishes section 18.1 from section 17.1?
>
> **Units blocked**: 3 — `SWE1-HVAC-129-01` … `-03` (section 18.1)
>
> **The sentence**:
>
> > W0.) The Comfort widget will have two screens: Comfort and Seats.
>
> **What is missing**: this sentence is **word-for-word identical** to the one in
> section 17.1, and nothing in section 18.1 says which vehicle it applies to.
>
> Two things we can state precisely, because both were measured rather than
> assumed:
>
> - Section 17.1 carries **one sentence more** than 18.1 — a pointer to the
>   front-climate and heated/vented-seat sections "for complete logic". It is a
>   cross-reference, not a distinguishing requirement, so it does not tell a
>   tester which chapter applies to the vehicle in front of them.
> - **We cannot compare the two chapters as wholes.** Only 18.1 appears in the
>   requirement analysis; sections 18.2 to 18.4 produced no verification units,
>   so we have not read them as requirements. The comparison above is between
>   **18.1 and 17.1**, not between chapter 18 and chapter 17.
>
> **What we have done**: chapter 17's three units are tested. Section 18.1's
> three are not, because the test cases would be identical to 17.1's with
> nothing to tell a tester which vehicle each applies to.
>
> **Once answered**: if the two differ by screen size, the screen size is stated
> as a pre-condition and three test cases are written. If 18.1 is a duplicate of
> 17.1, the three units are recorded as covered by chapter 17.
>
> ---

### 0.3 第 7 問（已寫入，與 68 §0.2 之提案逐字相同）

> ## 7. Does "not shown in MTC configurations" mean AUTO is unavailable?
>
> **Units blocked**: 1 — `SWE1-HVAC-047` (section 10.4)
>
> **The sentence**:
>
> > EH4.) When the AUTO function is off **and available**, the user's first
> > press of the AUTO button will activate the AUTO ECO functionality.
>
> **What we found**: two sections state one condition under which AUTO is not
> shown —
>
> > C2.) / ICE2.) … **(AUTO is not shown in MTC configurations)** — sections 2.3
> > and 16.3
>
> and that configuration is already a pre-condition in this delivery: test cases
> exist for both the automatic-climate and the manual-climate case.
>
> **What is missing**: whether "not shown" is what EH4 means by "not
> **available**". The document uses the two phrases in different places and never
> relates them. If they mean the same thing, the negative case can be set up
> today by putting a manual-climate vehicle on the bench. If they do not, we
> still have no way to make AUTO unavailable.
>
> **We are not assuming they are the same.** Treating "not shown" as "not
> available" would put our reading in place of a sentence the requirement never
> wrote.
>
> **What we have done**: the available case is covered. The unavailable case has
> no test case.
>
> **Once answered**: if the two mean the same, one test case is written with the
> manual-climate configuration as its pre-condition. If not, please state when
> AUTO is unavailable.
>
> ---

---

## 1. 第 7 問 —— 已寫入

`RD1_questions_comfort.md` 之第 7 問已由提案改為正文，摘要表之該列同步。
其全文見 §0.3，**與上繳 68 §0.2 之提案逐字相同**，未於寫入時另行修飾。

---

## 2. 全部 22 問之全稱否定 —— 形態式掃描與逐句複核

### 2.1 掃描

pattern（**形態非清單**）：**否定形態 × 範圍詞**之交集 ——
否定側 `no`／`not`／`never`／`nowhere`／`none`／`nothing`／`without`／
`cannot`／`could not`／`does not`／`has no`／`carries no`／`found no`；
範圍側 `section(s)`／`document(s)`／`clause`／`chapter`／`table`／`mapping`／
`anywhere`／`any`／`all`／`every`／`specification`／`material`。

**全檔 19 句命中**，其中**真正之全稱否定（對某一整個搜尋空間作斷言）7 句**，
其餘 12 句為對單一條文或單一文件之陳述（如「該封面不含 icon 表」），
不構成全稱否定。

### 2.2 七句逐句複核

| # | 句（節錄）| 所斷言之範圍 | 當時之搜尋範圍 | 現行語料重驗 | 處置 |
|---|---|---|---|---|---|
| 1 | `no section in the document says when AUTO is unavailable`（Q7）| 全 129 節 | 129 節通讀，**未以該詞搜過** | **不成立** —— `2.3`／`16.3` 各一句 `(AUTO is not shown in MTC configurations)`，實測 2 句 | **已改寫**（§0.3）|
| 2 | `The only difference between the two chapters is the chapter heading`（Q6）| ch17 對 ch18 之全部 | 兩節之逐字比對 | **不成立（兩處）**：(a) `17.1` 較 `18.1` **多一句**（指向前排氣候與座椅章節之交叉引用）；(b) **兩章無從整章比對** —— `18.2`～`18.4` 未產出任何 leaf，不在 129 節內，我方從未以需求讀過它們 | **已改寫**（§0.2）—— 標題亦自「chapter 18 vs chapter 17」改為 **「section 18.1 vs section 17.1」** |
| 3 | `The four-mode set (C13) still carries no condition of its own **anywhere we have looked**`（Q2）| 已看過之處 | 129 節 ＋ CFTS043 ＋ MCT | **成立**（其已自帶範圍限定語）—— 實測：129 節中提及四氣流模式者 4 句，皆述模式與其高亮，無一給適用條件 | **範圍具名化**：把「anywhere we have looked」展開為三個具名來源 |
| 4 | `no section carries that mapping`（Q3，指 `see Climate section`）| 全 129 節 | 129 節 | **成立** —— 實測 icon×對照之句 3 句（`2.5`／`16.5`／`16.16`），三者皆**指向**對照而無一**是**對照 | 維持 |
| 5 | `No document named "HMI Notes" exists in the material available to us`（Q8）| **已自帶範圍**（material available to us）| 客戶樹全樹 `find` ＋ 系統層 `mdfind` ＋ 四個 repo | **成立** | 維持 —— 其範圍已寫在句子裡 |
| 6 | `no document we have says whether any of those values is retained`（Q9）| 我方所有文件 | CFTS009／CFTS010 ＋ 已取得之外部文件 | **成立而須補一項事實** —— Massage Seats 之 `M6` 陳述了**另一個功能**於點火循環後之狀態 | **已改寫**：措辭自「no document we have says」改為「**none of the documents we have read** states…」，並補入 M6（§0.1）|
| 7 | `the document does not say` / `no test asserts either way`（附錄）| 全 129 節 | 129 節 | **成立** | 維持 |

### 2.3 一項須明說的事

第 2 句之錯與第 1 句**不同型**，且更難發現。

第 1 句是「沒查而說沒有」。第 2 句是**查了，但把查的結果說得比它大** ——
我方逐字比對過 `17.1` 與 `18.1` 之 W0 句（那部分是對的），
**卻把結論寫成「兩章之唯一差別是標題」**，而我方從未讀過 `18.2`～`18.4`
（它們根本不在 129 節內）。

**「我比對過的那兩節」與「那兩章」之間，隔著三節我沒讀過的東西。**

---

## 3. M6 併入第 9 問 —— 措辭之三項限制

全文見 §0.1。其守則之落實：

| 限制 | 落實 |
|---|---|
| **陳述事實** | 逐字引 `M6.)`，並標明其出自 Massage Seats HMI Logic and Flow |
| **不預測答案** | 未寫「因此 Comfort 也應該有」「我們認為應補上」；改寫為 `We record this only as a fact about how this family of documents is written` |
| **幫上游定位** | 明列三種可能：`an omission, a deliberate silence, or a behaviour owned elsewhere` —— **三者並列而不指其一** |

原句之 `no document we have says` 亦一併改為
`none of the documents we have read states` —— **「我們有的」與「我們讀過的」
不是同一個集合**，而可稽核的是後者。

---

## 4. 換引 SR25 版（89 §3）

| 項 | 改動 |
|---|---|
| `external_docs.py` | `EXT_SETTINGS` → `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026)_Settings`；其上方註記記換版之依據與量測 |
| profile §1.1 | 該列改指 `inputs/` 之 SR25 版，原引用出處以〔〕保留；版本落差欄記「兩版 30／31 節逐格相同（實測）」 |
| `-382` 之 `reasoning` | 增一句記其換版：原引 SR24 Post 2A，今引 SR25 R1L-R，**依據是該量測而非版本之新舊** |
| 對 Pei 之補檔請求 | **撤銷**（上繳 68 §7 第 1 項）—— 判準三於改引 SR25 後即已滿足 |

### 4.1 換版觸發了一道 gate，且該 gate 之修正須被看見

`spec-ref-sr25` 原式為 `if "SR25" in ref` —— 對整個 `specification_reference`
字串搜 `SR25`。換版後 `-382` 立即 FAIL。

**該 gate 沒有錯，是它的範圍寫得比它的理由大**：R-C1 禁的是
**Comfort spec 之基線為 SR25**，不是「任何文件之名字裡不得出現 SR25」。

改為**逐段檢查並以身分豁免已認可之外部出處**（`EXTERNAL_REFS`）。
**反向驗證兩案已加入 `verify_b_gates.py`**：

- Comfort stem 之 SR25 引用**不在**已認可清單內 → 仍會被檢查（PASS）
- 已認可清單中帶 SR25 者**恰為一件**（HMI Settings List）→ **豁免之窄度可量**（PASS）

**一道被放寬的 gate，其放寬幅度必須可量** —— 否則下次沒人記得它寬到哪裡。

---

## 5. 語料已變動 —— 現行工作簿與交付物皆已落後

**89 §3 稱「語料不需重跑」，該句在本例不成立，本層於上繳 68 §1.2 已先報，此處為其實現。**

`EXT_SETTINGS` 進入 `-382` 之 `specification_reference`，即工作簿之 **N 欄**。
換版後：

| | |
|---|---|
| `generated/SWE1-HVAC-058.json` | **已變**（N 欄之末段自 SR24 改為 SR25）|
| lint | **54 / 54 PASS，0 finding across 434 TCs**（gate 修正後）|
| **ENTRY 026 之工作簿** | **與語料不一致** —— 其 `-382` 列仍寫 SR24 |
| **已交付之副本**（ENTRY 028）| **同上** |

**本輪未寫回、未重新交付** —— 兩者皆非本包指示，且重新交付屬 Tier 3。

**待裁定**：

- (a) **重寫回並重新交付**（一列一欄之差異，代價是一次完整交付）
- (b) **維持交付物不動**，待下一次因其他理由重寫回時一併帶入
- (c) 撤回換版（回到 SR24），交付物與語料即刻一致

本層之判斷：**(b)** —— 該差異為出處字串之版本名，其所指之事實逐格相同；
交付物之內容不因此為錯。惟 **(b) 期間台帳與交付物之關係須明記**：
現行交付物**不是**現行語料之產物，而是其前一版。**若不記，下一個人會以為它是。**

---

## 6. Massage Seats 入未認可表

profile §1.1 之未認可表已列（上輪 88 §7 執行時一併加入，本輪確認在位）：

> **已查而不解**（2026-08-17 唯讀查證）：`2.1` 指向它，而它**不載配置 → tab
> 組之對照**；所載為 Massage tab 之切換時機（M1／M3）與 back/cushion 之配備
> 條件（M5）。DR #17 之問句不變。

---

## 7. 現況

- lint **54 / 54 PASS，0 finding across 434 TCs**
- 反向驗證 **7 支全 PASS**（`verify_b_gates` 新增 2 案）
- `BASELINE.sha256` 11 列全 OK；台帳 gate 驗過 68／已知不存在 1／問題 0
- RD-1：**22 問**，其中第 6、7、9 問本輪改寫；**仍未送出**（89 §5 之附帶條件已滿足，待分析層覆核 §0）

**未做**：未生成 TC、未寫回、未重新交付、未動交付夾、未搬檔至 `inputs/`；git 未執行。
