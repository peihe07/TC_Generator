# 下放包 04 — profile 落檔、四訊號解佔位、Browse／Navigation 面（2026-08-29）

> **引用體例變更（A-ICS27③）**：本包起，引上繳包節號一律寫 `upstream-NN §x`，
> 不寫「上繳包 NN §x」——後者會被 `canon_refs` 解析器誤判為 canon 節號。

## §0 背景與量測時點

upstream-03 已審結，b03 八條收下。分析層即裁 **R-ICS18～R-ICS21**，
登 **A-ICS21～A-ICS27**，新開 **DR-ICS14／DR-ICS15**，
`framework.md` 改二列（Display Control 判健康；Camera Transition 轉 out-of-scope-pending）。

**本包前提之量測時點為 2026-08-29 15:0x。** 執行前依 R-DD26 v2(f) 先驗。

| # | 前提 | 驗法 |
|---|---|---|
| P1 | `RULINGS.md` 之錨點：**相異 ruling_id 21，錨點總數 22**（`R-ICS2` 有 v1／v2 二列）| `ledger_guard.py` |
| P2 | `ANOMALIES.md` 至 **A-ICS27**；`DATA_REQUESTS.md` 至 **DR-ICS15**，15 條全開 | `ledger_guard.py` |
| P3 | `ANALYSIS_LOCK.md` `holder: analysis-A`、`released: null` | `ledger_guard.py` |
| P4 | b03 八條之出貨資格已由 R-ICS18 解鎖 | 讀 R-ICS18 |

**開工第一件事**：重測本檔 sha256 並入 upstream-04 §0（R-ICS17(e)）；
**第二件事**：跑 `ledger_guard.py`，報 DUPLICATE／INCONSISTENT 即停（E1）。

## §1 禁區

沿下放包 03 §1 全部七項，不變。特別重申：
`ANALYSIS_LOCK.md` 與分析層四簿、`docs/handoff/**` 一字不得寫；
009／005 之 TC 仍為 0（R-ICS15(b)(c)）；`<Tstuck_button>`、
`<TPeriodToCountKnobDetents>`、`SIS-5161` 之電壓一律不臆值。

**本包新增禁區第 8 項**：`docs/runtime/profiles/FW036_R1L_ICS_Profile.md`
之內容**逐字取 R-ICS18(a)(b)(c)**，不得改寫、不得增補己意——
執行層落檔，但不是條文之作者。

## §2 裁決引用（sha8 由執行層實測填實；`R-ICS2` v1／v2 並列）

| 條 | 本包用於 |
|---|---|
| R-ICS18 | 作業 A（profile 落檔）；b03 八條之自檢改判 |
| R-ICS19 | §2 之 sha8 比對程序：不符時先取圍籬 diff，0 行則不停 |
| R-ICS20 | 作業 C 之 verbatim 摘取法 |
| R-ICS21 | (a) DBC 綁定註記／(b) 強度分級／(c) 偵察範圍 |
| R-ICS2 **v2** | 作業 C 之適用判準（v1 一律不得再用） |
| R-ICS8／13／14 | 作業 B 之 LID→CAN 路徑與取捨 |
| R-ICS15(b)(c) | 009／005 之凍結 |

## §3 作業清單

### 作業 A — profile 落檔（R-ICS18(e)）

1. 落 `docs/runtime/profiles/FW036_R1L_ICS_Profile.md`，內容逐字取 R-ICS18(a)(b)(c)，
   標 cited `[OVERRIDE IN §11]`，體例比照既有 profile 檔（先讀一本現存者定體例）。
2. `selfcheck` 之方括號／單引號二項：上半 verbatim 之列示改判 **PASS**（R-ICS18(d)），
   作者欄位維持硬 FAIL。改後重跑 16 條合檢。
3. `feature.yaml` 增 `profile` 欄指向該檔（sha256 自實體檔算）。

**此作業牽涉 `docs/runtime/` —— 屬全域目錄。** 落檔前先跑 `lint_paths.py`
取基線，落檔後再跑；若基線外數增加，停下回報（E2），不自行加入基線。

### 作業 B — 四訊號 LID→CAN（DR-ICS15）

`$TGW_DISP_STAT$`／`$RQ_DISP_INTS$`／`$DCSD_DISP_STAT$`／`$Telematic_Power$`，
依 R-ICS8＋R-ICS13 逐一：LID v1_78 `Atlantis High` 欄 → 二 DBC 存在性與 `BO_` 發送節點
→ 取捨（節點 = ICS 為主路徑）→ `VAL_` 逐字（無列舉者記「無 `VAL_`」）。

- **DBC 讀取必依 A-ICS25**：以 `latin-1` 開檔；訊息邊界以下一個 `BO_` 判定。
  以 UTF-8 讀而得「查無」者一律視為未查。
- 解出者回改 b03 之 14 處佔位；查無者**維持佔位**並於 DR-ICS15 具名。
- 輸出併入 `generated/b04/lid_dbc_map.json`（含 b03 之八個，累計對照表）。

### 作業 C — Browse／Navigation 面（008 解鎖，003／004 視偵察）

**前置**：依 R-ICS2 v2 判 `1.8.1.2 {4819577}` 群與 `1.8.1.1 {4819542}`／
`1.8.1.3 {4819587}` 群之適用物件。upstream-03 §3-1(f) 實測 `1.8.1.3` 之 24 中 23 不適用
——**此為 v2 下之結果，不是舊判準之殘留**（A-ICS27②）。故：

1. **008（`Enter_Button`）**：其直載原句為 `4819555`。判其 v2 適用即生成；
   不適用則停下回報（E3），不得改錨他物件。
