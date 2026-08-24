# 上繳 29 包：內容三項（下放包 `handoff/28_content.md` §二 A／B／C）

基底 `features/power/sandbox/b28/pm_28.xlsx`（sha256 `0dded0ea…`）。
輸出 `features/power/sandbox/b29/pm_29.xlsx`（sha256 `35305835…`），
389 資料列（列 10–399，其中列 334／No.# 325／`SWE-PM-089` 為既有空列），
止於工作副本，客戶目錄未動。

## 〇、與下放包字面之偏離 —— 先講

下放包 28 寫「基底 `pm_27`、輸出 `b28/pm_28.xlsx`」，且 §四-2 裁「四軌
**不收斂**，維持現狀，登記 A-PM18」。但 `b28/pm_28.xlsx` 在該下放包寫成前
一分鐘已由 commit `c2980fe`（上繳 `28_paren_convergence.md`）產出，內容正是
**已收斂為 V2**。兩者互斥。

Pei 當面裁定：**接 `pm_28`，輸出 `b29`**，理由為 §四-1 的 30 列 ER-only
括號已被該收斂包涵蓋且更徹底（ER-only 歸零），不重做。因此：

| 下放包 28 條目 | 本包處置 |
|---|---|
| §一 §四-1（30 列 ER-only 括號） | **已由 28 包達成**，本包零動作 |
| §一 §四-2（維持四軌、登記 A-PM18） | **已被 28 包越過**（已收斂）；A-PM18 未登記，待裁 |
| §二 A／B／C（內容三項） | **本包執行** |
| §三 驗收第 1 條「I 欄改動 = 恰 30 列」 | 不適用（§一已無動作），改驗「I 欄改動僅來自 §二-A 之括號下半」 |
| §三 其餘各條 | 逐條驗，見 §三 |
| 檔名 `pm_28` | 改 `pm_29`；③ 人讀覆核之基準隨之為 **pm_29** |
| 上繳檔名 `upstream/28_content.md` | 改 `upstream/29_content.md`（即本檔），與包號一致 |

## 摘要

| 項 | 要求 | 實測 | 狀態 |
|---|---|---|---|
| A 主詞 TLM→HU | 四欄＋括號下半殘留 0 | **828 次／272 列**改寫，殘留 **0** | 達成 |
| B 內部變數行為化 | 依表逐字句式 | proc/er **95 步**、pre **45 行** | 達成 |
| B 裸讀式殘留 | `Read Antitheft_Activation.Req`／`Read VPLastStatus`／`Read Timeout1` = 0 | **2 行**（VPLastStatus，套不進，見 §二-3） | **未達成，已列出** |
| C `Front_Panel_OnOff.Req` | proc 殘留 0 | **0**（9 步已改） | 達成 |
| PENDING 新增 | = RemStartFail 檢查步數 | proc **11** ／ er **11**，逐列見 §五 | 達成 |
| E（proc/er 1:1） | 0 | **0** | 達成 |
| lint A–N（含 I-sibling） | 全零 | **全零** | 達成 |
| 相異範圍 | test_item／pre／input／proc／er | **僅此五欄，285 列**；input 實際 0 改動 | 達成 |
| 列數／ID／No.# | 不變 | 399 列、Test Case ID 與 No.# 逐格同 pm_28 | 達成 |
| x14 讀回 | 前後相等 | `R10:R325` → `R10:R325` | 達成 |
| zip 成員 | 42 | **42**，差異成員僅 `xl/worksheets/sheet6.xml` | 達成 |
| `surgical_save` 唯一路徑 | 是 | 是（無插列，單段） | 達成 |

`verify.py` 共 13 項，**12 項達成、1 項為明列之例外**（裸讀式 2 行，
驗收判準寫成「殘留僅為明列之套不進句式者」，故 exit 0；其為未達成之事實
不因此被藏起來，見上表與 §二-3）。

規則在 `rules.py` 單一來源，`verify.py` **自 pm_28 獨立重跑該模組**再與
pm_29 逐格比對（不讀 `plan.json` 之結果值），故 build／apply 若脫節、
或規則實作有誤，驗收會攤開而非放行。

### lint 前後（`--profile power`）

| | A–N | I-sibling | P | Q | R | T | **U** |
|---|---|---|---|---|---|---|---|
| 28 包 `pm_28` | 全 0 | 0 | 10 | 0 | 0 | 0 | 10 |
| 29 包 `pm_29` | **全 0** | **0** | 10 | 0 | 0 | 0 | **32** |

