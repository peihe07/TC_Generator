# 29 — Comfort HMI / `044-02` 補證、候選分級判定、等價組擴充

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 40
- 結果：`044-02` 五項補證齊備，**結論為與既有兩用例異型**（不建議增列白名單）。
  等價組擴充後候選由 205 增至 **686 對**，分級判定完成；
  **抽樣覆核當場打掉兩個類級判定，並找到兩對真 sibling**。
  A-CF23 登記時**發現原始事實記錯**，已訂正。lint **41/41 PASS，80 條**。

---

## 1. `044-02` 補證五項

### 1.1 Requirement Description 全文（不截斷）

```
SWE1-HVAC-044-02
  TITLE : System Reduces Control System Power Consumption
  DESC  : The system shall reduces climate control system power consumption
  VC    : Precondition: - Vehicle is EV equipped with ECO HVAC / - Ignition ON
          Action: - Activate HVAC controls
          Expected Result: - Reduces climate control system power consumption
  VM    : Manual UI Testing
```

### 1.2 其所屬節之對應句

`10.1`（EH1）全文**僅一句**：

> EH1.) ECO HVAC is an HVAC Mode, used on EV Vehicles only, **to reduce
> Climate control System Power Consumption**.

**該 leaf 對應者為其目的子句 `to reduce …`。**

### 1.3 委派之對象文件與其字面 —— **沒有**

**條文內無任何委派字面。** 10.1 未指名任何外部文件、未寫 `see …`、
未寫 `as per …`、未寫 `refer to …`。

**這一項是本次補證最關鍵者**，因為它使 `044-02` 與既有兩個用例分屬異型
（見 §1.5）。

### 1.4 扣除委派後之餘留分析

**無委派可扣除**，故「餘留」即該 leaf 之全部：`reduces climate control
system power consumption`。

**該餘留是否可於 Comfort 範圍內獨立驗證？**

- **耗電量本身**：HMI 不顯示耗電量。實測 037 之 VC 亦只寫
  `Expected Result: - Reduces climate control system power consumption`
  —— **上游自己也沒給可觀察量**，其 Verification Method 卻標
  `Manual UI Testing`
- **降耗之機制**：AUTO ECO 之設定（取消 airflow mode 選取、風速指示）
  —— 但那是 **`10.6` 之兩個 leaf**（已由 `-075`／`-076` 涵蓋）。
  以之充當 `044-02` 即為**兩個 leaf 共用一組可觀察量**，違 §4.5

**結論：Comfort 範圍內無可獨立驗證之餘留，且不足以構成一條 TC。**

### 1.5 與既有兩個 `[BLOCKED-SPEC]` 用例之對照 —— **異型**

| | `080-02` | `081-02` | **`044-02`** |
|---|---|---|---|
| leaf 描述 | `logic as per **HMI Core Logic and Flow (requirement N0)**` | `equivalent to short press of **previous 4-way rocker hard control**` | `reduces climate control system power consumption` |
| **明文指名之外部擁有者** | **有**（具名文件＋需求編號）| **有**（具名硬體控制）| **無** |
| 扣除委派後之餘留 | 空 | 空 | **不適用 —— 無委派可扣** |
| 不可驗之成因 | 內容**在別的文件裡** | 內容**在別的文件裡** | 內容**不是 HMI 行為** |

**R-C24 之 `[BLOCKED-SPEC]` 判準為「條文把內容委派到別的文件」。
`044-02` 不符** —— 它沒有把內容交給誰，它的內容根本不是介面行為。

### 1.6 我的建議（不代裁）

**不建議增列白名單。** 兩種形態不宜共用一個 marker：前者之 Remarks 可寫出
`Owner: <文件>`（R-C27 要求擁有者於首行可見），而 `044-02` **寫不出擁有者**
—— 硬要寫只能寫「動力系統」，那是我推的，非條文所指。

較合形態者為 **R-C16 之覆蓋缺口項**（不產列、登記、不入分母），
其現況已與之相同。**若採此路，本 leaf 之處置即為現狀之追認**，
無須新增 marker 亦無須動白名單。

**待裁**：採 R-C16 覆蓋缺口，抑或另立一種 marker 以區別「內容在別處」與
「內容非 HMI 行為」。在此之前該 leaf 維持停下、不產列、不入分母。

