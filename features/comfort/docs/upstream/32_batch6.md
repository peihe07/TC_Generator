# 32 — Comfort HMI / 觸發改邊、階層表、換軸、axis-values 推廣、批次 6

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 43
- 結果：七項全數落實。觸發改邊後 **632 → 0**，反向驗證 **6/6**。
  階層表增 **77 對**。換軸**三項齊備，已換**，影響評估同輪完成。
  `axis-values` 由 1 個軸推廣至 **5 個軸**（另加未受保護之否定式必 FAIL 之覆蓋檢查），
  反向驗證全過。`-019` 已補限定式 PC。批次 6 產 **16 條**（`-082`…`-097`），
  **1 leaf 停下**。lint **42/42 PASS，97 條**。**未寫回。**

---

## 0. 下放包九項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | 改觸發條件，重跑五案，回報 FAIL 數（預期 0）| ✅ §1 —— **0**，反向驗證擴為 6 案全過 |
| 2 | 加階層表與 `via-hierarchy` 標記，回報新增對數 | ✅ §2 —— **77 對** |
| 3 | 查換軸三條件；齊備則換並同輪回報影響評估 | ✅ §3 —— **齊備，已換**；影響三項見 §3.3，另開 DR #31 |
| 4 | `axis-values` 推廣至全部有否定式 PC 之軸，反向驗證 | ✅ §4 —— 1 → **5** 軸，另加覆蓋檢查 |
| 5 | `-019` 補排除式 PC，更新 `spec_ref`／`reasoning` | ✅ §5 |
| 6 | `RUNBOOK` 記「橡皮圖章」與「未見紅燈之 gate」| ✅ §6 |
| 7 | 執行批次 6 | ✅ §7 —— **但 Layer 3 為三節而非兩節**，見 §7.1 |
| 8 | 全批重跑 lint 與 §9 自評；不寫回 | ✅ §8／§9 |
| 9 | 上繳 32 | 本件 |

---

## 1. 觸發改邊 —— 632 → 0，且改邊本身被驗證了

### 1.1 改法

`provisional-sibling` 之條件改為 43 §1 明示之判定依據：

```
provisional == "true"  且  兩側皆已生成
```

即「原本缺的那一側已補上」。**改後本輪 FAIL 列數為 0。**

### 1.2 一處與 43 §1 措辭之差異，已擇其一並回報

43 §1 之程式碼區塊寫「該列中原本未生成之那一側，其所屬 **Test Set 全數生成**
之日」，而其下之判定依據寫「`provisional == true` 且**兩側皆已生成**」。
**兩者粒度不同**：節生成早於其所屬組全數生成。

採**後者（節粒度）**，理由：它是條文自己給出的 ⇔，且它在**證據出現的那一刻**
觸發，而非在其後的組邊界。**早一點，永不晚一點。**
若分析層意在組粒度，改回只是把條件多加一個 `Test Set 完成` 合取項。

### 1.3 反向驗證擴為六案，並補上「舊版會答錯的那一個」

**舊觸發條件通過了它自己全部五個案例，而它是錯的。** 成因值得記：
那五案全部在斷言 predicate 做了什麼，**沒有一案在斷言那面旗子是什麼意思**。

新增第五案即舊版會答錯者：

```
PASS — both sides generated, flag still true -> due
PASS — same row, flag cleared by re-confirmation -> silent
PASS — neither side generated -> silent (nothing landed yet)
PASS — verdict is irrelevant — the FLAG decides, sibling included
PASS — generated side's set is COMPLETE but counterpart still missing
       -> silent (the old trigger fired here, on unchanged evidence)
PASS — order does not matter — missing side may be on either side

6 / 6 directional cases PASS
```

### 1.4 改邊後 gate 立刻抓到東西 —— 批次 6 觸發 26 列

批次 6 使 `16.2`／`16.14`／`16.16` 首次生成，於是 26 列「對造終於補上」之
provisional 列到期。**這是新觸發第一次在真實情境下動作，且它動對了時點** ——
26 列全部兩側皆有 TC，可用之證據與當初判定時**不同**。

26 列全部重新確認完畢，**verdict 全數維持**（見 §7.4：重新確認查出兩項實質
發現）。

### 1.5 **重建曾自行清旗，已修正** —— 本輪最接近出事的一處

