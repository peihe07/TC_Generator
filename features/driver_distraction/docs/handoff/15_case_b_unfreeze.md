# 下放包 15 —— 乙案裁定（R-DD19、A-DD8/A-DD9）、DR 文稿三處補強、B2 生成規格（-017~-024）

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`14_framework_fix.md`（T20 系列**先行**，本包 T21 接續其後）
- 裁定：**Pei 2026-08-28 裁乙** —— `-017`~`-024` 以雙 assumption marker 解凍生成；DR-DD5／DD6 **必發等級不變**
- `-025`~`-028`（DD1）**凍結維持** —— 乙案不及於此（錯猜代價不對稱：DD1 錯則 037 原文改寫、verbatim 全變）
- 落檔註記：首寫於 MCP 逾時中失敗（get_file_info 驗 ENOENT），本檔為重寫，同稿

---

## 一、R-DD19（乙案條文；T-抄）

```
R-DD19（DR-DD5／DD6 未回覆期間之假設生成 —— Pei 2026-08-28 裁乙）

(a) 施加路徑假設（marker A-DD8）：$VC_Trans_Equipped$ 依 LID
    `Proxi & Configuration` r421 之 Atlantis 欄採 PROXI 參數
    `Gear_Box_Type`（`Powertrain_Configuration_4`，byte 101，bit 0–2）。
    採認基礎：r420／r421 之三種自洽讀法中二種收斂於此
    （新舊列讀法、訊號/參數分答讀法），唯一阻斷之讀法（r421 該格為孤立
    筆誤）無任何形態支持 —— 此為讀法收斂之採認，非文件記載，故掛 marker。
(b) 代表值假設（marker A-DD9）：
      [Manual]    → PROXI Gear_Box_Type = 1 (MTX)
      [Automatic] → PROXI Gear_Box_Type = 4 (ATX)
    採認基礎：MTX／ATX 為兩極之無疑義代表 —— MTX 之 M 為業界命名之
    manual（IN §8.4.1 domain constant 家族），PROXI Annotation 之
    `manual` 舉例對應之；ATX 同理。
(c) **邊界（硬）**：`MTA`（2）與 `DDCT`（3）之歸屬為 DR-DD6 之未決問題，
    **不得以該二值作任何 TC 之 Pre-Condition 或輸入** ——
    乙案採認之範圍止於兩極，不及於邊界。
(d) 回覆後之處置：DR-DD5／DD6 之回覆與 (a)(b) 相符 → 撤 marker；
    不符 → 回修範圍為 8 TC 之 PROXI 值（機械性換值），結構不動。
(e) 本條不減 DR-DD5／DD6 之必發等級，不影響 DD1 之凍結。
（Pei 2026-08-28 裁乙，下放包 15 §一）
```

**A-DD8／A-DD9 條目**（T-登，逐字）：

```
A-DD8（假設：VC_Trans_Equipped 之施加路徑）
狀態 OPEN。內容：依 R-DD19(a)，-017~-024 之生成假設 r421 為準
（PROXI Gear_Box_Type）。撤銷條件：DR-DD5 回覆確認。
用及之 TC 標 [ASSUMPTION A-DD8]。
```

```
A-DD9（假設：Manual/Automatic 之兩極代表值）
狀態 OPEN。內容：依 R-DD19(b)，[Manual]=1 (MTX)、[Automatic]=4 (ATX)。
MTA/DDCT 之歸屬未決（DR-DD6），不入任何 TC。
撤銷條件：DR-DD6 回覆確認。用及之 TC 標 [ASSUMPTION A-DD9]。
```

---

## 二、DR 文稿三處補強（T-登；皆為待發稿之修訂，逐字替換所示段落）

### 2.1 DR-DD1 —— 末段（`Until clarified…`）**之前**插入一問

> If the answer is (b) LATAM: please also specify how the market condition
> is expressed for these rows — as a list of `$Country_Code$` values, or
> via the `Regulation_type` property referenced in the System Architectural
> Design. "LATAM" is a region, not a single country code, and the test
> cases need a concrete precondition value.

### 2.2 DR-DD6 —— 問句段**之後**插入判準句

> For reference: the decision-relevant criterion appears to be encoded in
> the requirement structure itself — rows `-126`/`-127` condition on
> `$PresentGear$ = [P]` (a Park position must exist), while `-128`/`-129`
> condition on the parking brake (no Park position). The question therefore
> reduces to: do `MTA` and `DDCT` gearboxes have a Park position for the
> purpose of these requirements?

### 2.3 DR-DD5／DD6 —— 末行（`…on hold in SWQT test case generation`）**替換**為

> SWQT test case generation for the affected rows proceeds under a
> documented assumption (parameter path per row 421; `MTX`/`ATX` as the
> representative Manual/Automatic values); the affected test cases carry
> assumption markers and will be revised if the answer differs.

**理由**：乙案生效後原句不再屬實 —— DR 不得向上游陳述已失實之狀態。

