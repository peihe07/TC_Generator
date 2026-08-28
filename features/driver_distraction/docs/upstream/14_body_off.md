# 上繳包 14 —— R-DD20 v2 落地、A-DD10 基礎改述、`-001`／`-002` 生成（T23a）、`RE_ACCESS` 導出式（T23b）

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放包：`17_body_off.md` §五（T-抄／T-登／T23a／T23b）
- 本輪**未生成 `-025`~`-028`**、**未寫回**、**未執行 git**、**共用路徑未寫入一字**

> **三件事**：
> **`-001`／`-002` 已生成，26 檢 24 PASS ／ 1 N/A ／ 1 WARN ／ 0 FAIL** ——
> WARN 即 T23b 所設之「聯集外動詞須人審」，**本輪首次觸發**（`Bring`／`Terminate`）。
> **包 16 之自檢跑同一份未注入之產物，紅 3 項**（檢 6／13／15，§四-1）——
> 三處皆為既有拘束在「首次真正行使」時才浮現的碰撞，非產物之瑕疵。
> **`-002` 因 PENDING 不得出貨**（IN §8.4.3），生成與台帳照常。
> **`-001` 之 priority 照 profile §4 生成 P1，與下放包 17 §三 所書之 P0 相衝** ——
> 未逕改 profile（Pei 裁准之列表），提交裁定（§十 10-1）。

---

## 一、T-抄 —— R-DD20 v2（v1 留存）

| 條號 | 來源 | 字元數 | 落檔 | 逐字元差異 |
|---|---|---|---|---|
| R-DD20 v2 | 下放包 17 §二 | **1241** | 1 次 | **0** |

**錨點依 R-DD14(a) 之二版體例**（同 R-DD6）：
舊 `## R-DD20` 改題為 **`## R-DD20 v1`**（留存版），新增 **`## R-DD20`**（現行版）。
**v1 之圍籬內文一字未動** —— 其 `sha8` 試跑值仍為 `00912428`，與上輪完全相同（下表）。

`scripts/t17a_add_anchors.py` 之 `ANCHOR_OVERRIDE` 同步補二列
（`R-DD20 → R-DD20 v1`、`R-DD20 v2 → R-DD20`）—— 否則重跑該工具會把二版之錨點寫反。

**條數與停止值同步**：

| | 上輪 | **本輪** |
|---|---|---|
| 索引現行 | 20 | **20**（R-DD20 由 v1 改列 v2，不增條）|
| 索引留存 | 1 | **2**（新增 `R-DD20`（v1））|
| 錨點（`^## R-DD`）| 21 | **22** |
| **停止條件 2 之值** | 21 | **22** |

**指紋試跑**（共用路徑，依「tsv 不在本輪」只試跑後還原；`git status` 對 `docs/fw036/` 無變更）：

| ruling_id | ancestor | sha8 | 狀態 |
|---|---|---|---|
| R-DD20 | `R-DD20 v1` | **`00912428`** | **與上輪同** —— 留存版逐位元未動 |
| R-DD20 | `R-DD20` | **`5ae8694f`** | 新增（v2）|
| R-DD19 | `R-DD19` | `e293c320` | 仍未入 tsv（§一之落差，10-4 已裁：以錨點數為準）|

既有 19 條之 `sha8` **逐一比對全未變**；非 DD 之列 **diff 0 行**。

**留存表新增一列**，逐條列出 v1 之失效值（依 R-DD6 v1 之體例）：
(a) 之「78 處命中」為關鍵詞族計數；(b) 之「只得逐字取自 power 線已裁之施加式」
（該線無本序列之施加步驟）；**無 (f)**（`TLM_Status.Info` 之不適用未載）。

---

## 二、T-登

### 2.1 A-DD10 之採認基礎改述（定義級）

`ANOMALIES.md` 之 `### 採認基礎` 節整段換為 **R-DD20 v2(a) 逐字**，
並附 CFTS009 `4941238` 之逐字原文（唯讀引自 power 線文字層）。

**上繳 13 §6.1 之「⚠ 實測與所書不符」節改為刪除線 ＋ 結案說明** ——
分析層已於下放包 17 §一-1 採認該不符並改條，故該節於本輪結案。

**新增一節「殘餘假設之範圍（v2 之收窄）」**：

