# 上繳 48 —— pilot defect 之全母體修正、重寫回

執行層寫入。依據：`docs/handoff/83_pilot56_verdict.md` §3（55 輪指令）。canon §8.2 六節。
**母本已重寫 243 列（`83dbef7a…`），結構七項全數持平。**

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | 依 R-VS35 分線列兩數；D-6 骨架對照 | ✅ |
| D-3 | 新開 **A-VS161**（拆分時改寫 `test_item` 上半段） | ✅ |
| **W-157** | 五項 defect 之全母體修正（各附可失敗錨點） | ✅ **含二處判準收窄，見 §2.1** |
| **W-158** | R-VS76 完整性重跑 | ✅ PASS |
| **W-159** | 重寫回 | ✅ 243 列 |

---

## 1. 預期 vs 實測（相符者亦列出）

### §1a 錨點 —— 修正前之違規數（R-VS54：兩側皆須有標的）

| defect | 83 包所載之母體 | **修正前實測** | 修正後 | 錨點 |
|---|---|---|---|---|
| **D-1** procedure 之不可執行步驟 | G2 共 9 條 | **8** | **0** | ✅ 可失敗 |
| **D-2** pre_condition 之重複配置 | G3／G4／G8 共 10 條 | **7**（初測 8，減偽陽性 1） | **0** | ✅ 可失敗 |
| **D-3** ER 為 PENDING 而 procedure 已寫 check target | 未載 | **11**（初測 23，減 D 型 12） | **0** | ✅ 可失敗 |
| **D-4** 最弱斷言未套用 | `screen_pending = yes` 16 條 | **2** ＋ 修正過程露出之殘餘 **1** | **0** | ✅ 可失敗 |
| **D-5** `test_item` 上半段非逐字 | `split_flag = true` 7 條 | **5 列／2 leaf** | **0** | ✅ 可失敗 |
| **note** 未標 `duplicate_of` | `-010`／`-013` | **8 對** | **0** | ✅ 可失敗 |
| | | **合計 42** | **0** | |

**升級條件「任一錨點未報出違規」未命中** —— 六項於修正前皆報出非零。

### §1b 其餘

| # | 項 | 實測 | 判 |
|---|---|---|---|
| 1 | W-157 §9 十七項自檢（七個新版逐檔） | `batch01_v8` 0／`batch02_v6` 0／`batch07_v6` 0／`batch17_v6` 0／`batch18_v5` 0／`batch21_probe_v2` 0／`batch23_v2` 0 | PASS |
| 2 | W-157 固定錨點 20 項 | 未命中 **0**，20/20 必命中 | PASS |
| 3 | 升級：D-5 逐字不符者 > 2 | **恰為 2 leaf** | **未逾，惟見 §2.3** |
| 4 | W-158 三類之和 | 219 ＋ 7 ＋ 11 ＝ **237**，未歸類 0 | PASS |
| 5 | W-159(1) 備份 | `REF/036_pre_fullwrite3_20260823.xlsx`，與寫前母本 sha256 相等（`d5d2d3af…`）；既有三備份未動 | PASS |
| 6 | W-159 七項比對 | **全數持平**（dv 4／x14 **0**／cf 1／分頁 10／rel 19／ss 0／members 48） | PASS，惟見 §2.4 |
| 7 | W-159 重讀逐列比對十六欄 | **243 列 × 16 欄，0 項不符** | PASS |
| 8 | W-159 總列數 | **243**（225 TC ＋ 18 未生成 leaf）—— 修正不增減條數 | 相符 |
| 9 | W-159 實寫後 sha256 | **`83dbef7abce41090c3aac88eb7f619358e97e63e70bd02872d5502778e5c4430`** | 記明 |
| 10 | **x14 修復所需之範圍** | 資料列 10–252 → **`R10:R252`** | 記明 |

---

## 2. 不符項目（不自行調和）

### 2.1 **二處判準收窄** —— 初測之數含偽陽性，逐條抽驗後收窄（R-VS73 之反向）

R-VS73 規範「使數上升者須逐條抽驗增量」。**本輪為其反向：初測之數高於 83 包所載，
逐條抽驗後判其為偽陽性而收窄。** 兩處各具名如下。

**(a) D-2 由 8 → 7**

`HeatedSteeringWheelManagement-025`（`batch11_v4`）：

```
pre  1. PROXI Heated_Steering_Wheel = 0 (Absent)
proc 2. Set PROXI Heated_Steering_Wheel = 1 (Present)
```

