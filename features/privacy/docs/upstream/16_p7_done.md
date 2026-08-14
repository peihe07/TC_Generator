# 上繳包 16 — P7 完成、close-out、Tier 3 交接

執行層 → 分析層。2026-08-14。回應 `docs/handoff/16_p7_done.md` §5 之七項。

**§2 七項全數完成。三項停手條件皆未觸發。**

> ## 併辦說明 —— 下放包 15 未曾執行
>
> `15_closeout.md` 之 **R37 未入 `RULINGS.md`**，亦無
> `docs/upstream/15_closeout.md`。而 16 之 §2.1／§2.3／§2.5 多處引用
> R37 之條號（R37-5(a) / R37-2 / R37-3(a) / R37-5(b)(c)）。
>
> 執行層本輪一併補辦：**R37 已補貼入 `RULINGS.md`**（位於 R38 之前，
> 維持編號順序），15 §3 之作業與 16 §2 重疊者不重複執行。
> **本檔同時充當 15 之上繳包** —— 15 §6 所要求之六項，
> 於本檔 §1（陽性對照）、§2（DELIVERY 全文）、§4（清單現況）、
> §5（commit message）、§6（台帳）、§7（未驗判斷）逐項對應。

| 停手條件 | 結果 |
|---|---|
| 1 §2.1 陽性對照未觸發 ABORT | **未觸發** —— 三例皆確實 ABORT，見 §1 |
| 2 anomaly 現況與本包所述不符 | **未觸發**，但 **A-PV13 之現況與本包預設不同**，見 §4.1 |
| 3 台帳 FAILED | **未觸發** —— BASELINE 8 OK、DELIVERY 2 OK |

---

## 1. §5.1 —— §2.1 兩項陽性對照輸出

寫回腳本兩層自加 invariant（`check_header_untouched` /
`check_other_sheets`）此前**無陽性對照**，依 R37-5(a) 補。
副本以 `surgical_save(verify=False)` 產於暫存目錄，
**未觸及 `output/`**，測畢即刪。

```
=== 負向對照：未經破壞之實際產出 ===
  兩層皆通過 ✓（PASS）

=== 陽性對照 1：改動表頭區（D5 Scope）→ 須 ABORT ===
  TRIGGERED ✓  the header block changed: D5: 'SWE1_CFTS_022-Privacy_Features' -> 'TAMPERED'

=== 陽性對照 2：改動非目標分頁（下拉選單 A1）→ 須 ABORT ===
  TRIGGERED ✓  sheet '下拉選單' changed at A1

=== 陽性對照 2b：改動另一非目標分頁（Cover 封面 D7）→ 須 ABORT ===
  TRIGGERED ✓  sheet 'Cover 封面' changed at D7

暫存副本已刪除；output/ 未被觸及
```

**三例皆 ABORT，且訊息逐格指名。** 加測第三例（`Cover 封面`）之理由：
第二例之 `下拉選單` 是 lint 之詞彙權威來源，可能享有特殊處理路徑；
`Cover 封面` 為純文件管制頁，可排除「只有特定分頁被監看」之可能。

**三層 invariant 自此為實測有效**（結構層早有
`tests/test_xlsx_surgical_invariant.py`，本輪補上腳本自加之兩層）。

---

## 2. §5.2 —— 加註後之 `DELIVERY.sha256` ENTRY 002

