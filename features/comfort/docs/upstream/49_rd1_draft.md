# 49 — Comfort HMI / 狀態句之弱量測、test-setup 反向量測、RD-1 清單起草

- 產出層：執行層｜2026-08-16｜對象：分析層
- 承接：下放包 71
- 結果：四項全數落實。狀態句實詞量測上線（5 行全部命中）——
  **其誤報率以注入式探針量得，四種成因俱現，故本輪不宜升為 FAIL**（§1.2）。
  `test-setup` 最長 20 種寫法量測上線，**逐一判定：無一應改標**，
  且其長 run 之成因一致（§3）。RD-1 清單已起草
  （`docs/RD1_questions_comfort.md`，25 單位、7 個問句），**未送出**。
  lint **54/54 PASS，383 條**；**本輪未新增寫回**，理由見 §5。

---

## 0. 下放包四項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | 加狀態句實詞之弱量測（具名回報，不 FAIL），回報誤報實例與成因 | ✅ §1 |
| 2 | 維持去重並列列數 | ✅ §2 |
| 3 | `test-setup` 量最長 20 行，逐一判是否應改標 | ✅ §3 |
| 4 | 起草 `docs/RD1_questions_comfort.md`，遵三項紀律，不送出 | ✅ §4 |
| — | 上繳 49 | 本件 |

---

## 1. 兩段式狀態句之實詞量測

### 1.1 現況：5 行全部命中

```
- PASS — 兩段式狀態句之實詞（71 §1，量測不 FAIL）：5 行，其中 0 行有實詞未見於所引節
    · NR1L-ComfortHMI-377 (14.14) 'the vehicle under test is such a vehicle' — 全部命中
    · NR1L-ComfortHMI-378 (17.4)  'the vehicle has one of those screens'   — 全部命中
    · NR1L-ComfortHMI-379 (17.4)  同上
    · NR1L-ComfortHMI-380 (17.5)  'the vehicle is such a vehicle'          — 全部命中
    · NR1L-ComfortHMI-381 (17.5)  同上
```

**惟「0 行未命中」不足以說明什麼**：現行五句皆為**回指句**（`such a
vehicle`／`those screens`），其實詞本就少且必然出現於該節。
**一個永遠靜默之量測與一個沒有量測，讀起來一樣。**

### 1.2 誤報率以**注入式探針**量得（不依賴語料）

| 探針（`— ` 之後） | 節 | 未命中之實詞 | 判讀 |
|---|---|---|---|
| `the vehicle has one of those screens` | 17.4 | （無）| 現行寫法 |
| **`and the rear zone is enabled`** | 17.4 | `rear`／`zone`／`enabled` | ✅ **真陽性** —— 正是 §8.4.1 之違反 |
| `the vehicle has a widescreen display` | 17.4 | `widescreen`／`display` | ❌ 誤報：**同義／換詞** |
| `the vehicle has a landscape display` | 17.4 | `display` | ❌ 誤報：**詞形變化**（`landscaped` 含 `landscape`，故該詞反而命中；`display` 不在節內）|
| `the head unit is a radio of one of those sizes` | 14.14 | `head`／`unit`／`sizes` | ❌ 誤報：**上位詞**（節寫 `radios`，未寫 `sizes`）|
| `the unit under test is configured accordingly` | 17.5 | `unit`／`configured`／`accordingly` | ❌ 誤報：**測試語彙未被停用詞涵蓋** |
| `the vehicle supports dual airflow` | 17.5 | `supports` | ❌ 誤報：**動詞換詞** |

**七個探針中 1 真陽性、5 誤報、1 現況**。四種成因（同義、詞形、上位、測試語彙）
在七句之內全部出現 —— **誤報不是偶發，是這個判準的常態**。

> 故**本輪不升為 FAIL**，維持具名回報。
> 其價值在於：**若有人寫出 `and the rear zone is enabled`，那一行會被印出來**，
> 而不在於它印出來的每一行都是錯的。

**一項副產物值得記**：`landscaped` 之探針顯示，子字串比對使
**詞形變化在一個方向上被隱藏**（節有 `landscaped`，句寫 `landscape` → 命中；
反過來則不命中）。該不對稱是實作之性質，不是判準之意圖。

