# 下放包 27 —— 三項 FAIL 之處置、R-SU32 v2（第三型與語形正交）、TC-6 v2、TC-10

- 日期：2026-08-28
- 方向：分析層 → 執行層
- 前一包：`26_batch1_tc.md`（**檔尾截斷，本包補完，見 §四**）
- 對應上繳：`docs/upstream/25_batch1_review.md`
- 裁定狀態：R-SU32 v2 —— 分析層即裁；三項 FAIL 全部為分析層之誤

---

## 一、下放包 26 之三項 FAIL —— 全部確認，皆分析層之誤

### 1.1 檔尾截斷（阻斷）—— 確認，§四補完

截掉之處恰為 §七-6 之自評題收束。**本包補完該問句，並由分析層自行作答**
（§四）—— 該問是對分析層前一包之檢驗，執行層答與分析層答皆有價值，
但既已截斷，分析層先答，執行層於本輪覆核。

### 1.2 索引數「33 條」錯一 —— 確認

現行 R-SU1～R-SU31 連續無缺 = 31 條，加 R-SU32 為 **32 條**。
執行層之旁證正確（留存 17 + R-SU30 v1 = 18，本輪僅「一取代 + 一新增」，
現行數不可能跳兩格）。**以 32 為準**，執行層抄錄時之處置正確。

### 1.3 TC-6 未宣告 facet 切分 —— 確認，且其指出之矛盾為真

`180` 之第二句
> The WiFi Update Service shall automatically request SWMC to initiate
> deployment package download without user interaction.

與 `179` 之第三句
> If the DD metadata indicates a Silent Update, the WiFi Update Service shall
> automatically request SWMC to initiate deployment package download.

**幾乎逐字相同**，而 `179` 已被判為 R-SU32(iii) 不可區辨並掛 `PENDING`。
同一包內二種作法（TC-8 對 `184` 之後半句有明文交代、TC-6 對 `180` 之後半句沒有）
—— **不一致為分析層之疏漏**。

**裁定（不取執行層所列之二支，取第三支）**：

該行為之**需求單元為 `179`**（其 `Requirement Title` 即
`Start Silent Update Download Automatically`，正是該行為之標題）；
`180` 之需求單元為**抑制下載確認畫面**（其標題
`Optionally Suppress Download Confirmation Screen`）。

故 `180` 之第二句係**複述 `179` 所擁有之行為**，
依 IN §8.2.1（不得擴入 sibling Req 所擁有之行為），
**TC-6 不涵蓋該句，並須明文宣告其委派** —— 與 TC-8 委派安全條款予
`176` facet B 之作法一致。

**`179` 之判定不受影響**：該行為之 `PENDING` **只掛一次，掛在 `179`**。
二列各掛一次會使 DR-SU2 之清單重複計數同一件事。

**執行層所設之二支皆不成立之理由**：
- 「`180` facet B 亦須掛 PENDING」→ 不成立，因該 facet 不屬 `180`
- 「`179` 之不可區辨判定不成立」→ 不成立，因 `180` 底下該句**同樣不可寫**，
  只是它根本不該由 `180` 驗

---

## 二、R-SU32 v2（抄入 RULINGS.md，逐字）

`SWE1-FOTA-181` 之起草（§三 TC-10）揭出 v1 之一項範圍誤設。

