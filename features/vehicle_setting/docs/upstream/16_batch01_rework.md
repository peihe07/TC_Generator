# 上繳 16 —— batch01 改寫（10 條）與 feature profile 建檔

執行層寫入。依據：`docs/handoff/35_pilot_review1.md` §5。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | 轉錄 R-VS41 ＋ 三處加註 | ✅ |
| D-3 | DR-19／DR-20 補入提問文 | ✅ **仍未送出** |
| D-4 | A-VS57／60／61 關閉 ＋ 兩數 | ✅ 見 §5.1 |
| **W-54** | 建 feature profile | ✅ **不新增任何規則** |
| **W-55** | batch01 改寫 → `batch01_v2.json` | ✅ **§9 僅餘 1 項不通過（DR-20）** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 W-55 改寫之覆蓋

| 項 | v1 | **v2** |
|---|---:|---:|
| TC 條數 | 10 | **10** |
| 訊號行（`$<MESSAGE>.<Signal>$ = <raw> (<label>)`） | 0 | **27** |
| 殘留已撤回之三件組 | 34 行 | **0** |
| 機械檢查違規總數 | 1 | **1**（同一項，見 §1.3） |
| Pre-Condition 之匯流排條目已置末位 | 7 條中 3 條非末位 | **7 / 7 置末位** |

`SwitchLHD/RHD-010`／`-011`／`ThirdRowHeadrestDump-025` 三條**無匯流排條目**
（其驗證不觸及 CAN），故無須置末位。

### 1.2 新增之機械驗證：`<raw> (<label>)` 對 DBC `VAL_` 逐字核對

`scripts/selfcheck_w53.py` 本輪加入 R-VS39／L-VS2 之檢查：
自兩份基線 DBC 讀入 **2,044 個 signal** 之 `VAL_` 表，
逐行核對 TC 中之 `<raw>` 與 `<label>`。

| 項 | 值 |
|---|---:|
| 受核對之訊號行 | **27** |
| `<label>` 與 DBC `VAL_` 不符者 | **0** |
| signal 不在基線 DBC 者（L-VS2） | **0** |

三個訊號之 DBC `VAL_` 逐字：

| signal | `VAL_` |
|---|---|
| `ESS_ENG_ST` | `1 ENS Stopped`／`2 ENS Request Start`／`3 ENS Running`／`4 ENS Stop Pending`／`5 ENS Start protection`／`6 ENS Start inhibit`／`7 ENS disabled`／`8 ENS_IHB_LATCH`／`9 ENS Starting`／`15 SNA` |
| `EngineSts` | `0 Engine_Off`／`1 Engine_Cranking`／`2 Engine_On`／`3 SNA` |
| `FL_HS_Tlm` | `0 Not_Pressed`／`1 Pressed` |

### 1.3 canon §9 十七項自檢（v2）—— **逐項**

