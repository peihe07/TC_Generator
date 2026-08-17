# 94 — Comfort HMI / pre_conditions 之 source class 標籤不入工作簿

- 產出層：分析層｜2026-08-17｜對象：執行層
- 裁定：Pei，2026-08-17 —— **「拿掉標籤，我從來都沒說可以加上標籤」**
- 性質：**交付物之內容訂正**，非新開發（feature 已 CLOSED，93 §1）

---

## 1. 裁定與其成因

`pre_conditions` 之 source class 標籤
（`[spec-verbatim]`／`[spec-derived]`／`[ext-verbatim]`／`[test-setup]`）
**一律不寫入工作簿**。

### 1.1 成因 —— 分析層之疏漏，且其形態具體

該標籤出自 profile §3.2（下放包 15 起草，16 §1 由 Pei 簽署 profile 時
一併生效）。**流程上非未經授權，而其未經裁定者是另一件事**：

> **「這個標籤要不要出現在交給客戶的那一格裡」，這個問題從未被問過。**

分析層對其他內部產物皆有明文處置：`reasoning` 不入工作簿、
`interface_axis_review` 列 `NOT_IN_WORKBOOK`、Layer 3 明文禁止寫入欄位
（§4.1.5）、Remarks 明訂「外部可見，不得出現內部 ruling id 或 A-CF 編號」。

**唯獨 pre_conditions 之標籤未被問過內外**，它順著「pre_conditions 是一個
欄位」被寫進交付欄位。

### 1.2 未量之事

`DECISIONS.md` 之 exemplar 為 `home`。G-1（下放包 16 §2）量了 home 之
**Test Item 欄**（144 列、143 含 modal），**未量其 pre_conditions 之格式**。

故 Comfort 之 J 欄格式**是否與既有 feature 一致，至今未經量測**。
依 Pei 之裁定「不回頭處理其他份」，**本包不量他 feature**，
惟此未量之事實記於此，使日後不被誤讀為「已比對過而選擇不同」。

---

## 2. 處置

### 2.1 profile §3.2 之修改

source class 為 `generated/*.json` 之**內部欄位**，不進工作簿 J 欄。

J 欄只寫**條件本文與其節次括號**：

```
1. The vehicle is equipped with Comfort features, such as heated/vented
   seats and a heated steering wheel (17.3)
```

**節次括號保留** —— 它是**條文出處**，非內部語彙；其讀者（評閱方、測試員）
需要它來定位該條件所依據之條文。

### 2.2 既有 434 列

`pre_conditions` 全數移除標籤，節次括號保留。

**JSON 內之標籤保留** —— 它仍是 R-C28 第一問（出處）之依據，
只是不外露。**內部依據與外部呈現分離，兩者皆存在。**

### 2.3 lint

- 既有 `source-class` 相關 gate 之驗證對象改為 **JSON**，不驗工作簿
- **新增 `no-source-class-in-workbook`**：J 欄命中四種標籤任一 → FAIL，
  指名該列與該標籤。反向驗證（注入一個 → FAIL；乾淨 → PASS）

**該 gate 之必要性由本案自證**：標籤之外露自 pilot 起持續 434 列而無任何
檢查會問「這一格裡有沒有我們自己的語彙」。

---

## 3. 與第二件之關係 —— **合併一次寫回**

Pei 另指出 `test_item` 之括號內容應**置於該格最下方**（格式待其確認，
見 §4）。

**兩件合併於一次寫回與一次交付** —— 使 Pei 之 Excel 四項確認只需一次。
本包先落 §2 之作業，`test_item` 之格式確認後補入同一輪。

---

## 4. 待確認（分析層已於 chat 提出）

`test_item` 現為 `… for heated/vented seats (HVS6.)`（括號在句尾同一行）。

待 Pei 確認其應為：

```
The system shall follow the HMI Settings List for the details on the
Auto Comfort Settings options for heated/vented seats

(HVS6.)
```

抑或另一種形態。**確認前不改 `test_item`。**

---

## 5. 執行層作業指示

1. 依 §2.1 改 profile §3.2。
2. 依 §2.2 移除 434 列之標籤，節次括號保留；JSON 不動。
3. 依 §2.3 改既有 gate 之驗證對象並新增 `no-source-class-in-workbook`，
   反向驗證。
4. **本輪不寫回** —— 待 `test_item` 之格式確認後合併執行。
5. **不動其他 feature、不改 RD-1、不動交付夾。** git 不執行。
6. 上繳 `docs/upstream/73_precond_labels.md`。

---

## 6. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| （無新條文）| — | — |

| 本輪於 chat 承諾落檔之包 | 編號 | 已落檔？ |
|---|---|---|
| 標籤移除 | **94** | ✅ 本包（**延遲一輪**；chat 承諾在前，落檔在後，第六次）|
