# V20 — pilot #1 覆核：**不通過**。Priority 集合不符、Pre-Condition 違反 §4.4

下放包 **V20**。對應上繳：`docs/upstream/V20_*.md`。
本包新增 **R-VF59–R-VF62**（4 條）、**A-VF14／A-VF15**（2 件）、
**W-VF54–W-VF57**（4 項工單）。

**本包所據之最新上繳**：`docs/upstream/V19_pilot_start.md`，
**實測於 2026-08-23（`read_text_file` 全文）**；
另實測 `generated/vf230_pilot1.json` 全文十條。

---

## 1. pilot #1 之覆核結論：**不通過**

依 canon §1.2 分類：**defect 2 ／ style-divergence 2 ／ note 3**。
**defect 二項皆為 blocking，須修正後重提。**

**done-region check**：VF230 兩本工作簿之 done region 皆為空集合
（V05 §4.4 實測），風格權威沿用 Part 1 已鎖者。
**惟本包之二項 defect 皆為 canon 條文之直接違反，不繫於 done region。**

**先具名一事**：執行層之自檢六項全數 ✅ 且自檢失敗 0，
**而本層讀十條全文後仍得二項 blocking defect** ——
**自檢之六項係對照 V19 §5.3 之升級條件，而該清單為本層所擬。
清單未列者，自檢無從發現。責任在本層之清單，不在執行層之自檢。**

---

## 2. Defect 1（blocking）—— 10 條中 4 條不屬 R-VF57 所定之 P0

**量測條件**：以 R-VF57 之 P0 集合（P0(a) 九簇 ＋ P0(c) 七簇 = 16 簇）
逐條比對 `generated/vf230_pilot1.json` 之 `layer3` 欄。

| seq | layer3 | 屬 R-VF57 之 P0？ |
|---:|---|---|
| 238 | Power Liftgate/Tailgate Alert | ✅ P0(a) |
| 239 | Blind Spot Alert | ✅ P0(c) |
| 240 | Lane Sense Warning | ✅ P0(c) |
| 241 | Suspension Service Mode | ✅ P0(a) |
| 242 | Blind Spot with Trailer Detection | ✅ P0(c) |
| 243 | Park Sense | ✅ P0(c) |
| **244** | **Illuminated Approach** | **❌ 不在 16 簇內** |
| **245** | **4 AUX Switches** | **❌** |
| **246** | **Daytime Running Lights** | **❌** |
| **247** | **Passive Entry** | **❌** |

R-VF57 定 P0 = 88，其組成為 P0(a) 49 ＋ P0(c) 39。
**該四簇不在任一類中，卻被列為 P0 並進入池首。**

**二者必有其一為真，須查明而非擇一**：
  (i) 生成器之 Priority 賦值與 R-VF57 之集合不一致 → 選池序失真，
      本批十條非真正之池首
  (ii) R-VF57 之 88 實含該四簇，而 §3 之簇列舉不完整 →
      **則 R-VF57 之條文本身漏列，須補**

**且 `reasoning` 十條全數具名「P0(c) safety (R-VF57)」** ——
包含二條 P0(a)（238／241）與四條非 P0 者。
**依 R-VF13 第 5 項，`reasoning` 須具名其依據；具名錯誤之依據較不具名更有害** ——
其使審查者以為該判定已有依據。

---

## 3. Defect 2（blocking）—— Pre-Condition 違反 canon §4.4，10/10

十條之 `pre_conditions` 逐字相同：

```
1. The vehicle is powered and the HU has completed start-up
2. The Vehicle Settings menu is reachable from the home screen
```

**第 1 項為系統預設。** canon §4.4 之 Forbidden 首例逐字為
`system defaults (HU is powered on.)`。**十條全數違反。**

**第 2 項為「feature under test as premise」之形態。**
本批十條之驗證目標即「某設定項是否出現於 Vehicle Settings menu」，
而以「該 menu 可達」為前提，與 §4.4 所禁之 `Dealer Mode is accessible.` 同型。
**其可達性應由 procedure 之步驟建立，非置於 Pre-Condition。**

