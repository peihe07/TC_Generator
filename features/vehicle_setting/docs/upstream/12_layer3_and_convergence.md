# 上繳 12 —— 委派收斂重做、HSW 階數複核、Layer 3 全掃

執行層寫入。依據：`docs/handoff/30_review_round13.md` §4。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | 逐字轉錄 R-VS37 | ✅ |
| D-3 | A-VS48 新開 ＋ 登記簿兩數 | ✅ 見 §5.1 |
| D-4 | DR-17 新開 ＋ 12 列改 `pending` | ✅ **未送出** |
| **W-44** | 委派收斂之重做 | ⚠ **實測 12／174，與自陳之 14 不符** |
| **W-45** | HSW 側階數委派複核 | ✅ **無矛盾，升級未命中** |
| **W-46** | Layer 3 歸屬全掃 | ✅ 6 筆不一致（門檻 10）；**追到上游 typo** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 D-4 與 W-44 之母體

| 項 | 30 包 | 實測 | 判定 |
|---|---:|---:|---|
| 改為 `pending` 之列 | 12 | **12** | 符 |
| `delegate` 分布（改後） | — | `yes` 162／`no` 46／`blocked` 17／**`pending` 12** | 合計 237 |
| Comfort 有階數標記者 | 6 | **6** | 符（13 輪） |
| Comfort 有唯一側別標記者 | — | **1** | 新 |

### 1.2 W-44 —— 收斂前／後兩組

母體：`yes` ＋ `pending` = **174** 列（與 08 包同母體）。

| 項 | 收斂前 | 收斂後 |
|---|---:|---:|
| `comfort_leaf_ids` 總數 | **1,228** | **1,204** |
| 每列剩餘之分布 | — | 5 個:40 列／7 個:68 列／8 個:66 列 |
| **有收斂（清單縮短）** | — | **12 / 174** |
| **完全收斂（恰一個）** | 0 / 174（08 包） | **0 / 174** |

剔除之 24 個 comfort id **全部由階數維度剔除**，側別維度貢獻 **0**。

> **08 包之 `0 / 174` 其結果為真，其成因診斷為假。**
> 「資料本身沒有可收斂之維度」錯了（維度存在）；
> 但即使用上該維度，**完全收斂仍是 0 / 174**。

### 1.3 W-45 —— HSW 側，升級條件未命中

| 項 | 實測 |
|---|---|
| 本側 HSW leaf | **31**（30 包記 20+11=31，符） |
| 引用 `$Heated_Steering_Levels$` 者 | **2**（`HeatedSteeringWheel-004`／`-005`） |
| 含階數措辭者 | **0** |
| Layer 3 名稱帶階數者 | **0**（`HeatedSteeringWheel`／`HeatedSteeringWheelManagement`） |
| 委派列 | 31（`yes` 28／`blocked` 3） |
| **28 列之委派標的階數標記** | **全部為 `multi \| single`** |

**28 列全部同時引用 `-062`（Multi-Level）與 `-063`（Single-Level）** ——
**委派標的涵蓋兩種階數，無 A-VS46 同型之矛盾。**

**成因與座椅側之差異可具名**：Comfort 對加熱方向盤**兩種階數皆有條文**
（`-062`／`-063`），對座椅**只有 Multi-Level**。故座椅側才產生矛盾。

### 1.4 W-46 —— Layer 3 全掃與左右對稱

| 項 | 30 包 | 實測 | 判定 |
|---|---|---:|---|
| 母體 | 237 | **237** | 符 |
| token 判定 vs 章節判定不一致 | 「已知至少 2」 | **6** | 符（≥2）；**未達升級門檻 10** |

**依 R-VS37 重判後之左右對稱：**

| Layer 3 | token 判定 | **章節判定** |
|---|---:|---:|
| `LeftFrontHeatedSeat` | 17 | **15** |
| `RightFrontHeatedSeat` | 15 | **15** |
| `LeftFrontVentedSeat` | 15 | **15** |
| `RightFrontVentedSeat` | 15 | **15** |

**A-VS47 之不對稱已消解，四側齊為 15。**

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **升級：W-44 之實測收斂為 12 / 174，非 13 輪自陳之 14**

13 輪 §6-1 自陳其上限為「**14 個 OneStage 可分離**、其餘 84 個仍不可分」。
實測 **12**。

**差 2 之成因可具名**：`OneStageHeatedSeat` 全母體為 **14** 個 leaf，
但其中**只有 12 個在委派母體內**（另 2 個之 `delegate` 非 `yes`）。
自陳之 14 取自 **leaf 母體**，實測之 12 取自 **委派母體**。

**不自行調和** —— 兩數皆正確，口徑不同；本輪依 30 包 W-44(2) 之要求
給出**實測值 12**，並記明自陳之 14 為 leaf 母體口徑。

