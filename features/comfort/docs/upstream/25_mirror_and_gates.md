# 25 — Comfort HMI / R-C35、ch16 鏡射表、兩個 gate、`2.7.1` 停下

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 36
- 結果：**鏡射表找到 7 個 `no-counterpart`，其中三節已生成 —— `-041`、
  `-015`～`-017`、`-031` 共 5 條之 EMEA 排除式 PC 過嚴**（未自行移除）。
  `2.7.1` **停下**（條件 1 不成立）。lint **38 → 40 gate，全 PASS，64 條**。
  **未寫回、未開新批。**

---

## 1. R-C35 貼入 ＋ DR #20

`RULINGS.md` 現有 **37 個**逐字條文區塊。R-C35 前附來源說明，
記明分析層自陳規則之前件有誤，與執行層之違反為正確。

**DR #20** 已登（High，**不阻塞**），與 **DR #17** 併記為 2.1 內容不足之兩問。
條目含 §2 之三句要點，其中：

> **現在不補不是判斷該配置不存在，是判斷條文尚未使它可陳述。**

並記風險：若答案為「涵蓋」，`Seat Control Tab` 之 14 條在僅前排氣候之車上
無對象，屆時須補 PC。

---

## 2. `2.7.1` —— 三條件逐項評估，**條件 1 不成立，停下**

### 2.1 條件 1（值須取自 2.7.1 之逐字列舉）—— **不成立**

2.7.1 之全文**僅一句**：

> C6.1) In some vehicles fan speed ranges for front hvac are: **Off, 1-8**.

**它只列舉一個值。** 該軸若要成立，另一值（`Off, 1-7`）須取自 **2.7**：

> C6.) Fan ranges: **Off, 1-7**, 15h (denoting to show AUTO instead)

**依條件 1 之字面，2.7.1 未逐字列舉其值域變體 → 不成立 → 停下。**

**但有一個讀法我必須併陳，因為它可能推翻上述結論**：
2.7.1 之條文 id 為 **`C6.1`**，是 2.7 之 `C6.` 的**子條**。
兩者合讀即為完整列舉，且取 2.7 之值**不是推論而是另一條文之逐字**
（R-C29 本就允許跨節取據）。若分析層採此讀法，條件 1 成立。

**我不自行決定**，因為增軸屬不得自我授權者，而條件 1 正是為此而寫。

### 2.2 條件 2（類別）—— **功能型**，若日後增列則不進介面型清單

該軸之兩值皆**不移除任何介面** —— 風速顯示於 climate screen 與 main
category control，7 段或 8 段皆在。改變的是**值域**，非承載介面。
依 R-C34 為**功能型**。

### 2.3 條件 3（既有 63 條之影響）—— **實測，0 條受影響**

**搜尋範圍**：根目錄 `data/section_fulltext.tsv` 全 129 節，
pattern `1-7`／`1-8`／`fan speed range`／`fan ranges`（不分大小寫）。

| 節 | leaf | 命中 |
|---|---|---|
| 2.7 | 5 | `1-7`、`Fan ranges` |
| **2.7.1** | 1 | `1-8` |
| 7.5 | 4 | `1-7`、`Fan ranges`（`Rear Climate` 組，未生成）|
| 16.7 | 5 | `1-7`、`Fan ranges`（ICS 鏡射，未生成）|

**命中 4 節、15 leaf。已生成者僅 2.7（5 leaf → `-058`…`-062`）。**

逐條檢視該 5 條：`-058`（顯示位置）、`-059`（popup）、`-060`（三種調整途徑）、
`-061`（不可關閉，下界）、`-062`（全暗僅由電源）——
**無一條之判定依賴風速上界為 7 或 8**。故即使該軸日後增列，
**既有 5 條不需補 PC**。

### 2.4 停下之處置

`2.7.1` 維持不生成、不入 coverage 分母、不列 BLOCKED（R-C16）。
若條件 1 依 §2.1 之子條讀法獲裁定成立，該 leaf 可續生成，
**條件 2 與 3 之答案已備妥，不需重做**。

---

## 3. 兩個新 gate（38 → 40）

### 3.1 `interface-axis-answered`（36 §6）

每個 doc 增 `interface_axis_review` 欄，五鍵：`observable_interface`、
`axis_9`、`axis_12`、`axis_13`、`emea_ics`。gate 檢查五鍵皆在且非空。
該欄已列入 `NOT_IN_WORKBOOK` 白名單（不入工作簿）。

**既有 64 條全數回填**（19 個節，四個 generator）。

**反向驗證（兩方向）**：

| 注入 | 結果 |
|---|---|
| 清空 2.16 之 `axis_12` | **FAIL** — `SWE1-HVAC-022 (2.16): interface_axis_review is missing or empty for ['axis_12']` |
| 整個欄位缺席 | **FAIL ×4** — 逐節指名 |

