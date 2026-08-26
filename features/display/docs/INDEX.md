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
| 04 | 2026-08-24 | 參考素材庫（`forms/`）建置；訊號三段解析鏈 | [handoff/04_reference_store.md](handoff/04_reference_store.md) | [upstream/04_reference_store.md](upstream/04_reference_store.md) | R-G12–R-G14（全域，抄入 `docs/fw036/RULINGS_LEDGER.md`）＋ R-DM16／R-DM17（逐字抄錄 5/5，Display 累計 19/19） | A-DM14／A-DM15／A-DM16 新增；**A-DM10 拆為 a（RESOLVED）／b（PENDING）**；A-DM11 之 `[value]` 數字更正；DR-DM5 開立 | **步驟 1–12 全數執行；十三條停止條件全未觸發。`.gitignore` 加一行否定使 `LOOKUP_MISSES.md` 可 tracked** |
| 05 | 2026-08-24 | `[VALUE]` 定義定案、PROXI 開工、DBC 適用性 | [handoff/05_proxi_and_values.md](handoff/05_proxi_and_values.md) | [upstream/05_proxi_and_values.md](upstream/05_proxi_and_values.md) | R-DM18–R-DM21 ＋ R-G15（全域）（逐字抄錄 5/5，Display 累計 23/23） | A-DM17 新增；A-DM16 結案並記執行結果；A-DM11 之值 token 定案；DR-DM6 開立；LOOKUP_MISSES M-3 | **步驟 1–9 全數執行；十五條停止條件全未觸發。59 vs 44 已調和：擷取無誤，錯在聚合** |
| 06 | 2026-08-25 | 縮寫錨定案、聚合缺陷通則、037 精讀、Polarion 分頁清償 | [handoff/06_glossary_anchor.md](handoff/06_glossary_anchor.md) | [upstream/06_glossary_anchor.md](upstream/06_glossary_anchor.md) | R-DM22／R-DM23 ＋ R-G16／R-G13 補充（全域）（逐字抄錄 4/4，Display 累計 25/25） | A-DM18／A-DM19／A-DM20 新增；**A-DM4 升級（`_polarion` 字典）**；DR-DM7 開立 | **步驟 1–10 全數執行；十七條停止條件全未觸發。積欠四輪之步驟 8、9 一併清償** |
| 07 | 2026-08-25 | Q5 定案 B、錨優先序、分隔符正規化；**首次授權改 `scripts/intake.py`** | [handoff/07_pipeline_and_anchors.md](handoff/07_pipeline_and_anchors.md) | [upstream/07_pipeline_and_anchors.md](upstream/07_pipeline_and_anchors.md) | R-DM24–R-DM27 ＋ R-G17（全域）（逐字抄錄 5/5，Display 累計 29/29） | A-DM21／A-DM22 新增；A-DM4 之 `_polarion` 待辦結案；DR-DM8 開立 | **步驟 1–11 全數執行；二十條停止條件全未觸發。回歸 14/14 逐字相同；`recon.py` 仍失敗於同一點，成因已定位（A-DM21）** |
| 08 | 2026-08-25 | Q5-B 誤診歸屬、警示分支實測、正規化回施 | [handoff/08_recon_and_norm.md](handoff/08_recon_and_norm.md) | [upstream/08_recon_and_norm.md](upstream/08_recon_and_norm.md) | R-DM28／R-DM29 ＋ R-G18（全域）（逐字抄錄 3/3，Display 累計 31/31） | A-DM23 新增 | **步驟 1、2、4–7 執行；步驟 3（選項 D）待 Pei 裁示未做。二十二條停止條件全未觸發** |
| 09 | 2026-08-25 | 選項 D 執行、sidecar 化、ETM 判準否定 | [handoff/09_recon_crosscheck.md](handoff/09_recon_crosscheck.md) | [upstream/09_recon_crosscheck.md](upstream/09_recon_crosscheck.md) | R-DM30／R-DM31 ＋ R-G19／R-G20（全域）（逐字抄錄 4/4，Display 累計 33/33） | A-DM24（自查，RESOLVED）／A-DM25 新增 | **步驟 1–4、6 執行；步驟 5 觸發停止條件 25 已停。`recon.py` 七輪來首次跑通，回歸 11/12 相同** |
| 10 | 2026-08-25 | 交叉檢查結案、DECISIONS 合併、PROXI 改需求驅動 | [handoff/10_decisions_merge.md](handoff/10_decisions_merge.md) | [upstream/10_decisions_merge.md](upstream/10_decisions_merge.md) | R-DM32–R-DM34 ＋ R-G21／R-G22（全域）（逐字抄錄 5/5，Display 累計 36/36） | A-DM26 新增 | **步驟 1–7 全數執行；二十七條停止條件全未觸發。Q2／Q3 材料已備，`docs/proxi_triage_proposal.md` SUPERSEDED** |
| 11 | 2026-08-25 | 綁定檢查、合併複驗、待裁期間之不阻塞工作 | [handoff/11_binding_verify.md](handoff/11_binding_verify.md) | [upstream/11_binding_verify.md](upstream/11_binding_verify.md) | R-DM35 ＋ R-G23（全域）（逐字抄錄 2/2，Display 累計 37/37） | （無新 A-DM） | **⚠ 步驟 3 觸發停止條件 29：合併漏了 3 項，已停於待裁。步驟 1、2、4–6 完成** |
| 12 | 2026-08-25 | marker 衝突裁定、已裁常數改為機器檢查 | [handoff/12_assertions.md](handoff/12_assertions.md) | [upstream/12_assertions.md](upstream/12_assertions.md) | R-DM36／R-DM37 ＋ R-G24（全域）（逐字抄錄 3/3，Display 累計 39/39） | A-DM27／A-DM28 新增 | **步驟 1–8 全數執行；三十二條停止條件全未觸發。三項分歧已處置，複驗 24/24 有對應** |
| 13 | 2026-08-25 | 會說謊的警示補測、綁定範圍收束、不阻塞工作見底 | [handoff/13_honest_guards.md](handoff/13_honest_guards.md) | [upstream/13_honest_guards.md](upstream/13_honest_guards.md) | R-DM38／R-DM39 ＋ R-G25（全域）（逐字抄錄 3/3，Display 累計 41/41） | A-DM29／A-DM30 新增（皆自查）；A-DM27 更正 | **⚠ 步驟 3 觸發停止條件 34（1 項不符）。步驟 1、2、4、5、6 完成。綁定 9/9** |
| 19 | 2026-08-25 | **合併包**：14–18 撤回重排；裁定落地、framework、簽核、pilot-01 | [handoff/19_consolidated.md](handoff/19_consolidated.md) | [upstream/19_consolidated.md](upstream/19_consolidated.md) | R-DM40–46（7 條）＋ R-G26–31（6 條，全域）＋ R-G32（逐條 12/12 PASS，Display 累計 48/48） | A-DM31／A-DM32 新增 | **⚠ 步驟 13 觸發停止條件 46（值無出處），未產出 TC。步驟 1–12、15 完成；簽核已轉錄，Phase 4 解封** |
| 20 | 2026-08-25 | A-DM32 裁定（R-DM48）；**pilot-01 三條 TC 產出** | [handoff/20_pilot01_tc.md](handoff/20_pilot01_tc.md) | [upstream/20_pilot01_tc.md](upstream/20_pilot01_tc.md) | R-DM47／R-DM48（逐條 2/2 PASS，Display 累計 50/50） | DR-DM9 開立；A-DM32 標已裁 | **步驟 1–6 全數執行；五十二條停止條件全未觸發。lint036 二十項行計皆 0** |
| 21 | 2026-08-25 | pilot-01 覆核：四項退回、負向補列 | [handoff/21_pilot01_rev2.md](handoff/21_pilot01_rev2.md) | [upstream/21_pilot01_rev2.md](upstream/21_pilot01_rev2.md) | （無新條文） | A-DM33 新增；DR-DM10 開立 | **步驟 1–7 全數執行；五十五條停止條件全未觸發。rev2 三條，lint 二十項行計 0** |
| 22 | 2026-08-25 | #1 亦受 A-DM33 波及：popup 側分離 deferred | [handoff/22_pilot01_rev3.md](handoff/22_pilot01_rev3.md) | [upstream/22_pilot01_rev3.md](upstream/22_pilot01_rev3.md) | R-DM49 | A-DM34 新增；DR-DM10 阻斷範圍擴至 004 | **步驟 1–6 全數執行；五十八條停止條件全未觸發。rev3 三條，lint 二十項行計 0；寫回前兩項閘皆 PASS** |
| 23 | 2026-08-25 | pilot-01 收束、揭露義務入條 | [handoff/23_pilot01_closeout.md](handoff/23_pilot01_closeout.md) | [upstream/23_pilot01_closeout.md](upstream/23_pilot01_closeout.md) | R-G33（全域）；R-DM48 之補充 | A-DM34 複驗 PASS | **停止條件 59 觸發且處置完畢；rev4 三條，lint 二十項行計 0** |
| 24 | 2026-08-25 | CFTS013 SYSRA 之驗明（**檔未落磁碟，步驟 4／5／6 未執行**） | [handoff/24_cfts013.md](handoff/24_cfts013.md) | 併入 [upstream/25](upstream/25_disclosure_lifecycle.md) §五 | R-DM51／R-DM52 | A-DM31 敘述修正；DR-DM10(b) 改問法 | **停止條件 61／62 無從通過；R-DM51 拘束已生效（60 未觸發）** |
| 25 | 2026-08-25 | 揭露句之時效與 token 資料化 | [handoff/25_disclosure_lifecycle.md](handoff/25_disclosure_lifecycle.md) | [upstream/25_disclosure_lifecycle.md](upstream/25_disclosure_lifecycle.md) | R-G34／R-G33(d)（全域）；R-DM53 | B11 結案；B12／B13／A6 新增 | **MISSING 0／STALE 0；R-DM 區塊 55，順序驗證 exit 0** |
| 26 ＋ 26a | 2026-08-25 | 機器抽取原則入條、A-DM35 補件、**STALE 實測失敗** | [handoff/26_extraction_principle.md](handoff/26_extraction_principle.md)、[26a](handoff/26a_materials_landed.md) | [upstream/26_extraction_principle.md](upstream/26_extraction_principle.md) | R-G35／R-G36（全域）；R-G25 適用註記 | A-DM35 補件；A-DM36 新增；A6 解除；A7／A8 新增 | **停止條件 66／67 皆觸發；24-4／24-5 未執行** |
| 27 | 2026-08-25 | A8 解除、STALE 乙案修畢、24-4／24-5 完成 | [handoff/27_stale_fix.md](handoff/27_stale_fix.md) | [upstream/27_stale_fix.md](upstream/27_stale_fix.md) | R-DM54；R-G16 口徑指標 | A-DM37 新增；A-DM35 結案；DR-DM9 重擬 | **停止條件全 70 條無一觸發；綁定 entries: 12／12 of 12；STALE 誘發測試報 1** |
| 28 | 2026-08-25 | CFTS_013 全文驗明、矩陣判讀、**rvc-01（007／008 六條）** | [handoff/28_cfts013_full_and_rvc.md](handoff/28_cfts013_full_and_rvc.md) | [upstream/28_cfts013_full_and_rvc.md](upstream/28_cfts013_full_and_rvc.md) | （無新條文） | A-DM38／A-DM39 新增；DR-DM11 開立；A9／A10、B17–B20 新增 | **停止條件 71 觸發（A3 停手）；rvc-01 六條，lint 20 項行計 0；綁定 entries: 13** |
| 28a | 2026-08-26 | 附件：A-DM36 結案、DR 十筆改 SENT、DR-DM7 對帳 | [handoff/28a_dr_sent.md](handoff/28a_dr_sent.md) | 併入 [upstream/28](upstream/28_cfts013_full_and_rvc.md) §三之二 | （無新條文） | A-DM36 CLOSED；A11／B21 新增 | **停止條件 74／75 皆未觸發；DR-DM7 判定為全案結案而非部分結案** |
| 29 | 2026-08-26 | A3 解封、DM2 降級、007／008 切分裁定 | [handoff/29_a3_and_arbitration.md](handoff/29_a3_and_arbitration.md) | [upstream/29_a3_and_arbitration.md](upstream/29_a3_and_arbitration.md) | R-DM55 | A-DM40 新增（CLOSED）；DR-DM12 開立；A12／B22／B23 新增；B20 解除 | **停止條件 76 觸發 —— CFTS_013 之 50 vs CFTS_020 之 85；未改任何 TC** |
| 30 ＋ 30a | 2026-08-26 | 追五個轉指條號；R-DM51 依據補驗；DR-DM7 結案 | [handoff/30_crossref_chase.md](handoff/30_crossref_chase.md)、[30a](handoff/30a_vf169.md) | [upstream/30_crossref_chase.md](upstream/30_crossref_chase.md) | R-G37（全域）；R-G27 指標 | A11 關閉；A13／B24／B25 新增；B23 解除；DR-DM7 CLOSED；A-DM20 改標 | **停止條件 79／80／81 皆未觸發；TC 一字未動** |
| 31 | 2026-08-26 | 讀 71 條漏網；自陳即驗入條 | [handoff/31_missed_clauses.md](handoff/31_missed_clauses.md) | [upstream/31_missed_clauses.md](upstream/31_missed_clauses.md) | R-G38（全域）；R-G22 指標 | A-DM33 母體加註；A14／B26／B27 新增；B24 解除 | **停止條件 84／85／86 皆未觸發；三項重測皆不變；TC 一字未動** |
| 32 | 2026-08-26 | 開第三批 `ops-01` 之勘查（**停止條件 87 觸發，未生成**） | [handoff/32_ops01.md](handoff/32_ops01.md) | [upstream/32_ops01.md](upstream/32_ops01.md) | （無新條文；PLAYBOOK §5a 慣例） | A-DM37 增列；A-DM33 加註複核；A15／A16／B28／B29 新增；B26 併入 | **T1b 適用條文 172 條 > 30 → 停手不生成** |
| 33 ＋ 34 | 2026-08-26 | `ops-01` 生成；**22 條寫回 036**；收尾 | [handoff/33_ops01_scoped.md](handoff/33_ops01_scoped.md)、[34](handoff/34_closeout.md) | [upstream/33](upstream/33_ops01_scoped.md)、[34](upstream/34_closeout.md) | R-G39（全域）；R-DM56／R-DM57 | B30–B33 入 BACKLOG（R-DM57(b)） | **lint 22 條全 0；完整性計數逐項相等；回讀 22×15 不符 0** |

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

