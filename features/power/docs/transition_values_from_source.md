# 轉態目標值對照（自 CFTS 原文查證，2026-08-21）

Pei 裁定採路線 (c)：不由分析層依情境推定，一律回查 CFTS009／010
原文取值。本表為查證結果，供附件 A–D 修訂與後續各批引用。

## 一、完整 VAL_（DBC 實查，補全先前未列之值）

`OperationalModeSts`（`STATUS_BH_BCM1` on BH-CAN，
sha256 9ef1ec98…30d0）：
```
0 Initialization    1 Ignition_Off_WithoutKey  2 Ignition_Off
3 Ignition_Acc      4 Ignition_On             5 Ignition_Pre_Start
6 Ignition_Start    7 Ignition_Cranking       8 Ignition_On_EngOn
9 Ignition_Pre_Acc  10 Ignition_Pre_Off       11 Automatic_Cranking
12 Automatic_Stop   13 Key_Authenticated      14 Not_Used   15 SNA
```
**先前各附件僅列 0–8，遺漏 `10 Ignition_Pre_Off`** —— 該值為本次
查證之關鍵，見 §二。

## 二、CFTS009 原文（objects 4941466–4941469，逐字）

```
4941466  Behaviour 1: "RRM_OperationalModeSts.Info" is equal to
         "Ignition Pre Off" OR to "Ignition Off"
4941467  IF Phone_Call.Info == "Not Active", TLM has to set
         RemStartFail ="False" AND TLM_Status.Info and $Telematic_Power$
         to "Standby" value and it passes to TLM Standby state.
4941468  IF Phone_Call.Info == "Active", TLM has to set
         RemStartFail ="True" AND TLM_Status.Info and $Telematic_Power$
         to "Timed" value and it passes to TLM Timed state.
4941469  In this case, TLM has to stay in this state until
         Phone_Call.Info becomes equal to "Not_Active", OR at maximum
         until MaxCallTimeout expiration.
```

## 三、據此修訂先前之填值

**rows 49／50（附件 D）之修訂**：分析層原填
`Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off)`
並自註「依情境所定，非來源明載」。查證結果：

- 原文之轉態條件為 **`Ignition_Pre_Off` OR `Ignition_Off` 二者之一**，
  非單一值。填 `2 (Ignition_Off)` 屬**合法值之一**，非杜撰，
  但**未涵蓋 `10 (Ignition_Pre_Off)` 分支**。
- 依 §8.3（sibling 軸：不同 trigger 各為一 TC），二值應各為一列。
  現行 036 僅一列 → 覆蓋不足。
  **登記 A-PM09**：rows 49／50／52／53／54 各缺 `Ignition_Pre_Off`
  分支之對應 TC。拆列屬 Pei，本包不拆。
- 附件 D 之 rows 49／50 填值**維持 `2 (Ignition_Off)`**，
  自註改為：「原文為 Ignition_Pre_Off OR Ignition_Off 二選一，
  本列取 Ignition_Off；另一分支缺 TC，見 A-PM09」。

**row 48 之修訂**：原文 4941467／4941468 顯示
`RemStartFail` 之值與 `Phone_Call.Info` 同時被設定 ——
`Not Active → RemStartFail=False + Standby`；
`Active → RemStartFail=True + Timed`。
附件 D row 48 之 ER「RemStartFail is False」與原文一致，維持。

**row 47 之修訂**：原文之 `RemStartFail="True"` 係
`Phone_Call.Info == "Active"` 之結果（4941468），
而附件 D row 47 之 PRE 未載 Phone_Call.Info 狀態。
**補 PRE**：`Phone_Call.Info is Active`。

## 四、ECU 不一致（登記 A-PM10）

原文 4941466 之主體為 **`RRM_OperationalModeSts.Info`**（RRM），
036 各列則寫 `LTM_OperationalModeSts.Info`（LTM）。
CFTS009 該段 [ECU:RRM]、[Radio:noSys, VP1.5]，與 PM 之 Atlantis High
LTM 情境未必相符。**須確認 036 引用之來源是否為另一段 LTM 條文**，
或屬跨 ECU 誤植。查證前，各列之 `OperationalModeSts` 訊號名維持
`$STATUS_BH_BCM1.OperationalModeSts$`（DBC 實有），不因 ECU 疑義而改。

## 五、後續作業原則（路線 c 之執行方式）

46 列含未指明目標值之驅動步驟（實測，全 283 列掃描）：
`Bring the HU to …` 15／`Bring the TLM to the status …` 9／
`Let LTM_OperationalModeSts.Info transition occur` 5／
`Attempt an/a …` 6／`Let the TLM enter/exit/settle/evaluate` 6／
`Apply each …` 1 等。

逐列處置順序：
1. 於 CFTS009／010 以該列 test_item verbatim 之關鍵詞定位原文 object
2. 取原文明載之目標值；原文為多值擇一者，取其一並登記缺分支
3. 原文確無值者，標 `PENDING: DR-{n}`，**不得依情境推定**
4. 每列於附件中註明所據 object id，供覆核回溯
