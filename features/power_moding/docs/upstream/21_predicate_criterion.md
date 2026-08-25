# 上繳包 21 —— 牴觸之判準、矩陣 × ch 7 之全對照與 DR 之狀態機

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/21_predicate_criterion.md](../handoff/21_predicate_criterion.md)
  ＋ [../handoff/21a_dr_dispatch.md](../handoff/21a_dr_dispatch.md)（同輪併讀）
- 前一包上繳：[20_matrix_scope.md](20_matrix_scope.md)
- **本包零寫回工作簿；未撰寫任何 TC**

**20 包之提交狀態**：已於 2026-08-25 經 Pei 授權並提交（`7468feb`，9 路徑）。

---

## ⚠ 本包之三項須先看

1. **ch 7 × 矩陣：30 事件列全部對照，牴觸 0、印證 0、未對照 30。**
   停止條件 7 未觸發。**batch 1 不受規範性素材之牴觸影響。**（§3）
2. **停止條件 9 一度觸發並已修** —— `RESIDUE_VERDICT` 20 條中有 **5 條**
   未引任何 anomaly 或裁決條號。已補引並重跑至 0。（§5）
3. **`DR-PMH1`～`4` 之狀態欄自始至終為 `OPEN`，而四者從未被發出** ——
   R-PMH82 之四級狀態機已落地，該事實已於表中以「**（從未發出）**」記明。（§7）

---

## 一、五條之抄錄核對表（步驟 1）

| 條號 | 來源 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|---|
| R-PMH79 | 21 | 牴觸之判準（同一謂詞相反值）與三種記法 | 479 | `2434c2ce08f08f0d` | `2434c2ce08f08f0d` | ✅ |
| R-PMH80 | 21 | `10.3` 之處置：限縮 ＋ 揭露，不裁權威 | 695 | `f680f9dd1d940a54` | `f680f9dd1d940a54` | ✅ |
| R-PMH81 | 21 | R-PMH26 之範圍不外推至素材格內容 | 382 | `7c6a15c014300329` | `7c6a15c014300329` | ✅ |
| R-PMH82 | 21a | DR 之四級狀態機 | 549 | `8c412360a1a1e9c0` | `8c412360a1a1e9c0` | ✅ |
| R-PMH83 | 21a | `DR-PMH5`／`6` 之發出授權；執行層不得代為發出 | 370 | `264be045c8906824` | `264be045c8906824` | ✅ |

**命中數**：handoff 5 塊、RULINGS 回讀 5 塊，`a == b` 皆 `True`。
**既有條文未動**：`R-PMH10`／`R-PMH76`／`R-PMH78` SHA256 皆相符。

---

## 二、20 §4 之七項依 R-PMH79 重記（步驟 2）

以**勘誤**形式附於 `docs/upstream/20_matrix_scope.md` 末（**§4.1 原表一字未改**，R-PMH44）。

| outline | 原記 | **重記** | 謂詞 |
|---|---|---|---|
| **10.1** `PITA4` | 一致 | **印證** | `Screen Off／Power 鍵之輸入是否被忽略` —— 規格 `shall be ignored…`／矩陣 `r40`・`r44` 之 `Gear = Reverse` 欄皆 `Event ignored`，**同一謂詞取相同值** |
| **10.2** `PITA5` | 一致 | **印證**（第三句）＋ **未對照**（第一、二句） | 印證：`RVC 解除後 Power Button Off 是否回復` —— `shall be reinstated`／`r43c10` = `Return to Power OFF state` |
| **10.3** `PITA6` | ⚠ 字面牴觸 | **牴觸**（不變） | `HVAC pop-up 是否顯示` —— **同一謂詞取相反值** |
| **10.4** `PITA6.1` | 無矛盾 | **未對照** | **無對應列** |
| **10.5** `PITA8` | 一致（軸層面） | **未對照** | **無對應列** —— 有同名之軸（`HU on`），**惟無任何格斷言「功能與 key on 相同」**。**「有同名之軸」不等於「有對應之敘述」** |
| **10.6** `PITA9` | 措詞差異，非牴觸 | **未對照（不同謂詞）** | 規格講畫面（popup 顯示）／矩陣講電源（`HU Powers on`）。**矩陣既未支持亦未否定該敘述** |
| **10.7** `PITA10` | 無矛盾 | **未對照** | **無對應列** |

