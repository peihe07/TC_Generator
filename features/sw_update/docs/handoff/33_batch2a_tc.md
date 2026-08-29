# 下放包 33 —— 探針結果：第四型（觸發面）、R-SU37 v2、R-SU38、batch 2a 六 TC

- 日期：2026-08-29
- 方向：分析層 → 執行層
- 前一包：`32_batch2_probe.md`；對應上繳：`docs/upstream/30_batch2a_review.md`
- 裁定狀態：R-SU37 v2、R-SU38、R-SU39（第四型）、`313` 之處置 —— 分析層即裁
- **探針之答案：錯誤碼解不了 105 列，而擋住的不是觀測面，是觸發面**

---

## 一、上繳包 29 審查判定

**收。§9 之作答是本輪最重要之一節 —— 它自己找到了一個答案，然後自己拆掉。**

### 1.1 §9 —— `313` 之判別問句作答

執行層找到「多個中斷條件併發時處理錯亂」作為 `313` 之獨有失敗情形，
**隨即以二個理由拆掉它**：

1. **它不在 `313` 之 Description 裡** —— 併發是自「協調」一詞**推想**而來，
   **推想不是需求**（§8.4.1）。據此寫 TC 即為驗一個沒人寫過的需求。
2. **併發另有其列**（`321`–`329` 之範圍）。若併發已有專屬列，
   則該情形是**那一列**之驗證點。

**二個理由皆成立，第二個是決定性的。裁定：`313` 餘量為空，適用 R-SU37(b)。**

### 1.2 §9(己) 之回饋 —— **採納，R-SU37 v2**

> (c) 之判別問句很有效，**但它會把「我想得到的失敗情形」誤認為
> 「需求所要求的驗證點」**。

**正確，且此為該問句之結構性風險** —— 問「還有什麼情形能使它失敗」
是在問**想像力**，而 TC 之依據是**需求文字**。§三 v2 補其拘束。

### 1.3 §3.2／§3.4 —— `I-cross` 之跨簿限制

併入 lint 補上「跨 req_id」一維，**未補「跨簿」一維**；
且**分得越細，漏得越多** —— batch 2a 起草後，其 6 列與既有 10 列之配對
在逐簿執行下**一組都比不到**。

執行層指出交付簿為一本、故交付時本限制不存在 —— **正確，但不足以放心**：
**開發期漏掉的配對，交付時才發現，其修改成本在最貴的時點。**
**裁定取 (乙)**，見 §五 T46b。

### 1.4 §4.1-3 —— 候選錯誤碼之產出極不均勻，且其成因已指認

`318`（Emergency State）之候選幾乎全落空，成因為
**碼側用 `abort`／`suspend`，需求側用 `emergency`** ——
詞彙法之漏。**「無候選」不等於「無對應碼」**，此限定須隨表陳述。

---

## 二、探針之答案 —— 錯誤碼解不了 105 列，且擋住的不是觀測面

**分析層讀畢六列材料後之判定**：

| 037 列 | 105？ | **觀測面** | **觸發面** | 可寫？ |
|---|:--:|---|---|:--:|
| `315` Socket 讀寫錯誤 | ⚠ | 有（更新未完成） | **無** —— 需 socket 層之錯誤注入 | ✗ |
| `316` 網路遺失 | ⚠ | 有 | **有** —— 關閉 AP／拔網路 | **✓** |
| `317` 使用者關閉網路 | — | 有 | **有** —— 使用者操作（本即其定義） | **✓** |
| `318` 車輛緊急狀態 | ⚠ | 有 | **無** —— 需事故偵測訊號，本 feature 未綁 DBC | ✗ |
| `319` 電源遺失 | ⚠ | 有 | **有** —— 斷電為物理動作 | **✓** |
| `320` 主機實體斷開 | — | 有 | **有** —— 物理動作 | **✓** |

### 2.1 三項結論

**(一) 錯誤碼對本組之貢獻幾近於零。**
六列所驗者為「偵測並處理中斷條件」，其觀測面為
**「更新未完成且系統未損毀」**，不需錯誤碼即可觀測（版本號未變、HU 可操作）。
R-SU35 之錯誤碼對**安裝階段之失敗**有用，對**中斷條件之偵測**幾乎無用。

**(二) 105 列之分類與可寫性再度正交。**
可寫之四列中有三列（`316`／`319`）屬 105；不可寫之二列中有一列（`317`）不屬。
**R-SU32 v2(e) 之正交性於本批再獲一次獨立佐證。**

