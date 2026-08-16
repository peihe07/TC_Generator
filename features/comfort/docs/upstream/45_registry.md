# 45 — Comfort HMI / 登錄簿之性質、PC 逐字化、客戶端可讀性

- 產出層：執行層｜2026-08-16｜對象：分析層
- 承接：下放包 67
- 結果：三項全數落實。`AMBIGUITY_REMARKS` 改為**登錄簿**（列名不需個案裁定），
  gate 雙向對帳並實跑 mutation 驗證；內容三限制改由 gate 檢查。
  `126-02` 與 `125-08` 之首行 PC 改為**逐字引用** —— 前者改後直接命中，
  **其 disposition 區塊已撤**；後者改後仍不命中，**且其原因由「引用不足」
  變為「形態如此」**（§2.2）。兩列 BLOCKED row 之 Remarks 增一短句
  `No test case in this delivery covers those options.`
  lint **52/52 PASS，383 條**。ENTRY 016 已產出（列數不變，三處欄內容差異）。

---

## 0. 下放包三項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | `AMBIGUITY_REMARKS` 改登錄簿，gate 雙向對帳，內容三限制由 gate 檢查 | ✅ §1 |
| 2 | 改寫 `126-02`（及 `125-08` 若同）之首行 PC 為逐字引用，撤 disposition 區塊 | ✅ §2 —— **一撤一留，留者之理由已變** |
| 3 | 確認兩列 BLOCKED row 之 Remarks 使客戶讀出「該選項不由本交付件涵蓋」 | ✅ §3 —— **並發現同一缺口在另外三列上仍在** |
| — | 上繳 45 | 本件 |

---

## 1. `AMBIGUITY_REMARKS` —— 登錄簿

### 1.1 性質已改（profile §3.6 同步改寫）

| | marker 白名單（R-C26）| 本登錄簿（67 §1）|
|---|---|---|
| 作用 | **豁免 lint** | **不豁免任何檢查，只對帳** |
| 增列 | 須裁定 | **作者逕行寫入並同時登錄** |
| 理由 | 放寬須有人負責 | 66 §3 是一般義務；**對義務加審批，其淨效果是那件事不再發生** |

我上一包把它做成了許可證，**而那會讓下一個人在該寫 Remarks 時先去等一個裁定**
—— 66 §3 立的義務會因此變成一件「可以等等再說」的事。已改。

### 1.2 gate 雙向對帳（`ambiguity-register`，第 52 道）

| 向 | 判準 | 44 §7.3 之缺口 |
|---|---|---|
| 有文字而未登錄 | 非 BLOCKED 列之 Remarks 非空且不在登錄簿 → FAIL | 原已有 |
| **已登錄而文字不在** | 登錄簿之片語不出現於該列 Remarks → FAIL | **本輪補上** |

登錄簿由 `set` 改為 `dict`：值為該列 Remarks 必須含有之**片語**
（現為 `cannot be determined from the Comfort HMI`），故「登錄了但文字被改空」
與「文字被改成別的意思」皆會被抓到。

### 1.3 內容三限制，由 gate 檢查

| 限制 | 實作 | 其代理性 |
|---|---|---|
| 無內部 id | `R-C` / `DR #` / `A-CF` / `§` 任一出現即 FAIL | 精確 |
| 足以說明何者不可判定 | 長度 ≥ 40 字元 | **代理** —— 長度不等於清楚 |
| 以執行者所讀之語言 | 非拉丁字元（`ord > 0x2FF`）即 FAIL | **代理** —— 擋得住中文，擋不住英文寫壞 |

**兩項代理已具名**（§5a），其實質仍賴人讀。

### 1.4 反向驗證（實跑 mutation，非斷言）

自 `gen_batch16.py` 之 `LEAF_REMARKS` 移除 `096-01` 後重生成並重跑：

```
[FAIL] ambiguity-register: NR1L-ComfortHMI-374 is registered as carrying a
clause ambiguity, but its Remarks does not contain 'cannot be determined
from the Comfort HMI' — the register would go on asserting an ambiguity the
tester never sees
```

還原後 52/52 PASS。`verify_b_gates.py` 另加四向（登錄簿非空、每列文字仍在、
無內部 id、無未登錄之 Remarks），現 **20 向全 PASS**。

---

## 2. PC 逐字化

### 2.1 `126-02`（17.3）—— 改後直接命中，區塊已撤

| | 改前 | 改後 |
|---|---|---|
| 首行 PC | `The vehicle shows the 50% Comfort widget (17.3)` | **`On the 50% widget, these features are separated between driver and passenger (17.3)`** |
| gate | 不命中（共同字串 ` Comfort widget`，前文 `CW2.) The second`）| **命中**（`On the` 在限定語清單內）|
| disposition 區塊 | 有 | **已撤** |

**分析層之判斷正確且我上一包之理由不成立**：45 §4 已裁寫回為全量重寫，
**每一次寫回都在重寫那一列**，故「改寫會動到已寫回之列」不是成本。
我把一個**每輪都會發生的動作**說成了一個**額外的動作**。

### 2.2 `125-08`（17.2）—— 亦為改述，已改；**仍不命中，惟其原因已變**