**pre 自載一個相異之值**，其與 procedure 構成**前後轉換**而非重複設定。
判準收窄為「pre 之值與 procedure 之值相同者方判重複」。**偽陽性 1，未修。**

**(b) D-3 由 23 → 11**

初測之 23 條依 ER 之 DR 分三類：

| ER | 條 | 判 |
|---|---|---|
| `PENDING: DR-15` | **10** | **不判為 defect** —— 其為 **80 包 §1 所明令之形態**（D 型之驗證目標即 DR-15 標的者，ER 寫 PENDING）。**其不確定即結果本身**（所送之值為何），非 83 包 D-3 所述之「前提之不確定」 |
| `PENDING: DR-19` | **4** | **判為 defect** —— 83 包 §2 D-3 之標的（`LeftFrontHeatedSeat-010` 即其一） |
| `PENDING: DR-5-B` | **9** | **判為 defect** —— 其中 2 條為 83 包 D-4 所指（`SwitchLHD/RHD-010`／`-013`），**另 7 條為早批（`batch17`／`batch18`）之同型** |

**11 ＝ 4 ＋ 9 − 2**（`SwitchLHD/RHD` 二條同時計入 D-3 與 D-4，此處只計一次）。

**該 7 條早批之同型逐條抽驗（R-VS73），真陽性 7／偽陽性 0**：

| leaf | procedure 之 check target | 可觀察？ |
|---|---|---|
| `OneStageHeatedSeat-047` | `check that it changes to off` | ✅ |
| `OneStageHeatedSeat-048` | `check that it changes to high` | ✅ |
| `OneStageHeatedSeat-041` | `check that the icon status returns to off` | ✅ |
| `OneStageHeatedSeat-046` | `check that it follows the status` | ✅ |
| `OneStageHeatedSeat-049` | `check that the displayed state … changes to off` | ✅ |
| `OneStageHeatedSeat-050` | `check that the displayed state … changes to high` | ✅ |
| `HeatedSteeringWheelManagement-026` | `check that the … icon is shown on the left side` | ✅ |

**該 7 條經 pilot #3＋#4 覆核而通過** —— 其為 73 包 §3 之最弱斷言裁定
**未推廣至該批**所致，與 83 包 D-2 對 `-021`／`-022` 之判形態相同。

### 2.2 D-4 之殘餘 1 條 —— 修正過程方露出

`OneStageHeatedSeat-041` 修正 ER 3 後，其 **ER 2 仍為 `PENDING: DR-5-B`**：

```
proc 2. Press the left front heated seat icon and read the icon status
ER   2. PENDING: DR-5-B
```

該步驟**無 `check that`**，故初次掃描未及；修正 ER 3 使該 TC 之 `screen_pending`
轉為 `yes` 後，D-4 之判準方將其攔出。

**其條文逐字載其循環**：
`the relative icons status shall follow the logic descibed below (off -> high -> off)`
—— **首次按壓之終態 `high` 為來源逐字，不待 HMI requirements。**
故 ER 2 改 `The icon status changes to high`，procedure 2 併改為 `check that …`
使其具驗證意圖（§5.5）。

**此處改了 procedure**，超出 83 包所令之「ER 改寫」——
其理由為 §6 之 1:1 與 §5.5：若只改 ER 而 procedure 仍為 `read the`，
該步驟仍非驗證。**具名供裁。**

### 2.3 D-5 之 2 leaf 恰為門檻，**但其非隨機**

升級條件為「> 2 則拆分之改寫為系統性」，實測**恰 2**，未逾。

**惟本層判其實質接近系統性**：二者皆為**條文以非 `shall` 語氣起首**者
（`will also be` ／ `When the stop-start system`），其改寫皆為「規範化為 `shall`／`If`」。
**該規範化只在此類條文觸發** —— 故其覆蓋率取決於母體中此類條文之數，
**非取決於拆分之次數**。若母體中此類條文多，2 這個數就不代表其罕見。

**不自行改判**（門檻為分析層所定，實測未逾即未逾），具名於此。

### 2.4 x14 仍為 0

七項「全數持平」，其 `x14:dataValidation` 之持平值為 **0** ——
**其為 48 輪 openpyxl 存檔所失（A-VS153），非本輪所致**，至今未復原。
**修復屬 Pei，範圍為 `R10:R252`。**

