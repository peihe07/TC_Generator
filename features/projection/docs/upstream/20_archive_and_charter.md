# 上繳包 20 — 封存規範 + Operating Charter 修訂

> 交付對象：分析層（Claude Project）
> 對應下放包：[`handoff/20_archive_and_charter.md`](../handoff/20_archive_and_charter.md)
> 日期：2026-08-13
> **R-P95 首次適用**——本包為第一份落檔之上繳包。
> 結果：**PASS**（三項新發現，見 §6）

---

## 0. 執行摘要

§5 七步全數執行完畢。

| 步 | 動作 | 結果 |
|---|---|---|
| 1 | 建立 `handoff/` `upstream/` `reports/` | 完成 |
| 2 | 搬移既有 19 檔 | 完成，19/19 雜湊不變 |
| 3 | 建立 `INDEX.md`（01–20 全列） | 完成 |
| 4 | 建立 `docs/runtime/OPERATING_CHARTER.md` | 完成，逐字元等同 §4 fence |
| 5 | 串接產生 `docs/runtime/PROJECT_INSTRUCTION.md` | 完成，第二段雜湊相同 |
| 6 | R-P95 / R-P96 / R-P97 → `DECISIONS.md §0.27` | 完成 |
| 7 | 本包寫入 `upstream/20_archive_and_charter.md` | 本檔 |

**Pei 要的路徑**：

```
/Users/peihe/Work_Projects/TC_Generator/docs/runtime/PROJECT_INSTRUCTION.md
```

680 行。整檔可直接全選貼回 Claude Project 設定。

**不 commit。** git 狀態見 §5。

---

## 1. 搬移前後之檔案清單與雜湊比對（§6 第 1 項）

**量測條件**：`shasum -a 256`，對 `features/projection/docs/` 下之 `*.md`
逐檔計算；搬移以 `mv` 執行（`git mv` 不適用——其中 2 檔未追蹤）。
搬移前 19 檔，搬移後 19 檔（11 於 `handoff/`，8 於 `reports/`）。
比對方式為**雜湊多重集合逐一 `diff`**，非目視。

### 1.1 → `handoff/`（11 檔）

| 新檔名 | 原檔名 | SHA256 | 判定 |
|---|---|---|---|
| `10_phase7_writeback.md` | `HANDOFF_phase7_writeback.md` | `4f8e2329…` | 不變 |
| `11_dr14_disposition.md` | `HANDOFF_dr14_disposition.md` | `75ab9587…` | 不變 |
| `12_phase7_step6_conditions.md` | `HANDOFF_phase7_step6_conditions.md` | `6dd6840c…` | 不變 |
| `13_phase7_stepF_conditions.md` | `HANDOFF_phase7_stepF_conditions.md` | `7e284662…` | 不變 |
| `14_apj69_rerun.md` | `HANDOFF_apj69_rerun.md` | `66b93f2b…` | 不變 |
| `15_phase7_closeout.md` | `HANDOFF_phase7_closeout.md` | `5011340d…` | 不變 |
| `16_closeout_disposition.md` | `HANDOFF_closeout_disposition.md` | `9f86cefa…` | 不變 |
| `17_delivery_precheck.md` | `HANDOFF_delivery_precheck.md` | `4d3618d3…` | 不變 |
| `18_delivery_execute.md` | `HANDOFF_delivery_execute.md` | `74f0bc84…` | 不變 |
| `19_sidecar_policy.md` | `HANDOFF_sidecar_policy.md` | `1057c312…` | 不變 |
| `20_archive_and_charter.md` | `HANDOFF_archive_and_charter.md` | `1fc0f230…` | 不變 |

### 1.2 → `reports/`（8 檔）

