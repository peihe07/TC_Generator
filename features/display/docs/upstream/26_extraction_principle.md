# 上繳包 26 —— 機器抽取原則入條、A-DM35 補件、STALE 之實測（含 26a）

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/26_extraction_principle.md`
  ＋ 其附件 `26a_materials_landed.md`（含下放包 24 之步驟 4／5／6）
- **兩條停止條件觸發，兩者皆為「檢查抓到東西」而非失敗**：
  - **66**（`STALE` 未報 1）→ **`check_disclosure.py` 之 STALE 方向有缺陷，本輪確診**
  - **67**（24-6 重算不符）→ **`EE Architecture` 非全列 `All`**
- 依上述，**24-5／24-4 未執行**（26a §3.1 定 24-6 為其前提）
- 停止條件 65／68 未觸發
- **git 未執行**（§8 為建議）

---

## 摘要

| 步驟 | 結果 |
|---|---|
| 26-1 抄錄 | R-G35／R-G36 → ledger，**兩條相符**；R-G25 指標已置（非 fence） |
| 26-2 A-DM35 補件 | 已補逐字出處與計數；**與 R-DM48 相容，非相衝**（停止條件 65 未觸發）；DR-DM9 之文字從未被縮小 |
| 26-3 兩處指標 | 已置，並依 26a 改為「A6 已解除」＋ 24-6 之實際結果 |
| 26-4 `STALE` 實測 | **未報 1 → 停止條件 66 觸發**。缺陷已確診並以反例證明其非全然失效 |
| 26-5 BACKLOG A1 | 已增註抽取標的；阻斷者依 26a 改為 DR-DM2 |
| 26a-8 / 24-6 | **已執行**。九項相符（兩項須具名口徑），**一項不符 → 停止條件 67** |
| 26a-8 / 24-5、24-4 | **未執行**（24-6 為其前提） |
| 26a-9 重複檔 | **該檔於本層量測時不存在**；A-DM36 登記 |
| 26-7 INDEX | 已更新 |

**26 §一「錯在我」之自陳，本輪出現了它的第四例 —— 而這次錯的是我。**
`check_disclosure.py` 是我 25 輪寫的，我在上繳 25 §八第 2 項自陳
「`STALE` 從未真被觸發過，我可以造一個假的解除來測它，本輪沒做」。
26 包把它列為步驟 4。**一測就倒。**

---

## 一、R-G35／R-G36 之抄錄核對表；R-G25 指標之置放

置放依 **R-G34**：兩條入 `docs/fw036/RULINGS_LEDGER.md` 之新節
「下放包 26 之全域條文」，非各自所補充之條下。

## 抄錄核對表 — 26_extraction_principle.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| — | R-G35 | `docs/fw036/RULINGS_LEDGER.md` | 608 | `7b3d83e1d4a86dd9` | 是 |
| — | R-G36 | `docs/fw036/RULINGS_LEDGER.md` | 660 | `fb144aee4ae62afc` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **55** 個，與各下放包原檔逐字元比對 **全數相符**（55 vs 55）。

`RULINGS.md` 之 R-DM 區塊維持 **55**（本包無 R-DM 條文），順序驗證 exit 0。

### 1.1 R-G25 之適用範圍註記（指標形態，不入核對表母體）

置於 ledger 之 R-G25 條下，逐字：

> **適用範圍註記（下放包 26 §三，2026-08-25）—— 不改本條原文**：
> R-G25 規制「宣稱不做 X」之測試須連跑兩次。其精神及於另一形態 ——
> **某方向恆為 0 之檢查，其有效性未經證明者，須以人為構造之情境
> 觸發該方向一次**，證明它抓得到，而後還原。
> 適用實例：`check_disclosure.py` 之 `STALE` 方向（上繳 26 §五）。
> 依 R-G34，本註記為指標形態，不入核對表母體。

**該註記在本輪立即兌現，且結果是 FAIL** —— 見 §五。

---

## 二、`A-DM35` 之全文與出處，及其與 R-DM48 之關係

### 2.1 分析層之質疑與其前提

26 §2.4 指出：`DCSD_DISP_STAT` 之 `VAL_` 有 `1 "ON"`、`3 "RR_CMRA"`，
而**規格側之 token 為 `[DISP_ON]`、`[DISP_REAR_CAMERA]`，兩者逐字不等**，
故「逐字解得」一語與 R-DM48 相衝。

**該前提為誤。** 規格對 `$DCSD_DISP_STAT$` **同時使用兩套拼法**。
逐字實測（`python-docx` 段落序，配對式
`\$([A-Za-z0-9_]+)\$\s*=\s*\[([^\]]+)\]`）：

| 標籤 | 於 `$DCSD_DISP_STAT$` 之命中 | DBC `VAL_` | R-DM48 判定 |
|---|---:|---|---|
| `[OFF]` | **85** | `0 "OFF"` | 解得 raw 0 |
| `[ON]` | **53** | `1 "ON"` | 解得 raw 1 |
| `[BLANK]` | **20** | `2 "BLANK"` | 解得 raw 2 |
| `[RR_CMRA]` | **72** | `3 "RR_CMRA"` | 解得 raw 3 |
| `[DISP_HOT]` | **46** | `4 "DISP_HOT"` | 解得 raw 4 |
| `[SNA]` | **8** | `7 "SNA"` | 解得 raw 7 |
| `[DISP_ON]` | 23 | 查無 | **逐字查無** |
| `[DISP_OFF]` | 12 | 查無 | **逐字查無** |
| `[DISP_REAR_CAMERA]` | **0** | — | **從未用於本訊號** |

逐字例：

```text
[629]  For limp-in action, the HU shall assume $DCSD_DISP_STAT$ = [ON].
[1742] When the DCSD screen is in the 'DCSD Screen ON' state and the HU transitions to the high priority Rear View Camera screen ($TGW_DISP_STAT$ = [DISP_REAR_CAMERA]), the DCSD shall send $DCSD_DISP_STAT$ = [RR_CMRA].
```

段落 1742 一句之內同時出現兩者，**且分屬兩個訊號** ——
`[DISP_REAR_CAMERA]` 掛 `$TGW_DISP_STAT$`，`[RR_CMRA]` 掛 `$DCSD_DISP_STAT$`。

### 2.2 `[DISP_NORMAL]`／`[DISP_REAR_CAMERA]` 是 HU 側的值

| 標籤 | `$TGW_DISP_STAT$` | `$DCSD_DISP_STAT$` |
|---|---:|---:|
| `[DISP_REAR_CAMERA]` | **107** | **0** |
| `[DISP_NORMAL]` | **99** | 0 |
| `[DISP_OFF]` | 146 | 12 |

**DR-DM9 把兩個 HU 側標籤問到了 DCSD 側的訊號上** —— 此即 A-DM35 之主張。

### 2.3 關係判定：**相容，非相衝**（停止條件 65 未觸發）

R-DM48 之規則是**逐字**：解得則寫、解不得則改驗行為。
A-DM35 不修改該規則，只修正「解不得者有多少」之估計：
解得六個、解不得兩個別名。

R-DM48 立條之理由（「同一訊號之六個值裡規則就不一致」）**仍為真** ——
`[DISP_REAR_CAMERA]` 對 `RR_CMRA` 確實不是前綴規則所能外推者，
而該不可外推性現在有了更精確的說明：**它們根本是兩個訊號的值。**

### 2.4 【重要】判定落在**條款**層級，不落在訊號層級

| 條款 | 逐字寫法 | 可否寫 raw |
|---|---|---|
| `{4820287}`（005 回復，本批 #3） | `$DCSD_DISP_STAT$ = [DISP_ON]` | **否** —— 該條用別名 |
| RVC 諸條（007／008） | `$DCSD_DISP_STAT$ = [RR_CMRA]` | **是**（raw 3） |
| `{4820282}`（004，本批 #1） | `$DCSD_DISP_STAT$ = [DISP_HOT]` | 是（raw 4） |

**故本批三條 TC 一字不必改。** #3 所引之 `{4820287}` 用的正是解不得的
`[DISP_ON]`，其 ER 只驗行為 —— rev4 之處置事後仍然正確。

> 這一點我 25 輪沒說清楚。當時只寫「DCSD 側之 `[RR_CMRA]`／`[ON]`
> 逐字解得，不受阻」，**沒有說它取決於條款用哪一種拼法** ——
> 分析層據此質疑是合理的。

---

## 三、DR-DM9 範圍之現況

**`DATA_REQUESTS.md` 之 DR-DM9 文字從未被本層修改，範圍未曾縮小。**

25 輪之「縮小」只出現在**上繳 25 §六之 A 類表**（A3 列之敘述），
即報告側，非 DR 記錄。故無可還原者。

具名之差別：

| 位置 | 25 輪之狀態 | 現況 |
|---|---|---|
| `DATA_REQUESTS.md` 之 DR-DM9 | 原文，未動 | 原文，未動 |
| 上繳 25 §六 A3 列之敘述 | 稱「範圍已依 A-DM35 縮小」 | 本包 §七 A3 已改為「A-DM35 已補件；縮小之裁定屬分析層」 |

**本層對 DR-DM9 之建議（不逕改）**：重擬為三問 ——
(a) `[DISP_ON]`／`[DISP_OFF]` 與 `[ON]`／`[OFF]` 是否為同一狀態；
(b) `$TGW_DISP_STAT$` 之值對應（其標籤與 `TGW_DISP_STATSts` 之
`VAL_` 逐字不等）；
(c) 規格自帶之雙記法（`DISP_NORMAL / Normal_mode`、
`DISP_REAR_CAMERA / Rear_Camera_Display`）是否為權威。

---

## 四、A-DM31／DR-DM10(b) 兩處指標之全文

依 26a §三，兩處之措辭由「掛回 A6」改為「A6 已解除＋ 24-6 之結果」。

### 4.1 A-DM31 之修正註記下

> **指標（下放包 26 §四.3，經 26a §三修正）**：A6（CFTS013 未落磁碟）
> **已於 26a 解除**，檔案現位於 `inputs/`。本項之依據已由 24-6 之獨立重算
> 覆核 —— **表單編號實測為 `FM-WI-FSM-035-A02`，且逐字見於該檔五個分頁**
> （`封面`／`修訂履歷`／`Product Document 記錄封面頁`／`Analysis Report`／
> `Instructions`）。**本項至此不再是繞道，已為實測所支持。**
> 惟 24-6 另有一項不符（`EE Architecture` 非全列 `All`），見上繳 26 §六。

**這一處已由「繞道」升為「實測」** —— 25 輪我只能以「該詞見於手上的
CFTS043 檔名」自證，本輪直接在 013 檔內五個分頁量到它。

### 4.2 DR-DM10(b) 之問法後

> **【指標，26 §四.3／26a §三】A6 已於 26a 解除，CFTS013 已落 `inputs/`。
> 惟該五列（`>=51`／`>=56`／`>=60`／`>50`→`<=50` 之分段）之獨立重算
> **尚未執行** —— 24-6 於 `EE Architecture` 一項不符而依停止條件 67 停手，
> 24-4／24-5 連同本項之重算一併待裁。本問法之成立不依賴該五列之數字
> （其改變的是問題之變數：溫度而非時間），但其**引為依據之五列仍未經
> 本層驗證**。A6 關閉之複核於此一併記明**

**這一處仍是繞道。** 我沒有把 §2.3 之五列重算 —— 24-6 之範圍是
24 包 §一§二所列之數字，那五列在 §2.3，不在其內；而 24-4／24-5
既已停手，我不逕行擴大重算範圍。

---

## 五、`STALE` 觸發測試 —— **未報 1，停止條件 66 觸發**

### 5.1 測試與其結果

依 26 §四.4：自 `deferred` 陣列**暫時移除 `multi-stage` 一項**
（其 blocking DR 為 DR-DM4，與 pilot 之兩條主 TC 無涉），
跑 `check_disclosure.py`。

**期望**：`STALE` 報 1，指名 `multi-stage` 與 TC#3。
**實得**：

```text
移除後 deferred 項數: 2
| #1 | SWE1-DM-004 | `warning popup` | MISSING | 含 |
| #2 | SWE1-DM-004 | `warning popup` | MISSING | 含 |
| #3 | SWE1-DM-005 | `protective shutdown` | MISSING | 含 |

