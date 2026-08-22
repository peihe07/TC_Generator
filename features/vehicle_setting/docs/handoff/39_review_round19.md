# 39 下放包 — 19 輪覆核：缺件之系統性、類別式 DR、20 輪指令

分析層寫入，2026-08-22。對象：19 輪之回報、`batch01_v3.json`、`batch02.json`。

**覆核結論：接受。** batch01_v3 零違規、8 條；batch02 十選六且四條**未撰寫**。
**「四條一律未撰寫，寫了就是造值」是正確的處置** —— 與 batch01
「已寫後移出」分開記，兩種狀態確實不同。

---

## 1. 本輪最重要的不是那四條，是那句話

> **IGN_RUN 能用不是因為我推出來的，是因為 CFTS044 在 5 個地方自己寫了 `4h`。
> 沒有那個 `4h`，IGN_RUN 跟 IGN_START 的處境一模一樣。**

`IGN_START` → `START`、`IGN_OFF_ACC` → `ACC` 這兩個調和**看起來極其顯然**，
而顯然正是 §8.4.1 最容易被跨過的地方。**未跨，且說明了為何另一個可以。**

同理 R-VS36 三形態試法第二次奏效：只試 `$X$` 則 `-028` 會被判為可寫，
**寫出一個觸發訊號根本不存在的 TC**。

---

## 2. 缺件之系統性 —— 先量洞的大小，再繼續生成

| 輪 | 批次 | 可寫 | 阻塞 |
|---|---|---:|---:|
| 18 | batch01 | 10 | 0（當時未知） |
| 18→19 | batch01_v3 | 8 | 2 |
| 19 | batch02 | 6 | 4 |

**累計 6 條 TC 阻塞，分屬 5 個 DR，而母體還有 227 個 leaf 未觸及。**

執行層具名兩個未量之維度：

1. CFTS044 對外部 HMI 文件之引用**慣於不具名**（`4858560`「HMI requirements」、
   `4859032`「HMI Logic & Flow」）——「全文還有幾條同型我沒數，
   **這直接決定後面還會卡幾條**」
2. `spec_variables.tsv` 之 30 個 token 係以 `$var$` 形態建立，
   **裸名 token 會漏**（A-VS64 已證）

**兩者皆滿足 R-VS40 之解凍條件 (b)（阻塞具體 leaf）。分析層逕予解凍。**

```
W-58（全量可寫性掃描，20 輪唯一作業）
對 237 個 Functional leaf 之來源條文，一次掃出全部阻塞因子，
產出 `docs/reports/writability.tsv`：

  leaf_id / reqid_list / layer3 / writable(yes|no) /
  blocker_class / blocker_detail / dr_id

`blocker_class` 之四類（**掃描條件須逐類具名**）：

  B1 未具名之外部交叉參照
     形態：`as defined by`／`refer to`／`follow the`／`per the`
           ＋ 未帶文件名或章節號者
     已知實例：4858560、4859032
  B2 規格值於 LID 與 DBC 皆無對應
     以 R-VS39 之正規化鍵比對；**須含裸名 token**（R-VS36 三形態）
     已知實例：EngRun_Stat 四值、IGN_START、IGN_OFF_ACC
  B3 PROXI／參數於 LID 三處皆無命中
     已知實例：VC_HdRstPrsnt
  B4 其他（逐條具名，不得歸「其他」而不述）

並列出**分母**：237 leaf 中 writable = yes 者幾條。
**該數是本 feature 之實際可交付量**，此前未曾量過。

配套：`spec_variables.tsv` 以 R-VS36 三形態重建 token 全集，
列「原 30 個」與「重建後 N 個」兩數，新增者逐一具名。
```

**先量再生成之理由**：現行節奏為每批撞一次牆，而每次撞牆產生一個新 DR、
一輪往返。若 B1／B2／B3 之總量為數十條，逐批發現將耗數十輪；
一次掃出則**一次送、一次覆**。

---

## 3. R-VS42 —— 類別式 DR（本輪唯一新條文）

```
R-VS42（分析層裁定 2026-08-22）
同一形態之缺件，**以類別開一個 DR，不逐實例開**。

DR 之本文結構：
  (1) 形態之描述（我方如何判定其為同一類）
  (2) 已知實例之完整清單（reqid ＋ 逐字節錄 ＋ 受影響 leaf）
  (3) 我方之掃描條件與其盲區
  (4) 影響範圍（leaf 數）

已開之逐實例 DR，於其類別 DR 開立時**併入之**，
原編號保留並註「併入 DR-{n}」（R-TM13）。

理由：逐實例開 DR 使上游收到 N 封同型提問，
其回覆亦將逐封而來，我方每收一封解一條 TC。
類別式一次問清，一次覆蓋全部實例。
本 feature 已因此形態累計 5 個 DR 覆蓋 6 條 TC。
```

**依本條，DR-21／22／23 改為類別式**，其實例清單待 W-58 補全：

| 新 DR | 類別 | 併入 |
|---|---|---|
| **DR-21** | 規格值於 LID／DBC 皆無對應（B2） | DR-19（EngRun_Stat 四值）併入 |
| **DR-22** | PROXI／參數於 LID 無對應（B3） | — |
| **DR-23** | 未具名之外部交叉參照（B1） | **DR-20**（4858560）併入 |

