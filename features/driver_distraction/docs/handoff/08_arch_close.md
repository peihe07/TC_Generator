# 下放包 08 —— 上繳 04／05 併審、R-DD6 v2、R-DD9／R-DD10、profile §3 解除、DR-DD6、T13

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`07_q789_rulings.md`；對應上繳：`04_arch_binding.md`、`05_signal_close.md`
- **pilot 條件成就**：組 3（leaf 009–012）於本包之 profile §3 解除後即可開

---

## 一、分析層之誤（本輪四項，逐項認）

| # | 誤 | 出處 | 更正 |
|---|---|---|---|
| 1 | 「r421 **末二欄**逐字為 `Gear_Box_Type`」—— 實為 c10（CUSW）與 c15（ATLANTIS）；末二欄是 `Revision Comments`／`Sort Tool` | 包 07 §四 | 依上繳 05 §3.4 |
| 2 | 以「與 `Country_Code` **同族**」為證據 —— 上繳 05 §3.4 實測：`r43` 之 CAN 欄逐字書 `PROXI`、名用全稱 `<Group>.<Param>`；`r421` **二者皆無**。**該推論在 LID 上不成立**，結論係由 PROXI 檔（上繳 05 §3.1）獨立證成 | 包 07 §四 | 二路徑不得混同；本包不再援引「同族」 |
| 3 | 「**T12 查得** → 寫 `PROXI Gear_Box_Type = <值>`」寫成無條件 —— 實則繫於「r421 為準」之未裁前提，且 `<值>` 另有值域不共格問題 | 包 07 §四 | 見 §四、§五 |
| 4 | 包 06 §1.2 之計數（223 列／`N` 58）**排除了 `WORLD` 一列而未書明**；且欄號採 1-based 而未標起點 | 包 06 §1.2 | 見 R-DD10；計數改書「223（不含 `WORLD`）」 |

誤 2 與誤 3 同源：**把「形態相似」當成「證據」**。與下放包 05 §1.2 之誤二
（未量測即斷言施加路徑）為同一家族——**看起來像，就當它是**。

---

## 二、R-DD6 v2（全文；R-TM13：v1 不刪除，留存於索引）

```
R-DD6 v2（訊號名之架構軸）

實測（上繳包 04 T10c）：綁定之二 DBC（PDT27_E2A_R4_BHCAN 155 訊息、
PDT27_E2A_R5_FDCAN8 323 訊息）為 ATLANTIS 側；LID 之 Powernet 欄名
（GW_C1.VEH_SPEED／GW_C1.Gr／VehCfg7.*）於二 DBC 皆不存在。

(a) 匯流排訊號之名一律取 **Atlantis High 欄**。理由非「該架構較佳」，
    而是**台架庫已綁定於此**：綁定件含 FD CAN（R5_FDCAN8），而 LID 中
    FD 側之名（PT_SYSTEM_FD_1.*、BRAKE_FD_2.*）**僅見於 Atlantis High 欄**，
    Atlantis 欄無 FD 條目。Powernet 名於本台架上寫得出來也送不出去。
(b) `Atlantis` 與 `Atlantis High` 二欄同字時無差別；**不同字時取
    Atlantis High**。實例：$Speedometer$ 二欄同字（STATUS_CCAN3.*）；
    $PresentGear$ 二欄不同字，Atlantis 欄之三名於二 DBC 皆不在，
    Atlantis High 欄之 PT_SYSTEM_FD_1.GearEngagedForDisplay_PT 在。
(c) 本條之效力繫於 R-DD5 之四庫綁定。若日後改綁他架構之庫，
    本條隨之失效並須重裁，不得沿用。
(d) LID 為多架構對照表。引其列時須同時標明所取之架構欄，
    格式 `LID {分頁名} r{n} [{架構}欄]`；只標列號者視同未標。
(e) **本條之適用範圍限於匯流排訊號。** PROXI 參數不經匯流排施加，
    (a) 之理由（可施加性）在其上不咬合；PROXI 參數以 **PROXI 檔為權威**，
    LID 僅為指標。LID 各架構欄對同一 PROXI 參數所載不一致者，
    登 DR，不逕選。
    （立此項之由來：上繳包 05 §5.4 —— v1 之失效條件只寫了「改綁」，
      未涵蓋「標的根本不走匯流排」；該案結論恰好不受影響，
      但理由不成立即應更正。）
（Pei 下放，分析層即裁，下放包 08 §二）
```

