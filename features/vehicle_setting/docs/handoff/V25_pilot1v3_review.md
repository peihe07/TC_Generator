# V25 — pilot #1 v3 覆核：**有條件通過**。我的字數表是錯的

下放包 **V25**。對應上繳：`docs/upstream/V25_*.md`。
本包新增 **R-VF70／R-VF71**（2 條）、**W-VF63**（1 項工單）。

**本包所據之最新上繳**：`docs/upstream/V24_pilot1v3.md`，實測於 2026-08-24；
另實測 `generated/vf230_pilot1_v3.json`（前 60 行逐字讀，delta 已核）。

---

## 1. 覆核結論：**有條件通過**

**W-VF62(4)（UI 標籤引號）之判定核可** —— 其論證可證偽且證據明確：
Part 1 之 7 個標籤中 **5 個「來源條文未加引號而 Part 1 仍加」**，
故慣例為「逐字螢幕標籤一律加雙引號」而非「隨來源」。
**若為隨來源，那 5 個就不會加。** 本層無異議，且其附記正確 ——
本批僅 seq 247 之條文自身加引號，隨來源之讀法會使 241 與 247 對同一標籤不一致。

**v3 之 delta 已核**：`pre_conditions` 縮為 PROXI 一項、`check that` 已改、
引號插入未誤傷 `test_item`（其為條文逐字，R-VS6）。

**剩餘二項為完全指定之字串取代，無判斷餘地**（§4、§5），
故不再要求回本層覆核 —— **v4 產出後逕入第 2 批**（§6）。

---

## 2. 分析層之錯 —— V24 §4 之字數表有二處誤

執行層 §2.1 之實測正確，本層之表錯：

| seq | V24 §4 所載 | 執行層實測 | 判 |
|---:|---|---:|---|
| 241 | **未列**（歸入「其餘 7 條合規」） | **15** | **本層漏列** |
| 247 | 17 | **18** | **本層少算 1** |

`seq 241` 之切分：`Suspension`／`Service`／`Mode`／`is`／`not`／`displayed`／
`when`／`CAN`／`node`／`27`／`(ASM`／`/`／`ASCM)`／`is`／`"Absent"` = **15**。
**本層當時未逐詞切分，以目視估之。**

**執行層 §6.2 之歸納正確且須記**：

> V24 §2 說 V23 的自檢第 7 項「執行層據以自檢、回報通過，而系統預設原封未動」。
> 這一輪換成分析層的表列漏了一條。**兩次是同一件事：一個沒有被機械執行的量測，
> 其結果不可靠。**

**R-VF69 之拘束及於分析層之量測本身，非僅及於自檢項之措辭。**
本層列舉「違規之逐項清單」時，須以與執行層相同之機械判準產出，
不得以目視估算。**此併入 R-VF71。**

**且其連帶效果已被執行層指出**：241 與 247 為同一 leaf 之 Absent／Present 對，
只縮 247 會使該對之標題形式不一致。**四條一併處理為正確。**

---

## 3. R-VF70 —— tc_title 採純句式；括號別名不入標題

```
R-VF70（VF230 之 tc_title 形式，分析層裁定 2026-08-24）

**一、採純句式，不採情境標籤式，不用冒號。**

依 R-1（格式須窮盡既有已交付範例，不自創）：執行層實測 Part 1 之 225 條
`tc_title`，**無一採 `X: Y = "Z"` 之情境標籤式，全為句式**。
canon §4.3(c) 雖允許標籤式，**專案既有慣例優先**。

v3 §2.3 所提之冒號式（`Suspension Service Mode not displayed: CAN node 27 "Absent"`）
介於兩式之間，**不採**。

**二、括號內之別名不入 tc_title。**

`(ASM / ASCM)`／`(PTGM)`／`(PAM/CVADAS)` 為節點之別名，
其節點號已足以識別。**別名保留於 `test_item`／`test_procedure`／
`expected_result`，僅自 `tc_title` 移除。**

其效果：四條逾字者皆降至 14 字內，**且未逾字之六條亦一併縮短，
使十條之標題形式一致**（形式之一致本身即手足可讀性之一部分）。

**三、正負向之句式固定**：
  負向  `<Setting> is not displayed when <Param> is "<Value>"`
  正向  `<Setting> is displayed and modifiable when <Param> is "<Value>"`

  正向不用 `can be modified`（3 字）而用 `modifiable`（1 字）——
  其語義相同而字數省二。

**手足區辨 token 為分割值本身**（`"Absent"`／`"Present"`／
`"Active Lane Management"`／`"Not Present"`），皆保留於標題內。
```

---

## 4. R-VF71 —— ER 與 procedure 之動詞取自條文；量測須機械執行

```
R-VF71（用詞來源與量測形式，分析層裁定 2026-08-24）

**一、`listed` 與 `displayed` 統一為 `displayed`。**

上繳 §2.2 具名 procedure 用 `listed` 而 ER 用 `displayed`，
並自判二者於選單語境為同一可觀察（本層同意其判斷）。
**惟統一仍有其據**：來源條文逐字為 `shall not display the ... customer setting`
—— **ER 與 procedure 之動詞取自條文，可使 TC 與條文之對應在字面上可見**。

  procedure 3  `Read the Vehicle Settings menu and check that the "X"
                customer setting is not displayed`
  ER 3         `The "X" customer setting is not displayed`

  正向四條同理，`is listed` → `is displayed`。

**二、分析層之量測須機械執行**（承 §2）。

本層於下放包中列舉「違規之逐項清單」「字數」「命中數」等量時，
**須以與執行層相同之機械判準產出並具名該判準**，不得以目視估算。
**R-VF69 之拘束及於量測本身，非僅及於自檢項之措辭。**

**成因**：V24 §4 之字數表漏列 seq 241、seq 247 少算 1，
其成因為本層未逐詞切分而以目視估之。

**三、`PRE_FORBIDDEN` 等列舉須標其性質。**

上繳 §6.1 自承：pattern 清單「是概念的一次列舉，其是否窮盡沒有任何檢查在管」，
「pattern 化把『解讀之不可檢驗』換成『列舉之不完整』——
它是嚴格的改善，但不是消除」。**該自我限制正確且須保留。**

  凡此類列舉，**於其定義處標「已知集合，非全集」**，
  新發現之表述即時補入並具名其發現輪次。
  **機械檢查與人讀互為補位**：pattern 攔已知者，pilot 之人讀補未知者。
  **二者缺一，則列舉之不完整無人發現。**
```

