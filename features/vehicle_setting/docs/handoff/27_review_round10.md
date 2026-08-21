# 27 下放包 — 10 輪覆核、反向覆蓋之實測、11 輪指令

分析層寫入，2026-08-20。對象：`docs/upstream/08_polarity_and_delegation.md`。

**覆核結論：接受。** §6-5 之自陳（「R-VS15 之母體判準未反向驗證
CFTS044 之條文是否全被 037 涵蓋」）**是本 feature 迄今最重要的一個未驗項**，
分析層已就其實測，結果見 §2 —— **並非全綠。**

---

## 1. 兩項處置先記

### 1.1 §2.4「已回報 ≠ 已登記」—— 立為條文

A-VS33／A-VS34 於 09 輪之上繳 §5 表中已列，而未進 `ANOMALIES.md`。
成因為上繳包之 anomaly 表與 `ANOMALIES.md` 為兩處，只填了前者。

```
R-VS35（分析層裁定 2026-08-20）
上繳包 §5 之 anomaly／DR 表為**當輪之陳述**，
`ANOMALIES.md` 與 `DATA_REQUESTS.md` 為**跨輪之登記簿**。
二者不得互相替代。

每輪上繳前之最後一個動作：以上繳包 §5 之表逐列核對登記簿，
**列出「本輪新增 N 筆，登記簿現有 M 筆」兩數**；
差額非 0 即為未登記，須補後方得上繳。
```

### 1.2 A-VS37（`TRUNCATED_ENUM` 低估 8 倍）

執行層未改判準而登記之，正確（改判準屬新作業）。
**且其自陳 102 為上界**（跳號亦可能是規格保留未用）—— 該界線具名，接受。

**不排作業**：`TRUNCATED_ENUM` 之用途為標記 LID 值域不可信者；
現行 13 筆已涵蓋本 feature 實際取值之 token（`VC_VEH_LINE`）。
**待 framework 階段若有 token 之值域取自跳號列舉，再逐筆確認。**

---

## 2. 反向覆蓋 —— 分析層實測，**37 條在自己的章節內未被 037 涵蓋**

執行層 §6-5 指出：R-VS15 以 037 之 `Categorization` 定母體，
**未反向驗證 CFTS044 之條文是否全被 037 涵蓋**。

分析層實測（掃描條件：CFTS044 原始 docx，條文區塊以
`\d{7}\s*:\s*\[Artifact Type` 為界得 2,030；in-scope 定義為
`Artifact Type` 含 `Subsystem Functional Requirement`
**且** `EE Architecture` 含 `Atlantis High` 或 `All`；
章節以 `word/styles.xml` heading 1–7 樣式階層歸屬）：

### 2.1 全文層級 —— **不是缺口**

| 量 | 值 |
|---|---|
| CFTS044 之 in-scope 條文 | **1,128** |
| 237 leaf 所覆蓋之 reqid | 251 |
| 未被覆蓋 | 998（覆蓋率 11.5%） |

**該 998 不是缺口。** CFTS044 為「Vehicle Controls」全域規格，
含 Hazard Switch、Seat Zone、Rear Camera Softkey、PHEV 充電排程等
本 feature 之四份 037 從未宣稱涵蓋之主題。
依既定原則「**037 之 leaf 母集定義驗證範圍**」，此為設計而非遺漏。

### 2.2 章節層級 —— **這裡才是缺口**

限縮於本 feature 之 237 leaf 實際落點之 **21 個章節**內：

| 量 | 值 |
|---|---|
| 該 21 章節內之 in-scope 條文 | **169** |
| 其中未被任何 037 leaf 覆蓋 | **39** |
| **覆蓋率** | **76.9%** |

缺口逐章（前八）：

| 章節 | 未覆蓋條文數 |
|---|---|
| `1.3.2.1.3` | 6 |
| `1.3.4.2.2` | 6 |
| `1.3.2.1.3.11` | 5 |
| `1.3.2.1.3.1` | 4 |
| `1.3.2.1.3.2` | 4 |
| `1.3.2.1.3.3` | 4 |
| `1.3.2.1.3.4` | 4 |
| `1.3.2.1.3.12.1` | 3 |

