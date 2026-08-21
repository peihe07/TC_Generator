# 上繳 02：Power Management 全項回修（批 1）

執行層：Opus5（Claude Code）｜日期：2026-08-21｜新規 0 條
工作副本：`features/power/sandbox/b02/pm_remediated.xlsx`（**未交付，待 Pei 覆核**）

## 1. 驗收對照

| 項目 | 目標 | 實測 | 判定 |
|---|---|---|---|
| P（三件組殘留，四欄） | 0 | **0**（前 41） | 達成 |
| J（行首大寫） | 0 | **0**（前 2） | 達成 |
| L（上半 >50 token） | 0 | **0**（前 71） | 達成 |
| I-sibling | 0 | **0**（前 104） | 達成 |
| D / G / K / M / N / B | 不得變動 | 0 / 0 / 0 / 0 / 0 / 0，全數未動 | 達成 |
| A | 不得變動 | 20 → 20，未動 | 達成（下放包載「A=0」有誤，見 §6） |
| E | 維持 0 | 0 → 0 | 達成 |
| F / H | 維持原值 | 0 / 0，未動 | 達成 |
| C | 維持原值 | 3 → **2** | **未達成**，原因見 §6 |

P 之前值 41 = 附件第一節七種訊號於 pre/input/proc/er 四欄之出現次數合計
（10+6+4+4+4+1+12），與附件「出現」欄逐項相符。

## 2. 逐項改動

| 項目 | 裁決 | 改動列數 | 改動格數 |
|---|---|---:|---:|
| M3 訊號記法（四欄） | R-1 | 42 | 42 |
| M11 首字大寫 | R-4 | 2 | 2 |
| M15 sibling 區分 token | S4 | 104 | 104 |
| M10 test_item 摘句 | R-3 | 71 | 71 |
| **合計（去重後）** | | **154 列** | **188 格** |

M10 與 M15 之 71／104 列有交集，故格數 188 > 列數 154；同列之 test_item
若同時受 M10 與 M15 影響，合併為一次寫入。

### M3（42 格）

CAN 七種逐字照附件改三件組，含 A-PM01 之 `Radio_Btn0` → `Radio_btn0`
大小寫更正（12 次出現、10 列）。內部訊號 A-PM02 `PhoneCall.Info` →
`Phone_Call.Info`（列 51、83、84、86、107，共 5 列）。
A-PM03 `$Radio_Theme$`（4 列）維持 `$...$` 未套三件組。

### M15（104 列，42 組）

區分 token **一律自該列既有欄位之實測差異逐字取得**，不臆造：
比對順序 pre → input → proc → er，取組內內容不一致之行；
單欄無區分力之多軸 sibling 再取雙欄組合。來源分佈：
pre 22 組、input 12 組、proc 6 組、pre+proc 1 組、pre+input 1 組。
**未解 0 列** —— 42 組全數可由實測差異區分，無「差異無法辨識」者，
故無待覆核標記。

寫法：`(<token> — <原括號內容>)`，原內容逐字保留。前置而非附加，
因 canon §4.3 明訂「the tag IS the distinguishing token」。

token 自 **M3 之後**的欄位推導，以免把舊式 CAN 記法帶回 test_item
（如 row 57 之 token 為 `Drive Radio_btn0 in CLIMATIC_PANEL on BH-CAN …`）。

### M10（71 列）

摘句規則依 canon §4.3.1「以與括號下半之測試目的直接相關之句為限」：
切段（行 → 句 → 子句 → 逗號，僅在該層仍超限時往下切）→ 以與括號下半之
實詞交集評分 → **只取相關度 > 0 之段**（零相關之段不得因「還有額度」混入）
→ 依原文順序輸出。段落逐字保留，不改寫、不縮寫。

兩項結構性處置：
- **表格型 verbatim 之首行為狀態鍵**（如 `Full-Operation` / `Timed`），
  設為必留錨。否則 rows 12／23 這類「同一張表不同狀態列」摘句後將逐字
  相同，反而製造 sibling 不可分。
- 摘句係自原句中段起抄，依 **R-4** 對句首字母作大寫正規化。

token 數：中位 88 → 摘句後全數 ≤ 50，最大壓縮 266 → 48（row 187）。

## 3. 非目標欄零變動之證明

全工作簿逐格比對（10 個 sheet、所有非空格）：