---

## 5. 起始狀態之縫 —— **無須補，canon §8.5 已涵蓋**

上繳 §6.3 具名：刪 `The vehicle is powered and the HU has completed start-up` 後，
十條之起始狀態無任何記載，而步驟 1 為 `Power cycle the HU` —— 自何種狀態？

**本層之判定：不補，且此非縫。**

canon **§8.5** 逐字：「環境穩定性條件…**測試者自然會在執行前確保環境穩定**」，
其決定測試為「該狀態是否為本 TC 直接驗證之觸發條件」。
**車輛之上電狀態非本批任一條之觸發條件**（觸發條件為 PROXI 值），
故其正屬 §8.5 令其略去者。

**且 `Power cycle` 為自足之動作** —— 其於任何已上電狀態皆可執行，
不需前置狀態之特定化。

**執行層之提問正確且值得問**（canon 禁的是寫進 Pre-Condition，非禁止該狀態存在），
**惟其答案為既有條文已涵蓋，不需新規。**

---

## 6. W-VF63 — pilot #1 v4（**兩項字串取代，不再回本層覆核**）

產出 `generated/vf230_pilot1_v4.json`，`supersedes: vf230_pilot1_v3.json`。

### 6.1 tc_title —— 十條全改（依 R-VF70）

| seq | v4 之 tc_title | 字 |
|---:|---|---:|
| 238 | `Power Tailgate Alert is not displayed when CAN node 82 is "Absent"` | 12 |
| 239 | `Blind Spot Alert is not displayed when Blind_Spot_Monitoring is "Absent"` | 11 |
| 240 | `Lane Sense Warning is not displayed when Lane_Assist is "Not Present"` | 11 |
| 241 | `Suspension Service Mode is not displayed when CAN node 27 is "Absent"` | 12 |
| 242 | `Blind Spot with Trailer Detection is not displayed when Blindspot_Trailer_Detection is "Absent"` | 12 |
| 243 | `Park Sense is not displayed when CAN Node 24 is "Absent"` | 11 |
| 244 | `Power Tailgate Alert is displayed and modifiable when CAN node 82 is "Present"` | 13 |
| 245 | `Blind Spot Alert is displayed and modifiable when Blind_Spot_Monitoring is "Present"` | 12 |
| 246 | `Lane Sense Warning is displayed and modifiable when Lane_Assist is "Active Lane Management"` | 13 |
| 247 | `Suspension Service Mode is displayed and modifiable when CAN node 27 is "Present"` | 13 |

**上表之字數為本層以 `len(title.split())` 計得**（R-VF71 二）。
**執行層須以同一判準複驗，不符者以實測為準並回報。**

### 6.2 `listed` → `displayed`（依 R-VF71 一）

十條之 procedure 步驟 3（正向者為步驟 3）之 `is listed`／`is not listed`
改為 `is displayed`／`is not displayed`。**ER 不動**（其已為 `displayed`）。

### 6.3 自檢

沿用 `vf230_selfcheck_wvf62.py`，**增二項**：

```
tc_title 不得含 ":"（R-VF70 一）
tc_title 不得含 "(" 或 ")"（R-VF70 二）
```

於 `PRE_FORBIDDEN`／`VERB_FORBIDDEN` 之定義處加註
**「已知集合，非全集」**（R-VF71 三）。

### 6.4 完成後

**逕行開第 2 批**（10 條，依選池序續取 seq 248–257），
**不待本層再覆核 v4** —— 其修正無判斷餘地。
**惟第 2 批之產出仍須上繳並覆核**（一批一上繳）。

---

## 7. 給 Pei

**pilot #1 之 verdict**：本層建議 **有條件通過** ——
v4 依 §6 之完全指定修正後即為定稿，pilot 階段結束，量產批次開始。

**pilot 之覆蓋面限制不變**（R-VF61）：本批十條同屬「PROXI 值決定設定項有無」
一型，訊號斷言型、狀態轉換型、值域切換型未受檢。
**pilot #2 之分層取樣仍須為之**，其時點建議在第 2–3 批之後、量產全速前。

**待你裁者仍為一項**：DR-34／DR-35 之送出（R-VF27）。

---

## 8. 本包產生之新條文清單（自檢）

| 編號 | 型別 | 區塊 |
|---|---|---|
| R-VF70（tc_title 純句式、無冒號、括號別名不入標題、正負向句式固定） | 分析層裁定 | ✅ §3 |
| R-VF71（`displayed` 統一取自條文；分析層量測須機械執行；列舉須標非全集） | 分析層裁定 | ✅ §4 |

**工單**：W-VF63（pilot #1 v4，兩項字串取代 ＋ 自檢增二項 ＋ 逕開第 2 批）。

**分析層本輪之錯**：V24 §4 之字數表漏列 seq 241、seq 247 少算 1，
成因為目視估算而非機械量測（§2）。

**執行層上繳時須附「本包是否仍有該驗而未驗者」之獨立判斷。**
