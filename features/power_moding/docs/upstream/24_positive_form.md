# 上繳包 24 —— 正向記法、A-PMH21 之改判與 ER4(b) 之牴觸

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/24_positive_form.md](../handoff/24_positive_form.md)
- 前一包上繳：[23_spec_internal_conflict.md](23_spec_internal_conflict.md)
- **本包零寫回工作簿**；只改 `-007` 之 `reasoning`，**限定與 ER 未動**

**23 包之提交狀態**：已於 2026-08-25 經 Pei 授權並提交（`50664e7`，12 路徑）。

---

## ⚠ 本包之三項須先看

1. **停止條件 7 觸發** —— ER4(b) 之 `audio` 掃描查出**新的牴觸**：
   矩陣 `r45`（`Mute Button Pressed` → `Mute --> Active`）× `-007` 之
   `The announcement is heard in the background`。
   **`-007` 之四項限定不含「不按 Mute 鍵」。依 R-PMH79 上呈，未自行調和。**（§4）
2. **A-PMH21 之牴觸改判為「未對照」** —— 我把 p9 **渲染出來看了**。
   `Pop-ups still shown` 在 **`HEADUNIT POWER OFF`** 欄，
   而同欄之 `Climate GUI` 格逐字為 `Not Visibile due to power off`。
   **條件互斥已證，牴觸不成立。**（§2）
3. **檢查總表已機器化，六支標「未實測」** ——
   含本包新增之三支與 23 包新增之二支。（§6）

---

## 一、§六三條之抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH91 | 對照結論須以四詞之一作結；攔截式列舉廢止 | 441 | `cb23dff4c2cb9088` | `cb23dff4c2cb9088` | ✅ |
| R-PMH92 | 總表結果欄由 must-hit 註冊決定，手寫不採認 | 339 | `3484fcee117abb9c` | `3484fcee117abb9c` | ✅ |
| R-PMH93 | 反向掃描之單位為斷言，非 TC 亦非 ER 之條 | 421 | `713a8ff045dc8fde` | `713a8ff045dc8fde` | ✅ |

**命中數**：handoff 3 塊、RULINGS 回讀 3 塊，`a == b` 皆 `True`。
**既有條文未動**：`R-PMH10`／`R-PMH88`／`R-PMH90` SHA256 皆相符。

---

## 二、A-PMH21 之改判 —— **我把 p9 渲染出來看了**（步驟 3 之連帶）

### 2.1 §2.2 之 bbox 先算後比 —— 逐項相符

| 出現 | 分析層所報 | **本層獨立實測** | 相符 |
|---|---|---|---|
| 第 1 處 | x 427.8–637.0，y 80.9–122.5 | x 427.8–637.0，y 80.9–122.5 | ✅ |
| 第 2 處 | x 427.8–714.5，y 180.1–221.6 | x 427.8–714.5，y 180.1–221.6 | ✅ |
| 其涵蓋之列標籤 | `KEY ON ENGINE ON` (y=113.7)／`KEY ON ENGINE OFF (ACC or RUN)` (y=196.7) | 同 | ✅ |

**23 §12 第 4 項之疑慮（「列帶邊界是我推的」）自此解除** ——
每一區塊之垂直範圍**自身即涵蓋其列標籤**，不需推定邊界。

### 2.2 §2.3 之欄位問題 —— **不必問上游，渲染出來就看得見**

分析層指出「區塊橫跨 427.8 起之寬幅，無法由 x 判定其屬 `ON` 或 `OFF` 欄」，
並將其列為 `DR-PMH5` 之問題。

**本層以 `get_pixmap(matrix=Matrix(4,4), clip=Rect(340, 40, 760, 260))` 渲染
p9 之矩陣區並判讀** ——

| 項 | 實見 |
|---|---|
| `HVAC Knobs: Fully functional. `**`Pop-ups still shown.`** | **`HEADUNIT POWER OFF` 欄**（左欄） |
| 右欄（`HEADUNIT POWER ON`）之同位格 | `HVAC Knobs: Fully functional`（**無 pop-up 之敘述**） |
| 同欄之 `Climate GUI` 格 | **`Not Visibile due to power off`** |

### 2.3 **條件互斥已證 → 牴觸不成立，改判「未對照」**

