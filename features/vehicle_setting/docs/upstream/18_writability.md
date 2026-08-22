# 上繳 18 —— 全量可寫性掃描（237 leaf）

執行層寫入。依據：`docs/handoff/39_review_round19.md` §6。canon §8.2 六節。

> **編號更正**：39 包 §6 之 D-1 指定 `docs/upstream/17_writability.md`，
> 惟 **`17_batch01_v3_and_batch02.md` 已於 19 輪佔用該號**。
> 本輪改用 **18**，不覆蓋既有檔（R-TM13：不刪不覆）。**不自行調和編號**，於此記明。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅（改號，見上） |
| D-2 | 逐字轉錄 R-VS42 | ✅ |
| D-3 | DR-8／12 補登記；三類別式；三項併入 | ✅ |
| D-4 | A-VS66 新開 ＋ 兩數 | ✅ 見 §5.1 |
| **W-58** | 全量可寫性掃描 | ⚠ **升級：writable = no 88 條（37.1%）> 40** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 (a) **本 feature 之實際可交付量** —— 此前未曾量過

| 項 | 值 |
|---|---:|
| 母體 | **237** |
| **writable = yes** | **149** |
| **writable = no** | **88（37.1%）** |

**⚠ 升級條件命中**：逐字為「writable = no 者超過 40 條（即 >17% 之母體）」，
實測 **88 條 / 37.1%**。

### 1.2 (b) 四類之分布

| 類 | 命中次數 | 涉及 leaf |
|---|---:|---:|
| **B1** 未具名之外部交叉參照 | 8 | **8** |
| **B2** 規格值於 LID／DBC 皆無對應 | 104 | **82** |
| **B3** PROXI／參數於 LID 三處無命中 | 2 | **2** |
| **B4** 其他 | **0** | **0** |

**B4 = 0 → 「B4『其他』類非 0」之升級條件未命中。**

B2 之主要 token：`Hybrid_Type` 14／`EngRun_Stat` 12／`PowerMode` 10／
`DriverSide` 6／`HeatedSeatFL`・`HeatedSeatFR`・`VentedSeatFL`・`VentedSeatFR` 各 6／
`PrplsnSysAtv` 5／`HSW_Stat_2` 5／`HdRstRelRq` 4／`Heated_Seat_Levels` 4。

B1 之 8 條相異條文：`4858560`／`4859509`（`as defined by HMI requirements`）、
`4859032`（`follow the HMI Logic & Flow`）、
`4859386`／`4859387`／`4859448`／`4859449`／`4859498`（`TLM has to show an informative popup …`）。

B3 之 2 條：`ThirdRowHeadrestDump-028`（`VC_HdRstPrsnt`）、
`HeatedSteeringWheel-004`（`HSW_StatS` —— **實為來源 `$` 不對稱之 typo**，見 §2.3）。

### 1.3 (c) token 全集重建

| 項 | 值 |
|---|---:|
| 原 `spec_variables.tsv` | **30** |
| 重建後（識別碼形態過濾後） | **31** |
| **新增** | **5** |
| 其中**真為 token 者** | **3** |

新增五者逐一具名：

| token | 條文 | leaf | 判 |
|---|---:|---:|---|
| `Cooled_Seats` | 2 | 2 | **真** —— `4858264` 寫 `Left Front Vented Seat Cooled_Seats = Front Seats…`（**裸名**），`4858295` 寫 `$Cooled_Seats$`。**即 A-VS40 之 token** |
| `FL_HS_Cmd_Tlm` | 1 | 1 | **真** —— `4859363` 寫 `TELEMATIC_CLIMATE_SETUP.FL_HS_Cmd_Tlm = "Pressed"`（`message.signal` 形態） |
| `VC_HdRstPrsnt` | 1 | 1 | **真** —— A-VS64 |
| `RVC` | 2 | 2 | **非 token** —— `internal signal RVC IMAGE ON/OFF`，為內部訊號片語（§8.7.5(d) 不阻塞） |
| `HSW_StatS` | 1 | 1 | **非 token** —— 來源 `$` 不對稱（A-VS68） |

**新增 5 ≤ 10 → 「重建後 token 數較原 30 增加超過 10」之升級條件未命中。**

原有而本次未命中者 **4**：`HSW_StatFailSts`／`Heated_Seats_Levels`／
`Heated_Steats_Levels`／`TGW_DISP_STAT` —— 其於 237 leaf 所引之條文中未以
「token ＋ 比較運算子 ＋ 方括號值」形態出現（見 §6-2）。

### 1.4 掃描之交叉驗證 —— **6 / 6 相符**

以 17／19 輪已知之 6 條阻塞 leaf 反查本掃描：

