# 上繳 35 — X-1 跨節 popup、X-2 受檢畫面之指名、review pack 拆檔

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`35_review_batch04.md`（**無裁決條文**）
- 另附：`docs/upstream/35_review_pack_26a.md`（`109`–`121`）
  ＋ `35_review_pack_26b.md`（`122`–`134`）
- **本輪未執行任何 git**；**未寫回工作簿**；**RD v2 未寄出**（Tier 3，屬 Pei）；
  **第五批未取樣**
- 語料：**134 條，未變動**（本輪修改其中 2 條）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 134 條，**違規 0** |
| `lint_tcs.py --self-test` | 64 / 64 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ 134 條違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |
| `audit_consistency.py` | K-3 0／K-4a 0／**X-1 6 待判**／W-1 4 待判／V-1 15 待判／U-2 0／U-1 7 待判／T-1 0／K-4b 0／Q-1 11 待判 |
| `audit_consistency.py --self-test` | **40 / 40**（＋3：X-1）|
| `audit_variant_pairs.py` ／ `--self-test` | 違規 0 ／ 7 / 7 |
| `audit_delegation.py` ／ `--self-test` | 紅 0 ／ 黃 13 ／ 8 / 8 |
| `scan_override_notes.py --check` | 與 TSV 一致 |
| `lint_outbound_doc.py --self-test` | 8 / 8 |

---

## 1. X-1 —— `TC-128` 之修正

### 1.1 下放包之診斷成立

`TC-128`（`030-02`，5.7 末句）之步驟 2 存座椅位置到**非現用 profile 所連**之座椅
—— **那正是 5.10.1 之觸發條件**。原 procedure 完全沒提 PU0588，
測試者會撞上未預期之 popup，**而結果取決於他按了什麼**：
選 Yes 則該座椅**就會**連到 A，與 ER3 相反。

**「兩條條文並不衝突，衝突的是 TC 之寫法」這句判定是對的** ——
5.7 之 `not **automatically**` 為「不經詢問即發生」，
5.10.1 為「問過且答 Yes 才發生」。

### 1.2 修正

| 欄 | 後 |
|---|---|
| 步驟 3（新增）| `Select No on PU0588` |
| ER2 | `… and **PU0588 is displayed**` |
| ER3（新增）| `No is selected on PU0588` |
| ER4 | `No memory seat is linked to Driver Profile A` |

**ER2 併驗 popup 出現**，而非只在 procedure 裡按掉它 ——
否則「該詢問是否真的發生」未被斷言，而它正是 5.7 與 5.10.1 之接縫。

引用欄併列 **5.10.1**（`REF_EXTRA`）：PU0588 之字面值出現於本 TC，
依 J-10 須登記其來源節。

---

## 2. X-1 之全批自檢 —— **判準 v1 得 60 處，等於沒有範圍**

### 2.1 v1 之失敗

依下放包所提之判準（TC 動作字串與 popup 觸發條件比對），
我先以「觸發句關鍵詞與 procedure 重疊 ≥3」實作，得 **60 處**。

逐條看，絕大多數只是**主題重疊**：

> `NR1L-UserProfiles-047 (12.2) 可能觸發 PU0832 —— 共同詞：mode, valet, vehicle`

**一份 60 筆的待判清單不是縮小範圍，是噪音** ——
而噪音清單會被略過（R-G9 之立條理由）。

### 2.2 v2：登記表式

逐個 popup 登記其**觸發動作**之 regex 與**成立條件**，**兩者皆命中**方列待判：

| popup | 觸發動作 | 成立條件 |
|---|---|---|
| PU0588 | 存座椅位置 | —（「非現用」為語意，留待人判）|
| PU0584 | 建立 profile | 已達五個上限 |
| PU0091 | 按 Valet 鍵 | 行車中 |
| PU0832 | 進入 Valet 之提示 | 車輛具手套箱鎖 |
| PU0934 | 自主機嘗試退出 | SPAAK 情境 |
| PU0118／PU0626／PU0833／PU0580 | 各自之動作 | — |

