# 下放包 09 — 死常數處置、A-TM25 量值更正、常數表 v2

分析層 → 執行層。往返編號 `09`。對應上繳 `docs/upstream/09_constants.md`。
`08` 受理。**五項提請全部成立，其中兩項更正我的陳述。**

---

## 1. §5 死常數 —— 採 (b)，且我的「只等 §3.4」是錯的

`TC_ID_FORMAT` 與 `PLACEHOLDER_BODY` 只出現於宣告與 unresolved 檢查，
從不被讀用；真正生效之 tc_id 格式在 `feature.yaml`。
**`--write` 被兩個不影響任何輸出之常數擋著。**

`08` §5 稱「B1 之啟動只等 §3.4 過目」為我所寫，**不成立** ——
我在寫該句時只清點了「條文層之未決項」，沒查程式碼層之 unresolved 清單。
**與 R-TM7（指令須經實測）同族：那次是介面未讀，本次是狀態未讀。**

```
R-TM59（分析層裁定，2026-08-22）—— 死常數處置採 (b)

TC_ID_FORMAT：改為自 feature.yaml 之 write_back.tc_id_format 讀入，
  消除雙來源。不刪除該識別字 —— 保留「此處曾有一個值」之痕跡，
  且使 lint 日後可比對兩處。
  **同時加一項一致性檢查**：模組層讀入之值與 write_rows 實際使用者
  須為同一來源，不得各讀一次。

PLACEHOLDER_BODY：保留 TODO 標記，但**移出 unresolved 清單**。
  理由：其無任何使用點，未決不影響任何寫入。留在 unresolved 內
  等於以一個不生效之未決項阻擋整條寫回路徑。
  待 BLOCKED 佔位之寫入路徑實作時再移回。

執行層傾向 (b) 之理由（雙來源即本 feature 一路在防之漂移形態，
而現況恰為「一處已裁定、另一處還是 None」，且 lint 不會發現因兩處
從不比對）—— **採納為本條之依據**。

unresolved 檢查之判準由 `v is None` 改為 `v is None or v == ""`
（§4.1 紅向 2 之已知射程缺口，本包一併補）。
```

## 2. §3 A-TM25 量值 —— 更正，且我的「7」是這樣來的

**(a) 436 處、直雙引號 0 處。** 我原述「用 `“All Profiles”`」語意上像是
「有些地方用了彎引號」，而實情是**五個文字欄中直雙引號一次都沒出現**
—— 交付件並非混用，是整體採用另一套形式。**影響面由「零星幾條」變為
「每一條含 UI 標籤的 TC」。**

**(b) 11 處而非 7 處 —— 成因我可以說明。** 我當時跑的是
「步驟字串去掉編號後之出現次數，取 ≥5 者」，得到
`Read the screen and check whether the popup is displayed  7`。
**那是「該一條特定句子出現 7 次」，不是「`check whether` 共 11 處」。**
我把單一字串之頻次當成該違規之總數報出。

執行層兩種算法都試不出 7 而**只回報差異不臆測成因**，作法正確；
成因在我這邊，現說明如上。

**這與 R-TM31（計數須可歸屬）同族**：我報了一個計數而未說明其量測條件
（哪個欄、相異字串或全部出現、閾值 ≥5），使對造無從重現。

```
A-TM25 量值更正（2026-08-22，依 08 上繳 §3）

(a) 彎引號 `“…”`：**436 處**（J 44 / L 200 / M 192），
    **直雙引號 0 處** —— 非混用，整體採另一套形式。
(b) `check whether` 作主要動詞：**11 處、10 列**（列 104 有兩處），
    全在 L 欄。逐處明細見 08 上繳 §3。

原記之「7 次」為分析層之量測條件未明所致：該數為單一步驟字串
（`Read the screen and check whether the popup is displayed`）之出現頻次，
非該違規之總數。

**一項對交付件有利之補充（08 上繳實測）**：canon §5.1 其餘禁用主要動詞
（`confirm whether` / `observe whether` / `see if` / `observe` / `verify`）
**實測 0 處**。交付件僅在 `check whether` 一項上牴觸 canon，
其餘措辭紀律良好 —— A-TM25 之範圍比「交付件與 canon 不合」窄得多。
```

## 3. §6.2 覆蓋缺口 —— 常數表 v2

執行層以 22 片描述關鍵詞實測，指出 **時區/DST（003/012/013 三片）**
與 **12H/24H 格式（005/011 兩片）** 無任何對應常數，
而 `Zone and DST` 是七個 Test Set 之一整組。

**此為覆蓋問題非措辭問題**（即使原表通過，那五片仍須逐 TC 自寫），
定性正確。補入如下。

### 3.1 常數表 v2（**[PROPOSED]，待 Pei 過目**）