**(三) 擋住的是觸發面，不是觀測面 —— 此為新的一型。**
`315`／`318` 之外部後果可觀測，**但測試者無法使該條件發生**。
R-SU25 全篇問的是「看哪裡」，**從未問「怎麼讓它發生」**。§三 R-SU39 立條。

---

## 三、裁決條文（抄入 RULINGS.md，逐字）

```
R-SU37 v2（統攝型需求之驗證點 —— 餘量判準之依據拘束）

v1(a)(b)(d)(e) 維持。(c) 補拘束。

(c) v2 —— 判別問句
    **「若所統攝各列各自都通過，還有什麼情形能使統攝列失敗？」**
    仍為判準，**惟其答案須通過依據檢定**：

    **該情形必須在統攝列自身之 Description 中有文字依據。
    推想出來的失敗情形不算。**

    理由（上繳包 29 §9(己)）：該問句問的是**想像力**，
    而 TC 之依據是**需求文字**。不加此拘束，一個想得到的失敗情形
    會被誤認為需求所要求之驗證點，據以寫出之 TC
    **驗的是一個沒人寫過的需求**（§8.4.1）。

    **檢定之二問**（二者皆須通過）：
    1. 該情形之要素，是否逐一見於統攝列之 Description？
    2. 該情形是否已由本 Test Set 之其他列所擁有？
       —— 若是，其為那一列之驗證點，不是統攝列的。

    實例（`313`）：「多個中斷條件併發時處理錯亂」——
    問 1 否（`313` 只說協調六條件之處理，未提併發）、
    問 2 是（併發屬本組其他列）。**故餘量為空。**
```

```
R-SU38（併入列之追溯記法）

R-SU37(b)／R-SU32(d) 之「驗證併入他列」一旦經上游確認，
該列於工作簿即**無屬於自己之 TC**，而 SWE.6 之追溯性
要求每一需求列有其覆蓋。

**其解不是替它寫一個 TC**（那正是被判為無驗證點者），
**而是記其併入之去向**。

裁定：

(a) 建 `features/{slug}/TRACE_MERGE.md`：欄為
    **被併列 id｜併入之列 id（可多）｜依據之裁決｜上游確認之狀態**。
(b) 該列於工作簿**不出現**；其覆蓋由被併入各列之 TC 承擔。
(c) **交付時須附本台帳** —— 其為追溯矩陣之補件。
(d) **上游未確認前，被併列不得自工作簿缺席** ——
    其狀態為 `PENDING`（掛於該列之 TC），不是「已併入」。
    **「分析層認為可併」與「上游確認可併」是兩件事。**
(e) 交付面之接受與否（追溯矩陣是否認可本記法）**屬 Tier 3**，
    提 Pei 裁；未裁前依 (d) 掛 `PENDING`。
```

```
R-SU39（第四型 —— 觸發手段不可得）

實測（下放包 33 §二）：`SWE1-FOTA-315`（socket 讀寫錯誤）與
`318`（車輛緊急狀態）之**外部後果可觀測**（更新未完成、系統未損毀），
**而測試者無法使該條件發生** —— 前者需 socket 層之錯誤注入，
後者需事故偵測訊號而本 feature 未綁 DBC。

R-SU25 全篇問「台架上的人要看哪裡」，**從未問「怎麼讓它發生」**。

裁定：

(a) **第四型：觸發手段不可得。** 其與第二型（無觀測手段）、
    第三型（不可區辨）並列，**成因與解方皆不同**。

(b) **判別**：TC 之 Procedure 中，凡須使某條件成立之步驟，
    其手段須為測試者可執行者：**UI 操作、物理動作
    （斷電、拔線、關閉 AP）、可送之訊號、可置放之檔案**。
    皆不可得者為第四型。

(c) **處置**：該步驟掛 `PENDING`，DR 之請求為**觸發手段**
    （注入工具、模擬訊號、測試模式），**不是觀測手段**。
    DR-SU2 增第四型之段。

(d) **與第二型之別**：第二型是「發生了但看不到」，
    第四型是「看得到但弄不出來」。**二者可同時存在，須分別記。**

(e) **本型不可由語形判定** —— 其取決於台架之能力，
    而台架能力不在任何來源文件中。故**無母群可估**，
    只能隨批次逐列發現。
```

