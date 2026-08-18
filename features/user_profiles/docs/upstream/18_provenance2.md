# 上繳 18（A）— 來源標示、第一批 ER 出處對照、J-6 雙向自檢

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`18_provenance2.md`（**無裁決條文**）
- **本輪未執行任何 git**；**未寫回工作簿**（R-U14）
- 語料：44 條 TC（pilot 16 ＋ 第一批 28）

## 0. 全閘現況

| 項 | 結果 |
|---|---|
| `lint_tcs.py` 語料 | 44 條，**違規 0** |
| `lint_tcs.py --self-test` | **44 / 44**（原 37 ＋ **G17／G18 七案**）|
| `lint_variant_labels.py` 反向 | 9 / 9 |
| `lint_variant_labels.py --check` | 44 條，違規 0 |
| `build_batch_context.py --selfcheck` | 8 / 8 |
| `render_spec_region.py --regression` | 7 / 7 |

**本輪修正三條 TC**（皆為 J-5 之範圍層級問題，見 §2.3）：`011`／`020`／`023`。

---

## 1. 作業 A-1 —— pilot 之來源標示（J-4，**ER 文字未動**）

五處，逐條於 `reasoning` 內具名其權威：

| tc_id | ER | 句 | 類 | 權威 |
|---|---|---|---|---|
| 003 | ER1 | The Add New Profile button is present while four Driver Profiles exist | **方法** | §5.6 BVA 界前基準線（5.2 只寫「達上限時不在」，未寫其反面）|
| 004 | ER4 | The vehicle completes the ignition cycle | **裁決** | **R-U21**（Service B 群；spec 從未提及 ignition cycle）|
| 008 | ER2 | The Welcome Popup is still displayed at 29 seconds | **方法** | §5.6（7.4 之「30 秒後清除」亦可讀為「不遲於 30 秒」）|
| 010 | ER3 | The vehicle completes the ignition cycle | **裁決** | **R-U21**；另 ER5 之觀察點出自 **5.1.1**（17 輪已補列引用）|
| 015 | ER3 | The deactivation screen still accepts a further PIN entry | **方法** | §5.6（12.9 只寫「10 次後取消」）|

**未新增工作簿欄位**（18 包明文）—— 標示走 `reasoning`。

**第一批之同型檢查**：本批**無 `ignition cycle`**（grep 全 44 條，僅 pilot 之
`032`／`070` 有）。BVA 兩條之界前基準線：

- `030`（9.5.3）—— **有 spec 依據**：條文為「until the number of Profiles
  **exceeds** the number of Memory Seats」，`exceeds` 為嚴格大於，
  故「相等時仍不可用」由條文明含，**不是方法產物**。
- `036`（9.9）—— 只驗上限，**無界前基準線**。

**故第一批之「方法」「裁決」句數皆為 0。** 這不是巧合：
本批多為呈現與分支條款，其可觀察形態由條文直接給出。

---

## 2. 作業 A-2 —— 第一批 28 條之 ER 出處對照

### 2.1 總計（**77 句 ER**）

| 關係 | 句數 |
|---|---|
| 逐字引用 | 17 |
| 改寫自 | 31 |
| 由該句推得 | 9 |
| 無直接出處（步）步驟回聲 | 20 |
| **無直接出處（缺）真缺口** | **0** |
| 合計 | **77** |

### 2.2 逐條（以 Test Set 分組；`步`＝步驟回聲）

#### Editing — ch9 之 9.1–9.3.2

