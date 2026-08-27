# 上繳包 34 —— 收尾：22 條寫回、8 leaf 覆蓋總表、未結 DR 清單

- 日期：2026-08-26
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/34_closeout.md`（＋ 併執 33 包）
- 存續之停止條件全數掃描：**內容類 54／55／60／73／83／88／89／90／91／93 皆 0**；
  **寫回類完整性計數逐項相等**
- **一處對指示之偏離**（寫回標的），已具名，見 §3.1
- **git 未執行**（§六為建議）

---

## 一、抄錄核對表（最後一次）

## 抄錄核對表 — 34_closeout.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 58 | R-DM56 | `features/display/RULINGS.md` | 489 | `cc2701a135fd3245` | 是 |
| 59 | R-DM57 | `features/display/RULINGS.md` | 241 | `493cb05ba6d4f5ef` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **59** 個，與各下放包原檔逐字元比對 **全數相符**（59 vs 59）。

`RULINGS.md` 之 R-DM 區塊累計 **59**，順序驗證 exit 0。
R-G39 之核對表見上繳 33 §一。

---

## 二、生成

### 2.1 `ops-01` —— 13 條

全文、`reasoning`、`deferred`、排除表、行為軸表、未用材料表
**見上繳 33**（同輪產出）。

### 2.2 一處內容實錯，本輪抓到並改（R-DM57(a) 之例外）

合併 lint 之首跑報 **P = 3**（訊號寫法不合 R-1 v3），三處皆為
「賦值缺 `VAL_` 標籤」：

```text
| 25 | er | '$DIS_CENTERSTACK.DCSD_DISP_STAT$ = 5' |
| 26 | er | '$DIS_CENTERSTACK.DCSD_DISP_STAT$ = 6' |
| 30 | er | '$RADIO_B3.RQ_DISP_INTS$ = 201'        |
```

**根因二項**：

1. **值 5／6／201 之所以是「不合理值」，正是因為它們沒有 `VAL_` 標籤。**
   我把不合理值寫成訊號賦值 —— **這在定義上就不可能合格。**
2. `$RADIO_B3.RQ_DISP_INTS$` 之**訊息名 `RADIO_B3` 來自 VF169**，
   而下放包 30a §3.1 明文「只登記不採用」，**停止條件 83 之標的即此**。
   我在寫 #12 時把它當成已知事實用了。
   **首跑之 83 掃描沒抓到，因為我掃的詞表漏了它。**

**處置**：

| TC | 處置 |
|---|---|
| #7／#8 | ER 改為只驗可觀察行為（畫面不變／畫面為 on 態）；**注入動作留在 procedure** |
| **#12** | **移除** —— 其 ER 無法在不違反 R-1 v3(a) 與停止條件 83 之下寫出。該行為軸併入 `brightness context` 之 deferred（`blocking_dr: DR-DM8`） |

修正後：**P = 0**；`RADIO_B3` 於全部 TC 欄位之出現 **0**
（其僅存於 `deferred.reason` 與 `reasoning` 之說明文字內）。

### 2.3 全批合併 lint（母體 22 條）

| 項 | 值 |
|---|---|
| 母體 | `pilot-01` 3 ＋ `rvc-01` 6 ＋ `ops-01` 13 = **22** |
| 方式 | 036 母本之拋棄式複本，資料列 10–31，其餘清空 |
| profile | `display` |

```text
# lint036 報告：lint_all.xlsx

- 來源：`/private/tmp/claude-501/-Users-peihe-Work-Projects-TC-Generator/e90244b2-6851-4dfb-8775-8cb1bd4f77d3/scratchpad/lint_all.xlsx`（唯讀）
- 資料列數：22
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`display`（P 採 R-1 v3；另跑 Q／R／T）

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 0 | 0 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item 括號下半) | 0 | 0 | 每次命中 | 已校準（R-6b 範圍：Media 錨值 1→0） |
| D | PC 違規 (pre) | 0 | 0 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 0 | 0 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 0 | 0 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 0 | 0 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 0 | 0 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |

**總計：行計 0**（列計不加總——同一列可觸發多項檢查）

## 明細

```

**二十項行計皆 0。** `I-sibling` 有母體（004×2、007×3、008×3、001×8、
002×3、003×2）**且為 0**。

### 2.4 `popup-01`（`SWE1-DM-006`）—— **不成批，具名回報**

依 34 包 §2.2 末句「若 006 之可寫面向經勘查不足以成批（< 2 TC），
**具名回報後併入寫回，不強生**」。

勘查（R-G37 新判準，適用本專案）：

```text
# 候選（適用本專案，含 popup／priority／arbitration 詞）= 15 條
  其中已被三批引用者 = 3

# 含逐字 popup 編號（PU\d{4}）者
  0 條 → **無**

