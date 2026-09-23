# NR1L-RVC-039 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Auxiliary Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781654`（來源列 `SYS-RA-CAM-089`）

## test_item 上半（verbatim，SYS2 逐字）

> The Surround View Camera Softkey button shall be accessible from the Controls screen.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-089`（ObjectID 4781654，Surround View Camera 節）之「Surround View Camera Softkey 可自 Controls screen 取用」。Controls screen 之導航 hop 於 B 本 SYS1 HeadUnitCameraSystems 匯出與 `forms/HMI Settings List` 皆查無（A-CA24／DR-CAM-g，與 batch01 未生成之 `SYS-RA-CAM-076` 同因）；R-CAM13(a)「不得略過」優先於該缺件，故本列生成，hop 與其 ER 標 `PENDING: DR-CAM-g`（A-CA32）。本列與 `NR1L-RVC-037` 之分列：`-084` 驗 PROXI 配備對虛擬鍵之啟用、`-089` 驗該鍵於 Controls screen 之可取用，兩者為不同畫面之不同驗證點。本列依 **R-CAM13(c)** 落 Test Set `Auxiliary Cameras`（framework Part VIII 第 10 組，CAM-06 重開）；其 SWE 列 `SWE-CAM-016` 於 Layer 2 仍歸 `Display Arbitration`，「組 ↔ SWE 列」與「TC ↔ Test Set」於本組分離。A-CA28 之「不生成」處置作廢。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Surround_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. PENDING: DR-CAM-g open the Controls screen
2. Read the Controls screen and check that the Surround View Camera Softkey button is present and selectable
```

## expected_result

```
1. PENDING: DR-CAM-g the Controls screen is displayed
2. The Surround View Camera Softkey button is shown on the Controls screen and can be selected
```
