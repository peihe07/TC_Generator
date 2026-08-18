# 上繳包 23 —— OR 分支閘門、台帳補洞與第四批

> 對應下放包：`features/power/docs/handoff/23_or_branch.md`
> 執行層：Claude（TC_Generator）
> **§J 自檢已先驗**：§A fenced block = **8**、§J 列數 = **8**、§H 步驟 9 = 「**八條**」——
> **三處一致，未停。**
> 本包**未執行任何 git 子命令**（R-P149）；**未對任何 workbook 呼叫 `save()`**；
> **未觸碰客戶樹與 `inputs/`**；**未為求 G113 重現七項而調整抽取規則**；
> **未自行補齊 layer3**；**未合併或拆分 `SWE-PM-025` 之八條**；
> **`SWE-PM-001`–`010` 未納入任何批次**；**第四批未啟動**（見 §五）。

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**

**編號查核（R-P147，先查後開）**：
**A-PW 最大 119、R-P 最大 160、DR-PW 最大 11、閘門最大 G112。**
本包新號自 **A-PW120 / R-P161 / G113** 起；**DR-PW9 依 R-P164 補開**（21 包保留之號）。

---

## 一、B1 —— G113 OR 分支閘門（最高優先）

### 1.1 判準

自 `source_clause` 抽 `OR` / `or` / `nor` 之並列，成**分支組**（不限二元）；
以各支之**獨有實詞**（該支有而 sibling 支皆無者）是否見於該 leaf 之**任一 TC** 為判準；
未覆蓋者**不判 FAIL**，入 R-P76 之待人工裁決類。
正規化限於分隔符層（黏連之 `OR` 補空白、換行視為句界、連接詞不分大小寫）。

### 1.2 驗證條件 —— **2 / 7**

| 實例 | 結果 | 漏檢形態 |
|---|---|---|
| 16 包 `BODY OFF-TIMED` | **重現** | 缺 `off-tim` |
| 18 包 `Ignition Pre Off` | **重現** | 缺 `pre` |
| 17 包 `greater` 負分支 | **未重現** | **根本不是 OR 結構** —— 原文為 `and if the volume was greater`，條件句 |
| 22 包 VR 長按 | **未重現** | **根本不是 OR 結構** —— 原文為 `both short and long presses` |
| 22 包 Behaviour 1 之 LTM High | **未重現** | OR 之右運算元以 `( If …` 起首，`IF` 在分隔符集合內 → 運算元被截至長度不足而丟棄 |
| 22 包 Behaviour 2 之 LTM High | **未重現** | 同上 |
| 22 包 `028` 之 LTM High | **未重現** | 同上 |

**首版更為 0 / 7** —— 定界以「自 OR 向左**反轉**搜尋分隔符」為之，
而反轉字串配上正向詞邊界樣式（`THEN` / `AND`）**永不匹配**，左界一路退到句首。
**此為實作瑕疵，判準一字未改**；已修正並於程式碼註記（A-PW124）。

> **後三項可由分隔符集合之調整（自 `IF` 移出邊界，或令括號具保護性）達成重現。
> 執行層未為之** —— 23 §I 明令「不得為求 G113 重現七項而調整抽取規則」。
> **呈請裁定。**

### 1.3 **G113 於現況資料之首次真實命中 —— 第八、第九例**

| leaf | 錨點 | 原文 | 首寫所取 |
|---|---|---|---|
| `SWE-PM-014` | `4941504` | `Ignition Pre Off` **OR** `Ignition Off` | 僅 `Ignition Off` |
| `SWE-PM-018` | `4941548` | `Ignition Pre Off` **OR** `Ignition Off` | 僅 `Ignition Off` |

**與前七例同型，惟本次係由閘門於現況資料上攔下，非事後由反向涵蓋抓到。**
已依 R-P161(c) 裁為真缺口並補二條，**第三批 61 → 63、全批 106 條**（A-PW125）。

### 1.4 噪音實測

全批未覆蓋分支 **55**，真陽性 **2** —— **3.6%**（A-PW126）。
多數為運算元被分隔符切在語義中間（`Info is equal to "Ignition Pre Off`、
`to "Ignition Off" valueAND STATUS_BH_BCM2`）。**未調整判準以降噪。**
惟其產出量（55）遠小於透鏡 3（452），逐項裁決仍可行。

---

## 二、B2 —— G103 全量掃描（R-P162 / G114）