| tc_id | ER | 出處 | 關係 |
|---|---|---|---|
| 017 | 1 | 5.1（UI 定位詞登記）| 步 |
| 017 | 2 | 9.1 `listed in the order according to Table EDPR1` ＋ **p14 之 Table EDPR1 列項**（must_carry）＋ 9.1 `a circled number 1 next to Resume Tutorials` | **逐字引用**（列項與圈號）|
| 018 | 1 | 5.1 | 步 |
| 018 | 2 | 9.1.1 `will not show the username and avatar to the left of the Edit Profile List (8.4" will show the username in the Edit Username line like “Edit username: [username]”)` | **逐字引用** |
| 019 | 1 | 5.1 | 步 |
| 019 | 2 | 9.1.2 `Memory seat status is not available if vehicle is not equipped` | 改寫自 |
| 020 | 1 | 5.1 | 步 |
| 020 | 2 | 9.2 `Don’t show the Connected Profile options/info or Stellantis Connected Account button` | **逐字引用**（label 見 §2.3）|
| 021 | 1 | —— | **步**（基準線之記錄；非邊界，不屬「方法」）|
| 021 | 2 | —— | 步 |
| 021 | 3 | 9.3 `the following will be greyed out and cannot be selected/completed: Deleting a Profile, editing username, editing avatar, Tutorials, Resume Setup, and viewing info of what is linked to a Profile` | **逐字引用**（六項全數）|
| 022 | 1 | 9.3 `cannot be selected/completed` | 由該句推得 |
| 022 | 2 | 9.3.1 `a bonk tone will be played along with the message “Function not available while vehicle in Motion.”` | **逐字引用** |
| 023 | 1–2 | —— | 步 |
| 023 | 3 | 9.3.2 `play the bonk and show the message specified above` ＋ 9.3.1（訊息字串）| **逐字引用** |

#### Editing — ch9 之 9.4–9.6.1

| tc_id | ER | 出處 | 關係 |
|---|---|---|---|
| 024 | 1、3 | —— | 步 |
| 024 | 2、4 | 9.4 `Pressing anywhere on the avatar or anywhere on the “Change Avatar” line will initiate a screen` | 改寫自 |
| 025 | 1 | 9.4 | 步 |
| 025 | 2 | 9.4.1 `show the currently selected Avatar highlighted and provide the option to choose from all other available avatars` | 改寫自 |
| 026 | 1–3 | —— | 步 |
| 026 | 4 | 9.4.2 `Exiting without saving will not result in an Avatar change` | 改寫自 |
| 027 | 1–2 | —— | 步 |
| 027 | 3 | 9.5 `the active Profile will be linked to that memory seat button/position` | 改寫自 |
| 028 | 1–2 | 5.1／—— | 步 |
| 028 | 3 | 9.5.1 `swap the active Profile’s previous seat preference with the other Profile` | 改寫自 |
| 029 | 1–2 | 5.1／—— | 步 |
| 029 | 3 | 9.5.2 `take the newly selected memory seat position from the previous user…The previously linked Profile will no longer be linked` | 改寫自 |
| 030 | 1 | 9.5.3 `will not be available and will be greyed out until the number of Profiles exceeds` | **改寫自**（`exceeds` 含相等時不可用）|
| 030 | 2 | —— | 步 |
| 030 | 3 | 9.5.3 同上 | 由該句推得 |
| 031 | 1 | —— | 步 |
| 031 | 2 | 9.6 `pushing save will update the seat position for whichever Profile is linked to that seat` | 改寫自 |
| 031 | 3 | 9.6 `a popup message (PU0588) will come up…inform the user of which Profile the seat was saved to` | **逐字引用**（PU0588）|
| 032 | 1 | 9.6.1 `The Welcome Popup size setting will default on small` | 改寫自 |
| 032 | 2–3 | —— | 步 |
| 032 | 4 | 9.6.1 `If turned off, do not show welcome popup for that Profile when it becomes active` | 改寫自 |

#### Editing — ch9 之 9.7–9.9 ＋ ch10

| tc_id | ER | 出處 | 關係 |
|---|---|---|---|
| 033 | 1 | —— | 步 |
| 033 | 2 | 9.7 `a verification popup message will confirm the delete` | **改寫自**（「尚未刪除」為 §7 false-pass 之防線，由 `previous to` 推得）|
| 034 | 1–2 | —— | 步 |
| 034 | 3 | 9.7.1 `they will be taken back to the All Profiles tab` | **逐字引用** |
| 035 | 1–2 | —— | 步 |
| 035 | 3 | 9.7.2 `“User 1” or the last known Profile, prior to the deleted one, will become active` | **逐字引用**（二擇一照錄）|
| 036 | 1 | 5.1 | 步 |
| 036 | 2 | 9.9 `maximum of 6 lines of information per page` | 改寫自 |
| 037 | 1 | 10.2 `Choosing anywhere on the line for “What is linked to my Profile”` | **逐字引用** |
| 037 | 2 | 10.2 `will show a page of general info…Remove “Memory Seat” section for all vehicles` | **逐字引用** |
| 038 | 1–3 | 10.2／5.1 | 步 |
| 038 | 4 | 10.3 `show the same page as from the Edit Profiles tab` | 改寫自 |
| 039 | 1 | 10.3.1 | 步 |
| 039 | 2 | 10.3.1 `“Your Driver Profile will remember your personal preferences…Below are some examples.” followed by the info in the chart above, when applicable` | **逐字引用**（引言字串）|

