# NR1L-RVC-036 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Additional Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781633`（來源列 `SYS-RA-CAM-068`）

## test_item 上半（verbatim，SYS2 逐字）

> When the user presses the Cargo/CHMSL Camera Softkey button, the HU shall receive the internal signal CHMC IMAGE ON and shall display the image of the truck cargo area of the vehicle.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-068`（ObjectID 4781633，Cargo/CHMSL Camera 節）之「按下軟鍵 → HU 收到內部訊號 CHMC IMAGE ON → 顯示貨斗區影像」。**內部訊號 `CHMC IMAGE ON` 不可觀察** —— `forms/` 四本 DBC 全文字面掃描 `CHMC` 零命中，其為 HU 內部事件而非匯流排訊號，依 §6 以其後果（貨斗區影像顯示）判定。本列與 `NR1L-RVC-035` 之分列依 §8.2.2「一個 sub-id 可需數個 TC，不得反向合併」——`-067` 驗軟鍵之啟用與按鍵行為、`-068` 驗影像來源正確（貨斗區），兩來源各有其驗證點。Controls screen 之導航 hop 於 B 本 SYS1 HeadUnitCameraSystems 匯出與 `forms/HMI Settings List` 皆查無（A-CA24／DR-CAM-g，與 batch01 未生成之 `SYS-RA-CAM-076` 同因）；R-CAM13(a)「不得略過」優先於該缺件，故本列生成，hop 與其 ER 標 `PENDING: DR-CAM-g`（A-CA32）。本列依 **R-CAM13(c)** 落 Test Set `Additional Cameras`（framework Part VIII 第 10 組，CAM-06 重開）；其 SWE 列 `SWE-CAM-016` 於 Layer 2 仍歸 `Display Arbitration`，「組 ↔ SWE 列」與「TC ↔ Test Set」於本組分離。A-CA28 之「不生成」處置作廢。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Digital_CHMSL_Camera_Prsnt = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. PENDING: DR-CAM-g open the Controls screen
2. Press the Cargo/CHMSL Camera Softkey button on the HU display
3. Read the HU display and check that the image shown is the image of the truck cargo area
```

## expected_result

```
1. PENDING: DR-CAM-g the Controls screen is displayed
2. The Cargo/CHMSL Camera Softkey button registers the press
3. The image of the truck cargo area of the vehicle is displayed on the HU display
```