---

## 2. 去重與列數並存 —— 維持

`spec-derived` 之最短 20 種寫法表維持「依 節×措辭 去重 ＋ `×n` 列數」之形式。
**分佈看種類，影響看列數** —— 例如 `16.2` 之 EMEA 排除句列數為 246／96，
其 run=10 之意義與一個 `×1` 之寫法完全不同。

---

## 3. `test-setup` 之反向量測 —— **最長者，逐一判**

### 3.1 前 20 種寫法（依 節×措辭 去重）

| run | 節 | 措辭（截） | ×n | 應否改標 |
|---|---|---|---|---|
| 23 | 7.1.1 | The rear climate screen is open and the climate system is on | 1 | ❌ 不改 |
| 22 | 7.6／7.4／7.1 | 同上 | 5／4／3 | ❌ |
| 21 | 17.2 | The Comfort widget is shown on the home screen | 8 | ❌ |
| 20 | 7.5 | 同 7.1.1 | 4 | ❌ |
| 20 | 2.10 | The climate screen is open and the climate system is on | 6 | ❌ |
| 20 | 13.5 | The Seats tab is open and the lumbar/bolster level is away from both its minimum and its maximum | 1 | ❌ |
| 19 | 17.1 | The Comfort widget is shown on the home screen | 3 | ❌ |
| 18 | 13.5 | The lumbar/bolster level is away from both its minimum and its maximum | 1 | ❌ |
| 16 | 7.7／7.3／7.1.1／17.3 | （同型）| 3／3／2／2 | ❌ |
| 14 | 14.4／14.10 | The head unit is on and the climate system is on | 2／1 | ❌ |
| 9–10 | 7.2／2.5／2.15／17.4 | （同型）| 5／3／2／2 | ❌ |

### 3.2 判定與其共同理由

**20 種全部維持 `test-setup`**，且其長 run 之成因**完全一致**：

> 共同子字串落在**受測物之名稱**（`the rear climate screen`／
> `the Comfort widget`／`the lumbar/bolster`），
> **而不落在該行所斷言之事**（`is open`／`is shown`／`is away from both its
> minimum and its maximum`）。

條文說的是「後排氣候畫面上有什麼」，本行說的是「把它打開」——
**同一個名詞，兩種主張**。前者是需求，後者是測試之佈置，故標籤正確。

**最值得看的一列**（13.5，run=20）：`the lumbar/bolster` 出自條文，
而 `away from both its minimum and its maximum` 是本層為使增減可觀察而設之
起始狀態 —— **條文從未說腰靠應該在中間**。若把它標成 `spec-derived`，
就等於宣稱條文要求了一個它沒要求的起始狀態。

### 3.3 該量測之侷限

其比對對象為**該條所標之出處節**。若某行實際源自**另一節**而被標成
`test-setup`，本量測看不見 —— 它只問「這一節說過嗎」，不問「有沒有哪一節說過」。

---

## 4. RD-1 清單已起草（**未送出**）

`features/comfort/docs/RD1_questions_comfort.md`。

### 4.1 形式

25 個單位歸為 **7 個問句**，依其所待之答案分組（非依節分組）：

| # | 問句 | 阻塞單位 |
|---|---|---|
| 1 | 哪一種配置產生哪一組 comfort tabs？ | 2 |
| 2 | 哪一種車適用哪一組氣流模式？ | **9** |
| 3 | recirc 與座椅圖示之對照表在哪裡？ | 3 |
| 4 | 這些前排條文所述之車輛是否配備後排氣候？ | 4 |
| 5 | 哪些車輛有附加之後排控制？ | 1 |
| 6 | 這些條文所委派之文件在哪裡？ | 3 |
| 7 | 第 18 章與第 17 章之區別為何？ | 3 |

每項含：條文逐字片段、所缺之物、現行處置、得答覆後之處置。
文件開頭列總計 25 與 378／403 之現況。

### 4.2 三項紀律之自查（方法 `[machine]`：對該檔 grep）

