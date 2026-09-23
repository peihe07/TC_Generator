# NR1L-RVC-100 — SWE-CAM-003

- **Test Group**：Rear View Camera｜**Test Set**：State Handling
- **Vehicle Model**：HDCC27=1｜DT27=1｜VF(ProMaster)637=0｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=0
- **priority**：P2｜**design_method**：決策表 (Decision Table Testing)
- **specification_reference**：`VF551_V2_PHDCC27_VF_1762`（來源列 `SYS-RA-VF551_V2-507`）

## test_item 上半（verbatim，SYS2 逐字）

> a. The head unit shall display the rear camera image display.

## reasoning

驗證目標為 `SYS-RA-VF551_V2-507` 之 `a.` 子句「HU 顯示後方相機影像」。**⚠ 章節歸屬為執行層之判讀，請審閱確認** —— V2 本之 `VF章節`(I) 欄於此區**落後一組**：`-499`～`-501` 標 `1.13.2.1.4` 而其節首句在 `-502`（標 `1.13.2.1.5`，Audio Mode ON 之轉入條件）；`-505`～`-507` 標 `1.13.2.1.6` 而其節首句為 `-505` 本身（Audio Mode OFF 之行為）。依此讀法，`-501` 屬 **Audio Mode ON** 之脈絡、`-507` 屬 **Audio Mode OFF**，兩者因而為不同前提之不同驗證點（否則兩句逐字近同而無從區分）。若審閱認定另一讀法，兩列可合為一列。同節之 `b.` 子句（不中斷影像）由 `-500`／`-506` 承接，其驗證點為「不中斷」，與本列之「顯示」不同，屬 `SWE-CAM-003` 之未列入驗證點 —— plan 已記其為同一節之他子句。**lint `J`（首字小寫）之豁免**：本列 test_item 上半為來源逐字，其首字本即小寫（來源之子句編號 `a.`／`c.`）；依 **profile §5.1**，§4.3.1 之逐字忠實優先於版面規則。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The HU is in Audio Mode OFF
4. No camera image is displayed
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: TRANSM_FD_4.ShiftLeverPosition = 2 (R)
2. Read the HU display and check that the rear camera image is displayed
```

## expected_result

```
1. TRANSM_FD_4.ShiftLeverPosition = 2 (R) is sent
2. The rear camera image is displayed
```
