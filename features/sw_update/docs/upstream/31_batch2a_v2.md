# 上繳包 31 —— T49 執行結果（下放包 35 + 36）

- 日期：2026-08-29｜方向：執行層 → 分析層
- 對應下放包：`35_batch2a_er_fix.md`（二項 FAIL）+ `36_batch2a_final.md`（其處置）
- **下放包 36 之落檔驗證：算術全對；一項須確認已於本輪查得新證據**（§5）
- **T49c 之回溯掃描查出 6 句無來源之 ER 斷言 —— 本輪核心**

---

## 1. T49e —— 抄錄與索引

| 條文 | 來源 | 逐字相符 |
|---|---|:--:|
| `R-SU41（sibling 之區分須位於判定對象之內）` | 35 §二（**T48 未執行，本輪補**） | **True** |
| `R-SU42（ER 之斷言 —— 物理必然之後果 vs 系統設計之選擇）` | 36 §二 | **True** |

| 項 | 預期 | 實測 | |
|---|---:|---:|:--:|
| 現行 | **42** | **42** | ✅ |
| 留存 | 24（無取代） | **24** | ✅ |

`R-SU1` – `R-SU42` 無缺號無重複。PLAYBOOK 追加四則：
**(39)** 區分須在判定對象內、**(40)** API 決定看得見什麼、
**(41)** 退化值污染分母、**(42)** 佔位不必搬進判定對象。

---

## 2. T49a —— 六 TC 定稿改寫與 lint

依下放包 35 §三 + 36 §三（**本包措辭優先**）。共用之 `TAIL`／`ER_TAIL`
**已拆除** —— 各 TC 之 Final Step 現各自帶入其觸發側狀態（R-SU41(c)）。

### 2.1 六列之 Final Step（改寫後，判定對象兩兩相異）

| TC | 037 | Final Step 之判定對象（節錄） |
|---|---|---|
| `011` | `315` | `…after the socket read/write error has been injected` |
| `012` | `316` | `…while the head unit settings still show Wi-Fi as enabled with no connection present` |
| `013` | `317` | `…while the head unit settings show Wi-Fi as disabled` |
| `014` | `318` | `…while the vehicle is in the emergency state` |
| `015` | `319` | `…after the head unit has powered off and started up again` |
| `016` | `320` | `…after the host system connection has been lost and restored` |

`015` 之 ER 第 4 行依 36 §3.3 改為 `completes start-up and its screen responds to
user input`（刪 `home screen`）；`016` 之第 4 行依 35 §3.6 改為
`The host system connector is reconnected and the head unit screen responds to user
input`（不宣稱開機）。`017` 不動。

### 2.2 lint 全輸出（逐字）

```
python3 scripts/lint036.py <batch02a 之簿> --profile sw_update
  行計 A=0  B=0  C=0  D=0  E=0  F=0  G=0  H=0  I=0  I-sibling=0  J=0
       K=0  L=0  M=0  N=0  P=0  Q=0  R=0  T=0  U=9  V=0  I-cross=7   exit 0
```

| 項 | 預期 | 實測 | |
|---|---:|---:|:--:|
| U | **9** | **9** | ✅ |
| 其餘 20 項 | 0 | **全 0** | ✅ |

`I-cross=7` 仍全為「窗未完整宣告」（本批無 `until` 片語），**零組配對**，
覆蓋狀況與上輪相同 —— 逐包揭露。

---

## 3. T49b —— Final Step 遮蔽測試（R-SU41(b)）

`scripts/mask_test.py`，17 個 TC、136 組配對，比對 ER 之末行
（`PENDING` 正規化為 `<PENDING>` 後再比）。

| 類 | 組數 |
|---|---:|
| Final Step **逐字相同** | **0** |
| **僅差 `PENDING` 佔位** | **0** |

**17 個 Final Step 兩兩字面相異。**

