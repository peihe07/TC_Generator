# framework.md — Popup

狀態：**LOCKED**（Pei 裁定 2026-08-27：R-POP4 定 Layer 1／2；R-POP8 定
spec_reference 錨定）。Part III 已經 R-G10 餘數驗證（5/5 leaf、2/2 Heading，
餘數與溢出皆空）。
Feature slug：`popup`
規範依據：IN §4.1（三層框架）、IN §4.2（Test Set）、FO §0（Tier 2：
framework Test Set derivation 屬 Pei 簽核）

---

## Part I — Layer 1（Test Group）

```
Popup
```

依 IN §4.1.1 與 R-POP1／R-POP4：Layer 1 = feature 名。本 feature 之規格
載體為 Core HMI Logic and Flow 之第 5 章（General Popup Behavior），
非獨立 spec 文件，故 Layer 1 取 feature 名 `Popup` 而非全文件標題
（全文件標題涵蓋 Mute／Swipe／Anti-Theft 等他 feature 射程）。
寫入工作簿 Test Group 欄，全簿逐字一致。

---

## Part II — Layer 2（Test Set，寫入工作簿）

單一組（R-POP4）。依 IN §4.2：英文名詞片語、不重複 Test Group 前綴。

| # | Test Set | 能力叢集 |
|---|---|---|
| 1 | `Pop-up Close` | popup 關閉之四途徑與例外：time-out、press second time、touch outside、selection、selection exception |

單一 Test Set 之依據：5 leaf 同屬「popup 關閉」一個 capability，共用
setup 形態（觸發一個 popup）與觀察對象（popup 顯示狀態）；IN §4.1.3
granularity test 通過（filter 得 5–7 TC 之有意義叢集，非 1 條、非全簿
—— 本 feature 全簿即此叢集，因 037 V0.2 範圍僅此）。queue／priority
若日後補件再增 Set（R-POP4）。

---

## Part III — Layer 3（規格章節分組，**不寫入工作簿**）

依 IN §4.1.5：Layer 3 僅存本檔。用途見 IN §4.1.4。

| Layer 2 | Layer 3 | 037 母號 | Heading 數 | leaf 數 | 規格節（037 C 欄逐字尾碼） |
|---|---|---|---|---|---|
| Pop-up Close | PC1（GP3／GP4 條族） | SWE1-POP-001、SWE1-POP-002 | 2 | 5 | `_5.5`（僅 POP-001 引用）、`_5.6`（POP-002 與全部 5 leaf） |
| **合計** | | | **2** | **5** | |

### 餘數驗證（R-G10）—— 全綠

實測 2026-08-27，`openpyxl`（`read_only=True, data_only=True`）讀 037
`Analysis Report` r8–r14（逐列，A 欄非空），依 G 欄分類：

| 判準 | 結果 |
|---|---|
| 合計 leaf = 母體 5（G 欄 = `Functional Requirement`） | **PASS** |
| Heading 已分類 = 2/2（G 欄 = `Heading`） | **PASS** |
| 餘數（全集 7 − 已分類 7）= 空 | **PASS** |
| 溢出（已分類 − 全集）= 空 | **PASS** |

執行層 recon（上繳包 01）之七列台帳同數，雙方各自實測（FO §8.3 第二層）。

### Heading 之台帳處置（R-POP5 [DEFAULT]，待 Pei 追認）

- SWE1-POP-002：`No TC — Heading; refer to child IDs -002-01..-05`
- SWE1-POP-001：`No TC — Heading; duplicated of SWE1-POP-002-02`
  （037 K8 逐字）—— 行為由 -002-02 之 TC 承載，非未驗（A-POP3 查證：
  GP3 與 GP4 第 2 途徑為同一行為之兩處敘述）

### 已知範圍缺口（R-POP2，記 COVERAGE_GAPS.md）

GP1（5.3）、GP2（5.4）與 queue／priority 本體無 SWE1 列 —— 不在
Layer 3 之列不是遺漏，是 037 V0.2 之範圍實況；RD-1 具名上報。

---

## Part IV — TC ID 與追溯欄

- TC ID：`{project}-POP-{NNN}`（IN §10.3），project 前綴依 feature.yaml 定義
- `Requirement or Design ID`：填 leaf 之 `SWE1-POP-002-{mm}`，逐字沿用
  上游；一 leaf 多 TC 同 ID 重複列出（IN §8.2.2）
- `specification_reference`（IN §10.7(b)，**無 override**）：值取 037
  `HMI Source ID` 欄逐字，帶章節尾碼：
  - -002-02 衍生 TC 併列兩行（R-POP8，升冪、前綴逐行重述）：
    `SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_5.5`
    `SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_5.6`
  - 其餘 leaf 單行 `_5.6`
  - 本 feature 無 CFTS 家族
- 值來源接線（R-POP6）：-002-01／-002-03／-002-05 之實值逐字取
  `forms/Pop Up List HMI R1 (26PI).xlsx`，選定 PU id 併記；
  PU 引文控制記法沿 IN §11 profile-scoped 例外（Home A-H10 前例）

---

## Part V — 變更紀錄

| 日期 | 變更 | 依據 |
|---|---|---|
| 2026-08-27 | 初版鎖定：Layer 1／2／3 定案、餘數驗證全綠、spec_reference 錨定（含 -002-02 併列兩節）、Pop Up List 值來源接線 | Pei 裁定（R-POP4／6／8）；下放包 01–02；A-POP2／A-POP3 處置 |
