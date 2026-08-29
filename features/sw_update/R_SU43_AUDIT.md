# R-SU43 回溯檢定 —— 17 個 TC 之判定核心

**T51c**（下放包 38 §五）。**R-SU43(b) 之檢定**：對判定核心所斷言之值，回查規格
**「在本 TC 所設之情境下，該值是否可以是別的？」答是 → 該斷言不得作為判定核心。**

**檢定須以最寬之情境**（R-SU43(c)）—— TC 之 Procedure 未釘死之條件，
其情境即涵蓋規格所允許之全部取值。

> **本表為執行層之檢定與陳報，不是裁定。** 每列列出其判定核心、
> 規格是否允許他值、其依據（CFTS ObjectID 或 037 列），以及**待裁與否**。

---

## 一、結論摘要

| 判定 | 列數 | TC |
|---|---:|---|
| **✅ 通過** —— 規格於該情境下不允許他值 | **6** | `004`／`005`／`006`／`007`／`009`／`010` |
| **⚠ 待裁** —— 規格允許他值，現行斷言可能誤判合規系統 | **3** | **`001`／`002`／`003`** |
| **已掛 `PENDING`**（本輪或前輪） | **8** | `008`／`011`–`017` |

**batch 1 十列中有 3 列同病** —— 與 batch 2a 六列之成因**同型但來源不同**：
batch 2a 之他值來自 `4907673` Table 4-6；**batch 1 之他值來自 037 自身之兄弟列。**

---

## 二、⚠ 待裁三列 —— 其例外由**同一需求之另一 facet** 給出

### 2.1 `newR1L-SU-001`（`175`）

**判定核心**：`the recorded screen content contains no SW Update prompt and no progress notification`

**規格是否允許他值？** —— **是。**

**037 `SWE1-FOTA-176` 第二句**（facet B，`newR1L-SU-003` 之來源）逐字：

> During a Silent Update session, the WiFi Update Service shall **allow user
> notification only when required to satisfy safety-related requirements**.

**而其 CFTS 錨 `4907477` 之原文更明白** —— 例外直接寫在同一句裡：

> During silent sessions the user **SHALL NOT be notified unless necessary for
> safety requirements**.

即：**靜默期間，安全相關之通知是被允許的。**
而 `001` 之錄影窗涵蓋整段更新，其斷言為「**無**任何 SW Update prompt」。

**一個於靜默更新中因安全需要而顯示通知之系統，是合規的，
而 `newR1L-SU-001` 會判它 fail。**

> **與 batch 2a 之差別**：後者之他值來自 `RECOMMENDED`（SHOULD 級），
> **本例之他值來自 `shall`** —— 其強度更高，**病更重**。

### 2.2 `newR1L-SU-002`（`176` facet A）

**判定核心**：`The recorded screen content contains no update progress notification
**at any point** of the session`

**規格是否允許他值？** —— **是，且本例最明顯。**

`002` 與 `003` **出自同一個 037 列**（`SWE1-FOTA-176`）之二個 facet：
- facet A（`4907476`）：靜默期間不觸發進度通知
- facet B（`4907477`）：**安全需要時允許通知**

**`at any point` 這三個字，與同列 facet B 直接抵觸。**

**實測**：037 `SWE1-FOTA-176` 全文中**查無 `at any point`** ——
其為分析層所加之強化語。**該強化把一個有例外的規則寫成了無例外的規則。**

**且 `002` 之錨 `4907476` 本身不帶例外子句**：

> Silent updates shall not display progress notifications and shall NOT require
> end-user interaction.

**故只查錨物件，`002` 會通過** —— 例外在**鄰居** `4907477` 裡。

### 2.3 `newR1L-SU-003`（`176` facet B）

**判定核心**：`The safety-related notification is displayed on the head unit and the
session continues`

**規格是否允許他值？** —— **是，但方向相反。**

