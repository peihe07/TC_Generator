# 上繳包 04 — vsm_v43：W-5‴ 以 LID `Atlantis` 欄組重跑

日期：2026-09-01　執行層　對應下放包：`docs/handoff/04_signal_atlantis.md`
sha8 報 **`body_sha8`**。R-VT1–R-VT10 取自**台帳**；R-VT11–R-VT14 台帳尚無，取樹外 `--out`（R-VT10(a)）。
台帳**不重生**（R-VT14(c)：改由 Pei 提交前一次）。

---

## 〇、一句話結論

**W-5‴ 八項全數執行。E10‴／E26／E27／E28 相符；E25 依掃描條件而異（20 或 21，已定位到單一儲存格）；
E29 字面 3 列／實質 247 列，兩讀法並列；E30 差值 0。**

| 項 | 結果 |
|---|---|
| **E27 `解得` = 0** | ✅ v3 之「解得 41」全數重判為 `段3待ATL-Mi DBC`（R-VT13(b)） |
| **E28 B-1 = 0** | ✅ |
| **K-1 複驗** | `STATUS_CCAN3.*` 於 Atlantis 欄命中 **2** 處；`BRAKE1.*` 命中 **0** 處 → R-VT13(c) 獲證 |
| **R-13 28 → 21** | Atlantis 欄命中者撤除 7 列（6 為 E26 所指者＋1） |
| **重音三名全解** | 第六規則生效，其一升為 `UI+PROXI 雙路徑` |
| **新登執行層自誤** | **A-VT23**：v2／v3 之 `PROXI路徑` 判準含 catch-all，**39 應為 35**；四名為偽陽性 |

**本包最該讀的一句**：內部訊號 **83 名，第四輪擴充仍是零變動**（規則→欄→檔→**欄組**）。
DR-VT4 已升為與 DR-VT1 同級，這是對的。

## 一、結果三分法（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | 段 1 改綁 `Atlantis` 欄組；v3「解得 41」重判為待件；R-13 28→21；第六規則落實；值域增二值；A-VT16／A-VT19／A-VT20 轉 RESOLVED；**v4 之 8 列誤指派段 2 主值撤除（R-VT12(a)）**；`RECON.md` §7 全面更新 |
| 核實無誤 | E10‴ **12/12**；E26 = 6；E28 = 0；`訊息名不符` 之 21 列與 v3 之 28 列逐列可追；Atlantis High ⊆ Atlantis（10 ⊂ 21）；六偽陽性標記維持 |
| 正確地不動 | 台帳**不重生**（R-VT14(c)）；`LOOKUP_MISSES.md` 仍未寫；**不重抽名**；A-VT23 之四名**不擅自設排除旗標**（待裁）；E25／E29 之兩讀法**並列不擇一**；段 3 對 Atlantis High DBC 之實查**只記旁證，不作判準** |

---

## 二、W-5‴ 逐項

### 1. 抽名（不重抽；標記 A-VT21 六偽陽性）

母體維持 **230**；`排除(A-VT21)` 欄標記六名（`CAN Node 35 (TBM)`／`CAN node 24 (PAM )`／
`CAN node 24 (PAM)`／`Component`／`Impact`／`Implementation`），**不刪**。

> **本包另發現同型四名**（`LTM`／`TBM`／`Unit`／`Resolution`，見 §六 A-VT23），
> 於 v4 逐列標記但**未設排除旗標** —— 04 包第 1 項只指 A-VT21 之六名，
> 擴充排除清單非執行層可為。併計後 PROXI 抽名偽陽性為 **10**，母體應由 49 降為 **39**（待裁）。

### 2. 段 1：LID `Atlantis` 欄組為主、`Atlantis High` 為旁證

**掃描條件（R-G8 揭露）**：LID 14 分頁逐頁定位表頭；
`CAN Mapping` 之 `Atlantis` = P（Signal Name）／Q（CAN），`Atlantis High` = Z／AA；
`Proxi & Configuration` 只有合併欄組 `Atlantis & Atlantis High` = P／Q；
`* Specific Signals` 分頁為單一 `Signal Name`／`CAN`。
三欄（`Logical Identifier`／`Function`／`Object Text`）逐字 ＋ 規則 1–6。

**儲存格內多值切分**：見 §三 E25 與 A-VT24 —— 一格可含兩個訊號名且**不以換行分隔**。

**第六規則（重音正規化）命中 3 名**，逐列備註記「重音正規化」（R-VT13(e)）：

