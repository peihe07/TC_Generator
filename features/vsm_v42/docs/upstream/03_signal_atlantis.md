# 上繳包 03 — vsm_v42：W-5′（Atlantis 欄組 ＋ ATL-Mi DBC）、W-7、P3 前置

日期：2026-09-02　執行層：Claude Code　對應下放包：`docs/handoff/03_signal_atlantis.md`
**（含 2026-09-02 補遺，補遺優先）**

> **本上繳取代 2026-09-01 之同名前版。** 前版係於 ATL-Mi DBC **未到件**時所跑（v2，
> 結果欄一律「段3待ATL-Mi DBC」、`解得` 0）。補遺落 R-VL14 後段 3 有正件，
> 本包重跑為 **v3**。前版之產物 `data/signal_chain_v42_v2.tsv` **保留不刪**，
> 供對照；v1（`signal_chain_v42.tsv`）亦保留。三版並存。

## 結果分類（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | W-5′ 七項以 v3 重跑；段 3 綁定 ATL-Mi DBC；**解得 98**；DR-VL3 執行層結案紀錄；A-VL8 阻塞面解除；新開 A-VL11／A-VL12 |
| 核實無誤 | E18″ 11／11；E26 過（30 ≥ 26）；E29 0／20；DBC 之 `BO_`／`VAL_` 與 R-VL14(b) 六個爭議訊息逐一複驗 |
| 正確地不動 | 台帳不重生（R-VL13）；`scripts/` 未改；v1／v2 之 tsv 不覆寫；**DR 一律不送**；B-1 之標的不自選；W-7／P3 前置沿用上輪成果（實測未變，未重做） |

**總判：W-5′／W-7／P3 前置完成。E28 = 1（K-1），該名停下列 §K，其餘 250 名續行。**

---

## 0. 段 3 之件：驗收與一項不符

`forms/Project__637MCA_BH-CAN_R1_(29_01_2025)_plusCR19670.dbc`
sha256 **`5cac2abcecdf37e2f07991e26dc4cf748fe24874fde93af77a85ea8936d3ed16`**
（425,072 bytes；`file` 判 `ISO-8859 text, with CRLF line terminators`；解析以 **latin-1** 讀）。

| 項 | R-VL14(a) 所載 | 執行層實測 | 判 | 掃描條件 |
|---|---|---|---|---|
| `BO_` | 139 | **139** | **相符** | `^BO_ ` |
| `VAL_` | 619 | **619** | **相符** | `^VAL_ ` |
| **`SG_`** | **5568** | **844** | **不符** | `^\s*SG_ `（訊號定義行）；去重 **794** 名 |

**不調和，逐項歸因**（→ **A-VL11**）：其他計法之量測 ——
「全檔出現 `SG_` 字串」**5572**、「含 `SG_` 之行數」**5571**；
而 `^BA_ ` 屬性行 **5349** 行，多數形如 `BA_ "…" SG_ <msgid> <signal> …`。
即 **5568 應為「`SG_` 字串出現數」而非訊號定義數**。
**檔案本身確為正件**：`BO_`／`VAL_` 兩數逐字相符，且 R-VL14(b) 之六個爭議訊息
（`TELEMATIC_VEHICLE_SETUP2`／`IPC_VEHICLE_SETUP2`／`IPC_VEHICLE_SETUP3`／
`SERVICE_SETUP`／`TELEMATIC_SERVICE_SETUP`／`STATUS_CCAN3` 含 `VehicleSpeedVSOSig`）
**逐一複驗全數在內**。段 3 之索引以 844 行為準，解析不受影響。

---

## 1. E18″ 與條文 sha

| 條號 | 上繳 02 所報 `body_sha8` | 本包 | 判 |
|---|---|---|---|
| R-VL1 | `5897969a` | `5897969a` | **同** |
| R-VL2 | `01c67a04` | `01c67a04` | **同** |
| R-VL3 | `e306aa75` | `e306aa75` | **同** |
| R-VL4 | `08cea35e` | `08cea35e` | **同** |
| R-VL5 | `1de01344` | `1de01344` | **同** |
| R-VL6 | `7321474a` | `7321474a` | **同** |
| R-VL7 | `afb452ed` | `afb452ed` | **同** |
| R-VL8 | `3c02775c` | `3c02775c` | **同** |
| R-VL9 | `5a0230ee` | `5a0230ee` | **同** |
| R-VL10 | `6ced1b1f` | `6ced1b1f` | **同** |
| R-VL11 | `13a4dfcd` | `13a4dfcd` | **同** |

