# RULINGS — Diagnostics (FW036)

Pei 之裁決與分析層自裁條文之逐字登記。條文一律照錄（R19-2：原文貼入，
不改寫、不摘要），執行層之回報另起段落。本檔為 Diagnostics 之裁決權威；
跨 feature 條文承接時註明來源包。

---

### R-DIAG1 — TC ↔ SWE1 為 N:1；三段式各列各自成 TC 群（Pei 裁，2026-09-17）

```text
R-DIAG1  TC ↔ SWE1 為 N:1；三段式各列各自成 TC 群
  (a) 每條 TC 之 Requirement or Design ID 只填一個 SWE1 ID；一條 TC 不得同時掛多個 SWE1 ID。
  (b) 一個 SWE1 ID 依 IN §8.3 sibling 軸可產多條 TC（例：negative response 列拆
      「無效長度」／「超範圍」／「不支援 DID」三條，全部掛同一 SWE1 ID）。
  (c) 三段式之 negative response 列與 Service Not Supported 列各自成 TC 群，
      不併回同 DID 之正向列；近似 TC 以 test_item 括號下半之 DID／SID／NRC 值作區分 token。
```

### R-DIAG2 — 重複 SWE1 ID 之處置（Pei 裁，2026-09-17）

```text
R-DIAG2  重複 SWE1 ID 之處置
  `SWE1-Diagnostics-340` 兩列（row 347 SYS-RA-DIAG-264 Audio、row 348 SYS-RA-DIAG-188 Clock Defrost）
  以 `SWE1-Diagnostics-340-001`（row 347）／`SWE1-Diagnostics-340-002`（row 348）區分，
  工作簿 Requirement ID 與 specification_reference 皆用此二號；不發 DR、不改 037。
```

### R-DIAG3 — Out of Scope 列不產 TC、保留原內容（Pei 裁，2026-09-17）

```text
R-DIAG3  Out of Scope 列不產 TC、保留原內容
  `SWE1-Diagnostics-057`（SYS-RA-DIAG-248，CFTS004 索引 Category = Out of Scope）
  不產 TC；工作簿保留一列，test_item 上半照抄 037 Description，
  Test Set 欄外之處置欄（execution 依 SWC 0708 之對應欄位實測後定）寫 `Out of Scope`，
  Remarks 註 `CFTS004 Category: Out of Scope`。coverage.tsv 以 `OUT_OF_SCOPE` 計，不計入未覆蓋。
```

### R-DIAG4 — 拼字與空白（Pei 裁，2026-09-17）

```text
R-DIAG4  拼字與空白
  (a) 037 之拼字（Caemera／senario／recevied／diagnopstic／bightness）與 CFTS004 原文
      在 test_item 上半 verbatim 照抄，不修；作者側四欄用正確拼字。
  (b) 037 之來源 ID／標題／描述之首尾空白（SYS-RA-DIAG-315 三列尾端 3 空格等）
      於 MANIFEST／coverage 比對前 strip；工作簿不得帶入。
```

### R-DIAG5 — DID 與 UDS 記法（IN §8.7.5 之本 feature [ADD]）（Pei 裁，2026-09-17）

```text
R-DIAG5  DID 與 UDS 記法（IN §8.7.5 之本 feature [ADD]）
  (a) 敘述層（test_item 上半、pre_conditions、expected_result 散文）：`DID $283F`，
      與 CFTS004 原文及 037 標題一致；037 混寫之 `0x283F` 在上半 verbatim 照抄，作者側一律 `$`。
      `$XXXX` 無尾 `$`，不受 lint P（`$MESSAGE.Signal$`）規制。
  (b) 執行層（test_procedure）：寫 UDS 位元組串，與 security 批次之 UDS 通道同式：
        2. Send UDS request 22 28 3F via diagnostic tool
        3. Check that positive response 62 28 3F <brightness byte> is received
      NRC 寫 `7F <SID> <NRC> (<label>)`，label 逐字取 CFTS004 用字
      （例 `7F 22 31 (Request Out of Range)`）。
  (c) SID／NRC／sub-function 值以 CFTS004 原文為準；原文未載者寫 `PENDING: DR-{n} <缺件>`，
      不得引 ISO 14229 通用表補值（IN §8.4.1）。
```

### R-DIAG6 — 037 Verification Method 空白之處置（Pei 裁，2026-09-17）

```text
R-DIAG6  037 Verification Method 空白之處置
  `SWE1-Diagnostics-189/190/191/192`（SYS-RA-DIAG-124/125）VM 空白；
  依同組 `-187/-188`（SYS-RA-DIAG-123，同型）之步驟型態產出，步驟自 Description ＋ CFTS004 原文推出，
  Remarks 註 `037 VM blank; procedure derived from Description + CFTS004`；不發 DR。
```

