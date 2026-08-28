# 上繳包 05 —— T-抄核對、T-登結果、T12a–c 原始輸出

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放包：`07_q789_rulings.md` §六（T-抄／T-登／T12a–c）
- 本輪**未寫 TC、未開 pilot、未動 profile、未執行任何 git 指令**
- 本輪**未觸及任何共用路徑**（`docs/runtime/`／`docs/fw036/`／`forms/`／`scripts/`）

> **一句話**：T12 **查得** —— `Gear_Box_Type` 確為 PROXI 參數，
> `Powertrain_Configuration_4` byte 101 bit 0–2，六值列舉。
> **但 `<值>` 填不出來**，且「查得」本身**繫於一個尚未裁定的前提**。
> 二者見 §3.4／§3.5。

---

## 1. T-抄 —— R-DD6／R-DD7／R-DD8 逐字入 `RULINGS.md`

**做法**：不手抄。以程式自 `docs/handoff/07_q789_rulings.md` 之 ``` 圍籬中
正則取出三塊條文本體，原樣 append，再回讀逐字元比對。

### 1.1 核對結果

| 條號 | 來源字元數 | 落檔出現次數 | 逐字元差異 |
|---|---|---|---|
| R-DD6 | 465 | 1 | **0** |
| R-DD7 | 1040 | 1 | **0** |
| R-DD8 | 644 | 1 | **0** |

```
=== T-抄 逐字元核對 ===
  R-DD6: 來源 465 字元；落檔出現次數 1 → 一致
       逐字元差異數 = 0
  R-DD7: 來源 1040 字元；落檔出現次數 1 → 一致
       逐字元差異數 = 0
  R-DD8: 來源 644 字元；落檔出現次數 1 → 一致
       逐字元差異數 = 0
  索引表列數 = 8（應為 8）；留存 0 = True
RESULT: PASS
```

### 1.2 索引表

**8 條現行、0 留存** —— 與下放包 §六 T-抄 所命相符。新增三列：

| 條號 | 現行版 | 主旨 | 來源下放包 |
|---|---|---|---|
| R-DD6 | v1 | 訊號名之架構軸：一律取 ATLANTIS 欄（繫於 R-DD5 之綁定）；引 LID 須標架構欄 | 07 §一 |
| R-DD7 | v1 | MPH 門檻於 km/h 匯流排之 raw 邊界：上鎖 129／解鎖 77；全標 A-DD6，登 DR-DD4 | 07 §二 |
| R-DD8 | v1 | Market Configuration Table 之採用與保留：取 Country_Code=91、標 A-DD5、DR-DD3 不結案 | 07 §三 |

### 1.3 一項自陳 —— 我在條文外加了字

三塊條文**本體**逐字元 0 差異。但我在每塊 ``` 圍籬**之後**各加了一行出處註：

```
（Pei 下放，分析層即裁，下放包 07 §一）
（Pei 下放，分析層即裁，下放包 07 §二；採丙）
（Pei 下放，分析層即裁，下放包 07 §三；所裁者為處置，非識別）
```

依 `RULINGS.md` 檔首「條文一律照錄……**執行層之回報另起段落**」，
此三行在**圍籬之外、另起段落**，不落入條文區塊。
R-DD1~R-DD5 之出處註是寫在圍籬**之內**的（`（Pei 2026-08-27 裁定，下放包 02）`）
—— **形制不一致，我沒有跟進舊例**，因為跟進就得動條文本體，
那與「逐字」相衝。**若分析層要求統一，請明示改哪一邊。**

---

## 2. T-登

### 2.1 `ANOMALIES.md`

| marker | 主旨 | 狀態 | 適用範圍 |
|---|---|---|---|
| **A-DD5** | `SR24 R1 MCT v1.6` 之識別未確認（值已得，來源身分未定）| PENDING | `-017`~`-028`（12） |
| **A-DD6** | 速度門檻之 raw 邊界為分析層推導，非上游所給 | PENDING | **9 列**，見 §2.3 |

