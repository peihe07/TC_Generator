# 上繳包 03 — vsm_v42：W-5′ Atlantis 重跑、W-7、P3 前置

日期：2026-09-01　執行層：Claude Code　對應下放包：`docs/handoff/03_signal_atlantis.md`

## 結果分類（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | W-5′ 七項；抽名通式（R-VL12(d)）；段 1 改以 `Atlantis`(P–T) 為主、`Atlantis High`(Z–AD) 併記；段 3 降為旁證；W-7 四項；P3 前置兩表 |
| 核實無誤 | E18″ 11／11；E26 過（30 ≥ 26）；**E27 = 0**（無一名記「解得」）；E29 偽陽性 **0／20** |
| 正確地不動 | 台帳**不重生**（R-VL13(a)）；`scripts/` 未改；v1 之 `signal_chain_v42.tsv` **不覆寫**；兩筆 B-1 之標的**不自選、不合併** |

**總判：W-5′／W-7／P3 前置全數完成；E28 = 2 觸發升級 —— 該二名停下列 §K，其餘續行。**

---

## 0. E18″ —— R-VL1–R-VL11 `body_sha8`

工具 `rulings_hash.py --target features/vsm_v42/RULINGS.md --out <scratchpad>`
（**未寫入 `docs/fw036/RULINGS.sha.tsv`**，R-VL13(a)）。

| 條號 | 上繳 02 所報 `body_sha8` | 本包 | 判 | `sha8`（觀測值，本包） |
|---|---|---|---|---|
| R-VL1 | `5897969a` | `5897969a` | **同** | `2a3dd0b6` |
| R-VL2 | `01c67a04` | `01c67a04` | **同** | `d88dae19`（上繳 02 為 `582d0c6d`） |
| R-VL3 | `e306aa75` | `e306aa75` | **同** | `ec287e40` |
| R-VL4 | `08cea35e` | `08cea35e` | **同** | `49be4fb8` |
| R-VL5 | `1de01344` | `1de01344` | **同** | `0b1174ab`（上繳 02 為 `482a6990`） |
| R-VL6 | `7321474a` | `7321474a` | **同** | `bba2d813` |
| R-VL7 | `afb452ed` | `afb452ed` | **同** | `30ba05fa` |
| R-VL8 | `3c02775c` | `3c02775c` | **同** | `762824c8` |
| R-VL9 | `5a0230ee` | `5a0230ee` | **同** | `56fc8e0f`（上繳 02 為 `67a2d29b`） |
| R-VL10 | `6ced1b1f` | `6ced1b1f` | **同** | `b78694ad` |
| R-VL11 | `13a4dfcd` | `13a4dfcd` | **同** | `7689b41c` |

**11／11 逐字相同，E18″ 過。**
R-VL2／R-VL5／R-VL9 之 `sha8` 位移，成因為 R-VL12／R-VL13 依 R-TM13 於該三節加註
（R-VL9 之作廢註、R-VL5 之投遞區作廢註、R-VL2 之 R-VL12 指向註），
**三者 `body_sha8` 皆未動** —— 正是 R-VL10(a) 所預期之行為，第二次驗證其判準正確。

### R-VL12／R-VL13 之 `body_sha8`

| 條號 | **`body_sha8`** | `sha8`（觀測值） | body_kind | 行 | body_lines |
|---|---|---|---|---|---|
| R-VL12 | **`34577e46`** | `2d62ac95` | fenced | — | 20 |
| R-VL13 | **`6d382ff3`** | `0232ddea` | fenced | — | 9 |

十三條 R-VL 皆為 `fenced` 本體，無 `section` 型。

---

## 1. W-5′-1 抽名（R-VL12(d) 通式）

CAN 形改用通式 `[A-Z][A-Z0-9_]{3,}\.[A-Za-z]\w*`（不限 `_VEHICLE_SETUP` 家族）。
內部形（`.Req`／`.Info`／`.GUI`）優先於 CAN 形分類；PROXI 三式不變。

