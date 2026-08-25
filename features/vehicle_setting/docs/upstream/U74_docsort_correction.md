# 上繳 U74 — **W-VF92 之排序鍵模型為假**；已依「來源文件 → 文件內編號」重排並送交付路徑

**所據**：Pei 之指正（2026-08-25）「同一份文件的排在一起照數字順序去排」
＋ 文件序之裁定（**文件名字母序**）
**日期**：2026-08-25

---

## 〇、本包對交付物之推進（R-G31）

**有：交付本之列序已更正並就位**（`adee5dc4…f8e27`，457 列，11 段）。

---

## 一、**W-VF92 錯在哪裡**

`R-G32` 首版之措辭「**family 名依字母序，數字尾碼依數值序**」
**內含一個未經查證的模型**：預設 ID 之名為分群單位、尾碼為該名下之流水號。

**實測其為假**（`data/vf230_leaves.tsv`，627 leaf）：

```
11 份 037 分報告，**每一份之編號皆自 002 起編至該份長度**
   131 條 | 002-138 | STLA_Trailer_Name - Max_Power_Level_Report
    99 條 | 002-119 | Blind Spot Alert_Passive Entry_Phone Repetition_Park Sense_features
    79 條 | 002-095 | Time_Date_Autodoor_Camera_features
    …

上游列號與之平行遞增 —— **同一份文件內，不同名之需求編號連續**：
   SYS-RA-VF230_V1-672 → SWE1-VC-BlindSpotAlert-002
   SYS-RA-VF230_V1-673 → SWE1-VC-BlindSpotAlert-003
   SYS-RA-VF230_V1-679 → SWE1-VC-**PassiveEntry**-009
```

**故 `-NNN` 是該條在其分報告內之行號，不是「該名下的第 N 條」。**

**依 D 欄整字串排序之後果（實測）**：

```
11 份文件 → 被切成 **74 段**（平均每份散在 **6.7** 處）
文件內編號之逆序 **43 處**（457 列中）
```

**已登記 `A-VF34`（新開即結案）。**

---

## 二、**為什麼五道閘全綠而結果是錯的** —— 本包最該記的一件事

W-VF92 之閘：閘 0（尾碼位數一致）／閘 3a／3b（結構不變式）／
閘 4（457 × 16 逐欄）／新閘（D 欄非降序）—— **全過，且過得沒有勉強。**

**因為那些閘全部以該假模型自身為判準。**

- 閘 0 驗的是「**尾碼位數一致，故字串序即數值序**」——
  **驗了鍵的形式，沒問「尾碼是相對於什麼而編」。**
- 新閘驗的是「D 欄非降序」—— **那正是錯鍵自身的定義**，
  **一個由錯模型導出的閘，對該錯模型必然全綠。**
- 閘 4 驗的是「重排沒改動任何值」—— 這是真的，**而列序錯不錯它管不著。**

**其被發現之途徑：Pei 打開交付本用眼睛看。非任何機制。**

**`R-VF136`「合法 ≠ 可用」之第六次** —— 且**本次是機械判準全綠而結果為錯**，
為該條至今最強之一次實例。**前五次是「未驗」，這一次是「驗了，而驗錯了東西」。**

**通則（建議入條）**：
**排序鍵、分群鍵之語意須向資料查證，不得自 ID 之外形推得** ——
**「名 + 數字」之外形不蘊含「數字是名的序號」。**

---

## 三、`R-G32` 之修正（已落檔）

`docs/fw036/RULINGS_LEDGER.md` 之 `R-G32` **加註修正段**（原文保留，`R-TM13`）：

```
第一層  上游來源文件（037 分報告 / 等同單位），依文件名字母序
第二層  該條在該文件內之編號（ID 結尾數字，不論有無連字號）升冪
        同鍵者 stable
判準    **每一份來源文件恰佔一段，且段內編號非降序**
```

**判準寫關係、不寫實例數** —— 即 V73 §2 之教訓（`R-VF114`）於本輪之正面套用。

---

## 四、重排之結果

**腳本**：`scripts/vf230_reorder_by_document.py`
（**import `vf230_wvf92_reorder` 之工法與閘，不複製**；只換鍵、換不變式）

```
[閘 0] 資料列 457（列 10–466）｜B 244–700 連號｜文件 **11** 份
       文件內編號撞號而 ID 相異者 **0**（否則「照編號排」無定序）
[量測] 重排前 文件段數 **74**（平均散 6.7 處）｜文件內編號逆序 **43**
       重排後 文件段數 **11**（= 份數）｜文件內編號逆序 **0**
[閘 3a] xlsx_surgical.verify_structure：**通過**（相異 part 恰 1）
[閘 3b] dv 6｜x14 2｜cf 1｜probe 2｜part 48    **前後全一致**
[閘 4] 重讀比對 457 列 × 16 欄（B 除外）：**差異 0**
[新閘] (文件, 編號) 逐列非降序 **違者 0**｜文件段數 11 = 份數 11
[新閘] B 欄連號 244–700 True
```

**獨立複驗（跨兩次重排，比對最原始之本）**：

```
內容多重集合（B 除外）與 **W-VF92 之前之本** 相同：**True**
   → 二次重排合計未增、未減、未改動任何一格之值
```

**文件之序（Pei 所擇：文件名字母序）**：

