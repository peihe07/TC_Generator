# 上繳 11 —— Atlantis Mid 之範圍證據、階數維度全量複核、左右對稱追因

執行層寫入。依據：`docs/handoff/29_review_round12.md` §4。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | A-VS45 新開、A-VS44 標口徑 ＋ 登記簿兩數 | ✅ 見 §5.1 |
| D-3 | DR-15 更正引用 ＋ 加問 | ✅ **仍未送出** |
| **W-42** | Atlantis Mid 之範圍證據 | ✅ **(c) 獲強證據；(a)=0** |
| **W-43** | 階數維度之全量複核 | ⚠ **升級：可橋接，且現行對映有 12 列矛盾** |
| **W-41′** | Layer 3 左右對稱追因 | ✅ **非 037 遺漏，為歸屬問題** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 W-42 —— 29 包 §1 之八數重測

| 類 | 29 包 | 實測 | 判定 |
|---|---:|---:|---|
| 全部 reqid 皆為純 Mid | 112 | **112** | 符 |
| 部分 reqid 為純 Mid | 3 | **3** | 符 |
| 無 Mid | 121 | **121** | 符 |
| 無 reqid | 1 | **1** | 符 |
| **合計** | 237 | **237** | 符 |

family 分布：HeatedSeat **56**／VentedSeat **42**／HSW **8**／Common **6** —— **四數逐項相符**。

### 1.2 W-42(1) —— 四屬性並列對照

母體：純 Mid leaf 所引條文 **118**；無 Mid leaf 所引條文 **127**。

| 屬性 | 純 Mid（118 條） | 無 Mid（127 條） |
|---|---|---|
| `Radio` | `R1H`:118, `R1L`:118, `R1L-R`:118, `R1M`:118, `VP2R5`:47… | `R1L`:127, `R1L-R`:127, `R1H`:112, `R1M`:112, `VP4R7`:109… |
| `ECU` | `LTM`:118, `ETM`:118 | `LTM`:127, `ETM`:127, `CCDMR`:3 |
| `Market` | `All`:118 | `All`:127 |
| `Model Year` | 2021–2025 各 7, `Default`:1 | 2021 :36, 2022–2025 各 33, 2019:30 |

### 1.3 W-42(2) —— 關鍵判定

| 組 | `Radio` 含 `R1L`／`R1L-R` | `Radio` 為空 | `ECU` 為頭端 |
|---|---|---|---|
| **純 Mid** | **118 / 118（100%）** | 0 | **118 / 118（100%）** |
| 無 Mid | 127 / 127（100%） | 0 | 127 / 127（100%） |

**兩組在 `Radio`、`ECU`、`Market` 三個屬性上完全一致。**
純 Mid 之條文 **全部** 標記 `R1L` 與 `R1L-R`、**全部** 由頭端模組 `LTM`／`ETM` 執行。

> **此即 29 包 §1.1 之 (c)：架構標籤在此不具排他性。**
> 同一批 R1L／R1L-R 車型、同一批頭端模組，同時出現在 `Atlantis Mid`
> 與 `Atlantis High` 兩種標籤之下。**取證完畢，不裁定（屬 Pei，P20）。**

**旁證**（W-42(3) 讀出，非事後尋找）：純 Mid 之 `4859399` 與 `4859463`
**逐字為** `The requirements in this section are applicable for R1 Low only from SR22 and beyond.`
—— **標記 `Atlantis Mid` 之章節，其自身宣告適用於 R1 Low。**

### 1.4 W-42(3) —— 兩筆未讀條文之判定

`NEW ∪ Mid` 之 21 節內未覆蓋 **8** 筆（29 包記 8，**符**），
其中 11 輪已讀 6 筆、**未讀 2 筆**（符）。

| reqid | 章節 | EE Arch | 全文 | 判 |
|---|---|---|---|---|
| `4859399` | 1.3.3.3.3.1 | Atlantis Mid | `The requirements in this section are applicable for R1 Low only from SR22 and beyond.` | **(c)** |
| `4859463` | 1.3.3.3.5.1 | Atlantis Mid | 同上，逐字相同 | **(c)** |

