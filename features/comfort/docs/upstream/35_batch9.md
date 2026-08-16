# 35 — Comfort HMI / 第十六軸、DR #37 實測、privacy 實測、批次 9

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 50／51
- 結果：八項全數落實。第十六軸登記，**判為功能型**（依據見 §1），
  故 **124 條不回填**。DR #37 實測結論：**可變，阻塞維持**，
  且查出更要緊的一項 —— `14.12` 之前提與條文其餘部分**相矛盾**。
  privacy 已唯讀實測（`ad595ed0…`，11 列，`P10:Q11`）。
  批次 9 產 **26 條**（`-127`…`-152`），停下 9 leaf。
  lint **42/42 PASS，152 條**。ENTRY 006 已產出，3 項 FAIL 同源，不可交付。

---

## 0. 下放包八項之對照

| # | 指示 | 狀態 |
|---|---|---|
| 1 | 登第十六軸，判類別回報依據；介面型則回填 124 條 | ✅ §1 —— **功能型**，故不回填 |
| 2 | 收窄 DR #37 問句，並自行實測「型態是否逐車型可變」 | ✅ §2 —— **可變**，阻塞維持 |
| 3 | DR #34 類名改「入口或操作方式未定義」，`-115` 併入並標子類 | ✅ §3 |
| 4 | `17.1` 三條補 `distinguishing_axis` 與 `duplicate_of` 判定，風險陳述改寫 | ✅ §4 |
| 5 | 唯讀量測 privacy 之 P 欄 DV，更新 A-CF26；不得寫入 | ✅ §5 —— 未寫入該 feature 任何檔案 |
| 6 | `RUNBOOK` 記「一個檢查沒問的問題…」 | ✅ §6 |
| 7 | 更新 DR #6 影響範圍，不新增候選 | ✅ §7 |
| 8 | 執行批次 9 | ✅ §8 —— 產 26、停 9 |
| — | 上繳 35 | 本件 |

---

## 1. 第十六軸 —— 登記，**功能型**

### 1.1 判定依據

R-C34 之判準：某值移除的是**承載可觀察量之介面**（功能仍在）＝介面型；
抑或**功能本身**＝功能型。

**逐一比對既有三個介面型軸，其共同形態是「功能還在，只是換了地方看或看不到」**：

| 軸 | 某值移除了什麼 | 功能是否還在 |
|---|---|---|
| 9 secondary lower screen | comfort section 自 head unit 移除 | **在**（移到下螢幕）|
| 12 僅前排氣候 | tabs 不顯示 | **在**（各分頁之功能仍在）|
| 13 3 旋鈕 ICS | 無 HVAC 畫面／popup | **在**（氣候仍可由旋鈕操作）|

**第十六軸不是這個形態**：車輛若未配備 Comfort Features，
加熱／通風座椅與加熱方向盤**本身就不存在**。`17.3` 之
「this widget page will not be shown」是**功能不存在之後果**，
不是另一個介面之移除。

**反面檢驗（決定性）**：介面型軸之價值在於「**功能仍在而別條 TC 之可觀察量
消失**」。實測全 124 條已生成 TC：**無一條之可觀察量位於 widget 第二頁**，
亦**無一條之功能是 Comfort Features 而其可觀察量在別處**。
該軸不產生「功能仍在而觀察端消失」之情形。

**結論：功能型 → 不進 `interface_axis_review` 之鍵，既有 124 條不回填。**
判定依據已寫入 profile §3.2 之附註。

### 1.2 連帶

`126-01`／`126-03` 解封並已生成（`-125`／`-126`）。
另為該軸增 `axis-values` 區塊（二值、邏輯窮盡、`scan:` 具名），
因 `126-03` 之 PC 為否定式，若無區塊則 43 §4 之覆蓋檢查必紅 —— 已驗證為綠。

`Home Screen Widget` 之 coverage 由 10/21 升為 **12/21**。

---

## 2. DR #37 —— 實測結論：**可變，阻塞維持**；另查出一項更要緊者

問句已依 50 §2 收窄為「ch14 所引用之各硬控，其**物理型態於各車型間是否
固定**？」**執行層自行實測，不待上游**（全 129 節）：

