# 下放包 10 —— pilot 審查：6 缺陷（全落於檢查清單漏列處）、R-DD11~R-DD13、DR-DD7、T16 修訂

- 日期：2026-08-28
- 方向：分析層 → 執行層 ＋ Pei（§七 二項）
- 前一包：`09_pilot_spec.md`；對應上繳：`07_pilot.md`
- 落檔註記：首寫於 MCP 逾時中失敗（get_file_info 驗 ENOENT），本檔為重寫，同稿
- **pilot 不退回重做**：4 TC 之結構、追溯、訊號、marker 皆正確；缺陷集中於欄位形制與 IN 條文之未檢面

---

## 一、分析層之誤（本輪最重要之一項）

**上繳包 07 自檢 13 項全綠，而本包列出 6 個缺陷。二者不衝突 ——
6 個缺陷有 5 個落在我寫的 §6.2 清單之外。**

| §6.2 所列 | 所涵 IN 條文 |
|---|---|
| 1–8 | R-S4、§10.7、profile §2／§3、§10.2、§8.4.2、§10.5、§6、§11（四欄）|
| **未列** | **§4.4（Pre-Condition 之禁）、§4.5（Input Test Data 歸屬）、§5.1（禁用動詞）、§5.2（步驟長度）、§12（Design Method 首合原則）、§11 之方括號於 `test_item`** |

**缺陷 D1／D2／D3／D5／D6 全部落在「未列」欄。** 執行層之自檢忠實執行了
我給的清單，清單沒問到的地方就沒被問到。

> **這不是執行層漏檢，是我漏寫。** §6.2 之八項是我從 profile 逐條抄下來的，
> **抄的是 profile 有的，沒抄 IN 有而 profile 沒重述的** ——
> 而 IN §9 之自檢十七項本來就該全跑。
> 拘束修正見 §八 T16b：**自檢一律對 IN §9 十七項全跑，
> 下放包之 §6.2 為「額外」而非「全部」。**

---

## 二、缺陷清單（D1–D6）

### D1｜Pre-Condition 含 IN §4.4 明文所禁之二類（4 TC 全中）

四則之 `pre_conditions` 第 1 行皆為：

```
1. The head unit is powered on and the Driver Distraction service is running
```

IN §4.4 **Forbidden** 逐字列有二：
- **系統預設**：`HU is powered on.` —— 本行前半即該例本身
- **feature under test as premise**：`Dealer Mode is accessible.` ——
  本行後半「Driver Distraction service is running」即以待測 feature 為前提

**修**：刪除該行。二者皆為測試員自然確保之環境，非 spec 觸發條件（§8.5）。

**併查**：PC3（`The Phone screen is displayed and …` /
`The menu-bar configuration view … can be opened`）為 step 可控之狀態，
依 §4.4 之 `step-controlled state` 應移入 Procedure 首步或刪除；
**T16 逐則覆核**。PC2（`$…$ is transmitted at 0`）為環境訊號源，**留**（§4.5-1）。

### D2｜Input Test Data 與 Procedure 重複同值（4 TC 全中）

`input_test_data` 書 `$STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (…)`，
而 `test_procedure` 步驟 1 又書 `Send the signal $…$ = 129 (8.0625 km/h)`。

IN §4.5 逐字：**「Do not duplicate the same value across Pre-Condition,
Input Test Data, and Procedure」**；且其 SWC 基準（R-1 v2 同批採認）逐字：
**「資料應內聯至 Pre-Condition 或 Procedure，使步驟自足；
Input Test Data 以 `NA` 為常態（SWC 0708 實測 285/286 為 `NA`）」**。

**修**：四則之 `input_test_data` 一律改 **`NA`**。
`[ASSUMPTION A-DD6]` marker 隨值移至其實際出現處
（`test_procedure` 與 `expected_result` 已各有一處，足）。

### D3｜`test_procedure` 用 IN §5.1 禁用動詞（1 處）

`newR1L-DD-001` 步驟 3：

