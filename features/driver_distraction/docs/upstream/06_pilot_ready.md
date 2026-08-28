# 上繳包 06 —— T-抄核對、T-登結果、T13a–c 原始輸出

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放包：`08_arch_close.md` §七（T-抄／T-登／T13a–c）
- 本輪**未改 profile**（分析層自辦）、**未寫 TC／未開 pilot**、**未執行 git**
- 共用路徑：**未寫入**；**讀**了 `forms/…v1_78.xlsx` 一檔（唯讀，見 §2.3）

> **一句話**：T13a 之答案是 **「配對是系統性的，但 r420／r421 之衝突形態不是」**。
> 17 組重複 LID 全為 2 列配對；**14 組之衝突落在 G 欄（Powernet CAN）**，
> 其中 **11 組只差 G 欄**，形態一致為 `CAN-C` → `CAN-B`。
> **r420／r421 是唯一一組衝突觸及 CUSW／Atlantis 訊號名、且唯一一組出現
> `Not Applicable` 者。** 分布在 §3.2–§3.3，**不下結論**。

---

## 1. T-抄 —— R-DD6 v2／R-DD9／R-DD10

### 1.1 逐字元核對

```
=== T-抄 逐字元核對（下放包 08）===
  R-DD6 v2: 來源 1011 字元；落檔出現次數 1 → 逐字元差異數 = 0
  R-DD9:    來源  642 字元；落檔出現次數 1 → 逐字元差異數 = 0
  R-DD10:   來源  387 字元；落檔出現次數 1 → 逐字元差異數 = 0
  R-DD6 v1 留存核對：465 字元；與下放包 07 原文差異數 = 0
  索引：現行 10 條（應 10）／留存 1 條（應 1）
RESULT: PASS
```

### 1.2 出處註之形制已切換