#### Connected Account — ch11

| tc_id | ER | 出處 | 關係 |
|---|---|---|---|
| 040 | 1 | 5.1 | 步 |
| 040 | 2 | 11.3 `The Connected Account line item will always be displayed on the “Edit Profile” tab if the vehicle is equipped with connectivity` | **逐字引用** |
| 041 | 1 | 11.3.1 | 步 |
| 041 | 2 | 11.3.1 `will bring the user to the Connected Account App` | 改寫自 |
| 042 | 1–3 | —— | 步 |
| 042 | 4 | 11.5 `it would update for all users who have installed it locally` | 改寫自 |
| 043 | 1–3 | —— | 步 |
| 043 | 4 | 11.5 `it should only appear in the app tray for the local user that has installed it` | 改寫自 |
| 044 | 1 | 5.1 ＋ p17 之表級註記 | 步 |
| 044 | 2 | **p17** `**R1 High Only: This table (Table CPA2) is not applicable. There will be no info button showed nextto the Connected Account button.` | **逐字引用**（版面註記）|

### 2.3 `pre_conditions` 之字面值與**變體／排除條款之範圍層級**（J-5）

#### (a) 字面值

| 字面值 | 出現於 | 出處 | 關係 |
|---|---|---|---|
| `8.4-inch screen` | 018 | 9.1.1 `8.4inch screen size` | 逐字（連字號為英文正寫）|
| `region without the brand app` | 020 | 9.2 `regions without the <Brand> app` | 改寫自（`<Brand>` 為 spec 之佔位符）|
| `memory seat 1`／`memory seat 2` | 028／029／031 | —— | **無直接出處** —— 條文只說 `memory seat position`，**編號為測試設置**（同 `ignition cycle` 之形態，但屬「方法」而非「裁決」）|
| `two memory seats` | 030 | —— | 同上（數量為設置，使邊界可量）|
| `Navigation` | 039 | 10.3.1 `if a vehicle does not have Navigation, do not show the Navigation examples` | 逐字 |
| `connectivity` | 040／041 | 11.3 `if the vehicle is equipped with connectivity` | 逐字 |
| `R1 High variant` | 017／044 | 9.3.2／p17 之 `R1 High Only` | 逐字 |
| `setup assistant is not completed` | 017 | 9.1 `removed as a line item once the user has completed setup assistant` | 由該句推得 |
| `Connected Account`（各自之帳號）| 042／043 | 11.5／11.3 | 逐字 |

#### (b) 變體／排除條款之**範圍層級** —— 本輪逐條複位

| 條款 | 出處 | **範圍層級** | 判定依據（版面）|
|---|---|---|---|
| `****R1 High Only: "Stellantis Account" to be replaced with "Connected Account"` | p14 | **列級** | 該註記印於 p14 左側，其 `****` 與 **Table EDPR1 之 `****“ Stellantis Account”` 那一列**對應（y=289.8）；表中其餘列無 `****` |
| `**R1 High Only: This table (Table CPA2) is not applicable` | p17 | **表級** | `**` 與表標題 `**Table CPA2.)` 對應（16 輪 F-2 已判，本輪未改）|
| `****For China market only: do not show this content` | p17 | **列級** | `****` 與 `****Connected Navigation` 該列對應（16 輪 F-2 更正）|
| `8.4inch screen size will not show…` | 9.1.1 | **節級** | 整條 EDPR1.1 即該尺寸之規定 |
| `not equipped with memory seats` | 9.1.2 | **節級** | 整條 EDPR1.2 |
| `regions without the <Brand> app` | 9.2 | **節級** | 整條 EDPR2 |
| `This logic is not applicable for 7” screens` | 5.1.2 | **句級** | 該句只否定 PRACC7.2 之圖示與字串邏輯（14 輪已據此加 pre-condition）|
| `if a vehicle does not have Navigation` | 10.3.1 | **句級** | 括號內之例示條件，只約束 Navigation 範例之顯示 |

