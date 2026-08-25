# 下放包 35 —— DESC 完整涵蓋之一次性總結，及追溯維度之封閉

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/35_desc_closing_pass.md`
- 前一包：[34_leaf_realign.md](34_leaf_realign.md) ＋ [34a_flowchart_and_cutoff.md](34a_flowchart_and_cutoff.md)

---

## 一、34 包之覆核 —— **通過，兩項停止條件皆為正確觸發**

六條抄錄逐位相符；三處撤回之正文 SHA256 前後同值；TSV 48 列全帶值；
`-017`／`-018` 改掛後 batch 3 lint 32/32；`-024` 撤除且 `Splash Screen` = 3 leaf。

**三項特別記明**：

1. **§3.2 之翻案為本包最實質之所得** —— A-PMH25 之「不造值」前提
   （9.1 之權威文本於逾時處為破句）**被 037 之 DESC 推翻**：
   `within **the 60-second timeout** defined in the pop-up list, the system shall
   close the popup. If no other popups remain, the system shall shut off the radio.`
   **60 秒與其後二句皆完整。**
   其自評逐字為：**「我在 30 包看的是 SYS1，而該欄一直在 037 裡。」**
2. **§6 之偽陰自查** —— 寬鬆前綴比對把 `-016` 之 `60 秒` 讀成相符
   （`'0 seconds'` 之首詞命中 `'60-second'`），改精確集合差方測出。
   **「若我沒有改，本包會報『單位全數相符』。」**
3. **§13.1 之 `n_leaf` 未變（46）** —— `-024` 撤除減之為 TC 非 leaf
   （`-001-01` 仍有 `-025`）。該分辨正確。

---

## 二、迴圈之形狀 —— **問題不在這七處，在於維度是一次加一個**

| 輪 | 新增之追溯維度 | 其回頭作廢者 |
|---|---|---|
| 33 | `requirement_title` | batch 3（`-017`／`-018` 錯掛）、batch 4 |
| 34 | **`requirement_description`** | **batch 1（`-008`）**、batch 3（`-016`）、batch 4（`-026`） |
| 34 | **單位** | batch 3（`-016`）、batch 4（`-025`／`-032`） |

**batch 1 於 12 包覆核通過，此後十九輪未再以任何新判準重驗過。**

**而執行層 §12 第 2 項已指出其根源**：

> **037 之 DESC 是二包前才進到台帳的，在此之前所有基於「素材不足」之判斷
> 都沒有對照過它。**

**A-PMH25 即其一例，而沒有人知道還有幾例。**

**故本包不再加第四個維度，而是把 DESC 這一個維度做到底，然後封閉。**

---

## 三、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH133（DESC 為斷言完整性之權威）
037 之 `Requirement Description` 為**該 leaf 應被驗證之範圍**之權威。

**每一 leaf 之 DESC 所含之每一斷言，須被掛在該 leaf 之 TC 集合完整涵蓋。**
涵蓋之單位為**斷言**（R-PMH101 之切分），非 TC、非 ER 之條。

依據二項：
  canon §6 —— `Final ER covers the **complete** Test Item outcome`
               （partial = incomplete）；
  canon §8.2 —— RD（037）為「什麼構成一個需求單位」之權威。

**分工自此明定**：
  **DESC 決定「要驗什麼」**；
  **PDF／SYS1 決定「其措詞為何」**（`source_clause` 之來源，R-PMH50／R-PMH75）。

**二者衝突時**：DESC 缺而 PDF 有者 → 該內容無 leaf，依 R-PMH55(b) 不寫 TC
（`-024` 之形態）；DESC 有而 PDF 側為破句者 → **以 DESC 為準**
（A-PMH25 之形態，34 包 §3.2）。

**本條之回溯效力**：凡以「素材不足」「無法確定」「破句」為由而未斷言者，
**須逐項對照 DESC 重判** —— 其前提可能只在 SYS1 側成立。
```

