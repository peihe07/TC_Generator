# 上繳包 18 —— 切斷循環指涉、判準之偽陰與 doc-sync 之錨

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：[../handoff/18_break_the_circle.md](../handoff/18_break_the_circle.md)
- 前一包上繳：[17_scope_of_inventory.md](17_scope_of_inventory.md)
- **本包零寫回工作簿**

**17 包之提交狀態**：已於 2026-08-24 經 Pei 授權並提交（`84a0c27`，12 路徑）。
本包之提交待授權。

**⚠ 本包查出一項新異常：`A-PMH16`** —— SYS1 之 `9.1` 散文本身漏字，
**其中兩處為時序子句**。與 A-PMH03 之 7.1 完全同型。詳見 §2.3。

---

## 一、§五三條之抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 逐字相符 |
|---|---|---|---|---|---|
| R-PMH66 | 判定為二值（逐字命中），門檻只分流殘餘且殘餘須人讀 | 395 | `a9ed686549088dfc` | `a9ed686549088dfc` | ✅ 逐字相符 |
| R-PMH67 | 列舉式判準須附偽陰之抽樣估計；補標記不構成滿足 | 479 | `8effc16c06b1800f` | `8effc16c06b1800f` | ✅ 逐字相符 |
| R-PMH68 | doc-sync 之錨取門檻表輸出，不取整支程式 | 340 | `88c540f9cba69e2b` | `88c540f9cba69e2b` | ✅ 逐字相符 |

**命中數**：handoff 3 塊、RULINGS 回讀 3 塊，`a == b` 皆 `True`。
**既有條文未動**：`R-PMH10`／`R-PMH63`／`R-PMH65` SHA256 皆相符。

---

## 二、章 9 與章 11 之建錨重跑（步驟 2，R-PMH66）

`chapter_bidirectional.py` 改為**只給起錨**，章之範圍 =
[本章起錨, **下一章起錨**)，使相鄰兩章之邊界**必然共用同一個字串**
（區間在構造上不可能重疊或留縫）。六章全部建錨。

判定改為 R-PMH66：**逐字命中為權威**，逐字未命中者一律進殘餘，
**殘餘須有人讀之具名結論**（`RESIDUE_VERDICT`），未具名者 → FAIL。

### 2.1 章 11 —— 殘餘 5 句，**無新漏**

```
=== 章 11 之雙向複驗（R-PMH51）===
PDF 段：679 字元；SYS1：2 則、420 字元
PDF 段起錨 `VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS:`（訖 = 下一章之起錨）
PDF 段內 marker：1 個 —— ['VRLP1:']
```

