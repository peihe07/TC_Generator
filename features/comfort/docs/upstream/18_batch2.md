# 18 — Comfort HMI / 批次 2：Tri-Mode Climate

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 28 §2
- 結果：**11 條生成（3.1 ×3、3.2 ×8），tc_id -015 … -025**。
  **3.3 與 3.4 之 3 個 leaf 停下回報 —— 配置軸不在 profile §3.2 之九軸內
  （28 §2.1(b)）。** lint 35/35 PASS，0 finding，全 25 條。

---

## 1. 條數 —— 宣告 14，生成 11，停下 3

| 節 | parent | 宣告 leaves | 生成 | 說明 |
|---|---|---|---|---|
| 3.1 | `SWE1-HVAC-023` | 3 | **3** | 一葉一 TC |
| 3.2 | `SWE1-HVAC-024` | 8 | **8** | 一葉一 TC，§8.2.2 未觸發（見 §4） |
| 3.3 | `SWE1-HVAC-025` | 2 | **0** | 停下，§3 |
| 3.4 | `SWE1-HVAC-026` | 1 | **0** | 停下，§3 |
| 計 | | 14 | **11** | ＋ 3 停下 |

**條數變動之理由不是 §8.2.2，是 §2.1(b) 之停下條件。** 生成之 11 條與其
leaf 為嚴格 1:1，無拆無併。

---

## 2. 生成之 11 條

`tc_id` 由位置指派（R-C7），承接 pilot 之 001–014。

| tc_id | req_id | tc_title | 步/ER | design_method |
|---|---|---|---|---|
| -015 | 023-01 | Each Tri-Mode airflow button toggles independently | 5/5 | 功能測試 |
| -016 | 023-02 | MODE hard control cycles the airflow combinations in order | 8/8 | 狀態轉換 |
| -017 | 023-03 | Multi-directional MODE control moves forward and backward | 5/5 | 狀態轉換 |
| -018 | 024-01 | MAX DEF replaces the FRONT DEF button | 2/2 | 功能測試 |
| -019 | 024-02 | MAX DEF sets seven climate states when turned on | 9/9 | 功能測試 |
| -020 | 024-03 | MAX DEF switches off automatically and restores the manual mode | 3/3 | 狀態轉換 |
| -021 | 024-04 | Pressing A/C breaks MAX DEF and leaves A/C off | 3/3 | 狀態轉換 |
| -022 | 024-05 | Pressing AUTO breaks MAX DEF and enters AUTO | 2/2 | 狀態轉換 |
| -023 | 024-06 | Pressing MAX A/C breaks MAX DEF and enters MAX A/C | 2/2 | 狀態轉換 |
| -024 | 024-07 | Temperature, RECIRC, mode and MAX DEF again each break MAX DEF | 8/8 | 決策表 |
| -025 | 024-08 | A fan speed change does not break MAX DEF | 2/2 | 功能測試 |

---

## 3. 停下回報 —— 3.3 與 3.4 之配置軸不在九軸內

**28 §2.1(b)：「若某節之配置軸不在 profile §3.2 之九軸內，停下回報，
不自行增軸。」條件成立，故停下。**

### 3.1 profile §3.2 現有之九軸

ATC／MTC、單區／雙區／四區、**tri-mode 有無**、**MAX A/C 有無**、
**MAX DEF 有無**、独立座椅分區有無、加熱方向盤 Multi／Single、
Standard vs Multi-Level 座椅、secondary lower screen 有無。

批次 2 用到其中三軸（粗體），皆合規。

### 3.2 3.3（`SWE1-HVAC-025`，2 leaves）—— 需 REAR DEFROST 有無

條文全文**僅一句**：

> C21.) MAX DEF and REAR DEF are available during climate off.

037 之兩個 leaf 之 Precondition 皆寫
`Vehicle equipped with MAX DEF and REAR DEF`。

- `MAX DEF 有無` → 第五軸，合規
- **`REAR DEFROST 有無` → 不在九軸內**

且此處有第二層問題：**該事實在 3.3 自身之 `full_text` 沒有明文對應**
—— C21 一句話裡沒有任何裝備條件。依 **R-C28 第一問**，把
「vehicle equipped with REAR DEF」標為 `(3.3)` 即為造值（§8.4.1）。

