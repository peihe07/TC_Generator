# 上繳 19 —— 可寫性之精化、可生成量、兩個判準之召回率

執行層寫入。依據：`docs/handoff/40_review_round20.md` §4。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔（編號續前，18 已用） | ✅ |
| D-2 | 逐字轉錄 R-VS43 | ✅ |
| D-3 | A-VS69 關閉；A-VS70 新開 ＋ 兩數 | ✅ 見 §5.1 |
| **W-59** | 跨條文錨點 ＋ R-VS43 | ⚠ **升級：修正後仍 72 > 60** |
| **W-60** | 可生成量 | ✅ **141**（> 100，未命中） |
| **W-61** | 兩判準召回率 | ⚠ **升級：`== "值"` 形態未掃** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 W-59 —— 跨條文錨點聚合

| 項 | 20 輪 | **21 輪** |
|---|---:|---:|
| writable = yes | 149 | **165** |
| **writable = no** | **88（37.1%）** | **72（30.4%）** |
| B1 leaf | 8 | 8 |
| B2 leaf | 82 | **65** |
| B3 leaf | 2 | 2 |

**⚠ 升級條件命中**：逐字為「W-59 修正後 `writable = no` 仍 > 60」，實測 **72**。

移除之 (leaf, token, 值) 對 **17**：**跨條文錨點 13 ／ R-VS43 演繹 4**。

| token | 值 | 依據 |
|---|---|---|
| `PowerMode` | `Ignition run / IGN_RUN`／`Ignition run`／**`IGN_RUN`** | 錨點 `4h: ignition run` |
| `FL_HS_RQ`／`FR_HS_RQ` | `Not Pressed / HS_NOT_PSD` | 錨點 `0h: not pressed` |
| `HSW_RQ_TGW` | `NOT Pressed / NOT_PSD` | 同上 |
| `FL_VS_RQ_TGW`／`FR_VS_RQ_TGW` | `Not Pressed / VS_NOT_PSD` | 同上 |
| `DriverSide` | `Right Drive` | **R-VS43 三條件成立** |

> **裸寫 `[IGN_RUN]` 之解出多繞一層**：其單獨出現時無 `/` 可切，
> 故先由**來源自載之別名對**（`Ignition run / IGN_RUN` 同格並列 → 二者互為別名）
> 得 `ignition run`，再由錨點 `4h` 解出。**別名對亦取自來源，非本層造。**

### 1.2 W-59 —— R-VS43 三條件之逐筆判定

| 判 | 組數 |
|---|---:|
| **成立（derivable）** | **1** |
| 不成立 | 59 |

唯一成立者即 R-VS43 之成立例本身：

| 條件 | `$DriverSide$` 之 `[Right Drive]` |
|---|---|
| (1) 二值域且目標唯一 | 值域 2 值；與 `right side` 共享實詞 `right`，與 `left side` 不共享 → **唯一** |
| (2) 錨點 | 有（`0h: Left Side, 1h: Right Side`／`1h: Right Side`／`1h: Right hand`） |
| (3) 無平行對偶 | `left drive` 全文 **0 命中** |

### 1.3 W-60 —— **本 feature 之實際可交付量**

| 項 | 值 |
|---|---:|
| `writable = yes`（上界） | 165 |
| `delegate` 再扣（`pending` 12 ＋ `blocked` 12） | −24 |
| **`generatable = yes`** | **141 / 237（59.5%）** |

**141 > 100 → 「generatable < 100」之升級條件未命中。**

| Layer 2 | 可生成 / 總 | % |
|---|---:|---:|
| Common Features | 30 / 46 | 65 |
| Vented Seat | 46 / 72 | 64 |
| Heated Steering Wheel | 19 / 31 | 61 |
| Heated Seat | 46 / 88 | 52 |

阻塞成因分布：`writable=B2` 62／`delegate=pending` 12／`delegate=blocked` 12／
`B1+blocked` 5／`B1|B2` 2／其餘各 1。

