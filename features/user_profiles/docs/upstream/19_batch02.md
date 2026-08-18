# 上繳 19（作業 1–5）— J-7～J-12 落地與第二批生成

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`19_batch02.md`（**無裁決條文**）
- 另一份上繳：`19_provenance3.md`（作業 6，第二批之 ER 出處對照）
- **本輪未執行任何 git**；**未寫回工作簿**（R-U14）
- 語料：**73 條 TC**（pilot 16 ＋ 第一批 28 ＋ 第二批 29）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | **73 條，違規 0** |
| `lint_tcs.py --self-test` | **51 / 51**（原 44 ＋ **J-10 七案**）|
| `lint_variant_labels.py` 反向 | **11 / 11**（原 9 ＋ **J-11 兩案**）|
| `lint_variant_labels.py --check` | 73 條，違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |

```
掃 73 個 leaf 檔 / 73 條 TC
tc_id 範圍 NR1L-UserProfiles-001 … NR1L-UserProfiles-073（73 條）
design_method 分布：功能測試×40, 基礎故障注入×2, 情境 / 用例×3,
                    狀態轉換×10, 負向測試×11, 邊界值分析×7
priority 分布：P0×17, P1×25, P2×28, P3×3
違規 0
```

---

## 1. 作業 1 —— J-7／J-8 落地

### 1.1 J-7：`PROF-088`（TC-020）之 remarks 與 RD

ER 維持 9.2 之逐字；remarks 改為：

> label 逐字取自 9.2。R1 High 車上該按鈕之 label 可能顯示為 Connected Account；
> **兩者指同一個按鈕**，本 TC 驗其**不顯示**，label 形式不影響判定（J-7）。
> 該覆寫是否及於本節已列 RD 查詢（併 DR #3 送出）。

**`DATA_REQUESTS.md` 新增 RD #5**，載明：覆寫在版面上為列級之**座標依據**
（註記於 x=101.4／y=275.9–286.7，對應之列於 y=289.8，表中其餘列無 `****`）、
受影響之兩節（9.1／9.2）、以及**若答案為「及於全章」須連帶處理之三處**
（`VARIANT_LABEL_OVERRIDES` 之適用範圍、9.1／9.2 之 ER 逐字、TC-017 已用之形式）。

### 1.2 J-8：`128-03` 照寫並註明成本

`remarks`：

> **執行成本：本 TC 需 30 分鐘等待**（J-8：照寫、不縮時、不刪除）。
> 縮時屬測試實作之手段（bench 上如何撥時鐘），非 TC 內容之決定；排程時須計入。

並依 J-8 之分工，把「不需等待」之部分切給 `128-02`（鎖定**生效**），
`128-03` 只承擔**時間長度**之驗證 —— 兩條之 remarks 互相指名。

---

## 2. 作業 2 —— J-10：兩閘之盲區補上（**首跑結果如實回報**）

### 2.1 G18 擴及未加引號之字面值

新增三類：**PU id**、**數值**、**狀態值**（`Small`／`Off`／`On`／`None`）。
掃描前移除行首編號與 `step N` 之互參。

### 2.2 G17 增 `provides` 欄

`REF_EXTRA` 每筆由 `"9.3.1"` 改為 `("9.3.1", "Function not available while
vehicle in Motion.")`，G17 驗**該字面值確實出現在該 TC 之欄位內**。

### 2.3 **首跑：紅 6 條**（44 條語料）

```
G18 TC-008: ER 之數值 `29` 溯不到被引之節，亦未登記為測試設置
G18 TC-010: ER 之數值 `2` 溯不到被引之節
G18 TC-009: ER 之數值 `11` 溯不到被引之節
G17 TC-022: `REF_EXTRA` 登記 `9.3` 提供「cannot be selected」，
            但該字面值不在本 TC 之欄位內
G18 TC-032: ER 之狀態值 `Small` 溯不到被引之節
G18 TC-032: ER 之狀態值 `Off` 溯不到被引之節
```

**逐條追因 —— 一條真陽性、五條判準未涵蓋**：

| # | 條 | 追因 | 處置 |
|---|---|---|---|
| 1 | TC-008 `29`、TC-009 `11` | BVA 之**界前讀值**（邊界 30／12）。**它承載驗證，但其權威是 §5.6 而非條文** | 立 `METHOD_NUMERALS` 登記（J-4 之「方法」類），**不是測試設置** |
| 2 | TC-010 `2` | ER 為 `the username and avatar from **steps 1 and 2**` —— 是**步驟互參**。判準只移除 `step \d`，未處理 `steps 1 and 2` | **改判準**：`steps?\s+\d+(\s*(and\|,\|-\|to)\s*\d+)*` |
| 3 | **TC-022 `provides` 不符** | **真陽性** —— 我登記 9.3 提供 `cannot be selected`，而 TC 之 ER 寫的是 `The selection is not accepted`。**登記時寫的字面值不是 TC 裡的字面值** | 改為 `Delete Profile`（步驟 1 選的正是 9.3 清單之該項）|
| 4 | TC-032 `Small`／`Off` | spec 以散文寫小寫（`default on small`、`If turned off`），UI 以首字大寫顯示 | **改判準**：狀態值以大小寫不敏感比對 —— 大小寫之差是呈現形式，不是字面值不同 |

**J-10 之收穫即第 3 項**：舊 G17「有登記就綠」，登記一個不相干的節照樣通過；
加了 `provides` 驗證之後，**我自己登記錯的那一筆立刻現形**。

### 2.4 第二批生成後之第二次首跑：**再紅 3 條**

```
G18 TC-056: ER 之數值 `1` 溯不到（memory seat 1）→ 登記為測試設置
G18 TC-066: ER 之數值 `29` 溯不到（30 分鐘之界前值）→ 登記為方法
G17 TC-072: `REF_EXTRA` 登記 `12.6` 提供「deactivate Valet Mode」，
            但該字面值不在本 TC 之欄位內
```

**TC-072 又是真陽性**：我為 `134` 併列了 12.3.1 與 12.6，
但本 TC 走的是 welcome popup 之按鈕，**12.6 給的是「按狀態列 Profile 鍵」那條路徑
—— 沒被用到，屬多引**。已移除 12.6。

**G17 之 `provides` 在兩個批次各抓到一筆我自己的多引。**

### 2.5 一個舊案例隨判準失效（同 14 輪 G2 之形態）

