# 19 — Comfort HMI / 批次 2 補齊：第十・十一軸、R-C29、R-C30

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 29
- 結果：**Tri-Mode Climate 14 個 leaf 全數生成**（tc_id -015 … -028），
  無停下、無 withheld。lint **35/35 PASS，0 finding，28 條**。
  `json-key-coverage` 擴及 doc 層；`spec-ref` 系列改判多節；
  `DELIVERY.sha256` 增 `type` 欄與 ENTRY 003。**未寫回 workbook。**

---

## 1. 條文與 profile

### 1.1 R-C29、R-C30 貼入

`RULINGS.md` 現有 **32 個**逐字條文區塊（R-C1…R-C30 ＋ R-C4-1、R-C5-1）。
兩條各附一段來源說明（分別指向上繳 18 §3.5 第 3 問與 17 §3.5），
再接逐字區塊。

### 1.2 profile §3.2 增第十、十一軸

設備配置軸由九項增為十一項。兩軸之來源節**皆為 3.4**，並各加一段說明：

- **第十軸 REAR DEFROST 之有無** —— 明寫「**3.3 之條文（C21 一句）不含
  任何裝備條件，不得作為本軸之出處**」，並指向 R-C29 之處置
- **第十一軸 soft top 車身之有無** —— 明寫與機型軸（R1 Low／High）
  **為不同維度，不併入**

soft top 之措辭限制以引用區塊寫入：

> **措辭限制**：PC 一律寫「soft top」，**不寫成「JL or JT」**。條文為
> `such as JL/JT`（**例示**），寫成 JL/JT 即窄於條文 —— 屬 §8.4.1 之
> **反向造值：把例示讀成窮舉**。JL/JT 得於同句以 `such as` 形式引為例示。

---

## 2. 生成之 3 條（tc_id -026 … -028）

| tc_id | req_id | 節 | tc_title | 步/ER | spec_ref |
|---|---|---|---|---|---|
| -026 | 025-01 | 3.3 | MAX DEF and REAR DEF stay available while climate is off | 3/3 | **3.3; 3.2; 3.4** |
| -027 | 025-02 | 3.3 | Other climate functions are not available while climate is off | 2/2 | **3.3; 3.2; 3.4** |
| -028 | 026 | 3.4 | Rear defrost button is absent when the vehicle has no rear defrost | 2/2 | 3.4 |

既有 11 條**未重跑內容**，逐欄未變；`gen_batch2.py` 之 3.1／3.2 區塊未動。

### 2.1 R-C29 之三項義務，逐項落實

**義務一（出處節列入 `specification_reference`）**：-026／-027 之 spec_ref
為三節，格式為 `; ` 分隔且**每項各帶完整 stem**：

```
SYS1_..._(September_25_2023)_3.3; SYS1_..._(September_25_2023)_3.2; SYS1_..._(September_25_2023)_3.4
```

**每項各帶 stem 而非只帶一次**，是為了讓 R-C1 之 stem 檢查**逐項成立**
—— 只檢查第一項再假設其餘相同，正是這條 pipeline 反覆栽的形態。

**義務二（reasoning 說明跨節取據且未擴張）**：3.3 之 reasoning 內寫明
「引用其裝備事實不等於驗證該兩節之行為，本批未擴張至 3.2 之 MAX DEF
連動或 3.4 之按鈕隱藏（§8.2.1）」。

**義務三（coverage 分母以 leaf 計）**：本批 14 leaf → 14 TC，
`specification_reference` 之節數（-026／-027 各 3）**不進分母**。
現時全 feature 之 coverage 仍為 **28 / 403 leaf**。

### 2.2 PC 之節次標註 —— 逐行第一問

| tc_id | PC 行 | 標註 | 第一問具名之句 |
|---|---|---|---|
| -026／-027 | 車輛配備 MAX DEF | **(3.2)** | 「**On vehicles with MAX DEF**, MAX DEF replaces FRONT DEF button」 |
| -026／-027 | Rear defrost 存在 | **(3.4)** | 「the rear defrost button will not appear **when not present in the vehicle**」 |
| -028 | 車輛為 soft top（such as JL/JT） | (3.4) | 「**For soft top vehicles such as JL/JT**, when configured」 |
| -028 | Rear defrost 不存在 | (3.4) | 同上句之 `when not present in the vehicle` |

**-026／-027 兩行皆為跨節**——這是 R-C29 之首次適用，且**同一條 TC 之兩行
指向兩個不同的他節**。3.3 自身之 `full_text` 只有一句，**不含任何裝備條件**，
故若照舊標 `(3.3)`，兩行都會在 R-C28 第一問失敗。

