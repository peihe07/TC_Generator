# 上繳包 18 —— Vehicle Category：第 2 批 32 筆收斂（T99–T104）

- 日期：2026-08-26
- 對應下放：`docs/handoff/18_batch2_tc.md`
  （SHA256 `8aa22a27c288a16060db8315560fbef10e0831654f88f96a12333610c74b57f9`，226 行）
- **結論：T99–T104 六項全數完成。第 2 批 32 筆，收斂 19 項全過。**
- 未寫回工作簿、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T99 | 子串判準只跑不判 | ✅ **34/34 通過** → 依 §2.3 第 2 步改採 |
| T100 | PLAYBOOK §7.2 修訂 ＋ §7.1(b) 增句 | ✅ 原措辭不刪 |
| T101 | A-VC10 加註三面 | ✅ 未立新 A |
| T102 | 第 15 項 `split_delta` | ✅ 雙向實測 |
| T103 | 生成 32 筆 | ✅ |
| T104 | 收斂 19 項 | ✅ **19 checked / 0 failed** |

---

## 1. T99 —— 34/34 通過（本輪最重要之回報）

`scripts/t99_substring_probe.py`，**只跑不判**，未改任何 TC 與判準。

判準：上半（去首尾空白、首字母大小寫正規化）
∈ substring( 037 `Title` ∪ 037 `Description` ∪ SYS1 對應節全文 )。

### 1.1 逐筆結果

| 批 | leaf | 命中來源 |
|---|---|---|
| pilot | `026-01`／`026-02`／`026-03`／`027`／`028-02`／`029`／`031`／`033-01` | **037 Title**（8 筆）|
| pilot | `028-01`／`030`／`032`／`033-02` | **037 Description**（4 筆）|
| 第 1 批 | `001-01`~`001-03`／`002`~`006`／`007-02`~`-05`／`008`~`011`／`012-01`／`013-01` | **037 Description**（18 筆）|
| 第 1 批 | `012-02`／`012-03`／`013-02`／`013-03` | **SYS1 §2.6.2／§2.6.3**（4 筆）|

**34 筆 / 不通過 0 筆。**

### 1.2 §2.3 第 3 種情形未發生

下放包預留了「不通過」之二種可能（真陽性須修 TC／判準過嚴須修判準），
並明文其處置相反、須看實例才能裁。**本輪不需要那個裁定。**

### 1.3 依 §2.3 第 2 步：第 7b 項改採子串判準

token 比對已移除（非降為輔助 —— 子串判準嚴格覆蓋它）。
三項優於前版：**不需樣式表**（任何記法自動受驗，
`「…」`／`｢…｣`／任何未來記法皆然）、**token 對得上而其間文字被竄改者
亦抓得到**、零閾值無語意判斷。

**一項附帶效益**：新實作之輸出**報出取材來源分布** ——
第 2 批為 `{'Description': 30}`、pilot 為 `{'Title': 8, 'Description': 4}`。
**這正是 §3.2 要求記於 `reasoning` 之「取自哪一欄」**，
現在由機器直接算出，不再只靠人寫。

---

## 2. T100 —— PLAYBOOK 二處

**§7.2 修訂**：範圍由「複核腳本之掃描標的」擴為
「**任何判讀之輸入**，不論由腳本或由人為之」，
適用範圍明列「**以及據以下裁**」。原措辭保留並註明範圍已擴充，
另補記第二次之形態（`d[:230]` 後下裁，非腳本判準錯）。

**§7.1(b) 增句**：已知標的**優先取單筆或極小之探針**，
並記其由來 —— 第九件（`TCS[10]`）之所以被抓到是因為用了單筆探針，
而**第 6 批（2 leaf）與第 7 批（1 leaf）正是那樣的批次**。

---

## 3. T101 —— A-VC10 三面