**11／11，E18″ 過。**

| 條號 | **`body_sha8`** | `sha8`（觀測值） | body_lines |
|---|---|---|---|
| R-VL12 | `34577e46` | `2d62ac95` | 20 |
| R-VL13 | **`782082cf`** | `c0264dff` | 9 |
| R-VL14 | **`3cc6e581`** | `6f362276` | 12 |

> **一項須指出**：R-VL13 之 `body_sha8` 為 `782082cf`，而本執行層於
> **2026-09-01 之前版上繳所報為 `6d382ff3`** —— 即 **R-VL13 之條文本體在兩次執行之間
> 被改寫**（非加註，`body_sha8` 動了）。R-VL13 不在 E18″ 之範圍（E18″ 只涵蓋 R-VL1–R-VL11），
> 故未觸發停下條件；**據實記明，不追問、不調和**。

R-VL2／R-VL5／R-VL9 之 `sha8` 相對上繳 02 位移（`d88dae19`／`0b1174ab`／`56fc8e0f`），
成因為 R-VL12／R-VL13 之 R-TM13 加註，**三者 `body_sha8` 皆未動** —— R-VL10(a) 之判準
第三次驗證正確。十四條 R-VL 皆為 `fenced` 本體。

---

## 2. W-5′-1 抽名

母體 **251 名**（CAN 112／`.Req` 69／`.Info` 32／`.GUI` 2／PROXI 36），
與前版（v2）之抽名**逐名相同**（同一通式 R-VL12(d)、同四來源），故未重列。
通式相對 v1 窄式新增之 18 個非 `_VEHICLE_SETUP` 家族 CAN 名亦不變
（`SERVICE_SETUP.*`／`TELEMATIC_SERVICE_SETUP.*` 13 名為其主體）。

**E29 偽陽性率：0／20**（seed 42，人工判讀；母體與前版相同，未重抽）。

---

## 3. W-5′-2／3 段 1 與段 2

段 1 五規則（R1 逐字／R2 去 `MESSAGE.` 前綴／**R2′ 去 `.Req`_`.Info`_`.GUI` 後綴**／
R3 去 `_Req`_`_Sts`_`_Info` 後綴／R4 底線↔空白大小寫／R5 去 `_Menu`_`_Setting`，
R5 僅 HMI Settings／PROXI／SR26／SR24）。命中證據格式
`檔/分頁/r{列}c{欄}/欄名/規則`，逐列存於 tsv。

### 段 1 七檔命中（涉及訊號名數）

| 檔／分頁 | 名數 |
|---|---|
| `PROXI_HDCC27_R3` `Format`（F 欄） | **57** |
| LID `CAN Mapping`（A/B/C ＋ P ＋ Z） | **33** |
| LID `Proxi & Configuration` | **10** |
| `HMI Settings List R1 SR25` `Settings`（B／C 欄） | **10** |
| `SR26 Default Settings` `Default Parameters` | **1** |
| LID `637MCA Specific Signals` | **2** |
| `SR24 R1 Market Configuration Table` | **0** |

### E26 —— Atlantis vs Atlantis High

| 項 | Atlantis（P–T） | Atlantis High（Z–AD） |
|---|---|---|
| CAN 形段 1 命中列數 | 30 | 30 |
| **該欄組實際解出 `MESSAGE.Signal`** | **30** | **26** |

**E26 過**（30 ≥ 26）。命中列數相等係因命中發生在共用之名稱欄（A/B/C），
分野在各欄內是否有值。逐名對照表落 `data/atlantis_vs_high_v42.tsv`
（**124 列**，本包重產並加 `seg3_637` 欄）。

`CAN` 欄值（本線命中列）：**Atlantis Q 欄** `PROXI`×10、`CAN-B`×3；
**Atlantis High AA 欄** `FD`×13、`CAN-B`×8、`CAN-B/FD` 混×2、`CFTS102`×1
—— 與 R-VL14(a) 之「本件為 BH-CAN、Atlantis High 之件為 FD／BH」一致。

