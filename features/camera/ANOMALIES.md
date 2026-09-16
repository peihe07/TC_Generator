# ANOMALIES — FW036 Camera

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-CAnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

本批全部由下放包 CAM-01 任務 3-6／3-7 登記，**皆為候選，非裁定**。
每條之「實測」欄為執行層自量，母體與查詢條件見
`docs/fw036/handoff/up/20260916_CAM-01.md` §3–§4。

---

## A. 缺件

| # | 事由 | 實測 | 影響 | 狀態 |
|---|---|---|---|---|
| A-CA01 | **`VF617_V5` 缺件**（SYS2 xlsx ＋ VF docx 皆無）| A 本 541 個來源引用中 **119 個**不可解析，prefix 全為 `SYS-RA-VF617_V5`（117）＋ `SYS-RA-VF617V5`（2）| `SWE-CAM-024`（AUX Camera）12/12 全數不可追，整條 PENDING；`-003`／`-015`／`-018` 部分來源不可追 | PENDING（DR-CAM-a）|
| A-CA02 | **SYS2 `VF551_V4` 之 `VF章節`(I) 欄全空** | 321/321 空。對照 V2 752/752、V3 747/747、V33 662/662、V42 801/801 皆有值 | A 本引用之 44 列 V4 無法直接取 Layer 3 | **RESOLVED** —— R-CAM7 裁定以 `D` 欄前導號向下繼承（321/321、60 章），不回查 docx。DR-CAM-b 結案 |

## B. A 本 RD 品質（037 `SWRA_V02`，母體 25 列）

| # | 事由 | 實測（逐字） | 提議 | 狀態 |
|---|---|---|---|---|
| A-CA03 | **`SWE-CAM-017` 之描述與 VC/VM 不對齊** | 037 Description 逐字：「The daemon shall manage the camera display state and transmit the `CameraDisplaySts = [Default]` signal to the vehicle network within `<Tsend>` upon a display state change, and continuously maintain this status until the next keypress trigger.」其來源 CFTS092 `SYS-RA-CAM-097`（`4781662`）／`-098`（`4781663`）屬 Forward Facing Camera 節，原文為 HU 側訊號行為；而該列之 VC/VM 講 Air Suspension PROXI 與 4X→1X reset | 依描述暫歸 Layer 2 `State Handling`；RD 對齊後可能改歸 `HMI Overlays` | PENDING |
| A-CA04 | **`SWE-CAM-018` 把硬門檻標成「e.g.」** | 037 Description 逐字：「…or the vehicle exceeds the speed threshold (**e.g., 8 mph**) for the defined 10s duration.」CFTS092 `SYS-RA-CAM-078`（`4781643`）原文逐字：「Rear Camera display image shall remain displayed until display timer is greater than 10s AND vehicle speed is above 8 mph.」—— 為**合取之硬條件**，非舉例。VF551_V2-492 為 Manual mode 之退出條件，與之不同 | 生成時以 CFTS092 原文為準，`8 mph`／`10s` 不加 `e.g.` | PENDING |
| A-CA05 | **`VF617V5` 與 `VF617_V5` 拼寫並存** | `SWE-CAM-003` 之 `Source ID` 欄逐字：`CFTS092, VF551_V2, VF551_V33, VF551_V4, VF551_V42, VF617V5, VF617_V5` —— 同一份文件出現兩種拼法；`Source Requirement ID` 側對應 `SYS-RA-VF617V5-*` 2 個、`SYS-RA-VF617_V5-*` 117 個 | 視為同一文件；DR-CAM-a 補件時一併請上游統一 | PENDING |
| A-CA06 | **重疊列（同一批來源被兩列瓜分）** | 實測兩兩交集：`-004 ∩ -009` = **20**（母體 24／27）；`-015 ∩ -018` = **9**（42／35）；`-012 ∩ -014` = **5**（6／6）；`-020 ∩ -025` = **1/1**（`SYS-RA-VF551_V33-227`，兩列唯一來源完全相同，僅分屬 Daemon 與 App）| 逐組判其為「同一驗證點之分層」抑或「應併」；`-020`／`-025` 一組建議以 sibling 處理 | PENDING |
| A-CA07 | **下放包未列之重疊列**（本包全量掃出，交集 ≥3）| `-002 ∩ -010` = 9；`-009 ∩ -023` = 7；`-003 ∩ -022` = 5；`-001 ∩ -023`／`-003 ∩ -016`／`-008 ∩ -023`／`-010 ∩ -023`／`-016 ∩ -023`／`-017 ∩ -023` 各 4；`-001 ∩ -003`／`-002 ∩ -003`／`-004 ∩ -023`／`-010 ∩ -017` 各 3 | 與 A-CA06 同案處置；`SWE-CAM-023` 與 6 列有交集，宜優先釐清 | PENDING |
| A-CA08 | **`Sub Categorization` 與 `Description` 相斥** | `SWE-CAM-014` 之 Sub Cat 為 `NormalCameraDaemon`，其 Description 逐字以「**NCD HAL** shall manage the power shutdown notifications…」起首 | Layer 2 歸屬以何者為準，待裁 | PENDING |
| A-CA09 | **`Sub Categorization` 之混合值** | `SWE-CAM-019` 逐字 `NormalCameraApp, NormalCameraDaemon`（25 列中唯一之混合值；另注意此處寫 `NormalCameraApp` 無空格，他列為 `NormalCamera App`）| 拆 sibling 或擇一，待裁 | PENDING |
| A-CA10 | **037 標題之拼寫** | `SWE-CAM-012` Title 逐字 `Message: PowerShutDownNotifcation`（`Notifcation` 缺 `i`），`-014` Description 同拼法 | 照抄，不更正 | **RESOLVED**（CAM-01 審閱 §二-2）—— **來源原文，非 037 筆誤**。`Video_Parking_Assistance_-_LTM_VF551_V2_R1.docx` Head Unit Requirements 節逐字：「Transmit PowerShutDownNotifcation.Power_Down = True over LVDS to the RVCM」。LVDS 訊息名以來源為準（R-13）；verbatim 上半與訊號行皆保留此拼法 |