```
=== 結果（R-PMH66 —— 判定為二值，門檻只分流殘餘）===
  方向一未逐字命中：1 則
    outline 11.1（覆蓋 100.0%）：VRLP1: VR hard key to activate SIRI/non-native Voice Assistants (eg. Long press of VR HK) 

  方向二逐字命中 1/6；**殘餘 5 句**
  **殘餘不得由門檻自動判為「非漏」** —— 逐句須有人讀之具名結論；
  覆蓋率只決定人讀之優先順序（高者先看），不決定結論。

    [覆蓋 100.0%] VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS: VRLP1: VR hard key to activate SIRI/non-native Voice Assistants (eg.
      人讀結論：非漏 —— SYS1 之 outline `11` 逐字為 `VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS`（無尾冒號），`11.1` 逐字為 `VRLP1: VR hard key to…`。逐字未命中之因為 PDF 之節標題帶尾冒號、且切分於 `(eg.` 處斷開

    [覆蓋 100.0%] Radio status after interaction with SIRI depends on outcome of the interaction: Screen Off and Audio OFF (i.e.
      人讀結論：非漏 —— 切分假象：句切於 `(i.e.` 處；其全句於 SYS1 11.1 逐字存在

    [覆蓋 100.0%] radio back to off), Screen ON and Audio OFF, Screen Off, and Audio ON, Screen ON and Audio ON.
      人讀結論：非漏 —— **條列再流**（A-PMH03 原記之形態，A-PMH14 已以方向二確認）：SYS1 11.1 作 `- Screen Off and Audio OFF (i.e. radio back to off), - Screen ON and Audio OFF, …`，僅條列符號不同，四個 outcome 全在

    [覆蓋  0.0%] (DCR19385) POWER MODING STATE MATRIX: Power Moding behavior shall not be developed without following the Power Moding State Matrix, which is in a separate Excel document.
      人讀結論：**漏 —— A-PMH14 新漏 3（既有，非新）**：`POWER MODING STATE MATRIX:` 段於 SYS1 全簿命中 0。句首之 `(DCR19385)` 屬前一句（VRLP1）之尾，SYS1 11.1 有之

    [覆蓋  0.0%] If this document is not available, please request a copy from the author of this logic and flow document.
      人讀結論：**漏 —— A-PMH14 新漏 3 之第二句（既有，非新）**

  殘餘未具名結論者：**0**
```

**五句之人讀結論**：3 句為**非漏**（節標題帶尾冒號、切分於 `(eg.`／`(i.e.` 處、
條列再流），2 句為 **A-PMH14 新漏 3 之既有兩句**（p10 之
`POWER MODING STATE MATRIX:` 段）。

**R-PMH51 對 11.1 之要求自此以逐字二值法結清** ——
其「條列再流」之歸因成立：SYS1 之 `11.1` 四個 outcome 全在，僅條列符號不同。

### 2.2 章 9 —— 殘餘 15 句，**與 A-PMH14「狀態矩陣整表缺失」一致**

```
=== 章 9 之雙向複驗（R-PMH51）===
PDF 段：2942 字元；SYS1：2 則、1278 字元
PDF 段起錨 `8 Power Moding Please refer to Power Moding State Matrix`（訖 = 下一章之起錨）
PDF 段內 marker：1 個 —— ['PM1)']
```

```
=== 結果（R-PMH66 —— 判定為二值，門檻只分流殘餘）===
  方向一未逐字命中：1 則
    outline 9.1（覆蓋 54.3%）：PM1) In the event that there are popups to show at IGN OFF but the user has set Power Acce

  方向二逐字命中 0/15；**殘餘 15 句**
  **殘餘不得由門檻自動判為「非漏」** —— 逐句須有人讀之具名結論；
  覆蓋率只決定人讀之優先順序（高者先看），不決定結論。

    [覆蓋 66.7%] Charge Now - XEV key off-Pop-ups Charge Now/Summary; Preconditioning.
      人讀結論：非漏 —— 其散文 `3. XEV key off-Pop-ups Charge Now/Summary; Preconditioning.` 於 SYS1 9.1 逐字存在；句首之 `Charge Now -` 為前一條列項之尾，屬 `-layout` 之切分

    [覆蓋 50.0%] Fully functional for 60 seconds up to 2.5 minutes to display the popup(s).
      人讀結論：**部分漏 —— A-PMH16(1)**：`Fully functional` 為矩陣格（漏，屬新漏 2）；散文側 PDF 作 `should 'stay awake' for 60 seconds up to 2.5 minutes`，**SYS1 作 `should 'stay awake up to 2.5 minutes`** —— `' for 60 seconds` 整段缺失

    [覆蓋 47.1%] HVAC Knobs: HVAC Knobs: Maximum time the radio can 'stay awake' because of these popups is 10 KEY OFF OFF OFF minutes.
      人讀結論：非漏（散文側）—— `Maximum time the radio can 'stay awake' because of these popups is 10 minutes.` 於 SYS1 逐字存在；`HVAC Knobs:`／`KEY OFF OFF OFF` 為矩陣格，屬新漏 2

    [覆蓋 42.1%] OFF Forced OFF Headunit: If user chooses to dismiss Wi-Fi configuration popup, display Charge Now (if Headunit: Full on, some limited functionality applicable).
      人讀結論：非漏（散文側）—— `If user chooses to dismiss Wi-Fi configuration popup, display Charge Now (if applicable).` 於 SYS1 逐字存在；其餘為矩陣格，屬新漏 2

    [覆蓋 41.2%] FOTA update available - OFF Full on, some limited functionality If user accepts FOTA popup, start update and dismiss FOTA via Wi-Fi / Charge Now (if applicable) ICS Hard Controls: If user schedules an update time or dismisses update, display FOTA via Wi-Fi / Power Button is functional until power ICS Hard Controls: Charge Now (if applicable).
      人讀結論：非漏（散文側）—— FOTA 條列三句於 SYS1 9.1 逐字存在；`OFF`／`Full on, some limited functionality`／`ICS Hard Controls:` 為矩陣格，屬新漏 2

    [覆蓋 38.1%] (No ACC Climate GUI: Climate GUI: position) OFF Forced OFF The priority of the popups which occur at IGN OFF are as follows: Headunit: Headunit: 1.
      人讀結論：非漏（散文側）—— `The priority of the popups which occur at IGN OFF are as follows:` 於 SYS1 逐字存在；`(No ACC position)`／`Climate GUI:`／`Forced OFF` 為矩陣格，屬新漏 2

    [覆蓋 32.7%] [CR22412] OFF be functional (See CTS009) (DCR19385) Full on, some limited functionality If the user interacts with the FOTA [CR22412] popup the radio shall 'stay ICS Hard Controls: ICS Hard Controls: Power Button only is functional Only headunit-related controls functional awake' until the user has not interacted with the popup for 60 seconds.
      人讀結論：非漏（散文側）—— `If the user interacts with the FOTA [CR22412] popup the radio shall 'stay awake' until the user has not interacted with the popup for 60 seconds.` 於 SYS1 逐字存在；`VR HK to activate SIRI…(See CTS009)` 等為矩陣格，屬新漏 2

    [覆蓋 30.8%] FOTA via Wi-Fi configuration - OFF OFF position If user chooses to configure Wi-Fi, display Charge Now (if applicable) when Climate GUI: Climate GUI: available) Wi-Fi configuration is complete.
      人讀結論：非漏（散文側）—— `2. FOTA via Wi-Fi configuration` 之兩句於 SYS1 逐字存在；矩陣格屬新漏 2

    [覆蓋 23.5%] Fully functional ENGINE ON Climate GUI: Climate GUI: Not Visibile due to power off Fully functional Headunit: Headunit: VR HK to activate SIRI/Voice assistants shall OFF be functional (See CTS009) (DCR19385) Fully functional ICS Hard Controls: ICS Hard Controls: Power Button only is functional Only headunit-related controls functional PM1) In the event that there are popups to show at IGN OFF but the user has KEY ON HVAC Knobs: HVAC Knobs: set Power Accessory Delay to 0 seconds, the head unit should 'stay awake' ENGINE OFF Fully functional.
      人讀結論：**部分漏** —— `PM1) In the event that there are popups to show at IGN OFF but the user has set Power Accessory Delay to 0 seconds, the head unit should 'stay awake` 之散文於 SYS1 存在（惟見 A-PMH16(1)）；`KEY ON ENGINE ON`／`ENGINE OFF`／`Climate GUI:`／`Headunit:`／`ICS Hard Controls:`／`Fully functional`／`Not Visibile due to power off` 全為矩陣格 —— **漏，屬新漏 2**

    [覆蓋 22.2%] Shut the radio down if user dismisses Charge Now XEV key off Pop-ups.
      人讀結論：非漏（散文側）—— SYS1 作 `Shut the radio down if user dismisses XEV key off Pop-ups.`，逐字存在；句中之 `Charge Now` 為前一條列項之尾，屬切分

    [覆蓋 10.4%] If the user does not (ACC or Climate GUI: Climate GUI: RUN) interact with the popup within 60 seconds the timeout defined in pop-up list, Not Visibile due to power off Fully functional (compressor and heater not working) the radio should shut Off the popup should close aofnd if no other popups Headunit: Headunit: VR HK to activate SIRI/Voice assistants shall are to be shown the radio should shut off.
      人讀結論：**部分漏 —— A-PMH16(2)(3)(4)**：PDF 作 `within 60 seconds the timeout defined in pop-up list, the radio should shut Off the popup should close aofnd if no other popups…`；**SYS1 作 `within 60 the timeout defined in pop-up list, the popup should close if no other popups…`** —— 缺 `seconds`、缺 `the radio should shut Off the`、`aofnd` 被逕改為 `if`。其餘 `(ACC or RUN)`／`Climate GUI:` 為矩陣格，屬新漏 2

    [覆蓋  0.0%] 8 Power Moding Please refer to Power Moding State Matrix for further specifications.
      人讀結論：**漏 —— 屬新漏 2 之範圍，惟 A-PMH14 未具名此句**：`Please refer to Power Moding State Matrix for further specifications.` 為章 9 之首句（指標句），SYS1 全 52 則探針 `Please refer to Power Moding State Matrix` 命中 **0**。與新漏 3（p10 之 `POWER MODING STATE MATRIX:` 段）同一形態、不同位置

    [覆蓋  0.0%] HEADUNIT POWER HEADUNIT POWER OFF ON ICS Hard Controls : ICS Hard Controls: Power Button only is functional Fully functional HVAC Knobs: HVAC Knobs: KEY ON Fully functional.
      人讀結論：**漏 —— 新漏 2**：狀態矩陣之表頭（`HEADUNIT POWER OFF`／`ON` × `ICS Hard Controls`／`HVAC Knobs`）。探針 `HEADUNIT POWER`／`ICS Hard Controls`／`HVAC Knobs` 於 SYS1 全簿命中皆 0

    [覆蓋  0.0%] KEY OFF accessory delay expires Only headunit-related controls functional (ACC HVAC Knobs: HVAC Knobs: 2.
      人讀結論：**漏 —— 新漏 2**：矩陣之 `KEY OFF (ACC)` 列（`accessory delay expires`／`Only headunit-related controls functional`）

    [覆蓋  0.0%] OFF OFF after power accessory delay expires 3.
      人讀結論：**漏 —— 新漏 2**：矩陣之 `KEY OFF (No ACC)` 列（`after power accessory delay expires`）；句末之 `3.` 為條列編號被切分所併入

  殘餘未具名結論者：**0**
```

**逐字命中 0/15** —— 因 PDF p9 之文字層是**兩欄狀態矩陣與 `PM1)` 散文交錯**。
十五句之人讀結論分三類：

| 類 | 句數 | 結論 |
|---|---:|---|
| 散文側存在、矩陣格造成逐字未命中 | 8 | **非漏** |
| 矩陣格本身 | 4 | **漏 —— A-PMH14 新漏 2**（表頭、`KEY OFF (ACC)`／`(No ACC)` 兩列） |
| 章 9 首句之指標句 | 1 | **漏 —— 屬新漏 2 之範圍，惟 A-PMH14 未具名此句**（`Please refer to Power Moding State Matrix for further specifications.`，SYS1 全 52 則命中 0） |
| **散文側本身漏字** | 2 | **A-PMH16 —— 新異常**（見 §2.3） |

**與 A-PMH14 之「狀態矩陣整表缺失」一致 —— 停止條件 7 未觸發。**

### 2.3 ⚠ **A-PMH16 —— 殘餘人讀查出 SYS1 之 `9.1` 散文本身漏字**

以 PyMuPDF `get_text("blocks")` 取 p9 之 `PM1)` **單一區塊**（658 字元，
不與矩陣交錯），對 SYS1 `9.1`（1,265 字元）做**字級 diff**：

| # | PDF p9 `PM1)` 區塊 | SYS1 `9.1` | 判定 |
|---|---|---|---|
| **1** | `should 'stay awake'` **`for 60 seconds`** `up to 2.5 minutes` | `should 'stay awake up to 2.5 minutes` | **漏 —— 時序子句 ＋ 收尾單引號** |
| **2** | `within 60` **`seconds`** `the timeout` | `within 60 the timeout` | **漏 —— 時序單位**（SYS1 之句不成句） |
| **3** | `pop-up list,` **`the radio should shut Off the`** `popup should close` | `pop-up list, the popup should close` | **漏 —— 整個子句** |
| 4 | `popup should close` **`aofnd`** `if` | `popup should close if` | **非漏** —— `aofnd` 為 PDF 原文之 typo，SYS1 逕改為 `if`（未經授權之改寫，登記） |

