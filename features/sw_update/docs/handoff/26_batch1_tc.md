# 下放包 26 —— 四項裁定、R-SU30 v2／R-SU32、batch 1 TC 草案（4 列）

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`25_batch1_relist.md`；對應上繳：`docs/upstream/25_batch1_review.md`
- 裁定狀態：`C`／`E` 欄、DR-SU2 母群、批次順序、R-SU30 v2、R-SU32 —— 分析層即裁
- **`SWE1-FOTA-179` 之處理結果：掛 `PENDING`，且其成因為 R-SU29 未預見之第三型**

---

## 一、上繳包 24 審查判定

**收。§7.3 與 §7.1 各自找到一件「照著任務做不會發現」的事。**

### 1.1 §7.3 —— 替代鍵之反向實測，未被要求而做

T38a 只令追查 `vehicle_category` 之 `C` 欄來源。查完得一條 126/126 全對之鏈路，
**而那條鏈路對本 feature 無用**（第一環 `HMI Source ID` 不存在）。

執行層另做「本 feature 有沒有**別的**鍵可接上 SYS1」——三欄交集皆 0，
且形態不同族。其記明之理由應立為通則：

> 查一條路走得通，與查**所有路都走不通**，是兩件事。
> 前者只需一個成功案例，後者需要窮舉。
> **而「有沒有別的路」這個問題通常不會出現在任務清單裡 ——
> 因為任務是照著已知的那條路寫的。**

### 1.2 §7.1 —— DR-SU2 二段之成員資格用了兩套判準

`365` 在已確認段而不在未確認母群內，成因為其 VC 之
`Send a server-initiated OTA **notification** through the TC client`
命中 `notification` 之 regex，而該 `notification` 是**服務間之訊息**。

執行層之診斷正確且指出 R-SU30 之設計缺口：

> R-SU30 之二段設計是為了防「未確認被讀成已確認」，
> **而它防不到「二段之成員資格用了兩套不同的判準」** ——
> (a) 用人裁、(b) 用 regex。
> **一個台帳若二段來源不同，其比值就不是進度。**

§三 v2 更正。

### 1.3 §7.2 —— 三段建議採納，其甲乙丙之並陳為正確之作法

尤其 (丙)「在 `179` 之結果出來前，我們不知道 R-SU25(c) 對 105 列是否夠用」
—— **本包即給出該結果，見 §四**。

---

## 二、四項裁定

### 2.1 `C` 欄（`Requirement or Design ID (Polarion)`）—— **留空**

依據：本 feature 之 037 為 18 欄舊版面、**無 `HMI Source ID` 欄**，
鏈路之第一環不存在；替代鍵三欄交集皆 0（§1.1）。
**`vehicle_category` 之作法不可移植** —— 其可行係因其 037 版面較新（20 欄 rev D），
非因其方法較好。

**留空為裁定，不是遺漏** —— 須於 `framework.md` 與交付說明中明記其理由。
若 Pei 日後要求填，須向上游索一份 037↔Polarion 之對照，**屆時為新 DR**；
**分析層不得以任何推定值填入**（037 之 `Source Requirement ID` 形態與
Polarion `NRL-` 不同族，強行對應即造值）。

### 2.2 `E` 欄（`Test Case ID (TestRail)`）—— **不用**

依據：15 本簿 2167 列**全空**、母本無 DV／無條件式格式、
其語意為 TestRail 之測試管理端 id，填寫者非 TC 產出端。
（同 `AB`–`AG` 之判準，且有 2167 列之實測佐證。）

### 2.3 `SOURCE_COLUMNS.md` 之清帳完成

| 欄 | 裁定 |
|---|---|
| 036 `C` | **不用（留空，依 §2.1；理由須逐字記入台帳）** |
| 036 `E` | **不用（測試管理端）** |
| SYS1 `SYSRE_HMI_Source ID`（欄 4） | **改標「已用」** —— 其為 R-SU4(b) 之錨 token 來源，一直在用，前輪標「未定」為分析層之誤 |
| SYS1 `ID`（欄 0）、`_polarion`（欄 6） | **不用** —— 其唯一用途為 036 `C` 欄之鏈路，而該鏈路於本 feature 不成立（§2.1） |

**未定欄自此為 0。** R-SU26(b) 之要求全案履行完畢。

### 2.4 批次順序 —— 採納三段建議，並即刻授權併行線

