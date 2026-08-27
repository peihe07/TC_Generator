# 上繳包 02 —— 編號歸屬處分、036 母本補位（T-登、T8a–c）

- 日期：2026-08-27
- 對應下放：`docs/handoff/03_review_close.md`
  （SHA256 `838f8a50fd2b5f5c4945d8e755c6350aff85dc4ee7aa86ad4721f815f890d04e`，102 行）
- **結論：T-登、T8a–c 全數完成。R-DD2 之閘補跑通過（D2 = `newR1L`）。**
- **framework 未落檔** —— §五 為提案，待 Pei 裁。
- 未寫 profile、未產任何 TC、未寫回、未進行任何 git 操作。

---

## 1. T-登 —— 編號歸屬

依 §二「台帳先登先得」：

| 編號 | 內容 | 狀態 |
|---|---|---|
| **A-DD1** | `-025`~`-028` 市場條件衝突 | PENDING（待 DR-DD1）|
| **A-DD2** | `$PARK_BRK_EGD$` 四庫皆查無 | PENDING（待 DR-DD2）|
| **A-DD3** | 狀態命名兩制（`Locked/Unlocked` vs `RESTRICTED/NOT_RESTRICTED`）| **RESOLVED**（登記即結案）|
| ~~`_x000D_` 正規化~~ | **作廢，不登異常** | §二-3 之分析層自認 |

**A-DD2 條目上方已加註**「包 01 §二 之候選編號 A-DD2／A-DD3 已由本包 §二
重配，以台帳為準」，並一併記明 `_x000D_` 候選之作廢。

**A-DD3 之結案理由已逐字入檔**：R-DD3 已定 ER 主錨為 HMI 現象 →
**兩套列舉皆不得出現於 ER**；`test_item` 上半 verbatim 照 037 原文
（含 `RESTRICTED` 措辭）不改字。**二制之衝突不落到產出上** ——
一個在 ER 被 R-DD3 擋掉，另一個在上半以 verbatim 保留。

**§一-5 之拘束**（`Sub Categorization` 尾空白）另立一節記入 `ANOMALIES.md`：
「日後任何以該欄為鍵之比對一律 verbatim 含尾空白，或於比對端明文 rstrip
並揭露；**不得靜默修資料**。」

---

## 2. T8a —— 母本副本，cmp ＋ sha 雙驗

```
來源  forms/FM-WI-FSM-036-A01 …_20260817_ext.xlsx   200,650 B
副本  features/driver_distraction/workbook/driver_distraction_00.xlsx

cmp   逐位元全等 ✅
sha   6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2（原件）
      6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2（副本）  相符 ✅
```

### 2.1 T8a 之 openpyxl 禁令 —— 我實測了它所指的東西

下放包稱「本副本自始不得經 openpyxl 存回（R 欄 x14 下拉摧毀，A-UP09 同族）」。
**實測該分頁之驗證結構**：

| 量 | 值 |
|---|---|
| 標準 `dataValidation` | 3 條 |
| **`x14:dataValidation`** | **1 條** |
| x14 清單來源 | **`下拉選單!$A$1:$A$9`**（跨分頁 range）|
| x14 範圍 | **`R10:R1411`** |

**openpyxl 讀不到 x14 擴充**（其載入時直接警告
`Data Validation extension is not supported and will be removed`）——
**禁令所指為真，非預防性措辭**。已逐字寫入 `feature.yaml` 之
`paths.workbook` 註解與 `workbook.writeback_method`。

**本輪對副本只做 `read_only=True` 載入，未 save。**

---

## 3. T8b —— R-DD2 之閘

```
C2 = "專案名稱 Project  Name："
D2 = "newR1L"
```

**相符 ✅** —— `tc_id_format: "newR1L-DD-{n:03d}"` 生效。
已於 `feature.yaml` 逐字記明其為**實測**而非沿用。

---

## 4. T8c —— `feature.yaml` 回填

### 4.1 `workbook_state` = **BLANK**（實測，附依據）

```
自 r10 至 r1411：
  D 欄（req id）非空列          = 0
  除 B 欄外任一欄非空之列       = 0
  B 欄非空列                    = 1402   ← **公式宿主，非資料**
  B10 = '=IF(ISBLANK($D10),"",ROW()-9)'
```

**判 BLANK 之依據須寫清楚**：若以「B 欄非空」判，1402 列會使它看起來像
DONE-REGION。**故不以 B 欄判 state** —— 已逐字記入 yaml。

### 4.2 表頭與欄位 —— **逐項實測，未轉錄**

