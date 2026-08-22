# 上繳 15 —— 首批 TC 生成（10 條）

執行層寫入。依據：`docs/handoff/34_pilot_batch.md` §3。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | 轉錄 R-VS19″／R-VS40；A-VS55 關閉 | ✅ |
| D-3 | 建 `docs/reports/BACKLOG.md` | ✅ 10 項凍結 |
| D-4 | 更新 framework 阻塞項第 1 | ✅ **已解**，另增三項 |
| **W-53** | 首批 10 條 ＋ §9 自檢 | ⚠ **十七項中 1 項不通過，3 項須裁** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 leaf 選取

| 項 | 值 |
|---|---:|
| Layer 2 = `Common Features` 之 Functional leaf | **46**（R-VS15，符） |
| 排除 `$HdRstRelRq$` 引用者（DR-14′） | **4** |
| 排除 `delegate = pending`（DR-17） | **0** |
| 排除 `delegate = blocked`（R-VS17） | **0** |
| 排除 reqid 為空（DR-11） | **0** |
| **可用 leaf** | **42** |
| **本批取用（reqid 升冪前 10）** | **10** |

**42 ≥ 10 —— 「選出之 leaf 不足 10」之升級條件未命中。**

取用之 10 個 leaf：`Stop-StartSystem-002`～`-007`（6）、
`SwitchLHD/RHDConfiguration-009`～`-011`（3）、`ThirdRowHeadrestDump-025`（1）。

### 1.2 訊號解析（R-VS9(1)′：拼寫取 DBC、對映取 LID）

| 規格 token | DBC signal | message | 網段 | DBC `VAL_` 逐字 |
|---|---|---|---|---|
| `$ESS_ENG_ST$` | `ESS_ENG_ST` | `STATUS_CCAN3` | CAN-B | `1 ENS Stopped`／`3 ENS Running`／`4 ENS Stop Pending`／`7 ENS disabled`／`15 SNA`（共 10 值） |
| `$EngRun_Stat$` | `EngineSts` | `STATUS_CCAN3` | CAN-B | `0 Engine_Off`／`1 Engine_Cranking`／`2 Engine_On`／`3 SNA` |
| `$FL_HS_RQ$` | `FL_HS_Tlm` | `TELEMATIC_VEHICLE_SETUP3` | BH-CAN | `0 Not_Pressed`／`1 Pressed` |
| `$DriverSide$` | **不在 DBC**（PROXI） | `Car_Configuration_1` | PROXI | LID Format `0 = Left Side`／`1 = Right Side` |

`$DriverSide$` 依 §8.7.5(c) 寫為 `PROXI Driver_Side = <值>`，**不加 `$`**。

### 1.3 canon §9 十七項自檢 —— **逐項列出**

