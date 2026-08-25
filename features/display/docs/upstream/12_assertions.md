# 上繳包 12 —— 三項分歧處置、assertion 機器化、綁定串接

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/12_assertions.md`
- 結果：**步驟 1–8 全數執行；三十二條停止條件全未觸發**
- 全部 git 操作屬 Pei —— §9 只備妥訊息與 pathspec，未執行

---

## 1. §四三條之抄錄核對表（步驟 1，腳本產出）

## 抄錄核對表 — 12_assertions.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 38 | R-DM36 | `features/display/RULINGS.md` | 537 | `2510dd0c68848316` | 是 |
| 39 | R-DM37 | `features/display/RULINGS.md` | 428 | `bc80baabe1f50e26` | 是 |
| — | R-G24 | `docs/fw036/RULINGS_LEDGER.md` | 556 | `6651aa3f59c5f458` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **39** 個，與各下放包原檔逐字元比對 **全數相符**（39 vs 39）。

---

## 2. 三項分歧之處置與複驗（步驟 2）

### 2.1 處置

| # | 項 | 上輪合併後 | 本輪 | 依據 |
|---|---|---|---|---|
| 1 | `ruled-constant assertions` | **缺席** | `[AUTO]` **1 checked, 1 PASS, 0 FAIL** | R-DM36 |
| 2 | `Test Set table (Part N)` | `[PROPOSED]` | **`[PEI]`** | R-G24 |
| 3 | `profile [OVERRIDE] clauses` | `[PROPOSED]` | **`[PEI]`** | R-G24 |

第 2、3 項於該兩項下加註其 02 輪之原標記與更正依據（R-TM13 不刪除），
並明記**機器是對的**：`FEATURE_ONBOARDING` 已定該二者屬 Tier 2。

`DECISIONS.md` 之合併紀錄增「追加處置」表（第 10–12 項），並載明
R-G24 與 R-DM32 之關係：**兩條方向相反而判準一致 —— 寧可多問一個問題。**

### 2.2 複驗：recon 之 24 項全部有對應

```
### 正向：recon 之 24 項在合併檔中是否有對應
  無對應者: 0 （無）

### marker 一致性（recon vs 合併檔）
  spec_reference                     recon=PROPOSED  合併檔=PEI
  marker 不一致者: 1
```

僅餘之一項不一致為 `spec_reference`，**係刻意** ——
R-DM32（機器不得降格）與 R-G24（取較嚴者）**兩條皆判取 `[PEI]`**。

---

## 3. 反向比對之逐項判定（步驟 3）—— **停止條件 30 未觸發**

合併檔 42 個項目行中，**17 項** recon 側無同名項。逐項以
`recon.json` 之鍵與 `RECON.md` 之內文判其性質：

| 判定 | 項數 | 項 |
|---|---|---|
| **recon 有測，只是未列入 `DECISIONS.new.md`** | **10** | Missing referenced specs／Header row index／`feature.yaml` column conflicts／Regen-region segments／Draft-region disposition／Categorization 欄與分布／Covered by done region／Parent-child both-leaf duplications／Priority rubric deviations／Authors present |
| 自測獨有（recon 不涉及此概念） | 7 | Spec release/version pinned／SYS2 覆蓋落差／Granularity precedent／Known scope carve-outs／Contested attributions／Model assignment per batch／BLOCKED batches at start |
| **recon 漏測** | **0** | —— |

**無任何一項為 recon 漏測，故停止條件 30 未觸發。**

### 3.1 但第一類值得登記 —— A-DM27

那 10 項在 `recon.json` 與／或 `RECON.md` 中**都有**，
只是 `DECISIONS.new.md` 之模板不列它們。即：

> **`DECISIONS.new.md` 不是 recon 之全部量測，是其一個子集。**

上輪之合併以 `.new.md` 為唯一依據，因此那 10 項從未進入對照 ——
**上輪查出的三項遺漏，與這 10 項是同一個成因的兩種表現**。

本 feature 之對照此後一律兼看 `RECON.md` 與 `recon.json`。
是否擴充 recon 之 DECISIONS 模板屬全域 Tier 2，未代處置。

### 3.2 一項解析瑕疵之記明

我的反向比對式把說明段落中之 `` `[PROPOSED: value — rationale]` ``
一行也當成項目行抓進來（因其形似 `- <label>: [MARKER…]`）。
已於判定表中剔除，**但該式若用於其他 feature 會重犯**。
未一般化為工具，僅記於此。

---

## 4. `recon_assertions` 宣告後之 Assertions 節（步驟 4）

`feature.yaml`：

```yaml
recon_assertions:
  functional_requirement_count: 8
```

`RECON.md`：

```
## Assertions — ruled constants, checked mechanically
- PASS — leaf count == Functional Requirement rows: expected `8`, measured `8`
  — categorization distribution: {'Functional Requirement': 8}; the banned
  id-suffix criterion would have selected 0 (8 parent-shaped requirements dropped)

