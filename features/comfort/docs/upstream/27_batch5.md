# 27 — Comfort HMI / R-C36-1 逐條補答、三組候選、批次 5 全停

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 38
- 結果：**R-C36-1 之逐條補答立刻抓到 5 條「否」＋ 1 條「判不出」**
  —— `mirrored` 掩蓋之過嚴排除已現形（未自行移除）。
  候選產生器對三組執行，**並由人工補上一對它漏掉的 sibling**。
  **批次 5 全數停下**（15 leaf）—— 第十五軸不在十四軸內。
  lint **40 → 41 gate，全 PASS，65 條**。**未寫回。**

---

## 1. R-C36-1 貼入

置於 **R-C36 之後**，**R-C36 原文一字未改**。`RULINGS.md` 現有 **40 個**
逐字條文區塊。

---

## 2. 45 條逐條補答 —— **`mirrored` 掩蓋了 5 條**

### 2.1 機制

新增 `data/emea_ics_per_tc.tsv`（45 列，欄 `tc_id`／`outline`／
`ch16_outline`／`verdict`／`ch16_sentence`），generator 將其附為每條 TC 之
`emea_ics_review`，並列入 `NOT_IN_WORKBOOK`。

新 gate **`emea-per-tc-answered`**（lint 40 → 41）：凡帶 EMEA 排除式 PC 者，
須有指向 ch16 具體句之逐條判定，缺者 FAIL。

**verdict 非 `yes` 者不使 lint 變紅**，改以具名回報行輸出：

```
- PASS — EMEA exclusions whose per-TC answer is NOT `yes` (R-C36-1;
  over-strict, removal awaits a ruling): [('NR1L-ComfortHMI-036',
  'undecided', '16.2'), ('NR1L-ComfortHMI-044', 'no', '16.14'), …]
```

**設計理由**：移除須經裁定（§1 之前例）。若 gate 因「否」而變紅，
執行層會被紅燈推著自行移除 —— 那正是本輪要避免的。

### 2.2 結果：39 `yes`／5 `no`／1 `undecided`

| verdict | tc_id | ch16 對造 | 理由 |
|---|---|---|---|
| **no** | `-044`／`-045`／`-046` | 16.14 | **ICE13 僅兩句**（MTC screens/popups 之使用時機、與 ATC 之差異），**完全不含 C15 之 3 旋鈕 ICS 段落** |
| **no** | `-064` | 16.17 | **16.17 僅一句**，不含 C18 之第二句「After blower reduction, return blower speed to previous speed…」 |
| **no** | `-065` | 16.7 | **ICE6 只列 `Fan ranges: Off, 1-7`**，本條驗 `Off, 1-8` |
| **undecided** | `-036` | 16.2 | ICE1 有「(or half degree increments for Celsius)」**但無 C1 之「and for Fahrenheit do not show half degrees」** —— 本條同時驗攝氏與華氏，**一半涵蓋一半未涵蓋** |

**5 條之排除式 PC 過嚴，1 條判不出。回報清單，未自行移除。**

### 2.3 這正是 R-C36-1 要抓的東西

`16.14` 與 `2.14` 在鏡射表中記為 **`mirrored`**，依據為「首二句逐字相同」
—— 而 **ICE13 全文就只有那兩句**。`16.17` 同理：與 2.16 之首句逐字相同，
而它只有一句。

**節級 `mirrored` 之依據是「開頭一樣」，TC 級要問的是「這條所驗的那一句
在不在」。** 兩者在 `-044`…`-046`、`-064` 上給出相反答案。

`-036` 之 `undecided` 則是另一種形狀：**同一條 TC 之行為橫跨涵蓋線兩側**。
R-C36-1 之三分支中「判不出 → 停下回報」正為此而設；若 TC 拆成攝氏、華氏
兩條，兩者各自可判 —— **但拆條屬 §8.2.2 之裁定，不自行為之。**

### 2.4 39 條 `yes` 之依據皆為具體句，非「該節為 mirrored」

例：`-028`（風速改變不破壞 MAX DEF）之依據為
ICE7「Change in fan speed doesn't break MAX DEF」；
`-057`（僅滑桿把手可移動）之依據為
ICE5.1「User must press slider handle to move temperature slider position;
if user initially presses slider area outside of handle, ignore the press」。

---

## 3. 三組各跑一次候選產生器

| 組 | 候選對 | 判定 |
|---|---|---|
| `Seat Control Tab` | **0** | 座椅控制之語彙與氣候章無交集 |
| `Front Climate Anatomy` | **0** | 其節之高頻詞（`FAN`／`MODE`／`TEMPERATURE`）皆在排除清單內 |
| `Tri-Mode Climate` | **14** | 全數判定，皆 `not-sibling` |