MISSING = 0   STALE = 0
exit=0
```

**`STALE = 0`。** 而 TC#3 之括號下半確實仍含該 token：

```text
(Return path of the ON/OFF decision — verifies the recovery side, not the protective shutdown and not the multi-stage thresholds, both deferred)
```

**依停止條件 66：停並回報。該方向之檢查不成立。**

### 5.2 確診

```text
# 現行實作（check_disclosure.py）之 STALE 候選集來源
  tokens   = {leaf -> [token, ...]}          ← 自 deferred 陣列建
  all_tokens = 全部 token 之聯集              ← 亦自 deferred 陣列建
  STALE 候選 = all_tokens - 該 leaf 之 token   ← **仍在陣列內**

# 三種情境下 all_tokens 之內容
  (a) 完整陣列          : all_tokens = ['multi-stage', 'protective shutdown', 'warning popup']
  (b) 移除 multi-stage  : all_tokens = ['protective shutdown', 'warning popup']
      → 'multi-stage' 不在候選集內，**無人去檢查它**
  (c) 陣列清空          : all_tokens = []  → STALE 恆為 0

# 缺陷之陳述
  STALE 只抓得到「token 被搬到別的 leaf」，
  **抓不到「token 被整個移出陣列」—— 而後者正是 deferred 解除之實際形態。**

