# 上繳包 26 —— 斷言之二分、掃描母體全枚舉與限定合併之可驗性

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/26_enumeration_over_keywords.md](../handoff/26_enumeration_over_keywords.md)
- 前一包上繳：[25_limitation_union.md](25_limitation_union.md)
- **本包零寫回工作簿**；**未改任何 TC**（`-007` 之七項限定一字未動）

**25 包之提交狀態**：已於 2026-08-25 經 Pei 授權並提交（`2fe66a6`，9 路徑）。

---

## ⚠ 本包之三項須先看

1. **三條停止條件全未觸發**，惟其中一條（8）之「未觸發」須讀作
   **「全枚舉之入選集合與關鍵詞篩選相同」，不是「關鍵詞篩選沒問題」**。（§4）
2. **`verdict_form.py` 在改造當輪就攔下了一次不同步** ——
   `ER_VERDICT` 之值由三元組改為四元組，記法自 `v[0]` 移至 `v[1]`，
   **本檔以 23 項全 FAIL 攔下**。（§7）
3. **batch 1 之涵蓋率由 78% 升為 100%**（18 條 ER → 23 個斷言，牴觸 0）。（§3）

---

## 一、§五三條之抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH97 | 斷言之二分；測試執行斷言不入掃描母體，須具名 | 633 | `831a17ff1f6c624b` | `831a17ff1f6c624b` | ✅ |
| R-PMH98 | 掃描母體為全枚舉，關鍵詞降為排序輔助 | 530 | `ac0769deb890f727` | `ac0769deb890f727` | ✅ |
| R-PMH99 | 限定合併之上限 ＋ ER 逐項複述 ＋ lint 字串檢查 | 388 | `9ac724e2d21b886d` | `9ac724e2d21b886d` | ✅ |

**命中數**：handoff 3 塊、RULINGS 回讀 3 塊，`a == b` 皆 `True`。
**既有條文未動**：`R-PMH10`／`R-PMH94`／`R-PMH96` SHA256 皆相符。

---

## 二、5 個未單獨對照之斷言（步驟 2）—— **牴觸 0**

25 §12 第 1 項所指之五個（`-001` ER1／ER3、`-002` ER2、`-004` ER2／ER3）
已逐一單獨對照：

| 斷言 | 類（R-PMH97） | 記法 | 依據之要點 |
|---|---|---|---|
| `-001` ER1.2 `no "Accept" button is shown` | SUT | 未對照 | 矩陣無 `Accept`（0 命中） |
| `-001` ER3.2 `the "Accept" button is shown` | SUT | 未對照 | 同上 |
| `-002` ER2.1 `The disclaimer screen is removed` | SUT | 未對照 | 矩陣無 `disclaimer`（0 命中） |
| `-004` ER2.2 `has not timed out` | SUT | 未對照 | 矩陣無 `timeout`；其 `Timer` 8 處全為 `Radio Off Delay` |
| `-004` ER3.1 `The disclaimer screen is removed` | SUT | 未對照 | 同 `-002` ER2.1 |

**牴觸 0 → 停止條件 7 未觸發。**

---

## 三、`batch_er_vs_matrix.py` 改以斷言為單位（步驟 3）

```
=== 結果 ===
  ER 條 **18** → **斷言 23**（比值 1.28）
  二分（R-PMH97）：SUT 行為斷言 **21**／測試執行斷言 **2**（後者不入掃描母體）
  記法：牴觸 **0**／印證 **1**／未對照 **20**／待定義 **0**
  未具名 **0**；**涵蓋率 100%**（25 包以 ER 條為單位時為 78%）
```

**涵蓋率 78% → 100%。**

**R-PMH97 之二分實測**：SUT 行為斷言 **21**／測試執行斷言 **2**
（`-003` ER2.1、`-004` ER1.1 之 `No user input is given`）。
**二者之歸類與理由已寫入 `ER_VERDICT` 之常數，非只在上繳包**（R-PMH97 明令）。

---

## 四、`spec_assertion_scan.py` 之矩陣側全枚舉（步驟 4，R-PMH98）

