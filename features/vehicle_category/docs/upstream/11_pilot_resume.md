# 上繳包 11 —— Vehicle Category：pilot 停點解除（T60–T66）

- 日期：2026-08-26
- 對應下放：`docs/handoff/11_pilot_resume.md`
  （SHA256 `e8e9afc2b8b2d8cfde1c6877b115d830a4d392d2a7659c796143077ad803ac6b`，197 行）
- **結論：T60–T66 七項全數完成。收斂條件 13 checked / 0 failed，pilot 收斂。**
- 未寫回工作簿、未改 lint、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T60 | R-VC19／R-VC20 抄錄 | ✅ 逐字（`4cc9e8c8619c0166`／`6b751ccd2a3fa1d8`）|
| T61 | VC profile | ✅ 112 行，四節；**lint 支援程度如實回報 → 無法實作 (c)** |
| T62 | 6 筆保留記法之來源驗證 | ✅ **6 token / 0 未對上** |
| T63 | `VC-033-01` 之 R-VC20 處置 | ✅ 四項揭露已補；**ER 複查後無須改** |
| T64 | 重跑 `verify_pilot.py` | ✅ **13 checked / 0 failed** |
| T65 | T52 全表掃描 | ✅ **已於上繳包 09 §1 完成並回報**（見 §6）|
| T66 | RUNBOOK 勾選 ＋ A-VC15 | ✅ |

**一件請你先看**：§四.3 說「T52 尚未見於上繳包 10」——
**它在上繳包 09**（本 feature 之 09 與 10 為同輪產出之二份）。
結果為真陽性 1 筆（即 `VC-033-01` 本身），故 R-VC20 之適用範圍
現階段為單筆。詳見 §6。

---

## 1. T60 —— R-VC19／R-VC20

抄入 `RULINGS.md` 行 640／675（接 R-VC18 之後）。

| 條 | 來源 | bytes | lines | sha256(前16) | 逐字一致 |
|---|---|---|---|---|---|
| R-VC19 | 包11 50–79 | 1,783 | 30 | `4cc9e8c8619c0166` | **是** |
| R-VC20 | 包11 120–146 | 1,518 | 27 | `6b751ccd2a3fa1d8` | **是** |

---

## 2. T61 —— VC profile

檔：`docs/runtime/profiles/FW036_R1L_VehicleCategory_Profile.md`（112 行）。
命名 `VehicleCategory`（CamelCase 無分隔），與 `VehicleSetting` 並列。

四節最小內容：**§0 適用範圍**（六項，各標其權威條號）／
**§1 `[OVERRIDE]` 引號例外**（逐字採 R-VC19 (a)–(d)）／
**§2 lint 之 profile 分流**（見下）／
**§3 IN §8.7.5 無適用對象**。
另設 **§4「本檔未涵蓋者」**，載明四項刻意未寫入者，
並記「**未寫入不等於已裁定為預設**」——
此為 A-VC8 家族（宣告一個不被讀的東西）之反向防範。

### 2.1 lint `--profile` 支援程度 —— **無法實作 R-VC19(c)**

R-VC19 §2.3 第 3 項要我「如實回報其能否實作 (c)」。**不能。** 五項實測：

| # | 事實 | 證據 |
|---|---|---|
| 1 | `--profile FEATURE` **不讀取任何 profile 檔案** | `grep 'profile\s*==\|profile.lower()\|profile in '` **零命中** |
| 2 | 該值僅作**真值**使用，字串內容從未被讀取 | `lint036.py:185`／`:189`／`:195`／`:496`／`:740` |
| 3 | 故傳 `--profile vehicle_category` 與傳**任意非空字串等效** | 由 1、2 推得 |
| 4 | 其作用固定：`P` 改採 R-1 v3、另啟 `Q`／`R`／`T` | `check_order()`／`PROFILE_CHECKS` |
| 5 | **輸入為 `.xlsx`**，非 `generated/*.json` | `files` metavar「一個或多個 .xlsx 路徑」；`openpyxl.load_workbook` |

另查引號能力：`quoted_spans()`（`:294`）只認 `" "` 與 `“ ”`，
且僅供檢查 B（ER 情態詞之引號內豁免）。
**無禁止 `'...'`／`«...»` 之檢查，亦無驗證來源之機制。**