```
3. Read the Phone screen and check whether the pairing flow has been entered
```

§5.1 **Forbidden verbs** 逐字含 `check whether`。

**修**：改 `Check that`＋具體可觀察標的，例：
`Read the Phone screen and check that the pairing flow has not started`。

**併查**：`-003` 步驟 3 `check the notification that is presented to the user`
非禁用詞但非 §5.1 之 preferred 形式；`-002`／`-004` 之末步僅 `read the screen`，
依 §5.5「Final Step 須含 ACTION ＋ check target」宜補 `and check that …`。
**T16 四則末步一律改為 `check that` 形式。**

### D4｜`design_method` 未依 §12 首合原則（1 處）

`newR1L-DD-001` 取 `情境 / 用例 (Scenario / Use Case Testing)`。

§12 為 **first-match** 表，其序為：Negative → Fault Injection →
**State Transition（State A → State B）** → Decision Table → …→ Scenario。
本則之觸發為車速由 0 跨越門檻，**即 A→B 狀態轉換**，於 Scenario 之前命中；
且 §12 tie-break 逐字「Scenario = ≥3 steps crossing features」——
本則為單一 feature 之存取嘗試，不合。

**修**：改 `狀態轉換 (State Transition Testing)`，與 `-003` 一致。
`-002`／`-004` 之 Fault Injection 正確（模擬故障，於 State Transition 之前命中）。

> 下拉選單之實值為權威（`基礎故障注入 (Fault Injection Lite)` 等），
> **選單值之選定仍受 §12 首合原則拘束** —— 二者不衝突。

### D5｜`test_item` 含方括號，而 IN §11 之例外未經 profile 啟用

四則之上半皆含 `Case [Normal]…` / `Case [Exception]…`（037 逐字）。

IN §11 逐字：方括號「**MUST NOT appear in TC output fields**」，
其 Exception 逐字為 **「profile-scoped … may retain the source's notation
when the feature profile says so」**。

**本 feature profile 未有該條款 → 例外未啟用 → 現況為違規。**

**修**：**不改 TC**（改即違 R-S4 逐字）。**改 profile** —— 見 §三 R-DD12。
自檢之 `方括號 無` 一項，其掃描範圍為「四欄」（標籤已誠實載明），
**惟 IN §11 之拘束及於全部輸出欄**；T16 之自檢須含 `test_item`
並以 R-DD12(c) 為 carve-out。

### D6｜ER 之冗餘與非觀察性語句（2 處，輕）

- `-001` ER1 末句 `the first representable step at or above the 5 MPH threshold`
  為**推導說明**，非可觀察結果。ER 應止於可觀察之事實
  （`raw 129, which is 8.0625 km/h`）；推導屬 `reasoning` 與 profile §3.1
- `-001` ER2 與 ER3 皆斷言 pairing 未啟動，**同一事實重複**。
  ER2 宜僅述步驟 2 之直接結果（存取嘗試已發出而未被接受），
  終局判定留 ER3（§5.5 Final Step owns validation）

---

## 三、裁決條文（R-DD11／R-DD12／R-DD13；出處註在圍籬內）

```
R-DD11（引號內字串之終端標點）

IN §11 之「無行尾句號」，其規制對象為**作者所書句子之句末標點**。
逐字引用之 UI 字串，其自身之終端標點屬該字串之一部分，**保留**。

例（合規）：
  The Standard Lockout Popup is displayed, showing
  "Feature not available while the vehicle is in motion."
  —— 句點在引號內，屬 HMI spec p4 之原字串；item 之末字元為 `"`，非 `.`

例（違規）：
  … showing "Feature not available while the vehicle is in motion.".
  —— 引號外另加句點，該句點為作者所書

判準：**移除引號後，該 item 是否以作者之句點結尾**。是即違規。
（Pei 下放，分析層即裁，下放包 10 §三）
```

```
R-DD12（IN §11 方括號例外之啟用；profile-scoped）

依 IN §11 之 Exception，本 feature 啟用之：

