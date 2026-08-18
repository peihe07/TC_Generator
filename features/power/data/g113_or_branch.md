# G113 —— OR 分支涵蓋（R-P161）

> **不判 FAIL**：未覆蓋之分支入 R-P76 之待人工裁決類，逐支裁決三選一。
> 正規化限於分隔符層（黏連之 `OR` 補回空白、大小寫統一），**不擴及語義**。

## 批次 `batch_001_power_down`

### `SWE-PM-071` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | TLM has not to pass to Standby status | `pas`、`standby`、`tlm` | `pas` | **部分未覆蓋** |
| 1 | 2 | to Bench status | `bench` | — | 已覆蓋 |

### `SWE-PM-073` —— 分支 4

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | in BODY ON | — | — | 無獨有實詞 —— 不判 |
| 1 | 2 | BODY OFF-TIMED mode | `mode`、`off-tim` | — | 已覆蓋 |
| 2 | 1 | defined otherwise, TLM shall stay in this state until ei | `condition`、`defin`、`either`、`otherwise`、`range`、`satisfi` | `defin`、`either`、`otherwise`、`satisfi`、`thi` | **部分未覆蓋** |
| 2 | 2 | shall go back to normal behavior 10 seconds after STATUS | `after`、`back`、`behavior`、`go`、`normal`、`second` | `back`、`behavior`、`go`、`status_lin` | **部分未覆蓋** |

**合計分支 6，未覆蓋 **3**。**

## 批次 `batch_002_timeout_settings`

### `SWE-PM-057` —— 分支 28

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | Req to "00 min | `req` | `req` | **未覆蓋** |
| 1 | 2 | to "20 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 2 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 2 | 2 | 20 minutes" respectively | `minut`、`respectively` | `respectively` | **部分未覆蓋** |
| 3 | 1 | Req to "00 min | `req` | `req` | **未覆蓋** |
| 3 | 2 | to "60 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 4 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 4 | 2 | 60 minutes" respectively | `minut`、`respectively` | `respectively` | **部分未覆蓋** |
| 5 | 1 | Req to "00 min | `req` | `req` | **未覆蓋** |
| 5 | 2 | to "180 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 6 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 6 | 2 | 180 minutes" respectively | `minut`、`respectively` | `respectively` | **部分未覆蓋** |
| 7 | 1 | Req value equal to "00 minutes | `minut`、`req` | `req` | **部分未覆蓋** |
| 7 | 2 | equal to the value specified by PROXI parameter "Switch_ | `parameter`、`proxi`、`specifi`、`switch_off_time` | `specifi` | **部分未覆蓋** |
| 8 | 1 | Req to "00 minutes | `req` | `req` | **未覆蓋** |
| 8 | 2 | to "20 minutes | — | — | 無獨有實詞 —— 不判 |
| 9 | 1 | Req to "00 min | `req` | `req` | **未覆蓋** |
| 9 | 2 | to "20 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 10 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 10 | 2 | 20 minutes" respectively | `minut`、`respectively` | `respectively` | **部分未覆蓋** |
| 11 | 1 | Req to "00 min | `req` | `req` | **未覆蓋** |
| 11 | 2 | to "60 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 12 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 12 | 2 | 60 minutes" respectively | `minut`、`respectively` | `respectively` | **部分未覆蓋** |
| 13 | 1 | Req to "00 min | `req` | `req` | **未覆蓋** |
| 13 | 2 | to "180 min" in TLM menu | `menu`、`tlm` | — | 已覆蓋 |
| 14 | 1 | so Timeout1 is equal to "00 min | `equal`、`min`、`timeout1` | `equal` | **部分未覆蓋** |
| 14 | 2 | 180 minutes" respectively | `minut`、`respectively` | `respectively` | **部分未覆蓋** |

### `SWE-PM-063` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | to receive one | `one`、`receive` | `one` | **部分未覆蓋** |
| 1 | 2 | more bluetooth phone calls according to following logics | `accord`、`bluetooth`、`call`、`depend`、`follow`、`logic` | `accord`、`depend`、`follow`、`logic`、`more`、`timeout1` | **部分未覆蓋** |

### `SWE-PM-064` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | the Ignition working condition switches to "Ignition Pre | `condition`、`pre`、`switch`、`work` | — | 已覆蓋 |
| 1 | 2 | to "Ignition Off | — | — | 無獨有實詞 —— 不判 |

### `SWE-PM-065` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | TLM has to restore the active source managed by TLM befo | `active`、`before`、`call`、`dab`、`entertainment`、`example` | `entertainment`、`example`、`featur`、`like`、`rather`、`restore` | **部分未覆蓋** |
| 1 | 2 | BT streaming audio) staying still in Timed state | `audio`、`bt`、`state`、`stay`、`stream`、`tim` | `bt`、`stay`、`stream` | **部分未覆蓋** |