**架構差異（非 B-1）18 名**：同名於兩欄組解出不同 `MESSAGE.Signal`，逐列於對照表。
**段 1 不適用（R-VL12(c)）83 名**：規格原名已為 `MESSAGE.Signal` 形而段 1 未命中，
直入段 3。`637MCA Specific Signals` 分頁命中 **2** 名。

---

## 4. W-5′-4／5／6 段 3 與結果

段 3 主件＝ATL-Mi DBC；Atlantis High 之 `PDT27_E2A_R1_BHCAN2`／`FDCAN8` 降旁證，
存於 `seg3_side_high` 欄。輸出 `data/signal_chain_v42_v3.tsv`，**251 列 × 16 欄**。

| 結果 | 總 | CAN(112) | Req(69) | Info(32) | GUI(2) | PROXI(36) |
|---|---|---|---|---|---|---|
| **解得** | **98** | 95 | 1 | 1 | 0 | 1 |
| 未解得(止於段1) | 94 | 0 | 62 | 28 | 2 | 2 |
| 未解得(止於段3) | 9 | 9 | 0 | 0 | 0 | 0 |
| 訊息名不符(R-13) | 7 | 7 | 0 | 0 | 0 | 0 |
| **B-1 衝突** | **1** | 1 | 0 | 0 | 0 | 0 |
| PROXI路徑(R-P375b/c) | 35 | 0 | 3 | 2 | 0 | 30 |
| UI路徑(R-P375b) | 3 | 0 | 2 | 1 | 0 | 0 |
| UI+PROXI 雙路徑 | 4 | 0 | 1 | 0 | 0 | 3 |
| 未解得（CAN-C DBC 未到件） | **0** | 0 | 0 | 0 | 0 | 0 |
| 查無(R-G13) | 0 | 0 | 0 | 0 | 0 | 0 |

`forms/LOOKUP_MISSES.md` **未新增任何列**。

### E27′ —— 每一「解得」列之段 3 備註

**98／98 皆有備註**，格式 `BO_<msgid> <BO_名> / SG_ <SG_名> / VAL_ <有 n 項｜無>`。
其中 **VAL_ 有者 97 名、無者 1 名**。
（`<label>` 依 R-VL14(d)／IN §8.7.5(a) 逐字取本 DBC 之 `VAL_`；
該 1 名無 `VAL_` 者於 P4 寫 `= <raw>` 而無 `(<label>)`，屆時須註明。）

### R-VL14(c) —— CAN-C 情形

**本線實測 0 名。** 9 個「未解得(止於段3)」之 `Atlantis CAN` 欄**皆為空**，非 CAN-C。
故 CAN-C DBC 於本線**無實據需求**，依 Pei 裁**不預開 DR**。

九名逐一（供分析層判）：

| 名 | 段 2 解至 |
|---|---|
| `TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req` | 同名（段 1 不適用） |
| `IPC_VEHICLE_SETUP.SdwChimeVolume` | 同名 |
| `TELEMATIC_VEHICLE_SETUP.SdwChimeVolume_Req` | `IPC_VEHICLE_SETUP.SdwChimeVolume` |
| `IPC_VEHICLE_SETUP.AutomaticResetTripB` | 同名 |
| `TELEMATIC_VEHICLE_SETUP.AutomaticResetTripB_Req` | 同名 |
| `IPC_VEHICLE_SETUP.PassiveEntry` | **`RFHUB3.RFReq`**（LID Atlantis 欄所指，本 DBC 查無） |
| `TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req` | **`RFHUB3.RFReq`**（同上） |
| `SERVICE_SETUP.RestoreDefaulSetting` | 同名（**拼字，見 A-VL12**） |
| `TELEMATIC_SERVICE_SETUP.RestoreDefaultSettimgReq` | 同名（**拼字，見 A-VL12**） |

### 訊息名不符(R-13) 七名（`SG_` 查得而其 `BO_` 與規格訊息名不符）

