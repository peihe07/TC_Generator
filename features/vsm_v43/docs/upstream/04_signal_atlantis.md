# 上繳包 04 — vsm_v43：W-5‴ 以 Atlantis 欄組重跑、段 3 綁 ATL-Mi DBC

日期：2026-09-02　執行層　對應下放包：`docs/handoff/04_signal_atlantis.md`（**含 2026-09-02 補遺，補遺優先**）
sha8 報 **`body_sha8`**。R-VT1–R-VT10 取自台帳；R-VT11–R-VT15 台帳尚無，取樹外 `--out`（R-VT10(a)）。
台帳**不重生**（R-VT14(c)）。**DR 一律不送**（Pei 裁）。本線因 DR-VT1 不送**續止於 P0–P3**。

> **本檔取代同名之前一版**（該版寫於 DBC 到件前，段 3 一律 `段3待ATL-Mi DBC`、E27 判 `解得 = 0`）。
> 補遺作廢 E27 與「E27 ≥ 1 即停」，「解得」自此合法（R-VT15(d)），故 W-5‴ 第 5／6 項與 v4 全部重跑。
> 前一版之 §二-1～4、§四（Atlantis vs High 對照）不受 DBC 影響，結論不變，本版沿用並標明。

---

## 〇、一句話結論

**ATL-Mi DBC 到件後，CAN 側幾乎全解：`解得` 0 → 86，R-13 28 → 4（其中 2 為架構性），E31 = 2 ≤ 2 相符。
內部訊號 83 名第五輪擴充仍是零變動 —— DBC 解不了它，因為缺的是對照表不是 DBC。**

| 項 | 結果 |
|---|---|
| E10‴ | ✅ **14/14 相同**（R-VT1–R-VT14） |
| E25／E26／E28／E29／E30 | 21（掃描條件已定位）／6／**0**／3 或 247／−15 |
| **E31（原 R-13 28 列重判後仍未解 ≤ 2）** | ✅ **2** —— 且與 R-VT15(b) 之預測**逐名相同** |
| E27 | **作廢**（補遺）；`解得` 為觀測值 = **86**，全數有 `VAL_` |
| §K | **空** |

## 一、結果三分法（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | 段 3 改綁 P363 ATL-Mi DBC，86 列判「解得」並逐列記 BO_／SG_ 實名與 VAL_ 有無；原 R-13 28 → 2；段 1 綁 Atlantis 欄組；第六規則；值域二增；`RECON.md` §7 全面更新 |
| 核實無誤 | E10‴ 14/14；**26/28 與 R-VT15(b) 逐名相同**；BO_ 99／VAL_ 503 與驗收數字一致；Atlantis High ⊆ Atlantis（10 ⊂ 21）；86 列**全部有 VAL_**（0 列缺） |
| 正確地不動 | 台帳不重生；**DR 一律不送**（含 DR-VT3 之 2 名、DR-VT4 之 83 名）；`LOOKUP_MISSES.md` 未寫；不重抽名；A-VT23 四名不擅自設排除旗標；E25／E29 兩讀法並列；R1 DBC 之實查**只記旁證** |

---

## 二、W-5‴ 逐項（八項）

### 1. 抽名（不重抽）

母體 **230**；`排除(A-VT21)` 標記六名，**不刪**。另四名（`LTM`／`TBM`／`Unit`／`Resolution`，A-VT23）
逐列標記但**未設排除旗標**（擴充排除清單非執行層可為）。併計偽陽性 **10**，PROXI 母體實為 **39**。

### 2. 段 1：LID `Atlantis` 欄組為主

掃描條件：`CAN Mapping` 之 `Atlantis` = P（Signal Name）／Q（CAN）、`Atlantis High` = Z／AA；
`Proxi & Configuration` 只有合併欄組（P／Q）；`* Specific Signals` 單一 `Signal Name`／`CAN`。
三欄（`Logical Identifier`／`Function`／`Object Text`）逐字 ＋ 規則 1–6，**儲存格內多值切分**（見 §三 E25）。

**CAN 形之 Atlantis 欄逐字命中 = 21**（＝ 有段 2 主值者，互為交叉驗算）。
**第六規則命中 3 名**（`DRL_Menù_Enable`／`Horn_Chirp_Menù` → PROXI路徑；
`Greeting_Lights_Menù` → UI+PROXI 雙路徑），逐列備註「重音正規化」。

