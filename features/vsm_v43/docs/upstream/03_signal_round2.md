# 上繳包 03 — vsm_v43：W-5″ 擴充比對第二輪、SYSAD 拓撲實測、W-8 計數

日期：2026-09-01　執行層　對應下放包：`docs/handoff/03_signal_round2.md`
sha8 一律報 **`body_sha8`**（R-VT10(a)）。**R-VT1–R-VT10 本包已改自台帳讀取**
（台帳於上繳 02 後由他線重生，A-VT13 RESOLVED）；R-VT11／R-VT12 尚未入台帳，仍取樹外 `--out`。

---

## 〇、一句話結論

**W-5″ 六項、W-7、W-8 全數執行。E10″／E19／E20／E21／E22／E24 六項相符；E23 = 0 段，依判準所定路徑列 §K。**

| 項 | 結果 |
|---|---|
| 擴充比對第二輪 | `未解得(止於段1)` **113 → 108**；HMI Settings List 命中 **4**（v2 為 0）；PROXI `Format` 命中 **35**；LID 三欄 **25**（v2 一欄 24） |
| §K | **1 列** —— A-VT19：SYSAD 不含車輛網路拓撲，LTM 所在匯流排無從定 |
| 升級條件觸發 | **一項**：三名 PROXI 需第六條規則（重音 `ù`）方能命中 → **回報，不自創**（A-VT20） |
| B-1 衝突 | **0**（E22 ✅） |

**本包最實質的一個數字**：仍止於段 1 的 PROXI 有 9 名，但其中 **6 名是抽名偽陽性**（A-VT21），
**實質缺口只有 3 名，且全是同一個原因 —— 重音字元 `ù`**。
即 R-VT11(b) 之對象檔擴充，對 PROXI 類已近乎收斂（49 名中 40 已解、3 真缺口、6 偽陽性）。

## 一、結果三分法（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | W-5″ 六項；A-VT17 轉 RESOLVED；A-VT16 之但書部分依 R-VT12(a) 落實（兩弧不互為旁證）；v3 之偽陽性與該命中卻不中逐列標記 |
| 核實無誤 | E10″ **10/10**（且改自台帳讀取）；E24 = 0；R-VT11(d) 斷言於 SYSAD 抽取亦通過（`</?w:` = 0）；B-1 仍 0；`訊息名不符(R-13)` 仍 28，與 01／02 逐列相同 |
| 正確地不動 | **不自創第六規則**（A-VT20）；**不重抽名**（03 包明令）；v2 不覆寫；六個偽陽性**不刪**（母體數字在包間須可追）；`LOOKUP_MISSES.md` 仍未寫（三要件未滿足）；SYSAD **不通讀、不摘要全文**，僅限定詞搜尋＋圖說核對 |

---

## 二、W-5″ 逐項

### 1. LID 擴充比對對象欄：一欄 → 三欄（R-VT11(a)）

比對對象自 `Logical Identifier` 擴為 `Logical Identifier`／`Function`／`Object Text`
（LID 14 分頁逐頁定位表頭；三欄非空格 **5653**，正規化鍵 **4801**）。
命中記法已含欄名：`LID/{分頁}/r{列}c{欄}/{欄名}/{規則}`。

**實效：LID 擴充命中 24 → 25（＋1）。** 新增之欄只多解出一個名。
逐名列出「因新增欄而命中」者（5 名中僅 `Country_Code`／`Fuel_Type` 之命中欄為新增欄，
其餘三名原本即由 `Logical Identifier` 命中）：

| 規格原名 | 命中欄 | 位置 | 結果 |
|---|---|---|---|
| `Country_Code` | **function** | `CAN Mapping` r46c2 | PROXI路徑 |
| `Fuel_Type` | **function** | `Proxi & Configuration` r89c2 | PROXI路徑 |
| `BRAKE1.VehicleSpeedVSOSig` | **object text** | `CAN Mapping` r1736c3 | 解得（原已由 li 欄命中） |
| `STATUS_CCAN3.VehicleSpeedVSOSig` | **object text** | 同上 | 解得（同上） |
| `Cluster_Display_Type` | logical identifier | `Proxi & Configuration` r39c1 | PROXI路徑 |

