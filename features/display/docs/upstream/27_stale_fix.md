# 上繳包 27 —— A8 解除、STALE 乙案修畢、24-4／24-5 完成

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/27_stale_fix.md`
- 步驟 1–7 全數執行。**停止條件 62／70 皆通過；66／67／69 未觸發；
  全部 1–70 無一觸發。**
- **git 未執行**（§7 為建議）

---

## 摘要

| 步驟 | 結果 |
|---|---|
| 1 A8 收尾 | 六列表**逐格相符**；FR **11/11 為 `All`**；24 包已加修正註記；A-DM37 登記；**A8 解除** |
| 2 STALE 乙案 | 修畢。誘發測試 **`STALE = 1`、exit 1、指名 TC#3**；還原後連跑兩次逐字元一致 |
| 3 24-5 綁定 | **`entries: 12`／12 of 12 match**；`cfts013_sysra` sha256 `1036b2af…`（停止條件 70 通過） |
| 4 24-4 來源登記 | 機器抽取，`{CFTS013-937}` 全文與 `PU0130` 逐字指名已入 `data/popup_priority_sources.tsv` ＋ sidecar |
| 5 抄錄 | R-DM54 相符；R-DM 區塊累計 **56**，順序驗證 exit 0；R-G16 口徑指標已置 |
| 6 DR-DM9／A-DM35 | DR-DM9 重擬（含十列附件表）；A-DM35 結案註記 |
| 7 INDEX | 已更新 |

**上一輪兩條停止條件觸發，這一輪兩件事都收乾淨了。**
A8 由「未定之風險」變成「已知之零」；STALE 由「一測就倒」變成
「同一情境下報 1」。

---

## 一、A8 之收尾

### 1.1 六列之獨立重算

量測條件：`openpyxl` `read_only=True` `data_only=True`；
`Analysis Report` 表頭列 5（1-based），資料自第 6 列；
欄以「欄名含該簡稱」定位（檔內實際欄名為
`文件識別碼 \nDocument ID`／`分類\nCategory`／
`EE Architecture\n(All,ATL-Hi,ATL-Mi)`／`需求描述 Description`）。

```text
欄 index: DocumentID=5 Category=9 EE=6 Description=2

## 非 `All` 之列（含空白），逐列（列號為 1-based 之工作表列）
| 列 | Document ID | Category | EE | Description（前 60 字，逐字） |
|---|---|---|---|---|
| r8 | CFTS013-752 | Information | （空） | `Date | Author | Description_x000D_ _x000D_ 2015/05/28 | Don ` |
| r9 | 0 | Information | （空） | `Change Identifier | Review Readiness Date | Approved Date | ` |
| r12 | CFTS013-1192 | Information | （空） | `The TBM shall do this or that` |
| r17 | CFTS013-1196 | Heading | PowerNet | `HU requirements` |
| r18 | CFTS013-1197 | Information | （空） | `The HU shall dipslay xxxxxxxx` |
| r19 | CFTS013-1194 | Information | （空） | `0` |

非 All 之列數 = 6

## Functional Requirement 之 EE 分布
  FR 列數 = 11
  'All': 11
  **FR 全為 All：True**
