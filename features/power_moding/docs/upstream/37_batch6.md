# 上繳包 37 —— `-004` 之裁定、batch 5 三項修正、**batch 6（最後一批）**

- 日期：2026-08-25
- 下放包：[handoff/37_batch6.md](../handoff/37_batch6.md)
- **零寫回工作簿**

---

## 0. 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-PMH139～141 **3/3 逐字相符** |
| 2 `-004` 之處置 | ER3 維持；本體 leaf 已具名；**反向 `無依據` 1 → 0** → 停止條件 7 未觸發 |
| 3 batch 5 三項修正 | `-045` → **P0**；`-042`／`-045` 依 R-PMH140 具名三事；`-040` 補不拆理由；`-044` 推定具名 ＋ **A-PMH31** |
| **4 batch 6** | **5 條 TC 自 5 leaf**，lint **32/32**；`desc_coverage` **未涵蓋 0／無依據 0** → 停止條件 8 未觸發 |
| 5 KNOWN-INCOMPLETE | 二項已登記，各附風險陳述 |
| 停止條件 9 | **未觸發** —— 51 條全批自套，priority 與其依據**逐條相符** |
| **TC 產出階段** | **完畢** —— 六批 **51 條**，涵蓋 **45 leaf**；停手 3；**45 + 3 = 48** |

---

## 1. 條文抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH139 | 例外條款之依據得取其本體 leaf | 746 | `fd15fbb8599d6d1a` | `fd15fbb8599d6d1a` | 1 | ✅ |
| R-PMH140 | 許可式之斷言處置 | 509 | `cf25538cf5c6196a` | `cf25538cf5c6196a` | 1 | ✅ |
| R-PMH141 | priority 之依據與級別須同條相符 | 419 | `b9bbbd71e7cd7248` | `b9bbbd71e7cd7248` | 1 | ✅ |

---

## 2. 步驟 2 —— `-004` 之處置（裁乙）

### 2.1 其 `reasoning` 之新增段

```
⚠ **R-PMH139（37 包）—— 本條 ER3 之依據取自其本體 leaf**：本 leaf `SWE1-HMI-PM-001-05` 之 DESC 以 `Exception:` 起首，其逐字為 `Exception: For Maserati applications, the system provides no timeout (per CFTS009); the user must manually press Accept.` —— **未載按下 Accept 之後之結果**。ER3 之 `The disclaimer screen is removed and the last mode screen is displayed` **其依據為本體 leaf `SWE1-HMI-PM-001-04`** 之 DESC（`press Accept to go directly to last mode screen`）。**依 R-PMH1
```

### 2.2 ⚠ 一項自查：我第一次把它插錯了位置

**`gen_batch01.py` 之 `self_check()` 立刻攔下** ——
其驗「`reasoning` 首句須以 `**P?**` 起首」（`priority` 與其依據之相符檢查），
**而我把 R-PMH139 之段落插在 reasoning 之開頭**，使首句不再是 priority 之陳述。

**已改插於該條 reasoning 之末。**

> **值得記一件事**：**R-PMH141 所令之「priority 之依據與級別須同條相符」，
> 其機制在 `gen_batch01.py` 裡早就有了**（12 包所建之 `self_check`）——
> **而 batch 2～6 之產生器沒有它。**
> **`-045` 之矛盾之所以能活到 37 包，正是因為它在 batch 5 而不在 batch 1。**
> 依 R-PMH104 apparatus 凍結，**本包未將其擴及其餘五批**；
> 本包改以**一次性全批自套**代之（§5），**其非常設檢查**。

### 2.3 反向 `無依據` 已降為 0

`desc_coverage` 之 `-004 ER3` 由 `無依據` 改記 **`例外-本體`**，
其於程式中為一獨立分支（不入 `rev_bad`），**其二條件之檢查屬人讀，程式只承載其結果**（已於碼內具名）。

---

## 3. 步驟 3 —— batch 5 之三項修正

### 3.1 `-045` 之 priority 改 **P0**

**其矛盾成立**：`priority` 欄為 `P1` 而其軸註逐字為「**本批唯一之 P0**」。
canon §10.2 之 P0 明列 `safety`／`eCall`，**P0 為正解**。

### 3.2 ⚠ 我在修它的時候又寫錯一句