---

## 三、B2 生成規格（`-017`~`-024`，8 leaf；**T20a framework 落檔後始得開始**）

### 3.1 範圍與骨架

| leaf | 內容 | Test Set | priority（profile §4）|
|---|---|---|---|
| `-017`／`-018` | 自排＋P → 解鎖／fail-safe | `Hong Kong Market` | P1／P1 |
| `-019`／`-020` | 自排＋非P → 上鎖／fail-safe | `Hong Kong Market` | **P0**／P1 |
| `-021`／`-022` | 手排＋手煞ON → 解鎖／fail-safe | `Hong Kong Market` | P1／P1 |
| `-023`／`-024` | 手排＋手煞OFF → 上鎖／fail-safe | `Hong Kong Market` | **P0**／P1 |

### 3.2 施加路徑（profile §3 ＋ 本包）

| 條件 | 寫法 | marker |
|---|---|---|
| 市場 | `PROXI Country_Code = 91` | 無（確定值）|
| 自排 | `PROXI Gear_Box_Type = 4 (ATX)` | **A-DD8 ＋ A-DD9** |
| 手排 | `PROXI Gear_Box_Type = 1 (MTX)` | **A-DD8 ＋ A-DD9** |
| P 檔 | `$PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ = 12 (Park)` | 無 |
| 非 P 檔 | **待 T21a**（VAL_ 全列舉傾印後取一代表，見 §3.3）| 無 |
| 手煞 ON／OFF | `$BCM_FD_9.ParkBrakeSts$ = 1 (ON)`／`= 0 (OFF)` | **A-DD2**（R-DD18(b)）|
| 速度 | PC 訊號源行 `$STATUS_CCAN3.VehicleSpeedVSOSig$` at 0 —— **排除基準速度規則之干擾**，使觀察可歸因於檔位／手煞 | 無（0 非門檻值，不掛 A-DD6）|

### 3.3 T21a —— 非 P 代表值（B2 前置）

`GearEngagedForDisplay_PT` 之 `VAL_` **全列舉傾印**（前輪僅確認含 `12 "Park"`）。
非 P 取值原則：037 書 `<> [P]` 為一**類**，類內任一成員皆合法（同取樣 feature
之理）；**取行車常態檔位**（如 Drive 類）為代表，reasoning 載明所取之
`VAL_` 逐字與取法。**不掛 marker**（類內取樣非假設）。

### 3.4 fail-safe 列（`-018`/`-020`/`-022`/`-024`）

- 形態**逐 leaf 依 037 AC2 原文定**（profile §3.2 之紀律，B1 同）
- AC2 若僅書「required vehicle signal」未指名：**取該 source AC1 所條件之
  訊號**為所停之訊號（`-126`/`-127` 側 → 檔位訊息；`-128`/`-129` 側 →
  手煞訊息），reasoning 載明此取法之依據（判定所需訊號即 AC1 之條件訊號）
- **PROXI 參數不作失效標的**（其為組態非訊號）
- 四列屬 A-DD7 組 3／組 4（各組內 037 原文逐字全等）—— reasoning 依 B1
  同式載明實質同一，不得以取樣差偽稱為不同驗證目標

### 3.5 其餘拘束（承 pilot／B1，不重述）

1. spec_reference 雙引：`CFTS022-4915120` 一行 ＋ 條文 ObjectID 一行，升冪
2. 觀察面 A 取樣依 profile §2.1（黃標、NAV 系不取；具名）
3. ER 四禁詞、R-DD11/12/17、R-DD15/16 全套
4. 自檢第 1 項須為 T20b 改版後之**實際比對 framework.md**
5. **只生成，不寫回、不 git**

---

## 四、分析層自辦（本包發出後）

- profile §3：`$VC_Trans_Equipped$` 列由 SUSPENDED 改
  **CONDITIONAL（R-DD19，A-DD8/A-DD9）**，寫法欄填 §3.2 之二值；
  §5 表同步（`-017`~`-024` 解凍、marker 義務載明）
- 待 T21a 回報後補非 P 代表值入 profile

## 五、任務彙總（次序：T20 系列 → T21）

| # | 任務 |
|---|---|
| T-抄 | R-DD19 入 `RULINGS.md`（錨點、條數與停止值同步回報）|
| T-登 | A-DD8／A-DD9 建條；§二 三處 DR 文稿修訂（逐字）|
| T21a | 非 P 代表值傾印與取定（§3.3）|
| T21b | **B2 生成**（§3.1–§3.5；T20a ＋ T21a 之後）|

**不在本輪**：`-025`~`-028`、寫回、git、tsv（T17b 停止維持）。

## 六、上繳包要求（`docs/upstream/12_batch_b2.md`）

T-抄／T-登 結果、T21a 傾印、B2 八則全文 ＋ 自檢（含 framework 實比對）、
未結 DR 清單（狀態依 §二 修訂後）、獨立自評、R-G8 揭露。
