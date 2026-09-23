# NR1L-RVCHMI-023 — SWE1-RVC-008-06

- **Test Group**：Rear View Camera｜**Test Set**：Activation and Exit
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=1｜Fastack (376)=1
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`SYS1_HMI_RVC+PAM_R1_Low_SR24_1A_(June_25_2021)_7.2.6`（來源列 `NRL-142620`）

## test_item 上半（verbatim，SYS1 逐字）

> By pressing the «Camera» shortcut icon, in the Status bar Shortcut menu;

## reasoning

驗證目標為 §7.2 之第六款（cache 本 §7.2.6 逐字）。hop label 逐字取該列之 `«Camera» shortcut icon` 與 `Status bar Shortcut menu`。與 `-022`（§7.2.5，`«Controls» screen`）之分工：兩者為相異之手動入口。入口路徑（如何開啟狀態列捷徑選單）於 `spec-index/cache/` 之 Status Bar 本（99 列）與 Core HMI 本（169 列）掃描字串 `shortcut` 皆查無可用之逐字動作 → 沿 **DR-CAM-g**（該條由「Controls page 之入口」擴為「HMI 入口路徑之逐字來源」，見 DATA_REQUESTS）。依 CAM-14 審閱 §一-4 併入 B01a（不切開 §7.2 家族），B01a 由 22 列改 **23 列**。

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
1. PENDING: DR-CAM-g the entry path to the Status bar Shortcut menu is not sourced
2. Select the Camera shortcut icon in the Status bar Shortcut menu
3. Read the HU display and check that the RVC+PAM layout is displayed
```

## expected_result

```
1. PENDING: DR-CAM-g the Status bar Shortcut menu is displayed
2. The Camera shortcut icon registers the selection
3. The RVC+PAM layout is displayed
```
