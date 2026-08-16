# 33 — Comfort HMI / R-C39、階層×等價、四軸窮盡、批次 7、第二次寫回

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 44 ＋ 45
- 結果：九項全數落實。R-C39 已貼入、profile §5.3 增第四出口；
  `122-02` 依五條件核對後**維持停下**（第二項不成立）。
  階層×等價組合後**新增 0 對、重分類 3 對**，並修正一處靜默丟字。
  五軸窮盡實測完成，**未見任何未列之值**。批次 7 產 **17 條**（`-098`…`-114`）。
  lint **42/42 PASS，114 條**。
  **第二次寫回已產出，但 assertion 3 項 FAIL —— 該檔不可交付，且非本次寫入之錯誤，
  是範本只有 50 列。已登 DR #35，未送 Pei 確認。**

---

## 0. 下放包十一項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 44-1 | R-C39 貼入 `RULINGS.md`；profile §5.3 增出口 | ✅ §1 |
| 44-2 | `122-02` 依五條件處理，條件三逐句比對須具名 | ✅ §2 —— **第二項不成立，維持停下** |
| 44-3 | `RUNBOOK` 記「數字對不上是唯一的線索」 | ✅ §3 |
| 44-4 | profile 記推導欄重算風險 | ✅ §3（profile §5.5）|
| 44-5 | 階層與等價可組合，回報新增對數 | ✅ §4 —— **新增 0、重分類 3**，見 §4.2 |
| 44-6 | 更新三對 sibling 之 `distinguishing_axis` | ✅ §5 |
| 44-7 | 四軸窮盡實測，更新 `value-count` 語意與具名 | ✅ §6 —— 做了**五**軸；另見 §6.3 之機制上限 |
| 44-8 | 開 `controls screen` 之 DR | ✅ §7（DR #34）|
| 44-9 | 執行批次 7 | ✅ §8 —— **Layer 3 為四節而非三節**，見 §8.1 |
| 45 | 第二次寫回，ENTRY 003，產出後停下 | ⚠️ §9 —— **已產出、3 項 FAIL、不可交付**；編號改 **ENTRY 004** |
| 44-11 | 上繳 33 | 本件 |

---

## 1. R-C39 與 profile §5.3 之第四出口

R-C39 原文貼入 `RULINGS.md`（置於 R-C38 之後）。profile §5 現為五段：
§5.1 `[BLOCKED-SPEC]`／§5.2 `[BLOCKED-NON-HMI]`／**§5.2a `[COVERED-BY]`**／
§5.3 對照與次序／§5.4 R-C16 不產列者／§5.5（見 §3）。

判別次序改寫為樹狀，第一問之「有」分岔為二：

```
條文有無委派字面？
├─ 有 → 委派對象是外部文件，抑或本 spec 之節？
│   ├─ 外部文件     → [BLOCKED-SPEC]
│   └─ 本 spec 之節 → [COVERED-BY]（對象節未生成 → 記 deferred，不得先標）
└─ 無 → 本 feature 內有無可觀察端？
    ├─ 無 → [BLOCKED-NON-HMI]
    └─ 有 → 正常生成
```

§5.2a 另以引文記下 44 §2 之判斷理由，因為它比欄位表更難重建：

> 前三類皆為「**本交付件不涵蓋**」；`[COVERED-BY]` 是「**本交付件涵蓋，
> 但在別的列上**」。標成任何一種 BLOCKED，等於向評閱方宣告一個實際上
> 已被涵蓋的缺口。

`lint_tcs.py` 之具名回報行亦依此分列（本輪 `[COVERED-BY]` 為 0 列）。

---

## 2. `122-02` —— 五條件逐項核對，第二項不成立

| 條件 | 結果 | 依據 |
|---|---|---|
| 一、委派對象為本 spec 之節 | ✅ | 「see **Climate section**」未指名任何外部文件 |
| **二、對象節之 leaf 已產出 TC** | **❌** | 見下 |
| 三、逐句比對其 ER | **無法執行** | 無對象 TC 可比 |
| 四、扣除委派後無獨立餘留 | ✅ | 餘留為「depend on system configuration」，無可判之期望值 |
| 五、白名單增列 | 未進入 | —— |

