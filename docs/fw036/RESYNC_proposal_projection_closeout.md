# Close-out re-sync 提案 — Project instruction

> 產出日期：2026-08-12
> 依據：`features/projection/docs/HANDOFF_phase7_closeout.md` §3
> **提案性質：分析層不自行更新 Project instruction，由 Pei 決定是否併入。**

Project instruction 之 §-rules 為 `docs/runtime/ASPICE_SWE6_AI_Instruction.md` 的
週期性副本。本 feature（FW036 R1L Projection）期間產生之新增內容如下。

---

## A. 必須更正（路徑已失效）

### A-1｜Operating Charter 之 feature entry point 路徑

```diff
- Entry point per feature: `<Feature>HMI/PLAYBOOK.md`
+ Entry point per feature: `features/<feature>/PLAYBOOK.md`
```

**依據**：2026-08-11 之目錄重組（commit `ab490eb` — `features/` + `archive/`
重組）。實測 repo 內：

```
features/amfm/PLAYBOOK.md
features/home/PLAYBOOK.md
features/projection/PLAYBOOK.md
features/sxm/PLAYBOOK.md
```

`<Feature>HMI/PLAYBOOK.md` 於檔案系統中**不存在任何相符者**。

**此為本 feature 開案時即發現而延至 close-out 處理者。**

> 註：`docs/runtime/ASPICE_SWE6_AI_Instruction.md` 全文**不含** `Entry point`
> 或 `PLAYBOOK` 字樣 —— 該句只存在於 Project instruction 本身，故此項僅能由
> Pei 更正，無對應的 repo 檔案 diff。

---

## B. canon 新增（`FEATURE_ONBOARDING.md`，已落檔）

### B-1｜§5a 數字紀律 第 11 ~ 14 條

前十條為本 feature 之前已存在。本 feature 期間新增四條：

| 條 | 內容 | 來源 |
|---|---|---|
| **11** | 檢查項須確認其在該階段確實可能失敗；不可能失敗者標「未實測」，不得標 PASS | A-PJ56 |
| **12** | 抽取式之缺陷不會報錯 —— 少抽表現為「不存在」、多抽表現為「多出無意義項」，皆不觸發例外 | A-PJ65 |
| **13** | 量出來的數字不一定能當規則 —— 母體導出之統計範圍為代理判準，不得凌駕實質判準 | R-P87 / A-PJ68 |
| **14** | 檢查條件要自我完備 —— 寫成「與參照對象在所有可讀屬性上一致」而非「已知的幾項正確」 | A-PJ69 / W-9 |

四條之間有明確關係，建議一併併入而非擇一：

- **11 與 12 互補**：11 說「檢查項可能不會失敗」，12 說「抽取式失敗了也不會說」
- **13 與 12 互補**：12 說抽取式會安靜地錯，13 說量測值會安靜地變成規則
- **14 是 11 的建設性版本**：11 教你識別無效的檢查項，14 教你寫出不會失效的

### B-2｜§5a 條號索引（本輪補，格式性）

**發現**：第 1~10 條原以散文與 bullet 形式書寫、**未編號**，而全案有數十處
「canon §5a 第 N 條」之引用指向它們 —— **這些引用在文件中無法解析**。

第 11~14 條（本 feature 新增）採編號條列，形式與前十條不一致。

**處置**：於 §5a 開頭補一份**條號索引**，把既有的對應關係寫明。
**不改寫原文**，僅補索引，故為無損處置。

| 條 | 內容 | 原形式 |
|---|---|---|
| 1–5 | 列號／計數／門檻／掃描範圍／文字比對 之標明要求 | 五個 bullet |
| 6–10 | 傳染性／詞彙型兩缺陷／不得自我校準／單一來源涵蓋範圍／累計重算 | 五個粗體段 |
| 11–14 | 本 feature 新增 | 編號條列 |

**驗證**：以既有引用逐一回查，對應關係全部成立 ——
「第 2 條」用於計數單位、「第 4 條」用於掃描範圍、「第 5 條」用於大小寫與詞界
（A-PJ37）、「第 9 條」用於單一來源涵蓋範圍（**五次引用，全案最密集**）、
「第 10 條」用於累計數字重算（A-PJ51）。