## 04 輪要點

**相符者（執行層獨立重算 vs 下放包 §3.1／§3.2）**
- 四本 DBC 之訊號定義列／訊息數 344/63、1916/318、914/155、2037/323 逐項相符
- BHCAN2-R1 vs BHCAN-R4 訊號名三分 310／573／32 逐項相符
- 三個顯示訊號之 tx 節點差異逐項相符；位元定義與 `VAL_` 兩本逐字相同
- `CM_TCH_STAT` 於 BHCAN2 之 0 命中確為「本就不在該匯流排」（R-G13 教案）

**須加限定者**
- §3.4 之「15 個 `$Signal$` 全數解得」：LID 階段 15/15 成立，**DBC 階段
  14/15** —— `CCDMF_RQ_DISP_INTS` 之 CAN 名不在任一本 DBC（LOOKUP_MISSES M-1）
- R-DM16 之 regex 與其所載之「13」不一致：`[^\]]+` 實測 44（含 Polarion
  metadata），13 為 `[A-Za-z0-9_%\s]+` 之數。本輪兩者並列，未擇一

**新查明者**
- 三個顯示訊號之 **rx 節點亦隨 tx 對調**（下放包只列 tx）
- BHCAN2 之四個 FPDM 顯示訊號與 `DCSD_*` 為平行族（A-DM15）
- LID `Proxi & Configuration` 有 `DSP_SK_PRSNT`／`RVC_SK_PRSNT`／`DCSD_cfg`
  等組態旗標，形態上像 TC 前置條件來源（A-DM16，未解析）

## 05 輪要點

**調和 59 vs 44** —— 擷取兩次都是 59（正規化與否皆同）；44 是**聚合**造成的：
以逗號串進 TSV 再以逗號切回，而 token 本身可含逗號（`[Radio:R1M, VP5R120,
R1H]`）。分隔符已改為 ` ¦ `。

**`[VALUE]` 定案（R-DM18）**：寬式 59 → 扣除含 `:` 者 43 → 餘 16
（值 13 + 文件名 3），涉及 35 個 FR 列。與條文 §2.2 之表逐項相符。

**PROXI（R-DM20）**：446 列母體，`proxi_param` 176／`cfts_usage` 1／
`leaf_phrase` **0**／`none` 269。`DCSD_cfg`→PROXI r37、`RVC_SK_PRSNT`→r401+r494，
皆 `0=Absent 1=Present`；`DSP_SK_PRSNT` 查無 → M-3／DR-DM6。

**A-DM17（新）**：以 LID 名直接查 PROXI 只得 70/446，改用 `Atlantis Signal
Name` 後得 177/446 —— **漏 107 列**，與「以 `ICSPowerButton` 查 DBC」同型。

**LID v1.78 vs v1.76**：2,548 個 LID 中**僅 2 個**相異（`CallAction`、
`EngineRPM`），單側有 0。兩者皆未出現於任何已交付 TC，停止條件 15 未觸發。
本 feature 之 15 個訊號在兩版**全部相同**。

## 06 輪要點

**glossary（R-DM22）**：13 個縮寫查得並列，**無一衝突**（停止條件 16 未觸發）。
`SK`／`TGW`／`SGW`／`ETM` 查無並列，依條文不建條目。

**錨之效果相反（A-DM19）**：SYS2 側 `SWE-DM-007`／`008` 候選 0 → **各 12**；
PROXI 側**仍為 0** —— 阻塞點是底線 vs 空格（`Rear_View_Camera`），
非縮寫，R-DM22(c) 禁止再放寬。

**037 精讀（A-DM18，積欠四輪）**：八條全部 —— 數值+單位 0、`$Signal$` 0、
外部引用 0、句號後併句 8/8。R-DM8 之缺值清單實為八條全無具體值，非四處。