**0 failed / 1 checked.**
```

**停止條件 32 未觸發**（非 FAIL）。

### 4.1 PASS 之意義（步驟 4 明文要求寫明）

它證明的是「**037 之 leaf 數仍為 8**」，**不是**「8 這個數字是對的」。

8 之正確性來自上繳 09 §4 第 2 項之交叉檢查（recon 與自寫腳本兩側相符）；
assertion 只保證它此後不會**無聲**改變。兩者是不同的保證，
把後者當成前者，就是把「沒有人動過」誤讀成「當初是對的」。

### 4.2 assertion 之附註揭露一件事

`recon.py` 之 note 印出：**被禁用之 id-suffix 判準會選出 0 個 leaf
（8 個 parent-shaped requirements 全被丟掉）**。

即：若本 feature 當初採 id-suffix 判準，leaf 數會是 **0** 而非 8 ——
而 0 個 leaf 與「這個 feature 已經做完」在輸出上難以分辨。
`FORMS.md` 對 AM/FM 記過同型情形（「an empty leaf list is
indistinguishable from a finished feature」）。本 feature 未採該判準，
此處只是第一次看見它會有多錯。

### 4.3 Q2 之連動已記入 `feature.yaml`

宣告處加註：**Q2 若裁為選項 B 或 C 而 leaf 母體改變，須改宣告值並記其
理由；靜默更新 assertion 等同取消該 assertion。**

---

## 5. `verify_reference_binding.py` 五項輸出（步驟 5，R-DM37）

```
# reference binding check (R-G23)
feature.yaml: /Users/peihe/Work_Projects/TC_Generator/features/display/feature.yaml
entries: 5

| key | file | declared | actual | verdict |
|---|---|---|---|---|
| dbc_b | `PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3db62ac9f…` | `46cb73f3db62ac9f…` | MATCH |
| dbc_fd | `PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf3e670d71…` | `2a86c4bf3e670d71…` | MATCH |
| lid | `Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679c706cd45…` | `a01e1679c706cd45…` | MATCH |
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3d58d…` | `e7c2020f01c3d58d…` | MATCH |
| workbook_master | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` | `6372fb6be02f48dc…` | `6372fb6be02f48dc…` | MATCH |

**5 of 5 match.**
```

036 母本已納入（`workbook_master`），**5/5 相符**。

R-DM37 之一般化判準已記於 `feature.yaml` 之該節註解：
**「凡其變動會使既有產出失效之素材，皆應在 `reference:` 節內；
判準不是它是不是參考資料庫，是它變了以後我們的東西還對不對。」**

---

## 6. 串接後四支腳本之列數（步驟 6）—— **停止條件 31 未觸發**

`signal_resolution.py`／`dbc_probe.py`／`proxi_candidates.py`／
`lid_version_diff.py` 四支之 `main()` 進入點加入 `_verify_bindings()`。

| TSV | 串接前 | 串接後 |
|---|---|---|
| `signal_resolution.tsv` | 26 | **26** |
| `proxi_candidates.tsv` | 446 | **446** |
| `lid_v178_vs_v176.tsv` | 2548 | **2548** |
| `sys2_heading_tree.tsv` | 45 | **45** |

（`sys2_heading_tree.py` 不讀參考素材，未串接；其列數併列以示未受影響。）

### 6.1 守衛之實測

蓄意將 `dbc_b` 之宣告值改為 `deadbeef…` 後執行 `signal_resolution.py`：

| 項 | 實測 |
|---|---|
| 退出碼 | **1** |
| stdout 行數 | **0** —— 未產出任何量測 |
| `signal_resolution.tsv` 是否被改寫 | **否**（`git status` 0 行） |
| 訊息 | 印出宣告值與實際值之**全碼**，並明寫不得更新宣告值 |

狀態已還原並複驗（5/5 相符）。

> 「stdout 0 行」是這次特別要看的：守衛若在量測**之後**才擋，
> 檔案已經被寫過了。它擋在進入點，所以什麼都沒發生。

---

## 7. `spec_text_layer` 期望值比對（步驟 7）

sidecar 新增 `expected_chars` 區塊，記三個抽取器之當期值。
`probe_spec_mode.py` 每次執行比對現算值與其，不符即印警示並列兩值。

### 7.1 一項自查出之缺陷 —— 警示曾與其自身行為相反（A-DM28）

首版實作**印出「NOT updating the expectation」，而同一次執行之
`write_meta` 仍以實測值重寫 `expected_chars`** —— 訊息說不採納，
程式卻採納了。

發現方式：蓄意把期望值改為 `999999` 後**連跑兩次**，第二次警示消失。

修正為 `{**現算, **既有}`（既有鍵一律保留，只有從未見過之抽取器才新增）。
修正後之實測：

```
--- 第一次執行 ---
WARNING: spec text layer drift — pymupdf: sidecar records 999999,
         this run measured 854333. NOT updating the expectation
