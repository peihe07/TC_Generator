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

## RDF-12 —— `SWE1-RVC-069` 自陳 N/A 但仍須追溯

> **改題（CAM-26，R-CAM19(c)，Pei 2026-09-24）**：原題「`SWE1-RVC-069` 之來源自陳 `N/A`，037 不應將其列為 leaf」。
> 本 feature 之處置由「零 TC」改為「出一列 TC，以父題 §27.3 之可驗事實為驗證點」（`NR1L-RVCHMI-211`）；
> 回 RD 之請求不變 —— 037 仍不應將自陳 `N/A` 之列列為 leaf。

**觀察**：037 B 本把 `SWE1-RVC-069` 之 `Categorization` 填為需求類（非 `Heading`、非 `Out of scope`），
使其成為一個**應出 TC 而無從出**之 leaf。

**證據**：其 `HMI Source ID` 指向 SYS1 HeadUnitCameraSystems cache 本 §27.3.2（`NRL-188058`），
該列 `Description` **全文 4 token**：`First surface needs: N/A`（依 profile §7.7 取全文實測）。
同層鄰居為 §27.3.1（`Technical hardware requirements – (R1 High only due to architecture)`）、
§27.3.3（`Pop-up Messages …`）、§27.3.4（`Lock out conditions / Requirements`）、
§27.3.5（`Signals from head unit …`）—— 即 §27.3 之子節為 HMI 規格之**結構欄位**，
`First surface needs` 一欄於本 feature 填 `N/A`。

**TC 側現行處置**：依 **R-CAM16(b)** 記零 TC，`coverage_b.tsv` 之 disposition 為
`No TC — source states N/A (A-CA35)`，`tc_count = 0`；**不造來源未載之判準**（§8.4.1）。

**請求之動作**：將該列之 `Categorization` 改為 `Out of scope`（或 `Heading`），
使「037 之 leaf 數」與「應出 TC 之列數」一致。
同型列之全案掃描結果見 CAM-17 上繳 §3 證據表第 2 項。

---

## RDF-13 —— `Enable Wireless Cameras` 設定名之大小寫三處不一

**觀察**：同一個設定，SYS1 與彈窗表之拼法不一致，且 SYS1 內部亦不一致。

**證據**：

| 來源 | 座標 | 逐字 |
|---|---|---|
| SYS1 HeadUnitCameraSystems §27.4.1 | `NRL-188065` | `the user has to activate the **‘enable wireless cameras’** setting.` |
| SYS1 同本 §27.4.4 | `NRL-188070` | `The **‘Enable wireless cameras’** setting is dynamically updated.` |
| SYS1 同本 §27.4.5 | `NRL-188071` | `If the **Enable Wireless Cameras** setting is enabled (setting ON) …` |
| `forms/Pop Up List HMI R1 (26PI).xlsx` `PU1517`／`PU1518` | —— | `the **Enable Wireless Cameras** setting is enabled` |

三種拼法：全小寫、句首大寫、全詞首字大寫。

**TC 側現行處置**：hop label 取**彈窗表之拼法** `Enable Wireless Cameras`（與 §27.4.5 相同，
四處中佔二處且為最終畫面之權威）；B02a 六列（`NR1L-RVCHMI-063`～`-069`、`-071`～`-073` 中涉該設定者）
依此書寫。

**請求之動作**：統一為畫面上之實際標籤，並更正 §27.4.1／§27.4.4。

---

## RDF-14 —— SYS1 §34.3／§34.4 之子列逐字全等且父題全等，僅圖不同

**觀察**：`SYS1_HMI_HeadUnitCameraSystems_…` 之 §34.3、§34.4、§34.5 三節**父題逐字全等**
（`Accessing Aux Cameras – Backup Cam Only`），只 image token 不同；
其子列亦成對全等，使 037 產生**無法分辨之重複 leaf**。

**證據**（正規化後與原始格皆全等）：

| 群 | 列 | 逐字 |
|---|---|---|
| A | §34.3.1、§34.4.1、§34.6.1 | `CHMSL cam only configuration does not exist` |
| B | §34.3.2、§34.4.2、§34.6.2 | `Below screen is also accessed when shifting to REVERSE, but <X> is not present` |

群 B 之 §34.6.2 其父題為 `Accessing Aux Cameras – Backup and Cargo Cam`（配置含 Cargo），
**與 §34.3／§34.4 不同**，故可分辨；而 §34.3.2 與 §34.4.2 之父題全等，**不可分辨**。

**TC 側現行處置**：不可分辨者委派 —— `SWE1-RVC-136`（§34.4.2）委派 `NR1L-RVCHMI-086`（§34.3.2）、
`SWE1-RVC-139`（§34.6.1）委派 `NR1L-RVCHMI-087`（§34.4.1，章節號較小者承接）；
`coverage_b.tsv` 記零 TC（**A-CA36**）。**不造來源未載之區別**（§8.4.1）。

**請求之動作**：說明 §34.3／§34.4／§34.5 三節之差異（何者為哪一種螢幕配置），
或合併重複之子列。若差異只在圖，請在 `Description` 內以文字載明。

---

## RDF-15 —— Pop Up List `PU0456` 之按鈕欄拼作 `<Nol>`

**觀察**：刪除相機之確認彈窗，其**按鈕欄**與**訊息文字欄**之第二個按鈕拼法不一致。

**證據**（`forms/Pop Up List HMI R1 (26PI).xlsx` `Main` 分頁，`PU0456`，module `Aux Camera`）：

