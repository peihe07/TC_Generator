# RD-1 之全稱否定複核 —— 留檔（2026-08-17）

本檔為 `docs/RD1_questions_comfort.md` **送出時之依據記錄**（下放包 89 §1.3
／90 §4.3）。RD-1 將交需求方，其中每一句「某某東西不存在」都是對一個
**搜尋空間**的斷言；**一句假的全稱否定，其代價不只是問錯問題** ——
上游若查出該句就在文件裡，全部 22 問之可信度一併折損。

故於定稿前逐句複核，並留下本檔，使日後可查**當時驗過哪些、以什麼驗的**。

---

## 1. 掃描方法

**形態式 pattern，非清單**（67 §1.2 之教訓：清單只找得到自己想得到的）。
取**否定形態 × 範圍詞**之交集：

| 側 | 詞形 |
|---|---|
| 否定 | `no`／`not`／`never`／`nowhere`／`none`／`nothing`／`without`／`cannot`／`could not`／`does not`／`has no`／`carries no`／`found no` |
| 範圍 | `section(s)`／`document(s)`／`clause`／`chapter`／`table`／`mapping`／`anywhere`／`any`／`all`／`every`／`specification`／`material` |

**全檔命中 19 句**，其中**對整個搜尋空間作斷言者 7 句**；
其餘 12 句為對單一條文或單一文件之陳述（例：「該封面不含 icon 表」），
不構成全稱否定，不在本檔之複核範圍。

---

## 2. 七句之複核結果

| # | 句（節錄）| 所斷言之範圍 | 當時之搜尋範圍 | 重驗 | 處置 |
|---|---|---|---|---|---|
| 1 | `no section in the document says when AUTO is unavailable`（Q7）| 全 129 節 | 129 節通讀，**未以該詞搜過** | **不成立** —— `2.3`／`16.3` 各有 `(AUTO is not shown in MTC configurations)`，實測 2 句 | **改寫**：問題自「有沒有任何條件」改為「**這一個算不算**」 |
| 2 | `The only difference between the two chapters is the chapter heading`（Q6）| ch17 對 ch18 之全部 | `17.1`／`18.1` 兩節之逐字比對 | **不成立（兩處）**：(a) `17.1` 較 `18.1` 多一句交叉引用；(b) `18.2`～`18.4` **未產出 leaf、不在 129 節內**，從未以需求讀過 | **改寫**：標題自「chapter 18 vs chapter 17」收窄為「**section 18.1 vs section 17.1**」，並於文中明寫「我們無法整章比對」 |
| 3 | `The four-mode set carries no condition of its own anywhere we have looked`（Q2）| 已看過之處（**已自帶限定**）| 129 節 ＋ CFTS043 ＋ MCT | **成立** —— 129 節提及四氣流模式者 4 句，皆述模式與高亮，無一給適用條件 | **範圍具名化**：把 `anywhere we have looked` 展開為三個具名來源 |
| 4 | `no section carries that mapping`（Q3）| 全 129 節 | 129 節 | **成立** —— icon × 對照之句 3 句（`2.5`／`16.5`／`16.16`），三者皆**指向**對照而無一**是**對照 | 維持 |
| 5 | `No document named "HMI Notes" exists in the material available to us`（Q8）| **已自帶範圍** | 客戶樹全樹 `find` ＋ 系統層 `mdfind` ＋ `Work_Projects/` 四個 repo | **成立** | 維持 |
| 6 | `no document we have says whether any of those values is retained`（Q9）| 我方所有文件 | CFTS009／CFTS010 ＋ 已取得之外部文件 | **成立而須補一項事實** —— Massage Seats 之 `M6` 陳述了**另一個功能**於點火循環後之狀態 | **改寫**：措辭改為 `none of the documents we have **read** states…`，並補入 `M6` 為事實 |
| 7 | `the document does not say` ／ `no test asserts either way`（附錄）| 全 129 節 | 129 節 | **成立** | 維持 |

**改寫者三句（Q6／Q7／Q9），維持者四句。**

---

## 3. 兩種錯，其中一種更難發現

**第 1 句是「沒查而說沒有」。** 那句話就在 `2.3`／`16.3`，而我方在別處
正是以它為第一軸（ATC／MTC）之出處 —— 同一份語料在兩處被讀成相反的樣子。

**第 2 句是「查了，但把查的結果說得比它大」。**
我方確實逐字比對過 `17.1` 與 `18.1` 之 W0 句（那部分是對的），
卻把結論寫成「兩章之唯一差別是標題」——
**「我比對過的那兩節」與「那兩章」之間，隔著三節我沒讀過的東西。**

第二種較難發現，因為它的每一步都做了，只有最後一句話跨出了範圍。

---

## 4. 一項措辭上的分別

Q9 原句為 `no document **we have** says…`，改為
`none of the documents **we have read** states…`。

**「我們有的」與「我們讀過的」不是同一個集合**，而可稽核的是後者。
凡對搜尋空間之斷言，其空間應以**我方之行為**界定（讀過、搜過、掃過），
不以**持有狀態**界定。
