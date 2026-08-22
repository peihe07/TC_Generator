# 下放包 07 — BOUNDARY_SIGNALS 補 018 / 017（**不補 022**）、守衛可獨立呼叫

分析層 → 執行層。往返編號 `07`。對應上繳 `docs/upstream/07_boundary.md`。
`06Z` 受理，`06` 往返結案。

**§2.4 之三處提請，分析層只准兩處。** 022 那處若補會產生誤報，見 §2。

---

## 1. §2.3 之自我更正 —— 受理，且形態值得記

「三條自動判準」實為三個 **leaf** 在表內，非三對鄰接有判準。
成因（`lint_boundary` 首行 `BOUNDARY_SIGNALS.get(leaf)` 不在即
`return []`，故一對之兩側只有一側在表內時另一側完全不檢查）**診斷正確**。

自我定性亦正確：**以資料表之成員資格代替實際覆蓋**，與 C-2 之
「以無 gap 即通過代替 gap 非空」同型，即 R-TM52 之形態發生在回報而非
程式碼。

**改以「逐對造違規 TC 送 `lint_boundary` 實跑」為判定方式，是本包最重要
的方法改進** —— 「該片在表內」與「該對之違規抓得到」是兩件事，
前者可讀表得知，後者只能實跑。往後涉及「某檢查是否涵蓋某情形」之陳述，
一律以實跑為準。

## 2. §2.4 三處「可測而未測」—— **准兩處，駁一處**

### 2.1 018（B-3）與 017（B-5）—— 准

**018**：其能力為「reset／斷電後之時間日期**值**之初始化」，
格式（12H/24H）之保存與重送屬 011（B-3 之界線原文）。
故 018 之 TC 提及 `$DateTmFormat$` 為越界，加入 `not_ours` 正確。

**017**：其能力為「日期**通道**」（`TELEMATIC_TIME_DATE` + TLM LIDs 至
IPC），GPS 來源值之送出屬 014（B-5 之界線原文）。
故 017 之 TC 提及 `$GPSDateTm` 為越界，加入 `not_ours` 正確。

### 2.2 022（B-2）—— **駁回，補之會誤報**

執行層提「022 之 TC 提 `$GPSDateTm`（014 owns）→ 抓不到」為射程未及。
**分析層不採**，理由如下：

B-2 之界線原文為：

> 014 描述含「or SNA if unavailable」，但 **SNA／預設值之送出規則屬 022**；
> 014 只驗 GPS 資料之送出。

即 **022 對 `$GPSDateTm*$` 這組訊號有正當管轄** —— 它擁有「無效／不可用時
送 SNA 進這些訊號」之規則。CFTS015 物件 `4814105` 逐字為：
`set "SNA" into BH-CAN message for each signal involved time and date.`
其後即列 `$GPSDateTmHour$` 等六訊號。

**故 022 之 TC 提及 `$GPSDateTm` 是條文要求它提及，不是越界。**

**B-2 之區辨軸是「條件與值」（GPS 值 vs SNA 值），不是訊號名** ——
兩片合法地共用同一訊號組。以訊號名為判準必然誤報 022 之正常內容，
而誤報之後果比漏抓更惡劣（`06` §4.3 已立：誤報主動製造雜訊使其他防線失效）。

**B-2 維持「無自動判準」，其驗證責任歸 B1 pilot。**

