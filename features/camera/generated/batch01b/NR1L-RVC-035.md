# NR1L-RVC-035 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Auxiliary Cameras
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781632`（來源列 `SYS-RA-CAM-067`）

## test_item 上半（verbatim，SYS2 逐字）

> The Cargo/CHMSL Camera Softkey button shall enable displaying the Cargo/CHMSL camera image. The softkey button shall perform similar to the other buttons within the same touch screen (i.e. press time to actuation, color change when pressed, size of button).

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-067`（ObjectID 4781632，Cargo/CHMSL Camera 節）之「軟鍵啟用 Cargo/CHMSL 影像，且其行為與同一觸控畫面之其他按鍵一致」。ER2 只取原句三項舉例中**讀取當下可判**之一項（按下時之顏色變化）；press time to actuation 與 size of button 需量測治具，屬 HMI L&F 之量測項，不在本列（§6 可判性）。Controls screen 之導航 hop 於 B 本 SYS1 HeadUnitCameraSystems 匯出與 `forms/HMI Settings List` 皆查無（A-CA24／DR-CAM-g，與 batch01 未生成之 `SYS-RA-CAM-076` 同因）；R-CAM13(a)「不得略過」優先於該缺件，故本列生成，hop 與其 ER 標 `PENDING: DR-CAM-g`（A-CA32）。本列依 **R-CAM13(c)** 落 Test Set `Auxiliary Cameras`（framework Part VIII 第 10 組，CAM-06 重開）；其 SWE 列 `SWE-CAM-016` 於 Layer 2 仍歸 `Display Arbitration`，「組 ↔ SWE 列」與「TC ↔ Test Set」於本組分離。A-CA28 之「不生成」處置作廢。三個 PROXI 參數之平台覆蓋為 `forms/proxi/` 六本之逐格實測：`Digital_CHMSL_Camera_Prsnt`（byte 222 bit 7）只存在於 Atl-Hi 兩本；`Surround_View_Camera`／`Forward_Facing_Camera`（byte 177 bit 0／1）存在於 Atl-Hi 兩本與 637（`Promaster_ATL_MI` row 762／763）、376（`Fastback_ATL_MI` row 760／761）；**2261（`Toro_ATL_MI`）之 PROXI 表止於 byte 172，三者皆查無**，故該平台一律勾 0。六本之 default 值皆為 `0 = Absent`（R-CAM13(c) 所令之註）。

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
3. Read the HU display and check that the Cargo/CHMSL camera image is displayed
```

## expected_result

```
1. PENDING: DR-CAM-g the Controls screen is displayed
2. The Cargo/CHMSL Camera Softkey button changes colour while it is pressed, in the same way as the other buttons on the same touch screen
3. The Cargo/CHMSL camera image is displayed on the HU display
```