| # | 項目 | 結果 |
|---|---|---|
| 1 | Test Set | **通過 10/10** —— `Common Features`，其粗粒度已由 profile `[OVERRIDE §4.1.3／§4.2]` 合法化 |
| 2 | tc_title | **通過 10/10** —— 7–12 字，無模態 |
| 3 | Pre-Condition 為觸發條件非環境前提 | **通過 10/10** —— 匯流排模擬器條目依 **R-VS41(2)／R-12a** 為工具型前置且置末位，非 §8.5 所指之環境穩定前提（35 包 §4 已裁，非本層自判） |
| 4 | Input Test Data 歸屬 | **通過 10/10** —— 全 `NA`（profile `[ADD]`） |
| 5 | 步驟可執行、末步驟擁有驗證 | **9/10；`SwitchLHD/RHD-010` 不通過**（DR-20，見 §2.1） |
| 6 | 步驟長度／意圖層級 | **通過 10/10** |
| 7 | 標準 snippet | **不適用** |
| 8 | CLI 步驟格式 | **不適用** |
| 9 | baseline | **通過** —— `SwitchLHD/RHD-011`（`record` → `compared with step 1`）；`ThirdRowHeadrestDump-025` 保留記錄步驟 |
| 10 | Procedure ↔ ER 1:1、ER 無模態、完整涵蓋 | **通過 10/10** |
| 11 | FP／FF | **通過** —— `Stop-Start-004`／`-005` 互為正負對照，本輪並補 `distinguishing_axis` |
| 12 | 追溯、不擴入 sibling、不造值、不造範圍 | **通過** —— `ThirdRowHeadrestDump-025` 之「再按一次」步驟依 35 包 §4 **刪除**（條文未定義再按之行為，寫其結果即造值） |
| 13 | Design Method | **通過** —— State Transition 3／Decision Table 2／Functional Based 5 |
| 14 | 四欄無尾句號 | **通過 10/10** |
| 15 | UI 標籤用 `"..."`，不用 `[...]` | **通過** —— 四個交付欄 0 方括號；`test_item` 之逐字方括號依 **profile `[OVERRIDE §11]`** 保留，非違規 |
| 16 | `specification_reference` | **通過 10/10** —— 皆 `CFTS044-<7位數>` 單值單行，合 R-VS41(3) |
| 17 | 來源優先、門檻為規格值、相近操作區辨、樣式化元件 | **通過** |

**機械化部分：10 條、1 項不通過**（與 v1 同一項，成因未變）。

### 1.4 W-54 profile 之內容核對

35 包 §2 所列五項全數落檔，**未新增任何規則**：

| 項 | 落檔 | cite |
|---|---|---|
| `[OVERRIDE §11]` test_item 方括號保留 | ✅ | R-VS6／R-S4；先例 Home A-H10 |
| `[OVERRIDE §4.1.3／§4.2]` Layer 2 粗粒度 | ✅ | R-VS4（Pei）；00 包 §3 |
| `[ADD]` 訊號依 canon §8.7.5 v3、網段入 Pre-Condition | ✅ | R-VS41(1)(2)；R-VS9(1)′(5) |
| `[ADD]` spec_ref 依 canon §10.7(a)，一行一個 | ✅ | R-VS41(3) |
| `[ADD]` input_test_data 一律 `NA` | ✅ | R-VS5 |

## 2. 不符項目（不自行調和）

### 2.1 `SwitchLHD/RHD-010` 之 §9 檢查 5 **仍不通過** —— 成因未變

該項於 17 輪即記為不通過（A-VS59），成因為 `4858560` 交叉參照未具名之 HMI 需求。
**本輪之改寫不觸及該成因**，故仍不通過。

**這不是新的不通過項** —— 升級條件逐字為「改寫後 §9 有**新的**不通過項」，
本輪之不通過項與 v1 為同一項、同一成因。**該升級條件未命中。**

在 DR-20 答覆前無法修正。

### 2.2 canon §8.7.5 v3 與本批之相容性 —— **無衝突，惟兩處須記明**

升級條件之一為「§8.7.5 v3 之形式與某條 TC 之內容不相容（具名該 TC 與衝突點）」。
逐條檢視後**未命中**，但有兩處是本層之處理選擇，非條文所明定：

**(a) `PROXI Driver_Side` 不套 `$` —— 依 §8.7.5(c)，非依 (a)**

`$DriverSide$` 於兩份基線 DBC **皆不存在**（`can_signal_map.tsv` 判 `NOT_IN_DBC`），
其 LID `can` 欄為 `PROXI`。依 §8.7.5(c)「PROXI 參數：`PROXI <Param> = <值>`，
前綴 `PROXI` 必寫，**不加 `$`**」，故 `SwitchLHD/RHD-009`／`-010`／`-011`
之 `PROXI Driver_Side = 1 (Right Side)` **不套 (a) 之 `$MESSAGE.Signal$` 式**。
其值取 **LID `Format`**（`0 = Left Side`／`1 = Right Side`），非 DBC —— DBC 無此參數。

**(b) `ThirdRowHeadrestDump-025` 全條無訊號行**

