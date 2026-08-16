# 53 — Comfort HMI / 拆分之界線、22→28 條改判、15.1 之「離開」側

- 產出層：執行層｜2026-08-16｜對象：分析層
- 承接：下放包 75
- lint **54/54 PASS，385 條**（新增 2 列，見 §5）；ENTRY 020 已產出

---

## 0. RD-1 問句 8／9 之全文（75 §7 —— 請覆核後方送 Pei）

### 問句 8

> ## 8. When is AUTO unavailable?
>
> **Units blocked**: 1 — `SWE1-HVAC-047` (section 10.4)
>
> **The sentence**:
>
> > EH4.) When the AUTO function is off **and available**, the user's first
> > press of the AUTO button will activate the AUTO ECO functionality.
>
> **What is missing**: the clause makes the behaviour conditional on AUTO
> being "available", and **no section in the document says when AUTO is
> unavailable**. We can test the available case, which we have; we cannot
> test the other side, and we cannot tell a tester how to put the vehicle in
> it.
>
> **What we have done**: the available case is covered. The unavailable case
> has no test case.
>
> **Once answered**: one test case is written for the unavailable case, with
> the condition stated as a pre-condition.

### 問句 9

> ## 9. Which document defines whether comfort settings survive an ignition cycle?
>
> **Units blocked**: 0 — this question stops nothing; it may add work rather
> than unblock it.
>
> **What is missing**: of the 373 verification units we examined, **at most
> 222 describe a state the user sets** (the count is an upper bound — it was
> taken by a keyword rule that errs towards including) — AUTO on or off, fan
> speed, airflow mode, seat heating level — **and the document never says
> whether any of them is retained after an ignition cycle or a cold boot**.
> Only two sections mention power or key cycles at all (the pop-up
> suppression during ignition cycles, and the latching of the last
> lumbar/bolster selection).
>
> We checked the power-management specifications (CFTS009 Wake-up and
> Power-up, CFTS010 Power Down) before asking. They state that climate
> pop-ups are shown and HVAC controls stay active in certain power states,
> and they require the restoring of *audio and telematics* settings by name —
> **but they say nothing about retaining climate or seat settings**.
>
> **What we have done**: nothing. Writing a test for "the fan speed is still
> 3 after a restart" would be inventing a requirement, so we have not written
> one.
>
> **Once answered**: if the behaviour is owned by another document, we record
> the owner and write nothing. If it belongs to Comfort, this becomes a batch
> of new test cases rather than a correction to existing ones.

**「至多 222」之上限標記依 75 §7 已加**（其判準 `stateful` 偏寬）。
摘要表之總計為 **26**，並註明問句 9 不阻塞任何 leaf。

---

## 1. 七條之複判（75 §1）

判準：**條文列舉了 N 個觸發者 → N 條；泛稱而由我方挑樣 → 一條。**
自查句：**能不能把這 N 個項逐字引出來？**

| leaf | 節 | 條文之列舉句（逐字）| 判定 |
|---|---|---|---|
| `013-03` | 2.9 | `Rear defrost is independent of **any other climate functions**.` | **不拆** —— 泛稱；AUTO 與 FRONT DEF 是**我挑的**（**推翻我上包之「應拆」**）|
| `021-02` | 2.15 | `EXTERIOR REAR-VIEW MIRROR DEFROST is independent of **any other climate functions**.` | **不拆**（同上）|
| `121-02` | 16.15 | 同 `021-02`（ICE14 逐字相同）| **不拆** |
| `009-03` | 2.6.1 | `move 1 increment **up/down** per press` | **拆 2** |
| `023-01` | 3.1 | `there are 3 airflow mode buttons (**Windshield, Face, Feet**) … **Each** Mode button can be pressed to individually toggle ON / OFF` | **拆 3**（**推翻 74 §2.2 之「維持不拆」**）|
| `023-03` | 3.1 | `Toggling **UP (or RIGHT)** moves forward in the order and toggling **DOWN (or LEFT)** moves backwards` | **拆 2**（同上，推翻）|
| `036-01` | 7.8 | `The Rear Airflow Modes has 3 states: **1) Feet, 2) Face + Feet, 3) Face**` | **拆 3**（推翻）|

