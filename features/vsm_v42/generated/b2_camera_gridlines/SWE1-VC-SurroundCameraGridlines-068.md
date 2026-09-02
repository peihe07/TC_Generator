# SWE1-VC-SurroundCameraGridlines-068

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Camera Gridlines
- TC 數: 1

**reasoning**：驗證 TLM 收到 $IPC_VEHICLE_SETUP3.SVC_Guidelines$ 時，更新 Surround View Camera Gridlines 之顯示。關鍵情境為 IPC 回報後之畫面更新，本條驗兩個值（Off／On）之顯示，為同一機制之不同輸入，依 §8.2.2 不拆。該訊號 v3 解得（BO_1294／VAL_ 0 = Off、1 = On），label 逐字取 DBC。TLM_Vehicle_Setup_Menu.Info 為未解得(止於段1)，依 R-P355(c) 該步寫 PENDING，不得以 Set X.Info 假裝可執行。

## TC 1 — SVC Gridlines display follows the IPC reported value

### test_item
```
The HMI layer shall evaluate the received IPC_VEHICLE_SETUP3.SVC_Guidelines signal, update the TLM_Vehicle_Setup_Menu.Info` internal signal, and display the **Surround View Camera Gridlines** setting information accordingly within <TDisplay>
(Reported SVC gridlines value drives the displayed control in both states)
```

### pre_conditions
1. PROXI Surround_View_Camera = 1 (Present)
2. The named UI element "Surround View Camera (SVC) Gridlines" setting screen is displayed

### input_test_data
NA

### test_procedure
1. Send the signal $IPC_VEHICLE_SETUP3.SVC_Guidelines$ = 0 (Off)
2. Read the named UI element "Surround View Camera (SVC) Gridlines" control and check that it is "Off"
3. Send the signal $IPC_VEHICLE_SETUP3.SVC_Guidelines$ = 1 (On)
4. Read the named UI element "Surround View Camera (SVC) Gridlines" control and check that it is "On"
5. PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info

### expected_result
1. The signal $IPC_VEHICLE_SETUP3.SVC_Guidelines$ = 0 (Off) is registered without a bus error
2. The named UI element "Surround View Camera (SVC) Gridlines" control is "Off"
3. The signal $IPC_VEHICLE_SETUP3.SVC_Guidelines$ = 1 (On) is registered without a bus error
4. The named UI element "Surround View Camera (SVC) Gridlines" control is "On"
5. PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.38
- design_method: 狀態轉換 (State Transition Testing)
- priority: P2
- split_flag: False
- distinguishing_axis: trigger_state — 由 IPC 回報之 SVC_Guidelines 驅動顯示，與 -066／-067 之 HMI 送出方向相反
- remarks: UI element names are taken from the setting wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. TLM_Vehicle_Setup_Menu.Info is unresolved at stage 1 in signal_chain_v42_v3.tsv; observation method requested under DR-VL4