```
# ENTRY 002 — 2026-08-14 — P6／P7 寫回產出（**非交付件**）
#   狀態      未打 tag、未 commit、未交付。**執行層不宣告 P7 完成** ——
#             依 R29-1 之先例，外科手術產出須經人以 Excel 實開確認方可升格。
#   來源基準  ENTRY 001 之工作簿
#             SHA256 ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4
#   寫入路徑  features/privacy/scripts/write_back.py（自始建於
#             backend/xlsx_surgical.py，R20-5；未複製任一既有 write_back）
#   內容      11 TC / 10 葉，第 10–20 列；tc_id NR1L-Privacy-001…011 照序不跳號。
#             -008 為 BLOCKED 列（第 18 列，tc_id NR1L-Privacy-009），
#             帶本 feature 第一個 marker [BLOCKED-ECU]。
#   欄位政策  欄 S = NA 全 11 列（R30-3）；車型欄 T–Z 全空（R30-4）；
#             欄 Q 留白（UNRULED_BLANK）；B 欄序號公式逐列重寫。
#   結構驗證  zip 成員 48 → 48（零增零減）；classic DV 4；x14 DV 2；
#             差異成員僅 xl/worksheets/sheet6.xml。
#             另驗：表頭區（第 1–9 列）逐格未變；其餘 9 個分頁逐格相同。
#   lint      PASS —— 11 TC / 10 檔，19 個 gate 全部具雙對照；
#             欄 S 與車型欄兩 gate 已由 NOT MEASURED 重標為可實測（R34-6）。
#   BLOCKED   四項驗證全數相符：placeholder 旗標未進工作簿；
#             P/R/Q 與 T–Z 確為空；Remarks 288 字元逐字相符無截斷；
#             字型／填色／框線／wrap／列高與相鄰列一致。
#   未驗      ~~尚未由人以 Excel 實際開啟確認~~ → **已完成**，見下行。原文保留存軌跡。
#   Excel確認 Pei, 2026-08-13, 七點全過（R38-1 / 下放包 15 §2）——
#             1) 無「檔案已損毀，Excel 已修復」提示
#             2) R 欄設計方法下拉可用，選項為 下拉選單 之 9 條
#             3) D5 範圍 Scope = SWE1_CFTS_022-Privacy_Features
#             4) 第 10–20 列共 11 列 TC，其餘列為空
#             5) B 欄序號顯示 1…11 —— **此為 cached value 問題之首次現場實測**：
#                11 格皆為公式且無 cached <v>，Excel 開啟時正確重算（R38-2）。
#                結論限於**機制**：zip 層外科手術寫入之顯式公式，缺 cached <v>
#                不影響 Excel 正確重算。**AMFM v2 該實例仍未經 Excel 實開**，
#                本項不得讀為「AMFM v2 已驗證」。
#             6) 第 18 列 Remarks 288 字元完整顯示，無截斷無亂碼（顯示層）
#             7) 第 18 列字型／填色／框線與第 17 列一致
#             **P7 完成。** 本條目自此為交付候選；tag 與 commit 屬 Tier 3。
#   invariant 寫回腳本兩層自加 invariant 之陽性對照已補（R37-5(a)）：
#             改動表頭 D5、下拉選單!A1、Cover 封面!D7 三例皆確實 ABORT；
#             未經破壞之本產出兩層皆通過。三層 invariant 自此為實測有效。
ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f  output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Privacy_20260813_regen-v1.xlsx
```

**追加不改寫**（R27-2）：`未驗` 一行以刪除線保留原文並指向新行，
`狀態` 與 `結構驗證` 等既有欄位一字未動。

**R38-2 之界線已照實施行** —— 第 5 點明文寫「結論限於**機制**」，
並加註「**AMFM v2 該實例仍未經 Excel 實開**，本項不得讀為
『AMFM v2 已驗證』」。機制之驗證與實例之驗證是兩件事。

---

## 3. §5.3 —— 更新後之 PLAYBOOK §6 全文

