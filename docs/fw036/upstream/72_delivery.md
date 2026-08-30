# 上繳包 72 —— T84 執行結果（下放包 72，全域線）｜**出貨包**

- 日期：2026-08-30｜方向：執行層 → 分析層
- 對應下放包：`docs/fw036/handoff/72_delivery.md`
- **319 個 TC｜可交付 124｜帶 `PENDING` 195｜037 覆蓋 311／311 = 100%｜寫回全部通過**

---

## 1. T84c —— 寫回驗證（本輪核心）

**`scripts/write_back_all.py`**（新）：沿用 `write_back_036.py` 之 `_set_row` 與逐 byte 重打包，
**一次寫入 319 列**（列 10–328），輸出 `features/sw_update/delivered/…_SWUpdate_20260830.xlsx`。

### 1.1 48 部件與結構量（R-SU2 之基線）

| 量 | 母本 | 輸出 | 基線 | |
|---|---:|---:|---:|:--:|
| zip 部件總數 | 48 | 48 | 48 | ✅ |
| worksheet 數 | 9 | 9 | 9 | ✅ |
| `<dataValidation`（sheet6） | 3 | 3 | 3 | ✅ |
| **`<x14:dataValidation`（sheet6）** | **1** | **1** | **1** | ✅ |
| `<extLst>`（sheet6） | 1 | 1 | 1 | ✅ |
| printerSettings | 5 | 5 | 5 | ✅ |
| media | 2 | 2 | 2 | ✅ |
| drawing 相關部件 | 13 | 13 | 13 | ✅ |
| `t="shared"` | 1401 | 1401 | 1401 | ✅ |
| **母本 SHA256 前後** | `6372fb6be02f…` | 同 | 未變 | ✅ |

### 1.2 **本輪新增之二項比對**（依下放包 72 §五-4 之查證）

| 量 | 母本 | 輸出 | |
|---|---:|---:|:--:|
| 全簿 `<dataValidation` | 4 | 4 | ✅ |
| 全簿 `<x14:dataValidation` | 1 | 1 | ✅ |
| **`calcChain.xml`** | 有 | 有 | ✅ |
| `sharedStrings.xml` | 有 | 有 | ✅ |

**其增列之理由見 §4（`sxm` 與 `amfm` 之先例）。**

### 1.3 逐部件 byte 比對與 `R` 欄

- **相異者 1／48**：`xl/worksheets/sheet6.xml`（**唯一被寫入者**）；部件名稱與順序相同
- **`R` 欄**：本簿用 **7 種** `design_method`，**逐字元皆見於 `下拉選單!$A$1:$A$9`**；
  **自輸出之 XML 反讀，其值之集合與所用者相同**

**寫回結果：全部通過 ✅**

### 1.4 交付簿之 lint（319 列）

```
A=0 B=0 C=0 D=0 E=0 F=0 G=0 H=0 I=0 I-sibling=0 **J=1** K=0 L=0 M=0
N=0 P=0 Q=0 R=0 T=0 **U=712** V=0 **I-cross=218** **W=21**
```

- **`J=1`** —— `SU-081`（`346`）之 `he WiFiUpdateService`，**037 之缺字（D-5），逐字保留**
- **`U=712`** —— 即 `PENDING` 行數，**帶 `PENDING` 出貨之預期值**
- **`I-cross=218`／`W=21`** —— **警示器非判準**（R-SU34 v3(c)／下放包 48 §二）；
  其大宗為 `Silent Update` 族之同窗同違例類（設計上如此：該組諸列本即驗同一段窗內之不同缺席）

---

## 2. T84a／T84d／T84e

- **T84a**：`SU-318`／`SU-319` 補齊 `116` 之「忽略」與「關閉」二支 ——
  **`COVERAGE_GAPS` 之 `未起草` 類歸零，`D-11` 結清**。lint 全 0。
- **T84d**：`docs/TESTRAIL_MAP.tsv`（319 列）——
  `tc_id｜row｜req_id｜test_set｜priority｜design_method｜has_pending`。