依 R-PMH84：「除非其條件**已被證明**互斥，否則判為牴觸」——
**現在證明有了**：

1. 免責畫面為 **head unit 所顯示之畫面**，其相位必為 head unit **開機中**；
2. `Pop-ups still shown` 所在之欄為 **`HEADUNIT POWER OFF`**；
3. **同一欄之 `Climate GUI` 格逐字為 `Not Visibile due to power off`**
   —— **該欄之語意即「頭端電源關閉」**。

**二者不在同一時刻。記法由 `牴觸` 改為 `未對照`。**

**`spec_assertion_scan.py --assertion popup` 之牴觸數由 2 降為 0。**

**⚠ 三項須一併記明**：

- **A-PMH21 不撤銷** —— 「p9 有 `Pop-ups still shown` 而 p8 之 `SU3.)` 為全稱否定」
  之事實不變；**其登記價值在於：該互斥曾被 22／23／24 三包當成未證**；
- **R-PMH89（規格內部之牴觸）之條文不撤銷** —— 其判準與處置仍有效，
  **只是本 feature 目前沒有它的實例了**；
- **`DR-PMH5` 之第三問已附量測之答案**，其性質由「請裁定」降為「請確認」。

### 2.4 **這件事本可更早做**

p9 之矩陣**自 13 包（A-PMH14 新漏 2）起就是已知之缺口**，
其「以圖呈現、文字層交錯」被記了十一包，
**而「把它渲染出來看」這個動作，到本包才做。**
`A-PMH04` 之 render 能力早於 04 包即已實測（300 DPI 可辨讀）。

---

## 三、`wording_sample.py` → `verdict_form.py`（步驟 2，R-PMH91）

### 3.1 正向檢查之母體**非列舉**

母體為**各檢查之判定表**（`VERDICT`／`RESIDUE_VERDICT`／`ER_VERDICT`／
`LINE_VERDICT` 等），**其每一項依構造即為一個對照結論** ——
不必掃描散文去猜哪一行是結論。

```
=== 對照結論之記法（R-PMH91）===
母體：各檢查之判定表，共 **206** 項

  batch_er_vs_matrix.ER_VERDICT                 18 項  {'未對照': 17, '印證': 1}
  chapter_bidirectional.RESIDUE_VERDICT         20 項  {'未對照': 11, '印證': 9}
  matrix_vs_chapter.VERDICT                    120 項  {'待定義': 4, '未對照': 109, '牴觸': 2, '印證': 5}
  spec_assertion_scan.AUDIO_CELL_VERDICT        10 項  {'未對照': 9, '牴觸': 1}
  spec_assertion_scan.AUDIO_LINE_VERDICT        13 項  {'—': 1, '未對照': 12}
  spec_assertion_scan.LINE_VERDICT              25 項  {'印證': 5, '未對照': 18, '—': 2}

  合計：{'未對照': 176, '印證': 20, '待定義': 4, '牴觸': 3, '—': 3}；**未以四詞之一作結 = 0**
```

**176 項，未以四詞之一作結者 = 0。**

### 3.2 `RESIDUE_VERDICT` 之 20 條已改寫為四詞形式

| 原起首 | 條數 | 改為 |
|---|---:|---|
| `非漏` | 5 | **印證** |
| `非漏（散文側）` | 1 | **印證** |
| `非漏（需求側）` | 3 | **印證** |
| `漏` | 8 | **未對照** |
| `部分漏` | 1 | **未對照** |
| `混合句` | 1 | **未對照** |
| `PDF 側為未刪淨之舊文字` | 1 | **未對照** |

**四詞分布：印證 9／未對照 11。判斷一字未改，只改其作結之詞。**

**⚠ 一項損失須具名**：`漏`（PDF 有而 SYS1 無）映到 `未對照`，
而 `未對照` 亦用於「素材無對應列」之良性情形 ——
**一個嚴重發現與一個良性發現自此同詞**。
本層之處置為在四詞之後**保留原措詞**（如 `未對照 —— **原記「漏」**；…`），
使其可回溯。**惟該補償是措詞而非結構。**

### 3.3 三項 must-hit