**即：本 feature 之 profile 寫了什麼，`lint036` 都看不到。**

依 R-VC19 §2.3 第 3 項「不得改 lint」——**未改**。
登記為 **A-VC15**，提案處置二項（`--profile` 改為讀檔、新增來源驗證檢查），
並註明**與 R-VC8 之授權非同一件不得併案**（R-VC8 之範圍為 `recon.py`）。

### 2.2 一項順帶記入 profile 之推論

037 全文之 CAN／PROXI／VF 命中皆為 0（R-VC10），故
`--profile` 所啟之 `P`（R-1 v3 訊號寫法）與 `RE_P3_*` 系列
於本 feature **應恆為零違規** —— **非因合規，而因無訊號行**。
已於 profile §3 記明：日後若見該項全綠，**不得讀為「訊號寫法已驗」**。

---

## 3. T62 —— 保留記法之來源驗證（R-VC19(c)）

腳本：`scripts/t62_verbatim_source_check.py`。由人工流程承擔，
**不隨 lint 執行**（A-VC15），故逐輪明列於此。

```
母體: 12 TC（Glove Box，12 leaf ⊂ 117 leaf 母體）
帶非 "..." 記法之 TC: 6
token 數: 6

leaf                  token                        出處          判
SWE1-HMI-VC-026-01    'Glove Box'                  Title        PASS
SWE1-HMI-VC-026-02    'Yes'                        Title        PASS
SWE1-HMI-VC-027       'Glove Box Activated'        Title        PASS
SWE1-HMI-VC-030       «Glove Box»                  Description  PASS
SWE1-HMI-VC-031       'Glove Box Mode deactivated' Title        PASS
SWE1-HMI-VC-032       «OK»                         Description  PASS

6 tokens / 0 未對上來源
```

**6/6 對得上。** 恰為上繳包 10 §5 所列之六筆 —— 二者為同一集合。
四筆之記法來自 `Title`（`'...'`）、二筆來自 `Description`（`«...»`），
與 profile §1(a) 所述之二種來源記法一一對應。

---

## 4. T63 —— `VC-033-01` 之 R-VC20 處置

### 4.1 (c) 之複查：**ER 無須改**

R-VC20(c) 要我複查 ER 有無 `third`／`three`／`fourth` 等次數判準。
現行 ER 三項：

```
1. The PIN popup is displayed
2. Each wrong entry is rejected and the sequential wrong-entry count advances
3. The deactivation feature is blocked for 30 minutes
```

**三項皆為行為表述，無門檻值。** 第 2 項之
`the sequential wrong-entry count advances` 說的是計數在推進，
不是計數達到幾 —— 判準位置無爭議值。門檻由 procedure 之 `PENDING` 承載。

> 過程記一筆：我的快掃正則對 ER 報了 `['1','2','3']` 三個命中 ——
> 那是**條列編號**（`1.` `2.` `3.`），不是門檻值。正則未排除行首序號。
> 逐字讀過三行後確認無誤。**又一次是檢查手段誤報，不是內容有錯。**

### 4.2 (b) 之四項揭露：已補入 `reasoning`

`reasoning` 由 430 字元增為 1,159 字元。新增段落之四項：

| # | 項 | 內容 |
|---|---|---|
| 1 | 二欄逐字內容 | Title 與 Description 全句照錄 |
| 2 | 分歧點 | **二者之數字同為 three，差別在比較器** —— `After three` 觸發於第 3 次、`more than three` 觸發於第 4 次 |
| 3 | 以何欄為上半及理由 | 取 `Title`，因其為完整需求句（R-S4）；**非採信其值為 3**；依 R-VC20(a) 不換欄取值 |
| 4 | 阻斷之 DR | **DR-VC8**（同批 A），回覆後依值 Revise 並依 R-VC18 另裁 boundary 拆分 |

另載 (c) 之複查結論。

### 4.3 我接受「那不是自我矛盾」之更正

上繳包 10 §6 我寫「交付欄位裡出現了一個 PENDING 說它未定的值」，
並稱其為自我矛盾。**§3.1 之更正成立**：上半是**引用**不是**斷言**，
其性質為「規格對此事的原話是這樣」。

