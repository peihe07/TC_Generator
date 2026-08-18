# 上繳包 30 —— 台帳重複閘、涵蓋缺口登記與兩項複核

> 對應下放包：`features/power/docs/handoff/30_ledger_dup.md`
> 執行層：Claude（TC_Generator）
>
> **§J 自檢二次皆一致（R-P200(c)）**：開工時與抄錄條文前皆為
> §A block **6** / §J 列數 **6** / §H 步驟 10「**六條**」；
> 檔案 **9965 bytes、mtime 08-18 16:15:29 均未變**。
>
> 本包**未執行任何 git 子命令**；**未對 workbook 呼叫 `save()`**；
> **未觸碰客戶樹與 `inputs/`**；**寫回仍未開放**；
> **未以臨時加驗取代常設閘門**（G146 已實作）；
> **未使合規修正之涵蓋缺口靜默消失**（已開 DR-PW15）；
> **未自行修改 `SWE-PM-064` 之 Timed 判斷**；
> **本包所引之腳本產物皆已重跑並載明比對結果**（R-P220）。

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**

**編號查核（R-P147，先查後開）**：
**R-P 最大 214（1–214 連續）、A-PW 最大 155、DR-PW 最大 14、閘門最大 G145。**
本包新號：**R-P215–R-P220**、**A-PW156–A-PW159**、**G146–G149**、**DR-PW15**。

---

## 一、B1 —— 20 項 (b) 型 `pre_conditions` 逐項表（R-P217 / G147）

> **依 R-P217 置於上繳包最前，供分析層以原始素材複核。**
> 由 `scripts/audit_precond_state.py` 自動產出；
> **前提行為逐字轉錄未經改寫**；第 5 / 6 欄摘自 29 包所寫入各該 leaf 之
> `reasoning`，**非本包新增之判斷**。
> **執行層不就其正確性作任何主張**（R-P214）。


> 欄位依 R-P217：`tc_id` / `leaf` / **前提行逐字** / 該狀態值是否見於 clause / 執行層所載之選擇依據 / 待驗行為是否隨該狀態而異。
> **前提行為逐字轉錄，未經改寫**；後二欄取自該 leaf 之 `reasoning`。