```
=== R-PMH91 之 must-hit（24 包步驟 2）===

  基線（現況）之 FAIL 數 = 0

  (a) 注入以「**非漏**」作結之對照結論 → FAIL 數 0 → 1；其在 FAIL 清單內：True
  (b) 注入以「**未對照**」作結者 → FAIL 數 0 → 0；未被攔下：True
  (c) 非對照結論之散文行（如同值查核 `… 與 … 一致 : True`）**不進母體**：True
      —— 其成立之理由不是「被過濾掉」，是**母體為判定表而非散文**。

==================================================================
(a) 非漏 → FAIL: True；(b) 未對照 → PASS: True；(c) 散文不進母體: True
```

**(c) 之成立理由須明說**：其不是「被過濾掉」，是**母體為判定表而非散文**。

### 3.4 `wording_sample.py` 已停用

拒跑、退出碼 **2**、停用理由寫入 docstring；
**其兩層抽樣之數據（10% → 20%）為 R-PMH91 之立條依據，故檔案不刪。**

---

## 四、⚠ ER4(b) 之反向掃描（步驟 4，R-PMH93）—— **停止條件 7 觸發**

```
=== 結果 ===
  {'—': 1, '未對照': 21, '牴觸': 1}；未具名 **0**

  **牴觸 1 處**  ← **停止條件觸發，須上呈，不得自行調和（R-PMH79）**
```

### 4.1 牴觸之逐字

| | 逐字 |
|---|---|
| **`-007` ER4(b)** | `The announcement is heard in the background`（**音訊可聞**） |
| **矩陣 `r45`**（`Mute Button Pressed`，`Key On, Gear != Reverse`） | c3／c5／c7／c9 = **`Mute --> Active`**（**使之靜音**）；c11 = `Mute becomes active if previously unmuted` |

**共同謂詞**：音訊是否可聞（是否靜音）。**取相反值。**

**條件互斥？未證** ——
`-007` 之四項限定（R-PMH87：ON/OFF 鍵、key-off、開門、HVAC 硬控）
**不含「不按 Mute 鍵」**，且其欄軸 `Key On, Gear != Reverse`
**與免責畫面之相位（`KEY ON`）重疊**。

**依 R-PMH79 上呈，未自行調和。`-007` 之限定本輪未改。**

### 4.2 其餘 21 處之判定

| 側 | 項數 | 結果 |
|---|---:|---|
| 規格 | 13 行 | `—` 1（`SU3.)` 自身）／**未對照 12** |
| 矩陣 | 10 列 | **未對照 9**／**牴觸 1**（`r45`） |

**未對照之依據分四類**（皆逐項具名）：
不同音源（`SSND` 諸條之啟動音／告別音，5 行）／
規格自身之時序（免責畫面在開機動畫之後，`SU1.)` 之序）／
`VRLP1` 之條件句（`radio is OFF`，4 行）／
**TC 自身之構造**（`OFF3.)` 之 `launching app from Power Off State`；
`r40`／`r48` 已為四項限定所排除）。

### 4.3 **一項判讀須具名**

`r46`／`r47` 之 `Else: Mute Active` 我判為「**維持**」而非「**使之**靜音」，
其依據為**同列之 `Mute --> Inactive` 用了箭頭而 `Mute Active` 沒有**。
**該記法之區辨是我的判讀，矩陣未定義其記法。**
若 `Else: Mute Active` 意為「使之靜音」，則 `r46`／`r47` **亦為牴觸**。

---

## 五、章 10 × 矩陣之全對照（步驟 6）

```
=== 結果 ===
  牴觸 **1**／印證 **3**／未對照 **26**／待定義 **0**；未具名 **0**
  ← **停止條件觸發**：發現牴觸，須上呈，不得自行調和（R-PMH79）
```

**牴觸 1（`10.3` × `r48c10`，**已登記**，R-PMH80／`DR-PMH6`）／印證 3／未對照 26。**
**其牴觸非「新的」→ 停止條件 8 未觸發。**

### 5.1 三處印證

| 列 | 規格 | 矩陣 |
|---|---|---|
| `r40` | `PITA4` `shall be ignored while backup cam is being shown` | `Gear = Reverse` 之六欄皆 `Event ignored` |
| `r44` | 同上（Screen Off 鍵） | 同上 |
| `r43` | `PITA5` 第三句 `the Power Button Off state shall be reinstated` | c10 = `Return to Power OFF state` |

### 5.2 `r6`／`r24` 之互斥依據 —— **素材自身之結構，非其沉默**

