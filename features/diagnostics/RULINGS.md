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

### R-DIAG8(amend) — 母體依 037 V1 (3)（Pei 裁，2026-09-17）

```text
R-DIAG8(amend)  母體依 037 V1 (3)
  母體為 V1 (3) 之 166 源 389 列。V1 (2) 之 SYS-RA-DIAG-167/168 六列不產；
  167/168 回歸 CFTS004 未收 FR 清單（50 → 52），依 R-DIAG8(a) 不補產。
```

### R-DIAG5(amend) — SID／NRC 值之來源層級（Pei 裁，2026-09-17）

```text
R-DIAG5(amend)  SID／NRC 值之來源層級
  (c′) SID／NRC 值依序取：CFTS004 原文 → 037 Description／Title 明載值 → ISO 14229-1 標準碼。
       三者衝突時前者優先；衝突逐筆登 ANOMALIES。
  (d)  取 ISO 14229-1 標準碼者，限下列五碼，且只在 037 已述其失效型態時使用
       （IN §8.4.1 domain constant；CFTS004 自身以 $22／$31 引用同一標準）：
         0x11 serviceNotSupported                    ← 037「Service Not Supported」
         0x12 subFunctionNotSupported                ← 037「unsupported sub-function」
         0x13 incorrectMessageLengthOrInvalidFormat  ← 037「invalid length」／「incorrect format」
         0x22 conditionsNotCorrect                   ← 037「conditions not correct」
         0x31 requestOutOfRange                      ← 037「unsupported DID」／「out of range」
       ER 之 label 用 ISO 名稱；Remarks 註 `NRC per ISO 14229-1 (037 unspecified)`。
       037 未述失效型態者仍 `PENDING: DR-DIAG-1`。
  (e)  I/O Control 之 SID 0x2F 依 (c′) 第二層取 037 明載值（24 列），
       同母節其餘 90 列以同一 DID 之 037 明載值類推，Remarks 註 `SID per 037 <SWE1-ID>`。
```

### R-DIAG9(amend) — Layer 2/3 之實測修正（Pei 裁，2026-09-17）

```text
R-DIAG9(amend)  Layer 2/3 之實測修正
  (a) 被 037 引用之 Layer 3 為 42（R/W 23／I-O 14／Routine 5）；`$5007 - Mid-Range Settings` 未引用。
  (b) Test Set #11 `Audio Output Settings`（單列 SWE1-056）併入 #14 `Audio Tone Settings`；
      #21 `Clear Key Sense PIN` 維持獨立（§4.2 genuine outlier）。Layer 2 定為 20 個。
  (c) 跨母節依 DID 合一者共 6 個：$5000／$5001／$5008／$5009／$500A／$500C；Layer 3 各保留母節。
```

### R-DIAG7(amend) — Region → Vehicle Model 填法（Pei 裁，2026-09-17）

```text
R-DIAG7(amend)  Region → Vehicle Model 填法
  依 PROXI Market_Area 實測（up CDD-01 §7-2 表）：
    Region = All   → HDCC27 1／DT27 1／637 1／598 0／5210 0／2261 1／376 1
    Region = NAFTA → HDCC27 1／DT27 1／637 1／598 0／5210 0／2261 0／376 0
  空值僅 SYS-RA-DIAG-248（Out of Scope 列），不產 TC。
  `Toro_ATL_MI` Market_Area 之 Type = Not Used 記於 ANOMALIES，不影響填法。
```

### R-DIAG3(amend) — Out of Scope 列之處置欄（Pei 裁，2026-09-17）

```text
R-DIAG3(amend)  Out of Scope 列之處置欄
  處置欄 = `AF` `Test Result 測試結果`，值 `Out of Scope`；`AH` Remarks 註 `CFTS004 Category: Out of Scope`。
  該列 Requirement ID 照填 SWE1-057，TC ID 照序取號（不跳號），Test Set 依 L3 歸 #10 Screen Test Pattern。
```

