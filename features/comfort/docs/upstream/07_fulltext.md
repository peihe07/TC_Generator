# 上繳包 07 — R-C18 落實 ＋ #15 更名 ＋ 129 節全文抽出

執行層 → 分析層。2026-08-15。回應下放包 `13_upstream06_review.md` §4。

**結論：六項作業全部完成。全文抽出四個 assertion 全 PASS。**
Phase 4 未開始。§4 之 ch11／ch12 事實已備，**不下結論**。

---

## 0. 置頂

| # | 事項 |
|---|---|
| **甲** | **ch11.1／12.1 與 ch11.2／12.2 之唯一實質差異是同一個片語：`opens popup and`**。ch11 有，ch12 無；其餘差異皆為標點與一處明顯錯字。事實見 §4，**不下結論** |
| **乙** | 全文抽出時 assertion **抓到一個假陽性並已修正判準** —— 3.3 之條文恰好 60 字整，與其截斷值相等是巧合而非未抽出。判準改為比對**原文長度**而非標題長度（§3.1） |

---

## 1. §8 R-C18 貼入

`RULINGS.md` 現載 **R-C1 ~ R-C18 + R-C4-1 + R-C5-1**，共 20 條，全部原文照錄。
R-C18 另立小節，標注適用全 feature、待 canon re-sync。

R-C18 對執行層之直接後果：本包所產之 `section_fulltext.tsv` 即為「一律讀
全文」之基礎設施。13 §4 選擇一次抽出全部 129 節而非逐題抽出，此判斷正確 ——
Phase 4 每寫一條 TC 都要讀條文，逐次繞開只會把同一個陷阱留給下一個問題。

## 2. §2 Test Set #15 更名 —— 三處同步，回報項已消失

`Comfort Widget` → **`Home Screen Widget`**。Layer 3 不變（17.1 ~ 17.5、18.1），
leaves 仍 21。

| 處 | 動作 |
|---|---|
| `scripts/verify_partn.py` | `PART_N` 之期望值更名；第四項檢查之註解改寫為通則 |
| `framework.md` | §2 表、§3.3 命名段（改記更名依據）、§6 明細標題、§7 插入邊界 |
| `data/test_set_map.tsv` | 由腳本重生，15 個名稱實測無舊名 |

**回報項已消失**（13 §2 指定之驗收條件）：

```
- PASS — no Test Set name starts with the Test Group word (§4.2):
    expected [], measured [] — 15 names checked against prefix 'Comfort'
```

更名前該行為 `measured ['Comfort Widget']`。另實測 `RUNBOOK.md` 有一處以舊名
指涉 Test Set（插入邊界段），一併更新。

**其餘 `Comfort Widget` 字樣刻意保留**：SR24 自身之章標題（ch17
`Home screen - Comfort Widget`、ch18 `10.25" Home screen - Comfort Widget`）
與條文用語（`W0.) The Comfort widget will have two screens`）是 spec 原文，
更名的是 Test Set 名稱，不是 spec。`layer3_map.tsv`／`sr24_uncited_sections.tsv`
之 `chapter_title` 欄同理。

### 2.1 接受更名之裁定，並記一句給日後

我原主張「spec 稱其為 the Comfort widget，故該字指涉受測物件」。13 §2 之
反駁成立且乾淨：**Bluetooth 之例中，spec 也稱該功能為 "Bluetooth pairing"**
—— §4.2 禁的正是這個形態，我的理由若成立，該範例本身就不成立。

更值得記的是 13 §2 指出的另一件事：若那行 `and n != "Comfort Widget"` 留在
條件式裡，**這次更名永遠不會發生 —— 檢查會 PASS，而問題會被 PASS 蓋住**。
我已把該理由寫進 `verify_partn.py` 該項檢查之註解，使下一個維護者知道那行
獨立回報不是冗餘。

## 3. §4 全文抽出 —— `data/section_fulltext.tsv`

129 列，四欄：`outline`｜`req_id`｜`test_set`（更名後之值）｜`full_text`。
內部換行以字面 `\n` 轉義，一節恰一列。腳本
`scripts/build_section_fulltext.py`，可重跑。

```
- PASS — row count == 129: expected 129, measured 129
- PASS — no row equals its truncated layer3_map value: expected [], measured []
    — 比對基準為原文長度而非標題長度；1 列因巧合相等（條文恰 60 字）：['3.3']
- PASS — full_text shorter than 60 chars: 5 rows listed, each confirmed
    genuinely short — [('3.3',60),('7.9',27),('9.4.1',43),('10.3',38),('14.1',52)]
- PASS — outline set equals layer3_map's: expected [], measured [] — 129 vs 129
```

