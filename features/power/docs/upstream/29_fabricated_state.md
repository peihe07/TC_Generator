# 上繳包 29 —— 造值判準補洞與 Day_Night_Mode 裁定

> 對應下放包：`features/power/docs/handoff/29_fabricated_state.md`
> 執行層：Claude（TC_Generator）
>
> **§J 自檢二次皆一致（R-P200(c)）**：開工時與抄錄條文前皆為
> §A block **5** / §J 列數 **5** / §H 步驟 9「**五條**」；
> 檔案 **11066 bytes、mtime 08-18 15:40:02 均未變**。
>
> 本包**未執行任何 git 子命令**；**未對 workbook 呼叫 `save()`**；
> **未觸碰客戶樹與 `inputs/`**；**寫回仍未開放**；
> **未以「已通過 R-P204」為由結案任何 (b) 型狀態**；
> **未以「為驗證需要」為由保留無依據之注入**；
> **未以首次適用之結果作為自訂判準正確之證據**（見 R-P214 之回報）。

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**

**編號查核（R-P147，先查後開）**：
**R-P 最大 209（1–209 連續）、A-PW 最大 151、DR-PW 最大 13、閘門最大 G141。**
本包新號：**R-P210–R-P214**、**A-PW152–A-PW155**、**G142–G145**、
**DR-PW14**（依 §G 之明示，R-P210(b) 產生無法說明之狀態選擇時開）。

---

## 一、B1 —— 全批 `pre_conditions` 依 R-P210 重掃（G142）**最高優先**

腳本 `scripts/audit_precond_state.py`（判準先寫定後執行）；
產物 `data/g142_precond_state.md`。

### 1.1 計數

| 類 | 數 | 佔比 |
|---|---|---|
| (a) 狀態值逐字見於 clause | **244** | 92.4% |
| **(b) 有狀態值未見於 clause** | **20**（11 leaf）| **7.6%** |
| **合計** | **264** | 100% |

**20 條先經逐項查證非抽取殘段** —— 其未命中之值於各該 clause 中
**連較長詞形亦不存在**（例：`Full` 於 `SWE-PM-057` 之 clause 無任何 `Full*` 詞）。
**執行層未修改抽取式**：其方向（減少 (b) 數）對執行層有利，依 R-P187 不自為之。

### 1.2 (b) 型逐條處置（每 leaf 皆載 (i)(ii)）

| leaf | 條 | 未見之值 | (i) 選擇依據 | (ii) 行為隨狀態而異？|
|---|---|---|---|---|
| `SWE-PM-057` / `060` / `062` | 8 | `Full-Operation` | **規格他處明文** —— `SWE-PM-061` 之 clause 逐字載「These settings could be only done in TLM Full-Operation Status」| 是；否定側由 `SWE-PM-061` 之 `024` 承擔（§8.2.1），本 leaf 不另立 |
| `SWE-PM-061` | 1 | `Timed` | 否定側需一非 Full-Operation 狀態；`Timed` 為 §E 既有狀態 | 是，而本條所驗即該差異；規格僅二分，取任一即足 |
| `SWE-PM-064` | 1 | `Timed` | **他 leaf 之定義** —— `Timeout1` 之計時與到期依 `SWE-PM-038` / `063` 發生於 Timed | **規格未載**；依據為他 leaf 明文而非推定，故不列待查（**見 §七第 2 項之自判**）|
| `SWE-PM-019` | 2 | `False` | clause 之 ELSE 分支即該條件不成立；布林訊號之唯一否定值 | 是，二分支皆已成條 |
| `SWE-PM-027` / `028` / `029` | 6 | `True` | clause 之「set … **back to** `False`」蘊含起始為 `True` | 是 —— 起始若已為 `False` 則無可觀察變化，該前提為必要 |
| `SWE-PM-031` | 1 | `Standby` | 測試可執行性需一具體狀態 | **否** —— clause 逐字載 `regardless of TLM_Status.Info and $Telematic_Power$ value`。**本批依據最強者** |
| **`SWE-PM-094`** | **1** | `STANDBY MODE` | 他 leaf 明文（`SWE-PM-093` 列三模式，此為其一）| **無法說明** |

### 1.3 `SWE-PM-094` —— 唯一無法完整說明者

其 clause 逐字為
`The HU shall display the startup animation separately from the Splash screen and disclaimer screen.`
—— **完全未提任何模式**。

