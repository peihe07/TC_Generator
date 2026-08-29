# 上繳包 37 —— T55 執行結果（下放包 42）

- 日期：2026-08-29｜方向：執行層 → 分析層
- 對應下放包：`42_rov_a.md`
- **⚠ lint 非全 0：`F=2`** —— 訊號記法之方括號與 F 檢查衝突，見 §2.2
- **T55a 之查表：三類，其中一類是上游未指派** —— §1

---

## 1. T55a —— `PU` 編號之查表（**本輪核心**）

對 `inputs/Pop Up List HMI R1 (26PI).xlsx`（3 分頁，`Main` 為主表，
表頭 `ID Number｜Module｜Timeout｜Exit Conditions｜Description｜Category｜String/Popup Message｜Template`）逐格掃描。

**結果分三類，其處置各不相同：**

### 1.1 ✅ 在案且可引（**2 個，皆本組所需**）

| `PU` | Module | Description（逐字） | 引用之 037 列 |
|---|---|---|---|
| **`PU0303`** | FOTA | `Shown after a successful update.` | **`088`** |
| **`PU0416`** | FOTA | `Displayed when the software update is complete.` | **`095`** |

`PU0303` 之 `String/Popup Message` 載其實際文字
（`Software Update <X> / Your Uconnect System has been updated with the latest
Software. / <OK> / <What's New?>`），**其 Exit Conditions 為 `<OK> <What's New?> <X>`**
—— **`088` 之 TC 得逕引該彈窗，且其按鈕名有來源。**

### 1.2 ⚠ **上游未指派之佔位（`PUXXX1`／`PUXXX3`）—— 與 A-SU3 不同型**

`104`／`105` 引 `PUXXX3`、`106` 引 `PUxxx1`（**037 側大小寫不一致**）。

**實測其於彈窗清單之狀態**：

> **二者皆非任何一列之 `ID Number`** ——
> 其**只出現於他列 `Description` 欄之敘述文字中**，如：
> `When TBM Update is available … show TBM Update Popup (**PUXXX1**).`
> `If Radio ON and Update installation has not been completed yet, then show
> TBM Ongoing Update Popup (**PUXXX3**).`
> 另見 `PUXXX2`（TBM Forced Update Popup）、`PUXXX1 b`／`PUXXX3 b`（背景全黑之變體）。

**即：`XXX` 是佔位符，二側皆未指派。**

> ### **與 A-SU3 之別，須分清**
>
> **A-SU3**：PDF 之 `PU971`（3 位）於清單查無 —— **裁為原文筆誤，作 `PU0971`**。
> **其為一個已存在之彈窗被寫錯編號。**
>
> **本項**：`PUXXX1`／`PUXXX3` 於**二側皆為佔位** ——
> **其為一個尚未被指派編號之彈窗**。
> **不可比照 A-SU3 推定其正解** —— 沒有正解可推。

**故 `104`／`105`／`106` 三列之 TC**：其彈窗**無編號可引**，
其 ER 只能以彈窗之**功能描述**指稱（如 `the TBM ongoing update pop-up`）。
**是否可接受，屬分析層之裁定** —— 執行層列此供裁，**本輪未起草該三列**。

### 1.3 `PU0410` —— 在案，惟**不屬本組**

`PU0410`（FOTA，Exit Conditions `<X>`）在案，
**但 ROV 20 列之 Description 中無一引用它** ——
其於 `feature.yaml` 之 `popup_ids`（51 個）內，來源為 037 全欄與 PDF 之聯集。
**T55a 將其與本組所需者並列，係下放包之誤（不影響任何 TC）。**

---

## 2. T55b —— ROV-A 產出與 lint

| 列 | TC ID | 037 | 錨 | P | `PENDING` | 型 |
|---|---|---|---|---|---:|---|
| 10 | `newR1L-SU-028` | `090` | `4907909` | P2 | 0 | 可寫 |
| 11 | `newR1L-SU-029` | `092` | `4907898` | P1 | 0 | 可寫 |
| 12 | `newR1L-SU-030` | `093` | `4907901` | P1 | **3** | **第四型** |
| 13 | `newR1L-SU-031` | `094` | `4907902` | P1 | **3** | **第四型** |

四份 `test_item` 上半**皆實測逐字見於 037**（含彎引號與 `( $FOTA_Status$ = […])` 之不規則空格）。

### 2.1 lint 全輸出（逐字）