## (a) 不相等之 leaf —— **2 / 115**

| leaf | 037 token 數 | 重算 item 數 | layer3 item 數 | **layer3 缺** | layer3 多 |
|---|---|---|---|---|---|
| `SWE-PM-008` | 13 | 17 | 14 | **4941425、4941430、4941433** | — |
| `SWE-PM-010` | 8 | 8 | 7 | **4941984** | — |

其餘 **113 leaf 全數相等**；全量之 unresolved token 為 **0**。

## (b) 被丟棄之 item 於兩份 CFTS 文字層之存在情形

| item id | 所屬 leaf | CFTS009 / CFTS010 文字層之內文段落 | 判讀 |
|---|---|---|---|
| `4941425` | `SWE-PM-008` | **無**（`anchor_bodies()` 查無該錨點）| 該 item 於 CFTS 本文中不存在 |
| `4941430` | `SWE-PM-008` | **無**（`anchor_bodies()` 查無該錨點）| 該 item 於 CFTS 本文中不存在 |
| `4941433` | `SWE-PM-008` | **無**（`anchor_bodies()` 查無該錨點）| 該 item 於 CFTS 本文中不存在 |
| `4941984` | `SWE-PM-010` | **無**（`anchor_bodies()` 查無該錨點）| 該 item 於 CFTS 本文中不存在 |

**四個被丟棄之 item 全部於文字層不存在** —— 非「有內文而章節解析失敗」，
而是 **037 → SYS2 所指之 item id 在 CFTS 文件裡根本沒有對應之需求錨點**。
`build_layer3` 以「item → 章節」為索引建表，該等 item 因無章節而**靜默丟棄**，
`layer3_full.tsv` 遂少載，`source_anchor` 隨之少列，而 **G94 與 G99 皆會全綠**。

## (c) 與既有 anomaly / DR 之關聯

| 既有項 | 關係 |
|---|---|
| **A-PW02 / DR-PW3**（`4942087` 無法解析至任一 CFTS 章節）| **同型之最早一例** —— 當時判為「錨點鏈之缺口」，未查其內文是否存在。本次四例證明該形態會**靜默改變 `source_anchor`**，其後果較當時所評估者嚴重 |
| **DR-PW11**（`4941984`，22 包開）| 本次擴大為 **4 個 item / 2 個 leaf**，已併入該 DR |
| **DR-PW6**（`SWE-PM-001`–`009` 之懸空 `WrapperResource`）| `SWE-PM-008` 同時受此二者影響 —— 其 TC 於 DR-PW6 與 DR-PW11 皆解之前無法產出 |

**執行層未自行補齊 layer3**（R-P162 明令）。


---

## 三、B3 —— 21 包補執行（R-P164 / G115）

| 步驟 | 產出 | 結果 |
|---|---|---|
| §H 3（B1）| DR-PW9（High）已開；R-P7 加註 | **G107 UNCHANGED**（388 bytes，SHA256 前後同為 `8ba43d3f…0cd4`）|
| §H 4（B2）| `check_edit_integrity.py`（**G108**）| 三案 fixture 如期；7 檔 163 符號之基準快照 |
| §H 5（B3）| A-PW02 / DR-PW3 / R-P151 交叉指引 | 三處已互相標註 |
| §H 6（B4）| 第二批狀態快照 | `data/b4_batch2_snapshot.md` |
| §H 8 | 五條依原編號抄入 | **`RULINGS.md` 現為 R-P1 – R-P160 連續無缺** |

**G108 之三層檢查**：語法（`ast.parse`）／載入（`importlib`）／
**符號**（頂層函式、類別、常數集合對基準快照）。
fixture 以 **20 包之實際損壞形態**建構 —— 自 `lint_tcs.py` 刪去四個函式：
**語法仍 True 而符號層攔下**。

> **須據實回報**：G108 **不保證「同一步內完成」** ——
> 它是一道可執行之檢查，**何時執行仍靠執行者**。
> 本包之作法為每次編輯後立即跑 lint（其 import 即涵蓋載入層），
> 並於結束前跑全檔檢查。**這是紀律加工具，不是機制**（A-PW111）。

**一項不可回溯之事實**：B4 快照之 SHA256 **取自 23 包當下**，
**非 21 包當時之值** —— 22 包已對第二批作 R-P153 ~ R-P157 之修改。
該值已不可回溯取得，如實記明。