- **T84e**：**檢查清單全項結清**（D-1～D-11）——
  **其中 D-1～D-4／D-7～D-10 之結清方式為「其內容寫入交付說明」**，非另行處置。
  **唯一未由我方完成者為 Excel GUI 實開驗收（屬 Pei）。**

---

## 3. T84b —— 交付說明（`features/sw_update/docs/DELIVERY_NOTE.md`）

**七節**：①三數（**124 與 195 分開計，不合為一個覆蓋率**）②**Who owns each gap** 四類表
③「100% 覆蓋 ≠ 每一句都被驗到」④`PENDING` 之保留理由與七筆 DR ⑤**D-1～D-9 之逐項**
⑥各欄留空之理由（含 **`AH` 不併入 `REASONING.md`** 之裁定）⑦附件五項。

### 3.1 **Who owns each gap**（其數為本輪實測）

| 歸屬 | TC | 最強實例 |
|---|---:|---|
| **貴方規格之欠件** | **31** | `175` —— 何者為「safety-related」條件 |
| **台架能力之欠缺** | **120** | `184` —— 「across all session flows」於台架不可分 |
| **貴方之切分決定** | **27** | `313` —— 統攝 `315`–`320` |
| **外部系統之可及性** | **17** | `330` —— 其證據在 OTA 伺服器上，而我方從未確立可讀 |

**最大一塊為台架能力，且其大宗繫於一筆請求：DR-SU2 擋 151 個 TC。**

---

## 4. §五-4 之答 —— **有，且不只一種形態；該人工項仍必要**

**問：歷來各 feature 之寫回，有無任何一次是部件比對通過而 GUI 出錯的？**

**答：有二例，且其形態不同。**

| 例 | 程式層之結果 | 而其壞掉的是 |
|---|---|---|
| **`sxm` A-SX28（及其複發）** | 內容層不變量**全數通過**（215 TC、202／202 leaves 精確相等、TC ID 單調唯一、與 RUNBOOK close-out 完全一致） | **zip 成員 lost 11／added 10；x14 資料驗證 2 → 0；`R` 欄「測試用例設計方法」下拉遺失**。「重產並未加重損害，也未修復損害」 |
| **`amfm` R17-9** | zip 成員 59 = 59 零增零減、DV 4／2 完整、逐格零差異、連跑兩次 SHA256 相同 | **未壞，而未證明其不壞** —— 外科手術寫顯式 `<f>` 公式，新增列不在被逐 byte 保留之 `calcChain.xml` 內；**「Excel 通常會靜默重建」是推論不是實測**，故該筆列為 `DEFERRED` 待 Pei 實開 |

### 4.1 **故該人工項仍必要，而其所驗者不是我方比對過的東西**

> **我方之 48 部件比對，其對象是「部件在不在、內容變沒變」。**
> **GUI 所驗者是「Excel 接不接受」** —— 資料驗證下拉、`calcChain` 之重建、
> 列印設定、SmartArt／圖片。**二者不是同一層。**
>
> **`sxm` 那次尤其切題**：其 `R` 欄之逐字元核對會全綠（值確實在儲存格裡），
> **而使用者打開時下拉不見了。** **我方本輪之 `R` 欄核對，其限度與那次完全相同。**

### 4.2 **本輪已補跑 LibreOffice headless 預檢（自評第 1 項，於本包內補做）**

| 檢項 | 結果 |
|---|---|
| `soffice --headless --convert-to pdf` | ✅ **轉出成功，879 頁**，無錯誤輸出 |
| openpyxl 開啟 | ✅ 9 個工作表；TC 列 **10–328（319 列）**；`F10 = newR1L-SU-001`、`F328 = newR1L-SU-319` |
| 標準 dataValidation | ✅ 3 支（`P10:Q1411`＝P0–P3、`T10:Z1411`＝0/1、`AF10:AF1411`＝Pass/Fail/…） |
| **`R` 欄之 x14 下拉（`sxm` 那次壞掉的正是這個）** | ✅ **母本與交付簿逐字相同**：公式 `下拉選單!$A$1:$A$9`、範圍 `R10:R1411` |
| `R10` 之值 | ✅ `功能測試 (Functional based ; no specific technique)` |