> ⚠ **本結果為下界，不是通過證明**（R-SU41(e)：本條無機器覆蓋）。
> 本檔只抓**逐字相同或僅差佔位**者 —— **字面有別而語意相同者抓不到**。
> 例：`015` 與 `016` 之差異僅在末尾之情境子句
> （`powered off and started up again` vs `host system connection has been lost and
> restored`），**字面相異故不入表**，其實質是否足夠見 §5。

---

## 4. T49c —— R-SU42 回溯掃描（**本輪核心**）

產出 `ER_ASSERTIONS.md`。範圍：**17 TC／75 行 ER／38 句相異**
（以相異句為單位，同句出現於多 TC 者分類與來源相同）。

| 類 | 相異句 | 行次 |
|---|---:|---:|
| **(a) 物理必然** | 1 | 1 |
| **(b) 有來源** | 17 | 47 |
| **⚠ (b) 無來源** | **6** | **12** |
| (c) 不適用（記錄確認） | 7 | 8 |
| (c) `PENDING` 佔位（暫不分類） | 7 | 7 |

### 4.1 (a) 僅一句 —— 且其分界正是 R-SU42 之射程

**`The head unit powers off`**（`015`）—— 切斷電源則裝置停止，
**若不停止即意味硬體故障**。

依 **R-SU42 拘束 1**，其 (a) 資格**限於「停止」這個後果本身**：
若寫成「於 2 秒內停止」或「停止時顯示關機動畫」，細節即為 (b)。
本句未帶細節，故成立。**全 75 行中僅此一句夠得上 (a)。**

### 4.2 ⚠ 六句無來源 —— 實測 CFTS 全語料

`operable`／`responds to user input`／`home screen` 於 CFTS_57 全語料**命中 0**。

| # | 句 | TC 數 |
|---:|---|---:|
| 1 | `the head unit remains operable and its screen responds to user input` | **6**（`011`–`016`） |
| 2 | `the head unit shows no Wi-Fi connection` | 1（`012`） |
| 3 | `the head unit settings still show Wi-Fi as enabled with no connection present` | 1（`012`） |
| 4 | `the head unit settings show Wi-Fi as disabled` | 1（`013`） |
| 5 | `The head unit loses the host system connection` | 1（`016`） |
| 6 | `its screen responds to user input`（`015`／`016` 第 4 行後半） | 2 |

### 4.3 ⚠ **一項條文交互作用 —— 二包皆未預見**

**R-SU41(c) 令把觸發側之狀態帶進 Final Step；R-SU42(b) 令此類狀態須有來源。**

上表 **#2／#3／#4 正是為履行 R-SU41(c) 而寫進去的** ——
`012` 與 `013` 之區分（`enabled with no connection` vs `disabled`）**就是這三句**。

**即：滿足 R-SU41 的動作，製造了三個 R-SU42(b) 之無來源斷言。**

**且其代價比改寫前更高**：改寫前，該區分寫在 ER 第 3 行 —— 其病為「區分不足」；
改寫後，它進了判定對象 —— 其病變為**交付物中之無來源斷言**。
**病從 R-SU41 之範疇移到了 R-SU42 之範疇，而後者較重。**

若該三句取不到來源，`012`／`013` 之區分**無處可放** ——
放第 3 行違 R-SU41、放末行違 R-SU42。**此為待裁之第一項。**

### 4.4 #1 之部分來源 —— `CFTS057-4907440`，**射程不吻合**

全語料唯一相關者：

> **`4907440`（4.7.1 OTA Client Performance Requirements）**
> `OTA client shall be a low priority process when active such that it does not
> impact normal functionality of the host system (ex, navigation/radio shall not
> be impacted).`

| | `4907440` | 六 TC 之斷言 |
|---|---|---|
| 時點 | **更新進行中**（`when active`） | **中斷發生之後** |
| 對象 | OTA client 不影響 host system 之正常功能 | HU 於中斷後仍可操作 |

