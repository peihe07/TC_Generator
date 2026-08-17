# 10 — 欄位對應交叉驗證與首批 pilot 回覆（上繳）

上繳包 | 執行層 → 分析層 | 往返 NN = 10
結果：**九步全部完成。R-P73 已取得結論 —— A-PW40 成立。**
F1 接受並修正（TC 9 → 10 條）；F2、F3 附依據不修正。

---

## 0. 結論摘要

| 步驟 | 狀態 |
|---|---|
| 建立 `handoff/10_column_verify.md` | DONE（§A 6 區塊 / §J 6 列 / §H 9 步，自檢一致） |
| 1 G0 前置閘 | **PASS 7 / 7** |
| 2 B1 三方欄位交叉，驗 G52 / G53 | DONE —— **A-PW40 成立** |
| 3 G50 / G51，fixture 驗證 | DONE —— 五個 fixture 全如期 |
| 4 findings 分流，驗 G54 | DONE —— **實測 exit 仍為 0** |
| 5 `feature.yaml` 兩項訂正，重跑 G46 | DONE |
| 6 F1 / F2 / F3 回覆；TC 修正後重跑 lint | DONE —— **10 條 TC 全閘 PASS** |
| 7 §D 全表自驗 | DONE |
| 8 §A 六條抄入 RULINGS.md、§F 入 ANOMALIES.md | DONE（RULINGS R-P1–R-P78；ANOMALIES A-PW01–A-PW47 連續無缺） |
| 9 上繳 ＋ 更新 INDEX.md | DONE（本檔） |

---

## 一、B1 —— 三方欄位交叉驗證（R-P73 / R-P74，**上繳項一**）

全文見 `features/power/data/b1_column_crosscheck.md`。
三份工作簿皆 `read_only=True`，未寫入任何一份。

### 1.1 三份來源

| feature | 分頁 | 欄數 | 資料列 | 狀態 |
|---|---|---|---|---|
| **Power** | `Test Case Specification&Result` | **35** | 0（BLANK，G10） | 待產出 |
| Comfort | `Test Case Specification 測試用例規範` | 34 | 466 | 已交付、已驗收 |
| Privacy | `Test Case Specification 測試用例規範` | 34 | 11 | 已交付、已驗收 |

> **第一項發現：分頁名不同。** Power 為 `Test Case Specification&Result`，
> 另二者為 `Test Case Specification 測試用例規範`。二者為不同範本版本。→ A-PW47

### 1.2 G52 —— r9 逐欄三方對照

**三者一致之欄：15 / 35（A–O）。差異欄：P 起共 20 欄。**

| 欄 | Power | Comfort | Privacy | |
|---|---|---|---|---|
| A–O | 逐字相同 | 逐字相同 | 逐字相同 | ✓ 15 欄 |
| **P** | `Estimated Test Time (mins)` | `Test Case Priority` | `Test Case Priority` | ✗ |
| **Q** | `Test Case Priority` | `Estimated Test Time (mins)` | `Estimated Test Time (mins)` | ✗ |
| **R** | `Estimated Test Time (mins)` | `Test Case Design Methods` | `Test Case Design Methods` | ✗ |
| **S** | `Test Case Design Methods` | `Functional Safety` | `Functional Safety` | ✗ |
| **T** | `Functional Safety` | `HDCC27 Atl-Hi` | `HDCC27 Atl-Hi` | ✗ |
| U–AA | 七個車型欄 | `DT27` … `Test Case Author` | 同 Comfort | ✗ |
| **AB** | `Test Case Author` | `Test Version` | `Test Version` | ✗ |
| … | … | … | … | ✗ |
| **AI** | `Remarks` | （無此欄） | （無此欄） | ✗ |

**Comfort 與 Privacy 之 r9 完全一致**（皆 34 欄，末欄 `AH` = Remarks）。
差異形態為：**Power = Comfort/Privacy 於 P 位置插入一欄 `Estimated Test Time`，
其後每欄右移一格**。

### 1.3 G53 —— 兩個 `Estimated Test Time` 之權威（R-P74）

判準（R-P74 指定）：已交付件實際填寫哪一欄。

| feature | 資料列 | `Estimated Test Time` 欄 | **非空列數** |
|---|---|---|---|
| Comfort | 466 | Q | **0 / 466** |
| Privacy | 11 | Q | **0 / 11** |

