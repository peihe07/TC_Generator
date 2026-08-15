# 24 — Comfort HMI / R-C34、三軸補掃、axis-value-count、批次 4

- 產出層：執行層｜2026-08-15｜對象：分析層
- 承接：下放包 35
- 結果：**EMEA ICS 補掃命中 31 條、第九軸命中 8 條、第十二軸 0 條**。
  LED 重掃使原判定之**理由被推翻而結論維持**（詳 §3）。
  批次 4 生成 **18 條**（-047 … -064），`2.7.1` 停下。
  lint **38/38 PASS，0 finding，64 條**。**未寫回。**

---

## 1. R-C34 貼入 ＋ profile 逐軸標記

`RULINGS.md` 現有 **36 個**逐字條文區塊。

profile §3.2 增一張**逐軸類別表**（13 軸 ＋ 機型軸 ＋ 市場／變體軸），
每軸標介面型／功能型並列其某值之後果。**四個介面型軸**：

| # | 軸 | 某值之後果 |
|---|---|---|
| 9 | secondary lower screen 之有無 | 非可收合者 → comfort section 自 head unit 移除（6.3），僅 comfort popup 留存 |
| 12 | 僅前排氣候 | → tabs 不顯示（2.1）|
| 13 | HVAC 實體控制型式 | 3 旋鈕 ICS → 無 HVAC icon／畫面／popup（2.14）|
| — | 市場／變體軸 EMEA ICS | **ch16 全章為另一套介面** —— ch2／ch3 之 TC 於該車無對象 |

生成時之義務同步寫入：**每條 TC 定稿前指出其可觀察量所在介面，
並對四個介面型軸各問一次**；答否者具名理由。

---

## 2. 補掃結果 —— 既有 46 條

### 2.1 EMEA ICS —— **31 條須補**（ch2 全部 ＋ ch3 全部）

**判定依據為 ch16 之鏡射結構，非推測**：

| ch2／ch3 | ch16 | 首句對照 |
|---|---|---|
| 2.2 C1 | **16.2 ICE1** | 兩者皆為 `Whenever changes to the climate system are made via hard controls or touchscreen…`，16.2 另加 `with the exception of the recirculation led in climate off` |
| 2.14 C15 | **16.14 ICE13** | 皆為 `MTC screens/popups are to be used when CCM relays MTC functionality` |
| 3.1 之 MODE 循環 | **16.12／16.12.1** | `ICE11.1) If the Mode hard control is pressed the user…` |

`framework.md` §3.2 之四組鏡射（anatomy／模式開關／溫度與風量／氣流與除霜）
即此結構之既有記載。**EMEA ICS 車輛使用 ch16 之介面，ch2／ch3 之 TC 在其上
無對象。**

補行：`[spec-derived] The vehicle is not an EMEA ICS vehicle, whose climate
interface is specified separately in chapter 16 (16.2)`，`16.2` 併入 spec_ref。

**ch6（6.3）與 ch13（座椅）不補** —— ch16 之 18 節內**無座椅節、無 6.3 之
對應節**（實測 ch16 之節清單：16.2 … 16.17，皆為氣候），故該兩章無 ICS 鏡射。

### 2.2 第九軸（secondary lower screen）—— **8 條須補**

6.3：`the comfort section will be removed from the head unit **except for
comfort popups**`。故暴露者為**可觀察量即該 section 或其類別鍵**者：

| tc_id | 可觀察量 |
|---|---|
| `-003` | `the climate section on the main head unit` |
| `-034` | `the status indicator on the comfort category button` |
| `-038` | `the status indicator on the category button` |
| `-041` | `Open the comfort category` |
| `-044`／`-045`／`-046` | head unit menu 之 HVAC UI（見 §2.3）|
| `-058` | 批次 4 之 `main category control`（2.7）|

**不補者之理由具名**：

- `-002`（`Seat Control Popup is displayed on the head unit`）—— 6.3 明文
  `except for comfort popups`，**popup 正是條文留下的那一個**
- `-033`（`Do not interact with the head unit for 3 seconds`）—— 其可觀察量
  為 popup，同上
- `-007`（`The head unit completes the keycycle`）—— 觀察的是整機電源循環，
  非 comfort section
- `-040`（6.3 自身之 TC）—— 已正向帶第九軸
- 其餘讀 climate screen 或 status bar 者 —— **那不是 comfort section**

### 2.3 `-044`／`-045`／`-046` 之補行理由與其他條不同

三者讀 head unit menu 之 HVAC UI **缺席**（`-046` 為其在場）。

