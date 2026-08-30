# 56 — B1 回報覆核與四項裁示

下放包 | 分析層 → 執行層 | 往返 NN = 56

前置：55 包 B1 回報（`data/55_b1_report.md`）已覆核，判定 **ACCEPT**。
基底確認成立：現行 corpus = `generated/batch_00{1..7}.json`（283 條，第三代）；
pm_29 落後兩代，`(req_id, test_item)` 逐字重疊僅 37/390。
**55 包 §0 之自陳不僅成立，且低估差距** —— 據實記明。
55 包 §E「寫回移至 56 包」由本包取代，寫回移至 57 包。

本包為 55 包之續，不改 55 包原文（R-P200(a)）；55 包 §A 七條照抄，本包四條另抄。

## 0. 分析層之誤（自陳，二項）

1. **R-P358(c) `#325`**：分析層掃描把 `SWE-PM-089` 之 R-P141 留白列
   （`No.# 325`，req_id 有值、其餘全空）判為「缺括號下半、僅 1 步」，
   並寫入條文。**留白列是制度，不是缺陷。** 撤回，見 R-P361。
2. **R-P357 比對鍵**：分析層以 pm_29 之四欄定鍵，pm_29 之 ITD 全為 `NA`，
   故未察覺鍵須含 ITD。現行 corpus 有區辨內容落於 ITD 之型別（44 包後出現），
   四欄鍵會誤刪 14 對真實測項。見 R-P360。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P359] R-P356 於現行 corpus 無標的，本包略過；spec ref 格式問題另列待裁。
         現行 corpus 之 specification_reference 全 283 條為
         `{spec_filename}_{section_id}` 式，無任何 ObjectID；
         R-P356 之標的（整段共用之 6–11 個 ObjectID）無一實例。
         （a）R-P356 記明「於 55 包無標的」，本包不施作，不改條文
         （b）**不**將 R-P356 之意旨自行改適用於 section_id 收斂 ——
              執行層之判斷正確，判準變更不由執行層推定，亦不由本包推定
         （c）另列待裁：現行格式與 IN §10.7(a)「CFTS 母文件 →
              `CFTS{nnn}-{ObjectID}`」之關係 —— feature.yaml 之
              `spec_reference_template` 是否為已裁之 profile override，
              分析層未查；G248 於本包**停用**，待該項裁後另定
         裁決者：分析層（Tier 2，依 B1 §五-1 (i)）。
```

```
[R-P360] R-P357 比對鍵改為五欄；`listed in Input Test Data` 回指須內聯後再比對。
         （a）重複對之比對鍵加入 `Input Test Data`，
              為 Test Item / Pre / ITD / Procedure / ER 五欄逐字
         （b）B1 §五-2 所報 14 對「Procedure 寫 `… the event listed in
              Input Test Data …`、區辨內容落於 ITD」之型別，
              違反 IN §4.5 SWC 基準「步驟不得以『listed in Input Test Data』
              回指該欄」與 R-1 v2「ITD 以 NA 為常態」。
              **此為 pm_29 所無、現行 corpus 新增之缺陷家族，登記為 K。**
              處置：ITD 之值內聯至 Procedure 該步（`Send the signal …` /
              具體事件），ITD 改 `NA`；內聯後該 14 對自然不再逐字相同
         （c）G249 改為：先施作 (b)，再以五欄鍵重跑；
              新增 G251：`listed in Input Test Data` 殘留 **0**、
              ITD 非 `NA` 者須逐列說明其為 IN §4.5 第 3 類獨立資料集
         （d）B1 所報 11 對真重複、req_id 全數不同者 → 依 R-P357(b)
              二列皆留、Remarks 互註；可刪列 0；B6 三代對照表本包無異動
         裁決者：分析層（Tier 2，套用既有 IN §4.5 / R-1 v2，無新判準）。
```

```
[R-P361] R-P358(c) 之 `#325` 撤回；R-P358 其餘各款不變。
         pm_29 `No.# 325` 為 `SWE-PM-089` 之 R-P141 留白列，非缺陷；
         tc_id `-325`（`No.# 326`）括號下半完整、Procedure 2 步，亦非缺陷。
         分析層之誤（§0-1）。R-P358 依 R-P36 原文不改，於 (c) 下加註
         「`#325` 項撤回（R-P361）」。
         R-P358(c) 其餘三項（#9–11、#80、#10）之列號同受 55 包 §0 約束，
         須先在現行 corpus 上以 `(req_id, test_item)` 找到對應物再施作；
         找不到者記「無對應物，略過」。
         裁決者：分析層（Tier 2，撤回自身錯誤）。