| leaf | 期望類 | 掃描結果 | |
|---|---|---|---|
| `Stop-StartSystem-006` | B2（EngRun_Stat） | `no` / B2 | ✅ |
| `SwitchLHD/RHD-010` | B1（4858560） | `no` / B1\|B2 | ✅ |
| `ThirdRowHeadrestDump-028` | B3（VC_HdRstPrsnt） | `no` / B3 | ✅ |
| `ThirdRowHeadrestDump-029` | B2（IGN_START） | `no` / B2 | ✅ |
| `ThirdRowHeadrestDump-031` | B2（IGN_OFF_ACC） | `no` / B2 | ✅ |
| `ThirdRowHeadrestDump-039` | B1（4859032） | `no` / B1\|B2 | ✅ |

**已知阻塞 6 條全數被掃出。**

### 1.5 各 Layer 3 之可寫率

| Layer 3 | 可寫 / 總 | % |
|---|---:|---:|
| `ThreeStagesHeatedSeat` | 22 / 22 | 100 |
| `ThreeStagesVentedSeatsManagement` | 22 / 22 | 100 |
| `OneStageHeatedSeat` | 14 / 14 | 100 |
| `StopStartSystemBehavior` | 3 / 3 | 100 |
| `PHEVFeatures` | 1 / 1 | 100 |
| `HeatedSteeringWheelManagement` | 10 / 11 | 91 |
| `TwoStagesHeatedSeat` | 18 / 20 | 90 |
| `TwoStagesVentedSeatsManagement` | 18 / 20 | 90 |
| `ScreenOFF` | 5 / 6 | 83 |
| `ThirdRowHeadrestDump` | 11 / 21 | 52 |
| `Stop-StartSystem` | 3 / 6 | 50 |
| `HeatedSteeringWheel` | 9 / 20 | 45 |
| `FeaturesEnableCriteria` | 1 / 3 | 33 |
| **`LeftFrontHeatedSeat`／`RightFrontHeatedSeat`／`LeftFrontVentedSeat`／`RightFrontVentedSeat`** | **各 3 / 15** | **20** |
| **`SwitchLHD/RHDConfiguration`** | **0 / 6** | **0** |
| **`CrossZone Common`** | **0 / 2** | **0** |

**四個單側座椅 Layer 3（60 leaf）之可寫率僅 20%** —— 其為 B2 之主要集中處。

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **B1 初測 65 條，逐條讀後只有 8 條是真阻塞 —— 我的判準過寬**

初測判準：`as defined by`／`as defined in`／`refer to`／`refer the`／`follow the`／
`per the`／`as specified by`／`according to` ＋ 條文內未帶文件名或章節號。得 **65 個相異條文**。

逐條讀後分為兩型：

| 型 | 數 | 例 |
|---|---:|---|
| **尾綴修飾**（參照之前已有具體結果動詞） | **57** | `the left front heated seat switch, shall be shown as greyed-out, **per the HMI**` —— 結果（greyed-out）已具體，參照只修飾其呈現細節 |
| **整個結果被外推**（參照之前無結果動詞） | **8** | `the HMI shall be modified **as defined by HMI requirements**` —— 無任何具體結果 |

**尾綴修飾不阻塞。**

> **若止於初測，本包會報 writable = no **117 條（49.4%）** 而非 88（37.1%），
> 並把 **57 個實際可寫之 leaf** 誤列為阻塞。**
> **與 A-VS39（分析層之 in-scope 判準漏 ECU／Radio）同型，本次犯者為執行層。** → A-VS67

### 2.2 ⚠ **B2 標記了 6 條「已寫出且已放行／已交付」之 leaf —— 三種成因須分開裁**

| leaf | 狀態 | B2 之理由 | 判 |
|---|---|---|---|
| `Stop-Start-004`／`-005` | batch01_v3 已放行 | `EngRun_Stat` 四值 | **標記正確** —— 該二條本就帶 `PENDING: DR-19` |
| `ThirdRowHeadrestDump-032`／`-038` | batch02 已交付 | `IGN_RUN` 不在 DBC 值域 | **可解**：CFTS044 於**他條文**寫 `[4h:Ignition run]` 5 次，**來源自載原始碼值**。本掃描以**單條文**為單位比對，看不見跨條文之錨點 |
| `SwitchLHD/RHD-009`／`-011` | batch01_v3 已放行 | `[Right Drive]` 不在 LID 值域 | **需裁** —— 見 §2.3 |

**掃描之界線已記明**：`value_matched()` 只在**該值自身**帶 `Nh:` 時credit 原始碼值，
**不做跨條文之錨點聚合**。故 `-032`／`-038` 為**掃描之假陽性**。
若計入該二條，writable = yes 為 **151**。**本層不逕自調整計數**，兩數並列。

