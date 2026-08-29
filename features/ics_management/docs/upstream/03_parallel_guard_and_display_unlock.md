# 上繳包 03 — 並行防護、CFTS020 全域重判、Display 面解鎖（2026-08-29）

對應下放包：`docs/handoff/03_parallel_guard_and_display_unlock.md`
**開工時重測之 sha256（R-ICS17(e)）＝ `1ebd3601cbd96a472429e58f82ef52dc9c26f104a8a7c0159a1dbd3bfdd539ce`**
—— 執行層自身記錄與之相符，未停。

**禁區遵守**：git 全數未執行；`RULINGS.md`／`ANOMALIES.md`／`DATA_REQUESTS.md`／
`framework.md`／`ANALYSIS_LOCK.md`／`docs/handoff/**` 一字未寫（`ledger_guard.py`
開工前／完工後二次輸出**逐字相同**，見 §7-1，即此事之機器證據）；
canon／`GATES.tsv`／`RULINGS.sha.tsv`／`PATH_POLICY_BASELINE.tsv` 未動；未搬素材；
009／005 之 TC 新增 0；ignore 面未用 120 s；`<TPeriodToCountKnobDetents>` 未臆值。

**並行執行說明**：本包之作業 B／E／F 以三個並行執行層實例同時進行，
各自之可寫檔集合互斥（B：`cfts020_probe.py`＋`gen_recon_v2.py`＋`03_cfts020_recon_v2.md`；
E：`lid_dbc_probe.py`＋`generated/b03/lid_dbc_map.json`；
F：`src_recon_03.py`＋`03_source_recon.md`），無一觸及 §1 禁區。
作業 A／C／D 由主實例執行。此為**執行層內部之並行**，
與 R-ICS17 所治之分析層台帳單一寫者無涉。

---

## §0 量測基礎

沿上繳包 01 §0 與 02 §0 之全部條件。本包新增／自驗者：

| 項 | 條件 |
|---|---|
| CFTS020 物件母數 | **2180**（屬性頭 `^\d{7}: \[`）。**407 為章節標題數**，本包凡引必明標其為章節數 |
| v2 判準實作 | (i) `Radio ∈ {R1L, R1L-R, allSys}` ∧ `EE ∈ {Atlantis High, All}`；(ii) `ECU` 軸**存在時**須含 `{ICS, LTM}`，不存在時不視為不適用亦不記 WARN |
| LID 表頭（**本包自驗，未沿用前包**）| 群組列 = 第 2 列（`Atlantis High` 起於 c26），欄名列 = 第 3 列，資料自第 4 列起（`max_row` 2627）；`Atlantis High` 五欄 = c26 `Signal Name`／c27 `CAN`／c28 `Format`／c29 `SNA`／c30 `VFs`；另 c1 `Logical Identifier`、c31 `Usage Comment`。腳本以「掃到 `Atlantis High` 定位群組欄，再逐一斷言下一列五個子欄名相符」實作，欄號不符即拋錯 |
| DBC 解析 | 訊息 `^BO_ <id> <NAME>: <dlc> <node>`；訊號**以界內行號認定**（下一個 `BO_` 為邊界）；列舉 `^VAL_ <id> <sig>`。**編碼為 ISO-8859-1，非 UTF-8**（見 §六-3） |
| PDF 抽取（作業 F）| `pdftotext` 與 `pdfplumber` 雙工具逐頁；非空白字元逐頁皆 0 者記 `NO_TEXT_LAYER`，**不 OCR**。另做**去連字號重掃**（PDF 有 `pop-\nup` 斷行，逐行掃會漏） |
| 逐字比對之正規化 | 上繳包 01 §0 之四項，**本包新增第五項**：句首字母之大小寫（R-4：自原句中段起抄時句首轉大寫屬排版正規化）|

---

## §1 裁決指紋（R-ICS1 ~ R-ICS17 全部，`R-ICS2` v1／v2 並列）

`python3 scripts/rulings_hash.py --target features/ics_management/RULINGS.md`
—— **18 錨點**，來源 1 檔。工具對 `R-ICS2` 之二列印出「本體不同」之提示，屬預期（R-ICS17(d)）。

| 條 | sha8 | 落檔行 | 本文行數 |
|---|---|---|---|
| R-ICS1 | `3e48552b` | 12 | 8 |
| **R-ICS2 v1** | **`4a8819f0`** | 25 | 17 |
| R-ICS3 | `b10318e0` | 47 | 9 |
| R-ICS4 | `85de9871` | 61 | 10 |
| R-ICS5 | `e6a4790d` | 76 | 11 |
| R-ICS6 | `77478a91` | 92 | 10 |
| R-ICS7 | `2c51cc80` | 107 | 13 |
| R-ICS8 | `bf473e9c` | 125 | 22 |
| R-ICS9 | `7e7aa921` | 152 | 23 |
| R-ICS10 | `a2cda337` | 180 | 14 |
| R-ICS11 | `e16c88e3` | 199 | 11 |
| R-ICS12 | `558acc83` | 215 | 13 |
| R-ICS13 | `273e1dbb` | 233 | 17 |
| **R-ICS2 v2** | **`b6ddfe90`** | 255 | 29 |
| R-ICS14 | `6f9e4686` | 289 | 13 |
| R-ICS15 | `545928c0` | 307 | 23 |
| R-ICS16 | `4d0eb301` | 335 | 21 |
| R-ICS17 | `ed8d8f0c` | 361 | 27 |

### 1.1 **【重】`R-ICS2 v1` 之 sha8 已變 —— R-G13 與 R-ICS17(d) 之交互**

上繳包 01／02 所引之 `R-ICS2` sha8 為 **`ad557b5d`**；本包實測 **`4a8819f0`**。