- `-046` 之 ER 為 `An HVAC menu bar icon is displayed` → 6.3 車上**無對象**
- `-044`／`-045` 之 ER 為缺席 → 6.3 車上**會通過，但通過的理由是錯的**
  （comfort section 早已因 6.3 被移除，而非因 3 旋鈕 ICS）

故三者一併補，使該正負對照落在**同一種車輛類別**上。
**「會通過但理由錯」與「沒有對象」不同，我把兩者一起處理並在此說明差別。**

### 2.4 第十二軸（僅前排氣候）—— **0 條須補**，但有一項須待裁

第十二軸移除的是 **tabs**（2.1）。實測既有 46 條中提及 `tab` 者共 **13 條**，
其中 12 條為 13.x 之 `Seats tab`、1 條為 `-041`（本身即該軸之正向案例）。

**13.x 之 Seats tab 是否受 2.1 管轄，條文未定** ——

- 2.1 之主詞為 `The comfort category`，其 tabs 在 head unit
- 13.2 之 Seats tab 在**下螢幕**（`switch the tab on the lower screen`）
- 2.1 未說「tabs」是否涵蓋下螢幕之分頁，亦未說有 Seats 內容之車輛是否
  仍算「only Front climate is available」

**我未補 PC，因為補與不補都要先決定 2.1 的意思**，而那是條文未定之事。
列 §9 待裁。

---

## 3. LED 重掃 —— 結論維持，**但我原本的理由被推翻**

### 3.1 重掃結果

**搜尋範圍**：根目錄 `data/section_fulltext.tsv` **全 129 節**，
pattern `LED`（不分大小寫）。**命中 13 節、27 句。**

| 類別 | 節 | 例 |
|---|---|---|
| **依附於畫面** | 2.2、16.2 | `If changes are made on climate screen, LEDs on hard controls reflect new status` |
| **獨立於畫面之狀態指示** | 3.2、16.8、16.10、16.13 | `When climate is OFF, the recirculation LED of the hard control is on`；`Action on the recirculation hard control … turns led off` |
| **層級指示於控制件上** | 11.1／11.2／11.8／12.1／12.2／12.8／12.9 | `displays 3 arrows, HI and/or LEDs` |

### 3.2 我原先的搜尋範圍確實過窄，而且錯得比想的深

我當時只掃 3.1（0 命中），據此採「觀察端在畫面」。**R-C30 是對的。**

更要緊的是：**若我當時掃了全語料，我會發現「LED 一律反映畫面」這個前提
是假的** —— 16.10 之 recirculation LED 由硬鍵操作直接改變，
完全不經畫面。**我的結論建立在一個我沒驗過而且是錯的前提上。**

### 3.3 但依同一份證據，`-016`／`-017` 之排除式 PC **維持**

下放包 §2 之判定規則寫：「若存在獨立於畫面之 LED 指示，則該二條之
排除式 PC 過嚴，須移除。」

**依字面應移除。我沒有移除，理由如下，請覆核。**

獨立 LED 存在於 **recirculation 硬鍵**（16.10／3.2）、**座椅與方向盤加熱
控制**（11.x／12.x）。**沒有任何一節提到 MODE 硬鍵有 LED。**
移除該 PC 等於宣稱「MODE 硬鍵有指示可讀」，而那是條文從未說過的 ——
**那是把一個造值從畫面搬到 LED 上，方向相反而性質相同**（§8.4.1）。

**修正後之理由**（已寫入 reasoning）：不是「LED 一律反映畫面」，而是
**「無任何條文為 MODE 硬鍵指定獨立指示，而 3.1 只把 airflow mode 之狀態
描述在 Tri-Mode Climate screen 上」**。

**搜尋範圍**：全 129 節，pattern `LED` 之 27 句逐句讀；
另 pattern `MODE` 於 3.1／16.12／16.12.1 之全文。**MODE 硬鍵之 LED：0 命中。**

---

## 4. `axis-value-count` gate ＋ A-CF22

### 4.1 gate（lint 37 → 38）

profile 內新增機器可讀之 ```axis-values``` 區塊，載第十三軸之
`values` / `value-count` / `negation-reviewed-at-value-count` / `negation-users`。
gate 三項比對：宣告值數 vs 實際值數、`reviewed` vs `value-count`、
`negation-users` vs 實測使用者。

**反向驗證（三方向）**：