**修法**：Pre-Condition 應僅留真正之環境／初始狀態（本批可能為空）；
menu 之開啟改為 procedure 步驟。**修改後 procedure ↔ ER 之 1:1 對齊須重驗。**

---

## 4. Style-divergence 2 項（非 blocking，惟須裁）

### 4.1 `specification_reference` 之形式 —— 由 R-VF59 定案

執行層具名其為推得而非條文所定（上繳 V19 §3.2）。**處置正確。**

### 4.2 procedure 步驟 1 缺動詞

十條之步驟 1 為 `PROXI $X$ = "Absent"`，**無動詞**。
canon §5.1 令每一步驟須可執行；`PROXI $Param$ = "值"` 為 **R-1 v2 之
資料記法**，非步驟之句式。

**惟本層不逕裁** —— R-1 令「格式裁定須窮盡 Pei 既有已交付範例」。
須先查 Part 1 已交付之 TC 中 PROXI 設定步驟之實際句式，見 W-VF55。
**在查證前，本項為 style-divergence 而非 defect。**

---

## 5. Note 3 項

1. **十條同屬單一形態**（PROXI 配置決定選單項有無），執行層已具名
   （上繳 V19 §6 第 3 項）。**其使 pilot 之效力僅及於該形態** —— 見 R-VF61。
2. **十條皆為「不顯示」之負向分割，無一正向**。canon §7 令列舉型須配對
   負向；此處反之 —— 正向者（配置存在 → 顯示）為另一 leaf，
   不在本批。**非 defect，惟須確認其確為獨立 leaf 而非遺漏。**
3. **`tc_title` 240 稱 `absent` 而所測值為 `Not Present`**
   （其為兩個抑制值之一）。§4.3 令手足區辨之 token 須可見於 title。
   **輕微，併入 W-VF54 修正。**

---

## 6. R-VF59 —— `specification_reference` 之形式

```
R-VF59（VF230 之 specification_reference 形式，分析層裁定 2026-08-23）

**形式為 `VF230_V1-{n}`**，即 037 之 `Source Requirement ID`
（`SYS-RA-VF230_V1-{n}`）**去 `SYS-RA-` 前綴**。

**依據為 Part 1 之已交付慣例**（R-1：格式裁定須窮盡既有已交付範例，
不得自創）：Part 1 用 `CFTS044-{7 位 reqid}`，其構成規則同為
「來源 id 去 `SYS-RA-` 前綴」。VF230 之 037 無 7 位 Polarion reqid，
其來源 id 即 `SYS-RA-VF230_V1-{n}`，故套同一規則得 `VF230_V1-{n}`。

**執行層本批所採者與本裁定相同，十條無須改此欄。**

**附帶登記 A-VF14**：`feature.yaml` 之 `spec_reference_template` 為
`<Spec Filename>_{outline}`（spec_mode D），**與 Part 1 及 VF230 之實作皆不符**。
其為兩線共同之既存不一致。**本裁定不改該設定值** ——
須先依 R-VF33 查明誰在讀它、怎麼讀（W-VF57），再定其處置。
```

---

## 7. R-VF60 —— 值域來源鏈補第 0 位：條文自帶值

```
R-VF60（值域來源鏈之第 0 位，分析層裁定 2026-08-23）

R-VF13 定值域來源鏈為 LID → DBC → PROXI → VC/VM 四位。
本批十條之 `reasoning` 皆記「值域來源：**條文自帶值**（R-VF13 鏈序之前）」
—— **該來源不在 R-VF13 之四位內**，執行層以「鏈序之前」表述之，
其判斷正確而條文無據。

**補立第 0 位**：

  0-CLAUSE  **需求條文自身逐字載明之值**
            （如 `[Absent]`／`[Not Present]`／`≠ [Type1]`）

**其優先於 LID／DBC／PROXI／VC-VM 四位**，理由：條文為需求之本體，
其他四者為實作或配置之快照。**來源說有而快照沒有，是快照不完整之可能
大於來源錯誤**（R-VS57 之同一理據）。

**限縮**：
1. 僅限**逐字載明**者。條文未載而由上下文推得者不屬本位（推論即造值，§8.4.1）。
2. 採用時 `reasoning` 須引該條文之逐字片段，不得僅稱「條文自帶」。
3. 本位之存在**不使 W1／W2 之判定放寬** —— 條文載其一值而未載其值域全集者，
   其值域仍為未解（如 seq 242 之 DR-34 案）。

**錨點**：
  必命中   seq 239 之 `[Absent]`（條文逐字）→ 應解出值域含 `Absent`
  必不命中 seq 242 之 `Blindspot_Trailer_Detection` 之**全集** ——
           條文只載 `[Absent]` 一值，其允許值全集仍為未解，
           **不得因第 0 位而判為已解**
```

