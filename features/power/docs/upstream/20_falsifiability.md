# 上繳包 20 —— 複述判準訂正與地基再下一層

> 對應下放包：`features/power/docs/handoff/20_falsifiability.md`
> 執行層：Claude（TC_Generator）
> **§J 自檢已先驗**：§A fenced block = **6**、§J 列數 = **6**、§H 步驟 9 = 「**六條**」——
> **三處一致，未停。**
> 本包**未執行任何 git 操作**（除為修復自身瑕疵而 `git checkout` 還原一檔，見 §八(丙)）；
> **未對任何 workbook 呼叫 `save()`**；**未觸碰客戶樹與 `inputs/`**；
> **未改寫 19 §6.3 之十二條 ER**；**未對成對錨點裁定合併或排除**；
> **G103 之重算未讀 layer3 之任何中間產物**；**未以黏連正規化值取代原信噪比**；
> **未啟動第三批**。

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**

**編號查核（§H 步驟 2，R-P147 —— 先查後開）**：
**A-PW 最大 102、R-P 最大 141、DR-PW 最大 8、閘門最大 G102。**
本包新號自 **A-PW103 / R-P142 / G103** 起，無衝突。**本包無新增 DR。**
**全包未書寫任何未經查證之推估編號。**

---

## 一、B1 —— R-P142 之落實

### 1.1 十二條之處置

19 §6.3 之十二條**全數裁為偽陽性，ER 一字未改**（R-P142(a) / 20 §I）。

### 1.2 G73 之改動

| 項 | 改動 |
|---|---|
| **末步 ER 行** | **不再計 overlap**，一律以 `rule="R-P142"` 入 R-P76 之待人工裁決類（永久）|
| R-P133 之剝除邏輯 | **已移除**（該條後段由 R-P142 撤回）|
| 非末步 ER 行 | overlap 判定不變（`R-P96(a)` / `R-P96(b)`）|
| finding 之 `detail` | 逐條載明須以**可證偽性**裁決 |

### 1.3 加註與雜湊佐證（依 R-P36，原文不改）

| 條 | 加註前 SHA256 | 加註後 | bytes | 判定 |
|---|---|---|---|---|
| **R-P96** | `5bcbe45ead1b2edfea93b1b243a59af705fba12ca1371164463c5ba07a56cb54` | 同 | 1499 | **UNCHANGED** |
| **R-P133** | `fd3c7c25c1b2aa04cbc1e5a0f78738d26fb0e402097c1e209c4b65385d0d5c30` | 同 | 993 | **UNCHANGED** |

加註內容分置於各該裁決區塊**之外**（比照 12 / 14 / 15 包之作法）。

### 1.4 改動後之 lint（G104）

| 項 | 實測 |
|---|---|
| TC 數 | **43** |
| **阻斷類** | **PASS** |
| **待人工裁決類** | **44 項** |
| 其中 `R-P142` | **43 項**（每條 TC 之末步 ER 行各一）|
| 其中 `R-P96(a)` | **1 項** —— `028` 之**非末步**第 1 行（overlap 0.57）|
| `R-P42(b)` | 0 |

**`028` 之該項執行層裁為偽陽性**：
`The outgoing call is connected and its audio is routed through the TLM` ——
在「撥出動作成功執行」之情形下**仍可能失敗**（未接通、音訊未路由至 TLM），
符可證偽性。

**十二條中之十一條為末步行，已隨 R-P142 改入 `R-P142` 類；
餘一條（`028` #1）為非末步，仍走 overlap 而由執行層裁為偽陽性。**

### 1.5 G73 fixture 之隨判準改寫

複述案改置於**非末步**（三步 procedure），使 overlap 判定仍適用；
正常案之期望改為「非末步 R-P96 **0** 項、末步 R-P142 **1** 項」。**二案皆如期。**

---

## 二、B2 —— R-P143 之屬性資料（**未裁定**）

