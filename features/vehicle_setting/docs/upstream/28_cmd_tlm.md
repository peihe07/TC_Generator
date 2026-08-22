# 上繳 28 —— `*_Cmd_Tlm` 之 LID 回查、pilot #2 defect 修正、適用性前言全掃

執行層寫入。依據：`docs/handoff/50_review_round29.md` §4（30 輪作業）
＋ `docs/handoff/51_pilot2_review.md` §4（31 輪指令）。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 沿用既有骨架，逐節填入 | ✅ |
| D-2 | 逐字轉錄 R-VS50 | ✅（**已於 30 輪完成**，`RULINGS.md:1063`） |
| D-3 | DR-21 之影響範圍以 W-86 之結果重估並改寫 | ✅ |
| D-4 | 依 R-VS35 列兩數 | ✅ |
| **W-86** | `*_Cmd_Tlm` 四者之 LID 回查 | ✅ **不採用**（架構欄組不符） |
| **W-89** | pilot #2 之 defect 修正（4 項／5 條） | ✅ |
| **W-87** | 適用性前言之全量掃描 | ✅ 108/2/127 → **103/2/132** |
| W-88 / batch13 | 51 包 §4 明令順延 | ⏸ 順延 |

---

## 1. 預期 vs 實測（相符者亦列出）

| # | 預期（下放包） | 實測 | 判 |
|---|---|---|---|
| 1 | W-86：四 token 於 LID 有命中 | `CAN Mapping` **5 列**、`Proxi & Configuration` **0 列**；全部經 **R-VS36 裸名形態**命中 | 相符 |
| 2 | W-86(3)：Format 為實值域／轉指／空 | **實值域**（四級編碼，非 `See Proxi Table`、非空） | 相符 |
| 3 | 50/51 包：判實值域 → **正向，61 leaf 可解** | **不成立** —— 值域落在 LID **`Atlantis` 欄組**，非 R-VS20 第二階指定之 `Atlantis High` 欄組 | **不符 → §2.1** |
| 4 | W-86(5)：實值域 → 併入 `spec_variables.tsv` 並重跑 | **未併入、未重跑**，分級維持 **108/2/127** | **不符 → §2.1** |
| 5 | W-87(1)：同型總數（升級門檻 > 20） | 條文層 **9 條**、leaf 層 **6 個**（唯一來源 5／併引 1） | 相符，升級未命中 |
| 6 | W-87(3)：W0 之虛高幅度 | **5 條**（108 → 103），非 A-VS96 所載之 4 條 | 相符（幅度較預期多 1） |
| 7 | W-89：五條 defect 修正後 §9 無新違規 | 三批機械自檢**各 0 項** | 相符 |
| 8 | D-3：DR-21 逐 token leaf 數 | **137 leaf／215 次／27 token**（現載為 82 leaf／104 次） | **不符 → §2.3** |
| 9 | 51 包 §0：30 輪 D-2～D-5 全部未執行 | **D-2 已於 30 輪完成**（R-VS50 在 `RULINGS.md:1063`）；W-86(1)(2)(3) 亦已於 30 輪執行並口頭回報，**惟未落檔** | **不符 → §2.4** |

---

## 2. 不符項目（不自行調和）

### 2.1 W-86 —— 實值域存在，但屬他架構欄組，**依 R-VS20 不得取用**

LID `CAN Mapping` 命中五列（逐字）：

| 列 | LID | 欄組 | Signal Name | Format（逐字） |
|---|---|---|---|---|
| 764 | `FL_HS_RQ2` | **Atlantis**（欄 16–20） | `TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm` | `0 = Heated_seat_off / 1 = Heated_seat_low / 2 = Heated_seat_medium / 3 = Heated_seat_high` |
| 769 | `FL_VS_RQ_TGW` | **Atlantis** | `TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm` | `Atlantis / 2 bit signal / 0 = Vented_Seat_Off / 1 = Vented_Seat_Low / 2 = Vented_Seat_Medium / 3 = V…` |
| 769 | 同列 | **Atlantis High**（欄 26–30） | `TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm`／`BH-CAN` | `0 = Not_Pressed / 1 = Pressed` |
| 770 | `FL_VS_RQ_TGW2` | **Atlantis** | `TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm` | `0 = Heated_seat_off … 3 = Heated_seat_high` |
| 784 | `FR_HS_RQ2` | **Atlantis** | `TELEMATIC_VEHICLE_SETUP.FR_HS_Cmd_Tlm` | `0 = Heated_seat_off … 3 = Heated_seat_high` |
| 790 | `FR_VS_RQ_TGW2` | **Atlantis** | `TELEMATIC_VEHICLE_SETUP2.FR_VS_Cmd_Tlm` | `0 = Heated_seat_off … 3 = Heated_seat_high` |

