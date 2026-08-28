# DATA_REQUESTS — Popup

依 IN §8.4.3（S6）：缺件欄位落 `PENDING: DR-POP{n} <缺件名>` 佔位，
不留空、不填 NA、不造值。每包上繳附本表未結清單。

| DR | 項目 | 證據 | 受影響範圍 | 狀態 | 送出日 |
|---|---|---|---|---|---|
| DR-POP1 | `HMI Popup List` 文件（popup 逐條 timeout 值、multi-task popup 之界定、文案／模板） | GP4-1 逐字："timeout is defined in Pop-up List document"（037 E10）；GP4-4 例外之適用清單無來源 | SWE1-POP-002-01（timeout 值）、-002-03（啟用實例）、-002-05（multi-task popup 之選定） | **RESOLVED（2026-08-27）**：標的已在 repo `forms/Pop Up List HMI R1 (26PI).xlsx`（SR24 Post 2A CR25802），經 Pei 納入（R-POP6，A-POP2）；不送上游。殘留兩點（CR 版位、(26PI) 適用性）隨 RD-1 確認 | （不送） |
| DR-POP2 | `HMI Popup List Priority Matrix` 文件 **SR24 Post 2A 現版**（repo `forms/` 存 SR24 1A (May 3 2021) 舊版，早於基線兩代，R-POP7 裁不納入） | spec 5.1 逐字引用（SYS1 NRL-168283）；queue／priority 行為之唯一具名來源 | 現有 5 leaf 無直接引用；屬 R-POP2 範圍缺口之上游件 | 已登記，未送出 | （空） |
| DR-POP3 | SWE1-POP-002 之 VC 引用 `SWE1-POP-004-01`～`-05` 於本簿不存在，請上游確認實指（形似 -002-01～-05 之誤植，依 IN §8.4.1 不推定） | 037 S9 逐字五行 | 追溯台帳之母子對映註記 | 已登記，未送出 | （空） |
| DR-POP4 | multi-task popup 之完整例外清單，並請上游具名 GP4-4 所舉 `search keyboard` 對應之 PU | SYS1 5.6 GP4-4 逐字；Pop Up List 三 sheet 全欄實測：`search keyboard` 連續詞組命中 0，同列兼含 `keyboard` 與 `search` 之 PU 列 0（詳 A-POP8） | SWE1-POP-002-05 之額外實例；**不阻斷**本輪生成（R-POP14 採規格原句） | 已登記，未送出 | （空） |

## 分析層裁示（2026-08-27，回應下方執行層回報）

- 執行層「DR-POP1 之結案不涵蓋 -002-05」之指正**採納**，且其實測正確（分析層
  獨立重測 Main 分頁亦得 `keyboard` 15 列、無一列載「選擇後 popup 保持開啟」語義）。
- 惟**結論不同**：-002-05 之命題不依賴 Pop Up List。GP4-4 為規格自載之行為
  陳述，`e.g in the search keyboard` 是規格自己的舉例而非向 Pop Up List 之委派
  （對照 GP4-1 逐字 `timeout is defined in Pop-up List document` 才是委派）。
  故採 **R-POP14**：照規格原句生成，`spec_reference` 單行 `_5.6`，不引 PU，
  亦不落 PENDING。DR-POP4 另開但**不阻斷**。
- 「本輪 PENDING = 0」之實測取信；本 feature 至交付前應維持 0。

## 執行層回報（下放包 02，2026-08-27）

- **DR-POP1 之結案不涵蓋 `-002-05`**。該 leaf 之受影響點為
  「multi-task popup 之選定」，而 GP4-4 逐字所舉之 `search keyboard`
  於納入之 Pop Up List **三 sheet 全欄查無對應列**（`keyboard` 與 `search`
  同列命中 0）。詳 `ANOMALIES.md` A-POP8。
  `-002-01`／`-002-03`／`-002-04` 之實值已自該表逐字取得。
- **本輪 `PENDING:` 佔位 = 0**（`lint036.py --profile popup` 之 U 檢查
  全簿全欄實測 0）—— `-002-05` 依 IN §8.4.1 是**不生成**，不是落佔位。
- **未開新 DR**。A-POP8 之三個提案中僅「向上游索 search keyboard 之 PU
  具名」需開 DR-POP4，另兩個不需要；**開哪一個屬 Pei 裁定，執行層不預開**。