| | v1 | **v2（現行）** |
|---|---|---|
| 所假設者 | **同一性本身**（跨文件同名之採認）| **台架實現與 DR-DD9 回覆之一致性** |
| 基礎 | 命中計數（**已撤**）| CFTS009 `4941238` 之**定義**，CFTS022 `-113` 引用之 |
| 回覆不符時之回修 | 2 TC 之電源時序步驟 | **不變** |

> **同一性已不在假設之列** —— marker 現所標者為「照 CFTS009 所定義之時序，
> 台架上確實可如此驅動」。**這是收窄，不是撤銷**，故 marker 續掛而非移除。

`### 適用範圍` 節同步更新：二則已生成，marker 實際掛於電源時序步驟。

### 2.2 [CG-DD1] —— 我的提案是錯的，已依 §一-2 更正

上繳 13 §2.3 提案「`-120`／`-121` 之 037 衍生 leaf 為 `-021`~`-024`」。
**執行層本輪自行覆核 CFTS022 `Basic Report` 之 ObjectID → 列號對照**（機器讀，非目視）：

| ObjectID | CFTS022 列 | 037 衍生 leaf | 出處 |
|---|---|---|---|
| `4915112` | `SYS-RA-Driver_Distraction-120` | **`-013`／`-014`** | r121；B1 之 spec_ref |
| `4915115` | `-121` | **`-015`／`-016`** | r122；B1 之 spec_ref |
| `4915120` | `-125`（HK 章閘）| `-017`~`-024` 之共同閘 | r126 |
| `4915123`／`4915124` | `-128`／`-129` | `-021`~`-024` | r129／r130 |

**分析層之更正成立** —— `-021`~`-024` 之 source 為 `-125` ＋ `-128`／`-129`，
與 `-120`／`-121` 無關。本條之影響範圍**維持 `-013`／`-015`**（10-5）。

> **兩邊都記，逐字照下放包 17 §一-2**：
> 執行層依「範圍之認定屬分析層」**不逕改而提交裁定，程序正確 —— 而提案本身是錯的**。
> **若當時逕改，錯的對映就會直接寫進台帳。** 這正是該拘束存在的理由。

### 2.3 DR-DD9 文稿

**不動**（下放包 17 §五 T-登：其未引 78 之數）。已核：文稿全文無該計數。

---

## 三、T23a —— `-001`／`-002` 生成

產物：`generated/batch_body_off_init.json`（2 則）。`tc_id` 依既有分批體例
（pilot 無字母、B1 `B`、B2 `C`）取 **`newR1L-DD-D001`／`D002`**。

### 3.1 ⚠ 生成前先報三處與現行拘束之碰撞

| # | 碰撞 | 我怎麼處置 |
|---|---|---|
| **甲** | **priority**：下放包 17 §三 書 `-001` = **P0**（boot/recovery，IN §10.2）；**profile §4（Pei 2026-08-27 裁准）之 PR-c 明列「初始化 → P1」，且其列表把 `001`／`002` 都放在 P1(20)** | **照 profile §4 生成 P1**，提交裁定（10-1）。理由：profile 為現行且經裁准之權威，自檢「+ §10.2 合 profile §4」即以其為準；改 P0 須連帶改 profile §4 之規則與 8+20 之閉合，**屬分析層** |
| **乙** | **`$PowerMode$` 之值以方括號書之**（`[IGN_LK]` 等）。R-DD20 v2(b) 要求條件錨定 CFTS009 逐字，而 **profile §2.5：四交付欄一律不得出現方括號**（唯一例外為 marker）| **不把 `[IGN_LK]` 寫入四欄**；步驟以 power 線通稱式承載，**`4941028` 之五值錨定記於 `reasoning`**。power 線之 profile §3.2 對 `[Nh]` 有 profile-scoped OVERRIDE，**本 feature 之 profile 無同類條款**，故不自行比附 |
| **丙** | **§5.4 之範例把 `$` 指令行縮排**，而 **IN §11：多行欄位無行首空白** | 取 §5.4 之**規範句**（`Command line: starts with $`，未言縮排），**指令行不縮排**。二者遂皆合 |

### 3.2 二則全文

#### `newR1L-DD-D001` —— `SWE1-RA-Driver_Distraction-001`（P1／`Body Off Init`／狀態轉換）