輸出 `data/b2_anchor_state.md`，含六個錨點之**標頭原字串逐字**
（供覆核屬性抽取是否完整）。

## 1. 逐欄原值

| 屬性 | `4941727` | `4941728` | `4941729` | `4941730` | `4941735` | `4941736` |
|---|---|---|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | Subsystem Functional Requirement | Subsystem Functional Requirement | Subsystem Functional Requirement | Subsystem Functional Requirement |
| ECU | LTM, ETM, RRM | RRM, LTM, ETM | LTM, ETM, RRM | RRM, ETM, LTM | LTM, ETM, RRM | RRM, LTM, ETM |
| EE Architecture | Atlantis Mid, Atlantis High | Atlantis Mid, Atlantis High | Atlantis High, Atlantis Mid | Atlantis High, Atlantis Mid | Atlantis High, Atlantis Mid | Atlantis Mid, Atlantis High |
| Market | All | All | All | All | All | All |
| Model Year | （無此欄） | 2017 | （無此欄） | 2017 | （無此欄） | 2017 |
| Radio | allSys | allSys | allSys, noSys | allSys | allSys, noSys | allSys |
| **State** | **Under Review** | **Under Review** | **New** | **Under Review** | **New** | **Under Review** |

## 2. `State` 值（本條特別要求）

| 錨點 | `State` | 對 |
|---|---|---|
| `4941727` | **Under Review** | 第 1 對 |
| `4941728` | **Under Review** | 第 1 對 |
| `4941729` | **New** | 第 2 對 |
| `4941730` | **Under Review** | 第 2 對 |
| `4941735` | **New** | 第 3 對 |
| `4941736` | **Under Review** | 第 3 對 |

## 2.1 SYS2 匯出之 `All_Accepted` 是否即 `State` 過濾（R-P143 之附帶回報）

> **否 —— 二者不是同一件事。**

| 項目 | 實測 |
|---|---|
| SYS2 匯出檔名 | `SYS2_CFTS_009_…_Polarion_uploaded_**All_Accepted**_04_13_2026.xlsx` |
| 匯出中之狀態欄 | **無 `State` 欄** —— 有 `SYS2 HARMAN Status`（第 15 欄）與 `SYS2 MD Status`（第 17 欄）|
| CFTS009 之 `HARMAN Status` 值分布 | `Accepted` **168**、**`Need rework` 4**（其餘列該欄為空）|
| CFTS009 之 `MD Status` 值分布 | `Accepted` 168 |
| CFTS010 | `HARMAN Status` / `MD Status` 皆 `Accepted` 4，無非 Accepted 者 |
| `Need rework` 之四列 | `Sys-RA-PM-0021`、`Sys-RA-PM-0291`、`Sys-RA-PM-0292`、`Sys-RA-PM-0293` |

**兩項結論**：

1. **`All_Accepted` 指的是 SYS2 之審查狀態（HARMAN / MD Status），
   與 CFTS 錨點標頭之 `[State:…]`（Polarion 工作流狀態，值為 `New` / `Under Review`）
   是兩個不同層級的欄位。** 匯出中不含 `[State:…]` 之對應欄。
2. **檔名之 `All_Accepted` 於 CFTS009 並非字面為真** ——
   `HARMAN Status` 有 **4 列為 `Need rework`**。
   **該四 token 之範圍已順帶查證**（成本極低）：全 115 leaf 中，
   僅 **`SWE-PM-112`** 引用其一（`Sys-RA-PM-0293`）；
   **不落在已產出 TC 之 11 leaf 內**，故不影響現有 43 條。
   `Sys-RA-PM-0021` / `0291` / `0292` **無任何 leaf 引用**。

**執行層不就 `State` 相異是否影響範圍作任何裁定**（R-P143 明訂裁定於 21 包）。


### 2.1 `State` 之實測 —— **相異者為二對，非三對**