**(1)(2) 皆為時序** —— 60 秒之 stay-awake 窗、60 秒之互動逾時，
正是 **A-PW68** 之形態。**7.1 漏的是動畫／splash 之時序，9.1 漏的是
popup stay-awake 之時序 —— 同一份 SYS1 匯出，同一類內容，兩處。**
**5 個 leaf 引 `9.1`。R-PMH50 第三度獲直接佐證。**

### 2.4 **為何 13 包之全簿雙向 diff 沒查出 —— 這正是 R-PMH66 之立條理由兌現**

13 包方向二以 `-layout` 全文切句，p9 切出之「句」皆為矩陣格與散文之混合串；
該等混合串之 6-gram 覆蓋率多 >= 30%，**遂被門檻自動判為「切分假象」而濾掉**。

**門檻做了本不該由它做的判定。** 本輪依 R-PMH66(b)(c) 令殘餘逐句人讀，
該四處即於第 9、11 句浮現。

**16 §12 第 2 項之循環指涉自此切斷**：9.1／11.1 之結論不再建於 6-gram 門檻，
而建於逐字二值 ＋ 逐句人讀之具名結論。

### 2.5 據實記載：**章 7／10／12 現為 FAIL**

六章皆已建錨，**而只有 8／9／11 之殘餘寫了人讀結論**
（R-PMH51 所涉之三則）。章 7／10／12 執行即 FAIL（殘餘未具名）。