**`1.3.2.1.3.1` ～ `.4` 正是 Left/Right Front Heated/Vented Seat 之章節** ——
即**037 在自己宣稱涵蓋的章節內，仍有 in-scope 條文未被任何 leaf 引用**。

### 2.3 這是什麼性質

**尚不確定。** 三種可能，本包不裁：

| 可能 | 意涵 |
|---|---|
| (a) SWE.1 之真遺漏 | 037 漏了該章節內之部分需求 → **RD-1，且母體 237 不完整** |
| (b) 該等條文之 `EE Architecture` 雖含 Atlantis High，但另有屬性（Radio／Market／Model Year）使其不適用本專案 | 我方之 in-scope 判準過寬 |
| (c) 該等條文為 Description 型或被 037 併入他 leaf | 覆蓋存在但不以 1:1 呈現 |

**(b) 之可能性不低**：本包之 in-scope 判準**只看了 `EE Architecture`
與 `Artifact Type` 兩個屬性**，未看 `Radio`／`Market`／`Model Year`／`ECU`。
—— **此即分析層自身之判準不足，與 R-VS34 同型**（以自訂形態掃描而未先確認定義）。

```
W-37（反向覆蓋之歸因，11 輪首項）
對 §2.2 之 39 條逐條判定其屬 (a)／(b)／(c)：

(1) 逐條列出其全部屬性（`Artifact Type`／`State`／`ECU`／`Market`／
    `Model Year`／`Radio`／`EE Architecture`），與**已被覆蓋之 130 條**
    之屬性分布對照 —— 若缺口條文在某屬性上與已覆蓋者系統性不同，
    即為 (b)，且該屬性須加入 in-scope 判準
(2) 逐條讀其正文，判其主題是否落在四個 Test Set 之能力範圍內
(3) 產出 `docs/reports/reverse_coverage.md`，逐條給 (a)／(b)／(c) 與依據

**(a) 類非 0 者為升級條件** —— 其表示 R-VS15 之母體 237 不完整，
須 Pei 裁定是否擴母體或向上游提 RD-1。

**本項不得以「037 沒寫就不理」收尾** —— 該原則之前提是
037 已涵蓋其宣稱之範圍；本實測正在檢驗該前提。
```

---

## 3. §6-1 極性只餵一個下游 —— 補作業

執行層自陳：W-33 重算了差異對與交集內容，
**未重跑 `attribution.py` 之 C1–C5 歸因**，而該歸因之輸入即值集合。

其引 §5a 條 6（字串比對缺陷具傳染性）正確。

```
W-36(1)（11 輪）
以分極性後之 CFTS044 include 集合重跑 `attribution.py`，
列出 C1／C2／C3／C4／C5／待判之**新舊兩組計數**（R-VS32(2)）。
變動者逐項說明成因。
**W-28 之三個反向錨點（DR-8／A-VS23／DR-12）須仍在待判清單。**
```

```
W-36(2)（11 輪）
自 `cfts044_exclude` 欄產出**負向測試候選清單**
`data/negative_test_candidates.tsv`：
  token / excluded_value / reqid / arch_scope / leaf_ids
其為 §7「enumerated supported items → 必配至少一個 unsupported 負向 TC」
之來源。framework 階段需要它。
```

---

## 4. §6-3 —— R-VS7(a) 之委派句精度，**提請 Pei**

W-34(1) 收斂 0 / 174，成因為**資料本身無可收斂之維度**
（27 個相異 Comfort leaf 中，明示側別者 2、明示階數者 1）。

R-VS7(a) 令 reasoning「指名 Comfort 之對應 leaf id」，
而現行資料只支援指名**對應之功能群**（6 或 12 個 id）。