```
變動格數 188｜涉及 sheet {'Test Case Specification&Result'}｜涉及欄 ['I','J','K','L']
非目標欄變動：無
新增/刪除之格：0
計畫變動 188 格｜實際 188 格｜相符：True
```

I/J/K/L = test_item / pre / input / proc。**M 欄（er）零變動** ——
七種 CAN 訊號於 er 欄無出現。計畫與實際逐格相符，無非預期寫入。

## 4. x14 下拉驗證（寫回後讀回）

```
patched sheets: {'Test Case Specification&Result': 188}
zip members: 42   differing: ['xl/worksheets/sheet6.xml']
data-validation counts: {'sheet5.xml': (1, 0), 'sheet6.xml': (3, 1)}
x14 dataValidation (src): 1   →   (out): 1
```

zip 成員 42 個全數保留、僅目標 sheet 之 XML 相異、classic 與 x14
下拉計數逐 sheet 相等。寫入路徑為 `backend/xlsx_surgical.surgical_save()`，
**全程未呼叫 `Workbook.save()`**。

sha256：來源 `c80ee6da…c2` → 工作副本輸出 `cfda6769…aa`。
**交付檔全程唯讀，執行前後 mtime 未變。**

## 5. 抽驗結果

**CAN 七種各抽 1 列比對附件**（附件即 DBC 實查之唯一依據）：
7 / 7 相符，舊式記法於該格全數消失。例：
row 57 proc `Drive CLIMATIC_PANEL.Radio_Btn0 from …` →
`Drive Radio_btn0 in CLIMATIC_PANEL on BH-CAN from …`。

**M15 抽 10 列**：10 / 10 之 token 均可逐字對回該列該欄（M3 後之值），
且均已寫入括號下半。另對**全 104 列**做同一比對，失敗 0 列。

**M10 抽 8 列**（rows 12、68、136、189、210、219、236、276）：
8 / 8 之每一保留段落均可逐字回指原文（首字大寫還原後比對），
且括號下半未被 M10 改動。

**A-PM02 殘留檢查**：`PhoneCall.Info` 於四欄殘留 0 處。
**A-PM03 殘留檢查**：4 列 `$Radio_Theme$` 無一被套三件組。

## 6. 未達成項與偏離（3 項）

### (a) C 由 3 降為 2 —— 未維持原值

row 39 之 hedge `properly` 位於被 M10 摘掉的子句內：

```
前：After a battery reconnection … TLM is able to work properly again and it has to
    restore the last user settings and the last variables values: VPLastStatus, …
後：VPLastStatus, SwitchOffSetting.Req, Auto_SwitchOn_Setting.Req shall be restored
    to their values before the battery disconnection / battery reset
```

該列括號下半為「read the three stored variables -> VPLastStatus,
SwitchOffSetting.Req and Auto_SwitchOn_Setting.Req read their values …」，
摘句取直接相關之子句係依 R-3 應為之處置；被摘掉的前半恰含該 hedge。
**要維持 C=3 就必須刻意保留一段與測試目的無關之文字，與 M10 相牴觸。**
本包選擇遵 M10，變動方向為減少違規。row 32（`properly`）與
row 147（`Successfully`）之 hedge 皆保留，未受影響。

### (b) 下放包載「A=0（PM 原即清零）」與實測不符

PM 之 A 於 00c 報告即為 **20**（列 15、86、128、178、205、210、225、
238、242、255、256、257、275–281、292），非 0。本包未動 A，前後皆 20。
下放包該句之前提有誤，惟「不得變動」之實質要求已滿足。
A=20 屬既有違規，不在本包範圍，未處置。

### (c) M3 之施用範圍限四欄，test_item 未改

附件之量測範圍即「283 列之 pre/input/proc/er 四欄」，且 canon §4.3.1
明訂 test_item 上半為**需求原句 verbatim**。改寫 verbatim 內之訊號記法
將破壞 verbatim 性質，故本包不動。

**殘留：18 列之 test_item 仍含舊式記法**
（`STATUS_BH_BCM2.RemStActvSts` 10、`CLIMATIC_PANEL.Radio_Btn0` 6、
`STATUS_BH_BCM1.DriverDoorSts` 1、`STATUS_LIN.Batt_ST_Crit` 1）。
回修後之工作簿因此在四欄用三件組、在 test_item 用原文兩段式。
此為 R-1 與 §4.3.1 之界面問題，**須裁定**：verbatim 引用內之訊號記法
是否豁免 R-1。本包依 verbatim 優先處理並具名回報。

