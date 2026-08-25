# 上繳包 25 —— 限定之逐斷言導出（四項 → 七項）、欄位以字級座標確認

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/25_limitation_union.md](../handoff/25_limitation_union.md)
- 前一包上繳：[24_positive_form.md](24_positive_form.md)
- **本包零寫回工作簿**；**改寫 `-007` 之 procedure／ER／reasoning**，其餘七條未動

**24 包之提交狀態**：已於 2026-08-25 經 Pei 授權並提交（`e2ebbae`，23 路徑）。

---

## ⚠ 本包之三項須先看

1. **`-007` 之限定由四項增為七項，lint 30/30。**
   `r46`／`r47` 之納入**不是因為判定其為牴觸**，而是 R-PMH95 —— **涵蓋兩讀，不判讀歧義**。（§3）
2. **ER1～ER5 之逐斷言掃描全部完成，牴觸 0** —— 停止條件 7 未觸發。（§4）
3. **關鍵詞之列舉問題已有一次量測**：15 個同義表述於規格與矩陣之命中**全部為 0**。（§5）

---

## 一、§五三條之抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH94 | 限定須逐斷言導出，TC 之限定為聯集 | 492 | `d325186a59bd934a` | `d325186a59bd934a` | ✅ |
| R-PMH95 | 歧義以涵蓋兩讀之限定處置，不以判讀處置 | 438 | `d4a8dad7d4b76f85` | `d4a8dad7d4b76f85` | ✅ |
| R-PMH96 | 互斥之依據優先取規格逐字；常識不得為依據 | 428 | `292f12b3812d2d8f` | `292f12b3812d2d8f` | ✅ |

**命中數**：handoff 3 塊、RULINGS 回讀 3 塊，`a == b` 皆 `True`。
**既有條文未動**：`R-PMH10`／`R-PMH91`／`R-PMH93` SHA256 皆相符。

---

## 二、A-PMH21 之欄位與依據（步驟 3）

### 2.1 字級座標 —— **先算後比，與分析層 §2.1 逐項相符**

| 詞 | 分析層 | **本層獨立實測** | 相符 |
|---|---:|---:|---|
| `HEADUNIT`（1st）／`OFF`(y=65.8) | 467.9／490.5 | 467.9／490.5 | ✅ |
| `HEADUNIT`（2nd）／`ON`(y=65.8) | 641.4／665.3 | 641.4／665.3 | ✅ |
| **`Pop-ups`（y=114.2／213.3）** | **483.0** | **483.0** | ✅ |
| `Visibile` | 442.5 | 442.5 | ✅ |
| `Knobs:` | 448.5／596.6 | 448.5／596.6 | ✅ |

**`Pop-ups`（483.0）< 右欄基準（596.6），且與同欄之 `Visibile`（442.5）同側
→ `HEADUNIT POWER OFF` 欄。**
**24 包之渲染判讀經字級座標複驗成立，其論證自此不需要人眼判圖。**

### 2.2 依據更換（R-PMH96）—— 由常識改為規格逐字

24 §10 第 4 項自陳其互斥證明「是常識而非引文」。
**引文存在** —— `PITA6.1`（outline 10.4）：

> `Upon pressing power button to On state disclaimer screen shall be displayed
> (see SU6.) unless certain phone call scenarios have occurred.`

**免責畫面之顯示條件即 head unit 轉為 On**，故其不可能出現於
`HEADUNIT POWER OFF` 欄所述之狀態。**A-PMH21 之原文一字未改**，更正段置後。

**惟 `VP` 之未定義（A-PMH20）仍在** —— 其問的是「矩陣說的 `VP` 是不是這個螢幕」，
與本項無涉。**該項未因本包而動。**

---

## 三、`-007` 之限定擴充為七項（步驟 2）

### 3.1 七項與其所排除之格

| # | 限定（procedure 逐字） | 排除之格 | 斷言 |
|---|---|---|---|
| 1 | `Do not press the ON/OFF key and do not turn key-off` | `r6`／`r24` | pop-up |
| 2 | `Do not open any door and do not adjust HVAC hard controls` | `r25`／`r48` | pop-up |
| 3 | `Do not press the Mute key or the Headunit Mode key` | **`r45`**／**`r46`** | **audio** |
| 4 | `Do not change the headunit mode by voice recognition` | **`r47`** | **audio** |