| # | 項目 | 結果 |
|---|---|---|
| 1 | Test Set 名詞片語、能力層級、合 `framework.md`、無 Test Group 前綴、無 `Unclassified`／`Misc` | **通過（但見 §2.4）** —— 10 條皆 `Common Features`，即 framework 之 Layer 2 |
| 2 | tc_title 三形之一、2–14 字、sibling token 可見、無模態 | **通過 10/10** —— 機械檢查字數 7–12，無模態 |
| 3 | Pre-Condition 僅狀態／環境，且為規格觸發條件非環境穩定前提 | **通過 10/10** —— 人讀；皆為配備、設定、匯流排連接與畫面可見狀態 |
| 4 | Input Test Data 欄位歸屬正確 | **通過 10/10** —— 全部 `NA`（R-VS5） |
| 5 | 步驟可執行、無禁用動詞、末步驟擁有驗證 | **9/10 通過；`SwitchLHD/RHD-010` 不通過**（見 §2.3） |
| 6 | 步驟長度與意圖層級 | **通過 10/10** —— 人讀；一般步驟 ≤12 字，末步驟 ≤18 字 |
| 7 | 標準 setup snippet 逐字重用 | **不適用** —— `ENTER_DEALER_MODE` 等四個常數皆與本批無關 |
| 8 | CLI／tooling 步驟採描述 ＋ `$` 指令 | **不適用** —— 本批無 shell／adb 步驟 |
| 9 | 需要前後比較時建立 baseline | **通過** —— `SwitchLHD/RHD-011` 與 `ThirdRowHeadrestDump-025` 採 §5.6 之記錄／比較式（`record` → `compared with step 1`） |
| 10 | Procedure ↔ ER 1:1、ER 可觀察、**ER 無模態動詞**、完整涵蓋 | **通過 10/10** —— 機械檢查步數相等、無 `shall/will/should/would` |
| 11 | 無 FP／FF；列舉支援項須配負向 | **通過** —— 本批無「列舉支援項」型；`Stop-Start-005`（greyed-out）與 `-004`（保持可選）互為正負對照 |
| 12 | 追溯 Req／SWRA、不擴入 sibling、不造值、不造範圍 | **通過（附說明）** —— 見 §1.4 之委派記載 |
| 13 | Design Method 於 procedure 定稿後指派 | **通過** —— State Transition 3／Decision Table 2／Functional Based 5 |
| 14 | 四欄之每個 numbered item 無尾句號 | **通過 10/10** —— 機械檢查 0 違規 |
| 15 | UI 標籤用 `"..."`，不用 `[...]` | **通過於四欄；`test_item` 不通過**（見 §2.2） |
| 16 | `specification_reference` 列出所有直接驗證之章節 | **通過 10/10** —— 皆 `CFTS044-<7位數>` 單行，格式機械驗證 |
| 17 | 來源優先於索引匯出；門檻為規格值；相近操作於 ER 區辨；樣式化元件不假設不可操作 | **通過** —— `Stop-Start-005` 之 greyed-out 未斷言不可操作（§8.7.4） |

**機械化部分之最終結果：10 條、1 項不通過**（`selfcheck_w53.py`）。

### 1.4 §8.2.1 之委派記載（不擴入 sibling）

| TC | 未涵蓋之行為 | 擁有者 |
|---|---|---|
| `Stop-Start-003` | 開關之啟用／灰階結果 | `4858551`／`4858553` |
| `Stop-Start-007` | 「未配備 Stop-Start 車輛」之完整行為 | 本 Req 之外（§8.4.2） |
| `SwitchLHD/RHD-009` | Driver／Passenger 標籤互換 | `4858561` |
| `SwitchLHD/RHD-011` | `CFTS044-348`／`-325`／`-393`／`-371` 之各按鈕需求 | 該四條各自擁有 |

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **訊號書寫形式：下放包所引之 R-VS9(3) 與 TC 規則書 §8.7.5 直接衝突**

下放包 §3 逐字：`procedure 訊號斷言須 <signal> in <message> on <網段>（R-VS9(3)）`。

而同包 §3 令本輪起適用之 `docs/runtime/ASPICE_SWE6_AI_Instruction.md` §8.7.5 逐字：

> **v1 之三件組 `<Signal> in <MESSAGE> on <segment>` 與 v2 之
> `Send CAN:` 前綴式皆已撤銷**
> (a) 訊號一律以 `$<MESSAGE>.<Signal>$` 全名書寫，值採 `= <raw> (<label>)`

**二者不可同時滿足。** 本層採 **R-VS9(3)（三件組）**，理由具名如下：

| 依據 | 內容 |
|---|---|
| (1) | R-VS9 為 **Pei 裁定**（2026-08-20）；§8.7.5 之撤銷署名為**分析層下放包 12／17／19**，且其為 **time_management 之包**（`R-TM13`、「下放包 17 §三」） |
| (2) | 下放包 §3 之欄位規則是**針對本輪本任務之最具體指令**，且明文引 R-VS9(3) |
| (3) | §8.7.5 §0 之衝突條款為「**feature profile 之 cited override 勝過本文件之通則**」；本 feature **無 profile 檔**（`docs/runtime/profiles/` 下 9 份，無 VehicleSetting），R-VS9 實質承擔該角色 |

