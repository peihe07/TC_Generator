# 上繳包 22 —— pop-up 組改判、`VP` 之未定義與 `-007` 之事件層限定

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/22_popup_conflict.md](../handoff/22_popup_conflict.md)
  ＋ [../handoff/22a_007_limitation.md](../handoff/22a_007_limitation.md)（同輪併讀）
- 前一包上繳：[21_predicate_criterion.md](21_predicate_criterion.md)
- **本包零寫回工作簿**；**改寫了 `-007` 一條 TC**（R-PMH87）

**21 包之提交狀態**：已於 2026-08-25 經 Pei 授權並提交（`31228a6`，11 路徑）。

---

## ⚠ 本包之三項須先看

1. **我沒有照步驟 2 之字面把五格全改「牴觸」** —— `r6`／`r15`／`r24`／`r25`
   之 pop-up **由 `VP` 承載**，依 **R-PMH85(c)「本條優先」**記為「待定義」；
   只有 `r48`（`Show Pop-Up`，不用 `VP`）記為「牴觸」。**理由見 §2.2，請覆核。**
2. **`matrix_vs_chapter.py` 之 `VERDICT` 鍵不含章號** ——
   以 `matrix_vs_chapter.py 10` 執行會**靜默沿用章 7 之判定**。已修並實測。
   **形態同於 19 包之 `RESIDUE_VERDICT` 鍵碰撞 —— 兩次皆為「鍵不足以識別」。**（§2.3）
3. **章 8 × 矩陣：牴觸 0**，停止條件 7 未觸發。（§6）

---

## 一、§四三條 ＋ 22a 一條之抄錄核對表（步驟 1）

| 條號 | 來源 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH84 | 22 | 條件互斥須被證明，不得被假定 | 605 | `3eb154d9a736b93f` | `3eb154d9a736b93f` | ✅ |
| R-PMH85 | 22 | 素材使用規格未定義之術語 → 標「待定義」並開 DR | 574 | `9ec1d35217e49049` | `9ec1d35217e49049` | ✅ |
| R-PMH86 | 22 | `matrix_vs_chapter.py` 標未實測；三分類之正向錨點 | 393 | `9b5b226ebad5f7f5` | `9b5b226ebad5f7f5` | ✅ |
| R-PMH87 | 22a | `-007` 之事件層限定；不採三案之理由 | 749 | `f660aab26625f0b4` | `f660aab26625f0b4` | ✅ |

**命中數**：handoff 側 4 塊、RULINGS 側回讀 4 塊，`a == b` 皆 `True`。
**既有條文未動**：`R-PMH10`／`R-PMH79`／`R-PMH83` SHA256 皆相符。

---

## 二、pop-up 組之改判（步驟 2）

### 2.1 全簿 pop-up 格之窮舉 —— **21 格，五列，四事件**

| 列 | 事件（列標籤） | **顯示 pop-up 之格** | 其共同條件 | 否定格（`no pop-up`／`not displayed`） |
|---|---|---:|---|---:|
| `r6` | `ON/OFF button Pressed`（Key-on） | **4**（c2／c3／c6／c7） | **全數 `Call Active`** | 0 |
| `r15` | `Key-off`（Key-on 區塊） | **4**（c2／c3／c6／c7） | **全數 `Call Active`** ＋ 僅 `R1High` | 0 |
| `r24` | `ON/OFF button Pressed`（Key-off） | **4**（c2／c3／c6／c7） | **全數 `Call Active`** | 0 |
| `r25` | `Door opened`（Key-off） | **1**（c3） | `Call Active` ＋ `Door = Closed` | **1**（c7 = `VP stays ON, no pop-up`） |
| `r48` | `HVAC Hard Control Adjustment` | **4**（c2／c3／c4／c5） | `Gear != Reverse`（**不涉通話**） | **3**（c6／c10／c11 = `Popup not displayed over RVC`） |

**合計：含 `pop-up` 字樣之格 21；其中顯示者 17、否定者 4。**
**事件列外之非空格含 `pop-up` 者 = 0**（軸／標題皆無）。

**22a §二之表逐項複驗相符** —— 五列、其欄位、`Call Active` 之共同條件，
以及 `r48` 為唯一不倚賴通話者，**四項全部成立**。