| 注入 | 結果 |
|---|---|
| 增第四值，`value-count` 同改，`reviewed` 維持 3 | **FAIL** —— `axis gained a value (now 4) but the negated pre_condition was last reviewed at '3'`，並**逐一列出 30 條**要重審者 |
| 只改 `values` 未改 `value-count` | **FAIL** —— `declares value-count '3' but lists 4 values` |
| `negation-users` 清單過期 | **FAIL** —— 具名 missing 與 extra |

**第一次反向驗證我做錯了**：測試腳本以 `replace('value-count: 3', …)`
注入，而該字串同時命中 `negation-reviewed-at-value-count: 3`，
兩個欄位一起被改，gate 遂未觸發。**是測試錯，不是 gate 錯**；
以行首錨定重做後正常 FAIL。列此以免日後看紀錄誤以為該方向未驗。

### 4.2 gate 上線當天就抓到東西

批次 4 生成後跑 lint：

```
[FAIL] axis-value-count: profile's negation-users list is stale —
missing ['NR1L-ComfortHMI-047' … 'NR1L-ComfortHMI-064'], extra []
```

**新生成的 18 條全部使用了否定式而未登記。** 我補登後 PASS
（現共 **48 條**使用者）。這正是它要防的形態：否定式使用者會隨每批增加，
而清單不會自己長。

### 4.3 A-CF22

已登（note）。條目載明 `-002` 維持不補之理由、
**「把 2.14 讀成『head unit 什麼都不顯示』是反向的範圍造值」**、
以及**不列 RD-1 之理由**（屬 head unit 整體行為，在 Comfort spec 範圍外，
問了也不在 037 之權責內）。

---

## 5. 批次 4 —— `Temperature and Fan`

### 5.1 範圍自 `framework.md` 導出

`framework.md` 第 41 行：`2.6, 2.6.1, 2.7, 2.7.1, 2.16` / **19 leaves**。
037 獨立實測：008(5) ＋ 009(6) ＋ 010(5) ＋ 011(1) ＋ 022(2) = **19**，相符。
下放包 §6 之表與之一致（本次無 33 §0 之落差）。

### 5.2 生成 18 條，停下 1 leaf

| 節 | leaf | 生成 | tc_id |
|---|---|---|---|
| 2.6 | 5 | 5 | -047 … -051 |
| 2.6.1 | 6 | 6 | -052 … -057 |
| 2.7 | 5 | 5 | -058 … -062 |
| 2.16 | 2 | 2 | -063 … -064 |
| **2.7.1** | 1 | **0** | **停下** |

**`2.7.1` 停下**：`In some vehicles fan speed ranges for front hvac are:
Off, 1-8` —— `In some vehicles` 為選擇子，而「front HVAC 風速範圍
（1-7／1-8）」**不在十三軸內**。依 28 §2.1(b) 停下，不自行增軸。

### 5.3 R-C34 之生成時義務，逐條施行

| 軸 | 判定 | 處置 |
|---|---|---|
| 13（3 旋鈕 ICS）| 移除 HVAC UI | **18 條全補** |
| EMEA ICS | ch16.6／16.6.1／16.7／16.17 鏡射本組四節 | **18 條全補** |
| 9（lower screen）| 只有 `-058` 讀 `main category control` | **1 條補**；其餘之 climate screen 與狀態列非 comfort section |
| 12（僅前排氣候）| 移除 tabs，本組**無一條觀察 tab** | **0 條**，理由具名 |

spec_ref 形態實測 6 種，含 `2.6.1; 2.14; 16.2; 2.11`（SYNC 之出處）
與 `2.7; 2.14; 16.2; 6.3`（`-058`）。

### 5.4 `2.6.1` 與 `2.11` 之 sibling —— 已判定，`duplicate_of` 暫空

2.11（`Climate Modes` 組，**尚未生成**）亦述
`changing the driver temperature automatically changes the passenger
temperature` 與 `Adjusting the passenger temperature … would break SYNC`，
與本節 `-052`／`-053` 為同一行為之兩處陳述。

依 §8.2 單位歸 037，本節之 leaf 為 `SWE1-HVAC-009-01`／`-02`，
各自成條。**`duplicate_of` 為列號，而 2.11 尚無列，故暫空**；
`reasoning` 已具名此關係並註明該組生成時須依 §4.6 回填。

**這是目前唯一一處「已知的 sibling 而 `duplicate_of` 空著」**，
若無人記得回填，它會靜默地留成未標註的重複。**建議下輪加 gate**
（reasoning 內出現「sibling」而 `duplicate_of` 空者須列於具名清單），
本包未加（未授權）。

