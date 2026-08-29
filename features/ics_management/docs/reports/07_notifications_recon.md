# 07 Notifications 偵察報告（作業 H，DR-ICS17）

> 本檔為下放包 07 作業 H 之偵察，依 **R-ICS21(c)**：**只列材料不判採用、不充 verbatim 來源、不充錨**。
> 本檔所有數字與檔名皆為實測。命中與否只作證據陳述，不構成任何裁定。

---

## §0 掃描條件

### 0.1 實際 `ls spec-index/sources/` 結果

實測共 **33 件**。目標本為第 15 件，實際檔名逐字為：

```
Notifications HMI Logic and Flow R1L-R (Feb 13 2026).pdf
```

與下放包所給名稱**完全一致**（無錯字、無版本差）。

### 0.2 抽取法（雙工具逐頁）

| 工具 | 版本／指令 |
|---|---|
| pdftotext | `/opt/homebrew/bin/pdftotext -layout <pdf> -`，以 form feed (`\f`) 切頁 |
| pdfplumber | 0.11.9，`page.extract_text()` 逐頁 |

判定規則：**二者逐頁非空白字元皆為 0** 者記 `NO_TEXT_LAYER`。
**未做 OCR，未強解。**

### 0.3 正規化四式（A-ICS32）

A-ICS32 指出前輪漏命中的真因是**純換行斷詞**（如 `Rear` / `View` 各據一行），不只是連字號。
故每頁備四種文本，**逐式各掃一次**並記錄命中形態：

| 形態 | 定義 |
|---|---|
| `raw` | 原文（pdftotext 與 pdfplumber 之逐頁文本合併） |
| `dehyph` | **去連字號重掃**：移除 `-\n`（含前後縮排） |
| `flatnl` | **壓平換行重掃**：僅把換行及其兩側縮排換成單一空格，不動連字號 |
| `flat` | `dehyph` 再把所有空白壓成單一空格（最寬鬆） |

比對一律**大小寫不敏感**。

### 0.4 關鍵詞清單

主掃（下放包指定）：

```
VOLUME POP_UP / VOLUME POP-UP / VOLUME POPUP / VOLUME POP UP
volume, mute, timeout, duration, dismiss, priority
```

另加寬鬆 regex：`volume[\s_\-]*pop[\s_\-]*up`（大小寫不敏感），
以涵蓋 `VOLUME POP_UP`、`VOLUME POP-UP`、`VOLUME POPUP`、`VOLUME POP UP`、以及跨換行之 `VOLUME\nPOP_UP`。

「是否即 Pop-up List Notification」之線索詞（§3 用）：

```
Pop-up List Notification / Pop up List Notification / Popup List Notification
Pop-up List / Pop Up List / Priority Matrix / Notifications HMI
Cat. / Category / X button / 5 sec / 5 second
```

另加寬鬆 regex：`pop[\s_\-]*up[\s_\-]*list`。

### 0.5 腳本

`features/ics_management/scripts/src_recon_07.py`（新建，**唯讀**，不改任何素材）。

---

## §1 基本量測

| 項目 | 實測值 |
|---|---|
| 檔名 | `Notifications HMI Logic and Flow R1L-R (Feb 13 2026).pdf` |
| 路徑 | `spec-index/sources/` |
| 檔案大小 | 812,377 bytes |
| sha256 | `599f4ff6805330997836e8596db97346a6133348c7b96cbe60f2fe83776a37b4` |
| 頁數（pdftotext） | **6** |
| 頁數（pdfplumber） | **6** |
| 文字層 | **有**（6 頁全有） |
| `NO_TEXT_LAYER` 頁 | **0 頁** |

sha256 以 `shasum -a 256` 實算，並經腳本內 hashlib 覆算，二者一致。

### 逐頁非空白字元數

| 頁 | pdftotext | pdfplumber | 文字層 |
|---:|---:|---:|---|
| 1 | 235 | 235 | 有 |
| 2 | 715 | 715 | 有 |
| 3 | 2845 | 2845 | 有 |
| 4 | 394 | 394 | 有 |
| 5 | 2485 | 2485 | 有 |
| 6 | 634 | 634 | 有 |

二工具逐頁字元數**完全相同**，表示文字層乾淨、無抽取分歧。

---

## §2 目次／章節結構

本本**無獨立目次頁**。6 頁之章節標題（逐字照錄自頁面標題列）：

| 頁 | 標題／內容 |
|---:|---|
| 1 | 封面：`R1L-R Notifications` / `HMI Logic and Flow` / `February 13, 2026` / `HMI/NAFTA Lead: Hannah Zheng` |
| 2 | `Assumptions` ＋ `Document Related Content` 表 |
| 3 | `Notifications`（Notes NTF1 ~ NTF4） |
| 4 | `7" Notification Drawer`（純圖示頁，僅圖說文字） |
| 5 | `Notifications Continued`（Notes NTF4 ~ NTF18） |
| 6 | `Stored Notifications & Notifications Settings`（訊息類型／是否入 Notification List／是否有 On-Off 設定 三欄表） |

