# 下放包 21 — 四項裁定、A1/A2 補做、寫回就緒

分析層 → 執行層。往返編號 `21`。對應上繳 `docs/upstream/21_writeback.md`。
`20` 受理。**57 條 / 22 片、lint 零發現、dry-run 就緒。**

---

## 1. §6.1 dry-run 抓到之錯 —— **成因是我的指令**

`.pre-arch.json` 四份備份由 `20` §3(1) 之指令建立，
**而該指令未提示其會進入 `load_tcs()` 之 glob**。
若未跑 dry-run 直接寫回，**交付件會有 114 列、每條重複一次**。

執行層之處置正確且其理由值得記：排除以**副檔名樣式**為準而非白名單
——「白名單須隨批次增減維護，而漏維護之後果是少寫一批，
那比多寫一批更難察覺」。**兩種失敗之可見度不對稱，故選可見度高的那種。**

`skipped : 4 個軌跡備份` 之輸出使排除成為可見狀態，非靜默行為。

```
R-TM78（分析層裁定，2026-08-22）—— dry-run 為寫回之必要前置

`write_back` 之 `--write` 前必跑一次不帶 `--write` 之 dry-run，
並**逐項核對其輸出**：`rows` 數、`skipped` 清單、`tc_id` 區間、
`columns` 對映、`unresolved` 是否為空。

不得視為選用之檢查。依據：20 §6.1 —— 首次 dry-run 顯示 114 列而應為 57，
成因為軌跡備份進入 glob；該備份係依下放包指令刻意建立，
而指令未提示其會進入寫回路徑。**建立產物之指令與消費產物之路徑
分屬兩包，無人負責其交集。**

**dry-run 之核對須逐項寫入上繳**，不得只寫「dry-run 通過」——
本次若只看「無錯誤訊息」，114 這個數字不會被注意到。
```

## 2. §2.2 —— **我的 `on CAN-B` 無來源**

`18` §5 T4 我寫「`$DateTmHour$` 在 Atl-Mid 為 `TIME_DATE.Hour1` on CAN-B」。

實測：該 LID 之 Atl-Mid 側 **SignalName 有值、CAN 欄為空**。
訊號名正確，**`on CAN-B` 是我從別的 LID 之網段推的，無來源**。

**這是第四次同型**（v1 推設備、v2 推 UI 開關、v3 推 UI 標籤、本次推網段），
且是在**已立 R-TM49「不得杜撰網段」之後**。條文擋得住生成端，
擋不住我在下放包裡順手寫的例示。

**執行層之三態分辨正確且必要**：

```
無訊號         8 → 不寫任何斷言
有訊號無網段  11 → 訊號可寫，segment 寫 DR-6 佔位   ← Atl-Mid 側全部
有訊號有網段  19 → 照用
```

「合併二者會使處置錯誤 —— 前者不該寫，後者該寫而標缺件」**成立**。
**DR-6 對 Atlantis Mid 未解除**，`DATA_REQUESTS.md` 須據此更新其狀態
（現記為已由 LID 表解除，該記載只對 Atl-Hi 成立）。

## 3. §0 條數計數 —— R-TM46 須兼計刪除線標題

撤回條改為 `## ~~R-TM62 …~~` 後不再匹配 `^## R-TM`，
致標題計數 78 而實際條文 80。

```
R-TM79（分析層自裁，2026-08-22）—— 條數檢查須兼計撤回條

R-TM46 之增量檢查，其計數樣式須兼計刪除線標題：

    grep -cE '^## (~~)?R-TM'

理由：R-TM13 要求撤回條加刪除線保留，而刪除線改變了標題之字面，
使其脫離既有計數樣式。**兩條規則各自正確，其交互作用使計數失準** ——
與 R-TM69(3)（條文變更須檢查以該欄位為判準之既有閘門）同族。

上繳須同時回報兩個數（含撤回、不含撤回），使差額可見。
```

## 4. §2.5 —— 值得單獨記一句

> 舊判準只驗「reasoning 有記錄架構欄」。而 `11`–`17` 九輪中每條 TC 都記了
> `Atlantis High (col 26-30)` —— **記錄完備，而記錄的內容整整九輪都是錯的。**

**這是 A-TM26 之強制記錄要求最完整的一次驗證，也是最完整的一次否證。**
記錄之存在使人相信該面向已受控，而其內容錯誤無人察覺 ——
`14` §1.2 已把該射程限制寫入 docstring，本次即為其實例化。

