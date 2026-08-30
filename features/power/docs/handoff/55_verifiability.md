# 55 — 站③ 可驗證性整改（配方先行）

下放包 | 分析層 → 執行層 | 往返 NN = 55

前置：54 包上繳已覆核，§D 全表 PASS，**ACCEPT**。
本包由 Pei 站③ 審閱 `pm_29`（delivered，SHA `35305835…`；Pei 上傳之
`…PowerManagement_20260824.xlsx` 與之五欄逐字一致，390 資料列）觸發。
**54 包 §E「55 包即寫回」由本包取代** —— 寫回順延至本包完成後（R-P352）。
裁決者 Pei，逐字依據：「都裁 1. 是 2. 可 3.但只要SWRA ID不同就不可以合併 4.不用 5.允許」。

盤點全文：`features/power/docs/handoff/55_review_findings.md`（本包附件，同批落檔）。

沿用不變之節：`§C 抽取規格` 同 02 包；`§I 禁區` 沿用 54 包 §I，另增列見本包 §I。

## 0. 分析層之誤（自陳）

本包盤點之列數統計全部量自 `pm_29`（390 列）。
54 包上繳載「283 條 / 284 列」寫入 dry-run —— **二者何者為 Revise2 之基底，
分析層未查明即立條**。§H 第 2 步令執行層先回報現行 corpus 列數與其與 `pm_29`
之對應，本包各家族列號**須在該 corpus 上重量**（R-DD26 verify before act），
不得沿用附件之列號直接施作。此為「未重量即移用結論」之既知錯誤形態，據實記明。

## A. 本包裁決條文（逐字，抄入 RULINGS.md）

```
[R-P352] 站③ 審閱成立；整改採「先立配方，後機器改寫，最後人審」，寫回順延。
         Pei 站③ 審閱 pm_29，判定 390 列中 290 列（74%）之驗證步驟目標
         非可觀察量，屬結構性缺陷，根因為 `Read the <X> and check that it is <Y>`
         模板將規格名詞（functionality / state / reaction / behavior）填入 <X>，
         ER 同義反覆，判斷實際推回測試員（IN §5.1 defer judgement 之變形）。
         處置：不逐列手修。依 R-P353–R-P358 立配方，執行層機器改寫，
         再進站④ 人審。54 包 §E「55 包即寫回」作廢，寫回順延至本包
         G245–G250 全數 PASS 後之次包。
         裁決者 Pei，逐字依據：「1. 是」。
```

```
[R-P353] 可觀察目標白名單；`functionality (not) available` 由分析／執行層指定代理量。
         Procedure 之 `Read <X>` / `Check that <X> …` 與 ER 之主詞 <X>，
         **限四類**：
         （i）`$MESSAGE.Signal$`（R-1 v3 (a)）
         （ii）具名 UI 元件，以 `"..."` 標示（IN §11），如 `"Splash Screen"`、
               `"Chrysler App icon"`、`"FOTA update available"` pop-up
         （iii）可量測音訊：source indicator 顯示值、`AUD_LVL` 值、指定揚聲器
               有／無輸出
         （iv）log / trace 之具名行或具名計數器
         其餘（`functionality`、`reaction`、`behavior`、`network state`、
         `HU mode`、`screen sequence`、`main CPU`、`CAN micro` 等）**一律不得作 <X>**。

         **代理量指定（Pei 裁：允許）**：`<功能> functionality is (not) available`
         型（pm_29 計 38 列）及其他非白名單 <X>，由執行層為每一功能指定
         **一個**白名單類代理量，**須引 CFTS009 / SYS1 中載明該功能可觀察面之
         錨點**（ObjectID 或章節）；查無錨點者不得自造，改登 DR。
         代理量表落於 `data/observable_proxy_55.md`，格式：
         `<原 X> | <代理量（白名單類別）> | <錨點> | <影響列>`，
         分析層於上繳覆核時逐條核對錨點。
         `Read the HU mode and check that it is <STATE>`（pm_29 計 15 列）
         一律改為 `$STATUS_TELEMATIC.PowerSts_Telematic$ = <raw> (<label>)`。
         `proper` / `as defined (per HMI)` / `normal` 不得出現於 Procedure 與 ER；
         改為具名畫面／具名值並引錨點，查無定義者 `PENDING: DR-{n}`。
         裁決者 Pei，逐字依據：「5. 允許」。
```

