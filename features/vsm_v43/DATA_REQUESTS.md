# DATA_REQUESTS — Vehicle Setup Management R1L TBM（VF665 V43）

DR 送出權屬 Pei（Tier 3）；分析層草擬、登記。每包上繳附未結 DR 清單（IN §8.4.3）。
一 DR 一條目（`## DR-VTn`），表列摘要與條目同步更新。

| DR | 項目 | 阻塞 | 影響 | 狀態 | 送出日 | 回覆日 |
|---|---|---|---|---|---|---|
| DR-VT1 | VF665 V43 之 037（SWE1 分析報告）缺件 | **yes** | 全線（母體 = 0） | 已登記，建議送出 | | |
| DR-VT2 | V43 SYSRA DocID `VF655_V43_R3`（247 列）疑為 `VF665` 之誤植；SYSRA 記 R3 而規格為 R4；`Melco ID` 於 Functional 507 列全空（A-VT9）；`Out of scope` 二拼法 55／44 | no | 追溯欄 | 已登記，未送出 | | |
| DR-VT3 | V43 R4 規格之訊息名與 forms/ DBC（R1_FDCAN8／R1_BHCAN2）不符 28 列：`TELEMATIC_VEHICLE_SETUP2` 全無、`IPC_VEHICLE_SETUP2.*` 九名落在 `IPC_VEHICLE_SETUP`、`SERVICE_SETUP.*` 落在 `TBM_SCHEDULE_FD_2` | no（本線無母體）| 訊號實名 | 已登記，建議送出 | | |

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
