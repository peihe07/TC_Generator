# 10b 下放包 — Phase 2 開工（pilot 批）

裁決見 `10a_rulings.md`（R-U42～R-U45、R-G10）。09 輪核可。
**本輪首次生成 TC。** 生成物落 `generated/`，**不寫回工作簿**（R-U14）。

## 前置（1–3，先辦完才生成）

1. **條文入庫與標記修正**
   R-U42～R-U45、R-G10 逐字追加。
   依 R-U42 改六條之標記；原文一字不改。R-U43 之註記指明 R-C3。

2. **R-U45 落地** — `.gitignore` 加例外使 `data/outline_map.json` 被追蹤
   （先裁後改已授權），列入 `BASELINE.sha256`，`shasum -c` 全綠並附輸出。
   **`git add`／`commit` 不執行** —— 只準備，回報待 Pei 之指令清單。

3. **生成前之組裝自檢** — 逐項回報，不得以「已設定」帶過：
   - spec 內文來源 = `outline_map.json` 之 `pdf_text`（**非 `text`**）
   - 補句表七條之 `must_carry` 於其所屬 outline 生成時**確實注入** prompt
     （回報注入點與其驗證方式）
   - Test Group = `User Profiles`；Test Set = framework §2 八組逐字
   - tc_id = `NR1L-UserProfiles-{NNN}`
   - `specification_reference` 格式依 R-U1（Source ID 字串，非檔名形式）

## Pilot 批（4–6）

4. **取樣 —— 分層，非單一 Test Set**（canon §1.2）
   pilot 之目的為驗規則，不是產量。自 **8 個 Test Set 各取 2 個 leaf**，
   共 **16 leaf**，取樣須含：
   - 至少 1 個 `Service` 之 B 群（設定 → key cycle → 讀回，R-U21）
   - 至少 1 個帶補句表 must_carry 之 outline（9.1／9.3.2／9.8／11.4）
   - 至少 1 個落在 spec `4.1.1`（驗 R-U27 之「可生成但不寫 popup 內文」）
   - 至少 1 個 `PROF-001-01`（驗 R-U39(2) 之 PLP 引用與 3.x 併列）
   取樣清單先回報，**Pei 覆核後才生成**。

5. **R-U39(2) 之前置掃描**（生成前）
   掃全部 180 leaf 之 `pdf_text`，列出凡引用 PLP 表
   （`PLP` / `Profile Linked Preferences`）者。
   **先掃再定，不以假設限縮。** 結果決定哪些 leaf 之
   `specification_reference` 併列 `3.x`。

6. **生成與 lint**
   16 leaf 之 TC 落 `generated/`，逐條跑：
   - `lint_variant_labels.py`（R-U35(c)）
   - 既有 TC lint（欄位、trailing period、雙引號、design method…）
   - lint 全綠**不等於**通過 —— pilot 之覆核為分析層之工作

## 不在本包授權範圍

- **寫回工作簿**（R-U14：x14 DV gate 未立且未實跑）
- 第二批 —— **前批未覆核不得開下批**
- `git add`／`commit`／任何改狀態之 git（R-G5）
- 寫入他 feature 之檔（R-U24／R-U30／R-U44）
- 刪除 `inputs/` 之 spec 副本（R-U17，屬 Pei）

## 上繳

`docs/upstream/10_pilot.md`，更新 `docs/INDEX.md`，
附「本包是否仍有該驗而未驗者」之獨立判斷。
每個比率附分子定義（R-G8）；lint 驗證含範圍向（R-G9）；
清單式分類以餘數驗證（R-G10）；
動作清單與 git 陳述逐項對照（R-G6）。

**16 條 TC 全文須附於上繳包**（或指明其 `generated/` 路徑），
供分析層逐條覆核。pilot 覆核之發現先分類為
defect／style-divergence／note，再決定是否阻塞（canon §1.2）。

## 承前之未決

- **A-UP09 / R-U14** —— DV gate 未立，擋 Phase 6 寫回
- **DR #3**（上游覆蓋缺口）、**DR #4**（PU1087／1088 之 popup 內文）—— 屬 Pei
- **R-U17** —— `inputs/` spec 副本之刪除，屬 Pei
- **N-XF01** —— comfort 孤兒檔，待 Comfort 下次開輪次（R-U44 觸發點）