**第二項之實測（R-C30，具名搜尋範圍）**：
`data/section_fulltext.tsv` 全 **129 節**——

| pattern | 命中 |
|---|---|
| `off icon\|icon of seats` | **1 節，即 `16.16` 自身** |
| `\bicon\b` | 13 句／9 節：`2.5`／`7.3`／`10.8`／`11.10`／`12.3`／`14.16`／`14.16.1`／`16.5`／`16.16` |

**條文根本沒有指名一個節** —— 「Climate section」不是節次。座椅類之候選只有
兩處，且**兩組皆未生成**：

- `12.3`（Heated Vented Seats）：`Active button state text/icon color is white.
  Inactive button text/icon color is grey.`
- `14.16.1`（Climate Popups）：`The icon will grey out if the heated and
  vented seats are off.`

依 R-C39 明文「第二項未滿足時**不得先標** `[COVERED-BY]`，該 leaf 標
`deferred`」，**維持停下、不產列**。

**須先答之問，已寫入 DR #32**：上列兩節所述為**顏色**與**熄滅時之灰化**，
**皆非「configuration → icon」之對照**。故該二節生成之日，**第三項仍可能
不成立** —— 屆時本項將轉為 §8.4.2 之 coverage gap，而不是 `[COVERED-BY]`。
先把這句寫下來，是為了那一天不必重推一次。

**A-CF25**（ICE1 引 ICE11 而該規則實居 ICE9）與本項獨立，維持登記。

---

## 3. 兩處記述

**`RUNBOOK.md`「數字對不上，是唯一的線索」** —— 記 26→10 之差、
其成因、以及三項可操作推論（先記舊輸出再改；預期值寫下來再跑；差額要追到底
且能被解釋才算追完）。末句記其與 R-C30 同源：
**一個沒有參照物的觀察，不構成證據。**

**profile §5.5「推導欄之重算風險」** —— 新增推導欄時之三問，其中第 2 問是關鍵：

> **推導欄之危險不在它會變，而在它變的時機往往正好是它該被凍住的時機。**

---

## 4. 階層 × 等價 —— 組合成立，且修好一處靜默丟字

### 4.1 實測：`DEF` 與 `DEFROST` 在複合名內是同一個字

先量再改。全 129 節之 `(FRONT|MAX|REAR)?\s*/?\s*(DEF|DEFROST)` 命中：

| 形式 | 次數 | 出現節 |
|---|---|---|
| `MAX DEF` | 32 | 16.13／16.3／16.4／16.8／3.2／3.3 |
| `REAR DEFROST` | 19 | 8 節 |
| `DEFROST`（單獨）| 15 | 15.1／16.15／2.12.2／2.15／2.4／2.8／2.9 |
| `FRONT/MAX DEFROST` | 3 | 16.10／2.10 |
| **`FRONT DEFROST`** | **2** | **2.3** |
| `MAX DEFROST` | 2 | 15.1／3.2 |
| `FRONT /MAX DEFROST` | 1 | 2.10 |
| `FRONT DEF` | 1 | 3.2 |
| `REAR DEF` | 1 | 3.3 |
| **裸 `DEF`** | **0** | —— |

`MAX DEF`/`MAX DEFROST` 與 `REAR DEF`/`REAR DEFROST` 兩對早已在等價組內。
**`FRONT DEFROST` 是實見的**（2.3 之 `front defrost` ×2），故
`FRONT DEFROST ≡ FRONT DEF` 與前兩對**完全同形**，非推論。已補入等價組。

於是 `FRONT DEF → DEFROST` 由**兩個實測事實之組合**得出，不是手動補列：
(a) 等價 `FRONT DEF ≡ FRONT DEFROST`；(b) `FRONT DEFROST` 之末字 `DEFROST`
單獨出現 15 次。`HIERARCHY_GAPS` 現為空。

**32 §2.1 當時之診斷不完全正確**：我記為「無實見形式拼出 DEFROST」。
實情是**規則跑在正規化之前** —— 證據一直都在，是順序把它藏住了。