首次跑批次 6 之後的重建，`provisional_of()` 把 **16 列由 `true` 自動改為
`false`** —— 因為兩側都生成了。

> **那正是 gate 要問問題的那一刻，而重建搶在人之前把旗子拔掉了。**
> 機器自己蓋了那個橡皮圖章，重新確認**永遠不會發生**，
> 而 lint 會是綠的。

42 §1 只寫了「`false` 不可被改回 `true`」（避免人工複核被抹除），
我當時據此寫成單向。**單向不夠 —— 它得是「已記錄之值一律不重算」**：

| 方向 | 若允許重算會怎樣 |
|---|---|
| `true → false` | 缺的那側一落地，旗子自己消失；gate 永遠不會問 |
| `false → true` | 人工複核被下一次重建抹除；gate 永遠無法被滿足 |

已改為：`verdict ∈ {deferred, 類級}` 恆 `true`；其餘**只在該列首次寫入時
計算一次**，其後僅由人手變更。那 16 列已還原為 `true` 並實際重新確認。

**發現途徑**：改完之後 FAIL 數由 26 掉到 10，而我預期的是 26。
**數字對不上是唯一的線索** —— 若當初沒有先量 26，這 16 列會靜靜地消失。

---

## 2. 階層表 —— 77 對新增，且與等價組分離

### 2.1 實測所得之階層邊

規則（43 §2）：掃全 129 節，取「`X Y` 形態且該詞之某個**實見**表面形式中有
一個字恰為另一個**單獨出現**之控制名者」。實測頻次：

| 特化詞 | 實見次數 | → 泛化詞 | 單獨出現次數 |
|---|---|---|---|
| `AUTO ECO` | 9 | `AUTO` | 82 |
| `ECO HVAC` | 2 | `HVAC` | 34 |
| `MAX A/C` | 26 | `A/C` | 18（另 `AC` 11）|
| `MAX DEF`（實見 `MAX DEFROST` 2／`FRONT/MAX DEFROST` 4）| 32 | `DEFROST` | 17 |
| `REAR DEF`（實見 `REAR DEFROST` 19）| 20 | `DEFROST` | 17 |

**缺口具名，未以推論補齊（R-C37）**：`FRONT DEF`（1 次，於 `3.2`）
**語意上是 defrost，但它的任何實見表面形式都不曾拼出 `DEFROST`**，
故量測規則構不到它。加進去就是推論，而 43 §2 要求本表為實測。
已寫入 `HIERARCHY_GAPS` 並隨每次執行印出。

### 2.2 階層不是等價，且程式上也不混用

`HIERARCHY` 與 `SYNONYMS` 是兩個表，一個單向、一個雙向：

> 每個 `AUTO ECO` 都是 `AUTO`，但 `AUTO` 不必然是 `AUTO ECO`。
> 併成等價組會使 `10.3`（「Button label will read AUTO ECO」）**當作它寫了
> `AUTO`** 去配對，且會讓 `AUTO ECO` 在它才是精確用語的地方消失。

故階層只**增加**候選對，且其輸出**另標來源**：`pending_sibling.tsv` 增
`source` 欄（`vocab`／`via-hierarchy`）。

### 2.3 新增 77 對，並解掉上繳 31 §2.2 之懸案

| 共有語彙 | 新增對數 |
|---|---|
| `DEFROST` | 39 |
| `AUTO` | 22 |
| `HVAC` | 12 |
| `A/C` | 4 |
| **合計** | **77** |

`vocab` 1591 ＋ `via-hierarchy` 77 = **1668 列**。

**`3.2 ↔ 10.3` 回到候選集**：上繳 31 §2.2 記它於 42 §2 之重建退為
「不再是候選」，成因正是 `AUTO ECO` 不吐 `AUTO`。43 §2 之階層表使其回歸，
`source = via-hierarchy`，**原判定不變**，並於 `reason` 記其來回。
「carried over (no longer a candidate)」現為 **0 列**。

### 2.4 判定處置，及一處我未照字面辦的地方

43 §2 曰「其判定沿用高頻詞之類級處置（`AUTO` 已為類），**不逐對**」。
實作分兩支：

| 共有語彙 | 對數 | 處置 |
|---|---|---|
| ∈ 高頻詞（`AUTO` 22／`HVAC` 12）| **34** | `not-broken-by-3-samples (class)`，沿用類級 |
| ∉ 高頻詞（`DEFROST` 39／`A/C` 4）| **43** | **`deferred`** |