**`Sys-RA-PM-0293` 之逐字值**：`HARMAN Status` = **`Need rework`**、`MD Status` = 空。
037 引用者為 `SWE-PM-112`，**不在已產出之 33 leaf 內**。

---

## 四、B4 —— `SWE-PM-025` 之裁定素材（R-P167）

## 2. 二組之全部屬性逐欄比對

### `4941569` vs `4941572` —— **相異：ECU**

| 屬性 | `4941569` | `4941572` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, RRM | LTM, RRM, ETM | **否** |
| EE Architecture | Atlantis High, Atlantis Mid | Atlantis Mid, Atlantis High | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

### `4941570` vs `4941573` —— **相異：ECU**

| 屬性 | `4941570` | `4941573` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | RRM, LTM | RRM, ETM, LTM | **否** |
| EE Architecture | Atlantis High, Atlantis Mid | Atlantis High, Atlantis Mid | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

### `4941571` vs `4941574` —— **相異：ECU**

| 屬性 | `4941571` | `4941574` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, RRM | ETM, RRM, LTM | **否** |
| EE Architecture | Atlantis Mid, Atlantis High | Atlantis Mid, Atlantis High | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

## 3. 八條之 `tc_title` / `split_reason` 對照

| tc_id | split_index | tc_title | split_reason |
|---|---|---|---|
| `083` | 1 | Front_Panel_OnOff.Req press in Timed with an active call shows a popup | 本條驗 Front_Panel_OnOff.Req ＋ 通話中之 popup |
| `084` | 2 | Accepting the Front_Panel_OnOff.Req popup passes the TLM to Standby | 本條驗 Front_Panel_OnOff.Req popup 之接受分支 |
| `085` | 3 | Declining the Front_Panel_OnOff.Req popup keeps the TLM in Timed | 本條驗 Front_Panel_OnOff.Req popup 之拒絕分支 |
| `086` | 4 | Front_Panel_OnOff.Req press in Timed with no active call passes to Standby | 本條驗 Front_Panel_OnOff.Req ＋ 無通話之直接轉換 |
| `087` | 5 | CLIMATIC_PANEL.Radio_Btn0 press in Timed with an active call shows a popup | 本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ 通話中之 popup |
| `088` | 6 | Accepting the CLIMATIC_PANEL.Radio_Btn0 popup passes the TLM to Standby | 本條驗 CLIMATIC_PANEL.Radio_Btn0 popup 之接受分支 |
| `089` | 7 | Declining the CLIMATIC_PANEL.Radio_Btn0 popup keeps the TLM in Timed | 本條驗 CLIMATIC_PANEL.Radio_Btn0 popup 之拒絕分支 |
| `090` | 8 | CLIMATIC_PANEL.Radio_Btn0 press in Timed with no active call passes to Standby | 本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ 無通話之直接轉換 |

## 4. 執行層之陳述（非建議）

二組錨點之內文**逐字比對結果**：`4941569` 與 `4941572` 之差異僅在觸發訊號名
（`Front_Panel_OnOff.Req` vs `CLIMATIC_PANEL.Radio_Btn0`），其餘一字不差；
`4941570` / `4941573` 與 `4941571` / `4941574` 亦然。

執行層當時之依據為 **§5.7「不同觸發即拆分」**，與 `SWE-PM-015` / `SWE-PM-019`
之處置一致（該二 leaf 之二鍵亦各自成條）。
**若本 leaf 裁為應合併，則 `SWE-PM-015`（4 條）與 `SWE-PM-019`（4 條）
之拆法同受影響** —— 三個 leaf 合計 16 條之其中 8 條將消失。

**執行層不就此提出建議**（R-P167 明訂裁定於 24 包）。


---

## 五、B5 —— **第四批未啟動**

R-P161 明訂「**G113 為第四批之前置條件 —— 未就位不得啟動第四批**」，
而 §D 對 G113 之期望值為「**七項已知實例全數重現**」。**實測 2 / 7。**

執行層之判斷：G113 已實作、已執行、驗證條件已如實回報，**惟期望值未達成**。
於此情形啟動第四批，即為「**前置未達而照樣前進**」——
該形態正是本專案歷次修正之對象（R-P132(d)、R-P124、R-P152 皆為前置條件之設立）。
**故不啟動，停並上繳。**

### 5.1 已完成之準備 —— 依 R-P165 之 live DR 影響面查核

Power State 剩餘 **31 leaf（`SWE-PM-033`–`063`）**：

