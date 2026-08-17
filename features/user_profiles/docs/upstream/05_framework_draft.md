# 上繳 05 — User Profiles / 跨 feature 掃描、抽圖能力與 framework 草案

- 產出層：執行層｜2026-08-17｜對象：分析層
- 下放包：`05a_rulings.md`（R-U21～R-U24、R-G7）＋ `05b_tasks.md`（作業 1–6）

---

## 0. 結果一覽

| 作業 | 狀態 | 一句話 |
|---|---|---|
| 1 條文入庫 | ✅ | 五條逐字；R-G7 併全域段 |
| 2 跨 feature 掃描（唯讀）| ✅ | **無污染**。comfort 為 recon 形態**而非被污染**；sxm／amfm／projection **無此檔** |
| 3 home 實跑 | ⚠ **原定作法做不到** | home 之 `inputs/` 不存在 → 改以「餵兩形態給三個讀者」，**危害已由推導變為觀察** |
| 4 抽圖能力（R-U23）| ✅ **6 節中 5 節改判** | 圖不在 xlsx 而在 PDF；**8.2 由「完全依賴」改為「不依賴」** |
| 5 PLP 表（R-U22）| ✅ **可讀** | 逐項清單全抽得出 → `PROF-001-01` 正常生成；A-UP02 性質重估 |
| 6 framework 草案 | ✅ | `framework.md` 落檔，每個數字複驗相符 |

**未執行任何會改變 repo 狀態之 git**；唯讀 git 亦**未使用**（本輪一次都沒跑）。見 §8。

---

## 1. 作業 2 — 跨 feature 掃描（唯讀）：**無污染**

**量測條件**：讀 `features/<f>/data/spec_id_to_outline.tsv` 之欄名、
資料列數、第一欄前 5 值，並以 home `make_batch_context` 之
`CHAPTER_RE = ^([A-Z]{2,4})` 對第一欄逐列比對命中率。**全程唯讀。**

| feature | 欄名 | 資料列 | 形態 | 第一欄命中 `^[A-Z]{2,4}` |
|---|---|---|---|---|
| **comfort** | `req_id / outline / polarion_id / spec_reference / title` | **403** | **recon 形態** | **403 / 403 → `SWE`** |
| sxm | — | — | **檔不存在** | — |
| amfm | — | — | **檔不存在**（其用 `data/stla_to_cfts.tsv`）| — |
| projection | — | — | **檔不存在** | — |
| home | `spec_id / outline / desc` | 104 | build_outline_map 形態 | 76 / 104 → `HSD` |
| user_profiles | `section_id / outline_number / polarion_id / phys_row / chars` | 169 | build_outline_map 形態 | 0 / 169 |

### 1.1 comfort **不是被污染** —— 兩項證據

1. **comfort 沒有 `build_outline_map.py`**（`ls features/comfort/scripts/ | grep -i outline` 無命中）。
   該檔名在 comfort 從來就只有一個生產者。
2. **comfort 自己的四份文件一致記載它為 recon 的表**：

| 檔 | 記載 |
|---|---|
| `RUNBOOK.md:27` | outline map：`data/spec_id_to_outline.tsv`（**403 列**，追蹤入版控）|
| `docs/INDEX.md:111` | **403 leaf → SR24 outline 之查表** |
| `RULINGS.md:1195` | 403 列 + 表頭 |
| `DECISIONS.md:18` | map at data/spec_id_to_outline.tsv |

**記載與內容相符，且無任何讀者。** 故 04 包 §7.2 之危害**在 comfort 上不成立** ——
危害的落點是 home 那三個讀者，而它們只讀 `features/home/data/`。

### 1.2 惟 R-G4 給 comfort 留下一個新後果，須上報

R-G4 生效後，**comfort 若重跑 recon，產物會落到 `recon_leaf_to_section.tsv`**，
而現存的 `spec_id_to_outline.tsv` 會留著不再更新 —— **變成孤兒**，
且 comfort 的四份文件全部指向舊名。