**低頻側不給類級 verdict 的理由**：`DEFROST` 與 `A/C` 沒有既有的類級判定
可以沿用。**對一個沒有類的詞給類級 verdict，等於宣稱一個沒有人做過的判定**
—— 而 `deferred`（尚未問）是真的。兩者都滿足「不逐對」。

其中 4 對兩側皆已生成，依 41 §4 已逐對判完（`2.14 ↔ 10.3`、`2.7 ↔ 10.3`、
`2.7.1 ↔ 10.9.1`，及 §7.4 之 `10.3 ↔ 16.14`），全數 `not-sibling`。

---

## 3. 換軸 —— 三項齊備，已換

### 3.1 三項條件逐項核對

| 條件 | 結果 | 依據 |
|---|---|---|
| 一、三值皆逐字出現，具名節次與句 | ✅ | `2.12` C13.「There are **4 Airflow Mode** displayed in this order (1) Face, (2) Face plus Feet, (3) Feet, (4) Feet plus Windshield」／`2.12.1` C13.0「In some non-tri mode equipment types, airflow modes has **5 states**（1.Face…5. Windshield）」／`3.1` C19「there are **3 airflow mode buttons** (Windshield, Face, Feet) … which provides **7 possible distribution modes**」 |
| 二、互斥且窮盡，或條文明示三種並列 | ✅ | **互斥**：一台車之前排氣流模式集合只能是其一；C13.0 以 `non-tri mode` 明文排除 tri-mode，其 5 與 C13 之 4 為同一物之不同計數。**窮盡（實測）**：全 129 節掃 `airflow mode\|Airflow Mode\|distribution mode\|mode buttons\|states`，**逐一判讀 26 個命中節**，前排側無第四值 |
| 三、無任何值由推論補齊 | ✅ | 三句皆條文原文 |

**兩個看似第四值者，逐一排除**：

- `16.12`（ICE11）`Airflow Modes has 5 states` —— 同一個值在**另一套介面**上，
  `ch16_mirror_map.tsv` 記 `16.12 ↔ 2.12.1 mirrored`，非第四值
- `7.8`（CR8）`The Rear Airflow Modes has 3 states` —— **後排**，屬前後排軸，
  非前排值。（本軸因此明確限定為**前排**；不限定的話 CR8 就會是第四值。）

### 3.2 換軸內容

profile §3.2 第三軸：

| | 舊 | 新 |
|---|---|---|
| 名稱 | tri-mode 有無 | **前排氣流模式集合** |
| 值 | 有／無（2） | **4 模式（2.12）／5 狀態（2.12.1）／tri-mode 7 組合（3.1）（3）** |
| 某值之後果 | 無 tri-mode 功能 | 移除的不是「tri-mode 功能」，而是**另外兩組模式集合** |

**換軸而非增值之理由（上繳 31 §3.2 已證）**：`C13.0` 之 5 狀態是
「非 tri-mode」之**細分**，不是 `有`／`無` 之並列項；二值布林**沒有位置**
可以放它。

### 3.3 影響評估（同輪完成，未先改後評）

**(a) `-015`／`-016`／`-017` 之肯定式 PC —— 不需改寫。**
現為「[spec-verbatim] The vehicle is equipped with Tri-Mode climate (3.1)」，
**它本來就是在指名一個值**，換軸後仍逐字對應 C19。二值軸時它碰巧成立，
三值軸時它依然成立 —— 因為它從一開始就沒有用「非某某」的形式寫。

**(b) `2.12`／`2.12.1`／`2.12.2` 生成時之 PC 形態 —— 一半有解，一半沒有。**

| 節 | 值 | 能否寫出有出處之肯定式 PC |
|---|---|---|
| `2.12.1` | 5 狀態 | ✅ C13.0 自帶正面限定語 `In some non-tri mode equipment types` |
| `3.1` | tri-mode | ✅ C19 自帶 `On vehicles with Tri-Mode climate` |
| `2.12`／`2.12.2` | 4 模式 | ❌ **C13 是無限定之一般句** |