```
[R-P354] `ENTER_<STATE>` 標準片段表；來源得併用 CFTS009 與 SYS1 HMI spec。
         Pre-Condition `The HU is in <State> state`（pm_29 計 226 列）
         其進入路徑全案無定義。依 IN §5.3 常數制，為每一 HU 電源狀態建立
         `ENTER_<STATE>`：`Full-Operation` / `Timed` / `Idle` / `Standby` /
         `Partial_Operation` / `Sleep` / `Bench` / `INIT`。
         （a）內容 = 自起始態之 `$STATUS_BH_BCM1.OperationalModeSts$` 序列
              （及其他必要觸發訊號）＋ 確認步
              `Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check
              that it is <raw> (<label>)`；每一片段須引其轉移條文之錨點
         （b）來源：CFTS009 為主，**SYS1 HMI spec 得併用**（Pei 裁：可）；
              二者衝突時 CFTS 勝，並登 DR
         （c）狀態名以 DBC `VAL_` 標籤為唯一拼法（R-7）；
              `FULL OPERATION` / `IDLE` / `Partial Operation` 等變體全案改齊
         （d）`The HU is in an operative state`（25 列）、`a … state`（3 列）
              須逐列改為具體狀態；改不出者登 DR
         （e）`BODY ON` / `BODY OFF-TIMED` 為車輛模式，非 HU 態；
              須依 spec 對照改為對應 HU 態，並保留原車輛模式於 Remarks
         （f）片段之套用方式：Pre-Condition 保留
              `The HU is in <State> state`，Procedure 第 1 步改為
              `Apply ENTER_<STATE>`，其 ER 為該片段之確認值；
              抽象動詞 `Bring the HU to` / `Let the HU enter` /
              `Bring the HU through the switch on sequence`（pm_29 計 69 列）
              同以片段取代
         片段表落於 `data/enter_state_55.md`，同步登入 lint 常數表。
         裁決者 Pei，逐字依據：「2. 可」。
```

```
[R-P355] 內部訊號不得直接 Set；DR-PW23 擴大為 PM 內部訊號對照總表。
         `Set <X>.Info to <v>` / `Set <X>.Req to <v>`（pm_29 計 40 列）
         及以 `.Info` / `.Req` / `RemStartFail` 作 Pre-Condition（66 列），
         其對象為 HU 內部變數，測試台無法直接寫入或讀出。
         （a）DR-PW23 擴大：列出全案出現之每一內部訊號名，
              逐一向上游索取**驅動方法**與**觀察方法**；
              落於 `DATA_REQUESTS.md` DR-PW23 條下之附表
         （b）已有 DBC 對照者，依 R-1 v3 (d) 改為 `$MESSAGE.Signal$`
         （c）尚無者，Procedure 該步改 `PENDING: DR-PW23 <訊號名>`，
              ER 同；**不得以 `Set X.Info` 假裝可執行**
         （d）`Let the bench place an incoming phone call` 等外部動作
              改為具體操作（如 `Place a call from the paired phone to the HU`），
              不屬本條，屬 R-P354(f)
         裁決者 Pei，逐字依據：「都裁」。
```

```
[R-P356] `Specification Reference` 收斂至直接驗證之 ObjectID。
         pm_29 計 100 列每列引 6–11 個 ObjectID 且整段共用同組
         （#1–43、#52–67 等）。IN §10.7 要求列出 TC **直接驗證**之章節。
         每列僅保留其 `test_item` 括號下半所對應之 ObjectID（通常 1–2 個），
         由執行層依 037 SWRA 逐列對回；對不回者登 DR，不得保留整組。
         DR-PW6 所阻斷之 `SWE-PM-001`–`009` 依其 DR 狀態處理，不因本條解阻。
         裁決者 Pei，逐字依據：「都裁」。
```

```
[R-P357] 重複對之去留：同 Req ID 刪後者；SWRA ID 不同者不得合併。
         pm_29 四欄逐字相同之重複對 12 對：
         (126,129) (212,354) (213,355) (214,356) (215,357) (216,358)
         (217,359) (218,347) (250,389) (255,390) (305,320) (306,321)。
         （a）`Requirement or Design ID` 相同 → 刪列號較大者
         （b）`Requirement or Design ID` 不同 → **二列皆保留，不得合併**
              （Pei 裁：只要 SWRA ID 不同就不可以合併）；
              其為同一 TC 掛雙需求之事實，於二列 Remarks 互註對方 tc_id
         刪除者入三代對照表（R-P349(c) 同批），tc_id 不重編。
         裁決者 Pei，逐字依據：「3.但只要SWRA ID不同就不可以合併」。
```