| 欄 | 逐字 |
|---|---|
| 按鈕欄 | `<X>` / `<Yes>` / **`<Nol>`** |
| 觸發欄 | `Displayed when user selects "Delete Camera"` |
| 訊息文字欄 | `Delete Camera?  <X>` … `Are you sure you want to delete [Insert Camera Name] from Uconnect?  <Yes>  <No>` |

同表之同型彈窗（`PU1518`／`PU1519`）其按鈕欄皆作 `<No>`，故 `<Nol>` 為**孤例**。

**TC 側現行處置**：`NR1L-RVCHMI-137` 之 ER 依**訊息文字欄**書寫（`<Yes>` 與 `<No>`），
差異註於該列之 `Remarks`（profile §10 第二類）。**不改彈窗表、不造第三種拼法。**

**請求之動作**：更正 `PU0456` 按鈕欄之 `<Nol>` 為 `<No>`。

---

## RDF-16 —— `Check Entire Surroundings` 之時限：SYS1 載 5 秒，Pop Up List `PU0362` 載 10

**觀察**：同一個橫幅訊息，其顯示時限於 SYS1 與彈窗表**相差一倍**。

**證據**：

| 來源 | 座標 | 逐字 |
|---|---|---|
| SYS1 RVC+PAM §8.2 | `NRL-142633` | `a message stating “Check Entire Surroundings” (**PU0362**) will be displayed for **5 seconds**` |
| SYS1 RVC+PAM §9.2 | `NRL-142646` | `Display “Check Entire Surroundings” for **5 seconds** for the following events` |
| SYS1 HeadUnitCameraSystems §28.2.1 | `NRL-188092` | `“check entire surroundings message is shown for **5 seconds**` |
| `forms/Pop Up List HMI R1 (26PI).xlsx` `Main` r365 `PU0362` | —— | module `Surround View Camera`；文字欄 `Check Entire Surroundings`；**Timeout 欄 `10`** |

同表之其餘同訊息列亦為 10：`PU0447`（`Rearview Camera with all features`，10）、
`PU0467`（`Surround View Camera`，10）；**只有** `PU1102`（`Turn Signal Activated Blind Spot View`）為 5。
即 SYS1 三處皆 5，彈窗表之相機類三處皆 10。

**TC 側現行處置**：依 **§4.3.1** 以 SYS1 之逐字為 ER —— `NR1L-RVCHMI-173`（§8.2）以 4／6 秒兩點
驗其 5 秒窗；差異註於該列之 `Remarks`（profile §10 第二類）。**不改彈窗表、不取折衷值。**

**請求之動作**：確認該橫幅之實際時限，並更正 SYS1 或彈窗表之錯者。
`§8.2` 本身即引 `PU0362`，故非兩條獨立需求之差異，而是同一需求之兩處記載不一（同 RDF-11 之型）。

---

## RDF-17 —— 同一動作於 R1 High／R1 Low 兩章異名（`Make Favorite` vs `Edit Favorite`）

**觀察**：「把某台 AUX 相機設為最愛」之控制項，SYS1 兩章給出**不同之按鍵名**。

**證據**（`SYS1_HMI_HeadUnitCameraSystems_…` cache 本）：

| 章 | 節 | 座標 | 逐字 |
|---|---|---|---|
| §30（R1 High，`Favorite a camera – Camera App`）| §30.1.2 | `NRL-188129` | `From the AUX Cam settings menu, the user presses **“Make Favorite”**.` |
| 同上 | §30.1.4 | `NRL-188131` | `the button in the settings menu updates to read **“Remove as favorite”**` |
| §34.9（R1 Low，`AUX Cam Settings`）| §34.9.4 | `NRL-188192` | `From the AUX Cam settings menu, the user presses **“Edit Favorite”**` |

兩句之句型**逐字相同**（`From the AUX Cam settings menu, the user presses “…”`），
只按鍵名相異 —— 即同一動作、同一位置、兩個 label。

**TC 側現行處置**：各依其來源之逐字書寫 —— `NR1L-RVCHMI-141`（§30.1.2）寫 `“Make Favorite”`、
`NR1L-RVCHMI-162`（§34.9.4）寫 `“Edit Favorite”`；差異記於 `b05_plan.tsv` 之 note。
**不統一、不造第三種**（§4.3.1）。

**請求之動作**：確認實機之按鍵名。若兩者本即同一鍵，請更正其一；
若 R1 Low 之鍵確為 `Edit Favorite`（即該鍵同時管新增與移除），請於 §34.9.4 補其行為說明
—— 現行條文只寫「按下」，未寫按下之後果（§30 側有 §30.1.3～§30.1.6 四列說明，§34.9 側無）。

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
| RDF-12 | `SWE1-RVC-069`（SYS1 §27.3.2）| 自陳 N/A 但仍須追溯（來源自陳 `N/A` 而 037 列為 leaf）| A-CA35／R-CAM19(c)／`NR1L-RVCHMI-211` |
| RDF-13 | `SWE1-RVC-073`／`-078`／`-079`（SYS1 §27.4.x）| 設定名大小寫三處不一 | `NR1L-RVCHMI-063` 等 |
| RDF-14 | `SWE1-RVC-136`／`-139`（SYS1 §34.3／§34.4）| 子列與父題皆逐字全等，僅圖不同 | A-CA36 |
| RDF-15 | `PU0456`（Pop Up List）| 按鈕欄拼作 `<Nol>` | `NR1L-RVCHMI-137` |
| RDF-16 | `SWE1-RVC-026`（SYS1 §8.2）| 橫幅時限 SYS1 5 秒 vs `PU0362` 10 | `NR1L-RVCHMI-173` |
| RDF-17 | `SWE1-RVC-151`（SYS1 §34.9.4）| 同動作於 R1 High／Low 異名 | `NR1L-RVCHMI-141`／`-162` |
