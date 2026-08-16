# 46 — Comfort HMI / 五列一致、對帳片語具名化、逐字化之全 corpus 量測

- 產出層：執行層｜2026-08-16｜對象：分析層
- 承接：下放包 68
- 結果：四項全數落實。五列 marker row 之措辭自此一致（`-081` 之句不轉指）。
  登錄簿之值改逐列具名，gate 增「值不得重複」並以 mutation 驗證。
  miss 路徑之斷言改條件式 ＋ **注入式** mutation，**不再依賴語料存在**。
  逐字化全 corpus 量測完成 —— **最重要的結果不是分佈，是標籤**：
  **123 條標 `[spec-verbatim]` 之首行 PC 中，僅 5 條真正逐字，39 條為改述**（§4.3）。
  字元訛誤 **1 處**（`-361` 之 `test_item` 仍寫 `12"`，其 PC 已是 `12'`）。
  lint **52/52 PASS，383 條**。ENTRY 017 已產出。

---

## 0. 下放包四項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | `-010`／`-012`／`-081` 補「無測試涵蓋」短句；`-081` 不得暗示他處在測 | ✅ §1 |
| 2 | 登錄簿之值改逐列具名，gate 增「值不得重複」，反向驗證 | ✅ §2 |
| 3 | miss 路徑斷言改條件式 ＋ mutation | ✅ §3 |
| 4 | 全 corpus 逐字化量測與字元訛誤掃描，回報分佈與最短 20 條，不立 gate | ✅ §4 |
| — | 上繳 46 | 本件 |

---

## 1. 五列 marker row 之措辭一致化

| 列 | marker | 新增之句 |
|---|---|---|
| `-010`（`080-02`）| `[BLOCKED-SPEC]` | `No test case in this delivery covers that logic.` |
| `-012`（`081-02`）| `[BLOCKED-SPEC]` | `No test case in this delivery covers that equivalence.` |
| `-081`（`044-02`）| `[BLOCKED-NON-HMI]` | `No test case in this delivery covers that property.` |
| `-382`／`-383` | `[BLOCKED-SPEC]` | （67 §3 已補）`… covers those options.` |

**`-081` 之措辭**：只說「本交付件不涵蓋」，**不含任何轉指** ——
該 marker 之定義即「無外部擁有者」，若寫成「由他處涵蓋」即與 marker 自相矛盾。
`Owner:` 仍在首 60 字元內（R-C27 之 gate 通過）；三句皆置於末。

> 68 §1 之一句已記下：**範圍窄不是理由**。上一輪我只改兩列，
> 因為指示只提兩列；而客戶讀到的是同一份交付件。

---

## 2. 登錄簿之值改逐列具名

三列之 Remarks 亦隨之改寫（原三列共用同一句）：

| 列 | 該列之歧義（Remarks 之後半）| 登錄簿之對帳片段 |
|---|---|---|
| `-374` | whether **radial** popups apply | `whether radial popups apply` |
| `-375` | whether **vertical** popups apply | `whether vertical popups apply` |
| `-376` | whether the popup style must match **every control or only the predominant control type** | `only the predominant control type` |

gate 增「值不得重複」；**mutation 實跑**（把 `-375` 之值改成與 `-374` 相同）：

```
[FAIL] ambiguity-register: the register reuses the fragment(s)
['whether radial popups apply'] on more than one row — a shared fragment
only checks that the sentence exists, never that it is about this row
```

`verify_b_gates.py` 增一向（值集合無重複），現 **21 向全 PASS**。

---

## 3. miss 路徑之斷言 —— 條件式 ＋ 注入式 mutation

| 項 | 作法 | 是否依賴語料 |
|---|---|---|
| 條件式 | 若存在 miss，則每個 miss 皆有 disposition；無 miss 時空過 | 是（故不足以單獨成立）|
| **注入式** | 以 `2.11` 之無限定語句（`Adjusting Fan speed and Mode will alter the Front and Rear`）**構造**一個 miss，斷言其被偵測為 miss | **否** |

實測：注入之片段與 `2.11` 共有 58 字元，其前文為 `ntrol would break SYNC. ` —— 無限定語，**如期判為 miss**。