## C. SYS2 匯出之資料品質

| # | 事由 | 實測 | 影響 | 狀態 |
|---|---|---|---|---|
| A-CA11 | **`Category`(K) 欄大小寫不一致** | A 本已解析之 422 個來源，其 Category 分佈為 `Functional Requirement` 309 ＋ `Functional requirement` 77；`Out of Scope` 22 ＋ `Out of scope` 10；`Non Functional Requirement` 2 ＋ `Non Functional requirement` 2 | 任何以字面比對 Category 之篩選皆會漏算。本包之 §6 對帳採**大小寫歸一後**之數（386／32／4），與下放包預期一致 | 已知，量測一律歸一 |

## D. B 本 framework 草案之落差

| # | 事由 | 實測 | 狀態 |
|---|---|---|---|
| A-CA12 | **§5 B 本 Layer 2 之章節前提與 037 實際引用不符** | B 本 230 列實際只引 HeadUnitCameraSystems 章 `6, 27, 28, 29, 30, 31, 33, 34` 與 RVC+PAM 章 `6, 7, 8, 9, 11`。草案所據之 HU 章 `1`／`3`／`4`／`18`–`22`／`26`／`32` **一列未引**，故 Test Set `Camera App`（HU 18–22）實測 **0 列** | **RESOLVED** —— CAM-01 審閱 §四 重切八組：`Camera App` 撤組、HU 3／4／26／32 刪、新設 `Camera View Switching`（HU 28）。本包重跑實測 10／50／5／13／62／31／6／53 ＝ 230，與修訂案全合 |
| A-CA13 | **10 列未落入任何草案 Test Set** | HU `6.10`（`Non Surround View Vehicles access to Cameras:`）1 列；RVC+PAM `8.1`（`RVC1)` X 退出鍵）6 列、`8.6`／`8.7`／`8.8` 各 1 列 | **RESOLVED** —— 修訂案將 `6.10`／`8.1`／`8.6`／`8.7` 併入 `Activation and Exit`、`8.8` 併入 `PAM Integration`；重跑後未歸屬 0 |

## E1. CameraEventHal 不可注入訊號之處置（CAM-01 審閱 §二-3，本包落）

| # | 事由 | 實測／依據 | 處置 | 狀態 |
|---|---|---|---|---|
| A-CA15 | **`PT_SYSTEM_FD_1.ShiftLeverPosition_PT` 不可注入，惟僅 hybrid 分支取用** | CEH 表：Atl-H、`Supported by Harman = N`、`MD fake CEH status = Not yet`。依 `SYS-RA-VF551_V2-551`／`-552`，僅 `Hybrid_Type = REP／FCEV` 時取此訊號，其餘取 `TRANSM_FD_4.ShiftLeverPosition`（CEH 表 Atl-H、`Y`／`verified`）| `SWE-CAM-015` 之主路徑改取 `TRANSM_FD_4.ShiftLeverPosition`，**不受影響**；hybrid 分支之可測性登記於此。**不開 DR** | PENDING（僅 hybrid 分支）|
| A-CA16 | **`STATUS_LIN.DynamicGridSts`／`.DynamicGridFailSts` 不可注入** | CEH 表：Atl-M、`N`／`Not yet` 兩者皆是。屬 V33／V42 Dynamic Grid Line Overlay 線；A 本 `SWE-CAM-023` 引 `V42-230`／`-231`／`-232` | ER 若須以 `DynamicGridSts` 觀察，改以 **HMI 現象**（guideline 顯示與否）為觀察面；來源名保留（§8.7.5(f)）。**不開 DR** | PENDING |
| A-CA17 | **`IPC_VEHICLE_SETUP.LanguageSelection` 不可注入** | CEH 表：Atl-H、`N`／`Not yet`。命中 `SWE-CAM-021` 之 localized overlay | 該 TC 以 **HMI 語言設定**為觸發（§5.8(e)），不走 CAN | PENDING |