### R-DIAG5(amend2) — `0x11` 之 037 觸發語含標題句式（Pei 裁，2026-09-17）

```text
R-DIAG5(amend2)  0x11 之 037 觸發語含標題句式
  R-DIAG5(amend)(d) 之 `0x11 serviceNotSupported` 觸發語，除 Description 之「Service Not Supported」外，
  含標題句式「Unsupported service requests」。SWE1-Diagnostics-157 由 PENDING_DR1 改 RESOLVED_ISO；
  DR-DIAG-1 餘 2 列（-156、-237）。
```

### R-DIAG10 — Priority 判準（草案，pilot 後 Pei 裁）（Pei 裁，2026-09-17）

```text
R-DIAG10  Priority 判準（草案，pilot 後 Pei 裁）
  P0  I/O Control 寫入（0x2F）與 Routine Control（0x31）之正向 TC —— 直接改變車機輸出或狀態
  P1  DID 讀（0x22）／寫（0x2E）之正向 TC；I/O、Routine 之 negative
  P2  DID 讀寫之 negative、全部 unsupported（0x11）
  P3  無
  Out of Scope 列不填 Priority（依 SWC 0708 該列空白慣例，執行層實測後定）
```

### R-DIAG11 — Out of Scope 佔列之 lint 豁免（Pei 裁，2026-09-17）

```text
R-DIAG11  Out of Scope 佔列之 lint 豁免
  `AF` Test Result = `Out of Scope` 之列，lint `I`／`M`／`R`／`Z` 豁免；`R1-DIAG`、`RM-DIAG` 仍檢
  （Requirement ID 須單值、Remarks 須含 `CFTS004 Category: Out of Scope`）。
  實作為 FEATURE_EXEMPT 之列級條件（非全 feature），供其他 feature 之 OOS 列沿用。
```

### R-DIAG12 — `I-cross` 之 Diagnostics 豁免（Pei 裁，2026-09-17）

```text
R-DIAG12  `I-cross` 之 Diagnostics 豁免
  比照 R-SEC15(j)：`FEATURE_EXEMPT["diagnostics"]` 加 `I-cross`。理由：ER 為 UDS 請求／回應斷言，無觀測窗。
```

### R-DIAG10(amend) — Priority 值域對齊 SWC 0708（Pei 裁，2026-09-17）

```text
R-DIAG10(amend)  Priority 值域對齊 SWC 0708
  P3 不用（SWC 0708 值域實測無 P3）；Out of Scope 佔列 Priority 留空。其餘不變。
```

### R-DIAG13 — I/O Control TC 之 security 前提（Pei 裁，2026-09-17）

```text
R-DIAG13  I/O Control TC 之 security 前提
  SID 0x2F 之 TC 一律含 Pre-Condition `Security access 0x27 has been granted`；
  pc_sources 註 SYSAD §4.5 保守套用；SYSAD 作者回覆不需者，依 R-G72 於下一 Revise 移除。
```

> **判定法依 CDD-04 追補 A §一**：母體以 `layer3_assign.tsv` 之母節為 I/O Control DIDs
> 反查，**不以 Procedure 有無 `$ 2F` 位元組串為條件** —— pilot `-006` 之觸發步驟整行為
> `PENDING: DR-DIAG-4`，無位元組串而仍屬 `0x2F` 之 TC。

### R-DIAG14 — 觸發鍵之選擇（Pei 裁，2026-09-17）

```text
R-DIAG14  觸發鍵之選擇
  按鍵狀態類 DID（$1820／$1821）之觸發步驟不得選 Power／Dark 等會改變 HU 電源或畫面狀態之鍵；
  優先選導航類鍵（Up／Down／Select）。
```

### R-DIAG13(amend) — `SEC-DIAG` 母體排除 unsupported 型（Pei 裁，2026-09-17）