| 控制 | 實測 | 結論 |
|---|---|---|
| **MODE** | `3.1`「If the MODE button is **a multi-directional toggle or a hard control that allows 2 controls (UP/DOWN or RIGHT/LEFT)**」| **可變**（明文二擇一）|
| **RECIRC** | `2.5.1`「**Some vehicles have a configuration for** a 3 state toggle recirc button」| **可變**（明文逐車）|
| **TEMPERATURE** | `2.14` 之「**push button TEMPERATURE**」與同節「3 knob HVAC controls」並列 | **可變**（隨配置）|
| **FAN** | 僅 `7.1`「fan knob」一種形態 | 未見可變之陳述；**惟依 R-C13 零命中不得升為「固定」之結論** |

**故 50 §2 之「實測若顯示全數固定則無此阻塞」不成立 —— 阻塞維持。**

### 2.1 更要緊的一項（原問句沒問到）

`14.12` 是 **ch14 唯一提及硬控之節**，而它寫「**the hard controls**」——
以**整車單一型態**為前提。而上列實測顯示**同一車上各控制之型態本就不同**
（風速為旋鈕、溫度可為按鍵、MODE 可為多向 toggle）。

> **`14.12` 之前提與條文其餘部分相矛盾。**
> 這已不是「缺一個軸」，是「**該句無法適用**」。

DR #37 之待答改為三問：(1)「the hard controls」指哪一個控制？
(2) 各控制型態不同時，popup 樣式各自依其對應控制，抑或全車統一？
(3) 其餘三種型態（RIGHT/LEFT、push button、多向 toggle）之 popup 樣式為何？

**增軸不能解此問** —— 即使逐控制登記三個軸，`14.12` 那一句仍寫著
「the hard controls」，仍指不到任何一個。

---

## 3. DR #34 —— 類名與子類

類名改為「**條文以名詞指稱而未定義其入口或操作方式**」，`-115` 併入。
三例，兩子類：

| 子類 | 例 | 實測 |
|---|---|---|
| `entry` | `16.16` 之 `controls screen` | pattern `controls screen` 全 129 節僅 1 命中（該節自身）|
| `entry` | `16.17` 之 `Voice Recognition session` | pattern `Voice Recognition\|voice command` 命中 4 節，無一節定義如何啟動 |
| **`gesture`** | `17.1`／`17.2` 之 widget 畫面切換（`-115`／`-118`）| pattern `swipe\|scroll\|drag\|gesture` 全 129 節 **零命中** |

**兩子類合為一項而不分立**（50 §3）—— 其處置完全相同，而
**分類之目的是導出不同處置；不導出者只是多一個要記的名字**。
影響 7 條 TC 之可執行性。

---

## 4. `17.1` 三條 —— 由 §4.5 改記為 §4.6，並附 `duplicate_of` 判定

50 §4 之更正正確：§4.5 管的是**一條 TC 之內**資料屬於哪個欄位，
而 `-115`／`-116`／`-117` 是三條 TC 各溯不同 leaf，**不在其射程內**。

§10.6 嚴格等價四項之逐條檢查已寫入 `SWE1-HVAC-124` 之 `distinguishing_axis`：

| TC | trigger | verification target |
|---|---|---|
| `-115` | 循環 widget 畫面 | **畫面之數目**（two）|
| `-116` | 讀第一頁 | **第一頁之身分**（Comfort）|
| `-117` | 移至第二頁 | **第二頁之身分**（Seats）|

**verification target 相異 → 不構成 `duplicate_of`**。依 R-C33 037 之單位不動。

**風險陳述已改寫**：由「§4.5 未消除」改為「**sibling 重疊已依 §4.6 處置**」
—— 前者暗示有一個未修的違規，後者才是實情。

**一項過程紀錄**：我最初把區別 token 加成**逐 TC** 之 `sibling_token` 欄。
它被 doc builder 靜默丟棄（該函式只複製具名欄位），於是
**`json-key-coverage` 全綠而該欄哪裡也沒去** —— 一段通過所有 gate 的死碼。
已刪除，並於註解記其成因：新增逐 TC 欄位需 `NOT_IN_WORKBOOK` 之裁定（26 §4.1），
而 `distinguishing_axis` 本就是為此而設。

---

## 5. privacy —— 唯讀實測完成，A-CF26 由「轉述」改為「實測」

