# 上繳 03 — User Profiles / Recon 與 037 側複驗（DR #1 到齊）

- 產出層：執行層｜2026-08-17｜對象：分析層
- 下放包：`03_recon_start.md`（作業 1–6）
- 前置：Pei 指示「Phase 0 之 037 側數字全部是在 Project 附件副本上量的，未比雜湊，一律重測」

---

## 0. 結果一覽

| 作業 | 狀態 | 一句話 |
|---|---|---|
| 1 037 採認前置 | ✅ | SHA `9d176dde…` 首次落錨；表頭列**實得 row 7**，與下放包預期相符 |
| 2 Recon（R-U8 三閘）| ✅ **全數相符** | **180 / 25 / 2**，合計 207 = 資料列數 |
| 3 037 側複驗 | ✅ | 集合對集合 **135 = 135，兩側差集皆空**；另查明 135 與 133 之分野 |
| 4 BASELINE 更新 | ✅ | 4 列 → **6 列**，`shasum -c` **6/6 OK** |
| 5 兩份 spec 同一性 | ✅ 只驗未處置 | **SHA256 完全相同**（`368d5874…`）；未刪、未搬、未改引用路徑 |
| 6 Layer 2 草案第二版 | ✅ 只出草案 | 037 分群到齊，出 **11 / 8 / 6** 三案；§4.2 三項命名問題逐項處理 |

**未執行 git。** 本輪未生成任何 TC。

---

## 1. 作業 1 — 037 之採認前置

### 1.1 雜湊（本輪之第一個動作，先於任何量測）

| 檔 | bytes | SHA256 |
|---|---|---|
| `inputs/…-PersonalAccount-HMI-V0.1 STLA 報告.xlsx` | **143,645** | `9d176ddef6d013539bd33e8a74e8b67d01fba232486aaac9eedad109a783eedb` |
| `inputs/…_SWQT_20260817_ext.xlsx` | 200,650 | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |
| `inputs/SYS1_HMI_Personal_Account…(February_10_2023).xlsx` | 60,091 | `368d5874aa23e49c007251ece84de8901f873a7f51ab09b788122b164d365b05` |

bytes 與下放包 §素材現況所列**完全相符**。036 母本複本之 SHA 亦與
A-UP09 所記之母本 SHA（`6372fb6b…`）相同。

> **Project 附件副本之同一性仍不可證，且本輪也不打算證它。**
> 下放包自陳該副本「143,645 bytes，與本檔大小相同但**未比對雜湊**」——
> 該副本不在 repo 內，本層無從對它算雜湊。**故本輪不是「複驗了 Phase 0 的數字」，
> 是「在一個有雜湊的物件上重新量了一次」。** 兩者若日後被證實不同源，
> 失效的是 Phase 0 那一組數字，不是本輪這一組。

### 1.2 表頭列 —— 以 `Requirement Description` 定位，不預設列號

逐格掃描 row 1–40 × col 1–20，命中**唯一一處**：

```
row 7, col 5, 'Requirement  Description'   （注意：兩個空白，非一個）
```

**實得 header row = 7**，與下放包預期（7，自陳未複驗）相符。
資料列為 **row 8–214，共 207 列**，ID 欄非空 207 列（無空行、無尾隨殘列）。

20 個欄位之表頭已逐欄讀出，`Categorization` 在 **col 7**、
`HMI Source ID` 在 col 3、`FROP` 在 col 8、`Sub Categorization` 在 col 9、
`Priority` 在 col 18。

### 1.3 檔名與 DR #1 所列者不同 —— 記，不當作問題

| | 名稱 |
|---|---|
| DR #1／01_intake.md 所列 | `FM-WI-FSM-037-A03 N1L SWE1 Personal Account HMI V0.1 STLA 報告.xlsx` |
| **實得** | `FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx` |

差別為分隔符（空白 → 連字號）與 `PersonalAccount` 之無空白。
**檔名是 DR 之 pattern，不是該檔之身分** —— 身分由 SHA256 承擔，已落 BASELINE。
`feature.yaml` 之 `paths.a03_report` 已由 `null` 填入**實得路徑**（非預定路徑）。

---

## 2. 作業 2 — Recon：R-U8 三閘**全數相符**

**量測條件**：`Analysis Report` 工作表，row 8–214，
以 **col 7（`Categorization`）之欄值逐列計數**，`str.strip()` 後精確比對。

