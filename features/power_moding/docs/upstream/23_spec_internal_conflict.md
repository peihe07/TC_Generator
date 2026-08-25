# 上繳包 23 —— 規格內部之牴觸、batch 1 之逐條對照與章 11

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/23_spec_internal_conflict.md](../handoff/23_spec_internal_conflict.md)
- 前一包上繳：[22_popup_conflict.md](22_popup_conflict.md)
- **本包零寫回工作簿**；只改 `-007` 之 `reasoning`（依據擴充），**限定與 ER 未動**

**22 包之提交狀態**：已於 2026-08-25 經 Pei 授權並提交（`273594e`，12 路徑）。

---

## ⚠ 本包之三項須先看

1. **A-PMH21 之列位與分析層所報不同，且更正後牴觸更強** ——
   `Pop-ups still shown` 之兩處在 **`KEY ON ENGINE ON`** 與
   **`KEY ON ENGINE OFF (ACC or RUN)`** 兩列，**非** `KEY OFF` 兩列。
   **免責畫面之相位正是 `KEY ON`** —— 條件不僅「未證互斥」，而是**高度可能重疊**。（§2）
2. **batch 1 其餘七條之 18 條 ER 斷言逐條對照完畢：牴觸 0、印證 1。**（§5）
3. **第二層抽樣查出一整類漏網措詞：「非漏」** ——
   `RESIDUE_VERDICT` 之 20 條多以其起首，**而停止條件 8 完全攔不到**。（§7）

---

## 一、§四三條之抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH88 | 條文優先於步驟；描述與被描述者相衝時錯在描述 | 317 | `1feb1c559eb1374a` | `1feb1c559eb1374a` | ✅ |
| R-PMH89 | 規格內部之牴觸；不得以「以規格為權威」解之 | 507 | `95189413b2b17a98` | `95189413b2b17a98` | ✅ |
| R-PMH90 | 斷言類之限定須經規格全文反向掃描 | 406 | `319bfcb85c10532a` | `319bfcb85c10532a` | ✅ |

**命中數**：handoff 3 塊、RULINGS 回讀 3 塊，`a == b` 皆 `True`。
**既有條文未動**：`R-PMH10`／`R-PMH85`／`R-PMH87` SHA256 皆相符。

**R-PMH88 之效力已生**：22 包 §2.2 之選擇（依條文而非步驟）自此不再由執行層承擔。

---

## 二、`A-PMH21` —— 規格內部之牴觸（步驟 2）

### 2.1 兩造逐字

| 出處 | 逐字 | 形態 |
|---|---|---|
| **p8 `SU3.)`**（outline 7.4） | `No pop-ups will appear until the disclaimer screen has been removed.` | **全稱否定** |
| **p9 能力矩陣，`HVAC Knobs` 格（兩處）** | `HVAC Knobs: Fully functional. `**`Pop-ups still shown.`** | **無條件肯定** |

### 2.2 ⚠ **其列位與分析層 §3.2 所報不同 —— 以座標複驗後更正**

分析層記其為「`KEY OFF (ACC)` 與 `KEY OFF (No ACC)` 兩列」。**實測不然**：

| 出現 | 座標 | 所屬列（其標籤之座標） | 欄 |
|---|---|---|---|
| 第 1 次 | x=428, **y=81** | **`KEY ON ENGINE ON`**（y=114） | `HEADUNIT POWER OFF` |
| 第 2 次 | x=428, **y=180** | **`KEY ON ENGINE OFF (ACC or RUN)`**（y=197） | `HEADUNIT POWER OFF` |

**`KEY OFF` 兩列之 `HVAC Knobs` 格逐字為 `OFF`，無 pop-up 之敘述**
（21 包 §3 之章 9 殘餘已錄其逐字）。

**該更正使牴觸更強而非更弱**：免責畫面之相位**正是 `KEY ON`**
（`SU1.)` 之開機序列；`PITA6.1` 之 ignition OFF → ACC／RUN）。
**二者之條件不僅「未證互斥」，而是高度可能重疊。**

### 2.3 判定與處置

- 共同謂詞：**pop-up 是否顯示**；取相反值；條件互斥**未證且證據指向重疊** → **牴觸**（R-PMH84）。
- **不得以「以規格為權威」解之**（R-PMH89 明文）—— 兩造皆是規格（同一份 PDF）。
- 處置：**限縮 ＋ 揭露，不裁權威**。`-007` 之四項限定已含「不操作 HVAC 硬控」，
  而 p9 該格所述之情境即 HVAC 旋鈕之操作 —— **限定不必增加**。

---