依 50 §5 之授權（R-C21 禁的是代他 feature 建檔與修改，唯讀量測不在其列）。

| 項 | 實測值 |
|---|---|
| 檔 | `features/privacy/output/…_Privacy_20260813_regen-v1.xlsx`（63,001 bytes）|
| SHA256 | `ad595ed0cad24375b64762679487e1e79c714b06f203c0b0c081d6da3b420b7f` |
| 身分 | 與 privacy `DELIVERY.sha256` 所記**已置入客戶交付夾**之副本 hash **相同** |
| 資料工作表 | `dimension A1:AH59` |
| **已填列** | **row 10–20，共 11 列**（`NR1L-Privacy-001` ～ `-011`）|
| **P 欄 DV `sqref`** | **`P10:Q11`** |
| R 欄 x14 `sqref` | `R10` ＋ `R11:R59` —— **11 列全在範圍內**，design_method 側**無缺口** |
| `T–Z` / `AF` DV | `T10:Z11` / `AF10:AF11` |

**故 privacy 已交付件之 `row 12–20`（9 列）確實無 P 欄下拉約束**，
數字與 46 §2 所述相符。A-CF26 之陳述已更新為實測，並保留
「**未寫入該 feature 任何檔案**」之聲明（`git status` 對 `features/privacy/`
零命中）。

---

## 6. `RUNBOOK.md` —— 「一個檢查沒問的問題…」

已逐字記入，含其成因（九項 assertion 未檢查 DV 涵蓋；四項確認問「R 欄下拉
可用」而 `R10` 恰在範圍內）與三項可操作推論。核心句：

> **兩道檢查各自都對，合起來仍然什麼都沒問。**
> 綠燈之總數與涵蓋範圍無關 —— 十項綠燈可以全部避開同一個問題。

第 3 項推論值得單獨看：**抽樣式的確認項（「R 欄下拉可用」）會被第一列滿足**；
凡措辭為「某欄可用」者，須改為「**每一寫入列**之該欄可用」。

---

## 7. DR #6 —— 影響範圍更新，未提新候選

由「3 節」更新為 **3 節 ＋ 9 leaf**（`19.1`–`19.3`
＋批次 8 之 `125-08`／`126-02`／`127-01`／`127-02`／`128-01`／`-02`／
`129-01`～`-03`）。`Home Screen Widget` 之 coverage 為 **12/21（57%）**。

其中 `128-01`／`-02` 另因 dual airflow modes 軸而停，已另立 **DR #38**
（三條件第一項不成立：正向值於三節逐字出現，**其反面於全 129 節無任何字面**，
pattern `single airflow|without dual airflow|not equipped with dual` 零命中）。

**本項為成本更新，非重提問題** —— 分析層已言明不再猜候選檔案，
故**不提出新候選**。處置由 Pei 決定；現行作法（續行其他組）不需動作即維持。

---

## 8. 批次 9 —— `Climate Modes`

### 8.1 節次與 leaf 數，自 framework.md 導出，與 037 相符

| outline | leaves |
|---|---|
| `2.3` | 9 |
| `2.3.1` | 2 |
| `2.4` | 4 |
| `2.5` | 4 |
| `2.5.1` | 2 |
| `2.10` | 6 |
| `2.11` | 5 |
| `2.13` | 3 |
| **合計** | **35** |

037 獨立實測：003(9)＋004(2)＋005(4)＋006(4)＋007(2)＋014(6)＋015(5)＋019(3)
= **35**。相符。

### 8.2 產 26（`-127`…`-152`），停 9 —— 四種成因，無一為新

| leaf | 成因 | 去向 |
|---|---|---|
| `004-01`／`-02` | dual airflow modes 軸未登記 | DR #38 |
| `006-04` | 「as displayed in **the table**」未指名節次，全 129 節無該對照 | DR #32 之「configuration → icon」類 |
| `007-01`／`-02` | RECIRC 控制型態逐車可變而該軸未登記 | DR #37（即其實測所引三例之一）|
| `015-04`／`-05` | 可觀察量在**後排**，而「是否配備後排氣候」不在十六軸內 | DR #17 |
| `019-02`／`-03` | 「On/Off logic should follow requirements from **VF HVAC document**」—— 明文**外部**委派 | `[BLOCKED-SPEC]` 形態，白名單須裁（**R-C26**）|

