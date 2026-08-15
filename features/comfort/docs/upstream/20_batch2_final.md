# 20 — Comfort HMI / 批次 2 定案：-024 拆四、兩個 gate、三則 anomaly

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 30（內容覆核）＋ 31（gate 授權、anomaly、第十軸前瞻）
- 結果：`-024` 拆為四條，Tri-Mode Climate **14 leaf → 17 TC**，全 feature
  **28 leaf / 31 TC**。lint **37/37 PASS，0 finding**。**未寫回 workbook。**

---

## 1. R-C31 貼入

`RULINGS.md` 現有 **33 個**逐字條文區塊。R-C31 前附一段來源說明，
指向上繳 18 §5.1 —— 我當時自陳「本包最可能被推翻者」，覆核維持並立為條文。

---

## 2. `-024` 拆為四條 —— 我的不拆判斷被推翻，三處說明

### 2.1 我錯在哪裡（照 30 §1 逐項）

**（a）把「條件」讀成「許可」。** 我寫「§8.2.2 允許 RD sub-id ≠ TC count，
**允許不等於要求**」，漏了同條後半：`different control entities → split
into independent TCs`。那不是許可，是判準；溫度／RECIRC／mode／MAX DEF 鍵
為四個不同控制實體，且我自己在 18 §4.2 就寫了「改溫度會破壞而改 RECIRC
不破壞，是可能的」—— **兩個條件我都陳述了，卻沒有把它們接上判準。**

**（b）把 locatability 當成 §8.3 的判準。** 我以「編號 ER 保證定位性，
第 4 行失敗即知是 RECIRC 那一路」為理由。§8.3 問的是 **pass/fail verdict
是否明確**，不是失敗報告的粒度。四個獨立行為共用一個 verdict，
fail 只有一個意思：「其中某項壞了」。

**（c）同批的不一致是最直接的證據，而我看著它寫下了不拆。**
A/C、AUTO、MAX A/C 三個破壞源各自成條（`-021`／`-022`／`-023`），
只因 037 各給一個 leaf；溫度／RECIRC／mode／再按 MAX DEF 性質完全相同，
只因 037 併在一個 leaf 就變一條。**我在 18 §4.2 把四者與前三者並列描述過，
卻沒問「那為什麼前三個是三條」。**

### 2.2 拆後四條

| tc_id | tc_title（帶破壞源 token）| 步/ER | design_method |
|---|---|---|---|
| -024 | Changing the temperature breaks MAX DEF | 2/2 | **狀態轉換** |
| -025 | Changing RECIRC breaks MAX DEF | 2/2 | **狀態轉換** |
| -026 | Changing the mode distribution breaks MAX DEF | 2/2 | **狀態轉換** |
| -027 | Pressing MAX DEF again breaks MAX DEF | 2/2 | **狀態轉換** |

四條 `req_id` 皆為 `SWE1-HVAC-024-07`，`split_flag` 皆為真，
`split_reason` 逐條具名 §8.2.2 之控制實體判準（**寫在每一列上**，
使拆分於工作簿內即可辨讀，不必回查生成器）。

**`design_method` 由「決策表」改為「狀態轉換」** —— 拆前為四條件之決策表，
拆後各為單一狀態遷移，§12 之 tie-break 於此翻轉。**這不是順帶的欄位更新：
若沿用決策表，欄位會宣稱一個拆分後已不存在的結構。**

### 2.3 `-028`（風速不破壞）之 negative 配對

維持一條。`reasoning` 更新為：

> -08（風速改變不破壞）維持一條，其 §7 negative 配對對象為**拆後之四條
> 全體，非其中任一條**。

配對關係若只掛在其中一條，另三條就變成沒有負向對照的正向斷言。

### 2.4 新舊 `tc_id` 對照表

| 舊 | 新 | req_id | 說明 |
|---|---|---|---|
| -015 … -023 | -015 … -023 | 023-01 … 024-06 | **未動** |
| **-024** | **-024** | 024-07 | 溫度（拆分第 1 條）|
| — | **-025** | 024-07 | RECIRC（**新增**）|
| — | **-026** | 024-07 | mode distribution（**新增**）|
| — | **-027** | 024-07 | 再按 MAX DEF（**新增**）|
| -025 | **-028** | 024-08 | 風速不破壞（順移 +3）|
| -026 | **-029** | 025-01 | 3.3 可用（順移 +3）|
| -027 | **-030** | 025-02 | 3.3 不可用（順移 +3）|
| -028 | **-031** | 026 | 3.4 按鈕不出現（順移 +3）|

