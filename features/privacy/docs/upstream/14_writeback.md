# 上繳包 14 — P6 前置收尾、P6／P7 寫回

執行層 → 分析層。2026-08-14。回應 `docs/handoff/14_writeback.md` §5 之八項。

**§2 四項與 §3 寫回全數完成。五項停手條件皆未觸發。**

**未打 tag、未 commit、未交付，且不宣告 P7 完成** —— 依 R29-1 之先例，
外科手術產出須經人以 Excel 實開確認方可升格。

---

## 0. 停手條件逐項

| # | 條件 | 結果 |
|---|---|---|
| 1 | §2.2 某節措辭多數無 CFTS022 對應且非 test-setup | **未觸發** —— §3.4 / §4 全數逐字命中；§6 兩項不命中但屬 VF651 檔名（見 §1.2）|
| 2 | 寫回路徑無法在不複製既有腳本下建立 | **未觸發** —— 見 §2 |
| 3 | ABORT invariant 觸發 | **未觸發** —— 48 → 48 成員、DV 3/2 不變 |
| 4 | BLOCKED 列驗證任一項不符 | **未觸發** —— 四項全符，見 §4 |
| 5 | 台帳 FAILED | **未觸發** —— BASELINE 8 OK、DELIVERY 2 OK |

---

## 1. §5.1 —— §2 四項完成狀態與 profile 回溯

| # | 作業 | 狀態 |
|---|---|---|
| 2.1 | `spec_ref_reviewed.json` 增 `source_sha256` + gate | ✅ |
| 2.2 | profile §3.4／§4／§6 回溯 + 四節標來源類別 | ✅ 見 §1.2 |
| 2.3 | 兩項 gate（排序、test-group 近似值）| ✅ |
| 2.4 | 全批回跑 | ✅ **PASS** |

### 1.1 §2.1 —— 兩份台帳已接起來

`spec_ref_reviewed.json` 各筆增記 `source_sha256`
（`5eb0dd739f002fe0…`，取自 `BASELINE.sha256` 之 CFTS022 行）。
新 gate **`spec-ref-source-version`** 比對現行值，不符即 FAIL，
訊息為「來源文件已換版，語意對應覆核須重做」。

這補上的正是「reference 字串沒變、但條文內容換了」那個洞 ——
素材完整性台帳與判斷有效性至此有了連結。

### 1.2 §2.2 —— 三節回溯結果（逐條，含來源類別）

**§3.4 訊號引用 —— 全數 `spec-verbatim`**

| 詞彙 | CFTS022 命中 |
|---|---|
| `$VolumeSCV$` | **8** |
| `<Tsend>` | **12** |

**§4 切分政策 —— 全數 `spec-verbatim`**

| 詞彙 | 命中 |
|---|---|
| `the amp is not present` / `the AMP is present` | 1 / 1 |
| `amplifier is not present` / `amplifier is present` | 1 / 1 |
| `shall not change the level` | 1 |
| `customer selects to change` | 3 |
| `store the new value in memory` | 1 |
| `personalization entry` | 13 |

**§6 外部參照 —— 兩種來源，須分別標示**

| 詞彙 | CFTS022 命中 | 類別 |
|---|---|---|
| `{VF651}` / `{CFTS019}` | 1 / 3 | `spec-verbatim`（CFTS022）|
| `speed controlled audio behavior` | 1 | `spec-verbatim`（CFTS022）|
| `AMP present configuration requirements` | 1 | `spec-verbatim`（CFTS022）|
| `LTM Non-Amplified` / `Amplified Audio System` | **0** / **0** | `spec-verbatim`（**VF651 檔名**）|
| `ANC` | 3 | `spec-verbatim`（CFTS022）|

**一項對 R36-4 三分法之補述**：`spec-verbatim` / `spec-derived` /
`test-setup` 之三分**預設只有一份 spec**。本 feature 引用兩份文件，
故 §6 之標示改為**點名來源**（`spec-verbatim (CFTS022)` /
`spec-verbatim (VF651 filenames)`）。兩個命中 0 的字串**不是自創** ——
它們逐字取自 VF651 之檔名，只是不在 CFTS022 裡。
若僅以「CFTS022 命中數」判斷，會把它們誤判為自創詞彙。

**§3.2 亦已補標類別**（本輪前已回溯但未標）：
`spec-verbatim` ×3、`test-setup` ×3、`banned` ×1。
節首並註明 **R36-3 之理由** —— 詞彙表之權威是被假定的，
故未標類別者視為未回溯。

### 1.3 §2.3 —— 兩項 gate

