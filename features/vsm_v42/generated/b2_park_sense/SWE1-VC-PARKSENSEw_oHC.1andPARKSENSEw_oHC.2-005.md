# SWE1-VC-PARKSENSEw/oHC.1andPARKSENSEw/oHC.2-005

- Test Group: Vehicle Setup Management R1 Low
- Test Set: Park Sense
- TC 數: 1

**reasoning**：驗證 TLM 收到 $IPC_VEHICLE_SETUP.PamAlertMode$ 時，經內部訊號 TLM_Vehicle_Setup_Menu.Info 更新 Park Sense Alert Mode 之顯示。關鍵情境為 IPC 回報後之畫面更新（規格段 1211–1212）。本條驗兩個值之顯示（Sound 與 Sound_Display），其為同一機制之不同輸入，依 §8.2.2 不拆。TLM_Vehicle_Setup_Menu.Info 於 v3 為未解得(止於段1)，依 R-P355(c) 該步寫 PENDING，不得以 Set X.Info 假裝可執行；畫面更新以具名 UI 元件觀察（R-P353 白名單 (ii)）。

## TC 1 — Alert Mode display follows the IPC reported value

### test_item
```
The HMI layer shall evaluate the received IPC_VEHICLE_SETUP.PamAlertMode signal, update the TLM_Vehicle_Setup_Menu.Info internal signal, and display the Park Sense Alert Mode setting information accordingly within <TDisplay>
(Reported alert mode drives the displayed control in both values)
```

### pre_conditions
1. PROXI CAN node 24 (PAM) = 1 (Present)
2. The named UI element "Park Sense Setting" screen is displayed

### input_test_data
NA

### test_procedure
1. Send the signal $IPC_VEHICLE_SETUP.PamAlertMode$ = 1 (Sound)
2. Read the named UI element "PAM Alert Mode" control and check that it is "Sound"
3. Send the signal $IPC_VEHICLE_SETUP.PamAlertMode$ = 2 (Sound_Display)
4. Read the named UI element "PAM Alert Mode" control and check that it is "Sound+Display"
5. PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info

### expected_result
1. The signal $IPC_VEHICLE_SETUP.PamAlertMode$ = 1 (Sound) is registered without a bus error
2. The named UI element "PAM Alert Mode" control is "Sound"
3. The signal $IPC_VEHICLE_SETUP.PamAlertMode$ = 2 (Sound_Display) is registered without a bus error
4. The named UI element "PAM Alert Mode" control is "Sound+Display"
5. PENDING: DR-VL4 TLM_Vehicle_Setup_Menu.Info

### 其他
- specification_reference: Vehicle_Setup_Management_by_VP-LTM_R1_Low_VF665_V42_R6_1.11.1.1.29
- design_method: 狀態轉換 (State Transition Testing)
- priority: P2
- split_flag: False
- distinguishing_axis: trigger_state — 由 IPC 回報之 PamAlertMode 驅動顯示，與 -003／-004 之 HMI 送出方向相反
- remarks: UI element names are taken from the menu item wording named in the spec section and in the 037 description (R-VL21(a)); they are not anchored in HMI Settings List. TLM_Vehicle_Setup_Menu.Info is unresolved at stage 1 in signal_chain_v42_v3.tsv; observation method requested under DR-VL4
