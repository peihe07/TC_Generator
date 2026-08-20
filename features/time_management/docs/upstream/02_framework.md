# 上繳 02 — A-TM02a 升級、037 檔名複驗、leaf→章節對映

執行層 → 分析層。對應 `docs/handoff/02_framework.md`。
**僅回報差異。** 2026-08-20。

## 0. 一項逕行 —— R-TM13 之登記未見於 T1–T4 指派

02 包 §4 自檢表列 R-TM13 為本包新條文，但 §3 之 T1–T4 **無登記它的指派**
（與 `01Z-A4` 漏掉 A-TM02a 同型）。

**執行層逕行登記**，理由：條文逐字寫入 `RULINGS.md` 為歷來每包之常規
義務（`00` §4(1)、`01` §1、`01Z-A2` T5(3)、`01Z-A4` T1），且本包
「不得執行者」未含相關限制。**與 `01Z-A4` 之 A-TM02a 情形不同** ——
該次 A4 明文寫「四項數字不符即回報，不自行調整」，故僅提請未逕改。

`RULINGS.md` 現為 **16 條**（15 + R-TM13）。若分析層認為不應逕行，回覆即撤。

**本條已即時適用於本包**：A-TM11 舊提案段之保留處置早於本條成文，
本條為其追認。

## 1. T1 — A-TM02a 升級

**索引列**

```
改前：| A-TM02a | 037 之版本身分未定（原 A-TM02，經 R-TM6 分拆） | PENDING | Tier 3（隨 RD-1 上問） |
改後：| A-TM02a | 037 之版本身分未定（原 A-TM02，經 R-TM6 分拆）—— **阻塞 D5 交付欄位** | PENDING | Tier 3（隨 RD-1 上問）|
```

**條文**：「性質升級」段已逐字追加於 A-TM02a 末尾（原「執行層建議」段之後）。

**T4(4) 索引條數複查**：`^| A-TM` = **16**，`^## A-TM` = **16**。
T1 未增條數，符合預期。

## 2. T2 — 三個 037 檔名複驗：**與分析層實測完全相符**

純目錄列舉，未開啟任何檔案。四個目錄之完整結果：

```
=== Core HMI/HomeHMI/ ===
FM-WI-FSM-036-A01 …_SWQT_Home_20260809.xlsx
FM-WI-FSM-037-A03-N1L-SWE1-Home-HMI-V0.1 STLA 報告.xlsx
REF

=== Core HMI/Menu Bar and AppDrawer/ ===
FM-WI-FSM-036-A01 …_SWQT_AppDrawer_20260729.xlsx
FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-HMI-V0.1 STLA 報告.xlsx
REF

=== User Profiles/ ===
FM-WI-FSM-036-A01 …_SWQT_UserProfiles_20260820.xlsx
FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx
REF

=== Time Management/ ===
R1LR_Atl-H_25PI3.5_Cabin_CFTS _015 Time and Date _SR26_20250909-1851.docx
SWE1_Secure_Date&Time.xlsx
SYS2_CFTS_015_Time and Date _SR26_V1_Including_Delta_Released.xlsx
```

**判準逐項核對**：

| 判準 | 結果 |
|---|---|
| 前三者各恰一個 `FM-WI-FSM-037-A03-N1L-SWE1-*-HMI-V0.1 STLA 報告.xlsx` | ✅ 各恰一個 |
| `Time Management/` 無任何 `FM-WI-FSM-037-*` | ✅ 零 |

A-TM16 之追加行已寫入（`ANOMALIES.md:935`）：

> **（2026-08-20）執行層以純目錄列舉獨立複驗三個 037 檔名，與分析層實測相符。
> 本條之檔名形態論證自此為雙方確認，非單方實測。**

### 2.1 附帶確認（非判準，但值得記錄）

`Time Management/` 之三個檔案**恰為本 feature `inputs/` 內之三份素材**
（檔名逐字相同）。此確認了素材之來源路徑，並印證 A-TM02a：該目錄下
**連 036 工作簿都沒有**，與 R-TM5「改以母本為之」之處置一致 ——
本 feature 之交付目錄從未有過客戶預填件。

## 3. T3 — SWE leaf → 章節對映（22 列全表）

輸出保留於 `data/leaf_to_section_probe.txt`。

