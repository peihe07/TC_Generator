# 66 下放包 — 貼回（write-back）之程序

分析層寫入，2026-08-23。**交付母本已定位；本包為貼回之完整程序。**

---

## 1. 交付母本

```
/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/
  Vehicle Settings/CFTS044/
  FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case
  Specification & Result_SWQT_CFTS044_Vehicle Controls_20260819.xlsx
```

與 `features/vehicle_setting/inputs/` 之同名檔為同一份（00 輪之進場副本）。
**目標分頁**：`Test Case Specification 測試用例規範`
**表頭列 9，資料列 10 起。** 現有 237 列為 037 之機械投影，
**依 R-VS1 效力等同 BLANK，全欄重生、append from first data row。**

---

## 2. 貼回前之三道 gate（**缺一不得貼**）

| # | Gate | 現況 |
|---|---|---|
| **G1** | **pilot 覆核** —— 129 條中 **28 條**（pilot #3 13 ＋ pilot #4 15）未經人工關卡；**43 條**未入任何 pilot | ❌ **未過** |
| **G2** | **交付揭露** —— `docs/reports/delivery_disclosure.md`（21 條畫面層 PENDING）須隨交付一併提出 | ✅ 已備 |
| **G3** | **母本備份 ＋ sha256** —— 貼回為不可逆，**貼前之母本須留一份帶雜湊之副本** | ❌ 未做 |

**G1 是實質 gate**：貼回後若 pilot 發現形態層缺陷（如 pilot #1 之三項），
其修正須在**已交付之工作簿上**做，代價遠高於在 JSON 上做。

**分析層建議**：先過 pilot #3＋#4 之 28 條合併覆核，再貼回。

---

## 3. 欄位對映（JSON 十鍵 → 036 欄）

| 036 欄 | 表頭 | 來源 |
|---|---|---|
| **B** | `No.#` | 流水號，自 1 起 |
| **C** | `Requirement or Design` | 037 之 `Requirement Title`（H 欄之來源同） |
| **D** | `Requirement or Design ID` | **`swe_id`**（如 `SWE1-VC-LeftFrontHeatedSeat-004`） |
| E | `Test Case ID (TestRail)` | **空**（TestRail 匯入後回填） |
| **F** | `Test Case ID` | `{project}-{abbr}-{NNN}`，**由生成器指派**（§10.3） |
| **G** | `Test Group` | `Vehicle Setting`（R-VS3′，全表同值） |
| **H** | `Test Set` | 四值之一（R-VS4） |
| **I** | `Test Item` | `tc_title` —— **上半段 037 逐字 ＋ 空行 ＋ 下半段括號內**（R-VS6） |
| **J** | `Pre-Conditions` | `pre_conditions` |
| **K** | `Input Test Data` | **一律 `NA`**（R-VS5） |
| **L** | `Test procedure` | `test_procedure` |
| **M** | `Expected Result` | `expected_result` |
| **N** | `Specification Reference` | `specification_reference` —— **一個 `CFTS044-{7位數}` 一行，禁 `,`／`;` 串接**（R-VS41(3)） |
| O | `Test Case Reference ID` | 空 |
| **P** | `Test Case Priority` | `priority`（R-VS56：P0／P1／P2，**不用 P3**） |
| Q | `Estimated Test Time (mins)` | 空（交付本亦多為空） |
| **R** | `Test Case Design` | `design_method` —— **受控 9 值之 `中文 (English)` 形態**（R-VS52 之對齊） |
| S | `Functional Safety` | 空 |
| T–Z | 車型欄 | 空（交付本以 `HDCC27`／`DT27` 等標，本 feature 未裁） |
| **AA** | `Test Case Author` | Pei 之姓名 |
| AB–AG | 測試結果欄 | **空**（執行階段填） |
| **AH** | `Remarks` | **`BLOCKED: DR-{n}` ＋ 待補來源**（畫面層 PENDING 者，21 條） |

**`reasoning` 不入工作簿** —— 其為審計欄，留於 `generated/*.json`。

---

## 4. 步驟

```bash
# 0) 備份 ＋ 雜湊（G3）
cd "/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Vehicle Settings/CFTS044"
cp "FM-WI-FSM-036-A01 …_CFTS044_Vehicle Controls_20260819.xlsx" \
   "REF/036_pre_writeback_$(date +%Y%m%d).xlsx"
shasum -a 256 "FM-WI-FSM-036-A01 …_20260819.xlsx" \
   "REF/036_pre_writeback_$(date +%Y%m%d).xlsx"
```

**1)** 執行層寫 `scripts/writeback_036.py`（**現無此腳本**），其要求：

- 以 `openpyxl` 開母本，**`keep_vba=False`／保留格式**
- **只寫 §3 表所列之欄**；其餘欄一格不動
- **不新增、不刪除分頁**；不動列 1–9
- 自列 10 起 append，**先清空現有 237 列之 B–AH**（R-VS1 全欄重生）
- 寫入前 **dry-run**：輸出將寫入之列數、每欄之非空數，與 129 逐項對照
- 寫入後 **重讀驗證**：逐列比對 JSON 與工作簿之十欄，**不符即中止並還原**

**2)** dry-run 之結果交 Pei 核可後，方執行實寫。

**3)** 實寫後：

```bash
shasum -a 256 "FM-WI-FSM-036-A01 …_20260819.xlsx"   # 記入交付紀錄
```

---

## 5. 貼回之範圍 —— **129 / 237，非全量**

| 項 | 數 |
|---|---:|
| 已生成 TC | **129** |
| 母體 Functional leaf | 237 |
| 未生成 | **108** |

**其中 21 條之畫面層為 `PENDING`**（AH 欄標 BLOCKED）。

**分析層建議**：貼回時**同時提交**下列三份，使覆蓋論述完整：

1. `docs/reports/delivery_disclosure.md` —— 21 條畫面層 PENDING 之逐條清單
2. `docs/reports/writability.tsv` —— 108 條未生成者之逐 leaf 阻塞歸屬
3. `DATA_REQUESTS.md` —— 十一份未結 DR 及其解鎖量

**沒有第 2、3 份，客戶會問「其餘 108 條為何沒有」而我方只能口頭答。**

---

## 6. 待 Pei

| # | 事項 |
|---|---|
| **1** | **G1**：pilot #3＋#4 之 28 條合併覆核 —— 分析層次包出建議分類 |
| **2** | **G3**：母本備份 ＋ 雜湊（§4 之步驟 0） |
| **3** | 授權執行層寫 `writeback_036.py` 並跑 **dry-run**（實寫仍待你核可） |
| **4** | DR-25′（23）／DR-19（7）／DR-15′ 補送 —— **池 16，兩輪見底** |

---

## 7. 本包產生之新條文清單（自檢）

無新條文。本包為程序文件。
