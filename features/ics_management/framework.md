# ICS Management — 三層框架（framework.md）

- 建檔：2026-08-29（下放包 01）；修訂：2026-08-29（下放包 02，R-ICS9 納 CFTS020 為第二來源）
- 狀態：**Layer 2 暫定**（12 RD ≈ 2 RD/set，逼近 IN §4.1.3「太細」門檻；
  俟首波 TC 數確定後複核 granularity，屆時可能合併 Test Set）
- 命名裁定（R-ICS1）：slug = `ics_management`，Test Group = `ICS`

## Layer 1 — Test Group

`ICS`

## Layer 2 / Layer 3 對照表

| Layer 2 Test Set | RD (SWE-ICS-) | Layer 3（spec 章節；不出貨） | 母文件狀態 |
| --- | --- | --- | --- |
| Volume Control | 001, 002, 005 | CFTS022 2.2 {4914970}、2.2.2 {4914991}；CFTS019 | CFTS019 缺（DR-ICS4）；005 受 A-ICS1 錯置暫緩。**b01 已出 V1/V2/V3**（存續繫於 DR-ICS9） |
| Browse Control | 003, 004 | CFTS020 1.8.1.2 Rotary Knob Data Transfer {4819577} | 母條已尋獲（R-ICS9）— **b02 偵察**，未生 TC |
| Display Control | 006, 007, (011) | CFTS020 1.8.1.1.1 {4819556}（6/8 適用）、1.8.1.1.3 {4819570}（6/6 適用）；1.5.1.1.2 {4819389} 實測 PowerNet-only，不適用 | **已解鎖**（R-ICS15(a)）— **b03 已出 8 條**（P1–P4／S1–S4）；granularity 判**健康**（共用 setup 與 entry path） |
| Menu Navigation | 008, 009 | CFTS020 1.8.1.1 {4819542}、1.8.1.3 Button Press Events {4819587} | 母條已尋獲（R-ICS9）— **b02 偵察**，未生 TC |
| Stuck Button | 010 | (i) DTC 面：CFTS022 1.5 {4914953}（物件 4914954–4914958）；(ii) ignore 面：CFTS020 1.8.1.4 {4819615}（物件 4819617）；1.4.1.3.1 {4819296}（DTC 成熟條件） | (i) **b01 已出 S1/S2/S3**；(ii) **b02 補寫**（R-ICS9(c)） |
| Camera Transition | (012) | SYSAD §4.10.1（本文缺，A-ICS5） | **轉 out-of-scope-pending**（b03 審查）— 無 RD 在案（需求分頁缺列，DR-ICS2）且無母文（A-ICS5），filter 永遠為空，不成 Test Set（IN §4.1.3）。DR-ICS2 補列且納源（RVC+PAM）後得復活 |

括號之 (011)(012) 為 SYS2 Traceability 所列、SWE1 Requirements 分頁缺列之項（DR-ICS2）。

## 適用域（R-ICS2，暫定）

CFTS022 物件適用判準：
`ECU ∋ {ICS, LTM}` ∧ `Radio ∋ {R1L, R1L-R, allSys}` ∧ `EE ∋ {Atlantis High, All}`
DUT 邊界待 DR-ICS9 上游確認；裁定收窄時受影響 TC 以 A- 登冊回收。

## TC ID

`NR1L-ICS-{NNN}`（循 popup 之 `NR1L-Popup-{NNN}` 既例，量測既有交付慣例而定，非新設）。