**條文本體逐字未變**：本包以 `git show 87963f3:features/ics_management/RULINGS.md`
取出當時之 ``` 圍欄內容，與現行 `R-ICS2 v1` 之圍欄內容 `diff`，**輸出 0 行**。
變的是標題（`## R-ICS2` → `## R-ICS2 v1`）與其上新增之作廢註記區塊 ——
**正是 R-ICS17(d) 所令之作法**。

問題在於：`rulings_hash.py` 之 `body_lines` 涵蓋標題與註記（11 → 17 行），
故「**依 R-ICS17(d) 正確改題之條文，其 R-G13 指紋必然改變**」。
後果是舊包所引之 sha8 一律對不上，而 R-G13 之設計正是「sha 不符即停下」（FO §8.4）。
**此二條文之交互需要一條裁決**（§十-1）：或指紋只取圍欄內容，
或改題時於 ANOMALIES 具名記錄新舊 sha8 之對照，二者擇一。

### 1.2 前提驗證（R-DD26 v2(f)）

| # | 前提 | 驗法 | 結果 |
|---|---|---|---|
| P1 | 錨點 **17** 個 | `ledger_guard.py` ＋ `rulings_hash.py` 二法獨立實測 | **不符 —— 實測 18**。下放包 §0 P1 之括號列舉（R-ICS1、R-ICS2 v1、R-ICS2 v2、R-ICS3～R-ICS17）本身即 18 個；**其數字與其列舉不一致**，本包取列舉（＝實測值），不自行調和 |
| P2 | `ANALYSIS_LOCK.md` 存在，`holder: analysis-A`、`released: null` | `ledger_guard.py` | **相符**（一致性 OK）|
| P3 | `ANOMALIES.md` 至 A-ICS20；`DATA_REQUESTS.md` 至 DR-ICS13，13 條全開 | `ledger_guard.py`（登記列 `^\| A-ICS\d+`／`^\| DR-ICS\d+`）| **相符**（A-ICS 20 列相異 20、DR-ICS 13 列相異 13，**號段皆無缺口、無重號**）|
| P4 | 母數 2180、407 為章節數 | 作業 B 重測 | **相符** |
| P5 | b02 之 82 物件判定與「1.8.1.3 之 24 中 23 不適用」已作廢 | 作業 B 依 v2 重判 | **相符（但見 §三-2 之意外）** |

---

## §2 作業 A — `scripts/ledger_guard.py`

功能四項全實作，**不自動修復、不寫任何檔**。掃描條件寫入檔頭 docstring：
錨點取 `^## (R-ICS\d+)(?: (v\d+))?\s*$`；A-／DR- 之重號**只掃登記表之首格**
（`^\| (A-ICS\d+)`／`^\| (DR-ICS\d+)`）**而不掃內文引用** ——
內文提及同一編號屬正常，非重號；scope 檔清單自 `ANALYSIS_LOCK.md` 之
`scope:` 區塊讀出後 glob 展開（該行帶行尾註解，故不以行尾錨定，此為本包實作時撞到並修正之點）。

exit code：有 DUPLICATE 或 INCONSISTENT → 1，否則 0。

---

## §3 作業 B — CFTS020 全域 v2 重判

產出：**`docs/reports/03_cfts020_recon_v2.md`**（622 行，表格全由
`scripts/gen_recon_v2.py` 產生，非人工謄寫）。
`cfts020_probe.py` 之 `verdict_v1()` 保留並標明作廢、新增 `verdict_v2()` 與 `diffs()`，
CLI 增 `--v1`／`--diff`。**舊報告 `02_cfts020_face_recon.md` 原封保留**，新報告開頭標明取代關係。

### 3-1 六個實測值

| # | 項 | 實測 |
|---|---|---|
| (a) | v2 適用物件總數 | **254**／2180（v1 為 28）|
| (b) | `4819617` 之 v2 判定 | **適用**（ECU 軸缺、Radio 含 R1L／R1L-R、EE 含 Atlantis High）|
| (c) | `1.5` 下之 SFR 型物件 | **114 個，114 個不適用 → 仍 100% 不適用** |
| (d) | `1.8.1.1.1 {4819556}` 群 | **8 物件，6 適用** |
| (e) | `1.8.1.1.3 {4819570}` 群 | **6 物件，6 適用** |
| (f) | `1.8.1.3 {4819587}` 群 | v1「24 中 23 不適用」；**v2 亦為 24 中 23 不適用**，唯一轉變者 `4819588`（Description 型章節引言）|

### 3-2 v1 → v2 差異：**236 筆**（母數之 10.8%），全數源自 v1 之 `WARN-軸缺`

- `WARN-軸缺` → **適用**：**226 筆**（因 v2(b)(ii) 之「ECU 軸缺不再判排除」）
- `WARN-軸缺` → **不適用**：**10 筆** —— 缺的是 `Radio`／`EE`（v2(b)(i) 之必要軸），
  v1 之 WARN 於 v2 落為實質不適用。ObjectID：4819712、4819748、4819827、4819869、
  4819947、4819960、4819985、4819990、4819996、4819997
- **「軸值」原因者 0 筆**：v1 判不適用之 1916 個與判適用之 28 個，v2 下判定一律未變

全 236 筆已以 ObjectID 為鍵逐筆列於報告 §2（含三軸實值與轉變原因）。

**意外（P5 之部分不成立）**：下放包 §0 P5 稱 b02 之「1.8.1.3 之 24 中 23 不適用」已作廢，
但 v2 重判後**該數字未變**（唯一轉變者為 Description 型引言）。
「判準作廢」不等於「結論作廢」—— 本包如實回報，不自行調和。

### 3-3 R-ICS2 v2(c) 之敘述與實測之落差（不影響其結論）

