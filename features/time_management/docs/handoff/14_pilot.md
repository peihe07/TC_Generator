# 下放包 14 — B7 衝突裁定、鍵名統一、pilot 部分覆核（7/19）

分析層 → 執行層。往返編號 `14`。對應上繳 `docs/upstream/14_pilot.md`。
`13` 受理。**B1 19 條已生成，本包為 pilot 之第一部分。**

**分析層只讀了前 7 條**（001 ×3、003 ×2、006 ×2），本包之覆核**僅及於此**。
其餘 12 條之覆核指派於 §5 —— 不以部分覆核冒充全部。

---

## 1. §4 B7 衝突 —— 採 (a)，並補 020/021 之空欄處置

執行層之診斷正確：**lint 抓到的不是寫錯，是規則有未定義處**
（佔位與真值並存時之分隔符無條文規定），且 15/19 全綠、4 條全落在
「同一 leaf 既有 Atl-Hi 又有 Atl-Mid」之情形 —— **這是 lint 有效性之
正面實測，不是缺陷。**

傾向 (a) 之理由（與 A-TM13 之 B3 處置同形、不需新增條文）成立，
但其自陳之缺口（020/021 無真值可留，該欄會空）須一併解決。

```
R-TM64（分析層裁定，2026-08-22）—— spec_reference 只放真值，佔位放 Remarks

specification_reference（工作簿 N 欄）**只放符合 canon §10.7(a) 之真值**，
排列依 §10.7（前綴一次、`, ` 續列、升冪、禁 `;`）。

**佔位一律放 Remarks（AH 欄）**，與 A-TM13 之 DR-5 佔位同處
（G-TM1 項 3 已如此規定）。Remarks 因此成為**全部缺口宣告之單一落點**。

**例外 —— 零真值之片**：若某條 TC 之全部引用物件皆非 Atl-Hi
（020 / 021 兩片），spec_reference 留空即違反 canon §8.4.3。
故該情形下 spec_reference 寫**單一佔位**：

    PENDING: DR-11 Atl-H 對應需求

（不含物件 id —— 逐項明細寫在 Remarks，N 欄只需標明「此欄待補」）

**B7 之判準隨之調整為**：
  (i) 欄值符合 `CFTS015-<7位>(, <7位>)*` 之形式；**或**
  (ii) 欄值恰為 `PENDING: DR-11 Atl-H 對應需求` 單一佔位
二者以外皆報。**分隔符 ` / ` 自此不再使用。**
```

## 2. §5.1 鍵名不一致 —— 統一為 `spec_reference`

執行層指出兩層用不同鍵，且 **write_back 側是靜默失效**（取不到值即該欄
空白寫入工作簿）。傾向 `spec_reference`（`feature.yaml` 之權威宣告）
**分析層同意**。

```
R-TM65（分析層裁定，2026-08-22）—— 欄位鍵名統一為 feature.yaml 之宣告

TC JSON 之欄位鍵名以 `feature.yaml` 之 `workbook.columns` 宣告為準。
本 feature 即 `spec_reference`（非 `specification_reference`）。

lint 之 B7 與 arch 閘改讀 `spec_reference`。
**19 條 TC 之 `specification_reference` 鍵移除** —— 兩鍵並存本身即雙來源
（`13` §5.1 自陳為權宜非解法）。

**write_back 增啟動檢查**（執行層 §5.1 之建議，採納）：
`cols` 之每個 key 是否至少在一條 TC 內出現；未出現者報
「該欄將全空寫入」並 raise，不得靜默續行。

canon §10.1 之 `specification_reference` 為**輸出契約之欄名**，
與 TC JSON 之鍵名為兩件事；本條只統一後者。
```

## 3. §5.3 A-TM26 無 lint 閘 —— 補

自檢發現 30 處訊號中只有 2 條記了 `ArchColumn`，**靠人工發現**。
A-TM26 明訂「無此記錄一律視為未驗」，而該判準無自動攔截。