```
R-SU32 v2（105 列之三型 —— 第三型與語形分類正交）

v1(a)(b)(c)(d) 維持。增 (e)(f)。

(e) **第三型（不可區辨）不限於 105 列。**
    實測：`SWE1-FOTA-181` **不屬 105 列**（其 `Verification Criteria`
    含外部面之語形，故未被語形判準攔下），
    但其需求之限定詞「**immediately** after download」
    **無可觀測之判準** —— 下載完成之時點不可觀測，
    且規格未給任何時間閾值（§8.4.1 禁造值）。
    即：**其可寫性之缺口與語形分類無關。**

    故「105 列」與「不可寫之列」**是兩個不同的集合，且不互相包含**：
    - 105 列中有可寫者（其外部後果可取得）
    - 105 列外有不可寫者（`181`）
    **語形判準測的是「文字裡有沒有提到外部面」，
    可寫性問的是「這件事驗不驗得出來」—— 二者正交。**

(f) **DR-SU2 之母群須另立第三型之段**：
    R-SU30 v2(f) 之母群定義（語形條件 ∪ 已人裁為無觀測面者）
    **涵蓋不了第三型**，因第三型之列可能完全不符語形條件。

    故 DR-SU2 之台帳改三段：
      (a) 已確認・第二型（無觀測手段）
      (b) 未確認之母群（語形條件 ∪ 已人裁者）—— **僅對第二型有意義**
      (c) 已確認・第三型（不可區辨／不可量之限定詞）——
          **其母群未知，且不可由語形估計**

    **(c) 段無上界可報。** 陳述時須明記「第三型之母群未經盤點，
    其規模未知」，**不得以 (b) 之 106 冒充全體之上界**。
```

---

## 三、TC-6 v2 與 TC-10

### 3.1 TC-6 v2 ← `SWE1-FOTA-180`（`newR1L-SU-006`）

**除下列宣告外，其餘六欄逐字同下放包 26 §五 TC-6，不重列。**

**新增之委派宣告（入 reasoning，不入工作簿欄位）**：

> 本列 Description 之第二句
> （`The WiFi Update Service shall automatically request SWMC to initiate
> deployment package download without user interaction`）
> 所述之行為，其需求單元為 **`SWE1-FOTA-179`**
> （`Start Silent Update Download Automatically`）。
> 依 IN §8.2.1，本 TC **不涵蓋該行為**，其驗證由 `179` 之 TC
> （`newR1L-SU-009`）承擔；該 TC 現掛 `PENDING`（R-SU32(iii)）。
> 本 TC 之驗證單元限於**抑制下載確認畫面**。

### 3.2 TC-10 ← `SWE1-FOTA-181`（`newR1L-SU-010`）

**test_item**
```
Upon receiving deployment package download completion status, the WiFi Update Service shall immediately start installation prechecks and deployment.
(Installation follows download completion with no further interaction)
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
3. Record the head unit screen content and any user input from the availability check until the software version changes
4. PENDING: DR-SU2 step to observe the point at which deployment package download completes
5. Read the software version shown on the head unit and record it as Version_after
6. Check that Version_after differs from Version_initial and that no user input was required between download completion and installation
```

**expected_result**
```
1. Version_initial is recorded
2. The update availability check completes and an update is reported as available
3. The head unit screen content and user input from the availability check until the software version changes are recorded
4. PENDING: DR-SU2 observable evidence of the download completion point
5. Version_after is recorded
6. Version_after differs from Version_initial; no user input occurred between download completion and installation
```

**specification_reference**
```
CFTS057-4907483
```
**design_method**：`功能測試 (Functional based ; no specific technique)`｜**priority**：`P1`

**錨定依據**：首選 `4907483`（4.7.3.2，`2. After the deployment package is
downloaded, its deployment shall start immediately`）與本列逐句對應，採之。

**PENDING 之成因（第三型，R-SU32(iii)）**：
本列之限定詞為「**immediately** after download」。其驗證需
(i) 下載完成之時點可觀測、(ii) 「immediately」之時間閾值。
**(i) 無觀測通道；(ii) 規格未給任何閾值** —— 自行設一個秒數即造值（§8.4.1）。
**其餘部分（安裝於下載完成後進行、其間無使用者操作）可觀測，故本 TC 不整列掛
`PENDING`，只掛該時點之觀測步驟。**

⚠ **`181` 不屬 105 列** —— 其為 R-SU32 v2(e) 之首例：
**語形判準未攔下它，而它同樣不可完整驗證。**

---

## 四、下放包 26 §七-6 之補完與作答

**補完之問句**：

> 獨立自評 —— 特別回答：TC-8（`184`）與 TC-1（`175`）之外部可觀測面
> 是否也構成 R-SU32(iii) 之不可區辨 —— 即：`184` 之「三階段皆適用」
> 在畫面記錄上，是否真的能與 `175` 之「背景執行」分開判讀，
> 還是分析層在 §五之區分只是措辭上的。