```text
R-DIAG13(amend)  SEC-DIAG 母體排除 unsupported 型
  R-DIAG13 之「SID 0x2F 之 TC」指實際送出 0x2F 者：positive 與 negative 型；
  unsupported 型送不支援之 SID，不在母體。lint SEC-DIAG 母體加條件 row_kind ≠ unsupported。
  已產之 unsupported 型 TC 不補 PC-3。
```

### R-DIAG15 — 佔位之追蹤（比照 R-SEC21）（Pei 裁，2026-09-17）

```text
R-DIAG15  佔位之追蹤（比照 R-SEC21）
  作者側四欄之 `<…>` 佔位一律登 `features/diagnostics/sandbox/placeholder_summary.tsv`
  （欄：TC ID／SWE1 ID／欄位／佔位文字／缺件 token DR-DIAG-n／來源節）。
  交付本可含佔位（U=0）但 `asset_request.md` 須載明「佔位填入前不得執行」；
  DR 回覆到件後依 R-G72 以 Revise 本填值。
```

### R-DIAG16 — 觀察不成步（IN §5.1 之本 feature 適用）（Pei 裁，2026-09-17）

```text
R-DIAG16  觀察不成步（IN §5.1 之本 feature 適用）
  Procedure 步驟只寫動作（送出／按壓／保持／讀取）；聽、看、觀察只入 ER。
  保持步驟固定句 `Hold for <n> s`，ER 寫該期間之可觀察結果。
```

### R-DIAG17 — lint `X` 之 Diagnostics 豁免（Pei 裁，2026-09-17）

```text
R-DIAG17  lint X 之 Diagnostics 豁免
  比照 R-DIAG12：FEATURE_EXEMPT["diagnostics"] 加 `X`。理由：本 feature 不寫導航 hop，X 之命中皆為 DID 名／CFTS004 用詞之字面。
```

### R-DIAG18 — Pre-Condition 之機械守門（IN §4.4 之本 feature 實作）（Pei 裁，2026-09-17）

```text
R-DIAG18  Pre-Condition 之機械守門（IN §4.4 之本 feature 實作）
  產生器與 lint `PC-DIAG`：Pre-Condition 行含 record／recorded／read／measure／send／sent／press／
  by a diagnostic command 者 FAIL；`*_initial` 只得於 Procedure 宣告並於 ER 使用。
```

### R-DIAG19 — KeySense HMI Logic and Flow 為缺件（Pei 裁，2026-09-17）

```text
R-DIAG19  KeySense HMI Logic and Flow 為缺件
  CFTS004-4940469 明引「KeySense HMI Logic and Flow」而該件不在來源集且 CFTS004 未載其版本；
  登 DR-DIAG-7（文件請求，對 Nik）。`-290` 之 ER 在到件前只斷言常式正回應與完成；到件後 Revise。
```

### R-DIAG20 — 常式（RoutineControl）之位元組式（Pei 裁，2026-09-17）

```text
R-DIAG20  常式（RoutineControl）之位元組式
  start `31 01 <RID>` [＋ routineControlOptionRecord]、stop `31 02 <RID>`、results `31 03 <RID>`；
  正回應 `71 <sub> <RID> …`。RID 不得以 0x22 讀。lint RT-DIAG 於 Routine 母節 TC 施檢。
```

### R-DIAG21 — 上半摘句（canon §4.3.1 R-3 之本 feature 適用）（Pei 裁，2026-09-17）

```text
R-DIAG21  上半摘句（canon §4.3.1 R-3 之本 feature 適用）
  test_item 上半 > 50 tokens 者，摘與下半測試目的直接相關之句或子句（逐字，不改寫），
  其餘以 specification_reference 指回；lint L 不豁免。
```

### R-DIAG22 — 長度軸 negative 之請求寫法（Pei 裁，2026-09-17）