```
R-PMH134（追溯維度之封閉）
TC 與其 leaf 之對應，其比對維度**封閉為三項**：

  (1) **leaf 指派** —— TC 所掛之 leaf 是否為其 DESC 所述之行為之 leaf；
  (2) **斷言涵蓋** —— 該 leaf 之 DESC 之每一斷言是否被涵蓋（R-PMH133）；
  (3) **單位** —— TC 所用之計次／計時單位是否與 DESC 逐字相同。

**自本包之總結完成後，不再新增第四個維度**，除非：
  (a) 某條已交付或已產出之 TC 經**實測**有誤，且該誤為上開三項所不能攔；或
  (b) Pei 裁定。

**其判別與 R-PMH104 同** —— 增加「檢查什麼種類的對應」者為封閉之標的；
既有三項對新批之適用不是。

**理由**：33、34 兩包各新增一個維度，各回頭作廢一批已通過之產出
（33 之 title 打到 batch 3／4，34 之 DESC 打到 batch 1／3／4，
34 之單位打到 batch 3／4）。**維度一次加一個，則每一批都會被作廢 N 次。**
**一次做完並封閉，其總成本低於逐次加。**
```

```
R-PMH135（因新判準而生之修正不計入輪數上限）
R-PMH120 之「每批覆核循環上限二輪」，其所計者為**產出面之覆核循環**
（同一判準下，產出有誤而重做）。

**因新立或新修之判準而回頭所生之修正，不計入該上限**，
其比照 R-PMH128（更正一個事實錯誤不是重做一批）。

**惟其須具名**：該次修正之上繳須載明「本次修正繫於哪一條新判準」，
不得以「重做」之名記之 —— 二者之意義不同：
前者是**判準變了**，後者是**做錯了**。

依據：`-016`／`-026` 之射程不足係 R-PMH133 之產物，
而 batch 3 已覆核通過、batch 4 已用滿二輪（34 包 §12 第 3 項，執行層自陳
「其輪數如何計，未定」）。
```

---

## 四、作業步驟

> **本包為一次性總結，其步驟數多而其後應顯著減少。**

1. **抄錄** —— §三之 R-PMH133 ~ R-PMH135 逐字抄入 `RULINGS.md`，附核對表。

2. **全 36 條之 DESC 逐斷言涵蓋表（R-PMH133，本包核心）** ——
   對每一 leaf：
   - 依 R-PMH101 將其 DESC 切為斷言（機器產生候選 ＋ 人讀複核）；
   - 逐斷言標其被哪一條 TC 之哪一條 ER 涵蓋，或標 **`未涵蓋`**；
   - **一 leaf 多 TC 者，其涵蓋為該 TC 集合之聯集**。

   **輸出為一張表，每列一個 DESC 斷言。** 已知之四處（`-016`／`-026`／
   `-008`／`-025`）應出現於其中，**若未出現則本表之切分有誤，停並回報**。

3. **「素材不足」類判斷之回溯重判（R-PMH133 末段）** ——
   掃 `ANOMALIES.md` 與四批之 `reasoning`，找出所有以
   「素材不足」「無法確定」「破句」「未載」「權威文本於該處」為由而未斷言者，
   **逐項對照 037 之 DESC 重判**。
   **A-PMH25 已翻，其餘未知** —— 本步即為求其數。
   **翻案者逐項具名，其原文依 R-PMH44 保留。**

4. **七處之修正** ——
   | # | 處置 |
   |---|---|
   | `-016` | 補三斷言：60 秒逾時、popup 關閉、radio 關機。**A-PMH25 改 `RESOLVED`** |
   | `-026` | 補二斷言：動畫被中斷、其後進入免責畫面 |
   | `-032` | 計次基準由 `ignition cycle` 改 **`CAN BUS wake-up`**；`ignition cycle` 降為前提 |
   | `-025` | **不改** —— 其 DESC 首句由 `-028` 承載而 `-028` 掛 `-006-01`，**其為 037 自身之重複**。登記為 A-PMH30（**只記現象，不判其為 037 之缺陷、不對 RD 提異議**） |
   | `-008` | **不改** —— `certain phone call scenarios` 未定義，**`DR-PMH8` 增 Q8**（形態同 A-PMH22：記法未定義）。其修正待答覆 |
   | batch 2 六條 | **只補具名**（R-PMH126 之形式要求），**不重做** —— 其陳述實質為真（34 包 §7.1 已逐條驗過） |
   | `-026`／`-033`／`-034` | `reasoning` 補引 **R-PMH131**（其「不斷言輪替順序」自此為裁定而非暫置） |