`C13`「There are 4 Airflow Mode…」**未附任何配置條件**；4 模式這個值之適用
條件只能由**排除**得出（非 tri-mode、且非 5 狀態那類），而條文從未正面陳述。
形態與 #17（`2.1` 之 tab 集合：「depending on vehicle configuration」而不說
哪種配置產生哪一組）**同型**。

已開 **DR #31（High）**，並寫入 profile §3.2 之換軸附註。
**`Airflow and Defrost` 生成時該 2 leaf 之 PC 形態即被此阻塞**，屆時不會措手不及。

**(c) 對 `axis-values` 機制之影響 —— 無。**
第三軸**沒有否定式 PC**（其三個使用者 `-015`／`-016`／`-017` 全為肯定式），
故本軸不需要 `axis-values` 區塊，換軸也不觸發任何 gate 動作。
這與上繳 31 §3.3 所測一致。

---

## 4. `axis-values` 之推廣 —— 1 軸 → 5 軸，另加覆蓋檢查

### 4.1 五個區塊

每塊自帶 `negation:` 欄，gate 不再硬寫單一字串：

| axis | 名稱 | 值數 | 否定式 | 使用者 |
|---|---|---|---|---|
| 13 | HVAC 實體控制型式 | 3 | `does not have 3 knob HVAC controls with ICS` | **77** |
| EMEA | 市場／變體軸 EMEA ICS | 2 | `is not an EMEA ICS vehicle` | **40** |
| 9 | secondary lower screen 之有無 | 3 | `is not configured with a non-foldable secondary lower screen` | **19** |
| 2 | 單區／雙區／四區 | 3 | `is not a single zone climate configuration` | **3** |
| 10 | REAR DEFROST 之有無 | 2 | `Rear defrost is not present in the vehicle` | **1** |

**值一律具名出處**（6.3 CM1.／13.2 LS1.／2.11 C12.／2.6 C5.／7.10 CR10.／
3.4 C22.），不自造。軸 13 與軸 9 沿用既有之 `other` 作 catch-all，
與該區塊原本的寫法一致。

**軸 10 只有 1 個使用者**，仍立區塊 —— 一個使用者的軸和七十七個使用者的軸，
在「軸增值時該否定式的涵蓋悄悄改變」這件事上沒有差別。

### 4.2 真正的推廣是**覆蓋檢查**，不是多開四個區塊

多開四塊只保護「已經想到的四個」。新增之檢查是：

> 掃全部 TC 之 pre_conditions，凡形態為否定式（`does not`／`is not`／
> `not configured`／`not present`／`not currently`）者，
> **若既不匹配任何區塊之 `negation`，也不在 `NON_AXIS_NEGATIONS` 具名清單內
> —— FAIL。**

沒有這一條，**日後為一個沒有區塊的軸加一句否定式 PC，其靜默程度與軸 13 在
34 §4 之前完全相同**。有了它，那件事會出聲。

`NON_AXIS_NEGATIONS` 具名三項（皆非配置軸）：

| 句 | 為何不是軸 |
|---|---|
| `The lower screen is not in the stowed position`（13.2）| 執行期狀態，同一台車兩種狀態 |
| `The user is not in the climate section on the main head unit`（13.2）| 執行期畫面位置 |
| `The Seats tab is not currently shown`（test-setup）| 測試起始狀態 |

### 4.3 反向驗證 —— `verify_axis_gate.py`（新增）

同樣 import `lint_tcs` 本身。四個方向：

```
axis 13 / EMEA / 9 / 2 / 10：值數相符、reviewed-at 相符、
                             negation-users 與語料相符、否定式確實存在
PASS — adding a value without bumping reviewed-at FAILs: count 4 vs reviewed 3
PASS — no negated PC is left unprotected: 0 uncovered
PASS — an invented negation for an axis with no block DOES fire
PASS — 三個 NON_AXIS_NEGATIONS 條目皆仍有使用者（清單不得養殭屍）
```

最後一項是刻意加的：**一個沒有使用者的豁免條目，和一個沒有人維護的清單，
是同一件事。**

### 4.4 推廣當場就抓到東西

批次 6 一產出，`axis-value-count` 立刻對 **三個軸**報 stale：
軸 13（+12）、軸 9（+10）、軸 2（+1）。
**若只有軸 13 有區塊，軸 9 與軸 2 那 11 條會靜靜地漏掉。**
已全部更新。

---

## 5. DR #29 —— `-019` 已補限定式 PC

