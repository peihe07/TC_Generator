# G178 —— 四欄逐字全同之偵測（R-P257）

> 判準：`pre_conditions` / `input_test_data` / `test_procedure` /
> `expected_result` **四欄逐字全同**（不正規化空白）。
> **與 G168 之 C5 互補**：C5 為「`delta` 同而內文異」（文件缺陷）；
> 本閘為「內文同而 `tc_title` 異」（**事實缺陷** —— 二條實測同一件事）。
> 掃描範圍為**全批**，不限同一 leaf。

## 一、實測（280 條）

| 項 | 組數 |
|---|---|
| 內文全同而 `tc_title` **相異** | **6** |
| 內文全同且 `tc_title` 亦同（真重複） | **6** |

## 二、逐組

| TC | 同 leaf | `tc_title` |
|---|---|---|
| `…-099`、`…-102` | **否** | Antitheft success clears the activation request<br>Antitheft success clears the activation request on this variant |
| `…-100`、`…-103` | **否** | Antitheft success with a zero timeout takes Timeout1 from PROXI<br>Timeout1 follows Switch_Off_Time when the setting is zero |
| `…-149`、`…-192` | **否** | No audio brand without SDARS shows the vehicle brand logo only |
| `…-150`、`…-193` | **否** | Beats brand white without SDARS adds the Beats logo |
| `…-151`、`…-194` | **否** | SDARS present without audio brand adds the Sirius logo |
| `…-152`、`…-195` | **否** | SDARS present with beats brand white adds both logos |
| `…-153`、`…-196` | **否** | The special package drives the Klipsch Splash Screen on the 2025 model year |
| `…-154`、`…-197` | **否** | The splash screen type drives the Klipsch Splash Screen after the 2025 model year |
| `…-162`、`…-225` | **否** | An incoming call from IDLE bypasses the disclaimer screen<br>An incoming call from IDLE bypasses the not yet shown disclaimer screen |
| `…-165`、`…-226` | **否** | The bypassed disclaimer is shown at the next transition to FULL OPERATION<br>The disclaimer bypassed for a call is shown at the next FULL OPERATION |
| `…-231`、`…-246` | **否** | The theme special package value is sent on this chapter while the network is awake<br>The theme special package value is sent while the CAN network is awake |
| `…-232`、`…-247` | **否** | A theme change on this chapter updates the sent value within the send window<br>A theme change updates the sent value within the send window |