> **`Atlantis` 欄之 `CAN` 值僅 10 列有值**（230 名中）。R-VT13(c) 所倚之
> 「HU 匯流排依 LID Atlantis 欄之 `CAN` 值」在逐訊號層級**仍不足以支撐**；
> 所幸 DBC 到件後此路已非必要（見 §五-2）。

### 3. HMI Settings List：`Technical Reference` 先篩（R-VT14(b)）

F 欄非空 **384** 列、相異值 **38**。

| 讀法 | 列數 |
|---|---|
| 含 `VF665` **字面**（判準原文） | **3**（`VF665` ×1、`VF230/VF665, CFTS022` ×2） |
| 含 `665` | **247**（`VF230/665` ×**235** 為主，另 5 種寫法） |

**兩讀法並列，不調和。** 依判準原文以 3 列候選集先比、未命中再對全表；
命中集合不因讀法而異（R-VT14(b) 定「未命中再對全表」），差別只在錨點取哪一列。
**HMI 命中 4 名**，其中 3 名同時命中 PROXI → 記 `UI+PROXI 雙路徑`（另 `Greeting_Lights_Menù` 亦是，共 4 列）。

### 4. 段 2：Atlantis 欄之 `MESSAGE.Signal` 為主值

CAN 形有段 2 主值者 **21**。
**段 2 主值只能來自 Atlantis 欄對該名之逐字命中** —— 不得以 LID 三欄之正規化命中去取
「該列 Atlantis 欄所載之他名」，那正是 R-VT12(a) 禁止之弧線合併（前一版曾誤指派 8 列，已撤）。

### 5. 段 3：綁 `P363_BH-CAN [07338]_3A_R2.dbc`（R-VT15）

**讀法**：`latin-1`、CRLF（實測 6363 個 CRLF、非 ASCII byte 18）。
索引以**行首錨定**建立：`BO_` 定義訊息，其後之 `SG_` 行歸屬該訊息。

**驗收數字對照（A-VT28）**

| 項 | R-VT15(a) | 本包實測 | 判 |
|---|---|---|---|
| `BO_` | 99 | **99** | ✅ 相同 |
| `SG_` | 4576 | **688**（訊號定義，行首錨定）／相異名 **655** | ⚠ **計數條件不同** |
| `VAL_` | 503 | **503**（行首錨定）／有 VAL_ 之相異訊號 **496** | ✅ 相同 |

**`SG_` 差異之歸因**：DBC 之 `BA_ "GenSigStartValue" SG_ <id> <sig> 0;` 等**屬性指派行**內含 `SG_`。

| 計數條件 | 值 |
|---|---|
| 行首錨定（訊號定義） | **688** |
| 全文 `\bSG_\s+識別字` | 4570 |
| 含字串 `SG_` 之行數 | 4578 |

4576 落在 4570–4578 之區間 —— 即**含屬性行之計數**。
**影響為零**：索引一律行首錨定，屬性行不入索引；`BO_ 99` 與 `VAL_ 503` 兩數完全一致。

**每列備註記 BO_／SG_ 實名與 VAL_ 有無**（補遺明令）。
**86 個「解得」之 `VAL_` 有無：有 86、無 0** —— `<label>` 可逐字取，無待補者。

**R1 DBC（Atlantis High）降旁證**：其實查結果只寫入備註，標「R1 DBC（Atlantis High）旁證」，不作判準。

**CAN-C 未到件（R-VT15(c)）**：`SG_` 於 P363 BH-CAN 查無者 **8 列**，記
`未解得（CAN-C DBC 未到件）` ——
`IPC_VEHICLE_SETUP.BSDEnable`／`.CorneringLightsEnable`／`.RainSensorLevel`、
`TELEMATIC_VEHICLE_SETUP.BSDEnable_Req`／`.RainSensorLevel_Req`、
`SERVICE_SETUP.RestoreDefaulSetting`（規格拼字漏 `t`）、
`TELEMATIC_SERVICE_SETUP.RestoreDefaultSettimgReq`（規格拼字 `m`）、`PROXI.First`。

> 其中**兩列為規格側拼字錯誤**（`RestoreDefaulSetting`／`RestoreDefaultSettimgReq`），
> 正確拼法之同名訊號在 DBC 內存在且已解。**不擅自更正規格原名**（R-13／R-6），
> 列為 **DR-VT2 之新增佐證**。

### 6. 原 R-13 28 列之重判（E31）

| 新結果 | 列數 |
|---|---|
| **解得** | **26** |
| 訊息名不符(R-13) | **2** |