```text
R-DIAG22  長度軸 negative 之請求寫法
  「invalid length / incorrect format」軸之 Procedure 請求 = 該 DID／RID 之合法請求省去最後一個 byte；
  描述行綴 `with the last byte omitted`；ER `7F <SID> 13 (incorrectMessageLengthOrInvalidFormat)`。
  值域軸之請求保留完整長度，以 `<out-of-range value>` 或 CFTS004 明載之越界值填資料位元組。
  lint NEG-DIAG：長度軸 negative 之請求串不得與同 DID／RID 之正向請求串相同。
```

### R-DIAG22(amend) — 值域軸依 SID 分型（Pei 裁，2026-09-17）

```text
R-DIAG22(amend)  值域軸依 SID 分型
  0x22 讀類：negative 第二條為「unsupported DID」型，請求 `22 <unsupported DID>`（佔位，token DR-DIAG-6），ER `7F 22 31`。
  0x2E／0x2F／0x31：值域軸請求保留完整長度，資料 byte 為 `<out-of-range value>` 或 CFTS004 明載越界值。
  DR-DIAG-6 改題為「不支援之 SID 與 DID 清單」。
```

### R-DIAG20(amend) — 與 R-DIAG22 之重疊（Pei 裁，2026-09-17）

```text
R-DIAG20(amend)  與 R-DIAG22 之重疊
  長度軸截斷串（描述行含 `with the last byte omitted`）不受 RT-DIAG 之「RID 須兩 byte」判準拘束。
```

### R-DIAG23 — 延伸審計（交付前必經）（Pei 裁，2026-09-17）

```text
R-DIAG23  延伸審計（交付前必經）
  對 389 列逐列比對三個延伸來源，產 `extension_audit.tsv`（列／來源／原句／現有 TC 是否已斷言／候選 sibling／錨）：
  (a) 037 Description 之定型句列舉之失效型態；(b) 037 Verification Criteria／Method 欄所述情境；
  (c) 該列所引錨之同節 Information 列中補充該 FR 之列舉／值域。
  候選只列不產；Pei 裁後於 Revise 產出。canon §8.3 之環境／持久軸因 CFTS004 零載，於 coverage 說明明記「未延伸之由」。
```

### R-DIAG24 — SWE1 = 037 全欄；VC／VM 為 sibling plan 之必讀輸入（Pei 裁，2026-09-17）

```text
R-DIAG24  SWE1 = 037 全欄；VC／VM 為 sibling plan 之必讀輸入
  (a) 037 之 Verification Criteria／Verification Method 欄與 Description 同為 SWE1 依據；
      sibling plan 逐列抽出 VC/VM 之情境詞（狀態／條件／邊界／逾時／重試／各欄位…），每一情境至少一條 TC。
  (b) 情境之值依序取：該列所引錨 → 同 $XXXX 節內之 CFTS004 列舉／值域（引兩錨）→ `<…>` 佔位（R-DIAG15 登錄）。
      VC/VM 只供情境，不供值（IN §8.4.1）。
  (c) VC/VM 之 unit／integration 字樣不在 SWE.6 層級，略過；純 boilerplate 句（無情境詞）不產。
```

### R-DIAG25 — 詳細度（Pei 裁，2026-09-17）

```text
R-DIAG25  詳細度
  (a) 一列所引錨或其 VC/VM 列舉之每一狀態／值，各成一條 sibling（狀態軸），PC 寫該態、ER 斷言該態下之回報；
      態之建立方式 CFTS004 未載者不寫步驟，只寫態（§8.5 例外）。
  (b) 同節其他列已各自成 TC 之欄位，不重複斷言（§8.2.1 不變）；但該列自身之錨列舉多個值／子項者，ER 依 §6.1 逐項。
  (c) 單一 SWE1 列拆分上限 8；超過者回報不產，Pei 裁。
```

### R-DIAG25(amend) — 離散值之拆法（Pei 裁，2026-09-17）

```text
R-DIAG25(amend)  離散值之拆法
  錨列舉之離散值 ≤ 8 → 逐值各一條（design_method 功能測試）；> 8 之連續值域 → BVA 兩式（CDD-05 追認）。
```

