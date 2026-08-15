# 21 — Comfort HMI / R-C32、locate 移除、批次 3：Front Climate Anatomy

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 32
- 結果：批次 3 生成 **9 條**（2.2 ×8、6.3 ×1），tc_id **-032 … -040**。
  **2.1（3 leaf）與 2.14（4 leaf）停下回報 —— 配置軸不在十一軸內。**
  lint **37/37 PASS，0 finding，40 條**。**未寫回 workbook。**

---

## 1. 下放包 §5 之 Layer 3 清單與 leaf 數不一致 —— 依 framework.md 取 16

| 來源 | Layer 3 | leaf |
|---|---|---|
| 下放包 32 §5 之表 | 2.1、2.2、6.3 | 16 |
| 上表逐節相加（`layer3_map.tsv`）| 2.1(3) ＋ 2.2(8) ＋ 6.3(1) | **12** |
| `framework.md` 第 39 行（Part N 第 1 組）| 2.1、2.2、**2.14**、6.3 | **16** |

**取 framework.md**，理由有三：leaf 數 16 與之相符；下放包 §5 自身要求處理
**2.14** 之 ICS 邊界（若不在範圍內則無此要求）；`2.14` 於 Part N 修正案
（14 §1.2）即由 `Climate Modes` 改置本組，該改置正是 4 leaf 之來源。

037 實測：`SWE1-HVAC-001`(3) ＋ `-002`(8) ＋ `-020`(4) ＋ `-027`(1) = **16**，
與 framework.md 相符。

**下放包之 Layer 3 欄漏列 2.14**，不影響作業（16 這個數字與 §5 之要求
把它帶回來了），但兩處若都漏列，本批就會少做 4 個 leaf 而數字看起來仍對。

---

## 2. 生成之 9 條

| tc_id | req_id | 節 | tc_title | 步/ER | design_method |
|---|---|---|---|---|---|
| -032 | 002-01 | 2.2 | Hard control and touchscreen changes mirror each other | 3/3 | 功能測試 |
| -033 | 002-02 | 2.2 | Pop-up appears off the climate screen and times out | 3/3 | 狀態轉換 |
| -034 | 002-03 | 2.2 | Status bar and category button indicator follow the change | 3/3 | 功能測試 |
| -035 | 002-04 | 2.2 | Sync suppresses the passenger side slider pop-up | 2/2 | 功能測試 |
| -036 | 002-05 | 2.2 | ATC pop-up shows the degree with unit-dependent half degrees | 5/5 | 決策表 |
| -037 | 002-06 | 2.2 | MTC pop-up shows a slider bar with the arrow at the setting | 3/3 | 功能測試 |
| -038 | 002-07 | 2.2 | On the climate screen no status bar pop-up is shown | 3/3 | 功能測試 |
| -039 | 002-08 | 2.2 | Hard control LEDs follow a change made on the climate screen | 3/3 | 功能測試 |
| -040 | 027 | 6.3 | Comfort section is removed from the head unit except popups | 3/3 | 功能測試 |

9 leaf → 9 TC，無拆無併。

---

## 3. 停下回報 —— 2.1（3 leaf）與 2.14（4 leaf）

### 3.1 `2.1`（`SWE1-HVAC-001`）—— **兩層問題，第一層比軸更前面**

條文：

> R1C1.) The comfort category will have **up to 4 tabs depending on vehicle
> configuration**. Tabs are displayed in the following order: Front, Seats
> (WS or R1 Low) or Seat & Wheel (Maserati), Massage, Rear. **If only Front
> climate is available in a specific vehicle the tabs will not be displayed.**
> Refer to separate HMI Logic and Flow documentation for Massage Seats logic.

**第一層：條文未述何種配置產生何種 tab。** `-01`（幾個 tab）與 `-02`
（顯示順序）之 TC 必須先能設定出一個已知的 tab 集合，而條文只說
「depending on vehicle configuration」，**沒有說 depending on what**。
依 R-C28 第一問，任何「本車配備 rear climate／massage seats」之 PC
在 2.1 之 full_text 都找不到明文對應 —— 這是造值，不是軸的問題。