**成立條件是關鍵**：v1 把 `TC-047`（靜止中按 Valet 鍵）判為可能觸發 PU0091
（其觸發為**行車中**）—— 加上條件後即消失。

得 **7 處**（修正 `TC-128` 後為 **6 處**）。

### 2.3 六處逐條判 —— **無進一步缺陷**

| tc_id | popup | 判 |
|---|---|---|
| `004`（5.9）| PU0588 | **綠 —— 觸發不成立**：其步驟 3 明寫 `Leave the memory seat set and save controls **untouched**`，**根本沒有存**。regex 誤匹配 `memory seat set and save controls` 這個**名詞片語** |
| `130`（5.10）| PU0588 | **綠 —— 觸發不成立**：其 pre-condition 使**現用者即該座椅之連結者**，而 5.10.1 之觸發要求存到**非現用** profile 所連之座椅。**那個 pre-condition 是刻意設的** |
| `108`／`117`／`119`／`120` | PU0580 | **綠 —— 見 §2.4** |

### 2.4 一條分類判準：**該 popup 是否要求一個會改變結果之決定**

四條切換 profile 之 TC 確實可能看到 PU0580（welcome popup），
但它與 PU0588 **不同類**：

| | PU0588 | PU0580 |
|---|---|---|
| 型態 | **決策型**（Yes／No）| 資訊型 |
| 不處理之後果 | **答案改變結果** —— 座椅連到 A 或不連 | 自行消失（5.3.1 載明 5 秒），**不改變任何斷言** |
| 判 | 必須處理 | 不必處理 |

**故 X-1 之真正判準不是「會不會跳 popup」，是「跳出來之後測試者是否必須做一個會改變結果的決定」。**
已寫入該掃描之 docstring。

**殘留（R-G11）**：PU0580 出現期間會**短暫遮蔽畫面**；
四條 TC 之讀取步驟皆在其後，故不影響判定 —— **但那是我讀出來的，不是閘驗的**。
另 5.3.1 之 `(if turned on for that Profile)` 使其出現與否取決於未指定之設定，
**四條 TC 皆未指定該設定**；本輪未改（改動涉及跨兩批之四條 TC，
且其結果不受影響），**具名待裁**。

---

## 3. X-2 —— `TC-134` 之受檢畫面

| 欄 | 前 | 後 |
|---|---|---|
| 步驟 2 | `Attempt to link … **from outside the “Edit Profile” screen**` | `Attempt to link the memory seat position **from the “All Profiles” tab and from vehicle settings**` |

**「outside」不是一個測試者能執行的位置** —— 下放包之判定成立。
比照 `NR1L-UserProfiles-047` 之作法：逐一指名實際受檢之畫面。

reasoning 另加：

> 「Edit Profile 以外」之位置**不可窮舉** —— 本條取兩個最可能提供該操作者，
> **未涵蓋之其他入口，其結果不由本條保證。**

remarks 亦註明受檢之兩個畫面**為抽樣，非窮舉**。

---

## 4. 作業 3 —— review pack 拆為兩檔

| 檔 | 範圍 | 條數 | 行數 |
|---|---|---|---|
| `35_review_pack_26a.md` | `109`–`121` | 13 | 328 |
| `35_review_pack_26b.md` | `122`–`134` | 13 | 328 |

兩檔各自完整（含 spec 原文、must_carry、037 description、九欄與 reasoning），
檔首互相指路，並載明**本輪已修正之二條（`128`／`134`）之內容為修正後之現況**。

**下放包之自陳照收**：分析層之單輪讀取量有上限，而 34 輪之單一長檔（26 條）
未能一輪讀完。**該上限我方無從得知，故此後之 review pack 一律拆至
每檔 ≤ 13 條**；若下包認為仍過長，請給一個具體條數。

---