```

**與下放包 27 §1.1 之六列表逐格相符**：列號、`Document ID`、
`Category`、`EE`、內容五欄無一不符。`PowerNet` 之 r17 為 Heading
（章名 `HU requirements`），其餘五列為 Information 且 `EE` 為空。

**`Functional Requirement` 11 列之 `EE Architecture` 為 `All` 11/11。**

### 1.2 24 包之修正註記（原文依 R-TM13 不刪不改）

已加於 24 包 §一之 `EE Architecture` 列下，逐字：

> **更正（下放包 27 §1.1，2026-08-25；原文依 R-TM13 不刪不改）**：
> 上列之「全列」為分析層**未逐列驗即寫下之總括語**。
> 執行層獨立重算（上繳 26 §6.4、上繳 27 §一）：
> **`All` 26／空 5／`PowerNet` 1**，共 32 列。
> **惟 11 條 Functional Requirement 之 `EE Architecture` 為 `All` 11/11** ——
> 不符之六列全為 Information／Heading，需求本體無一受影響。
> 故「→ 適用 Atlantis High」之結論對需求本體成立，**其「全列」之說不成立**。
> 六列之逐列驗明見 A-DM37。**A8 於 27 輪解除。**

### 1.3 A-DM37（LOW）與 **A8 解除宣告**

三句樣板殘渣已登記：r12 `The TBM shall do this or that`、
r18 `The HU shall dipslay xxxxxxxx`（`dipslay` 為原文錯字）、
r19 `0`。**三者皆帶正式之 `Document ID`**（`-1192`／`-1197`／`-1194`），
在只看 id 清單時與真需求無從分辨 —— 此即其登記之理由。

**A8 解除**：六列已逐列驗明，五列為空白之 Information、一列為
`PowerNet` 之 Heading，**無一為需求本體**，適用性之疑慮消滅。
24-5／24-4 之前提恢復，兩者本輪已執行（§三／§四）。

> 上繳 26 §十第 2 項我自陳「把『停手』執行成了『不再往下看一眼』」。
> 本輪看了 —— **看了之後，A8 從一個未定之風險變成一個已知之零。**
> 停手是對的（不得以下放包之數字覆蓋實測值），
> **但停手與不看，是兩件事。**

---

## 二、R-DM54 之抄錄核對表，與修後之誘發測試

### 2.1 抄錄

## 抄錄核對表 — 27_stale_fix.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 56 | R-DM54 | `features/display/RULINGS.md` | 804 | `84fa06c411b8f259` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **56** 個，與各下放包原檔逐字元比對 **全數相符**（56 vs 56）。

置放依 R-G34：`RULINGS.md` 之新節「來源：下放包 27」。
R-G16 之口徑指標（非 fence，不入核對表母體）已置於 ledger 該條下：

> **口徑之補充（下放包 27 §1.5，2026-08-25）—— 不改本條原文**：
> R-G16 所稱之「量測條件」**自此明文包含計數口徑** ——
> 至少須具名為「儲存格計」或「出現次數計」。
> 實例：CFTS013 之 `DCSD` 儲存格計 13／出現次數計 94；
> `CFTS013-952` 為 1／2。**兩者皆非錯，未具名則兩造無從比對**。

### 2.2 實作之變更

```python
active, lifted = {}, {}
for item in deferred:
    bucket = lifted if item.get("lifted") else active
    bucket.setdefault(item["leaf_id"], []).append(item["token"])
all_tokens = {i["token"] for i in deferred}      # ← 含已解除項
```

三向判定：

| 母體 | 條件 | 方向 |
|---|---|---|
| 未解除項（該 leaf） | token **不見於**括號下半 | `MISSING` |
| **已解除項（該 leaf）** | token **仍見於**括號下半 | **`STALE`** |
| 他 leaf 之全部 token | 出現於本 leaf 之括號下半 | `STALE`（誤置，既有行為維持） |

**關鍵差別**：`all_tokens` 現自**全部**項（含已解除）建，
故被解除之 token **永遠留在候選集內** —— 這正是乙案之全部要旨。

### 2.3 誘發測試全輸出（R-G25 適用註記）

```text
===== (1) 基線 =====
# R-G33(c) 雙向檢查（R-G33(d)(2)；乙案 R-DM54）
batch: generated/pilot-01.json
tcs: 3   deferred entries: 3   （未解除 3 / 已解除 0）

| TC | leaf | token | 項之狀態 | 方向 | 判定 |
|---|---|---|---|---|---|
| #1 | SWE1-DM-004 | `warning popup` | 未解除 | MISSING | 含 |
| #2 | SWE1-DM-004 | `warning popup` | 未解除 | MISSING | 含 |
| #3 | SWE1-DM-005 | `protective shutdown` | 未解除 | MISSING | 含 |
| #3 | SWE1-DM-005 | `multi-stage` | 未解除 | MISSING | 含 |

MISSING = 0   STALE = 0
exit=0

===== (2) 誘發：於拋棄式複本標 multi-stage 為 lifted =====
已標 lifted 之項數: 1
# R-G33(c) 雙向檢查（R-G33(d)(2)；乙案 R-DM54）
batch: generated/pilot-01.json
tcs: 3   deferred entries: 3   （未解除 2 / 已解除 1）

