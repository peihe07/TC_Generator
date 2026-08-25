# Q2／Q3 裁定材料 —— Display

- 日期：2026-08-25
- 依據：下放包 10 §五步驟 6
- 性質：**已量測之事實**。凡未量測者逐處標「未量測」，不補推論
  （下放包 10 §六第 27 條）。分析層與執行層之偏好**不列入**。

---

## Q2 —— 驗證範圍

### Q2.1 037 之 8 個 leaf（全集）

| SWE-DM | Sub Categorization | Requirement Title |
|---|---|---|
| 001 | State Management | Display Operative State Management [ON/OFF/Wakeup] - ON/OFF states |
| 002 | Wake-up Management | …[ON/OFF/Wakeup] - Touch Based WakeUp |
| 003 | Startup & Wake-up Handling | …[ON/OFF/Wakeup] - Sleep and Splash |
| 004 | Thermal Management | …& Warning Pop Ups - Hot Algorithm & Warning Expectations |
| 005 | Thermal Protection Management | …& Warning Pop Ups - Hot Algorithm & Decisions of OFF/ON |
| 006 | HMI Popup Management | …& Warning Pop Ups - Pop Up handling |
| 007 | RVC Management | Display RVC Handling - Static |
| 008 | Dynamic Display Arbitration | Display RVC Handling - Dynamic |

8 筆之 `Categorization` 皆為 `Functional Requirement`，無 `Heading`。
（`recon.py` 與自寫腳本兩側皆得 8，逐 id 相符。）

### Q2.2 SYS2 之 Functional Requirement 母體

**80 列**（`Category` 正規化為 `functional requirement`）。

該母體之定義另有一項已驗之事實：SYS2 自帶之 `_polarion` 字典列有
`Non Functional Requirement` 為合法值，而主表**使用該值之列數為 0**。
即：**80 列之母體未遺漏 NFR**。

（同時記明：主表 333 列中有 **117 列（35%）**之 `Category` 值不在該
字典內，違規之拼法 `Out of Scope` 為多數 —— A-DM4。此不影響 80 之數，
因正規化後兩種拼法歸為同一類。）

### Q2.3 兩側之連結現況

| 連結方式 | 連上之 SYS2 列數 | 說明 |
|---|---|---|
| **id 層級**（037 之 `Sys-RA-Feature-ID(s)` 逐字比對 SYS2 之 id） | **0** | A-DM2。037 寫 `SYS-RA-DISP-001…008`，SYS2 之 id 含 `DISP` 者 0 |
| heading 錨（leaf 片語逐字出現於 SYS2 heading） | **4**（r31–r34） | 命中片語為 `'Hot Algorithm'`，同時屬 004 與 005 |
| glossary 錨（R-DM22 展開後逐字） | **12**（r37/41/42/44/45/52/53/54/213/217/219/226） | 命中 `Rear View Camera`，同時屬 007 與 008 |
| glossary_norm（R-DM25 正規化後） | 0（SYS2 側） | 底線正規化在 SYS2 側加 0 列 |
| **無候選** | **64** | 見 Q2.4 |

`candidate_from` 分布：heading only **4**／glossary only **12**／
兩者皆有 0／**無候選 64**。合計 80。

### Q2.4 64 列無候選之語意 —— 逐字寫明

依 **R-DM23**，該 64 列之語意為 **(3) 方法之界線**：

> heading 與 glossary 兩錨皆已施用而未接上；**非「已查證不存在」，
> 亦非「未追查」。**

**它不等於「不屬於本 feature 之範圍」。** 三種語意在本 feature 之其他
產出中各有其例，不得互相替代：
(1) 已依 R-G13 三要件查證而確認不存在（`signal_resolution.tsv` 之 2 列）；
(2) 本輪未追查（`proxi_candidates.tsv` 之全部 446 列）；
(3) 方法之界線（本處之 64 列）。

### Q2.5 其餘四個 leaf 之候選為 0 —— 成因

`SWE-DM-001`／`002`／`003`／`006` 之候選列數為 **0**。

**成因為「無逐字錨」，不是「SYS2 無對應需求」。** 已量測之佐證：

- SYS2 之 heading 中無任何一個逐字含此四者之 leaf 片語
  （`State Management`／`Wake-up Management`／`Sleep and Splash`／
  `Pop Up handling` 等）
- glossary 目前只有 `RVC` 一條能用於這些 leaf 之外的比對；
  037 用 `DISPLAY_ON`／`DISPLAY_OFF`（001／002）而 SYS2／DBC 用
  `DISP_ON`／`DISP_OFF`，**逐字不等且無並列出處可建 glossary 條目**
  （A-DM18、DR-DM8）
- **未量測**：這四個 leaf 在 SYS2 中是否有語意上對應之列。
  以逐字錨判定不出來，而非逐字之判定為本專案所禁（R-DM13）

### Q2.6 兩個選項之交付形態與已知代價（不含偏好）

