# ICS Management — 三層框架（framework.md）

- 建檔：2026-08-29（下放包 01）
- 狀態：**Layer 2 暫定**（12 RD ≈ 2 RD/set，逼近 IN §4.1.3「太細」門檻；
  俟首波 TC 數確定後複核 granularity，屆時可能合併 Test Set）
- 命名裁定（R-ICS1）：slug = `ics_management`，Test Group = `ICS`

## Layer 1 — Test Group

`ICS`

## Layer 2 / Layer 3 對照表

| Layer 2 Test Set | RD (SWE-ICS-) | Layer 3（spec 章節；不出貨） | 母文件狀態 |
| --- | --- | --- | --- |
| Volume Control | 001, 002, 005 | CFTS022 2.2 {4914970}、2.2.2 {4914991}；CFTS019 | CFTS019 缺（DR-ICS4）；005 受 A-ICS1 錯置暫緩 |
| Browse Control | 003, 004 | （無 CFTS022 對應） | HMI L&F 缺（DR-ICS6）— 不可動工 |
| Display Control | 006, 007, (011) | CFTS020 FS（缺） | CFTS020 FS 缺（DR-ICS5）— 不可動工。CFTS022 3.2.13/3.2.14（screen-off 設定）實測屬 Atl-Mid 域居多，不充錨 |
| Menu Navigation | 008, 009 | （無 CFTS022 對應） | HMI L&F 缺（DR-ICS6）— 不可動工 |
| Stuck Button | 010 | CFTS022 1.5 {4914953}（物件 4914954–4914958） | 齊備 — **可動工** |
| Camera Transition | (012) | SYSAD §4.10.1（本文缺，A-ICS5） | 缺文 — 不可動工 |

括號之 (011)(012) 為 SYS2 Traceability 所列、SWE1 Requirements 分頁缺列之項（DR-ICS2）。

## 適用域（R-ICS2，暫定）

CFTS022 物件適用判準：
`ECU ∋ {ICS, LTM}` ∧ `Radio ∋ {R1L, R1L-R, allSys}` ∧ `EE ∋ {Atlantis High, All}`
DUT 邊界待 DR-ICS9 上游確認；裁定收窄時受影響 TC 以 A- 登冊回收。

## TC ID

`NR1L-ICS-{NNN}`（循 popup 之 `NR1L-Popup-{NNN}` 既例，量測既有交付慣例而定，非新設）。
