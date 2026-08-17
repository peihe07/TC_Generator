# 上繳 06 — User Profiles / 基線稽核：xlsx 與 PDF 之 169 條逐節比對

- 產出層：執行層｜2026-08-17｜對象：分析層
- 下放包：`06a_rulings.md`（R-U25～R-U30、R-G4-1）＋ `06b_tasks.md`（作業 1–8）

---

## 0. 結論先講

**判定為系統性掉句 → 依 06b 作業 3 停手上報，未重建 `outline_map.json`。**

| 量 | 值 |
|---|---|
| 分母（標籤可於 PDF 定位之節）| **140 / 169** |
| **節數比（上界，無頁界切段）** | 24 / 140 = **17.1%** |
| **節數比（加頁界，本輪之數）** | 13 / 140 = **9.3%** |
| **字元比（加頁界）** | 1,963 / 31,192 = **6.3%** |
| **經逐條查證後之真掉句** | **4 節**（另 9 節為本工具之切段殘留）= **2.9%** |

**而判定為系統性者不是那個百分比，是它掉的東西是什麼。** 見 §3.4。

| 作業 | 狀態 |
|---|---|
| 1 條文入庫 | ✅ 七條逐字；R-G4 原文**未改**，R-G4-1 置其後 |
| 2 169 條全掃 | ✅ **不抽樣**；逐節結果落 `data/xlsx_pdf_audit.tsv` |
| 3 後續判定 | ✅ **系統性 → 停手上報，未重建** |
| 4 PLP3 | ✅ **可讀，且不需 `pdfimages`** —— 一直在文字層 |
| 5 PU id 擴充 | ✅ 20 → **32**，加 `source` 欄 |
| 6 R-U27 落地 | ✅ `PROF-002-03` 解除；DR #4 降 MEDIUM 並收窄標的 |
| 7 R-U28 落地 | ✅ A-UP02 兩支分列；DR #3 性質改 |
| 8 R-U30 登記 | ✅ 登於本 feature，**comfort 一個檔都沒動** |

**framework 未定稿**（06b 明文，待 R-U25 之結果）。

---

## 1. 量測條件（自陳，逐項）

**工具**：`scripts/audit_xlsx_vs_pdf.py`（可重跑）。

### 1.1 PDF 段落如何定位到 outline

每節之 xlsx Description 幾乎都以條款標籤起首（`PRACC1.)`、`NEWPR2.1)` …），
**實測 140 / 169 如此**。故：

1. 自 xlsx 取標籤：`^\s*([A-Za-z][A-Za-z0-9]*(?:\.\d+)*\.?)\)`
2. 於 PDF 全文（21 頁串接）搜「標籤 ＋ `)`」取其位置 —— **140 個全數定位成功，0 個找不到**
3. 該節之 PDF 段落 = 自其標籤起，至**下一個標籤**或**本頁頁尾**之較早者

### 1.2 多節同頁如何切分 —— **這一步改過一次，且改動很重要**

**第一版以「下一個標籤」為唯一邊界，得 17.1% / 16.8%。那是高估。**

逐條看最大差額才發現：`7.5`（ch7 末條）之段落一路吃到 p12 之頁首
「New Profile Setup 12」與整張流程圖之標籤；`11.5` 吃進 Table CPA2；
`9.9` 吃進 Profile Info Page 之整張表。**那些不是該條之續句，是下一頁的內容。**

本 spec 為投影片式版面、一頁一主題、條款不跨頁續寫，故加**頁界為硬邊界**，
得 9.3% / 6.3%。**兩組數都報**（§0），因為第一組是「若不看內容會得到的答案」。

### 1.3 比對前之正規化

- 去 `_x000D_`（xlsx 之硬換行殘留）
- **去 xlsx 側之 `(image: …)` 標記** —— 那是 export 之佔位符，不是條文；不去會使 xlsx 虛胖
- 空白正規化、去頭尾
- **不去標點、不改大小寫** —— 標點差異要看得見（其自成一類且**不算掉句**）

### 1.4 29 個無標籤之節

章標題（`4`、`5`…）、`1.x` 假設段等，其 Description 為純標題，
**PDF 側無段落可切**，故**不入分母**，另行列出。

### 1.5 R-G7 之對照向

**以 PDF 段落自己跟自己比**，140 節之差額須全為 0 —— **PASS**，
分類集合僅 `{相同, PDF 側無段落}`。

> 缺此向，下方任何非零差額都可能是本工具之正規化或切段所造成，
> 而不是 export 所造成。

---