**⚠ 停止條件（22a §七：「發現第六個 pop-up 格即停」）之兩讀，據實回報**：

| 讀法 | 實測 | 觸發 |
|---|---|---|
| 「第六個 pop-up **列／事件**」（22a §二之表為五列） | 五列、**四種事件**，**無第六者** | **否** |
| 「第六個 pop-up **格**」（字面） | **21 格** | 字面早已超過六 |

**採前者** —— 22a §二之表以「列」為單位，且 §四之限定亦以「事件」為單位。
**本層據實兩面回報，不自行以目的覆蓋字面**（R-PMH77(c)）。

### 2.2 ⚠ **我沒有照步驟 2 之字面 —— 五格中只有一格改「牴觸」**

下放包步驟 2 令「`r6`／`r15`／`r24`／`r25`／`r48` 五格對 `SU3.)` 之記法
由『未對照』改為**『牴觸』**」。

**我只把 `r48` 改為「牴觸」；其餘四列記為「待定義」。**

**理由**：R-PMH85 逐字載「**本條優先**。若某對照之判定倚賴 `VP` 之指涉，
則其記法為『待定義』而非 R-PMH84 之『牴觸』」，
其後接「**惟 §三之 pop-up 組不倚賴 `VP` 之指涉** ——
`r48` 之 `Show Pop-Up` 未用 `VP` 一詞，其牴觸獨立成立」。

**該句之前半（「pop-up 組不倚賴 `VP`」）涵蓋五列，
而其括號所給之依據（`r48` 未用 `VP`）只涵蓋一列。** 逐格查證：

| 列 | 其 pop-up 之逐字 | 是否用 `VP` |
|---|---|---|
| `r6` | `VP Stays ON Pop-up: Cannot Power Off System during active phone call.` | **是** |
| `r15` | `(R1Low) VP Stays ON (R1High) VP display pop-up: "Power OFF System…"` | **是** |
| `r24` | `VP display pop-up: "Power OFF System. Continue call on mobile phone? Yes or NO"` | **是** |
| `r25` | `VP display pop-up: "Power OFF System…"` | **是** |
| **`r48`** | `Show Pop-Up, Simulated Off Still Active: …` | **否** |

**四列之 pop-up 全由 `VP` 承載。** 若 `VP` 非 head unit 之顯示螢幕，
則其與 `SU3.)` 之 `No pop-ups will appear` **無共同謂詞** ——
**而共同謂詞正是 R-PMH84 判牴觸之前提。**

**故依 R-PMH85(c)，該四列之判定所需之語意尚未存在，記「待定義」。**
`DR-PMH7` `ANSWERED` 後即應改判。**此處請分析層覆核。**

### 2.3 ⚠ **`VERDICT` 之鍵不含章號 —— 本輪查出並修**

首版之鍵為 `(區塊起列, 列)`。**以 `matrix_vs_chapter.py 10` 執行時
會靜默沿用章 7 之判定**，而每列都「有結論」故檢查不會察覺。

已改為 `(章, 區塊起列, 列)`。**實測**：`matrix_vs_chapter.py 10`
現正確報「未具名 30」並 FAIL（改前會報章 7 之結果並 PASS）。

**形態同於 18→19 包之 `RESIDUE_VERDICT` 60 字元鍵碰撞** ——
**兩次皆為「鍵不足以識別其所指」，兩次皆是在做別的事時撞出來的。**

### 2.4 章 7 之重記結果

```
=== 結果 ===
  牴觸 **1**／印證 **0**／未對照 **25**／待定義 **4**；未具名 **0**
  ← **停止條件觸發**：發現牴觸，須上呈，不得自行調和（R-PMH79）
```

**21 包 §3.2 之「牴觸 0／未對照 30」已以勘誤更正**（其原文一字未改，R-PMH44），
勘誤中並記入 §2.3 之鍵缺陷。

---

## 三、`-007` 之改寫（22a 步驟 8，R-PMH87）

### 3.1 複驗 22a 之擬案 —— **四項事件窮盡矩陣之 pop-up 格，成立**