**該欄於已交付件中從未被填寫。** 故 Power 之 P 與 R **二者皆留空**，
權威問題在實務上不存在。語義上 Power 之 **R** 對應另二者之 Q（右移後之原欄），
**P** 為新插入者；因一律不填，此區分不影響寫回。

### 1.4 附帶查得之一項分歧（A-PW46）

| feature | 七個車型欄 | 非空列數 |
|---|---|---|
| Comfort | 全部填 `1` | **466 / 466** |
| Privacy | 全部留空 | **0 / 11** |

**兩份「已知 good」對車型欄之處置相反。** Privacy 之留空符 R30-3 / R30-4，Comfort 則否。
與 R-P54（Power 維持留白）直接相關。
**此例顯示「已交付」不足以單獨作為權威** —— 本包不裁，登記待決。

### 1.5 結論 —— **A-PW40 成立**

`scaffold` 之錯為**兩層疊加**：

1. scaffold 之值（priority `P` / design_method `Q` / functional_safety `R` / author `Z`）
   為 **A-PV13 / R39-2 訂正之前**的版本。Privacy 已訂正為 `R` / `S` / `AA`，
   **Power 之 scaffold 從未套用該訂正**。
2. Power 之範本又較 Comfort / Privacy 多插入一欄，其後再右移一格。

**09 包所填之對應與本次交叉結果完全一致**：
`tc_id F` / `priority Q` / `design_method S` / `functional_safety T` /
`author AB` / `remarks AI`。

---

## 二、B2 —— G50 / G51 與 findings 分流（R-P75 / R-P76，**上繳項二**）

### 2.1 G50（§11）與 G51（§4.4）

| 閘 | fixture | 期望 | 實際 |
|---|---|---|---|
| G50 | 無句點、雙引號、方括號僅訊號值 | （無） | （無） |
| G50 | **行以句點結尾** | `§11` | **`§11`** |
| G50 | **UI 標籤用方括號** | `§11` | **`§11`** |
| G51 | pre_conditions 僅述狀態與環境 | （無） | （無） |
| G51 | **pre_conditions 含動作**（`Connect the …`） | `§4.4` | **`§4.4`** |

> **一項例外須登記**：G50 初版把 `[spec-derived]` 之 source-class 標記判為違規，
> 致既有 fixture 全滅。查 Comfort 之已交付 TC 即以 `1. [spec-derived] …` 書寫 ——
> 該為 §3.2 之既有慣例。已於 G50 明文豁免行首之 source-class 標記。
> **這是第三次「合成 fixture 未涵蓋真實慣例」**（前二次見 A-PW45）。

### 2.2 G54 —— findings 分流（R-P76）

`run_all_gates()` 回傳 `(阻斷類, 待人工裁決類)`；**R-P42(b) 不計入 exit code**。

合成 fixture 實測：

```
[PASS] G54 findings 分流（R-P42(b) 觸發，exit 仍為 0）
        阻斷類 0 項（期望 0）；待人工裁決類 1 項（期望 ≥ 1）
        → R-P42(b) NR1L-PowerManagement-001: 內容逐字引用未被引用之錨點 `4941009` …
```

真實檔案輸出格式：

```
檢查 10 個 TC

【阻斷類】PASS

【待人工裁決類 —— R-P42(b)，依 R-P67 不自動判 FAIL】（無觸發）
```

R-P67 自此不再只存在於紙上。

---

## 三、B3 —— `feature.yaml` 兩項訂正（R-P77）

| 欄位 | 原 | 現 | 依據 |
|---|---|---|---|
| `done_region.author_value` | `"Arif"` | **`""`** | R-P77(a) / A-PW43 |
| `write_back.fill_test_group_set` | `false` | **`true`** | R-P77(b)；本 workbook 為 BLANK（G10） |

二項已納入 G46 之 `YAML_EXPECTED`（現五項），repo 現況通過。

> **過程中修正 G46 一個 bug**：其欄位正則 `[^"#\n]+?` 要求至少一字元，
> **無法匹配 `author_value: ""` 之空值** —— 若不修，訂正後之正確值反而會被判 FAIL。
> 已改為 `(?:"([^"]*)"|([^"#\n]*?))`。

---

## 四、B4 —— F1 / F2 / F3 之逐項回覆（**上繳項三**）

### F1 —— **接受並修正**

