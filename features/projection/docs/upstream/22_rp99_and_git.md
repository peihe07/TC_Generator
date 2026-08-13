# 上繳包 22 — R-P99 修訂 + Charter 補正 + git 準備

> 交付對象：分析層（Claude Project）
> 對應下放包：[`handoff/22_rp99_and_git.md`](../handoff/22_rp99_and_git.md)
> 日期：2026-08-13
> 結果：**CONDITIONAL** —— §1 全數完成；**§3 之前提已於本包下達前變更**（見 §0.1），
> §3.1 兩項待裁之premise 皆已過時，另開 A-PJ79 一項須裁

---

## 0. 執行摘要

### 0.1 首先：git 已於本包下達前執行

**下放包 22 §3 假定 git 尚未入庫。實測：已入庫。**

```
1569a9e  2026-08-13 10:06:33 +0800
         docs(projection): add canon §8 handoff contract, converge charter,
         rebuild project instruction (R-P98, R-P99)
         31 files changed, 4640 insertions(+), 1 deletion(-)
```

Pei 已以單一 commit 完成第 20、21 兩輪之全部產出，**未分七組**。
`git status --porcelain` 現僅餘 4 筆本包所生之工作區變更。

**重新命名偵測成立**：16 筆搬移全數呈現為 `R100`（相似度 100%），
非「刪 16 加 19」。**`git add -A` 之建議兌現。**

§2 之四項準備工作**照做**，惟第 1–3 項已由事前查核轉為**事後查核**，
第 4 項（副檔名統計）為本包最要緊之發現來源，見 §3。

### 0.2 §1 五步

| 步 | 動作 | 結果 |
|---|---|---|
| 1 | 重新串接 `PROJECT_INSTRUCTION.md` | **705 行**（與預期相符）；第二段 `fa9833ae64c9092f…` **相符** |
| 2 | R-P100 → `DECISIONS.md §0.29` | 完成，併同追認兩項通則 |
| 3 | `INDEX.md` 第 22 列 | 完成 |
| 4 | §2 git 準備，不執行 | 完成，四項見 §2–§3；**未執行任何 git 寫入** |
| 5 | 上繳包 | 本檔 |

**Pei 要貼回 Project 設定的檔案**：

```
/Users/peihe/Work_Projects/TC_Generator/docs/runtime/PROJECT_INSTRUCTION.md
```

705 行。全檔 SHA256 `0fdc1ec1…`。

---

## 1. 第 1 步：重新串接（§4 第 1 項）

### 1.1 Charter 98 行之驗證

| 項 | 實測 |
|---|---|
| 行數 | **98**（`wc -l`，與下放包 §0.4 所述相符） |
| SHA256 | `32b0ae22…`（前版 `3e1258e7…`） |
| 新增條目 | L31–33「**不限於下放包**：分析層產出之**任何**供落檔文件（charter、canon 節文、應 Pei 要求另行產出之文件），一律 `write_file` 寫入 repo。」 |
| 節結構 | 六節不變（L1 / 21 落檔 / 37 數字紀律 / 53 觸點 / 71 工作形態 / 91 探測與工具） |

A-PJ79 之前身（上繳包 21 §6.3）**已閉合**——該條現同時存在於
canon §8.7 與 Charter 落檔節。

### 1.2 串接與驗證

命令與 R-P97 所定者逐字相同，未改。

**結構**：705 行 = 98（Charter）+ 3（空行 / `---` / 空行）+ 604（ASPICE §0–§13）。

**邊界定位依 §0.2 之新常規——以實測推得，不以文件所述行數硬編碼**：

```
N     = wc -l OPERATING_CHARTER.md        →  98
START = N + 4                             →  102
```

**加驗**：第 102 行內容為 `## 0. Purpose` —— 起點正確，非僅算術巧合。

| # | 比對 | SHA256 | 判定 |
|---|---|---|---|
| 1 | L102–EOF vs `ASPICE_SWE6_AI_Instruction.md` | `fa9833ae64c9092fb1fb10cbce303c0eaba7239b055e1505ce141c35ad1b147a` | **相同** |
| 2 | L1–98 vs `OPERATING_CHARTER.md` | `32b0ae22…` | 相同 |

第 1 項即 §1 第 1 步所指定之 `fa9833ae64c9092f`，逐字元相符。

### 1.3 三版串接之對照

| | 包 20（680 行） | 包 21（702 行） | 包 22（705 行） |
|---|---|---|---|
| Charter | 73 行 `2b02e588…` | 95 行 `3e1258e7…` | 98 行 `32b0ae22…` |
| 第二段起點 | L77 | L99 | L102 |
| 第二段 | `fa9833ae…` | `fa9833ae…` | `fa9833ae…` |
| 全檔 | `b6a2ee0b…` | `dd42b6e7…` | `0fdc1ec1…` |