## E2. 品牌 label 之來源誤讀（本包自報）

| # | 事由 | 實測（逐格） | 影響 | 狀態 |
|---|---|---|---|---|
| A-CA18 | **CAM-01 把 `Rear View Camera Delay [CR14730]` 誤歸 Fiat，實為 Maserati** | `forms/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` 分頁 `Brand-Specific Names`：表頭 `B1`=`Jeep / Chrysler / Ram / Dodge`、`C1`=`Fiat / Fiat Commercial`、`D1`=`Maserati`、`E1`=`Alfa`。`B48`=`ParkView Backup Camera Delay`、**`C48`=空**、`D48`=`Rear View Camera Delay [CR14730]`、**`E48`=空**；49 列同形。無合併儲存格 | CAM-01 上繳 §6、profile §3.1、DECISIONS 6-3、CAM-01 審閱 §三-3 四處皆誤。R-CAM5(b) 之品牌軸於 Camera 範圍內實為**兩分支**（RAM 系 vs 其餘），非逐品牌 | **RESOLVED** —— 本包已於 DECISIONS 6-3／6-8 與 profile §3.1 更正，逐字表落 `data/brand_labels.tsv` |
| A-CA19 | **`Fastack (376)` 之品牌為 `5 = Abarth`，不在 `Brand-Specific Names` 四欄之內** | `forms/proxi/Fastback_ATL_MI/R1L_PROXI_363_376_3A_CR2783_20220802.XLSM` 分頁 `PROXI Write_Read` `Y570` = `5`；PROXI Format 表 `5 = Abarth` | 該車型之帶星號設定無品牌專屬 label 可取 | **RESOLVED** —— R-CAM5(c)′ 明文「無該品牌欄或欄空者，回落基礎 label」。Abarth 與 Fiat(2261) 同落基礎分支 |
| A-CA20 | **`SWE-CAM-025` 之訊息文字與 SYS1 不一致** | A 本 `-025` Description 逐字「display a "Camera Not in position" warning overlay」；SYS1 RVC+PAM §9.2.3（`SWE1-RVC-039`）逐字「Display "Camera Out of Position" message」。**CAM-03 實測：`Pop Up List HMI R1 (26PI)` 兩串皆 0 命中**（`Main!G` 全欄；同時含 `osition`＋`amera` 者亦 0 列）| 裁定「以 Pop Up List 為準」無法落地；兩本各依自身來源寫 ER，最終文字待補件 | **PENDING** —— DR-CAM-h（DECISIONS 6-9）|
| A-CA21 | **`= 8 mph` 邊界之 VF 與 CFTS 判準相斥** | VF551_V2 `SYS-RA-VF551_V2-496` 逐字：退出條件之一為 `BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX`（**含等於**，且為 any-of，立即退出）；`-490` 逐字 `The Ttimer2 shall start when BRAKE_FD_2.VehicleSpeedVSOSig >= c_VEHSPD_MAX.`。CFTS092 `SYS-RA-CAM-078`（`4781643`）逐字：`remain displayed until display timer is greater than 10s AND vehicle speed is above 8 mph`（**不含等於**，且為 all-of）；`-079` 逐字：`if vehicle speed is below 8mph Rear display remains until the softkey to disable it is pressed` | 恰為 8 mph 時：依 VF 立即退出、依 CFTS 不退出。pilot TC #9（`NR1L-RVC-009`）依 VF `>=` 寫 ER，reasoning 具名衝突 | PENDING |
| A-CA22 | **`c_VEHSPD_MAX` 為標定常數，且 DBC 單位為 km/h 而門檻以 mph 表示** | `BRAKE_FD_2.VehicleSpeedVSOSig`（FDCAN8 `BO_ 258`）與 `STATUS_CCAN3.VehicleSpeedVSOSig`（`BO_ 994`）之 `SG_` 皆為 `(0.0625,0) [0|511.9375] "Km/h"`，`VAL_` 僅 `8191 "SNA"`（無列舉 label）。8 mph = 12.874752 km/h，非 0.0625 之整數倍：raw 205 = 12.8125 km/h = 7.9614 mph（未達）、**raw 206 = 12.875 km/h = 8.000154 mph（首個 ≥ 8 mph 之 raw）** | `c_VEHSPD_MAX` 之標定值本包無來源可查，TC 以 raw 206 表達「恰達 8 mph」之邊界並於 reasoning 說明換算 | PENDING（標定值待補）|
| A-CA23 | **`TRANSM2` 不存在於 `forms/` 之四本 DBC** | `SYS-RA-VF551_V42-302` 逐字引 `TRANSM2.ShiftLeverPosition`；`CameraEventHal status.xlsx` 亦列 `TRANSM2.ShiftLeverPosition ｜ Atl-M ｜ Y ｜ Could emulate`。四本 DBC 全文搜尋：`FDCAN8` 有 `TRANSM_FD_1`／`_FD_2`／`_FD_4`，`BHCAN2`／`P363`／`637MCA` **無任何 `TRANSM*` message**。Atl-Mi 側實際帶 `ShiftLeverPosition` 者為 `STATUS_CCAN5`（`BO_ 998`，`VAL_ … 2 "R" …` 具備）| Atl-Mi 之 raw 值與 `VAL_` label 無法自現有 DBC 取得 | PENDING —— **DR-CAM-f**；依 R-13 保留來源名 `TRANSM2.ShiftLeverPosition`，raw/label 標 PENDING |
| A-CA24 | **「controls page」之 hop label 無 HMI 來源** | SYS1 HeadUnitCameraSystems §6.5.1（`NRL-187347`）逐字只給入口清單「The Rear View Camera can be manually activated via the controls page, apps drawer, or camera app」，**無可逐字引用之 label**；§5.3 之 `ENTER_VEHICLE_SETTINGS` 第一 hop 本即 PENDING | 依 §5.8(d) 不得臆造。pilot #5／#6 改走 **App Drawer** 路徑（`ENTER_APP_DRAWER` ＋ Menu Bar §4.1 naming table 之 `Rear View Camera`），亦為 §6.5.1 所列之入口 | PENDING —— **DR-CAM-g** |