**第一次反向驗證我做錯了**：改到了 `gen_batch4.py` 副本裡它**不發射的節**
（3.2），故無 doc 受影響而未 FAIL。改指定 2.16 後正常。
**是測試錯，不是 gate 錯** —— 但它暴露了一件真的事，見 §6.1。

### 3.2 `pending-sibling`（36 §4）

`PENDING_SIBLING = {"2.6.1": "2.11"}`。gate 檢查：**表中 sibling 之節次一旦
出現於已生成集合**，而該 doc 之 `duplicate_of`／`distinguishing_axis`
仍為暫空 → FAIL。

每次執行印出具名行：

```
- PASS — pending siblings awaiting their counterpart section (36 §4): {'2.6.1': '2.11'}
```

**反向驗證**：把表改為 `{"2.6.1": "2.6"}`（2.6 已生成）→

```
[FAIL] pending-sibling: 2.6.1's sibling 2.6 is now generated, but
duplicate_of/distinguishing_axis is still unset for ['NR1L-ComfortHMI-052'
… '-057'] — §4.6 判定須於對造節生成後回填
```

`Climate Modes` 生成之日，lint 會自己要求回填。

---

## 4. `data/ch16_mirror_map.tsv` —— 雙向，44 節全數覆蓋

四欄 `ch16_outline`｜`ch2_or_ch3_outline`｜`對應強度`｜`依據`，
**30 列**（不含表頭）。

**覆蓋檢查（實測）**：ch16 全 18 節皆列、ch2／ch3 全 26 節皆列，**未列者 0**。

| 對應強度 | 列數 |
|---|---|
| `mirrored` | 15 |
| `partial` | 8 |
| `no-counterpart` | 7 |

`partial` 之典型：**16.4 ICE3 一句綑綁五個 on/off 狀態**
（MAX A/C, A/C, RECIRC, MAX DEF, REAR DEFROST），對應 ch2 之 2.4／2.5／
2.8／2.9／2.13 五節 —— 一對五，故五列皆記 `partial`。

**一項順帶發現**：`16.17` 之條文 id 標為 **`C16.`**，與 **`2.15` 之 `C16.`
相撞**；而其內容與 **`2.16`（`C18.`）** 逐字相同。**id 撞號而內容對應他節**
—— 若日後有人以條文 id 建索引，此處會錯配。已記於該列之依據欄。

---

## 5. `no-counterpart` 之後果 —— **5 條之 EMEA 排除式 PC 過嚴**（未自行移除）

依 36 §5：「若出現 ch2／ch3 之節在 ch16 無對應，其 TC 之 EMEA ICS 排除式
PC 即過嚴，須移除；**回報清單，不自行移除**。」

### 5.1 `no-counterpart` 七項

| ch2／ch3 | 已生成？ | 影響之 tc_id |
|---|---|---|
| **2.1** | **是** | **`-041`**（1 條）|
| **3.1** | **是** | **`-015`／`-016`／`-017`**（3 條）|
| **3.4** | **是** | **`-031`**（1 條）|
| 2.3.1 | 否（`Climate Modes`）| — |
| 2.5.1 | 否（`Climate Modes`）| — |
| 2.7.1 | 否（本包停下）| — |
| 16.16 | —（ch16 側）| — |

**合計 5 條之 EMEA 排除式 PC 過嚴。** 未移除，待裁。

### 5.2 三節為何無對應，逐節具名

- **2.1**（`R1C1` comfort category 之 tabs 與順序）—— ch16 十八節無 tabs 節。
  16.16 ICE15 述 `Always show 'Driver' or 'Passenger'` 與 controls screen，
  非 comfort category 之分頁結構
- **3.1**（`C19` Tri-Mode 三鍵七組合）—— **16.12 ICE11 為 5 states 之單選**
  （`Only one airflow mode can be selected at a time` 見 2.12），
  與 tri-mode 之「三鍵各自 toggle → 7 組合」**結構不同**，非其鏡射
- **3.4**（`C22` soft top 之 rear defrost 按鈕不出現）—— ch16 無對應節

### 5.3 `partial` 之待裁一項

**`3.3` ↔ `16.10`** 記為 `partial`：ICE9 之
`grey out remaining buttons except for Front/Max defrost and rear defrost`
涵蓋 C21 之可用性，**但未逐字重述 C21**。

故 `-029`／`-030` 之 EMEA 排除式 PC **既非明顯成立亦非明顯過嚴**。待裁。

### 5.4 我原先的歸納錯在哪裡

上繳 24 §2.1 以**三節首句 ＋ framework.md 之鏡射表**歸納出「ch16 鏡射
ch2／ch3」，據此對 31 條補 PC。

