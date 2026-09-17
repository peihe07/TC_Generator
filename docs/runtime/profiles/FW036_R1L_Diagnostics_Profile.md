# FW036 R1L Diagnostics — Profile（骨架）

- 設立依據：下放包 **CDD-01 §4 任務 5**（`docs/fw036/handoff/down/20260917_CDD-01.md`）；
  **CDD-01_A 依 R-DIAG3/5/7/8/9(amend) ＋ R-G73／R-G74 更新**（`down/20260917_CDD-01_A.md`）。
- 命名依既有慣例（CamelCase 無分隔，同 `VehicleCategory`／`PowerModing`）。
- 本檔為 **Phase 0–1 之骨架**：只寫已有實測依據者，未鎖定之項一律標
  `[PROPOSED]` 或 `[PEI]`，不預先設計未來條款。
- **母體標註**：本檔凡引用計數必標母體，限下列六者（**CDD-01_A 起以 037 V1 (3) 為母體**，
  R-DIAG8(amend)）—— 037 `389 列`（唯一 SWE1 ID `388`）／037 來源 `166 項`（解析 `166`，100%）／
  CFTS004 索引 `404 列`／CFTS004 `$XXXX` Heading `63`（被引用 `42`）／
  negative＋unsupported `226 列`／Layer 2 `20 組`。

---

## 0. 適用範圍

| 項 | 值 | 權威 |
|---|---|---|
| feature | `Diagnostics` | CDD-01 §4 任務 1 |
| slug | `diagnostics` | 同上 |
| `test_group`（工作簿 G 欄）| `Diagnostics` | **R-DIAG9(a)** |
| Layer 2 Test Set（H 欄）| **20 組**（R-DIAG9(amend)(b)：#11 併入 #14）| **[PEI]** 名稱歸 Pei，見 §5 |
| ABBR（TC ID `NR1L-{ABBR}-{nnn}`，R-G42）| `DIAG` | **R-DIAG9(a)** |
| `spec_reference`（N 欄）| `CFTS004-{ObjectID}` 錨（IN §10.7(a)）；ObjectID 空值 `0` | 本包實測 |
| 產出母體 | 389 列 − 1（Out of Scope，R-DIAG3）= **388 列** | CDD-01_A 實測 |
| spec_mode | **[PROPOSED] `D`** 待 `intake.py` 判定 | — |

---

## 1. lint 啟用（R-G70／R-G71）

依 R-G71，新 feature 之 profile **一律啟用 `X` 與 `P`(v4)**。
`P=0`／`X=0` 在未啟用時是沉默，不是核可。

| 代號 | 現行標題 | 本 profile |
|---|---|---|
| `P` | 訊號寫法不合 R-1 v2（profile 下判準為 R-G70 v4.1）| **啟用** |
| `X` | 導航路徑無固定入口（§5.8／R-G71）| **啟用**（WARN 只報不改）|
| `Y` | PROXI 舊式 | 隨 `P` 連動 |

呼叫形式：`python scripts/lint036.py --profile diagnostics <xlsx…>`。

**現況如實回報**：`lint036.py` 之 `--profile` 只作真值使用，不讀本檔內容
（Camera／VehicleCategory profile 皆已實測並記錄同一事實）。故以下各節之
新檢查項 **必須另行實作於 `lint036.py`** 才會生效，不會因寫在本檔而自動啟用。

### 1.1 feature 專屬檢查（`FEATURE_CHECKS["diagnostics"]`）—— **七項全數已實作**