### B-3｜§7 下放包／上繳包契約

已落檔。本 feature 期間之相關偏差：**A-PJ28 → A-PJ53 → A-PJ62 三代同族** ——
「條文被指名而正文未送達」四次、「整份文件被指名而文件不存在」一次。

處置機制已生效並建議保留：
1. 每包末附「本包產生之新條文清單」，逐條確認以可貼區塊形式出現（A-PJ53）
2. 下放包一律以 `Filesystem:write_file` 寫入
   `features/<feature>/docs/HANDOFF_<phase>.md`，聊天附件僅作副本（A-PJ62）

---

## C. profile 新增（`FW036_R1L_Projection_Profile.md`，已落檔）

本 feature 專屬，**不併入 Project instruction**，此處列出供 close-out 盤點：

| 項 | 內容 |
|---|---|
| §1 `[OVERRIDE]` | `workbook_state = FULL_REFINE`（canon §2 未定義之第五種狀態） |
| §2 `[ADD]` | O-1 ~ O-4 修訂總則 |
| §5 | L-PJ1 ~ L-PJ10（L-PJ11 經 R-P48 不採納） |
| §5a `[OVERRIDE]` | dry-run 檢查表 v4：**D-1 ~ D-11** |
| §5b `[ADD]` | 寫回動作清單 **W-0 ~ W-9** |
| 凍結欄窄口 | **兩處**：R-P12（`Expected Result` 純刪除 6 列）、R-P75（`Remarks` 純附加 30 列） |

### C-1｜可推廣至 canon 者（建議，非本包裁定）

以下三項雖寫在 profile，但其形式與本 feature 無關，建議評估是否上升為 canon：

1. **凍結欄之例外一律為窄口，不得為一般授權**
   形式：白名單 + 固定形式 + 純變更方向（純刪除／純附加）+ 逐列 log。
   兩處窄口獨立設計卻收斂到同一形式，顯示其為通則而非巧合。

2. **列身分須由「凍結欄」與「授權例外」推導，不得列舉**（R-P84）
   依據：同一缺陷發生兩次（A-PJ57 ER 窄口、A-PJ66 Remarks 窄口），
   第一次的修正寫成「排除 ER 這個特例」，所以第二次還會踩。

3. **比對式與量測條件均須單一實作**（R-P49 → R-P65）
   R-P49 只收編了比較條件（regex、詞界、大小寫），量測條件（欄索引、掃描範圍、
   計數單位、列身分）仍分散，導致四項過程缺陷。R-P65 補齊後歸零。

---

## D. framework 新增（`docs/fw036/framework.md`）

Part V（§N.0 ~ §N.9）已落檔 —— Projection 三層框架推導。

| 層 | 內容 |
|---|---|
| Layer 1 | `Projection`（單值） |
| Layer 2 | **16 乾淨叢集 + 1 橫切（`Performance`）+ 1 綑綁（`HMI Display`）** |
| Layer 3 | CFTS085 五位數章節 |
| 軸 | protocol / transport 為 §8.3 之**同層軸**，非層級 |

**雙閘門並存**（R-P31）：結構性閘門（R-P29，跨 Test Set 計數 ≥ 6 即排除，
機器可算）與語意閘門（R-P23／R-P32，邊界須依功能，人工判斷，**明文禁止自動化**）。
兩者互不涵蓋。

---

## E. 建議併入順序

| 序 | 項 | 理由 |
|---|---|---|
| 1 | **A-1 路徑更正** | 現行路徑失效，任何新 feature 開案即受影響 |
| 2 | **B-1 canon §5a 第 11~14 條** | 與既有十條同族，四條互補 |
| 3 | **B-2 條號索引** | 使既有數十處引用可解析；純格式，無損 |
| 4 | C-1 三項評估 | 需判斷是否具跨 feature 普適性，非本包可裁 |

**D 與 C（除 C-1 外）為 feature 專屬，不併入。**