**第二層：`-03` 之條件是條文明文，但不是軸。**
`only Front climate is available` 逐字在條文內（第一問通過），
但它不在 profile §3.2 之十一軸內 → 依 28 §2.1(b) 停下，不自行增軸。

### 3.2 `2.1` 之 leaf 與條文數字不符 —— 併此回報，不自行取捨

| | 說 |
|---|---|
| 條文（`section_fulltext.tsv`，SYS1 export）| **up to 4 tabs**；順序 Front, Seats (WS or R1 Low) or Seat & Wheel (Maserati), **Massage**, Rear |
| 037 leaf `-01` | **up to 3 tabs** |
| 037 leaf `-02` | 順序 Front, Seats, Rear（**無 Massage**）|

037 之兩個 leaf **系統性地少了 Massage tab**。

依 §8.6（source spec wins over index export）條文應勝，但**037 不是 index
export，它是 SWE.1 之分析報告**，而 R-C1 所定之驗證單位正是 037 之 leaf。
**兩者衝突時該以何者為準，現行條文未涵蓋** —— §8.6 管的是 spec 與其索引，
不是 spec 與上游分析。

**我不自行取捨**，因為兩種取法會產生不同的 TC 數與不同的 test_item：
取條文則須驗 4 個 tab 含 Massage，取 leaf 則 3 個。登為 **A-CF21**（見 §5），
與軸的問題一併待裁。

**條文自身另有一句指向委派**：`Refer to separate HMI Logic and Flow
documentation for Massage Seats logic` —— Massage 之**邏輯**確實委派他處，
但 tab **是否存在**是 2.1 自己說的。委派的是行為，不是存在。

### 3.3 `2.14`（`SWE1-HVAC-020`）—— 三個條件，皆不在十一軸內

> C15.) MTC screens/popups are to be used when CCM relays MTC functionality.
> … **For MTC with ICS**, there will be no redundant interaction with the
> screen for certain types of physical knobs (**3 knob HVAC controls**) …
> In these cases, no HVAC menu bar icons, no HVAC screens and no HVAC pop ups
> will be displayed. **For one zone MTC with push button TEMPERATURE** and
> hard controls that would not create a mismatch … this exception does not
> apply.

| 條件 | 是否在十一軸內 |
|---|---|
| ATC／MTC | **是**（第一軸）|
| 單區 | **是**（第二軸）|
| **ICS 之有無（於 ch2）** | **否** —— profile 之市場／變體軸為 `EMEA ICS`，且**範圍寫明 ch16 全章**；2.14 在 ch2 |
| **3 旋鈕 HVAC 實體控制** | **否** |
| **push button TEMPERATURE** | **否** |

三者皆為條文明文（第一問可通過），但皆不在十一軸內 → 停下。

### 3.4 §8.2.1 之 ICS 邊界 —— 依下放包要求先具名，供裁定後直接使用

即使本輪未生成，邊界已判定並記此：

**2.14 之 TC 若生成，只驗「不顯示」此一事實** ——
`no HVAC menu bar icons, no HVAC screens and no HVAC pop ups will be
displayed`，此為 2.14 自身之明文。

**不驗 ICS 自身之行為**：三旋鈕如何運作、ICS 之畫面長什麼樣、ICS 之
climate 功能如何操作，皆屬 `ICS Anatomy`（16.2／16.14／16.16）與
`ICS Climate Modes`（16.3 等）—— **不同 Test Set，§8.2.1 不得擴張**。

判別方式：本節之可觀察量是**HMI 之缺席**，ICS 章之可觀察量是**ICS 之行為**。
前者在 head unit 上看，後者在 ICS 上看，**觀察位置不同**。

### 3.5 我未做的事

- 未自行增軸（三個候選軸皆未加）
- 未把 `EMEA ICS` 軸之範圍由 ch16 擴大到 ch2 —— 那是改寫既有軸之定義，
  比新增一個軸更難察覺
