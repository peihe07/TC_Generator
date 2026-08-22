# 54 下放包 — 依 SWC 0708 交付本對齊書寫形式（R-VS52）、33 輪

分析層寫入，2026-08-22。**Pei 裁定：依交付本。**

---

## 1. 裁決正文（執行層逐字轉錄入 `RULINGS.md`）

```
R-VS52（Pei 2026-08-22）
本 feature 之訊號書寫形式，**依 SWC 0708 交付本**
（`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/SWC/
  FM-WI-FSM-036-A01 …SWQT_SWC_20260708.xlsx`，286 條、284 條含 CAN 步驟）
之實際樣式，**不依 canon §8.7.5 v3**。

**(1) 送出型步驟**
    procedure：`Send CAN: <MESSAGE>.<Signal> = <raw> (<label>)`
    ER       ：`<MESSAGE>.<Signal> = <raw> (<label>) is sent`
               必要時附時機（交付本用 `during press window`／`after release`）
    **訊號名不加 `$` 包夾**（交付本 `$MSG.Sig$` 形態命中 0）

**(2) 讀取型步驟**
    procedure：`Read <對象> and record as <變數名>`
    ER       ：`<變數名> is recorded`；比較步驟之 ER 用
               `<變數名> = <期望>` 或 `<變數名A> = <變數名B> …`

**(3) 保持型步驟**
    `Hold for <t>` **自成一步**，ER 為 `The signal is held for <t>`

**(4) baseline 比較採具名變數**（交付本：`Vol_initial`／`Vol_after`），
    **不用「the same as recorded in step N」**

**推翻之條文**：
  R-VS41(1)（採 canon §8.7.5 v3 之 `$<MESSAGE>.<Signal>$` 形式）—— **撤回**
  A-VS62 之 (a) 認可（`is registered without a bus error`）—— **撤回**
  R-VS41(2)(3)(4) 不變（網段入 Pre-Condition／spec_ref 逐行／canon 優先之通則）

**canon 優先之通則（R-VS41(4)）於本項之例外依據**：
canon §0 明文「a feature profile's cited override wins over the generic rule
here」。本條寫入 `FW036_R1L_VehicleSetting_Profile.md` 之 [OVERRIDE §8.7.5] 段
並 cite 之，即取得該例外之資格。

**理由**：訊號書寫慣例專由 Pei 之交付本推導；canon §8.7.5 v3 之修訂
（2026-08-21，time_management 之下放包 17）晚於 SWC 0708 交付（2026-07-08），
惟本 feature 之交付物須與 SWC 交付本外觀一致 —— 該一致性屬交付形式，Pei 裁定。

**影響**：已交付 **76 條**之 procedure 與 expected_result **全數改寫**。
```

---

## 2. 改寫之規模與其可驗性

| 項 | 值 |
|---|---:|
| 已交付 TC | **76** |
| 受影響之批次 | `batch01_v3`／`02`／`03`／`04_v2`／`05`／`06`／`07`／`08`／`09`／`10`／`11` |
| 改寫類型 | (a) `$MSG.Sig$` → `MSG.Sig` 去 `$`；(b) `Send the signal X` → `Send CAN: X`；(c) ER `is registered without a bus error` → `is sent`；(d) baseline 改具名變數 |

**(a)(b)(c) 為機械替換，(d) 須逐條改寫**（其涉及 procedure 與 ER 之對應）。

**驗收（須可失敗）**：
- 全批次掃 `\$[A-Z0-9_]+\.` → **須為 0**
- 全批次掃 `is registered without a bus error` → **須為 0**
- 全批次掃 `Send CAN: ` 之出現數 ≥ 原 `Send the signal` 之出現數
- 隨機抽 3 條與交付本之對應樣式**並列比對**

---

## 3. 33 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/52_review_round31.md   ← 32 輪作業（未執行）
  features/vehicle_setting/docs/handoff/54_swc_alignment.md    ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/29_swc_alignment.md，六節先留空。
D-2  逐字轉錄 52 包 §1 之 **R-VS51** 與 54 包 §1 之 **R-VS52** 入 RULINGS.md；
     **R-VS20 加註「排除清單經 R-VS19″(a) 縮限」**；
     **R-VS41(1) 標「撤回，經 R-VS52 取代」**（原文保留）。
D-3  profile 增 **[OVERRIDE §8.7.5]** 段（54 包 §1 全文）並 cite R-VS52；
     A-VS62 之 [ADD] 段**改寫為 `is sent`**（53 包 §2 之 (a) 撤回）。
D-4  `DATA_REQUESTS.md`：DR-15 補入 52 包 §2 之架構欄組觀察段（不改待覆狀態）；
     A-VS97 併入 DR-18。
D-5  ANOMALIES.md：A-VS98 依 R-VS51 關閉；**A-VS62 改標「撤回並以 R-VS52 取代」**。
     依 R-VS35 列兩數。
D-6  本輪結束前以骨架 ⬜／✅ 對照各節實際內容，空節而標 ✅ 者列為不一致。

## 作業（三項，R-VS25）

W-93  **全批次依 R-VS52 改寫**（最高優先，76 條）
      (1) 機械替換 (a)(b)(c)；(d) baseline 具名變數逐條改寫
      (2) 各批次產 `_v{n+1}`，**原版保留不刪**
      (3) 驗收四項（54 包 §2）逐項列出，**須可失敗**
      (4) 重跑 §9 十七項自檢 ＋ DBC 值表逐字核對
      **不得順帶改動 test_item／pre_conditions／spec_reference 等其他欄**
      —— 其變動須單獨具名

W-90  **依 R-VS51 重跑分級**（32 輪未執行）
      全文同 52 包 §4 之 W-90，不變。
      **必列**：因 R-VS51 而由 W2 轉出者之條數，及其中被 `guard()` 攔下者之條數。

W-91  batch13 —— **10 條**，依 R-VS52 之形式撰寫。
      自 W-90 後之池選 leaf，逐 Layer 2 輪流；逐條過 `guard()`；
      §9 十七項自檢 ＋ DBC 值表核對。池不足時取全部並回報。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
**不得以 R-VS51 解掉 DR-15 之標的**（R-VS44 優先）。
**W-93 不得順帶改動非訊號書寫之欄位。**

## 升級條件

W-93 之驗收四項有任一不可失敗；
W-93 改寫後 §9 出現新違規；
W-90 之轉出數 < 20，或 DR-15 之 token 有未被攔下者；
W-91 交付 < 5。
```

---

## 4. 待 Pei

| 項 | 狀態 |
|---|---|
| **DR-21**（137 leaf）／DR-17／DR-24′／DR-18／DR-11（型 A） | 待送 |
| DR-20／DR-23／DR-8′（型 B） | 待送 |
| DR-15 | 待覆 |

**條文面無待裁項。**

---

## 5. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS52 | 訊號書寫依 SWC 0708 交付本；撤回 R-VS41(1) 與 A-VS62 之 (a) | **Pei** |