| # | tc_id | leaf | 前提行（逐字）| 見於 clause | 選擇依據 | 行為隨狀態而異 |
|---|---|---|---|---|---|---|
| 1 | `NR1L-PowerManagement-018` | `SWE-PM-057` | `3. The TLM is in Full-Operation status` | **否**（`Full`）| 規格他處明文 —— `SWE-PM-061` clause 載「These settings could be only done in TLM Full-Operation Status」 | **是**；否定側由 `SWE-PM-061` 之 `024` 承擔（§8.2.1） |
| 2 | `NR1L-PowerManagement-019` | `SWE-PM-057` | `3. The TLM is in Full-Operation status` | **否**（`Full`）| 規格他處明文 —— `SWE-PM-061` clause 載「These settings could be only done in TLM Full-Operation Status」 | **是**；否定側由 `SWE-PM-061` 之 `024` 承擔（§8.2.1） |
| 3 | `NR1L-PowerManagement-020` | `SWE-PM-057` | `3. The TLM is in Full-Operation status` | **否**（`Full`）| 規格他處明文 —— `SWE-PM-061` clause 載「These settings could be only done in TLM Full-Operation Status」 | **是**；否定側由 `SWE-PM-061` 之 `024` 承擔（§8.2.1） |
| 4 | `NR1L-PowerManagement-021` | `SWE-PM-060` | `2. The TLM is in Full-Operation status` | **否**（`Full`）| 同 `SWE-PM-057`（`SWE-PM-061` 之明文） | **是**；否定側由 `024` 承擔 |
| 5 | `NR1L-PowerManagement-022` | `SWE-PM-060` | `2. The TLM is in Full-Operation status` | **否**（`Full`）| 同 `SWE-PM-057`（`SWE-PM-061` 之明文） | **是**；否定側由 `024` 承擔 |
| 6 | `NR1L-PowerManagement-024` | `SWE-PM-061` | `1. The TLM is in Timed status` | **否**（`Timed`）| 否定側需一非 Full-Operation 狀態；`Timed` 為 §E 既有狀態 | **是，而本條所驗即該差異**；規格僅二分，取任一即足 |
| 7 | `NR1L-PowerManagement-025` | `SWE-PM-062` | `2. The TLM is in Full-Operation status` | **否**（`Full`）| 同 `SWE-PM-057`（`SWE-PM-061` 之明文） | **是**；否定側由 `024` 承擔 |
| 8 | `NR1L-PowerManagement-026` | `SWE-PM-062` | `2. The TLM is in Full-Operation status` | **否**（`Full`）| 同 `SWE-PM-057`（`SWE-PM-061` 之明文） | **是**；否定側由 `024` 承擔 |
| 9 | `NR1L-PowerManagement-027` | `SWE-PM-062` | `2. The TLM is in Full-Operation status` | **否**（`Full`）| 同 `SWE-PM-057`（`SWE-PM-061` 之明文） | **是**；否定側由 `024` 承擔 |
| 10 | `NR1L-PowerManagement-030` | `SWE-PM-064` | `2. The TLM is in Timed state` | **否**（`Timed`）| 他 leaf 之定義 —— `Timeout1` 之計時與到期依 `SWE-PM-038` / `063` 發生於 Timed | **規格未載** —— 依據為他 leaf 明文而非推定，故不列待查（**R-P218 送複核**） |
| 11 | `NR1L-PowerManagement-076` | `SWE-PM-019` | `3. Rear_Camera_Enable.Info reads "False"` | **否**（`False`）| clause 之 ELSE 分支即該條件不成立；布林訊號之唯一否定值 | **是**，二分支皆已成條 |
| 12 | `NR1L-PowerManagement-078` | `SWE-PM-019` | `3. Rear_Camera_Enable.Info reads "False"` | **否**（`False`）| clause 之 ELSE 分支即該條件不成立；布林訊號之唯一否定值 | **是**，二分支皆已成條 |
| 13 | `NR1L-PowerManagement-098` | `SWE-PM-027` | `2. Antitheft_Activation.Req reads "True"` | **否**（`True`）| clause 之「set … **back to** `False`」蘊含起始為 `True` | **是** —— 起始若已為 `False` 則無可觀察變化 |
| 14 | `NR1L-PowerManagement-099` | `SWE-PM-027` | `3. Antitheft_Activation.Req reads "True"` | **否**（`True`）| clause 之「set … **back to** `False`」蘊含起始為 `True` | **是** —— 起始若已為 `False` 則無可觀察變化 |
| 15 | `NR1L-PowerManagement-100` | `SWE-PM-028` | `2. Antitheft_Activation.Req reads "True"` | **否**（`True`）| 同 `SWE-PM-027` | **是**，同 `SWE-PM-027` |
| 16 | `NR1L-PowerManagement-102` | `SWE-PM-028` | `2. Antitheft_Activation.Req reads "True"` | **否**（`True`）| 同 `SWE-PM-027` | **是**，同 `SWE-PM-027` |
| 17 | `NR1L-PowerManagement-104` | `SWE-PM-029` | `2. Antitheft_Activation.Req reads "True"` | **否**（`True`）| 同 `SWE-PM-027` | **是**，同 `SWE-PM-027` |
| 18 | `NR1L-PowerManagement-107` | `SWE-PM-029` | `2. Antitheft_Activation.Req reads "True"` | **否**（`True`）| 同 `SWE-PM-027` | **是**，同 `SWE-PM-027` |
| 19 | `NR1L-PowerManagement-110` | `SWE-PM-031` | `3. The TLM is in Standby state` | **否**（`Standby`）| 測試可執行性需一具體狀態；`Standby` 為 §E 既有狀態 | **否** —— clause 逐字載 `regardless of TLM_Status.Info and $Telematic_Power$ value` |
| 20 | `NR1L-PowerManagement-187` | `SWE-PM-094` | `2. The HU is in STANDBY MODE` | **否**（`STANDBY`、`MODE`）| 他 leaf 明文 —— `SWE-PM-093` 列三模式，此為其一 | **無法說明** —— clause 一字未載；已標待查並開 **DR-PW14** |