---

## 2. DR #22 ＋ `-022` 之 reasoning

**DR #22** 已登（RD-1 候選，Medium，**不阻塞**），含 §8.4.2 之處置理由、
兩側皆未述之實測（ch10 對 `MAX DEF`／`defrost`／`break` 零命中），
以及風險：解答前 `-022` 於 BEV 上之判定由測試員自行認定，屬 §7 之 FP／FF。

`-022` 之 `reasoning` 增一句具名該缺口與編號，**TC 內容一字未動**
（PC、procedure、ER 皆同）。

---

## 3. 候選分級判定 —— 686 對

### 3.1 等價組擴充後之數量變化

下放包所稱之 205 對係**擴充前**之數。擴充後（§4）五組相關之候選為 **686 對**：

| 級別 | 對數 | 作法 |
|---|---|---|
| 共有語彙 ≥ 2 | **195** | 逐對判定 |
| 單一**低頻**語彙（`MAX DEF`／`REAR DEF`／`CLIMATE OFF`／`RECIRC`／`MAX A/C`／`A/C`）| **19** | **亦逐對判定** —— 下放包之類級適用於高頻詞，低頻單一語彙不在其列 |
| 單一**高頻**語彙（`AUTO` 150／`FAN` 128／`MODE` 81／`HVAC` 56／`TEMPERATURE` 53／`HI` 4）| **472** | 類級判定 ＋ 抽樣覆核 |

逐對 **214**、類級 **472**。

### 3.2 逐對判定之依據分類（每對各記其理由）

七類：ch16 鏡射、ch10 之 ECO 外加狀態、ch11／12 之座椅層級同形異義、
ch14／15 之呈現 vs 行為、前後排之不同需求、ch17 之 widget 呈現、
同章不同組之控制名共用。

**前後排一類我逐節讀了全文**（7.1／7.1.1／7.2／7.4／7.5／7.7／7.8／9.2），
其中一對為新發現：

> **`2.7` ↔ `7.5`（sibling）**：CR5 逐句重述 C6 之 `Fan ranges: Off, 1-7,
> 15h`、指示位置、以及 Fan up/down 按鈕／觸碰 fan segment／滑動三種調整
> 途徑 —— 差異軸為前排 vs 後排 climate screen。

### 3.3 類級判定之抽樣覆核 —— **兩個類當場失效**

依 R-C37，抽樣**刻意挑「看起來最可能真的是 sibling」的三對**，
非挑最明顯不是的三對。六類各三對，逐對讀全文。

**結果：六類中兩類失效。**

| 類 | 抽樣結果 |
|---|---|
| **`AUTO`** | **失效** —— `2.3 ↔ 7.2`：C2「AUTO has on/ off state. The fan speed indicator shows Auto instead of the actual fan speed」與 CR2「**Rear** AUTO has on/ off state. The fan speed indicator shows Auto instead of the actual fan speed」**逐字相同** |
| **`MODE`** | **失效** —— `2.12 ↔ 7.8`：C13「ON state for the **four** airflow modes is shown by highlighting the button and increasing button size」與 CR8「ON state for the **three** airflow modes is shown by highlighting the button and increasing button size」近乎逐字 |
| `FAN` | 成立（`2.7 ↔ 9.2`／`2.2 ↔ 7.5`／`7.5 ↔ 2.7.1` 三對皆非同一需求）|
| `HVAC` | 成立（`10.1 ↔ 2.14`／`2.7.1 ↔ 14.11` 皆非）|
| `TEMPERATURE` | 成立（`2.6 ↔ 7.1`／`2.6.1 ↔ 7.1.1`／`2.6 ↔ 2.2` 皆非；後二者為**對比**而非重述）|
| `HI` | 成立（座椅層級 vs 溫度檔位，同形異義）|

**處置依 40 §3 末段**：失效者為**該類之判定**而非該對之判定，故
`AUTO`（150 對）與 `MODE`（81 對）**共 231 對之 verdict 改為
`class-invalidated`**，須改以逐對判定，**本輪未進行**。

兩對新 sibling 已入表。`data/pending_sibling.tsv` 現 **689 列**：