## 三、`DR-PMH5` 之增補（步驟 3）

其狀態仍為 **`DRAFT`**（發出日期欄空白）→ 依 22 包所立之二擇一形態採（甲），
**直接增補其全文**，增列第三問：

> (3) p9 之能力矩陣，其 `Pop-ups still shown` 與 p8 之 `SU3.)` 應如何並存？
>     是否 `SU3.)` 本該寫成有條件句（排除 HVAC pop-up），
>     或該矩陣格本該註明其不適用於免責畫面期間？

並附兩造逐字與**以座標實測之列位**。

**⚠ 若 Pei 實際已發出 `DR-PMH5`，此項須改以 `DR-PMH9` 另開。**
**執行層無從得知其是否已發出**（發出日期欄仍空著）——
**此為 R-PMH82 所要解決之事，而該欄第二次空著。**

---

## 四、`-007` 之 `reasoning` 擴充（步驟 4，R-PMH90）

**限定本身未動**（四項事件）；**ER 與 procedure 未動**；只擴充 `reasoning` 之依據。

新增段之逐字：

> ⚠ **R-PMH90 —— 規格側之反向掃描（23 包）**：只掃素材不足以主張限定充分。以 `pop-up`／`popup`／`pop up` 掃規格 PDF 全文得 **25 行**（匹配 30 次），逐行判定：印證 5（`Geolocation + SOS Popup` 於流程圖中位於免責畫面之後；`GDPR/SOS popup` 明載其條件為**免責畫面被跳過**）／未對照 16（`PM1)` 之 IGN OFF popup 群 12 行、`PITA6`／`6.1`／`9` 之 Power Button Off 相位 3 行、重複顯示之謂詞 1 行）／**牴觸 2**（p9 能力矩陣之 `HVAC Knobs: Fully functional. Pop-ups still shown.`，見 A-PMH21）。**該 2 行之情境為 HVAC 旋鈕之操作，已為本條四項限定中之「不操作 HVAC 硬控」所涵蓋，故限定不必增加** —— 惟其依據自此為「矩陣之 17 格 ＋ 規格 p9 之 2 行」。⚠ **殘餘風險具名**：四項限定**不含「無來電」**；`PITA9` 之 phone call popup 於免責畫面相位是否顯示，**規格未表態**（其只述 `Power Button Off state`）。

### 4.1 反向掃描之實跑（新增 `scripts/spec_assertion_scan.py`）

```
=== 結果 ===
  {'印證': 5, '未對照': 16, '—': 2, '牴觸': 2}；未具名 **0**

  **牴觸 2 行** —— **規格內部之牴觸（R-PMH89），A-PMH21**

  **與分析層 23 §3.1 之對照**：其報「25 處」，本檔行數 **25** —— **相符**；
  其所報之行號（131／147／155／263／144／164／341／357／416–439／453／455／460）
  與本檔（127／143／151／257／140／160／332／348／407–430／443／445／450）**逐一相差 4~13**，
  **因二者之文字萃取不同**（分析層用 `pm.txt`，本檔用 `fitz` 逐頁串接）。
  **其分類（牴觸 2／印證 5／未對照 18）與本檔逐項相符**（本檔之印證 5 含 L140；`SU3.)` 自身 2 行本檔另計為 `—`，分析層併入未對照）。
```

**停止條件 9 之判定**：分析層 §3.1 報「25 處」，本檔**行數 25 —— 相符**。
**行號逐一相差 4~13，因二者之文字萃取不同**（分析層 `pm.txt`／本檔 `fitz` 逐頁串接）；
**分類（牴觸 2／印證 5／未對照 18）逐項相符**
（本檔另將 `SU3.)` 自身 2 行計為 `—`，分析層併入未對照）。
**差異已查明 → 停止條件 9 未觸發。**

**計數單位須明說**：**匹配數 30、行數 25** —— 二者皆列出，不混用。

### 4.2 `r6` 之斷句歧義（22 §2.2 之連帶）

`r6` 逐字為 `VP Stays ON Pop-up: Cannot Power Off System during active phone call.`
—— 可斷為兩句（`VP Stays ON` ／ `Pop-up: …`，則 pop-up 之存在**不繫於 `VP`**），
亦可讀為一句（繫於 `VP`）。

**現階段維持「待定義」**（歧義本身即待定義之一部分）；
**`DR-PMH7` 回覆後，`r6` 須與其餘三列分開重看** —— 其歧義不在 `VP` 之指涉，
**而在該格之斷句**。已記於 `matrix_vs_chapter.py` 之 `r6` 依據欄。

---

