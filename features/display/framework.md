# framework — Display（FW036）

- 落檔：2026-08-25（合併包 19 步驟 10）
- 內容出處：下放包 17 §二之草案全文，**逐字落檔，不增删**
- 狀態：**已由 Pei 2026-08-25 簽核**（`DECISIONS.md` §Sign-off 第 2 項）
  —— 簽核所結者為 Layer 2 之四組 Test Set；Layer 1 已由 R-DM1 定，
  Layer 3 僅存本檔、不入工作簿
- Test Group／Test Set 之寫入依 canon §2.1 之 BLANK 綁定
  （`feature.yaml` 之 `fill_test_group_set: true`）

> 本檔為 canon §4.1.2 步驟 5 所指之 framework 定版。
> Layer 3 之「待 Phase 2 查補」欄逐列列出尚未定錨者，
> **不得以空白代替**。

---

## 三層

### Layer 1 —— Test Group

`Display`（spec 模組名，R-C6；`feature.yaml` 已載）

### Layer 2 —— Test Set（4 組，寫入工作簿 H 欄）

| Test Set | leaves | 共同 setup 形態 | 命名依據 |
|---|---|---|---|
| `Operative State` | 001, 002, 003 | 電源狀態／喚醒操作 | 037 標題 `Display Operative State Management [ON/OFF/Wakeup]` |
| `Thermal Management` | 004, 005 | 溫度條件注入 | 037 Sub Categorization `Thermal Management`／`Thermal Protection Management` |
| `Pop Up Handling` | 006 | popup 觸發 | 037 標題 `Pop Up handling` |
| `Rear View Camera` | 007, 008 | RVC 觸發訊號 | glossary R-DM22 之 `RVC = Rear View Camera`；§4.2 禁縮寫入欄 |

§4.1.3 自檢：以任一 Test Set 過濾皆得 1–3 個 leaf 之 TC 群、
共享 setup 與入口，非逐 leaf 一組、無 Misc。單 leaf 之
`Pop Up Handling` 為真實離群（其 setup 與其他三組皆異），合於
「genuine outlier」例外。

### Layer 3 —— spec 章節分組（僅存 framework.md，不入工作簿）

| L3 | 對應 L2 | 已定錨之章節／列 | 待 Phase 2 查補 |
|---|---|---|---|
| `DM-OS` | Operative State | CFTS_020 splash 相關段（probe 命中 9 段，時段轉指 `{CFTS009-722}`） | 001/002 之 CFTS 條號 |
| `DM-TH` | Thermal Management | **CFTS `1.11.2.2 {4820281}`**（含 `{4820289}` `{4820290}`）；回復 `{4820287}` `{4820288}`；SYS2 r31–r34 | multi-stage（DR-DM4） |
| `DM-PU` | Pop Up Handling | Pop Up List `Main`（PU0130／PU0517 等）＋ Priority Matrix | popup↔leaf 歸屬逐條判 |
| `DM-RVC` | Rear View Camera | SYS2 r37/41/42/44/45/52/53/54（`SYS-RA-DM-036…053`） | r213–r226 區段之副本疑問 |

---

---

## 落檔複驗（執行層）

| 項 | 實測 |
|---|---|
| Layer 2 之 Test Set 組數 | **4** |
| 四組所涵蓋之 leaf | 001,002,003 ／ 004,005 ／ 006 ／ 007,008 = **8，無重複、無遺漏** |
| 與 `DECISIONS.md` 簽核第 2 項之四組名稱 | 逐字相符 |
| Layer 3 之列數 | 4，與 Layer 2 一一對應 |