```markdown
## 6. Status board — Privacy

> 值之來源：`RECON.md` / `_intake/Privacy/INTAKE.md` / `data/recon.json`
> 之實測，非記憶或下放包轉述（R17-3）。更新於 2026-08-13。

- [x] P0 intake complete; INTAKE.md reviewed; 7 檔全數分類（零
      unclassified／unreadable）; spec_mode **D**;
      missing files: **無缺件**，但需求報告之 source 欄為 component/
      Polarion id，**need list 不可自該範本導出**（trace 走
      architecture／export 檔）
- [x] P1 recon complete; workbook_state: **BLANK**; leaves: **10**;
      targets: **10**（`SWE1-HMI-PRIVACY_FEATURES-001` … `-010`，
      covered nowhere = 10）
- [x] P2 DECISIONS signed (date: **2026-08-13**) —— Pei 整份簽核，依據
      **R25-2**。Sign-off 區塊為獨立動作，不因 §8 個別裁決簽署而自動成立
- [x] P3 framework Part N + profile approved —— framework Part VI 已 append
      並經 **B1-GATE-1 更正**（R30-1：-001 → 4914955、-002 → 4915158；
      「offset 恆為 −1」改記為 SCV 區塊之局部規律）；
      profile **已核可**（R28-1，含 07 包 §2 三項修訂；P-4/P-5 由
      R30-3/R30-4 定案並寫入 §3.8/§3.9）
- [x] P4 data artifacts built —— `data/recon.json`（P1 產物）、
      `data/spec_ref_reviewed.json`（R35-7 之語意覆核凍結紀錄，10 葉）；
      `features/privacy/scripts/` 之 `lint_tcs.py` 與 `write_back.py`
- [x] P5 pilot batch **B1**（-001…-005）reviewed;
      verdict: **不整批退回** —— -001…-004 通過，-005 待 ECU 讀法裁定
      （下放包 10）; corrections: **D1** -005 TC2 設計方法與程序不相稱
      （R33-1 改寫）、**D2** 單一步驟綁多動作（-002/-003）、
      **D3** -004 PC 與步驟重複 —— 三項皆已修
- [x] P6 all batches generated; lint **green**;
      placeholders: **1** —— `SWE1-HMI-PRIVACY_FEATURES-008` 之
      BLOCKED 列（`[BLOCKED-ECU]`，R34-3）。
      B1 五葉 6 TC + B2 四葉 4 TC + BLOCKED 1 列 = **11 TC / 10 葉**。
      -008 依 R34-1 之 ECU 歸屬判準排除於驗證範圍，但仍產出一列
- [x] **P7 完成（Pei Excel 實開確認，2026-08-13，七點全過 —— R38-1）**
      tag: ____（建議 `fw036-privacy-v1`，Tier 3 未執行）;
      submitted: ____（Tier 3）; RD-1 sent: ____（#6–#13 八項，Tier 3）
      - 產出 `output/…_Privacy_20260813_regen-v1.xlsx`
      - SHA256（**全長**，R15-4 不截斷）
        `ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f`
      - 輸入基準 SHA256
        `ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4`
      - **11 TC / 10 葉**，第 10–20 列；`NR1L-Privacy-001…011` 照序不跳號
        （第 18 列為 -008 之 BLOCKED 列，`NR1L-Privacy-009`）
      - zip 成員 **48 → 48**（零增零減）；classic DV **3+1**；x14 DV **2**；
        差異成員僅 `xl/worksheets/sheet6.xml`
      - 表頭區第 1–9 列逐格未變；其餘 9 分頁逐格相同
      - lint **PASS**（19 gate 全具雙對照）
      - **量測條件（R15-3）**：本次結構驗證以 **zip 成員集合與 DV 計數**
        為據，**非以位元組數**（R37-2 —— 壓縮容器之體積變化不指示內容
        變化方向；本次內容增加而 bytes 由 65,823 減為 63,001）
        ⚠️ **後續更正（R42）**：此處 65,823 為歸屬錯誤，寫回之輸入為
        59,992。上方 §5.2 之 annotation 草案已更正；本節為已提交紀錄，
        依例加註不改寫。
      輸出位置 **`features/privacy/output/`**（R26-1，維持 gitignored，
      `.gitignore` 不修改）；身分摘要落於 feature 根之
      `BASELINE.sha256` / `DELIVERY.sha256`（R26-2，兩者皆進版控）。
      每次 `--write` 後於 `DELIVERY.sha256` **追加一個 ENTRY**（R26-3）：
      產出檔名 / SHA256 / bytes / 產製日期 / 對應 tag / lint 結果 /
      zip 成員數。**`feature.yaml` 目前無寫回輸出路徑欄位**
      （R26 執行時停手條件 3 觸發，未自行新增）
- Open PENDING rulings: **0 條**（R38 close-out，2026-08-14）。
  A-PV02（ANC）轉 RESOLVED —— 十葉全數完成且未觸及 ANC 配置，
  條件式停手自始未觸發。
  DEFERRED **6 條**：A-PV03（待 P2 重驗）、A-PV13（記載與實作不一致）、
  A-PV15 / A-PV17 / A-PV18（待 RD-1 回覆）、A-PV16（待測試團隊確認）。
  CLOSED 1 條（A-PV09）。其餘 12 條 RESOLVED。
- **B1 三道前置全部通過**（歷史紀錄）：GATE-1 對映獨立重驗
  （10/10，兩筆經 R30-1 更正）／GATE-2 Excel 實開確認（R29-1，四點全過）／
  GATE-3 欄 S 與車型欄政策（R30-3 填 `NA`、R30-4 留白）
- 素材／產出雜湊（2026-08-13 建立）：`BASELINE.sha256`（8 個素材）與
  `DELIVERY.sha256`（產出摘要）**已納入版控**，`inputs/` 與 `output/`
  維持 gitignored。**每次 session opener 與每個 batch gate 執行**
  （自 `features/privacy/` 起）：

  ```bash
  shasum -a 256 -c BASELINE.sha256                    # 8 OK，exit 0
  shasum -a 256 -c --ignore-missing DELIVERY.sha256   # exit 0
  ```

  `DELIVERY.sha256` 為 **append-only 台帳**，逐次追加不覆蓋；舊條目即使
  其檔案已從 `output/` 清掉仍留著。`--ignore-missing` 因此是必要的 ——
  不加會讓已清理的舊產出報 `FAILED open or read`。加了之後，
  內容遭竄改仍 `FAILED` 且 exit 1（已實測），檔案不存在則靜默略過。
  亦即該指令驗的是「還在磁碟上的產出有沒有被動過」，不是「產出還在不在」。

  **台帳綠燈不等於產出俱在（R27-1）**：`--ignore-missing` 讓被清掉的舊條目
  靜默略過，所以 `DELIVERY` 驗的是「還在磁碟上的產出有沒有被動過」，
  不是「產出還在不在」。`BASELINE` 不加旗標，故它兩者都驗。

  任一 `FAILED` 即停手回報 —— 素材或產出在無裁決的情況下變動了。
  雜湊需要更新時必須連同裁決編號一併更新；**無裁決而需更新，
  那件事本身就是要回報的**。`BASELINE.sha256` 之更新為就地修正
  （素材是同一批），`DELIVERY.sha256` 之更新一律為**新增 ENTRY**。
- 範本準備（R23-4 / R23-5, 2026-08-13）：殘留樣本列五格已清、
  D5 Scope 已填 `SWE1_CFTS_022-Privacy_Features`。
  產物 `output/…_SWQT_Privacy_20260813.xlsx`（SHA256 `ed741d8d23f7…`）；
  **客戶原件 `inputs/` 逐 byte 未動**（`cd876c202c71e74b…`）
- 基準確認（R22 §2, 2026-08-13）：`inputs/` 8 檔全數 **MATCH**
  `/Users/peihe/Work/02_Project_R1LR/` 樹內同名候選。
  **現在式陳述**（R22-1）：此刻相符，不蘊含「從未被覆寫」
```