其驗證對象為軟鍵按壓與頭枕之實體位置，**無 CAN 觀察點**。
§8.7.5 之各式皆不適用，故該條之 procedure／ER **無 `$...$`**。
**這不是遺漏。**

### 2.3 `$EngRun_Stat$` 之兩組 DBC 對映 —— 本輪未再裁，維持 17 輪之選擇

17 輪 §2.6 已記：`EngineSts`／`STATUS_CCAN3`／CAN-B 與
`EngineSts_W`／`ENGINE_FD_2`／CAN-FD 兩列皆為 Atlantis High 欄組，R-VS9(1) 無法決定。

35 包**未觸及此點**，本層維持原選擇（`STATUS_CCAN3`），理由同 17 輪：
`$ESS_ENG_ST$` 亦位於該 message，而 `4858549`／`4858550` 要求同時評估兩訊號。

**仍為本層之選擇，非條文所定。** 若日後裁為 `ENGINE_FD_2`，
`Stop-Start-002`／`-003`／`-007` 之訊號行與 Pre-Condition 之網段條目須改。

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | `generated/batch01_v2.json` 10 條，27 個訊號行改依 canon §8.7.5 v3，殘留三件組 0；Pre-Condition 之匯流排條目 7/7 置末位；`ThirdRowHeadrestDump-025` 刪「再按一次」步驟；`Stop-Start-004`／`-005` 補 `distinguishing_axis`；`docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md` 建檔；`selfcheck_w53.py` 加入 DBC `VAL_` 逐字核對與三件組偵測；R-VS41 轉錄，R-VS9(3)／L-VS1／R-VS33′／R-VS14 加註；DR-19／20 提問文補入 |
| **核實無誤** | 27 個訊號行之 `<raw> (<label>)` 對 2,044 個 DBC signal 之 `VAL_` **逐字核對 0 不符**；L-VS2 之 signal 存在性 0 不符；§9 十七項逐項列出，僅餘 1 項不通過且成因未變 |
| **正確地不動** | **v1 `batch01.json` 保留不刪**（R-TM13）；**未修 `SwitchLHD/RHD-010` 之末步驟**（DR-20 前修即造值）；**未再裁 `$EngRun_Stat$` 之兩組對映**；**三條 PENDING 維持**；**profile 未新增任何規則**；**未寫回工作簿、未鎖定 framework、未執行 backlog** |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| 訊號書寫改寫 | 對 `test_procedure`／`expected_result` 逐式替換：`Send <sig> in <MSG> on <SEG> = ` → `Send the signal $<MSG>.<sig>$ = `；`Read <sig> in <MSG> on <SEG> and check that it is ` → `Read the signal $<MSG>.<sig>$ and check that it is `；`check that <sig> in <MSG> on <SEG> is ` → `check that the signal $<MSG>.<sig>$ is `；ER 之 `= v is registered` 與 `reads v` 兩式同理 |
| 改寫完整性之驗證 | **不以替換次數自證**，另以 `\b\w+ in [A-Z0-9_]+ on (CAN-B\|BH-CAN\|CAN-FD)\b` 反查殘留，v2 得 **0**、v1 得 **34**（同一支腳本、同一判準，兩本對照） |
| DBC `VAL_` | 以 `latin-1` 讀兩份基線 DBC，`^VAL_\s+\d+\s+(\w+)\s+(.*?);` 多行模式取表，再以 `(\d+)\s+"([^"]*)"` 取值對，共 **2,044 個 signal** |
| TC 訊號行之核對 | `\$[A-Z0-9_]+\.(\w+)\$\s*=\s*(\d+)\s*\(([^)]+)\)`，比對 `DBC_VALS[signal][raw] == label`（**區分大小寫**） |
| 規格 token 之殘留檢查 | `\$([^$]+)\$` 中**不含 `.`** 者視為規格 token（R-VS9(5)），`$MESSAGE.Signal$` 因含 `.` 而放行 |
| Pre-Condition 末位 | 以 `bus simulator` 命中者移至末位並重編號；未命中者不動 |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

