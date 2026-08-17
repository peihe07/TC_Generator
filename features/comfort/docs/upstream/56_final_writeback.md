# 56 — Comfort HMI / 範本驗證 **不通過**，最終寫回未執行

- 產出層：執行層｜2026-08-16｜對象：分析層／Pei
- 覆核對象：`docs/handoff/78_final_writeback_prep.md`、`79_delivery.md`
- **結論：78 §2 之四項中一項 FAIL —— 依其「任一項不過即停」之指示，未進 §3，未登 ENTRY 022／023。**

---

## 1. 範本驗證（78 §2）—— 3 PASS／1 FAIL

對象：`…_Comfort_20260816_prepared_ext.xlsx`，123,744 bytes，
SHA256 `10913771c2d7bad40ce571c386d44de48087533c7ebd5eb56d02207a4ce68d4c`
（來源母本 `…_20260815_prepared.xlsx` = `b68117a2…`，未被覆寫，仍在）

### 1.1 DV `sqref` 涵蓋（B／R／P／T–Z／AF）

| 欄 | 擴充前 | **擴充後（實測）** | 判定 |
|---|---|---|---|
| **B** 編號公式 | row 10–59 | **row 10–601** | PASS |
| **R** design_method（x14 DV）| `R10` ＋ `R11:R59` | **`R10:R601`** | PASS |
| **P** priority | `P10:Q11` | **`P10:Q601`** | PASS |
| **T–Z** | `T10:Z11` | **`T10:Z601`** | PASS |
| **AF** 測試結果 | `AF10:AF11` | `AF10:AF11 AF60:AF61 AF110:AF111 AF160:AF161 AF210:AF211 AF260:AF261 AF306:AF307 AF356:AF357 AF406:AF407 AF456:AF457 AF506:AF507 AF556:AF557` | **FAIL** |

**AF 之實測**：row 10–500 之間**只有 20 列受 DV 涵蓋，471 列未涵蓋**
（首個未涵蓋為 row 12，末三個為 498／499／500）。

其形態為**每 50 列一組、每組只有 2 列**——與原本 `AF10:AF11` 之
「2 列」相同。**這是原有之 2 列 DV 被隨某個 50 列區塊反覆複製的結果，
而非被延伸。** 其餘四項是延伸（單一連續範圍），只有 AF 是複製。

**修法（一次動作）**：於 Excel 選 `AF10:AF500`，重新套用資料驗證
（來源 `Pass, Fail, Pending,Block,NA`，即現行 AF DV 之同一字串），
或自 `AF10` 之格式複製並貼至 `AF11:AF500` 之「僅驗證」。

### 1.2 B 欄公式抽格（78 §2 指定之四格）

| 格 | 實測 |
|---|---|
| `B60` | `dtype='f'`，`=IF(ISBLANK($D60),"",ROW()-9)` |
| `B200` | `dtype='f'`，`=IF(ISBLANK($D200),"",ROW()-9)` |
| `B438` | `dtype='f'`，`=IF(ISBLANK($D438),"",ROW()-9)` |
| `B500` | `dtype='f'`，`=IF(ISBLANK($D500),"",ROW()-9)` |

另抽 `B10`／`B59`／`B501` 亦為公式。**四格皆為公式而非值 —— PASS。**

### 1.3 zip member 數與差異範圍

- member 數 **48 = 48**，無新增亦無消失 —— PASS
- **位元組層面 15 個 member 有差異**：`docProps/core.xml`、`xl/calcChain.xml`、
  `xl/styles.xml`、`xl/sharedStrings.xml`、`xl/workbook.xml`、
  `xl/drawings/vmlDrawing1.vml`、`sheet1–sheet9.xml`
- **內容層面：全 9 個工作表逐格比對，共 542 格不同，且 542 格全部是
  `Test Case Specification` 之 B 欄 row 60–601 之公式**
  （601 − 60 + 1 = 542，數字自證）。**其餘 8 個工作表、其餘全部欄位，
  0 格不同。**