- **`spec-ref-order`**（R36-6）：`specification_reference` 之第一成分
  須等於 `spec_ref_reviewed.json` 所記之葉子條文。
  陽性對照為「顛倒順序」，負向對照為「正確順序」。
- **`test-group` 近似值**（R36-7）：新增 `"privacy"`（小寫）與
  `"Privacy "`（尾隨空白）兩例陽性對照，皆 FAIL。
  執行層前次自陳「本就會 FAIL，加測試只是確認既有行為」——
  該說法本身即為推定，**已實測**。

---

## 2. §5.2 —— 寫回路徑實作說明

落點 `features/privacy/scripts/write_back.py`。
**未複製任一既有 write_back 腳本**（四支皆封存，R20-3；複製即繼承
openpyxl 存檔路徑）。停手條件 2 未觸發 —— 所需元件皆已存在。

### 2.1 與 `xlsx_surgical` 之介面

```
openpyxl 載入 ENTRY 001 之工作簿  →  逐列寫入 11 TC（純記憶體）
                                  ↓
              surgical_save(wb, src, out)     ← 唯一落盤點
                                  ↓
        只重寫 xl/worksheets/sheet6.xml，其餘 47 個成員逐 byte 複製
```

openpyxl 只用來**計算要寫什麼**，不用來**產生檔案**。

### 2.2 invariant 檢查點（三層，落盤後依序執行）

| 層 | 檢查 | 依據 |
|---|---|---|
| 1 | `surgical_save` 內建 —— zip 成員集合、逐 sheet DV 計數 | R18-3 規則 2，ABORT 級 |
| 2 | `check_header_untouched` —— 第 1–9 列逐格比對 | BLANK workbook 無凍結資料區，表頭區即等價保證（Scope 欄、表單編號、文件管制區皆不在本腳本職權內）|
| 3 | `check_other_sheets` —— 其餘 9 個分頁逐格比對 | 同上 |

三層皆過方回報成功。**任一層失敗即 `WriteBackError`，不 warn。**

### 2.3 兩項刻意的設計

- **欄位由表頭文字解析，不讀 `feature.yaml` 之字母**：`feature.yaml`
  仍帶 rev C 之前的字母（A-PV13），recon 早已把落差列為證據。
  本腳本自當下的工作簿解析（結果：`design_method=R`、
  `functional_safety=S`、`author=AA`、`remarks=AH`）。
- **車型欄由合併儲存格橫幅定位**，不硬編 T–Z：讀第 8 列之
  `Vehicle Model 車型` 合併範圍得 `TUVWXYZ`。橫幅找不到即 ABORT，
  **不猜**。

---

## 3. §5.3 —— 結構驗證數據

| 項目 | 輸入基準（ENTRY 001）| 輸出（ENTRY 002）|
|---|---|---|
| SHA256 | `ed741d8d23f74878…` | `ad595ed0cad24375…` |
| bytes | 65,823 ⚠️（見上方 R42 更正：應為 **59,992**）| **63,001** |
| zip 成員 | 48 | **48**（零增零減）|
| classic DV | 3（sheet6）+ 1（sheet5）| **3 + 1** |
| x14 DV | 2 | **2** |
| 差異成員 | — | **僅 `xl/worksheets/sheet6.xml`** |
| 表頭區第 1–9 列 | — | 逐格未變 |
| 其餘 9 個分頁 | — | 逐格相同 |

**R 欄下拉（`下拉選單!$A$1:$A$9` / `$A$1:$A$11`）與 P/T–Z/AF 三組傳統 DV
全數保留。**

> ⚠️ **後續更正（R42，2026-08-14）**：本節之「輸入基準 bytes = 65,823」
> 為**歸屬錯誤** —— 65,823 是**空白範本**之大小，而寫回之真正輸入
> （ENTRY 001 準備工作簿）為 **59,992**。故寫回實為 **59,992 → 63,001，
> 變大**；下段之「bytes 反而變小」係跨越準備與寫回兩步之比較，
> 該比較本身成立但不是寫回那一步。
> **本節原文依例不改寫**（已提交之紀錄不因後續事件而失效），
> 更正見 `RULINGS.md` R42。

bytes 反而變小（65,823 → 63,001）：寫入 11 列內容的同時，
第 10–11 列殘留樣本之 sharedStrings 引用被替換、且新內容以 inline string
寫入，壓縮後淨減。**成員數與 DV 計數未變才是結構完整性之判準，位元組數不是。**

---

## 4. §5.4 —— BLOCKED 列之寫回行為驗證（單獨成節）

**BLOCKED 列落在第 18 列，`tc_id = NR1L-Privacy-009`** ——
tc_id 照序配發、不跳號（R34-3）。

