# 23 — Comfort HMI / rev4 覆核：TC-007 判定程序、列高前例、R-C27

- 產出層：分析層｜2026-08-15｜對象：執行層
- 覆核對象：`docs/upstream/14_pilot_rev4_and_dryrun.md`
- 判定：rev4 **通過**。TC-007 待證據；列高待前例；Remarks 順序即刻調整。
  **寫回仍不執行。**

---

## 1. TC-007 —— 我不裁，因為我手上的證據不足以裁

執行層將此列為「本輪最可能被推翻的判定」，並把理由寫出來而非默默保留 ——
處置正確。

但我要據實說明：**我讀不到 13.3.1 之全文。** 我所見僅
`LS2.1) The user last selected lumbar/bolster selection will …`（60 字截斷）。
依 **R-C18**，我不得以截斷欄位做落點判斷 —— 那正是 6.3 與 2.16 兩次踩過的坑。

執行層之論證繫於一個事實主張：「**四種類型中恆有一個為選定項，無需步驟
建立**」。該主張若出自 13.3.1／13.2.1 之明文，PC2 即為 §4.4 所允許之
「feature initial state」，落點在 pre_conditions，不改；該主張若出自推論，
PC2 即為 §7 FF 所禁之「假定隱藏狀態」。

**判定規則（執行層自行套用，回報依據）**：

```
讀 13.3.1 與 13.2.1 之 full_text，回答一個問題：
  條文是否明文陳述「恆有一個調整類型為選定項」或給出預設選定項？

是 → PC2 為 feature initial state（§4.4 允許），落點 pre_conditions，不改。
     於 reasoning 具名該條文出處。
否 → PC2 屬假定隱藏狀態（§7 FF）。改法為：procedure 增一步「選定一個
     具名之調整類型」，PC2 刪除。此為 R-C25 之落點判定，非新規則。
     選定哪一個類型屬 interaction data，歸 procedure（§4.5），不構成造值。
```

**回報時須引該條文之相關句全文**，使判定可覆核。

若答案為「否」，此即同一形態之**第五次**，且與前四次一樣是逐條被抓到的 ——
但這次是由執行層自己標出來的，形態上已有差別。

---

## 2. 列高 —— 先量前例，不先決定

執行層列三方向並自陳「三個方向都是對範本呈現之改動」。**在量到前例之前
不決定**，理由是 profile canon 之既有紀律：**先量 done region，再立規則；
兩者不合時記錄量測而非直覺**（Privacy §3.8 之 `NA` 即由此翻轉）。

其 §8.2 第 1 項自己已指出可解之路，且成本為一次唯讀掃描。**照做。**

指示：掃描既有交付件之對應列高，對象與量測條件明載 ——

- `forms/…_Home_20260809.xlsx`（done region 144 列）
- Privacy、SXM、Projection 之已交付 workbook（依 `DELIVERY.sha256` 所記路徑；
  不可達者如實記為未量，不以推測代替）
- 每份回報：`customHeight` 為 True 之列數／總列數、`height` 之相異值、
  `wrapText` 狀態、以及**內容最長之三列其估算所需行數**

**判定規則**：

- 既有交付件**同樣受限**且未見客戶反映 → 方向 3（維持）有前例，採之，
  並將此事實登為 anomaly（已知可讀性損失，非疏漏）
- 既有交付件**不受限** → 本 feature 不宜與之分歧，於方向 1／2 中擇一，
  屆時另裁

**兩種結果皆須 Pei 過目後方寫回** —— 列高屬交付件呈現，Tier 2 以上。

---

## 3. Remarks 之資訊順序 —— 即刻調整（不待列高裁定）

無論列高如何處置，下列問題獨立成立：R-C24 要求 BLOCKED row 之 Remarks
承載「擁有該內容之文件名 ＋ 何以無餘留」，而現行措辭之首行可見範圍為
`[BLOCKED-SPEC] Long-press logic is defined by` —— **marker 看得到，
擁有者看不到**。

```
R-C27  受可見性限制之欄位，其資訊依可見性排序

某欄位之實際可見範圍小於其內容者，該欄位之關鍵資訊須置於可見範圍內。

適用於 Remarks 之 marker 型內容：marker 之後**緊接**擁有者／原因之最短
可辨識形式，說明性文字置後。

判準為「截斷於首行時，讀者是否仍取得該欄位存在之目的所要傳達者」。
```

修法（措辭自定，符合外部可見之限制）：

```
[BLOCKED-SPEC] Owner: HMI Core Logic and Flow requirement N0 — long-press
logic is defined there; with that delegation removed this requirement has
no content verifiable against the Comfort HMI specification alone
```

```
[BLOCKED-SPEC] Owner: CFTS044 — the equivalence to the previous 4-way
rocker hard control is defined there; with that delegation removed …
```

`blocked-remarks` gate 增一項：marker 之後 60 字元內須出現擁有者標記
（`Owner:`）。反向驗證之。

---

## 4. 通過、無須修改者

- **R-C25 全批掃描 4 候選 → 1 真**，三個誤報成因逐條分析 —— 採納。
  「詞彙重疊與同一事實之間沒有可靠閾值；門檻調高不能解決 007，調低會漏掉
  014」為正確結論，且它自證了 22 §4 之判準／表徵之分
- **`marker-whitelist` 反向驗證之設計**：對 004 掛 marker 後，豁免回報行
  確實顯示它取得了豁免，而白名單攔下它 —— **兩道機制並存且各自可見**，
  正是 R-C24 與 R-C26 互補之意
- **§9 第 3 項依據更換**（由 `source-class` gate 改為全批兩問測試）——
  R-C23 之第二個實例，且其自陳精確：「該 gate 只驗標籤存在，不驗落點是否
  正確 —— TC-014 之 PC3 標籤正確而落點錯誤，且它通過了該 gate 三輪」
- **生成器內留判定路徑之註解** —— 使下一個讀者不必回查往返包，採納此作法
- **dry-run 全程未 `save()`**、未產新檔、`DELIVERY.sha256` 未增列 —— 正確

---

## 5. 執行層作業指示（rev5）

1. R-C27 原文貼入 `RULINGS.md`。
2. 依 §1 讀 13.3.1／13.2.1 全文，套用判定規則，**引相關句全文**回報；
   依結果處置 TC-007 之 PC2。
3. 依 §3 改寫兩個 BLOCKED row 之 Remarks，`blocked-remarks` gate 增
   `Owner:` 檢查並反向驗證。
4. 依 §2 掃描既有交付件之列高，回報量測條件與結果；**不依結果自行處置**。
5. 全批重跑 lint 與 §9 自評（依 R-C23），僅回報變動項。
6. **寫回仍不執行** —— dry-run 報告依 §3 之 Remarks 變更更新即可。
7. 上繳 `docs/upstream/15_pilot_rev5.md`。git 不執行。

---

## 6. 本包產生之新條文清單（自檢）

| 條文 | 已以可貼入區塊形式出現 | 狀態 |
|---|---|---|
| R-C27 受可見性限制之欄位，其資訊依可見性排序 | ✅ §3 | 已簽 2026-08-15 |

R-C27 適用全 feature，安置位置待 canon re-sync。§1 之判定規則與 §2 之
列高規則為程序，非條文；其結果另裁。
