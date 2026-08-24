# 24 — W-P1′ 上繳包（canon 整併與四項裁定落地）

日期：2026-08-24
下放包：`docs/fw036/handoff/24_wp1_continuation.md`
執行層：Claude Code
結論：**§D 九項作業全數交付**。canon 整併完成、R-G13~R-G21 併入、
裁定 1／2／4 落地、裁定 3 於錨點層套用。**兩項升級**（§F-2 一處、§F-5 一處）
與**一項須 Pei 覆核之衝突**（裁定 3 之目標編號與 R-VF45 §一）見 §五。

**git**：未執行任何 git 操作（R-G5@`9814d24c`）。全部變更以檔案系統寫入。

---

## 一、逐步狀態（§D 作業清單）

| 步 | 事項 | 狀態 |
|---|---|---|
| 1 | 裁定 2 之措辭修正採 §C 版 | **交付** —— R-G18 條文即 §C 版全文 |
| 2 | FO 整併：兩個 `## 9.` 併一、R-G1~G12 單一落點、逐條錨點、[MOVED] | **交付**（§二）|
| 3 | R-G13~R-G21 併入 §9；§8.1／§8.8／§1.2 修訂；裁定 1 之行 432 | **交付**（§三）|
| 4 | FO 全文引用加前綴 | **交付 21 處，1 處升級**（§四）|
| 5 | IN §8.7.5 範圍查驗 ＋ 一行註記 | **交付**（§六）|
| 6 | `CANON_REFS_WAIVER.tsv` 產出 | **交付，789 列**（§七）|
| 7 | 裁定 3 之對映表 + 套用 + tsv 重產 | **對映表與錨點層套用交付**；交叉引用面未套用（§五-1）|
| 8 | `canon_refs.py --waiver` ＋ 三向測試 | **交付**（§八）|
| 9 | 全套 pytest ＋ 上繳 | **交付** —— 1113 passed / 8 failed（既有）|

---

## 二、預期數字對照（§E；相符者亦列）

| # | 指標 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| 1 | FO `^## 9\.` 標題數（逐行、區分大小寫）| 2 → **1** | **1** | **符** |
| 2 | FO 之 `R-G1` 落點 | 2 → **1** | **見下** | **須分定義**（§二-1）|
| 3 | `ruling` 型 unresolved 之 `R-G13`~`R-G21` 類 | 125 → **0** | **0** | **符** |
| 4 | FO 內 `canon §7.3` 字面落點 | 1 → **0** | **0** | **符** |
| 4b | 同串於全 repo 之其餘落點（下放包令回報）| 未知 | **5**（§二-2）| 基線 |
| 5 | `canon_refs.py --waiver` 之 FAIL 數 | **0** | **0**（`PASS`，exit 0）| **符** |
| 6 | waiver 列數 | 未知，首產即基線 | **805 列 / 299 檔**（量測時點見 §七）| **基線** |
| 7 | `rulings_hash.py` 重複 ruling_id 組數 | 8 → **0** | **0** | **符** |
| 8 | R-VF 最大號 | 82 → **90** | **90** | **符** |
| 9 | 全套 pytest 失敗數 | **8**（既有，不得增減）| **8**，且為同一 8 項 | **符** |
| 9b | pytest 通過數 | 下放包未列 | **1113**（23a 之 1096 + 本包新增 17）| 基線 |

### 二-1 第 2 項須分定義 —— **不自行調和，回報兩個數**

「`R-G1` 落點」在整併後有兩種可數之物，其值不同：

| 定義 | 實測 | 說明 |
|---|---|---|
| **條文錨點**（`^#### R-G1 `）| **1** | R-G13 所要之穩定錨點，**單一落點達成** |
| `^\| R-G1 \|` 之表列 | **2** | §9.2 導覽表 1 列 ＋ **§9.8.2「兩版摘要出入表」1 列** |

第二個 `| R-G1 |` 在 §9.8.2，其身分為**兩版比對之記錄**（下放包 §D-2 令
「摘要出入處列表回報」之落檔形式），**不是條文之第二個落點**。
**未為了讓數字變成 1 而改寫該表** —— 該表正是本步驟之產物。
若 Pei 認為該記錄應移出 canon（例如移入本上繳包），一句話即可，本層照辦。

### 二-2 第 4b 項 —— `canon §7.3` 之其餘 5 處落點

| 檔 | 行 | 性質 |
|---|---|---|
| `features/projection/docs/handoff/17_delivery_precheck.md` | 53 | **歷史檔**，入 waiver。**與 FO §5a-16 為同一句** |
| `docs/fw036/upstream/23a_wp1.md` | 179 | 歷史檔（23a 引述該懸空引用以升級）|
| `docs/fw036/handoff/24_wp1_continuation.md` | 41、110 | 本輪下放包（裁定 1 之條文與預期數字）|
| `tests/test_canon_refs.py` | 124–125 | **刻意以字面釘入之測試案例**（G-N）；判準改對即失效，故不得改 |

