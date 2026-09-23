# RD_FEEDBACK — Camera（FW036 A 本 037，SWRA_V02）

建檔依據：下放包 `docs/fw036/handoff/down/20260923_CAM-06.md` §1
（CAM-05 審閱 §三-1「登 RD 反饋清單」，Pei 2026-09-23）。

**本檔之用途與界線**：供 Pei 回 037 之 RD 作者；**TC 側不承接**，
即本檔任一條皆不改 TC 之生成範圍，亦不作 `specification_reference` 之依據。
每條之格式為「觀察 → 證據（可複驗之座標）→ TC 側現行處置 → 請求之動作」。

母本：`SWE1_CAMERA_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_V02.xlsx`
（doc_id `camera_037_swra_v02`，sha16 `cae0df17016b3532`，`Analysis Report` 分頁，
標題列為第 7 列，資料自第 8 列起）。

---

## RDF-01 —— `SWE-CAM-016` 之 CFTS092 來源混引四個相機節

**觀察**：`SWE-CAM-016`（`Camera Manual Mode Arbitration Logic`，Sub Cat `NormalCamera App`）
之 `Source Requirement ID` 列有 18 個 CFTS092 來源，橫跨 CFTS092 之四個相機節，
其中**只有 6 個屬 Rear Camera 節**，其餘 12 個分屬 Cargo/CHMSL、Surround View、
Forward Facing 三節，與該 SWE 列之題名（Rear 之手動模式仲裁）不同題。

**證據**（節界依 R-CAM12 之實測，五個 `Heading` 列）：

| 節 | 節界 | `-016` 所引 |
|---|---|---|
| Cargo/CHMSL Camera（§1.3.5）| `-060`(4781625) 起 | `-063`、`-067`、`-068` |
| **Rear Camera（§1.3.6）** | `-070`(4781635) 起 | `-072`、`-073`、`-074`、`-076`、`-080`、`-081` |
| Surround View Camera（§1.3.7）| `-083`(4781648) 起 | `-084`、`-085`、`-089`、`-090`、`-091`、`-092`、`-093` |
| Forward Facing Camera（§1.3.8）| `-094`(4781659) 起 | `-095`、`-096` |

**TC 側現行處置**：依 **R-CAM13** 全數生成，12 列落 Test Set `Additional Cameras`
（`batch01b/`，`NR1L-RVC-034` 起），不再以 Test Group 不符為由略過。
A-CA28 之「不生成」處置因而作廢。

**請求之動作**：確認 `-016` 是否應拆為四列（每個相機節一列），或其題名／
Sub Categorization 應改寫為涵蓋四相機之軟鍵行為。現況下 Layer 2 之
「組 ↔ SWE 列」與「TC ↔ Test Set」被迫分離（framework VIII.2 註）。

---

## RDF-02 —— `SWE-CAM-017` 之 Description 與 VC／VM 講兩件不同的事

**觀察**：`-017` 之 `Requirement Description` 講 `CameraDisplaySts` 訊號之送出與維持，
而同列之 `Verification Criteria`／`Verification Method` 兩欄講 Air Suspension PROXI
組態與 4X → 1X 縮放重置 —— 兩者無交集。

**證據**（`Analysis Report` 之 `SWE-CAM-017` 列）：

- `[4] Requirement Description`：`The daemon shall manage the camera display state and
  transmit the CameraDisplaySts = [Default] signal to the vehicle network within <Tsend>
  upon a display state change, and continuously maintain this status until the next
  keypress trigger.`
- `[18] Verification Criteria`：`Verify that the system handles various hardware
  configurations correctly without crashing, and resets the 4X view to 1X when dictated
  by the camera module.`
- `[19] Verification Method`：`Configure the PROXI to simulate an Air Suspension setup and
  power cycle the system. Confirm no system crash occurs. Trigger a 4X zoom, then send the
  reset command from the camera module and verify the UI returns to 1X zoom.`
- 其 `Source Requirement ID` 六個來源（`SYS-RA-CAM-097`／`-098`／`VF551_V2-569`／
  `-578`／`-580`／`VF551_V3-185`）**全數對應 Description 側**，無一講 Air Suspension
  或 4X → 1X；`-578`／`-580` 另為 `Out of Scope`（R-CAM9）。

