# 上繳 20 —— 可寫性之最後收斂、R-VS44 實作、batch03

執行層寫入。依據：`docs/handoff/41_review_round21.md` §5。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | 逐字轉錄 R-VS44 | ✅ |
| D-3 | 5 條 popup 改可寫；B1 8 → 3；A-VS72 關閉 | ✅ |
| D-4 | 依 R-VS35 列兩數 | ✅ 見 §5.1 |
| **W-62** | 可寫性之收斂 | ⚠ **升級：no 由 72 增至 146** |
| **W-63** | R-VS44 實作 | ✅ **錨點通過且可失敗** |
| **W-64** | batch03 生成 | ✅ **10 條，§9 檢查 0 違規** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 D-3 ＋ W-62(1) —— `writable` 之三次移動

| 階段 | yes | no | 成因 |
|---|---:|---:|---|
| 21 輪結束 | 165 | 72 | — |
| **D-3**（5 條 popup 依 R-VS17 改可寫） | **170** | **67** | B1 8 → **3** |
| **W-62(1)**（引號形態之阻塞併入） | **91** | **146** | 4 個 PROXI 參數回查 LID **全數未解** |

**⚠ 升級條件命中**：逐字為「W-62(1) 回查後 `writable = no` 較 72 增加」，實測 **146**。

### 1.2 W-62(1) —— 四個 PROXI 參數逐一回查 LID

| token | LID 命中 | `can` | **Format 欄** | 待解值 | 判 |
|---|---:|---|---|---|---|
| `Cooled_Seats` | 1 | PROXI | **`See Proxi Table`** | `Front Seats` | **未解（轉指）** |
| `Heated_Seats` | 1 | PROXI | **`See Proxi Table`** | `Front Seats` | **未解（轉指）** |
| `Heated_Seat_Levels` | 1 | PROXI | **`See Proxi Table`** | `One Level` | **未解（轉指）** |
| `Heated_Steering_Wheel` | 4 | PROXI | **`See Proxi Table`** | `Present` | **未解（轉指）** |

**四者之 Format 皆為 `See Proxi Table`** —— **其為轉指而非不存在**（41 包 §5 已預期此形態）。
所指之 Proxi Table **不在 `inputs/`**。

> 順帶量到：同表之 `Heated_Steering_Levels` 有實 Format
> （`0 = 1  Level`／`1 = 2 Levels`／`2 = 3 Levels`／`# = Not Used`）。
> **未以其類推 `Heated_Seat_Levels`** —— 跨 token 之類推不在 R-VS43 之三條件內。

### 1.3 W-62(2) —— 餘數驗證，**(b) = 0**

| 項 | 值 |
|---|---:|
| (token, 出現) 對總數 | **336** |
| 兩式（`= [值]`／`== "值"`）已命中 | **269** |
| **餘數** | **67** |

餘數逐 token 檢視其上下文，分類：

| 類 | 數 | 例 |
|---|---:|---|
| **(a) 不承載值域** | **67** | `based on the $EngRun_Stat$ signal`／`shall Monitor $Heated_Steering_Wheel$`／`the $DriverSide$ signal value shall have no impact`／`Valid values for the $X$ are shown below`（其值列於後續 `= [值]`，已由式一命中）／`send an on change $FL_HS_RQ$ depending on the current status` |
| **(b) 承載值域但為第三式** | **0** | —— |
| **(c) 無法判定** | **0** | —— |

**五個候選第三式逐一實測，全數 0 命中**：

| 候選形態 | 命中 |
|---|---:|
| `= '值'`（單引號） | **0** |
| `is set to <值>` | **0** |
| `shall be set to <值>` | **0** |
| `shall be <大寫值>` | **0** |
| `= <裸值>`（無括號無引號） | **0** |

**(b) = 0 → 「(b) 類非 0 且無法化為新式」之升級條件未命中。**

### 1.4 W-63 —— R-VS44 之實作與可失敗錨點

`scripts/dr_conflict.py`：未結 DR 之提問範圍以 **(token 集合, 值之正則, 狀態)** 宣告，
`guard()` 於**輸出階段**攔截。已併入 `scripts/writability_w58.py` 之 `scan_leaf()`。

| 輸入 | 輸出 |
|---|---|
| `FL_HS_RQ` × `High`／`Low`／`Medium` × `derivable` | **`DR-CONFLICT`** —— `DR-15（待覆）之提問標的，依 R-VS44 不採用「derivable」` |
| `DriverSide` × `Right Drive` × `derivable` | `derivable`（不在任何未結 DR 範圍內） |
| `EngRun_Stat` × `IDLE_STBL//…` × `blocked` | `blocked`（維持） |

