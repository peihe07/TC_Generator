# 上繳包 40 —— T58＋T59 執行結果（下放包 45／46）

- 日期：2026-08-29｜方向：執行層 → 分析層
- 對應下放包：`45_delegation.md`（分工改制）＋ `46_rov_b_close.md`
- **本批為新分工下之首次自行起草** —— ROV-C ＋ ROV-D **七列七 TC**
- **lint 20 項全 0 ＋ U=0**；**全簿遮蔽測試 45 TC／990 組，逐字相同 0**

---

## 1. 待裁清單（**本輪核心**，依 45 §2.3 之 (a)–(d) 四類）

### (a) 一列是否拆、拆幾個 —— **二列皆判「不拆」，其一與下放包之預判相反**

| 037 | 判 | 理由 |
|---|---|---|
| **`108`** | **不拆** | 其條件為 `$LTE_Status$ <> […] **OR** $Cellsignal$ = […]`，形式上為二個獨立之部分失效（IN §8.2.2 疑須拆）。**惟二者在台架上無法獨立產生** —— 拔除／遮蔽行動網路會使二條件同時成立。**拆之即得二個 procedure 完全相同之 TC，落入 R-SU32(iii) 不可區辨。** 故不拆 |
| **`109`** | **不拆** | 下放包 46 §三 預判「若各分支之畫面不同，疑須拆」。**實測其多分支只在 s3**（`display the appropriate HMI based on current FOTA_Status`），**而 s3 已由 46 §三 委派 `092`–`095`**。s2 為**單一條件**（`<> [Waiting for HMI Acceptance]`）。**委派之後本列只剩一個驗證單元，不須拆** |

> **`108` 之判斷值得提出**：**IN §8.2.2（獨立部分失效即拆）與 R-SU32(iii)
> （不可區辨者不得並列）在此相衝突** —— 前者要拆，後者禁止拆出不可區辨之二列。
> **執行層取後者**，理由：拆出之二 TC 若無法以任何台架動作分開，
> **其存在只增加 TC 數而不增加驗證力**。**此為新型之衝突，列待裁。**

### (b) 錨之最終裁定（建議，待抽驗確認）

| TC | 037 | **建議之錨** | 首選？ | 內容覆核 |
|---|---|---|---|---|
| `039` | `089` | `4907907`（分 0.382） | ✅ #1 | 逐字含 `monitor $Speedometer$` 與 `lockout behavior defined in Requirement ID 4915105 present in CFTS022` |
| `040` | `098` | `4907881`（分 0.386） | ✅ #1 | `The pop-up shall dismiss if the radio enters Standby/Sleep mode` |
| `041` | `107` | `4907894`（分 0.472） | ✅ #1 | `…compare the current system time…and then send the difference in $HU_Scheduled_Install$` |
| `042` | `108` | `4907895`（分 0.713） | ✅ #1 | 逐句對應，含二個連線條件 |
| `043` | `109` | `4907896`（分 0.746） | ✅ #1 | 逐句對應 |
| `044` | `088` | `4907906`（分 0.268） | ✅ #1 | `display pop-up, PU0303 after a successful FOTA update at Body ON mode` |
| `045` | `095` | `4907904`（分 0.451） | ✅ #1 | `…display the software update complete pop-up, PU0416` |

**七列皆取首選** —— **惟每一列皆經內容覆核，非因其為首選而取**。
`044` 之首選分僅 0.268（接近機制 3 之門檻 0.267）**而內容逐字命中**，
**其為「低分而對」之例，與 `037` 之「高分而錯」互為反面。**

### (c) `PENDING` 與其型別 —— **本批 0 個**

七列皆可觀測、皆可觸發（`088`／`095` 須一次真實更新成功，**非第四型**）。

### (d) 範圍委派之對象列

| TC | 不涵蓋之行為 | 所屬列 | 依據 |
|---|---|---|---|
| `039`（`089`） | **車速鎖定行為本身** | **`CFTS022` 之 `4915105`（外部規格）** | 錨 `4907907` 逐字指向該處；**IN §8.4.2 不涵蓋**。⚠ 執行層覆核：`4915105` 於 `ANCHOR_POOL.md` 有登記，**惟其身分為「內文交叉引用之出處」而非 CFTS_57 之物件**（語料中查無）——**外部性成立** |
| `041`（`107`） | 排程時間之**決定** | `103`／`104`／`105` | 45 §3.2 |
| `042`（`108`） | `Update Now` 之選擇處理 | `099`（`033`） | 46 §三 |
| `043`（`109`） | 各 `FOTA_Status` 值對應之**畫面內容** | `092`–`095` | 46 §三 |
| `044`（`088`） | What's New 之快取與次次 Body ON 之顯示 | `090`（`028`） | 45 §3.2 |
| `045`（`095`） | Body ON 模式之判定 | `088`（`044`） | 45 §3.2 |