**重記後之計數**：印證 **2**／牴觸 **1**／未對照 **5**。

**另附勘誤 2**：§3.4 之 `rmutes` 處置，其依據由 R-PMH26 改為 **R-PMH81**
（結論不變，依據更換）。

---

## 三、矩陣 × ch 7 之全對照（步驟 3，**最高優先**）

新增 `scripts/matrix_vs_chapter.py`。母體與判定方式：

| 項 | 數 |
|---|---:|
| `State Matrix` 非空列 | **43** |
| 其中**事件列**（有列標籤且至少一格有值） | **30** |
| 非空格總數 | **362** |
| 其中 `-`／`'-` 佔位 | **93** |
| **事件列之有值格（＝可對照之母體）** | **174** |
| 其餘（區塊名、欄軸、列軸、標題） | **95** |

**每一事件列皆須於 `VERDICT` 具名其記法、謂詞與依據**，未具名 → FAIL。

### 3.1 範圍向 —— ch 7 之關鍵名詞於矩陣之命中

```
--- 範圍向：章 7 之關鍵名詞於矩陣之命中 ---
    0  animation
    0  splash
    0  disclaimer
    0  comfort
    0  Maserati
    0  lower comfort
    0  traffic announcement
    0  CAN BUS
    0  ignition
    0  driver door
    0  black
    0  timeout
    0  3 sec
    0  1.5
    0  10s
    0  last mode
    0  Radio OFF

  命中之名詞 = **0/17** —— **全部 0 命中**
  ⚠ 字面比對；`0 命中` 為 `未對照` 之**支持證據**，非其證明（見 LIMITS）。
```

**十七個名詞全部 0 命中。** ch 7 之整個主題（開機動畫、splash、disclaimer、
comfort controls、Maserati 變體、ignition 轉移、螢幕黑、逾時、CAN BUS）
**不在矩陣之詞彙裡**。

**⚠ 一處必須說明**：不敏感之比對會使 `Radio OFF` 誤命中 `Radio Off Delay`
**15 次** —— 二者為不同之詞（前者為「最後狀態為關機」，後者為延時參數）。
**探針已改為大小寫敏感**，該誤報消除。

### 3.2 逐列結果

```
=== 結果 ===
  牴觸 **0**／印證 **0**／未對照 **30**；未具名 **0**
```

**牴觸 0／印證 0／未對照 30；未具名 0。停止條件 7 未觸發。**

### 3.3 最接近牴觸之三列（已具名為須人讀）

| 列 | 為何接近 | 為何仍判未對照 |
|---|---|---|
| **`r30`**（Key-off／`Door closed`，`HU off` 欄亦 `Event ignored`） | `SU1.)`（7.1）之情境即「駕駛門關閉 → 播放開機動畫」 | 本列之謂詞為**事件是否被處理**，未提動畫；且矩陣之 `Door` 軸**未區分駕駛門**（`driver door` 0 命中） |
| **`r48`**（HVAC 硬控 → `Show Pop-Up`） | `SU3.)`（7.4）為**全稱否定**：`No pop-ups will appear until the disclaimer screen has been removed` | 本列為**無條件之肯定**，其軸不含 disclaimer 狀態，**二者之條件互不涵蓋** |
| **`r33`**（Key-on → `Recall Last state of VP`） | **共同名詞 `Last state`** —— `SU6.)`（7.7）載 `If last state is Radio OFF, play startup animation…` | 矩陣之謂詞為**回復何狀態**，規格之謂詞為**是否播放動畫／顯示 splash**；矩陣未言回復過程中是否播放動畫 |

**同一形態之 pop-up 面亦見於 `r6`／`r15`／`r24`／`r25`** ——
皆為「全稱否定 vs 無條件肯定，而條件互不涵蓋」。
**若該等情境可發生於 disclaimer 顯示期間，即成牴觸；矩陣之軸無法回答此問。**
**已逐列具名為高風險項，交人讀。**

---

## 四、`DR-PMH6` 之開立（步驟 4）

已登記於 `DATA_REQUESTS.md`，狀態 **`DRAFT`**（R-PMH83 已授權發出，
待 Pei 告知實際日期與對象）。**不阻斷** —— R-PMH80 已以限縮＋揭露解除。

