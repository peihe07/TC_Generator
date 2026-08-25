# 上繳包 19 —— 合併包執行；**步驟 13 觸發停止條件 46，未產出 TC**

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/19_consolidated.md`
- 結果：**步驟 1–12、15 完成；步驟 13（生成 TC）觸發停止條件 46，已停。
  步驟 14 隨之無標的**
- 全部 git 操作屬 Pei —— §10 只備妥訊息與 pathspec，未執行

---

## 0. 先講：TC 未產出，因為指定之值在指定之出處裡不存在

18 §二.2 指定顯示狀態之值標籤為 `DISP_HOT`／`DISP_OFF`／`DISP_NORMAL`，
出處為「`data/signal_resolution.tsv`，三段鏈解至 DBC，名稱依 R-DM43
取訊號側」。逐字查證：

| 標籤 | DBC `VAL_` | LID `Format` | 全 DBC 逐字掃描 |
|---|---|---|---|
| `DISP_HOT` | **有**（raw 4） | **有** | BHCAN2 3 次 |
| `DISP_OFF` | **無** | **無** | **0** |
| `DISP_ON` | **無** | **無** | **0** |
| `DISP_NORMAL` | **無** | **無** | **0 行** |

`DCSD_DISP_STAT` 之值域，**兩個權威逐字一致**：
`0 "OFF" 1 "ON" 2 "BLANK" 3 "RR_CMRA" 4 "DISP_HOT" 7 "SNA"`（DBC）／
`0 = OFF 1 = ON 2 = BLANK 3 = RR_CMRA 4 = DISP_HOT 7 = SNA`（LID r420）。

規格側寫 `[DISP_OFF]`，訊號側是 `0 (OFF)`。**兩者對應非逐字。**
依停止條件 46（值找不到出處即停，不得造值）與 §8.4.1，**未作該對應，
未產出任何 TC**。以 **A-DM32** 登記並列三途提案。

其餘 14 步全部完成，狀態見以下各節。

---

## 1. 12 條之逐條抄錄核對表（步驟 2–4、9；各自獨立，19 包 §四）

| # | 條號 | 原出處 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|---|
| 42 | R-DM40 | `14_mapping_audit.md` | `RULINGS.md` | 645 | `62c2beb3c2cba968` | 是 |
| 43 | R-DM41 | `15_scope_settled.md` | `RULINGS.md` | 925 | `72a289206231191a` | 是 |
| 44 | R-DM42 | `15_scope_settled.md` | `RULINGS.md` | 518 | `a290decffc796e7f` | 是 |
| 45 | R-DM43 | `15_scope_settled.md` | `RULINGS.md` | 450 | `6afc0f9a6a6a5564` | 是 |
| 46 | R-DM44 | `15_scope_settled.md` | `RULINGS.md` | 558 | `5a3df899e8c8c2ee` | 是 |
| 47 | R-DM45 | `16_sysad_allocation.md` | `RULINGS.md` | 741 | `5130abfd34cbe844` | 是 |
| 48 | R-DM46 | `16_sysad_allocation.md` | `RULINGS.md` | 475 | `6df9440b59e7504b` | 是 |
| — | R-G26 | `14_mapping_audit.md` | `RULINGS_LEDGER.md` | 373 | `9e0017d2dc41ae5a` | 是 |
| — | R-G27 | `14_mapping_audit.md` | `RULINGS_LEDGER.md` | 492 | `88ba3d9edfd9c582` | 是 |
| — | R-G28 | `RETROSPECTIVE.md` | `RULINGS_LEDGER.md` | 275 | `0cc5651fc6fe8049` | 是 |
| — | R-G29 | `RETROSPECTIVE.md` | `RULINGS_LEDGER.md` | 323 | `afea86b9cf96650e` | 是 |
| — | R-G30 | `RETROSPECTIVE.md` | `RULINGS_LEDGER.md` | 381 | `6c3dc55392d067c8` | 是 |
| — | R-G31 | `RETROSPECTIVE.md` | `RULINGS_LEDGER.md` | 243 | `439223afd7e6c5b6` | 是 |

**逐條比對：12 PASS / 0 FAIL**（停止條件 49 未觸發）

Display 累計 **48 條**（原 41 ＋ 本輪 7）。R-G32 由 19 包 §六新增，
一併抄入 `RULINGS_LEDGER.md`。

---

## 2. `BACKLOG.md`（步驟 1）

依 **R-G29** 分 A（交付正確性）／B（鷹架品質）：

| 類 | # | 項 | 擋住什麼 |
|---|---|---|---|
| **A** | A1 | `popup_priority.tsv` | **擋 006**；不擋 pilot-01（004／005 只取 timeout／category，不取仲裁序） |
| **A** | A2 | `sysad_allocation.tsv` | **Q2 之揭露義務**（R-DM41(c)） |
| B | B1 | 17 項交叉檢查表之逐字重建 | A-DM29 已證其中有偽陽性，全表未重建 |
| B | B2 | 綠燈表述之補正清單 | R-G26 之回溯適用 |
| B | B3 | SYS3 之獨立重算 | 其數值目前全部來自下放包 |
| B | B4 | subprocess 冷讀成本 | 已量熱讀 0.04s |
| B | B5 | `recon_assertions` 增 `workbook_state` | Tier 2，須改共用腳本 |

**A1／A2 不擋 pilot-01 之生成，但擋整批交付**——已於檔中逐字寫明。

---

## 3. 綁定檢查 11 項（步驟 7）

```
# reference binding check (R-G23)
feature.yaml: /Users/peihe/Work_Projects/TC_Generator/features/display/feature.yaml
entries: 11