```
[R-P358] `LIN and CAN tool is available on HU` 保留；步驟控制狀態移出 Pre-Condition；零星項同批修。
         （a）`LIN and CAN tool is available on HU` **保留**，不刪
              （Pei 裁：不用）
         （b）步驟控制狀態（`The previous internal state was …`、
              `held a known value before the disconnection`、
              `The boot of the HU is not ended`、
              `The disclaimer screen has not yet been shown`、
              `has already played the startup sound`；pm_29 計 16 列）
              依 IN §4.4 移入 Procedure 為 Setup 步，附 ER 證明條件成立
         （c）零星項：#325 補括號下半與第 2 步；#9–11 前置只留該列所測之
              來源，`An active phone call is available` 自 #9/#10 移除；
              #80 Test Item 之 AMP/ICS/DTV OFF 須有對應觀察步；
              #10 `Select BT Music streaming` 補 UI 路徑或引錨點
         裁決者 Pei，逐字依據：「4.不用」。
```

## B. 本包須產出

### B1. 基底確認（§0）—— **最優先，未回報前不得施作**
回報現行 corpus 之路徑、列數、與 `pm_29` 390 列之對應關係；
附件列號在該 corpus 上重量，產出 `data/findings_remeasure_55.tsv`
（`family | pm_29_rows | current_rows | delta`）。

### B2. `ENTER_<STATE>` 片段表（R-P354）
`data/enter_state_55.md`，八態，每態附錨點；lint 常數表同步。

### B3. 可觀察代理量表（R-P353）
`data/observable_proxy_55.md`，覆蓋全數非白名單 <X>；每條附錨點；
查無錨點者開 DR（先查現行最大號並回報，現行 DR-PW25）。

### B4. DR-PW23 附表（R-P355(a)）
全案內部訊號名清單，逐一標 `已對照 / PENDING`。

### B5. 機器改寫
依 B2–B4 改寫 Procedure / ER / Pre-Condition；R-P356 收斂 spec ref；
R-P357 處理重複對；R-P358 零星項。產出 `sandbox/b55/pm_55.xlsx`。

### B6. 三代對照表更新（R-P357 刪列）

## D. 閃點

G0 為前置閘。

| # | 項目 | 期望值 |
|---|---|---|
| G245 | 白名單 lint（R-P353）：`Read <X>` / ER 主詞非四類者 | **0** |
| G246 | 狀態前置解析（R-P354）：`The HU is in <State>` 之 <State> ∈ 八態且 Procedure 首步為 `Apply ENTER_<STATE>` | **100%**；`operative` / `a … state` 殘留 **0** |
| G247 | 內部訊號（R-P355）：`Set <X>.Info/.Req` 殘留 **0**；每一內部訊號名在 DR-PW23 附表有列 | **PASS** |
| G248 | spec ref（R-P356）：每列 ObjectID 數 ≤ 括號下半對應數；整段共用組殘留 **0** | **PASS** |
| G249 | 重複對（R-P357）：四欄逐字相同對 **0**；(b) 型保留列 Remarks 互註 | **PASS** |
| G250 | `proper` / `as defined` / `normal` / `Read the HU mode` 殘留 | **0** |
| G70 | lint 全閘 | 全 PASS |

## E. framework

§E 已定版（R-P35），本包不動。寫回移至 56 包，條件同 54 包 §E。

## F. Anomaly 異動

開新號前先查現行最大號並回報（54 包上繳至 A-PW339）。

- 新增：`Read the <X>` 模板將規格名詞填入 <X>，290 列（R-P352）
- 新增：HU 電源狀態作前置而全案無進入配方，226 列（R-P354）
- 新增：內部訊號 `.Info/.Req` 直接 Set，40 列（R-P355）
- 新增：spec ref 整段共用同組，100 列（R-P356）
- 新增：分析層立條前未查明 Revise2 基底（283 vs 390）（本包 §0）

## G. DATA_REQUESTS

DR-PW23 擴大（R-P355(a)）。B3 可能新開 DR，號自 DR-PW26 起，**先查再開**。
其餘 DR 狀態不變。

## H. 作業指示

