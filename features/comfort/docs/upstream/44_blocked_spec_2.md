# 44 — Comfort HMI / DR #43 之執行、限定語判準式、Remarks 承載歧義

- 產出層：執行層｜2026-08-16｜對象：分析層
- 承接：下放包 66
- 結果：五項全數落實。`058`／`072` 已列入 `[BLOCKED-SPEC]` 白名單並各產一列
  （`-382`／`-383`），§1.1 之段落逐字寫入 DR #43。限定語改判準式定義，
  gate 效力改為**具名回報，沉默即 FAIL**，兩向反向驗證（含實跑之 mutation）。
  `126-02` 納入 DR #6 之逐條判清單。`14.12` 三條之 Remarks 已承載歧義，
  profile §3.6 記其通則**並加一道白名單**（見 §4.2 之自陳）。
  lint **51/51 PASS，383 條**；leaf **378 / 403 ＝ 93.8%**。ENTRY 015 已產出。

---

## 0. 下放包五項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | `058`／`072` 入白名單並產 BLOCKED row；§1.1 逐字寫入 DR #43 | ✅ §1 |
| 2 | 限定語集合改判準式；`rc42-condition-marker` 改具名回報，反向驗證 | ✅ §2 —— **並訂正我上一包對 `126-02` 之一句話** |
| 3 | `126-02` 納入 DR #6 之逐條判清單 | ✅ §3 |
| 4 | `14.12` 三條之 Remarks 增記歧義；profile §3.6 記通則 | ✅ §4 |
| 5 | `RUNBOOK` 記「文字上差別很小，責任上差別是全部」 | ✅ §5 |
| — | 上繳 44 | 本件 |

---

## 1. `058`／`072` —— BLOCKED row 已產

| | `-382`（`058`／`11.5`）| `-383`（`072`／`12.6`）|
|---|---|---|
| `test_item` | The system shall follow the **HMI Settings List** for the details on the Auto Comfort Settings options for heated/vented seats (HVS6.) | The system shall follow the **HMI Notes** for … (HVS6.) |
| `test_procedure`／`expected_result` | 留白（R-C24）| 留白 |
| Remarks 首 60 字元 | `[BLOCKED-SPEC] Owner: **HMI Settings List** — the Auto Comf…` | `[BLOCKED-SPEC] Owner: **HMI Notes** — the Auto Comfort Set…` |
| `priority` | P3 | P3 |

白名單於 `lint_tcs.py` 增列二者並註明其裁定出處（66 §1）。
**`Heated Vented Seats` 組現無停下之 leaf**：59 emitted ＋ 0 withheld = 59。

**`test_item` 之措辭**：037 之 leaf 描述即條文原句（`HVS6. Refer to …`），
惟 profile §3.1 要求 Test Item 含 modal，故改寫為 `The system shall follow …`
並於句末附條款標籤 `(HVS6.)`。**委派對象之字面未改**。

§1.1 之段落**逐字**寫入 DR #43 條目（含「若日後只補入其一，兩者將合法地
不一致，且 R-C40 不會攔它」與「看起來一樣而依據不同者，最容易在日後被誤以為
可以一起處理」），§1.2 之限制亦照記。

---

## 2. 限定語 —— 判準式定義與 gate 效力

### 2.1 profile §3.2.2 已改

定義取代逐詞列舉（連接詞／限定性名詞片語／**介系詞片語**），
逐詞清單降為**實例**並擴充至九項（加 `Where`／`Vehicles equipped with`／`On the`），
其出處記於清單旁。gate 效力改為：命中失敗**不硬阻**，改要求
`condition:`（是條件，附逐字片段）或 `not-a-condition:`（不是，回復停下），
**沉默即 FAIL**。

### 2.2 **訂正我上一包的一句話**

上繳 43 §4.2 稱 `126-02` 之範圍「以介系詞片語 `On the 50% widget,` 界定」，
並在本輪初稿的 profile 區塊裡寫成「66 §2.2 擴充清單後**本條已直接命中**」。

**實測不是這樣**：本條之 PC 寫成 `The vehicle shows the 50% Comfort widget`，
與條文之共同連續字串為 ` Comfort widget`（15 字元），其**前文是
`CW2.) The second`** 而非 `On the 50% widget,`。

> **不命中之因是 PC 沒有引到帶限定語的那一段，不是條文沒有限定語。**

已於 profile 之 disposition 區塊訂正，並記其可解之路：**若改寫該 PC 以逐字引
`On the 50% widget,`，即可直接命中而該區塊可撤**。
本輪不改寫 —— 改寫 PC 會動到已寫回之列，而該列之內容本身無誤。

### 2.3 反向驗證（實跑）

| 向 | 作法 | 結果 |
|---|---|---|
| 沉默 | 移除 `125-08` disposition 之 `condition:` 行 | **FAIL** — `…carries no named disposition … Silence is the one answer not available` |
| 具名 | 還原 | PASS，且 lint 每輪列印兩條 disposition 及其出處 |
| 清單 | `verify_b_gates.py` 增三向：misses 非空、每個 disposition 有答、清單含 66 §2.2 之三項新增 | 全 PASS（現 16 向）|

**每輪可見之回報行**：

```
- PASS — R-C42 unblocks whose quoted fragment does not match a listed
  qualifier, and their named dispositions (66 §2.2): 2
    · 125-08 (17.2): condition — 出處 66 §2.1（分析層裁定不回復停下）
    · 126-02 (17.3): condition — 出處 66 §2.1
```

---

## 3. `126-02` 已納入 DR #6 之逐條判清單

DR #6 之條件式預裁增記四條之**值集合各異**：