- 未在 2.1 之條文與 037 leaf 之間自行取捨
- 未標 `[BLOCKED-SPEC]` —— 同批次 2 之理由：本案非委派，是 profile 未涵蓋
- 未產生任何列（R-C16）

---

## 4. 兩個判斷須說明，因為它們是我自己決定不停下的

### 4.1 `2.2` 之硬鍵存在 —— 判為執行前提，非配置軸

`-032`…`-039` 之 PC 第 1 行為
`[spec-derived] The vehicle has climate hard controls and a climate
touchscreen (2.2)`，具名之句為
`Whenever changes to the climate system are made via hard controls or
touchscreen`。

**依 R-C31 第一問通過**（操作對象之存在為句子之執行前提）。

**判為非配置軸之理由，我用了一個可機械檢查的判別**：

> **條文有無「On vehicles with X」型選擇子。**
> 3.1「**On vehicles with** Tri-Mode climate」、3.2「**On vehicles with**
> MAX DEF」、3.4「**For soft top vehicles such as** JL/JT」、
> 6.3「**When a vehicle is configured with** a non-foldable secondary lower
> screen」—— 四者皆有，且四者皆對應一個軸。
> **2.2 沒有。** 它整節都在講硬鍵與觸控之互相反映，硬鍵是**主詞**，
> 不是在兩種行為之間做選擇的**變數**。

**若分析層認為此判別不成立**，則 `2.2` 全部 8 條須退回待「climate 硬鍵
有無」之軸裁定 —— 那會使本批只剩 `-040` 一條。**這是本包最大的單點風險**，
故把判別寫成可反駁的形式而非只寫結論。

### 4.2 `-037` 之「if the MTC has a Climate screen」—— 照錄為 PC，未升格為軸

該限定語逐字在 2.2 內（`for MTC (if the MTC has a Climate screen)`），
第一問通過。我**未**停下，理由：ATC／MTC 已是第一軸，此語為該軸 MTC 側之
**條文自身限定**，非新維度。

**但它確實描述了一種裝備差異**（有 Climate screen 的 MTC vs 沒有的）。
若分析層判其為第十二軸，`-037` 一條須退回。列此待裁。

---

## 5. R-C32、`locate` 移除、A-CF20、A-CF21

### 5.1 R-C32 貼入

`RULINGS.md` 現有 **34 個**逐字條文區塊。前附來源說明，指向上繳 20 §4.3
—— 我當時自陳逾越授權，覆核追認並立為通則。

### 5.2 `forbidden-verb` 移除 `locate`

**移除屬實，且我原本的理由確實錯了**：canon §5.6 之**正面示例**就是
`Locate the phone and record its A2DP and HFP status shown in the list`。
我以一次手查時的主觀不適，在 gate 裡固化了一個 canon 推薦寫法之禁令。

**順帶修正一處我沒注意到的計數問題**：移除 `locate` 後詞表剩 **8 項**，
而下放包說「回到 §5.1 之**九詞**」。差異來自 §5.1 之
`observe whether` 被 `observe` 這個 matcher 吸收。

功能上等價，**但一份與其權威來源逐項對不起來的清單無法被查核**，
故補回 `observe whether` 使其為九項，並改為**長詞優先**排序，
讓回報之詞組為最完整者（`check whether` 而非 `check`）。

**反向驗證（九詞逐一 ＋ 三項放行）**：

| 注入行首 | 結果 |
|---|---|
| `observe whether` / `observe` / `see if` / `check whether` / `confirm whether` / `verify` / `watch` / `monitor` / `inspect` | **九項全數命中**，回報之詞組為最長匹配 |
| `Locate the phone and record its status` | **放行**（§5.6 正面示例）|
| `Read the label to verify that it changed` | **放行**（§5.1 目的子句例外）|
| `Record the current fan speed` | **放行**（§5.1 偏好動詞）|

