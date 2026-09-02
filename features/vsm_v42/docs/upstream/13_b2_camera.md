# 上繳包 13(b) — vsm_v42：b2-2 生成（Camera Gridlines，10 leaf）

日期：2026-09-02　執行層：Claude Code　對應下放包：`docs/handoff/13_b2_camera.md`

> **取號說明**：下放包 13 指定上繳檔名 `docs/upstream/13_b2_camera.md`，
> 而 `13_ship_b1.md` 已於出貨時佔用上繳序號 13（該件無對應下放包）。
> 本檔依下放包所指之**檔名**落檔，標題以 `13(b)` 區別。**兩者非同一往返，據實記明。**

## 結果分類

| 分類 | 內容 |
|---|---|
| 改對了 | 10 leaf × 1 TC 生成；`generated/b2_camera_gridlines/` 21 檔；`lint_p_waivers_b2.tsv` 起檔 |
| 核實無誤 | **E38–E45／E56（10／10）／E86 型全過**；lint 判準預檢 J／K／Q／V／M／R 全 0；**§4.6 axis 規則** 0 違規 |
| 正確地不動 | b1 凍結件／b2-PS／`delivered/`／`sandbox/` 全未動；**`-063` 之需求文本不造**（BLOCKED 寫入而非略過） |

**總判：10／10 覆蓋，自檢全綠。一列 BLOCKED（`-063`），成因為上游 —— 見第 3 節。**

---

## 1. 母體與素材

| 項 | 實測 |
|---|---|
| `test_set = Camera Gridlines` | **11 列** = leaf **10** ＋ `No TC — Heading` **1**（`-028`） |
| 家族 | `Dynamic Gridlines` **4**（`-029`…`-032`）／`Surround Camera Gridlines` **6**（`-063`…`-068`） |
| 與下放包 §二-1 之 4／6 | **逐項相符** |
| 037 leaf 序位置 | Dynamic **#24–#27**；Surround **#52–#57** |

**spec_reference**（R-VL19 單錨，二節各歸各）：
`Dynamic Gridlines` → `…_V42_R6_1.11.1.1.31`（**4 條**）；
`Surround Camera Gridlines` → `…_V42_R6_1.11.1.1.38`（**6 條**）。**E86 型過。**

---

## 2. 訊號與 PROXI

| 名 | v3 結果 | 段 3 證據／段 1 錨 | 本批寫法 |
|---|---|---|---|
| `IPC_VEHICLE_SETUP3.SVC_Guidelines` | **解得** | `BO_1294`；`VAL_` `0 = Off`／`1 = On` | `$…$ = 0 (Off)` / `= 1 (On)` |
| `TELEMATIC_VEHICLE_SETUP3.SVC_Gridlines_Req` | **未解得（規格拼字疑誤）** | 主 DBC 查無；正確拼法 `SVC_Guidelines_Req`（`BO_1291`，`VAL_` 2 項）存在 | **保留規格原名，不加 `$`、不附 label**（R-VL16(a)／R-13） |
| `DynamicGrid.Req` | 未解得(止於段1) | — | `PENDING: DR-VL4`（R-P355(c)） |
| `TLM_Vehicle_Setup_Menu.Info` | 未解得(止於段1) | — | `PENDING: DR-VL4` |
| PROXI `Rear_View_Camera` | PROXI路徑 | **PROXI Format r401 欄 F 逐字**；`0 = Absent`／`1 = Present` | `PROXI Rear_View_Camera = 1 (Present)` |
| PROXI `Surround_View_Camera` | PROXI路徑 | **PROXI Format r761 欄 F 逐字**；`0 = Absent`／`1 = Present` | 同式 |

> **兩個 PROXI 皆為逐字命中**（不同於 b2-PS 之 `CAN node 24 (PAM )` ↔ `CAN node 24 (PAM/CVADAS)` 之不一致，§K K-8）。

### `lint_p_waivers_b2.tsv`

**起檔，0 列**（僅表頭）—— **本批無 `VAL_` 缺值之賦值**：
唯一寫 `$…$` 之訊號 `IPC_VEHICLE_SETUP3.SVC_Guidelines` 具完整 `VAL_`（2 項）。
`SVC_Gridlines_Req` 因拼字疑誤**不寫 `$`**，故不落入檢查 P 之判準。
**預期本批之 lint 檢查 P 為 0。**

---

## 3. **一列 BLOCKED —— `-063`，成因為上游**

**實測**：`SWE1-VC-SurroundCameraGridlines-063` 之 037 `Requirement Description`
**逐字全文為 `Surround Camera Gridlines`** —— 即**家族標題本身，無任何需求語句**。

