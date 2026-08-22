# 下放包 18 — 架構範圍更正：撤回 R-TM62 / R-TM63，DR-11 取消

分析層 → 執行層。往返編號 `18`。對應上繳 `docs/upstream/18_arch.md`。

**本包撤回兩條裁決、取消一個 DR、修正一條 anomaly 之前提。**
成因為分析層之範圍推定錯誤，證據一直在手上而未使用。

---

## 1. 實測 —— 35 個 Atl-Mid 物件全部標為 R1L / R1L-R

分析層對 CFTS015 之 269 個物件擷取三種標籤
（`[EE Architecture:...]`、`[Radio:...]`、`[ECU:...]`），
比對 037 引用之 35 個 Atl-Mid 專屬物件：

```
Radio 標籤含 R1L 或 R1L-R 者：35 / 35   （100%）
ECU 標籤：LTM                 35 / 35   （100%）
```

其形態為 `R1L-R, R1L`（18 筆）或 `VP2Rxx, R1L-R, R1L, …`（17 筆），
**無一例外**。

**本專案為 R1LR（= R1L-R）。** 故該 35 個物件之 Radio 維度**正是本專案**，
其 Atl-Mid 為 **EE architecture 維度之另一個變體**，非「別的專案」。

### 1.1 交付件之佐證

`FM-WI-FSM-036-A01` 母本之車型欄七欄：

```
T HDCC27  Atl-Hi     U DT27  Atl-Hi
V ProMaster637 / W Commander598 / X Renegade5210 / Y Toro2261 / Z Fastack376  —— 皆 Atl-Mi
```

**七欄中五欄為 Atl-Mi。036 工作簿本身即為雙架構設計。**
此證據我引用過（`vehicle_setting` 之 feature.yaml 註記 `Z 為 Fastack (376) Atl-Mi`），
卻未用於本 feature 之範圍判斷。

### 1.2 我錯在哪裡

我由 spec 檔名 `R1LR_Atl-H_25PI3.5_Cabin_CFTS_015` 之 `Atl-H` 推得
「本 feature 為 Atl-H」，寫入 Part VII，其後四層裁決疊在其上。

**檔名之 `Atl-H` 是該 CFTS 版本之標示，不是本 feature 之驗證範圍** ——
而該文件內含整支 §1.5.2（Atl-Mid / LTM / R1L），037 也引用了它。
**若範圍真為 Atl-H only，037 不會引用它們。**

**這是「以檔名代替內容」** —— 與 A-TM26 之「以第一欄代替正確欄」、
R-TM66 之「以字串形態代替資料性質」同族，只是發生在最上游，
故其後所有裁決一併受污染。

## 2. 撤回與更正（五項）

```
R-TM75（分析層裁定，2026-08-22）—— 本 feature 涵蓋 Atl-Hi 與 Atl-Mid 兩架構

依 §1 之實測：037 引用之 35 個 Atl-Mid 專屬物件，其 Radio 標籤
35/35 含 R1L / R1L-R（即本專案），ECU 標籤 35/35 為 LTM。
036 母本之七個車型欄中五欄為 Atl-Mi。

**本 feature 之驗證範圍涵蓋 Atlantis High 與 Atlantis Mid 兩種
EE architecture**，以 Radio 維度（R1L / R1L-R）為專案界線。

隨之撤回／更正：

(1) **R-TM63 撤回。** Atl-Mid 物件之引用寫**真值** `CFTS015-{objid}`，
    不寫 `PENDING: DR-11`。R-TM63 之「覆蓋不縮減」原則本身正確且維持
    —— 錯的是其處置前提。

(2) **DR-11 取消。** 其所登記之缺件（Atl-H 對應需求）不存在 ——
    那些需求本就是本專案的。約 40 處佔位改為真值。

(3) **A-TM27 之結論作廢，事實記載保留。** 「35 個物件標為 Atl-Mid」
    為真；「架構不符」為偽。依 R-TM13 加註不刪。

(4) **R-TM62 撤回。** 五個 `TLM_MANAGED_TIME_DATE_*` LID 在 Atlantis 欄
    有值，**適用於 Atl-Mid 之 TC**。017 / 020 之相關斷言得寫。

(5) **A-TM26 修正**：架構欄之選取**依該條 TC 之目標架構**而定 ——
    Atl-Hi 之 TC 取欄 26–30、Atl-Mid 之 TC 取欄 16–20。
    **強制記錄之要求不變且更形重要**：須記錄取自哪一欄，
    因現在兩欄都可能是對的，取錯更難察覺。
```

## 3. 架構限定寫入 Pre-Condition（Pei 指示）

Pei 2026-08-22：「如果只限定在某個車型，只要做那個車型，
Pre-Condition 加上 Atl-Mid 或是 High only 之類的」。

**交付先例存在**：User Profiles 交付件之 Pre-Conditions 有
`The vehicle is an R1 High variant`（11 條）—— **變體限定寫 Pre-Condition
之機制已在交付件中使用**。

**但該先例之維度是 radio variant（R1 High），本 feature 需要的是
EE architecture 維度。** 措辭須自定，形式比照。

```
R-TM76（分析層裁定，2026-08-22）—— 架構限定之 Pre-Condition 措辭

某條 TC 若只適用於單一 EE architecture，其 Pre-Condition 加一行：

    The vehicle is an Atlantis High architecture variant
    The vehicle is an Atlantis Mid architecture variant

**取值來源**：CFTS015 物件之 `[EE Architecture:...]` 標籤值逐字
（`Atlantis High` / `Atlantis Mid`），非自擬簡稱（不寫 `Atl-Hi` / `High only`）。

**加與不加之判準**：
- 該 TC 之全部引用物件皆為單一架構 → **加**該架構之限定行
- 引用物件跨兩架構 → **不加**（該行為適用於兩者之共通行為）
- 引用物件標為 `All` → 不加

canon §4.4 之允許類型含「system version / mode」（如 `Dev / Pre-Prod
build only`），架構變體屬同類，為合法之 Pre-Condition。

**置於 Pre-Condition 之首行**，使審閱者一眼見其適用範圍。
```

