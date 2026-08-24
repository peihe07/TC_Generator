# 下放包 28：括號兩案裁定 + 內容三項（PM 收尾批）

基底 `sandbox/b27/pm_27.xlsx`（sha 6e7023c7…）。輸出 `b28/pm_28.xlsx`。
止於工作副本。新規 0 條。

## 一、27 包上繳 §四 裁定

**§四-1（30 列 ER-only 括號）：改。** 形態統一為
`(<trigger> -> <ER 核心子句>)`，`<trigger>` 取該列 setup 段之
**末一驅動步**（去編號、首字小寫）；setup 無驅動步（純讀取列）者取
setup 首步。**此 30 列比照縮併列免 20 詞上限**（trigger 完整性優先，
27 包 §八-2 之先例）。文字全取自該列既有步驟，零新文字。

**§四-2（四軌並存）：不收斂，維持現狀。** lint 全零、sibling 可分
皆達成，四軌均合規；收斂需再動 111 列與一輪覆核，成本大於一致性
收益。登記 **A-PM18**（已知形態差異，非缺陷）。日後若收斂，
時機為下一次 test_item 全欄改動時順帶。

## 二、內容三項

### A. 主詞 TLM→HU（Pei 裁定，語料權威 SWC 全用 HU）

四欄 + 括號下半中，作為**行為主體／裝置指涉**之 `TLM` 一律改 `HU`：
`The TLM is in` → `The HU is in`；`TLM screen`／`display` →
`HU screen`／`display`；`the TLM plays`／`audio output`／`volume` →
`the HU …`；`Bring the TLM to` → `Bring the HU to`。

**例外（不改，白名單）**：
1. `test_item` 上半 verbatim（R-6）
2. 訊號名內之字串：`$STATUS_TELEMATIC.PowerSts_Telematic$` 等
   `$...$` 內一律不動；`TLM_Status.Info`（如仍殘留於任何欄）不動
3. `LTM` 全部不動（13 行，radio 型號）
4. PENDING 字串內文不動

### B. 內部變數行為化（依 `internal_var_observability.md` 逐字句式）

| 變數 | 現行 `Read X and check that it is <V>` 改為 |
|---|---|
| `Timeout1`／`SwitchOff_Timeout_Setting.Req`／`Auto_SwitchOn_Setting.Req` | `Open the <setting> entry in the HU menu and read the <setting> value and check that it is <V>`；作為 PRE 者改 `HMI: "<setting>" is set to <V>` |
| `Antitheft_Activation.Req` = True | `Press the HU power button and check that the Antitheft HMI screen is shown`（ER：`The Antitheft HMI screen is shown`） |
| 同上 = False | `…and check that the HU powers up without the Antitheft HMI screen` |
| `VPLastStatus` = ON | `Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 4 (Ignition_On) and check that the HU powers up automatically and shows the splash screen` |
| 同上 = OFF | `…and check that the HU does not power up automatically` |
| `Phone_Call.Info` = Active／Not_Active | `Place a phone call from the paired device and check that the call screen is shown`／`End the call and check that the call screen is dismissed` |
| `Rear_Camera_Enable.Info` | 行為化：倒車影像顯示與否 |
| `RemStartFail` | **不可行為化**（無直接 HMI）。該檢查步改
  `PENDING: DR-PW23 observation method for RemStartFail`，ER 同步 |
| `Antitheft_Result.Info` | Antitheft HMI screen 之結果畫面 |

規則：改一步即同步改該步之 ER 行（1:1 維持，E=0）。
**套不進上表句式之列不得自創**——列清單於上繳回報，分析層接手。
PRE 中作為**前提宣告**之變數（`Antitheft_Activation.Req is set to True`
等）維持宣告式不動（前提非觀察）。

### C. `Front_Panel_OnOff.Req`（13 行）

`Drive Front_Panel_OnOff.Req from Not_Pressed to Pressed`
→ `Press the HU power button`；ER 對應行
→ `The HU power button press is registered`。
DR-PW24 已載其與 `$ICSPowerButton$` 之對應待確認，本包不改名不加 `$`。

## 三、驗收

- I 欄改動 = 恰 30 列（§一）；其餘 test_item 零變動
- 主詞 `TLM` 於四欄殘留 = 0（白名單除外，逐項列出殘留與所屬白名單類）
- `Read Antitheft_Activation.Req`／`Read VPLastStatus`／
  `Read Timeout1`（裸讀式）殘留 = 0
- `Front_Panel_OnOff.Req` 於 proc 殘留 = 0
- PENDING 新增數 = RemStartFail 檢查步數，逐列列出
- E=0；lint A–N 全零；x14 讀回；zip 42；`surgical_save` 唯一路徑
- 與 pm_27 逐格比對：相異欄限 I／K／N／O（test_item／pre／proc／er）

## 四、上繳

`docs/fw036/upstream/28_content.md`：三項各自改動清單、套不進句式
之列清單、PENDING 清單、lint 前後、diff 證明、
「本包是否仍有該驗而未驗者」獨立判斷、引用裁決編號清單。

## 五、本包後續（既定，不變）

③ 390 列人讀覆核（分析層，基準 pm_28）→ ④ Pei Excel 實開抽驗＋
重新授權 → ⑤ 寫回 `(Revise2)`＋TestRail 舊 ID→新 ID 對照表同包產出。
其餘七本仍凍結。