> **這不是本輪造成的錯，是 R-G4 這條規則的必然連帶。**
> 處置屬 Tier 2：或改 comfort 之四份記載、或為 comfort 保留舊名、
> 或裁定 comfort 不再重跑 recon。**本層不自裁，未動 comfort 任何檔。**

### 1.3 一個 04 輪漏掉的讀者

04 包 §7.1 查了兩個讀者（`lint_tcs.py`、`make_batch_context.py`），
R-G4 條文也只點名這兩個。**實際有第三個**：

```
features/home/scripts/extract_exemplars.py:97
    outline_to_chapter = load_outline_to_chapter(out / "spec_id_to_outline.tsv")
```

其用法與 `make_batch_context` 相同（`load_outline_to_chapter` → `chapter_of`），
**故受同一危害**。04 輪之「兩個讀者」是漏數，於此更正。

---

## 2. 作業 3 — home 實跑：**原定作法做不到，改以更貼近危害落點者**

### 2.1 為什麼做不到

依 05b 複製 `features/home` 全樹至 tempfile 後跑 `recon.py`：

```
input not found: inputs/FM-WI-FSM-036*.xlsx under …/features/home
```

**`features/home/inputs/` 不存在** —— 這正是 **R-G2 條文自身所記載的事實**：

> 實測（2026-08-17）：features/home/ 已無 inputs/ 亦無 output/ ……
> 前例：2026-08-13 amfm／home／media／projection 之 inputs/ 全數清空，
> git 無從還原（從未被追蹤）。

**故 04 包 §10 第 1 項所提之「對 home 實跑 recon」，其不可行不是授權問題，
是素材問題。** 那一項當時被列為「真缺口」，本輪查明它**在現況下無法清除**。

### 2.2 改以直接餵兩種形態給 home 之讀者

**危害的落點在讀者端，不在 recon 端** —— recon 只是把檔寫成那個形狀。
故本層直接以 home 之三個讀者函式為對象，用 home **自己的 104 條 outline**
造一份 recon 形態（欄序照 `recon.py` 之輸出），比較兩者。

**含 R-G7 之兩個對照向。**

| 向 | `lint_tcs.load_outlines` | `make_batch_context` 之 chapter 集合 | `chapter_of` 抽樣 |
|---|---|---|---|
| **對照 1：原檔逐字（什麼都沒做）** | 104 | **6 種**：`BSP HS HSD HSS SNS SW` | `4.1→HSD`、`10.1→?`、`11.5→BSP` |
| **對照 2：原檔重寫一次，不改內容** | 104 | **6 種**（同上）| 同上 |
| **注入：recon 形態（同一批 outline）** | 104 | **1 種：`SWE`** | `4.1→SWE`、`10.1→SWE`、`11.5→SWE` |

**兩個對照向逐項一致**（R-G7 滿足）。

> **04 包 §7.2 之危害，於此由推導變為觀察**：
> `chapter_of` 對每一個 outline 都回 `'SWE'`，chapter 集合由 6 種**退化為 1 種**。
> **不是崩潰，是一個安靜的錯答案** —— 正如當時所推導。

### 2.3 一項須據實講明的界線

`lint_tcs.load_outlines` 在本實驗中**兩側皆為 104，沒有差異** ——
因為我為控制變因，**只改欄形態而用了同一批 outline**。

04 包 §7.2 曾寫「其列集會由全 spec outline 變成被引之子集，
沒被引用的 outline 會開始 lint FAIL」—— **那一半仍是推導，本輪未觀察到**，
要觀察它須用真正的 recon 產物（即真實的被引子集），而那需要 home 的 037，
即 §2.1 之同一個缺口。**這一點不能算已驗。**

---

## 3. 作業 4／5 之共同前提：**圖不在 xlsx，在 PDF**

**量測條件**：以 `zipfile` 讀兩份 xlsx 之 member 清單。

| 檔 | zip members | `xl/media/` | drawing |
|---|---|---|---|
| spec `SYS1_HMI_Personal_Account…xlsx` | 37 | **0** | **0** |
| 037 `FM-WI-FSM-037-A03…xlsx` | 59 | 1（`image1.jpeg`）| 4 |