17 個顯示格全數繫於四個事件（其列標籤即該事件）：
`ON/OFF button Pressed`（8 格）／`Key-off`（4）／`Door opened`（1）／
`HVAC Hard Control Adjustment`（4）。**排除該四事件即排除全部 17 格。**

**R-PMH84 所要求之「條件互斥之證明」由 TC 自身之構造成立** ——
不是靠推論矩陣「不涉及 disclaimer 期間」（那正是被 R-PMH84 推翻者）。

### 3.2 改寫後之 procedure／ER（**拆為兩步**，R-PMH87 實施 1）

```
procedure                                                      字數
1. Do not press the ON/OFF key and do not turn key-off          11
2. Do not open any door and do not adjust HVAC hard controls    12
3. Deliver a traffic announcement while the disclaimer screen
   is displayed                                                 10
4. Read the screen and the audio output and record both         10
5. Remove the disclaimer screen and check that the pop-up
   is displayed                                                 11

expected_result
1. No ON/OFF key press and no key-off transition occurs
2. No door is opened and no HVAC hard control is adjusted
3. The traffic announcement is delivered
4. The announcement is heard in the background and no pop-up is displayed
5. The traffic announcement pop-up is displayed
```

**§5.2 之字數檢查通過**（normal <= 12／final <= 18）；
**procedure 與 ER 5:5 逐位對齊**；**lint 30/30**。
**四項限定一項未刪** —— 缺一即漏一格（R-PMH87 實施 1）。

**未以 `R1Low` 限定 `r15`**（R-PMH87 實施 2）—— `SU3.)` 全稱適用於所有變體。

### 3.3 `reasoning` 之新增段（逐字）

> ⚠ **R-PMH84／R-PMH87 —— 事件層限定**：State Matrix（規範性文件，PDF p10 `shall not be developed without following`）之 pop-up 顯示格共 **17 個**，分布於五列：`r6` `ON/OFF button Pressed`(4)／`r15` `Key-off`(4)／`r24` `ON/OFF button Pressed`(4)／`r25` `Door opened`(1)／`r48` `HVAC Hard Control Adjustment`(4)。**全數繫於四個事件**，且四者皆為測試員可控之操作，故 procedure 步驟 1、2 排除之 —— **排除事件即排除全部 17 格**，R-PMH84 所要求之「條件互斥之證明」由 TC 自身之構造成立，非由對矩陣涵蓋範圍之推定成立（21 包之推定已被推翻）。不採 `No phone call is active`（`r48` 不涉通話，不充分）、不採 `Gear != Reverse`（只擋 `r48` 之一部）、不採以 `R1Low` 限定 `r15`（`SU3.)` 全稱適用於所有變體，違 R-PMH55(a)）。**連帶之覆蓋缺口三項見 ANOMALIES A-PMH19。**

---

## 四、`DR-PMH7` 之開立（步驟 4）

已登記，狀態 **`DRAFT`**，可寄出全文已備妥（`DATA_REQUESTS.md` §DR-PMH7）。

**Pei 於 2026-08-25 逐字表明「`DR-PMH5`／`6`  DR-PMH7 我處理」** ——
三筆之發出由 Pei 為之，**執行層未代為發出**（R-PMH83）。

**A-PMH20 已登記**：`VP` 於規格 PDF 全 11 頁 **0 命中**、Excel **30 格**，
其三種用法逐字在案。

---

## 五、R-PMH86 之正向錨點（步驟 5）

```
=== R-PMH86 —— 三項正向錨點（四分類之機制驗證）===
**本錨點驗機制，不驗判斷** —— `VERDICT` 之記法由人寫入，本檢查只驗其能被正確讀出、計數並影響退出碼。

  (10, 37, 48)     期望 **牴觸** → 實得 **牴觸**  ✅
      謂詞：`HVAC pop-up 是否顯示` —— `PITA6` `shall be … displayed`／`r48c10` `Popup not displayed over RVC`
  (10, 37, 40)     期望 **印證** → 實得 **印證**  ✅
      謂詞：`Power 鍵之輸入是否被忽略` —— `PITA4` `shall be ignored while backup cam is being shown`／`r40` 之 `Gear = Reverse` 欄 `Event ignored`
  (10, 37, 44)     期望 **印證** → 實得 **印證**  ✅
      謂詞：`Screen Off 鍵之輸入是否被忽略` —— 同上／`r44` 之 `Gear = Reverse` 欄 `Event ignored`
  (10, 1, 10)      期望 **未對照** → 實得 **未對照**  ✅
      謂詞：`Projection 之後果` —— ch 10 全文無 Projection

  計數：{'牴觸': 1, '印證': 2, '未對照': 1}
  含牴觸 1 件 → 退出碼 **1**（牴觸須使檢查非 0 退出）
  退出碼行為正確：True

  (d) 未具名之鍵不在表中 → 主流程會記 FAIL：True

==================================================================
三項正向錨點: True；退出碼行為: True；未具名攔截: True
```

