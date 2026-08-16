# 28 — Comfort HMI / 移除 6 條、`-036` 拆二、第十五軸、批次 5

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 39
- 結果：6 條之 EMEA 排除式 PC 已移除（含 `-036` 拆出之華氏條）；
  **第十五軸判為「一軸、功能型」並附依據**；批次 5 生成 **14 條**，
  `SWE1-HVAC-044-02` 停下（R-C26）。候選產生器之同義正規化**證實有效** ——
  它現在抓得到先前漏掉的那一對。lint **41/41 PASS，80 條**。**未寫回。**

---

## 1. 移除 6 條 ＋ `-036` 拆二

### 1.1 移除以 `req_id` 為粒度，不以節為粒度

同一節內有的條保留、有的移除，故改以 `EMEA_REMOVED_REQ_IDS` 實作：

| 節 | 移除 | 保留 | 依據 |
|---|---|---|---|
| 2.14 | `020-03`／`020-04`（3 條）| `020-01`／`020-02` | ICE13 全文**僅兩句**，不含 C15 之 3 旋鈕 ICS 段落；而 -01／-02 之「MTC 無離散溫度／無 Auto」正落在其第二句內 |
| 2.16 | `022-02` | `022-01` | 16.17 全文**僅一句**，不含 C18 之第二句（回復前一風速）|
| 2.7.1 | `011` | —— | ICE6 只列 `Fan ranges: Off, 1-7` |
| 2.2 | 華氏條（新）| 攝氏條 | ICE1 有 `or half degree increments for Celsius`，**無** C1 之 `and for Fahrenheit do not show half degrees` |

`16.2` 引用一併移除。**實測：帶 EMEA PC 者 40 條、含 `16.2` 引用者 40 條**
—— 兩數相同，一對一無殘留。

`reasoning` 逐條記依據；`emea_ics_per_tc.tsv` 之 46 列保留（含 6 條已移除者），
**作為「為何移除」之紀錄**，非殘留 —— gate 只要求帶 PC 者有列，多列無害。

### 1.2 `-036` 拆為二條

依據為 **§8.3 之 input_data 軸**（非 EMEA 問題）：溫度單位兩值產生不同
預期結果且各自獨立可失效。`split_flag` 真、`split_reason` 具名該依據。

`design_method` 由**決策表改為功能測試**（拆後各為單一單位下之顯示檢查，
R-C19）。

| | tc_id | 單位 | EMEA |
|---|---|---|---|
| 攝氏 | `-036` | Metric | **維持** |
| 華氏 | `-037` | 非 Metric | **移除** |

### 1.3 新舊 `tc_id` 對照（拆分致後續順移 +1）

| 舊 | 新 | 說明 |
|---|---|---|
| `-001` … `-036` | 同 | 未動（`-036` 內容改為只驗攝氏側）|
| — | **`-037`** | **新增**，華氏條 |
| `-037` … `-065` | **`-038` … `-066`** | 全數 **+1** |
| — | `-067` … `-080` | 批次 5（新）|

**順移 30 條，全部僅編號改變、內容未動。** 凡以 tc_id 引用過 `-037` 以後
各條之既有文件（上繳 21～27），其引用自本包起失效；`req_id` 仍為穩定識別。

---

## 2. `RUNBOOK.md` 兩則

**（a）節級看開頭，TC 級看那一句**

> 節級 `mirrored` 之依據是「開頭一樣」，TC 級要問的是「這條所驗的那一句
> 在不在」。

附 16.14／16.17 之實例（首句相同而全文只有那一兩句），並記「逐條補答
45 條時，這句話值 6 條過嚴的排除式 PC」。

**（b）gate 的紅綠，對應「違規」而非「待裁」**

> gate 之紅綠應對應「是否違反已定之規則」，不對應「是否有待裁決之事」。
> 待裁事項以具名回報行呈現。
> **紅燈會製造壓力，而壓力會催生未經授權的處置。**

同源標註 R-C24（豁免須為具名回報行）。

---

## 3. 第十五軸 —— 判為**一軸、功能型**，依據逐項

### 3.1 一軸而非二軸

**判準**：兩性質須在條文自身之措辭中可各自獨立取值。

**實測**（ch10 全 10 節）：

| pattern | 命中 |
|---|---|
| `\bBEV\b` | 10.2 |
| `\bEV Vehicles?\b` | 10.1 |
| `ECO HVAC is equipped` | 10.9.1 |
| `\bconfigured\b` | **0** |
| `\bif\b.*\bECO\b` | **0** |