**兩筆皆為章節適用性宣告，無可測內容 → (a) = 0，升級條件未命中。**
**「(a) = 0、母體 237 完整」至此完成舉證。**

### 1.5 W-43(1) —— Comfort 全母體之階數掃描

母體 **129**（29 包 §3 裁定之口徑，符）。明示階數者 **6 / 129**：

| Comfort leaf | 標記 | 節錄 |
|---|---|---|
| `SWE1-HVAC-054` | Multi-Level | `11.1 HVAC Popup Behavior HVS1. For Multi-Level Heated/Vented seats…` |
| `SWE1-HVAC-055` | Multi-Level | `11.2 HVAC Popup Behavior HVS2. For Multi-Level Heated/Vented seats…` |
| `SWE1-HVAC-062` | Multi-Level | `11.8 … W1HVS2.) For Multi-Level Heated steering wheel…` |
| `SWE1-HVAC-063` | **Single-Level** | `11.9 … R1HVS2.) For Single-Level heated steering wheel…` |
| `SWE1-HVAC-067` | Multi-Level | `12.1 Heated Seat Control HVS1. For Multi-Level Heated/Vented seats…` |
| **`SWE1-HVAC-068`** | Multi-Level | `12.2 Vented Seat Control HVS2. For Multi-Level Heated/Vented seats…` |

12 輪掃 17 個委派所引者得 5；**全母體掃得 6 —— 多出 `-068`，其未被任何委派引用。**

### 1.6 W-41′ —— 左右對稱

| 節 | 條文數 |
|---|---:|
| §1.3.2.1.3.1 LF Heated | **29** |
| §1.3.2.1.3.2 RF Heated | **29** |
| §1.3.2.1.3.3 LF Vented | 29 |
| §1.3.2.1.3.4 RF Vented | 30 |

**CFTS044 之左右兩節條文數相同（29 / 29）—— 來源規格對稱。**

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **升級：階數維度可橋接，但現行委派對映有 12 列直接矛盾**

W-43(2) 本側實測：237 個 Functional leaf 中 **98 個之 Layer 3 名稱已具名階數**
（`OneStageHeatedSeat` 14／`TwoStagesHeatedSeat` 20／`ThreeStagesHeatedSeat` 22／
`TwoStagesVentedSeatsManagement` 20／`ThreeStagesVentedSeatsManagement` 22）。

**兩份文件之階數維度確實存在且可對應** ——
故 08 包「**資料本身沒有可收斂之維度**」之結論**須撤回**（29 包 §2.1 已預期）。

**但橋接為粗粒度**：Comfort 側為二值（`Single` / `Multi`），
本側為三值（`One` / `Two` / `Three`）。
`Single ↔ One`、`Multi ↔ {Two, Three}` —— **無法分辨 Two 與 Three。**

**而現行 `delegation_lookup.tsv` 之對映與該維度直接矛盾。**
174 列 `delegate = yes` 逐列對照：

| 本側 Layer 3 階數 | 所引 Comfort leaf 之階數標記 | 列數 |
|---|---|---:|
| （無階數） | Multi | 62 |
| （無階數） | Multi \| Single | 28 |
| **One** | **Multi** | **12** ⚠ |
| Two | Multi | 32 |
| Three | Multi | 40 |

**12 列 `OneStage` 之 leaf，全部委派給標記 `Multi-Level` 之 Comfort 條文。**
該 12 列所引者逐字為 `SWE1-HVAC-054;…;-067;…`，
而 `-054`／`-067` 之開頭逐字為 **`For Multi-Level Heated/Vented seats`**。

**成因已查明且為上游事實**：

> Comfort 全母體 129 個 leaf 中，**唯一**明示 `Single-Level` 者為 `SWE1-HVAC-063`，
> 其主詞為 **`heated steering wheel`**。
> 以 `single[\s-]?level` 且含 `seats?` 交叉查詢，**命中 0**。
> —— **Comfort 側沒有任何「單階座椅」之條文。**