下放包 §三 T8c 明文「bed_lowering 為 row 9 起，**本 feature 以實測為準，
不轉錄**」。實測：**表頭 r9（33 個非空表頭格）、資料自 r10、模板至 r1411**。

19 個欄位逐一自表頭字串定位（`C` polarion_id … `AH` remarks），
另記二項拘束：
- **`do_not_write: ["B"]`** —— B 欄為公式宿主，覆寫即毀序號欄
- **`writeback_method: "xml_surgical"`** —— 依 §2.1 之實測

### 4.3 diff

```diff
--- /tmp/dd_yaml_before.yaml	2026-08-27 20:13:03
+++ feature.yaml	2026-08-27 20:13:24
@@ -9,9 +9,12 @@
 test_group: "Driver Distraction"          # R-DD1；取 037 `Project Name` 欄實值（實測 r3 = "Driver Distraction"）
 
 paths:
-  # ⚠ **036 母本不在 inputs/** —— 下放包 01 T2 只列 S1–S4（＋S5 依 Q5）。
-  # R-DD2 之「project 前綴權威為工作簿 D2」**因此尚不可實測**（上繳包 01 §6）。
-  workbook: null
+  # 036 母本於下放包 03 §三（T8）補位 —— 包 01 T2 之漏列為分析層之誤，該包自認。
+  # **副本自 `forms/` 之原件複製，cmp 逐位元全等 ＋ sha256 雙驗**（T8a）。
+  # ⚠ **本副本自始不得經 openpyxl 存回**（T8a 明文，A-UP09 同族）——
+  # 實測其 `R10:R1411` 之設計方法下拉為 **x14 擴充**（清單來源 `下拉選單!$A$1:$A$9`），
+  # openpyxl 讀不到且 save 時會將其刪除。
+  workbook: "workbook/driver_distraction_00.xlsx"
   a03_report: "inputs/DD_SWE1_0807_EN.xlsx"
   sys1_export: "inputs/SYS1_HMI_Driver_Lockout_HMI_Logic_and_Flow_R1_SR24_1A_(May_3_2021).xlsx"
   spec_pdf: "inputs/Driver Lockout HMI Logic and Flow R1 SR24 1A (May 3 2021).pdf"
@@ -21,11 +24,14 @@
 spec_reference_template: null              # R-DD1 未裁；錨定協定屬 Phase 2/3
 
 # TC ID 之格式（IN §10.3）—— **R-DD2**（Pei 2026-08-27 裁定）。
-# project 前綴之權威為工作簿 D2 儲存格；**036 母本到位後須實測確認為 `newR1L`**，
-# 不符即停並回報，不得逕改本字串。
+# **R-DD2 之閘已補跑（T8b）**：副本 D2 實測 = `newR1L`，**相符**。
+#   C2 = "專案名稱 Project  Name："   D2 = "newR1L"
 tc_id_format: "newR1L-DD-{n:03d}"
 
-workbook_state: null                       # 036 母本未到，未量
+# **BLANK**（T8c 實測）：自 r10 至 r1411，**除 B 欄外任一欄非空之列 = 0**；
+# D 欄（req id）非空列 = 0。B 欄之 1402 列為公式宿主
+# （`=IF(ISBLANK($D10),"",ROW()-9)`），**非資料** —— 故不以 B 欄判 state。
+workbook_state: "BLANK"
 
 reference:
   # S1–S5。**sha256 自實體檔重算**（T2）。
@@ -55,6 +61,10 @@
   dbc_fdcan8:
     file: "features/vehicle_setting/inputs/PDT27_E2A_R5_FDCAN8.dbc"
     sha256: "51c8fd6092925071bbf443711e5161d78df292de232dc7427b1cceaa8f181cd2"
+  workbook_master:
+    # 綁 `forms/` 之**原件**（非本 feature 之副本）—— 原件變動才是需偵測之事件。
+    file: "forms/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx"
+    sha256: "6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2"
   proxi:
     file: "features/vehicle_setting/inputs/PROXI_HDCC27_R3_20250424.xlsx"
     sha256: "e7c2020f01c3d58db431babe7f8a41acbe528c451bd37ef6bb84f1b312be6ff2"
@@ -63,6 +73,40 @@
   # R-DD4：SYSAD **不入** prompt_sources。
   prompt_sources: ["a03_report", "cfts022_sysra", "sys1_export", "spec_pdf"]
 
+workbook:
+  # **逐項自副本表頭實測**（T8c，下放包 03 §三明文「以實測為準，不轉錄」）。
+  sheet: "Test Case Specification 測試用例規範"
+  header_row: 9              # 實測：r9 有 33 個非空表頭格
+  first_data_row: 10
+  last_template_row: 1411    # 實測：B 欄公式宿主至 r1411（1402 列）
+  columns:
+    polarion_id: "C"         # Requirement or Design ID (Polarion)
+    req_id: "D"              # Requirement or Design ID
+    tc_id_testrail: "E"
+    tc_id: "F"
+    test_group: "G"
+    test_set: "H"
+    test_item: "I"
+    pre_conditions: "J"
+    input_test_data: "K"
+    test_procedure: "L"
+    expected_result: "M"
+    spec_reference: "N"
+    tc_ref_id: "O"
+    priority: "P"
+    est_test_time: "Q"
+    design_method: "R"
+    functional_safety: "S"
+    author: "AA"
+    remarks: "AH"
+  # ⚠ **B 欄不得寫入** —— 其為公式宿主 `=IF(ISBLANK($Dn),"",ROW()-9)`，
+  # 序號由 D 欄之填寫經公式自動產生。
+  do_not_write: ["B"]
+  # ⚠ **寫回不得經 openpyxl 存檔** —— R10:R1411 之設計方法下拉為 x14 擴充
+  # （清單來源 `下拉選單!$A$1:$A$9`），openpyxl 讀不到且 save 時會刪除它。
+  # 實測：標準 dataValidation 3 條、x14 dataValidation 1 條。
+  writeback_method: "xml_surgical"
+
 a03:
   sheet: "Analysis Report"
   header_row: 8
```