**仍未解之 2 名**：`SERVICE_SETUP.TelematicSetupACK`、`TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock`
—— 二者之 `SG_` 於 P363 **皆落於 `BO_ IPC_VEHICLE_SETUP`**。
**與 R-VT15(b) 之預測逐名相同。E31 = 2 ≤ 2 ✅。**

**全表 R-13 為 4 列，但入 DR-VT3 者只有 2 列**：

| 規格原名 | 判 |
|---|---|
| `SERVICE_SETUP.TelematicSetupACK` | 入 DR-VT3（暫持不送） |
| `TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock` | 入 DR-VT3（暫持不送） |
| `BRAKE1.VehicleSpeedVSOSig` | **架構性，不入 DR-VT3**（A-VT27） |
| `BRAKE1.VehicleSpeedVSOSigFailSts` | **架構性，不入 DR-VT3**（A-VT27） |

### 7. `data/signal_chain_v43_v4.tsv`（v3 不覆寫）—— 同母體（230）對 v3 分布差

| 結果 | v3 | **v4** | 差 |
|---|---|---|---|
| **解得** | 41（以 R1 DBC 判，已作廢） | **86** | **+45** |
| 訊息名不符(R-13) | 28 | **4** | **−24** |
| **未解得（CAN-C DBC 未到件）** | — | **8** | +8 |
| 未解得(止於段2) | 13 | **0** | −13 |
| 未解得(止於段1) | 108 | **93** | **−15** |
| UI路徑(R-P375b) | 1 | **1** | 0 |
| PROXI路徑(R-P375b/c) | 39 | **34** | −5 |
| **UI+PROXI 雙路徑** | — | **4** | +4 |
| B-1 衝突 | 0 | **0** | 0 |
| 查無(R-G13) | 0 | **0** | 0 |
| 合計 | 230 | **230** | — |

**v3 → v4 之逐筆轉移（70 列變動）**

| 筆數 | 轉移 |
|---|---|
| 26 | `訊息名不符(R-13)` → `解得` |
| 13 | `未解得(止於段2)` → `解得` |
| 11 | `未解得(止於段1)` → `解得` |
| 4 | `解得` → `未解得（CAN-C DBC 未到件）` |
| 4 | `未解得(止於段1)` → `未解得（CAN-C DBC 未到件）` |
| 4 | `PROXI路徑` → `未解得(止於段1)`（**A-VT23，判準收緊**） |
| 3 | `PROXI路徑` → `UI+PROXI 雙路徑` |
| 2 | `未解得(止於段1)` → `PROXI路徑`（重音二名） |
| 1 | `未解得(止於段1)` → `UI+PROXI 雙路徑`（重音一名） |
| 1 | `解得` → `訊息名不符(R-13)`（`BRAKE1.*`，架構性） |
| 1 | `未解得(止於段1)` → `訊息名不符(R-13)`（`BRAKE1.*FailSts`，架構性） |

**`解得 86` 之類別**：CAN **81**／內部 **5**。

**`未解得(止於段1)` 93 之類別拆解**

| 類別 | v3 | **v4** |
|---|---|---|
| **內部** | 83 | **83** |
| CAN | 15 | **0** |
| PROXI | 10 | **10** |

### 8. 兩弧（R-VT13(c)）

| 規格原名 | Atlantis 欄 | P363 DBC | v4 結果 |
|---|---|---|---|
| `STATUS_CCAN3.VehicleSpeedVSOSig` | 命中 2 處（r1736、r2329） | `BO_ STATUS_CCAN3` ✅ | **解得**（LTM 觀察弧） |
| `BRAKE1.VehicleSpeedVSOSig` | 命中 **0** 處 | `SG_` 落於 `STATUS_CCAN3`，**無 `BRAKE1` 訊息** | 訊息名不符(R-13)，**架構性**（上游弧） |

**DBC 對 R-VT13(c) 構成第二個獨立印證**：P363 BH-CAN 內根本沒有 `BRAKE1` 這個訊息。

---

