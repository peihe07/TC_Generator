# W-VF14 —— R-VF13 之回溯掃描（**存查表；未觸發任何變更**）

**V06 §5.1 依 R-VF14 修訂本工單為存查性。**
本表**不含「應轉之新分級」之建議**，不改分級、不改 TC、不改條文。

其價值：日後若上游質疑某 leaf 之分級，可證本層知其存在且依 R-VF14 未改。

## 0. 量測條件

- 值域形態：VC/VM 欄內之 `SIGNAL = "值"` 或 `SIGNAL == "值"`
- **`not clear` 之列一律排除**（R-VF13 第 4 項）
- 現行分級取自 `docs/reports/writability.tsv`（Part 1）；VF230 尚無分級，一律記 `—`
- 「已交付」之三判準（W-VF16，**未裁**）並列，不擇一：

  | 判準 | 定義 | 集合大小 |
  |---|---|---:|
  | (a) | 已寫回交付路徑並 tag | **0** —— 036 之本 pipeline 產出欄全數 0 filled |
  | (b) | 已生成之批次（各批取最高版次） | 129 |
  | (c) | 已於 RD-1 送出之項次（Heated／Vented Seat） | 158 |

## 1. 存查表（14 列）

| feature | leaf | VC/VM 內之 (訊號, 值) | 現行分級 | blocker | DR | 已交付 (a)/(b)/(c) |
|---|---|---|---|---|---|---|
| CFTS044 | `SWE1-VC-HeatedSteeringWheelManagement-029` | `STATUS_CSWM.HSW_StatFailSts` = `Fail_Not_Present`／`TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm` = `ON` | W2 | B6-value-absent | DR-21 | 否／否／否 |
| CFTS044 | `SWE1-VC-HeatedSteeringWheelManagement-030` | `STATUS_CSWM.HSW_StatFailSts` = `Fail_Not_Present`／`TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm` = `OFF` | W2 | B6-value-absent | DR-21 | 否／否／否 |
| CFTS044 | `SWE1-VC-HeatedSteeringWheelManagement-031` | `STATUS_CSWM.FL_HS_STATFailSts` = `Fail_Present` | W0 | — | — | 否／是／否 |
| CFTS044 | `SWE1-VC-HeatedSteeringWheelManagement-033` | `TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm` = `ON` | W2 | B6-value-absent | DR-21 | 否／否／否 |
| CFTS044 | `SWE1-VC-HeatedSteeringWheelManagement-034` | `TELEMATIC_VEHICLE_SETUP.HSW_Cmd_Tlm` = `OFF` | W2 | B6-value-absent | DR-21 | 否／否／否 |
| VF230 | `SWE1-VC-AutoHighBeam-086` | `TELEMATIC_VEHICLE_SETUP.AutoHighBeamEnable_Req` = `Not_Enable to IPC within` | —（無分級紀錄） | — | — | 否／否／否 |
| VF230 | `SWE1-VC-AutoUnlockonExit-043` | `TELEMATIC_VEHICLE_SETUP.AutoUnlockDoorExit_Req` = `Enable and send it to IPC within` | —（無分級紀錄） | — | — | 否／否／否 |
| VF230 | `SWE1-VC-FlashLightWithLock-048` | `TELEMATIC_VEHICLE_SETUP.FlashLightWLock_Req` = `Off to IPC within` | —（無分級紀錄） | — | — | 否／否／否 |
| VF230 | `SWE1-VC-FlashLightWithLock-049` | `TELEMATIC_VEHICLE_SETUP.FlashLightWLock_Req` = `On to IPC within` | —（無分級紀錄） | — | — | 否／否／否 |
| VF230 | `SWE1-VC-NavigationTurnbyTurn-055` | `TELEMATIC_VEHICLE_SETUP.NavigationRepetition_Req` = `Off within` | —（無分級紀錄） | — | — | 否／否／否 |
| VF230 | `SWE1-VC-NavigationTurnbyTurn-056` | `TELEMATIC_VEHICLE_SETUP.NavigationRepetition_Req` = `On within` | —（無分級紀錄） | — | — | 否／否／否 |
| VF230 | `SWE1-VC-PassiveEntry-011` | `TELEMATIC_VEHICLE_SETUP.PassiveEntry_Req` = `Off` | —（無分級紀錄） | — | — | 否／否／否 |
| VF230 | `SWE1-VC-PhoneRepetition-066` | `TELEMATIC_VEHICLE_SETUP.PhoneRepetition_Req` = `Off to IPC within` | —（無分級紀錄） | — | — | 否／否／否 |
| VF230 | `SWE1-VC-PhoneRepetition-067` | `TELEMATIC_VEHICLE_SETUP.PhoneRepetition_Req` = `On to IPC within` | —（無分級紀錄） | — | — | 否／否／否 |

## 2. 小結（陳述事實，不作建議）

- 存查列合計 **14**
- 其中現行分級為 **W2** 者 **4**
- 其中**三判準皆判「未交付」**者 **13** ——
  **對此類，R-VF14 之排除效力於任一判準下皆不成立。**

**本層未依本表改動任何 leaf 之分級。**

現行 W2 且三判準皆未交付者：

- `SWE1-VC-HeatedSteeringWheelManagement-029`（CFTS044，blocker `B6-value-absent`）
- `SWE1-VC-HeatedSteeringWheelManagement-030`（CFTS044，blocker `B6-value-absent`）
- `SWE1-VC-HeatedSteeringWheelManagement-033`（CFTS044，blocker `B6-value-absent`）
- `SWE1-VC-HeatedSteeringWheelManagement-034`（CFTS044，blocker `B6-value-absent`）

