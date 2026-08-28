# 下放包 09 —— DR-DD5 建檔、v1_76 更正、四項結案、T14、pilot 規格（組 3）

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`08_arch_close.md`；對應上繳：`06_pilot_ready.md`
- **profile §3 已解除並回填**（分析層自辦，`edit_file` 二次局部改，diff 已驗）：
  `$Speedometer$`／`$PresentGear$`／`$Country_Code$` 三列生效，
  新增 §3.1（速度門檻 raw 表）與 §3.2（fail-safe 形態），
  `$VC_Trans_Equipped$` 維持 SUSPENDED

---

## 一、上繳包 06 審查判定 —— 收

**T-抄 PASS（三條 0 差異、v1 留存 0 差異、索引 10/1 相符）。**

### 1.1 T13a 之三層 —— 記入案例

執行層自陳「改了三次腳本才問對問題」。**交出來的是對的那個量，而這比
一次到位更值得記**：

- 第一版只數非空欄數（§3.1）→ 12/17 相等 → 結論「稀疏＋完整**不是**慣例」
- 逐欄比對（§3.2/§3.3）→ 慣例在 **G 欄**（`CAN-C`→`CAN-B`，11 組只差此欄）

**二者方向相反，而第一版交得出去。** 下放包 §四問的是「稀疏＋完整」——
**問題本身把量測軸問偏了**，執行層沒有照著偏的軸答完就收。
此為「照指示做完」與「答對問題」分岔之實例，與上繳包 03
「照 profile 查 → 查不到 → 回頭驗 profile」同族。

### 1.2 §7.4 —— 本輪最關鍵之一步

`CAN-C`→`CAN-B` 形態第一眼像解答（「同一 LID 在兩條匯流排上各一列」），
若停在該處即會寫出「二者並存不矛盾，DR 不必發」。

**執行層未停**：CUSW 與 Atlantis 是**架構**欄，同一 LID 不會因 Powernet
走 C 或 B 而變成 `Not Applicable`；11 組只差 G 欄者，其 K／P 欄全部一致或全空。
**且該事實寫在分群裡而未寫成判斷** —— 分寸正確。

**此為 §二 DR-DD5 裁定之直接依據。**

### 1.3 T13c 之對照組

「0 命中」為否定性判斷，最易之錯法是掃描寫錯而全 0。二個對照組
（`VehicleSpeedVSOSig` 二庫皆中、`GearEngagedForDisplay_PT` 僅 FD 中，
且與 msg 263 相符）把該可能排除。**否定性判斷附對照組，自本包起為常規**。

---

## 二、DR-DD5 —— 裁定：建檔

T13a 之分布已足以定性：

| 判準 | r420／r421 |
|---|---|
| 配對系統性 | 合（17 組全 2 列）|
| 主形態（G 欄 `CAN-C`→`CAN-B`）| **部分合** —— 其 G 欄合，但另有 F／K／P 三欄衝突，為 17 組中衝突欄最多者 |
| `Not Applicable` 出現 | **全分頁唯一** |
| CUSW 與 Atlantis 訊號名同時衝突 | **全分頁唯一** |

**裁定**：主形態解釋不了 K／P 欄之衝突（§1.2 之理由），
r420／r421 **不合該表之任何既有慣例**，認定為**上游矛盾**（R-13 家族）。
**DR-DD5 建檔**。

> **不以「r421 較完整」裁之**——該推理與下放包 08 §一 之誤 2 同型
> （形態當證據）；亦不以 PROXI 側證據反推（上繳 05 §5.3 之循環論證）。
> 裁定所據者為「**不合慣例**」之量測，非「哪一列看起來對」。

### DR-DD5 文稿（執行層建檔，DRAFTED；Pei 發送）

