# ICS Management — ANOMALIES

登錄日：2026-08-29。量測基礎：SWRA xlsx 三分頁、SYSAD、CFTS022（皆為專案掛載本）。

| A- | 內容 | 狀態 |
| --- | --- | --- |
| A-ICS1 | SWRA Requirement Description 欄與 Title/Verification Criteria 不一致（5/10 列），呈 +1 位移：001 desc 載 $ICS_KNOB1_VAL$（=002 訊號）；005 desc 載 $ICSPowerButton$+display ON/OFF（=006 題）；006 desc 載 $ICSScreenOffButton$+3s timeout（=007 題）；009 desc 載 <Tstuck_button>（=010 題）；010 desc 載 $TGW_DISP_STAT$/$RQ_DISP_INTS$ during HU Screen ON（=011 題，而 011 缺列）。007 自身相符，位移為 005–006、009–010 兩帶 | OPEN（DR-ICS1） |
| A-ICS2 | SYS-RA-ICS-001~012 於 SWRA 與 SYSAD Table 5 語意逐條零對應（例：SWRA 001=KNOB1_DIR，SYSAD 001=Restore TGW_DISP_STAT）；Excluded 分頁引 013/014/015，SYSAD 僅至 012 | OPEN（DR-ICS3） |
| A-ICS3 | SYS2 Traceability `Source NRL ID(s)` 欄 12/12 全空；Excluded 分頁 `NRL ID` 欄 9/9 全空 | OPEN |
| A-ICS4 | ID 前綴不一致：需求分頁 `SWE-ICS-0nn`，追溯分頁 `SWE1-ICS-0nn`。本 feature 文件一律以 `SWE-ICS-0nn`（需求分頁本）指稱 | NOTED |
| A-ICS5 | SYSAD §4.10.1（reverse gear）/§4.10.2（resuming Screen OFF）僅存目次，本文無內容；正為 (012) 之預期母文 | OPEN（DR-ICS2/ICS5） |
| A-ICS6 | SWRA Priority 欄為 High/Medium，與 IN §10.2 P0–P3 不同軸，不得直取；TC priority 依 TEST_CASE_PRIORITY.md 重判 | NOTED |
| A-ICS7 | 分析層之誤（自承）：下放包 01 初稿之 DR-ICS5 將「according HMI and CFTS020」句之物件號寫為 4915277，實測為 **4915278**；未量測即填號，違 R-G36 精神。已於落檔前修正 | CLOSED |
| A-ICS8 | 分析層之誤（自承）：下放包 01 §一-1 稱 inputs/ 將置「三份來源檔…皆偽 docx／UTF-8 文字」—— 以專案掛載副本之型態推度 repo 實體，未量測即斷言。實測（上繳包 01 §六-1）：inputs/ 實四檔、皆真 Office 檔、無 CFTS022；b01 所錨之 CFTS022 實體在 features/privacy/inputs/ | CLOSED（事實已正，約束見 R-DD26 v2(g) 同族：分析層書前提須標量測時點） |
| A-ICS9 | DR-ICS5 前提過時：CFTS020 Functional Specification（R1LR_Atl-H_26PI1.5 … CFTS_020 ICS and DCSD_20260310-1533.docx）實在 inputs/，407 個 ObjectID，目次直接涵蓋 Display／Browse／Navigation／Stuck Button 四面。登記時之量測基礎僅及專案掛載三檔，素材落入後未同步 | OPEN（DR-ICS5 已改述；納源與解鎖屬 Pei 範圍裁定） |
| A-ICS10 | 分析層之誤（自承）：下放包 01 缺 FO §8.1 五成分（禁區、R-XX@sha8 引用、預期數字、掃描條件、升級條件），且未查 R-G25 即指定 workbook/／batches/ 落點（lint_paths 實測基線外 4）。自下放包 02 起依 FO §8.1 全成分書寫 | CLOSED（落點已由 R-ICS5 採認改正） |
| A-ICS11 | SWE-ICS-010 之第二行為面未涵蓋：CFTS020-4819617（逐字：ignore the press request until … released）即 SWRA 010 之 Verification Criteria 所指，b01 三條皆在 CFTS022 之 DTC 面，無一驗該 VC。並：二門檻未必同值（CFTS022-4914956 之 120 s 管 DTC；CFTS020-4819617 之 <Tstuck_button> 管 ignore），R-ICS3 只涵蓋前者 | OPEN（DR-ICS10 已登；b02 補寫中，R-ICS9） |
| A-ICS12 | 分析層之誤（自承，A-ICS9 同失效族第二例）：DR-ICS4 登「CFTS019 未提供」前未檢索 repo。實測（2026-08-29，search_files）：`features/audio_mgmt/inputs/` 存 CFTS019 七件，含 `R1LR_Atl-H_25PI3.5_…_CFTS 019_Audio Management_20250910_1235.pdf` 與 Part1（released 20260415）／Part2 xlsx。登記 DR-ICS4/5/6 三件時皆未執行 repo 全域檢索，自本輪起「未提供」類 DR 發出前必附 repo 檢索實測 | CLOSED（DR-ICS4 已改述；納源待裁） |
| A-ICS13 | CFTS022 版本雙軌：repo 唯一實體（privacy 所綁，b01 逐字驗證所據）為 **25PI3.5_20250910**；分析層偵察所用之專案掛載本為 **26PI2.5_20260608**（較新，不在 repo）。b01 所用之 4 句 verbatim（4914956/57/75/76）二版實測相符（偵察自新版摘、執行層於舊版逐字命中），**全域等價未證**；新版落 repo 與否屬 Pei | OPEN（R-ICS12 已定二態處置） |
| A-ICS14 | **語境不同步**：下放包 02 之 §8 追補（E1 預解、spec-index 四本 HMI L&F 偵察、CFTS022 新版處置、CFTS019 七件偵察）與 R-ICS11／12／13 未進入執行層語境。證：上繳包 02 之 sha8 表僅 10 錪點（實檔為 13）、§12 引用清單無 R-ICS11／12／13、追補之二項偵察作業（四本 HMI L&F、CFTS019）未執行。影響：執行層將 R-ICS13 已裁之事當新判準回報（其取捨與 R-ICS13 一致，獨立收斂，無實害）。拿法：下放包落檔後之追補一律另發一包（NN+1），不以同檔追寫；執行前須重測 handoff sha256 與 rulings 錪點數並入上繳包 | CLOSED（拿法已定，見 R-ICS14） |
| A-ICS15 | 分析層之誤（自承）：下放包 02 §0 P3 將 CFTS020 之「407」寫為物件數。實測（上繳包 02 §1.1）：407 為章節標題之 `{ObjectID}` 相異數，物件屬性頭 `^\d{7}: \[` 之數為 **2180**。承接上繳包 01 之數字而未辨口徑。TC 生成之母數一律取 **2180** | CLOSED |
| A-ICS16 | `VOLUME POP_UP` 顯示條件未載於任一已納來源：CFTS022-4914974 無條件式陳述，CFTS020 全文 `VOLUME POP_UP` 命中 **0**（上繳包 02 §11-1）。V1／V2／V3 共 6 行 ER 斷言 popup 顯示，便 FF 風險。現階段依 IN §8.4.1「模糊即保留模糊」維持不改；CFTS019 到位後（DR-ICS4）必須複核 | OPEN（追蹤項，非現存缺陷） |
| A-ICS17 | b01 之 V3「一次連轉三格」隱含 detent 計數時間窗，CFTS020-4819583 逐字載 `<TPeriodToCountKnobDetents>`（及 `<TPeriodToSendNoChange>`）皆為符號無值，而 V3 現無佔位涵蓋此點（上繳包 02 §11-4）—— 屬 IN §8.4.3 之缺件未佔位 | OPEN（DR-ICS12；b03 補佔位） |
| A-ICS18 | R-ICS2 之三軸判準於 CFTS020 幾近不可用：該文件 2180 物件中 `ECU` 軸不存在者 **1916（87%）**，逐字套用後只放行 28 個物件，連 b02 所錨之 4819617 亦被判不適用（上繳包 02 §四）。成因：R-ICS2 係依 CFTS022（跨 ECU 文件）之屬性形制所設，CFTS020 為 ICS 專屬文件，不以 ECU 作區別軸。連帶：上繳包 02 §11-5 之「1.8.1.3 之 24 物件中 23 不適用」係舊判準下之結果，須重判 | CLOSED（R-ICS2 v2） |
