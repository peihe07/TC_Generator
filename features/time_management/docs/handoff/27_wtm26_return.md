# 27 — W-TM-26 回繳（rev A, 2026-08-25）

上游包：`26_pei_review_remediation.md`（含 §6 執行層反驗、§7 追加裁定點）。
啟動依據：Pei 於 2026-08-25 對 §3 選 (a)、§7 Q1 選 (a)、Q2 選 (a)。

基準檔：`output/…_SWQT_20260822.xlsx`
SHA256 `2afd87be418e85599a99670db74457c3a629220583d39db195870a61093833c1`
輸出件：`output/…_SWQT_20260825.xlsx`（`--out`，R-TM80）
SHA256 `b45659624330c5d7578481d6b3d9989fea72697066b37ba1dc137ff95c0fe483`

---

## §1 完成度

| 工作 | 內容 | 狀態 |
|---|---|---|
| T1 | J 欄 59 條補編號 | 完成（42 條編號、17 條全數遷出後為 `NA`） |
| T2 | 37 條設定狀態遷移＋14 條補入口＋ER 1:1＋Proxi 5 條正規化 | 完成 |
| T3 | `Ignition is ON` ×56、`The CAN bus is awake` ×18 刪除；16 行轉步驟 | 完成 |
| T4 | 29 處 v1→v3 改寫；#035 之 DR-6 佔位移除；DATA_REQUESTS #6 加註 | 完成 |
| T5 | I–M 資料列改 left+top（295 格） | 完成（含 write_back 樣式通道，Q2(a)） |
| T6 | 逐列 diff、lint 報告、未結 DR 清單 | 本文 |

## §2 Pre-Condition 逐行處置（180 行全覆蓋，R-TM4）

| 處置 | 行數 |
|---|---|
| DELETE（§4.4 system default） | 74 |
| KEEP（合法 PC） | 48 |
| →STEP（D2 本 feature 設定狀態） | 37 |
| →STEP（D3 步驟可控狀態） | 16 |
| NORMALIZE（Proxi → canon §8.7.5(c)） | 5 |
| **合計** | **180** |

### DELETE（74）
`Ignition is ON` 56 行、`The CAN bus is awake` 18 行。

### KEEP（48）
架構限定行 27（Atl-High 21 / Atl-Mid 6，R-TM76）、
`GPS signal is available` 8、`GPS signal is unavailable` 1、
`The VES screens are powered on` 5、
`The cluster does not have the data needed to reference the date` 4、
`The splash screen display time has ended` 1、DST 環境二行 2。

> **借調判斷一項，請 Pei 覆核**：`The VES screens are powered on`（5 行，
> #009 #015 #016 #017 #043）判為 KEEP。理由是 VES 為獨立供電之後座螢幕，
> 其「已通電」非點火 ON 所蘊含，故非 §4.4 之 system default。
> 若 Pei 認為 VES 供電同屬預設，該 5 行應改 DELETE —— 一行指示即可改。

### →STEP（D2，37 行）
Sync Time with GPS 33（OFF 20 / ON 13）、Time Format 4（其中 #041 #042
為 §6 C3 補入者）。定式依 R-TM81：`Open the "Clock" settings` →
`Set "<項名>" to <值>`。14 條需補入口，23 條併入既有入口步。

### →STEP（D3，16 行）
| 原 PC 行 | 條 | 轉為 |
|---|---|---|
| `The CAN bus is asleep` | 7 | `PENDING: DR-9 使 CAN bus 進入 sleep 之操作方式與可觀察終止條件` |
| `Ignition is OFF` | 3 | `Turn the ignition to OFF` |
| `A date other than the initial value has been set` | 2 | 開設定 + 設一非初始日期 |
| `A date has been set` / `A time has been set on the HU` | 2 | 開設定 + 設值 |
| `The VES screen is showing dashes` | 1 | `PENDING: DR-20 持續注入無效訊號直至畫面顯示破折號…` |
| `A time zone has been applied` | 1 | `PENDING: DR-10 使車輛位置進入一時區並使其被套用…` |

**次序約束已處理**：設定步一律排在點火轉換與 sleep 建立之前
（否則點火 OFF 後無法進設定頁）。#041 #042 依 Q1(a) 成四步式
（開設定 → 設 Time Format → 建立 sleep → 喚醒 → 讀取）。

## §3 lint 與結構複驗

```
lint_tcs.py --feature-dir .            → 檔 4；發現 0 項
lint_tcs.py --self-test                → 自驗 53 / 53
verify_structure（write_back 內建）     → 通過
zip member 數                          48 → 48
data-validation 計數（classic, x14）    逐分頁相同（sheet6 之 3 + 1 完整保留）
sharedStrings.xml 於 restyle 後未變更   已斷言
```