而它確實是真實變數 —— **由 3.4 證明**（3.4 明寫 rear defrost 可能
「not present in the vehicle」）。所以這不是「要不要寫 PC」的問題，
是「**這個軸該不該存在，以及它的來源節是哪一節**」的問題。**待裁。**

### 3.3 3.4（`SWE1-HVAC-026`，1 leaf）—— 需車型軸與 REAR DEFROST 有無

> C22.) For soft top vehicles such as JL/JT, when configured, the rear
> defrost button will not appear when not present in the vehicle.

兩個配置條件**皆為條文明文**（R-C28 第一問通過），但**皆不在九軸內**：

- **soft top 車型（JL/JT）** —— profile 之機型軸只有 `R1 Low / R1 High`；
  JL/JT 為車身型式，不同於機型
- **rear defrost 有無** —— 同 §3.2

### 3.4 我未做的事

- 未自行增軸
- 未以「JL/JT 屬機型軸之延伸」硬套 —— 那正是 R-C18 同型風險：
  **措辭正確地屬於別處**
- 未把三個 leaf 標為 `[BLOCKED-SPEC]` —— 該 marker 之語意為
  「條文把內容委派到別的文件」（profile §5.1），本案不是委派，
  是**本 feature 之 profile 尚未涵蓋該軸**。標錯 marker 會使
  `marker-whitelist` 之白名單被迫增列，而白名單增列須經裁定（R-C26）
- 未產生任何列 —— 依 R-C16，覆蓋缺口不產列

### 3.5 待裁之問

1. 是否於 profile §3.2 增列 **REAR DEFROST 有無**（第十軸）？其來源節為 3.4。
2. 是否於機型／變體軸增列 **soft top 車身（JL/JT）**，抑或另立車身型式軸？
3. 3.3 之 PC 若需 REAR DEF 之存在，其 `(節次)` 標註應為 `3.4`（實際出處）
   或 `3.3`（TC 所屬節）？**這是新問題，pilot 未遇過** —— 至今所有 PC 之
   出處節與 TC 所屬節同一。

裁定後可續生成該 3 條，不需重跑既有 11 條。

---

## 4. §8.2.2 之壓力測試 —— 逐 leaf 施加，結果為不拆

下放包 §2.1(a) 指 3.2 可能首次觸發 §8.2.2。**測了，未觸發。** 兩個最接近者：

### 4.1 `024-02` —— 七項連動設定

條文一次列出 A/C 開、airflow 改 Windshield、風速最高 (7/7)、溫度 HI、
RECIRC 開（LED off）、Sync 開、REAR DEFROST 啟動。

**§8.3 壓力測試：「若只有部分行為失效，pass/fail 判定是否仍明確？」**

明確 —— 條件是 **ER 逐項編號**。若風速未到 7/7，失敗定位於 ER 第 5 行。
故採 9 步／9 ER 之列舉式設計（步驟 1 建立基準狀態、步驟 2 按 MAX DEF、
步驟 3–9 逐項讀取），**procedure／ER 維持 1:1，locatability 不損**。

**不拆之理由（正面）**：七項為**同一次按壓之同時後果**，spec 未將其區分為
七個行為。拆成七條會產生 spec 不存在的區別，而每條都要重按一次 MAX DEF
—— 那是**測試設計上的重複，不是需求上的區別**。

### 4.2 `024-07` —— 四個獨立之破壞來源

改溫度／改 RECIRC／改 mode／再按 MAX DEF，四者各自獨立可失效
（改溫度會破壞而改 RECIRC 不破壞，是可能的）。**這一項比 4.1 更接近拆條。**

仍採一條，設計為 8 步／8 ER（四組「按 MAX DEF → 施加破壞源」）。
定位性同樣由編號 ER 保證：第 4 行失敗即知是 RECIRC 那一路。

**判斷之依據**：§8.2.2 允許 RD sub-id ≠ TC count，**允許不等於要求**。
四者在 037 是**一個 leaf**，其上游已判定為一個需求；拆條會使
`req_id` 一對多，而下放包明寫**反向合併禁止、拆分須同溯該 leaf**
—— 同溯是可行的，但沒有必要性：locatability 已由 ER 編號取得。

**若分析層認為此判斷過鬆，-024 為唯一需重做者**，其餘 10 條不受影響。

### 4.3 其餘六個 leaf

