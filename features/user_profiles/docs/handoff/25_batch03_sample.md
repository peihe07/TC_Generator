# 25 下放包 — 覆核結案（78／78）與第三批開批

**本包無裁決條文。** 24 輪上繳**核可**。

## 覆核結案

**78 條全部經第二人逐條讀畢**（`TC-001`～`078`）。
分析層自 20 輪起積欠之內容覆核至此結清，未經覆核者為 **0**。

### P-4 之論證比我提的更強，且結論相反 —— 接受

我以「六條依 description 生成，若 title 才是需求單位則驗錯東西」要求重生成。
執行層以 180 leaf 全量實測反證：

- Description 以條款編號起首 **105/180**；**Title 0/180**
- 決定性者為 `125-03`：其 Title 寫手套箱提示，而 **PVAL8 通篇沒有手套箱** ——
  **該 Title 指向不屬於自己章節的行為**

「一個需求單位不可能指向不屬於自己章節的行為。Title 會，Description 不會。」
—— 這句話把問題一次解掉。六條不重生成，A-UP11 降為記載瑕疵，正確。

### `062`／`063` 之對調成立，且它補了一條我沒寫的

我只指出判級與 §8.7.4 相衝。執行層另指出**「取中」這個做法本身就是錯的** ——
一條 TC 之判級取其**核心斷言**，不取各 ER 之平均。這條比對調本身更通用。

其佐證亦紮實：`061`／`062`／`063`／`064` 四條中，
**「手套箱實際鎖上」之唯一斷言在 `064` 之 ER2**，
而 `062` 是唯一完全不觸及實體狀態者 —— 判 P2 與此一致。

### `TC-070` 之 `etc` 一節

我說全稱斷言超出 procedure。執行層補：13.2 逐字為 `(PU0934, **etc**)`，
**spec 自己就沒列盡該集合** —— 全稱斷言在此不只超出 procedure，
是超出**條文所能界定的範圍**。

### M-2 之閘在同一輪攔下立閘者本人

`062` 之新 reasoning 寫「由 **126-03** 承擔」，非合格 leaf id，D-1 判紅。
**閘立起來的同一輪就抓到寫閘的人**，這是它會生效的證據。

## 唯一新發現

### Q-1（style-divergence）`TC-075` 之 ER2 內嵌逐字字串未加引號

> `The Connected Account row reads **Save your preferences to the cloud and
> access them from vehicle to vehicle**, with no Uconnect.com subscription clause`

該句係逐字引自 p16 之覆寫註記，屬**顯示文字**，
依 §11「Display text and indicators that are values rather than tappable
elements follow the same convention」應加雙引號。

同批之 `TC-055`（`“Function not available while in Valet Mode…”`）與
`TC-072`（`“Exit Valet Mode”`）皆已加 —— **同批不一致**。

**作業**：`075` 之該字串加雙引號；並自檢全批**逐字引自 spec 而未加引號**者
（G18 現查引號內字面值，查不到「該加而未加」之反向）。

## 作業

### A. Q-1 與兩個自陳缺口

1. `075` 加引號；全批反向自檢（該加引號而未加者）
2. **`remarks` ↔ `specification_reference` 一致性閘**（24 輪 §6 第 1 項）
   —— C-2 與 P-3 為同一形狀之兩次發生，現行 K-4a／K-4b 掃不到。
   判準建議：`remarks` 中出現之節號，須與 `specification_reference` 之集合一致；
   不一致即紅。含方向性案例
3. **A-UP13 之三個行為仍無 TC**（承 23 輪）—— 併入第三批取樣，不再延後

### B. 第三批取樣清單（先回報，不生成）

現況：180 leaf 中已覆蓋 **72**（pilot 16 ＋ batch01 27 ＋ batch02 29），
餘 **108**，全部落在 ch4–ch8。

**第三批 = Preference Storage（ch4）之剩餘**，估 26 leaf。
理由：ch4 為 Layer 3 之首章、Test Set 一次收乾淨（同前例批界原則）、
且 `PROF-001-01` 之 PLP 併列已在 pilot 受檢，其餘 ch4 leaf 可沿用同一判準。

清單須具名：
- 三項必含（比照前例）：待兌現之 (b) 類委派、§7 列舉配對、變體對造之新 axis
- **A-UP13 之三個行為**歸入何 leaf
- 估計條數與其切分依據

### C. 不變

第三批**生成**待取樣清單覆核。

## 不在本包授權範圍

- 任何寫入性 git（R-G5／R-G12）
- 寫回工作簿（R-U14）
- 第三批之生成 —— 待取樣清單覆核

## 上繳

`docs/upstream/25_batch03_sample.md`，更新 `docs/INDEX.md`，附獨立判斷。

## 現況總表（供第三批之後對照）

| 項 | 數 |
|---|---|
| 語料 | 78 條 ／ 已覆蓋 72 leaf ／ 餘 108 leaf |
| 已覆核 | **78 / 78** |
| 閘 | lint 0 違規、五支 audit 之 self-test 全過 |
| 擋 Phase 6 | A-UP09 / R-U14（DV gate 未立） |
| 待 Pei | R-U17、DR #3–#7、N-XF01、A-UP10、A-UP11 是否回報上游 |