需求編號體系為 **`NTF*`**（NTF1、NTF2、NTF2.1、NTF3、NTF3.1~3.4、NTF4、NTF6~NTF18；
另 p.5 有一處拼為 `NOTF7.1`，且 `NTF4` 在 p.3 與 p.5 各出現一次 —— 原文如此，**不代為調和**）。

p.2 `Document Related Content` 表逐字照錄：

> `Core HMI Logic and Flow` — `Core behaviors`
> `HMI Settings Lists` — `Notification Settings`
> `HMI Pop Up List` — `Pop Ups`

---

## §3 「是否即 `Pop-up List Notification`」之證據

### 3.1 背景

`Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` p.3 逐字：

> "Popups with X button which do not have a timeout defined in the **Pop-up List Notification** will have a 5 sec timeout."

被外指之文件不在 `spec-index/sources/` 的 33 件內（前輪已對 `ls` 全表比對）。
本本檔名近似，惟檔名近似**不足以認定**。以下逐項列證。

### 3.2 自稱證據（文件自己怎麼稱呼自己）

| # | 位置 | 逐字照錄 | 評 |
|---|---|---|---|
| A1 | p.1 封面標題 | `R1L-R Notifications` / `HMI Logic and Flow` | 自稱為 **Notifications HMI Logic and Flow**，非 `Pop-up List Notification` |
| A2 | 全文 | 掃 `Pop-up List Notification` / `Pop up List Notification` / `Popup List Notification`（四式正規化、大小寫不敏感） | **0 命中**。文件從未如此自稱 |
| A3 | 頁首／頁尾 | 無頁首。頁尾僅阿拉伯頁碼（p.3 `3`、p.5 `5`、p.6 `6`） | 無版本頁、無文件編號、無 SR/CR 版次標記 |

### 3.3 結構對應證據

| # | Priority Matrix 側所預期之特徵 | 本本實測 | 評 |
|---|---|---|---|
| B1 | 應為**逐項 pop-up 清單** | 本本無任何 pop-up 逐項清單。p.5 僅示例三種尺寸（`Example of a "Small" Popup` / `"Medium"` / `"Large"`）之圖示；p.6 之表為「訊息類型 × 是否入 Notification List × 是否有 On/Off 設定」，非 pop-up 清單 | **不對應** |
| B2 | 應含 **timeout 欄位** | 全文掃 `timeout`（四式）→ **0 命中**。亦無 `duration`（0 命中）、`dismiss`（0 命中） | **不對應** |
| B3 | 應與 Priority Matrix 之 **Cat. 分類體系**對得上 | 全文掃 `Cat.` → 0 命中；`Priority` → **0 命中**；`Category` 僅 1 次，出現於 p.5 `NTF6.)`，語意為「電話類別的簡訊圖示」，與 Priority Matrix 之 Cat. 分類無關 | **不對應** |
| B4 | 應為被 Priority Matrix 指向之**下游定義文件** | 本本**反向外指**另一份文件。p.2 `Document Related Content` 列 `HMI Pop Up List` — `Pop Ups`；p.3 `NTF2.)` 逐字：「Notifications are popups that get stored (when applicable). **See HMI Popup List.**」；p.3 `NTF3.1)` 逐字：「…be remembered (latching) over key cycles for each user. **See HMI Popup List.**」 | **強烈不對應**。本本自認 pop-up 清單在**別本**（`HMI Pop Up List`），而該本不在 33 件內 |
| B5 | Priority Matrix p.3 之 `X button` / `5 sec` 語彙 | 全文掃 `X button` → 0 命中；`5 sec` / `5 second` → 0 命中 | **不對應** |

### 3.4 證據評估（**非裁定**）

> **不支持同一。**

理由摘要：本本自稱為 `Notifications HMI Logic and Flow`（A1、A2）；結構上不是逐項 pop-up 清單、無 timeout 欄位、無 Cat. 分類體系（B1~B3、B5）；且本本於三處（p.2 Related Content、p.3 NTF2、p.3 NTF3.1）**主動外指**一份名為 `HMI Pop Up List` / `HMI Popup List` 的**另一份文件**（B4）——這正是 Priority Matrix 所稱 `Pop-up List Notification` 的更可能所指，而該文件**不在 `spec-index/sources/` 的 33 件內**。

**本節為證據評估，不是裁定。**採用與否、DR-ICS17 是否改指 `HMI Pop Up List`，均待裁定層處理。

---

## §4 關鍵詞逐頁命中表