**`OneStageHeatedSeat` 為 0 / 14** —— 其 14 條**全部可寫**，
但 12 條 `delegate = pending`（DR-17）、2 條 `blocked`。
**此即 §2.4 所指「可寫 ≠ 可生成」之最極端例。**

### 1.4 W-61(2) —— B1 動詞表之反向抽樣

| 向 | 母體 | 抽法 | 反例 |
|---|---:|---|---:|
| 尾綴修飾（應有結果動詞） | 57 | **reqid 升冪後系統抽樣，步長 6，起點 index 0，取前 10** | **0 / 10** |
| 整個外推（應無結果動詞） | 8 | **逐條全查，不抽樣** | **0 / 8** |

**「W-61(2) 之抽樣有反例」之升級條件未命中** —— 惟見 §2.3。

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **升級：`== "值"` 之語法形態，W-58 一條未掃**

W-61(1) 追四個未命中 token 時發現：

```
4859496  STATUS_CSWM.HSW_StatFailSts == "Fail_Not_Present"
4859377  $Heated_Steats_Levels$ == "Two Levels"
4859363  TELEMATIC_CLIMATE_SETUP.FL_HS_Cmd_Tlm = "Pressed"
```

**W-58 之 `TOKEN_CMP` 只匹配 `= [值]`（方括號），該形態一條未掃。**

全量重掃（`(?:[A-Z0-9_]+\.)?(token)\s*(?:==|=|passes to|!=)\s*"(值)"`）：

| 項 | 值 |
|---|---:|
| token 數 | **20** |
| 涉及 leaf | **95** |
| 值對照 **DBC** 後解出之 token | **5**（`*_STATFailSts` 之 `Fail_Present`／`Fail_Not_Present`） |
| **仍未解之 token** | **14** |
| **其中原判 `writable = yes` 之 leaf** | **79** |

**⚠ 升級條件命中**：逐字為「W-61(1) 之四 token 有任一承載值域而未被抽出」——
`HSW_StatFailSts` 與 `Heated_Steats_Levels` **皆承載值域**。

**14 個未解者分兩型**：

| 型 | token | 情況 |
|---|---|---|
| **實質不符** | `HeatedSeatFL`／`FR`、`VentedSeatFL`／`FR` | 條文寫 `Heated_seat_mid`／`Vented_seat_mid`，**DBC 為 `Heated_seat_medium`** |
| **未查 LID** | `Cooled_Seats`／`Heated_Seats`／`Heated_Seat_Levels`／`Heated_Steering_Wheel` | 皆為 **PROXI 參數**，其值域在 **LID** 而非 DBC；**本輪未逐一回查 LID** |
| 不在 DBC | `FL_HS_Cmd_Tlm`／`FR_`／`FL_VS_Cmd_Tlm`／`FR_`／`HSW_Cmd_Tlm` | LID 記其 `_Req` 變體為 `NOT_IN_DBC`（早輪已知） |

**故 165 與 72 兩數仍為上界／下界，本輪不逕自改寫。**
受影響之 79 列已於 `writability.tsv` 標 `quoted_form_risk = yes`。

> **這是 A-VS67 之鏡像**：A-VS67 是判準**過寬**致高估阻塞；
> **本項是掃描形態不全致低估阻塞**。兩者同源於「以自己假設的形態去掃」（R-VS34）。
> → **A-VS71**

### 2.2 W-59 之 R-VS43 判定，我第一版寫錯了

初版實作將條件 (1)「二值域，**或目標在值域內唯一可判**」讀為「值域大小 == 2」，
並將條件 (3) 無對偶詞可測時**預設為成立**。結果判出 **20 組 derivable**，其中包含：

```
FL_HS_RQ  之 High / Low / Medium   →  值域 {Not_Pressed, Pressed}
```

**那正是 DR-15 之衝突本身**（請求訊號為 1 bit 或承載階數，影響 160 leaf）。
把它判為「可演繹」等同**逕自解掉一個已送出待覆之 DR**。