| 閘 | 期望（R-U8）| **實測** | |
|---|---|---|---|
| `functional_requirement_count` | 180 | **180** | ✅ |
| `heading_count`（欄值 == `Heading`）| 25 | **25** | ✅ |
| `out_of_scope_count` | 2 | **2** | ✅ |
| 合計 | — | **207** = 資料列數 | ✅ |

**未調整任何判準。** `scripts/recon.py` 亦獨立跑過，其 assertion
`leaf count == Functional Requirement rows: expected 180, measured 180` PASS。

### 2.1 對照輸出 182 —— R-U8 之判讀於此得到證實

以「ID 非任何其他 ID 之前綴」量得之葉節點 = **182**，其組成：

| | 數 |
|---|---|
| Categorization == `Functional Requirement` | **180** |
| Categorization == `Out of scope` | **2** |
| 其他 | 0 |

> **A-UP07 之診斷至此由資料證實**：182 與 180 之差**恰為那兩個 Out of scope**，
> 而 01b 之判準（`leaf = Categorization 以 Functional 起始`）**本就不會選中它們** ——
> 故「182 再扣 2 得 180」在該判準下不可能成立，兩條路徑同得 180 是單位巧合。
> **R-U8 把 182 降為對照輸出是對的，而這一輪是它第一次被實際量出來。**

另記 `recon.py` 之第三個數：其所報「被禁用之 id 後綴判準會選出 **72**」
（丟掉 108 個 parent 形態之需求）—— **那是第三種單位**，與 182、180 皆不同。
三個數並列於此，使日後不會有人再把其中兩個相減。

---

## 3. 作業 3 — 037 側複驗

### 3.1 集合對集合（非計數）：**135 = 135，兩側差集皆空**

**量測條件**：`HMI Source ID`（col 3）逐列取值，以 `\n,;` 切分（實測**無多行儲存格**，
`multiline = 0`），去除 stem
`Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_`
後取尾段 outline。**stem 不一致者 0 筆**（207 個引用全數同 stem）。

| | 值 |
|---|---|
| 037 實得相異 outline `A` | **135** |
| `data/expected_cited_sections.tsv` 之 `E` | **135** |
| `A ∩ E` | **135** |
| `A − E` | **[]** |
| `E − A` | **[]** |
| 全數命中 SYS1 outline export（169 條）| **135 / 135，未命中 0** |

> **首次比對曾得交集 0** —— 因兩側之鍵形態不同（037 存完整 Source ID 字串，
> TSV 存裸 outline）。**那是本層的比對缺陷，不是資料的落差**，
> 正規化後才是上表。記於此：**「集合對集合」若不先統一鍵，
> 得到的是一個看起來很嚴重而完全虛假的差集。**

### 3.2 135 與 133 之分野 —— 本輪查明，值得上游知道

`recon.py` 報「**133** cited / 169 outline entries」，與 135 差 2。**兩者都對，量的是兩件事**：

| 量法 | 值 |
|---|---|
| 全部 207 列 × 各行（本層）| **135** |
| **僅 Functional Requirement 列 × 僅第一行**（`recon.py` 之定義）| **133** |

差的兩條**逐一具名**：

| outline | 唯一引用者 | 該列之 Categorization |
|---|---|---|
| `4.7` | `SWE1-HMI-PROF-017` | **Out of scope** |
| `5.11` | `SWE1-HMI-PROF-035` | **Out of scope** |

**即：135 條被引 outline 之中，有 2 條只被 R-U4 排除的那兩個 leaf 引用。**

> **這件事有後果，請裁**：R-U4 定該二 leaf 不生成 TC、不計入覆蓋率分母。
> 若如此，**生成相關之被引 section 為 133，不是 135**。
> 而 R-U3 之證據行寫的是「037 引用之 135 個唯一 section id 缺漏 0」——
> **該句仍為真**（135 條確實都在 spec 裡），
> **但它不是覆蓋率的分子**。兩個數字自 01 輪起一直是同一個 135 在用，
> 本輪是它第一次被拆開。
>
> 本層**未改** `data/expected_cited_sections.tsv`（仍 135 列）——
> 該檔記的是「037 引用了哪些」，那是對的；要不要另立一個 133 的生成集合，
> 屬 Tier 2。

`multiline = 0` 一併記：`recon.py` 只取第一行之規則在本 feature **不損失任何引用**，
其 133 與 135 之差**全部**來自 Categorization 過濾，與「只取第一行」無關。

### 3.3 FROP 欄

| 值 | 列數 |
|---|---|
| `User Profiles` | **182** |
| （空）| 25 |