**三個樣本（2.2、2.14、3.1 之 MODE 循環）全部選自有對應者**，
而我把 `3.1` 之對應認成 `16.12.1` —— 逐節建表後才看清
**16.12.1 對應的是 2.12.2（`C13.1`），不是 3.1（`C19`）**，
兩者皆述 Mode hard control 而所屬體系不同。

**歸納之樣本若全部取自陽性側，其結論必然是「普遍成立」。**
這與 §4.1 判別（無選擇子→不需要軸）是同一形態：
**我用一組正例得出一條規則，然後把它當成判準用。**

---

## 6. 「本包是否仍有該驗而未驗者」

依 R-C30。

1. **`INTERFACE_AXIS_REVIEW` 在四個 generator 內各有一份副本（實測 4 份）。**
   §3.1 之第一次反向驗證失敗即由此暴露：改一份不影響其他三份。
   目前四份內容一致（由同一腳本寫入），**但沒有任何機制保證它們維持一致**
   —— 改了一份而漏改其他三份，lint 不會報。
   **建議下輪抽為單一來源**（如 `data/interface_axis_review.tsv`），本包未做。
2. **`interface-axis-answered` 只驗「答了沒有」，不驗「答得對不對」。**
   這是 36 §6 明白接受的限制，記此以免日後誤讀其綠燈。
   §5 之發現正說明：我在上繳 24 對 `3.1` 之 `emea_ics` 答過「mirrored」，
   **那個答案是錯的，而任何 gate 都不會知道。**
3. **鏡射表之 `mirrored`／`partial` 判定由我逐節閱讀而得，未經第二人覆核。**
   **搜尋範圍**：ch16 全 18 節與 ch2／ch3 全 26 節之 `full_text`，逐節通讀。
   判定依據已逐列寫入 `依據` 欄，故可覆核 —— 但尚未被覆核。
4. **`partial` 之八列尚無處置規則。** `mirrored` → 排除成立、
   `no-counterpart` → 排除過嚴，兩者清楚；**`partial` 落在中間而規則未定**。
   現時僅 `3.3`（2 條）受影響，但 `Climate Modes` 與 `Airflow and Defrost`
   兩組生成時會遇到 2.4／2.5／2.8／2.9／2.13 五節，屆時 `partial` 之處置
   規則是必要的。
5. **`2.7.1` 之條件 1 我判不成立而併陳了可能推翻它的讀法**（§2.1）。
6. **`PENDING_SIBLING` 表目前只有一筆，且是我手動維護的。**
   跨 Test Set 之 sibling 若有第二筆而我沒察覺，該表不會自己長。
   與 `negation-users` 清單同型，但後者已有 gate 比對實測值，
   **前者沒有** —— 沒有任何檢查會問「還有哪些 sibling 該入表」。

---

## 7. lint

```
40 / 40 gates PASS; 0 finding(s) across 64 TCs
```

四個 generator 連續重跑，輸出不變。未寫回（`output/` 仍 2 檔）、未開新批。

進度不變：**60 leaf / 64 TC**，阻塞／停下 3 leaf（DR #17 之 2 ＋ `2.7.1` 之 1）。

---

## 8. 建議 commit message（git 未執行）

```
feat(comfort): ch16 mirror map; two gates; 2.7.1 held

- add R-C35 (a rule's antecedent must be about what it judges) to RULINGS
- register DR #20 alongside DR #17 as 2.1's two content gaps
- hold 2.7.1: condition 1 fails on 2.7.1 alone (it enumerates one value);
  the C6/C6.1 sub-clause reading that would satisfy it is presented too.
  Conditions 2 and 3 answered anyway: function-type axis, zero impact on
  the existing 63
- build data/ch16_mirror_map.tsv, bidirectional, all 44 sections covered:
  15 mirrored, 8 partial, 7 no-counterpart
- no-counterpart hits 2.1, 3.1 and 3.4, so five TCs carry an over-strict
  EMEA exclusion; listed, not removed
- add interface-axis-answered and pending-sibling gates, both
  reverse-verified; backfill interface_axis_review across all 64 TCs
- lint 38 -> 40 gates, all PASS
```

---

## 9. 待分析層

1. **§5.1** —— `-041`／`-015`～`-017`／`-031` 之 EMEA 排除式 PC 是否移除。
2. **§5.3 ／ §6.4** —— `partial` 之處置規則（現影響 2 條，
   `Climate Modes` 與 `Airflow and Defrost` 生成時影響五節）。
3. **§2.1** —— `2.7.1` 之條件 1 是否依 `C6`／`C6.1` 子條讀法成立。
4. **§6.1** —— `INTERFACE_AXIS_REVIEW` 之四份副本是否抽為單一來源。
5. **§6.6** —— `PENDING_SIBLING` 表之完整性是否需機制。
6. **§4 之 id 撞號**（`16.17` 標 `C16.` 而 `2.15` 亦為 `C16.`）是否須登 anomaly。
