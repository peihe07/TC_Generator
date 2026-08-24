# 下放包 25：拆分套用（A 型逐字 + B 型規則化）

Pei 裁定：A／B 皆拆；重複列**保留**（A-PM04／13／14 不刪）；
新列原位插入、**全本 TC ID 重排**（政策 b）。
基底：`sandbox/b19/pm_19.xlsx`（b4dd5ca0…）。

## 一、A 型（5 列 → 14 列，逐字）

**row 11 → 4 列**。共同 PRE（四列逐字同）：
```
1. The TLM is in Full-Operation state
2. LIN and CAN tool is available on HU
```
各列 PROC／ER（`<V>`／`<L>` 代入下表）：
```
PROC:
1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = <V> (<L>)
2. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 4 (Full_Operation)
ER:
1. The signal $STATUS_BH_BCM1.OperationalModeSts$ = <V> (<L>) is registered without a bus error
2. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation) is received
```
| 分列 | V | L | 括號下半 |
|---|---|---|---|
| 11a | 5 | Ignition_Pre_Start | (send OperationalModeSts = 5 Ignition_Pre_Start -> Full-Operation is kept) |
| 11b | 6 | Ignition_Start | (send OperationalModeSts = 6 Ignition_Start -> Full-Operation is kept) |
| 11c | 7 | Ignition_Cranking | (send OperationalModeSts = 7 Ignition_Cranking -> Full-Operation is kept) |
| 11d | 8 | Ignition_On_EngOn | (send OperationalModeSts = 8 Ignition_On_EngOn -> Full-Operation is kept) |

**row 12 → 3 列**（PRE 沿原列五行）：
| 分列 | PROC（2 步） | 括號下半 |
|---|---|---|
| 12a | `1. Select SDCARD as the audio active source`／`2. Read the played audio source and check that it is the SDCARD` | (select SDCARD -> SDCARD is played) |
| 12b | `1. Select BT Music streaming as the audio active source`／`2. Read the played audio source and check that it is the BT Music streaming` | (select BT Music streaming -> BT Music streaming is played) |
| 12c | `1. Place a phone call`／`2. Read the played audio source and check that it is the phone call` | (place a phone call -> the phone call is played) |
ER 逐步對應（`The <source> is selected…`／`The TLM plays the <source>…`
沿原列該兩行逐字）。

**row 23 → 3 列**：同 12a–c，PRE 沿 row 23 原列（Timed 狀態）。

**rows 179／180 → 各 2 列**（PRE 沿各原列）：
| 分列 | PROC | 括號下半 |
|---|---|---|
| a | `1. Let the bench place an incoming phone call to the HU`／`2. Read the HU mode and check that it is FULL OPERATION` | (incoming call -> FULL OPERATION) |
| b | PRE 增一行 `An incoming phone call is active on the HU`；`1. Let the phone call become inactive`／`2. Read the HU mode and check that it is IDLE` | (call becomes inactive -> IDLE) |
ER 沿原列對應行。

## 二、B 型（30 列 → 186 列，規則化）

**拆分演算法**（執行層依此組裝，內容全取自原列，零新文字）：
1. **setup 段判定**：PROC 自首步起，至第一個
   `Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$…` 止
   （含該步）為 setup 段；無此步者，凡 `Send…`／`Bring…`／
   `Power up…`／`Reconnect…` 之連續前導步為 setup 段；
   兩者皆無（純讀取列，如 row 24）→ setup 段 = 第 1 步。
2. **面向列生成**：setup 段之後每一步為一面向，各生成一列：
   - PRE：逐字複製原列
   - PROC：setup 段全部步驟 + 該面向一步（重新編號 1..n）
   - ER：setup 段對應 ER 行 + 該面向對應 ER 行（重新編號）
   - test_item 上半：逐字複製；括號下半：
     `(<該面向 PROC 步驟去編號、首字小寫> -> <該面向 ER 行去編號>)`
     超過 20 詞時取 ER 行之核心子句
3. **原列處置**：原列改寫為第一面向列（即 setup + 面向 1），
   其餘面向為新插入列，緊接其後。
4. Requirement ID／Test Set／spec_reference／Priority／
   Design Method：逐字複製原列至所有面向列。

**30 列清單與面向數**（合計 186）：
10(5)、17(5)、21(6)、24(7)、26(7)、28(5)、29(6)、30(7)、32(5)、
39(5)、45(7)、97(5)、102(5)、109(5)、124(8)、125(8)、126(8)、
127(8)、157(6)、158(6)、159(6)、162(6)、170(5)、188(6)、189(8)、
190(5)、194(8)、197(5)、204(5)、285(6)

⚠ 面向數 = 原列 ER 編號行數；**執行層須逐列以實際 ER 行數重算**，
上表為分析層預核值，不一致時以實測為準並於上繳列出差異。

## 三、ID 重排（政策 b）

拆分插列完成後，全本 `Test Case ID` 自首列起重編
`NR1L-PowerManagement-001` 連續遞增至末列（預估 ~448）。
**僅重寫 ID 欄，他欄不動。**

## 四、驗收

- A 型 14 列與 B 型 186 列逐列存在；原 5+30 列已為各自首面向
- 全本列數 = 283 + 9 + 156 = **448**
- ID 連續無跳號、無重複；`proc↔er` 編號數逐列相等（E=0）
- 每一面向列：PRE 與原列逐字同；setup 段與原列逐字同
- 括號下半：任兩同源面向列不得逐字相同（sibling 可分）
- lint A–N 全零；x14 讀回；`surgical_save` 唯一路徑；止於工作副本

## 五、上繳

`docs/fw036/upstream/25_split.md`：插列對照表（原 row → 新 rows）、
面向數差異清單、ID 重排前後對照（首尾樣本）、lint 前後、
「本包是否仍有該驗而未驗者」獨立判斷。

**本包後續**：內容三項（TLM→HU 448 行、內部變數行為化、
Front_Panel_OnOff）於拆分套用並覆核通過後另包執行（23 包 §第二步）。