`024-01`／`-03`／`-04`／`-05`／`-06`／`-08` 各為單一行為，壓力測試無爭議。
`023-01`／`-02`／`-03` 同。

---

## 5. R-C28 三問 —— 逐 PC 行處理

批次 2 共 **14 行 PC**（11 條，其中 -016／-017／-023 各 2 行，餘 8 條各 1 行）。逐行第一問
之條文相關句：

| PC 行 | 第一問（出處）具名之句 | class |
|---|---|---|
| 車輛配備 Tri-Mode climate (3.1) | 「**On vehicles with Tri-Mode climate**, there are 3 airflow mode buttons」 | spec-verbatim |
| 車輛有硬鍵 MODE 按鈕 (3.1) | 「**Pressing the hard control MODE button** will cycle through all MODE combinations」 | spec-derived |
| MODE 為多向 toggle 或雙控硬鍵 (3.1) | 「**If the MODE button is a multi-directional toggle or a hard control that allows 2 controls (UP/DOWN or RIGHT/LEFT)**」 | spec-verbatim |
| 車輛配備 MAX DEF (3.2) | 「**On vehicles with MAX DEF**, MAX DEF replaces FRONT DEF button」 | spec-verbatim |
| 車輛配備 MAX A/C (3.2) | 「**Similarly, pressing MAX A/C turns MAX DEF off**」 | spec-derived |

第二問（資格）：五者皆為 spec 定義之 trigger condition（§8.5 例外），
且皆為**裝備配置**，非執行期狀態 —— TC 之步驟無論如何都建立不了它們。

第三問（落點）：因步驟無法建立，落點為 `pre_conditions`，不重複於 procedure。

### 5.1 一個要說明的判斷 —— `MAX A/C 有無` 標 spec-derived

3.2 未寫「On vehicles with MAX A/C」，只寫「pressing MAX A/C turns MAX DEF
off」。我判其通過第一問，理由：**該句所述之動作在無此裝備時不可執行**，
故裝備存在是該句之執行前提，非我的補充。

**這與 TC-007 之差別須寫明，因為形狀相近**：TC-007 是由
「last selected」推出一個**執行期狀態**（曾有選擇行為 ≠ 恆有選定項）；
此處推出的是**裝備存在**，而條文正在描述對該裝備之操作。
前者推的是歷史，後者推的是句子自身的執行條件。

**若分析層認為此推論仍屬第一問不合格，-023 之 PC2 應刪，改於 procedure
第一步建立** —— 但那在物理上不可行（裝備不能由步驟裝上去），
故真正的替代方案是**該條退回，與 3.3／3.4 一同待軸之裁定**。列此待覆核。

### 5.2 未寫入 pre_conditions 者

A/C、AUTO、溫度、風速、RECIRC、mode 等基本控制**未寫入 PC** ——
profile §3.2 明禁 `Climate is available` 型隱含環境前提。
循環之起點（Face 模式）亦未寫入 PC，而由 procedure 第一步建立
（§7 FF ＋ R-C28 第三問）。

---

## 6. §8.2.1 —— 3.3 之委派具名

即使 3.3 本輪未生成，其邊界已確認並記此備用：

`SWE1-HVAC-025-02`（other climate functions remain off/grayed out）之內容
**定義於 2.10（C11，Climate Modes）**：

> When the system is turned off, show the CLIMATE OFF screen with the OFF
> button turned into an ON button and **grey out remaining buttons except for
> Front/max defrost and rear defrost**.

3.3 自身之全文只有一句，未述其他功能之狀態。故該 leaf 之 TC 若生成，
其 `reasoning` 須具名 2.10 為委派節次，且**不得驗證 greyed out 之行為**
（§8.2.1 不得擴張至 sibling Req）。

---

## 7. lint

```
35 / 35 gates PASS; 0 finding(s) across 25 TCs
```

含下放包 26 §4 之三項（`json-key-coverage`、`anomaly-id-registered`、
`residue-scan-window`），三項之反向驗證見上繳 17 §2。

批次 2 於既有 32 gate 下**首次即全過**，但這不構成「本批較好」之證據
—— pilot 之六次 defect 有五次是 lint 抓不到的判斷問題（PC 落點、PC 出處、
ER 主詞），gate 全過只說明它沒犯 gate 能表達的錯。

---

## 8. §9 self-check 17 項 —— 依 R-C23 逐項具名獨立依據