# 反證：TC#3 之括號下半確實仍含該 token
  (Return path of the ON/OFF decision — verifies the recovery side, not the protective shutdown and not the multi-stage thresholds, both deferred)
  含 'multi-stage' : True

# 現行實作唯一抓得到 STALE 之情境（構造以證明其非全然失效）
  把 multi-stage 之 leaf_id 由 SWE1-DM-005 改為 SWE1-DM-004：
```

**缺陷之根因**：`STALE` 之候選集為

```python
sorted(all_tokens - set(tokens.get(leaf, [])))     # all_tokens 亦自 deferred 陣列建
```

即候選集**只能由陣列裡還在的 token 構成**。一個被整個移出陣列的 token，
從此不在候選集內，**沒有任何一行程式碼會去找它**。

| 情境 | 現行實作 |
|---|---|
| token 被搬到**別的 leaf** | **抓得到** |
| token 被**整個移出陣列**（deferred 解除之實際形態） | **抓不到** |
| 陣列**清空** | `all_tokens = []`，STALE 恆為 0 |

**它抓得到的，正好不是 R-G33(d) 要防的那一種。**

### 5.3 反例：證明該方向非全然失效

把 `multi-stage` 之 `leaf_id` 由 `SWE1-DM-005` 改為 `SWE1-DM-004`
（token 仍在陣列內，只是換了 leaf），於**拋棄式複本**上跑：

```text
| #3 | SWE1-DM-005 | `multi-stage` | STALE | **含（陣列無）** |
MISSING = 2   STALE = 1
  STALE    TC#3 SWE1-DM-005 有 token 'multi-stage' 而 deferred 陣列無此項