**三項錨點全部報出其應報之記法；含牴觸時退出碼為 1；未具名之鍵會被主流程攔下。**

**⚠ 本錨點所驗者為機制，非判斷** —— `VERDICT` 之記法由人寫入，
本檢查只驗「所寫之記法能被正確讀出、計數、並影響退出碼」，
**它無法證明某一列之記法判對了**。已寫入 `LIMITS`。

**依 R-PMH86，`matrix_vs_chapter.py` 之結果於錨點通過前只得標「未實測」——
本輪錨點已通過，故 §10 之總表得標 PASS，惟其 PASS 之含意限於上述機制。**

---

## 六、章 8 × 矩陣之全對照（步驟 6）

### 6.1 範圍向

```
--- 範圍向：章 8 之關鍵名詞於矩陣之命中 ---
    0  sound
    0  Sound
    0  start-up
    0  startup
    0  goodbye
    0  Always
    0  Once a Day
    0  Never
    0  volume
    0  Volume
    0  entertainment
    0  setting
    0  Setting
    0  played
    0  plays
    0  sync

  命中之名詞 = **0/16** —— **全部 0 命中**
  ⚠ 字面比對；`0 命中` 為 `未對照` 之**支持證據**，非其證明（見 LIMITS）。
```

**十六個名詞全部 0 命中。**
**⚠ 兩處子字串偽命中已修**：純子字串比對使 `play` 命中 `display` **19 次**、
`played` 命中 `displayed` **3 次**；**探針已字界錨定**，二者歸零。

### 6.2 逐列結果

```
=== 結果 ===
  牴觸 **0**／印證 **0**／未對照 **30**／待定義 **0**；未具名 **0**
```

**牴觸 0／印證 0／未對照 30／待定義 0；未具名 0。停止條件 7 未觸發。**

### 6.3 最接近之三列（已具名）

| 列 | 為何接近 | 其條件互斥之依據（R-PMH84 要求具名） |
|---|---|---|
| `r16`（`Radio Wakes Up and mutes`） | ch 8 之 `SSND 2.1)` 謂「設定為 Always 時啟動音應播放」 | 本列為 **Off Road+／SRT 之喚醒**，其靜音即**規格自身 `OFF3.)`（12.3）所載** —— `Head unit is muted when launching app from Power Off State.`。**互斥之依據為規格文字本身，非假定** |
| `r45`（`Mute Button Pressed`） | 其謂詞確為靜音狀態 | 其觸發為**使用者按 Mute 鍵**，`SSND 2.1)` 之條件為「開機動畫播放時」。**條件互斥** |
| `r8`／`r30`（`Door closed` → `Event ignored`） | `SSND 1)` 之觸發亦為 `upon driver door close` | 本列之格為**事件是否被處理**，未提聲音；且矩陣之 `Door` 軸**未區分駕駛門**。**無共同謂詞** |

**⚠ 一項判斷須具名**：「`mute` 是否即 `SSND` 所稱之 sounds 不被播放」
**為本層之判斷，非量測**（見 §13 第 2 項）。

---

## 七、停止條件 8 之偽陰抽樣（步驟 7，R-PMH67）

母體：`docs/upstream/*.md` 中含八個候選措詞之一**而不含「無矛盾」「非牴觸」**
之行 = **124**；抽樣 N = 10，種子 **22**（可重現）。