**這是正確之預設** —— 未經人讀之殘餘不得被當成「非漏」。
**惟其代價須明說**：`chapter_bidirectional.py` 現在**不是**一支可全綠之檢查，
其 6 章中有 3 章處於 FAIL。**列為下一輪之工作。**

---

## 三、章錨之分割檢查（步驟 3）

```
=== 章區間之分割檢查（17 §12 第 1 項）===
  章       起      訖     字元  起錨
  7    4845   8192   3347  7 Startup Notes:
  8    8192   9029    837  R1Low Only
  9    9029  11972   2943  8 Power Moding Please refer to Power Moding State Ma
 10   11972  13489   1517  9 Power Moding Additional Power Moding Behavior Note
 11   13489  14169    680  VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS:
 12   14169  15171   1002  10 Power Moding - Off Road+

  已覆蓋 10326 / 15171 字元（68.1%）；重疊 **0**（構造上不可能）

  未覆蓋段【首章之前】4845 字元；**其中之 marker：無**
    首 120 字元：R1 ‐ Power Moding HMI Logic and Flow SR24 Post 2A. DCR22412 January 24, 2023 HMI Lead: Paolo Visconti paolo.visconti@ext
    末 120 字元：th driver door closed Ignition ON ≤ 3 sec. Power Hard Key Ignition ON if driver door removed/not present/open Screen On 

  未覆蓋段【末章之後】0 字元；**其中之 marker：無**

  **未覆蓋段皆不含 marker —— 停止條件 8 未觸發。**
  （首章之前為 p1–p7 之封面與五張流程圖頁，A-PMH04 已知之圖片佔位）
```

**未覆蓋段只有「首章之前」4,845 字元（p1–p7 之封面與五張流程圖頁），
其中之 marker 為「無」** —— **停止條件 8 未觸發**。

**構造上之改進須具名**：訖錨改為「下一章之起錨」後，
**重疊與縫隙不再可能發生** —— 17 §12 第 1 項所擔憂之「錨之外的第 7 個
marker」，其藏身處被壓縮為僅首尾兩段，而該兩段已逐段列出且不含 marker。

**殘餘盲區（已寫入 `LIMITS`）**：本檢查查不出「起錨落在章內某處」——
若某章之起錨取得太後面，其前半會被併入前一章，**覆蓋率仍是 100%**。

---

## 四、R-PMH67 之落實（步驟 4）

### 4.1 補六標記後之候選

```
=== 質疑型條文之候選清單（R-PMH64）===
`RULINGS.md` 之條文總數 = **68**；判準標記 = 21 個；**候選 = 37**
命中率 = 54.4%

條號         命中之標記
R-PMH8     撤回
R-PMH9     作廢
R-PMH10    取代
R-PMH13    撤回／而非
R-PMH15    取代
R-PMH16    不符
R-PMH17    取代
R-PMH20    而非
R-PMH23    矛盾
R-PMH24    取代／撤回
R-PMH26    不成立
R-PMH27    並非／作廢／取代
R-PMH28    而非
R-PMH36    而非
R-PMH37    失效
R-PMH39    作廢／取代／湊得
R-PMH41    不符
R-PMH42    不符
R-PMH44    過時
R-PMH45    而非
R-PMH46    失效
R-PMH47    而非
R-PMH48    過時
R-PMH49    而非
R-PMH50    由…查出
R-PMH51    不符／改判
R-PMH55    不成立／而非
R-PMH57    而非
R-PMH59    失效／矛盾
R-PMH60    誤用
R-PMH61    判錯
R-PMH62    不成立／之錯／失效／由…查出
R-PMH63    矛盾
R-PMH64    不成立／不符／之瑕疵／之缺陷／之錯／作廢／判錯／取代／失效／推翻／撤回／改判／未套用／由…查出／矛盾／誤用
R-PMH65    過時
R-PMH67    並非／失效／湊得／無來源／而非／過時
R-PMH68    失效
```

**候選由 23 增為 37**（母體亦由 65 增為 68 條）。
**R-PMH20 已被抓到**（`而非`）—— 分析層 §3.2 所舉之實測偽陰，補標記後命中。

**代價須具名**：`而非` 為極常用之詞，補入後
R-PMH28／36／45／47／49／55／57 一併命中，**偽陽隨之上升**。
**召回與精確之交換是真的，不是修辭。**

### 4.2 偽陰之抽樣（N = 10，種子 = 18，可重現）