v2(c) 稱「1.5 之 132 物件中 130 為 PowerNet、**餘二皆 Description 型章節引言**」。
實測：EE 恰為 `['PowerNet']` 者確為 130（相符），但 `1.5` 之 Artifact Type 分佈為
**Description 18／SFR 114** —— 「餘二」指的是 **EE 非 PowerNet 的那兩個**，
不是「1.5 只有兩個 Description」。該二為 `4819364`（`[ECU:FPDM]`，v2 判不適用，
即 v2(b)(ii) 所舉之例）與 `4819365`（Radio `R1L-R, R1L`、EE `All`、Description 型，**v2 判適用**）。
故 `1.5` 下 v2 唯一適用者是 Description 型的 4819365，**非需求物件**，(c) 之結論成立。

### 3-4 執行層之實作取捨（非裁決，須追認）

v2(b)(ii) 明文不記 WARN，故 v1 之 236 個 WARN 於 v2 全數消滅，**R-DD24 之第四欄無 WARN 可用**。
本包改以「軸齊備與否」分級：`正面命中（三軸齊備且全命中）` 28 個／
`正面命中（ECU 軸缺，依 v2(b)(ii) 不記 WARN）` 226 個／不適用者 `—`。
已於報告 §1 明文說明。若分析層要另定強度分級，請下條文。

---

## §4 作業 C — Display 面解鎖（b03，8 條）

落點 `generated/b03/b03_tcs.json`（sha256 `52d6796e…`）、`generated/b03/manifest.json`。
**E2 未觸發**（二群皆有適用物件）。

| # | tc_title | req_id | 錨 | design_method | priority |
|---|---|---|---|---|---|
| P1 | Power hardkey pressed while HU screen on | SWE-ICS-006 | CFTS020-4819560 | State Transition | P0 |
| P2 | Power hardkey pressed at Telematic Power full operation | SWE-ICS-006 | CFTS020-4819561 | State Transition | P1 |
| P3 | Power hardkey pressed while HU screen off | SWE-ICS-006 | CFTS020-4819563 | State Transition | P0 |
| P4 | Power hardkey pressed at Telematic Power idle | SWE-ICS-006 | CFTS020-4819564 | State Transition | P1 |
| S1 | Screen off hardkey starts the three second timer | SWE-ICS-007 | CFTS020-4819572 | Functional Based | P1 |
| S2 | Screen off hardkey pressed again within three seconds | SWE-ICS-007 | CFTS020-4819573 | State Transition | P1 |
| S3 | Three second period completed after screen off hardkey | SWE-ICS-007 | CFTS020-4819574 | State Transition | P0 |
| S4 | Screen off hardkey pressed while HU screen off | SWE-ICS-007 | CFTS020-4819576 | State Transition | P0 |

Test Set 一律 `Display Control`（framework 之第三個相異值）。

### 4-1 適用性之**雙路徑獨立收斂**

主實例於作業 B 完成前，自 docx 獨立以 v2(b) 判準算得
`1.8.1.1.1` 群 6/8 適用、`1.8.1.1.3` 群 6/6 適用；
作業 B 之腳本重判**得同一結果**。二路徑獨立而收於一點（R-ICS14 所述之同族情形）。
不適用之二者為 `4819557`、`4819562`，成因同為 `EE = ['PowerNet']`（實值命中失敗，非軸缺）。

### 4-2 12 個適用物件中，**4 個不生 TC**，逐一具名

| ObjectID | 不生成之理由 |
|---|---|
| 4819558 | POWER 之「是否忽略」仲裁：`based on the current combination of audio volume mute/unmute state, screen On/Off state and screen priority state`，並轉引 HMI 文件之 Note PITA4。無具體判準可寫成可判定之 ER |
| 4819571 | 同上（SCREEN OFF 側，轉引 HMI Note H4）|
| 4819559 | 音量面：`as defined in {CFTS019}`，該文件版本未確認（DR-ICS4、R-ICS11）|
| 4819575 | pop-up 期間之行為：`For the pop-ups stated in HMI core specification requirement H4`，該 pop-up 清單本 feature 未納源 |

### 4-3 訊號

- `ICSPowerButton` → **`$CLIMATIC_PANEL.Radio_btn0$`**（`BO_ 1050`，節點 **ICS**，
  `VAL_ 1050 Radio_btn0 0 "Not_Pressed" 1 "Pressed";`），備援 `DIS_CENTERSTACK.DCSD_Power`
- `ICSScreenOffButton` → **`$CLIMATIC_PANEL.Radio_btn2$`**（`BO_ 1050`，節點 **ICS**，
  `VAL_ 1050 Radio_btn2 0 "Not_Pressed" 1 "Pressed";`），備援 `DIS_CENTERSTACK.DCSD_Screen_Off`
- `$TGW_DISP_STAT$`／`$RQ_DISP_INTS$`／`$DCSD_DISP_STAT$`／`$Telematic_Power$`
  **不在作業 E 之點名清單**，依下放包 §三 C 一律 `PENDING: DR-ICS8 <…>` 佔位，不臆造。
  **建議 b04 將此四者納入 LID 驗證**（§十-4）。

### 4-4 **【須裁】三件於本批首次浮現之形式問題**

**(a) R-3 之 50 token 上限與 CFTS020 之單句長度衝突。**
`4819560`（66 token）、`4819561`（54）、`4819572`（66）三個物件皆為**單一句**，
無次句可摘。本包取其**後半獨立子句之連續逐字片段**（`then the HU shall …` 起），
依 R-4 將句首 `then` 轉大寫，前提子句改由 Pre-Condition 與括號下半承載，
全文以 `specification_reference` 指回。
逐字比對腳本已加入「句首大小寫」為第五項正規化，三條皆命中。
**此摘取法為執行層之判斷，非條文所明定。**