不一致之所在**本來就在上游**，我們的產出只是忠實反映它。
我當時想的是「怎麼讓 TC 內部看起來一致」，
那個方向本身就會把上游的問題藏進產出裡。
正解是**讓不一致可被讀懂**，即 (b) 之揭露。

---

## 5. T64 —— `verify_pilot.py` 重跑：13 checked / 0 failed

```
  1  12 筆 JSON 完整，10 個必要 key 齊備（IN §10.1）                      PASS
  2  IN §9 十七項自檢（機械化子項見第 3–8 項；全項見上繳包）                         PASS
  3  test_item 括號下半 12 筆兩兩不同（機械）                               PASS
 3b  test_item 括號下半無中文（R-S4）                                   PASS
  4  specification_reference 12 筆與 recon_leaf_to_section.tsv 逐字相符  PASS
  5  priority 12 筆與 priority_final.tsv 逐字相符                      PASS
  6  Test Set 12 筆皆為 `Glove Box`，Test Group 皆為 `Vehicle Category` PASS
  7  尾句號／方括號／單引號／行首尾空白（IN §11，作者欄位）                            PASS
 7b  test_item 上半保留之來源記法對得上其來源列（R-VC19(c)）                    PASS
     保留 token 6 個；未對上來源 0 個
  8  `VC-033-01` 帶且僅帶一處 PENDING，字串逐字相符                          PASS
  9  `028-02`／`033-01` 之括號下半明載其流程                              PASS
 10  `VC-021` 之委派載於全部 12 筆之 reasoning（§8.2.1）                  PASS
  A  Procedure ≥2 步 ∧ Procedure↔ER 1:1 ∧ ER 無 modal ∧ 無 observe/verify 起首 PASS
13 checked / 0 failed
```

### 5.1 ⚠ 7b 之判準改變 —— 依據是裁決，不是結果

7b 前一輪判 FAIL（「是否帶非 `"..."` 記法」），本輪判 PASS
（「保留之記法是否對得上來源」）。**判準換了。**

**其依據為 R-VC19 落條與 profile 存在**，非為了讓結果變綠：
§11 之例外其啟動條件為「when the feature profile says so」——
前一輪 profile 不存在故例外未啟動，本項判「禁止」；
現在 profile 存在且明文，故依 R-VC19(c)「lint 之職責由禁止改為
驗證其來源」改判。**前提改變在先，判準改變在後。**

該理由已逐字寫入 `verify_pilot.py` 之該段註解，
使日後讀腳本者不必回頭翻上繳包才知道為何改。

### 5.2 §四.2 之配套 —— 每項判準之反例

下放包 §四.2 要求「每一項判準須載明其反例（什麼樣的輸入應該 FAIL）」，
使判準本身可被複核：

| # | 應 FAIL 之輸入 |
|---|---|
| 1 | 任一 TC 缺 `split_reason`；或 `tcs` 長度 ≠ 12 |
| 3 | 二筆之括號下半逐字相同；或某筆 `test_item` 無末尾 `(...)` |
| 3b | 括號下半寫成繁中（如 `(啟用流程之說明彈窗)`）—— 即 R-PMH153 之形態 |
| 4 | `specification_reference` 少一段章節號、或前綴少一個底線 |
| 5 | 把 `VC-032` 之 `P3` 寫成 `P2`（與 `priority_final.tsv` 不符）|
| 6 | 某筆 `test_set` 寫成 `GloveBox`／`Glove box`（變體拼寫）|
| 7 | ER 某行以 `.` 結尾；或 procedure 寫 `Press [OK]`／`Press 'OK'` |
| **7b** | **`test_item` 上半出現 `«Cancel»`（037 二欄皆無此 token）** —— 即「保留了一個來源沒有的記法」|
| 8 | `PENDING` 出現於第二筆 TC；或字串寫成 `PENDING: DR-VC8 lockout` |
| 9 | `033-01` 之括號下半寫成 `attempt threshold`（未載 deactivation）|
| 10 | 某筆 `reasoning` 未提 `VC-021` |
| A | ER 寫 `The popup shall be displayed`；或 procedure 首步寫 `Verify that…` |

**7b 之反例尤須看** —— 它區分了「保留來源記法」（准）與
「保留一個來源沒有的記法」（禁）。前一輪之判準無法區分二者，
因其只問「有沒有非 `"..."` 記法」。