`full_text` 長度：**最短 27、中位 245、最長 1232**。
對照 `layer3_map` 之 60 字上限 —— **中位數即為截斷值之 4 倍**，最長者 20 倍。
R-C18 所擔心的資訊遺失，在本 feature 是多數列的常態而非少數例外。

### 3.1 乙：assertion 抓到假陽性，判準已修

第二項 assertion 首次執行報 **FAIL `['3.3']`**。查證：

```
3.3 原文：C21.) MAX DEF and REAR DEF are available during climate off.
原文長度：60（句號結尾、語意完整）
```

**該節條文恰好就是 60 字整**，故它與自己的截斷值相等 —— 是巧合，不是「仍為
截斷輸出」。原判準用「標題長度 ≥ 60」推斷發生過截斷，對邊界值失效。

已改為比對**原文長度 > 60**（截斷是否真的移除了東西），並將巧合相等者另列
回報。修正後 PASS，且該巧合仍留在輸出裡供人看見，不是消失。

這條 assertion 本來可以寫成永遠不會失敗的樣子（例如只比長度）。它會失敗，
且第一次就抓到邊界 —— 記此一筆，因為 §5a 要求的正是「檢查項須確認其在該
階段確實可能失敗」。

### 3.2 五列短於 60 字者，逐列確認原文確實短

| outline | 長度 | 全文 |
|---|---|---|
| `7.9` | 27 | `CR9.) AC has on/ off state.` |
| `10.3` | 38 | `EH3.) Button label will read AUTO ECO.` |
| `9.4.1` | 43 | `CR13.1.) The button label will read «Rear».` |
| `14.1` | 52 | `HVACP1.) HVAC pop-ups should follow the pop-up list.` |
| `3.3` | 60 | `C21.) MAX DEF and REAR DEF are available during climate off.` |

五列皆為完整句、句號結尾，非截斷殘留。

## 4. §4.1 ch11／ch12 —— 事實，不下結論

依 13 §4.1，只供事實；「入口是否相同」之判定屬 Tier 2，由分析層做。

### 4.1 全文

**`11.1`**（`SWE1-HVAC-054`，518 chars）
> HVS1. For Multi-Level Heated/Vented seats**,** a press of the heated seat
> button **opens popup and** turns the seat on HI, the soft button highlights
> red and the control displays 3 arrows, HI and/or LEDs. The next button press
> sets the seat to MED, button remains highlighted and displays 2 arrows, MED
> and/or LEDs. The third button press sets the seat to LO, button remains
> highlighted and displays 1 arrow, LO and/or LED. The next press, turns the
> heated seat OFF, the button is no longer highlighted and 3 arrows are shown.