| 規格原名 | v3 | **v4** |
|---|---|---|
| `DRL_Menù_Enable` | 未解得(止於段1) | **PROXI路徑(R-P375b/c)** |
| `Horn_Chirp_Menù` | 未解得(止於段1) | **PROXI路徑(R-P375b/c)** |
| `Greeting_Lights_Menù` | 未解得(止於段1) | **UI+PROXI 雙路徑** |

### 3. HMI Settings List：`Technical Reference` 先篩（R-VT14(b)）

**F 欄實測（E29）**：`Settings` 分頁 F 欄非空 **384** 列，相異值 **38**。

| 讀法 | 列數 | 說明 |
|---|---|---|
| **含 `VF665` 字面**（判準原文） | **3** | `VF665` ×1、`VF230/VF665, CFTS022` ×2 |
| **含 `665`** | **247** | 涵蓋 `VF230/665` ×**235**、`VF230/665/CFTS022` ×5、`VF230/440/665` ×2、`VF230/665/046` ×1、`VF230/665/247, CFTS101` ×1、上列 3 列 |

> **回報而不調和**：F 欄之實際寫法是 **`VF230/665`**（235 列，佔含 665 者之 95%），
> 即 VF230 與 VF665 共用之設定項。判準原文「含 `VF665`」逐字讀只得 3 列，
> 先篩形同虛設。**兩讀法並列，交裁。**
> **對最終結果無影響**：R-VT14(b) 定「候選集未命中者再對全表」，故命中集合與讀法無關；
> 差別只在**先取哪一列作錨點**與備註所記之 `Technical Reference` 值。
> 本包依判準原文以 3 列候選集先比，未命中再對全表；命中列之 F 值一律入備註。

**HMI 命中 4 名**，其中 3 名同時命中 PROXI → 依 R-VT14(a) 記新值 **`UI+PROXI 雙路徑`**：

| 規格原名 | v3 | **v4** |
|---|---|---|
| `Cornering_Lights` | UI路徑(R-P375b) | **UI路徑(R-P375b)** |
| `Auto_Park_Brake_Menu` | PROXI路徑 | **UI+PROXI 雙路徑** |
| `Geolocation_Menu` | PROXI路徑 | **UI+PROXI 雙路徑** |
| `Side_Distance_Warning` | PROXI路徑 | **UI+PROXI 雙路徑** |
| `Greeting_Lights_Menù` | 未解得(止於段1) | **UI+PROXI 雙路徑**（重音正規化） |

雙路徑之備註逐列記：`UI："<設定名>"（HMI Settings r{列}{欄}，Technical Reference=<F 值>）／
PROXI：`<參數名>`（Format r{列}）；Procedure 用 UI、Pre-Condition 用 PROXI（R-P375(b)）`。

### 4. 段 2：Atlantis 欄之 `MESSAGE.Signal` 為主值

**CAN 形有段 2 主值者 = 21**（＝ E25 之命中數，兩者必然一致，互為交叉驗算）。

> **⚠ 本包撤除了 8 列誤指派之段 2 主值（R-VT12(a)）**：
> 初版實作把「LID 三欄之正規化命中」也拿來指派段 2 主值 ——
> 例如 `BRAKE1.VehicleSpeedVSOSig` 因 `Logical Identifier` = `VehicleSpeedVSOSig` 而命中 r1736，
> 於是被指派了**該列 Atlantis 欄所載之他名** `STATUS_CCAN3.VehicleSpeedVSOSig`。
> **這正是 R-VT12(a) 明文禁止的「以一方為他方旁證」**。
> 改為：段 2 主值**只能來自 Atlantis 欄 Signal Name 對該名之逐字命中**；
> 無命中者段 2 留空並註明「Atlantis 欄實測無本訊息名」。8 列受影響。

**架構差異**（Atlantis 與 Atlantis High 之值不同者）記於備註，**非 B-1、非 R-13**。

### 5. 段 3：一律待件

forms/ 之 `PDT27_E2A_R1_BHCAN2.dbc`／`R1_FDCAN8.dbc` 為 **Atlantis High** 之件。
本包對其實查之結果**只記旁證**（備註標「Atlantis High DBC 實查（旁證，非本線判準）」），
結果一律 `段3待ATL-Mi DBC`（**62 列**）。CAN 形逐列備註「段 1 不適用（規格原名已為 `MESSAGE.Signal` 形）」。

### 6. 結果值域（九值）與 R-13 之重判