| 對 | 錨點 | `State` | 是否相異 |
|---|---|---|---|
| 1 | `4941727` / `4941728` | **Under Review** / **Under Review** | **相同** |
| 2 | `4941729` / `4941730` | **New** / **Under Review** | **相異** |
| 3 | `4941735` / `4941736` | **New** / **Under Review** | **相異** |

19 包所報「三對之差異欄位為 Model Year / Radio / State」為**逐對聯集之陳述**；
逐對細看，**第一對僅 `Model Year` 相異，其 `State` 相同**。此處更正。

### 2.2 `All_Accepted` 是否即 `State` 過濾 —— **否**

| 項目 | 實測 |
|---|---|
| SYS2 匯出中有無 `[State:…]` 對應欄 | **無** |
| 其狀態欄 | `SYS2 HARMAN Status`（第 15 欄）、`SYS2 MD Status`（第 17 欄）|
| CFTS009 `HARMAN Status` | `Accepted` **168**、**`Need rework` 4** |
| CFTS009 `MD Status` | `Accepted` 168 |
| CFTS010 | 皆 `Accepted`（各 4）|

> **兩項結論**：
> 1. `All_Accepted` 指 **SYS2 之審查狀態**（HARMAN / MD Status），
>    與 CFTS 錨點標頭之 `[State:…]`（Polarion 工作流狀態）**是兩個不同層級的欄位**。
> 2. **檔名之 `All_Accepted` 於 CFTS009 並非字面為真** —— 有 4 列為 `Need rework`。

該四列為 `Sys-RA-PM-0021` / `0291` / `0292` / `0293`。
**範圍已順帶查證**（成本極低）：全 115 leaf 中僅 **`SWE-PM-112`** 引用其一（`0293`），
**不落在已產出 TC 之 11 leaf 內**，不影響現有 43 條；
`0021` / `0291` / `0292` **無任何 leaf 引用**。

**執行層未就 `State` 相異或 `Need rework` 作任何範圍裁定**（R-P143 明訂裁定於 21 包）。

---

## 三、B3 —— G103 layer3 token 層完整性（R-P144）

`features/power/scripts/verify_layer3.py` → `data/g103_layer3.md`

自 037 之 `Source Requirement ID` 欄**獨立重算** token → SYS2 → item id；
§C 之正則於該檔**獨立宣告**（非自 `build_layer3.py` import）；
**未讀取 `item_to_chapter.json` / `leaf_main_chapter.json` 之任何內容**，
`layer3_full.tsv` 僅作比對對象（R-P144(a)）。

## 比對範圍：已產出 TC 之 11 leaf

| leaf | token 數 | 重算 item 數 | layer3 item 數 | layer3 缺 | layer3 多 | 判定 |
|---|---|---|---|---|---|---|
| `SWE-PM-038` | 6 | 13 | 13 | — | — | **相等** |
| `SWE-PM-057` | 7 | 9 | 9 | — | — | **相等** |
| `SWE-PM-060` | 1 | 1 | 1 | — | — | **相等** |
| `SWE-PM-061` | 1 | 1 | 1 | — | — | **相等** |
| `SWE-PM-062` | 1 | 1 | 1 | — | — | **相等** |
| `SWE-PM-063` | 1 | 1 | 1 | — | — | **相等** |
| `SWE-PM-064` | 1 | 1 | 1 | — | — | **相等** |
| `SWE-PM-065` | 1 | 2 | 2 | — | — | **相等** |
| `SWE-PM-071` | 1 | 1 | 1 | — | — | **相等** |
| `SWE-PM-072` | 1 | 1 | 1 | — | — | **相等** |
| `SWE-PM-073` | 1 | 1 | 1 | — | — | **相等** |

**11 / 11 相等。**

未能解析至任何 SYS2 列之 token：（無）


### 3.1 fixture 與**一項須明報者**

