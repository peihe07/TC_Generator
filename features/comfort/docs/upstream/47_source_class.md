# 47 — Comfort HMI / source class 之名實、字元差集掃描

- 產出層：執行層｜2026-08-16｜對象：分析層
- 承接：下放包 69
- 結果：四項全數落實。`[spec-verbatim]` 之 PC 行由 **155 減為 21**
  —— 非逐字者改標 `spec-derived`（內容未動），**R-C42 之 6 條改文字而非標籤**。
  `source-class-truthful` gate 成立，**逐行**檢查，兩向反向驗證。
  `-361` 之 `test_item` 已改為 `12'`。字元掃描改為以節之實際字元集為基準之
  差集比對，**不再手列對照表**。
  **另修一處自行發現之缺陷並自加一道 gate（§2.2，須報備）**：
  五條 TC 之 pre_conditions 第 2 行無行號而第 3–5 行有。
  lint **54/54 PASS，383 條**。ENTRY 018 已產出。

---

## 0. 下放包四項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | 非逐字之 `spec-verbatim` 改標 `spec-derived`；R-C42 之 21 條若有不合者改文字 | ✅ §1 |
| 2 | 加 `source-class-truthful` gate，逐行檢查，反向驗證 | ✅ §2 |
| 3 | 改 `-361` 之 `test_item` 字元為 `12'` | ✅ §3 |
| 4 | 字元掃描改為以節之實際字元集為基準之差集比對 | ✅ §4 |
| — | 上繳 47 | 本件 |

---

## 1. source class 之訂正

### 1.1 全 corpus 之前後對照（方法 `[machine]`）

| source class | 改前 | 改後 |
|---|---|---|
| `spec-verbatim` | **155 行** | **21 行**（全部為 R-C42 解封之條件式 PC）|
| `spec-derived` | 1212 | **1346** |
| `test-setup` | 99 | 99 |

**判準**：空白正規化後，該行所引之片段須為其所標出處節 `full_text` 之
**連續子字串**。改前 155 行中僅 5 行通過。

**改的是標籤，不是內容**：這 134 行之明文對應皆真實存在（R-C28 第一問通過），
其所述之車輛狀態亦未改一字。改的是**那一行對其出處所作之主張**。

### 1.2 R-C42 之六條 —— **改文字，不改標籤**

R-C42 一明文要求逐字，故此六條之處置與其餘全部相反：

| 節 | 改前（改述）| 改後（條文原句）|
|---|---|---|
| 2.3.1 | The vehicle has dual zone climate with dual airflow mode and a configuration for dual AUTO modes, one for… | **Some vehicles with dual zone climate with dual airflow mode can have a configuration for dual AUTO modes** |
| 2.5.1 | The vehicle has a configuration for a 3 state toggle recirc button: … | **Some vehicles have a configuration for a 3 state toggle recirc button: Auto, Manual, Open** |
| 9.1 | The vehicle is one of the vehicles that have additional Rear Climate controls and shortcuts | **On some vehicles (See CFTS043 for details), there are additional Rear Climate controls and shortcuts** |
| 14.14 | The vehicle has a dual zone climate version with dual airflow modes on an 8.4"… or 12.3" radio | **For vehicles with dual zone climate versions with dual airflow modes on 8.4", 10.1" Landscape, 10.25" and 12.3" radios** |
| 17.4 | The vehicle has an 8.4/10.1/12 landscaped screen | **For 8.4/10.1/12 landscaped screens** |
| 17.5 | The vehicle is a dual zone climate with dual airflow modes equipped vehicle | **For dual zone climate with dual airflow modes equipped vehicles** |

改後 21 行全部通過連續子字串檢查。
`14.12` 之三條與 `17.2`／`17.3` 之二條原本即逐字，未動。

> **同一項發現，兩種相反的處置** —— 其分野是「逐字」在該處是不是規則本身：
> 在 R-C42 之下逐字是規則，故改文字；在其餘各處逐字只是我加給自己的形容詞，
> 故改形容詞。

---

## 2. `source-class-truthful` gate

### 2.1 判準與其範圍

逐行檢查（69 §1.3）：標 `[spec-verbatim]` 者，其片段須為所標出處節之
連續子字串（空白正規化）；`spec-derived`／`test-setup` 不受此檢查。

**與 68 §4 之「不立 gate」不衝突**：該處所拒者為「PC 須逐字」之**義務**；
此處所立者為「標籤須為真」之**真值檢查**。**作者仍得自由改述，
只是改述之後不得自稱逐字。**

**反向驗證（實跑 mutation，兩向）**：

| 向 | 作法 | 結果 |
|---|---|---|
| 首行 | 把 `14.12` 之 `knobs that turn` 改為 `knobs that rotate` | **FAIL**：`line labelled [spec-verbatim] is not a contiguous quotation of 14.12 — 'If the hard controls are knobs that rotate'` |
| **非首行** | 把 `gen_batch14.py` 之 `PC_MULTIZONE`（出現在第 2 行）改標 `spec-verbatim` | **FAIL ×4** —— 若只檢查首行，此四條永不受檢 |

### 2.2 **一處自行發現之缺陷與自加之 gate（須報備）**

上述非首行 mutation 之 FAIL 訊息裡，片段竟仍帶著 `[spec-verbatim]` 前綴。
追下去發現的不是 gate 的問題：

> **`-280`／`-283`／`-293`～`-295` 五條之 pre_conditions，第 2 行沒有行號，
> 而第 3、4、5 行有。**

成因：`gen_batch14.py` 把 `LEAF_EXTRA` 之額外一行以手工 `join` 接上，
未經 `add_lines`，故其後之行從 3 開始編號。**兩端看起來都對，中間是錯的。**

