# NR1L-RVC-064 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_320`（來源列 `SYS-RA-VF551_V33-420`）

## test_item 上半（verbatim，SYS2 逐字）

> During the transition LTM_OperationalModeSts.Info=="Ignition_Pre_Off", LTM stores DTC and Rear_Camera_Enable.Req Rear_Camer_Enable.Info values into its non volatile memory.

## reasoning

驗證目標為 `SYS-RA-VF551_V33-420` 之「`Ignition_Pre_Off` 轉態時，LTM 將 DTC 與 `Rear_Camera_Enable.Req`／`Rear_Camer_Enable.Info` 之值存入非揮發性記憶體」。**與 `NR1L-RVC-061` 之分工**：`-061` 驗「下次開機保留」（讀側），本列驗「關機時寫入 NVM」（寫側）——以**斷電**區別二者：僅點火循環不足以證明值在 NVM（可能留在 RAM），斷電後仍保留才證明已落 NVM（§6 可判性）。`Ignition_Pre_Off` 之 `CmdIgnSts` 對應值無來源（DR-CAM-i），Pre-Condition 標 PENDING，procedure 以 `IGN_LK` 為最接近之關機轉態（寫法沿 pilot02 `NR1L-RVC-002`）。來源另載 DTC 之儲存 —— DTC 之讀取屬 `Diagnostics` 組（`SWE-CAM-004`／`-013`），本列不承（§8.2.1）。來源之 `Rear_Camer_Enable.Info` 為 037／SYS2 之拼寫（少一 `a`），依逐字原則不更正，登 RD_FEEDBACK 之候選。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. CAN source: BCM_FD_10.CmdIgnSts (HDCC27, DT27) / STATUS_BH_BCM2.CmdIgnSts (637, 2261, 376)
4. PENDING: DR-CAM-i the CmdIgnSts value that corresponds to Ignition_Pre_Off is not sourced
5. The camera delay setting is set to "On"
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 1 (IGN_LK)
2. Disconnect and reconnect the battery supply to the HU
3. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
4. Press "Apps" on Menu Bar to open App Drawer
5. Select "Settings" in the App Drawer
6. Select "Camera"
7. Read the "Camera" settings screen and check the state of the camera delay setting
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 1 (IGN_LK) is sent and the HU leaves the RUN power state
2. The HU is fully de-energised and energised again
3. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up
4. The App Drawer is displayed
5. The "Settings" screen is displayed
6. The "Camera" settings screen is displayed
7. The camera delay setting is still on
```