其問題摘要含 `PITA6` 逐字、矩陣 `r48c10` 逐字，
以及「**`PITA4` 之對象為按鍵輸入（`selections`）而非 popup 之顯示**」之查證
—— 即分析層 §3.1 所駁回之調和。

**21a §3 之兩份可寄出全文已逐字轉錄於 `DATA_REQUESTS.md` §五、§六**，
以便 Pei 直接取用。**執行層未代為發出。**

---

## 五、`RESIDUE_VERDICT` 之可覆核清單（步驟 5）

新增 `chapter_bidirectional.py --export-residue`：逐條輸出
（章、句之逐字、覆蓋率、結論、**其所引之 anomaly 或裁決條號**）。

### 5.1 ⚠ **停止條件 9 一度觸發**

首跑：**20 條中 5 條缺引用** ——

| 章 | 句首 | 原結論之措詞 |
|---|---|---|
| 9 | `FOTA update available - If user accepts…` | 「非漏 —— 條列再流」 |
| 9 | `Charge Now - XEV key off-Pop-ups…` | 「屬 `-layout` 之切分」 |
| 9 | `Shut the radio down if user dismisses…` | 「屬切分」 |
| 11 | `VR HARD KEY FOR SIRI…` | 「切分於 `(eg.` 處斷開」 |
| 11 | `Radio status after interaction with SIRI…` | 「切分假象」 |

**五者皆為「切分／條列再流」型之結論，而該現象本身有登記**
（`A-PMH03` 之條列再流），**我當時只寫了現象，沒寫它登記在哪** ——
**一個沒有出處的結論，讀者無從查它是不是我當場想的。**

已補引：三者引 `A-PMH03`（條列再流之形態）、章 11 之一者另引 `A-PMH17`
（作為對照：章 11 之全大寫標籤**於 SYS1 有**，章 10 之兩個則全缺），
五者皆補引 `R-PMH66`(c)（本結論依該條由人讀作成）。

### 5.2 重跑結果

```
=== 合計 **20** 條；缺引用者 **0**；**未被任何殘餘句用到之鍵 0**（18 包 `-layout` 之遺留） ===
```

**20 條、缺引用 0、遺留鍵 0。停止條件 9 已解除。**

---

## 六、三條停止條件之自檢（步驟 6，R-PMH77 之自套）

| # | 字面 | 其所欲攔者 | 是否一致 |
|---|---|---|---|
| **7** | 「發現矩陣與 ch 7 之任一 leaf 有 **R-PMH79 意義下之牴觸**（**「新的」牴觸，即未經登記者**）」 | 同左 | **一致** —— 下放包已依 R-PMH77(a) 寫「新的」，且指明判準（R-PMH79）與基準（「未經登記者」）。**本輪之三條中，只有這一條寫對了** |
| **8** | 「步驟 2 之重記後，仍有**任一項**記為『無矛盾』或『非牴觸』」 | 同左 | **一致** —— 其所攔者為**措詞**，而措詞之有無可逐字判定，「任一」在此無歧義。**惟其只攔這兩個詞** —— 若我改寫成「未發現問題」「相容」，本條攔不下。**列舉式判準之形態（R-PMH67 之同型），本條未附抽樣** |
| **9** | 「步驟 5 之清單有**任一條**缺其所引之 anomaly 或裁決條號」 | 同左 | **一致**，且**已實地觸發並修正**（§5.1）。**惟其只驗「有引用」，不驗「該引用是否切題」** —— 我大可引一條不相干的條號而通過 |

**自檢之結論**：本包三條之字面與目的皆一致，**未再現 R-PMH77 之形態**。
**惟 8 與 9 各有一處已具名之弱點**（列舉式、只驗存在不驗切題），
二者皆為「檢查通過不等於該事已做對」之同一家族。

---

## 七、DR 之狀態機落地（21a 步驟 8、9）

`DATA_REQUESTS.md` 全表改用 R-PMH82 之四級，並增
`發出日期`／`發出對象`／`管道`／`結案依據` 四欄。