處置：（一）改該生成器，額外行改由 `add_lines` 產生；
（二）**自加 gate `pc-line-numbering`**：pre_conditions 之非空行須編號 1..n。

**這是指示之外自加的第二道 gate**（前次為 66 §4.2 之 Remarks 限制）。
其理由：該缺陷是我在讀另一道 gate 的錯誤訊息時撞見的，
**若無人再讀那則訊息，它可以一直存在** —— 而它出現在客戶會逐行讀的欄位裡。
請裁是否保留。

---

## 3. `-361` 之 `test_item`

`12"` → `12'`（依 `17.2` 之條文）。該條之 PC 已於 67 §2 逐字化，
**自此同一條 TC 內同一識別符只有一種寫法**。

---

## 4. 字元掃描改為差集比對（69 §3.1）

不再手列對照表。對每條 TC：取**其所屬節 `full_text`** 之排版類／非 ASCII
字元集合，與**該條各欄位**之同類集合比對，回報兩側差集。

### 4.1 結果

| 方向 | 筆數 | 讀法 |
|---|---|---|
| **節有而 TC 無**（可能漏錄）| 97 | 多為該節某一句之字元而本條未引該句 |
| **TC 有而節無** | 326 | 其中 **18 筆與該節之某字元同類**（可能為代用）|

**「同類」之判定亦為導出而非列舉**：以字元之類別（guillemet／curly quote／
straight quote／prime／dash／hyphen／degree…）相同或跨類可代用者為準。

### 4.2 18 筆代用嫌疑之判讀（`[manual]`）

全部為 **ER 引用按鍵名之慣例**：本層以 `"REAR DEFROST"` 之形式標示按鍵，
而該節之文字裡恰好有一個 `’`（如 `16.8` 之 `doesn’t break MAX DEF`）或 `'`。
**兩者無關** —— 差集只說「這個字元在節裡沒有」，不說「它是誤用」。

> **差是候選，不是缺陷。** 68 §4.5 之六對是我想得到的形態，
> 其「命中為零」只代表那六種沒有；本法之涵蓋範圍隨語料長，
> 代價是誤報變多，**而誤報看得見、漏報看不見**。

### 4.3 97 筆漏錄中值得一看者

| 節 | 字元 | 條數 | 判讀 |
|---|---|---|---|
| `16.10`／`2.10` | `°` | 8／6 | 該節述溫度顯示含度數符號，而本層之 ER 以文字描述（`the temperature is displayed`），**未逐字引該符號** —— 屬設計，非缺陷 |
| `16.8` | `’` | 12 | `doesn’t break MAX DEF` 之撇號；本層之 ER 改寫為 `does not break` |
| 多節 | `'`／`"` | 多 | 節內之引號屬其他句子 |

**無一筆構成須改之錯**（`-361` 那一筆已於 §3 修掉，且它是**上一輪手列對照表
抓到的**，本法亦能抓到 —— 其形態為「TC 有而節無且同類」）。

---

## 5. lint 與 §9 自評

```
54 / 54 gates PASS; 0 finding(s) across 383 TCs
```

反向驗證六支全 PASS（`verify_b_gates` 21 向）。

TC **383**（不變）；leaf **378 / 403 ＝ 93.8%**（不變）；節 **123**（不變）。

**§9 十七項**：受影響者為 pre_conditions（項 3）與 test_item（項 1）。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 1 | Test Item | 變（1 條）| `-361` 之 `12"` → `12'` |
| 3 | Pre-Condition | 變（134 行改標籤、6 行改文字、5 條修行號）| 標籤之真值（69 §1.2）；R-C42 一之逐字（69 §1.1）；行號 1..n |
| 其餘 | — | 不變 | |

ENTRY 018 已產出（383 列），標「範本容量待擴充」，**不送 Excel 四項確認**。

---

## 6. 「本包是否仍有該驗而未驗者」（R-C30）

1. **`source-class-truthful` 只檢查 `spec-verbatim`** ——
   `spec-derived` 之「確有明文對應」無機器判準，仍為 `[manual]`；
   **一行標成 `spec-derived` 而其實無任何對應，本 gate 不會說話。**
2. **空白正規化之比對容忍換行與多重空白，不容忍標點差異** ——
   若條文為 `Auto, Manual, Open` 而 PC 寫 `Auto/Manual/Open`，會 FAIL；
   該嚴格性是刻意的，但可能在日後產生無謂之 FAIL。
3. **§4 之 `TYPO_CLASS` 仍是一份清單**（雖不再是「對照表」）——
   類別之歸屬由我定；一個不在清單且為 ASCII 之字元（如 `` ` ``）不會被視為排版類。
4. **五條行號缺失是被 FAIL 訊息帶出來的**，不是被任何檢查抓到的；
   **在此之前它已存在了兩輪寫回**（ENTRY 016／017 皆含之）。
5. **§1.2 之六條改文字後，其 PC 讀起來像條文而不像車輛狀態**
   （如 `For 8.4/10.1/12 landscaped screens`）—— 逐字與可讀性在此衝突，
   本輪依 R-C42 一選逐字。

---

## 7. 待分析層

1. **§2.2** —— 自加之 `pc-line-numbering` gate 請裁是否保留。
2. **§6.5** —— R-C42 之條件式 PC 逐字化後讀起來是條文句而非狀態句；
   若日後要兼顧可讀性，可考慮「逐字引句 ＋ 括號內註其對應之車輛狀態」之格式，
   惟該格式須先裁。
3. **§6.1** —— `spec-derived` 之對應真實性目前無檢查，是否值得一道
   「該節 full_text 內須含其關鍵詞」之弱檢查（會有誤報）。
4. **剩餘 25 個停下之 leaf** 分佈不變。
