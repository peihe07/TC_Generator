# 58 包 B4′ / B2″ —— 執行層回報

承 58 包 §H。57 包 §H 第 1–3 步一併完成（該包未及施作即由 58 包接續）。

## 1. 抄錄與登記（§H 第 2 步）

- `RULINGS.md`：**R-P363–R-P367**（57 包五條）＋ **R-P368–R-P369**（58 包二條）逐字抄入。
  抄前重驗 §J：5/5/五條、2/2/二條，皆一致。
- 依 R-P36 加註四處：**R-P348**（相容性檢查之盲區 → R-P364）、
  **R-P354(c)**（八態改依 `VAL_ 1470` → R-P363）、
  **R-P360(b)**（三分法 → R-P366）、
  **R-P355(b)**（「已有 DBC 對照」重定義 → R-P368）、
  **R-P365(b)**（台帳 DBC 改 forms 三檔 → R-P368(e)）。
- `ANOMALIES.md`：**A-PW352–A-PW357**（57 包三項 ＋ 58 包三項）。

## 2. G0 台帳（§H 第 3 步）

`verify_gates.py` 增 `REFERENCE_LEDGER`（路徑 ＋ SHA256，R-P365(c)）。
三檔 SHA **與 `forms/FORMS.md` 所載逐字相同**：

| 檔 | SHA256 |
|---|---|
| `forms/Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679…` |
| `forms/PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3…` |
| `forms/PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf…` |

R4 BHCAN **未入台帳**（R-P368(e)：降為旁證）。
**G0 重跑：素材 9 / 9 ＋ 參考庫 3 / 3，PASS。**

> 素材段與參考庫段分開計數：素材在 `inputs/`（集合相等判準，多一份即 FAIL），
> 參考庫在 `forms/`（全案共用，多出之檔非本 feature 之缺陷）。
> 原素材段之判準 `not missing and not extra` **一字未動**。

## 3. B2″ —— 片段表複驗（G254）

**B-1 衝突數 = 0。片段內容一字未改，僅出處由 R4 改註為 BHCAN2。**

四個訊號在 BHCAN2 與旁證 R4 之**訊息 ID、訊息名、`VAL_` 表全部逐字相同**：
`PowerSts_Telematic`（1470 `STATUS_TELEMATIC`）、
`OperationalModeSts`（854 `STATUS_BH_BCM1`）、
`RemStActvSts`（1132 `STATUS_BH_BCM2`）、
`PowerModeSts`（854 `STATUS_BH_BCM1`）。

⚠ **據實記明（A-PW356）**：實測結果對本包有利，**但不改變 57 包未查 forms/ 之事實**。
B-1 明載「僅 R4 有 573 個訊號」；若四訊號中有一落入該 573，六片段全數作廢。
**未查而僥倖。**

依 R-P363 之更新：片段集改為 `VAL_ 1470` 八值 ＋ 規格態 `INIT` = **九個**；
`ENTER_LOGISTIC_ON` 自附錄移入正表（片段可立、TC 不產）；
`INIT` 依 R-13 保留原名並標 PENDING。**九個片段：七可用、二 PENDING。**

**G246（R-P365(a) 新期望值）**：可用片段 7 / 7 之 `$…$` 全在 BHCAN2 有 `SG_`；
PENDING 片段 2 / 2 逐條掛 DR-PW26。**前二項 PASS**；
第三項（`operative` / `a … state` 殘留 0）須待 B5 施作後方可量，本包不報。

### 首個 B-1 型衝突（A-PW357）

`$PwrAccDelayAct$`（`Timeout1` 之來源，CFTS009-4941055）：
段 1 LID r1458 c1 逐字命中 → 段 2 `BODY_CNTRL3.Comfort_Enable_Time`（`B-CAN`）
→ 段 3 **BHCAN2 無、R4 有、FDCAN8 之訊息為 `BCM_FD_27`**。
依 R-P368(e) 不得逕用 R4 名。影響 `ENTER_STANDBY` 之 `Timeout1` **值**
（不影響片段常數名）。**列 §K 交 Pei。**

## 4. B4′ —— 三段鏈重解（G253）

落檔 `data/dr_pw23_internal_signals_58.md`；55 包版已加標「其結論不得引用」。