U 由 10 → 32 為本包新置之 22 行 `PENDING: DR-PW23`（11 proc ＋ 11 er），
即 §二-6 之 RemStartFail。U 不屬 A–N，驗收不受影響；其上升是**刻意且可數**的。
報告：`docs/fw036/lint_reports/pm_29__power_35305835_20260824.md`。

## 一、A：主詞 TLM → HU

判準：`\bTLM\b`（word boundary）於 pre／input／proc／er 四欄全欄，
以及 test_item 之**括號下半整行**，替換為 `HU`；`$…$` 內一律不動。

白名單之四項全部由判準本身保證，未另寫例外表：

| 白名單 | 為何自動成立 |
|---|---|
| 1. `test_item` 上半 verbatim（R-6） | 只改整行為 `(…)` 之括號行，上半永不進入替換 |
| 2. `$…$` 內字串；`TLM_Status.Info` | `$…$` 逐段遮罩；`TLM_Status`／`TLM_Display` 之 `_` 為 word 字元，`\bTLM\b` 天然不命中（實測 206 處全數未動） |
| 3. `LTM`（radio 型號） | `LTM` 不含 `TLM` 子字串 |
| 4. PENDING 字串內文 | 基底 10 行（6 種）`PENDING:` 之說明內文中無 `TLM`；唯一相關者為 row 397 之 `Read the TLM screen and check that PENDING: DR-PW22 …`，`TLM` 在 `PENDING:` **之前**，屬裝置指涉，已改 |

改寫量：

| 欄 | 次數 | 列數 |
|---|---|---|
| test_item（括號下半） | 235 | 134 |
| pre | 216 | 212 |
| input | 0 | 0 |
| proc | 198 | 146 |
| er | 179 | 144 |
| **合計** | **828** | **272**（去重） |

殘留檢查：四欄＋括號下半之 `$…$` 外獨立 `TLM` token = **0**。

## 二、B：內部變數行為化

句式逐字取自下放包 §二-B 之表與 `features/power/docs/internal_var_observability.md`，
表外一律不改。改一步即同步改該步之 ER 行（索引對位，1:1，E=0）。

| 規則 | 對象 | 步數 | 列數 |
|---|---|---|---|
| B1 | 三設定之 proc 讀值 | 30 | 21 |
| B1-pre | 三設定之 pre 宣告 | 45 行 | 38 |
| B2 | `Antitheft_Activation.Req` | 24 | 24 |
| B3 | `VPLastStatus` | 16 | 16 |
| B4 | `Phone_Call.Info` | 4 | 4 |
| B5 | `Rear_Camera_Enable.Info` | 1 | 1 |
| B6 | `RemStartFail` → PENDING | 11 | 11 |
| C | `Front_Panel_OnOff.Req` | 9 | 9 |
| **合計** | | **95 步 ＋ 45 pre 行** | **285 列有改動（含 A）** |

### B1 三設定（`Timeout1`／`SwitchOff_Timeout_Setting.Req`／`Auto_SwitchOn_Setting.Req`）

proc：`Read <VAR>[ on the ex-factory unit] and check that it is <V>`
→ `Open the <setting> entry in the HU menu[ on the ex-factory unit] and read
the <setting> value and check that it is <V>`
ER：`<VAR> is <V>` → `The <setting> value is <V>`

pre：`<VAR> is [configured to ]<V>` → `HMI: "<setting>" is set to <V>`

`<setting>` 之取名（**執行層判斷，待追認**）：

| 變數 | `<setting>` | 依據 |
|---|---|---|
| `Timeout1` | `timeout setting` | 全本既有 16 列前例 `Open the timeout setting entry in the TLM menu`；SYSAD 載 Timeout1 由 SwitchOff_Timeout_Setting.Req 控制，同一 HMI 條目 |
| `SwitchOff_Timeout_Setting.Req` | `timeout setting` | 同上 |
| `Auto_SwitchOn_Setting.Req` | `auto switch-on setting` | **無前例**，依 SYSAD 之 user selectable setting 名意譯 |

逐條改動見 §六（附全清單）。

### B2 `Antitheft_Activation.Req`（24 步）