**本層不裁定此衝突，僅陳報並具名所採之讀法。**
若裁為 §8.7.5 形式，**本批 10 條之 procedure 與 ER 全數須改寫**（每行皆受影響）。
→ **A-VS57**，`framework.md` 阻塞項第 10。

**兩形式之實質差異**：`$MESSAGE.Signal$` 帶 message 但**不帶網段**；
R-VS9(3) 之理由（兩份 DBC 之 141 個共有 signal 中 128 個起始位元不同）
所要防的正是網段不明。

### 2.2 ⚠ **`test_item` 上半之方括號與 §11 衝突，且本 feature 無 profile 可援引例外**

§11 逐字：「Square brackets `[...]` … MUST NOT appear in TC output fields」，
其例外為 **profile-scoped**（「may retain the source's notation **when the feature
profile says so**」）。

而 R-VS6／R-S4 要求 `test_item` 上半為**來源逐字**，
CFTS044 原文即含 `[IDLE_STBL//UNLIMITED//LIMITED//RUN]`、`[ENS_DSBL]`、
`[SNA]`、`[Right Drive]`、`[Pressed]` 等方括號 token。

**本 feature 無 profile 檔，無從援引該例外。** 本層採「逐字優先」——
四個交付欄（pre_conditions／input_test_data／test_procedure／expected_result）
**已全數無方括號**（機械驗證 0 違規），方括號僅存於 `test_item` 上半之逐字段。
→ **A-VS60**。

### 2.3 ⚠ **升級：`SwitchLHD/RHD-010` 之 §9 檢查 5 不通過，且在 DR-20 前無法修正**

`4858560` 逐字：`the HMI shall be modified as defined by HMI requirements` ——
**未具名任何文件、章節或需求 ID**。

其 TC 之末步驟因此無可寫之驗證目標：
寫具體修改項即違 §8.4.1／§8.4.2（造值／造範圍），
寫「HMI is modified」則違 §6（不可觀察）。

依 §8.4.3 填 `PENDING: DR-20`，**該欄不留空、不填 NA**。
**§9 檢查 5（§5.5 末步驟擁有驗證）記為不通過**，
符合升級條件「canon §9 自檢有項目不通過而無法修正」。→ **A-VS59**。

### 2.4 ⚠ **`EngRun_Stat` 之規格值於 LID 與 DBC 皆無對應 —— 三個 leaf 阻塞**

| 來源 | 值域 |
|---|---|
| LID `Format`／DBC `EngineSts` | `Engine_Off`／`Engine_Cranking`／`Engine_On`／`SNA` |
| CFTS044 `4858551`／`4858553`／`4858555` 所用 | **`IDLE_STBL`／`UNLIMITED`／`LIMITED`／`RUN`** |

四者**在 LID 與 DBC 中皆不存在**。依 **R-VS9(2)**「兩者不一致時停下回報，
**不自行調和**」，本層未作任何對映（例如未把 `RUN` 讀為 `Engine_On`）。

三條 TC 之相應步驟填 `PENDING: DR-19`。
符合升級條件「某 leaf 之 TC 無法在不違反 §8.4.1 之下寫出」——
**具名**：`SWE1-VC-Stop-StartSystem-004`／`-005`／`-006`；
**缺何值**：`IDLE_STBL`／`UNLIMITED`／`LIMITED`／`RUN` 之匯流排對應。
→ **A-VS58**。

### 2.5 Layer 2 `Common Features` 觸 §4.1.3 之「too coarse」反樣式

§4.2／§4.1.3 禁止「catch-all 吸收互不相關之能力」，
其判準為「以此 Test Set 過濾工作簿，是否得到**有意義之群集**」。

`Common Features` 為 **037 之檔界**，其 46 個 leaf 含
Stop-Start System、Switch LHD/RHD、Third Row Headrest Dump、ScreenOFF、
PHEV Features、Features Enable Criteria —— **彼此無共用 setup，無共用 UI 進入路徑**。

