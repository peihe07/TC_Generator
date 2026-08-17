# 57 — Comfort HMI / 範本驗證通過（ENTRY 022）、最終寫回 14/14 PASS（ENTRY 023）

- 產出層：執行層｜2026-08-16｜對象：分析層／Pei
- 覆核對象：`docs/handoff/78_final_writeback_prep.md`、`79_delivery.md`
- **結論：78 §2 四項全 PASS，78 §3 之 assertion **14 項全數 PASS —— 自 ENTRY 004 起首次**。交付阻塞解除，餘待 Pei 之 Excel 四項確認。**

---

## 1. 範本驗證（78 §2）—— 四項全 PASS，登 ENTRY 022

對象：`…_Comfort_20260816_prepared_ext.xlsx`，**123,717 bytes**，
SHA256 `6d53056e559bd0c13d26d38f16754536ede0230a5ce69c8596cce8e8b28b9d4c`

| 項 | 擴充前 | 擴充後（實測）| 判定 |
|---|---|---|---|
| B 編號公式 | row 10–59 | **row 10–601** | PASS |
| R design_method（x14）| `R10` ＋ `R11:R59` | **`R10:R601`** | PASS |
| P priority | `P10:Q11` | **`P10:Q601`** | PASS |
| T–Z | `T10:Z11` | **`T10:Z601`** | PASS |
| **AF** | `AF10:AF11` | **`AF10:AF601`（單一連續範圍）** | **PASS** |

**AF 之複驗**：row 10–500 之 491 列**全部受涵蓋，未涵蓋 0 列**
（上一版為 12 段離散 sqref、涵蓋 20 列、未涵蓋 471 列）。

其餘三項沿用上輪之方法：

- **B 欄抽格**：`B60`／`B200`／`B438`／`B500`（另加 `B10`／`B59`／`B501`）
  逐格 `dtype='f'`，值為 `=IF(ISBLANK($Dn),"",ROW()-9)` —— 是公式非值
- **zip member 48 = 48**；位元組層面 15 個 member 差異（Excel 另存必然重寫之
  共用部件）。**內容層面：全 9 個工作表 × row 1–601 × col 1–39 逐格比對，
  差異 542 格，`col == 2` 之單一欄，row 60–601**（601−60+1 = 542，數字自證），
  **其餘 0 格**
- **R 欄九項**：x14 公式為 `下拉選單!$A$1:$A$9`，該九格內容逐字元相符，
  `A10`／`A11` 為空

**已登 `DELIVERY.sha256` ENTRY 022（`type: template-extension`）**，
含 AF 之中間態記錄（首版看似已擴充而實際只涵蓋 20 列）。

---

## 2. 最終寫回（78 §3）—— ENTRY 023

- 來源：**ENTRY 022 之新母本**（`6d53056e…`）。`write_back.py` 之 `SRC`／
  `SRC_SHA` 與前置 gate 之名稱同步改指新母本；
  `…_20260815_prepared.xlsx` **未動**，仍為 ENTRY 001 之對象
- 產出：**`…_SWQT_Comfort_20260816.xlsx`**
  SHA256 `c37e572f63250bc144e65ed86b57bca3cc4ca48bbf333295c4d21cf016588b75`
- row 10–438，**429 列**（語料未增減，與 ENTRY 021 同一批 TC）
- 48 zip members，僅 `sheet6.xml` 差異；DV counts 與來源相同

### 2.1 前置 gate 6 項全 PASS

`BASELINE` 8 OK／`DELIVERY` 44 OK 0 FAILED／台帳無 ENTRY 023／
來源 hash 相符／lint **54 / 54 PASS across 429 TCs**／tc_id 001–429 連續無缺號

### 2.2 assertion **14 / 14 PASS**

**自 ENTRY 004 起固定 FAIL 之三項，本次全部轉 PASS**：

| 項 | ENTRY 021（前）| **ENTRY 023（今）** |
|---|---|---|
| B 欄公式 row 10–450 逐列原樣存在 | FAIL（row 60–450 為 `None`，391 列）| **PASS** |
| 每一寫入列在 R 欄 x14 DV 內 | FAIL（379 列在外；DV 止於 row 59）| **PASS**（0 列在外；DV covers 10–601）|
| 每一寫入列在 P 欄 DV 內 | FAIL（427 列在外；DV 止於 row 11）| **PASS**（0 列在外；DV covers 10–601）|

其餘 11 項照舊 PASS，含第 14 項（J 欄行號自 1 起連續）與 N 欄 429 格逐字元。