5. **修正後之全批重跑** —— 四批 lint、`--limit-must-hit`、
   `--final-step-must-hit`、`verdict_form`、granularity self-test。
   **依 R-PMH135，本次修正於上繳記為「繫於 R-PMH133」，不記為重做。**

6. **`DR-PMH8` 增 Q8** —— 其逐字：

```text
  Q8: SU6 and the related requirement both state that the disclaimer screen is
      displayed "unless certain phone call scenarios have occurred", without
      saying which scenarios those are. Could you list them? At present our test
      case for that requirement does not exclude any call scenario, because we
      do not know which ones to exclude.
```

   **狀態維持 `DRAFT`、`SENT` 欄留空。**

7. **`PENDING-ON-DR` 補一筆** —— `-008` 之例外未處理，繫於 `DR-PMH8` Q8。

---

## 五、停止條件

canon §0 六條，另加本包三條：

7. 步驟 2 之涵蓋表**未含**已知之四處（即其切分有誤）
8. 步驟 3 之回溯重判發現**任一**「素材不足」之判斷其前提只在 SYS1 側成立
   而**未被翻案**
9. 步驟 4 之修正後，任一 TC 之 procedure 與 ER 不再 1:1

**本包零寫回工作簿。本包未由分析層授權提交**（R-PMH65）。
**apparatus 維持凍結；追溯維度自本包總結完成後封閉**（R-PMH134）。
**不得改動 `scripts/new_feature.py`、`docs/runtime/`、任何他 feature 之檔案。**

---

## 六、上繳包要求（`docs/upstream/35_desc_closing_pass.md`）

1. §三三條之抄錄核對表（含命中數）
2. **步驟 2 之全 36 條 DESC 逐斷言涵蓋表** —— 每列一個斷言，
   標其涵蓋之 TC／ER 或 `未涵蓋`
3. **步驟 3 之回溯重判清單** —— 其母體規模、翻案數、逐項具名
4. 步驟 4 之七處修正 ＋ 修正後之 TC 全文
5. 步驟 5 之全批重跑輸出（**依 R-PMH135 記為「繫於 R-PMH133」**）
6. `DR-PMH8` 之 Q8（8 問，`DRAFT`）
7. `PENDING-ON-DR`（14 筆）
8. 由程式產生之檢查總表
9. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
10. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之揭露表

---

## 七、本包之後

**追溯維度封閉後，其餘工作為**：

| # | 項 | 估 |
|---|---|---|
| 1 | batch 5 —— `Power Off Behavior`(8) ＋ `Off Road Plus`(2) | 2 輪 |
| 2 | batch 6 —— `Voice Assistant Key`(5) | 2 輪 |
| 3 | Phase 5–7：`tc_id` 單次指派、寫回、Q10、profile 例外、交付 | 3 輪 |

**本包 ＋ 上表 = 約 8 輪。**

---

## 八、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **`DR-PMH8`（8 問 ＋ 更正句）之發出 ＋ 日期與對象** —— 其載 R-PMH112 之更正，未發出期間該不符持續存在 | 否 |
| 2 | 9.1 之 profile 例外；17 §5.4 其餘五項；Q10 | Phase 6／7 前 |

---

## 九、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §三 |
|---|---|---|
| R-PMH133 | DESC 為斷言完整性之權威；其回溯效力 | ✅ |
| R-PMH134 | 追溯維度封閉為三項 | ✅ |
| R-PMH135 | 因新判準而生之修正不計入輪數上限 | ✅ |

三條各管一事。**本包未新增任何檢查程式或檢查項**（符合 R-PMH104）。