依 §八-4，三條之出處註**由分析層寫在圍籬內**，執行層照錄。
**本輪未另加圍籬外註**（程式驗：三塊之 ` ``` ` 後緊接 `---`）。

R-DD6 v1／R-DD7／R-DD8 之圍籬外三行**依 §八-4 不回修**，原樣保留。
**故本檔現行二制並存** —— 舊三條註在外、新三條註在內。這是 §八-4 所擇，
非未整理；記於此以免日後被讀成漏改。

### 1.3 R-DD6 v1 之留存

沿 `sw_update/RULINGS.md` 之既定形制（未自創）：
**v1 區塊原地不動、不加註、不搬移**；僅索引另立留存表。

| 條號版本 | 已被取代於 | 其所載之失效值 |
|---|---|---|
| `R-DD6`（v1） | R-DD6 v2（下放包 08 §二）| (a) 只書「取 **ATLANTIS 欄**」—— 未區分 `Atlantis` 與 `Atlantis High` 二欄，亦未載二欄不同字時之取捨；**無 (b)**、**無 (e)**。其 (a) 之理由（可施加性）對非匯流排標的不成立 |

索引現行 10 條（R-DD1~R-DD10），留存 1 條。

---

## 2. T-登

### 2.1 `DATA_REQUESTS.md`

| DR | 動作 | 結果 |
|---|---|---|
| **DR-DD6** | **建檔** | DRAFTED；§五 文稿逐字（1341 字元，落檔出現 1 次，差異 0）|
| **DR-DD5** | **列為保留號** | 摘要表新增一列書「未建檔／保留給 r420-r421 件」—— **不是跳號** |
| DR-DD1／2／4 | 不動 | DRAFTED |
| DR-DD3 | 不動 | ANSWERED-PENDING-CONFIRM |

DR-DD5 之保留列是刻意加的：摘要表若從 DD4 直接跳到 DD6，
下一個人會以為漏了一筆或編號出錯。§五 明文「號隨事項配，不隨時序配」，
**那句話得在台帳上看得到，不能只在下放包裡**。

### 2.2 `ANOMALIES.md`

A-DD5／A-DD6 維持 PENDING。A-DD6 依 T13b 加註覆核結果（§4）。
另補 A-DD4 之本輪遵行紀錄。

### 2.3 ⚠ DR-DD6 文稿引之 LID 版本非 R-DD5 所綁

文稿書 `Logical Identifiers and CAN Mapping **v1_78**`；
**R-DD5 綁定者為 `v1_76`**。`v1_78` 在 `forms/`，未入本 feature 之 reference。

**實測二版之 r421**（`Proxi & Configuration`，二版皆 449 列）：

| 欄 | v1_76（綁定）| v1_78（文稿所引）|
|---|---|---|
| A `Logical Identifier` | `VC_Trans_Equipped` | **同** |
| F `Signal Name`（Powernet）| `VehCfg7.VC_Trans_Equipped` | **同** |
| G `CAN`（Powernet）| `CAN-B` | **同** |
| H `Format`（Powernet）| `Transmission equipped: 0 = Automatic & 1 = Manual` | **同** |
| K `Signal Name`（CUSW）| `Gear_Box_Type` | **同** |
| P `Signal Name`（Atlantis & Atlantis High）| `Gear_Box_Type` | **同** |
| `VC_Trans_Equipped` 所在列 | r420／r421 | **同** |
| `Country_Code` 所在列 | r43 | **同** |

**所引各欄逐字相同、列號未位移 —— 文稿內容不誤。**
但**所引版本與綁定版本不一致**，此屬綁定之事：

- **文稿逐字照錄不改**（改之即非 Pei 所發之版本）
- 發送前請擇一：**(甲) 文稿改書 `v1_76`**，或 **(乙) 依 R-DD5 重綁 `v1_78`**
- **執行層不逕改、不逕綁** —— R-DD5 之綁定為裁決事項

> 我沒有把這件事寫成「錯」。二版該列一字不差，**風險是零**。
> 但列號在版本間位移是這類引用最常見的失效模式，
> **這次剛好沒位移，不代表下次不會** —— 所以還是報。

---

## 3. T13a 原始輸出 —— 重複 Logical Identifier 之分布

**程式**：`features/driver_distraction/scripts/t13_probe.py`（新增）

### 3.0 母體判準（R-DD10(c)）

- `LID Proxi & Configuration`，**r4 起至 r449**（r1 表題／r2 架構帶／r3 欄名，**排除**）
- **A 欄 `Logical Identifier` 非空者計入**；空白列排除
- 架構帶自 r2 讀取：`A=LID Information／F=Powernet／K=CUSW／P=Atlantis & Atlantis High／U=Compact／Z=Comments`
- 列號 1-based（R-DD10(d)）；欄書欄名（R-DD10(a)）

```
非空 Logical Identifier 列數 = 446；unique = 429
重複之 LID 名 = 17，佔 34 列
重複組之列數分布：2 列 × 17 組     ← 無三列以上之組
```

### 3.1 「稀疏＋完整」之形態 —— 組內非空欄數

```
相等 12 組／遞增 4 組／遞減 1 組
```

**「上列稀疏、下列完整」只佔 4 組（遞增），且另有 1 組是反向（遞減）。**
`VC_Trans_Equipped` r420(6 欄)→r421(9 欄) 屬遞增之一。

> 即：**若只看非空欄數，「稀疏＋完整」不是該表之慣例**（17 組中 12 組相等）。
> 但非空欄數是個粗指標 —— 見 §3.2。

### 3.2 逐欄比對 —— 17 組之衝突形態

判準：同一欄二列**皆非空且值不同** = 「同欄異值」。

```
**同欄異值**              16 組
純補全（一空一有，無衝突）      1 組   ← Heated_Steering_Levels r99/r100
```

**16 組有衝突。配對本身是系統性的，衝突也是。**

### 3.3 衝突欄之集中度（母體 = 16 組）

```
逐欄之衝突組數：
   G [Powernet 帶 · CAN]                        14 組
   F [Powernet 帶 · Signal Name]                 4 組
   P [Atlantis & Atlantis High 帶 · Signal Name] 3 組
   C [LID Information 帶 · Object Text]          1 組
   K [CUSW 帶 · Signal Name]                     1 組