**`_polarion` 分頁（積欠四輪）**：是欄位合法值字典。`Category` 合法值五個，
而 **117/333 列（35%）之實際值不在字典中**，且違規的是多數拼法
（`Out of Scope` 116 列）。A-DM4 由此升級並取得逐字權威。
另證實 `Non Functional Requirement` 合法但 0 列 —— R-DM7 母體未遺漏 NFR。

**R-G16 複查**：六支寫檔腳本之逗號串接全改 ` ¦ `；六份 TSV 之筆數
（80／446／26／45／13／2548）修正前後**完全一致**，還原檢查通過，
停止條件 17 未觸發。

**PROXI NODE 欄（A-DM20）**：`Checked by` 6/1058 不可用；`Used by` 500/1058
結構可用但**缺本專案之 VF 代碼**這把鑰匙 → DR-DM7。

## 07 輪要點

**`intake.py` 覆寫機制（R-DM24）**：`SHEET_SIGNATURES` 逐字未動；
缺省惰性經 14 個目錄、82 個檔之回歸驗證，**全部逐字相同**。
（`_intake/` 多數目錄已被歷次 scaffold 搬空，故另以各 feature 之
`inputs/` 建 8 個 `_regr_*` 臨時語料，使回歸真正有覆蓋。）

**Q5-B 未達其目的（A-DM21）**：`"Analysis Report"` 寫死於 **5 處**，
Q5-B 只繞過其中 1 處（`SHEET_SIGNATURES`）。條文所載之
`kind: a03_report` 不驅動下游（need list 仍報 NO requirement report）；
改為能驅動下游之 `kind: swra_report` 則 `intake.py` 崩於其自身
`cited_documents()` 之同一假設。`recon.py` 重跑仍失敗於 `recon.py:568`。

**錨優先序（R-DM26）**：調整後 `glossary_phrase` **仍為 0** ——
16 個產生候選之列**全部同時含 `$signal$`**，而 signal 居首。
`anchor_kind` 與 `candidate_from` 回答的是不同問題（A-DM22）。

**分隔符正規化（R-DM25）**：`RVC_SK_PRSNT` → PROXI r401／r494
（`0 = Absent 1 = Present`），標 `glossary_phrase_norm` ——
**本 feature 首次出現 leaf ↔ PROXI 之連結**。
停止條件 19 未觸發：PROXI 1,052 個參數名、LID 429＋2,548 個識別碼，
正規化後碰撞組**皆為 0**。

**R-DM27**：037 八條之缺值點逐條表入 `data/leaf_value_gaps.tsv`。

## 08 輪要點

**R-DM24(b) 警示分支實測（步驟 2）**：以 SYS2 檔冒名頂替 037 之檔名，
三項各自成立 —— 警示印出（含兩側雜湊前 16 碼）、signature 結果
`polarion_export` 保留、exit 0 不崩潰。另補測「缺 sha256」分支亦如預期。
狀態已還原並複驗（`ab3198e8…`，覆寫恢復生效）。

**正規化回施 SYS2（步驟 4）**：新增候選 **0**。**但我上輪的推測是錯的**
—— 80 列中 **66 列含底線**（40 個相異底線 token），不是「散文，底線少見」。
0 之真正原因：那些底線 token 是識別碼形態之訊號名，
`DISP_REAR_CAMERA` 正規化為 `DISP REAR CAMERA`，與 `Rear View Camera`
仍不等（少 `View`、多 `DISP` 前綴、大小寫不同）。

**`compare_req_families.py`（步驟 6）**：**無任何腳本或管線呼叫它**，
為手動 CLI 工具；唯一使用紀錄在 AMFM。其 `SHEET` 用法有 guard
（`sys.exit` 而非 `KeyError`），與 `recon.py:568`／`intake.py:311` 不同型。
Display 用不到它（它比較兩份同範圍需求報告，本 feature 只有一份）。

**A-DM23（新）**：我上輪加的 TSV `#` 註解行使 `csv.DictReader` 讀不到表頭，
且錯得像空資料而非報錯。

**步驟 3（選項 D）未執行** —— 待 Pei 裁示。

## 09 輪要點

**`recon.py` 跑通** —— 本 feature 首次取得獨立管線交叉檢查。
17 項可對照者中 **16 項相符**，1 項不符（spec text layer 字元數：
pymupdf 854,333 vs python-docx 907,382，兩數皆重現，**未擇一**）。
另 4 項為 recon 有而自寫腳本未測（ASIL/FTTI、版面 revision、
`estimated_test_time=Q`、id-suffix 判準）。

**選項 D 之改動實為四處非一處**（函式簽章／取分頁處／其錯誤訊息／
`main()` 之唯一呼叫處）。已如實回報，不主張四等於一。
回歸 12 個 feature：11 個逐字相同，僅 Display 改變。

**下放包 08 §2.3 之逐項表**首次實測：7 項中 6 項相符，
1 項「結果對而理由錯」（Display 其實**有** `sys1_export`）。

**停止條件 25 觸發**：ETM 判準鑑別力實測 **0.88x**（群內 8.0% 低於
群外 9.1%），第一梯次判準不成立，已停，未自行改判準。

**A-DM24（自查）**：我上輪排程提案有索引錯位（ETM 50→100）與
不成立之互斥宣稱（69+117+269 實為 455）。第六次同型缺陷，
但這次錯的是**我親手打在表下的一句斷言**，無程式在檢查它。

**R-DM30**：11 個 TSV 全部改為表頭起首 + `.tsv.meta.json` sidecar，
列數 11/11 未變。全 repo 82 個 TSV 中另有 15 個帶註解行（多在
`user_profiles`），**登記未代改**。

## 10 輪要點

**`DECISIONS.md` 合併完成**（R-DM32）。9 處分歧逐處留處置與理由；
最要緊者為 `spec_reference` **維持 `[PEI]`、拒絕降格為 `[PROPOSED]`**
（後者未經修改即生效，會使無法提案之項無聲通過）。
§1–§7 之項目行**無一未標記**（停止條件 26 未觸發）；原三項未標記者已補標。

**字元數定案**：登記 **854,333**（pymupdf／管線探針），自測之 907,382
並列保留於 `data/spec_text_layer.tsv`。兩者皆遠超 500 字元門檻，
**結論相同**。連帶登記 **A-DM26**：欄名 `spec_pdf` 而內容為 `.docx`。

**PROXI 改為需求驅動（R-DM33）**：`related_leaf` 全 446 列停止填寫，
語意一律標 (2)；錨仍照跑，結果留在 `note` 欄。
`docs/proxi_triage_proposal.md` **撤回**（原文依 R-TM13 保留並加註）。

**Q 欄／B 欄**：`feature.yaml` 已註記兩者皆「辨識但不寫入」，
理由不同（B 為公式欄 R-DM15；Q 為版面標記 R-DM34(a)）。

**Q2／Q3 材料已備**：`docs/Q2_Q3_briefing.md`。Q2 由「暫緩」改為
`[PEI]` 可提交；Q5 標為已裁定（B）並註明其未達原目的。
briefing 末列 **6 項未涵蓋者**，逐項標「未查證／未量測」，不補推論。

## 11 輪要點

**⚠ 停止條件 29 觸發** —— 上輪之 `DECISIONS` 合併漏了三項，複驗查出：

| # | 項 | recon | 合併後之 `DECISIONS.md` |
|---|---|---|---|
| 1 | `ruled-constant assertions` | `[AUTO] 0 checked, 0 PASS, 0 FAIL` | **無此項** |
| 2 | `Test Set table (Part N)` | `[PEI]` | `[PROPOSED]` |
| 3 | `profile [OVERRIDE] clauses` | `[PEI]` | `[PROPOSED]` |

第 2、3 項之 `[PROPOSED]` 出自 `61d1c12`（02 輪），**早於 recon 首次執行**
—— 是合併未察覺之既存分歧，非合併時降格。三項皆**未自行修正**。

> 上輪 §8 第 2 項我自陳「合併這個動作本身沒有被交叉檢查」。
> 本輪一驗就查出三項 —— 該自陳不是形式話。

**R-G23 綁定檢查**：`verify_reference_binding.py` 四項 **4/4 相符**；
另測其失敗分支（蓄意改宣告值），確認印出兩值全碼、退出碼 1、
且**不改寫宣告值**。狀態已還原並複驗。

**`spec_text_layer.tsv` 改為腳本產出**（`probe_spec_mode.py`），
三數現算不再人工登記，列數 3→3 未變。

**`proxi_candidates.tsv` sidecar** 加入三份來源之 sha256（LID／PROXI／037），
使索引與其來源之綁定可見。

**`DECISIONS.new.md`** 依 R-DM35 加註地位；重跑之新舊兩份**逐字相同**，
舊者改名 `DECISIONS.new.2026-08-25a.md` 保留。

## 12 輪要點

**三項分歧處置完畢**：`ruled-constant assertions` 補入並填實；
`Test Set table`／`profile [OVERRIDE]` 依 **R-G24** 改為 `[PEI]`
（**機器是對的**，02 輪自填之 `[PROPOSED]` 是錯的）。
複驗：recon 之 24 項**全部有對應**，marker 不一致僅餘 `spec_reference`
一項，且該項為 R-DM32／R-G24 皆判取 `[PEI]` 之刻意結果。