**指派實作**（§5 T3）：TC 之 procedure 或 ER 含 LID 訊號名者，
其 reasoning 須含 `Atlantis High (col 26-30)` 與來源列號，否則報。

## 4. **pilot 部分覆核 —— 前 7 條**

**兩項 defect、三項 style-divergence、一項 note。**

### 4.1 defect-1 —— TC#3（001 第三條）違反 canon §8.7.4

```
test_item 下半：(confirm the manual entry items are unavailable while GPS sync is enabled)
expected_result 2/3：  "Set Time Hours" is greyed out
```

**test_item 主張「unavailable」（可操作性），ER 只驗「greyed out」（外觀）。**

canon §8.7.4 逐字：

> A visual state (greyed-out, dimmed) does NOT imply non-operability;
> the ER must not assert operability that contradicts the spec.

**此處是其鏡像**：ER 驗外觀而 test_item 斷言可操作性，
兩者不等價 —— 灰階仍可能可點。

**處置二擇一**（執行層決，回報所擇）：
- ER 增一步：嘗試操作該項並確認無效（若 spec 有此敘述）
- test_item 下半改為 `(confirm the manual entry items are greyed out …)`
  —— 與 ER 對齊，只主張外觀

**傾向後者**：HMI Settings List 之來源為 `Greys out with sync option
selected`，其本身即只敘述外觀。**主張不得超過來源。**

### 4.2 defect-2 —— TC#4（003 第一條）違反 canon §4.5 欄位歸屬

```
input_test_data:  PENDING: DR-10 設定 GPS 位置（跨時區邊界）之操作方式
test_procedure 1: PENDING: DR-10 使車輛位置跨越時區邊界之操作方式
```

**同一缺件在兩個欄位各寫一次。** canon §4.5 明訂資料只屬一個欄位，
不得在 Pre-Condition / Input Test Data / Procedure 間重複。

GPS 位置之設定是**操作**（互動資料），依 §4.5 屬 Procedure；
`input_test_data` 應為 `NA`。

TC#5 同型。**兩條皆須改。**

### 4.3 style-divergence（三項，不阻塞）

| # | 情形 | 判定 |
|---|---|---|
| S1 | `The HU main screen is displayed` 出現於 TC#1 / #7 之 pre_conditions | canon §4.4 明列「系統預設狀態」（如 `HU is powered on`）為禁用之 Pre-Condition。本項屬同族。**建議刪除** |
| S2 | `Ignition is ON` 幾乎每條皆有 | 邊界情形 —— CFTS 4813907 明列 Ignition working conditions 為 spec 條件，故非純預設。**保留，但不再視為理所當然**：若某 TC 之驗證與點火狀態無關，應刪 |
| S3 | TC#1 步驟 2 `Read the setting items shown and record them` ↔ ER 2 `…are enabled for entry` | 步驟說「讀項目」，ER 說「可輸入」—— 不完全對應。建議步驟改為 `Read the state of "Set Time Hours" and "Set Time Minutes" and record it`（與 TC#3 之寫法一致）|

### 4.4 note（一項）—— **值得記錄的正面**

TC#6 之 ER：

```
4. $DateTmHour$ carries 0 in Hour1_TLM and 8 in Hour2_TLM
```

**正確使用了 Atlantis High 欄之 4-bit 雙數位形態**（`11` §2.1 所述，
與 CFTS 4813930 之「0–23 單值」敘述不同）。

**若當初取了 Powernet 欄，此處會寫成 `$DateTmHour$ = 8`，形式合理而實質錯誤**
—— A-TM26 之風險在此具體化，且本次防住了。

### 4.5 未見問題者

`test_item` 兩段式與上半 verbatim、同 leaf 括號內容不重複、
禁用動詞 0 處、彎引號 0 處、步驟與 ER 1:1、`tc_id` 未出現、
design_method 為母本九條之一、priority 值域合法 —— **前 7 條皆合。**

