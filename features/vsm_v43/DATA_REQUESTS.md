# DATA_REQUESTS — Vehicle Setup Management R1L TBM（VF665 V43）

DR 送出權屬 Pei（Tier 3）；分析層草擬、登記。每包上繳附未結 DR 清單（IN §8.4.3）。
一 DR 一條目（`## DR-VTn`），表列摘要與條目同步更新。

| DR | 項目 | 阻塞 | 影響 | 狀態 | 送出日 | 回覆日 |
|---|---|---|---|---|---|---|
| DR-VT1 | VF665 V43 之 037（SWE1 分析報告）缺件 | **yes** | 全線（母體 = 0） | 已登記，建議送出 | | |
| DR-VT2 | V43 SYSRA DocID `VF655_V43_R3`（247 列）疑為 `VF665` 之誤植；SYSRA 記 R3 而規格為 R4 | no | 追溯欄 | 已登記，未送出 | | |

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