**(b) 方括號：8 條之 `test_item` 上半帶來源自身之記法。**
`[DISP_OFF]`、`[DISP_NORMAL]`、`[0% Intensity]`、`[current non-zero value]`、`[Idle]`。
R-S4 令上半逐字不得改字；IN §11 禁方括號但其 Exception 為 **profile-scoped**，
而**本 feature 無 profile**（`docs/runtime/profiles/` 無 ICS 檔，本包實測）。
`driver_distraction` 為同一件事開了 R-DD12。

**(c) 單引號：6 處 `'HU Screen ON'`／`'HU Screen OFF'`，同源同理。**

**本包之處置**：自檢之該二項**分流**為
「作者所書之欄位」（硬 FAIL，實測 **0**）與
「`test_item` 上半 verbatim」（**列示待裁，不自行認定合規**）。
分流之依據為 IN §11 Exception 本文：
「lint validates retained tokens against the cited source row instead of banning them」——
本包之 `verify_verbatim_b01.py` 即該 cited source row 之比對器，16/16 命中。

---

## §5 作業 D — V3 補佔位

`pre_conditions` 增第 3 行：
`3. The detent counting time window of the ICS is PENDING: DR-ICS12 <detent counting time window>`

寫為**系統組態之狀態**而非動作，以合 IN §4.4（Pre-Condition 只記狀態／環境）。
依據為 CFTS020-4819583 逐字：`the ICS shall count the relative number of detents
rotated through in <TPeriodToCountKnobDetents> seconds`。
**S1／S2／S3 與 V1／V2 一字未動**（R-ICS16）。
`b01_tcs.json` 就地修訂，`manifest.json` 之 `tcs_sha256` 重算為 `b32ec5d0…`。

**附帶複驗（作業 B 提出）**：`CFTS020-4819583` 本身之 v2 判定為**適用**
（v1 為 `WARN-軸缺`），故本佔位所依之物件錨仍成立。

---

## §6 作業 E — 8 個 LID 入 DBC（DR-ICS8 收口）

產出 `generated/b03/lid_dbc_map.json`（含 `scan_conditions` 節：自驗之表頭欄號、
二 DBC 之 sha256 實算值）與 `scripts/lid_dbc_probe.py`。

| LID | 列號 | 主路徑 | 節點 | `VAL_` |
|---|---|---|---|---|
| `ICS_KNOB1_DIR` | 1024 | `CLIMATIC_PANEL.Radio_Knob1_DIR`（BO_ 1050）| ICS | 有 |
| `ICS_KNOB1_VAL` | 1025 | `CLIMATIC_PANEL.Radio_Knob1_VAL`（BO_ 1050）| ICS | **無 `VAL_`** |
| `ICS_KNOB2_DIR` | 1026 | `CLIMATIC_PANEL.Radio_Knob2_DIR`（BO_ 1050）| ICS | 有 |
| `ICS_KNOB2_VAL` | 1027 | `CLIMATIC_PANEL.Radio_Knob2_VAL`（BO_ 1050）| ICS | **無 `VAL_`** |
| `ICSPowerButton` | 1039 | `CLIMATIC_PANEL.Radio_btn0`（BO_ 1050）| ICS | 有 |
| `ICSScreenOffButton` | 1044 | `CLIMATIC_PANEL.Radio_btn2`（BO_ 1050）| ICS | 有 |
| `Enter_Button` | 666 | `CLIMATIC_PANEL.Radio_btn1`（BO_ 1050）| ICS | 有 |
| `Back_Button` | 131 | `CLIMATIC_PANEL.Radio_btn3`（BO_ 1050）| ICS | 有 |

**E1／E4 各 0 筆**；8 個 LID 全數 `RESOLVED`，**無「未查」**。
備援一律為 `BO_ 1445 DIS_CENTERSTACK`（節點 DCSD）之對應訊號，
`Back_Button` 除外（LID 僅單名，無備援）。
方法對照：以同一腳本複驗 b02 之 `ICSMuteButton`，結論可重現。

### 6-1 二個 `_VAL` 無 `VAL_` 列舉

`BO_ 1050` 全部只有七條 `VAL_`（`Radio_btn0`～`btn4`、`Radio_Knob1_DIR`、`Radio_Knob2_DIR`）。
二個 `_VAL` 為連續量（LID `Format` 記 `6 bit signal, 0-63, resolution = 1`），
依 R-ICS8(d) 記「無 `VAL_`」，**未自造 label**。
下游若要為 knob 值寫預期值，須自 `Format` 欄取範圍，不得取 `VAL_`。

### 6-2 **綁定 DBC B（R5_FDCAN8）對本 feature 零貢獻**

`CLIMATIC_PANEL` 與 `DIS_CENTERSTACK` 於該檔 **grep 0 命中**；
八個 LID 之全部候選在 DBC B 一律「訊息不存在」。加上 b02 之 `ICSMuteButton` 亦然
（三候選全無）。**是否應繼續將 R5_FDCAN8 列為本 feature 之綁定 DBC，值得一裁**（§十-5）。

### 6-3 DBC 檔案格式之二個坑（後續腳本必讀）

1. **編碼為 ISO-8859-1（latin-1），非 UTF-8**。以 UTF-8 讀會產生替換字元；
   `grep` 在 UTF-8 locale 下無 `-a` 時**靜默無輸出**，`awk` 直接報
   `towc: multibyte conversion failure`。**「靜默無輸出」正是最危險的形態**
   —— 它看起來像「查無」。
2. **`BO_` 區塊之間沒有空行分隔**。以「空行 = 訊息結束」切塊會把後續所有訊息之
   `SG_` 全部誤掛到前一則。訊息邊界只能由「下一個 `BO_`」判定。
   嚴格界內計數：`BO_ 1050` 有 9 個 `SG_`、`BO_ 1445` 有 25 個。