**「更新中不影響正常功能」不蘊含「中斷後仍可操作」** ——
後者是**失敗路徑之強健性**，前者是**正常路徑之資源佔用**。

**執行層不逕自引用該錨**（引之即等於宣稱射程吻合）。三個處置：

- **(甲)** 引 `4907440` 並於 `reasoning` 明記射程差；
- **(乙)** 另求一條關於中斷後系統狀態之需求（`321`／`4907673` 之復原表為候選）；
- **(丙)** 刪除該尾句 —— **惟刪除後六列之 Final Step 只剩版本比對**，
  而「更新未完成」與「更新未完成且系統壞了」**在 ER 上將無從分辨**，
  中斷處理之驗證意義大幅縮小。

### 4.5 `PENDING` 佔位落地時之義務

七句佔位**暫不分類**。**其落地之時即為新的 R-SU42 判別時點** ——
上游給的觀測手段若含 UI 狀態之描述，該描述**同樣須有來源**。
**不得因其出自上游即免於分類**（上游給的是**手段**，不是**需求**）。

建議立為條文之附款，本輪列為待裁。

---

## 5. 對下放包 36 §1.3 之更新 —— **查得新證據，其性質由「無據」降為「有據而未消歧」**

上輪執行層指出：§1.3 之論證依賴「拔除主機連接器不影響 HU 自身之寫入」，
而 `320` 原文為 `the host system (HU/TBM)`。

**本輪查得**：

> **`4907340`（4.4.2 OTA Client Configuration options）**
> `In the event that the OTA client components are on **multiple host systems**
> (tethered phone for example), common communications interfaces shall be defined…`

**故「host system 可為多個，HU 為其一，另一個被拔除時 HU 為觀察者」之讀法有據** ——
**分析層之論證不是憑空。**

**惟其未消歧**：`320` 原文並列 `HU/TBM`，未指明被拔者為何者。
若被拔者即 HU，§1.3 之論證仍不成立。**待分析層確認，但已非空言。**

---

## 6. T49d —— 「無 DV」之射程更正

### ⚠ **T49d 之前提須更正：既有陳述沒有一句是錯的**

逐項覆核 `SOURCE_COLUMNS.md` 之三處「無 DV」（`C`／`E`／`S`）——
**該三欄確實不在母本任一 DV 範圍內**（DV 範圍為 `P10:Q1411`／`T10:Z1411`／
`AF10:AF1411`／`R10:R1411`）。**三處皆為欄範圍內之真陳述。**

上繳包 24 §4 更寫明 **「`C`／`E` 於母本無 DV、**無 x14 DV**、無條件式格式」**
—— **連 x14 都查了，且結論正確**。

**故本項不是更正錯誤，是補其射程** —— 已改為
「該欄無標準 DV 亦無 x14 DV」，並於檔中加一段說明全簿之事實
（標準 4 處、x14 1 處）並指向 `CONTROLLED_VOCAB.md`。

> **這件事本身值得記**：沒有人寫錯任何一句話，而結論仍然誤導 ——
> **每一句都帶著它的射程，而射程在傳遞過程中掉了。**
> 「`C`／`E` 無 DV」被記成「母本無 DV」，再被用來推論「`R` 也不受拘束」。
> 已入 PLAYBOOK (40)。

`CONTROLLED_VOCAB.md` 之 `AF` 清單原已照抄原文（含 `Fail, Pending` 與
`Pending,Block` 之空白不一致），本輪未動。

---

## 7. 未結 DR 清單（**3 筆**）

| DR | 標的 | 進度 |
|---|---|---|
| **DR-SU1** | 安全相關通知條件清單 | `003` 三個 `PENDING` |
| **DR-SU2 v3** | (a) 顯示途徑／(b) 正向狀態／(c) 區辨手段 3 列／(d) 觸發手段 2 列 | 第二型 5/106；第三型 3；第四型 2 |
| **DR-SU3** | 統攝列 `313`／`327` 之併入確認 | `017` 三個 `PENDING`；`327` 未起草 |