```
python3 scripts/lint036.py <rov_a 之簿> --profile sw_update
  行計 A=0  B=0  C=0  D=0  E=0  **F=2**  G=0  H=0  I=0  I-sibling=0  J=0
       K=0  L=0  M=0  N=0  P=0  Q=0  R=0  T=0  U=6  V=0  I-cross=4   exit 0
```

| 項 | §四 之預期 | 實測 | |
|---|---|---|:--:|
| U | 6 | **6** | ✅ |
| `I-cross` | 「實報」 | **4** | 見 §2.3 |
| 其餘 | 全 0 | **F=2**，餘 19 項全 0 | ❌ |

### 2.2 ⚠ **`F=2` —— 訊號記法之方括號被判為未填佔位**

```
| 10 | newR1L-SU-028 | proc | 方括號佔位 '[Successful FOTA Update]' |
| 11 | newR1L-SU-029 | proc | 方括號佔位 '[Installing FOTA Update]' |
```

**F 之判準**（`lint036.py:87`）：`RE_F = re.compile(r"\[[A-Za-z][^\]]{0,30}\]")`
—— **`proc` 中任何 `[Word…]` 皆判為未填佔位。**

而下放包 42 §三令「訊號記法**依來源逐字**（`$FOTA_Status$ = [值]`）」——
**該記法之值一律以方括號包覆，故必然觸發 F。**

> ### ⚠ **一項更要緊者：P 檢查對此記法是沉默的，不是通過的**
>
> P v3 之二式：
> ```
> RE_P3_DOLLAR_ASSIGN  \$[A-Z][A-Z0-9_]{2,}\.[A-Za-z][A-Za-z0-9_]*\$\s*=\s*…
> RE_P3_BARE_ASSIGN    (?<!\$)\b[A-Z][A-Z0-9_]{2,}\.[A-Za-z][A-Za-z0-9_]*\s*=
> ```
> **二者皆要求訊號名含一個點**（`$<MSG>.<Sig>$`）。
> 而 037 寫的是 **`$FOTA_Status$`（無點）** ——
> **P 根本沒把它認成訊號，故 `P=0` 是沉默不是核可**（PLAYBOOK (30)）。
>
> **於是同一個字串**：**P 看不見它，F 把它當成未填的佔位。**
> **無任何檢查在確認它是一個合法之訊號寫法。**

**執行層未改 TC**（其為下放包所定之整列全文，且訊號記法有 R-1 v3(d) 之依據）。
**待裁三選一**：

- **(甲)** F 之判準加一例外：`$<name>$ = [值]` 形態不判 —— **改共用腳本，影響他 feature**；
- **(乙)** 本 feature 之訊號改寫為不帶方括號 —— **違「依來源逐字」**；
- **(丙)** 接受 `F=2` 並逐包揭露 —— **惟 F 之語意（未填佔位）與事實相反，
  交付時審閱者會據此要求補填**。

**執行層傾向 (甲)**，因 (丙) 之代價落在交付時，而 (乙) 動的是來源逐字性。

### 2.3 `I-cross=4` —— **四列全為半窗，`029` 之 `until` 不被認得**

下放包 §四 預期「`028` 無 `until`、`029` 有」。**實測四列皆為半窗。**

成因：`IX_END` 之詞表只有二個片語 ——
`until the software version changes`／`until the update finishes`。
而 `029` 寫的是 **`until the installation ends`**，**二者皆不匹配**。

> **這張表是寫死的，每進一個新 Test Set 就會落後一次** ——
> 而它落後的方式是**靜默地把該列算成半窗**（PLAYBOOK (41) 之同族）。
> `Silent Update` 之收尾語是「版本改變／更新結束」，
> `ROV Installation` 是「安裝結束」，下一組會是別的。

已入 `BACKLOG.md` **B-9**。

---

## 3. T55e —— `ROV Installation` 餘 16 列之三軸盤點