10.9.1 之 `When ECO HVAC is equipped on a vehicle` **係重述本章之適用範圍**
（其下半句即 `compared to the standard ICE AUTO pop up`，對照的是 ICE 車），
**未使「配備 ECO HVAC」成為可獨立取值之第二性質** —— 全章無任何條件句
使之與 EV/BEV 分離。

`AUTO ECO` 與 `AUTO ON` 之切換為**執行期狀態**（10.4／10.5 之按壓循環），
依 R-C28 第三問落 `test_procedure`。**→ 一軸。**

### 3.2 功能型而非介面型

**判準**：非 BEV 車輛是沒有這個**功能**，抑或有功能而無**介面**？

**條文自證**：10.5 之 `AUTO mode will only be broken by acting on other
buttons e.g. fan speed, airflow mode etc (**see standard ICE AUTO logics**)`；
10.9.1 之 `an additional info text **compared to the standard ICE AUTO pop
up**`。

**ICE 車上 AUTO 鍵、Menu Bar icon、comfort popup 皆存在** —— 缺的是
ECO 這組能力，不是承載它的介面。**→ 功能型。**

**與 EMEA ICS 形狀相似而類別相反**：ch16 是**另一套介面**實現同一批能力
（介面型）；ch10 是**多出來的一組能力**（功能型）。兩者皆為「整章繫於一個
車輛屬性」—— **不得以形狀類推（R-C18）**。下放包 §2 已預先警告此點，
而實測結果確與其「BEV-only 意味整章無介面」之預期相反。

**後果**：本軸不進 `interface_axis_review` 之鍵，**既有 66 條不需逐條補答**。

---

## 4. `-022` —— 分支二（明文無），不補不改

**實測**：ch10 全章掃 `MAX DEF`／`defrost`／`break`／`brakes`
—— **全部 0 命中**。

ch10 從未述及 MAX DEF，亦未述其 AUTO 行為與 3.2 所述有何不同。
依 39 §3 分支二：**不補 PC、不改 ER**，`reasoning` 已記
「ch10 未述其差異，故 3.2 之字面於 BEV 亦成立」。

**我上一包判「有影響」而本包判「不補」，兩者不衝突** —— 前者是實務上
「進入 AUTO」在 BEV 有三態而顯得不唯一，後者是**條文層面 ch10 未宣稱
任何差異**。裁定之判準是後者。實務上的不唯一仍在，列 §10 待裁。

---

## 5. 候選產生器 —— 標記取代排除 ＋ 同義正規化

### 5.1 兩項改造

- **高頻詞由排除改為標記**：`AUTO`／`FAN`／`HI`／`HVAC`／`LO`／`MODE`／
  `TEMPERATURE` 七詞不再逐出詞彙集，其候選改於輸出標 `high-frequency`。
  **排除是靜默的，標記是可見的。**
- **同義正規化**：等價組**自語料實測**而得（掃全 129 節之
  `MAX *`／`REAR *`／`FRONT *` 形態），得
  `MAX DEFROST → MAX DEF`、`REAR DEFROST → REAR DEF` 等。

### 5.2 修正證實有效 —— 它抓到先前漏掉的那一對

```
- 2.10  [Climate Modes] <-> 3.3  [Tri-Mode Climate]  ['MAX DEF']  sibling
```

**`2.10 ↔ 3.3` 上一包是人工補上的，產生器看不見；正規化後它自己產出了。**
這是修正之直接驗證 —— 不是「改了以後沒壞」，是**它抓到了那個當初讓我們
知道要改的實例**。

### 5.3 三組重跑之結果 —— 陳述依 §4.3 訂正

**舊陳述**「0 對」訂正為「**以當時之語彙集掃描得 0 對**」。新版結果：

| 組 | 舊 | 新 | 判定 |
|---|---|---|---|
| `Seat Control Tab` | 0 | **0** | 座椅控制之語彙與氣候章確無交集，**兩版皆 0** |
| `Tri-Mode Climate` | 14 | **45** | 全數判定（15 舊 ＋ 30 新）|
| `Front Climate Anatomy` | 0 | **19** | **舊版之 0 是排除清單造成的** |

**`Front Climate Anatomy` 由 0 變 19，正是上繳 27 §10.3 所預測者** ——
我當時寫「排除清單是為可讀性設的，不是為正確性設的，而它直接造成了那個
0」。改後即現形。

**49 對新候選全數為高頻詞單獨重疊**（`AUTO`／`HVAC`／`HI`／`MODE`），
逐項判 `not-sibling` 並入表，理由具名其為「39 §4.1 之標記取代排除而首次
出現」。**無一對有實質重疊** —— 即改造未帶來新的 sibling，
但它把「沒有」這件事從未知變成已檢視。

`data/pending_sibling.tsv` 現 **70 列**（5 `sibling`／65 `not-sibling`），
三組之 `reviewed_at` 皆為 **129**。