| DR | 狀態 | 發出日期 | 結案依據 | 阻斷 |
|---|---|---|---|---|
| DR-PMH1 | **`CLOSED`** | **（從未發出）** | R-PMH72 | 解除 |
| DR-PMH2 | **`CLOSED`** | **（從未發出）** | R-PMH73 | ⚠ 其素材與 p9 不對應（A-PMH18）→ 另開 `DR-PMH5` |
| DR-PMH3 | **`CLOSED`** | **（從未發出）** | R-PMH74 | 解除 |
| DR-PMH4 | **`CLOSED`** | **（從未發出）** | R-PMH75 | 解除 |
| **DR-PMH5** | **`DRAFT`** | **（待填）** | — | **ch 9 開批** |
| **DR-PMH6** | **`DRAFT`** | **（待填）** | — | 否 |

**合計未結 2 筆，二者皆 `DRAFT`。**

**R-PMH82 之回溯記明已寫入**：四者自 2026-08-24 開立起，
經執行層於**六個往返連續重申**而狀態欄始終為 `OPEN` ——
**該欄無法分辨「登記了」與「發出了」**，
致「尚未發出」這件事沒有任何欄位承載它。

**發出日期欄留白** —— 待 Pei 告知實際日期與對象後方填，
**未以本包之日期充當**（R-PMH83）。

---

## 八、矩陣未對照部分之具名（步驟 7）

已寫入 `ANOMALIES.md` 之 A-PMH18 補記（含 §3 之六列數字表）。

| 章 | 範圍 | 結果 |
|---|---|---|
| **7** | **30 事件列全部** | 牴觸 0／印證 0／未對照 30 |
| 10 | 7 列（部分欄） | **牴觸 1**（`10.3`）／印證 2／未對照 5 |
| 12 | `r16`（12 欄逐欄） | 互補，不衝突 |
| **8** | **完全未對照** | —— |
| **9** | **完全未對照** | A-PMH18 之主體：p9 之能力矩陣本不在此 Excel 內 |
| **11** | **完全未對照** | —— |

**已於 `DECISIONS.md` 登記為 KNOWN-INCOMPLETE**：
矩陣之 `VR button long press without/at Projection`（`r11`／`r12`／`r28`／`r29`）
**與 ch 11 之 `VRLP1` 顯有共同主題，而該對照本包未做**。

---

## 九、lint 全跑輸出

**本輪未動 `generated/batch01.json`，未撰寫任何 TC。**

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

## 十、檢查總表

| 檢查 | 結果 |
|---|---|
| `lint_batch.py generated/batch01.json` | **30/30 PASS** |
| **`matrix_vs_chapter.py 7`** | **PASS** —— 30 列全具名、牴觸 0 |
| `chapter_bidirectional.py 7～12` | **六章全 PASS** |
| `chapter_bidirectional.py --partition`／`--source-must-hit` | **PASS** |
| **`chapter_bidirectional.py --export-residue`** | **PASS**（首跑 FAIL 5 條，補引後 0） |
| `check_granularity.py --self-test`／`--check-doc-sync`／`--doc-sync-must-hit` | **PASS** |
| `challenge_rulings.py`／`tsv_vs_pdf.py --truncation` | **PASS** |
| `marker_coverage.py --self-test`／`canon_coverage.py`／`check_state_consistency.py`／`check_write_back.py --self-test` | **PASS** |
| `bidirectional_spec_diff.py` | **拒跑（2）** —— 已停用 |
| `shasum -c`（inputs） | **6/6 OK** |

---

## 十一、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | **是** —— p9 之能力矩陣仍無來源（`DR-PMH5`，`DRAFT`） |
| 2 | 判準衝突未決 | **是** —— `10.3` 之牴觸（R-PMH80 已給處置，惟權威未裁） |
| 3 | 須寫回而工作簿狀態不明 | 否（零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論建於臆測 | **是** —— 同 1 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| 7 | ch 7 × 矩陣有**新的**牴觸 | 牴觸 **0**（30 列全具名） | **否** |
| 8 | 重記後仍有「無矛盾」或「非牴觸」 | 七項全部改為三種記法之一；勘誤中無該二詞 | **否** |
| 9 | 清單有任一條缺引用 | **首跑 5 條缺 → 已補 → 0** | **一度觸發，已解除** |

---

## 十二、未結 DR 清單

