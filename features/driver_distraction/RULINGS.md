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
| R-DD6 | **v2** | 訊號名之架構軸：匯流排訊號取 Atlantis High 欄；(e) 限匯流排訊號，PROXI 參數以 PROXI 檔為權威 | 08 §二 |
| R-DD7 | v1 | MPH 門檻於 km/h 匯流排之 raw 邊界：上鎖 129／解鎖 77；全標 A-DD6，登 DR-DD4 | 07 §二 |
| R-DD8 | v1 | Market Configuration Table 之採用與保留：取 Country_Code=91、標 A-DD5、DR-DD3 不結案 | 07 §三 |
| R-DD9 | v1 | 訊號值之書寫形式：有 VAL_ 者取逐字列舉，連續量改置物理值與單位，SNA 分流 | 08 §三 |
| R-DD10 | v1 | 外部表格之引用格式：Excel 書欄名不書 c{n}；LID 須標架構欄；計數須書母體判準與排除項；列號 1-based | 08 §三 |
| R-DD11 | v1 | 引號內字串之終端標點：逐字 UI 字串自身之句點保留；判準為移除引號後是否以作者句點結尾 | 10 §三 |
| R-DD12 | v1 | IN §11 方括號例外之啟用（profile-scoped）：僅及 test_item 上半之 037 逐字；lint 以「是否為來源逐字」判 | 10 §三 |
| R-DD13 | v1 | 訊號一格載多名時之取捨：先以綁定 DBC 篩，再取同見於 Atlantis 與 Atlantis High 二欄者；未取者記為備援 | 10 §三 |
| R-DD14 | v1 | `RULINGS.md` 之錨點體例：圍籬上方加 `## R-DDn`；加標題為新增行，不違 R-TM13；錨點數須等於條文數 | 11 §一 |
| R-DD15 | v1 | IN §5.2 之 word 計法：去編號後空白切分；偏嚴為刻意；逾限改步驟不改尺 | 12 §三 |
| R-DD16 | v1 | 輸出鍵名依既有寫回形制（test_item／spec_reference）；split_flag／split_reason 仍須輸出 | 12 §三 |
| R-DD17 | v1 | Pre-Condition 之訊號源行只書訊號源本身，不兼作觸發條件之主張 | 12 §三 |
| R-DD18 | v1 | 上游書面勘誤之採認界線：有書面回覆者得採認為施加名（僅及施加路徑）；無回覆者仍登 DR | 13 §三 |
| R-DD19 | v1 | DR-DD5／DD6 未回覆期間之假設生成（乙案）：施加路徑 A-DD8、代表值 A-DD9；**MTA(2)／DDCT(3) 為硬邊界，不得入任何 TC** | 15 §一 |

**留存之被取代條文（依 R-TM13 不刪不改，不得引用）**：

> **`R-DD6` 之 v1 與 v2 於 `RULINGS.sha.tsv` 中同 `ruling_id`**
> —— 工具之錨點正則將 prime（`′″‴`）與子條 `(a)` 併入 id，**不併入 ` v1`**。
> 二列皆收錄，無資料遺失（現行 tsv 已有 17 組同 id）。
> **故本表並列其 `sha8` 使二者以雜湊可辨**（下放包 12 §四-9；
> 承 §1.1 之全域拘束：歸因鍵須為內容雜湊，不得為識別名）。

| 條號版本 | 已被取代於 | `sha8`（v1／v2）| 其所載之失效值 |
|---|---|---|---|
| `R-DD6`（v1） | R-DD6 v2（下放包 08 §二）| **v1 `f28ee265`** ／ v2 `a5cbaf9c` | (a) 只書「取 **ATLANTIS 欄**」—— 未區分 `Atlantis` 與 `Atlantis High` 二欄，亦未載二欄不同字時之取捨；**無 (b)**（Atlantis High 優先）、**無 (e)**（本條限匯流排訊號；PROXI 參數以 PROXI 檔為權威）。其 (a) 之理由（可施加性）對非匯流排標的不成立 |

---

