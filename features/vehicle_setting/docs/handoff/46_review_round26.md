# 46 下放包 — R-VS47 可寫性分級、pilot #2 分層抽樣、27 輪指令

分析層寫入，2026-08-22。Pei 指示「都繼續做」——
本包同時出 27 輪指令與 pilot #2 之抽樣設計。

**現況：交付 65 條，穩定核心餘量 1，照常開輪會生不出任何 TC。**
**成因為分析層之 `writable` 判準過嚴，非素材不足。**

---

## 1. R-VS47 —— 可寫性改為分級（本輪唯一新條文）

```
R-VS47（分析層裁定 2026-08-22）
可寫性為**分級**，非二值：

  W0  完全可寫 —— 無未解值
  W1  **部分可寫** —— 有未解值，惟扣除 `PENDING` 步驟後
      仍有 **≥ 2 個可執行步驟**，且**其驗證目標本身不是該未解值**
      → **照常生成**，未解處標 `PENDING: DR-{n}`，
        並於該 TC 標 `dr_dependent = {DR 編號集合}`
  W2  不可寫 —— 扣除後 < 2 個可執行步驟，
      **或其驗證目標本身即為未解值**
      → 移出批次，記 `blocked_pending_dr.json`

`writability.tsv` 之 `writable` 欄由 `yes/no` 改為 `W0/W1/W2`。
`generatable = yes` ⟺ `writable ∈ {W0, W1}` ∧ `delegate ∉ {pending, blocked}`。

W1 之 TC 於其所依 DR 覆後**逐條複檢**（比照 `dr15_exposed` 之機制）。

理由：R-VS17（畫面層 BLOCKED 仍產 TC）與 22 包（`PENDING` 行不計入
§10.5 最低步數，扣除後仍有 ≥2 個可執行步驟者留在批次內）——
**二者之精神皆為「寫得出的部分先寫」**。
而 W-58 之判準為「來源條文含任一未解值 → 不可寫」，
**比上開二者嚴，且該嚴格從未經裁定** ——
其係分析層於 39 包 §2 定 W-58 規格時之預設。

先例：`Stop-StartSystem-004`／`-005` 帶 `PENDING: DR-19` 而
**經 pilot review 放行**（2026-08-22）。W1 即該先例之一般化。
```

**W1 之判準要點在第二個條件**：
`Stop-StartSystem-006` 之驗證目標即 `$EngRun_Stat$` 之四值本身 → **W2**；
而 `-004`／`-005` 之驗證目標為開關之啟用／灰階 → **W1**。

---

## 2. pilot #2 —— 分層抽樣設計（**不要 Pei 讀 57 條**）

65 條中僅 8 條經人工關卡，**57 條未經任何 review**。
pilot #1 於 10 條上抓出三項內容層缺陷，其中 `SwitchLHD/RHD-009` 為
**false pass**（TC 未驗證其需求所主張之事）——
**同型缺陷若累積至交付前才發現，回溯成本數倍。**

```
pilot #2 之抽樣（canon §1.2 之分層取樣；抽法具名）

母體：57 條（batch02 6／batch03 10／batch04_v2 10／batch05 8／
      batch06 9／batch07 7／batch08+09 待 27 輪產出）

分層維度二：
  (a) Layer 2（四層）—— 確保四個 Test Set 皆被檢視
  (b) design_method（Functional Based／State Transition／
      Decision Table／Negative-Invalid／Equivalence Partitioning）
      —— pilot #1 之三項缺陷分屬不同 method，故 method 為有效分層維度

抽樣數：**12 條**（母體 57 之 21%）
抽法：(a)×(b) 之交叉格內各取 1；空格跳過；
      同格多條者取其 reqid 最小者；
      不足 12 時自條數最多之格補足，補足順序依格內條數降冪。

**另加 3 條必檢（非抽樣）**：
  - `dr15_exposed = yes` 之 2 條（`LeftFrontHeatedSeat-014`／
    `RightFrontHeatedSeat-031`）—— 其斷言落在未結 DR 之標的上
  - `duplicate_of` 之 1 對取其一（`HeatedSteeringWheel-021`）
    —— 驗嚴格等價之判定是否正確

**合計 15 條。**

Pei 之判準（同 pilot #1）：逐條分 defect／style-divergence／note，
defect 須改寫後方得放行。
分析層先行逐條讀過並附**建議分類**，Pei 覆核其分類而非從零讀起。
```