### 5.3 本輪之檢查器錯誤：一件

T63 之 ER 快掃正則未排除行首序號，對 `1.` `2.` `3.` 報三個假命中。
**未影響結論**（逐字讀過三行後確認 ER 無門檻值），
但併上前二輪之二件，**三輪三支檢查器各出一錯**：

| 輪 | 檢查器 | 錯 |
|---|---|---|
| 09 | `t52_numeric_conflict_scan` 初版 | 類別切分，漏抓它要抓的那一筆 |
| 10 | `verify_pilot` 初版 modal 檢查 | 未排除引號內之 `must` |
| 11 | T63 之 ER 快掃 | 未排除行首序號 |

三件皆為**判準寫得比標的粗**。§四.2 之反例要求正是對此的處置 ——
寫得出反例，判準的邊界就被逼出來了。

---

## 6. T65 —— T52 已完成，在上繳包 09

下放包 §四.3 稱「T52 之全表掃描結果尚未見於上繳包 10」。
**它在上繳包 09 §1** —— 本 feature 之 09 與 10 為同輪產出之二份上繳包
（09 對應下放包 09 之 T52–T55，10 對應下放包 10 之 T56–T59）。

結果摘要（全文見 `docs/upstream/09_pilot_amend.md` §1）：

```
母體: 117 leaf
二欄至少一方含數值者: 38
同類別而 (值, 比較器) 不一致者: 10
→ 逐筆判讀：真陽性 1（VC-033-01 本身）／假陽性 6（章節標記滲入）／
             非矛盾 3（exactly one vs only one 等同義措辭）
```

**故 R-VC20 之適用範圍現階段為單筆**（`VC-033-01`）。

⚠ 該掃描之**初版漏抓 `VC-033-01` 自身**（類別切分錯誤），修正後始命中；
其五型偽陰性列於上繳包 09 §1.4。**「全表僅此一例」之效力以該方法為限。**

---

## 7. 未結清單

**DR 八筆全未結**（DR-VC1 ~ DR-VC8）。同批 A 五項。
**A 十一筆未結**：A-VC2、A-VC3、A-VC4、A-VC8、A-VC9、A-VC10、A-VC11、
A-VC12、A-VC13（通則）、A-VC14、**A-VC15**。
已結四筆：A-VC1（撤銷）、A-VC5／A-VC6／A-VC7（RESOLVED）。

**全域排程現有五筆工具修法**：A-VC4（`new_feature.py`）、
A-VC8（`recon.py` 之 `leaf_count`）、A-VC11（`recon.py` 之顯示層）、
A-VC13 通則（送簽稿元資料）、**A-VC15（`lint036.py` 之 `--profile`）**。
五者標的各異，依既有裁定不得併案。

---

## 8. 待你裁

1. **pilot 是否收斂放行** —— 十項收斂條件已全過（13 checked / 0 failed）。
   下放包 10 §四末句「收斂後始得議 Phase 4 之全量批次」。
2. **§四.1 之分析層複核** —— `-028-02`／`-033-01` 之流程區分由分析層
   逐字複核，不採信機械檢查。本輪未動該二筆之括號下半與 reasoning。
3. 同批 A（五項）與 DR-VC3 之發送（Tier 3）。

---

## 9. 量測條件揭露（R-G8）

- **T61 之 lint 調查為靜態閱讀**（grep + 讀 argparse 與呼叫點），
  **未實際以 `--profile` 跑過本 feature 之工作簿** ——
  因本 feature 尚未寫回，無 `.xlsx` 可跑。
  故「無法實作 (c)」之結論來自**程式碼結構**，非執行實測。
  若日後 lint 有未被 grep 命中的動態載入路徑，本結論須重驗。
- **T62 之比對為子字串包含**（逐字，不正規化空白與大小寫）。
  **偽陰性風險**：若某 token 在 037 中跨行斷開（如 `'Glove\nBox'`），
  包含檢查會判為未對上而虛報 FAIL。本次 6 筆皆單行，未實現。
- **T63 之 (c) 複查為人工逐字讀三行 ER**，其正則僅作輔助且已知誤報。
  以人工為準。
- **7b 之判準改變**其依據為裁決（R-VC19）而非量測，
  故不列入本節；其理由記於 §5.1 與腳本註解。