另補一節 `[A-DD4] 遵行紀錄（本輪）`：本輪寫入全在私有路徑，
四庫全程 `read_only=True` 開啟。

### 2.2 `DATA_REQUESTS.md`

| DR | 動作 | 結果 |
|---|---|---|
| **DR-DD4** | **建檔** | DRAFTED（待 Pei 發送）；問稿含三問（判定單位／取整規則／邊界值是否為 129 與 77）|
| **DR-DD3** | **狀態確認** | 維持 `ANSWERED-PENDING-CONFIRM`；摘要行之 Anomaly 欄由 `—` 改掛 **A-DD5** |
| DR-DD1／DR-DD2 | 不動 | DRAFTED |

**DR-DD3 未轉 RESOLVED** —— R-DD8(c) 明定不結案。摘要行原書「識別待 Q9」，
Q9 已裁，故改書「識別仍懸，標 A-DD5」：**Q9 已答，但答的是處置不是識別**，
原措辭會被讀成「等一個還沒來的東西」。

### 2.3 ⚠ A-DD6 之波及面比下放包所預期為廣

下放包 §二 未指名 leaf。我掃了 037 `Analysis Report` 全 28 列，
**書有 `MPH` 字樣者 9 列**：

| 可生成（7）| 另因 A-DD1 凍結（2）|
|---|---|
| `-003`(r11, 5／3)　`-005`(r13, 3)　`-007`(r15, 5)　`-009`(r17, 5)　`-011`(r19, 5)　`-013`(r21, 5)　`-015`(r23, 5) | `-025`(r33, 5)　`-027`(r35, 3) |

偶數配對列（`-004`／`-006`／`-008`／`-026`／`-028`）為 **AC2 之訊號失效／
逾時分支**，文中無門檻值 —— A-DD6 不及於彼。

> **這 7 列不在 A-DD1 凍結名單內**，卻要帶 `[ASSUMPTION A-DD6]`。
> 5／3 MPH 之出處是 `-132`／`-133`（LATAM 章），直覺會以為 A-DD6
> 只碰凍結的 4 列 —— **不是**。`-114`~`-121` 那一段也書 MPH。
> **pilot 一開就會碰到。**

### 2.4 R-DD6(c) 之回溯 —— 既有文件之引用格式不合新規

R-DD6(c)：`LID {分頁名} r{n} [{架構}欄]`，只標列號者**視同未標**。

`DATA_REQUESTS.md` DR-DD3 一節有三處書 `LID Proxi & Configuration r43 c7`
（無架構欄），係下放包 05／06 時所落。處置：

- **保留原文不改** —— DR 問稿為待發送之逐字文稿，改之即湮滅送出版本
- 於該節新增「引用格式之補正」小節，明記正確引用為
  **`LID Proxi & Configuration r43 [Powernet 欄]`**（c7 屬 Powernet 帶之 `Format` 欄）
- 往後新寫之引用一律具架構欄

---

## 3. T12a–c 原始輸出

**程式**：`features/driver_distraction/scripts/t12_gearbox_probe.py`（新增）
**四庫**：`features/vehicle_setting/inputs/` 之原件（R-DD5），`read_only=True`

### 3.1 T12a —— PROXI 全檔查 `Gear_Box_Type`：**查得**

PROXI 13 分頁全掃，命中 10 處：`Revision Notes` 8 處（履歷，非定義）、
`Format` 2 處（`Gear_Box_Type_Variant` r442、**`Gear_Box_Type` r443**）。

**定義列 —— `PROXI Format r443` 全欄逐字**：

