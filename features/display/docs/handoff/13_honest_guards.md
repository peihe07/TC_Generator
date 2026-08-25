# 下放包 13 —— 會說謊的警示、綁定範圍收束、剩餘不阻塞工作已見底

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 範圍：Display ＋ 全域一條
- 對應上繳：`features/display/docs/upstream/13_honest_guards.md`
- 前一包：`12_assertions.md`（上繳已覆核，見 §一）
- **Q2／Q3 仍在 Pei 處。本包執畢，不阻塞之工作即告見底 —— 見 §六**

---

## 一、上繳包 12 之覆核

**核可，無退回項。** 三項具名。

### 1.1 A-DM28 —— 一個會說謊的警示，且是自己抓到的

首版實作印出 `NOT updating the expectation`，而**同一次執行之
`write_meta` 仍以實測值重寫 `expected_chars`** —— 訊息說不採納，
程式採納了。

發現方式值得記：**蓄意把期望值改為 `999999` 後連跑兩次，第二次警示
消失。** 若只跑一次，警示會如期出現，測試會 PASS，而守衛實際上是壞的。

執行層之定性採認：

> 前六次是數字錯或聚合錯，這次是**宣稱之行為與實際之行為不一致**。
> 一個會說謊的警示比沒有警示更糟 —— 它讓人以為有守衛。

其一般化提案予以採納並立為全域條文（§四 R-G25），
且**適用範圍即刻擴及其自陳之另兩處**。

### 1.2 §6.1 之「stdout 0 行」

蓄意破壞綁定後執行 `signal_resolution.py`：退出碼 1、
**stdout 0 行**、TSV 未被改寫。

> 守衛若在量測**之後**才擋，檔案已經被寫過了。它擋在進入點，
> 所以什麼都沒發生。

**這是本輪最好的一個量測選擇。** 「退出碼 1」只證明它有擋，
「stdout 0 行 ＋ 檔案未改」才證明它擋在正確的位置。

### 1.3 A-DM27 —— 上輪三項遺漏之真正成因

> **`DECISIONS.new.md` 不是 recon 之全部量測，是其一個子集。**

10 項在 `recon.json` 與／或 `RECON.md` 中都有，只是 DECISIONS 模板不列。
上輪之合併以 `.new.md` 為唯一依據，故那 10 項從未進入對照 ——
**上輪查出的三項與這 10 項是同一成因的兩種表現**。

反向比對 17 項中 recon 漏測 **0**，停止條件 30 未觸發，判定正確。

---

## 二、§8 五項未驗之處置

| # | 項 | 處置 |
|---|---|---|
| 1 | A-DM27 之 10 項未逐項值比對 | 步驟 3（立 R-DM39） |
| 2 | subprocess 啟動成本未量測 | 步驟 5（量測即可，不優化） |
| 3 | `inputs/` 之素材無綁定檢查 | 立 R-DM38（§四）＋ 步驟 4 |
| 4 | `recon_assertions` 是否支援其他 assertion 種類 | **分析層已查明，見 §三** |
| 5 | A-DM28 之一般化未實作 | 立 R-G25（§四）＋ 步驟 2 |

---

## 三、第 4 項之答案 —— 分析層已自 `recon.py` 原始碼查明

執行層問「`run_assertions` 是否支援 `workbook_state`／`column mapping`／
`design_method 詞彙` 三種 assertion」。**不必再花一輪去查，答案在碼裡。**

分析層讀 `scripts/recon.py` 之 `run_assertions()`（下放包 08 §2.3 之
同一次通讀）：其僅取 `cfg.get("recon_assertions")` 之**三個鍵**：

| 鍵 | 檢查對象 | 本 feature 適用性 |
|---|---|---|
| `functional_requirement_count` | leaf 數 | **已宣告**（R-DM36） |
| `distinct_spec_sections` | 引用之相異章節數 | 不適用（本 feature `sections` 為 0） |
| `spec_reference_stem` | 引用之 stem | 不適用（`citation_stems` 為空） |

`workbook_state`、`column mapping`、`design_method 詞彙` 三者
**皆不在支援之列**。要加須修改 `run_assertions()`，屬共用腳本，Tier 2。