## 2. 形態分類（加頁界後，140 節）

| 形態 | 節數 |
|---|---|
| 相同 | **116** |
| 標點/空白差異（**不算掉句**）| 9 |
| 句尾截斷 | 7 |
| 其他不一致 | 6 |
| PDF 側無段落 | 1 |
| xlsx 較長 | 1 |

---

## 3. 逐條查證：13 節之殘餘，**其中真掉句 4 節**

06b 要求判斷是否系統性，而**不逐條看內容就答不了這個問題**。13 節全部讀過：

### 3.1 本工具之切段殘留（**不是掉句**）—— 9 節

| 節 | 差額 | 多出來的是什麼 |
|---|---|---|
| `11.5` | +538 | Table CPA2 之表格列（同頁之表，非該條續句）|
| `10.3.1` | +224 | **`10.1` 之條文**（版面上緊接其後）—— 見 §3.3 |
| `8.12` | +177 | 圖說：`Avatars/icons are placeholders…`／`Choose/Edit Avatar - 7 inch`… |
| `8.5` | +130 | 流程圖之按鈕標籤：`Add New`／`Continue`／`Save & Continue`／`Cancel/"X"` |
| `14.2` | +24 | 按鈕標籤：`OK OK Yes Yes No No "X"` |
| `3.1`／`3.2`／`3.4`／`3.5` | +126／+64／+144／+137 | **相鄰 PLP 表之內容**（五表並排，文字層順序 ≠ outline 順序）|

### 3.2 真掉句 —— **4 節**，全語料查無

**判準**：把 PDF 有而該節 xlsx 無之片段，拿去查**全部 169 節之 xlsx Description**。
查得到 = 歸屬問題；**查不到 = 真掉句**。

| 節 | 掉的內容 | 類型 |
|---|---|---|
| **`9.8`** | `If a setting linked to the Profile is changed, a popup will indicate that it has been changed for the active Profile (PU0609).` | **一整句段落型條文，含 PU id** |
| **`9.3.2`** | `****R1 High Only: "Stellantis Account" to be replaced with "Connected Account"` | **變體覆寫註記** |
| **`9.1`** | `there will be a circled number 1 next to Resume Tutorials. It will be removed as a list item once the user has completed setup assistant` | **條文中段之一句**（05 輪已撞見）|
| **`11.4`** | `Table CPA2.) Connected Account vs Local Profile` 之表頭與列項（`Connected FCA Account`／`Local Profile`／`Personalization`／`App Store Download`／`Marketplace`／`Connected Navigation`）| **表格內容** |

### 3.3 一個我先前誤讀、於此更正

比對之中曾判「`10.3.1` 之內容跑到 `10.1`」。**那是我讀錯。**

實測 `10.1` 之 xlsx Description **全文**為：

> `R1 High Only: for the "Connected Account" category title (if applicable)
> the Description is the following: "Save your preferences to the cloud and
> access them from vehicle to vehicle."`

**那條註記本來就屬於 `10.1`**，只是版面上緊接 `10.3.1` 之後，被我的切段吃進去。
**故 `10.3.1` 不是掉句，是切段殘留** ——已計入 §3.1。

> **同時它證實了 R-U28 之歸類**：`10.1` 確為**變體覆寫條款**，
> 與 R-U28「10.1／11.1／11.2 為變體覆寫條款且無 SWE 需求」相符。

### 3.4 判定：**系統性**，而理由不在百分比

真掉句 4 / 140 = **2.9%**。**若只看這個數，答案會是「低且非系統性」。
我判定為系統性，理由有三，逐項可反駁**：

**一、掉的三種東西，恰好都是判讀關鍵。**

| 掉的類型 | 它決定什麼 |
|---|---|
| 變體覆寫註記（`****R1 High Only:`）| **TC 之適用範圍** —— 哪一種車該不該有這條 |
| 表格內容（Table CPA2）| **ER 之列舉** —— 該畫面上有哪些項 |
| 含 PU id 之行為句（`9.8` 之 PU0609）| **一整條可驗行為** |

**二、`9.8` 掉的是純段落型條文，沒有任何形態上的理由該被掉。**

其餘三處還能解釋成「export 不處理表格／不處理 `****` 標記行」；
**`9.8` 是一句正常的散文條文，和它前後被正確 export 的句子沒有結構差別。**

> **這一點最要緊**：如果連純段落句都會掉，**我就指不出一個「不會掉」的節型** ——
> 而「指不出安全節型」與「非系統性」不能並存。