原文不改，加註三面表：資訊量不對稱（本條）／數值矛盾（A-VC14）／
記法不對稱（下放包 18 §3.2）。**未立新 A** —— 三面同源，分立會使追蹤點散開。

---

## 4. T102 —— 第 15 項 `split_delta`

判準：`len(tcs) == len(leaf_scope) + split_delta`，
**且 `split_delta` 須與實際拆分相符** —— 「實際拆分」自 `tcs` 直接數得
（同一 `leaf_id` 出現多筆之超額數），**不採信 JSON 之宣告值**。

### 4.1 雙向實測

**(a) 令 `split_delta = 0` 而實有拆分 → FAIL**

```
  1  30 筆 JSON 完整…                                    **FAIL**   TC 數 32
 15  母體 = leaf_scope + split_delta = 30 + 0 = 30       **FAIL**
     tcs=32；宣告 split_delta=0；實際拆分增量=2
     （{'SWE1-HMI-VC-046-05': 2, 'SWE1-HMI-VC-048-02': 2}）
exit: 1
```

第 1 項與第 15 項**同時 FAIL** —— 因 `EXPECT_N` 由 `split_delta` 推得。
二者互為佐證。

**(b) 真實值 → PASS**（見 §6）。

**(c) 回歸**：pilot 與第 1 批之 `split_delta` 缺省為 0，二批仍 19/0。

---

## 5. T103 —— 第 2 批 32 筆

`generated/batch2_settings_list.json`。30 leaf → 32 TC，
`split_delta: 2`，`held_leaves: []`（**無 b 段**），無 `PENDING`。

### 5.1 二筆拆分之落實

| leaf | 二筆之括號下半 |
|---|---|
| `VC-046-05` | `(Knob rotation and arrow presses as cursor movement -- no selection made)` ／ `(Knob press as selection -- the action that follows the movement)` |
| `VC-048-02` | `(The positive rule -- a setting outside the exception list)` ／ `(The negative pairing -- the three listed exception settings)` |

二筆之 `Requirement or Design ID` 與 `specification_reference` **相同**
（機器已驗：第 4 項 32/32 逐字相符），**其區分僅在括號下半** ——
故第 3 項（32 筆兩兩不同）於本批**尤其吃重**，已 PASS。

`split_note` 逐字記入 IN §8.2.2 之工作簿處置。

### 5.2 本批特有拘束之落實

| 拘束 | 落實 |
|---|---|
| 記法 | 32 筆之上半**全部取自 `Description`**（第 7b 項之來源分布已證），二欄不混用 |
| `051-03` | `Description` 之**彎單引號** `‘Setting not saved, please try again’` 於上半與 ER 皆逐字保留；`reasoning` 載明二欄記法不對稱及取材決定 |
| `043` | 上半含**方括號** `[Example: Language (English) >]`，`reasoning` 載明 IN §11 之禁令於 verbatim 上半讓位（R-VC23 末段）|
| `049`／`050` | 括號下半以**適用對象**區分（五類 vs Brightness），非以速率 |
| `HMI Settings List` | `040`／`041`／`044` 之 `reasoning` 載明該素材確載其所需內容、不需 PENDING |
| `055` | ER 為「**仍可用**」（`responds`／`opens and is available`），**未寫成禁用或灰化** |
| 常數 | 32 筆首步皆為 `ENTER_VC_TAB(Settings)`（第 14 項已驗）|

### 5.3 一處我另行處理者

`VC-050` 之門檻與速率**同為 500 ms** 但意義不同（前者為觸發門檻、
後者為重複間隔）。步驟已分別表述以免混讀，`reasoning` 載明。
**下放包未點名此點**，是生成時發現的。

---

## 6. T104 —— 收斂 19 項全過

