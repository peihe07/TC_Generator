# 下放包 20 — 收尾包：B1–B3 重生成、B4 生成、DR-12b 記號

分析層 → 執行層。往返編號 `20`。對應上繳 `docs/upstream/20_final.md`。

**本包不新增任何條文。** 合併 `18`（架構更正）與 `19`（HMI 標籤）之
未執行指令，加 B4 生成，一次跑完。

**Pei 2026-08-22 指示**：其餘缺口留佔位，不再追 —— 常數表 v3 不建、
RD-1 不送、A-TM25 依 canon 不追既有交付件。**本包不再提請該三項。**

---

## 1. 前置：`18` 與 `19` 之條文落檔（若未做）

`18`、`19` 兩包之上繳皆未回。**若其 T 項尚未執行，本包 T1 先補**：

- `18` T1–T3：R-TM75/76/77 入 `RULINGS.md`；R-TM62 / R-TM63 加刪除線
  保留並註記；A-TM27 結論作廢事實保留；A-TM26 加訂正段；
  DR-11 標 **CANCELLED**（不刪列）
- `19` T1–T3：新版 HMI Settings List 入 `inputs/`；舊版標 SUPERSEDED；
  DR-12 → RESOLVED；A-TM28 + DR-12b 登記

`18` T3 之工具連動（`tm_rulings` / context / lint）為 T2 之前置。

## 2. T2 — 工具連動（`18` T3）

1. `load_ee_arch()` 之 `is_atl_hi` 改為**目標架構標記**
   （`Atlantis High` / `Atlantis Mid` / `Both`）
2. `arch` 段**不再產生 DR-11 佔位**，改輸出該物件之架構
   與 R-TM76 所需之 Pre-Condition 行
3. `load_lid_table()` 依 TC 之目標架構取欄：
   **Atl-Hi → 欄 26–30；Atl-Mid → 欄 16–20**。
   `TLM_MANAGED_*` 於 Atl-Mid 之 TC 取欄 16–20 之值（R-TM62 已撤回）
4. lint：移除 DR-11 判準；`lint_arch_column` 改驗
   「記錄之架構欄與該 TC 之 Pre-Condition 架構行一致」；
   `lint_placeholder_completeness` 之應有集合移除 Atl-Mid 項

**各附 red-green，紅向依 R-TM67 加構造複驗。**

## 3. T3 — **B1–B3 重生成**（採 (乙)）

分析層 `18` §5 T4 傾向 (乙) 重生成，**本包確定採之**。

理由（`18` §5 已述，此處重申供執行時對照）：受影響者不只
`spec_reference` 一欄 —— 訊號斷言之 MESSAGE 與 segment 依架構而異
（`$DateTmHour$` 在 Atl-Mid 為 `TIME_DATE.Hour1` on CAN-B，
非 `TELEMATIC_FD_1.Hour1_TLM` on FD），Pre-Condition 亦須加架構行。

**重生成之對照要求**（使重生成不致丟失既有成果）：

1. **B1 之原 19 條保留為 `generated/B1.pre-arch.json`**（不覆蓋、不刪除）
   —— 其已通過 pilot 覆核，是唯一經人工看過的樣本，
   重生成後之比對基準（R-TM13 之同一精神）
2. B2 / B3 同樣保留 `.pre-arch.json`
3. 重生成後**逐條比對新舊**，回報：
   - 條數是否相同（不同即回報成因）
   - 每條之 `test_item` 上半是否逐字不變（應不變 —— 架構更正不動需求原文）
   - `spec_reference` 由佔位改真值之處數
   - 新增之 Pre-Condition 架構行處數
   - 訊號斷言之 MESSAGE / segment 改變之處數

4. **`14` 之四項修正須在重生成後仍然成立**（否則等於回退）：
   - TC#3 之 `greyed out` 收斂（不得改回 `unavailable`）
   - 六條 `input_test_data` = `NA`
   - S1 之 `The HU main screen is displayed` 已刪
   - S3 之步驟措辭

   **逐項複驗並回報。**

## 4. T4 — DR-12b 記號（Pei 指示之唯一例外）

`Open the "Clock" settings` 出現之全部 TC，其 Remarks 加一行：

```
PENDING: DR-12b 設定頁名（Clock 或 Clock & Date）待確認
```

**值照留 `Clock` 不改** —— A-TM28 未裁定前，`Clock` 為文件字面值。
記號之目的是使「已寫入之值可能需改」成為可見狀態，
而非宣告該值為缺件。

**Remarks 依 R-TM68 升冪排列**（DR-5 → DR-8/9/10 → DR-12b → DR-20）。

## 5. T5 — DR-12 之值寫入