依「衝突欄之組合」分群：
   G          11 組   SteeringWheelType, VC_SLD_DR_ALRT_CSO, VC_SLD_DR_CHM_CSO,
                      VC_SVC_DELAY_CSO, VC_TEEN_FCW_BRK_CSO, VC_TEEN_FCW_SENS_CSO,
                      VC_TEEN_FT_PRK_VOL_CSO, VC_TEEN_PLG_CHIME_CSO,
                      VC_TEEN_PRK_ASST_CSO, VC_TeenKey, VC_Trans_N_Hold_Prsnt
   F＋G        2 組   VC_AUTO_HL, VC_RemStPrsnt
   C＋F＋P     1 組   DSP_SK_PRSNT
   P           1 組   VC_Launch_Control_PRSNT
   F＋G＋K＋P  1 組   **VC_Trans_Equipped**

G 欄之衝突值配對逐字：
   上列 'CAN-C' → 下列 'CAN-B'    12 組
   上列 'CAN-B' → 下列 'BH-CAN'    1 組
   上列 'CAN-B' → 下列 'CAN-C'     1 組

衝突值含 `Not Applicable` 者：
   VC_Trans_Equipped  r420/r421      ← 全分頁唯一一組
```

### 3.4 `VC_Trans_Equipped` r420／r421 之逐字（四個衝突欄）

```
F [Powernet 帶 · Signal Name]
    r420 = 'VC_Trans_Equipped'
    r421 = 'VehCfg7.VC_Trans_Equipped'
G [Powernet 帶 · CAN]
    r420 = 'CAN-C'
    r421 = 'CAN-B'
K [CUSW 帶 · Signal Name]
    r420 = 'Not Applicable'
    r421 = 'Gear_Box_Type'
P [Atlantis & Atlantis High 帶 · Signal Name]
    r420 = 'Not Applicable'
    r421 = 'Gear_Box_Type'