**一項未預期之發現**：`features/projection/docs/handoff/17_delivery_precheck.md:53`
與 FO §5a-16 之第 17 條**為逐字同一句**（含「雙層檢驗（canon §7.3）」之兩誤）。
其方向未查 —— 是 projection 之下放包升格入 canon，或反向轉錄，本層不推測。
**該誤已在 canon 側修正，歷史檔側依裁定 2 不追改。**

---

## 三、canon diff 摘要

| 檔 | +/− | 內容 |
|---|---|---|
| `docs/fw036/FEATURE_ONBOARDING.md` | **+356 / −86** | §9 整併、R-G13~21 併入、§8.1／§8.8／§1.2 修訂、裁定 1、21 處前綴 |
| `docs/runtime/ASPICE_SWE6_AI_Instruction.md` | **+1 / −0** | §8.7.5 之一行範圍註記（僅入 diff，待 Pei 裁）|
| `docs/fw036/templates/DECISIONS.md` | +2 / −2 | 前綴 |
| `docs/fw036/templates/PLAYBOOK.md` | +3 / −3 | 前綴 |
| `docs/fw036/templates/feature.yaml` | +2 / −2 | 前綴 |
| `features/vehicle_setting/RULINGS.md` | **+59 / −21** | 裁定 3 之改編 21 處、永久對照表、R-VF45 §一之 SUPERSEDED 註記 |

FO 行數 809 → **1079**。

### 三-1 §9 整併之結構

整併後單一 `## 9. 全域條文與通則（整併落點）`，八節：

| 節 | 內容 | 來源 |
|---|---|---|
| 9.1 | 十一項通則 | 原第一個 §9 之 §9.1（**號不變**）|
| 9.2 | 全域裁決條文 R-G1 ～ R-G21 | 原第一個 §9 之 §9.2 **併** 第二個 §9 之 §9.1 |
| 9.3 | 一條裁決只管一件事 | 原第一個 §9 之 §9.3（**號不變**）|
| 9.4 | 缺口 —— 具名留給下一個 feature | 原第二個 §9 之 §9.4（**號不變**）|
| 9.5 | 欄位接合矩陣（含 9.5.1～9.5.3）| 原第二個 §9 之 §9.5（**號不變**）|
| 9.6 | 全域常規 G-A ～ G-K ＋ G-N | **[MOVED]** 自原第二個 §9 之 §9.2 |
| 9.7 | 兩項素材與資料之判準 G-L／G-M | **[MOVED]** 自原第二個 §9 之 §9.3 |
| 9.8 | [MOVED] 對映表（9.8.1）＋ 兩版摘要出入（9.8.2）| 新增 |

**節序之取捨已寫入 canon 之導覽表**：9.4／9.5 保號（其外部引用最多，含
§9.5.2／§9.5.3 之子節引用），故 G-A～G-N 與 G-L／G-M 後移至 9.6／9.7
而非插在中間。**保住既有引用優先於保住閱讀順序。**

### 三-2 內容保存之逐行實測（**不是「應該沒掉」，是量過**）

以整併前之八個原段（各以行界抽出，逐字寫入）對整併後之 FO 逐行比對：

```
a91 (十一項通則)      18 非空行，缺 2   ← 皆為步 4 之前綴改寫（§5a→FO §5a、§9.3→FO §9.3）
a93 (一條裁決一件事)    9 非空行，缺 0
b92 (G-A～G-N)       15 非空行，缺 1   ← 標題改號 9.2→9.6
b93 (G-L／G-M)        5 非空行，缺 1   ← 標題改號 9.3→9.7
b94 (缺口)            7 非空行，缺 0
b95 (欄位接合矩陣)     49 非空行，缺 1   ← 步 4 之前綴改寫（§4.5→IN §4.5）
                    合計 103 行，缺 5
```

**5 處缺失逐一歸因於本包之刻意變更，非遺漏。非刻意之內容遺失 = 0。**
第二版 R-G 表（b91）之 16 行不入本比對 —— 其「一句話」依 §D-2 已改寫，
其**來源欄逐項升為主表之來源欄**（`user_profiles 02 輪`／`A-UP09`／
`05 輪（部分取代）`／`全輪次`／`多輪`／`37 輪` 六值實測皆在新檔內）。

### 三-3 §8.1／§8.8／§1.2 之修訂

- **§8.1**：「裁決逐字」列改為「裁決引用」（R-G13 之 `R-XX@<sha8>`）。
  **原「裁決逐字的理由」段保留不刪**，其下加
  `[SUPERSEDED by R-G13 — 逐字照錄之要求部分]` 並記其成因（23 包 §B-2）