| 規格原名 | `SG_` 實際所屬 `BO_` |
|---|---|
| `BRAKE1.VehicleSpeedVSOSig` | `STATUS_CCAN3` |
| `BRAKE1.VehicleSpeedVSOSigFailSts` | `STATUS_CCAN3` |
| `IFSTATUS_TTM.TrailerConnectionSts` | `STATUS_TTM` |
| `TELEMATIC_SERVICE_SETUP.PrivacyModeReq`（段 2 解至 `GLOB_LTM.PrivacyModeReq`） | `TELEMATIC_SERVICE_SETUP` |
| `TELEMATIC_VEHICLE_SETUP4.HeadlampOnWithWiperEnable` | `IPC_VEHICLE_SETUP…` |
| `TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock` | `IPC_VEHICLE_SETUP` |
| `SERVICE_SETUP.TelematicSetupACK` | `IPC_VEHICLE_SETUP` |

依 R-VT9／R-VL12 之同判：**記「訊息名不符(R-13)」，不記 B-1，保留規格原名**。

### W-5′-7 `VehicleSpeedVSOSig` 兩弧

本線有該型，四名（`BRAKE1.VehicleSpeedVSOSig{,FailSts}`／
`STATUS_CCAN3.VehicleSpeedVSOSig{,FailSts}`）。依 R-VT12(a) **各自解析、不互為旁證**：
`STATUS_CCAN3` 兩名**解得**，`BRAKE1` 兩名記**訊息名不符(R-13)**。
**未以其一代其二、未合併。**

### E30 —— 同母體分布差

| 結果 | v1 | v3 | 差 |
|---|---|---|---|
| 解得 | 35 | **87** | **+52** |
| 未解得(止於段1) | 100 | 94 | −6 |
| 未解得(止於段2) | 35 | 0 | −35 |
| 未解得(止於段3) | 0 | 7 | +7 |
| 訊息名不符(R-13) | 27 | 2 | **−25** |
| B-1 衝突 | 0 | 1 | +1 |
| UI路徑 | 1 | 3 | +2 |
| UI+PROXI 雙路徑 | 0 | 4 | +4 |

（同母體 v1 ∩ v3 = 233 名。）

對 **v2**（同母體 251 名，僅段 3 之件不同）：

| 結果 | v2 | v3 | 差 |
|---|---|---|---|
| 段3待ATL-Mi DBC | 73 | **0** | −73 |
| 解得 | 0 | **98** | **+98** |
| 訊息名不符(R-13) | 40 | **7** | **−33** |
| 未解得(止於段3) | 0 | 9 | +9 |
| B-1 衝突 | 2 | **1** | −1 |

> **此表即 R-VL12(b)／R-VL14 之驗證**：只換段 3 之件（Atlantis High → ATL-Mi），
> 「訊息名不符」由 40 降為 7。**上繳 02 之「訊息名不符 27」與上繳 03 前版之 40，
> 其多數並非規格與 DBC 之真實不符，而是比對了錯誤家族之 DBC。**

---

## §K 衝突表（E28 = 1）

| # | 規格原名 | 類 | 命中處 A | 解得 A（段 3） | 命中處 B | 解得 B（段 3） | 交 Pei 之問 |
|---|---|---|---|---|---|---|---|
| K-1 | `TELEMATIC_VEHICLE_SETUP.LanguageSelection_Req` | CAN | `LID/CAN Mapping/r1112cP/Atlantis Signal Name/R1 逐字` | `TELEMATIC_VEHICLE_SETUP.LanguageSelection_Req` → `BO_158 TELEMATIC_VEHICLE_SETUP / SG_ LanguageSelection_Req / VAL_ 有 22 項` | `LID/CAN Mapping/r1111cA/Logical Identifier/R3 去 _Req 後綴` | `IPC_VEHICLE_SETUP.LanguageSelection` → `BO_1468 IPC_VEHICLE_SETUP / SG_ LanguageSelection / VAL_ 有 23 項` | **兩者於 ATL-Mi DBC 皆完整解得且各有 VAL_ 表**，故非查無、非訊息名不符，為真 B-1。A 為**目標欄逐字**（最強證據），B 為名稱欄之弱規則命中。**規則強弱之優先序下放包未裁**，不自選 |

**K-2（前版之 `Country_Code`）已消解**：其兩標的中 `META_DATA.ADAS_Meta_CountryCode`
於 ATL-Mi DBC 查無，僅 `Car_Configuration_16.Country_Code` 一路成立，結果改為
PROXI 路徑。**B-1 由 2 降為 1。**