## 五、batch 1 其餘七條之逐條 ER 對照（步驟 5）

新增 `scripts/batch_er_vs_matrix.py`。母體：**7 條 TC、18 條 ER 斷言**
（`-007` 已於 22 包單獨處置，不入母體）。

```
=== 結果 ===
  ER 斷言 **18** 條；牴觸 **0**／印證 **1**／未對照 **17**／待定義 **0**；未具名 **0**
```

### 5.1 唯一之**印證**：`-008` ER2 × 矩陣 `r6` c12／c13

| | 逐字 |
|---|---|
| `-008` ER2 | `The radio changes to On state` |
| 矩陣 `r6` c12／c13（`Key-on` × `ON/OFF button Pressed` × `Power Button OFF` × **`Call Not Active`**） | **`Head Unit Power ON`** |

**同一謂詞取相同值，且條件相符** —— `-008` 之 pre-condition 已含
「無通話情境進行中」（`PITA6.1` 之 `unless certain phone call scenarios have
occurred`），**恰對應 `Call Not Active` 欄**。**矩陣為該 ER 之獨立佐證。**

### 5.2 其餘 17 條皆為「未對照」，其依據分三類

| 類 | 條數 | 依據 |
|---|---:|---|
| **素材無對應列** | 13 | `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` 於矩陣 **全數 0 命中** |
| **不同謂詞** | 3 | `-002`／`-004` 之 ER（按 Accept 後之畫面）vs `r33`（Key-on 後回復 VP 狀態）；`-005` 之 comfort controls（畫面）vs `HVAC Knobs`（硬體旋鈕） |
| **無可相反之值** | 1 | `-008` ER1 為**記錄前提狀態**，非斷言某事件之後果 |

**牴觸 0 → 停止條件 7 未觸發。**

---

## 六、章 11 × 矩陣之對照（步驟 6）

```
=== 結果 ===
  牴觸 **0**／印證 **2**／未對照 **28**／待定義 **0**；未具名 **0**
```

**牴觸 0／印證 2／未對照 28；未具名 0。停止條件 8 未觸發。**

### 6.1 兩處**印證**

| 列 | 矩陣逐字 | `VRLP1` 之對應 |
|---|---|---|
| `r11`（VR 長按，**無** Projection） | `Head Unit Remain OFF See CFTS009` | 其四種容許結果之一：`Screen Off and Audio OFF (i.e. radio back to off)` |
| `r12`（VR 長按，**Projection 中**） | `Head Unit Power ON See CFTS009` | 其四種容許結果之一：`Screen ON and Audio ON` |

**二者之條件皆落在 `VRLP1` 之條件內**（`radio is OFF and KEY ON or ACC`；
矩陣為 `Key-on` 區塊 × `Power Button OFF`）。

**矩陣補上了規格所無之區辨**：`VRLP1` 只說「結果視互動而定」而未言何時取何者，
**矩陣以 `Projection` 之有無區辨之**。
⚠ 該區辨**只在矩陣有、規格未載**，依 R-PMH55(b) 不得為其單獨撰 TC。

### 6.2 `r28`／`r29` 之未對照，其互斥依據**由規格自身給出**

二者屬 `Key-off` 區塊，而 `VRLP1` 之條件逐字為
`shall be functional when radio is OFF and **KEY ON or ACC**`
—— **在其條件之外**。R-PMH84 所要求之互斥證明由規格文字提供，非假定。

### 6.3 一項須具名者

`r11`／`r12`／`r28`／`r29` **四列與 `VRLP1` 皆註 `See CFTS009`** ——
**該文件不在本 feature 之六筆素材內**（A-PMH13 之同型）。
**本次之「印證」建立在二者之可見部分上，其所指之 CFTS009 內容雙方皆未見。**

---

## 七、停止條件 8 之第二層抽樣（步驟 7）

### 7.1 第一層（重跑）

```
  **偽陰率之點估計 = 1/10 = 10%**；**Wilson 95% 區間 = [2%, 40%]**
  推估母體 130 行中應被攔者：點估計 **13** 行，**區間 [2, 53] 行**
```

**⚠ 母體由 22 包之 124 行增為 130 行** —— 新增之上繳文件（21 之勘誤、22）
使**種子固定而樣本全數更換**。已寫入 `LIMITS`：
**「種子固定不保證樣本固定；本檔之抽樣結果須與其執行時之母體大小併讀。」**

新樣本之唯一「應被攔」：`02_baseline_switch.md:121` ——
「037 之 `Priority` 欄實測值即為 `High` 等，**二者一致**。**本包未實測母本**」
—— **一個以「一致」作結而其一造未實測之對照結論。**