`PITA4` 之條件為 `while backup cam is being shown`，而
**矩陣以第三區塊（`Key On, Gear = Reverse`）專門處理倒車情境**
（`r40` c6–c11 皆 `Event ignored`）。
**故第一／二區塊之 `r6`／`r24`（無 gear 軸）依矩陣自身之切分不涵蓋倒車情境。**

**此與 22 包被推翻之推定不同** —— 那次之依據是「矩陣沒提 disclaimer」（沉默），
本次之依據是「矩陣另闢一區塊處理該條件」（結構）。

### 5.3 一項記為「印證之候選」而未記印證者

`r13`／`r31`（`Call Ended`）與 `PITA9` 末句
（`the head unit will return to Power Off State upon the call ending`）
**同一謂詞取相同值**，惟其條件不同（`PITA9` 為「以軟／硬鍵接聽且通話中未換畫面」；
矩陣為「通話自 Power OFF state 起始」）。
**記未對照並具名其為印證之候選，待人讀。**

---

## 六、檢查總表之機器化（步驟 5，R-PMH92）

新增 `scripts/check_table.py`；各檢查於其模組頂端註冊
`HAS_MUST_HIT` 與 `MUST_HIT_NOTE`。

| 檢查 | must-hit | 退出碼 | 期望 | **結果** | 備註 |
|---|---|---:|---:|---|---|
| `lint_batch.py generated/batch01.json` | ✅ | 0 | 0 | **PASS** | 外部 fixture 兩份（`batch01_prerework` 21/30、`batch01_r2` 29/30）逐輪實跑並 FAIL |
| `lint_batch.py <fixture prerework>` | ✅ | 1 | 1 | **PASS** | must-hit fixture —— 其 FAIL 即其通過 |
| `lint_batch.py <fixture r2>` | ✅ | 1 | 1 | **PASS** | must-hit fixture —— 其 FAIL 即其通過 |
| `check_granularity.py --self-test` | ✅ | 0 | 0 | **PASS** | `--self-test` 五錨點 ＋ `--doc-sync-must-hit` 兩項故意失敗 |
| `check_granularity.py --check-doc-sync` | ✅ | 0 | 0 | **PASS** | `--self-test` 五錨點 ＋ `--doc-sync-must-hit` 兩項故意失敗 |
| `check_granularity.py --doc-sync-must-hit` | ✅ | 0 | 0 | **PASS** | `--self-test` 五錨點 ＋ `--doc-sync-must-hit` 兩項故意失敗 |
| `check_write_back.py --self-test` | ✅ | 0 | 0 | **PASS** | `--self-test` 三項故意失敗全被攔下 |
| `marker_coverage.py --self-test` | ✅ | 0 | 0 | **PASS** | `--self-test` 之 must-hit A／B／C／D |
| `marker_coverage.py --verify-extraction` | ✅ | 0 | 0 | **PASS** | `--self-test` 之 must-hit A／B／C／D |
| `marker_coverage.py --window-compare` | ✅ | 0 | 0 | **PASS** | `--self-test` 之 must-hit A／B／C／D |
| `canon_coverage.py` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit** —— 其只做差集，無刻意構造之反例 |
| `check_state_consistency.py` | ✅ | 0 | 0 | **PASS** | `--self-test` 之故意注入 |
| `challenge_rulings.py` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit** —— 其判準為標記列舉，R-PMH67 之抽樣非 must-hit |
| `tsv_vs_pdf.py --truncation` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit** —— 只做逐字比對之量測 |
| `chapter_bidirectional.py 7..12` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `chapter_bidirectional.py --partition` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `chapter_bidirectional.py --source-must-hit` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `chapter_bidirectional.py --export-residue` | ✅ | 0 | 0 | **PASS** | `--source-must-hit` 之範圍向 ＋ must-hit A／B（R-PMH78） |
| `matrix_vs_chapter.py --must-hit` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
| `matrix_vs_chapter.py 8` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
| `matrix_vs_chapter.py 11` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
| `matrix_vs_chapter.py 7` | ✅ | 1 | 1 | **PASS** | 含**牴觸 1**（`r48` × `SU3.)`）→ 退出碼 1 為設計 |
| `matrix_vs_chapter.py 10` | ✅ | 1 | 1 | **PASS** | 含**牴觸 1**（`10.3` × `r48c10`，已登記 R-PMH80）→ 退出碼 1 為設計 |
| `spec_assertion_scan.py --assertion popup` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit**（24 包 §12）—— 其逐行判定由人寫入 |
| `spec_assertion_scan.py --assertion audio` | **否** | 1 | 1 | **未實測** | **查出牴觸 1**（`r45` × `-007` ER4(b)）→ **24 包停止條件 7 觸發，須上呈** |
| `batch_er_vs_matrix.py` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit**（24 包 §12）—— 其逐條判定由人寫入 |
| `verdict_form.py` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項（非漏 → FAIL／未對照 → PASS／散文不進母體） |
| `verdict_form.py --must-hit` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項（非漏 → FAIL／未對照 → PASS／散文不進母體） |