原 28 列 R-13：**Atlantis 欄命中 7 列 → 改記 `段3待ATL-Mi DBC`**（其中 6 列為 E26 所指之
`SERVICE_SETUP.*` 四名 ＋ `TELEMATIC_SERVICE_SETUP.ClearPersonalDataReq`／`RestoreDefaultSettingReq`）；
**未命中之 21 列維持 `訊息名不符(R-13)`**，備註記「待 DR-VT5 重驗」。

### 7. `data/signal_chain_v43_v4.tsv`（v3 不覆寫）—— 同母體（230）分布差

| 結果 | v3 | **v4** | 差 |
|---|---|---|---|
| 解得 | 41 | **0** | **−41**（R-VT13(b)） |
| **段3待ATL-Mi DBC** | — | **62** | **+62** |
| 訊息名不符(R-13) | 28 | **21** | −7 |
| 未解得(止於段2) | 13 | **0** | −13 |
| 未解得(止於段1) | 108 | **108** | **0** |
| UI路徑(R-P375b) | 1 | **1** | 0 |
| PROXI路徑(R-P375b/c) | 39 | **34** | −5 |
| **UI+PROXI 雙路徑** | — | **4** | +4 |
| B-1 衝突 | 0 | **0** | 0 |
| 查無(R-G13) | 0 | **0** | 0 |
| 合計 | 230 | **230** | — |

**v3 → v4 之逐筆轉移**（合計 72 列變動）：

| 筆數 | 轉移 |
|---|---|
| 41 | `解得` → `段3待ATL-Mi DBC` |
| 13 | `未解得(止於段2)` → `段3待ATL-Mi DBC` |
| 7 | `訊息名不符(R-13)` → `段3待ATL-Mi DBC` |
| 4 | `PROXI路徑` → `未解得(止於段1)`（**A-VT23，判準收緊**） |
| 3 | `PROXI路徑` → `UI+PROXI 雙路徑` |
| 2 | `未解得(止於段1)` → `PROXI路徑`（重音二名） |
| 1 | `未解得(止於段1)` → `UI+PROXI 雙路徑`（重音一名） |
| 1 | `未解得(止於段1)` → `段3待ATL-Mi DBC` |

**`未解得(止於段1)` 之類別拆解**

| 類別 | v3 | **v4** | 差 |
|---|---|---|---|
| **內部** | 83 | **83** | **0** |
| CAN | 15 | **15** | 0 |
| PROXI | 10 | **10** | 0（−3 重音 ＋4 A-VT23 −1 其他） |

> **`未解得(止於段1)` 總數 108 → 108，差 0（E30）。看似原地踏步，其實是三股相消**：
> 重音三名解出（−3）、A-VT23 之四名落回（+4）、另一名解出（−1）。
> **若無 A-VT23 之判準收緊，本欄會是 104，而那個數字是假的。**

### 8. 兩弧（R-VT13(c)）

| 規格原名 | Atlantis 欄命中 | 備註 |
|---|---|---|
| `STATUS_CCAN3.VehicleSpeedVSOSig` | **2 處**（`CAN Mapping` r1736、r2329） | **LTM 觀察弧（R-VT13(c)）** |
| `BRAKE1.VehicleSpeedVSOSig` | **0 處** | **上游弧（R-VT13(c)）**；段 2 主值留空 |

`BRAKE_FD_2.VehicleSpeedVSOSig` 只見於 **`Atlantis High`** 欄（`CAN Mapping` r2321，`CAN` = `FD`）。
**R-VT13(c) 獲本包獨立複驗。**「旁證」字樣已自兩列刪除。

---

## 三、E 對照（相符者亦列，不符不調和）

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| E10‴ | R-VT1–R-VT12 `body_sha8` 與上繳 03 逐字相同 | 全同 | **12/12 相同**（R-VT1–10 自台帳、R-VT11–12 自樹外） | ✅ 相符 |
| E25 | 段 1 Atlantis 欄逐字命中（CAN 形） | ≥ 21 | **21**（欄內多值切分）／**20**（僅切換行） | ⚠ **依掃描條件而異，已定位；採 21** |
| E26 | 原 R-13 28 列中 Atlantis 欄命中 | ≥ 6 | **6** | ✅ 相符 |
| E27 | 結果 `解得` | **0** | **0** | ✅ 相符（未觸停） |
| E28 | B-1 衝突 | 0 | **0** | ✅ 相符 |
| E29 | `Technical Reference` 含 VF665 之候選集列數 | 觀測值 | **3**（字面）／**247**（含 `665`） | ⚠ 兩讀法並列 |
| E30 | 同母體（230）`未解得(止於段1)` 對 v3 | 觀測差值 | **108 → 108，差 0**（三股相消，見 §二-7） | — 觀測值 |

