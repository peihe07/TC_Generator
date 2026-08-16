# 54 — Comfort HMI / R-C43 之盤點、30 條生成（28 拆分 ＋ 2 缺口）、寫回 ENTRY 021

- 產出層：執行層｜2026-08-16｜對象：分析層
- 覆核對象：`docs/handoff/76_rc43_split_approved.md`
- 狀態：**lint 54/54 PASS，0 finding across 429 TCs**；寫回 ENTRY 021 完成，**不可交付**（DR #35）

---

## 0. 一句話

385 → **429 列**（+44：拆分 +41、缺口 +3），而 **leaf 數不變**——
本輪增加的不是覆蓋面，是**同一個 leaf 內被分開驗的觸發**。

---

## 1. R-C43 —— 已貼入，並全面盤點

R-C43 原文已貼入 `RULINGS.md`（含「它是事實，直到下一次追加為止」之出處說明）。

### 1.1 盤點之涵蓋範圍（R-C30）

- **範圍**：`features/comfort/scripts/` 全部 `.py`（`lint_tcs.py`、`write_back.py`、
  `coverage_audit.py`、`survey_verbatim.py`、6 支 `verify_*.py`、16 支 `gen_*.py`、
  `splits.py`）
- **判準**：檢索 `== <常數>`、`>= <常數>`、`<= <常數>`、`_N = `、`range(`、
  `len(...) == <常數>`，逐一閱讀其**該常數是否在界定「誰是成員」**
- **已知漏報**：以字面常數為條件者可被檢索到；**以變數間接表達之邊界**
  （例如 `if tc_id > LAST_OF_BATCH`）不被此檢索命中。現行碼中未見此形態，
  但這是**未被證明不存在**，不是被證明不存在（R-C13）。

### 1.2 判定表

| 位置 | 原界定 | 判定 | 處置 |
|---|---|---|---|
| `lint_tcs.py` `RC42_FIRST_N = 361` | 區間（`tc ≥ 361`）| **範圍** | 已於 76 §1 前改為 `RC42_LEAVES`，自 `gen_batch16.py` 讀出身分 |
| `verify_no_tcid_gate.py` `len(LEAF_UNIVERSE) == 403` | 計數 | **範圍** | **已改**：改與 `recon.json` 之 leaf 集合**逐一比對身分**。原式只保證「有 403 個」，037 若換掉 3 個 leaf 而總數不變，原式靜靜通過 |
| `verify_no_tcid_gate.py` `len(withheld_cited) == 4` | 計數 | **範圍** | **已改**：`== len(probes)`，探針清單即其身分，加減探針不再需要改常數 |
| `verify_b_gates.py` `len(mirrored) == 18` | 計數 | **範圍** | **已改**：其欲證者為「非空掃描」，故改 `>= 1` 並列印實數。凍結 18 使下一批鏡射列一加入即誤報 |
| `verify_b_gates.py` `len(declared) == 19 and declared == produced16` | 計數 ＋ 身分 | **混合** | **已改**：刪去 `== 19`，保留 `declared == produced16`（本來就是身分式，計數只是多餘的脆弱處） |
| `verify_b_gates.py` `len(withheld) >= 20`、`size_i >= 15` | 下限 | **不必改** | 二者皆為**非空性下限**與 mutation 之注入長度，不界定成員；語料增長只會使其更容易成立 |
| `write_back.py` `FIRST_ROW = 10`、`range(FIRST_ROW, FIRST_ROW + len(tcs))` | 起點 ＋ 導出長度 | **不必改** | 起點為**範本之外部事實**（非成員界定），長度自 `len(tcs)` 導出 |
| `write_back.py` / `lint_tcs.py` `nums == list(range(1, len(nums)+1))` | 導出區間 | **不必改** | 右式自左式之長度導出，**不含任何凍結之常數** |
| `lint_tcs.py` `2 <= len(words) <= 14` | 閾值 | **不必改** | 品質閾值（title 長度），非成員界定 |
| `splits.py` `FIRST_N = 386` | 起點 | **不必改（但已具風險註記）** | 為 late tc_id 之**配置起點**而非成員界定；成員為 `SPLITS` 之鍵（身分）。其失效形態是**號碼碰撞**，而該形態由 `tc-id-sequence` gate 大聲報錯，非靜默 |
| `lint_tcs.py` `AMBIGUITY_REMARKS` / `MARKER_WHITELIST` / `MOVED_TO_BATCH16` | 具名 dict／集合 | **已是身分** | 無須處置 |

**已改 4 處、判定不必改 6 類、既已為身分 3 處。** 四項改動後
`verify_b_gates.py`、`verify_no_tcid_gate.py` 皆全數 PASS。

### 1.3 一項自陳

