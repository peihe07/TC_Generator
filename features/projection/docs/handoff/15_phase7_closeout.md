# 下放包 — Projection Phase 7 Close-out

> 交付對象：Claude Code
> 觸發：交付檔 `b16debb7bc609e39…` 由單一次完整執行產出，W-0~W-9 全過、D-1~D-11 全綠
> 授權層級：Tier 1（**git 操作除外，全屬 Tier 3**）
> 日期：2026-08-12

---

## 0. 交付確認與結案

**Phase 7 交付完成。**

| 項 | 值 |
|---|---|
| 交付檔 SHA256 | `b16debb7bc609e39044803760171cf1d2b583fd1…` |
| 基準檔（備份） | `11579c9b3b8e56eb…` |
| 作廢版本 | `2c2abd22420bcd1f…`（已還原覆蓋，不列為交付版本） |
| 資料列 | 559 → 565（刪 r562、補 7 條） |
| 變更列 | 既有 63 列 + 授權例外 76 列（ER 6 / Author 40 / Remarks 30） |

### A-PJ68 結案

> **A-PJ68 CLOSED by R-P87。**
> 代理判準（11–143 字）非通過條件，實質判準（反映該 leaf 之需求敘述、逐字）7/7 通過即為合格。R-P81 之長度範圍已於 R-P87 更正為觀測性描述。
> **兩點待裁不再存在**——R-P87 已一併涵蓋，且如執行層所述，無論怎麼裁交付內容皆不變。

### A-PJ72｜變數遮蔽之延遲爆炸（記錄）

> W-9 迴圈以 `dst` 作儲存格變數，遮蔽了函式參數 `dst`（輸出路徑），致 `wb.save(dst)` 取得一個 `Cell`，於 zip 寫入階段才以 `'Cell' object has no attribute 'write'` 爆出。
> **遮蔽不會在遮蔽處報錯，會在很後面以看不懂的訊息報錯。**
> 與 canon §5a 第十二條（抽取式缺陷不會報錯）同族：**缺陷之顯現位置與其發生位置分離者，最難歸因。**
> 另有絕對參照 `$` 被正則吃掉（`$AJ$568` → `$AJ568`）——同族，已修正。
> 三者皆發生於複本，交付檔未受影響。

---

## 1. 可推廣之設計原則（寫入 canon）

執行層本輪第 7 項獨立判斷首次交白卷，其理由本身即為結論：

> **canon §5a 第十四條（新增）｜自我完備之檢查條件**
> 檢查項之通過條件應寫成「**與參照對象在所有可讀屬性上一致**」，而非「**已知的幾項正確**」。
> 前者涵蓋尚未想到的屬性，後者只涵蓋已想到的；後者每發現一項遺漏即需修訂一次條件，前者不需要。
>
> 實例（W-9）：條件寫為「補列與參照列 r561 在所有可讀屬性上一致，除內容欄與 `No.#` 公式外」，涵蓋 font 7 項、fill 2 項、border 5 項、alignment 6 項、protection 2 項、number_format、quotePrefix、列高／隱藏／outline、篩選 ref 共 252 格逐屬性。
> **反例**（W-6）：條件寫為「資料驗證範圍延伸至 r568」，只涵蓋當時已發現之一項；框線、對齊、篩選範圍三項因無人發現而無人寫，成為 A-PJ69。
>
> **判別法**：若某檢查項在發現新遺漏時需要修訂其條件文字，該條件即非自我完備。

---

## 2. RD-1 提交文件

產出 `docs/fw036/RD1_projection_submission.md`。**自 repo 現有檔案彙整，不重新判斷**。

### 2.1 結構

```
1. 文件目的與交付狀態（交付檔 SHA256、覆蓋率、變更統計）
2. 需求層問題（RD 作者須答）
3. 規格層缺件（文件持有方須提供）
4. 工具與資源缺件
5. 簿內既有缺陷（凍結欄，本專案無權修改）
6. 測試設計選擇待確認
7. 統計與交付慣例待裁
```

### 2.2 各節內容來源

**第 2 節 — 需求層問題**

| 項 | 來源 | 服務列 |
|---|---|---|
| 037 兩版 Verification Criteria 171/171 全異、description 127/171 不同 | A-PJ01 | 全案 |
| `$HCP_DISP2.Est_Range_BEV$` 無對映 LID，三候選互不等價 | A-PJ03 / R-P9 / DR#2 | 4 |
| `SWE1-PROJ-190 / 195` 之 VC 明言無可驗之物 | A-PJ54 / DR#16 | 2（補列） |
| `SWE1-PROJ-146` 全文轉指 `CFTS025-4660`，需求本文未確認存在 | A-PJ16 / R-P18 / DR#8 | 1（未覆蓋） |
| 037 Sub Categorization `额外来源需求` 非能力叢集 | A-PJ25 | 70 |
| `r131 / r132` 五欄全同，僅凍結之 `Test Item` 相異 | A-PJ43 | 2 |
| `NR1L-PROJ-415`（r415/r416）、`NR1L-PROJ-540`（r541/r542）ID 重複；`r48 / r53` ID 空白 | R-P64 | 4 |

