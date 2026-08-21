# 批次 Playbook B：批 5–尾批 + 你的指令速查（2026-08-21）

---
## 批 5：M3 PM 訊號記法（105 列）
規則：R-1 三件組；網段自 DBC 實查（包內附 DBC 路徑與查得之
signal→message→segment 對照表；查無者標 PENDING: DR-{n}，
不得杜撰網段）。
Pei 前置：批 4 寫回；若 DBC 不在既定根目錄，先把 PM 之 DBC
放入 inputs/（素材補入屬你）。
下放：`出批5包` → `06_m3_pm_signal.md` → Opus5。
覆核判準：lint P 對 PM = 0 或僅剩 PENDING 列；43 列混用行全數
分層改寫；抽 8 列對 DBC 原文比對。
完成動作：寫回 PM ＋ ledger ＋履歷；未結 DR 入 DATA_REQUESTS.md。

---
## 批 6：M6+M9 AMFM 合批（30+154 列）
規則：§5.1 check that、S4 括號下半、§4.3 sibling 區分。
Pei 前置：**知會 Wilson**（動其 done 區 30 列＋68 列補括號）；
知會完成後才觸發。
下放：`已知會Wilson，出批6包` → `07_m6m9_amfm.md` → Opus5。
覆核判準：lint A/I 對 AMFM = 0；row87–90 四條 sibling 括號
各不相同且對應各自 Pre-Condition 差異；Wilson 列改動僅限
兩類目標字串。
完成動作：寫回 AMFM（新版次，不動 v1 tag）＋ ledger ＋履歷。

---
## 批 7：M10 test_item 摘句（583 列，最大內容批）
規則：R-3（你裁定之閾值）；摘句=保留與括號目的直接相關句，
全文以 spec_reference 指回；verbatim 摘句首字依 R-4。
Pei 前置：批 6 寫回；R-3 閾值已於批 R 定案。
下放：`出批7包` → 分本出包（BT/PM/Projection/AMFM/Home 各一，
量大不合批）→ 逐本 Opus5。
覆核判準：lint L = 0；抽 10%：摘句仍可回指原文（spec_ref 可解
析至含該句之章節/物件）；Home row135 表格內容移出 test_item
（去向：spec_reference 指回或 Remarks，包內裁定）。
完成動作：逐本寫回 ＋ ledger ＋履歷。

---
## 批 8：M2a Home Test Set（216 列）
規則：§4.1/§4.2；Home Layer 2 框架。
Pei 前置：我先出 Home Layer 2 提案（`出Home框架提案`）→
你簽署詞彙表 → 才出包。
下放：`框架已簽，出批8包` → `09_m2a_home_testset.md` → Opus5。
覆核判準：lint G 對 Home = 0；每 Test Set 過濾後為有意義叢集
（§4.1.3 判別法抽 3 組驗）。
完成動作：寫回 Home ＋ ledger ＋履歷。

---
## 批 9（條件批）：M13 去中文化
僅當 R-5 勾「去中文化」才存在；BT 436＋Projection 648 分本出包，
排最末。R-5 勾 OVERRIDE 則本批取消，改於 lint K 配置豁免。

---
## 尾批：防線啟用（S3 收口）
規則：PREVENTION_ARCHITECTURE 層 2/3。
Pei 前置：批 1–8（含條件批）全數寫回。
下放：`出尾批包` → `99_gate_enable.md`（lint --gate 納 pipeline
出貨流程、prompt builder 必填鍵模板更新、8 本回修後全跑 gate
留檔為基線）→ Opus5。
覆核判準：gate 模式對全部回修本 exit 0；對任一舊版本 exit 1
（自證 gate 有效）；Time Management 產出流程掛上 gate。
完成動作：git commit（你）；宣告新制生效，TM 起適用。

---
## 你的指令速查（全部逐字可貼）

| 時機 | 貼給 | 指令 |
|---|---|---|
| 現在 | Opus5 | `讀 docs/fw036/handoff/00_lint_bootstrap.md 與 00_lint_spec.md，執行` |
| 批0覆核後 | 我 | `批0覆核通過` |
| 勾完計畫 | 我 | `裁定完成，出批R包` |
| 每批覆核後 | 我 | `批N覆核通過，出批N+1包` |
| Opus5 每包 | Opus5 | `讀 docs/fw036/handoff/<檔名>，執行` |
| 卡住/異常 | 我 | `批N異常：<一句描述>`（我出診斷或修訂包） |

寫回樣板（每批完成、你本人執行）：
```bash
cp "<工作副本>" "<10_Reviewing 對應目錄>/<原檔名改日期加(Revise)>"
shasum -a 256 "<寫回檔>" >> <LEDGER>
```