- **§8.8**：「一批一上繳」加註「**除 R-G14 綠色通道生效期間**（FO §9.2）」
- **§1.2**：pilot protocol 之 Output 項下新增 R-G15 之數字化 verdict 判準
  （PASS／PASS-with-corrections／REGENERATE 之閾值、重跑上限 2 次、
  第 3 次之 Tier 2 檢討對象為規則而非語料）

### 三-4 R-G1～R-G21 之錨點與 sha8（R-G13 之引用基礎）

canon 側 21 條全數具 `#### R-Gn` 錨點並入 `RULINGS.sha.tsv`。
`RULINGS.sha.tsv`：**186 錨點**（ruling 167／group 15／superseded 4），
`--check` **exit 0**。

---

## 四、步 4 之前綴改寫 —— 逐處統計

**判準**：改寫者僅「實指某份 canon 之節號引用」；
以他文件為名之節號引用（`framework §2`、`PLAYBOOK.md §6`、`BT profile §3.6`、
`User Profiles 09 輪 §4`）**不加 canon 前綴** —— 其已由該名詞限定。

| 檔 | 改 FO | 改 IN | 其他表述調整 | 合計 |
|---|---|---|---|---|
| `docs/fw036/FEATURE_ONBOARDING.md` | 11 | 4 | 6 | **21** |
| `docs/fw036/templates/DECISIONS.md` | 2 | 0 | 0 | 2 |
| `docs/fw036/templates/PLAYBOOK.md` | 3 | 0 | 0 | 3 |
| `docs/fw036/templates/feature.yaml` | 2 | 0 | 0 | 2 |
| | | | | **28** |

**FO 之 4 處 IN 引用**（實指判定之依據）：

| 行（改前）| 原文 | 判 IN 之依據 |
|---|---|---|
| 110 | `any value the source does not state (§8.4)` | IN §8.4 = `No Fabrication`；FO §8.4 = 結果三分法 |
| 210 | `standard §4.3 tc_title` | IN §4.3 = `Test Item / tc_title — three acceptable shapes` |
| 213 | `spec_reference = constructed from spec_mode template (§10.7)` | IN §10.7 = `specification_reference`；FO 無 §10 |
| 771 | `input_test_data 之欄位歸屬（§4.5）` | IN §4.5 = `Input Test Data — field ownership`；FO 無 §4.5 |

**「其他表述調整」6 處**：本層新寫之散文中以「canon」加裸節號**舉例**者
（非引用），改為不觸閘之表述 —— 例：「`canon §9.1` 因而為歧義引用」改為
「以『canon』加裸 §9.1 之引用因而歧義」。**條文本體一律不改**（見 §七-2）。

**未改而升級者 1 處**：見 §五-2。

---

## 五、升級項

### 五-1 裁定 3 之目標編號與 R-VF45 §一 衝突（**須 Pei 覆核**）

**事實**：R-VF45（`bea4bbb8`）§一 明載「VF230 線之八條改為 **R-VF1–R-VF8**
（依 V04 §3.1 之對照表）」。裁定 3 令改為 **R-VF83–R-VF90**，
而其自身引 R-VF45 為依據。

**實測**（`RULINGS.md`）：

| 號 | 條文起始 | 全檔引用 |
|---|---|---|
| `R-VF1` | **0** | 8 |
| `R-VF2` | **0** | 6 |
| `R-VF3`～`R-VF7` | **0** | 0 |
| `R-VF8` | **0** | 6 |
| `R-VF9` | 1 | 15 |
| `R-VF10` | 1 | 19 |

**`R-VF1`–`R-VF8` 八號至今為空，且係 V04 §3.1 與 R-VF45 §一保留給這八條者。**
採 R-VF83–R-VF90 後，**該八號成為永久空號**（`A-VS02` 之先例為「缺號，
不補不重編」，故其不會被回收）。

**本層之處置**：**依裁定 3 執行**（Pei 之裁定優先於分析層之 R-VF45），
並於 `RULINGS.md` 之 R-VF45 §一 該句加
`【本句之目標編號經 24 包 §C 裁定 3 取代…原文保留不刪（R-TM13）】`。
**若 R-VF83–R-VF90 係誤寫而本意為 R-VF1–R-VF8，現在改回之成本最低**
（本輪僅動 21 處，且交叉引用面尚未套用）—— 一句話即可，本層照辦。

### 五-2 §F-2 觸發 —— 一處引用之實指不明，不猜

```
docs/fw036/FEATURE_ONBOARDING.md（原行 198，§2 Per-state strategy binding）
  | Style authority | fallback chain (§3) | done region | done region | done region |
```

- FO §3 = `spec_mode — source taxonomy`，**與 style authority 之 fallback 無關**
- IN §3 = `Workflow (Generate)`，亦無關
- 該表所指之 fallback chain **實體在 FO §2 之無編號子節**
  `### BLANK fallback chain (style decisions when no done region exists)`
  （原行 203，即該表下方五行）