```

```
[R-P362] 家族 A 之判準採 `remeasure_55.py` 上界，G245 以之為 lint。
         B1 報二界在現行 corpus 上同為 260，且 G245 期望值為 0，
         界之寬窄不影響目標，取**上界**（併計句中 `… and check that …`）
         以保攔截力。分析層原掃描（290）之判準為
         `^\d+\.\s*Read (the )?(<X>) and check`、<X> 不含 `$`，
         窄於上界且未含 ER 主詞，**以偵測器為準，分析層判準廢**。
         `remeasure_55.py` 之白名單判準即 G245 之實作；兩層同一份程式碼，
         符合 R-P348 之精神（判準不得二源）。
         裁決者：分析層（Tier 2）。
```

## B. 本包須產出（承 55 包 B2–B6，並加）

- B7：家族 K 內聯（R-P360(b)），先於 B5 重複對處理
- B6 改為「無異動，記明」
- R-P358 加註（R-P361）；R-P356 加註「55 包無標的」（R-P359(a)）

## D. 閃點（取代 55 包 §D 對應列）

| # | 項目 | 期望值 |
|---|---|---|
| G245 | 白名單 lint，判準 = `remeasure_55.py` 上界（R-P362） | **0** |
| G246 | 同 55 包 | 同 55 包 |
| G247 | 同 55 包；C3 111 條為主要形態，逐條須落 (b) 或 (c) | **PASS** |
| G248 | **停用**（R-P359(c)） | — |
| G249 | 五欄鍵，於 B7 後重跑（R-P360(c)） | 逐字相同對 **0**；11 對 (b) 型 Remarks 互註 |
| G250 | 同 55 包 | **0** |
| G251 | `listed in Input Test Data` 殘留；ITD 非 `NA` 者有說明（R-P360(c)） | **0** / 全數有說明 |
| G70 | lint 全閘 | 全 PASS |

## E. framework

不動。寫回移至 57 包。

## F. Anomaly 異動

自 A-PW340 起，先查再開：

- 新增：分析層將 R-P141 留白列判為缺陷並立條（R-P361）
- 新增：分析層以 pm_29 四欄定重複鍵，未察 ITD 可載區辨內容（R-P360）
- 新增：現行 corpus 以 `listed in Input Test Data` 回指 ITD，違 IN §4.5，家族 K（R-P360(b)）
- 新增：C3 自 72 惡化至 111，`TLM_Status.Info and $Telematic_Power$ read "…"` 為現行主要前置形態（B1 §六）

## G. DATA_REQUESTS

不變。DR-PW26 起號。

## H. 作業指示

1. 抄 R-P359–R-P362 入 RULINGS.md；R-P356 / R-P358 加註；§F 入 ANOMALIES.md
2. 續 55 包 §H 第 4 步（B2 片段表）起
3. B7 家族 K 內聯，驗 G251
4. B5 機器改寫，驗 G245–G247、G249、G250
5. 以本包 §D 全表自驗
6. 上繳 `features/power/docs/upstream/56_b1_rulings.md`（含 55 包全部產出）

## I. 禁區

沿用 55 包 §I，另增列：

- 不得將 R-P356 自行改適用於 section_id（R-P359(b)）
- 不得依 pm_29 四欄鍵刪任何列（R-P360）
- 不得對 `No.# 325` 留白列施作（R-P361）
- 不得以分析層之 290 判準另寫 lint（R-P362）

## J. 本包產生之新條文清單（自檢）

1. R-P359 R-P356 無標的略過；G248 停用；格式問題待裁
2. R-P360 五欄鍵；家族 K 內聯；G251
3. R-P361 `#325` 撤回
4. R-P362 家族 A 判準採偵測器上界

四條，四個頂層 fenced block，§H 第 1 步四條，一致。

**R-P348 相容性（C(4,2) = 6 對）**：
R-P359×R-P360：無共用產物（spec ref vs 重複鍵）；
R-P359×R-P361 / R-P359×R-P362：無交集；
R-P360×R-P361：R-P361 撤回列非重複對成員，無交集；
R-P360×R-P362：B7 內聯後之 Procedure 亦受 G245 掃描，內聯之 `Send the signal $…$` 為白名單 (i)，有解；
R-P361×R-P362：無交集。**六對無互斥。**

## K. 待 Pei 裁（二項，非阻本包）

1. **spec ref 格式**：現行 `{spec_filename}_{section_id}` 對 CFTS 母文件，
   與 IN §10.7(a) 不符 —— 是既裁 override 或未察之偏差？裁後定 G248 去留。
2. **PENDING 對 S6**：R-P353 / R-P355(c) 施作後 I 家族必自 0 回升，
   S6「含 PENDING 不得出貨」與之衝突。**須於 57 包（寫回）前裁**：
   降轉 NA 之條件，或寫回時 PENDING 列之處置。

## L. 分析層自判

**有，一項。** C3 之 111 條為現行主要形態，R-P354×R-P355 之「有解」
係指落 `PENDING: DR-PW23`；若 DR-PW23 附表多數查無對照，
本包施作結果將是**逾百條 PENDING** —— 與 §K-2 直接相連。
分析層未預估該比例，據實記明。
