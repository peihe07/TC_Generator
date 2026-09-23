# NR1L-RVC-162 — SWE-CAM-011

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1158`（來源列 `SYS-RA-VF551_V2-483`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall never send vehicleUpdate_2.ZoomViewReq = SNA to RVCM.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-483` 之「HU 永不送 `vehicleUpdate_2.ZoomViewReq = SNA` 給 RVCM」。**negative 之可判化**：走過會使 `ZoomViewReq` 改值之兩個情境（按下 Zoom、離開相機畫面）後以整段錄製檢查 SNA 未出現（§6），寫法同 `NR1L-RVC-120`。`SYS-RA-VF551_V3-271` 與本列逐字同句（Atl-Mi 本），依同義列不另出 TC，plan 記 covered_by；本列因而亦涵蓋其行為，惟 **Vehicle Model 只勾 Atl-Hi** —— `ZoomViewReq` 之值語意（`Pressed`／`Not_Pressed`／`Default`）於 Atl-Mi 側另有 `-079`／`-134`／`-135` 承接。LVDS 訊號無 DBC（四本零命中），其值以來源 label 逐字書寫、觀察以 bus analyzer 進行，**不造命令**（profile §7.2／§7.3）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera image is displayed
4. A bus analyzer is connected to the LVDS link between the HU and the RVCM
```

## input_test_data

`NA`

## test_procedure

```
1. Press the Zoom Button on the HU display
2. Press the "X" exit button on the top right corner of the HU display
3. Read the whole recording of vehicleUpdate_2.ZoomViewReq and check that SNA never appears
```

## expected_result

```
1. The Zoom Button registers the press
2. The rear view camera image is closed
3. vehicleUpdate_2.ZoomViewReq is never sent as SNA in the whole recording
```
