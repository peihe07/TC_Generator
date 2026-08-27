# DATA REQUESTS — SW Update (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/sw_update/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM／Privacy）**：任何新發現之外部引用，登記 anomaly
的同時必須新增一列於此表；且每次 session opener 與 batch gate 都要按
Urgency 回報。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| — | **本輪 0 筆** | — | — | — | — | — |

## 本輪（下放包 01 + 02，2026-08-27）之結案記錄

Q5 裁定不發 DR，本輪執行後**維持 0 筆**。逐項確認：

- **CFTS_57 Reflash 原件**：不需 DR —— repo 側為真 OOXML（A-SU1），
  R-SU4 v2(a) 之 Q3 裁定照舊。
- **HMI 規格本文**：不需 DR —— 真 PDF 1.6，68 頁全文字層（A-SU1／R-SU6 v2）。
- **VF747**：已在 `inputs/`，並已綁定於 `feature.yaml` 之 `reference.vf747`。
  A-SU2 之 10 個 VF747 族 source id 因此**不構成外部引用**，不入本表。
- **PROXI**：`Brand_Configuration_2`（SWE1-FOTA-208 引用）於
  `forms/PROXI_HDCC27_R3_20250424.xlsx` `Format` 表 row 566 查得，
  已綁 `reference.proxi`，不需 DR。
- **Pop Up List**：`forms/Pop Up List HMI R1 (26PI).xlsx` 在場；
  A-SU3 之 `PU971` 為清單內查無，屬判讀問題非缺件，**不發 DR**。
- **DBC / LID**：037 無 CAN frame 與 Logical Identifier 引用（T4' 掃描），
  無外部引用可登記。

Standing rule 照常生效：日後新發現之外部引用仍須於登記 anomaly 之同時新增一列。