```
  **偽陰率之點估計 = 1/10 = 10%**；**Wilson 95% 區間 = [2%, 40%]**
  推估母體 124 行中應被攔者：點估計 **12** 行，**區間 [2, 50] 行**
```

**十行中只有一行應被攔**（`03_testgroup_and_dv.md:138`，
「母本 DV 之 priority 值 vs canon §10.2」以「三方一致」記之 ——
**與 `10.5` 之「一致（軸層面）」同型**，21 §2 已改記為未對照）。

**其餘九行皆非對照結論**：五行為**同值查核**（identity，如
`重新產生亦一致`／`靜態彙集與執行期一致`／`diff = 0`）、
二行為條文或檢查項之**名稱**、一行為 anomaly 之**描述**、
一行為停止條件之**自檢**。

**故偽陰率低（10%）之原因不是判準好，是對照結論本身很少** ——
124 行之母體中，真正為「規格 × 素材之對照結論」者屈指可數。
**這個數字不宜被讀成「該判準夠用」。**

---

## 八、lint 全跑輸出

```
batch = batch01；TC 數 = 8；leaf 數 = 7

  R-PMH50 每 leaf 有 source_clause 且非空                       PASS
  R-PMH50 source_clause 取自 PDF（非 SYS1）                     PASS
  profile §3.1 test_item 具下半括號（硬規則）                        PASS
  profile §3.3 design_method ∈ 下拉選單 9 詞條                   PASS
  profile §3.4 spec_reference 形態且與 layer3_sections.tsv 相符  PASS
  profile §3.5 priority ∈ {P0,P1,P2,P3}（母本 DV）             PASS
  profile §3.6 estimated_test_time 留白                      PASS
  profile §3.8 vehicle_models 留白                           PASS
  profile §3.7 functional_safety = NA                      PASS
  R-PMH18 test_group = 'Disclaimer screen'（小寫 s）           PASS
  R-PMH36 test_set = 'Disclaimer Screen'（大寫 S）             PASS
  R-PMH16 tc_id 形態 NR1L-DisclaimerScreen-{NNN}             PASS
  test_set ∈ Layer 2 定版 8 組                                PASS
  canon §11 方括號禁止（本 feature 無 profile 例外）                  PASS
  procedure 與 ER 步數一致                                      PASS
  必填欄無空                                                    PASS
  ER 未以 NA 充當未知                                            PASS
  canon §10.5 test_procedure >= 2 步                        PASS
  canon §5.1 procedure 無禁用動詞                               PASS
  canon §5.2B/§5.5 Final Step 含驗證意圖                        PASS
  canon §4.3.1 test_item 上半 ⊆ source_clause（verbatim）      PASS
  交付欄位無 markdown 標記（**／__／`）                               PASS
  canon §11 無彎引號                                           PASS
  canon §11 UI 標籤加直雙引號                                     PASS
  canon §5.2 步驟字數（normal <=12／final <=18）                  PASS
  R-PMH53 交叉引用存在且語意相容                                      PASS
  procedure／ER 編號自 1 起連號且逐位對齊                              PASS
  tc_id 唯一                                                 PASS
  tc_id_status = provisional                               PASS
  本批 leaf == Disclaimer Screen 之 7 leaf                    PASS

30/30 PASS

⚠ **本 lint 未涵蓋之 canon 節號（R-PMH52／R-PMH56）**：
    由 `scripts/canon_coverage.py` 自 canon 之節號全集減去上方 `COVERED` 產生，**不手寫**。
    執行：`python scripts/canon_coverage.py`
    本 lint 宣告涵蓋 10 節：['10.2', '10.3', '10.5', '10.7', '11', '4.3.1', '5.1', '5.2', '5.5', '8.4.3']
    （R-PMH58：靜態彙集與本次實際執行到之檢查點一致）
    **以上以外之全部 canon 節皆未由本 lint 檢查，須人讀。**
    R-PMH52：lint 全綠不得作為 TC 可用之證據。

⚠ R-PMH50 之限度：本 lint 只驗 source_clause **存在且取自 PDF**。
  **「是否忠於規格」不可機械檢查** —— 須人讀 PDF 原文與 TC 對照。
  本檢查只保證覆核所需之材料存在，不保證覆核已做。