(a) `test_item` **上半**（需求原句 verbatim）中，源自 037 之方括號記法
    （`Case [Normal]`／`Case [Exception]`／`$VC_Trans_Equipped$ = [Manual]` 等）
    **保留原樣**，不得改寫為雙引號 —— 改之即違 R-S4 之逐字。
(b) 例外**僅及於上半**。`test_item` 之括號下半（作者所書之測試目的）、
    以及 `pre_conditions`／`input_test_data`／`test_procedure`／
    `expected_result` 四欄，**一律依 IN §11 用 `"..."`，不得出現方括號**。
    唯一例外為裁決所命之 `[ASSUMPTION A-DDn]` marker（標記，非 UI 標籤）。
(c) lint／自檢對 `test_item` 之方括號，須以「該 token 是否為所引來源列
    之逐字」為判準（比對 037 原文），非一律禁。
（Pei 下放，分析層即裁，下放包 10 §三）
```

```
R-DD13（訊號一格載多名時之取捨）

LID 之單一儲存格載多個訊號名者（如 `LID CAN Mapping r1738 [Atlantis High 欄]`
同時載 STATUS_CCAN3.VehicleSpeedVSOSig 與 BRAKE_FD_2.VehicleSpeedVSOSig）：

(a) 先以「該名存在於綁定 DBC」為篩。篩後唯一者即取之。
(b) 篩後仍多於一者，取**同時見於 `Atlantis` 與 `Atlantis High` 二欄者**
    —— 其不因架構欄之取捨而變，施加路徑最穩定。
    實例：STATUS_CCAN3.VehicleSpeedVSOSig 見於 P 欄與 Z 欄二者；
    BRAKE_FD_2.VehicleSpeedVSOSig 僅見於 Z 欄。故取前者。
(c) (b) 仍無法區別者，登 DR，不逕選。
(d) 未取之名於 profile §3 記為**備援**並註其匯流排，不得逕自替換；
    台架若無主路徑之匯流排，須先報再換。