## R-DD1

```
R-DD1（feature 身分）

Feature slug = `driver_distraction`；Test Group = `Driver Distraction`
（取 037 Project Name 欄實值；CFTS 章名 `Driver Distraction Lockout`、
HMI spec 題名 `Driver Lockout` 均不採 —— 037 為生成主驅動，Layer 1 從其命名）。
裁決／異常／資料請求前綴 = R-DD／A-DD／DR-DD。
（Pei 2026-08-27 裁定，下放包 02）
```
---

## R-DD2

```
R-DD2（TC ID 格式）

tc_id_format = `newR1L-DD-{n:03d}`（IN §10.3）。
project 前綴之權威為工作簿 D2 儲存格；執行層開副本時實測確認為
`newR1L`，不符即停並回報，不得逕改格式字串。
（Pei 2026-08-27 裁定，下放包 02）
```
---

## R-DD3

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

## R-DD4

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

## R-DD5

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

## R-DD6 v1

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

## R-DD7

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

## R-DD8

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

## R-DD6

```
R-DD6 v2（訊號名之架構軸）

實測（上繳包 04 T10c）：綁定之二 DBC（PDT27_E2A_R4_BHCAN 155 訊息、
PDT27_E2A_R5_FDCAN8 323 訊息）為 ATLANTIS 側；LID 之 Powernet 欄名
（GW_C1.VEH_SPEED／GW_C1.Gr／VehCfg7.*）於二 DBC 皆不存在。

(a) 匯流排訊號之名一律取 **Atlantis High 欄**。理由非「該架構較佳」，
    而是**台架庫已綁定於此**：綁定件含 FD CAN（R5_FDCAN8），而 LID 中
    FD 側之名（PT_SYSTEM_FD_1.*、BRAKE_FD_2.*）**僅見於 Atlantis High 欄**，
    Atlantis 欄無 FD 條目。Powernet 名於本台架上寫得出來也送不出去。
(b) `Atlantis` 與 `Atlantis High` 二欄同字時無差別；**不同字時取
    Atlantis High**。實例：$Speedometer$ 二欄同字（STATUS_CCAN3.*）；
    $PresentGear$ 二欄不同字，Atlantis 欄之三名於二 DBC 皆不在，
    Atlantis High 欄之 PT_SYSTEM_FD_1.GearEngagedForDisplay_PT 在。
(c) 本條之效力繫於 R-DD5 之四庫綁定。若日後改綁他架構之庫，
    本條隨之失效並須重裁，不得沿用。
(d) LID 為多架構對照表。引其列時須同時標明所取之架構欄，
    格式 `LID {分頁名} r{n} [{架構}欄]`；只標列號者視同未標。
(e) **本條之適用範圍限於匯流排訊號。** PROXI 參數不經匯流排施加，
    (a) 之理由（可施加性）在其上不咬合；PROXI 參數以 **PROXI 檔為權威**，
    LID 僅為指標。LID 各架構欄對同一 PROXI 參數所載不一致者，
    登 DR，不逕選。
    （立此項之由來：上繳包 05 §5.4 —— v1 之失效條件只寫了「改綁」，
      未涵蓋「標的根本不走匯流排」；該案結論恰好不受影響，
      但理由不成立即應更正。）
（Pei 下放，分析層即裁，下放包 08 §二）
```
---

## R-DD9

```
R-DD9（訊號值之書寫形式：列舉量與連續量）

IN §8.7.5(a) 之 `= <raw> (<label>)`，其 <label> 定為 DBC VAL_ 之逐字列舉。
實測（上繳包 04）：綁定件中部分訊號無 VAL_ 列舉（連續量），
部分僅列舉 SNA。故分流：

(a) **有 VAL_ 列舉者**：`= <raw> (<VAL_ 逐字>)`。
    例：`$PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ = 12 (Park)`
(b) **無 VAL_ 之連續量**：<label> 位改置**物理值與單位**，
    並以 DBC 之 factor／offset 換算，換算式須可覆算。
    例：`$STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)`
    物理值以 DBC 單位書寫（本件為 km/h）；spec 之 MPH 值另依
    R-DD7(d) 併記，不取代 DBC 單位。
(c) **僅列舉 SNA 者**（如 VehicleSpeedVSOSig 之 8191 "SNA"）：
    正常值依 (b)，失效值依 (a) 書 `= 8191 (SNA)`。
(d) 任一寫法之 raw 皆須為 DBC 可表示之整數格；
    不可表示者依 R-DD7(c) 取跨越側第一格，並具名之。
（Pei 下放，分析層即裁，下放包 08 §三）
```
---