### (d′) ⚠ **一項新提出之委派疑義：`107` 之驗證點是否還在**

45 §3.2 將「排程時間之決定」委派 `103`／`104`／`105`；
46 §二 #3 裁 `$HU_Scheduled_Install$` 之外部表徵為「排程畫面所顯示之時間」。

**而 037 `107` 四句全為內部行為**（存排程時間／讀系統時間／算時間差／設屬性），
**無一句講顯示**。若顯示歸他列、屬性不可引，**本列恐無自己的驗證點**（同 `313` 之形）。

**執行層之判斷（列待裁）**：**其餘量為「所顯示之剩餘時間算得對」** ——
`103`／`104`／`105` 驗的是「開啟排程畫面／可選時間」，
**無一列驗『顯示的剩餘時間與所排時間一致』**。故 `041` 之判定核心取此，
**且不寫任何秒數或誤差**（§8.4.1；037 與 CFTS 皆無精度值）。

---

## 2. T59b —— 產出

| 列 | TC ID | 037 | 錨 | P |
|---|---|---|---|---|
| 10 | `newR1L-SU-039` | `089` | `4907907` | P1 |
| 11 | `newR1L-SU-040` | `098` | `4907881` | P2 |
| 12 | `newR1L-SU-041` | `107` | `4907894` | P2 |
| 13 | `newR1L-SU-042` | `108` | `4907895` | P1 |
| 14 | `newR1L-SU-043` | `109` | `4907896` | P1 |
| 15 | `newR1L-SU-044` | `088` | `4907906` | P1 |
| 16 | `newR1L-SU-045` | `095` | `4907904` | P1 |

**`PENDING` 0｜TC 7｜涵蓋 037 列 7。**

**產出腳本設二道停止條件**（皆於寫檔前）：
1. `design_method` 對母本 `下拉選單!$A$1:$A$9`；
2. **`test_item` 上半逐句對 037 全文**（R-S4）——
   **任一不符即 `sys.exit`，不吐半份簿**。

> **第 2 道是本輪新增** —— 前此各批之逐字性由分析層給文、執行層核對；
> **自行起草後，該核對必須在產出鏈內**，否則沒有人會發現。

### 2.1 屬性之逐個判（下放包 46 §二 #3）

| 屬性 | 判 | 本批之用法 |
|---|---|---|
| `$Speedometer$` | 可觀測 | ER：`the speed shown on the instrument cluster is greater than zero` |
| `$OperationalModeSts$`（`088`） | 可觀測 | pre／proc 以 Body ON 模式表述 |
| `$Cellsignal$`／`$LTE_Status$` | 可觀測（表徵） | ER：`the status bar shows no cellular signal` |
| `$HU_Scheduled_Install$` | 可觀測（表徵） | ER：`Time_remaining corresponds to the interval…`，**無秒數** |
| `$FOTA_Status$` | **不可觀測** | ER 改以 `PU0303`／`PU0416`／畫面替換表述 |

> ⚠ **`$OperationalModeSts$` 為本批新見之屬性**（`088` s1／s4），
> **不在下放包 46 §二 #3 之四項裁定內**。執行層依同一判準判其**可觀測**
> （Body ON／OFF 為車輛模式，台架可控可讀；037 s4 即其定義）——
> **列此以備追認。**

---

## 3. T59a —— `032`／`036`／`037` 之 pre 改寫

依 46 §二 #2 之 (乙解) 逐字套用（`has been staged … with deferral permitted/prohibited`）。
**lint 不變**：`rov_b` 仍為 20 項全 0 ＋ U=0 ＋ `I-cross=5`。

---

## 4. T59d —— lint ＋ 全簿遮蔽測試

```
rov_b   行計 A=0 … R=0  T=0  U=0  V=0  I-cross=5
rov_cd  行計 A=0 … R=0  T=0  U=0  V=0  I-cross=7
```

**二簿皆 20 項全 0 ＋ U=0。** `rov_cd` 之 `I-cross=7` **全為半窗**
（七列僅 `040`／`043` 帶 `until`？——實測七列之 procedure 皆無 `until` 子句，故全半窗），
**零配對**。

### 4.1 全簿遮蔽測試