| 類別 | v1（窄式） | **v2（通式）** | 增減 |
|---|---|---|---|
| CAN | 107 | **112** | +5 |
| `.Req` | 69 | **69** | 0 |
| `.Info` | 37 | **32** | −5 |
| `.GUI` | 2 | **2** | 0 |
| PROXI | 36 | **36** | 0 |
| **合計** | **251** | **251** | 0 |

合計巧合相同，**組成不同**：v1 獨有 18 名、v2 獨有 18 名。
通式新增之 CAN 名 **18** 個，全為非 `_VEHICLE_SETUP` 家族，逐一：

`BRAKE1.VehicleSpeedVSOSig`／`BRAKE1.VehicleSpeedVSOSigFailSts`／
`STATUS_CCAN3.VehicleSpeedVSOSig`／`STATUS_CCAN3.VehicleSpeedVSOSigFailSts`／
`IFSTATUS_TTM.TrailerConnectionSts`／`STATUS_TTM.TrailerConnectionSts`／
`VF528STATUS_TTM.TrailerConnectionSts`／
`SERVICE_SETUP.{ClearPersonalData, PrivacyMode, RestoreApp, RestoreDefaulSetting,
RestoreDefaultSetting, TelematicSetupACK, TelematicSetupAck}`／
`TELEMATIC_SERVICE_SETUP.{ClearPersonalDataReq, PrivacyModeReq, RestoreAppReq,
RestoreDefaultSettimgReq, RestoreDefaultSettingReq}`

> **通式之收穫**：`SERVICE_SETUP.*`／`TELEMATIC_SERVICE_SETUP.*` 兩族（13 名）
> 承載 Clear Personal Data／Restore Default Setting／Privacy 三個 Layer 2 家族之訊號，
> **v1 之窄式全數漏掉**。R-VL12(d) 之改判在本線是實質的，不是形式的。
> 另見**規格原文之拼字**：`RestoreDefaulSetting`（少 t）與 `RestoreDefaultSetting`、
> `TelematicSetupACK` 與 `TelematicSetupAck`、`RestoreDefaultSettimgReq`（Settimg）
> 與 `RestoreDefaultSettingReq` —— 依 R-P369(b) **二拼法皆入段 1 查**，未合併；
> 三對於段 1 皆未命中，故無「解至同一標的」可判，維持各自一列。

### E29 偽陽性率（人工抽 20，seed 42）

**0／20 = 0%**。二十名逐一判讀皆為真實之 CAN 訊號／內部訊號／PROXI 參數名
（如 `IPC_VEHICLE_SETUP.SdwChimeVolume`、`TELEMATIC_SERVICE_SETUP.RestoreAppReq`、
`Remote_Door_Unlock_Menu`、`LDW_Sensibility_Setting.Req`）。

> **但此 0% 是修正後之值 —— 修正前為 5%，且成因在本執行層，據實登出。**
> 見第 6 節「自我糾錯」與 A-VL9 之補正段。

---

## 2. W-5′-2／3 段 1 與段 2：Atlantis vs Atlantis High

### 2.1 欄組實測（R-VL12(a) 之複驗）

LID `CAN Mapping` r2／r3 逐格讀取，五個欄組確認：

| 欄組（r2） | 欄範圍 | Signal Name | CAN |
|---|---|---|---|
| Powernet | F–J | F | G |
| CUSW | K–O | K | L |
| **Atlantis** | **P–T** | **P** | **Q** |
| Compact | U–Y | U | V |
| Atlantis High | Z–AD | Z | AA |

**與 R-VL12(a) 所載逐字相符。**

### 2.2 比對規則（五規則，命中逐一載明欄／列／規則）

| 規則 | 內容 | 使用次數 |
|---|---|---|
| R1 | 逐字 | 114 |
| R2 | 去 `MESSAGE.` 前綴 | 30 |
| R2′ | 去 `.Req`／`.Info`／`.GUI` 後綴（內部訊號取點左基名） | （併入下列組合） |
| R3 | 去 `_Req`／`_Sts`／`_Info` 後綴 | 12 |
| R4 | 底線↔空白、大小寫（與 R1–R3 組合） | 59 |
| R5 | 去 `_Menu`／`_Setting`（僅 HMI Settings／PROXI／SR26／SR24） | 35 |