**反向比對（停止條件 30 未觸發）**：17 項合併檔獨有者中，
**10 項是 recon 有測而未列入 `DECISIONS.new.md`**、7 項為自測獨有概念、
**recon 漏測 0 項**。由此立 **A-DM27**：`DECISIONS.new.md` 是 recon
量測之**子集**，此後對照一律兼看 `RECON.md` 與 `recon.json`。

**`recon_assertions` 宣告**（R-DM36）：`functional_requirement_count: 8`，
recon 重跑得 **PASS，0 failed / 1 checked**。PASS 證明的是「仍為 8」，
不是「8 是對的」。

**綁定**：036 母本納入 `reference:`（R-DM37），**5/5 相符**；
四支讀取素材之腳本已串接該檢查，蓄意破壞後實測 **退出碼 1、
stdout 0 行、TSV 未被改寫**。串接前後列數 4/4 未變。

**A-DM28（自查）**：漂移警示首版「說不採納卻採納了」——
連跑兩次第二次警示即消失。已修正並以連跑兩次驗證。
**第七次同型缺陷，但形態是新的：宣稱之行為與實際行為不一致。**

## 13 輪要點

**R-G25 補測三處，全數通過**：`verify_reference_binding.py` 之「不更新
宣告值」、`intake.py` 覆寫之兩條分支（sha 不符／缺 sha）。各連跑兩次、
訊息不變、標的（`feature.yaml`、該 xlsx）逐字未變。`intake.py` 一行未改。

**⚠ 停止條件 34 觸發**（步驟 3，R-DM39 之 10 項比對）：

| 判定 | 項數 |
|---|---|
| 值相符 | **8** |
| **不符** —— 兩側量的是不同的量 | **1**（`Missing referenced specs`） |
| **映射不成立**（上輪偽陽性） | **1**（`Header row index`） |

由此立 **A-DM29**：上輪之分類以**子字串比對**判斷「recon 有沒有測這個」，
而子字串會在無關句子裡命中（`"header"` 命中 `"from header text"`）——
**與 R-DM13 所禁之 bag-of-words 同型，我在判斷概念是否同一時用了非逐字
之方法**。A-DM27 之「10/7」更正為 **8/1/8**。

**A-DM30（自查）**：四個新 `reference:` 鍵曾靜默落入 `lint:` 之下 ——
YAML 解析無誤、檢查照常輸出 `5 of 5 match.`。**一個通過的檢查，
檢查的卻不是我以為的東西。** 修正後 **9/9**。`entries: N` 那一行是
唯一能察覺此錯的線索。

**綁定範圍**（R-DM38）：`inputs/` 四份納入，共 **9 項 9/9 相符**。
`feature.yaml` 加註 `paths:`（檔在哪）與 `reference:`（檔是哪一份）之分工。

**subprocess 成本**：守衛本身中位數 **0.04s**；佔比 0.9%（proxi）～
**46%（dbc_probe）**。絕對值小，但對快腳本幾乎等於加倍。

## 19 輪要點

**14–18 五包編號作廢**，其內容由 19 包之 15 步執行序取代。

**12 條逐條抄錄 12/12 PASS**（各自獨立比對，停止條件 49 未觸發）。

**裁定落地**：Q2 取 037 之 8 leaf（**R-DM41** —— 037 界定的不只「測什麼」，
還包含「要不要測」）；Q3 取 `SWE1-DM-{nnn}`（**R-DM42**）；
DR-DM8／DR-DM7 結案（**R-DM43／R-DM44**）；
`Safety attributes` 之依據由「查不到」改為「**查到了，答案是沒有**」
（**R-DM46**：SYS3 表 6 有 `ASIL Level`，31/31 為 `QM`，`SG ID`／`FSR ID` 全空）。

**簽核已轉錄**：實質 `[PEI]` 殘留 **0**（標記分布 AUTO 28／PROPOSED 12／
RULED 3）；`recon.py` 回 **REFUSED (R-C9)**，兩項複驗皆過。

**綁定 11/11**（Pop Up List 兩檔納入）。過程中查出 `paths:` 與
`reference:` 之**路徑基準不同**（feature 目錄 vs repo 根）——
首次宣告即令 recon 以 `input not found` 中止，依 `home` 之先例改置
`inputs/`。

**framework.md 落檔**：四組 Test Set 涵蓋 8 leaf，無重複無遺漏。

**⚠ 停止條件 46 觸發，未產出 TC**：18 §二.2 指定之值標籤
`DISP_OFF`／`DISP_NORMAL` **在 DBC 與 LID 皆不存在**（`DISP_HOT` 有，raw 4）。
規格側寫 `[DISP_OFF]`、訊號側為 `0 (OFF)`，兩者對應**非逐字**。
以 **A-DM32** 登記，並列三途提案，未裁定。

## 20 輪要點

**A-DM32 已裁（R-DM48）**：不採我所提之三途中任一，改為**按可得性分寫**
—— 逐字解得 DBC `VAL_` 者寫入訊號值，解不得者 ER 改驗規格所載之
**可觀察行為**。分析層之關鍵補充：**#2／#3 之阻塞不是缺值，
是 18 §2.2 指定了它們不需要的值**。

**pilot-01 三條 TC 已產出**（`generated/pilot-01.json`）：
004 × 1（Hot 門檻 → PU0517 警示，**含** `= 4 (DISP_HOT)`）、
005 × 2（保護性關閉 → PU0130／溫度回落 → 背光與觸控恢復，**皆不寫訊號值**）。

**`lint036.py --profile display`：A–N 及 P/Q/R/T/U 二十項行計皆 0。**
首跑 A 檢查 **4 處 FAIL**（`Observe`／`check whether` 為 §5.1 禁用動詞），
**該 FAIL 是我產出的缺陷不是判準問題**，改為 `Read`／`check that` 後歸零。

> lint 需 xlsx 而本輪禁寫回母本 —— 以 scratchpad 之**拋棄式副本**執行，
> 母本 SHA 前後複驗未變（`6372fb6be02f48dc…`）。

**R-DM47**：`paths:`（feature 目錄）與 `reference:`（repo 根）之路徑基準
不同，補 R-DM38 之未涵蓋處。

**DR-DM9 開立**（HIGH）：請上游確認四個規格值標籤各對應哪一個 raw；
取得後得於既有 ER **增列**訊號值，增列不改變行為驗證，**不構成回修**。

## 21 輪要點

**四項退回全數處置**：#2 deferred（§2.1）／欄位歸屬修正（§2.2）／
`{4820282}` 複驗後保留（§2.3）／邊界負向條補列（§2.4）。

**§2.1 之查證把搜尋面自一節擴到全文，結果改變了處置**：
warning 與 OFF 兩階段之區分準據，經**四條路徑**（組 A `{4820283}`／
組 B `{4820289}`／組 C `{4820951}`／Pop Up List `PU0130`）查證**皆不產生
可觀測之判準**。依分支 3 → #2 deferred、開 **DR-DM10**。與 DR-DM4 不併。

**A-DM33（新）**：`1.11.2.2` 之下有**兩組皆宣告適用於 `R1H`／`Atlantis High`
且互相排斥**之關閉流程 —— 組 A（HU 下令關背光、關後續送 `[DISP_HOT]`）
與組 B（DCSD 自主關背光並送 `[DISP_OFF]`、無警示階段）。
Multi-stage 之第三組**不構成第三個適用流程**（DCSD 側 `Radio:noSys`，
且該節自載不由 DCSD 供應商實作）。本批 TC 只取兩組皆一致之部分。

> 這是第二次「查得比預期多」而改變處置（第一次是 06 輪之 `_polarion`）。
> **兩次都是把搜尋面從指定的一節擴到全文才看見的。**
>
> 本輪之 A-DM33 初稿曾寫「三組皆適用」，逐條讀屬性行後改正；
> **結論不變而理由改變，依 R-G19 分別更正。**

**rev2 三條**：004 正向、004 邊界（`=85` 不觸發）、005 回復。
`input_test_data` 三條皆改 `NA`，門檻值移入 `pre_conditions` 之具體值。
`lint036.py` 二十項行計 0；母本 SHA 未變。

## 22 輪要點

**21 包只指出 #2，而 #1 掛在同一個矛盾上。** #1 原 ER 3 驗 `PU0517`
顯示十秒，其前提是越過門檻後顯示仍亮著；而組 B `{4820289}` 於越過門檻時
**即關背光** —— **一個看不見的 popup 顯示十秒，該 ER 不可觀測**，
#1 在組 B 之實作上恆為 False Fail。

> 我 21 包判「#3 不受影響」（正確）就收手，**沒有回頭檢 #1**。
> 兩者掛的是同一個矛盾，只是形態不同：#2 的問題在觸發條件（何時關），
> #1 的問題在**可觀測性**（關了就看不見）。**形態不同使我沒把它們歸為一類。**

