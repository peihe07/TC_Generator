# NR1L-RVC-247 — SWE-CAM-013

- **Test Group**：Rear View Camera｜**Test Set**：Diagnostics
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P1｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V42_P637MCA_VF_1996`（來源列 `SYS-RA-VF551_V42-593`）

## test_item 上半（verbatim，SYS2 逐字）

> Once the LTM receives the LVDS Video Signal, LTM shall: set the DTC to not present according to the "TLM Diagnostic Requirement" document.

## reasoning

**R-CAM19 追溯補齊**（CAM-26 §2）：`SWE-CAM-013`（NCD HAL，題名 `Message: diagnosticRequest / Response`）之三個來源皆由他列承接 —— `V42-592`／`-593` **同源 SWE-CAM-006**（TC `NR1L-RVC-211`／`-212`）、`V42-595` **同源 SWE-CAM-004**（TC `NR1L-RVC-195`）；下放包 §2 之「全委派 `-004`」與 `batch03_plan.tsv` 不合，更正記 A-CA38。依 **R-CAM19(b)**，驗證角度取本列 037 Description（`NCD HAL shall process Message: diagnosticRequest / Response via LVDS.`）：以 DTC 之讀取為觸發，觀察 LVDS 上之 `diagnosticRequest`／`diagnosticResponse`（兩訊息名逐字取 037 之題名與 Description）。錨取 `V42-593`（§1.13.2.1.2.0.4）—— 三來源中唯一使 LVDS 鏈路**正常**者（`-592` 為鏈路斷開，其間 LVDS 訊息無從觀察；`-595` 為 CAN 訊息逾時，與 LVDS 無涉）；ER 步 1 之「DTC not present」即該來源之結果。**兩訊息之欄位與值於來源無載** —— 掃描字串 `diagnosticRe`（不分大小寫）於六本 SYS2 各 0 命中 → `PENDING: DR-CAM-t`（本包新開），不造訊息內容。DTC 之讀取依 profile §7.3 以散文書寫；LVDS 之觀察前置 bus analyzer。車型只勾 637（V42）。實機可觀察性記入 `bench_verify.md`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. A bus analyzer is connected to the LVDS link between the HU and the RVCM
4. The LVDS Video Signal is received by the LTM
```

## input_test_data

`NA`

## test_procedure

```
1. Read the DTC list with the diagnostic tool and check the DTC state
2. Read the bus analyzer recording and check the diagnosticRequest message sent over LVDS to the RVCM
3. Read the bus analyzer recording and check the diagnosticResponse message returned over LVDS by the RVCM
```

## expected_result

```
1. The DTC for the missing LVDS video is not present
2. PENDING: DR-CAM-t the diagnosticRequest message is sent over LVDS to the RVCM; its fields and values are not sourced
3. PENDING: DR-CAM-t the diagnosticResponse message is returned over LVDS by the RVCM; its fields and values are not sourced
```