1. G0 前置閘
2. **B1 基底確認並回報**；待分析層覆核 `findings_remeasure_55.tsv` 後始進 3
3. 查 A-PW / DR-PW 現行最大號並回報
4. B2 片段表，驗 G246 之可解析性（乾跑）
5. B3 代理量表；B4 DR-PW23 附表
6. B5 機器改寫，驗 G245–G250
7. B6 三代對照表更新
8. 以 §D 全表自驗
9. 抄錄前重驗 §J（R-P200(c)）；§A 七條逐字抄入 RULINGS.md；§F 入 ANOMALIES.md
10. 上繳 `features/power/docs/upstream/55_verifiability.md`，更新 `docs/INDEX.md`

## I. 禁區

沿用 54 包 §I 全部條目（**「不得寫回」續有效**），另增列：

- 未完成 B1 回報前**不得**依附件列號施作（§0）
- 不得為 `functionality` 自造代理量而不引錨點（R-P353）
- 不得以 `Set <X>.Info` 表示可執行步驟（R-P355(c)）
- 不得合併 SWRA ID 不同之重複對（R-P357(b)）
- 不得刪 `LIN and CAN tool is available on HU`（R-P358(a)）
- 不得改動 `test_item` 上半 verbatim（R-P343 / R-P347 續有效）

## J. 本包產生之新條文清單（自檢）

1. R-P352 站③ 審閱成立；配方先行；寫回順延
2. R-P353 可觀察目標白名單；代理量指定
3. R-P354 `ENTER_<STATE>` 片段表；CFTS009 + SYS1
4. R-P355 內部訊號不得直接 Set；DR-PW23 擴大
5. R-P356 spec ref 收斂
6. R-P357 重複對去留
7. R-P358 LIN/CAN 保留；步驟控制狀態移出；零星項

逐條確認：**七條**，皆為獨立頂層 fenced block。
自檢：§A 區塊數 = 7、§J 列數 = 7、§H 步驟 9 寫「七條」，三處一致。

**R-P348 相容性檢查（C(7,2) = 21 對）**，取極端案例問「有無同時滿足之解」：
- R-P353 × R-P354：一列同時有非白名單 <X> 與狀態前置 → 首步 `Apply ENTER_<STATE>`、末步用代理量，有解
- R-P353 × R-P355：內部訊號既非白名單亦不得 Set → 二者皆指向 `PENDING: DR-PW23`，同解
- R-P354 × R-P355：`ENTER_<STATE>` 序列若須驅動內部訊號 → (a) 要求引錨點，錨點只用 CAN 訊號，有解；若 CFTS 只給內部訊號則落 PENDING，仍有解
- R-P354 × R-P358(b)：`The boot of the HU is not ended` 移入 Procedure 後與 `Apply ENTER_STANDBY` 之次序 → 先 ENTER 後 Setup 步，有解
- R-P356 × R-P357(b)：保留之雙列 spec ref 各自收斂，互不影響，有解
- R-P357 × R-P358(c)：#325 非重複對成員，無交集
- R-P352 × 其餘六條：R-P352 為流程條文，無共用要件
- R-P353 × R-P356/357/358、R-P354 × R-P356/357、R-P355 × R-P356/357/358、R-P356 × R-P358、R-P357 × R-P358(a)(b)：無共用產物欄位或共用者互不約束
**21 對皆有解，無互斥。**

**本包下放後分析層不再修改**（R-P200(a)）。

## K. 分析層自判：本包是否仍有該驗而未驗者

**有，三項。**

1. **基底未查明**（§0）—— 本包七條之列數依據皆為 `pm_29`，
   若現行 corpus 為 283 列，其中部分缺陷可能已於 51–54 包消失或形態改變。
   已以 B1 作為前置閘擋住施作，但條文本身之數字未待重量即寫入。
2. **R-P353 之代理量指定將 38 列之判準交由執行層＋錨點**，
   分析層僅於上繳覆核錨點，**未預先查 CFTS009 是否確有各功能之可觀察面**；
   若多數查無，B3 將大量落 DR，整改效益打折。
3. **R-P354 之八態片段須自 CFTS009 轉移條文抽取**，
   而 RULINGS 待裁區載 `SWE-PM-008`（Logistic 三態）受 DR-PW11 阻斷、
   `SWE-PM-001`–`009` 受 DR-PW6 阻斷 —— **`INIT` / `Bench` 之進入條文
   是否落在受阻 leaf 內，分析層未查**。若是，該二片段亦須 PENDING。