新判準（記錄須與 Pre-Condition 之架構限定一致）**是正解**：
它把記錄綁到另一個獨立來源，使兩者不一致時可被發現。

**不另立條文** —— R-TM52（綠向須驗內容非退化）已涵蓋其原理，
本例併入該條之註記。

## 5. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM78 / R-TM79；R-TM52 加註（§4）

**增量**：`## R-TM`（兼計撤回）**+2**。回報含撤回與不含撤回兩個數。

### T2 — `DATA_REQUESTS.md`

- **DR-6 之狀態更正**：由「已由 LID 表解除」改為
  **「Atlantis High 已解除；Atlantis Mid 未解除（11 個 LID 有訊號無網段）」**
- DR-21（兩份同名 HMI Settings List）已登記，維持

### T3 — A2：015 之顯示前提（§1.4）

`Set Date is only shown for vehicles in which the cluster does not have
data needed to reference date`（原文 typo `Set Dateis` 保留於引用）。

**寫入 015 相關 TC 之 Pre-Condition**，措辭依該註記與 4814000
（`If the HU has No GPS, the HU shall provide a manual method…`）同向，
**不得自擬超出兩者之條件**。

### T4 — A1：017 之跨架構拆分

017 判為 `Both`，其 TLM 斷言因取 Atl-Hi 欄而 `excluded`。
**該片之 Atl-Mid 部分需 TLM 斷言。**

**處置**：017 之相關 TC 拆為兩組 —— Atl-Hi 一組（現行內容，加 Atl-Hi
限定行）、Atl-Mid 一組（TLM 斷言取欄 16–20，加 Atl-Mid 限定行，
segment 依 §2 之三態處置）。

**若拆分後條數改變，回報前後條數與新 tc_id 區間** ——
tc_id 依位置賦號（canon §10.3），拆分會改變其後全部編號。

### T5 — 重跑全批驗證

```bash
python3 features/time_management/scripts/lint_tcs.py --self-test
python3 features/time_management/scripts/build_batch_context.py --self-test
python3 features/time_management/scripts/lint_tcs.py
python3 features/time_management/scripts/write_back.py --feature-dir features/time_management
```

**dry-run 之輸出逐項核對並寫入上繳**（R-TM78）：`rows`、`skipped`、
`tc_id` 區間、`columns`、`unresolved`。

### T6 — 上繳

`docs/upstream/21_writeback.md`。**依 R-TM74 列逐 T 對照表。**

**本包不寫回。** `--write` 待 Pei 放行。

### 不得執行者

- **不動 git；不加 `--write`**
- 不刪除 `.pre-arch.json`
- 不改 `Clock` 之頁名（A-TM28 未裁）
- 不建 `tm_constants.py`；不送 RD-1
- 不碰 `features/vehicle_setting/`

---

## 6. 呈報 Pei —— **就緒，等你一句**

| 項 | 數 |
|---|---|
| TC | **57 條**（T4 拆分後可能微增）|
| leaf 覆蓋 | **22 / 22**，無遺漏無重複 |
| lint | **0 項發現** |
| 佔位 | **49 處**，其中 23 為 DR-12b 記號；扣除後 **26 處** |
| 真正卡上游文件者 | **DR-5 四處 + DR-6 一處** |
| 設備類（問測試團隊可解） | **21 處** |

**寫回只差你一句放行。** 兩件屆時要知道：

1. **`surgical_save` 之寫入路徑至今從未執行** —— G-TM3 之正向驗證
   （寫回後重開檔比對指定 cell）是唯一能發現「讀碼推論與實際行為不符」
   之機制。
2. **dry-run 已抓到一次會毀掉交付件的錯**（114 列 vs 57 列）。
   若當時直接寫回，交付件每條重複一次而 lint 不會報 ——
   lint 檢查 TC 內容，不檢查工作簿列數。

**A-TM28（`Clock` / `Clock & Date`）影響 23 條，寫回後改動成本更高。**
你若能在寫回前確認，那 23 條的 DR-12b 記號可一併移除。

## 7. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM78 | 分析層裁定，dry-run 必跑 | §1 | ✅ T1 + T5 |
| R-TM79 | 分析層自裁，條數兼計撤回條 | §3 | ✅ T1 |
| R-TM52 註記 | 記錄完備而內容錯誤之實例 | §4 | ✅ T1 |
| DR-6 狀態更正 | Atl-Mid 未解除 | §2 | ✅ T2 |

分析層本包未動 git、未改任何腳本、未改任何 TC。
