# 26 包 —— 三項掃描（G131 / G132 / G133）

## G131 —— 逗號列舉規模（R-P192）

- 判準：冒號後（或 `In the following …:` 型）以逗號分隔**三項以上**者計一個列舉
- **出現次數 5**，分布於 **5 個 leaf**
- 抽樣：**1 / 5 = 20.0%**（≥ 16.7%），**種子 = 26**（`random.Random(26).sample`）
- **未擴充 G113 之辨識規則**（R-P192）

所在 leaf：`SWE-PM-013`、`SWE-PM-028`、`SWE-PM-041`、`SWE-PM-042`、`SWE-PM-103`

### 抽樣明細（判別欄由執行層人工填寫）

| leaf | 批次 | 列舉（截斷 90 字）| 項數 |
|---|---|---|---|
| `SWE-PM-028` | 003 | THENTLM has to set Timeout1 to the value specified by PROXI parameter “Switch_Off_Time” (f | 3 |

## G132 —— 適用性條件盤點（R-P193）

含品牌 / 車型 / 市場 / 配備條件之 leaf：**40 / 103**

| leaf | 批次 | 命中之條件詞 |
|---|---|---|
| `SWE-PM-057` | 002 | `PROXI`、`LTM High` |
| `SWE-PM-062` | 002 | `LTM High` |
| `SWE-PM-014` | 003 | `Jeep`、`LTM High` |
| `SWE-PM-015` | 003 | `PROXI` |
| `SWE-PM-016` | 003 | `PROXI` |
| `SWE-PM-017` | 003 | `PROXI` |
| `SWE-PM-019` | 003 | `PROXI` |
| `SWE-PM-021` | 003 | `PROXI` |
| `SWE-PM-026` | 003 | `Brand_Configuration_2`、`Jeep`、`PROXI` |
| `SWE-PM-028` | 003 | `PROXI`、`LTM High` |
| `SWE-PM-029` | 003 | `PROXI` |
| `SWE-PM-031` | 003 | `PROXI` |
| `SWE-PM-039` | 004 | `PROXI`、`LTM High` |
| `SWE-PM-044` | 004 | `Engineering Line` |
| `SWE-PM-046` | 004 | `PROXI` |
| `SWE-PM-053` | 004 | `Brand_Configuration_2`、`PROXI` |
| `SWE-PM-054` | 004 | `Brand_Configuration_2`、`Audio_Brand`、`SDARS_Presence`、`Beats` |
| `SWE-PM-055` | 004 | `$VC_VEH_LINE$`、`$VC_MODEL_YEAR$`、`$VC_SpecialPKG_IC$` |
| `SWE-PM-056` | 004 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$`、`Fiat Latam` |
| `SWE-PM-058` | 004 | `LTM High` |
| `SWE-PM-093` | 005 | `$DriverDoorOnOffSts$` |
| `SWE-PM-097` | 005 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$`、`Fiat Latam` |
| `SWE-PM-098` | 005 | `Fiat Latam`、`$Themed_Sound$` |
| `SWE-PM-099` | 005 | `Fiat Latam`、`$Themed_Sound$` |
| `SWE-PM-100` | 005 | `Fiat Latam`、`$Themed_Sound$` |
| `SWE-PM-101` | 005 | `Brand_Configuration_2`、`Audio_Brand`、`SDARS_Presence`、`Beats` |
| `SWE-PM-102` | 005 | `$VC_VEH_LINE$`、`$VC_MODEL_YEAR$`、`$VC_SpecialPKG_IC$` |
| `SWE-PM-108` | 005 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$`、`Maserati` |
| `SWE-PM-109` | 005 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$`、`Maserati`、`$Country_Code$`、`Market`、`$TBM_Present$` |
| `SWE-PM-110` | 005 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$`、`Maserati`、`$Country_Code$`、`Market`、`$TBM_Present$` |
| `SWE-PM-111` | 005 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$`、`Maserati`、`$Country_Code$`、`$TBM_Present$`、`screen sizes` |
| `SWE-PM-113` | 005 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$`、`Maserati`、`$Country_Code$`、`$TBM_Present$`、`screen sizes` |
| `SWE-PM-078` | 006 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$` |
| `SWE-PM-081` | 006 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$`、`Maserati`、`Jeep` |
| `SWE-PM-082` | 006 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$`、`Maserati`、`Jeep` |
| `SWE-PM-083` | 006 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$`、`Maserati`、`Jeep` |
| `SWE-PM-084` | 006 | `$VC_VEH_LINE$`、`PROXI` |
| `SWE-PM-085` | 006 | `$VC_VEH_LINE$`、`PROXI` |
| `SWE-PM-087` | 006 | `$VC_Veh_Brand$`、`$VC_VEH_BRAND$`、`$VC_VEH_LINE$` |
| `SWE-PM-088` | 006 | `$VC_VEH_LINE$` |

## G133 —— 重疊對掃描（R-P196）

- **門檻：Jaccard(實詞集合) ≥ 0.60**（實詞集合取自 `reverse_coverage.words()`，含詞幹化與停用詞移除）
- 重疊對合計 **27**：錨點集合**相同**者 **5**（已由 A-PW137 登記）、**不同**者 **22**（本條之對象）

### 錨點不同而內容重疊者

| leaf A | leaf B | 相似度 | A 之錨點 | B 之錨點 |
|---|---|---|---|---|
| `SWE-PM-041` | `SWE-PM-042` | **1.00** | `4941410,4941411,4941412,4941413` | `4941416,4941417,4941418,4941419` |
| `SWE-PM-080` | `SWE-PM-086` | **1.00** | `4942017` | `4942041` |
| `SWE-PM-109` | `SWE-PM-110` | **0.88** | `4941962` | `4941963` |
| `SWE-PM-098` | `SWE-PM-100` | **0.88** | `4941943` | `4941947` |
| `SWE-PM-028` | `SWE-PM-029` | **0.85** | `4941580,4941581,4941582` | `4941586,4941587,4941588,4941589` |
| `SWE-PM-027` | `SWE-PM-052` | **0.84** | `4941579,4941642` | `4941648` |
| `SWE-PM-047` | `SWE-PM-052` | **0.83** | `4941602` | `4941648` |
| `SWE-PM-027` | `SWE-PM-045` | **0.78** | `4941579,4941642` | `4941585` |
| `SWE-PM-106` | `SWE-PM-107` | **0.78** | `4941955` | `4941956` |
| `SWE-PM-045` | `SWE-PM-047` | **0.76** | `4941585` | `4941602` |
| `SWE-PM-047` | `SWE-PM-049` | **0.75** | `4941602` | `4941623` |
| `SWE-PM-049` | `SWE-PM-052` | **0.75** | `4941623` | `4941648` |
| `SWE-PM-091` | `SWE-PM-092` | **0.75** | `4942105` | `4942107` |
| `SWE-PM-023` | `SWE-PM-024` | **0.74** | `4941565` | `4941566` |
| `SWE-PM-018` | `SWE-PM-033` | **0.74** | `4941548` | `4941634,4941635` |
| `SWE-PM-084` | `SWE-PM-085` | **0.73** | `4942029` | `4942033` |
| `SWE-PM-027` | `SWE-PM-047` | **0.70** | `4941579,4941642` | `4941602` |
| `SWE-PM-081` | `SWE-PM-082` | **0.66** | `4942019` | `4942025` |
| `SWE-PM-027` | `SWE-PM-049` | **0.64** | `4941579,4941642` | `4941623` |
| `SWE-PM-024` | `SWE-PM-036` | **0.63** | `4941566` | `4941654` |
| `SWE-PM-045` | `SWE-PM-052` | **0.63** | `4941585` | `4941648` |
| `SWE-PM-066` | `SWE-PM-067` | **0.60** | `4941873` | `4941874` |

### 錨點相同者（A-PW137 已登記，列此以示未遺漏）

| leaf A | leaf B | 相似度 |
|---|---|---|
| `SWE-PM-054` | `SWE-PM-101` | 1.00 |
| `SWE-PM-055` | `SWE-PM-102` | 1.00 |
| `SWE-PM-056` | `SWE-PM-097` | 1.00 |
| `SWE-PM-068` | `SWE-PM-114` | 1.00 |
| `SWE-PM-070` | `SWE-PM-115` | 1.00 |
