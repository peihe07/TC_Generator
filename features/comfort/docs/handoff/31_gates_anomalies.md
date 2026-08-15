# 31 — Comfort HMI / forbidden-verb gate、三則 anomaly、第十軸之前瞻

- 產出層：分析層｜2026-08-15｜對象：執行層
- 承接：下放包 30（同一次覆核，拆檔）

---

## 1. `forbidden-verb` gate —— 授權

執行層兩度建議（上繳 18 §11.1、19），我兩度未授權。**現授權。**

證據足夠：初稿之 `Check the A/C state`／`Locate the front defrost control`
兩處，是**手查**才抓到的（18 §9 第 5 項）。第三批仍靠人眼掃 §5.1 之九個
禁用動詞，不是可持續的作法。

規格：比對 `test_procedure` 每一步之**行首主動詞**與 §5.1 之九詞
（`observe`／`observe whether`／`see if`／`check whether`／`confirm whether`
／`verify`／`watch`／`monitor`／`inspect`），另加執行層自加之 `locate`。

**例外**：`verify` 出現於目的子句（`... to verify that ...`）者不算 ——
§5.1 明文允許。gate 須能區分行首主動詞與子句內動詞，**不得以字串包含
判定**（否則會誤殺合法用法，而誤殺會促使作者繞過 gate 而非改正）。

反向驗證：注入 `Check that ...` 於某步之行首 → FAIL 並指名該 tc_id 與步號。

---

## 2. ER 主詞之詞表 —— 授權為**補網**，不得作為判準

執行層 18 §11.2 自陳：ER 主詞之檢查仍是人眼，而 rev1／rev2 兩度栽在同處
正說明人眼會漏；但它同時指出詞表是 22 §4 明說「可繞過而不自知」者，
故「只能當補網不能當判準」。**該自我限制正確，照此授權。**

- gate 名 `er-subject-net`，比對 `is recorded`／`is readable`／`is noted`
  ／`can be read` 四詞組
- **gate 之輸出須自稱為補網**，形如：
  `- PASS — er-subject-net (a safety net, not the criterion; the criterion
    is §6 and is human-reviewed)`
- **§9 第 10 項之依據不得引用本 gate**（R-C23）。該項仍須逐行讀 ER 並
  具名其獨立依據

理由：一個標榜自己是判準的補網，會使下一個人以為那項已被覆蓋 ——
而 rev1／rev2 兩次錯誤正是「以為被覆蓋」。

---

## 3. 三則 anomaly —— 登記，皆不阻塞

### 3.1 `3.4` 之 `when configured` 無受詞（A-CF17，note）

條文：`For soft top vehicles such as JL/JT, **when configured**, the rear
defrost button will not appear when not present in the vehicle.`

執行層依 R-C30 附搜尋範圍：根目錄 `data/section_fulltext.tsv`（129 節），
pattern `configured`，**命中 3 處**（3.4、6.3、11.11），其餘兩處皆為
`configured with X`（配備 X）之形式，**3.4 之 `when configured` 無受詞**，
無法以同一讀法還原。

處置：登記，**不推測其所指**，PC 維持不寫入任何配置步驟（§8.4.1）。
列 RD-1 候選。`-028` 之 TC 內容不因此變動 —— 它已迴避該詞。

### 3.2 `3.3` 未定義 `not available` 之可觀察形態（A-CF18，note）

3.3 只說 `available`，未說不可用時之外觀；`greyed out` 之描述在 **2.10**，
屬 `Climate Modes`，依 §8.2.1 不得於 3.3 之 TC 驗證。

故 `-027` 之 ER 停在 `are not available`，其判定實際仰賴測試員對「不可用」
之理解。**執行層自陳「這是本批裡最不滿意的一行，但寫得更具體就會踩進
2.10」—— 該取捨正確**：越界之害大於措辭之弱。

處置：登記；`reasoning` 須具名 2.10 為該外觀之擁有者（若尚未具名則補）。
列 RD-1 候選。

### 3.3 多節 `specification_reference` 之儲存格呈現未實測（A-CF19，note）

`-026`／`-027` 之 N 欄將為三段以 `; ` 分隔、各帶完整 stem 之字串
（約 240 字元），而交付件之列高為 14.0 且 `wrapText=True`（A-CF16）。

處置：登記，**於下次寫回時一併實測**該欄之呈現，結果併入 A-CF16 之
重審依據。本批不寫回，故本項現為未測而非已測。

---

## 4. 第十軸之前瞻 —— 影響遠大於本批，須逐節判定

執行層依 R-C30 全掃：根目錄 `data/section_fulltext.tsv` 全 129 節，
pattern `rear defrost`／`soft top`（不分大小寫）。

| 軸 | 命中節 | 合計 leaf |
|---|---|---|
| 第十軸 rear defrost | 2.9(4)、2.10(6)、3.2(8)、3.4(1)、16.4(1)、16.8(12)、16.9(2)、16.10(8) | **42** |
| 第十一軸 soft top | 3.4(1) | **1** |

**「提及 rear defrost」不等於「需要 rear defrost 有無之 PC」。**
本包不逐節判定，但立下規則：

> `Climate Modes`（2.9／2.10）與四個 ICS 組（16.4／16.8／16.9／16.10）
> 生成時，凡欲寫入第十軸之 PC 者，一律逐節走 R-C28 三問 ＋ R-C31，
> **第一問須具名該節自身之條文相關句**；不得以 3.4 之句子為所有節之出處
> （R-C29 允許跨節取據，但要求具名實際出處，不是允許一句話覆蓋全語料）。

**第十一軸全語料僅 3.4 一處** —— 它是為一個 leaf 立的軸。執行層主動記錄
此事，正確：一個永遠只有一個使用者的軸，其存在本身是需要被看見的事實，
而非缺陷。

---

## 5. 執行層作業指示

1. 加 `forbidden-verb` gate（§1）與 `er-subject-net` gate（§2），
   兩者皆反向驗證；`er-subject-net` 之輸出須自稱補網。
   lint 由 35 增至 **37**。
2. 登 A-CF17、A-CF18、A-CF19（§3）；A-CF17／A-CF18 列 RD-1 候選。
3. `-027` 之 `reasoning` 補具名 2.10 為 `not available` 外觀之擁有者
   （若已具名則回報無變動）。
4. §4 之逐節判定規則寫入 `RUNBOOK.md` 與 profile §3.2 第十軸之說明段。
5. 併同下放包 30 之作業一次上繳
   `docs/upstream/20_batch2_final.md`。git 不執行。

---

## 6. 進度

| | 數 |
|---|---|
| 驗證單位 | 403 |
| 已生成（leaf 計） | 28 |
| 已生成（TC 計，`-024` 拆後） | **31** |
| 未開始（leaf 計） | 375 |

**TC 數自本批起大於 leaf 數**，兩者不再可互換使用；進度一律以 leaf 計，
工作量以 TC 計。

---

## 7. 本包產生之新條文清單（自檢）

無新條文。§1／§2 為 gate 授權，§3 為 anomaly 登記，§4 為前瞻規則
（寫入 RUNBOOK 與 profile，非 R-Cnn）。