```
--- 矩陣側之**全枚舉**（R-PMH98）—— 斷言 `audio` ---

  母體 = 事件列之**全部有值格 174**（非關鍵詞命中之子集）
  入選（謂詞域 `audio`，判準 `\b(mute[sd]?|unmute[sd]?|audio|sounds?|volume|background)\b`）= **48** 格，分布於 **10** 列
  落選 = **126** 格 —— **逐格具名其落選理由**：

     41 格  該格之謂詞域為 ['state']，與 `audio` 不交
     28 格  該格之謂詞域為 ['power']，與 `audio` 不交
     25 格  該格之謂詞域為 ['display', 'power']，與 `audio` 不交
     10 格  該格之謂詞域為 ['display']，與 `audio` 不交
      9 格  該格無任何謂詞域之詞
      8 格  該格之謂詞域為 ['display', 'power', 'state']，與 `audio` 不交
      4 格  該格之謂詞域為 ['display', 'state']，與 `audio` 不交
      1 格  該格之謂詞域為 ['power', 'state']，與 `audio` 不交

  **落選之 126 格皆已具名其理由，無靜默略過者。**

  === 與關鍵詞篩選之對照（26 包停止條件 8）===
    關鍵詞篩選得 **48** 格；全枚舉入選 **48** 格
    **其所在之列是否相同：True**
```

### 4.1 四個斷言之結果

| 斷言 | 母體 | 入選 | 落選（**逐格具名理由**） | 與關鍵詞篩選之列集合相同 |
|---|---:|---:|---:|---|
| `popup` | 174 | 21（5 列） | 153 | **True** |
| `audio` | 174 | 48（10 列） | 126 | **True** |
| `announcement` | 174 | 0 | 174 | **True** |
| `popup_after` | 174 | 21（5 列） | 153 | **True** |

**四者之入選集合與關鍵詞篩選完全相同 → 停止條件 8 未觸發。**

### 4.2 ⚠ **「未觸發」之正確讀法**

**這不證明關鍵詞篩選沒問題** —— 只證明「本輪之粗篩判準與原關鍵詞
選出了同一批」。**二者本就以詞為之**（R-PMH98 允許之兩層作法）。

**真正之改變是**：落選之 153／126／174 格**現在各有一句具名之理由**
（依其自身之謂詞域），**而非不存在於輸出中**。
**母體自此可見；判準之偽陰仍在。** 已寫入 `LIMITS`。

### 4.3 落選理由之分布（以 `audio` 為例）

其 126 落選格依其自身之謂詞域分群具名，
如「該格之謂詞域為 `['state']`，與 `audio` 不交」（41 格）、
「該格無任何謂詞域之詞」（9 格）等 —— **無靜默略過者**。

---

## 五、`-007` 之七項限定之 lint 檢查（步驟 6，R-PMH99(c)）

新增 lint 第 31 項：**七項限定之字串於 procedure 中各出現一次**
（0 次或 ≥2 次皆 FAIL）。

```
=== R-PMH99(c) 之 must-hit（26 包步驟 6）===
**七項限定得合併於同一步驟，故『某項被忽略』與『某項被刪去』在文本上難以分辨** —— 本錨點即驗其可分辨。

  刪去 `press the ON/OFF key` → FAIL 被攔下：True
  刪去 `turn key-off` → FAIL 被攔下：True
  刪去 `open any door` → FAIL 被攔下：True
  刪去 `adjust HVAC hard controls` → FAIL 被攔下：True
  刪去 `press the Mute key` → FAIL 被攔下：True
  刪去 `the Headunit Mode key` → FAIL 被攔下：True
  刪去 `change the headunit mode by voice recognition` → FAIL 被攔下：True

  重複 `press the Mute key` → FAIL 被攔下：True

============================================================
刪去 7/7 皆 FAIL: True；重複 FAIL: True
```

**刪去 7/7 皆 FAIL；重複 1/1 FAIL → 停止條件 9 未觸發。**

**該 must-hit 已落為可重跑之模式**（`lint_batch.py --limit-must-hit`），
非一次性之臨時執行；並已註冊入 `check_table.py`。

**R-PMH99(a)(b) 之現況**：四步之分配為 **2/2/2/1**（≤2 ✅）；
ER 逐項複述（ER1～ER4 各對應其步驟之各項）✅。

---

## 六、章 12 × 矩陣之全對照（步驟 7）

```
=== 結果 ===
  牴觸 **0**／印證 **1**／未對照 **29**／待定義 **0**；未具名 **0**
```

**牴觸 0／印證 1／未對照 29；未具名 0。**

**唯一之印證**：`r16`（`SRT or Off Road+ Hard Button press.`）×
`OFF3.)`（`Head unit is muted when launching app from Power Off State`）——
**同一謂詞（是否靜音）取相同值**，且**矩陣補上了規格所無之另一半**
（`OFF3.)` 只說靜音而未言喚醒；矩陣逐字為 `Radio Wakes Up and mutes`）。
**與 `OFF1.)` 為互補之兩支**（20 包 §3 已定，本輪以四詞記法重記）。