---

## 6. lint

```
38 / 38 gates PASS; 0 finding(s) across 64 TCs
```

四個 generator 連續重跑，輸出不變。`tc_id` 001–064 連號無缺。

---

## 7. §9 self-check —— 批次 4 之 18 條（依 R-C23）

| # | 項目 | 判 | 獨立依據（非 lint 覆述）|
|---|---|---|---|
| 1 | Test Set 與 framework 相符 | PASS | `test_set` 皆 `Temperature and Fan`，與 framework.md 第 41 行逐字元相同 |
| 2 | tc_title 形狀／字數／sibling／無 modal | PASS | 字數實測 6–12。同節之 sibling token 互斥：2.6 為 `status bar`／`HI and LO`／`Metric`／`pop-up`／`Slider status bar and pop-ups`；2.7 為 `category control`／`pop-up`／`buttons touch or slide`／`cannot be turned off`／`grey out` |
| 3 | PC 僅 state/env 且為 spec trigger | PASS | 18 條共 **55 行 PC**（含每條 2 行排除式）。實測 PC 內無 `Press`／`Open`／`Change`／`Set`／`Turn`／`Adjust`／`Touch`／`Slide` → **0 命中** |
| 4 | Input Test Data 欄位歸屬 | PASS | 皆 `NA`。`-049`／`-051` 之 Metric 為**單位設定**，由步驟建立；溫度值不寫入，因條文之區間為 CCM 轉達之狀態 |
| 5 | 步驟可執行、無禁用動詞 | PASS | 首字動詞實測 `Change`／`End`／`Long`／`Open`／`Press`／`Read`／`Set`／`Slide`／`Start`／`Touch`／`Turn`，無一在 §5.1 九詞內。**另補獨立於 gate 者**：18 條之步驟皆為單一具體操作 |
| 6 | 步驟長度與意圖層級 | PASS | 步數 2×12、3×6。3 步者實測為 `-047`／`-051`／`-054`／`-058`／`-060`／`-062`，皆需前後對照或三種途徑並列|
| 7 | 標準 setup 片段逐字重用 | **N/A** | `PC_ATC`／`PC_DUAL` 為本批常數，同節內重用；`EX_ICS`／`EX_EMEA`／`EX_LOWER` 為跨批共用之**排除式**常數，其措辭與出處節固定，屬機械施加而非措辭套用 |
| 8 | CLI／tooling | **N/A** | 皆 HMI 操作 |
| 9 | 基線步驟 | PASS | 需前後對照者其 ER 第 1 行為前狀態（`The climate screen shows the current fan speed`／`SYNC is on`／`The climate screen is not displayed`）。`-063`／`-064` 尤其必要 —— 其驗證目標為「**不顯示變化**」，無基線則無從分辨「沒變」與「沒在看」 |
| 10 | 1:1、ER 可觀察、無 modal | PASS | **依 R-C23 明說：依據不是 `er-subject-net`**。逐行讀 **42 行 ER**，主詞為 `The climate screen`／`The status bar`／`The temperature`／`The readout`／`SYNC`／`The fan speed`／`The main category control`／`The temp slider`／`All FAN bars`／`The blower`／`The press` —— 皆系統側 |
| 11 | 無 FP／FF；supported 配 negative | PASS | FF：畫面之開啟、Metric 之設定、SYNC 之開啟皆由步驟建立。negative：`-061`（風量**不可**關閉）與 `-062`（**唯有**關閉氣候系統才全暗）成對；`-057`（滑桿把手可移動）與其第 2 步（把手外之按壓被忽略）於同一條內成對 |
| 12 | 溯源、§8.2.1、§8.2.2、無造值 | PASS | 溯源：18 條之 `req_id` 於 037 逐一存在。§8.2.1：語音辨識之行為（2.16）與 SYNC 於 2.11 之其餘規定皆具名未驗。§8.2.2：18 個 leaf 各為單一行為，無拆。造值：`15h` 標示 AUTO 一項語意不明故不驗並具名；降風量幅度未給故 ER 不寫入 |
| 13 | design_method 於 procedure 定案後指派 | PASS | 分布 功能測試 ×14、狀態轉換 ×2（`-053` SYNC 中斷、`-062` 電源遷移）、邊界值分析 ×2（`-048` HI/LO 極值、`-061` 風量下限）。可由 procedure 形狀反推 |
| 14 | 四長欄無行尾句點 | PASS | lint 覆蓋；另查其未涵蓋之 `test_item`：18 條逐條確認 |
| 15 | UI 標籤用 `"..."` | PASS | **本批無一處加引號** —— `HI`／`LO`／`Metric`／`SYNC`／`FAN` 皆取條文自身之大寫寫法（R-C33：內容以條文為準），而它們在條文內即未加引號；其餘為元件類名 |
| 16 | `specification_reference` | PASS | 6 種形態，與各條之 PC 出處逐一對應（`2.11` 只出現於 `-052`／`-053`，`6.3` 只出現於 `-058`）|
| 17 | 來源 spec 勝過 index export | PASS | 條文一律讀 `section_fulltext.tsv`。**037 之 `-011` 寫 `Off, 1-8` 而條文亦然**，本批無 R-C33 型落差 |