```

**`STALE = 1`，訊息可讀，不崩潰。** 即 26 §四.4 之 (ii)(iii) 兩項條件
在此情境下滿足，(i) 不滿足於指定之情境。探針檔已刪除
（`generated/` 現僅 `pilot-01.json`）。

### 5.4 還原與 R-G25 之連跑兩次

```text
還原後第一次 : MISSING = 0   STALE = 0   exit=0
還原後第二次 : MISSING = 0   STALE = 0   exit=0
diff 兩次輸出          → 逐字元相同：PASS
diff 還原後 vs 基線檔  → 逐字元相同：PASS
```

`pilot-01.json` 已逐字元還原，測試未留下痕跡。

### 5.5 修法之三個選項（**本層不逕行擇一**）

`STALE` 之候選集須有一個**獨立於當前陣列**的來源。三種可能：

| 選項 | 作法 | 代價 |
|---|---|---|
| **甲** | 掃括號下半之句型（如 `... is deferred`／`both deferred`），把其中之名詞片語當候選 | 回到「詞表由人給」—— **B9／B11 之老問題復發** |
| **乙** | `deferred` 項不刪除，改加 `lifted: true`／`lifted_at`，陣列只增不減 | 陣列會長期堆積；但 token 永遠在候選集內，**且解除之時點成為可查之紀錄** |
| **丙** | 另立一份 `deferred_history` 清單供 STALE 取用 | 多一份要同步的檔，**其自身之時效無人保證**（即 R-G33(d) 之同型問題再現） |

**本層之判斷（僅供參考，不逕行實作）**：選項乙最合本案之理路 ——
它把「解除」變成一次**寫入**而非一次**刪除**，而本案至今每一條
機器保證（R-DM30 sidecar、R-G23 綁定、R-G20 核對表）都是靠
「留下可比對之痕跡」成立的，**刪除本質上不留痕跡**。

但這是資料模型之變更（R-DM53 才剛定四鍵），屬 Tier 2，故不逕改。

---

## 六、24-6 之獨立重算 —— **一項不符，停止條件 67 觸發**

### 6.1 量測條件與檔案

```text
path   : features/display/inputs/SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx
bytes  : 85518
sha256 : 1036b2af9f655441cc01bed6e2780a359334d8b10fca5d1bf693fb7137b911b0
mtime  : 2026-08-16 06:30:00
openpyxl, read_only=True, data_only=True；字串比對逐字、區分大小寫
```

### 6.2 逐項比對

| 項 | 下放包 24 | 本層實測 | 判定 |
|---|---|---|---|
| 分頁（6 個，逐字） | `封面`／`修訂履歷`／`Product Document 記錄封面頁`／`Analysis Report`／`Instructions`／`下拉選單設定處` | **相同，順序亦同** | 相符 |
| 表單編號 | `FM-WI-FSM-035-A02` | **相同**，且見於 5 個分頁 | 相符 |
| 資料列 | 32 | **32** | 相符 |
| `Category` 分布 | Information 12／Functional Requirement 11／Heading 9 | **12／11／9** | 相符 |
| `SW/HW/System` | Information 12／Heading 9／System 8／SW 3 | **12／9／8／3** | 相符 |
| **`EE Architecture`** | **`All`（全列）** | **`All` 26／空 5／`PowerNet` 1** | **不符** |
| 修訂履歷 | Ver A → F | **A B C D E F** | 相符 |
| `85 degree` / `85 deg` | 0 / 0 | **0 / 0** | 相符 |
| `DISP_HOT` | 0 | **0** | 相符 |
| `DCSD` | 94 | **94**（出現次數計）／13（儲存格計） | 相符（**口徑須具名**） |
| `Document ID` 全集 | 32 個（列舉） | **32 個相異，逐一相符** | 相符 |
| `629`／`633`／`952` 之落點 | 各 1／1／2 次，全在 `r8` 之自由文字 | **全在 `Analysis Report` 第 8 列**；次數 1／1／**2**（出現次數計） | 相符（同上口徑） |
| `Document ID` 是否含 629／633／952 | 否 | **否**（32 個全集逐一檢查） | 相符（**停止條件 61 未觸發**） |

### 6.3 兩項曾看似不符、經具名口徑後相符

依 A-DM31 之教訓（`Display` 480 vs 477，因掃描範圍不同），本輪對
`DCSD` 與 `CFTS013-952` 同時以兩種口徑量：

```text
'DCSD'         儲存格計 =   13   出現次數計 =   94
'CFTS013-952'  儲存格計 =    1   出現次數計 =    2
'CFTS013-629'  儲存格計 =    1   出現次數計 =    1
'CFTS013-633'  儲存格計 =    1   出現次數計 =    1
```

**下放包 24 用的是「出現次數計」，本層首算用的是「儲存格計」。**
兩者皆非錯，但**下放包未具名其口徑**。建議日後之計數一律附口徑
（R-G16 之量測條件要求於此處之應用）。

### 6.4 唯一之實質不符：`EE Architecture`

下放包 24 §一記：

> `EE Architecture` | **`All`（全列）** → 適用 Atlantis High

實測（欄名逐字為 `EE Architecture\n(All,ATL-Hi,ATL-Mi)`，32 資料列）：

| 值 | 列數 |
|---|---:|
| `All` | **26** |
| （空） | **5** |
| `PowerNet` | **1** |

**「全列」為誤。** 其後果：

- `All` 之 26 列涵蓋 Atlantis High → 該部分之推論成立
- **`PowerNet` 之 1 列不適用於本專案**（`Atlantis High`）
- **空白之 5 列適用性未定** —— 不得預設為 `All`

即下放包 24 §一之結論「→ 適用 Atlantis High」**對 26/32 列成立，
對其餘 6 列未經證明**。依停止條件 67：**停並回報，不以下放包之
數字覆蓋實測值。**

### 6.5 停手之範圍

依 26a §3.1「24-6 先於 24-4／24-5」，24-6 為其餘兩者之前提，故：

| 步驟 | 狀態 |
|---|---|
| **24-5**（`reference:` 增 `cfts013_sysra`、綁定 12 項） | **未執行** —— 綁定現仍 `entries: 11`／11 of 11。停止條件 62 未評估 |
| **24-4**（`popup_priority.tsv` 之機器抽取登記） | **未執行** |

> **我判斷 24-5 本身其實不受該不符影響**（綁定只是登記 sha256，
> 與 `EE Architecture` 之分布無關）。**但 26a 明文定序，且該序之
> 理由正是「重算為其餘兩者之前提」** —— 我不自行判斷哪一項可以
> 例外，這正是 24 包那類「以未查證之前提下指令」的反面。
> 若分析層裁定 24-5 可先行，本層可於單輪內補上。

---

## 七、`inputs/` 之重複檔（26a §二／步驟 9）—— **該檔不存在**

### 7.1 實測

```text
# `features/display/inputs/` 普查（實測，9 個檔案）

