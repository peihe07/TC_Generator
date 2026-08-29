# 上繳包 33 —— T51 執行結果（下放包 38）

- 日期：2026-08-29｜方向：執行層 → 分析層
- 對應下放包：`38_batch2a_pending.md`
- **U=21 如預期；batch 2a 無一列可交付**
- **T51c 之回溯檢定：batch 1 十列中 3 列同病，且其例外之強度高於 batch 2a** —— §3

---

## 1. T51e —— 抄錄與索引

| 條文 | 逐字相符 |
|---|:--:|
| `R-SU43（判定核心不得斷言一個規格允許其為他值之結果）` | **True** |

現行 **42 → 43** ✅；留存 25 不動。PLAYBOOK 追加
**(45)** 拼接二個射程互補之物件是綜合不是引用、**(46)** 涵蓋全部合規結果之斷言等於沒有斷言。

---

## 2. T51a —— 六列改判之產出與 lint

### 2.1 改判

| 位置 | 前 | **後** |
|---|---|---|
| Procedure 末步 | `Check that Version_after equals Version_initial …` | **`PENDING: DR-SU4 step to check the observable state showing that the head unit continues operation after the interruption`** |
| ER 末行 | `Version_after equals Version_initial …` | **`PENDING: DR-SU4 observable state showing that the head unit continues operation after the interruption`** |
| 版本讀取／記錄 | （原併於末步） | **保留為倒數第二步／第二行**（R-SU43(f)：降為記錄，值仍為證據） |

### 2.2 lint 全輸出（逐字）

```
python3 scripts/lint036.py <batch02a 之簿> --profile sw_update
  行計 A=0  B=0  C=0  D=0  E=0  F=0  G=0  H=0  I=0  I-sibling=0  J=0
       K=0  L=0  M=0  N=0  P=0  Q=0  R=0  T=0  U=21  V=0  I-cross=7   exit 0
```

| TC | `PENDING` |
|---|---:|
| `011` | 5 |
| `012`／`013`／`015`／`016` | 各 2 |
| `014` | 5 |
| `017` | 3 |
| **合計** | **21** ✅ |

其餘 20 項全 0。**本批無一列可交付。**

### 2.3 ⚠ §3.4 暫態之揭露 —— **lint 完全抓不到，遮蔽測試抓得到**

六列（連同 `017` 共七列）之 Final Step 正規化後**逐字相同**。

| 檢查 | 值 | **是否抓到** |
|---|---:|---|
| `I-sibling` | **0** | ❌ 分組鍵含 `req_id`，七列七個不同 req_id ——**結構上永不觸發** |
| `I-cross` | 7 | ❌ **全為「窗未完整宣告」** —— 本批無 `until` 片語，窗抽不出來，**七列一組配對都沒進比對** |
| **`mask_test.py`（T49b）** | — | ✅ **「僅差 `PENDING` 佔位」21 組**（七列兩兩，`C(7,2)=21`） |

**二個機器檢查都是 0，而問題真實存在。** 唯一抓到的是人工複核用的遮蔽測試腳本
—— 其正是 R-SU41(e)（本條無機器覆蓋）之具體代價。

**恢復條件**（依下放包 38 §3.4，逐包揭露）：
各列之 (a2) 觸發側狀態**仍留於 ER 第 3 行**，
**DR-SU4 一經回覆，六列之 Final Step 須即依 R-SU41(c) 重建其區分並重跑遮蔽測試。**

> ⚠ **執行層另記一項下放包未指出者**：§3.4 只稱「違 R-SU41(b)」，
> 而觸發側狀態退回 ER 前段**正是 R-SU41(a) 所禁之形態**。
> **T49a 那一輪把區分搬進判定對象之工作，被本輪整個回退。**
> 此為改判之必然後果，非錯誤 —— **但暫態之範圍應記為 R-SU41 全條，不只 (b)。**

---

## 3. T51c —— R-SU43(b) 回溯檢定（**本輪核心**）

產出 `R_SU43_AUDIT.md`。17 列逐一回查「該值於本 TC 所設之情境下，規格是否允許其為別的」。

| 判定 | 列數 | TC |
|---|---:|---|
| ✅ **通過** | **6** | `004`／`005`／`006`／`007`／`009`／`010` |
| ⚠ **待裁** | **3** | **`001`／`002`／`003`** |
| 已掛 `PENDING` | 8 | `008`／`011`–`017` |

### 3.1 ⚠ **batch 1 三列同病，且其例外來自 `shall`，強度高於 batch 2a**

**batch 2a 之他值來自 `RECOMMENDED`（SHOULD 級）；本三列之他值來自 `SHALL`。**