**判定：PASS（附條件）**。字面之「差異僅限預期之 sheet xml」不成立，
但其不成立之原因是 **Excel 另存時會重寫 styles／sharedStrings／calcChain
等共用部件**——這是人在 Excel 中操作之必然結果，與本次擴充無關。
**故本層以「內容層面 0 格非預期差異」判其通過**，並在此載明改判之理由，
以免日後讀者以為位元組差異被忽略了。

### 1.4 R 欄下拉九項逐字元

`下拉選單!A1:A9` 之九項（`功能測試…`／`狀態轉換…`／`決策表…`／`等價劃分…`／
`邊界值分析…`／`組合測試…`／`情境 / 用例…`／`負向測試…`／`基礎故障注入…`），
`A10`／`A11` 為空。ext 之 x14 DV 公式為 `下拉選單!$A$1:$A$9` —— **PASS**。

**附帶訂正一項**：擴充前 R 欄有**兩個** DV，`R10` 指向 `$A$1:$A$9` 而
`R11:R59` 指向 **`$A$1:$A$11`**（多含兩個空列）。擴充後合併為單一
`R10:R601` → `$A$1:$A$9`。**此為改善**（原 row 11 起之下拉會多兩個空選項），
本層未要求而 Pei 之操作順帶修掉，記此以免日後被當成非預期變更。

---

## 2. 因此未做之事

- **未登 ENTRY 022**（範本驗證未通過，不得記為 template-extension 已驗）
- **未執行最終寫回、未登 ENTRY 023**
- 78 §3.2 之「三項固定 FAIL 應轉 PASS」尚未驗證。**依現況預測：
  B 欄與 R 欄二項會轉 PASS，P 欄一項會轉 PASS，AF 不在該三項之列**
  —— 亦即**若不修 AF，最終寫回之 14 項 assertion 仍會全數 PASS**。
  本層仍不逕行，因 78 §2 之指示為「任一項不過即停」，
  而 AF 是 78 §1.2 表列之第 4 項。**請分析層裁定二者擇一**：
  (a) Pei 修 AF 後重驗，或
  (b) 裁定 AF 不在最終寫回之前置條件內，本層據以續行並將 AF 記為未決項。

---

## 3. 三項久懸量測（78 §3.3）—— 先行實測

**量測對象為 ENTRY 021 之產出**（`…_20260815_enumsplit.xlsx`，429 列），
非最終寫回之產物；最終寫回後將重測。**三項之結果不依賴母本之列數**，
故先行報出。

| 項 | 實測 |
|---|---|
| **P 欄允許集合** | 429 列之值：`P1` 296、`P2` 124、`P3` 9；**落在允許集合 {P0,P1,P2,P3} 之外者 0 列** |
| **A-CF19 內容完整性** | N 欄 429 格與 JSON **逐字元比對，不符 0 格**；最長 **600 字元**（`NR1L-ComfortHMI-323`，多節 spec_ref）；多節 spec_ref 共 **416 條**（429 中之 97%）|
| **A-CF16 marker row 可見性** | AH 欄寬 11.83、列高 14.0 → 可見約 **11 字元**。五列之首行實際可見：`[BLOCKED-SP`（010／012／382／383）、`[BLOCKED-NO`（081）。**`Owner:` 不可見；`[BLOCKED-NON-HMI]` 亦不完整** |

**P 欄一項之意義**：78 §3.3 稱其「427 列自寫入以來從未受下拉約束」，
**實測結果是 429 列全部合格**。該值之正確性此前僅由 generator 之常數保證，
現已對照 DV 之允許集合實測 —— **它一直是對的，但這是第一次被證明。**

**A-CF16 之判定**：marker 於列高 14.0 下**不可讀**（只見前 11 字元）。
惟三類 marker 之前 11 字元已足以區分二類（`[BLOCKED-SP` vs `[BLOCKED-NO`），
且評閱者以搜尋而非目視尋找 marker。**列高屬呈現，程式不得自改**（26 §2）——
故此為量測而非缺陷，其處置已於交付說明中改為「搜尋 Remarks 欄之 `[BLOCKED`」。

---

## 4. 交付說明草案（79 §2.2）—— 已起草，**未放入交付夾**