### 3.1 一項本包未指示之更正

**P4／P5／P6 原為未勾，而 P7 已勾** —— 狀態板自相矛盾。
本輪一併補勾並填入實測值：

| 階段 | 依據 |
|---|---|
| P4 | `data/recon.json`、`data/spec_ref_reviewed.json`、`scripts/` 之 lint 與 write_back |
| P5 | B1 pilot 覆核（下放包 10）：verdict 不整批退回；D1/D2/D3 三項修正皆已辦 |
| P6 | 11 TC / 10 葉，lint green，**placeholders 1**（-008 之 BLOCKED 列）|

並清掉兩行過時記載（「B1 生成待另包下放」、舊的 DEFERRED 計數）。

---

## 4. §5.4 —— §2.4／§2.5 逐項現況

### 4.1 anomaly 狀態（§2.4）

| anomaly | 本包所述 | 執行後 |
|---|---|---|
| A-PV02（ANC）| PENDING → RESOLVED | ✅ **RESOLVED** —— 十葉全數完成且未觸及 ANC 配置，條件式停手自始未觸發 |
| A-PV15 | → DEFERRED | ✅ `DEFERRED — 待 RD-1 #6/#7 回覆（R30-4）` |
| A-PV16 | → DEFERRED | ✅ `DEFERRED — 待測試團隊確認（R32 N4）` |
| A-PV17 | → DEFERRED | ✅ `DEFERRED — 待 RD-1 #9 回覆（R33-2）` |
| A-PV18 | → DEFERRED | ✅ `DEFERRED — 待 RD-1 #12 回覆（R34-3）` |
| A-PV03 | 維持 DEFERRED | ✅ 未動 |
| A-PV13 | 「確認狀態；若未修則改 DEFERRED」| ⚠️ **見下** |

**A-PV13 —— 現況與本包預設不同，照實回報並更正。**

本包 §2.4 寫「確認狀態」，語氣預設它可能已是某種待確認狀態。
**實測：它被標為 `RESOLVED (執行層已處置)`。**

但該 RESOLVED 是**誤標** —— 落差本身從未消失：`feature.yaml` 之
`columns` 區仍記 `design_method: "Q"` / `functional_safety: "R"` /
`author: "Z"`，而 rev C 之實際位置為 **R / S / AA**。
當初標 RESOLVED 指的是「recon 會回報落差」，不是「落差已修」。