> **回報**：R-VT11(a) 把 R-P368(b) 之「Description 欄」讀作 `Function`／`Object Text`，
> 本包照辦。**實測其邊際效益為 +1 名** —— 兩個新欄各解出一名（`Country_Code`／`Fuel_Type`，
> 且二者本就會由 PROXI `Format` 命中，故對最終結果分布之淨貢獻為 **0**）。
> 據實回報，不因效益低而略過或誇大。

### 2. HMI Settings List R1 SR25 —— 表頭實測與設定項名欄

**表頭實測**（分頁 `Settings`，共 1015 列）：

| 列 | 內容 |
|---|---|
| r1／r2 | 說明文字（非表頭） |
| **r3（表頭列）** | `A = List Item`、`D = Template`、`E = Options (American English)`、`F = Technical Reference (CFTS/VF)`、`G = Notes`、`H = Info Popup`、`I = Graphics - NAFTA` |
| **B／C** | **無表頭文字** —— 實為 `List Item` 之縮排層級欄 |

**「設定項名」欄之判定（回報欄名與列數）**：
`A` 欄非空 393 列，但其值為 `1`／`3`／`1. KeySense (…)` 之**序號**，非設定名。
設定名實際落在 **B（第二層）與 C（第三層）**：A 持序號時名在 B，B 持子序號（`1.1`）時名在 C。
故本包取 **B／C 兩欄之非純數字文字**為設定項名：**623 個（相異 407）**，正規化鍵 **407**。
（判定依據：r5 `A=1`／`B=Automatic Emergency Braking*`；r6 `B=1.1`／`C=Forward Collision Warning*`。）

**命中 4 名**（E20 ✅ > 0）：

| 規格原名 | HMI 設定項 | 位置 | 亦命中 PROXI | v3 結果 |
|---|---|---|---|---|
| `Cornering_Lights` | `Cornering Lights` | `Settings` r? B/C | 否 | **UI路徑(R-P375b)** |
| `Auto_Park_Brake_Menu` | （見 TSV 備註） | 同上 | **是** | PROXI路徑（雙路徑，見下） |
| `Geolocation_Menu` | 同上 | 同上 | **是** | PROXI路徑（雙路徑） |
| `Side_Distance_Warning` | 同上 | 同上 | **是** | PROXI路徑（雙路徑） |

> **R-P375(b) 之雙路徑已逐列落實**：四名中三名同時命中 HMI 與 PROXI。
> 依 R-P375(b)「二者皆命中時，Procedure 用 UI、Pre-Condition 用 PROXI，各引其列」，
> v3 之備註欄記 `【R-P375(b) 雙路徑】UI："<設定名>"（HMI Settings r{列}{欄}）／
> PROXI：`<參數名>`（Format r{列}c{欄}）—— Procedure 用 UI、Pre-Condition 用 PROXI`。
> 結果欄仍記 `PROXI路徑(R-P375b/c)`：**02 包所定之值域無「雙路徑」一值，本包不自行擴充值域**，
> 資訊改由備註承載。**提請下包**：值域是否增列 `UI+PROXI 雙路徑`。

### 3. PROXI_HDCC27_R3 `Format` —— 表頭實測與命中

**表頭實測**：分頁 `Format`，**表頭列 2**，`A = Parameter Group`、`B/C = Start/Stop Byte`、
`D/E = Start/Stop Bit`、**`F = Parameter Name`**、`G = Annotation`、`H = Coding`、`I = Table`、`J = Offset`。
`Parameter Name` 非空 **1058**（相異 1052），正規化鍵 **1045**。

**命中 35 名**（v2 逐字式為 35；本輪以五規則比對後仍為 35，但命中之依據改為規則式並逐列記位置）。
v3 `PROXI路徑(R-P375b/c)` 由 35 增為 **39**。