即：本 feature 之 14 個 `OneStageHeatedSeat` leaf（12 個已委派），
**其委派標的所描述的行為，明文排除單階座椅**。
**此為委派之實質缺口，非對映筆誤。** 處置屬分析層。

### 2.2 W-41′ —— 差 2 **不是 037 遺漏**，是歸屬

CFTS044 兩節皆 29 條，**逐位對照**（左第 k 條 ↔ 右第 k 條），
引用狀態不一致者恰 **2**：

| 位 | 左 | 右 | 內容（左右逐字同型） |
|---|---|---|---|
| 第 4 | `4858304` 已引 | **`4858334` 未被右側 leaf 引** | `the HU shall use $Heated_Seat_Levels$ to determine which levels are supported…` |
| 第 17 | `4858317` 已引 | **`4858347` 未被右側 leaf 引** | `For vehicles equipped with the Stop-Start feature, when the vehicle engine is not running…` |

**但該二條並非無人引用** —— 追其引用者：

```
4858334  ←  SWE1-VC-LeftFrontHeatedSeat-004
             reqid_list = 4858304;4858334;4858364;4858395
             section    = 1.3.2.1.3.1;1.3.2.1.3.2;1.3.2.1.3.3;1.3.2.1.3.4
4858347  ←  SWE1-VC-LeftFrontHeatedSeat-011
             reqid_list = 4858317;4858347;4858377;4858408
             section    = 1.3.2.1.3.1;1.3.2.1.3.2;1.3.2.1.3.3;1.3.2.1.3.4
```

**該二 leaf 各引四節、四側，是「四側共通」之需求，卻掛在 `LeftFrontHeatedSeat` 名下。**

**故 17 vs 15 之差 2 = 037 把兩條四側共通需求歸入左側。**
**非遺漏，升級條件未命中。**

> **對 framework 之後果**：該二 leaf 依其實質應屬 Layer 3 之 `Common Features`，
> 而非 `LeftFrontHeatedSeat`。`framework.md` 之 Layer 3 以 SWE ID 中段 token
> 機械切分，**會把它們放錯層**。已於 `framework.md` 記明，**未自行搬動**。

### 2.3 W-43(1) 之 6 vs 12 輪之 5

多出者為 `SWE1-HVAC-068`（`12.2 Vented Seat Control … For Multi-Level Heated/Vented seats`）。
**其未被任何 `delegate = yes` 之列引用** —— 故 12 輪掃 17 個委派所引者時看不見它。
兩數皆正確，**口徑不同**（129 全母體 vs 17 委派所引），依 29 包 §3 標明。

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | `DATA_REQUESTS.md` 之 DR-15 引用改正為四條正確 reqid 並加問配置維度；A-VS44 標明口徑並降 498／27／22 為證據；A-VS45 登記 |
| **核實無誤** | 29 包 §1 之八數（112／3／121／1／237 ＋ family 56／42／8／6）逐項相符；未覆蓋 8 筆、未讀 2 筆相符；Comfort 母體 129 相符；**(a) = 0，母體 237 完整至此完成舉證**；**CFTS044 左右兩節對稱 29/29** |
| **正確地不動** | **未修改 in-scope 判準、未動 R-VS19**（29 包 §1.1 明訂屬 Pei）；**未把 `LeftFrontHeatedSeat-004/-011` 搬到 `Common Features`**（framework 不鎖定，屬 Pei）；**未撤回 08 包之結論**（僅陳述其須撤回，裁定屬分析層）；**DR-15 仍未送出**；`A-VS02` 缺號維持 |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| CFTS044 區塊與章節 | 同 12 輪（`scripts/inscope_w39.py` 之 `blocks_with_sec()`）：`\d{7}\s*:\s*\[Artifact Type` 為界得 2,030；節號取自 heading 樣式段落之文字前綴 |
| **「純 Mid」之定義** | 該 leaf 之**全部** reqid，其 `[EE Architecture]` 值集合**含** `Atlantis Mid` **且不含** `Atlantis High`。部分成立者另計為「部分純 Mid」 |
| leaf → reqid | `data/leaf_to_reqid.tsv` 之 `CFTS044-(\d{7})`；一列可含多個，以 `;` 分隔 |
| 四屬性 | `Radio`／`ECU`／`Market`／`Model Year`，以 `,` 展開後去空白；**條文層級去重後計數**（非 leaf 層級） |
| W-43 階數形態 | `\b(one\|two\|three\|single\|multi)[\s-]?(stage\|level)s?\b`，不分大小寫。Comfort 側掃 037 `Analysis Report` 分頁各列全欄接合；本側掃 `leaves.tsv` 各欄接合 |
| W-43 本側階數歸屬 | 以 SWE ID 中段 token 之 `(One\|Two\|Three)Stages?` 判定，**非以描述文字判定**（描述為樣板，不具鑑別力） |
| W-41′ 左右對照 | 取 §1.3.2.1.3.1 與 §1.3.2.1.3.2 之區塊**依文件順序逐位配對**（各 29 條），比對「是否被同側 leaf 引用」。**未用文字相似度** —— 兩側描述為樣板，`difflib` 序列比對之中位相似度 0.98，不具鑑別力（已試，捨棄） |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS45** | DR-15（已更正引用） | 分析層於 17／18 包引 DR-15 之條文 id 錯誤（29 包 §2.2 指定登記） |
| **A-VS46** | **需新 DR，本層不代擬** | **Comfort 側無「單階座椅」條文**；12 個 `OneStageHeatedSeat` leaf 委派至明文限定 `Multi-Level` 之 Comfort 條文。⚠ 升級 |
| **A-VS47** | — | `LeftFrontHeatedSeat-004`／`-011` 為四側共通需求卻掛在左側名下，致 Layer 3 左右不對稱（17 vs 15） |