修正兩處後（(1) 加「與值域中恰一成員共享實詞」之唯一性測；
(3) 無法測時**預設不成立**），**20 → 1**。

**若止於初版，本包會把 DR-15 所問之值當成已解。**

### 2.3 W-61(2) 之抽樣 0 反例，但抽樣對「表本身漏詞」不具鑑別力

兩向皆 0 反例 —— **惟該抽樣以同一張動詞表判定**。

逐條讀 8 條「整個外推」者：

| reqid | 措辭 |
|---|---|
| `4858560`／`4859509` | `the HMI shall be modified as defined by HMI requirements` |
| `4859032` | `the HU shall follow the HMI Logic & Flow to update the state` |
| **`4859386`／`4859387`／`4859448`／`4859449`／`4859498`** | **`TLM has to show an informative popup relative to the failure`** |

**五條之 `show` 為具體且可觀察之結果**，僅其內容（popup 文字）未具名。
表中有 `shall show`，**無 `has to show`**。

**若計入該措辭，B1 由 8 降為 3。**
**本層不逕自改判** —— 「show an informative popup relative to the failure」
是否足以撰寫可觀察之 ER，屬 TC 內容層之判斷。→ **A-VS72**

### 2.4 `TGW_DISP_STAT` 與 `Heated_Seats_Levels` 兩者之追因結果不同，一併記明

| token | 於 237 leaf 所引條文中 | 判 |
|---|---|---|
| `HSW_StatFailSts` | 3 條，`== "Fail_Not_Present"` 形態 | **承載值域，被漏掃**（A-VS71） |
| `Heated_Steats_Levels` | 6 條，`== "Two Levels"` 形態 | **承載值域，被漏掃**（A-VS71） |
| `TGW_DISP_STAT` | 1 條：`the HU shall send the $TGW_DISP_STAT$ signal. **See {CFTS020} for the signal value**` | **不承載值域** —— 其值明文外推至 `{CFTS020}`，**且該參照具名**，故非 B1 |
| `Heated_Seats_Levels` | **0 條** | **確實不出現**（其僅存於 `spec_variables.tsv`，來源未明） |

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | 跨條文錨點表（63 token）＋ 來源自載別名對（30 token）；`writability.tsv` 修正為 165/72 並增 `derivable`／`quoted_form_risk` 兩欄；`generatable.tsv` 237 列，**可交付量 141**；R-VS43 轉錄；A-VS69 關閉、A-VS70／71/72 登記 |
| **核實無誤** | R-VS43 之唯一成立例與 40 包 §1 之成立例一致；W-61(2) 兩向 0 反例；`Heated_Seats_Levels` 於 237 leaf 所引條文中確為 0 命中 |
| **正確地不動** | **未把 `FL_HS_RQ` 之 `High/Low/Medium` 判為可演繹**（那是 DR-15 之衝突本身，§2.2）；**未依 `== "值"` 之未解結果逕自改寫 165／72**（14 中有 4 個 PROXI 參數未回查 LID）；**未把 B1 由 8 改為 3**（屬 TC 內容層判斷）；**未生成任何 TC**；v1／v2／v3 保留 |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| **跨條文錨點表** | 全 2,030 條之 `(token)\s*(?:=\|&lt;&gt;\|<>)\s*(\[值\])`，於方括號內以 `([0-9A-Fa-f])h\s*:\s*([^,\]]+)` 取 `raw → label`。**一格可含多對**（`0h: Left Side, 1h: Right Side`）。得 **63 個 token** |
| **來源自載別名對** | 同上取值，去 `Nh:` 前綴後以 `\s/\s` 或 `(?<=\S)/(?=\S)` 切為二段者，二段互為別名。得 **30 個 token** |
| 可解判定 | 值之候選鍵 = {整串／去 `Nh:` 後／`/` 各段} ∪ 其別名，任一命中錨點即可解 |
| **R-VS43(1)** | 值域大小 == 2 **且** 該值與值域中**恰一個**成員共享實詞（實詞 = 去停用詞 `seat/the/of/and/a/signal/heated/vented/steering/wheel/front` 且長度 > 1） |
| **R-VS43(3)** | 以極性對照表（`right↔left`／`on↔off`／`present↔absent`／`active↔inactive`／`enabled↔disabled`）造出對偶措辭，全文回查其命中數；**0 命中方成立**。**無對偶詞可測時預設不成立**（保守） |
| W-60 | `generatable = yes` ⟺ `writable = yes` ∧ `delegate ∉ {pending, blocked}`；`delegate` 取自 `docs/reports/delegation_lookup.tsv` |
| **W-61(1) 引號形態** | `(?:[A-Z0-9_]+\.)?(\$?[A-Za-z][A-Za-z0-9_]{2,}\$?)\s*(?:==\|=\|passes to\|!=)\s*"([^"]{1,60})"`，token 再經識別碼形態過濾 |
| **W-61(2) 抽法** | 尾綴修飾 57 條：**reqid 升冪排序後系統抽樣，步長 6（57/10 ≈ 5.7），起點 index 0，取前 10**。整個外推 8 條：**逐條全查，不抽樣** |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS70** | — | W-58 之單條文比對設計致 B2 為上界，成因在分析層之 39 包 §2 規格（40 包 §2 指定登記） |
| **A-VS71** | **併 DR-21** | **`== "值"` 形態完全未掃**；20 token／95 leaf，14 未解，79 個原判可寫者受影響。⚠ 升級 |
| **A-VS72** | — | B1 動詞表漏 `has to show`；8 條中 5 條用該措辭，B1 可能應為 3 |

