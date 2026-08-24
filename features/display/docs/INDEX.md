# INDEX — FW036 Display

執行層於每次上繳時更新（canon §8.7）。分析層不寫此檔。

feature 之交付夾為 `10_Reviewing/00_TestCase/ASW-R2/Display/`（R-DM9），
四份素材皆取自該目錄；身分為 `Display`、`test_group` 為 `Display`（R-DM1）。
037 之模組名 `Display Management` 與 CFTS_020 之文件名 `ICS and DCSD`
皆不進入任何 TC 欄位（R-DM1）。

| NN | 日期 | 主題 | 下放 | 上繳 | 新條文 | 新 anomaly | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-24 | 開案：Phase 0 intake + Phase 1 recon | [handoff/01_intake_recon.md](handoff/01_intake_recon.md) | （併入 02 上繳） | R-DM1–R-DM8（分析層自裁 8 條） | （未及登記） | **步驟 1 即停：`_intake/Display/` 不存在、037 未就位；停止條件 8 觸發。另查出 R-DM2 之前提「磁碟上無 037」為誤** |
| 02 | 2026-08-24 | 素材來源更正，續跑 01 步驟 1–14 | [handoff/02_source_correction.md](handoff/02_source_correction.md) | [upstream/02_intake_recon.md](upstream/02_intake_recon.md) | R-DM2 廢止、R-DM2′、R-DM9–R-DM11（逐字抄錄 13/13 相符） | A-DM1–A-DM11；DR-DM1–DR-DM3 開立 | **步驟 1–14 全數執行；九條停止條件全未觸發。`recon.py` 依 R-DM5(b) 預期失敗，未修腳本 → RECON.md／recon.json 未產出** |

## 02 輪要點

**相符者（執行層獨立重算 vs 下放包對照值）**
- 037 三分頁資料列 8 / 8 / 8，`SWE-DM-\d{3}` 8/8，`SYS-DISP-\d{3}` 8/8，
  `Categorization` 全為 `Functional Requirement`，`Source NRL ID(s)` 空 8/8
- SYS2 資料列 333、`SYS-RA-DM-*` 87、`SYS2-RA-*` 246、含 `DISP` 者 0、
  `Grouping` 全空 333/333
- Category × id 區段交叉表（正規化後）44/36、22/23、14/71、7/116 —— 逐格相符
- 大小寫變體 8 列，列號 r314 與 r23/24/25/27/64/70/81 —— 逐列相符
- Melco ID 8/8 命中（R-DM4 複驗成立）
- 037 之 A/B 兩檔：唯讀 `max_row` 差異確為量測條件差異（見上繳 §16）

**不符或新發現者**
- 037 表頭含不規則空白（A-DM5）
- R-G1 母本之分頁名與 3 個欄位與 scaffold 模板不符（A-DM7）
- SYS2 無指向 CFTS 條號之錨（A-DM10）
- 覆蓋落差：80 列母體 58 列無對應（A-DM11）