| 代號 | 判準 | 出處 | 立於 | 校準 |
|---|---|---|---|---|
| `P-DIAG` | `$XXXX` 白名單（36 種，`layer3_assign.tsv` 之 DID 集合）| R-DIAG5(a) | CDD-01_A | **已校準** |
| `U-DIAG` | UDS 位元組串每 byte 兩位大寫 hex、單空格；`7F` 後兩 byte 必接 `(<label>)` | R-DIAG5(b)／(amend)(d) | CDD-01_A | **已校準** |
| `R1-DIAG` | Requirement ID 單值 `SWE1-Diagnostics-nnn(-001/-002)`；`-340` 裸號違規 | R-DIAG1(a)／R-DIAG2 | CDD-01_A | **已校準** |
| **`Z`** | Vehicle Model 七欄 1／0；598／5210 = 0；五有效欄至少一 `1` | R-CAM2／**R-G74** | 承接 Camera | 已校準 |
| `RM-DIAG` | Remarks 五種定型句（多句以 `; ` 接合）| R-DIAG3(amend)／6／7(a)／5(amend) | CDD-01_A | **已校準** |
| `SEC-DIAG` | I/O Control（`0x2F`）之 TC 須含 PC `Security access 0x27 has been granted`；**unsupported 型不在母體**（R-DIAG13(amend)）| R-DIAG13／(amend) | CDD-04 | **已校準** |
| `KEY-DIAG` | `$1820`／`$1821` 之觸發鍵不得為 Power／Dark | R-DIAG14 | CDD-04 | **已校準** |
| `PC-DIAG` | Pre-Condition 只述狀態 —— 不得含 record／read／measure／send／press 等動作詞；否定式之靜止態（`No … is pressed`）例外 | R-DIAG18 | CDD-06 | **已校準** |

**`VM-DIAG` ≡ `Z`**：下放包書 `VM-DIAG`，其判準逐字即 R-CAM2(a)(b)(c)，
與既有 `Z` 完全相同，且 R-G74 已將 598／5210 升為全域 —— 另立代號即為同一判準之第二份實作。

**`SEC-DIAG`／`KEY-DIAG` 之母體依母節反查**（CDD-04 追補 A §一），**不依 Procedure 有無位元組串** ——
pilot `-006` 之觸發步驟曾整行為 `PENDING`，無 `2F` 串而仍屬 `0x2F` 之 TC。
實作為 `lint036.py` 之 `DIAG_IO_ROWS`（114 列）／`DIAG_KEY_ROWS`（7 列）號段常數。

### 1.2 列級豁免（R-DIAG11）與整項豁免（R-DIAG12）

- **列級**：`AF` Test Result = `Out of Scope` 之列豁免 `I`／`M`／`R`／`Z`；
  `R1-DIAG`／`RM-DIAG` 仍檢。實作為 `ROW_EXEMPT_OOS`（列級，非整項）。
- **整項**：`I-cross` 入 `FEATURE_EXEMPT["diagnostics"]`，比照 R-SEC15(j)。

### 1.3 自測

`features/diagnostics/scripts/selfcheck_lint_diag.py` —— **九項，各 5 正例 ＋ 5 反例**。
實跑校準母體：pilot01（14 列）、batch 1（47 列）、batch 2（81 列）、合併本（133 列）。

### 1.4 寫入型 TC 不立 baseline

`[A-DIAG30]`／`[A-DIAG35]`／`[A-DIAG37]`（同一缺陷已**三犯**）：驗證對象為
「寫入值 ↔ 讀回值」時，初值不入 ER，於 Pre-Condition 宣告 `*_initial`
即為 §8.5 之多餘前提。**canon §9-9 自檢可攔，lint 無此判準。**

**CDD-05 起以產生器守門**：`gen_batch{1,2,3}.py` 於產出前自檢
「`*_initial` 出現於 PC 或 Procedure 而未出現於 ER」，命中即 `SystemExit`，不出檔。
三犯之後不再靠事後自檢。

### 1.5 R-4 —— verbatim 上半之句首大寫

canon §4.3.1 末句：verbatim 自原句中段起抄時，句首字母轉大寫屬**排版正規化**。
037 `-048` 之 Description 原文為 `1)when tester command…`，去編號後以小寫起首；
`test_item` 上半依 R-4 轉大寫，**lint `J` 不豁免**。產生器於組 `tc_title` 時結構性套用。

### 1.5a R-DIAG21 —— 上半摘句（`L` 之閾值為 canon 明文，非「待定」）