改 P0 時我把軸註寫成「**本 feature 唯一之 P0**」——
**而實測全六批 P0 共 4 條**（batch 1 之三條免責畫面相關者 ＋ `-045`）。

**已於同輪一併更正**，其 `reasoning` 現載：
四條之依據各異而互不矛盾（前三者為開機序列之阻斷，本條為緊急呼叫之電源回復），
**並記明前後兩次之錯**。

> **同一句話我錯了兩次**：第一次是級別與依據不符，第二次是唯一性宣稱不實。
> **二者皆為「未經量測之陳述」** —— 而第二次是在修第一次的時候犯的。

### 3.3 `-042`／`-045` 之許可式（R-PMH140）

二條之 `reasoning` 各具名三事：(a) 來源為許可式；
(b) 本 TC 所驗者為「於本條所述之條件下該行為確實可發生」；
(c) **其不發生不必然為缺陷 —— 判 fail 前須先確認 pre_condition 確已成立**。
**不另開 DR。**

### 3.4 `-040` 補不拆之理由；`-044` 之推定具名

`-040`：其二後果依 §5.7 不拆 —— **popup 未顯示則其互動無從發生**，後者以前者為前提，非獨立。

`-044`：`hard control` 一路未驗，**其「同結果故不拆」為推定，規格未言其實作為同一路徑**。
**登記為 A-PMH31，不補條。**

> **A-PMH31 之範圍比下放包所指為大**：同型者尚有 **`-041` 之 `ACC`／`RUN`**
> （步驟措詞為 `to ACC or RUN`，實測時取其一）。
> **`-038`／`-045` 不適用** —— 該二條之 ER1／ER2 各驗一鍵，**實際驗了二者**。

### 3.5 四條修正後之全文

#### `NR1L-DisclaimerScreen-040` — HVAC pop-ups display temporarily during Power Button Off state　（**pri = P1**）

**pre_conditions**

```
1. The radio is in Power Button Off state
2. The vehicle gear is not in Reverse
3. The HVAC hard controls are available
```

**test_procedure**

```
1. Adjust an HVAC hard control and read the screen
2. Interact with the pop-up shown and read the power state
3. Check that the Power Button Off state was not cancelled
```

**expected_result**

```
1. An HVAC pop-up is displayed temporarily
2. The radio remains in Power Button Off state after the interaction
3. The Power Button Off state is not cancelled
```

#### `NR1L-DisclaimerScreen-042` — Phone call pop-ups can be displayed over Power Button Off state　（**pri = P1**）

**pre_conditions**

```
1. The radio is in Power Button Off state
2. A phone is paired and able to receive a call
```

**test_procedure**

```
1. Place an incoming call to the paired phone
2. Check that the phone call pop-up is displayed over the Power Button Off state
```

**expected_result**

```
1. An incoming call arrives at the paired phone
2. The phone call pop-up is displayed over the Power Button Off state
```

#### `NR1L-DisclaimerScreen-044` — Answered call returns to Power Off state when it ends without screen change　（**pri = P1**）

**pre_conditions**

```
1. The radio is in Power Button Off state
2. A phone call pop-up is displayed over that state
```

**test_procedure**

```
1. Answer the call by soft control and do not change screens
2. End the call and read the power state
3. Check that the head unit returned to Power Off state
```

**expected_result**

```
1. The call is answered and no screen is changed during the call
2. The call ends
3. The head unit returns to Power Off state
```

#### `NR1L-DisclaimerScreen-045` — SOS and ASSIST can turn the head unit power back on　（**pri = P0**）

**pre_conditions**

```
1. The head unit power is off
2. The SOS and ASSIST controls are available in the vehicle
```

**test_procedure**

```
1. Press the SOS control and read the head unit power state
2. Return the head unit to power off and press the ASSIST control
3. Check that each control turned the head unit power back on
```

**expected_result**

```
1. The head unit power turns back on after the SOS control is pressed
2. The head unit power turns back on after the ASSIST control is pressed
3. Both controls turn the head unit power back on
```


---

## 4. 步驟 4 —— batch 6（最後一批）

### 4.1 拘束之逐項落實

