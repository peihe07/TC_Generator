# DATA_REQUESTS — Vehicle Setup Management R1L TBM（VF665 V43）

DR 送出權屬 Pei（Tier 3）；分析層草擬、登記。每包上繳附未結 DR 清單（IN §8.4.3）。
一 DR 一條目（`## DR-VTn`），表列摘要與條目同步更新。

| DR | 項目 | 阻塞 | 影響 | 狀態 | 送出日 | 回覆日 |
|---|---|---|---|---|---|---|
| DR-VT1 | VF665 V43 之 037（SWE1 分析報告）缺件 | yes（重錨前不得交付，R-VT18(c)） | 正式母體 | **Pei 裁定送出（2026-09-02「送＋三」），待 Pei 發送**；本線同時依 R-VT18 以 SYSRA 暫代進 P4 | | |
| DR-VT2 | V43 SYSRA DocID `VF655_V43_R3`（247 列）疑誤植；R3 vs R4；`Melco ID` 全空（A-VT9）；`Out of scope` 二拼法；重音三名（A-VT20）；拼字兩列（R-VT16(d)） | no（惟 171＋41 列之暫代母體邊界繫於此） | 暫代分母邊界 | 已登記，**建議與 DR-VT1 併送**（否則增補批永懸） | | |
| DR-VT3 | （重寫，R-VT13(d)）待重驗；R-VT15(b) 實測後候選僅餘 2 名 | no | 訊號實名 | 暫持，不送 | | |
| DR-VT4 | V43 內部訊號對照總表（83 名，形制照 DR-PW23） | **yes（P4 起）** | 內部訊號實名 | 已登記，**Pei 裁先不送（2026-09-02）→ P4 時 83 名只能 PENDING（R-P355）** | | |
| DR-VT5 | ATL-Mi DBC | ~~yes~~ | 全線 CAN 訊號 | **結案（2026-09-02，Pei 放件 `P363_BH-CAN [07338]_3A_R2.dbc`，R-VT15）** | | 2026-09-02 |

---

## DR-VT1 —— V43 之 037 缺件（阻塞）

- **來源**：intake 實測（2026-09-01）。現有 037 兩份
  （Park Sense And Restore Default Setting／Side Distance Warning Audio Repetition）之
  `Source Requirement ID` 152/152 皆為 `Sys-RA-VF665_V42_VSM-nnn`；`V43` 字串於兩檔命中 0。
  Pei 確認無其他 037 檔。
- **問題**：V43 SYSRA Functional 507 列無任何 SWE1 分析，本線無 TC 母體（R-VT4）。
- **阻塞**：是。P4 以後全部停等。
- **本地處置**：P0–P3 照常（scaffold、sources、recon、framework／profile 草案），
  使 037 到齊時可直接進 P4。
- **請求動作**：向 SWE1 報告作者索取 VF665 V43（R1L with TBM）之 037-A03 報告
  或其排程；並確認 V43 之 SWE1 分析是否以 V42 之 037 為基底延伸（若是，需明示差異列）。

## DR-VT2 —— SYSRA 之 DocID 與版次疑義（確認型）

- **來源**：intake 實測。`FMWIFSM035A02_VF665_V43_…SYSRA_VF665_V43_Release.xlsx`
  `Basic Report`：`SYS2 文件識別碼 Document ID` 欄值 `VF665_V43_R3` 951 列、
  **`VF655_V43_R3` 247 列**（其中 Functional 171 列）、空 82 列；
  `SYS2 來源需求項目ID` 欄另見 `VF665_V43_R4_P363`。規格檔為 `[VF665_V43_R4]`。
- **問題**：(a) `VF655` 是否為 `VF665` 誤植（VF655 若為另一 VF，該 247 列即他 VF 之需求混入）；
  (b) SYSRA 以 R3 分析而規格現為 R4，R3→R4 差異列是否已納入。
- **阻塞**：否（本線現無母體）。
- **本地處置**：recon 對該 247 列與 82 列分別標記，不併入任何計數之分母。
- **請求動作**：Pei 決定是否與 DR-VT1 併送。
- **佐證補充（2026-09-01，上繳 01）**：Functional 507 列內 `VF655` 171 列、DocID 空 41 列；`Melco ID` 0/507 非空（A-VT9 併本 DR）；
  Category `Out of scope` 55／`Out of Scope` 44（上游一致性同一面）。

## DR-VT3 —— 規格訊息名與 forms/ DBC 不符（R-13 型）

