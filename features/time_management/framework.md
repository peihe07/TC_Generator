> **⛔ 本檔作廢（2026-08-20，R-TM16）。**
> framework 之唯一位置為 `docs/fw036/framework.md`（Part VII）。
> 本檔係 `02R_framework_lock.md` T3 之誤指派所建，該指派已由 R-TM16 撤銷。
> 內容以全域檔為準，本檔不再維護，保留為軌跡（R-TM13）。

# framework — Time Management（Test Group: Time and Date）

**狀態：Layer 1 已裁（R-TM8）；Layer 2 [PROPOSED]，待 Pei 簽；
Layer 3 依實測鎖定（`data/leaf_to_section_probe.txt`）。**

**Layer 2 未經 Pei 簽核前，不得據以生成任何 TC。**

來源：`docs/handoff/02R_framework_lock.md` §3。
語意複核依據：037 `Requirement Description` 欄全 22 筆（分析層讀）。
章節對映依據：`data/leaf_to_section_probe.txt`（執行層 02 上繳 §3）。

---

## 1. Layer 1

```
Test Group = "Time and Date"        （R-TM8，已裁）
```

## 2. Layer 2 —— 七組，維持 `02` §2.2 不變

| # | Test Set | leaf | 數 |
|---|---|---|---|
| 1 | `Manual Setting` | 001, 015 | 2 |
| 2 | `GPS Sync` | 002, 003, 004, 014 | 4 |
| 3 | `Master Clock` | 005, 006, 016, 018, 021 | 5 |
| 4 | `CAN Transmission` | 008, 009, 017, 020 | 4 |
| 5 | `Display` | 007, 011, 019 | 3 |
| 6 | `Zone and DST` | 012, 013 | 2 |
| 7 | `Fault Handling` | 010, 022 | 2 |

合計 22 = leaf 全集。經 02R §2 之語意複核，七組全部維持，無一調整。

## 3. Layer 3 —— 主軸章節（全表見 `data/leaf_to_section_probe.txt`）

| Test Set | 主軸章節 | 標題 |
|---|---|---|
| `Manual Setting` | `1.5.2.3` / `1.5.2.6` | Time / Date function setting（同層姊妹節）|
| `GPS Sync` | `1.3.1.1.3` / `1.5.2.4` / `1.5.2.5` | GPS TIME / Automatic Time Adjustment via GPS / GPS Time and Date |
| `Master Clock` | `1.3.1.1.2` / `1.3.1.1.6.2` | Vehicle Time / Date Master Requirements |
| `CAN Transmission` | `1.3.1.1.4` / `1.5.2.1` | Time Information Transmission / T&D indication management |
| `Display` | `1.3.1.1.1` / `1.3.1.1.5` / `1.3.1.1.5.1` / `1.3.1.1.6.3` | Display Configuration / Time Display / Formats / Date Display |
| `Zone and DST` | `1.3.1.1.5.3` / `1.3.1.1.5.4` | Time Zones / Daylight Saving Time |
| `Fault Handling` | —— | 無主軸；異常處理散佈各章（02R §2.2）|

**條件章節不列為任一組之主軸**：`1.5.2.2`（Key Off）、`1.5.2.7`（Output
behavior）依 R-TM15 為條件／輸出章節，跨組出現屬預期。

## 4. 相鄰組界線（§8.2.1 用，寫 TC 時據此避免重複覆蓋）

讀過描述後浮現三處鄰接，**須在 framework 內明記**，否則 TC 作者會雙重覆蓋：

| 鄰接 | 界線 |
|---|---|
| 004 GPS Fallback ↔ 010 Invalid Data | 004 只管 **GPS 來源**不可用時改用內部時鐘；010 管**收到之時間訊號**無效時用最後有效值。觸發源不同 |
| 014 GPS Date/Time Broadcast ↔ 022 SNA Handling | 014 之描述含「or SNA if unavailable」，022 專責 SNA/預設值。**SNA 之送出規則屬 022**；014 只驗 GPS 資料之送出 |
| 018 Default Initialization ↔ 011 Time Format Handling | 018 管 reset／斷電後之預設值；011 管格式（12H/24H）跨喚醒週期之保存與廣播。兩者都涉「重開之後」，但一者是時間值、一者是格式 |