```
test_item:
AC1:
When the vehicle exits Body OFF sleep, DD Service provides Lock Out State initialization and state notification capabilities
Case [Normal]normal wake-up from Body OFF
Then DD Service sets all Lock Out States to NOT_RESTRICTED
(a normal wake-up from Body OFF leaves the locked-out features reachable)

pre_conditions:
1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)

input_test_data:
NA

test_procedure:
1. Bring the HU through the Body OFF power down [ASSUMPTION A-DD10]
2. Start CAN activity on Body CAN to wake the HU [ASSUMPTION A-DD10]
3. Open "Player Song, artist, title, etc. (speller search)" and check that it opens

expected_result:
1. The HU periodic messages are no longer present on the bus
2. The HU broadcasts all its periodic messages within 400 msec of wakeup
3. "Player Song, artist, title, etc. (speller search)" opens and its view is displayed

spec_reference:  CFTS022-4915104
priority:        P1        design_method: 狀態轉換 (State Transition Testing)
```

#### `newR1L-DD-D002` —— `SWE1-RA-Driver_Distraction-002`（P1／`Body Off Init`／狀態轉換）

```
test_item:
AC2:
When the DD process is terminated during Body OFF sleep, DD Service provides cold-start state initialization capability after wake-up
Case [Exception]the process is terminated during sleep
Then DD Service starts with the default NOT_RESTRICTED state and initializes all states to NOT_RESTRICTED
(a cold start after the process was terminated during sleep leaves the locked-out features reachable)

pre_conditions:
1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)

input_test_data:
NA

test_procedure:
1. Bring the HU through the Body OFF power down [ASSUMPTION A-DD10]
2. Terminate the DD process in the test environment
$ PENDING: DR-DD9 <DD process 終止指令>
3. Start CAN activity on Body CAN to wake the HU [ASSUMPTION A-DD10]
4. Open "DND Customize auto reply message" and check that it opens

expected_result:
1. The HU periodic messages are no longer present on the bus
2. The DD process is no longer running in the test environment
3. The HU broadcasts all its periodic messages within 400 msec of wakeup
4. "DND Customize auto reply message" opens and its view is displayed

spec_reference:  CFTS022-4915104
priority:        P1        design_method: 狀態轉換 (State Transition Testing)
```

**`-002` 因含 `PENDING` 而不得出貨**（IN §8.4.3）；生成與台帳照常（下放包 17 §三-8）。

### 3.3 逐條對照下放包 17 §三 之八項拘束

| # | 拘束 | 落實 |
|---|---|---|
| 1 | test_item 上半 verbatim 取 037 r9／r10；下半依 R-S4 相異 | 上半 **35**／**42** tok（cap 50，`mode=full`，未摘句）；檢 2 之「上半子串 ✓」為對 037 c3 之實際比對；下半相異（檢 2b 綠）|
| 2 | PC 只書速度訊號源行；Gear／PARK_BRK／Country **不入** | PC 各 1 項，合 R-DD17 之形式；四欄無 `Gear_Box_Type`／`ParkBrakeSts`／`Country_Code`（檢 3、R-DD19(c) 項皆綠）|
| 3 | 三步構形＋CFTS009 錨定 | `-001` 3 步、`-002` 4 步（多終止步）；ER 之喚醒句取 `4941103` 之可觀察面 —— **`shall` 不入 ER**（IN §6 禁 modal），故書 `The HU broadcasts …`，`Within 400 msec of wakeup` 逐字保留 |
| 4 | 電源時序步驟標 `[ASSUMPTION A-DD10]` | 二則之步驟 1／3（`-001` 為 1／2）皆標；**並新增一項自檢**使漏標必紅（§四-M）|
| 5 | `-002` 終止步驟：業務行照 037 Method 逐字；`$` 行留 PENDING | 037 r10 c18 原文 `terminate the DD process in the test environment` **逐字**（首字母大寫為步驟書寫之排版正規化，實詞未改）；`$ PENDING: DR-DD9 <DD process 終止指令>` 依 R-DD20 v2(c)＋IN §8.4.3 |
| 6 | spec_reference `CFTS022-4915104` 一行 | 檢 16 綠（`source ['113'] → ['CFTS022-4915104']`）|
| 7 | `TLM_Status.Info` 禁用；四禁詞照禁 | 四欄無 `TLM_Status`／`$Telematic_Power$`；profile §2.3 項 0 命中 |
| 8 | 26 檢全跑；`-002` 不得出貨 | **24 PASS ／ 1 N/A ／ 1 WARN ／ 0 FAIL**；不出貨已載 |

### 3.4 取樣 feature —— 可用列只有 5 個，故與他批共用