§5.7「不同 trigger 即拆分」成立：轉入 Standby 與轉入 Bench 為**兩個不同觸發**，
非同一觸發之兩個後果。§8.3 壓力測試亦成立 —— Standby 抑制正確而 Bench 誤顯示時，
原合併之一條無法給出明確判讀。

原 `002` 拆為二條，全批重新連號：

| tc_id | req_id | tc_title |
|---|---|---|
| 002 | `SWE-PM-071-02` | No splash screen when TLM passes to Standby |
| 003 | `SWE-PM-071-03` | No splash screen when TLM passes to Bench |

**TC 數 9 → 10。** leaf 涵蓋仍為 3。`reasoning` 已載明拆分依據與 F1 之出處。

### F2 —— **不接受修正；附逐字引用結案**

「10 秒」**出自 `4942354` 本文，非造值**。該錨點末句逐字為：

> Unless defined otherwise, TLM shall stay in this state until either voltage out of
> range conditions are satisfied or shall go back to normal behavior **10 seconds after
> STATUS_LIN.Batt_ST_Crit becomes [0h]**.

與 `SplashScreen_Time` 之情形不同：後者規格**只給參數名而未給數值**，故不編秒數；
前者規格**直接寫出 10 seconds**，引用即為忠實。已於該 TC 之 `split_reason` 附上逐字引用。

### F3 —— **不接受修正；附 §12 first-match 逐條走查**

§12 之順序為：Negative → Fault Injection → **State Transition** → **Decision Table** → …

`006`（現 `007`）Load Shed 之走查：

| 列 | 條件 | 命中？ |
|---|---|---|
| 1 | Invalid input / illegal op | ✗ 訊號為合法值 `[1h]` |
| 2 | Simulated fault | ✗ 訊號係主動送出，非模擬故障 |
| 3 | **State A → State B transition** | **✗ 見下** |
| 4 | Multiple conditions → outcome | **✓ 命中** |

**未於第 3 列命中之理由**：TLM 之「狀態」在本 feature 有明確定義 ——
CFTS009 §1.6.2.1.1–.13 所列之 Full-Operation / Idle / Partial Operation / Timed /
Standby / Sleep / Bench / Logistic ×3 / Init。
Load Shed **不是其中任何一個**，規格亦未將其命名為 TLM status；
其效果為音量上限、靜音、ICS 斷電，**TLM 之 status 全程不變**。
而觸發條件為 `PN14_LS_Actv = [1h]` **AND** `PN14_LS_Lvl7 = [1h]` 之合取 ——
正是第 4 列之「multiple conditions → outcome」。

`008`（現 `009`）Battery Critical 同理：條件為 `Batt_ST_Crit = [1h]`
**AND**（BODY ON **OR** BODY OFF-TIMED），TLM status 亦不變。

**對照組**：`010`（Battery Critical 回復）判為狀態轉換 —— 因其正是「離開 critical
handling 狀態、回到 normal behavior」，有明確之 A→B。
`002` / `003` 亦然：規格逐字寫「TLM has not to pass to **Standby status** nor to
**Bench status**」，其 A→B 為具名 status。

**執行層自陳**：09 §七第 4 項曾示警「first-match 順序理解偏差會系統性偏向同一值」。
本次走查後，10 條之分布為 狀態轉換 6 / 決策表 2 / 功能測試 1 / 故障注入 1 ——
狀態轉換佔 6 成，但每一條皆可指出其具名之 A→B status，非因順序理解偏差而落到同一值。

---

## 五、§D 全表實測值對照（**上繳項四**）

| # | 項目 | 期望值 | 實測值 | 判定 |
|---|---|---|---|---|
| G0 | 七份原始檔 SHA256 | 7 / 7 | 7 / 7 | PASS |
| **G52** | 三方 r9 交叉 | 【實測填入】 | **一致 15 / 35**；Power 獨有差異 20 欄（P–AI，整體右移一格）；Comfort = Privacy | 已填空 |
| **G53** | 兩個 `Estimated Test Time` 之權威 | 【實測填入】 | **Comfort 0/466、Privacy 0/11 —— 從未填寫**；二者皆留空 | 已填空 |
| **G50** | §11 閘門 | 正常 PASS、違規實際 FAIL | 3 fixture 全如期（1 PASS + 2 FAIL） | **PASS** |
| **G51** | §4.4 閘門 | 正常 PASS、違規實際 FAIL | 2 fixture 全如期（1 PASS + 1 FAIL） | **PASS** |
| **G54** | findings 分流 | 待裁決節有內容且 exit = 0 | **阻斷 0、待裁 1、exit = 0** | **PASS** |
| **G55** | 首批 lint 重跑 | 全閘 PASS；leaf 涵蓋仍為 3 | **10 條全 PASS**，0.27 秒；**leaf 3**；R-P42(b) 0 觸發 | **PASS** |
| G45–G49 | 沿用 | — | 未變（G47 之 TC 數 9→10，leaf 仍 3） | PASS |