- (i) **可說明**：`STANDBY MODE` 見於 `SWE-PM-093` 之 clause 所列三模式之一
- (ii) **無法說明**：「分開呈現」之關係是否隨起始模式而異，**clause 一字未載，
  執行層亦無查證來源**；若其隨模式而異，另二模式（`SLEEP` / `PARTIAL OPERATION`）未被涵蓋

**已依 R-P210 標為待查並開 DR-PW14，未以「已通過 R-P204」結案。**

---

## 二、B2 —— `$Day_Night_Mode$` 二項（R-P211 / G143）

### 2.1 clause 逐字

| leaf | clause |
|---|---|
| `SWE-PM-091` | `If the "Theme Mode" setting is set to "Day" the HU shall use the Day theme` |
| `SWE-PM-092` | `If the "Theme Mode" setting is set to "Night" the HU shall use the Night theme` |

二者**皆未載任何覆蓋機制**（無 `regardless` / `override` / `irrespective` 一類措詞），
**亦未提 `$Day_Night_Mode$`**。

對照：`SWE-PM-090` 之 clause **確載** `the HU shall use the $Day_Night_Mode$ to
determine which of the themes to show` —— 該訊號屬**該** leaf，非本二 leaf。

### 2.2 判定與處置 —— **(b) 真陽性**

**注入已移除**：`input_test_data` 改為 `NA`；
`test_item` 由「keeps the Day theme **regardless of the day night signal**」
改為「uses the Day theme」；ER 之「HU accepts the signal value」隨之移除。
二 leaf 之 `reasoning` 依 R-P191 同步。

**全批 G82 擴充欄之觸發：2 → 0。**

**執行層之自我檢討**：該注入為末批撰寫時所加，其動機為「證明設定會覆蓋訊號」——
**該命題本身不在 clause 內，是我加上去的**。R-P211 之裁定正確。

---

## 三、B3 —— R-P204 加註（G144）

| | SHA256 | bytes |
|---|---|---|
| 加註前 | `75254188c67f8d59c4f6606cde25ea498978c88cf10eac63197743d844c3bf62` | 1591 |
| 加註後 | **相同** | 1591 |

**G144 = UNCHANGED。**

---

## 四、B4 —— 閘門觸發數回報（R-P212 / G145）

新增 `scripts/gate_trigger_report.py`，產物 `data/g145_gate_triggers.md`。
**實作方式：自動彙整**（數字直接取自各閘門腳本之執行結果），**非人工填表** ——
避免抄錄誤差，亦使該紀錄與實測不會脫節。

### 本包之批次層閘門觸發數（含 0）—— 即 28 包回查所缺者

| rule | 閘 | 觸發 |
|---|---|---|
| `R-P104` | G79 | **0** |
| `R-P107` | G81 | **0** |
| `R-P109` | G82（`expected_result`）| **0** |
| `R-P109(擴充)` | G82（`pre_conditions` / `input_test_data`）| **0** |

**lint 總計：阻斷類 0、待人工裁決類 275。**
其餘各閘之實測值同載於該表（G0 / G94 / G99 / G103 / G108 / G113 / G121 /
G129 / G136 / G137 / G142）。

---

## 五、B5 —— 白名單命中統計（R-P213）

| 項 | 數 |
|---|---|
| **命中白名單而排除**（測試選用量）| **9** |
| **未命中而觸發** | **0** |

九項即 28 包所判之九個純數值（`SWE-PM-072` 之 `20` / `100`、
`SWE-PM-073` 之 `25` ×3 / `15` ×2）。

**(a) 完備性未經驗證** —— 未命中數為 0 **不足以證明白名單完備**：
未命中者會觸發並入待裁類（可補救），故其為零僅表示本批無此情形。

**(b) 反向風險仍未量得，據實標明** ——
「某規格閾值所在行恰不含規格參數跡象而被誤排除」之發生率，
**本統計無法直接量測**：其需先知道每個被排除之數值是否實為規格閾值，
而該判斷正是白名單所要取代者。**未以命中數充作其代理。**
現行唯一防線為「同行有規格參數跡象一律覆蓋排除」（G139 第四案 fixture 所驗）。

---

## 六、§D 全表自驗