14 對之判定：**9 對為 ch16 側**（鏡射關係而非 §4.6 sibling，由
`ch16_mirror_map.tsv` 承載）；**5 對為語彙重疊而非同一需求**
（如 `2.13 ↔ 3.2`：2.13 定義 MAX A/C 自身之 on/off，3.2 僅述「按 MAX A/C
會關閉 MAX DEF」）。

`data/pending_sibling.tsv` 現 **21 列**（5 `sibling`／16 `not-sibling`），
`reviewed_at = 129`。

### 3.1 產生器漏掉一對，我用人工補上 —— 且漏掉的原因可具名

**`2.10` ↔ `3.3` 是 sibling，而產生器沒有產出它。**

- 2.10：`grey out remaining buttons **except for Front/Max defrost and rear
  defrost**`
- 3.3：`**MAX DEF and REAR DEF** are available during climate off`

**同一事實之兩處陳述**（上繳 19 §6 早已把 2.10 認定為 3.3 之委派節）。

**漏掉的原因**（實測）：

```
2.10 之語彙 = ['CLIMATE OFF', 'MAX DEFROST', 'REAR DEFROST']
3.3  之語彙 = ['MAX DEF']
交集       = []
```

**一邊寫 `MAX DEFROST`、一邊寫 `MAX DEF`，交集為空。**

這是 R-C37 所述「無共同語彙之 sibling」之**具體實例**，且它不是假想的
——**是一對我們早就知道的 sibling，產生器卻看不見。** 已以
`verdict=sibling` 入表並註明其為人工發現。

**推論**：產生器之免責聲明不是客套。**它漏掉的第一個實例，正是我們手上
已經有答案的那一對** —— 若我們沒有先驗知識，這一對到今天仍不會被看見。

---

## 4. `2.6`／`2.6.1` 之時間條件 —— 分支二

**實測**：pattern `\d+\s*(ms|milliseconds?|sec|seconds?)` 於 2.6／2.6.1
**0 命中**；而 `long press`／`fast move` 有命中。

> 2.6：`[]`
> 2.6.1：`['long press', 'fast move', 'Long press', 'fast move']`
> 7.4（對照）：`['long press', 'fast move', 'hold', '500 ms']`

**即：有條件而無值 → 分支二 → 登 RD-1 候選（DR #21），ER 不變。**

**下放包對我措辭之訂正我接受**：`-055` 之 ER **不是「比條文所能支持的
更弱」，而是恰好等於 2.6.x 所支持的強度**。寫入 7.4 之 `500 ms` 即為
以他節數值補值（§8.4.1）。DR #21 之條目內已記此訂正。

---

## 5. 組別解析之反向驗證 ＋ 129 節比對

### 5.1 不需注入之檢查（每次執行）

`verify_parse()` 於解析後、使用前執行，三項比對 —— 對象為
**`test_set_map.tsv`**（Phase 3 獨立導出），故錯誤須同時發生於兩處才會通過：

```
parse check: 129 sections, each in exactly one Test Set,
             agreeing with test_set_map.tsv
```

任一不符即 `SystemExit`（ABORT），不繼續產生候選。

### 5.2 反向驗證三方向

| 注入 | 結果 |
|---|---|
| **A** 刪去 `Rear Climate` 之 `7.1 ~ 7.10` 區間 | **ABORT** —— `11 section(s) resolved to no Test Set: ['7.1','7.1.1',…]`，並逐節列出與 map 之歧異 |
| **B** 把 `2.6` 重複列入 `Climate Modes` | **第一次未觸發**，見 §5.3；加防護後 **ABORT** —— `framework.md lists 2.6 under both 'Climate Modes' and 'Temperature and Fan'` |
| **C** 刪去 `ECO HVAC` 列之 leaf 數欄 | **未 ABORT，且此為正解** —— 該損壞不改變「節 → 組」之映射（正規表示式仍取到 `10.1 ~ 10.9.1`），檢查之對象是映射而非表格排版。**通過是對的答案，不是漏抓** |

### 5.3 方向 B 第一次沒觸發 —— 是真缺陷，已修

原實作為 `mapping[part] = name`，**後者覆蓋前者**。注入使 `2.6` 先被指派
給 `Climate Modes`，而後第 3 組之列再把它寫回 `Temperature and Fan`
—— **最終映射正確，注入被靜默中和**，我的檢查因此看不見。

**重複指派本身即為錯誤**，故改為：同一節出現於兩組即 ABORT。
修後方向 B 正常觸發。

**若我只跑了方向 A 就收工，會得出「解析已驗」之結論** —— 而實際上
一整類損壞（重複列入）當時是通不過任何檢查的。

---