> **判準一換，方向就換**：我上包判「拆」的三條（獨立性）變成不拆，
> 而 74 §2.2 判「不拆」的三條（列舉集合）變成拆。
> **兩包之個案結論相反，而其原因是同一個 —— 舊判準讀的是觀察量，
> 新判準讀的是條文有沒有把它們列出來。**

---

## 2. 28 條之改判清單（每條引其列舉句）

複核 74 §1.3 之 22 條後：**其中 3 條改為不拆、19 條維持拆**；
加上 §1 之 4 條與 §3 之 4 條，**合計 28 個 leaf 應拆**。

### 2.1 應拆（28 leaf → 74 TC，**淨增 46 列**）

| leaf | 節 | 條文列舉句（`split_reason` 之依據）| N |
|---|---|---|---|
| `003-06` | 2.3 | `Manually selecting A/C, switching to another airflow mode (including front defrost), or changing fan speeds breaks Auto` | 3 |
| `009-03` | 2.6.1 | `move 1 increment up/down per press` | 2 |
| `009-05` | 2.6.1 | `jump to a value as well via touching a spot in a slider bar or voice command` | 2 |
| `009-06` | 2.6.1 | `press slider handle to move …; if user initially presses slider area outside of handle …, ignore the press` | 2 |
| `010-03` | 2.7 | `user can either use Fan up/down (minus/plus) buttons, directly touch a fan segment to jump or slide, or use Hard Control` | 3 |
| `010-04` | 2.7 | `shall not be able to turn the FAN off by using the FAN controls on the screen or the FAN hard control` | 2 |
| `012-05` | 2.8 | `Auto turns Defrost off.` ＋ `Turning Defrost on while in Auto will break Auto` | 2 |
| `023-01` | 3.1 | 見 §1 | 3 |
| `023-03` | 3.1 | 見 §1 | 2 |
| `031-01` | 7.3 | `(While unlocked = Lock Rear text with unlocked Lock icon, While locked = Unlock Rear text with the Lock icon)` | 2 |
| `032-04` | 7.4 | `adjusting driver temperature affects passenger temperatures, adjusting passenger temperatures would break SYNC` | 2 |
| `036-01` | 7.8 | 見 §1 | 3 |
| `036-05` | 7.8 | `If the Rear Mode hard control is pressed … press and hold of the control will only move one mode over` | 2 |
| `103-02` | 14.18 | `Popup will have a 5 sec timeout and restart with additional presses` | 2 |
| `107-06` | 16.3 | `Pressing MAX DEF or Max A/C the system goes to that function` | 2 |
| `107-07` | 16.3 | `Manually changing airflow mode or changing fan speeds breaks Auto` | 2 |
| `111-03` | 16.6.1 | `by using arrows … or slider …` ＋ `jump to a value as well via … or voice command` | 3 |
| `111-05` | 16.6.1 | 同 `009-06` 之 ICS 版 | 2 |
| `112-04` | 16.7 | `use Fan up/down buttons, directly touch a fan segment to jump or slide, or use Hard Control` | 4 |
| `112-05` | 16.7 | 同 `010-04` 之 ICS 版 | 2 |
| `113-09` | 16.8 | `Changing temperature, recirculation, mode distribution or pressing again MAX DEF break MAX DEF` | 4 |
| `115-05` | 16.10 | `Actions on rear defrost, heated/vented seats or heated wheel don t reactivate climate` | 3 |
| `118-07` | 16.12.1 | `(timeout after 3 seconds of inactivity or as soon as another button except Mode HC is pressed)` | 2 |
| `119-08` | 16.13 | 同 `113-09` 之 MAX A/C 版 | 4 |
| **§3 之四條** | | | |
| `008-02` | 2.6 | `when at the Highest possible position display HI when at the lowest display LO` | 2 |
| `032-01` | 7.4 | `display the current degree … when at the Highest possible position display HI when at the lowest display LO` | 3 |
| `033-01` | 7.5 | `Fan ranges: Off, 1-7, 15h (denoting to show AUTO instead)` | 3 |
| `110-01` | 16.6 | `Temperature ranges: LO, 60-84, HI (English), LO, 16-28, HI (Metric)` | 2 |

