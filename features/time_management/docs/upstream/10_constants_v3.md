# 10 上繳 —— v3 條文落檔、DR 更新、22 片逐字複驗

執行層，2026-08-22。對應下放包 `docs/handoff/10_constants_v3.md`。

---

## 0. 執行結果一覽

| 任務 | 內容 | 狀態 |
|---|---|---|
| T1 | R-TM60 / R-TM61 入 `RULINGS.md` | 完成 |
| T2 | DR-10 敘述四項分列（影響 1 → 3 片）；DR-7 空號定案註記 | 完成 |
| T3 | 22 片逐字閱讀，v3 對應複驗 | 完成 —— **無第二個 §5.1 型不符，未觸發停止條件** |
| T4 | 驗證 | 完成 |
| T5 | 本包 | 完成 |

**增量（R-TM46）**：`## R-TM` **+2**（62 → 64）；`## A-TM` **0**（25）；
`## G-TM` **0**（3）。與下放包所訂增量相同。

**T3 之主要發現：v3 之 19 條無一措辭不符，但有五個覆蓋缺口，
其中三個是系統性的**（跨多片、非單片遺漏）。最大者為
**「讀取 CAN 訊號值」之操作缺常數，影響七片**。

---

## 1. T3 —— 22 片逐字複驗全表

**方法**：對 `data/leaf_descriptions.txt` 之 22 片 `Requirement Description`
**逐字閱讀**，非關鍵詞掃描（`09` §5.3 已證關鍵詞會誤命中）。
逐片判定四事：需要哪些操作、v3 哪些適用、有無未涵蓋之操作、有無措辭不符。

| leaf | 題名 | v3 適用者 | 未涵蓋之操作 | 措辭不符 |
|---|---|---|---|---|
| 001 | Manual Time Setting | `SET_TIME_MANUAL` `GPS_SYNC_OFF` `READ_HU_TIME` | — | 無 |
| 002 | GPS Sync Enable/Disable | `GPS_SYNC_ON` `GPS_SYNC_OFF` | **G3 設定 PROXI 參數**（`NAV_Presence` / `GPS_Presence`） | 無 |
| 003 | GPS Time Calculation | `CROSS_TIME_ZONE`※ `CROSS_DST_BOUNDARY`※ `KEY_ON` `READ_HU_TIME` | — | 無 |
| 004 | GPS Fallback Handling | `GPS_LOST`※ `GPS_RESTORE`※ `READ_HU_TIME` | — | 無 |
| 005 | Internal Clock Accuracy | `GPS_LOST`※ `READ_HU_TIME` | **G5 24 小時 ±2 秒之長時量測** | 無 |
| 006 | Internal Time Representation | — | **G1 讀取 CAN 訊號值**（`HU_Time.Info`） | 無 |
| 007 | Time Display Handling | `READ_HU_TIME` `READ_HU_DATE` | **G4 讀取 VES 顯示** | 無 |
| 008 | Time Transmission on CAN | `CAN_WAKE` `SET_TIME_MANUAL` | **G1**（週期性／喚醒／更新後之送出須觀察訊號） | 無 |
| 009 | Time Signal Validation | — | **G1** ＋ **G2 注入越界值**（hour 0–23 等邊界） | 無 |
| 010 | Invalid Data Handling | — | **G1** ＋ **G2 注入無效／缺失訊號** | 無 |
| 011 | Time Format Handling | `SET_FORMAT_12H` `SET_FORMAT_24H` `KEY_OFF` `KEY_ON` `CAN_SLEEP`※ `CAN_WAKE` | **G1**（broadcast 之觀察） | 無 |
| 012 | Time Zone Handling | `CROSS_TIME_ZONE`※ `KEY_OFF` `KEY_ON` `READ_HU_TIME` | — | 無 |
| 013 | DST Handling | `CROSS_DST_BOUNDARY`※ `READ_HU_TIME` | — | 無 |
| 014 | GPS Date/Time Broadcast | `GPS_LOST`※ `GPS_RESTORE`※ | **G1**（GPS 值與 SNA 值之觀察） | 無 |
| 015 | Manual Date Handling | `SET_DATE_MANUAL` `GPS_SYNC_OFF` `READ_HU_DATE` | — | 無 |
| 016 | Date Master Function | `SET_DATE_MANUAL` `READ_HU_DATE` | **G1**（master 身分須看送出） | 無 |
| 017 | Date Transmission | `READ_IPC_TIME` `READ_HU_DATE` | **G1**（`TELEMATICS_TIME_DATE` 與 TLM LIDs） | 無 |
| 018 | Default Initialization | `ECU_RESET`※ `BATTERY_RECONNECT` `READ_HU_TIME` `READ_HU_DATE` | — | 無 |
| 019 | Proxi-Based Behavior | — | **G3 設定 PROXI 參數**（Cluster type / GPS / NAV） | 無 |
| 020 | IPC Synchronization | `READ_IPC_TIME` | **G1**（`TIME_DATE` messages） | 無 |
| 021 | Sleep/Wakeup Handling | `CAN_SLEEP`※ `CAN_WAKE` `READ_HU_TIME` | — | 無 |
| 022 | SNA Handling | — | **G1** ＋ **G2**（使資料無效以觀察 SNA） | 無 |

