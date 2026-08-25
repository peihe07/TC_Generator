# 下放包 21 —— pilot-01 覆核：四項退回、負向補列

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`docs/upstream/21_pilot01_rev2.md`
- **本包對交付物之推進：pilot-01 修訂版（含負向／邊界條）**（R-G31）
- **前置（已查證）**：上繳包 20 已回；`generated/pilot-01.json` 三條、
  lint 二十項行計 0；R-DM47/48 抄錄 2/2；DR-DM9 已開

---

## 一、上繳包 20 之覆核 —— 產出合格，四項退回

**首批 TC 產出，`lint036.py` 二十項行計 0，五十二條停止條件全未觸發。**
lint 之處理（拋棄式副本、母本 SHA 前後未變）正確且必要，記明。

首跑 A 檢查 4 處 FAIL 之處置尤其正確：`Observe`／`check whether` 是
§5.1 之禁用主動詞，執行層**改 TC 而非放寬判準**，並自陳
「該 FAIL 是我產出之缺陷，不是判準問題」。

§7 之負向路徑自陳亦記明 ——

> 下放包之三條清單看起來完整，而 §9 之檢查表問的是另一個問題。
> 兩者都照做，才會發現只照做其一是不夠的。

**下放包之 §二.1 明寫「下限，非上限」，而我沒有列負向。** 該缺口
是我的，不是執行層漏做。

以下四項為分析層覆核所見，**退回修訂**。

---

## 二、退回項

### 2.1 【最重要】#1 與 #2 之觸發條件相同 —— False Pass 風險

| | #1（004） | #2（005） |
|---|---|---|
| Pre-Condition | non-Hot | Hot |
| Procedure step 1 | Raise … above 85 degrees C | Keep … above 85 degrees C |
| ER | 亮度降低 ＋ PU0517 | 背光關閉、觸控停用 ＋ PU0130 |

**兩條之溫度條件相同（> 85），而結果不同。** 現行 TC 中沒有任何
可執行之條件能讓測試員知道「何時應看到亮度降低」與「何時應看到
背光關閉」——照 #2 之步驟執行，在剛越過門檻的瞬間讀 popup，
讀到的會是 PU0517 而非 PU0130，**而 TC 會判 fail**（False Fail）；
反之若系統從未進入關閉階段而測試員等得夠久，也無從分辨。

`PU0130` 之 Description 逐字為
`the display will turn off until it has cooled`，
`Exit Conditions` 為 `Timeout or when display turns off` ——
**兩處都指向一個「持續未冷卻」之時間或再判定條件，而該條件之值
不在現行三條之任一欄位內。**

**處置（不得自行補值，§8.4.1）**：

1. 回 CFTS_020 `{4820281}` 節（含 `{4820282}`／`{4820289}`／`{4820290}`）
   **逐字查**：warning 階段與 OFF 階段之間的區分條件為何
   —— 時間？再量測？第二門檻？
2. **查得** → 寫入 #2 之 Pre-Condition 或 Procedure（依其為狀態或動作），
   並於 #1 之 Pre-Condition 補其對應之區分（使兩條互斥）
3. **查無**（含「該區分條件轉指 `{CFTS013-*}`」之情形）→
   **#2 deferred，開 DR-DM10**，理由記為「warning 與 OFF 兩階段之
   區分條件不在受裁來源內」。#2 不得以現狀交付
4. 若查得之區分條件即為 DR-DM4 所指之 multi-stage 分級 →
   #2 併入該 deferred，**不另開 DR**

> 這一項是 §7（False Pass／False Fail）與 §8.7.2（語意相近之操作
> 須於 ER 區辨其終態）之交集。ER 已區辨終態（亮度 vs 背光），
> **但觸發側未區辨** —— 區辨只做了一半。

### 2.2 門檻值之欄位歸屬 —— §8.7.1 vs §4.5

現行三條：`input_test_data` 載門檻值，`test_procedure` 又重述
`above 85 degrees C`，而 `pre_conditions` 只寫 `non-Hot state`／
`Hot state` 之**狀態名**，無具體值。

canon 兩條之要求：

- **§8.7.1**：每一個觸發／釋放門檻**須以具體值出現於 Pre-Condition**，
  不得以模糊語（`in motion`、`approximately`）代之
- **§4.5 SWC 基準**：資料應內聯至 Pre-Condition 或 Procedure 使步驟自足；
  `Input Test Data` **以 `NA` 為常態**（SWC 0708 實測 285/286）

**裁定**：門檻值移入 `pre_conditions` 之具體值形態，
`input_test_data` 改 **`NA`**。Procedure 之操作值保留
（步驟須可執行，非欄位歸屬之重複）。

修正形態（示意，實際文字依 CFTS 原文）：

```
pre_conditions:
1. The DCSD display temperature is 85 degrees C or below (non-Hot state)
2. No high priority screen (RVC) is active

input_test_data: NA
```

