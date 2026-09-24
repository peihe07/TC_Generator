# NR1L-RVC-246 — SWE-CAM-007

- **Test Group**：Rear View Camera｜**Test Set**：LVDS Messaging
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V42_P637MCA_VF_2271`（來源列 `SYS-RA-VF551_V42-210`）

## test_item 上半（verbatim，SYS2 逐字）

> LTM shall scale the image received by RVCM over LVDS, according to the PROXI parameter Radio_Display_Type.

## reasoning

**R-CAM19 追溯補齊**（CAM-26 §2）：`SWE-CAM-007`（NCD HAL，題名 `Other LVDS / General Protocol`）之唯一來源 `SYS-RA-VF551_V42-210` 與 `SWE-CAM-006` 共引 —— **同源 SWE-CAM-006**（其 TC 為 `NR1L-RVC-200`）。依 **R-CAM19(b)**，驗證角度取本列 037 Description（`NCD HAL shall process Other LVDS / General Protocol via LVDS.`）：NCD HAL 為 LVDS 之接收側，故本列驗來源首句之「`the image received by RVCM over LVDS`」之**接收** —— 以 bus analyzer 觀察 RVCM 之影像確經 LVDS 送達 HU 並顯示；`-200` 驗其後之**縮放**（依 `Radio_Display_Type`），本列不判解析度與縮放。下放包所指之「LVDS 握手序列」於來源無載（掃描字串 `handshake` 於六本 SYS2 各 0 命中，A-CA38），**不造握手步驟**；037 `Verification Method` 欄所列之 SNA／6 cycles 逾時亦非本列來源所載（§8.4.1），不入。verbatim 取來源首句（保序子序列之前段）。LVDS 之觀察依 profile §7.3 以散文書寫、前置 bus analyzer（沿 `-209`）；觸發句沿 `-200`。車型只勾 637（V42 之錨 `P637MCA`，R-CAM11／R-CAM15(c)，同 `-200`）。實機可觀察性記入 `bench_verify.md`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. A bus analyzer is connected to the LVDS link between the HU and the RVCM
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_CCAN4.ReverseGearSts = 1 (Inserted)
2. Read the bus analyzer recording and check that the RVCM video is received by the HU over the LVDS link
3. Read the HU display and check that the rear view camera image is displayed
```

## expected_result

```
1. STATUS_CCAN4.ReverseGearSts = 1 (Inserted) is sent
2. The image from the RVCM is received by the HU over the LVDS link
3. The rear view camera image received over LVDS is displayed
```