| TC | leaf | token | 項之狀態 | 方向 | 判定 |
|---|---|---|---|---|---|
| #1 | SWE1-DM-004 | `warning popup` | 未解除 | MISSING | 含 |
| #2 | SWE1-DM-004 | `warning popup` | 未解除 | MISSING | 含 |
| #3 | SWE1-DM-005 | `protective shutdown` | 未解除 | MISSING | 含 |
| #3 | SWE1-DM-005 | `multi-stage` | **已解除** | STALE | **仍含** |

MISSING = 0   STALE = 1
  STALE    TC#3 SWE1-DM-005 token 'multi-stage' —— 項已解除而括號下半仍載其 token
exit=1

===== (3)(4) 還原後之輸出 =====
# R-G33(c) 雙向檢查（R-G33(d)(2)；乙案 R-DM54）
batch: generated/pilot-01.json
tcs: 3   deferred entries: 3   （未解除 3 / 已解除 0）

| TC | leaf | token | 項之狀態 | 方向 | 判定 |
|---|---|---|---|---|---|
| #1 | SWE1-DM-004 | `warning popup` | 未解除 | MISSING | 含 |
| #2 | SWE1-DM-004 | `warning popup` | 未解除 | MISSING | 含 |
| #3 | SWE1-DM-005 | `protective shutdown` | 未解除 | MISSING | 含 |
| #3 | SWE1-DM-005 | `multi-stage` | 未解除 | MISSING | 含 |

MISSING = 0   STALE = 0
exit=0

還原後連跑兩次 diff：無差異（PASS）
pilot-01.json 對基線 diff：無差異（PASS）
```

**`STALE = 1`，exit 1，逐字指名 `TC#3` / `SWE1-DM-005` / `'multi-stage'`
及其理由「項已解除而括號下半仍載其 token」。停止條件 69 未觸發。**

上輪同一情境（以移除為之）報 `STALE = 0`；本輪（以標記為之）報 1。
**乙案之實作成立。**

還原：`pilot-01.json` 對基線 `diff` 無差異；還原後連跑兩次輸出
逐字元相同。**測試未留下痕跡**（`generated/pilot-01.json` 本輪
最終狀態與 26 輪結束時相同，故不入本包 pathspec）。

---

## 三、24-5 —— 綁定十二項

`cfts013_sysra` 之 sha256 以磁碟實測為準：
`1036b2af9f655441cc01bed6e2780a359334d8b10fca5d1bf693fb7137b911b0`
—— 與 26 輪之量測相同，**停止條件 70 未觸發**。

```text
# reference binding check (R-G23)
feature.yaml: /Users/peihe/Work_Projects/TC_Generator/features/display/feature.yaml
entries: 12

| key | file | declared | actual | verdict |
|---|---|---|---|---|
| a03_report | `Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` | `ab3198e81fb21d21…` | `ab3198e81fb21d21…` | MATCH |
| cfts013_sysra | `SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx` | `1036b2af9f655441…` | `1036b2af9f655441…` | MATCH |
| cfts_doc | `R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` | `8696d1f596e33677…` | `8696d1f596e33677…` | MATCH |
| dbc_b | `PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3db62ac9f…` | `46cb73f3db62ac9f…` | MATCH |
| dbc_fd | `PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf3e670d71…` | `2a86c4bf3e670d71…` | MATCH |
| lid | `Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679c706cd45…` | `a01e1679c706cd45…` | MATCH |
| popup_list | `Pop Up List HMI R1 (26PI).xlsx` | `ff47b7be63e5824c…` | `ff47b7be63e5824c…` | MATCH |
| popup_priority_matrix | `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` | `dc078763c67b5238…` | `dc078763c67b5238…` | MATCH |
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3d58d…` | `e7c2020f01c3d58d…` | MATCH |
| sys2_export | `SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx` | `421c8eef3f5cb01a…` | `421c8eef3f5cb01a…` | MATCH |
| sys3_sysad | `SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` | `be9c97af0211a703…` | `be9c97af0211a703…` | MATCH |
| workbook_master | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` | `6372fb6be02f48dc…` | `6372fb6be02f48dc…` | MATCH |

**12 of 12 match.**
```

**`entries: 12`／12 of 12 match**（R-G26：綠燈連同母體引用）。
停止條件 62 通過。