B1 之 007 一處佔位改為 `"Show Time in Status Bar"`，
reasoning 註明來源（HMI Settings List R1L-R 2026-02-13 §7-5，
Technical Reference `CFTS015`）。

**不得寫入 `Show Time During Screen Off` 或
`Show Time and Date During Screen Off`** —— 該二項 Technical Reference
為 **CFTS022**，屬他 feature 範圍（§8.4.2）。

## 6. T6 — **B4 生成**（最後一批）

`013, 015, 022` 三片。

| leaf | 注意事項 |
|---|---|
| **013** DST Handling | 依 R-TM60 無手動 DST 開關；觸發為 `CROSS_DST_BOUNDARY`（`PENDING: DR-10`）。spec 錨為 4813995（`adjusted automatically`），**單一物件** |
| **015** Manual Date Handling | 標籤用 `Set Date Day` / `Set Date Month` / `Set Date Year`（`19` §4 逐字）。**父項三種區域排序，不得寫死其一** —— 不限定區域則寫 `Set Date`，限定則加 `$Country_Code$` 之 Pre-Condition 並用對應排序，子項步驟序隨之。<br>另讀出 `19` §4(4) 之截斷註記全文（`Set Date is only shown for vehicles…`），若其為顯示前提，寫入 Pre-Condition |
| **022** SNA Handling | **B-2 界線之另一側**：022 **得**涵蓋 SNA 送出規則（該規則屬 022），**不得**涵蓋 GPS 值之送出正確性（屬 014）。014 已在 B2，其寫法可作對照 |

**生成後跑 lint，回報全部發現，不預先修正。**

## 7. T7 — 全批驗證

```bash
python3 features/time_management/scripts/lint_tcs.py --self-test
python3 features/time_management/scripts/build_batch_context.py --self-test
python3 features/time_management/scripts/lint_tcs.py   # 對 B1–B4 四檔
ls features/time_management/generated/
grep -c '^## R-TM' features/time_management/RULINGS.md
```

回報：

1. 四批之總 TC 數與總 leaf 數（**期望 leaf = 22，無遺漏無重複**）
2. lint 對四檔之全部發現
3. **佔位總數與逐 DR 分佈**（先前僅有估計值，本次取實測）
4. `PENDING: DR-11` 之殘留數 —— **期望 0**

## 8. T8 — 上繳

`docs/upstream/20_final.md`。**依 R-TM74 列逐 T 對照表**（T1–T8 全列）。
依 R-TM54 三分列未驗清單。

**本包完成後，剩餘工作僅為寫回與交付**，故上繳須額外含：

- **寫回前之就緒檢查**：`write_back --feature-dir` 之 dry-run 輸出
  （unresolved 應為空、欄位對映、tc_id 區間），**不加 `--write`**

### 不得執行者

- **不動 git**；**不寫回工作簿**（本包止於 dry-run）
- 不刪除 `.pre-arch.json` 備份
- 不刪除 R-TM62 / R-TM63 / A-TM27 / DR-11 之原文
- 不改 `Clock` 之頁名（A-TM28 未裁）
- 不寫入 CFTS022 之兩項
- 不建 `tm_constants.py`；不送 RD-1（Pei 已指示）
- 不縮減任何 leaf 之覆蓋
- 不改寫 test_item 上半之 verbatim
- 不預先修正 B4 之 lint 發現
- 不碰 `features/vehicle_setting/`

---

## 9. 呈報 Pei

本包完成後：**22 片全覆蓋、四批 TC 生成完畢、lint 全綠、dry-run 就緒**。

其後只剩兩步：

| 步 | 內容 | 誰 |
|---|---|---|
| 寫回 | `surgical_save` 首次實跑 + G-TM3 正向驗證 | 執行層（需你一句放行）|
| 交付 | git、tag、DELIVERY.sha256 | **你** |

**寫回時要知道的兩件**：

1. `surgical_save` 之寫入路徑**至今從未執行過** —— 全部評估皆為讀碼與
   唯讀探測。G-TM3 之正向驗證（寫回後重開檔比對指定 cell）是唯一能發現
   「讀碼推論與實際行為不符」之機制。
2. 母本 R 欄之 x14 下拉**不可用 openpyxl 存回**，唯一路徑為
   `xlsx_surgical.py`。

**交付件會帶著約 25–30 處佔位出去**（DR-5 二、設備類約 20、DR-12b 六），
每一處是測試執行時的斷點 —— 這是你已知並接受的。

## 10. 本包產生之新條文清單（自檢 —— R-TM14）

**無。** 本包為既有裁決之執行，未新增條文。

分析層本包未動 git、未改任何腳本、未改任何 TC。
