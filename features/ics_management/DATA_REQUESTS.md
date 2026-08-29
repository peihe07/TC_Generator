# ICS Management — DATA_REQUESTS

發出日：2026-08-29（Pei 准，下放包 01）。每包上繳附未結 DR 清單。
未結期間，受阻欄位一律 `PENDING: DR-ICS{n} <缺件名>`（IN §8.4.3）。

> **本檔只有一個登記表**（R-ICS29）。狀態一律寫於 `狀態` 欄，
> 不另立過渡表。過去之「狀態重排」表已於 2026-08-29 併回本表並刪除
> （成因與拿法見 A-ICS45）。
> `狀態` 欄之值域：`OPEN` ／ `可結`（授權，佔位實際回收後方改）／ `CLOSED`。

**催件排序（Pei 2026-08-29「裁」核可，2026-08-29 重排）**：
- 上游急件：**DR-ICS18（§1.8／§1.18 權威歸屬及 TLM 之指涉；2026-08-29 新登）**、**DR-ICS16（DISP_STAT 家族零承載，二條路皆確認不通）**、DR-ICS9（V 組存續）、DR-ICS2（011/012 補列）
- 緩件：DR-ICS3（交付前須結，ASPICE 追溯鏈）、DR-ICS4／DR-ICS14（CFTS019 線）、DR-ICS6、DR-ICS11
- 待偵察：DR-ICS17（b07）
- 可結待回收：DR-ICS5／7／8／10／13／15

<!-- LEDGER-IGNORE-BEGIN -->
## 狀態重排（Pei 2026-08-29「准」，自解檢查後）

實測後重排，詳見 R-ICS22 v2／R-ICS24／R-ICS25 與 A-ICS34／35。
下表為現行狀態，與各列之 `狀態` 欄不一致時，**以本表為準**（b06 後合並）：

| DR | 新狀態 | 依據 |
| --- | --- | --- |
| DR-ICS1 | **降為帳面修正件**（阻斷面歸零） | R-ICS25(c)(d)：005 已解鎖 |
| DR-ICS5 | **可結**（檔在 inputs、R-ICS9 已採用） | A-ICS9 |
| DR-ICS7 | **可結**（120 s 三源互證：4914956、DTC Matrix r57、CFTS020 定義塊） | R-ICS24(b) |
| DR-ICS8 | **可結**（九個 LID 全解；殘項轉 A-ICS30） | upstream-04 §3 |
| DR-ICS10 | **可結**（`<Tstuck_button> = 120 sec` 逐字） | R-ICS24(b) |
| DR-ICS12 | **可結**（`= initial value 50 msec`／`= 20 msec` 逐字；reasoning 須註 initial value） | R-ICS24(c) |
| DR-ICS13 | **可結**（市場軸承接 R-DD25(a)：NAFTA 在案） | R-ICS25(a)(b) |
| DR-ICS15 | **可結**（2 解、2 併入 DR-ICS16） | upstream-04 §3 |
| DR-ICS16 | **降為確認件**，不再阻斷 | R-ICS22 v2(d) |
| DR-ICS17 | **待 b06 偵察**（`Notifications HMI L&F R1L-R (Feb 13 2026)` 為候選，未判同一） | 分析層 2026-08-29 量測 |
| DR-ICS2、3、4、6、9、11、14 | **維持 OPEN（真上游件）** | — |

結案一律以 b06 之實測為準：佔位實際回收後方改 `CLOSED`，
本表之「可結」為授權，非已結。

**催件排序（Pei 2026-08-29「裁」核可）**：- 上游急件：DR-ICS9（V 組存續）、DR-ICS10（ignore 門檻）、DR-ICS1（縮圍版：俟 b02 偵察定 006/009 可否繞過後發，005 恐繞不過）、DR-ICS2（011/012 補列）
- 緩件：DR-ICS3（交付前須結，ASPICE 追溯鏈）、DR-ICS5（與 A-ICS13 版本問併送）、DR-ICS7（純確認）
- 內部收口中：DR-ICS8（b02 作業 A，R-ICS8／13）、DR-ICS4（R-ICS11 綁 audio_mgmt 原件，上游只剩版本確認）