### 2.5 `duplicate_of` 由 2 擴為 8 對

83 包 note 只指 `SwitchLHD/RHD-010`／`-013`。全母體掃描（tc_title ＋ pre ＋
procedure ＋ ER 四欄逐字相同）得 **8 對**，其中 7 對為 83 包未指者：

`LeftFrontHeatedSeat-013`/`-015`、`LeftFrontVentedSeat-011`/`-013`、
`RightFrontHeatedSeat-030`/`-032`、`RightFrontVentedSeat-028`/`-030`、
`LeftFrontHeatedSeat-004`/`-005`/`-006`、`RightFrontHeatedSeat-023`/`-024`、
`ThirdRowHeadrestDump-035`/`-036`、`HeatedSteeringWheel-016`/`-022`

**全部標記**：其為同一形態（A-VS119 型冗餘），只標 `-010`/`-013` 而不標其餘
會使覆核者以為只有一處。**依 §8.2.2 皆不合併**（各為獨立 leaf）。

---

## 3. 結果三分法（canon §8.4）

**已驗相符**

- 六項錨點修正前皆報出非零、修正後皆為 0
- 七個新版之 §9 自檢逐檔 **0 項**、固定錨點 **20/20 必命中**
- W-158 完整性 **237 ＝ 219 ＋ 7 ＋ 11**，無未歸類
- W-159：七項無下降、**重讀 243 × 16 欄零不符**、備份四份齊且前三份未動
- batch23 之四項 defect **於生成器修正**（R-VS53：產物可自 driver 重製），
  非逐條手改

**已驗不符**

- §2.1 二處判準收窄（D-2 偽陽性 1／D-3 之 D 型 12 條不屬本 defect）
- §2.2 D-4 殘餘 1 條，其修正**改了 procedure**，超出指令所令之範圍
- §2.3 D-5 之 2 恰為門檻而其分布非隨機
- §2.4 x14 為 0
- §2.5 `duplicate_of` 由 2 擴為 8 對

**未驗**

- **本輪修正之 42 處無一經人工覆核** —— pilot #5＋#6 覆核的是修正前之版本；
  **修正本身是否引入新缺陷，未經任何抽樣**
- `assertion_from()` 之機械改寫（自 procedure 之 `check that <X>` 取其斷言、
  並將 `it` 代換為前句之名詞片語）**其語法正確性只由我自己讀過** ——
  7 條之 ER 皆為機器所生之英文句
- 早批之修正**未回其生成器** —— `batch17`／`batch18` 等之 `_v(n+1)` 由
  `earlyfix_w157.py` 疊加而生，**其原生成器重跑仍會產出舊形態**；
  R-VS53 之「可自 driver 重製」於早批**不成立**，本輪未修此

---

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| # | 條件 | 值 |
|---|---|---|
| 1 | D-1 | procedure 步驟含 `a value outside the declared valid set` **且**同序 ER 為 `PENDING` |
| 2 | D-2 | procedure 之 `Set PROXI <key>` 與 pre_condition 之別名相符，**且二者之值相同**（值相異者為前後轉換，見 §2.1a） |
| 3 | D-3 | ER 為 `PENDING` 且同序 procedure 含 `check that`，**排除 `PENDING: DR-15`**（見 §2.1b） |
| 4 | D-4 | `screen_pending = yes` 且任一 ER 為 `PENDING` |
| 5 | D-5 | `split_flag = true` 者，其 `test_item` 上半段須為條文之子字串（以 `blocks_with_sec()` 之 `text` 為錨） |
| 6 | note | tc_title ＋ pre_conditions ＋ test_procedure ＋ expected_result **四欄逐字相同** |
| 7 | 修正之落點 | batch23 → **生成器**（`batch23_w152.py`，9 處）；早批 → `earlyfix_w157.py` 疊加產 `_v(n+1)` |

---

## 5. 本輪新開之 anomaly 與 DR（成對）

| Anomaly | 主題 | 配對之 DR |
|---|---|---|
| **A-VS161** | 拆分時改寫 `test_item` 上半段，違 R-VS6（`will`→`shall`、`When`→`If`、`Softkey button`→`softkey` 等） | **無 DR** —— 本層之改寫，非來源之缺 |

**本輪未新開 DR。**
**AH 新增之 BLOCKED 標的**：`DR-5-B`（7 條早批 ＋ 2 條 G6，畫面層之樣式與內容）、
`DR-19`（4 條 G4 ＋ 1 條 G8，`$EngRun_Stat$` 四值與 `EngineSts` 之對應）——
**皆為既有 DR，未新開號**。