### 2.3 climate off 之落點 —— procedure，非 pre_conditions

`climate off` 為 3.3 明文之 trigger（R-C28 第二問通過），但 **TC 自身之
步驟必須自行建立它**（按 OFF），故依第三問落於 procedure 首步。

這與 **TC-014 之 PC3 同形**（22 §1.1 判過的那一次）：資格成立不等於落點。
本次是**生成時即照此處理，非事後被抓**。

---

## 3. `-027` —— 一處我改了設計，理由須明說

初稿之 procedure 第 3 步為「按下 MAX DEF 與 REAR DEF 以外之某個 climate
功能鍵」，ER 3 為「該功能不會啟動」。

**讀 2.10 全文後刪除該步**，因為它與條文明文牴觸：

> If a user presses a temp/fan control to turn climate back on, the system
> **reinstates to the last level of that feature** and if Front/Max Defrost
> is selected, the climate system turns back on

**按 temp／fan 控制不是「沒反應」，是「讓 climate 復電」。** 若照初稿寫入，
該 TC 會以一個 spec 明文反對的行為作為期望結果 —— 且它會 pass 所有 gate，
因為沒有任何 gate 讀得到 2.10。

改後之 -027 只用 3.3 自身之詞 **`available`** 判定，不按任何鍵、不驗
greyed out。2.10 擁有兩樣東西並在 reasoning 內具名：**視覺處置
（grey out）** 與 **按鍵復電行為**，兩者皆不由本批驗證（§8.2.1）。

**這一項是本包唯一一次「差點寫出造值」，且抓到它的不是 gate，是去讀了
委派節的全文。** 上繳 18 §6 當時已把 2.10 標為委派節，那筆記錄是本次能
及時停手的唯一原因 —— 記下委派節不只是為了 reasoning 好看。

---

## 4. gate 變更 —— 兩處，四項反向驗證

### 4.1 `json-key-coverage` 擴及 doc 層（29 §5.1）

掃描對象由「TC 物件」擴為「TC 物件 ＋ doc 物件」，白名單由 8 增為 **14 項**
（增 `assumptions`／`batch`／`outline`／`parent`／`source_clause`／`tcs`）。
具名回報行同步改寫，標明涵蓋兩層。

**反向驗證**：於某 doc 物件加入未具名之 `review_note` →

```
[FAIL] json-key-coverage: SWE1-HVAC-025 (doc): key(s) ['review_note'] neither
map to a workbook column nor appear in NOT_IN_WORKBOOK …
```

**下放包之診斷完全正確**：擴及之前，白名單裡的 `reasoning`／`keywords`／
`duplicate_of`／`distinguishing_axis` 四項是**名義上的具名** —— 它們在
doc 層，而 gate 只掃 TC 層，那四個名字**攔不到任何東西**。
白名單看起來有八項，實際生效的只有四項。

### 4.2 `spec-ref-stem` / `spec-ref-outline` 改判多節

原 gate 假設 `specification_reference` 為**單一**節：
`ref[len(STEM)+1:]` 直接切出 outline。R-C29 之多節格式會使該切法把
`3.3; SYS1_..._3.2; SYS1_..._3.4` 整串當成一個 outline，
**必然 FAIL 且理由是錯的**。

改為：以 `;` 切項 → 逐項驗 stem → 逐項驗 outline ∈ 129 節 →
另加兩項新檢查：

| 新檢查 | 理由 |
|---|---|
| **不得重複列同一節** | 重複不會被 outline 檢查抓到（每項各自合法），但它是複製貼上的痕跡 |
| **首項須為 TC 之所屬節** | R-C29 之「本節領頭，取據節在後」；順序若亂，讀者無從分辨哪一節是驗證對象、哪一節只是 setup 出處 |

**反向驗證（三項）**：

| 注入 | 結果 |
|---|---|
| 把 -026 之 spec_ref 首項改為 `3.2` | FAIL — `first specification_reference is not the TC's own section '3.3'` |
| 把 -028 之 spec_ref 改為 `("3.4","3.4")` | FAIL — `specification_reference repeats a section` |
| 把 -026 之第二項改為 `3.99` | FAIL — `'3.99' is not one of the 129 cited sections` |

第三項尤須注意：**它證明逐項驗證真的逐項在跑**。若沿用「只切一次」之舊寫法，
`3.99` 會藏在字串中間，第一項合法即整串放行。

### 4.3 gate 總數仍為 35

本次為既有 gate 之**判定改寫**，非新增 gate。`spec-ref-stem`／
`spec-ref-outline` 名稱未變，覆蓋範圍變寬。