## R-DD10

```
R-DD10（外部表格之引用格式）

(a) **Excel 欄一律書欄名**（`H`／`S`／`BF`），不書 `c{n}` ——
    後者有 0-based／1-based 二種起點，本案已實際發生二層各用一種
    而看似不符之情形（上繳包 04 §4A.2(a)）。
(b) LID 之列一律書 `LID {分頁名} r{n} [{架構}欄]`（R-DD6(d)）。
(c) **凡書計數，須同時書其母體判準與排除項。**
    本案先例：`Market Config - R1` 之國別列計數 223 係排除 `WORLD`
    （非目的地國，Country_Code = 0）後之值；未書明即被讀為差 1 之錯
    （上繳包 04 §5.4）。
(d) 列號一律 Excel 之 1-based。
（Pei 下放，分析層即裁，下放包 08 §三）
```
---

## R-DD11

```
R-DD11（引號內字串之終端標點）

IN §11 之「無行尾句號」，其規制對象為**作者所書句子之句末標點**。
逐字引用之 UI 字串，其自身之終端標點屬該字串之一部分，**保留**。

例（合規）：
  The Standard Lockout Popup is displayed, showing
  "Feature not available while the vehicle is in motion."
  —— 句點在引號內，屬 HMI spec p4 之原字串；item 之末字元為 `"`，非 `.`

例（違規）：
  … showing "Feature not available while the vehicle is in motion.".
  —— 引號外另加句點，該句點為作者所書

判準：**移除引號後，該 item 是否以作者之句點結尾**。是即違規。
（Pei 下放，分析層即裁，下放包 10 §三）
```
---

## R-DD12

```
R-DD12（IN §11 方括號例外之啟用；profile-scoped）

依 IN §11 之 Exception，本 feature 啟用之：

(a) `test_item` **上半**（需求原句 verbatim）中，源自 037 之方括號記法
    （`Case [Normal]`／`Case [Exception]`／`$VC_Trans_Equipped$ = [Manual]` 等）
    **保留原樣**，不得改寫為雙引號 —— 改之即違 R-S4 之逐字。
(b) 例外**僅及於上半**。`test_item` 之括號下半（作者所書之測試目的）、
    以及 `pre_conditions`／`input_test_data`／`test_procedure`／
    `expected_result` 四欄，**一律依 IN §11 用 `"..."`，不得出現方括號**。
    唯一例外為裁決所命之 `[ASSUMPTION A-DDn]` marker（標記，非 UI 標籤）。
(c) lint／自檢對 `test_item` 之方括號，須以「該 token 是否為所引來源列
    之逐字」為判準（比對 037 原文），非一律禁。
（Pei 下放，分析層即裁，下放包 10 §三）
```
---

## R-DD13

```
R-DD13（訊號一格載多名時之取捨）

LID 之單一儲存格載多個訊號名者（如 `LID CAN Mapping r1738 [Atlantis High 欄]`
同時載 STATUS_CCAN3.VehicleSpeedVSOSig 與 BRAKE_FD_2.VehicleSpeedVSOSig）：

(a) 先以「該名存在於綁定 DBC」為篩。篩後唯一者即取之。
(b) 篩後仍多於一者，取**同時見於 `Atlantis` 與 `Atlantis High` 二欄者**
    —— 其不因架構欄之取捨而變，施加路徑最穩定。
    實例：STATUS_CCAN3.VehicleSpeedVSOSig 見於 P 欄與 Z 欄二者；
    BRAKE_FD_2.VehicleSpeedVSOSig 僅見於 Z 欄。故取前者。