| 項 | 值 |
|---|---:|
| 回測集 | **45 個 TC** |
| 配對 | **990 組** |
| **逐字相同** | **0 組** |
| 僅差 `PENDING` | **21 組**（全為 batch02a 之已知暫態，未增） |

**本批未新增任何相同配對。**

---

## 5. T59d —— 抽驗材料 5 列（種子揭露）

**種子**：`random.seed(20260829)`、`random.sample(range(7), 5)` → 抽中索引 `[0,2,3,4,5]`
即 **`039`／`041`／`042`／`043`／`044`**。


### `newR1L-SU-039` ← `SWE1-FOTA-089`

**037 全文**：

> s1. The ROV Update Service shall retrieve the $Speedometer$ vehicle property using CarPropertyManager.
> s2. If the Speedometer value is greater than zero, the ROV Update Service shall determine that the vehicle is in motion and enforce the vehicle speed lockout behavior.
> s3. The ROV Update Service shall notify the ROV Update HMI of the vehicle-in-motion status.

**所裁之錨**：`CFTS057-4907907` —— `The HU shall monitor $Speedometer$ and implement the HU vehicle speed lockout behavior defined in Requirement ID 4915105 present in CFTS022 to support`

**前 5 候選**：

1. `4907907` 章 9.3 分 **0.382** ← **採** — The HU shall monitor $Speedometer$ and implement the HU vehicle speed lockout behavior defined in Requirement 
2. `4907886` 章 9.1 分 **0.195** — If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Availabl
3. `4907884` 章 9.1 分 **0.189** — User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Avail
4. `4907880` 章 9.1 分 **0.164** — When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU
5. `4907887` 章 9.1 分 **0.153** — When the $Hybrid_Type$ = [BEV] or [PHEV] and if the user selects 'Schedule Update' option on "ROV Forced Updat

**判定核心**（ER 末行）：`3. The head unit does not start the installation while the speed shown on the instrument cluster is greater than zero`

### `newR1L-SU-041` ← `SWE1-FOTA-107`

**037 全文**：

> s1. The ROV Update Service shall store the determined scheduled installation time for the update event.
> s2. The ROV Update Service shall retrieve the current system time from the system time source.
> s3. The ROV Update Service shall calculate the time difference between the scheduled installation time and the current system time.
> s4. The ROV Update Service shall set $HU_Scheduled_Install$ with the calculated remaining time value using CarPropertyManager.

**所裁之錨**：`CFTS057-4907894` —— `When the scheduled time has been determined, the HU shall compare the current system time (defined in CFTS015) to the scheduled time and then send the`

**前 5 候選**：

1. `4907894` 章 9.1 分 **0.472** ← **採** — When the scheduled time has been determined, the HU shall compare the current system time (defined in CFTS015)
2. `4907915` 章 9.4.1 分 **0.259** — When the scheduled time is reached, TBM shall send $Install_Time_Reached$ to SGW.
3. `4907900` 章 9.2 分 **0.228** — The HU shall populate the installation percentage and estimated time remaining progress in the pop-up, "Instal
4. `4907633` 章 4.10.5.1 分 **0.191** — If the user schedules an update, the HU shall wake up at the scheduled time and check the last known preinstal
5. `4907886` 章 9.1 分 **0.183** — If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Availabl

**判定核心**（ER 末行）：`4. Time_remaining corresponds to the interval between Time_now and Time_scheduled`

### `newR1L-SU-042` ← `SWE1-FOTA-108`

**037 全文**：

> s1. The ROV FOTA HMI shall capture user selection of “Update Now” from the “ROV Forced Update Available B” pop-up.
> s2. The ROV Update Service shall retrieve $LTE_Status$ or $Cellsignal$ using CarPropertyManager.
> s3. If ROV Update Service receives $LTE_Status$ <> [3G OR 4G OR H_Plus] OR $Cellsignal$ = [0 OR 1 OR SNA], the ROV Update HMI shall display the "No Connectivity" pop-up and prevent update initiation.

**所裁之錨**：`CFTS057-4907895` —— `HU shall display "No Connectivity pop-up", when the user selects 'Update Now' option on "ROV Forced Update Available B" pop-up and if the HU receives `

**前 5 候選**：

