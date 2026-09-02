# 上繳包 07 — vsm_v42：b1 微修（R-VL22）與凍結

日期：2026-09-02　執行層：Claude Code　對應下放包：`docs/handoff/07_b1_freeze.md`

## 結果分類（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | `-053` 一列；`-054` 量測後改 in-mode 型；`-046` design_method；INDEX 重產 |
| 核實無誤 | **E53 過**、**E54 = 0 過**、**E55 過**（E38–E45 全數）；`-054` 之歸類量測有對照組佐證 |
| 正確地不動 | **`-059` 不改** —— E56 之唯一不符落於該條，其不在本包修訂範圍（E53：其餘 diff = 0）；不寫工作簿；不建 `delivered/` |

**總判：三項修訂完成。E56 = 16／17，肇因同上輪之型（範圍以條列劃定而缺陷以型分布），不自行調和。
→ 第 6 節：b1 凍結之聲明**附條件保留**，待該一列裁定。**

---

## 1. `-054` 歸類量測（R-VL22(c)）—— 逐字證據

**量測式**：規格節中 Fdbk = 8 之段及其前後各一句，掃 `entering|exiting|request`（不分大小寫）。

### 受測範圍逐字（段 1092–1096）

| 段 | 逐字原文 |
|---|---|
| 1092 | （空） |
| 1093 | `IF TLM receives "IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk" set to " 8 "` |
| 1094 | `THEN TLM sall:` |
| 1095 | `activate and display the  Popup related to " Brake Service Park Brake Retracted. To reset, press brake pedal and activate Park Brake switch."  like described in the "Human Machine Interface logic &  flow" document` |
| 1096 | （空） |

### 掃描結果

| 詞 | 命中 |
|---|---|
| `entering` | **0** |
| `exiting` | **0** |
| `request` | **0** |

### 對照組（證量測式有效，非全節皆無）

| 段 | 命中詞 |
|---|---|
| 1064（Fdbk = 2 之 IF 句） | — |
| **1066（Fdbk = 2 之 popup 句）** | **`entering`** |
| 1097（Fdbk = 9 之 IF 句） | — |
| **1099（Fdbk = 9 之 popup 句）** | **`exiting`** |

即：同型之他值其 popup 句皆帶 `entering`／`exiting`，**唯 Fdbk = 8 之 popup 句兩者皆無**。

**判定：皆無 → in-mode 狀態回報型**（R-VL22(c) 第三分支）。
**升級條件「有詞但語意不明」未觸發**（無詞可歧義）。

---

## 2. 逐列 diff

### `-053`（R-VL22(a)，一列）

| | 內容 |
|---|---|
| 舊 ER1 | `The signal $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ = 1 (On) is registered without a bus error` |
| **新 ER1** | **`The signal value $TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req$ = 1 (On) is received`** |

其餘欄位（Procedure、Pre-Condition、test_item、reasoning、design_method、priority）**未動**。

### `-054`（R-VL22(c)）

| 項 | 修訂前 | 修訂後 |
|---|---|---|
| Procedure 步數 | 3 | **2** |
| P1 | `Select "EPB Maintenance Mode" = "Off" to request the exit from Service Mode` | **刪除** |
| E1 | `The named UI element "EPB Maintenance Mode" setting control is "Off"` | **刪除** |
| P1（現） | — | `Send the signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 8` |
| E1（現） | — | `The signal $IPC_VEHICLE_SETUP2.EPB_Maintenance_Fdbk$ = 8 is registered without a bus error` |
| P2／E2（現） | 原 P3／E3 | `Read the named UI element "Brake Service - Park Brake Retracted" …`／`… is displayed` |
| Pre-Condition | 三項（含 `The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 1 (On)`） | **維持不變**（R-VL22(c) 明令） |
| 括號下半 | `Fdbk = 8: park brake retracted reset instruction popup` | **`Fdbk = 8: park brake retracted reported while already in Service Mode`** |
| `distinguishing_axis` | `Fdbk 值 8（駐車煞車已收回）…` | 加註 **in-mode 型；規格段 1093–1095 無三詞，與進出側九條之發起型不同** |
| remarks | 退出側之「請求路徑未載」說明 | 改記 **R-VL22(c) 之量測結果與歸類依據** |
| reasoning | 退出側版本 | **重寫 5 句**，含量測結果與對照段 |

**Procedure ↔ ER 2:2，1:1 成立。** 括號下半與其餘 16 條**無一逐字相同**（E39 複驗 0 違規）。

### `-046`（R-VL22(d)）

| | 內容 |
|---|---|
| 舊 | `情境 / 用例 (Scenario / Use Case Testing)` |
| **新** | **`功能測試 (Functional based ; no specific technique)`** |

下拉詞彙逐字（`下拉選單` A1）。其餘欄位未動。

---

## 3. 同型全批掃描（下放包第一節之 4，本包起固定）

對全 17 條 grep `registered without a bus error`，逐步判其訊號之送出方：