(c) (b) 仍無法區別者，登 DR，不逕選。
(d) 未取之名於 profile §3 記為**備援**並註其匯流排，不得逕自替換；
    台架若無主路徑之匯流排，須先報再換。
（Pei 下放，分析層即裁，下放包 10 §三）
```
---

## R-DD14

```
R-DD14（RULINGS.md 之錨點體例）

`scripts/rulings_hash.py` 之錨點正則要求 `## R-…` 形式之標題，
其「條文本體」定義自錨點標題之次行起、至下一個同級或更高級標題之前一行止。
本 feature 之 `RULINGS.md` 採圍籬體例，**無標題錨點**，
故該工具收錄 0 條（上繳包 07 §1.1 實測）。

裁定（Pei 2026-08-28 准）：

(a) 於每一條文之圍籬**上方**加標題錨點 `## R-DDn`（留存版加
    `## R-DDn v1`，其標題文字須與索引表之留存列一致）。
(b) **加標題為新增行，非對條文本體之刪改** —— 圍籬符號與其內文字
    **一字不動**，故不違 R-TM13。執行層以逐字元 diff 證之：
    改動前後，全檔除新增之標題行與其後必要空行外，**差異須為 0**。
(c) 標題文字**不入雜湊**（工具 docstring 逐字），故加標題不改變
    任何既有條文之 sha 定義域內容；惟本檔原無錨點，
    **本次為自 0 條變為 n 條，非既有 sha 之變動**。
(d) 執行層於改動後以 `--target features/driver_distraction/RULINGS.md`
    導向 scratchpad 試跑，錨點數須等於現行條文數 ＋ 留存數；
    不等即停並回報，**不得調整條文以遷就工具**。
（Pei 2026-08-28 裁定，下放包 11 §一）
```
---

## R-DD15

```
R-DD15（§5.2 之 word 計法）

IN §5.2 未定義 word 之計法。本 feature 採：

(a) 去除編號前綴（`^\d+\.\s*`）後，以空白切分之 token 數。
(b) 訊號名 `$MESSAGE.Signal$` 計 1；`(8.0625 km/h)` 計 2；
    帶引號之 UI 標籤依其內含空白計（`"Pairing (1st time)"` 計 3）。
(c) 本計法對含單位與引號標籤之步驟**偏嚴**（同語意之步驟字數高於英文散文）。
    **偏嚴為刻意** —— 偏嚴不會放過違規，偏寬會。
(d) **不得為使步驟合格而改計法**。逾限時改步驟，不改尺。
（Pei 下放，分析層即裁，下放包 12 §三）
```
---

## R-DD16

```
R-DD16（輸出鍵名二制之處置）

IN §10.1 所列鍵名（tc_title／specification_reference／split_flag／
split_reason）與本專案既有 pilot／寫回形制（test_item／spec_reference）不同。

(a) **鍵名依既有寫回形制**：`test_item`／`spec_reference`。
    該二者為工具契約（寫回器所消費者），非 ASPICE 內容之要求；
    逕改鍵名將斷開寫回管線。
(b) **`split_flag`／`split_reason` 仍須輸出** —— 該二者承載資訊
    （某 leaf 是否被拆為多 TC 及其理由），非命名之別。
    未拆者 `split_flag: false`、`split_reason: "NA"`。
(c) 若寫回器拒受未知鍵，**回報，不得逕自刪鍵** ——
    刪之即湮滅 §8.2.2 之拆分紀錄。
（Pei 下放，分析層即裁，下放包 12 §三）
```
---

## R-DD17

```
R-DD17（Pre-Condition 之訊號源行）

四則 pilot 之 PC 現書
`The vehicle is stationary and $…$ is transmitted at 0 (0.0000 km/h)`。
其前半（`The vehicle is stationary`）與後半之 raw 0 重複陳述同一事實，
且前半為環境敘述而非 spec 觸發條件（IN §8.5）。

