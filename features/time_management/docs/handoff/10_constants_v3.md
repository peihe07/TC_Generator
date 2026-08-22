# 下放包 10 — 常數表 v3（刪三條）、DR-10 擴充、搜尋條文

分析層 → 執行層。往返編號 `10`。對應上繳 `docs/upstream/10_constants_v3.md`。
`09` 受理。**五項提請全部成立**，其中兩項更正我的產出。

---

## 1. §5.1 —— 三條常數與需求所述之能力不符，刪除

分析層回查 CFTS015 原文，**執行層之判定成立且有 spec 佐證**：

| spec | 逐字 |
|---|---|
| 1.3.1.1.5.3 Time Zones（物件 4813992） | `The HU that has a GPS input shall set the time zone **automatically**.` |
| 1.3.1.1.5.4 Daylight Saving Time（物件 4813995） | `The daylight saving time shall be **adjusted automatically**.` |

**兩節皆無使用者操作。** 037 之 012 / 013 描述與之一致
（`automatically using GPS`、`automatically based on time zone rules`）。

**我擬 `SET_TIME_ZONE` / `DST_ON` / `DST_OFF` 時，是照「設定類功能通常有
UI 開關」之常識推的，沒回查 spec。** 那三條若寫進 TC，測的是一個
spec 未述之能力 —— 即 §8.4.2 之 scope fabrication，而且是**由常數表
系統性地誘導**每一片相關 TC 都這樣寫。

```
R-TM60（分析層裁定，2026-08-22）—— 常數表 v3：刪除三條手動時區/DST 常數

v2 之 SET_TIME_ZONE / DST_ON / DST_OFF **刪除，不改佔位**。

刪除而非佔位之理由：佔位表示「該操作存在但方式未知」，而此三者是
**該操作依 spec 不存在** —— 012 / 013 之能力為自動判定，無使用者介面。
留佔位會使日後讀者以為只差一個 DR 就能填。

替代：012 / 013 之觸發改由位置與時間之改變為之：

    CROSS_TIME_ZONE = 'PENDING: DR-10 使車輛位置跨越時區邊界之操作方式'
    CROSS_DST_BOUNDARY = 'PENDING: DR-10 使車輛時間跨越 DST 切換點之操作方式'

`CROSS_TIME_ZONE` 由 v2 之具體措辭**改為佔位** —— 我在 09 §3.3 保留
具體措辭之理由（「位置設定是 GPS 測試之基本能力」）同樣是未經查證之推測，
與被我自己否決之 `Remove the GPS antenna …` 同型。**同一錯誤我犯了兩次，
第二次還為它寫了一段辯護。**
```

## 2. DR-10 —— 敘述擴充為三片之關鍵路徑

執行層指出 003（`using GPS UTC, time zone, and DST`）、012、013
**三片**皆依賴 GPS 位置／時間之可控性，非我原述之一片。

```
DR-10 敘述更新（2026-08-22）

原：Bench 之 GPS 訊號控制能力（使不可用／恢復／位置設定）

更新為：Bench 之 GPS 訊號控制能力，四項分列：
  (i)   使 GPS 訊號不可用          → 004 GPS Fallback、005 Internal Clock
  (ii)  恢復 GPS 訊號               → 同上
  (iii) 設定 GPS 位置（跨時區邊界）  → **003、012** 
  (iv)  設定 GPS 時間（跨 DST 切換點）→ **003、013**

**(iii)(iv) 為 003 / 012 / 013 三片之關鍵路徑** —— 若 Bench 不具該能力，
該三片無可執行之觸發操作，屬不可測而非待補措辭。

Urgency 維持 High；影響片數由 1 更正為 **3**（另 (i)(ii) 影響 2 片）。
```

## 3. §4 DR-7 空號 —— **維持，成因是我的配號錯誤**

執行層依令配 8/9/10 未自行前移，且指出但書只涵蓋向後順延 ——
**處置正確，錯在指令**：我指定 8/9/10 時未查既有最大號（實測為 6）。

**裁定維持現配**，理由：DR 號已寫入 `tm_constants` 之佔位字串與
`DATA_REQUESTS.md` 兩處，改號需同步兩處，而空號之成本僅為一行註記。
**成本不對稱。**

`DATA_REQUESTS.md` 之 DR-7 註記改為：

```markdown
| DR-7 | （未使用之空號）| —— | —— | 分析層於 09 包指定 DR-8/9/10 時未查既有最大號（時為 6），致 7 被跳過。非遺失之登記。 |
```

## 4. §2 三來源 —— 立為條文