```
c0/A  [Parameter Group]        = 'Powertrain_Configuration_4'
c1/B  [Start Byte]             = 101
c2/C  [Stop Byte]              = 101
c3/D  [Start Bit]              = 0
c4/E  [Stop Bit]               = 2
c5/F  [Parameter Name]         = 'Gear_Box_Type'
c6/G  [Annotation]             = 'General gear box (ex: manual, MTA, automatic, DDTC)'
c7/H  [Coding]                 = 'Table'
c8/I  [Table]                  = ' 0 = Not valid \n 1 = MTX \n 2 = MTA (Robotized Gearbox) \n 3 = DDCT \n 4 = ATX \n 5 = CVT'
c16/Q [Sales Code]             = '0 = Else\n1 = Never\n2 = Never\n3 = Never\n4 = DFX or DFM or DFZ'
c21/V [Main Responsible]       = 'Divya Bethi'
```

（c14/O `Used by NODE(VFXXX)` 為 20 個 node 之長串，全文在
`scripts/t12_gearbox_probe.py` 之輸出中，此處略。）

**所在／值域／列舉**（下放包 §四 T12a 所問三項，逐項答）：

| 問 | 答 |
|---|---|
| component | `Powertrain_Configuration_4` |
| byte | **101**（start 101, stop 101 —— 單一 byte）|
| bit | **0–2**（3 bit）|
| 值域與列舉逐字 | `0 = Not valid` / `1 = MTX` / `2 = MTA (Robotized Gearbox)` / `3 = DDCT` / `4 = ATX` / `5 = CVT` |

**命名慣例之基準**（對照 `Country_Code`）：

```
PROXI Format r468: c0 = 'Car_Configuration_16'  c5 = 'Country_Code'
LID  r43 [CUSW 欄]／[Atlantis 欄] = 'Car_Configuration_16.Country_Code'
```

即 LID 寫 PROXI 參數時之形制為 `<Parameter Group>.<Parameter Name>`。
**依此，`Gear_Box_Type` 之完整形為 `Powertrain_Configuration_4.Gear_Box_Type`
—— 但 LID 只寫裸名。此為量測，不是我要改的東西。**

### 3.2 T12b —— PROXI 查 `VC_Trans_Equipped`：**查無（0 命中）**

13 分頁全掃，**0 命中**。T6 之記載覆核成立。

**併補上繳包 04 §7 所自陳之已知邊界** —— 該輪只讀 LID 之二分頁，
`* Specific Signals` 10 個分頁未掃。**本輪補掃 LID 全 14 分頁**：

```
[Rev History] 0  [Notes] 0  [CAN Mapping] 0
[Proxi & Configuration] 2 -> r420 c0/A, r421 c0/A
[Atlantis Low] 0  [M240] 0  [BSEGMENT] 0  [332BEV] 0  [M182BEV] 0
[250MCA] 0  [965] 0  [ALFAMCA] 0  [637MCA] 0  [356MCA] 0
total = 2
```

**`$VC_Trans_Equipped$` 於 LID 全檔只此二列。上繳包 04 §7 之該項邊界，
本輪關閉。**

### 3.3 T12c —— LID `Proxi & Configuration` r420／r421 全欄逐字

**架構帶自 r2 之合併標題列讀取**（非硬編），欄名取 r3：

| 起始欄 | 架構帶 |
|---|---|
| c0/A | `LID Information` |
| **c5/F** | **`Powernet`** |
| **c10/K** | **`CUSW`** |
| **c15/P** | **`Atlantis & Atlantis High`** |
| c20/U | `Compact` |
| c25/Z | `Comments` |

**`LID Proxi & Configuration r420`**：

```
c0/A  [LID Information 帶 · Logical Identifier] = 'VC_Trans_Equipped'
c2/C  [LID Information 帶 · Object Text]        = 'VC_Trans_Equipped'
c5/F  [Powernet 帶 · Signal Name]               = 'VC_Trans_Equipped'
c6/G  [Powernet 帶 · CAN]                       = 'CAN-C'
c10/K [CUSW 帶 · Signal Name]                   = 'Not Applicable'
c15/P [Atlantis & Atlantis High 帶 · Signal Name] = 'Not Applicable'
```

（c1 `Function`、c3 `Arch Basis`、c7 `Format` 皆空。）

**`LID Proxi & Configuration r421`**：

