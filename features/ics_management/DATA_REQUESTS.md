# ICS Management — DATA_REQUESTS

發出日：2026-08-29（Pei 准，下放包 01）。每包上繳附未結 DR 清單。
未結期間，受阻欄位一律 `PENDING: DR-ICS{n} <缺件名>`（IN §8.4.3）。

| DR | 內容 | 阻斷面 | 狀態 |
| --- | --- | --- | --- |
| DR-ICS1 | SWRA `SWE1 Requirements` 之 Requirement Description 欄於 001/005/006/009/010 與 Title、Verification Criteria 不一致，呈 +1 位移（詳 ANOMALIES A-ICS1）。請提供各 ID 正確原句 | 001, 005, 006, 009, 010 | OPEN |
| DR-ICS2 | SYS2 Traceability 列 SWE1-ICS-011（HU Screen ON）、012（Rear View Camera Transition），需求分頁缺列。請補列或確認撤銷 | 011, 012 | OPEN |
| DR-ICS3 | SYS-RA-ICS-001~012 於 SWRA 與 SYSAD Table 5 語意逐條不對應；Excluded 分頁另引 013/014/015 而 SYSAD 僅至 012。請確認以何者為準（A-ICS2） | 全 feature 追溯 | OPEN |
| DR-ICS4 | CFTS019 未提供（SWE-ICS-001/002 之 volume 母文，Description 明引） | 001, 002 | OPEN |
| DR-ICS5 | CFTS020 Functional Specification 未提供（僅收到 SYSAD）；CFTS022 物件 4915278 載 screen off 行為 according HMI and CFTS020（該物件本身屬 Atlantis Mid 域，僅作 CFTS020 為 screen-off 母文之佐證，非錨） | 006, 007, (011) | OPEN |
| DR-ICS6 | ICS_KNOB2（browse/tune）、Enter_Button、Back_Button 之 HMI Logic and Flow 母文未提供；CFTS022 無對應物件 | 003, 004, 008, 009 | OPEN |
| DR-ICS7 | `<Tstuck_button>` 具體值確認。CFTS022-4914956（HU）= 120 s、4914954（SCCM）= 10 min；SWRA 寫可組態。首波暫採 120 s（R-ICS3） | 010 | OPEN |
| DR-ICS8 | 本 feature 未綁定 DBC。ICS_KNOB1_VAL/DIR、ICS_KNOB2_VAL/DIR、ICSMuteButton、ICSPowerButton、ICSScreenOffButton、Enter_Button、TGW_DISP_STAT、RQ_DISP_INTS 無 MESSAGE 前綴與 VAL_ 列舉，無法套 IN §8.7.5(a) | 全部訊號欄 | OPEN |
| DR-ICS9 | DUT 之 CFTS022 ECU 屬性歸屬：Stuck Button 物件列 `ICS`，Volume 物件（4914972–76）僅列 `LTM/ETM/RRM`。暫採 `{ICS, LTM}` 聯集（R-ICS2），請上游確認邊界 | 適用域 | OPEN |
