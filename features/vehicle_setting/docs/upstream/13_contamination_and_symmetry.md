# 上繳 13 —— 交叉前綴污染全掃、Vented 兩節對照、framework 定稿前檢查

執行層寫入。依據：`docs/handoff/31_review_round14.md` §5。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | 轉錄 R-VS37′、R-VS37 加註取代 | ✅ |
| D-3 | 三項改判 ＋ 更名 ＋ 兩數 | ✅ **不一致降為 2，非 3** |
| **W-47** | 交叉前綴污染之全掃 | ✅ **4 筆全判 typo，別名 0，升級未命中** |
| **W-48** | Vented 兩節逐位對照 | ⚠ **升級：不對稱型與 Heated 不同** |
| **W-49** | framework 定稿前最後檢查 | ✅ **46／88／72／31 逐項相符** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 D-3 —— R-VS37′ 四分支之套用

| 分支 | 筆數 |
|---|---:|
| (1) 單一章節 | **231** |
| (2) 跨同層 → `CrossZone Common` | **2** |
| (3) 跨異層 → 取最深章節 | **3** |
| (4) 無 reqid → token 預設值 | **1** |
| 合計 | **237** |

**R-VS37′(3) 之預期成立**：`HeatedSteeringWheelManagement-025/-026/-027`
取最深之 `1.3.3.3.6.1` 後歸 `HeatedSteeringWheelManagement`，
**與 token 判定一致**（31 包 §1 之預言正確）。

### 1.2 W-47 —— 污染全掃

| 項 | 14 輪 | **本輪（全欄全 token）** | 判定 |
|---|---:|---:|---|
| 掃描之 token | 2 | **14**（有語意前綴者，共 30 個 token） | 擴大 |
| 掃描之值域欄 | 1 | **6** | 擴大 |
| **相異 (token, 值) 對** | 4 | **4** | **符** |
| 反向（`Heated` 配 `VS_`） | 0 | **0** | 符 |

**擴大掃描後筆數不變 —— 14 輪之 4 筆即為全部。**

| # | token | 值 | 來源 | 章節 | EE Arch | 判 |
|---|---|---|---|---|---|---|
| 1 | `$VentedSeatFR$` | `Vented Seat High / HS_HI` | `4858393` | 1.3.2.1.3.4 | PowerNet | **typo** |
| 2 | `$VentedSeatFR$` | `Vented Seat High/HS_HI` | `4858001` | 1.3.1.1.3.4 | CUSW | **typo** |
| 3 | `$VentedSeatFR$` | `Vented Seat Off / HS_OFF` | `4860021` | 1.3.4.12.4 | Atlantis Mid | **typo** |
| 4 | `$VentedSeatFL$` | `Vented Seat Off / HS_OFF` | `4860015` | 1.3.4.12.3 | Atlantis Mid | **typo** |

**別名 0 → 升級條件未命中。** 逐筆判據見 `docs/reports/prefix_contamination.md`。

### 1.3 W-48 —— Vented 兩節逐位對照

移除 A-VS49 之 typo 重複條 `4858393` 後，LF **29** ／ RF **29**，逐位配對。

| 檢查 | 結果 |
|---|---|
| **(2a) 引用狀態不一致** | **0**（Heated 兩節為 2，A-VS47） |
| (2b) 方括號值不對稱（初測） | 3 |
| **(2b) 扣除大小寫差異後之真不對稱** | **1** |

配對之正確性已驗：第 20～25 位之本文逐對相符（`ECU`、句式、訊號名皆對應），
**非序列錯位。**

### 1.4 W-49 —— Layer 2 四數

| Layer 2 | R-VS15 | 實測 | 判定 |
|---|---:|---:|---|
| Common Features | 46 | **46** | 符 |
| Heated Seat | 88 | **88** | 符 |
| Vented Seat | 72 | **72** | 符 |
| Heated Steering Wheel | 31 | **31** | 符 |
| **合計** | 237 | **237** | 符 |

**四數逐項相符，升級條件未命中。**
委派狀態合計：`yes` 162／`no` 46／`blocked` 17／`pending` 12 = **237**。

## 2. 不符項目（不自行調和）

### 2.1 D-3 —— 不一致筆數為 **2**，非 31 包 §1 預期之 3

31 包 §1 逐字：「不一致筆數由 6 降為 **3**（`LeftFrontHeatedSeat-004`／`-011`
＋ `HeatedSteeringWheel-009` 之標記）」。實測 **2**。

**成因可具名**：R-VS37′(4) 令無 reqid 者「**依 SWE ID 中段 token 之預設值**」，
故 `HeatedSteeringWheel-009` 之判定結果 **等於** 其 token，**不構成「不一致」**。
其所得為一個 `UNRESOLVED-SOURCE` **標記**，而非改判。

**不自行調和** —— 兩數皆正確，31 包把「加標記」計入「不一致」，本輪只計改判。
`framework.md` 已將該筆列於改判表並標明其為標記而非改判。

