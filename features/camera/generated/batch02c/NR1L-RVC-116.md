# NR1L-RVC-116 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=0｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：功能測試 (Functional based ; no specific technique)
- **specification_reference**：`VF551_V4_PHDCC27_VF_1682`（來源列 `SYS-RA-VF551_V4-138`）

## test_item 上半（verbatim，SYS2 逐字）

> If the Head Unit Audio Mode is OFF, then the non-entertainment features shall be functional as per the Head Unit Audio Mode OFF behavior.

## reasoning

驗證目標為 `SYS-RA-VF551_V4-138` 之「Audio Mode OFF 時，the non-entertainment features 依 Audio Mode OFF 之行為運作」。**「依…之行為」為轉指**，其細目在 Audio 線之規格而非本 feature 之素材；依 §8.4.2 不展開該細目，ER 只驗「功能可用」與「相機影像不中斷」兩件可判之事 ——後者取自同節之 `b.` 子句語意（`-500`／`-506`／`-511`：不中斷相機影像），為本列之可判載體。與 `NR1L-RVC-100` 之分工：後者驗該模式下影像之**顯示**，本列驗該模式下其他功能之**可用與不干擾**。**只勾 HDCC27** —— V4 本之 anchor 前綴只有 `PHDCC27`（R-CAM11），RULINGS 平台表亦只將 V4 對應 `HDCC27 Atl-Hi`。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The HU is in Audio Mode OFF
4. The rear view camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Read the HU display and check that the non-entertainment features are functional
2. Read the HU display and check that the rear view camera image is not interrupted
```

## expected_result

```
1. The non-entertainment features are functional as per the Head Unit Audio Mode OFF behavior
2. The rear view camera image is not interrupted
```