| live DR | 影響面 | 是否及於該 31 leaf |
|---|---|---|
| DR-PW5（High）| `SWE-PM-003` | **否** |
| DR-PW6（Medium）| `SWE-PM-001`–`009` | **否** |
| DR-PW8（High）| `015`（TC，屬第一批）| **否** |
| DR-PW9（High）| `SWE-PM-112` | **否** |
| DR-PW10（Medium）| `037` / `039` / `042`（TC，屬第二批）| **否** |
| DR-PW11（High）| `SWE-PM-008` / `SWE-PM-010` | **否** |
| DR-PW1（High）| `SWE-PM-089` | **否** |
| DR-PW3 / DR-PW7 | 不阻斷任何 leaf | **否** |

> **第四批之 31 leaf 不受任何 live DR 影響，範圍為 `SWE-PM-033`–`063`。**
> **裁定 G113 之處置後即可啟動。**

---

## 六、§D 全表自驗

| # | 項目 | 期望值 | **實測** | 判定 | 證據型別 |
|---|---|---|---|---|---|
| **G0** | 素材同一性 | 7 / 7 | 7 / 7 | **PASS** | 真實 |
| **G113** | OR 分支涵蓋 | **七項已知實例全數重現**；輸出入待裁類不判 FAIL | **2 / 7**（二項非 OR 結構、三項因括號內 `If` 被截斷）；未覆蓋 55 項入待裁類，不判 FAIL；**現況資料真實命中 2 項** | **期望值未達成 —— 已如實回報，第四批因此未啟動** | 合成＋真實 |
| **G114** | G103 全量 | 115 leaf 掃畢；不相等清單與差集；每個被丟棄 id 之存在情形 | **115 掃畢**；不相等 **2**（`SWE-PM-008` 三個、`SWE-PM-010` 一個）；**四個 item 於文字層皆無內文段落** | **PASS** | 真實 |
| **G115** | 21 包補執行 | R-P148 ~ R-P152 已入 RULINGS，編號無重無缺；缺口記已更新 | **R-P1 – R-P160 連續無缺**；22 包缺口記與 INDEX 未執行列已更新 | **PASS** | 真實 |
| **G116** | 第四批產出 | leaf 數、TC 數、排除清單與 DR 編號 | **未啟動** —— G113 期望值未達成（R-P161 之前置）；範圍已備妥（31 leaf，不受任何 live DR 影響）| **未執行（附依據）** | —— |
| **G107** | R-P7 加註後原文位元組未變 | UNCHANGED | SHA256 前後同，388 bytes | **UNCHANGED** | 真實 |
| **G108** | 編輯完整性檢查 | 已納入作業規則；刻意刪函式之案例證明會攔下 | 三層檢查；**刪四函式時語法 True 而符號層攔下**；三案如期 | **PASS** | **合成＋真實** |
| **G70** | lint 全閘 | 全 PASS | `exit=0`；阻斷類 PASS；**TC 106、leaf 33** | **PASS** | 真實 |
| G94 / G99 / G103 | 沿用 | 期望值不變 | 33 / 33 皆相等 | **PASS** | 合成＋真實 |
| G1–G112 | 沿用 | 期望值不變 | `--self-test` **35 / 35 TC fixture ＋ G46 皆如期** | **PASS** | 混合 |

---

## 七、執行層對「本包是否仍有該驗而未驗者」之獨立判斷

分析層於 §K 自判三項（G113 為七次事後補救後才立、第三批未覆核、
`SWE-PM-025` 裁定將牽動 TC 數），執行層無異議，**本節不覆述**。

**（甲）本包新產生或新暴露之該驗而未驗者 —— 五項**

1. **G113 只重現 2 / 7，而其中三項之不重現我知道怎麼修但沒有修。**
   `IF` 在分隔符集合內是我自己設的；把它移出或讓括號具保護性即可重現。
   **我沒有做，是因為 §I 明令不得為求重現而調整抽取規則** ——
   但這意味著**現在交出去的是一個我知道可以更好而刻意沒改的閘門**。
   這個克制是否正確，我不確定；我把判斷交給分析層，並把修法寫明。

2. **G113 的真陽性率 3.6%（2 / 55），而它的 55 項全部要人裁決。**
   我在本包裁了 55 項（2 真、53 偽）。**第四批 31 leaf 的量會大得多。**
   R-P166 已把透鏡 1 的裁決負擔降下來，**而 G113 立刻又加了一份回去**。