**此三項自 2026-08-15 之第二次寫回起 FAIL 至今，歷 19 次寫回。
其成因自始即為範本容量而非內容缺陷 —— 這一點在 ENTRY 004 當時是判斷，
今日才是實測：同一份 TC 資料、同一支寫入路徑，只換母本即全數轉 PASS。**

---

## 3. 三項久懸量測（78 §3.3）—— 於最終產出上實測

| 項 | 實測 |
|---|---|
| **P 欄允許集合** | 429 列之值 `P1` 296／`P2` 124／`P3` 9；**落在 {P0,P1,P2,P3} 之外者 0 列** |
| **A-CF19 內容側** | N 欄 429 格與 JSON **逐字元比對，不符 0 格**；最長 **600 字元**（`NR1L-ComfortHMI-323`）；多節 spec_ref **416 條**（97%）|
| **A-CF16 呈現側** | AH 欄寬 11.83、列高 14.0 → 可見約 **11 字元**；五列 marker row 首行實見 `[BLOCKED-SP`（010／012／382／383）與 `[BLOCKED-NO`（081），**`Owner:` 不可見** |

**P 欄一項之意義**：78 §3.3 稱其「427 列自寫入以來從未受下拉約束」。
**實測結果是 429 列全部合格。它一直是對的，但這是第一次被證明** ——
此前其正確性只由 generator 之常數保證，未經 Excel 之驗證層。

**A-CF16 之處置**：列高屬呈現，程式不得自改（26 §2）。故不改列高，
改於交付說明中以「搜尋 Remarks 欄之 `[BLOCKED`」指路 —— **可讀性之缺口
以尋找方式繞過，而非以改動交付件繞過。**

---

## 4. 帳目同步

| 檔 | 變更 |
|---|---|
| `DELIVERY.sha256` | 追加 **ENTRY 022**（template-extension）與 **ENTRY 023**（produced）|
| `output/STATUS.md` | 增二列；023 標「**未經 Excel 確認**」而非「不可交付」|
| `docs/INDEX.md` | 台帳摘要改述至 023 |
| `DATA_REQUESTS.md` #35 | **轉 RESOLVED**，載其解除依據與 AF 之中間態 |
| `ANOMALIES.md` A-CF26 | **Comfort 側 RESOLVED**，**跨 feature 之本體仍 OPEN** —— 修的是本 feature 這一份副本，**通用空白範本 `SWQT_20260121` 本身未變**，privacy 已交付之 9 列與日後各 feature 仍受影響（DR #36）。**一份被修好的副本不會使原件變好** |

---

## 5. 交付前之現況（79 §2.1 之四項）

| # | 前置 | 狀態 |
|---|---|---|
| 1 | 範本擴充（Pei）| **完成** |
| 2 | ENTRY 022 之範本驗證 | **通過** |
| 3 | ENTRY 023 之寫回，14 項全 PASS | **通過** |
| 4 | **Pei 之 Excel 四項確認** | **待辦** —— 無修復提示／R 欄下拉九項可用／D5 Scope 正確／row 10–438 內容與編號正確 |

**第 4 項未完成前不得複製任何檔案至交付夾。本層未複製、未移除任何檔案。**

---

## 6. 交付說明草案（79 §2.2）—— 待覆核

`docs/Comfort_HMI_delivery_note.md`（結構與紀律自查見上繳 56 §4）。
**其中一項訂正重述**：79 §2.2 寫「26 個 leaf 不產任何列」，
**實數為 25** —— `SWE1-HVAC-047` 有列（`NR1L-ComfortHMI-070`，可用側已測），
缺的是不可用側，屬部分涵蓋而非零涵蓋；403 − 378 = 25。

---

## 7. 待 Pei／待裁定

1. **Excel 四項確認**（79 §2.1 第 4 項）—— 交付之唯一剩餘前置
2. **SR25 兩檔之移除**（79 §3）：
   `Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf`
   （**14,538,298 bytes**）與
   `SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR25_Post_3A_CR29359_(Feb_24_2025).xlsx`
   （**74,545 bytes**）。移除後本層唯讀驗證並將 A-CF02 轉 RESOLVED
3. **複製清單**（79 §2.3）：實需複製者 **2 項** ——
   `output/…_SWQT_Comfort_20260816.xlsx` 與交付說明；
   SR24 兩檔（6,462,311／70,040 bytes）與 037 報告（144,163 bytes）**已在夾內**
4. 交付說明之覆核與檔名確認
5. 夾內 `Device Manager HMI Logic and Flow R1 SR24 Post 2A (March 13 2023).pdf`
   （3,560,705 bytes）非本 feature 素材 —— 本層未動、未判

**未做**：未複製／未移除任何檔案；未改 prepared 檔與 ext 母本；
未改 ENTRY 001–022 之內容；git 未執行。