**內容未變而編號改變者為後四條**（舊 -025…-028）。其 `req_id` 是穩定的
識別，`tc_id` 不是 —— **凡以 tc_id 引用過這四條之既有文件（上繳 18／19），
其引用自本包起失效**。上繳 19 §2 之表所列 `-026`／`-027`／`-028`
即現在的 `-029`／`-030`／`-031`。

其餘 10 條不受影響，未重跑內容。

---

## 3. `-019` 維持一條 —— 判斷通過，並記入 RUNBOOK

30 §2 引 §5.7 確認：一個 trigger 之七個必然後果屬同一 TC。

`RUNBOOK.md` 新增一節，把 `024-02` 與 `024-07` 寫成對照表 ——
**同一節、同一 parent、外觀相近，拆與不拆方向相反**：

| | `024-02` | `024-07` |
|---|---|---|
| 結構 | 一個 trigger → 七個 outcome | 四個 trigger → 同一個 outcome |
| 判準 | §5.7 | §8.2.2 控制實體 |
| 處置 | 一條 | 四條 |

「拆成七條會產生 spec 不存在的區別，而每條都要重按一次 MAX DEF ——
那是**測試設計上的重複，不是需求上的區別**」逐字寫入，
連同 §2.1 之三處錯誤診斷。

---

## 4. gate —— 35 → 37，另有一項既有 gate 改判

### 4.1 `forbidden-verb`（31 §1）

比對 `test_procedure` 每一步之**行首主動詞**與 §5.1 之九詞 ＋ `locate`。

**不以字串包含判定**：regex 錨定於步號之後
（`^\s*\d+\.\s*(verb)\b`，multiline），故目的子句內之 `verify` 不受影響。

**反向驗證（兩個方向 —— 這個 gate 有兩種壞法）**：

| 注入 | 期望 | 實測 |
|---|---|---|
| `2. Verify the front defrost control label …` | FAIL | **FAIL** —— 指名 `-018` 與該步全文 |
| `2. Read the front defrost control label **to verify that** MAX DEF replaced it` | PASS | **PASS**（37/37）|

第二個方向與第一個一樣重要。31 §1 寫「**誤殺會促使作者繞過 gate 而非
改正**」——若合法用法被擋，下一個人會把 `to verify that` 改寫成別的字
以求綠燈，而那個改寫不會讓任何東西變得更正確。

### 4.2 `er-subject-net`（31 §2）—— 輸出自稱補網

比對四詞組 `is recorded`／`is readable`／`is noted`／`can be read`。
輸出：

```
- PASS — er-subject-net (a safety net, not the criterion; the criterion is §6
  and is human-reviewed)
```

**通用 gate 迴圈中之該行已抑制**：原本會同時印出
`- PASS — er-subject-net` 與上面那行，**兩行並列即等於兩個等價的宣稱**，
正是 31 §2 禁止的印象。現在只印自稱補網的那一行。

**§9 第 10 項之依據未引用本 gate**（見 §7），仍為逐行讀 ER。

**反向驗證**：把某 ER 首行改為 `The climate state is recorded` →
FAIL 並指名 `-029`，訊息內含「passing it does not mean the ER subjects
were checked」。

### 4.3 `req-id-unique` 改判 —— 未經授權但無此不可

拆分使四條共用 `SWE1-HVAC-024-07`，原 gate 直接 FAIL。

**未採之作法**：拿掉唯一性檢查。那會讓「宣告過的拆分」與「複製貼上的
意外重複」在 id 欄裡長得一模一樣，而後者正是該 gate 存在的理由。

**採用之作法**：重複合法，**但條件是每一列都宣告了拆分**：

- 有任一列未設 `split_flag` → FAIL（未宣告之重複）
- 全部設了但有一列 `split_reason` 空白 → FAIL（宣告了但沒說理由）

**反向驗證（兩項）**：

| 注入 | 實測 |
|---|---|
| 四條中一條 `split_flag: False` | FAIL — `appears on 4 TCs but ['NR1L-ComfortHMI-024'] do not set split_flag` |
| 四條皆宣告但一條 `split_reason: ""` | FAIL — `is split 4 ways but a row has an empty split_reason` |

**這一項是 30 §1.4 之必然後果而下放包未提**，我判為非做不可（否則拆分
無法通過 lint），故做了並列此回報。若分析層認為 gate 改判須另裁，
它是本包唯一一處逾越授權範圍者。

### 4.4 gate 清單現況

37 項：既有 35 ＋ `forbidden-verb` ＋ `er-subject-net`。
`req-id-unique` 為既有 gate 之判定改寫，不計入增量。

---