- `= True`（5 步，rows 149／201／202／203／204）→
  proc `Press the HU power button and check that the Antitheft HMI screen is shown`；
  ER `The Antitheft HMI screen is shown`
- `= False`（19 步，rows 45／52／64／133／134／135／138／150／154／156／205／206／209／210／211／212／216／218／219）→
  proc `Press the HU power button and check that the HU powers up without the Antitheft HMI screen`；
  ER `The HU powers up without the Antitheft HMI screen`

pre 之 `Antitheft_Activation.Req is True`（20 行）與 `is set to True`（2 行）
依「PRE 前提宣告維持宣告式不動」不改。

### B3 `VPLastStatus`（16 步）

- `ON`／`On`（10 步）→ `Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = 4
  (Ignition_On) and check that the HU powers up automatically and shows the
  splash screen`；ER `The HU powers up automatically and shows the splash screen`
- `OFF`／`Off`（6 步）→ `… and check that the HU does not power up automatically`；
  ER `The HU does not power up automatically`

`= 4 (Ignition_On)` 之 raw／label 對全本已有前例（row 170 之 pre），P 檢查未增（前後皆 10）。

### B4／B5

- `Phone_Call.Info`：`Active` 3 步（rows 256–258）→ `Place a phone call from
  the paired device and check that the call screen is shown`；`Not_Active`
  1 步（row 94）→ `End the call and check that the call screen is dismissed`
- `Rear_Camera_Enable.Info`：1 步（row 106）→ `Read the HU screen and check
  that the rear view camera image is shown`；ER `The rear view camera image is
  shown on the HU screen`。**表只給「行為化：倒車影像顯示與否」而未給逐字句式**，
  此句為執行層依該列既有措辭所擬，**待追認**

### B6 `RemStartFail` → PENDING（11 步，見 §五）

### C `Front_Panel_OnOff.Req`（9 步）

proc `Drive Front_Panel_OnOff.Req from Not_Pressed to Pressed` → `Press the HU
power button`（9 步：rows 102／104／110／111／121／124／149／201／202）；
ER `The Front_Panel_OnOff.Req press transition is registered`（8）與
`… is received`（1，row 110）→ 一律 `The HU power button press is registered`。
DR-PW24（與 `$ICSPowerButton$` 之對應）本包未動、未加 `$`。

pre 之 `The transfer popup is shown after the Front_Panel_OnOff.Req press`
（rows 122／123）為前提宣告、非 proc，未動。

## 三、執行層自加之判斷 —— 皆待追認

裁定未及、但不決就做不下去的，以下六項。全部非 Pei 原文。

### 1. B／C 一律不動括號下半（A 除外）

下放包 §二-A 明文含「括號下半」，B 與 C 只寫「四欄」（= pre／input／proc／er，
見 `lint036.P_FIELDS`），§三驗收亦只點名 proc。故本包**只讓 A 進括號**。

後果：77 列之括號下半仍含內部變數字樣（如 row 45
`(read Antitheft_Activation.Req -> Antitheft_Activation.Req reads "False")`），
而該列 proc 已無此步。**括號與 proc 就此不同調。** 括號文字係 28 包自 b19
原列推導（非自本列 proc／er 逐字複製，實測 389 列中 263 列兩半皆非本列行文），
故無法以「同一行改寫」順帶同步，須重跑 V2 通則才能收 —— 那是另一包的份量。
見 §七-1。

### 2. `timeout setting` 一名使兩變數之改寫撞號（5 列）

`Timeout1` 與 `SwitchOff_Timeout_Setting.Req` 同表列、同 HMI 條目，改寫後逐字相同：

| 列 | 欄 | 撞號後之重複行 |
|---|---|---|
| 95、96 | pre | `HMI: "timeout setting" is set to 00 MIN` ×2 |
| 97、98 | pre | `HMI: "timeout setting" is set to a value other than 00 MIN` ×2 |
| 237 | proc | `Open the timeout setting entry in the HU menu on the ex-factory unit and read the timeout setting value and check that it is 00 MIN` ×2（步 1 與步 3） |

**未去重。** 去重等於裁定「這兩條前提是同一件事」，超出下放包授權；
且 row 237 去重會動 proc 步數、連帶動 ER，E 由 0 變非 0。
lint 不因重複行違規（A–N 仍全零）。列此待裁。

### 3. 裸讀式殘留 2 行 —— 套不進