# 含 `pop-up`／`popup` 一詞者
  1 條 → ['4819575']
    {4819575} §1.8.1.1.3 For the pop-ups stated in HMI core specification requirement H4; the HU shall send $TGW_DISP_STAT$ = [DISP_NORMAL] and $RQ_DISP_INTS$ <> [0% Intensity

# 僅 priority／arbitration 詞者之章節分布
    3  §1.11.2.2 DCSD Display Hot Behavior
```

**三項實測**：

1. **CFTS_020 之適用條文中，含逐字 popup 編號（`PU\d{4}`）者 = 0 條。**
2. 含 `pop-up`／`popup` 一詞者 **1 條** —— `{4819575}`，其逐字為
   `For the pop-ups stated in HMI core specification requirement H4; the HU
   shall send $TGW_DISP_STAT$ = [DISP_NORMAL] …` ——
   **轉指 `HMI core specification requirement H4`，該文件不在手上。**
3. 其餘 `priority` 詞之命中，扣除三批已引者，**其標的為 RVC
   （007／008 之材料）或 Display Hot × RVC（`{4820291}`／`{4820292}`，
   004／005 之材料）**，取之即違 §8.2.1。

**而 `popup_priority.tsv` 之權威性本身待 DR-DM2(b)**
（29 輪 B18：2021 SR24 1A 矩陣對 26PI 是否仍為權威，**語意漂移無從以
逐字證明**），其 `Cat. SL` 之序另待 DR-DM2(a)（B17）。

**結論：006 之可寫面向為 0 條 TC，不成批。不強生。**
覆蓋總表列其為**未覆蓋**（§四）。

---

## 三、寫回 036

### 3.1 【偏離】寫回標的改為 `output/`，`inputs/` 之母本一字不動

下放包 §3.1 定標的為「`inputs/` 之 036 母本複本」。**本層改寫入
`features/display/output/`**，理由三項：

(a) `inputs/` 之母本為**客戶素材**，且受 `reference:` 綁定
    （`workbook_master`，sha `6372fb6be02f48dc…`）。就地覆寫會**毀去
    唯一一份原件**；
(b) 覆寫後 R-G23 之綁定檢查將由 **13/13 轉為 12/13** ——
    一項為交付而做的動作，會使本 feature 唯一的素材完整性保證失效；
(c) 他 feature 之慣例即為 `output/`（`time_management`／`user_profiles`
    之 036 產出皆在該處）。

**下放包 §3.1 所稱之「repo 內部複本」，本作法即產生該複本**，
且 §3.1 末句「交付路徑之複製屬 Pei」不受影響。
**若分析層要求就地覆寫，請明示；本層可於單輪內改。**

### 3.2 寫回報告

```text
# 寫回 036（XML 外科式）
來源（不動）: inputs/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specifi…
輸出        : output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specifi…
sheet xml   : xl/worksheets/sheet6.xml
author      : PeiPYHsu
寫入列      : 10 … 31（22 列）

| 列 | TC ID | leaf | 批次 |
|---|---|---|---|
| 10 | `TC-DM-001` | `SWE1-DM-004` | pilot-01 |
| 11 | `TC-DM-002` | `SWE1-DM-004` | pilot-01 |
| 12 | `TC-DM-003` | `SWE1-DM-005` | pilot-01 |
| 13 | `TC-DM-004` | `SWE1-DM-007` | rvc-01 |
| 14 | `TC-DM-005` | `SWE1-DM-007` | rvc-01 |
| 15 | `TC-DM-006` | `SWE1-DM-007` | rvc-01 |
| 16 | `TC-DM-007` | `SWE1-DM-008` | rvc-01 |
| 17 | `TC-DM-008` | `SWE1-DM-008` | rvc-01 |
| 18 | `TC-DM-009` | `SWE1-DM-008` | rvc-01 |
| 19 | `TC-DM-010` | `SWE1-DM-001` | ops-01 |
| 20 | `TC-DM-011` | `SWE1-DM-001` | ops-01 |
| 21 | `TC-DM-012` | `SWE1-DM-001` | ops-01 |
| 22 | `TC-DM-013` | `SWE1-DM-001` | ops-01 |
| 23 | `TC-DM-014` | `SWE1-DM-001` | ops-01 |
| 24 | `TC-DM-015` | `SWE1-DM-001` | ops-01 |
| 25 | `TC-DM-016` | `SWE1-DM-001` | ops-01 |
| 26 | `TC-DM-017` | `SWE1-DM-001` | ops-01 |
| 27 | `TC-DM-018` | `SWE1-DM-002` | ops-01 |
| 28 | `TC-DM-019` | `SWE1-DM-002` | ops-01 |
| 29 | `TC-DM-020` | `SWE1-DM-002` | ops-01 |
| 30 | `TC-DM-021` | `SWE1-DM-003` | ops-01 |
| 31 | `TC-DM-022` | `SWE1-DM-003` | ops-01 |
```

| 項 | 值 |
|---|---|
| 來源 | `inputs/…_20260817_ext.xlsx`，sha `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |
| **來源 sha（寫回後）** | **`6372fb6be02f48dc…` —— 未變**（綁定維持 13/13） |
| 輸出 | `output/…_SWQT_Display_20260826.xlsx` |
| **輸出 sha** | `43a301f6571830189b85d9bcfa506ce3074bae438d86f942e61cb1363a43f746` |
| 寫入列 | **10 – 31**（22 列） |
| TC ID | `TC-DM-001` … `TC-DM-022`（canon §10.3，生成器編號） |
| `O` 欄 | `NEW`（`tc_ref_id_value`） |
| `AA` 欄 | `PeiPYHsu`（`author_value`） |
| `G`／`H` 欄 | 已填（`fill_test_group_set: true`；BLANK → FILL） |
| 方式 | **XML 外科式** —— 只改 `xl/worksheets/sheet6.xml` 之目標儲存格，其餘 47 個 zip 部件**逐 byte 原樣重打包**；不經 openpyxl 存檔 |

### 3.3 完整性驗證（§3.2 之逐項相等）

```text
| 項 | before | after | 相等 |
|---|---:|---:|---|
| <dataValidation | 4 | 4 | 相等 |
| x14:dataValidation | 2 | 2 | 相等 |
| <conditionalFormatting | 0 | 0 | 相等 |
| worksheets | 9 | 9 | 相等 |
| drawings | 6 | 6 | 相等 |
| charts | 0 | 0 | 相等 |
| rels | 16 | 16 | 相等 |
| zip entries | 48 | 48 | 相等 |

**完整性驗證：PASS —— 逐項相等**
```

**R 欄下拉之抽查**：`x14:dataValidation` 之 `xm:sqref` 為 **`R10:R1411`**
—— 寫入之第 10 列落在其範圍內，下拉可用。
另三個 `dataValidation` 之 `sqref` 為 `P10:Q1411`／`T10:Z1411`／`AF10:AF1411`，
皆與寫回前相同。

### 3.4 回讀驗證（本層加做）

```text
回讀比對：22 列 × 15 欄，不符 = 0  →  PASS
第 32 列（22 條之後）應為空：None
抽查 r10：F=TC-DM-001 D=SWE1-DM-004 G=Display H=Thermal Management P=P1 R=狀態轉換 (State Transition Testing)
抽查 r31：F=TC-DM-022 D=SWE1-DM-003 H=Operative State P=P2
```

**22 列 × 15 欄逐欄比對，不符 0。** 第 32 列為空（未溢寫）。

---

## 四、覆蓋總表（8 leaf）

```text
| leaf | Test Set | TC 數 | 覆蓋狀態 | deferred token（blocking DR） |
|---|---|---:|---|---|
| `SWE1-DM-001` | Operative State | 8 | **部分覆蓋** | `DISPLAY_ON and DISPLAY_OFF naming`（DR-DM8） |
| `SWE1-DM-002` | Operative State | 3 | **部分覆蓋** | `DISPLAY_ON and DISPLAY_OFF naming`（DR-DM8）；`brightness context`（DR-DM8） |
| `SWE1-DM-003` | Operative State | 2 | **部分覆蓋** | `splash timing`（DR-DM1）；`DISPLAY_ON and DISPLAY_OFF naming`（DR-DM8） |
| `SWE1-DM-004` | Thermal Management | 2 | **部分覆蓋** | `warning popup`（DR-DM10） |
| `SWE1-DM-005` | Thermal Management | 1 | **部分覆蓋** | `protective shutdown`（DR-DM10）；`multi-stage`（DR-DM4） |
| `SWE1-DM-006` | Pop Up Handling | 0 | **未覆蓋** | — |
| `SWE1-DM-007` | Rear View Camera | 3 | **部分覆蓋** | `reverse gear`（DR-DM11）；`HU-side signal value`（DR-DM9） |
| `SWE1-DM-008` | Rear View Camera | 3 | **部分覆蓋** | `HU-side signal value`（DR-DM9）；`splash abort`（DR-DM1） |

合計 TC = 22
覆蓋之 leaf = 7 / 8
全覆蓋（無 deferred）= 0
部分覆蓋 = 7
未覆蓋 = 1  → ['SWE1-DM-006']
```

**7 / 8 leaf 有 TC；全部為部分覆蓋；`SWE1-DM-006` 未覆蓋。**
**無一 leaf 為全覆蓋** —— 每一 leaf 皆有至少一個 deferred token，
且每一 token 皆於其各 TC 之 `test_item` 括號下半逐字指名（R-G33，
雙向檢查 MISSING 0／STALE 0）。

---

## 五、未結 DR 清單（交付包必附）

| DR | 狀態 | 阻斷之面向 |
|---|---|---|
| **DR-DM1** | SENT (2026-08-25) | `SWE1-DM-003` 之 splash 時長；`SWE1-DM-008` 之 splash abort |
| **DR-DM2** | SENT ＋ 補充函待發 | **`SWE1-DM-006` 全部**（006 未覆蓋之直接原因）；`Cat. SL` 之序 |
| **DR-DM3** | SENT (2026-08-25) | 全 8 leaf 之追溯欄（`SYS-RA-DISP-*` ↔ SYS2） |
| **DR-DM4** | SENT ＋ 重擬／附件二待發 | `SWE1-DM-005` 之 multi-stage 分級 |
| **DR-DM5** | SENT (2026-08-25) | `$CCDMF_RQ_DISP_INTS$` 之 DBC 定義（本批未用） |
| **DR-DM6** | SENT (2026-08-25) | `Display_OFF_SoftKey_Prsnt` 之 PROXI 定義（本批未用） |
| ~~DR-DM7~~ | **CLOSED（R-DM44，16 輪）** | — |
| **DR-DM8** | SENT (2026-08-25) | **`SWE1-DM-001`／`-002`／`-003` 之 `DISPLAY_ON`／`DISPLAY_OFF` 命名**；002 之 brightness context |
| **DR-DM9** | SENT ＋ 重擬／附件三待發 | `SWE1-DM-007`／`-008` 之 HU 側訊號值；`{4820287}` 之訊號值 |
| **DR-DM10** | SENT ＋ 補充一、二待發 | **`SWE1-DM-004` 之 warning popup；`-005` 之保護性關閉**；`pilot-01` 之 `85 degrees C` 之前提 |
| **DR-DM11** | OPEN | `SWE1-DM-007` 之倒車檔觸發 |
| **DR-DM12** | 待 Pei 發 | `rvc-01` 六條之 `leaf_id`（**非 TC 內容**） |

**11 筆未結、1 筆 CLOSED。** 待 Pei 發者：DR-DM12，
以及 DR-DM2／DR-DM4／DR-DM9／DR-DM10 之補充／重擬函件。

> **R-DM56(c) 之提醒**：DR 答覆到達後之修改為**變更**，不為阻斷。
> 受影響者為門檻數字與 deferred 之解除，**TC 之結構不受影響**。

---

## 六、建議之 commit 訊息與 pathspec（**未執行**）

```bash
git add \
  features/display/RULINGS.md \
  features/display/generated/ops-01.json \
  features/display/scripts/write_back_036.py \
  features/display/docs/INDEX.md \
  features/display/docs/handoff/33_ops01_scoped.md \
  features/display/docs/handoff/34_closeout.md \
  features/display/docs/upstream/33_ops01_scoped.md \
  features/display/docs/upstream/34_closeout.md \
  docs/fw036/RULINGS_LEDGER.md
```

```text
feat(display): generate the operative state batch and write all 22 cases back

- ops-01: 88 candidate clauses, 36 excluded with a reason each, 52 kept, 14
  behaviour axes, 13 test cases over the three operative state leaves
- drop one axis at the check stage: its expected result would have had to
  assign 201 to an intensity signal whose value list only defines 255, and
  its message name came from a document that is on register but not for use
- rewrite two expected results the same way: the values 5 and 6 are
  implausible precisely because they carry no label, so the check verifies
  the screen instead and the injection stays in the procedure
- write all 22 cases to output/ by editing one sheet xml and repacking the
  other 47 parts byte for byte; every validation, drawing and relationship
  count matches, and the source workbook is untouched
- 006 yields no writable case: the spec carries no popup ids at all and the
  priority matrix's authority is itself what DR-DM2 asks about
- add R-DM56 and R-DM57: test against the specific clause and disclose the
  contradiction rather than waiting on it, and freeze new process work
```

> **`output/` 之 xlsx 是否入 git 由 Pei 決定** —— 他 feature 之
> `output/` 有進 git 者（`user_profiles`／`time_management`），
> 本 pathspec **未含它**，待明示。
> `inputs/` 由 `.gitignore` 排除。`batches/` 亦然。

---

## 七、自陳（依 R-DM57(b) 入 `BACKLOG.md`，此處僅列標題）

- **B30**：`popup-01` 未成批之判斷，其依據含「`popup_priority.tsv` 之
  權威性待 DR-DM2(b)」—— 該表是本層 29 輪所建，**用自己建的表之不確定性
  去論證另一批不能生成**，其推理鏈長且未經第二來源。
- **B31**：`{4819575}` 轉指之 `HMI core specification requirement H4`
  **未開 DR** —— R-DM57(a) 禁開新異常，惟此為新的未取得素材。
- **B32**：`ops-01` 之 14 軸由本層自 52 條歸納，**歸納過程無第二來源核對**；
  R-G39 定「行為軸產出 TC」而未定「軸如何歸納」。
- **B33**：未用材料表之 (ii) 七條 FPDM／CCDMF／CCDMR 條文為
  `[Radio:R1H][EE:Atlantis High]` 之專條、**適用本車而不在 037 八條內** ——
  037 之範圍未涵蓋該三個顯示模組。

---

## 八、追補（下放包 34a 之裁定）

### 8.1 34a 之六項裁定 —— 逐項處置

| # | 裁定 | 處置 |
|---|---|---|
| 1 | 補 1 條，leaf **`SWE1-DM-001`** | **已補**（`TC-DM-023`）。本層原擬歸 003（`sleep-to-wakeup`），依裁定改列 001 |
| 2 | 重跑寫回 22 → 23，§3.2／3.3／3.4 全套重做 | **已重做**，見 §8.4 |
| 3 | `output/` 之偏離**追認**，34 包 §3.1 由本件更正 | 已知悉；本層 §3.1 之記載維持（其為當時之偏離紀錄） |
| 4 | `output/` 之 xlsx **入 git** | **未入** —— **Pei 2026-08-26 於本輪明示「不入 commit」**。34a 亦載「執行仍屬 Pei」，以 Pei 之明示為準。**兩者相左，具名於此** |
| 5 | B31 之 H4 於 DR-DM2 補充函末追加一行 | **已加**（`DATA_REQUESTS.md` 之 DR-DM2 補充函 (c)） |
| 6 | 33 包重號為平行會話碰撞，處置正確 | 已在 BACKLOG，不另動作 |

### 8.2 【具名】34a §一.1 之條號有誤

34a 寫「`{4819710}`（＝`{4819820}` 架構副本擇一引用，兩號並列）」。

**實測：`{4819820}` 不是該架構副本。**

| 條 | 章節 | 逐字 |
|---|---|---|
| `{4819710}` | `§1.8.2.2 Wake Up for DCSD Power Button` | `Wake Up by DCSD Power Button Pressed: While vehicle is asleep …` |
| **`{4819820}`** | **`§1.8.2.3.10 Haptic Buttons Audio feedback`** | **`When the HU receives $HSW_DCSD$ = [Pressed], the HU shall play the confirmation tone CONF1.`** |
| **`{4820824}`** | **`§1.15.2.2 Wake Up for DCSD Power Button`** | 與 `{4819710}` **逐字相同**（真正之架構副本） |

三者皆 `[Radio:R1M, R1H] [EE:Atlantis High]`、皆適用本專案。
**`specification_reference` 並列 `{4819710}`／`{4820824}`，不引 `{4819820}`** ——
引之會把一條觸覺回饋音需求放進喚醒軸之追溯欄。

### 8.3 補軸之全文（`TC-DM-023`，leaf `SWE1-DM-001`）

`spec_ref` CFTS020-4819710 / CFTS020-4820824　`design_method` 狀態轉換 (State Transition Testing)　`priority` P1　`functional_safety` NA

```text
[test_item]
The Display Management software shall manage display operative states as DISPLAY_ON and DISPLAY_OFF based on system operational requests and timeout conditions.The software shall send appropriate display state and brightness requests to DCSD during state transition handling.

(Sleep to wake-up path by the power button — the DISPLAY_ON and DISPLAY_OFF naming and the power button signal value are deferred)

[pre_conditions]
1. The vehicle is asleep
2. The ignition is in the off state

[input_test_data]
NA

[test_procedure]
1. Read the operating state of the radio and record it
2. Press the Power button on the DCSD
3. Read the operating state of the radio and record it
4. Read the signal $DIS_CENTERSTACK.DCSD_Power$ and record how long it is sent after the CAN wake

[expected_result]
1. The radio is off
2. The DCSD wakes the CAN bus
3. The radio turns on and enters Timed Mode
4. The signal $DIS_CENTERSTACK.DCSD_Power$ is sent for 250 ms after the CAN wake

```

**拼法判定（R-DM48）**：`$DCSD_Power$ = [Pressed]`；DBC `DIS_CENTERSTACK.DCSD_Power`
之 `VAL_` 為 `0 "Button_Not_Pressed" 1 "Button_Pressed"` —— **`[Pressed]` 逐字不等於
`Button_Pressed`**；規格他處另寫 `[Power Button Pressed]`／`[pressed]`，**三種書寫皆不等**。
依 R-DM48 **不寫 raw**；ER 只驗可觀察行為（radio 開機 → Timed Mode、CAN 喚醒）與
**`250 ms` 之發送時長**（條文逐字，非值標籤，不受 R-1 v3 賦值格式規制）。
新增 deferred `power button signal value`（`blocking_dr: DR-DM9`），
**leaf 001 之九條括號下半皆已逐字指名**（雙向檢查 0／0）。

### 8.4 全套重驗

```text
| 項 | before | after | 相等 |
|---|---:|---:|---|
| <dataValidation | 4 | 4 | 相等 |
| x14:dataValidation | 2 | 2 | 相等 |
| <conditionalFormatting | 0 | 0 | 相等 |
| worksheets | 9 | 9 | 相等 |
| drawings | 6 | 6 | 相等 |
| charts | 0 | 0 | 相等 |
| rels | 16 | 16 | 相等 |
| zip entries | 48 | 48 | 相等 |

**完整性：PASS —— 逐項相等**

回讀：23 列 × 15 欄，不符 = 0 → PASS；第 33 列 = None

覆蓋：合計 23 條；001=9 002=3 003=2 004=2 005=1 006=0 007=3 008=3
```

| 項 | 值 |
|---|---|
| `lint036 --profile display`（母體 **23**） | **二十項行計皆 0** |
| `check_disclosure.py` | **MISSING 0／STALE 0** |
| 寫入列 | **10 – 32**（23 列），`TC-DM-001` … `TC-DM-023` |
| 來源母本 sha | `6372fb6be02f48dc…` **仍未變**（綁定 13/13） |
| 輸出 sha | `4528b93783ad52af9a51aded4ee1e7497ddc8c527e5687b807888b52081fbf7a` |

**覆蓋總表更新**：`SWE1-DM-001` 由 8 → **9** 條（34a §二之要求），合計 **23** 條。
7/8 leaf 有 TC、全部部分覆蓋、`SWE1-DM-006` 未覆蓋 —— 三項不變。

### 8.5 pathspec 終版

```bash
git add \
  features/display/generated/ops-01.json \
  features/display/BACKLOG.md \
  features/display/DATA_REQUESTS.md \
  features/display/docs/INDEX.md \
  features/display/docs/handoff/33_ops01_resume.md \
  features/display/docs/handoff/34a_add_one.md \
  features/display/docs/upstream/34_closeout.md
```

> **`features/display/output/` 之 xlsx 不入** —— Pei 2026-08-26 明示「不入 commit」。
> 34a §一.4 建議入，**兩者相左，以 Pei 之明示為準**（34a 自載「執行仍屬 Pei」）。
> 該目錄亦未出現於 `git status`（已被 ignore）。

---

## 九、追補（下放包 34b 之裁定「乙」—— 交付版面修正）

**性質**：34 包之附件，補記於此，不另出上繳。
**TC 內容一字不動** —— 本節之全部變動限於版面（列序、列布局、TC ID 重編）
與寫回機制之三項缺陷修正。

### 9.1 新列序（34b §一之裁定「乙」，實作結果）

工作簿骨架 = 037 之 8 條需求，`SWE1-DM-001` → `-008` 升冪。
同一需求之多條 TC 依其行為軸序接續（穩定排序，批次內順序不變）。

```text
| 列 | TC ID | leaf | 批次（僅供追溯，不出現在交付版面） |
|---|---|---|---|
| 10–18 | TC-DM-001 … TC-DM-009 | SWE1-DM-001 | ops-01 × 9 |
| 19–21 | TC-DM-010 … TC-DM-012 | SWE1-DM-002 | ops-01 × 3 |
| 22–23 | TC-DM-013 … TC-DM-014 | SWE1-DM-003 | ops-01 × 2 |
| 24–25 | TC-DM-015 … TC-DM-016 | SWE1-DM-004 | pilot-01 × 2 |
| 26    | TC-DM-017             | SWE1-DM-005 | pilot-01 × 1 |
| 27    | （無）                | SWE1-DM-006 | **空列，僅 D 欄** |
| 28–30 | TC-DM-018 … TC-DM-020 | SWE1-DM-007 | rvc-01 × 3 |
| 31–33 | TC-DM-021 … TC-DM-023 | SWE1-DM-008 | rvc-01 × 3 |
```

**與 34b §一之列布局逐列相符。** TC ID 依新列序重編 `TC-DM-001` … `TC-DM-023`
（O 欄全 `NEW`，重編無代價）。

需求全集之來源不寫死：`_leaf_order()` 取自 `data/recon.json` 之 `leaves`
（8 筆），前綴以 TC 實際所用者為準（recon 記 `SWE-DM-`、TC 用 `SWE1-DM-`，
兩者不同）；TC 之 leaf 若不在全集內即中止。

### 9.2 【實錯三項】寫回機制之缺陷，本輪抓到並改

三項皆為**寫回機制**之缺陷（非 TC 內容），於執行 34b 之版面比對時抓到。
其中 (a)(b) 直接屬本包之標的（版面），(c) 為既有條文之違反。

**(a) 寫入格喪失樣式 —— 版面缺陷**

`_set_row()` 重建 `<c>` 時未保留原 `s=` 樣式索引，
且 `<row>` 標籤被重建為 `<row r="10">`，母本之
`spans="1:34" s="84" customFormat="1"` 全數丟失。
影響範圍為既有交付本之 23 列 × 16 欄 —— 框線、換行、列高設定隨寫入消失。

處置：改寫時保留原儲存格之 `s=`，`<row>` 之開標籤原樣留存。
實測 after `r10` = `<row r="10" spans="1:34" s="84" customFormat="1">`、
`<c r="D10" s="81" t="inlineStr">`。

**(b) B 欄被賦值 —— 違反 R-DM15，且毀去共用公式之宿主**

母本 `B11` 為共用公式之**宿主**：
`<f t="shared" ref="B11:B74" si="0">IF(ISBLANK($D11),"",ROW()-9)</f>`。
既有寫回把 `B10`–`B32` 全寫成 inlineStr 死值，宿主隨之消失，
`B33`–`B74` 只剩 `si="0"` 而無定義 —— Excel 開檔有判損毀／掉公式之虞。
R-DM15 明文「寫回一律不得對 B 欄賦值」，`feature.yaml` 之註記亦已在，
**條文在、註記在，腳本仍寫了**。

處置（**Pei 2026-08-27 裁定：依 R-DM15 不寫 B**）：
`COLS` 移除 `B` 鍵。實測 after 之宿主字串與母本逐字相同。

**其代價，明列**：
序號由 D 欄之填寫經公式自動產生，故

- `r27`（`SWE1-DM-006` 空列）之 **B 欄由公式算出 `18`**，非留空。
  34b §一「其餘欄一律留空」就**我們寫入的欄**成立；B 欄不由我們寫入。
- `r27` 之後，**B 欄序號與 TC ID 永久差 1**（`B28 = 19` 對 `TC-DM-018`）。
  此為母本公式（`ROW()-9`）與「空列佔一列」兩者相乘之必然結果。

**(c) 回讀驗證之欄數**

B 欄移出 `COLS` 後，寫入欄為 **15 欄**（`D F G H I J K L M N O P R S AA`）——
與 §3.4／§8.4 一路沿用之「15 欄」口徑自此**名實相符**
（此前為 16 欄寫入而 15 欄回讀）。

### 9.3 全套重驗（34b §二.2）

```text
| 項 | before | after | 相等 |
|---|---:|---:|---|
| <dataValidation | 4 | 4 | 相等 |
| x14:dataValidation | 1 | 1 | 相等 |
| <conditionalFormatting | 0 | 0 | 相等 |
| worksheets | 9 | 9 | 相等 |
| drawings | 6 | 6 | 相等 |
| charts | 0 | 0 | 相等 |
| rels | 16 | 16 | 相等 |
| zip entries | 48 | 48 | 相等 |

**完整性：PASS —— 逐項相等**
```

> `x14:dataValidation` 之 **1** 為本輪計數口徑（`<x14:dataValidation\b`，
> 不計 `<x14:dataValidations>` 容器）；§3.3／§8.4 之 **2** 含容器。
> **口徑不同，before／after 相等之結論不受影響**；此處具名以免日後誤讀為回歸。

**逐部件比對**：48 個 zip 部件中**內容有差異者僅 `xl/worksheets/sheet6.xml` 一個**，
其餘 47 個逐 byte 相同。
`R` 欄下拉 `xm:sqref` = `R10:R1411`（涵蓋 10–33）；
另三個 `dataValidation` 之 `sqref` = `P10:Q1411`／`T10:Z1411`／`AF10:AF1411`，皆未變。

**回讀驗證**

```text
回讀比對：24 列 × 15 欄，不符 = 0  →  PASS
r27 空列：D = 'SWE1-DM-006'，其餘 14 欄皆 None  →  PASS
第 34 列（24 列之後）應為空：D = None、F = None
抽查 r10：F=TC-DM-001 D=SWE1-DM-001 G=Display H=Operative State P=P1 R=狀態轉換 (State Transition Testing)
抽查 r33：F=TC-DM-023 D=SWE1-DM-008 H=Rear View Camera P=P1
B 欄（不寫入，抽查）：r10／r11／r27 皆為 =IF(ISBLANK($D…),"",ROW()-9)
未寫欄逐 byte 不變（r10 之 A／C／E／Q／T／AH）：六欄皆同
```

**合併 lint 與揭露檢查**

| 項 | 值 |
|---|---|
| `lint036 --profile display` | **二十項行計皆 0**（`A…U`） |
| lint 母體 | **23**（報告之「資料列數：23」） |
| **r27 之排除** | **具名**：`lint_sheet()` 之取列條件為 `test_item`／`proc`／`er` 三欄任一非空；r27 三欄皆空，故**結構性排除**，非人工剔除。母體 23 = TC 條數，空列不入 |
| `check_disclosure.py` 雙向 | `pilot-01` **MISSING 0／STALE 0**；`rvc-01` **0／0**；`ops-01` **0／0** |
| `verify_reference_binding.py` | **13 of 13 match** |

**sha**

| 項 | 值 |
|---|---|
| 來源母本（寫回後） | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` —— **未變**（綁定 13/13） |
| 輸出（34b 版） | `069724551474a06e1deedcc18642bddb53251ea1e79ca9187be27b2043527995` |
| 輸出（34a 版，已被覆蓋） | `4528b93783ad52af9a51aded4ee1e7497ddc8c527e5687b807888b52081fbf7a` |

**輸出檔名不變**（34a §二之要求）：`…_SWQT_Display_20260826.xlsx`。

### 9.4 覆蓋總表（34b §二.3 之補記）—— **TC 數全部不變**

```text
| leaf | Test Set | TC 數 | 交付列 | 覆蓋狀態 |
|---|---|---:|---|---|
| SWE1-DM-001 | Operative State      | 9 | 10–18 | 部分覆蓋 |
| SWE1-DM-002 | Operative State      | 3 | 19–21 | 部分覆蓋 |
| SWE1-DM-003 | Operative State      | 2 | 22–23 | 部分覆蓋 |
| SWE1-DM-004 | Thermal Management   | 2 | 24–25 | 部分覆蓋 |
| SWE1-DM-005 | Thermal Management   | 1 | 26    | 部分覆蓋 |
| SWE1-DM-006 | —                    | 0 | 27    | **未覆蓋（空列，僅 D 欄）** |
| SWE1-DM-007 | Rear View Camera     | 3 | 28–30 | 部分覆蓋 |
| SWE1-DM-008 | Rear View Camera     | 3 | 31–33 | 部分覆蓋 |
| 合計        |                      | 23 | 10–33（24 列） | 7/8 leaf 有 TC |
```

deferred token 與 blocking DR 之對照**逐項不變**，見 §四；
**交付時仍不得表述為「八條全覆蓋」**。
`SWE1-DM-006` 之差別僅在於：此前它在工作簿上**不存在**，
自本包起它**存在且顯為空** —— 未覆蓋一事由「讀者須自行比對 037」
變為「打開工作簿即見」。

### 9.5 防再犯（34b §三，一句，不立條 —— R-DM57 凍結）

已記入 `PLAYBOOK.md` §5b（交付慣例）：

> `write_back_036.py` 之列序自 34b 起以 **Requirement ID 升冪**為預設；
> 批次序僅為生成時之內部順序，不得出現在交付版面。

### 9.6 §六 pathspec 之補記（**未執行；全部 git 操作屬 Pei**）

```bash
git add \
  features/display/scripts/write_back_036.py \
  features/display/DELIVERY.sha256 \
  features/display/PLAYBOOK.md \
  features/display/BACKLOG.md \
  features/display/docs/handoff/34b_layout_fix.md \
  features/display/docs/upstream/34_closeout.md
```

建議之 commit 訊息：

```text
fix(display): deliver layout by requirement ID order, restore master styles

- rows sorted by Requirement ID ascending; SWE1-DM-006 gets a D-only blank row
- TC IDs renumbered TC-DM-001..023 to follow the new row order
- stop writing column B (R-DM15): it hosts the B11:B74 shared formula
- preserve cell style indices and row attributes when writing cells
```

> `features/display/output/` 之 xlsx **仍不入**（Pei 2026-08-26 明示，§8.5 之理由不變）。

### 9.7 尚待 Pei 者（**執行層不動**）

1. ~~**交付路徑之副本已過時**~~ **← 已了結（2026-08-27，Pei 指示，本層執行）**
   `/Users/peihe/Work/…/ASW-R2/Display/` 之 `…_SWQT_Display_20260826.xlsx`
   已以 34b 版覆蓋，`cp` ＋ `cmp` 逐位元相同，兩副本皆 `06972455…`；
   台帳 ENTRY 002 之兩行實測皆 `OK`。
   **覆蓋前該檔實測 `b12bd378…`** —— 非 ENTRY 001 所記之 `4528b937…`，
   內容為 34a 之 23 條但**已經 Excel 開啟並重存**（inlineStr → sharedStrings、
   樣式重編、共用公式宿主移為 `B75:B138`）。該狀態已具名於台帳，其複本
   僅留於 session scratchpad（拋棄式，不入台帳）。
2. **Excel 實開確認**未完成（無「修復」提示、R／P／AE 下拉可用、分頁數 9）。
   本包修了 (b) 之共用公式宿主 —— **實開確認之價值因而更高，不是更低**。
3. `fw036-display-v1` tag、RD-1 —— 皆未動。