三項互相印證，指向同一結論：

1. 四者之 Format **皆在 `Atlantis` 欄組**，`Atlantis High` 欄組於該四 token 無值。
2. 引用 `*_Cmd_Tlm` 之條文 **65 條，`EE Architecture` 100% 為 `Atlantis Mid`**（實測，無其他值）。
3. R-VS20 逐字：第二階為「LID 表之對應欄組（`CAN Mapping` → **Atlantis High**）」，
   且「**他架構條文（CUSW／PowerNet／Atlantis Mid）之值域一律不取用**」。

**故 W-86(4)(5) 不執行。** 併入即等同以 Atlantis Mid 之值域描述 Atlantis High；
且列 769 之 `Atlantis High` 欄組所給者為**另一訊號** `FL_VS_Tlm`（`Not_Pressed`／`Pressed`）
—— **即 DR-15 之標的本身**，逕行併入將同時解掉一個未結 DR（**觸犯 R-VS44**）。

→ **A-VS98**（結構性，待裁）：R-VS19″ 使 `Atlantis Mid` **在母體內**，
R-VS20 使其值域**不可取用**；兩條之交集使 **60 個相異 leaf 恆在範圍卻恆不可寫**。
**此為條文層之矛盾，非執行層可解。**

### 2.2 LID 內部矛盾（附帶發現）

`FL_VS_Cmd_Tlm` 同一訊號：列 769 為 `Vented_Seat_*`、列 770 為 `Heated_seat_*`；
`FR_VS_Cmd_Tlm`（列 790，Vented）亦寫 `Heated_seat_*`。**不擇一** → **A-VS97**。
與 A-VS49 同型。

### 2.3 DR-21 之影響範圍與現載不符

現載「82 個 leaf、104 次命中」；實測 **137 leaf／215 次／27 相異 token**。
且「`*_Cmd_Tlm` 61 leaf 為單一最大解鎖」亦不成立 —— 實為 **60 相異 leaf**，
而**最大群為 `HeatedSeatFL`／`FR`／`VentedSeatFL`／`FR` 四者之 84 相異 leaf**
（現載將此四者各記為 6 次）。已改寫 DR-21 → **A-VS100**（R-VS50 第二次命中）。

### 2.4 51 包 §0 之狀態誤述

51 包 §0 記「D-2～D-5 與 W-86／W-87／W-88 全部 ⬜ 未執行」。
實況：**D-2 已於 30 輪完成**（R-VS50 逐字在 `RULINGS.md:1063`），
**W-86(1)(2)(3) 亦已於 30 輪執行並回報**，惟其結果**未寫入 `docs/upstream/28`**，
故自交付物觀之為未執行。**本層不辯**，僅記明差異：
**「已執行未落檔」與「未執行」在 R-VS18 之機制下不可區分** —— 此為機制之盲區。

---

## 3. 結果三分法（canon §8.4）

**(a) 確證**

- `*_Cmd_Tlm` 四者於 LID `CAN Mapping` 有 5 列命中，Format 為實值域（逐字如 §2.1）
- 四者全部僅經 **R-VS36 裸名形態**命中 —— R-VS36 第三次奏效
- 引用該四者之條文 **65 條全為 `Atlantis Mid`**（無例外）
- 適用性前言：條文層 **9 條**、唯一來源型 leaf **5 個**、併引型 **1 個**
- 分級 **108/2/127 → 103/2/132**
- W-89 五條修正後三批機械自檢 **各 0 項**；DBC `VAL_` 逐字核對
  （`FL_HS_Tlm`／`FL_VS_Tlm`／`FR_HS_Tlm`／`FR_VS_Tlm` 皆 `0 "Not_Pressed" 1 "Pressed"`）通過
- DR-21：137 leaf／215 次／27 token

**(b) 未定**

- `*_Cmd_Tlm` 之值域可否取用 —— **待裁（A-VS98）**
- `FL_VS_Cmd_Tlm` 兩個相衝之值域何者生效 —— **待裁（A-VS97）**
- A-VS62（`is registered without a bus error` 之 house style）—— 51 包 §2.5 待 Pei

**(c) 排除**

- 「W-86 判實值域即為正向、61 leaf 可解」—— **排除**，架構欄組不符
- 「四者之 Format 為 `See Proxi Table` 轉指」—— **排除**，其為實值域
- 「適用性前言之同型 > 20」—— **排除**，實測條文 9／leaf 6
- 「`Proxi & Configuration` 分頁另有該四 token」—— **排除**，0 列

---

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