`entries` 由 11 增為 12 一事本身即為 A-DM30（YAML 縮排使新鍵落入
`lint:` 之下）之防線 —— **若本次縮排有誤，`entries` 會停在 11
而輸出仍是「11 of 11 match」**。故此處具名。

`feature.yaml` 之新項附註記，逐字：

```yaml
  # 24 包步驟 5（27 包解封）：CFTS013 SYSRA 分析報告。R-DM37 之判準——
  # 其為 R-DM51／R-DM52 兩條裁決之事實依據，其變動會使該兩條所據之
  # 量測（32 列／Document ID 全集／629-633-952 之落點）失效，故納入綁定。
  # **納入綁定不等於得自其取值**：R-DM51(a) 之禁止代入不受本項影響。
```

---

## 四、24-4 —— `popup_priority` 之來源登記

### 4.1 產出

腳本：`features/display/scripts/popup_priority_sources.py`（本輪新增）。
**入口呼叫 `verify_reference_binding.py`**（R-G23），失敗即 exit。

```text
# popup_priority_sources —— 來源登記（R-G36 機器抽取）
source : SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx
binding: entries: 12（R-G23 已於入口比對）
母體   : 'Analysis Report' 之資料列 33（第 6 列起）
命中   : 含 popup 指涉之列 **4**

## CFTS013-933  (Functional Requirement)  @ SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx!Analysis Report!r30
   matched_by: phrase   popup_ids: NA   phrases: Screen is Hot ¦ pop up
   When the display touch screen surface has reached a temperature >= 56 degrees C and <60 degrees C and no other higher priority screen is to be shown, the HU shall not lower the screen intensity any further and the HU shall display the "Screen is Hot" warning (See the latest version of the referenced document [*HMI * Logic and Flow*] or [*Pop Up List*] for the "HU Display Hot" screen design).

## CFTS013-934  (Functional Requirement)  @ SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx!Analysis Report!r31
   matched_by: phrase   popup_ids: NA   phrases: Screen is Hot
   While displaying the "Screen is Hot" warning the HU shall "limit" radio HMI functionality by ignoring any "limited" HMI events. See {CFTS013-935} for a definition of "limited" versus "non-limited" HMI events.

## CFTS013-935  (Functional Requirement)  @ SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx!Analysis Report!r32
   matched_by: phrase   popup_ids: NA   phrases: Screen is Hot
   HMI functionality shall be "limited" as follows when the 'Screen is Hot' warning is displayed:_x000D_ _x000D_ - LIST/ENTER knob shall be disabled._x000D_ _x000D_ - All touch screen behavior shall be ignored.

## CFTS013-937  (Functional Requirement)  @ SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx!Analysis Report!r33
   matched_by: id   popup_ids: PU0130   phrases: Display is Hot ¦ Screen is Hot ¦ popup
   While displaying the "Screen is Hot" warning if an event occurs that results in the system transitioning to a state where a screen with higher priority (ex. Rear/Surround View Camera, SOS or Emergency Calls) than the 'Screen is Hot' popup (Popup PU0130, a.k.a. 'Display is Hot') is to be shown, then the HU shall display that screen.

-> features/display/data/popup_priority_sources.tsv
-> popup_priority_sources.tsv.meta.json
```

**`{CFTS013-937}` 之逐字全文已機器抽取**，其對 `PU0130` 之指名
（`the 'Screen is Hot' popup (Popup PU0130, a.k.a. 'Display is Hot')`）
逐字在內 —— **下放包 24 §2.4 之主張至此有了機器來源，不再是轉抄。**

其所載之優先序行為亦在同一句內：
`a screen with higher priority (ex. Rear/Surround View Camera, SOS or
Emergency Calls) than the 'Screen is Hot' popup`。

### 4.1.1 首版只得一列，反向查證後改為四列

本腳本首版之判準為 `\bPU\d{4}\b`，**命中 1 列**（`{CFTS013-937}`）。
該結果滿足 24-4 之字面要求，但我在寫 §七自陳時想到一句話 ——
**「一列是實測，『一列就是全部』不是」** —— 於是先做了反向查證：