**索引表**：R-DD6 現行版改 **v2**；**v1 轉留存**，附失效值清單
（v1 之 (a) 只書「ATLANTIS 欄」、無 (b)(e)）。

---

## 三、R-DD9／R-DD10（新立）

```
R-DD9（訊號值之書寫形式：列舉量與連續量）

IN §8.7.5(a) 之 `= <raw> (<label>)`，其 <label> 定為 DBC VAL_ 之逐字列舉。
實測（上繳包 04）：綁定件中部分訊號無 VAL_ 列舉（連續量），
部分僅列舉 SNA。故分流：

(a) **有 VAL_ 列舉者**：`= <raw> (<VAL_ 逐字>)`。
    例：`$PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$ = 12 (Park)`
(b) **無 VAL_ 之連續量**：<label> 位改置**物理值與單位**，
    並以 DBC 之 factor／offset 換算，換算式須可覆算。
    例：`$STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)`
    物理值以 DBC 單位書寫（本件為 km/h）；spec 之 MPH 值另依
    R-DD7(d) 併記，不取代 DBC 單位。
(c) **僅列舉 SNA 者**（如 VehicleSpeedVSOSig 之 8191 "SNA"）：
    正常值依 (b)，失效值依 (a) 書 `= 8191 (SNA)`。
(d) 任一寫法之 raw 皆須為 DBC 可表示之整數格；
    不可表示者依 R-DD7(c) 取跨越側第一格，並具名之。
（Pei 下放，分析層即裁，下放包 08 §三）
```

```
R-DD10（外部表格之引用格式）

(a) **Excel 欄一律書欄名**（`H`／`S`／`BF`），不書 `c{n}` ——
    後者有 0-based／1-based 二種起點，本案已實際發生二層各用一種
    而看似不符之情形（上繳包 04 §4A.2(a)）。
(b) LID 之列一律書 `LID {分頁名} r{n} [{架構}欄]`（R-DD6(d)）。
(c) **凡書計數，須同時書其母體判準與排除項。**
    本案先例：`Market Config - R1` 之國別列計數 223 係排除 `WORLD`
    （非目的地國，Country_Code = 0）後之值；未書明即被讀為差 1 之錯
    （上繳包 04 §5.4）。
(d) 列號一律 Excel 之 1-based。
（Pei 下放，分析層即裁，下放包 08 §三）
```

---

## 四、r420／r421 —— 不裁，先量測（T13a）

二列對**同一 Logical Identifier**、**同一架構欄**給出互斥值
（`Not Applicable` vs `Gear_Box_Type`）。上繳 05 §5.3 指出以 PROXI 側證據
反推 r421 為準係**循環論證**——成立，分析層採。

**故不以「r421 較完整」裁之**——該推理與誤 2 同型（形態當證據）。

**登 DR 之前先窮盡量測**：該分頁是否**系統性**存在「稀疏列＋完整列」之配對？
若為該表之結構慣例（例如上列為 LID 宣告、下列為映射明細），則無矛盾可言，
DR 亦不必發。**此為 T13a。**

T13a 之後：
- **呈現為結構慣例** → 分析層依實測裁，不發 DR
- **未呈現慣例／配對無一致形態** → 認定為上游矛盾，分析層擬 **DR-DD5** 文稿

---

## 五、`[Manual]`／`[Automatic]` 之列舉對應 —— DR-DD6（本包建檔）

上繳 05 §3.5(甲) 之判定，分析層全採。補一項分析層側之量測所見：