**本輪新開 anomaly：0；新開 DR：0。**

**關閉 3 筆**：

| anomaly | 依據 |
|---|---|
| **A-VS57** | R-VS41(1) —— R-VS9(3) 撤回，canon §8.7.5 v3 勝，L-VS1 一併撤回 |
| **A-VS60** | W-54 之 profile `[OVERRIDE §11]` |
| **A-VS61** | W-54 之 profile `[OVERRIDE §4.1.3／§4.2]` |

**仍開啟且阻塞 TC 內容者**：A-VS58（DR-19，3 leaf）／A-VS59（DR-20，1 leaf）。

### 5.1 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **0** | **60**（相異編號；最大號 A-VS61，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **0**（DR-19／20 為 17 輪開立，本輪補提問文） | 未結 **9** |

§5 表列 0 筆新增，登記簿亦無新增，**差額 0**。另關閉 3。

### 5.2 未結 DR 清單（§8.4.3）

| DR | 阻塞？ | 影響 leaf | 提問文 | 狀態 |
|---|---|---:|---|---|
| DR-8／DR-12 | 不阻塞 | — | 早輪 | 未結 |
| DR-11 | 不阻塞 | 1 | 有 | 未送出 |
| DR-14′ | **阻塞** | 16 | 有 | 未送出 |
| DR-15 | **阻塞** | 160 | 有（已更正引用） | **未送出** |
| DR-17 | **阻塞** | 14 | 有 | **未送出** |
| DR-18 | 不阻塞（確認型） | 160 | 有 | **未送出** |
| DR-19 | **阻塞** | 3 | **本輪補入** | **未送出** |
| DR-20 | **阻塞** | 1 | **本輪補入** | **未送出** |

**5 份阻塞型待送**（DR-14′／15／17／19／20），共影響 **194 個 leaf**。

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **§9 之七項人讀項在 v2 仍是人讀。**
   17 輪 §6-1 已記；本輪加入之機械檢查（DBC `VAL_` 逐字、三件組殘留、
   規格 token 殘留）**只擴充了第 10、15 兩項之覆蓋**，
   檢查 3／6／7／11／12／13／17 仍無機械證據。

2. **`distinguishing_axis` 只補了 `Stop-Start-004`／`-005` 一對。**
   35 包 §4 只點名該對。其餘八條**未經 §4.6 之 sibling 比對** ——
   例如 `Stop-Start-002`（stop-start 啟用→指示燈熄）與 `-007`
   （SNA→不套抑制）是否為同一驗證點之正反面，**本輪未驗**。
   下批注入 `## Sibling Rows` 時應併驗此八條。

3. **profile 之 `[OVERRIDE §4.1.3／§4.2]` 合法化了粗粒度，但未解其下游後果。**
   §4.1.4 列 Layer 3 之四項用途，其一為「覆蓋分析之單位」。
   `Common Features` 之 46 leaf 橫跨 **7 個 Layer 3**，
   **以 Test Set 為單位之覆蓋分析在本 feature 不可行** —— 須改以 Layer 3 為單位。
   本輪未驗其是否可行。

4. **（本輪已補驗，改列為結果）** v1 與 v2 之逐欄比對：

   | 欄 | 差異 |
   |---|---|
   | `test_item` | **1 條**（`ThirdRowHeadrestDump-025`，其括號下半由「Single press, both restraints, lower only」改為「Single press, both restraints lower together」，配合刪步驟） |
   | `specification_reference`／`design_method`／`priority`／`split_flag`／`split_reason`／`test_set`／`tc_title`／`input_test_data` | **0** |

   即除訊號行、Pre-Condition 順序、`ThirdRowHeadrestDump-025` 三處外，
   **v2 與 v1 逐欄相同**。**此為量得，非由改寫腳本之程式碼推得。**

   > 原擬將此列為未驗項；因其可由前後比對直接量得，故本輪補做。