四式正規化（`raw` / `dehyph` / `flatnl` / `flat`）逐頁各掃一次，大小寫不敏感。

| 關鍵詞 | 命中頁 | 命中式 |
|---|---|---|
| `VOLUME POP_UP` | **無** | — |
| `VOLUME POP-UP` | **無** | — |
| `VOLUME POPUP` | **無** | — |
| `VOLUME POP UP` | **無** | — |
| `volume` | **無** | — |
| `mute` | **無** | — |
| `timeout` | **無** | — |
| `duration` | **無** | — |
| `dismiss` | **無** | — |
| `priority` | **無** | — |
| regex `volume[\s_\-]*pop[\s_\-]*up` | **無** | — |

**指定關鍵詞十項，逐頁逐式全數 0 命中。**

參考：另掃之線索詞命中（僅供 §3 佐證，非指定關鍵詞）

| 線索詞 | 命中頁 | 命中式 | 逐字片段 |
|---|---|---|---|
| `Notifications HMI` | p.1 | `flatnl`, `flat` | `R1L-R Notifications HMI Logic and Flow February 13, 2026`（跨換行，故僅壓平式命中） |
| `Pop Up List` | p.2 | 四式全命中 | `HMI Settings Lists Notification Settings HMI Pop Up List Pop Ups` |
| `Category` | p.5 | 四式全命中 | `NTF6.) Notifications types will have an associated icon (e.g. text message icon from the phone category for text message notifications).` |
| regex `pop[\s_\-]*up[\s_\-]*list` | p.2, p.3 | `flat` | p.2 `… HMI Pop Up List Pop Ups`；p.3 `NTF2.) Notifications are popups that get stored (when applicable). See HMI Popup List.`；p.3 `NTF3.1) … for each user. See HMI Popup List.` |

註：`Notifications HMI` 只在壓平換行式命中，正是 A-ICS32 所述**純換行斷詞**之實例——`Notifications` 與 `HMI` 分屬封面兩行。若只掃 `raw` 與 `dehyph` 會漏。**兩式重掃為必要。**

---

## §5 `VOLUME POP_UP` 之明確結論

> **查無。**

掃法陳述（供覆核）：

1. 雙工具（pdftotext `-layout` ＋ pdfplumber 0.11.9）逐頁抽取，6 頁文字層皆有，`NO_TEXT_LAYER` 0 頁 —— 故**無因缺文字層而漏掃之頁**。
2. 每頁四式正規化（`raw` / `dehyph` 去連字號 / `flatnl` 壓平換行 / `flat`），逐式各掃一次。
3. 字面掃 `VOLUME POP_UP`、`VOLUME POP-UP`、`VOLUME POPUP`、`VOLUME POP UP` 四變體，大小寫不敏感 → 0 命中。
4. 寬鬆 regex `volume[\s_\-]*pop[\s_\-]*up` 於最寬鬆之 `flat` 文本上掃 → 0 命中。
5. 單詞 `volume` 單掃 → **全文 0 命中**。既然 `volume` 一詞於本本 6 頁完全不出現，`VOLUME POP_UP` 不可能以任何斷行／連字號變體潛藏其中。

**結論：本本全文未出現 `volume` 一詞，遑論 `VOLUME POP_UP` 之顯示條件。**
b01 三條 TC 共 6 行 ER 所斷言之 `"VOLUME POP_UP"` 顯示條件，**在本本查無**。

**查無是有效結果。未編造、未強解、未 OCR。**

---

## §6 E5 是否觸發

E5 升級條件為：本本**確為**所指文件 **且** 載有 `VOLUME POP_UP` 的顯示條件。

| 條件 | 實測 |
|---|---|
| 確為 `Pop-up List Notification` 所指文件 | **否**（§3.4：不支持同一） |
| 載有 `VOLUME POP_UP` 顯示條件 | **否**（§5：查無，全文無 `volume` 一詞） |

> **E5 未觸發。**兩項條件皆不成立（任一不成立即不觸發，此處為雙重不成立）。

無需停下待納源裁定。

---

## §7 偵察副產物（供裁定層參考，本節不作任何主張）

1. **DR-ICS17 之線索指向已移轉**：Priority Matrix 所指之 `Pop-up List Notification`，經本本三處外指，**更可能是 `HMI Pop Up List` / `HMI Popup List`**。該文件名不在 `spec-index/sources/` 的 33 件內。
2. **`VOLUME POP_UP` 之素材窮盡狀態**：五包已窮盡 CFTS022／CFTS020／CFTS019 七件與 HMI L&F 六本；本輪加掃本本亦查無。至此 `spec-index/sources/` 內**無已知未掃之候選**。
3. 本本之 `NTF4` 重號與 `NOTF7.1` 拼寫，為原文所有，**未代為調和**（依紀律不自行調和不符）。
