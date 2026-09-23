# NR1L-RVC-050 — SWE-CAM-001

- **Test Group**：Rear View Camera｜**Test Set**：Startup and Shutdown
- **Vehicle Model**：HDCC27=0｜DT27=0｜VF(ProMaster)637=1｜Commander (598)=0｜Regengade (5210)=0｜Toro(2261)=0｜Fastack (376)=1
- **priority**：P1｜**design_method**：狀態轉換 (State Transition Testing)
- **specification_reference**：`VF551_V3_P363_VF_505`（來源列 `SYS-RA-VF551_V3-252`）

## test_item 上半（verbatim，SYS2 逐字）

> · The Head Unit shall implement a warning text overlay that displays the text, "Camera Not in Position" for five seconds in the upper center of the display of the event followed by ''check entire surroundings'' per the HMI definition when STATUS_BH_BCM1.RHatchSts = [Open].

## reasoning

驗證目標同 `NR1L-RVC-049` 而為 Atl-Mi 之逐字條文 `SYS-RA-VF551_V3-252`。上半為摘句（§4.3.1）：原句 62 token 逾 50，刪末句 `This warning text shall be in accordance with ISO font 15008 and sized greater than 18 arc minutes.`（17 token），摘後 45 token；為原句之保序子序列，條件（`RHatchSts = [Open]`）與結果（疊加文字）兩子句皆保留。ISO 字型與字高之量測另由 `SWE-CAM-003` 之 `SYS-RA-VF551_V4-117` 承接（batch02c）。**車型勾選**：V3 之母體為 376（`P363` anchor，R-CAM11），惟 V42（637）無同義條文、V33（2261）另有 `-051`／`-052`，故本列承 **637 ＋ 376**；訊號實測 `STATUS_BH_BCM1`（`BO_ 854`）於 P363 與 637MCA 兩本 DBC 皆有，值域同 Atl-Hi。

## pre_conditions

```
1. The HU is in the Full-Operation state
2. PROXI Rear_View_Camera = 1 (Present)
3. The rear view camera image is displayed
4. STATUS_BH_BCM1.RHatchSts = 0 (Closed)
```

## input_test_data

`NA`

## test_procedure

```
1. Send CAN: STATUS_BH_BCM1.RHatchSts = 1 (Open)
2. Read the upper center part of the HU display within 5 s and check the warning text
3. Read the upper center part of the HU display after the first text is removed and check the following text
```

## expected_result

```
1. STATUS_BH_BCM1.RHatchSts = 1 (Open) is sent
2. The text "Camera Not in Position" is overlaid on the upper center part of the display
3. The text "check entire surroundings" is overlaid after the first text
```