---

## §7 作業 F — 二項偵察（TC 新增 0）

產出 `docs/reports/03_source_recon.md` 與唯讀腳本 `scripts/src_recon_03.py`。

### 7-1 `spec-index/sources/`：實測 **33 個檔**（32 PDF ＋ 1 XLSX），四本全部找到

| 下放包描述 | 實際檔名（**二本與描述有出入**）| sha256 前 16 | 頁數 | 文字層 | 命中頁數 |
|---|---|---|---|---|---|
| Media | `Media HMI Logic and Flow R1L-L (Febuary 9th, 2026).pdf` | `dabf34286e9de405` | 45 | 有 | 31 |
| Core | `Core HMI Logic and Flow **R1 SR24 Post 2A** (February 2 2023).pdf` | `a9d0be2f13e4c44c` | 21 | **`NO_TEXT_LAYER`** | **0** |
| Menu Bar | `Menu Bar and App Drawer **HMI Logic and Flow R1 SR24 3A** (September 11 2023).pdf` | `c917461bb610b192` | 13 | 有 | 12 |
| RVC+PAM | `RVC+PAM R1 Low SR24 1A (June 25 2021).pdf` | `d16ac02e61c20a63` | 15 | 有 | 8 |

**Core 全 21 頁純圖像，雙工具逐頁非空白字元皆 0，依約束未 OCR** ——
故 **Screen Off／電源鍵之 UI 面目次命中，本包交不出來**（預期 #11 之部分不符）。
密集區：Menu Bar p.5「App Drawer Content」單頁命中 8 個關鍵詞（含唯一之 `Screen Off` 列
與 `Backup Cam / Rear View Camera` 列）；Media p.14「Tuning Controls」、p.24「Browse Tab」、
p.33–35「Audio Settings」。

### 7-2 CFTS019 七件：**`VOLUME POP_UP` 顯示條件查無、音量階數域無明示值域**

`features/audio_mgmt/inputs/` 共 10 件，檔名含 `CFTS019`／`CFTS 019` 者確為 **7 件**
（sha256 全數入報告 §3）。

**(a) `VOLUME POP_UP` 顯示條件 —— 查無。**
字面（含 `POP-UP`／`POPUP`／`POP UP` 變體、不分大小寫）七件命中 **0**。
放寬至 `pop[ _-]?up` 家族：六件 0，僅 CFTS019 PDF 有 2 處且皆非音量彈窗 ——
p.39 §1.3.2.10.1 之 `4866125`（Teen Key 音量上限，**條文自身把顯示條件外推給 HMI 文件**）
與 p.121 §1.3.3.13 之 `4866830`（EVAS 事件結束條件）。
掃描已窮盡：xlsx 全 sheet 全 cell、docx 全 1,763 段、PDF 全 227 頁並另做去連字號重掃。

**(b) 音量階數域 —— 無明示值域宣告。**
`0-63`／`0~63`／`\b63\b`／`volume range`／`volume scale`／`max/total/number of volume`
七件全數 0 命中（PDF 唯一 `63` 是頁碼）。最相干者為 CFTS019 PDF
**§1.3.2.10 Volume Gain {4866096}（p.36 起）**，但其 `4866112` 明言
`Refer to {Radio Performance Standard} for details regarding independent volume controls.`
→ 追至件 5，其 `Analysis Report` 只說 `the volume control curve defined in TABLE 34`，
**TABLE 34 之表本體不在該 xlsx 內**，引用鏈斷。
散落之具體階數值：`volume step 20`（CAN wake-up 上限，`4866117`）、`volume step 22`
（confirmation tone 上限）、`6`／`8`／`15`、chime `± 4 steps`、SDVC `0,1,2,3`。
上界之最強間接證據為 `CFTS 019_Part2` `[Basic Report]` C17/J17（`NRL-149964`）與
C19/J19（`NRL-149966`）之 `from cabin volume 7 to cabin volume 38` ——
**38 是列舉端點，不是宣告之最大階數**，未確認即為值域上界。
**照錄一處不符（未調和）**：同列 `Description`(C) 寫 `from cabin volume 1 to cabin volume 3`，
`SYS2 System-HW`(J) 寫 `from cabin volume 0 to cabin volume 3`，**下界不一致**。

### 7-3 **`sources/` 內有一本未在點名四本之列，但最可能有答案**

`Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` ——
檔名直指 pop-up 優先權矩陣。另有 `HeadUnitCameraSystems HMI L&F …v7 (February 10th, 2023).pdf`
與 (012) RVC 相干。**二者皆不在下放包點名之四本內，本包未掃**（只記於報告附錄 A）。

---

## §8 預期數字對照（下放包 §5，12 項，相符者亦列）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | `ledger_guard.py` 開工前 | exit 0；錨點 17、A-ICS max 20、DR-ICS max 13 | exit **0**；錨點 **18**、A-ICS **20**、DR-ICS **13** | **錨點不符（§1.2 P1）**，其餘相符 |
| 2 | 重判母數 | 2180 | **2180** | 相符 |
| 3 | v2 適用數 | > 28 | **254** | 相符 |
| 4 | `4819617` v2 判定 | 適用 | **適用** | 相符 |
| 5 | `1.5` 之需求物件 | 仍 100% 不適用 | **114／114 不適用** | 相符 |
| 6 | 006 面 TC | ≥ 2 | **4** | 相符 |
| 7 | 007 面 TC | ≥ 2 | **4** | 相符 |
| 8 | b03 之 Test Set | 皆 `Display Control` | 8/8 `Display Control`（全案相異值 3）| 相符 |
| 9 | V3 之 PENDING | 1 → 2 | **1 → 2** | 相符 |
| 10 | LID 驗證 | 8 個全有判，無「未查」 | **8 個全 `RESOLVED`**，E1／E4 各 0 | 相符 |
| 11 | 作業 F | 四本目次命中 ＋ CFTS019 七件各一節；TC 新增 0 | **三本可交，Core `NO_TEXT_LAYER` 交不出**；CFTS019 七件各節齊備；TC 新增 **0** | **部分不符（§7-1）** |
| 12 | `ledger_guard.py` 完工後 | exit 0，錨點／最大號同開工前 | exit **0**，二次輸出**逐字相同**（`diff` 0 行）| 相符 |