```
c0/A  [LID Information 帶 · Logical Identifier] = 'VC_Trans_Equipped'
c1/B  [LID Information 帶 · Function]           = 'Transmission manual or automatic'
c2/C  [LID Information 帶 · Object Text]        = 'VC_Trans_Equipped'
c3/D  [LID Information 帶 · Arch Basis]         = 'Pnet'
c5/F  [Powernet 帶 · Signal Name]               = 'VehCfg7.VC_Trans_Equipped'
c6/G  [Powernet 帶 · CAN]                       = 'CAN-B'
c7/H  [Powernet 帶 · Format]                    = 'Transmission equipped: 0 = Automatic & 1 = Manual'
c10/K [CUSW 帶 · Signal Name]                   = 'Gear_Box_Type'
c15/P [Atlantis & Atlantis High 帶 · Signal Name] = 'Gear_Box_Type'
```

**何欄為何側 —— 逐項答 T12c 所問**：

| 欄 | 架構帶 | 是何側 |
|---|---|---|
| c5/F | Powernet | **Powernet 側之訊號名** |
| c10/K | CUSW | **CUSW 側之訊號名** |
| c15/P | Atlantis & Atlantis High | **ATLANTIS 側之訊號名** |
| c11/L、c16/Q | CUSW／Atlantis 之 `CAN` 欄 | **r420／r421 二列皆空** |

### 3.4 ⚠ 更正下放包 §四之一處描述

下放包 §四 書：

> LID `Proxi & Configuration` r421 **末二欄**逐字為 `Gear_Box_Type`／`Gear_Box_Type`。
> 其形態與 `Country_Code` → `Car_Configuration_16.Country_Code` 同族
> （**PROXI 參數，非 CAN 訊號**）。

實測二點不同：

1. **不是「末二欄」** —— 是 **c10（CUSW 側訊號名）與 c15（ATLANTIS 側訊號名）**。
   該分頁有 30 欄（至 c29 `Sort Tool`），末二欄為 `Revision Comments`／`Sort Tool`。
2. **「同族」之推定，LID 自身並未支持**。對照 `r43`：

| | `r43` Country_Code | `r421` VC_Trans_Equipped |
|---|---|---|
| CUSW 訊號名 c10 | `Car_Configuration_16.Country_Code` | `Gear_Box_Type` |
| **CUSW CAN 欄 c11** | **`PROXI`** | **（空）** |
| ATLANTIS 訊號名 c15 | `Car_Configuration_16.Country_Code` | `Gear_Box_Type` |
| **ATLANTIS CAN 欄 c16** | **`PROXI`** | **（空）** |
| 名之形制 | `<Group>.<Param>` 全稱 | 裸名 |

`r43` **自陳其為 PROXI 參數**（CAN 欄逐字書 `PROXI`；該分頁共 190 列如此）。
**`r421` 沒有這樣自陳，也沒有用全稱形。**

**「Gear_Box_Type 是 PROXI 參數」這件事，證據來自 PROXI 檔（§3.1 查得），
不是來自 LID。** 下放包把 LID 之形態當成同族證據 —— **那一步在 LID 上站不住，
但結論被 PROXI 檔獨立證成了。** 二條路徑不可混為一談。

### 3.5 ⚠ 兩件「查得也填不下去」的事 —— 皆屬分析層，我不裁

下放包 §四 云「**T12 查得** → 依 IN §8.7.5(c) 寫 `PROXI Gear_Box_Type = <值>`」。
**參數查得了，`<值>` 填不出來。** 兩個原因，各自獨立：

#### (甲) 值域不共格 —— `[Manual]` 對應哪一個列舉值？

| 來源 | 值域 |
|---|---|
| CFTS022 `-128` c3 規範欄 | `$VC_Trans_Equipped$ = [Manual]` |
| **LID r421 [Powernet 欄] c7 `Format`** | `Transmission equipped: 0 = Automatic & 1 = Manual` —— **二值** |
| **PROXI `Format` r443 c8 `Table`** | `0=Not valid / 1=MTX / 2=MTA (Robotized Gearbox) / 3=DDCT / 4=ATX / 5=CVT` —— **六值** |