```
=== 偽陰之抽樣（R-PMH67）===
未命中母體 = 31 條；抽樣 N = 10；種子 = 18（`random.Random(18).sample`，**可重現**）
**逐條由人讀判其是否應命中**；命中數即偽陰率之估計。

  R-PMH11    R-PMH11（素材雜湊檔之版控）
     不應命中 —— 要求型 —— 其所指定之實施方式後被 R-PMH15 推翻，故本條為**被質疑者**而非質疑者
  R-PMH18    R-PMH18（本 feature 兩個字面常數之保真）
     不應命中 —— 防禦型 —— 預先禁止一個尚未發生之處理（把兩常數統一），非推翻既有結論
  R-PMH25    R-PMH25（design_method vocabulary 之權威）
     **應命中** —— **質疑型（偽陰）** —— 推翻「以分頁名認 DV source」之做法，依據為實測：客戶那份之 x14 指向 `Reference!$C$4:$C$12`，`下拉選單` 為孤兒分頁。「以分頁名認 source 會取到未生效之清單」即其結論。**未命中之因：全條無 21 個標記中之任一詞**
  R-PMH29    R-PMH29（不確定性之處置方式）
     **應命中** —— **質疑型（偽陰）** —— 駁斥「以『測了會有併入之誘惑』為由不測」之理由，並禁止任選一案與擱置。**未命中之因：其反駁以「會讓一個可關閉之不確定性繼續開著」表達**
  R-PMH34    R-PMH34（涵蓋率類陳述之分母）
     **應命中** —— **質疑型（偽陰）** —— 其依據逐字指認 07 包上繳之分母有二錯（0 列工作簿計入、兩候選重複計入）。**未命中之因：措詞為「重複計算」「看起來比實際強」**
  R-PMH35    R-PMH35（判準須含 must-hit 且經實跑）
     **應命中** —— **質疑型（偽陰）** —— 其依據指認 07 包 §三之六列皆 must-not-hit、門檻不可執行、對 Q11 無鑑別力。**未命中之因：措詞為「不構成門檻」「無法區分」「無鑑別力」**
  R-PMH4     R-PMH4（素材台帳之到齊定義）
     不應命中 —— 定義型 —— 定「到齊」之定義並排除較弱判準（檔名相符／大小相同），未推翻任何既有結論
  R-PMH40    R-PMH40（判準門檻之單一來源）
     **應命中** —— **質疑型（偽陰）** —— 「兩份獨立維護之副本**一律視為缺陷**」，依據為 08 包自陳。**未命中之因：「視為缺陷」不在標記內，而「之缺陷」在**（差一個「之」）
  R-PMH6     R-PMH6（G/H 兩欄現值之處置延後）
     不應命中 —— 延後處置型 —— 登記 G/H 兩欄現況（H 欄違 canon §4.2）並禁止 Phase 0/1 改動，不推翻既有裁定
  R-PMH7     R-PMH7（交付母本）
     不應命中 —— 新裁定型 —— 定交付基底並給辨識判準；其所引發之作廢由 R-PMH8／R-PMH9 執行，本條自身不質疑

  **偽陰率之估計 = 5/10 = 50%** —— 推估未命中母體 31 條中約 **16** 條為質疑型
  即真正之質疑型條文約 37（候選，含偽陽） ＋ 16（未命中之推估） —— **判準只抓到其中一部分**
```

### 4.3 結果：**偽陰率 50%**

| 抽中 | 判定 | 未命中之因 |
|---|---|---|
| R-PMH25 | **應命中** | 全條無 21 標記中任一詞 |
| R-PMH29 | **應命中** | 反駁以「會讓一個可關閉之不確定性繼續開著」表達 |
| R-PMH34 | **應命中** | 措詞為「重複計算」「看起來比實際強」 |
| R-PMH35 | **應命中** | 措詞為「不構成門檻」「無法區分」「無鑑別力」 |
| R-PMH40 | **應命中** | 「視為缺陷」不在標記內，**而「之缺陷」在** —— 差一個「之」 |
| R-PMH4／6／7／11／18 | 不應命中 | 定義型／延後型／新裁定型／被質疑者／防禦型 |

**5/10 = 50%** —— 推估未命中母體 31 條中約 **16** 條為質疑型。

**即：判準抓到 37 個候選（含偽陽），而漏掉約 16 個。**
R-PMH67 之目的達成 —— **「不知道還漏多少」變成了「約漏 16 條」。**

**R-PMH40 那一列最該看**：它漏掉的原因是「視為缺陷」與標記「之缺陷」
**差一個字**。列舉式判準之脆弱在此具體可見。

---

## 五、R-PMH68 之落實（步驟 5）

錨由 `self_sha256()`（整支程式）改為 `thresholds_sha256()`
（`emit_thresholds()` 輸出之 SHA256）；`framework.md` 之行由
`> 產生時之程式 SHA256：` 改為 `> 門檻表 SHA256：`（命中 1 處，R-PMH41）。
`self_sha256()` 保留供追溯，其 docstring 載明其自本條起不再作為錨。

### 5.1 兩項故意失敗之實跑

```
=== R-PMH68 must-hit (a) —— 改門檻值而不重貼文件 → 須 FAIL ===
  改 G2 之門檻為 3 後：**FAIL** — **門檻表已與程式分岔（雜湊）** —— 文件記 `f574db043d496671…`，門檻表現值 `f5736b24513f4844…`。請重跑 `--emit-thresholds` 並重貼門檻節。
  攔下：True

=== R-PMH68 must-hit (b) —— 加一行純註解 → 須 PASS ===
  複本之 SHA256 與本檔不同：True
  複本之 --check-doc-sync 退出碼 = 0（0 = PASS）：True
  doc-sync PASS — 文件與程式同源 —— 門檻表 SHA256 `f574db043d496671…`（命中 1 處）＋ 門檻表 7 列逐字相同
  誤報已消除：True

==================================================================
(a) 改門檻值 → FAIL: True；(b) 加純註解 → PASS: True
**若改用舊錨（整支程式之 SHA256），(b) 必然 FAIL** —— 
  該誤報即 17 §12 第 5 項所述之「訓練出重貼反射」之來源。
```