## 5. 三則 anomaly

| 編號 | 類別 | 現象 | 狀態 |
|---|---|---|---|
| **A-CF17** | 條文缺口 | `3.4` 之 `when configured` 無受詞 | OPEN，**RD-1 候選** |
| **A-CF18** | 條文缺口 | `3.3` 未定義 `not available` 之可觀察形態 | OPEN，**RD-1 候選** |
| **A-CF19** | 交付件呈現 | 多節 `spec_ref` 之儲存格呈現未測 | OPEN（下次寫回時實測）|

A-CF17 之條目含 R-C30 之搜尋範圍與三處 `configured` 之對照表
（3.4 無受詞／6.3 與 11.11 皆為 `configured with X`）。

A-CF19 之條目寫明它與 A-CF16 之關係：

> **本欄比當時量測過的任何一欄都長**（約 240 字元），故它可能是 A-CF16
> 重審條件之第一個觸發者。

**登記過程本身值得一報**：加完 `forbidden-verb` 兩個 gate 後跑 lint，
`anomaly-id-registered` **主動指名 A-CF17／A-CF18／A-CF19 未登記，
並指出首見於 `docs/handoff/31_gates_anomalies.md`** —— 下放包一進 repo，
gate 就開始要求對應的登記。這是它上線後第一次抓到真的東西。

---

## 6. `-030` 之 reasoning ＋ 第十軸逐節規則

### 6.1 `-030`（原 `-027`）

原 reasoning 已具名 2.10 擁有「grey out」之視覺處置。**依 31 §3.2 補一句
更精確的**，因為「擁有 grey out 之描述」與「擁有 not available 之外觀定義」
不是同一件事：

> **「not available」之可觀察外觀由 2.10 擁有，本節未定義**，故其 ER
> 停在該詞而不描述外觀（A-CF18）。

### 6.2 第十軸逐節判定規則

寫入 **profile §3.2 第十軸說明段**與 **`RUNBOOK.md`**，兩處內容一致：

> 全 129 節掃 `rear defrost` 命中 **8 節、42 leaf**。
> **「提及 rear defrost」不等於「需要 rear defrost 有無之 PC」。**
> `Climate Modes`（2.9／2.10）與四個 ICS 組（16.4／16.8／16.9／16.10）
> 生成時，凡欲寫入本軸之 PC 者，一律逐節走 **R-C28 三問 ＋ R-C31**，
> 第一問須具名**該節自身**之條文相關句。
> **不得以 3.4 之句子為所有節之出處** —— R-C29 允許跨節取據，但要求具名
> **實際**出處。

RUNBOOK 版另加一句：**一條允許跨節的規則若被讀成「一句話可覆蓋全語料」，
它就從追溯機制變成免責機制。**

---

## 7. §9 self-check —— 僅回報變動項（R-C23）

前 14 條（pilot）與 3.1／3.3／3.4 之 6 條未變，見上繳 18 §8、19 §8。
以下為 **3.2 之 11 條**（含拆後四條）之變動項。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 2 | tc_title | **變** | 拆後四條之 title 逐條帶破壞源 token（`the temperature`／`RECIRC`／`the mode distribution`／`MAX DEF again`），四者互斥；字數 6／5／7／7，皆在 2–14 |
| 10 | procedure↔ER 1:1、ER 可觀察 | **變** | 拆後四條各 2/2。ER 主詞逐行讀：`The "MAX DEF" button`／`the system` —— 皆系統側。**依 R-C23 明說：本項依據不是 `er-subject-net`**，該 gate 為補網，其 PASS 不構成本項之依據 |
| 11 | 無 FP／FF；supported 配 negative | **變** | negative 配對由「-025 對 -024 一條」改為「-028 對拆後四條全體」，已寫入 reasoning。FF 未變 |
| 12 | §8.2.2 | **變** | 由「壓力測試後不拆」改為「控制實體判準要求拆」。四條 `split_flag` 為真、`split_reason` 具名判準，且 `req-id-unique` gate 現在**機械性地**要求此宣告（§4.3）—— 但依 R-C23，本項依據為我逐條讀了四個 `split_reason` 之內容，非該 gate 之 PASS |
| 13 | design_method 於 procedure 定案後指派 | **變** | 決策表 → 狀態轉換。可由 procedure 形狀反推：拆後每條為「按 MAX DEF → 施加一個破壞源」之單一遷移，無多條件表 |
| 5 | 禁用動詞 | 未變（**依據變**）| 前三批為手查；本批起有 `forbidden-verb` gate。**依 R-C23 另補一項獨立於 gate 者**：列出全 31 條步驟之相異首字動詞，實得 **17 個** —— `Change`／`Do`／`Leave`／`Long`／`Note`／`Open`／`Press`／`Read`／`Record`／`Release`／`Retract`／`Run`／`Select`／`Set`／`Short`／`Toggle`／`Turn`。`Read`／`Record` 為 §5.1 之偏好動詞，其餘為具體操作動詞；`Do`（`Do not interact …`）與 `Long`／`Short`（`Long-press`／`Short-press`）為 pilot 之既有寫法，非模糊動詞 |