```
R-TM55（分析層裁定，2026-08-22）—— BOUNDARY_SIGNALS 增列 018 與 017

tm_rulings.BOUNDARY_SIGNALS 增列兩片之 not_ours：

  018 Default Initialization
      owns     ：（無；其能力為值之初始化，無專屬訊號）
      not_ours ：$DateTmFormat$          ← 011 owns（B-3）
  017 Date Transmission
      owns     ：（無；其能力為通道，TELEMATIC_TIME_DATE / TLM LIDs）
      not_ours ：$GPSDateTm              ← 014 owns（B-5）

**022 不增列。** B-2 之區辨軸為「條件與值」（GPS 值 vs SNA 值），
非訊號名 —— 022 對 $GPSDateTm* 有正當管轄（CFTS015 物件 4814105：
`set "SNA" into BH-CAN message for each signal involved time and date.`
其後列六訊號）。以訊號名為判準必然誤報其正常內容。

增列後之預期覆蓋：B-3 / B-5 由「無」轉為**單向有**（僅 018 側 / 017 側
被守，另側仍無訊號可測）；B-2 維持「無」。
B-1 原理上不可自動化（雙側皆無訊號可比）。

`owns` 為空之片，`lint_boundary` 須能處理（現行以 `.get(leaf)` 取整筆
規則，`owns` 空集不得使其誤判）—— **實作時須有紅綠雙向證明**。
```

## 3. §3.2 之方法改進 —— 立為條文

> 守衛若只存在於產生函式內部，其正確性原理上無法被獨立測試，
> 只能靠「產生函式恰好產出壞值」的間接路徑。

**這比修正該次構造更有價值**，且解釋了為何首次紅向失敗不是守衛失效
而是構造錯誤 —— 兩者在現象上相同（紅向未 raise），成因不同。

```
R-TM56（分析層自裁，2026-08-22）—— 守衛須抽為可獨立呼叫之函式

執行期守衛不得只內嵌於產生函式之流程中，須抽為**接受待驗值、
可獨立呼叫**之函式（如 `assert_rendered(r)`）。

理由：內嵌之守衛只能經由「使產生函式恰好產出壞值」之間接路徑測試，
而該路徑往往被產生函式自身之其他邏輯阻斷（monkeypatch 回傳後才改值時，
守衛早已跑過）。**守衛之正確性原理上無法被獨立驗證，即等同未驗。**

判準：該守衛能否以一行 `assert_x(<壞值>)` 直接觸發？不能 → 須抽出。

依據：06Z 上繳 §3.2 —— C-3 首次紅向未 raise，成因為構造錯誤而非守衛
失效，兩者現象相同；抽出獨立函式後三個紅向皆正確 raise。
```

## 4. §3.1 `len()` 守衛 —— 記入 R-TM31 之註記

> 我把 key `"002"` 改為 `"_x"`，長度仍為 2 …… `len()` 對「內容被替換但
> 數量相同」不敏感 —— 正是 R-TM31 所指之計數盲點，
> 而我把它寫進了為防止裁決值遺失而設的守衛裡。

**同一盲點出現在為防止它而設的機制內部** —— 此即本 feature 反覆出現之
「防護規則與其防護對象同形」（`01Z-A4` 已登記為 canon 再同步候選）之
第二個實例。

不另立條文，以註記併入 R-TM31（T1(c)）。

## 5. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`

**(a)** 追加 R-TM55、R-TM56，標題行
`## R-TM55 — BOUNDARY_SIGNALS 增列 018 與 017`、
`## R-TM56 — 守衛須抽為可獨立呼叫之函式`，內文為 §2.2 / §3 之區塊全文。

**(b)** R-TM53 之回報段追加 §2.2 之駁回理由（B-2 為何維持「無」），
使日後讀者不會重提同一補入。

**(c)** R-TM31 條末追加：

```markdown
**計數盲點出現於守衛內部（2026-08-22，06Z 上繳 §3.1）**

`tm_rulings.py` 之首版模組載入斷言以 `len()` 檢查常數完整性，
而 key 改名（`"002"` → `"_x"`）使長度不變即漏網 —— **本條所指之計數
盲點，出現在為防止裁決值遺失而設的守衛內部**。已改驗 key 集合。

此為「防護規則與其防護對象同形」之第二實例（第一實例：01Z-A4 之
負向後查 regex 自我抵銷，已列為 canon 再同步候選）。
```

**增量**：`## R-TM` **+2**；`## G-TM` **0**；`## A-TM` **0**。