第三處以字典鍵字面量 `cfg['write_back']['tc_id_format']` 存取，
**識別字 grep 不到**。

```
R-TM61（分析層自裁，2026-08-22）—— 搜尋未決項須兼搜識別字與字面量鍵

清點某項之使用點時，不得只搜其識別字（常數名、變數名），
須同時搜其**字面量鍵**（字典鍵字串、yaml 鍵名、欄位標題文字）。

理由：同一個值常有兩條存取路徑 —— 具名常數與字典查表，
前者可由識別字搜得，後者只出現為字串。只搜前者會漏掉後者，
而漏掉的那條往往正是實際生效的那條。

依據：09 上繳 §2 —— `TC_ID_FORMAT` 之使用點實為三處，
第三處（run() 之預覽列印）以 `cfg['write_back']['tc_id_format']` 存取，
分析層於 08 §5 之 grep 未命中，致 R-TM59 述為「雙來源」。

本條與 R-TM31（判準須列明細）同族：前者管輸出之可歸屬，
本條管輸入之涵蓋完整。
```

**§2.1 三項超出指令之設計決定，全部採納**：

- **(a) 保留值改為來源指標** —— 比留一份真格式字串更好。
  「痕跡留下了、雙來源也一併留下」之判斷精準；指標使誤用立即失敗。
- **(b) 格式須含 `{n`** —— 無序號欄位會使全列同 id，而 G-TM3 之逐列比對
  **兩側同錯驗不出來**。此為 R-TM21 之正確應用，且是我未想到的。
- **(c) 守衛抽為可獨立呼叫** —— R-TM56 之落實。

## 5. §5.3 之更正 —— 記載於此，不回改 `08`

執行層自查發現 `08` §6.2 之「12H/24H：005、011 兩片」中 **005 為誤命中**
（關鍵詞 `24.?h` 命中 `24 hours`）。**正確為只有 011 一片。**

**不回改 `08`**（軌跡不回頭改），本包記載即為更正之落檔處。

執行層之自我定性正確：「報了計數並附片號，看似可歸屬，但未複核每一個
命中是否為真命中」。**且其能自行發現，正因 `08` §6.2 之表列出了量測方法
（關鍵詞）** —— 這是 R-TM31 要求附量測條件之實際回報：
不只讓對造能查，也讓自己能查。

**連帶**：005 之驗證需「24 小時內 ±2 秒」之長時量測，v2/v3 無對應常數。
執行層「該類步驟可能不宜常數化（時長與量測方式屬 TC 內容）」之判斷
分析層同意，**不擬措辭**。

## 6. 常數表 v3（**[PROPOSED]，待 Pei 過目**）

```python
# features/time_management/scripts/tm_constants.py  [PROPOSED v3]
# 依 canon §5.3；本 feature 專屬（08 §3.2 實測：既有專案常數無一適用）

# —— 手動設定 ——
SET_TIME_MANUAL    = 'Open the "Time and Date" settings and set the time manually'
SET_DATE_MANUAL    = 'Open the "Time and Date" settings and set the date manually'

# —— GPS 同步 ——
GPS_SYNC_ON        = 'Set "Sync Time with GPS" to ON'
GPS_SYNC_OFF       = 'Set "Sync Time with GPS" to OFF'

# —— 時區 / DST（v3：刪除三條手動操作，改為位置/時間觸發）——
CROSS_TIME_ZONE    = 'PENDING: DR-10 使車輛位置跨越時區邊界之操作方式'
CROSS_DST_BOUNDARY = 'PENDING: DR-10 使車輛時間跨越 DST 切換點之操作方式'

# —— 時間格式（011 一片；005 為 v2 之誤命中，已更正）——
SET_FORMAT_12H     = 'Set the time format to 12-hour'
SET_FORMAT_24H     = 'Set the time format to 24-hour'

# —— 電源與重置 ——
KEY_OFF            = 'Turn the ignition to OFF'
KEY_ON             = 'Turn the ignition to ON'
BATTERY_RECONNECT  = 'Disconnect and reconnect the vehicle battery'
ECU_RESET          = 'PENDING: DR-8 ECU 軟體重置之操作方式'

# —— CAN ——
CAN_WAKE           = 'Wake the CAN bus'
CAN_SLEEP          = 'PENDING: DR-9 CAN sleep 之可觀察終止條件'

# —— GPS 訊號可用性 ——
GPS_LOST           = 'PENDING: DR-10 Bench 使 GPS 訊號不可用之操作方式'
GPS_RESTORE        = 'PENDING: DR-10 Bench 恢復 GPS 訊號之操作方式'

# —— 讀值 ——
READ_HU_TIME       = 'Read the time shown on the HU display and record it'
READ_IPC_TIME      = 'Read the time shown on the IPC display and record it'
READ_HU_DATE       = 'Read the date shown on the HU display and record it'
```