## 三、E 對照（相符者亦列，不符不調和）

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| E10‴ | R-VT1–R-VT12 `body_sha8` 與上繳 03 逐字相同 | 全同 | **14/14 相同**（另含 R-VT13／R-VT14 與前一版同） | ✅ 相符 |
| E25 | 段 1 Atlantis 欄逐字命中（CAN 形） | ≥ 21 | **21**（欄內多值切分）／20（僅切換行） | ⚠ 掃描條件已定位，採 21 |
| E26 | 原 R-13 28 列中 Atlantis 欄命中 | ≥ 6 | **6** | ✅ 相符 |
| E27 | 結果 `解得` = 0 | **補遺作廢** | `解得` = **86**（觀測值） | — 已作廢 |
| E28 | B-1 衝突 | 0 | **0** | ✅ 相符 |
| E29 | `Technical Reference` 含 VF665 之候選集列數 | 觀測值 | **3**（字面）／**247**（含 `665`） | ⚠ 兩讀法並列 |
| E30 | 同母體（230）`未解得(止於段1)` 對 v3 | 觀測差值 | **108 → 93，差 −15** | — 觀測值 |
| **E31** | 原 R-13 28 列重判後仍未解者 | **≤ 2** | **2**（且與 R-VT15(b) 逐名相同） | ✅ **相符** |

### E25 之掃描條件（04 包原文明令「< 21 即回報」）

| 掃描條件 | CAN 形 | R-13 |
|---|---|---|
| Atlantis，僅**換行**切分、逐字 | **20** | 6 |
| Atlantis，**子串包含** | **21** | 6 |
| Atlantis，**欄內多值切分**（換行 ＋ 格內 `MESSAGE.Signal` 詞元）、逐字 | **21** | 6 |
| Atlantis High，僅 `CAN Mapping` Z 欄、多值切分 | **10** | **0** |

**根因為單一儲存格**：`CAN Mapping` **r1736** 之 Atlantis Signal Name 為
`STATUS_CCAN3.VehicleSpeedVSOSig   'STATUS_CCAN3.VehicleSpeedVSOSigFailSts`
—— **一格兩名，以空白與一個單引號分隔，非換行**。

本包採**欄內多值切分 ＋ 逐字**，該條件下分析層四個數字**全部重現**（21／10／6／0，段 2 待解 7）。
**不採子串**（會把 `X.Foo` 誤配到 `X.FooBar`）。此技術選擇改變了 E25 之結論（20 → 21），
依 FO 之第 0 節 Tier 0 末句即為 **Tier 2**，三讀法全列交裁（A-VT24）。

### R-VT13／R-VT14／R-VT15 之 `body_sha8`

| 條號 | 一句話 | `body_sha8` | `sha8`（觀測） | 來源：列 | 本體列數 |
|---|---|---|---|---|---|
| R-VT13 | ATL-Mi 線之訊號解析綁定：段 1 取 `Atlantis` 欄組 | **`3e332b48`** | `4fd8102d` | `RULINGS.md`:187 | 16 |
| R-VT14 | 值域增雙路徑；`Technical Reference` 先篩；台帳重生同 R-VL13 | **`8525adfa`** | `747675c1` | 同上:206 | 9 |
| R-VT15 | 段 3 DBC 綁定 `P363_BH-CAN [07338]_3A_R2.dbc`；DR-VT5 結案 | **`9ace16a9`** | `608e336b` | 同上:218 | 11 |

---

## 四、Atlantis vs Atlantis High 逐名對照

`data/atlantis_vs_high_v43.tsv`（**本輪未變更** —— 該表只依 LID，與 DBC 到件無關）。

| 項 | 值 |
|---|---|
| 對照列數 | **56**（Atlantis **46**／Atlantis High **10**） |
| 涉及之相異規格原名 | **30** |
| Atlantis High ⊆ Atlantis（CAN 形） | **是**（10 ⊂ 21） |

代表列：`STATUS_CCAN3.VehicleSpeedVSOSig` 於 Atlantis 命中 `CAN Mapping` r1736／r2329；
`BRAKE_FD_2.VehicleSpeedVSOSig` 僅見於 Atlantis High（r2321，`CAN` = `FD`）。

---

## 五、§K

**空。** E28 = 0；E31 = 2 符判準；E27 已作廢；本包**未新增任何規則**（未觸「需第七規則」）。

---

## 六、anomaly／DR 狀態

### 本包新登

| id | 一句話 | 狀態 |
|---|---|---|
| **A-VT25** | DBC 到件後解析躍升（解得 86、R-13 4）；**內部訊號 83 名第五輪擴充仍零變動** | PENDING（唯一結構缺口） |
| **A-VT26** | 五名內部訊號之「解得」係跳過段 1／2 之 DBC 直查，R-P368(a) 三段鏈僅段 3 過 | PENDING（判準待裁） |
| **A-VT27** | `BRAKE1.*` 之 R-13 為**架構性**（該弧不在 BH-CAN），非上游錯誤，不入 DR-VT3 | RESOLVED |
| **A-VT28** | R-VT15(a) 之 `SG_ 4576` 係含 `BA_` 屬性行之計數；訊號定義實為 **688**／相異 **655** | RESOLVED（影響為零） |

