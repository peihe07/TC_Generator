# 01Z-A4 — 指令集（01Z-A3 六項指派之執行）

分析層 → 執行層。取代 `01Z-A3_review.md` §7 之散文條列。
上繳寫入 `docs/upstream/01Z-A4_corrections.md`。

## R-TM12（分析層自裁，2026-08-20）—— 下放包一律附指令段

```
R-TM12（分析層自裁，2026-08-20）—— 下放包末尾一律附可執行指令段

每一個下放包末尾須有「指令」節，內容為執行層可直接照做之動作：
shell 指令、或逐字之貼入區塊與其插入位置。不得以「執行層下一步」之
散文條列代替 —— 那把「裁決 → 可執行動作」之翻譯工序推回給 Pei。

R-TM7（指令須經實測）之射程限於有 CLI 之指令；檔案編輯、條文登記、
索引更新無 CLI 可查，一律直接寫死逐字內容與插入位置。
不確定 CLI 時之正解是查 argparse，不是省略指令。

依據：00 rev A（無指令）、01（指令錯誤）、01Z-A3（散文條列）三次
同型缺失；01Z-A2（完整指令集）為唯一正確形態。
```

---

## T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

## T1 — `RULINGS.md`：追加兩條裁決

於 `features/time_management/RULINGS.md` 末尾追加，逐字：

```markdown
## R-TM9-A2 — 撤回 R-TM9 之 D5 內容，改綁 A-TM02a

（分析層，2026-08-20。上游包 `docs/handoff/01Z-A3_review.md` §3.2）

R-TM9 及 R-TM9-A1 關於 D5 值之全部內容撤回，包括
「feature 識別段 = Time-and-Date-HMI-V0.1」與前綴段之切分作業。
撤回理由：D5 之語意為「本工作簿所依據之 037 報告之文件識別」，
非 feature 標籤，故不可由 feature 名組成。

證據（交付路徑實測，2026-08-20）：
  Core HMI/HomeHMI/            → FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx
  Core HMI/Menu Bar and AppDrawer/ → FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-HMI-V0.1 STLA 報告.xlsx
  User Profiles/               → FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx
  Time Management/             → 無任何符合該形態之檔案

新規定：
1. D5 之值 = 本 feature 所依據之 037 報告之檔名（去副檔名），逐字照抄。
2. 該值在 A-TM02a（037 身分）裁定前無法取得。D5 維持空白。
3. 空白是可見狀態；指向不存在文件之值不是。任何情況下不得以
   feature 名、spec 標題或類推形態組出一個字串填入（§8.4.1）。
4. A-TM11 之解除條件改為：A-TM02a 裁定 + 037 檔名逐字實測。
   不再綁 Home 之前綴段切分。

R-TM8（test_group = "Time and Date"）不受本條影響 —— 該欄語意為功能
模組名，與 D5 之文件識別語意不同，兩者本不必一致。

## R-TM11 — 驗收條件不得預設 commit 節奏

（分析層，2026-08-20。上游包 `docs/handoff/01Z-A3_review.md` §2）

下放包之驗收條件不得以 `git diff` 之範圍為判準。本專案全部 git 操作屬
Pei，執行層之工作樹持續累積跨往返之未提交更正，故 `git diff` 反映的是
「自上次 commit 以來」而非「本包」。

單行修改之正確驗收方式為：修改前 assert 目標字串存在且唯一、
以 count=1 取代、修改後複查該行。

依據：01Z-A2 T1 之驗收條件不可能成立。與 R-TM7 同族 —— 前者是指令
未經實測，本條是驗收條件未經可行性檢查。

## R-TM12 — 下放包一律附可執行指令段

（分析層，2026-08-20。上游包 `docs/handoff/01Z-A4_command_set.md`）

每一個下放包末尾須有「指令」節，內容為執行層可直接照做之動作：
shell 指令、或逐字之貼入區塊與其插入位置。不得以「執行層下一步」之
散文條列代替。

R-TM7（指令須經實測）之射程限於有 CLI 之指令；檔案編輯、條文登記、
索引更新無 CLI 可查，一律直接寫死逐字內容與插入位置。

依據：00 rev A（無指令）、01（指令錯誤）、01Z-A3（散文條列）三次同型
缺失；01Z-A2 為唯一正確形態。
```

追加後 `RULINGS.md` 之 `## R-TM` 條數應為 **15**（原 12 + 3）。

## T2 — `ANOMALIES.md`：新增 A-TM16

於 `ANOMALIES.md` 之 A-TM15 條之後追加，逐字：

```markdown
## A-TM16 — Home A-H26 之既有定性可能低估

**狀態：PENDING。Tier 2。屬 Home，非本 feature —— 僅登記供 Home owner 覆核。**

Home 之 A-H26 於既有文件中記為「Scope 欄未修正」。依 `docs/handoff/
01Z-A3_review.md` §3 之實測，該欄之語意為 037 文件識別，而 Home 工作簿
之 D5 值為：

    FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-Projection-SWE1HMI-V0.1 STLA 報告

該值指向 AppDrawer-Projection 之 037，即**另一個 feature 的追溯來源**；
且其 `SWE1HMI` 形態不對應交付路徑上任何實存檔名（三個實例一致為 `HMI`）。

若此讀法成立，A-H26 不是標籤筆誤而是追溯來源指錯文件，其嚴重性與既有
記載不同。

證據：交付路徑三個 feature 之 037 檔名形態一致
（`Home-HMI-V0.1` / `AppDrawer-HMI-V0.1` / `PersonalAccount-HMI-V0.1`）。

執行層 01Z 上繳 §3.1 所取得之 D5 `repr()` 原樣，保留為本條之證據，
不因 T3 切分作業作廢而刪除。

本 feature 之處置已由 R-TM9-A2 涵蓋，本條不影響本 feature 之任何動作。
```