`019-02`／`-03` 之形態與 `080-02`／`081-02` **完全相同**，故不自行標記。
**且不以 `16.13`（ICE12）之逐項列舉補之** —— 那是另一套介面之條文，
援引即跨介面移植（§8.2.1）。

`006-04` 值得記一句：**`16.5`（ICE4）逐字重述該句，且把表之位置寫成
`Climate Main page table`（比 ch2 的「the table」還具體），仍未給對照** ——
所以這不是「ch16 有而 ch2 無」，是**兩側皆無**。

### 8.3 R-C36-1 於本批密集適用 —— 26 條中 **6 條為 `no`**

51 §2 預告本批之 ch16 對造多為 `partial`，而 `ch16_mirror_map.tsv` 之分界欄
正是為此備妥的。逐條答之結果：

| TC | ch16 | verdict | 何以 |
|---|---|---|---|
| `-130`（AUTO 與四模式互斥）| 16.3 | **no** | **ICE2 之互斥對象為 MAX A/C 與 MAX DEF**，不含四氣流模式與 front defrost |
| `-131`（AUTO 改 A/C 而不顯示）| 16.3 | **no** | **ICE2 語意相反**：「In Auto the A/C button is highlighted」|
| `-137`（Auto 自動開 A/C）| 16.4 | **no** | 分界欄：「未涵蓋：C3 之『Auto can automatically turn on AC』等連動邏輯」|
| `-138`（A/C 中斷 Auto）| 16.4 | **no** | 同上；**且 ICE2 為「Manually selecting A/C keeps the system in AUTO」—— 語意相反** |
| `-139`（Defrost／Recirc 自動開 A/C）| 16.4 | **no** | 同 `-137` |
| `-141`（RECIRC 灰化）| 16.4 | **no** | 分界欄：「未涵蓋：C4 之可用性灰化」|

**其中 `-131` 與 `-138` 不是「ch16 沉默」，是「ch16 說了相反的話」。**
兩者在台帳上都記 `no`，但其意義不同：前者是**缺口**，後者是**衝突**。
本輪如實記其措辭而未合併為「無對應句」。

> **這是 `partial` 分界欄第一次成規模地用在生成上**，而它省下的正是
> 「每次重讀 ch16 全文再判一次」的成本 —— 37 §2 立該欄時所預期者。

### 8.4 §4.6 回填 —— 兩對 sibling，兩種結論

批次 9 使 `2.10`／`2.11` 落地，`pending-sibling` gate 立刻對兩對變紅：

**(一) `2.6.1 ↔ 2.11`（SYNC）—— 兩對 TC 嚴格等價**

| | trigger | outcome | 判定 |
|---|---|---|---|
| `-053` vs `-150` | SYNC on ＋ 改駕駛側溫度 | 乘客側跟隨 | **四項全同** |
| `-054` vs `-151` | SYNC on ＋ 改乘客側溫度 | SYNC 關閉 | **四項全同** |

**`duplicate_of` 未設**，理由必須寫明而非省略：
**§10.6 之該欄是「節級」且為工作簿列號，而此處之重複是「條級」**
（2.6.1 之 6 條中 2 條、2.11 之 3 條中 2 條）。設之即宣稱**整節重複**，為假。
兩節之 `distinguishing_axis` 已具名其分界（2.6.1 之主題為**溫度調整途徑**，
2.11 之主題為 **SYNC 這個功能本身**）。

> **待裁**：`duplicate_of` 之粒度為節級，而重複可以是條級。
> 現行 schema 表達不了「這一節的第 1、2 條與那一節的第 1、2 條重複」。

**(二) `2.10 ↔ 3.3`（climate off 之 defrost 例外）—— 同一事實之兩側**

`3.3`（C21）自**例外**側陳述（MAX DEF／REAR DEF 於 climate off 期間可用），
`2.10`（C11）自**通則**側陳述（其餘按鈕灰化，該二者為例外）。
verification target 相異（該二者可用 vs 其餘變灰）→ **不構成 `duplicate_of`**，
已於 `2.10` 之 `distinguishing_axis` 具名。

**另修一處機制缺陷**：`gen_batch4.py` 之 doc builder 把
`distinguishing_axis` 寫死為 `see per-TC titles`，
使批次內任何節都無法帶自己的判定。已改為 `b.get(...)`，與 batch8 一致。