**可失敗性驗證（negative control）**：

```
移除交叉檢查前： ['DR-CONFLICT', 'DR-CONFLICT', 'DR-CONFLICT']
移除交叉檢查後： ['derivable',   'derivable',   'derivable']
還原後：         ['DR-CONFLICT', 'DR-CONFLICT', 'DR-CONFLICT']
```

**錨點可失敗** —— 非恆為 `DR-CONFLICT`。「驗收錨點不可失敗」之升級條件未命中。

### 1.5 W-64 —— 穩定核心與 batch03

| 項 | 值 |
|---|---:|
| **穩定核心**（`generatable = yes` ∧ `quoted_form_risk = no`） | **72** |
| 已用（batch01_v3 8 ＋ batch02 6 ＋ 移出／未撰寫 6 中之核心者） | 12 |
| **本批可選** | **59** |
| **本批取用** | **10** |
| §9 機械檢查違規 | **0** |

**72 ≥ 10 → 「穩定核心不足 10」之升級條件未命中。**

**Sibling Rows 已注入**：10 條分屬三個 Layer 3，其中**四對為左右鏡像**
（`-003`/`-022`、`-007`/`-025`、`-008`/`-026`、`-012`/`-029`）。
逐對比對後 **`duplicate_of` 無** —— 其 verification target 分屬不同座椅，
訊號亦相異（`FL_HS_STATSts` vs `FR_HS_STATSts`），非 §10.6 之嚴格等價。
**10 / 10 輸出 `distinguishing_axis`**，軸為 `trigger_state` 6／`input_data` 2／`mode` 1／`timing` 1。

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **升級：`writable = no` 由 72 增至 146**

成因為 21 輪 §2.1 已具名而本輪確認之事：`== "值"` 形態之 14 個未解 token
中，4 個 PROXI 參數回查 LID 後**全數為 `See Proxi Table` 轉指**，
故 **79 個原標 `quoted_form_risk` 之 leaf 全數轉為阻塞**。

**這不是新發現，是 21 輪已標記之風險落地。**
21 輪未逕自併入是對的（當時 4 個 token 未回查）；**本輪回查完畢，故併入。**

`generatable` 隨之由 141 降為 **72**。

### 2.2 穩定核心與 generatable 在本輪**數值相同**，其概念差異須記明

41 包 §3 定義穩定核心為 `generatable = yes ∧ quoted_form_risk = no`，
其設計前提為「`quoted_form_risk` 尚未併入 `writable`」。

**本輪 W-62(1) 已將 risk 併入 `writable`**，故
`generatable = yes` 者其 `quoted_form_risk` 必為 `no` ——
實測 `quoted_form_risk = yes ∧ generatable = yes` 者為 **0**，
兩集合**完全重合，皆為 72**。

**該重合是本輪處置之後果，非巧合。** `generatable.tsv` 仍保留 `stable_core` 欄，
以備日後 risk 與 writable 再度分離。

### 2.3 五條 popup 條文**其實有具名** —— 我的「具名」正則漏字

其全文為 `… popup relative to the failure. **Refer to TLM HMI Document.**`

W-58 之 `NAMED` 末式為 `[A-Z][A-Za-z]*_[A-Za-z_]*(?:Document|Spec|List)` ——
**要求含底線**，故 `TLM HMI Document`（空白分隔）不命中。

41 包 §2 以 **R-VS17**（DR-5-B 之既有政策）判其可寫，**結論相同但成因不同**：
分析層之依據是政策，**本項是正則漏字**。→ **A-VS74**

**B1 剩餘 3 條已逐條複查**：

| reqid | 措辭 | 判 |
|---|---|---|
| `4858560`／`4859509` | `as defined by HMI requirements` | **泛稱，非文件名** |
| `4859032` | `follow the HMI Logic & Flow` | **文件類型名；本 feature 之 `inputs/` 無此檔** |

**三者確為未具名或具名而不存在**，B1 = 3 成立。

### 2.4 極性對照表召回率 **7 / 16**，且補表不是單純的字典擴充

W-62(3) 以**普查**（非抽樣）掃 30 個 token 之全部 **351 個值**：

| 項 | 值 |
|---|---:|
| 含極性詞之 (token, 值) 對 | **156** |
| 相異極性詞 | **16** |
| **對偶在表內者** | **7** |
| **不在表內者** | **9** |

