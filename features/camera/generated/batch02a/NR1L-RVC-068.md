# NR1L-RVC-068 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V42_P637MCA_VF_2338`（來源列 `SYS-RA-VF551_V42-223`）

## test_item 上半（verbatim，SYS2 逐字）

> The user can select RVC_Swing_Doors_Check.Req value equal to "ON" or "OFF".

## reasoning

驗證目標為 `SYS-RA-VF551_V42-223` 之「使用者可將 `RVC_Swing_Doors_Check.Req` 選為 `"ON"` 或 `"OFF"`」。label 取 `HMI Settings List` `Settings` 分頁 **row 470** `Rear View Camera with Rear Door`（`F` 欄 `VF551`、`H` 欄 `Display Rear View camera while rear cargo…`）—— 其語意即後門／貨斗門開啟時之相機顯示，與 `RVC_Swing_Doors_Check.Req` 對應。該列**無 `*`**，不涉品牌軸；Pre-Condition 之品牌行仍書寫以與 `NR1L-RVC-067` 之同批設定操作一致。**此對應為執行層之判讀而非來源明載** —— `RVC_Swing_Doors_Check` 於 HMI Settings List 零命中，若審閱認為不足以推定，本列可退為 `PENDING`，於上繳包 §5 具名。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Set "Rear View Camera with Rear Door" = "On"
5. Set "Rear View Camera with Rear Door" = "Off"
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" settings screen is displayed
4. The "Rear View Camera with Rear Door" setting is set to "On"
5. The "Rear View Camera with Rear Door" setting is set to "Off"
```
