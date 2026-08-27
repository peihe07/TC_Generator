# 上繳包 30 —— Vehicle Category：107 → 9 ＋ 交付前清單（T157–T159）

- 日期：2026-08-27
- 對應下放：`docs/handoff/30_xref_triage.md`
  （SHA256 `bbf9377247f4297ac631c9c8c811dbead77c1246635b4f9b4661255cbb074a94`，153 行）
- **結論：T157–T159 全數完成。107 個候選縮至 9 個該先讀。**
- 未寫回交付本、未執行清單任何一項、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T157 | PLAYBOOK §7.4（表徵 vs 內容）| ✅ 建議位階；已記明無承載者 |
| T158 | 107 候選粗篩 | ✅ 三份 tsv；**高優先 18 個標的，其中 9 個無解決標記** |
| T159 | `docs/DELIVERY_CHECKLIST.md` | ✅ 建檔；**第 5 項之母體經實測更正為 12 處** |

**三件請你先看**：
1. **107 → 61 → 18 → 9。** 最後一段（18 → 9）是我加的欄位做的，
   而它揭出一件結構性的事：**R-TM13 保證每一個已解之牴觸永遠留在台帳裡**，
   故第二層**必然**收進已解案。見 §2.3。
2. **`DELIVERY_CHECKLIST` 第 5 項之「7 處 PENDING」是第 5 批之數** ——
   全簿實測 **12 處**。驗收母體應為 12。見 §3.2。
3. **§3.3 落入高優先，而它早在 REV-01 就作廢了** ——
   這是粗篩的正確行為，不是誤報。它也順帶顯示 `owner` 噪音之具體形態。見 §2.4。

---

## 1. T157 —— PLAYBOOK §7.4

「以**內容**為據，不以表徵為據」逐字入 §7（建議位階）。
並列二次實例之偏誤方向表 —— **皆為誇大破壞**。

**已記明本節無承載者**：無檢查驗「這個描述是依內容還是依表徵下的」。
與 §7.1／§7.3 同為紀律。

> 下放包 §1.1 末段之「同一種病，兩層都犯過」亦逐字收入
> （R-VC12 二(a)：看到衍生 PDF 裡只有圖，就寫「SYS1 未帶文字」）。

---

## 2. T158 —— 粗篩

### 2.1 完整輸出

```
xref_triage —— self-test 前置（PLAYBOOK §7.1.1）
  self-test 1  (b) §10.1 之二處皆落入第一層保留            PASS  保留 16 處，檔 ['ANOMALIES.md', 'DATA_REQUESTS.md', 'RULINGS.md', 'data/tableB_draft.md']
  self-test 2  (b) §10.1 須落入第二層高優先               PASS  高優先 16 處
  self-test 3  (a) 反向 純編號引用行須被剔除              PASS  '- 其依據為 R-VC12' → 剔除（a 純編號引用）
  → 三個斷言全過，開始跑正式母體

母體：`ledger_xref.tsv` 1055 處提及
  第一層剔除 653 處 → xref_triage_pruned.tsv
  第一層保留 321 處／**61 個標的** → xref_triage_review.tsv
  第二層高優先 149 處／**18 個標的** → xref_triage_priority.tsv
  剔除之類別分布 {'a 純編號引用': 576, 'b 清單成員': 77}

  高優先中**無任何解決標記**者 **9 個標的** —— 先讀這些：
    [dr] DR-VC2
    [ruling] R-VC19
    [ruling] R-VC4
    [section] 15
    [section] 16.2.1
    [section] 16.2.2
    [section] 2
    [section] 4
    [section] 8.3
  其餘 9 個標的帶有解決標記（RESOLVED／作廢／REV-nn 等）—— R-TM13 使已解案永遠留在台帳裡，其對立為真而早已了結。

**本檔不判定牴觸** —— 只把該讀的縮到可讀之數。判斷由人做。
```

### 2.2 帳目

```
母體 1055 處
  = 第一層剔除     653 處（純編號引用 576／清單成員 77）
  + 第一層保留入 review 321 處（61 個標的）
  + 保留但其標的之**保留者不跨檔** 81 處
```

**第三項須解釋**：某標的跨 ≥2 檔進入 107，但**剔除純引用後只剩一檔有內容性描述**
—— 其跨檔性來自被剔除的引用，**不構成 A-VC20 之形態**，故不入 review。

