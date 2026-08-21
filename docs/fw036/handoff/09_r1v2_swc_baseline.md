# R-1 v2 修訂：訊號寫法一律以 SWC 0708 為準（Pei 裁定，2026-08-21）

Pei 裁定逐字：「都是照我 SWC 怎麼樣寫就這樣寫」。
基準本：`00_TestCase/SWC/…SWQT_SWC_20260708.xlsx`（286 列）。
**R-1 v1 之三件組（`Signal in MESSAGE on segment`）撤銷。**

## 一、撤銷紀錄（R-TM13：不刪除，加註保留）

~~R-1 v1：CAN 訊號斷言採三件組 `<Signal> in <MESSAGE> on <segment>`~~

> **撤銷（2026-08-21，Pei 裁定）**：v1 係分析層自「同一 signal 於
> BH-CAN 與 FD-CAN8 皆存在且 message 不同」推導網段必要性而立，
> **未先查證 Pei 既有測項之實際寫法**，違「引用任何單一來源為權威前，
> 先確認其涵蓋範圍」。實際上 SWC 以 `MESSAGE.Signal` 定位，message 名
> 本身即可判別網段（`BCM_FD_14` → FD-CAN），無須另書。
> 依 v1 已改動之 PM 42 格須回改，見 §四。

## 二、R-1 v2 條文（依 SWC 語料歸納，逐項有實例）

```
R-1 v2 訊號與參數寫法（基準：SWC 0708）

(a) CAN 訊號 —— Procedure：
    `Send CAN: <MESSAGE>.<Signal> = <raw> (<label>)`
    實例：`3. Send CAN: BCM_FD_14.Command_02Sts = 1 (PSD)`
    不寫網段、不加 `$`。<label> 逐字取自 DBC `VAL_` 列舉（R-7）。

(b) CAN 訊號 —— Expected Result：
    `<MESSAGE>.<Signal> = <raw> (<label>) is sent <時機>`
    實例：`3. BCM_FD_14.Command_02Sts = 1 (PSD) is sent during press window`

(c) PROXI 參數 —— Pre-Condition：
    `PROXI <Param> = <值>`，前綴 `PROXI` 必寫。
    參數名之 `$...$` 於 SWC 兩式並存（`PROXI $X$ = "V"` 與
    `PROXI X = V`），**採加 `$` 式**（Pei「訊號值要加上 $」之指示）：
    `PROXI $Audio_Steering_Wheel_Controls_on_IPC$ = "Enabled"`

(d) 內部訊號（`X.Info` / `X.Req` / `X.GUI`）：
    SWC 無先例。維持來源記法，不加 `$`，不套 (a) 之 CAN 格式。

(e) 保持／等待步驟：`Hold for <n> ms` 獨立成一步驟並於 ER 對應
    `The signal is held for <n> ms`。

(f) baseline 記錄：`Read <對象> and record as <Name>_initial` →
    `Read <對象> ... and record as <Name>_after` →
    `Check that <Name>_after <關係> <Name>_initial`。
    ER 對應 `<Name>_initial is recorded`。
```

## 三、SWC 其餘全案慣例（一併採為基準）

```
Pre-Condition 五段式（SWC 逐列一致）：
  1. Ignition state = ON and HU is in Full-Operation state
  2. PROXI <參數> = <值>
  3. HMI: "<設定項>" is selected for <位置>
  4. <來源／情境> is active on the HU
  5. CAN tool is available on HU
Input Test Data：一律 `NA`（SWC 285/286）
spec_reference：CFTS 家族在前、HMI 文件在後，一行一來源
  `CFTS042-4813401`⏎`Steering_Wheel_Controls_HMI_…_2022-Volume Down`
```

## 四、對已完成工作之影響

- **PM 批 1 之 42 格**（7 種 CAN 訊號改三件組）**須回改為 (a)/(b) 式**。
  例：`RemStActvSts in STATUS_BH_BCM2 on BH-CAN`
  → `Send CAN: STATUS_BH_BCM2.RemStActvSts = 1 (Remote Start Active)`
- **A-PM01 裁定維持**：步驟中之訊號名以 DBC 為準（`Radio_btn0` 小寫），
  即使 CFTS009 原文作 `Radio_Btn0`；verbatim 上半不動（R-6）。
- **lint P 檢查須重寫**：改為偵測「賦值步驟未採 (a) 式」與
  「值缺括號標籤」，原三件組判準作廢。
- **R-7 維持**：語意標籤取自 DBC `VAL_`，SWC 即此作法，二者一致。
- **R-6／R-6b 維持不變**。

## 五、程序檢討（§5a）

R-1 v1 之立，係分析層先自 DBC 推導理想格式、再回頭要求語料遵從，
方向顛倒。**格式類裁決應先窮舉 Pei 既有交付之實際寫法，
以語料為權威，分析層僅負責歸納與一致化。**
此原則追溯適用於 R-2、R-3、R-4 之後續檢視。