**TC 側現行處置**：依 **R-CAM13(d)**「VC／VM 不是來源」，`-017` 之 TC 依 Description
與其六個來源生成；VC／VM 所述之 Air Suspension／4X→1X 因**對應不到任一所引來源**
而不生成，登本條。原 A-CA03 不因 framework 重開而結。

**請求之動作**：確認 VC／VM 兩欄是否誤植自他列（4X→1X 之重置條文實為
`SYS-RA-VF551_V2-586`／`VF551_V3-142`，由 `SWE-CAM-021`／`-023` 線所引）。

---

## RDF-03 —— 速度門檻之標定：三份文件三個值，且 037 未指定何者為準

**觀察**：Rear View Camera 之速度退出門檻在三份被引文件中各有標定，**單位皆有載明**
（原提報所疑之「無單位」不成立），但**值不相同**，037 之 `-018` 未指定以何者為準。

**證據**（逐格實測）：

| 文件 | 常數 | 值 | 單位 | 座標 |
|---|---|---|---|---|
| CFTS092 | （無常數名，條文逐字）| `8 mph` | mph | `SYS-RA-CAM-078`（ObjectID 4781643）|
| VF551_V2（Atl-Hi）| `c_VEHSPD_MAX` | **8** | **mph** | §1.8.13 表；`SYS-RA-VF551_V2-139` 名、`-138` 值、`-135` 單位 |
| VF551_V33（2261）| `MAX_SPEED` | **13,0** | **Km/h** | §1.14.1 表；`SYS-RA-VF551_V33-503` 名、`-504` 值、`-507` 單位；容差 `0,5`（`-506`）、範圍 `[10,0;18,0]`（`-505`）|

8 mph ＝ 12.874752 km/h，與 13,0 km/h 相差 0.125 km/h —— **落在 V33 所載之 ±0,5 容差內**，
故兩者應為同一門檻之兩種標定。CFTS092 `-078` 之 `Verification Criteria` 亦自寫
`Vehicle speed exceeds 8 mph (≈ 13 km/h)`。

**此發現對 A-CA30 之影響（須併看）**：CAM-05 §3.4 判「`>` 與 `>=` 之分歧不可觀察」，
其前提為門檻 ＝ 8 mph（12.874752 km/h，非 0.0625 km/h 解析度之整數倍，等值 raw 不存在）。
以 V33 之 `MAX_SPEED = 13,0 km/h` 計，**13.0 ÷ 0.0625 ＝ 208 為整數，等值 raw 存在**，
2261 之嚴格大於（`>`）於門檻點因而**可判**。A-CA30 之「不可判」只對 Atl-Hi（8 mph）成立。
`NR1L-RVC-030`／`-031` 之供試值依此由 raw 206／205 改為 **raw 209／208**（CAM-06 §2 自報）。

**TC 側現行處置**：各平台以各自所屬 VF 本之標定書寫；跨本不換算。

**請求之動作**：於 `-018` 之 Description 或 VC 指定門檻之權威標定
（建議以 VF 本之常數為準、CFTS092 之 `8 mph` 標為 informative），
並確認 V2 之 `c_VEHSPD_MAX = 8 mph` 與 V33 之 `MAX_SPEED = 13,0 Km/h` 是否確為同一門檻。

---

## RDF-04 —— `SWE-CAM-018` 以 `e.g.` 書寫門檻值，使其不可作驗收判準

**觀察**：`-018` 之 Description 將 8 mph 寫為 `e.g.`（舉例），
其 VC／VM 卻以 8 mph／10 mph 作具體判準 —— 同一列內「舉例」與「判準」互斥。

**證據**（`Analysis Report` 之 `SWE-CAM-018` 列）：

- `[4] Requirement Description`：`The NormalCameraDaemon shall enforce camera display exit
  conditions, maintaining the video feed until the user manually closes it, or the vehicle
  exceeds the speed threshold (e.g., 8 mph) for the defined 10s duration.`
- `[18] Verification Criteria`：`Simulate the vehicle speed > 8 mph …`
- `[19] Verification Method`：`… simulate a vehicle speed of 10 mph …`
- 同型措辭另見 `SWE-CAM-016` `[4]`：`… default vehicle speed restrictions
  (e.g., VehicleSpeedVSOSig).` —— 訊號名亦以 `e.g.` 書寫。