### 4.2 組合之效果：新增 0 對，重分類 3 對，另修好一處靜默丟字

`expand()` 之輸出另過一次等價正規化（44 §4 第 2 項）。**今日為 no-op**
（每個泛化詞本已是正規形），仍寫入 —— 兩張表各自維護，
哪天泛化詞多了一個變體，沒有這一行不會有任何東西出聲。

| | 前 | 後 |
|---|---|---|
| `vocab` | 1591 | **1588** |
| `via-hierarchy` | 77 | **80** |
| 合計 | 1668 | **1668** |

**新增 0 對、遺失 0 對、重分類 3 對**（`2.3 ↔ 16.15`／`2.3 ↔ 2.15`／
`2.3 ↔ 2.9`，由 `vocab` 轉 `via-hierarchy`）。

真正的收穫不在對數，在**一處靜默丟字**：`VOCAB` 之交替順序使
`\bFRONT DEF\b` 在 `front defrost` 上不成立（`def` 後無詞界），
於是 **2.3 之兩處 `front defrost` 一直被當成裸 `DEFROST`，`FRONT` 被丟掉**。
現在 `2.3` 之詞彙集正確含 `FRONT DEF`，而 `DEFROST` 由階層補回。
**對數不變，token 變對了** —— 兩者不是同一件事。

---

## 5. 三對 sibling 之 `distinguishing_axis`

`2.12 ↔ 3.1`／`2.12.1 ↔ 3.1`／`2.12.2 ↔ 3.1` 之措辭已更新，
逐對具名新軸與**兩側各自之取值**：

| 對 | 軸 | 左側值 | 右側值 |
|---|---|---|---|
| `2.12 ↔ 3.1` | 第三軸「前排氣流模式集合」| **4 模式**（C13）| **tri-mode 7 組合**（C19）|
| `2.12.1 ↔ 3.1` | 同上 | **5 狀態**（C13.0）| 同上 |
| `2.12.2 ↔ 3.1` | 同上 | **4 模式**（C13.1 之循環序即 C13 之集合）| 同上（C19 之七組合循環序）|

舊措辭「第三軸 tri-mode 有無」**陳述了一個已不存在的結構**，依 R-C19 更新；
`2.12 ↔ 3.1` 之新文內保留一句引述舊措辭並說明其為何不成立，
以免日後有人以為那只是換了個名字。

`distinguishing_axis` 之 JSON 欄位仍待 `Airstream and Defrost` 生成時
依 §4.6 回填（36 §4），本輪更新的是判定台帳之措辭。

---

## 6. 五軸窮盡實測

44 §6 寫「其餘四軸」，而 `axis-values` 現有**五**塊（13／EMEA／9／2／10）。
**五塊全做**，各以與第三軸同等強度之全 129 節掃描。

### 6.1 結果 —— 未見任何未列之值

| axis | pattern | 命中句 | 結論 |
|---|---|---|---|
| 13 | `knob\|physical control\|hard control type\|push button\|rocker\|toggle\|ICS\b` | 15 | 三值互斥，**以 `other` 收尾** |
| EMEA | `EMEA\|LATAM\|market\|ICS\b\|region` | 5 | **無一句字面出現 `EMEA`**；值名源自 16.1 之適用性判讀（R-C15／A-CF08），非條文字面 |
| 9 | `lower screen\|secondary screen\|stowed\|stowable\|foldable\|second screen` | 6 | 13.3.1 之 `stowed/retracted` 仍屬既有第二值；未見第四值 |
| 2 | `single zone\|dual zone\|4 Zone\|four zone\|tri zone\|zone climate\|zones` | 10 | 逐句判讀：2.11／16.11 = single、2.6／2.3.1／14.14／17.5 = dual、7.10×2 = 4 zone；11.6／11.7 之 `seat zones` 為**座椅分區非氣候分區**（同形異義，不計）。**列舉窮盡** |
| 10 | `rear defrost\|REAR DEF\b\|defrost button\|not present` | 18 | 唯一陳述配置者為 3.4；**二值為邏輯窮盡** |