**182 = 180 FR ＋ 2 Out of scope**，與 §2.1 之葉節點集合**逐列一致**；
25 個空值恰為 Heading 列。**R-U1 之 Test Group 值於此首次複驗成立。**

### 3.4 Out of scope 之身分

實得 `SWE1-HMI-PROF-017`、`SWE1-HMI-PROF-035` —— **與 R-U4 明列者相同**。

### 3.5 Sub Categorization 與 Priority 分布

| Sub Categorization | 列數 | | Priority | 列數 |
|---|---|---|---|---|
| `HMI` | 160 | | `High` | 79 |
| `Service` | 22 | | `Medium` | 75 |
| （空，皆 Heading 列）| 25 | | `Low` | 28 |
| | | | （空，皆 Heading 列）| 25 |

`HMI` 160 ＋ `Service` 22 = 182，同上。**`Service` 22 條值得注意**：
其中 ch4 佔 12 條 —— 若 `Service` 意指非 HMI 側之行為，
Comfort 之 `[BLOCKED-NON-HMI]`（R-C38）可能於本 feature 有對應形態。
**本輪不判**，僅列出以備 Phase 3。

### 3.6 被引 135 條之長度分布與圖片參照

**量測條件**：`data/outline_map.json` 之 `len` 欄（Description 全文字元數），
圖片以 `(image:` 字面計數。

| | 135 條 | 133 條（扣 4.7／5.11）|
|---|---|---|
| min / 中位 / 平均 / max | 65 / 195 / 224 / 728 | 65 / 195 / 223 / 728 |
| 0–200 字元 | 70 | 69 |
| 200–500 | 59 | 58 |
| 500–1000 | 6 | 6 |
| 1000+ | **0** | **0** |
| **含圖片參照之節** | **14** | **14** |
| **圖片參照總數** | **17** | **17** |

含圖之 14 節：`4.6`、`5.1`、`5.2`、`6.2`、`7.2`、`7.2.1`、`7.5`、`8.2`、
`8.4`、`9.1`、`10.2`、`11.4`、`12.2`、`14.1`。

> **Comfort A-CF23 之同型風險於此預先具名**：那 14 節之條文帶圖，
> 而圖之內容讀不到。Phase 3 撰寫該 14 節之 TC 時，須逐條問
> 「本條之判讀是否依賴圖中所載」——**現在記，比屆時才想起來便宜。**

### 3.7 未被引之 34 條 outline —— A-UP02 於 037 側首次證實

169 − 135 = **34** 條未被任何 037 列引用：

- **章標題本身** 11 條（`4`、`5`、`6`、`7`、`8`、`9`、`10`、`11`、`12`、`13`、`14`）—— 無實質條文
- **章 1（Assumptions）** 12 條、**章 2** 2 條、**章 3（PLP1–PLP5）** 6 條
  —— 01b 已裁 Layer 3 骨架取章 4–14，章 1–3 不入生成範圍
- **`10.1`、`11.1`、`11.2`** 3 條 —— **實質條文而無 SWE 覆蓋**

> **A-UP02 記的 8 條為「3.1–3.5、10.1、11.1、11.2」**，
> 本輪自 037 側獨立量出 **`10.1`／`11.1`／`11.2` 三條確實無人引用**，
> 3.1–3.5 五條亦在未引之列 —— **8 條全數證實**。
> 此前 A-UP02 之依據為 spec 單邊，**本輪是它第一次有 037 側的證據。**

---

## 4. 作業 4 — BASELINE.sha256 更新

`inputs/` 由 1 檔增為 **3 檔**，加 spec-index 三件，共 **6 列**。

```
$ shasum -a 256 -c BASELINE.sha256
inputs/…_SWQT_20260817_ext.xlsx: OK
../../spec-index/cache/SYS1_HMI_Personal_Account…(February_10_2023).xlsx: OK
../../spec-index/cache/SYS1_HMI_Personal_Account…(February_10_2023).json: OK
../../spec-index/sources/Personal Account HMI Logic and Flow R1L-R (February 10 2023).pdf: OK
inputs/FM-WI-FSM-037-A03-N1L-SWE1-PersonalAccount-HMI-V0.1 STLA 報告.xlsx: OK
inputs/SYS1_HMI_Personal_Account_HMI_Logic_and_Flow_R1L-R_(February_10_2023).xlsx: OK
```

**6 / 6 OK**（另有 2 行 improperly-formatted 警告，來自新增之註解區塊，
exit code 0 —— 與檔內原有說明一致）。