**三種可能，本層不擇**：(a) 應為指向該無編號子節（則須給它一個節號）；
(b) `(§3)` 為序數「第三項」之筆誤；(c) 指向已不存在之舊節。
**未改**。裸 `§3` 記為 `unqualified`，不觸閘，故不阻塞。

### 五-3 §F-5 觸發 —— 活躍文件之改寫量不成比例，回報實測數再裁

§D-6 令「活躍文件之引用**改寫加前綴**，不入 waiver」。實測其量：

| | 處 | 檔 |
|---|---|---|
| 活躍檔之 unresolved + ambiguous | **279** | **~100** |
| 其中已 close-out feature 之治理簿（`RULINGS`／`ANOMALIES`／`DATA_REQUESTS`／`DECISIONS`）| ~120 | 7 個 feature |

前十名：`features/vehicle_setting/ANOMALIES.md`(24)、
`features/projection/DECISIONS.md`(23)、`docs/dev/PIPELINE_DESIGN.md`(17)、
`features/vehicle_setting/RULINGS.md`(14)、`features/comfort/RULINGS.md`(12)、
`features/projection/ANOMALIES.md`(11)、`features/user_profiles/docs/INDEX.md`(10)、
`features/time_management/RULINGS.md`(7)、各 feature `PLAYBOOK.md`(4~5)。

**其困難不在數量，在每一處都須在兩份 canon 間做語意判別。**
`canon §6` 於 FO 是 `Write-back → tag sequence`、於 IN 是 `Expected Results`
—— **判錯即把一個「錯的」引用寫進現行有效之裁決簿，比留一個「歧義的」更糟。**
（此即 §9.1 第 10 項通則之代價形態。）

**本層之處置**：
1. **R-G18 明文指名者已改完**：兩份 canon 自身、`docs/fw036/templates/`（§四）
2. **其餘 279 處入 waiver，理由標 `active-backlog`**，使閘現在可用（FAIL = 0）
   **且該積壓被逐檔逐行列舉、可數**（G-D：一個永遠空的清單與一個壞掉的清單，
   輸出相同 —— 故不以「不列」代替）
3. `active-backlog` **為暫時豁免，非永久**；工具於每次產出時印出該字樣

**待裁**：(a) 排一輪專做這 279 處（可機械化定位，但須逐處人判實指）；
(b) 只改活躍度最高之二本（`vehicle_setting` 之 `RULINGS`／`ANOMALIES`，38 處）
其餘留 backlog；(c) 維持現狀，以「waiver 只減不增」自然消化。
**本層無偏好，但指出 (c) 之下該 279 處永不轉紅。**

---

## 六、IN §8.7.5 範圍查驗結果與註記（§D-5）

**查驗結果**：**未載明適用範圍。** §8.7.5 現行文字之首二行為
「基準：CR30580/30581 參考本（TestResult 分頁）＋ SWC 0708 交付本。／
條文全文落檔於本節，台帳見 `RULINGS_LEDGER.md`。」—— 其後 (a)~(g)
與沿革皆為書寫形式之規定，**無一句界定其適用於哪些 feature**。

**惟排除機制已存在，故可一行表述（§F-3 未觸發）**：
FO §0 明文 `a feature profile's cited override wins over the generic rule here`，
而 `FW036_R1L_VehicleSetting_Profile.md:98` 已有
`## [OVERRIDE §8.7.5] 訊號書寫依 SWC 0708 交付本（R-VS52）`。
即：§8.7.5 事實上**已是「全域預設 + profile 可 override」**，只是未寫明。

**已寫入之一行（僅入 diff，待 Pei 裁）**：

```
**適用範圍**：全域預設；feature profile 之 cited `[OVERRIDE §8.7.5]` 勝出（FO §0）—— 現有 override：`vehicle_setting`（R-VS52／R-VS67，依 SWC 0708 交付本風格，不適用本節）。
```

置於 `#### 8.7.5` 標題之次行。IN 之 diff 為 **+1 / −0**，
除此一行外 IN 未動一字（§A）。

> **本層之附註**：`R-VS52`(`ec58cc91`) 之推翻段載「R-VS41(1)（採 canon §8.7.5
> v3 之 `$<MESSAGE>.<Signal>$` 形式）—— **撤回**」，且 `R-VS67`(`858768bb`)
> 進一步改由 LID 取名。故 override 之現行依據為**二條**，註記已並列。

---

## 七、`CANON_REFS_WAIVER.tsv`（§D-6）

**805 列 / 299 檔**，欄：`source line kind target reason`。

> **量測時點（FO §5a-10）**：waiver 於**本上繳包寫入後**產出。本檔自身位於
> `docs/fw036/upstream/`，其引用依裁定 2 為歷史檔，故計入 `historical-record`。
> 寫入前之值為 789 列 / 297 檔；本檔與其 16 處引用使 `historical-record`
> 由 509 升至 **525**，`active-backlog` **不變（279）**。
> **`active-backlog` 不變是本包之驗收點之一** —— 本包未新增任何活躍檔積壓。