## 6. `RUNBOOK.md` —— 比對基礎設施

新增一節，含兩次事故之對照表（zsh `${PIPESTATUS[0]}` 取空字串／
`/tmp/base` 為既存檔案），並記：

> **兩次都是假 FAIL，方向安全 —— 但下一次未必。**
> 一個假 PASS 長得跟真 PASS 一模一樣。
>
> 凡以比對為驗證手段者，**先確認比對之兩側皆實際存在**，再讀其結果。
> 看到全部都 DIFF 時，**先懷疑比對，不要先懷疑被比對的東西**。

---

## 7. 批次 5 `ECO HVAC` —— **全數停下（15 leaf）**

### 7.1 範圍自 `framework.md` 導出

第 45 行：`10.1 ~ 10.9.1` / **15 leaves**。`layer3_map.tsv` 逐節相加
= 15，相符。**章標題為 `ECO HVAC (BEV only)`。**

### 7.2 停下之理由：第十五軸不在十四軸內

ch10 **全部 15 個 leaf** 之可測性皆繫於同一配置條件：

| 條文 | 逐字 |
|---|---|
| 10.1 | `ECO HVAC is an HVAC Mode, used on **EV Vehicles only**` |
| 10.2 | `**For BEV vehicles**, the AUTO functionality can have 3 states: AUTO ECO, AUTO ON, AUTO OFF` |
| 10.9.1 | `**When ECO HVAC is equipped on a vehicle**, the AUTO pop ups…` |

無此配置即無 `AUTO ECO` 可按、無第三狀態可循環、無附加提示文字可讀
—— **15 條無一有對象**。該軸不在十四軸內，依 28 §2.1(b) 停下，不自行增軸。

### 7.3 軸提案（三項條件已備妥，裁定後不需重做）

**條件 1 —— 值取自條文逐字**：

```
第十五軸候選  動力系統／ECO HVAC 配備
  值：EV / BEV 車輛且配備 ECO HVAC（10.1「used on EV Vehicles only」、
      10.2「For BEV vehicles」、10.9.1「When ECO HVAC is equipped on a vehicle」）
   ／ 非 EV 車輛或未配備（同上三句之反面）
```

**須一併裁定者**：條文用了**三種措辭**（`EV Vehicles`／`BEV vehicles`／
`ECO HVAC is equipped`）。三者是否同一條件？10.9.1 之
`When ECO HVAC is equipped` 暗示**即使是 BEV 也可能未配備**
—— 若如此，這是**兩個軸**（動力系統、ECO HVAC 配備）而非一個。
**我不自行決定其為一或二。**

**條件 2 —— 類別（R-C34）**：判為**功能型**。

理由：非 BEV 車上 AUTO 按鈕、Menu Bar icon、comfort popup **皆仍存在**
（10.5 引「standard ICE AUTO logics」、10.9.1 對照「the standard ICE AUTO
pop up」），消失的是 **AUTO ECO 這個狀態**，不是承載它的介面。

**與下放包 §6 之預期不同，故明說**：下放包預期「BEV-only 意味非 BEV 車上
整章無介面」。實測條文顯示介面在、功能不在 —— 若判為介面型，
`interface_axis_review` 須增鍵；判為功能型則不必。**此判定請覆核。**

**條件 3 —— 既有 65 條之影響（實測）**：

**搜尋範圍**：全 65 條之 `test_item`＋`test_procedure`＋`expected_result`，
pattern `\bAUTO\b|"Auto"`。**命中 2 條**：

| tc_id | 條 | 影響 |
|---|---|---|
| `-043` | 2.14 | 驗「MTC 無 Auto 控制」。ch10 之三狀態屬 BEV 之 AUTO，與 MTC 無 Auto 不衝突 —— **無影響** |
| `-022` | 3.2 | 驗「按 AUTO 關閉 MAX DEF → 進入 AUTO」。**在配備 ECO HVAC 之 BEV 上，「進入 AUTO」有兩種可能（AUTO ECO 或 AUTO ON），其 ER 之判定變得不唯一** —— **有影響，須補排除式 PC 或收緊 ER** |

另掃全 129 節之 `BEV`／`EV Vehicles`／`ECO HVAC`／`AUTO ECO`：
命中 **9 節、14 leaf，全部在 ch10 之內**（10.7 未命中，其句為
`HVAC AUTO shall keep the selected setting through ignition cycles`）。
**ch10 之外零命中** —— 該軸之影響不外溢，僅 `-022` 因 AUTO 之語意分歧而
受波及。

### 7.4 我未做的事

- 未增軸、未生成任何列（R-C16：缺口不產列）
- 未替 `-022` 補 PC —— 該補行繫於軸是否成立、成立後為一軸或兩軸
- 未把 ch10 標 `[BLOCKED-SPEC]` —— 本案非委派而是 profile 未涵蓋（同前例）