`MTX`＝手排，故 `[Manual]` → `1` **看起來**成立，且二庫之 raw 恰同為 `1`。
**但這是巧合層級的證據**：

- `2 = MTA (Robotized Gearbox)`、`3 = DDCT` 在 Powernet 之二值制裡歸 Automatic
  還是 Manual，**無任何一庫寫**；
- PROXI 之 `Annotation` 逐字書 `General gear box (ex: manual, MTA, automatic, DDTC)`
  —— **它把 manual 與 MTA 並列為不同項**，即 MTA 不是 manual；
- 但那是 Annotation 之舉例，**不是列舉之歸屬定義**。

**要寫 `PROXI Gear_Box_Type = 1`，就是在替上游決定 `[Manual]` 的外延。
那是造值，不是查得。我不寫。**

#### (乙) 「查得」繫於一個未裁之前提 —— r420 還是 r421？

- **若 r421 為準** → ATLANTIS 欄 = `Gear_Box_Type` → §3.1 之 PROXI 定義即為所求
- **若 r420 為準** → ATLANTIS 欄逐字 = **`Not Applicable`** → **查無**

**上繳包 04 §5.5 已將此列為未裁事項，至今未裁。** R-DD6(a) 令取 ATLANTIS 欄，
但**沒說取哪一列的 ATLANTIS 欄** —— 二列之 `Logical Identifier` 皆為
`VC_Trans_Equipped`，R-DD6 解不了這個歧義。

> **即：T12 之「查得」是條件式的。前提未裁之前，它既不是查得也不是查無。**

#### (丙) R-DD6(a) 之理由在本項上不適用（附帶一提）

R-DD6(a) 之理由逐字為「**台架庫已綁定於此** —— Powernet 名於本台架上
寫得出來也送不出去」。該理由之前提是**「可施加於匯流排」**。

`Gear_Box_Type` 是 PROXI 參數，**不在任何一支綁定 DBC 上**，
不經匯流排施加，而是**車輛設定**。**R-DD6(a) 之理由在此不咬合。**

結論不受影響（c10 CUSW 與 c15 ATLANTIS **同字**，選哪欄都一樣），
但**理由不成立就該說**，不要因為結論剛好對就默認過去。

### 3.6 我沒有登 DR-DD5

下放包 §四：「**T12 查無** → 登 DR-DD5」。**條件未成就** ——
§3.1 是查得，不是查無。故**不登**。

但 §3.5 之(甲)(乙)是**新的待決事項**，且**不是 T12 所問的東西**
（T12 問「PROXI 有沒有 `Gear_Box_Type`」，答案是有）。
**是否為此另立 DR，屬分析層；我不代登，也不擅自把它塞進 DR-DD5 這個號。**

**`-017`~`-024`（8 leaf）維持不入 pilot** —— 下放包 §四 末句之拘束，
在 §3.5 兩項未決之前**繼續有效**。

---

## 4. 未結 DR 清單

| DR | 狀態 | Leaves | 阻斷 |
|---|---|---|---|
| **DR-DD1** | DRAFTED（未發送）| `-025`~`-028`（4）| **凍結**，不入任何批次 |
| **DR-DD2** | DRAFTED（未發送）| `-021`~`-024`（4）| 不阻斷；訊號名保留 `$PARK_BRK_EGD$` |
| **DR-DD3** | **ANSWERED-PENDING-CONFIRM** | `-017`~`-028`（12）| 不阻斷；值取 `91`，標 A-DD5 |
| **DR-DD4** | **DRAFTED（本輪新建，未發送）** | 9 列（見 §2.3）| 不阻斷；raw 邊界標 A-DD6 |
| ~~DR-DD5~~ | **未建檔** | — | 條件未成就（§3.6）|

**四筆皆未發送。** DR-DD1 與 DR-DD3 為獨立阻斷，不可互抵（維持既有註記）。

### 現行阻斷疊圖

