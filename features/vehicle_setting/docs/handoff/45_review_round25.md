# 45 下放包 — 25 輪覆核：四項確認、一條新規、26 輪續產

分析層寫入，2026-08-22。**速度優先：本包一次裁完。**

**產出現況：58 條交付、12 條移出／未撰寫。**

---

## 1. 三項處置確認（皆為既有政策之適用，不改）

### 1.1 `ScreenOFF-051` —— **處置正確**

`4859108` 令 HU 送 `$TGW_DISP_STAT$`，其值定義於 **`{CFTS020}`（具名）**。

依 canon §8.4.2：值定義於**外部 spec** 者，屬該 spec 之擁有者，
**本 feature 不吸收**；本 Req 所擁有者僅「該訊號被送出」此一事實。

ER 寫「a TGW_DISP_STAT signal is transmitted on CAN-B」——
**可觀察、不斷言值、不越界。確認採用。**
`reasoning` 須記「值由 {CFTS020} 擁有」之委派句（§8.2.1）。

### 1.2 `TwoStagesHeatedSeat-057` 等三條標 `dr15_exposed = no` —— **確認**

24 輪 §6-4 與本輪 §6-4 兩度提出而未解，**本包解之**：

```
分析層裁定 2026-08-22（結案 24 輪 §6-4）
以畫面行為驗證狀態循環之 TC（`TwoStagesHeatedSeat-057`／
`ThreeStagesHeatedSeat-080`／`TwoStagesVentedSeatsManagement-039`），
其 `dr15_exposed = no` **成立**。

理由：該等條文之需求標的為**畫面狀態之循環**（`off → high → low → off`），
請求訊號為其實作手段。DR-15 所問者為請求訊號之編碼，
**其答覆不改變畫面應如何循環** —— 循環由 `$HeatedSeatFL$` 等狀態訊號
與畫面規格決定，非由請求訊號之位元寬決定。

**惟若 DR-15 覆為「承載階數」，該等 TC 之 procedure 若含請求訊號之
斷言者仍須複檢** —— 判準以「是否斷言請求訊號之值」為準，本輪已掃（3 條）。
```

### 1.3 A-VS85 兩對嚴格等價 —— **處置正確，不合併**

§8.2.1 之反向禁令明文：TC 作者**不得合併 RD sub-id**。
標 `duplicate_of` ＋ `axis = none` 為正解。

**其總數未量一事**：不阻塞生成，**入 BACKLOG**。
**惟最終覆蓋報告須揭露 `duplicate_of` 之條數** ——
否則「58 條 TC」會被讀成 58 個獨立驗證點。

---

## 2. R-VS46 —— 「已窮盡」之宣稱須附涵蓋清單（本輪唯一新條文）

21 輪測五個候選形態後宣稱 `(b) = 0`；25 輪找到**彎引號**，
其為當時五式所不涵蓋者。

**問題不在漏了一式，在於當時之宣稱未列其涵蓋範圍** ——
讀者（含分析層）因而把「測過五式」讀成「窮盡」。

```
R-VS46（分析層裁定 2026-08-22）
凡宣稱某一掃描「已窮盡」「無殘餘」「(b) = 0」者，
**須於同一段落逐式列出其所測之形態清單**，並具名其**未測者**。

未列清單之窮盡宣稱，一律讀為「就已測形態而言為 0」，
**不得作為後續判斷之前提**。

實例：21 輪測 `'值'`／`is set to`／`shall be set to`／`shall be <大寫>`／
裸值 五式，**未測彎引號**；25 輪即於彎引號中找到 `ENS_DSBL`（2 leaf）。

**本條適用於分析層與執行層雙方。**
```

---

## 3. 26 輪指令 —— 續產，一項收尾

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/45_review_round25.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/24_batch0809.md，六節先留空。
D-2  逐字轉錄 45 包 §2 之 **R-VS46** 入 RULINGS.md。
D-3  BACKLOG.md 增：A-VS85 之「同一需求兩次書寫」總數未量。
D-4  `ScreenOFF-051` 之 `reasoning` 補委派句（值由 {CFTS020} 擁有）。
D-5  依 R-VS35 列兩數。

## 作業（三項，R-VS25）

W-74  **引號／值形態之窮舉收尾**（依 R-VS46）
      對 237 leaf 所引條文，逐式測下列形態並**列出完整清單**：
        直引號 `"值"`／彎引號 `“值”`／單引號 `'值'`／彎單引號 `‘值’`／
        全形引號 `「值」`／方括號 `[值]`／裸值／`is set to`／
        `shall be set to`／`shall be <大寫>`／`passes to`／`equals`
      **每式列其命中數與新解出之 token／leaf**；
      **並具名本輪仍未測之形態**（R-VS46）。
      新解出者更新 `writability.tsv`，**逐筆過 `guard()`**。

W-75  batch08 —— **10 條**
W-76  batch09 —— **10 條**
      依逐 Layer 2 輪流（配額以當時餘量重算），套 profile ＋
      canon §8.7.5 v3 ＋ R-VS43 ＋ Sibling Rows ＋ 無效值優先序；
      選入後逐條過 `guard()`；§9 十七項自檢 ＋ DBC 值表核對。
      **W-75 完成後不等覆核，逕行 W-76。**
      **某 Layer 2 餘量不足其配額時，自餘量最大者補足並記明。**

## 禁區

git 不執行。不寫回工作簿。不代擬條文。各版保留不刪。
不得再執行型 B 之唯讀搜尋。不得採用他車型 PROXI 表之值。
不得合併 037 之 leaf（§8.2.1 反向禁令）。

## 升級條件

W-74 新解出之 token 使某 leaf 由阻塞轉可寫者 > 10（**正向**，須回報）；
W-75／W-76 之交付合計 < 12；
§9 出現新型違規。
**本輪無必停項 —— 兩批連續生成，不中斷。**
```

---

## 4. 待 Pei —— **無變動，五份仍待送**

DR-22′（79 leaf，是非題）／DR-20／DR-23／DR-8′／DR-24′／DR-21／DR-18／DR-11。

**DR-22′ 仍是最大的一塊**，一個是非題解 79 個 leaf。

---

## 5. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS46 | 「已窮盡」之宣稱須附涵蓋清單並具名未測者 | 分析層（本輪額度用畢） |
| 24 輪 §6-4 之結案 | 畫面行為型 TC 之 `dr15_exposed = no` 成立 | 分析層 |
| `ScreenOFF-051` 之確認 | §8.4.2，值由 {CFTS020} 擁有 | 分析層 |
