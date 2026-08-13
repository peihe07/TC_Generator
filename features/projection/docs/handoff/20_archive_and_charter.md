# 下放包 — 封存規範 + Operating Charter 修訂

> 交付對象：Claude Code
> 授權層級：Tier 1（檔案搬移與索引建立）
> 觸發：Pei 要求「每次下放上繳的內容都要整理好」+ close-out re-sync
> 日期：2026-08-12

---

## 0. 兩件事

1. **封存規範**——下放包與上繳包一律落檔、編號、建索引（§1–§3）
2. **Operating Charter 修訂提案**——供 Pei 貼回 Project instruction（§4）

---

## 1. 封存結構

```
features/<feature>/docs/
├── INDEX.md            ← 全部往返之索引（本包新建）
├── handoff/            ← 下放包（分析層 → 執行層）
│   └── NN_<slug>.md
├── upstream/           ← 上繳包（執行層 → 分析層）
│   └── NN_<slug>.md
└── reports/            ← 執行產出之報告（dryrun / phase 報告）
    └── <既有檔名>.md
```

### 命名

```
NN      兩位數流水號，依時間順序，下放與上繳各自獨立編號
<slug>  小寫英數與底線，取自主題，不含日期
```

**一次往返之下放與上繳使用相同 NN**——`handoff/07_phase7_writeback.md` 對應 `upstream/07_phase7_writeback.md`。若某次下放無對應上繳（或反之），該號在另一側留空並於 `INDEX.md` 標明。

---

## 2. 既有檔案之搬移

`features/projection/docs/` 現有 18 檔，依下表搬移。**搬移不改內容。**

### → `handoff/`

| 新檔名 | 現檔名 |
|---|---|
| `01_phase0_onboarding.md` | *（僅存於聊天，見 §2.1）* |
| `02_phase2_rulings.md` | *（同上）* |
| `03_phase4_pilot.md` | *（同上）* |
| `04_phase5_batches.md` | *（同上）* |
| `05_b3.md` | *（同上）* |
| `06_b10prime_b11prime.md` | *（同上）* |
| `07_vf176_b11prime.md` | *（同上）* |
| `08_handoff_contract.md` | *（同上）* |
| `09_phase6_dryrun.md` | *（同上）* |
| `10_phase7_writeback.md` | `HANDOFF_phase7_writeback.md` |
| `11_dr14_disposition.md` | `HANDOFF_dr14_disposition.md` |
| `12_phase7_step6_conditions.md` | `HANDOFF_phase7_step6_conditions.md` |
| `13_phase7_stepF_conditions.md` | `HANDOFF_phase7_stepF_conditions.md` |
| `14_apj69_rerun.md` | `HANDOFF_apj69_rerun.md` |
| `15_phase7_closeout.md` | `HANDOFF_phase7_closeout.md` |
| `16_closeout_disposition.md` | `HANDOFF_closeout_disposition.md` |
| `17_delivery_precheck.md` | `HANDOFF_delivery_precheck.md` |
| `18_delivery_execute.md` | `HANDOFF_delivery_execute.md` |
| `19_sidecar_policy.md` | `HANDOFF_sidecar_policy.md` |
| `20_archive_and_charter.md` | **本包** |

### 2.1 缺口：01–09 只存在於聊天

**A-PJ62 之更正（下放包一律寫入 repo）自第 10 號起才生效**，01–09 從未落檔。

處置：
- `INDEX.md` 為 01–09 各建一列，標 `狀態: 未落檔（A-PJ62 生效前）`，並記其主題與已知產生之條文編號
- **不重建內容**——重建即為以記憶產出文件，違反 canon §5a 第十五條
- 其實質內容已落於 `DECISIONS.md` / `ANOMALIES.md` / `profile`，該三處為權威

### → `reports/`

`dryrun_report.md`、`dryrun_v2_report.md`、`dryrun_v3_report.md`、`phase7_step1_5_report.md`、`phase7_step_a_e_report.md`、`phase7_delivery_report.md`、`git_inventory_closeout.md`、`closeout_pending_items.md`

### → `upstream/`

**目前為空。** 執行層之上繳包至今僅以聊天形式產出，未落檔——**與 A-PJ62 同型缺陷，只是方向相反**。自本包起補正（見 §3）。

---

## 3. 上繳包亦須落檔

> **R-P95｜上繳包一律落檔**
> 執行層之上繳包一律以 `write_file` 寫入 `features/<feature>/docs/upstream/NN_<slug>.md`，NN 與其對應之下放包相同。聊天中之呈現僅為副本。
>
> **依據**：Operating Charter「a ruling not written to the repo did not happen」對雙向同等適用。分析層之違反已登記為 A-PJ28／A-PJ53／A-PJ62；執行層之上繳包同樣未落檔，至今全部只存在於聊天，**若聊天遺失則無任何稽核軌跡**。ASPICE SWE.6 要求之可追溯性涵蓋往返雙向。
>
> 上繳包之必要成分依 canon §7.2，不因落檔而改變。