**#1 收斂為訊號側**：ER 3／step 3 移除 → 2 步 2 ER；`tc_title` 改為
`Hot threshold exceeded → Hot state notified to HU`；括號下半明寫
`the warning popup is deferred`。`test_item` 上半**不動**（需求文依 §4.5 保留），
其與 ER 之落差以 §7.3 之覆蓋缺口表揭露 —— **004 為部分覆蓋，
交付時不得以「004 有 TC」表述**。

**R-DM49（新）**：負向條之 ER 為「不發生」時得自「觸發條件未成立」推得，
須 (a) 正向出處逐字存在、(b) 不引入新值、(c) 記明證據強度差異。
**其來源是上繳 21 §八第 3 項之自陳** —— 執行層自報「這是最接近越界之一處」，
分析層把該處置定為規則而非個案。

**寫回前兩項閘（21 包 §八之自陳，本輪閉合）**：
(a) framework 對 037 **8／8**，組名與簽核逐字相符；
(b) `4 "DISP_HOT"` 重跑重現。

**A-DM34（新）**：`DISP_HOT` 在 `DCSD_DISP_STAT` 上是 raw **4**，
在 `FPDM_DISP_STAT`／`TGW_FPDM_DISP_STATSts` 上是 raw **3**
（FPDM 側少了 `3 "RR_CMRA"`）。**值標籤不是全域名稱，必須連同訊號一起解析。**
本批未被污染，因 04 輪已把選定判準改為 `MESSAGE.Signal` 兩半皆相等。

lint 二十項行計 0，I-sibling 0 **為實測**（#1 與 #4 同 leaf）；母本 SHA 未變。

## 23 輪要點

**R-G33 立條的當下就抓到兩條違反，其中一條是立條者與執行者雙方都漏掉的。**

下放包 23 步驟 2 只指定複驗 #3（005）。但 **#4（004 邊界條）之 leaf
同樣在 `deferred` 陣列中** —— 22 輪我自發寫揭露句時只寫了 #1，
因為當時被 deferred 的是「#1 的 ER 3」，我把它想成「#1 的事」。
**R-G33 之判準是 leaf 級而非 TC 級，這個差別正是它抓到的東西。**

| TC | 補寫前 | 判定 |
|---|---|---|
| #1 | `the warning popup is deferred` | 滿足 |
| #4 | 無任何 popup 指名 | **違反** |
| #3 | `not the protective shutdown`（1/2） | **部分違反** —— multi-stage 未指名 |

停止條件 59 觸發 → 補寫 → 全數 PASS，且「補寫後逐字相同」之停手條款
未觸發（`distinct = 3 of 3`）。

**一次對指示之偏離（§1.1，已具名上報）**：R-DM48 之補充**未**置於
R-DM48 條下。先照做再量測 —— 字面置放使 `transcribe_rulings.py` 之
順序驗證由 `全數相符` 轉為 `有不符` 並 **exit 1**；改置檔末（依下放包序）
則 exit 0。代償：R-DM48 條下留指標、對照表增列。
**R-TM13 之「原條文不刪不改」兩種置放皆滿足；差別在會不會弄壞
本檔唯一的機器保證。**

**BACKLOG 增列一項（本層自行判斷）**：deferred 解除時，
**各 TC 括號下半之揭露句須同步移除** —— 否則工作簿會宣告一個
已被測的面向沒被測。**R-G33 立條時只想到單向誤讀，其風險是雙向的。**

**A-DM34 複驗 PASS**（三個 raw 值皆與 `dbc_probe.py` 實測相符）。

> §八自陳三項，兩項是本輪自己製造的：R-G33 之「指名 token」對照表
> 由我自中文對譯（B11，與 B9 同類）；三句 `is deferred` 之正確性有時效
> 而無機制提醒。第三項最重要：**本輪把落差寫出來，沒有縮小它 ——
> 004 仍是部分覆蓋，而本輪之後看起來更像已處理完畢。**

## 24／25 輪要點

**兩包合併執行**（25 包 §四步驟 5 指定），故只出一份上繳包。

### CFTS013 檔案不在本機

下放包 24 據 `SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx`
作出全部量測。**該檔不存在於本機任何位置** —— 全 repo、`_intake/`、
`forms/`、各 feature `inputs/`、`~/Downloads`、`~/Desktop` 皆無，
**且無任何檔名含 `Associated`／`ADspl`／`Radio Error`**。

**這不是 01 輪那種檔名差異問題**（037 當時確實在磁碟上，只是用連字號）。
本輪沒有任何近似候選。依 R-DM2(a) 停手不替代。

| 24 包步驟 | 狀態 |
|---|---|
| 1 抄錄（R-DM51 為保護性條文，愈早生效愈好） | 已執行 |
| 2 A-DM31／3 DR-DM10(b) | 已執行，**各附「本層未能重算」之限定** |
| 4 `popup_priority.tsv` 來源登記 | **未執行** —— 全案唯一一次被要求把沒見過的規格文字寫進交付所依之資料檔 |
| 5 綁定 12 項／6 獨立重算 | **不可執行**（停止條件 62 無從通過、61 無從評估） |

### B11 結案 —— 不是對譯變可靠，是不再需要對譯

上繳 23 我自陳 R-G33(c) 之三個英文 token 是我從中文 deferred 項
**自行對譯**的（B11）。**我只診斷、沒開方**；下放包 25 的解法是
**R-DM53：把 token 移到宣告端** —— `deferred` 每項改為四鍵物件
（`leaf_id`／`token`／`reason`／`blocking_dr`），檢查遂成純字串比對。

`check_disclosure.py`（本輪新增）雙向檢查：**MISSING 0／STALE 0**。
`STALE` 方向有母體（004 之 TC 檢兩個非本 leaf 之 token、005 之檢一個），
0 為實測。

### R-G33(d)／R-G34

- **R-G33(d)**：揭露句之誤讀風險是雙向的 —— 23 輪我增列於 BACKLOG，
  25 包採納立為條文，並加一項我沒想到的：該檢查須於**兩個時點**
  各執行一次（寫入時、**交付前**）。
- **R-G34**：抄錄之置放以順序驗證 exit 0 為準；補充置於其所屬下放包之節，
  被補充之條下留指標。**立條後第一次適用就是我自己的補充**（R-G33(d)）。

> §八三項自陳，第二項最該記：**`STALE` 方向從未在真實情境下被觸發過。**
> 本輪 0 只證明「現在沒有殘留」，沒有證明「解除發生時抓得到」。
> R-G25（宣稱不做 X 須跑兩次）之精神在此適用而本輪未做。

## 26／26a 輪要點

**兩條停止條件觸發，兩條都是檢查抓到東西。**

### 66 —— `STALE` 一測就倒，而錯在我

`check_disclosure.py` 是我 25 輪寫的。我在上繳 25 §八自陳
「`STALE` 從未真被觸發過，我可以造一個假的解除來測它，**本輪沒做**」。
26 包把它排成步驟 4。移除 `multi-stage` 一項後，**`STALE` 報 0**。

根因：候選集為 `all_tokens - 該 leaf 之 token`，而 `all_tokens`
**也是自 deferred 陣列建的**。一個被整個移出陣列的 token
從此不在候選集內，沒有任何一行程式碼會去找它。

| 情境 | 現行實作 |
|---|---|
| token 搬到別的 leaf | **抓得到**（已以反例證明，STALE=1） |
| token 整個移出陣列（**解除之實際形態**） | **抓不到** |
| 陣列清空 | STALE 恆為 0 |

**它抓得到的，正好不是 R-G33(d) 要防的那一種。**
修法三選項（掃句型／`lifted` 旗標只增不減／另立 history）待裁，
本層不逕擇；傾向選項乙 —— **本案每一條機器保證都靠「留下可比對之痕跡」
成立，而刪除本質上不留痕跡**。

### 67 —— CFTS013 重算：十二項相符，一項不符

`EE Architecture` 下放包記 **`All`（全列）**，實測
**`All` 26／空 5／`PowerNet` 1**（32 列）。「→ 適用 Atlantis High」
之推論對 26 列成立，對其餘 6 列未經證明。

另兩項曾看似不符（`DCSD` 94、`952` 2 次），**以口徑釐清後相符** ——
下放包用「出現次數計」，我首算用「儲存格計」。
**建議日後之計數一律附口徑**（B15）。

依 26a §3.1 之定序（24-6 為前提），**24-5／24-4 未執行**。
我判斷 24-5 本身不受該不符影響，**但不自行判斷哪一項可以例外** ——
那正是 24 包那類錯誤的反面。

### A-DM35 補件 —— 分析層之質疑，其前提為誤

26 §2.4 稱「規格側之 token 為 `[DISP_ON]`、`[DISP_REAR_CAMERA]`，
與 DBC 逐字不等」。實測：規格對 `$DCSD_DISP_STAT$` **同時用兩套拼法** ——
`[OFF]` 85／`[ON]` 53／`[BLANK]` 20／`[RR_CMRA]` 72／`[DISP_HOT]` 46／
`[SNA]` 8 **六個全部逐字解得**；`[DISP_ON]` 23／`[DISP_OFF]` 12 為別名，
解不得；`[DISP_REAR_CAMERA]` 於本訊號 **0 命中**（它是 HU 側的值，107 次）。