```

參考：全分頁 `Not Applicable` 之總分布（母體同 §3.0）——
**Powernet 欄 4 列／CUSW 欄 6 列／Atlantis 欄 11 列**。

### 3.5 分布之摘述（量測層，**不判讀**）

下放包 §四 問：「該分頁是否**系統性**存在『稀疏列＋完整列』之配對？」
拆成可量之三問，逐一答：

| 問 | 量測 |
|---|---|
| 配對是否系統性？ | **是。** 17 組全為 2 列，無三列以上；佔 446 列中之 34 列 |
| 配對是否為「稀疏＋完整」？ | **否為主。** 非空欄數相等 12 組、遞增 4 組、遞減 1 組 |
| 配對之衝突是否有共同形態？ | **有一個主形態**：G 欄（Powernet CAN）`CAN-C` → `CAN-B`，11 組**只差此欄**，加上另 3 組共 14 組涉及 G 欄 |
| r420／r421 是否合於該主形態？ | **部分合、部分不合。** 其 G 欄合（`CAN-C`→`CAN-B`）；但它**另有 F／K／P 三欄衝突**，是 17 組中衝突欄最多者（4 欄）|
| r420／r421 是否為唯一形態？ | **在二點上是唯一：**（一）全分頁**唯一**一組衝突值含 `Not Applicable`；（二）**唯一**一組同時在 CUSW 與 Atlantis 二欄之訊號名衝突 |

**以上為分布。r420／r421 何者為準，未裁，我不裁**（下放包 §四）。

> 我把 §3.1（非空欄數）與 §3.2（逐欄比對）分開報，是因為**二者給出不同的像**：
> 只看非空欄數，會得出「稀疏＋完整不是慣例」；逐欄一比，才看到
> **真正的慣例在 G 欄**，而那和「稀疏／完整」無關。
> **若只做 §3.1 就交，結論方向會反。**

---

## 4. T13b 原始輸出 —— 037 門檻表述五組字樣重掃

**母體判準**：`Analysis Report` 全列中含 `SWE1-RA-Driver_Distraction-{n}` 者
（**28 列，無排除**）；比對為全列各格串接後之正則掃描。

| 字樣 | 正則 | 命中 leaf 數 |
|---|---|---|
| `MPH` | `\bMPH\b` | **9** |
| `mph` | `\bmph\b` | **0** |
| `mile` | `mile` | **0** |
| `km/h` | `km\s*/\s*h` | **0** |
| `kph` | `\bkph\b` | **0** |

命中之 9 列與字樣，與上繳包 05 §2.3 **完全相同**：

```
-003 r11  3 MPH, 5 MPH      -009 r17  5 MPH      -015 r23  5 MPH
-005 r13  3 MPH             -011 r19  5 MPH      -025 r33  5 MPH
-007 r15  5 MPH             -013 r21  5 MPH      -027 r35  3 MPH
```

**結果**：037 之門檻**只以大寫 `MPH` 表述**，無 `km/h`／`mile`／`kph` 之措辭。
**上繳包 05 §6.4 所自陳之邊界（「該輪限 MPH 字樣，其他措辭掃不到」），
本輪關閉 —— 且結果不變，A-DD6 之 9 列名單無需修正。**

---

## 5. T13c 原始輸出 —— `Gear_Box_Type` 於二 DBC 之存在性

**這一項是為了關掉我自己上輪的一個未量測斷言**（上繳 05 §3.5(丙)：
「`Gear_Box_Type` 不在任何一支綁定 DBC 上」—— 當時未跑掃描）。

**母體**：二 DBC 全文。四種比對法**分開計**，避免單一寫法之盲區。

```
[PDT27_E2A_R4_BHCAN.dbc]   BO_ 155 訊息／SG_ 914 訊號
    SG_ 定義名                    : 0 命中
    BO_ 訊息名                    : 0 命中
    VAL_ 列舉行                   : 0 命中
    全文裸字串（大小寫不敏感）    : 0 命中
    [對照] SG_ VehicleSpeedVSOSig       : 1 命中
    [對照] SG_ GearEngagedForDisplay_PT : 0 命中

[PDT27_E2A_R5_FDCAN8.dbc]  BO_ 323 訊息／SG_ 2037 訊號
    SG_ 定義名                    : 0 命中
    BO_ 訊息名                    : 0 命中
    VAL_ 列舉行                   : 0 命中
    全文裸字串（大小寫不敏感）    : 0 命中
    [對照] SG_ VehicleSpeedVSOSig       : 1 命中
    [對照] SG_ GearEngagedForDisplay_PT : 1 命中
