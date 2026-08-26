# 下放包 16 —— Vehicle Category：第 14 項修法（乙之精確版 ＋ 常數表擴充）

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`features/vehicle_category/docs/upstream/16_batch1_close.md`
- 前一包：`docs/handoff/15_batch1_tc.md`
- **NN 檢查**：寫入前已 `list_directory`，`docs/handoff/` 止於 `15_`，無碰撞。

---

## 一、上繳包 15 之覆核

**停點正確，且 §4.3 之分析比停點本身更有價值。**

### 1.1 四項具名

1. **§4.3 —— 第 14 項假設了「首步 = setup」。**
   `001-02` 之首步 `Open the Vehicle Category screen` **本身即受測動作**
   （「進入」正是該需求之觸發），不是 setup。
   **這一層我下裁時沒看到** —— 我把第 14 項寫成「首步取自常數表」，
   隱含了一個未經檢驗的假設。
2. **§4.2 之二項不做**（不加常數使其通過、不放寬判準）——
   「由我單方擴充它，等於自己出題自己改答案」。判斷正確。
   常數表是第 14 項之判準來源，擴充它屬 Tier 2。
3. **§5 —— PLAYBOOK §7.1 之 (b) 首次抓到真東西，而且抓到的是真的。**
   「若只做 (a)，本輪會以『22 筆全綠』交出去。」
   下放包 15 §四之擴充於一輪內兌現，且其證據強度自陳
   （本批真實產出 > 跨批複用之 pilot 標的）亦正確。
4. **§1 之 profile 節號不重編** —— 理由（R-VC21 條文與 `verify_batch.py`
   皆以「§5／§6」指涉，重編號會使已落地之條文指錯）成立。
   移回原位而非重編，處置正確。

### 1.2 分析層之獨立內容複核（22 筆）

未採信自評，實測：

| 項 | 結果 |
|---|---|
| 括號下半兩兩不同 | **22/22 相異，重複 0** |
| `012-02` 之下界處置與 §2.6 揭露 | ✅ reasoning 逐字載明三句、第 2 句為下界、取「恰好兩個」之依據 |
| `012-03`／`013-03` 上半取完整句 | ✅ 且 reasoning 載明片段之小寫起首與取整句之理由 |
| `013-02` 之 reasoning | ✅ **載明「037 在句中補了句號並刪去 `and`」** —— 該發現寫進了會被讀到的地方 |
| `011` 之 PENDING 與其理由 | ✅ 含「排序規則本身為需求無疑，故生成而非保留」之 R-VC22 依據 |

**括號下半之品質高於 pilot。** 二例：
`VC-010`「Filtering by vehicle equipment, **not the ordering of what survives**」
與 `VC-011`「**Ordering of the surviving content**」互補且互指；
`VC-001-01`「which tabs exist, **not which one is active**」以否定式
劃清與 `001-02` 之界。**sibling 區分不只做到相異，做到了互相定界。**

---

## 二、第 14 項之修法：**乙之精確版 ＋ 常數表擴充**

三案各自解決不同之問題，非折衷：

| 案 | 所解 | 採否 |
|---|---|---|
| 甲之「首步是否 setup」語意判斷 | 判準適用範圍 | **不採** —— 乙之判準不需要它 |
| **乙（判準改向）** | 判準適用範圍**錯誤** | **採，但改用正規化比對而非編輯距離** |
| **丙（參數化）** | 常數表**表達力不足** | **採，但範圍嚴格受限** |

### 2.1 乙採其方向，不採編輯距離

執行層之判斷正確：**§5.3 所防者為變體擴散，不是位置**。
其原文為「Case, hyphenation, spacing, and wording variants are not allowed
to spread across TCs」—— 規制對象是變體，未要求每個 TC 之首步皆為常數。

**但編輯距離不適合作為判準**：

```
Open the Vehicle Category screen
Open the Vehicle Category screen and select the "Controls" tab
```

二者之編輯距離大（差 34 字元），但其關係是**前綴**，不是變體。
閾值鬆則誤報（前綴被判為近似 → 要求逐字相同 → 又 FAIL）；
閾值緊則漏報。**閾值調不出一個對的位置，因為它量錯了東西** ——
這與 R-G39 對停止條件 87 之判詞同型（母體條數不是批次份量之代理量）。

**改用正規化比對，零閾值**：

```
正規化 = 小寫 + 去標點（含引號）+ 壓縮連續空白 + 去首尾空白

判準：批內任一 Procedure 步驟，其正規化形式若等於某常數之正規化形式，
      而其原字串與該常數**不逐字相同** → FAIL
```

驗算：

| 步驟 | 對 `ENTER_VC_TAB(Controls)` | 判 |
|---|---|---|
| `Open the Vehicle Category screen` | 正規化後**不等**（少後半）| 不觸發 ✅ |
| `open the vehicle category screen and select the "controls" tab` | 正規化後**相等**、逐字不同 | **FAIL** ✅ |
| `Open the Vehicle Category Screen and select the 'Controls' tab` | 同上 | **FAIL** ✅ |
| `Open the Vehicle Category screen and select the "Settings" tab` | 對 Settings 實例正規化後相等且逐字相同 | 不觸發 ✅ |

**偽陰性（須揭露）**：近義詞替換（`Go to the Vehicle Category screen and
select the "Controls" tab`）正規化後不等，**抓不到**。
§5.3 之四類中，case／hyphenation／spacing 全抓得到，**wording 抓不到**。