| fixture | 期望 | 實測 |
|---|---|---|
| 037 原值 | 相等 | **相等** |
| **刻意刪去一個 token（`Sys-RA-PM-0146`）** | FAIL | **FAIL —— layer3 多 `4941692`** |
| **037 該列為空** | FAIL | **FAIL —— layer3 多全部 9 個** |
| **037 引用 SYS2 未載之 token** | FAIL | **FAIL**（改判準後）|

> **第四案原本寫的是「多一個不存在之 token → 應 FAIL」，而實測為「相等」。**
> **那不是閘門瑕疵，是我的期望值寫錯** —— 不可解析之 token 不產生任何 item，
> 集合自然相等。
> **但它暴露了一個真的漏洞**：037 若引用 SYS2 未載之 token，
> **該錨點形同消失而閘門全綠**。
> 已將 `unresolved` 併入判定（`ok = 集合相等 and not unresolved`），
> fixture 改為對應之描述，現如期。本包 11 leaf 之 unresolved 為 **0**（A-PW109）。
>
> 此為「**fixture 期望值寫錯反而查出真問題**」之第二例
> （首例為 18 包 G95 之分頁選錯）。

**至此：G94 驗「抄對了」、G99 驗「抄全了 layer3 所載者」、
G103 驗「layer3 載全了 037 所引者」。**

---

## 四、B4 / B5 —— 第二桶抽樣與並存信噪比

## B4 —— 「已由他條涵蓋」桶之覆核（R-P145）

該桶共 **20** 項，**全數列出（覆核率 100%，高於「措詞差異」桶之 16.7%）**。

> 該桶雖為機械判定（該殘差詞見於同 leaf 之他條 TC），**其判定規則仍為執行層所訂** —— 故一併送覆核。

| leaf | 行為項 | 殘差詞 | 最佳對應 | overlap | 見於同 leaf 之他條 |
|---|---|---|---|---|---|
| `SWE-PM-038` | #1 | `call` | `033` | 0.61 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #1 | `dab` | `033` | 0.61 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #1 | `expiration` | `033` | 0.61 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #1 | `restore` | `033` | 0.61 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #1 | `tuner` | `033` | 0.61 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #6 | `expiration` | `033` | 0.82 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #6 | `maxcalltimeout` | `033` | 0.82 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #7 | `expiration` | `033` | 0.85 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #7 | `maxcalltimeout` | `033` | 0.85 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #8 | `expiration` | `033` | 0.69 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #9 | `expiration` | `033` | 0.73 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #10 | `pass` | `043` | 0.67 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #10 | `start` | `043` | 0.67 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #14 | `condition` | `033` | 0.60 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #14 | `previou` | `033` | 0.60 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #15 | `condition` | `033` | 0.67 | 同 leaf 共 11 條 |
| `SWE-PM-038` | #15 | `previou` | `033` | 0.67 | 同 leaf 共 11 條 |
| `SWE-PM-062` | #1 | `active` | `026` | 0.69 | 同 leaf 共 3 條 |
| `SWE-PM-062` | #1 | `recall_last` | `026` | 0.69 | 同 leaf 共 3 條 |
| `SWE-PM-065` | #1 | `manag` | `031` | 0.46 | 同 leaf 共 2 條 |

---

## B5 —— 信噪比：原值與黏連正規化後之值並存（R-P146）

> **判準未改**（20 §I）—— 黏連僅另列一行，不自母體剔除，**不以任一值取代另一值**。

| 口徑 | 分子（真缺口）| 分母（殘差詞）| 信噪比 |
|---|---|---|---|
| **原值**（19 包所報）| 1 | 145 | **0.7%** |
| **黏連正規化後** | 1 | 138 | **0.7%** |

被判為抽取層黏連之殘差詞（**7** 項，2 個相異詞）：

`expirationthenat`、`minutesand`

其原文形態取自 `source_clause` 中含內部大小寫轉折之詞（如 `00 minutesAND`、`expirationTHENat`、`THENTLM`）——
係轉檔時空白遺失所致，**非語義單位**。