### E25 之掃描條件歸因（04 包明令「< 21 即回報掃描條件差異」）

| 掃描條件 | CAN 形 | R-13 |
|---|---|---|
| Atlantis，僅**換行**切分、逐字 | **20** | 6 |
| Atlantis，**子串包含** | **21** | 6 |
| Atlantis，**欄內多值切分**（換行 ＋ 格內 `MESSAGE.Signal` 詞元）、逐字 | **21** | 6 |
| Atlantis High，僅 `CAN Mapping` Z 欄、多值切分 | **10** | **0** |
| Atlantis High，全分頁（`Proxi & Configuration` P 欄兼用） | 10 | 2 |

**根因為單一儲存格**：`CAN Mapping` **r1736** 之 Atlantis Signal Name 為
`STATUS_CCAN3.VehicleSpeedVSOSig   'STATUS_CCAN3.VehicleSpeedVSOSigFailSts`
—— **一格兩名，以空白與一個單引號分隔，非換行**。

**本包採「欄內多值切分 ＋ 逐字」**，該條件下分析層之四個數字**全部重現**：
Atlantis **21**／Atlantis High **10**／R-13 Atlantis **6**／R-13 Atlantis High **0**／段 2 待解 **7**。
**不採「子串包含」**：子串會把 `X.Foo` 誤配到 `X.FooBar`（前綴假陽性），
而多值切分得到同樣的 21 且無此風險。
此一技術選擇**改變了 E25 之結論（20 → 21）**，依 FO 之第 0 節 Tier 0 末句即為 **Tier 2**，故三讀法全列交裁（A-VT24）。

### R-VT13／R-VT14 之 `body_sha8`

| 條號 | 一句話 | `body_sha8` | `sha8`（觀測） | 來源：列 | 本體列數 |
|---|---|---|---|---|---|
| R-VT13 | ATL-Mi 線之訊號解析綁定：段 1 取 `Atlantis` 欄組；段 3 待 ATL-Mi DBC | **`3e332b48`** | `4fd8102d` | `features/vsm_v43/RULINGS.md`:187 | 16 |
| R-VT14 | 值域增雙路徑；`Technical Reference` 先篩；台帳重生同 R-VL13 | **`8525adfa`** | `747675c1` | 同上:206 | 9 |

---

## 四、Atlantis vs Atlantis High 逐名對照

落於 `data/atlantis_vs_high_v43.tsv`，欄位
`規格原名 | 類別 | 欄組 | LID 分頁 | 列 | Signal Name | CAN 欄值`。

| 項 | 值 |
|---|---|
| 對照列數 | **56**（Atlantis **46**／Atlantis High **10**） |
| 涉及之相異規格原名 | **30** |
| Atlantis High ⊆ Atlantis（CAN 形） | **是**（10 ⊂ 21） |

**代表性列**（完整表見 TSV）：

| 規格原名 | 欄組 | 位置 | Signal Name | CAN |
|---|---|---|---|---|
| `STATUS_CCAN3.VehicleSpeedVSOSig` | Atlantis | `CAN Mapping` r1736 | `STATUS_CCAN3.VehicleSpeedVSOSig   'STATUS_CCAN3.…FailSts` | (空) |
| `STATUS_CCAN3.VehicleSpeedVSOSig` | Atlantis | `CAN Mapping` r2329 | `STATUS_CCAN3.VehicleSpeedVSOSig` | (空) |
| `STATUS_CCAN3.VehicleSpeedVSOSig` | Atlantis High | `CAN Mapping` r1736 | 同上 | `CAN-B` ／ `FD` |
| `SERVICE_SETUP.PrivacyMode` | Atlantis | `CAN Mapping` r1398 | `SERVICE_SETUP.PrivacyMode` | **`CAN-B`** |
| `Cluster_Display_Type` | Atlantis | `Proxi & Configuration` r39 | `Cluster_Display_Type` | `PROXI` |

> **`CAN` 欄大量為空**：Atlantis 欄組之 `CAN`（Q）在多數列未填 ——
> 這使 R-VT13(c) 所倚之「HU 匯流排依 LID Atlantis 欄之 `CAN` 值」在**逐訊號層級並不總是可用**。
> 已填者以 `CAN-B` 為主（如 `SERVICE_SETUP.PrivacyMode`）。列為 §八獨立判斷之一。