三條皆須改。**#3 之 `deg C` 寫法依 R-DM48 之單位處置維持不統一**
（各依其所引 ObjectID 之原文）。

### 2.3 `CFTS020-4820282` 之內容須複驗

#1 之 `specification_reference` 列 `CFTS020-4820282`。
而 `DATA_REQUESTS.md` §R-DM8 再判定載：
**`{4820282}` 亦轉指 `{CFTS013-629}`** —— 即該條號是 multi-stage
之外部指標。

**若 `{4820282}` 之內容為 multi-stage 之轉指而非 warning 階段之
需求本體，則 #1 引用它即為引入 deferred 之內容**（停止條件 47）。

處置：逐字取 `{4820282}` 之全文入上繳包，判其是否為 #1 所直接驗證
之節（§10.7 之要求為「TC 直接驗證之每一節」）。
**不是** → 自 #1 之 `specification_reference` 移除。

### 2.4 負向／邊界條 —— 補列（§9 第 11 項、§8.3）

執行層自陳未涵蓋負向，判定正確且應補。

**補列 #4**（leaf `SWE1-DM-004`）：邊界 —— 溫度等於門檻時**不**觸發。

- §8.3 之 boundary 軸：`=limit`、`limit±1`
- `{4820290}` 之 `<= 85 deg C` 為 non-Hot 之定義 ——
  即 **85 恰好屬 non-Hot**，此為 spec 明載，非推論
- ER：無 popup 顯示、亮度未降低、
  `$DIS_CENTERSTACK.DCSD_DISP_STAT$` **不為** `4 (DISP_HOT)`

> `DISP_HOT` 之**否定**可寫，因其為逐字解得之標籤；
> 但**不得**寫「應為 `0 (OFF)`」或「應為 `1 (ON)`」—— 那需要
> DR-DM9 之答案（R-DM48）。

`design_method` 依 §12 於 procedure 定稿後指派
（預期 `邊界值分析`，以自檢為準）。

---

## 三、不退回但須記明者

| 項 | 判定 |
|---|---|
| `design_method` 用中英並列（`狀態轉換 (State Transition Testing)`） | **不退回** —— 036 母本之 `design_method` 詞彙為既定清單，lint K（CJK）已校準且行計 0。此為工作簿詞彙非自由文字，§1「English only」不及於受控詞彙 |
| #3 之 baseline（step 1 先讀背光並記錄） | **正確**，§5.6 之形態符合（記錄步驟不用 `baseline` 一詞，比較留於 ER） |
| popup 歸屬之逐字依據 | **正確**，兩者 Description 與 Exit Conditions 皆逐字相異，非因同為 `1T` 而假定 |
| Priority 三條皆 P1 且說明為何非 P0 | **正確**，且其理由引 R-DM46 之實測（ASIL 31/31 QM）而非泛稱 |
| `PU0008` 之排除 | **正確**，已記為 §8.2.1 委派 |

---

## 四、作業步驟

1. **§2.1 之查證**：逐字取 `{4820281}` 節全文（含其下各 ObjectID），
   判 warning 與 OFF 兩階段之區分條件。依 §2.1 之四分支處置。
   **查證結果先於修訂** —— 若落入分支 3／4，#2 不修訂而改 deferred。
2. **§2.3 之複驗**：逐字取 `{4820282}` 全文，判其是否為 #1 直接驗證之節。
3. **§2.2 之欄位歸屬修正**：三條（或修訂後之條數）全數施行。
4. **§2.4 之 #4 補列**。
5. 重跑逐條 §9 自檢十七項與 `lint036.py`（**整批**，附母體行數）。
6. `batch_context.md` 更新；`DATA_REQUESTS.md` 依 §2.1 之結果處置。
7. 更新 `docs/INDEX.md`。

**仍不寫回 036 母本。**

---

## 五、停止條件

沿用 1–52，另加：

53. §2.1 之查證若得「區分條件存在但其值不在受裁來源內」→
    #2 deferred 並開 DR-DM10，**不得以推定之時間值補寫**（§8.4.1）。
54. #4 之 ER 若寫入任一未逐字解得 DBC `VAL_` 之值（含 `0 (OFF)`／
    `1 (ON)`）→ 停（R-DM48）。
55. §2.2 修正後若 `pre_conditions` 出現非狀態之內容（動作、檢查）→
    停（§4.4）。

**全部 git 操作屬 Pei。**

---

## 六、上繳包要求（`docs/upstream/21_pilot01_rev2.md`）

1. `{4820281}` 節與 `{4820282}` 之逐字全文，及其判定
2. §2.1 之處置（修訂／deferred／併入 DR-DM4，擇一並記理由）
3. 修訂後之 TC 全文（含 #4）
4. 逐條 §9 自檢十七項
5. `lint036.py` 全文輸出（整批，附母體）
6. 未驗項分流（A／B，R-G29）
7. 建議之 commit 訊息與 pathspec（不執行）