**第一段已換三版，第二段三次全同。** R-P97 之設計意圖第三次兌現。

---

## 2. §2 git 準備：第 1–3 項

### 2.1 `git status --porcelain` 全量（§2 第 1 項）

```
 M docs/runtime/PROJECT_INSTRUCTION.md
 M features/projection/DECISIONS.md
 M features/projection/docs/INDEX.md
```

（本表為 §1 完成、本檔寫入前之狀態；本檔與 `ANOMALIES.md` 寫入後另加 2 筆。）

**已暫存者：0 筆**（`git diff --cached --name-only` 為空）。

| 檔案 | 變更行數 | 內容 |
|---|---|---|
| `docs/runtime/PROJECT_INSTRUCTION.md` | +3 / −0 | Charter 補入之三行 |
| `features/projection/DECISIONS.md` | +30 / −0 | §0.29（R-P100 + 兩項追認通則） |
| `features/projection/ANOMALIES.md` | +36 / −0 | A-PJ79 |
| `features/projection/docs/INDEX.md` | +1 / −0 | 第 22 列 |

### 2.2 六組分類（§2 第 2 項）—— **五組已於 `1569a9e` 入庫**

| 組 | §3.2 所列內容 | 現況 |
|---|---|---|
| 1 canon + charter | `FEATURE_ONBOARDING.md`、`OPERATING_CHARTER.md`、`PROJECT_INSTRUCTION.md`、profile | **已追蹤**（4/4） |
| 2 治理文件 | `DECISIONS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md`、`PLAYBOOK.md`、`RECON.md`、`feature.yaml` | **已追蹤**（6/6） |
| 3 往返封存 | `docs/`（handoff / upstream / reports / INDEX） | **已追蹤**（24 檔），16 筆 `R100` 重新命名 |
| 4 分析產物 | `data/` | **已追蹤**（40 檔，含 `pcts_ui/` 14 檔） |
| 5 腳本 | `scripts/` | **已追蹤**（4 檔） |
| 6 `.gitignore` | 若裁定變更 | **已追蹤**，且 `backup/` 已在其中（見 §2.3） |
| 7 batches | 若裁定入庫 | **未追蹤**（0 檔），仍由 `.gitignore:22` 排除 |

**§3.2 之七組指令現已無對應之待入庫內容**，僅第 6、7 組視 §3.1 裁定而定。

### 2.3 `git check-ignore -v`（§2 第 3 項）—— **兩項與下放包所述不符**

| 路徑 | 實測 | 命中規則 | 下放包所述 |
|---|---|---|---|
| `features/projection/inputs/` | **IGNORED** | `features/projection/.gitignore:2:inputs/` | 一致 |
| `features/projection/backup/` | **IGNORED** | `features/projection/.gitignore:8:backup/` | ✗ 述「預期未被忽略」 |
| `features/projection/data/pcts_ui/` | NOT-IGNORED | — | 一致（但已追蹤，見下） |
| `features/projection/batches/` | **IGNORED** | `features/projection/.gitignore:22:batches/` | 一致 |
| `output/` | **IGNORED** | `.gitignore:20:output/` | 一致 |
| `features/projection/data/sysad_sections.json` | **IGNORED** | `features/projection/.gitignore:27` | 一致 |

---

## 3. §2 第 4 項：副檔名統計（硬性前置）

**量測條件**：`git ls-files` 取已追蹤檔案全集共 **1,239** 檔；
以最後一個 `.` 之後字串為副檔名，正規化為小寫；無 `.` 者計為「無副檔名」。
`git add -A --dry-run` 另取待納入集合（**`--dry-run` 不寫入任何 git 狀態**）。

### 3.1 `git add -A` 待納入之集合

**3 筆，全部為 `.md`**：

```
add 'docs/runtime/PROJECT_INSTRUCTION.md'
add 'features/projection/DECISIONS.md'
add 'features/projection/docs/INDEX.md'
```

**無任何 `.xlsx` / `.pdf` / `.docx` / `.dbc` / `.apk`。**

### 3.2 `1569a9e`（Pei 已執行者）之副檔名統計 —— 事後查核

31 檔：**`.md` 29、`.json` 2**。無任何客戶原始檔格式。

兩份 `.json` 為 `data/d7_proc_excerpt_diff.json` 與 `data/dryrun_v6.json`，
屬 `adda62b` 已建立之 prose-stripped 稽核軌跡族。