### T2 — `tm_rulings.py`：增列 018 / 017（R-TM55）

含 `owns` 為空之處理。**模組載入斷言須同步更新**
（`BOUNDARY_SIGNALS` 之 key 集合由三片變五片）。

### T3 — `lint_boundary` 之 `owns` 空集處理

紅綠雙向：

- **綠向**：018 之正常 TC（提 `$DateTmHour$` 等值相關訊號）不報
- **紅向**：018 之 TC 提 `$DateTmFormat$` → 報 boundary
- **綠向**：017 之正常 TC（提 `TELEMATIC_TIME_DATE`）不報
- **紅向**：017 之 TC 提 `$GPSDateTm` → 報 boundary
- **陰性對照（必做）**：**022 之 TC 提 `$GPSDateTm` 仍不報**
  —— 證明 R-TM55 之駁回確實落實，非一併補入

### T4 — 對照表更新（六對）

依 T2/T3 之實測結果重出 B-1…B-6 對照表，**判定方式仍為逐對實跑**
（不以成員資格代替）。兩處落檔（`tm_rulings.py` 檔頭 + `RULINGS.md`
R-TM53 回報段）逐字相同。

預期：B-4 / B-6 雙向有；B-3 / B-5 **單向有**；B-1 / B-2 無。
**以實測為準，不符即回報。**

### T5 — 驗證（R-TM31 列明細；R-TM46 增量）

```bash
grep -n '^## R-TM5[56]' features/time_management/RULINGS.md
grep -n '計數盲點出現於守衛內部' features/time_management/RULINGS.md
grep -n '022' features/time_management/scripts/tm_rulings.py   # 應不在 BOUNDARY_SIGNALS
python3 features/time_management/scripts/lint_tcs.py --self-test
python3 features/time_management/scripts/build_batch_context.py --self-test
python3 -c "import sys; sys.path.insert(0,'features/time_management/scripts'); import tm_rulings; print(sorted(tm_rulings.BOUNDARY_SIGNALS))"
```

末項期望：五片（008 / 011 / 014 / 017 / 018），**不含 022**。

### T6 — 上繳

`docs/upstream/07_boundary.md`。依 R-TM54 三分列未驗清單。
須含 T5 全部輸出、T3 五項紅綠與陰性對照、T4 之六對實測表。

### 不得執行者

- 不動 git（除非 Pei 直接指示）
- **不生成任何 TC**
- **不將 022 加入 `BOUNDARY_SIGNALS`**（R-TM55）
- 不改 `backend/`、不改 canon、不改 `docs/fw036/framework.md`
- 不修改任何既有上繳包或下放包
- 不填 `functional_safety`、不杜撰 CAN 網段
- 不動 `TODO(R-TM10-A1)` 之步驟措辭常數與 ER 樣板
- 不碰 `features/vehicle_setting/`
- 不送出 RD-1

---

## 6. 呈報 Pei —— 待你之兩項（第四次）

依 R-TM54，此二項已移出執行層待辦，改列「待 Pei」：

1. **`functional_safety` 之值**（A-TM24）
2. **步驟措辭常數與 ER 樣板**（R-TM10-A1）—— (a) 解除並指定樣式來源，
   或 (b) 本 feature 自擬。**選 (b) 我下一包直接擬常數表。**

管線技術面在 `07` 之後即備妥；**B1 之啟動只等這兩項。**

## 7. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM55 | 分析層裁定，增列 018/017、駁回 022 | §2.2 | ✅ T1(a) + T2 + T3 |
| R-TM56 | 分析層自裁，守衛須可獨立呼叫 | §3 | ✅ T1(a) |
| R-TM53 回報段補駁回理由 | 防止重提同一補入 | §2.2 | ✅ T1(b) |
| R-TM31 註記 | 計數盲點出現於守衛內部 | §4 | ✅ T1(c) |

分析層本包未動 git、未改任何腳本、未改 canon、未改 `backend/`。