### 2.3 ⚠ 18 → 9：`resolved_marks` 欄為執行層增設

下放包 §2.1 之第二層判準為「對立語彙」。跑出 18 個標的後，
抽看發現 **`§3.3` 在列** —— 而它早在 **REV-01** 就作廢、A-VC5 已標 RESOLVED。

**那不是誤報。** 原因是結構性的：

```
R-TM13（既交付者不改原文，加註保留）
  → 舊斷言與其反駁**永遠並存於台帳**
  → 二者之語彙**必然對立**
  → 第二層**必然**收進每一個已解之牴觸
```

**即：對立語彙判準與 R-TM13 直接相衝。** 判準抓的正是 R-TM13 要保留的東西。

故增 `resolved_marks` 欄 —— 標記該標的之保留行中**帶有解決標記**
（`RESOLVED`／`已解`／`作廢`／`撤銷`／`正解`／`更正`／`修訂`／`REV-nn`）者之處數。
**本欄不判定「是否已解」，只標記「有沒有解決標記」**，讓讀表者先看沒有的。

### 2.4 高優先 18 個標的全表（**粗體 = 無解決標記，先讀這 9 個**）

| 標的 | kind | 保留處數 | 解決標記處數 | 說「無」之檔 | 說「有」之檔 |
|---|---|---|---|---|---|
| **15** | section | 14 | 0 | ANOMALIES.md／DATA_REQUESTS.md／tableB_draft.md | ANOMALIES.md／DATA_REQUESTS.md／RULINGS.md |
| **R-VC4** | ruling | 7 | 0 | ANOMALIES.md | RULINGS.md |
| **R-VC19** | ruling | 6 | 0 | ANOMALIES.md／FW036_R1L_VehicleCategory_Profile.md | ANOMALIES.md |
| **2** | section | 6 | 0 | FW036_R1L_VehicleCategory_Profile.md／framework.md | FW036_R1L_VehicleCategory_Profile.md |
| **8.3** | section | 6 | 0 | tableB_draft.md | RULINGS.md |
| **DR-VC2** | dr | 4 | 0 | ANOMALIES.md | DATA_REQUESTS.md |
| **4** | section | 4 | 0 | DECISIONS.md | ANOMALIES.md |
| **16.2.1** | section | 2 | 0 | DATA_REQUESTS.md／tableB_draft.md | DATA_REQUESTS.md |
| **16.2.2** | section | 2 | 0 | DATA_REQUESTS.md／tableB_draft.md | DATA_REQUESTS.md |
| R-VC12 | ruling | 21 | 6 | ANOMALIES.md／DATA_REQUESTS.md／RULINGS.md | ANOMALIES.md／tableB_draft.md |
| 4.2 | section | 17 | 4 | RULINGS.md／framework.md | FW036_R1L_VehicleCategory_Profile.md／RULINGS.md |
| 10.1 | section | 16 | 2 | ANOMALIES.md／DATA_REQUESTS.md／tableB_draft.md | DATA_REQUESTS.md／RULINGS.md |
| 10.2 | section | 13 | 1 | ANOMALIES.md／DATA_REQUESTS.md／tableB_draft.md | DATA_REQUESTS.md／RULINGS.md |
| 3.3 | section | 10 | 3 | ANOMALIES.md／RULINGS.md | ANOMALIES.md |
| A-VC1 | anomaly | 7 | 2 | ANOMALIES.md | ANOMALIES.md／RULINGS.md |
| A-VC20 | anomaly | 5 | 1 | ANOMALIES.md／DATA_REQUESTS.md | tableB_draft.md |
| 1 | section | 5 | 1 | FW036_R1L_VehicleCategory_Profile.md | ANOMALIES.md／FW036_R1L_VehicleCategory_Profile.md |
| 6 | section | 4 | 1 | REVISIONS.md／RULINGS.md | REVISIONS.md |

### 2.5 我**未**逐筆判定 —— 那是下一包

下放包 §四明文「讀 `xref_triage_review.tsv` 之逐筆判定」**不在本輪範圍**。
上表為**材料**，各欄皆為機械量測。**本包不主張其中任何一筆是或不是牴觸。**