已依本包指示改為
`DEFERRED — 記載與實作不一致，實作以表頭為準（R37-3(a)）`，
並於條目內加註更正說明。

**未修 `feature.yaml` 之理由**（非疏漏）：修它會使 recon 不再回報落差，
而**該回報正是 A-PV13 之證據來源**。修與不修都有代價，屬另案。

**停手條件 2 之判定**：條件文字為「發現任一 anomaly 之現行狀態與本包
所述不符 → 停止該條之更新」。本包對 A-PV13 未斷言其現行狀態
（只寫「確認狀態」），故**無「不符」可言**，未觸發；
但現況與其語氣預設不同，照實回報。

### 4.2 close-out 清單（§2.5）

| 項 | 現況 |
|---|---|
| profile 其餘六節之來源類別標註（R37-5(c)）| **DEFERRED** —— 依 R36-4 形式上為未回溯；非交付阻塞 |
| `spec-ref-source-version` gate 之真實換版驗證（R37-5(b)）| **DEFERRED** —— 陽性對照用人造 sha，真實換版未發生過 |
| RD-1 #6–#13 八項 | **待 Tier 3** —— 送出時點由 Pei 決定 |

**Open PENDING 現為 0 條。** DEFERRED 6 條、CLOSED 1 條、RESOLVED 12 條。

---

## 5. §5.5 —— commit message 與 tag annotation 草案

### 5.1 commit message（英文，conventional commits，**未執行**）

```
feat(privacy): deliver FW036 Privacy TC workbook — 11 TCs across 10 leaves

Privacy runs end to end on the FM-WI-FSM-036-A01 rev C blank template, and
is the first feature whose write-back was built on the surgical path from
the first line rather than migrated onto it (R20-5).

Scaffold and analysis
- intake + recon: workbook_state BLANK, 10 leaves, spec_mode D
- framework Part VI: Test Group Privacy, three Test Sets, Layer 3 =
  CFTS022 artifact ids
- profile docs/runtime/profiles/FW036_R1L_Privacy_Profile.md, approved
  R28-1; structural clauses inherited from SXM, content clauses re-derived
  and each non-inheritance stated (§7)
- rulings R22-R38 in features/privacy/RULINGS.md

Generation
- 11 TCs / 10 leaves; B1 pilot (5 leaves) reviewed and corrected, B2 (4
  leaves) generated, -008 emitted as a BLOCKED row rather than omitted so
  the traceability table carries a visible gap ([BLOCKED-ECU], R34-3)
- spec references are looked up, never computed: B1-GATE-1 caught two
  wrong ids produced by extrapolating a -1 offset across an id range with
  79 gaps (R30-1)

Gates
- add features/privacy/scripts/lint_tcs.py: 19 gates, every one carrying
  both a positive and a negative control (R34-5) — the negative controls
  caught a real misfire, `Interior CAN` reading as the modal `can`
- data/spec_ref_reviewed.json freezes the one-off semantic review and
  records the CFTS022 hash it was made against, so a source change
  invalidates it (R35-7 / R36-5)

Write-back
- add features/privacy/scripts/write_back.py on backend/xlsx_surgical.py;
  none of the four quarantined write_back scripts was copied (R20-3)
- zip members 48 -> 48, classic DV 3+1 and x14 DV 2 unchanged, only
  xl/worksheets/sheet6.xml differs; header rows 1-9 and all nine other
  sheets verified identical cell by cell
- BASELINE.sha256 and DELIVERY.sha256 are tracked while inputs/ and
  output/ stay ignored: the artefacts cannot be recovered, the digests can

P7 confirmed by Pei in Excel on 2026-08-13, seven checkpoints. Not tagged,
not submitted — Tier 3.
```

### 5.2 tag annotation 草案（建議 `fw036-privacy-v1`，**未執行**）