| verdict | 列數 |
|---|---|
| `sibling` | **8** |
| `not-sibling`（逐對）| 209 |
| `not-sibling (class)` | 241 |
| **`class-invalidated`** | **231** |

### 3.4 這次抽樣為什麼有用

**若抽樣挑的是「最明顯不是 sibling」的三對，六類都會通過。**
挑最像的那三對，兩類當場破。

`2.3 ↔ 7.2` 之兩句**逐字相同**，而它們的唯一共有語彙只有 `AUTO`
—— 因為 `Rear AUTO` 與 `AUTO` 在我的詞彙集裡是同一個 token，
其餘的詞（`fan speed indicator`／`Auto instead of the actual fan speed`）
**根本不在詞彙集內**。

**共有語彙之數量與是否為 sibling 無關。** 我用它分級，是為了分配工作量，
而不是因為它有判別力 —— 這次它把一對逐字相同的 sibling 分到了最粗的那一級。

---

## 4. 等價組擴充

### 4.1 兩項改造

1. **比對改為大小寫不敏感**（`re.I`）。實測支持：`SYNC` 20 次、`Sync` 8 次、
   `sync` 6 次 —— **分裂是真的，非假想**
2. **變體來源為實測**：掃全 129 節之縮寫／分隔形態，得
   `A/C` 44 vs `AC` 11、`MAX A/C` 23、`MAX DEF` 32 vs `MAX DEFROST` 2、
   `REAR DEFROST` 7 vs `REAR DEF` 1、`FRONT /MAX DEFROST` 1

等價組：`MAX DEFROST`／`FRONT /MAX DEFROST` → `MAX DEF`；
`REAR DEFROST` → `REAR DEF`；`MAX AC` → `MAX A/C`；`AC` → `A/C`；
`RECIRCULATION` → `RECIRC`。

### 4.2 驗證：`2.11 ↔ 3.2` 之 `SYNC` 現在對得上

```
2.11: ['FAN', 'MODE', 'SYNC', 'TEMPERATURE']
3.2 : ['A/C','AUTO','FAN','FRONT DEF','HI','MAX A/C','MAX DEF','MODE',
       'REAR DEF','RECIRC','SYNC','TEMPERATURE']
2.11 ∩ 3.2 = ['FAN','MODE','SYNC','TEMPERATURE']
```

`3.2` 寫 `turns on Sync`、`2.11` 寫 `SYNC` —— 擴充前交集不含 `SYNC`。

### 4.3 五組全部重跑

| 組 | 擴充前 | 擴充後 |
|---|---|---|
| `Seat Control Tab` | 0 | **0** |
| `Tri-Mode Climate` | 45 | **126** |
| `Front Climate Anatomy` | 19 | **111** |
| `Temperature and Fan` | 41 | **195** |
| `ECO HVAC` | 164 | **308** |

`reviewed_at` 皆更新為 **129**。不完備性之聲明維持（R-C37）。

---

## 5. A-CF23 —— **登記時發現原始事實記錯，已訂正**

下放包 40 §5 與我上繳 28 §10.5 皆記為「`10.2` 之三張圖片於
`section_fulltext.tsv` 僅存檔名」。**實測不然**：

| 來源 | `(image:` 命中 |
|---|---|
| `data/section_fulltext.tsv`（SYS1 export）| **0** |
| **037 之 Requirement Description** | **52 個標記，25 個 leaf** |

**圖片標記在 037（SWRA 分析報告）裡，不在 SYS1 export 的條文裡。**
我當初讀到那三個檔名是在 037 之 leaf 描述中，卻寫成 `section_fulltext`
—— **兩份文件混記**，而下放包照我的敘述複述了一次。

**範圍也遠大於當時所知**：25 個 leaf 帶圖，命中最多者為
`SWE1-HVAC-023`（3.1 Tri-Mode，**6 張**）、`-055`（5）、
`-001`／`-044`／`-045`／`-083`（各 3）。

**其中 `-023`（已生成 `-015`…`-017`）與 `-076`（已生成 `-001`…`-003`）
之 TC 皆已產出** —— 即**現有 TC 中已有數條，其上游 leaf 描述帶有我讀不到
的圖片**。這不是 `10.2` 一節的事。

A-CF23 與 DR #23（Low，圖片擷取工具）皆依實測敘述，**不列 RD-1**
（圖片在 037 內，非上游遺漏；問題在讀取能力）。