| reason | 列 | 意義 |
|---|---|---|
| `historical-record` | **525** | `docs/fw036/{handoff,upstream}/`、`features/*/docs/{handoff,upstream}/` —— 裁定 2 之不追改對象 |
| `active-backlog` | **279** | 活躍檔之積壓，**暫時**豁免（§五-3 待裁）|
| `verbatim-ruling-text` | **1** | 見 §七-2 |

`RULINGS.sha.tsv` 與 waiver 皆入版控。

### 七-1 歷史檔之判準有一處實測缺陷（**本包自身之缺陷，已修**）

首版以**子串**比對 `docs/handoff/`／`docs/upstream/` 判歷史檔 ——
**`docs/fw036/upstream/` 不含子串 `docs/upstream/`**，
致 `docs/fw036/` 下之歷史包（22／23／23a／24 四檔，共 46 處）被誤分為
`active-backlog`。改以**路徑成分**（`{"handoff","upstream"} & set(Path(source).parts)`）
判定後，同一時點之 `historical-record` 由 463 升至 **509**，
`active-backlog` 由 325 降至 **279**（該二值為本上繳包寫入前所量）。

**攔下它的不是任何閘，是 `test_is_historical_classification` 之一行斷言**
（`assert cr.is_historical("docs/fw036/upstream/23a_wp1.md")`）。
該測試係依 G-K 為「已知案例須命中」而寫，寫時未預期它會抓到真缺陷。

### 七-2 一處 `verbatim-ruling-text` —— 界線案例，本層之處置與理由

```
docs/fw036/FEATURE_ONBOARDING.md:783  section §9  ambiguous
  R-G13：裁決條文集中於各 feature 之 RULINGS.md 與 canon §9，每條具穩定
```

該行在 R-G13 之**逐字條文區塊內**。裁定 2 令活躍文件改寫加前綴，
而**條文逐字不得改寫** —— 兩令於此相衝。

**處置**（同 R-G21 之既有形態）：條文本體不動，於其後加註
「本條條文中以『canon』加裸節號 9 所指者為 **FO §9**（本節）」，
該逐字行入 waiver，理由 `verbatim-ruling-text`。
工具以「落在 ``` 圍籬內且該檔為 canon」自動判此理由，非人工列舉。

**若 Pei 認為條文本體得為此改寫**（`canon §9` → `FO §9`），
則該 waiver 列可刪，理由類別亦可移除。**本層不自裁改條文。**

---

## 八、`canon_refs.py --waiver` 之三向實測（§D-8）

| 向 | 測試 | 判 |
|---|---|---|
| **waiver 內不紅** | `test_waived_ref_does_not_trip_gate` —— 同一引用無 waiver 時 exit 1、有 waiver 時 exit 0 | 綠 |
| **waiver 外同型仍紅**（R-G9 範圍向）| `test_same_shape_ref_outside_waiver_still_trips` —— 同一 target `canon §8.4` 換一檔即紅 | 綠 |
| **同檔新增一行仍紅**（只增不減之反面）| `test_new_line_in_waived_file_still_trips` | 綠 |
| **stale 只報不紅** | `test_stale_waiver_row_reported_not_failed` —— 引用已改寫加前綴後，該 waiver 列記 stale、exit 0 | 綠 |
| **waiver 檔不存在** | `test_missing_waiver_file_is_empty_not_error` —— 視為空清單，該紅仍紅 | 綠 |
| **理由分類** | `test_emit_waiver_covers_historical_and_classifies_reason`、`test_verbatim_ruling_text_inside_canon_fence`、`test_is_historical_classification` | 綠 |

`tests/test_canon_refs.py`：**38 項全綠**（23a 之 30 + 本包 8）。
`tests/test_rulings_hash.py`：**19 項全綠**（未改）。

---

## 九、實跑輸出

### 九-1 `canon_refs.py --waiver`

```
FO  docs/fw036/FEATURE_ONBOARDING.md
    節號 36，重複 0
    具條號索引之節 11，R-G 編號 21
IN  docs/runtime/ASPICE_SWE6_AI_Instruction.md
    節號 58，重複 0
    具條號索引之節 7，R-G 編號 0

兩 canon 共用之節號（裸引用即歧義）17 個：
['0','1','2','3','4','5','6','7','8','8.1','8.2','8.3','8.4','8.5','8.6','8.7','9']

掃描 1494 檔，引用 24507 處（qualified 3441／unqualified 21066）
  section    2104   unresolved    60   ambiguous   723
  item         81   unresolved     2   ambiguous    11
  ruling     1256   unresolved     0   ambiguous     0

waiver docs/fw036/CANON_REFS_WAIVER.tsv：805 列，本跑命中 805 處，stale 0 列

unresolved  = 0   （waiver 外）
ambiguous   = 0   （waiver 外）
unqualified = 21066   （盲區，不計入 FAIL）