```
leaf                       sections                                 #SYS-RA
SWE-RA-TIME&DATE-001       1.3.1.1.2,1.3.1.1.5.2,1.5.2.3                  4
SWE-RA-TIME&DATE-002       1.3.1.1.2,1.3.1.1.3,1.5.2.3,1.5.2.4            6
SWE-RA-TIME&DATE-003       1.3.1.1.2,1.5.2.4,1.5.2.5                      3
SWE-RA-TIME&DATE-004       1.3.1.1.3,1.3.1.1.4,1.5.2.4,1.5.2.5            4
SWE-RA-TIME&DATE-005       1.3.1.1.3                                      2
SWE-RA-TIME&DATE-006       1.3.1,1.3.1.1.2                                3
SWE-RA-TIME&DATE-007       1.3.1.1.2,1.3.1.1.5,1.3.1.1.6.3                4
SWE-RA-TIME&DATE-008       1.3.1.1.2,1.3.1.1.4,1.5.2.1,1.5.2.4            7
SWE-RA-TIME&DATE-009       1.3.1.1.2,1.3.1.1.4,1.3.1.1.6.2                9
SWE-RA-TIME&DATE-010       1.3.1.1.5                                      2
SWE-RA-TIME&DATE-011       1.3.1.1.5.1                                    3
SWE-RA-TIME&DATE-012       1.3.1.1.5.3                                    2
SWE-RA-TIME&DATE-013       1.3.1.1.5.4                                    1
SWE-RA-TIME&DATE-014       1.3.1.1.6.1,1.5.2.5                            3
SWE-RA-TIME&DATE-015       1.3.1.1.6.1,1.3.1.1.6.2,1.5.2.6                6
SWE-RA-TIME&DATE-016       1.3.1.1.6.2                                    2
SWE-RA-TIME&DATE-017       1.3.1.1.6.2,1.5.2,1.5.2.3,1.5.2.4              4
SWE-RA-TIME&DATE-018       1.3.1.1.6.2,1.5.2.6,1.5.2.7                    3
SWE-RA-TIME&DATE-019       1.3.1.1.1,1.5.2.6                              3
SWE-RA-TIME&DATE-020       1.5.2.2,1.5.2.3,1.5.2.4                        4
SWE-RA-TIME&DATE-021       1.5.2.2                                        1
SWE-RA-TIME&DATE-022       1.3.1,1.5.2.1                                  2

sections by leaf-count: 1.3.1.1.2:7  1.5.2.4:6  1.3.1.1.6.2:5  1.5.2.3:4
  1.3.1.1.3:3  1.5.2.5:3  1.3.1.1.4:3  1.5.2.6:3  1.3.1:2  1.3.1.1.5:2
  1.5.2.1:2  1.3.1.1.6.1:2  1.5.2.2:2  1.3.1.1.5.2:1  1.3.1.1.6.3:1
  1.3.1.1.5.1:1  1.3.1.1.5.3:1  1.3.1.1.5.4:1  1.5.2:1  1.5.2.7:1  1.3.1.1.1:1
```

**交叉驗證**：相異章節數 **21**，與 `anchor_probe.txt` 之 21 相符。
兩份輸出由不同聚合路徑產出（前者按 SYS-RA 聚合、後者按 leaf 聚合），
收斂到同一章節集合。

### 3.1 章節標題（判斷相關性之依據，執行層另行實測）

分析層未提供標題，而「章節是否相關」無標題無法判斷，故補測：

| 章節 | 標題 |
|---|---|
| `1.3.1` | Time and Date |
| `1.3.1.1.1` | Time Display Configuration |
| `1.3.1.1.2` | Vehicle Time Master Requirements |
| `1.3.1.1.3` | GPS TIME |
| `1.3.1.1.4` | Time Information Transmission |
| `1.3.1.1.5` | Time Display |
| `1.3.1.1.5.1` | Time Display Formats (If applicable. Refer to HMI) |
| `1.3.1.1.5.2` | Changing Time |
| `1.3.1.1.5.3` | Time Zones |
| `1.3.1.1.5.4` | Daylight Saving Time (Nav. Only) |
| `1.3.1.1.6.1` | Date Display Configuration (If applicable. Refer to HMI) |
| `1.3.1.1.6.2` | Vehicle Date Master Requirements |
| `1.3.1.1.6.3` | Date Display |
| `1.5.2` | Time and Date indication management by LTM |
| `1.5.2.1` | Time and Date indication management |
| `1.5.2.2` | Time Indication management on Key Off Status |
| `1.5.2.3` | Time function setting |
| `1.5.2.4` | Automatic Time Adjustment via GPS |
| `1.5.2.5` | GPS Time and Date |
| `1.5.2.6` | Date function setting |
| `1.5.2.7` | Output behavior description for LTM: "Time and Date" indication |