**spec xlsx 一張內嵌圖都沒有。** `(image: %E5%9C%96%E7%89%87_1102096521.png)`
之 `%E5%9C%96%E7%89%87` URL-decode 即「圖片」—— 那是 **SYS1 export 產生的
文字標記**，指向 export 過程留在別處的檔。

**而 BASELINE 內的 PDF 有圖**：

| | 值 |
|---|---|
| `Personal Account HMI Logic and Flow R1L-R (February 10 2023).pdf` | 867,742 bytes，**21 頁** |
| `/Image` XObject | **174** |
| `/Font` | 47 → **有文字層** |
| 可用工具 | `pdftotext`／`pdfimages`／PyMuPDF **皆可用** |

> **與 Comfort A-CF23 的結論方向相反，須講明**：
> Comfort 是「**檔在手上而我方讀不到那一頁**」（缺讀取能力）。
> 本 feature 是「**xlsx 裡沒有圖，而圖在同一批素材的另一份檔裡，且讀得到**」——
> **不是缺讀取能力，是找錯檔案。** 04 輪只問了 xlsx，沒問 PDF。

---

## 4. 作業 4 — R-U23：**6 節中 5 節改判**

**方法**：以 PyMuPDF 於 PDF 全文搜條款標籤定位頁，讀該頁文字層。
關鍵發現：**這些「圖」多為向量圖形＋文字標籤**，`get_text()` 抽得出來。

### 4.1 04 包 §6 分類之前後對照

| 節 | **04 包（舊）** | **05 輪（新）** | 依據 |
|---|---|---|---|
| `8.2` | **完全依賴** | **不依賴** | p12 之流程圖，步驟／PU id／按鈕文字／分支全數可讀（§4.2）|
| `6.2` | 部分依賴 | **不依賴** | p9 之圖可讀：`PU0575`（小版）／`PU0576`（大版）welcome popup 之例，及 `Enter Username (PU0585)` → `Choose Avatar (PU0586)` 之流程 |
| `9.1` | 部分依賴 | **不依賴** | **Table EDPR1 之十個列項與順序全數可讀**（§4.3）|
| `10.2` | 部分依賴 | **不依賴** | p16 之 `Category / Title / Description` 三欄表可讀（Screen Customization／Apps／Media／Audio…）|
| `11.4` | 部分依賴 | **維持部分依賴** | table CPA2 之列項部分可讀（`Connected FCA Account`／`Local Profile`／`Personalization`／`App Store Download`／`Marketplace`／`Connected Navigation`…），惟其**逐列對應關係**於文字層無法確定 |
| `4.6` | 部分依賴 | **維持部分依賴**，**理由改變** | 見 §4.4 |

**改判後之分布**：

| 分類 | 04 包 | **05 輪** |
|---|---|---|
| 不依賴 | 8 | **12** |
| 部分依賴 | 5 | **2** |
| **完全依賴** | **1** | **0** |

**DR 候選歸零。** 04 包 §6.1 曾把 `8.2` 列為 DR 候選 —— **本輪撤回該建議**。

### 4.2 `8.2` 之流程圖，逐項抽出

```
Start: Initiating a New Profile from "All Profiles" Tab
  → Step 2: Enter User Name (PU0585)        按鈕 Continue
  → Step 3: Choose Category and Avatar (PU0586)   按鈕 Save & Continue
  → Step 4: (PU0612) "Some of your preferences have changed from default…
             Would you like to keep these changes?"
             按鈕 [Yes, Keep Changes] [No, Restore Defaults]
  → 分支 ****Is CPA Present
       是 → End: 依請求處理偏好，開始 Connected Personal Account login
       否 → End: 依請求處理偏好，開始 Tutorials
  Cancel/"X" → "Are you sure you want to cancel your Profile Setup?" (PU0587)
       Yes/Cancel → End: 回設定前之畫面，新 Profile 不儲存
       No/Go Back → 回前一畫面繼續設定
****NEWPR0.) R1 High Only: CPA 不啟動，step 4 後直接進 Tutorials
```

