# 22 — Comfort HMI / 批次 3 補齊：R-C33、第十二・十三軸、§4.1 之實質複查

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 33
- 結果：批次 3 由 9 條增至 **14 條**（-032 … -045）。
  **§4.1 之實質複查答案為「須補」—— 2.2 之 8 條各補一行 PC，內容未重寫。**
  `2.1-01`／`-02` 未生成，登 **DR #17**（High，阻塞）。
  lint **37/37 PASS，0 finding，45 條**。**未寫回。**

---

## 1. R-C33 貼入 ＋ profile 兩軸

`RULINGS.md` 現有 **35 個**逐字條文區塊。R-C33 前附來源說明。

profile §3.2 設備配置軸由十一增為 **十三**：

- **第十二軸 僅前排氣候** —— 來源節 2.1
- **第十三軸 HVAC 實體控制型式** —— 來源節 2.14，三值

第十三軸另附兩段引用區塊：**與 `EMEA ICS` 之區別**（後者範圍寫明 ch16 全章、
指整套 ICS 氣候介面；本軸指 ch2 之實體旋鈕配置），與
**`MTC has a Climate screen` 不另立軸**（它是本軸之後果，把後果立成軸會使
同一事實有兩個來源而無人維護其一致性）。

---

## 2. §4.1 判別改寫為候選產生器

profile §3.2 與 `RUNBOOK.md` 各增一段，內容一致：

| 用途 | 可否 |
|---|---|
| 有選擇子 → 需要軸 | **可** —— 產生候選 |
| 無選擇子 → 不需要軸 | **不可** —— 陰性結果只是索引層事實（R-C13）|

並附本案例本身作為限制之證據（見 §3）。

`RUNBOOK.md` 版另記其同源：§5a（代理不得凌駕實質）、R-C13、R-C18、
22 §4（用詞禁令可繞過而判準不行），末句：
**以表徵為判準者，其失敗形態是靜默的 —— 而這次它甚至通過了 37 個 gate。**

---

## 3. §4.1 之實質複查 —— 答案是「**須補**」

### 3.1 實質理由（非「2.2 沒有選擇子」）

2.14 明文：

> **For MTC with ICS**, there will be no redundant interaction with the
> screen for certain types of physical knobs (**3 knob HVAC controls**) …
> In these cases, **no HVAC menu bar icons, no HVAC screens and no HVAC pop
> ups will be displayed.**

2.2 之 8 條**全數依賴氣候觸控畫面或 popup**：
`-032` 讀 climate screen、`-033` 驗 popup 逾時、`-034` 讀狀態列與類別鍵、
`-035` 驗 slider popup 抑制、`-036`／`-037` 驗 popup 內容、
`-038` 驗在 climate screen 之呈現、`-039` 驗 climate screen 之改變。

**在 3 旋鈕 ICS 之車上，這 8 條沒有一條可以執行** —— 不是會失敗，是
根本沒有被操作的對象。

### 3.2 處置：8 條各補一行 PC，內容未重寫

新增之 PC 行（依 R-C29 跨節取據，出處 `(2.14)`）：

```
2. [spec-derived] The vehicle does not have 3 knob HVAC controls with ICS,
   for which no HVAC screens or pop ups are displayed (2.14)
```

- **標 `spec-derived` 而非 `spec-verbatim`**：條文陳述的是「有 3 旋鈕 ICS
  時不顯示」，本行是其否定側，由該句推得而非照錄
- `specification_reference` 由 `2.2` 改為 **`2.2; 2.14`**（本節領頭）
- 其餘 PC 行順延編號（`PC_ATC`／`PC_MTC` 由 2 改 3，`-037` 之
  `MTC has a Climate screen` 由 3 改 4，`-035` 之乘客側由 2 改 3）
- **`test_item`／`test_procedure`／`expected_result` 逐字未動**

`reasoning` 更新為記錄實質理由，並刪去原本「本節無選擇子」之論述 ——
那句是代理判準，留著會讓下一個讀者以為它仍是依據。

### 3.3 這次失敗的形狀

**判別產生的候選是空的，而實質答案不是。**

我在上繳 21 §10.1 自陳「這是本包最需要被檢驗的一句話」，
並把它寫成可反駁的形式。**風險在同一批內就實現了** ——
而且它通過了全部 37 個 gate、通過了我自己的 §9 十七項自評。
**沒有任何機械檢查會問「這 8 條在哪種車上跑不起來」。**

---

## 4. 新增之 5 條（-041 … -045）