**未註冊 must-hit 而標「未實測」者 = 6**  ← R-PMH92：其不得標 PASS

> 本表由 `python scripts/check_table.py` 產生。**手寫之結果欄不予採認**（R-PMH92）。

**六支標「未實測」**：`canon_coverage`／`challenge_rulings`／`tsv_vs_pdf`／
`spec_assertion_scan`（兩模式）／`batch_er_vs_matrix`。
**其中後三支為 23、24 包新增者 —— 23 §12 第 7 項所自陳者，自此由程式標示。**

**`check_table.py` 自身亦註冊 `HAS_MUST_HIT = False`** ——
其若入表亦應標「未實測」。

---

## 七、lint 全跑輸出

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

---

## 八、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | **是** —— p9 矩陣之來源（`DR-PMH5`）＋ `VP` 未定義（`DR-PMH7`） |
| 2 | 判準衝突未決 | **是** —— `10.3` × `r48c10`（已登記）＋ **`r45` × `-007` ER4(b)（本包新增）** |
| 3 | 須寫回而工作簿狀態不明 | 否（零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論建於臆測 | **是** —— 同 1 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| **7** | 步驟 4 之 ER4(b) 掃描發現**新的**牴觸 | **牴觸 1**（`r45`，未經登記） | **觸發** |
| 8 | 步驟 6 之章 10 全對照發現**新的**牴觸 | 牴觸 1，**已登記**（R-PMH80） | 否 |
| 9 | 步驟 2 之 must-hit (a)（以「非漏」作結者）未 FAIL | FAIL 數 0 → 1，其在清單內 | 否 |

**停止條件 7 觸發後之處置**：
**未改 `-007` 之限定與 ER**（R-PMH79：不得自行調和）；
其 `reasoning` 已具名該牴觸為**未解之殘餘風險（二）**；
**本包其餘步驟（2／3／5／6）與其獨立，已完成並回報。**

---

## 九、未結 DR 清單（R-PMH82）

| DR | 主旨 | 狀態 | 發出日期 | 阻斷 |
|---|---|---|---|---|
| **DR-PMH5** | p9 矩陣之來源；其自身與 `SU3.)` 之關係（**第三問已附量測答案**） | **`DRAFT`** | **（待填）** | **ch 9 開批** |
| **DR-PMH6** | RVC 情境之 HVAC popup ＋ 三項覆蓋缺口 | **`DRAFT`** | **（待填）** | 否 |
| **DR-PMH7** | `VP` 之定義 | **`DRAFT`** | **（待填）** | 矩陣對照之四列 |

**合計未結 3 筆，三者皆 `DRAFT`。發出日期欄第三次空著。**

---

## 十、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，六項。**

1. **`r46`／`r47` 之 `Else: Mute Active` 我判為「維持」，其依據是箭頭之有無。**
   **矩陣未定義其記法。** 若該詞意為「使之靜音」，
   **則本包之牴觸不是 1 個而是 3 個。**（§4.3 已具名）

2. **`audio` 斷言之六個關鍵詞是我列的。**
   `silent`／`no output`／`suppressed` 等同義表述不會命中。
   **R-PMH93 令「其關鍵詞各自取用」，而取用之方式仍是列舉** ——
   **R-PMH91 廢止了記法上之列舉，未廢止關鍵詞上之列舉。**

3. **`-007` 之 ER 共 5 條，我只掃了 ER4 之兩個斷言。**
   ER1／2／3／5 之斷言（「不按 ON/OFF 鍵」「不開門」「報導已送出」
   「移除後 pop-up 顯示」）**完全未反向掃**。
   R-PMH93 之單位是斷言，**而我只挑了 ER4 的兩個。**