### 8.5 92 列 provisional 重新確認

全部逐對判完並清旗。分佈：ch2↔ch10 30、ch2↔ch2 22、ch2↔ch16 19、
ch2↔ch3 15、ch2↔ch17 6。除上述兩對 `sibling` 維持外，其餘判為 `not-sibling`。

ch16 一側之理由值得記：**本批 26 條之 `emea_ics_review` 逐條指向 ch16 之
具體句並記其 `yes`／`no`，該逐條答本身即「兩節非同一需求」之逐句證據** ——
不必另找理由。

`provisional` 現 `false` **238**／`true` 1430。

---

## 9. 第四次寫回 —— ENTRY 006

前置 gate 6 項全 PASS（TC 數實測 152、tc_id 001–152 連續無缺號）。
splice row 10–161，152 列。assertion **10 PASS、3 FAIL**，
三項與 ENTRY 004／005 **完全同源**（範本 50 列）：

| FAIL | 後果 |
|---|---|
| B 欄公式止於 row 59 | **102 列無列號** |
| R 欄下拉止於 row 59 | **102 列無下拉** |
| P 欄 DV 止於 row 11 | **150 列無下拉** |

A-CF19 呈現側：N 欄最長 599 字元、可見約 2%，與 ENTRY 005 同。

依 46 §3：**不送 Excel 四項確認**，`DELIVERY.sha256` 增 **ENTRY 006**，
狀態記「範本容量待擴充 —— 不可交付」，`output/STATUS.md` 同步。

---

## 10. lint 與 §9 自評

```
42 / 42 gates PASS; 0 finding(s) across 152 TCs
```

TC 126 → **152**；leaf 121 → **147**；已生成節 41 → **46**。
`pending_sibling.tsv` 1668 列，重建冪等。

**§9 十七項**：本輪新增 26 條（批次 9）＋ 重生成 2 批（batch4／batch8，
`distinguishing_axis` 之機制修正，TC 內容未變）。

| # | 項目 | 變動 | 獨立依據 |
|---|---|---|---|
| 1 | Test Set | 變 | `Climate Modes`，自 framework.md 第 2 組 |
| 2 | tc_title | 變 | 26 條皆 2–14 字、無 modal |
| 3 | Pre-Condition | 變 | 第一軸（ATC／MTC，2.3）／第二軸（2.11）／第四軸（2.13）／第五軸＋第十軸（`-144`，3.2／3.4）＋ 軸 13（2.14）＋ EMEA（16.2）＋ 軸 9（6.3）|
| 4 | Input Test Data | 變 | 全數 `NA` |
| 5–8 | 步驟 | 變 | 每條 2–4 步，末步持驗證；無禁用動詞 |
| 9 | Baseline | 變 | `-129`／`-131`／`-137`／`-142`／`-147` 需前後對照，首步建立基線 |
| 10 | Procedure ↔ ER 1:1 | 變 | 26 條全數 1:1，ER 無 modal |
| 11 | FP／FF | 變 | `-131`（不顯示變化）、`-134`（不中斷）、`-135`（不顯示 AUTO）、`-139`（不顯示）四條為否定式，各配正向步驟 |
| 12 | 溯源、§8.2.1、§8.4 | 變 | 26 leaf 各溯其 037 req_id；9 leaf 依 §8.4.2 停下不吸收；**不以 ICE12 補 `019-02`**（跨介面）|
| 13 | Design Method | 變 | 25 條功能測試、`-147` 狀態轉換（關閉後回復至上次等級）|
| 14／15 | §11 格式 | 變 | 無行尾句點；UI 標籤用 `"…"` |
| 16 | `specification_reference` | 變 | 各條含自身節次 ＋ 2.14 ＋ 16.2 ＋ 6.3；`-144` 另加 3.2／3.4（R-C29）|
| 17 | §8.6／§8.7 | 變 | `-133` **只驗確定之一半**（按下特定模式鍵即進該模式）；「most closely matches」無對照表故不寫入 ER（§8.4.1）|

---

## 11. 「本包是否仍有該驗而未驗者」（R-C30）