**一項閘門失效已修（R-TM69(3)）。** lint 之 `arch-column` 檢查原以 LID
別名（`$DateTmHour$`）為「本條是否談及訊號」之偵測判準。T4 把別名全部
改為訊號全名之後，**該閘門覆蓋由 11 條掉到 0 條而不報任何錯** ——
T4 後第一次 lint 之「0 項」有一部分是閘門失效，不是真的乾淨。
已將偵測判準擴充為「LID 別名 ∪ 兩架構之訊號全名」（71 個 token），
覆蓋還原為原本同一組 11 條（#006 #007 #008 #015 #016 #017 #035 #042
#043 #046 #047）。**兩架構之訊號名皆納入**：偵測要問的是「本條談不談
訊號」，與訊號屬哪個架構無關 —— 架構之對錯正是該閘門要判的，
不能拿它當偵測前提。

## §4 逐列 diff

| TC | PC 行 | 步驟數 | 動作 |
|---|---|---|---|
| #001 | 2 → 0 | 5 → 6 | 補 1 步；T1 PC 全空→NA |
| #002 | 2 → 0 | 4 → 5 | 補 1 步；T1 PC 全空→NA |
| #003 | 2 → 0 | 3 → 4 | 補 1 步；T1 PC 全空→NA |
| #004 | 3 → 1 | 3 → 6 | 補 3 步；T1 編號 |
| #005 | 3 → 1 | 3 → 5 | 補 2 步；T1 編號 |
| #006 | 3 → 1 | 4 → 5 | 補 1 步；T4 v3 改寫；T1 編號 |
| #007 | 2 → 1 | 2 → 2 | T4 v3 改寫；T1 編號 |
| #008 | 2 → 1 | 2 → 2 | T4 v3 改寫；T1 編號 |
| #009 | 3 → 2 | 3 → 3 | T1 編號 |
| #010 | 2 → 1 | 1 → 1 | T1 編號 |
| #011 | 2 → 0 | 2 → 2 | T4 v3 改寫；T1 PC 全空→NA |
| #012 | 2 → 0 | 3 → 4 | 補 1 步；T4 v3 改寫；T1 PC 全空→NA |
| #013 | 2 → 0 | 1 → 1 | T4 v3 改寫；T1 PC 全空→NA |
| #014 | 3 → 0 | 4 → 5 | 補 1 步；T4 v3 改寫；T1 PC 全空→NA |
| #015 | 4 → 3 | 3 → 3 | T1 編號 |
| #016 | 3 → 2 | 2 → 2 | T1 編號 |
| #017 | 4 → 2 | 2 → 3 | 補 1 步；T1 編號 |
| #018 | 4 → 2 | 2 → 4 | 補 2 步；T1 編號 |
| #019 | 4 → 1 | 3 → 7 | 補 4 步；T1 編號 |
| #020 | 2 → 1 | 3 → 3 | Proxi 正規化；T1 編號 |
| #021 | 3 → 1 | 3 → 4 | 補 1 步；Proxi 正規化；T1 編號 |
| #022 | 2 → 1 | 2 → 2 | Proxi 正規化；T1 編號 |
| #023 | 3 → 1 | 3 → 5 | 補 2 步；T1 編號 |
| #024 | 3 → 1 | 3 → 5 | 補 2 步；T1 編號 |
| #025 | 2 → 0 | 2 → 5 | 補 3 步；T4 v3 改寫；T1 PC 全空→NA |
| #026 | 3 → 1 | 3 → 4 | 補 1 步；T1 編號 |
| #027 | 3 → 1 | 3 → 5 | 補 2 步；T4 v3 改寫；T1 編號 |
| #028 | 3 → 1 | 3 → 5 | 補 2 步；T4 v3 改寫；T1 編號 |
| #029 | 3 → 1 | 3 → 4 | 補 1 步；T1 編號 |
| #030 | 3 → 1 | 3 → 4 | 補 1 步；T1 編號 |
| #031 | 3 → 1 | 3 → 4 | 補 1 步；T1 編號 |
| #032 | 2 → 0 | 3 → 5 | 補 2 步；T1 PC 全空→NA |
| #033 | 2 → 0 | 2 → 4 | 補 2 步；T1 PC 全空→NA |
| #034 | 3 → 1 | 4 → 4 | T1 編號 |
| #035 | 3 → 1 | 2 → 3 | 補 1 步；T4 v3 改寫；T1 編號 |
| #036 | 3 → 0 | 3 → 4 | 補 1 步；T4 v3 改寫；T1 PC 全空→NA |
| #037 | 3 → 0 | 3 → 4 | 補 1 步；T4 v3 改寫；T1 PC 全空→NA |
| #038 | 3 → 0 | 3 → 4 | 補 1 步；T4 v3 改寫；T1 PC 全空→NA |
| #039 | 2 → 0 | 2 → 2 | T1 PC 全空→NA |
| #040 | 3 → 0 | 4 → 5 | 補 1 步；T4 v3 改寫；T1 PC 全空→NA |
| #041 | 4 → 1 | 2 → 5 | 補 3 步；T1 編號 |
| #042 | 4 → 1 | 2 → 5 | 補 3 步；T4 v3 改寫；T1 編號 |
| #043 | 4 → 2 | 2 → 4 | 補 2 步；T1 編號 |
| #044 | 4 → 1 | 3 → 4 | 補 1 步；T1 編號 |
| #045 | 5 → 1 | 4 → 7 | 補 3 步；T1 編號 |
| #046 | 4 → 1 | 4 → 5 | 補 1 步；T4 v3 改寫；T1 編號 |
| #047 | 4 → 1 | 3 → 4 | 補 1 步；T4 v3 改寫；T1 編號 |
| #048 | 3 → 1 | 2 → 3 | 補 1 步；Proxi 正規化；T1 編號 |
| #049 | 3 → 1 | 2 → 3 | 補 1 步；Proxi 正規化；T1 編號 |
| #050 | 4 → 1 | 4 → 6 | 補 2 步；T1 編號 |
| #051 | 4 → 1 | 3 → 6 | 補 3 步；T1 編號 |
| #052 | 5 → 3 | 3 → 5 | 補 2 步；T1 編號 |
| #053 | 5 → 3 | 3 → 5 | 補 2 步；T1 編號 |
| #054 | 3 → 1 | 3 → 4 | 補 1 步；T1 編號 |
| #055 | 4 → 1 | 4 → 5 | 補 1 步；T4 v3 改寫；T1 編號 |
| #056 | 4 → 1 | 3 → 4 | 補 1 步；T4 v3 改寫；T1 編號 |
| #057 | 3 → 1 | 5 → 6 | 補 1 步；T1 編號 |
| #058 | 2 → 0 | 2 → 2 | T4 v3 改寫；T1 PC 全空→NA |
| #059 | 2 → 0 | 2 → 2 | T4 v3 改寫；T1 PC 全空→NA |