### 承前（本包無變更者不列）

A-VT16／A-VT19／A-VT20 已於前一版 RESOLVED；A-VT12 指向 R-VT13(d)；A-VT21 六名維持標記；
A-VT23 四名標記、排除旗標待裁；A-VT24（E25 掃描條件）RESOLVED。

### DR —— **一律不送**（Pei 裁）

| DR | 項目 | 阻塞 | 狀態 | 本包實測 |
|---|---|---|---|---|
| DR-VT1 | V43 之 037 缺件 | **yes** | **Pei 裁先不送** | 本線續止於 P0–P3 |
| DR-VT2 | SYSRA DocID／版次／Melco ID／拼法 | no | 先不送 | **新增佐證**：規格側兩處拼字錯（`RestoreDefaulSetting`／`RestoreDefaultSettimgReq`），正確拼法之訊號在 DBC 內存在 |
| DR-VT3 | （重寫）訊息名不符 | no | 暫持不送 | **名單由 28 收斂為 2**（另 2 列為架構性，剔除） |
| DR-VT4 | 內部訊號對照總表 83 名 | **yes** | 先不送 | **第五輪擴充仍 83 → 83**；代價：P4 起 83 名只能寫 `PENDING: DR-VT4 <名>` |
| DR-VT5 | ATL-Mi DBC | — | **結案（到件）** | R-VT15(d) |

---

## 七、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 505
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符 —— 重跑本工具並覆核 diff
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）