---

## 6. lint 與 §9 自評

```
41 / 41 gates PASS; 0 finding(s) across 80 TCs
```

**本輪未新增或修改任何 TC 之內容** —— 唯一之 TC 層變動為 `-022` 之
`reasoning` 增一句（§2）。故 §9 十七項**僅第 12 項變動**：

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 12 | 溯源、§8.2.1、§8.4.2 | 變 | `-022` 之 reasoning 依 §8.4.2 呈報 coverage hole 並具名 DR #22；PC 與 ER 未動，故不構成範圍變更 |

`anomaly-id-registered` 於本輪**第四次**先於我開口 —— 貼完下放包即指名
A-CF23 未登記。

---

## 7. 進度

| | 數 |
|---|---|
| 驗證單位（leaf）| 403 |
| 已生成（leaf）| 75 |
| 已生成（TC）| 80 |
| 阻塞／停下（leaf）| 3（2.1 之 2 ＋ `044-02` 之 1）|
| 未開始（leaf）| 325 |

---

## 8. 「本包是否仍有該驗而未驗者」

依 R-C30。

1. **`class-invalidated` 之 231 對未逐對判定。** 這是本包最大的未完項
   —— 兩個類失效之後，其成員之 verdict 目前是「已知不可信」而非「已判」。
2. **其餘四類（241 對）之抽樣各只有三對。** `AUTO` 與 `MODE` 破在第一次
   抽樣，**這說明三對之抽樣力度足以破類，但不足以證類** —— 通過的四類
   只是「三對沒破」，不是「類成立」。
3. **逐對之 214 對中，只有前後排一類（含 8 對）我讀了全文。**
   其餘 206 對之理由為類別推導（ch16 鏡射、ch14/15 呈現…），
   **與類級判定之差別在於粒度，不在於證據強度**。
4. **A-CF23 之影響範圍已知而未評估**：25 個 leaf 帶圖，其中已生成者
   （`-023` 之 6 張、`-076` 之 1 張）**其 TC 是否因讀不到圖而漏驗，未逐條檢視**。
5. **等價組只涵蓋我掃到的形態。**
   **搜尋範圍**：`MAX *`／`REAR *`／`FRONT *`／`A/?C`／`SYNC`／`RECIRC*`
   六種 pattern 之全 129 節掃描。**未掃**者如
   `Defrost` vs `DEF`（`FRONT DEF` 與 `Defrost` 是否同指）、
   `Menu Bar` vs `menu bar`（已由 `re.I` 涵蓋）。

---

## 9. 建議 commit message（git 未執行）

```
docs(comfort): 044-02 evidence; grade 686 sibling candidates

- 044-02: five-part evidence. Unlike 080-02/081-02 it names no external
  owner — its content is not delegated, it simply is not HMI behaviour.
  Recommend R-C16 coverage-gap rather than a [BLOCKED-SPEC] whitelist entry
- register DR #22 (which AUTO state a BEV enters) and add the named gap to
  -022's reasoning; the TC itself is untouched
- expand the equivalence groups: case-insensitive plus measured variants
  (SYNC 20 / Sync 8 / sync 6). Candidates go 205 -> 686 across five sets
- grade them: 214 per-pair, 472 by class. Sampling the three most
  sibling-looking pairs per class broke two classes on the spot —
  2.3 <-> 7.2 and 2.12 <-> 7.8 are verbatim front/rear restatements — so
  AUTO's 150 and MODE's 81 are marked class-invalidated
- also found 2.7 <-> 7.5 by reading the rear sections in full
- register A-CF23, correcting the record: the image markers are in 037's
  Requirement Descriptions (52 across 25 leaves), not in section_fulltext
- lint 41/41 PASS across 80 TCs
```

---

## 10. 待分析層

1. **§1.6** —— `044-02` 採 R-C16 覆蓋缺口，抑或另立 marker。
2. **§3.3** —— `class-invalidated` 之 231 對之逐對判定（本輪未做）。
3. **§8.2** —— 通過之四類其抽樣力度是否足夠（三對只能破類不能證類）。
4. **§8.4** —— A-CF23 之 25 個帶圖 leaf 中，已生成者是否須逐條複查。