---

## 五、§K

**空。** E27／E28 皆 0，K-1 已由 R-VT13(c) 結案並經本包複驗。
本包唯一之升級條件相關項為 E25 之掃描條件差異，已依 04 包明令**回報**（§三、A-VT24），
**未觸「需第七規則」**（第六規則已足；本包未新增任何規則）。

---

## 六、anomaly／DR 清單

### 狀態變更

| id | 變更 | 依據 |
|---|---|---|
| A-VT16 | PENDING → **RESOLVED** | R-VT13(c)；本包複驗 Atlantis 欄 `STATUS_CCAN3.*` 2 處／`BRAKE1.*` 0 處 |
| A-VT19 | PENDING → **RESOLVED** | R-VT13(c)：K-1 結案，解在 LID 非 SYSAD；本包對 SYSAD 之結論不變（問錯文件為 A-VT22） |
| A-VT20 | PENDING → **RESOLVED** | R-VT13(e)：第六規則準；三名全解 |
| A-VT12 | 備註改指 **R-VT13(d)** | 28 → 21，餘待 DR-VT5 |
| A-VT21 | **維持**（六名標記不刪） | 04 包第 1 項 |

### 本包新登

| id | 一句話 | 狀態 | 配對 DR |
|---|---|---|---|
| **A-VT23** | **執行層之誤**：v2／v3 之 `PROXI路徑` 末支為 catch-all（任一入口檔逐字命中即算），四名（`LTM`／`TBM`／`Unit`／`Resolution`）為偽陽性；**v2／v3 所報之 39 實為 35** | RESOLVED（v4 判準收緊並逐列標記；排除旗標待裁） | — |
| **A-VT24** | E25 掃描條件差異已定位：LID r1736 一格兩名、非換行分隔；三讀法並列（20／21／21） | RESOLVED（採多值切分，理由與風險已列） | — |

### 未結 DR（本包未動 `DATA_REQUESTS.md`，未送）

| DR | 項目 | 阻塞 | 狀態 | 本包佐證 |
|---|---|---|---|---|
| DR-VT1 | V43 之 037 缺件 | **yes** | 建議送出 | — |
| DR-VT2 | SYSRA DocID／版次／Melco ID／拼法（＋重音三名） | no | 未送出 | 重音三名經第六規則解出，**證實為上游拼法不一而非本線誤讀** |
| DR-VT3 | （重寫）待 DR-VT5 重驗 | no | 暫持 | 28 → **21** 列（Atlantis 欄命中者已撤 7 列） |
| DR-VT4 | 內部訊號對照總表 83 名 | **yes** | 建議送出 | **第四輪擴充仍 83 → 83** |
| DR-VT5 | ATL-Mi DBC | **yes（P4）** | 先問 Pei 有無 | **62 列**現卡在 `段3待ATL-Mi DBC` |

---

## 七、`gate_all.py` 輸出與歸因

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
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 計數 **503**，與上繳 03 同。將本包全部產出移出（`ANOMALIES.md`／`RECON.md` 還原至 HEAD、`docs/upstream/04_signal_atlantis.md` 移出樹外）後重跑**仍為 503** |
| `rulings_hash` | **相關，且依 R-VL13／R-VT14(c) 為預期狀態** | 台帳含 R-VT1–R-VT10；**R-VT11–R-VT14 未入**，另缺 vsm_v42 之 R-VL 列。**依 R-VT14(c)「台帳重生由 Pei 提交前一次」，本包不重生** —— 此紅為**待 Pei 重生**，非缺陷 |
| `gates_tsv` | **無關** | 差異列全屬 `lint036`／`driver_distraction`／`ics_management`／`lint_docs036` |
| `lint_paths` | **無關** | 紅項全在 `driver_distraction/workbook/`、`ics_management/delivered/`、`sw_update/delivered/` |

---

## 八、獨立判斷（「本包是否仍有該驗而未驗者」）

1. **內部訊號 83 名，四輪擴充零變動 —— 這已不是「還沒解」，是「這條路上沒有答案」。**
   四輪分別擴了：正規化規則（02）、對象欄（03）、對象檔（03）、**欄組**（04）。
   83 → 83 → 83 → 83。forms/ 七檔沒有任何一本收 `X.Req` 形之內部訊號名。
   **DR-VT4 升級是對的，但升級不等於送出** —— 它已連續三包停在「建議送出」。

