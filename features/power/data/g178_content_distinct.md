# G178 —— 四欄逐字全同之偵測（R-P257）

> 判準：`pre_conditions` / `input_test_data` / `test_procedure` /
> `expected_result` **四欄逐字全同**（不正規化空白）。
> **與 G168 之 C5 互補**：C5 為「`delta` 同而內文異」（文件缺陷）；
> 本閘為「內文同而 `tc_title` 異」（**事實缺陷** —— 二條實測同一件事）。
> 掃描範圍為**全批**，不限同一 leaf。

## 一、實測（264 條）

| 項 | 組數 |
|---|---|
| 內文全同而 `tc_title` **相異** | **9** |
| 內文全同且 `tc_title` 亦同（真重複） | **6** |

## 二、逐組

| TC | 同 leaf | `tc_title` |
|---|---|---|
| `…-087`、`…-091` | 是 | Accepting the CLIMATIC_PANEL.Radio_Btn0 popup passes the TLM to Standby<br>Accepting the Front_Panel_OnOff.Req popup passes the TLM to Standby |
| `…-088`、`…-092` | 是 | Declining the CLIMATIC_PANEL.Radio_Btn0 popup keeps the TLM in Timed<br>Declining the Front_Panel_OnOff.Req popup keeps the TLM in Timed |
| `…-100`、`…-104` | **否** | Antitheft success clears the activation request<br>Antitheft success clears the activation request on this variant |
| `…-101`、`…-105` | **否** | Antitheft success with a zero timeout takes Timeout1 from PROXI<br>Timeout1 follows Switch_Off_Time when the setting is zero |
| `…-102`、`…-107` | **否** | Antitheft success on this variant passes the TLM to Timed<br>Antitheft success passes the TLM to Timed state |
| `…-152`、`…-196` | **否** | No audio brand without SDARS shows the vehicle brand logo only |
| `…-153`、`…-197` | **否** | Beats brand white without SDARS adds the Beats logo |
| `…-154`、`…-198` | **否** | SDARS present without audio brand adds the Sirius logo |
| `…-155`、`…-199` | **否** | SDARS present with beats brand white adds both logos |
| `…-156`、`…-200` | **否** | The special package drives the Klipsch Splash Screen on the 2025 model year |
| `…-157`、`…-201` | **否** | The splash screen type drives the Klipsch Splash Screen after the 2025 model year |
| `…-165`、`…-229` | **否** | An incoming call from IDLE bypasses the disclaimer screen<br>An incoming call from IDLE bypasses the not yet shown disclaimer screen |
| `…-168`、`…-230` | **否** | The bypassed disclaimer is shown at the next transition to FULL OPERATION<br>The disclaimer bypassed for a call is shown at the next FULL OPERATION |
| `…-235`、`…-250` | **否** | The theme special package value is sent on this chapter while the network is awake<br>The theme special package value is sent while the CAN network is awake |
| `…-236`、`…-251` | **否** | A theme change on this chapter updates the sent value within the send window<br>A theme change updates the sent value within the send window |