本批 40 條無任何步驟使用該九詞，移除與補回皆不改變現有結果。

### 5.3 `RUNBOOK.md` 兩則

**（a）逾越授權：可以做，但回報是它成立的條件。** 含 R-C32 之判別
（改判後之 gate 於裁定不成立之情形仍須 FAIL）與「放寬 vs 改判」之兩路對照。

**（b）gate 的詞表：canon 以外的項須具名授權，手查習慣不算。**
末句：**這跟 R-C26（豁免不可自取）是同一件事的另一面 —— 禁令同樣不可自取。**

### 5.4 A-CF20（維持）

`SWE1-HVAC-024-07` 拆後四條之 ER 逐字相同，登為已知性質。條目寫明其
登記目的：**供日後只掃 ER 欄之審閱者查考** —— 四列一模一樣在工作簿內
看起來像複製貼上的疏漏，實際是條文的形狀。

**登記過程再次由 gate 觸發**：貼完 R-C32 跑 lint，`anomaly-id-registered`
指名 A-CF20 未登記、首見於 `docs/handoff/32_rc32_batch3.md`。
連續第二包由它先開口。

### 5.5 A-CF21（新登，本包產生）

`2.1` 之 037 leaf 與條文之數字不符（3 tabs vs 4 tabs；順序缺 Massage），
且**現行條文未涵蓋「037 leaf 與 spec 條文衝突時以何者為準」**。
狀態 OPEN，阻塞 `SWE1-HVAC-001` 之 3 個 leaf，列 RD-1 候選。

---

## 6. lint

```
37 / 37 gates PASS; 0 finding(s) across 40 TCs
```

`tc_id` 001–040 連號無缺（實測）。三個 generator 連續重跑，輸出不變。

---

## 7. §9 self-check 17 項 —— 依 R-C23，僅列批次 3 之 9 條