```

**must-hit 兩份 fixture 仍 FAIL**：`batch01_prerework` 21/30／`batch01_r2` 29/30。

---

## 九、未結 DR 清單（R-PMH82 之四級）

| DR | 主旨 | 狀態 | 發出日期 | 阻斷 |
|---|---|---|---|---|
| **DR-PMH5** | PDF p9 之能力矩陣之來源文件 | **`DRAFT`** | **（待填）** | **ch 9 開批** |
| **DR-PMH6** | RVC 情境之 HVAC popup ＋ **三項覆蓋缺口**（本包增補） | **`DRAFT`** | **（待填）** | 否 |
| **DR-PMH7** | `VP` 之定義 | **`DRAFT`** | **（待填）** | 矩陣對照之四列判定；不阻斷 batch 1 |

**合計未結 3 筆，三者皆 `DRAFT`。**

**A-PMH19 之歸屬採（甲）**：`DR-PMH6` 之發出日期欄空白 → 依 R-PMH82 為
`DRAFT` → 直接增補其全文。**若 Pei 實際已發出，請改採（乙）另開 `DR-PMH8`。**
**執行層無從得知其是否已發出** —— 此正是 R-PMH82 所要解決之事，
**而該欄目前仍空著。**

---

## 十、檢查總表

| 檢查 | 結果 |
|---|---|
| `lint_batch.py generated/batch01.json` | **30/30 PASS**（含改寫後之 `-007`） |
| **`matrix_vs_chapter.py 7`** | 牴觸 **1**／未對照 25／**待定義 4**；未具名 0 → **退出碼 1（設計如此）** |
| **`matrix_vs_chapter.py 8`** | **PASS** —— 30 列全具名、牴觸 0 |
| **`matrix_vs_chapter.py --must-hit`** | **PASS** —— 三項正向錨點 |
| **`wording_sample.py`** | **PASS** —— 偽陰 1/10，Wilson [2%, 40%] |
| `chapter_bidirectional.py` 六章／`--partition`／`--source-must-hit`／`--export-residue` | **全 PASS** |
| `check_granularity.py` 三模式／`challenge_rulings.py`／`tsv_vs_pdf.py --truncation` | **PASS** |
| `marker_coverage.py`／`canon_coverage.py`／`check_state_consistency.py`／`check_write_back.py` | **PASS** |

---

## 十一、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | **是** —— p9 能力矩陣（`DR-PMH5`）＋ `VP` 未定義（`DR-PMH7`） |
| 2 | 判準衝突未決 | **是** —— `10.3` 之牴觸；`r48` × `SU3.)` 之牴觸（本包新增） |
| 3 | 須寫回而工作簿狀態不明 | 否（零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論建於臆測 | **是** —— 同 1 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| 7 | 章 8 × 矩陣發現**新的**牴觸 | 牴觸 **0**（30 列全具名） | **否** |
| 8 | 三項正向錨點有任一項未報出其應報之記法 | 三項全對 | **否** |
| 9 | 改判後有任一格之「牴觸」未具名其共同謂詞 | `r48` 已具名（`pop-up 是否顯示`，全稱否定 vs 無條件肯定） | **否** |

22a §七之停止條件（第六個 pop-up 格）：**依「列／事件」之讀法未觸發**（§2.1）。

---

## 十二、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，六項。**

1. **§2.2 之決定是我在兩條裁決條文之間做的選擇。**
   R-PMH85 說「本條優先」而其括號之依據只涵蓋 `r48`；
   下放包步驟 2 說五格全改牴觸。**二者不能同時滿足，我選了條文而非步驟。**
   **我認為條文優先於步驟是對的，但那是我的判斷，不是誰授權的。**

2. **§6.3 之「`mute` 是否即 sounds 不被播放」是判斷不是量測。**
   若二者為同一謂詞，則 `r45`（使用者按 Mute 鍵）與 `SSND 2.1)` 之
   條件互斥性我給的依據（「觸發不同」）**還算成立**；
   **但 `r16` 我引的是規格自身之 `OFF3.)`，那條在 ch 12** ——
   **以另一章之條文證明本章之條件互斥，其正當性我沒有查過。**

3. **章 8 之 30 列判定，其中 24 列之依據是同一句「ch 8 全文無此事件之敘述」。**
   那句話成立，**但它證明的是「規格沒說」，不是「二者條件互斥」** ——
   R-PMH84 要求的是後者。**嚴格說，「規格沒有對應敘述」屬 R-PMH79 之
   「無對應列」一支，我用對了記法，惟依據之措詞不夠精確。**

4. **`-007` 之四項限定排除了 17 格，而我沒有驗「排除之後 `SU3.)` 之
   斷言就成立」。** 矩陣只是**規範性素材之一**；
   規格 PDF 本身是否另有會在免責畫面期間產生 pop-up 之敘述，
   **我沒有反向掃過**（如 `PITA9` 之 phone call popups —— 其屬 ch 10，
   而 `-007` 之限定不含「無來電」）。

5. **`wording_sample.py` 之母體界定（八個候選詞）本身是列舉。**
   §7 已具名，**但我沒有對那八個詞再做一次抽樣** ——
   R-PMH67 之形態在此**只套了一層**。

6. **本包改寫了一條 TC（`-007`），而 batch 1 之其餘七條未依 R-PMH84 重看。**
   `-002`／`-003`／`-004` 之 ER 是否也與矩陣之某格取相反值，
   **我只查了 `-007` 所依之 `SU3.)`。** ch 7 × 矩陣之 30 列判定
   涵蓋的是「章」層，**不等於逐條 TC 之 ER 都被對照過**。

---

## 十三、建議之 commit 與 pathspec（**不執行**）

**訊息**：

```
feat(power_moding): package 22 — popup group reclassified, VP undefined (DR-PMH7), -007 event-layer limitation
```

**pathspec（12 路徑，R-G12 —— 逐一具名）**：

```
git commit -- \
  features/power_moding/ANOMALIES.md \
  features/power_moding/DATA_REQUESTS.md \
  features/power_moding/RULINGS.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/22_popup_conflict.md \
  features/power_moding/docs/handoff/22a_007_limitation.md \
  features/power_moding/docs/upstream/21_predicate_criterion.md \
  features/power_moding/docs/upstream/22_popup_conflict.md \
  features/power_moding/generated/batch01.json \
  features/power_moding/scripts/gen_batch01.py \
  features/power_moding/scripts/matrix_vs_chapter.py \
  features/power_moding/scripts/wording_sample.py