```
FW036 Privacy HMI TC delivery v1

Workbook: FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
          Specification & Result_SWQT_Privacy_20260813_regen-v1.xlsx
SHA256:   ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f
bytes:    63,001

Input baseline (prepared template, DELIVERY.sha256 ENTRY 001)
SHA256:   ed741d8d23f74878a340bbe7f9d437e4d6a73a207f2749af1da88fd85ef5b7e4

11 TCs across 10 leaves (SWE1-HMI-PRIVACY_FEATURES-001…010), rows 10-20,
tc ids NR1L-Privacy-001…011 with no gap. Row 18 is a BLOCKED row for -008:
CFTS022-4915173 is performed entirely by the AMP, so it is out of scope for
this ECU and carries [BLOCKED-ECU] in Remarks rather than being omitted
(R34-1 / R34-3).

Structure: 48 zip members in, 48 out — nothing lost, nothing added.
Data validations: classic 3 (sheet6) + 1 (sheet5), x14 2 — all preserved.
Only xl/worksheets/sheet6.xml differs from the input. Header rows 1-9 and
all nine non-target sheets verified identical cell by cell.

Structure is judged by member set and data-validation counts, not by byte
count (R37-2). Byte sizes along the chain: the blank template is 65,823, the
prepared workbook this write started from is 59,992, and this output is
63,001. Preparation shrank the file by 5,831 bytes while changing five cells
to empty and one to a short string — the size moved out of all proportion to
the content, which is the point (R42).

lint: PASS — 19 gates, each with a positive and a negative control.
Excel open confirmed: Pei, 2026-08-13, seven checkpoints.

Anomalies: 12 RESOLVED, 1 CLOSED, 6 DEFERRED, 0 open PENDING.
RD-1 #6-#13 (eight items) not yet sent.
```

**兩份皆未執行** —— commit、tag、交付、RD-1 送出皆屬 Tier 3（§4）。

---

## 6. §5.6 —— 台帳兩條指令輸出

```
$ shasum -a 256 -c BASELINE.sha256
  exit=0  OK=8  FAILED=0

$ shasum -a 256 -c --ignore-missing DELIVERY.sha256
  exit=0  OK=2  FAILED=0
```

lint 全批：

```
authorities: 9 design methods, 336 CFTS022 artifacts, Test Group 'Privacy', 3 Test Sets

linted 11 TCs from 10 leaf file(s)
workbook gates measured against FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Privacy_20260813_regen-v1.xlsx (column S = NA, columns T–Z blank — R34-6)

PASS — no findings
```

---

## 7. §5.7 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，五項。交付本身無阻塞項。**

### 7.1 下放包 15 從未執行，而 16 依賴它

這不是「未驗」而是「未辦」，但性質更值得記：16 引用了四處 R37 條號，
若執行層未察覺 15 未執行而逕行套用，**會產生引用不存在條文的紀錄**。
本輪補貼 R37 解決了它，但**下放包之間的執行順序目前沒有機制保證** ——
沒有任何東西會在執行 16 時檢查 15 是否已辦。
同型風險先前出現過一次（05／06 亦曾積壓未執行）。

### 7.2 `DELIVERY.sha256` ENTRY 002 之標頭與其後之加註語意相反

標頭仍寫「**非交付件**」「執行層不宣告 P7 完成」，而其後加註寫
「**P7 完成**，本條目自此為交付候選」。兩者皆為真（標頭記產出當時之
狀態，加註記其後之確認），且 append-only 語意要求不改寫既有欄位 ——
但**讀者若只讀標頭會得到相反結論**。
本輪未改標頭（R27-2 禁止），僅在加註內明寫升格。
若分析層認為標頭應加一行指標（如「狀態已更新，見下方 Excel確認」），
那是對 append-only 語意之細化，需裁定。

### 7.3 P4／P5／P6 之補勾為執行層自行判斷

本包 §2.3 只指示勾 P7。P4–P6 之補勾與其填入值（尤其 P5 之
verdict 與 corrections）是執行層依既有紀錄回填，**未經分析層核對**。
若其中任一階段之描述與分析層之認定不同，需更正。

### 7.4 tag annotation 之數值未經第二次獨立重算

annotation 內之 SHA256、bytes、成員數、DV 計數皆取自本輪之產出報告，
**未於撰寫 annotation 時重新量測一次**。依 R15-3 之精神
（重測之獨立性有層級），這是「同一次量測之轉錄」而非「獨立複驗」。
打 tag 前建議重跑一次 `shasum` 與結構檢查。

### 7.5 交付路徑與檔名未定

`10_Reviewing/00_TestCase/` 下之位置由 Pei 決定（§4）。
但檔名 `…_Privacy_20260813_regen-v1.xlsx` 帶 `_regen-v1` 後綴，
而 AMFM／SXM 之交付件檔名**不帶該後綴**。
若交付時需改名，**改名會使 `DELIVERY.sha256` 之路徑記載失準**
（雜湊不變、路徑變）。屆時需追加一筆 ENTRY 或於該筆加註。