> **DR-DD5 — Conflicting rows for LID `VC_Trans_Equipped` in the Logical
> Identifier table**
>
> In `Logical Identifiers and CAN Mapping v1_76`, sheet
> `Proxi & Configuration`, the logical identifier `VC_Trans_Equipped`
> appears twice, in rows 420 and 421, with conflicting content:
>
> - Row 420 — Powernet `Signal Name` = `VC_Trans_Equipped`, Powernet `CAN`
>   = `CAN-C`; CUSW `Signal Name` = `Not Applicable`;
>   Atlantis & Atlantis High `Signal Name` = `Not Applicable`.
> - Row 421 — Powernet `Signal Name` = `VehCfg7.VC_Trans_Equipped`,
>   Powernet `CAN` = `CAN-B`, Powernet `Format` = `Transmission equipped:
>   0 = Automatic & 1 = Manual`; CUSW `Signal Name` = `Gear_Box_Type`;
>   Atlantis & Atlantis High `Signal Name` = `Gear_Box_Type`.
>
> The sheet contains 17 logical identifiers that appear on two rows each.
> In 14 of those pairs the difference is confined to the Powernet `CAN`
> column (11 of them differ in that column only), following a consistent
> `CAN-C` → `CAN-B` pattern. `VC_Trans_Equipped` is the only pair whose
> conflict extends to the CUSW and Atlantis signal-name columns, and the
> only pair where one row states `Not Applicable` while the other names a
> parameter.
>
> Question: for the Atlantis architecture, which row governs
> `VC_Trans_Equipped` — is the identifier not applicable (row 420), or is
> it realised through the PROXI parameter `Gear_Box_Type` (row 421)?
>
> Until clarified, requirements conditioned on `$VC_Trans_Equipped$` are on
> hold in SWQT test case generation.

**DR-DD5 與 DR-DD6 為獨立阻斷**：DD5 定「有無施加路徑」，DD6 定
「值如何對應」。任一單獨回覆仍不解另一（同 DR-DD1／DD3 之理）。
執行層於台帳明記此關係，並撤 DR-DD5 之「保留號」列改為正式條目。

> 台帳留保留列之處置正確 —— 摘要表跳號會被讀成漏筆。

---

## 三、DR-DD6 文稿之版本 —— 分析層之誤，採甲

**誤（分析層第 5 項）**：文稿書 `v1_78`，而 R-DD5 綁定者為 `v1_76`，
且全部量測係對 v1_76 所為。**引一個未綁之版本，等於 DR 之舉證基礎
與台架不一致。**

**處置**：文稿之 `Logical Identifiers and CAN Mapping **v1_78**`
改為 **`v1_76`**（一處，僅版本號；其餘逐字不動）。
執行層以 `edit_file` 局部改該處，改後回讀驗。

> 執行層查而不憑感覺（逐欄比八欄並附表）正確；
> **「這次剛好沒位移，不代表下次不會」為本項之真正理由** ——
> 採認為一般拘束：**凡引外部表格之列號，所引版本須即綁定版本**。

**`forms/` 之 `v1_78` 是否重綁 → 屬 Pei**：牽動 `vehicle_setting` 等
其他 feature 之既有交付基線，不在本線裁。本包不動 R-DD5。

---

## 四、四項結案（上繳 06 §9）

| # | 事項 | 處分 |
|---|---|---|
| 1 | r420／r421 | **裁定：建 DR-DD5**（§二）|
| 2 | DR-DD6 之 `v1_78` | **採甲：改 v1_76**（§三）|
| 3 | profile §3 是否已落檔 | **已落**。§3 三列解除、新增 §3.1／§3.2；`$VC_Trans_Equipped$` 維持 SUSPENDED。執行層 pilot 前自行回讀確認 |
| 4 | 覆核 `r1738`／`r1397` 之 `Logical Identifier` 欄 | **不必再量 —— 已有實測**。上繳包 04 §1 之 T10a 傾印首列即為：`r1738` c0 `Logical Identifier` = `Speedometer`；`r1397` c0 = `PresentGear`。**該覆核當輪已做**，本項關閉 |
| 5 | `RULINGS.sha.tsv` 無 `R-DD` 條 | **授權執行層以 `edit_file` 追加**（A-DD4 禁者為整檔覆寫，非局部追加）。見 T14a |