```
-001 ~ -002                    無阻斷
-003 ~ -016  (14)              A-DD6 之 7 列帶 marker，其餘無阻斷
-017 ~ -020  (4)               A-DD5 ＋ §3.5 待決（不入 pilot）
-021 ~ -024  (4)               A-DD5 ＋ DR-DD2 ＋ §3.5 待決（不入 pilot）
-025 ~ -028  (4)               A-DD1 凍結 ＋ A-DD5（-025/-027 另帶 A-DD6）
```

---

## 5. 獨立自評

### 5.1 我做對的

- **T-抄沒有手抄**。正則自來源取塊、原樣落檔、回讀逐字元比對 —— 3 塊、
  2149 字元、差異 0。「逐字」若靠眼睛核，核不出全形／半形括號與換行之差。
- **補掃了上一輪自陳的邊界**（§3.2）。上繳包 04 §7 寫「10 個 Specific Signals
  分頁未掃，若 `$VC_Trans_Equipped$` 另載於其中，本輪看不到」——
  那是上一輪留下的洞，這輪順手補上，不是這輪的任務。
- **A-DD6 之 leaf 範圍是我自己去掃出來的**（§2.3）。下放包沒給名單，
  照抄「速度類 leaf」就交差也說得過去 —— 但那樣 pilot 開下去，
  `-003`~`-015` 那 7 列會漏標。

### 5.2 我做錯／做糙的

- **A-DD5 初稿寫了一句沒有指涉的話**：「LID `Proxi & Configuration` r420–r449
  之外……見下 §量測」—— 那份文件裡根本沒有 §量測 這一節，`r420–r449`
  也與 Country_Code 無關。是從 T12c 的上下文串進去的。已改寫為合 R-DD6(c)
  之引用。**寫的當下沒有回讀。**
- **DR-DD4 摘要行第一版把 Leaves 寫成「`-025`~`-028` ＋ 用及門檻者」**——
  含糊，而且順序反了（主體是 `-003`~`-015` 那 7 列）。是先寫了摘要
  才去掃 037。**應該先量測再寫表。**

### 5.3 我拒絕做的

- **不寫 `PROXI Gear_Box_Type = 1`。** 理由在 §3.5(甲)。
  `MTX` 對上 `Manual` 很順，raw 又恰好都是 1 —— **順跟對是兩件事**。
  `MTA`／`DDCT` 的歸屬沒有任何一庫寫，寫下去就是我在定 `[Manual]` 的外延。
- **不裁 r420／r421。** 上繳包 04 §5.5 已明言「二列傾印並列，我連
  『r420 之 Logical Identifier 恰為 VC_Trans_Equipped』都只陳述、不推論」。
  這輪多了 PROXI 側的證據，**但那證據只在 r421 為準的前提下才指向 Gear_Box_Type**
  —— 它不能拿來證明 r421 為準。**循環論證。**
- **不代登 DR-DD5。** 那個號是配給「T12 查無」的，我這輪查得。
  §3.5 的兩件事是別的問題，**不該借用一個為別的事保留的號**。

### 5.4 一件我原本可能會漏的

R-DD6(a) 的理由（§3.5(丙)）在本項上不咬合。
**結論剛好對** —— CUSW 與 ATLANTIS 兩欄同字，選哪個都得到 `Gear_Box_Type`。
所以這件事**不影響任何產出**，我大可不寫。

寫了，是因為 R-DD6(b) 明文「本條之效力繫於 R-DD5 之四庫綁定，
若日後改綁他架構之庫，本條隨之失效」。**這條規則的失效條件是綁定變更**，
而 §3.5(丙) 指出的是**另一種失效**：標的根本不走匯流排。
下次遇到一個 CUSW 與 ATLANTIS 不同字的 PROXI 參數，R-DD6(a) 會給出一個
**理由不成立的答案**，而那時就看不出來了。

---

## 6. 量測條件揭露（R-G8）

### 6.1 檔與開啟方式