每塊已增 `scan:` 欄，載明日期、pattern 與判讀結果；
`value-count` 之語意由「已知之值數」改為
**「經 129 節掃描未見第 N+1 個值」**。

### 6.2 `verify_axis_gate.py` 增兩項斷言

每塊必須有 `scan:`（無者其 value-count 未經證明），且 `scan:` 必須**載明是哪一類窮盡**。
第二項在寫的時候就抓到一次：軸 9 原本只寫「以 `other` 收尾」而未寫 `catch-all`，
斷言變紅，補字後轉綠。

### 6.3 一項機制上限，必須記下來

**值列以 `other` 收尾的軸，其窮盡是由構造保證的**，於是

> `value-count` 永遠不會合法增加，
> 該 gate 對這類軸**只能偵測「有人改了清單」，偵測不到「清單本來就漏了一個值」**。

五軸中**只有軸 2 與軸 10 之 value-count 檢查是活的**（軸 2 為列舉窮盡，
軸 10 為邏輯窮盡）；軸 13／EMEA／9 有 catch-all。這不是缺陷，是該檢查在
此類軸上的能力上限 —— **記之，以免把它的綠燈讀成比實際更強的保證**。
已寫入 profile 之 `AXIS-VALUES` 標頭。

### 6.4 掃描順帶查出一條未登記之配置軸

`14.12`：「If the hard controls are **knobs that turn** then the HVAC popups
should be **radial** popups. If the hard controls are **UP/DOWN toggles** then
the HVAC popups should be **vertical** popups…」

這是**硬體控制之輸入型態**，與軸 13（是否為 3 旋鈕 ICS／是否顯示 HVAC 畫面）
**不是同一個問題**：一台 3 旋鈕 ICS 車同時也是「knobs that turn」，兩者非互斥，
故**不是軸 13 的第四個值，而是一條 profile §3.2 十五軸中沒有的新軸**。

它決定 popup 之形狀，**影響 `Climate Popups`（42 leaf）之生成**。
**未自行增列**（增軸屬 profile 變更）—— 回報待裁。

---

## 7. DR #34 —— `controls screen` 之入口

已開（Medium，不阻塞）。實測：全 129 節 pattern `controls screen`
**僅 1 命中，即 `16.16` 自身**。

**照錄條文用語為正確處置（R-C33），未追問則為未竟** —— 而其後果具體：
`-094`～`-097` 之第一步為「Open the controls screen」，
**該步驟無法執行到底**，測試員不知從哪裡開。
補入口需先知道入口，自行指定即造值（§8.4.1）。**TC 內容不動。**

---

## 8. 批次 7 —— `ICS Temperature and Fan`

### 8.1 Layer 3 為**四節**，不是三節 —— 與批次 6 同型，第二次

44 §8 之表列「16.6、16.6.1、16.7」而 leaf 數列 **17**。三節實為 16 leaf。
`framework.md` 第 51 行列 **`16.6, 16.6.1, 16.7, 16.17`，17 leaves**
（`16.17` 由 14 §1 之修正案配對 `2.16`）。037 實測：110(6)＋111(5)＋112(5)＋
123(1) = **17**。依 framework.md 生成四節。

> **兩包連續同一形態**（32 §7.1 為批次 6）：下放包之表列少一節，
> 而其 leaf 數是**含該節**的數。兩個數字不相容時，
> 44 §8 自己寫的「自 framework.md 導出」即是解法 —— 已依之。
> 建議下放包之批次表改為**只列 leaf 數並指向 framework.md**，
> 或於列出節次時附各節 leaf 數，使不相容當場可見。

### 8.2 產出

| leaf | 節 | TC | tc_id |
|---|---|---|---|
| `SWE1-HVAC-110` | 16.6 | 6 | `-098`…`-103` |
| `SWE1-HVAC-111` | 16.6.1 | 5 | `-104`…`-108` |
| `SWE1-HVAC-112` | 16.7 | 5 | `-109`…`-113` |
| `SWE1-HVAC-123` | 16.17 | 1 | `-114` |
| **合計** | | **17** | 無停下項 |

