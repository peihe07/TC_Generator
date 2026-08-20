# ANOMALIES — FW036 Vehicle Setting

登記格式 `[A-VSnn]`。**Tier 1：登記，不裁定。**
本輪（00 包）之登記全部為執行層實測；標「沿用分析層」者為未複驗即照錄之項。

| id | 內容 | 證據 | 狀態 |
|---|---|---|---|
| A-VS01 | SYS-RA 指向 SYS2 之 `Heading` / `Information` 列 | **逐引用實測**：273 個可解析引用中 `Functional Requirement` **239**／`Heading` **25**／`Information` **9**。逐條見 `data/sysra_to_polarion.tsv` 之 `category` 欄 | 登記（數字與下放包預期完全相符） |
| A-VS03 | 四份 037 封面完全相同，無法區分 | 沿用分析層（00B §1）。**本輪未複驗** | 登記 |
| A-VS04 | CFTS044 內未填佔位 `{CFTS044-xxxx}` | 沿用分析層（00B §1.1）。**本輪未複驗** | 登記 |
| A-VS05 | `Heated_Seat_Levels` / `Heated_Seats_Levels` / `Heated_Steats_Levels` 三種拼寫並存 | **實測成立**：三者皆為 037 之 `$var$` token；對 3,000 個相異 LID 作**不分大小寫全字串**比對，`Heated_Steats_Levels` **無逐字對應** | 登記，RD-1 候選 |
| A-VS06 | body heading 270 對相異 `{7位數}` 254，差額 16 未追因 | **實測推翻其前提**：以 `word/styles.xml` 解出 heading 1–7 樣式後，body heading **270** 個，其 `{7位數}` **逐處 270、相異 270、差額 0**。254 係分析層在**轉檔文字**上以較寬形態量得（本輪同形態量得 逐處 444／相異 259，亦非 254） | **改寫為 A-VS06′**：原差額 16 於原始 docx 上不重現；254 為轉檔文字之產物 |
| A-VS07′ | DBC 檔名 `R4`／`R5` 在 `PDT27_E2A` 組指網段、在 `PDT25_E3A` 組指版本週次 | 沿用分析層（00H §1.1）。本輪複驗其 `PDT27_E2A` 側：兩檔 `VersionYear`=25、`VersionWeek`=50 **完全相同**，`BusType` 僅 FDCAN8 有且逐字為 `"CAN FD"` | 登記（FYI 類） |
| A-VS08 | `PDO Graphics Release` PDF 車型與主題皆與本 feature 無交集 | 沿用分析層（00C §3.1）。**本輪未複驗** | 登記 |
| A-VS09 | 26PI 版 Pop Up List 較 Comfort／User Profiles 基線新 | 沿用分析層（00D §5）。**本輪未複驗** | 登記 |
| A-VS10 | CFTS044 指名之 `TLM HMI Document` 於客戶 HMI 目錄無同名檔 | 沿用分析層（00D）。**本輪未複驗**（W-13 未執行） | 登記 |
| A-VS11 | 無 `PDT27_E2A` 組之跨版本比對表 | 沿用分析層（00H §2） | 登記 |
| **A-VS12** | **`SWE1-VC-HeatedSteeringWheel-009` 之 `Source Requirement ID` 逐字為 `SYS-RA-CFTS100`** —— 指向 **CFTS100**（非 CFTS044），且**無 `-N` 序號**，於 SYS2 解析不到任何列 | 實測。其為 271 leaf 中唯一取不到 7 位數 Polarion ID 者 | **新開**。下放包 §5.2 記其原因為「SYS2 該列 `Source Requirement items` 為空」——**原因不符**：SYS2 全 538 列之該欄無一為空，且此 leaf 根本解析不到列 |
| **A-VS13** | **`SYS-RA-CFTS\d+-\d+` 之正則使 `SYS-RA-CFTS100` 隱形** | 嚴格式得 273 引用、寬鬆式（`-N` 可省）得 **274**，多出者即 `SYS-RA-CFTS100`。故「273 全部指向 CFTS044」為真，但其為真之原因是**抽取式看不見反例** | **新開**。canon §5a 第 12 條之標準形態 |
| **A-VS14** | **5 個 leaf 對映到 >1 個 CFTS044 章節** | `SWE1-VC-LeftFrontHeatedSeat-004`／`-011` 各對映 4 章節（`1.3.2.1.3.1`–`.4`）；`SWE1-VC-HeatedSteeringWheelManagement-025`／`-026`／`-027` 各對映 2 章節（`1.3.2.1.3`；`1.3.3.3.6.1`） | **新開**。`specification_reference` 之單值形式對此 5 leaf 不成立 |
| **A-VS15** | **`Proxi & Configuration` 分頁無獨立之 `Atlantis High` 欄組** | 該分頁列 2 之欄組標題逐字為 **`Atlantis & Atlantis High`**（第 16 欄），而 `CAN Mapping` 分頁為 `Atlantis`(16) 與 `Atlantis High`(26) **分列** | **新開**。00G §4 之「10 個 Atlantis High 空欄」全數落在此分頁；**其非空欄，而是該表一欄兼管兩者且已自述** |
| **A-VS16** | **`Format` = `See Proxi Table` 之 LID 實測為 8，非 6** | 全簿（含十張車型專屬分頁）掃 `Atlantis High` 與 `Atlantis` 之 `Format` 欄：`Cooled_Seats`／`DSP_SK_PRSNT`／`EC_Mirror_HK_Prsnt`／`Heated_Seat_Levels`／`Heated_Seats`／`Heated_Steering_Wheel`／**`VC_TIRE_CIRCUMF`**／**`VC_VEH_BRAND`** | **新開**。多出之二者非本 feature 之 token，故「本 feature 用得到 4」不變 |
| **A-VS17** | **兩份 DBC 之 141 個共有 signal 中，128 個之起始位元不同** | 逐屬性比對 `SG_ name : start|len@order sign (factor,offset)`：128 / 141 之 `start` 不同（例 `ACV_FailType` BHCAN 55 vs FDCAN8 165） | **新開**。00H §5-3 自陳「同名不同定義本篇看不到」——**實測為常態而非例外**；TC 引用訊號時若不指明網段／DBC，起始位元即不確定 |
| **A-VS18** | **`recon.py` 之 leaf 數與 W-2 不符** | recon 讀單一 037（Common Features）得 `leaves=46`，而 W-2 對同一檔以「`Analysis Report`、表頭列 7、資料自列 8、A 欄非空」得 **56** | **新開**。差額 10 未追因；recon 之 leaf 判準與下放包 §5.1 不同 |
| **A-VS19** | **`new_feature.py` 之目錄名與 R-VS3 不一致** | `scripts/new_feature.py:144` 為 `feature.lower()`，不做空白→底線轉換；R-VS3 指定之指令 `"Vehicle Setting"` 產生 `features/vehicle setting`（**含空白**），而 R-VS3 同時指定目錄為 `features/vehicle_setting` | **新開**。已依 R-VS3 之目錄名為準，骨架複製至底線目錄；**空白目錄未刪，待 Pei** |