3. **G114 掃出 `SWE-PM-008` 缺三個 item，而該 leaf 早已因 DR-PW6 排除。**
   換句話說：**如果沒有 DR-PW6，我在 22 包就會用一份缺三個錨點的
   `source_clause` 去寫它的 TC，而 G94 / G99 都會全綠。**
   G103 是 20 包才有的；**在它之前產出的第一、二批，其 leaf 是否也曾如此，
   我是靠現在的全量掃描回頭確認的（結果為無）** —— 那是運氣，不是流程。

4. **21 包的 B4 快照我交了一個時序上不對的值。**
   R-P164 要我補執行 §H 3–9，而 B4 要的是「現行狀態快照」供覆核第二批。
   我交的 SHA256 是 23 包當下的，**22 包已經改過第二批**。
   我標明了這一點，但**這份快照對「覆核 21 包當時的第二批」這個原始用途已經無效**。

5. **`SWE-PM-025` 的素材顯示三對僅 `ECU` 相異 —— 而我沒有能力判斷 `ECU` 差異是否重要。**
   `LTM, ETM, RRM` 與 `RRM, LTM, ETM` 之外，實質差異見素材表。
   **若 `ECU` 相異即為變體登載，則本 leaf 與 R-P135 之三對同型**，
   而那三對的裁定至今未下（DR-PW10）。**兩件事可能該一起裁。**

**（乙）已驗而應標明其強度不足者 —— 一項**

6. **「第四批 31 leaf 不受任何 live DR 影響」是我逐一比對 DR 表得出的。**
   比對的是**各 DR 的「阻斷何物」欄所載之 leaf 清單**。
   若某張 DR 的實際影響面大於它自己欄位所寫的（如 DR-PW6 之影響面
   是後來才由 B2 v2 逐 leaf 算出的），**這個查核就會漏**。

**（丙）本包自身之作業瑕疵 —— 一項**

7. **G113 首版的定界邏輯（反轉字串 ＋ 正向詞樣式）是明顯錯的，
   而我是在看到 0 / 7 之後才去查為什麼。**
   若七項驗證條件不存在，我很可能就把那個版本交出去了 ——
   **它會安靜地回報「未覆蓋分支 0」而看起來像通過。**
   R-P161(d) 的驗證條件在這裡起了它該起的作用，這點值得記下。

---

## 八、DATA_REQUESTS

**DR-PW9（High）補開**（R-P148 / R-P164）；**DR-PW11 擴大**為 4 item / 2 leaf（R-P162）。
現存 live：DR-PW1、DR-PW5、DR-PW8、**DR-PW9**、**DR-PW11**（High）；
DR-PW3、DR-PW6、DR-PW10（Medium）；DR-PW7（Low）。DR-PW2、DR-PW4 維持撤回。

---

## 九、產出檔案

| 檔案 | 說明 |
|---|---|
| `features/power/scripts/or_branch_coverage.py` | **G113（新增，含七項驗證條件之 self-test）** |
| `features/power/scripts/check_edit_integrity.py` ＋ `data/edit_integrity_baseline.json` | **G108（新增，21 包補執行）** |
| `features/power/data/g113_or_branch.md` | G113 報告（新增）|
| `features/power/data/g114_layer3_full.md` | G103 全量掃描（新增）|
| `features/power/data/b4_swepm025_material.md` | `SWE-PM-025` 裁定素材（新增）|
| `features/power/data/b4_batch2_snapshot.md` | 第二批狀態快照（新增，21 包補執行）|
| `features/power/generated/batch_003_power_state_a.json` | G113 命中之二條補測（改，61 → 63）|
| `features/power/DATA_REQUESTS.md` | DR-PW9 補開、DR-PW11 擴大、DR-PW3 交叉指引（改）|
| `features/power/RULINGS.md` | **R-P148 ~ R-P152 補抄** ＋ R-P161 ~ R-P168 ＋ R-P7 加註（改）|
| `features/power/ANOMALIES.md` | A-PW120 ~ A-PW127、A-PW02 / 110 / 111 / 118 / 119 更新（改）|
| `features/power/docs/upstream/21_need_rework.md` | 21 包上繳（新增，補執行）|
| `features/power/docs/upstream/23_or_branch.md` | 本檔（新增）|
| `features/power/docs/INDEX.md` | 第 21 / 23 輪索引（改）|