PASS: unresolved + ambiguous = 0
```

**FO 節號重複由 4 降至 0**（整併前為 `['9','9.1','9.2','9.3']`）。
**FO 之 R-G 編號由 12 升至 21**（R-G13~R-G21 併入）。
**`ruling` 型 unresolved 由 125 降至 0**（§E 第 3 項之驗收數）。

### 九-2 `rulings_hash.py`

```
寫入 docs/fw036/RULINGS.sha.tsv：186 錨點（group 15／ruling 167／superseded 4），來源 2 檔
$ python3 scripts/rulings_hash.py --check
OK: docs/fw036/RULINGS.sha.tsv 與現行條文相符（186 條）   exit 0
```

**重複 ruling_id：8 組 → 0 組。** 錨點數 164 → 186
（+21 為 canon 之 R-G1~R-G21，+1 為 `RULINGS.md` 之永久對照表節被判 group）。

### 九-3 掃描條件揭露

- `canon_refs.py` 掃描面／排除／qualified 判準／盲區宣告：**同 23a §四，未變**
- 歷史檔判準：**已變**，由子串改為路徑成分（§七-1）
- `rulings_hash.py` 來源二檔（FO ＋ `vehicle_setting/RULINGS.md`），
  條文本體之雜湊定義同 23a §三，未變
- §E 第 4 項之 `canon §7.3`：**字面串**比對，不用詞界（該串含空白與 `§`，
  詞界不適用），排除 `.git/`／`archive/`／`sandbox/`

---

## 十、裁定 3 之對映表全文（§G）

**照原立條時序**（VF230 線八條於 `RULINGS.md` 之錨點行序）：

| 舊號 | 原錨點行 | slug | **新號** | 新號 sha8 |
|---|---|---|---|---|
| `R-VS59` | 1401 | VF230 之 B 欄序號自 238 起 | **`R-VF83`** | `9d5bfa4d` |
| `R-VS60` | 1430 | VF230 併入 `vehicle_setting`，不另開 feature | **`R-VF84`** | 見 tsv |
| `R-VS61` | 1449 | 素材補入由 Pei 執行 | **`R-VF85`** | 見 tsv |
| `R-VS62` | 1470 | `output/` 之證據位階 | **`R-VF86`** | 見 tsv |
| `R-VS63` | 1491 | 專案級 REF 素材得由 CFTS044 代用 | **`R-VF87`** | 見 tsv |
| `R-VS64` | 1620 | W 號改編追認 | **`R-VF88`** | 見 tsv |
| `R-VS65` | 1646 | W-115（DR 波及判定）之輸入改以 token 掃描 | **`R-VF89`** | 見 tsv |
| `R-VS66` | 1676 | Layer 2 決定前之前置複驗 | **`R-VF90`** | `a43f69b2` |

**同表已置入 `features/vehicle_setting/RULINGS.md` 檔首之
「VF230 線八條之永久編號對照」節**（R-VF45@`bea4bbb8` §三所令之永久對照表）。

### 十-1 本輪實際套用之範圍（21 處）＋ 未套用之範圍與理由

**已套用**：八個錨點標題（8）＋ 條文本體首行 id（8）＋
「編號待重編」註記改「已重編」（5，後三條原無該註記）= **21 處**。

**未套用**：共用簿之交叉引用（`ANOMALIES.md`／`CROSSLINE.md`／
`DATA_REQUESTS.md`／`docs/INDEX.md`／現行腳本常數）。**三個理由**：

1. **§E 之驗收數字只量錨點層**。第 7 項（重複組數 8→0）與第 8 項
   （R-VF 最大號 82→90）**皆已達標**，二者所量者即錨點
2. **R-VF45 §三 之永久對照表正是為此設計** —— 其原文
   「使歷史引用可解，而非可靠」。對照表已置入，交叉引用因而可解
3. **誤傷風險為實測所得，非顧慮**。W-VF39 已具名鑑別錨點
   （`docs/handoff/64_review_round40.md`：Part 1 檔名而引用 VF230 線）。
   本輪自身亦撞到同型：`RULINGS.md:1402` 之
   `> ⚠ 本條屬 VF230 線，與主線同號者為不同條文（R-VS63）` ——
   該 `(R-VS63)` 指的是 **1702 行之「編號分線」條（64 包 §4，CFTS044 線）**，
   **不是**同段之 VF230 線 R-VS63。**範圍取代會把它改錯。**
   故本輪逐錨點改，不做範圍取代

**已交付件一律未動**：`generated/*.json`（TC 語料）與 `data/*.json` 之
`R-VS59`–`R-VS66` 字面全數保留（§A、23 包 §A）。
實測該二類共 **~2500 處**，若改則屬改動已交付件。

**副作用（有利）**：改編後 `R-VS59`–`R-VS66` 於 `RULINGS.md` 各只剩一個
定義（CFTS044 本線），**該八號之引用因而不再歧義** —— 不動它們反而正確。

---

## 十一、本包引用之裁決（R-G13 回報格式首次適用，§G）

`ruling_id | 下放引用 sha8 | 實讀 sha8 | 判`。
下放包 24 以編號引用而未附 sha8（其成文時 canon 側條文尚無 sha），
故該欄標 `pre-merge`；**canon 側 R-G13~R-G21 之 sha8 為本包併入後首次產生**。

| ruling_id | 下放引用 sha8 | 實讀 sha8 | 判 |
|---|---|---|---|
| `R-G5` | pre-merge | `9814d24c` | 首產 |
| `R-G9` | pre-merge | `d4f630f0` | 首產 |
| `R-G12` | pre-merge | `eabe2726` | 首產 |
| `R-G13` | pre-merge | `abdc56e3` | 首產 |
| `R-G14` | pre-merge | `fb508d10` | 首產 |
| `R-G15` | pre-merge | `2aa0c28f` | 首產 |
| `R-G16` | pre-merge | `2ec55d94` | 首產 |
| `R-G17` | pre-merge | `24cdeec6` | 首產 |
| `R-G18` | pre-merge | `8f61f9fd` | 首產（§C 修訂版）|
| `R-G19` | pre-merge | `bd206972` | 首產 |
| `R-G20` | pre-merge | `3d0cd37b` | 首產 |
| `R-G21` | pre-merge | `1230e795` | 首產 |
| `R-VF10` | pre-merge | `518224a5` | **實讀** |
| `R-VF18` | pre-merge | `0512f0d1` | **實讀** |
| `R-VF21` | pre-merge | `d0fa5fe2` | **實讀** |
| `R-VF28` | pre-merge | `309642af` | **實讀** |
| `R-VF45` | pre-merge | `bea4bbb8` | **實讀**（其 §一 本包加註，sha 為加註後之值）|
| `R-VS52` | pre-merge | `ec58cc91` | **實讀** |
| `R-VS67` | pre-merge | `858768bb` | **實讀** |
| `R-VF83` | —（本包新編）| `9d5bfa4d` | 改編後首產 |
| `R-VF90` | —（本包新編）| `a43f69b2` | 改編後首產 |

**無不符項。** 下放包未附任何 sha8，故無可比對之不符 ——
**本欄之價值自下一包起顯現**（下放包引 `R-G18@8f61f9fd`，本層讀到不同值即停）。

其餘引用（無條文本體、故無 sha）：`G-D`、`G-K`、`G-N`、`A-VF10`、`A-VS02`、
`R-TM13`、`FO §0`、`FO §8.2`、`FO §8.3`、`FO §5a-11`、`FO §5a-16`、
`FO §9.1 第 10 項通則`、`V04 §3.1`、`W-VF39`、
23 包 §A／§B／§C／§D、23a §三／§四／§五／§六、24 包 §A～§H。

---

## 十二、本包之產物

| 檔 | 動作 | 行數 |
|---|---|---|
| `docs/fw036/FEATURE_ONBOARDING.md` | **修改** +356/−86 | 809 → **1079** |
| `docs/runtime/ASPICE_SWE6_AI_Instruction.md` | **修改** +1/−0（待裁）| 811 |
| `features/vehicle_setting/RULINGS.md` | **修改** +59/−21 | 5033 → **5071** |
| `docs/fw036/templates/{DECISIONS.md,PLAYBOOK.md,feature.yaml}` | **修改** 前綴 7 處 | —— |
| `docs/fw036/CANON_REFS_WAIVER.tsv` | **新增**，入版控 | 806（含表頭）|
| `docs/fw036/RULINGS.sha.tsv` | **重產** | 187（含表頭）|
| `scripts/canon_refs.py` | **修改**（`--waiver`／`--emit-waiver`）| 286 → **400** |
| `tests/test_canon_refs.py` | **修改**（+8 項）| 248 → **344** |
| `docs/fw036/upstream/24_wp1_continuation.md` | **新增**（本檔）| —— |

### 十二-1 sha256（Pei 覆核 diff 時之基準）

```
ff3267899d6c709e47bf4e7774890b5fb697ff711c22fddd11f8a2cadd63f81f  docs/fw036/FEATURE_ONBOARDING.md
61ccd5e5fd02dde9be5647a0c22ca6ee73e6e899456056a4caf86b203fe605d8  docs/runtime/ASPICE_SWE6_AI_Instruction.md
d95c6b2449565b45edd9ff0732febb021c010b518e680c0ff204e7fc3455b149  docs/fw036/RULINGS.sha.tsv
2275d013dbed9b2247846e50a773d1fe6aa64bd4f500b816764610100cd6edee  docs/fw036/CANON_REFS_WAIVER.tsv
763828422dd9085f50e4bbdb0f02ad554ee490012a00500b231f8b40b7cbdc98  features/vehicle_setting/RULINGS.md
```

**IN 之新 sha256 為 `61ccd5e5…`（sha8 `61ccd5e5`）** —— 依 R-G20@`3d0cd37b`，
Project 指令副本須改載此值。23a §六所報之 `526656df` **已因本包之一行註記失效**。
**若 Pei 於 diff 過目時退掉該行，IN 之 sha 回復為 `526656df`** ——
**re-sync 前請先確認該行之去留**，否則 Project 副本又載到一個已不存在之值。

### 十二-2 建議之 commit（Pei 執行，pathspec 明列，R-G12@`eabe2726`）

```
git add docs/fw036/FEATURE_ONBOARDING.md \
        docs/runtime/ASPICE_SWE6_AI_Instruction.md \
        docs/fw036/templates/DECISIONS.md \
        docs/fw036/templates/PLAYBOOK.md \
        docs/fw036/templates/feature.yaml \
        docs/fw036/CANON_REFS_WAIVER.tsv \
        docs/fw036/RULINGS.sha.tsv \
        features/vehicle_setting/RULINGS.md \
        scripts/canon_refs.py tests/test_canon_refs.py \
        docs/fw036/upstream/24_wp1_continuation.md

git commit -- docs/fw036/FEATURE_ONBOARDING.md \
        docs/runtime/ASPICE_SWE6_AI_Instruction.md \
        docs/fw036/templates/DECISIONS.md \
        docs/fw036/templates/PLAYBOOK.md \
        docs/fw036/templates/feature.yaml \
        docs/fw036/CANON_REFS_WAIVER.tsv \
        docs/fw036/RULINGS.sha.tsv \
        features/vehicle_setting/RULINGS.md \
        scripts/canon_refs.py tests/test_canon_refs.py \
        docs/fw036/upstream/24_wp1_continuation.md
```

commit message：

```
feat(fw036): consolidate canon section 9 and land R-G13..R-G21

Two `## 9.` sections merged into one; R-G1..R-G12 given a single landing
point with per-clause anchors, and their two divergent one-line summaries
reconciled with the discrepancies recorded in FO 9.8.2. R-G13..R-G21 land
in FO 9.2, with 8.1 / 8.8 / 1.2 amended accordingly. Canon references now
carry FO/IN prefixes; the existing backlog is enumerated in
CANON_REFS_WAIVER.tsv and gated by canon_refs.py --waiver. The eight
VF230-line rulings R-VS59..R-VS66 are renumbered R-VF83..R-VF90.
```

---

## 十三、獨立判斷 —— 本包是否仍有該驗而未驗者

1. **`unqualified` 21066 處仍未抽樣判讀。** 23a §八-4 已列此項，本包未做。
   其中「實指 canon 而未加前綴」之比例，即 §五-3 選項 (a) 之真實工作量分母 ——
   **279 處只是「已被判為 qualified 而不可解析」者，不是積壓之全集**（R-G11）。
2. **`item` 型仍只驗 81 處**（23a §八-3 之盲區未變）。FO 具條號索引之節由
   10 升至 11（§9.2 之 R-G 導覽表被判為條號索引），**該升值為副作用而非設計** ——
   `| R-G1 |` 型表列被 `RE_TABLE_N` 讀成條號 1。**不影響判定**（§9.2 無
   「第 N 條」形式之引用），但其為誤讀，記於此。
3. **`GATES.tsv`（R-G17）尚未存在**，故 R-G21 之自查表對映無處可落 ——
   其為 W-P3 §2 之題，本包不先行。
4. **R-G14 綠色通道尚未有生效起點之裁定**（23 包 §I-3 之開放事項）。
   §8.8 已加註「除 R-G14 生效期間」，但**該期間何時開始未定** ——
   現況等同未生效。
5. **兩支工具仍未在 CI 中執行**（23a §八-5 未變）。`--check` 與 `--waiver --gate`
   現皆依賴人為執行；接入點屬 W-P2 §3 之題。
6. **§9 整併未驗「外部引用讀新號會不會讀錯」**。本包驗了內容保存（§三-2）
   與節號唯一（§九-1），**但未逐處驗證歷史檔中之 `§9.1`／`§9.2`／`§9.3`
   引用經 §9.8.1 對映表後是否確實可判**。抽驗 0 處。
   **若要驗，其形式應為：自 waiver 取 §9.x 之歷史引用若干，逐處讀其上下文，
   判對映表是否足以定其實指。** 本包未做。
7. **`R-VF45` 之 sha 因本包加註而變。** 若有他處以 `R-VF45@bea4bbb8` 之前值
   引用，該引用將不符 —— **本包為 sha 首產，故無此情形**，但這是 R-G13
   生效後每次改動條文（含加註）都會發生之形態，**尚無處置條文**：
   加註是否算「改動條文」？**建議 Pei 於下包裁定**。