1. **先完成 batch 1（含 `179`）** —— 本包已完成其起草，結果見 §四
2. 依 `179` 之結果分岔 —— **本包已可分岔，見 §四 4.1**
3. **`ROV Installation`（20 列）＋ `Update HMI`（6 列）之 26 列即刻授權為併行線**
   —— 其 105 列為 0，不受本議題影響。材料傾印見 T39c

---

## 三、R-SU30 v2（抄入 RULINGS.md，逐字，append 於 v1 之後）

```
R-SU30 v2（滾動清單之讀法防誤 —— 二段判準一致性）

v1(a)(b)(c)(d) 維持。增 (e)(f)。

(e) **二段之成員資格須用同一判準。** 實測（上繳包 24 §7.1）：
    DR-SU2 之 (a) 段用**人裁**、(b) 段用**語形 regex**，
    致 `SWE1-FOTA-365` 在 (a) 而不在 (b) —— **(a) 不是 (b) 之子集**，
    其比值遂不是進度。

    判準不同時，**人裁為準**（語形判準之地位為上界之估計工具，
    上繳包 20 §7.1(乙2) 已裁）。

(f) **母群之定義改為**：「符合語形條件者」**聯集**「已由人裁判定為
    無觀測面者」。據此 DR-SU2 之母群由 105 → **106 列**（105 + `365`）。

    **母群數之變動須逐次記明其成因**，不得只改數字 ——
    本次之成因為 `notification` 之語形偽陰性（上繳包 19 §7.1(甲) 已預告之類），
    **其於 DR 清單本身出現，是該偽陰性首次造成台帳之邏輯不一致。**
```

---

## 四、R-SU32（新條）與 `SWE1-FOTA-179` 之處理

### 4.1 `179` 之處理過程（R-SU31(c) 令逐步記明）

**步驟 1 —— 依 R-SU25(c) 求其外部可觀測後果。**
其行為鏈為：SWMC 交付 DD metadata → WUS 分析 → 判定為 Silent →
WUS 自動請求 SWMC 啟動下載。
其**外部可觀測之後果**為：使用者未做任何操作，而下載自動開始並終至安裝。

**步驟 2 —— 檢查該後果是否可與鄰列區辨。**
`SWE1-FOTA-175`（已於 pilot 撰為 `newR1L-SU-001`）之外部可觀測後果為：
使用者未做任何操作，而更新於背景執行至完成（版本號改變）。

**二者之外部可觀測面完全相同。**
`179` 與 `175` 之差別全在內部（前者為 DD metadata 之分析與下載請求之發出，
後者為整體之背景執行），**而該差別無任何外部表徵**。

**步驟 3 —— 判定。**
若逕為 `179` 撰寫 TC，其 `test_item` 之括號下半將與 `175` 之測試目的
**不可區辨**，違 IN §4.3「sibling 兩列讀來相同 = FAIL」與 R-S4；
且二 TC 之 Procedure 與 ER 將逐行相同，構成 §7 之偽通過
（`179` 之 TC 實際上驗的是 `175` 之行為）。

**故 `179` 掛 `PENDING`，增列入 DR-SU2。**

### 4.2 R-SU32（新條，抄入 RULINGS.md，逐字）

```
R-SU32（105 列之三型 —— 「不可區辨」為第三型）

R-SU29 預設 105 列有二型：(i) 有外部可觀測後果 → 照常撰寫；
(ii) 無任何外部可觀測後果 → 掛 `PENDING`。

實測（下放包 26 §4.1，`SWE1-FOTA-179`）顯示**第三型**：

(iii) **有外部可觀測後果，但該後果與鄰列不可區辨。**
      `179` 之後果（無使用者操作而更新自動完成）與 `175` 完全相同；
      二列之差別全在內部（DD metadata 之分析 vs 整體之背景執行），
      **該差別無任何外部表徵**。

裁定：

(a) 第三型**同樣掛 `PENDING`**，但其**成因須明記為「不可區辨」而非
    「無後果」** —— 二者之解方不同。

(b) **DR 之請求內容不同**：第二型求**觀測手段**；
    第三型求**區辨手段**（如：可觀測其下載請求已發出之跡象，
    或確認該列之驗證得併入鄰列）。DR-SU2 之清單須分記二型。

(c) **禁止之作法**：不得為使第三型「可寫」而撰寫與鄰列逐行相同之 TC。
    該 TC 於 lint 全綠、於 sibling 檢查亦可能因 `test_item` 措辭不同而過關，
    **但它驗的是鄰列之行為** —— 此為 IN §7 之偽通過，
    且其偽裝性高於杜撰觀測面（後者尚可由「來源查無」揭穿）。

(d) **併入鄰列為一種合法解**，但**須由上游確認**（DR），
    不得由分析層逕定 —— 逕定即等於代上游合併需求單元（違 IN §8.2.2 之
    「TC 作者不得合併多個 RD sub-id」）。
```

