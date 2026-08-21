# 10a 覆核裁決（2026-08-21）

判定：**通過**。三項語料反證全部成立且處置正確；兩項保留之理由
成立；lint P 重寫、台帳補登 R-6/R-6b/R-7 皆為應為而先前缺漏者。
「五段式為已知為假之全稱命題故不寫進 canon」—— 此判斷正確，
分析層之 09 包 §三為第三次全稱命題失誤（前二次見 04 §零、06 §一、§二）。

## 一、PROXI `$`：「兩參數族」不成立，但結論方向正確

實測 SWC 全書 PROXI 賦值行：

| 寫法 | 參數 | 次數 |
|---|---|---|
| 加 `$` | `Audio_Steering_Wheel_Controls_on_IPC` | 24 |
| 不加 | `RRM_VPx_Steering_Wheel_Command_Type` | 214 |
| 不加 | **`Audio_Steering_Wheel_Controls_on_IPC`** | 2 |

**同一參數兩種寫法並存**（24 加 / 2 不加），故非「開關型 vs 配置型」
之族別差異；SWC 樣本僅 2 種參數，其中 1 種自身不一致。
214:24 之比實為「一種參數重複出現 214 次」，非多數決材料。

**R-1 v2(c) 修訂**：

```
PROXI 參數名之 `$...$` 沿用其來源文件之記法：來源以 `$X$` 書寫者
加 `$`，否則不加。前綴 `PROXI` 一律必寫。
PM 之 22 種參數於 CFTS009 原文全數為 `$X$` 式（實測 76 種 $..$ token
含 $Telematic_Power$ 等），故 PM 全數加 `$`，符合 Pei 指示。
SWC 之 `RRM_VPx_Steering_Wheel_Command_Type` 依此不加 `$`，
既有 214 行**非違規**；`Audio_Steering_Wheel_Controls_on_IPC`
之 2 行不加者為漏網，屬 SWC 內部不一致，登記 A-SW01，不回修。
```

lint 不得以「PROXI 必加 $」為判準。

## 二、ER 側標籤：不強制

基準本 P=195（proc 缺 8 = 98.7% 合規；er 缺 184 = 70.8%）。
**基準本自身違規 195 筆，即判準嚴於語料。** 依 09 §五之原則
（語料為權威），裁定：

```
R-7 修訂：括號語意標籤於 Procedure 之賦值步驟**強制**；
於 Expected Result **選用**。ER 描述已送出之訊號時得僅書
`<MESSAGE>.<Signal> = <raw> is sent`。
lint P 之 ER 側標籤檢查降為 warning，不計入違規總數。
```
調整後基準本 P 應降為 8（proc 側），該 8 筆登記 A-SW02，不回修。

## 三、A5 保留：確認，並選定第三路

三選項中**採「全數保留現況 + 開 DR」**：
- 155/283 之 anchor 為 2–13 候選之最佳猜測（f1 低至 0.2），
  寫入即造值（§8.4.1），且把不確定性偽裝為精確錨點
- 標 PENDING 依 §8.4.3 阻斷交付，代價不成比例
- 僅改 125 列即 03 §四已認可之「同欄兩制較全不改更糟」

**開 DR-PW19**（High）：請上游提供 037 各 leaf 之權威 ObjectID 對照
（現行 `anchor_attribution_53.json` 僅 44% determined）。
M16-PM 於該 DR 結案前**不得執行**。

## 四、A2/A3 保留 101 列：確認，改由分析層處置

「交付物之步驟文字若不成句，比保留回指更糟」—— 成立。
101 列屬逐列改寫之內容判斷，非機械代入，**不再下放**。
分析層將以 `edits.json` 之 `log.held` 為工作單逐列改寫，
產出後以下放包交付執行層寫入。

## 五、test_item 之 10 處 v1 三件組：解除限制

R-6 與 10a 驗收之牴觸屬實。**下包解除「test_item 零變動」限制**，
範圍嚴格限定：僅改括號下半（M15 token）內之 v1 三件組 10 處，
**上半 verbatim 仍不得動**。

## 六、DELIVERY_NOTE 雜湊：註明為交付當時值

`f59de2e7…` → `3d14a092…` 之差係 Pei 開檔後 Excel 重新序列化
（+7,671 B），經逐項複驗內容零差異、x14 未損。
**不更新為新值**，改註記：
`sha256 f59de2e7…（交付當時值；其後經 Excel 重新序列化為
3d14a092…，六欄逐格內容零差異，x14 DV 1 未變）`
理由：ledger 為 append-only 之交付跡證，記錄交付當時狀態；
事後之工具性重寫不改寫歷史值。

## 七、A6 信任鏈閉合（分析層補證）

DBC 原始行與檔案雜湊，供獨立複驗：
```
sha256 9ef1ec9830fc8018b23d0e36dbd7ca6023b9b0a03124095726eb5583a01930d0  PDT27_E2A_R4_BHCAN.dbc
sha256 51c8fd6092925071bbf443711e5161d78df292de232dc7427b1cceaa8f181cd2  PDT27_E2A_R5_FDCAN8.dbc

VAL_ 1050 Radio_btn0 0 "Not_Pressed" 1 "Pressed";
VAL_ 854 DriverDoorSts 0 "Closed" 1 "Open";
VAL_ 854 PsngrDoorSts 0 "Closed" 1 "Open";
VAL_ 1132 RemStActvSts 0 "Remote Start Not Active" 1 "Remote Start Active";
VAL_ 1462 Batt_ST_Crit 0 "False" 1 "True";
VAL_ 1462 PN14_LS_Actv 0 "Not_Active" 1 "Active";
VAL_ 1462 PN14_LS_Lvl7 0 "Not_Active" 1 "Active";
```
七項與 10a §A6 表逐字相符。信任鏈閉合。
「未對原檔複驗即為未閉合之信任鏈」之自我判斷正確，應予保持。

## 八、PM 未結項

M16-PM（凍結，待 DR-PW19）、A2/A3 101 列（分析層改寫中）、
test_item 10 處（下包）、A-PM05（16 列 proc/ER 矛盾之真側）、
step 1 未檢視、13 項 live DR。
**其餘七本仍凍結**（Pei 指示），總表存 `10_full_remediation.md` B–H 段。
