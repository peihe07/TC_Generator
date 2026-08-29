# ICS Management — DATA_REQUESTS

發出日：2026-08-29（Pei 准，下放包 01）。每包上繳附未結 DR 清單。
未結期間，受阻欄位一律 `PENDING: DR-ICS{n} <缺件名>`（IN §8.4.3）。

**催件排序（Pei 2026-08-29「裁」核可）**：
- 上游急件：DR-ICS9（V 組存續）、DR-ICS10（ignore 門檻）、DR-ICS1（縮圍版：俟 b02 偵察定 006/009 可否繞過後發，005 恐繞不過）、DR-ICS2（011/012 補列）
- 緩件：DR-ICS3（交付前須結，ASPICE 追溯鏈）、DR-ICS5（與 A-ICS13 版本問併送）、DR-ICS7（純確認）
- 內部收口中：DR-ICS8（b02 作業 A，R-ICS8／13）、DR-ICS4（R-ICS11 綁 audio_mgmt 原件，上游只剩版本確認）

| DR | 內容 | 阻斷面 | 狀態 |
| --- | --- | --- | --- |
| DR-ICS1 | SWRA `SWE1 Requirements` 之 Requirement Description 欄於 001/005/006/009/010 與 Title、Verification Criteria 不一致，呈 +1 位移（詳 ANOMALIES A-ICS1）。請提供各 ID 正確原句 | 001, 005, 006, 009, 010 | OPEN |
| DR-ICS2 | SYS2 Traceability 列 SWE1-ICS-011（HU Screen ON）、012（Rear View Camera Transition），需求分頁缺列。請補列或確認撤銷 | 011, 012 | OPEN |
| DR-ICS3 | SYS-RA-ICS-001~012 於 SWRA 與 SYSAD Table 5 語意逐條不對應；Excluded 分頁另引 013/014/015 而 SYSAD 僅至 012。請確認以何者為準（A-ICS2） | 全 feature 追溯 | OPEN |
| DR-ICS4 | 【改述 2026-08-29，見 A-ICS12】CFTS019 實在 `features/audio_mgmt/inputs/`（七件：25PI3.5 PDF、Part1 released 20260415、Part2 等），原述「未提供」前提過時。改問：①何件為本 feature 應用之 volume 母文現行版 ②音量階數域與 VOLUME POP_UP 顯示條件之所在章節。納源與綁定（R-ICS10 式）待 Pei 裁 | 001, 002；V3 佔位；V1–V3 之 popup FF 風險 | OPEN |
| DR-ICS5 | 【改述 2026-08-29，見 A-ICS9】請確認 inputs/ 之 `R1LR_Atl-H_26PI1.5 … CFTS_020 ICS and DCSD_20260310-1533.docx` 是否即本 feature 應用之 CFTS020 Functional Specification 現行版（原述「未提供」前提過時） | 006, 007, (011) | OPEN |
| DR-ICS6 | 【縮圍 2026-08-29】KNOB2／Enter／Back 之母條實在 CFTS020 1.8.1.1／1.8.1.2／1.8.1.3（上繳包 01 §六-2）；仍缺者為 HMI Logic and Flow 之畫面流（browse／tune／navigation 之 UI 行為） | 003, 004, 008, 009 | OPEN |
| DR-ICS7 | 【限縮 2026-08-29，見 A-ICS11】本 DR 僅及 **DTC 面**：請確認 CFTS022-4914956 之 120 s 即本 DUT 之 DTC 置位門檻（首波暫採 120 s，R-ICS3）。ignore 面之 <Tstuck_button> 另立 DR-ICS10 | 010 | OPEN |
| DR-ICS8 | 本 feature 未綁定 DBC。【解法已裁 2026-08-29：R-ICS8 之 LID→CAN 路徑，LID v1_78 實測 9/9 命中（上繳包 01 §六-4）】b02 依 R-ICS8 改寫佔位後提請結案；DBC 查無之備援名保留本 DR 追蹤 | 訊號欄 | OPEN |
| DR-ICS9 | DUT 之 CFTS022 ECU 屬性歸屬：Stuck Button 物件列 `ICS`，Volume 物件（4914972–76）僅列 `LTM/ETM/RRM`。暫採 `{ICS, LTM}` 聯集（R-ICS2），請上游確認邊界。【風險註 2026-08-29：若收窄為 ICS，b01 之 V1/V2/V3 全數回收（上繳包 01 §八-2）】 | 適用域 | OPEN |
| DR-ICS10 | 【新登 2026-08-29，自 DR-ICS7 拆出，見 A-ICS11】CFTS020-4819617 之 `<Tstuck_button>`（ignore 行為門檻）具體值；與 CFTS022-4914956 之 120 s（DTC 面）未必同值，請分別給值。【b02 二處佔位待其回覆】 | 010（ignore 面） | OPEN |
| DR-ICS11 | 【新登 2026-08-29，上繳包 02 §三-4】DTC `B14DA-2A` 之 Enable Condition EC3 轉引 `{SIS-5161}`（Local Battery Voltage operating range），該文件全 repo 掃描 0 命中。請提供電壓範圍或文件 | S1／S2／S3 之 Enable 條件無法入 Pre-Condition | OPEN |
| DR-ICS12 | 【新登 2026-08-29，見 A-ICS17】CFTS020-4819583 之 `<TPeriodToCountKnobDetents>` 與 `<TPeriodToSendNoChange>` 具體值（detent 計數時間窗）；V3 之「連轉三格」與將來 knob2 全面皆依賤此值 | 002（V3）、003、004 | OPEN |