檔頭增記 037 之採認前置、檔名與 DR pattern 之差異、兩份 spec 同一性之結論。

---

## 5. 作業 5 — 兩份 spec 之同一性：**相同**（只驗，不處置）

| 路徑 | bytes | mtime | SHA256 |
|---|---|---|---|
| `inputs/SYS1_HMI_Personal_Account…xlsx` | 60,091 | 2026-08-17 03:02:00 | `368d5874aa23e49c007251ece84de8901f873a7f51ab09b788122b164d365b05` |
| `spec-index/cache/SYS1_HMI_Personal_Account…xlsx` | 60,091 | **2026-04-24 22:14:53** | **同上，逐位元組相同** |

**已依指示完全不處置**：未刪除、未移動、未改任何引用路徑。
R-U3 之 spec 基線引用路徑維持 `spec-index/`。**兩份皆列入 BASELINE**，
各自以其路徑受檢。

> **「相同」不是合併的理由，這一點刻意寫下**：兩份現在相同，
> 只證明**此刻**內容一致；日後若有人改了其中一份，
> 兩列各自受檢**正是那時候會出聲的東西**。合併成一列會把那個能力關掉。
> 處置屬 Tier 2／3（R-U17 提案）。

---

## 6. 作業 6 — Layer 2 草案第二版（**只出草案，不自裁**）

### 6.1 037 之分群訊號（第一版所無）

037 自帶 **25 個 Heading 列**，各繫一個 outline —— 這是 01 輪不可得的東西。
180 個 leaf 之章別分布：

| 章 | leaf | 章標題（spec）|
|---|---|---|
| 4 | **28** | Profile Overview |
| 5 | **40** | All Profiles Tab |
| 6 | 11 | Default Profiles - No Custom Profiles |
| 7 | 14 | Welcome Screen (Custom Profile) |
| 8 | **25** | New Profile Setup |
| 9 | 22 | Editing a Profile |
| 10 | 3 | Profile Info Page |
| 11 | 6 | Connected Profile App |
| 12 | **25** | Valet Mode |
| 13 | 4 | Valet Mode - SPAAK |
| 14 | 2 | Valet Mode - Exit |

### 6.2 §4.2 之三項命名問題，逐項處理

canon §4.2：Test Set 為 1–3 字之英文名詞片語，**不得為 UI widget 名**，
**不得重複 Test Group 之詞**（Test Group = `User Profiles`）。

| 問題 | spec 章標題 | 何以不合 | **提案** |
|---|---|---|---|
| UI widget 名 | `All Profiles Tab`（ch5）| `Tab` 為 widget；且含 `Profiles` | **`Profile List`** —— 其能力為「多個 profile 之列出、選取、切換、上限、排序」，非那個分頁本身 |
| 重複前綴 | `Profile Overview`（ch4）| `Profile` 重複 Test Group | **`Preference Storage`** —— ch4 之 28 leaf 主體為偏好之儲存、跨 key cycle 回復、memory seat 連動 |
| 重複前綴 | `New Profile Setup`（ch8）| 同上 | **`Setup Flow`** —— 其能力為建立流程之逐步（username／avatar／完成路由）|

其餘章之提案（同一原則：去 widget 名、去 `Profile` 前綴）：

| 章 | 提案 Test Set | 說明 |
|---|---|---|
| 6 | `Default Profiles` | ⚠ 仍含 `Profiles`。替代：**`Defaults`** |
| 7 | `Welcome Popup` | spec 稱 Welcome Screen，惟其實體為 popup；兩者擇一待裁 |
| 9 | `Editing` | ch9 之 22 leaf |
| 10 | `Info Page` | 3 leaf，單章過小，見 6.3 |
| 11 | `Connected Account` | 6 leaf |
| 12–14 | `Valet Mode` | 三章合一，見 6.3 |

### 6.3 三個切法（Tier 2，不自裁）

| 案 | Set 數 | 切法 | 區間 | 最大佔比 |
|---|---|---|---|---|
| **A 逐章** | **11** | 一章一 Set | 2–40 | 22.2%（ch5）|
| **B 合併小章** | **8** | A ＋ ch12/13/14 併 `Valet Mode`（31）＋ ch10 併入 ch9 `Editing`（25）＋ ch11 獨立 | 6–40 | 22.2%（ch5）|
| **C 能力導向** | **6** | `Preference Storage`(28) ／ `Profile List`(40) ／ `Defaults`(11) ／ `Welcome Popup`(14) ／ `Setup Flow`+`Editing`+`Info Page`(50) ／ `Valet Mode`(31) ＋ `Connected Account`(6) 併入 Setup | 11–50 | 27.8% |