### 8.3 鏡射表反向使用 —— 三處不移植

| 對 | ch2 有而 ch16 無 | 處置 |
|---|---|---|
| `16.6 ↔ 2.6` | C5 之「This status is relayed from the CCM」| 不移植 |
| `16.6 ↔ 2.6` | C5 記 Metric 切換者為 **the readout**，ICE5 記為 **the CCM** —— 主詞不同 | 依 ICE5 措辭，ER 停在可觀察量（畫面所示增量），不驗 CCM 內部行為 |
| **`16.7 ↔ 2.7`** | **C6 有 `15h`，ICE6 沒有** —— ICE6 為「Off, 1-7 (denoting to show AUTO **label** instead **when in AUTO**)」| `15h` 為 CAN 值，**不得移植**；`-109` 之 ER 述 AUTO 標示而不述 15h |

另記一項條文品質觀察：**ICE5.1 把滑桿把手規則寫了兩次**
（`User must press slider handle…` 與 `The user can also press slider handle…`，
後者多一個括號說明）。037 只給一個 leaf，故一葉一 TC，**不因條文重複而拆**。

### 8.4 R-C36-1 之 TC 對 TC 驗證 —— 本批全面適用，19/19 成立

44 §8 預告本批之對造皆已生成。實測 `emea_ics_per_tc.tsv` 指向
`16.6`／`16.6.1`／`16.7`／`16.17` 者共 **19 筆**，逐一對照：

| ch2 TC | verdict | ch16 對應 | 結果 |
|---|---|---|---|
| `-048`／`-049`／`-050`／`-051`／`-052` | yes | `-098`～`-102` | 五筆全中 |
| `-053`…`-058` | yes | `-104`～`-108` | 六筆全中 |
| `-059`／`-060`／`-061`／`-062`／`-063` | yes | `-110`／`-111`／`-112`／`-113` | 五筆全中 |
| `-064` | yes | `-114` | 中 |
| **`-065`** | **no** | —— | **成立** —— 16.17 僅一句，不含 C18 第二句「After blower reduction, return blower speed to previous speed…」，批次 7 未產對應 TC |
| **`-066`** | **no** | —— | **成立** —— ICE6 只列 `Off, 1-7`，`-109` 之 ER 亦只述 1 至 7 |

**19/19 相符。連同批次 6 之 14 筆，R-C36-1 之逐條判定已有 33 筆以 TC 對 TC
驗證，33/33 成立。**

### 8.5 39 列 provisional 重新確認

批次 7 使四節落地，39 列到期（19 `not-sibling`／13 類級／**7 `deferred`**）。
全部逐對判完，**verdict 全為 `not-sibling`**。其中 7 列 `deferred` 為
**ch16 內部之跨組對**（`16.2 ↔ 16.6`／`16.6.1`／`16.7`／`16.17`、
`16.6`／`16.6.1`／`16.7 ↔ 16.14`）—— 兩節同屬 ch16 而分屬不同 Test Set，
今兩側皆有 TC，逐條比對其 `expected_result` 無共用可觀察量。

`provisional` 現 `false` **123** 列／`true` 1545 列。

### 8.6 生成時查出並修好兩處批次 6 之缺陷

| 缺陷 | 成因 | 處置 |
|---|---|---|
| 批次 6 之 PC 第一行**沒有編號**（`[spec-derived] …` 而非 `1. [spec-derived] …`）| `PC_EMEA` 常數漏了 `1. ` 前綴；`source-class` gate 只檢查每行有無 source class，不檢查編號 | 已修，批次 6 重生成 |
| 批次 6 之 `16.14`／`16.16` 之 `specification_reference` **不含 16.2**，而其 PC 引用 (16.2) | R-C29 要求出處節一併列入 spec_ref；批次 6 之 `refs` 未加 | 已修，批次 6 重生成；批次 7 一律加 |

第一項值得記：**它通過了每一道 gate**。`source-class` 問「有沒有標來源」，
沒有人問「編號是否從 1 開始且連續」。它是在寫批次 7、把兩批的 PC 並排看時
才顯出來的 —— **並排比對是 gate 之外的另一種檢查，不能被 gate 取代**。

