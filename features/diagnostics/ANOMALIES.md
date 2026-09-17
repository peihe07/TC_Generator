# ANOMALIES — FW036 Diagnostics HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-DIAGnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

---

| 標記 | layer | 事由 | 出處 | 型 | 狀態 |
|---|---|---|---|---|---|
| `[A-DIAG01]` | execution | R-DIAG5(c) 之 NRC／SID 適用空白：230 列 negative／unsupported 中 205 列（89%）CFTS004 與 037 皆無 NRC 值；I/O Control SID `0x2F` CFTS004 零命中、SYSAD 零命中、僅 037 之 24 列明載 | 本包實測 `data/nrc_coverage.tsv`、`data/sysad_uds_tables.md` | 條文適用空白 | **RESOLVED**（R-DIAG5(amend)，Pei 2026-09-17）—— 226 列中 223 列已解（CFTS004 5／037 20／ISO 198），殘 3 列轉 DR-DIAG-1（非阻斷）|
| `[A-DIAG02]` | execution | `R-DIAG` 四字母前綴不被 `scripts/ruling_anchor.py` 之 `RE_ANCHOR`（`R-[A-Z]{0,3}\d+`）接受，九條無法進 `RULINGS.sha.tsv`，R-G52 引用制對本 feature 失效 | `rulings_hash.py --target` 回報 0 錨點 | 全域工具 | **RESOLVED**（R-G73，Pei 2026-09-17）—— 正則放寬為 `{0,4}`；回歸實測既有 788 id 之 sha8 零變動 |
| `[A-DIAG03]` | execution | SYSAD 無 UDS 位元組序列表與 NRC 表；唯一序列表為 DTC 流程，而 037 之 DTC 提及列 = 0 | `data/sysad_uds_tables.md` §2 | 來源缺件 | **PENDING** — 不阻斷；DR-DIAG-2 維持 |
| `[A-DIAG04]` | execution | 598／5210 之前例衝突：R-DIAG7(b) 引 R-CAM2(b)「一律 0」，而已交付之 SWC 0708 工作簿 285 列中 202 列填 `1` | SWC 0708 `Test Case Specification` T..Z 欄實測 | 前例衝突 | **RESOLVED**（R-G74，Pei 2026-09-17）—— R-CAM2(b) 升為全域，598／5210 一律 0；SWC 0708 依 R-G72 不回修 |
| `[A-DIAG05]` | execution | SWC 0708 自身欄位錯位：10 列之作者名 `PeiPYHsu` 落入 `T` 欄（HDCC27 Atl-Hi），車型七欄整體右移一格 | 同上 | 外部工作簿瑕疵 | **記錄** — 非本 feature 產物，不修；供 SWC 線參考 |
| `[A-DIAG06]` | analysis | 下放包 CDD-01 §4(b) 以合併列書寫 8 列實為 11 檔，「必投遞」數不可直接對帳（審閱 A1）| `down/20260917_CDD-01.md` §4(b) | 下放包形式 | **RESOLVED** — 後續下放包投遞表一檔一列 |
| `[A-DIAG07]` | analysis | 下放包 CDD-01 §5 稱 `-057` 歸 #11；實測歸 #10 `$1801`。分析層以標題「Audio Output Settings」推定，未查 L3（審閱 A2）| 同上 §5 | 未查即斷言 | **RESOLVED** — R-DIAG3(amend) 落字；framework.md Part II 記明 |
| `[A-DIAG08]` | analysis | 下放包 CDD-01 §5 只點名 `$5000` 跨母節；實為 6 個（審閱 A3）| 同上 §5 | 漏列 | **RESOLVED** — R-DIAG9(amend)(c) 落字 |
| `[A-DIAG09]` | analysis | 選定 `R-DIAG` 四字母前綴前未查 `ruling_anchor.py` 正則（審閱 A4）| 同上 §2 | 未查即命名 | **RESOLVED** — R-G73；前綴為全域命名空間，其可行性由全域工具定義 |
| `[A-DIAG10]` | analysis | 下放包 CDD-01 §7 斷言「無阻斷性 DR」，未先量測 NRC 值之來源覆蓋率（審閱 A5）| 同上 §7 | 違「先量測後斷言」| **RESOLVED** — 審閱撤回該句；CDD-01 §8.1 已更正為阻斷性 |
| `[A-DIAG11]` | analysis | 下放包以 V1 (2) 為母體發包；V1 (3) 已在同目錄（審閱 A6）| 同上 §1 | 非預見性 | **RESOLVED** — R-DIAG8(amend)；記事實，非責任 |
| `[A-DIAG12]` | analysis | R-DIAG9(c) 條文書「43 個」實為 42（`$5007` 未引用計入，審閱 A7）| `features/diagnostics/RULINGS.md` R-DIAG9 | 條文與實測不符 | **RESOLVED** — 條文不改（R-TM13），R-DIAG9(amend)(a) 記 42 |
| `[A-DIAG13]` | execution | `Toro_ATL_MI` 之 PROXI `Market_Area`（byte 160）Type 欄記為 `Not Used`，其餘五本為 `Table`；值 `2` 仍存在 | `forms/proxi/Toro_ATL_MI/…XLSM` `PROXI Write!F682` | 證據強度 | **記錄** — R-DIAG7(amend) 明文「不影響填法」|
| `[A-DIAG14]` | execution | 下放包 CDD-01_A T4 書 `$XXXX` 白名單「27 種」，該數為 CDD-01 3-5 之 037 token 種數；依其自身定義（`layer3_assign.tsv` 之 DID 集合）實測為 **36 種** | `down/20260917_CDD-01_A.md` §3 T4 | 數字引用錯置 | **RESOLVED** — 依定義實作 36 種；追補 A §二**已追認** |
| `[A-DIAG15]` | execution | `docs/fw036/RULINGS.sha.tsv` 表頭自稱「單一全域檔，重生一律掃描全部 canon 與各 feature」，實際只含 `features/security/RULINGS.md` 32 列；全 repo 重生為 837 錨點。`rulings_hash.py --check` 因而 FAIL —— **本包動工前即 FAIL**，非本包造成 | `docs/fw036/RULINGS.sha.tsv` | **併發覆寫** | **PENDING** — 實測**五次**（第二次在 `b432893` 提交後；第三次由 R-G75(a) 之寫前檢查攔下；第四次在 CDD-03 已正確寫入**之後**；**第五次形態不同 —— 非覆寫而是表頭被寫到檔尾**，列數不變故 R-G75(b) 之集合比對查不出，只有解析時暴露）。五次皆已修復、**無資料損失**。**R-G75(a) 只防寫前，不防寫後；(b) 只比對集合，不查結構** —— 對方不執行本條時，我方每次收尾仍須再查。去向：GC-16 全 repo 重生＋`--check` 轉綠 |
| `[A-DIAG17]` | execution | `VM-DIAG` 沿用既有 `Z` 而未另立代號（判準逐字同 R-CAM2，且 R-G74 已升為全域）| 上繳包 §4.1 | 偏離下放包字面 | **RESOLVED** — 追補 A §二**已追認** |
| `[A-DIAG16]` | execution | CDD-01 上繳包 §2.2 之表標題書 `body sha8`，其值實為 `rulings_hash.py` 之 `sha8`（section_sha）欄；且 `R-DIAG9` 自算值 `802f0427` 與工具 `cc7b5200` 不符（手算未複製工具對章節尾界之處置）| `up/20260917_CDD-01.md` §2.2 | 自算代替工具 | **RESOLVED** — 本包以工具實跑取代自算，全表見上繳包 §3 |
| `[A-DIAG18]` | execution | **列型態分類器只看標題**：3 列（`-106` row113／`-160` row167／`-340-001` row347）標題無 negative 關鍵字而描述主旨為拒絕，CDD-01 判為 positive。CDD-02 改為「標題無關鍵字時再看描述」，型態 163／133／93 → **160／136／93**，`nrc_coverage` 母體 226 → **229**（三列皆解出，PENDING 仍 2）| CDD-02 §3 之 #10 與 §3 表不符而查出 | recon 判準 | **RESOLVED** — 分類器已修，受影響之 4 檔 tsv ＋ framework.md ＋ feature.yaml 已重導 |
| `[A-DIAG19]` | execution | **037 row 161（`-154`）之 Title 與 Description 互不相稱**：Title 述 NRC 31（其內容對應 `SYS-RA-DIAG-371`／CFTS004-4940476，即 037 row 167），Description 述三訊號偵測結果（與本列所掛之 `SYS-RA-DIAG-367`／CFTS004-4940482 一致）| CDD-02 pilot01 #8 | 037 欄位錯置 | **已處置** — 依 IN §8.6 與 R-SEC15(f) 取 Description ＋ 所掛來源產出正向 TC；登 RD 回饋 FB-DIAG-g |
| `[A-DIAG20]` | execution | **037 row 347 書 `"Previous Out of Range"`**，而 CFTS004-4940356 書 `"Request Out of Range", code $31` | CDD-02 pilot01 #10 | 037 用字 | **已處置** — 依 IN §8.6 取 CFTS004 用字；登 RD 回饋 FB-DIAG-h |
| `[A-DIAG21]` | execution | **`RM-DIAG` 實作缺陷**：R-DIAG6 之定型句 `037 VM blank; procedure derived from Description + CFTS004` **自身含 `; `**，而檢查以 `;` 切段後逐段比對，致該句永遠無法通過自己所規定之檢查 | pilot01 實跑之假陽性 2 例 | lint 實作 | **RESOLVED** — 改為自串首貪婪比對、以 `; ` 為接合符 |
| `[A-DIAG22]` | execution | **lint 之 `I`／`M`／`R`／`Z` 對 Out of Scope 佔列全數誤報**（pilot01 row 23，共 12 行計）：該列依 R-DIAG3(amend) 不產 TC，其 test_item 無括號下半、四欄空白、Vehicle Model 無從填 | pilot01 實跑 | 判準待調 | **PENDING** — 建議四項對 `Test Result = "Out of Scope"` 之列豁免；本包不自改判準 |
| `[A-DIAG23]` | execution | **`I-cross` 對本 feature 全列誤報「窗未完整宣告」**（14/14）：Diagnostics 之 ER 為 UDS 回應斷言，無 R-SU33/34 之觀測窗概念，與 Security 同形 | pilot01 實跑 | 判準待調 | **PENDING** — 建議比照 R-SEC15(j) 列入 `FEATURE_EXEMPT["diagnostics"]`；本包不自改判準 |
| `[A-DIAG24]` | execution | **下放包 CDD-02 §5-2 書「canon §9 自檢 18 項」，canon 實為 17 項**（§9 之編號止於 17）| 逐項核對時查出 | 下放包數字 | **RESOLVED** — 依 canon 實數 17 項出表，17/17 全過 |
| `[A-DIAG25]` | execution | **DR-DIAG-3 之內查推翻其前提**：SYSAD §4.5 Assumptions 明載「ECU starts in Default Session」「Security access (0x27) is required for: Write DID / Routine execution / DTC clearing」與 Hardware Dependencies「Diagnostic connector (OBD-II)」。CFTS004 全欄 grep 13 筆全為假陽性（`default values`／`Key status`／`Hard key`／`$10` 為 Package Indication Code）| CDD-03 T2 | 來源已載而先前未查 | **RESOLVED** — DR-DIAG-3 結案；pilot PENDING 15 → 2 |
| `[A-DIAG26]` | execution | **`Ignition ON` 無來源**：CFTS004 與 SYSAD 對 ignition／power state 皆零命中；power_moding 之 ignition 前提源於該 feature 自身規格，非可沿用之來源。依 §8.5 自 13 條 Pre-Condition 刪除 | CDD-03 T1-2 | 環境前提無據 | **已處置** — 刪除；若 Pei 認為須保留電源前提，須另開 DR |
| `[A-DIAG27]` | execution | **I/O Control（`0x2F`）之 security access 未載**：SYSAD §4.5 之列舉僅 Write DID／Routine execution／DTC clearing，未含 I/O Control。本包依「列舉為封閉」讀為不需 0x27，故 I/O 型 TC 不寫 PC-3 | CDD-03 T1 | 由列舉之缺漏反推 | **PENDING** — 請 Pei 追認該讀法 |
| `[A-DIAG28]` | execution | **`-331`／`-332` 之 Title 與所掛來源不符**：Title 書 `connected USB devices`（與 `-329`／`-330` 逐字相同），所掛 CFTS004-4939919 書 `detected USB Hub devices` | CDD-03 batch 1 | 037 Title 重複 | **已處置** — 依 IN §8.6 取 CFTS004；FB-DIAG-i |
| `[A-DIAG29]` | execution | **`-333` 將 UDS NRC 與資料值混寫**：037 書「negative response – Service Not Supported $FF」；CFTS004-4939922 之 `$FF` 為 USB 偵測不可用時之**回報資料值**，非 NRC | CDD-03 batch 1 | 037 語意混寫 | **已處置** — 產為正向回報 TC；FB-DIAG-j |
| `[A-DIAG30]` | execution | **6 條 TC 宣告 baseline 而未使用**（`rw_pair` 之寫向 5 條 ＋ `-052`）：Pre-Condition 立 `Setting_initial`／`Pattern_initial`，ER 只比對「寫入值 ↔ 讀回值」，初值未入 ER | canon §9-9 自檢實測 | 多餘前提（§8.5）| **RESOLVED** — 寫向不立 baseline |
| `[A-DIAG31]` | execution | **`J`（行首大寫）與 R-DIAG4(a)（verbatim 照抄）衝突**：`SWE1-Diagnostics-048` 之 Description 以小寫 `when` 起首（037 原文 `1)when tester command to Read request…`），`test_item` 上半照抄即觸發 `J`。batch 2 命中 2 行（`-107`／`-108`）| batch 2 實跑 | 判準衝突 | **RESOLVED**（CDD-04 審閱 §三-1）—— 不改 lint，改依 **R-4**（canon §4.3.1 末句：verbatim 自原句中段起抄時句首轉大寫屬排版正規化）；產生器結構性套用，`J` 複驗 0 |
| `[A-DIAG32]` | execution | **`SEC-DIAG` 母體含 unsupported 型**：追補 A §一定母體為「I/O Control 母節之全部 TC」，而 unsupported 型送的是**不支援之 SID**、根本不發 `0x2F`，security access 於其語意不適用。batch 2 命中 **19 條**，全為 unsupported 型 | batch 2 實跑 | 判準範圍 | **RESOLVED**（R-DIAG13(amend)）—— 母體加 `row_kind ≠ unsupported`（33 列排除集）；19 條不補 PC-3，`SEC-DIAG` 複驗 0 |
| `[A-DIAG33]` | execution | **CFTS004 引用 `$D013` 而無該章節**（r325／r327）；037 `-115`／`-116`／`-117` 據以寫成 `0x31 RoutineControl request for DID 0xD013`，而該要件在 CFTS004 置於 I/O Control 之 `$5000` 節 | batch 2 T2 回看 | 來源懸空參照 | **已處置** — 依 IN §8.6 以 `$5000` 為受測 DID；FB-DIAG-l |
| `[A-DIAG34]` | execution | **`-048` 之 session 失效軸無 NRC**：CFTS004／037／SYSAD 三處皆未載，不為該軸產出 | batch 2 | 來源缺件 | **已處置** — 只產格式／長度與值域二軸；FB-DIAG-m |
| `[A-DIAG35]` | execution | **baseline 宣告未用之缺陷重犯**：四象限 positive（`-110`／`-114`／`-121`／`-125`）再度於 PC 立 `Quadrant_initial` 而 ER 未用 —— 與 `[A-DIAG30]` 同因（模板複製時未檢視 ER）| canon §9 自檢 | 多餘前提（§8.5）| **RESOLVED** — 已移除；此為同一缺陷第二次，寫入 profile 之寫入型 TC 規則 |
| `[A-DIAG36]` | execution | **profile 之 §1–§6 自 CDD-01_A 起未生效**：編輯以 `str.replace()` 為之而未加 assert，字串不符時靜默失敗，腳本仍印「已更新」，我據以在 `up/CDD-01_A` §6 與 `up/CDD-03` §11 回報成功而未複讀檔案。檔內至 CDD-04 仍寫「尚未實作任何一項」「待實作」「21 組草案」| CDD-04 提交前複查 | **回報不實** | **RESOLVED** — 已以逐處 assert 重寫；教訓：凡以字串比對改檔，先 assert 命中再寫，回報前複讀 |
| `[A-DIAG37]` | execution | **baseline 宣告未用第三犯**：`NR1L-DIAG-231`（`$500D` 寫入）於 PC 立 `Source_initial` 而 ER 未用。前兩次為 `[A-DIAG30]`（CDD-03）／`[A-DIAG35]`（CDD-04）| canon §9-9 自檢 | 多餘前提（§8.5）| **RESOLVED** — 已修；**並於 `gen_batch{1,2,3}.py` 加產出前守門**（命中即 `SystemExit`，不出檔），三犯之後不再靠事後自檢 |
| `[A-DIAG38]` | execution | **`X`（導航路徑無固定入口）於本 feature 為結構性誤報**：本 feature 不寫導航 hop，命中皆為 DID 名與 CFTS004 用詞之字面（`Radio Audio Output Settings`、`in-motion menu options`）。batch 3 實測 12 行，真違規 0 | batch 3 實跑 | 判準範圍 | **RESOLVED**（R-DIAG17）—— 已入 `FEATURE_EXEMPT["diagnostics"]`；落地時另揭 lint 之實作缺陷（見 `[A-DIAG42]`）|
| `[A-DIAG39]` | execution | **`$5006`／`$5005`（fade／balance）之 037 無 negative／unsupported 列**：兩 DID 各只有 2 列 positive，越界與不支援服務之行為無 037 列可掛 | batch 3 T2 | 037 覆蓋缺口 | **已處置** — BVA 於該二 DID 取四點（含越界）以補；登 FB-DIAG-n |
| `[A-DIAG40]` | execution | **baseline 位置之守門漏洞**：CDD-05 之守門只查「宣告而未用」，未查「宣告之位置」。合併本 **148 行** Pre-Condition 含 `*_initial`，違 IN §4.4 | CDD-05 審閱 §三-1 | 守門不完整 | **RESOLVED** — baseline 全數移入 Procedure 首步（IN §8.7.5(f) 式）；四個產生器與 lint `PC-DIAG` 各加第二道守門 |
| `[A-DIAG41]` | execution | **`PC-DIAG` 詞幹比對過寬**：`press` 改詞幹後把 `No push button … is pressed`（靜止態）也攔下。R-DIAG18 之立意為「需執行才成立者不是 Pre-Condition」，否定式之靜止態不需執行 | 自測之假陽性 2 例 | 判準校準 | **RESOLVED** — 加否定式例外（`No … is pressed/sent/recorded/read`）；lint 與四個產生器同步 |
| `[A-DIAG42]` | execution | **`FEATURE_EXEMPT` 對 `check_row()` 內產生之項無效**：`X` 於 R-DIAG17 豁免後仍被 `check_row()` 產出，而該代號已不在 `enabled`，`enabled.index()` 拋 `ValueError`。**290 列之合併本直接 crash，且五本之「其餘 0」實為 crash 之假象** | CDD-06 T1(d) 落地後實測 | lint 實作 | **RESOLVED** — `check_row()` 之產出一律依 `enabled` 過濾；列級與整項豁免收斂為同一道 |
| `[A-DIAG43]` | execution | **`$030A` 之行為只指向本文件外之「KeySense HMI Logic and Flow」**，該件不在來源集且 CFTS004 未載其編號版本 | batch 4 #20 | 來源缺件 | **已處置** — ER 只斷言常式完成（§8.4.1）；FB-DIAG-o |

## Assumption markers

None yet（本包未產 TC）。Inline format in generated JSON reasoning: `[ASSUMPTION A-DIAGnn]`.