### 4. 「該命中卻不中」表（03 包 §三-4；不擅自判等同）

近似比對（`difflib`，門檻 0.86，對象為 HMI 與 PROXI 之全部正規化鍵）產出四筆，
去除偽陽性後**三筆為真**，且**同一成因**：

| 規格原名 | 五規則後之鍵 | 表內最近值 | 檔／欄 | 差異 |
|---|---|---|---|---|
| `DRL_Menù_Enable` | `drl menù enable` | `DRL_Menu_Enable` | PROXI `Format`／`Parameter Name` | **`ù` vs `u`** —— 規則 5 之 `_Menu` 因此不生效 |
| `Greeting_Lights_Menù` | `greeting lights menù` | `Greeting_Lights_Menu`／HMI `Greeting Lights` | PROXI／HMI Settings | 同上 |
| `Horn_Chirp_Menù` | `horn chirp menù` | `Horn_Chirp_Menu` | PROXI `Format` | 同上 |

**需第六條規則（Unicode 去重音）方能命中 → 依 03 包 §七回報，不自創。**
三列於 v3 維持 `未解得(止於段1)`，備註逐列標明最近值與差異。登 **A-VT20**。
旁證：規格自身即拼法不一（`Horn_Chirp_Menu` 與 `Horn_Chirp_Menù` 並存）→ **DR-VT2 之新增佐證**。

### 5. `data/signal_chain_v43_v3.tsv`（v2 不覆寫）—— 同母體（230）分布差

| 結果 | v2 | **v3** | 差 |
|---|---|---|---|
| 解得 | 41 | **41** | 0 |
| 訊息名不符(R-13) | 28 | **28** | 0 |
| **B-1 衝突** | 0 | **0** | 0 |
| 未解得(止於段2) | 13 | **13** | 0 |
| **未解得(止於段1)** | 113 | **108** | **−5** |
| **UI路徑(R-P375b)** | 0 | **1** | **+1** |
| PROXI路徑(R-P375b/c) | 35 | **39** | **+4** |
| 查無(R-G13) | 0 | **0** | 0 |
| 合計 | 230 | **230** | — |

**`未解得(止於段1)` 之類別拆解**

| 類別 | v2 | **v3** | 差 |
|---|---|---|---|
| 內部 | 83 | **83** | **0** |
| CAN | 16 | **16** | 0 |
| PROXI | 14 | **9** | −5 |

> **這張表是本包最重要的結論**：對象檔擴充把 PROXI 類從 14 收到 9（其中 6 為偽陽性，實質剩 3），
> 但**內部訊號 83 名一個都沒動**。HMI Settings List 與 PROXI `Format` 皆不收 `X.Req` 形之名。
> 上繳 02 §八-1 之判斷（瓶頸在缺對照表，不在比對規則）**於本輪再次獲證**：
> 這次連對象檔都擴了，內部訊號仍紋風不動。**DR-VT4 是唯一出路。**

### 6. 兩弧之處置（R-VT12(a)）

`BRAKE1.VehicleSpeedVSOSig` 與 `STATUS_CCAN3.VehicleSpeedVSOSig` 兩列
**各記「解得」**，備註之「旁證」字樣**已刪**，改註
`R-VT12(a)：本規格同載兩名，為兩條弧線各自解析；兩弧，主旁待 W-7（SYSAD）`。
**主旁未定**（W-7 結果見 §三）。

---

## 三、W-7 —— SYSAD 拓撲實測（限定範圍，未通讀）

抽取：`sources/raw/vf665_sysad_sys3/…SYSAD_v1.0.docx` → `word/document.xml`，
**1332** 個非空段落；**R-VT11(d) 斷言通過**（輸出 `</?w:` 出現數 = **0**）。

**目標詞之段落命中數（全 0，僅 `LTM` 兩處且皆非架構節點）**

