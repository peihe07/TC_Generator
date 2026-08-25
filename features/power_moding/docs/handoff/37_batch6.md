# 下放包 37 —— `-004` ER3 之裁定、batch 5 之三項修正與 batch 6（最後一批）

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- 對應上繳：`features/power_moding/docs/upstream/37_batch6.md`
- 前一包：[36_batch5.md](36_batch5.md)
  （上繳 [../upstream/36_batch5.md](../upstream/36_batch5.md)）

---

## 一、36 包之覆核 —— **程序面通過，產出面三項須改**

三條抄錄逐位相符；`desc_coverage.py` 建成且其首跑即攔下人讀表之一筆筆誤；
must-hit 錨點 (1) 之偽陽自查並改真；正向 55 項／反向 144 項全表；
五批 lint 32/32；`-040` 之 PC 含 `Gear is not in Reverse`。

**兩項特別記明**：

1. **人讀表之筆誤由程式攔下** —— `-036` ER3 不存在（該條僅 2 條 ER），
   而 35 包之人讀表未攔，其自陳逐字為
   **「人讀表不會回頭去數 ER」**。**R-PMH138 解凍之價值於同輪兌現。**
2. **must-hit 錨點 (1) 之偽陽** —— 原判準為「輸出含 `016` 或 `ER4`」，
   而現況本就有一筆不可解析，**使錨點在未攔到任何東西時亦報 `True`**。
   其總結逐字：**「一個錨點在它所要攔的東西之外另有一個常在之失敗時，
   它會一直是綠的。」** 與 31 包之 `record`／`read` 同型 ——
   **判準太寬，而其寬處剛好被別的東西填滿。**

---

## 二、`-004` ER3 —— **裁（乙）**

執行層提二路而未自行改，並自陳
**「`-004` 之 DESC 以 `Exception:` 起首，其在文義上就是 `-001-04` 之例外，
故 (乙) 有其道理；惟 R-PMH136 現行條文不容許之。」**

**採（乙）。該句本身即為理由**：例外條款不重述其本體之後續行為，
為規格書寫之常態；**刪去 ER3 將使該條無可觀察之離開路徑**
（其 procedure 之終點成為「按下 Accept」而無結果，違 §5.5）。

→ R-PMH139。

---

## 三、batch 5 之人讀覆核 —— **三項**

### 3.1 【嚴重】`-045` 之 priority 與其自述矛盾

| | |
|---|---|
| `pri` 欄 | **P1** |
| 其「軸」註逐字 | `等價類：緊急呼叫鍵之電源回復（**本批唯一之 P0**）` |

**同一條之內，依據寫 P0 而級別填 P1。**

**且 P0 為正解**：canon §10.2 之 P0 明列 `safety`／`eCall`；
`PITA10: SOS and ASSIST can turn head unit power back on` 即緊急呼叫之電源回復。

→ **改 P0**。**其形態為 R-PMH59 之自套**（依據與級別互相矛盾），
惟 R-PMH59 所規之範圍為「批內各 TC 之間」，**本處為一條之內** —— 見 R-PMH141。

### 3.2 【中】`-042`／`-045` 之許可式

| tc | `source_clause` 逐字 | 其 ER |
|---|---|---|
| `-042` | `PITA9: Phone call popups **can** be displayed over Power Button Off state.` | `The phone call pop-up **is** displayed …` |
| `-045` | `PITA10: SOS and ASSIST **can** turn head unit power back on.` | `The head unit power turns back on …` |

**`can` 為許可式** —— 其保證該行為之**容許**，不保證其**必然發生**。

**執行層判「不值再增一問」（`DR-PMH8` 已八問）—— 該判斷正確，本包裁認之**，
惟其須留在紙上。→ R-PMH140。

### 3.3 【輕】兩處補寫

| 處 | 補 |
|---|---|
| `-040` | 其二後果依 §5.7 不拆之理由**未寫**（`-039` 寫了）。補寫，並記 §8.2.2 壓力測試不觸發之理由 |
| `-044` | `hard control` 一路未驗，其「與 soft control 同結果故不拆」**為推定，規格未言其實作為同一路徑**。**具名為推定並登記覆蓋缺口**，**不補條** |