| 檔名 | bytes | mtime | sha256（前 16 碼） |
|---|---:|---|---|
| `Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` | 46993 | 2026-08-22 16:02:56 | `ab3198e81fb21d21` |
| `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` | 200650 | 2026-08-17 09:46:09 | `6372fb6be02f48dc` |
| `Pop Up List HMI R1 (26PI).xlsx` | 2951835 | 2026-08-25 13:51:21 | `ff47b7be63e5824c` |
| `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` | 1035049 | 2026-08-25 13:50:34 | `dc078763c67b5238` |
| `R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` | 292827 | 2026-08-22 16:02:33 | `8696d1f596e33677` |
| `SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx` | 85518 | 2026-08-16 06:30:00 | `1036b2af9f655441` |
| `SYS2_CFTS043_FM-WI-FSM-035-A02 STLA 技術安全需求分析報告_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA_CFTS043_V01.xlsx` | 216266 | 2026-08-25 13:56:27 | `1c0b2abf659f4911` |
| `SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx` | 193683 | 2026-08-16 06:30:00 | `421c8eef3f5cb01a` |
| `SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` | 3663612 | 2026-08-16 06:32:00 | `be9c97af0211a703` |

## 內容重複（同 sha256 之檔案群）
  重複群數 = 0

## 檔名含 `copy` 者
  **無**
