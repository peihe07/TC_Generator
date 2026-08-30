# 66 包 §H 第 4 步 —— 「執行層查」逐項結果

> 判準：R-P368 三段鏈；PROXI 走 (c)；HMI 設定條目走 R-P375(b)。
> **命中即候選，非認定**（R-P375(d)）；查無者記「未解得」，**不記查無**（R-G13 / R-P368(d)）。

## 1. PROXI `Format` 參數（R-P368(c)）

| 參數名 | `Format` 列 | 結果 |
|---|---|---|
| `Brand_Configuration_2` | r566 | **查得** |
| `SDARS_Presence` | r542 | **查得** |
| `Audio_Brand` | r597 | **查得** |
| `VC_VEH_BRAND` | — | **未解得**（`Format` 之 `Parameter Name` 無此名） |
| `VC_VEH_LINE` | — | **未解得**（`Format` 之 `Parameter Name` 無此名） |
| `VC_SpecialPKG` | — | **未解得**（`Format` 之 `Parameter Name` 無此名） |
| `Car_Shape_Configuration` | r305 | **查得** |
| `Number_of_Doors` | r309 | **查得** |
| `Rear_View_Camera` | r401 | **查得** |
| `Switch_Off_Time` | r510 | **查得** |
| `Ecall_Button_Variant` | r871 | **查得** |
| `TBM_Present` | — | **未解得**（`Format` 之 `Parameter Name` 無此名） |
| `Country_Code` | r468 | **查得** |

## 2. 規格 `$X$` 之三段鏈（段 1 LID → 段 2 → 段 3 DBC）

| 規格名 | 段 1（LID 列）| 段 2（`MESSAGE.Signal`）| 段 3 | 結果 |
|---|---|---|---|---|
| `$Themed_Sound$` | — | — | — | **未解得（止於段 1）** |
| `$Door_Ajar_Status$` | r474 | — | — | **未解得（止於段 2）** |
| `$VC_BODY_STYLE$` | — | — | — | **未解得（止於段 1）** |
| `$Radio_Theme$` | r1531 | RADIO_B4.Radio_Theme | RADIO_B4.Radio_Theme | **解得** |
| `$ICSPowerButton$` | r1039 | CLIMATIC_PANEL.Radio_btn0、DIS_CENTERSTACK.DCSD_Power | CLIMATIC_PANEL.Radio_btn0、DIS_CENTERSTACK.DCSD_Power | **解得** |
| `$Telematic_Power$` | r2069 | TELEMATIC_FD_4.PowerSts_Telematic、STATUS_TELEMATIC.PowerSts_Telematic | TELEMATIC_FD_4.PowerSts_Telematic、STATUS_TELEMATIC.PowerSts_Telematic | **解得** |
| `$PowerMode$` | r1375 | STATUS_BH_BCM2.CmdIgnSts、BCM_FD_10.CmdIgnSts | STATUS_BH_BCM2.CmdIgnSts、BCM_FD_10.CmdIgnSts | **解得** |

## 3. HMI Settings List `Settings` 分頁

| 條目 | `Settings` 列 | 結果 |
|---|---|---|
| `Welcome Onboard Sound` | r41、r172 | **查得** |
| `Startup Animation Selection` | — | **未解得** |

## 4. DBC 訊息／訊號探查（§1 表所指者）

| 探查 | BHCAN2 命中 | FDCAN8 命中 |
|---|---|---|
| `DIS_CENTERSTACK` | `DIS_CENTERSTACK.DCSD_AC`、`DIS_CENTERSTACK.DCSD_Auto`、`DIS_CENTERSTACK.DCSD_DISP_STAT` | **0** |
| `Chime` | `GW_B_1.PAM_CHIME_TYPE`、`GW_B_3.PAM_CHIME_REP_RATESts`、`GW_B_5.Chime_Priority` | `ADAS_FD_HMI.Chime_Priority`、`ADAS_FD_HMI.Chime_RepRate`、`ADAS_FD_HMI.Chime_TypSts` |
| `Door_Ajar` | **0** | **0** |
| `DCSD` | `DIS_CENTERSTACK.DCSD_AC`、`DIS_CENTERSTACK.DCSD_Auto`、`DIS_CENTERSTACK.DCSD_DISP_STAT` | `DIAGNOSTIC_REQUEST_DCSD.N_PDU`、`DIAGNOSTIC_RESPONSE_DCSD.N_PDU` |