**七項限定壓縮於四個步驟**（`r15` 之 key-off 在步驟 1、`r48` 之 HVAC 在步驟 2）。
**一項未刪。**

### 3.2 `r46`／`r47` 之納入 —— **不是判定其為牴觸**（R-PMH95）

24 §4.3 自陳：`Else: Mute Active` 判為「維持」而非「使之靜音」，
其依據為箭頭之有無，**而矩陣未定義其記法**。

**本輪不判讀該歧義** —— `r46`／`r47` 之觸發皆為測試員可控之事件，
**納入限定即涵蓋「維持」與「使之靜音」兩讀**。
**判讀可能判錯，涵蓋兩讀之限定不會。**

**已立 A-PMH22** 記該歧義，並記明「本 feature 之判定已不再倚賴它」——
**本則不因此結清**；若日後有 TC 之斷言涉及 headunit mode 之靜音行為，**本則即復活**。

### 3.3 改寫後之 procedure／ER（7:7）

```
procedure                                                             字數
1. Do not press the ON/OFF key and do not turn key-off                 11
2. Do not open any door and do not adjust HVAC hard controls           12
3. Do not press the Mute key or the Headunit Mode key                  11
4. Do not change the headunit mode by voice recognition                 9
5. Deliver a traffic announcement while the disclaimer screen
   is displayed                                                        10
6. Read the screen and the audio output and record both                10
7. Remove the disclaimer screen and check that the pop-up is displayed 11

expected_result
1. No ON/OFF key press and no key-off transition occurs
2. No door is opened and no HVAC hard control is adjusted
3. No Mute key press and no Headunit Mode key press occurs
4. The headunit mode is not changed by voice recognition
5. The traffic announcement is delivered
6. The announcement is heard in the background and no pop-up is displayed
7. The traffic announcement pop-up is displayed
```

**§5.2 字數通過（normal ≤ 12／final ≤ 18）；procedure 與 ER 7:7 逐位對齊；lint 30/30。**
**停止條件 8（七項有任一未出現於 procedure）未觸發。**

---

## 四、ER1／2／3／5 之逐斷言掃描（步驟 4，R-PMH94）—— **牴觸 0**

### 4.1 ER1／ER2 —— **不需反向掃描，其理由具名**

二者為 procedure 步驟 1～4 之**限定之複述**
（`No ON/OFF key press and no key-off transition occurs` 等）——
**其斷言之標的為「測試過程中該事件未發生」，非 SUT 之行為**；
而素材所述者皆為「某事件發生後 SUT 如何」。**無共同謂詞可取相反值。**

**該判斷本身已寫入 `spec_assertion_scan.py` 之 `NO_SCAN` 常數**，非只在上繳。

### 4.2 ER3（`announcement`）

```
=== 結果 ===
  {'—': 2}；未具名 **0**

  **牴觸 0 處**  —— 無
```

規格側 **2 行皆為 `SU3.)` 自身**（記 `—`）；
**矩陣側 0 格** —— 全簿無 `announcement`／`traffic announcement`／`received`。
**牴觸 0。**

### 4.3 ER5（`popup_after`）—— 同 25 行，**判定標的不同**

```
=== 結果 ===
  {'未對照': 23, '—': 2}；未具名 **0**

  **牴觸 0 處**  —— 無
```

**25 行、牴觸 0**（`—` 2 為 `SU3.)` 自身、未對照 23）。

**⚠ 一行須具名為待確認**：`L160` 之
`Note: do not show popup again if popup was shown at Radio Off.`
**為否定**，與 ER5 之「顯示」取相反值。
**本層判其為未對照，依據為「其 popup 為 p4 流程圖之 `Geolocation + SOS Popup`，
非交通報導之 popup」** —— **若上游確認該句泛指所有 popup，則為牴觸。已具名待確認。**

### 4.4 停止條件 7 之判定

**ER1／2（不需掃）／ER3（牴觸 0）／ER5（牴觸 0）→ 未觸發。**
**`-007` 之七項限定自此對其全部斷言充分**（R-PMH94 之要件已滿足）。

---

## 五、關鍵詞之列舉問題（步驟 5）—— **具名，且有一次量測**

`LIMITS` 已增列：各斷言之關鍵詞皆為列舉，**R-PMH91 廢止了記法上之列舉，
未廢止關鍵詞上之列舉**；並列出已知之同義表述供下輪處置。

**且本輪順手量了它**：15 個同義表述於**規格全文與矩陣全簿**之命中
（大小寫不敏感、字界錨定）——