| 037 | 標題 | Sub | 105 | **觸發面** | `PU` |
|---|---|---|:--:|---|---|
| `088` | Display Success Pop-up in Body ON Mo | HMI | — | 須真實更新成功 | `PU0303` |
| `089` | Enforce Vehicle Motion Lockout for R | Service | — | 測試者可直接造成（車輛模式／動作） | — |
| `095` | Display Software Update Complete Pop | HMI | — | 須真實更新成功 | `PU0416` |
| `097` | Display Forced Update Available A Po | HMI | — | 測試者可直接造成 | — |
| `098` | Dismiss Active Pop-up on Standby/Sle | HMI | — | 測試者可直接造成 | — |
| `099` | Handle “Update Now” Selection for RO | Service | — | 測試者可直接造成 | — |
| `100` | Handle Timeout or Cancel Action for  | HMI | — | 測試者可直接造成 | — |
| `101` | Allow Cancel or Ignore Action for Fo | HMI | — | 測試者可直接造成 | — |
| `102` | Force Update Scheduling When Delay I | HMI | — | 測試者可直接造成 | — |
| `103` | Launch Schedule Update HMI for ROV F | Service | — | 測試者可直接造成 | — |
| `104` | Display BEV/PHEV Schedule Update Pop | HMI | — | 測試者可直接造成 | `PUXXX3` |
| `105` | Display Schedule Update Pop-up for S | HMI | — | 測試者可直接造成 | `PUXXX3` |
| `106` | Display “Conditions Not Met” Pop-up  | HMI | — | 測試者可直接造成 | `PUxxx1` |
| `107` | Calculate and Report Remaining Time  | Service | — | 測試者可直接造成 | — |
| `108` | Display No Connectivity Pop-up for R | HMI | — | 測試者可直接造成 | — |
| `109` | Interrupt Pre-Installation Flow on S | HMI | — | 測試者可直接造成 | — |

**觸發面之分佈（餘 16 列）**：
- 測試者可直接造成：**13** 列
- 須真實更新成功：**2** 列
- 測試者可直接造成（車輛模式／動作）：**1** 列

### 3.1 三軸讀法

- **可觀測性**：**16 列全部非 105 列**（全組 105 = 0）—— 本軸無風險
- **錨定確定性**：**GT 涵蓋 0 列**（全組）—— **本軸為全批之風險所在**
- **觸發可行性**：**13 列可由測試者直接造成**，2 列須真實更新成功（`088`／`095`），
  1 列須車輛動作（`089`）

**故餘 16 列之分包建議**：**先做 13 列可直接觸發者**（其三軸皆無阻），
`088`／`095` 次之（其彈窗已在案，觸發須一次成功更新），
**`104`／`105`／`106` 最後**（待 §1.2 之裁定）。

### 3.2 一項與 ROV-A 之對照

ROV-A 四列中有 **2 列（50%）** 為第四型；
**餘 16 列中僅 2 列（12.5%）須真實更新成功、0 列須失敗**。

**即：ROV-A 這一批把本組最難觸發的兩列先做了。**
其為分析層之選樣，**而該選樣使「第四型」之比率於本組被前置放大** ——
**餘 16 列之實際難度低於 ROV-A 所呈現者。**

---

## 4. T55c —— DR-SU2(d) 第四型段增列

**2 列 → 4 列**：`315`／`318`（socket 注入／事故訊號）＋ **`093`／`094`（使更新失敗之手段）**。

DR 文本 §3.5 增二列，並明寫其與 `315`／`318` 同形：

> These two are the same shape as `315`/`318`: **we know what to look for, we cannot
> bring it about.** Note that the two need to be distinguishable from each other —
> one requires the rollback to succeed, the other requires it not to.

**末句為執行層所加**：`093` 與 `094` 之區別在於**回退是否成功**，
若上游只給「使更新失敗」之單一手段而不能控制回退之成敗，**二列仍不可分**。

---

## 5. T55d —— `DELIVERY_CHECKLIST.md` 建檔

**只建檔列項，未執行任一項。** 首三項依下放包 42 §五；**另自增五項**供追認或刪除：

| # | 項 | 狀態 |
|---|---|---|
| D-1 | `REASONING.md` 是否併入 `AH Remarks` | 未裁 |
| D-2 | `PENDING` 全數結案或經 Pei 降轉 `NA`（現 **43 行**） | 未達成 |
| D-3 | `C` 欄留空之理由須隨交付說明 | 未辦 |
| **D-4** | `TRACE_MERGE.md` 是否隨交付附上（Tier 3） | 未裁 |
| **D-5** | `ERROR_CODES.md` 之 `Test Set 候選`為**階段級代理**須明記其粒度 | 未辦 |
| **D-6** | 037 之標點／拼寫／彎引號皆逐字保留，**須列明否則會被當成我方打錯** | 未辦 |
| **D-7** | `I-cross` 之覆蓋率須隨 lint 陳述 | 未辦 |
| **D-8** | `005` 之規格自身抵觸須隨交付揭露 | 未辦 |