### 2.3 ⚠ **`[Right Drive]` 之對映是我做的判斷，而它已在放行的 TC 裡**

CFTS044 全文之 `$DriverSide$` 值：

| 值 | 次數 | 有 `Nh:` 錨點？ |
|---|---:|---|
| `[Right Side]` | 10 | — |
| `[Left Side]` | 7 | — |
| **`[Right Drive]`** | **4** | **無** |
| `[1h: Right Side]` | 4 | **有** |
| `[Right hand drive]` | 2 | 無 |
| `[0h: Left Side, 1h: Right Side]` | 2 | **有** |
| `[1h: Right hand]` | 1 | **有** |

17 輪之 `SwitchLHD/RHD-009`／`-011`（**已由 pilot review 放行**）以
`PROXI Driver_Side = 1 (Right Side)` 承載條文之 `[Right Drive]`。

**我的依據**：該 token 之值域為**二值**且已由 `1h: Right Side` 錨定；
`Right Drive` 非 `Left Side`，故為 `Right Side`。**這是二值域之演繹，不是發明。**

**與 `IGN_START → START` 之差別**：後者之值域有**六值**
（`Initialization`／`IGN_LK`／`ACC`／`RUN`／`START`／`SNA`），目標非唯一，
故我拒絕該調和。二值與六值不同。

**惟此仍是本層之判斷，且已進入已放行之產物。**
**請分析層裁定該演繹是否成立**；若不成立，該二條須改為 `PENDING`。→ A-VS69

### 2.4 `writable = yes` **不等於**「可生成」

本掃描只量**來源條文之可寫性**，**不含委派狀態**。
`OneStageHeatedSeat` 於本表為 **14 / 14（100%）**，
但其中 **12 條之 `delegate = pending`**（DR-17，19 輪 D-8 記為待覆）。

**兩個軸須分開讀**：來源可寫性（本表）× 委派狀態（`delegation_lookup.tsv`）。
**本輪未做二者之交叉**，故「149 條可生成」是**上界，不是可生成量**。

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | `docs/reports/writability.tsv` 237 列；`scripts/writability_w58.py`；token 全集重建（30 → 31，新增 5 逐一具名）；`DATA_REQUESTS.md` 補登記 DR-8／DR-12、DR-21／22／23 改類別式、DR-19→21／DR-20→23／DR-12→21 併入且原編號保留；R-VS42 轉錄；A-VS66～69 登記 |
| **核實無誤** | 已知阻塞 6 條 **6 / 6** 被掃出；B4 = 0；新增 token 5 ≤ 10；母體 237 |
| **正確地不動** | **未把 `IGN_START` 讀為 `START`**；**未把 `-032`／`-038` 之假陽性逕自扣除**（兩數並列）；**未自行裁定 `Right Drive` 之演繹是否成立**（已放行產物，交分析層）；**未生成任何 TC**（本輪不生成）；v1／v2／v3 保留；**未寫回工作簿** |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| **token 三形態（R-VS36）** | 以「token ＋ 比較運算子 ＋ 方括號值」為操作型定義：`(\$?[A-Za-z][A-Za-z0-9_]{2,}\$?)\s*(?:=\|&lt;&gt;\|<>\|&gt;\|&lt;)\s*(\[[^\]]{0,90}\])` —— **該式同時涵蓋 `$X$ = [v]` 與裸名 `X = [v]`**，故不需分別掃描；另加描述式 `(?:PROXI parameter\|signal\|LID\|parameter)\s+(\$?…)` |
| **識別碼形態過濾** | `^(?:\w*_\w+\|[A-Z]{3,}\|(?:[A-Z][a-z0-9]*){2,})$` —— **不以停用字表為主判準**（停用字表無法窮舉，形態判準才可；R-VS34 之教訓）。初測未加此濾網時抓到 `with`／`and`／`until`／`values`／`warning`／`within` 六個英文常用字 |
| **B1** | `\b(as defined by\|as defined in\|refer to\|refer the\|follow the\|per the\|as specified by\|according to)\b` **且**條文內無 `(CFTS\s*\d{3}\|\{\d{7}\}\|PU\d+\|\d+\.\d+(\.\d+)+\|…Document\|…Spec\|…List)`。**再以「參照之前是否有具體結果動詞」二分**（結果動詞表見 §2.1），僅「無結果動詞」者計為阻塞 |
| **B2** | 對每個 token 之每個方括號值，比對其是否落在該 token 之匯流排值域內。值域取自 `spec_variables.tsv` 之 `lid_values` ∪ `dbc` ∪ `lid_format` 之 `N = label` 解析。比對採三式聯集：整串正規化鍵（R-VS39）／以 `/` 切分後各段／去 `Nh:` 前綴後之串。**值自身帶 `Nh:` 者直接視為可定位**（來源自載原始碼值）。**已知界線：不做跨條文之錨點聚合**，見 §2.2 |
| **B3** | token 不在 `spec_variables.tsv` 且該條文無 `internal signal`／`.Req`／`.Info`／`.GUI` 者（§8.7.5(d)：內部訊號不阻塞） |
| **B4** | 前三類皆不命中而仍無法撰寫者。**實測 0** |
| Layer 3 歸屬 | `scripts/layer3_w46.py::by_section()`（R-VS37′ 四分支） |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS66** | DR-8／DR-12（**本輪補登記**） | 分析層開立之 DR 未逐筆確認入簿（39 包 §4 指定） |
| **A-VS67** | — | **B1 判準過寬：65 → 8**；若止於初測會誤列 57 個可寫 leaf 為阻塞 |
| **A-VS68** | 併 DR-18 | `4858516` 之 `$HSW_StatS` **缺右側 `$`**，致掃出不存在之 token |
| **A-VS69** | — | `[Right Drive]` → `1 (Right Side)` 為本層之二值域演繹，**已入已放行之 TC**，請裁 |