**選項 A —— 僅以 037 之 8 個 leaf 為驗證範圍**

- 交付形態：8 個 leaf 之 TC，`req_id` 為 `SWE-DM-nnn`（形態見 Q3）
- 已知代價：
  - SYS2 之 80 列中，**64 列與任何 leaf 無逐字連結**，其是否在範圍外
    **未經查證**（Q2.4）
  - SYS2 之 **7 個 `SW` 分類列（r17／r18／r245–r249）之 `candidate_from`
    全部為空** —— 七列皆與 8 個 leaf 無任何逐字連結。
    其是否為 Display 之軟體需求**未量測**
    （r17／r18 之內容為供應商協作條款，見下放包 01 §3.3）
  - 037 八條皆不含具體值（0/8 數值、0/8 訊號、0/8 外部引用，
    A-DM18／R-DM27），值須全部另求；而 SYS2 那 80 列**帶訊號與值**
    （15 個相異訊號、13 個值 token）

**選項 B —— 含 SYS2 之 80 列**

- 交付形態：以 SYS2 列為母體之 TC，`req_id` 需另定（SYS2 之 id 形態為
  `SYS-RA-DM-nnn`／`SYS2-RA-nnn`，與 037 之 `SWE-DM-nnn` 無 id 橋樑）
- 已知代價：
  - **037 為 SWE.1 之交付物，而 SWE.6 對其負責** —— 以 SYS2 為母體
    等於跨層取材，其正當性**未量測**（屬流程裁定，非量測問題）
  - 80 列中 **48 列**（60%）之 heading 祖先為
    `r72 2.2 Serializer Touch Interrupt PIN Definition`，該 heading 講的是
    序列器觸控中斷之接腳定義，與顯示行為無關 —— 母體之內部結構已知為
    退化（A-DM11 限制 1）
  - SYS2 後半段（`SYS2-RA-*` 區段）之 20 個 heading 節點中，
    節點名與前半段**大量重複**（`Rear Camera Events` 等各出現兩次），
    **是否為同一物之兩份副本未查證**（上繳 06 §5.1，無條文在追）

---

## Q3 —— `req_id` 之形態

### Q3.1 兩種寫法之出處與出現次數（037 內，逐分頁）

| 分頁 | `SWE-DM-nnn` | `SWE1-DM-nnn` | 分頁之性質 |
|---|---|---|---|
| `SWE1 Requirements` | **8** | 0 | **需求本體**所在（含 Title／Description／Priority／Verification 各欄） |
| `SYS2 Traceability` | 0 | **8** | 衍生索引（僅 5 欄：SWE1 ID／Source NRL ID(s)／Sys-RA-Feature-ID(s)／SW-HW 分類／Title） |
| `Excluded NRLs (HW-only)` | 0 | 0 | 與 leaf id 無關（載 Melco ID） |
| **合計** | **8** | **8** | |

### Q3.2 兩種寫法在其他三份素材中之出現

| 素材 | `SWE-DM-` | `SWE1-DM-` |
|---|---|---|
| SYS2 `Basic Report`（333 列） | **0** | **0** |
| CFTS_020（全文＋表格） | **0** | **0** |
| SYS3 SYSAD（全文＋表格） | **0** | **0** |

**兩種寫法皆只存在於 037 一份文件之內。** 外部素材對此無偏好可言。

### Q3.3 對下游欄位之影響

- 036 母本之 **D 欄** `Requirement or Design ID 需求/設計 ID` 為 `req_id`
  之落點（recon 與自測皆解出 D）。另有 **C 欄**
  `Requirement or Design ID (Polarion)`，本 feature **未使用**
- **B 欄之編號公式以 D 欄為條件**：`=IF(ISBLANK($D{row}),"",ROW()-9)`。
  D 欄一經填入，序號自動產生（R-DM15）
- TestRail 對應之 **E／F 欄**（`Test Case ID`）與 `req_id` 無關，
  本項不影響
- **未量測**：TestRail 或上游是否對 `req_id` 之形態有既定要求 ——
  四份素材中無此資訊

### Q3.4 一項須併同考慮之已知事實

037 之兩個分頁對**同一物件**使用兩種寫法，此事本身已以 **A-DM1** 登記
為上游不一致。無論裁定採何者，**A-DM1 不因此結案** ——
它記的是「上游文件內部不一致」，不是「我們該用哪一個」。

---

## 本材料未涵蓋者（逐項列出，不補推論）

1. 64 列無候選者是否在範圍外 —— **未查證**（逐字錨判定不出來）
2. `SWE-DM-001/002/003/006` 在 SYS2 是否有語意對應列 —— **未量測**
3. SYS2 後半段重複節點是否為同一物之副本 —— **未查證**
4. r245–r249 五個 `SW` 列是否為 Display 之軟體需求 —— **未量測**
5. TestRail／上游對 `req_id` 形態之要求 —— 四份素材中**無此資訊**
6. 選項 B 之跨層取材正當性 —— 屬流程裁定，**非量測問題**