**(b) 之作法須說明**：把本檔複製為 `scripts/_docsync_probe.py`
（置於 `scripts/` 下使其 `ROOT` 相同）並在其中**加一行純註解**，
以子行程跑其 `--check-doc-sync`。複本之檔案 SHA256 與本檔**不同**（已印出），
而其退出碼為 **0**。**若沿用舊錨，該複本必然 FAIL。**
跑畢即刪，不留檔。

### 5.2 殘餘盲區已具名

寫入 `LIMITS`：

> **R-PMH68 之殘餘盲區**：doc-sync 之錨為**門檻表輸出**之 SHA256，
> 守的是**值**而非**產生該值之邏輯** —— 改 `evaluate()` 之計算方式
> 而門檻值不變者，本檢查不會察覺。

---

## 六、TSV `section_title` vs PDF 之 48 列比對（步驟 6，只量測不改）

新增 `scripts/tsv_vs_pdf.py`。**判定為逐字二值**（R-PMH66）。

### 6.1 現行預設來源（`pdftotext -layout`）—— 不符 **10 / 48**

```
=== `layer3_sections.tsv` 之 `section_title` vs PDF（18 包步驟 6）===
leaf = **48**；PDF 側 = `pdftotext -layout`（現行預設），15171 字元

  章  leaf    不符
  7    19     5   ← 見下
  8     6     0
  9     5     5   ← 見下
 10    10     0
 11     5     0
 12     3     0

**逐字不符者 = 10 / 48**

  SWE1-HMI-PM-001-01  outline 7.1（p8）
    SYS1：SU1.) When the vehicle's driver door is closed a startup animation will be presented (3 sec), If ignition remains off af

  SWE1-HMI-PM-001-02  outline 7.1（p8）
    SYS1：SU1.) When the vehicle's driver door is closed a startup animation will be presented (3 sec), If ignition remains off af

  SWE1-HMI-PM-001-03  outline 7.1（p8）
    SYS1：SU1.) When the vehicle's driver door is closed a startup animation will be presented (3 sec), If ignition remains off af

  SWE1-HMI-PM-001-04  outline 7.1（p8）
    SYS1：SU1.) When the vehicle's driver door is closed a startup animation will be presented (3 sec), If ignition remains off af

  SWE1-HMI-PM-001-05  outline 7.1（p8）
    SYS1：SU1.) When the vehicle's driver door is closed a startup animation will be presented (3 sec), If ignition remains off af

  SWE1-HMI-PM-018-01  outline 9.1（p9）
    SYS1：PM1) In the event that there are popups to show at IGN OFF but the user has set Power Accessory Delay to 0 seconds, the

  SWE1-HMI-PM-018-02  outline 9.1（p9）
    SYS1：PM1) In the event that there are popups to show at IGN OFF but the user has set Power Accessory Delay to 0 seconds, the

  SWE1-HMI-PM-018-03  outline 9.1（p9）
    SYS1：PM1) In the event that there are popups to show at IGN OFF but the user has set Power Accessory Delay to 0 seconds, the

  SWE1-HMI-PM-018-04  outline 9.1（p9）
    SYS1：PM1) In the event that there are popups to show at IGN OFF but the user has set Power Accessory Delay to 0 seconds, the

  SWE1-HMI-PM-018-05  outline 9.1（p9）
    SYS1：PM1) In the event that there are popups to show at IGN OFF but the user has set Power Accessory Delay to 0 seconds, the
```

### 6.2 **block 層萃取（`--block`）—— 不符 5 / 48**

```
=== `layer3_sections.tsv` 之 `section_title` vs PDF（18 包步驟 6）===
leaf = **48**；PDF 側 = PyMuPDF block 層，15420 字元

  章  leaf    不符
  7    19     5   ← 見下
  8     6     0
  9     5     0
 10    10     0
 11     5     0
 12     3     0
```

**章 9 之 5 筆在 block 層全部相符** —— 其於 §6.1 之不符**是 `-layout`
交錯所致之偽陽**，非 SYS1 之問題（A-PMH16(d) 之同一原因）。

### 6.3 結論：**不符數不為 0，須裁**

**剩下之 5 筆全部是 outline `7.1`**（`SWE1-HMI-PM-001-01` ～ `-05`），
即 **A-PMH03 已知之漏句**，其漏落在 `section_title` 之**前 120 字元內**。

| 判定 | 內容 |
|---|---|
| **零誤報** | block 層之 5 筆全部落在已知損壞之 outline 上 |
| **零新發現** | 未查出 A-PMH03／A-PMH16 以外之任何不符 |
| **⚠ 惟其「相符」有一個很大的但書** | `section_title` **已截 120 字元**。outline `9.1` 之 5 筆之所以相符，**是因為 A-PMH16 之漏字落在第 120 字元之後** —— **截斷把它藏起來了** |

**故 17 §5.4 第 1 項不得降為低風險。** 其正確表述為：
`layer3_sections.tsv` 之 `section_title` 於**其所保留之前 120 字元內**，
除 7.1 外與 PDF 逐字相符；**120 字元之後未經任何比對**。

---

## 七、lint 全跑輸出（步驟 6 之延續）

**本輪未動 `generated/batch01.json`。**