命中證據格式：`檔/分頁/r{列}c{欄}/欄名/規則`，逐列存於
`data/signal_chain_v42_v2.tsv` 之 `seg1_atl`／`seg1_atlh`／`seg1_other` 三欄。

> **R2′ 為本包發現之必要規則，非自創第六規則**：下放包列「去 `MESSAGE.` 前綴」，
> 若對內部訊號 `Auto_High_Beam_Enable.Req` 施行，取到的是 `Req` 兩字母，無意義。
> 內部訊號要取的是**點左**之基名。初版誤用前者，致 `.Req` 69／69、`.Info` 37／37
> 全數落成「未解得(止於段1)」；修正後 `.Req` 有 7 名、`.Info` 有 4 名解出路徑。
> 此為下放包規則表述之邊界情形，**不是新規則，是同一規則對內部訊號之正確施行方向**，
> 故未依第 7 節「需第六規則即回報不自創」停下；一併在此陳明供裁。

### 2.3 段 1 七檔命中（涉及訊號名數）

| 檔／分頁 | 名數 |
|---|---|
| `PROXI_HDCC27_R3` `Format`（F 欄 Parameter Name） | **57** |
| LID `CAN Mapping`（A/B/C ＋ P ＋ Z） | **33** |
| LID `Proxi & Configuration` | **10** |
| `HMI Settings List R1 SR25` `Settings`（**B／C 欄**） | **10** |
| `SR26 Default Settings` `Default Parameters` | **1** |
| `SR24 R1 Market Configuration Table` `Market Config - R1` | **0** |
| LID `637MCA Specific Signals` | **2** |

（對照上繳 02 之 v1：PROXI 36／LID CAN Mapping 9／Proxi&Config 6／HMI Settings 2／
SR26 0／SR24 0／637MCA **0** —— 五規則與 Atlantis 欄組使段 1 命中面全面擴大。）

### 2.4 **E26** —— Atlantis vs Atlantis High

| 項 | Atlantis（P–T） | Atlantis High（Z–AD） |
|---|---|---|
| CAN 形之段 1 命中列數 | 30 | 30 |
| **其中該欄組實際解出 `MESSAGE.Signal` 者** | **30** | **26** |

**E26 過**（30 ≥ 26）。兩者命中列數相等係因命中發生在共用之名稱欄（A/B/C），
同一列兩欄組並存；**分野在該列各自欄內是否有值** —— Atlantis 欄 30 列皆有值，
Atlantis High 欄僅 26 列有值。

`CAN` 欄之值進一步佐證 R-VL12(b)：

| 欄組 | `CAN` 欄值分布（本線命中列） |
|---|---|
| **Atlantis（Q 欄）** | `PROXI` ×10、**`CAN-B` ×3** |
| Atlantis High（AA 欄） | **`FD` ×13**、`CAN-B` ×8、`CAN-B/FD` 混 ×2、`CFTS102` ×1 |

即 Atlantis 側為 CAN-B／PROXI，Atlantis High 側大量為 **FD** ——
與 forms/ 之 `FDCAN8.dbc`／`BHCAN2.dbc` 對應者是 **Atlantis High**，非本線。

### 2.5 架構差異（非 B-1）

同一名於 Atlantis 與 Atlantis High 解出**不同** `MESSAGE.Signal` 者 **18 名**，
依下放包記「架構差異」，**不記 B-1**。逐名對照表落
`data/atlantis_vs_high_v42.tsv`（124 列，欄：`name`／`kind`／`seg1_atl`／`seg1_atlh`／
`seg2_atlantis`／`seg2_atlantis_high`／`can_atl`／`can_atlh`／`arch_diff`／`result`）。

---

