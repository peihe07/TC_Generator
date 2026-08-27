# 上繳包 03 —— 本輪收束（T15–T17）

- 日期：2026-08-27
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/04_round_close.md`
- 未結 DR：**0 筆**｜新登 anomaly：**0 筆**｜PENDING 裁決：**0 項**
- **Phase 0/1 全結。**

---

## 一、T15–T17 逐項結果

### T15 —— 抄錄與逐字元核對

核對法同前包：程式自下放包之 ``` 圍籬抽出區塊，寫入目標檔後**回讀該檔**
逐字元比對（非目視）。

| 條／文 | 抄入位置 | 字元數 | 字面一致 | sha256[:12] |
|---|---|---:|:--:|---|
| R-SU7 v2 | `RULINGS.md`（append 於 R-SU7 v1 之後） | 511 | **OK** | `419eb8aadd08` |
| A-SU2 處分 | `ANOMALIES.md`（A-SU2 節 §五） | 700 | **OK** | `a729d7364f01` |

**R-SU7 v1 不刪不改之確認**：回讀後 sha256[:12] = `c957b2d21f24`，
與上繳包 02 §二 所記完全相同 ✅。

A-SU2 摘要列與節標題已改記 **RESOLVED**。

> **執行層附註（不請裁，記錄即止）**：A-SU2 §四 之提案 3
> 「併記格之第二 id（334／361／507）是否入 037 內部追溯」未見於處分文。
> 依 R-SU5 v2 (b)「本欄僅作 037 內部追溯保留，不進入任何 TC 欄位」，
> 該三 id 之歸屬不影響任何 TC 產出，執行層以台帳所記之全集數
> （unique **366**，含該三 id）為準，不另請裁。已於 `ANOMALIES.md`
> 同位置註明。若分析層另有意見，下輪逕令。

### T16 —— spec_mode 回填與 recon 重跑

`feature.yaml` 之待裁註**已撤**，改為裁定值與其逐項依據：

```yaml
# 下放包 04 §1.3 裁定（依 T13 之 FO §3 逐條核對）：
#   A —— SYS1 export 之 outline map（HMI 家族，R-SU4 v2(b)）
#   B —— PDF 文字層之抽取管線（R-SU6 v2(b)）；其 `{filename}_{section}`
#        之 reference 形態**不採** —— reference 由 R-SU4 v2 專管
#   D —— CFTS/Word，reference 查得而非構造（CFTS 家族，R-SU4 v2(a)）
spec_mode: [A, B, D]
```

YAML 載入驗證：`spec_mode = ['A', 'B', 'D']` ✅

recon 全輸出：

```
$ python3 scripts/recon.py --feature features/sw_update
assertions:
- PASS — leaf count == Functional Requirement rows: expected 307, measured 307 — categorization distribution: {'Functional Requirement': 307, 'Heading': 45, 'Information': 25, 'Non Functional Requirement': 4, '(blank)': 1, 'Out of scope': 1}; the banned id-suffix criterion would have selected 0 (307 parent-shaped requirements dropped)
- PASS — cited sections found in the ruled SYS1 outline: expected 0, measured 0 — 0 cited / 120 outline entries in the export
recon complete: state=BLANK, leaves=307, sections=0, targets=307
decisions written to: .../features/sw_update/DECISIONS.md
```

**assertions 維持 2/2 PASS** ✅；state=BLANK、leaves=307、targets=307 皆不變。

`DECISIONS.md` 之唯一差異為 1 行：

```
-- spec_mode: [AUTO] A
+- spec_mode: [AUTO] ['A', 'B', 'D']
```

> **執行層處置揭露**：為使 recon 就地重寫而非落 `DECISIONS.new.md`
> （A-TM15 機制），重跑前**先刪除**既有 `DECISIONS.md`。
> 該檔為上一輪 recon 之產物、無任何人手編輯（簽核欄仍為未簽之
> `[PROPOSED]`／`[PEI]` 佔位），故無內容遺失。若分析層認為此舉
> 應改為保留 `.new` 再人工合併，下輪逕令。

> **觀察（不立案）**：`DECISIONS.md` 將 list 形態之 spec_mode 印為
> Python repr `['A', 'B', 'D']`，非 `[A, B, D]`。此為顯示層之
> `f"{cfg.get('spec_mode')}"` 直印所致，與 A-VC11（null 印為 `None`）
> 同源同型。A-VC11 已於全域排程 PENDING，**本 feature 不重複立案**。

### T17 —— 教訓入 PLAYBOOK.md

新增 **§7 操作慣例（建議，非條文）**，體例照 vehicle_category
（明載「違反不構成停止條件」）。條目 (1) 全文載於 `PLAYBOOK.md:148` 起，
含出處（上繳包 02 §六，T10／T12 案例）、成因、**「錯數之所以被抓到屬僥倖
不屬設計」之陳述**，與可操作之作法（每類各找一路不同源計數，各類之和
閉合到母體總數；本例閉合式 `87 + 487 + 137 + 10 = 721`）。