```

**9 個檔案、檔名含 `copy` 者 0、同 sha256 之重複群 0。**
全 repo（排除 `.git`）檔名含 `copy` 者僅 `node_modules/`、`.venv/` 之無關檔。

### 7.2 時序與判定

| 時點 | 事件 |
|---|---|
| 2026-08-25 21:15:49 | 26a 所記之 `copy` 檔 mtime |
| 2026-08-25 21:18 | `inputs/` 目錄之 mtime |
| 其後 | 本層普查：9 檔、無 `copy` |

目錄 mtime 晚於該檔 mtime，**與「該檔曾存在而後被移除」相容**。
**本層不推定其成因**（同 26a §二之分寸），亦不主張分析層量錯。

**26a §二之三個選項現無標的**；若係 Pei 於此期間刪除，即選項甲已執行。
**停止條件 68 未觸發**：本輪母體（9 檔）不含任何 `copy` 檔。
已以 **A-DM36**（LOW）登記，含上表與時序。

### 7.3 26a §2.1 之觀察與該檔是否存在無關，仍然成立

> 綁定保護的是「這一份是不是原來那一份」，**不保護「旁邊有沒有第二份」**。

`verify_reference_binding.py` 綁確切路徑，不會發現 `inputs/` 多出檔案；
`inputs/` 又由 `.gitignore` 排除。**現有每一道機器檢查都會放過這種情形。**
本輪之目錄普查是首次有人實測它，**但那是一次性腳本，非常設檢查** ——
記入 B14。

---

## 八、未驗項分流（A／B，R-G29）

### A 類 —— 阻斷交付

| 編號 | 項 | 阻斷什麼 | 索取中 |
|---|---|---|---|
| A1 | 組 A／組 B 何者為準 | 004 popup 側；005 關閉側 | DR-DM10(a) |
| A2 | DCSD 側 warning → off 之分段變數與第二門檻 | 原 #2；`PU0130` | DR-DM10(b) |
| A3 | 值標籤之對應 | 005 之 `[DISP_ON]` 側；007／008 之 HU 側 | DR-DM9（**A-DM35 已補件；縮小之裁定屬分析層**） |
| A4 | `popup_priority.tsv` | `SWE-DM-006` | DR-DM2（**素材已到手**） |
| A5 | `sysad_allocation.tsv` | 全 8 leaf 之追溯欄 | DR-DM3 |
| **A7** | **`check_disclosure.py` 之 STALE 方向不成立** | **R-G33(d) 之交付前 gate** | **本包 §5.5 三選項待裁** |
| **A8** | **CFTS013 之 `EE Architecture` 6 列適用性未定** | 24-4／24-5；凡引該檔之值者 | **本包 §6.4 待裁** |

~~A6~~（CFTS013 未落磁碟）**已於 26a 解除**。A7／A8 為本輪新增。

> **A7 之份量須具名**：R-G33(d) 定「交付前再跑一次雙向檢查」為
> 揭露機制之時效保證。**該保證現在有一半是壞的** ——
> 而它壞的那一半，正是交付前最可能發生的情形（deferred 解除）。

### B 類 —— 不阻斷交付

| 編號 | 項 | 為何不阻斷 |
|---|---|---|
| B1–B10、B12、B13 | 見上繳 25 §六 | 不變（B13 之阻斷者由 A6 改為 24-6 之裁定） |
| ~~B11~~ | ~~token 為自訂對譯~~ | 25 輪結案 |
| **B14** | **`inputs/` 之目錄普查非常設檢查** | 本輪為一次性腳本；`inputs/` 由 `.gitignore` 排除，重複檔不進 diff |
| **B15** | **下放包之計數未具名口徑** | 本輪兩項（`DCSD` 94／`952` 2）以口徑釐清後相符；建議日後一律附口徑（R-G16） |

B14／B15 為本輪新增。

---

## 九、建議之 commit 訊息與 pathspec（**未執行**）

```bash
git add \
  features/display/ANOMALIES.md \
  features/display/DATA_REQUESTS.md \
  features/display/BACKLOG.md \
  features/display/docs/INDEX.md \
  features/display/docs/handoff/26_extraction_principle.md \
  features/display/docs/handoff/26a_materials_landed.md \
  features/display/docs/upstream/26_extraction_principle.md \
  docs/fw036/RULINGS_LEDGER.md