HMI spec p7 `Driver Lockout Tables` 之機器實測（`pdfplumber`，逐 rect 取
`non_stroking_color`）：**黃標（`(1.0, 1.0, 0.0)`）覆蓋三處** ——
`top 109–123`（Player / RSE）、`263–289`（Messaging 二列）、`341–354`（SRT Options）。
再扣除 NAV 類（分類欄 `NAV @ top=188`，涵蓋 `125`~`252` 各列，僅 LATAM）
與全 `Inv.` 之 `SXM 360L`，**可取之 L/O 列只餘 5 個**：

```
top=291  Edit phone book (speller input)          [Phone]
top=304  Pairing (1st time)                       [Phone]
top=317  DND Customize auto reply message         [DND]
top=330  Player Song, artist, title, etc. (speller search)   [Player]
top=356  Reconfigurable menu bar                  [Menu Bar]
```

五個**已全數被 pilot／B1／B2 用過**，故本批必然共用。
取 `top=330`（`-001`）與 `top=317`（`-002`），使二則於 ER 可具名區辨（檢 17 綠）。
**此為素材面之限制，非取樣之隨意** —— 其根因即 `[CG-DD1]`／`DR-DD8`（表不可機讀）。

---

## 四、自檢與變紅注入

### 4.1 ⚠ 包 16 之自檢跑**未注入**之 `-001`／`-002`：**紅 3 項**

```
[FAIL]   6 §5.2   字數 {'D001': [11, 12, 13], 'D002': [11, 14, 12, 11]}；超限 [('D002', 2, 14, 12)]
[FAIL]  13 §12    001／002 → 功能測試（無故障、無二值轉換、條件 <2）；不符 first-match [...]
[FAIL]  15 §11    [('D001','test_procedure','[ASSUMPTION A-DD10]','四欄不得出現方括號'), ...]
RESULT: PASS 22 ／ N/A 1 ／ FAIL 3　（共 26 檢）
```

**三處皆非產物之瑕疵，是既有判準在「首次真正行使」時才浮現的碰撞** ——
下放包 17 §四 10-6 所預言者（「它即將第一次被真正行使」）**在三個地方同時發生**：

| 檢 | 碰撞 | 修法 |
|---|---|---|
| **6** | §5.4 之 `$` 指令行被計入「步驟字數」（14 > 12）| **母體之更正**：`$` 行不屬描述部，故不計。**非尺之放寬** —— 描述行本身仍受 12／18 拘束（注入 **J** 為證）。R-DD15「逾限改步驟不改尺」之適用未變，**惟本更正須追認**（10-2）|
| **13** | `_want()` 只認「同一訊號二相異值」為 A→B，故電源域之 sleep→wake 判成功能測試 | IN §12 之列為 `State A → State B transition`，**未限以訊號承載**。補一條同族之機械判準：**ER 中二 item 對同一組實詞分作否定與肯定之斷言**（交集 ≥3 實詞）→ A→B |
| **15** | (i) `\[ASSUMPTION A-DD\d\]` 之 **`\d` 為單位數** → `A-DD10` 被判為違規；(ii) `"<" in field` 一律紅 → IN §8.4.3 所命之 `PENDING: DR-{n} <缺件名>` 被判為違規 | (i) `\d` → `\d+`（另一處 `findall` 同修）；(ii) 加 §8.4.3 形制之 carve-out（`PENDING: DR-\w+\d+ <…>`），**與 `[ASSUMPTION A-DDn]` 同型**。注入 **N** 證 carve-out 未開太大 |

> **`\d` 那一個值得單獨記**：`A-DD10` 是本 feature 第一個二位數 marker。
> 它同時使 **carve-out 失效（誤判為違規）** 與 **marker 義務檢失效（`findall` 抓不到）** ——
> **一個往紅、一個往綠，方向相反，同一個 `\d`。**
> 往綠的那一半不會有人發現，因為它只是少印一個 marker 名。

### 4.2 本輪之新檢與八組注入（**注入檔跑完即刪**）

