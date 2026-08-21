# 下放包 10a：Power Management 整批回修（A 段，Pei 指示單本進行）

Pei 指示：**目前只處理 Power Management，其餘七本暫緩。**
`10_full_remediation.md` 之 B–H 段**全部凍結**，非本包範圍，
不得順帶開工。本包即該檔 A 段之單本展開。

前置：`09_r1v2_swc_baseline.md`（R-1 v2 + SWC 全案慣例）須先回寫
canon、重寫 lint P。基準本：**SWC 0708**。
基底：交付本 `…PowerManagement_20260821(Revise).xlsx` 之位元組副本。
新規 0 條。

## 六項作業

| 項 | 內容 | 量 | 依據 |
|---|---|---|---|
| A1 | **回改**批 1 之三件組 → `Send CAN: <MESSAGE>.<Signal> = <raw> (<label>)`；ER 側用 (b) 式 | 42 格 | R-1 v2(a)(b) |
| A2 | Input Test Data 內聯至 Procedure／PC，全欄改 `NA` | 158 列 | §4.5、SWC 285/286=NA |
| A3 | 消除步驟中 `listed in Input Test Data` 之指涉，步驟自足 | 同 A2 | SWC 步驟自足 |
| A4 | PROXI 改 `PROXI $X$ = "值"`（現 129 行無 `PROXI` 前綴） | 129 行 | R-1 v2(c) |
| A5 | spec_reference → `CFTS009/010-{ObjectID}` 首行、HMI 式次行 | 283 列 | R-2(a)、SWC 兩家族並列 |
| A6 | 賦值加 DBC `VAL_` 括號標籤 | 18 行 | R-7 |

### A1 對照（七種，逐字）

| 批 1 現況（撤銷之三件組） | 回改為 |
|---|---|
| `RemStActvSts in STATUS_BH_BCM2 on BH-CAN` | `STATUS_BH_BCM2.RemStActvSts` |
| `Batt_ST_Crit in STATUS_LIN on BH-CAN` | `STATUS_LIN.Batt_ST_Crit` |
| `DriverDoorSts in STATUS_BH_BCM1 on BH-CAN` | `STATUS_BH_BCM1.DriverDoorSts` |
| `PN14_LS_Actv in STATUS_LIN on BH-CAN` | `STATUS_LIN.PN14_LS_Actv` |
| `PN14_LS_Lvl7 in STATUS_LIN on BH-CAN` | `STATUS_LIN.PN14_LS_Lvl7` |
| `PsngrDoorSts in STATUS_BH_BCM1 on BH-CAN` | `STATUS_BH_BCM1.PsngrDoorSts` |
| `Radio_btn0 in CLIMATIC_PANEL on BH-CAN` | `CLIMATIC_PANEL.Radio_btn0` |

A-PM01 維持：訊號名以 DBC 為準（`Radio_btn0` 小寫），
CFTS009 原文之 `Radio_Btn0` 僅存於 verbatim 上半（R-6，不動）。

### A6 值標籤（DBC VAL_ 實查，逐字）

| signal | 0 | 1 |
|---|---|---|
| RemStActvSts | Remote Start Not Active | Remote Start Active |
| DriverDoorSts／PsngrDoorSts | Closed | Open |
| Batt_ST_Crit | False | True |
| PN14_LS_Actv／PN14_LS_Lvl7 | Not_Active | Active |
| Radio_btn0 | Not_Pressed | Pressed |

改寫例：
```
前：1. Drive Radio_btn0 in CLIMATIC_PANEL on BH-CAN from "Not_Pressed" to "Pressed"
後：1. Send CAN: CLIMATIC_PANEL.Radio_btn0 = 0 (Not_Pressed)
    2. Send CAN: CLIMATIC_PANEL.Radio_btn0 = 1 (Pressed)
```
（transition 型拆為兩步，比照 SWC `= 1 (PSD)` / `= 0 (NOT_PSD)` 之作法；
拆步後 ER 須同步增列，見驗收第 3 項）

### A5 ObjectID 來源

`features/power/` 既有之 `layer3_full.tsv`／`source_anchor` 對照
（037 `Source Requirement ID` 經 SYS2 解析之 7 位 item id）。
**逐列取值，不得由章節號反推**；查無者標 `PENDING: DR-{n}` 並登記 DR。

## 共通規則

1. 工作副本作業；`surgical_save` 唯一寫入路徑；交付本唯讀不覆寫。
2. 不得自行撰寫缺失內容 —— §8.4.3 三態。
3. 不得刪列、不得新增列。
4. verbatim 上半（test_item）不動（R-6／R-6b）。
5. A2 之多值列舉列（如 row 11 四種 ignition working condition）
   **不拆 TC**，步驟內明列全部值並標記待覆核。

## 驗收

- Input Test Data 非 `NA` 列 = **0**；步驟含 `listed in Input Test Data` = **0**
- spec_reference 首行匹配 `^CFTS0(09|10)-\d{7}$` = 283 減 PENDING 列數
- 賦值步驟全數為 R-1 v2(a) 式且帶 VAL_ 標籤；三件組殘留 = **0**
- PROXI 行帶 `PROXI` 前綴且 `$...$` 包覆 = 全數
- **Procedure ↔ ER 1:1 對齊維持**（A6 拆步後 ER 須同步）→ **E 必須為 0**
- 不得變動：A0 B0 C0 D0 F0 G0 H0 I0 I-sib0 J0 K0 L0 M0 N0
- 逐格 diff 僅 `spec`／`input`／`pre`／`proc`／`er` 五欄；`test_item` 零變動
- x14 下拉讀回；抽驗 12 列（7 訊號各 1、PROXI 3、多值列舉 2）

## 上繳

`docs/fw036/upstream/10a_pm_full.md`：六項各自改動清單、ObjectID 查無列、
待覆核列、新增 DR、lint 前後、diff 證明、
「本包是否仍有該驗而未驗者」獨立判斷、引用裁決編號清單。

**止於工作副本。** 寫回版次 `(Revise2)`，屬 Pei。