---

## 8. R-VF61 —— pilot 取樣須分層，本批 verdict 之範圍受限

```
R-VF61（pilot 批之取樣方式，分析層裁定 2026-08-23）

canon §1.2 令 pilot review 採**分層取樣**。
**而 V19 §5.1 令「自池首取 10 條」，即依選池序連續取樣，非分層。**
**此為本層之令與 canon 相違，責任在本層。**

其後果已實測：十條同屬單一形態（PROXI 配置決定選單項有無），
訊號斷言型、狀態轉換型、值域切換型、正向顯示型**皆未受檢**；
R-VF57 之 P0／P1 界線亦僅其「有無」側受檢，音量／靈敏度側無一條。

**一、本批（pilot #1）之 verdict 範圍受限** ——
無論其後續判為通過與否，**其效力僅及於「PROXI 配置決定選單項有無」一型**。
**不得據以放行其他形態之批次生成。**

**二、pilot #2 須依 canon §1.2 分層取樣**，分層維度至少含：
  條文形態（訊號斷言／狀態轉換／值域切換／選單顯示）
  writability（W0／W1）
  Priority（P0／P1／P2）
  Test Set（九者之涵蓋）

**分層取樣得偏離選池序** —— 選池序（R-VS58）用於量產批次，
pilot 之目的為驗證書寫形式之適用性，二者目的不同。
**此為對 R-VS58 之明示例外，僅適用於 pilot 批。**
```

---

## 9. R-VF62 —— R-VF58 擴充；下放包首段須記載所據上繳

```
R-VF62（R-VF58 之擴充與下放包之現況記載，分析層裁定 2026-08-23）

**一、R-VF58 增列**：不僅「理由被更正時檢驗結論」，
**亦須「取得新事實時檢驗既有結論」**。

  採納上繳 V19 §5 之反向實例：W-VF44 之理由（252 leaf 之可測內容
  立於 PROXI 配置之取得）**仍成立**，而其結論（該 9 條之值域無來源）
  因逐條讀條文之新事實而**不成立**（A-VF13）。
  **理由未變而結論不成立**，為 R-VF58 未涵蓋之方向。

**二、下放包首段須逐字記載**：
  「本包所據之最新上繳為 `<檔名>`，實測於 `<日期>`」。

  **成因**：V19 §6 列四項並行工單為待辦，而該四項已於上繳 V18 完成。
  R-VF30 第 1 項（成文前須讀最新上繳）與 R-VF42 第 4 項（續發前須確認
  前包已有上繳）**皆已立而仍再現** —— 二者為程序義務，無可見之產物，
  故其未履行不留痕。
  **記載使其留痕**：首段之缺漏或日期之過時，於覆核時即可見。

  本包（V20）已依本條記載，見首段。
```

---

## 10. 工單

### W-VF54 — pilot #1 十條之修正（**最優先**）

1. **Pre-Condition 重寫**（Defect 2）：移除系統預設；menu 之開啟改為
   procedure 步驟；**procedure ↔ ER 之 1:1 對齊須重驗**。
2. **`reasoning` 之 Priority 依據重寫**（Defect 1）：逐條具名其實際所屬之
   P0 類別（P0(a)／P0(c)／或依 W-VF55 之對帳結果）。**不得沿用同一句式。**