| # | 注入 | **包 16 之檢** | **包 17 之檢** |
|---|---|---|---|
| H | §5.4(ii)：`$` 指令行帶編號（`3. $ PENDING…`）| FAIL 4（檢 8／10／13／15）| **FAIL 2（檢 8／10）** |
| I | §5.4(iv)：**ER 覆述 `$` 指令字串** | FAIL 3（檢 6／13／15 —— **皆非本意**）| **FAIL 1（檢 8）** |
| **J** | **檢 6：描述行本身逾 12 字** | FAIL 3（檢 6／13／15）| **FAIL 1（檢 6）** |
| K | §5.4(iii)：指令行與描述行之間插一空行 | FAIL 3（檢 6／13／15）| **FAIL 1（檢 8）** |
| L | §5.4(i)：item 無描述部，首行即 `$` 指令行 | FAIL 3（檢 8／13／15）| **FAIL 1（檢 8）** |
| **M** | **R-DD20 v2(b)(4)：拿掉 `[ASSUMPTION A-DD10]`** | FAIL 3（檢 6／13／15 —— **marker 之漏標無人攔**）| **FAIL 1（檢 +，marker 義務）** |
| N | 檢 15：非 §8.4.3 形制之角括號（`<the speller page>`）| FAIL 3（檢 6／13／15）| **FAIL 1（檢 15）** |
| O | 檢 13：ER 之否定側移除 → first-match 不符 | FAIL 3（檢 6／13／15）| **FAIL 1（檢 13）** |

**「包 16 之檢」欄之 FAIL 3 幾乎都是 §4.1 之基線紅，不是攔到注入。**
這正是**基線紅使一切注入看起來都被攔**的形態 —— 綠底才量得出攔截力。
故本表之判讀以**右欄之檢號是否即為該注入所指者**為準：**八組全中，無誤攔、無漏放**。

**J 與 M 為本輪最要緊的二組**：
- **J** 證「檢 6 之母體更正不是把尺放寬」—— 描述行逾限仍紅。
- **M** 證新增之 marker 義務項確實在工作 —— 包 16 對 A-DD10 之漏標**完全無防**
  （其 marker 表只登了 `Gear_Box_Type` 與 `ParkBrakeSts`）。

### 4.3 四產物之最終結果

| 產物 | 檢數 | 結果 |
|---|---|---|
| pilot（4 TC）| 26 | 24 PASS ／ 2 N/A ／ 0 WARN ／ **0 FAIL** |
| B1（10 TC）| 26 | 24 PASS ／ 2 N/A ／ 0 WARN ／ **0 FAIL** |
| B2（8 TC）| 26 | 24 PASS ／ 2 N/A ／ 0 WARN ／ **0 FAIL** |
| **Body Off Init（2 TC）** | 26 | **24 PASS ／ 1 N/A ／ 1 WARN ／ 0 FAIL** |

**三個既有產物零回歸** —— 本輪所有判準之改動（檢 6 母體、檢 13 新分支、
檢 15 carve-out、檢 8 強化、marker 表新列、`RE_ACCESS` 導出式）**皆未動其結果**。

---

## 五、T23b —— `RE_ACCESS` 改由交付語料導出

### 5.1 上繳 13 §8.2-1 之自認，本輪償還

前版：`RE_ACCESS = re.compile(r"\b(open|start|select|play|enter|launch)\b")` ——
**是我列的，不是量出來的**。本版比照 power profile §3.1 之作法：

- **母體**：已交付之三產物（pilot／B1／B2）之全部 `test_procedure` 步驟（**65 步**）
- **分類判準（機械，逐動詞看其所有步驟）**：
  - 引用 UI 標籤（`"…"` 且非全大寫之匯流排訊息名）**且**不涉訊號 → **ACCESS**
  - 涉 `$訊號$` 或匯流排訊息名**且**不引 UI 標籤 → **STIMULUS**
  - 二者皆否或兼有 → **未分類**（列出，**不逕用**）

**實測分類**：

| 動詞 | 步驟數 | 引 UI 標籤 | 涉訊號／訊息 | 判 |
|---|---|---|---|---|
| `Open` | 26 | 25 | 0 | **ACCESS** |
| `Select` | 7 | 7 | 0 | **ACCESS** |
| `Start` | 1 | 1 | 0 | **ACCESS** |
| `Send` | 18 | 0 | 18 | STIMULUS |
| `Stop` | 11 | 0 | 11 | STIMULUS |
| `Read` | 2 | 0 | 0 | **未分類** |

**`Read` 落在未分類是對的** —— 它是觀察動詞，既非存取亦非施加，
**而前版之手列名單裡本來就沒有它**。二者一致，但這一次是**量出來的一致**。
`play`／`enter`／`launch` 三個手列動詞**語料中一次也沒出現** ——
前版有三個從未被行使的分支。

### 5.2 WARN —— 聯集外動詞須人審（本輪首次觸發）