**`12.1`**（`SWE1-HVAC-067`，503 chars）
> HVS1. For Multi-Level Heated/Vented seats a press of the heated seat button
> turns the seat on HI, the soft button highlights red and the control displays
> 3 arrows, HI and/or LEDs **(.** The next button press sets the seat to MED,
> button remains highlighted and displays 2 arrows, MED and/or LEDs. The third
> button press sets the seat to LO, button remains highlighted and displays 1
> arrow, LO and/or LED. The next press, turns the heated seat OFF, the button
> is no longer highlighted and 3 arrows are shown.

**`11.2`**（`SWE1-HVAC-055`，534 chars）
> HVS2. For Multi-Level Heated/Vented seats**,** a press of the vented seat
> button **opens popup and** turns the seat on HI , the soft button highlights
> blue and control displays a large fan, HI and/or 3 LEDs. …（後續與 12.2 逐字相同）

**`12.2`**（`SWE1-HVAC-068`，516 chars）
> HVS2. For Multi-Level Heated/Vented seats a press of the vented seat button
> turns the seat on HI, the soft button highlights blue and control displays a
> large fan, HI and/or 3 LEDs. …（後續與 11.2 逐字相同）

### 4.2 逐詞差異（`difflib`，**autojunk 已關閉**）

| 對 | 相似度 | 差異 |
|---|---|---|
| 11.1 vs 12.1 | **0.9556** | ① `seats,` → `seats`（逗號）<br>② **`opens popup and` → （無）**<br>③ `LEDs.` → `LEDs (.`（多一個左括號） |
| 11.2 vs 12.2 | **0.9579** | ① `seats,` → `seats`（逗號）<br>② **`opens popup and` → （無）**<br>③ `HI ,` → `HI,`（空格位置） |

**四節之唯一實質差異，是同一個片語 `opens popup and`，ch11 有、ch12 無。**
其餘三處為標點與空白；`12.1` 之 `LEDs (.` 為明顯錯字（孤立左括號）。

### 4.3 依 13 §4.1 之三項逐項回報

**一、所述之操作元件**

| | 11.1／11.2 | 12.1／12.2 |
|---|---|---|
| 觸發 | `a press of the heated/vented seat button` | **同左，逐字相同** |
| 元件類型 | 條文稱 `button`，且下文以 `the soft button highlights` 指涉同一物 | **同左** |
| 硬鍵 | 兩者皆**未提及**任何實體鍵（無 `hard control`／`hard button`／`knob` 等詞） | 同左 |

四節之操作元件在**字面上完全相同**：一個 soft button，按壓循環
HI → MED → LO → OFF。

**二、所述之顯示位置**

| | 11.1／11.2 | 12.1／12.2 |
|---|---|---|
| 按鈕本身 | `the soft button highlights red`（11.2／12.2 為 `blue`） | 同左 |
| 指示內容 | `the control displays 3 arrows, HI and/or LEDs`（11.2／12.2 為 `a large fan, HI and/or 3 LEDs`） | 同左 |
| **彈窗** | **`opens popup`** | **無此語** |
| 狀態列 | 兩者皆**未提及** status bar | 同左 |

顯示位置之描述亦逐字相同，**唯一差別是 ch11 另外開一個 popup**。

**三、差異詞句逐一列出**

1. `opens popup and` —— **ch11 有，ch12 無**（11.1／11.2 各一處）
2. `seats,` vs `seats` —— 逗號有無
3. `LEDs.` vs `LEDs (.` —— 12.1 多一孤立左括號（疑為錯字）
4. `HI ,` vs `HI,` —— 11.2 之空格位置

### 4.4 執行層明確不做之事

**不判斷入口是否相同。** 上列為字面事實，其解讀有多種可能，而選擇哪一種
正是 Tier 2 之工作：

- `opens popup` 可能表示不同進入路徑（一者有中介彈窗）；
- 也可能是同一入口下之顯示差異（彈窗是回饋而非入口）；
- 也可能是 carryover 章漏寫。

**這三者我判不了，也不該判。** 13 §4.1 說「只供事實」，我照做。

一併提供之相關事實，供分析層一併衡量：13.1（`assumption`，未被 037 引用）
述及 `lower comfort screen` 之有無會改變座椅／腰靠控制之可及性；
Home Screen `HSD13`（outline 4.11）述及 `lower non-articulating screen`
存在時不提供 heated/vented seats widget 與 shortcut。**兩者皆不在 Part N
母體內**，但與「座椅控制之入口」同題。

## 5. §4.2 順帶查明 —— `14.19`

`SWE1-HVAC-104`，`Climate Popups` 組，全文 727 chars：

> HVACSB6.) When the Climate widget is shown on the currently displayed screen
> and the user interacts with climate controls, either soft or hard, pop ups
> will behave as follows:
> - Temperature Pop-up: only on status bar (do not show drop down menu)
> - FAN Speed Pop-up: show for R1Low, do not show for R1H.
> - Air Flow Mode (distribution) Pop-up: do not show (feedback is already on widget)
> - Climate On/Off Pop-up: do not show (feedback is already on widget)
> - Auto Pop-up: do not show (feedback is already on widget)
> - Heated Seats Pop-up: only on status bar (do not show drop down menu)
> - Vented Seats Pop-up: only on status bar (do not show drop down menu)
> - Heated Steering Wheel Pop-up: only on status bar (do not show drop down menu)

**leaf 分布：8 個 bullet → 8 個 leaves，順序一一對應。**

| leaf | 037 Requirement Title | 對應 bullet |
|---|---|---|
| `-01` | Temperature Control | Temperature Pop-up |
| `-02` | Fan Speed Control | FAN Speed Pop-up |
| `-03` | Airflow Mode Control | Air Flow Mode Pop-up |
| `-04` | HVAC Popup Behavior | Climate On/Off Pop-up |
| `-05` | AUTO Mode Behavior | AUTO Pop-up |
| `-06` | HVAC Popup Behavior | Heated Seats Pop-up |
| `-07` | HVAC Popup Behavior | Vented Seats Pop-up |
| `-08` | HVAC Popup Behavior | Heated Steering Wheel Pop-up |

**8 leaves 之成因已明**：不是一條複雜需求，是一張清單被逐項展開。037 之
拆法與條文結構一致，非過度切分。

供 Phase 4 之兩點觀察（**僅陳述**）：

