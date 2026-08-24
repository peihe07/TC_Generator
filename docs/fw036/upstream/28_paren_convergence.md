# 上繳 28 包：括號四軌收斂為 V2

基底 `features/power/sandbox/b27/pm_27.xlsx`（sha256 `6e7023c7…`）。
輸出 `features/power/sandbox/b28/pm_28.xlsx`（sha256 `0dded0ea…`），
390 資料列，止於工作副本，客戶目錄未動。

## 摘要

| 項 | 裁定／要求 | 實測 | 狀態 |
|---|---|---|---|
| 括號形態 | V2 | 全本 B 型 127 列**獨立重算**逐列相符 | 達成 |
| ER-only 括號 | 收斂掉 | **0 列**（27 包為 30 列） | 達成 |
| 形態 B 16 列 | V2 之特例、不應變動 | **16/16 逐字不變** | 達成 |
| A 型 14 列 | 不在本案 | **零變動** | 達成 |
| §八-1 row 160 | 保持原列逐字 | **仍與 b19 原列逐字同** | 達成 |
| 相異範圍 | —（本包自加） | 逐格比對 pm_27：**僅 I 欄、74 列** | 達成 |
| 列數／ID／No.# | 不變 | 390 列、001–389、1–390，與 pm_27 相同 | 達成 |
| 括號碰撞 | 0 | **0 組**；消歧列數 40 → **15** | 達成 |
| lint A–N | 全零 | 全零（含 I-sibling=0、C=0） | 達成 |
| x14 讀回 | 前後相等 | `R10:R325` → `R10:R325`，zip 42 未變 | 達成 |

`verify.py` 共 13 項，全項達成。V2 通則在 `verify.py` 內**獨立重算**
（不讀 `plan.json` 之 `I` 值），故 build／apply 若脫節、或規則實作有誤，
驗收會攤開而非放行。

### lint 前後（`--profile power`）

| | A | B | **C** | D–N（含 I-sibling） | P | U |
|---|---|---|---|---|---|---|
| 27 包 `pm_27` | 0 | 0 | 0 | 全 0 | 10 | 10 |
| 28 包 `pm_28` | 0 | 0 | **0** | 全 0 | 10 | 10 |

C 曾在中途變 4，已修正（見 §二-3）。
報告：`docs/fw036/lint_reports/pm_28__power_20260824.md`。

## 一、V2 通則之實作

`(<trigger> -> <ER>)`，trigger 依序取：

1. **該面向自己的驅動步** —— 即 §八-2 之形態 B。16 列，逐字不變，
   形態 B 因此不是第四軌而是本通則的特例。
2. **setup 段最後一個驅動步** —— 67 列。
3. **兩者皆無**（PROC 全為讀取之純觀察列，情境只寫在 PRE）→
   落回 `(<觀察步> -> <ER>)`。37 列。

trigger 判定用之動詞表較切分用之 `DRIVE_VERB` 寬
（多 `Bring`／`Power up`／`Reconnect`／`Open`／`Issue`），因 setup 段之
驅動步用語更雜。**切分判準未動**，兩表刻意分開並於程式註記。
實測選中之 trigger 無一含 `check that`（不會誤取觀察步）。

## 二、執行層自加之三項判斷 —— 皆待追認

裁定只給了「V2」二字，以下三項是實作過程中不得不決的，均非 Pei 原文：

### 1. 20 詞上限對 B 型面向列全面停用（22 列逾限）

§八-2 已裁「trigger 是重點，寧長不砍」，但免除範圍原文寫**僅縮併列**。
V2 下若對非縮併列仍套上限，22 列會退回 ER-only、四軌又變三軌，
與「收斂」直接矛盾。故按同一理由全面停用。最長 32 詞。

### 2. 同一原列內括號撞號 → 退回規則 3（原列 197，2 列）

V2 規則 2 使同一原列的各面向**共用同一 trigger**，括號因此只靠 ER 半區分。
原列 197 之面向 1 與 3 觀察步互異（`shows 15` vs `still shows 15`）
但 **ER 行同文**，括號遂逐字相同；而消歧兩段候選（setup 首步／PRE 行）
在同一原列內全同、救不了。故該組退回 V2 規則 3 之形態（觀察步式），
觀察步在該列內互異。影響 row 296／298（原列 197）。
**未新增形態** —— 退路用的是 V2 自己的規則 3。

### 3. trigger 含 lint check C 之 hedge 詞 → 退回規則 3（原列 102，4 列）

原列 102 之 setup trigger 為 `Set Antitheft_Result.Info to Successfully`。
`Successfully` 是 `Antitheft_Result.Info` 的**訊號值**，但 check C
（`properly`／`successfully`／`within reasonable time`）依 R-6b 對
**括號下半**生效、且不設引號豁免 —— trigger 搬進括號即令 C 由 0 變 **4**，
違反 §四「lint A–N 全零」。

故 trigger 式若含 C 之 hedge 詞即落回規則 3。判準直接綁
`lint036.RE_C`，不另立定義（單一來源）。影響 rows 150–153（原列 102）。

⚠ 此處暴露一個更一般的問題：**PROC 不受 C 規制、括號下半受**，
而 V2 通則的本質就是把 PROC 的文字搬進括號。目前只撞到一個詞
（`Successfully`），但只要日後有列的驅動步用到 `properly`
或 `within reasonable time`，同樣會撞。見 §四-1。

## 三、逐列資料

## 軌數分布（B 型 127 列）