```

```text
feat(display): prove the STALE direction does not work, and recount CFTS013

- the induced test required by R-G25 shows check_disclosure.py cannot see a
  token that was removed from the deferred array at all, only one moved to
  another leaf, and removal is what lifting a deferral actually looks like
- add R-G35: a handoff must state whether the material it relies on is
  reachable from the execution side
- add R-G36: spec content goes into data files by machine extraction only,
  never transcribed from a handoff
- supply the verbatim evidence A-DM35 was missing: the spec uses two
  spellings on DCSD_DISP_STAT, six of which resolve against the DBC, so the
  ruling holds per clause rather than per signal
- recount the CFTS013 workbook: every figure reproduces except the EE
  Architecture column, which is All on 26 of 32 rows, not on all of them
- record A-DM36: the duplicate SYS2 file is not present at measurement time
```

> `batches/pilot-01/batch_context.md` 不入 pathspec（`.gitignore` 已排除）。
> `generated/pilot-01.json` **未變更**（STALE 測試已逐字元還原），不入。
> `feature.yaml` **未變更**（24-5 未執行），不入。
> 036 母本未變更，亦不入。

---

## 十、本包是否仍有該驗而未驗者 —— 獨立判斷

**有三項。**

1. **我沒有修 `STALE`，也沒有測我提的那三個選項。**
   §5.5 之判斷（選項乙最合理路）是我的意見，**沒有任何實作或量測
   支持它**。特別是選項乙之代價（陣列只增不減）我沒有估過長度 ——
   本案現在 3 項，八個 leaf 全做完會是多少，我不知道。

2. **`EE Architecture` 之 6 列，我只數了它們，沒看它們是哪 6 列。**
   停止條件 67 要求停手回報，我照做了；但「`PowerNet` 那一列是哪一條
   需求、空白那 5 列是不是 Heading」是查得到的，而那會直接決定
   §6.4 之後果有多大。**我把「停手」執行成了「不再往下看一眼」。**

3. **26 §一列了三次同型錯誤（18／23／24 包），本輪之 STALE 缺陷是
   同一形態的第四次，而錯在我。**
   我在上繳 25 §八自陳「`STALE` 從未真被觸發過」——
   **我看見了那個洞，描述了它，然後把它留在原地一輪。**
   分析層把它排成步驟才被測出來。**自陳不等於處置**，
   這一點我在上繳 23 §八第 3 項也犯過（把落差寫出來，沒有縮小它）。