```python
# features/time_management/scripts/tm_constants.py  [PROPOSED v2]
# 依 canon §5.3；本 feature 專屬（08 §3.2 實測：既有專案常數無一適用）

# —— 手動設定 ——
SET_TIME_MANUAL   = 'Open the "Time and Date" settings and set the time manually'
SET_DATE_MANUAL   = 'Open the "Time and Date" settings and set the date manually'

# —— GPS 同步 ——
GPS_SYNC_ON       = 'Set "Sync Time with GPS" to ON'
GPS_SYNC_OFF      = 'Set "Sync Time with GPS" to OFF'

# —— 時區 / DST（v2 新增；003 / 012 / 013）——
SET_TIME_ZONE     = 'Open the "Time and Date" settings and set the time zone'
DST_ON            = 'Set "Daylight Saving Time" to ON'
DST_OFF           = 'Set "Daylight Saving Time" to OFF'
CROSS_TIME_ZONE   = 'Move the vehicle position across a time zone boundary'

# —— 時間格式（v2 新增；005 / 011）——
SET_FORMAT_12H    = 'Set the time format to 12-hour'
SET_FORMAT_24H    = 'Set the time format to 24-hour'

# —— 電源與重置（v2 補 ECU reset）——
KEY_OFF           = 'Turn the ignition to OFF'
KEY_ON            = 'Turn the ignition to ON'
BATTERY_RECONNECT = 'Disconnect and reconnect the vehicle battery'
ECU_RESET         = 'PENDING: DR-8 ECU 軟體重置之操作方式'

# —— CAN ——
CAN_WAKE          = 'Wake the CAN bus'
CAN_SLEEP         = 'PENDING: DR-9 CAN sleep 之可觀察終止條件'

# —— GPS 訊號可用性 ——
GPS_LOST          = 'PENDING: DR-10 Bench 使 GPS 訊號不可用之操作方式'
GPS_RESTORE       = 'PENDING: DR-10 Bench 恢復 GPS 訊號之操作方式'

# —— 讀值 ——
READ_HU_TIME      = 'Read the time shown on the HU display and record it'
READ_IPC_TIME     = 'Read the time shown on the IPC display and record it'
READ_HU_DATE      = 'Read the date shown on the HU display and record it'
```

### 3.2 三處改為 `PENDING: DR-n` 之理由

執行層 §6.1 指出 `GPS_LOST`（Bench 是否有可拔之天線未知）、
`CAN_SLEEP`（`wait until` 無可觀察終止條件）之問題，並正確定性為
**設備問題非措辭問題**。

**依 canon §8.4.3，未知者填佔位而非杜撰。** 我原表之
`Remove the GPS antenna …` 是我對 Bench 設備之推測 —— 該推測無來源，
屬 §8.4.1 所禁。**改為佔位並登記 DR。** `ECU_RESET` 同理（執行層指出
018 需區分 reset / 斷電 / 點火循環三種，而 reset 之操作方式無來源）。

**此三者不阻塞 B1 之生成** —— 生成時該步驟寫佔位，DR 答覆後替換。
但**阻塞該三片 TC 之實際執行**，須於 DATA_REQUESTS 標 Urgency = High。

### 3.3 `CROSS_TIME_ZONE` 之保留意見

該常數假設 Bench 可模擬車輛位置跨時區。**與 `GPS_LOST` 同屬設備問題**，
但我保留具體措辭而非改佔位，理由：GPS 模擬器之位置設定為 GPS 測試之
基本能力，若連位置都不能設，003（GPS Time Calculation）整片皆不可測 ——
**該假設若不成立，問題大於一個常數**。**請執行層於 DR-10 一併問**。

## 4. §8.1 十三處 TODO —— 四處過時，本包指派修訂

執行層之逐處判定（#1 #3 #7 #8 過時或失效、#2 #3 已無作用、七處仍正確）
**分析層覆核同意**。撤除／修訂屬條文範圍，本包指派：

| # | 位置 | 動作 |
|---|---|---|
| 1 | `write_back.py:18` docstring | 修訂措辭：`CONST_FUNCTIONAL_SAFETY` 已由 R-TM57 定案 |
| 3 | `write_back.py:69` `TC_ID_FORMAT` | 依 R-TM59 改為讀 yaml，TODO 撤除 |
| 7 | `write_back.py:328` unresolved 列印字串 | 修訂：該清單與 R-TM10-A1 之關係已變 |
| 8 | `lint_tcs.py:13` docstring | 修訂：Test Set 值與 priority 值域已實作 |

其餘九處**維持不動**。

---

## 5. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM59

`## R-TM59 — 死常數處置採 (b)`，內文為 §1 之區塊全文。
**增量**：`## R-TM` **+1**；`## A-TM` **0**；`## G-TM` **0**。