| tc_id | req_id | 節 | tc_title | 步/ER | spec_ref |
|---|---|---|---|---|---|
| -041 | 001-03 | 2.1 | No tabs are displayed when only Front climate is available | 2/2 | 2.1 |
| -042 | 020-01 | 2.14 | MTC shows no discrete temperature setting | 2/2 | 2.14 |
| -043 | 020-02 | 2.14 | MTC offers no Auto control over the set temperature | 2/2 | 2.14 |
| -044 | 020-03 | 2.14 | Screen offers no redundant interaction with the 3 knob controls | 2/2 | 2.14 |
| -045 | 020-04 | 2.14 | No HVAC icons screens or pop-ups with 3 knob ICS controls | 3/3 | 2.14 |

**四條之 PC 出處皆為其所屬節**，故 R-C29 之義務一不觸發，spec_ref 各列單節
—— 與同批 2.2 之 8 條（`2.2; 2.14`）恰成對照。

### 4.1 `-043` 之 `"Auto"` 依 R-C33 取條文寫法

037 leaf 寫 `"AUTO"`，條文寫 `"Auto" control over the set temperature`。
**依 R-C33 第二項，內容以條文為準**，故 TC 內一律 `"Auto"`。
這是本包內 R-C33 之第二次適用，且是**小到容易被略過**的那種 ——
大小寫也是內容。

### 4.2 `-044` 與 `-045` 之界線

- `-044` 驗**機制**：螢幕不提供與 3 旋鈕重複之互動（`no redundant
  interaction with the screen`）
- `-045` 驗**三項具體後果**：無 menu bar icon、無畫面、無 popup

037 給了兩個 leaf，依 §8.2 單位歸 037，**未合併**。兩者確有重疊
（沒有畫面即無從重複互動），此重疊來自上游而非本層。

### 4.3 `-045` 之例外情形未產生 TC —— 覆蓋缺口，已登 DR #19

`SWE1-HVAC-020-04` 之 leaf 同時含：

| | 配置 | 結果 |
|---|---|---|
| 主情形 | 3 旋鈕 ICS | 不顯示 HVAC UI |
| **例外** | `one zone MTC with push button TEMPERATURE` | 例外**不適用**，即**顯示** |

兩者為**不同車輛配置**，`pre_conditions` 無法共用，**一條 TC 涵蓋不了**。

下放包 33 §6 指示「共 5 條」，故本批依指示生成 4 leaf → 4 TC，
**例外情形未產生任何 TC**。這是 §7 之 negative pairing 的正向對照，
且條文明文支撐（不同於 `-035` 之無條文支撐）。

**已登 `DATA_REQUESTS.md` #19**，待裁是否依 §5.7（different scopes → split）
拆為兩條並同溯該 leaf。**我未自行拆**，因為下放包給了明確條數。

---

## 5. `2.1-01`／`-02` 未生成 —— 兩件事，只解了一件

### 5.1 已解：內容衝突（A-CF21 → RESOLVED-BY-RULING）

R-C33 定處置：leaf 維持 037 之三個，內容依條文之 **4 tabs 含 Massage**。
RD-1 候選登為 **DR #18**（Medium，**不阻塞** —— 呈報之目的為使 037 與 spec
對齊，非等待答案才能開工）。

**我原判「現行條文未涵蓋」對 §8.6 而言正確而不完整** —— §8.6 管 spec 與其
索引導出；但 §8.1「Conflict → Req wins; flag RD」與 §8.2 併讀即得分工，
**我當時未把兩條併起來讀**。

### 5.2 未解：內容不足（DR #17，High，阻塞）

條文只寫 `up to 4 tabs **depending on vehicle configuration**`，
**未述何種配置產生何種 tab**。故即使 037 與條文完全一致，
`-01`（tab 數）與 `-02`（順序）仍無法寫出一個已知的 tab 集合作為 PC ——
任何具體配置皆為造值（R-C28 第一問）。

**解 A-CF21 不解 DR #17。** 兩者已於 ANOMALIES 條目內明白分開，
避免日後有人看到 RESOLVED 就以為 2.1 可以開工。

第十二軸增列後，`-03` 已生成（`-041`）。

---

## 6. lint

```
37 / 37 gates PASS; 0 finding(s) across 45 TCs
```

三個 generator 連續重跑，輸出逐位元組不變。`tc_id` 001–045 連號無缺。

---

## 7. §9 self-check —— 僅列變動項（R-C23）