## 5. ⚠ §1 表所寫之四個 `PROXI <Param>` 在 PROXI `Format` 不存在

§1 表多處寫 `PROXI VC_VEH_BRAND`、`PROXI VC_VEH_LINE`、`PROXI VC_SpecialPKG`、
`PROXI TBM_Present`。實測：

| §1 表所寫 | PROXI `Format` | LID `Logical Identifier` | 近似名（**不採**）|
|---|---|---|---|
| `VC_VEH_BRAND` | **無** | **無** | `Brand_Configuration_2`(r566)、`Special_Brand_Configuration`(r472) |
| `VC_VEH_LINE` | **無** | **無** | `Vehicle_Line_Configuration`(r466) |
| `VC_SpecialPKG` | **無** | **無** | 無 |
| `TBM_Present` | **無** | **無** | 無（`TBM` 僅見於 ECU 清單欄）|
| `VC_BODY_STYLE` | **無** | **無** | 無 |
| `Themed_Sound` | **無** | **無** | 無 |

`VC_*` 為**規格側之 `$SIGNAL$` 名**（CFTS009 原文即以 `$VC_VEH_BRAND$` 書寫），
非 PROXI 參數名。§1 表以 `PROXI <Param>` 形式書寫者，其名須在 PROXI `Format`
查得列號（R-P375(b) / R-P368(c)），**本輪六名皆未查得**。

近似名（`Brand_Configuration_2` 對 `VC_VEH_BRAND`）**為語意跳接**：
除 `Brand` 一詞外無共同詞素，屬 R-P368(b) 所禁。
**本層不採、不代認定**（§8.4.1），依 R-P368(d) 記「未解得（止於段 1）」。

**影響**：品牌視覺類 12 名中，凡以 `PROXI VC_VEH_BRAND` / `VC_VEH_LINE` 為前置者
（`displayed font`、`displayed App icon`、`applied theme…`、`shown recirc icon`、
`shown gauges`、`shown seat graphic…`）之**前置條件寫法未定**。

三個可能處置（請裁）：
- 甲：依 **R-13** 保留規格原名不加 `$`（`VC_VEH_BRAND = <值>`），於 PROC 寫出應設定之值
- 乙：開 DR 請上游確認 `VC_VEH_BRAND` ≟ `Brand_Configuration_2` 等四對
- 丙：查 `SR26 Default Settings` / `SR24 Market Config` 之其他分頁（本輪未查）

## 6. 其餘未解得項

| 項 | 結果 | 處置 |
|---|---|---|
| `$Themed_Sound$` | 段 1 LID 無列、PROXI 無 | 未解得（止於段 1）；`audio output against the animation start` 之觸發未定 |
| `$Door_Ajar_Status$` | 段 1 LID **r474 有列**，惟 `Atlantis High` 欄空 | **未解得（止於段 2）** —— 與 M-1 / M-2 同型，惟本輪未達 R-G13（未確認該欄本應有值），不登 M-n |
| `$VC_BODY_STYLE$` | 段 1 無 | 未解得（止於段 1）|
| `Startup Animation Selection` | HMI `Settings` 無 | 與 §1 表一致 —— 該項為 **DID 診斷寫入**，非 HMI 設定；依 R-1 v3 (d) 保留來源名不加 `$` |
| chime 觸發訊號 | BHCAN2 有 `GW_B_1.PAM_CHIME_TYPE` / `GW_B_5.Chime_Priority` 等 | **查得候選**，惟「觸發一次 chime」對應哪一個未定 → 須分析層指定或開 DR |
| ICS 面板觸控座標 | BHCAN2 有 `DIS_CENTERSTACK.DCSD_AC` / `DCSD_Auto` / `DCSD_DISP_STAT` | **查得候選**；§1 表所稱之「觸控座標」無同名 `SG_`，最近者為 `DCSD_DISP_STAT`（顯示狀態）→ 須分析層指定 |