## 7. 未結 DR 清單

**本包新增 PENDING：0 處。** 附件第四節之 VF570 / VF601 / VF665 三份
未尋獲文件，本批確實未觸及其內容（M3 所需訊號全部命中附件對照表，
表外訊號 0 種），故未依 §8.4.3 開新 DR。

`features/power/DATA_REQUESTS.md` 現存未結 DR（本包未新增、未結案）：
DR-PW1、DR-PW3、DR-PW5、DR-PW7、DR-PW8、DR-PW10、DR-PW11
（DR-PW2 / PW4 撤回、DR-PW6 已結案）。VF570 / VF601 / VF665 於該檔
**尚無對應 DR 條目**，建議由分析層登記。

## 8. 本包是否仍有該驗而未驗者（獨立判斷）

**有，五項：**

1. **M10 摘句之「相關性」僅經詞彙層驗證，未經語意覆核。** 本包能自證
   摘句片段逐字出自原文、且與括號下半有實詞交集；**不能自證所取之句
   即需求之要旨**。已知弱例：row 32 之括號目的為
   `TLM_Status.Info -> "Sleep"`，而該列 verbatim 全文未出現 `Sleep`，
   摘句只能退而取分數最高之一段。71 列全數需人工覆核，本包僅抽驗 8 列。
2. **9 列摘句以連接詞起首**（rows 47、55、58、59、136、137、239、240、241），
   形如 `And STATUS_BH_BCM2…` / `Or if HU changes mode…`。係自原句中段
   起抄之必然結果，經 R-4 大寫正規化後 J=0，但可讀性不佳。
   刪除起首連接詞會改動 verbatim，R-4 只授權「首字母轉大寫」，
   未授權刪詞，故未處置。
3. **spec_reference 未依 R-2 改為 CFTS 家族格式。** 283 列現全為
   `R1LR_…_CFTS_009/010_…_{章節號}` 之 HMI 式格式。M10 稱「全文以
   specification_reference 指回（格式 `CFTS009-{ObjectID}`）」，
   但驗收清單無 spec 欄檢查，且僅改 71 列將使同一欄出現兩制、
   較全不改更糟。現值本身可回指到文件與章節，指回功能未失。
   **283 列之 R-2 遷移未做，須另包處理**（需 SWE-PM → Polarion
   7 位 ObjectID 之對照，本包未建立、未驗證）。
4. **A=20 未處置**（見 §6b），且 F=0 / H=0 / B=0 之「維持原值」係
   實測前後相等，非經逐列覆核。
5. **回修後之內容未經 Pei 之 R-P309 型授權。** 既有 `write_back_47.py`
   載明該授權「效力範圍為授權當時之 283 條內容，其後內容再有實質變動者
   不及於變動後版本」。本包變動 154 列之實質內容，**原授權不及於此**。
   本包止於工作副本，未複製回交付路徑、未動 ChangeHistory ——
   下放包 §完成後 Pei 動作 之兩步皆未代執行。

## 9. 引用之既有裁決

R-1（訊號記法三層，canon §8.7.5）、R-2（spec_reference 家族分流，§10.7，
見 §8 項 3 之未做聲明）、R-3（上半 50 token，§4.3.1）、
R-4（verbatim 首字轉大寫，§4.3.1）、S4（括號下半與 sibling 區分，§4.3.1）、
S6（缺件 PENDING，§8.4.3，本包 0 處）、
R16／R-G3（`surgical_save` 為唯一寫入路徑）、
R-P309（授權效力範圍，見 §8 項 5）、R-P42（未被引用之錨點不在範圍）。
編號落檔見 `docs/fw036/RULINGS_LEDGER.md` 與
`features/power/RULINGS.md`（R-P 系列）。

## 10. 產出檔案

| 路徑 | 內容 |
|---|---|
| `features/power/sandbox/b02/pm_work.xlsx` | 交付檔之位元組副本（來源，未改） |
| `features/power/sandbox/b02/pm_remediated.xlsx` | 回修後工作副本 |
| `features/power/sandbox/b02/edits.json` | 188 格編輯集與 M15／M10 推導紀錄 |
| `features/power/sandbox/b02/pm_remediated_20260821.md/.json` | 回修後 lint036 報告 |
| `features/power/scripts/b02/{edits,sibling_tokens,excerpt,build_edits,apply,verify,audit}.py` | 回修與驗收程式 |
