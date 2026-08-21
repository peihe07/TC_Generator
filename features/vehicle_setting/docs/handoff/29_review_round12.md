# 29 下放包 — 12 輪覆核：Atlantis Mid 之範圍問題、DR-15 之更正、13 輪指令

分析層寫入，2026-08-20。對象：`docs/upstream/10_criterion_and_framework.md`。

**覆核結論：接受。** 兩個升級皆為真，且 **A-VS42 之處置不是「補判準」——
是範圍問題，須 Pei 裁。** 另分析層於複驗中發現**自身在 DR-15 上引錯條文 id**，
見 §3。

---

## 1. A-VS42 —— 不是判準漏了 `Atlantis Mid`，是 R-VS19 與 037 直接衝突

執行層之實測：251 個已覆蓋 reqid 中 **121 筆之 `EE Architecture` 為
`Atlantis Mid`**（且 `Artifact Type` 全為 `Subsystem Functional Requirement`）。

**但分析層之 in-scope 判準並非疏漏 —— 它是 R-VS19 之實作。**

```
R-VS19（現行）
本 feature 僅採 `Atlantis High`（含 `All`）之條文；標記為
`CUSW`／`PowerNet`／`Atlantis Mid` 而未含 Atlantis High 者，
其值域不適用於本 feature。
```

故實測揭出的是：**037 之 Functional leaf 中，有一大批其來源條文
被 R-VS19 判為不適用。**

分析層自 `inputs/` 實體檔逐 leaf 量測（掃描條件：leaf → SYS-RA → SYS2
→ 7 位數 → 條文區塊之 `[EE Architecture]`；「純 Mid」定義為該 leaf 之
全部 reqid 之架構值含 `Atlantis Mid` 且**不含** `Atlantis High`）：

| 類 | leaf 數 |
|---|---|
| 全部 reqid 皆為純 Mid | **112** |
| 部分 reqid 為純 Mid | 3 |
| 無 Mid | 121 |
| 無 reqid | 1 |
| **合計** | **237** |

純 Mid 之 family 分布：**HeatedSeat 56／VentedSeat 42／HSW 8／Common 6**。

**即 237 個可測 leaf 中，112 個（47%）之來源條文全部落在
R-VS19 判為不適用的架構上。**

### 1.1 三種可能，本包不裁

| 可能 | 意涵 | 後果 |
|---|---|---|
| **(a)** R-VS19 過嚴：本專案實際涵蓋 Atlantis Mid | R-VS19 須修訂 | in-scope 母體擴大；值域取用之第一階範圍隨之擴大 |
| **(b)** 037 誤引：SWE.1 把 Atlantis Mid 之條文當成本專案需求 | 上游缺陷 | **112 個 leaf 之來源正當性存疑** → RD-1 |
| **(c)** 兩者並存：R1L／R1L-R 之車型同時出現在 Mid 與 High 條文中，架構標籤在此不具排他性 | R-VS19 之判準維度選錯 | 應改以 `Radio` 或 `ECU` 為主判準 |

**(c) 之徵候已在資料中**：執行層 §4 記 `Radio` 欄為空者視為不限；
而 §2.1 之 121 筆 `Artifact Type` 全為 Functional、
其 `Radio` 是否含 R1L 系列**未列**。**該欄是分辨 (a)/(b)/(c) 的關鍵。**

```
待 Pei 裁：R-VS19′（架構標籤之適用性）
實測：237 個 Functional leaf 中 112 個之來源條文全部標記為
`Atlantis Mid`（不含 `Atlantis High`），佔 47%。

現行 R-VS19 判其值域不適用本 feature。若維持，該 112 個 leaf 之值域
一律走 R-VS20 第二階（LID 表 ＋ DBC）——**這在技術上可行**，
因 LID／DBC 無架構條件。

但其連帶意涵為：**037 有 47% 之 leaf，其來源條文我方判為不適用** ——
該狀態應否向上游提出，屬範圍界定。

三選項：
(a) 維持 R-VS19，並就此向上游提 RD-1（037 之來源引用是否正確）
(b) 修訂 R-VS19：Atlantis Mid 於本 feature 適用（理由須具名）
(c) 改判準維度：以 `Radio` 含 R1L／R1L-R 為主判準，架構標籤為輔

分析層建議 **先做 §2 之 W-42 再裁** —— `Radio` 欄之分布會直接
排除或支持 (c)，該資料本輪未取。
```

### 1.2 對「母體 237 完整」之影響

執行層 §6-2 指出：`NEW ∪ Mid` 之未覆蓋為 **8**，較 11 輪逐條讀過之 6 筆多 **2**，
**該 2 筆從未被檢視**。