裁定：PC 之訊號源行**只書訊號源本身**，形如
`The signal $MESSAGE.Signal$ is transmitted on the bus at <raw> (<物理值>)`。

理由：如此該行純為 §4.5-1 之環境資料（外部訊號源），
**不再兼作對觸發條件之主張** —— 上繳 §1.2 所指
「-009 為四則中唯一非嚴格觸發條件者」之疑點，隨之消解：
四則之該行一律為環境資料，其是否兼為觸發條件，
由 037 原文於 test_item 與 Procedure 承載，不由 PC 承載。
（Pei 下放，分析層即裁，下放包 12 §三）
```
---

## R-DD18

```
R-DD18（上游書面勘誤之採認 —— 與「代換」之界線）

R-DD5 禁「查無者代以語意相近之他訊號」；R-13 禁以推定代缺件。
二者所禁為**自行推定**。下列情形不屬之：

(a) 上游於其自身文件內對同一疑問留有**書面回覆**者
    （本案：CFTS022 r129 之 SYS2 MD Feedback 欄逐字
    `The LID which is referred here is $PARK_BRK_EDG$`，
    並有 HARMAN Comments 之原始提問與 System-HW/SW 欄同載 EDG），
    得採認該回覆所指之名為**施加名**。此為 lookup ＋ 上游書面確認，
    非語意代換。
(b) 採認之界線：
    - **僅及於施加路徑**（Procedure／ER 之訊號名）。
      `test_item` 上半 verbatim 照 037／CFTS 原文（含 EGD），不改字。
    - 施加名之 CAN 對應**仍須自 LID 該列實測查得**（T19c），
      不得因勘誤成立而略過查證。
    - 規範欄未更正前，用及該施加路徑之 TC 標 `[ASSUMPTION A-DD2]`；
      上游正式更正（DR-DD2 之回覆）後撤。
(c) 本條不得反向援引：無書面回覆之「看起來像筆誤」仍依 R-DD5／R-13
    登 DR，不得採認。書面回覆之有無是本條與代換之**全部**界線。
（Pei 2026-08-28 准落，下放包 13 §三）
```
---

## R-DD19

```
R-DD19（DR-DD5／DD6 未回覆期間之假設生成 —— Pei 2026-08-28 裁乙）

(a) 施加路徑假設（marker A-DD8）：$VC_Trans_Equipped$ 依 LID
    `Proxi & Configuration` r421 之 Atlantis 欄採 PROXI 參數
    `Gear_Box_Type`（`Powertrain_Configuration_4`，byte 101，bit 0–2）。
    採認基礎：r420／r421 之三種自洽讀法中二種收斂於此
    （新舊列讀法、訊號/參數分答讀法），唯一阻斷之讀法（r421 該格為孤立
    筆誤）無任何形態支持 —— 此為讀法收斂之採認，非文件記載，故掛 marker。
(b) 代表值假設（marker A-DD9）：
      [Manual]    → PROXI Gear_Box_Type = 1 (MTX)
      [Automatic] → PROXI Gear_Box_Type = 4 (ATX)
    採認基礎：MTX／ATX 為兩極之無疑義代表 —— MTX 之 M 為業界命名之
    manual（IN §8.4.1 domain constant 家族），PROXI Annotation 之
    `manual` 舉例對應之；ATX 同理。
(c) **邊界（硬）**：`MTA`（2）與 `DDCT`（3）之歸屬為 DR-DD6 之未決問題，
    **不得以該二值作任何 TC 之 Pre-Condition 或輸入** ——
    乙案採認之範圍止於兩極，不及於邊界。
(d) 回覆後之處置：DR-DD5／DD6 之回覆與 (a)(b) 相符 → 撤 marker；
    不符 → 回修範圍為 8 TC 之 PROXI 值（機械性換值），結構不動。
(e) 本條不減 DR-DD5／DD6 之必發等級，不影響 DD1 之凍結。
（Pei 2026-08-28 裁乙，下放包 15 §一）
```
---