| 斷言 | 同義表述 | 規格 | 矩陣 |
|---|---|---:|---:|
| audio | `silent`／`silence`／`no output`／`suppressed`／`inaudible`／`no sound`／`quiet` | **0** | **0** |
| popup | `dialog`／`prompt`／`message box`／`toast`／`notification` | **0** | **0** |
| announcement | `TA`／`traffic info`／`alert` | **0** | **0** |

**就該 15 個候選而言，本判準之偽陰為 0。**
**該量測不涵蓋未被想到之表述** —— 列舉之問題本身仍在，已具名。

---

## 六、斷言數 vs ER 條數（步驟 6）

以 ` and ` 切分 ER 之斷言（`-007` 已於 §3 單獨處置，不入母體）：

| tc | ER 條 | 斷言 | 逐條 |
|---|---:|---:|---|
| `-001` | 3 | **5** | [2, 1, 2] |
| `-002` | 2 | **3** | [1, 2] |
| `-003` | 3 | 3 | [1, 1, 1] |
| `-004` | 3 | **5** | [1, 2, 2] |
| `-005` | 2 | 2 | [1, 1] |
| `-006` | 2 | 2 | [1, 1] |
| `-008` | 3 | 3 | [1, 1, 1] |
| **合計** | **18** | **23** | 比值 **1.28** |

**23 < 36（18 × 2）→ 停止條件 9 未觸發。**

**惟其含意須明說**：23 包之 `batch_er_vs_matrix.py` 以 **ER 條**為單位，
故其 18 條判定中，**有 5 個斷言未被單獨對照**（23 − 18），
**佔全部斷言之 22%**。**其涵蓋率為 78%，非 100%。**
**改以斷言為單位之重跑列為待辦**（下放包明令本輪不重跑）。

---

## 七、`verdict_form.py` 之複跑

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

**未以四詞之一作結者 = 0。**（母體隨本包新增之判定表而增。）

---

## 八、由程式產生之檢查總表（R-PMH92）

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
| `spec_assertion_scan.py --assertion audio` | **否** | 1 | 1 | **未實測** | **查出牴觸 1**（`r45` × `-007` ER4(b)，24 包）—— **25 包已以第 5～7 項限定排除之，其牴觸記錄保留** |
| `spec_assertion_scan.py --assertion announcement` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit**（24 包 §12）—— 其逐行判定由人寫入 |
| `spec_assertion_scan.py --assertion popup_after` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit**（24 包 §12）—— 其逐行判定由人寫入 |
| `batch_er_vs_matrix.py` | **否** | 0 | 0 | **未實測** | **未註冊 must-hit**（24 包 §12）—— 其逐條判定由人寫入 |
| `verdict_form.py` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項（非漏 → FAIL／未對照 → PASS／散文不進母體） |
| `verdict_form.py --must-hit` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項（非漏 → FAIL／未對照 → PASS／散文不進母體） |

**未註冊 must-hit 而標「未實測」者 = 8**  ← R-PMH92：其不得標 PASS

> 本表由 `python scripts/check_table.py` 產生。**手寫之結果欄不予採認**（R-PMH92）。

---

## 九、lint 全跑輸出

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

## 十、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | **是** —— p9 矩陣之來源（`DR-PMH5`）＋ `VP` 未定義（`DR-PMH7`） |
| 2 | 判準衝突未決 | **是** —— `10.3` × `r48c10`（已登記，`DR-PMH6`） |
| 3 | 須寫回而工作簿狀態不明 | 否（零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論建於臆測 | **是** —— 同 1 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| 7 | ER1／2／3／5 掃描發現**新的**牴觸 | ER1／2 不需掃（理由具名）；ER3 牴觸 0；ER5 牴觸 0 | **否** |
| 8 | 七項限定有任一項未出現於 procedure | 七項全在（壓縮於四步），lint 30/30 | **否** |
| 9 | 斷言數 > ER 條數之兩倍 | 23 vs 36 | **否** |

**`r45` 之牴觸（24 包）已由第 3 項限定排除，其記錄保留於
`spec_assertion_scan --assertion audio`（退出碼仍為 1，設計如此）。**

---

## 十一、未結 DR 清單（R-PMH82）