#### (c) **本輪據此修正三條**（範圍層級判錯）

| tc_id | 原狀 | 問題 | 修正 |
|---|---|---|---|
| **011**（pilot 091-01）| pre 有「R1 High variant」| 該覆寫為**列級**（Table EDPR1 之一列），而本 TC 之 ER **不含任何帳號 label** —— 把列級覆寫當成整條 TC 之條件，**無故把 TC 限縮到 R1 High 車上** | 移除該 pre-condition，remarks 改記其層級 |
| **023**（091-02）| 同上 | 同上 | 同上 |
| **020**（088）| ER 寫 `Connected Account` | 那是 R1 High 之覆寫形式；9.2 自己的字是 `Stellantis Connected Account`。**用別節之變體形式寫本節之 label，既非逐字亦未宣告變體** | ER 改回 9.2 之逐字，並記其待裁（見下）|

**待裁**：**R1 High 之覆寫是否及於 9.2 之 label？**
版面上該覆寫為列級（Table EDPR1），**是否推及全章之同名 label，版面無從判定**。

- 若**不及**（本輪之保守取法）：TC-020 在 R1 High 車上會讀到 `Connected Account`
  而 ER 寫 `Stellantis Connected Account` → **假失敗**。
- 若**及於**：則 9.2 之逐字須被覆寫，且 `lint_variant_labels` 之適用範圍應擴及本節。

**執行層未自裁**，取逐字（較窄）並具名。

---

## 3. 作業 A-3 —— J-6 雙向自檢落為閘（G17／G18）

### 3.1 兩閘只做機械可判定的那一半

| 閘 | 問什麼 | 對應之歷史缺陷 |
|---|---|---|
| **G17 多引** | 引用欄之每一節，是否為本節／PLP 併列／`REF_EXTRA` 登記之一 | **TC-013 之 `11.5`**（F-1）|
| **G18 少引** | ER 之**引號字面值**，是否溯得到某一被引之節之 `pdf_text` 或 must_carry | **TC-010 之 `5.1.1`**（17 輪）|

「該節是否真被驗證」終究要人讀，但**「引用了一個沒登記理由的節」與
「ER 裡有一個溯不到來源的字串」是機器擋得住的**。

### 3.2 首跑結果 —— **G18 轉紅 5 條，是真陽性**

```
G18 NR1L-UserProfiles-019: ER 之字面值 「Edit Profile」 溯不到被引之節（9.1.2）
G18 NR1L-UserProfiles-020: …（9.2）
G18 NR1L-UserProfiles-024: …（9.4）
G18 NR1L-UserProfiles-028: …（9.5.1）
G18 NR1L-UserProfiles-029: …（9.5.2）
```

`“Edit Profile”` 是**分頁名**，其來源為 5.1（`two tabs; “All Profiles”
and “Edit Profile”`），而各該節自己不含這個字串。

**處置：不逐條把 5.1 灌進引用欄。** 若那樣做，**每一條 ch9 之 TC 都會引用 5.1**，
引用欄就從追溯變成導覽紀錄 —— 那正是 F-1 要防的方向。
改為**一次登記於 `UI_LOCATORS`**，並讓 G18 **自己驗證這張登記表沒說謊**：
每個定位詞須確實出現在其登記節次之 `pdf_text` 內，否則轉紅。

### 3.3 方向性案例（**七案，含登記表說謊**）

```
PASS — G17 注入：引用未登記之節（TC-013 之 11.5 形狀）: 紅
PASS — G17 範圍：REF_EXTRA 已登記之節（9.3.1）→ 綠
PASS — G17 範圍：PLP leaf 併列 3.x → 綠
PASS — G18 注入：ER 之字面值溯不到被引之節: 紅
PASS — G18 範圍：字面值確在被引之節內 → 綠
PASS — G18 範圍：UI 定位詞已登記 → 綠
PASS — 登記表說謊（Edit Profile → 12.9）→ 紅
      └ G18: UI 定位詞登記表有誤 ——「Edit Profile」不在 12.9 之 pdf_text 內

44 / 44 directional cases PASS
```

### 3.4 全批 44 條之結果：**G17 0 紅、G18 0 紅**