| | 改前 | 改後 |
|---|---|---|
| 首行 PC | `The vehicle has a 12" Portrait 50% widget (17.2)` | **`12' Portrait 50% widget also includes fan speed (17.2)`** |
| 與條文之關係 | 改述（且把條文之 `12'` 寫成 `12"`）| **逐字**（含條文自己的撇號形式）|
| gate | 不命中 | **仍不命中** |

> **改前不命中，是因為沒引到帶限定語的那一段；
> 改後仍不命中，是因為那一段前面本來就沒有限定語。**
> 前者是我的問題，後者是條文的形態。

其 disposition 區塊保留，`why` 已改寫記明此分野：**名詞片語界定範圍**，
依 66 §2.2 之判準式定義仍屬條件；其適用性另由 DR #6 管。

**副產物**：改前之 PC 把條文之 `12'`（撇號）寫成 `12"`（雙引號）——
**一個字元之差，而它正是 DR #6 所問之螢幕識別**。逐字化順帶修掉了它。

---

## 3. 兩列 BLOCKED row 之客戶端可讀性

**改前**（僅止於歸屬）：

> `[BLOCKED-SPEC] Owner: HMI Settings List — … this requirement has no
> content verifiable against the Comfort HMI specification alone`

**改後**（末增一短句）：

> … `alone.` **`No test case in this delivery covers those options.`**

`Owner:` 仍在首 60 字元內（R-C27 之 gate 通過）。
依 67 §3 **未加**「本層未讀該文件」之聲明。

### 3.1 同一缺口在另外三列上仍在（**未動，請裁**）

| 列 | marker | 其 Remarks 是否說出「沒有被測」 |
|---|---|---|
| `-382`／`-383` | `[BLOCKED-SPEC]` | ✅ 本輪已補 |
| `-010`（`080-02`）| `[BLOCKED-SPEC]` | ❌ 僅止於 `Owner: HMI Core Logic and Flow requirement N0` |
| `-012`（`081-02`）| `[BLOCKED-SPEC]` | ❌ 僅止於 `Owner: CFTS044` |
| `-081`（`044-02`）| `[BLOCKED-NON-HMI]` | ❌ 說了「非 HMI 可觀察」，未說「因此無測試涵蓋」|

67 §3 之指示範圍為「兩列 BLOCKED row」，故**本輪只改兩列**。
惟客戶讀到的是同一份交付件裡**五列同型而三列少一句** ——
**請裁是否一併補**（若裁准，其改動僅為 Remarks 末句，不動任何其他欄）。

---

## 4. lint 與 §9 自評

```
52 / 52 gates PASS; 0 finding(s) across 383 TCs
```

反向驗證六支全 PASS（`verify_b_gates` 現 20 向）。

TC **383**（不變）；leaf **378 / 403 ＝ 93.8%**（不變）；節 **123**（不變）；
停下 **25**（不變）。**本輪無新增 TC**，改動為三處欄內容與一道新 gate。

**§9 十七項**：受影響者為 4 條。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 3 | Pre-Condition | 變（2 條）| `125-08`／`126-02` 之首行改為逐字引條文，標 `spec-verbatim`，出處不變（R-C42 一）|
| 14 | Remarks | 變（2 條）| 兩列 BLOCKED row 末增 `No test case in this delivery covers those options.`；`Owner:` 仍在首 60 字元內（R-C27）|
| 其餘 | — | 不變 | |

ENTRY 016 已產出（383 列，與 015 差異為三處欄內容），標「範本容量待擴充」，
**不送 Excel 四項確認**。

---

## 5. 「本包是否仍有該驗而未驗者」（R-C30）

1. **§1.3 之兩項限制為代理**：長度 ≥40 擋不住「寫滿 40 字元的廢話」，
   非拉丁字元檢查擋不住「英文寫得讓執行者看不懂」。**實質仍賴人讀。**
2. **登錄簿之片語目前三列相同** —— 若日後兩列之歧義不同而片語相同，
   對帳仍會通過。片語愈通用，對帳愈弱。
3. **`125-08` 之 disposition 是唯一一筆**（§2.2）—— 一筆之樣本使
   `verify_b_gates` 之「miss 路徑被走過」這一向從 ≥2 降為 ≥1；
   **若日後該筆亦消失，該向會變成空集合上之真命題**，屆時須改為
   「有 miss 時必有 disposition」之條件式斷言。
4. **§3.1 之三列未改**，其理由是指示範圍；**客戶看到的不一致是實在的**。
5. **`12'` 與 `12"` 之訂正只發生在被逐字化的那一條** ——
   我未掃描全 corpus 是否還有其他把條文字元寫錯之處。

---

## 6. 待分析層

1. **§3.1** —— `-010`／`-012`／`-081` 三列是否一併補「無測試涵蓋」之短句。
2. **§5.3** —— `verify_b_gates` 之 miss 路徑斷言：現為 `≥1`，
   是否改為條件式（有 miss 才要求 disposition）以免其歸零後失效。
3. **§5.5** —— 是否值得做一次「PC／ER 之引用是否逐字」之全 corpus 掃描
   （現行 `rc42-condition-marker` 只掃 R-C42 解封之 21 條）。
4. **剩餘 25 個停下之 leaf** 之分佈不變：DR #31（9）、DR #17（2）、
   DR #32（3）、DR #16（2）、DR #11（1）、R-C17（3）、後排配備（4）、
   `9.1`（1）。