| leaf | 其條件之值集合 |
|---|---|
| `098`（14.14）| 8.4"／10.1" Landscape／10.25"／12.3" **radio** |
| `127-01`／`127-02`（17.4）| 8.4／10.1／12 **landscaped screen** |
| `125-08`（17.2）| **12' Portrait 50% widget** |
| **`126-02`（17.3）** | **50% widget**（不限 Portrait，不限尺寸）|

**故不可整批撤**：DR #6 若答「不含 12.3" radio」，`098` 之範圍為空而
`126-02` 未必。另照錄 66 §2.1 之分工：**R-C42 管可否逐字陳述，DR #6 管是否在
交付範圍內** —— 同一組尺寸既使某些 leaf 停下、又使另一些解封，是兩個問題。

---

## 4. `14.12` 三條之 Remarks 與 profile §3.6 之通則

### 4.1 已增記（外部可見，無內部 id、無 DR 編號）

> The clause refers to the hard controls collectively. On vehicles whose
> hard controls are of mixed types, this case cannot be determined from the
> Comfort HMI specification alone.

profile §3.6 增補通則（逐字）：

> **凡條文之歧義會使測試員在執行時無法判定者，該歧義須出現於 Remarks。**
> `reasoning` 之讀者是**覆核者**，Remarks 之讀者是**執行者**，
> **而撞到它的是後者**。

### 4.2 **一處我自行加了限制，須報備**

原 gate 為「非 BLOCKED 列之 Remarks 必須為空」。要讓上述三條通過，
最省事的改法是「非空即放行」—— **我沒有那樣做**，理由是：

> Remarks 是**客戶可見**之欄。若「非空即放行」，則任何生成器日後都可以
> 往客戶看得到的地方寫任何東西，而沒有任何一道檢查會問一句。

故實作為：非 BLOCKED 列之 Remarks 若非空，須
（一）不含 `R-C…`／`DR #…`／`A-CF…`／`§`，且
（二）**該列列名於 `lint_tcs.py` 之 `AMBIGUITY_REMARKS`** ——
其增列是裁定，不是生成器可自取之選擇（同 marker 白名單之理由，R-C26）。

**這是我在指示之外加的一道限制**，請裁是否保留。

---

## 5. `RUNBOOK` 已記

新章「文字上的差別很小，責任上的差別是全部」，含 66 §4 指定逐字保留之自陳，
並補其成因：

> 加上「該功能之」之後，這條 TC 在混合型態之車輛上**可以執行且會過** ——
> 而條文其實沒說那種車該如何。**我替上游作了答，並且把它藏進了一個
> 介系詞片語裡。**

自查一句：**我這樣寫，是把條文說清楚了，還是替它做了決定？**

---

## 6. lint 與 §9 自評

```
51 / 51 gates PASS; 0 finding(s) across 383 TCs
```

反向驗證六支全 PASS（`verify_b_gates` 現 16 向）。

TC 381 → **383**；已生成 leaf 376 → **378 / 403 ＝ 93.8%**；節 121 → **123**；
**停下之 leaf 27 → 25**。

**§9 十七項**：新增 2 條（皆為 BLOCKED row），另 3 條之 Remarks 改動。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 3 | Pre-Condition | 變（2 條）| BLOCKED 列取第十六軸之正向值（17.3）＋軸 13／EMEA 之排除；**不設配置式 PC** |
| 5–8 | 步驟 | — | BLOCKED 列之 `test_procedure`／`expected_result` 留白（R-C24），故 §10.5 不適用（gate 已具名豁免）|
| 12 | 溯源、§8.2.1 | 變 | 二 leaf 各溯其 037 req_id；**委派對象不同一事寫入兩節之 `reasoning` 與 DR #43** |
| 14 | Remarks | 變（5 條）| 2 條 BLOCKED（首 60 字元具名 owner，R-C27）＋ 3 條歧義記載（66 §3，白名單控管）|
| 16 | `specification_reference` | 變（2 條）| 各含自身節次＋17.3＋2.14＋16.2 |
| 其餘 | — | 不變 | |

---

## 7. 「本包是否仍有該驗而未驗者」（R-C30）

1. **兩條 BLOCKED row 未經 §7 之人工複核**，只經 lint 與 marker gate。
2. **「零餘留」之判讀未讀該二外部文件本身**（未入 `inputs/`）——
   66 §1.2 已裁此為如實表達，惟該限制隨 BLOCKED row 一同交付給客戶，
   **客戶讀到的是 `Owner: HMI Notes`，讀不到「我們沒看過那份文件」**。
3. **`AMBIGUITY_REMARKS` 是手記清單**（§4.2）—— 與 `MOVED_TO_BATCH16`
   同型；其身分檢查（某列在清單而其 Remarks 已改回空）**尚無 gate**。
4. **`126-02` 之 PC 未改寫**（§2.2）—— 可解而未解，其代價是 disposition
   區塊會一直留著；我選擇不動已寫回之列，**這是取捨不是結論**。
5. **§4.2 之限制為我自行加入**，未經裁定。

---

## 8. 待分析層

1. **§4.2** —— 非 BLOCKED 列之 Remarks 白名單（`AMBIGUITY_REMARKS`）：
   請裁是否保留；若保留，其身分檢查是否比照 `moved-leaf-identity` 補一道。
2. **§7.2** —— BLOCKED row 交付予客戶時，是否須於某處聲明
   「本層未讀該外部文件」；現行僅 `reasoning` 有記，客戶端看不到。
3. **剩餘 25 個停下之 leaf**：DR #31（9）、DR #17（2）、DR #32（3）、
   DR #16（2）、DR #11（1，`14.1`）、R-C17（3）、後排配備（4，已裁同停）、
   `9.1`（1，無 ER）。
4. **DR #6** 之四條逐條判清單（§3）—— 其答覆到達時即須逐條執行，
   非整批。
