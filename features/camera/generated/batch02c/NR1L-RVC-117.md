# NR1L-RVC-117 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V42_P637MCA_VF_2359`（來源列 `SYS-RA-VF551_V42-255`）

## test_item 上半（verbatim，SYS2 逐字）

> IF the LTM receives: the signal LTM_OperationalModeSts.Info equal to "Ignition ON" or "Ignition_Start" or "Ignition_On_Prplsn_On" AND the signal RVC_Softbutton.Info equal to "Active" AND the internal variable is equal to "True" THEN LTM shall ignore the request.

## reasoning

驗證目標為 `SYS-RA-VF551_V42-255` 之「點火為 ON 系、`RVC_Softbutton.Info = "Active"` 且內部變數為 `"True"` 時，LTM 忽略該請求」—— 即**影像已顯示時重複按鍵不重入**。`RVC_Softbutton.Info` 與該內部變數皆**不在四本 DBC**（`RVC_Softbutton` 零命中），故以「影像已於手動模式顯示」之畫面態表達該兩前提（§6 以可判之等價態代之），不造訊號。`LTM_OperationalModeSts.Info` 為來源名，依 §8.7.5(f) 保留（三個 ON 系值取其一）。依 R-CAM15(c)，V42 列承 637。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. LTM_OperationalModeSts.Info = "Ignition ON"
4. The rear view camera image is displayed in Manual Display Mode
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Rear View Camera" in the App Drawer
3. Read the HU display and check the rear view camera image
```

## expected_result

```
1. The App Drawer is displayed
2. The rear view camera soft key control is activated a second time
3. The rear view camera image is unchanged and no transition occurs
```
