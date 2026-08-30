# 57 — B2/B4/B7 回報覆核與五項裁示

下放包 | 分析層 → 執行層 | 往返 NN = 57

前置：`data/55_b2_b4_b7_report.md` 已覆核，判定 **ACCEPT**。
執行層停在 B3/B5 前不施作、不以未定判準改寫 283 條 —— **處置正確**。
56 包 §E「寫回移至 57 包」由本包取代，寫回移至 58 包，**且受 §K-1 阻斷**。

## 0. 分析層之誤（自陳，二項）

1. **R-P354 與 canon R-7 互斥**（A-PW350）：八態自 pm_29 之前置拼法抄來，未對 DBC `VAL_` 核對，
   同條 (c) 又令以 `VAL_` 為唯一拼法 —— 自相矛盾。R-P348 之相容性檢查只查新條彼此，
   未查新條對既有 canon，**該檢查有結構性盲區**，見 R-P364。
2. **R-P360(b) 之規模估計失準一個數量級**（14 對 → 158 條）：條文所依為重複對之誤判樣本，
   未先全量掃 ITD 非 `NA` 之列數。IN §8.4.1「量測先於斷言」再次違反。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P363] R-P354 之狀態集與拼法改依 DBC `VAL_ 1470`；`INIT` 為規格態，保留原名並 PENDING。
         （a）`ENTER_<STATE>` 之 <STATE> 集合 = `VAL_ 1470` 之列舉值，
              拼法逐字取 `VAL_`（`Full_Operation`，非 `Full-Operation`）；
              R-P354 條文中之 `Full-Operation` 等拼法全部依此更正，
              R-P354 依 R-P36 原文不改，於 (c) 下加註指向本條
         （b）`Logistic_On`（raw 5）列入片段集，`ENTER_LOGISTIC_ON` 自附錄移入正表；
              惟其 TC 產出仍受 R-P349(a) / DR-PW11 阻斷，片段可立、TC 不產
         （c）`INIT` 不在 `VAL_` —— 依 R-13 精神，規格原文所載之狀態名**保留**，
              `ENTER_INIT` 標 `PENDING: DR-PW26 INIT 觀察量`；不得以 `VAL_` 內
              語意相近之值代入
         （d）`ENTER_SLEEP` 同標 `PENDING: DR-PW26 Sleep 觀察方法`；
              「CAN 睡眠後無法以 CAN 讀確認值」之事實寫入片段備註，
              待 DR-PW26 回覆是否有非 CAN 觀察面（電流／LIN／log）
         DR-PW26（High）之四問**核可**，維持「阻斷 G246，不阻斷其餘六片段」。
         裁決者：分析層（Tier 2，訂正自身條文以合 canon R-7）。
```

```
[R-P364] R-P348 增 (d)：新條文須對既有 canon 逐條查相容，不僅查新條彼此。
         A-PW350 為首例：R-P354(c) 引 R-7 而 R-P354 本文違 R-7，
         C(7,2) 之 21 對檢查全數「有解」而未攔。
         增訂：分析層於 §J 之相容性檢查，除新條兩兩配對外，
         **須列出每一新條所引用或觸及之既有 canon 條（IN §、R-、R-P-）**，
         逐條問「新條之極端案例是否違該 canon」；引用而未查者視同未檢。
         R-P348 依 R-P36 原文不改，加註指向本條。
         裁決者：分析層（Tier 2，作業規則）。
```

```
[R-P365] G246 改寫；G0 台帳納入判準所依之 DBC 並定版本凍結。
         （a）G246 期望值改為：「可用片段（非 PENDING 者）100% 解析
              ＋ PENDING 片段逐條掛 DR-PW26 且其所涉列以
              `PENDING: DR-PW26 <態>` 佔位」。不以降判準求綠（R-P187），
              改以「可達之部分全達、不可達之部分全數可追溯」為判準
         （b）`features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc`
              （SHA `9ef1ec98…`）納入 power 之 G0 台帳，G0 改 **10 / 10**；
              登記其為自 20 包（DR-PW21）起之判準來源，**遲登**據實記明（A-PW349）
         （c）版本凍結規則：台帳登記路徑＋SHA；SHA 不符即 G0 FAIL；
              換版須開 DR 或裁定，並重跑所有引 `VAL_` 之閘（G245 / G246）
         （d）該檔位於他 feature 目錄 —— 是否複製入 `features/power/inputs/`
              以去除跨 feature 依賴，列 §K 待 Pei
         裁決者：分析層（Tier 2）。