**TC 側現行處置**：門檻值不取 037 之 `e.g.` 句，一律回 SYS2 來源之常數／條文
（見 RDF-03 之表）；037 之 Description 只作題意判讀，不作 literal 來源。

**請求之動作**：將 `e.g.` 改為確定之引用（指向 VF 常數名或 CFTS092 條文），
或明文標示該括號為 informative。

---

## RDF-05 —— `SWE-CAM-003` 之 `VF617V5` 拼寫缺底線，造成第三類追不到之來源

**觀察**：全本 `VF617_V5` 之寫法一致，**惟 `SWE-CAM-003` 一列作 `VF617V5`**（缺底線），
`Source Requirement ID` 與 `Source ID` 兩欄同犯。該拼寫使機器對映多出一個 miss 類，
與 DR-CAM-a（`VF617_V5` 整本缺件）之成因不同，易被誤併為同一類。

**證據**（`Analysis Report` 之 `SWE-CAM-003` 列）：

- `[1] Source Requirement ID` 含 `SYS-RA-VF617V5-406`、`SYS-RA-VF617V5-407`
- `[2] Source ID` 含 `VF617V5`
- 全本其餘各列（`-002`／`-005`／`-006`／`-015`／`-016`／`-018`／`-021`／`-023`／`-024`）
  皆作 `VF617_V5`
- 落地痕跡：`features/camera/data/layer2_assign.tsv` 之 `SWE-CAM-003` 列
  `source_book` 欄同時出現 `VF617V5, VF617_V5` 兩形

**TC 側現行處置**：兩形視為同一本；該兩個來源與其餘 `VF617_V5` 來源同以
DR-CAM-a（缺件）處理，不生成。

**請求之動作**：更正為 `VF617_V5`（兩欄共三處）。

---

## RDF-06 —— `SWE-CAM-002` 只有配備成立側，無 Absent 側之行為

**觀察**：`SWE-CAM-002`（`PROXI based Camera Configuration and State`）之題名為
「以 PROXI 決定相機組態與狀態」，但其 20 個 in-scope 來源**全為成立側**
（`PROXI Rear_View_Camera = Present` 時啟用某行為），**無一條規定 Absent 時之行為**。
配備型需求缺 negative 側，測試無從驗「未配備時不啟用」。

**證據**（`-002` 之 in-scope 來源逐條，`features/camera/data/batch02_plan.tsv`）：

- `SYS-RA-VF551_V2-536`：`… shall enable Digital Rear View Camera behavior when
  PROXI Rear_View_Camera = Present.`
- `SYS-RA-VF551_V2-555`：`… shall enable Rear View Camera behavior when PROXI
  Rear_View_Camera = Present and Rear_View_Camera_Type = Digital`
- `SYS-RA-VF551_V3-212`／`SYS-RA-VF551_V4-112`：同型（V3 Digital／V4 Analog）
- `SYS-RA-VF551_V42-209`：`All the following requirements shall be implemented only if
  the PROXI parameter Rear_View_Camera is set to "Present".`
- 其餘 15 條為訊號 gating 與 LVDS 送出，皆以「已配備」為隱含前提
- **`Absent`／`= 0`／`not present` 三串於 `-002` 之 20 條來源逐字掃描：零命中**

對照：CFTS092 側之 VC 欄**有**寫 negative（如 `SYS-RA-CAM-084` 之
`$SVC_SK_PRSNT$ = [0] -> SVC 按鍵不顯示`），但 VC 不是來源（R-CAM13(d)）。

**TC 側現行處置**：**不生成 negative**（DECISIONS 6-18；CAM-06 審閱 §二-9）——
§8.4.1 之「不得自造規格」勝於 §7 之正負配對要求。缺口只登本條。

**請求之動作**：補一條 Absent 側之需求（例：`When PROXI Rear_View_Camera = Absent,
the HU shall not display any rear view camera image and the soft key shall not be present.`），
或明文宣告 Absent 側不在 R1L 範圍。

---

## RDF-07 —— `SYS-RA-VF551_V33-420` 之 `Rear_Camer_Enable.Info` 拼寫缺字

**觀察**：同一句內之兩個訊號名拼寫不一致 —— `Rear_Camera_Enable.Req` 正確，
緊接之 `Rear_Camer_Enable.Info` **少一個 `a`**。該句為 2261 關機時寫入 NVM 之清單，
拼寫錯誤使機器對映多出一個查無項。