### 3.3 `features/projection/` 之結論 —— **通過**

`git ls-files features/projection | grep -iE '\.(xlsx|xls|pptx|pdf|docx|dbc|apk)'`
→ **零命中**。

Projection 之 `.gitignore` 有效：`inputs/`（客戶原始檔）、`backup/`（工作簿副本）、
`batches/`（含逐字 prose）、`data/sysad_sections.json` 等四類全部擋住。

### 3.4 全 repo 普查 —— **projection 範圍外有 15 份客戶工作簿已追蹤（A-PJ79）**

副檔名分佈（前十）：

| 副檔名 | 數量 | | 副檔名 | 數量 |
|---|---|---|---|---|
| `json` | 571 | | `xlsx` | **19** |
| `md` | 144 | | `xml` | 14 |
| `py` | 134 | | `css` | 8 |
| `tsx` | 121 | | `yaml` | 6 |
| `ts` | 110 | | `yml` / `txt` | 4 / 4 |
| `svg` | 39 | | `tsv` / `sh` / **`pptx`** | 3 / 3 / **3** |
| `html` | 31 | | 其餘 | 各 ≤ 2 |

**19 個 `.xlsx` 之分佈**：

| 位置 | 數量 | 性質 |
|---|---|---|
| `docs/Report/compare/` | **15** | `FM-WI-FSM-036-A01` 客戶測試用例規範簿，涵蓋 AntiTheft / HFP / Notification / Player / SWC |
| `archive/M1/baselines/baseline_player_llm/` | 4 | sample／probe |

**`docs/Report/compare/` 之 15 份與 `features/*/inputs/` 為同一表單族**，
僅因不在 `inputs/` 路徑下而未被任何規則涵蓋
（`git check-ignore docs/Report/compare/` 零命中）。5.8 MB。

進入 history 之 commit：**`a4c013b`（2026-07-18）**，
`git merge-base --is-ancestor a4c013b HEAD` → 是。

**處置：不執行任何動作。** 版控政策屬 Tier 3，移除既有 blob 須改寫 history
（不可逆）——兩項皆為 Charter 明列之「須 Pei 裁定」。已登記為 **A-PJ79**。

**與 Projection 交付無關，不阻塞任何 commit。**

---

## 4. §4 第 4 項：`OPEN DR` 之現行記載（供 tag annotation）

**量測條件**：讀 `features/projection/DATA_REQUESTS.md` 主表（現行檔，
非任何先前列舉）；共 19 列，編號 1–19 無缺號；狀態取「狀態」欄之現行字樣。

### 4.1 分類

| 分類 | 數量 | 編號 |
|---|---|---|
| **OPEN** | **12** | `#1` `#2` `#8` `#11` `#12` `#13` `#14` `#15` `#16` `#17` `#18` `#19` |
| CLOSED | 5 | `#3`（R-P8′）`#4`（R-P22）`#5`（R-P13）`#6`（R-P16）`#7`（R-P17） |
| 撤銷 | 2 | `#9`（補裁 #2）`#10`（補裁 #3） |

### 4.2 供 tag annotation 之逐條（12 列）

```
OPEN DR  #1  PCTS 5 測項操作路徑與讀值位置 —— 部分滿足，3 項 partial 待人工確認
         #2  Est_Range_BEV 正式 LID 對映 —— 未提供
         #8  CFTS025 需求本文 —— 未提供，依 R-P18 不阻塞
         #11 MT1 / WP43 / D5 操作細節 —— 併入首次實跑（補裁 #4）
         #12 mobile GAL log 操作手冊 —— 未提供
         #13 Performance 組 7 列量測設備規格（+3 列 trace tool）—— 未提供
         #14 B5 跨車型前置條件三層問題 —— 未提供，B5 全批停下條件
         #15 SWE1-PROJ-227 客戶專屬手機 APP —— 未提供，不阻塞撰寫
         #16 SWE1-PROJ-190 / 195 需求有效性確認 —— 待 RD 確認
         #17 BLOCKED 佔位列之統計口徑 —— 待裁定
         #18 HDCC27 / DT27 之 27 後綴語意 —— 待答
         #19 與工作簿引用相符之 SYSAD 版本 —— 未提供，81 列
```

### 4.3 與下放包所警示之兩項錯誤對照

| 警示 | 本次結果 |
|---|---|
| 前次列舉誤列已撤銷之 `#9` `#10` | **未列入**（歸為「撤銷」） |
| 前次列舉漏列 `#14` | **已列入**（OPEN，B5 停下條件） |

### 4.4 一項讀取陷阱，須提醒

