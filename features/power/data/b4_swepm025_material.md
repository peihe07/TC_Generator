# B4 —— `SWE-PM-025` 之八條拆法裁定素材（R-P167）

> **執行層未合併亦未拆分**（23 §I）。裁定於 24 包。

## 1. 二組錨點之逐字原文

### 組 A（`Front_Panel_OnOff.Req`）

**`4941569`**

```
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” valueTHENIF Phone_Call.Info == ActiveTHEN TLM shall show a popup to the user, asking whether to transfer the call in order to turn off TLM or not (refer to TLM HMI Specification)
```

**`4941570`**

```
In this case, IF user accepts, TLM shall set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state.IF user does not accept, TLM shall stay in Timed state.
```

**`4941571`**

```
IF Phone_Call.Info == Not_ActiveTLM has to stop its active functionality (Media audio streaming, tuner, etc) and to set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state, in order to respond quickly to user requests, without requiring the activation of the network (if it was already not active).
```

### 組 B（`CLIMATIC_PANEL.Radio_Btn0`）

**`4941572`**

```
IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND CLIMATIC_PANEL.Radio_Btn0 has a transition from “Not_Pressed” value to “Pressed” valueTHENIF Phone_Call.Info == ActiveTHEN TLM shall show a popup to the user, asking whether to transfer the call in order to turn off TLM or not (refer to TLM HMI Specification)
```

**`4941573`**

```
In this case, IF user accepts, TLM shall set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state.IF user does not accept, TLM shall stay in Timed state.
```

**`4941574`**

```
IF Phone_Call.Info == Not_ActiveTLM has to stop its active functionality (Media audio streaming, tuner, etc) and to set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state, in order to respond quickly to user requests, without requiring the activation of the network (if it was already not active).
```

## 2. 二組之全部屬性逐欄比對

### `4941569` vs `4941572` —— **相異：ECU**

| 屬性 | `4941569` | `4941572` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, RRM | LTM, RRM, ETM | **否** |
| EE Architecture | Atlantis High, Atlantis Mid | Atlantis Mid, Atlantis High | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

### `4941570` vs `4941573` —— **相異：ECU**

| 屬性 | `4941570` | `4941573` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | RRM, LTM | RRM, ETM, LTM | **否** |
| EE Architecture | Atlantis High, Atlantis Mid | Atlantis High, Atlantis Mid | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

### `4941571` vs `4941574` —— **相異：ECU**

| 屬性 | `4941571` | `4941574` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, RRM | ETM, RRM, LTM | **否** |
| EE Architecture | Atlantis Mid, Atlantis High | Atlantis Mid, Atlantis High | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

## 3. 八條之 `tc_title` / `split_reason` 對照

| tc_id | split_index | tc_title | split_reason |
|---|---|---|---|
| `083` | 1 | Front_Panel_OnOff.Req press in Timed with an active call shows a popup | 本條驗 Front_Panel_OnOff.Req ＋ 通話中之 popup |
| `084` | 2 | Accepting the Front_Panel_OnOff.Req popup passes the TLM to Standby | 本條驗 Front_Panel_OnOff.Req popup 之接受分支 |
| `085` | 3 | Declining the Front_Panel_OnOff.Req popup keeps the TLM in Timed | 本條驗 Front_Panel_OnOff.Req popup 之拒絕分支 |
| `086` | 4 | Front_Panel_OnOff.Req press in Timed with no active call passes to Standby | 本條驗 Front_Panel_OnOff.Req ＋ 無通話之直接轉換 |
| `087` | 5 | CLIMATIC_PANEL.Radio_Btn0 press in Timed with an active call shows a popup | 本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ 通話中之 popup |
| `088` | 6 | Accepting the CLIMATIC_PANEL.Radio_Btn0 popup passes the TLM to Standby | 本條驗 CLIMATIC_PANEL.Radio_Btn0 popup 之接受分支 |
| `089` | 7 | Declining the CLIMATIC_PANEL.Radio_Btn0 popup keeps the TLM in Timed | 本條驗 CLIMATIC_PANEL.Radio_Btn0 popup 之拒絕分支 |
| `090` | 8 | CLIMATIC_PANEL.Radio_Btn0 press in Timed with no active call passes to Standby | 本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ 無通話之直接轉換 |

## 4. 執行層之陳述（非建議）

二組錨點之內文**逐字比對結果**：`4941569` 與 `4941572` 之差異僅在觸發訊號名
（`Front_Panel_OnOff.Req` vs `CLIMATIC_PANEL.Radio_Btn0`），其餘一字不差；
`4941570` / `4941573` 與 `4941571` / `4941574` 亦然。

執行層當時之依據為 **§5.7「不同觸發即拆分」**，與 `SWE-PM-015` / `SWE-PM-019`
之處置一致（該二 leaf 之二鍵亦各自成條）。
**若本 leaf 裁為應合併，則 `SWE-PM-015`（4 條）與 `SWE-PM-019`（4 條）
之拆法同受影響** —— 三個 leaf 合計 16 條之其中 8 條將消失。

**執行層不就此提出建議**（R-P167 明訂裁定於 24 包）。