**procedure 與 ER 皆寫得出來。** 該節之判讀不再缺任何東西。

### 4.3 `9.1` 之 Table EDPR1，順序完整

```
"Resume Setup" (only if not complete) / "Edit Name" / "Edit Avatar" /
****"Stellantis Account" / "Memory Seat" (If applicable) / "Welcome Pop Up" /
"Delete Profile" / "What is linked to my Profile?" / "Tutorials" / "More Settings"
```

PDF 之條文另比 xlsx **多出一句**：「there will be a circled number 1 next to
Resume Tutorials. It will be removed as a line item once the user has completed
setup assistant」。**xlsx 之 Description 欄沒有這一句。**

> **這件事本身值得記**：`outline_map.json` 取自 xlsx export，
> 而 **PDF 之條文比 export 完整**。本輪只在這一節撞見，**未逐節比對兩者之差**
> —— 列為 §7 之未驗項。

### 4.4 `4.6` 維持部分依賴，**而理由比原來強**

p6 之圖側文字為：

> Profile Icon (while on Home Screen) - Default Profile Icon /
> Profile Status Bar Icon Variations / **Avatars/icons are placeholders for
> final graphics**

**最後一句是 spec 自己說的**：那些圖示是**佔位圖，不是最終圖形**。

> 故「ER 只寫『圖示與登入之 profile 相符』、不寫是哪個圖示」——
> **不再只是因為我方讀不到，是因為 spec 本身就還沒定案。**
> 這比 04 包當時的理由強：那時是能力限制，現在是**條文自身之狀態**。

---

## 5. 作業 5 — R-U22：PLP 表**可讀**

**量測條件**：xlsx 之 `3.1`–`3.5` Description 欄逐節讀，再以 PyMuPDF 讀 PDF p5。

### 5.1 xlsx 側：**只有標題，內容全在圖裡**

| 節 | 字元 | 內容 |
|---|---|---|
| `3.1` | 86 | `PLP1.) Profile Linked Preferences -Radio (image: …)` |
| `3.2` | 70 | `PLP2.) … Cluster (image: image3.png)` |
| `3.3` | 81 | `PLP3.) … Memory Seat Module (image: image4.png)` |
| `3.4` | 71 | `PLP4.) … SiriusXM (image: image5.png)` |
| `3.5` | 73 | `PLP5.) … Navigation (image: image6.png)` |

**五節皆含 `(image:` 標記，皆只有一行標題。** 若只讀 xlsx，結論會是「不可讀」。

### 5.2 PDF 側（p5，11 張點陣圖）：**逐項清單完整可讀**

**PLP1 — Radio**（另有 `Low` / `High` 兩欄，即機型軸）：

> Home Screens（customized, added, and deleted）／Menu Bar order／Mixed Presets／
> Last screen on startup／Last Mode Table behaviors／App Drawer Favorites（and
> Favorites order）／Status Bar Customization／Bluetooth Phone Favorites (1 and 2)／
> Notification settings/preferences／Profile preferences（in the Edit Profile
> section）／Head Unit Settings（See HMI Settings List - My Profile section）／
> Apps（unique credentials per Profile）／Ambient Lighting／Virtual Concert Hall
> Selection（**Popup PU1497**）／Creep Selection（**Popup PU1511**）

**PLP2 — Cluster**：Cluster Screen setup／Last Screen／Speed Warning／
Speed Units／Cluster Home screen／Cluster Layouts／HUD settings

**PLP4 — SiriusXM**：SiriusXM 360L Listener Profile (last known)

**PLP5 — Navigation**：Nav Settings／Recent Destinations／Saved destinations
（三者皆 `determined by TomTom`）

**PLP3 — Memory Seat Module**：其標題在 xlsx，**惟本輪於 p5 之文字層未定位到
其列項** —— 未確認，列為 §7 之未驗項。

### 5.3 據此之兩個結論