**分布**：`Full-Operation` 8 條（`057` / `060` / `062`）、`True` 6 條
（`027` / `028` / `029`）、`Timed` 2 條（`061` / `064`）、`False` 2 條（`019`）、
`Standby` 1 條（`031`）、`STANDBY MODE` 1 條（`094`）。

---

## 二、B2 —— `091` / `092` 涵蓋缺口（R-P216 / G148）

### 2.1 clause 逐字與逐詞掃描

| leaf | clause |
|---|---|
| `SWE-PM-090` | `If the "Theme Mode" setting is set to "Auto" the HU shall use the $Day_Night_Mode$ to determine which of the themes to show` |
| `SWE-PM-091` | `If the "Theme Mode" setting is set to "Day" the HU shall use the Day theme` |
| `SWE-PM-092` | `If the "Theme Mode" setting is set to "Night" the HU shall use the Night theme` |

逐詞掃描 `regardless` / `override` / `irrespective` / `instead` /
`day_night_mode` / `priority` / `precede` / `takes` ——
**`091` 與 `092` 八詞皆無。**

### 2.2 判定與處置 —— **(b) clause 未載該機制**

**已開 DR-PW15**，載明「`Auto` 時明文跟隨訊號，而 `Day` / `Night` 時是否無視該訊號，
規格一字未載」，並請上游確認衝突時應採何主題。
二 leaf 之 `reasoning` 已記入涵蓋缺口登記，**未使其靜默消失**。

**執行層之補充**：本缺口係 29 包依 R-P211 移除注入所生 ——
移除是對的（該命題不在 clause 內），**而其代價直到本條才被登記**。

---

## 三、B3 —— `SWE-PM-064` 素材（R-P218）**未修改**

### 3.1 `source_clause` 逐字（錨點 `4941718`，§1.6.4.1）

```
MaxCallTimeout starts in the following two conditions: Timeout1 == 00 min: IF Phone_Call.Info is equal to “Active” in TLM Full-Operation state, AND the Ignition working condition switches to "Ignition Pre Off" OR to "Ignition Off";   Timeout1 <> 00 min: at Timeout1 expiration, only IF Phone_Call.Info is still equal to “Active”;
```

### 3.2 所涉 TC

| tc_id | tc_title | split_reason | pre_conditions |
|---|---|---|---|
| `029` | MaxCallTimeout starts on ignition off with Timeout1 at 00 min | 本條驗啟動條件一：Timeout1 == 00 min 且點火轉為 Pre Off 或 Off | Timeout1 `"00 min"` / TLM 於 **Full-Operation** / Phone_Call.Info `"Active"` |
| `030` | MaxCallTimeout starts at Timeout1 expiry with the call still active | 本條驗啟動條件二：Timeout1 到期時通話仍為 Active | Timeout1 非 `"00 min"` / TLM 於 **Timed** / Phone_Call.Info `"Active"` |

### 3.3 `reasoning` 全文

其含 27 包補寫之「關鍵情境條件」與 29 包之 R-P210 (b) 型處置，
後者逐字載：(i) 依據為他 leaf 之定義（`SWE-PM-038` / `063`）；
(ii)「行為是否隨狀態而異：**規格未載**」，惟「依據為他 leaf 之明文而非推定，故不列待查」。

### 3.4 執行層認為可能被推翻之具體理由

1. **clause 之第二條件根本未載狀態** —— 其逐字為
   `Timeout1 <> 00 min: at Timeout1 expiration, only IF Phone_Call.Info is still equal to "Active";`，
   通篇無任何狀態名；而第一條件明載 `in TLM Full-Operation state`。
   **同一 clause 內，一個條件載了狀態、另一個沒載** ——
   這可能表示「第二條件不限狀態」，而非「其狀態需自他處推得」。
   若如此，`030` 之 `Timed` 前提**縮小了該條件之適用範圍**。

2. **我的 (i)(ii) 之間不一致** —— (ii) 自陳「規格未載」，卻仍判其不列待查，
   理由是「依據為他 leaf 明文而非推定」。
   **而 `SWE-PM-094` 之 (i) 同樣是他 leaf 明文，我卻把它列了待查。**
   二者之別應在 (ii) 能否說明，而 `064` 之 (ii) 我其實也沒說明。