**分析層之作答：可區辨，但其可區辨之處不在我原本寫的地方。**

原文之區分為「`184` 之 ER 明列 check／download／installation 三階段」——
**若二 TC 之畫面記錄範圍相同，列出三個階段名只是措辭，不構成區辨。**

**真正之區辨在記錄之起點**：
- `TC-1`（`175`）步驟 3：`Record the head unit screen content throughout
  **the update execution**` —— 起點為更新開始執行
- `TC-8`（`184`）步驟 3：`Record the head unit screen content **from the
  availability check** until the software version changes` —— 起點為**可用性查詢**

**可用性查詢發生於下載之前。** 一個系統可以在查詢階段彈出
「有可用更新」之提示，而在執行階段完全靜默 ——
該情形會使 `TC-8` 判 fail 而 `TC-1` 判 pass。
**存在一個可使二者判決相異之系統行為，故二者可區辨**（§8.3 之壓力測試）。

**但原文之依據寫錯了**：其依據應為**記錄之起點涵蓋查詢階段**，
而非「ER 列出三個階段名」。TC-8 之 ER 第 5 行應據此改寫（§五 T40a）。

**一併記明**：本問若不問，TC-8 會以一個**措辭上之區分**通過 sibling 檢查，
而其實質區分（起點）從未被寫進任何欄位 ——
**那正是 R-SU32(c) 所禁之情形，只是尚未到逐行相同之地步。**

---

## 五、任務（T40）

| # | 任務 |
|---|---|
| T40a | **TC-8 之 ER 第 5 行改寫**（§四）：其區分依據改記為「記錄起點涵蓋可用性查詢階段」。改寫後之 ER 第 5 行為：<br>`Version_after differs from Version_initial; the recorded screen content, starting from the availability check, contains no SW Update prompt, no progress notification and no confirmation screen` |
| T40b | **batch 1 產出與 lint**：`sandbox/batch01/` 產出 TC-6 v2、TC-7、TC-8（含 T40a 之改寫）、TC-9、TC-10（`newR1L-SU-006`～`010`，五列）。**預期 U=5**（TC-9 之 3 + TC-10 之 2）。跑 lint 全輸出 |
| T40c | **DR-SU2 之台帳改三段**（R-SU32 v2(f)）：(a) 已確認・第二型（現 5 列，`363`–`367`）／(b) 未確認之母群 106 列（僅對第二型有意義）／(c) 已確認・第三型（現 **2 列**：`179`、`181`），**(c) 段明記「母群未經盤點，規模未知」**。表頭之進度記法須同時呈現二型，**不得以 (b) 之 106 冒充全體上界** |
| T40d | **`ROV Installation` + `Update HMI` 併行線材料**（下放包 26 §2.4-3 之 T39c，本輪續令）：26 列之 Title、Description 全文、前 5 候選（含全文）、VC 全文、VM、105/126 分類 |
| T40e | **T-抄**：R-SU32 v2 逐字 append；索引表同步（**32 條現行**、R-SU32→v2；留存 19 條）。PLAYBOOK 追加二則：(1)「語形判準測的是『文字裡有沒有提到』，可寫性問的是『驗不驗得出來』—— 二者正交，不可互相估計」（出處：R-SU32 v2(e)）；(2)「型態摘要之『型態』必須包含一個實例，否則它只是一個計數」（出處：上繳包 23 §7.3） |

**不在本輪**：併行線之 TC、寫回、git。

---

## 六、上繳包要求（`docs/upstream/25_batch1_review.md`）

1. T40e 核對結果 + 索引表（**32 條**）
2. T40b 之 lint 全輸出
3. T40c 之三段台帳
4. T40d 之 26 列材料
5. 未結 DR 清單（2 筆；DR-SU2 含二型分記）
6. 獨立自評 —— 特別回答：**§四之作答（TC-8 與 TC-1 以「記錄起點」區辨）
   是否經得起同一壓力測試 —— 即，是否真有一個可執行之測試步驟能使
   「查詢階段之提示」與「執行階段之提示」在記錄上分開**
