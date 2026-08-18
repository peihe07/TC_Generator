# 上繳 34 — 第四批 26 條落地（語料 134／leaf 125）

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`34_batch04_go.md`（**無裁決條文**）
- 另附：`docs/upstream/34_provenance5.md`（ER 出處對照）
  ＋ `docs/upstream/34_review_pack_26.md`（覆核用全文）
- **本輪未執行任何 git**；**未寫回工作簿**（R-U14）；**RD v2 未寄出**（Tier 3，屬 Pei）
- 語料：**108 → 134 條**；leaf 覆蓋 **100 → 125 / 180**

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | **134 條，違規 0** |
| `lint_tcs.py --self-test` | 64 / 64 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ **134 條違規 0** |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |
| `audit_consistency.py` | K-3 0／K-4a 0／W-1 4 待判／V-1 15 待判／U-2 0／U-1 6 待判／T-1 0／K-4b 0／Q-1 11 待判 |
| `audit_consistency.py --self-test` | **37 / 37**（＋1：K-4a v5）|
| `audit_variant_pairs.py` ／ `--self-test` | 違規 0 ／ 7 / 7 |
| `audit_delegation.py` ／ `--self-test` | **紅 0 ／ 黃 13** ／ 8 / 8 |
| `scan_override_notes.py --check` | 與 TSV 一致 |
| `lint_outbound_doc.py --self-test` | 8 / 8 |

```
全語料 priority：P0×37, P1×47, P2×44, P3×6   （P0 = 27.6%）
第四批 design_method：功能測試×15, 狀態轉換×5, 負向測試×4, 情境/用例×1, 邊界值×1
```

---

## 1. 條數之更正 —— **下放包沿用了我 29 輪之措辭錯誤**

34 包寫「25 leaf ＋ **2 額外造者**（`030-01` 反向、`041-04` 故障注入），估 26 條」。

**`041-04` 不屬本批**：它是 `5.13.2` 之 leaf，落在 `ALLPR` 群（**第五批**）；
且它本身就是一個 leaf，其 TC 是「一葉一 TC」，**不是額外造出來的一條**。

成因在我 **29 輪 §3.2** 之寫法：我把 `041-04` 與 `030-01` 之反向並列為
「另須額外造者」——**而前者只是一個需要故障注入之 leaf**。
故該處之「38 ＋ 2 ＝ 40」**多算了一條**；ch5 全章實為 38 ＋ 1 ＝ **39 條**。

**本批以 25 leaf ＋ 1 額外造者 ＝ 26 條執行** ——
與下放包所載之「估 26 條」及「5.1–5.10.1」之範圍**一致**，
只有「2 額外造者」那個標籤是錯的。`041-04` 之故障注入留待第五批。

---

## 2. 生成時被閘擋下者（**6 處，皆我方之錯**）

| 閘 | 處 | 成因 |
|---|---|---|
| G8（最終步無查核目標）| 4 | 我寫 `check which tab is shown`／`check the tone and message` —— **`check` 未接 `that`**，§5.5 之查核目標形態不成立。改為 `check that …` |
| G15（步驟字數）| 1 | 13 詞，縮寫後過 |
| G18（ER 字面值）| 1 | `TC-115` 之圖示字串溯不到 5.2 —— **該判定是對的**，見 §2.1 |

### 2.1 `TC-115` 之 G18 —— **判定正確，處置是補引用而非改寫**

5.2 之條文以**指涉**帶入 PRACC7.2 之字串
（`the icon and the string **described in note PRACC7.2**`），**未逐字重複**。
`TC-115` 之 ER 逐字寫出該字串，故 G18 判其溯不到 5.2 —— **正確**。

處置：`REF_EXTRA` 併列 **5.1.2**（**D-3／C-1 之同型第四例**，處置與前三例一致）。

**連帶發現**：`lint_tcs._ref_allowlist()` 原只讀
`gen_pilot`／`gen_batch01`／`gen_batch02` 三支之 `REF_EXTRA` ——
**第三、四批之登記讀不到**。已擴至五支，並以 `getattr` 容許無該表之批次
（第三批即無）。**若未擴，本批之併列會被 G17 判為未登記之多引** ——
即「補了引用反而更紅」。

---

## 3. 五支對應關係掃描（生成後即跑）

### 3.1 T-1（步驟 ↔ ER）與 U-2（其反向）：**各 0 處**