### R-DIAG7 — Harman Status 與 Region（Pei 裁，2026-09-17）

```text
R-DIAG7  Harman Status 與 Region
  (a) CFTS004 索引 `SYS2 HARMAN Status` 非空者（Need Rework 55／Need Clarification 1／Accepted 2），
      該來源之全部 TC Remarks 註 `Harman Scope: <status 原字>`；不影響產出與否。
  (b) Vehicle Model 七欄依 CFTS004 索引 `SYS2 限定地區 Region` 填 1／0（R-CAM 前例：598／5210 一律 0）；
      Region = All → 五個有效車型全 1；Region = NAFTA 系 → 依 forms/proxi 六平台之市場歸屬填，
      歸屬表由 recon 任務 3-7 產出後 Pei 裁。
```

### R-DIAG8 — 範圍（Pei 裁，2026-09-17）

```text
R-DIAG8  範圍
  (a) 只產 037 所收之 168 源 395 列；CFTS004 之 50 條未收 FR 不補產、不另立工作簿。
  (b) AME Diagnostics SYSRA 與 DTC（CS.00099）不另立工作簿。
  (c) 每列產 TC 前必須回看 CFTS004 該來源之原文與同 `$XXXX` 標題下之 Information 列，
      原文載有 037 Description 未展開之值域／子欄位／狀態者，依 IN §8.3 拆 sibling（延伸只向 CFTS004 原文，不向未收條目）。
```

### R-DIAG9 — Test Group、TC ID、Layer 2/3（Pei 裁，2026-09-17）

```text
R-DIAG9  Test Group、TC ID、Layer 2/3
  (a) Test Group = `Diagnostics`；TC ID = `NR1L-DIAG-{nnn}`。
  (b) Layer 2 走 DID 家族聚合（一個或數個相鄰 DID = 一 Test Set），候選見 §5；名稱歸 Pei。
  (c) Layer 3 = CFTS004 之 `$XXXX - <title>` 標題（43 個，含母節 Read/Write DIDs／I-O Control DIDs／Routine IDs），
      逐字，不入工作簿。
```

---

## 執行層回報（CDD-01，2026-09-17）

- **R-G23 取號現查**：`grep -rn "R-DIAG"` 於全 repo（排除本包下放檔 `down/20260917_CDD-01.md`）
  **零命中**；`docs/fw036/RULINGS.sha.tsv` 無 `R-DIAG` 列（該表現僅含 `R-SEC` 前綴）。
  `{live}` = **1** 成立，與下放包 §2 期望值一致。九條實際號為 **R-DIAG1～R-DIAG9**。
- **R-DIAG9(c) 之「43 個」與實測不符**：CFTS004 之 `$XXXX` Heading 總數為 **63**
  （R/W 38／I-O 15／Routine 10），其中被 037 引用者 **42**（R/W 23／I-O 14／Routine 5）。
  分析層之 43 = R/W 被引用 23 ＋ I-O **全部** 15 ＋ Routine 被引用 5；差之 1 為
  `$5007 - Mid-Range Settings`（CFTS004 有該節，037 未引用）。條文本體不改，事實記此。
- **R-DIAG3 之 Layer 2 歸屬與下放包 §5 散文不符**：`SWE1-Diagnostics-057` 之 CFTS004 母節為
  Read/Write DID Requirements、L3 = `$1801 - Screen Test Pattern (Read/Write)`，
  即 §5 之 **#10 Screen Test Pattern**，非 §5 所稱之 #11 `Audio Output Settings`。
  #11 之單列實為 `SWE1-Diagnostics-056`（SYS-RA-DIAG-222，正常 FR，**會產 TC**）。詳見上繳包 §5。
- **R-DIAG5(c) 於本 feature 之適用結果**：230 列 negative／unsupported 中，
  CFTS004 原文載有 NRC 值者 **5** 列、僅 037 載值者 **20** 列、**兩者皆無值者 205 列（89%）**。
  依 (c) 字面，該 205 列之 NRC 一律寫 `PENDING: DR-{n}`。此為 CDD-02 pilot 之阻斷點，
  已登 `DATA_REQUESTS.md` 與 `DECISIONS.md` [PROPOSED]，請 Pei 裁。
- **R-DIAG7(b) 之歸屬表**：已以 PROXI `Market_Area`（byte 160）逐平台實測產出，
  見 `data/vehicle_model_region.tsv` 與 DECISIONS §3。