> **R-P96｜INDEX.md 為往返之單一索引**
> 每 feature 維護 `features/<feature>/docs/INDEX.md`，每次往返新增一列，欄位：
>
> | NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
> |---|---|---|---|---|---|---|---|
>
> - **下放／上繳**欄填相對路徑或 `—`（未落檔者標 `未落檔`）
> - **產生之裁決／異常**填該次往返新增之編號範圍
> - **結果**填 `PASS` / `FAIL` / `CONDITIONAL` / `阻塞(<DR#>)` / `—`
>
> 索引由**執行層**於每次上繳時更新，分析層於下放時不寫索引（避免兩方同時寫同一檔）。

---

## 4. Operating Charter 修訂提案

以下為 Project instruction 之 Operating Charter 段落（`## 0. Purpose` 以上）之建議替換全文。**Project instruction 僅 Pei 可編輯**，本包僅提案。

同時寫入 `docs/runtime/OPERATING_CHARTER.md` 作為 repo 內之權威副本——目前該段落**只存在於 Project instruction，repo 無對應檔案**，這本身即為單點失效。

```markdown
## Operating Charter (this Project = the ANALYSIS layer)

This Project is the analysis/ruling side of the FW036 TC pipeline: evidence is
weighed and Pei rules HERE; execution (scripts, generation, lint, write-back)
happens in Claude Code. Claude in this Project never writes the workbook.

Ground truth lives in the repo, read live via the Filesystem MCP:
`/Users/peihe/Work_Projects/TC_Generator`

- Entry point per feature: `features/<feature>/PLAYBOOK.md` §6 status board
-往返索引：`features/<feature>/docs/INDEX.md`
- Rule authority: `docs/fw036/FEATURE_ONBOARDING.md` (process, tiers,
  workbook_state, spec_mode, §5a numeric discipline, §7 handoff contract);
  feature overrides in `docs/runtime/profiles/`. On conflict those win.
- The §-rules below are a periodic copy of
  `docs/runtime/ASPICE_SWE6_AI_Instruction.md`; the repo version is
  authoritative. Re-sync at each feature close-out.

### 落檔（動作，非原則）

- 下放包：分析層以 `Filesystem:write_file` 寫入
  `features/<feature>/docs/handoff/NN_<slug>.md`，並於聊天告知路徑。
  **聊天附件不是交付**——它只在 Pei 手動轉貼時才生效。
- 上繳包：執行層寫入 `features/<feature>/docs/upstream/NN_<slug>.md`。
- 裁決條文：一律以可直接貼入之區塊產出，不夾在敘述中；每包末尾附
  「本包產生之新條文清單」自檢表。
- 索引：執行層於每次上繳時更新 `INDEX.md`。

A ruling not written to the repo did not happen — 雙向適用。

### 數字紀律（canon §5a，十七條）

分析層之陳述與 TC 內容受同一紀律拘束。撰寫任何數字、狀態或事實前：

- 標明量測條件——量什麼、什麼單位、掃描哪些欄位、是否區分大小寫與詞界
- 跨輪次之累計量每輪自總量重算，不沿用前輪差值
- **不以自身先前輸出為來源**；回到 repo 或當下實測
- 立新規則前先查既有政策；既有政策優先
- 接受更正時之查證義務，與提出陳述時相同
- 引用任何單一來源為「權威」前，先確認其涵蓋範圍是否等同其類別

全文見 `FEATURE_ONBOARDING.md` §5a。**此節為分析層最常違反者**，Projection
期間十七條中有六條源自分析層之實際錯誤。

### 觸點與自裁界線

分析層得自裁：gate 條件與比對方法、量測與掃描定義、欄位判準之技術性選擇、
批次排序、anomaly 之登記與分類。

**須 Pei 裁定**（不得自裁）：
- 凍結欄之任何例外（窄口授權）
- 交付形式、交付位置、送達執行
- 範圍界定（何者在／不在驗證範圍）
- 版控政策（`.gitignore`、入庫範圍、tag）
- 素材補入超出既定根目錄
- 任何不可逆操作

**全部 git 操作屬 Pei**，分析層與執行層皆只準備不執行。

### 工作形態

- `<Feature>, 接手` = 讀該 feature 之 PLAYBOOK §6 + `INDEX.md` + open PENDING
- 一批一上繳，前批未覆核不得開下批
- 升級 chat 覆核之條件由下放包明列
- 執行層每次上繳附「本包是否仍有該驗而未驗者」之獨立判斷——
  此機制於 Projection 連續六輪產出實質發現，為最有效之單一檢查
- Dry-run：`regen` 型套 canon §6；`FULL_REFINE` 型套 profile 之
  `[OVERRIDE]` 檢查表（canon §6 之 segment 算術／順序／req-set 相等
  三項於該型態無對應概念）
- MCP 逾時：自動重試一次；連兩次失敗才請 Pei 重啟
- 沙箱副本可用於唯讀探測（解析、比對、統計）；**涉及檔案狀態
  （hash、大小、mtime、追蹤狀態）一律對 repo 或實際路徑實測**
- 無 emoji 之限制適用於 TC workbook 欄位；handoff 文件內之標記符號不受限
```