`--self-test`：**28 個 TC fixture ＋ G46 三案 ＋ G54 全數如期。無 MISMATCH。**

---

## 六、**明確回答：R-P73 是否已取得結論，寫回可否開放**（**上繳項五**）

### R-P73 —— **已取得結論，(a) 成立**

三者 r9 之 A–O 十五欄逐字相同；差異僅為 P 起之整體位移；
**Comfort 與 Privacy 兩份已交付件互相印證**（r9 完全一致）。
錯位者為 scaffold，非 Power 之 workbook。09 包所填之對應完全正確。

### 寫回可否開放 —— **執行層之建議：可就欄位對應開放，惟另有二項應先裁**

R-P73 所設之阻斷條件已解除。但本包查出兩項**與寫回直接相關而尚未裁定**者：

1. **A-PW46 —— 七個車型欄之處置，兩份已交付件相反。**
   Comfort 逐列填 `1`（466 列），Privacy 全數留空（11 列）。
   R-P54 裁 Power 維持留白，但該裁定作成時**尚不知 Comfort 之作法與之相反**。
   寫回時這七欄要不要填，目前有兩個互相矛盾的先例。

2. **A-PW47 —— 範本版本不同，r9 以外之差異未比對。**
   Power 35 欄、分頁名不同；資料驗證（DV）、公式、其他分頁是否亦有差異，**未查**。
   Comfort 之 DELIVERY.sha256 記有 `DV P10:Q601 / T10:Z601 / AF10:AF601` 等
   資料驗證範圍 —— 那些欄字母是 Comfort 之座標，套到 Power 會整體偏移一格。
   **若 Power 之 DV 範圍亦存在且範圍不同，寫回可能觸發驗證錯誤。**

**故：欄位對應本身已可信；寫回之開放建議俟上述二項裁定後為之。**
此為執行層之建議，開放與否屬分析層之裁定。

---

## 七、獨立判斷：本包是否仍有該驗而未驗者（**上繳項六**）

09 上繳包 §七之五項，本包處置：第 1 項→R-P73（已取得第二來源）；
第 2 項→R-P75（G50 / G51 已入 lint）；**第 3 項→未處置**（樣本仍不足，見下）；
第 4 項→F3（已附 first-match 走查）；第 5 項→B4 之 pilot review。

### 7.1 就第 3 項之現況（下放包指定為未處置）

首批 10 條 TC 之 R-P42(b) **仍為 0 觸發**。累計樣本 10 條、0 觸發 ——
**比 09 包時多 1 條，統計上無實質變化**。R-P67 所要求之「真實偽陽性率」
仍無法估計。須待第二批以後累積至數十條。

### 7.2 新增未驗項（五項）

**1.（最重）r9 以外之範本差異完全未比對。**
   B1 只比對了 r9 標頭。Power 與 Comfort/Privacy 為不同範本版本（A-PW47），
   而**資料驗證範圍、公式、其他分頁**皆未比對。
   Comfort 之交付紀錄明載 DV 範圍為 `P10:Q601` / `T10:Z601` / `AF10:AF601` ——
   若 Power 亦有 DV 而範圍以 Comfort 之欄字母設定，**寫回時會落在錯誤的欄上**。
   這與 A-PW40 是同一類錯誤，只是換了一個屬性。

**2. 「已交付」被當作權威，但兩份已交付件互相矛盾。**
   A-PW46 顯示 Comfort 與 Privacy 對車型欄的處置相反。
   R-P73 之交叉方法建立在「已交付、已驗收，屬已知 good」之假設上 ——
   該假設在 r9 標頭上成立（二者一致），**在資料內容上不成立**。
   本次結論之可信度僅及於「標頭」這一個屬性。

**3. G50 之 §11 覆蓋不完整。**
   §11 尚有「no HTML / Markdown tables」與「blank line between fields」二項未實作；
   §11 之例外條款（profile-scoped 逐字引用之 token）亦未實作 ——
   **而 Power 根本沒有 profile**（`docs/runtime/profiles/` 無 Power 檔，
   其餘七個 feature 皆有）。此為一項先前未登記之缺漏。