### 2.2 ⚠ **升級：Vented 兩節之不對稱型與 Heated 兩節不同**

Heated 兩節之不對稱為 **引用歸屬**（左側 leaf 引右側條文 → A-VS47），
引用狀態不一致 **2** 筆、值全對稱。

Vented 兩節相反：**引用狀態不一致 0**，但**值不對稱 1** 筆。

| 位 | 左 | 右 |
|---|---|---|
| 第 22 | `4858382`：`$CCDMF_FL_VS_RQ$ = **[Vented Seat Pressed / VS_PSD]**` | `4858413`：`$CCDMF_FR_VS_RQ$ = **[ Pressed]**` |

**右側之值退化為 `[ Pressed]` —— 標籤 `Vented Seat` 與代碼 `VS_PSD` 皆遺失**，
且保留了一個前導空白。**此為與 Heated 側不同型之不對稱 → 升級條件命中。**

**其對值域抽取之影響**：`$CCDMF_FR_VS_RQ$` 之第一階值域會少一個值，
且會多出一個字面為 `Pressed`（帶前導空白）之值。→ A-VS51。

### 2.3 我初測之 3 筆中有 2 筆是我自己的過濾器造成的

初測「值不對稱 3 筆」，逐條讀後：

| 位 | 左 | 右 | 實情 |
|---|---|---|---|
| 第 21 | `[Not Pressed / VS_NOT_PSD]` | `[Not pressed / VS_NOT_PSD]` | **僅大小寫差異** |
| 第 24 | `[Not Pressed]` | `[Not pressed]` | **僅大小寫差異** |
| 第 22 | `[Vented Seat Pressed / VS_PSD]` | `[ Pressed]` | **真不對稱** |

我的值過濾條件為「含 `Seat` 或 `Press`」—— **大小寫敏感**，
故 `pressed`（小寫）未被收進右側之值清單，看起來像「右側無值」。

**若止於初測而回報「Vented 兩節值不對稱 3 筆」，其中 2 筆會是我造出來的。**

**但該大小寫差異本身是真的，且有後果** —— 見 §2.4。

### 2.4 值域之大小寫雙寫，已在 `spec_variables.tsv` 產生重複值

CFTS044 對同一個值有多種大小寫寫法，逐字並存：

| 同一值之並存寫法 | 全文次數 |
|---|---|
| `[Vented Seat Low / VS_LO]` ／ `[Vented Seat Low / VS_Lo]` | 5 ／ 4 |
| `[Vented Seat Medium / VS_MED]` ／ `[Vented seat Medium / VS_MED]` ／ `[Vented seat medium / VS_MED]` | 2 ／ 2 ／ 4 |
| `[Not Pressed]` ／ `[Not pressed]` | — |

`$VentedSeatFR$` 之 `cfts044_include` 因此同時含
`Vented Seat Low / VS_LO`、`Vented Seat Low / VS_Lo`、
`Vented Seat Medium / VS_MED`、`Vented seat Medium / VS_MED`、`Vented seat medium / VS_MED`
—— **同一個值算成五個。** → A-VS52。**不自行合併**（屬 TC 內容）。

### 2.5 `$Heated_Steats_Levels$` —— token 本身是 typo

`spec_variables.tsv` 之 30 個 token 中有 `$Heated_Steats_Levels$`
（`Steats`，應為 `Seats`）。其與 `$Heated_Seats_Levels$` 並存。
**不自行合併或改名** → A-VS53。

### 2.6 31 包 §5 之 typo／別名判據不足以分辨

31 包逐字：「對稱側一律用另一前綴者判 typo；**對稱側亦用同前綴者判別名**」。

`4860015`（LF）與 `4860021`（RF）**兩側一致地寫 `HS_OFF`** —— 依該判據應判**別名**。

**但更寬之基礎顯示其為 typo**：

| 證據 | 值 |
|---|---|
| §1.3.4.12.3 內 `4860011`／`4860013` | `[Vented Seat Off / **VS_OFF**]` |
| §1.3.4.12.4 內 `4860017`／`4860019` | `[Vented Seat Off / **VS_OFF**]` |
| 全文 `$VentedSeatF*$ = [Vented Seat Off / VS_OFF]` | **15 次** |
| 全文 `$VentedSeatF*$ = [Vented Seat Off / HS_OFF]` | **2 次**（即本二筆） |

