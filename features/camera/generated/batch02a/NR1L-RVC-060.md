# NR1L-RVC-060 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=0
- **priority**：P2｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V33_P226MCA_VF_820`（來源列 `SYS-RA-VF551_V33-216`）

## test_item 上半（verbatim，SYS2 逐字）

> When LTM_OperationalModeSts.Info ==(equal)"Ignition_On", LTM starts to read the Rear_Camera_DelayOff.Req , Rear_Camera_Grid_Lines_Off.Req.

## reasoning

驗證目標為 `SYS-RA-VF551_V33-216` 之「Ignition_On 時 LTM 開始讀取 `Rear_Camera_DelayOff.Req` 與 `Rear_Camera_Grid_Lines_Off.Req`」。`LTM_OperationalModeSts.Info` 為 V33／V42 之來源名，依 §8.7.5(f) 保留；其對 `CmdIgnSts` 之值對應除 `Ignition_Pre_Off` 外皆以 RUN 表達（DR-CAM-i 只及該一值）。**兩者皆非 CAN 訊號**（四本 DBC 零命中），為 HMI 設定值；「已讀取」之可判後果取 Delay 設定之生效 —— 開機後退出 R 檔影像仍續顯，即該設定已被讀入（設定本身之操作由 `NR1L-RVC-067` 承接，Grid Lines 之生效由 `-062`／`-063` 承接）。設定名於工作簿以品牌中立之 `camera delay setting` 書寫，沿 `NR1L-RVC-009` 之既定寫法。

## pre_conditions

```
1. The HU is in Standby state
2. PROXI Rear_View_Camera = 1 (Present)
3. The camera delay setting is set to "On"
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM2.CmdIgnSts = 4 (RUN)
2. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
3. Send CAN: STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted)
4. Read the HU display and check that the rear view camera image is still displayed
```

## expected_result

```
1. STATUS_BH_BCM2.CmdIgnSts = 4 (RUN) is sent and the HU completes start-up
2. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent and the rear view camera image is displayed
3. STATUS_CCAN4.ReverseGearSts = 0 (Not_Inserted) is sent
4. The rear view camera image is still displayed
```
