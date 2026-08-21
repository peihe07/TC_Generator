# 16 包覆核裁決（2026-08-21）

判定：**通過**。253 列驗收全綠、lint A–N 全零、E=0、
test_item 內容變動 0（僅 163 格不可見字元正規化）、
spec_reference 變動 0、軌 C 30 列零變動、x14 與壓縮成員未變、
止於工作副本。PROC 步數 422→606 與拆步補值之預期相符。

## 一、row 17 —— **非偏離，追認**

附件 A row 17 之表下已明文載：

> ⚠ step 1 之現行寫法 `Send CAN: …` 係 R-1 v2 產物；依 R-1 v3
> 改為 `Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (…)`。
> 上表 PROC 1 已為 v2 式，**應改用 v3 式**，ER 1 已為 v3 式。

執行層之改寫即照此註記，屬**遵照指示**，非對「逐字可貼」之偏離。
分析層之疏失在於：既已知該處須改，仍將 v2 式留在可貼區塊內，
造成區塊與註記不一致。**責在分析層，處置正確。**

追認原則（適用後續各附件）：
```
附件之可貼區塊與其註記牴觸時，以註記為準；
分析層應確保區塊本身即為最終形態，不得倚賴註記補正。
```

## 二、DR-PW20 —— **確認**

rows 73／74／119／245 之原文僅載類別（`another value`／
`different from SNA`），依路線 (c) 標 `PENDING: DR-PW20` 正確。
**不得以「取任一符合類別之值」代替** —— 該類值之選定屬規格範圍，
非 TC 作者權限。

## 三、12 包 §二(d) 與附件 A 之衝突 —— **從附件 A，修訂 12 包**

```
R-1 v3(d) 修訂
內部訊號（X.Info／X.Req／X.GUI）於 DBC 查無對應者，
**保留來源名稱**（不加 `$`），並依 R-11(b) 於 PROC 寫出應設定
或應觀察之值。
理由：此類訊號多對應可執行之實體動作（Front_Panel_OnOff.Req =
前面板開關）或可讀之設定值（SwitchOff_Timeout_Setting.Req），
保留原名方能與規格逐條對應；強令改寫為「HMI 現象」將失去
追溯性，且該現象本身常無來源明載，反致造值。
原 §二(d)「不得留來源名」之表述作廢。
```

執行層以一致性為由從附件 A —— **判斷正確**。

## 四、lint P／Q／R 未改寫 —— **確認不動，排入改寫且限定範圍**

`scripts/lint036.py` 為八本共用，逕改將動及其餘七本基線 ——
此判斷正確，未動為是。`verify.py` 非共用閘之風險陳述亦成立。

裁定：lint 改寫**排入**，惟須以 **feature-scoped** 方式實作，
不得改動既有八本之現行基線：
```
lint036.py 新增 --profile <feature> 參數；P／Q／R 及 R-1 v3 相關
判準僅於指定 profile 下啟用。未指定時行為與現行完全一致
（以八本現行報告值為迴歸基準，逐項比對須全等）。
```
另立包處理，不併入 PM 內容批。

## 五、`PowerModeSts_Telematic` —— DBC 實測與裁定

DBC 實查（BH-CAN sha256 9ef1ec98…30d0）：**無此名稱**。
存在者為兩個**不同**訊號：

| 名稱 | message | 語意 |
|---|---|---|
| `PowerSts_Telematic` | `STATUS_TELEMATIC`（BH-CAN）／`TELEMATIC_FD_4`（FD-CAN8） | TLM 自身電源狀態（Sleep…Full_Operation） |
| `PowerModeSts` | `STATUS_BH_BCM1`（BH-CAN）／`BCM_FD_9`（FD-CAN8） | BCM 側車輛電源模式 |

`PowerModeSts_Telematic` 係二者名稱之混合，非 DBC 實有。

**裁定（Pei，2026-08-21）**：一律採 **`PowerSts_Telematic`**。
036 中出現之 `PowerModeSts_Telematic` 皆改寫為
`$STATUS_TELEMATIC.PowerSts_Telematic$`，VAL_：
0 Sleep／1 Standby／2 Timed／3 Idle／4 Full_Operation／
5 Logistic_On／6 Bench／7 Partial_Operation。
`PowerModeSts`（BCM 側）**不使用**。無須逐列判定，
執行層可全案改寫。

## 六、row 186 移除兩個非來源推定值 —— **確認**

主動移除無來源之推定值，符合 §8.4.1 與路線 (c)，予以確認。
此類移除若使該步驟失去判準，應標 `PENDING` 而非留空；
請於上繳確認該二處之現行狀態。

## 七、軌 C 現況

附件 G（軌 C 改寫）於 MCP 逾時中**未寫入**（已 `get_file_info`
確認不存在），故軌 C 之 30 列尚無改寫內容。
執行層「軌 C 零變動」為正確處置。分析層將重出附件 G／H。