**28 leaf → 74 TC；現為 28 條，故淨增 46 列**（74 §1.3 之估 +30 已過時）。

### 2.2 引不出列舉句而改為不拆（7 條）

| leaf | 原判定之由 | 現判定 |
|---|---|---|
| `013-03`／`021-02`／`121-02` | 兩個干擾源 | **不拆** —— `any other climate functions` 為泛稱 |
| `048-03`（10.5）| 三個 trigger | **不拆** —— 條文為 `broken by acting on other buttons **e.g.** fan speed, airflow mode **etc**`：`e.g.` ＋ `etc` 即明示其為例示 |
| `084`（14.1.1）／`106-03`（16.2）| 逾時 | **不拆** —— 條文只述一個行為 |
| `061-04`（11.7）| 兩步 | **不拆** —— 第一步為 setup |

> `048-03` 值得單記：**條文自己用了 `e.g.` 和 `etc`，等於明說「這不是完整清單」。**
> 依 §1 之自查句，我引得出那三個詞，但引不出「這就是全部」——
> **能逐字引出項目，不等於條文把它列舉完了。**

---

## 3. `110-01` 同型之掃描（75 §3）

pattern：procedure 含 ≥2 個 `Set`／`Select`／`Change … to` 且其值相異。
**候選 4 條，全數判為應拆**（已併入 §2.1）：

| leaf | 節 | 其兩個以上之設定值 | 判定 |
|---|---|---|---|
| `008-02` | 2.6 | highest／lowest | 拆 2 |
| `032-01` | 7.4 | 範圍內／highest／lowest | 拆 3 |
| `033-01` | 7.5 | 1／7／AUTO | 拆 3 |
| `110-01` | 16.6 | English／Metric | 拆 2（74 §2.2 已裁）|

**「已知漏報 ≥1」之處置到此完成**：該形態之全部 4 條已找出，
且其成因一致 —— **設定步驟之 ER 是狀態確認，故不被 trigger 判準看見**。

---

## 4. 7 節之 §7 反向配對（75 §5）

| 節 | 列舉 | 正向是否齊備 | 反向 | 判定 |
|---|---|---|---|---|
| `2.5.1` | Auto／Manual／Open | ✅ `007-01` 逐一驗 | ❌ | **缺口（來源側）** —— 其反向為「非該配置之車輛」，否定值無條文（同 DR #38 族）|
| `9.2` | level number／AUTO／OFF | ❌ **`040-01` 只驗「顯示前後排狀態」，未逐一驗三值** | ❌ | **缺口** |
| `13.2.1` | 四種調整型態 | ✅ `AC-077` 逐一驗 | 無條文依據 | 正向齊備；反向不可測 |
| `14.3` | Temp／fan／mode popups | ❌ 僅驗 fan | ❌ | **惟其列舉前綴為 `e.g.`** → 依 §1 為例示而非閉集；**列為觀察，不列為缺口** |
| `14.13` | temperature／fan speed／mode popup | ❌ 僅驗 temperature | ❌ | 同上（`e.g.`）|
| `16.4` | 五鍵之 on/off | ✅ `AC-108` 驗五鍵皆 on | ✅ 同條驗五鍵皆 off | **齊備** |
| `17.2` | widget 之六項內容 | ✅ `125-02`～`-08` 逐項驗 | 無條文依據 | 正向齊備 |

**新增缺口 2（`2.5.1`、`9.2`）；`14.3`／`14.13` 因 `e.g.` 降為觀察。**
真缺口累計 **10 ＋ 2 ＝ 12**。

---

## 5. `105-01`／`105-02` 之「離開」側 —— **已生成**（75 §4）

