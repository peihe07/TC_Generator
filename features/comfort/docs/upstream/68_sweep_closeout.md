# 68 — Comfort HMI / 盤點收尾：版本判準之適用、SYS2 不引、路徑改指、A-CF23 擴充

- 產出層：執行層｜2026-08-17｜對象：分析層
- 覆核對象：`docs/handoff/88_sweep_review.md`
- **未生成 TC、未寫回、未動交付夾。RD-1 之改寫為提案，未套用。**

---

## 0. 供覆核 —— RD-1 第 7 問之改寫措辭（**提案，尚未寫入 RD-1**）

### 0.1 現行全文（`docs/RD1_questions_comfort.md` 第 231–250 行）

> ## 7. When is AUTO unavailable?
>
> **Units blocked**: 1 — `SWE1-HVAC-047` (section 10.4)
>
> **The sentence**:
>
> > EH4.) When the AUTO function is off **and available**, the user's first
> > press of the AUTO button will activate the AUTO ECO functionality.
>
> **What is missing**: the clause makes the behaviour conditional on AUTO being
> "available", and **no section in the document says when AUTO is unavailable**.
> We can test the available case, which we have; we cannot test the other side,
> and we cannot tell a tester how to put the vehicle in it.
>
> **What we have done**: the available case is covered. The unavailable case has
> no test case.
>
> **Once answered**: one test case is written for the unavailable case, with the
> condition stated as a pre-condition.

### 0.2 提案之改寫全文

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
> > C2.) / ICE2.) … **(AUTO is not shown in MTC configurations)** — sections
> > 2.3 and 16.3
>
> and that configuration is already a pre-condition in this delivery: test
> cases exist for both the automatic-climate and the manual-climate case.
>
> **What is missing**: whether "not shown" is what EH4 means by "not
> **available**". The document uses the two phrases in different places and
> never relates them. If they mean the same thing, the negative case can be set
> up today by putting a manual-climate vehicle on the bench. If they do not,
> we still have no way to make AUTO unavailable.
>
> **We are not assuming they are the same.** Treating "not shown" as "not
> available" would put our reading in place of a sentence the requirement never
> wrote.
>
> **What we have done**: the available case is covered. The unavailable case
> has no test case.
>
> **Once answered**: if the two mean the same, one test case is written with
> the manual-climate configuration as its pre-condition. If not, please state
> when AUTO is unavailable.

**改寫之要點**：標題自「有沒有任何條件」改為「這一個條件算不算」，
並載明**我方原先寫錯了什麼** —— 舊文之「no section says」是一句全稱否定，
而那句話就在 `2.3`／`16.3`，且我方在別處以它為第一軸之出處。

---

## 1. `HMI Settings List` 之版本 —— 比對結果與**所選依據**

### 1.1 比對（88 §2 判準二）

| | `inputs/` 之 SR25 R1L-R (Feb 13 2026) | 客戶目錄之 SR24 Post 2A (June 15 2023) |
|---|---|---|
| `Settings` 工作表列數 | 1,015 | 1,015 |
| 30／31 節之列 | r104–r110 | r107–r113 |
| **逐格比對（各 7 列）** | **完全相同** | 同左 |

其七列逐字：`30 Auto-On Driver`／`30.1 Heated Seat｜Heated_Seat`／
`30.2 Heated Steering Wheel｜Heated_Steering_Wheel`／`30.3 Vented Seat｜Vented Seat`／
`31 Auto-On Passenger`／`31.1 Heated Seat`／`31.2 Vented Seat`。
列號差三，因 SR25 版少一個 `SR24 Change Log` 工作表所致之上移。

### 1.2 所選之依據：**SR24 Post 2A (June 15 2023)**，不換版

判準二之「內容相同 → 得改引 SR25」是**選項而非義務**，
而判準一（引用發生在哪一版，依據即是哪一版）與 R-C1 之精神
（**與所引之時點一致，而非與最新一致**）同向。故不換。