18 輪之「G17 範圍：REF_EXTRA 已登記之節 → 綠」其 fixture 之 ER 為 `1. a / 2. b`。
J-10 加了 `provides` 驗證後，**同一個 fixture 會紅** —— 它測的性質被擴充了，不是它壞了。
已補上該字面值，使其仍測「已登記之節不得轉紅」這一半。

---

## 3. 作業 3 —— J-11：兩個範圍分離

| 用途 | 掃描範圍 |
|---|---|
| **variant 之判定** | `pre_conditions`／`test_procedure`（**新**）|
| **禁用字串之檢查** | `tc_title`／`test_item`／`pre_conditions`／`test_procedure`／`expected_result`／**`remarks`**（不變）|

方向性兩案：

```
PASS — **remarks 之中文討論**提到 R1 High → **不得**改變 variant 判定（J-11）: clean
PASS — 判定為 R1 High 後，**remarks** 之禁用字串仍轉紅（J-11 之另一半）: FAIL（期望 FAIL）
```

**效果**：TC-020 之 remarks 現以中文討論「覆寫是否及於本節」，
**不再被判為 R1 High**；而若某條真為 R1 High，其 remarks 寫了禁用字串仍會紅。

---

## 4. 作業 4／5 —— J-12 之第四類與第二批生成

### 4.1 J-12：`測試設置` 標示已落地

| tc_id | 值 | 類 | 已標於 |
|---|---|---|---|
| 028／029／031 | `memory seat 1`／`2` | 測試設置 | reasoning ＋ `TEST_SETUP_NUMERALS` |
| 030 | 座椅數 2、profile 數 2→3 | 測試設置 | 同上 |
| 056（本批）| `memory seat 1` | 測試設置 | 同上 |
| 008／009／066 | `29`／`11`／`29` | **方法**（§5.6 界前值）| `METHOD_NUMERALS` |

**四類之界線（本輪釐清）**：`ignition cycle` 是**裁決**指定之觀察點（驗什麼）；
座椅編號是**測試設置**（怎麼擺，不承載驗證）；
BVA 界前值是**方法**（承載驗證，但權威是 §5.6 而非條文）。

### 4.2 第二批：**29 條，tc_id 045–073**

`data/batch02_sample.tsv`（29 leaf）＋ `scripts/gen_batch02.py`。
**實得 29 條，非 18 輪估計之 34** —— 差額之三條為 §7 之負向配對，見 §6。

---

## 5. **`134`（14.1）之 R-U51 判讀首次受檢 —— 結論成立，理由有誤**

11 輪之盲區掃描把 `134` 之 `…will initiate the Exit Valet Mode process
**above**` 判為「**指向 14.x 之流程**，非 PLP 表」。

**本輪複位**：

```
ch14 之節次：14（無內文）／14.1／14.2  —— 只有兩節
14.1 即 ch14 之首條
```

**故 `above` 不可能指向 ch14 之任何東西** —— 14.1 之上沒有 14.x。
其實際指涉為 **12.3.1**（`To get out of Valet Mode the same 4 digit PIN needs
to be entered`）所述之退出流程。

| | 11 輪所記 | 本輪複位 |
|---|---|---|
| 結論（非 PLP 表）| ✓ | **✓ 維持** |
| 理由（指向 14.x）| —— | **✗ ch14 無 14.1 之前的節** |

**具體後果**：`134` 之 TC 其 ER3 以「4 位 PIN 輸入畫面」為退出流程之可觀察形態，
其出處為 12.3.1 —— **該節原不在引用欄內**（少引之形態，同 5.1.1）。已併列。

**這是 R-U51 之判讀第一次被 TC 檢驗，而它抓到的是判讀之理由而非其結論。**
結論對而理由錯，在別的案例上不一定還會對。

---

## 6. 18 輪 §4 之六項風險 —— 逐項實際結果

| # | 風險（18 輪所列）| **實際結果** |
|---|---|---|
| 1 | `Service` 三條（119／124／127）需 key cycle 或斷電級操作；`119` 之觀察點恐再落入「裁決來源」| **未落入**。119 之 `at the next key on` 為**條文明述**，其權威是 spec 不是 R-U21 —— 已於 reasoning 具名此區別。124／127 之觀察點亦皆為條文所述之狀態 |
| 2 | `128-03` 之 30 分鐘等待 | 依 J-8 **照寫**，remarks 具名成本；並把「不需等待」之鎖定生效切給 `128-02`，使 29 條中只有一條需長時等待 |
| 3 | PIN 類判 P0，本批 P0 比例顯著上升 | **實得 P0 8／29 ≈ 27.6%**（全語料 17／73 ≈ 23.3%）。依 J-9 **未因比例調整 rubric** |
| 4 | SPAAK 群與 pilot 之 `016` 同組，G5 恐雷同 | **G5 未觸發**。`132-01`（主機各入口皆阻擋）與 pilot `016`（車主遠端可停用）之標題各帶其軸 |
| 5 | **12.8／12.8.1 七個 sub-id 為 §8.3 之最大壓力點** | **G5 未觸發**，但發現更嚴重的事：**037 之標題與描述錯位**（見 §7 第 1 項與 A-UP11）|
| 6 | R-U5 之 rubric 無安全帶，本批影響遠大於第一批 | **確認**。本批至少 `116`／`135` 兩條之失效後果為「行進中之安全」，第一批只有 `089` 一條。**仍待裁**，本輪就近歸類並於各條 `priority_basis` 具名 |

---