### 4.1 一項更正 —— 19 包之陳述為誇大

19 §八(乙)6 稱「它們拉高分母，也就拉低了信噪比 —— 0.7% 有一部分是抽取層造成的」。

**實測：黏連僅 7 項（2 個相異詞），分母 145 → 138，比值不動（0.7% → 0.7%）。**
**該陳述為誇大，執行層更正之。** 黏連確實存在，但其量不足以移動該比值。

**黏連辨識啟發式之演進亦如實記錄（三版）**：
初版以「內部大小寫轉折 `[a-z][A-Z]`」判定 → **誤將 `MaxCallTimeout` 這類
CamelCase 參數名判為黏連**，虛報 **23** 項；
次版以子字串精確化 → 仍留 `maxcalltimeout`，**10** 項；
現版限定「內嵌全大寫連接詞（`AND` / `THEN` / `OR` / `IF` / `WHEN` / `ELSE`）」→ **7** 項。
**專案判準（透鏡 3 之殘差規則）一字未改**（20 §I）；
改的僅為本報告之黏連辨識啟發式，其三版之誤判形態已寫入程式碼註解。

---

## 五、§D 全表自驗

| # | 項目 | 期望值 | **實測** | 判定 | 證據型別 |
|---|---|---|---|---|---|
| **G0** | 素材同一性 | 7 / 7 | 7 / 7 | **PASS** | 真實 |
| **G103** | layer3 token 層完整性 | 11 leaf 全數相等；刻意刪 token → FAIL | **11 / 11 相等**，unresolved **0**；fixture 四案如期 | **PASS** | **合成＋真實** |
| **G104** | R-P142 落實後之 lint | 阻斷類全 PASS；待裁類含全部末步 ER 行；十二條不再列為疑似複述 | 阻斷類 **PASS**；待裁 **44** = R-P142 **43**（每條末步各一）＋ R-P96(a) **1**（`028` 非末步）；**十二條中十一條已改入 R-P142 類，餘一條裁為偽陽性** | **PASS** | 真實 |
| **G105** | 第二桶抽樣 | 抽樣率 ≥ 16.7%；種子載明 | 「已由他條涵蓋」桶 20 項**全數列出（100%）**；「措詞差異」桶 20/120（16.7%，`SEED = 19`）| **PASS** | 真實 |
| **G106** | 並存信噪比 | 原值與正規化值並列；黏連 token 清單已附 | 0.7%（145）／0.7%（138）並列；黏連 **7 項、2 個相異詞**已附 | **PASS** | 真實 |
| **G70** | lint 全閘 | 全 PASS；leaf 11；TC 43 | `exit=0`；leaf **11**；TC **43**（R-P143 未裁，未增減）| **PASS** | 真實 |
| G94 / G99 | 沿用 | 期望值不變 | 11 / 11、11 / 11 | **PASS** | 合成＋真實 |
| G1–G102 | 沿用 | 期望值不變 | `--self-test` **35 / 35 TC fixture ＋ G46 皆如期**；G85 五案如期 | **PASS** | 混合 |

---

## 六、末步 ER 之 43 項裁決（R-P142(d)：沉默不算裁決）

R-P142(d) 明訂人工裁決不得省略。43 項逐條以**可證偽性**裁決之結果如下。
**判準**：該 ER 行能否在其 procedure 步驟成功執行之情形下仍然失敗。