**證據**（VF551_V33 §1.13.2.1.1，`SYS-RA-VF551_V33-420`，anchor `VF551_V33_P226MCA_VF_320`）：

> During the transition LTM_OperationalModeSts.Info=="Ignition_Pre_Off", LTM stores DTC and
> **Rear_Camera_Enable.Req Rear_Camer_Enable.Info** values into its non volatile memory.

同本之他列一律作 `Rear_Camera_Enable.Info`（例 `SYS-RA-VF551_V33-214`：
`Consider Rear_Camera_Enable.Info="FALSE" as the init default value.`）。

**TC 側現行處置**：`NR1L-RVC-064` 之 test_item 上半依 §4.3.1 **逐字照錄不更正**
（更正即破壞保序子序列之機器判準）；reasoning 已具名該拼寫。

**請求之動作**：更正為 `Rear_Camera_Enable.Info`（一處）。


---

## RDF-08 —— `SYS-RA-VF551_V3-281` 之 gating 標的誤植

**觀察**：主句之 gating 標的與其 `a)` 子句所指不一致 —— 主句寫「gate 到 `STATUS_CCAN5.LWSAngle`」
（即**來源訊號自身**，gating 至自己無意義），`a)` 子句則寫 `vehicleUpdate_2.LwsAngle`（正確之 LVDS 標的）。

**證據**（VF551_V3 §1.10.2，`SYS-RA-VF551_V3-281`，anchor `VF551_V3_P363_VF_615`）：

> · The Head Unit shall gate BH-CAN STATUS_CCAN5.LWSAngle to LVDS **STATUS_CCAN5.LWSAngle**
> a) The Head Unit shall send LVDS **vehicleUpdate_2.LwsAngle** = [SNA] when BH-CAN
> STATUS_CCAN3.VehicleSpeedVSOSig is missing…

同本之兄弟列一律作 `to LVDS vehicleUpdate_2.<Signal>`（`-280` 速度、`-282` 排檔）。
另注意其 `a)` 子句之**條件**亦寫 `STATUS_CCAN3.VehicleSpeedVSOSig is missing` ——
與主句之 `STATUS_CCAN5.LWSAngle` 不同訊號，疑為第二處誤植。

**TC 側現行處置**：test_item 上半逐字不改（§4.3.1）；ER 以 `a)` 子句之正確標的
`vehicleUpdate_2.LwsAngle` 書寫，reasoning 具名該誤植（CAM-09 審閱 §一-6）。

**請求之動作**：主句標的更正為 `vehicleUpdate_2.LwsAngle`；並確認 `a)` 子句之條件訊號。

---

## RDF-09 —— `SYS-RA-VF551_V3-283` 之 `a)` 子句標的誤植

**觀察**：`a)` 子句之送出標的寫成**來源側之 CAN 訊號**而非 LVDS 訊號。

**證據**（VF551_V3 §1.10.2，`SYS-RA-VF551_V3-283`，anchor `VF551_V3_P363_VF_613`）：

> · The Head Unit shall gate BH-CAN STATUS_CCAN4.ReverseGearSts to LVDS vehicleUpdate_2.ReverseGearSts
> a) The Head Unit shall send LVDS **STATUS_CCAN4.ReverseGearSts** = [SNA] when BH-CAN
> STATUS_CCAN4.ReverseGearSts is missing…

主句之標的正確（`vehicleUpdate_2.ReverseGearSts`），`a)` 子句卻回寫來源名。

**TC 側現行處置**：同 RDF-08 —— 上半逐字不改，ER 以主句之標的書寫。

**請求之動作**：`a)` 子句之標的更正為 `vehicleUpdate_2.ReverseGearSts`。

---

## RDF-10 —— `SYS-RA-VF551_V42-590` 與 `-584` 逐字同句，Communications_Timeout 缺清除側

**觀察**：V42 之三組 DTC 條文（Internal／External／Communications）各應有 set／clear 一對，
惟 **Communications 組之清除側（`-590`）其句子寫的是 `InternalErrorStatus`** ——
與 Internal 組之清除側（`-584`）逐字同句。結果：**`Communications_Timeout` 之清除側無條文**。

**證據**（VF551_V42，三組之節序）：