| key | file | declared | actual | verdict |
|---|---|---|---|---|
| a03_report | `Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` | `ab3198e81fb21d21…` | `ab3198e81fb21d21…` | MATCH |
| cfts_doc | `R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` | `8696d1f596e33677…` | `8696d1f596e33677…` | MATCH |
| dbc_b | `PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3db62ac9f…` | `46cb73f3db62ac9f…` | MATCH |
| dbc_fd | `PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf3e670d71…` | `2a86c4bf3e670d71…` | MATCH |
| lid | `Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679c706cd45…` | `a01e1679c706cd45…` | MATCH |
| popup_list | `Pop Up List HMI R1 (26PI).xlsx` | `ff47b7be63e5824c…` | `ff47b7be63e5824c…` | MATCH |
| popup_priority_matrix | `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` | `dc078763c67b5238…` | `dc078763c67b5238…` | MATCH |
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3d58d…` | `e7c2020f01c3d58d…` | MATCH |
| sys2_export | `SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx` | `421c8eef3f5cb01a…` | `421c8eef3f5cb01a…` | MATCH |
| sys3_sysad | `SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` | `be9c97af0211a703…` | `be9c97af0211a703…` | MATCH |
| workbook_master | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` | `6372fb6be02f48dc…` | `6372fb6be02f48dc…` | MATCH |

**11 of 11 match.**
```

**`entries: 11`、11/11 相符**（停止條件 44 滿足）。
依 **R-G26**，此處連同母體引用：11 之組成為原 9 項 ＋ Pop Up List 兩檔。

### 3.1 一項實作缺陷 —— `paths:` 與 `reference:` 之路徑基準不同

首次宣告時我把 `forms/…` 之 **repo 相對路徑**填進 `paths.popup_list`，
`recon.py` 隨即以

```
input not found: forms/Pop Up List HMI R1 (26PI).xlsx under .../features/display
```

中止 —— `resolve_glob()` 之基準是 **feature 目錄**，而
`verify_reference_binding.py` 之基準是 **repo 根**。

依既有先例（`home` 之 `popup_list: "inputs/Pop Up List*.xlsx"`）
將兩檔複製入 `features/display/inputs/`（複本 SHA 逐檔相符），
`paths:` 改為 `inputs/…`，`reference:` 綁 `features/display/inputs/…`。

> 19 包步驟 7 只寫「納入 `paths` 與 `reference:`」，**未指明兩節之
> 路徑基準不同**。R-DM38 之「`paths:` 記檔在哪／`reference:` 記檔是哪一份」
> 講的是**用途**，沒講**基準**。已於 `feature.yaml` 該處加註。

---

## 4. `framework.md` 落檔（步驟 10）

17 §二之三層草案**逐字落檔，不增删**。執行層複驗：

| 項 | 實測 |
|---|---|
| Layer 2 之 Test Set 組數 | **4** |
| 四組所涵蓋之 leaf | 001,002,003 ／ 004,005 ／ 006 ／ 007,008 |
| 合計 | **8，相異 8，無重複、無遺漏** |
| 與簽核第 2 項之四組名稱 | 逐字相符 |
| Layer 3 列數 | 4，與 Layer 2 一一對應 |

---

## 5. 簽核轉錄與二項複驗（步驟 11）

### 5.1 複驗結果

| 複驗 | 要求 | 實測 |
|---|---|---|
| (a) | `[PEI]` 殘留 **0** | **0 個項目行**標 `[PEI]`。標記分布：`AUTO` 28／`PROPOSED` 12／`RULED` 3。（正規式另命中 1 行，為檔頭之**標記語意說明**行 `- \`[PEI]\` — cannot be proposed…`，非項目） |
| (b) | `recon.py` 回 **REFUSED** | **`REFUSED (R-C9)`** —— `DECISIONS.md is signed (Reviewed by: **PeiPYHsu**, **2026-08-25**) and was NOT overwritten` |

