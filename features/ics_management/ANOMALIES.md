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
