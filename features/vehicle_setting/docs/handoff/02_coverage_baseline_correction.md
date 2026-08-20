# 02 下放包 — 覆蓋母體之更正與 01 輪殘項排序

分析層寫入，2026-08-20。對象：執行層 checkpoint（W-0c／W-16／W-18 完成）。

---

## 1. 獨立複驗 —— 該發現成立，且比回報所述更乾淨

**依 canon §5a 第 16 條，本節非照單接受。** 分析層自 `inputs/` 實體檔
（四份 037 + 036）重測，掃描條件：037 `Analysis Report`、表頭列 7
（**先 `\s+`→單一空格**再定位欄名）、資料自列 8、A 欄非空為 leaf、
`Categorization` 欄以表頭字串定位（實測為第 6 欄）；036
`Test Case Specification 測試用例規範` 資料列 10–246、D 欄。

### 1.1 `Categorization` 之分布

| 值（逐字） | 數 |
|---|---|
| `Functional Requirement` | **237** |
| `Heading` | **25** |
| `Information` | **8** |
| `information`（小寫） | **1** |
| 合計 | 271 |

### 1.2 兩個集合完全相等

| 量 | 值 |
|---|---|
| 036 覆蓋之 leaf | 237 |
| 未覆蓋 leaf | 34 |
| 非 Functional leaf | 34 |
| **交集** | **34** |
| 只在未覆蓋側 | **0** |
| 只在非 Functional 側 | **0** |

逐 family 亦相符：非 Functional = Common 10／HeatedSeat 11／VentedSeat 9／HSW 4；
**可測 leaf = Common 46／HeatedSeat 88／VentedSeat 72／HSW 31**（合 237）。

### 1.3 一項回報須修正措辭

執行層記「HeatedSeat 有一列 `Categorization` 是小寫 `information`，
**區分大小寫的掃描會漏**」。**方向要說反過來**：

- 篩 **Functional**：`startswith('Functional')` 區分大小寫 = **237**，
  不分大小寫 = **237**，**差 0** —— 該筆是 `information`，兩種寫法都不會
  被誤收進 Functional
- 篩／數 **Information**：區分大小寫得 **8**，不分大小寫得 **9**

**故該小寫值影響的是「非 Functional 之細分類」，不影響可測母體之界定。**
`recon.py` 之 `.lower()` 在此不是救了它，是恰好不需要救。
**但它仍是真缺陷**：任何以 `== 'Information'` 分類之下游都會少一筆
（A-VS20）。

### 1.4 額外收穫：**A-VS01 一併消解**

以 037 之 `Categorization` 對 SYS2 之 `Category` 交叉列表（逐 leaf）：

| 037 | SYS2 | 數 |
|---|---|---|
| Functional | Functional Requirement | **236** |
| Heading | Heading | **25** |
| Information | Information | **8** |
| information | Information | **1** |
| Functional | **NO_REF** | **1** ← `SWE1-VC-HeatedSteeringWheel-009`（CFTS100） |

**兩表逐 leaf 完全一致，零錯配。**

→ **A-VS01（「25 個 leaf 之 SYS-RA 指向 SYS2 之 Heading 列」）除役**：
那不是錯配，是**同一批非需求列在兩份文件裡各自被正確標記**。
分析層當初把它登記為異常，是因為只看了 SYS2 側而沒讀 037 自己的
`Categorization` 欄 —— **答案一直在同一張表的第 6 欄**。

---

## 2. 條文與數字之更正（**逐項取代先前記載**）

```
R-VS15（可測母體，取代一切先前之「271」表述）
本 feature 之 TC 母體為 037 四份中 `Categorization` 開頭為
`Functional`（不分大小寫）之列，共 237 個 leaf。

  Common Features        46
  Heated Seat            88
  Vented Seat            72
  Heated Steering Wheel  31

其餘 34 列（Heading 25／Information 9）為文件結構與說明，非可測需求，
**不產 TC、不佔 036 之列、不計入覆蓋稽核之分母**。

036 現有之 237 列恰為此 237 個 Functional leaf，兩集合相等
（交集 237，兩側差集皆 0）。

推論：
(a) 「34 個未覆蓋 leaf」之表述作廢。**本 feature 沒有覆蓋缺口。**
(b) 覆蓋稽核之判準改為：TC 數 >= 237，且每個 Functional leaf 至少一列
    （§8.2.2：一個 leaf 得對多個 TC，反向不可）
(c) 271 僅用於描述 037 之列數，不得作為任何比率之分母
```