## 3. W-5′-4／5／6 段 3 與結果

段 3 對 `forms/PDT27_E2A_R1_BHCAN2.dbc`／`FDCAN8.dbc` 之實查**只作旁證**，
存於 `seg3_side` 欄；**結果欄一律不記「解得」**（R-VL12(b)）。

`data/signal_chain_v42_v2.tsv`，**251 列**、15 欄。v1 之 `signal_chain_v42.tsv` **未覆寫**。

| 結果 | 總 | CAN(112) | Req(69) | Info(32) | GUI(2) | PROXI(36) |
|---|---|---|---|---|---|---|
| **段3待ATL-Mi DBC** | **73** | 72 | 1 | 0 | 0 | 0 |
| 未解得(止於段1) | **94** | 0 | 62 | 28 | 2 | 2 |
| 未解得(止於段2) | **0** | 0 | 0 | 0 | 0 | 0 |
| 訊息名不符(R-13) | **40** | 39 | 0 | 1 | 0 | 0 |
| **B-1 衝突** | **2** | 1 | 0 | 0 | 0 | 1 |
| UI路徑(R-P375b) | **3** | 0 | 2 | 1 | 0 | 0 |
| PROXI路徑(R-P375b/c) | **35** | 0 | 3 | 2 | 0 | 30 |
| UI+PROXI 雙路徑 | **4** | 0 | 1 | 0 | 0 | 3 |
| 查無(R-G13) | **0** | 0 | 0 | 0 | 0 | 0 |
| **解得** | **0** | 0 | 0 | 0 | 0 | 0 |

| 檢 | 預期 | 實測 | 判 |
|---|---|---|---|
| **E27** 結果 `解得` | 0 | **0** | **過**（R-VL12(b) 未違） |
| **E28** B-1 衝突 | 0 | **2** | **不符 → 升級，見 §K** |

`forms/LOOKUP_MISSES.md` **未新增任何列**（「查無(R-G13)」為 0）。

### E30 —— 同母體對 v1 之分布差

v1 251 ∩ v2 251 = **233 名**（各有 18 名獨有）。同母體 233 名之結果變動：

| 結果 | v1 | v2 | 差 |
|---|---|---|---|
| 解得 | 35 | **0** | **−35** |
| 未解得(止於段2) | 35 | **0** | **−35** |
| 段3待ATL-Mi DBC | 0 | **67** | **+67** |
| 未解得(止於段1) | 100 | 94 | −6 |
| 訊息名不符(R-13) | 27 | 28 | +1 |
| PROXI路徑 | 35 | 35 | 0 |
| UI路徑 | 1 | 3 | +2 |
| UI+PROXI 雙路徑 | 0 | 4 | +4 |
| B-1 衝突 | 0 | 2 | +2 |

**上繳 02 之「解得 35」已全數重判為 0**（R-VL12(b) 之要求）；
「未解得(止於段2)」35 名因段 1 命中面擴大而全數上移。

### W-5′-7 `VehicleSpeedVSOSig` 兩弧

本線**有**該型：`BRAKE1.VehicleSpeedVSOSig` 與 `STATUS_CCAN3.VehicleSpeedVSOSig`
（另各有 `…FailSts` 一對）。依 R-VT12(a) **各自解析，不互為旁證** ——
四名各為獨立列，段 1 皆未命中 Atlantis 欄，`seg3_side` 各記各的 DBC 實查。
**未合併、未以其一代其二。**

---

## §K 衝突表（E28 = 2，該二名停下交 Pei）