| 詞 | 命中 | 詞 | 命中 |
|---|---|---|---|
| `BH-CAN`／`BHCAN`／`CAN-BH` | **0** | `STATUS_CCAN3` | **0** |
| `FD-CAN`／`FDCAN` | **0** | `BRAKE_FD_2` | **0** |
| `BCM` | **0** | `VehicleSpeedVSOSig` | **0** |
| `gateway`／`Gateway` | **0** | `node`／`Node` | **0** |
| `topology`／`匯流排` | **0** | `LTM` | 2（一為 SYSRA 檔名、一為功能清單句） |

**佐證段落（3 段，各 ≤ 15 words 摘句，含節號）**

1. **§4.5 假設與相依性 Assumptions and Dependencies** — `Vehicle buses (CAN/LIN/Ethernet)`
2. **§4.7 架構設計組件 Architectural Design Components** — `CAN Bus Interface: Communication with the VHAL.`
3. **§4.3 系統需求–概述 System Requirements – Overview** — `…CAN signals … are maintained in SYS2 requirements`
   （§6 參考文檔重申：`CAN Signal Mapping … maintained in corresponding documents`）

**結論：不是「遺漏」，是文件類別不符。**
SYSAD 為 **Android/AOSP 軟體架構**文件，其鏈為
`Vehicle Settings App(1st Party Apps) → CarPropertyManager → CarPropertyService → VHAL → VCPU → (CAN/LIN Bus)`
（§5 Interface Description）。它描述 HU **內部軟體層**，不是車輛網路拓撲；
`LTM`／`BCM` 從未作為架構節點出現。

**圖面亦已核對（非通讀）**：12 個嵌入媒體，圖說 Figure 1–12 全為軟體架構圖與序列圖
（`System Architectural Interface Model`、各 `Sequence Diagram`），**無網路拓撲圖**。
抽樣開啟 `image2.png`（Figure 1／11）核對：內容為 `MCPU` 框內之
`1st Party Apps／CarPropertyManager／CarPropertyService／VHAL` 與框外 `VCPU`，
**無任何匯流排名稱或車輛 ECU 節點**。

**E23 = 0 段 → 依 03 包 W-7 之明文「記『SYSAD 未載』，列 §K 交 Pei」，其餘續行。**
登 **A-VT19**；**A-VT16 維持 PENDING**（但書部分已由 R-VT12(a) 結，主旁待另一來源）。

---

## 四、W-8 —— SYSRA `Polarion`／`_polarion` 分頁計數（只計數不分析）

| 分頁 | 總列 | 資料列（表頭 1，任一欄非空） | 欄數 | 表頭 |
|---|---|---|---|---|
| `Basic Report` | 1282 | **1280** | 83 | r1（`ID`／`SYS2 …`） |
| `Polarion` | 88 | **86** | 2 | `Property`／`Value` |
| `_polarion` | 1299 | **1295** | 6 | r3 為 `Type`／`Label`／`ID`／`Field` |

**與 `Basic Report` 之 ID 交集**（`Basic Report` A 欄 `ID` 相異 **1280**）：

| 分頁 | 交集最大之欄 | 交集數 | 該欄相異值數 |
|---|---|---|---|
| `Polarion` | 第 1 欄（`Property`） | **0** | 86 |
| `_polarion` | 第 1 欄（`Type`） | **0** | 1290 |

（掃描條件：對前 6 欄逐欄取相異非空值與 `Basic Report` 之 `ID` 集合求交，取交集最大者；**六欄皆為 0**。）

兩分頁之值為 Polarion 匯出之**設定與欄位對映中繼資料**（如
`New Work Item Type / task`、`NR1L/SYS2_System Requirements Anal | Heading | J.Category001 | 20206`），
**與需求 ID 無交集**。**只計數，不分析。**

---