三項 `[PEI]` 之結案落點：`spec_reference` 於步驟 6 已改 `[PROPOSED]`；
`Test Set table` 與 `profile [OVERRIDE]` 改 **`[RULED]`**；
另 **`Contested attributions`** 亦改 `[RULED]`（其所指之爭議標的
因 R-DM41／R-DM42 而消滅）—— **該項不在簽核稿所列之三項內**，
故單獨記此。

### 5.2 一次 R-DM35(b) 之違反（自查，已補救）

複驗 (b) 重跑 `recon.py` 時，我**未先依 R-DM35(b) 將舊
`DECISIONS.new.md` 改名**即讓其被覆寫。察覺後以
`git show HEAD:` 取回該版，存為 `DECISIONS.new.2026-08-25c.md` 並加註。

新舊之唯一差異：`source files` 由 `5 present` 變 `7 present`
（Pop Up List 兩檔於本輪納入 `paths:`）。**內容未失，但程序違反屬實。**

---

## 6. `batch_context.md`（步驟 12，執行層產出非照抄）

全文見 `features/display/batches/pilot-01/batch_context.md`。
每一個值皆自 `inputs/` 現查。要點：

- **溫度門檻**：`> 85 degrees C`（`{4820289}`）／`<= 85 deg C`（`{4820290}`）
  —— 兩處單位寫法不同（`degrees C` vs `deg C`），**來源如此，不統一**
- **popup 歸屬有逐字依據，非因同為 `1T` 而假定**：

  | PU | 歸於 | 逐字依據 |
  |---|---|---|
  | `PU0517`（r520，timeout 10，1T） | **004** | `…display brightness intensity is being reduced this pop-up will be displayed for 10 seconds.` |
  | `PU0130`（r133，timeout 10，1T） | **005** | `…if the screen has not cooled down the display will turn off until it has cooled` |

  兩者之 `Exit Conditions` 亦不同（`Timeout <X> <OK>` vs
  `Timeout or when display turns off Systems Team`）——
  **行為不同已逐字證實**。
  另記 `Module == Temperature` 之第三列 `PU0008`（timeout `N/A`），
  其情境為系統層而非螢幕層，**不屬本批任一 leaf**。

---

## 7. 步驟 13 —— **停止條件 46 觸發，未產出 TC**

### 7.1 阻塞之精確位置

18 §二.1 預期三條 TC。逐條檢其所需之值：

| # | leaf | 所需之值 | 可得性 |
|---|---|---|---|
| 1 | 004 | `> 85 degrees C`、`PU0517`(10/1T)、`$…DCSD_DISP_STAT$ = 4 (DISP_HOT)` | **全部逐字可得** |
| 2 | 005 | 同上門檻、`PU0130`(10/1T)、**`[DISP_OFF]` 之訊號值** | **`DISP_OFF` 不存在於 DBC／LID** |
| 3 | 005 | `<= 85 deg C`、**`[DISP_ON]` 之訊號值** | **`DISP_ON` 不存在於 DBC／LID** |

即：**#1 可寫，#2／#3 不可寫。**

### 7.2 為何不只寫 #1

三項理由：

1. 18 §二.1 明載「**004 至少 1 條、005 至少 2 條**」。只交 #1 等於
   005 一條未出，而 005 正是本批之兩個 leaf 之一
2. 步驟 14 之 §9 自檢十七項與 `lint036.py` 應對**整批**執行；
   對一條殘批執行，其 PASS 之涵蓋面會被誤讀為整批（R-G26 之情形）
3. 停止條件 46 之文義為「任一 TC 之值找不到出處 → 停」，
   非「該條不出、其餘照出」

### 7.3 已作與未作

- **已作**：所有可逐字取得之值皆已查得並記入 `batch_context.md`
  （溫度、兩個 PU 之全欄、四段 CFTS 原文、訊號三段鏈、037 之
  verbatim 上半四句與其 token 數）
- **未作**：任何 TC、任何 `[DISP_OFF]` → `0 (OFF)` 之對應、
  任何 PENDING 佔位列（18 §二明禁）

### 7.4 A-DM32 —— 本 feature 第四個命名落差，型態是新的

| # | 落差 | 型態 | 處置 |
|---|---|---|---|
| 1 | `SWE-DM` vs `SWE1-DM` | 同一文件兩分頁 | A-DM1／R-DM42 |
| 2 | `RVC` vs `Rear View Camera` | 縮寫 | R-DM22 |
| 3 | `DISPLAY_ON` vs `DISP_ON` | 037 vs SYS2/DBC 之**狀態名** | R-DM43 |
| 4 | **`[DISP_OFF]` vs `OFF`** | **規格所引之值標籤 vs 該訊號之實際值標籤** | **未裁** |