**建議（不自行施行）**：一條規則優先序即可消解 K-1 ——
「目標欄（`Atlantis Signal Name` P）之 R1 逐字命中，勝過名稱欄（A/B/C）之 R3／R4 命中」。
採之則 B-1 歸零，K-1 解為 `TELEMATIC_VEHICLE_SETUP.LanguageSelection_Req`。

---

## 5. W-7 與 P3 前置

**兩者於 2026-09-01 之前版已執行並入庫（commit `743455a`），本包實測其成果未變，未重做：**

| 項 | 實測 |
|---|---|
| `leaves.tsv` `remarks` 欄 | 在；`-051`／`-063` 兩列標記各 1 |
| `-051` | `tc_status = UNCATEGORIZED`（不入母體、不排除），註 A-VL5／DR-VL2(a) |
| `-063` | `tc_status = leaf`（入母體，R-VL4），註 A-VL7／DR-VL2(c) |
| A-VL5／6／7 | 標題狀態為「併 DR-VL2(a)／(b)／(c)」 |
| A-VL9 | RESOLVED（R-VL12(e)） |
| P3 前置 | `data/p3_families_v42.md`，24 家族、leaf 合計 128 |

母體維持 **128**。

**P3 之兩個對映維度（前版實測，本包不變）**：037 `Sub Categorization` 僅二值
（等於「來自哪一份 037」，無判別力）；SYSRA `Chapter for VF` 前二階**全為 `01.11`**
（零判別力）。Layer 2 之聚合只能靠 `Requirement Title` 語意，
或展開 `Chapter for VF` 第三階以下（待 P3 指示）。

---

## 6. A／DR 狀態

### anomaly

| 編號 | 狀態 | 本包之變動 |
|---|---|---|
| A-VL1／A-VL2／A-VL3／A-VL4／A-VL9／A-VL10 | RESOLVED | 無 |
| A-VL5／A-VL6／A-VL7 | 併 DR-VL2(a)/(b)/(c) | 無 |
| **A-VL8** | **阻塞面已解除**；段 1 命中率之問仍 PENDING | 更新：解得 98、訊息名不符 40→7、待件 73 歸零；**未解除者**＝ CAN 112 名中段 1 僅命中 30，其餘 82 依 R-VL12(c) 直入段 3，`637MCA` 分頁仍只 2 名 |
| **A-VL11** | **新開**（PENDING） | DBC 之 `SG_` 驗收數 5568 vs 實測 844 |
| **A-VL12** | **新開**（PENDING） | 規格三對拼字歧異，各對一方解得、另一方查無 |

**A-VL11／A-VL12 未成對開 DR** —— 補遺明令「DR 送出事項全數改為 Pei 裁先不送」，
且 A-VL11 為條文數字之更正（內部），A-VL12 待分析層先裁筆誤認定。
**刻意之不成對，非漏做。**

### DR

| DR | 狀態 |
|---|---|
| DR-VL1 | 已登記，未送出（實數 191） |
| DR-VL2 | 已登記，未送出（A-VL5／6／7 三面） |
| **DR-VL3** | **結案**（到件，非送出）；執行層結案紀錄已落 `DATA_REQUESTS.md` |

**本包未送出任何 DR。**

---

## 7. 獨立判斷

1. **一項須裁而本包不裁**：K-1 之規則優先序（第 §K 節）。
2. **一項條文數字待更正**：R-VL14(a) 之 `SG_ 5568`（A-VL11）。
3. **一項待分析層先裁方能施作**：A-VL12 之兩對拼字是否認定為規格筆誤 ——
   R-13 要求保留規格原名，若認定為筆誤而採正確拼法，須明裁；不裁則
   `RestoreDefaulSetting`／`RestoreDefaultSettimgReq` 兩名於 P4 只能保留原名不加 `$`。
4. **一項本包發現而下放包未涵蓋**：`IPC_VEHICLE_SETUP.PassiveEntry` 與
   `TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req` 之段 1（LID Atlantis 欄）解至
   **`RFHUB3.RFReq`** —— 一個與規格原名完全不同族之訊息，且該名於 ATL-Mi DBC 查無。
   此非拼字、非架構差異，而是 **LID 之對映指向他 ECU**。
   本包記「未解得(止於段3)」並保留證據，**不臆測、不改判**，交分析層。