3. `SWE-PM-038` / `063` 之 clause 確載 Timed 與 Timeout1 之關係，
   **惟其所述為「Timeout1 到期後進入 Timed」抑或「於 Timed 中計時」，
   二者於本條之推論力不同**，而我未逐字區辨。

---

## 四、B4 —— G137 口徑釐清（R-P219 / G149）

**為 (a) 口徑不同，非 (b) 退回或補寫未竟。**

| 口徑 | 定義 | 值 |
|---|---|---|
| **單項率** | 某一項之涵蓋 | 第 1 項 **33 / 33**、**第 2 項 33 / 33**、第 3 項 25 / 33 |
| **齊備率** | 第 1 ＋ 2 ＋ 3 **同時**成立 | **25 / 33** |

**27 包之 33 / 33 為第 2 項單項率**（本包複驗仍然）；**29 包之 25 / 33 為齊備率**。
已於閘門之 docstring 與輸出**明載二口徑並列**，G145 彙整表亦改為分列二列。

**未達齊備者 8 份**（`SWE-PM-073` / `015` / `016` / `017` / `021` / `022` / `024` / `032`），
**所缺全為第 3 項**。其「空語」判定係取段限制 ——
判定式取首個 `為什麼這樣切：` 段落（原有之「單一行為，不拆」，依 R-P203(c) 不得刪改），
而 27 包所補之實質依據位於其後且於 `**` 處截斷。
**內容非缺漏；放寬判定式方向對執行層有利，依 R-P187 未自行修改，
27 包已呈請裁定，至今未裁。**

---

## 五、B5 —— G146 台帳重複閘（R-P215）

| 台帳 | 檢查對象 | 相異數 | 重複 |
|---|---|---|---|
| `RULINGS.md` | 條號 | 214 → **220** | **0** |
| `ANOMALIES.md` | 列 | 155 → **159** | **0** |
| `DATA_REQUESTS.md` | 列 | **15** | **0** |
| `docs/INDEX.md` | 輪次 | 29 → **30** | **0** |

**fixture 五案如期**：現況通過；逐一刻意重複一列 → 四案皆 FAIL
（`R-P1` / `A-PW01` / `DR-PW1` / 輪次 `01` 各 2 次），
以 `tempfile` 複本為之，**未動真實台帳**。

**本包抄入六條、四列之後複跑 G146 仍為 0 重複** —— 即本閘於實際落檔後亦已驗過。

---

## 六、B6 —— 腳本產物重跑紀錄（R-P220）

**重跑時點 2026-08-18 16:20**，範圍 `data/*.md` 與 `*.tsv` 共 **54 檔**。

| 產物 | 比對 |
|---|---|
| **52 檔** | **逐位元組相同** —— 依 R-P220，證其係自現況資料所生，非早期快照 |
| `data/g136_pattern_variants.md` | **不同**（見下 1）|
| `data/g145_gate_triggers.md` | **不同**（見下 2）|

**二項陳舊皆為本條之直接成果**——若未重跑，二者將以陳舊內容被引用：

1. **G136 之判定表未隨新腳本擴充。** 其「未列入判定」桶之總括語
   「皆為建表 / 產生器類，不涉規格原文之樣式匹配」
   **對 `audit_precond_state.py` 已為假**（其確實比對 clause 原文）。
   已補判三檔 —— `audit_precond_state.py`（空白／大小寫**已涵蓋**）、
   `verify_ledger_dup.py`（比對本專案自身之編號格式）、
   `gate_trigger_report.py`（不比對規格原文，**惟與被擷取腳本之輸出格式耦合**）——
   判定表由 10 檔增為 **13 檔**，並於該桶加註「總括語須逐包複查」。

2. **G145 之 G137 比對式回歸係本包自身所致**（改 G137 口徑而未同步擷取式，
   致該列顯示「（未匹配）」）。已修，並改為分列齊備率與單項率二列，另補 G146 一列。

---

## 七、§D 全表自驗

