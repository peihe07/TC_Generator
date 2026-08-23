# W-119 —— Part 1 之 open DR 對 VF230 leaf 之波及判定

**依 R-VS65 之掃描定義（62 包 §3）。**

- 掃描面：`data/vf230_leaves.tsv` 之 `title` ＋ `desc`（627 leaf）；`swe_id`／`src_ref`／`family` 不掃
- 大小寫不分；**以詞界為準，不作子字串命中**
- token 由各 DR 之提問正文機械取得（`$X$`／`A.B`／`` `X` `` 三式），
  去泛用詞後去重。**不自創 token。**

> **「命中 0」不是「不波及」之證明** —— 其僅證該 token 未出現於 leaf 之
> title/desc。概念型 DR（提問不繫於可掃之 token）一律標「待判」。

| DR | 判定 | 命中 leaf | token 數 | 示例 swe_id |
|---|---|---:|---:|---|
| **DR-8** | 不波及 | 0 | 1 | — |
| **DR-11** | 待判 | 0 | 0 | — |
| **DR-12** | 不波及 | 0 | 3 | — |
| **DR-14′** | 不波及 | 0 | 9 | — |
| **DR-15** | 不波及 | 0 | 25 | — |
| **DR-17** | 不波及 | 0 | 1 | — |
| **DR-18** | 不波及 | 0 | 8 | — |
| **DR-19** | 不波及 | 0 | 7 | — |
| **DR-20** | 不波及 | 0 | 1 | — |
| **DR-21** | 波及 | 7 | 25 | `SWE1-VC-ChargePowerLevel-044`／`SWE1-VC-ChargePowerLevel-045`／`SWE1-VC-ConsumptionUnit-032` |
| **DR-25** | 不波及 | 0 | 5 | — |
| **DR-26** | 不波及 | 0 | 3 | — |
| **DR-27** | 不波及 | 0 | 1 | — |

## 逐 DR 之 token 與命中

### DR-8 —— 不波及

自正文取得之 token（1）：

```
VC_VEH_LINE
```

**全部 token 命中 0。**

### DR-11 —— 待判

**本檔無其正文 —— `DATA_REQUESTS.md` 之「仍開啟」表以**表列編號**（5-A／5-B／7／8／9／10）記之，與內文之 DR-N 編號不同套。DR-11 僅於行 136 以交叉參照出現（`即 DR-11`），指向表列第 9 項（`HeatedSteeringWheel-009` 之 Source Requirement ID）。**其提問為單一 leaf 之 reqid 更正，非 token 型**，掃描無從施力。**

### DR-12 —— 不波及

自正文取得之 token（3）：

```
IGN_OFF_ACC  PowerMode  STATUS_BH_BCM2.CmdIgnSts
```

**全部 token 命中 0。**

### DR-14′ —— 不波及

自正文取得之 token（9）：

```
Driver_Headrest_Req  ESS_ENG_ST  HdRstRelRq  Passenger_Headrest_Req  PowerSideStep_Req  RADIO_B3  RADIO_B3.HDRstRelRq_3rdRow  RQ_DISP_INTS  VR_Blower_Req
```

**全部 token 命中 0。**

### DR-15 —— 不波及

自正文取得之 token（25）：

```
Driver_Headrest_Req  FL_HS_RQ  FL_HS_Tlm  FL_VS_RQ_TGW  FL_VS_Tlm  FR_HS_RQ  FR_HS_Tlm  FR_VS_RQ_TGW  HSW_Tlm  HdRstRelRq  HeatedSeatFR  Heated_Seat_Levels  PDT27_E2A_R4_BHCAN.dbc  Passenger_Headrest_Req  PowerSideStep_Req  R4_BHCAN  R5_FDCAN8  RADIO_B3  RADIO_B3.HDRstRelRq_3rdRow  RQ_DISP_INTS  TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm  TELEMATIC_VEHICLE_SETUP3  TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm  VAL_  VR_Blower_Req
```

**全部 token 命中 0。**

### DR-17 —— 不波及

自正文取得之 token（1）：

```
Heated_Seat_Levels
```

**全部 token 命中 0。**

### DR-18 —— 不波及

自正文取得之 token（8）：

```
CCDMF_FR_VS_RQ  FL_VS_Cmd_Tlm  HS_OFF  Heated_Seats_Levels  Heated_Steats_Levels  VS_OFF  VentedSeatFL  VentedSeatFR
```

**全部 token 命中 0。**

### DR-19 —— 不波及

自正文取得之 token（7）：

```
EngRun_Stat  Engine_On  IDLE_STBL  PDT27_E2A_R4_BHCAN.dbc  STATUS_CCAN3  STATUS_CCAN3.EngineSts  VAL_
```

**全部 token 命中 0。**

### DR-20 —— 不波及

自正文取得之 token（1）：

```
DriverSide
```

**全部 token 命中 0。**

### DR-21 —— 波及

自正文取得之 token（25）：

```
DSP_SK_PRSNT  ESS_ENG_ST  EngRun_Stat  FL_HS_Cmd_Tlm  FL_HS_RQ  FL_VS_Cmd_Tlm  FL_VS_RQ_TGW  FR_HS_Cmd_Tlm  FR_HS_RQ  FR_VS_Cmd_Tlm  FR_VS_RQ_TGW  HSW_Cmd_Tlm  HSW_RQ_TGW  HSW_Stat_2  Heated_Seat_Levels  Heated_Steats_Levels  Heated_Steering_Levels  Heated_Steering_Wheel  Hybrid_Type  IGN_OFF_ACC  IGN_START  PowerMode  STATUS_BH_BCM2.CmdIgnSts  VAL_  VC_VEH_LINE
```

命中之 token 與其 leaf 數：

- `Hybrid_Type` — 7

### DR-25 —— 不波及

自正文取得之 token（5）：

```
PDT27_E2A_R4_BHCAN.dbc  PDT27_E2A_R5_FDCAN8.dbc  TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm  TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm  TELEMATIC_VEHICLE_SETUP3
```

**全部 token 命中 0。**

### DR-26 —— 不波及

自正文取得之 token（3）：

```
IGN_RUN  PowerMode  RVC_button_ign_lk
```

**全部 token 命中 0。**

### DR-27 —— 不波及

自正文取得之 token（1）：

```
HSW_Stat
```

**全部 token 命中 0。**

## 小結

波及 **1** ／ 不波及 **11** ／ 待判 **1**

**未以任何 DR 為由阻塞 VF230 之 P1**（61 包 §4.6 之禁令）。