依 43 §5 之第三條路：

```
pre_conditions（新增第 2 行）
  2. [spec-verbatim] The front HVAC fan range of the vehicle is Off, 1-7 (2.7)
specification_reference
  …_3.2; **…_2.7**; …_2.14; …_16.2
expected_result
  5. The fan speed is at the highest setting (7/7)      ← 一字未動
```

**限定式 PC 不是排除式**，程式上也分開：`confine` 欄與 `EX_*` 兩碼事，
且排在排除式之前 —— 它屬於需求本身，不屬於介面記帳。

`reasoning` 已具名：ER 不改（寫 8/8 為造值、寫「最高設定」弱於條文，
皆違 §8.4.1），改以第十四軸之值限定適用車輛，使既有 ER **在其可陳述之範圍內
為真**；`Off, 1-8` 側之涵蓋缺口由 DR #29 追，不吸收（§8.4.2）。

---

## 6. `RUNBOOK.md` 兩節已記

- **「橡皮圖章 —— 清旗之前先問『有沒有新東西可看』」**：含 632/0 之實測、
  觸發錯邊之機制描述，以及自查句「清掉這個旗標之前，我看得到什麼是當初看不到的？
  答不出來就不要清，回報」。
- **「未見過紅燈的 gate，等於沒被驗過」**：雙向斷言之要求、
  「import 出貨的判準而非重寫一份」、以及**案例須包含舊版會答錯的那一個**
  （§1.3 之實例）。末句記其與 R-C37 同源：
  **只驗陽性側的 gate 驗證，與只取陽性樣本的歸納，是同一個錯誤換了層。**

---

## 7. 批次 6 —— `ICS Anatomy`

### 7.1 Layer 3 為**三節**，不是兩節

43 §7 之表列「Layer 3：16.2、16.16」而 leaf 數列 **17**。**兩者不相容** ——
`16.2`（9）＋`16.16`（5）＝14。

`framework.md` 第 49 行（43 §7 自己指定的權威：「Layer 3 與 leaf 數**自
`framework.md` 導出**」）列 **`16.2, 16.14, 16.16`，17 leaves**，
其第 468 行另記「3 sections / 17 leaves」；`16.14` 進入本組是 14 §1 之修正案
（`2.14`／`16.14` 成 Anatomy 對）。037 實測：106(9) + 120(3) + 122(5) = **17**。

**依 framework.md 生成三節**，以 43 §7 自身之導出規則為準。

### 7.2 產出

| leaf | 節 | TC | tc_id |
|---|---|---|---|
| `SWE1-HVAC-106` | 16.2 | 9 | `-082`…`-090` |
| `SWE1-HVAC-120` | 16.14 | 3 | `-091`…`-093` |
| `SWE1-HVAC-122` | 16.16 | 4 | `-094`…`-097` |
| **合計** | | **16** | 16 emitted ＋ 1 withheld ＝ **17 leaves** |

### 7.3 ch16 側之三處反向，逐一處置

**(a) EMEA 軸取正向值，不取排除式。** ch16 之 TC 本就跑在 EMEA ICS 車上：

```
[spec-derived] The vehicle is an EMEA ICS vehicle, whose climate interface
is specified in chapter 16 (16.2)
```

與 ch2 之「不是 EMEA ICS 車（16.2）」是**同一事實之兩面**，出處同一節。
`emea_ics_review` 於本批不適用（其 gate 以排除式為鍵），
`interface_axis_review.emea_ics` 欄改記此反向判定與其理由。

**(b) 鏡射表反向使用 —— 查 ch2 側有而 ch16 側無者，避免移植（§8.2.1）。**

| 對 | 反向所見 | 處置 |
|---|---|---|
| `16.2 ↔ 2.2` | C1 有「for MTC (**if the MTC has a Climate screen**)」括號限定，ICE1 無 | **不移植**，`-088` 之 PC 不寫該限定 |
| `16.2 ↔ 2.2` | ICE1 有「with the exception of the recirculation led in climate off」，C1 無 | ch16 獨有，即 `-02` leaf（`-083`）|
| `16.14 ↔ 2.14` | **ICE13 僅 C15 之首二句，3 旋鈕 ICS 整段於 ch16 不存在** | **不驗**該行為；僅以 2.14 為軸 13 之出處而引之（R-C29）|
| `16.16` | `no-counterpart` | 無可移植者 |