```
  1  32 筆 JSON 完整，10 個必要 key 齊備                    PASS  TC 數 32
 11  pre_conditions 無 §4.4 三類禁項                       PASS  default 0；premise 0；step_overlap 0
 12  無對他筆之值的隱性依賴                                  PASS  命中 0 處
  3  test_item 括號下半 32 筆兩兩不同                        PASS  相異 32
 3b  括號下半無中文                                        PASS
  4  specification_reference 32 筆逐字相符                 PASS  不符 0
  5  priority 32 筆逐字相符                                PASS  不符 0
  6  Test Set 32 筆一致                                    PASS  ['Settings List']
  7  尾句號／方括號／單引號／行首尾空白                          PASS  皆 0
 7b  上半為來源之逐字子串                                    PASS  取材來源分布 {'Description': 30}；未對上 0
  8／9／10  pilot 專屬                                     PASS  N/A
  A  ≥2 步 ∧ 1:1 ∧ ER 無 modal ∧ 無禁用起首動詞               PASS
 13  Test Set 與 framework §2 逐字相符                     PASS
 14  常數之變體擴散                                         PASS  常數 3 條；變體 0
 15  母體 = 30 + 2 = 32                                   PASS  宣告 2 ＝ 實際 2
 16  續行型 leaf（本批無適用對象）                             PASS  N/A
19 checked / 0 failed
```

> 第 7b 項報 `{'Description': 30}` 而本批有 32 筆 ——
> **差額 2 為拆分之第二筆**，其 `leaf_id` 與第一筆相同故 key 覆寫。
> 該計數為**依 leaf 計之來源分布**，非依 TC 計。已於揭露節記明。

---

## 7. 未結清單

**DR 九筆全未結**。同批 A 六項；DR-VC9(一) 獨立發。
**A 十二筆未結**。已結五筆。

**進度**：117 leaf 中 **64 筆已收斂**（pilot 12 ＋ 第 1 批 22 ＋ 第 2 批 30），
b 段保留 2 筆，**剩 51 筆分五批**。TC 累計 **66 筆**。

---

## 8. 待你裁

1. **第 3 批 `Controls`（17 leaf）之勘查前置** —— R-VC21 末句。
   其含 `VC-021`（DR-VC1 阻斷）與 `VC-025-01`（A-VC17 之第三筆，
   純交叉引用，疑為表格題名）—— **後者之地位待 DR-VC9(二)，
   可能又是一個 b 段**。
2. 同批 A（六項）、DR-VC3、DR-VC9(一) 之發送（Tier 3）。

---

## 9. 量測條件揭露（R-G8）

### 第 7b 項之子串判準

- **偽陰性**：上半若為**跨來源之拼接**（前半取 Title、後半取 Description），
  任一單獨來源皆不含之，會 FAIL —— 此為**安全側**。
  但若某來源字串本身極短（如 `Vehicle Tab Labels and Order.`），
  任何更短之上半皆為其子串，**其保護力隨來源長度遞減**。
- **首字母正規化**僅試三形（原樣／首字大寫／首字小寫）。
  R-4 只許句首字母轉大寫，故三形已足；**若日後另有正規化被允許
  （如去除條號前綴 `VC2.)`），本判準會誤報**。
- **來源分布之計數依 leaf 計，非依 TC 計**（見 §6 之註）。
  拆分之二筆共用一個 leaf_id，故 32 筆之分布顯示 30。

### 第 15 項

- 「實際拆分增量」自 `tcs` 之 `leaf_id` 計數推得，**不採信 JSON 之宣告值** ——
  故宣告值錯會被抓到（(a) 已實測）。
- **偽陰性**：若某 leaf 被拆為二筆而其**二筆之 `leaf_id` 被寫錯成不同值**，
  本項會把它算成二個 leaf 而非一次拆分 —— 但那會被第 4 項
  （`specification_reference` 對照）抓到，因錯誤之 leaf_id 查不到對應。

### T99

- 母體為既有 34 筆，**未含第 2 批**（其當時尚未生成）。
  第 2 批之 32 筆由第 7b 項於本輪驗過，二者判準相同。