---

## 5. 未結 DR

| DR | 狀態 | 阻斷 |
|---|---|---|
| DR-DD1 | **DRAFTED**（待 Pei 發送）| `-025`~`-028` 四 leaf 凍結 |
| DR-DD2 | **DRAFTED**（待 Pei 發送）| 不阻斷；`-021`~`-024` 之訊號名待定 |

**二筆狀態未變** —— 本輪無發送動作，執行層亦不代發。

---

## 6. framework —— **未落檔**

§五 為**提案，待 Pei 裁**。下放包 §六 之任務表列「（待裁後）framework.md
落檔（§五 准後）」——**未准，故未落**。

**六組之閉合我複核了**：2+6+4+4+8+4 = **28** ✅，與 T3/T4 之 28 leaf 相符。
組 6 之 4 leaf 即 A-DD1 所凍結者，其 PENDING 標記與 framework 鎖定
之關係已於 §五 說明，本輪不預作。

---

## 7. 獨立自評

1. **`workbook_state` 差一點判錯。** B 欄有 1402 列非空，
   第一眼像 DONE-REGION。**是因為 vehicle_category 那份母本我量過同一個東西**
   才知道那是公式宿主 —— 但我沒有沿用該結論，**重新量了 D 欄與 A–AH**。
   判準（不以 B 欄判）已寫進 yaml，下一個人不必再踩。
2. **T8a 之禁令我沒有只記下來。** 「不得經 openpyxl 存回」若只抄進註解，
   下一個寫寫回腳本的人不會知道它有多真。**去量了 x14 之條數與範圍**，
   把 `R10:R1411`／`下拉選單!$A$1:$A$9` 寫進 yaml —— 那是可驗的，「禁令」不是。
3. **A-DD3 我照 §二-2 逐字落，沒有加自己的判斷。** 它是 RESOLVED，
   而 RESOLVED 的條目最容易被順手補一句「建議日後如何如何」——
   那會使一個已結案的條目重新變成待決。

---

## 8. 量測條件揭露（R-G8）

- **副本之驗證為 `cmp` ＋ sha256 雙驗** —— `cmp` 驗逐位元、sha 驗整體，
  二者皆過。**單用其一皆不足**（sha 相同而 cmp 不同在理論上不可能，
  但 cmp 給的是「第一個相異位元組在哪」這個資訊）。
- **`workbook_state` 之判定母體為 r10–r1411 × A–AH**；
  **r1412 之後未掃** —— 模板之公式宿主止於 r1411，其後若有資料本判定看不到。
- **x14 之計數以直接解 zip 讀 `xl/worksheets/sheetN.xml`** 為之，
  非 openpyxl（後者讀不到）。
- **表頭之欄位定位以字串比對**（`Requirement or Design ID` 等）——
  若日後母本改表頭措辭，`feature.yaml` 之 `columns` 須重測，**現無檢查攔它**。
- **framework 之六組閉合為複核**（2+6+4+4+8+4=28），
  **未複核各組之 leaf 歸屬是否合理** —— 那屬 framework 鎖定之裁定範圍。