**無新開 DR** —— DR-8／DR-12 為**補登記**（分析層早輪開立而未入簿）。
DR-21／22／23 依 **R-VS42** 改為類別式並補齊實例清單。

### 5.1 依 R-VS35 之登記簿核對（**含 39 包 §4 之分析層側**）

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **4**（A-VS66～69） | **68**（相異編號；最大號 A-VS69，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **0 新開；2 補登記**（DR-8／DR-12） | 未結 **12**（編號不變 —— DR-19→21、DR-20→23、DR-12→21 為併入，非減少） |

§5 表列 4 筆，登記簿逐筆核對皆在，**差額 0**。

**分析層側之核對（39 包 §4 之新機制，本輪首次執行）**：
39 包開立 **1 條 anomaly（A-VS66）**、**0 條 DR**；登記簿現有 A-VS66 **1 筆**，**差額 0**。
另補登記其早輪開立而未入簿者 **2 筆**（DR-8、DR-12）。

### 5.2 DR 現況（12 條）

| 態 | DR | 數 |
|---|---|---:|
| **待覆** | DR-14′／DR-15／DR-17／**DR-19**（併入 DR-21）／**DR-20**（併入 DR-23） | **5** |
| **待送** | DR-8／DR-11／**DR-12**（併入 DR-21）／DR-18／**DR-21**（B2，82 leaf）／**DR-22**（B3，2 leaf）／**DR-23**（B1，8 leaf） | **7** |

**三個類別式 DR 之影響合計 92 個 leaf**（有重疊，去重後 **88**）。

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **B2 不做跨條文之原始碼值錨點聚合，故其 82 leaf 為上界。**
   `-032`／`-038` 已證為假陽性（`4h:Ignition run` 在他條文）。
   **同型之假陽性尚有幾條，本輪未量** —— 其驗法為：對每個被 B2 標記之
   (token, 值) 對，全文回查該 token 是否有任一 `Nh:` 錨點可解該值。
   **該驗會直接改變 88 這個數。**

2. **`writable = yes` 未與委派狀態交叉，故 149 是上界不是可生成量。**
   見 §2.4。`OneStageHeatedSeat` 之 14 條全部可寫，但 12 條 `delegate = pending`。
   **實際可生成量 = writable ∩ delegate ∉ {pending, blocked}**，本輪未算。

3. **原有 30 個 token 中有 4 個本次未命中，未追因。**
   `HSW_StatFailSts`／`Heated_Seats_Levels`／`Heated_Steats_Levels`／`TGW_DISP_STAT`。
   可能之因：其於 237 leaf 所引條文中不以「比較運算子 ＋ 方括號值」形態出現
   （如僅出現於敘述句）。**若其實際承載值域，本掃描會漏掉其 B2 風險。**

4. **B1 之「結果動詞表」由本層手建，共 15 個詞。**
   `grey-out`／`display`／`shall set`／`shall send`／`activate`／`turn off`／
   `turn on`／`selectable`／`shall show`／`shall change`／`shall lower`／
   `shall monitor`／`shall allow`／`shall continue`／`accessible`／`is displayed`。
   **該表若漏詞，會把尾綴修飾誤判為整個結果被外推**（即 8 這個數偏高）。
   **未以反向抽樣驗證其召回率。**