```
[WARN]   8 §5.4  …；步驟起首動詞 ['Bring', 'Open', 'Start', 'Terminate']；
         語料聯集 ['Open', 'Read', 'Select', 'Send', 'Start', 'Stop']
         （ACCESS ['Open','Select','Start']／STIMULUS ['Send','Stop']／未分類 ['Read']）；
         聯集外 ['Bring', 'Terminate']　**聯集外動詞須人審**
```

`Bring`（power 線之通稱式風格，R-DD20 v2(b) 所許）與 `Terminate`（037 Method 逐字）
**皆為本批新引入**。WARN **不使自檢 exit 1**，其義為「機械判準不足，須人審」。

**請分析層裁**：本批入語料後，`Bring`／`Terminate` 應歸 ACCESS／STIMULUS／未分類？
（10-3。在裁定前，二者不參與 `RE_ACCESS`，故檢 9／11 對本批之 fail-safe 面
**本來就無適用對象**（本批 0 則 fault），無實質影響。）

---

## 六、⚠ 一件生成後自查才發現的 —— 檢 13 之 detail 又印錯了理由

`-001`／`-002` 首次跑出來時，檢 13 之 detail 是：

```
001／002 → 狀態轉換 (State Transition Testing)（同一訊號於 PC 與 procedure 得二相異值（A→B）…）
```

**但它們並不是由那個分支命中的** —— 是由本輪新加的 ER 極性對比命中的。
成因：`_want()` 只回傳方法名，detail 再拿方法名去查一張理由表
（`_WHY[方法]`），**於是同一方法之不同分支印出同一句話**。

**這與 D8 同族，而且就發生在我上一包剛修完 D8 之後。**
上繳 13 §8.4 寫的是「detail 導出與判斷正確是兩個獨立性質」——
這裡是第三種：**detail 是導出的、判斷也是對的，但「理由」是回查來的。**

**修法**：`_want()` 改回傳 `(方法, 實際命中之分支)`，分組之鍵改為二元組。修後：

```
001／002 → 狀態轉換 (State Transition Testing)
          （ER 對同一組實詞 ['hu', 'messages', 'periodic'] 分作否定與肯定之斷言（A→B））
```

**順帶修檢 11 之同型**：0 則 fault 時，舊 detail 仍書
「皆先建立正常態再注入，未假設隱藏狀態」—— **一個沒有主詞的斷言**。
改為「本產物無 simulated fault（`Stop transmitting`／`timeout` 0 命中）
—— **無適用對象，非「已驗證」**」。

---

## 七、未結 DR 清單（DD1–DD9）

| DR | 狀態 | 等級 | 阻斷之範圍 | 台帳項 |
|---|---|---|---|---|
| **DR-DD1** | DRAFTED | **必發** | `-025`~`-028`（4）**仍凍結** | A-DD1 |
| DR-DD2 | DRAFTED | 緩發 | 不阻斷 | A-DD2 |
| ~~DR-DD3~~ | **RESOLVED** | — | — | ~~A-DD5~~ |
| DR-DD4 | PARTIALLY ANSWERED | 緩發 | 不阻斷 | A-DD6 |
| **DR-DD5** | DRAFTED | **必發** | 已解凍；回覆不符 → 8 TC 機械換值 | A-DD8 |
| **DR-DD6** | DRAFTED | **必發** | 同上；`MTA(2)`／`DDCT(3)` 硬邊界 | A-DD9 |
| DR-DD7 | DRAFTED | 緩發 | 不阻斷 | A-DD7 |
| **DR-DD8** | DRAFTED | **必發** | `-013`／`-015` 之負向側（範圍依 10-5）| **[CG-DD1]** |
| **DR-DD9** | DRAFTED | **必發** | **`-002` 之 `$` 指令行 → 該則不得出貨** | **A-DD10** |

**八筆未發送；DD3 已結案。**

### 7.1 阻斷疊圖（本輪後）

| leaf | 狀態 | 未結之阻斷 |
|---|---|---|
| **`-001`** | **已產出**（本輪）| A-DD10（marker）—— **可出貨** |
| **`-002`** | **已產出**（本輪）| **DR-DD9 —— 含 PENDING，不得出貨**（IN §8.4.3）|
| `-003`~`-016` | 已產出 | `-013`／`-015` 另有 [CG-DD1]＋DD8 |
| `-017`~`-024` | 已產出 | DD5／DD6（marker）|
| `-025`~`-028` | **凍結** | **DR-DD1** |