1. `4907895` 章 9.1 分 **0.713** ← **採** — HU shall display "No Connectivity pop-up", when the user selects 'Update Now' option on "ROV Forced Update Ava
2. `4907884` 章 9.1 分 **0.377** — User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Avail
3. `4907886` 章 9.1 分 **0.345** — If the user selects 'Schedule Update' option on "ROV Forced Update Available A" or "ROV Forced Update Availabl
4. `4907880` 章 9.1 分 **0.345** — When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU
5. `4907887` 章 9.1 分 **0.294** — When the $Hybrid_Type$ = [BEV] or [PHEV] and if the user selects 'Schedule Update' option on "ROV Forced Updat

**判定核心**（ER 末行）：`3. The head unit does not start the installation while the status bar shows no cellular signal`

### `newR1L-SU-043` ← `SWE1-FOTA-109`

**037 全文**：

> s1. The ROV Update Service shall retrieve $FOTA_Status$ using CarPropertyManager.
> s2. During the pre-installation flow, if $FOTA_Status$ <> [Waiting for HMI Acceptance], the ROV Update Service shall interrupt the current pre-installation flow and shall notify the ROV FOTA HMI.
> s3. The ROV FOTA HMI shall display the appropriate HMI based on current FOTA_Status.

**所裁之錨**：`CFTS057-4907896` —— `When the HU is in the pre-installation flow, if $FOTA_Status$ &lt;&gt; [Waiting for HMI Acceptance], the HU shall interrupt the current pre-installati`

**前 5 候選**：

1. `4907896` 章 9.1 分 **0.746** ← **採** — When the HU is in the pre-installation flow, if $FOTA_Status$ &lt;&gt; [Waiting for HMI Acceptance], the HU sh
2. `4907880` 章 9.1 分 **0.425** — When HU receives $FOTA_Status$ = [Waiting for HMI Acceptance] AND $FOTA_Delay$ = [Not_Prohibited], then the HU
3. `4907884` 章 9.1 分 **0.391** — User shall be able to cancel or ignore the pop-up, "ROV Forced Update Available A" or "ROV Forced Update Avail
4. `4907898` 章 9.2 分 **0.300** — When the HU receives $FOTA_Status$ = [Installing FOTA Update], the HU shall display installation screens.
5. `4907900` 章 9.2 分 **0.285** — The HU shall populate the installation percentage and estimated time remaining progress in the pop-up, "Instal

**判定核心**（ER 末行）：`3. The recorded screen content shows the pop-up replaced by another SW Update screen`

### `newR1L-SU-044` ← `SWE1-FOTA-088`

**037 全文**：

> s1. The ROV Update Service shall retrieve $FOTA_Status$ and $OperationalModeSts$ using CarPropertyManager.
> s2. If FOTA_Status indicates successful FOTA update ( $FOTA_Status$ = [Successful FOTA Update]) completion and OperationalModeSts indicates Body ON mode, the ROV Update Service shall notify the ROV FOTA HMI.
> s3. The ROV FOTA HMI shall display the PU0303 success pop-up.
> s4. *Body on mode when $OperationalModeSts$ = Ignition_on or Ignition_pre_start or Ignition_start or Ignition_Cranking or Iginiton_on_Engine_on else Body off when $OperationalModeSts$ =Initialization or Ignition_Of

**所裁之錨**：`CFTS057-4907906` —— `The HU shall display pop-up, PU0303 after a successful FOTA update at Body ON mode. Refer to CFTS009 for power moding states`

**前 5 候選**：

1. `4907906` 章 9.3 分 **0.268** ← **採** — The HU shall display pop-up, PU0303 after a successful FOTA update at Body ON mode. Refer to CFTS009 for power
2. `4907909` 章 9.3 分 **0.267** — The HU shall cache $FOTA_Status$ = [Successful FOTA Update] and What's new details to display until next Body 
3. `4907874` 章 8.4 分 **0.244** — If the update is downloaded via Wi-Fi with Body OFF mode, the installation shall happen at the next Body ON mo
4. `4907904` 章 9.2 分 **0.239** — When the HU receives $FOTA_Status$ = [Successful FOTA Update] , the HU shall display the software update compl
5. `4907398` 章 4.6 分 **0.236** — Pre Conditions for FOTA via Wifi:➢ Vehicle’s battery is above 65% State of Charge ($IBS_SOC$ &gt; [65]). If $I

**判定核心**（ER 末行）：`4. Version_after differs from Version_initial; the head unit displays the PU0303 success pop-up`

---

## 6. 未結 DR 清單（**5 筆**，不變）

| DR | 阻斷 | Urgency |
|---|---|---|
| DR-SU1 | `001`／`002`／`003`；`005` 待釐清 | High |
| DR-SU2 v3 | (d) 第四型 4 列 | High |
| DR-SU3 | `017` | Medium |
| DR-SU4 | `011`–`016` | High |
| DR-SU5 | `021` ＋ `131` s4 | Medium |

