# 上繳包 12 —— Vehicle Category：pilot 二項退回之修正（T67–T72）

- 日期：2026-08-26
- 對應下放：`docs/handoff/12_pilot_fix.md`
  （SHA256 `ef0c2ee9b3a78732a92baaa94d831c1e2812113a610be8c3e6dff3f915e89960`，214 行）
- **結論：T67–T72 六項全數完成。`verify_pilot` 15 checked / 0 failed
  （含新增之第 11、12 項）。**
- 未寫回工作簿、未改 lint、未進行任何 git 操作。

---

## 0. 一頁摘要

| # | 任務 | 結果 |
|---|---|---|
| T67 | 12 筆 `pre_conditions` | ✅ 12/12 改為只留 feature initial state；導覽移入 Procedure 首步 |
| T68 | `VC-028-02` 第 3 步 | ✅ 門檻參照移除；N = 10 標為測試設計參數 |
| T69 | 第 11、12 項 | ✅ 新增，**皆以反向輸入實測會 FAIL** |
| T70 | 重跑 | ✅ **15 checked / 0 failed** |
| T71 | A-VC14 加註 | ✅ 原文未改（R-TM13）|
| T72 | 二項退回之登記 | ✅ **A-VC16**，不立新條 |

**二項退回我全部接受，沒有異議。** 它們是實錯，且是我自己的檢查器
看不到的那一類 —— 理由見 §5。

---

## 1. T67 —— `pre_conditions` 之修正

### 1.1 逐筆對照（12 筆）

**修改前（12 筆完全相同之第 1 條）**：

```
1. The head unit is powered on and the Vehicle Category screen is displayed
   with the "Controls" tab active
```

**修改後**：

| leaf | 修改後之 `pre_conditions` |
|---|---|
| `026-01`／`026-02`／`026-03`／`027`／`028-01`／`028-02`／`029`（七筆）| `1. The Glove Box feature is not activated` |
| `030`／`031`／`032`／`033-01`／`033-02`（五筆）| `1. The Glove Box feature is activated with a known 4-digit PIN` |

原第 2 條升為第 1 條，內容未動 —— 其為 §4.4 允許之
**feature initial state**，且 `4-digit` 為 spec-sourced（`VC-033-02`）。

### 1.2 導覽移入 Procedure 首步

12 筆之 Procedure 前置一步（§5.2 A 類，動作＋標的）：

```
1. Open the Vehicle Category screen and select the "Controls" tab
```

對應之 ER 第 1 項：

```
1. The Vehicle Category screen is displayed with the "Controls" tab active
```

**步數變化（Procedure ↔ ER 維持 1:1）**：

| leaf | Procedure | ER |
|---|---|---|
| `026-01`／`026-02`／`027`／`028-01`／`030`／`031`／`032`／`033-02` | 2 → **3** | 2 → **3** |
| `026-03`／`028-02`／`029`／`033-01` | 3 → **4** | 3 → **4** |

**既有首步之驗證語意未改** —— 原「Press "Glove Box" in the "Controls"
list…」逐字保留，只是位置後移一格。

### 1.3 §8.5 之決策測試

`head unit is powered on` 為「測試得以執行所需之隱含環境穩定前提」，
非本 TC 直接驗證之觸發條件 → **drop**，未移入 Procedure。
只有後半（導覽至 Controls）被移入，因其為步驟可達成之狀態。

---

## 2. T68 —— `VC-028-02` 之門檻參照

### 2.1 Procedure 對照

**修改前**：

```
3. Continue the mismatch cycle beyond the point at which a comparable attempt
   ceiling would apply, and record whether the flow stays available
```

**修改後**（含 §1.2 之首步前置，故編號為 3、4）：

```
3. Enter a value other than 1234 on the second keypad popup and dismiss the
   warning popup
4. Repeat the mismatch cycle until ten consecutive incorrect entries have been
   made, and record whether the keypad popup is still reachable
```

> 附帶收拾一處：修正後原第 3 步之「repeat this mismatch cycle multiple
> times」與新末步之重複語意重疊，故將其收為**單次不符**，
> 重複一律由末步承擔。此非下放包所指，是修改過程中自己冒出來的鬆散，
> 一併緊實。

### 2.2 ER 對照

| # | 修改前 | 修改後 |
|---|---|---|
| 3 | Each mismatch is answered by the warning popup and the keypad popup remains reachable | The mismatch is answered by the warning popup and the keypad popup remains reachable |
| 4 | The activation flow stays available with no attempt ceiling applied and no lockout imposed | The activation flow stays available **after ten consecutive incorrect entries**, with no attempt ceiling applied and no lockout imposed |

