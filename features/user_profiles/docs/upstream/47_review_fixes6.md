# 47 上繳 — AC-1：`TC-189` 之欄內殘留，與欄內矛盾之自檢

- 產出層：執行層｜2026-08-19｜對象：分析層
- 來源包：`docs/handoff/47_review_batch06b.md`（作業 1–2）
- **git 未執行**；**未產出交付件**；交付與 RD 寄出屬 Pei

## 0. 一頁摘要

| 作業 | 結果 |
|---|---|
| 1 | `TC-189` 之 `reasoning` 前半殘留已刪；**新掃描 AC-1 立起**（兩條判準、四個方向性案例），**全批命中 0** |
| 2 | 全閘重跑：**17 支之自我測試全過**，語料違規 0 |
| 連帶 | `TC-189` 之變動使 `44_review_pack_33b` 過期 → **同輪重出**為 `47_review_pack_33b.md` |

---

## 1. AC-1 之修正

`TC-189`（`084`，8.12）之 `reasoning`：

| | 內容 |
|---|---|
| 原 | 為什麼這樣切：`design_method` **取狀態轉換** ——`design_method` **取功能測試而非狀態轉換**：所驗者為值之保留…… |
| 現 | 為什麼這樣切：`design_method` **取功能測試而非狀態轉換**：所驗者為值之保留，畫面之來回不是系統狀態之遷移（K-4a） |

**成因確認**：41 輪 K-4a 判紅後改判方法時，**只替換了後半句而未刪前半**。
欄位本身填功能測試、後半之理由亦正確 —— 錯的只有那句殘留。
已於生成器該處留註記，記其成因。

---

## 2. 新掃描 AC-1：欄內自相矛盾

### 2.1 它與 K-4a／K-4b 之分界

| 掃描 | 比的是 |
|---|---|
| K-4a | `design_method` 欄 **vs** procedure 之形態 |
| K-4b | `priority` 欄 **vs** `priority_basis` 之措辭 |
| **AC-1** | **同一欄之內** |

**C-2（18 輪）是跨欄之同形**（文字稱「無界前基準線」而欄位掛 BVA）——
本條是其欄內版本。**兩支既有掃描比的都是欄與欄之間，欄內矛盾對它們不可見。**

### 2.2 兩條判準（依 47 包所指定）

| # | 形態 | 為何可測 |
|---|---|---|
| AC1-a | 同欄內 `design_method` 出現 **≥ 2 次** | 一個欄位不需要說兩次自己取了什麼方法 |
| AC1-b | 「取／為 Y **而非／不是** X」，而 **X 於同欄他處以肯定形式（`取 X`／`為 X`）再現** | 被否定者又被肯定，即矛盾本身 |

掃 `reasoning` 與 `remarks` 兩欄（47 包所指定者）。

### 2.3 **全批命中 0**

```
## AC-1 —— 欄內自相矛盾（reasoning／remarks）：0 處待判
```

**0 之意義是修正已生效，不是從來沒錯** —— `TC-189` 之原形正是本掃描之紅向案例。

### 2.4 四個方向性案例（`audit_consistency` 52 → **56**）

| 向 | 案例 | 結果 |
|---|---|---|
| 紅 | **`TC-189` 之原形**（先稱取狀態轉換、再稱取功能測試而非狀態轉換） | 列入 |
| 綠 | 其修正後之形 | 不列入 |
| 綠 | **護欄**：正當之「取 A 而非 B」而 B 未於他處被肯定 | 不列入 |
| 綠 | **護欄**：`remarks` 提及 `design_method` **一次** | 不列入 |

第三條護欄是必要的：語料中「取 X 而非 Y」是**正常且鼓勵的寫法**
（改判時具名其所棄者）。硬判會把 33 條正確的 reasoning 判紅。

### 2.5 盲區（R-G11）

1. **同義改寫者抓不到。** 「取狀態轉換」vs「屬狀態遷移之驗證」——
   AC1-b 以**逐字**比對認「被否定者」，改寫過的說法比不到。
   **本次之所以抓得到，是因為殘留與現行句用了同一個詞。**
2. **只掃中文之「取／為 … 而非 …」句式。** 英文欄位（ER／procedure）
   之欄內矛盾不在射程內 —— 那類由 §6 之行數對應與 T-1／AB-1 承擔。
3. **只掃 `reasoning` 與 `remarks` 兩欄**（47 包所指定者）。
   `priority_basis` 亦為散文欄而未納 —— **具名此缺口**，
   若分析層認為應納，加兩行即可。

### 2.6 已入 `audit_pending`

`SCAN_ROUND["AC-1"] = 47`，本輪命中 0 故登記表無新列。
**其存在使日後之命中會被登記與追蹤**，不會只出現在某一輪的上繳裡。

---

## 3. 連帶：`44_review_pack_33b` 過期，同輪重出

`TC-189` 之 `reasoning` 變動 → 依 G-G 之附件檢查：

```
44_review_pack_33b.md：相符 15 條，不符 1 條
  AA-1 NR1L-UserProfiles-189: 指紋 `54d8cd94d88a` 與現況 `fbeb005e8255` 不符
44_review_pack_33b.md：有變動 1 條
  NR1L-UserProfiles-189 — reasoning
```