- **來源**：上繳 01 §七 7.4（`data/signal_chain_v43.tsv`），R-VT9(a) 改判為「訊息名不符(R-13)」28 列。
- **問題**：V43 R4 規格所載之
  (a) `TELEMATIC_VEHICLE_SETUP2.*` 九名：兩本 DBC 皆無該訊息（存在者為 `TELEMATIC_VEHICLE_SETUP`／`_SETUP3`），訊號名落在 `TELEMATIC_VEHICLE_SETUP`；
  (b) `IPC_VEHICLE_SETUP2.*` 九名：訊號存在但落在 `IPC_VEHICLE_SETUP`，而 `IPC_VEHICLE_SETUP2` 另有 34 個 AUX 類訊號；
  (c) `TELEMATIC_SERVICE_SETUP.*` 四名落在 `TELEMATIC_VEHICLE_SETUP`；`SERVICE_SETUP.*` 四名落在 `TBM_SCHEDULE_FD_2`、一名落在 `IPC_VEHICLE_SETUP`；`TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock` 落在 `IPC_VEHICLE_SETUP`。
  請確認 forms/ 之 `PDT27_E2A_R1_FDCAN8.dbc`／`R1_BHCAN2.dbc` 與 V43 R4 規格之版次對應，及該 28 名之正確訊息。
- **阻塞**：否（本線無母體）；對 vsm_v42 同型訊號亦適用，vsm_v42 W-5 完成後合併列表。
- **本地處置**：保留規格原名（R-13），段 3 命中記旁證，候選非認定。
- **請求動作**：Pei 決定送出；建議與 DR-VT1／VT2 三項併送。

> **重寫（分析層 2026-09-01，R-VT13(d)，A-VT22）**：本 DR 原文**不得送出**。分析層實測 LID `CAN Mapping` 有獨立之 `Atlantis`（P–T）欄組，
> 本線（ATL-Mi）規格之 `TELEMATIC_SERVICE_SETUP.ClearPersonalDataReq`／`RestoreDefaultSettingReq`、`SERVICE_SETUP.*` 四名皆於該欄逐字命中，
> `TELEMATIC_VEHICLE_SETUP2`／`IPC_VEHICLE_SETUP3` 亦只見於該欄。所謂「不符」是 forms/ DBC 屬 Atlantis High 而本線屬 ATL-Mi。
> 本 DR 改為：待 DR-VT5（ATL-Mi DBC）到件後重驗 28 列；仍不符者再以新文送。狀態：暫持。

## DR-VT5 —— ATL-Mi 之 DBC（阻塞 P4；與 vsm_v42 DR-VL3 同件）

- **來源**：R-VT13(b)／A-VT22。實測見 vsm_v42 DR-VL3（同一實測，不重拄）。
- **問題**：須取得 ATL-Mi（V43 P363；V42 P637 同）之 CAN-B／CAN-C DBC，與 LID `Atlantis` 欄同世代。**先問 Pei 手上有無**；無則送出。
- **阻塞**：是（P4 起）。到件前 CAN 訊號一律「段3待ATL-Mi DBC」。
- **本地處置**：段 1 以 Atlantis 欄解至段 2；對 Atlantis High DBC 之實查併記旁證。
- **請求動作**：Pei 先答「有／無」。

## DR-VT4 —— V43 內部訊號之驅動與觀察方法對照總表

- **來源**：上繳 02 §二-2／§八-1。規格內部訊號 88 名（`X.Req` 62 型／`X.Info`／`X.GUI`），段 1 對 forms/ 七檔
  逐字＋擴充比對後 **83 名止於段 1**；LID `Logical Identifier` 欄不收 `X.Req` 形名，放寬分隔符僅 +1。
  瓶頸非比對規則，而是 forms/ 無「內部訊號 ↔ 可觀察面」對照表。PM 線同題以 DR-PW23 之對照總表解（R-P355(a)）。
- **問題**：請上游（SYS2／HMI 設計方）提供 V43 各內部訊號之 (a) 驅動方法（對應 HMI 設定項名→路徑→值，或 PROXI 參數）、
  (b) 可觀察面（對應 CAN 訊號 `MESSAGE.Signal`、UI 元件、或 log 具名行）；形制照 DR-PW23 之回覆表。
  名單取 `features/vsm_v43/data/signal_chain_v43_v2.tsv` 類別＝內部且結果＝未解得(止於段1) 之 83 列。
- **阻塞**：否（本線無母體）；037 到齊後 P4 起阻塞（R-P355(b)：尚無對照者只能 PENDING）。vsm_v42 同型需求於其 W-5 後另登。
- **本地處置**：先以 R-VT11(b) 對 HMI Settings List／PROXI Format 擴充比對收一部分；其餘保留原名不加 `$`（IN §8.7.5(d)）。
- **請求動作**：Pei 決定送出；可與 DR-VT1／VT2／VT3 四項併送。