> **`sxm` A-SX28 之損壞形態（`R` 欄下拉遺失、x14 DV 2 → 0）於本簿未發生** ——
> **其為一個實測，不再是推論。**
>
> ⚠ **惟 LibreOffice 不是 Excel** —— **本項把風險由「未知」降為「另一個實作可開」，
> 不能取代 Pei 之 Excel 實開**（`calcChain` 之重建、SmartArt、列印設定於 Excel 之行為仍未驗）。

### 4.3 本輪據此擴充了比對（§1.2）

**新比 `dataValidation` 節點數（全簿）與 `calcChain.xml` 之存廢** ——
**其為 `sxm`／`amfm` 二例所指之處。二項皆通過。**
**惟其仍不蘊含 GUI 可開** —— **擴充後之比對只是把「已知會壞的兩處」納入，
不是把「所有會壞的地方」納入。**

---

## 5. 獨立自評

### 5.1 **本輪我做得到而沒做的檢定**（固定項）

| # | 我能做什麼 | 它可能否證什麼 | 未做之理由 |
|---:|---|---|---|
| 1 | ~~以 LibreOffice headless 開啟交付簿並轉出 PDF~~ | —— | ✅ **本包內已補做**（§4.2）：轉出 879 頁 PDF，`R` 欄 x14 下拉逐字保留。**其為「把剛寫下的結論接到下一步」之補正** |
| 2 | 對 195 個帶 `PENDING` 之 TC 逐列核其 `PENDING` 措辭與 `PENDING_LIST` 之型別是否一致 | 可測我方型別標記之內部一致性 | 成本中等 |
| 3 | 以 `TESTRAIL_MAP.tsv` 回測 TC ID 與列號之單調性 | 可證寫回未錯位 | **已由寫回腳本之逐列輸出間接證之** |

> **第 1 項應該做** —— **它正是 §4 所指之風險最便宜的一次探測，而我在寫完 §4 之後
> 仍未去做它。** 其與 B-43（「做了會很麻煩」是一個需要被量的命題）同族，
> **只是這次的成因不是估錯成本，是沒有把自己剛寫下的結論接到下一步。**

### 5.2 一項交付前之提醒

**`delivered/` 之工作簿與 `MANIFEST.tsv` 尚未同步** —— 其登錄屬 T84f 之提交，
**而 git 由 Pei 執行**。

---

## 6. 待裁事項

| # | 事項 | § |
|---:|---|---|
| 1 | **寫回通過，交付簿已產出** —— 追認 | 1 |
| 2 | **Excel GUI 實開驗收**（屬 Pei）：無修復提示／`R`·`P` 下拉可用／列印設定在 | 1、4 |
| 3 | ~~LibreOffice headless 之預檢~~ —— **已於本包補做**，見 §4.2 | 4.2 |
| 4 | 交付說明之七節 —— 追認或增修 | 3 |
| 5 | `MANIFEST.tsv` 之登錄 | 5.2 |

---

## 7. T84f —— 提交指令（**未執行，git 屬 Pei**）

```bash
git add features/sw_update/scripts/gen_batch23.py \
        features/sw_update/scripts/write_back_all.py \
        features/sw_update/scripts/mask_test.py \
        features/sw_update/docs/DELIVERY_NOTE.md \
        features/sw_update/docs/TESTRAIL_MAP.tsv \
        features/sw_update/DELIVERY_CHECKLIST.md \
        features/sw_update/COVERAGE_GAPS.md \
        docs/fw036/upstream/72_delivery.md \
        docs/fw036/lint_reports/SWUpdate__sw_update_7f019b37_20260830.md

git commit -m "feat(sw_update): deliver 319 test cases, 311/311 requirement coverage

124 are executable as they stand; 195 carry a placeholder naming the data request
it waits on. Write-back verified: 47 of 48 parts byte-identical, data validation and
calcChain preserved, all seven design_method values match the master dropdown."
```