### `SWE-PM-038` —— 分支 12

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | ELSE TLM has to restore the active source managed by TLM | `active`、`before`、`call`、`dab`、`else`、`entertainment` | `else`、`entertainment`、`example`、`featur`、`like`、`rather` | **部分未覆蓋** |
| 1 | 2 | BT streaming audio) staying still in Timed state | `audio`、`bt`、`state`、`stay`、`stream`、`tim` | `bt` | **部分未覆蓋** |
| 2 | 1 | Info passes to "Not_Active | `info`、`not_active`、`pass` | `info` | **部分未覆蓋** |
| 2 | 2 | at maximum until MaxCallTimeout expiration | `expiration`、`maxcalltimeout`、`maximum` | `maximum` | **部分未覆蓋** |
| 3 | 1 | Info passes to "Not_Active | `info`、`not_active`、`pass` | `info` | **部分未覆蓋** |
| 3 | 2 | at MaxCallTimeout expiration, TLM sets TLM_Status | `expiration`、`maxcalltimeout`、`set`、`tlm`、`tlm_statu` | `tlm_statu` | **部分未覆蓋** |
| 4 | 1 | Info passes to "Not_Active | `info`、`not_active`、`pass` | `info` | **部分未覆蓋** |
| 4 | 2 | at MaxCallTimeout expiration, TLM has to set RemStartFai | `expiration`、`false`、`maxcalltimeout`、`remstartfail`、`set`、`tlm` | — | 已覆蓋 |
| 5 | 1 | the ignition working condition passes to "Ignition Pre O | `condition`、`pass`、`pre`、`work` | — | 已覆蓋 |
| 5 | 2 | to "Ignition Off"THENTLM has to pass in Timed state star | `counter`、`maxcalltimeout`、`pas`、`start`、`state`、`thentlm` | `pas`、`thentlm` | **部分未覆蓋** |
| 6 | 1 | Info passes to "Not_Active" value | `info`、`not_active`、`pass`、`value` | `info` | **部分未覆蓋** |
| 6 | 2 | at maximum until MaxCallTimeout expires | `expir`、`maxcalltimeout`、`maximum` | `maximum` | **部分未覆蓋** |

**合計分支 46，未覆蓋 **35**。**

## 批次 `batch_003_power_state_a`

### `SWE-PM-011` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | the CarPlay Device does not request audio control | `audio`、`carplay`、`device`、`doe`、`request` | `doe` | **部分未覆蓋** |
| 1 | 2 | video control | `video` | — | 已覆蓋 |

### `SWE-PM-014` —— 分支 10

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | Info is equal to "Ignition Pre Off | `equal`、`info`、`pre` | `equal`、`info` | **部分未覆蓋** |
| 1 | 2 | to "Ignition Off", TLM has to set RemStartFail = "True | `remstartfail`、`set`、`tlm`、`true` | — | 已覆蓋 |
| 2 | 1 | Info becomes equal to "Not_Active | `becom`、`equal`、`info`、`not_active` | `equal`、`info` | **部分未覆蓋** |
| 2 | 2 | at maximum until MaxCallTimeout expiration | `expiration`、`maxcalltimeout`、`maximum` | `expiration`、`maxcalltimeout`、`maximum` | **未覆蓋** |
| 3 | 1 | Info is not equal to "Ignition Pre Off | `equal`、`info`、`pre` | `equal`、`info` | **部分未覆蓋** |
| 3 | 2 | to "Ignition Off | — | — | 無獨有實詞 —— 不判 |
| 4 | 1 | Info has a transition to "Ignition Pre Off | `info`、`pre`、`transition` | `info` | **部分未覆蓋** |
| 4 | 2 | to "Ignition Off" valueAND STATUS_BH_BCM2 | `status_bh_bcm2`、`valueand` | `status_bh_bcm2`、`valueand` | **未覆蓋** |
| 5 | 1 | Info becomes equal to "Not_Active | `becom`、`equal`、`info`、`not_active` | `equal`、`info` | **部分未覆蓋** |
| 5 | 2 | at maximum until MaxCallTimeout expiration | `expiration`、`maxcalltimeout`、`maximum` | `expiration`、`maxcalltimeout`、`maximum` | **未覆蓋** |

### `SWE-PM-018` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | signal LTM_OperationalModeSts has a transition to "Ignit | `ltm_operationalmodest`、`pre`、`signal`、`transition` | `signal` | **部分未覆蓋** |
| 1 | 2 | to "Ignition Off" valueTHENTLM has to set TLM_Status | `set`、`tlm_statu`、`valuethentlm` | `set`、`tlm_statu`、`valuethentlm` | **未覆蓋** |

### `SWE-PM-025` —— 分支 4

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | Info == ActiveTHEN TLM shall show a popup to the user, a | `activethen`、`ask`、`call`、`info`、`off`、`order` | `activethen`、`info`、`off`、`order`、`turn` | **部分未覆蓋** |
| 1 | 2 | not (refer to TLM HMI Specification | `hmi`、`refer`、`specification` | `hmi`、`refer`、`specification` | **未覆蓋** |
| 2 | 1 | Info == ActiveTHEN TLM shall show a popup to the user, a | `activethen`、`ask`、`call`、`info`、`off`、`order` | `activethen`、`info`、`off`、`order`、`turn` | **部分未覆蓋** |
| 2 | 2 | not (refer to TLM HMI Specification | `hmi`、`refer`、`specification` | `hmi`、`refer`、`specification` | **未覆蓋** |

### `SWE-PM-031` —— 分支 2

| 組 | 支 | 分支文字 | 獨有實詞 | 未見於任何 TC | 判定 |
|---|---|---|---|---|---|
| 1 | 1 | Info, TLM shall show | `info`、`show`、`tlm` | `info`、`show` | **部分未覆蓋** |
| 1 | 2 | not rear view camera images regardless of TLM_Status | `camera`、`imag`、`rear`、`regardles`、`tlm_statu`、`view` | `tlm_statu` | **部分未覆蓋** |

**合計分支 20，未覆蓋 **17**。**