### 7.2 第二層

```
  **偽陰率之點估計 = 2/10 = 20%**；**Wilson 95% 區間 = [6%, 51%]**
  推估母體 332 行中應被攔者：點估計 **66** 行，**區間 [19, 169] 行**
```

**兩處「應被攔」，其一為本包最重要之發現**：

| 出處 | 措詞 | 為何重要 |
|---|---|---|
| `03_testgroup_and_dv.md:182` | 「**未造成任何逸出**」 | 對照結論（兩組字串）以完全在列舉外之措詞作結 |
| **`18_break_the_circle.md:107`** | 「**非漏（散文側）**」 | **「非漏」是一整類對照結論之措詞** —— `RESIDUE_VERDICT` 現有 **20 條，多數以其起首**，而停止條件 8 **完全攔不到** |

**第二層偽陰率 2/10 = 20%，Wilson [6%, 51%]；推估母體 332 行中 [19, 169] 行。**

### 7.3 兩層之結論

| 層 | 母體 | 點估計 | Wilson 95% |
|---|---:|---:|---|
| 1 | 130 | 10% | [2%, 40%] |
| 2 | 332 | **20%** | [6%, 51%] |

**第二層之偽陰率高於第一層** —— 且其查出之「非漏」一詞，
**其使用量遠大於停止條件 8 所攔之二詞**。
**「列舉式判準」之問題不在其漏了幾個詞，在於漏掉的可能正是用最多的那個。**

**第三層未量**：第二層之母體以 `CONTEXT` 六個標記界定，**其本身又是列舉**。
R-PMH67 之形態在此**只套了兩層，其收斂與否未知**。

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
| **DR-PMH5** | p9 能力矩陣之來源 ＋ **其自身與 `SU3.)` 之牴觸**（本包增補） | **`DRAFT`** | **（待填）** | **ch 9 開批** |
| **DR-PMH6** | RVC 情境之 HVAC popup ＋ 三項覆蓋缺口 | **`DRAFT`** | **（待填）** | 否 |
| **DR-PMH7** | `VP` 之定義 | **`DRAFT`** | **（待填）** | 矩陣對照之四列；不阻斷 batch 1 |

**合計未結 3 筆，三者皆 `DRAFT`。發出日期欄第二次空著。**

---

## 十、檢查總表

| 檢查 | 結果 |
|---|---|
| `lint_batch.py generated/batch01.json` | **30/30 PASS** |
| **`spec_assertion_scan.py`**（新） | **PASS** —— 25 行全具名；牴觸 2（A-PMH21） |
| **`batch_er_vs_matrix.py`**（新） | **PASS** —— 18 條 ER 全具名；牴觸 0、印證 1 |
| **`matrix_vs_chapter.py 11`** | **PASS** —— 30 列全具名；牴觸 0、印證 2 |
| `matrix_vs_chapter.py 8`／`--must-hit` | **PASS** |
| `matrix_vs_chapter.py 7` | 牴觸 1／待定義 4（退出碼 1，設計如此） |
| **`wording_sample.py`**／`--layer2` | **PASS** —— 10%／**20%** |
| `chapter_bidirectional.py` 六章／三模式 | **全 PASS** |
| `check_granularity.py` 三模式／`challenge_rulings.py`／`tsv_vs_pdf.py --truncation` | **PASS** |
| `marker_coverage.py`／`canon_coverage.py`／`check_state_consistency.py`／`check_write_back.py` | **PASS** |

---

## 十一、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | **是** —— p9 能力矩陣（`DR-PMH5`）＋ `VP` 未定義（`DR-PMH7`） |
| 2 | 判準衝突未決 | **是** —— `10.3`／`r48`／**A-PMH21（規格內部）** |
| 3 | 須寫回而工作簿狀態不明 | 否（零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論建於臆測 | **是** —— 同 1 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| 7 | 步驟 5 之逐條對照發現**新的**牴觸 | 18 條 ER，牴觸 **0** | **否** |
| 8 | 步驟 6 之章 11 對照發現**新的**牴觸 | 30 列，牴觸 **0** | **否** |
| 9 | 步驟 4 之反向掃描與分析層之 25 處分類不符**且差異未查明** | 行數 **25 相符**；分類逐項相符；行號差異**已查明**（萃取來源不同） | **否** |

---

## 十二、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，七項。**

1. **`-007` 之四項限定不含「無來電」，而 `PITA9` 之 phone call popup
   於免責畫面相位是否顯示，規格未表態。**
   已寫入 `reasoning` 與 `spec_assertion_scan.py` 之 L450 依據欄，
   **但那是具名，不是解決** —— **若上游答「會顯示」，`-007` 之 ER 即不成立。**