## E3. pilot v2 生成中發現（CAM-04）

| # | 事由 | 實測 | 狀態 |
|---|---|---|---|
| A-CA25 | **`LTM_OperationalModeSts.Info` 之 `Ignition_Pre_Off` 對 `CmdIgnSts` 之值無對應來源** | 於 SYS2 `VF551_V33`／`VF551_V42`／`VF551_V2` 三本全文搜尋同時含 `OperationalModeSts` 與 `CmdIgnSts`／`IGN_LK`／`BCM_FD` 之列，**零命中**。`NR1L-RVC-002` 暫用 `1 (IGN_LK)` 並標 `PENDING: DR-CAM-i` | PENDING —— **DR-CAM-i** |
| A-CA26 | **`SWE-CAM-015` 之 Atl-Mi 自動模式進入原句逾 lint L 上限** | V3 §1.10.2.2 之 `SYS-RA-VF551_V3-260` 為 **55** RE_TOKEN（> 50）；V42 之等價句 `-225` = 61、`-302` = 51。`NR1L-RVC-004` 因而取 V3 §1.10.2.3 之 `-266`（30 token），並將 `NR1L-RVC-003` 之錨同步改為其雙生句 `V2-488`（40 token），使兩列情境對齊 | PENDING（Pei 裁：放寬 L、接受現案、或另指定來源）|
| A-CA27 | **交付語料無 §5.4 兩行式指令之例** | 全語料（三本基準 ＋ 10 本 delivered）掃 `$ ` 起首之指令行，**零命中**。`NR1L-RVC-001`／`-002` 之 adb 步驟為全案首見 | PENDING（見上繳包 §2.4 之「新句型」清單）|

## E. 同名異體

| # | 事由 | 實測 | 狀態 |
|---|---|---|---|
| A-CA14 | **SYS1 RVC+PAM 同名兩本** | REF 本 sha16 `5a1c0ab24991dcb1`（55 列）vs `spec-index/cache/` 本 `1a0bef53c6de975c`（64 列）。cache 本獨有 `7.2.1`–`7.2.6`、`7.3.1`–`7.3.3` 九列；其餘 11 列差異僅為換行編碼；Polarion ID 全同。B 本 `SWE1-RVC-016/-017/-018` 引 `7.3.1`–`7.3.3`，**只有 cache 本解得開**（對映率 100% vs REF 本 98.70%）| **RESOLVED** —— R-CAM6 裁定以 `spec-index/cache/` 本為 B 本追溯母體；REF 本於 MANIFEST note 記「同名異體，cache 本之真子集，不作追溯母體」。DR-CAM-c 結案 |

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-CAnn]`.