| 拘束 | 落實 |
|---|---|
| (a) `source_clause` 取自 PDF | 五條 origin 皆為 `spec_pdf p10` |
| (b) 產出後即跑 `desc_coverage` | **已跑** —— batch 6 之 5 斷言**全數涵蓋**、其 11 條 ER **全數有依據** |
| (c) 限定逐條具名 | **本批 `limits` 為空** —— 逐斷言導出之結果為「無素材與其取相反值」，其依據見 (d) |
| (d) ch 11 × 矩陣 | **22 包已全對照，牴觸 0**（`VRLP1` × `r11`／`r12`／`r28`／`r29`）—— **直接引用，未重跑**；已於五條之 `reasoning` 各具名 |

### 4.2 `-049` 為強制式，`-050`～`-053` 為許可式

`VRLP1` 之 `shall be functional` 為**強制式** → `-049` 之 ER 得無條件斷言。
其四個互動結果為 `depends on outcome` ／ 037 之 `may result in` → **許可式**
→ `-050`～`-053` 各依 **R-PMH140** 具名三事。

### 4.3 四個結果之拆分依 §8.2.2

螢幕開／關 × 音訊開／關 之四類**互斥且獨立**，併為一條則「其一失效」之判定不明確。
**037 已將其各立一 leaf**，本批逐 leaf 一條，**無須再拆亦不得併**。

### 4.4 五條之全文

#### `NR1L-DisclaimerScreen-049` — VR hard key long press activates the voice assistant when the radio is off

- **leaf**：`SWE1-HMI-PM-026-01`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1
- **`source_clause`**（`spec_pdf p10`）：`VRLP1: VR hard key to activate SIRI/non-native Voice Assistants (eg. Long press of VR HK) shall be functional when radio is OFF and KEY ON or ACC.`
- **軸**：謂詞：VR 硬鍵之可用性（對四個互動結果狀態條）

**pre_conditions**

```
1. The radio is OFF
2. The ignition is in KEY ON or ACC
3. SIRI or a non-native voice assistant is available in the vehicle
```

**test_procedure**

```
1. Long press the VR hard key with the ignition in KEY ON
2. Repeat the long press with the ignition in ACC
3. Check that the voice assistant was activated in both cases
```

**expected_result**

```
1. The voice assistant is activated by the long press with the ignition in KEY ON
2. The voice assistant is activated by the long press with the ignition in ACC
3. The VR hard key is functional in both ignition positions
```

#### `NR1L-DisclaimerScreen-050` — Radio returns to off when the interaction ends with screen off and audio off

- **leaf**：`SWE1-HMI-PM-026-02`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P2
- **`source_clause`**（`spec_pdf p10`）：`Screen Off and Audio OFF (i.e. radio back to off),`
- **軸**：互動結果之等價類：螢幕關／音訊關（對 -051／-052／-053 之其餘三類）

**pre_conditions**

```
1. The radio was OFF and the voice assistant was activated by the VR hard key
2. The interaction with the voice assistant has ended
```

**test_procedure**

```
1. Read the screen state and the audio state after the interaction
2. Check that the radio returned to its off state
```

**expected_result**

```
1. The screen is off and the audio is off after the interaction
2. The radio is back to its off state
```

#### `NR1L-DisclaimerScreen-051` — Screen stays on with audio off after the voice assistant interaction

- **leaf**：`SWE1-HMI-PM-026-03`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P2
- **`source_clause`**（`spec_pdf p10`）：`Screen ON and Audio OFF,`
- **軸**：互動結果之等價類：螢幕開／音訊關（對 -050／-052／-053 之其餘三類）

**pre_conditions**

```
1. The radio was OFF and the voice assistant was activated by the VR hard key
2. The interaction with the voice assistant has ended
```

**test_procedure**

```
1. Read the screen state and the audio state after the interaction
2. Check that the screen is on and the audio is off
```

**expected_result**

```
1. The screen is on after the interaction
2. The audio is off after the interaction
```

#### `NR1L-DisclaimerScreen-052` — Audio stays on with the screen off after the voice assistant interaction

- **leaf**：`SWE1-HMI-PM-026-04`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P2
- **`source_clause`**（`spec_pdf p10`）：`Screen Off, and Audio ON,`
- **軸**：互動結果之等價類：螢幕關／音訊開（對 -050／-051／-053 之其餘三類）

**pre_conditions**