| # | 規格原名 | 類 | 命中處 A（檔/分頁/列/欄/規則） | 解得 A | 命中處 B | 解得 B | 交 Pei 之問 |
|---|---|---|---|---|---|---|---|
| K-1 | `TELEMATIC_VEHICLE_SETUP.LanguageSelection_Req` | CAN | `LID/CAN Mapping/r1112cP/Atlantis Signal Name/R1 逐字` | `TELEMATIC_VEHICLE_SETUP.LanguageSelection_Req` | `LID/CAN Mapping/r1111cA/Logical Identifier/R3 去 _Req 後綴` | `IPC_VEHICLE_SETUP.LanguageSelection` | 兩列解至**不同 MESSAGE**（TELEMATIC vs IPC）。A 為**目標欄逐字**（最強證據），B 為名稱欄之弱規則命中。**規則強弱之優先序下放包未裁**，故不自選 |
| K-2 | `Country_Code` | PROXI | `LID/Proxi & Configuration/r250cP/Atlantis Signal Name/R1 逐字` → `Car_Configuration_16.Country_Code` | `Car_Configuration_16.Country_Code` | `LID/CAN Mapping/r46cB/Function/R4 逐字+底線大小寫` → `META_DATA.ADAS_Meta_CountryCode` | `META_DATA.ADAS_Meta_CountryCode` | 同名於 config 與 ADAS meta 兩處，解至不同 MESSAGE。另 `PROXI/Format/r468cF` 逐字命中（PROXI 路徑）—— **三路並存** |

**兩筆皆為 R-VL6(c)／R-VT6(c) 字面之 B-1（多命中解至不同標的），非「訊息名不符」。**
二者於 tsv 中 `result = B-1 衝突`，**未擇一、未合併**；其餘 249 名續行不受影響。

**本包建議之待裁點（不自行施行）**：K-1 之型態可由一條**規則優先序**消解 ——
「目標欄（Atlantis Signal Name P）之 R1 逐字命中，勝過名稱欄（A/B/C）之 R3／R4 命中」。
若分析層採之，K-1 解為 `TELEMATIC_VEHICLE_SETUP.LanguageSelection_Req`，B-1 歸零。
K-2 不因此消解（兩處皆有 R1 逐字）。

---

## 4. W-7 —— A-VL5／6／7 處置落地

| 動作 | 實測 |
|---|---|
| `leaves.tsv` 加 `remarks` 欄（14 欄，152 列） | 完成 |
| `-051`（`SWE1-VC-IntelligentSpeedLimiterwithConfirmation-051`） | `tc_status = UNCATEGORIZED`（**不入母體、亦不排除**），remarks 註 A-VL5／DR-VL2(a) |
| `-063`（`SWE1-VC-SurroundCameraGridlines-063`） | `tc_status = leaf`（**入母體**，037 為需求單位之權威 R-VL4），remarks 註 A-VL7／DR-VL2(c) |
| A-VL5／A-VL6／A-VL7 | 標題狀態改為「**併 DR-VL2(a)／(b)／(c)**」 |
| A-VL9 | **RESOLVED**（R-VL12(e)：流向不於 P3 文字化，P4 逐 TC 依圖判） |

母體維持 **128**（`-051` 未加入、`-063` 未剔除）。

---

## 5. P3 前置（不鎖 Layer 2）

`data/p3_families_v42.md`：24 個 `Requirement Title` 家族，逐家族列
leaf 數／Heading 數／未分類數／037 來源檔／`Sub Categorization` 計數／
SYSRA `Chapter for VF` 前二階計數。

**24 家族 leaf 合計 128，與 00 包 §九 草案數逐項相符**（實測取代草案，結果無一項需改）。
兩處標題在 00 包為縮寫，實測全名為：

- `PARK SENSE w/o HC.1 and HC.2` → **`PARK SENSE w/o HC.1 and PARK SENSE w/o HC.2`**（5）
- `Rear Park Sense Volume` → **`Rear Park Sense Volume/ ParkSense Volume`**（6）

Layer 3 對映之兩個可用維度（實測）：

| 維度 | 值域 | 對 Layer 2 之判別力 |
|---|---|---|
| 037 `Sub Categorization` | 僅二值：`Vehicle Setting Management (VSM)`（parksense 檔）／`Display (including HAL)`（sdw 檔） | **低** —— 其實質等於「來自哪一份 037」，非功能分群 |
| SYSRA `Chapter for VF` 前二階 | **全為 `01.11`** | **零** —— 全母體同章 |