```

```
[R-P366] R-P360(b) 之適用範圍依執行層三分法；15 條逾長者不得為湊字數而截斷資料。
         家族 K 實測 158 / 283。
         （a）單行 ITD ≤ 60 字元（135 條）：內聯至 Procedure 該步，ITD 改 `NA`
         （b）單行 ITD > 60 字元（15 條）：逐條檢。內聯後末步逾 §5.2B 18 字者，
              **不得刪減資料以合字數**；改為拆步（資料送出步 ＋ 驗證步）
              或依 (c) 保留於 ITD 並說明。字數上限與資料完整性衝突時，資料完整性勝
         （c）多行 ITD（8 條）：保留於 ITD，逐列於 Remarks 說明其為
              IN §4.5 第 3 類獨立資料集；Procedure 該步改為具體引用
              （`Send each signal value listed in Input Test Data in turn`
              仍屬回指，不許；須寫明資料集之性質，如
              `Send the boundary values of $X$ one at a time`）
         G251 之判準隨之：`listed in Input Test Data` 殘留 0；
         ITD 非 `NA` 者 = (b)(c) 之保留列且 Remarks 有說明。
         R-P360 依 R-P36 原文不改，加註指向本條；
         規模估計失準登 A-PW（§F）。
         裁決者：分析層（Tier 2，適用 R-P360(c) 既留之例外）。
```

```
[R-P367] B3 代理量之錨點來源 = power 之 G0 台帳所列文件，不限 CFTS009。
         本 feature `sys1_export: null`，R-P353 / R-P354(b) 之「SYS1」在本 feature 為空集，
         二條於此**不改文，記明無適用對象**。
         代理量錨點得取自 G0 台帳（10 / 10）內任一文件：CFTS009、SYS3、
         WrapperResource 二份、DBC（`VAL_` 標籤本身即為錨點）等；
         台帳外文件一律不得為錨。查無錨點者登 DR，不得自造（R-P353 不變）。
         B3 施作前先出**可及性報告**：260 條非白名單 <X> 按「原 X」去重後之相異名數，
         逐名標「台帳內有錨 / 無錨」，分析層覆核後再填代理量表。
         裁決者：分析層（Tier 2）。