## §5 工具變更（Q2(a) 射程內）

1. `backend/xlsx_surgical.py` 新增 `surgical_restyle()` —— 樣式通道。
   **不改既有 `<xf>`**（那會連帶重掛所有共用該 id 之格），而是由該格
   現用之 xf **衍生**一筆新 cellXfs 附加於表尾，只把指名之格重掛過去；
   未指名者保留原 id，故影響半徑恰等於計畫本身。本次：295 格重掛、
   新增 cellXfs 1 筆（來源 id 81 → 新 id 176，`wrapText` 由來源帶過）。
2. `features/time_management/scripts/write_back.py` 新增
   `apply_data_alignment()`，由 `feature.yaml` 之
   `write_back.data_alignment` **明示啟用**。未寫該鍵者行為與本次變更前
   逐位元相同 —— 此即 Q2(a) 之立論（新增明示啟用之通道，不動既有預設，
   與 A-TM29 之「改既有預設值」不同族）。
3. `features/time_management/scripts/lint_tcs.py` —— `arch-column`
   偵測判準擴充（見 §3）。

## §6 未結 DR 清單（上繳之隨附義務）

DR-2（037 正式件身分，High）、DR-4（037 覆蓋缺口 48 筆，High）、
DR-5（CFTS015 缺件物件 ×2，中）、DR-8（High）、DR-9（High）、
DR-10 四分項（High）、DR-12（其餘 UI 標籤，開放）、
DR-12b（設定頁名，High）、DR-20（High）。
DR-6 —— **降轉為僅供追溯，不再阻塞**（R-TM82，見 `DATA_REQUESTS.md` 末節）。
DR-7 空號、DR-11 已取消（軌跡保留）。

**工作簿 PENDING 處數 51 → 59**，增減成因與「處數上升不代表缺口擴大」
之交代見 `output/DELIVERY_NOTE.md`。八處新增全部落在既有之設備能力
四問（DR-8/9/10/20），未新增任何新 DR。

## §7 待 Pei 表態

1. ~~`The VES screens are powered on` 之 KEEP／DELETE（§2）。~~
   **已裁定：KEEP（R-TM86, Pei 2026-08-25），追認執行層之借調判斷。**
2. R-TM81 / R-TM82 已謄入 `RULINGS.md`（條數 83 → 85 含撤回、
   81 → 83 不含撤回，增量 +2 相符）。**執行層回報欄已於 2026-08-25
   回填**（W-TM-26-A1 同輪）。

3. **§C1 之判定經 `28` §3 推翻** —— `088a4476…` 為 repo 外已送審交付件
   之真實 SHA，本包只搜 repo 內即判為謄錄錯誤，並因此抹去「兩個 0822
   為不同檔案」之訊號。真正缺陷為 identifier 欄未經裁定改名（A-TM31），
   已由 R-TM85 裁定回改、W-TM-26-A1 T2 執行完畢。A-TM30 之前提隨之
   部分更正（建議仍成立，已由 R-G19-3 承接）。
3. 本輪未動 DR-12b 之 `Clock` 佔位（25 處），依 §1 D2 照留。