21/21 全數取得。

## 4. 七組逐組觀察（**只觀察，未改任何分組**）

| Set | 內聚判定 | 依據 |
|---|---|---|
| 1 `Manual Setting` | **良好** | 見 4.1 |
| 2 `GPS Sync` | **良好** | 見 4.2 |
| 3 `Master Clock` | **最分散 —— 唯一觸發 §4.1.4 訊號者** | 見 4.3 |
| 4 `CAN Transmission` | 中等 | 見 4.4 |
| 5 `Display` | **良好，且證據支持 019 之歸屬** | 見 4.5 |
| 6 `Zone and DST` | **完美** | 見 4.6 |
| 7 `Fault Handling` | 章節證據**無鑑別力** | 見 4.7 |

### 4.1 Set 1 `Manual Setting`（001, 015）—— 良好

兩者呈**結構對稱**：001 落 `1.5.2.3 Time function setting`，
015 落 `1.5.2.6 Date function setting` —— 同層姊妹節，一時一日。
001 另有 `1.3.1.1.5.2 Changing Time`（使用者變更路徑）。

無共通章節，但**共通結構**：兩者各自落在自己資料欄位的「function setting」
節。此為 §4.2 所稱之共用 setup 與 UI 進入路徑之章節層證據。

### 4.2 Set 2 `GPS Sync`（002, 003, 004, 014）—— 良好

GPS 軸明確：`1.5.2.4 Automatic Time Adjustment via GPS` 命中 002/003/004，
`1.5.2.5 GPS Time and Date` 命中 003/004/014，
`1.3.1.1.3 GPS TIME` 命中 002/004。**四筆全部至少沾一個 GPS 章節。**

輕微雜訊：014 另有 `1.3.1.1.6.1 Date Display Configuration`，偏 Display 支。
不足以構成移組訊號 —— 014 為 GPS Date/Time Broadcast，其落在
`1.5.2.5 GPS Time and Date` 為主軸。

### 4.3 Set 3 `Master Clock`（005, 006, 016, 018, 021）—— **唯一觸發訊號者**

五筆**無任何共通章節**，分佈於四個不相鄰群：

| leaf | 章節 | 群 |
|---|---|---|
| 005 Internal Clock Accuracy | `1.3.1.1.3` | **GPS 支** |
| 006 Internal Time Representation | `1.3.1`, `1.3.1.1.2` | Time Master |
| 016 Date Master Function | `1.3.1.1.6.2` | Date Master |
| 018 Default Initialization | `1.3.1.1.6.2`, `1.5.2.6`, `1.5.2.7` | Date Master + LTM 輸出 |
| 021 Sleep/Wakeup Handling | `1.5.2.2` | **Key Off** |

006（Time Master）與 016（Date Master）對稱、016 與 018 共用
`1.3.1.1.6.2`，此三筆內聚尚可。**但 005 落在 GPS 支、021 落在 Key Off，
與其餘三筆無交集。**

**005 之證據不完整，須特別注意**：其 `#SYS-RA = 2`，而 sections 僅 1 個
—— 另一筆即 **A-TM13 之 `SYS-RA-221`（來源物件 `6151328` 不在 CFTS 基線）**。
即 005 之章節證據只有一半可用，其「落在 GPS 支」是**殘缺樣本之結論**，
不宜據以判定 005 應移組。

**021 之分散則無此保留**：`#SYS-RA = 1`，證據完整，確實只落在
`1.5.2.2 Time Indication management on Key Off Status`。

**執行層觀察（不改分組）**：分析層 §2.2 之設計說明稱「021 不是 outlier，
單獨成組會產生 §4.2 所禁之單需求 Test Set」。章節證據**不支持**該理由 ——
021 在章節層確實孤立。但「是否為 outlier」屬 Layer 2 之語意判斷（Tier 2），
章節證據只提供訊號，不作結論。