檔首明記其與 `BACKLOG.md` 之別：**BACKLOG 多數不需動作，本檔未答即不得交付**；
且 **D-2 之外，其餘七項皆不需上游即可完成**。

---

## 6. 未結 DR 清單（**5 筆**）

| DR | 阻斷 | Urgency |
|---|---|---|
| **DR-SU1** | `001`／`002`／`003`；`005` 待釐清 | **High** |
| DR-SU2 v3 | (d) 第四型 **4 列**（`315`／`318`／`093`／`094`） | High |
| DR-SU3 | `017` | Medium |
| **DR-SU4** | `011`–`016` | **High** |
| DR-SU5 | `021` ＋ `131` s4 | Medium |

**全案 `PENDING` 43 行**（pilot06 5 ＋ batch01 8 ＋ batch02a 21 ＋ batch03 3 ＋ rov_a 6）。
**可交付候選 14 列**（12 ＋ `028`／`029`），與 §四 相符。

---

## 7. 獨立自評（入 BACKLOG）—— §六-6：`$FOTA_Status$` 是否為不可觀測之限定條件

**答：是，而且它比題目所設想的更廣 —— 四列裡有三列都踩到，不只 TC-29。**

**(甲) 先確認其不可觀測。** `$FOTA_Status$` 為 CarPropertyManager 之車輛屬性
（`feature.yaml` 之 DBC 註記：三個 `$FOTA_MASTER.*$` 形態皆經 vehicle property 介面，
非 CAN frame）。**測試者於台架上看不到它** —— 除非另有診斷工具，而該工具未載於任何素材。

**(乙) 但它在四列中之角色不同，須分開判。**

| TC | 出現處 | 角色 | 判 |
|---|---|---|---|
| `028` | **proc 1**：`wait until $FOTA_Status$ = [Successful FOTA Update]` | **等待條件** —— 測試者須據此決定何時進行下一步 | **不可執行** |
| `028` | **ER 1**：`… is reported` | 判定對象 | **不可觀測** |
| `029` | **proc 3**：`while $FOTA_Status$ = [Installing FOTA Update]` | 限定條件 | **不可觀測**（題目所問） |
| `030`／`031` | **ER 2** | **已掛 `PENDING`** | 不受影響 |

**(丙) 故 `028` 之情形比 `029` 嚴重，而題目沒問到它。**
`029` 之該子句是**限定**（拿掉後 ER 3 仍可判：錄影中有無安裝進度畫面）；
**`028` 之 proc 1 是一個等待條件 —— 拿掉之後測試者不知道何時該切 Body OFF。**
且其 ER 1 直接以該屬性為判定對象。

**(丁) 改寫之方向（不裁，執行層不擅改）**：
其外部可觀測之對應物為**更新完成之表徵** ——
`088`（`PU0303`「Shown after a successful update」）與
`095`（`PU0416`「Displayed when the software update is complete」）
**二個彈窗皆為「更新成功」之可觀測表徵，且其編號已在案**（§1.1）。

**故 `028` 之 proc 1 可改為「等待至更新完成之彈窗出現」** ——
**其來源為彈窗清單，不是推想。**
`029` 之限定子句同理可改以「安裝進度畫面顯示期間」表述（該畫面即其 ER 3 之對象）。

**(戊) 一項通則**：本例顯示**訊號值與彈窗是同一件事的兩種寫法** ——
037 以 `$FOTA_Status$ = [值]` 寫其內部狀態，彈窗清單以 `PU` 編號寫其外部表徵。
**二者之對照表若建起來，本組多數「內部狀態」之列即可轉為可觀測。**
已入 `BACKLOG.md` **B-10**。

---

## 8. 待裁事項

| # | 事項 | § |
|---:|---|---|
| 1 | **`F=2`** —— 訊號記法之方括號與 F 檢查衝突（執行層傾向 (甲) 改 F 之判準） | §2.2 |
| 2 | **`PUXXX1`／`PUXXX3` 為二側皆未指派之佔位** —— `104`／`105`／`106` 之彈窗無編號可引 | §1.2 |
| 3 | **`028`／`029` 之 `$FOTA_Status$` 不可觀測** —— 執行層建議改以彈窗表徵（其來源已在案） | §7 |
| 4 | `IX_END` 之片語表每進一新 Test Set 即落後一次 | §2.3 |
| 5 | ROV 餘 16 列之分包順序（13 直接觸發 → `088`／`095` → `104`–`106`） | §3.1 |