**第 3 節 — 規格層缺件**

| 項 | 來源 | 服務列 |
|---|---|---|
| 81 列引用之 26 個 SYSAD `NRL-*` id 於 `inputs/` 版本不存在（判定為版本落差） | A-PJ63 / DR#19 | 81 |
| `Vehicle_Line_Configuration` 之 `HDCC27` / `DT27` 之 `27` 後綴語意 | A-PJ45 / DR#18 | 12 |
| `Projection Device HMI` 之 `(May 3 2023)` 與 `(February 5 2026)` 版本落差（116 列引用舊版） | A-PJ15 / R-P17 | 116 |
| `r219–r224` Remarks 自載「Section 35 應修改為 Section 15」而該欄凍結 | A-PJ33 | 6 |

**第 4 節 — 工具與資源缺件**

| 項 | 來源 | 服務列 |
|---|---|---|
| PCTS Verifier 操作手冊（`MT1` / `D5` / `WP43` 之選單路徑與讀值位置） | DR#1 / R-P11 | 9 |
| mobile GAL log 操作文件 | A-PJ32 / DR#12 | 4 |
| logcat 之產品專屬過濾 tag | A-PJ35 / R-P38 / DR#12 | 3 |
| 量測設備規格（`Test equipment for measuring …` 泛稱共 17 處） | A-PJ39 / A-PJ50 / DR#13 | 15 |
| `NR1L-PROJ-566`（227）所需之客戶專屬手機 APP | DR#15 | 1（補列） |
| `row 441` 之 refresh rate 測項（`V59` vs `V8` 不等價） | A-PJ20 / DR#9 | 1 |
| `row 443` 引用之測項於 431 個 PCTS 測項中不存在（`V45/V46/V47/V50` 四候選） | A-PJ21 / DR#10 | 1 |

**第 5 節 — 簿內既有缺陷（凍結欄，無權修改）**

| 項 | 來源 | 服務列 |
|---|---|---|
| `r372 / r376` 之 `Design Method` 違反本簿自身之資料驗證（`Reference!$C$4:$C$12`） | A-PJ58 / R-P69 | 2 |
| Procedure↔ER 術語與機制分歧（ER 凍結所致） | R-P37 / `er_divergence.json` | 35 |
| ER 內無可觀察判準之模糊語（`normally` / `correctly`） | R-P12 / A-PJ19 | 3 |
| `r230` 之步驟與 ER 皆無可觀察判準，三份 spec 查無依據 | A-PJ34 | 1 |

第 5 節之 `er_divergence.json` 須依 D-7 之更新後版本引用（`proc_excerpt` 已更新為修訂後內容）——**`mechanism_assertion` 2 列（r151/r152）之提問須同時涵蓋 ER**，其 ER 斷言了一個本專案判定無依據之機制。

**第 6 節 — 測試設計選擇待確認**

| 項 | 來源 |
|---|---|
| `SWE1-PROJ-133` 之「無 ByeBye 斷線」以手機關機實現（替代手段：超出範圍、USB 拔除） | R-P62 |

**第 7 節 — 統計與交付慣例待裁**

| 項 | 來源 |
|---|---|
| BLOCKED 佔位列（190/195）之 `Test Result` 留空，將計入 `TestProgress` 分母而永無結果 | R-P63 / R-P68 / DR#17 |
| Atl-Mid 30 列之範圍外標記以 `Remarks` 純附加寫入（凍結欄窄口） | R-P75 |

### 2.3 撰寫要求

- **每一項須附：現況、依據編號、服務列數、以及「若答 X 則後續為 Y」之分支說明**
- 引用 037 或 spec 原文者**逐字引用**，含原文之拼寫與標點，不得修正
- **不重新判斷**——所有內容自 `ANOMALIES.md` / `DATA_REQUESTS.md` / `DECISIONS.md` 彙整；若彙整時發現既有記載與本包不符，**停下回報**

---

## 3. Close-out re-sync

Project instruction 之 §-rules 為 `docs/runtime/ASPICE_SWE6_AI_Instruction.md` 之週期性副本，須於 feature close-out 時 re-sync。本 feature 期間產生之新增內容：