※ = v3 中已為 `PENDING: DR-n` 之佔位。

### 1.1 停止條件未觸發 —— 且此事本身是判準之佐證

T3 之停止條件為「發現第二個 §5.1 型之不符」。**逐片查完，無一措辭不符。**

**一項正向佐證**：`GPS_SYNC_ON` / `GPS_SYNC_OFF` 假設有
`"Sync Time with GPS"` 之使用者開關 —— 表面上與被 R-TM60 刪除的
`SET_TIME_ZONE` / `DST_ON` / `DST_OFF` 同型（都假設 UI 開關），
**但 002 逐字含 `and user settings`**：

```
002  The software shall enable/disable GPS time synchronization based on
     NAV_Presence, GPS_Presence, **and user settings**
```

而 012 / 013 逐字為 `automatically using GPS`、`automatically based on
time zone rules`，**無任何使用者操作之提及**。

**故判準是可操作的**：spec 有無提及使用者操作，決定該操作之常數是否
可寫。`GPS_SYNC_*` 通過此判準，被刪的三條不通過。
（UI 標籤之**正式名稱**是另一問題 —— 見 §1.3。）

### 1.2 五個覆蓋缺口，三個是系統性的

| # | 缺口 | 影響片數 | 性質 |
|---|---|---|---|
| **G1** | **讀取／觀察 CAN 訊號值** | **9**（006 008 009 011 014 016 017 020 022）| **系統性** |
| **G2** | 注入無效／越界／缺失之訊號 | 3（009 010 022） | 系統性 |
| **G3** | 設定 PROXI 參數 | 2（002 019） | 系統性 |
| G4 | 讀取 VES 顯示 | 1（007） | 單片 |
| G5 | 24 小時 ±2 秒之長時量測 | 1（005） | 單片，已知（`10` §5 同意不擬） |

**G1 之片數更正**：上表逐列統計後為 **9 片**（006 / 008 / 009 / 011 /
014 / 016 / 017 / 020 / 022），非我初估之七片。**列全集如下**，
以免重蹈 `08` §6.2 之計數未複核：

```
006 讀 HU_Time.Info        008 讀週期/喚醒/更新後之送出
009 讀送出前之驗證結果      011 讀 broadcast 之格式值
014 讀 GPS 值與 SNA 值      016 讀 master 送出之日期
017 讀 TELEMATICS_TIME_DATE 020 讀 TIME_DATE messages
022 讀 SNA/預設值
```

**G1 是 v3 最大的缺口**：v3 只有三條讀值常數（`READ_HU_TIME` /
`READ_IPC_TIME` / `READ_HU_DATE`），**全部是讀「顯示畫面」**。
而九片需要的是讀 **CAN 訊號值** —— 兩者是不同的量測點，
且本 feature 之核心（Time Transmission / Broadcast / Synchronization）
恰恰落在訊號側而非畫面側。

**執行層未擬措辭**（禁令：不代擬 `PENDING: DR-n` 之替代措辭；
且讀訊號之操作方式涉診斷工具，與 DR-9 同屬設備能力，無來源）。
**提請分析層裁量是否登記為新 DR。**

### 1.3 UI 標籤之正式名稱 —— 與本表無關但須並記

v3 中含引號 UI 標籤者三條：`"Time and Date"`（兩處）、
`"Sync Time with GPS"`。**其正式名稱未經查證** —— `11` T4 指派以
HMI Settings List 查證，本包未執行（屬 `11`）。

本表之「措辭不符：無」係就**操作類型**而言（該操作依 spec 是否存在），
**不含標籤字面之正確性**。二者不同層，不可互相代替。

---

## 2. T1 / T2

### T1 —— R-TM60 / R-TM61

兩條已入 `RULINGS.md`（第 2396 / 2437 行），內文為下放包 §1 / §4 之區塊
全文，並附 spec 佐證表（1.3.1.1.5.3 / 1.3.1.1.5.4 之逐字）。

**執行層就 R-TM60 記了一條可操作之判準**（見該條回報段）：凡設定類功能
之步驟措辭，落筆前須先查 spec 該能力是自動或由使用者觸發 ——
「設定類功能通常有 UI 開關」是最容易成立的常識推論，也是最容易寫出
spec 未述能力（§8.4.2）之路徑。**§1.1 之 002 對照即此判準之首次應用。**