| 檔名（未改） | SHA256 | 判定 |
|---|---|---|
| `dryrun_report.md` | `f8135445…` | 不變 |
| `dryrun_v2_report.md` | `31caf61a…` | 不變 |
| `dryrun_v3_report.md` | `dd8e78b9…` | 不變 |
| `phase7_step1_5_report.md` | `65a69839…` | 不變 |
| `phase7_step_a_e_report.md` | `897ddfaf…` | 不變 |
| `phase7_delivery_report.md` | `d74d214b…` | 不變 |
| `git_inventory_closeout.md` | `59afa00f…` | 不變 |
| `closeout_pending_items.md` | `b7f39956…` | 不變 |

### 1.3 判定

```
diff <(搬移前 19 雜湊 | sort) <(搬移後 19 雜湊 | sort)  →  無差異
```

**19/19 逐字元不變，檔數不變，無新增無遺失。**

### 1.4 §2 之「18 檔」與實測 19 檔

下放包 §2 述「現有 18 檔」。實測搬移前為 **19** 檔。
差額為下放包 20 自身（`HANDOFF_archive_and_charter.md`，於 §2 表中列為 20 號）。
即 18 = 既有 + 1 = 本包。**非缺陷**，僅計數口徑差異，記錄以免後續對不上。

---

## 2. `INDEX.md`（§6 第 2 項）

路徑：`features/projection/docs/INDEX.md`。全文見該檔，此處不轉錄
（R-P97 之同型理由：轉錄會漂移）。

### 2.1 結構

依 R-P96 之八欄，01–20 共 20 列。

### 2.2 可填與不可填

| 範圍 | 下放 | 上繳 | 裁決 | 異常 | 結果 |
|---|---|---|---|---|---|
| 01–09 | 未落檔 | 未落檔 | 部分（推得） | 不可填 | 不可填 |
| 10–19 | 路徑 | 未落檔 | **實錄** | **實錄** | 不可填 |
| 20 | 路徑 | 路徑 | 實錄 | 實錄 | PASS |

**10–19 之裁決／異常為實錄**，來源為各下放包 §「本包產生之新條文清單」，
非推得。R-P67 起逐包歸屬有直接紀錄。

**01–09 之裁決為推得**，以 `DECISIONS.md` 之 `^## 0` 節標題（共 27 列）
與 §2 之 slug 逐字比對。命中 5 列（01/02/03/05/09），未命中 4 列（04/06/07/08）。
推導方法與量測條件已寫入 `INDEX.md` §2，並標明**不具權威性**。
`R-P1` ~ `R-P66` 全數落於 §0 ~ §0.19，逐包歸屬僅部分可還原。

**「結果」欄 01–19 全部不可填。** 理由：結果之權威紀錄本應在上繳包，
而 01–19 之上繳包全部未落檔——**這正是 R-P95 所補正之缺口，其代價此刻具體化**。
不重建（canon §5a 第十五條）。

### 2.3 `reports/` 與 NN 之對應未記錄

8 份報告與往返編號之對應無紀錄，同屬上述缺口。已於 `INDEX.md` §3 標明，
並定自 NN=20 起由上繳包指向其報告。

---

## 3. `docs/runtime/OPERATING_CHARTER.md` 建立確認（§6 第 3 項）