`DATA_REQUESTS.md` 第 20–23 行有一段醒目的粗體摘要：

> **Phase 2 結束狀態（2026-08-12…）：11 列中 5 列 CLOSED**…**OPEN 4 列**

**該段為 Phase 2 之歷史快照**（當時僅 11 列），與現行主表之 19 列 / OPEN 12 列
**不同**。段首雖標「Phase 2 結束狀態」，但其位置在主表之前且為粗體，
**極易被誤取為現行狀態**——前次列舉出錯之形態與此一致。

**建議**：於該段加註「以下為歷史快照，現行狀態以下表為準」，
或移至檔末。本層不自行更動（屬分析層維護之文件）。

---

## 5. §3 之兩項待裁：**premise 均已過時**

下放包 §3.1 列 A、B 兩項待 Pei 裁定。**兩項之現狀描述皆與實測不符。**

### 5.1 A 項｜`backup/` —— **已被排除，無須裁定**

> 下放包述：「`features/projection/backup/` 未被 `.gitignore` 涵蓋…❌ 未忽略」，
> 建議新增 `backup/`。

**實測**：`features/projection/.gitignore` **第 8 行即為 `backup/`**，
且第 4–7 行載有完整理由，**明引 R-P89 與 R-P78**：

```
# Backups of customer workbooks - same policy as inputs/ (R-P89). R-P78 requires
# the write-back backups be kept, so exclusion is the only available fix: each
# .bak.xlsx is a byte-identical copy of the customer workbook, and the
# delivery-target backup is a copy of what sat in the customer review folder.
backup/
```

`git check-ignore -v` 確認命中該行。該規則**已 commit，非工作區改動**。

即：**分析層所建議之處置，早已是既有政策，且理由與建議逐字同構。**

**另一項計數差異**：下放包述「內含 **2 份** 572 KB 客戶工作簿完整副本」，
實測 `backup/` 內為 **3 份**，各 572,672 bytes
（`…delivery-target.20260812T101458Z.bak.xlsx`、`…20260812T081932Z.bak.xlsx`、
`…20260812T084057Z.bak.xlsx`）。不影響結論（全數已排除），惟記錄以免對不上。

**§3.2 第 6 組之 commit 若照執行會是空 commit**（`.gitignore` 無變更）。

### 5.2 B 項｜`data/pcts_ui/` —— **已入庫，追認即可**

> 下放包述：「`features/projection/data/pcts_ui/*.xml`（14 份 297 KB）…❌ 未追蹤」，
> 並註「我先前於 R-P90 逕自裁為入庫，已越出自裁界線，改列為建議待你追認或推翻」。

**實測**：**14 份 `.xml` 已追蹤**（`git ls-files` 計 14），
入庫 commit 為 **`9e190c7`「feat(projection): track PCTS uiautomator dumps as
capture evidence (R-P90)」**。實際佔用 320 KB（下放包述 297 KB，量測口徑差異）。

即：**該裁決不僅已作成，且已執行入庫。** 現在能做的只有「追認」或
「推翻並改寫 history」，**後者為不可逆操作**。

**須 Pei 之動作已由「事前裁定」變為「事後追認或撤除」。**

### 5.3 兩項 premise 過時之共同成因

A 與 B 皆為**分析層以自身較早之認知描述 repo 現況，而未於下放前實測**——
與 canon §5a「不以自身先前輸出為來源」同族，
與 §0.2 所自承之「Charter 93 行」為同一形態（本輪第二、三次）。

**建議**：涉及 repo 現況（追蹤狀態、忽略狀態、檔數、大小）之陳述，
下放包一律以 `[待執行層實測]` 標記而不預填值——
**檔案狀態一律對 repo 實測**已是 Charter 探測與工具節之明文，
該條現僅約束執行層，形態上應雙向適用。

---

## 6. 本包是否仍有該驗而未驗者

### 6.1 R-P100 首次適用之自指命中複核（R-P100 明定須標明）

掃描 `handoff/22_rp99_and_git.md`，pattern `canon §5a 第.+條` **命中 1 次**，
位於 §0.1 R-P100 條文內對該 pattern 之字面引述（第 24 行），
**非真實引用**，屬 R-P100 所預告之自指。依規定人工複核後於此標明，**不自動排除**。

`R-P\d+` / `A-PJ\d+` / `DR#\d+` 三個 pattern 本輪無自指命中。

### 6.2 §3.3 tag annotation 之數字，本層無法驗證者