R-VS4 為 Pei 所裁且 framework 已建，**本層不改**。
惟 §4.2 之「same Test Set implies a shared setup pattern and UI entry path」
在本批 10 條上**明顯不成立**（Stop-Start 走 Climate 畫面＋CAN-B，
Third Row Headrest Dump 走軟鍵＋實體致動）。→ **A-VS61**。

### 2.6 `$EngRun_Stat$` 有兩組 DBC 對映，本層取其一並具名

| LID scope | signal | message | DBC |
|---|---|---|---|
| Atlantis High | `EngineSts` | `STATUS_CCAN3` | `PDT27_E2A_R4_BHCAN.dbc` |
| Atlantis High | `EngineSts_W` | `ENGINE_FD_2` | `PDT27_E2A_R5_FDCAN8.dbc` |

兩列皆為 Atlantis High 欄組，**R-VS9(1) 無法在其間決定**。
本層取 `EngineSts` / `STATUS_CCAN3` / CAN-B，理由：
同一批 TC 之 `$ESS_ENG_ST$` 亦位於 `STATUS_CCAN3`，
而 `4858549`／`4858550` 之條文要求**同時**評估兩訊號 ——
置於同一 message 與同一網段方能同步觀察。
**此為本層之選擇，非條文所定。** 若裁為 `ENGINE_FD_2`／CAN-FD，
`Stop-Start-002`／`-003`／`-007` 之步驟須改寫。

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | `generated/batch01.json` 首批 **10 條**；`scripts/selfcheck_w53.py`（§9 可機械化部分）；`docs/reports/BACKLOG.md` 10 項凍結；`RULINGS.md` 轉錄 R-VS19″／R-VS40 並註記 R-VS19′ 被取代；A-VS55 關閉；`framework.md` 阻塞項第 1 已解、另增三項；DR-19／DR-20 開立 |
| **核實無誤** | 46 個 Common Features leaf（符）；42 可用 ≥ 10；四個 token 之 DBC／LID 解析；§9 十七項逐項列出，機械化部分 1 項不通過 |
| **正確地不動** | **未把 `RUN` 讀為 `Engine_On`**（R-VS9(2) 停下回報）；**未為 `4858560` 編造修改項**；**未裁定訊號書寫形式之衝突**；**未改 Layer 2 之 `Common Features`**；**未寫回 036 工作簿**；**未鎖定 framework**；**未執行任何 backlog 項**（R-VS40）；DR-15／17／18／19／20 **皆未送出** |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| Layer 2 歸屬 | `data/_leaf_origin.json`（16 輪 W-52 自四份 037 檔逐儲存格抓 `SWE1-VC-…-\d{3}` 建立），取 `Common Features` 者 |
| `$HdRstRelRq$` 排除 | `leaves.tsv` 各欄接合後 `re.search(r'HdRstRelRq', txt)` —— **裸名形態**（R-VS36 之 (2)），未限 `$X$` |
| reqid 升冪 | `leaf_to_reqid.tsv` 之 `CFTS044-(\d{7})`，以該 leaf 之**最小** reqid 為排序鍵，同值以 `swe_id` 次序 |
| DBC `VAL_` | 以 `latin-1` 讀 `inputs/PDT27_E2A_R4_BHCAN.dbc`／`…R5_FDCAN8.dbc`（檔為 ISO-8859，**以 UTF-8 讀會失敗**），正則 `^VAL_\s+(\d+)\s+<signal>\s+(.*?);` 多行模式 |
| DBC 位元屬性 | `^\s*SG_\s+<signal>\s*:\s*(\S+)` |
| signal ↔ message ↔ 網段 | `data/can_signal_map.tsv`（LID 側），取 `lid_scope` 為 `Atlantis High` 或 `Atlantis(&High)` 之列；網段依 R-VS9(4) 由 DBC 檔名決定 |
| §9 機械化自檢 | `scripts/selfcheck_w53.py` —— **尾句號之規制單位為 numbered item 非物理行**（§11），續行併入其 item 後再判 |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS57** | —（條文衝突，非資料缺口） | 訊號書寫形式：R-VS9(3) 三件組 vs TC 規則書 §8.7.5 v3；本 feature 無 profile 檔。⚠ 影響每一條 procedure／ER |
| **A-VS58** | **DR-19** | `EngRun_Stat` 之 `IDLE_STBL`／`UNLIMITED`／`LIMITED`／`RUN` 於 LID 與 DBC 皆無對應。⚠ 阻塞 3 leaf |
| **A-VS59** | **DR-20** | `4858560` 交叉參照未具名之 HMI 需求，§9 檢查 5 不通過。⚠ 阻塞 1 leaf |
| **A-VS60** | 併 A-VS57 | `test_item` 上半之逐字方括號與 §11 衝突，無 profile 可援引例外 |
| **A-VS61** | — | Layer 2 `Common Features` 為 037 檔界，觸 §4.1.3 「too coarse」反樣式 |