**`001`（`175`）**：其判定核心斷言 `contains no SW Update prompt and no progress
notification`，而 `4907477` 逐字：

> During silent sessions the user **SHALL NOT be notified unless necessary for
> safety requirements**.

**一個於靜默更新中因安全需要而顯示通知之系統是合規的，而 `001` 會判它 fail。**

**`002`（`176` facet A）**：其判定核心含 **`at any point of the session`** ——
**實測：037 `SWE1-FOTA-176` 全文查無 `at any point`**，該三字為分析層所加之強化語。
**它把一個有例外的規則寫成了無例外的規則**，而例外就在同一個 037 列的第二句。

**`003`（`176` facet B）**：其病方向相反 —— facet B 之情態為 **`allow`（許可）**，
而 ER 斷言「通知**被顯示**」，**即把一個許可讀成了一個義務**。
一個在安全條件成立時選擇不通知之系統並未違反 `allow`。

> 本列已因 DR-SU1 掛 `PENDING`，**但其病與 DR-SU1 無關** ——
> 縱使安全條件清單到手，`allow` 仍非 `shall`。
> **DR-SU1 落地時須一併處理**，否則會寫出一個驗證義務而規格只給許可之 TC。

### 3.2 ⚠ **一項對 R-SU43(b) 之範圍發現：只查錨物件會漏**

`002` 之錨為 `4907476`：

> Silent updates shall not display progress notifications and shall NOT require
> end-user interaction.

**該句不帶例外子句 —— 只查它，`002` 會通過。**
例外在**相鄰物件** `4907477` 裡，而 `4907476` 與 `4907477` 是 CFTS 中相鄰的兩句。

**故 R-SU43(b) 之回查範圍不得限於該 TC 之錨物件**，須及於：
**同一 037 列之全部 facet**、**同組之兄弟列**、**錨物件於 CFTS 中之相鄰物件**。

> **這與 R-SU16（兄弟區塊錨定）之結構相同** ——
> **例外與其規則往往是相鄰之二個物件，而錨定只取其一。**
> 建議 R-SU43(b) 補明此範圍。

### 3.3 通過六列之理由不同，值得分辨

- `004`／`006`／`007`：規格之**否定式本身不帶例外子句**
- `005`：`will display` —— **直述其行為**，無條件無例外
- `009`／`010`：「無互動」為該需求之**定義本身**，非附加之斷言

---

## 4. T51b —— `remains operable` 族之重掃（陳報，不裁定）

| 句 | 改判後 ER 中之存留 |
|---|---|
| `the head unit remains operable and its screen responds to user input` | **0 處** —— 隨判定核心之替換而全部移除 |
| `its screen responds to user input` | **2 處，皆非判定行** |

存留之二處：

| TC | 行 | 全文 |
|---|---|---|
| `015` | ER-4（transition） | `The head unit completes start-up and its screen responds to user input` |
| `016` | ER-4（transition） | `The host system connector is reconnected and the head unit screen responds to user input` |

**分類（陳報）**：二行皆為 **transition 之 ER**，非 Final Step。其前半各為
(a) 物理必然（`completes start-up`）與 (a2) 測試者操作之反映（`connector is reconnected`），
**後半 `screen responds to user input` 仍為 (b) 無來源**。

**處置（不裁定，三選項）**：
- **(甲)** 維持 —— 其非判定對象，R-SU42 之射程是否及於 transition 之 ER 未經裁定；
- **(乙)** 刪除後半 —— 惟 `016` 之 ER-4 若只剩「連接器已接回」，
  則**無任何指標顯示 HU 已回到可測狀態**，第 5 步之讀版本可能讀到開機中之值；
- **(丙)** 併入 DR-SU4 —— 其與六列尾句所求為同一件事（HU 之可操作性）。

**執行層傾向 (丙)** —— 二者本是同一個未知，分開處置會使 DR 回覆後仍留一處。

> ⚠ **一項自陳**：本輪執行 T51a 時，執行層一度逕自刪除 `015` ER-4 之該後半，
> **並回改其 procedure 第 4 步** —— 而該二處措辭為下放包 36 §3.3 所明定，
> **T51 未令更動**。**已於同輪內撤回，恢復原措辭**，本節改以陳報處理。
> 記此以存跡證（T32b：執行層不改寫分析層所定之 TC 內容）。

---

## 5. T51d —— DR-SU4 之開立

`DATA_REQUESTS.md` 新增 DR-SU4（High，阻斷六列），
並於第四型段加註 **`315`／`318` 同時掛 DR-SU2(d) 與 DR-SU4，二者不互相取代**
（前者求觸發手段、後者求判定準據，**一者到手而另一者未到，該二列仍不可交付**）
—— 此為下放包 38 未令而執行層認為必要之調和，見 §7-2。

