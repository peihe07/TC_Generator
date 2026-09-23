# NR1L-RVC-095 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：Auxiliary Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781634`（來源列 `SYS-RA-CAM-069`）

## test_item 上半（verbatim，SYS2 逐字）

> When the user presses the X on the top right corner of the HU screen, the HU shall receive the internal signal CHMC IMAGE OFF and shall close the image of the truck cargo area of the vehicle.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-069`（ObjectID 4781634，Cargo/CHMSL 節）之「按 X → HU 收到內部訊號 CHMC IMAGE OFF → 關閉貨斗區影像」。**內部訊號不可觀察**（四本 DBC `CHMC` 零命中），依 §6 以影像關閉之後果判定 —— 寫法同 `NR1L-RVC-036`（`CHMC IMAGE ON`）與 `-047`（Rear 節之 `RVC IMAGE OFF`）。與 `-047` 之分工：兩者分屬不同相機節、不同來源、不同承接列（`-047` 歸 `SWE-CAM-001`）。本列來源屬 CFTS092 之 Cargo/CHMSL 或 Surround View 節，依 **R-CAM13(c)** 落 Test Set `Auxiliary Cameras`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
3. The shift lever is in P
4. The Cargo/CHMSL camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press the "X" exit button on the top right corner of the HU display
2. Read the HU display and check that the cargo area image is closed
```

## expected_result

```
1. The "X" exit button registers the press
2. The image of the truck cargo area is closed and the HU returns to the previous screen
```