**不符 2 項、部分不符 1 項，皆不自行調和**（另 §3-2 之 P5 意外、§3-3 之 v2(c) 落差一併具名）。

---

## §9 自檢與閘之實跑

### 9-1 `ledger_guard.py` 開工前／完工後（R-ICS17(f)）

二次輸出**逐字相同**（`diff` 0 行），exit code 皆 **0**：

```
== 1. ANALYSIS_LOCK ==   holder analysis-A / acquired 2026-08-29T14:05+08:00 / released null / 一致性：OK
== 2. RULINGS.md 錨點 ==  錨點總數 18（相異 ruling_id 17）；並存（合法）：R-ICS2 ['v1','v2']
== 3. ANOMALIES.md ==     登記列 20，相異 20，最大號 A-ICS20，號段缺口：無
== 3. DATA_REQUESTS.md == 登記列 13，相異 13，最大號 DR-ICS13，號段缺口：無
== 4. scope 檔之 sha256 / mtime ==（七檔逐一列出）
總判：OK（無 DUPLICATE／INCONSISTENT）
```

**「逐字相同」即「執行層未寫台帳」之機器證據** —— 不需要靠自陳。

### 9-2 `selfcheck_b01.py`（b01+b02+b03 合檢，**16 條**）

```
受檢批次：b01（6 條）、b02（2 條）、b03（8 條）
§9-1 Test Set                    PASS  ['Display Control','Stuck Button','Volume Control']
§9-2 tc_title                    PASS  16 條字數 [6,6,5,4,5,4,5,4,7,8,7,7,8,8,8,8]；違規 0
§4.3.1 test_item 兩段式          PASS  16 條皆有下半、皆英文；違規 0
§10.1 十鍵齊備                   PASS  缺鍵 0
§10.2 priority                   PASS  {'P0': 7, 'P1': 9}；越界 0
§10.5 procedure ≥2 步            PASS  步數 [4,6,5,4,4,4,5,5,5,5,6,5,4,5,4,5]
§9-10 Procedure↔ER 1:1           PASS  違規 0
§6 ER 無情態動詞                 PASS  命中 0
§5.1 禁用動詞（主動詞）          PASS  命中 0
§11 無尾句號                     PASS  違規 0
§11 無行首行尾空白               PASS  違規 0
§11 無方括號（作者所書之欄位）   PASS  違規 0
§11 UI 標籤雙引號（作者所書）    PASS  單引號 token 0
§10.7 spec_reference             PASS  違規 0
§12 design_method                PASS  ['Boundary Value Analysis','Fault Injection','Functional Based','State Transition']
§8.4.3 PENDING 佔位              PASS  佔位 19 處，涉 11 條
§1 交付欄無非 ASCII              PASS  命中 0
§11 方括號於 test_item 上半      MANUAL 8 條（列示，待裁）
§11 單引號於 test_item 上半      MANUAL 6 處（列示，待裁）
§11 角括號之出現                 MANUAL 21 處（PENDING 佔位語法 ＋ 來源符號）
§9-3／9-5／9-11／9-12／9-17                MANUAL

總判：PASS —— 機檢 17 項，FAIL 0；人工 8 項
```

### 9-3 `verify_verbatim_b01.py`（**16 條，來源三份**）

```
總判：PASS —— 16 條，逐字命中 16，未命中 0
```
b03 之 8 條全數命中 CFTS020；其中 P1／P2／S1 三條靠新增之第五項正規化
（R-4 句首大小寫）命中，其餘五條為原樣命中。

### 9-4 四支 gate（`gate_all.py`）

| 閘 | 開工前 | 完工後 | 差 |
|---|---|---|---|
| `lint_docs036` | PASS exit 0 | PASS exit 0 | **0** |
| `canon_refs` | FAIL：**475** | FAIL：**475** | **0** |
| `rulings_hash` | FAIL | FAIL | **0** |
| `gates_tsv` | FAIL | FAIL | **0** |
| `lint_paths` | FAIL：基線外 **2** | FAIL：基線外 **2** | **0** |

**`lint_paths` 之基線外 2 筆逐筆具名**（下放包 §7-7 要求能分辨）：
`features/driver_distraction/workbook/driver_distraction_00.xlsx` 與
`features/driver_distraction/workbook/driver_distraction_00_bak.xlsx` ——
**二筆皆屬 `driver_distraction`，`features/ics_management/` 之落點違規為 0**。
b03 之 `.json` 落 `generated/b03/`、報告落 `docs/reports/`、腳本落
`features/ics_management/scripts/`，皆合 R-ICS5。

**`canon_refs` 由上繳包 02 之 474 增為 475**，逐筆追出增加者為
**`docs/handoff/03_parallel_guard_and_display_unlock.md:88`** ——
即下放包 03 自身之 §三 D.4，其「上繳包 01 §六-2」被解析器當成 canon 節號。
**成因為分析層之下放包，非本包之產出。**

---

## §10 待分析層裁定