```
待 Pei 裁：R-VS7(a)′（委派句之精度）
現行 R-VS7(a) 令 reasoning 指名 Comfort 之對應 leaf id。
實測其可達精度為 Layer 3（功能群）而非 leaf：
174 個待委派 leaf 各對應 6 或 12 個 Comfort leaf，
且 Comfort 側 27 個相異 leaf 中明示側別者僅 2、明示階數者僅 1。

三種處置：
(a) 委派句改為指名**功能群**（如「加熱方向盤之畫面行為，
    見 Comfort SWE1-HVAC-062/063/065/104/104-08/…」），
    並於 reasoning 註明其為群層級
(b) 維持逐 leaf 指名之要求，於 Comfort 側資料補足前標為未決
(c) 向 Comfort 之作者請求逐 leaf 之側別／階數標註（RD-1）

分析層建議 (a)：其為現行資料所能達到之上限，
且委派句之作用是**指出該行為由誰擁有**，群層級已足以達成；
(b) 會使 174 個 leaf 之 reasoning 全部懸置，(c) 之代價與收益不成比例。
```

---

## 5. 11 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/27_review_round10.md 本輪依據
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入三項上限）

D-1  依 R-VS18 建立 docs/upstream/09_reverse_coverage.md，六節先留空。
D-2  逐字轉錄 27 包 §1.1 之 R-VS35 入 RULINGS.md。
D-3  依 R-VS35，本輪上繳前以 §5 之表逐列核對 ANOMALIES.md 與
     DATA_REQUESTS.md，列出「本輪新增 N／登記簿現有 M」兩數。

## 作業（三項，R-VS25）

W-37  反向覆蓋之歸因（27 包 §2.3 之全文）
      對「21 個章節內、in-scope、未被任何 037 leaf 覆蓋」之 **39 條**
      逐條判定 (a) SWE.1 真遺漏／(b) 我方 in-scope 判準過寬／
      (c) 被併入他 leaf。
      (1) 逐條列全部屬性，與已覆蓋之 130 條之屬性分布對照
      (2) 逐條讀正文，判其主題是否落在四個 Test Set 之能力範圍
      (3) → docs/reports/reverse_coverage.md
      **(a) 類非 0 為升級條件**（母體 237 不完整）。
      **不得以「037 沒寫就不理」收尾** —— 該原則之前提正在被檢驗。
      分析層之實測基數：in-scope 1,128／21 章節內 169／未覆蓋 39／
      覆蓋率 76.9%。**須自行重測並列出與此四數之對照。**

W-36  極性之下游回算
      (1) 以分極性後之 include 集合重跑 attribution.py，
          列 C1–C5 與待判之新舊兩組計數；變動者說明成因。
          W-28 之三錨點須仍在待判。
      (2) 自 cfts044_exclude 產出 data/negative_test_candidates.tsv
          （token / excluded_value / reqid / arch_scope / leaf_ids）

W-38  36 條「未分左右」複核（06 輪 §6-1，已延五輪）
      逐條讀其 Comfort 原文，確認其確未明示側別；
      有明示而先前漏判者具名。

## 禁區

git 寫入性操作一律不執行。需入庫者，準備指令給 Pei（帶 pathspec）。
不補素材、不代擬條文、不自行調和數字。
衍生檔之刪除屬 Pei；.gitignore 之修改屬 Pei。

## 升級條件

W-37 之 (a) 類非 0；
W-36(1) 之三錨點任一落入 C1–C5；
實測與 27 包之四數不符；撞到 §8.4.1 編造壓力；需要判斷而無條文。
本輪無「必停」項。

## 完成後

DR-15 到位且 W-37 結案後，進 framework Part Vehicle Setting ＋ profile。
```

---

## 6. 待 Pei

| # | 事項 |
|---|---|
| **P18** | 裁 **R-VS7(a)′**（委派句之精度，三選項見 §4，分析層建議 (a)） |

（DR-15 之送出與入庫依 R-VS31 不重列。）

---

## 7. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS35 | 上繳包之表與登記簿不得互相替代；上繳前逐列核對並列兩數 | 分析層 |
| R-VS7(a)′ | 委派句之精度（三選項） | **待 Pei** |
| W-36／W-37／W-38 | 作業 | 分析層 |