2. **`Atlantis` 欄之 `CAN` 值大量為空，R-VT13(c) 的推論鏈在逐訊號層級有缺口。**
   K-1 之結論（LTM 觀察面為 `STATUS_CCAN3.*`）成立於「Atlantis 欄有該名而 Atlantis High 無」，
   這一步很穩。但 R-VT13(c) 另說「HU 匯流排依 LID Atlantis 欄之 `CAN` 值」——
   實測該欄多數列為空（見 §四）。**若 P4 要逐訊號指定匯流排，此欄不足以支撐**，
   仍需 DR-VT5 之 DBC 或 SYS2 之 CAN Signal Mapping。建議下包明確此界線。

3. **A-VT23 這類錯誤的共同形狀：判準寫寬了，而數字往好的方向偏。**
   `PROXI路徑` 被高報 4 列，橫跨兩包無人察覺（含我自己兩次覆核）。
   與 A-VT15（抽取正則）同型 —— 兩者都不會讓任何 gate 變紅。
   **建議**：凡結果值域中之「已解」類，其判定式末支不得為 catch-all；
   每一「已解」都必須指得出**命中哪一個檔的哪一欄**。v4 已照此重寫。

4. **E30 差 0 是本包最容易被誤讀的數字。**
   108 → 108 看似停滯，實為 −3（重音解出）+4（A-VT23 落回）−1（其他）。
   **若不做 A-VT23 之收緊，這欄會顯示 104，而那是假的進展。**
   建議此類欄位往後一律附「轉移矩陣」，不只報淨值。

5. **本包未驗而下放包亦未要求者**：
   (a) `Proxi & Configuration` 之合併欄組（`Atlantis & Atlantis High`）在欄組分立之判準下
       應歸何方，本包依分析層數字反推為「Atlantis High 僅取 `CAN Mapping` Z 欄」，**此界線未經明裁**；
   (b) `Brand-Specific Names` 分頁（1001 列）仍未用（R-VT14(b) 明令 P3 不動）；
   (c) `未解得(止於段2)` 於 v4 歸零，是因全數併入 `段3待ATL-Mi DBC`；
       DR-VT5 到件後須能區分「段 2 已解待段 3」與「段 2 未解」，**v4 未保留該區分**，建議下包加欄；
   (d) `forms/LOOKUP_MISSES.md` 仍未寫（三要件未滿足，本應不寫）。

---

## 九、禁區遵守聲明（00 包 §零）

| 禁區 | 遵守 |
|---|---|
| 1. git 一律不動 | 本包未跑任何 `git` 寫入指令 |
| 2. 不寫 `features/vehicle_setting/`、`features/vsm_v42/` | 未寫、未讀 |
| 3. 不寫 `docs/runtime/profiles/` | 未寫 |
| 4. 不改寫 `sources/raw/` 原檔 | 全程唯讀 |
| 5. 不以 SYSRA 或規格代 037 建母體或生成 TC | 未建、未生成；`generated/`／`batches/` 仍空 |
| 6. 不自行送 DR | 未送、未改 `DATA_REQUESTS.md` |

本包寫入之檔（全在 `features/vsm_v43/` 之下）：
`ANOMALIES.md`（改）、`RECON.md`（改 §7）、`data/signal_chain_v43_v4.tsv`（新）、
`data/atlantis_vs_high_v43.tsv`（新）、`docs/upstream/04_signal_atlantis.md`（新）。
v1／v2／v3 TSV、`feature.yaml`、`sources/`、`forms/`、`docs/fw036/`、`scripts/` **未寫入**。

---

## 十、下一步

1. **Pei：DR-VT5（ATL-Mi DBC）先答有無** —— **62 列**卡在此，阻塞兩線 P4
2. **Pei：DR-VT1／VT2／VT4 三項併送**（VT3 暫持）
3. **Pei（累計五包）**：commit；台帳重生（R-VT14(c)）；`_intake/` 空目錄刪；共用腳本一裁（六項）
4. 分析層：E25 掃描條件（A-VT24）、E29 之 `VF230/665` 讀法、A-VT23 四名是否併入排除清單、
   `Proxi & Configuration` 合併欄組之歸屬（§八-5(a)）
5. 下包：v4 加欄以區分「段 2 已解待段 3」與「段 2 未解」（§八-5(c)）
6. P3：framework Layer 1 鎖定、profile、`spec_reference_template` 定案
7. DR-VT5 到件 → 段 3 重驗 62 列 ＋ R-13 餘 21 列 → 037 到齊 → Layer 2 → P4