### (1) `placeholder` 旗標是否影響寫回

| 欄 | 值 |
|---|---|
| D18 req_id | `SWE1-HMI-PRIVACY_FEATURES-008` |
| I18 test_item | `When the AMP wakes up on the Interior CAN, the AMP shall rec…` |
| N18 spec_ref | `CFTS022-4915173` |

**旗標未進工作簿**（它是 JSON 層之控制欄位，不是儲存格值），
該列各欄皆已正常寫入。✅

### (2) 四個空白欄位是否真為空

| 欄 | 值 | 判定 |
|---|---|---|
| P18 priority | `None` | ✅ 空 |
| R18 design_method | `None` | ✅ 空 |
| Q18 Estimated Test Time | `None` | ✅ 空 |
| T18–Z18 車型欄 | 七格皆 `None` | ✅ 空 |

四個驗證欄位皆為 `BLOCKED - see Remarks`：
J18 / K18 / L18 / M18 ✅

### (3) Remarks marker 是否完整無截斷

| 項 | 值 |
|---|---|
| 寫回長度 | **288** 字元 |
| 來源長度 | **288** 字元 |
| 逐字相符 | **True** |
| 開頭 token | `[BLOCKED-ECU]` |
| 結尾 | `…the leaf allocation (A-PV18 / RD-1 #12).` |

✅ 無截斷。288 字元寫入單一儲存格未被切斷 ——
這是本次唯一長文字欄位之風險點。

### (4) 樣式是否與其餘列一致

對第 17 列（相鄰之一般 TC 列）逐欄比對字型粗細／字級／填色／
`wrap_text`／框線樣式：

| 欄 | D | I | N | P | R | S | AH |
|---|---|---|---|---|---|---|---|
| 一致 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

列高亦相同（`row18 = row17 = 14.0`）。✅

**四項全符 → 停手條件 4 未觸發，ENTRY 002 得以新增。**

### 全列一覽（佐證欄位政策）

```
S 欄全 11 列  : NA ×11
車型欄 T 全列 : None ×11
B 欄序號      : =IF(ISBLANK($D10),"",ROW()-9) … =IF(ISBLANK($D20),"",ROW()-9)
```

---

## 5. §5.5 —— `DELIVERY.sha256` ENTRY 002 全文

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
#   未驗      **尚未由人以 Excel 實際開啟確認。** 同 ENTRY 001 之 R17-9 型前置。
ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f  output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Privacy_20260813_regen-v1.xlsx
```

**追加不覆蓋**（R27-2）—— ENTRY 001 原文一字未動。
驗證：`shasum -a 256 -c --ignore-missing DELIVERY.sha256` → **2 OK**。

---

## 6. §5.6 —— 欄 S／車型欄兩 gate 重標後之雙對照

依 **R34-6** 由 NOT MEASURED 重標為可實測。lint 現對 `output/` 內最新之
`*_regen-v*.xlsx` 執行該兩 gate。

```
=== 負向對照：未經破壞之寫回檔 ===
  findings=0  PASS ✓

=== 陽性對照 1：欄 S 改為非 NA ===
  findings=1  TRIGGERED ✓
    [column-s-na] row 12: Functional Safety is 'Yes', must be 'NA' (R30-3)

=== 陽性對照 2：車型欄填值 ===
  findings=1  TRIGGERED ✓
    [vehicle-blank] row 13 col T: 1, vehicle columns stay blank (R30-4)
```

破壞用之副本以 `surgical_save(verify=False)` 產生於暫存目錄，
**未觸及 `output/`**，測畢即刪。

### 6.1 全 19 gate 之雙對照

```
authorities: 9 design methods, 336 CFTS022 artifacts, Test Group 'Privacy', 3 Test Sets

positive control — every gate is deliberately violated once:

  baseline TC: clean (0 findings)

  TRIGGERED      design-method
  TRIGGERED      test-group
  TRIGGERED      test-group
  TRIGGERED      test-group
  TRIGGERED      test-set
  TRIGGERED      priority
  TRIGGERED      spec-reference
  TRIGGERED      er-modal
  TRIGGERED      step-er-parity
  TRIGGERED      step-count
  TRIGGERED      step-actions
  TRIGGERED      precondition-banned
  TRIGGERED      trailing-period
  TRIGGERED      negative-scope
  TRIGGERED      remarks-marker
  TRIGGERED      placeholder-body
  TRIGGERED      placeholder-blank
  TRIGGERED      placeholder-remarks

  TRIGGERED      spec-ref-reviewed (changed ref + unrecorded leaf)
  TRIGGERED      spec-ref-source-version (CFTS022 replaced)
  NOT TRIGGERED  spec-ref-order (references reversed)