**canon §4.3.1 之 R-3 = 50 tokens，是明文上限，不是待校準之暫定值。**
`lint036.py` `CHECK_STATUS["L"]` 原書「閾值待 R-3」，已據 CDD-07 審閱 §三-2 更正為
「已校準（R-3 = 50，canon §4.3.1；超限依 R-DIAG21 摘句）」。

上半 > 50 tokens 者**不得**以「來源逐字、不可改」為由留置 —— R-DIAG4(a) 之 verbatim
要求的是「所抄之字不改寫」，不是「必須抄完整句」。處置為**摘句**：
取與括號下半測試目的直接相關之句或子句，逐字照抄不改寫，其餘以
`specification_reference` 指回原錨。自原句中段起抄者，句首依 R-4 轉大寫。

實例（CDD-08 T1(c)，8 條）——
原：`If retries are performed as shown on the flowchart, and the retries are the result of
three identical instances of Indication Codes $03, $0D, or $0F, then the HU shall provide
the respective code $03, $0D, or $0F in the routine results.`（52 tokens）
摘：`The retries are the result of three identical instances of …`（≤ 50）——
刪去之「as shown on the flowchart」為流程圖指引（DR-DIAG-8 缺件），與本條測試目的無關。

產生器守門第四條：上半 > 50 tokens 即 `SystemExit`，token 口徑與 `lint036.RE_TOKEN` 同。

### 1.6 R-DIAG16 —— 觀察不成步

Procedure 只寫動作（送出／按壓／保持／讀取）；聽、看、觀察只入 ER。
保持步驟固定句 `Hold for <n> s`，ER 寫該期間之可觀察結果。
CDD-05 依此改 **16 行／13 條**（`Listen to …` 全數移入 ER）。

### 1.8 Pre-Condition 之機械守門（R-DIAG18）

`*_initial` **只得於 Procedure 宣告**（IN §8.7.5(f) 式：
`n. Read <對象> and record as <Name>_initial` ＋ `$ 22 xx xx`，ER-n `<Name>_initial is recorded`），
不得寫入 Pre-Condition。四個產生器與 lint `PC-DIAG` 各設一道守門；
兩道合計攔下之缺陷：CDD-05 之 148 行位置錯置、CDD-06 產出時之 6 條漏網。

**否定式例外**：`No push button … is pressed` 為靜止態，不需執行即成立，不算動作詞。

### 1.7 ~~`X` 之結構性誤報~~ **已解**（R-DIAG17）

`X` 為 WARN（只報不改）。本 feature **不寫導航 hop** —— HMI 入口不在其範圍，
其命中皆為 DID 名與 CFTS004 用詞之字面（`Radio Audio Output **Settings**`、
`in-motion **menu** options`）。batch 3 實測 **12 行**，真違規 0。
已依 **R-DIAG17** 列入 `FEATURE_EXEMPT["diagnostics"]`。

> **落地時揭出 lint 之實作缺陷（`[A-DIAG42]`）**：`X` 於 `check_row()` 內產生，
> 而 `FEATURE_EXEMPT` 只從 `check_order()` 移除 —— 豁免後該代號仍被產出卻已不在
> `enabled`，`enabled.index()` 拋 `ValueError`，290 列之合併本直接 crash。
> 已改為 `check_row()` 之產出一律依 `enabled` 過濾，**列級豁免與整項豁免收斂為同一道**。

---

## 2. `[ADD]` UDS 記法（R-DIAG5）—— **已實作**（`P-DIAG`／`U-DIAG`）

### 2.1 敘述層（`test_item` 上半、`pre_conditions`、`expected_result` 散文）

- DID 一律 `$XXXX`（四位 hex，無尾 `$`）：`DID $283F`。
- `$XXXX` 無尾 `$`，**不受 lint `P`（`$MESSAGE.Signal$`）規制** —— 實作時須於 `P`
  之判準加白名單，否則 037 之 27 種 `$XXXX` token 會全數誤報。
- 037 混寫之 `0x283F` 於 `test_item` 上半 verbatim 照抄（R-DIAG4(a)）；
  作者側四欄一律 `$`。實測：037 之 `$XXXX` 27 種 232 次、`0xXXXX` 23 種 94 次，
  **同列並存 74 列**——照抄與正規化之界線必須逐欄判別，不得全檔取代。