- 規則 3：純觀察列（PROC 無驅動步）：**37** 列
- 規則 2：setup 末個驅動步：**67** 列
- 規則 1：面向自己的驅動步：**16** 列
- 退路：規則 3：**6** 列
- §八-1 原列逐字：**1** 列

## 收斂前後對照樣本

**row 25**（`…-016`）
- 27 包：`(read the AMP state and check that it is off -> The AMP is off)`
- 28 包：`(send the signal $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active) -> The AMP is off)`

**row 53**（`…-044`）
- 27 包：`(read the AMP state and check that it is on -> The AMP is on)`
- 28 包：`(bring the TLM to the Bench state -> The AMP is on)`

**row 151**（`…-142`）
- 27 包：`(A proper Splash Screen is shown on the TLM screen for Response_Wait_Time)`
- 28 包：`(read the TLM screen and check that a proper Splash Screen is shown for Response_Wait_Time -> A proper Splash Screen is shown on the TLM screen for Response_Wait_Time)`

**row 175**（`…-166`）
- 27 包：`(send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) — read the network state and check that the network is on -> The network is on)`
- 28 包：`(send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 2 (Ignition_Off) -> The network is on)`

**row 275**（`…-266`）
- 27 包：`(the TLM is in BODY ON mode — read the TLM volume indicator and check that it shows 25 -> The TLM volume indicator shows 25)`
- 28 包：`(the TLM is in BODY ON mode — set the TLM volume level to 25 -> The TLM volume indicator shows 25)`

**row 297**（`…-288`）
- 27 包：`(send the signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) -> No AUD_LVL signal carrying a new volume level appears in the CAN trace)`
- 28 包：`(send the signal $STATUS_LIN.Batt_ST_Crit$ = 1 (True) -> No AUD_LVL signal carrying a new volume level appears in the CAN trace)`

**row 306**（`…-297`）
- 27 包：`(The HU collects and saves logs at the time of the reset)`
- 28 包：`(read the stored logs and check that the HU collected and saved logs at the time of the reset -> The HU collects and saves logs at the time of the reset)`

**row 389**（`…-379`）
- 27 包：`(The core disclaimer screen is shown on the first ignition cycle)`
- 28 包：`(run the head unit through the first ignition cycle -> The core disclaimer screen is shown on the first ignition cycle)`


## 四、本包是否仍有該驗而未驗者 —— 獨立判斷

**有，四項。**

### 1. `lint C × 括號取自 PROC` 之結構性衝突，只被繞過、未解決

§二-3 的退路解了目前唯一的實例（`Successfully`），但沒解掉成因：
V2 通則把 PROC 文字搬進括號，而 PROC 不受 check C 規制、括號下半受。
現行退路是**靜默降級**（該列悄悄變成觀察步式），下次撞到時同樣悄悄降級 ——
形態不齊會慢慢累積而沒人看到。

可選的根治方向：(a) 對括號下半之 C 加引號／訊號值豁免（動 lint，
須併 canon）；(b) 明訂「trigger 含 C 詞者一律用規則 3」為 V2 之第四條
（把現行退路升格為規則，形態不齊就是明訂的而非意外）。**未擅改。**

### 2. 43 列仍為觀察步式 —— 其中 6 列是退路、37 列是純觀察列

收斂後為兩軌（trigger 式 83 列、觀察步式 43 列、原列逐字 1 列）。
37 列純觀察列的情境只寫在 PRE，括號因此不含任何情境資訊 ——
這是 V2 明訂接受的代價（單一形態做不到）。若日後要再收，
唯一材料是 PRE 之狀態行，屆時括號會再長一截。此處僅記錄，不建議現在動。

### 3. 同列 ER 同文者不只 197 一列？—— 本包只驗到 0 碰撞，未普查

§二-2 的退路是碰撞觸發式的，本包實測殘餘碰撞 0，故**現況無漏**。
但「同一原列有兩個面向 ER 行同文」這件事本身可能是原列的缺陷
（197 的 `shows 15` 與 `still shows 15` 對應同一句 ER，ER 沒把
「仍然」寫出來）。那是 ER 的措辭問題，屬 ② 內容三項的鄰域，
本包未查其他 29 列有無同型。

### 4. 沿舊仍未做者

- **② 內容三項**（TLM→HU、行為化、Front_Panel）—— **下放包未到**，
  本包因此只做 ①。你原本的規劃是「① 併入 ②」，實際是 ① 先獨立成包；
  ② 到時基準為 **pm_28**
- **③ 390 列人讀覆核** —— 未跑，基準已換為 pm_28
- **④ Excel 實開抽驗 + 授權** —— 屬 Pei，未做
- **⑤ 寫回 `(Revise2)` + TestRail 對照表** —— 未做。本包未動列數與 ID，
  故對照表基準不因本包而變（pm_26／27／28 之 ID 完全相同）

## 五、產物

| 路徑 | 內容 |
|---|---|
| `features/power/sandbox/b28/pm_28.xlsx` | 輸出工作副本，390 列，sha256 `0dded0ea…` |
| `features/power/scripts/b28/build.py` | 分析層：V2 通則三規則 + 兩條退路 → `plan.json` |
| `features/power/scripts/b28/plan.json` | 35 原列 × 141 面向列之四欄內容 |
| `features/power/scripts/b28/apply.py` | 執行層：I 欄 74 列改寫，`surgical_save` 單段 |
| `features/power/scripts/b28/verify.py` | 驗收 13 項，V2 通則獨立重算 |
| `docs/fw036/lint_reports/pm_28__power_20260824.md` | lint 後報告 |