| 項 | 實測 |
|---|---|
| 全批出現數 | **15** |
| 其中**測試員送出**（步以 `Send the signal` 起）| **15** |
| 其中 **DUT 送出**（`Select …` 觸發 TLM 送出） | **0** |

**E54 = 0，過。** 修訂前為 1（`-053`），已由本包消除。

---

## 4. 預期數字 E53–E56

| # | 項 | 判準 | 實測 | 判 |
|---|---|---|---|---|
| **E53** | 修訂檔數 | `-053` 必改；`-054` 依量測；`-046` 必改；其餘 diff = 0 | **改 6 檔**（`-046`／`-053`／`-054` 各 json＋md）；其餘 28 檔逐位元 diff = 0（`INDEX.md` 另行重產，見第 7 節） | **過** |
| **E54** | DUT 送出步之 bus-error 式 | 0 | **0** | **過** |
| **E55** | E38–E45 重跑 | 全過 | **E38 17/17／E39 0／E40 0／E41 0／E42 0／E43 0／E44 0／E45 0** | **過** |
| **E56** | `test_item` 逐字全等斷言（對 037 Description） | 17／17 | **16／17** | **不符** |

### E56 之不符 —— 逐字證據

唯一不符者 **`SWE1-VC-EPBMaintenanceMode-059`**。

**本包所寫之 `test_item` 上半**：
```
When the TLM receives a value changing from <= [V_Car_Moving] to > [V_Car_Moving] via signals
(STATUS_CCAN3.VehicleSpeedVSOSig), Then TLM shall send a layout request to the display manager
through internal signal (ServiceMode_Popup_Trigger.Info)
```

**037 `Requirement Description` 之原句**：
```
When the TLM receives a value changing from <= [V_Car_Moving] to > [V_Car_Moving], or a transition
from [Ignition Off] to [Ignition On] via signals (STATUS_CCAN3.VehicleSpeedVSOSig) | (Ignition_{S}tatus),
Then TLM shall send a layout request to the display manager through internal signal
(ServiceMode_Popup_Trigger.Info)
```

**差異**：本包上半**剪去了句中之 ignition 子句**（`, or a transition from [Ignition Off] to
[Ignition On]` 與 `| (Ignition_{S}tatus)`），以配合該 TC 之窄化範圍（ignition 分支未涵蓋，
上繳 05 §K K-3 已揭露）。

**性質**：此為**句內剪接**，非「摘句」。R-S4 之「摘句以與括號下半直接相關之**句**為限」以**句**為單位；
剪去句中子句即改寫原文，違 R-4／R-6 之逐字紀律。**這是本執行層於上繳 05 所造之缺陷，
歷經 05／06 兩輪自檢未被察覺 —— E56 為本線首跑，一跑即攔下。**

**修法已備妥（一列，未施行）**：上半改為**完整原句 verbatim**（含 ignition 子句），
實測 **42 token**（R-3 上限 50，通過），且為 037 Description 之**逐字子字串**（機讀驗證 `True`）。
ignition 分支之未涵蓋聲明維持於 `reasoning` 與 `remarks`（§8.2.1 委任式揭露），不受影響。

**未施行之理由**：`-059` **不在下放包 07 之修訂範圍** ——
下放包第一節只列 `-053`／`-054`／`-046` 三條，E53 明定「其餘 diff = 0」。
依 **R-VL22(a)** 之裁定（「執行層守明文不自調和正確」），本包**不動 `-059`**，回報並備妥修法。

> **此為上輪 E46↔E50 之同型復發，且 R-VL22(a) 之防再犯措施未涵蓋之**：
> 該條令「往後修訂包之範圍一律附同型全批掃描式」，下放包 07 確實照辦（第一節之 4），
> **但該掃描只針對 `bus-error` 一型**。E56 是**另一型**且為首跑，
> 其發現之缺陷因而落在已劃定之範圍外。
> **建議**：凡**首跑**之新檢查（E56 型）不應與修訂範圍同包發布 ——
> 或其範圍條款須加「首跑檢查所揭之缺陷自動入範圍」之但書。

---

## 5. §9 機讀重跑

17 條全數重跑，機讀可判之 **14 項全 PASS，未過項 0**（清單同上繳 05／06）。

`scripts/lint036.py` 仍未跑（只吃 `.xlsx`，寫工作簿為禁區），以自檢表代。

### 分布（07 後）

| 項 | 分布 |
|---|---|
| priority | P1 4／P2 13（未動） |
| design_method | 等價劃分 9／**功能測試 3**（`-046` 由情境用例改入）／狀態轉換 2／負向測試 1／基礎故障注入 1／邊界值分析 1；**情境／用例 0** |
| PENDING | **6**（未動） |
| `$…$` | 4 種訊號，皆 v3「解得」 |
| bus-error 式 | 15，**全為測試員送出步** |

---

## 6. b1 凍結之聲明（**附條件**）

下放包第五節：「完成即 b1 凍結（R-VL22(e)）」。