**與 R-DM48 相容，非相衝**（停止條件 65 未觸發）。關鍵限定：
**判定落在條款層級** —— `{4820287}` 用 `[DISP_ON]` 故不可寫 raw，
RVC 諸條用 `[RR_CMRA]` 故可寫。**本批三條 TC 一字不必改。**

### 26a §二之 `copy` 檔不存在

`inputs/` 普查 9 檔、含 `copy` 者 0、同 sha256 重複群 0。
目錄 mtime（21:18）晚於 26a 所記之檔 mtime（21:15:49），
**與「曾存在而後被移除」相容**。不推定成因，A-DM36 登記。

> §十第 2 項最該記：`EE Architecture` 那 6 列，**我只數了它們，
> 沒看它們是哪 6 列**。停止條件 67 要求停手回報，我照做了 ——
> 但「`PowerNet` 是哪一條需求、空白 5 列是不是 Heading」查得到，
> 且會直接決定後果多大。**我把「停手」執行成了「不再往下看一眼」。**

## 27 輪要點

**上一輪觸發的兩條停止條件，這一輪都收乾淨了。**

### A8 解除 —— 從「未定之風險」到「已知之零」

六列逐列驗明，與下放包 27 §1.1 之表**逐格相符**：五列為空白之
Information、一列為 `PowerNet` 之 Heading（章名 `HU requirements`）。
**11 條 Functional Requirement 之 `EE Architecture` 為 `All` 11/11。**
需求本體無一受影響。

**A-DM37（新，LOW）**：r12／r18／r19 三列為撰寫樣板殘句 ——
`The TBM shall do this or that`、`The HU shall dipslay xxxxxxxx`
（原文錯字）、`0`。**三者皆帶正式之 `Document ID`**，
只看 id 清單時與真需求無從分辨。

> 上繳 26 我自陳「把『停手』執行成了『不再往下看一眼』」。
> 本輪看了。**停手是對的，但停手與不看是兩件事。**

### STALE 乙案修畢，同一情境下報 1

`deferred` 改為只增不減，解除以 `lifted`／`lifted_at`／`lifted_by`
三鍵為之。`all_tokens` 現自**全部**項（含已解除）建 ——
被解除之 token 永遠留在候選集內。

誘發測試：標 `multi-stage` 為 `lifted` → **`STALE = 1`、exit 1、
逐字指名 TC#3 與其理由**。上輪同一情境（以移除為之）報 0。
還原後連跑兩次逐字元一致，`pilot-01.json` 無殘留。

### 24-5／24-4 完成

- 綁定 **`entries: 12`／12 of 12 match**（`cfts013_sysra` sha256 `1036b2af…`）
- `data/popup_priority_sources.tsv`（4 列）＋ sidecar，`generated_by` 為腳本

**首版只得一列，反向查證後改為四列**：`\bPU\d{4}\b` 只命中
`{CFTS013-937}`，但另有三列以文字指涉同一個 popup 而不帶編號 ——
其條件（`>=56 且 <60 degrees C`）與副作用（HMI 功能受限、
LIST/ENTER 停用、觸控忽略）都在那三列。**以編號為唯一判準，
會把三分之二的相關條文留給下一個人重查，而來源登記存在的
全部理由就是免除那次重查。**

**A 類自 8 項降為 5 項**（A6／A7／A8 皆解除），本輪無新增。

> §七第 3 項是本輪自己開的缺口：反向查證把 CFTS013 之溫度門檻
> （56／60）寫進了 `data/` 檔。登記不是代入，`side` 欄與 sidecar
> 都寫明了 —— **但停止條件 60 只掃 TC 與 `batch_context.md`，不掃 `data/`。**

## 28 輪要點

三項任務互不阻塞：A（CFTS_013）停在 A3，B／C 完成。

### A —— DR-DM4 求的三個條號，是**另一套編號**

CFTS_013 全文之條號 **117 個相異，位數分布 100% 為 7 位**
（`4819633`…`5423093`）。`629`／`952` 連裸子字串都 0 次。

**佐證**：其集合**含 `4820282`** —— 那正是 CFTS_020 `1.11.2.2` 之
`{4820282}`。**兩份文件共用同一個 7 位編號空間**（Polarion 全域 id）。

即 **A-DM39：不是「有沒有這一條」，是兩套編號。** 求 3 位條號可能永遠
查無，DR-DM4 之標的須重擬。**A-DM38**：CFTS_013 為 `26PI2.5 Jun`，
CFTS_020 為 `26PI1.5 Mar`，晚三個月且屬下一個 PI 家族。

**A4／A5 之副產品**：`{CFTS013-XXX}` 與 `CFTS013-967` 在 CFTS_013 本身
**0 命中** —— 佔位符是 CFTS_020 側之未填欄，不是 CFTS_013 側之缺頁。
A-DM37 之兩句樣板殘句於全文 0 命中，**分類不變**（SYSRA 側殘渣）。

> **A3 停手之代價是真的**：本檔有 `1.5.1 Activating the DCSD Display Hot
> Algorithm {4943080}` —— **標題逐字即 DR-DM4 想要的東西**，而 DR-DM4
> 已開三輪。停止條件 71 說停 A3，我停了。一句「續行 A3」即可解封。

### B —— 矩陣是類別制，含 **0 個 PU 編號**

交集 0、僅清單有 1332 —— 這三個數字說的是同一件事：**兩份文件以不同的
鍵在講話**。接合點在**類別碼**：清單 `Main` 欄 5，**1272／1341 = 94.9%**
帶單一矩陣類別；`PU0517`／`PU0130` 皆為 `1T`。

**DR-DM2 在原理上可機器化**：明序清單（p4）＋ N×N 表（p10）× 欄 5 之類別碼。

B3 之問法須改：矩陣以 id 無關之方式定義優先序，故 popup 增刪**不使其失效**；
會使其失效的是類別詞彙漂移，實測為 **0**。

**B17（新）**：矩陣對 `Cat. SL` 之位置**三處說法不同** —— p4 排在 `Cat. X`
之下、p9 稱 `is maximum priority`、p10 稱 `stacked under RVC`。
**DR-DM2 即使答覆了，這個不一致仍在。**

### C —— `rvc-01` 六條

007 三條（進入／還原／負向）、008 三條（前態 OFF 之進入／目的態 OFF 之還原／
過渡畫面期間之進入）。**六條皆寫 DCSD 側 raw 值** —— 所引六條之逐字皆為
短拼法（`[RR_CMRA]` → 3、`[ON]` → 1、`[OFF]` → 0），依 A-DM35 之條款層級判定。
HU 側 `$TGW_DISP_STAT$` 一律不寫 raw（DR-DM9(b)）。

**007／008 之切分是本層的判斷**：CFTS_020 全文 `static` 0 命中、`dynamic`
1 命中，SYS2 之 12 列同時錨到兩個 leaf 且錨據相同。本層以「前態／目的態」
切分並揭露之。**停止條件 72 未觸發，但其判準在本批無標的** ——
037 八條之外部引用 0/8，不引章節。**不是斷裂，是不可區分**，
而後者會讓人以為追溯成立。

**DR-DM11（新，HIGH）**：037 之 007 要倒車檔訊號，CFTS_020 之 24 條適用
條文一律寫 `if the Rear View Camera is to be displayed`。
2021 矩陣 p8 有逐字之 `Gear in R` —— **看得到而不能用**（HU 側文件，
不得混引）。**這是本輪最想抄而沒抄的一句。**

lint 二十項行計 0（I-sibling 有母體，0 為實測）；`check_disclosure` 雙向 0；
綁定 `entries: 13`／13 of 13；母本 sha 未變。

## 28a 輪要點

**十筆 DR 改 `SENT (2026-08-25)`，阻斷範圍一字未動。** `DR-DM11` 維持
`OPEN` —— 其於 28 輪任務 C 開立，時序在 28a 之後，不在其涵蓋內。
另具名：28a 之封別表列九筆而內文稱十筆，`DR-DM2` 只見於 §三；
本層以 §三之逐字為據一併改 SENT。

### DR-DM7 對帳 —— **不相衝，是台帳落後裁決十二輪**

28a §2.1(c) 設想「R-DM44 只結 VF 代碼、DR-DM7 兼求 PROXI 實例檔 →
部分結案」。**實測不成立**：R-DM44 引的就是 DR-DM7 之原文，
所求之物與所求之用途兩項逐字相同，**為全案結案**。

真正的不一致是：**R-DM44 立於 16 輪，其指示之兩處台帳動作從未執行** ——
`DATA_REQUESTS.md` 之 DR-DM7 仍列未結、`ANOMALIES.md` 之 A-DM20 仍
`[PENDING]` 而非 `RESOLVED-BY-SCOPE-CHANGE`。

> 這與 18 輪之「宣稱已執行而未執行」同型，**只是方向相反 ——
> 那次是聲明超前事實，這次是事實落後裁決。** 登為 **A11**。

**一項提請注意**：R-DM44 之重開條件為「某參數之值域在 PROXI 中依 VF 而異」。
本輪之 `rvc-01` 已觸及 PROXI 之 `r401 Rear_View_Camera`／
`r494 Rear_View_Camera_Soft_Button`（其 `Used by` 皆為長串 VF 清單），
**但六條 TC 未用到任何 PROXI 值，故重開條件尚未成立** ——
007／008 若日後要驗「無 RVC 配備之車型」即會踩到。