`no attempt ceiling applied` **保留**（下放包 §3.3(b)）——
該句為行為表述，未引入門檻值。

### 2.3 `reasoning` 之新增段

```
⚠ 測試設計參數（下放包 12 §3.2）：本步驟之重複次數 N = 10 為測試設計選擇，
規格未給上限值。037 之 `There's not a limit for the incorrect input.` 為
否定性存在命題 —— 無法以有限次數證明，測試至多做到「重複 N 次仍可用」。
N 之正當性來自其被明確標示為測試設計，非被偽裝成規格值；
此與 §8.4.1 所禁之「發明來源未述之規格值」不同類。
前一版之 `a comparable attempt ceiling` 已移除 —— 該參照指向 -033-01 之
停用門檻（正由 DR-VC8 爭議），既造了一個規格未述之參照對象，
又使本筆之可執行性隱性繫於他筆之未定值。
```

§3.2 之區分我照收：**N 是測試設計參數，不是規格值**，
其正當性來自被標示，而非被偽裝。

---

## 3. T71 —— A-VC14 之加註

原文未改（R-TM13），於狀態行前加註：

> **二欄之數字同為 `three`，差別在比較器。**
> `After three sequential wrong PINs` —— 觸發於第 3 次
> `more than three times in sequence` —— 觸發於第 4 次
>
> 即：**只比數字會漏掉這個矛盾**（二者皆為 3）。
> T52 之掃描器初版正是因此而漏抓本案 —— 它比的是 (類別, 值)，
> 比較器是後來才加入判準的。

條文之 (a)(b)(c) 三項拘束不受影響。

---

## 4. T69／T70 —— 新增二項檢查與重跑

### 4.1 全輸出（15 checked / 0 failed）

```
  1  12 筆 JSON 完整，10 個必要 key 齊備（IN §10.1）                      PASS
  2  IN §9 十七項自檢（機械化子項見第 3–8、11、12 項；全項見上繳包）              PASS
 11  pre_conditions 無 §4.4 三類禁項（system defaults／premise／step-controlled） PASS
     default 0；premise 0；step_overlap 0
 12  無對他筆之值的隱性依賴（comparable/corresponding/... ＋ 門檻類名詞）        PASS
     命中 0 處 無
  3  test_item 括號下半 12 筆兩兩不同（機械）                               PASS
 3b  test_item 括號下半無中文（R-S4）                                   PASS
  4  specification_reference 12 筆與 recon_leaf_to_section.tsv 逐字相符  PASS
  5  priority 12 筆與 priority_final.tsv 逐字相符                      PASS
  6  Test Set 12 筆皆為 `Glove Box`，Test Group 皆為 `Vehicle Category` PASS
  7  尾句號／方括號／單引號／行首尾空白（IN §11，作者欄位）                        PASS
 7b  test_item 上半保留之來源記法對得上其來源列（R-VC19(c)）                  PASS
  8  `VC-033-01` 帶且僅帶一處 PENDING，字串逐字相符                        PASS
  9  `028-02`／`033-01` 之括號下半明載其流程                            PASS
 10  `VC-021` 之委派載於全部 12 筆之 reasoning（§8.2.1）                PASS
  A  Procedure ≥2 步 ∧ Procedure↔ER 1:1 ∧ ER 無 modal ∧ 無 observe/verify 起首 PASS
15 checked / 0 failed
```

（下放包 §五之「十二項」為原十項 + 新二項；本腳本另有 3b／7b／A
三項子檢查，故顯示 15。）

### 4.2 ⚠ 二項新檢查已**實測**其會 FAIL，非僅宣稱

§四.2 要求「每項判準須載明其反例」。本輪更進一步：
**把反例真的塞進 JSON 跑一次**，確認檢查器會抓到。

注入三處：`026-01` 之 PC 加 `The head unit is powered on`；
`026-02` 之 PC 改為 `The "Controls" tab is active`；
`026-03` 之 Procedure 加 `a comparable attempt threshold`。

```
 11  pre_conditions 無 §4.4 三類禁項  **FAIL**
 12  無對他筆之值的隱性依賴          **FAIL**