| 佐證 | 內容 |
|---|---|
| 037 側 | `Categorization` = `Functional Requirement`，但 Description 只有標題 |
| SYSRA 側 | 其 `Source Requirement ID`（`Sys-RA-VF665_V42_VSM-857`）之 `分類 Category` = **`Heading`**（**A-VL7**，上繳 02 已登） |

**兩側互相印證：此 leaf 實為 Heading，被 037 誤標為 Functional Requirement。**

### 處置

**寫入一列，不略過**（`features/privacy/scripts/write_back.py` 之 R34-3 先例逐字：
「a leaf missing from the deliverable leaves an unexplained hole in the traceability table,
and the marker in Remarks is what makes the hole auditable」）。

| 欄 | 值 |
|---|---|
| `test_item` 上半 | `Surround Camera Gridlines`（037 之逐字全文，E56 通過） |
| 括號下半 | `(Blocked: the 037 description carries only the family title, so no behaviour is specified)` |
| `pre_conditions`／`test_procedure`／`expected_result` | 全為 `PENDING: DR-VL2 SWE1-VC-SurroundCameraGridlines-063` |
| `priority` | **P3** |
| `remarks` | 記 BLOCKED、成因、privacy R34-3 先例、A-VL7 之佐證、錨 DR-VL2(c) |

**未造任何需求語句**（§8.4.1）。**未剔除該 leaf**（母體仍 128，覆蓋 10／10）。

> **§4.6 之一項須指出**：本列原擬 `distinguishing_axis.axis = "none"`，
> 但 §4.6 明定 `axis="none"` ⇔ `duplicate_of` 已設，而本列**非任何列之重複**。
> 已改為 `mode`，`delta` 說明其與同族五條在**可驗性**上即為不同類。**自查所得，已修。**

---

## 4. 自檢（10 條，全項）

| # | 項 | 實測 | 判 |
|---|---|---|---|
| E38 | 覆蓋 | 10／10，落空 0 | **過** |
| E39 | R-S4 括號下半 | 違規 **0**；全批 10 個下半互不重複 | **過** |
| E40 | 尾句號 | **0** | **過** |
| E41 | `[..]`／`'..'`／`<..>` | **0** | **過** |
| E42 | `$..$` 皆可回溯解得 | **0** 違規 | **過** |
| E43 | PENDING 格式 | **0** 違規（15 項全合格式） | **過** |
| E44 | reasoning 2–5 句繁中 | **0** | **過** |
| E45 | ER／下半 modal | **0** | **過** |
| C | hedge | **0** | **過** |
| **E56** | 逐字全等（037 Description） | **10／10** | **過** |
| E86 型 | spec_ref 二節各歸各 | `1.11.1.1.31` ×4／`1.11.1.1.38` ×6 | **過** |

### lint 判準預檢（承 14 包補強後之範圍）

| 判準 | 實測 |
|---|---|
| **J 行首大寫（含 `test_item` 上下兩半）** | **0** |
| K CJK 於入簿欄 | **0** |
| Q 不可見字元・行尾空白 | **0** |
| V 行首空白 | **0** |
| M 空欄三態 | **0** |
| **R Pre-Condition 版面（含單 `and` 並列型）** | **0** |
| Procedure↔ER 1:1／步驟數 ≥2／`tc_title` 2–14 words | 全過 |
| bus-error 式限測試員送出步 | **0** 違規 |
| **§4.6 `axis="none"` ⇔ `duplicate_of`** | **0** 違規（見第 3 節末） |

> **一項自查修正已記**：初版之複合預檢正規式 `[一-鿿　-〿 ]` **末尾含一個普通半形空格**，
> 使其把所有含空格之句子判為命中（假陽 77 筆）。已拆為逐項判式並複驗，全 0。
> **該假陽未流入產物**，僅為檢查腳本之瑕疵。

### 分布

| 項 | 值 |
|---|---|
| priority | P2 **9**／P3 **1**（P3 為 BLOCKED 之 `-063`） |
| design_method | 等價劃分 4／功能測試 3／負向測試 2／狀態轉換 1 |
| **PENDING 項** | **15** —— `-031`／`-032` 各 2（`DynamicGrid.Req`）、`-066`／`-067` 各 2（`SVC_Gridlines_Req`）、`-068` 2（`TLM_Vehicle_Setup_Menu.Info`）、**`-063` 5**（BLOCKED 之四欄） |

---

## 5. §K 增補

### K-10 —— `-063` 之 037 需求文本闕如（見第 3 節）