## 五、E 對照（相符者亦列，不符不調和）

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| E10″ | R-VT1–R-VT10 `body_sha8` 與上繳 02 §三逐字相同 | 全同 | **10/10 相同**（且已改自**台帳**讀取，非樹外） | ✅ 相符 |
| E19 | v3 對 v2 同母體（230）`未解得(止於段1)` < 113 | < 113 | **108**（差 **−5**） | ✅ 相符 |
| E20 | HMI Settings List 命中 > 0 | > 0 | **4** | ✅ 相符 |
| E21 | v3 `UI路徑(R-P375b)` > 0 | > 0 | **1**（另 3 名同時命中 PROXI，依 R-P375(b) 記雙路徑於備註） | ✅ 相符 |
| E22 | B-1 衝突 | 0 | **0** | ✅ 相符 |
| E23 | W-7 SYSAD 命中段落 1–3 段 | 1–3；0 → 記未載並列 §K | **0 段** | ⚠ **走 0 段之判準路徑**：記未載、列 §K（A-VT19） |
| E24 | v3 之 `</?w:` 出現數 | 0 | **0** | ✅ 相符 |

**E10″ 逐條**：`R-VT1 93666dae`／`R-VT2 a6acf352`／`R-VT3 d3823bca`／`R-VT4 9844b823`／
`R-VT5 e8e8724b`／`R-VT6 8db4c81b`／`R-VT7 9b4427c5`／`R-VT8 2b3fcbe6`／
`R-VT9 0f1a1f3f`／`R-VT10 fa2558ff` —— **十項全同**。

### R-VT11／R-VT12 之 `body_sha8`

| 條號 | 一句話 | `body_sha8` | `sha8`（觀測） | 來源：列 | 本體列數 |
|---|---|---|---|---|---|
| R-VT11 | 段 1 擴充比對之對象欄與對象檔；OOXML 抽取自驗 | **`45eb10ea`** | `8d35060b` | `features/vsm_v43/RULINGS.md`:155 | 12 |
| R-VT12 | R-VT9(b) 但書；HU 匯流排依 SYSAD；母體可變之指標採同母體差 | **`ed51f088`** | `24c1e640` | 同上:170 | 11 |

**來源揭露**：R-VT1–R-VT10 取自 `docs/fw036/RULINGS.sha.tsv`（台帳，10 列齊備）；
**R-VT11／R-VT12 尚未入台帳**，取樹外 `rulings_hash.py --out`（R-VT10(a) 裁可）。
台帳下次重生後應複驗此二值。

---

## 六、§K —— 交 Pei 之項（1 列）

| # | 項 | 依據 | 建議處置 |
|---|---|---|---|
| K-1 | **SYSAD 不含車輛網路拓撲，LTM 所在匯流排無從定** —— 兩弧（`BRAKE1.*`／`STATUS_CCAN3.*`）之主旁因此未定 | 03 包 W-7「未載則列 §K」；R-VT12(b) | 改自 **SYS2 之 CAN Signal Mapping** 取（SYSAD §4.3／§6 兩處自指該處），或逕以 LID `CAN` 欄之 `Atlantis High` 欄組為準 |

**另有一項雖非 §K 但同屬升級條件**（03 包 §七第 3 條）：
三名 PROXI 需第六條規則方能命中（A-VT20）—— 已回報、未自創，見 §二-4。

---

## 七、anomaly／DR 清單

### 狀態變更

| id | 變更 | 依據 |
|---|---|---|
| A-VT16 | 但書部分**結**（R-VT12(a)：兩弧各自解析、不互為旁證，v3 已落實）；**主旁未定，維持 PENDING** | W-7 實測 SYSAD 未載（A-VT19） |
| A-VT17 | PENDING → **RESOLVED** | R-VT12(c)：同母體 97 < 102 判相符，113 為觀測值 |

### 本包新登

| id | 一句話 | 狀態 | 配對 DR |
|---|---|---|---|
| A-VT19 | SYSAD（SYS3 v1.0）為 AOSP 軟體架構文件，不含車輛網路拓撲；12 圖亦無 | PENDING（**§K K-1**） | — （來源選擇之裁決，非上游索資） |
| A-VT20 | 三名 PROXI 需第六規則（重音 `ù`→`u`）方能命中；回報不自創 | PENDING | 併 **DR-VT2**（上游拼法不一之新增佐證） |
| A-VT21 | 抽名之六個偽陽性名（`CAN Node …`×3、`Component`／`Impact`／`Implementation`） | RESOLVED（v3 逐列標記，不刪不重抽） | — |

