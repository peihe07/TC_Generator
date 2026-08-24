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
| 03 | 2026-08-24 | 上繳 02 覆核；覆蓋對照退回重做（錨定法） | [handoff/03_coverage_redo.md](handoff/03_coverage_redo.md) | [upstream/03_coverage_redo.md](upstream/03_coverage_redo.md) | R-DM12–R-DM15（逐字抄錄 4/4 相符，累計 17/17） | A-DM12／A-DM13 新增；**A-DM11 結論撤回並改寫**；A-DM5 適用範圍擴及 036；DR-DM4 開立 | **步驟 1–10 全數執行；十條停止條件全未觸發。舊覆蓋表依 R-TM13 加註保留為 `…RETRACTED.tsv`** |

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

## 03 輪要點

**撤回者**
- 「80 列中 58 列無對應」「004/005/007 命中 0 列」—— bag-of-words 方法由
  R-DM13 廢止，該方法對 r31–r34 同時產生偽陽性與偽陰性

**錨定法之結果（逐字錨，R-DM13）**
- anchor_kind：signal 43／heading 36／value 1／melco 0／none 0
- `candidate_leaf`：僅 `SWE-DM-004`／`005` 各 4 列（r31–r34），依據為
  heading 錨逐字含 `'Hot Algorithm'`；其餘 76 列無候選
- 唯一站得住之覆蓋陳述仍是「以 id 為據之對應 0 列」（A-DM2）

**錨定法自身之兩項限制（本輪實測，須併同引用）**
- heading 錨在 `r72 2.2 Serializer Touch Interrupt PIN Definition` 退化：
  48/80 個 FR（60%）掛於該單一節點
- `RVC` → `Rear Camera` 之展開不逐字，故 SWE-DM-007／008 候選為 0 ——
  是方法之界線，非「SYS2 無 RVC 需求」

**R-DM8 再判定**
- 004 單級門檻、005 回復條件 → **不缺**（CFTS `{4820289}`／`{4820290}`／
  `{4820287}`／`{4820288}`）
- 005 之 multi-stage critical 判準 → **仍缺**，轉指 `{CFTS013-952}` → DR-DM4
- SYS2 r31–r34 經逐字比對為 CFTS `1.11.2.2` 之 HU 側子集，非另一組需求

**新查明之工作簿事實**
- 036 母本 B 欄為公式欄（1402/1402），且其 `data_only` 快取為陳舊值
- 036 母本表頭之分隔符為換行，33 欄皆然（A-DM5 適用範圍擴大）
- CFTS_020 引用 8 份外部 CFTS 文件（A-DM13）