### 3.4 其餘七條通過

`-038`～`-039`／`-041`／`-043`／`-046`／`-047` 逐項合格；
`-047` 之 Mute 限定依 R-PMH94 逐斷言導出且已具名；
`-046` 之 PC 含 `The vehicle is in Off Road state` —— **20 包 §三所指之
`OFF1.)` 條件句已被正確納入**。

---

## 四、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH139（例外條款之依據得取其本體 leaf）
某 leaf 之 DESC 以例外標記起首（`Exception:`／`unless`／`except`／
`Exception for`），且其**本體 leaf 可資辨識**者，
其 TC 之 ER 得以**本體 leaf 之 DESC** 為依據，
**不計為 canon §8.4.2 之範圍捏造**（R-PMH136 之反向涵蓋於此不報 `無依據`）。

**其條件二項**：
(a) 該 ER 所斷言者須為**本體 leaf 已載之行為**，非新增之行為；
(b) `reasoning` 須**具名其本體 leaf**，使追溯可循。

現行適用：`-004`（leaf `-001-05`，DESC 為
`**Exception:** For Maserati applications, the system provides no timeout
(per CFTS009); the user must manually press Accept.`）之 ER3
`The disclaimer screen is removed and the last mode screen is displayed`
—— 其依據為本體 leaf `-001-04` 之 `press Accept to go directly to last mode screen`。

**不採（甲）刪去 ER3 之理由**：例外條款不重述其本體之後續行為，
為規格書寫之常態；刪之則該條之 procedure 終於「按下 Accept」而無結果，
**違 canon §5.5**（Final Step 須持有可觀察之驗證標的）。
```

```
R-PMH140（許可式之斷言處置）
`source_clause` 以許可式書寫者（`can`／`may`／`is able to`），
其保證該行為之**容許**，不保證其**必然發生**。

其 ER 之寫法：**以「於本條所述之條件下實測其發生」為之**，
**並須於 `reasoning` 具名三事**：
(a) 其來源為許可式；
(b) 本 TC 所驗者為「於該條件下該行為確實可發生」；
(c) **其不發生不必然為缺陷** —— 判 fail 前須先確認該條件確已成立。

**不另開 DR** —— 許可式為規格之常見書寫，非未定義之記法；
其與 A-PMH22（`Else: Mute Active` 之記法未定義）不同類。
**採認執行層 36 包 §10 第 4 項之判斷（「不值再增一問」），本條使其成為裁定。**

現行適用：`-042`（`PITA9: Phone call popups **can** be displayed …`）、
`-045`（`PITA10: SOS and ASSIST **can** turn head unit power back on.`）。
```

```
R-PMH141（priority 之依據與級別須於同一條之內相符）
R-PMH59 所規之「priority 依據須批內互不矛盾」，**擴及一條之內**：
該 TC 之 `priority` 欄之值，須與其 `reasoning`／軸註中所載之依據相符。

**檢查方式**：凡 `reasoning` 或軸註中出現 `P0`／`P1`／`P2`／`P3` 之字樣者，
其與 `priority` 欄比對；不符即 FAIL。**此項不可機械涵蓋於現行 lint
（apparatus 凍結，R-PMH104），故列為人讀覆核之必查項。**

