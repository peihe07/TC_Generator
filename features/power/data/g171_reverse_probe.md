# G171 —— 第 7 / 2 列之反向查（R-P244）

> 自**結構特徵**出發，不自詞彙出發。**本檔只出候選，判定屬人工。**

## 一、第 7 列（Combinatorial）候選 —— **9** 對

判準：同一 leaf 內存在二條 TC，其**二個以上**獨立參數同時取不同值。
單一參數變動而其餘固定者為決策表之逐列，不計。

| leaf | TC 對 | 同時相異之參數 |
|---|---|---|
| `SWE-PM-073` | `…-007` / `…-011` | `STATUS_LIN.PN14_LS_Actv`、`STATUS_LIN.PN14_LS_Lvl7` |
| `SWE-PM-073` | `…-011` / `…-012` | `STATUS_LIN.PN14_LS_Actv`、`STATUS_LIN.PN14_LS_Lvl7` |
| `SWE-PM-073` | `…-011` / `…-016` | `STATUS_LIN.PN14_LS_Actv`、`STATUS_LIN.PN14_LS_Lvl7` |
| `SWE-PM-038` | `…-038` / `…-040` | `Phone_Call.Info`、`Timeout1` |
| `SWE-PM-038` | `…-038` / `…-043` | `Phone_Call.Info`、`Timeout1` |
| `SWE-PM-038` | `…-039` / `…-040` | `Phone_Call.Info`、`Timeout1` |
| `SWE-PM-038` | `…-039` / `…-043` | `Phone_Call.Info`、`Timeout1` |
| `SWE-PM-014` | `…-064` / `…-065` | `Auto_SwitchOn_Setting.Req`、`Timeout1` |
| `SWE-PM-026` | `…-095` / `…-097` | `Brand_Configuration_2`、`PhoneCall.Info` |

## 二、第 2 列（Fault Injection）候選 —— **2** 條

判準：`test_procedure` 含「移除／中斷／停止某既有輸入」之動作。

| tc | leaf | 命中之結構 | 現值 `design_method` |
|---|---|---|---|
| `…-008` | `SWE-PM-073` | `Stop the broadcast of the two Load Shed signals on the bus` | 基礎故障注入 (Fault Injection Lite) |
| `…-011` | `SWE-PM-073` | `Stop the broadcast of the two Load Shed signals on the bus` | 決策表 (Decision Table Testing) |