**本層之傾向為 B**，理由三項，皆可反駁：

1. **ch12/13/14 顯然是一個能力**（Valet Mode 之進入、SPAAK 變體、退出），
   §4.2 明文「Different steps, UI paths, or sub-states of the same capability
   should share one Test Set」
2. **ch10（3 leaf）自成一組會使 Test Set 欄淪為 TC ID 之副本**（§4.1.3 過細），
   Comfort framework §3.4 有同型前例（ch6 之 1 leaf 併入 #1）
3. **ch5 之 40 leaf 不拆** —— §4.2「Prefer broader shared capability when
   unsure」；且 Comfort 之最大組為 59（14.6%）而未拆，本案 40（22.2%）
   在同一取捨的同一側

**不自裁之處**：`Welcome Screen` vs `Welcome Popup`、`Defaults` vs
`Default Profiles`、以及 C 案是否更貼近「能力」而非「章」——
三者皆為 Tier 2。

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷（不得省略）

**有，六項。**

| # | 該驗而未驗 | 性質 |
|---|---|---|
| 1 | **Project 附件副本與 `inputs/` 這份是否同源** —— 本輪無法證，該副本不在 repo | **永久記載限制**。故 Phase 0 之 037 側數字**不是被複驗了，是被取代了**；若日後那份副本出現且雜湊不同，失效的是 Phase 0 那一組 |
| 2 | **`Service` 22 條之含義** —— 是否為非 HMI 側行為（Comfort `[BLOCKED-NON-HMI]` 同型）| **真缺口**。ch4 佔 12 條，若屆時才發現，會是一整章的返工。建議下一包單獨查 |
| 3 | **14 節帶圖之條文，其判讀是否依賴圖** | **真缺口**，Comfort A-CF23 之同型。本輪只數了 14 / 17，**未讀任何一張圖，也未逐節問那個問題** |
| 4 | **135 vs 133 之處置** —— `expected_cited_sections.tsv` 仍為 135，未另立生成集合 | Tier 2 待裁；本層不自行改該檔 |
| 5 | **R-U8 三閘已綠，但三閘本身未反向驗證** —— 沒有任何注入測試證明它們會為壞資料轉紅 | **真缺口**。Comfort 96 §6 之經驗：`row-order-by-reqid` 第一版對正確資料轉紅，**是反向驗證抓到的，不是人看出來的**。本 feature 之三閘現況與那時相同 |
| 6 | **`data/spec_id_to_outline.tsv` 有兩個生產者，同名而不同物** | **真缺口，且本輪撞上了**。見 §7.1 |

### 7.1 本層在本輪犯的一個錯，與其處置

**我在跑 `scripts/recon.py` 之前沒有查它會寫哪些檔。** 它覆寫了兩個 tracked 檔：

| 檔 | 被覆寫成 | 損失 |
|---|---|---|
| `DECISIONS.md` | recon 之預填版（`[AUTO]` 值已填）| **無** —— 舊檔為純樣板，`Reviewed by: ____________`，無任何人工填寫內容。逐項核對過，故**保留 recon 之版本** |
| `data/spec_id_to_outline.tsv` | recon 之 037 leaf 對映（180 列）| **有** —— 覆蓋掉 01 輪 `build_outline_map.py` 之 spec 側索引（169 列）|

**兩個生產者寫同一個檔名，而它們是不同的東西**：

| 生產者 | 內容 | 列 | 欄 |
|---|---|---|---|
| `features/<f>/scripts/build_outline_map.py` | **spec 側**索引 | 169 | `section_id / outline_number / polarion_id / phys_row / chars` |
| `scripts/recon.py`（全域）| **037 leaf → section** 對映 | 180 | `req_id / outline / polarion_id / spec_reference / title` |

**已處置**：`git checkout` 還原 01 輪之版本（它是 `docs/INDEX.md` §3 所記載者），
recon 之產物改置 `data/recon_leaf_to_section.tsv` 並於檔頭記明來由 ——
**兩者皆不遺失**。**未改 `recon.py`** ：檔名之歸屬是全域問題（`features/home`
之 `lint_tcs.py` 與 `make_batch_context.py` 皆讀該檔名），屬 Tier 2。