依據：`-045` 之 `priority` 欄為 `P1`，而其軸註逐字為
`等價類：緊急呼叫鍵之電源回復（**本批唯一之 P0**）` ——
**同一條之內，依據寫 P0 而級別填 P1**；
且 P0 為正解（canon §10.2 之 P0 明列 `safety`／`eCall`）。
```

---

## 五、作業步驟

1. **抄錄** —— §四之 R-PMH139 ~ R-PMH141 逐字抄入 `RULINGS.md`，附核對表。

2. **`-004` 之處置（R-PMH139）** —— ER3 **維持**；
   `reasoning` 具名其本體 leaf `-001-05` → `-001-04`；
   `desc_coverage` 之反向須自 `無依據 1` 降為 **`無依據 0`**
   （其判定改為 `例外-本體`）。

3. **batch 5 之三項修正（§三）** ——
   (a) `-045` 之 `priority` 改 **P0**；
   (b) `-042`／`-045` 之 `reasoning` 依 R-PMH140 具名三事；
   (c) `-040` 補不拆之理由；`-044` 之推定具名並登記覆蓋缺口。
   **修正後重跑五批 lint。**

4. **batch 6 之產出 —— `Voice Assistant Key`（ch 11，5 leaf）** ——
   `-026-01`～`-026-05`（outline 11.1，`VRLP1`）。

   **四項拘束**：
   (a) `source_clause` 取自 **PDF**，`origin` = `spec_pdf p{n}`；
   (b) **產出後即跑 `desc_coverage`（正向＋反向）**，不待下一輪；
   (c) 依 R-PMH94／R-PMH97／R-PMH101 逐斷言導出限定，
       **依 R-PMH126 逐條具名，不得樣板**；
   (d) ch 11 × 矩陣已於 22 包全對照（**牴觸 0**，`VRLP1` × `r11`／`r12`／
       `r28`／`r29`）—— **其結果得直接引用，不重跑**。

   `tc_id` 續 provisional；**零寫回工作簿**。

5. **36 §10 第 1、2 項之登記（不作業，只登記）** ——
   反向表 117 項之高重疊依據未逐項人讀、`測試執行` 26 項之分類為單一正規式，
   二者依 R-PMH103 入 `DECISIONS.md` 之 KNOWN-INCOMPLETE，**各附風險陳述**。
   **本輪不處理** —— 其為精化項，不指向產出可能有錯。

---

## 六、停止條件

canon §0 六條，另加本包三條：

7. 步驟 2 後 `desc_coverage` 之反向 `無依據` **≠ 0**
8. batch 6 之 `desc_coverage` 有任一 `無依據` 或 `未涵蓋-部分`
9. 步驟 3(a) 後，五批之 priority 有任一條其 `reasoning` 所載級別與其欄值不符
   （R-PMH141 之全批自套）

**本包零寫回工作簿。本包未由分析層授權提交**（R-PMH65）。
**apparatus 維持凍結；追溯維度維持封閉為三項。**
**不得改動 `scripts/new_feature.py`、`docs/runtime/`、任何他 feature 之檔案。**

---

## 七、上繳包要求（`docs/upstream/37_batch6.md`）

1. §四三條之抄錄核對表（含命中數）
2. `-004` 之 `reasoning` ＋ 反向 `無依據 0` 之輸出
3. batch 5 三項修正後之 TC 全文 ＋ 五批 lint
4. **batch 6 之 5 leaf、其 TC 全文、`source_clause`、`desc_coverage`（正反）**
5. 步驟 5 之 KNOWN-INCOMPLETE 二項
6. 由程式產生之檢查總表
7. 未結 DR 清單
8. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 不得省略
9. 建議之 commit 訊息與 pathspec（**不執行**）＋ R-G6 之揭露表

---

## 八、本包之後 —— **TC 產出完畢，只剩交付**

batch 6 完成後，48 leaf 之處置全數確定：

| 類 | 數 |
|---|---|
| 有 TC 之 leaf | **45** |
| 停手（`-002`／`-023`／`-028`） | 3 |
| **TC 總數** | **約 52 條** |

**其後為 Phase 5–7**（約 3 輪）：
`tc_id` 單次指派 → 寫回工作簿（`check_write_back` 三項首次接線）→
Q10（`Product Document` 分頁）→ profile 之 9.1 例外 →
交付揭露清單（R-PMH132(b)：`PENDING-ON-DR` 14 筆 ＋ 停手 3 筆 ＋ A-PMH30 二例）。

---

## 九、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **`DR-PMH8`（8 問 ＋ 更正句）之發出 ＋ 日期與對象** —— **其為唯一仍在你手上者** | 否 |
| 2 | 9.1 之 profile 例外；Q10；17 §5.4 其餘五項 | **Phase 6／7 —— 即下下輪** |

---

## 十、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §四 |
|---|---|---|
| R-PMH139 | 例外條款之依據得取其本體 leaf | ✅ |
| R-PMH140 | 許可式之斷言處置；不另開 DR | ✅ |
| R-PMH141 | priority 之依據與級別須於同一條之內相符 | ✅ |

三條各管一事。**本包未新增任何檢查程式或檢查項**（符合 R-PMH104）。