### 7.1 2.2 之 8 條（變動項）

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 3 | PC 僅 state/env 且為 spec trigger | **變** | 各補一行第十三軸之排除項。8 條之逐條 PC 行數由 `1,1,1,1,1,2,2,3` 增為 `2,2,2,2,2,3,3,4`（批次 3 全 14 條共 **28 行 PC**）。實測 PC 內無動作動詞 → 0 命中 |
| 12 | 溯源、§8.2.1、無造值 | **變** | 引 2.14 之**裝備事實**而不驗其行為 —— 2.14 之行為由同批 `-044`／`-045` 驗證，兩者之 `req_id` 不同、觀察對象不同，未構成擴張 |
| 16 | `specification_reference` 涵蓋所有直接驗證或賴以 setup 之節 | **變** | 8 條由 `2.2` 改為 `2.2; 2.14`，與新增之 PC 行逐一對應（R-C29 義務一）|

其餘 14 項未變。

### 7.2 新增之 5 條

| # | 項目 | 判 | 獨立依據（非 lint 覆述）|
|---|---|---|---|
| 1 | Test Set 與 framework 相符 | PASS | `test_set` 皆 `Front Climate Anatomy`，與 framework.md 第 39 行逐字元相同；四節（2.1／2.2／2.14／6.3）現已全數有 TC |
| 2 | tc_title 形狀／字數／sibling／無 modal | PASS | 字數 10／6／9／10／11。`-042`（discrete temperature）／`-043`（Auto control）／`-044`（redundant interaction）／`-045`（icons screens pop-ups）四者互斥，且四者同屬 2.14，區分尤須清楚 |
| 3 | PC 僅 state/env 且為 spec trigger | PASS | 5 條共 **7 行 PC**，全為系統類型或裝備（僅前排氣候／MTC／3 旋鈕 ICS）。實測無動作動詞 → 0 命中 |
| 4 | Input Test Data 欄位歸屬 | PASS | 皆 `NA`；5 條無數值輸入 |
| 5 | 步驟可執行、無禁用動詞 | PASS | 首字動詞 `Open`／`Read`／`Change`。**本項現有 gate，故依 R-C23 另補**：5 條之步驟皆為「開啟 → 讀取」型，無「執行後自行判斷」型指示 |
| 6 | 步驟長度與意圖層級 | PASS | 步數 2／2／2／2／3，無贅步 |
| 7 | 標準 setup 片段逐字重用 | **N/A** | 5 條之 PC 逐條獨立撰寫，未共用常數 —— 因其出處節與所屬節同一，無跨節套用之風險 |
| 8 | CLI／tooling | **N/A** | 皆 HMI 操作 |
| 9 | 基線步驟 | PASS | 5 條之 ER 第 1 行皆為前置畫面之確認（`The comfort category is displayed`／`The climate screen is displayed`／`The head unit menu is displayed`）—— 使「什麼都沒顯示」與「畫面根本沒開」可分辨。**這對五條全為否定式 ER 的批次特別必要**（見 §8.3）|
| 10 | procedure↔ER 1:1、ER 可觀察、無 modal | PASS | **依 R-C23 明說：依據不是 `er-subject-net`**。逐行讀 **11 行 ER**，主詞為 `The comfort category`／`No tabs`／`The climate screen`／`No discrete temperature setting`／`No "Auto" control`／`The head unit`／`No HVAC menu bar icon`／`No HVAC screen and no HVAC pop up` —— 皆系統側之物或其缺席 |
| 11 | 無 FP／FF；supported 配 negative | PASS | FF：畫面之開啟由步驟建立。negative：`-045` 之例外情形為其正向對照而**未生成**，已登 DR #19（§4.3）—— 此為已知缺口，非遺漏 |
| 12 | 溯源、§8.2.1、§8.2.2、無造值 | PASS | 溯源：5 條之 `req_id` 於 037 逐一存在。**§8.2.1**：2.14 之 TC 只驗 head unit 上之**缺席**，不驗 ICS 自身行為（觀察位置不同）；2.1 之 Massage **行為**委派他份文件而其**存在**屬 2.1，兩者未混。造值：`depending on vehicle configuration` 未展開，故 `-01`／`-02` 不生成 |
| 13 | design_method 於 procedure 定案後指派 | PASS | 5 條皆 `功能測試`（讀取型，無遷移、無條件表）。批次 3 全體分布：功能測試 ×12、狀態轉換 ×1（`-033`）、決策表 ×1（`-036`）|
| 14 | 四長欄無行尾句點 | PASS | lint 覆蓋；另查其未涵蓋之 `test_item`：5 條逐條確認無行尾句點 |
| 15 | UI 標籤用 `"..."` | PASS | **本批唯一加引號者為 `-043` 之 `"Auto"`** —— 因條文自身即以引號寫 `"Auto" control`，那是螢幕上的字。其餘（tabs／temperature setting／menu bar icons）為元件類名，不加引號 |
| 16 | `specification_reference` | PASS | 5 條各列單節，與其 PC 出處逐一相符 |
| 17 | 來源 spec 勝過 index export | PASS | **本項為本包之重點**：`-043` 依 R-C33 取條文之 `"Auto"` 而非 037 之 `"AUTO"`；`2.1` 之內容依條文之 4 tabs 而非 037 之 3 tabs。條文一律讀 `section_fulltext.tsv` |