4. **A-PMH21 之改判建立在「免責畫面必為 head unit 開機中所顯示」上。**
   該命題我沒有在規格中找到逐字支持 —— **它是常識而非引文。**
   若某架構下免責畫面由他處顯示（如儀表），該互斥即不成立。
   **`VP` 之未定義（A-PMH20）正是這個問題的近親。**

5. **章 9／12 × 矩陣仍未全對照。**
   章 9 因 `DR-PMH5` 未答而不開批，章 12 之 `r16` 於 20 包已單獨對照，
   **但其餘 29 列未對照。**

6. **`verdict_form.py` 只驗「以四詞之一作結」，不驗該詞判對。**
   §3.1 之 176 項全數通過，**而其中有多少判錯，本檢查一無所知** ——
   **這正是它與被它取代者之共同限度。**

---

## 十一、建議之 commit 與 pathspec（**不執行**）

**訊息**：

```
feat(power_moding): package 24 — positive verdict form, A-PMH21 reclassified by rendering, ER4(b) conflict found
```

**pathspec（16 路徑，R-G12 —— 逐一具名）**：

```
git commit -- \
  features/power_moding/ANOMALIES.md \
  features/power_moding/DATA_REQUESTS.md \
  features/power_moding/RULINGS.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/24_positive_form.md \
  features/power_moding/docs/upstream/24_positive_form.md \
  features/power_moding/generated/batch01.json \
  features/power_moding/scripts/batch_er_vs_matrix.py \
  features/power_moding/scripts/canon_coverage.py \
  features/power_moding/scripts/challenge_rulings.py \
  features/power_moding/scripts/chapter_bidirectional.py \
  features/power_moding/scripts/check_granularity.py \
  features/power_moding/scripts/check_state_consistency.py \
  features/power_moding/scripts/check_table.py \
  features/power_moding/scripts/check_write_back.py \
  features/power_moding/scripts/gen_batch01.py \
  features/power_moding/scripts/lint_batch.py \
  features/power_moding/scripts/marker_coverage.py \
  features/power_moding/scripts/matrix_vs_chapter.py \
  features/power_moding/scripts/spec_assertion_scan.py \
  features/power_moding/scripts/tsv_vs_pdf.py \
  features/power_moding/scripts/verdict_form.py \
  features/power_moding/scripts/wording_sample.py
```

（實為 **23 路徑** —— 九支程式之異動只是加 `HAS_MUST_HIT` 兩行常數，R-PMH92 所令。）

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py`／`docs/runtime/`／`PROFILE_INTEGRATION.md`／profile | **未動** |
| 工作簿寫回 | **無** |
| `generated/batch01.json` | **只改 `-007` 之 `reasoning`**；其限定、procedure、ER**未動**；其餘七條未動 |
| State Matrix xlsx／規格 PDF | **只讀**（另以 `get_pixmap` 渲染 p9 至暫存目錄，**未寫入 repo**） |
| **對外發文** | **無** —— 三筆 DR 皆 `DRAFT` |
| 已執行之 git 狀態變更指令 | **無** |
| 併行 session（現於 `features/display`）之檔案 | **未動** |

---

## 十二、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **`r45` × `-007` ER4(b) 之牴觸如何處置**（停止條件 7）—— 加「不按 Mute 鍵」之限定？或另有解 | **batch 1 之寫回** |
| 2 | **§10 第 1 項** —— `Else: Mute Active` 之記法若為「使之靜音」，牴觸由 1 增為 3 | 同上 |
| 3 | 三筆 DR 之發出 ＋ 日期與對象（`DR-PMH5` 第三問已附量測答案，性質降為「請確認」） | `DR-PMH5` 阻斷 ch 9 |
| 4 | §10 第 3 項 —— `-007` 之其餘四條 ER 未反向掃 | batch 1 之寫回 |
| 5 | §10 第 4 項 —— 「免責畫面必為 head unit 所顯示」無逐字支持，與 `VP` 未定義同源 | 否 |
| 6 | 章 9／12 × 矩陣之全對照；9.1 之 profile 例外；17 §5.4 其餘五項；Q10 | 否 |