1. 該節之前置條件為 `When the Climate widget is shown on the currently
   displayed screen` —— 與 `Home Screen Widget` 組（#15）之題材相關，
   但本節依 Part N 屬 `Climate Popups`（#10）。兩組之 TC 前置條件會有交集。
2. `-02` 之 bullet 含 variant 分歧（`show for R1Low, do not show for R1H`），
   為八者中唯一含機型條件者；§8.7.3 之 variant label 可能適用。

## 6. Phase 4 未開始

未產 TC、未指派 tc_id、未做 sibling 判定、未寫 profile `[OVERRIDE]`。

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 7.1 已驗

1. 全文抽出四個 assertion（含一次真實失敗與判準修正）。
2. 五列短於 60 字者逐列確認原文確實短。
3. 更名之三處同步，及第四項回報項由 `['Comfort Widget']` 轉為空。
4. ch11／ch12 四節全文與逐詞差異（`autojunk` 關閉）。
5. `14.19` 全文與其 8 leaves 之逐 bullet 對應。
6. `verify_partn.py` 六項檢查更名後全 PASS。

### 7.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **ch11／ch12 其餘 20 節之差異** | 13 §4.1 只指定 11.1/12.1 與 11.2/12.2 四節 | **中** —— 合併與否之判定若以 `opens popup` 為關鍵，其餘節是否呈現同一模式會影響結論。全文已在 `section_fulltext.tsv`，再比對成本低，**未做係因未指示** |
| 2 | **`opens popup` 之 popup 究竟指何物** | 需查 HMI Pop Up List；`paths.popup_list` 為 null，該檔不在 `inputs/` | **中** —— 若要判斷它是入口還是回饋，這是關鍵證據。已於 `DATA_REQUESTS.md` 登記 |
| 3 | **15 組之組內語意一致性** | 13 §6 裁定暫不處置，材料已備（本包之全文） | 低 —— 路徑已存在 |
| 4 | **既有判斷之全文複核**（R-C18 末句「凡以此類欄位為輸入之既有判斷，須回頭以全文複核」） | 本包只複核了 13 §4.1 指定之四節 | **中** —— 見下 |
| 5 | profile `[OVERRIDE]`、DR #6 | 分析層下一包／待 Pei 指認 | 中／低 |

**第 4 項需要說清楚，因為它是 R-C18 自己要求的。**

R-C18 末句要求回頭複核所有以截斷欄位為輸入之既有判斷。我盤點了本 feature
之既有判斷，其輸入來源如下：

| 判斷 | 輸入 | 是否受影響 |
|---|---|---|
| A-CF08 之 51 節四值分類 | `classify_uncited_sections.py` 直接讀 **export 全文**（`bare_text()` 無長度限制） | **否** |
| 17 節適用性判讀 | CFTS043 `.doc` 全文 ＋ tree view 結構化欄位 | **否** |
| Part N 之 15 組切分 | 分析層作業；11 §2／12 §2 之依據為 `layer3_map.tsv` | **是（部分）** |
| ch11／ch12 合併 | 13 §3 已自承係讀截斷標題 | **是** —— 本包已供全文 |
| 6.3 落位 | 已於上繳 06 讀全文複核 | 已複核 |

**Part N 之 15 組切分是唯一未複核者。** 其切分依據（章別、條款主題）多數
不依賴 60 字之後的內容，但我無法斷言全部如此 —— 那需要逐節讀全文再對照
分組理由，屬 Tier 2 之語意判斷。**材料現已齊備**（`section_fulltext.tsv`），
是否複核請分析層明示。

### 7.3 未做、亦未偷做者

- **未就 ch11／ch12 入口是否相同下任何結論**（13 §4.1 明文）。
- 未改 Part N 之任何分組或 leaf 歸屬；更名只動名稱，Layer 3 不變。
- 未依 `14.19` 之結構提出拆 TC 主張（§8.2.2 屬 Phase 4）。
- 未產 TC、未指派 tc_id、未寫 profile。
- 未重跑任何既有 feature 之 recon（R-C8）；對其目錄零寫入。
- 未執行任何 git 操作。

### 7.4 執行層對「本包可否結案」之判斷

**可結案。** 全文基礎設施已就位並通過驗算；更名三處同步且驗收條件（回報項
消失）達成；ch11／ch12 之事實已備且未越界下結論。

**建議分析層在裁定 ch11／ch12 之前，一併看 §7.2 第 1 與第 2 項**：
其餘 20 節是否呈現同一模式（我可再比對，成本低），以及 `opens popup` 之
popup 為何物（需 HMI Pop Up List，該檔不在 `inputs/`）。若不看第 2 項，
「彈窗是入口還是回饋」這個問題只能從措辭推斷。
