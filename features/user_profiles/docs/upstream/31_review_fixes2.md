# 上繳 31 — U-1 分支綁定、U-2 反向形態掃描

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`31_review_batch03b.md`（**無裁決條文**）
- **本輪未執行任何 git**；**未寫回工作簿**；**RD v2 未寄出**（Tier 3，屬 Pei）；
  **第四批未生成**
- 語料：**108 條，未變動**（本輪修改其中 2 條之 ER）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 108 條，**違規 0** |
| `lint_tcs.py --self-test` | 64 / 64 |
| `lint_variant_labels.py` 反向／語料 | 11 / 11 ／ 108 條違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |
| `audit_consistency.py` | K-3 0／K-4a 0／**U-2 0**／**U-1 3 待判**／T-1 0／K-4b 0／Q-1 9 待判 |
| `audit_consistency.py --self-test` | **32 / 32**（＋3：U-2）|
| `audit_variant_pairs.py` ／ `--self-test` | 違規 0 ／ 7 / 7 |
| `audit_delegation.py` ／ `--self-test` | 紅 0 ／ 黃 13 ／ 8 / 8 |
| `scan_override_notes.py --check` | 與 TSV 一致 |
| `lint_outbound_doc.py --self-test` | 8 / 8 |

---

## 1. U-1 —— `TC-082` 之 ER3 與多觸發 popup 之全批自檢

### 1.1 `TC-082` 之修正

| | 內容 |
|---|---|
| 前 | `PU1088 is displayed` |
| 後 | `PU1088 is displayed **and the setting under test is back to its default value**` |

依下放包所給之方向，並取其所指之觀察點（pre-condition 已有
「至少一項設定偏離預設」，故該值取得到）。

**與 `TC-081` 之分野維持不變**：`081` 驗回復之**範圍**
（只及現用 profile、不刪 username／avatar，且步驟 4 另查 Profile B 未被波及）；
`082` 驗**流程提示**，本次只加一個**綁定分支用**的觀察點 ——
`082` 仍未斷言「不波及他 profile」，那仍是 `081` 的事。

### 1.2 全批自檢 —— **命中 3 處，真缺陷 1**

判準：ER 斷言之 popup，其 PU id 在 spec 全文中有**一句以上**之觸發句者。

| tc_id | 節 | PU | 觸發句數 | 判 |
|---|---|---|---|---|
| **`082`** | 4.1.1 | PU1088 | 2 | **紅 —— 已修**（見 §1.1）|
| `002` | 4.1.1 | PU1088 | 2 | **綠，但綁法不同** —— 見下 |
| `031` | 9.6 | PU0588 | 2 | **綠 —— 兩句是同一個觸發**，非兩個分支 |

#### `002` 為何是綠的（**且它的綁法與 `082` 不同**）

`002` 之 leaf（`002-03`）為**未確認分支**。其綁定不在斷言 popup 的那一句，
而在**前一條 ER**：

> ER3 `The head unit **does not receive the completion confirmation**`
> ER4 `PU1088 is displayed`

procedure 步驟 3 主動 `Withhold the completion confirmation` ——
**一個走成功分支之實作無法滿足 ER3**，故分支被綁住。

**這一點決定了本掃描為何只能是「待判」而不能直接判紅**（見 §1.3）。

#### `031` 為何是綠的

PU0588 之兩句分別在 5.10.1 與 9.6：

> 5.10.1：`If a new seat position is saved to a Profile that is not currently
> active, a popup will prompt…`
> 9.6：`If the memory seat that is being saved is not linked to the active
> profile, a popup message (PU0588) will come up…`

**兩句描述同一個情境**（所存座椅不屬現用 profile），只是分別寫在兩節 ——
**是同一個觸發被記載兩次，不是兩個分支**。
且其 ER3 另併驗 `informs the user that the seat was saved to Profile B`，
即使有第二分支亦已具名對象。

### 1.3 **本掃描列為「待判」而非「紅」之理由**

綁定分支之方式**不只一種**：

| TC | 綁法 |
|---|---|
| `082`（修正後）| **同一句**併驗回復結果 |
| `002` | **另一條 ER** ＋ procedure 之情境注入 |

**機械判準無法斷定「哪一條 ER 綁住了哪一個分支」。**
若硬判為紅（例如要求「斷言 popup 的那一句必須帶額外條件」），
**`002` 那種正確作法會轉紅** —— 而它是本語料中綁得最紮實的一條。

故本掃描只負責**縮小人工範圍**：3 處，逐條由人判。已逐條記於 §1.2。

---

## 2. U-2 —— 反向形態（T-1 之補）

### 2.1 **判準第一版即錯，且錯得很典型**

v1 以 `\brecord` 比對步驟，得 **14 處**。
逐條看才發現**其中 13 處是比較步驟**：

> `3. Read the preference and check that it matches the value **recorded** in
> step 1`

**`recorded in step N` 是回指，不是記錄動作。**
v1 把「引用基準線的那一步」當成「建立基準線的那一步」——
**方向剛好相反，而它要找的正是方向。**

v2 排除 `recorded`（只認動詞 `record`），得 **1 處**。

### 2.2 命中 1 處：`TC-104`（4.6.3）—— 判為 **ER 漏斷言**

| | |
|---|---|
| 步驟 1 | `Open the status bar edit mode drawer and **record its state**` |
| 原 ER1 | `The Profile button is shown in the status bar edit mode drawer` |
| 原 ER3 | `The Profile button is highlighted in … drawer and in the app drawer` |

**沒有任何 ER 用到步驟 1 所記之狀態。**

### 2.3 兩類之分辨 —— **本例屬「ER 漏斷言」，不是「多餘步驟」**

