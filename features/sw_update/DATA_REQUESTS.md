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
| **DR-SU1** | **靜默期間之安全相關通知條件清單**（pattern：規格側之 safety-related notification 條件表；來源未定，得為 CFTS_57 之補件或 SYSAD 之安全需求節） | **OPEN** | `SWE1-FOTA-176`（facet B） | `newR1L-SU-003`（v2）之 `pre`／`proc`／`er` 三欄各掛一**英文** `PENDING`；該 TC 不可執行 | — | **High** —— pilot 批已受阻，Silent Update 之 9 列尚有 5 列未撰 |

## DR-SU1 —— 詳（下放包 19 §四 TC-3）

`CFTS057-4907477` 與 037 `SWE1-FOTA-176` 皆僅稱
「necessary for **safety requirements**」，**未列舉何者為安全相關條件**。
無此清單則**無可執行之觸發步驟** —— TC-3 之 Procedure 第 3 步
（「觸發一項安全相關條件」）無從寫成實機可跑之動作。

依 IN §8.4.3 掛 `PENDING`，**不得自行舉例**（如 eCall、碰撞偵測）
—— 舉例即造值（下放包 19 §四）。

**執行層之補充實測**：

| 版 | lint | 說明 |
|---|---|---|
| v1（`sandbox/pilot01`，上繳包 18 §T32b） | **K=3／T=3／U=3** | K 與 T 為草案本身之缺陷（PENDING 說明以中文書寫，違 R-14）；U 為計數用 |
| **v2（`sandbox/pilot02`，上繳包 19 §T33a）** | **K=0／T=0／U=3** | 下放包 20 §四已英文化，K 與 T 清零；**U=3 為 DR-SU1 之三個佔位，仍在** |

v2 之三行佔位（逐字）：

```
pre  3. PENDING: DR-SU1 list of safety-related notification conditions applicable during a silent session
proc 3. PENDING: DR-SU1 step to bring one safety-related condition into effect
er   3. PENDING: DR-SU1 observable state showing the safety-related condition is in effect
```

**U=3 唯有 DR-SU1 落地方能清零** —— 其為 DR 之直接量度，非格式問題。

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