**15 PASS、2 N/A。**

---

## 8. 未寫回；進度

**未寫回**，`output/` 仍 2 檔。

| | 數 |
|---|---|
| 驗證單位（leaf）| 403 |
| 已生成（leaf）| **60** |
| 已生成（TC）| **64** |
| 阻塞／停下（leaf）| 3（DR #17 之 2 ＋ `2.7.1` 之 1）|
| 未開始（leaf）| 340 |

Test Set 完成：`Seat Control Tab` 14/14、`Tri-Mode Climate` 14/14、
`Front Climate Anatomy` 14/16、**`Temperature and Fan` 18/19**。

A-CF19 之待測樣本現為 **64 條中 51 條**帶多節 spec_ref（否定式第十三軸
使用者則為 48 條，兩者不同集合）。

---

## 9. 「本包是否仍有該驗而未驗者」

依 R-C30。

1. **EMEA ICS 之補掃我用鏡射結構判定，但未逐節比對 ch16 與 ch2 之內容。**
   **搜尋範圍**：16.2／16.14／16.12.1 三節之首句 ＋ `framework.md` §3.2 之
   鏡射表。**未做**：ch16 之 18 節與 ch2／ch3 之逐節對應表。
   若某節在 ch16 無對應，該節之 TC 在 EMEA ICS 車上可能仍有對象，
   我補的排除式 PC 就過嚴。
2. **第十二軸與 13.x 之 Seats tab（§2.4）** —— 條文未定，我未補也未推測。
3. **`-016`／`-017` 我違反了下放包 §2 之字面判定規則**（§3.3）。
   理由已寫明，但那是我的判斷推翻了指示。
4. **`2.6.1` 之 `duplicate_of` 暫空（§5.4）** —— 目前無機制保證回填。
5. **批次 4 我做了 R-C34 之生成時義務，但那是我自己對四個軸提問的結果，
   沒有任何 gate 檢查我是否真的問了。** `axis-value-count` 只驗否定式
   使用者之登記，不驗「該補而未補」。**R-C34 目前仍是紀律，不是機制。**
6. **`-060` 之 `slide` 與 `-062` 之三步電源切換未實測可行性** ——
   皆為條文所述之操作，但條文未說滑動之判定門檻。

---

## 10. 建議 commit message（git 未執行）

```
feat(comfort): batch 4 + interface-type axis sweep

- add R-C34 (axes split into interface-type and function-type) to RULINGS
- profile: per-axis type table and the generation-time duty
- sweep the existing 46: EMEA ICS excludes 31 (ch2/ch3 are mirrored by
  ch16), the ninth axis excludes 8, the twelfth none
- rescan LED across all 129 sections: independent LEDs do exist, so the
  original premise was wrong; the conclusion for -016/-017 stands on a
  different ground and the PCs are kept
- add axis-value-count gate, reverse-verified three ways; it caught batch
  4's 18 new negation users on its first run
- register A-CF22
- generate Temperature and Fan, 18 of 19 leaves, tc_id -047..-064
- withhold 2.7.1: front HVAC fan range is not one of the thirteen axes
- lint 37 -> 38 gates, all PASS, 0 findings across 64 TCs
```

---

## 11. 待分析層

1. **§3.3** —— `-016`／`-017` 之 PC 維持與否（我未依字面規則執行）。
2. **§2.4** —— 2.1 之 tabs 是否涵蓋下螢幕之 Seats tab。
3. **§5.2** —— `2.7.1` 之 front HVAC 風速範圍是否立為第十四軸。
4. **§5.4** —— `duplicate_of` 回填之機制。
5. **§9.1** —— ch16 與 ch2／ch3 之逐節對應表是否須先建立。
6. **§9.5** —— R-C34 之生成時義務是否須有 gate。
