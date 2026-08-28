# 下放包 07 —— Q7／Q8／Q9 裁定（R-DD6~R-DD8）、profile §3 解除、T12、DR-DD4

- 日期：2026-08-27
- 方向：分析層 → 執行層
- 前一包：`06_market_config.md`
- 裁定狀態：Q7／Q8／Q9 —— **Pei 下放，分析層即裁**（R-DD6／R-DD7／R-DD8）
- **pilot 條件解除**：§四所列三項回填完成後即可開；`$VC_Trans_Equipped$` 相關 leaf 除外

---

## 〇、先分清一件事

Q7／Q8 為**方法與形制之裁定**，分析層有權為之（同 R-SU10~R-SU13 之型態）。

**Q9 不是**。「SR24 R1 MCT 是否即 CIP MCT」為**事實**，分析層無證據可定，
裁了也只是把猜測寫成條文。**故 R-DD8 所裁者為「處置」，非「識別」** ——
識別仍懸，且以 assumption marker 使其在交付物上可見。二者不得混同。

---

## 一、R-DD6（Q7 架構選定）

```
R-DD6（訊號名之架構軸）

實測（上繳包 03 T9a）：綁定之二 DBC（PDT27_E2A_R4_BHCAN 155 訊息、
PDT27_E2A_R5_FDCAN8 323 訊息）為 ATLANTIS 側；LID 之 Powernet 欄名
（GW_C1.VEH_SPEED／GW_C1.Gr／VehCfg7.*）於二 DBC 皆不存在。

裁定：
(a) profile §3 之訊號名一律取 **ATLANTIS 欄**。理由非「ATLANTIS 較佳」，
    而是**台架庫已綁定於此** —— 綁定之庫決定何者可施加，
    Powernet 名於本台架上寫得出來也送不出去。
(b) 本條之效力繫於 R-DD5 之四庫綁定。**若日後改綁他架構之庫，
    本條隨之失效並須重裁**，不得沿用。
(c) LID 為多架構對照表。引其列時**須同時標明所取之架構欄**，
    格式 `LID {分頁名} r{n} [{架構}欄]`；只標列號者視同未標
    （下放包 05 §1.1 之誤一之延伸）。
```

**回填**（`$Speedometer$`，T9a 實測）：

```
STATUS_CCAN3.VehicleSpeedVSOSig   13 bit, factor 0.0625, unit Km/h
```

`$PresentGear$` 之 ATLANTIS 名待 T10c 回報後回填。
`$VC_Trans_Equipped$` 見 §四。

---

## 二、R-DD7（Q8 門檻之 raw 邊界）—— 採丙

```
R-DD7（MPH 門檻於 km/h 匯流排上之邊界定義）

spec 門檻以 MPH 表述（5 MPH 上鎖／3 MPH 解鎖），而綁定匯流排之
速度訊號單位為 Km/h、factor 0.0625（raw = km/h × 16）。

(a) `1 MPH = 1.609344 km/h` 為單位定義，屬 IN §8.4.1 之 domain constant，
    援用不構成造值。
(b) 換算結果不落於整數 raw：
      5 MPH = 8.04672 km/h → raw 128.74752
      3 MPH = 4.828032 km/h → raw 77.248512
    即此匯流排上**不存在「等於 5 MPH」之格**。
(c) 邊界依**條文之不等號方向**取跨越側之第一個可表示格：
      「equal or greater than 5MPH」→ 上鎖之最小 raw = **129**
        （129 × 0.0625 = 8.0625 km/h = 5.0097 MPH ≥ 5 ✓
         128 × 0.0625 = 8.0000 km/h = 4.9710 MPH < 5 ✗）
      「equal or less than 3MPH」→ 解鎖之最大 raw = **77**
        （77 × 0.0625 = 4.8125 km/h = 2.9903 MPH ≤ 3 ✓
         78 × 0.0625 = 4.8750 km/h = 3.0292 MPH > 3 ✗）
(d) TC 內**一律具名 raw 並附其 km/h 與 MPH 實值**，
    不得只寫「5 MPH」而讓執行者自行換算。
(e) BVA（IN §12）之 limit±1 依 (c) 定義：
      上鎖側 128（不應鎖）／129（應鎖）
      解鎖側 77（應解）／78（不應解）
(f) (c) 之推導為**分析層依 DBC 實測值所為**，DUT 內部之取整可能相異
    （±1 raw ≈ 0.04 MPH）。故**全部依本條產出之 TC 標
    `[ASSUMPTION A-DD6]`**，並登 DR-DD4 向上游確認判定單位與取整規則。
    DR 回覆若與 (c) 不同，回修範圍為速度類 leaf 之 ER 數值，
    不動其結構。
```