1. **【最重】R-G13 與 R-ICS17(d) 之交互**（§1.1）：依 (d) 正確改題之條文，
   其 R-G13 指紋必然改變（`R-ICS2 v1`：`ad557b5d` → `4a8819f0`，圍欄內容 `diff` 0 行）。
   或指紋只取圍欄內容，或改題時於 ANOMALIES 具名記錄新舊 sha8 對照。
2. **【重】ICS 之方括號／單引號例外**（§4-4(b)(c)）：IN §11 之 Exception 為 profile-scoped
   而本 feature 無 profile。是否比照 `driver_distraction` R-DD12 開一條，
   或為本 feature 立 profile。**8 條 TC 之出貨資格繫於此。**
3. **R-3 之 50 token 上限與 CFTS020 單句長度之衝突**（§4-4(a)）：
   本包之「取後半獨立子句＋R-4 轉大寫」摘取法是否採認。
4. `$TGW_DISP_STAT$`／`$RQ_DISP_INTS$`／`$DCSD_DISP_STAT$`／`$Telematic_Power$`
   四者是否納入 b04 之 LID 驗證（§4-3）。
5. `PDT27_E2A_R5_FDCAN8.dbc` 是否續列為本 feature 之綁定 DBC（§6-2，實測零貢獻）。
6. v2 下之「強度」分級（§3-4，執行層實作取捨）是否追認。
7. `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` 與
   `HeadUnitCameraSystems HMI L&F …v7` 是否納入偵察範圍（§7-3）。
8. 下放包 §0 P1 之「17」與實測「18」（§1.2）；P5 之「1.8.1.3 已作廢」與實測數字未變（§3-2）。

---

## §11 結果三分法

| 分類 | 項 |
|---|---|
| **改對了** | `ledger_guard.py`；`cfts020_probe.py` v2 化＋`gen_recon_v2.py`＋`03_cfts020_recon_v2.md`；b03 八條＋manifest；V3 補佔位；`lid_dbc_probe.py`＋`lid_dbc_map.json`；`src_recon_03.py`＋`03_source_recon.md`；自檢之方括號／單引號分流；逐字比對加入 R-4 正規化 |
| **核實無誤** | `R-ICS2 v1` 圍欄內容與 commit `87963f3` 逐字相同（`diff` 0）；LID 表頭欄號自驗與前包相符；`4819617` v2 適用（I1／I2 無需回收）；`4819583` v2 適用（作業 D 之佔位所依之錨成立）；b01／b02 之 7 個 CFTS022 錨走 v2(a) 判準未變；`ICSMuteButton` 之前輪結論以新腳本可重現 |
| **正確地不動** | 009／005 未生成（R-ICS15(b)(c)）；ignore 面未用 120 s（R-ICS9(d)）；`<TPeriodToCountKnobDetents>` 未臆值；`$TGW_DISP_STAT$` 等四訊號未查即不入 TC（依作業 C 之令佔位）；二個 `_VAL` 未自造 label；Core 無文字層未 OCR；`Pop Up List Priority Matrix` 未掃（不在點名範圍）；分析層五簿一字未寫（`ledger_guard` 前後逐字相同為證）；`02_cfts020_face_recon.md` 保留未刪；未代擬任何條文 |

---

## §12 獨立判斷

### 12-1 【下放包 §7-8 指定】Layer 2 六組於 Display 面解鎖後是否仍合 IN §4.1.3

IN §4.1.3 之判準為「filter 此 Test Set 是否得到 **meaningful cluster** —— 不只一條、
也不是整本」，健康徵候為「同一 Test Set 蘊含**共用之 setup pattern 與共用之 UI entry path**」。

現況（本包後之實數）：

| Layer 2 | RD | 現有 TC | 判 |
|---|---|---|---|
| Volume Control | 001, 002, 005 | 3 | 尚可（005 未解鎖）|
| Browse Control | 003, 004 | **0** | 待解鎖 |
| **Display Control** | 006, 007, (011) | **8** | **健康** —— 共用 setup（HU／DCSD 螢幕態）與共用 entry path（ICS 實體面板硬鍵）|
| Menu Navigation | 008, 009 | **0** | 待解鎖，且 009 已由 R-ICS15(b) 凍結 |
| Stuck Button | 010 | 5 | 健康 |
| Camera Transition | (012) | **0** | **建議重估** |

**建議（只建議不改，framework 屬分析層之簿）**：

1. **Display Control 判健康**，8 條共用同一 setup 與同一 entry path，不需再分。
   framework 現載「12 RD ≈ 2 RD/set，逼近太細門檻」之疑慮，於本組已消除。
2. **Browse Control（003/004）與 Menu Navigation（008/009）建議觀察後再議**：
   二者之母條同在 `1.8.1` 之相鄰節（`1.8.1.2 Rotary Knob Data Transfer` 與
   `1.8.1.1 Push Button Data Transfer`／`1.8.1.3 Button Press Events`），
   但 **entry path 不同**（旋鈕 vs 按鍵），依 §4.1.3 之健康徵候不宜合併。
   然若二者各自最終只落 1～2 條，即觸「每個 RD parent 各自成組」之 too-granular 形態。
   **判準應在其 TC 數確定後再套，現在合併是提早最佳化。**
3. **Camera Transition（012）建議自 Layer 2 移出或標為 out-of-scope**：
   其母文 SYSAD §4.10.1／§4.10.2 僅存目次無本文（A-ICS5），
   012 於 SWRA 需求分頁亦缺列（DR-ICS2）。
   **一個沒有 RD 在案、也沒有母文的 Test Set，filter 出來永遠是空的** ——
   這正是 §4.1.3 所謂「破壞 Test Set 欄之索引價值」的另一面。
   （作業 F 另測得 `RVC+PAM R1 Low SR24 1A` 有文字層且 8 頁命中，
   若日後納源則此組可復活；現況不成組。）