---

## 五、batch 1 TC 草案（4 列，`181` 待其 VC）

`181` 之 `Verification Criteria` 於上繳包 23 §2 已備而分析層本輪未讀畢，
**其 TC 於下放包 27 補**（**不重列材料** —— 分析層自該檔讀）。

---

### TC-6 ← `SWE1-FOTA-180`（`newR1L-SU-006`）

**test_item**
```
When the update type is identified as Silent Update, the WiFi Update Service shalll not trigger the SW Update HMI to display a download confirmation screen.
(No download confirmation screen shown for a silent update)
```
> **verbatim 保留原文之 `shalll`**（R-4 僅允許句首大寫之正規化）。
> 登 **D-4**（拼寫殘留，非缺字，與 D-1／D-2 不同型）。

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package with update type Silent Update is staged on the OTA Server for this head unit
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Record the head unit screen content from the availability check until the software version changes
4. Check that no download confirmation screen appears in the recorded screen content
```

**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. The head unit screen content from the availability check until the software version changes is recorded
4. The recorded screen content contains no download confirmation screen
```

**specification_reference**
```
CFTS057-4907482
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P2`

**錨定依據**：首選 `4907470` 為 **4.7.3.1 Critical Updates** 之條文
（其述「download starts automatically; SHALL NOT display a download
confirmation screen」）—— **章與情境皆非本列**。正解為候選 **#2 `4907482`**
（4.7.3.2 Silent，`The OTA client MAY NOT display a download confirmation screen`）。
⚠ CFTS 用 `MAY NOT`、037 用 `shall not` —— **SWE.6 以 037 為需求本文**，
TC 依 037 之強度撰寫；該強度差異記於 reasoning，不改二者、不發 DR。

---

### TC-7 ← `SWE1-FOTA-182`（`newR1L-SU-007`）

**test_item**
```
The WiFi Update Service shall not trigger the SW Update HMI to display a deployment confirmation screen when the update type is identified as Silent Update.
(No deployment confirmation screen shown for a silent update)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package with update type Silent Update is staged on the OTA Server for this head unit
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Record the head unit screen content from the availability check until the software version changes
4. Check that no deployment confirmation screen appears in the recorded screen content
```

**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. The head unit screen content from the availability check until the software version changes is recorded
4. The recorded screen content contains no deployment confirmation screen
```

**specification_reference**
```
CFTS057-4907484
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P2`

**錨定依據**：首選 `4907470`、次選 `4907471` 皆為 **4.7.3.1 Critical Updates**；
`4907471` 尤為**相反之規定**（Critical 更新**須**顯示 deployment confirmation screen）。
正解為候選 **#3 `4907484`**（4.7.3.2 Silent，
`The OTA client MAY NOT display a deployment confirmation screen`）。
**與 TC-6 之 sibling 區分**：前者為 download confirmation、本列為 deployment
confirmation，其括號下半逐字不同。

---

### TC-8 ← `SWE1-FOTA-184`（`newR1L-SU-008`）

**test_item**
```
The WiFi Update Service shall apply Silent Update execution rules to all supported update session flows, including update check, deployment package download and installation processing.
(Silent rules apply across check, download and installation phases)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package with update type Silent Update is staged on the OTA Server for this head unit
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Read the software version shown on the head unit and record it as Version_initial
2. Trigger an update availability check to the OTA Server
3. Record the head unit screen content from the availability check until the software version changes
4. Read the software version shown on the head unit and record it as Version_after
5. Check that Version_after differs from Version_initial and that the recorded screen content contains no SW Update prompt, progress notification or confirmation screen
```

**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. The head unit screen content from the availability check until the software version changes is recorded
4. Version_after is recorded
5. Version_after differs from Version_initial; the recorded screen content contains no SW Update prompt, no progress notification and no confirmation screen across the check, download and installation phases
```