---

## 三、R-DD8（Q9 之處置，非識別）

```
R-DD8（Market Configuration Table 之採用與其保留）

LID `Proxi & Configuration` r43 c7 指名 `CIP Market Configuration Table
v*.xlsx`；到位者為 `SR24 R1 Market Configuration Table v1.6.xlsx`。
**檔名不同，二者是否同一份為事實問題，分析層無證據可定。**

裁定（處置）：
(a) 採其值 —— `$Country_Code$` Hong Kong = `91`（十進位，Hex 5B），
    取自 `Market Config - R1` r97 c19，表頭逐字
    `PROXI3  <Country_Code>Signal - Decimal`。
(b) 凡用及該值之 TC 一律標 `[ASSUMPTION A-DD5]`。
(c) **DR-DD3 不結案**，狀態 `ANSWERED-PENDING-CONFIRM` ——
    值已得、識別未確認。上游確認後始轉 RESOLVED 並撤 A-DD5。
(d) 本條不改變 A-DD1／DR-DD1：市場歸屬仍懸，二者為獨立阻斷。
    亦不得以該表 c58（Navigation DD Lockout Disable）推論 A-DD1 ——
    該欄對應 CFTS022 -136（Out of scope），範圍不同（下放包 06 §1.2）。
```

---

## 四、`$VC_Trans_Equipped$` —— 兩架構皆無解（T12）

Pei 回報：該項於 Powernet 與 ATLANTIS 兩側皆無可施加之 CAN 訊號。

**登 DR 之前先窮盡量測** —— 上繳包 01 T6 之原始輸出，
LID `Proxi & Configuration` r421 末二欄逐字為 `Gear_Box_Type`／`Gear_Box_Type`。
其形態與 `Country_Code` → `Car_Configuration_16.Country_Code` 同族
（**PROXI 參數，非 CAN 訊號**）。

**此為候選，非結論** —— 未查證前不得寫入 profile。

| # | 任務 |
|---|---|
| T12a | PROXI 檔（`PROXI_HDCC27_R3_20250424.xlsx`）全檔查 `Gear_Box_Type`：所在 component／byte／bit、值域與列舉逐字。查無即明記查無 |
| T12b | 同法查 `VC_Trans_Equipped` 於 PROXI 之直接命中（T6 記為 0 處，本輪覆核） |
| T12c | LID `Proxi & Configuration` r420 與 r421 兩列**全欄逐字**（含欄名），標明何欄為 Powernet、何欄為 ATLANTIS、何欄為 PROXI 側 |

- **T12 查得** → 依 IN §8.7.5(c) 寫 `PROXI Gear_Box_Type = <值>`（不加 `$`），分析層回填 profile §3
- **T12 查無** → 登 DR-DD5，`-017`~`-024` 之該條件欄位掛 `PENDING: DR-DD5`（§8.4.3），不留空

**在此之前，`$VC_Trans_Equipped$` 相關 leaf（017–024）不入 pilot。**

---

## 五、profile §3 之解除條件（分析層自辦，待 T10c／T12 回報）

| 訊號 | 狀態 |
|---|---|
| `$Speedometer$` | **可解除** —— ATLANTIS 名已實測；raw 邊界依 R-DD7 |
| `$PresentGear$` | 待 T10c 之 ATLANTIS 名 |
| `$VC_Trans_Equipped$` | 待 T12 |
| `$PARK_BRK_EGD$` | 維持保留來源名（DR-DD2 未結） |
| `$Country_Code$` | **可解除** —— `PROXI Country_Code = 91`，標 A-DD5 |

## 六、任務彙總

| # | 任務 |
|---|---|
| T-抄 | R-DD6／R-DD7／R-DD8 逐字 append 入 `RULINGS.md`，索引表同步（8 條現行 0 留存）；程式回讀逐字元核對 |
| T-登 | A-DD5（MCT 識別未確認）、A-DD6（raw 邊界為分析層推導）登入 `ANOMALIES.md`；DR-DD4 建檔（§二(f)）；DR-DD3 狀態改 ANSWERED-PENDING-CONFIRM |
| T12a–c | §四 三項 |

**不在本輪**：TC、pilot、寫回、git。

## 七、上繳包要求（`docs/upstream/05_signal_close.md`）

T-抄核對、T-登結果、T12a–c 原始輸出、未結 DR 清單（DD1/DD2/DD3/DD4[/DD5]）、
獨立自評、R-G8 揭露。