037 之 `Requirement Description` 只有家族標題。**與 A-VL7（其 Source ID 於 SYSRA 為 `Heading`）
互為佐證**，指向上游之誤標。**待裁**：(a) 併入 DR-VL2(c) 一併詢問；
或 (b) 認定為 Heading 並自母體移除（母體由 128 → 127，
但 R-VL4 之母體定義為「037 之 Functional leaf」，改之須新裁決）。

### K-11 —— `SVC_Gridlines` 之拼字方向與 b1 之 K-1 型不同

規格與 037 寫 `SVC_Gridlines_Req`（TELEMATIC 側）**與** `SVC_Guidelines`（IPC 側，`-068`）——
**同一功能之兩個訊號，037 內部即用了兩種拼法**；而主 DBC 兩者皆為 `Guidelines`。
即 **IPC 側拼法與 DBC 一致（解得），TELEMATIC 側不一致（拼字疑誤）**。
上繳 04 之 R-VL18(b) 曾註「疑 DBC 側誤（Gridlines 為攝影機領域正確用語）」——
**本批之實測使該推定弱化**：若 DBC 側誤，則 037 之 IPC 側亦誤；
更可能是**上游對該功能之命名本身不一致**。**據實記明，不改判。**

---

## 6. 獨立判斷

1. **一列 BLOCKED 且成因具名**（第 3 節）—— 未造需求、未剔除 leaf。
2. **一項 §4.6 規則違反自查修正**（第 3 節末）—— `axis="none"` 蘊含 `duplicate_of`。
3. **一項檢查腳本之假陽自查修正**（第 4 節末）—— 正規式含半形空格，77 筆假陽，未流入產物。
4. **一項推定弱化已回報**（§K K-11）—— R-VL18(b) 之「疑 DBC 側誤」與本批實測不完全相容。
5. **本批未跑 lint 實跑** —— 下放包明定不寫工作簿。
   **惟依 b2-PS 之教訓（lint 抓出預檢漏掉之 J／R），本批已在生成端納入補強後之全部判準**，
   預期寫回後之 lint 對本批新增紅為 **0**（P 亦為 0，見第 2 節末）。**待寫回時驗證。**
6. **綠色通道**：本批為第 2／3。若第 5 節之預期成立（寫回後零新增紅），計數應可續。
   **但 `-063` 之 BLOCKED 是否算「零修訂」，屬分析層判定** —— 其內容係依規則正確地寫成
   PENDING，非缺陷，本執行層認為不應計為修訂。

---

## 7. `gate_all.py` 與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 509
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 5 檔，基線 4 列）
```

**`rulings_hash`** 依 R-VL13 待 Pei 重生；`body_sha8` 之他線變動依 **R-VL27(c)** 之但書不計。
**`canon_refs`** 含 `vsm_v42` 者 3 列，與上繳 02–14 逐字相同，本批 21 個新檔未增任何一列。
**`gates_tsv`／`lint_paths`** 與本線無關，先在。**無一支肇因於本包。**

---

## 8. 本包之寫入清單

| 檔 | 動作 |
|---|---|
| `generated/b2_camera_gridlines/*.json`（10）／`*.md`（10）／`INDEX.md` | **新建**（21 檔） |
| `data/lint_p_waivers_b2.tsv` | **起檔**（0 列，僅表頭） |
| `docs/upstream/13_b2_camera.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：`generated/b1_epb/`（凍結件）、`generated/b2_park_sense/`、
**`delivered/` 全三檔**、`sandbox/`（`base`／`b1`／`b2`／`wb_trial`）、`data/` 之其餘、
`docs/fw036/`、`scripts/`、`backend/`、`forms/`、`docs/runtime/`、
`features/vsm_v43/`、`features/vehicle_setting/`、`sources/`。
**git**：本包未執行任何 git 寫入指令。

---

## 9. 待 Pei／分析層

1. **§K K-10**：`-063` 之處置（併 DR-VL2(c) 或認定為 Heading 而改母體）。
2. **§K K-11**：`SVC_Gridlines`／`SVC_Guidelines` 之命名不一致方向，R-VL18(b) 之推定是否修正。
3. **綠色通道第 2 批之計數**（第 6 節 6）：BLOCKED 一列是否計為修訂。
4. 承前未結：b1＋b2 累積簿之出貨 A／B／C 三案（上繳 14 第 2 節）、
   §K K-1〜K-9、DR-VL1／VL2／VL4 送出、台帳重生、`DELIVERY_NOTE.md` 第五節之過時段落。