漏詞（依出現次數）：**`pressed`(43)**／`high`(19)／`low`(19)／`start`(7)／
`disabled`(6)／`lock`(2)／`true`(1)／`stop`(1)／`invalid`(1)。

**`pressed` 為出現最多者卻不在表內。**

後果：R-VS43(3) 於無對偶詞可測時**保守判不成立**，故 **derivable 被低估**。

> **但補表不是單純的字典擴充** —— `pressed` 之對偶 `not pressed` 直接落在
> **DR-15 之 1 bit vs 階數爭點**上。依 **R-VS44**，補表後新增之 derivable
> **須先過未結 DR 之交叉檢查**。**本輪未補表。** → A-VS75

### 2.5 **`B4 = 0` 應讀為「掃描偵測不到 B4」，不是「B4 不存在」**

`4858310`／`4858340`（`The HU shall ignore **invalid** $HeatedSeatFL/FR$ signals`）
**無方括號值**，B1/B2/B3 三類皆不命中，判 `writable = yes`。

惟其可寫性取決於「何謂 invalid」：基線 DBC 之 `FL_HS_STATSts` 為 **2 bit**，
**0–3 四個編碼全部已定義**，**無現成之無效編碼可注入**。

本輪之所以寫得出來，是因 **`4858307` 逐字給出二階配置之有效值**
（`HS_OFF`／`HS_LO`／`HS_HI`），故 `2 (Heated_seat_medium)` 於二階下為無效
—— **來源自載，非造值**。

**但該解法是人讀他條文得來，掃描看不見。** → **A-VS76**

### 2.6 `Heated_Steering_Levels` 有實 Format，`Heated_Seat_Levels` 無 —— 未類推

同一 LID 表內：

```
Heated_Steering_Levels   0 = 1  Level / 1 = 2 Levels / 2 = 3 Levels / # = Not Used
Heated_Seat_Levels       See Proxi Table
```

形態高度相似，**惟跨 token 之類推不在 R-VS43 之三條件內**（其三條件皆為
同一 token 內之證據）。**未類推，`Heated_Seat_Levels` 維持未解。**

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | `scripts/dr_conflict.py`（R-VS44 之輸出閘，含可失敗錨點）並併入 `writability_w58.py`；`writability.tsv` 增 `blocked_layer`／`blocked_ref` 兩欄、B1 8 → 3、引號形態阻塞併入；`generatable.tsv` 增 `stable_core` 欄；**`generated/batch03.json` 10 條、§9 檢查 0 違規**；R-VS44 轉錄；A-VS72 關閉、A-VS74/75/76 登記 |
| **核實無誤** | 四個 PROXI 參數逐一回查 LID，**四者皆 `See Proxi Table`**；餘數 67 全數為 (a) 類，五個候選第三式 **0 命中**；穩定核心 72 ≥ 10；四對左右鏡像無 `duplicate_of` |
| **正確地不動** | **未以 `Heated_Steering_Levels` 之 Format 類推 `Heated_Seat_Levels`**（§2.6）；**未補極性對照表**（其新增者須先過 R-VS44，§2.4）；**未把 `pressed` 之對偶引入而動到 DR-15 之爭點**；**未生成 `4858310` 之無效值於三階配置下之分支**（該分支由 `4858308` 擁有）；v1/v2/v3 保留；未寫回工作簿 |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| W-62(1) LID 回查 | `data/lid_pairs.tsv` 2,710 列，以 token 之底線式與空白式**兩種拼法**（如 `Cooled_Seats` 與 `Cooled Seats`）不分大小寫全列字串比對；待解值再於命中列之 `fmt` 欄內回查 |
| **W-62(2) 餘數之母體** | 237 leaf 所引條文中，**全部已知 token 之每一次出現**（`\$?\b([A-Za-z][A-Za-z0-9_]{2,})\b\$?` 且 token ∈ 已知集合），共 **336** 對 |
| W-62(2) 兩式之判定 | 出現位置之後 30 字元內，`\s*(?:=\|&lt;&gt;\|<>\|&gt;\|&lt;)\s*\[`（式一）或 `\s*(?:==\|=\|passes to\|!=)\s*"`（式二） |
| W-62(2) 候選第三式 | 五式逐一全掃：`(?:==\|=)\s*'[^']{1,40}'`／`is set to\s+\S{1,40}`／`shall be set to\s+\S{1,40}`／`\$\w+\$\s+shall be\s+[A-Z_]…`／`\$\w+\$\s*(?:==\|=)\s*(?!\[\|")[A-Za-z0-9_]{2,}` |
| **W-62(3) 抽法** | **普查，非抽樣** —— 30 個 token 之 `cfts044_include`／`cfts044_exclude`／`lid_values` 三欄全部 **351 個值**；極性詞表 24 詞（`on/off/left/right/present/absent/active/inactive/enabled/disabled/high/low/open/close/closed/up/down/yes/no/true/false/lock/unlock/pressed/start/stop/valid/invalid/available/unavailable`） |
| W-63 未結 DR 之範圍宣告 | `scripts/dr_conflict.py::OPEN_DR`，以 **(token 集合, 值之正則, 狀態)** 宣告，粒度與判定腳本之輸出粒度一致 |
| W-64 選 leaf | `generatable.tsv` 之 `stable_core = yes`，扣除已入 batch01_v3／batch02／`blocked_pending_dr.json` 者，依最小 reqid 升冪 |
| W-64 值之解析 | `$PowerMode$` 之 `[Ignition run]` → `4 (RUN)`，依**跨條文錨點** `[4h:Ignition run]`（全文 5 處，W-59 建表）；`$FL_HS_RQ$` 之 `[Not Pressed / HS_NOT_PSD]` → `0 (Not_Pressed)`，依錨點 `0h: not pressed`；**二者皆非 R-VS43 之演繹，而是來源自載原始碼值** |
| W-64 無效值之依據 | `4858307` 逐字：`For vehicles with two states (i.e. LO and HI) … Valid values … $HeatedSeatFL$ = [Heated Seat Off / HS_OFF] … [Heated Seat Low / HS_LO] … [Heated Seat High / HS_HI]` → `2 (Heated_seat_medium)` 於二階配置下為無效 |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS74** | — | B1 之「具名」正則漏帶空白之文件名（`Refer to TLM HMI Document`） |
| **A-VS75** | — | 極性對照表召回率 7 / 16；漏 `pressed`(43) 等 9 詞；**補表須先過 R-VS44** |
| **A-VS76** | — | `B4 = 0` 為掃描盲區所致，非 B4 不存在 |