---

## 9. 第二次寫回 —— **已產出，3 項 FAIL，不可交付**

### 9.1 前置 gate 5 項全 PASS

```
- PASS — BASELINE.sha256 8 檔全數 OK — OK=8, FAILED=0
- PASS — DELIVERY.sha256 --ignore-missing 全數 OK — OK=6, FAILED=0
- PASS — 台帳尚無 ENTRY 004（一次性 gate） — absent
- PASS — 來源為 A-CF07 經 Pei 確認之同一份位元組 — b68117a211b08009…
- PASS — lint 全數 PASS — 42 / 42 gates PASS; 0 finding(s) across 114 TCs
- PASS — TC 數實測且 tc_id 連續無缺號 — measured 114 TCs, tc_id 001–114
```

TC 數**實測不預填**（45 §2），並另斷言 tc_id 連續無缺號。

### 9.2 編號為 **ENTRY 004**，非下放包所寫之 ENTRY 003

**003 已由 27 §3 之交付夾附件佔用**（`type: folder-attachment`）。
append-only 台帳之編號若重複，它就不再是索引。以次一可用號記之。
`ENTRY 002` 之狀態欄增記 `superseded by ENTRY 004`，pilot 檔保留不刪。

### 9.3 assertion 13 項：10 PASS、**3 FAIL**

**PASS 者**：zip member 數、差異僅限目標 sheet、DV counts、
114 列 × 14 欄逐格與 JSON 一致、Q 與 T–Z 留白、S 欄一律 NA、
**三類 marker 之 Remarks 規則**（新，45 §3.3 第 11 項）、
**N 欄逐字元與 JSON 相同**（新，第 10 項之內容側）、
row 124 起無殘留、**已寫入列數 == TC 數**（新，第 12 項）。

**A-CF19 之實測（第 10 項之呈現側，以 MEASURED 行輸出而非 assertion）**：

```
N 欄最長 430 字元（NR1L-ComfortHMI-105）；欄寬 15.5；wrapText=True；
列高 14.0 → 可見約 1 行 ≈ 15 字元，即最長者之 3%。
```

**內容完整而僅首行可見。** 兩個問題分開問：內容完不完整（可判，PASS）、
看不看得見（是個數字，不是 pass/fail）。呈現屬 Tier 3，程式不得自行改列高。

**FAIL 三項 —— 同一個成因：範本只有 50 列**

實測 `inputs/…_SWQT_20260121.xlsx` 與 prepared 檔（兩者相同）：
資料工作表 `max_row=59`，可用列為 **row 10–59 共 50 列**。本次寫入 114 列。

| 項 | 範本涵蓋 | 後果 |
|---|---|---|
| B 欄編號公式 | row 10–59 | **row 60–123 無列號**（64 列）|
| R 欄 x14 下拉（設計方法）| sqref `R10` ＋ `R11:R59` | **64 列無下拉** —— profile §0.1 確認項 2「R 欄下拉可用且為九項」於該 64 列為假 |
| P 欄 DV（優先級）| sqref **`P10:Q11`** | **112 列無下拉** |

**P 欄那一項最值得記**：它**在 ENTRY 002 之 pilot 就已經存在**
（row 12–23 共 12 列無 P 下拉），而當時之 assertion **完全沒有檢查 DV 涵蓋**，
所以九項全 PASS、Pei 於 Excel 確認四項亦通過 —— 確認項只問「R 欄下拉可用」，
而 R10 恰好在範圍內。

> **一個檢查沒問的問題，不會因為別的檢查通過而變成已答。**

已補為 **assertion 13**：每一寫入列皆須落在 R 欄與 P 欄之 DV sqref 內。
它現在會紅，且**應該紅到範本擴充為止**。

（過程中另修一處：我最初以 regex 掃 XML 找 B 欄公式，只找到 row 10 ——
因為 openpyxl 序列化為 **shared formula**，非 master 之列不帶 `<f>` 文字。
已刪除該重複檢查，改由既有之 openpyxl 檢查負責，並於註解記其成因。）