---

## 5. `DELIVERY.sha256` —— `type` 欄與 ENTRY 003

### 5.1 `type` 欄

台帳頭部增一段，二值定義並說明其差別**不是位置而是責任**：

> `produced` —— `output/` 之產出物。「這份位元組是我們做出來的」
> `folder-attachment` —— 置入客戶交付夾之附件。「這份位元組是我們放過去的」
>
> `produced` 者其內容由本 pipeline 負責；`folder-attachment` 者其內容
> 來自別處（`spec-index`），本 pipeline 只負責「放進去的與來源逐位元組相同」。

ENTRY 001／002 補標 `type: produced`。**兩者之 hash 與既有記載未動。**

### 5.2 ENTRY 003（`folder-attachment`）

含操作（`cp` ＋ `cmp` 逐位元組）、依據（A-CF02／Pei 選項 1）、目的地全路徑、
來源、bytes、先放後移之順序、待辦（SR25 移除屬 Tier 3）、未做事項。

**一項限制須寫明，否則會被讀成持續驗證**：

> 本 ENTRY 之 hash 指向 **repo 內之來源檔**，非交付夾內之副本 ——
> 交付夾在 repo 外，`shasum -c` 之相對路徑到不了它。故本 ENTRY 驗的是
> 「**來源仍未被動過**」，交付夾那一端之相符由當時之 `cmp` 記錄於此，
> **事後不可重驗**。此為跨樹台帳之固有限制。

複驗：`shasum -a 256 -c --ignore-missing DELIVERY.sha256` → **6 行全 OK**。
（4 行為 ENTRY 001／002 之產出鏈，2 行為 ENTRY 003 之來源。）

### 5.3 一個我自己犯的錯，當場抓到

初稿之 ENTRY 003 兩個 hash，我是**從先前輸出被截斷的顯示補完的**——
前 32 字元正確，其後為臆造。追加後立刻 `shasum -c`，兩行 FAIL，
以實測值更正後全 OK。

**寫進台帳之前先驗一次台帳，這一步不能省。** 若當時只看「檔案有複製成功」
就收工，台帳會帶著兩個假 hash 存活到下一個人來驗的那天。

---

## 6. `RUNBOOK.md` —— `A-CF-XX` 例示寫法

新增一節，含三部分：現象（`anomaly-id-registered` 掃 `docs/` 全部 `*.md`，
而上繳包與下放包都在 `docs/` 內）、上繳 17 撞上它的實例、約定
（例示一律寫 `A-CF-XX`，編號位改為非數字）。

另寫明**不要做的兩件事**：

> 不要為了寫文件而放寬 gate 的 pattern，也不要把例示用的編號真的登記進
> `ANOMALIES.md`。前者讓真正的孤兒編號溜過去，後者在 anomaly 台帳裡塞
> 一筆不存在的異常 —— 兩者都是為了文件方便而弄髒機制。

---

## 7. lint

```
35 / 35 gates PASS; 0 finding(s) across 28 TCs
```

`gen_pilot.py` 與 `gen_batch2.py` 連續重跑，輸出逐位元組不變（冪等）。

---

## 8. §9 self-check 17 項 —— 依 R-C23，僅列**新 3 條**之判定與變動項

前 25 條之自評見上繳 18 §8，未變。以下為 -026／-027／-028 之逐項依據。