**A-VS69 依 R-VS43 關閉。無新開 DR** —— A-VS71 之實例併入既有之類別式 **DR-21**（B2），
惟**其實例清單須俟 §2.1 之 14 個 token 逐一回查 LID 後方能定案**。

### 5.1 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **3**（A-VS70／71／72） | **71**（相異編號；最大號 A-VS72，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **0** | 未結 **12**（不變） |

§5 表列 3 筆，登記簿逐筆核對皆在，**差額 0**。另關閉 1（A-VS69）。

**分析層側核對（40 包）**：40 包開立 anomaly **1 筆**（A-VS70）、DR **0 筆**；
登記簿現有 A-VS70 **1 筆**，**差額 0**。

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **`== "值"` 之 14 個未解 token 中，4 個為 PROXI 參數而未回查 LID。**
   `Cooled_Seats`／`Heated_Seats`／`Heated_Seat_Levels`／`Heated_Steering_Wheel`。
   **其值域若在 LID 中存在，該 4 個 token 之 leaf 應自阻塞清單移除。**
   **在此之前，`writable = no` 之 72 為下界、165 為上界，二者皆不可引為決策依據。**
   —— **與 20 輪之情形相同**：量出來的數又是一個界，不是實數。

2. **值之比對形態可能還有第三種。**
   已知 `= [值]`（W-58）與 `== "值"`（本輪）。
   **未掃者**：`= '值'`（單引號）、`is set to 值`、`shall be 值`、表格式（同列並置）。
   **未量其有無**，故第三種形態存在與否未知。

3. **`generatable = 141` 承接 `writable = 165`，故亦為上界。**
   若 §6-1 之回查使阻塞增加，141 隨之下降。
   **batch03 之排程若以 141 為依據，須先解 §6-1。**

4. **R-VS43(3) 之極性對照表僅 5 對，由本層手建。**
   `right↔left`／`on↔off`／`present↔absent`／`active↔inactive`／`enabled↔disabled`。
   **漏對者會使條件 (3) 落入「無對偶詞可測 → 不成立」而低估 derivable。**
   本輪 derivable 僅 1 組，**該表之漏詞直接決定這個數**，未以反向抽樣驗其召回率。
