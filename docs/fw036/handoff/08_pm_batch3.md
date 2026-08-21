# 下放包 08：PM 第三批 —— 三項風格導正（Pei 覆核意見，2026-08-21）

Pei 對 `…SWQT_PowerManagement_20260821(Revise).xlsx` 提出三項。
分析層實測後判定：**三項為同一病根之三面** —— 步驟不自足。
基準本：**SWC 0708**（286 列，經實測為全語料最合規之範本）。
本包基底：交付本 `20260821(Revise)`（Pei 已寫回）之位元組副本。
新規 0 條（R-2 為既有裁決，R-7 由分析層依 SWC 語料成文，見 §四）。

## 一、問題實測

| 項 | PM 現況 | SWC 基準 |
|---|---|---|
| spec_reference | **283/283 皆 HMI 式**，CFTS-ObjID 0 列 | `CFTS042-4813401`＋換行＋HMI 式，**兩家族並列一行一來源** |
| Input Test Data | **158/283 有內容** | **285/286 = NA** |
| 送訊號步驟 | 18 行含賦值，**帶語意標籤者 0** | `Send CAN: BCM_FD_14.Command_02Sts = 1 (PSD)` |

**病根**：PM 大量步驟寫成
`1. Send the transition listed in Input Test Data`、
`1. Apply each ignition working condition listed in Input Test Data in turn`
—— 步驟本身不含被驅動之訊號與值，測試者須跳讀他欄始能執行。
SWC 步驟自足，故 Input 全 NA。三項因而連動：**內聯回步驟即同時解決
問題 2 與 3；問題 1 為獨立之 M16-PM**。

## 二、M16-PM：spec_reference 家族遷移（283 列）

依 R-2(a) 改為 `CFTS009-{ObjectID}` / `CFTS010-{ObjectID}`，
並依 SWC 範例保留 HMI 式為第二行（一行一來源，換行分隔）：

```
CFTS009-4941354
R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.1
```

**ObjectID 來源**：`features/power/` 既有之 `layer3_full.tsv` /
`source_anchor` 對照（037 之 `Source Requirement ID` 經 SYS2 解析所得
之 item id，即 7 位錨點）。**須以該對照表逐列取值，不得由章節號反推**。
對照表查無者標 `PENDING: DR-{n}`，不得杜撰 ObjectID。

## 三、Input Test Data 內聯（158 列）

依 canon §4.5 判別歸屬，逐列將內容移入步驟或 Pre-Condition，
`Input Test Data` 一律改 `NA`：

- **訊號值／狀態轉換（約 40+81 列）** → 併入 Procedure 之驅動步驟。
  `1. Send the transition listed in Input Test Data`
  → `1. Drive RemStActvSts in STATUS_BH_BCM2 on BH-CAN from 0 (Remote Start Not Active) to 1 (Remote Start Active)`
- **PROXI 參數（37 列）** → 移入 Pre-Condition。
  `$VC_SpecialPKG_IC$: "Tungsten (147)"`
  → PC 增列 `PROXI $VC_SpecialPKG_IC$ = "Tungsten (147)"`，
  步驟移除 `listed in Input Test Data` 之指涉
- **多值列舉（如 row 11 四種 ignition working condition）** → 該列若
  逐一驗證多值，屬 §8.3 sibling 軸；**本包不拆列**，改於步驟內明列
  全部值，並標記待覆核由分析層判定是否需拆 TC

**不得刪除任何資訊** —— 移動而非丟棄；移動後 Input 欄方可寫 NA。

## 四、R-7（分析層依 SWC 語料成文）：訊號值語意標籤

```
R-7 訊號賦值之三段式
步驟中驅動或設定訊號時，須同時具備：訊號三件組（R-1）、原始值、
括號內之語意標籤，格式 `<signal> in <MESSAGE> on <segment> = <raw> (<label>)`。
語意標籤取自該訊號之 DBC `VAL_` 列舉，逐字照抄，不得自撰。
DBC 無 VAL_ 定義者，僅寫原始值並於 remarks 標明。
內部訊號（`X.Info`／`X.Req`）之值標籤取自來源文件之列舉；無列舉者同上。
```

**PM 七個 CAN 訊號之 VAL_ 對照（DBC 實查，逐字）**：

| signal | 0 | 1 |
|---|---|---|
| RemStActvSts | `Remote Start Not Active` | `Remote Start Active` |
| DriverDoorSts | `Closed` | `Open` |
| PsngrDoorSts | `Closed` | `Open` |
| Batt_ST_Crit | `False` | `True` |
| PN14_LS_Actv | `Not_Active` | `Active` |
| PN14_LS_Lvl7 | `Not_Active` | `Active` |
| Radio_btn0 | `Not_Pressed` | `Pressed` |

現行 18 行賦值步驟（rows 56–59、64–67、75、78 等）改寫例：
```
前：1. Drive Radio_btn0 in CLIMATIC_PANEL on BH-CAN from "Not_Pressed" to "Pressed"
後：1. Drive Radio_btn0 in CLIMATIC_PANEL on BH-CAN from 0 (Not_Pressed) to 1 (Pressed)
```
⚠ 現行寫法之值為 VAL_ 標籤字串，缺原始值；改寫後兩者並存。

## 五、驗收

- spec_reference：283 列首行皆匹配 `^CFTS0(09|10)-\d{7}$`；
  PENDING 列數與 DR 登記數相等
- Input Test Data：非 NA 列 = **0**
- 步驟含 `listed in Input Test Data` 之行 = **0**
- 賦值步驟：含原始值且括號標籤逐字等於 DBC VAL_ 者 = 全數
- **不得變動**：A0 B0 C0(R-6b後) D0 E0 F0 G0 H0 I0 I-sib0 J0 K0 L0 N0 P0
- 逐格 diff：僅 spec／input／pre／proc 四欄；`er`／`test_item` 零變動
- x14 下拉讀回；`surgical_save` 唯一路徑
- 抽驗 12 列：7 個 CAN 訊號各 1、PROXI 3、多值列舉 2

## 六、上繳

`docs/fw036/upstream/08_pm_batch3.md`：三項各自之改動列清單、
ObjectID 對照來源與查無列、待覆核列（多值列舉是否需拆 TC）、
新增 DR、lint 前後、diff 證明、
「本包是否仍有該驗而未驗者」獨立判斷、引用裁決編號清單。

**止於工作副本。** 交付本 `20260821(Revise)` 不得覆寫 —— 本批完成後
之寫回版次由 Pei 另定（建議 `(Revise2)`）。