### T2 —— DR-10 / DR-7

DR-10 主表列改為「四項分列」，影響 leaf 由
`001–005 / 012 / 014 / 015 / 019` 精確化為
`(i)(ii) 004 / 005；(iii) 003 / 012；(iv) 003 / 013`，
並於檔末追加敘述更新區塊全文。

DR-7 於主表新增一列（狀態列為「未使用之空號」），檔末追加定案說明。
**成因記為分析層之配號錯誤**，並記明執行層依令配號且回報空號之處置正確
—— 此為分析層於 `10` §3 之自陳，照錄。

---

## 3. T4 —— 驗證輸出（R-TM31：列明細）

```
grep -n '^## R-TM6[01]' RULINGS.md
  2396:## R-TM60 — 常數表 v3：刪除三條手動時區/DST 常數
  2437:## R-TM61 — 搜尋未決項須兼搜識別字與字面量鍵

grep -c 'DR-7\|DR-10' DATA_REQUESTS.md        9 處
grep -c '^## R-TM' RULINGS.md                 64（62 + 2）

lint_tcs --self-test              自驗：31 / 31
build_batch_context --self-test   自驗：13 / 13
```

---

## 4. 未驗清單（R-TM54 三分）

### A. 可驗而未驗 —— 執行層能清

| # | 項目 | 說明 |
|---|---|---|
| A1 | **G1–G4 四個覆蓋缺口未擬措辭** | 依禁令未代擬。G1 影響 9 片，為最大者 |
| A2 | v3 之 UI 標籤字面未查證 | 屬 `11` T4，本包未執行 |
| A3 | `rows = 0` 時 tc_id 區間印 `-000` | 09 遺留 |
| A4 | A-TM25 (a)(b) 無自動攔截 | 08 遺留 |
| A5 | B-1 / B-2 及 B-3 / B-5 未守之側 | 07 遺留 |
| A6 | 018 / 017 之 objects 未逐一複驗 | 07 遺留 |
| A7 | `BOUNDARY_NOTES` 與 `BOUNDARY_SIGNALS` 對 018 之並存 | 07 遺留 |
| A8 | 交付件之 pre_conditions / ER 形式慣例未逐條驗 | 08 遺留 |

**`09` A7（v3 逐片對應未全查）已由本包 T3 清除。**

### B. 結構性不可複驗 —— 待 Pei

| # | 項目 |
|---|---|
| B1 | 常數表 v3 過目（**含本包 §1.2 之五個缺口**） |
| B2 | DR-8/9/10 之設備能力答覆；**DR-10 (iii)(iv) 為三片之關鍵路徑** |
| B3 | A-TM25 |
| B4 | RD-1 送出 |

### C. 已解決 —— 註明包號後移除

| # | 項目 | 解決於 |
|---|---|---|
| C1 | v3 之三條手動時區/DST 常數不符（09 §5.1） | 本包 T1（R-TM60），且有 spec 逐字佐證 |
| C2 | DR-7 空號之處置（09 §4） | 本包 T2，維持現配並記成因 |
| C3 | 三來源是否立為條文（09 §9.5） | 本包 T1（R-TM61） |
| C4 | 005 誤命中之更正（09 §5.3） | 下放包 `10` §5 已記載，不回改 `08` |
| C5 | v3 逐片對應未全查（09 A7） | 本包 T3，22 列全表 |

---

## 5. 未執行者（下放包所禁，逐項確認）

- 未生成任何 TC
- **未建 `tm_constants.py`**
- **未代擬任何 `PENDING: DR-n` 之替代措辭** —— G1–G4 只列缺口
- 未改 `backend/`、canon、`docs/fw036/framework.md`
- 未回改任何既有上繳包或下放包（`08` §6.2 之更正由下放包 `10` §5 承載）
- 未碰 `features/vehicle_setting/`
- 未送出 RD-1
- 未動 git（R-TM36）

---

## 6. 提請裁定

1. **G1 —— 讀取 CAN 訊號值之操作無常數，影響 9 片**（列全集見 §1.2）。
   v3 之三條讀值常數全為讀顯示畫面，而本 feature 之核心落在訊號側。
   是否登記新 DR（與 DR-9 同屬設備／診斷工具能力）。
2. **G2 / G3 —— 注入無效訊號（3 片）、設定 PROXI 參數（2 片）** 同樣無常數。
   G3 之 PROXI 參數另見 `11` T3 末段（LID 表 `Proxi & Configuration` 分頁
   是否含該六參數 —— 若含，其值域即前置條件之來源）。
3. **§1.1 之判準**（spec 有無提及使用者操作）是否值得立為條文 ——
   它使 R-TM60 之刪除與 `GPS_SYNC_*` 之保留有同一個可複驗的分界。