**分析層之提案（提交 Pei，與 Q2／Q3 並列，不急）**：
增 `workbook_state` 一種 assertion。理由：本 feature 之 `BLANK` 是
`fill_test_group_set: true`、style authority 走 fallback chain、
「64 列無候選為 (3) 方法界線」等一連串下游判斷之前提；
它若被動過而無人察覺，那一連串判斷全部失去依據。
`column mapping` 與 `design_method 詞彙` 不提案 —— 前者 recon 本就每次
自表頭重解並報 `col_conflicts`，後者為 9 條字串之逐字清單，
以 assertion 表達不如直接比對檔案。

**本輪不動 `recon.py`。** 未獲授權前，此提案只是提案。

---

## 四、裁決條文

```
R-G25（「宣稱不做 X」之測試須連跑兩次 —— 全域）
凡程式之輸出含「不會做 X」「未更新」「不套用」「維持原值」等
**對自身行為之宣稱**者，其測試不得只跑一次。

必測項目二：
(a) 連跑兩次，**第二次仍應出現同一訊息**
(b) 該次執行前後，被宣稱「不會被動」之標的其內容逐字未變

理由：只跑一次時，訊息會如期出現而測試 PASS，但守衛可能同時
做了它宣稱不做的事 —— 下一次執行才會顯現，而那時已經沒有人在看。
**一個會說謊的警示比沒有警示更糟：它讓人以為有守衛。**

實例（上繳 12 §7.1，A-DM28）：`probe_spec_mode.py` 之漂移警示印出
`NOT updating the expectation`，而同一次執行之 `write_meta` 以實測值
重寫了 `expected_chars`。蓄意將期望值改為 `999999` 連跑兩次後，
第二次警示消失，缺陷因此顯現。

本條即刻適用於既有之一切同型宣稱，不待其被懷疑。
```

```
R-DM38（`inputs/` 之素材納入綁定檢查）
R-DM37 之判準為「凡其變動會使既有產出失效之素材，皆應在
`reference:` 節內」。依該判準，`inputs/` 下之四份素材
（037／SYS2／CFTS_020／SYS3）**符合而尚未納入**：

  037    —— leaf 全集、`recon_assertions` 之 8、八條之缺值判定
  SYS2   —— 80 列母體、15 個訊號、13 個值 token、覆蓋對照全部
  CFTS_020 —— spec_mode D 之判讀基準、glossary 13 條之出處
  SYS3   —— glossary 之 DPU 一條

其 sha256 已記於 `data/materials_ledger.tsv`，**而無腳本比對**
（上繳 12 §8 第 3 項自陳）。此即 R-G23 所指之「宣告不等於保護」。

處置：於 `feature.yaml` 之 `reference:` 節增
`a03_report`／`sys2_export`／`cfts_doc`／`sys3_sysad` 四項，
與既有五項同受 `verify_reference_binding.py` 檢查。

**`reference:` 節與 `paths:` 節之分工自此明確**：
`paths:` 記「檔在哪」，`reference:` 記「檔是哪一份」。
同一個檔出現在兩節不是重複，是兩個不同的問題。
```

```
R-DM39（A-DM27 之 10 項須逐項值比對）
A-DM27 所指之 10 項，本輪僅判明其「非 recon 漏測」，
**未比對其值**。判明「有測」與比對「測得相同」是兩件事，
前者不蘊含後者。

10 項為：Missing referenced specs／Header row index／
`feature.yaml` column conflicts／Regen-region segments／
Draft-region disposition／Categorization 欄與分布／
Covered by done region／Parent-child both-leaf duplications／
Priority rubric deviations／Authors present

須自 `recon.json` 與 `RECON.md` 取其值，與 `DECISIONS.md` 及自寫腳本
之對應值逐項比對，結果依上繳 09 §4 之格式列「相符／不符」。

不符者一律停並回報，不得逕以任一方為準（停止條件 20 之延伸）。

理由：上繳 09 §4 之 17 項交叉檢查是本 feature 唯一一次獨立驗證，
而它漏掉了這 10 項 —— 因為它也是以 `.new.md` 為界。
交叉檢查之涵蓋面自身未被檢查過。
```