**「其餘 84 個仍不可分」之部分實測為真**：Two(32) ＋ Three(40) ＝ 72 列
所引皆為 `Multi`，**無一被剔除**；加上 90 列本側無階數者，
共 162 列收斂量為 0。

### 2.2 W-46(3) —— RF Vented 之 30 條追因：**上游 typo，且已污染值域**

| 節 | 條文數 | **正規化後相異** | 重複組 |
|---|---:|---:|---|
| LF Vented §1.3.2.1.3.3 | 29 | **28** | 1 組（`4858387`／`4858388`） |
| RF Vented §1.3.2.1.3.4 | **30** | **28** | **2 組** |

**兩節之相異條文數皆為 28 —— 來源規格對稱。**

RF Vented 之二重複組，逐條查其方括號值：

| 組 | 值 | 判 |
|---|---|---|
| `4858418`／`4858419` | `[Vented Seat High / VS_HI]` vs `[Vented seat medium / VS_MED]` | **真為二條**（LF 之 `4858387`／`4858388` 同型，對稱） |
| **`4858393`／`4858394`** | `…[Vented Seat High / **HS_HI**]` vs `…[Vented Seat High / **VS_HI**]` | ⚠ **僅差前綴 `HS_` vs `VS_`** |

LF 之對應條文（`4858363`／`4858367`／`4858368`）**一律為 `VS_HI`**。

> **`4858393` 把通風座椅之值寫成加熱座椅前綴（`HS_HI`）—— 上游 typo。**
> 差 1 即源於此：RF Vented 比 LF Vented 多一條「同文而值有誤」之條文。

**且該錯值已進入本 feature 之值域資料**（`data/spec_variables.tsv`）：

| token | `cfts044_include` 中之交叉前綴值 |
|---|---|
| `$VentedSeatFR$` | `Vented Seat High / HS_HI`、`Vented Seat High/HS_HI`、`Vented Seat Off / HS_OFF` |
| `$VentedSeatFL$` | `Vented Seat Off / HS_OFF` |

反向（`Heated …` 配 `VS_` 前綴）掃描**命中 0** —— 污染為單向，範圍 **4 個值 / 2 個 token**。

**不自行清除** —— 值域內容屬 TC 內容，且須先確認其為 typo 而非別名。→ A-VS49。

### 2.3 W-46(2) —— **6 筆中有 4 筆 R-VS37 未涵蓋**

| leaf | 原 token | `section` 欄逐字 | R-VS37 涵蓋？ |
|---|---|---|---|
| `LeftFrontHeatedSeat-004` | LeftFrontHeatedSeat | `1.3.2.1.3.1;.2;.3;.4` | **是**（四節同層，→ Common） |
| `LeftFrontHeatedSeat-011` | 同上 | 同上 | **是** |
| `HeatedSteeringWheelManagement-025` | HSWManagement | **`1.3.2.1.3;1.3.3.3.6.1`** | **否** |
| `HeatedSteeringWheelManagement-026` | 同上 | 同上 | **否** |
| `HeatedSteeringWheelManagement-027` | 同上 | 同上 | **否** |
| `HeatedSteeringWheel-009` | HeatedSteeringWheel | **（空）** | **否** |

R-VS37 之第二分支逐字為「該 leaf 之 reqid **跨越多個同層章節**」。
`1.3.2.1.3` 為**四段**、`1.3.3.3.6.1` 為**五段** —— **不同層**。
R-VS37 亦**未規定「無 reqid」之歸屬**。

**本輪暫依「多章節即 Common Features」處理該 3 筆，並將無 reqid 者單列** ——
**該處理無條文依據，已於 `framework.md` 以 ⚠ 標明。**
**不代擬條文** → 請分析層補 R-VS37 之第三、四分支。

### 2.4 `Common Features` 之名稱衝突