--- 第二次執行（期望值應仍為 999999，警示應再現）---
WARNING: spec text layer drift — pymupdf: sidecar records 999999,
         this run measured 854333. NOT updating the expectation
sidecar 之期望值: 999999
```

**連跑兩次警示皆出現、期望值維持不變。** 狀態已還原。

這是本 feature 第七次同型缺陷，但**形態是新的**：前六次是數字錯或
聚合錯，這次是**宣稱之行為與實際之行為不一致**。
一個會說謊的警示比沒有警示更糟 —— 它讓人以為有守衛。

一般化提案（Tier 2，未實作）：凡輸出中含「不會做 X」之宣稱者，
其測試須含「連跑兩次，第二次仍應出現同一訊息」。

---

## 8. 「本包是否仍有該驗而未驗者」—— 執行層之獨立判斷

**有，共 5 項。**

1. **A-DM27 所指之 10 項從未進入任何對照。** 本輪判明它們「recon 有測
   而未列入 `.new.md`」，但**沒有逐項比對其值與我的值是否相符** ——
   只確認了「不是漏測」。那 10 項之交叉檢查仍是空的。
2. **`_verify_bindings()` 以 subprocess 呼叫，每支腳本多一次 Python
   啟動。** 對 `lid_version_diff.py`（讀兩份 2,600 列之 xlsx）不明顯，
   但**若日後有逐 leaf 迴圈呼叫這些腳本，成本會變成 N 倍**。未量測其
   實際耗時。
3. **`sys2_heading_tree.py` 未串接綁定檢查**，理由是它只讀 SYS2
   （`inputs/` 內之複本，不在 `reference:` 節）。但 **SYS2 之複本本身
   沒有任何綁定檢查** —— `materials_ledger.tsv` 記了它的 sha256，
   而沒有腳本在比對。
4. **`recon_assertions` 只宣告了一項。** `workbook_state == BLANK`、
   `column mapping 15 鍵`、`design_method 詞彙 9 條` 三者同樣是經交叉
   檢查確立且被反覆引用之常數，`recon.py` 之 `run_assertions` **是否
   支援這三種 assertion 未查**（我只看了 `functional_requirement_count`
   與另兩個被我排除的鍵）。
5. **A-DM28 之一般化提案未實作。** 「連跑兩次」之測試目前只做在
   `spec_text_layer` 一處；本 feature 另有兩處含「不會做 X」之宣稱
   （`verify_reference_binding.py` 之「不更新宣告值」、
   `intake.py` 覆寫之「不套用並警示」），**兩者皆只跑過一次**。

另記本輪**已驗而下放包未要求**者：守衛之 stdout 0 行與 TSV 未改寫；
A-DM28 之連跑兩次驗證；assertion note 所揭露之「id-suffix 判準會選出
0 個 leaf」；反向比對式之解析瑕疵（§3.2）。

---

## 9. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(display): settle marker conflicts, machine-check ruled constants

- R-DM36/37 + R-G24 verbatim (3/3, 39/39 cumulative)
- the three items the round-10 merge missed are settled: assertions
  restored and filled in, Test Set table and profile [OVERRIDE] raised to
  [PEI] per R-G24. The machine was right and my round-02 [PROPOSED] was
  wrong - the mirror image of recon trying to demote spec_reference
- re-verification: all 24 recon items now have a counterpart; the one
  remaining marker difference is spec_reference, which both R-DM32 and
  R-G24 resolve to [PEI]
- reverse comparison: of 17 items only in my file, 10 are measured by
  recon but absent from DECISIONS.new.md and 7 are concepts recon has no
  notion of. None is a recon miss, so stop condition 30 does not fire.
  A-DM27 records that DECISIONS.new.md is a subset of what recon measures
- recon_assertions declares functional_requirement_count: 8; PASS means
  the count has not changed, not that 8 is correct
- 036 master joins reference: (R-DM37); 5 of 5 bindings match, and the
  check is now called at the entry point of the four scripts that read
  reference material. Breaking a binding gives exit 1, zero stdout, and
  an unmodified TSV
- A-DM28: my own drift warning said 'NOT updating the expectation' while
  the same run rewrote it. Caught by running twice. Fixed and verified by
  running twice again
```

pathspec：

```
git add docs/fw036/RULINGS_LEDGER.md \
        features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/DECISIONS.md \
        features/display/DECISIONS.new.md \
        features/display/DECISIONS.new.2026-08-25b.md \
        features/display/RECON.md \
        features/display/feature.yaml \
        features/display/scripts/ \
        features/display/data/ \
        features/display/docs/
```

**`DECISIONS.md` 本輪重新帶入**（三項分歧已依裁定處置）。
共用 `scripts/`、`forms/`、`.gitignore` 未動。