| # | 項目 | 期望值 | 實測 | 判定 |
|---|---|---|---|---|
| G146 | 台帳重複偵測 | 四項皆無重複；刻意重複一列 → FAIL | 四項**重複 0**（落檔後複跑亦然）；**fixture 五案如期** | **PASS** |
| G147 | 20 項 (b) 型逐項表 | 20 項六欄齊備，置於上繳最前 | **20 項六欄**，置於 §一 | **PASS** |
| G148 | `091`/`092` 涵蓋缺口 | 判 (a) 或 (b) 並依裁定處置；無靜默消失者 | 判 **(b)**（八詞皆無）；**已開 DR-PW15** ＋ 二 leaf `reasoning` 登記 | **PASS** |
| G149 | G137 口徑 | 量測定義已載；未達者逐份列出並處置 | **(a) 口徑不同**；二口徑已明載並列；未達 8 份逐份列出，所缺全為第 3 項（取段限制，已呈請裁定）| **PASS** |
| G70 | lint 全閘 | 全 PASS | **264 TC，阻斷類 PASS，exit = 0**；self-test exit = 0 | **PASS** |

**無 MISMATCH。**

補驗：**G0 7 / 7**、**G94 103 / 103**、**G99 103 / 103**、**G103 103 / 103**、
**G108 7 / 7**、**G113 5 / 5**、**G121 PASS**、**G129 103 / 103**、
**G136 未涵蓋 0（判定 13 檔）**、**G142 (a) 244 / (b) 20**、**G38 連號 001–264**。

**Phase 4：103 leaf / 264 條**（本包無 TC 增刪）。

---

## 八、§F Anomaly 異動與 §G DATA_REQUESTS

**A-PW156 ~ A-PW159**（A-PW01 – A-PW159 連續無缺）：

| 號 | 摘要 |
|---|---|
| A-PW156 | 台帳重複檢查為臨時加驗（已實作 G146 常設閘門，fixture 五案）|
| A-PW157 | R-P211 之合規修正製造未登記之涵蓋缺口（判 (b)，已開 DR-PW15）|
| A-PW158 | G137 之 25/33 與 27 包之 33/33 並存（為口徑不同，已明載）|
| A-PW159 | **腳本產物陳舊二例，由 R-P220 之重跑比對當場揭出** |

**DR-PW15（Medium）新增**；DR-PW9 ~ DR-PW14 沿用。

---

## 九、裁決條文與台帳

**§A 六條逐字抄入 `RULINGS.md`**（逐條字串比對確認），各附執行層回報。
`RULINGS.md` 現為 **R-P1 – R-P220 連續無缺，且經 G146 驗無重複**。
§F 四項已入 `ANOMALIES.md`。

---

## 十、執行層自判：本包仍有該驗而未驗者

**有，四項。**

1. **R-P217 與 R-P218 之素材我備妥了，複核仍未發生。**
   20 項逐項表與 `SWE-PM-064` 之全部素材都在上繳裡，
   **但判斷仍是我自己的** —— §K 第 3 項自陳分析層對 29 包上繳本體未讀，
   本包之素材要求即為補此。**在複核回來之前，那 20 項與 `064` 都仍是未定的。**

2. **G136 之總括語為假一事，是重跑才發現的，不是設計時想到的。**
   我在 27 包寫下「皆為建表 / 產生器類」時，該語當時為真；
   29 包我自己新增了一個會比對 clause 原文的腳本，**卻沒有回頭改那句話**。
   R-P220 抓到了它 —— 但**同型問題在別處還有多少，我沒有查**。

3. **G145 之回歸是我本包自己造成的。**
   改 G137 輸出口徑時沒同步其擷取式，若非 R-P220 要求重跑，
   該欄會以「（未匹配）」的樣子留在彙整表裡而無人注意。
   **這說明彙整表與被彙整者之間的耦合本身是個未受監控的面。**

4. **T24 與 R-P159 之分層取樣仍未動**（§K 第 1、2 項）。
   §K 已明言「若 31 包仍不處置，須說明其何以持續推遲」——
   就執行層而言，本包之工作量並未排擠該二項，
   **它們未被處置的原因單純是下放包未要求**。
