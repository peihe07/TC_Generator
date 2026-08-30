# 下放包 55 —— canon 已改（R-G28 立條）、`RULINGS.sha.tsv` 重生

- 日期：2026-08-30
- 方向：分析層 → 執行層
- 前一包：`54_wifi_download.md`（T66 照跑，本包並行且**優先**）
- 對應上繳：`docs/upstream/48_canon_rg28.md`
- **本包為全域線之變更**，其射程及於全部 feature

---

## 一、已發生之變更（分析層已寫入，執行層須驗）

**Pei 裁定 2026-08-30**：「CFTS Embedded Objects 逐 feature 檢查」寫入 canon。

**分析層已直接編輯 `docs/fw036/FEATURE_ONBOARDING.md`，三處**：

| # | 落點 | 變更 |
|---:|---|---|
| 1 | §0 Tier 0（intake 清單） | 新增一則 bullet，指向 §9.2 之條文 |
| 2 | §9.2 索引表 | 新增一列 `R-G28` |
| 3 | §9.2 條文區 | 新增 `#### R-G28` 條文本體 ＋ 成因段（位於 R-G27 之後、`#### R-G4／R-G7 之原文與 R-G12 之來源` 之前） |

**條文本體**（`R-G28`，逐字如下，供比對）：

```
R-G28（Pei 裁定 2026-08-30）：intake 時須檢查該 feature 之母 CFTS 是否於
`…/Reference Documents/CFTS Embedded Objects/CFTS<nnn>/` 下有嵌入物件；
有者逐張轉為可讀影像並出「由圖找列」二欄表：**其所載之值／流程**、
**其對應之 037 列**，併記其與文字來源**一致或不一致**。不一致者為 DR 之材料。
查無者亦須記明「已查、無此目錄」，不得以未提及代替。
嵌入物件之 ObjectID 落於錨點池號段內而**不在錨定語料內** ——
其內容不進路徑 A，故錨定之三機制對其一律無效；
該事實須記入該 feature 之 `ANCHOR_POOL.md` 附記（R-G8）。
```

---

## 二、其後果 —— **`RULINGS.sha.tsv` 已過期**

依 **R-G13**（裁決引用制）與 **R-G22**（任何字元變動皆變更其 sha）：

1. `R-G28` 為新條，**`RULINGS.sha.tsv` 中無其列**
2. §9.2 索引表之變動**不影響各條之條文本體**，但 `rulings_hash.py` 之
   切段邏輯若以節界定範圍，**須實測其是否波及鄰條**（尤其 `R-G27`，
   其與新條相鄰）

**故本包之首要任務為重生並驗其影響範圍。**

> ⚠ **R-G22 之代價於此兌現**：若重生後有任何**既有條**之 sha 改變，
> 表示切段邏輯把新條之文字算進了鄰條 —— **那是實作缺陷，不是條文變更**，
> 須停下回報，不得以「反正要換發引用」帶過。

---

## 三、任務（T67，**優先於 T66**）

| # | 任務 |
|---|---|
| T67a | **canon 變更之驗證**：`docs/fw036/FEATURE_ONBOARDING.md` 之三處變更逐一核對（§0 bullet、§9.2 表列、§9.2 條文區）。**條文本體與 §一之逐字文字比對**，不符即停 |
| T67b | **`RULINGS.sha.tsv` 重生**：跑 `scripts/rulings_hash.py`（**全量重生，非部分更新**）。輸出 **diff**：哪些列新增、哪些列之 sha 改變、哪些不變。**既有條之 sha 若有任何改變，逐條列出並停下回報**（§二之 ⚠） |
| T67c | **`R-G18` 之 canon 引用閘重跑**：新條文含 `FO §9.2`／`R-G8`／`G-M` 等引用，**須通過 `scripts/canon_refs.py`**；新增之 unresolved／ambiguous 即紅（R-G18「waiver 只減不增」） |
| T67d | **`GATES.tsv` 之檢視**（R-G17）：R-G28 為 intake 階段之人工項，**非 lint 閘**；確認其不需登錄，或依 R-G21 標為「人工項」。**陳報結論，不逕改** |
| T67e | **sw_update 側之連動**：`ANCHOR_POOL.md` 附記（上繳包 46 §1 已辦，本項為追認並確認其措辭與 R-G28 之要求相符）；`REASONING.md` 之 intake 規範記明其已升格為 R-G28，**feature 側之記述改為引用而非重述** |
| T67f | **git**：canon 變更 **單獨 commit**（R-G26 之精神：不混入其他變更），pathspec 明列 `docs/fw036/FEATURE_ONBOARDING.md` 與 `docs/fw036/RULINGS.sha.tsv`。**執行層只準備不執行**（R-G5）—— 備妥指令與訊息，由 Pei 執行 |

**T66（`inputs/` 全盤點 ＋ `Wi-Fi Download` 起草）於 T67 之後續跑**，不取消。

---

## 四、上繳包要求（`docs/upstream/48_canon_rg28.md`）

1. **T67b 之 sha diff —— 本輪核心**（新增列 ＋ **既有條有無變動**）
2. T67a 之逐字比對結果
3. T67c 之 `canon_refs` 輸出
4. T67d 之陳報、T67e 之連動、T67f 之 commit 指令（未執行）
5. 獨立自評（入 BACKLOG）—— 特別回答：**R-G28 令「查無者亦須記明已查」，
   而既有七個 feature 之 intake 皆早於本條 —— 其「未記明」究竟是
   「查過而沒寫」還是「沒查」，現已不可區辨。
   本條對既有 feature 之追溯適用，是否應一併裁定，抑或明訂其只管新 feature**