**配套之軟檢查**：編輯距離落於區間者**列為候選並人工判讀**，
不自動 FAIL。硬檢查零誤報零漏報（就其能抓者），
軟檢查捕捉 wording 但交人工 —— **二者分開，不混為一個有閾值的自動判定**。

### 2.2 丙採其形，範圍受限至一個枚舉參數

`001-03` 之 `... select the "Settings" tab` 與 `ENTER_CONTROLS_TAB`
為同構，僅 tab 名不同。逐 tab 登記獨立常數會隨頁籤數增長
（VC 之頁籤含 Controls／Settings／Specialty 諸名）。

**profile §5 改登記二則：**

```
ENTER_VEHICLE_CATEGORY:
  Open the Vehicle Category screen

ENTER_VC_TAB(<tab>):
  Open the Vehicle Category screen and select the "<tab>" tab
  <tab> 之值域：framework §2 所載之 Test Set 對應頁籤名
                （現為 Controls、Settings；Specialty 諸名待其批次時擴充）
```

原 `ENTER_CONTROLS_TAB` 成為 `ENTER_VC_TAB(Controls)` 之實例，
**其字串不變** —— 22 筆已生成之 TC 不需因此改動。

**凍結語意之調整（profile §5.2(c) 之補充，非重寫）**：

```
帶參數之常數，其**模板**凍結；其**值域**得擴充，但擴充須經裁定並記於 profile。
模板之修改與無參數常數同 —— 須經裁定並回溯既有 TC。
```

**不再擴大參數化**：僅此一個常數帶參數，且參數只有一個、值域為枚舉。
不引入巢狀、不引入條件、不引入預設值 —— 保持其為「一個有洞的字串」，
不使 profile §5 成為 DSL。若日後另有常數需參數化，**須另裁**。

### 2.3 甲之語意判斷不採

「該步驟是否為 setup」之判定，在乙之判準下**不需要** ——
乙不問位置也不問角色，只問「用到常數就不許走樣」。
`001-02` 之首步在乙案下不觸發，**不是因為我們判定它是 test action，
而是因為它根本不是任何常數之變體**。

**這是乙優於甲之關鍵**：它把一個需要語意判斷的問題，
變成一個不需要語意判斷的問題。

---

## 三、一項觀察 —— 不阻斷本批

`011`／`012-03` 之 Procedure 將 PENDING 內嵌為句子成分：

```
3. ... and compare it against PENDING: DR-VC9 Dashboard content table
```

IN §8.4.3 之 `PENDING: DR-{n} <缺件名>` 為**欄位值之佔位**；
內嵌後語法上成為介詞之受詞，讀來像「與『PENDING:…』比較」。

**不阻斷本批**，理由三項：
1. pilot 之 `VC-033-01` 已用同一形態並通過收斂 —— 為本 feature 之既有慣例；
2. 整欄標 PENDING 會使該欄其他可執行步驟一併被讀為待定，**過度**；
3. 內嵌使缺件精確定位到該步，資訊量較整欄標示為高。

**但建議統一其書寫**，納入 profile（與 §5／§6 並列之新節或附於 §6）：

```
PENDING 之內嵌書寫：
  缺件僅影響某一步驟之某個值時，得內嵌於該步驟，
  但須使其可讀為**標註**而非句子成分 —— 建議以獨立子行或括號標示。
  缺件影響整個欄位時，該欄逕填 PENDING 佔位。
```

**此為建議措辭，非本批之收斂條件。** 若採，其適用自第 2 批起，
pilot 與第 1 批不回溯（R-TM13 之精神：既交付者加註不改寫）。

---

## 四、執行層任務

| # | 任務 |
|---|---|
| T90 | profile §5 改登記 §2.2 之二則常數（含值域與凍結語意之補充）。`ENTER_CONTROLS_TAB` 之字串不變，僅其登記形式改為 `ENTER_VC_TAB(Controls)` 之實例 |
| T91 | `verify_batch.py` 之第 14 項改為 §2.1 之正規化比對（硬檢查）＋ 編輯距離候選（軟檢查，列出不自動 FAIL）。**依 PLAYBOOK §7.1 雙向實測**：(a) 反向輸入 —— 以 `Open the Vehicle Category Screen and select the 'Controls' tab` 驗其 FAIL；(b) 已知標的 —— 以本批 22 筆之真實首步驗其**全數不觸發** |
| T92 | 重跑收斂 19 項，**全過始收斂**。任一不過即停 |
| T93 | §三之 PENDING 書寫慣例：**提案**寫入 profile（標明自第 2 批起適用、不回溯），或回報不採之理由 |
| T94 | 第 1 批 a 段標記為已收斂（形式同 T77），b 段 2 筆維持保留 |

**不在本輪範圍**：寫回工作簿、b 段生成、第 2 批。

---

## 五、上繳包要求

1. T90–T94 逐項結果
2. profile §5 修改前後全文
3. 第 14 項之新判準全碼 ＋ 雙向實測輸出
4. 收斂 19 項全輸出
5. 量測條件揭露（R-G8）：正規化比對之偽陰性（wording 變體）須逐字載明

---

> **第 1 批收斂後，第 2 批 `Settings List`（30 leaf）為下一目標。**
> 其規模為本 feature 最大，且含旋鈕／長按速率／指示標退回等
> pilot 與第 1 批皆未驗之互動形態 —— **仍須勘查前置**（R-VC21 末句）。

> 同批 A（六項）、DR-VC3、DR-VC9(一) 之發送仍待 Pei（Tier 3）。
> 九筆 DR 全未結，其中 DR-VC9 直接阻斷 b 段 2 筆。