DR 文本增 **§3B**，含三節：

- **3B.1** `OTA client continues operation` 於 HU 上之可觀測表徵
  —— 併列 `4907673` 與 `4907440` 之原文與其射程差，明寫
  **"The two requirements each cover one half and their scopes do not overlap.
  We are not willing to combine them into a statement neither document makes."**
- **3B.2** 階段不可判定下之判準 —— 附 Table 4-6 之三列與其版本後果
- **3B.3** 我方之處置 —— 明寫
  **"We would rather hand you six visibly blocked test cases than six that quietly
  pass the wrong thing."**

**發送者為 Pei，未發送。**

---

## 6. 獨立自評 —— §六-6：R-SU43(a) 是否會使幾乎所有肯定式判定核心失格

**答：不會。而本輪 17 列之實測給出了分界所在。**

**(甲) 先給數據。** 17 列中通過 6、待裁 3、已掛起 8。
**待裁之 3 列，無一是因為「規格沒說不可以」而失格** ——
`001`／`002` 之例外由 **`SHALL NOT … unless`** 給出，
`003` 之問題是把 **`allow`** 讀成 `shall`。
**三者皆為「規格明文允許他值」，不是「規格未排除他值」。**

**(乙) 分界在此：R-SU43(a) 之「允許」須為明文，不含默許。**

該題之顧慮成立於一種讀法 ——「規格只寫『應如何』未寫『不得如何』，
故任何他值都『未被排除』，故任何斷言都失格」。
**該讀法會使本條吞掉一切，但它不是本條之讀法。**

理由在 (b) 之檢定問句本身：**「該值是否**可以**是別的？」**
—— `可以` 問的是**規格之許可**，不是**規格之沉默**。
規格沉默處，其許可未被給出，**故不構成他值**。

**(丙) 三種形態之分辨（本輪實測皆有實例）**：

| 形態 | 例 | 失格？ |
|---|---|---|
| 規格**明文允許**他值 | `4907477` 之 `unless necessary for safety` | **是** |
| 規格**建議**他值（SHOULD／RECOMMENDED） | `4907673` Table 4-6 之 `Complete the deployment` | **是** —— 依建議實作者仍合規 |
| 規格**沉默**（未提及他值） | `4907485` `will display …` 未說「或不顯示」 | **否** |

**第三列即該題所慮者，而它不失格。**

**(丁) 惟須補一個 (a) 未載之限制，否則第三形態會被誤判。**

`005`（`4907485` `will display a success notification`）之所以通過，
**不只因為規格沉默，還因為該句是直述式且無條件** ——
若其寫成 `the OTA client will display … **if configured to do so**`，
則「未配置」即為一個明文允許之他值，`005` 隨即失格。

**故分界之精確表述為**：
**「規格對本 TC 所設之情境，有無給出一個使該值為他值之明文許可、建議或條件？」**
—— 三者任一為是即失格；三者皆否則通過。**沉默不算。**

建議以此收窄 R-SU43(a) 之措辭。

**(戊) 一項附帶之量化**：本輪 6 列通過中，
**3 列（`004`／`006`／`007`）之通過依賴「其否定式不帶例外子句」** ——
而 `002` 之失格正是因為**它的例外不在它的錨物件裡，在鄰居裡**（§3.2）。
**故「通過」之可靠度取決於回查範圍**，而本輪之回查範圍已擴至相鄰物件與兄弟 facet。
**若範圍再擴（如 SYSAD、VF747），現行之 6 列通過仍可能減少。**
**本檢定之結果為上界，不是定論。**

---

## 7. 待裁事項

| # | 事項 | § |
|---:|---|---|
| 1 | **`001`／`002`／`003` 三列之處置** —— 其例外來自 `SHALL`，強度高於 batch 2a | §3.1 |
| 2 | `315`／`318` 之雙 DR 並存記法（執行層已逕行調和，請追認） | §5 |
| 3 | **R-SU43(b) 之回查範圍是否補明**（錨物件 → ＋兄弟 facet ＋相鄰物件） | §3.2 |
| 4 | **R-SU43(a) 之措辭是否依 §6(丁) 收窄**（明文許可／建議／條件；沉默不算） | §6 |
| 5 | `015`／`016` ER-4 之 `screen responds to user input` —— **執行層傾向併入 DR-SU4** | §4 |
| 6 | 暫態之範圍應記為 R-SU41 全條而非只 (b) | §2.3 |