## 4. 車型欄 T–Z —— 依交付先例留空

實測 User Profiles 交付件之 T–Z 七欄：**189/189 全空**，
無任何 TC 勾選車型。

```
R-TM77（分析層裁定，2026-08-22）—— T–Z 車型欄留空

`feature.yaml` 之 T–Z 七欄由 `TODO(R-TM10-A1)` 改為
`BLANK_BY_DECISION`，理由：交付件 UserProfiles_20260820 之該七欄
189/189 全空，**車型欄在既有交付實務中不作為範圍標示之用**。

範圍標示改由 Pre-Condition 承載（R-TM76）。

**此項自 `04` 起掛在 `TODO(R-TM10-A1)` 下未裁，而它正是會逼分析層
去看架構的那一步** —— 我未將其視為阻塞項，反而繞過它推定架構。
記於此，因該疏漏是 §1.2 之錯誤能存活四輪的原因之一。
```

## 5. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM75 / R-TM76 / R-TM77；四項撤回加註

R-TM62 / R-TM63 **依 R-TM13 加刪除線保留**，其下加註指向 R-TM75。
A-TM27 之結論段同樣處理（事實記載保留）。
A-TM26 依 R-TM75(5) 加訂正段。

**增量**：`## R-TM` **+3**。

### T2 — `DATA_REQUESTS.md`：DR-11 取消

標 **CANCELLED**，理由逐字為 R-TM75(2)。**不刪除該列**（軌跡）。
DR-5 不受影響（其為真實之 CFTS 缺件）。

### T3 — `tm_rulings` / context / lint 之連動

1. `load_ee_arch()` 之 `is_atl_hi` 語意由「是否適用」改為
   **「目標架構標記」**，取值 `Atlantis High` / `Atlantis Mid` / `Both`
2. `arch` 段**不再產生 DR-11 佔位**，改輸出該物件之架構與
   R-TM76 所需之 Pre-Condition 行
3. `load_lid_table()` 依 TC 之目標架構取欄（26–30 或 16–20），
   `TLM_MANAGED_*` 於 Atl-Mid 之 TC 取欄 16–20 之值（R-TM75(4)）
4. lint：**移除 DR-11 相關判準**；`lint_arch_column` 之要求改為
   「記錄之架構欄須與該 TC 之 Pre-Condition 架構行一致」
5. `lint_placeholder_completeness` 之應有集合**移除 Atl-Mid 項**

**各附 red-green，紅向依 R-TM67 加構造複驗。**

### T4 — B1 / B2 / B3 之重生成或修補

49 條中受影響者：**全部含 DR-11 佔位之條**（B1 14 處、B2 18 處、
B3 之 017/019/020）。

**擇一並回報所擇與理由**：
- **(甲) 修補** —— 佔位換真值、加 R-TM76 之 Pre-Condition 行、
  訊號斷言依目標架構重取
- **(乙) 重生成** —— 三批全部重跑

**分析層傾向 (乙)**：受影響者不只 spec_reference 一欄 ——
訊號斷言之 MESSAGE 與 segment 依架構而異（`$DateTmHour$` 在 Atl-Mid 為
`TIME_DATE.Hour1` on CAN-B，非 `TELEMATIC_FD_1.Hour1_TLM` on FD），
Pre-Condition 亦須加行。**修補之涉及面與重生成相當，而重生成之一致性較高。**

**惟 B1 已經 pilot 覆核**，重生成即作廢該覆核。故若擇 (乙)，
**B1 之重生成須再覆核**（分析層負責前 7 條，同 `14`）。

### T5 — B4 生成（若尚未做）

`013, 015, 022` 三片，依本包之新規則。

### T6 — 上繳

`docs/upstream/18_arch.md`。**依 R-TM74 列逐 T 對照表。**
依 R-TM54 三分列未驗清單。

### 不得執行者

- 不動 git；**不寫回工作簿**
- 不刪除 R-TM62 / R-TM63 / A-TM27 / DR-11 之原文（R-TM13）
- 不縮減任何 leaf 之覆蓋
- 不改寫 test_item 上半之 verbatim
- 不碰 `features/vehicle_setting/`

---

## 6. 呈報 Pei

**約 40 處佔位是我自己造出來的，本包取消。** 剩餘佔位由 85 降至約 45，
且其中 20 處（DR-8/9/10/20）是**你去問測試團隊當天可解**的設備問題，
真正卡在上游的只剩 DR-5 兩處與 DR-12 一處。

**一項要你裁**：§5 T4 之 (甲) 修補 vs (乙) 重生成。
我傾向 (乙)，但那會作廢 B1 已完成之 pilot 覆核，需再跑一次。

**另一項要你知道**：這個錯能存活四輪，直接原因是我由檔名推架構；
但**結構原因是 T–Z 車型欄自 `04` 起掛著 TODO 從未裁定** ——
那七欄裡五欄寫著 Atl-Mi，只要當時去填它就會撞見這件事。
我把它當成可延後的欄位，而它其實是範圍問題的入口。

## 7. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM75 | 分析層裁定，雙架構 + 四項撤回 | §2 | ✅ T1 + T2 + T3 |
| R-TM76 | 分析層裁定，架構限定之 Pre-Condition | §3 | ✅ T1 + T3 + T4 |
| R-TM77 | 分析層裁定，T–Z 留空 | §4 | ✅ T1 |

分析層本包未動 git、未改任何腳本、未改任何 TC。