## 7. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **A-UP11：037 標題／描述錯位** | **新開 PENDING** | 本輪只複核 12.8／12.8.1 七條，**未全量掃描 037 之 title↔description 對齊**。若他章亦有，先前批次之取樣理由欄可能引到錯的標題 |
| 2 | **§7 負向配對未另切 TC** | **待覆核之選擇** | 18 輪估 +3；本輪把對照組置於**同一 TC 之 ER**（125-02 之 ER4「Media 仍可用」、125-03 之 ER3「HVAC 圖示仍回應」、129 之 ER4「4 碼後 Go 可用」）。理由：對照與受測項同觸發同條件，分兩條會產生除斷言外全同之 TC。**若分析層要求分立，改寫成本為三條** |
| 3 | **`115` 與 `132-01` 之「窮舉入口」不可能完備** | note | 兩條都驗「別處沒有」，而畫面數不可窮舉。各取兩個最可能之位置，**此為抽樣**，已於 reasoning 具名 |
| 4 | **R-U5 無安全帶** | **待裁（第三次提出）** | 17 輪 §4 第 1 項提出、18 輪 §4 第 6 項預告、本輪實得兩條。**本批已生成，若裁定後 rubric 有變，受影響者為 116／135／089 三條之 priority** |
| 5 | **`128-03` 之可執行性** | 已依 J-8 處置 | TC 本身無問題，**但它仍是一條需 30 分鐘等待之 TC**；排程時看得見即達 J-8 之目的 |
| 6 | **第二批之內容覆核未做** | **分析層待辦** | 第一批之內容覆核亦仍未完成（19 包自記）。**兩批合計 57 條之內容未經第二人讀過** |
| 7 | **G18 仍不查非引號之英文詞組** | 判準盲區（R-G11）| 現查：引號字串、PU id、數值、四個狀態值。**不查**：`Bonk`、`Go`、`Device Manager` 等未加引號之 UI 名詞 |
| 8 | A-UP09／R-U14、DR #3／#4／**#5**、R-U17、N-XF01、A-UP10 | 承前 | 擋 Phase 6 寫回 |

---

## 8. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | **檔案新建** | `scripts/gen_batch02.py`（29 條之單一來源）、`data/batch02_sample.tsv` | 否 |
| 2 | **檔案新建 ×29** | `generated/`（045–073）| 否 |
| 3 | 檔案編輯 | `scripts/lint_tcs.py`（G18 擴及未加引號字面值、G17 之 `provides` 驗證、`METHOD_NUMERALS`／`TEST_SETUP_NUMERALS`、七個方向性案例、一個失效案例更新）| 否 |
| 4 | 檔案編輯 | `scripts/lint_variant_labels.py`（J-11 之 `VARIANT_SCAN_FIELDS` ＋ 兩案例）| 否 |
| 5 | 檔案編輯 | `scripts/gen_pilot.py`／`gen_batch01.py`（`REF_EXTRA` 加 `provides`；J-7 之 remarks；J-12 之標示；TC-022 之 provides 更正）| 否 |
| 6 | 檔案追加 | `DATA_REQUESTS.md`（**RD #5**）、`ANOMALIES.md`（**A-UP11**）| 否 |
| 7 | 檔案新建 | `docs/upstream/19_batch02.md`（本檔）、`docs/upstream/19_provenance3.md` | 否 |
| 8 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 9 | 程式執行 | 生成 ×3、`lint_tcs`（語料＋self-test）、`lint_variant_labels`（反向＋check）、`--selfcheck`、`render_spec_region --regression` | 否 |
| 10 | **唯讀** | `fitz` 讀 spec PDF（p14 之 `****` 座標、ch14 之節次清單）| 否 |