**且判準二附註之「語料不需重跑」在本例不成立，此點須明講**：
`EXT_SETTINGS` 之字串為 `HMI Settings List R1 SR24 Post 2A (June 15 2023)_Settings`，
它**進到工作簿之 N 欄**（`-382` 之 `specification_reference` 末段）。
改版本名即改一列已交付之儲存格 → 須重跑 lint、重寫回、重新交付。

**換言之，換版之代價不是「改一行常數」，而是「再交付一次」。**
內容既然相同，這個代價買不到任何東西。

### 1.3 因此產生之一項待辦（判準三）

判準三要求 `inputs/` 存放**被引用的那一版**，而現放者為 SR25。
**故 profile §1.1 該列已加 ⚠ 標記**：

> ⚠ 尚未入 `inputs/`，故未受 `BASELINE.sha256` 保護 —— 待 Pei 補入

**該標記即「這一列現在還不可複驗」**。素材補入屬 Pei，本層不自行搬檔。
（SR25 版已在 `inputs/` 且已入 BASELINE，其留置無害 —— **列入保護與可否引用
是兩件事**。）

---

## 2. SYS2 報告 —— 已入「未認可」表

profile §1.1 之未認可表新增一列，其理由逐字引該文件自身：

> `SYS-RA-HVAC-007`：`In the case of conflict between this document and the
> HMI requirements, **the HMI requirements shall have precedence.**`

**該文件自己說了它不是行為之依據。** 並記其得作唯讀之對照與導覽
（同 R-C18 對 `layer3_map` 之處置：可看，不可據以判讀）。

---

## 3. 路徑改指 `inputs/`

| 檔 | 改動 |
|---|---|
| profile §1.1 | 表頭改為「**引用對象之路徑**（以受 `BASELINE.sha256` 保護者為準）」；CFTS043 與 Pop Up List 改指 `inputs/`，客戶目錄之原始出處以〔〕附註保留；HMI Settings List 保留客戶目錄路徑並加 ⚠（見 §1.3）|
| `external_docs.py` | 於 `EXT_*` 常數上方記各字串之對應檔案與其路徑，並記「**改字串即改 workbook 之 N 欄，故版本名一旦寫下，換版就是換依據，不是改一行常數**」|

**規約已寫入 profile**：引用之路徑指向**會被檢查的那一份位元組**；
客戶目錄不在本 pipeline 控制下，其被替換時無人出聲。
**來源可考，依據可驗，兩者都要。**

**`EXT_*` 字串本身未動** —— 它們是文件名 ＋ section，不含路徑，
故本項改動**不觸及語料**（lint 54/54 PASS，434 TCs 未變）。

---

## 4. `RUNBOOK.md` 之兩則

### 4.1 R-C43 段增第三例

`write_back.py` 之 `BASELINE.sha256 8 檔全數 OK`，於 `inputs/` 自 5 增為 8 後
立即失效 —— **素材變多了而檢查壞了**。三例並列（`len(withheld) >= 20`／
`len(LEAF_UNIVERSE) == 403`／本例）並記其共同形狀：

> gate 要證的是「每一列都驗過且都對」，而那句話裡本來就不該有一個數字。
> **數字進到一個 gate 裡，通常是因為寫的時候剛好數了一下。**

### 4.2 形態式 vs 清單式

新節「形態式 pattern 找得到的，比清單式多一種東西」，其要點：
**改為純形態後，結論不是「找到更多」，是兩個 0 命中變成了資訊** ——
`PROXI`／`$…$` 與 `defined in` 於 129 節皆 0，即本 spec 不以參數名指涉配置、
不用該句式，**它們界定了這份文件的說話方式**。並記
`2.1` 之 Massage Seats 第一版被找到是因為它恰好含 `Logic and Flow`，
**若那份文件叫別的名字，第一版就會漏掉它，而漏掉不會出聲**。

