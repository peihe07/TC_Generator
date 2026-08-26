# DELIVERY NOTE —— Power Moding HMI（FW036 / SWE.6）

- feature：`power_moding`　**Test Group**：`Disclaimer screen`
- 交付基底：`FM-WI-FSM-036-A01 …_SWQT_20260817_ext.xlsx`（R-PMH7，SHA256 `6372fb6b…`）
- 工作副本：`output/…_PowerModing_20260826_writeback_rev2.xlsx`
  （SHA256 `01e917b88e050ce1f164db1f1121ea9fe665bae34bcfa5e153c03d1f322f248c`）
- 產生日：2026-08-26　撰寫依據：39 包 §四步驟 7（R-PMH149）

> **本文件與「已知未決清單」併為一份**（39 包步驟 8 令執行層擇一）。
> **理由**：二者之讀者相同，且第 (b)(c)(d) 節之每一項在未決清單中皆有其對應筆；
> **分立會使同一件事在兩份文件裡各說一次，而其中一份先過期。**
> 未決清單為本文之 **§8**。

---

## 1. 交付範圍

| 項 | 數 |
|---|---|
| 037 之 leaf 全集 | **48** |
| **有 TC 之 leaf** | **45** |
| 停手（不寫入工作簿） | **3** |
| **TC 條數** | **51** |
| 其中**封鎖**（已產出、不可執行） | **4** |
| 工作簿寫入列 | **r10 – r60**（51 列） |

**45 + 3 = 48。** 工作簿之 `Test Case Specification 測試用例規範` 分頁自 r10 起 51 列，
其餘分頁一律未動。

| Test Set | TC |
|---|---|
| `Splash Screen` | 3 |
| `Disclaimer Screen` | 8 |
| `Startup Animation` | 10 |
| `Startup Sounds` | 7 |
| `Power Transitions` | 8 |
| `Power Off Behavior` | 8 |
| `Voice Assistant Key` | 5 |
| `Off Road Plus` | 2 |

---

## 2. 不寫入工作簿之三筆 —— **1 停手 ＋ 2 依裁定結案**（此為裁定之結果，非遺漏）

| leaf | outline | 037 之 Requirement Title | 依據 | **所需之上游輸入** |
|---|---|---|---|---|
| `SWE1-HMI-PM-002` | 7.1.1 | Power Button Transitions during Ignition Off | **R-PMH117** ＋ **R-PMH151**（Pei 裁定 2026-08-26） | **無 —— 依 R-PMH151 結案**。其行為逐字委於 `based on vehicle architecture. See CFTS009 for clarification.`，**行為定義在外部規格 CFTS009，屬該規格 owner 之 SWE 需求範圍**（canon §8.4.2），不得由本 feature 吸收 |
| `SWE1-HMI-PM-023` | 10.5 | Headunit Functionality during Key OFF Power ON | **R-PMH111**（條件式，停手待答） | **`DR-PMH8`／`DR-PMH5` 之 (1)(2)**：p9 能力矩陣之權威來源。其斷言之謂詞正是「`Headunit` 於 `KEY OFF (No ACC)` × `HEADUNIT POWER ON` 下之可用程度」，與 p9 同格同一謂詞 |
| `SWE1-HMI-PM-028` | 12.2 | CFTS009 Behavior Reference | **R-PMH72** ＋ **R-PMH151**（Pei 裁定 2026-08-26） | **無 —— 依 R-PMH151 結案**。其內文逐字為 `OFF2.) Please refer to CFTS009 for complete behavior.`，同上 |

> ⚠ **`-002` 與 `-028` 為 out of scope（經裁定不寫入）；`-023` 仍在範圍內，只是暫不產出。**
> **三者之狀態詞因而不同**（`ACCEPTED`／`ACCEPTED`／`STOPPED-PENDING-DR`），此為刻意。
>
> ⚠ **`3` 之組成（R-PMH151，2026-08-26）**：**3 = 1 停手（`-023`）＋ 2 依裁定結案（`-002`／`-028`）**。
> **`CFTS009` 自此不再是本 feature 之待取件** —— 取得與否不改變本輪交付；
> 若日後取得且上游要求納入，屬**範圍變更**，另案。**§1 之統計數字不因本條而變。**

