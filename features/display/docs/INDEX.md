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