2. **003／004（knob2）**：`1.8.1.2` 群之適用物件逐一列出後生成。
   `4819583` 之 `<TPeriodToCountKnobDetents>` 一律 `PENDING: DR-ICS12 <…>`。
3. **009 不生成**（R-ICS15(b)，DR-ICS13 未回）。
4. **`1.8.1.3` 之 23 個不適用物件**：若其中含「按壓事件之定義」（Short／Long Press）
   而 008／003／004 之 TC 需要該定義，**不得自他處補**——具名回報為覆蓋缺口
   （upstream-03 §12-2-5 已預示）。
5. Test Set：008 → `Menu Navigation`；003／004 → `Browse Control`。
6. verbatim 逾 R-3 者依 **R-ICS20** 摘取，(c) 之三項限制須逐條自檢。

### 作業 D — 二本新納偵察（R-ICS21(c)）

`Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` 與
`HeadUnitCameraSystems HMI Logic and Flow R1 SR24 Post 2A v7 (February 10th, 2023).pdf`：

1. 頁數、文字層有無（`NO_TEXT_LAYER` 者不 OCR）、sha256。
2. **Pop Up List**：`VOLUME POP_UP`／`volume` 相關之目次與命中頁
   ——此為 upstream-03 §12-2-1 所指「三包以來最接近答案」之一本。
3. **HeadUnitCameraSystems**：(012) rear camera transition 相關之目次與命中頁。
4. **只列章節與命中，不判採用、不充 verbatim 來源、不充錨**（R-ICS21(c)）。

## §4 掃描條件

沿 upstream-03 §0 全部條件（含第五項正規化：句首大小寫）。另：

| 項 | 條件 |
|---|---|
| DBC 讀取 | `latin-1` 開檔；訊息邊界由下一個 `BO_` 判定（A-ICS25）。以 UTF-8 讀得之「查無」不算數 |
| LID 表頭 | 每次自驗，不沿用前包欄號 |
| v2 判準 | (i) `Radio ∈ {R1L, R1L-R, allSys}` ∧ `EE ∈ {Atlantis High, All}`；(ii) `ECU` 軸存在時須含 `{ICS, LTM}`，不存在時不判不適用亦不記 WARN |
| 強度分級 | R-ICS21(b) 之三級，二級命中須可區別 |
| PDF | `pdftotext` ＋ `pdfplumber` 雙工具逐頁；另做去連字號重掃 |
| profile 體例 | 先讀一本現存 profile 定體例，於 upstream-04 §0 載明所讀何本 |

## §5 預期數字（相符者亦列）

| # | 項 | 預期 |
|---|---|---|
| 1 | `ledger_guard.py` 開工前 | exit 0；錨點總數 22（相異 21）、A-ICS max 27、DR-ICS max 15 |
| 2 | profile 檔 | 1 個；`lint_paths` 基線外數**不增** |
| 3 | b03 之自檢 | 方括號／單引號二項自 MANUAL 改 **PASS**；機檢項數 +2 |
| 4 | 四訊號 | 4 個全有判（取用名／備援／DBC 查無），無「未查」 |
| 5 | b03 之 14 處佔位 | 依作業 B 之結果減少；**減少數 = 解出訊號所涉之佔位數**，未解者具名 |
| 6 | 008 之 TC | ≥ 1 條（`4819555` 判適用時）；不適用則 0 並停下回報 |
| 7 | 003／004 之 TC | 依 `1.8.1.2` 群適用數，**分析層不預設**；差異須具名 |
| 8 | 009／005 之 TC | **0**（凍結）|
| 9 | Test Set 相異值 | 3 → 4 或 5（視 `Browse Control`／`Menu Navigation` 是否落地）|
| 10 | 作業 D | 二本各一節；TC 新增 **0** |
| 11 | `ledger_guard.py` 完工後 | exit 0，輸出與開工前逐字相同 |
| 12 | `canon_refs` | 475 → **475**（本包不引「上繳包 NN §x」式）|

## §6 升級條件

- **E1**：`ledger_guard.py` 開工前報 DUPLICATE／INCONSISTENT → 停，不做任何作業。
- **E2**：作業 A 落 profile 後 `lint_paths` 基線外數增加 → 停，不自行加基線（Tier 3）。
- **E3**：`4819555` 之 v2 判定為不適用 → 008 不生成，停下回報。
- **E4**：`1.8.1.2` 群無任一適用物件 → 003／004 不生成。
- **E5**：四訊號中任一於 LID 查無、或 LID 有而二 DBC 皆無 → 該訊號維持佔位並具名。
- **E6**：作業 C 所需之按壓事件定義落在 `1.8.1.3` 之不適用物件內 → 具名為覆蓋缺口，不自他處補。
- **E7**：任一作業須改動 §1 禁區所列之檔方能完成。

## §7 上繳要求

1. 沿 upstream-01～03 之體例。§0 含本檔重測之 sha256。
2. §1 列 R-ICS1～R-ICS21 全部 sha8（`R-ICS2` v1／v2 並列）。
   **sha8 不符時依 R-ICS19(b) 先取圍籬 diff**，0 行則不停、具名新舊值。
3. 附 `ledger_guard.py` 開工前／完工後二次實跑輸出。
4. §預期數字對照逐項對 §5 之 12 項，相符者亦列。
5. 落點依 R-ICS5；profile 為唯一例外（`docs/runtime/profiles/`，R-ICS18(e) 明令）。
6. 四支全域紅閘二次實跑；`lint_paths` 基線外逐筆具名。
7. §獨立判斷須回答：Browse／Navigation 二組落地後，
   依 IN §4.1.3 是否應合併為一組（旋鈕 vs 按鍵之 entry path 不同，
   但若各只落 1～2 條即觸 too-granular）——**只建議不改**。