**分析層同意其判斷：在那 2 筆讀完之前，「(a) = 0、母體 237 完整」不能算已證。**
→ **W-42(3)**。

---

## 2. A-VS43 —— 成立，且分析層據此複驗，DR-15 之處置有變

`Multi-Level`／`Single-Level` 不在 08 包之 `one|two|three stage(s)` 形態內，
故其「1 / 27」為必然。**R-VS34 形態第三次，本次後果最重**
（08 包據此判「資料本身沒有可收斂之維度」）。

分析層複驗兩件事：

### 2.1 `Single/Multi Level` 於 CFTS044 之命中為 **0**

CFTS044 全文不使用該措辭；其對應概念寫作
`$Heated_Seat_Levels$ = [1]／[2]／[3]`（實測值域三值）。

→ **Comfort 側之 `Single-Level`／`Multi-Level` 與 CFTS044 側之
`Heated_Seat_Levels` 為同一維度之兩種措辭。**
兩份文件之階數維度**可以橋接**，08 包「資料無可收斂維度」之結論**確實錯了**。

### 2.2 分析層在 DR-15 上引錯了條文 id

17 包 §2.1 與 18 包 §2 稱 DR-15 之 CFTS044 證據為 **`4858356` / `4858386`**。
分析層本輪自實體檔複驗：

| reqid | 實際內容 |
|---|---|
| `4858356` | `When the HU receives a $HeatedSeatFR$ = [Heated Seat Off / HS_OFF] signal, the HU shall change the stored status…` —— **接收側，非請求側** |
| `4858386` | 同型（VentedSeatFL） |

**循環降階表之實際出處為四條，皆 `[EE Architecture:Atlantis High]`**：

| reqid | token |
|---|---|
| **`4858325`** | `$FL_HS_RQ$` |
| **`4858355`** | `$FR_HS_RQ$` |
| **`4858385`** | `$FL_VS_RQ_TGW$` |
| **`4858416`** | `$FR_VS_RQ_TGW$` |

**成因**：分析層當時以正則抓 `$FR_HS_RQ$ = [Medium]` 之命中位置，
再取「前一個 7 位數」作為其 reqid——**取到的是前一個區塊的號**（差 1）。
**未以區塊邊界驗證其歸屬。**

→ **DR-15 之問文須改正引用**（`4858325`／`4858355`／`4858385`／`4858416`），
**且該 DR 尚未送出，更正無外部代價。**

### 2.3 DR-15 之實質是否改變 —— **未變，但問法應加一問**

四條之 `[EE Architecture]` 皆為 `Atlantis High`，故 R-VS19 不排除之；
其明文令請求訊號承載 `Medium`／`Low`／`Off`／`High`，
而 DBC 之 `FL_HS_Tlm` 等為 1 bit `Not_Pressed`／`Pressed`。**衝突仍在。**

**惟 §2.1 之發現使其多一個可能解**：階數為配置維度
（`$Heated_Seat_Levels$` = 1／2／3），**請求訊號之行為是否隨階數配置而不同**，
CFTS044 未明言。DR-15 應加問此點。

---

## 3. A-VS44（Comfort 母體 27／22／17／498／129）之處置

執行層不自行調和，正確。分析層裁定：

```
分析層裁定 2026-08-20
Comfort 側之數字以**本輪實測**為準：
  相異 `SWE1-HVAC-` id（037 `Analysis Report`）= **129**
  `delegate = yes` 之 174 列所引之相異 Comfort leaf = **17**
06 輪之 498 為**資料列數**（含同一 id 之多列），非相異 leaf 數；
08 包之 27／22 為當時不同口徑之計數，**皆降為證據**。

爾後凡引 Comfort 母體，一律標明其口徑：
「資料列」或「相異 SWE1-HVAC id」。
```

**注意其對 §2 比例之影響**：階數明示 **5 / 17**（僅委派所引者），
若以 129 為分母則比例不同；**但分子 5 與分母無關**，
「資料有階數維度」之結論不因此動搖。

---

## 4. 13 輪指令