```
batch = batch01；TC 數 = 8；leaf 數 = 7

  R-PMH50 每 leaf 有 source_clause 且非空                       PASS
  R-PMH50 source_clause 取自 PDF（非 SYS1）                     PASS
  profile §3.1 test_item 具下半括號（硬規則）                        PASS
  profile §3.3 design_method ∈ 下拉選單 9 詞條                   PASS
  profile §3.4 spec_reference 形態且與 layer3_sections.tsv 相符  PASS
  profile §3.5 priority ∈ {P0,P1,P2,P3}（母本 DV）             PASS
  profile §3.6 estimated_test_time 留白                      PASS
  profile §3.8 vehicle_models 留白                           PASS
  profile §3.7 functional_safety = NA                      PASS
  R-PMH18 test_group = 'Disclaimer screen'（小寫 s）           PASS
  R-PMH36 test_set = 'Disclaimer Screen'（大寫 S）             PASS
  R-PMH16 tc_id 形態 NR1L-DisclaimerScreen-{NNN}             PASS
  test_set ∈ Layer 2 定版 8 組                                PASS
  canon §11 方括號禁止（本 feature 無 profile 例外）                  PASS
  procedure 與 ER 步數一致                                      PASS
  必填欄無空                                                    PASS
  ER 未以 NA 充當未知                                            PASS
  canon §10.5 test_procedure >= 2 步                        PASS
  canon §5.1 procedure 無禁用動詞                               PASS
  canon §5.2B/§5.5 Final Step 含驗證意圖                        PASS
  canon §4.3.1 test_item 上半 ⊆ source_clause（verbatim）      PASS
  交付欄位無 markdown 標記（**／__／`）                               PASS
  canon §11 無彎引號                                           PASS
  canon §11 UI 標籤加直雙引號                                     PASS
  canon §5.2 步驟字數（normal <=12／final <=18）                  PASS
  R-PMH53 交叉引用存在且語意相容                                      PASS
  procedure／ER 編號自 1 起連號且逐位對齊                              PASS
  tc_id 唯一                                                 PASS
  tc_id_status = provisional                               PASS
  本批 leaf == Disclaimer Screen 之 7 leaf                    PASS

30/30 PASS

⚠ **本 lint 未涵蓋之 canon 節號（R-PMH52／R-PMH56）**：
    由 `scripts/canon_coverage.py` 自 canon 之節號全集減去上方 `COVERED` 產生，**不手寫**。
    執行：`python scripts/canon_coverage.py`
    本 lint 宣告涵蓋 10 節：['10.2', '10.3', '10.5', '10.7', '11', '4.3.1', '5.1', '5.2', '5.5', '8.4.3']
    （R-PMH58：靜態彙集與本次實際執行到之檢查點一致）
    **以上以外之全部 canon 節皆未由本 lint 檢查，須人讀。**
    R-PMH52：lint 全綠不得作為 TC 可用之證據。

⚠ R-PMH50 之限度：本 lint 只驗 source_clause **存在且取自 PDF**。
  **「是否忠於規格」不可機械檢查** —— 須人讀 PDF 原文與 TC 對照。
  本檢查只保證覆核所需之材料存在，不保證覆核已做。