### 兩處我做壞了

1. **改 `DR-DM3` 之狀態時整格替換，連帶刪掉了「兩度被指定而皆不答」之沿革**
   （CFTS043 實測為 HVAC；SYS3 SYSAD 不答本 DR）。已自 `git diff` 逐字取回。
   **那正是 R-TM13 所防之事，而我在一個看似機械的欄位替換裡犯了。**
2. **27 輪我把上繳分流之 `B16` 逕放入 `BACKLOG.md`** —— 該節原有之
   `B1`–`B5` 是常設鷹架待辦，兩套編號語意不同。已加「編號之界」註記並
   改為本節序（`B6`＝分流 `B16`、`B7`＝分流 `B14`）。登為 **B21**。

### 停止條件 74 之自我複核

`rvc-01` 六條之每一個值皆可逐條溯至 CFTS_020 之短拼法 ＋ DBC `VAL_`，
**無一以「DR 已發」為由放行**。反面證據：**HU 側 `$TGW_DISP_STAT$` 之值
DR-DM9 已 SENT 而本批仍不寫** —— 那是最容易鬆手的地方，未鬆手。

## 29 輪要點

### 停止條件 76 觸發 —— 第三種讀法出現了

CFTS_013 §1.5.3 之 **13 條全部適用本專案**（`Radio` 含 `R1H`、
`EE Architecture:All`），其門檻為 **50／51–55／56–<60 degrees C**。
而 CFTS_020 `{4820289}` 對同一專案給 **85 degrees C**。

最尖銳的一組並列：

> `{4820290}`：`When the DCSD Display transitions from a Hot state (> 85 deg C) to a non-Hot state (<= 85 deg C) …`
> `{4943107}`：`When the DCSD Display transitions from a Hot state (> 50 degrees C) to a non-Hot state (<= 50 degrees C) …`

**同一主詞、同一句型、同一轉換、不同數字。** 我原先寫「或許量的是
不同的東西」，補驗後**該說法站不住，已具名更正**（R-G19）。

21 輪 A-DM33 曾記「若答覆顯示存在第三種讀法，#4 之 ER 3 須重估」——
**它出現了**。`pilot-01` 三條之 `85 degrees C` **一字未動**（停止條件 76）。

### A-DM40 —— 我的判準把 13 條適用條文判成 0 條

首算用 `"R1H" in Radio and "Atlantis High" in EE`。該判準在 CFTS_020 上
**兩輪都正確**（該檔逐一列舉架構名）。**而 CFTS_013 對 1.5.3 全節寫
`EE Architecture:All`。**

| | 首算 | 更正後 |
|---|---:|---:|
| §1.5.3 適用條數 | **0** | **13** |

**結論完全相反，而抓到它的不是機器** —— 是「一份被 CFTS_020 轉指五次的
文件不可能完全不適用」這個不合理感。全檔 EE 值域實測
`All` 68／`PowerNet` 16／…／`Atlantis High` **1**，該分布本身就是線索。

形態同 A-DM29 與 STALE 候選集：**判準寫得像在量測，
實際上編碼了一個未被檢查的假設。** R-G27 防過寬，本項是過嚴。
回溯檢查：21／28 兩輪皆針對 CFTS_020，該檔 EE 值域不含 `All`，未受影響。

### 補驗 R-DM51 之依據 —— 成立，但事實變了

SYSRA 全檔 **`the DCSD shall` 0 列、`the HU shall` 6 列**，
其回復條寫 `the **HU Display** transitions from a Hot state (> 50 …)`。
**R-DM51 之依據經本層重算確認。**

**新事實**：CFTS_013 **docx** §1.5.3 以 `the DCSD shall`／
`the DCSD Display` 為主詞，給了**同一組數字**。
即 R-DM51(a) 之禁止仍有效且未被違反，
**但「DCSD 側沒有 50 這組數字」本輪起不再為真。**

### DM2 降級 —— `popup_priority.tsv` 已建

**1341 列 = PU 母體（相符）**，1272 已解析／69 `UNRESOLVED`。
鍵為**類別碼**（矩陣全篇 0 個 PU 編號），序取矩陣 p4 之九列明序清單
（逐字存於 sidecar 之 `ladder_verbatim`）。
`PU0517`／`PU0130` 皆 `1T` → rank 5。

三項強制揭露俱全：**26 列 SL 逐列標 `PENDING: DR-DM2 Cat SL precedence`**、
語意漂移前提未證、69 列標 `UNRESOLVED` 不省略。

### R-DM55 ＋ DR-DM12

007／008 之切分**維持，六條不動** —— 素材內確無區分依據，
且**錯誤可逆：只需改 `leaf_id` 一欄，TC 內容不受影響**。
DR-DM12 開立（037 作者），`BACKLOG.md` 新增其重審節。

> §九第 3 項最該接著做：`{4821589}`／`{4821590}`／`{4821591}` 等五個轉指
> 條號**就是 warning → off 之訊號序列，也就是 pilot-01 原 #2 被 deferred
> 的那個東西**。本輪停手範圍內未追是對的，**但它們現在位置已知、可取得、
> 且直接對應一個開了四輪的 DR。**

## 30／30a 輪要點

### 五條轉指全部是 CUSW —— 假說否證，而否證的方式指出了答案

`{4821587}`／`{4821589}`／`{4821590}`／`{4821591}`／`{4821592}` **全部**
`[Radio:VP4R84] [EE Architecture:CUSW]`，落在 `§1.15.5.5.2`。
既非組 A 亦非組 B（停止條件 80 未觸發）。**A1／A2 不能因此自解。**

**但補測（§1.7）把「查不到」變成「查到了」**：五條各有**逐架構之孿生**。
以三元組為例，本專案之孿生為 `{4819862}`／`{4819863}`／`{4819864}`：

| 成員 | 角色 | 對本專案 |
|---|---|---|
| `{4819862}` | DCSD 決定關背光 → 送 `[DISP_OFF]` | **`noSys`** |
| **`{4819863}`** | HU 見 `[DISP_HOT]→[DISP_OFF]` → 送 `[DISP_OFF]`＋`[0%]` | **適用** |
| `{4819864}` | DCSD 收 HU 之 `[DISP_OFF]` → 關背光 | **`noSys`** |

即：**multi-stage 之 HU 側對本專案有定義、DCSD 側沒有；
而 CFTS_013 §1.5.3（13/13 適用）補的正是 DCSD 側。**
兩份文件之分工在此對得上。**本層不作此裁定**（DR-DM10(a)，Tier 2）。

另一項並列（**後件逐字相同、前件不同**）：組 A 之 `{4820283}` 缺的
「何時算顯示完畢」，multi-stage 版本給了 ——
**DCSD 送出 `[DISP_HOT] → [DISP_OFF]` 之轉換**，而 CFTS_013 `{4943104}`
說那發生在 popup 顯示 **10 秒**後（`Only DCSD shall implement 10 sec timer`）。

### R-G37 ＋ 一項我自己的更正

**R-G37（全域）**：適用性判準須自該檔之值域導出，含通配值之檢查，
不得沿用他檔之判準。R-G27 條下留指標 —— **R-G27 防過寬，R-G37 防過嚴。**

**而本輪第一件事就是它抓到我**：上繳 29 §2.2 我寫「CFTS_020 之
`EE Architecture` 值域**不含 `All`**」，並以此證明 21／28 兩輪未受
A-DM40 影響。**本輪實測：`All` 出現 83 次，舊判準漏網 71 條。**

重做回溯：21 輪之標的（`4820282`–`4820292`）與 28 輪之標的
（RVC × `$DCSD_DISP_STAT$`）**皆不在漏網內** —— **結論仍成立，
但理由是假的**。真正的理由是「那兩組條文恰好逐一列舉架構名」。
登為 **B25**：**R-G22 立於 12 輪規制的正是這件事，
而我在一份宣告自己在做回溯檢查的文件裡犯了。**

### `{CFTS013-930}` 補驗 —— R-DM51 之依據成立

逐字取得（`Document ID` 錨定，1 列）。`Associated`／`Disassociated`／
`DCSD`／`_ADspl`／`_DDspl` 五項俱在，與 R-DM51 之表述逐字相符。
**上繳 29 §九第 2 項之自陳至此閉合。** 停止條件 81 未觸發。

### DR-DM7 CLOSED、A-DM20 改標、A11 關閉

依 R-DM44（16 輪）：DR-DM7 標 **CLOSED**，A-DM20 標
`RESOLVED-BY-SCOPE-CHANGE`（**不標 `RESOLVED`** —— 所求之物未取得，
是用途被 R-DM33 消滅）。**十二輪未執行之事實記於 A-DM20。**

DR 現況 12 筆：**9 SENT、1 CLOSED、1 OPEN、1 待發**。

### `pilot-01` 凍結

三條之 `85 degrees C` 登記為**條件性正確** ——
其正確性以「本專案走組 B」為前提，而 CFTS_013 §1.5.3 之出現使該前提
**待證而非已證**。**維持現狀、不改、不寫回。**