**每項之依據須獨立於 lint**，不得以「某 gate 通過」充數；凡依據即為某
gate 者，明說並補一項 lint 未覆蓋之獨立查核。

| # | 項目 | 判 | 獨立依據（非 lint 覆述） |
|---|---|---|---|
| 1 | Test Set 名詞片語、與 framework 相符 | PASS | 人工比對 `framework.md` Part N 第 3 組之名稱 `Tri-Mode Climate`，逐字元相同；無 Test Group 前綴、非 Unclassified |
| 2 | tc_title 三種形狀之一、2–14 字、sibling token 可見、無 modal | PASS | 逐條讀 11 個 title：11 條皆為「主詞＋行為」形；字數實測 6–11；sibling token（Face／MODE／A/C／AUTO／MAX A/C／fan speed）逐條可見於 title 本身 |
| 3 | PC 僅 state/env，且為 spec trigger（§8.5） | PASS | §5 之三問表逐行處理，五類 PC 皆為**裝備配置**；另實測 PC 內無 `Press`／`Open`／`Toggle`／`Change`／`Set` 等動作動詞 → 0 命中 |
| 4 | Input Test Data 欄位歸屬，重複資料下放 | PASS | 11 條 `input_test_data` 相異值僅 `{"NA"}`。本批無數值型輸入 —— 全為 UI 操作，資料即操作對象，已在 procedure |
| 5 | 步驟可執行、無禁用動詞、Final Step 擁有驗證 | PASS | 以 §5.1 之九個禁用主動詞（observe／see if／check whether／confirm whether／verify／watch／monitor／inspect，另加 locate）掃 25 條 procedure 之行首動詞 → **0 命中**。初稿曾用 `Check the …`／`Locate …`，已改為 §5.1 之偏好動詞 `Read` |
| 6 | 步驟長度與意圖層級 | PASS | 步數實測 2/2/2/2/3/3/5/5/8/8/9；最長者 -019 之 9 步為七項連動之逐項讀取，非贅步；無 `... to ...` 贅接 |
| 7 | 標準 setup 片段逐字重用 | **N/A** | 本 feature 無標準 setup 片段庫。`PC_TRIMODE`／`PC_MAXDEF`／`PC_MODE_HC` 為生成器常數，同節內逐字重用，**跨節不套用**（19 §2.1 之紀律） |
| 8 | CLI／tooling 步驟格式 | **N/A** | 本批 11 條皆為 HMI 觸控／硬鍵操作，無 CLI 步驟 |
| 9 | 需要前後對照時有基線步驟 | PASS | 7 條之 ER 第 1 行為前狀態（-015 螢幕呈現、-016／-017 循環起點、-019 MAX DEF 未作用、-020／-021 手動模式設定值）。其餘 4 條（-018／-022／-023／-025）之驗證不涉前後差，無需基線 |
| 10 | procedure↔ER 1:1、ER 可觀察、無 modal | PASS | **此項之 lint 依據為 `proc-er-1to1`／`er-modal`，故另查「可觀察」**：逐條讀 11 條之 ER 全部 49 行，主詞皆為系統側之物（button／mode／fan speed／temperature／RECIRC／Sync／REAR DEFROST／climate system），**無一行以觀察者為主詞**（rev1 `is readable`、rev2 `is recorded` 之形態未再出現） |
| 11 | 無 FP／FF；supported 配 negative | PASS | FF：循環起點、手動模式基準值、MAX DEF 之初始關閉皆由步驟建立，未假定。negative：`-025`（風速改變**不**破壞 MAX DEF）即 `-024`（四者**會**破壞）之反面，兩者成對 |
| 12 | 溯源、§8.2.1 不擴張、§8.2.2、無造值 | PASS | 溯源：11 條之 `req_id` 對 037 之 `SWE1-HVAC-023-01`…`-024-08`，逐一存在且無重覆。§8.2.1：3.3 之委派已具名 2.10（§6），本批未涉。§8.2.2：壓力測試逐 leaf 施加（§4）。造值：3.2 之「set time」無數值，`-020` 之步驟以可觀察量終止，**未寫入任何秒數** |
| 13 | Design Method 於 procedure 定案後指派 | PASS | 生成器內 `design_method` 位於每個 TC 之末欄，於 procedure／ER 之後；三值之分派可由 procedure 形狀反推 —— 有狀態遷移者 狀態轉換（6 條）、多條件分支者 決策表（-024）、單純功能者 功能測試（4 條） |
| 14 | 四個長欄無行尾句點 | PASS | lint `trailing-period` 覆蓋；**另查其未覆蓋者**：11 條之 `test_item`（非長欄，不在該 gate 範圍）亦逐條確認無行尾句點 |
| 15 | UI 標籤用 `"..."` 不用 `[...]` | PASS | lint `ui-bracket` 僅擋方括號；**另查引號之實際使用**：`"Face"`／`"Feet"`／`"Windshield"`／`"MAX DEF"`／`"FRONT DEF"`／`"A/C"`／`"AUTO"`／`"MAX A/C"` 逐條加引號。未加引號者為狀態名（Windshield 作為 airflow mode 值）而非按鈕標籤，**兩者刻意分寫** |
| 16 | `specification_reference` 列出所有直接驗證之節 | PASS | 11 條之 spec_ref 相異後綴僅 `{3.1, 3.2}`，與其 parent 一致。**無一條直接驗證第二個節** —— 若 3.3 生成，其 PC 之出處問題即 §3.5 待裁第 3 問 |
| 17 | 來源 spec 勝過 index export；閾值為 spec 具體值 | PASS | 條文一律讀 `section_fulltext.tsv`（未截斷），**未讀 `section_title`**（R-C18）。閾值：`7/7`、`HI` 皆為 3.2 之原文；`-016` 之七種組合順序逐字照 3.2 之列舉，未重排 |