| 結果 | 數 |
|---|---|
| **解得** | **2 / 13** |
| 未解得（止於段 1） | **11 / 13** |
| 未解得（止於段 2） | 0 |
| **段 3 查無（R-G13）** | **0** |
| B-1 衝突 | 0（於 13 名之內；`$PwrAccDelayAct$` 為附帶項，見 §3）|

**G253：13 名全有段 1–3 記錄；無「止於段 1/2」而標查無者；本輪不新增 M-n。PASS。**

解得二名：
1. `TLM_Status.Info`（素材恆與 `$Telematic_Power$` 成對）→ **LID r2069 c1 `Telematic_Power` 逐字**
   → `STATUS_TELEMATIC.PowerSts_Telematic` → BHCAN2 ✓
2. `LTM_OperationalModeSts.Info` → **LID r1286 c1 `OperationalModeSts`**（前綴差異，R-P368(b)）
   → `STATUS_BH_BCM1.OperationalModeSts` → BHCAN2 ✓
   ⚠ `LTM_` 指 ECU 側、解得者為 BCM 側車輛點火狀態，**是否同一物屬上游職權**，DR-PW26 第 (1) 問維持。

**三筆語意跳接依 R-P368(b) 拒收**（不得憑語意接 LID 列）：
`Antitheft_Activation.Req` / `Antitheft_Result.Info` → r76 `AntiTheftStatus`（Activation/Result ≠ Status）；
`Front_Panel_OnOff.Req` → r1039 `ICSPowerButton`（即 DR-PW24 之待確認假說）。

## 5. PENDING 重算（R-P369(d)）—— ⚠ 方法正確，實益極小

| 量 | 55 包 | **58 包重算** |
|---|---|---|
| 含任一內部訊號 | — | 131 / 283（46.3%）|
| 含非 `TLM_Status.Info` 者 | 105 | 105 |
| 全部內部訊號皆經 R-P368 解得者 | — | 29（10.2%）|
| **施作後仍帶 `PENDING: DR-PW23`** | **105** | **102 / 283（36.0%）** |

**105 → 102，只少 3 條（−2.9%）。**

R-P368 之判斷成立 —— 55 包之「0 / 13」確為未查，段 1 一做即推翻。
**但重做後 PENDING 幾乎不動。** 原因不在方法而在 LID 之涵蓋：
十一名中有九名在 LID 三個比對欄**完全無列**（非「有列而解不出 CAN 名」）。
LID 收錄的是有 CAN 對應之 Logical Identifier；PM 之這些名是 **HU 內部變數**
（DR-PW23 原案對 `RemStartFail` 已如此判：SYSAD 載其為
`The internal variable to manage the success or failure of remote start`），
**本來就不會進 LID**。

**故 57 包 §K-1 之三選項其量化前提由 105 改為 102 而結構不變 ——
S6 衝突未因 forms/ 而解消，仍待 Pei 裁。**

## 6. 待裁

1. **B-1 型衝突之處置**（58 包 §K）：目前僅一筆（`$PwrAccDelayAct$` →
   `BODY_CNTRL3.Comfort_Enable_Time`，BHCAN2 無 / R4 有 / FDCAN8 訊息名不同）。
2. **57 包 §K-1（PENDING 對 S6）**：量化前提改為 **102 / 283（36.0%）**，三選項結構不變。
3. **57 包 §K-2 / R-P365(d)**：R4 BHCAN 既已降為旁證，
   「是否複製入 `features/power/inputs/`」之問題**隨之消解** —— 台帳所列三檔皆在 `forms/`，
   為全案共用而非跨 feature 依賴。**建議撤回本項**，請確認。

## 7. 未施作

- **B3 可及性報告**（57 包 §H 第 4 步，R-P367）—— 未做
- **B7 三分法施作**（57 包 §H 第 5 步，R-P366）—— 未做，分類已備
  （135 內聯 / 15 逐條檢 / 8 保留說明）
- **B5 機器改寫** —— 依 57 包 §B「仍不施作」，待 B3 覆核與 §K-1 裁後

58 包 §H 之六步全部完成；上述三項為 57 包遺留，待 §6 三問裁後接續。