| 項 | 位置 | 狀態 |
|---|---|---|
| canon §5a 第一~十四條 | `FEATURE_ONBOARDING.md` | 十二條已落檔，第十三條（R-P87 代理判準）、第十四條（自我完備條件）本包新增 |
| canon §7 下放包／上繳包契約 | `FEATURE_ONBOARDING.md` | 已落檔 |
| profile 全文（`FULL_REFINE`、O-1~O-4、L-PJ1~L-PJ11、W-0~W-9、檢查表 v4、三處窄口） | `FW036_R1L_Projection_Profile.md` | 已落檔 |
| framework Part V | `framework.md` | 已落檔 |

**re-sync 之執行**：產出 `docs/runtime/ASPICE_SWE6_AI_Instruction.md` 之更新提案（diff 形式），**由 Pei 決定是否併入 Project instruction**。分析層不自行更新 Project instruction。

⚠️ **另須更正**：Project instruction 現行之 Operating Charter 寫「Entry point per feature: `<Feature>HMI/PLAYBOOK.md`」，該路徑於 2026-08-11 之目錄重組後已失效，實際為 `features/<feature>/PLAYBOOK.md`。**此為本 feature 開案時即發現而延至 close-out 處理者。**

---

## 4. git 提案（Tier 3，僅提案不執行）

### 4.1 三項入庫政策待 Pei 裁定

| # | 項目 | 現況 | 爭點 |
|---|---|---|---|
| 1 | `data/*_sections.json` 四份（cfts085 39KB / huig 69KB / sysad 41KB / addendum） | 已追蹤 | 內含客戶 spec 之章節標題全文。repo 自身排除 `spec-index/cache/*`，理由為「可能含機敏資料」——四份為同類文件之結構萃取，一致性上應同policy |
| 2 | `data/pcts_ui/*.xml`（14 份 297KB） | 已追蹤 | R-P11 證據綁定之唯一物證，不可再生（需實機）。不入庫則 `pcts_evidence.json` 之 status 無法複驗；入庫則含第三方 app 之 UI 結構 |
| 3 | `batches/` | 被 feature `.gitignore` 排除，標「regenerable artifacts」 | 於 `FULL_REFINE` 下不成立——batch JSON 含逐列 verdict 與理由，屬**稽核軌跡非可再生產物**。`b5_knob_BLOCKED.json` 尤其（記錄 42 列為何不動）。ASPICE SWE.6 要求之正是此物 |

**分析層建議**：#2 入庫（證據可追溯優先）、#3 改為只排除中間檔而保留 batch 記錄。#1 因涉及客戶資料政策，不建議由分析層判斷。

### 4.2 commit 分組提案（六組，順序可逐一 review）

| 組 | 內容 | 訊息 |
|---|---|---|
| 1 | canon §5a 十四條 + §7 契約 + profile 全文 | `docs: add canon numeric-discipline and handoff contract, Projection profile` |
| 2 | framework Part V | `docs: add Projection three-layer framework (Part V)` |
| 3 | 治理文件（DECISIONS / ANOMALIES / DATA_REQUESTS / PLAYBOOK / RECON / feature.yaml） | `docs(projection): record R-P1..R-P87 and 72 anomalies` |
| 4 | `data/*.json`（依 §4.1 之裁定決定納入範圍） | `feat(projection): add Layer 3 derivations, signal map, and evidence` |
| 5 | `scripts/lint_defs.py` + `writeback.py` | `feat(projection): centralise lint matchers and measurement conditions (R-P49, R-P65)` |
| 6 | batch 記錄（若 §4.1 #3 裁定入庫） | `docs(projection): add Phase 5 batch audit records` |

第 5 組單獨成一 commit 有其意義——**R-P49 / R-P65 的整個重點就是比對式與量測條件必須單一實作**，獨立的 commit 歷史使日後 blame 直接指向該裁決。

### 4.3 tag 提案

```
tag  fw036-projection-refine-v1
```

annotation 須含：交付檔 SHA256 `b16debb7bc609e39…`、資料列 559→565、覆蓋 leaf 165/171、變更列 63 + 授權例外 76、OPEN DR 清單。

**tag 由 Pei 執行。**

---

## 5. 上繳要求

1. `RD1_projection_submission.md` 全文
2. re-sync 提案（`ASPICE_SWE6_AI_Instruction.md` 之 diff 形式）
3. canon §5a 第十三、十四條落檔確認
4. A-PJ68 CLOSED、A-PJ72 登記
5. **git 狀態盤點**（`git status --porcelain` 全量 + 依 §4.2 六組分類之檔案清單），**不 commit**
6. 彙整 RD-1 時若發現既有記載與本包不符者，逐項列出

---

## 6. 本包產生之新條文清單（A-PJ53 要求）

| 編號 | 形式 | 位置 |
|---|---|---|
| canon §5a 第十四條 | 可貼區塊 | §1 |
| A-PJ72 | 可貼區塊 | §0 |
| A-PJ68 CLOSED | 可貼區塊 | §0 |

R-P87 已於前包落檔，本包建議其升格為 canon §5a 第十三條。

**不 commit。**