第三列即 `RUNBOOK.md`「節級看開頭，TC 級看那一句」之**反向應用**。

**(c) 軸 13 之出處在 ch2，而所治者正是 ICS 車。**
C15「For MTC **with ICS** … 3 knob HVAC controls … no HVAC menu bar icons,
no HVAC screens and no HVAC pop ups」—— 該句寫在 ch2，但 `with ICS` 使它
**綁 ch16 的 TC 綁得更緊**。故 16.2 與 16.14 全數補之（跨節取據，2.14 入
`spec_ref`）；**16.16 不補** —— 其可觀察量為座椅之 controls screen，
不屬 C15 所列之三者，補之即為過嚴之排除（35 §1 形態）。

**軸 9**：可觀察量在 head unit 之 comfort section 者補（10 條），
可觀察量為 comfort popup 者不補（**6.3 自己的例外**），硬鍵 LED 者不補。
**軸 12**：全數不補 —— ch16 十八節無任何 tab 條文，`2.1` 屬另一套介面，
援引即為跨介面移植。

### 7.4 26 列 provisional 重新確認 —— 查出兩項實質發現

批次 6 使 `16.2`／`16.14`／`16.16` 首次生成，26 列到期（§1.4）。
**verdict 全數維持 `not-sibling`（鏡射非 §4.6 sibling：兩套介面不共存於同一
車輛）**，但重新確認本身查出兩件事：

**(一) R-C36-1 之逐條判定，本輪首次以 TC 對 TC 驗證，全部成立。**
`emea_ics_per_tc.tsv` 中指向 `16.2`／`16.14` 之 14 筆逐一比對：

| ch2 TC | verdict | ch16 對應 TC | 結果 |
|---|---|---|---|
| `-032`／`-033`／`-035`／`-036`／`-038`／`-039`／`-040` | yes | `-082`／`-084`／`-085`／`-087`／`-088`／`-089`／`-090` | **七筆皆有對應** |
| `-037`（華氏不顯示半度）| no | —— | **成立** ——批次 6 確實未產任何華氏 TC，因 ICE1 無該句 |
| `-043`／`-044` | yes | `-092`／`-093` | 有對應 |
| `-045`／`-046`／`-047`（3 旋鈕）| no | —— | **成立** —— 16.14 只產三條，無 3 旋鈕 TC |

**兩年來以節級 `mirrored` 為預設、逐條回答的那 45 條排除式 PC，
其中 14 條今天有了實物對照，14/14 相符。**

**(二) 037 在兩側之分解不一致 —— 新開 DR #33。**
ICE1 第二句「…according pop-ups are shown if NOT on climate screen (timeout
after 3 sec), **and changes are reflected in status bar/ status indicator on
category button**」：
ch2 側（C1）037 為後半產出了 leaf（`-034` 所驗者），
**ch16 側之九個 leaf 無一對應之** —— `-03` 只取前半。
同一句話，兩側分解不同。依 R-C33 單位歸 037、依 R-C16 為覆蓋缺口，
不自行增列 leaf（§8.2）。

### 7.5 停下一項 —— `SWE1-HVAC-122-02`，DR #32

`16.16`（ICE15）「Off icon of seats will depend on system configuration
(**see Climate section**)」。**三類 marker 皆不合**：

| marker | 為何不合 |
|---|---|
| `[BLOCKED-SPEC]` | 其判準為「內容由**另一份 spec** 擁有」；此處委派對象是**本 spec 之另一節** |
| `[BLOCKED-NON-HMI]` | 其判準為「內容不是介面行為」；此處確是一個圖示，是介面可觀察的 |
| R-C16 覆蓋缺口（不產列）| 其判準為「037 未產出該 leaf」；037 產出了 |

缺者為「configuration → icon」之對照表，形態與 #17 同型。
**新 marker 不得於生成當下自創（R-C26／profile §5.4 末）**，故停下回報，
登 **DR #32（High）**。**待裁**：另立第四類 marker（「委派對象在本 spec 內，
而該節未定義」），抑或依 §8.4.2 逕列 coverage gap。

`044-02` 之前例在此重演了一次形狀：**判別次序（profile §5.3）能告訴我
「不是前兩類」，但它的終點是「正常生成」，而這一個生成不了。**
次序缺一條出口。