| 組 | set | clear |
|---|---|---|
| Internal | `-583`（`systemStatus.InternalErrorStatus = "True"`）| `-584`：`Once the systemStatus.**InternalErrorStatus** signal is set to "False", LTM shall: set the DTC to not present …` |
| External | `-586`（`ExternalErrorStatus = "True"`）| `-587`：`Once the systemStatus.**ExternalErrorStatus** signal is set to "False" …` |
| **Communications** | `-589`（`Communications_Timeout = "True"`）| `-590`：`Once the systemStatus.**InternalErrorStatus** signal is set to "False" …` ← **應為 `Communications_Timeout`** |

`-584` 與 `-590` 之 `Description` 逐字相同，只 anchor 不同（`…VF_1993` vs `…VF_1995`）。

**TC 側現行處置**：`batch03_plan.tsv` 之 `-590` 列記 `covered_by: V42-584`，
**不造 Communications 之清除側**（§8.4.1）。該側之覆蓋缺口由本條承接。

**請求之動作**：`-590` 之訊號名更正為 `systemStatus.Communications_Timeout`。

---

## RDF-11 —— `“X”` 退出鍵之位置：SYS1 載 upper right，Pop Up List `PU0170` 載 bottom right

**觀察**：同一個 `X` 退出鍵，兩份來源文件載其位置**相反**。

**證據**：

| 來源 | 座標 | 逐字 |
|---|---|---|
| SYS1 RVC+PAM（cache 本）§7.5.3 | `NRL-142629` | `In ANY OTHER GEAR, the camera image will display an “X” in the **upper right** corner of the screen.` |
| SYS1 RVC+PAM（cache 本）§8.1 | `NRL-142631` | `an “X” exit button will be placed in the **upper-right** corner of the screen (PU0170)` |
| `forms/Pop Up List HMI R1 (26PI).xlsx` `Main`，`PU0170`（module `Rearview Camera`）| —— | `A clear ‘X’ exit button will be placed in the **bottom right** corner while the user is in Drive and camera delay is active.` |

SYS1 內部兩處**自洽**（皆 upper right），與彈窗表相左；且 §8.1 本身即引 `PU0170`，
故非兩條獨立需求之差異，而是同一需求之兩處記載不一。

**TC 側現行處置**：依 **§4.3.1** 以 SYS1 之逐字為 ER —— `NR1L-RVCHMI-038` 判
`the "X" exit button is shown in the upper-right corner of the camera image`；
差異註於該列之 `Remarks` 欄（profile §10 第二類）。**不改彈窗表、不造第三種位置。**

**請求之動作**：確認 `X` 鍵之實際位置，並更正兩份文件中之錯者。
疑為彈窗表之舊稿（其文字欄另載 `[v.SR12]` 之版本註）。

---

## 索引

| # | 標的列 | 類 | 對應 anomaly／DR |
|---|---|---|---|
| RDF-01 | `SWE-CAM-016` | 來源混引跨節 | A-CA28（處置經 R-CAM13 作廢）|
| RDF-02 | `SWE-CAM-017` | Description ↔ VC/VM 錯位 | A-CA03 |
| RDF-03 | `SWE-CAM-018` | 標定值跨文件不一 | A-CA21／A-CA22／A-CA30 |
| RDF-04 | `SWE-CAM-018`（`-016` 同型）| `e.g.` 使判準不確定 | —— |
| RDF-05 | `SWE-CAM-003` | 來源代號拼寫 | DR-CAM-a（須分類）|
| RDF-06 | `SWE-CAM-002` | 配備需求缺 Absent 側 | DECISIONS 6-18 |
| RDF-07 | `SWE-CAM-001`（`V33-420`）| 訊號名拼寫缺字 | `NR1L-RVC-064` |
| RDF-08 | `SWE-CAM-011`（`V3-281`）| gating 標的誤植 | batch03b |
| RDF-09 | `SWE-CAM-011`（`V3-283`）| `a)` 子句標的誤植 | batch03b |
| RDF-10 | `SWE-CAM-004`（`V42-590`）| 同句誤植致缺清除側 | batch03c |
| RDF-11 | `SWE1-RVC-024-01`（SYS1 §8.1）| 同一需求兩處位置記載相反 | A-CA34／`NR1L-RVCHMI-038` |