| 紀律 | 實測 |
|---|---|
| 無內部語彙 | `R-Cnn` 0、`A-CFnn` 0、`DR #n` 0、下放包／上繳／`§n` 0、gate／lint 0（唯一命中為 `delegate` 一詞內之字母序列）|
| 依 DR 分組 | 7 組，其一（問句 2）涵蓋 2.12 與 2.12.2 兩節共 9 單位 |
| 每項附阻塞數 ＋ 開頭總計 | ✅ 表列 ＋ 摘要 |
| **不列 tc_id** | 實測 `NR1L-ComfortHMI-` 出現 **0 次**；只用 `SWE1-HVAC-` 之 req_id |

### 4.3 兩處自主判斷（請覆核）

1. **問句 5 之內部分層**：`9.1` 之單位本身無可觀察行為，而**其後七個單位
   已產出且其執行需知道車輛群**。我把「這一個單位可能根本沒有測試案例」與
   「那七個要能執行」寫在同一項裡並分開陳述 —— **因為對上游而言那是同一個
   問題（哪些車），對我們而言是兩種處置。**
2. **文末另列兩項「不阻塞但影響交付形態」**（螢幕尺寸、ch11／ch12 之
   popup）—— 71 §4 未要求，惟其一會使 5 條 TC 失去適用對象、其一牽涉 20 條
   是否為重複。**不列它們，等於把已知的事藏在清單之外。**

### 4.4 未做

未送出、未預測答案、未列我方傾向、未合併 DR（清單以問句分組，
惟每項對應之既有 DR 編號保留在本層之 `DATA_REQUESTS.md`，未帶入該檔）。

---

## 5. lint 與 §9 自評 —— **本輪未新增寫回**

```
54 / 54 gates PASS; 0 finding(s) across 383 TCs
```

TC **383**、leaf **378 / 403 ＝ 93.8%**、節 **123** —— 皆不變。

**本輪未產生 ENTRY 020**，理由：本輪之改動為**兩支量測與一份文件**，
**未觸及任何 TC 之內容**。實測（讀 ENTRY 019 之產出檔與現行 JSON 逐列比對）：
383 列之 `tc_id` 與 `pre_conditions` **完全相同，0 處不符**。

> 46 §3 要求「寫回照常」，其目的是使交付件與 JSON 同步。
> **兩者現已同步**；再產一份位元組相同之檔案並登記一個 ENTRY，
> 只會讓台帳多一列而不多一分資訊。**若分析層要求逐輪留痕，本層照辦。**

---

## 6. 「本包是否仍有該驗而未驗者」（R-C30）

1. **§1 之停用詞表由我列**（含 `vehicle`／`test`／`system` 等測試語彙）——
   探針顯示 `unit`／`configured`／`accordingly` 未被涵蓋；
   **表愈長誤報愈少，也愈容易吞掉真陽性**（若把 `zone` 加入停用詞，
   §1.2 之真陽性就會消失）。
2. **§3 之 20 種為去重後**，第 21 種以下未看；其 run 已降至 9 以下，
   惟未逐一確認。
3. **§4 之 RD-1 清單為草稿，其內容正確性依賴我對 25 個單位之既有記載** ——
   本輪未回頭重讀該 25 節之全文，**引用之片段取自既有記錄**。
4. **§4.2 之紀律自查為 grep**，可抓字串不可抓語氣：
   一句「我們認為應該是 X」不含任何內部語彙，仍違反「不預測答案」。
   我自認未寫此類句子，**惟該項無機器判準**。
5. **未送出**，故其可讀性未經上游檢驗。

---

## 7. 待分析層

1. **§1.2** —— 狀態句量測維持回報或升 FAIL；本層建議維持
   （1 真陽性 : 5 誤報）。
2. **§4.3 之兩處自主判斷**請覆核，尤其文末兩項是否保留於送件版。
3. **§5** —— 未產生 ENTRY 020 之判斷請追認；若須逐輪留痕，本層下輪補一次
   全量重寫並註明其與 019 位元組相同。
4. **RD-1 清單之交付形式與送達**屬 Tier 3（Pei）。