CFTS022 之規範欄於 `-126`~`-129` 使用 **二值制**（`[Automatic]`／`[Manual]`），
與 **LID r421 [Powernet 欄] `Format`** 之 `0 = Automatic & 1 = Manual` 同構；
而 PROXI `Format` r443 為 **六值制**。**規範文係對著二值制寫的**，
六值制中 `MTA`／`DDCT` 歸於何側，**無任一庫載明**。

> 執行層拒寫 `= 1` 正確。`MTX` 對上 `Manual` 順、raw 又恰同為 1 ——
> **順與對是兩件事**。PROXI `Annotation` 逐字 `(ex: manual, MTA, automatic, DDTC)`
> 把 manual 與 MTA **並列為不同項**，恰是反證；但 Annotation 為舉例，
> 非歸屬定義，**故亦不得反過來據以排除**。兩個方向都不足以定案。

### DR-DD6 文稿（執行層建檔，狀態 DRAFTED；Pei 發送）

> **DR-DD6 — Enumeration mapping for `$VC_Trans_Equipped$` = `[Manual]` / `[Automatic]`**
>
> CFTS022 SYSRA rows `SYS-RA-Driver_Distraction-126` ~ `-129` specify the
> condition as `$VC_Trans_Equipped$ = [Automatic]` or `= [Manual]` — a
> two-valued domain, consistent with the Powernet-side format recorded in
> `Logical Identifiers and CAN Mapping v1_78`, sheet `Proxi & Configuration`,
> row 421, Powernet band `Format` column: `Transmission equipped:
> 0 = Automatic & 1 = Manual`.
>
> On the Atlantis side the same LID row points to the PROXI parameter
> `Gear_Box_Type` (`PROXI_HDCC27_R3_20250424.xlsx`, sheet `Format`, row 443:
> parameter group `Powertrain_Configuration_4`, byte 101, bits 0–2), whose
> table is six-valued: `0 = Not valid / 1 = MTX / 2 = MTA (Robotized Gearbox)
> / 3 = DDCT / 4 = ATX / 5 = CVT`.
>
> Question: for the purpose of the Hong Kong market requirements above,
> which `Gear_Box_Type` values constitute `[Manual]` and which constitute
> `[Automatic]`? In particular, do `2 = MTA (Robotized Gearbox)` and
> `3 = DDCT` fall on the `[Manual]` or the `[Automatic]` side? The parameter
> annotation (`General gear box (ex: manual, MTA, automatic, DDTC)`) lists
> manual and MTA as separate items but does not define the grouping.
>
> Until clarified, the affected rows are on hold in SWQT test case generation.

**編號說明**：DR-DD5 保留給 §四 之 r420／r421 件（T13a 後視結果建或不建），
本件取 DR-DD6。**號隨事項配，不隨時序配**；不因 DD5 未建而順移。

---

## 六、profile §3 —— 解除三列、維持二列

分析層自辦（`edit_file` 局部改，A-DD4）。解除後之 §3：

| `$…$` | 施加路徑 | 寫法 | 狀態 |
|---|---|---|---|
| `$Speedometer$` | `LID CAN Mapping r1738 [Atlantis High 欄]` → `STATUS_CCAN3.VehicleSpeedVSOSig`（`R4_BHCAN`，msg 994，13 bit，factor 0.0625，offset 0，Km/h） | `Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = <raw> (<km/h>)`；門檻 raw 依 R-DD7；失效值 `= 8191 (SNA)` | **解除** |
| `$PresentGear$` | `LID CAN Mapping r1397 [Atlantis High 欄]` → `PT_SYSTEM_FD_1.GearEngagedForDisplay_PT`（`R5_FDCAN8`，msg 263，5 bit，factor 1） | `= <raw> (<VAL_ 逐字>)`；Park = `12 (Park)` | **解除** |
| `$Country_Code$` | `LID Proxi & Configuration r43 [Atlantis & Atlantis High 欄]` → `Car_Configuration_16.Country_Code`（PROXI） | `PROXI Country_Code = 91`（不加 `$`）；標 `[ASSUMPTION A-DD5]` | **解除** |
| `$VC_Trans_Equipped$` | 未定 | 欄位掛 `PENDING: DR-DD6 <變速箱型式之列舉對應>`；r420／r421 待 T13a | **維持 SUSPENDED** |
| `$PARK_BRK_EGD$` | DR-DD2 未結 | 保留來源名：`Drive PARK_BRK_EGD from <值> to <值>`；不得代以 `PARK_BRK_EDG` | 不變 |