```

## B. 本包須產出

- B2 修正：片段表依 R-P363 重排（`VAL_` 拼法、`ENTER_LOGISTIC_ON` 入正表、INIT/SLEEP PENDING）
- B3 前置：可及性報告 `data/proxy_reachability_55.md`（R-P367），**覆核後**再出代理量表
- B7：依 R-P366 三分法施作，出 `data/family_k_disposition_55.tsv`（tc_id | 類別 | 處置 | 字數）
- G0 台帳更新（R-P365(b)(c)）
- **B5 仍不施作**，待 B3 覆核與 §K-1 裁後

## D. 閃點

| # | 項目 | 期望值 |
|---|---|---|
| G0 | 台帳 | **10 / 10**，含 DBC SHA |
| G246 | 依 R-P365(a) | 可用片段 100%；PENDING 片段逐條掛 DR-PW26 |
| G251 | 依 R-P366 | `listed in Input Test Data` 殘留 0；保留列皆有 Remarks 說明 |
| G252（新） | 可及性報告 | 260 條之相異 <X> 全數標記；無錨者有 DR 號 |
| 其餘 | 同 56 包 | 同 56 包 |

## F. Anomaly 異動

自 A-PW352 起，先查再開：

- 新增：R-P348 相容性檢查不涵蓋新條對既有 canon（R-P364）
- 新增：R-P360(b) 規模估計失準一個數量級，未先全量掃 ITD（R-P366）
- 新增：R-P353 / R-P354(b) 引 SYS1 而本 feature 無 SYS1，分析層未查 feature.yaml（R-P367）
- 素材拼法不一致（`Phone_Call.Info`/`PhoneCall.Info`、`SwitchOff_Timeout_Setting.Req`/`SwitchOffSetting.Req`）：非執行層所生，已入 DR-PW23，**登 A-PW 供追溯，不改素材**

## G. DATA_REQUESTS

DR-PW26 核可（High）。DR-PW23 附表已掛。無新增。

## H. 作業指示

1. 抄 R-P363–R-P367；R-P348 / R-P354 / R-P360 加註；§F 入 ANOMALIES.md
2. G0 台帳更新，重跑 G0
3. B2 修正
4. B3 可及性報告 → **停，待覆核**
5. B7 依 R-P366 施作，驗 G251
6. 上繳 `features/power/docs/upstream/57_b2b4b7_rulings.md`

## I. 禁區

沿用 56 包 §I，另增列：
- 不得以 `VAL_` 內近義值代 `INIT`（R-P363(c)）
- 不得為合 18 字而刪減內聯資料（R-P366(b)）
- 不得以台帳外文件為代理量錨點（R-P367）
- 可及性報告未覆核前不得填代理量表

## J. 自檢

五條，五個頂層 fenced block，§H 第 1 步五條，一致。

**新條彼此 C(5,2) = 10 對**：
R-P363×R-P365：G246 之 PENDING 片段即 R-P363(c)(d) 所定，同解；
R-P363×R-P367：`VAL_` 標籤為錨點，DBC 入台帳後方合 R-P367，順序 = R-P365(b) 先於 B3，有解；
R-P365×R-P367：台帳擴至 10/10 後 R-P367 之範圍隨之，一致；
R-P366×R-P367：內聯之 `$X$` 須在 DBC，DBC 在台帳，有解；
其餘六對無共用產物。

**依 R-P364(d) 對既有 canon**：
R-P363 對 R-7（DBC 為準）— 合；對 R-13（規格名保留）— 合，INIT 適用；對 R-P349(a) — 合，(b) 明示 TC 不產。
R-P365 對 R-P187（不降判準）— (a) 非降判準，為改寫可達性；對 R-P327（素材層重跑）— 台帳變動須重跑，已列 §H 2。
R-P366 對 IN §5.2B（18 字）— (b) 明示衝突時資料完整性勝，**此為對 canon 之例外，非違反**，記明；對 IN §4.5 — 合。
R-P367 對 R-P353 / R-P354(b) — 記明 SYS1 為空集，不改文。
R-P364 對 R-P348 — 為其增補。
**無違反；一項例外（R-P366(b) 對 §5.2B）已明示。**

## K. 待 Pei 裁（二項）

1. **PENDING 105 / 283（37.1%）對 S6** —— DR-PW23 未結則寫回不可能成立。
   甲：等 DR-PW23 回覆，寫回無期限順延
   乙：分兩段寫回 —— 無 PENDING 之 178 條先寫回交付，105 條列「待上游資料」附清單，
       工作簿留 `PENDING: DR-PW23 <名>` 原樣（等於對 S6 開例外，須你明文裁）
   丙：由你逐名審 13 個內部訊號，可裁定為「測試台可觀察」者降轉具體步驟，餘者依甲
2. R-P365(d)：DBC 是否複製入 `features/power/inputs/` 去除跨 feature 依賴

## L. 分析層自判

**有，一項。** 本包五條仍未經施作驗證，R-P366(b) 之「拆步」與 (c) 之「寫明資料集性質」
皆為措辭級指示，執行層施作後可能再出現本包未預見之形態（如拆步後 Procedure 逾 ER 1:1 對齊）。
據實記明，不預估。