**已重出為 `47_review_pack_33b.md`**（相符 16 條、不符 0 條），舊檔加警語保留。

依 profile §7.5.1（46 輪所立）：**重出是產出方之義務，重讀是覆核方之判斷。**
`TC-189` 已由分析層讀畢（47 包記 `33b` 已讀 183–189），
**其變動僅為 `reasoning` 一欄且係刪去殘留** —— 但是否重讀由分析層定，
本層不代為認定。

---

## 4. 作業 2 —— 全閘輸出

```
lint_tcs                : 64 / 64 directional cases PASS   語料 189 條，違規 0
audit_consistency       : 56 / 56 directional cases PASS   AC-1 0 處、AB-1 16 處待判
audit_pending           :  5 / 5  directional cases PASS   新命中 0，抑制 59 條，違規 0
audit_enums             :  7 / 7  directional cases PASS   違規 0
audit_verbs             :  5 / 5  directional cases PASS   違規 0
audit_variant_pairs     :  7 / 7  directional cases PASS   違規 0
audit_assignment        :  6 / 6  directional cases PASS   違規 0
audit_delegation        :  8 / 8  directional cases PASS   紅 0
lint_variant_labels     : 11 / 11 directional cases PASS
lint_outbound_doc       :  8 / 8  directional cases PASS   本輪各檔違規 0
verify_dv_integrity     :  6 / 6  directional cases PASS
build_review_pack       :  4 / 4  directional cases PASS
stamp_static_doc        :  5 / 5  directional cases PASS
write_back              : 10 / 10 directional cases PASS   未產出
build_batch_context     :  8 / 8  self-check items PASS
render_spec_region      :  7 / 7  checks PASS
scan_override_notes     : 掃描結果與 data/override_notes_m3.tsv 一致
```

`design_method` 分布：功能測試 120、狀態轉換 33、負向測試 16、
情境／用例 9、邊界值分析 8、基礎故障注入 3。
`priority` 分布：P0×38、P1×66、P2×71、P3×14。

---

## 5. 附件（G-G 之常規）

### 5.1 現行四份 review pack

```
44_review_pack_24a.md：相符 11 條，不符 0 條
45_review_pack_24b.md：相符 11 條，不符 0 條
44_review_pack_33a.md：相符 17 條，不符 0 條
47_review_pack_33b.md：相符 16 條，不符 0 條
```

**被取代者**（已加警語）：`40_24a`／`40_24b`／`41_33a`／`41_33b`／
`44_24b`／**`44_33b`**。

### 5.2 三份靜態轉錄

```
27_rd_queries_v2.md：不符 0 條
28_provenance4.md：不符 0 條
34_provenance5.md：不符 0 條
```

---

## 6. 現況

| 項 | 值 |
|---|---|
| TC | 189 ／ leaf 180 / 180 |
| 已覆核 | 171 / 189（47 包所記）；餘 18（`157`–`165`、`174`–`182`）|
| 閘 | 17 支（`audit_consistency` 之掃描 13 支）|
| 產出 | 無 |
| 擋交付者 | 無 |

---

## 7. 獨立判斷

1. **AC-1 與 AA-1／AB-1 是同一件事的三個位置。**
   AA-1：pack 之轉錄與語料不同步（**檔與檔之間**）。
   AB-1：ER 之兩端未指名（**句與句之間**）。
   AC-1：同一欄先後兩句互相否定（**欄之內**）。
   **三者都不是「寫錯」，是「改對了但沒把舊的拿掉」** ——
   AA-1 沒重出 pack、AB-1 改了條文理解而 ER 沒跟上、
   AC-1 換了後半句而前半留著。
   **本專案現在最常見的缺陷型態是「殘留」，不是「錯誤」。**
   建議：凡以「改判／改寫」落地之修正，其 diff 應同時檢查
   **被取代者是否已消失**，而不只檢查新內容是否正確。
   AC1-a／AC1-b 是這件事在單一欄位上的機械化；跨欄與跨檔尚無同型工具。

2. **AC-1 之判準能抓到本次，靠的是一個巧合：殘留與現行句用了同一個詞。**
   §2.5-1 已具名此盲區。**它的意思是：這支掃描的召回率無法估計。**
   0 處待判在這裡不代表「沒有殘留」，只代表「沒有這種形狀的殘留」。
   本層不建議據此宣稱欄內矛盾已清 —— **它是一道護欄，不是一次普查。**

3. **`priority_basis` 未納入 AC-1（§2.5-3）是我照 47 包字面執行的結果。**
   該欄同為散文、同樣會在改判時被改（K-4b 即為此而設），
   **其殘留風險與 `reasoning` 相同**。
   我未擅自擴大範圍；若分析層同意，下輪加兩行。

4. **本輪之修正再次使一份 pack 過期（第三次：44 輪 24b、45 輪 24b、47 輪 33b）。**
   三次都是「修正 → pack 過期 → 同輪重出」。
   這已是穩定的節奏，而它有一個代價：**`docs/upstream/` 現有 6 份被取代之 pack**，
   每份都帶警語且保留不刪。**目前尚可讀，但再過十輪會不好找現行版。**
   建議：於 `docs/INDEX.md` 立一節「**現行 pack 一覽**」，
   四行，隨每次重出更新 —— 比在檔案清單裡辨認檔名可靠。