`splits.py` 之 `FIRST_N = 386` 是**本輪自己新引入的邊界值**——在寫下 R-C43 的
同一輪。它之所以留著，是因為它界定的是「新號碼從哪裡開始發」而不是
「誰算數」；但若日後有第二支模組也從 386 發號，兩者會撞號。
**該碰撞不是靜默的**（`tc-id-sequence` 立刻 FAIL），故依 R-C43 之自查
（「若明天多了一筆，這個界定還對嗎？」）答案是：**會錯，但會出聲**。
記此，以免日後讀者以為它被漏掉了。

---

## 2. 30 條之生成 —— 28 拆分 ＋ 2 缺口

### 2.1 實數

| 項 | 條目 | 淨增列 |
|---|---|---|
| §2 之列舉式拆分 | **28 個 leaf** | **+41** |
| §4 之缺口 | **2 個 leaf** | **+3** |
| 合計 | 30 | **+44**（385 → **429**）|

淨增 44 而非下放包預估之 46，差額全在 `033-01`（見 §2.3）。

### 2.2 逐條之列舉句（節錄；全文見 `scripts/splits.py` 之 `quote` 欄）

| leaf | 拆 | 條文列舉句（逐字，節錄） |
|---|---|---|
| `003-06` | 3 | `Manually selecting A/C, switching to another airflow mode (including front defrost), or changing fan speed …` |
| `107-06` | 2 | `Pressing MAX DEF or Max A/C the system goes to that function` |
| `107-07` | 2 | `Manually changing airflow mode or changing fan speeds breaks Auto` |
| `008-02` | 2 | `when at the Highest possible position display HI when at the lowest display LO` |
| `032-01` | 3 | `Temperature will display the current degree … Highest … HI … lowest … LO` |
| `110-01` | 2 | `Temperature ranges: LO, 60-84, HI (English), LO, 16-28, HI (Metric)` |
| `009-03` | 2 | `move 1 increment up/down per press` |
| `009-05` | 2 | `jump to a value … via touching a spot in a slider bar or voice command` |
| `009-06` | 2 | `User must press slider handle …; if user initially presses slider bar …` |
| `111-03` | 3 | `by using arrows … or slider … can jump to a value as well …` |
| `111-05` | 2 | 同 `009-06` 之對應條文 |
| `010-03` | 3 | `use Fan up/down (minus/plus) buttons, directly touch a fan segment to jump or slide` |
| `010-04` | 2 | `shall not be able to turn the FAN off by using the FAN controls on the screen or the FAN hard control` |
| `112-04` | 4 | `Fan up/down buttons, directly touch a fan segment to jump or slide, or use …` |
| `112-05` | 2 | 同 `010-04` 之對應條文 |
| `012-05` | 2 | `Auto turns Defrost off. Turning Defrost on while in Auto will break Auto …` |
| `023-01` | 3 | `there are 3 airflow mode buttons (Windshield, Face, Feet) … Each … individually toggle` |
| `023-03` | 2 | `Toggling UP (or RIGHT) moves forward … toggling DOWN (or LEFT) moves backwards` |
| `031-01` | 2 | `While unlocked = Lock Rear text …, While locked = Unlock Rear text …` |
| `032-04` | 2 | `If SYNC is ON, adjusting driver temperature affects …, adjusting passenger …` |
| `033-01` | **2** | `Fan ranges: Off, 1-7, 15h (denoting to show AUTO instead)` —— **見 §2.3** |
| `036-01` | 3 | `The Rear Airflow Modes has 3 states: 1) Feet, 2) Face + Feet, 3) Face` |
| `036-05` | 2 | `If the Rear Mode hard control is pressed … next mode available in the order` |
| `103-02` | 2 | `Popup will have a 5 sec timeout and restart with additional presses` |
| `113-09` | 4 | `Changing temperature, recirculation, mode distribution or pressing again MAX DEF break MAX DEF` |
| `119-08` | 4 | `Changing temperature, recirculation, mode distribution, or pressing MAX A/C again …` |
| `115-05` | 3 | `Actions on rear defrost, heated/vented seats or heated wheel don't reactivate climate …` |
| `118-07` | 2 | `timeout after 3 seconds of inactivity or as soon as another button except Mode HC is pressed` |

**引不出列舉句而不拆者：0 條**——28 條在 53 §2 已逐條驗過其列舉句可逐字引出，
本輪未再刷掉任何一條。

### 2.3 `033-01` 之第三值（`Off`）—— 76 §2.3 之一問，先答

**問**：條文中是否存在**可將風速置於 `Off` 之觸發**？

**答：無可自本 leaf 觸及之觸發。** 依據為 `7.5` 之逐字條文：

> The user shall not be able to turn the FAN off by using the FAN controls on
> the screen … **The only way to have all FAN bars grayed out is by shutting
> the CLIMATE system OFF**

即 `Off` 這個值**存在於顯示狀態中，但其觸發不在風速控制上**，而在
「關閉 CLIMATE 系統」——而該觸發**已是 `033-04` 之 leaf**，該處已有 TC。