## T3 — `ANOMALIES.md`：A-TM14 補條文

於 A-TM14 條文末尾追加一段，逐字：

```markdown
**補充（2026-08-20，01Z 上繳 §2.2）—— 受測物身分亦不可判定**

除基準（Home v2）不存在外，磁碟上另有**兩份同名之 Home 036 複本**：

| | 交付路徑 | `archive/forms_superseded/` |
|---|---|---|
| 檔名 | `…_SWQT_Home_20260809.xlsx` | `…_SWQT_Home_20260809.xlsx`（同名）|
| SHA256 | `469b2f6d346d0b1ddd8c86b597760c60a643b3a6beab2036a358b1e288f6c3df` | `1895fb2a2b44f06c46147e5c24731d2d1adf0f2eea80c7ec6f8900a679f24d72` |
| bytes | 120,639 | 119,885 |
| mtime | 2026-08-19 12:01 | 2026-08-09 22:22 |

`cmp` 報 differ: char 2534, line 3。

故 FORMS.md provenance warning 所述之四項污染，**其受測物為哪一份現已
無從得知**。損害範圍因此擴大：不只基準不可覆驗，被判定受污染者是哪一份
亦不確定。

不得以任一份充當基準 —— 以受測物充當基準即失去比對意義。
```

## T4 — `ANOMALIES.md`：A-TM11 解除條件改寫

於 A-TM11 條文內，將解除條件段落整段換為：

```markdown
**解除條件（2026-08-20 依 R-TM9-A2(4) 改寫）**：

原條件（Home v2 之 D5 前綴段切分）**作廢** —— D5 非 feature 標籤欄，
不可由前綴段組成（R-TM9-A2）。

新條件（兩項均須）：
1. A-TM02a（037 身分）經 Pei 裁定
2. 該 037 之檔名逐字實測，去副檔名後即為 D5 之值

在此之前 D5 維持空白，A-TM11 維持 PENDING。
```

## T5 — `ANOMALIES.md`：索引表 → 16 條

索引表追加一列（置於 A-TM15 之後）：

```markdown
| A-TM16 | Home A-H26 之既有定性可能低估 | PENDING | Tier 2（屬 Home）|
```

並確認 A-TM11 之狀態欄仍為 `PENDING`（不因 T4 改寫而變）。

## T6 — 作廢事項

`01Z-A2` T3 之「切分點提議」作業**全部作廢**，不必再做、不必回報。
已取得之 `C5` / `D5` `repr()` 原樣**保留**，其歸屬由 T2 移至 A-TM16 證據。

**不得**因本次作廢而刪除 `01Z_corrections.md` §3 之任何內容 ——
上繳包是軌跡，不回頭改。

## T7 — 驗證

```bash
grep -c '^## R-TM' features/time_management/RULINGS.md      # 期望 15
grep -c '^## A-TM' features/time_management/ANOMALIES.md    # 期望 16
grep -c '^| A-TM'  features/time_management/ANOMALIES.md    # 期望 16（索引列）
grep -n 'A-TM02a' features/time_management/ANOMALIES.md     # A-TM11 解除條件應命中
```

四項數字不符即回報，不自行調整。

## T8 — 上繳

`docs/upstream/01Z-A4_corrections.md`，僅差異。須含：

1. T7 四項數字
2. T1–T5 之逐項寫入確認（改前／改後，或追加位置）
3. **本包是否仍有該驗而未驗者之獨立判斷**，並明列盤點所用之全集
   —— 依 01Z 上繳 §7.2 之新增全集，含「寫入後複查」一項

## 不得執行者

- 不動 git（不 commit、不 tag）
- 不填 `D5`、不組任何 Scope 值（R-TM9-A2）
- 不援引任何他 feature 樣式（R-TM10-A1 仍 SUSPENDED）
- 不開啟交付路徑之 Home 複本檢查其內容（01Z 上繳 §7.3 第三列之理由成立）
- 不以 openpyxl 存回任何工作簿
- 不跑 `recon.py`（會沖掉 `DECISIONS.md`，A-TM15）

## 本包產生之新條文清單（自檢）

| 編號 | 形態 | 已以可貼區塊呈現 |
|---|---|---|
| R-TM12 | 分析層自裁，下放包一律附指令段 | ✅ 節首 + T1 |
| R-TM9-A2 | 已於 01Z-A3 裁定，本包提供貼入區塊 | ✅ T1 |
| R-TM11 | 已於 01Z-A3 裁定，本包提供貼入區塊 | ✅ T1 |
| A-TM16 | 已於 01Z-A3 登記，本包提供貼入區塊 | ✅ T2 |