其餘 11 項未變。

---

## 8. lint 與冪等

```
37 / 37 gates PASS; 0 finding(s) across 31 TCs
```

`gen_pilot.py` 與 `gen_batch2.py` 連續重跑，輸出逐位元組不變。

---

## 9. 未寫回

依 30 §5 第 5 項與 31，**未寫回**。`output/` 仍 2 檔，`write_back.py` 未執行，
`DELIVERY.sha256` 未增列。

**須注意**：`write_back.py` 之 `assertions()` 目前寫死目標列為
`FIRST_ROW … FIRST_ROW + len(tcs) - 1`，而下批寫回將是 **31 列**而非 14 列。
該處以 `len(tcs)` 計算，不需改；但 ENTRY 之「14 列」記載屬 ENTRY 002，
不受影響。列此以免下次誤以為要改。

---

## 10. 進度

| | 數 |
|---|---|
| 驗證單位（leaf）| 403 |
| 已生成（leaf）| **28** |
| 已生成（TC）| **31** |
| 未開始（leaf）| 375 |

**TC 數自本批起大於 leaf 數，兩者不再可互換。** 進度以 leaf 計，
工作量以 TC 計 —— 已寫入 RUNBOOK 並由 `gen_batch2.py` 之收尾行分別斷言
（`14 leaves -> 17 TCs`，另印 `split leaves: {'SWE1-HVAC-024-07': 4}`）。

---

## 11. 「本包是否仍有該驗而未驗者」

依 R-C30，陰性陳述附搜尋範圍。

1. **`req-id-unique` 之改判逾越了本包之授權範圍**（§4.3）。我判為拆分之
   必然後果，但那是我判的。
2. **拆後四條之 ER 完全相同**（逐字比對：四條之 `expected_result` 為同一
   字串）。這是條文使然 —— 四個破壞源之後果在 C20 裡是同一句。
   但它使**四條之間只有 procedure 第 2 步不同**，若日後有人只讀 ER 欄
   會看不出區別。tc_title 與 procedure 承擔了全部區分。列此為已知性質。
3. **`forbidden-verb` 之詞表是 §5.1 之九詞加我自己補的 `locate`。**
   `locate` 不在 canon 內，是我在 18 §9 手查時自行加入的。它現在以
   gate 形式固化了一個**非 canon 之禁令**。若分析層認為不妥，移除即可，
   本批無任何步驟使用該詞。
4. **`er-subject-net` 之四詞組來自 rev1／rev2 兩次實際犯錯**，
   **未對全語料掃過是否還有第五種寫法**。
   **搜尋範圍**：我只用了那四個詞組本身；未以 `is \\w+ed by`
   或類似形態掃 31 條之 ER。故「沒有其他觀察者主詞」這句話**我沒有資格說**。
5. **A-CF19 仍為未測**，且它要到下次寫回才會被測。本批之 31 條若寫回，
   N 欄最長者即 `-029`／`-030`。

---

## 12. 建議 commit message（git 未執行）

```
fix(comfort): split 024-07 four ways; add two gates

- add R-C31 (a clause's own execution premise counts as explicit) to RULINGS
- split SWE1-HVAC-024-07 into four TCs on the 8.2.2 control-entity
  criterion; all four trace to the leaf and declare split_flag/split_reason
- design_method decision-table -> state-transition after the split
- negative pairing of 024-08 now covers all four
- tc_id -025..-028 shift to -028..-031; mapping table in upstream 20
- add forbidden-verb (step-head only, purpose clauses exempt) and
  er-subject-net (self-declaring as a net, not the criterion)
- req-id-unique re-judged: a repeated req_id is legal only when every row
  declares the split
- register A-CF17, A-CF18, A-CF19
- record the tenth axis's per-section rule in RUNBOOK and profile 3.2
- lint 35 -> 37 gates, all PASS, 0 findings across 31 TCs
```

---

## 13. 待分析層

§4.3（`req-id-unique` 改判）與 §11 第 1、3 項為我逾越或自行決定者，
列此待裁。批次 3 之下放待授權。