**DR-19／DR-20 已於 2026-08-22 送出**，故其併入之處置為：
不撤回已送者，於 DR-21／23 之本文註明
「本類別包含已於 2026-08-22 單獨送出之 DR-19／DR-20，其為本類之實例」。

---

## 4. 登記簿之一項不一致（R-VS35 之形態）

執行層記：「第 7、8 項在登記簿裡沒有 DR 編號」。

**37 包 §2 之第 7、8 項為 DR-8（`$VC_VEH_LINE$` 車型碼）與
DR-12（`IGN_OFF_ACC`）**，二者於 00G §5 與 29 包 §1.2 開立，
**但似未寫入 `DATA_REQUESTS.md`**。

→ **A-VS66**：分析層於下放包開立之 DR，未逐筆確認其入登記簿。
R-VS35 所立之核對機制**只覆蓋執行層側**，未覆蓋分析層側。

```
分析層裁定 2026-08-22（R-VS35 之補充，不另編號）
分析層於下放包開立之 DR／anomaly，須於**次輪之下放包**列
「上輪開立 N 筆／登記簿現有 M 筆」兩數，差額非 0 即補。
本輪即補：DR-8、DR-12 應入 `DATA_REQUESTS.md`；
**DR-12 依 R-VS42 併入 DR-21**（其為 `IGN_OFF_ACC` 之實例，同 B2 類）。
```

---

## 5. 其餘

| 項 | 評述 |
|---|---|
| `-009` 之 design_method 改 Equivalence Partitioning | **正確**。§12 之「Input partitioned valid / invalid」——LHD／RHD 為配置參數之兩個等價類，且斷言其輸出相同 |
| batch02 之 sibling 比對 | **正確**。11 列互為 sibling、無 `duplicate_of`、與 `-025` 不重複（`-025` 驗致動，本批驗可及性與可選性）——**此為 §4.6 首次實質運作** |
| P5 記 `pilot batch 01, verdict PASS (Pei, 2026-08-22)` | 已記 |
| DR 送出照實記 5 項、未推定 | **正確** |

---

## 6. 20 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md
  docs/runtime/ASPICE_SWE6_AI_Instruction.md
  docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md
  features/vehicle_setting/RULINGS.md
  features/vehicle_setting/docs/handoff/39_review_round19.md   ← 本輪依據

## 文書

D-1  依 R-VS18 建 docs/upstream/17_writability.md，六節先留空。
D-2  逐字轉錄 39 包 §3 之 **R-VS42** 入 RULINGS.md。
D-3  `DATA_REQUESTS.md`：
     - 補入 **DR-8**（00G §5）與 **DR-12**（29 包 §1.2）之條目
     - DR-21／22／23 改為類別式（39 包 §3 之三類），
       其實例清單待 W-58 補；DR-19 併入 DR-21、DR-20 併入 DR-23、
       DR-12 併入 DR-21，原編號保留並註「併入 DR-{n}」
     - 於 DR-21／23 本文註明「本類別包含已於 2026-08-22 送出之
       DR-19／DR-20」
D-4  ANOMALIES.md 新開 **A-VS66**（39 包 §4）。依 R-VS35 列兩數。

## 作業（**一項**，R-VS25）

W-58  全量可寫性掃描（39 包 §2 全文）
      產出 `docs/reports/writability.tsv` 與
      重建後之 `spec_variables.tsv`。
      **必列之數**：
        (a) 237 leaf 中 writable = yes 者幾條 ← **本 feature 之實際可交付量**
        (b) B1／B2／B3／B4 各幾條，涉及幾個 leaf
        (c) token 全集：原 30 → 重建後 N，新增者逐一具名
      **掃描條件逐類具名**（canon §5a 條 1）；
      B2 之比對須含裸名形態（R-VS36），且以 R-VS39 之正規化鍵。

**本輪不生成 TC。** batch03 俟 W-58 之可寫清單產出後再排。

## 禁區

git 不執行。不寫回工作簿。不代擬條文。
v1／v2／v3 保留不刪。

## 升級條件

writable = no 者超過 40 條（即 >17% 之母體）；
B4「其他」類非 0；
重建後之 token 數較原 30 增加超過 10。
```

---

## 7. 現況（依 R-VS31，僅列改變者）

| 項 | 變動 |
|---|---|
| pilot batch01 | **PASS**（Pei 2026-08-22），8 條放行 |
| framework | **已鎖定** |
| DR 送出 | 5 項待覆；**DR-18 仍待送**；DR-8／12 待補登記 |
| 已生成 | 14 條（batch01_v3 8 ＋ batch02 6） |
| 待 Pei | **DR-18 送出**；DR-21／22／23 俟 W-58 補全實例後一次送 |

---

## 8. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS42 | 同型缺件以類別開 DR，不逐實例；已開者併入 | 分析層（本輪額度用畢） |
| R-VS35 之補充 | 分析層側亦須逐輪核對其開立之 DR／anomaly 是否入簿 | 分析層（不另編號） |
