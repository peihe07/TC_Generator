# B3 —— `SWE-PM-025` 觸發訊號逐字原文（R-P179）

> 原文取自 CFTS 文字層（R-P17），**未經任何改寫**。
> **執行層不作判斷、不合併、不拆分**；裁定於 26 包。

## 1. 三對之觸發子句並列

### `4941569` vs `4941572`

**`4941569`** —— 觸發子句：

```
Front_Panel_OnOff.Req has a transition from “Not_Pressed” value to “Pressed” value
```

**`4941572`** —— 觸發子句：

```
CLIMATIC_PANEL.Radio_Btn0 has a transition from “Not_Pressed” value to “Pressed” value
```


### `4941570` vs `4941573`

**`4941570`** —— **本錨點不含觸發訊號名**，完整原文如下：

```
In this case, IF user accepts, TLM shall set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state.IF user does not accept, TLM shall stay in Timed state.
```

**`4941573`** —— **本錨點不含觸發訊號名**，完整原文如下：

```
In this case, IF user accepts, TLM shall set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state.IF user does not accept, TLM shall stay in Timed state.
```


### `4941571` vs `4941574`

**`4941571`** —— **本錨點不含觸發訊號名**，完整原文如下：

```
IF Phone_Call.Info == Not_ActiveTLM has to stop its active functionality (Media audio streaming, tuner, etc) and to set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state, in order to respond quickly to user requests, without requiring the activation of the network (if it was already not active).
```

**`4941574`** —— **本錨點不含觸發訊號名**，完整原文如下：

```
IF Phone_Call.Info == Not_ActiveTLM has to stop its active functionality (Media audio streaming, tuner, etc) and to set TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state, in order to respond quickly to user requests, without requiring the activation of the network (if it was already not active).
```


## 2. 二訊號名於 CFTS 文字層之出現處

| 訊號名 | 出現之錨點數 | 錨點 |
|---|---|---|
| `Front_Panel_OnOff.Req` | **13** | `4941454`、`4941540`、`4941542`、`4941552`、`4941569`、`4941578`、`4941583`、`4941639`、`4941699`、`4941757`、`4941762`、`4941802`、`4941807` |
| `CLIMATIC_PANEL.Radio_Btn0` | **10** | `4941541`、`4941543`、`4941555`、`4941572`、`4941584`、`4941590`、`4941661`、`4941758`、`4941803`、`4941808` |

## 3. 二訊號之共現情形（中性陳述，不作判斷）

同時含二訊號之錨點：**0**。

**證據方向須說明清楚，以免誤讀**：

- 若二者曾**於同一錨點內並列**（例如同一句列出二個觸發），即為「二個相異訊號」之**強證據**（(a)）。
- 二者**從未共現**，則**傾向 (b) 之弱證據** ——同一訊號之不同稱法本就不會被並列書寫。
- **惟「從未共現」亦與 (a) 相容**：二個相異訊號若分屬不同硬體來源，各自成段書寫亦屬常態。

**故本節之數字不足以獨立裁定，僅供 26 包參考。**

## 4. 二訊號各自出現之章節分布

| 訊號名 | 章節（去重）|
|---|---|
| `Front_Panel_OnOff.Req` | 1.6.2.1.15、1.6.7.1、? |
| `CLIMATIC_PANEL.Radio_Btn0` | 1.6.2.1.15、1.6.7.1、? |