```
1. The radio was OFF and the voice assistant was activated by the VR hard key
2. The interaction with the voice assistant has ended
```

**test_procedure**

```
1. Read the screen state and the audio state after the interaction
2. Check that the screen is off and the audio is on
```

**expected_result**

```
1. The screen is off after the interaction
2. The audio is on after the interaction
```

#### `NR1L-DisclaimerScreen-053` — Screen and audio both stay on after the voice assistant interaction

- **leaf**：`SWE1-HMI-PM-026-05`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P2
- **`source_clause`**（`spec_pdf p10`）：`Screen ON and Audio ON.`
- **軸**：互動結果之等價類：螢幕開／音訊開（對 -050／-051／-052 之其餘三類）

**pre_conditions**

```
1. The radio was OFF and the voice assistant was activated by the VR hard key
2. The interaction with the voice assistant has ended
```

**test_procedure**

```
1. Read the screen state and the audio state after the interaction
2. Check that both the screen and the audio are on
```

**expected_result**

```
1. The screen is on after the interaction
2. The audio is on after the interaction
```


---

## 5. 停止條件 9 —— 51 條全批自套

**凡 `reasoning` 或軸註中出現 `P0`／`P1`／`P2`／`P3` 者，與 `priority` 欄比對。**

```
TC 總數 = 51；不符 = 0
priority 分布：P0 4／P1 41／P2 6
```

> ⚠ **本項為一次性自套，非常設檢查**（apparatus 凍結，R-PMH104）——
> **下一批（若有）不會自動再做一次**；`gen_batch01.py` 之 `self_check` 只管 batch 1。

---

## 6. `desc_coverage` 全表（正向＋反向）

```
=== 正向：DESC 之每一斷言 × 其 leaf 之 TC 集合（R-PMH133）===
  leaf = **45**；斷言 = **60**；**未涵蓋 = 3**；**未判定／不可解析 = 0**

  SWE1-HMI-PM-001-01 A1  **未涵蓋-重複**  `-028` ER1（掛 `SWE1-HMI-PM-006-01`）—— R-PMH137
      When driver door is closed, the system plays a 3-second startup animation.
  SWE1-HMI-PM-003 A2  **未涵蓋-重複**  `-004` ER2（掛 `SWE1-HMI-PM-001-05`）—— R-PMH137
      No timeout is provided for Maserati applications, see CFTS009.
  SWE1-HMI-PM-012 A3  **未涵蓋-部分**  `-009` ER4 只涵蓋啟動音側；**告別音側未涵蓋（A-PMH23，`DR-PMH8` Q3）**
      Sounds will sync amongst all supported vehicle displays.

=== 反向：TC 之每一 ER 斷言 × 其 leaf 之 DESC（R-PMH136）===
  ER 斷言 = **155**；**無依據 = 0**


```

| 項 | 值 |
|---|---|
| 正向 leaf | **45** |
| 正向斷言 | **60** |
| **未涵蓋** | **3**（`-001-01` A1／`-003` A2 之 R-PMH137 重複二例 ＋ `-012` A3 之 A-PMH23） |
| 未判定／不可解析 | **0** |
| 反向 ER 斷言 | **155** |
| **無依據** | **0** |

**停止條件 7（反向 `無依據` ≠ 0）未觸發；停止條件 8（batch 6 有任一 `無依據` 或 `未涵蓋-部分`）未觸發。**

---

## 7. 步驟 5 —— KNOWN-INCOMPLETE 二項（只登記，不作業）

| # | 項 | 風險 |
|---|---|---|
| 五 | 反向表約 **117 項**之 DESC 依據為機器以詞重疊挑出，**只人讀了 25 項低重疊者** | 一條 ER 與某斷言用詞相近而其實驗的是另一件事 → **被記為「有依據」而實際無依據**；**`--must-hit` 之錨點 (2) 只攔「完全無條目」者，攔不到「條目指錯」者**。**其偽陰無法以現行手段量測** —— 量之即須逐項人讀，而那正是本項所缺者 |
| 六 | `測試執行` 之 **26 項**由**一條正規式**判定 | **一條真正的 SUT 斷言若被誤分，其永遠不會被要求 DESC 依據** —— **本檔最大之單一漏檢面**。已列於 `desc_coverage.LIMITS` |