第四批之 26 條全數通過。**兩支為「紅」型掃描，0 即為結果**。

### 3.2 U-1（斷言 ↔ 分支）：本批新增 **3 處待判 → 逐條判為綠**

| tc_id | PU | 判 |
|---|---|---|
| `131`／`132`／`133` | PU0588 | **綠** |

PU0588 在 spec 內有兩句（5.10.1 與 9.6），**31 輪已判其為同一觸發被記載兩次**
（皆為「所存座椅不屬現用 profile」），非兩個分支。

且三條各自另有綁定：`131` 之 ER3 併述**詢問內容**、
`132`／`133` 之 ER3 併述**選 Yes 之後果**（座椅歸屬與 `“None”`）——
**一個顯示 PU0588 卻不執行改派之實作，`132`／`133` 不會通過**。

### 3.3 V-1（步驟 ↔ 條文時序）：本批新增 **2 處待判 → 逐條判為綠**

`115`／`116`（5.2）之 `before` 出現在 **PU0584 之 popup 文字內**
（`must first delete a Profile **before** creating a new one`）——
**那是畫面上要顯示的字，不約束測試順序**。
與 32 輪對 `TC-003`（同節）之判定一致。

### 3.4 W-1（前提 ↔ ER）：本批 **0 處新增**

第四批之 pre-condition 無一以完成式描述動作結果。

### 3.5 K-4a 之 3 處紅 —— **判準漏詞，非案例錯**

| tc_id | 動作 | 判 |
|---|---|---|
| `117`（5.3）| `Select the username of Driver Profile B` | 真狀態遷移（現用者 A→B）|
| `132`／`133`（5.10.1）| `save it to the memory seat linked to …` | 真狀態遷移（座椅連結歸屬改變）|

三者所改變者皆為**持續存在之狀態**，只是動作詞不在表內。
詞表補 `save` 與 `select … Driver Profile`；
**`open`／`read` 仍未收進來**，28 輪之護欄案例（純讀取仍須紅）不變，
並新增一條綠向（`save` 改變座椅歸屬）。

---

## 4. `audit_delegation` 之三處紅 —— **兩處我方措辭、一處閘本身之 bug**

### 4.1 兩處 D-1：`承擔` 一詞被誤用於 ER

`126`／`129` 之 reasoning 我寫「其成立本身**由 ER3 前半承擔**」——
**`承擔` 在本專案專指跨 leaf 之委派**，D-1 遂要求它指名 leaf id。
改為「其斷言**落在** ER3 前半」。**是我用錯詞，不是閘誤報。**

### 4.2 一處 D-3 —— **閘本身有 bug，且它讓 D-3 之判別力有一部分是意外得來的**

`TC-121` 之 remarks 引 5.4 之條文並委派 `SWE1-HMI-PROF-022`，
D-3 抽出之詞串為 `switch system that Profile` —— 而 5.3 之原文是
`switch system **to** that Profile`。

**成因**：`phrase_of` 只收 ≥4 字母之詞，
而 1–3 字母之詞（`to`／`the`／`not`／`of`）**既不收進詞串、也不當成斷點** ——
**於是詞串中間的短詞被靜靜地丟掉**，再拿去逐字比對節文，當然對不上。

**這件事的嚴重性不只是一次誤報**：22 包那個 D-3 要抓的案例
（`does not support the connected profile feature`）**之所以轉紅，
有一半是因為詞串被打斷**（`not`／`the` 被丟），不全是因為內容不符。
**它一直在為對的結論給錯的理由。**

**v4 修正**：短詞在詞串**已開始**時併入（保持連續），但不得作為詞串之起點。
修正後複驗：

- 22 包之案例**仍紅**（`does not support the connected profile feature`
  確實不在 11.3 之 `does not support connectivity` 內）——**這次是為對的理由**
- 其綠向案例仍綠；`TC-121` 轉綠
- 方向性 8 / 8，語料紅 0

---

## 5. 一項本輪發現、**未在本批處理**之既有問題

`TC-003`（`SWE1-HMI-PROF-021-01`，5.2）之 ER3 為：

> `The Add New Profile button is not present; **the icon and the string
> “This icon is associated…” are not present**; and **“Max Profiles reached.
> Delete to create a new one.” (PU0584) is displayed`