**4. G51 之動詞清單為我自行列舉，未經任何來源佐證。**
   §4.4 給的是判準（「requires do / check / confirm → NOT a Pre-Condition」）
   與若干範例，**未給動詞清單**。我列了 20 個動詞。
   漏列者不會被攔下，誤列者會誤殺 —— 二者皆未量測。

**5. F3 之走查建立在「TLM status 之清單」上，而該清單是我從 CFTS009
   §1.6.2.1.1–.13 讀出的。**
   若 CFTS010 另有定義 Load Shed 為一個 status，我的論證即不成立。
   **我只查了 CFTS009 之狀態清單，未在 CFTS010 全文搜尋 Load Shed 是否被命名為 status。**

---

## 八、禁區遵守聲明

| 禁區 | 遵守情形 |
|---|---|
| **不得寫回 FW036 workbook（R-P73 未取得結論前一律不開放）** | **未寫回任何 workbook。** B1 之三份皆 `read_only=True` |
| 不得執行任何 git 操作 | 本包執行期間未執行任何 git 指令 |
| 不得以 openpyxl save 寫任何 xlsx | 未呼叫 `save()` |
| 不得補齊 `SWE-PM-089`（R-P1） | 未補 |
| 不得沿用純文字衍生物之任何數字（R-P10） | 全部數字自原始檔重生 |
| 不得自行調整 §C 正則 | `SEC_RE` / `REQ_RE` 一字未改 |
| 不得修改任何已落檔裁決條文之內文（R-P36） | 未動任何 `[R-Pnn]` 區塊內文 |
| 不得測試未被引用之錨點（R-P42） | 10 條 TC 皆只引三個被引用錨點；R-P42(b) 0 觸發 |
| 不得解析任何 RTF 或 OLE stream 之內容 | 未讀任何 RTF 或 OLE stream |
| 不得續行章節層反向缺口調查（R-P37） | 未做任何章節層量測 |
| 不得變更 §E 之分布數字（R-P35） | 63/24/16/8/3 未動 |
| 不得以 A-PW29 之存在逕行填寫車型欄（R-P54） | **未填**；A-PW46 之分歧僅登記待裁 |
| 不得調整 `MIN_FINGERPRINT`（R-P62） | 維持 40 |
| **不得擴大批次範圍超出 `Power Down` 3 leaf** | **leaf 仍為 3**。TC 由 9 增為 10 係 F1 所命之拆分，非範圍擴大 |
| **不得以 repo 現況作為任何 fixture 之測試對照** | 28 個 fixture 與 G46 之違規 yaml 全為合成。B1 讀已交付件係 R-P73 明令之第二來源，非 fixture |
| **B1 讀 Comfort / Privacy 工作簿一律 `read_only=True`** | **已遵守**，二者位於客戶樹，未做任何寫入 |
| 素材補入超出 `inputs/` 需 Pei 裁定 | 未補入任何素材 |

---

## 九、待裁

- **Q1（寫回前）A-PW46：七個車型欄之處置，兩份已交付件相反。**
  Comfort 填 `1`（466/466）、Privacy 留空（0/11）。R-P54 作成時尚不知此分歧。
- **Q2（寫回前）§七第 1 項：r9 以外之範本差異未比對** ——
  尤其資料驗證範圍。Comfort 之 DV 為 `P10:Q601` / `T10:Z601` / `AF10:AF601`，
  以 Comfort 之欄字母設定；Power 若比照，會落在錯誤的欄上。
- **Q3 §七第 2 項：「已交付」作為權威之限度。** 本次結論僅及於「r9 標頭」一個屬性。
- **Q4 §七第 3 項：Power 無 profile**（`docs/runtime/profiles/` 無 Power 檔，
  其餘七個 feature 皆有）。§11 之 profile-scoped 例外因此無所依據。
- **Q5 §七第 4 項：G51 之動詞清單為執行層自行列舉，未經來源佐證。**
- **Q6 §七第 5 項：F3 之走查未在 CFTS010 全文確認 Load Shed 是否被命名為 status。**
- **Q7 首批 10 條 TC 之內容覆核**（F1 拆分後）。
- **Q8 寫回是否開放** —— R-P73 已解除，惟建議俟 Q1 / Q2 裁定後為之。
