# CFTS020 節前定義塊 — 全面掃查（2026-08-29）

> 下放包 07 作業 B 之第二半，依 **R-ICS27(e)**。
> 本檔由 `scripts/predef_sweep_07.py` 產生；**表格非人工謄寫**。
> 操作型定義與五組型樣見該腳本檔頭。
> **候選非結論** —— 型樣命中只表示「像定義塊」，逐筆仍須人讀。

## §0 母數與命中

- CFTS020 物件總數 **2180**（屬性頭 `^\d{7}: \[`）
- 型樣命中之候選 **35** 個（1%）
- 其中 R-ICS2 v2 判**適用**者 **6** 個

型樣分佈（一物件可命中多型）：

- T1 宣告式引語：23
- T2 符號賦值：20
- T3 值域宣告：8
- T4 預設值：16

## §1 **適用**之候選（逐筆；本節為須人讀之清單）

| ObjectID | § | Artifact Type | 命中型樣 | 賦值符號 | 本文（前 160 字）|
|---|---|---|---|---|---|
| **4819351** | 1.4.3.1 | Subsystem Functional Requirement | T4 預設值 | — | If the CmdIgnStat signal is received with an implausible value (values of 1, 2 or 6) , the DCSD shall continue to behave using the last plausible value received |
| **4819541** | 1.8.1 | Subsystem Functional Requirement | T1 宣告式引語、T2 符號賦值、T4 預設值 | TPeriodToCountKnobDetents、TPeriodToSendNoChange、Tbutton、Tpower、Tpress、Tsend、Tstuck_button | For this section, the following time variables shall be used:<Tsend> = 150 msec<Tbutton> = 100 msec<TPeriodToCountKnobDetents> = initial value 50 msec. This is  |
| **4819580** | 1.8.1.2 | Subsystem Functional Requirement | T1 宣告式引語 | — | The ICS shall send the $ICS_KNOB<n>_DIR$ and $ICS_KNOB<n>_VAL$ signals to indicate the periodic and on-change status of any physical knob on the ICS. Within the |
| **4819626** | 1.8.2 | Subsystem Functional Requirement | T2 符號賦值 | TBackChnlSend、Tbutton、Tsend、Ttouch | The following variables shall be used in this section. <TBackChnlSend> = 20 msec <Tsend> = 150 msec            <Tbutton> = 100 msec <Ttouch> = 40 msec |
| **4819628** | 1.8.2.1 | Subsystem Functional Requirement | T3 值域宣告 | — | The DCSD shall send the $DCSD_DISP_STAT$ signal to indicate the periodic and on-change status of the display. Valid values for this signal follow below. All oth |
| **4821013** | 1.15.3 | Subsystem Functional Requirement | T3 值域宣告 | — | The DCSD shall send the $DCSD_DISP_STAT$ signal to indicate the periodic and on-change status of the display. Valid values for this signal follow below. All oth |

## §2 已錨定者（對照）

`CFTS020-4819541` 為 R-ICS27(a) 所錨之 §1.8.1 定義塊。本掃查是否命中它，是本工具有效性之自檢：

- `4819541` 是否命中：**是**
- 其命中型樣：T1 宣告式引語、T2 符號賦值、T4 預設值
- 其賦值符號：TPeriodToCountKnobDetents、TPeriodToSendNoChange、Tbutton、Tpower、Tpress、Tsend、Tstuck_button

## §3 不適用之候選（僅列數與 ObjectID，供回溯）

共 **29** 個：

```
4819367  4819368  4819394  4819455  4819456  4819625  4819741  4820155  4820172  4820200  4820243  4820244  4820246  4820371  4820389  4820390  4820407  4820460  4820461  4820463  4820739  4820740  4820742  4821099  4821100  4821102  4821377  4821378  4821380
```

## §4 全文之賦值符號總表（`<符號> =` 之相異識別字）

| 符號 | 出現於幾個物件 | 其中判適用者 |
|---|---|---|
| `<SwipeMinimumPixelsPerSecond>` | 1 | 0 |
| `<Swipe_Active_Distance_X>` | 8 | 0 |
| `<Swipe_Active_Distance_Y>` | 8 | 0 |
| `<Swipe_Minimum_Velocity_X>` | 8 | 0 |
| `<Swipe_Minimum_Velocity_Y>` | 8 | 0 |
| `<TBackChnlSend>` | 6 | 1 |
| `<TPeriodToCountKnobDetents>` | 4 | 1 |
| `<TPeriodToSendNoChange>` | 4 | 1 |
| `<Tbutton>` | 5 | 2 |
| `<Tpower>` | 4 | 1 |
| `<Tpress>` | 4 | 1 |
| `<Tsend>` | 11 | 2 |
| `<Tstuck_button>` | 4 | 1 |
| `<Ttouch>` | 7 | 1 |