**`PENDING` 總計 20 行**。**§4.2 之六句無來源斷言尚未構成 DR** ——
其待裁之結果可能產生第四筆，亦可能以改寫解決。

---

## 8. 獨立自評 —— 下放包 36 §五-7：`the head unit remains operable…` 應判 (a) 或 (b)

**答：(b)。而且這一題的答案會決定六個 TC 還剩下多少驗證意義。**

**(甲) 判別問句之直接套用。**
「HU 於更新中斷後不可操作，是否意味硬體壞了？」——**否**。
中斷處理沒做好、狀態機卡住、分割區半寫而開機失敗，**皆為軟體缺陷** ——
**而那正是這六個 TC 要抓的東西**。
**故其為 (b)，須有來源。** 依 R-SU42 拘束 2（不確定歸 (b)），亦得同一結論。

**(乙) 但這一題有一個轉折，且它比答案本身更要緊。**

`remains operable` 之所以難判，不是因為它介於 (a)(b) 之間，
而是因為 **它就是這六個 TC 的驗證點本身**。

拆開六列之 Final Step：
- 前半「`Version_after equals Version_initial`」= **更新未完成**
  —— 這是**中斷之後果**，任何中斷都會產生，**不是「處理得好」的證據**；
- 後半「`remains operable`」= **系統未損毀**
  —— 這才是「偵測**並處理**該中斷條件」之處理面。

**刪掉後半，六列驗的就只剩「中斷後更新沒完成」** ——
而那件事**不需要任何需求也會發生**：拔掉電源更新當然不會完成。
**六個 TC 會退化為「驗證物理定律」。**

**(丙) 故 §4.4(丙) 之「刪除」實質上不是一個選項。**
下放包 36 §四把三個處置並列，但其代價不對等：
(甲)(乙) 是找來源，(丙) 是**放棄驗證點**。

**(丁) 我的建議：(乙) 優先，(甲) 為其退路。**

`321`（`4907673`）之「中斷解除後之 OTA client action」表
**很可能載有中斷後之系統狀態要求** —— 若有，即為本句之正解來源，
且其射程（中斷之後）與本句吻合。
**該列屬本組而本批未涵蓋**（範圍紀律，`321` 之復原不入 batch 2a），
**但讀其內容以取來源不違範圍紀律** —— 取來源與寫 TC 是兩件事。

**本輪未讀 `4907673`**（下放包未令，且其屬 `321` 之材料）。
**建議下放包 37 令其為一項任務**，其結果同時決定六列尾句之去留。

**(戊) 一項附帶之觀察**：本題揭示 R-SU42 有一個未言明之推論 ——
**一個 TC 若其 (b) 類斷言全部取不到來源，該 TC 之驗證點即為空**，
其處置應同 R-SU37(b)／R-SU34 v3(e)（無屬於自己之驗證點）。
**R-SU42 現只管單句之合法性，未管「全句皆不合法時該 TC 如何」。**
建議補其與 R-SU34 v3(e) 之接續。

---

## 9. 待裁事項

| # | 事項 | § |
|---:|---|---|
| 1 | **`012`／`013` 之區分句無來源** —— 放第 3 行違 R-SU41、放末行違 R-SU42，**無處可放** | §4.3 |
| 2 | **六列尾句之處置**（(甲) 引 `4907440` 記射程差／**(乙) 讀 `4907673` 求來源**／(丙) 刪除＝放棄驗證點） | §4.4、§8 |
| 3 | `016` 之 `loses the host system connection` —— **有據而未消歧**（`4907340`） | §5 |
| 4 | `PENDING` 落地時之回本表分類義務，是否立為 R-SU42 之附款 | §4.5 |
| 5 | **R-SU42 與 R-SU34 v3(e) 之接續** —— 全句皆無來源時該 TC 如何 | §8(戊) |