**本輪未執行任何 git**：`add`／`commit`／`push`／`checkout`／`restore`／`reset`／
`rebase`／`stash`／`clean`／`rm` 皆無，**唯讀之 `git status` 亦未跑**。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`（本包無裁決條文）、`DECISIONS.md`、`BASELINE.sha256`、`.gitignore`、
`data/` 之其餘檔、**他 feature 之任何檔**、`docs/fw036/`。

---

## 9. 第二批 29 條 TC 全文

> `test_group` 皆為 `User Profiles`；`test_item` 依 R-U6 等同 `tc_title`；
> `functional_safety` 全批 `NA`；`estimated_test_time` 全批留空；`split_flag` 全批 false。
> 路徑：`features/user_profiles/generated/<req_id>.json`

### NR1L-UserProfiles-045 — SWE1-HMI-PROF-113（12.1）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode starts from defaults and restores on exit |
| pre_conditions | 1. A Driver Profile with customized preferences is active<br>2. Valet Mode is not active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the preferences of the active Profile<br>2. Activate Valet Mode<br>3. Read the preferences and change one of them<br>4. Exit Valet Mode<br>5. Read the preferences and check that they match those recorded in step 1 |
| expected_result | 1. The preferences of the active Profile are recorded<br>2. Valet Mode is active and its preferences are the default ones, not those recorded in step 1<br>3. The changed preference is stored while Valet Mode is active<br>4. Valet Mode is exited<br>5. The preferences match those recorded in step 1 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.1 |
| priority | **P0** — Valet 進出時之偏好儲存與重設 —— 核心五類之二者交會 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | （空） |

**reasoning**：驗證目標：12.1（PVAL1）—— 啟用 Valet Mode 視同以預設偏好建立新 profile，退出視同刪除該 profile；期間之變更只存到退出為止。關鍵情境條件：須有一個已客製化之 profile 作為基準線，否則「預設 vs 客製」分不出來（§5.6）。為什麼這樣切：進入與退出雖為兩個觸發，但條文以「像建立／像刪除」成對定義，**只驗一半則另一半之語意不成立** —— 同 13.2 之處置（§5.7 之例外，具名）。

### NR1L-UserProfiles-046 — SWE1-HMI-PROF-114（12.1.1）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Status bar returns to its default setup in Valet Mode |
| pre_conditions | 1. The status bar is configured away from its default setup<br>2. Valet Mode is not active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the current status bar setup<br>2. Activate Valet Mode<br>3. Read the status bar and check that it shows the default setup with the Profile icon visible |
| expected_result | 1. The current status bar setup is recorded<br>2. Valet Mode is active<br>3. The status bar shows the default setup and the Profile icon is visible |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.1.1 |
| priority | **P2** — 狀態列之預設版面；呈現層 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.1.1（PVAL1.1）—— Valet Mode 啟用時狀態列須回到預設版面，使 Profile 圖示恆可見。關鍵情境條件：pre-condition 要求狀態列先偏離預設，否則「回到預設」與「本來就是預設」無從分辨。為什麼這樣切：預設版面之細節條文委派 Core HMI Logic and Flow，本 TC 只驗其回到預設且 Profile 圖示可見（§8.4.1 不代擬他份文件之內容）。

### NR1L-UserProfiles-047 — SWE1-HMI-PROF-115（12.2）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode activates only from the All Profiles tab |
| pre_conditions | 1. Valet Mode is not active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “Edit Profile” tab and read the option list<br>2. Open the vehicle settings and read the option list<br>3. Open the “All Profiles” tab and check that the Valet Mode button is present there |
| expected_result | 1. No Valet Mode activation control is present on the “Edit Profile” tab<br>2. No Valet Mode activation control is present in the vehicle settings<br>3. The Valet Mode button is present on the “All Profiles” tab |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.2 |
| priority | **P1** — 啟用入口之限制；非主路徑分支 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：12.2（PVAL2）—— Valet Mode 只能經 All Profiles 分頁之按鈕啟用。關鍵情境條件：「只能」之驗證須同時看兩側 ——別處沒有（步驟 1、2）與該處有（步驟 3）；**只驗該處有，一個到處都能啟用之實作也會通過**（§7）。為什麼這樣切：受檢之他處取 Edit Profile 分頁與車輛設定兩個最可能之位置；**窮舉所有畫面不可行**，此為抽樣，已於上繳具名。

### NR1L-UserProfiles-048 — SWE1-HMI-PROF-116（12.2.1）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode button greyed out while the vehicle is in motion |
| pre_conditions | 1. Valet Mode is not active<br>2. The vehicle is stationary on a test track and can be brought into motion |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and read the Valet Mode button<br>2. Bring the vehicle into motion<br>3. Read the Valet Mode button and press it<br>4. Read the screen and check that the unavailability popup is displayed |
| expected_result | 1. The Valet Mode button is selectable while stationary<br>2. The vehicle is in motion<br>3. The Valet Mode button is greyed out<br>4. PU0091 indicates that the function is not available |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.2.1 |
| priority | **P1** — 行車中之啟用限制分支（**rubric 無安全帶，見上繳 19 §7**） |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | （空） |

**reasoning**：驗證目標：12.2.1（PVAL2.1）—— 行車中 Valet Mode 按鈕變灰；按下已變灰之按鈕時顯示 PU0091。關鍵情境條件：以靜止時可選為基準線（§5.6），判準為靜止→行進之狀態轉換（§12 首匹配 → 狀態轉換）。為什麼這樣切：變灰與按下之提示為同一條件下之兩個結果，037 未再切分，故併為一條（§5.7）。

### NR1L-UserProfiles-049 — SWE1-HMI-PROF-117（12.3）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Four-digit PIN required to activate Valet Mode |
| pre_conditions | 1. Valet Mode is not active<br>2. The vehicle is stationary |
| input_test_data | PIN: a 4-digit one-time PIN chosen at activation |
| test_procedure | 1. Open the “All Profiles” tab and press the Valet Mode button<br>2. Read the screen and check that a 4-digit PIN entry is required<br>3. Enter a 4-digit PIN and confirm<br>4. Read the screen and check that Valet Mode is active |
| expected_result | 1. The Valet Mode activation is started<br>2. A 4-digit PIN entry is requested before activation<br>3. The 4-digit PIN is accepted<br>4. Valet Mode is active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.3 |
| priority | **P0** — 啟用之 PIN —— Valet Mode 之防護本身 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.3（PVAL3）—— 啟用 Valet Mode 須輸入 4 位一次性 PIN。關鍵情境條件：ER2 明寫「在啟用之前」要求 PIN ——若寫成「輸入 PIN 後啟用」，一個先啟用再問 PIN 之實作也會通過（§7）。為什麼這樣切：停用側之同一 PIN 屬 12.3.1，PIN 錯誤之次數上限屬 12.9，皆不在本條。

### NR1L-UserProfiles-050 — SWE1-HMI-PROF-118（12.3.1）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Same four-digit PIN required to leave Valet Mode |
| pre_conditions | 1. Valet Mode is active and was activated with a known 4-digit PIN<br>2. The vehicle is stationary |
| input_test_data | PIN: the same 4-digit PIN used at activation; one differing 4-digit PIN |
| test_procedure | 1. Start the Valet Mode deactivation<br>2. Enter a 4-digit PIN that differs from the activation PIN<br>3. Enter the same 4-digit PIN used at activation<br>4. Read the screen and check that Valet Mode is no longer active |
| expected_result | 1. The PIN entry for deactivation is displayed<br>2. The differing PIN is rejected and Valet Mode is still active<br>3. The same PIN as at activation is accepted<br>4. Valet Mode is no longer active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.3.1 |
| priority | **P0** — 停用之 PIN —— 同上 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.3.1（PVAL3.1）—— 退出 Valet Mode 須輸入**與啟用時相同**之 PIN。關鍵情境條件：「相同」之驗證須有一個不同之 PIN 作對照（§7）——只驗正確 PIN 可退出，一個任何 4 位數都接受之實作也會通過。為什麼這樣切：錯誤次數之上限屬 12.9，本條只驗「須相同」。

### NR1L-UserProfiles-051 — SWE1-HMI-PROF-119（12.3.2）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Battery disconnect resets Valet Mode at the next key on |
| pre_conditions | 1. Valet Mode is active<br>2. The last known Driver Profile before Valet Mode is recorded<br>3. The vehicle is stationary and the battery can be disconnected on the bench |
| input_test_data | Fault injected: battery disconnected while Valet Mode is active |
| test_procedure | 1. Disconnect the vehicle battery<br>2. Reconnect the battery and switch the key on<br>3. Read the active Profile and check that Valet Mode is no longer active |
| expected_result | 1. The battery is disconnected<br>2. The vehicle powers up at key on<br>3. Valet Mode is not active and the last known Driver Profile is loaded |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.3.2 |
| priority | **P1** — 斷電後之重設與 profile 接續；spec 明訂之行為，非漏洞 |
| design_method | 基礎故障注入 (Fault Injection Lite) |
| remarks | （空） |

**reasoning**：驗證目標：12.3.2（PVAL3.2）—— 斷開電瓶會覆寫並重設 Valet Mode，下次 key on 時載入最後已知之 Driver Profile。關鍵情境條件：斷電為可模擬之故障（§12 首匹配 → 基礎故障注入）；「最後已知 profile」須於 pre-condition 先記錄，否則無比對對象。**來源標示（J-4）**：`key on` 之觀察點與 `ignition cycle` 同屬 **R-U21** 之「設定→key cycle→讀回」形態，惟本條之 key on 為**條文明述**（`at the next key on`），故其權威為 spec 而非裁決。

### NR1L-UserProfiles-052 — SWE1-HMI-PROF-120（12.3.3）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Previous Profile restored after Valet Mode is exited |
| pre_conditions | 1. Driver Profile A is active and Valet Mode is not active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the active Profile<br>2. Activate Valet Mode<br>3. Deactivate Valet Mode<br>4. Read the active Profile and check that it matches the one recorded in step 1 |
| expected_result | 1. Driver Profile A is recorded as active<br>2. Valet Mode is active<br>3. Valet Mode is deactivated<br>4. Driver Profile A is active again |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.3.3 |
| priority | **P1** — 退出後之 profile 接續 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | （空） |

**reasoning**：驗證目標：12.3.3（PVAL3.3）—— 退出 Valet Mode 後回到先前之 profile。關鍵情境條件：以步驟 1 之記錄為基準線（§5.6）。為什麼這樣切：Valet Mode 期間之偏好處置屬 12.1，本條只驗退出後之 profile 接續。

### NR1L-UserProfiles-053 — SWE1-HMI-PROF-121（12.4）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Pressing elsewhere cancels the Valet PIN entry |
| pre_conditions | 1. Valet Mode is not active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Start the Valet Mode activation so that the PIN entry is displayed<br>2. Press another portion of the screen outside the PIN entry<br>3. Read the screen and check that the PIN entry is cancelled |
| expected_result | 1. The PIN entry is displayed<br>2. The press outside the PIN entry is treated as a cancel command<br>3. The PIN entry is closed and Valet Mode is not active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.4 |
| priority | **P2** — PIN 輸入之取消路徑 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.4（PVAL4）—— PIN 輸入期間按畫面他處視為取消。關鍵情境條件：條文涵蓋啟用與停用兩側之 PIN，本條取啟用側；停用側之取消行為相同，未另切 TC（037 未為其切 leaf）。為什麼這樣切：ER3 併驗「未進入 Valet Mode」—— 只驗畫面關閉，一個關掉畫面卻已啟用之實作會通過（§7）。

### NR1L-UserProfiles-054 — SWE1-HMI-PROF-122（12.5）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Lock symbol shown with the Profile icon in Valet Mode |
| pre_conditions | 1. Valet Mode is not active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read the Profile icon in the status bar<br>2. Activate Valet Mode<br>3. Read the status bar and check that the lock symbol is combined with the Profile icon |
| expected_result | 1. The Profile icon is shown without a lock symbol<br>2. Valet Mode is active<br>3. The status bar shows a lock symbol combined with the Profile icon |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.5 |
| priority | **P2** — 狀態列之 Valet 指示；呈現層 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.5（PVAL5）—— Valet Mode 於狀態列以鎖頭圖示結合 Profile 圖示表示。關鍵情境條件：以啟用前之圖示為基準線（§5.6），否則「有鎖頭」與「本來就有」分不出。為什麼這樣切：狀態列之預設版面屬 12.1.1，本條只驗該指示。

### NR1L-UserProfiles-055 — SWE1-HMI-PROF-123（12.6）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile button in Valet Mode offers to deactivate |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the Profile button in the status bar<br>2. Read the popup and check that it offers to deactivate Valet Mode |
| expected_result | 1. The Profile button is pressed<br>2. A popup indicates “Function not available while in Valet Mode. Do you want to deactivate Valet Mode” |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.6 |
| priority | **P2** — Valet 中按 Profile 鍵之提示 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.6（PVAL6）—— Valet Mode 中按狀態列之 Profile 鍵時，以 popup 告知功能不可用並詢問是否停用。關鍵情境條件：popup 文字逐字取自條文，含其未加問號之原樣（§8.4.1）。為什麼這樣切：按下「是」之後續退出流程屬 12.3.1／12.9，本條只驗該提示。

### NR1L-UserProfiles-056 — SWE1-HMI-PROF-124（12.7）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Memory seat buttons move the seat without loading a Profile |
| pre_conditions | 1. The vehicle is equipped with memory seats<br>2. Driver Profile A is linked to memory seat 1 and its position differs from the current seat position<br>3. Valet Mode is active<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the active Profile and the seat position<br>2. Press the memory seat 1 button<br>3. Read the seat position and the active Profile and check that only the seat position changed |
| expected_result | 1. The active Profile is the Valet Mode Profile and the seat position is recorded<br>2. The memory seat 1 button is pressed<br>3. The seat moves to the memory seat 1 position and the active Profile is still the Valet Mode Profile |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.7 |
| priority | **P0** — **Valet 下不得載入車主 profile** —— 失效即隔離被繞過 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | **來源標示（J-12）**：`memory seat 1` 之編號為測試設置，條文只說 `the memory seat buttons` |

**reasoning**：驗證目標：12.7（PVAL7）—— Valet Mode 中按記憶座椅鍵只改座椅位置，不載入其所連之 Driver Profile。關鍵情境條件：pre-condition 要求該座椅所連 profile 之位置與現況不同，否則座椅有沒有動看不出來。為什麼這樣切：失效之後果是 **Valet 使用者載入了車主之 profile**，即隔離被繞過，故依 D-UP16-01 判 P0。

### NR1L-UserProfiles-057 — SWE1-HMI-PROF-125-01（12.8）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Device Manager locked out inside Media in Valet Mode |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the Media section<br>2. Select Device Manager<br>3. Read the screen and check that Device Manager is locked out |
| expected_result | 1. The Media section is available in Valet Mode<br>2. The Device Manager entry is greyed out<br>3. Device Manager cannot be opened |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8 |
| priority | **P1** — Valet 下之可用範圍限制（Device Manager） |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：12.8（PVAL8）之 Media 例外 —— Media 區可用，惟其中之 Device Manager 被鎖住。關鍵情境條件：ER1 併驗 Media 本身可用 —— **那是本條之對照組**（§7）：若整個 Media 都打不開，Device Manager 打不開就沒有意義。為什麼這樣切：037 為 12.8 切出四個 leaf，本條依其 description 之單位（Device Manager 之例外）生成；**該 leaf 之標題與描述錯位，見 A-UP11**。

### NR1L-UserProfiles-058 — SWE1-HMI-PROF-125-02（12.8）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Projection, native HFP and VR disabled in Valet Mode |
| pre_conditions | 1. A projection-capable device is connected to the head unit<br>2. Valet Mode is active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Attempt to start projection mode from the head unit<br>2. Attempt to place a call over native HFP<br>3. Press the voice recognition control<br>4. Open the Media section and check that it is available |
| expected_result | 1. Projection mode is disabled and does not start<br>2. Native HFP is disabled and no call is placed<br>3. Voice recognition is not active<br>4. The Media section is available |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8 |
| priority | **P1** — Valet 下之功能停用（Projection／HFP／VR） |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：12.8（PVAL8）—— Valet Mode 中 Projection、native HFP 停用，VR 不啟動。關鍵情境條件：三者為條文並列之停用項，同一條件下之三個結果，依 §5.7 併為一條 TC 之三條 ER。為什麼這樣切：**ER4 為 §7 之對照** —— 以「Media 仍可用」證明本條測到的是選擇性停用，而非整機不可用。**未另切負向 TC**：對照置於同一 TC（§5.6），理由見上繳 19 §6。

### NR1L-UserProfiles-059 — SWE1-HMI-PROF-125-03（12.8）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Status bar interaction limited to Valet Profile and HVAC |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press a status bar item other than Valet Profile or HVAC<br>2. Read the screen and check that the item does not respond<br>3. Press the HVAC icon in the status bar and check that it responds |
| expected_result | 1. The other status bar item is pressed<br>2. The item does not respond and no screen change occurs<br>3. The HVAC icon responds |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8 |
| priority | **P1** — Valet 下之狀態列互動限制 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：12.8（PVAL8）—— Valet Mode 中狀態列不可互動，**惟 Valet Profile 與 HVAC 圖示為例外**。關鍵情境條件：ER3 為 §7 之對照 —— 例外項須仍可用，否則「不可互動」與「整條狀態列壞掉」分不出。為什麼這樣切：本條依 037 之 description 生成（狀態列互動限制）；**該 leaf 之標題寫的是手套箱提示，與描述錯位，見 A-UP11**。

### NR1L-UserProfiles-060 — SWE1-HMI-PROF-125-04（12.8）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Non-interactable items greyed out in Valet Mode |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open a screen that contains locked-out items<br>2. Read the locked-out items and check that they are greyed out |
| expected_result | 1. The screen with locked-out items is displayed<br>2. All non-interactable items are greyed out |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8 |
| priority | **P2** — 不可互動項之變灰呈現 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.8（PVAL8）末句 —— 所有不可互動之項目一律變灰。關鍵情境條件：本條驗的是**呈現之一致性**，不是哪些項目被鎖（那屬 125-01～03）。為什麼這樣切：依 037 之 description 生成；**標題與描述錯位，見 A-UP11**。

### NR1L-UserProfiles-061 — SWE1-HMI-PROF-126-01（12.8.1）

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU0832 shown when prompting to enter Valet Mode |
| pre_conditions | 1. The vehicle is equipped with an electronic Glove Box Lock<br>2. Valet Mode is not active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Open the “All Profiles” tab and press the Valet Mode button<br>2. Read the prompt and check that PU0832 is displayed |
| expected_result | 1. The Valet Mode entry prompt is displayed<br>2. PU0832 informs the user that the glove box will be locked |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8.1 |
| priority | **P2** — 手套箱鎖之進入提示（PU0832） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.8.1（PVAL8.1）—— 配備電子手套箱鎖之車輛，在提示進入 Valet Mode 時顯示 PU0832。關鍵情境條件：車輛配置為條文明列之條件，列 pre-condition。為什麼這樣切：未配備手套箱鎖之車輛不顯示該提示，其對照未生成（取樣單位為 leaf，§8.4.2）。**本條依 037 之 description 生成；標題與描述錯位，見 A-UP11。**

### NR1L-UserProfiles-062 — SWE1-HMI-PROF-126-02（12.8.1）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Glove Box Lock button greyed out while Valet Mode is active |
| pre_conditions | 1. The vehicle is equipped with an electronic Glove Box Lock<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Read the Glove Box Lock button before Valet Mode is activated<br>2. Activate Valet Mode<br>3. Read the Glove Box Lock button and check that it is greyed out |
| expected_result | 1. The Glove Box Lock button is selectable<br>2. Valet Mode is active<br>3. The Glove Box Lock button is greyed out |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8.1 |
| priority | **P2** — 手套箱鎖按鈕之變灰 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.8.1（PVAL8.1）—— Valet Mode 啟用時手套箱鎖按鈕變灰。關鍵情境條件：以啟用前可選為基準線（§5.6）。為什麼這樣切：按下已變灰之按鈕之提示屬 126-03，本條只驗其變灰。**依 description 生成；標題與描述錯位，見 A-UP11。**

### NR1L-UserProfiles-063 — SWE1-HMI-PROF-126-03（12.8.1）

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU0833 shown when the greyed Glove Box Lock button is pressed |
| pre_conditions | 1. The vehicle is equipped with an electronic Glove Box Lock<br>2. Valet Mode is active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the greyed-out Glove Box Lock button<br>2. Read the screen and check that PU0833 is displayed |
| expected_result | 1. The press is not accepted and the glove box lock state does not change<br>2. PU0833 indicates that the function is not available while in Valet Mode |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8.1 |
| priority | **P2** — 按下已變灰之手套箱鎖按鈕之提示（PU0833） |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：12.8.1（PVAL8.1）末句 —— 按下已變灰之手套箱鎖按鈕時顯示 PU0833。關鍵情境條件：受測動作為對已變灰項目之按壓（§12 首匹配 → 負向測試）。為什麼這樣切：ER1 併驗「鎖定狀態未變」——只驗 popup 出現，一個顯示 popup 卻仍執行動作之實作會通過（§7）。

### NR1L-UserProfiles-064 — SWE1-HMI-PROF-127（12.8.2）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Glove box returns to its previous state after Valet Mode |
| pre_conditions | 1. The vehicle is equipped with an electronic Glove Box Lock<br>2. The glove box is unlocked<br>3. Valet Mode is not active<br>4. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Record the glove box lock state<br>2. Activate Valet Mode<br>3. Deactivate Valet Mode<br>4. Read the glove box lock state and check that it matches the state recorded in step 1 |
| expected_result | 1. The glove box is recorded as unlocked<br>2. Valet Mode is active and the glove box is locked<br>3. Valet Mode is deactivated<br>4. The glove box is unlocked again |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.8.2 |
| priority | **P1** — 手套箱狀態之還原；退出後之狀態接續 |
| design_method | 狀態轉換 (State Transition Testing) |
| remarks | （空） |

**reasoning**：驗證目標：12.8.2（PVAL8.2）—— 手套箱於退出 Valet Mode 後回到進入前之狀態。關鍵情境條件：pre-condition 取「未上鎖」，使 ER2 之「Valet 中變為上鎖」與 ER4 之「回到未上鎖」皆可觀察；若進入前即上鎖，整條 TC 之三個狀態相同，什麼都驗不到。為什麼這樣切：Valet Mode 啟用手套箱鎖之行為屬 12.8.1，本條驗其還原。

### NR1L-UserProfiles-065 — SWE1-HMI-PROF-128-02（12.9）

| 欄 | 值 |
|---|---|
| tc_title / test_item | PIN entry blocked during the 30-minute lockout |
| pre_conditions | 1. Valet Mode is active and a 4-digit PIN is set<br>2. The vehicle is stationary |
| input_test_data | PIN attempts: 10 incorrect attempts, then a further attempt |
| test_procedure | 1. Open the Valet Mode deactivation screen<br>2. Enter an incorrect 4-digit PIN ten times<br>3. Attempt to enter a PIN again immediately<br>4. Read the screen and check that the PIN entry is not accepted |
| expected_result | 1. The Valet Mode deactivation screen is displayed<br>2. The tenth incorrect attempt cancels the deactivation<br>3. A further PIN entry is attempted<br>4. The PIN entry is not accepted and Valet Mode is still active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.9 |
| priority | **P0** — 鎖定期間不得輸入 PIN —— 防暴力嘗試之機制本身 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | 鎖定期為 30 分鐘；本 TC 只驗**鎖定生效**（不需等待），屆滿後之回復屬 128-03（需 30 分鐘等待） |

**reasoning**：驗證目標：12.9（PVAL9）之鎖定側 —— 10 次錯誤後之 30 分鐘內不受理 PIN。關鍵情境條件：本條刻意只驗「立刻再試不受理」，**不涉時間長度**，故無須等待 30 分鐘；長度之驗證由 128-03 承擔。為什麼這樣切：第 10 次取消本身屬 pilot 之 TC-015（12.9），本條為其後之狀態。

### NR1L-UserProfiles-066 — SWE1-HMI-PROF-128-03（12.9）

| 欄 | 值 |
|---|---|
| tc_title / test_item | PIN entry restored after the 30-minute lockout elapses |
| pre_conditions | 1. Valet Mode is active and a 4-digit PIN is set<br>2. The vehicle is stationary and can remain powered for the duration of the test |
| input_test_data | Elapsed time after the tenth incorrect attempt: 29 min, 30 min |
| test_procedure | 1. Enter an incorrect 4-digit PIN ten times to trigger the lockout<br>2. Attempt a PIN entry after 29 minutes<br>3. Attempt a PIN entry after 30 minutes<br>4. Enter the correct PIN and check that Valet Mode is no longer active |
| expected_result | 1. The lockout is in effect after the tenth incorrect attempt<br>2. The PIN entry is not accepted at 29 minutes<br>3. The PIN entry is accepted at 30 minutes<br>4. Valet Mode is no longer active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.9 |
| priority | **P1** — 鎖定屆滿後之可用性回復 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| remarks | **執行成本：本 TC 需 30 分鐘等待**（J-8：照寫、不縮時、不刪除）。縮時屬測試實作之手段（bench 上如何撥時鐘），非 TC 內容之決定；排程時須計入。 |

**reasoning**：驗證目標：12.9（PVAL9）末句 —— 30 分鐘後可再試。關鍵情境條件：以 29 分（仍鎖定）與 30 分（可再試）構成邊界前後（§5.6）。**來源標示（J-4）**：ER2「29 分鐘時仍不受理」之權威為 **§5.6 之 BVA 界前基準線**，非條文 —— 12.9 只寫「30 分鐘後可再試」。為什麼這樣切：鎖定之生效屬 128-02，本條驗其屆滿與計數重置（ER4 以正確 PIN 成功退出證明計數已重置）。

### NR1L-UserProfiles-067 — SWE1-HMI-PROF-129（12.10）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Go button greyed out until four digits are entered |
| pre_conditions | 1. The Valet Mode PIN entry popup is displayed<br>2. The vehicle is stationary |
| input_test_data | PIN digits entered: 3, then 4 |
| test_procedure | 1. Enter three digits and read the Go button<br>2. Press the Go button while it is greyed out<br>3. Read the screen and check the tone and the popup<br>4. Enter a fourth digit and read the Go button |
| expected_result | 1. The Go button is greyed out with three digits entered<br>2. The press is not accepted<br>3. A Bonk tone is played and the popup “PIN must be 4 digits” is displayed<br>4. The Go button is available with four digits entered |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.10 |
| priority | **P2** — Go 鍵之可用性與其提示 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：12.10（PVAL10）—— 未滿 4 碼前 Go 鍵變灰；此時按下播 Bonk 並顯示指定 popup。關鍵情境條件：ER4 為對照 —— 輸滿 4 碼後 Go 須可用，否則「未滿時變灰」與「永遠變灰」分不出（§7）。**來源標示（J-12）**：3 碼為測試設置（條文只說「未滿 4 碼」）。為什麼這樣切：兩個結果同屬「未滿 4 碼」此一條件，依 §5.7 併為一條。

### NR1L-UserProfiles-068 — SWE1-HMI-PROF-130（12.10.1）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Numeric buttons greyed out once four digits are entered |
| pre_conditions | 1. The Valet Mode PIN entry popup is displayed<br>2. The vehicle is stationary |
| input_test_data | PIN digits entered: 4 |
| test_procedure | 1. Enter three digits and read the numeric buttons<br>2. Enter a fourth digit<br>3. Read the numeric buttons and check that they are greyed out |
| expected_result | 1. The numeric buttons are available with three digits entered<br>2. The fourth digit is entered<br>3. All numeric buttons are greyed out |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.10.1 |
| priority | **P3** — 輸滿 4 碼後數字鍵變灰 —— 呈現細節 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：12.10.1（PVAL10.1）—— 輸滿 4 碼後所有數字鍵變灰。關鍵情境條件：以 3 碼時可用為基準線（§5.6）。**來源標示（J-12）**：3 碼為測試設置。為什麼這樣切：Go 鍵之可用性屬 12.10，本條只管數字鍵。

### NR1L-UserProfiles-069 — SWE1-HMI-PROF-131（13.1）

| 欄 | 值 |
|---|---|
| tc_title / test_item | SPAAK key activates Valet Mode without a PIN |
| pre_conditions | 1. A SPAAK key with Valet Mode permissions is available<br>2. Valet Mode is not active<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Present the SPAAK key with Valet Mode permissions to the vehicle<br>2. Read the screen and check that Valet Mode is active without a PIN entry |
| expected_result | 1. The SPAAK key with Valet Mode permissions is detected<br>2. Valet Mode is active and no PIN entry was requested |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_13.1 |
| priority | **P0** — SPAAK 之自動啟用（免 PIN）—— Valet 進出 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：13.1（PVALSPK1）—— SPAAK 啟用之 Valet Mode 不需 PIN，偵測到具 Valet 權限之 SPAAK 鑰匙時自動啟用。關鍵情境條件：ER2 明寫「未要求 PIN」——只驗「已啟用」，一個仍要求 PIN 之實作也會通過。為什麼這樣切：SPAAK 下之退出限制屬 13.2，提示屬 13.3。

### NR1L-UserProfiles-070 — SWE1-HMI-PROF-132-01（13.2）

| 欄 | 值 |
|---|---|
| tc_title / test_item | All head unit Valet exit paths blocked for the SPAAK user |
| pre_conditions | 1. Valet Mode is active under the SPAAK scenario<br>2. The user at the head unit is the SPAAK user<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the Valet Profile icon in the status bar<br>2. Open the “All Profiles” tab and look for a deactivation control<br>3. Read the screen and check that no head unit path exits Valet Mode |
| expected_result | 1. The Valet Profile icon does not open a deactivation flow<br>2. No deactivation control is available on the “All Profiles” tab<br>3. Valet Mode is still active and any popup that would allow an exit is blocked |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_13.2 |
| priority | **P0** — SPAAK 下主機退出之全面阻擋 —— 隔離被繞過即失效 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | sibling 軸：本條驗**主機各入口皆被阻擋**（窮舉入口）；pilot 之 TC-016 驗**車主遠端停用可行**（同節之另一 leaf） |

**reasoning**：驗證目標：13.2（PVALSPK2）之阻擋側 —— SPAAK 使用者無法自主機退出。關鍵情境條件：本條之單位是「**所有**主機路徑」，故步驟逐一走過狀態列圖示與 All Profiles 分頁兩個入口。為什麼這樣切：037 為 13.2 切出兩個 leaf —— 本條（阻擋）與 pilot 之 132-02（車主遠端停用）；一葉一 TC（§8.2.1）。刻意略過：**入口之窮舉不可能完備** —— 取兩個最可能者，已具名。

### NR1L-UserProfiles-071 — SWE1-HMI-PROF-133（13.3）

| 欄 | 值 |
|---|---|
| tc_title / test_item | PU1573 shown when the SPAAK user presses the locked icon |
| pre_conditions | 1. Valet Mode is active under the SPAAK scenario<br>2. The user at the head unit is the SPAAK user<br>3. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Press the Profiles icon with the lock in the status bar<br>2. Read the screen and check that PU1573 is displayed |
| expected_result | 1. The Profiles icon with the lock is pressed<br>2. PU1573 is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_13.3 |
| priority | **P2** — SPAAK 下按 Profile 圖示之提示（PU1573） |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | （空） |

**reasoning**：驗證目標：13.3（PVALSPK3）—— SPAAK 使用者按下帶鎖之 Profiles 圖示時顯示 PU1573。關鍵情境條件：帶鎖之圖示即 12.5 所述之呈現，本條以其為操作對象。為什麼這樣切：非 SPAAK 情境下按同一圖示之行為屬 12.6（PU 不同），兩者之 pre-condition 互斥。刻意略過：PU1573 之內文未載於 spec，本 TC 只驗其顯示（同 R-U27 之處置）。

### NR1L-UserProfiles-072 — SWE1-HMI-PROF-134（14.1）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet welcome popup indicates Valet Mode with an exit button |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary |
| input_test_data | NA |
| test_procedure | 1. Trigger the welcome popup<br>2. Read the popup and check its Valet indication and button<br>3. Press the “Exit Valet Mode” button and check that the PIN entry for deactivation is displayed |
| expected_result | 1. The welcome popup is displayed<br>2. The popup indicates that the vehicle is in Valet mode and shows a button to deactivate it<br>3. The 4 digit PIN entry for deactivating Valet Mode is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_14.1<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.3.1 |
| priority | **P1** — Valet welcome popup 之內容與退出入口 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| remarks | 條文之「the Exit Valet Mode process **above**」其指涉對象**不在 ch14**（ch14 僅 14.1／14.2，本節即首條）—— 複位後為 12.3.1（同一 PIN 退出）與 12.6（停用詢問），故併列該二節。見上繳 19 §4 |

**reasoning**：驗證目標：14.1（PVALEX1）—— Valet Mode 中之 welcome popup 須指出車輛處於 Valet Mode 並提供停用按鈕，按下後進入退出流程。關鍵情境條件：ER3 之「退出流程」以 12.3.1 之 PIN 輸入為其可觀察形態；**該指涉之複位為本輪之查證結果**（R-U51 之判讀首次受檢）。為什麼這樣切：狀態列圖示亦可觸發同一流程（條文並列），本 TC 取 popup 之按鈕一側；圖示側之觸發屬 12.6 之 leaf。

### NR1L-UserProfiles-073 — SWE1-HMI-PROF-135（14.2）

| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode cannot be deactivated while the vehicle moves |
| pre_conditions | 1. Valet Mode is active<br>2. The vehicle is stationary on a test track and can be brought into motion |
| input_test_data | NA |
| test_procedure | 1. Bring the vehicle into motion<br>2. Attempt to access the Profile section<br>3. Read the screen and check that the unavailability popup is displayed and Valet Mode is still active |
| expected_result | 1. The vehicle is in motion<br>2. The Profile section is not accessible<br>3. PU0394 is displayed and Valet Mode is still active |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_14.2 |
| priority | **P0** — **行車中不得停用** —— 失效即 Valet 可於行進中被解除 |
| design_method | 負向測試 (Negative / Invalid) |
| remarks | （空） |

**reasoning**：驗證目標：14.2（PVALEX2）—— 行車中不得停用 Valet Mode；行車中嘗試進入 Profile 區時顯示 PU0394。關鍵情境條件：受測動作為行進中之停用嘗試，屬不被允許之操作（§12 首匹配 → 負向測試）。為什麼這樣切：ER3 併驗「Valet Mode 仍啟用」——只驗 popup 出現，一個顯示 popup 卻仍解除之實作會通過（§7）。**本條之失效後果為行進中 Valet 可被解除** —— R-U5 之 rubric 無安全帶，依 D-UP16-01 就近判 P0，見上繳 19 §7。