`Read VPLastStatus and check that it is the value held before the disconnection`
（rows 67、78；ER `VPLastStatus is the value held before the disconnection`）。
B3 之行為化需先知 ON 或 OFF 才選得出句式，「維持斷電前之值」兩者皆非。
依「不得自創」未改。**§三 驗收第 3 條因此未達成**，如實記於摘要表。

### 4. 三處「on the ex-factory unit」限定語就地保留

rows 215／237（共 5 步）之 `Read X on the ex-factory unit and check that…`
改寫時把限定語留在原位（`… in the HU menu on the ex-factory unit and read …`／
`Send the signal … on the ex-factory unit and check that …`）。
視為同一句式帶原有限定語之實例，非新句式。若判為自創，改回列入套不進清單即可
（會使 §三 第 3 條再多 2 行殘留）。

### 5. B1 之 ER 句式為推導所得

表只給 proc 側句式；「改一步即同步改該步之 ER 行」要求 ER 必須跟著換掉，
故 ER 取 `The <setting> value is <V>`（proc 側 `read the <setting> value` 之
直接對應）。B2–B6／C 之 ER 則有表內或 `internal_var_observability.md` 之逐字依據。

### 6. C 與 B2 同列各自套句式 → 同一 proc 出現兩次電源鍵按壓（3 列）

rows 149、201、202：

```
1. Press the HU power button                                        ← C
2. Press the HU power button and check that the Antitheft HMI screen is shown  ← B2
```

原文是「按鍵」與「讀 Antitheft_Activation.Req」兩件事，B2 的句式把「按鍵」
併進了觀察步，於是按了兩次。**未合併** —— 合併要刪一步、動 ER、動 E。
這三列的正解大概是刪掉 B2 那步的按壓前綴，但那是新句式，不得自創。列此待裁。

## 四、套不進上表句式之列清單（243 行，分析層接手）

依變數彙總；每組給句型與列號。

| 變數 | 行數 | 主要句型（欄） |
|---|---|---|
| `Antitheft_Result.Info` | 56 | `Set … to Successfully`(18)／`Not_Successfully`(9)／`In_Progress`(1)（proc）＋對應 ER 28 |
| `Phone_Call.Info` | 58 | pre 宣告 34；`Drive …`／`Set … to Not_Active [before …]`（proc 8）＋ ER 12、`MaxCallTimeout`／`Timeout1` 複合句 4 |
| `Antitheft_Activation.Req` | 22 | pre 宣告 22（依裁定不動） |
| `SwitchOff_Timeout_Setting.Req` | 21 | `Select … = <V>`(6)／`Read the offered values for …`(3)／`Read the offered parameters …`(2)／`Set … to 00 min`(1)＋ ER 9 |
| `Auto_SwitchOn_Setting.Req` | 20 | pre `holds/held a known value` 8／`Select … = <V>` 3／`Set … to Active` 1／`Read the offered parameters …` 2＋ ER 6 |
| `Rear_Camera_Enable.Info` | 20 | pre 宣告 6／`Set … to False/True` 4／`Drive … from False to True` 1／複合觀察 2＋ ER 7 |
| `Timeout1` | 19 | `Let Timeout1 run to its expiration …` 4／`… while Timeout1 is still running` 2／`Wait until Timeout1 has elapsed` 1／Antitheft 畫面時限 3／MaxCallTimeout 1＋ ER 7、pre 1 |
| `VPLastStatus` | 17 | pre 宣告 13／§三-3 之 2 行 proc ＋ ER 2 |
| `RemStartFail` | 8 | pre 宣告 7／`Let the HU evaluate the call state after the RemStartFail transition` 1 |
| `Front_Panel_OnOff.Req` | 2 | pre `The transfer popup is shown after the Front_Panel_OnOff.Req press`（rows 122、123） |

逐行明細（含列號）在 `features/power/scripts/b29/plan.json` 之 `unfit` 陣列，
共 243 筆，欄位為 `{row, field, var, line}`。

兩類值得單獨看：

- **`Antitheft_Result.Info` 之 28 個 `Set … to <V>` 步**：表寫「Antitheft HMI
  screen 之結果畫面」，但沒給句式；且 `Successfully` 是 lint check C 的 hedge
  詞，28 包 §二-3 已因此讓 4 列括號退回規則 3。**行為化這 28 步會同時解掉那個
  結構性衝突**，優先度應高於其他套不進項。