惟 §3.3 之抽看（為校準粗篩之行為而做，非判定）另顯示一件事：
其命中之十行中，**二行來自 `A-VC21`** —— 因其正文寫「下放包 29 **§3.3**」，
那是**下放包之節號**，非規格節。
**`owner` 噪音在此有了具體形態**：不是 `IN §3` 那種帶擁有者的，
而是「下放包 29 §3.3」——**擁有者在數字之前二個詞，正則吃不到**。

---

## 3. T159 —— 交付前人工驗收清單

`docs/DELIVERY_CHECKLIST.md`，五項逐項建檔，**狀態全為「☐ 未執行」**。
另附各項之**現有材料**（丙″ 已驗六項、母本版面實測、欄位映射、PENDING 清單）。

### 3.1 未增刪五項

下放包 §三所列五項，執行層**未增刪**。已於檔末記明：
「若交付前另有人工項（如與他 feature 之交付本並置檢查），**本清單看不到**。」

### 3.2 ⚠ 第 5 項之母體更正為 **12 處**

下放包 §三第 5 項作「**7 處** PENDING」。**7 為第 5 批之數**。
全簿實測（收斂第 8b 項之 `pending_scope`）：

| DR | 處數 |
|---|---|
| DR-VC10 | 7（第 5 批）|
| DR-VC9 | 3（第 1 批 2／第 3 批 1）|
| DR-VC1 | 1（第 3 批）|
| DR-VC8 | 1（pilot）|
| **合計** | **12** |

**第 5 項之驗收母體應為全簿 12 處**，已於清單中更正並註明下放包原文之數。

---

## 4. 量測條件揭露（R-G8）—— §2.3 三項偽陰性逐項

### (1) 語彙表列舉式，同義而不同詞者抓不到

`NEG` 為 9 個詞、`POS` 為 8 個樣式。
**「該節為空」之「空」在表內，「該節付之闕如」之「闕如」不在** ——
後者若出現於台帳，第二層看不到。**未量測其實際發生率。**

### (2) 同檔內之牴觸看不到

第二層要求 `neg` 與 `pos` **跨檔**（`neg - pos or pos - neg` 非空）。
**R-VC12 二(a) 與 R-VC12 其餘各款就在同一個檔裡** ——
該類若再發生，`ledger_xref` 與本粗篩**皆看不到**。
本輪 A-VC20 被抓到，是因為它**恰好跨檔**（DR-VC6 記對、RULINGS 記錯）。

### (3) `owner` 降噪 7/107 之限制不變

且 §2.5 顯示其形態比原先描述的更廣：
除 `IN §3` 外，尚有「**下放包 29 §3.3**」這種擁有者在前二詞者，
現行正則 `(IN|FO|PLAYBOOK|canon|下放包|上繳包|包)\s*(?:\d+\s*)?§\s*$`
**本應吃到**「下放包 29 §」—— 實測未吃到，因該行之 `§3.3` 前為
`下放包 29 §3.3` 而 `§` 與數字間無空白、且 `29 ` 後接 `§` 之樣式
與實際文字之全形／半形空白不符。**本輪未修**（屬 `ledger_xref` 之改動，
非本包任務），記為已知缺陷。

### (4) 另一項本包新增之揭露

`resolved_marks` 之樣式表同為列舉式。
**帶解決標記 ≠ 已解**（該行可能只是提到「作廢」二字），
**無解決標記 ≠ 未解**（其解可能寫在另一個未被本標的命中的行）。
**該欄只用於排序閱讀順序，不得作為結案依據。**

---

## 5. 進度

**117 leaf 中 112 筆已收斂，TC 累計 120 筆。**
出貨門檻二表：表 A 完成、表 B 草稿（四處待 DR-VC3）。
`reasoning` 側檔 120 筆。TC ID 已裁（R-VC28）。寫回方案丙″ 六項全過。

**十筆 DR 發送中**（Pei 2026-08-27）。生成側仍停於 DR-VC3／DR-VC9(二)。

---

## 6. 待你裁

1. **9 個無解決標記之高優先標的**（§2.4 粗體）—— 下一包之逐筆判定範圍
2. **`ledger_xref` 之 owner 正則缺陷**（§4(3)）—— 是否修
3. **同檔內牴觸看不到**（§4(2)）—— R-VC12 之形態若再發生，現行工具全盲；
   是否需要第三個判準
4. Tier 3：十筆 DR 之回覆