⚠ **`delivered/` 之工作簿是否入版控，依 `0f33849` 之裁定（交付件不入 git）——
本指令未含該檔。**

---

## 8. ⚠ 補正（Pei 指出，2026-08-30 出貨後）：**交付本未依 `Requirement or Design ID` 排序**

**R-BLM17（Pei 2026-08-27 裁「乙」，bed_lowering 立）**：
**交付本依 `Requirement or Design ID`（D 欄）升冪重排，TC ID 隨列重新指派。**

**而本 feature 之首版交付本依起草批次序寫回** —— **該裁定就在 repo 內
（`features/bed_lowering/docs/handoff/17_row_order_by_reqid.md`），我未查即寫回。**

### 8.1 已重排並依 R-BLM17 §1.3 之七項逐項驗證

| # | 檢項 | 結果 |
|---:|---|---|
| 1 | **內容不變性** —— 以 `req_id` 配對，逐列比 TC ID 與列號以外之**全部 15 欄** | **相異 0 欄** ✅ |
| 2 | **排序正確性** —— `req_id` 之**數值**逐列非遞減 | 逆序 **0** 處；**同一 req 之多列未被拆散 0 處** ✅ |
| 3 | **TC ID 連續性** | `newR1L-SU-001`–`-319` 無跳號無重複 ✅ |
| 4 | **計數** | 交付本 **319** 列 = 生成器 **319** 個 TC ✅ |
| 5 | **保全計數**（legacy DV 與 x14 分開計） | 母本／交付：標準 DV **3**／**3**、x14 DV **1**／**1**、部件 **48**／**48** ✅ |
| 6 | **全簿 lint** | `J=1`（D-5 之缺字）、`U=712`（`PENDING` 行）、其餘 A..W 全 0 —— **與重排前逐項相同** ✅ |
| 7 | **round-trip** | 期望值取自**配對表**（生成器），實測值取自**交付本實檔** —— **二來源不同** ✅ |

**排序鍵**：`SWE1-FOTA-{nnn}` 之 `nnn` 以**數值**排（非字串）；
**同一 req_id 之多列以其起草序為次鍵（穩定排序）**，使一列之內的各 facet 相鄰且不被打散。
**新增 `scripts/verify_order.py`**（七項驗證之實作）。

### 8.2 連帶更新

- `docs/TESTRAIL_MAP.tsv` —— 依新列序重出（`SU-001` = `SWE1-FOTA-003`；`SU-319` = `SWE1-FOTA-383`）
- `docs/PENDING_LIST.md` —— 逐列表依新列序重出，並增「列」欄
- `docs/DELIVERY_NOTE.md` §1 —— 增列序之說明
- **LibreOffice headless 預檢重跑** —— 轉出 PDF 成功，**`R` 欄 x14 下拉逐字保留**（`下拉選單!$A$1:$A$9`，`R10:R1411`）

### 8.3 其成因 —— **不是沒查到，是沒有去查**

**R-BLM17 為跨 feature 適用之裁定**（其標頭即載「Pei 裁『乙』」），
**而我在 T84c 寫回時未查既有 feature 之交付慣例。**

> **本 feature 之寫回腳本自 display 移植**（`write_back_036.py` 之註即載此），
> **而移植的是「怎麼寫」，沒有一併移植「寫成什麼樣」。**

**其與 B-44（用組名代替組之內容）不同族，而與 B-43 同族**：
**B-43 是「對未做之事估其後果」；本項是「對未查之事假設其不存在」。**
**二者皆為：在沒有去看的情況下，先當它不是問題。**

**入 `BACKLOG.md` B-46。**