### 未結 DR（本包未動 `DATA_REQUESTS.md`，未送）

| DR | 項目 | 阻塞 | 狀態 | 本包新增之佐證 |
|---|---|---|---|---|
| DR-VT1 | V43 之 037 缺件 | **yes** | 建議送出 | 差集仍待 vsm_v42 |
| DR-VT2 | SYSRA DocID／版次／Melco ID／拼法 | no | 未送出 | **A-VT20 之重音三名**（`Menù` vs `Menu`） |
| DR-VT3 | 規格訊息名與 forms/ DBC 不符 28 列 | no | 建議送出 | 28 列於 v3 未變，逐列依據仍在備註欄 |
| DR-VT4 | 內部訊號驅動／觀察對照總表（83 名） | no（P4 起 yes） | 建議送出 | **對象檔擴充後內部訊號 83 名零變動**（§二-5）—— DR-VT4 之必要性再獲證 |

---

## 八、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 503
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）

總判：**FAIL** —— 4 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths
依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。
```

| 閘 | 與本包之關係 | 歸因 |
|---|---|---|
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 計數 **503**（上繳 02 時為 502）。將本包**全部產出**（`ANOMALIES.md` 還原至 HEAD、`docs/upstream/03_signal_round2.md` 與 `data/signal_chain_v43_v3.tsv` 移出樹外）後重跑，**仍為 503** → 本包貢獻 **0**。502 → 503 之 +1 來自他線：實測 `git status` 顯示 `features/vsm_v42/`（`RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／`DECISIONS.md`／`feature.yaml`）於本包執行期間同時處於未提交修改 |
| `rulings_hash` | **相關** | 台帳現含 R-VT1–R-VT10（十列，E10″ 即據此），**R-VT11／R-VT12 尚未入**，另缺 vsm_v42 之 R-VL 列。該檔於本包執行期間再度處於 `M`（他線作業中）。**本線不重生**（R-VT8(a)） |
| `gates_tsv` | **無關** | 差異列全屬 `lint036`／`driver_distraction`／`ics_management`／`lint_docs036` |
| `lint_paths` | **無關** | 紅項全在 `driver_distraction/workbook/`、`ics_management/delivered/`、`sw_update/delivered/` |

依 FO 之第 8.2 節／26 包 §C 裁定 2：**本包附本節之升級說明上繳**。

---

## 九、獨立判斷（「本包是否仍有該驗而未驗者」）

1. **內部訊號 83 名在本輪「零變動」，這是一個結論而不只是一個數字。**
   上繳 02 說瓶頸在缺對照表；本包把對象檔從 LID 一本擴到三本、對象欄從一欄擴到三欄，
   **內部訊號仍是 83 → 83**。三次擴充（規則、欄、檔）全部無效，
   已足以認定**這不是比對問題**。DR-VT4 不送，本線 P4 起就會有 83 條 `PENDING: DR-` 佔位（R-P355(c)）。
   **建議把 DR-VT4 從「建議送出」升為與 DR-VT1 同級的優先項。**

2. **PROXI 類已近收斂，但收斂之後才看得見抽名的髒。**
   49 名中 40 已解、3 真缺口、**6 偽陽性**。偽陽性佔仍未解者的三分之二 ——
   在 v2 那個「14 未解」的數字裡，這個比例是看不出來的。
   **教訓**：母體數字在解析率提高之前無法自證品質；下包重抽名時，
   建議同時報「抽名偽陽性率」而不只報母體大小。