---

## 3. 封鎖四條 —— **已產出、不可執行**

| tc_id | leaf | 其 ER |
|---|---|---|
| `NR1L-DisclaimerScreen-046` | `SWE1-HMI-PM-026-02` | 螢幕關／音訊關 |
| `NR1L-DisclaimerScreen-047` | `SWE1-HMI-PM-026-03` | 螢幕開／音訊關 |
| `NR1L-DisclaimerScreen-048` | `SWE1-HMI-PM-026-04` | 螢幕關／音訊開 |
| `NR1L-DisclaimerScreen-049` | `SWE1-HMI-PM-026-05` | 螢幕開／音訊開 |

**四條之 `test_procedure` 逐字相同而其 `expected_result` 互斥** ——
同一組步驟執行一次只會落在一類，**四條之中至多一條能通過，其餘三條必然 fail**。
其為 canon §7 之 **false fail**（因設計而失敗，非因缺陷）。

**成因**：`VRLP1` 逐字為 `Radio status after interaction with SIRI **depends on
outcome of the interaction**`，**而規格與 037 皆未言如何使結果落在某一類**。

**其 `Remarks` 欄載**：
`[BLOCKED-UNTIL-DR] DR-PMH8 Q9 — applicable condition for each outcome not stated in the specification.`

**解封二路**（`DR-PMH8` Q9 之答覆）：
(甲) 答覆載明各類之條件 → **四條各加其條件為 Pre-Condition，封鎖解除**；
(乙) 答為「四者皆為可能之結果而無條件之分」→ **四條併為一條**。
**二路皆須屆時另裁。**

---

## 4. 兩處「未涵蓋」實為追溯之位置，**其行為已被驗證**

037 於兩處以**兩個 leaf** 承載同一行為。依 **R-PMH137**，
該行為由任一 leaf 之 TC 涵蓋即為已涵蓋；於另一 leaf 記 `未涵蓋`。

| leaf | 其 DESC 之該斷言 | **實際驗證它的 TC** |
|---|---|---|
| `SWE1-HMI-PM-001-01` A1 | `When driver door is closed, the system plays a 3-second startup animation.` | **`NR1L-DisclaimerScreen-012`**（掛 `SWE1-HMI-PM-006-01`） |
| `SWE1-HMI-PM-003` A2 | `No timeout is provided for Maserati applications, see CFTS009.` | **`NR1L-DisclaimerScreen-007`**（掛 `SWE1-HMI-PM-001-05`） |

> **請勿將此處之 `未涵蓋` 讀成 `未驗證`** —— **該二行為皆有 TC 驗到，只是該 TC 掛在另一個 leaf。**
> 補一條即為重複驗證（canon §8.2.1 明禁），故不補。

**另有一處為真正之未涵蓋**：`SWE1-HMI-PM-012` A3
（`Sounds will sync amongst all supported vehicle displays.`）——
**啟動音側已驗，告別音側未驗**（A-PMH23），其繫於 `DR-PMH8` Q3。

---

## 5. `Product Document 記錄封面頁` —— **依裁定整張留空**

Pei 於 2026-08-25 裁定不填（**R-PMH145**）。

> ⚠ **本項與語料之多數不同**：交付母體 16 檔中，該分頁 **4 空／12 填**。
> **本欄之留空是一個選擇，不是遺漏。**

其依據非多數，而為三項成本：五個欄位之字串須由我方自擬；
`B4` 取檔名即依賴上游命名（與 R-PMH26(d) 相衝），其值不得自客戶那份複製（與 R-PMH23 相衝）；
`B7` 帶資料驗證而現行三項寫回檢查不涵蓋之。

---

## 6. 其他刻意留空之欄位