| # | 項目 | 判 | 獨立依據（非 lint 覆述）|
|---|---|---|---|
| 1 | Test Set 與 framework 相符 | PASS | `test_set` 皆 `Front Climate Anatomy`，與 `framework.md` 第 39 行第 1 組名稱逐字元相同 |
| 2 | tc_title 形狀／字數／sibling token／無 modal | PASS | 字數實測 7–12（皆在 2–14）。sibling token：`mirror each other`／`times out`／`status bar`／`Sync`／`ATC`／`MTC`／`no status bar pop-up`／`LEDs`／`removed`，九者互斥 |
| 3 | PC 僅 state/env 且為 spec trigger | PASS | 9 條共 **13 行 PC**，全為裝備或系統類型（硬鍵＋觸控／ATC／MTC／MTC 有 Climate screen／乘客側溫控／secondary lower screen）。實測 PC 內無 `Press`／`Open`／`Change`／`Set`／`Turn`／`Adjust`／`Read` → **0 命中**。在／不在 climate screen 為步驟建立者，落 procedure |
| 4 | Input Test Data 欄位歸屬 | PASS | 9 條相異值僅 `{"NA"}`。`-036` 之攝氏／華氏為**單位設定**，由步驟 2／4 建立，非輸入資料 |
| 5 | 步驟可執行、無禁用動詞 | PASS | 首字動詞實測 `Adjust`／`Change`／`Continue`／`Do`／`Open`／`Read`／`Set`／`Turn` 八個，無一在 §5.1 九詞內。**本項現有 `forbidden-verb` gate，故依 R-C23 另補**：逐條讀 9 條之步驟，每步皆為單一具體操作，無「執行後自行判斷」型指示 |
| 6 | 步驟長度與意圖層級 | PASS | 步數 2／3×7／5。最長者 `-036` 之 5 步為攝氏、華氏兩輪，非贅步 |
| 7 | 標準 setup 片段逐字重用 | **N/A** | `PC_CONTROLS`／`PC_ATC`／`PC_MTC` 為生成器常數，**同節內逐字重用，跨節不套用**。`-040` 之 PC 獨立撰寫，未沿用 13.x 之措辭（見第 17 項）|
| 8 | CLI／tooling 步驟格式 | **N/A** | 9 條皆 HMI 操作 |
| 9 | 需要前後對照時有基線步驟 | PASS | 9 條之 ER 第 1 行皆為前置狀態之確認（`The climate screen is displayed`／`is not displayed`／`Sync is on`／`The head unit menu is displayed`），使「不在 climate screen」這類條件於判讀時可證確已成立 |
| 10 | procedure↔ER 1:1、ER 可觀察、無 modal | PASS | **依 R-C23 明說：本項依據不是 `er-subject-net`**，該 gate 為補網。逐行讀 **28 行 ER**，主詞為 `The climate screen`／`The fan speed`／`A fan speed pop-up`／`The status bar`／`The status indicator`／`No slider pop-up`／`A pop-up`／`The arrow`／`The LEDs`／`The comfort section`／`Sync`／`The temperature unit` —— **皆系統側之物，無一以觀察者為主詞** |
| 11 | 無 FP／FF；supported 配 negative | PASS | FF：在／不在 climate screen、Sync 開啟、單位設定皆由步驟建立。negative：`-033`（不在 climate screen → **顯示** popup）與 `-038`（在 climate screen → 狀態列**不顯示** popup）成對；`-035` 為 Sync 下之抑制，其正向對照（未 Sync 時是否顯示）**條文未述，故未作反向配對**（§7 之配對須條文支撐）|
| 12 | 溯源、§8.2.1、§8.2.2、無造值 | PASS | 溯源：9 條之 `req_id` 於 037 逐一存在。**§8.2.1 為本批之重點**：2.14 之 ICS 行為（§3.4）與 6.3 之 popup 觸發規則（屬 2.2／ch14）皆具名且未驗。§8.2.2：9 個 leaf 各為單一行為。造值：`3 sec` 為條文明載故照用；`comfort section` 之子項條文未列舉，故 ER 以該詞本身判定而不列舉 |
| 13 | design_method 於 procedure 定案後指派 | PASS | 分布 功能測試 ×7、狀態轉換 ×1（`-033`，逾時遷移）、決策表 ×1（`-036`，ATC × 單位兩條件）。可由 procedure 形狀反推 |
| 14 | 四長欄無行尾句點 | PASS | lint `trailing-period` 覆蓋；**另查其未涵蓋之 `test_item`**：9 條逐條確認無行尾句點 |
| 15 | UI 標籤用 `"..."` | PASS | 本批**無一處加引號**，因為 9 條之操作對象皆為**元件類名**（fan speed hard control／temperature hard control／climate screen／status bar／category button／driver temperature slider），**非螢幕上的字串標籤**。加引號即宣稱那就是螢幕上的字 —— 同 `-031` 之 `rear defrost button` 之判斷 |
| 16 | `specification_reference` 涵蓋所有直接驗證之節 | PASS | 9 條各列單節（`2.2` ×8、`6.3` ×1），**本批無跨節 PC**，故 R-C29 之義務一不觸發。此與批次 2 之 `-029`／`-030` 相反，值得對照 |
| 17 | 來源 spec 勝過 index export | PASS | 條文一律讀 `section_fulltext.tsv`。**`-040` 之第一問具名 6.3 自身之句**（`When a vehicle is configured with a non-foldable secondary lower screen that contains comfort information`），**未引 13.x** —— 實測 6.3 之 reasoning 內無任何 `13.` 之引用。§8.6 之衝突見 §3.2 之 A-CF21，該項**已停下未取捨** |

**15 PASS、2 N/A。**

---

## 8. 未寫回

依 32 §6 第 6 項，**未寫回**。`output/` 仍 2 檔，`write_back.py` 未執行，
`DELIVERY.sha256` 未增列。