下放包要求分開講。分辨之依據是**該斷言需不需要基準線**：

- 4.6.3 要驗的是「highlight 狀態**仍適用**」——
  **若無開啟前之基準線，一個「永遠 highlight」之實作會通過**
- 故該記錄步驟**是必要的**，缺的是 ER 沒去用它
- 同批之 `TC-103`（4.6.2）正是把兩者都寫齊的樣子

**若判為多餘步驟而刪掉它**，等於把 `TC-104` 降級成「開啟後有 highlight」——
**那正是 §5.6 所要防的**。

**處置（補 ER，不刪步驟）**：

| | 後 |
|---|---|
| ER1 | `… is shown in the status bar edit mode drawer **and its highlight state is recorded**` |
| ER3 | `… is highlighted in … and in the app drawer, **differing from the state recorded in step 1**` |

**全批 32 處記錄動作中，多餘步驟為 0 處。**

### 2.4 方向性案例（＋3，共 **32 / 32**）

| 案例 | 期望 |
|---|---|
| **`TC-104` 之原形**（步驟記錄 state 而 ER 從未引用）| **紅** |
| 其修正後之形（ER1 記錄、ER3 比對）| 綠 |
| **護欄**：比較步驟之 `recorded in step N` 不得被當成記錄步驟 | **綠** |

**第三條是護欄，也是 v1 之 13 處假紅的固化** ——
若日後有人把判準改回 `\brecord`，紅向兩條仍過，**只有這一條會倒**。

### 2.5 盲區（沿 30 輪 §3 第 2 項，具名不加同義詞表）

字面比對：步驟寫 `record the button graphic`、ER 寫 `the icon` 會假紅。
**現行語料無此形態**，故不加同義詞表 —— 加了就要維護，而維護不動的詞表會過期。

---

## 3. 獨立判斷 —— 本包是否仍有該驗而未驗者

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **U-1 之母體限於「spec 內同一 PU 出現多句」** | 判準盲區 | **同一分支之兩個不同 popup**（例：成功顯示 A、失敗顯示 B）不在母體內 —— 那種 ER 若只驗「A 顯示」亦可能不綁分支，本掃描看不見 |
| 2 | **U-1 無法自動判定綁定與否** | 設計選擇 | §1.3 —— 硬判會使 `002` 那種正確作法轉紅。**「待判」是刻意的，不是還沒做完** |
| 3 | **U-2 之字面比對** | 判準盲區 | §2.5 |
| 4 | **`TC-087`～`TC-095` 之 9 條未經覆核** | **分析層待辦** | 下放包已聲明 |
| 5 | **第四批取樣清單仍未經覆核** | **分析層待辦** | 29 輪提出，已隔兩輪 —— **第四批因此未生成** |
| 6 | **`082` 之 popup 內文仍不寫** | 承前（DR #4／R-U27）| 本次只加綁定分支之觀察點，**未動該限制** |
| 7 | **Q-1 9 處、D-3 13 處黃** | 承前 | 判讀未變 |
| 8 | **RD v2 未寄出** | **待 Pei（Tier 3）** | |
| 9 | A-UP09／R-U14、DR #4、RD #5／#6、R-U17、N-XF01、A-UP10、A-UP11 | 承前 | 擋 Phase 6 寫回 |

### 3.1 一項關於連續三輪之觀察

30 輪之 T-1、31 輪之 U-1／U-2，**三處缺陷都是人工覆核抓到的，
且三處的判準第一版都寫錯了**：

| 輪 | 判準 v1 之錯 |
|---|---|
| T-1 | 只查動詞 `read`／`record` —— **而缺陷那條步驟正好有 `Read`** |
| U-1 | （未寫 v1；直接設計為待判）|
| U-2 | 以 `\brecord` 比對 —— **把回指之 `recorded in step N` 當成記錄動作，方向剛好相反** |

**共同形狀：判準抓的是「有沒有那個詞」，而缺陷在「那個詞指的是不是同一件事」。**
這與 22 輪 D-3 之教訓（`does not support connectivity` 與
`does not support the connected profile feature` 共用三個詞）是同一個。

---

## 4. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | 檔案編輯 | `scripts/gen_batch03.py`（`TC-082` 之 ER3、`TC-104` 之 ER1／ER3 與 remarks）| 否 |
| 2 | 檔案編輯 | `scripts/audit_consistency.py`（**U-1 待判掃描** ＋ **U-2 掃描** ＋3 方向性案例）| 否 |
| 3 | 檔案重生成 ×30 | `generated/`（batch03；**內容變動者 2 條**：`082`／`104`）| 否 |
| 4 | **檔案新建** | `docs/upstream/31_review_fixes2.md`（本檔）| 否 |
| 5 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 6 | 程式執行 | U-1 之 PU 觸發句統計、U-2 之 v1／v2 各一次、生成 ×1、全部閘、九支 audit／lint 之 `--self-test` | 否 |

**本輪未執行任何 git**：寫入性與唯讀皆無。
**RD 查詢單未寄出** —— Tier 3，屬 Pei。
**第四批未生成**。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`、`DECISIONS.md`、`ANOMALIES.md`、`DATA_REQUESTS.md`、`data/`、
`scripts/gen_pilot.py`、`gen_batch01.py`、`gen_batch02.py`、`gen_pairs.py`、
`lint_tcs.py`、`lint_variant_labels.py`、`render_spec_region.py`、
`build_batch_context.py`、`audit_variant_pairs.py`、`audit_delegation.py`、
`scan_override_notes.py`、`lint_outbound_doc.py`、**他 feature 之任何檔**、
`docs/runtime/profiles/`、`docs/fw036/`。