**`$Speedometer$` 之 fail-safe 形態**：`VehicleSpeedVSOSigFailSts` 於二 DBC
**皆不在**（上繳 04 T10c）。故 AC2 之「訊號失效」以 **SNA（8191）** 或
**匯流排逾時**表現；**何者適用逐 leaf 依 037 AC2 原文定**，
不由 profile 統一指定（037 措辭各列不同，統一即造值）。

---

## 七、任務

| # | 任務 |
|---|---|
| T-抄 | R-DD6 v2、R-DD9、R-DD10 逐字入 `RULINGS.md`；**R-DD6 v1 轉留存不刪**；索引表更新（現行 10 條、留存 1）。**出處註自本包起由分析層寫在圍籬內**（見 §八-4），執行層照錄即可，不再另加圍籬外註 |
| T-登 | DR-DD6 建檔（§五 文稿逐字，DRAFTED）；A-DD5／A-DD6 維持；A-DD6 之 leaf 範圍依上繳 05 §2.3 之 9 列 |
| T13a | `LID Proxi & Configuration` 全分頁掃**重複 Logical Identifier**：列出所有重複之 LID 名、其列號、各列之非空欄數與各架構欄值。**判斷「稀疏＋完整」是否為系統性配對，只給量測與分布，不下結論** |
| T13b | 037 全 28 列以 `MPH`／`mph`／`mile`／`km/h`／`kph` 五組字樣重掃門檻表述，補上繳 05 §2.3 之已知邊界（該輪限 `MPH` 字樣） |
| T13c | `Gear_Box_Type` 於二 DBC 之存在性**實測**（上繳 05 §3.5(丙) 之陳述本輪未重跑，屬未量測之斷言，關掉它） |

**不在本輪**：改 profile（分析層自辦）、`$VC_Trans_Equipped$` 相關 leaf、
pilot 之外的 TC、寫回、git。

---

## 八、四項既決事項之回覆（上繳 05 §7）

1. **r420／r421** → 不裁，T13a 後定（§四）
2. **`[Manual]` 對應** → 不裁，DR-DD6（§五）
3. **是否另立 DR** → 立，二支分開（DR-DD5 待 T13a、DR-DD6 本包建檔）。
   理由同 DR-DD1／DR-DD3：**任一單獨回覆仍不解另一**
4. **`RULINGS.md` 出處註形制** → 往後**由分析層寫在圍籬內**，成為條文本體
   之一部分隨條文流動；**R-DD6 v1／R-DD7／R-DD8 已落之圍籬外三行不回修**
   （動之即須動條文本體，與逐字相衝）。執行層不跟進舊例為正確
5. **R-DD6(a) 理由之適用** → 採，落為 R-DD6 v2 (e)（§二）

## 九、一項記入案例（上繳 04 §4.1）

`LID CAN Mapping r43` 之 `ACV_FailType` 其 Atlantis High 名**在二 DBC 皆查得**
——即當初若對 profile §3 之 `LID r43` 做「該訊號在不在 DBC」之檢查，
**會亮綠燈**。

**存在性檢查抓不到「指錯列」。** 能抓到的只有回頭核對該列之
`Logical Identifier` 是否為所欲之名。此為 R-DD10(a)(b) 之實證依據。

## 十、上繳包要求（`docs/upstream/06_pilot_ready.md`）

T-抄核對、T-登結果、T13a–c 原始輸出、未結 DR 清單、獨立自評、R-G8 揭露。
