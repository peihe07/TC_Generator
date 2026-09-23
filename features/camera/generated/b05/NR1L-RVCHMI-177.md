# NR1L-RVCHMI-177 — SWE1-RVC-030

- **Test Group**：Rear View Camera｜**Test Set**：Warning Banners
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：負向測試 (Negative / Invalid)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_8.3.3`（來源列 `NRL-142637`）

## test_item 上半（verbatim，SYS1 逐字）

> RVC2.4) If the system technological constraints prevent the camera from displaying the “X” exit button on the camera image while in DRIVE, the camera delay option will not be supported

## reasoning

本列與 H 本 §6.1.2（`NR1L-RVCHMI-001`）**同旨而非逐字全等** —— 本列有 `RVC2.4)` 之編號前綴，H 本無（分群實測相異）。**兩者之來源本不同**（RVC+PAM vs HeadUnitCameraSystems），依 **R-CAM10** 各自出 TC；**R-CAM16(c) 不適用**（該款以「同組另一列」為要件，本對跨兩本且分屬 `Warning Banners`／`Activation and Exit` 兩組）。前提 3 為車輛配置事實，非可注入之訊號 → 記入 `bench_verify.md`（同 `-001`）。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera cannot display the "X" exit button on the camera image while in DRIVE
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Press "Apps" on Menu Bar to open App Drawer
2. Select "Settings" in the App Drawer
3. Select "Camera"
4. Read the "Camera" list and check that "Rear View Camera Delay" is not offered
```

## expected_result

```
1. The App Drawer is displayed
2. The "Settings" screen is displayed
3. The "Camera" list is displayed
4. "Rear View Camera Delay" is not present in the "Camera" list
```