> **斷言若只在資料存在時成立，資料消失即等於斷言消失。**
> 注入式那一向現在是這道 gate 唯一不會隨語料歸零而失效的部分。

---

## 4. 全 corpus 逐字化量測（**量測，未立 gate**）

腳本：`scripts/survey_verbatim.py`（可重跑）。量測對象為**每條之首行 PC**
與其**所標出處節之 `full_text`** 之最長共同連續字串（`autojunk=False`，profile §3.7.1）。

### 4.1 分佈（383 條）

| run 長度 | 條數 |
|---|---|
| 0–9 | 41 |
| 10–19 | 197 |
| 20–39 | 101 |
| 40–59 | 21 |
| 60–99 | 23 |
| 100+ | 0 |

### 4.2 依首行 PC 之 source class

| class | n | median run | min | max |
|---|---|---|---|---|
| `spec-derived` | 174 | 10 | 10 | 34 |
| `spec-verbatim` | **123** | 32 | **9** | 99 |
| `test-setup` | 86 | 16 | 2 | 23 |

`test-setup` 之低 run 是**預期的**（其內容本就不出自條文）；
`spec-derived` 亦然（R-C28 第一問要的是明文對應，改述可滿足）。

### 4.3 **本次量測最重要之結果：`[spec-verbatim]` 這個標籤名不副實**

以「首行片段有多少比例落在共同連續字串內」分級（123 條標 `spec-verbatim` 者）：

| 級 | 條數 | 例 |
|---|---|---|
| **完全逐字**（run = 片段全長）| **5** | `126-02`：`On the 50% widget, these features are separated between driver and passenger` |
| 近逐字（≥0.8）| 13 | `065-01`：0.98 |
| 部分（0.4–0.8）| 66 | `042-01`：0.53（`The vehicle is one of the vehicles that have additional Rear Climate controls and shortcuts` vs 條文之 `On some vehicles …, there are additional …`）|
| **改述（<0.4）** | **39** | `097`（14.13）：`The vehicle has a lower HVAC screen`，run 9；`020-01`～`-04`（2.14）：`The climate system is MTC`，run 9 |

> **`spec-verbatim` 之語意是「這句話是條文的原話」。**
> 實測 123 條中只有 5 條真的是；**39 條連四成都不到**。
> 其餘多數是「意思正確之改述」—— 那是 `spec-derived` 之定義，不是 `spec-verbatim`。

**這不是內容錯誤**（其對應皆真實存在，R-C28 第一問滿足），
**是標籤錯誤**：讀者看到 `spec-verbatim` 會以為可以直接把該行當條文引用。

**不逕行改**（68 §4：先量後裁）。可能之處置有三，其成本差異甚大：

| 處置 | 影響 | 成本 |
|---|---|---|
| (甲) 把非逐字者改標 `spec-derived` | 118 條之標籤 | 標籤改動，內容不動 |
| (乙) 把它們改寫成真逐字 | 118 條之 PC 文字 | 大，且部分條文句子不適合直接作 PC（如 `042-01` 之 `On some vehicles …` 需改寫成車輛狀態才可讀）|
| (丙) 放寬 `spec-verbatim` 之定義為「逐字或其忠實改寫」| 定義 | 零成本，惟該標籤自此不再承載可機讀之承諾 |

**本層建議 (甲)**：標籤之價值在於可信；`spec-derived` 已足以表達「有明文對應」。
惟 R-C42 一要求條文自帶條件者**逐字**表述 —— 那 21 條須維持 `spec-verbatim`
且確實逐字（現況：其中 `126-02` 完全逐字、`125-08` 逐字、其餘多為部分）。

### 4.4 最短之 20 條

