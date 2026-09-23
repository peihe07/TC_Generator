# NR1L-RVC-046 — SWE-CAM-016

- **Test Group**：Rear View Camera｜**Test Set**：Display Arbitration
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`CFTS092-4781641`（來源列 `SYS-RA-CAM-076`）

## test_item 上半（verbatim，SYS2 逐字）

> The Rear Camera Softkey button shall be accessible from the Controls screen.

## reasoning

驗證目標為 CFTS092 `SYS-RA-CAM-076`（ObjectID 4781641，**Rear Camera 節**）之「Rear Camera Softkey 可自 Controls screen 取用」。**本列原為不生成**（CAM-05 §3.1，理由為 Controls screen 之 hop 無 HMI 來源，A-CA24／DR-CAM-g）；**CAM-06 審閱 §二-8 裁定比照 `-063`／`-089` 生成**（DECISIONS 6-17，A-CA32）——缺件不是略過來源之理由，hop 與其 ER 標 `PENDING: DR-CAM-g` 即可。**Test Set 為 `Display Arbitration` 而非 `Additional Cameras`** —— R-CAM13(c) 之判準是**來源列所屬之節**，`-076` 屬 Rear Camera 節（`-070`～`-082`），與 `-063`（Cargo/CHMSL）、`-089`（Surround View）不同節；本列因而歸 `SWE-CAM-016` 之原組。檔案落於 `batch01b/` 只是落檔批次之便，與 Test Set 無關（framework VIII.2 註之反向例）。Vehicle Model 五車型全勾 —— 前提只需 `PROXI Rear_View_Camera = 1 (Present)`，該參數六本 PROXI 皆有（byte 86 bit 0），與 Cargo/SVC/FFC 三列之平台受限情形不同。軟鍵之啟用側（`$RVC_SK_PRSNT$ = [Present]`）由 `NR1L-RVC-025` 承接、IGN_RUN 之閘由 `-023`／`-024` 承接，本列只驗其於 Controls screen 之可取用（§8.2.1 分工）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The shift lever is in P
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. PENDING: DR-CAM-g open the Controls screen
2. Read the Controls screen and check that the Rear Camera Softkey button is present and selectable
```

## expected_result

```
1. PENDING: DR-CAM-g the Controls screen is displayed
2. The Rear Camera Softkey button is shown on the Controls screen and can be selected
```