| DR | 主旨 | 狀態 | 阻斷 |
|---|---|---|---|
| **DR-PMH5** | PDF p9 之能力矩陣之來源文件 | **`DRAFT`**（已授權發出） | **ch 9 開批** |
| **DR-PMH6** | RVC 情境下 HVAC popup 之規格依據 | **`DRAFT`**（已授權發出） | 否 |

**合計未結 2 筆。**

---

## 十三、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，六項。**

1. **§3 之「未對照 30」建立在一個我沒有驗證的前提上** ——
   我把「矩陣之謂詞是電源／VP／mute／screen off」與「ch 7 之謂詞是動畫／
   splash／disclaimer」當成不相交。**`VP`（Vehicle Projector？顯示器？）
   這個詞在矩陣裡出現數十次而我從未查明它指什麼。**
   若 `VP Turns OFF` 之 `VP` 就是 ch 7 所說的螢幕，
   則 `r15c4`（Key-off → `VP Turns OFF`）與 `SU1.)`「螢幕維持黑」**同謂詞**。
   **我判了 30 列，而其中一個關鍵詞我沒查。**

2. **pop-up 那一組（`r6`／`r15`／`r24`／`r25`／`r48`）之「條件互不涵蓋」是推論。**
   我說「矩陣之軸不含 disclaimer 狀態，故二者不在同一命題上」——
   **但全稱否定（`No pop-ups will appear until…`）之涵蓋範圍是所有時刻**，
   矩陣之無條件肯定落在其中一個時刻即為牴觸。
   **我把「矩陣沒說是否在 disclaimer 期間」當成「矩陣不涉及 disclaimer 期間」，
   那是兩件事。** 已具名為高風險項，**但我判的是「未對照」而非「牴觸」，
   這個選擇本身該由分析層覆核。**

3. **章 8 與章 11 完全未對照，而 `Startup Sounds`（ch 8，6 leaf）
   是 batch 2 之候選。** 已登記，但登記不是對照。

4. **停止條件 8 之自檢我判「一致」，惟其為列舉式（只攔兩個詞）。**
   R-PMH67 要求列舉式判準附偽陰之抽樣估計，**我沒有對它做抽樣**。

5. **`--export-residue` 只驗「有引用」不驗「切題」（§6 已具名）。**
   我補的 5 條引用是我自己判斷切題的，**沒有第二個來源** ——
   而 `RESIDUE_VERDICT` 之第二來源本身就是已登記之未完成項。**同一個洞被引用了兩次。**

6. **本包新增之 `matrix_vs_chapter.py` 沒有 must-hit。**
   R-PMH35(c) 明訂任何正式判準須有刻意構造之反例實跑並證明其 FAIL。
   **本檔只有「未具名 → FAIL」這一條保護，沒有「把一個真牴觸放進去，
   檢查須報牴觸」之錨點。** 依 R-PMH35(c)，其結果**只得標「未實測」**，
   不得標 PASS —— **而我在 §10 之總表裡標了 PASS。據實更正於此。**

---

## 十四、建議之 commit 與 pathspec（**不執行**）

**訊息**：

```
feat(power_moding): package 21 — predicate criterion, matrix x ch7 full comparison, DR state machine
```

**pathspec（10 路徑，R-G12 —— 逐一具名）**：

```
git commit -- \
  features/power_moding/ANOMALIES.md \
  features/power_moding/DATA_REQUESTS.md \
  features/power_moding/DECISIONS.md \
  features/power_moding/RULINGS.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/21_predicate_criterion.md \
  features/power_moding/docs/handoff/21a_dr_dispatch.md \
  features/power_moding/docs/upstream/20_matrix_scope.md \
  features/power_moding/docs/upstream/21_predicate_criterion.md \
  features/power_moding/scripts/chapter_bidirectional.py \
  features/power_moding/scripts/matrix_vs_chapter.py
```