**15 PASS、2 N/A。**

---

## 8. 未寫回

依 33 §6 第 7 項，**未寫回**。`output/` 仍 2 檔。

寫回節奏仍待 Pei（32 §7）。補一項事實：批次 3 現有 **8 條**帶多節
`spec_ref`（`2.2; 2.14`，約 160 字元），批次 2 有 2 條（約 240 字元）。
**A-CF19 之待測樣本由 2 條增為 10 條**，且最長者仍在批次 2。

---

## 9. 進度

| | 數 |
|---|---|
| 驗證單位（leaf）| 403 |
| 已生成（leaf）| **42** |
| 已生成（TC）| **45** |
| 阻塞（leaf）| 2（`SWE1-HVAC-001-01`／`-02`，DR #17）|
| 未開始（leaf）| 359 |

Test Set：`Seat Control Tab` 14/14、`Tri-Mode Climate` 14/14、
**`Front Climate Anatomy` 14/16**（餘 2 leaf 阻塞於 DR #17）。

---

## 10. 「本包是否仍有該驗而未驗者」

依 R-C30，陰性陳述附搜尋範圍。

1. **§3 之複查我只做了一個方向。** 我問的是「2.2 是否須排除某種車輛」，
   **沒問「其他已生成之批次是否也須排除某種車輛」**。
   **搜尋範圍**：僅 2.2 之 8 條 ＋ 2.14 之條文。
   pilot 14 條、批次 2 之 17 條**未以同一問題複查** ——
   例如 `Seat Control Tab` 之 13.x 是否在某種配置下無 lower screen 可用。
   **這是本包最可能重演同一錯誤之處。**
2. **第十三軸之「其他」值我用了否定式表述。**
   PC 寫 `does not have 3 knob HVAC controls with ICS`，
   而該軸尚有第三值（`one zone MTC with push button TEMPERATURE`）。
   否定式涵蓋了「其他」與「單區 MTC 附 push button」兩者 ——
   **對 2.2 而言正確**（兩者皆顯示 HVAC UI），
   但它把三值軸壓成二值，若日後某節需區分後兩者，此措辭不敷使用。
3. **`-044` 之 ER 是我改寫過的。** 條文之 `-03` leaf 說「no mismatch
   occurs」，那是**目的**（`in order to prevent a mismatch`）而非可觀察量。
   我改以「螢幕不提供重複互動」為 ER —— 那是條文之機制句。
   **若分析層認為 mismatch 本身須被驗證，本條須重寫**；
   但我判「無軟控可與硬控相牴觸」即為其可觀察形式。
4. **DR #19 之例外情形**未生成 TC，`-045` 之 `test_item` 亦未提及例外
   —— 我只寫主情形。**leaf 之一半內容目前沒有任何 TC 提到它。**
5. **`2.1` 之 4 tabs 內容依 R-C33 應以條文為準，但本輪無 TC 用到它**
   —— `-041` 驗的是「不顯示」，用不到 tab 清單。故 R-C33 之第二項於 2.1
   **尚未真正被行使**，要到 DR #17 解答後 `-01`／`-02` 生成時才會。

---

## 11. 建議 commit message（git 未執行）

```
feat(comfort): complete batch 3 — 14 of 16 leaves

- add R-C33 (037 owns the unit, the clause owns the content) to RULINGS
- profile 3.2: twelfth axis (Front-only climate) and thirteenth (HVAC
  physical control type), with the EMEA-ICS distinction spelled out
- demote the "On vehicles with X" test to a candidate generator; a negative
  result may not be read as "no axis needed"
- substantive re-review: 2.2's eight TCs each gain one pre_condition
  excluding 3-knob-ICS vehicles, and cite 2.14; no content rewritten
- generate 2.1-03 and 2.14's four leaves, tc_id -041..-045
- A-CF21 resolved by ruling; 2.1-01/-02 stay blocked on DR #17 (content
  gap, a different problem from the conflict)
- register DR #17, #18, #19
- lint 37/37 PASS, 0 findings across 45 TCs
```

---

## 12. 待分析層

1. **§10.1** —— pilot 與批次 2 是否須以同一問題複查（我判「應該要」，
   但未做，因為超出本包授權）。
2. **DR #19** —— `-045` 之例外情形是否拆條。
3. **§10.3** —— `-044` 之 ER 改寫是否成立。
4. **DR #17** —— `2.1` 之 tab 集合由何種配置決定（High，阻塞 2 leaf）。