---

## 8. lint 與 §9 自評（僅變動項）

```
41 / 41 gates PASS; 0 finding(s) across 65 TCs
```

四個 generator 連續重跑，輸出不變。**本輪未新增 TC**，故 §9 十七項
**無一項變動** —— 變動者為 TC 之附註欄（`emea_ics_review`）與 gate，
非 TC 內容本身。

依 R-C23 仍具名一項獨立查核：45 條之 `emea_ics_review` 我**逐條讀了
ch16 對造節之全文**（16.2／16.6／16.6.1／16.7／16.8／16.10／16.14／16.17
八節），而非引鏡射表之結論 —— 這正是 §2.3 之五條「否」被找出來的方式。

---

## 9. 進度

| | 數 |
|---|---|
| 驗證單位（leaf）| 403 |
| 已生成（leaf）| **61** |
| 已生成（TC）| **65** |
| 阻塞／停下（leaf）| **17**（2.1 之 2 ＋ ch10 之 15）|
| 未開始（leaf）| 325 |

---

## 10. 「本包是否仍有該驗而未驗者」

依 R-C30。

1. **45 條之逐條判定由我一人做成，未經第二人覆核。**
   `ch16_sentence` 欄逐條可查，故可覆核 —— 但尚未被覆核。
   **且我是先讀 ch16 全文再判**，若某句我讀漏，該條會被判成 `yes` 而
   沒有任何機制會發現（同「答了不等於答對了」）。
2. **`-036` 之 `undecided` 目前沒有處置路徑。** 它既未被移除也未被拆條，
   `emea_ics_review` 記著它判不出。**在裁定前，該條之 PC 狀態是未定的**
   —— 而它看起來跟其他 44 條一樣正常。
3. **候選產生器對三組之「0 對」，其可信度低於 `Tri-Mode Climate` 之 14 對。**
   `Front Climate Anatomy` 之 0 對，成因是其節之高頻詞全在排除清單內
   —— **排除清單是為可讀性設的，不是為正確性設的**，而它直接造成了那個 0。
4. **`2.10 ↔ 3.3` 之漏抓已補，但我沒有系統性地找「還有多少對這樣的」。**
   **搜尋範圍**：僅該一對（因為我事先知道它）。
   同型（同義而異寫）之 sibling 可能還有，例如 `MAX A/C` vs `MAX AC`、
   `REAR DEF` vs `REAR DEFROST`。**未掃。**
5. **第十五軸為一軸或二軸（§7.3），我未決而它影響 15 個 leaf 之 PC 形態。**
6. **`-022` 之影響我判為「有」，但未判其處置**（補排除式 PC 抑或收緊 ER）
   —— 兩者對 coverage 之意義不同：前者縮小適用車型，後者縮小驗證範圍。

---

## 11. 建議 commit message（git 未執行）

```
feat(comfort): per-TC EMEA answers (R-C36-1); batch 5 held

- add R-C36-1 after R-C36 without touching its text
- data/emea_ics_per_tc.tsv: all 45 EMEA exclusions answered against a named
  ch16 sentence; 39 yes, 5 no, 1 undecided
- section-level `mirrored` had hidden five over-strict exclusions: ICE13 is
  two sentences where C15 is a paragraph, ICE17 one where C18 is two, and
  ICE6 lists only Off, 1-7. Listed, not removed
- add emea-per-tc-answered gate; a non-yes verdict reports on a named line
  rather than reddening the build, because removal is a ruling
- run the sibling generator for the three older Test Sets; 14 candidates in
  Tri-Mode Climate, all not-sibling. Add 2.10 <-> 3.3 by hand: the generator
  missed it because one clause writes MAX DEFROST and the other MAX DEF
- verify_parse: 129 sections, one group each, checked against
  test_set_map.tsv; duplicate group assignment now aborts
- DR #21: 2.6.1 states a long-press condition with no value
- hold batch 5 entirely: ECO HVAC needs a fifteenth axis (function-type,
  proposal and impact measured); -022's ER becomes ambiguous on a BEV
- lint 40 -> 41 gates, all PASS across 65 TCs
```

---

## 12. 待分析層

1. **§2.2** —— 5 條「否」之排除式 PC 是否移除；`-036` 之 `undecided` 如何處置
   （拆條抑或其他）。
2. **§7.3** —— 第十五軸：一軸或兩軸；類別判為功能型是否成立。
3. **§7.3** —— `-022` 在 BEV 上之 ER 歧義，補 PC 抑或收緊 ER。
4. **§10.3／§10.4** —— 候選產生器之排除清單與同義異寫之 sibling 是否須另掃。