```

**must-hit 兩份 fixture 仍 FAIL**：`batch01_prerework` 21/30／`batch01_r2` 29/30。

---

## 八、檢查總表

| 檢查 | 結果 |
|---|---|
| `lint_batch.py generated/batch01.json` | **30/30 PASS** |
| `chapter_bidirectional.py 8` | **PASS** |
| **`chapter_bidirectional.py 9`** | **PASS** —— 殘餘 15 句全具名 |
| **`chapter_bidirectional.py 11`** | **PASS** —— 殘餘 5 句全具名 |
| `chapter_bidirectional.py 7／10／12` | **FAIL（預期）** —— 殘餘未具名，見 §2.5 |
| **`chapter_bidirectional.py --partition`** | **PASS** —— 未覆蓋段不含 marker |
| **`challenge_rulings.py`** | **PASS** —— 68 條／候選 37／偽陰率 50% |
| **`check_granularity.py --doc-sync-must-hit`** | **PASS** —— (a) FAIL／(b) PASS |
| `check_granularity.py --check-doc-sync` | **PASS** —— 門檻表 SHA256 `f574db043d496671…` |
| `tsv_vs_pdf.py` ／ `--block` | 不符 10／**5**（**量測，須裁**） |
| `marker_coverage.py --self-test`／`--verify-extraction`／`--window-compare` | **PASS** |
| `canon_coverage.py`／`check_state_consistency.py`／`check_write_back.py --self-test` | **PASS** |

---

## 九、停止條件逐條檢查

canon §0 六條：

| # | 條件 | 觸發 |
|---|---|---|
| 1 | 規格缺件／不可讀 | 否 |
| 2 | 判準衝突未決 | 否 |
| 3 | 須寫回而工作簿狀態不明 | 否（零寫回） |
| 4 | 授權範圍不明之破壞性動作 | 否 |
| 5 | 上游資料未到而結論建於臆測 | **是（既有）** —— DR-PMH1 阻斷交付 |
| 6 | 產出與已交付件之慣例衝突 | 否 |

本包三條：

| # | 條件 | 實測 | 觸發 |
|---|---|---|---|
| 7 | 章 9 結論與 A-PMH14「狀態矩陣整表缺失」不一致 | **一致** —— 矩陣格 4 句 ＋ 首句指標句皆判漏；另查出之 A-PMH16 為**散文側之補充**，非與矩陣結論相反 | **否** |
| 8 | 分割檢查發現未覆蓋文字**且含 marker** | 未覆蓋 4,845 字元（p1–p7），**marker = 無** | **否** |
| 9 | 步驟 5 之 (b)（純註解 → 須 PASS）未通過 | 複本退出碼 **0** | **否** |

**本包無新觸發之停止條件。**

**惟須明說**：A-PMH16 是本包所查出之新異常，其未觸發停止條件 7
**是因為條件 7 問的是「與矩陣結論是否一致」，而它問的不是「有沒有新漏」**。
**若條件 7 寫成「章 9 發現任一新漏句即停」，本包會停。** 據實回報。

---

## 十、未結 DR 清單

| DR | 主旨 | 狀態 | 阻斷 |
|---|---|---|---|
| **DR-PMH1** | CFTS009 之 Off Road+ 行為 | `OPEN` | **阻斷交付** |
| DR-PMH2 | Power Moding State Matrix Excel | `OPEN` | 否（阻斷 ch 9 判讀） |
| DR-PMH3 | `SU9.)`／`SU9.1)` 是否應在 037 | `OPEN` | 否 |

**三筆皆尚未發出。第六度重申。**

**DR-PMH2 之理由本輪再增一項（A-PMH16）**：p9 之問題不只是「表格缺」——
**SYS1 所保留之 `9.1` 散文本身已失真，且失真處為時序**。
**索取該矩陣之必要性因而更高，不是更低。**

---

## 十一、**本包是否仍有該驗而未驗者** —— 獨立判斷（不得省略）

**有，五項。**

1. **A-PMH16 是我用 block 層萃取查出來的，而 `chapter_bidirectional.py`
   的預設來源仍是 `-layout`。**
   也就是說：**該檢查此刻若重跑，查不出 A-PMH16** ——
   我把結論寫進了 `RESIDUE_VERDICT`，但產生該結論的量測不在那支程式裡。
   **這正是「宣告與實作分離」（A-PMH12 形態）**，只是這次分離的是
   「結論」與「產生結論之量測」。我依 A-PMH16(d) 未改預設（判準變更須另立條文），
   **但據實記明：現行狀態下那 15 句人讀結論之依據不可由該程式重現。**

2. **章 7／10／12 之殘餘未讀，而章 7 是 batch 1 之來源章。**
   §2.5 已具名其 FAIL。**但更該說的是**：batch 1 之 8 條 TC 全部出自
   outline 7.1～7.4 與 10.4，**而章 7 與章 10 之殘餘正是未讀的那兩章**。
   A-PMH16 之發現方式證明「殘餘裡會有東西」。**章 7 尤其該先讀。**

3. **`tsv_vs_pdf.py` 之 120 字元截斷，我具名了但沒量測其影響。**
   §6.3 說「120 字元之後未經任何比對」—— **我沒有算那是多少內容**。
   48 個 `section_title` 中有幾個實際被截？被截掉的總字數是多少？
   **這三個數字都可算，我沒算。**

4. **偽陰率 50% 是一次 N=10 之抽樣，其信賴區間我沒給。**
   5/10 之 95% 區間約為 19%–81%（Wilson），**推估之「約 16 條」
   實際上是「約 6 到 25 條」**。我在 §4.3 寫了一個點估計而未附區間，
   **那使該數字看起來比它應有的樣子確定。**

5. **R-PMH66 只施行於 `chapter_bidirectional.py` 與 `tsv_vs_pdf.py`。**
   `bidirectional_spec_diff.py`（13 包之全簿雙向 diff）**仍以 6-gram
   30% 門檻自動判定**，而它正是漏掉 A-PMH16 的那一支。
   **該支未依 R-PMH66 改造，亦未於本包被停用或標註。**
   這是 R-PMH62 之同型 —— 立了條而未回頭套用於它所指認的那個對象。

---

## 十二、建議之 commit 與 pathspec（**不執行**）

**訊息**：

```
feat(power_moding): package 18 — chapter 9/11 verbatim verify, A-PMH16 timing omission, doc-sync anchor on threshold table
```

**pathspec（10 路徑，R-G12 —— 逐一具名）**：

```
git commit -- \
  features/power_moding/ANOMALIES.md \
  features/power_moding/RULINGS.md \
  features/power_moding/framework.md \
  features/power_moding/docs/INDEX.md \
  features/power_moding/docs/handoff/18_break_the_circle.md \
  features/power_moding/docs/upstream/18_break_the_circle.md \
  features/power_moding/scripts/challenge_rulings.py \
  features/power_moding/scripts/chapter_bidirectional.py \
  features/power_moding/scripts/check_granularity.py \
  features/power_moding/scripts/tsv_vs_pdf.py
```

### R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 本包所改之他 feature 檔案 | **無** |
| `scripts/new_feature.py`／`docs/runtime/`／`PROFILE_INTEGRATION.md` | **未動** |
| 工作簿寫回 | **無** |
| `generated/batch01.json` | **未動** |
| `framework.md` 之改動 | **僅門檻節之 SHA256 行**（`> 產生時之程式 SHA256：` → `> 門檻表 SHA256：`），門檻值一字未變 |
| 暫時檔 | `scripts/_docsync_probe.py` 於 must-hit (b) 中建立後**即刪**，未留檔（`git status` 可證） |
| 已執行之 git 狀態變更指令 | **無** |
| 併行 session（`vehicle_setting`）之檔案 | **未動** |

---

## 十三、待 Pei

| # | 事項 | 阻斷 |
|---|---|---|
| 1 | **三筆 DR 之發出** —— **第六度重申**；DR-PMH2 本輪因 A-PMH16 而理由更強 | **DR-PMH1 阻斷交付** |
| 2 | 18 之 commit 授權（10 路徑，見 §12） | 否 |
| 3 | **章 7／10／12 之殘餘人讀**（§11 第 2 項 —— 章 7 是 batch 1 之來源章） | **建議 Phase 5 前** |
| 4 | `chapter_bidirectional.py` 之預設來源是否改 block 層（判準變更，須立條） | Phase 5 |
| 5 | `bidirectional_spec_diff.py` 是否依 R-PMH66 改造或停用（§11 第 5 項） | Phase 5 |
| 6 | 17 §5.4 其餘五項之處置 | Phase 5 |
| 7 | Q10、`PROFILE_INTEGRATION.md` | 否 |