**19 條，其中 5 條為 `PENDING: DR-n` 佔位**（DR-8 一、DR-9 一、DR-10 三）。

`READ_HU_DATE` 之新增（執行層 §5.5 指出 016 / 017 須讀日期而非時間）
**採納並致謝** —— 那是 `08` 我漏掉的。

---

## 7. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM60 / R-TM61

標題行 `## R-TM60 — 常數表 v3：刪除三條手動時區/DST 常數`、
`## R-TM61 — 搜尋未決項須兼搜識別字與字面量鍵`，內文為 §1 / §4 之區塊。

**增量**：`## R-TM` **+2**；`## A-TM` **0**；`## G-TM` **0**。

### T2 — `DATA_REQUESTS.md`

- DR-10 敘述依 §2 更新（四項分列、影響片數 1 → 3）
- DR-7 空號註記依 §3

### T3 — v3 之逐片對應複驗（補 §7 A7 之缺口）

`09` §7 A7 自陳「只逐字查了六片，其餘採關鍵詞掃描，而 §5.3 已證關鍵詞
掃描會誤命中」。**本包補之。**

對全 22 片之 `Requirement Description` **逐字閱讀**（非關鍵詞掃描），
逐片判定：

1. 該片之測試觸發需要哪些操作
2. v3 之 19 條中哪些適用
3. **有無 v3 未涵蓋之操作**（如 005 之長時量測）
4. **有無 v3 之條目對該片而言措辭不符**（如 §5.1 之情形）

回報 22 列全表（R-TM4：列全集不列計數）。
**發現第二個 §5.1 型之不符即回報並停**。

### T4 — 驗證（R-TM31 列明細；R-TM46 增量）

```bash
grep -n '^## R-TM6[01]' features/time_management/RULINGS.md
grep -n 'DR-7\|DR-10' features/time_management/DATA_REQUESTS.md
grep -c '^## R-TM' features/time_management/RULINGS.md
python3 features/time_management/scripts/lint_tcs.py --self-test
python3 features/time_management/scripts/build_batch_context.py --self-test
```

### T5 — 上繳

`docs/upstream/10_constants_v3.md`。依 R-TM54 三分列未驗清單。
須含 T4 全部輸出、T3 之 22 列全表。

### 不得執行者

- 不動 git（除非 Pei 直接指示）
- **不生成任何 TC**
- **不建 `tm_constants.py`**（v3 仍待 Pei 過目）
- 不改 `backend/`、canon、`docs/fw036/framework.md`
- **不代擬任何 `PENDING: DR-n` 之替代措辭**
- 不回改任何既有上繳包或下放包
- 不碰 `features/vehicle_setting/`
- 不送出 RD-1

---

## 8. 呈報 Pei

1. **v3 待你過目。** 與 v2 之差異：刪三條（手動時區/DST —— spec 明文為
   自動，無使用者操作）、`CROSS_TIME_ZONE` 改佔位、新增
   `CROSS_DST_BOUNDARY`。19 條中 5 條為佔位。
2. **DR-10 是 003 / 012 / 013 三片之關鍵路徑**，不是附帶一問。
   若 Bench 不能設 GPS 位置與時間，該三片**不可測**（非待補措辭）。
3. **我在時區/DST 上犯了兩次同型錯誤**：v1 的 `Remove the GPS antenna …`
   是對設備的推測，v2 的 `SET_TIME_ZONE` / `DST_ON/OFF` 是對 UI 的推測，
   **而且第二次我還為 `CROSS_TIME_ZONE` 寫了一段辯護說它不必改佔位**。
   兩者都是「照常識推、未回查 spec 或設備」。
4. A-TM25、DR-8/9/10 之答覆、RD-1 送出，仍待你。

## 9. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM60 | 分析層裁定，v3 刪三條 | §1 | ✅ T1 |
| R-TM61 | 分析層自裁，搜尋須兼搜字面量 | §4 | ✅ T1 |
| DR-10 敘述更新 | 影響片數 1 → 3 | §2 | ✅ T2 |
| DR-7 空號註記 | 成因為分析層配號錯誤 | §3 | ✅ T2 |
| 常數表 v3 | [PROPOSED]，待 Pei | §6 | ⏸（不建）|

分析層本包未動 git、未改任何腳本、未改 canon、未回改任何既有包。