**A-VS72 依 R-VS17 關閉。無新開 DR。**

> **`See Proxi Table` 所指之 Proxi Table 不在 `inputs/`** —— 其為**素材缺件**。
> 依禁區「不補素材」，本層不索取；**是否開 DR 屬分析層**。
> 現以 DR-22（B3 類）承載其四個 token，惟 **DR-22 之提問文未涵蓋「Proxi Table 缺件」此一具體訴求**。

### 5.1 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **3**（A-VS74／75／76） | **75**（相異編號；最大號 A-VS76，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **0** | 未結 **12**（不變） |

§5 表列 3 筆，登記簿逐筆核對皆在，**差額 0**。另關閉 1（A-VS72）。

**分析層側核對（41 包）**：41 包開立 anomaly **0 筆**、DR **0 筆**；**差額 0**。

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **`Proxi Table` 為素材缺件，而現行 DR 無一以其為訴求。**
   四個 PROXI token 之 LID Format 皆為 `See Proxi Table`，該表不在 `inputs/`。
   DR-22 承載該四個 token，**但其提問文問的是「token 於三處無記載」**，
   而實情是「**LID 有記載，其轉指之表我方沒有**」——**兩者之解法不同**：
   前者要上游定義，後者只要一份既有文件。**提問文須改，屬分析層。**

2. **B4 之偵測方法未建立。**
   §2.5 之 `invalid` 型是人讀他條文才解出。
   **同型（條文引用一個值之類別而非具體值）尚有幾條，本輪未掃** ——
   候選措辭：`invalid`／`all other states`／`any other value`／`unsupported`。

3. **batch03 之 `<Tsend>` 未展開。**
   `4858320` 逐字為 `within a time period of <Tsend>`，**來源未給具體時值**。
   本層依 §8.4.1 保留 `<Tsend>` 原樣（其明文允許 `<configured limit>` 形態）。
   **惟該 TC 之末步驟斷言「within <Tsend>」在執行時無法判定通過與否** ——
   **是否須開 DR 索取 Tsend 之值，本輪未判**（屬 TC 內容層）。

4. **穩定核心 72 之組成尚未逐 Layer 3 檢視其代表性。**
   其中 `Common Features` 佔 30、四個單側座椅 Layer 3 各僅 5。
   **若後續批次持續依 reqid 升冪取，會先耗盡座椅類而使 Layer 2 覆蓋不均** ——
   canon §4.1.3 之覆蓋均勻性未納入選 leaf 判準。**本輪未驗其影響。**