### 7.6 A-CF25 —— ICE1 之交叉引用指錯節

ICE1 之例外子句附 `(see ICE11.)`，實測：

| 條款 | 節 | 含 recirculation LED 規則？ |
|---|---|---|
| ICE11 | `16.12`（Airflow Modes has 5 states）| **否**，全句無 `recirc` |
| ICE9 | `16.10` | **是** |

應為 `see ICE9.`。與 A-CF13 同類而形態相反（A-CF13 是同一標籤跨多節，
本項是引用指向錯標籤），同一結論再次成立：**條款標籤不是唯一鍵**。
`-083` 只驗 ICE1 自身所述之例外，不依該誤引取用 16.10 之內容，
`16.10` 亦未列入其 `spec_ref`。**不列 RD-1**。

---

## 8. lint

```
42 / 42 gates PASS; 0 finding(s) across 97 TCs
```

TC 81 → **97**；leaf 76 → **92**；已生成節 30 → **33**。
`pending_sibling.tsv` 1592 → **1668** 列（`vocab` 1591／`via-hierarchy` 77），
重建**冪等**（連跑兩次 md5 相同 `922e6bc0…`）。

| verdict | 列數 |
|---|---|
| `deferred` | 946 |
| `not-sibling` | 467 |
| `not-broken-by-3-samples (class)` | 244 |
| `sibling` | 11 |

`provisional`：`true` 1584／`false` 84。

---

## 9. §9 自評

本輪新增 16 條 TC（批次 6）＋ 修改 1 條（`-019` 之 PC 與 spec_ref）。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 1 | Test Set（§4.1／§4.2）| 變 | `ICS Anatomy`，取自 framework.md Part N 第 11 組，無 Test Group 前綴 |
| 2 | tc_title（§4.3）| 變 | 16 條皆 2–14 字、無 modal；`-092`／`-093` 以 `no discrete temperature settings`／`no AUTO control` 區辨同節之兩個否定 |
| 3 | Pre-Condition（§4.4／§8.5）| 變 | EMEA **正向**軸值（16.2）＋ 軸 13（2.14，10 條）＋ 軸 9（6.3，10 條）＋ ATC／MTC 值（16.2）＋ CCM relays MTC（16.14）＋ 單區排除（16.11）；`-019` 另補第十四軸之值（2.7）|
| 4 | Input Test Data（§4.5）| 變 | 全數 `NA`；無資料須置於此 |
| 5／6／7／8 | 步驟（§5.x）| 變 | 每條 2–3 步，末步持驗證；無禁用動詞；無 CLI |
| 9 | Baseline（§5.6）| 變 | `-082`／`-090`／`-097` 需前後對照，首步建立基線 |
| 10 | Procedure ↔ ER 1:1（§6）| 變 | 16 條全數 1:1，ER 無 modal |
| 11 | FP／FF（§7）| 變 | `-083`／`-089` 為否定式驗證（畫面**不**反映／status bar **不**顯示），各自配有正向步驟 |
| 12 | 溯源（§8.1／§8.2.1／§8.4）| 變 | 16 leaf 各溯其 037 req_id；**§8.2.1 之三處反向判斷見 §7.3(b)**；`-122-02` 依 §8.4.2 停下不吸收 |
| 13 | Design Method（§12）| 變 | 15 條功能測試、`-097` 狀態轉換（進入畫面前後之狀態保持）|
| 14／15 | §11 格式 | 變 | 無行尾句點；UI 標籤用 `"…"` |
| 16 | `specification_reference`（§10.7）| 變 | 各條含自身節次 ＋ 2.14（軸 13）＋ 6.3（軸 9，10 條）＋ 16.11（`-085`）|
| 17 | §8.6／§8.7 | 變 | 條文權威為 `section_fulltext.tsv`；`(7/7)`／`3 sec`／`Off, 1-7` 皆條文明值，未自造 |

**未寫回**（43 §8）。`write_back.py` 未執行，工作簿未動。

---

## 10. 「本包是否仍有該驗而未驗者」（R-C30）

1. **重建自行清旗之事（§1.5）已修，但它提示一件更一般的事**：
   凡「由狀態推導、且會被機器每輪重算」的旗標，都有同一個風險。
   本表現在只有 `provisional` 一個，**未系統性檢查其他欄位**。