| req_id | tc_id | 節 | class | run / 片段長 |
|---|---|---|---|---|
| `086-01`／`086-02` | `-169`／`-170` | 14.3 | test-setup | 2 / 48 |
| `005-01`～`005-04` | `-136`…`-139` | 2.4 | test-setup | 4 / 55 |
| `037` | `-301` | 7.9 | test-setup | 4 / 60 |
| `085` | `-168` | 14.2 | test-setup | 4 / 48 |
| `092` | `-178` | 14.9 | test-setup | 4 / 48 |
| `084`／`088`／`089`／`091` | `-167`／`-173`／`-174`／`-177` | 14.1.1／14.5／14.6／14.8 | test-setup | 5 / 48 |
| `012-01`～`012-06` | `-153`…`-158` | 2.8 | test-setup | 6 / 55 |
| `036-01`／`036-02` | `-296`／`-297` | 7.8 | test-setup | 6 / 60 |

**全部 20 條皆為 `test-setup`** —— 即「開啟氣候畫面」這類設定行為，
其文字本就不出自條文。**最短的一批不是問題，`spec-verbatim` 那一批才是。**

### 4.5 字元訛誤掃描

| 對 | spec 端 | corpus 端誤寫 |
|---|---|---|
| `12'` vs `12"` | `17.2` | **1 處：`-361`（`125-08`）之 `test_item` 仍寫 `12"`** |
| `«` `»` | `9.2`／`9.3`／`9.4.1`／`10.9.1`／`11.7` | 0 處（無 `<<`／`>>` 之代用）|
| `’` vs `'` | `16.8`（`doesn’t break MAX DEF`）| 0 處 |
| `“` `”` | 不出現 | — |

**`-361` 之情形值得具名**：其**首行 PC 已於 67 §2 改為 `12'`（逐字）**，
而**同一條之 `test_item` 仍是 `12"`** —— **同一條 TC 內，同一個識別符兩種寫法**。
依 68 §4「其處置另裁」，**本輪不改，僅回報**；改法為一行（`test_item` 之字元）。

**`«»` 之承載**：使用 guillemets 之 5 節共有 10 條 TC，其中 3 條照錄該符號、
7 條未含。**其中多數為正常**（該節之 guillemets 出現在另一 leaf 之句子裡，
本條不涉），惟**未逐條核對**，故此數只是分佈不是缺陷清單。

---

## 5. lint 與 §9 自評

```
52 / 52 gates PASS; 0 finding(s) across 383 TCs
```

反向驗證六支全 PASS（`verify_b_gates` 現 21 向）。

TC **383**（不變）；leaf **378 / 403 ＝ 93.8%**（不變）；節 **123**（不變）。
本輪無新增 TC —— 改動為 **6 列之 Remarks** 與一支量測腳本。

**§9 十七項**：受影響者為 6 條之 Remarks（項 14），其餘不變。

ENTRY 017 已產出（383 列，差異僅 6 列 Remarks），標「範本容量待擴充」，
**不送 Excel 四項確認**。

---

## 6. 「本包是否仍有該驗而未驗者」（R-C30）

1. **§4.3 之分級門檻（1.0／0.8／0.4）是我選的**，無外部依據；
   「5 條完全逐字」不受門檻影響，其餘三級之界線受之。
2. **量測只涵蓋首行 PC** —— 第二行以後之 PC、`test_item`、ER 未量。
   `-361` 之 `12"` 正是落在 `test_item`，**是字元掃描抓到的，不是逐字化量測抓到的**。
3. **字元掃描之對照表是手列的六對** —— 未涵蓋 en dash／em dash、
   不斷行空格等；其命中為零不代表不存在。
4. **`«»` 之 7 條未含者未逐條核對**（§4.5）。
5. **§1 之三句措辭由我擬定** —— `that logic`／`that equivalence`／`that property`
   之受詞選擇未經裁定，惟其形式比照已裁准之 `those options`。

---

## 7. 待分析層

1. **§4.3 —— `spec-verbatim` 之名實不符**：118 條之標籤（或文字）待裁，
   本層建議 (甲) 改標 `spec-derived`，並保留 R-C42 之 21 條為真逐字。
   **此為本輪之主要發現，其餘皆已完成。**
2. **§4.5 —— `-361` 之 `test_item` 之 `12"`**：一行可改，待裁。
3. **§6.2 —— 量測是否擴及 `test_item`／ER**：`-361` 顯示同一條 TC 內可能
   自我不一致，而現行量測看不到。
4. **剩餘 25 個停下之 leaf** 分佈不變。