## 5. 獨立判斷 —— 本包是否仍有該驗而未驗者

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **X-1 之登記表為人工** | **判準盲區** | 32 個 popup 中只登記了 9 個（有動作型觸發者）。**未登記者，本掃描看不見** —— 其餘多為狀態型觸發（如 6.1 之 `PU0575`／`PU0576`），但那是我判的，未逐條驗 |
| 2 | **PU0580 之四條未指定其開關** | **具名待裁** | §2.4 —— 結果不受影響，但其出現與否取決於未指定之設定 |
| 3 | **`TC-003` 之 ER 越界** | 承 34 輪，**待裁** | 三條 TC 斷言同一組事實 |
| 4 | **第四批 26 條之覆核仍未完成** | **分析層待辦** | 已讀 11（`124`–`134`），未讀 15（`109`–`123`）。**拆檔後之兩檔與該進度不對齊** —— `26a` 含 `109`–`121`（皆未讀）、`26b` 含 `122`–`134`（其中 `124`–`134` 已讀）。**下一輪讀 `26a` 即可補齊未讀之 13 條中的 13 條**，餘 `122`／`123` 在 `26b` 之首 |
| 5 | **V-1 15／U-1 7／W-1 4／Q-1 11／D-3 13 黃** | 承前 | 本批新增者已於 34 輪逐條判 |
| 6 | **`pending` 兩 axis** | 待第六／七批 | 29 輪已具名批次 |
| 7 | **RD v2 未寄出** | **待 Pei（Tier 3）** | |
| 8 | A-UP09／R-U14、DR #4、RD #5／#6、R-U17、N-XF01、A-UP10、A-UP11 | 承前 | 擋 Phase 6 寫回 |

### 5.1 一項關於本輪判準之觀察

X-1 之 v1（60 處）與 30 輪 T-1 之 v1、31 輪 U-2 之 v1 同型 ——
**都是「找得到相關字就算命中」**。三次之修法也同型：
**把「相關」換成「該動作／該物／該條件確實成立」**。

差別在本輪之修法用的是**登記表**而非更聰明的正則 ——
因為觸發條件（「非現用 profile 所連之座椅」）**本來就不是字串比對得出來的**。
**登記表之代價是它要維護；其好處是它的盲區可以被列出來**（§5 第 1 項）。

---

## 6. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | 檔案編輯 | `scripts/gen_batch04.py`（`TC-128` 之 procedure／ER／remarks／reasoning 與 `REF_EXTRA`；`TC-134` 之步驟 2／remarks／reasoning）| 否 |
| 2 | 檔案編輯 | `scripts/audit_consistency.py`（**X-1 掃描（登記表式）** ＋3 方向性案例）| 否 |
| 3 | 檔案重生成 ×26 | `generated/`（batch04；**內容變動者 2 條**：`128`／`134`）| 否 |
| 4 | **檔案新建** | `docs/upstream/35_review_fixes4.md`（本檔）＋ `35_review_pack_26a.md` ＋ `35_review_pack_26b.md` | 否 |
| 5 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 6 | 程式執行 | X-1 之 v1／v2 各一次、生成 ×1、全部閘、九支 audit／lint 之 `--self-test` | 否 |

**本輪未執行任何 git**：寫入性與唯讀皆無。
**RD 查詢單未寄出** —— Tier 3，屬 Pei。
**第五批未取樣** —— 待第四批覆核完成。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`、`DECISIONS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md`、`data/`、
`scripts/gen_pilot.py`、`gen_batch01.py`、`gen_batch02.py`、`gen_batch03.py`、
`gen_pairs.py`、`lint_tcs.py`、`lint_variant_labels.py`、`render_spec_region.py`、
`build_batch_context.py`、`audit_variant_pairs.py`、`audit_delegation.py`、
`scan_override_notes.py`、`lint_outbound_doc.py`、**他 feature 之任何檔**、
`docs/runtime/profiles/`、`docs/fw036/`。
