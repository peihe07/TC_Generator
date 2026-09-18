# Diagnostics —— 佔位填值請求（asset request）

依 **R-DIAG15**（比照 R-SEC21）＋ **R-DIAG33**（佔位之兩類）。
對應 `sandbox/placeholder_summary.tsv`（**592 行／429 條 TC**，含 `class` 欄）。
母體：`diagnostics_v13.xlsx` 合併本 **565 列**（Layer 2 20 組全產／389 個 037 列，100%）。

---

## ⚠ 執行前提（R-DIAG33(a)）

**本交付本之絕大多數佔位為「工具可解」（`TOOL_RESOLVED`）** —— 其值定義於本 ECU 之 **CDD 檔（CANdela）**，
手動執行時由載入該檔之診斷工具解出，TC 保留 `<…>` 佔位**即為可執行**。

| class | 行數 | 條數 | token |
|---|--:|--:|---|
| `TOOL_RESOLVED` | **574** | **427** | `DR-DIAG-4` 99／`DR-DIAG-5` 206／`DR-DIAG-6` 269 |
| `ASSET_MISSING` | **18** | **18** | `DR-DIAG-8` |

**故不可派工者只有 18 條**（交付本中整列以 `FCE4D6` 著色者），其餘 547 條可直接執行。

---

## 一　`ASSET_MISSING` —— 真缺件（三件）

### 1.1　`DR-DIAG-8` —— `SX-9830-0095` 本文 ＋ vehicle sales code → PkgIndex 對照（**18 行／18 條 TC**）

`CFTS004-4940451`／`-4940461`／`-4940450`／`-4940462` 明引 `SX-9830-0095` 與 `CIP Radio Tables`。
**流程圖已到**（`cip_radio_tables_v6_7`，CDD-12 登錄並轉錄），retry 五結局已據以產出。

**仍缺**：

| 件 | 為何需要 |
|---|---|
| `SX-9830-0095` "Sirius XM Multi-Package Factory Activation OEM Requirements" 本文 | `<Package Indication value>` 之編碼定義於此；流程圖只書「依 vehicle sales codes 決定 PkgIndex」，未給值 |
| vehicle sales code → PkgIndex 對照表 | 同上；`CIP_Radio_Tables_v6.7` 之 12 分頁均無此表 |

**此值不在 CDD 檔內**（PkgIndex 由車輛銷售代碼決定，非 ECU 之診斷資料定義），故列為真缺件。

### 1.2　`DR-DIAG-7` —— `KeySense HMI Logic and Flow`（**非佔位**）

`CFTS004-4940469` 明引而該件不在來源集。只影響 `NR1L-DIAG-290` 之 ER 深度（現只斷言常式正回應與完成，R-DIAG19）。

### 1.3　`DR-DIAG-11` —— `SD.00049` 之附件 `Diagnostic Services Secure Access Rights 28JAN2026.xlsx`（**非佔位**）

`SD.00049.pdf` 原件已取得（`STLA Standard/Update/`，Change Level F），其 §3 明言存取權矩陣在該內嵌 xlsx，
**該 xlsx 未附於 PDF**。只影響 I/O 母節 114 列之 PC-3 去留（現依 R-DIAG13 保守加 `Security access 0x27 has been granted`）。

---

## 二　建議取得 ECU CDD 檔（`.cdd`）—— **非交付前提**

`TOOL_RESOLVED` 之 574 行佔位，其值皆在本 ECU 之 CANdela 檔內：

| token | 佔位型 | CDD 檔內之對應 |
|---|---|---|
| `DR-DIAG-4` | `<controlState for "…">`／`<out-of-range controlState>` | 各 I/O DID 之 `controlState` 參數定義與其列舉值 |
| `DR-DIAG-5` | `<… byte>`／`<… record>`／`<out-of-range value>` | 各 DID 之資料位元組版面、值域與換算 |
| `DR-DIAG-6` | `<unsupported SID>`／`<unsupported DID>` | 工具之服務／DID 清單 —— **清單中不存在者即為不支援** |

**取得後可將該類佔位填為實值**，供自動化測試腳本使用。
**手動執行不需要** —— 診斷工具載入 `.cdd` 後即以人可讀之名稱呈現這些值。

---

## 三　到件後之處置

依 **R-G72**：已交付本不就地改，以 `_Revise{n}` 本發出；
`placeholder_summary.tsv` 逐行對照填值（`class` 欄可作篩選），填畢後該行自表移除。