```

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py`／`docs/runtime/`／`PROFILE_INTEGRATION.md`／profile | **未動** |
| 工作簿寫回 | **無** |
| `generated/batch01.json` | **`-007` 一條改寫**（procedure 3→5 步、ER 3→5、reasoning 增段）；其餘七條未動 |
| State Matrix xlsx | **只讀**（`data_only=True`，未 `save`） |
| **對外發文** | **無** —— 三筆 DR 皆 `DRAFT`，Pei 表明自行處理 |
| 已執行之 git 狀態變更指令 | **無** |
| 併行 session（`vehicle_setting`）之檔案 | **未動** |

---

## 十四、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **§2.2 之覆核** —— 四列記「待定義」而非「牴觸」，我在條文與步驟之間選了條文 | 矩陣對照之四列 |
| 2 | **`DR-PMH6` 是否已發出** —— 決定 A-PMH19 三項採（甲）增補或（乙）另開 `DR-PMH8` | 否 |
| 3 | `DR-PMH5`／`6`／`7` 之發出 ＋ **日期與對象**（以便改標 `SENT`） | `DR-PMH5` 阻斷 ch 9 |
| 4 | **§12 第 4 項** —— `-007` 之限定只排除了矩陣之 pop-up；**規格自身（如 `PITA9`）之 pop-up 未反向掃過** | batch 1 之寫回 |
| 5 | §12 第 6 項 —— batch 1 其餘七條未依 R-PMH84 逐條對照 | batch 1 之寫回 |
| 6 | 章 11 × 矩陣之對照（`VRLP1` vs `r11`／`r12`／`r28`／`r29`） | 該組開批前 |
| 7 | 9.1 之 `source_clause` 例外是否寫入 profile；17 §5.4 其餘五項；Q10 | 否 |