| # | 項目 | 判 | 獨立依據（非 lint 覆述） |
|---|---|---|---|
| 1 | Test Set 與 framework 相符 | PASS | 三條之 `test_set` 皆 `Tri-Mode Climate`，與 3.1／3.2 之 11 條同字串；`framework.md` Part N 第 3 組名稱逐字元比對相同 |
| 2 | tc_title 形狀／字數／sibling token／無 modal | PASS | 逐條讀：字數 11／10／12（皆在 2–14）；sibling token 為 `MAX DEF and REAR DEF`／`Other climate functions`／`Rear defrost button`，三者互斥且可見於 title 本身 |
| 3 | PC 僅 state/env 且為 spec trigger | PASS | 三條共 6 行 PC，**全為裝備配置**（MAX DEF 有／rear defrost 有／soft top／rear defrost 無）。`climate off` **刻意不在 PC 內** —— 它是步驟可建立者，落 procedure（§2.3）。另實測 PC 內無動作動詞 → 0 命中 |
| 4 | Input Test Data 欄位歸屬 | PASS | 三條之 `input_test_data` 皆 `NA`；本節無數值輸入，操作對象即 UI 元件，已在 procedure |
| 5 | 步驟可執行、無禁用動詞、Final Step 擁有驗證 | PASS | 以 §5.1 之九個禁用主動詞（另加 `locate`／`check`）掃 **28 條**之行首動詞 → **0 命中**。三條之動詞為 `Turn`／`Read`／`Open`，`Read` 為 §5.1 之偏好動詞 |
| 6 | 步驟長度與意圖層級 | PASS | 步數 3／2／2，皆為「建立狀態 → 逐項讀取」；無 `... to ...` 贅接 |
| 7 | 標準 setup 片段逐字重用 | **N/A** | 同 18 §8 第 7 項。`PC_MAXDEF_X`／`PC_REARDEF`／`PC_SOFTTOP` 為生成器常數，**同節內逐字重用，跨節不套用** |
| 8 | CLI／tooling 步驟格式 | **N/A** | 三條皆 HMI 操作，無 CLI |
| 9 | 需要前後對照時有基線步驟 | PASS | -026／-027 之 ER 第 1 行為 `The climate system is off`，即步驟 1 所建立之前置狀態之確認；-028 之 ER 第 1 行為 `The climate screen is displayed`。三條皆非「前後差」型，基線步驟之作用是**確認 trigger 條件確已成立**再讀結果 |
| 10 | procedure↔ER 1:1、ER 可觀察、無 modal | PASS | lint 依據為 `proc-er-1to1`／`er-modal`，故另查「可觀察」：三條共 **7 行 ER** 逐行讀，主詞為 `climate system`／`"MAX DEF" button`／`"REAR DEF" button`／`climate functions`／`climate screen`／`rear defrost button` —— **皆為系統側之物，無一行以觀察者為主詞** |
| 11 | 無 FP／FF；supported 配 negative | PASS | FF：`climate off` 由步驟 1 建立，未假定。negative：-026（兩者**可用**）與 -027（其餘**不可用**）成對；-028 為單向顯示規則，**未作反向配對** —— 條文未述 rear defrost 存在時之行為，配對需條文支撐（見 §8.1 之說明） |
| 12 | 溯源、§8.2.1、§8.2.2、無造值 | PASS | 溯源：`SWE1-HVAC-025-01`／`-02`／`-026` 三者於 037 逐一存在。§8.2.1：**本包最實質的一項** —— 2.10 之兩樣內容具名且未驗（§3）。§8.2.2：三個 leaf 各為單一行為，壓力測試無爭議。造值：`when configured` 未定義所指設定項，**不寫入任何配置步驟** |
| 13 | Design Method 於 procedure 定案後指派 | PASS | 三條皆 `功能測試` —— 無狀態遷移、無條件表；此判定由 procedure 形狀反推可得（讀取型步驟，無遷移序列） |
| 14 | 四長欄無行尾句點 | PASS | lint `trailing-period` 覆蓋；另查其未覆蓋之 `test_item`：三條逐條確認無行尾句點 |
| 15 | UI 標籤用 `"..."` | PASS | `"MAX DEF"`／`"REAR DEF"` 加引號。**`rear defrost button` 於 -028 刻意不加引號** —— 3.4 之條文寫的是 `the rear defrost button`（**指涉該元件**），非給出其標籤字串；加引號即宣稱那就是螢幕上的字，屬造值 |
| 16 | `specification_reference` 列出所有直接驗證之節 | PASS | -026／-027 列 3 節、-028 列 1 節，**與 PC 之標註逐一對應**（§2.2 之表即其對照）。R-C29 義務一之落實 |
| 17 | 來源 spec 勝過 index export；閾值為 spec 具體值 | PASS | 三條之條文一律讀 `section_fulltext.tsv`；**另讀 2.10 之全文**以判 -027 之邊界（§3）。本批無數值閾值 |

**15 PASS、2 N/A。**

---

## 9. 未寫回 workbook

依 29 §6 第 7 項，**未寫回**。`output/` 仍為 2 檔，`write_back.py` 未執行，
`DELIVERY.sha256` 之 `produced` 類 ENTRY 未增（新增者為
`folder-attachment` 類之 ENTRY 003，與寫回無關）。

---

## 10. 進度

| | 數 |
|---|---|
| 驗證單位（037 Functional Requirement） | 403 |
| 已生成 | **28**（pilot 14 ＋ Tri-Mode Climate 14） |
| 待覆核（批次 2 之內容） | 14 |
| 未開始 | 375 |

`Tri-Mode Climate` 為**第一個全數生成完畢之 Test Set**（15 組中之第 3 組）。

---

## 11. 「本包是否仍有該驗而未驗者」