**specification_reference**
```
CFTS057-4907486
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

**與 `175` 之區分**：`175` 驗「Silent 時自動於背景執行」，
本列驗「該規則**及於全部三個階段**」—— 其 ER 第 5 行明列
check／download／installation 三階段，為本列獨有之驗證點。
**其後半句「unless required for safety-related conditions」為 `176` facet B
所轄（`newR1L-SU-003`），本列不涵蓋**（IN §8.2.1 不擴入 sibling）。

---

### TC-9 ← `SWE1-FOTA-179`（`newR1L-SU-009`）—— **PENDING**

**test_item**
```
If the DD metadata indicates a Silent Update, the WiFi Update Service shall automatically request SWMC to initiate deployment package download.
(Download request is issued automatically on silent classification)
```

**pre_conditions**
```
1. The head unit is connected to a Wi-Fi network with internet access
2. An update package with update type Silent Update is staged on the OTA Server for this head unit
3. PENDING: DR-SU2 means of distinguishing the automatic download request from the overall silent background execution
```

**input_test_data**
```
NA
```

**test_procedure**
```
1. Trigger an update availability check to the OTA Server
2. PENDING: DR-SU2 step to observe that the deployment package download request has been issued
3. Check that the download request is issued without any user interaction
```

**expected_result**
```
1. The update availability check completes and an update is reported as available
2. PENDING: DR-SU2 observable evidence that the download request has been issued
3. No user interaction occurs before the download request is issued
```

**specification_reference**
```
CFTS057-4907481
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

> **成因為 R-SU32(iii)「不可區辨」，非「無後果」** ——
> 其後果（無操作而下載自動開始並終至安裝）存在，但與 `175` 完全相同。
> DR-SU2 對本列之請求為**區辨手段**（R-SU32(b)），不是觀測手段。

---

## 六、任務（T39）

| # | 任務 |
|---|---|
| T39a | **batch 1 產出與 lint**：`sandbox/batch01/` 產出 TC-6～TC-9（`newR1L-SU-006`～`009`），欄集同 pilot v3。**預期 U=3**（TC-9 之三個 PENDING）。跑 lint 全輸出 |
| T39b | **台帳更新**：(i) DR-SU2 依 R-SU30 v2(f) 母群改 **106**，並依 R-SU32(b) 分記二型（第二型＝求觀測手段；第三型＝求區辨手段，現有 `179` 一列），確認進度改記 **6/106**；(ii) `DESCRIPTION_DEFECTS.md` 新增 **D-4**（`180` 之 `shalll`，拼寫殘留）；(iii) `SOURCE_COLUMNS.md` 依 §2.3 清帳，**未定歸 0** |
| T39c | **併行線材料**（§2.4-3）：`ROV Installation`（20 列）與 `Update HMI`（6 列）共 26 列之材料傾印 —— Title、Description 全文、前 5 候選（含候選全文）、`Verification Criteria` 全文、`Verification Method`、105/126 分類。**分二檔或分節，供分析層分批起草** |
| T39d | **T-抄**：R-SU30 v2、R-SU32 逐字 append；索引表同步（33 條現行、R-SU30→v2；留存 18 條）。PLAYBOOK 追加二則：(1)「查一條路走得通，與查所有路都走不通，是兩件事 —— 後者需要窮舉，而它通常不在任務清單裡」（出處：上繳包 24 §7.3）；(2)「一個台帳若二段來源不同，其比值就不是進度」（出處：上繳包 24 §7.1） |

**不在本輪**：`181` 之 TC（下放包 27）、寫回、git。

---

## 七、上繳包要求（`docs/upstream/25_batch1_review.md`）

1. T39d 核對結果 + 索引表
2. T39a 之 lint 全輸出
3. T39c 之 26 列材料
4. T39b 之三項台帳更新
5. 未結 DR 清單（2 筆；DR-SU2 含二型分記與 6/106）
6. 獨立自評 —— 特別回答：**TC-8（`184`）與 TC-1（`175`）之外部可觀測面
   是否也構成 R-SU32(iii) 之不可區辨** ——
   即：`184` 之「三階段皆適用」在畫面記錄上，是否真的能與 `175` 之
   「背景執行」分開判讀，還是分析層在 §五之區分只是措辭上的