**另注意**：021 與 Set 4 之 020（IPC Synchronization）**共用 `1.5.2.2`**，
兩者卻分屬不同組。此為跨組共用之唯一實例。

### 4.4 Set 4 `CAN Transmission`（008, 009, 017, 020）—— 中等

`1.3.1.1.4 Time Information Transmission` 命中 008/009 —— 傳輸軸成立。
`1.5.2.4` 命中 008/017/020。

**020 IPC Synchronization 無任何 Transmission 章節**：其落在
`1.5.2.2`(Key Off) / `1.5.2.3`(Time function setting) / `1.5.2.4`(GPS adjust)。
如 4.3 末所述，020 與 021 共用 `1.5.2.2`。此為本組之最弱一環。

### 4.5 Set 5 `Display`（007, 011, 019）—— 良好，**且回答了分析層自陳之不確定項**

分析層稱 019 Proxi-Based Behavior「為七組中最不確定的一項」。

**章節證據支持其歸入 Display**：019 落在 **`1.3.1.1.1 Time Display
Configuration`** —— 該節本身即 Display 家族（與 007 之 `1.3.1.1.5 Time
Display`、011 之 `1.3.1.1.5.1 Time Display Formats`、007 之
`1.3.1.1.6.3 Date Display` 同族）。

019 另有 `1.5.2.6 Date function setting`（與 015 共用，Set 1）。
故若要移，方向是 Set 1 而非 Set 3；但主軸 `1.3.1.1.1` 明確屬 Display。

**執行層觀察**：分析層所慮之替代歸屬（獨立 / 歸入 `Master Clock`），
章節證據**不支持 `Master Clock`** —— 019 與 005/006/016/018/021 無任何
共通章節。

### 4.6 Set 6 `Zone and DST`（012, 013）—— 完美

012 → `1.3.1.1.5.3 Time Zones`；013 → `1.3.1.1.5.4 Daylight Saving Time`。
**兩個相鄰姊妹節，同屬 `1.3.1.1.5 Time Display` 之下，各自單一章節。**
七組中章節對應最乾淨者。

### 4.7 Set 7 `Fault Handling`（010, 022）—— 章節證據無鑑別力

010 → `1.3.1.1.5`(Time Display)；022 → `1.3.1`, `1.5.2.1`。**無共通章節。**

**但此不構成訊號**：本組之分組依據為「異常路徑」，而異常處理在 spec 中
本就散佈於各功能章節之內，不會自成一節。章節證據對本組**既不支持也不
反對**，如實記為無鑑別力，不充作「已檢驗且通過」。

### 4.8 綜合

**七組中僅 Set 3 觸發 §4.1.4 第 4 用途之訊號**，且其中 005 之證據因
A-TM13 而殘缺，真正無保留的孤立者為 021。

`1.5.3.*`（ETM）零命中一事，執行層複驗屬實（21 個章節全落
`1.3.1.*` 與 `1.5.2.*`）。分析層稱「與 A-TM09 之 48 筆缺口是否同源尚未
查證，不在本包主張之列」—— 執行層同樣未查證，不主張。

## 5. T4(5) — 該驗而未驗者之獨立判斷

### 5.1 盤點所用之全集（明列）

沿用 `01Z` §7.1 四全集（其中「寫入後複查」源自 A-TM15）：

1. 02 包 §3 之 T1–T4 每一項指示
2. 本包所觸及之每一個檔案（寫入後複查）
3. 本包引用之每一個外部事實（實測或轉述）
4. 每一個「不存在 / 0 命中」之結論（有無陰性對照）

**本包新增第 5 個全集**：**§2 framework 草案之每一項設計說明**，
逐項問「其所據之事實，本包是否已驗」。理由：本包首次收到含實質內容
主張之草案（前此各包為程序與登記），而草案之說明句（如「021 不是
outlier」「019 與 007/011 共用 UI 進入路徑」）皆為可驗或不可驗之斷言，
不逐項過即等於默認。

### 5.2 依全集 2 — 寫入後複查