**一、`PROF-001-01` 正常生成**（R-U22 之「可讀」分支）：
`specification_reference` 併列 `4.1` 與 `3.1`–`3.5`，偏好清單以上列原文為據，
**不列舉未載之項**（§8.4.1）。**PLP3 之列項未確認前，該部分不寫。**

**二、A-UP02 之性質重估** —— R-U22 明文要求：

> **其為「spec 有而 SWE 未涵蓋」，非「內容不存在」。**

`3.1`–`3.5` **有內容且可讀**，只是 037 沒有為它們產出 leaf。
**這改變了 DR #3 的性質**：不是索取缺件，是上游之覆蓋缺口
（037 未對已存在之條文產出需求）—— 形態同 Comfort **R-C16**。

---

## 6. 一個順帶查到、且會改動 DR 範圍的事

**`spec_popup_ids.tsv` 的 20 個 PU id 少算了。**

**量測條件**：以 `PU[\s_]?(\d{3,4})` 掃 PDF 全 21 頁之文字層，正規化為 `PU%04d`。

| | 數 |
|---|---|
| PDF 全文之相異 PU id | **32** |
| `data/spec_popup_ids.tsv`（自 xlsx Description 欄掃得）| 20 |
| **只出現在圖裡者** | **12** |

那 12 個：`PU0575`、`PU0576`、`PU0577`、`PU0578`、`PU0579`、`PU0586`、
`PU0587`、`PU0609`、`PU0612`、`PU0614`、`PU1497`、`PU1511`。

**且 `PU1087` 與 `PU1088` 在 PDF 中確實存在**（p6）：

> `PU1087` is displayed when users confirm Setting restore to default by
> pressing Yes in pop-up `PU_0118`. `PU1088` is displayed when settings have
> been successfully restored to default.

> **這對 DR #4 有影響，請裁**：DR #4 索取的是「載有 PU1087／PU1088 之
> **Pop Up List** 版本」。本輪查明 **spec 自己已說明這兩個 popup 何時顯示**
> —— 缺的是 Pop Up List 裡那兩列（popup 之**內文**），
> **不是它們的觸發條件**。R-U15 之阻斷範圍是否應據此收窄，屬 Tier 2。
>
> **另請裁**：`spec_popup_ids.tsv` 是否應由 20 擴為 32。
> 本層**未改該檔** —— 它記的是「xlsx Description 欄掃得者」，那個記載正確；
> 要不要換成「spec 全文（含圖）掃得者」是另一個決定。

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷（不得省略）

**有，六項。**

| # | 該驗而未驗 | 性質 |
|---|---|---|
| 1 | **`lint_tcs` 那一半危害仍是推導** —— 本輪只控制欄形態，未用真實的被引子集（§2.3）| **真缺口，且與 §2.1 同源**：要驗它須有 home 之 037，而 home 的 `inputs/` 已清空 |
| 2 | **PDF 之條文比 xlsx export 完整**（§4.3 於 `9.1` 撞見一句），**未逐節比對兩者之差** | **真缺口**。若 export 系統性地掉句，則 `outline_map.json` 之 169 條全部有此風險 —— 而本 feature 之所有判讀都建立在它上面 |
| 3 | **PLP3（Memory Seat Module）之列項未定位** | 記載限制。其餘四表可讀，PLP3 未確認；`PROF-001-01` 之 ER 於該部分不寫 |
| 4 | **`11.4` 之 table CPA2 逐列對應未確定** | 記載限制。列項名稱抽得出，兩欄之對應關係未確定 |
| 5 | **12 個「只在圖裡」之 PU id 未逐一查其所屬 section** | 記載限制。本輪只比了集合差，未逐一定位 |
| 6 | **framework 草案之 Layer 3 逐章對映未經分析層覆核** | 依 05b「草案即可，定稿待覆核」，非缺口，惟其數字已複驗（§9）|

**另記一件方法上的事**：作業 4／5 之答案之所以與 04 輪相反，
**單純因為這一輪多問了一個檔**。04 輪問「xlsx 裡有沒有圖」，答案是沒有；
**沒有人問「圖會不會在 PDF 裡」**，而 PDF 一直在 `BASELINE.sha256` 的第四列上。