```text
你是 FW036 管線的執行層。repo: /Users/peihe/Work_Projects/TC_Generator

讀：
  docs/fw036/FEATURE_ONBOARDING.md                          流程權威
  features/vehicle_setting/RULINGS.md                        裁決正文
  features/vehicle_setting/docs/handoff/29_review_round12.md 本輪依據
其餘 handoff 只作證據。00 包 §3 之 R-VS1～R-VS6 仍逐字有效。

## 文書（不計入三項上限）

D-1  依 R-VS18 建立 docs/upstream/11_arch_scope.md，六節先留空。
D-2  ANOMALIES.md：
     - 新開 **A-VS45**：分析層於 17／18 包引 DR-15 之條文 id 錯誤
       （`4858356`／`4858386` 為接收側；實際為 `4858325`／`4858355`／
        `4858385`／`4858416`）。成因：以命中位置取「前一個 7 位數」，
       未以區塊邊界驗證歸屬
     - A-VS44 依 29 包 §3 標明口徑並降 06／08 之數為證據
     依 R-VS35 列「本輪新增 N／登記簿現有 M」兩數。
     **`A-VS02` 之缺號維持，不補不重編**（12 輪已記明）。
D-3  更正 `DATA_REQUESTS.md` 之 DR-15 條文引用為四條正確 reqid，
     並依 29 包 §2.3 加問：「請求訊號之行為是否隨
     `$Heated_Seat_Levels$`（1／2／3）之配置而不同？」
     **DR-15 仍不送出**（送出屬 Pei）。

## 作業（三項，R-VS25）

W-42  Atlantis Mid 之範圍證據（**不裁定，只取證**）
      (1) 對 112 個「純 Mid」leaf 之全部來源條文，逐條列出其
          `Radio`／`ECU`／`Market`／`Model Year` 四屬性之分布，
          與 121 個「無 Mid」leaf 之同四屬性分布**並列對照**
      (2) 判定：純 Mid 條文之 `Radio` 是否含 `R1L`／`R1L-R`？
          其 `ECU` 是否為頭端（`LTM`／`ETM`／`RRM`）？
          **若含且是，則架構標籤在此不具排他性（29 包 §1.1 之 (c)）**
      (3) 讀 `NEW ∪ Mid` 之 8 筆未覆蓋中、11 輪未讀過之 **2 筆**，
          判其 (a)／(b)／(c)。**(a) 非 0 為升級條件**
      **不得自行修改 in-scope 判準或 R-VS19** —— 屬 Pei（29 包 §1.1）

W-43  階數維度之全量複核
      (1) 以放寬形態
          `\b(one|two|three|single|multi)[\s-]?(stage|level)s?\b`
          掃 Comfort **全部 129 個相異 leaf**（非僅委派所引之 17），
          列明示階數者之筆數與逐筆節錄
      (2) 同一形態掃本 feature 之 237 個 Functional leaf 描述，
          與 `$Heated_Seat_Levels$`／`$Heated_Steering_Levels$` 之
          引用交叉，判兩份文件之階數維度能否逐 leaf 橋接
      (3) 依結果重估 08 包 W-34(1) 之「收斂 0 / 174」——
          **若可橋接，該收斂須重做**（記為 W-44，排 14 輪）

W-41′ framework Layer 3 之左右對稱追因（12 輪 §6-4）
      `LeftFrontHeatedSeat`(17) 與 `RightFrontHeatedSeat`(15) 之
      leaf 數差 2，逐條追因。**左右理應對稱** ——
      差額為 037 之遺漏、或右側條文被併入他 leaf，須具名。
      `framework.md` 仍**不鎖定**。

## 禁區

git 寫入性操作一律不執行。不補素材、不代擬條文、不自行調和數字。
**不得自行修改 in-scope 判準、R-VS19、或 framework 之鎖定狀態。**

## 升級條件

W-42(3) 之 (a) 類非 0；
W-43(2) 判定可逐 leaf 橋接（則 08 包之結論須撤回）；
W-41′ 之差 2 追因指向 037 遺漏；
實測與 29 包之數字不符；撞到 §8.4.1 編造壓力；需要判斷而無條文。
本輪無「必停」項。
```

---

## 5. 待 Pei

| # | 事項 |
|---|---|
| P18 | 裁 **R-VS7(a)′**（委派句精度）—— **已掛三輪**；且 W-43 之結果可能使其前提改變，**得俟 13 輪後再裁** |
| **P20** | 裁 **R-VS19′**（Atlantis Mid 之適用性，112 leaf 佔 47%）—— **建議俟 W-42 取證後再裁** |
| P19 | framework 草案簽核 —— **建議俟 W-41′ 之左右對稱追因後再簽** |

**三項皆建議俟 13 輪產出後一併裁**，本輪不催。

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS19′ | Atlantis Mid 之適用性（三選項） | **待 Pei** |
| A-VS44 之口徑裁定 | Comfort 母體以 129（相異 id）／17（委派所引）為準 | 分析層 |
| A-VS45 | 分析層引錯 DR-15 之條文 id | 分析層登記 |
| W-42／W-43／W-41′ | 作業 | 分析層 |