R-VS37 令跨章節者歸 `Common Features`，而 `Common Features` **已是 Layer 2 之名稱**
（R-VS4）。重判後其同時是 Layer 2 名與 Layer 3 名（5 個 leaf）。
**未自行改名**，於 `framework.md` 記為鎖定前須解之第 5 項。

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | `delegation_lookup.tsv` 之 12 列改 `pending` 並註 basis；`DATA_REQUESTS.md` 新開 DR-17；`framework.md` 依 R-VS37 重判 Layer 3（左右對稱回復 15/15/15/15），改判六筆逐筆記明依據；新腳本 `converge_w44.py`／`layer3_w46.py` |
| **核實無誤** | 12 列（符）；HSW 31 leaf（符）；237 母體（符）；不一致 6 筆（≥2，未達門檻 10）；**LF/RF Vented 相異條文皆 28，來源對稱** |
| **正確地不動** | **未清除 `$VentedSeatFR$` 之 `HS_` 交叉前綴值**（屬 TC 內容，且須先確認為 typo 而非別名）；**未代擬 R-VS37 之缺分支**（3 筆跨異層、1 筆無 reqid）；**未改 `Common Features` 之名稱衝突**；**未調和 12 vs 14**（口徑不同，兩數皆正確）；**framework 未鎖定**；DR-17 未送出 |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| W-44 階數橋接 | Comfort 側：`data/_comfort_leaf_text.json`（13 輪自 037 `Analysis Report` 取得之 129 個相異 id），以 `\b(one\|two\|three\|single\|multi)[\s-]?(stage\|level)s?\b` 判，含 `single` 者標 `single`，否則 `multi`。本側：SWE ID 中段 token 之 `(One\|Two\|Three)Stages?`，`One→single`、`Two/Three→multi` |
| W-44 側別 | Comfort 側 `\b(driver\|passenger\|left\|right)\b`，**唯一命中時**才標記（driver/left→left，passenger/right→right）；本側 `(Left\|Right)Front` |
| W-44 相容性 | **未標記之維度不構成排除** —— 僅當兩側皆有標記且相異時才剔除 |
| W-44 收斂之定義 | 清單縮短者為「有收斂」，縮至恰一個者為「完全收斂」（同 08 包） |
| W-45 | HSW leaf 取 `swe_id` 含 `HeatedSteeringWheel` 者；`$Heated_Steering_Levels$` 之查詢依 **R-VS36** 三形態（`$X$`／裸名／描述式） |
| W-46 章節判定 | `data/leaf_to_reqid.tsv` 之 `section` 欄，以 `;` 分隔；章節→Layer 3 之對照表寫在 `scripts/layer3_w46.py` 之 `SEC_L3`（21 個章節，取自 12 輪草案之實際落點） |
| W-46(3) 重複判定 | 條文本文去除**所有**方括號內容後，再以 `\b(left\|right\|front\|fl\|fr\|lf\|rf)\b→·` 正規化並小寫，同字串者為一組。**方括號值另行逐條比對**（此即分辨真重複與 typo 之關鍵） |
| **已試而捨棄** | 以 `difflib` 序列比對定位 RF Vented 之多出條文 —— **差 1 卻算出 shift = 2，方法失效**（樣板文字相似度過高）。改用上列可判定之重複測試 |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS48** | — | W-42 之四屬性對照在條文層級去重，未查同一 leaf 之多 reqid 屬性是否一致；`Model Year` 為唯一有實質差異者，未追因（30 包 §4 D-3 指定登記） |
| **A-VS49** | **需新 DR，本層不代擬** | `4858393` 將通風座椅之值寫為 `HS_HI`（加熱前綴），與 `4858394` 同文而值異；該錯值已入 `spec_variables.tsv` 之 `$VentedSeatFR$`／`$VentedSeatFL$` |
| **A-VS50** | — | R-VS37 未涵蓋「跨**異層**章節」與「無 reqid」二情形，3+1 筆之改判無條文依據 |

**無新開 DR** —— A-VS49 之提問屬分析層。DR-17 已建立，**仍未送出**；DR-15 亦未送出。

### 5.1 D-3 —— 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **3**（A-VS48／49／50） | **49**（相異編號；最大號 A-VS50，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **1**（DR-17，30 包 §2 全文） | — |

§5 表列 3 筆，登記簿逐筆核對皆在，**差額 0**。`A-VS02` 缺號維持。

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **W-44 之「完全收斂 0 / 174」是在 `comfort_leaf_ids` 既有清單上過濾得到的。**
   **未驗證該清單本身是否完整** —— 若某本側 leaf 其實還對應到清單外的
   Comfort leaf，收斂率會不同。08 包之配對來源（Layer 3 物理功能）未複核。

2. **A-VS49 之污染只掃了 `cfts044_include` 一欄。**
   `cfts044_exclude` 與 `cfts044_other_arch` **未掃**；
   且**只查了 `Heated`/`Vented` 一對前綴** ——
   其他 token 是否有同型交叉（如 `HSW_` 配座椅值）**未掃**。

3. **W-46 之 `SEC_L3` 對照表由本層依 12 輪草案手建，共 21 個章節。**
   若某 leaf 之 `section` 值不在表內，`by_section()` 會回傳
   `(未知章節 …)` 而**非報錯**。本輪 237 筆未出現該值，
   **但該對照表本身未經分析層確認。**

4. **`framework.md` 之左右對稱已回復（15/15/15/15），但未驗其內容對稱。**
   只驗了**筆數**。左右各 15 個 leaf 是否**逐條對應同一需求**，未驗 ——
   13 輪之逐位對照只做過 HeatedSeat 兩節，**Vented 兩節未做**。