總判：**FAIL** —— 4 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths
依 FO §8.2／26 包 §C 裁定 2，該包不得上繳，除非附升級說明。
```

| 閘 | 與本包之關係 | 歸因 |
|---|---|---|
| `canon_refs` | **本包貢獻 0（移除歸因法實測）** | 計數 **505**（上繳 03 時 503）。將本包三份產出（`ANOMALIES.md`／`RECON.md`／本檔）全數還原至 `HEAD` 後重跑**仍為 505** → 本包貢獻 **0**。503 → 505 之 +2 來自他線（`git status` 顯示 `features/vsm_v42/` 與 `docs/` 多處同時處於未提交狀態） |
| `rulings_hash` | **相關，且為預期狀態** | 台帳含 R-VT1–R-VT10；R-VT11–R-VT15 未入。**依 R-VT14(c) 台帳重生歸 Pei 提交前一次，本線不重生** —— 此紅為待重生，非缺陷 |
| `gates_tsv` | **無關** | 差異列全屬 `lint036`／`driver_distraction`／`ics_management`／`lint_docs036` |
| `lint_paths` | **無關** | 紅項全在 `driver_distraction/workbook/`、`ics_management/delivered/`、`sw_update/delivered/`。**新入之 `forms/P363_BH-CAN [07338]_3A_R2.dbc` 未判紅**（`forms/` 為共用件落點） |

---

## 八、獨立判斷

1. **DBC 到件解了 CAN 側，對內部訊號一點作用都沒有 —— 這正是 DR-VT4 的證明。**
   五輪擴充：規則（02）→ 欄（03）→ 檔（03）→ 欄組（04）→ **DBC（04 補遺）**。
   內部訊號 **83 → 83 → 83 → 83 → 83**。
   88 名中只有 5 名之基名恰好與 DBC 之 `SG_` 同名（且那 5 名還走的是繞過段 1／2 的路，A-VT26）。
   DBC 是「訊號在哪條匯流排、什麼編碼」的表，**不是「內部變數怎麼驅動、怎麼觀察」的表**。
   Pei 裁先不送 DR-VT4，其代價已明確：**P4 起 83 名只能是 `PENDING: DR-VT4 <名>`**，
   即該批 TC 無法宣稱驗證了那些內部行為。本包不再重複建議，只把代價寫清楚。

2. **A-VT26 是本包唯一可能高報的地方，我把它標出來而不是藏著。**
   五名內部訊號記「解得」，但三段鏈只過了段 3。承 v2／v3 之既有判定不動，
   是為了避免「無裁決之結果跳動」；但若判準從嚴，這五列該退回 `未解得(止於段2)`。
   **86 這個數字裡有 5 是可爭議的，81 是穩的。**

3. **兩處規格拼字錯（`RestoreDefaulSetting`／`RestoreDefaultSettimgReq`）不該由我改。**
   正確拼法之訊號在 DBC 內存在且已解，改一個字母就能讓兩列從「待 CAN-C DBC」變「解得」——
   但那是改規格原文（R-13／R-6 明禁）。列 DR-VT2 佐證，等上游。
   **順帶一提**：這兩列被歸到「CAN-C 未到件」是**誤導性的**——
   它們不是 CAN-C 的問題，是拼字。已於備註逐列標明；建議下包為此另立一值
   （如 `未解得（規格拼字疑誤）`），現行值域無處可放。

4. **`Atlantis` 欄之 `CAN` 值只有 10 列有值。**
   R-VT13(c) 說「HU 匯流排依 LID Atlantis 欄之 `CAN` 值」—— 該欄在 230 名中僅 10 列非空。
   DBC 到件後這條路已非必要（訊息歸屬直接由 `BO_` 決定），但若日後要逐訊號指定匯流排
   （例如 CAN-C DBC 到件後要判某訊號屬 B 或 C），**LID 這一欄撐不住**。

5. **本包未驗而下放包亦未要求者**：
   (a) DBC 之 `VAL_` 逐值內容未取（只查有無）—— P4 寫 `<label>` 時須逐訊號取列舉，本包未建該表；
   (b) `BA_` 屬性（`GenSigSendType`／`GenSigStartValue`）未讀，其中含送出型態，
       對 Procedure 之「Send／Hold」寫法可能有用；
   (c) CAN-C DBC 未到件之 8 列中，有 2 列實為拼字問題（見 §八-3）；
   (d) `Brand-Specific Names` 分頁仍未用（R-VT14(b) 明令 P3 不動）；
   (e) `forms/FORMS.md` **未登錄本 DBC**（R-P368(e)／R-P365(b) 之台帳要求 SHA 取自 FORMS.md）——
       本包實測其 sha256 為 `a51079be6e98e6e5d907b7c44bc77663daadbed60e63418dd9dd9f2b07188abd`，
       **未寫入 FORMS.md**（共用件，非本線可為）。建議下包或 Pei 補登。

---

## 九、禁區遵守聲明（00 包 §零）

| 禁區 | 遵守 |
|---|---|
| 1. git 一律不動 | 未跑任何 `git` 寫入指令 |
| 2. 不寫 `features/vehicle_setting/`、`features/vsm_v42/` | 未寫、未讀 |
| 3. 不寫 `docs/runtime/profiles/` | 未寫 |
| 4. 不改寫 `sources/raw/` 原檔 | 全程唯讀 |
| 5. 不以 SYSRA 或規格代 037 建母體或生成 TC | 未建、未生成；`generated/`／`batches/` 仍空 |
| 6. 不自行送 DR | **未送任何 DR**；`DATA_REQUESTS.md` 未動 |

`forms/` **未寫入**（P363 DBC 為 Pei 放件；本包只讀，未登 FORMS.md，見 §八-5(e)）。
本包寫入之檔（全在 `features/vsm_v43/` 之下）：
`ANOMALIES.md`（改）、`RECON.md`（改 §7）、`data/signal_chain_v43_v4.tsv`（**重寫**）、
`docs/upstream/04_signal_atlantis.md`（**重寫**）。
`data/atlantis_vs_high_v43.tsv`、v1／v2／v3 TSV、`feature.yaml` **未動**。

---

## 十、下一步

1. **分析層**：A-VT26（五名內部訊號之判準）；A-VT28（`SG_` 計數口徑）；
   E25 掃描條件（A-VT24）；E29 之 `VF230/665` 讀法；A-VT23 四名是否併入排除清單
2. **Pei**：commit；台帳重生（R-VT14(c)）；`forms/FORMS.md` 補登 P363 DBC 之 SHA（§八-5(e)）；
   `_intake/` 空目錄刪；共用腳本一裁（六項）
3. 下包：CAN-C 未到件 8 列中之 2 列拼字問題另立值域（§八-3）；`VAL_` 逐值表（§八-5(a)）
4. **P3**：framework Layer 1 鎖定、profile `FW036_R1L_VSM_V43_Profile.md`、`spec_reference_template` 定案
   —— **CAN 側已具備（81 列穩解、全部有 VAL_）**，P3 可動
5. P4 待 DR-VT1（037）；屆時 83 名內部訊號依 DR-VT4 之未送而寫 `PENDING`