---

## 5. A-CF23 之標題與範圍，`15.1` 之 chart

### 5.1 A-CF23

標題改為 **「spec 內以圖承載之內容，本 pipeline 讀不到」**（原為
「SYS1 export 之圖片內容不可讀」），範圍表列四項成員：037 之 52 個圖片標記
（25 leaf）／export 之 0 命中／**`15.1` 之 chart**／`12.7`（呈現要求，不構成缺口）。
摘要表該列一併改述。

並記其與缺件之分別：

> 東西就在我方所引之 spec 裡，**缺的是讀取能力而非文件**。
> 不記這一句，它會被誤讀為又一件缺件 ——
> 而缺件是上游之事，讀不到是我方之事。

### 5.2 `15.1` 之 chart 與 profile §5.4

**該項早已在 §5.4**（第五項成員，56 §3 所記），本輪未重複登記，
改為**補上其與 A-CF23 之連結**：

> 其成因歸 A-CF23 —— 該 chart 讀不到**不是缺件而是缺讀取能力**。
> **外部參照盤點之三分類容不下本項** ——
> 盤點以「文件在哪」為軸，而本項之問題是「文件在手上而我方讀不到那一頁」。

---

## 6. Massage Seats 文件 —— **已查而不解**

唯讀查證（`pdftotext`，1,036,491 bytes → 文字 4,513 字元）。

**問**：該文件是否載有**配置 → tab 組**之對照？**答：無。**

其所載與 tab 有關者，皆為**切換時機**而非**配置對照**：

> M1.) When the massage button is turned On with the door control, if the lower
> screen is not in the stowed position, **switch the tab on the lower screen to
> the Massage tab** with the system On.
>
> M3.) …**do not switch the tab** on the lower screen to the Massage tab with
> the system Off…
>
> M5.) **For vehicles equipped with a selectable back/cushion feature** for
> massage seats, the user can deselect the massage for either the back or the
> seat cushion.

`M5` 是本文件唯一之配備條件，其對象為 back/cushion **而非 tab 是否存在**。

**故記為「已查而不解」，入 profile §1.1 之未認可表**；DR #17 之問句不變，
RD-1 第 1 問維持。**未生成任何 TC** —— `2.1` 所擁有者為「Massage tab 是否顯示」，
其行為屬該文件自身之 SWE 需求（R-C33、§8.4.2）。

### 6.1 一項順帶所得（不屬本題）

該文件有一句與 RD-1 第 9 問（設定之保持）同型：

> **M6.) The Massage feature will be Off after an ignition cycle, regardless of
> the previous state.**

**它證明「點火循環後之狀態」是這一族文件會寫的東西** ——
Massage 寫了，Comfort 沒寫。這使第 9 問更站得住：
不是「這種需求沒人寫」，是**這一份沒寫**。

**本層未改 RD-1**；此點供分析層決定是否併入第 9 問之措辭。

---

## 7. 現況與待辦

- lint **54 / 54 PASS，0 finding across 434 TCs**（本輪之改動皆未觸語料）
- 台帳 gate：驗過 68／已知不存在 1／有問題 0；反向驗證 7 支全 PASS
- `BASELINE.sha256`：11 列，**11 OK／0 FAILED**

**待 Pei**：

1. **將 `HMI Settings List R1 SR24 Post 2A (June 15 2023).xlsx` 補入 `inputs/`**
   （判準三；補入後本層更新 BASELINE 與 profile §1.1 之 ⚠）
2. RD-1 之送達（22 問，回覆去向一行待填）—— **其第 7 問待 §0.2 覆核後定稿**

**待分析層**：§0.2 之改寫措辭；§6.1 是否併入第 9 問。

**未做**：未生成 TC、未改 RD-1、未寫回、未動交付夾、未搬任何檔案至 `inputs/`；
git 未執行。
