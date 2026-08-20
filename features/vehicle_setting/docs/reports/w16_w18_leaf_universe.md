# W-16 / W-18 — leaf 母體之判準與 N 欄未定項（01 輪）

## W-16：`recon.py` 46 vs W-2 之 56 —— 追因完成，**recon 是對的**

`scripts/recon.py:602`：`is_leaf = cat.lower().startswith("functional")`
—— 依 037 之 `Categorization` 欄過濾。
下放包 §5.1 之判準為「A 欄非空者為 leaf」，**無此過濾**。

| family | A 欄非空 | Categorization = Functional* | 差額 | 非 Functional 之分布 |
|---|---|---|---|---|
| Common Features | 56 | **46** | 10 | Heading 8／Information 2 |
| HeatedSeat | 99 | **88** | 11 | Heading 8／Information 2／`information` 1 |
| VentedSeat | 81 | **72** | 9 | Heading 6／Information 3 |
| Heated Steering Wheel | 35 | **31** | 4 | Heading 3／Information 1 |
| **合計** | **271** | **237** | **34** | Heading 25／Information 9 |

### `Categorization` 之值域全集（W-16′，04 包 §4 要求）

對 271 列**逐列取值**：`Functional Requirement` **237**／`Heading` **25**／`Information` **8**／`information` **1** —— **四值合計 271，無其他值、無空值。**

此為**全集之宣告**，非樣本：若某 037 版本另有第五種值，`startswith("functional")` 會將其歸入非 Functional 而不報錯（canon §5a 第 12 條），故本行須於任何 037 換版後重測。

> `HeatedSeat` 有一列之 Categorization 為小寫 `information` ——
> recon 之 `.lower()` 吸收了它；**區分大小寫之掃描會漏**。

## 關鍵結果：34 = 34，且為同一批 leaf

**「036 未覆蓋之 34 個 leaf」與「非 Functional 之 34 個 leaf」為完全相同之集合**
（交集 34，兩側差集皆 0；逐 family 亦相同：10 / 11 / 9 / 4）。

推論：

1. **036 之 237 列 = 037 之 237 個 Functional Requirement 列。**
   W-6 所報之「未覆蓋 34」**不是覆蓋缺口** —— 那 34 個是 Heading 與
   Information 列，本就不是可測需求。
2. **TC 生成之 leaf 母體應為 237，非 271。**
   R-VS4 之四個 Test Set 其可測 leaf 數為 **46 / 88 / 72 / 31**。
3. **A-VS18 除役** —— recon 與 W-2 並非「兩個工具對同一件事給出不同答案」，
   而是**兩個判準在數兩件不同的事**，且 recon 之判準與 036 之實際投影一致。

## W-18：N 欄未定之 26 個 leaf —— 25 個自動消解

| 群 | 數 | 屬性 | 處置 |
|---|---|---|---|
| NO_SECTION | 25 | **全部為非 Functional**（Heading／Information） | **不需處置** —— 不產 TC，無 N 欄 |
| NO_ID | 1 | `SWE1-VC-HeatedSteeringWheel-009`，**Functional Requirement** | **待 DR-11**（CFTS100 之身分） |

**可測 leaf 237 個中，N 欄已定 236、未定 1。**

01 包 §2.2 記為「245 / 271 已定，26 / 271 未定」——
以可測母體重述為 **236 / 237 已定，1 / 237 未定**。
該 1 個即 A-VS12／DR-11，**非 25 個一般性缺口**。