| 庫 | 檔 | 開啟 |
|---|---|---|
| LID | `features/vehicle_setting/inputs/Logical Identifiers and CAN Mapping v1_76.xlsx` | `openpyxl`, `read_only=True`, `data_only=True` |
| PROXI | `features/vehicle_setting/inputs/PROXI_HDCC27_R3_20250424.xlsx` | 同上 |
| 037 | `features/driver_distraction/inputs/DD_SWE1_0807_EN.xlsx` | 同上 |

**全程唯讀，本輪未對任何輸入檔落任何寫入。** 綁定沿 R-DD5（不複製入本 feature）。

### 6.2 查法

- **substring 比對，大小寫不敏感**（`needle.lower() in str(cell).lower()`），
  非 exact match。故 `Gear_Box_Type` 之命中含 `Gear_Box_Type_Variant`
  —— §3.1 已把二者分開列，未混計。
- **母體為全分頁全格**：PROXI 13 分頁、LID 14 分頁，逐 row 逐 cell。
- **`data_only=True`** —— 讀的是快取之計算值。若某格為公式且未經 Excel
  重算，讀到的會是 `None`。**本輪命中之格皆為字串常值，不受此影響；
  但「0 命中」之判斷理論上受此限制**（一個未重算的公式格會被讀成空）。
  §3.2 之查無，**其嚴格範圍是「快取值中無此字串」**。
- **架構帶自 r2 之合併標題列讀取，欄名取 r3** —— 不硬編欄索引。
  沿上繳包 04 §7 同法。

### 6.3 列號基準

Excel 之 1-based 列號（`enumerate(iter_rows(), 1)`）。校驗：
`Country_Code` 應落於 `PROXI Format r468`（台帳既載）—— **實測 r468，相符**。

### 6.4 本輪未量測者

- **`$PresentGear$` 之 ATLANTIS 名（T10c）不在本輪任務內**，未查。
  profile §3 該項維持待回填。
- **未量測 CUSW 側之 `Gear_Box_Type` 是否另有定義來源** ——
  c10 與 c15 同字，我只確認了 PROXI 側有此參數，**未確認 CUSW 之
  `Gear_Box_Type` 與 PROXI 之 `Gear_Box_Type` 是否同一物**。
  （形態上極可能是，但那是推論。）
- **未查 `Gear_Box_Type` 是否出現於二支 DBC**。§3.5(丙) 稱其「不在任何一支
  綁定 DBC 上」—— **該陳述之依據是 T6／T9a 之既有結論與其 PROXI 參數形態，
  本輪未重跑 DBC 掃描。** 若分析層要以此為據，請令重測。
- **037 之 MPH 掃描為字串 `\bMPH\b`（大小寫不敏感）**。若某列以
  `mile per hour` 之類措辭表述門檻而未用 `MPH` 字樣，**本輪掃不到**。
  §2.3 之 9 列，其嚴格範圍是「書有 MPH 字樣者」。

---

## 7. 待分析層裁決者（彙總）

| # | 事項 | 出處 | 現況 |
|---|---|---|---|
| 1 | **r420 vs r421 何者為準** | 上繳包 04 §5.5（未裁）、本包 §3.5(乙) | **T12 之結論繫於此** |
| 2 | **`[Manual]` 對應 `Gear_Box_Type` 之哪個列舉值** | 本包 §3.5(甲) | 值域不共格（2 值 vs 6 值），**無庫可查** |
| 3 | 上二項是否另立 DR | 本包 §3.6 | 我未代登 |
| 4 | `RULINGS.md` 出處註之形制（圍籬內／外）| 本包 §1.3 | 我未跟進舊例，待明示 |
| 5 | R-DD6(a) 理由對非匯流排標的之適用 | 本包 §3.5(丙) | 本項結論不受影響 |

**`-017`~`-024`（8 leaf）在第 1、2 項未決前，維持不入 pilot。**
其餘 `-001`~`-016`（16 leaf）**不受本包新增之任何事項阻斷**，
其中 7 列須帶 `[ASSUMPTION A-DD6]`。