**寫回節奏（32 §7）待 Pei 裁定。** 執行層之補充事實，供裁量：
若採每批寫回，本批之 9 條**不含多節 spec_ref**（§7 第 16 項），
故**測不到 A-CF19**；A-CF19 之待測項在批次 2 之 `-029`／`-030`。
換言之「每批寫回」要解 A-CF19，得從**批次 2**那一批寫起，不是從本批。

---

## 9. 進度

| | 數 |
|---|---|
| 驗證單位（leaf）| 403 |
| 已生成（leaf）| **37** |
| 已生成（TC）| **40** |
| 本批停下待裁（leaf）| 7 |
| 未開始（leaf）| 359 |

Test Set 完成狀況：`Tri-Mode Climate` 14/14；`Seat Control Tab` 14/14；
`Front Climate Anatomy` **9/16**。

---

## 10. 「本包是否仍有該驗而未驗者」

依 R-C30，陰性陳述附搜尋範圍。

1. **§4.1 之「On vehicles with X」判別是我立的，不是條文立的。**
   我用四個正例（3.1／3.2／3.4／6.3）歸納它，**未對 129 節全掃驗證該判別
   是否普遍成立**。
   **搜尋範圍**：僅上述四節 ＋ 2.2。若某節有選擇子而其條件不是軸、或
   無選擇子卻確實需要軸，本判別即失效。**這是本包最需要被檢驗的一句話。**
2. **`-032` 與 `-039` 之界線是我畫的。** 條文首句（改變反映於兩處）與末句
   （climate screen 之改變反映於 LED）在行為上重疊；037 給了兩個 leaf。
   我讓 `-032` 用「硬控之指示」、`-039` 用「LED」以區分，**但條文沒有說
   這兩者是不同的東西**。若它們是同一件事，兩條之區別即為我造的。
3. **`-035` 之 ER 只有否定項**（`No slider pop-up is shown on the passenger
   side`）。條文未述 Sync 時駕駛側是否顯示 popup，故未寫；
   **一條只驗「沒有發生什麼」的 TC，其 pass 也可能來自功能整個壞掉。**
   ER1（`Sync is on`）提供了部分保護，但不完整。
4. **`-040` 之步驟 3 觸發 comfort popup 以驗證「除外」。**
   popup 之觸發機制屬 2.2，我把它當成步驟而非驗證對象，reasoning 已具名。
   **但這一步是否已構成 §8.2.1 之擴張，我判為否，該判斷可被推翻。**
5. **2.14 之四個 leaf 我讀了條文但未逐 leaf 判定其可測性** ——
   停在軸的問題就停下了。裁定後仍需逐 leaf 走一次。

---

## 11. 建議 commit message（git 未執行）

```
feat(comfort): batch 3 — Front Climate Anatomy, 9 of 16 leaves

- add R-C32 (re-judge a gate the ruling broke, never relax it) to RULINGS
- forbidden-verb: drop `locate` (canon 5.6 uses it in a positive example),
  restore `observe whether` so the list maps one-for-one onto 5.1, and
  match longest-first so the reported phrase is the fullest one
- RUNBOOK: overstepping must be reported; a gate's word list needs a cited
  authority, and a habit from hand-checking is not one
- generate 2.2 (8) and 6.3 (1), tc_id -032..-040
- withhold 2.1 (3) and 2.14 (4): their configuration axes are not among the
  eleven, and 2.1's leaves also disagree with the clause on tab count
- register A-CF20 (identical ERs after the split) and A-CF21 (leaf vs
  clause conflict at 2.1)
- lint 37/37 PASS, 0 findings across 40 TCs
```

---

## 12. 待分析層

1. **§4.1 之判別**（有無「On vehicles with X」選擇子）—— 若不成立，
   本批 8 條須退回。
2. **§4.2** —— `MTC has a Climate screen` 是否為第十二軸。
3. **§3 之三個軸**（Front-only climate／ICS 於 ch2／3 旋鈕 HVAC ＋
   push button TEMPERATURE）。
4. **A-CF21** —— 037 leaf 與 spec 條文衝突時以何者為準（現行條文未涵蓋）。