### R-DIAG26 — CFTS004 原始文件為來源（IN §8.6）（Pei 裁，2026-09-17）

```text
R-DIAG26  CFTS004 原始文件為來源（IN §8.6）
  CFTS004 之 Polarion 索引匯出（sys2_cfts004_general_diag）不含列舉列表；交付前須取 CFTS004 原始文件
  （docx／pdf）登錄 MANIFEST，引言句之列表以原始文件為錨（`CFTS004-{ObjectID}` 不變，Remarks 不另註），
  依 R-DIAG23(c) 補產。未取得 → DR-DIAG-10，交付本 coverage 說明明記。
```

### R-DIAG27 — 交付形式（沿 R-SEC25 前例）（Pei 裁，2026-09-17）

```text
R-DIAG27  交付形式（沿 R-SEC25 前例）
  單一工作簿；列序依 037 列序（SWE1 ID 升冪，`-340-001`/`-002` 依 037 row）；TC ID 依交付列序重編為 NR1L-DIAG-001 起連號，
  附 `id_map_v08_to_delivery.tsv`；Test Set 欄保留不作排序鍵；佔位列整列著色 FCE4D6（沿 R-SEC 前例，文字不動）；
  檔名 `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Diagnostics_<YYYYMMDD>.xlsx`；
  Cover 版本／日期／作者、Product Document 依 SWC 0708／Home 0809 實測填；核准／審查／中文作者三格留給 Pei。
  specification_reference 維持 §10.7(a) `CFTS004-{ObjectID}`（7 位 Polarion 物件號，同 SWC 0708 之 `CFTS042-4813401` 式）。
```

### R-DIAG28 — CIP Radio Tables v6.7 為 `$0307`／`$0309` 之流程來源（Pei 裁，2026-09-17）

```text
R-DIAG28  CIP Radio Tables v6.7 為 $0307／$0309 之流程來源
  (a) `forms/CIP_Radio_Tables_v6.7.xlsx` 登 FORMS.md（六欄）與 MANIFEST（doc_id `cip_radio_tables_v6_7`，features `diagnostics`）。
  (b) MPFA Validate／Select 兩流程圖轉錄為 `features/diagnostics/data/cip_mpfa_flowcharts.md`（逐節點文字＋NOTE 逐字），
      錨記法 `CIP_Radio_Tables_v6.7:MPFA Validate Process`／`…:MPFA Select Process`，於 Remarks 引用；
      specification_reference 維持 CFTS004 ObjectID（CFTS004-4940451/4940462 等已明引該流程）。
  (c) retry 軸之 sibling 依流程圖 NOTE 五種結局各一條：600 ms timeout ×3 → $FF；0x03 ×3 → 0x03；0x0D ×3 → 0x0D；
      0x0F ×3 → 0x0F；混合 → $FF。PC 寫 X65 之回應態（如 `The Sirius XM chipset returns Indication Code 0x03 to each package validate command`），
      不寫建立步驟（§8.5 例外）。
  (d) `<Package Indication value>` 佔位維持（sales code → PkgIndex 對照不在本檔）；DR-DIAG-8 改 PARTIAL：流程圖已到，
      餘 `SX-9830-0095` 本文與 PkgIndex 對照表。
```

### R-DIAG29 — CS.00100 Table 51 為 I/O Control 之 IOCP 位元組來源（Pei 裁，2026-09-18）