3. **`tc_title` 240** 之區辨 token 改為所測之 `Not Present`（Note 3）。
4. **值域來源之表述**依 R-VF60 改為 `0-CLAUSE`，並引條文逐字片段。
5. `specification_reference` **不改**（R-VF59 已確認其正確）。
6. **不生成新 TC，不擴批。**

### W-VF55 — Priority 集合之對帳（Defect 1 之查明）

1. 列出生成器實際賦予 P0 之**全部簇**，與 R-VF57 之 16 簇逐一比對。
2. 判為 (i) 生成器與條文不一致，或 (ii) R-VF57 之簇列舉不完整。
   **二者之處置不同**：(i) 修生成器並重排選池；(ii) 補 R-VF57 之條文。
3. 若為 (ii)，**本批十條可能確為池首**；若為 (i)，**本批非池首，須重取**。
4. **並查 Part 1 已交付之 TC 中 PROXI 設定步驟之實際句式**（§4.2），
   附逐字實例；無實例者具名「Part 1 無 PROXI 步驟之先例」。
5. 依 R-VF21／R-VF28 附三錨點。

### W-VF56 — A-VF13 之全量重跑（上繳 V19 §6 第 1 項自判為最須先辦）

`PROXI_REF` 抽取式補三變體（含括號與 `status`、參數以方括號包夾、
**無 `PROXI` 一詞**之 `configuration value`）。重跑 627 leaf 之分級。

**重點**：漏認之 PROXI 參數若不在表內，該 leaf 應為 W1 而現判 W0 ——
**W1 之 28 條可能低估**。回報重跑前後之逐級差異。
**依 R-VF62 一，此為「新事實」，須連帶檢驗既有結論**：
選池 621、批數 63 是否隨之改變。

### W-VF57 — `feature.yaml:spec_reference_template` 之消費者查證（A-VF14）

依 R-VF33：誰在讀它、怎麼讀。**只查不改。**
若無任何消費者，具名為死設定；若有，回報其與實作不符之後果。

---

## 11. 待 Pei 裁定

**pilot #1 之 verdict。** 本層之分類為：**defect 2（blocking）／
style-divergence 2 ／ note 3**，建議 **不通過，修正後重提**。

**請裁**：(i) 同意不通過，或 (ii) 另有判斷。

**另請知悉**：R-VF61 已令 pilot #2 須分層取樣，
**pilot #1 之通過與否，其效力僅及於「PROXI 配置決定選單項有無」一型。**

---

## 12. 本包產生之新條文清單（自檢）

| 編號 | 型別 | 區塊 |
|---|---|---|
| R-VF59（`specification_reference` = 來源 id 去 `SYS-RA-` 前綴） | 分析層裁定 | ✅ §6 |
| R-VF60（值域來源鏈補第 0 位「條文自帶值」；三項限縮；二錨點） | 分析層裁定 | ✅ §7 |
| R-VF61（pilot 須分層取樣；本批 verdict 範圍受限；對 R-VS58 之明示例外） | 分析層裁定 | ✅ §8 |
| R-VF62（R-VF58 擴充；下放包首段須記載所據上繳） | 分析層裁定 | ✅ §9 |
| A-VF14（`feature.yaml:spec_reference_template` 與兩線實作皆不符） | anomaly | ✅ §6 |
| A-VF15（Priority 集合與 R-VF57 不符，4/10） | anomaly | ✅ §2 |

**工單**：W-VF54（十條修正，**最優先**）／W-VF55（Priority 對帳 ＋ PROXI 步驟句式查證）／
W-VF56（A-VF13 全量重跑）／W-VF57（`spec_reference_template` 消費者）。

**分析層本輪之錯**：V19 §5.1 令「自池首取 10」與 canon §1.2 之分層取樣相違（§8）；
V19 §5.3 之升級條件清單未列 Pre-Condition 與 Priority 一致性，
致執行層自檢無從發現二項 blocking defect（§1）；
V19 §6 之並行工單清單過時（§9 二）。

**未解除之風險，須於每次上繳具名**：10 條跨線條文未受保護。

**執行層上繳時須附「本包是否仍有該驗而未驗者」之獨立判斷。**