> **P3 之提醒**：兩個維度都切不開 24 家族。Layer 2 之聚合只能靠
> `Requirement Title` 本身之語意（即 00 包 §九 之作法）。
> 若需更細之對映，須用 `Chapter for VF` 之**第三階以下**（本包未展開，待 P3 指示）。

---

## 6. 獨立判斷：本包是否仍有該驗而未驗者

### 兩項自我糾錯（皆為本執行層之缺陷，已修並複驗）

1. **圖形文字還原之「同 y 接合」**（承 A-VL9）：上繳 02 之 SVG 還原以「同 y 即同行」
   接合 `<tspan>`，致圖上**相鄰但不同元件**之標籤被黏成一名，產生 **10 個偽名**，
   例：`IPC_VEHICLE_SETUP2.TyrePressureUnitClearPersonalData`
   ＝ `IPC_VEHICLE_SETUP2.TyrePressureUnit` ＋ `ClearPersonalData.Info`。
   已改為同 y 之內再依 **x 間距（門檻 140 svg 單位）**斷行，
   `image1_text.tsv` 行數 **240 → 786**，偽名 10 個全數消滅（重掃該型 → 0）。
   **E29 偽陽性率因此由 5%（1／20）降為 0%（0／20）。**
   該檔於上繳 02 已入庫，本包為修正 —— **上繳 02 之「圖單獨貢獻 158 名」係含偽名之數。**
2. **內部訊號之段 1 候選取錯邊**（見第 2.2 節 R2′）：初版對 `X.Req` 取點右之
   `Req` 而非點左之 `X`，致 `.Req`／`.Info` 共 101 名全數落成「未解得(止於段1)」。
   已修；修後 `.Req` 7 名、`.Info` 4 名解出 UI／PROXI 路徑。

### 一項該驗而**本包無法驗**

**段 3 全線待件**。`DR-VL3`（ATL-Mi 之 CAN-B／CAN-C DBC）未到，
故 112 個 CAN 名中 **73 名只能停在「段3待ATL-Mi DBC」**，40 名之「訊息名不符(R-13)」
亦是**對錯誤家族 DBC** 的比對結果 —— **該 40 之判定在正確 DBC 到件後可能全變**。
本包已於 tsv 之 `seg3_side` 保留 Atlantis High 之實查值作旁證，件到即可重跑。

### 三項具名交裁（不自行施行）

1. **規則優先序**（§K K-1）：目標欄 R1 逐字是否勝過名稱欄 R3／R4。
2. **R2′ 之地位**（第 2.2 節）：視為下放包規則對內部訊號之正確施行方向（本包所採），
   或視為第六規則而須先裁。
3. **`Chapter for VF` 第三階以下**是否展開為 Layer 3 之對映維度（第 5 節）。

### 一項已在上繳 02 提出、本包續為未決

A-VL8 之 32 名「段 1 未命中而段 3 逐字查得」—— 於 v2 已因 R-VL12(b) 全數重判為
「段3待ATL-Mi DBC」，**問題本身未消失，只是延後到正確 DBC 到件時再現**。

---