### 12-2 本包是否仍有該驗而未驗者 —— **有，五項**

1. **`VOLUME POP_UP` 之 6 行 ER 仍無來源**（上繳包 01 §八-3 起連續三包具名）。
   本包窮盡 CFTS019 七件仍查無，且 `4866125` 顯示 **CFTS 層一律把彈窗顯示條件外推給
   HMI 文件** —— 答案很可能根本不在 CFTS 系列。而 `sources/` 內正有
   `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf`（§7-3），
   不在點名四本內故未掃。**這是三包以來最接近答案的一次，但被範圍擋住。**
2. **Core HMI L&F 無文字層**（§7-1）：Screen Off／電源鍵之 UI 面對照這次交不出來，
   而 b03 之 8 條**正是**該面。目前 8 條全靠 CFTS020 之訊號面，
   **UI 面（"TOUCH SCREEN TO TURN ON" 圖形之實際樣貌與位置）無第二來源可校**。
3. **`$RQ_DISP_INTS$ = [current non-zero value]` 之「current」不可絕對判定**：
   P3／P4／S2／S4 四條之 ER 因此只斷言 `$TGW_DISP_STAT$` 與畫面回復，
   未斷言亮度值。**該四條對亮度面之驗證強度為零**，已於各條 reasoning 具名。
4. **CFTS019 之引用鏈有 5 個斷點文件不在七件內**（TABLE 34、HU Component Specification、
   未具名之 HMI 文件、CIP Radio DSPPP 表、`Table for CFTS019-4866516`），
   已列於作業 F 報告 §6.4。**是否另開 DR 未決。**
5. **`Enter_Button`／`Back_Button` 之訊號已解（作業 E）但其行為面仍凍結**
   （008 待 DR-ICS6 之 HMI L&F、009 待 DR-ICS13 之市場軸）。
   **訊號解了而行為面沒解 —— 這兩件事不可互相充當。**

---

## §13 未結 DR 清單

**DR-ICS1 ~ DR-ICS13，13 條全開。** 本包之新事實：

| DR | 新事實 |
|---|---|
| DR-ICS1 | 006／007 已由 R-ICS15(a) 繞過，**其阻斷面縮為 005** |
| DR-ICS2 | (012) 之 Test Set 建議重估（§12-1-3）|
| DR-ICS4 | CFTS019 七件實測**查無** `VOLUME POP_UP` 顯示條件與音量階數域（§7-2）；DR 內容建議改為「請指明其所在文件」而非「請提供 CFTS019」|
| DR-ICS6 | 003／004／008 之 CFTS020 母條已定位（`1.8.1.2`／`1.8.1.1`／`1.8.1.3`）；Media 與 Menu Bar 二本 HMI L&F 有文字層且命中密集（§7-1），**DR 之範圍可縮** |
| DR-ICS8 | **9/9 個 LID 全數解出**（b02 一個 ＋ 本包八個）。但 `$TGW_DISP_STAT$` 等四訊號未在點名清單，b03 有 14 處佔位待其解 —— **DR 不宜逕結** |
| DR-ICS10 | b02 二處佔位待其回覆 |
| DR-ICS12 | b01 之 V3 新增一處佔位待其回覆（§5）|
| DR-ICS13 | 009 之凍結繫於此（§12-2-5）|
| DR-ICS3／5／7／9／11 | 無新事實 |

---

## §14 本包引用之編號清單

R-ICS1 `3e48552b`、**R-ICS2 v1 `4a8819f0`**、R-ICS3 `b10318e0`、R-ICS4 `85de9871`、
R-ICS5 `e6a4790d`、R-ICS6 `77478a91`、R-ICS7 `2c51cc80`、R-ICS8 `bf473e9c`、
R-ICS9 `7e7aa921`、R-ICS10 `a2cda337`、R-ICS11 `e16c88e3`、R-ICS12 `558acc83`、
R-ICS13 `273e1dbb`、**R-ICS2 v2 `b6ddfe90`**、R-ICS14 `6f9e4686`、R-ICS15 `545928c0`、
R-ICS16 `4d0eb301`、R-ICS17 `ed8d8f0c`；
A-ICS1、A-ICS5、A-ICS12、A-ICS13、A-ICS14、A-ICS15、A-ICS17、A-ICS18、A-ICS19、A-ICS20；
DR-ICS1 ~ DR-ICS13；
R-G13、R-G18、R-G23、R-G25；R-DD4、R-DD9、R-DD10、R-DD12、R-DD13、R-DD23、R-DD24、
R-DD25、R-DD26 v2；R-TM13；R-BLM11；R-P96；
FO §8.1、FO §8.2、FO §8.4、FO §8.5、FO §8.8；
IN §4.1.3、IN §4.1.4、IN §4.3、IN §4.3.1、IN §4.4、IN §5.1、IN §5.6、IN §5.7、
IN §8.2.2、IN §8.3、IN §8.4.1、IN §8.4.3、IN §8.6、IN §8.7.5、IN §9、IN §10.7、
IN §11、IN §12。

**本包未產生任何新裁決條文**（執行層不代擬）。
建議登錄之 anomaly 六則（編號由分析層取，落檔亦由分析層為之 —— 本包依 R-ICS17(a)
不寫台帳，亦未於 `docs/handoff/proposals/` 落提案，因本包無「擬增之條文全文」可提，
僅有待裁之問題）：
§1.1（R-G13 與 R-ICS17(d) 之交互）、§4-4(b)(c)（方括號／單引號之 profile 缺口）、
§4-4(a)（R-3 與 CFTS020 單句長度之衝突）、§6-2（R5_FDCAN8 零貢獻）、
§6-3（DBC 之 latin-1 與無空行分隔，靜默無輸出之風險）、
§7-1（Core HMI L&F 無文字層）。