多引方向：44 條之引用欄共 **60 個節次引用**（實測），其中
本節 **44**、`REF_EXTRA` **6**（`5.1.2`／`5.1.1`／`9.3.1`×2／`9.3`／`10.2`）、
PLP 併列 **10**（TC-001／004 各 5）—— **餘數 0，全部登記在案**。
少引方向：ER 之引號字面值全部溯得到來源或屬已登記之 UI 定位詞。

---

## 4. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 分類 | 說明 |
|---|---|---|---|
| 1 | **R1 High 覆寫是否及於 9.2 之 label** | **待裁** | §2.3(c)。取逐字（較窄）之代價是 **TC-020 在 R1 High 車上會假失敗** |
| 2 | **`memory seat 1／2` 之編號無 spec 依據** | note（方法）| 條文只說 `memory seat position`。編號是為了讓 028／029／031 可執行而設。**與 `ignition cycle` 同形態但不同類** —— 那是裁決指定，這是測試設置 |
| 3 | **G18 只查 ER 之引號字面值** | 判準盲區（R-G11）| 不加引號之字面值（數字、`PU0588`、`Small`／`Off`）**不被 G18 檢查**。本輪以人工對照補上（§2.2），但**下一批若只跑閘會漏** |
| 4 | **G17 只驗「有無登記」，不驗「登記得對不對」** | 判準盲區 | `REF_EXTRA` 裡塞一個不相干的節，G17 一樣是綠 —— 它擋的是**未登記**，不是**登記錯誤** |
| 5 | **`variant_of()` 仍會被中文散文觸發** | note | TC-020 之 remarks 討論「R1 High 之覆寫是否及於本節」→ 被判為 R1 High。本輪無害（其 ER 無禁用字串），但**與 N-1 之否定判讀同一類盲區** |
| 6 | **第一批 28 條之內容覆核未做** | **分析層待辦** | 18 包已自記。本輪只交出對照表，**不得以「對照表齊了」推定內容已通過** |
| 7 | **pilot 之 `test_procedure`／`input_test_data` 仍未逐句對照** | note | J-5 只擴及 `pre_conditions`；步驟欄之字面值（如 `Restore Settings to Default`）**未系統性查過** |
| 8 | A-UP09／R-U14、DR #3／#4、R-U17、N-XF01、A-UP10（ACCEPTED）| 承前 | 擋 Phase 6 寫回 |

---

## 5. 動作清單（R-G6）

| # | 動作 | 對象 | git |
|---|---|---|---|
| 1 | 檔案編輯 | `scripts/gen_pilot.py`（五處來源標示；TC-011 之 pre-condition 與 remarks）| 否 |
| 2 | 檔案編輯 | `scripts/gen_batch01.py`（TC-020 之 ER label 與 remarks；TC-023 之 pre-condition 與 remarks）| 否 |
| 3 | 檔案編輯 | `scripts/lint_tcs.py`（**新閘 G17／G18**、`UI_LOCATORS` 登記表與其自我查核、七個方向性案例）| 否 |
| 4 | 檔案重生成 ×44 | `generated/`（三條內容變動，其餘僅 reasoning）| 否 |
| 5 | 檔案新建 | `docs/upstream/18_provenance2.md`（本檔）、`docs/upstream/18_batch02_sample.md` | 否 |
| 6 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 7 | 程式執行 | 生成 ×2、`lint_tcs`（語料＋self-test）、`lint_variant_labels`（反向＋check）、`--selfcheck`、`render_spec_region --regression` | 否 |
| 8 | **唯讀** | `fitz` 讀 spec PDF p14（`****` 標記之座標複位）| 否 |

**本輪未執行任何 git**：`add`／`commit`／`push`／`checkout`／`restore`／`reset`／
`rebase`／`stash`／`clean`／`rm` 皆無，**唯讀之 `git status` 亦未跑**。

**未動**：工作簿（**未寫回**）、`inputs/`、`forms/`、`feature.yaml`、`framework.md`、
`RULINGS.md`（本包無裁決條文）、`DECISIONS.md`、`ANOMALIES.md`、
`BASELINE.sha256`、`.gitignore`、`data/` 之任何檔、**他 feature 之任何檔**、`docs/fw036/`。