**15 PASS、2 N/A**（第 7、8 項）。兩個 N/A 依 R-C23 具名理由，非以「不適用」
一詞帶過。

---

## 9. 未寫回 workbook

依 28 §2.2 第 4 項，**本批未寫回**。`output/` 仍為 2 檔（prepared、pilot），
`DELIVERY.sha256` 未增列，`write_back.py` 未執行。

---

## 10. 進度

| | 數 |
|---|---|
| 驗證單位（037 Functional Requirement） | 403 |
| 已生成 | **25**（pilot 14 ＋ 批次 2 之 11） |
| 本批停下待裁 | 3 |
| 未開始 | 375 |

---

## 11. 「本包是否仍有該驗而未驗者」

1. **§5.1 之禁用動詞我是自己補進掃描的。** lint 沒有這個 gate ——
   初稿之 `Check the A/C state`／`Locate the front defrost control` 兩處
   若非我在 §9 第 5 項手查，會原樣留下。**建議加 `forbidden-verb` gate**
   （行首主動詞比對 §5.1 之九詞），未自行加入。
2. **ER 主詞之檢查仍是人眼。** §9 第 10 項之 49 行逐行讀是我讀的；
   rev1／rev2 兩次栽在同一處，正說明人眼會漏。**該判準難以機械化**
   （主詞辨識），但至少可擋詞表（`is recorded`／`is readable`／`is noted`
   ／`can be read`）—— 那是 22 §4 明說「用詞禁令可繞過」的東西，
   故只能當補網不能當判準。列此說明現況，不建議以詞表冒充判準。
3. **`-023` 之 `MAX A/C 有無` 標 spec-derived 是本包最可能被推翻者**
   （§5.1）。我把理由寫出來而非默默保留。
4. **`-024` 之不拆是次可能被推翻者**（§4.2）。
5. **11 條之 ER 未經任何交叉檢驗** —— 沒有第二個來源可對照 3.1／3.2 之
   行為（037 之 Verification Criteria 與 leaf description 同源，非獨立）。
   這是本 feature 一貫狀況，非本批新增。

---

## 12. 建議 commit message（git 未執行）

```
feat(comfort): generate batch 2 — Tri-Mode Climate, 11 TCs

- 3.1 (3 leaves) and 3.2 (8 leaves) authored, tc_id -015..-025
- 3.3 and 3.4 withheld: their configuration axes (rear defrost presence,
  soft top JL/JT) are not among profile 3.2's nine; no rows produced
- every pre_condition passes R-C28's three questions with the clause
  sentence named
- 8.2.2 pressure-tested per leaf; no split taken, reasoning recorded
- lint 35/35 PASS, 0 findings across 25 TCs
```

---

## 13. 待分析層

**§3.5 之三個軸相關問題**。裁定後 3.3／3.4 之 3 條可續生成，
既有 11 條不受影響。