| 檔案 | 複查 | 結果 |
|---|---|---|
| `ANOMALIES.md`（T1 索引 + 條文） | `grep -n '^| A-TM02a'`、條數 | 16 / 16 ✅ |
| `ANOMALIES.md`（T2 A-TM16 追加） | `grep -n '雙方確認'` | 命中 :935 ✅ |
| `RULINGS.md`（R-TM13） | `grep -c '^## R-TM'` | 16 ✅ |
| `data/leaf_to_section_probe.txt` | `cat` 全文 | 22 列 ✅ |

三處 `str.replace` 全部前置 `assert`。

### 5.3 依全集 5 — 草案設計說明之可驗性（本包新增）

| § | 斷言 | 本包是否已驗 |
|---|---|---|
| 2.2 | 「每筆 leaf 恰屬一組，無重複無遺漏，合計 22」 | **已驗**：逐筆點算，22 筆無重複、與 leaf 全集相等 |
| 2.2 | 「時間與日期共用主控、共用傳輸、共用初始化」 | **已驗**：`1.3.1.1.2` Time Master 與 `1.3.1.1.6.2` Date Master 分立，但 006/016 對稱、018 跨兩者；`1.3.1.1.4` Transmission 兼含時日 → 斷言成立 |
| 2.2 | 「021 與 005/006 同屬內部計時能力」 | **章節層不支持**（見 4.3），但屬語意判斷，未反駁 |
| 2.2 | 「019 與 007/011 共用同一 UI 進入路徑」 | **章節層支持**（見 4.5） |
| 2.2 | 「010 與 022 都是異常路徑」 | **未驗** —— 需讀 037 之 leaf 描述全文，本包未做 |
| 2.3 | 「`1.5.3.*` ETM 零命中」 | **已驗**：21 章節全落 `1.3.1.*` / `1.5.2.*` |

### 5.4 仍未驗者 — 逐項

| # | 項 | 為何未驗 | 判斷 |
|---|---|---|---|
| 1 | 037 之 22 筆 leaf **描述全文** | 本包指令未涉；§4 之組別觀察僅用章節，未用 leaf 內容 | **可驗而未驗** —— 見下 |
| 2 | Set 7 之「異常路徑」語意判準 | 同 #1，依賴 leaf 描述 | 併 #1 |
| 3 | 交付路徑 Home 複本內容 | 刻意不驗（R-TM10-A1 SUSPENDED） | 正確之不驗 |
| 4 | PU 陽性對照 | 跨 feature 取用須 Pei 裁（`01Z-A3` §6） | 待裁 |
| 5 | `write_back` 兩值 | Phase 3 排程 | 範圍外 |
| 6 | `1.5.3.*` 零命中與 A-TM09 之關聯 | 分析層明言不在主張之列 | 一致，不主張 |

**第 1 項須說明**：Layer 2 之分組本質是**語意分組**，章節只是外部檢驗
（§4.1.4 第 4 用途）。本包之七組觀察全部僅憑章節，**未讀任何 leaf 之
描述全文**。故 §4 之判定只能說「章節證據支持 / 不支持 / 無鑑別力」，
**不能說某組分對或分錯**。

`Set 3` 之訊號與 `Set 7` 之無鑑別力，兩者都可能在讀過 leaf 描述後改變
判讀。執行層**未逕讀**，因 T3 僅指派章節對映，且 Layer 2 屬 Tier 2。
**提請**：若分析層要據 §4 調整分組，宜先指派一次 leaf 描述之逐筆閱讀，
否則調整所據之證據面窄於決策面。

### 5.5 依全集 4 — 「不存在 / 0 命中」之陰性對照

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| `Time Management/` 無 `FM-WI-FSM-037-*` | 同一 `ls` 於另三目錄各命中一個 | ✅ |
| `1.5.3.*` 零命中 | 同一映射 `1.3.1.*`/`1.5.2.*` 命中 21 節 | ✅ |
| Set 3 五筆無共通章節 | 同一資料下 Set 6 兩筆各有單一明確章節、Set 2 四筆共用 GPS 軸 | ✅ |

## 6. 本包未動之事項

未動 git。未開啟交付路徑之任何檔案（T2 純 `ls`）。未填 `D5`、未組任何
Scope 值。**未改 §2.2 之任何分組**。未產出 `leaf_to_section.tsv` 正式檔
（輸出為 `*_probe.txt`）。未援引任何他 feature 樣式。未以 openpyxl 存回
任何工作簿。**未跑 `recon.py`**。未讀 037 之 leaf 描述全文（見 §5.4）。