**全案 `PENDING` 43 行**（本批 0）｜**可交付候選 28 列**（21 ＋ 本批 7）。

---

## 7. 獨立自評（入 BACKLOG）—— 45／46 §五-6：最不確定之一列與其攔截機制

**答：`newR1L-SU-041`（`107`）。而若抽驗未抽中它，現有機制一個都攔不到。**
（本輪抽驗恰好抽中它 —— **但那是運氣，不是機制。**）

**(甲) 為何是它。** 其餘六列之判定核心皆為**畫面或彈窗之有無**，
其對錯一眼可判。**`041` 之判定核心是一個計算之正確性**：

> `Time_remaining corresponds to the interval between Time_now and Time_scheduled`

**而「corresponds to」是我寫的，不是規格寫的。** 037 與 CFTS 皆無精度值，
故不能寫秒數或誤差（§8.4.1）—— **但「不寫誤差」與「寫一個模糊詞」是兩件事，
而我寫了後者。** 一個相差三分鐘之實作會不會通過，**取決於執行者怎麼讀那個詞。**

**(乙) 現有機制為何攔不到它。** 逐項對照：

| 機制 | 對 `041` 之效力 |
|---|---|
| **lint 之 H（ER 模糊語）** | ❌ **未命中** —— 其詞表收的是 `properly`／`correctly`／`as expected` 之類，**`corresponds to` 不在表內** |
| **`I-cross`** | ❌ 本列為半窗，**根本不參與比對** |
| **遮蔽測試** | ❌ 其 Final Step 與他列字面相異，**通過** |
| **R-SU43 檢定** | ❌ 規格未給他值（沉默），**依 v2(a) 通過** |
| **R-SU42 分類** | ⚠ 其為 (b) 設計選擇，**而我引了 `4907894` 作來源** —— 惟該物件只說「送出差值」，**未說 HMI 顯示之精度**，**射程不吻合**（同 `4907440` 之形）|
| **抽驗 5/7** | ✅ **唯一可能攔到者** —— 而其命中率為 5/7 |

**(丙) 故其攔截完全依賴抽驗，而抽驗是抽樣。**
本批 7 列抽 5，未中之機率 2/7 ≈ 29%。
**若本批為 45 §2.1 所令之 20–30 列，抽 5 列之未中率將升至 75–83%。**

> **這是新分工之結構性風險，且它會隨批量增大而變壞** ——
> 45 §2.4 稱「抽驗之效力來自『抽中即全退』」，
> **而全退之前提是抽中；批量愈大，抽中愈難。**

**(丁) 我認為可補之機制（不裁，入 BACKLOG）**：

1. **H 之詞表擴充**：加入 `corresponds to`／`matches`／`is consistent with`
   等**關係模糊詞** —— 其與現有詞表（`properly` 類**程度模糊詞**）不同族，
   **現行詞表整族沒收**；
2. **自陳式標記**：起草者於 `REASONING.md` 逐列標其**自信度**，
   **低者優先納入抽驗** —— 使抽驗由隨機改為**分層**；
3. **「規格無值而 ER 有比較」之機器檢查**：凡 ER 含比較關係
   （`corresponds`／`equals`／`differs`）而其 `test_item` 上半無任何數值者，
   **列為待人裁**。本列即此形。

**(戊) 一項自陳**：本輪抽驗抽中 `041` 是隨機的結果。
**若我為求好看而挑選抽驗列，本節之發現就不會存在** ——
**種子已揭露（`20260829`）且抽樣在起草之後，可覆核。**

---

## 8. 待裁事項

| # | 事項 | § |
|---:|---|---|
| 1 | **`108` 不拆之判斷** —— IN §8.2.2（獨立部分失效即拆）與 R-SU32(iii)（不可區辨者不得並列）**相衝突**，執行層取後者 | §1(a) |
| 2 | **`109` 不拆** —— 委派之後多分支已不在本列 | §1(a) |
| 3 | **`107` 之餘量是否為「所顯示之剩餘時間算得對」** | §1(d′) |
| 4 | **`$OperationalModeSts$` 之可觀測性**（本批新見，不在 46 §二 #3 之四項內） | §2.1 |
| 5 | **抽驗之未中率隨批量增大而升** —— 20–30 列批抽 5 之未中率 75–83% | §7(丙) |
| 6 | **H 之詞表整族未收「關係模糊詞」**（`corresponds to` 類） | §7(丁) |