| 欄 | 處置 | 依據 |
|---|---|---|
| `D3`／`D4`／`D5` | **留空** | **R-PMH27** —— 其母體語料為 `D5` 9 空／7 非空且非空者有六種互不相容之格式；`D3`／`D4` 四次量測皆全空 |
| `Q`（Estimated Test Time） | **留白** | **A-PMH12** —— 該欄之資料驗證為 priority 之列舉 `"P0,P1,P2,P3"`，**任何分鐘數皆會被 Excel 擋下**。其為母本之缺陷，非本 feature 之選擇 |
| `T`–`Z`（車型欄） | 留白 | profile §3.8 |
| `Cover 封面` 之作者欄 | **留空，待裁** | 母體 17 檔實測：**11 空／6 非空**，非空者為兩個他人姓名，**無一為本 feature 之作者**；「依慣例填」之前提不成立（§8 之未決） |

---

## 7. `outline 9.1` 之 `source_clause` 取自 SYS1 —— **及其已具名之風險**

`SWE1-HMI-PM-018-01`～`-05`（5 leaf）之 `source_clause` **取自 SYS1 匯出，非規格 PDF**
（**R-PMH75**，Pei 裁定 2026-08-25「以刪掉之後的為主」）。
規格 PDF 之該句本身損壞（含 `aofnd`、新舊兩版疊寫），SYS1 之版本為刪去舊文字後之定稿。

> ⚠ **承擔之風險**：PDF 側之 `the radio should shut Off`（逾時後收音機關機）
> **不會有任何一條 TC 驗到** —— 其為已被裁定排除之舊文字。
> **若上游日後主張該行為仍屬需求，ch 9 之覆蓋即有缺口。**

---

## 8. 已知未決清單（R-PMH132(b)）—— **11 筆**

> **交付日至而 `DR-PMH5`／`6`／`7`／`8` 有任一未 `ANSWERED` 者，以現況交付**，
> 其 TC 不因未覆而延（R-PMH121／R-PMH132(a)）。**下表即該規則所要求之揭露。**