---

## 8. 檢查總表 ＋ 六批 lint

```
batch01 32/32  batch02 32/32  batch03 32/32  batch04 32/32  batch05 32/32  batch06 32/32
--limit-must-hit 通過   --final-step-must-hit 通過   verdict_form 0 failure
desc_coverage exit 0   desc_coverage --must-hit 通過   check_granularity --self-test 通過
```

**新增檢查程式 0、新增檢查項 0** —— apparatus 維持凍結；追溯維度維持封閉為三項。
`check_table` 新增二列（`lint_batch.py generated/batch06.json`；
`desc_coverage.py` 之期望退出碼由 **1 改 0**，其緣由為 R-PMH139）。

---

## 9. 未結 DR —— **4 筆**

| DR | 狀態 | 阻斷 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | `-023` 停手 |
| `DR-PMH6` | `SENT` 2026-08-25 | 否 |
| `DR-PMH7` | `SENT` 2026-08-25 | 矩陣四列 ＋ L160 |
| `DR-PMH8` | **`DRAFT`（8 問）** | 否 —— **其為唯一仍在 Pei 手上者** |

---

## 10. 本包是否仍有該驗而未驗者 —— **有**

1. **batch 6 之五條未經任何人讀覆核。** 五批之中五批皆在 lint 全綠後被判產出面須改
   （12／29／31／33／37 包）。**這是第六批，而 R-PMH120 給它二輪。**
2. **`-050`～`-053` 之四條，其 procedure 完全相同（讀螢幕與音訊狀態），
   只有 ER 不同。** 其可測性繫於「如何使互動之結果落在該類」——
   **而規格與 037 皆未言如何控制之**。**四條之步驟 1 因而是同一句話，
   其於實測時如何區分，本批未答**（§8.4.1 不造值之處置，惟其代價是四條可能都跑成同一個）。
3. **A-PMH31 之範圍我判為二處（`-044`／`-041`），而 `and`／`or` 並列處全批不只二處** ——
   我只查了本批 §7.2 所列之四條。**其餘各批未查。**
4. **R-PMH141 之全批自套為一次性** —— **下一批不會自動再做**，
   而 `-045` 之矛盾正是因為 batch 1 有 `self_check` 而其餘沒有。
   **依 apparatus 凍結未擴及，該取捨已具名。**
5. **`-049` 之 `(eg. Long press of VR HK)`** —— 規格用 `eg.`，
   **其餘啟動手段未驗**；本條取長按一路。**其為列舉之開放式，未量其偽陰。**
6. **51 條之 `tc_id` 仍為 provisional** —— Phase 5 之單次指派尚未做，
   **而 `-024` 之位次空出一格**（R-PMH129）；**指派時該空格如何處置，未定。**

---

## 11. 建議之 commit（**未執行**）

```
feat(power_moding): package 37 — -004 ruled, batch 5 fixes (P0), batch 6 (final batch), TC production complete
```

pathspec（**14 路徑**）：

```
features/power_moding/ANOMALIES.md
features/power_moding/DECISIONS.md
features/power_moding/RULINGS.md
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/37_batch6.md
features/power_moding/docs/upstream/37_batch6.md
features/power_moding/generated/batch01.json
features/power_moding/generated/batch05.json
features/power_moding/generated/batch06.json
features/power_moding/scripts/check_table.py
features/power_moding/scripts/desc_coverage.py
features/power_moding/scripts/gen_batch01.py
features/power_moding/scripts/gen_batch05.py
features/power_moding/scripts/gen_batch06.py
```

### 11.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 寫回工作簿 | **無** —— `workbook_state = BLANK` 未變 |
| 停止條件 7／8／9 | **全未觸發** |
| apparatus | **維持凍結** —— 新增程式 0、新增檢查項 0 |
| 自查 | **二處**：R-PMH139 段落插錯位置（`self_check` 攔下）；`-045` 之唯一性宣稱不實（修正時新犯，同輪更正） |
| 產出階段 | **完畢** —— 六批 51 條／45 leaf ＋ 停手 3 = **48** |
| DR 之發出 | **執行層未發出任何一封**；`DR-PMH8` 維持 `DRAFT`（8 問） |
| 他 feature／`docs/runtime/`／`new_feature.py` | **未觸** |