**新開 DR：DR-19（阻塞 3 leaf）、DR-20（阻塞 1 leaf）** ——
依 §8.4.3「DR 登記於該 feature 之 DATA_REQUESTS.md」開立，
**提問文待分析層擬**（本層不代擬）。**二者皆未送出。**

**A-VS55 依 R-VS19″ 關閉。**

### 5.1 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **5**（A-VS57～61） | **60**（相異編號；最大號 A-VS61，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **2**（DR-19／DR-20） | 未結 DR：DR-8／DR-11／DR-12／DR-14′／DR-15／DR-17／DR-18／DR-19／DR-20 |

§5 表列 5 筆，登記簿逐筆核對皆在，**差額 0**。另關閉 1（A-VS55）。

### 5.2 未結 DR 清單（§8.4.3 要求每包上繳附）

| DR | 阻塞？ | 影響 leaf | 狀態 |
|---|---|---:|---|
| DR-11 | 不阻塞 | 1 | 未送出 |
| DR-14′ | **阻塞** | 16 | 未送出（本批已排除其 4 個 Common Features leaf） |
| DR-15 | **阻塞** | 160 | 已定稿，**未送出** |
| DR-17 | **阻塞** | 14 | 已定稿，**未送出** |
| DR-18 | 不阻塞（確認型） | 160 | 已定稿，**未送出** |
| **DR-19** | **阻塞** | **3** | **本輪開立，未送出** |
| **DR-20** | **阻塞** | **1** | **本輪開立，未送出** |
| DR-8／DR-12 | 不阻塞 | — | 早輪，未結 |

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，四項**

1. **§9 之十七項中有七項為人讀，無機械證據。**
   檢查 3（Pre-Condition 為觸發條件而非環境前提）、6（步驟長度）、
   7（snippet）、11（FP／FF）、12（上游分解）、13（方法適配）、17（來源優先）
   **皆由本層目視判定**。`scripts/selfcheck_w53.py` 只涵蓋十項。
   **pilot review 是這七項的唯一關卡。**

2. **本批未取用 `## Sibling Rows` 注入，故 `duplicate_of`／`distinguishing_axis` 一律未輸出。**
   `Stop-Start-004`（保持可選）與 `-005`（灰階）之區分 token 僅靠 tc_title，
   **未經 §4.6 之正式 sibling 比對**。若二者實為同一驗證點之正反面，本批看不出來。

3. **`ThirdRowHeadrestDump-025` 之第 3 步驟（再按一次不上升）為條文之否定面。**
   條文逐字為 `The switch is only to lower the head restraints, and not to raise them`。
   本層將其寫為可觀察之步驟，**但條文未定義「再按一次」時應發生什麼** ——
   保持下放為本層之讀法，非條文所明載。**§8.4.1 之邊界，請 pilot review 判。**

4. **十條之 `pre_conditions` 皆含「CAN-B／BH-CAN 連接匯流排模擬器」之類條目。**
   依 §8.5，其為**測試執行之環境前提**而非規格觸發條件，
   **嚴格讀應刪除**。本層保留之，理由為無該條目則步驟中之訊號送出無從執行。
   **此為本層對 §8.5 之讀法，未經裁定。**