**`r45`（Mute 鍵）× `OFF3.)` 之互斥依據為 `OFF3.)` 之條件句本身**
（`when launching app from Power Off State`）。

**章 7／8／10／11／12 全部完成全對照；章 9 待 `DR-PMH5`。**

---

## 七、⚠ `verdict_form.py` 在改造當輪攔下一次不同步（步驟 3 之連帶）

`ER_VERDICT` 之值由 `(記法, 謂詞, 依據)` 改為
**`(類, 記法, 謂詞, 依據)`**（R-PMH97 之二分），**記法自 `v[0]` 移至 `v[1]`**。

`verdict_form.py` 仍讀 `v[0]`，遂以 **23 項全數「未以四詞之一作結」FAIL** 攔下
（其讀到的是 `SUT`／`測試執行`）。

**該攔截即 R-PMH91 之價值之一次實地兌現** ——
**一個結構變更破壞了下游讀取，而檢查在同一輪內就報了出來。**
已修（讀 `v[1]`），並於該處具名其成因。

```
=== 對照結論之記法（R-PMH91）===
母體：各檢查之判定表，共 **241** 項

  batch_er_vs_matrix.ER_VERDICT                 23 項  {'未對照': 20, '—': 2, '印證': 1}
  chapter_bidirectional.RESIDUE_VERDICT         20 項  {'未對照': 11, '印證': 9}
  matrix_vs_chapter.VERDICT                    150 項  {'待定義': 4, '未對照': 138, '牴觸': 2, '印證': 6}
  spec_assertion_scan.AUDIO_CELL_VERDICT        10 項  {'未對照': 9, '牴觸': 1}
  spec_assertion_scan.AUDIO_LINE_VERDICT        13 項  {'—': 1, '未對照': 12}
  spec_assertion_scan.LINE_VERDICT              25 項  {'印證': 5, '未對照': 18, '—': 2}

  合計：{'未對照': 208, '印證': 21, '待定義': 4, '牴觸': 3, '—': 5}；**未以四詞之一作結 = 0**
```

---

## 八、由程式產生之檢查總表（R-PMH92）

| 檢查 | must-hit | 退出碼 | 期望 | **結果** | 備註 |
|---|---|---:|---:|---|---|
| `lint_batch.py generated/batch01.json` | ✅ | 0 | 0 | **PASS** | 外部 fixture 兩份（`batch01_prerework` 21/30、`batch01_r2` 29/30）逐輪實跑並 FAIL |
| `lint_batch.py <fixture prerework>` | ✅ | 1 | 1 | **PASS** | must-hit fixture —— 其 FAIL 即其通過 |
| `lint_batch.py <fixture r2>` | ✅ | 1 | 1 | **PASS** | must-hit fixture —— 其 FAIL 即其通過 |
| `lint_batch.py --limit-must-hit` | ✅ | 0 | 0 | **PASS** | 外部 fixture 兩份（`batch01_prerework` 21/30、`batch01_r2` 29/30）逐輪實跑並 FAIL |
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
| `matrix_vs_chapter.py 12` | ✅ | 0 | 0 | **PASS** | `--must-hit` 三項正向錨點（R-PMH86） |
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
  R-PMH99(c) `-007` 之七項限定字串各出現一次                           PASS
  procedure／ER 編號自 1 起連號且逐位對齊                              PASS
  tc_id 唯一                                                 PASS
  tc_id_status = provisional                               PASS
  本批 leaf == Disclaimer Screen 之 7 leaf                    PASS

31/31 PASS

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
| 7 | 5 個斷言對照發現**新的**牴觸 | 五者皆未對照，牴觸 **0** | **否** |
| 8 | 全枚舉（174 格）之結果與關鍵詞篩選**不同** | 四斷言之入選列集合**全部相同** | **否**（其讀法見 §4.2） |
| 9 | 步驟 6 之 must-hit（刪去任一項）未 FAIL | 刪去 **7/7 皆 FAIL**；重複亦 FAIL | **否** |

---

## 十一、未結 DR 清單（R-PMH82）