**主要變更（供 Pei 對照）**：

| # | 變更 | 理由 |
|---|---|---|
| 1 | `<Feature>HMI/PLAYBOOK.md` → `features/<feature>/PLAYBOOK.md` | 2026-08-11 目錄重組後失效，開案時即發現而延至今 |
| 2 | 新增「落檔（動作，非原則）」整節 | 原則被違反五次（A-PJ28/53/62）；寫成動作後未再犯 |
| 3 | 新增「數字紀律」節並指向 canon §5a | §5a 十七條中六條源自分析層錯誤，而 Project instruction 原本完全沒有對應段落 |
| 4 | 「五個觸點」→ 明列自裁／須裁兩類 | 實際約九十條裁決中僅約八條由 Pei 親裁，界線一直由分析層自畫 |
| 5 | canon §6 標明僅適用 regen | `FULL_REFINE` 下三項無對應概念，最終整份換掉（R-P53） |
| 6 | MCP 逾時改為「重試一次再請重啟」 | 原文直接要求請 Pei 處理，實測重試常可恢復 |
| 7 | 沙箱探測規則細分為「唯讀探測可／檔案狀態不可」 | 原文一概禁止，實務上大量唯讀解析在沙箱進行且無害；真正出錯的是檔案狀態（大小那次） |
| 8 | emoji 限制範圍澄清 | 原文限 TC 欄位，但 handoff 文件用了大量標記符號，處於灰色地帶 |
| 9 | 新增「執行層獨立判斷」為明文機制 | 連續六輪產出實質發現，而分析層自查從未攔下任何一項 |

---

## 4.1 產出完整之 Project instruction 檔

Pei 需要一份可直接貼回 Claude Project 設定之完整 markdown。

> **R-P97｜Project instruction 以串接產生，不以轉錄產生**
> `docs/runtime/PROJECT_INSTRUCTION.md` 由兩段**串接**而成，不得由任何一方憑記憶或複製聊天內容轉錄：
>
> ```
> 第一段  docs/runtime/OPERATING_CHARTER.md            （本包 §4 之內容）
> 分隔    ---
> 第二段  docs/runtime/ASPICE_SWE6_AI_Instruction.md   （§0–§13，權威副本）
> ```
>
> **依據**：§0–§13 約六百行，任何轉錄都可能靜默漂移，而漂移不會報錯（canon §5a 第十二條同型）。串接使兩段各自維持單一權威來源。
>
> 產生後須驗證：`PROJECT_INSTRUCTION.md` 之第二段與 `ASPICE_SWE6_AI_Instruction.md` **逐字元相同**（以雜湊比對，不以目視）。
>
> **此後每次 close-out re-sync 重跑串接即可**，不需人工比對兩份。

---

## 5. 執行

```
1. 建立 handoff/ upstream/ reports/ 三個子目錄
2. 依 §2 搬移既有 18 檔（git mv 不適用——尚未 commit，用檔案系統搬移）
3. 建立 INDEX.md，含 01–20 全部列；01–09 標「未落檔」
4. 建立 docs/runtime/OPERATING_CHARTER.md，內容為 §4 之 markdown 區塊
5. 依 R-P97 串接產生 docs/runtime/PROJECT_INSTRUCTION.md，驗證第二段雜湊相同
6. R-P95 / R-P96 / R-P97 落檔至 DECISIONS.md §0.27
7. 自本包之上繳起，上繳包寫入 upstream/20_archive_and_charter.md
```

**搬移前後須驗證檔案數與內容雜湊不變**（18 檔全部）。

---

## 6. 上繳要求

1. 搬移前後之檔案清單與雜湊比對
2. `INDEX.md` 全文
3. `docs/runtime/OPERATING_CHARTER.md` 建立確認
4. R-P95 / R-P96 落檔確認
5. 本包之上繳包本身落檔於 `upstream/20_archive_and_charter.md`（R-P95 之首次適用）
6. 本包是否仍有該驗而未驗者

---

## 7. 本包產生之新條文清單（A-PJ53 要求）

| 編號 | 形式 | 位置 |
|---|---|---|
| R-P95 | 可貼區塊 | §3 |
| R-P96 | 可貼區塊 | §3 |

落檔：R-P95 / R-P96 → `DECISIONS.md §0.27`。

**不 commit。**
