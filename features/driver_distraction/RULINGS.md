# RULINGS — driver_distraction (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 driver_distraction 之裁決權威；
跨 feature 條文承接時註明來源包。

---

(no rulings recorded yet)

## 現行版索引（沿 R-SU8(b) 同型；本 feature 自始即建）

> 判準：同一條號有多版本時，**v 字尾最大者為現行**；無 v 字尾者視為 v1。
> 被取代之版本僅供沿革查考，其所載之數值、形態陳述、拘束**一律不得引用**。
> 本表與條文區塊不一致時，**以條文區塊為準**，並即修本表。

| 條號 | 現行版 | 主旨 | 來源下放包 |
|---|---|---|---|
| R-DD1 | v1 | feature 身分：slug `driver_distraction`、Test Group `Driver Distraction`、前綴 R-DD／A-DD／DR-DD | 02 §一 |
| R-DD2 | v1 | tc_id_format `newR1L-DD-{n:03d}`；project 前綴權威為工作簿 D2 | 02 §一 |
| R-DD3 | v1 | ER 之斷言錨層級：HMI 現象為主錨；callback／Listener 依 reaction presence 降階 | 02 §一 |
| R-DD4 | v1 | SYSAD 為人讀參考，不入語料、不入 prompt 指紋 | 02 §一 |
| R-DD5 | v1 | 四庫綁 `vehicle_setting/inputs/` 原件；sha256 自實體檔重算；查無者逐項登 DR | 02 §一 |
| R-DD6 | v1 | 訊號名之架構軸：一律取 ATLANTIS 欄（繫於 R-DD5 之綁定）；引 LID 須標架構欄 | 07 §一 |
| R-DD7 | v1 | MPH 門檻於 km/h 匯流排之 raw 邊界：上鎖 129／解鎖 77；全標 A-DD6，登 DR-DD4 | 07 §二 |
| R-DD8 | v1 | Market Configuration Table 之採用與保留：取 Country_Code=91、標 A-DD5、DR-DD3 不結案 | 07 §三 |

**留存之被取代條文**：無（本 feature 自始無改版）。

---

```
R-DD1（feature 身分）

Feature slug = `driver_distraction`；Test Group = `Driver Distraction`
（取 037 Project Name 欄實值；CFTS 章名 `Driver Distraction Lockout`、
HMI spec 題名 `Driver Lockout` 均不採 —— 037 為生成主驅動，Layer 1 從其命名）。
裁決／異常／資料請求前綴 = R-DD／A-DD／DR-DD。
（Pei 2026-08-27 裁定，下放包 02）
```
---

```
R-DD2（TC ID 格式）

tc_id_format = `newR1L-DD-{n:03d}`（IN §10.3）。
project 前綴之權威為工作簿 D2 儲存格；執行層開副本時實測確認為
`newR1L`，不符即停並回報，不得逕改格式字串。
（Pei 2026-08-27 裁定，下放包 02）
```
---

```
R-DD3（ER 之斷言錨層級）

037 之 Verification Criteria 以軟體層事件表述
（「The subscribed Listener receives a RESTRICTED callback」等）。
SWQT 之可觀察面為 HMI 現象與可讀之 log。裁定：

(a) ER 之主錨為 **HMI 現象**（鎖定 feature 之 UI 態、Fullscreen
    Lockout 畫面、Standard Lockout Popup、feature 之可及性）。
(b) VC 中之 callback／Listener 事件類敘述，依 reaction presence
    降階處理（R-BLM13 同族）：ER 得斷言「系統對條件變化有可觀察
    之反應」（如鎖定生效／解除於 HMI 呈現），**不得**斷言
    callback 本身之送達、時序或參數 —— 該層非 SWQT 觀察面。
(c) 細則（各 leaf 之 HMI 錨對照、log 錨之採認條件）入 feature
    profile，於 pilot 前定稿。
（Pei 2026-08-27 裁定，下放包 02）
```
---

```
R-DD4（SYSAD 之地位）

SYS3 SYSAD（FM-WI-FSM-015-A01）入 `inputs/` 並入 feature.yaml
`reference` 節綁 sha256；地位為**人讀參考**，不入批次語料、
不入 prompt 指紋 fingerprint.prompt_sources。
TC 之任何內容不得以 SYSAD 為來源（其為 SWE.2 側架構文件，
非 SWE.1 需求 —— 引之即層級錯置）。
（Pei 2026-08-27 裁定，下放包 02）
```
---

```
R-DD5（四庫綁定）

$Speedometer$／$VC_Trans_Equipped$／$PresentGear$／$PARK_BRK_EGD$／
$Country_Code$ 之 DBC/LID/PROXI 對應，沿 R-BLM11 乙案：
綁 `features/vehicle_setting/inputs/` 之四原件
（LID v1_76、PDT27_E2A_R4_BHCAN.dbc、PDT27_E2A_R5_FDCAN8.dbc、
PROXI_HDCC27_R3_20250424.xlsx），不複製入本 feature inputs/。
sha256 由執行層自實體檔重算，不抄他 feature 之宣告值。
逐訊號查對照；查無者依 IN §8.7.5(d)(g) 保留來源名稱並逐項登 DR，
不得代以語意相近之他訊號（R-13）。
（Pei 2026-08-27 裁定，下放包 02）
```

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
（Pei 下放，分析層即裁，下放包 07 §一）
---

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
（Pei 下放，分析層即裁，下放包 07 §二；採丙）
---

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
（Pei 下放，分析層即裁，下放包 07 §三；所裁者為處置，非識別）
---