> **「抽不出來」與「沒去抽那一份」是兩件事** —— R-U23 之所以要求先驗抽取能力，
> 防的正是這個，而它防中了。

---

## 8. 動作清單 —— 與 git 陳述逐項對照（R-G6，唯讀與改狀態分列）

| # | 動作 | 對象 | 是否 git |
|---|---|---|---|
| 1 | 檔案追加 | `RULINGS.md`（＋五條）| 否 |
| 2 | 檔案新建 | `framework.md`（草案）| 否 |
| 3 | 檔案新建 | `docs/upstream/05_framework_draft.md` | 否 |
| 4 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 5 | **唯讀**讀取 | 他 feature 之 `data/spec_id_to_outline.tsv` ×4、`features/home/scripts/*` ×3 | 否 |
| 6 | **唯讀**讀取 | spec xlsx／PDF、037、`data/*.tsv`／`*.json` | 否 |
| 7 | 暫存目錄建立與刪除 | `features/home` 之複本、讀者實驗之三個目錄、PDF 渲染之 PNG | 否（repo 外，用完即刪）|

**未執行任何會改變 repo 狀態之 git**：`commit`／`push`／`add`／`checkout`／
`restore`／`reset`／`stash`／`clean`／`rm`。

**唯讀 git 亦未使用** —— 本輪一次都沒跑 `git status`／`diff`／`show`。
（04 輪曾為查 schema 而跑過唯讀 git；本輪之查證全部以檔案系統與
`zipfile`／`PyMuPDF` 完成。）

**未寫入他 feature 任何檔**（R-U24 唯讀之要求）：comfort／sxm／amfm／
projection／home 之檔案**一個都沒有被寫**。`features/home` 之實驗全在
tempfile 複本上，且複本內之 `spec_id_to_outline.tsv` 經比對與 repo 內**逐位元組相同**
（recon 未跑成，故未寫）。

**未動**：`inputs/`（含 R-U17 之 spec 副本 —— 刪除屬 Pei）、`BASELINE.sha256`、
`data/` 之任何既有檔（含 `spec_popup_ids.tsv` —— 見 §6 之請裁）、
`ANOMALIES.md`（A-UP02 之性質重估屬 Tier 2）、`scripts/recon.py`、
`docs/handoff/*`、`spec-index/`。

---

## 9. framework 草案之複驗

`framework.md` 已落檔。其每個數字之量測條件與實測：

| 項 | 實測 |
|---|---|
| Layer 1 = `User Profiles` | 037 FROP 欄 **182 列**（180 FR ＋ 2 Out of scope），空 25 列為 Heading |
| Layer 2 八組 leaf 數 | **逐組相符，合計 180**（04 輪已驗，本輪重驗）|
| Layer 3 逐章 leaf | ch4=28、5=40、6=11、7=14、8=25、9=22、10=3、11=6、12=25、13=4、14=2 → **180** |
| Layer 3 逐章生成 section | 16／27／10／9／20／21／3／4／18／3／2 → **133** |
| 兩數之別 | 135（037 引用）vs 133（生成）—— §4 逐條具名其差 |

**§6「待覆核之處」列三項**，皆為本層所擬而非 R-U20 所定者。

---

## 10. 待裁

1. **comfort 之孤兒檔**（§1.2）—— R-G4 之連帶，comfort 四份文件指向舊名。
2. **`spec_popup_ids.tsv` 是否由 20 擴為 32**（§6）。
3. **DR #4 之範圍是否收窄**（§6）—— spec 已載 `PU1087`／`PU1088` 之觸發條件，
   缺的是 Pop Up List 之內文。
4. **A-UP02／DR #3 之性質**（§5.3）—— 重估為「spec 有而 SWE 未涵蓋」，
   形態同 Comfort R-C16。
5. **framework 草案之定稿**（§9）。
6. **§7 第 2 項是否值得一驗** —— PDF 與 xlsx export 之逐節差異；
   若 export 系統性掉句，影響面是全部 169 條。
