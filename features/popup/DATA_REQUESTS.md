# DATA_REQUESTS — Popup

依 IN §8.4.3（S6）：缺件欄位落 `PENDING: DR-POP{n} <缺件名>` 佔位，
不留空、不填 NA、不造值。每包上繳附本表未結清單。

| DR | 項目 | 證據 | 受影響範圍 | 狀態 | 送出日 |
|---|---|---|---|---|---|
| DR-POP1 | `HMI Popup List` 文件（popup 逐條 timeout 值、multi-task popup 之界定、文案／模板） | GP4-1 逐字："timeout is defined in Pop-up List document"（037 E10）；GP4-4 例外之適用清單無來源 | SWE1-POP-002-01（timeout 值）、-002-03（啟用實例）、-002-05（multi-task popup 之選定） | **RESOLVED（2026-08-27）**：標的已在 repo `forms/Pop Up List HMI R1 (26PI).xlsx`（SR24 Post 2A CR25802），經 Pei 納入（R-POP6，A-POP2）；不送上游。殘留兩點（CR 版位、(26PI) 適用性）隨 RD-1 確認 | （不送） |
| DR-POP2 | `HMI Popup List Priority Matrix` 文件 **SR24 Post 2A 現版**（repo `forms/` 存 SR24 1A (May 3 2021) 舊版，早於基線兩代，R-POP7 裁不納入） | spec 5.1 逐字引用（SYS1 NRL-168283）；queue／priority 行為之唯一具名來源 | 現有 5 leaf 無直接引用；屬 R-POP2 範圍缺口之上游件 | 已登記，未送出 | （空） |
| DR-POP3 | SWE1-POP-002 之 VC 引用 `SWE1-POP-004-01`～`-05` 於本簿不存在，請上游確認實指（形似 -002-01～-05 之誤植，依 IN §8.4.1 不推定） | 037 S9 逐字五行 | 追溯台帳之母子對映註記 | 已登記，未送出 | （空） |