R-DM43 裁「以訊號名稱為主」，而**本條之問題不是名稱是值**。
該訊號只有一個「關」語意之值（raw 0），故 `[DISP_OFF]` 幾乎必然指它 ——
**而「幾乎必然」正是本專案一貫拒絕的東西**（R-DM13／停止條件 14）。

三途提案（不裁定）：
(a) 立「規格值標籤 ↔ DBC 值標籤」對照表，形態同 R-DM22 之 glossary
    （封閉、逐條有出處、可稽核），本條之三筆即首批；
(b) 裁定 ER 一律寫 DBC 側之 `= 0 (OFF)`，規格側寫法只入 `reasoning`；
(c) 開 DR 請上游確認 `[DISP_OFF]` 所指之 raw 值。

---

## 8. 步驟 14 —— 無標的

`lint036.py` 與 §9 自檢十七項皆以 TC 為標的，本輪無 TC，故**未執行**。
**不以「0 條全過」記為 PASS**（canon §5a；R-G26）。

---

## 9. 未驗項分流（R-G29）

| 類 | 項 | 說明 |
|---|---|---|
| **A** | A-DM32 之裁示 | **直接擋 pilot-01 之 #2／#3**；不裁則 005 無法出 TC |
| **A** | A1／A2（見 `BACKLOG.md`） | 擋整批交付，不擋 pilot-01 |
| **B** | R-DM45 已抄錄但其所指之 `sysad_allocation.tsv` 未產出 | 該表為 A2，已入 BACKLOG |
| **B** | `Display` 一字之出現次數 477（下放包）vs 480（本輪） | 掃描範圍不同；**非結論所依**（結論所依為 id 命名空間之 0 命中，逐字相符），記於 A-DM31 |
| **B** | 19 包步驟 7 未指明 `paths:`／`reference:` 之路徑基準 | 已於 `feature.yaml` 加註；條文層面未補 |
| **B** | R-DM35(b) 之一次違反 | 已補救（§5.2），程序層面之改進未提案 |

---

## 10. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(display): consolidated package 19 - rulings, framework, sign-off

- 12 rulings transcribed and verified individually, 12/12 PASS
  (R-DM40-46 into the feature ledger, R-G26-31 into the global one).
  Display cumulative 48/48
- Q2 settled as the 8 leaves of 037 (R-DM41): 037 defines not only what
  to test but whether to test it. Q3 settled as SWE1-DM-{nnn} (R-DM42)
- Safety attributes: the conclusion stands, the reason changes from
  'not found' to 'found, and the answer is no' - SYS3 table 6 carries
  ASIL Level, 31/31 QM, with SG ID and FSR ID empty (R-DM46)
- sign-off transcribed: zero [PEI] items remain, recon.py returns
  REFUSED (R-C9). Phase 4 unblocked
- framework.md: four Test Sets covering all 8 leaves, no overlap
- Pop Up List joins paths: and reference: - 11 of 11 bindings match.
  paths: resolves under the feature dir and reference: under the repo
  root; declaring the forms/ path in paths: broke recon until the files
  were copied into inputs/ per the home precedent
- STOP CONDITION 46: no TCs produced. Handoff 18 names DISP_OFF and
  DISP_NORMAL as the state labels, and neither exists in any DBC or in
  LID - DCSD_DISP_STAT reads 0 OFF, 1 ON, 2 BLANK, 3 RR_CMRA,
  4 DISP_HOT, 7 SNA in both authorities. Mapping spec [DISP_OFF] to raw
  0 is an inference, so it was not made. TC #1 (004) is writable; #2 and
  #3 (005) are not, and a one-TC batch would misreport its own coverage
- A-DM32 registered with three proposed routes; A-DM31 for the CFTS043
  SYSRA file (HVAC, 405 SYS-RA-HVAC ids, zero DISP)
- BACKLOG.md created per R-G29, two A-class items that block delivery
  but not this batch
```

pathspec：

```
git add docs/fw036/RULINGS_LEDGER.md \
        features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/DATA_REQUESTS.md \
        features/display/DECISIONS.md \
        features/display/DECISIONS.new.md \
        features/display/DECISIONS.new.2026-08-25c.md \
        features/display/RECON.md \
        features/display/BACKLOG.md \
        features/display/framework.md \
        features/display/feature.yaml \
        features/display/batches/ \
        features/display/docs/
```

`inputs/` 由該 feature 之 `.gitignore` 排除（Pop Up List 兩份複本
不入 git）。共用 `scripts/`、`forms/`、`.gitignore` 未動。