（Pei 下放，分析層即裁，下放包 10 §三）
```

> R-DD13(b) 之理由為**穩定性**（不受 R-DD6 v2(b) 取捨影響），
> 非「哪個看起來對」。

---

## 四、A-DD7 → 立 DR-DD7

執行層之處置（依 037 原文斷言存取阻擋，不代上游改寫為通知面）**正確**。
分析層補一項其未言之後果：

**`-010` 與 `-012` 之 037 原文 18/20 欄全等 → 其衍生之 TC，
其區別僅在於「取樣 feature」，而取樣 feature 是作者所選，非 spec 所定。**
即：**二 TC 之驗證目標實質相同**，僅追溯 ID 不同。
依 IN §4.6 之等價判準（same trigger + outcome + input + verification target），
**四者皆同** —— 若非追溯需求，其為重複。

**處置**：二 TC **皆保留**（追溯要求每 leaf 有 TC），
但於 `reasoning` 明記「本列與 newR1L-DD-002 之驗證目標實質相同，
區別僅在取樣 feature 與追溯 ID；成因見 A-DD7／DR-DD7」。
**不得以取樣 feature 之不同偽稱為不同之驗證目標。**

### DR-DD7 文稿（執行層建檔，DRAFTED；Pei 發送）

> **DR-DD7 — Identical AC2 text for `SWE1-RA-Driver_Distraction-010` and `-012`**
>
> In FM-WI-FSM-037-A03, rows `-010` and `-012` are byte-identical across 18
> of 20 columns; they differ only in the leaf id and the Source Requirement
> ID. `-010` traces to `SYS-RA-Driver_Distraction-117`, whose normal-case
> outcome is `HMI prevents access to the feature`; `-012` traces to `-118`,
> whose normal-case outcome is `HMI displays the driver-distraction lockout
> notification`.
>
> The AC1 pair derived from the same two sources (`-009` and `-011`) does
> differ in Requirement Description and Verification Criteria, each following
> its own source. The AC2 pair does not: both state
> `HMI keeps the corresponding feature locked`, which is the `-117` outcome.
>
> Question: for `-012`, should the AC2 outcome be the notification behaviour
> of `-118` (i.e. the lockout notification is presented when a required
> signal is unavailable), or is the access-blocking wording intended as
> written? As it stands, the two rows yield test cases with the same
> verification target, distinguished only by traceability.

---

## 五、通過之項（不修）

| 項 | 判 |
|---|---|
| 上半 verbatim ＋ 摘句規則（`Case..Then` 二行為 `-009`／`-011` 之相異處；`When`／`And` 逐字全等，取之無分辨力）| **正確且有據** |
| 括號下半之 sibling 分辨 | 無重複，合 R-S4 |
| spec_reference（4915108×2／4915109×2，一行一 ID）| 合 profile §1 |
| 四禁詞 0 命中；觀察面 A 具名、B 逐字 | 合 profile §2 |
| raw 129 ＋ `[ASSUMPTION A-DD6]` 集合一致 | 合 R-DD7(f) |
| §8.4.2 界線 10 禁詞 0 命中 | 合 |
| fail-safe 取逾時而非 SNA —— **回頭查 037 原文（書停送＋After the signal timeout）而得** | **正確，且方法正確** |
| 黃標以 PDF 填色實測定位，±2 容差收緊 | **正確**。2 pt 之差目視不可分 |
| `-002` ER 具名之自修（自檢比規則嚴而抓到） | **正確** |

---

## 六、T14a 之處分 —— 停為正確

三個理由皆成立且互相獨立（產物非簿／本檔無錨點／全域形態）。
**手工追加會在下次重跑被抹除且使 `--check` 必 FAIL** —— 停是對的。

**修法之判斷（分析層意見，待 Pei）**：於各條文圍籬**之上**加標題錨點
（`## R-DDn`），**屬新增行，非對條文本體之刪改** —— 工具之本體定義
自錨點之次行起算，圍籬與其內容原字不動，故**不違 R-TM13**。
惟該改及於 5 個 feature、148 條，**屬全域政策，本線不裁**（§七-1）。

`--check` 現行 FAIL 之 13 行差異全為 popup 線之 `R-POP18~20`，
**與本線無涉**；本輪未動該檔為正確。

---

## 七、待 Pei（二項）

1. **`RULINGS.md` 是否改標題錨點體例** —— 影響 display 59／sw_update 31／
   vehicle_category 30／bed_lowering 17／driver_distraction 11，合計 148 條
   之 sha 台帳可見性。分析層意見見 §六
2. **`RULINGS.sha.tsv` 由誰重生** —— 現行 `--check` FAIL 源於 popup 線

---

## 八、任務（T16）

| # | 任務 |
|---|---|
| T16a | 依 §二 D1–D4／D6 修訂 4 TC（D5 不改 TC，改 profile —— 分析層自辦）；每處修訂於上繳包標明所依 IN 條文 |
| T16b | **自檢擴充**：對 **IN §9 十七項全跑**，下放包所列為額外項而非全部。新增至少涵蓋 §4.4／§4.5／§5.1／§5.2／§5.5／§12／§11（含 `test_item`，以 R-DD12(c) 為 carve-out） |
| T16c | `reasoning` 依 §四 補記 `newR1L-DD-004` 與 `newR1L-DD-002` 之實質同一 |
| T-抄 | R-DD11／R-DD12／R-DD13 逐字入 `RULINGS.md`（現行 13 條、留存 1）|
| T-登 | DR-DD7 建檔（§四 文稿逐字，DRAFTED）；A-DD7 條目連結 DR-DD7 |

**不在本輪**：寫回工作簿、git、`-013` 以後之 leaf、`RULINGS.md` 體例變更。

## 九、上繳包要求（`docs/upstream/08_pilot_rev.md`）

修訂後 4 TC 全文、T16b 之十七項自檢輸出、T-抄核對、T-登結果、
未結 DR 清單（DD1–DD7）、獨立自評、R-G8 揭露。