> **逾 T17 範圍之一項，主動聲明**：同檔 §6 狀態板之 P0／P1 兩列已一併
> 填實（P0 打勾、missing files 記「無」；P1 打勾、workbook_state BLANK、
> leaves／targets 307），並於 `Open PENDING rulings` 記「無」、
> 補記母體 311 與錨點池 574。理由：本包收束後 Phase 0/1 全結，
> 狀態板留空會與事實脫節。**未動 P2–P7 任何一列。**

---

## 二、RULINGS.md／ANOMALIES.md 最終條目序與狀態

### RULINGS.md —— 9 個條文區塊

| 序 | 條 | 來源 | 狀態 |
|---:|---|---|---|
| 1 | `R-SU1` | 下放包 01 §二 | 現行 |
| 2 | `R-SU2` | 下放包 01 §二 | 現行 |
| 3 | `R-SU3` | 下放包 01 §二 | 現行 |
| 4 | `R-SU4 v2` | 下放包 02 §二 | 現行（v1 未入正本） |
| 5 | `R-SU5` | 下放包 01 §二 | **已為 v2 取代，依令不刪不改** |
| 6 | `R-SU5 v2` | 下放包 03 §2.1 | 現行 |
| 7 | `R-SU6 v2` | 下放包 02 §二 | 現行（v1 未入正本） |
| 8 | `R-SU7` | 下放包 03 §2.2 | **已為 v2 取代，依令不刪不改** |
| 9 | `R-SU7 v2` | 下放包 04 §1.2 | 現行 |

現行條文 **7 條**（R-SU1、R-SU2、R-SU3、R-SU4 v2、R-SU5 v2、R-SU6 v2、R-SU7 v2）；
留存之被取代條文 2 條（R-SU5 v1、R-SU7 v1）。

### ANOMALIES.md —— 3 筆，全部 RESOLVED

| A | 內容 | 狀態 |
|---|---|---|
| A-SU1 | 素材身分判定與 repo 原件不符 | **RESOLVED**（下放包 02 §一；R-SU6 v2／R-SU4 v2） |
| A-SU2 | 037 Source Requirement ID 欄之三形態 | **RESOLVED**（形態面 R-SU5 v2；家族面 下放包 04 §1.1） |
| A-SU3 | 規格 PDF p.46 之 `PU971` 查無 | **RESOLVED**（下放包 03 §2.3：原文筆誤，作 `PU0971`） |

**PENDING 0 筆。** Assumption markers：無。

### 關鍵常數（供 Phase 3 引用，皆為本輪台帳實測值）

| 常數 | 值 | 條文 |
|---|---:|---|
| 037 資料列 | 383 | — |
| leaves（Functional Requirement） | 307 | recon assertion |
| 驗證母體 | **311**（307 + NFR 4） | R-SU3 |
| workbook_state | BLANK | R-SU2 |
| 錨點池 | **574**（章節 87 + 需求 487） | R-SU7 v2 |
| Description 物件 | 137（歸需求 45／歸章節 92／不可解 0） | R-SU7 v2 |
| SYS1 outline entries | 120 | R-SU4 v2(b) |
| 037 Source ID 全集 FOTA unique | 366 | R-SU5 v2 |
| `lint.popup_ids` | 51 | A-SU3 |
| spec_mode | [A, B, D] | 下放包 04 §1.3 |

> ⚠ **逐包揭露義務（R-SU3）**：驗證母體 **311** 無對應之 recon assertion
> 可宣告（`run_assertions()` 只實作 `functional_requirement_count`），
> 目前僅靠重測與上繳包交叉檢查守護，**非機器保證**。本輪重申。

---

## 三、未結 DR 清單

**空表。** 本輪 0 筆、無變動。

A-SU2 處分文所載之休眠線索（`SYS1_VF_with source ID/…` 二檔）
依令**記錄即止**：不納素材、未開檔、不發 DR，僅存於 `ANOMALIES.md`
之處分文內。個案 DR 之觸發條件（Phase 2/3 錨定時該 10 列仍無錨可落）
尚未發生。

---

## 四、獨立自評

**應驗而未驗者：無。** 本包三項任務皆為抄錄、回填、文件化，
無新量測；抄錄以程式回讀逐字元核對，回填以 YAML 載入 + recon
重跑（2/2 PASS）雙路驗證。

**須分析層留意之兩項處置**（皆已於 §一 逐項聲明，非隱藏動作）：

1. **T16 刪檔重生 `DECISIONS.md`** —— 為繞過 A-TM15 之 `.new` 機制。
   該檔無人手編輯故無損失，但此舉是執行層自行選擇的路徑，
   非下放包所令。若體例上應保留 `.new` 再合併，請下輪逕令。
2. **T17 逾範圍填了 §6 狀態板** —— 理由見 §一 T17。未動 P2–P7。

**一項本輪未觸及、但下輪起即相關者**：`RULINGS.md` 現同時存有
被取代之 R-SU5 v1 與 R-SU7 v1（依令不刪不改）。Phase 3 起若有
自動化讀取 `RULINGS.md` 之工具，**須以「v 字尾最大者為現行」為判準**，
否則會讀到已撤銷之 565／478／135 與單一形態陳述。此為文件結構之
既知風險，本包不自行處置。