5. **一項本包未做且指得出理由**：三版 tsv（v1／v2／v3）並存而未合併為單一檔 ——
   下放包令「v1 不覆寫」，v2 為前版產物，合併需裁。
6. **R-VL13 之 `body_sha8` 在兩次執行間變動**（第 1 節），已記明。

---

## 8. `gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 504
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0
```

**(甲) `rulings_hash` —— 依 R-VL13 記「待 Pei 重生」。**
以 id 為單位實測（`--out <scratchpad>`，**未寫入 repo**）：

| 類 | 內容 |
|---|---|
| 新增 id（13） | `R-VL12`／`R-VL13`／**`R-VL14`**（本線）；`R-VT11`–`R-VT15`（vsm_v43）；`R-VS84`–`R-VS88`（vehicle_setting） |
| 移除 id | **0** |
| `sha8` 變動（3） | `R-VL2`／`R-VL5`／`R-VL9`（R-TM13 加註） |
| 其中 `body_sha8` 亦變者 | **0** |

同上繳 03 前版所指：R-VL13(a) 之但書「**全為** `R-VL*`／`R-VT*` **新增列**」
仍未被字面滿足（有 `R-VS*`、有 3 筆修改列）。**本包不自行放寬**。

**(乙) `canon_refs` 504**（前版 503，+1）—— 逐檔逐行歸因，含 `vsm_v42` 者 **3 列**，
與前版**逐字相同**（`ANOMALIES.md:62` 之 `R-G40`、`RUNBOOK.md:9` 之裸 `§3`、
`DECISIONS.md:3` 之裸 `§4`，後二者為共用腳本模板）。
**本包新寫之檔未新增任何一列**；+1 落於本線之外（vsm_v43 同時在跑）。

**(丙)(丁) `gates_tsv`／`lint_paths` = 4** —— 與本線無關，先在，與上繳 02／03 前版相同。

**無一支肇因於本包之寫入。**

---

## 9. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `features/vsm_v42/data/signal_chain_v42_v3.tsv` | **新建**（251 列 × 16 欄）；v1／v2 未覆寫 |
| `features/vsm_v42/data/atlantis_vs_high_v42.tsv` | 重產（124 列，加 `seg3_637` 欄） |
| `features/vsm_v42/ANOMALIES.md` | A-VL8 更新；**A-VL11／A-VL12 新開** |
| `features/vsm_v42/DATA_REQUESTS.md` | DR-VL3 之執行層結案紀錄 |
| `features/vsm_v42/docs/upstream/03_signal_atlantis.md` | **改寫**（取代 2026-09-01 前版） |
| `features/vsm_v42/docs/INDEX.md` | 03 列更新 |

**未動**：`docs/fw036/RULINGS.sha.tsv`（R-VL13）、`scripts/`、`forms/`（含
`LOOKUP_MISSES.md`、新到之 DBC **唯讀**）、`docs/runtime/`、`features/vsm_v43/`、
`features/vehicle_setting/`、`sources/`、`features/vsm_v42/{RULINGS.md,
feature.yaml, sandbox/, data/leaves.tsv, data/signal_chain_v42.tsv,
data/signal_chain_v42_v2.tsv, data/p3_families_v42.md}`、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 10. 待 Pei／分析層之五項

1. **§K K-1 之規則優先序** —— 目標欄 R1 逐字是否勝過名稱欄 R3／R4。採之則 B-1 歸零。
2. **R-VL14(a) 之 `SG_ 5568` 更正為 844**（A-VL11）。
3. **A-VL12 之兩對拼字**是否認定為規格筆誤（涉 R-13 保留原名之例外）。
4. **`PassiveEntry` 二名之 LID 對映指向 `RFHUB3.RFReq`**（第 7 節第 4 項）如何處置。
5. **R-VL13(a) 之但書**（第 8 節甲）＋ 台帳重生時機 ＋ 共用腳本一裁（六項）
   ＋ `_intake/Vehicle_Setup_VF665/` 空目錄刪除。