---

## 五、任務

| # | 任務 |
|---|---|
| T14a | 讀 `docs/fw036/RULINGS.sha.tsv` 既有 schema（欄序、雜湊演算法、範圍界定），**照其形制**以 `edit_file` 追加 R-DD1~R-DD10（現行 10 條）＋ R-DD6 v1（留存）之列。**不自創欄、不改他 feature 之列**；追加後回讀驗。schema 無法確定即停並回報，不猜 |
| T14b | **pilot 前置** —— `LID CAN Mapping` 分頁之重複 `Logical Identifier` 掃描（母體判準比照 T13a）。**特別確認 `Speedometer` 與 `PresentGear` 是否唯一**。若非唯一，逐列全欄傾印並**停止 pilot**，回報待裁 |
| T14c | DR-DD5 建檔（§二 文稿逐字）；DR-DD6 文稿版本號改正（§三）；二者關係註記 |
| **T15** | **pilot 生成 —— 組 3 `Lockout Enforcement`（leaf 009–012，4 leaf）**。規格見 §六。**T14b 清白後始得開始** |

---

## 六、pilot 規格（T15）

### 6.1 範圍

leaf `-009`／`-010`／`-011`／`-012`（Test Set = `Lockout Enforcement`）。
**只生成，不寫回工作簿、不 git。** 產物置 `features/driver_distraction/generated/`。

### 6.2 拘束（逐條可查）

1. **來源**：test_item 上半 verbatim 取 037 Requirement Description
   （R-S4；上半 token ≤ 50，超限摘句）；下半括號為測試目的，
   **同一 Requirement ID 衍生之列不得逐字相同**
2. **spec_reference**：profile §1 —— `CFTS022-4915108`（`-117`）／
   `CFTS022-4915109`（`-118`），一行一 ObjectID
3. **ER 錨**：profile §2 —— 觀察面 A（存取阻擋，**取樣 feature 具名**，
   受 p7 R1L 註記拘束、黃標項不得取樣）／觀察面 B（Standard Lockout Popup
   逐字 `"Feature not available while the vehicle is in motion."`）。
   `RESTRICTED`／`NOT_RESTRICTED`／`Locked`／`Unlocked` **不得出現於 ER**
4. **訊號寫法**：profile §3 ——
   `Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)`；
   §3.1 之 raw 表；用及者標 `[ASSUMPTION A-DD6]`（`-009`／`-011`）
5. **priority**：profile §4 —— `-009`／`-011` = **P0**，`-010`／`-012` = **P1**
6. **§8.4.2 界線**：安全帶／乘客偵測／`Are you the passenger?` 分支／
   UF1／UF2／ADAS 兩版分支 **一律不得引入**
7. **fail-safe 形態**（`-010`／`-012`）：依 profile §3.2，
   **逐 leaf 依 037 AC2 原文定** SNA 或逾時，不統一
8. IN 全域：§9 自檢 17 項、§10 輸出契約、§11 格式（尾句號、雙引號）

### 6.3 交付形式

每 leaf 一 TC 為預設；**若 §8.2.2 之獨立部分失效判準成立則得拆**，
拆者於 `reasoning` 具引 §-節與拆分軸。
`reasoning` 為繁中 2–5 句（IN §10.4）。

**不得**：改 profile、動凍結 leaf（`-017`~`-028`）、寫回、git。

---

## 七、上繳包要求（`docs/upstream/07_pilot.md`）

T14a–c 結果、T14b 原始輸出、T15 之 4 TC 全文、逐條自檢對照（§6.2 八項）、
未結 DR 清單、獨立自評、R-G8 揭露。