### 2.2 執行層（`test_procedure`）

位元組串式，與 security 批次之 UDS 通道同式：

```
2. Send UDS request 22 28 3F via diagnostic tool
3. Check that positive response 62 28 3F <brightness byte> is received
```

**lint 判準**：
- 位元組串每 byte **兩位 hex、空格分隔**、大寫。
- `7F` 後必接兩 byte，再接 `(<label>)`：`7F 22 31 (Request Out of Range)`。
- label 逐字取 CFTS004 用字（R-DIAG5(b)）。

### 2.3 ~~`[BLOCKED]`~~ **已解** SID／NRC 值之來源 —— R-DIAG5(amend)

R-DIAG5(c)「以 CFTS004 原文為準；原文未載者寫 `PENDING: DR-{n}`，
不得引 ISO 14229 通用表補值」。本包實測其適用結果：

**R-DIAG5(amend)（Pei 2026-09-17）落地後**（V3 母體 226 列）：

| 分類 | 列數 |
|---|---:|
| `RESOLVED_CFTS004` | 5 |
| `RESOLVED_037` | 20 |
| `RESOLVED_ISO`（五碼，037 已述失效型態）| **198** |
| `PENDING_DR1` | **3** |

I/O Control SID `0x2F` 依 (e) 全數 `RESOLVED_037`（114 列：24 列直接明載 ＋ 91 列同 DID 類推）。
`U-DIAG` 之 `7F <SID> <NRC> (<label>)` 檢查**已可啟用**。逐列見 `data/nrc_coverage.tsv`。

---

## 3. `[ADD]` Requirement ID 欄單值檢查（R-DIAG1(a)）—— **已實作**（`R1-DIAG`）

- 工作簿 `Requirement or Design ID` 欄**每列只得一個 SWE1 ID**，不得逗號／換行並列。
- 接受形式：`SWE1-Diagnostics-{nnn}`，以及 R-DIAG2 之
  **`SWE1-Diagnostics-340-001`／`SWE1-Diagnostics-340-002`** 兩個三段式號。
- 反向檢查：394 個唯一 ID（含上述二號）於全工作簿之覆蓋，缺者列 coverage 未覆蓋；
  `SWE1-Diagnostics-057` 以 `OUT_OF_SCOPE` 計，**不計入未覆蓋**（R-DIAG3）。

---

## 4. `[ADD]` Vehicle Model 七欄檢查（沿用 R-CAM2 條文）—— **已實作**（`Z`）

判準逐字承接 `features/camera/RULINGS.md` R-CAM2：

- (a) 七子欄每列填 `1` 或 `0`，不留空、不用其他符號。七欄為
  `HDCC27 Atl-Hi`／`DT27 Atl-Hi`／`VF(ProMaster)637 Atl-Mi`／
  `Commander (598) Atl-Mi`／`Regengade (5210) Atl-Mi`／`Toro(2261) Atl-Mi`／
  `Fastack (376) Atl-Mi`。
- (b) `Commander (598)`／`Regengade (5210)` 兩欄一律 `0`。
- (c) 其餘五欄每列至少一個 `1`。

**本 feature 之 [ADD]**（R-DIAG7(b)，歸屬表見 `data/vehicle_model_region.tsv`）：

| CFTS004 Region | HDCC27 | DT27 | 637 | 598 | 5210 | 2261 | 376 | 037 列數 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---:|
| `All`（89 源）| 1 | 1 | 1 | 0 | 0 | 1 | 1 | **206** |
| `NAFTA` 系（78 源）| 1 | 1 | 1 | 0 | 0 | **0** | **0** | 182 |
| （空，1 源）| — | — | — | — | — | — | — | 1（Out of Scope，不產 TC）|

依據為 PROXI `Market_Area`（byte 160）逐平台實測，同 R-CAM5(c)′ 之證據型態：
HDCC28/DT28/Promaster = `0 (NAFTA)`；Toro/Fastback = `2 (LATAM)`。
**已裁**：R-DIAG7(amend)（Pei 2026-09-17）。598／5210 之 `0` 另由 **R-G74** 升為全域。