---

## 四、`313` 之處置與 batch 2a 之六 TC

### 4.1 `313` —— 適用 R-SU37(b)，掛 `PENDING`，入 DR-SU3

**新開 DR-SU3**（其請求對象與 DR-SU2 不同 —— 不是觀測或觸發手段，
是**需求單元之合併確認**）：

| 欄 | 值 |
|---|---|
| 事項 | 統攝型需求之驗證併入確認 |
| 對象 | `SWE1-FOTA-313`（統攝 `315`–`320`）、`SWE1-FOTA-327`（統攝 `328`／`329`） |
| 理由 | 二列之 Description 所述行為，逐句拆解後全部由其所統攝各列承擔；其餘量（協調行為本身）於其自身 Description 中無文字依據可支撐獨立之驗證點（R-SU37 v2(c)） |
| 請求 | 確認該二列之驗證得併入其所統攝各列；若否，請指出其獨有之驗證點 |
| Urgency | Medium（不阻斷其餘各列） |

### 4.2 六 TC 之共通欄（以下各 TC 不重列）

**input_test_data**：`NA`（全部六列）
**design_method**：`故障注入 (Fault Injection)`（全部六列 —— 皆為模擬故障）
**priority**：`P1`（037 Priority 皆 High，且中斷處理涉資料完整性）