**分析層將於 27 輪產物到齊後，出 pilot #2 之 15 條清單與建議分類。**

---

## 3. 27 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/46_review_round26.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/25_regrade.md，六節先留空。
D-2  逐字轉錄 46 包 §1 之 **R-VS47** 入 RULINGS.md。
D-3  `writability.tsv` 之 `writable` 欄改為 W0/W1/W2；
     `generatable.tsv` 依新定義重算。
D-4  依 R-VS35 列兩數。

## 作業（三項，R-VS25）

W-77  **依 R-VS47 重分級**（最高優先 —— 直接決定本輪能否生成）
      對現判 `writable = no` 之 **165 條**逐條分級：
      (1) 列出其未解值之出現位置（procedure 之哪一步驟）
      (2) 判「扣除 PENDING 步驟後是否仍有 ≥2 個可執行步驟」
      (3) 判「其驗證目標是否即該未解值」
      **必列**：W0／W1／W2 三數，及 W1 之逐條清單與其 `dr_dependent`。
      **W1 之條數即可立即恢復之產能。**
      驗收錨點（須可失敗）：
        `Stop-StartSystem-004`／`-005` 須判為 **W1**（其已 pilot PASS）
        `Stop-StartSystem-006` 須判為 **W2**（其驗證目標即未解值）

W-78  **docx 表格抽取**
      現行抽取以段落文字流為之，**表格之列欄關係遺失**。
      改以 `word/document.xml` 之 `<w:tbl>` 保留列欄，重抽 CFTS044。
      **驗收錨點（須可失敗）**：`4859495` 之 `described below` 所指之序列
      須被抽出；現行法抽不到。
      抽出後：
      (1) 列出新增之 (token, 值) 對數，及其使多少 leaf 之未解值獲解
      (2) 新解出者逐筆過 `guard()`（R-VS44′）
      (3) 更新 `writability.tsv` 並重跑 W-77 之分級

W-79  batch10 —— **10 條**
      自 `W0 ∪ W1` ∧ `delegate ∉ {pending, blocked}` 之池選 leaf，
      依逐 Layer 2 輪流；W1 之 TC 須標 `dr_dependent`。
      套 profile ＋ canon §8.7.5 v3 ＋ R-VS43 ＋ Sibling Rows ＋
      無效值優先序；逐條過 `guard()`；
      §9 十七項自檢 ＋ DBC 值表核對。
      **若 W-77／W-78 後之池仍不足 10，取全部並回報其數。**

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
不得再執行型 B 之唯讀搜尋。不得採用他車型 PROXI 表之值。
不得合併 037 之 leaf。
**W1 之未解處一律標 `PENDING: DR-{n}`，不得以任何判準填值。**

## 升級條件

W-77 之 W1 條數 < 20（則產能恢復有限，須另尋路徑）；
W-77 之驗收錨點不可失敗；
W-78 之驗收錨點抽不出 `4859495` 之序列；
W-79 之交付 < 5。
**本輪無必停項。**
```

---

## 4. 待 Pei

| 項 | 狀態 |
|---|---|
| **DR-22′**（79 leaf，是非題） | 待送 —— **單一最大解鎖** |
| DR-21（148 leaf，含重疊）／DR-20／DR-23／DR-8′／DR-24′／DR-18／DR-11 | 待送 |
| **pilot #2** | 分析層於 27 輪產物到齊後出 15 條清單與建議分類 |

**但自 R-VS47 起，不送亦不停產** —— W1 照寫，覆後複檢。

---

## 5. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS47 | 可寫性分三級；W1 照常生成並標 `dr_dependent` | 分析層（本輪額度用畢） |
| pilot #2 抽樣設計 | 分層 12 ＋ 必檢 3 ＝ 15 條；分析層先分類，Pei 覆核 | 分析層 |