```text
反向查證：Description 欄逐列搜以下詞（忽略大小寫）
  ['popup', 'pop-up', 'pop up', 'PU0', 'PU ', '彈出', '快顯', 'screen is hot', 'display is hot']

命中列數 = 4

  r30  CFTS013-933  詞=['pop up', 'screen is hot']
       PU 編號=**無**
       When the display touch screen surface has reached a temperature >= 56 degrees C and <60 degrees C and no other higher priority screen is to be shown, the HU shall not lower the screen intensity any fu

  r31  CFTS013-934  詞=['screen is hot']
       PU 編號=**無**
       While displaying the "Screen is Hot" warning the HU shall "limit" radio HMI functionality by ignoring any "limited" HMI events. See {CFTS013-935} for a definition of "limited" versus "non-limited" HMI

  r32  CFTS013-935  詞=['screen is hot']
       PU 編號=**無**
       HMI functionality shall be "limited" as follows when the 'Screen is Hot' warning is displayed:_x000D_ _x000D_ - LIST/ENTER knob shall be disabled._x000D_ _x000D_ - All touch screen behavior shall be i

  r33  CFTS013-937  詞=['PU0', 'display is hot', 'popup', 'screen is hot']
       PU 編號=['PU0130']
       While displaying the "Screen is Hot" warning if an event occurs that results in the system transitioning to a state where a screen with higher priority (ex. Rear/Surround View Camera, SOS or Emergency
```

**四列提及同一個 popup，只有一列帶編號。** 另三列是它的條件
（`{CFTS013-933}`：`>=56 且 <60 degrees C` 時顯示該警示）與其副作用
（`{CFTS013-934}`／`{CFTS013-935}`：警示顯示中 HMI 功能受限，
LIST/ENTER 旋鈕停用、觸控全部忽略）。

**以編號為唯一判準，會把三分之二的相關條文留給下一個人重查** ——
而來源登記存在的全部理由就是免除那次重查。故改為二擇一判準
（id 或詞表），`matched_by` 欄記何者命中。

**詞表為人所給定**（`popup`／`pop-up`／`pop up`／`Screen is Hot`／
`Display is Hot`），與 B9／B11 同形態，已於腳本註解與 sidecar 之
`measurement_conditions` 兩處具名。

### 4.2 sidecar（R-DM30）

```json
{
 "data_file": "popup_priority_sources.tsv",
 "columns": [
  "source_locator",
  "document_id",
  "category",
  "matched_by",
  "popup_ids",
  "matched_phrases",
  "side",
  "verbatim"
 ],
 "data_rows": 4,
 "generated_by": "features/display/scripts/popup_priority_sources.py",
 "generated_at": "2026-08-25",
 "inputs": [
  "SYS2_CFTS013_Radio_Error_Management-Associated_Display.xlsx (reference: cfts013_sysra)"
 ],
 "measurement_conditions": "openpyxl read_only data_only；sheet='Analysis Report'；表頭列 5，資料自第 6 列；popup id 之抽取式 r'\\bPU\\d{4}\\b'；verbatim 欄為 Description 之空白正規化（' '.join(split())），未改動任何字元內容；綁定檢查 entries: 12",
 "rulings": [
  "R-G36",
  "R-DM51",
  "R-DM30",
  "R-G23",
  "R-G26"
 ],
 "notes": "**來源登記，非仲裁順序表。** 仲裁表待 DR-DM2（BACKLOG A1）。本檔之全部內容為 Associated Display（HU 側）之事實；依 R-DM51(a) 不得代入 DCSD 標的 —— `verbatim` 欄內之溫度值（56／60 degrees C 等）為 HU 顯示器之門檻，**與 DCSD 之 85 無關**。以編號為唯一判準只得 1 列；反向查證後改為二擇一，得 4 列。"
}
```

`generated_by` 為腳本路徑，非「人工登記」——**R-G36 之要求達成**。

### 4.3 三項須具名者

1. **檔名為 `popup_priority_sources.tsv`，非 `popup_priority.tsv`。**
   後者是 A1 之交付物（Pop Up List xlsx × Priority Matrix PDF 之
   仲裁順序表），**待 DR-DM2**。本檔只是來源登記，
   **用同一個檔名會使 A1 看起來像已完成。**
2. **母體之口徑差異**（依本輪新立之 R-G16 口徑要求，先行具名）：
   本腳本報「資料列 33（第 6 列起）」＝ `len(rows) - 5`，
   **未濾全空列**；上繳 26 §6.2 之「32」為**濾去全空列後**之數。
   兩者差一列（末尾之空列）。**非不符，是兩個口徑。**