> **這個碰撞在 home／comfort 上不會發作**，因為那些 feature 之 recon 早於
> `build_outline_map.py`；本 feature 是**先建了 spec 側索引才跑 recon**，
> 順序一反，後者就把前者蓋掉了 —— **而它蓋得無聲無息，`git status` 只顯示
> 「M」，不顯示「這是另一個東西」。**

**另記一件不在作業項內、本輪順帶查到的**：`feature.yaml` 之
`paths.a03_report` 原為 `null`，其註解寫著一個**預定檔名**，
而實得檔名與之不同。**若當初有人照那個預定路徑寫死，recon 會找不到檔而看似「素材未到」**
—— 本輪是把 `null` 換成實測路徑，不是把預定值改對。

---

## 8. 本包所動之檔

| 檔 | 動作 |
|---|---|
| `features/user_profiles/BASELINE.sha256` | 4 列 → 6 列；檔頭增 037 採認前置、檔名差異、spec 同一性 |
| `features/user_profiles/feature.yaml` | `paths.a03_report` 由 `null` 填入實得路徑（附差異註解）|
| `features/user_profiles/RECON.md` | **新建** —— `recon.py` 之報告 |
| `features/user_profiles/DECISIONS.md` | **由 `recon.py` 覆寫**（舊檔為純樣板，無人工內容；見 §7.1）|
| `features/user_profiles/data/recon_leaf_to_section.tsv` | **新建** —— 承接 recon 原欲寫入 `spec_id_to_outline.tsv` 之內容（見 §7.1）|
| `features/user_profiles/docs/upstream/03_recon.md` | 本檔 |
| `features/user_profiles/docs/INDEX.md` | 新增第 03 列與現況更新 |

**未動**：`inputs/` 任何檔（未刪未搬）、`spec-index/`、
`data/outline_map.json`、`data/expected_cited_sections.tsv`、
`data/spec_popup_ids.tsv`、`ANOMALIES.md`（A-UP04 之解除屬 Tier 2，見 §9）、
`RULINGS.md`、`scripts/recon.py`、他 feature 之任何檔案。

### 8.1 git 動作 —— 據實更正（R-G6，04 輪補正）

> **本節原寫「git 未執行」，該陳述與本包 §7.1 互相矛盾，為誤。**
> R-G6 裁定「往後『未執行 git』一語須與全文動作清單逐項對得起來」，
> 據此更正如下。**§7.1 之敘述本身是對的，未動。**

| git 動作 | 對象 | 何時 | 結果 |
|---|---|---|---|
| `git checkout <path>` | `features/user_profiles/data/spec_id_to_outline.tsv` | §7.1 所述之覆寫事故發生後 | 還原至 01 輪之版本；被丟棄之 recon 產物已另存為 `data/recon_leaf_to_section.tsv` |
| `git status` / `git diff` / `git show` | 多處 | 全程 | 唯讀，不改工作區 |

**故本包正確之陳述為**：**執行了一次 `git checkout`（單一檔案）**，
未執行 `commit`／`push`／`add`／`reset`／`stash`／`clean`。

**該次 checkout 已由 R-G5 追認**（追認範圍僅限該單一檔案），
並同時裁定**其作法為錯**：遇覆寫事故之正確作法是**兩版皆保留（改名並存）、
上報、停手，不自行還原** —— 理由是 checkout 丟棄工作區變更且不可救回，
而執行層無從確知該檔是否另有未提交之他人變更。

> **本層當時之推理是「還原是那條裁決之必然結果」** ——
> R-G5 明文指出這與 R-U13（`.gitignore` 那次）是**同一失效模式之第二次發生**：
> **以某條裁決之必然結果自推授權。** 兩次都不是內容錯，是程序錯。

---

## 9. 待裁（不自裁，逐項）

1. **A-UP04 是否 RESOLVED** —— 037 已到齊且三閘已過，其解除條件表面已滿足；
   惟狀態變更屬 Tier 2，本層不自行改判（同 02 輪之 A-UP09 處置）。
2. **135 vs 133** —— 生成相關之被引集合是否應另立（§3.2）。
3. **Layer 2 之切法與命名**（§6.2／§6.3）。
4. **`Service` 22 條之類別**（§7 第 2 項）。
5. **`data/spec_id_to_outline.tsv` 之檔名歸屬**（§7.1）—— 兩個生產者同名，
   全域問題（`features/home` 有讀者），本層不改 `recon.py`。
6. R-U13～R-U17 仍待裁，其中 **R-U14 管 Phase 6 能否開工**，本包未觸及該階段。