all 18 + 1 gates verified reachable

negative controls — a compliant, similar input must NOT fire:

  PASS           design-method
  PASS           test-group
  PASS           test-group
  PASS           test-group
  PASS           test-set
  PASS           priority
  PASS           spec-reference
  PASS           er-modal
  PASS           step-er-parity
  PASS           step-count
  PASS           step-actions
  PASS           precondition-banned
  PASS           trailing-period
  PASS           negative-scope
  PASS           remarks-marker
  PASS           placeholder-body
  PASS           placeholder-blank
  PASS           placeholder-remarks

  PASS           spec-ref-reviewed (recorded ref + recorded source sha must not fire)
  PASS           spec-ref-order (correct order must not fire)
every gate has both controls
```

### 6.2 全批回跑

```
authorities: 9 design methods, 336 CFTS022 artifacts, Test Group 'Privacy', 3 Test Sets

linted 11 TCs from 10 leaf file(s)
workbook gates measured against FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_Privacy_20260813_regen-v1.xlsx (column S = NA, columns T–Z blank — R34-6)

PASS — no findings
```

---

## 7. §5.7 —— 台帳兩條指令輸出

```
$ shasum -a 256 -c BASELINE.sha256
  exit=0  OK=8  FAILED=0

$ shasum -a 256 -c --ignore-missing DELIVERY.sha256
  exit=0  OK=2  FAILED=0
```

---

## 8. §5.8 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，五項。第 1 項為 P7 之硬性前置。**

### 8.1 寫回產出尚未經人以 Excel 實開確認

**這是 P7 唯一未過的關卡。** ENTRY 001 之工作簿有 R29-1 之四點確認，
ENTRY 002 沒有。本輪之全部驗證仍在程式層 ——
成員數、DV 計數、逐格比對、樣式屬性 —— 而程式層驗不到 Excel 自身之
檔案完整性判定。

**建議之確認項（在 R29-1 四點之外，本輪新增之風險點）**：
1. 無「檔案已損毀，Excel 已修復」提示
2. R 欄下拉在第 10–20 列**是否可用** —— 原 DV 範圍為 `R10` 與 `R11:R59`，
   本次寫入 11 列，落在該範圍內，但**未實測 Excel 是否仍顯示下拉**
3. **第 18 列 Remarks 之 288 字元是否完整顯示**（儲存格層已驗，顯示層未驗）
4. B 欄序號是否正確顯示 1–11（公式已寫入，**Excel 計算結果未驗** ——
   本次未寫入 cached value，依賴 Excel 開啟時重算）

**第 4 點是本輪新增之依賴**：B 欄 11 格皆為公式且無 cached `<v>`。
AMFM v2 有同型情況且尚未經 Excel 驗證（R17-9 至今未解）。

### 8.2 `spec-ref-source-version` gate 尚未在真實換版下觸發過

陽性對照用的是人造 sha（`deadbeef…` ×8）。真正的換版
（同 id、不同內容之 CFTS022）**未發生過**，故該 gate 之
「訊息是否足以引導正確處置」未經現場檢驗。

### 8.3 profile §0 / §1 / §2 / §5 / §7 / §9 未標來源類別

本輪標了 §3.2 / §3.4 / §4 / §6 四節。其餘各節亦含引用 spec 之措辭
（如 §1 之 artifact id、§2 之 Test Set 名稱、§5 之 marker 定義），
**未依 R36-4 標註**。依該條「未標類別者視為未回溯」，
那幾節目前形式上皆為未回溯。

### 8.4 寫回腳本無測試

`features/privacy/scripts/write_back.py` 之三層 invariant
（表頭未變、其餘分頁相同、結構檢查）**只在本次真實資料上跑過一次**，
沒有陽性對照 —— 即「刻意改動表頭／其他分頁時，該檢查是否確實 ABORT」
未經驗證。依 R34-5 之精神，這三層目前應標為**未實測**而非 PASS。
`backend/xlsx_surgical.py` 之結構 invariant 有
`tests/test_xlsx_surgical_invariant.py`，但本腳本自加的兩層沒有。

### 8.5 11 列以外之寫回情境未驗

本次為 BLANK workbook 之首次寫入，第 10–20 列。
**未驗**：重複寫回（同一輸出再寫一次）之行為、
超過範本 tail（第 59 列）之列數、以及 `output/` 已有 `regen-v1` 時
再產 `regen-v2` 之命名與台帳處置。

<!-- UPSTREAM-COVERS: 14 -->