| 群 | TC | 末步 ER 行之形態 | 裁決 | 依據 |
|---|---|---|---|---|
| 首批 splash / standard screen | `001` `004` | `No splash screen appears before …, and the splash screen is loaded once …` | **非複述** | 讀了畫面仍可能顯示錯誤內容或時序不符 |
| 首批 Standby / Bench 抑制 | `002` `003` | `No splash screen appears at any time through SplashScreen_Time …` | **非複述** | 讀了畫面仍可能出現 splash |
| 首批事件緩衝 | `005` `006` | `The buffered event count equals the injected event count …` / `Every buffered event is processed …` | **非複述** | 計數可不符、可有事件未處理 |
| 首批 Load Shed / Battery Critical | `007` `009` `014` `016` `017` | `The maximum volume … is reduced to 20, AUD_LVL carries …` / `No AUD_LVL signal … appears` | **非複述** | 值可不符、訊號可出現或不出現 |
| 首批故障／回復 | `008` `010` `011` `012` `013` `015` | `The Load Shed action is maintained …` / `The volume limit returns to its normal maximum …` / `The continuing call is routed to the head set …` | **非複述** | 皆為系統側狀態，可與期望不符 |
| 第二批 Timeout1 選項 | `018` `019` `020` | `Timeout1 reads "00 min" after the first selection and "…" after the second` | **非複述** | 讀到他值即 fail |
| 第二批參數個數 | `021` `022` | `Auto_SwitchOn_Setting.Req is the only parameter offered …` | **非複述** | 可多可少 |
| 第二批 Full-Operation 限制 | `023` `024` | `The parameter reads back the newly selected value` / `… its previous value and no change is stored` | **非複述** | 讀到他值即 fail；否定側可被錯誤接受 |
| 第二批 Auto_SwitchOn 三值 | `025` `026` `027` | `Auto_SwitchOn_Setting.Req reads "…" and Timeout1 …` | **非複述** | 二參數之值皆可不符 |
| 第二批 Timed 通話 | `028` | `Both calls were served and the TLM remains in Timed state` | **非複述** | 可掉話、可離開 Timed |
| 第二批 MaxCallTimeout 啟動 | `029` `030` | `The MaxCallTimeout counter is running from …` | **非複述** | 可未啟動或起算點錯誤 |
| 第二批還原音源 | `031` `032` | `The DAB Tuner source is active again and the TLM remains in Timed state` | **非複述** | 音源可未還原 |
| 第二批 Case 1–4 | `033`–`043` | `RemStartFail reads "False", TLM_Status.Info reads "Standby" and the TLM is in Standby state` 等 | **非複述** | 訊號值與狀態皆可不符 |

> **43 / 43 裁為非複述（偽陽性）。**
> **一項自陳**：裁決者仍為撰寫者 —— 這 43 條的 ER 是我寫的，
> 判它們可證偽的也是我。R-P142(d) 要求不得省略裁決，這一步做到了；
> **它沒有解決「誰來裁決」的問題。**

---

## 七、DATA_REQUESTS

DR-PW1（High）、DR-PW5（High）、DR-PW8（High）、
DR-PW3（Medium）、DR-PW6（Medium）、DR-PW7（Low）維持 live；
DR-PW2、DR-PW4 維持撤回。**本包無新增。**

---

## 八、執行層對「本包是否仍有該驗而未驗者」之獨立判斷

分析層於 §K 自判四項（第二批覆核未完成、R-P142 之規模問題、037 欄本身無閘門、
`ATTR_RE` 之限制未解），執行層無異議，**本節不覆述**。

**（甲）本包新產生或新暴露之該驗而未驗者 —— 四項**

1. **R-P142 把 43 項推入人工裁決，而我在同一包裡把 43 項全裁完了。**
   §K 第 2 項指出規模問題未解；我要補的是**更根本的一點**：
   **這 43 項的裁決者就是撰寫者。** 我判「可證偽」的依據，
   和我當初寫這些 ER 時的依據是同一個。
   R-P142(d) 的「沉默不算裁決」防的是漏裁，**防不了自我背書**。

2. **`028` 那一項是十二條裡唯一沒被 R-P142 接手的，而它的處理路徑不同。**
   它是非末步行，仍走 overlap，仍由我以 R-P96 之舊判準之外的理由裁為偽陽性。
   **即：同一批十二條，十一條依新判準、一條依舊判準加人工判斷。**
   這個不一致是 R-P142(c)（非末步維持不變）的直接後果，
   本包照做了，但它意味著**非末步行的判準仍是已知有誤的那一個**。