**三、`****` 註記之全量掃描顯示掉法不一致。**
PDF 中 10 條 `**` 起首之註記，xlsx 側有 6 條、無 4 條。
**同一種形態，有的進了有的沒進** —— 那比「整類都掉」更難防：
整類都掉還能整類補，時有時無則每一條都得查。

**故依 06b 作業 3 之系統性分支：停手上報，未重建 `outline_map.json`。**

---

## 4. 04／05 輪之判讀，哪些建於 xlsx 側（06b 作業 3 之要求）

| 輪 | 結論 | 依據面 | 若以 PDF 重建會不會變 |
|---|---|---|---|
| 03 | 三閘 180／25／2 | **037**，非 spec | 不變 |
| 03 | 集合對集合 135 = 135 | **xlsx 之 Source ID 欄** | 不變（R-U25：xlsx 之**結構**是完整的）|
| 03 | 被引 135 條之長度分布、圖片參照數 14／17 | **xlsx Description（`len` 欄）** | **會變** —— 長度低估，圖片標記數不等於實際圖數 |
| 04 | `Service` 22 條之可觀察端判讀 | **xlsx Description** | **可能變** —— 若某條之掉句正好含可觀察量。**本輪未逐條複查該 22 條** |
| 04 | 14 節帶圖之依賴分類 | xlsx（數 `(image:` 標記）| 已於 05 輪以 PDF 改判 |
| 05 | 6 節中 5 節改判、完全依賴歸零 | **PDF** | 不變 |
| 05 | PLP 表可讀 | **PDF** | 不變 |
| 05 | PU id 32 個 | **PDF** | 不變 |
| 05／06 | framework 之 Layer 2／3 對映 | **037 之章別**，非 spec 內文 | 不變 |

> **要緊的是第四列**：`Service` 22 條之判讀全部讀 xlsx Description，
> 而本輪證明那些 Description 可能少句。**本輪未逐條以 PDF 複查該 22 條** ——
> 列為 §7 之未驗項。R-U21 已據該判讀裁定「22 條全數納入生成母體」，
> 該裁定之依據面因而有一個未量之邊。

---

## 5. 作業 4 — PLP3：**可讀，且不需 `pdfimages`**

R-U29 假設「PLP3 之列項可能在點陣圖內」，指示以 `pdfimages` 抽 p5 之 11 張圖。

**實測：不需要。列項一直在 PDF 之向量文字層裡。**

```
Memory Seat Module   Low   High
  Memory Profiles (Seats, mirrors, steering wheel)
  Massage seat preferences (linked to memory seat positions)
PLP3.) Profile Linked Preferences - Memory Seat Module
```

**05 輪未定位到它的原因**：p5 五張 PLP 表並排，**文字層之順序與 outline 順序不一致** ——
PLP3 之列項排在 `PLP3.)` 標籤**之前**，且落在 `3.5` 之切段範圍內。
05 輪以「`3.3` 之段落」去找，自然找不到。

> **這是一條死路之記錄，供日後不重試**（06b 作業項 4 之要求）：
> **不是抽圖能力的問題，是切段方向的問題。** 在版面並排之表格上，
> 「標籤之後即其內容」這個假設不成立。

**五張 PLP 表現皆可讀**，`PROF-001-01` 之 ER 範圍不再有缺項。

---

## 6. 作業 5–8 之落地

| 作業 | 落地 |
|---|---|
| **5** | `data/spec_popup_ids.tsv` **20 → 32 列**，加 `source` 欄（`xlsx_text` 20／`pdf_only` 12）。原 20 列之 `refs`／`sections` **未改**。12 個 pdf_only 之 `sections` 欄填其所在頁之條款節次（**版面歸屬，非引用關係** —— 檔頭已註明）|
| **6** | `PROF-002-03` 阻斷解除；DR #4 **HIGH → MEDIUM**，索取標的由「整份 Pop Up List 版本」收窄為「該二列之 popup **內文**」，並記明觸發條件已由 spec PDF p6 提供 |
| **7** | `ANOMALIES.md` 之 A-UP02 改記為「spec 有而 SWE 未涵蓋」，**兩支處置分列**；`DATA_REQUESTS.md` 之 DR #3 性質改為「上游覆蓋缺口」。另附 06 輪之補充實測（`10.1` 之全文即變體覆寫條款）|
| **8** | comfort 孤兒檔登為 **`N-XF01` 跨 feature note**，寫在本 feature 之 `ANOMALIES.md`。**comfort 一個檔都沒動**（實測：`find features/comfort -newer` 無命中）|

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷（不得省略）