**故依 76 §2.3 之第二支**：`Off / 1-7 / 15h` 為**值域之列舉而非觸發之列舉**，
不拆為三條。拆為 **2**（`1-7` 之數值域一條、`15h`／AUTO 一條），
其 `Off` 側之處置**寫入該條之 `reasoning`**：

> 該行列舉之三值中 `Off` 係顯示狀態而非可自風速控制觸及之觸發（`7.5`：
> the only way … is by shutting the CLIMATE system OFF），其觸發歸
> `HVAC-033-04` 之 leaf；此為值域之列舉而非觸發之列舉，依 §8.3 不另拆一條。

**這一問值得被問的理由**：`Fan ranges: Off, 1-7, 15h` 與
`The Rear Airflow Modes has 3 states: 1) Feet, 2) Face + Feet, 3) Face`
在版面上完全同型——都是逗號分隔的三項。**一個該拆 3、一個該拆 2**，
而區別它們的不是那一行，是**另一節有沒有給出到達該值的路**。

### 2.4 R-C28 第一問 —— `115-05` 之三條

其三個觸發（rear defrost／heated seats／heated wheel）於未配備之車輛不可觸發，
故三條各依 R-C28 第一問**引該條文之明文為 PC**（`splits.py` 之 `extra_pc`）。
其餘 25 條之觸發不依裝備，未增 PC。**無一條因引不出而不生成。**

---

## 3. `14.3`／`14.13` 之 `e.g.` —— 維持一條

依 76 §3 維持一條，未逐項驗。其 `reasoning` 已具名該列舉為 `e.g.`：
所引之例為 interaction data（§4.5），逐項驗即把條文之例示讀成窮舉
（§8.4.1；29 §2 之 `such as JL/JT` 前例）。

---

## 4. 二新缺口（76 §4）

| leaf | 依據 | 生成 |
|---|---|---|
| `007-01` | `2.5.1` 之 `3 state toggle recirc button: Auto, Manual, Open` 之**反向**（§7）——第四次按壓回到 Auto 之閉環側現無 TC | +1（共 2）|
| `040-01` | `9.2` 之 `front fan speed status (level number, AUTO, OFF)` 三值（§8.3）| +2（共 3）|

二者之 `split_reason` **具名其為 §7／§8.3 之缺口補列而非拆分**——
其母條並未被改判，補的是原本就缺的一側。

---

## 5. 寫回 —— ENTRY 021

- 產出：`…_Comfort_20260815_enumsplit.xlsx`
  sha256 `c9fda8f38f9df020698abe17bca0f4c6c328057630ad95b4866b753b2270ebfe`
- row 10–438（**429 列**），全量重寫；48 zip members，僅 `sheet6.xml` 差異
- §3.1 前置 gate **6 項全 PASS**
- §3.3 assertion **14 項中 11 PASS、3 FAIL** —— 三者與 ENTRY 004～020 同源
  （B 欄公式 row 60+、R 欄 DV row 60+、P 欄 DV row 12+），
  **皆為範本容量，DR #35 / A-CF26**
- **不可交付；依 46 §3 不送 Pei 之 Excel 四項確認**
- `DELIVERY.sha256` 追加 ENTRY 021；`output/STATUS.md`、`docs/INDEX.md` 已同步

暴露面隨本批擴大：現 **429 列中 379 列無 R 欄下拉、427 列無 P 欄下拉**
（前批為 375／383）。依 56 §6 之判定，其**不改變補救之緊急度**——
補救為單一動作，成本與列數無關。

---

## 6. §9 自評

| 項 | 自評 |
|---|---|
| §5.7（一觸發一 TC）| 本輪之全部依據；28 條之拆分維度皆自條文列舉句逐字引出 |
| §8.2.2（拆分政策）| 每條 `split_reason` 引其列舉句，未出現「不同 trigger」之空話 |
| §8.4.1（不得造值）| `e.g.` 維持一條、`033-01` 之 `Off` 不另拆——**二者皆是「不做」之判定** |
| §10.4／§10.5 | 新列之 reasoning 2–5 句、procedure ≥2 步；本輪修了 5 條單步變體與 1 條 6 句 reasoning |
| R-C30 | §1.1 已載明盤點之涵蓋範圍與**已知漏報形態** |
| R-C13 | §1.1 之漏報陳述為「未被證明不存在」而非「不存在」 |

**未做**：未改 privacy 任何檔案；未複製至客戶交付路徑；未動 prepared 檔；
未刪既有產出檔；**git 未執行**。

---

## 7. 待分析層裁定

1. §1.3 之 `splits.py FIRST_N` —— 本層判定其為**配置起點而非成員界定**，
   且其失效會出聲。若分析層認為 R-C43 之範圍及於配置起點，請明示，
   本層將改為自現有 corpus 之最大 tc_id 導出。
2. §2.3 之區分（值域之列舉 vs 觸發之列舉）目前只寫在該條之 `reasoning`。
   **若其為通則，宜升為條文**——因為它與 75 §1 之判準同型：
   兩者都在問「這個列舉是誰列的、列的是什麼」，而外觀相同、處置相反。