3. **`side` 欄一律 `HU (Associated Display)`** —— 依 R-DM51，
   本檔全部內容為 HU 側之事實，**不得代入 DCSD 標的**。
   該限定同時寫入 sidecar 之 `notes`。

---

## 五、DR-DM9 之重擬與 A-DM35 之結案

### 5.1 DR-DM9

原文依 R-TM13 不刪不改，其下加「重擬（下放包 27）」註記，含三問與
十列附件表。三問逐字見 `DATA_REQUESTS.md`；附件表為機器輸出
（`cfts_doc` 綁定 MATCH，配對式
`\$([A-Za-z0-9_]+)\$\s*=\s*\[([^\]]+)\]`）：

| 標籤 | `$DCSD_DISP_STAT$` | `$TGW_DISP_STAT$` | DBC `DCSD_DISP_STAT` | 判定 |
|---|---:|---:|---|---|
| `[OFF]` | **85** | 0 | `0 "OFF"` | 解得 raw 0 |
| `[ON]` | **53** | 0 | `1 "ON"` | 解得 raw 1 |
| `[BLANK]` | **20** | 0 | `2 "BLANK"` | 解得 raw 2 |
| `[RR_CMRA]` | **72** | 0 | `3 "RR_CMRA"` | 解得 raw 3 |
| `[DISP_HOT]` | **46** | 0 | `4 "DISP_HOT"` | 解得 raw 4 |
| `[SNA]` | **8** | 0 | `7 "SNA"` | 解得 raw 7 |
| `[DISP_ON]` | 23 | 0 | 查無 | **逐字查無** |
| `[DISP_OFF]` | 12 | **146** | 查無 | **逐字查無** |
| `[DISP_REAR_CAMERA]` | **0** | **107** | — | **非本訊號之值** |
| `[DISP_NORMAL]` | **0** | **99** | — | **非本訊號之值** |

阻斷範圍隨之修正並寫入 DR：**用短拼法之條款不受阻**（007／008 之
RVC 諸條逐字為 `= [RR_CMRA]`）；**用長拼法者仍受阻**
（`{4820287}` 逐字為 `= [DISP_ON]`，即本批 #3 只驗行為之理由）。

### 5.2 A-DM35 結案註記

已加於 A-DM35 節首，記分析層之採認（相容非相衝、判定落在條款層級、
段落 1742 之一句兩訊號為決定性、A3 之縮小自此有據）。

---

## 六、未驗項分流（A／B，R-G29）

### A 類 —— 阻斷交付

| 編號 | 項 | 阻斷什麼 | 索取中 |
|---|---|---|---|
| A1 | 組 A／組 B 何者為準 | 004 popup 側；005 關閉側 | DR-DM10(a) |
| A2 | DCSD 側 warning → off 之分段變數與第二門檻 | 原 #2；`PU0130` | DR-DM10(b) |
| A3 | **長拼法**標籤之對應（`[DISP_ON]` 等） | `{4820287}` 之訊號值；007／008 之 HU 側 | DR-DM9（**已重擬**；短拼法側已解除） |
| A4 | `popup_priority.tsv`（仲裁順序表） | `SWE-DM-006` | DR-DM2（**來源登記本輪完成**） |
| A5 | `sysad_allocation.tsv` | 全 8 leaf 之追溯欄 | DR-DM3 |

~~A6~~（26a 解除）、~~A7~~（**本輪解除：STALE 乙案修畢且測試 PASS**）、
~~A8~~（**本輪解除：六列驗明**）。**A 類自 8 項降為 5 項，本輪無新增。**

### B 類 —— 不阻斷交付

| 編號 | 項 | 狀態 |
|---|---|---|
| B1–B10、B12–B15 | 見上繳 25／26 | 不變；**B13 之阻斷者（24-6 之裁定）已消滅，本輪完成 24-4** |
| ~~B11~~ | token 為自訂對譯 | 25 輪結案 |
| **B16** | **`deferred` 陣列只增不減之長度未實測** | R-DM54 定「逾百項再議」；本 feature 現 3 項，8 leaf 全做完之實數**未估**（見 §七第 1 項） |