- **pre 宣告共 90 行**（Phone_Call 34、Antitheft_Activation 22、VPLastStatus 13、
  Auto_SwitchOn 8、RemStartFail 7、Rear_Camera 6）：依裁定「前提非觀察」不動，
  但三設定之 pre 已被改成 `HMI: …`。同一本裡「前提可以行為化」與「前提不行為化」
  兩種待遇並存，理由是「有無 HMI 條目」—— 這個理由成立，但沒寫進裁定，補記於此。

## 五、PENDING 清單（DR-PW23，11 步 ×（proc＋er）= 22 行）

字串一律 `PENDING: DR-PW23 observation method for RemStartFail`。

| 列 | Test Case ID | 步 | 原 proc | 原 er |
|---|---|---|---|---|
| 65 | …-056 | 3 | `Read RemStartFail and check that it is False` | `RemStartFail is False` |
| 93 | …-084 | 3 | `Read RemStartFail and check that it is True` | `RemStartFail is True` |
| 94 | …-085 | 3 | `… is False` | `RemStartFail is False` |
| 101 | …-092 | 3 | `… is True` | `RemStartFail is True` |
| 120 | …-111 | 3 | `… is False` | `RemStartFail is False` |
| 157 | …-148 | 3 | `… is False` | `RemStartFail is False` |
| 158 | …-149 | 2 | `… is False` | `RemStartFail is False` |
| 159 | …-150 | 3 | `… is False` | `RemStartFail is False` |
| 163 | …-154 | 2 | `… is False` | `RemStartFail is False` |
| 165 | …-156 | 2 | `… is False` | `RemStartFail is False` |
| 168 | …-159 | 2 | `… is False` | `RemStartFail is False` |

pre 側之 `RemStartFail is True/False`（7 行，rows 94／158／159／160／163／165／168）
為前提宣告，未改為 PENDING。

## 六、diff 證明

- 逐格比對 pm_28 × pm_29（A1:AH399，34 欄）：相異 **285 列**，
  相異欄僅 `I`(test_item)／`J`(pre)／`L`(proc)／`M`(er)；`K`(input) 實際 0 格。
- test_item 之相異：逐行比對後，**每一相異行皆為括號行且 `tlm_to_hu(舊行) == 新行`**
  —— 上半 verbatim 逐字未動，此為 verify 第 5 項。
- No.# (`B`)／Test Case ID (`F`)／spec (`N`)／其餘 29 欄：逐格相同。
- 列數 399、資料列 389、`R10:R325` 之 x14 下拉逐字相同、zip 42 成員中
  僅 `xl/worksheets/sheet6.xml` 有差異（`surgical_save` 單段路徑）。
- 自 pm_28 獨立重跑 `rules.py` 之結果與 pm_29 **389 列 × 5 欄逐格相符**。

## 七、本包是否仍有該驗而未驗者 —— 獨立判斷

**有，五項。**

### 1. 括號下半與 proc 已不同調（77 列）—— 本包刻意不碰，但沒人會自動發現

§三-1 已述成因。要緊的是：28 包的 V2 括號是**自 b19 原列**推導的，本包改的是
**pm_28 的 proc／er**。兩者從此各自為政 —— 日後任何一方再改，另一方都不會動。
28 包的 `verify.py` 仍會從 b19 重算並通過，因為它根本不看 proc／er。
**這是一個從此不再有人守的不變量。** 根治要嘛把 V2 通則改成從當前列的
proc／er 推導（然後重跑），要嘛明訂「括號是 b19 之摘要、與 proc 無需一致」。
本包未擅改。

### 2. 行為化改變了 40 步（38 列）的**受測情境**，未逐列覆核其仍測得到原需求

B2（24 步）把「讀 Antitheft_Activation.Req」換成「按電源鍵看畫面」，
B3（16 步）換成「送 Ignition_On 看是否自動開機」。row 45 是典型：原本是
「讓 HU 進 Standby → 讀變數 = False」，現在是「讓 HU 進 Standby → **按電源鍵**」——
按下去 HU 就離開 Standby 了，這一步把被測狀態本身破壞掉。
row 218 亦然（步 3 送 Ignition_On，改變了 Antitheft 流程進行中的前提）。

句式是裁定給的，本包照套；**但「照套之後這 39 列還測不測得到原需求」沒有驗，
也不是靜態檢查驗得出來的**。這 38 列應優先進 ③ 人讀覆核。