**建立方式**：自 `handoff/20_archive_and_charter.md` 第 119–191 行
（§4 之 ```` ```markdown ```` fence 內容）**以 `sed` 範圍擷取**，
未經任何轉錄或編輯。73 行。

| 比對 | SHA256 | 判定 |
|---|---|---|
| `OPERATING_CHARTER.md` | `2b02e588…` | — |
| 下放包 §4 fence（L119–191） | `2b02e588…` | **逐字元相同** |

### 3.1 一處格式瑕疵，未修（見 §6.3）

第 11 行為 `-往返索引：features/<feature>/docs/INDEX.md`——
`-` 與文字之間**缺空格**，markdown 不會渲染為清單項。
上下 5 行皆為 `- ` 開頭之正常清單項。

**未修**：擷取須逐字元等同來源，改一個空格即破壞 §3 之雜湊證明，
且 Charter 文字屬分析層。留待分析層於下次 re-sync 修正。

---

## 4. R-P95 / R-P96 / R-P97 落檔確認（§6 第 4 項）

`features/projection/DECISIONS.md` 新增 **§0.27**，位於 §0.26 之後、§1 Intake 之前。
三條均以逐字區塊落檔。

| 條文 | 落檔 | 附加 |
|---|---|---|
| R-P95 | §0.27 逐字 | 首次適用之路徑；01–19 不重建之註記 |
| R-P96 | §0.27 逐字 | 含八欄表頭；`INDEX.md` 建立確認 |
| R-P97 | §0.27 逐字 | **串接命令**（可重跑、冪等）+ 2026-08-13 三項雜湊實測 |

> **註**：下放包 §7 之自檢表僅列 R-P95 / R-P96，漏列 R-P97。
> 依 §5 第 6 步（明載三條）執行。已登記為 **A-PJ77**，見 §6.2。

### 4.1 R-P97 之串接與驗證（§5 第 5 步）

```sh
cd docs/runtime
{ cat OPERATING_CHARTER.md; printf '\n---\n\n'; cat ASPICE_SWE6_AI_Instruction.md; } \
  > PROJECT_INSTRUCTION.md
```

**結構**：680 行 = 73（Charter）+ 3（空行 / `---` / 空行）+ 604（ASPICE §0–§13）。
第二段自第 77 行 `## 0. Purpose` 起至 EOF。

**驗證**（以雜湊，不以目視）：

| # | 比對 | SHA256 | 判定 |
|---|---|---|---|
| 1 | `PROJECT_INSTRUCTION.md` L1–73 vs `OPERATING_CHARTER.md` | `2b02e588…` | 相同 |
| 2 | `OPERATING_CHARTER.md` vs 下放包 §4 fence | `2b02e588…` | 相同 |
| 3 | `PROJECT_INSTRUCTION.md` L77–EOF vs `ASPICE_SWE6_AI_Instruction.md` | `fa9833ae…` | **相同** |

第 3 項為 R-P97 明定之驗證。第 1、2 項為加驗——R-P97 只要求驗第二段，
但第一段同樣是串接產物，同樣可能漂移；一併驗證成本為零。

`PROJECT_INSTRUCTION.md` 全檔 SHA256 `b6a2ee0b…`。

**此後 re-sync 只需重跑上列命令並複驗第 3 項。**

---

## 5. git 狀態（不 commit）

`mv` 對 git 呈現為「刪除 + 未追蹤新增」。**16 檔顯示為 `D`，非 19**——
`18_delivery_execute.md` 與 `19_sidecar_policy.md` 搬移前即未追蹤，
`20_archive_and_charter.md` 亦然。

```
 M docs/fw036/FEATURE_ONBOARDING.md          （前包遺留）
 M features/projection/ANOMALIES.md          （本包：A-PJ76 / A-PJ77）
 M features/projection/DECISIONS.md          （本包：§0.27）
 D features/projection/docs/HANDOFF_*.md     （8 檔，已搬入 handoff/）
 D features/projection/docs/<reports>.md     （8 檔，已搬入 reports/）
?? docs/runtime/OPERATING_CHARTER.md         （本包新建）
?? docs/runtime/PROJECT_INSTRUCTION.md       （本包新建）
?? features/projection/docs/INDEX.md         （本包新建）
?? features/projection/docs/handoff/         （本包新建）
?? features/projection/docs/reports/         （本包新建）
?? features/projection/docs/upstream/        （本檔寫入後始出現）
?? features/projection/data/*.json           （前包遺留，本包未觸及）
```

**入庫時須用 `git add -A`**（或 `git add -u` 併同新增路徑）——
只 `git add <新目錄>` 會留下 16 筆未暫存之刪除，重命名偵測失效，
history 上看起來是「刪 16 檔、加 19 檔」而非搬移。

**全部 git 操作屬 Pei**，本層只準備不執行。

---

## 6. 本包是否仍有該驗而未驗者——執行層獨立判斷

