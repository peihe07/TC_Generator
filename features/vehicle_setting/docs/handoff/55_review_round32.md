# 55 下放包 — A-VS101（產物不可重現）、34 輪

分析層寫入，2026-08-22。

**注意**：本輪執行之依據為 52／53 包（32 輪），**54 包之 W-93（SWC 對齊，76 條）
尚未執行** —— 其為 33 輪指令，於本輪之上繳前發出。**34 輪以之為首項。**

---

## 1. A-VS101 —— 交付前必解，理由不是方法潔癖

`writability.tsv` 自 20 輪起為 inline heredoc 逐次修改之產物，
`scripts/` 中無任何腳本可重現之。以現有模組重建之驅動得 82/3/152，
與產物 103/2/132 **逐 leaf 不一致 52 筆**。

**其後果不在數字本身，在交付時之可辯護性**：

FW036 之交付須能回答「237 個 leaf 中，為何 X 條未產 TC」。
該答案現繫於一份**不可自 repo 重現**之表。
稽核時若問「這 94 條為何判 W2」，我方只能出示產物，**無法出示其如何算得**。

**且 R-VS50（引為決策依據時須回查組成）於此失效** ——
組成之回查若基於不可重現之表，回查本身亦不可稽核。

```
R-VS53（產物須可重現，分析層裁定 2026-08-22；本輪唯一新條文）
凡進入交付論述之產物（覆蓋率、可寫性分級、母體計數、
`writability.tsv`／`generatable.tsv` 等），**須可自 repo 之腳本重現**。

具體要求：
(1) 每一份此類產物須有**具名之驅動腳本**於 `scripts/`，
    其輸入僅為 `inputs/` 之素材與 `RULINGS.md` 之條文
(2) 歷輪之裁定（R-VS43／R-VS47／R-VS48′／R-VS49／R-VS51／W-87 等）
    須以**可回放之形式**寫入該驅動，不得只寫進產物
(3) 驅動之輸出與現行產物不一致時，**逐筆列出差異**並判其為
    「驅動缺某條裁定」或「產物含未落條文之調整」
(4) inline heredoc 之一次性修改**不得作為產物之最終來源**

過渡期之處置：現行 `writability.tsv` 之**絕對值標「不可稽核」**，
**可稽核者僅其增量**（本輪之 +33 與 +5）。引用時須連同此限制。
```

**執行層之處置正確**：以受控比較給出增量、以增量法套回產物、
並自陳「絕對值仍不可稽核，可稽核者為增量」。**不掩飾，不調和。**

---

## 2. `guard()` 之誤用 —— 採其建議

`guard(tok, v, "blocked")` 為**靜默直通**，誤用不報錯，致 58 次被誤記為「被攔」。
**由執行層自行發現並更正，未進入交付數字。**

```
分析層裁定（併入 W-94）
`guard()` 改名為 `guard_new_conclusion(tok, value, conclusion)`，
其 `conclusion` 僅接受 `{"resolved", "derivable", "write"}`；
傳入 `"blocked"` 或其他值時 **raise**，不靜默直通。

理由：R-VS44 令其「併入輸出階段」已達成，
**但未令其呼叫方式可驗** —— 一個靜默直通之分支，
其誤用在計數上與正確呼叫不可分辨。
```

---

## 3. 三項未定之處置

| 項 | 處置 |
|---|---|
| **A-VS103** `FR_VS_Cmd_Tlm` 須跨列引入 | **不跨列引入**，執行層正確。「判某值為 typo」與「以對稱側之列補其值域」確為兩事。維持 DR-18 |
| **A-VS104** `_mid` → `_medium` | **不擴充判準**。`mid` 非 `medium` 之前綴（`m-i-d` vs `m-e-d`），亦非其字元子序列之前綴段 —— **其為變母音之縮寫，無結構性判準可依**。併入 DR-18（確認型） |
| §6-3 LID 雙鍵之跨列串鍵風險 | 入 BACKLOG。本輪增量僅取「HIGH 未解而 MID 解得」者，未受其害 |

---

## 4. 34 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/54_swc_alignment.md   ← 33 輪（**未執行**）
  features/vehicle_setting/docs/handoff/55_review_round32.md  ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/30_swc_alignment.md，六節先留空。
D-2  逐字轉錄 54 包 §1 之 **R-VS52**、55 包 §1 之 **R-VS53** 入 RULINGS.md；
     **R-VS41(1) 標「撤回，經 R-VS52 取代」**（原文保留）。
D-3  profile 增 **[OVERRIDE §8.7.5]** 段（54 包 §1 全文）並 cite R-VS52；
     A-VS62 之 [ADD] 段**改寫為 `is sent`**。
D-4  ANOMALIES.md：A-VS104 併入 DR-18；A-VS101 標「待 W-94」。
     依 R-VS35 列兩數。D-6 之骨架對照照做。

## 作業（三項，R-VS25）

W-93  **全批次依 R-VS52 改寫**（最高優先，76 條）
      全文同 54 包 §3 之 W-93，不變。
      **驗收四項須可失敗**；不得順帶改動非訊號書寫之欄位。

W-94  **`writability.tsv` 之驅動化**（R-VS53）
      (1) 補寫 `scripts/writability_driver.py`，輸入僅
          `inputs/` 之素材 ＋ `RULINGS.md` 之條文
      (2) 逐輪回放 R-VS43／R-VS47／R-VS48′／R-VS49／R-VS51 ＋ W-87
      (3) 驗其能否重現 **141/2/94**；不一致者**逐筆列出**並判其為
          「驅動缺某條裁定」或「產物含未落條文之調整」
      (4) `guard()` 改名為 `guard_new_conclusion()`，
          `conclusion` 僅受 `{"resolved","derivable","write"}`，
          其餘 **raise**；**驗收：以 `"blocked"` 呼叫須拋例外**
      **本項之產出即交付時之可辯護性**，不得以「數字對得上」收尾 ——
      須列出驅動與產物之逐筆差異。

W-91  batch13 —— **10 條**，依 R-VS52 之形式撰寫。
      池已備（`generatable = 118`，扣已交付 76，**餘 42**）。
      逐 Layer 2 輪流；逐條過 `guard_new_conclusion()`；
      §9 十七項自檢 ＋ DBC 值表核對。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
**不得跨列引入 `FR_VS_Cmd_Tlm` 之值域**（A-VS103）。
**不得擴充 R-VS48(a) 以涵蓋 `_mid`**（A-VS104）。
不得以 R-VS51 解掉 DR-15 之標的。

## 升級條件

W-93 之驗收四項有任一不可失敗；
W-94(3) 之逐筆差異 > 30（則歷輪裁定之落條文有系統性缺漏）；
W-94(4) 之 `"blocked"` 呼叫未拋例外；
W-91 交付 < 5。
```

---

## 5. 待 Pei

| 項 | 狀態 |
|---|---|
| **DR-21**（137 leaf）／DR-17／DR-24′／DR-18／DR-11 | 待送 |
| DR-20／DR-23／DR-8′ | 待送 |
| DR-15 | 待覆（32 輪已補架構欄組之觀察段） |

**條文面無待裁項。**

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS53 | 交付論述之產物須可自 repo 重現；歷輪裁定須可回放 | 分析層（本輪額度用畢） |
| `guard()` 改名 | `"blocked"` 呼叫改為 raise，不靜默直通 | 分析層（併入 W-94） |