### R-VS75 之回流（本輪與 Pei 之直接往返）

**本輪無選項式徵詢，亦無新的 Pei 裁定。**

---

## 6. 獨立判斷（canon §8.2 §6）

1. **§2.1(b) 那 12 條 `PENDING: DR-15` 是本輪最該擋下的東西。**
   我的 D-3 判準寫出來就會把它們掃進去 —— 而它們是 **80 包明令的形態**，
   是 A-VS157 的修正結果本身。**若我照初測的 23 逕改，
   等於把上一輪剛修好的東西改回 false pass。**
   擋下它的不是任何檢查，是我去讀了每一條的 ER 屬哪個 DR。
   **判準的數與判準的對不相干（R-VS73 之理由），這次是往下的方向。**

2. **§2.1(b) 那 7 條早批同型，暴露了 pilot 的結構限制。**
   它們經 pilot #3＋#4 覆核而通過 —— 不是覆核者看漏，
   而是**當時 73 包的最弱斷言裁定還沒下**。
   **裁定下了之後，沒有任何機制回頭掃已通過的批次。**
   R-VS29／R-VS73 管的是判準改變後的數，**不管判準改變後的舊產物**。
   這是 83 包 D-2 說「80 包對 `-021` 之修正未推廣至 batch23」的同一件事，
   只是方向相反（那是往後未推廣，這是往前未回掃）。

3. **§2.2 我改了 procedure，那超出指令。**
   只改 ER 會留下一個 `read the …` 對 `The icon status changes to high` 的 1:1，
   步驟本身仍非驗證。我判 §5.5 與 §6 要求併改，**但這是我自己的判斷，
   不是 83 包所令**。若分析層認為不該動 procedure，這一條要退回。

4. **§3 未驗的第三項是本輪最實質的技術債。**
   早批的修正是**疊加**上去的 —— `batch17_v6` 不是 `batch17` 的生成器重跑，
   是 `batch17_v5` 加一層修正。**R-VS53 說產物須可自 driver 重製，
   這在早批已經不成立**，而且從 46 輪的 `pilot_fix_w130.py` 起就是如此。
   **交付的工作簿裡有 100 多條 TC，其生成路徑是「原生成器 ＋ N 層修正腳本」**，
   重製它們需要按順序跑 N 個腳本，而那個順序沒有任何地方記著。

5. **修正了 42 處，沒有一處被人看過。**
   pilot #5＋#6 看的是修正前的 18 條。**下一輪就是交付。**
   若 56 輪不再抽驗，這 42 處的正確性只有我自己讀過一遍 ——
   特別是那 7 條機器生成的英文 ER 句。

---

### D-2 依 R-VS35 之分線兩數

| 線 | 登記簿 | 數 |
|---|---|---|
| **主線（CFTS044）** | `ANOMALIES.md` 之 `A-VS*` | **159 相異**（最大 `A-VS161`；缺號 2：`A-VS2`、`A-VS131`，皆為讓號） |
| **VF230 線** | `ANOMALIES.md` 之 `A-VF*` | **12 相異**（最大 `A-VF12`，無缺號） |

`DATA_REQUESTS.md`：**DR-5／7／8／8′／11–34**（含 `14′`／`15′`／`22′`／`24′`／`25′`）。
**本輪未新開 DR。**

### D-6 骨架對照

| 節 | 骨架要求 | 本包 |
|---|---|---|
| §1 | 預期 vs 實測，相符者亦列 | ✅ §1a 六項錨點之修正前後對照 ＋ §1b 十列 |
| §2 | 不符項目，不自行調和 | ✅ 五項；§2.1 之二處收窄逐條抽驗具名，§2.3 恰為門檻而不自行改判 |
| §3 | 三分法 | ✅ 已驗相符／已驗不符／未驗（未驗三項，含早批之 R-VS53 不成立） |
| §4 | 掃描條件揭露 | ✅ 7 列，含二處收窄後之判準原文 |
| §5 | 新開 anomaly 與 DR 成對 | ✅ 1 anomaly／0 新 DR；R-VS75 回流表為空並具名其空 |
| §6 | 獨立判斷 | ✅ 五項，含「超出指令改了 procedure」與「早批已無 driver 可重製」之自陳 |