三項。第一項須裁定，第二項為機制失效，第三項留待 re-sync。

### 6.1 A-PJ76｜R-P95 援引之 `canon §7.2` 不存在

R-P95 結語：「上繳包之必要成分依 canon §7.2，不因落檔而改變」。
下放包 §4 之 Charter 草案亦述 `§7 handoff contract`。

**實測**：`docs/fw036/FEATURE_ONBOARDING.md` 之 `^## ` / `^### ` 標題共 20 列，
最末為 `## 7. RD-1 packaging (Phase 7)`（第 444 行），**無 §7.2 亦無子節**。
全檔以 `上繳`、`handoff contract` 逐字掃描（區分大小寫）**零命中**。

即：**R-P95 所定之「上繳包必要成分」無來源可查。**
落檔本體可執行且已執行；成分要求懸空。

**處置**：依 A-PJ28 → A-PJ53 常規——不代擬（不自行擬定成分清單），回報，
R-P95 依原文落檔。本包之成分沿用 10–19 各包 §「上繳要求」之實際慣例，
**該慣例非 canon，僅為權宜**。

**須 Pei 裁定**：§7.2 補入 canon，或 R-P95 之援引改指他處
（Charter 中之 `§7 handoff contract` 同須一併更正）。

### 6.2 A-PJ77｜自檢表機制首次失效

下放包 §7「本包產生之新條文清單（A-PJ53 要求）」列 R-P95 / R-P96 兩條；
R-P97 立於 §4.1，且 §5 第 6 步明載三條落檔。同包內兩處不一致。

**意義**：A-PJ53 所設之自檢表，目的正是攔下「條文被立而未被清點」。
本次自檢表**自身**漏了一條——**該機制首次於實測中失效**。
且漏列者恰為本包唯一產出檔案之條文：若執行層僅依 §7 行事，
`PROJECT_INSTRUCTION.md` 不會被建立，而 Pei 索取的正是它。

**建議**：自檢表改為**自文件全文掃描新編號**而非人工列舉——
與 R-P97「串接而非轉錄」同型：人工複述之處即漂移之處。

### 6.3 Charter 之兩處待修（不阻塞）

| # | 位置 | 問題 |
|---|---|---|
| 1 | `OPERATING_CHARTER.md` L11 | `-往返索引：` 缺空格，markdown 不渲染為清單項 |
| 2 | 同檔 §-rules 段 | 述「§-rules below are a periodic copy」——自 R-P97 起 `PROJECT_INSTRUCTION.md` 為**串接產物**而非人工副本，「periodic copy」語義已過時 |

兩項皆屬分析層文字，未自行更動。留待下次 re-sync。

### 6.4 已驗且無異常者

- 搬移之 19 檔雜湊——多重集合 `diff` 無差異
- 三段串接雜湊——三項全同
- 空 `upstream/` 目錄不會被 git 追蹤——本檔寫入後解除
- `INDEX.md` 之 01–09 推導——已標明方法、量測條件與不具權威性

---

## 7. 本包產生之新條文清單（A-PJ53 要求）

**本包為上繳包，未立新裁決條文。** 落檔者為下放包所立之三條。

| 編號 | 動作 | 位置 |
|---|---|---|
| R-P95 | 落檔（逐字） | `DECISIONS.md §0.27` |
| R-P96 | 落檔（逐字） | `DECISIONS.md §0.27` |
| R-P97 | 落檔（逐字） | `DECISIONS.md §0.27` |
| A-PJ76 | 新登記 | `ANOMALIES.md`（分析層規則缺陷） |
| A-PJ77 | 新登記 | `ANOMALIES.md`（分析層規則缺陷） |

**清點方式**：對本檔與下放包全文掃描 `R-P\d+` 與 `A-PJ\d+`，
取編號 > 既有最大值者（R-P94 / A-PJ75）為新增，非人工列舉——依 §6.2 之建議。

**不 commit。**