### 9.4 處置 —— 不送 Pei 確認，登 DR #35

45 §3.4 之「產出後停下等 Pei 確認」**本輪不執行**：
送一份已知 64 列無下拉、112 列無優先級下拉、64 列無列號的檔去做四項確認，
是把一個已知的失敗交給人再發現一次。

`DELIVERY.sha256` 之 **ENTRY 004** 已追加，狀態欄逐項載明三個 FAIL 與其成因，
並註明**不可交付**。產出檔保留於 `output/`（台帳記的是產出過什麼）。

**擴充範本屬結構性變更，執行層不自取** —— 下拉 sqref 延伸、編號公式與樣式
往下複製，比照 **R23-4** 須先裁決並經 Pei 於 Excel 確認；且 A-CF07 之四項
確認即以現行結構為對象，自行延伸等於使該確認失去對象。**已登 DR #35（High）。**

**未做**：不複製至客戶交付路徑；prepared 檔未動；ENTRY 001／002／003 之
hash 與內容未變動；pilot 檔未刪；git 未執行。

---

## 10. lint 與 §9 自評

```
42 / 42 gates PASS; 0 finding(s) across 114 TCs
```

TC 97 → **114**；leaf 92 → **109**；已生成節 33 → **37**。
`pending_sibling.tsv` 1668 列不變（`vocab` 1588／`via-hierarchy` 80），
重建冪等。

**§9 十七項**：本輪新增 17 條（批次 7）＋ 重生成 16 條（批次 6，PC 編號與
spec_ref 修正，內容未變）。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 1 | Test Set | 變 | `ICS Temperature and Fan`，取自 framework.md 第 13 組 |
| 2 | tc_title | 變 | 17 條皆 2–14 字、無 modal |
| 3 | Pre-Condition | 變 | EMEA 正向軸值（16.2）＋ 軸 13（2.14，17 條）＋ 軸 9（6.3，14 條）＋ 軸 2（16.11，3 條）＋ ATC 值（16.6，`-099`）|
| 4 | Input Test Data | 變 | 全數 `NA` |
| 5–8 | 步驟 | 變 | 每條 2–4 步，末步持驗證；無禁用動詞 |
| 9 | Baseline | 變 | `-100`／`-110`／`-114` 需前後對照，首步建立基線 |
| 10 | Procedure ↔ ER 1:1 | 變 | 17 條全數 1:1，ER 無 modal |
| 11 | FP／FF | 變 | `-103`（無 popup）、`-108`（不移動）、`-113`（不可關閉）、`-114`（不顯示）四條為否定式，各配正向步驟 |
| 12 | 溯源、§8.2.1、§8.4 | 變 | 17 leaf 各溯其 037 req_id；§8.2.1 之三處不移植見 §8.3；`voice command` 照錄於 test_item 而不入 procedure（觸發方式未定義，§8.4.1）|
| 13 | Design Method | 變 | 15 條功能測試、`-098`／`-109` 邊界值分析。**首版之字串少了 `, BVA` 而被 `design-method` gate 擋下** —— profile §3.3 要求與 `下拉選單!A1:A9` 逐字元相符 |
| 14／15 | §11 格式 | 變 | 無行尾句點；UI 標籤用 `"…"` |
| 16 | `specification_reference` | 變 | 各條含自身節次 ＋ 16.2（EMEA PC 出處，R-C29）＋ 2.14 ＋ 6.3／16.11（適用者）|
| 17 | §8.6／§8.7 | 變 | `60-84`／`16-28`／`1-7`／`3 sec` 皆條文明值；**`15h` 與 `Off, 1-8` 刻意未取**（ch16 無之）|

---

## 11. 「本包是否仍有該驗而未驗者」（R-C30）

1. **批次 7 之 17 條未經 §7 之 FP／FF 人工複核**，只經 lint。
2. **`-098` 之「Adjust the temperature across its whole range」不是一個可數的步驟** ——
   邊界值分析之實作細節（要按幾次、如何確認到頂）留給測試員。
   條文給的是值域，不是操作次數；我未追問這是否足夠。