A-VS44 依 29 包 §3 標明口徑，**不新開**。
**無新開 DR** —— A-VS46 之提問屬分析層（不代擬條文）。DR-15 已更正但**仍未送出**。

### 5.1 D-3 —— 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **3**（A-VS45／46／47） | **46**（相異編號；最大號 A-VS47，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **0**（DR-15 為更正，非新開） | 不變 |

§5 表列 3 筆，登記簿逐筆核對皆在，**差額 0**。
**`A-VS02` 缺號維持，不補不重編**（12 輪已記明，29 包 §4 D-2 重申）。

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **W-43(2) 之橋接只證明「維度存在且粗粒度可對應」，未證明可逐 leaf 收斂。**
   `Multi` 涵蓋 `Two` 與 `Three` 兩者，**該二者無法藉此分辨**。
   08 包之 `0 / 174` 若重做（29 包預告之 W-44），
   **其上限為「14 個 OneStage 可分離、其餘 84 個仍不可分」** —— 未實測。

2. **A-VS46 只查了 `HeatedSeat`。**
   `OneStageVentedSeat` 於本 feature **不存在**（Layer 3 僅 Two／Three Stages Vented），
   故未生同樣問題。但 **`HeatedSteeringWheel` 側未查** ——
   Comfort `-063` 明示 `Single-Level heated steering wheel`，
   而本側 `HeatedSteeringWheel`(20) 與 `HeatedSteeringWheelManagement`(11)
   **之 Layer 3 名稱不帶階數**，其委派是否對得上，**本輪未驗**。

3. **W-42 之四屬性對照在條文層級去重，未看「同一 leaf 之多條 reqid 屬性是否一致」。**
   若某 leaf 之四條 reqid 分屬不同 `Model Year`，本表看不出來。
   `Model Year` 是唯一兩組有實質差異的屬性（純 Mid 各年 7 vs 無 Mid 各年 33），
   **該差異未追因。**

4. **`framework.md` 之 Layer 3 分層錯誤已知但未改。**
   §2.2 證明 `LeftFrontHeatedSeat-004`／`-011` 應屬 `Common Features`。
   **同型問題是否存在於其他 Layer 3（例如 Vented 側之四側共通需求），本輪未掃。**
   §1.6 之 RF Vented 為 **30 條**（其餘三節 29），該多出之 1 條亦**未追因**。