```text
R-DIAG29  CS.00100 Table 51 為 I/O Control 之 IOCP 位元組來源
  (a) 0x2F 請求一律書 `2F <DID> <IOCP> [<controlState>]`，IOCP 逐字取 Table 51：
      00 Return Control to ECU／01 Reset to Default／02 Freeze Current State／03 Short Term Adjustment。
      CDD-04 之「ISO IOCP 通用值禁用」係因無 STLA 來源；今 CS.00100 為 STLA 來源，該禁令解除。
  (b) `<controlState>`（Table 51 NOTE 之 `XX`）仍為佔位 —— DR-DIAG-4 題目縮為「各 I/O DID 之 controlState 編碼」，
      不再含 IOCP 本身；`<option-name selection>` 佔位改寫為 `2F <DID> 03 <controlState for "<option-name>">`。
  (c) 037 列之 VC/VM 或 CFTS004 同節點述及「return control」「stop」「reset」者，得依 (a) 產 `00` sibling；
      述及 session 結束／逾時者，得依 CS.00099 §5.10.2.3-2 ＋ CS.00100 §5.1.5-4 產「S3 timeout → 控制權回收」sibling，
      timeout 值 5000 ms 取 CS.00099 Table 8。無此敘述者不產（§0 範圍）。
  (d) Control Enable Mask 只於 packeted DID（CS.00100 §5.6.1.2.1.3-1）；單參數 DID 之 TC 不得帶 mask。
```

### R-DIAG30 — Session 與安全序列之來源升級（Pei 裁，2026-09-18）

```text
R-DIAG30  Session 與安全序列之來源升級
  (a) `Security access 0x27 has been granted` 之 PC 來源由 SYSAD §4.5 改為併引 CS.00099 §9.3.3（序列 `10 → 27 → 2E/31`）；
      是否含 0x2F 仍**不定** —— SD.00049 附件到件前維持 R-DIAG13 保守；DR-DIAG-10 登記該附件。
  (b) 037 有 session 軸敘述之列（FB-DIAG-m 之 `-048` 類），S3ECU 5000 ms 回 default 取 CS.00099 §5.5.6.2 為來源，
      可產「非 default session 閒置 5000 ms → 回 default session」sibling；ER 之 NRC 值若需 Annex A 者仍佔位。
  (c) 常式類：不需車速之常式於車速 > 0 拒絕（CS.00099 §6.2-8）—— 只對 037 VC 或 CFTS004 同節點述及車速者產 sibling。
```

### R-DIAG5(amend3) — NRC 來源鏈補一級（Pei 裁，2026-09-18）

```text
R-DIAG5(amend3)  NRC 來源鏈補一級（CDD-13 附錄 A 改寫）
  來源鏈 CFTS004 → 037 → CS.00100 Annex A → ISO 14229-1:2020 §7.5。
  (a) DR-DIAG-1 之 3 列（`-156`／`-157`／`-237`）依 Annex A 對應圖之第一個適用判斷取碼，PENDING 清零；`U` 應降至 0。
  (b) 既有 223 列：以 `nrc_coverage` 對照 Annex A —— 長度軸 `$13`、值域軸 `$31`、不支援 SID `$11` 預期全合；
      不合者才 Revise，回報差異表。
  (c) 新負向軸只在 037 Description／VC 或 CFTS004 同節點述及者產：安全未解鎖 → `$33`（2E/2F/31 類）、
      session 不符 → `$7F`、子功能不支援 → `$12`（$31 類）。無敘述者不產（R-DIAG8）。
```

## 承接之全域條（本 feature 適用）

- **R-G73** 裁決錨點前綴放寬至四字母 —— 本 feature 九條 `R-DIAG{n}` 因之得入 `RULINGS.sha.tsv`。
- **R-G74** Commander (598)／Regengade (5210) 全域一律 0 —— 由 R-CAM2(b) 升格，取代
  R-DIAG7(b) 所引之「R-CAM 前例」；`[A-DIAG04]` 之前例衝突據此結案。
- **R-G75** `RULINGS.sha.tsv` 之併發寫入過渡規則 —— 本 feature 每次動該檔皆依其 (a)(b) 行，
  上繳包依 (c) 記三個列數。成因為本 feature 實測之三次覆寫（`[A-DIAG15]`）。

兩條本體落 `docs/fw036/RULINGS_LEDGER.md`，此處只記承接，不複製本體（R-G52）。

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