**共通 pre_conditions 前二行**：
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package with update type Silent Update is staged on the OTA Server for this head unit
```

**驗證面之共通形態（範圍紀律，IN §8.2.1）**：
本六列所擁有者為**「偵測並處理該中斷條件」**；
**中斷解除後之復原**為 `321` 所擁有（`4907673`），**本批不涵蓋**。
故其 ER 之終點為「更新未完成且系統未損毀」，**不寫「恢復後續行」**。

---

### TC-11 ← `SWE1-FOTA-315`（`newR1L-SU-011`）—— **第四型，掛 `PENDING`**

**test_item**
```
The SWMC shall detect and handle socket read/write errors during OTA server communication, flashing, or software component update, and shall report the error status to WiFiUpdateService.
(Socket read or write error during an update session)
```
**pre_conditions**：共通二行 +
```
3. PENDING: DR-SU2 means of injecting a socket read or write error during OTA server communication
```
**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. PENDING: DR-SU2 step to inject a socket read or write error during the update session
4. Read the software version shown on the head unit and record it as Version_after
5. Check that Version_after equals Version_initial and that the head unit remains operable
```
**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. PENDING: DR-SU2 observable evidence that the socket error has occurred
4. Version_after is recorded
5. Version_after equals Version_initial; the head unit remains operable and its screen responds to user input
```
**specification_reference**：`CFTS057-4907667`

> **第四型之記明**（R-SU39）：本列之觀測面**有**（版本未變、HU 可操作），
> 缺者為**觸發手段**。DR 之請求為 socket 層之錯誤注入工具，**非觀測手段**。

---

### TC-12 ← `SWE1-FOTA-316`（`newR1L-SU-012`）—— **可寫**

**test_item**
```
The SWMC shall detect network loss conditions, including network errors, no data coverage, loss of Wi-Fi connection, phone tether disconnection, and embedded modem roaming, during OTA server communication, flashing, or software component update, and shall report the network loss status to WiFiUpdateService.
(Wi-Fi access point switched off during an update session)
```
**pre_conditions**：共通二行
**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Switch off the Wi-Fi access point while the update session is in progress
4. Read the software version shown on the head unit and record it as Version_after
5. Check that Version_after equals Version_initial and that the head unit remains operable
```
**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. The Wi-Fi access point is switched off and the head unit shows no Wi-Fi connection
4. Version_after is recorded
5. Version_after equals Version_initial; the head unit remains operable and its screen responds to user input
```
**specification_reference**：`CFTS057-4907668`

> **sibling 區分（vs TC-13）**：本列之觸發為**網路側**之中斷（AP 關閉），
> TC-13 為**使用者側**之關閉。二者之觸發動作不同，判決可相異
> （AP 關閉時使用者設定仍為開啟）。

---

### TC-13 ← `SWE1-FOTA-317`（`newR1L-SU-013`）—— **可寫**

**test_item**
```
The WiFiUpdateService shall handle user-initiated deactivation of mobile data usage or an active Wi-Fi connection reported by SWMC during OTA server communication, flashing, or software component update.
(User switches off the Wi-Fi connection during an update session)
```
**pre_conditions**：共通二行
**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Switch off the Wi-Fi connection in the head unit settings while the update session is in progress
4. Read the software version shown on the head unit and record it as Version_after
5. Check that Version_after equals Version_initial and that the head unit remains operable
```
**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. The Wi-Fi connection is switched off and the head unit settings show Wi-Fi as disabled
4. Version_after is recorded
5. Version_after equals Version_initial; the head unit remains operable and its screen responds to user input
```
**specification_reference**：`CFTS057-4907669`

---

### TC-14 ← `SWE1-FOTA-318`（`newR1L-SU-014`）—— **第四型，掛 `PENDING`**

**test_item**
```
The WiFiUpdateService shall handle the vehicle emergency state (accident detection) notified by the appropriate system component during OTA server communication, flashing, or software component update.
(Vehicle enters emergency state during an update session)
```
**pre_conditions**：共通二行 +
```
3. PENDING: DR-SU2 means of placing the vehicle into the emergency state (accident detection) on the test bench
```
**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. PENDING: DR-SU2 step to place the vehicle into the emergency state while the update session is in progress
4. Read the software version shown on the head unit and record it as Version_after
5. Check that Version_after equals Version_initial and that the head unit remains operable
```
**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. PENDING: DR-SU2 observable evidence that the vehicle is in the emergency state
4. Version_after is recorded
5. Version_after equals Version_initial; the head unit remains operable and its screen responds to user input
```
**specification_reference**：`CFTS057-4907670`

> **第四型**（R-SU39）。⚠ **不得以「模擬碰撞訊號」充數** ——
> 本 feature 未綁 DBC，訊號名與值域皆無來源，寫之即造值（§8.4.1）。

---

### TC-15 ← `SWE1-FOTA-319`（`newR1L-SU-015`）—— **可寫**

**test_item**
```
The WiFiUpdateService shall coordinate the handling of condition during OTA server communication, flashing, or software component update by interacting with SWMC and the appropriate installer component.
(Power loss during an update session)
```
> **verbatim 保留 D-1 之缺字**（`the handling of condition` —— 條件名脫落）。
> 其括號下半依 `Requirement Title`（`Power Loss Handling`）與
> GT-A1 已裁之錨（`4907671` 電源遺失）補其情境，**不改上半一字**。

**pre_conditions**：共通二行
**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Disconnect the head unit battery supply while the update session is in progress
4. Reconnect the battery supply and wait until the head unit completes start-up
5. Read the software version shown on the head unit and record it as Version_after
6. Check that Version_after equals Version_initial and that the head unit remains operable
```
**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. The head unit powers off
4. The head unit completes start-up and its home screen is displayed
5. Version_after is recorded
6. Version_after equals Version_initial; the head unit remains operable and its screen responds to user input
```
**specification_reference**：`CFTS057-4907671`

> **錨之依據**：路徑 A 之首選為 `4907380`（分 0.174，章 4.5.4.1），
> **與本列無關** —— 其成因為 D-1 之缺字使本列無詞可共。
> 錨取 **GT-A1 已裁之 `4907671`**（由區塊錨 R-SU16 三證推得）。
> **本列為 R-SU14 v5「不取首選為錨」之最強實例。**
>
> **範圍紀律**：ER 第 4 行只寫「完成開機」，**不寫「更新自斷點續行」** ——
> 後者屬 `321`（`4907673`）。開機後之防磚與 PBL 狀態
> （錯誤碼 `393216`／`393217`）同屬他列（`Update Agent`），本列不涵蓋。

---

### TC-16 ← `SWE1-FOTA-320`（`newR1L-SU-016`）—— **可寫**

**test_item**
```
The WiFiUpdateService shall detect end-user physical disconnection of the host system (HU/TBM) during OTA server communication, flashing, or software component update and notify SWMC.
(Host system physically disconnected during an update session)
```
> **facet 委派**：本列第二句
> （`The SWMC shall handle the OTA session based on the notification and
> report the update status to the WiFiUpdateService`）之**回報**行為，
> 其需求單元為 `SWE1-FOTA-358`（`Update Status Reporting to SWMC`），
> 依 IN §8.2.1 本 TC 不涵蓋。

**pre_conditions**：共通二行
**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Physically disconnect the host system connector while the update session is in progress
4. Reconnect the host system connector and wait until the head unit completes start-up
5. Read the software version shown on the head unit and record it as Version_after
6. Check that Version_after equals Version_initial and that the head unit remains operable
```
**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. The head unit loses the host system connection
4. The head unit completes start-up and its home screen is displayed
5. Version_after is recorded
6. Version_after equals Version_initial; the head unit remains operable and its screen responds to user input
```
**specification_reference**：`CFTS057-4907672`

> **錨之依據同 TC-15**：首選 `4907279`（章 4.2.3 HU FOTA with TBM）與本列無關，
> 正解 `4907672` 於路徑 A **排第 14**，由 GT-A1 與區塊錨定之。

---

### 4.3 本批之 `I-cross` 預期

TC-12／TC-13／TC-15／TC-16 之窗皆為
`availability-check → version-check`，**且其 ER 皆為肯定式**
（`Version_after equals Version_initial`）——
**R-SU34 v2(b) 之違例類抽取對肯定式 ER 無輸出**，故預期 `I-cross=0`。

⚠ **此為 `I-cross` 之一個未經宣告之射程限制**：
其僅覆蓋否定式 ER 之 TC。本批四個結構高度相同之 TC
（僅第 3 步之觸發動作不同）**完全不會被它比到**。
**須逐包揭露**，並列入 T46 之自評題。

---

## 五、任務（T46）

| # | 任務 |
|---|---|
| T46a | **batch 2a 產出與 lint**：`sandbox/batch02a/` 產出 `newR1L-SU-011`–`016`。**預期 U=6**（TC-11 之 3 + TC-14 之 3）。跑 lint 全輸出 |
| T46b | **`I-cross` 多簿合併模式**（§1.3 裁 (乙)）：`lint036.py` 增 `--merge <簿1> <簿2> …`，使比對範圍等同交付簿。**回測**：以 pilot05 + batch01 + batch02a 三簿合併，其結果須與「三簿併為一簿」之探針**逐項相同**；不同即停 |
| T46c | **`313` 之 TC 與 DR-SU3**：`newR1L-SU-017` ← `SWE1-FOTA-313`，**全欄掛 `PENDING: DR-SU3`**（pre_conditions／procedure／expected_result 各一行，`specification_reference` 取其自證六錨 —— R-SU15(b) 不變）。`DATA_REQUESTS.md` 新增 DR-SU3（§4.1 之表）；`TRACE_MERGE.md` 建檔（R-SU38(a)），首二列為 `313`／`327`，狀態 `上游未確認` |
| T46d | **DR-SU2 增第四型段**（R-SU39(c)）：`315`／`318` 二列，請求為**觸發手段**。DR 文本同步（§3.4 增一類，摘要表更新）。**發送者為 Pei** |
| T46e | **T-抄**：R-SU37 v2、R-SU38、R-SU39 逐字 append；索引表：現行 37 → **39**（+R-SU38、+R-SU39；R-SU37 為版本升級不佔列），留存 23 → **24**。PLAYBOOK 追加二則：(1)「問『還有什麼情形會失敗』是在問想像力，而 TC 之依據是需求文字 —— 答案須回文件核對」（出處：上繳包 29 §9(己)）；(2)「開發期之檢查範圍若小於交付範圍，漏掉的會在最貴的時點才發現」（出處：§1.3） |

**不在本輪**：`Interruption Handling` 其餘 12 列、`Update HMI` 6 列、寫回。

---

## 六、上繳包要求（`docs/upstream/30_batch2a_review.md`）

1. T46e 核對結果 + 索引表（現行 39）
2. T46a 之 lint 全輸出（**預期 U=6**；含 `newR1L-SU-017` 則 U=9）
3. T46b 之合併模式回測
4. T46c／T46d 之台帳與 DR 文本
5. 未結 DR 清單（**3 筆**：DR-SU1／DR-SU2 v3／DR-SU3）
6. 獨立自評 —— 特別回答：**§4.3 所指之 `I-cross` 射程限制
   （只覆蓋否定式 ER）—— TC-12／13／15／16 四者僅第 3 步之觸發動作不同，
   其餘逐行幾乎相同。若其中二列之觸發動作在台架上其實是同一個操作
   （例如「關閉 AP」與「使用者關 Wi-Fi」若台架只有一個 Wi-Fi 開關），
   則二者即為不可區辨 —— 請就台架之實際可行性判斷，此四列中有無此情形**