### 5.4 一對值得單記

`10.5 ↔ 3.2`（共有 `AUTO`）判 `not-sibling`，但其理由欄另註：
3.2 之「按 AUTO 中斷 MAX DEF」與 10.5 之 AUTO 狀態循環於 BEV 上語意相接
—— 即 §4 之 `-022` 問題。**判為非 sibling 而記其相接**，兩者不混。

---

## 6. 批次 5 `ECO HVAC` —— 生成 14 條，1 leaf 停下

### 6.1 範圍

`framework.md` 第 45 行：`10.1 ~ 10.9.1` / **15 leaves**；
037 實測 044(2)＋045…047(各1)＋048(3)＋049(2)＋050…052(各1)＋053(2) = **15**，相符。

tc_id **`-067` … `-080`**。

### 6.2 R-C34 之生成時義務

| 軸 | 判定 |
|---|---|
| 13（3 旋鈕 ICS）| 移除 HVAC 畫面／popup → **14 條全補** |
| **EMEA ICS** | **不補** —— ch16 十八節無 ECO HVAC 之對應節，`ch16_mirror_map.tsv` 之 ch10 側**全無列**，排除即無所依據。理由具名而非靜默略過 |
| 9（lower screen）| 僅 `-077`（`051`，讀 Comfort main Menu Bar icon）**暴露 → 補**；`-078`／`-079`／`-080` 之 popup 於 6.3 車輛仍存（`except for comfort popups`），不補 |
| 12（僅前排氣候）| 不觀察 tab，**0 條** |

### 6.3 `SWE1-HVAC-044-02` 停下 —— gate 擋住了我

`10.1` 之 `reduces climate control system power consumption` **無任何 HMI
可觀察量**，形態合於 `[BLOCKED-SPEC]`（擁有者為動力系統之耗電規格）。

我先產了該 BLOCKED row，**`marker-whitelist` gate 立刻 FAIL**：

```
[FAIL] marker-whitelist: NR1L-ComfortHMI-068: carries [BLOCKED-SPEC] but is
not in profile §5.1's named whitelist; an exemption-granting marker cannot
be self-issued (R-C26)
```

**R-C26 是對的，我不該自加。** 改為停下回報：該 leaf 不產列、不入分母，
待白名單增列之裁定。

**這是 R-C26 上線以來第一次真的擋住東西** —— 先前三輪它都只是綠燈。

---

## 7. lint 與 §9 自評（僅變動項）

```
41 / 41 gates PASS; 0 finding(s) across 80 TCs
```

五個 generator 連續重跑，輸出不變；`tc_id` 001–080 連號無缺。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 2 | tc_title | 變 | 批次 5 之 14 條字數 5–10；`-036`／`-037` 拆後各帶單位 token（Celsius／Fahrenheit）|
| 3 | PC | 變 | 6 條各減一行；批次 5 之 14 條各 2–3 行（第十五軸 ＋ 第十三軸排除，`-077` 另加第九軸）。實測 PC 內無動作動詞 → 0 命中 |
| 10 | ER 可觀察 | 變 | **依 R-C23 明說：依據不是 `er-subject-net`**。批次 5 之 32 行 ER 逐行讀，主詞為 `The AUTO state`／`The climate screen`／`The button label`／`The airflow modes`／`The fan speed indication`／`The Comfort main Menu Bar icon`／`The comfort pop up`，皆系統側 |
| 11 | negative 配對 | 變 | `-072`（`048-03`）驗「按 AUTO 無法退出 AUTO」與「按其他鍵可中斷」，正負同條成對，且兩側皆條文明文 |
| 12 | §8.2.1／造值 | 變 | 批次 5 之委派逐節具名：10.5 之中斷條件完整清單委派 standard ICE AUTO、10.6 之取消選取細節委派 2.3、10.9／10.9.1 之 popup 觸發規則委派 2.2／ch14。造值：10.1 之耗電無可觀察量故停下，不寫入任何量測方式 |
| 13 | design_method | 變 | 批次 5：功能測試 ×9、狀態轉換 ×5（AUTO 狀態遷移、跨點火保留）。`-036`／`-037` 由決策表改功能測試 |
| 16 | spec_ref | 變 | 批次 5 之 13 條為 `10.x; 10.1; 2.14`（第十五軸出處為 10.1，R-C29），`-077` 另加 `6.3`；`-067` 之出處即本節故為 `10.1; 2.14` |

其餘 10 項未變。

---

## 8. 進度

| | 數 |
|---|---|
| 驗證單位（leaf）| 403 |
| 已生成（leaf）| **75** |
| 已生成（TC）| **80** |
| 阻塞／停下（leaf）| 3（2.1 之 2 ＋ `044-02` 之 1）|
| 未開始（leaf）| 325 |

