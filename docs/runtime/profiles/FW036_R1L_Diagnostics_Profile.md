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
（Camera／VehicleCategory profile 皆已實測並記錄同一事實）。故 §2–§5 之
新檢查項 **必須另行實作於 `lint036.py`** 才會生效，不會因寫在本檔而自動啟用。
本包止於 Phase 0–1，**尚未實作任何一項**。

---

## 2. `[ADD]` UDS 記法（R-DIAG5）—— **待實作**

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

## 3. `[ADD]` Requirement ID 欄單值檢查（R-DIAG1(a)）—— **待實作**

- 工作簿 `Requirement or Design ID` 欄**每列只得一個 SWE1 ID**，不得逗號／換行並列。
- 接受形式：`SWE1-Diagnostics-{nnn}`，以及 R-DIAG2 之
  **`SWE1-Diagnostics-340-001`／`SWE1-Diagnostics-340-002`** 兩個三段式號。
- 反向檢查：394 個唯一 ID（含上述二號）於全工作簿之覆蓋，缺者列 coverage 未覆蓋；
  `SWE1-Diagnostics-057` 以 `OUT_OF_SCOPE` 計，**不計入未覆蓋**（R-DIAG3）。

---

## 4. `[ADD]` Vehicle Model 七欄檢查（沿用 R-CAM2 條文）—— **待實作**

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

## 5. `[PEI]` Layer 2 Test Set（21 組草案）

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

## 6. `[ADD]` Remarks 欄格式檢查 —— **待實作**

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
| 3 | 五項 lint 之校準 —— CDD-02 pilot（14 列）＋ CDD-03 batch 1（47 列）實跑，**真違規 0**；`P-DIAG`／`U-DIAG`／`R1-DIAG`／`Z`／`RM-DIAG` 皆 0 | **已校準** |
| 4 | `docs/fw036/RULINGS.sha.tsv` 僅含 security 32 列而自稱全域檔（`--check` 動工前即 FAIL）| **全域待辦**，`[A-DIAG15]` |
| 5 | `new_feature.py` 之 `feature[:2]` ABBR 缺陷 | **全域待辦**（審閱 §五-6，不阻斷）|