3. **`-114` 之「Start a Voice Recognition session」無入口步驟**，與 DR #34 之
   `controls screen` **同型**（照錄條文用語而未追問入口）。**未開 DR** ——
   兩者是否應合為一項「條文以名詞指稱畫面／功能而未定義其入口」之通案，待裁。
4. **`14.12` 之新軸未登記**（§6.4），`Climate Popups` 生成前須有結論。
5. **範本容量（DR #35）未解前，所有寫回產物皆不可交付**，包含日後各批。
6. **assertion 13 只檢查 R 與 P 兩欄之 DV**；T–Z 與 AF 之 DV 同樣只到 row 11，
   但該六欄留白，故未列入斷言 —— **若日後有欄改為須填，此處會是下一個
   同型缺口**。已記於此，未實作。
7. **`[COVERED-BY]` 之 lint 具名回報行已就位但從未有列**（0 列），
   故其輸出格式未經實測。

---

## 12. 建議 commit message（git 未執行）

```
feat(comfort): batch 7 ICS Temp/Fan; R-C39, axis scans, second write-back

- R-C39 [COVERED-BY] pasted; profile §5.3 gains a fourth exit. The first
  three markers all mean "not covered by this deliverable"; this one means
  "covered, on another row"
- 122-02 re-checked against R-C39's five conditions: condition TWO fails
  ("Climate section" names no section; the two seat-icon candidates are
  ungenerated), so it stays stopped, recorded `deferred`, per R-C39's own
  text. DR #32 notes condition three will likely fail too
- compose hierarchy with the equivalence groups. FRONT DEFROST is attested
  (2.3, x2), so FRONT DEF -> DEFROST falls out of two measured facts. 32
  §2.1 blamed missing evidence; the real cause was rule-before-normalise.
  0 new pairs, 3 reclassified — and 2.3 stops silently dropping the FRONT
- exhaustive scans for all five axis blocks, each recorded as a `scan:`
  line. No missing value anywhere. But three axes end in `other`, so their
  value-count can never legitimately rise and the gate is inert on them —
  recorded, so its green is not read as more than it is
- 14.12 turns out to be an unregistered axis (turning knobs -> radial
  popups, UP/DOWN toggles -> vertical). Not added; it affects Climate Popups
- batch 7: 17 TCs, -098..-114. framework.md gives FOUR sections; the handoff
  listed three — same shape as batch 6, second package running
- R-C36-1 verified TC-against-TC for all 19 pointers; 33/33 across both
  ICS batches. Fixed two batch-6 defects found by putting the two batches
  side by side: an unnumbered first PC line, and 16.2 missing from spec_ref
- second write-back: 114 rows, 10 assertions pass, 3 FAIL. The template is
  a 50-row scaffold — B numbering to row 59, R dropdown to row 59, and P
  dropdown to row ELEVEN, which has been wrong since the pilot and was
  never checked. New assertion 13 makes it audible. Not delivered, not sent
  for Excel confirmation; DELIVERY ENTRY 004 (003 was taken) records why
- lint 42/42 PASS across 114 TCs
```

---

## 13. 待分析層

1. **DR #35（High）** —— 範本擴充：由 Pei 於 Excel 擴至 403 列以上另立 ENTRY，
   抑或由本 pipeline 以 `xlsx_surgical.py` 延伸而另立確認程序。
   **在此之前寫回產物皆不可交付。**
2. **§6.4** —— `14.12` 之硬控輸入型態是否登記為第十六軸。
3. **§11 第 3 點** —— 「條文以名詞指稱畫面／功能而未定義入口」是否立為通案
   （現有 `controls screen` 與 `Voice Recognition session` 兩例）。
4. **§8.1** —— 下放包批次表之節次與 leaf 數不相容，已連續兩包；
   建議改列各節 leaf 數使其當場可見。
5. **§2** —— `122-02` 於 `12.3`／`14.16.1` 生成後若第三項仍不成立，
   即轉 coverage gap；是否預先裁定其處置。
6. **批次 8 之授權。**