30a 之 VF169 **未落磁碟**，T1 完成（確認不存在）、T2–T5 待置入；
綁定維持 13 項。

> §九第 3 項最該記：**自陳欄不該是待辦清單的傾倒處。**
> 初稿寫「我沒有查」，寫完去查，五分鐘。**本輪是第二次**
> （27 輪反向查證是第一次）**「自陳未驗」在寫下的當下就變成可驗**。

## 31 輪要點

### 71 條漏網全在診斷章 —— 十輪無害是運氣，不是設計

68 條 SFR ／ 3 條 Description，章節集中於 **`§1.4.x`**
（Lost Communication／Component fault／Implausible values）。
其中 **51 條**為同一種四句式樣板（DTC matrix／monitor type／
monitor rate／limp-in action）。

**本 feature 之每一次量測其標的皆在行為章**（`1.11.2.2`／`1.15.x`／
`1.8.2.5.x`），**而漏網之 71 條全在診斷章 —— 兩者不相交。**

> **若當初某一輪之標的落在 `§1.4.x`，該輪之結論就是錯的，
> 而且沒有任何機制會發現。**

**T4 三項重測皆不變**：RVC 24→24、組 A 7→7／組 B 4→4、
`turn off … backlight` 2→2；兩批次所引 11 個條號之適用性**無一改變**。
**T5**：`coverage_map.py` 不讀架構欄（其母體判準是 SYS2 之 `Category`），
**不需重跑**。

### 三條要緊的

- **`{4819273}`**（§1.4.1.2.6「DCSD - Display Hot」，`[EE:All]`，**適用本專案**）
  逐字 `Execute 'Display is Hot' portion of DCSD Display Hot Algorithm -
  See CFTS013-629.` —— **被舊判準排除十輪，且其轉指正是 DR-DM4 之標的。**
  A-DM33 之母體已加註（結論不變，**但 `1.11.2.2` 不是全部**）。登為 **A14**。
- **`{4819353}`**：`$DCSD_DISP_STAT$` 之 **5／6 為不合理值** ——
  與 DBC `VAL_`（定義 0,1,2,3,4,7）互相印證，A-DM35／R-DM48 之獨立佐證。
- **`{4819134}`**（`§1.2`，`Artifact Type: Description`）：
  **CFTS_020 自己也載 Associated／Disassociated 之區分** ——
  30 輪補驗 R-DM51 時我只在 SYSRA 找到它。**R-DM51 因此多一個獨立來源，
  且該來源正是本 feature 之主要規格。**
  而它是「不重要的 3 條 Description」之一 —— **T2 之分列計數若被拿來衡量份量，
  會把它算掉。**

### 我在同一份文件裡把同一個錯犯了第二次

§5.2 之初稿：我用八個關鍵詞去計數，**59/63 零命中**，
然後在那份輸出**正下方**寫了一句「其主題為診斷行為」——
**從章節標題推的，而我計數的是本體。**

**第一次是上繳 29 §2.2 的 `All` 那句，本輪才剛把它寫成 R-G22 的指標。**
這次當場被自己的輸出打臉（零命中就在那句話上面），遂逐條讀了全部 63 條。
**但那是輸出恰好擺在旁邊，不是我先想到要驗。**

> **R-G38 規制自陳欄之項，而本例不在自陳欄** —— 它是正文裡的一句判定。
> **R-G22 規制它，而 R-G22 已經在了。問題不在缺條文，
> 在我讀自己寫的句子時不夠警覺。**

## 32 輪要點

### 停止條件 87 觸發 —— 172 條，逾 30，未生成

以三條需求文之逐字內容導出九個詞掃 CFTS_020（R-G37 新判準），
**命中 172 條**。下放包 §2.2 定「逾 30 條 → 停並回報（不生成）」。
**`ops-01` 未生成，T2／T3 未執行。**

### 但 172 有一半是我的詞表造成的

九個詞裡有三個是**訊號提及詞**（`disp stat` 126／`intensity req` 77／
`touch coord` 38）—— **凡提及該訊號者皆命中**，而 `$DCSD_DISP_STAT$`
是三個批次共用的訊號。故母體**與另兩批重疊：RVC 48 條、Display Hot 18 條**。

| 界定 | 條數 | 87 |
|---|---:|---|
| (A) 主題詞 **或** 訊號提及詞（本輪所用） | **172** | 觸發 |
| (B) 僅主題詞 | **88** | 仍逾 30 |
| (C) 主題詞且不含任何訊號提及 | **18** | 未逾 |

**本層不自行擇一** —— 縮窄母體等於自行改變任務範圍。
**但三種各有其漏**：(C) 最小，**而它排除的恰好是 001 需求文逐字要求的
「send appropriate display state and brightness requests to DCSD」那些條文**。
登為 **A16**。

### 兩項既有阻斷在本組立即現形

- **A15（新）**：037 三條全用 `DISPLAY_ON`／`DISPLAY_OFF`，DBC 為
  `1 "ON"`／`0 "OFF"`，規格側另有別名 `[DISP_ON]`／`[DISP_OFF]` ——
  **三者兩兩逐字不等**。DR-DM8 問的正是這個，**SENT 未答**。
  **DR-DM8 不是新問題，但這是它第一次直接擋住一整批 TC。**
- **003 之 Splash 時段**轉指 `{CFTS009-722}` —— DR-DM1 SENT 未答，
  003 之時長面向可預見為 deferred。

### 附帶五項全數執行

`{4819344}` 之 `[Fh: sna]` 入 DR-DM9(b) 附件三（**規格對 HU 側值至少有
三種書寫**：長拼法／雙記法／十六進位）；`{4819273}` 入 DR-DM4 附件二
（**3 位號亦在診斷章且適用本專案**）；`{4819233}`／`{4819234}`
（`Ethernet Cable`／空字串）併入 A-DM37；A-DM33 加註複核（A14 併入）。

**`PLAYBOOK.md` 新增 §5a 寫作慣例（建議，非條文）**：
凡寫「全在／皆為／不含」之句，其**正上方**應緊接該句所據之腳本輸出。
附兩例 —— 29 §2.2 之 `All`、31 §5.2 初稿之「主題為診斷行為」，
**兩次皆為 R-G22 所規制，而 R-G22 已經在了**。

## 33／34 輪要點（收尾）

**兩包合併執行** —— 34 包落檔時 33 尚未執行，其 §2.1 明文指示執行 33 之步驟 2–8。

### `ops-01`：88 → 52 → 14 軸 → 13 條

排除 36 條（E1 已被兩批引用 6、E2 主題屬 Display Hot／RVC 27、E3 `wake` 偽陽性 3），
逐條具名理由。**R-G39 之兩段式生效** —— 母體 52 與產出 13 之間隔著行為軸。

### 一處內容實錯，本輪抓到並改

合併 lint 首跑報 **P = 3**。根因二項：

1. **值 5／6／201 之所以是「不合理值」，正是因為它們沒有 `VAL_` 標籤** ——
   我把不合理值寫成訊號賦值，**這在定義上就不可能合格**。
2. `$RADIO_B3.RQ_DISP_INTS$` 之訊息名**來自 VF169**，而 30a 明文
   「只登記不採用」（停止條件 83 之標的）。**首跑之 83 掃描沒抓到，
   因為我掃的詞表漏了它。**

處置：#7／#8 之 ER 改為只驗可觀察行為（注入動作留在 procedure）；
**#12 移除**，其軸併入 `brightness context` 之 deferred。修正後 **P = 0**。

### 寫回 —— 一處具名偏離

下放包定標的為「`inputs/` 之母本複本」，**本層改寫入 `output/`**：
母本是客戶素材且受 `reference:` 綁定，就地覆寫會毀去唯一原件、
並使綁定由 13/13 轉為 12/13。他 feature 之慣例亦為 `output/`。
**若要求就地覆寫，請明示。**

| 項 | 值 |
|---|---|
| 寫入列 | 10 – 31（22 列），`TC-DM-001` … `TC-DM-022` |
| 方式 | **XML 外科式** —— 只改 `sheet6.xml`，其餘 47 個 zip 部件逐 byte 原樣重打包 |
| 完整性 | dataValidation 4/4、x14 2/2、worksheets 9/9、drawings 6/6、rels 16/16、zip 48/48 —— **逐項相等** |
| R 欄下拉 | `x14:dataValidation` `xm:sqref = R10:R1411` —— 寫入列在其內 |
| 回讀 | 22 列 × 15 欄，**不符 0**；第 32 列為空 |
| 來源 sha | `6372fb6be02f48dc…` **未變** |

### 覆蓋：7/8 leaf 有 TC，**無一為全覆蓋**

`SWE1-DM-006` **未覆蓋** —— CFTS_020 之適用條文中**含逐字 popup 編號者 0 條**，
唯一含 `pop-up` 一詞者轉指不在手上的 `HMI core specification requirement H4`；
而 `popup_priority.tsv` 之權威性本身待 DR-DM2(b)。依 34 §2.2 **不強生**。

其餘七 leaf 皆為部分覆蓋，每一 deferred token 皆於各 TC 括號下半逐字指名
（雙向檢查 0／0）。**未結 DR 11 筆**，清單見上繳 34 §五。