| DR | 主旨 | 狀態 | 發出日期 | 阻斷 |
|---|---|---|---|---|
| **DR-PMH5** | p9 矩陣之來源（第三問已由字級座標實測自答） | **`DRAFT`** | **（待填）** | **ch 9 開批** |
| **DR-PMH6** | RVC 情境之 HVAC popup ＋ 三項覆蓋缺口 | **`DRAFT`** | **（待填）** | 否 |
| **DR-PMH7** | `VP` 之定義 ＋ **`Else: Mute Active` 之記法** ＋ **`Note:` 之適用範圍**（本包增二問） | **`DRAFT`** | **（待填）** | 矩陣對照之四列 |

**合計未結 3 筆，三者皆 `DRAFT`。發出日期欄第五次空著。**

---

## 十二、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，六項。**

1. **§4 之「相同」是我用同一類判準比出來的。**
   全枚舉之粗篩判準與原關鍵詞**皆以詞為之**，
   **二者選出同一批是可預期的，不是驗證。**
   R-PMH98 所要之「母體全枚舉」我做到了，
   **「關鍵詞降為排序輔助」我沒有做到** —— 它仍在決定入選。

2. **規格側之全枚舉未做**（下放包明令本輪只做矩陣側）。
   **故 R-PMH98 現只實施了一半。**

3. **斷言之切分以 ` and ` 為之，該規則本身未經驗證。**
   `-004` ER2 `The disclaimer screen is still displayed and has not timed out`
   切為兩個；**而 `-002` ER1 `The disclaimer screen is displayed with the
   "Accept" button` 含兩個可分之斷言（畫面顯示／按鈕顯示）卻未被切開**
   —— 其連接詞為 `with` 而非 ` and `。**23 這個數字是該規則之產物。**

4. **R-PMH99(a) 之「每步至多兩項」我報 2/2/2/1 —— 而那是我自己數的。**
   lint 只驗字串各出現一次，**不驗每步幾項**。

5. **章 9 × 矩陣仍未對照**（待 `DR-PMH5`）。
   **五章已完成而一章未做，其未做之理由是外部的。**

6. **`-007` 之 pre_conditions 與 test_procedure 之斷言仍不入任何掃描母體**
   （`batch_er_vs_matrix.py` 之 `LIMITS` 已具名）。
   **R-PMH94 之單位是斷言，而我只掃 `expected_result` 之斷言。**

---

## 十三、建議之 commit 與 pathspec（**不執行**）

**訊息**：

```
feat(power_moding): package 26 — assertion dichotomy, full-enumeration matrix scan, limitation lint
```

**pathspec（9 路徑，R-G12 —— 逐一具名）**：

```
git commit -- \
  features/power_moding/DATA_REQUESTS.md \
  features/power_moding/RULINGS.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/26_enumeration_over_keywords.md \
  features/power_moding/docs/upstream/26_enumeration_over_keywords.md \
  features/power_moding/scripts/batch_er_vs_matrix.py \
  features/power_moding/scripts/check_table.py \
  features/power_moding/scripts/lint_batch.py \
  features/power_moding/scripts/matrix_vs_chapter.py \
  features/power_moding/scripts/spec_assertion_scan.py \
  features/power_moding/scripts/verdict_form.py
```

（實為 **11 路徑**。）

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py`／`docs/runtime/`／`PROFILE_INTEGRATION.md`／profile | **未動** |
| 工作簿寫回 | **無** |
| `generated/batch01.json` | **未動** —— 本包未改任何 TC |
| `ANOMALIES.md` | **未動** —— 本包未新增 anomaly |
| State Matrix xlsx／規格 PDF | **只讀** |
| 暫存檔 | `tests/fixtures/_limit_must_hit.json` 於 must-hit 中建立後**即刪**（`finally` 保證） |
| **對外發文** | **無** —— 三筆 DR 皆 `DRAFT` |
| 已執行之 git 狀態變更指令 | **無** |
| 併行 session（`features/display`）之檔案 | **未動** |

---

## 十四、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **三筆 DR 之發出 ＋ 日期與對象** —— `DR-PMH7` 現含**三問**（`VP`／`Else: Mute Active`／`Note:` 之範圍） | `DR-PMH5` 阻斷 ch 9 |
| 2 | **§12 第 1 項** —— 「關鍵詞降為排序輔助」未做到，粗篩仍在決定入選 | 否 |
| 3 | §12 第 3 項 —— 斷言之切分規則（` and `）未經驗證；`with` 連接者未被切開 | batch 1 之寫回 |
| 4 | §12 第 6 項 —— `pre_conditions`／`test_procedure` 之斷言不入母體 | 否 |
| 5 | 章 9 × 矩陣（待 `DR-PMH5`）；9.1 之 profile 例外；17 §5.4 其餘五項；Q10 | 否 |