3. **有：`Technical Reference (CFTS/VF)` 欄未被利用。**
   HMI Settings List 之 `F` 欄載 `VF230/665`、`CFTS019` 等 —— **本 feature 正是 VF665**。
   以該欄先篩出屬於 VF665 之設定項再比對，可能比純字串正規化更準，
   且能給 R-P375(b) 之 UI 路徑一個**來源錨點**（R-P353 之白名單 (ii) 需要具名 UI 元件）。
   本包**未做**（03 包只令對「設定項名欄」施五規則）。**提請下包納入。**

4. **W-7 的結論其實回答了一個更早的問題。**
   R-VT2 之「待 recon 查證」與 R-VT12(b) 都把 LID `Atlantis High` 欄組適用性寄望於 SYSAD。
   本包實測 SYSAD 根本不是那一類文件 —— **這條路是斷的**，
   而 SYSAD 自己兩處指向 SYS2 之 CAN Signal Mapping。
   建議把「LID 欄組／匯流排」一題直接改綁 SYS2，不要再等 SYSAD。

5. **本包未驗而下放包亦未要求者**：
   (a) HMI Settings List 之 `Brand-Specific Names` 分頁（1001 列）完全未用 ——
       其 `Jeep / Chrysler / Ram / Dodge` 等品牌別名可能是 UI 元件實名之來源；
   (b) SYSAD 之其餘 11 張圖未開（只開了 Figure 1／11 之 `image2.png` 作抽樣）；
   (c) `forms/LOOKUP_MISSES.md` 仍未寫入（R-VT10(c) 三要件未滿足，**本應不寫**，記明以免誤為漏做）；
   (d) v3 之 `未解得(止於段2)` 13 列未再往前推 —— 其段 2 有 `MESSAGE.Signal` 而段 3 查無，
       依 R-P368(d) 應可判「查無」，但三要件之第三項（登 `LOOKUP_MISSES.md`）未滿足，故仍記段 2。

---

## 十、禁區遵守聲明（00 包 §零）

| 禁區 | 遵守 |
|---|---|
| 1. git 一律不動 | 本包未跑任何 `git` 寫入指令 |
| 2. 不寫 `features/vehicle_setting/`、`features/vsm_v42/` | 未寫、未讀 |
| 3. 不寫 `docs/runtime/profiles/` | 未寫 |
| 4. 不改寫 `sources/raw/` 原檔 | 全程唯讀（SYSAD 與 SYSRA 之讀取皆 `read_only`／`zipfile` 讀） |
| 5. 不以 SYSRA 或規格代 037 建母體或生成 TC | 未建、未生成；`generated/`／`batches/` 仍空 |
| 6. 不自行送 DR | 未送、未改 `DATA_REQUESTS.md` |

本包寫入之檔（全在 `features/vsm_v43/` 之下）：
`ANOMALIES.md`（改）、`data/signal_chain_v43_v3.tsv`（新）、`docs/upstream/03_signal_round2.md`（新）。
`RECON.md`、`feature.yaml`、v1／v2 TSV、`sources/`、`forms/`、`docs/fw036/`、`scripts/` **未寫入**。

---

## 十一、下一步

1. **Pei：§K K-1** —— LTM 匯流排改自 SYS2 CAN Signal Mapping 或 LID `Atlantis High` 欄組（A-VT16 之主旁待此）
2. **Pei：A-VT20** —— 是否增訂第六規則（Unicode 去重音），或由 DR-VT2 要求上游統一拼法
3. **Pei（累計四包未動）**：commit；共用腳本一裁（五項）；DR-VT1／VT2／VT3／VT4 四項併送
   —— **建議 DR-VT4 升為與 DR-VT1 同級**（§九-1）
4. 下包：`Technical Reference (CFTS/VF)` 欄之利用（§九-3）；抽名重做並報偽陽性率（§九-2）；
   值域是否增列「UI+PROXI 雙路徑」（§二-2）
5. vsm_v42 之 W-0 → 台帳含 R-VL／R-VT11–12 → 複驗二值；`signal_chain_v42.tsv` → 補差集
6. P3：framework Layer 1 鎖定、profile、`spec_reference_template` 定案
7. 037 到齊 → 母體建檔 → Layer 2 → P4