（實為 **11 路徑**。`docs/upstream/20_*.md` 之異動為本包所附之**勘誤節**，
其 §3、§4 原文一字未改。）

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py`／`docs/runtime/`／`PROFILE_INTEGRATION.md`／profile | **未動** |
| 工作簿寫回 | **無** |
| `generated/batch01.json`／任何 TC | **未動、未撰寫** |
| State Matrix xlsx | **只讀**（`data_only=True`，未 `save`） |
| **對外發文** | **無** —— `DR-PMH5`／`6` 之全文已備妥且標 `DRAFT`，**執行層未代為發出**（R-PMH83） |
| 已執行之 git 狀態變更指令 | **無** |
| 併行 session（`vehicle_setting`）之檔案 | **未動** |

---

## 十五、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **`DR-PMH5`／`DR-PMH6` 之實際發出**，並告知**日期與對象**以便改標 `SENT` | `DR-PMH5` 阻斷 ch 9 開批 |
| 2 | **§13 第 2 項** —— pop-up 那一組我判「未對照」而非「牴觸」，**該選擇請覆核** | `Disclaimer Screen`／`Power Off Behavior` 組 |
| 3 | §13 第 1 項 —— 矩陣之 `VP` 指什麼（我未查明而已據以判 30 列） | 同上 |
| 4 | §13 第 6 項 —— `matrix_vs_chapter.py` 無 must-hit，其結果應標「未實測」 | 否 |
| 5 | 章 8／章 11 × 矩陣之對照 | 該二組開批前 |
| 6 | 9.1 之 `source_clause` 例外是否寫入 profile | `Power Transitions` 開批前 |
| 7 | 17 §5.4 其餘五項；Q10、`PROFILE_INTEGRATION.md` | 否 |

---

## 勘誤（22 包補記 —— **§3 原文一字未改**，R-PMH44）

### 勘誤 1 —— §3.2 之「牴觸 0／印證 0／未對照 30」**已被推翻**

§3.2 所報之計數建立於「pop-up 諸格與 `SU3.)` **未對照**」之判定，
而該判定之理由為「矩陣之軸不含 disclaimer 狀態」。

**該理由已由 R-PMH84 推翻** —— **「素材未提及某條件」不等於
「素材不涉及該條件」**；前者是素材之沉默，後者是一個關於素材涵蓋範圍之主張。
`SU3.)` 為**全稱否定**（涵蓋免責畫面移除前之所有時刻），
矩陣之 pop-up 格為**無條件肯定**，**其條件未經證明互斥**。

**該自我質疑由執行層於 21 包 §13 第 2 項提出**，分析層於 22 包 §三採之。

**重記後之計數（22 包步驟 2）**：

| 記法 | 21 包 §3.2 | **22 包** |
|---|---:|---:|
| 牴觸 | 0 | **1**（`r48`） |
| 印證 | 0 | 0 |
| 未對照 | 30 | **25** |
| **待定義**（R-PMH85(c) 新增） | — | **4**（`r6`／`r15`／`r24`／`r25`） |

**`r6`／`r15`／`r24`／`r25` 記為「待定義」而非「牴觸」，其理由須明說**：
四者之 pop-up 由 **`VP`** 承載（`VP display pop-up`／`VP Stays ON Pop-up: …`），
而 `VP` 於規格全 11 頁 **0 命中**（A-PMH20、`DR-PMH7`）——
若 `VP` 非 head unit 之顯示螢幕，則與 `SU3.)` 無共同謂詞。
依 **R-PMH85(c)**「本條優先」，其判定所需之語意尚未存在。

**`r48` 不倚賴 `VP`**（其格逐字為 `Show Pop-Up`），故其牴觸**獨立成立**。

**⚠ 此與 22 包步驟 2 之字面（五格皆改「牴觸」）不同** —— 差異、理由
與其依據見上繳 `22_popup_conflict.md` §2.2。

### 勘誤 2 —— §3 之判定曾以**不含章號之鍵**存放

`matrix_vs_chapter.py` 首版之 `VERDICT` 鍵為 `(區塊起列, 列)`，**不含章號** ——
以 `matrix_vs_chapter.py 10` 執行時會**靜默沿用章 7 之判定**，
而每列都「有結論」故檢查不會察覺。**22 包已改為 `(章, 區塊起列, 列)` 並實測**
（`matrix_vs_chapter.py 10` 現正確報 30 列未具名）。

**形態同於 18→19 包之 `RESIDUE_VERDICT` 60 字元鍵碰撞** ——
**兩次皆為「鍵不足以識別」，兩次皆由做別的事時撞出來。**

**§3 之原文一字未改，其 SHA256 不受本節影響。**