**本包之聲明**：三項修訂已完成，E53／E54／E55 全過。
**惟 E56 = 16／17，`-059` 帶一個已具名、已備妥修法之逐字違規。**

**執行層不逕行宣告凍結**，理由：

1. 凍結之效力為「此後任何變更須新裁決」。若於**已知**且**已備妥修法**之逐字違規上凍結，
   該一列修正將被迫走新裁決之流程，成本高於現在改。
2. 該違規之性質為**追溯性**（`test_item` 上半為需求原句之逐字載體），非風格問題；
   b1 若寫回工作簿，該列即成交付內容。

**兩條路，交分析層／Pei 擇一**：

| 路 | 動作 | 結果 |
|---|---|---|
| **A（建議）** | 授權本包外加修 `-059` 一列（上半改完整原句 verbatim），重跑 E55／E56 | E56 → 17／17，**b1 乾淨凍結** |
| B | 維持範圍，**帶著該違規凍結** | b1 凍結成立，`-059` 之修正另開包並須新裁決 |

**在裁定前，本上繳不記「b1 已凍結」**；`INDEX.md` 之「已知未結」段已載此項。

---

## 7. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `generated/b1_epb/…-046.{json,md}` | design_method（R-VL22(d)） |
| `generated/b1_epb/…-053.{json,md}` | ER1 一列（R-VL22(a)） |
| `generated/b1_epb/…-054.{json,md}` | in-mode 型改寫（R-VL22(c)） |
| `generated/b1_epb/INDEX.md` | 重產 —— 加「歸類（量測後定）」段、修訂輪欄、**「已知未結」段（E56）** |
| `features/vsm_v42/docs/upstream/07_b1_freeze.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：`generated/b1_epb/` 其餘 28 檔（逐位元 diff = 0，含 **`-059`**）、
`features/vsm_v42/sandbox/`（未開啟）、`delivered/`（未建）、
`docs/fw036/RULINGS.sha.tsv`、`docs/runtime/profiles/`、`scripts/`、`forms/`、
`features/vsm_v43/`、`features/vehicle_setting/`、`sources/`、
`features/vsm_v42/{RULINGS.md, DATA_REQUESTS.md, ANOMALIES.md, DECISIONS.md, feature.yaml,
framework.md, data/}`、`docs/handoff/`。
**git**：本包未執行任何 git 寫入指令。

---

## 8. `gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 506
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0
```

**(甲) `rulings_hash`** —— 依 **R-VL13** 記「**待 Pei 重生**」；
依 R-VL15(c) 之判準（無刪除列、既有列 `body_sha8` 無變動）滿足，可上繳。
**`R-VL22` 之 `body_sha8` = `1d91e1b5`**（`sha8` = `e6ac2299`，觀測值）。

**(乙) `canon_refs` 506** —— 含 `vsm_v42` 者 **3 列**，與上繳 02–06 逐字相同。
本包修訂之 7 檔未新增任何一列。

**(丙)(丁) `gates_tsv`／`lint_paths` = 4** —— 與本線無關，先在。

**無一支肇因於本包之寫入。**

---

## 9. 獨立判斷

1. **一項缺陷由本包之新檢查攔下，且係本執行層所造**：`-059` 之句內剪接（第 4 節）。
   於上繳 05 生成時即已存在，05／06 兩輪自檢未涵蓋該面向。**E56 之制度化有效。**
2. **一項同型復發已具名**：範圍以條列劃定 vs 缺陷以型分布（第 4 節末），
   R-VL22(a) 之防再犯措施只涵蓋 `bus-error` 一型。建議加「首跑檢查所揭之缺陷自動入範圍」之但書。
3. **一項未依下放包字面**：本包**未宣告 b1 凍結**（第 6 節），附理由與兩條路。
4. **一項提醒**：`-054` 改為 in-mode 型後，其 Pre-Condition 之
   `The signal $IPC_VEHICLE_SETUP2.EPB_MaintenanceMode$ is 1 (On)` 為**訊號值型**之前置狀態。
   §4.4 允許「feature initial state」，本包判其合規；若覆核認為訊號值前置應改為步驟注入，
   則該條需再改一次 —— **現在提出，避免凍結後才發現**。
5. **一項承上未結**：上繳 05／06 之 §K K-1〜K-6 六項仍未結（皆已具名，DR 依 Pei 裁不送）。

---

## 10. 待 Pei／分析層之四項

1. **E56 之 `-059` 一列**（第 4／6 節）：走 A 路（授權外加修，b1 乾淨凍結）或 B 路（帶違規凍結）。
2. **範圍條款之但書**（第 4 節末／第 9 節 2）：首跑檢查所揭缺陷是否自動入範圍。
3. **`-054` 之 Pre-Condition 訊號值前置**是否合 §4.4（第 9 節 4）。
4. **寫回工法包**（R-VL22(e)，含 x14 DV 保全查證）＋ b2 批次序
   ＋ §K K-1〜K-6 ＋ 台帳重生時機。
