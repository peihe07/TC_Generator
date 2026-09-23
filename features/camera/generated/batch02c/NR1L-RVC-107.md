# NR1L-RVC-107 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V2_PHDCC27_VF_526`（來源列 `SYS-RA-VF551_V2-535`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall implement the soft key button controls for RVC activation, refer to VF664 and HMI logic and flow.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-535` 之「HU 實作 RVC 啟用之軟鍵控制，依 VF664 與 HMI logic and flow」。依 **R-CAM13(b)** 生成 —— 該條文為 037 所引，不受 §8.4.2 之「不測外部規格」所擋。**VF664 於 `sources/` 與 `forms/` 皆查無**（DR-CAM-k），其具體判準無來源，ER 因而標 `PENDING: DR-CAM-k`；軟鍵之存在與可讀性仍可執行，不整列 BLOCKED。軟鍵之其他面向已分工：可用態之閘 → `-106`／`-023`／`-024`；配備之啟用 → `-025`；切換時間 → `-103`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. PENDING: DR-CAM-k VF664 is not present in sources or forms
4. The shift lever is in P
5. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Read the "Rear View Camera" soft key control in the App Drawer and check it against VF664
```

## expected_result

```
1. The App Drawer is displayed
2. PENDING: DR-CAM-k the soft key button control is as defined in VF664 and in the HMI logic and flow
```