| # | 項目 | 期望值 | 實測 | 判定 |
|---|---|---|---|---|
| G142 | `pre_conditions` 之 (a)/(b) 分類 | 264 條全掃；(b) 型逐條具處置；無以「已通過 R-P204」結案者 | **264 全掃**；(a) 244 / (b) 20；**20 條逐條載 (i)(ii)**；`SWE-PM-094` 標待查並開 DR-PW14 | **PASS** |
| G143 | `$Day_Night_Mode$` 裁定 | 【實測填入】clause 屬 (a) 或 (b)；處置結果 | 二者皆 **(b)**（clause 無覆蓋機制、未提該訊號）；**注入已移除**，擴充欄觸發 2 → 0 | **已填** |
| G144 | R-P204 加註後原文位元組未變 | UNCHANGED | `75254188…`，1591 bytes，前後相同 | **UNCHANGED** |
| G145 | 閘門觸發數回報 | 各閘之觸發數皆已載明，含 0 | **自動彙整**；批次層四項皆 **0**；lint 阻斷 0 / 待裁 275 | **PASS** |
| G70 | lint 全閘 | 全 PASS | **264 TC，阻斷類 PASS，exit = 0**；self-test exit = 0 | **PASS** |

**無 MISMATCH。**

補驗：**G0 7 / 7**、**G94 103 / 103**、**G99 103 / 103**、**G103 103 / 103**、
**G108 7 / 7**、**G113 5 / 5**、**G121 PASS**、**G129 103 / 103**、
**G136 未涵蓋 0**、**G137 25 / 33**、**G38 連號 001–264**。

**Phase 4：103 leaf / 264 條**（本包無新增或刪除 TC —— `091` / `092` 為改寫）。

---

## 七、§F Anomaly 異動與 §G DATA_REQUESTS

**A-PW152 ~ A-PW155**（A-PW01 – A-PW155 連續無缺）：

| 號 | 摘要 |
|---|---|
| A-PW152 | R-P204 未涵蓋 §8.4.1 之造值（已由 R-P210 補；重掃 (a) 244 / (b) 20）|
| A-PW153 | `$Day_Night_Mode$` 為執行層注入而 clause 未載（注入已移除）|
| A-PW154 | 上繳未載閘門觸發紀錄（已實作 G145 自動彙整）|
| A-PW155 | 白名單之反向風險未量測（據實標明，未以命中數充作代理）|

**DR-PW14（Medium）新增** —— `SWE-PM-094` 之「分開呈現」是否隨起始模式而異。
DR-PW9 ~ DR-PW13 沿用。

---

## 八、裁決條文與台帳

**§A 五條逐字抄入 `RULINGS.md`**（逐條字串比對確認），各附執行層回報。
`RULINGS.md` 現為 **R-P1 – R-P214 連續無缺**。
R-P204 已加註且原文位元組未變。§F 四項已入 `ANOMALIES.md`。

---

## 九、執行層自判：本包仍有該驗而未驗者

**有，四項。**

1. **R-P210 之結果同受 R-P214 拘束，本包無第二方。**
   (a) 244 / (b) 20 只表示「依此判準，264 條中有 20 條需說明」——
   **不表示該判準的寬嚴是對的**。§K 第 1 項已預先點明，我照實回報，
   但**能複核它的仍然只有分析層**。

2. **本包最可能被推翻者是 `SWE-PM-064` 之 `Timed`。**
   它的 (ii) 我自陳「規格未載」，卻仍判其不列待查，
   理由是「依據為他 leaf 明文而非推定」——
   **而 `SWE-PM-094` 的 (i) 同樣是他 leaf 明文，我卻把它列了待查。**
   二者之別在 (ii) 能否說明，而 `064` 的 (ii) 我其實也沒說明，
   只是說了「依據不是推定」。**這條線我畫得不穩，請優先複核。**

3. **`SWE-PM-091` / `092` 改寫後，「設定是否真能覆蓋訊號」變成無人驗證。**
   移除注入是對的 —— 那個命題不在 clause 裡。
   但它**在現實中仍可能是個真問題**（Theme Mode 設為 Day 而訊號指向 night 時會怎樣），
   而現在沒有任何 TC 碰它，也沒有 DR 問它。
   **依 §I 我不能保留無依據之注入，但我可以指出這個洞。**

4. **T24 與 R-P159 之分層取樣仍未動。**
   §K 第 2 項已將 T24 排至 30 包；分層取樣則已積欠九包。
   本包又改了 20 個 leaf 的 `reasoning` 與 2 條 TC，**改動仍大於覆核**。