| 項 | 下放包所載 | 本層可否驗證 |
|---|---|---|
| 交付檔 SHA256 `b16debb7…` / size 574,700 | §3.3 | **可**——與 `DECISIONS.md §0.26` 送達執行結果所載相符 |
| 基準檔 `11579c9b…` | §3.3 | **可**——同上 |
| 資料列 559 → 565 | §3.3 | 不可——`output/` 已排除，交付檔不在 repo 內 |
| 覆蓋 170/171、未覆蓋僅 `SWE1-PROJ-146` | §3.3 | 不可——同上 |
| 變更既有 132 列（65 + 76 含重疊） | §3.3 | 不可——同上 |
| 裁決 R-P1 ~ R-P100 | §3.3 | **可**——`DECISIONS.md` 現含至 R-P100 |
| 異常 A-PJ01 ~ A-PJ78 | §3.3 | **須更正為 A-PJ79**（本包新開，見 §3.4） |

**`OPEN DR` 一行**已依 §4 自現行記載產生，**未沿用任何先前列舉**。

### 6.3 tag annotation 之 `異常` 範圍須改

annotation 草案寫 `A-PJ01 ~ A-PJ78`。本包新開 **A-PJ79**，
若於本包後打 tag，該行應為 `A-PJ01 ~ A-PJ79`。

惟 A-PJ79 為**跨 feature 之版控問題，與 Projection 交付無關**——
是否納入 Projection 之 tag，屬分析層判斷，本層僅回報數字已變。

### 6.4 已驗且無異常者

- 串接第二段 `fa9833ae64c9092f`——與 §1 指定值相符，三版連續相同
- 第二段起點以實測推得且經內容驗證（L102 = `## 0. Purpose`）
- Charter 98 行、新增條目、六節結構
- `git add -A --dry-run` 待納入集合——3 檔全為 `.md`
- `1569a9e` 之 31 檔——`.md` 29 / `.json` 2，無客戶原始檔
- 16 筆搬移之 `R100` 重新命名偵測成立
- `features/projection/` 全域客戶原始檔掃描——零命中
- 六項 `check-ignore` 逐項實測
- OPEN DR 12 列，未誤列 `#9` `#10`，未漏 `#14`

### 6.5 未執行之 git 操作

**本層未執行任何 git 寫入操作。** 僅用讀取型指令：
`status` / `log` / `show` / `ls-files` / `check-ignore` / `diff` / `merge-base`，
以及 `add -A --dry-run`（`--dry-run` 不改動 index）。

---

## 7. 本包產生之新條文清單（依 R-P100，新立與結案分列）

**掃描方法**：對 `handoff/22_rp99_and_git.md` 全文以
`grep -ohE 'R-P[0-9]+|A-PJ[0-9]+|DR#[0-9]+'` 抽取去重，
扣除基線後之餘數。**基線 = `git show HEAD`（`1569a9e`）之 `DECISIONS.md` /
`ANOMALIES.md` / `DATA_REQUESTS.md` 三檔全部編號，共 194 個**
（本輪基線可直接取 HEAD——包 20/21 之產出已 commit，無須再手動併入）。

### 7.1 新立

| 編號 | 來源 | 落檔位置 |
|---|---|---|
| R-P100 | 下放包 §0.1 | `DECISIONS.md §0.29` |
| **A-PJ79** | **本上繳包 §3.4**（執行層新開） | `ANOMALIES.md` |

**掃描結果與分析層 §5 之列舉一致**（皆為 `R-P100`）。A-PJ79 為本上繳包所開，
不在下放包文內，故不在掃描集合中——依 R-P95 之精神一併列出。

### 7.2 結案／援引／更正（不混入新立）

| 編號 | 動作 |
|---|---|
| R-P99 | 經 R-P100 **修訂範圍**（不就地改寫） |
| R-P95 | 援引更正之處置獲**追認**（`DECISIONS.md §0.27` 加註維持） |
| A-PJ78 | Charter 補正完成，落檔節與 canon §8.7 一致 |

### 7.3 併同落檔之兩項通則（下放包 §0.2 / §0.3）

| 通則 | 落檔位置 |
|---|---|
| 串接驗證以實測邊界定位，不以文件所述行數定位 | `DECISIONS.md §0.29` |
| 逐字落檔之條文一律不就地改寫（`SUPERSEDED` / `援引經 R-Pxx 更正`） | `DECISIONS.md §0.29` |

---

**不 commit。** git 全部屬 Pei。
本輪待入庫者為 4 檔工作區變更（`PROJECT_INSTRUCTION.md`、`DECISIONS.md`、
`ANOMALIES.md`、`INDEX.md`）加本檔，全部為 `.md` 與串接產物，無新增目錄，
`git add -A` 無風險（§3.1 已驗）。