1. **批次 9 之 26 條未經 §7 之 FP／FF 人工複核**，只經 lint。
2. **`-133` 只涵蓋 C2 之一半。**「the manual mode that **most closely matches**
   the auto mode exited」無對照表，該半未驗，**已於 reasoning 具名而未開 DR**
   —— 它與 DR #32 之「對照未定義」同型，是否併入待裁。
3. **`duplicate_of` 之粒度問題未解**（§8.4）—— 現行 schema 表達不了條級重複。
4. **DR #37 之三問未答前，`Climate Popups`（42 leaf）仍不宜開工。**
5. **`Climate Modes` coverage 為 26/35（74%）**，停下之 9 leaf 分屬四個既有 DR。
6. **第十六軸之類別判定依賴「實測 124 條無一條之可觀察量在 widget 第二頁」** ——
   該陳述於**未來新增 TC 時可能失效**（例如 ch11／ch12 生成時），
   **無任何機制會在那時重問**。與 `provisional` 之問題同型而尚無對應機制。
7. **`006-04` 併入 DR #32 之類，但 DR #32 之標題仍以座椅 off icon 為名** ——
   類項之標題未隨其成員擴充而更新。

---

## 12. 建議 commit message（git 未執行）

```
feat(comfort): batch 9 Climate Modes; axis 16, DR #37 measured

- register axis 16 (Comfort Features present/absent) and judge it
  FUNCTION-type, so the 124 existing TCs are NOT backfilled. The evidence
  is the reverse test: an interface-type axis matters because the function
  survives while some other TC's observable disappears — measured, no TC
  observes the second widget page and none has Comfort Features as its
  function with its observable elsewhere. 126-01/-03 unblocked
- DR #37 measured without waiting upstream: the form VARIES (MODE, RECIRC
  and TEMPERATURE all have per-vehicle alternatives in the clauses), so the
  block stands. And a sharper finding — 14.12 says "the hard controls",
  presupposing one form per vehicle, while the corpus has one vehicle
  carrying three different forms. That is a contradiction, not a missing
  axis, and no number of axes would fix that sentence
- DR #34 becomes "entry OR interaction undefined", -115 folded in with an
  `entry`/`gesture` subtype. Same disposition, so one item, not two
- 17.1's overlap re-recorded as §4.6 not §4.5, with the §10.6 four-part test
  written out per TC. A first attempt put the token in a per-TC field that
  the doc builder silently dropped — dead code that passed every gate
- privacy measured read-only (50 §5): ad595ed0…, 11 rows, P10:Q11, so rows
  12-20 confirmed. A-CF26 moves from relayed to measured. No file under
  features/privacy/ was written
- batch 9: 26 TCs, -127..-152, 9 leaves stopped across four existing DRs.
  019-02/-03 delegate to the VF HVAC document — same shape as 080-02, so
  the [BLOCKED-SPEC] whitelist is a ruling, not ours to take
- R-C36-1 bites hardest here: 6 of 26 get a `no`, and two of those are not
  "ch16 is silent" but "ch16 says the opposite" — recorded as such
- backfill two sibling pairs. 2.6.1<->2.11 has two strictly equivalent TC
  pairs, and duplicate_of is still NOT set: §10.6's field is section-level
  while the duplication is per-TC. Setting it would claim the whole section
  duplicates, which is false
- lint 42/42 PASS across 152 TCs; ENTRY 006, same three template FAILs,
  not delivered
```

---

## 13. 待分析層

1. **§8.4 / §11.3** —— `duplicate_of` 之粒度：節級欄位表達不了條級重複，
   是否擴充 schema 或另立記法。
2. **§2.1 / DR #37** —— `14.12` 之矛盾；**建議先於 `Climate Popups` 開工**。
3. **§11.2** —— `-133` 未涵蓋之「most closely matches」是否併入 DR #32 之類。
4. **§11.6** —— 第十六軸之類別判定依賴當下語料，將來可能失效而無回訪機制；
   是否比照 `provisional` 立一個「軸類別待複核」旗標。
5. **§11.7** —— DR #32 之類項標題是否隨成員擴充更新。
6. **DR #35 / A-CF26** —— 範本擴充仍為交付之硬阻塞（現 152 列，102 列無下拉）。
7. **批次 10 之授權**；建議 `Airflow and Defrost`（DR #31 只卡其 2 leaf）
   或 `Rear Climate`（`ch2_ch7_mirror_map` 已備）。