而 `021-01` 之 037 description 只有
`There can be up to five (5) Driver Profiles per vehicle, plus a Valet Mode
Profile.` —— **即「數目上限」**。

其 ER3 之後兩段分別是 **`021-02`**（按鈕與圖示消失）與 **`021-03`**（PU0584 文字）
之內容 —— 而那兩個 leaf 正是本批之 `TC-115`／`TC-116`。

**故現況為三條 TC 斷言同一組事實。** 依 D-UP24-01（description 為需求單位）
與 §8.2.1（一葉一 TC），`TC-003` 之 ER 越出了它自己的 leaf。

**本輪未改 `TC-003`。** 理由：

1. 它屬 **pilot 批**，已於 16 輪覆核並核可 —— 改動已核可之 TC 應由分析層裁示
2. 其 ER3 若收斂為「數目上限」，**其可觀察形式為何**需要判斷
   （「無法建立第 6 個」之觀察點恰恰就是「按鈕不見了」，即 `021-02` 之內容）
   —— **這不是機械改寫，是要決定 `021-01` 這個 leaf 該怎麼驗**

**建議**：下包裁示。在此之前，`115`／`116` 各自完整驗其 leaf，
**重複存在但不矛盾** —— 三條皆為真，只是失敗時無法區分是哪一條規則壞了。

---

## 6. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **`TC-003` 之 ER 越界** | **本輪發現，待裁** | §5 |
| 2 | **第四批 26 條未經覆核** | **分析層待辦** | 覆核用全文已同輪交出（`34_review_pack_26.md`）|
| 3 | **D-3 之 bug 修正前所產生之判定** | **已複驗** | §4.2 —— 22 包之案例與現行語料皆已重跑，結論未變 |
| 4 | **`TC-129` 之 popup 無 PU id** | note | 5.8 未給編號，ER 只述內容要旨；若 Pop Up List 補上得再補（同 DR #4 之形態）|
| 5 | **`018-02` 之「逐 profile 隔離」未驗** | **OUT-OF-SCOPE（R-U56）** | 條文有述而 037 未為其另切 leaf，**不列缺口**；已於該條 remarks 具名 |
| 6 | **V-1 15 處、U-1 6 處、W-1 4 處、Q-1 11 處、D-3 13 處黃** | 承前 | 本批新增者已逐條判（§3）|
| 7 | **`pending` 兩 axis 未兌現** | 待第六／七批 | 29 輪已具名其批次 |
| 8 | **RD v2 未寄出** | **待 Pei（Tier 3）** | |
| 9 | A-UP09／R-U14、DR #4、RD #5／#6、R-U17、N-XF01、A-UP10、A-UP11 | 承前 | 擋 Phase 6 寫回 |

---

## 7. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | **檔案新建** | `scripts/gen_batch04.py`（第四批生成器，含 `REF_EXTRA`）| 否 |
| 2 | **檔案生成 ×26** | `generated/`（`109`–`134`）| 否 |
| 3 | 檔案編輯 | `scripts/lint_tcs.py`（`_ref_allowlist` 擴至五支批次）| 否 |
| 4 | 檔案編輯 | `scripts/audit_consistency.py`（K-4a v5 ＋1 案）| 否 |
| 5 | 檔案編輯 | `scripts/audit_delegation.py`（**`phrase_of` v4：短詞不再被丟掉**）| 否 |
| 6 | **檔案新建** | `docs/upstream/34_batch04.md`（本檔）＋ `34_provenance5.md` ＋ `34_review_pack_26.md` | 否 |
| 7 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 8 | 程式執行 | 生成 ×1、全部閘、五支對應關係掃描、九支 audit／lint 之 `--self-test`、出處對照 | 否 |

**本輪未執行任何 git**：寫入性與唯讀皆無。
**RD 查詢單未寄出** —— Tier 3，屬 Pei。
**第五批未取樣** —— 待第四批覆核。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`、`DECISIONS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md`、`data/`、
`scripts/gen_pilot.py`、`gen_batch01.py`、`gen_batch02.py`、`gen_batch03.py`、
`gen_pairs.py`、`lint_variant_labels.py`、`render_spec_region.py`、
`build_batch_context.py`、`audit_variant_pairs.py`、`scan_override_notes.py`、
`lint_outbound_doc.py`、**他 feature 之任何檔**、`docs/runtime/profiles/`、`docs/fw036/`。