```
 1.  33 條  6 Aux Switches, SWITCH 1 Power Mode and E-Save features
 2.  92 條  Blind Spot Alert_Passive Entry_Phone Repetition_Park Sense_features
 3.  27 條  Cornering Lights_lane_features
 4.  14 條  Daytime_Running_Light And Headlights_Off_Delay features^
 5.  17 條  Pressure_Unit , Power_Unit And Torque_Unit features
 6.  50 條  STLA_Illuminated_Approach - Trailer_Number_Report
 7.  23 條  STLA_SWITCH_1_Type - SWITCH 4 Hold_Last_State Features_Report
 8.  33 條  STLA_Suspension_Flash_Lights_With_Lower - SWITCH 4_Power_Mode Features_Report
 9.  49 條  STLA_Suspension_Service_Mode - Headlights_with_Wipers Features_Report
10.  93 條  STLA_Trailer_Name - Max_Power_Level_Report
11.  26 條  Time_Date_Autodoor_Camera_features
```

**一處可注意**：該序為 ASCII 字母序（大寫先於小寫），
故 **`STLA_SWITCH_1_Type…` 排在 `STLA_Suspension…` 之前**。
**其為 Pei 於選項預覽中所見並所擇之序**；若欲改為不分大小寫，
`DOC_KEY` 一處即可，**其只動文件之間，段內一列不變**。

---

## 五、對照表改為**三段式** —— 兩次重排之 B 號皆不斷鏈

```
data/vf230_id_remap.tsv   457 列
  b_orig    量產原序（W-VF92 之前）—— pilot 紀錄、DR、隔離表所引者
  b_wvf92   W-VF92 之後（依 ID 字串排；曾短暫送達交付路徑 16:49–19:11）
  b_final   現行交付本
  req_id    D 欄
```

**三欄各自唯一、值域皆 244–700**；
`b_orig`→`req_id` 與量產原序之本一致 **True**、
`b_final`→`req_id` 與現行本一致 **True**。

**若只記本輪，第一次重排之舊 B 即斷鏈** —— 故 `write_remap()`
自現存表接續 `b_orig`（本輪接續 **457** 筆），**且其 `new_b` 與工作簿之 B
不吻合時即停**（鏈斷之偵測）。

---

## 六、交付路徑（**已就位**）

```
19:11  交付路徑 ← repo 內本   adee5dc4…f8e27   186,452 bytes   **二本 sha256 相同**
       覆蓋前為 W-VF92 之本   67256f58…07d4cb（其保留於 _vf230_036_docsort_backup.xlsx）
```

**逐字具名檔名複製**（`R-VF112`；複製屬 Pei，本輪循其先前之即令代執行，具名不視為通例）。
**複製前實測 Excel 未持有該檔**（無 `~$` 鎖檔、`lsof` 無輸出）。

**備份現為四個**（本輪新增第四個）：

```
_vf230_036_prewrite_backup.xlsx     82,467 bytes  寫入前（0 列）
_vf230_036_append_backup.xlsx      186,784 bytes  補入前（438 列）
_vf230_036_reorder_backup.xlsx     191,421 bytes  **量產原序（457 列）** ← b_orig 之對應本
_vf230_036_docsort_backup.xlsx     189,846 bytes  W-VF92 之本（依 ID 字串排）
```

**四個皆不刪** —— `_reorder_backup` 為 `b_orig` 之唯一實體對應物，
`_docsort_backup` 為 `b_wvf92` 之唯一實體對應物；**對照表之二欄若無對應本即不可複驗。**

---

## 七、本包是否仍有該驗而未驗者（canon FO §8.2）

**有，四項。**

1. **重排後之工作簿仍未經人以 Excel 開啟確認** —— 本輪之驗證仍全為機械判準。
   **且 §二 已證機械判準全綠不蘊含結果正確。** **只有人眼能驗。**
2. **「11 份分報告」之單位本身未經 Pei 確認為正確之分群單位** ——
   本層取 `vf230_leaves.tsv` 之 `family` 欄為文件。**實測其中 3 份之編號
   於中途自 002 重來一次**（如 `MaxPowerLevel143` → `TrailerName-002`），
   **即該 3 份實為二份分報告合併之檔名**。
   **本輪不切細**（切細則文件數由 11 增為 14，且其序須另裁）——
   **現行排序下該 3 份內部未交錯**（各名之段數 = 名之相異數），故不影響可讀性，
   **惟「一份文件」之定義於該 3 處與檔名不符，具名之。**
3. **`autoFilter A9:AH132`** —— 狀態不變（`BACKLOG` B2）。
4. **19 條之 `test_item` 內容未經人讀** —— 狀態不變（`BACKLOG` A1）。

---

## 八、給 Pei

**你看出來的那件事，我的五道閘一道都沒攔到，因為那五道閘全部是用錯的模型自己導出來的。**
**攔下它的是你打開檔案用眼睛看。**

現在的樣子：**11 份分報告各佔一整段，段內編號從小到大，一路不跳。**

```
B244  SWE1-VC-6AuxSwitches-002        ┐
B245  SWE1-VC-6AuxSwitches-003        │ 6 Aux Switches, SWITCH 1 Power Mode…
B246  SWE1-VC-SWITCH5PowerMode-021    │  （33 條）
B249  SWE1-VC-SWITCH6PowerMode-025    ┘
…
B700  SWE1-VC-SuspensionAutoEntryorExit-092
```

**交付路徑已經是這一份了**（19:11）。**剩下的還是那一步：用 Excel 開來看。**
四個備份在確認前一律不動。