facet B 之情態為 **`allow`（許可）**，不是 `shall display`（要求）。
**一個在安全條件成立時「選擇不通知」之系統，並未違反 `allow`。**

現行 ER 斷言「通知**被顯示**」，**即把一個許可讀成了一個義務**。

> 本列已因 DR-SU1 掛三個 `PENDING`（安全條件清單未知），
> **但其病與 DR-SU1 無關** —— 縱使清單到手，`allow` 仍非 `shall`。
> **DR-SU1 落地時須一併處理，否則會寫出一個驗證義務而規格只給許可之 TC。**

---

## 三、✅ 通過六列 —— 其通過之理由各不相同，值得分辨

| TC | 判定核心 | 為何規格不允許他值 |
|---|---|---|
| `004`（`177`） | `contains no opt-out control and no defer control` | `4907478`：`If an HMI is available, the user SHALL NOT be presented with a choice of opting out or deferring` —— **條件式全稱否定，其條件（HMI available）已入 pre_conditions，且無例外子句** |
| `005`（`183`） | `displays the update success notification and the What's New details` | `4907485`：`When the update completes, the OTA client **will display** a success notification and what's new details` ——**直述其行為**，無條件、無例外 |
| `006`（`180`） | `contains no download confirmation screen` | 037 為 `shalll not trigger`；CFTS `4907482` 為 `MAY NOT display` ——**二者皆不允許顯示**（強度差已記於 reasoning） |
| `007`（`182`） | `contains no deployment confirmation screen` | 同上（`4907484`） |
| `009`（`179`） | `No user interaction occurs before the download request is issued` | `4907481` 為 `automatically request … without user interaction`，**「無互動」即其定義** |
| `010`（`181`） | `no user input occurred between download completion and installation` | `4907483` 為 `deployment shall start immediately` ——**其間無互動為其蘊含** |

> **一項須明記之分辨**：`004`／`006`／`007` 之通過，其依據為
> **規格之否定式本身不帶例外子句**。
> **而 `001`／`002` 之否定式，其例外寫在同一需求之另一 facet 裡** ——
> **即例外不在該句之內，在該句之旁。**
>
> **故 R-SU43(b) 之回查範圍不得限於該 TC 之錨物件** ——
> 須及於**同一 037 列之全部 facet**、**同組之兄弟列**、
> 以及**錨物件於 CFTS 中之相鄰物件**（`4907476` 與 `4907477` 為相鄰二句）。
>
> **只查錨物件，`001`／`002` 會通過。**
> 這與 R-SU16（兄弟區塊）之結構相同 —— **例外與其規則往往是相鄰之二個物件**，
> 而錨定只取其一。

---

## 四、已掛 `PENDING` 八列（不入本次檢定）

| TC | 成因 |
|---|---|
| `008`（`184`） | R-SU32(iii) 不可區辨（下放包 30 §2.2） |
| `011`–`016` | **本輪 R-SU43 改判**，判定核心改掛 `PENDING: DR-SU4` |
| `017`（`313`） | R-SU37 v2(b) 餘量為空，DR-SU3 |

> **其判定核心一經 DR 回覆而重建，須即重跑本檢定**（R-SU43(b) 為撰寫前之檢定，
> 而重建即為一次新的撰寫）。

---

## 五、對 §六-6 自評題之材料

下放包 38 §六-6 問：R-SU43(a) 嚴格套用之下，
是否幾乎所有肯定式判定核心都會因「規格未排除其他結果」而失格？

**本檢定之實測數據**：17 列中，**通過 6、待裁 3、已掛起 8**。
**待裁之 3 列，其失格皆非因「規格未排除」，而是因「規格明文允許」。**

- `001`／`002`：例外由 **`shall allow`** 給出（`4907477`）
- `003`：**`allow` 被讀成 `shall`**

**無一列是因為「規格沒說不可以」而失格。** 詳見上繳包 33 §6 之作答。