3. **G103 補到了 037 這一層，而 037 之上是空的。**
   §K 第 3 項已明載此為鏈路終點。我要補的是它的**具體後果**：
   G94 / G99 / G103 三閘全綠，其涵蓋範圍是
   「037 所寫的 → layer3 → source_clause → ER」這條鏈**內部一致**。
   **它們合起來不能排除「037 本身引錯了 token」。**
   A-PW110 之 `Need rework` 四列即是這一層的提醒：
   037 引用了 SYS2 標為需重工的需求，而本專案沒有任何機制會注意到。

4. **B2 之屬性資料我附了標頭原字串，但那只是讓人**能**覆核，不是已覆核。**
   §K 第 4 項指出 `ATTR_RE` 之形態限制。我附上原字串正是為此，
   **但沒有人讀過那六段原字串** —— 分析層讀不到 CFTS 本文（19 §K 第 2 項），
   而我就是抽取者。原字串在報告裡，覆核仍未發生。

**（乙）已驗而應標明其強度不足者 —— 一項**

5. **我在 19 包說黏連「拉低了信噪比」，實測顯示那是誇大。**
   已於 §四之 4.1 與 A-PW107 更正。
   值得記的不是這個數字，而是：**那句話當時聽起來合理，我也就寫了，
   沒有算過。** R-P64 之「量化修飾語須標實測或推測」正是為此而設，
   而我當時既未標推測、也未實測。

**（丙）本包自身之作業瑕疵 —— 二項**

6. **落實 R-P142 時，我用了過寬的字串切片，一併刪掉了
   `lint_tcs.py` 的四個函式**（`check_s52b_final_step_intent`、
   `check_source_clause`、`check_misread_terms`、`check_er_clause_coverage`）。
   **當場由 `NameError` 攔下**，以 `git checkout` 自 HEAD 還原後改以精確之最小替換重做。
   **這是寬切片的第三次** —— 05 包（§E 偏移）、11 包（誤刪二常數）、本包。
   前兩次我都寫過「每次編輯獨立進行、不共用位移」，**而這次是切片邊界選錯，
   不是位移問題** —— 舊規則沒有涵蓋這個形態。已登記 A-PW111。
   附帶說明：該次 `git checkout` 是為修復我自己造成的損壞而還原單一檔案至 HEAD，
   非版本控管操作，未 commit、未 push、未動任何他人檔案。

7. **黏連辨識啟發式我改了三版（23 → 10 → 7 項）。**
   每一版都是看到誤判之後才改的。**這與 13 包「先看答案再定門檻」同型**，
   差別在於它影響的是**報告中的一個附帶數字**，不是專案判準
   （專案判準一字未改，20 §I）。三版之誤判形態已寫入程式碼註解供檢驗。

---

## 九、產出檔案

| 檔案 | 說明 |
|---|---|
| `features/power/scripts/verify_layer3.py` | G103（新增，含 self-test）|
| `features/power/data/g103_layer3.md` | G103 報告（新增）|
| `features/power/data/b2_anchor_state.md` | R-P143 屬性原值與 `All_Accepted` 查證（新增）|
| `features/power/data/b5_residual_sample.md` | B4 第二桶全列 ＋ B5 並存信噪比（改）|
| `features/power/scripts/build_residual_sample.py` | B4 / B5 之產生（改）|
| `features/power/scripts/lint_tcs.py` | R-P142 之末步分支與 G73 fixture（改）|
| `features/power/RULINGS.md` | R-P142 ~ R-P147、R-P96 / R-P133 加註（改）|
| `features/power/ANOMALIES.md` | A-PW103 ~ A-PW111、A-PW92 更新（改）|
| `features/power/docs/upstream/20_falsifiability.md` | 本檔（新增）|
| `features/power/docs/INDEX.md` | 第 20 輪索引（改）|