---

## 5. 指令

### T0 / T1 — `RULINGS.md`：追加 R-TM64 / R-TM65

內文為 §1 / §2 之區塊全文。**增量**：`## R-TM` **+2**。

### T2 — B1 之四項修正

1. **spec_reference 依 R-TM64 重寫**：真值留 N 欄、佔位移 Remarks；
   020/021 型（本批無）之單一佔位規則一併實作於 context
2. **移除 `specification_reference` 鍵**（R-TM65），lint 改讀 `spec_reference`
3. **defect-1**：TC#3 依 §4.1 二擇一，回報所擇與理由
4. **defect-2**：TC#4 / TC#5 之 `input_test_data` 改 `NA`（§4.2）

**style-divergence S1 / S3 建議採納，S2 保留** —— 三項皆非阻塞，
執行層可自行判斷，回報所為。

### T3 — 三個 lint 閘

1. **B7 判準依 R-TM64 調整**（真值形式 or 單一 DR-11 佔位）
2. **A-TM26 閘**（§3）：含 LID 訊號名之 TC，reasoning 須有
   `Atlantis High (col 26-30)` 與來源列號
3. **write_back 啟動檢查**（R-TM65）：`cols` 之 key 未在任何 TC 出現即 raise

**各附 red-green。**

### T4 — **pilot 覆核之其餘 12 條**

分析層只覆核了前 7 條。其餘 12 條（007 ×3、008 ×4、010 ×3、012 ×2）
由執行層依**本包 §4 所用之同一組判準**自檢並回報：

```
canon §8.7.4  ER 驗外觀而 test_item 斷言可操作性
canon §4.5    同一資料在兩個欄位重複
canon §4.4    系統預設狀態出現於 pre_conditions
步驟 ↔ ER 之語意對應（非只數量 1:1）
§5.1 禁用動詞 / §11 引號與句尾句點
test_item 兩段式與同 leaf 括號不重複
A-TM26 之 ArchColumn 記錄
```

**逐條回報，發現即列，不預先修正**（同 `13` T5 之作法）。
分析層將於 `15` 覆核該自檢並補做獨立抽驗。

### T5 — 上繳

`docs/upstream/14_pilot.md`。依 R-TM54 三分列未驗清單。

### 不得執行者

- 不動 git；**不寫回工作簿**
- 不建 `tm_constants.py`
- 不自 Atlantis High 以外之架構欄取值
- 不縮減任何 leaf 之覆蓋
- 不碰 `features/vehicle_setting/`

---

## 6. 呈報 Pei

**B1 19 條已生成，品質高於預期。** 分析層覆核前 7 條，
發現兩項 defect（皆為 canon 條文之精確適用問題，非內容錯誤）、
三項 style-divergence。**無一項涉及 spec 理解錯誤或捏造。**

TC#6 之 ER 正確使用 Atlantis High 之 4-bit 雙數位形態 ——
**若當初取了 Powernet 欄會寫成 `$DateTmHour$ = 8`，形式合理而實質錯誤。
A-TM26 在此具體防住了一次。**

仍待你：

1. 常數表 v3 之 `SET_TIME_MANUAL` 依 HMI Settings List 改寫
   （設定頁名為 `Clock` 非 `"Time and Date"`）；v3 另缺
   `Read <signal> in <MESSAGE> on <segment> and record it` 一類（9 片受影響）
2. A-TM25（彎引號 / `check whether`）
3. RD-1 送出；DR-8/9/10/11/12/20 之上游查詢

## 7. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM64 | 分析層裁定，佔位移 Remarks + 零真值例外 | §1 | ✅ T1 + T2 + T3 |
| R-TM65 | 分析層裁定，鍵名統一 + write_back 啟動檢查 | §2 | ✅ T1 + T2 + T3 |

分析層本包未動 git、未改任何腳本、未改任何 TC。
§4 之覆核僅及前 7 條，其餘 12 條之覆核指派於 T4。