2. **§5 之 18 條 ER 對照，其「素材無對應列」13 條之依據是同一組零命中探針。**
   那組探針（`disclaimer`／`splash`／`animation`／`comfort`／`Accept`／
   `loading`／`timeout`）**是我列的**。**若矩陣以別的詞說同一件事**
   （如 `VP` 說螢幕、`Recall Last state` 說 last mode），**該 13 條就不是「無對應列」。**
   **`VP` 正是這個問題之現行實例，而它還沒答覆。**

3. **§6 之兩處「印證」建立在 `CFTS009` 之外部引用上。**
   `r11`／`r12` 與 `VRLP1` 皆註 `See CFTS009`，**而該文件我們沒有**。
   **二者可能各自指向 CFTS009 之不同段落而我們無從分辨。**

4. **A-PMH21 之列位我以座標判定，而座標之列帶邊界是我推的。**
   列標籤在 y=114／197／296／396，我據以推得帶界約為 70–160／160–250 等。
   **PDF 未畫出格線於文字層，該推定未經驗證。**
   結論（兩處在 `KEY ON` 兩列）我有把握，**但其論證不是量測。**

5. **第三層抽樣未做（§7.3 已具名）。**

6. **`-007` 之 ER 另斷言「音訊照常播放」，該面完全未反向掃。**
   R-PMH90 只令掃 pop-up 一類；**`-007` 之 ER4 有兩個斷言，我只驗了一個。**

7. **本包新增之三支程式（`spec_assertion_scan`／`batch_er_vs_matrix`／
   `wording_sample --layer2`）皆無 must-hit。**
   依 R-PMH35(c)，其結果**只得標「未實測」** —— **而我在 §10 之總表裡標了 PASS。
   據實更正於此**（`matrix_vs_chapter.py` 已於 22 包補上錨點，其 PASS 有效；
   本包新增之三支尚無）。

---

## 十三、建議之 commit 與 pathspec（**不執行**）

**訊息**：

```
feat(power_moding): package 23 — spec-internal conflict (A-PMH21), batch 1 ER-level comparison, chapter 11 vs matrix
```

**pathspec（12 路徑，R-G12 —— 逐一具名）**：

```
git commit -- \
  features/power_moding/ANOMALIES.md \
  features/power_moding/DATA_REQUESTS.md \
  features/power_moding/RULINGS.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/23_spec_internal_conflict.md \
  features/power_moding/docs/upstream/23_spec_internal_conflict.md \
  features/power_moding/generated/batch01.json \
  features/power_moding/scripts/batch_er_vs_matrix.py \
  features/power_moding/scripts/gen_batch01.py \
  features/power_moding/scripts/matrix_vs_chapter.py \
  features/power_moding/scripts/spec_assertion_scan.py \
  features/power_moding/scripts/wording_sample.py
```

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py`／`docs/runtime/`／`PROFILE_INTEGRATION.md`／profile | **未動** |
| 工作簿寫回 | **無** |
| `generated/batch01.json` | **只改 `-007` 之 `reasoning`**；其 procedure／ER／限定**未動**；其餘七條未動 |
| State Matrix xlsx／規格 PDF | **只讀** |
| **對外發文** | **無** —— 三筆 DR 皆 `DRAFT` |
| 已執行之 git 狀態變更指令 | **無** |
| 併行 session（`vehicle_setting`）之檔案 | **未動** |

---

## 十四、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **三筆 DR 之發出 ＋ 日期與對象** —— **`DR-PMH5` 之內容因 A-PMH21 而變更**，若尚未寄出請用增補後之版本 | `DR-PMH5` 阻斷 ch 9 |
| 2 | **`DR-PMH5`／`DR-PMH6` 是否已發出** —— 決定 A-PMH21／A-PMH19 之增補是否須改為另開 `DR-PMH9`／`DR-PMH8` | 否 |
| 3 | **§12 第 1 項** —— `PITA9` 之 phone call popup 於免責畫面相位是否顯示（`-007` 之殘餘風險） | batch 1 之寫回 |
| 4 | §12 第 7 項 —— 本包三支新程式無 must-hit，其結果應標「未實測」 | 否 |
| 5 | 章 9／10／12 × 矩陣之**全**對照（現只章 7、8、11 為全對照） | 該三組開批前 |
| 6 | 9.1 之 `source_clause` 例外是否寫入 profile；17 §5.4 其餘五項；Q10 | 否 |