exit: 1
```

**二項皆如預期 FAIL。** 隨後還原 JSON，複跑回到 15/0。

> 這一步是針對上繳包 11 §5.3 之自我限定（「寫檢查器與寫被檢查物者同一」）
> 之實際處置：**光寫反例還是我自己說了算，跑一次才知道判準真的接得住。**

### 4.3 三項新判準之反例（文件層）

| # | 應 FAIL 之輸入 |
|---|---|
| 11 · system defaults | `The head unit is powered on`／`HU is booted`／`Ignition is ON`（非該 TC 直接驗證之觸發條件時）|
| 11 · premise | `Glove Box is accessible`／`Glove Box feature is available` |
| 11 · step-controlled | `The "Controls" tab is active`／`The PIN popup is displayed` |
| 12 | `beyond a comparable attempt ceiling`／`the corresponding lockout duration` |

---

## 5. 我接受二項退回，並記其形態

### 5.1 這二件與前三件方向相反

| 件 | 形態 | 誰抓到 |
|---|---|---|
| T52 初版類別切分 | 太嚴 → 漏抓（分類過細）| 我自己 |
| modal 未排除引號 | 太嚴 → 誤報 | 我自己 |
| ER 快掃未排除序號 | 太嚴 → 誤報 | 我自己 |
| **§4.4 只驗一類** | **太鬆 → 漏檢 12/12** | **分析層複核** |
| **隱性依賴他筆之值** | **看不到 → 漏檢** | **分析層複核** |

**前三件我自己抓得到，後二件我抓不到。** 差別不在難度，在方向：
太嚴的判準會 FAIL，FAIL 會逼我去看；太鬆的判準會 PASS，
而 PASS 不會逼任何人做任何事。

### 5.2 §4.4 那一項，我的判讀本身就寫得太滿

上繳包 10 §4 第 3 項我寫：

> 人工：二式（未啟用／已啟用且 PIN 已知）＋ 進入畫面；**未寫**「Glove Box is accessible」

「未寫 Glove Box is accessible」是真的，但那只是三類禁項中的一類。
**那句話讀起來像驗過了整條 §4.4**，實際只驗了三分之一 ——
而且我還把它列在「PASS」欄裡。

這與 REV-13（「本組無 PENDING」之涵蓋範圍小於字面）是同一個毛病：
**把一個窄的檢查，用一個寬的詞報出去。**

登記為 A-VC16（**不立新條** —— §4.4 已明文，缺的是檢查覆蓋）。

---

## 6. 未結清單

**DR 八筆全未結**（DR-VC1 ~ DR-VC8）。同批 A 五項。
**A 十一筆未結**：A-VC2、A-VC3、A-VC4、A-VC8、A-VC9、A-VC10、A-VC11、
A-VC12、A-VC13（通則）、A-VC14、A-VC15。
已結五筆：A-VC1（撤銷）、A-VC5／A-VC6／A-VC7、**A-VC16**（RESOLVED）。

---

## 7. 待你裁

1. **pilot 是否放行** —— 十二項（實跑 15 項）全過。
2. 同批 A（五項）與 DR-VC3 之發送（Tier 3）。

---

## 8. 量測條件揭露（R-G8）

### §4.4 第三類（step-controlled state）之偽陰性

下放包 §四.1 明言該類「最難機械化」，其可機械化之近似為
「與 procedure 步驟之標的重疊」。我實作為：
**該 `pre_condition` 與該筆 `test_procedure` 是否共用一個 `"..."` 引號標的**。

**偽陰性（抓不到者）**：

1. **不含引號標的之 step-controlled 狀態** ——
   `The keypad is showing`、`The user has entered the flow`
   無 `"..."` 可比對，零命中。
2. **標的名稱不同而實為同一狀態** ——
   PC 寫 `The confirmation dialog is open`、Procedure 寫
   `Press "OK" in the confirmation popup`，`dialog` 與 `popup` 不重疊。
3. **跨筆之 step-controlled** —— PC 所述之狀態由**他筆**之步驟達成，
   本筆 Procedure 內無對應標的。

**故第 11 項之第三類為「近似」而非「判定」**，
其 PASS 應讀作「以引號標的重疊為準未發現」，非「已證明無 step-controlled」。
前二類（system defaults／premise）為詞表比對，同受詞表涵蓋範圍所限。

### 第 12 項

詞表為 `comparable`／`corresponding`／`similar`／`equivalent`
＋ 門檻類名詞（`ceiling`／`threshold`／`limit`／`count`／`timeout`／
`duration`／`interval`）之鄰接。
**偽陰性**：以其他措辭表達之跨筆參照 —— 如
`the same number of attempts as the deactivation flow`（無詞表命中）、
或以代名詞指涉（`that limit`）。**語意層之參照，機械掃描抓不到。**