---

## 5. `[PEI]` Layer 2 Test Set（**20 組**，R-DIAG9(amend)(b)）

CDD-01 §5 之 21 組草案經 CDD-01 逐列驗算 **21/21 吻合（V2 母體 395）**；
**R-DIAG9(amend)(b)** 裁定 #11 `Audio Output Settings`（`$180C`）併入 #14 `Audio Tone Settings`，
Layer 2 定為 **20 組**。V3 母體下合計 **389**，逐列歸屬見 `data/layer2_assign.tsv`，
框架文件見 `features/diagnostics/docs/framework.md`（狀態 `DRAFT`）。

§4.1.3 決策測試（V3、20 組）：
- **#20 `Clear Key Sense PIN`（`$030A`）= 1 列** —— §4.2 genuine outlier，R-DIAG9(amend)(b) 裁定維持獨立。
- 4 列以下者：#10（`$1801`，4 列，實產 **3**）／#17（`$500D`+`$5100`，5 列）／#19（`$031B`，3 列）。
- 無 > 80 者（最大 #2 `SXM Signal Quality` = 72）。
- #5 `GPS Signal Data` 因 V1 (3) 刪列由 40 → **34**。

Layer 2 之 **20 組名稱**仍歸 Pei（framework.md Part IV）。

---

## 6. `[ADD]` Remarks 欄格式檢查 —— **已實作**（`RM-DIAG`）

| 情形 | 固定句式 | 母體 |
|---|---|---|
| CFTS004 `HARMAN Status` 非空（R-DIAG7(a)）| `Harman Scope: <status 原字>` | 58 源（Need Rework 55／Accepted 2／Need Clarification 1）|
| Out of Scope（R-DIAG3）| `CFTS004 Category: Out of Scope` | 1 列 |
| 037 VM 空白（R-DIAG6）| `037 VM blank; procedure derived from Description + CFTS004` | 4 列（SWE1-189～192）|

`<status 原字>` 之合法值域限上列三者，逐字比對，不得改寫大小寫。

---

## 7. 未決項（本包不鎖定）

CDD-01 之六項已於 CDD-01_A 全數處置：

| # | 項 | 處置 |
|---|---|---|
| 1 | R-DIAG5(c) 之 NRC／SID 適用空白 | **已解** R-DIAG5(amend)；殘 3 列 → DR-DIAG-1（非阻斷）|
| 2 | Region → Vehicle Model 歸屬表 | **已裁** R-DIAG7(amend) |
| 3 | 單列 Test Set 之合併 | **已裁** R-DIAG9(amend)(b) |
| 4 | Out of Scope 列之處置欄位名 | **已裁** R-DIAG3(amend)：`AF` `Test Result 測試結果` |
| 5 | Layer 2 名稱 | **[PEI]** 仍未逐字簽核 |
| 6 | `R-DIAG` 四字母前綴 | **已解** R-G73（正則放寬為 `{0,4}`）|

CDD-01_A 後之未決項：

| # | 項 | 去向 |
|---|---|---|
| 1 | Layer 2 之 20 組名稱 | **[PEI]**，framework.md Part IV |
| 2 | `PENDING_DR1` 3 列之 NRC（`-156`／`-157`／`-237`）| DR-DIAG-1 |
| 3 | **八項** lint 全數已校準（CDD-02 14 列／CDD-03 47／CDD-04 81／CDD-05 99／CDD-06 61 實跑，真違規 0）| 見 §1.1 |
| 6 | ~~`J`~~／~~`SEC-DIAG`~~／~~`X`~~ 三項判準待調**全數已解**（R-4／R-DIAG13(amend)／R-DIAG17）| 無未決 |
| 4 | `docs/fw036/RULINGS.sha.tsv` 僅含 security 32 列而自稱全域檔（`--check` 動工前即 FAIL）| **全域待辦**，`[A-DIAG15]` |
| 5 | `new_feature.py` 之 `feature[:2]` ABBR 缺陷 | **全域待辦**（審閱 §五-6，不阻斷）|
