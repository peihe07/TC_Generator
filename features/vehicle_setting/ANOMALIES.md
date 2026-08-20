# ANOMALIES — FW036 Vehicle Setting

登記格式 `[A-VSnn]`。**Tier 1：登記，不裁定。**
本輪（00 包）之登記全部為執行層實測；標「沿用分析層」者為未複驗即照錄之項。

| id | 內容 | 證據 | 狀態 |
|---|---|---|---|
| ~~A-VS01~~ | ~~SYS-RA 指向 SYS2 之 `Heading` / `Information` 列~~ | 逐引用實測 273：`Functional Requirement` **239**／`Heading` **25**／`Information` **9** | **除役（02 包 §1.4）** —— 以 037 之 `Categorization` 對 SYS2 之 `Category` **逐 leaf 交叉列表，零錯配**（Functional↔FR 236、Heading↔Heading 25、Information↔Information 9、CFTS100 那筆 NO_REF 1）。**那 25 個不是錯配，是同一批非需求列在兩份文件裡各自被正確標記。**當初登記為異常之成因：只讀了 SYS2 側，未讀 037 自己的 `Categorization`（第 6 欄） |
| A-VS03 | 四份 037 封面完全相同，無法區分 | 沿用分析層（00B §1）。**本輪未複驗** | 登記 |
| A-VS04 | CFTS044 內未填佔位 `{CFTS044-xxxx}` | 沿用分析層（00B §1.1）。**本輪未複驗** | 登記 |
| A-VS05 | `Heated_Seat_Levels` / `Heated_Seats_Levels` / `Heated_Steats_Levels` 三種拼寫並存 | **實測成立**：三者皆為 037 之 `$var$` token；對 3,000 個相異 LID 作**不分大小寫全字串**比對，`Heated_Steats_Levels` **無逐字對應** | 登記，RD-1 候選 |
| ~~A-VS06′~~ | body heading 270 對相異 `{7位數}` 254，差額 16 未追因 | **實測推翻其前提**：以 `word/styles.xml` 解出 heading 1–7 樣式後，body heading **270** 個，其 `{7位數}` **逐處 270、相異 270、差額 0**。254 係分析層在**轉檔文字**上以較寬形態量得（本輪同形態量得 逐處 444／相異 259，亦非 254） | **除役（05 包 §11）**。原記之差額 16 為轉檔文字之產物：原差額 16 於原始 docx 上不重現；254 為轉檔文字之產物 |
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
| ~~A-VS18~~ | ~~`recon.py` 之 leaf 數與 W-2 不符~~ | recon 46 vs W-2 56（Common Features）；全體 237 vs 271 | **除役（01 輪 W-16）** —— `scripts/recon.py:602` 為 `is_leaf = cat.lower().startswith("functional")`，依 037 之 `Categorization` 過濾；下放包 §5.1 之判準為「A 欄非空」，無此過濾。**二者非對同一件事給出不同答案，是兩個判準在數兩件不同的事**，且 recon 之判準與 036 之實際投影一致（036 之 237 列 = 237 個 Functional 列）。**recon 未錯。** |
| **A-VS19** | **`new_feature.py` 之目錄名與 R-VS3 不一致** | `scripts/new_feature.py:144` 為 `feature.lower()`，不做空白→底線轉換；R-VS3 指定之指令 `"Vehicle Setting"` 產生 `features/vehicle setting`（**含空白**），而 R-VS3 同時指定目錄為 `features/vehicle_setting` | **新開**。已依 R-VS3 之目錄名為準，骨架複製至底線目錄；**空白目錄未刪，待 Pei** |
| **A-VS20** | **037 之 `Categorization` 大小寫不一致** —— `HeatedSeat` 有一列為小寫 `information` | 逐字值分布：`Functional Requirement` 237／`Heading` 25／`Information` 8／`information` **1** | **新開（02 包 §1.3）**。⚠ **方向須說明白**：其影響 **`Information` 側之計數**（區分大小寫 8、不分 9），**不影響 Functional 母體之界定**（`startswith('Functional')` 區分與不分大小寫**皆得 237**）——該筆是 `information`，兩種寫法都不會被誤收進 Functional。`recon.py` 之 `.lower()` 在此**不是救了它，是恰好不需要救**。惟任何以 `== 'Information'` 分類之下游會少計一筆。RD-1 FYI 類，我方以不分大小寫吸收，不待上游修正 |
| **A-VS21** | **分析層經 MCP 讀取含中文之 repo 檔時，偶發單字元顯示為替代字元** | 曾兩度回報「檔案疑似毀損」（`ANOMALIES.md`「相異 259」後、`00 §1 第 6 點`「沙」後）；執行層位元層實測：嚴格 UTF-8 解碼**通過**、`U+FFFD` **= 0**，「沙」後三處皆為「箱」 | **新開（05 包 §11，工具類）**。⚠ **其危險不在顯示，在於它偽裝成資料之缺陷** ——若執行層照辦改寫，會把一個好的檔案改壞。**通則：跨層回報「檔案毀損」前須先以位元層確認，不得以讀取結果之外觀為據。** |
| **A-VS22** | **CFTS044 之 `$VentedSeatFL$` 值中出現 `Vented Seat Off / HS_OFF`**（`HS_` 為 Heated 之前綴，應為 `VS_OFF`） | 逐 token 抽值時命中；同一 `= [值]` 內之左式已定其為 VentedSeat | **新開（07 包 §3.2，W-21）**。規格筆誤，RD-1 FYI 類。**不影響取值** —— 左式已定其歸屬 |
| **A-VS23** | **LID 表之 `TGW_DISP_STAT` 值域有拼字錯誤 `diplay closed`** | W-19 逐值比對：DBC 作 `Display_closed`，LID 表 `Format` 欄作 `Diplay_closed`（缺 `s`） | **新開（03 輪 W-19）**。RD-1 FYI 類。⚠ **若以 LID 表之字串為 ER 之逐字值，會寫出一個匯流排上不存在的狀態名** |
| **A-VS24** | **CFTS044 以 `IGN OFF` 描述 `$PowerMode$`，而其匯流排訊號 `CmdIgnSts` 之值域無 OFF** | CFTS044 in-scope 值含 `IGN OFF`／`IGN OFF ACC`；DBC 與 LID 表之 `CmdIgnSts` 值域為 `Initialization`／`IGN_LK`／`ACC`／`RUN`／`START`／`SNA` —— **無任何 OFF** | **新開（03 輪 W-19）**。⚠ **非拼字差異，是狀態不存在** —— 引用 `$PowerMode$ = IGN OFF` 之條文，其 ER 無法以 `CmdIgnSts` 之單一值表達。待判：是否對映至 `IGN_LK`，或另有他訊號承載。**登記待判，不自行對映** |