**28 leaf 中 24 則已產出（其中 1 則不得出貨）、4 則凍結。**
`framework.md` Layer 2 之六組，**五組已全數產出**，餘 `Market Speed Gating`（凍結）。

---

## 八、獨立自評

### 8.1 我做對的

1. **生成前先跑一次舊檢，把基線紅量出來。** 若先修檢再生成，
   §4.1 那三項就會被我的修改吞掉，**永遠不知道舊檢對這批是什麼態度**。
   量了才看得出：`\d` 那一項是**往綠**的漏放，不是往紅的誤攔。
2. **priority 沒有照下放包寫。** §三 的表白紙黑字寫 P0，照抄最省事，
   而且自檢會立刻紅給我看 —— 但紅了我就得改 profile §4，**那是 Pei 裁准的表**。
   照 profile 生成 P1、把衝突提上去，是唯一不越權的路。
3. **`[IGN_LK]` 沒有寫進四欄。** R-DD20 v2(b) 要求錨定 CFTS009 逐字，
   而 power 線之 profile §3.2 恰好有一條允許 `[Nh]` 逐字記法的 profile-scoped OVERRIDE。
   **比附過去很順手** —— 但那是 power 的 profile，不是 DD 的。
4. **注入表把「包 16 之檢」欄一起印出來，並在正文說明它幾乎都是基線紅。**
   不說明就會被讀成「舊檢也攔得到」，那是反過來替舊檢說了它沒有的好話。
5. **§六 那個錯是我自己跑出來看到的**，不是誰指出來的 ——
   而它就發生在我上一包剛寫完「下一次的分類，判準要分兩欄」之後。**第三欄是理由。**

### 8.2 我做糙的

1. **檢 13 之新分支（ER 極性對比）之門檻「交集 ≥3 實詞」是我定的。**
   3 這個數字沒有量過偽陽／偽陰 —— 我只驗了「三個既有產物不誤攔」。
   **那是必要條件，不是充分條件。**
2. **`NEG` 與 `STOP` 兩個字集同樣是手列的。** 與 §5.1 剛償還完的 `RE_ACCESS` 同型 ——
   **我在修掉一個手列名單的同一輪裡，新增了兩個。** 記在這裡，不辯解。
3. **marker 義務表新增 `Body OFF|Body Off → A-DD10` 是登記式，不是導出式。**
   它與既有二列同型（由裁決所命），故我照該體例加 —— 但整張表的性質是
   「人手維護，漏加即漏檢」，**和上繳 12 §5.2 罵過的白名單是同一個東西**。
   差別只在它的每一列都可回指一條裁決。**這個差別是真的，但不大。**
4. **`-002` 之 `$` 佔位含中文**（`<DD process 終止指令>`）。R-DD20(c) 之圍籬逐字如此，
   故照寫 —— 但工作簿其餘皆為英文，這一格會很突兀。建議見 10-4。
5. **取樣 feature 與他批共用**，且 `-001` 用了 B1 `-013`／`-014` 已用過的
   `Player Song…`。素材面無可選（§3.4），但**同一個 feature 在四則 TC 裡出現**
   會讓人讀不出它們在驗不同的事。

### 8.3 我拒絕做的

1. **不改 profile §4 使 `-001` 成 P0**（§3.1 甲）。
2. **不把 `[IGN_LK]` 寫進四交付欄**，也不自行給 DD profile 加一條比附 power §3.2 之例外。
3. **不把 `Bring`／`Terminate` 逕自歸類進 `RE_ACCESS`** —— 那會使 T23b 的
   「語料導出」退回成「我說了算」，只是換個地方說。故轉 WARN。
4. **不改 R-DD20 v2、不改 A-DD10 之狀態。**
5. **不寫 `docs/fw036/RULINGS.sha.tsv`**（10-4 已裁：tsv 延後，以錨點數為準）。
6. **`-002` 未因「含 PENDING 不好看」而降轉 NA** —— IN §8.4.3：NA 僅限確認不適用。

### 8.4 一件我原本會漏的

**`RE_ACCESS` 改成導出式之後，我差點沒發現 `play`／`enter`／`launch` 從未被行使。**

分類表跑出來時我先看的是「ACCESS 有沒有含 open/start/select」——
有，於是就想收工。回頭比對手列名單才注意到：**手列六個，語料只出現三個**。
另外三個在這個 feature 裡**一次也沒有出現過**。