```

**結論：查無。二 DBC 皆不含 `Gear_Box_Type`，四種比對法皆 0 命中。**

**對照組證明掃描法有效** —— `VehicleSpeedVSOSig` 於二庫皆 1 命中；
`GearEngagedForDisplay_PT` 僅於 `R5_FDCAN8` 命中（與下放包 08 §六
之 `msg 263` 相符）。**若掃描法失效，對照組也會是 0。**

> 上輪 §3.5(丙) 之斷言**方向正確，但當時無據**。現在有了。
> 這也順帶支撐 R-DD6 v2 (e)：`Gear_Box_Type` 確實不經匯流排。

---

## 6. 未結 DR 清單

| DR | 狀態 | Leaves | 阻斷 |
|---|---|---|---|
| **DR-DD1** | DRAFTED（未發送）| `-025`~`-028`（4）| **凍結**，不入任何批次 |
| **DR-DD2** | DRAFTED（未發送）| `-021`~`-024`（4）| 不阻斷生成；保留 `$PARK_BRK_EGD$` |
| **DR-DD3** | ANSWERED-PENDING-CONFIRM | `-017`~`-028`（12）| 不阻斷；值 `91`，標 A-DD5 |
| **DR-DD4** | DRAFTED（未發送）| 9 列（§4）| 不阻斷；raw 邊界標 A-DD6 |
| **DR-DD5** | **保留號，未建檔** | — | 待 T13a 後由分析層定建或不建 |
| **DR-DD6** | **DRAFTED（本輪新建，未發送）** | `-017`~`-024`（8）| **該 8 leaf 不入 pilot** |

**五筆 DRAFTED／ANSWERED 皆未發送。**

### 阻斷疊圖（本包後）

```
-001 ~ -002   (2)    無阻斷
-003 ~ -008   (6)    -003/-005/-007 帶 A-DD6；-004/-006/-008 為 AC2 無門檻
-009 ~ -012   (4)    **組 3 —— pilot 標的**；-009/-011 帶 A-DD6
-013 ~ -016   (4)    -013/-015 帶 A-DD6
-017 ~ -020   (4)    A-DD5 ＋ DR-DD6 → 不入 pilot
-021 ~ -024   (4)    A-DD5 ＋ DR-DD2 ＋ DR-DD6 → 不入 pilot
-025 ~ -028   (4)    A-DD1 凍結 ＋ A-DD5；-025/-027 另帶 A-DD6
```

**組 3（`-009`~`-012`）之阻斷**：無。其中 `-009`／`-011` 須帶
`[ASSUMPTION A-DD6]`（5 MPH 門檻）。**profile §3 之 `$Speedometer$` 已於
下放包 08 §六 解除，pilot 條件成就** —— 惟 profile 為分析層自辦，
**執行層本輪未讀寫該檔，未能自行確認其已落檔**。開 pilot 前請確認。

---

## 7. 獨立自評

### 7.1 我做對的

- **T13a 沒有停在第一層。** §3.1（非空欄數）跑完就交得出去，
  而且會得到一個**方向相反**的像 ——「稀疏＋完整不是慣例（12/17 相等）」。
  逐欄一比才看到慣例在 G 欄。**下放包問的是「稀疏＋完整」，
  但表的慣例根本不在那個軸上。**
- **T13c 有對照組。** 「0 命中」是否定性判斷，最容易的錯法是掃描寫錯而全 0。
  `VehicleSpeedVSOSig`（二庫皆有）與 `GearEngagedForDisplay_PT`（僅 FD 有）
  兩個對照把這個可能排掉。
- **DR-DD6 文稿之版本問題有查而不是有感覺。** v1_78 vs v1_76 我沒有
  「看起來一樣就算了」，逐欄比對了八個欄位並附表。
- **DR-DD5 在台帳上留了保留列。** 下放包在內文說明了「號隨事項配」，
  但台帳是另一個人會讀的東西 —— 只在下放包裡說，台帳上就是一個跳號。

### 7.2 我做糙的

- **T13a 我改了三次腳本才問對問題。** 第一版只數非空欄數（§3.1），
  第二版才做逐欄比對，第三版才做衝突欄集中度。
  **前兩版都會交得出去，而且都會誤導。** 這不是「逐步深入」，
  是我一開始沒想清楚「系統性配對」要用什麼量。
- **腳本最後一次改動把 `__main__` 放在函式定義前**，跑出空輸出，
  再改一次才對。低級。

### 7.3 我拒絕做的

- **不裁 r420／r421。** §3.5 的表已經把「哪些像、哪些不像」全列了，
  但**「G 欄 11 組只差 CAN-C→CAN-B」這個慣例，恰恰解釋不了
  r420／r421 的 K／P 欄衝突** —— 它合主形態的那一半，
  和它不合的那一半，是兩回事。**拿合的那一半去推，就是上繳 05 §5.3
  被採認的那個循環論證換一件衣服。**
- **不改 DR-DD6 文稿之 `v1_78`。** 二版該列一字不差，改了「更正確」，
  但那就不是 Pei 要發的那份稿。**綁定該怎麼定，是 R-DD5 的事。**

### 7.4 一件我原本會漏的

§3.3 那個 `CAN-C` → `CAN-B` 的形態，**第一眼像是解答**
（「同一 LID 在兩條匯流排上各一列」）。
如果我停在那裡，就會寫出「r420 是 CAN-C 側、r421 是 CAN-B 側，
二者並存不矛盾，DR 不必發」。

**但那解釋不了 K／P 欄。** CUSW 與 Atlantis 是**架構**欄，
不是 Powernet 的匯流排欄 —— 同一個 LID 在 Atlantis 架構下
不會因為 Powernet 走 C 還是 B 而變成 `Not Applicable`。
**11 組只差 G 欄的配對裡，K／P 欄全部一致或全空**，
只有 r420／r421 例外。這件事我寫在 §3.3 的分群裡，沒有寫成判斷。

---

## 8. 量測條件揭露（R-G8）

### 8.0 本包所書比率之分子與分母（R-G8 逐字：「任何比率須同時載明其分子與分母之定義」）

| 比率／計數 | 分子 | 分母 |
|---|---|---|
| 重複之 LID 名 17 | A 欄 `Logical Identifier` 出現 ≥2 次之**相異名數** | unique LID 名 429（自非空列 446 去重）|
| 佔 34 列 | 上列 17 名所涵之**列數** | 非空 LID 列 446（母體 = r4–r449，A 欄非空）|
| 同欄異值 16 組 | 至少一欄二列**皆非空且值不同**之組數 | 重複組 17 |
| 純補全 1 組 | 無同欄異值、僅「一空一有」之組數 | 重複組 17 |
| G 欄衝突 14 組 | G 欄（Powernet `CAN`）為衝突欄之組數 | **同欄異值組 16**（非 17）|
| 只差 G 欄 11 組 | 衝突欄集合恰為 `{G}` 之組數 | 同欄異值組 16 |
| `CAN-C`→`CAN-B` 12 組 | G 欄衝突值為該配對之組數 | **G 欄衝突組 14**（非 16、非 17）|
| 非空欄數相等 12／遞增 4／遞減 1 | 組內二列非空欄數之序 | 重複組 17 |
| `Not Applicable` 4／6／11 列 | 各架構欄之 `Signal Name` 值為該字串之**列數** | 非空 LID 列 446 |
| MPH 命中 9 leaf | 全列串接後命中 `\bMPH\b` 之 leaf 數 | 037 leaf 28（`Analysis Report` 含 leaf id 之列，無排除）|
| DBC 0 命中 | 四法各自之命中數 | `R4_BHCAN` BO_155／SG_914；`R5_FDCAN8` BO_323／SG_2037 |

> **三個分母不同，且差異會改變讀法**：14/16 與 14/17 之別在於
> `Heated_Steering_Levels` 一組無衝突（不進衝突統計）；
> 12/14 與 12/16 之別在於另有 2 組之 G 欄衝突值非 `CAN-C`→`CAN-B`。

### 8.1 檔與開啟方式

| 庫 | 檔 | 開啟 |
|---|---|---|
| LID（綁定）| `features/vehicle_setting/inputs/…v1_76.xlsx` | `openpyxl`, `read_only=True`, `data_only=True` |
| LID（比對用）| **`forms/…v1_78.xlsx`** | 同上 —— **僅讀，未寫**（§2.3）|
| DBC | `features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc`、`…R5_FDCAN8.dbc` | `read_text('utf-8', errors='replace')` |
| PROXI | `features/vehicle_setting/inputs/PROXI_HDCC27_R3_20250424.xlsx` | 唯讀（本輪未新查）|
| 037 | `features/driver_distraction/inputs/DD_SWE1_0807_EN.xlsx` | 唯讀 |

### 8.2 T13a 之查法與其界線

- **重複之判準為 A 欄 `Logical Identifier` 之字串完全相等**
  （`str(v)`，**未 strip**）。若某列之 LID 名帶前後空白，
  **會被判為與無空白者不同名，即漏計一組重複**。
  （A-DD3 之尾空白件為前例 —— 該件在 037 之 `Sub Categorization` 欄，
  非本欄；**本欄未查是否有此現象**。）
- **「同欄異值」之比對為 `str(va) != str(vb)`**，未做正規化 ——
  全形／半形、大小寫、前後空白之差**一律計為異值**。
  §3.3 之 14 組 G 欄衝突，其值皆為 `CAN-B`／`CAN-C`／`BH-CAN` 之乾淨字串，
  不受此影響；**其他欄未逐一目視**。
- **僅掃 `Proxi & Configuration` 一分頁**。`CAN Mapping` 分頁**未做同樣之
  重複 LID 掃描** —— 下放包 §四 問的是該分頁，但若 `CAN Mapping`
  亦有此形態，本輪看不到。
- **非空欄數之定義為「非 `None` 且非空字串」**。含單一空白字元之格
  （如 r43 之 I 欄 `' '`）**計為非空**。

### 8.3 T13b 之查法與其界線

- 五組正則見 §4。`mile` 未加 `\b`（故 `miles`／`mileage` 亦會命中）——
  **仍 0 命中**，即無論寬鬆與否皆無。
- **母體為列內各格串接後之全文**，含 037 之所有欄（Description、
  Verification Criteria、Source Requirement ID 等）。
- **未掃 CFTS022 原件** —— 本項只問 037（下放包 §七 T13b 之標的）。

### 8.4 T13c 之查法與其界線

- 四法：`SG_` 定義名（行首）、`BO_` 訊息名、`VAL_` 列舉行、全文裸字串。
  **前三者大小寫敏感，第四者不敏感。**
- **對照組二個**，見 §5。
- 訊息／訊號總數為本輪實測：`R4_BHCAN` 155／914，`R5_FDCAN8` 323/2037
  —— **與 R-DD6 v2 所載之 155／323 訊息數相符**。

### 8.5 本輪未量測者

- **profile §3 之實際落檔狀態**。下放包 §六 云分析層自辦，
  拘束四命「勿動」——**故未讀該檔**，無法回報其是否已解除。
- **`LID CAN Mapping r1738`／`r1397`**（下放包 §六 所引之 `$Speedometer$`／
  `$PresentGear$` 施加路徑）**本輪未覆核**。非本輪任務，且該二列出自
  上繳包 04 之 T10c。**若要我覆核請下令** —— 下放包 §九 之
  `ACV_FailType` 案例正指出「存在性檢查抓不到指錯列」，
  而**這二個列號本輪無人回頭核過 `Logical Identifier` 欄**。
- **`Proxi & Configuration` 以外分頁之重複 LID 分布**（見 §8.2）。
- **`Gear_Box_Type` 於 CUSW 側之定義來源**（上繳 05 §6.4 已列，本輪仍未查）。

---

## 9. 待分析層者

| # | 事項 | 現況 |
|---|---|---|
| 1 | **r420／r421 何者為準** | T13a 分布已交（§3.2–§3.5）；**未裁**。DR-DD5 建或不建待此 |
| 2 | **DR-DD6 文稿之 `v1_78`** | 擇「文稿改 v1_76」或「依 R-DD5 重綁 v1_78」；執行層不逕改（§2.3）|
| 3 | **profile §3 是否已落檔** | 分析層自辦；執行層未讀，開 pilot 前請確認（§6）|
| 4 | 是否覆核 `CAN Mapping r1738`／`r1397` 之 `Logical Identifier` 欄 | 未量測；§九之案例正指此類失效（§8.5）|
| 5 | **`docs/fw036/RULINGS.sha.tsv` 未收錄任何 `R-DD` 條** | 本輪實測：該台帳 `ruling_id` 欄**無一列以 `R-DD` 起首**。本 feature 本輪新增 3 條現行條文、轉留存 1 條。**共用路徑，執行層不逕改**（A-DD4）—— 請定由誰補登 |

**組 3（`-009`~`-012`）不受上列任一項阻斷**，其中 `-009`／`-011`
須帶 `[ASSUMPTION A-DD6]`。**pilot 可開。**