依 **R-C30**，以下凡陰性陳述皆附其搜尋範圍。

1. **`-028` 之 `when configured` 未解。** 條文寫「when configured, the rear
   defrost button will not appear when not present」，其中 `when configured`
   所指之設定項，於 3.4 全文無定義。
   **搜尋範圍**：根目錄 `features/comfort/data/section_fulltext.tsv`（129 節
   全文），pattern `configured` —— **命中 3 處**，無一定義該設定項：

   | 節 | 用法 |
   |---|---|
   | 3.4 | `when **configured**, the rear defrost button will not appear` |
   | 6.3 | `**configured** with a non-foldable secondary lower screen` |
   | 11.11 | `**configured** with hard buttons for comfort controls` |

   **另兩處皆為 `configured with X` 之形式，即「配備 X」。** 3.4 之
   `when configured` **無受詞**，故無法以同一讀法還原。我未寫入任何配置
   步驟（§8.4.1），但**也沒有把這件事登為 anomaly**。若分析層認為該詞
   實質改變適用條件，須另裁。
2. **`-027` 之 `not available` 未定義其可觀察形態。** 3.3 只說 available，
   未說不可用時長什麼樣；2.10 說 greyed out 但屬他節。故 ER 停在
   `are not available`，**其判定實際仰賴測試員對「不可用」之理解**。
   這是我在本批裡最不滿意的一行，但寫得更具體就會踩進 2.10。
3. **`spec-ref` 之多節格式尚未經寫回驗證。** N 欄將出現三段以 `; ` 分隔、
   各帶完整 stem 之長字串（約 240 字元）。**寫回未執行，故其於儲存格內之
   呈現未實測** —— 與 A-CF16 之列高同一類問題，且此欄更長。
   建議寫回時一併量測，本包未做。
4. **第十／十一軸之適用範圍 —— 已全掃，結果非陰性。**
   初稿此項我寫「未掃」。**依 R-C30 要載明範圍時，才發現該掃而未掃**，
   故補掃並改寫此項 —— 條文要求留痕跡，留痕跡的動作本身把漏掉的事逼出來了。

   **搜尋範圍**：根目錄 `features/comfort/data/section_fulltext.tsv`
   全 129 節之 `full_text`，pattern `rear defrost`／`soft top`（不分大小寫）。

   | 軸 | 命中節數 | 節（leaf 數） |
   |---|---|---|
   | 第十軸 rear defrost | **8 節** | 2.9(4)、2.10(6)、**3.2(8)**、**3.4(1)**、16.4(1)、16.8(12)、16.9(2)、16.10(8) |
   | 第十一軸 soft top | **1 節** | **3.4(1)** —— 僅此一處 |

   **第十軸之影響遠大於本批**：`2.9`／`2.10` 屬 `Climate Modes`，
   `16.4`／`16.8`／`16.9`／`16.10` 屬 EMEA ICS 章，合計 **33 個 leaf**
   將來可能需要此軸。本包只把它立起來，**未逐節判定其是否確為配置條件**
   （提及 rear defrost ≠ 需要 rear defrost 有無之 PC）。

   **第十一軸則相反：全語料僅 3.4 一處。** 它是為一個 leaf 立的軸，
   這件事本身值得記錄 —— 若日後無第二處，該軸將永遠只有一個使用者。
5. **`§5.1` 禁用動詞仍無 gate。** 上繳 18 §11 第 1 項已建議，本包未加
   （29 §6 未授權）。本批 3 條之動詞是我手查的，第三次了。

---

## 12. 建議 commit message（git 未執行）

```
feat(comfort): complete Tri-Mode Climate — 14/14 leaves

- add R-C29 (a pre_condition's section marker points at the fact's source)
  and R-C30 (a search-based claim must state its scope) to RULINGS
- profile 3.2: tenth axis (rear defrost presence) and eleventh (soft top
  body), both sourced to 3.4, with the illustration-not-enumeration limit
- generate 3.3 (2) and 3.4 (1), tc_id -026..-028; cross-section
  pre_conditions cite 3.2 and 3.4 and both join specification_reference
- spec-ref gates re-judged for multi-section references, reverse-verified
- json-key-coverage extended to the doc layer, whitelist 8 -> 14
- DELIVERY: type column, ENTRY 003 (folder-attachment)
- RUNBOOK: the A-CF-XX convention for illustrating an anomaly id
- lint 35/35 PASS, 0 findings across 28 TCs
```

---

## 13. 待分析層

**批次 2 之 14 條內容覆核**（29 §6 註明另包）。
另 §11 第 1、2、4 項為我判斷不足以自決者，列此待裁。