> 它們不是錯的，是**空的**。
> 空的分支和恆偽的條件（上繳 13 §3.2 乙）差在哪？
> **恆偽的條件會讓人以為有在檢；空的分支會讓人以為涵蓋得比較廣。**
> 兩者都是在輸出上看不出來的 —— 而這一次，
> **是因為換成導出式，那三個才自己掉出來。**

---

## 九、量測條件揭露（R-G8）

### 9.1 分子與分母

| 所書 | 分子 | 分母 | 方法 |
|---|---|---|---|
| 「24 PASS ／ 1 N/A ／ 1 WARN ／ 0 FAIL」| 各檢之 verdict | 26 檢 | `SC_ARTIFACT=batch_body_off_init.json python3 scripts/selfcheck_tcs.py` |
| 「上半 35／42 tok」| `len(037 c3.split())` | cap 50 | `gen_body_off_init.py`；逾 cap 即 `assert` 中止，**不逕截** |
| 「語料 65 步」| 三產物之 `test_procedure` 編號步驟數 | pilot 12 ＋ B1 29 ＋ B2 24 | 檢 8 之 detail |
| 動詞分類表（§5.1）| 逐動詞之 UI／訊號命中步驟數 | 該動詞之全部步驟 | `_build_access()`；UI＝`"…"` 且非 `^[A-Z][A-Z_0-9]*$` |
| 「錨點 22 ／ 索引現行 20 ／ 留存 2」| `grep -c` | `RULINGS.md` | `^## R-DD` ／ `^\| R-DD` ／ 留存表列數 |
| 「逐字元差異 0」| 落檔 vs 下放包 | R-DD20 v2 1241 字元 | Python 字串全等 |
| p7 黃標（§3.4）| `non_stroking_color == (1.0,1.0,0.0)` 之 rect | 該頁全部 rect | `pdfplumber`，x0∈[61,132]（分類欄）|

### 9.2 注入之條件

- 注入檔寫於 `generated/inj17_*.json`，**每組跑完即 `os.remove`**；
  跑後 `ls generated/` 僅餘四個正式產物（已核）。
- 包 16 之自檢副本置於 `scripts/_sc_p16_tmp.py`，**跑完即刪**（已核）。
- 二者以同一 `SC_ARTIFACT` 值餵入，除腳本外無差異。

### 9.3 本輪未量測者

1. **檢 13 新分支之門檻 3 的偽陽／偽陰率**（§8.2-1）—— 未量。
2. **`NEG`／`STOP` 二字集之涵蓋**（§8.2-2）—— 未量。
3. **`-002` 之台架可執行性** —— `PENDING` 未結，無從量。
4. **寫回工作簿之任何面** —— 本輪未寫回。
5. **`Bring`／`Terminate` 入語料後之分類** —— 待 10-3 裁定，未逕算。

---

## 十、待分析層／Pei

| # | 事項 | 為何須分析層 |
|---|---|---|
| **10-1** | **`-001` 之 priority：下放包 17 §三 書 P0，profile §4（Pei 裁准）之 PR-c 與其列表書 P1** —— 本輪照 profile 生成 P1 | 改 P0 須連帶改 profile §4 之規則文與 8+20 閉合；profile 為 Pei 裁准 |
| **10-2** | **檢 6 之母體更正須追認** —— `$` 指令行不計入步驟字數。**R-DD15 明文「逾限改步驟不改尺」**，本輪主張此為母體之更正而非放寬（注入 J 為證），惟仍請裁 | R-DD15 之解釋權 |
| **10-3** | **`Bring`／`Terminate` 之歸類**（T23b 之 WARN）—— 本批是否入語料？入後二動詞歸 ACCESS／STIMULUS／未分類？ | 語料之納入為判準之變更 |
| **10-4** | **`-002` 之 `$` 佔位含中文**（`<DD process 終止指令>`，R-DD20(c) 圍籬逐字）。建議改 `<DD process termination command>` | 改動裁決所命之字串 |
| 10-5 | 取樣 feature 與他批共用（§3.4、§8.2-5）—— 可用列僅 5 個，根因為 [CG-DD1]／DR-DD8 | 是否接受共用，或先發 DD8 |
| 10-6 | §8.2 之三項自認（門檻 3 未量、`NEG`／`STOP` 手列、marker 表為登記式）| 是否要求補量 |

**本輪未動**：`generated/` 之三個既有產物、工作簿、git、`docs/fw036/`、
`features/power/`、`docs/runtime/profiles/`。