<!-- LEDGER-IGNORE-END -->

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
| DR-ICS13 | 【新登 2026-08-29，見 R-ICS15(b)】本專案（newR1L／R1L-R，Atlantis High）之 **市場軸**為何？CFTS020-4819554（Back_Button 唯一直載原句）之 Market 限 NAFTA；市場軸未定前不得判其在案（R-DD25 同族）。順帶確認 CFTS022／CFTS020 之 `Market` 屬性於本 DUT 之採認值域 | 009；及後續所有帶 Market 限定之物件 | OPEN（**改問 2026-08-29**，R-ICS25 v2(c)：009 之阻斷面實在 Radio／EE 二軸而非 Market。現問「請提供 ICS／HU 側之 Back_Button 行為母條，或確認 009 出案外」。**2026-08-29 R-ICS35(g)**：Pei 裁 ③（二節並存）**不使本 DR 結案** —— §1.18 側之 `4821681` 為 LID 清單非行為母條，`4821704` 主詞為 TLM，其可用與否繫於 DR-ICS18／b09 作業 A 之 TLM 指涉量測；009 於其定案前不生成） |
| DR-ICS14 | 【新登 2026-08-29，上繳包 03 §七-2、§12-2-4】CFTS019 七件之引用鏈有五個斷點文件不在件內：`TABLE 34`（音量曲線，自 Radio Performance Standard 轉引）、HU Component Specification、`4866125` 所指之未具名 HMI 文件、CIP Radio DSPPP 表、`Table for CFTS019-4866516`。請提供或指明其所在 | 001, 002（音量階數域） | OPEN |
| DR-ICS15 | 【新登 2026-08-29，上繳包 03 §四-3】`$TGW_DISP_STAT$`、`$RQ_DISP_INTS$`、`$DCSD_DISP_STAT$`、`$Telematic_Power$` 四訊號不在 LID 點名清單，b03 共 14 處佔位。已令 b04 依 R-ICS8 進 LID→CAN 驗證；驗證後仍查無者以本 DR 向上游要對應 | 006, 007, (011) 之訊號欄 | OPEN |
| DR-ICS16 | 【新登 2026-08-29，見 A-ICS28／R-ICS22(a)】`$TGW_DISP_STAT$` 與 `$Telematic_Power$` 於 B-CAN（`TELEMATIC_DISPLAY2` @1500／`STATUS_TELEMATIC` @1470）與 CAN-FD（`TELEMATIC_FD_4` @1427）二條匯流排上均有承載。**本 DUT 於哪條匯流排上觀察該二訊號？** 二候選發送節點皆非 ICS，台架取捨無量測依據 | b03 之 12 處佔位 | OPEN（**升回阻斷件 2026-08-29**，見 A-ICS47：ETM=DUT 不成立；若 DUT 為 LTM，二 DBC 皆無其發送側。b08 須查 §1.18 是否有解） |
| DR-ICS17 | 【新登 2026-08-29，upstream-04 §6-1】`Pop-up List Notification`（由 `Pop Up List Priority Matrix` p.3 逐字外指之文件）**不在 `spec-index/sources/` 33 件內**。請提供。理由：`VOLUME POP_UP` 之顯示條件連續四包追索（CFTS022／020／019 七件／ HMI L&F 六本）皆強查無，線索首次收斂至此一具名而未入庫之文件 | b01 之 V1／V2／V3 共 6 行 ER（A-ICS16） | OPEN（**線索移轉 2026-08-29**：upstream-07 §8 實測 Notifications 本不支持為該文件，且其 p.2／p.3 反向外指 `HMI Pop Up List`（亦不在 33 件內）。現請提供 `HMI Pop Up List`） |
| DR-ICS18 | 【新登 2026-08-29，R-ICS35(d)】CFTS020 二節之權威歸屬：§1.8（`PNet & AtlHi & AtlMi`）與 §1.18（`AtlMi & AtlHi & AtlLo`）對本 DUT（newR1L／R1L-R，Atlantis High）係**並存（各有涵蓋面）**、**取代關係**、或**適用條件差異**？附受影響之 25 條 TC 與 15 個 CFTS020 錨清單（`docs/reports/08_s118_vs_s18.md` §5）。**一併請確認**：§1.18 所稱之 `TLM` 是否即本 DUT（其 §1.18.1.2 逐字載 TLM 有畫面、有 `"Screen Off"` 模式、須管 browsing lists），及其與 ECU 屬性 `LTM`／`ETM`／`RRM` 之關係（連帶 DR-ICS9） | 13 條之錨歸屬；009；A-ICS55 之泛用母條處置 | OPEN |