**別名須為系統性雙軌命名；此處同一章節內即自相矛盾。**
本輪改以「章節內並存 ＋ 全文頻次」為基礎判 typo。
**判據之修訂屬分析層**，本層只陳述所用基礎與理由 → A-VS54。

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | `layer3_w46.py` 補齊 R-VS37′ (3)(4) 兩分支；`framework.md` 依 R-VS37′ 重判並列鎖定前 9 項未解；`CrossZone Common` 更名完成；`spec_variables.tsv` 增 `suspect_prefix` 欄（**原值未改**）；`docs/reports/prefix_contamination.md` 產出 |
| **核實無誤** | 污染 4 筆（擴大掃描後不變）；反向命中 0；**Layer 2 四數 46／88／72／31 逐項相符**；委派合計 162+46+17+12=237；R-VS37′(3) 使 3 筆回歸 token 一致（31 包預言正確） |
| **正確地不動** | **未清除或改寫任何原值**（31 包 §3）；**未合併大小寫重複值**；**未改 `$Heated_Steats_Levels$`**；**未代擬 DR-18**；**未修訂 typo／別名判據**；**framework 未鎖定**；DR-15／DR-17 仍未送出 |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| W-47 值域欄 | `cfts044_include`／`cfts044_exclude`／`cfts044_other_arch`／`lid_values`／`dbc`／`lid_format`。**`cfts044_other_arch` 為 JSON（架構→值陣列），逐值展開**；其餘以 `\|` 分隔 |
| W-47 期望前綴 | 依序比對：`HSW_\|Heated_Steering`→`HSW_`；`VentedSeat\|Vented_Seat`→`VS_`；`HeatedSeat\|Heated_Seat\|Heated_Steats`→`HS_`。**順序有意義**（`Heated_Steering` 須先於 `Heated_Seat` 比對） |
| W-47 值中前綴 | `\b([A-Z]{2,4})_[A-Za-z]`，僅取 `{HS, VS, HSW}` 三個本 feature 語意前綴 |
| W-47 typo 判據 | **(a) 對稱側同位條文之值**（31 包 §5）；**(b) 同章節內是否兩形態並存**；**(c) 全文頻次**。(b)(c) 為本輪所加，理由見 §2.6 |
| W-48 配對 | 移除 `4858393`（A-VS49 之 typo 重複條）後 LF 29 ／ RF 29，**依文件順序逐位配對**。**未用 `difflib`**（14 輪已證其失效） |
| W-48 配對之驗證 | 逐位讀本文確認 `ECU`／句式／訊號名對應，非序列錯位 |
| W-48 值抽取 | `\[[^\]]{0,60}\]` 且含 `Seat` 或 `Press`。**該條件大小寫敏感，已知會漏 `pressed`** —— §2.3 之 2 筆假不對稱即源於此，逐條讀後已剔除 |
| W-49 Layer 2 歸屬 | token 含 `HeatedSteeringWheel`→HSW；`HeatedSeat`→Heated Seat；`VentedSeat`→Vented Seat；`CrossZone Common`→Heated Seat（依 31 包 §2 之隸屬）；其餘→Common Features |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS51** | **併入 DR-18（分析層擬）** | `4858413` 之值退化為 `[ Pressed]`，LF 對應條文為 `[Vented Seat Pressed / VS_PSD]`。⚠ 升級 |
| **A-VS52** | 同上 | 值域大小寫雙寫致 `$VentedSeatFR$` 之同一值算成五個 |
| **A-VS53** | 同上 | `$Heated_Steats_Levels$` token 本身為 typo（`Steats`） |
| **A-VS54** | — | 31 包 §5 之 typo／別名判據無法分辨「兩側一致地抄錯」與「真雙軌命名」 |

**無新開 DR** —— DR-18 之擬定屬分析層（31 包 §6 已如此排定）。
DR-15／DR-17 仍未送出；DR-11 未決（`HeatedSteeringWheel-009` 已標 `UNRESOLVED-SOURCE`）。

### 5.1 D-3 —— 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **4**（A-VS51／52／53／54） | **53**（相異編號；最大號 A-VS54，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **0** | 不變 |

§5 表列 4 筆，登記簿逐筆核對皆在，**差額 0**。`A-VS02` 缺號維持。

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **W-47 之期望前綴對照由本層手建，只涵蓋 `HS_`／`VS_`／`HSW_` 三個。**
   `spec_variables.tsv` 之 30 個 token 中，**16 個無期望前綴而被跳過**
   （`$ESS_ENG_ST$`／`$PowerMode$`／`$Hybrid_Type$` 等）。
   **其值域是否有同型交叉，本輪看不見。**

2. **W-48 只做了 Vented 兩節。**
   `1.3.1.1.3.*`（CUSW 遷入之四節）**未做逐位對照**，
   而 `4858001` 之 typo 正出自該節族 —— **同節族是否還有其他不對稱，未驗**。

3. **A-VS52 之大小寫重複只在 `$VentedSeat*$` 上量過。**
   其餘 29 個 token 之值域是否有同型重複，**未掃**。
   其後果為值域基數虛高，直接影響 TC 之列舉分支數。

4. **`framework.md` 之 Layer 2 歸屬由本層以 token 字串判定，未以 037 檔界驗證。**
   R-VS15 之 46／88／72／31 恰好相符，**但那是四數合計相符** ——
   **未逐 leaf 核對其是否真來自對應之 037 檔**。
   `CrossZone Common` 之 2 leaf 歸 `Heated Seat` 係依 31 包 §2 之文字，
   **其原始檔屬 HeatedSeat.xlsx 一事未驗。**