B16 為本輪新增。

---

## 七、本包是否仍有該驗而未驗者 —— 獨立判斷

**有三項。**

1. **R-DM54 之規模界（「逾百項再議」）我沒有實測。**
   條文以「8 leaf × 每 leaf 三面向 ≈ 二十餘項」估之，而那是分析層
   替我補的估算（上繳 26 §十第 1 項我自陳未估）。**我本輪仍未估** ——
   004／005 兩個 leaf 已產生 3 項，若其餘六個 leaf 之面向數相仿，
   約 12 項；但 006（popup 仲裁）與 007／008（RVC）之 deferred
   面向可能遠多於此。**條文之界未被任何量測支持，我只是接受了它。**

2. **`lifted` 三鍵之寫入路徑不存在。**
   R-DM54 定解除須增 `lifted`／`lifted_at`／`lifted_by`，
   `check_disclosure.py` 讀得懂它們 —— **但沒有任何腳本會寫它們**。
   本輪之誘發測試是我手寫 JSON 塞進去的。真正解除發生時，
   仍是人去編輯 JSON，**而人編輯 JSON 正是 R-DM53 想從檢查端移走的
   那類判斷，現在它出現在解除端**。

3. **`{CFTS013-933}` 之 `>=56 且 <60 degrees C` 現在躺在一份 `data/` 檔裡。**
   反向查證使登記由 1 列增為 4 列（§4.1.1），這是改善；
   **但它同時把 CFTS013 之溫度門檻寫進了本 feature 之資料檔。**
   R-DM51(a) 禁止的是「代入 DCSD 標的」，登記不是代入，
   且 `side` 欄與 sidecar 之 `notes` 都寫明了 ——
   **但停止條件 60 只掃 TC 與 `batch_context.md`，不掃 `data/`。**
   即：現在有一條路徑可以讓 56／60 這兩個數字進到交付面而不觸發任何檢查。
   我判斷登記仍應保留（其價值大於該風險），**但這道缺口是我開的**。

---

## 八、建議之 commit 訊息與 pathspec（**未執行**）

```bash
git add \
  features/display/feature.yaml \
  features/display/scripts/check_disclosure.py \
  features/display/scripts/popup_priority_sources.py \
  features/display/data/popup_priority_sources.tsv \
  features/display/data/popup_priority_sources.tsv.meta.json \
  features/display/RULINGS.md \
  features/display/ANOMALIES.md \
  features/display/DATA_REQUESTS.md \
  features/display/BACKLOG.md \
  features/display/docs/INDEX.md \
  features/display/docs/handoff/24_cfts013.md \
  features/display/docs/handoff/26_extraction_principle.md \
  features/display/docs/handoff/26a_materials_landed.md \
  features/display/docs/handoff/27_stale_fix.md \
  features/display/docs/upstream/26_extraction_principle.md \
  features/display/docs/upstream/27_stale_fix.md \
  docs/fw036/RULINGS_LEDGER.md
```

```text
feat(display): lift a deferral by marking it, not by deleting it

- add R-DM54: the deferred array only grows; an entry is lifted by adding
  lifted / lifted_at / lifted_by, so the token stays in the candidate set
- rewrite check_disclosure.py accordingly: MISSING over unlifted entries,
  STALE over lifted ones, cross-leaf misplacement unchanged
- the induced test now reports STALE = 1 on the case that reported 0 before
- verify the six CFTS013 rows that are not All: five are blank Information
  rows and one is a PowerNet heading, while all eleven functional
  requirements are All, so the concern is closed
- record A-DM37: three of those Information rows are leftover template text
  carrying real document ids
- bind the CFTS013 workbook, taking the reference set to twelve
- register the popup sources by machine extraction; searching by id alone
  found one row, searching by phrase as well found the three rows that carry
  the condition and the side effects
- reword DR-DM9: two of its four labels belong to the HU-side signal, and
  six labels on the DCSD-side signal already resolve against the DBC
```

> `generated/pilot-01.json` **未變更**（誘發測試已逐字元還原），不入。
> `batches/pilot-01/batch_context.md` 由 `.gitignore` 排除，不入。
> 036 母本未變更，亦不入。
> 本 pathspec 併入上繳 26 之檔案（26 輪建議之 commit 未執行）。