**有，五項。**

| # | 該驗而未驗 | 性質 |
|---|---|---|
| 1 | **`Service` 22 條未以 PDF 逐條複查** —— R-U21 之裁定建於 xlsx 側之判讀，而本輪證明 xlsx 可能少句 | **真缺口**。若某條掉的正好是其可觀察端，該條之分群會變。**22 條，逐條可查** |
| 2 | **29 個無標籤之節完全沒比** —— 它們不入分母，也就從未被檢查過 | **真缺口**。其中含 `3`（PLP 表章）與各章標題；若 export 對它們有別的掉法，本輪量不到 |
| 3 | **「頁界為硬邊界」之假設未反向驗證** —— 我斷言「條款不跨頁續寫」，依據是 140 個標籤全數與 xlsx 起首相符，**那證明的是起首，不是結尾** | **方法缺口**。若有條款跨頁，其續頁部分會被我當成下一節之殘留而不計入掉句 —— **本輪之 2.9% 因而是下界** |
| 4 | **`pdf_only` 之 12 個 PU id，其 `sections` 欄為版面歸屬** | 記載限制，已於檔頭註明。真正的引用關係須逐一讀其上下文，本輪未做 |
| 5 | **重建之影響面未量** —— 若 Tier 2 裁定重建 `outline_map.json`，哪些既有產物要跟著改（`expected_cited_sections.tsv` 之 `chars` 欄、`generation_sections.tsv`…）本輪未清點 | 待裁後才需要，惟先講明 |

**另記一件方法上的事**：本輪之第一版切段給出 17.1%，加頁界後 9.3%，
逐條讀完後真掉句 2.9%。**三個數差了六倍，而三次用的都是同一份資料。**

> **一個比率若不附上「它把什麼算成掉句」，它就不是一個量測。**
> 06b 要求「節數比與字元比分列」擋住了一半的問題；
> 擋住另一半的是**逐條去看那 13 節到底多出了什麼** —— 那不在指示裡，
> 是不看就答不了「是否系統性」。

---

## 8. 動作清單 —— 與 git 陳述逐項對照（R-G6，唯讀與改狀態分列）

| # | 動作 | 對象 | 是否 git |
|---|---|---|---|
| 1 | 檔案追加 | `RULINGS.md`（＋七條，R-G4 原文未改）| 否 |
| 2 | 檔案編輯 | `ANOMALIES.md`（A-UP02 重估 ＋ N-XF01 新增）| 否 |
| 3 | 檔案編輯 | `DATA_REQUESTS.md`（DR #3 性質、DR #4 降級與收窄）| 否 |
| 4 | 檔案**重寫** | `data/spec_popup_ids.tsv`（20 → 32 列，加 `source` 欄）| 否 |
| 5 | 檔案新建 | `scripts/audit_xlsx_vs_pdf.py`、`data/xlsx_pdf_audit.tsv` | 否 |
| 6 | 檔案新建 | `docs/upstream/06_baseline_audit.md`；`docs/INDEX.md` 編輯 | 否 |
| 7 | **唯讀**讀取 | spec PDF（21 頁）、spec xlsx、`data/outline_map.json`、他 feature 之檔 | 否 |

**未執行任何會改變 repo 狀態之 git**：`commit`／`push`／`add`／`checkout`／
`restore`／`reset`／`stash`／`clean`／`rm`。

**唯讀 git**：**一次都沒跑**（本輪之查證全以檔案系統與 PyMuPDF 完成）。

**未動**：`data/outline_map.json`（**作業 3 之停手所在**）、
`data/spec_id_to_outline.tsv`、`data/expected_cited_sections.tsv`、
`data/generation_sections.tsv`、`data/recon_leaf_to_section.tsv`、
`framework.md`（**未定稿**）、`feature.yaml`、`BASELINE.sha256`、
`inputs/`（含 R-U17 之 spec 副本）、`scripts/recon.py`、
**comfort／sxm／amfm／projection／home 之任何檔**。

---

## 9. 待裁

1. **`outline_map.json` 是否重建、以何為準**（06b 作業 3 之 Tier 2）——
   本層已停手，未重建。
2. **`Service` 22 條是否以 PDF 逐條複查**（§7 第 1 項）—— 影響 R-U21 之依據面。
3. **29 個無標籤之節是否納入比對**（§7 第 2 項）。
4. **「條款不跨頁」之假設是否須反向驗證**（§7 第 3 項）—— 其結論影響 2.9% 是不是下界。
5. **framework 定稿**（待第 1 項）。