Test Set 完成：`Seat Control Tab` 14/14、`Tri-Mode Climate` 14 leaf/17 TC、
`Temperature and Fan` 19/19、`Front Climate Anatomy` 14/16、
**`ECO HVAC` 14/15**。

---

## 9. 未寫回

`output/` 仍 2 檔，`write_back.py` 未執行，`DELIVERY.sha256` 未增列。

---

## 10. 「本包是否仍有該驗而未驗者」

依 R-C30。

1. **`-022` 之實務歧義未消。** 條文層面 ch10 未宣稱差異（§4），故不補；
   但在配備 ECO HVAC 之 BEV 上，「進入 AUTO」實際上是 AUTO ECO 或 AUTO ON，
   **`-022` 之 ER 由測試員自行認定其一**。條文兩側皆未涵蓋此交界
   —— 這是 RD-1 型缺口，我**未自行登記**（未授權），列此待裁。
2. **`ECO HVAC` 與 `Temperature and Fan` 兩組之候選未判。**
   新版產生器對其分別產出 **164 對**與 **41 對**，本包只判了下放包所指定
   之三組。`ECO HVAC` 之 164 對尤其多（`AUTO` 於全語料極常見）。
   **搜尋範圍**：僅 `Seat Control Tab`／`Tri-Mode Climate`／
   `Front Climate Anatomy` 三組。
3. **等價組只涵蓋 `MAX *`／`REAR *`／`FRONT *` 三種前綴。**
   **搜尋範圍**：即該三 pattern 之全 129 節掃描。
   其他同義異寫（如 `A/C` vs `AC`、`SYNC` vs `Sync`）**未掃**
   —— 後者實際存在（3.2 寫 `turns on Sync`，2.11 寫 `SYNC`），
   而 `VOCAB` 之 `\bSYNC\b` 為大小寫敏感之字面，故 `Sync` 不被計入。
   **這可能正在漏掉 sibling，與 `MAX DEFROST` 同型。**
4. **批次 5 之 `-067`（ECO HVAC 可被選取）其 ER「AUTO ECO 模式為作用中」**
   實際上與 `-070`（第一次按壓啟動 AUTO ECO）之驗證目標重疊。
   037 給了不同 leaf（044-01 vs 047），依 §8.2 未合併 —— 但兩者之
   procedure 幾乎相同，**區別僅在 test_item 所引之條文**。
5. **10.2 之三張圖片不可讀**（`section_fulltext` 僅存檔名），
   故 `-068` 只驗三狀態之存在與循環，不驗其視覺呈現。
   若圖片載有狀態圖示之規格，該部分目前無 TC 涵蓋。

---

## 11. 建議 commit message（git 未執行）

```
feat(comfort): axis 15 and ECO HVAC; remove 6 over-strict EMEA PCs

- remove the EMEA exclusion and 16.2 citation from 020-03/-04, 022-02, 011
  and the new Fahrenheit row; 40 TCs keep both, one-to-one with no residue
- split -036 into Celsius and Fahrenheit rows on 8.3's input_data axis;
  decision-table -> functional after the split; -037..-065 shift by one
- judge the fifteenth axis from ch10's own wording: one axis (nothing makes
  "ECO HVAC equipped" independent of EV/BEV) and function-type (an ICE
  vehicle keeps the AUTO button, icon and pop-ups). Same shape as EMEA ICS,
  opposite class
- -022 takes branch two: ch10 never mentions MAX DEF, so 3.2's wording holds
  on BEV too; no PC, no ER change
- sibling generator marks high-frequency tokens instead of dropping them and
  normalises measured synonyms; it now finds 2.10 <-> 3.3, the pair it
  missed. Front Climate Anatomy goes 0 -> 19 candidates, all judged
- generate ECO HVAC as -067..-080; hold 044-02, whose [BLOCKED-SPEC] marker
  would need a whitelist ruling (marker-whitelist caught the attempt)
- RUNBOOK: section-level reads the opening, TC-level reads that sentence;
  a gate goes red for a violation, not for a pending decision
- lint 41/41 PASS across 80 TCs
```

---

## 12. 待分析層

1. **§6.3** —— `SWE1-HVAC-044-02` 之 `[BLOCKED-SPEC]` 白名單增列。
2. **§10.1** —— `-022` 於 BEV 之實務歧義是否登 RD-1。
3. **§10.2** —— `ECO HVAC`（164 對）與 `Temperature and Fan`（41 對）之候選是否須判。
4. **§10.3** —— 等價組是否擴及 `A/C`／`Sync` 等大小寫與縮寫變體。