**W-86** — `openpyxl` 讀 `Logical Identifiers and CAN Mapping v1_76.xlsx`
之 `CAN Mapping` 與 `Proxi & Configuration` 兩分頁，逐列全掃（無取樣）。
比對採 **R-VS36 三形態**：`$X$`／裸名／描述式。
欄組歸屬由列 2 之合併標題向左回溯決定（Powernet 欄 6／CUSW 欄 11／
**Atlantis 欄 16**／Compact 欄 21／**Atlantis High 欄 26**）。

**W-87** — 對 `blocks_with_sec()` 之全部條文，四式正則（大小寫不敏感、
容忍字間空白差異）：

```
Following\s+requirements?\s+are\s+valid\s+only\s+if
The\s+requirements?\s+in\s+this\s+section\s+are\s+applicable
applicable\s+(?:for|to)\b[^.]{0,80}?\bonly\b
This\s+section\s+applies
```

leaf 對映經 `data/leaf_to_reqid.tsv`（欄 `swe_id` / `reqid_list`，237 列）。
**唯一來源型**（`reqid_list ⊆ 前言集合`）與**併引型**分開計數 —— 後者不改判。

**D-3** — 自 `docs/reports/writability.tsv` 取 `blocker_class` 以 `B2` 起首之列，
以 ``` `(token)` 之值無匯流排對應 ``` 抽 token，
**同時列累加次數與相異 leaf 數**（R-VS50 之教訓：兩者不可互代）。

**盲區（具名）**：

- LID 之其餘欄組（Powernet／CUSW／Compact）未掃 —— 其與本 feature 無關，但未實證
- W-87 之四式為 51 包所指定，**第五式以上未測**（R-VS46 形態）；
  且前言之判定為**字面形態**，語意上無可測內容而措辭不同者（如 A-VS76 型）看不見
- LID v1_78 之同列是否已修正 §2.2 之矛盾 —— 未查（素材更新屬 Pei，A-VS80）

---

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| 編號 | 主題 | 配對 DR |
|---|---|---|
| **A-VS97** | LID 內 `FL_VS_Cmd_Tlm` 值域自相矛盾 | 併入 **DR-21**（B2 類）；**惟其為型 A 規格缺陷，須另向上游反映** |
| **A-VS98** | R-VS19″ × R-VS20 → 60 leaf 恆不可寫 | **無 DR** —— 其為**我方條文之交集問題**，非上游缺件，**待分析層裁定** |
| **A-VS99** | W-87 之修正幅度 5 條（A-VS96 漏第五條） | 無（內部修正） |
| **A-VS100** | DR-21 優先序數字兩度與實測不符 | **DR-21 已改寫** |

**關閉**：**A-VS96**（依 W-87，四條轉 W2／`B4-preamble`）。

**D-4（R-VS35 兩數）**

| 側 | 本輪開立 | 登記簿現有 |
|---|---:|---:|
| 執行層 | **4**（A-VS97～A-VS100） | **99**（A-VS01～A-VS100，`A-VS02` 永久缺號，不重編） |
| 分析層（51 包） | **0**（51 包 §6 自陳「無新條文」，亦未開 anomaly） | 差額 0 |

**DR 現況**：新開 0、改寫 1（DR-21）、撤回 0。
待送：DR-17／DR-20／DR-23／DR-8′／DR-24′／DR-18／DR-11；**DR-21 現已定案可送**。

---

## 6. 獨立判斷：本包是否仍有該驗而未驗者

**有，三項。**

1. **A-VS98 未解之前，W-88／batch13 之池無法確定。**
   51 包已令 batch13 順延「俟 W-86 之結果定其池」；W-86 之結果是**待裁**，
   故順延之條件未解除。現行 `generatable = yes` 為 **81**（W-87 修正後由 86 降），
   但其中已交付 76 條，**實際餘量須於下輪實測**，本輪未測。

2. **W-89 之修正未經 pilot 複核。**
   五條之修法皆逐字採 51 包 §2 所給之措辭，機械自檢 0 項，
   **但「ER 改為可觀察終態」是否仍完整驗證原需求**，只有人讀能判。
   `-014`／`-031` 之時限要求已完全移出 ER 並標 `BLOCKED: DR-24′` ——
   **若 DR-24′ 覆為具體毫秒值，兩條須再改一次**。

3. **A-VS62 仍懸置**（自 25 輪，橫跨 8 條已交付 TC）。
   51 包 §2.5 已將其上呈 Pei 之二選一，本輪無新資訊可加。

**另記一項機制觀察**（非作業）：§2.4 之情形顯示 **R-VS18 之「上繳包為第一項」
只保證骨架先建，不保證結果落檔**。30 輪之 W-86 已執行、已口頭回報，
在交付物上仍為空。**建議之驗法**：每輪結束前以骨架之 ⬜／✅ 對照實際節內容，
空節而標 ✅ 者為不一致。**本層本輪已自行套用此法**（見本檔首表）。