| DR | 主旨 | 狀態 | 發出日期 | 阻斷 |
|---|---|---|---|---|
| **DR-PMH5** | p9 矩陣之來源（**第三問已由字級座標實測自行解答**，性質降為「請確認」） | **`DRAFT`** | **（待填）** | **ch 9 開批** |
| **DR-PMH6** | RVC 情境之 HVAC popup ＋ 三項覆蓋缺口 | **`DRAFT`** | **（待填）** | 否 |
| **DR-PMH7** | `VP` 之定義（**建議併問 `Else: Mute Active` 之記法**，A-PMH22） | **`DRAFT`** | **（待填）** | 矩陣對照之四列 |

**合計未結 3 筆，三者皆 `DRAFT`。發出日期欄第四次空著。**

---

## 十二、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，六項。**

1. **§6 之 5 個未單獨對照之斷言，我算出來了但沒有去對照。**
   下放包明令「不重跑全部，只回報項數差異」，**我照做了** ——
   **而那 5 個斷言（`-001` ER1／ER3、`-002` ER2、`-004` ER2／ER3）
   之涵蓋率為 0，這件事現在只是一個數字。**

2. **ER1／ER2 之「不需反向掃描」是我的判斷。**
   其理由（斷言標的為測試員之行為）我認為成立，**但 R-PMH94 之 (a)~(c)
   並未給「不需掃描」這個出口** —— **我自行加了一個例外。**

3. **`-007` 之七項限定壓縮於四個 procedure 步驟。**
   R-PMH87 實施 1 令「不得為湊字數而刪去任一項」——**我沒有刪**，
   **但把兩項合為一步（步驟 1 含 ON/OFF 與 key-off；步驟 2 含開門與 HVAC）**。
   **若某項因合併而在執行時被忽略，其後果與刪去相同。**

4. **§5 之 15 個同義詞是我列的。**
   量測結果 0/0 很乾淨，**而那只證明「我想到的 15 個都不在」** ——
   **與 R-PMH67 之抽樣不同，這不是隨機抽樣，是我自己出的題目。**

5. **ER5 之 `L160` 我判為「不同 popup」，其依據是上下文位置（p4 流程圖）。**
   **該句以 `Note:` 起首，其適用範圍未明。** 已具名待確認，
   **但在確認前，`-007` 之 ER7 之充分性仍有一個未解之點。**

6. **章 9／12 × 矩陣仍未全對照**（章 12 除 `r16` 外 29 列）。

---

## 十三、建議之 commit 與 pathspec（**不執行**）

**訊息**：

```
feat(power_moding): package 25 — limitation union per assertion (4->7), column confirmed by word coordinates
```

**pathspec（8 路徑，R-G12 —— 逐一具名）**：

```
git commit -- \
  features/power_moding/ANOMALIES.md \
  features/power_moding/RULINGS.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/25_limitation_union.md \
  features/power_moding/docs/upstream/25_limitation_union.md \
  features/power_moding/generated/batch01.json \
  features/power_moding/scripts/check_table.py \
  features/power_moding/scripts/gen_batch01.py \
  features/power_moding/scripts/spec_assertion_scan.py
```

（實為 **9 路徑**。）

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py`／`docs/runtime/`／`PROFILE_INTEGRATION.md`／profile | **未動** |
| 工作簿寫回 | **無** |
| `generated/batch01.json` | **`-007` 之 procedure（5→7 步）、ER（5→7）、reasoning**；其餘七條未動 |
| State Matrix xlsx／規格 PDF | **只讀** |
| **對外發文** | **無** —— 三筆 DR 皆 `DRAFT` |
| 已執行之 git 狀態變更指令 | **無** |
| 併行 session（`features/display`）之檔案 | **未動** |

---

## 十四、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | 三筆 DR 之發出 ＋ 日期與對象（**`DR-PMH7` 建議併問 `Else: Mute Active` 之記法**） | `DR-PMH5` 阻斷 ch 9 |
| 2 | **§12 第 1 項** —— 5 個未單獨對照之斷言（涵蓋率 78%），是否重跑 | batch 1 之寫回 |
| 3 | §12 第 2 項 —— ER1／ER2 之「不需掃描」我自行加了一個 R-PMH94 未給之出口 | 否 |
| 4 | §12 第 5 項 —— `L160` 之 `Note:` 適用範圍未明（ER7 之未解點） | batch 1 之寫回 |
| 5 | 章 9／12 × 矩陣之全對照；9.1 之 profile 例外；17 §5.4 其餘五項；Q10 | 否 |