## 7. `python3 scripts/gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 503
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0
```

**(甲) `rulings_hash` —— 依 R-VL13(a) 待 Pei 重生；惟其但書未被滿足，據實陳明。**

R-VL13(a) 之免責條件為「diff **全為** `R-VL*`／`R-VT*` **新增列**」。
本包以 id 為單位實測（`--out <scratchpad>`，**未寫入 repo**）：

| 類 | 內容 |
|---|---|
| 新增 id（11） | `R-VL12`、`R-VL13`（本線）；`R-VT11`–`R-VT14`（vsm_v43）；**`R-VS84`–`R-VS88`（`vehicle_setting`，第三條線）** |
| 移除 id | **0** |
| `sha8` 變動 id（3） | `R-VL2`、`R-VL5`、`R-VL9` —— 皆因 R-VL12／R-VL13 之 R-TM13 加註 |
| 其中 `body_sha8` 亦變者 | **0** |

即 **(i) 有 `R-VS*` 之新增（第三條線，非 R-VL／R-VT）**、
**(ii) 有 3 筆 `sha8` 修改列（非純新增）** —— 兩點皆超出 R-VL13(a) 之字面。
**本包不自行放寬該但書**，據實回報：實質上仍屬良性（無移除、無 `body_sha8` 變動），
但**條文之字面未被滿足**。建議 R-VL13(a) 補為
「新增 id 全為 `R-*` 之新條、無移除、且無 `body_sha8` 變動」——
`sha8` 因加註而動是 R-VL10(a) 已認定之常態。

**(乙) `canon_refs` 503** —— 逐檔逐行歸因，含 `vsm_v42` 者 **3 列**，與上繳 02 **完全相同**：
`ANOMALIES.md:62`（分析層 A-VL2 內之 `R-G40`）、`RUNBOOK.md:9`（`new_feature.py` skeleton 裸 `§3`）、
`DECISIONS.md:3`（`recon.py` 模板裸 `§4`）。**本包新寫之四檔未新增任何一列。**

**(丙) `gates_tsv`／(丁) `lint_paths` = 4** —— 與本線無關，先在，與上繳 02 逐字相同。

**結論：無一支肇因於本包之寫入。**

---

## 8. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `features/vsm_v42/data/signal_chain_v42_v2.tsv` | 新建（251 列 × 15 欄）；**v1 未覆寫** |
| `features/vsm_v42/data/atlantis_vs_high_v42.tsv` | 新建（124 列，逐名對照） |
| `features/vsm_v42/data/p3_families_v42.md` | 新建（24 家族） |
| `features/vsm_v42/data/leaves.tsv` | 加 `remarks` 欄，`-051`／`-063` 標記 |
| `sources/extracted/vf665_v42_spec_r6/media/image1_text.tsv` | **重產**（同 y 接合之修正，240 → 786 行） |
| `features/vsm_v42/ANOMALIES.md` | A-VL5／6／7 併 DR-VL2；A-VL9 RESOLVED ＋ 補正記錄 |
| `features/vsm_v42/docs/upstream/03_signal_atlantis.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：`docs/fw036/RULINGS.sha.tsv`（**R-VL13(a)**）、`scripts/`、`forms/`（含
`LOOKUP_MISSES.md`）、`docs/runtime/`、`features/vsm_v43/`、`features/vehicle_setting/`、
`sources/raw/`、`features/vsm_v42/{RULINGS.md, DATA_REQUESTS.md, feature.yaml,
data/signal_chain_v42.tsv, sandbox/}`、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 9. 待 Pei／分析層之六項

1. **DR-VL3（阻塞 P4）**：手上有無 ATL-Mi（P637／CAN-B／CAN-C）DBC？
   在件之前，**112 個 CAN 名無一可寫 `$…$`**，其中 40 名之「訊息名不符」判定亦待重驗。
2. **§K 之規則優先序**（K-1）：目標欄 R1 逐字是否勝過名稱欄 R3／R4。採之則 B-1 由 2 降為 1。
3. **R2′ 之地位**（第 2.2 節）：本包視為既有規則對內部訊號之正確施行，非第六規則；請追認。
4. **R-VL13(a) 之但書**（第 7 節甲）：建議補為「新增 id 全為新條、無移除、無 `body_sha8` 變動」。
5. **R-VL13(a) 之追認**（下放包 03 §四-2）＋ `_intake/Vehicle_Setup_VF665/` 空目錄刪除
   ＋ 共用腳本一裁（六項）＋ DR-VL1／DR-VL2 送出。
6. **P3 之 Layer 3 維度**（第 5 節）：`Sub Categorization` 與 `Chapter for VF` 前二階
   對 24 家族**皆無判別力**（前者等於檔案來源，後者全為 `01.11`）；
   是否展開 `Chapter for VF` 第三階以下。