### 3. `<setting>` 之 HMI 條目名未對過 HMI 文件

`timeout setting` 有本文件內 16 列前例，`auto switch-on setting` 沒有任何前例，
是意譯。SYSAD 給的是變數名不是畫面上的字。真正的條目名應該去 HMI 規格
（`test_item` 有列提到 `TLM HMI documents`）對，本包未查 —— 該列 DR 尚未開。
建議併 DR-PW24 一起問上游。

### 4. `Timeout1` vs `SwitchOff_Timeout_Setting.Req` 是不是同一件事，本包只是假設

§三-2 的撞號、以及 B1 把兩者映到同一條目，都建立在「SYSAD 說 Timeout1 由
SwitchOff_Timeout_Setting.Req 控制 ⇒ 同一 HMI 條目」。SYSAD 原文只講控制關係，
沒講畫面。若其實是兩個條目（例如一個顯示 timeout 值、一個選 timeout 設定），
B1 的 30 步中有 21 步的條目名是錯的。**未查證。**

### 5. 沿舊仍未做者

- **A-PM18（四軌並存之已知形態差異）** —— 下放包要求登記，但 28 包已收斂，
  該異常實際不存在。`ANOMALIES.md` 未動，待裁：撤銷登記，或改登記為
  「28 包越過 §四-2 裁定」
- **③ 390 列人讀覆核** —— 未跑，基準應為 **pm_29**（非下放包所寫之 pm_28）
- **④ Excel 實開抽驗 + 授權** —— 屬 Pei，未做
- **⑤ 寫回 `(Revise2)` + TestRail 舊 ID→新 ID 對照表** —— 未做。本包未動列數
  與 ID，對照表基準不因本包而變（pm_26／27／28／29 之 ID 完全相同）
- 其餘七本仍凍結

## 八、引用之裁決編號

| 編號 | 出處 | 本包用法 |
|---|---|---|
| 下放包 28 §二-A | `handoff/28_content.md` | TLM→HU 及其四項白名單 |
| 下放包 28 §二-B | 同上 | 內部變數行為化之逐條句式 |
| 下放包 28 §二-C | 同上 | `Front_Panel_OnOff.Req` → 電源鍵 |
| 下放包 28 §三 | 同上 | 驗收七條（第 1 條改寫、第 3 條未達成，見 §〇／§三-3） |
| R-6 | canon | `test_item` 上半 verbatim，不受作者用語類檢查規制 |
| R-6b | canon | C 檢查僅及括號下半 |
| R-14 | canon | `PENDING:` 說明須為英文（T 檢查，本包新增 22 行皆合） |
| R-1 v3 | 21 包 | 訊號寫法 `$MSG.Sig$ = <raw> (<label>)`；B3 之新步依此 |
| R-9(a) | canon | pre 版面（R 檢查）；`HMI: …` 單一謂詞，未觸發 |
| 26 包 §C 裁定 3 | lint036 | 報告檔名帶來源 sha8 |
| 28 包 §八-1／§八-2 | `upstream/27_paren_fix.md`／`28_paren_convergence.md` | 括號現況之由來（本包不動括號之背景） |
| DR-PW23 | `DATA_REQUESTS.md` | RemStartFail 觀察途徑，本包置 11 步 PENDING |
| DR-PW24 | `DATA_REQUESTS.md` | `Front_Panel_OnOff.Req` ↔ `$ICSPowerButton$`，本包未動 |

## 九、產物

| 路徑 | 內容 |
|---|---|
| `features/power/sandbox/b29/pm_29.xlsx` | 輸出工作副本，389 資料列，sha256 `35305835…` |
| `features/power/scripts/b29/rules.py` | 三項改寫規則之**單一來源**（build／verify 共用） |
| `features/power/scripts/b29/build.py` | 分析層：逐列套規則 → `plan.json`（含 unfit／撞號／雙重按壓告警） |
| `features/power/scripts/b29/plan.json` | 285 列之新值、95 步 audit、243 筆 unfit |
| `features/power/scripts/b29/apply.py` | 執行層：285 列 / 731 格，`surgical_save` 單段 |
| `features/power/scripts/b29/verify.py` | 驗收 13 項，規則自基底獨立重算 |
| `docs/fw036/lint_reports/pm_29__power_35305835_20260824.md` | lint 後報告 |