---

## 五、作業步驟

1. 抄錄 §四三條（`R-G25` 入 `docs/fw036/RULINGS_LEDGER.md`；
   `R-DM38`／`R-DM39` 入 `features/display/RULINGS.md`），
   核對表由腳本產出。

2. **依 R-G25 補測既有之兩處宣稱**（上繳 12 §8 第 5 項自陳）：
   - `verify_reference_binding.py` 之「不更新宣告值」
   - `intake.py` 覆寫之「不套用並警示」（sha256 不符與缺 sha256 兩分支）
   各連跑兩次，並逐項驗 (b)：被宣稱不會被動之標的
   （`feature.yaml`）其內容逐字未變。
   **`intake.py` 為共用腳本，本項為測試不是修改** —— 不得改其任何一行。

3. **依 R-DM39 逐項值比對 10 項**，格式依上繳 09 §4。
   不符者停並回報。

4. **依 R-DM38 將 `inputs/` 四份納入 `reference:`**，
   重跑 `verify_reference_binding.py`，**九項**逐項回報。
   `feature.yaml` 之該節加註 `paths:` 與 `reference:` 之分工。

5. **subprocess 成本量測**（上繳 12 §8 第 2 項）：
   量四支腳本串接前後之實際耗時，各三次取中位數。
   **量測即可，不優化** —— 現況若可接受即記其值作為日後比較之基準。

6. 更新 `docs/INDEX.md`。

---

## 六、本包執畢後之狀態 —— 不阻塞工作見底

本包執畢後，`features/display/` 之待辦僅餘下列各項，**全部依賴 Pei**：

| 待辦 | 依賴 |
|---|---|
| framework 三層（Test Set 分群） | **Q2**（範圍） |
| `req_id` 形態定案 | **Q3** |
| `DECISIONS.md` 簽核 | Q2／Q3 定案後 |
| TC 產出（Phase 4） | 簽核後 |
| `recon_assertions` 增 `workbook_state` | §三之提案，Tier 2 |
| 11 個開放 DR（DR-DM1–DM8 等） | 上游回覆 |
| A-DM10b（leaf → CFTS 條號無 id 橋樑） | 與 `spec_reference` 之 `[PEI]` 同一件事 |

**執行層於本包上繳後不得自行開展任何新工作。** 若無新下放包，
即為等待狀態；等待狀態下不得為了「有事可做」而擴大既有工作之範圍
—— 那會產生無人要求、無人覆核之產出。

---

## 七、停止條件

沿用既有各條（1–32），另加：

33. 步驟 2 之連跑兩次若發現任一處宣稱與行為不符 →
    **停並回報，不自行修正**。`intake.py` 者尤然（共用腳本）。
34. 步驟 3 之逐項比對若任一項不符 → 停並回報，不得逕以任一方為準。
35. 步驟 4 之九項綁定若任一項不符 → 停並回報，不得更新宣告值。

**全部 git 操作屬 Pei。**

---

## 八、上繳包要求（`docs/upstream/13_honest_guards.md`）

1. §四三條之抄錄核對表（腳本產出）
2. R-G25 兩處補測之輸出（各含兩次執行與標的未變之證明）
3. R-DM39 之 10 項逐項比對表
4. `verify_reference_binding.py` 九項輸出
5. subprocess 成本量測
6. **「本包是否仍有該驗而未驗者」之獨立判斷**
7. 建議之 commit 訊息與 pathspec（不執行）

---

## 九、本包產生之新條文清單（自檢表）

| 條號 | 主旨 | 範圍 | 已以可貼區塊出現於 §四 |
|---|---|---|---|
| R-G25 | 「宣稱不做 X」之測試須連跑兩次；含標的未變之驗證 | 全域 | 是 |
| R-DM38 | `inputs/` 四份納入綁定；`paths:` 與 `reference:` 之分工 | Display | 是 |
| R-DM39 | A-DM27 之 10 項須逐項值比對；「有測」不蘊含「測得相同」 | Display | 是 |

三條皆為獨立單一事項。