`docs/Comfort_HMI_delivery_note.md`（檔名由本層定，可改）。其結構：

| 段 | 內容 |
|---|---|
| 版本 | **明載其為某一版本而非最終版**（79 §4）|
| 涵蓋 | 429 test cases covering 378 of the 403 verification units；並解釋「一單位可有多列」之成因 |
| 未涵蓋 | **25 個單位逐列**：`req_id`｜節｜一句話說明所缺者（自 RD-1 之問句改寫為陳述句）|
| 部分涵蓋 | **`SWE1-HVAC-047` 另立一段** —— 它**有列**（可用側已測），缺的是不可用側 |
| 5 列 marker row | 逐列具名 tc_id｜節｜無 procedure 之理由；並告知以搜尋 `[BLOCKED` 尋找 |
| 螢幕尺寸 | 五條之尺寸取自條文，若該配置不在本專案內應撤下而非執行 |
| 尚未解決 | 問題文件已備妥**尚未發出**；答覆後之二種去向 |

**一項訂正**：79 §2.2 寫「26 個 leaf 不產任何列」，
**實數為 25**——`SWE1-HVAC-047` 有列（`NR1L-ComfortHMI-070`，可用側）。
RD-1 之「26」是**被問到的單位數**，其中一個是部分涵蓋而非零涵蓋。
403 − 378 = **25**，與交付說明之表列數一致。

**紀律自查**：全文 grep 無 `R-C`／`A-CF`／gate 名／下放包編號／`§`；
無我方傾向語；無對答案之預測。

---

## 5. SR25 兩檔之確切檔名與 bytes（79 §3）

交付夾 `/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Climate Control Interface/ComfortHMI/` 唯讀實測：

| 檔名 | bytes | mtime |
|---|---|---|
| `Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf` | **14,538,298** | 2025-02-25 02:47 |
| `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR25_Post_3A_CR29359_(Feb_24_2025).xlsx` | **74,545** | 2025-04-15 14:25 |

**移除由 Pei 執行**（客戶樹屬 Tier 3）。移除後本層唯讀量測清單與 bytes，
A-CF02 轉 RESOLVED 並載其重審條件。

夾內現有 7 個檔（另有 `.DS_Store`）：上列二檔、SR24 兩檔、
`Device Manager HMI Logic and Flow R1 SR24 Post 2A (March 13 2023).pdf`
（3,560,705 bytes）、`FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx`
（144,163 bytes）。
**`Device Manager` 一檔非本 feature 之素材** —— 本層未動、未判，僅回報其存在。

---

## 6. 應複製至交付夾之清單（79 §2.3）—— **由 Pei 執行複製**

四項齊備前不得複製（79 §2.1）；現第 2 項未過，故本清單為預備。

| # | 來源 | 目的 | 現況 |
|---|---|---|---|
| 1 | `output/…_SWQT_Comfort_<ENTRY 023 之檔名>.xlsx` | 交付夾 | **尚不存在**（寫回未執行）|
| 2 | `docs/Comfort_HMI_delivery_note.md` | 交付夾 | 草案已備，**待分析層覆核** |
| 3 | `Comfort HMI Logic and Flow R1 SR24 Post 3A CR24879 (September 25 2023).pdf` | 交付夾 | **已在夾內**（6,462,311 bytes），不需複製 |
| 4 | `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023).xlsx` | 交付夾 | **已在夾內**（70,040 bytes），不需複製 |
| 5 | `FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx` | 交付夾 | **已在夾內**（144,163 bytes），不需複製 |

**實需複製者僅 1 與 2**；3–5 已在位。另需 Pei **移除** §5 之 SR25 兩檔。

---

## 7. 待裁定

1. **§2 之二擇一**：Pei 修 AF 後重驗，或裁定 AF 不在前置條件內。
2. 交付說明之檔名與覆核（§4）。
3. §5 之 `Device Manager` 一檔是否應在本 feature 之交付夾內 —— 本層無判斷依據。

**未做**：未複製任何檔案至交付夾；未移除任何檔案；未改 prepared 檔；
未登 ENTRY 022／023；git 未執行。