2. **946 列 `deferred` 全未判定。** 本輪只多了 43 列（階層低頻側），沒有變少。
3. **`FRONT DEF → DEFROST` 未入階層表**（§2.1），故涉 `3.2` 之 `FRONT DEF`
   與 defrost 系節次之對仍配不成。已具名，未補。
4. **換軸之影響僅評估了 PC 形態**（§3.3），**未評估**：
   換軸是否使既有 `2.12`／`2.12.1`／`2.12.2 ↔ 3.1` 三對 sibling 之
   `distinguishing_axis` 措辭需改（現寫「第三軸 tri-mode 有無」）。
5. **`axis-values` 五軸之值皆取自條文，但「窮盡」只對第三軸做了全語料掃描。**
   其餘四軸之值數（3／2／3／3／2）未經同等強度之窮盡實測，
   其 `value-count` 目前是「已知之值數」而非「證明過的窮盡」。
6. **批次 6 之 16 條未經 §7 之 FP／FF 人工複核**，只經 lint。
   `-094`～`-097` 之 `controls screen` 究竟是哪一個畫面，ICE15 未定義入口，
   我以「controls screen」照錄條文用語而未追問 —— **這是一個未問的問題**。
7. **DR #32 之待裁未決前，`ICS Anatomy` 之 coverage 為 16/17。**

---

## 11. 建議 commit message（git 未執行）

```
feat(comfort): batch 6 ICS Anatomy; trigger fix, hierarchy, axis swap

- provisional-sibling fires on the side that was MISSING, not on either
  side. 632 -> 0. The reverse-validation gains the case the old trigger got
  wrong: five green cases had all asserted what the predicate did, none
  what the flag meant
- and the rebuild was clearing flags itself the moment the missing side
  landed — the exact instant the gate exists to ask about. A recorded flag
  is now never recomputed in either direction; 16 rows restored
- one-way HIERARCHY table (AUTO ECO -> AUTO, ...), measured, kept separate
  from the synonym groups and marked `via-hierarchy`: +77 pairs, and
  3.2<->10.3 returns to the candidate set
- swap axis 3 to the three-valued front airflow mode set. All three values
  are verbatim; 26 hits scanned to show there is no fourth. C13 states its
  value with no configuration qualifier, so value one can only be reached
  by elimination — DR #31, and it will block 2.12/2.12.2's PCs
- generalise axis-values from 1 axis to 5, plus the check that actually
  generalises it: a negated PC matching no block and not named in
  NON_AXIS_NEGATIONS now FAILs. It caught 11 stale entries on axes 9 and 2
  the moment batch 6 landed
- -019 gains a confining PC (front fan range Off,1-7) so its (7/7) ER is
  true where stated; the Off,1-8 side stays with DR #29
- batch 6: ICS Anatomy, 16 TCs, -082..-097. framework.md gives THREE
  sections (16.2/16.14/16.16 = 17 leaves); the handoff listed two
- ch16 inverts three habits: positive EMEA axis value, mirror map read in
  reverse, and axis 13 cited from ch2 because "MTC with ICS" binds ICS
- re-confirming the 26 due rows checked R-C36-1 TC-against-TC for the
  first time: 14/14 pointers hold. It also found DR #33 — 037 decomposes
  the same ICE1 sentence differently on the two sides
- withhold SWE1-HVAC-122-02: delegated to a section of THIS spec, so none
  of the three markers fit (DR #32). A-CF25: ICE1 cites ICE11 for a rule
  that lives in ICE9
- lint 42/42 PASS across 97 TCs; no write-back
```

---

## 12. 待分析層

1. **§7.5 / DR #32** —— 第四類 marker，抑或逕列 coverage gap。
   profile §5.3 之判別次序目前缺一條出口。
2. **§1.2** —— 觸發粒度取節而非組，是否照準。
3. **§2.1** —— `FRONT DEF → DEFROST` 是否以裁定補入（實測構不到）。
4. **§10 第 4 點** —— 三對 sibling 之 `distinguishing_axis` 措辭是否隨換軸更新。
5. **§10 第 5 點** —— 其餘四軸之值是否須做同等強度之窮盡實測。
6. **§10 第 6 點** —— `16.16` 之 `controls screen` 入口未定義，是否開 DR。
7. **批次 7 之授權。**