| # | 判定之所在 | 所繫之 DR | 答覆為何值時改為何（節錄） |
|---|---|---|---|
| 1 | `matrix_vs_chapter.VERDICT[(9, 1, 15)]` —— 矩陣 `r15`（`Key-off`）× `PM1)` 之記法，現為 `待定義` | `DR-PMH5` (1)(2)／`DR-PMH7` Q1（`VP`）／`DR-PMH8` Q4（二延遲 | **逐值**：(甲) `VP` = head unit 顯示螢幕 **且** 二延遲名同指 → **改記 `牴觸`**（同謂詞相反值，條件完全重合）；(乙) `VP` = head unit 顯示螢幕 **而** 二延遲名為不同設定 → **仍記 `牴觸`惟其範圍縮小**，須重寫其依據並登記條件；(丙) `VP` **非** head unit 之顯示螢幕 → **改記 `未對照`**（無共同謂詞），與二延遲名之答覆無關；(丁) 任一問未獲答覆 → **維持 `待定義`**… |
| 2 | `gen_batch02.py` 之六條 TC 各二項事件層限定中，因 `r46`／`r47` 而納入者（R-PMH95 之涵蓋兩讀） | `DR-PMH7` Q2（`Else: Mute Active` 之記法） | **逐值**：(甲) 答為「**使之靜音**」（事件使 mute 變為 active）→ **限定正當，維持不動**，並將該二列由 `待定義` 改記 `牴觸`；(乙) 答為「**維持靜音**」（mute 狀態不變）→ **該二列改記 `未對照`**，而**六條之第二項限定即為過度限定** —— 其不致誤判，惟使 TC 較規格所需為窄；**須逐條評估是否移除**（移除須重跑 lint 之限定字串檢查，因 `limits` 宣告隨之改變）；(丙) 未獲答覆 → 維持現狀（限定保留… |
| 3 | `gen_batch02.py` 之 `-013`（`Once a Day`）之 procedure 與 `-011` 之 pre_condition | `DR-PMH8` Q1（「一日」之起算點）／Q2（設定之所在路徑） | **逐值**：(甲) Q1 答為具體起算點（午夜／點火週期／滾動 24 小時）→ **`-013` 之步驟須重寫**，以該起算點表述其「第二次觸發」之時點，並增一項 input_test_data；(乙) Q1 答為「未定義／由實作決定」→ **維持現狀**（現行措詞 `on the same day` 於三讀皆成立），並將此登記為永久限度；(丙) Q2 答為具體路徑 → **`-011` 之 pre_condition 改寫為該路徑**，其 `test_procedure`… |
| 4 | `ANOMALIES.md` 之 **A-PMH23**（告別音之跨螢幕同步無 ER 斷言）與 `gen_batch02.py` 之 `-010` | `DR-PMH8` Q3（`Sounds will sync amongst all supported | **逐值**：(甲) 答為「涵蓋二者」→ **`-010` 之 ER 須增一條**（告別音於各支援螢幕間同步）**且其 procedure 須增一步**（維持 1:1），A-PMH23 改 `RESOLVED`；(乙) 答為「只涵蓋啟動音」→ **`-010` 不動**，A-PMH23 改 `ACCEPTED（經釐清不補）`；(丙) 答為「只涵蓋告別音」→ **`-009` 之 ER4 須移至 `-010`**（此讀法目前未被任何產出所採，其後果最大）；(丁) 未答 → 維持… |
| 5 | `gen_batch03.py` 之 `Power Transitions` 各 TC 之 Pre-Condition `No phone call or projection call is | `DR-PMH8` Q5（IGN OFF 後通話結束且有 popup 待顯示時之行為） | **逐值**：(甲) 答為「**應 stay awake**」（`PM1)` 優先）→ **該 Pre-Condition 得移除**，且**應增一條 TC** 驗「通話結束後 popup 仍顯示」；`r31`／`r32` 之記法由 `牴觸` 改為 `未對照`（矩陣該格須更正）；(乙) 答為「**應關機**」（矩陣優先）→ **該 Pre-Condition 保留**，且 `PM1)` 之條件須加註例外；**應增一條 TC** 驗「通話結束即關機」；`r31`／`r32` 改… |
| 6 | `matrix_vs_chapter.VERDICT[(9, 1, 6)]`／`[(9, 19, 24)]`／`[(9, 19, 25)]` —— 三列現為 `待定義` | `DR-PMH7` Q1（`VP` 之定義） | **逐值**：(甲) `VP` = head unit 之顯示螢幕 → **三列逐列重判**，其中 `r25`（`VP Turns Off` 於 key-off 狀態門開啟）**極可能改記 `牴觸`**（與 `PM1)` 之 stay awake 期間可同時成立而取相反值）；(乙) `VP` 為他物（如儀表板顯示）→ **三列改記 `未對照`**；(丙) 未答 → 維持 `待定義`。⚠ **本筆與第 1 筆之差別**：`r15` 另受 A-PMH24 所阻，即使本問獲答仍可能… |
| 7 | `Power Transitions` 組（batch 3）之全部斷言 —— 其是否須依 R-PMH94 重掃 | `DR-PMH5` (1)(2)（p9 能力矩陣之權威來源） | **逐值**：(甲) 答為「另有文件」並提供之 → **該文件為第七筆素材**，須補 `MANIFEST.sha256`，**batch 3 之全部斷言須依 R-PMH94 對其重掃一次**（R-PMH111 末段明令）；(乙) 答為「p9 自身即權威」→ **batch 3 之各 TC 須逐條複驗 R-PMH111 之判別法結果**（原判「不倚賴 p9」者仍成立，惟其依據由「來源不明」改為「主題不同」）；A-PMH18 改 `RESOLVED`；(丙) 未答 → 維持現狀，… |
| 8 | `spec_assertion_scan.IGNOFF_LINE_VERDICT[160]` —— 規格 p4 之 `Note: do not show popup again if popu | `DR-PMH7` Q3（該 `Note:` 之適用範圍） | **逐值**：(甲) 答為「**泛指所有 popup**」→ **改記 `牴觸`** —— 於 Radio Off 已顯示過之 popup 於 IGN OFF 不得再顯示，與 batch 3 之斷言取相反值；**`-016`～`-021` 須加 Pre-Condition「本次點火週期內該 popup 尚未於 Radio Off 顯示過」**；(乙) 答為「**僅適用於同段之 `Geolocation + SOS Popup`**」→ **改記 `未對照`**，batch 3… |
| 13 | `generated/batch03.json` 之 `stopped` 中之 **`-023`**（`PITA8`）—— 停手待答，**非 out of scope** | `DR-PMH5` (1)(2)（p9 能力矩陣之權威來源） | **逐值**：(甲) 答為「另有文件」→ 取得後 **`-023` 得撰寫 TC**，`Power Transitions` 組由 5 leaf 有 TC 增為 **6**；(乙) 答為「p9 自身即權威」→ **`-023` 得撰寫，惟其斷言須逐條套 R-PMH111 之判別法並具名**；(丙) 答為「p9 無權威來源」→ `-023` **改判 out of scope**，其狀態詞屆時方改為 `ACCEPTED`，`n_leaf` 46 → **45**；(丁) 未答 … |
| 14 | `gen_batch01.py` 之 `-008`（leaf `-022-02`）—— 其 DESC 之例外 `unless certain phone call scenarios have | `DR-PMH8` Q8（該 `certain` 指哪些情境） | **逐值**：(甲) 上游列舉該等情境 → **`-008` 之 pre_condition 須增其排除**，且**應評估是否另立 TC 驗該例外之行為**（其時該例外即成為可驗之行為）；(乙) 答為「無特定情境／該句為贅語」→ **`-008` 不動**，該例外自 DESC 之涵蓋要求中移除；(丙) 未答 → **`-008` 之射程持續不足**，其於「已知未決清單」中具名。⚠ **037 之 DESC 於同處亦未列舉** —— 非 SYS1 側之偏差，而是上游本身未定義… |
| 15 | `generated/batch06.json` 之 `-050`／`-051`／`-052`／`-053` 四條 —— **標 `BLOCKED-UNTIL-DR`，已產出而不可執行**（R | `DR-PMH8` Q9（四種互動結果各自之適用條件） | **逐值**：(甲) 答覆**載明各類之條件** → **四條各加其條件為 Pre-Condition，`BLOCKED` 解除**，其 procedure 之步驟 1 隨之具體化；(乙) 答為「**四者皆為可能之結果而無條件之分**」→ **四條併為一條**（其 ER 為「結果為所列四類之一」），並依 R-PMH137 於其餘三 leaf 記 `未涵蓋-重複`；**二路皆須屆時另裁，R-PMH142 明言不預判**；(丙) 未答 → **四條維持封鎖，隨交付附其封鎖依據**… |