條文逐字列舉二觸發：

> `when a user **enters** (starts a function) **or exits** (breaks a function)
> that function then the HVAC pop ups displayed will follow the chart below`

新增 `NR1L-ComfortHMI-384`／`-385`，溯同一 leaf；四條之 `split_flag` 皆 true，
`split_reason` 引該句並記其獨立失效之形態
（「pop-up 可能於進入時正確而於離開時停留在舊值」）。

**leaf 數不變（Climate Popups 仍 36 leaf），TC 36 → 38；全 corpus 383 → 385。**
ENTRY 020 已寫回（sha `875d5372…`），標「範本容量待擴充」，不送 Excel 確認。

---

## 6. Q2 正規式之修正（75 §6）

| | 前 | 後 |
|---|---|---|
| pattern | `\\d+/\\d+` | `(?<![\\d."'/])\\d+/\\d+(?![\\d./])` |
| `For 8.4/10.1/12 landscaped screens` | ❌ 誤命中 | ✅ 不命中 |
| `fan speed at highest setting (7/7)` | ✅ | ✅ 仍命中 |
| Q2 之「無」 | 7 | **5** |
| Q2 之「不適用」 | 215 | **217** |

**其餘 5 格之 boundary 缺口**（`001-03`／`011` 等）已於 51 §2 逐格判過。

---

## 7. 一處連帶損害（本輪自行發現並修）

新增 `-384`／`-385` 後，`rc42-condition-marker` **立刻對這兩條 FAIL** ——
該 gate 以「tc 編號 ≥ 361 即為 R-C42 解封之 leaf」判斷成員，
而 65 §4 當時稱該界線是「corpus 之事實而非手記清單」。

> **它是事實，直到下一次追加為止。**

已改為**身分判定**：成員 = `gen_batch16.py` 所產之 leaf ∪ `{125-08, 126-02}`，
自生成器讀出。`verify_b_gates.py` 同步改。

**同型三例已記於本 pipeline**：`MOVED_TO_BATCH16` 之計數 vs 身分（65 §4）、
等價對之 `req_id:tc_id`（60 §1.1）、本次之編號界線 ——
**凡以「當下之範圍」代替「成員之身分」者，都會在下一次增長時失效。**

---

## 8. 「本包是否仍有該驗而未驗者」（R-C30）

1. **28 條之拆分本輪未生成**（75 §9.2 明示先出清單）；其 `split_reason`
   之文字已備於 §2.1 之表，生成時逐條引入。
2. **§2.1 之 N 值為條文所列項數，未逐條確認「每一項在該車型上皆可觸發」** ——
   例如 `115-05` 之三者（rear defrost／heated seats／heated wheel）
   於未配備該功能之車輛上不可觸發，屆時需配置式 PC。
3. **§4 之 `14.3`／`14.13` 以 `e.g.` 降為觀察** —— 若分析層認為
   `e.g.` 之列舉仍須逐項驗，則此二節各需 +2 條。
4. **§1 之三條推翻與 74 §2.2 之三條推翻方向相反**，兩者皆依 75 §1 之判準；
   **若該判準本身再被修訂，這六條會再翻一次**。
5. **`033-01` 之三值（Off／1-7／15h）中 `Off` 未被現行 TC 觸及** ——
   其拆分後之第三條應驗 `Off`，惟 `2.7`／`7.5` 另有「不可自畫面關閉風扇」之條文，
   **兩者之關係須於生成時處理**（拆分不是單純複製）。

---

## 9. 待分析層

1. **§2.1 之 28 條是否核准生成**（淨增 46 列，385 → 431）。
2. **§4 之 `14.3`／`14.13`**（`e.g.` 列舉）是否須逐項驗。
3. **§4 之二新缺口**（`2.5.1` 之反向、`9.2` 之三值）之處置。
4. **§8.5 之 `033-01` 第三條與「不可關閉風扇」條文之關係**，生成前請裁。
5. RD-1 問句 8／9 之措辭（§0）覆核後，其送達仍待 Pei。