| 先前記載 | 更正後 |
|---|---|
| 271 leaf / 34 未覆蓋 | **237 可測 leaf / 0 覆蓋缺口** |
| 245 / 271 之 N 欄已定 | **236 / 237 已定**，未定 1（DR-11） |
| A-VS01 PENDING | **除役**（§1.4） |
| A-VS18 PENDING | **除役** —— `recon.py` 未錯，兩判準在數兩件事，且 recon 之判準與 036 之實際投影一致 |
| W-18 之 26 個未定 | **1 個**（25 個隨非 Functional 一併消解） |

**新開 A-VS20**：037 之 `Categorization` 存在大小寫不一致（`information`
一筆），任何區分大小寫之分類器會少計。**登記於 RD-1 FYI 類**，
我方以不分大小寫比對吸收，不待上游修正。

---

## 3. 01 輪殘項之排序（**照執行層之判斷，不改**）

執行層之排序與理由與 01 包 §7 一致，分析層無異議。逐項確認：

| 序 | 作業 | 為何是這個順序 |
|---|---|---|
| **1** | **W-8** 三來源 `$變數$` 對照 | CFTS044／DBC／LID 表為三個不同上游作者之產物 —— **本 feature 目前唯一之跨源獨立檢驗**。尚缺 CFTS044 內嵌值域抽取（兩式並用：`$var$ = [值]`、`路徑.名稱 == "值"`）。三者不一致逐項列出並停 |
| **2** | **W-13** 26PI2.5/HMI 全文掃描 | A-VS10 之唯一獨立檢驗。**檔數以實測之 107 為準**，分析層先前所記之「約 112」為 `list_directory` 之目測，非計數 —— 以執行層實測值取代 |
| **3** | **W-15b′** DBC ↔ LID 逐屬性交叉 | R-VS9 v2 第 (3) 項之依據；91% 起始位元差異已知，但 LID 表側尚未交叉 |
| **4** | **W-17** LID 列數差 6 + `TRUNCATED_ENUM` 其他形態 | 影響 `lid_map.tsv` 之完備性，不阻塞 |
| **5** | **W-9** Comfort 43 leaf 逐條對照 | **做完必停**。排最後正確 —— 它是唯一會中斷批次之作業 |

**W-9 之比對母體須改用可測 leaf**：本 feature 側之對照集合為 237 個
Functional leaf，非 271。Comfort 側之 43 為子字串上界，維持不變。

---

## 4. 待 Pei（**與 01 包 §5 相同，新增一項**）

| # | 事項 | 狀態 |
|---|---|---|
| P1 | 刪 `features/vehicle setting/` | 未處理 |
| P2 | 產物入庫 | 未處理 |
| P3 | 裁 **R-VS9 v2** | 未處理 |
| P4 | 追認 R-VS8 | 未處理 |
| P5 | 追認 R-VS11 撤回、DR-10 撤銷、A-VS06 除役 | 未處理 |
| **P9（新）** | 追認 **R-VS15**（可測母體 237）、**A-VS01 除役**、**A-VS18 除役** | 本包提出 |
| P6 | R-VS7 —— 俟 W-9 產出 | 可延 |
| P7 | R-VS10 | 可延 |

---

## 5. 一項流程觀察（記入 canon 候選）

A-VS01 與 A-VS18 兩條異常，**成因相同**：分析層在讀 037 時只取了
`SWE-Requirement ID`／`Source Requirement ID`／`Requirement Title`／
`Requirement Description` 四欄，**未讀 `Categorization`（第 6 欄）**，
於是把「037 自己標記為非需求的列」當成需求，並把由此產生的兩個下游
現象各自登記為異常。

> **候選通則**：對一份結構化來源建立 leaf 全集時，**先列出該來源之
> 全部欄位並逐欄判斷其是否影響 leaf 之界定**，再取值。
> 只取「看起來需要的欄」會使界定判準隱含而不可檢驗 ——
> 其症狀是下游出現數個彼此獨立、實則同源的異常。

本例之代價：兩條異常、一次覆蓋缺口誤報（34）、一次工具誤責（A-VS18
指 `recon.py` 與下放包不一致，實則 `recon.py` 是對的）。