### 8.2 本輪已結之 5 筆（**其原文依 R-TM13 保留，不刪**）

| # | 判定之所在（節錄） | 結案詞 | 所依條號 | 結案語 |
|---|---|---|---|---|
| 9 | `gen_batch03.py` 之 `-017` —— `60 秒無互動` 與 `總計 10 分鐘` 二上限**何者先到即何者生效**，本條以二個獨立步驟分別 | **`ACCEPTED-RISK`** | **R-PMH152** | 不另開問；`-017` 之二上限交互作用不斷言，其風險依裁定為**終態**（§9 第 8 項） |
| 10 | `ANOMALIES.md` 之 **A-PMH25**（9.1 權威文本於逾時處為破句）與 `-016` 之不斷言處置 | **`ACCEPTED-RISK`** | **R-PMH152** | 不另開問；`-016` 之逾時秒數不斷言，其風險依裁定為**終態**（§9 第 7 項） |
| 11 | `gen_batch04.py` 之 `-024` **撤除**（R-PMH129）—— `SU1.)` 之「動畫後呈現 splash，1.5 each」一句無 | **`CLOSED-BY-RULING`** | **R-PMH150** | 照既定預設排除 —— 037 未載者不納入本輪交付，永久登記為覆蓋缺口（§9 第 5 項） |
| 12 | `ANOMALIES.md` 之 **A-PMH28**（p3–p7 流程圖之五類行為）—— 依 **R-PMH131** 不寫 TC | **`CLOSED-BY-RULING`** | **R-PMH150** | 同上（§9 第 4 項） |
| 16 | `gen_batch02.py` 之 `-012`／`-013` —— 其 `source_clause` 主語為 `start-up **and** good | **`RESOLVED-BY-R-PMH147`** | **R-PMH147** | `-012`／`-013` 已擴涵蓋告別音側（各 ER5 明載 `goodbye`，ER6 為其總結），**實測已涵蓋** |

> **其「逐值」欄之原文未刪** —— 仍在 `DECISIONS.md` 之 `PENDING-ON-DR` 登記簿內；
> **本表只縮為結案語**（R-TM13：不刪除，加註保留）。
> ⚠ **第 9／10 筆日後若上游主動釐清，屬 Revise 批次**，屆時依其原載之 (甲)(乙) 路處置，**R-PMH152 不預判**。

### 8.1 未結 DR

| DR | 狀態 | 其所繫之未決 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | `-023` 之停手；p9 矩陣之權威來源 |
| `DR-PMH6` | `SENT` 2026-08-25 | RVC 情境下 HVAC popup；三項無需求之行為 |
| `DR-PMH7` | `SENT` 2026-08-25 | `VP` 之定義；`Else: Mute Active`；`Note:` 之範圍 |
| **`DR-PMH8`** | **`DRAFT`（9 問，其中 2 為附註）** | **其 Q9 封鎖四條**；**Q1–Q5、Q8 另繫五筆未決**；**Q6／Q7 為告知性附註（R-PMH150），不繫任何未決** |

---

## 9. 本交付未涵蓋者（一次列全）

1. **停手一筆**（`-023`）**與依裁定結案二筆**（`-002`／`-028`）之行為（§2）；
2. **封鎖四條**之行為（§3）—— 其 TC 已寫入而不可執行；
3. `SWE1-HMI-PM-012` A3 之**告別音跨螢幕同步**（§4）；
4. **p3–p7 流程圖**所載而散文所無之**五類行為**（A-PMH28／R-PMH131；**依 R-PMH150 屬裁定排除**）——
   其中 `If vehicle supports more than 1 Splash screen, toggle them one after
   another with a 1.5 timeout each` 直接落在 splash 各條之標的內；
5. `SU1.)` 之 `after the animation (3 sec) a splash screen is presented timeout
   (1.5 each).` —— **該句於 SYS1 匯出 0 命中，037 因而無其 leaf**（A-PMH29／R-PMH129；
   **依 R-PMH150 屬裁定排除**）；
6. **9.1 之 `the radio should shut Off`**（§7）；
7. `-044` 之 `hard control` 接聽路徑與 `-041` 之 `ACC`／`RUN` 其一（A-PMH31）——
   **其「同結果故不拆」為推定，規格未言其實作為同一路徑**；
8. **`-016` 之逾時秒數**（`the 60-second timeout defined in the pop-up list` 之逾時本身）
   **無任何 TC 驗到**（A-PMH25／**R-PMH152**，`ACCEPTED-RISK`）——
   **與第 6 項之 `the radio should shut Off` 同源而非同項，故分列**；
9. **`-017` 之二上限交互作用**（`60 秒無互動` 與 `總計 10 分鐘` 何者先到即何者生效）
   **無任何 TC 驗到**（**R-PMH152**，`ACCEPTED-RISK`）—— 規格未言其優先。

---

## 10. 本交付之驗證狀態

| 項 | 狀態 |
|---|---|
| lint（32 項 × 6 批） | **32/32 全數通過** |
| DESC 逐斷言涵蓋（正向） | 60 斷言／45 leaf，**未涵蓋 3**（皆列於 §4） |
| DESC 反向涵蓋 | 155 ER 斷言，**無依據 0** |
| 寫回三項前置閘 | **通過**；其故意失敗三項**全被攔下** |
| 四項不變量 | 分頁數／DV 組數（含 x14）／`last_capacity_row`／B 欄公式 —— **前後全同** |
| 母本 | **未被動過**（SHA256 前後同值，實測） |
| **Excel 之四點確認** | **屬 Pei** —— 程式層之檢查代替不了它 |