### T2 — `ANOMALIES.md`：A-TM25 量值更正

條末追加 §2 之區塊全文（原文加刪除線保留 —— R-TM13）。**條數不變。**

### T3 — `write_back.py`：R-TM59 之實作

- `TC_ID_FORMAT` 改讀 `feature.yaml`，加一致性檢查（模組層與 `write_rows`
  同一來源）
- `PLACEHOLDER_BODY` 移出 unresolved，保留 TODO
- unresolved 判準改 `v is None or v == ""`

**red-green**：綠向 —— unresolved 清空、`--write` 之該項阻擋解除；
紅向三個 —— yaml 之 `tc_id_format` 缺失應 raise、值改 `""` 應被攔、
模組層與 `write_rows` 取值不同應被一致性檢查抓到。

### T4 — TODO 四處修訂（§4）

逐處回報改前／改後。

### T5 — `DATA_REQUESTS.md`：登記 DR-8 / DR-9 / DR-10

| DR | 缺件 | 阻塞 | Urgency |
|---|---|---|---|
| DR-8 | ECU 軟體重置（不斷電）之操作方式 | 018 之 reset 情境 TC 執行 | High |
| DR-9 | CAN sleep 之可觀察終止條件 | 021 / 011 之 sleep→wake TC 執行 | High |
| DR-10 | Bench 之 GPS 訊號控制能力（使不可用／恢復／**位置設定**）| 001–005 / 012 / 014 / 015 / 019 之 GPS 情境 TC 執行 | High |

**DR-10 須一併問位置設定**（§3.3）—— 若不可設，003 整片不可測。

**回報所配之實際號碼**（若既有 DR 已用到 8 以上，順延並回報）。

### T6 — `tm_constants.py` **仍不建**

§3.1 為 v2 [PROPOSED]，仍待 Pei 過目。執行層就 v2 提技術面意見
（同 `08` T6 之範圍），特別是：**時區/DST 與格式切換之四條新常數，
其措辭是否可執行**。

### T7 — 驗證（R-TM31 列明細；R-TM46 增量）

```bash
grep -n '^## R-TM59' features/time_management/RULINGS.md
grep -n '量值更正' features/time_management/ANOMALIES.md
grep -n 'TC_ID_FORMAT\|PLACEHOLDER_BODY' features/time_management/scripts/write_back.py
grep -n 'DR-8\|DR-9\|DR-10' features/time_management/DATA_REQUESTS.md
grep -rn 'TODO(' features/time_management/scripts/ | wc -l   # 並逐處列出
python3 features/time_management/scripts/lint_tcs.py --self-test
python3 features/time_management/scripts/build_batch_context.py --self-test
```

**回報 `--write` 之 unresolved 清單為空之實測**（本包之核心成果）。

### T8 — 上繳

`docs/upstream/09_constants.md`。依 R-TM54 三分列未驗清單。

### 不得執行者

- 不動 git（除非 Pei 直接指示）
- **不生成任何 TC**
- **不建 `tm_constants.py`**
- 不修改既有交付件
- 不改 `backend/`、canon、`docs/fw036/framework.md`
- 不將 022 加入 `BOUNDARY_SIGNALS`
- **不杜撰 ECU reset / CAN sleep / GPS 控制之操作方式**（三者為 DR）
- 不碰 `features/vehicle_setting/`
- 不送出 RD-1

---

## 6. 呈報 Pei

1. **§3.1 常數表 v2 待你過目** —— v1 之 13 條增為 21 條，補入時區/DST
   四條、格式二條、ECU reset 與讀日期各一。**三條改為 `PENDING: DR-n`**
   （GPS 控制、CAN sleep、ECU reset）—— 我 v1 的
   `Remove the GPS antenna …` 是**對 Bench 設備的推測，無來源**，
   依 §8.4.1 不得寫入。
2. **DR-8 / DR-9 / DR-10 須向測試團隊問設備**。DR-10 尤其要緊 ——
   若 Bench 不能設 GPS 位置，003 整片不可測，那不是一個常數的問題。
3. **A-TM25 之量值比我原報嚴重**：直引號在交付件中 0 處。若你要求
   與既有交付件外觀一致，須改 canon 或立 profile `[OVERRIDE]`。
4. RD-1 Q-TM1–3 + N-TM1 已備齊，送出屬你。

## 7. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM59 | 分析層裁定，死常數採 (b) | §1 | ✅ T1 + T3 |
| A-TM25 量值更正 | 依 R-TM13 加註 | §2 | ✅ T2 |
| 常數表 v2 | [PROPOSED]，待 Pei | §3.1 | ⏸ T6（不建）|
| DR-8/9/10 | 缺件登記 | §3.2 | ✅ T5 |

分析層本包未動 git、未改任何腳本、未改 canon、未改交付件。
