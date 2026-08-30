# 上繳包 70 —— T82 執行結果（下放包 70，全域線）

- 日期：2026-08-30｜方向：執行層 → 分析層
- 對應下放包：`docs/fw036/handoff/70_wrapup1.md`
- **⚠ 037 覆蓋 311／311 = 100%｜未起草 0 列｜帶 `PENDING` 之 TC 195／317**
- **⚠ 盲測失效，其成因在我方之抽樣（§3）；⚠ DR 請求文確實過期，已更正（§5）**

---

## 1. T82a —— 起草完成，**037 覆蓋 100%**

| 批 | 內容 | TC | `PENDING` | 可交付 |
|---|---|---:|---:|---:|
| batch 21 | `Bearer Selection` 16 列 | 16 | 49 | **0** |
| batch 22 | **`057`** | 1 | 5 | **0** |

**batch 21 之可交付 0／16 與上繳包 68 §1 之預估相符**（其為預估之實現，非巧合 ——
該預估係逐列讀其 037 原文所得）。

**`057` 依下放包 70 §3.2 起草**，其判定核心掛 `PENDING: DR-SU4`：
**30 分鐘之起算點於 037（session 起）與 `4908702`（timed mode 到期起）不一致，我方無權擇一。**

**lint**：batch 21 A..W 全 0（`U=49`、`I-cross=16`）；batch 22 全 0（`U=5`，首版 `T=1` ——
我在 `PENDING` 說明中用了全形破折號，已改為冒號）。
**遮蔽測試**：全簿 **317 TC／50,086 組**，逐字相同 **1 組**（已知之 `006`／`061`）。

### 1.1 **三數**

| | 值 |
|---|---|
| **037 覆蓋率** | **311／311 = 100%** |
| **未起草之列數** | **0** |
| **帶 `PENDING` 之 TC** | **195／317**（可交付候選 **122**） |

---

## 2. T82d —— `PENDING` 清單（**交付說明之附件**）

**落 `features/sw_update/docs/PENDING_LIST.md`**，逐列記 TC ID／037 列／Test Set／DR／型別／行數。

| 型別 | TC | 行 |
|---|---:|---:|
| 第二型（觀測手段） | 81 | 268 |
| 第四型（觸發手段） | 30 | 143 |
| 切分型（統攝／重複表述） | 27 | 104 |
| 判準型（能力／全稱） | 17 | 53 |
| 車外表徵（伺服器側） | 13 | 57 |
| 中斷處理之判準 | 11 | 36 |
| 安全與認證之觀測 | 11 | 34 |
| 第三型（區辨手段） | 5 | 17 |
| **合計** | **195** | **712** |

| DR | 阻斷之 TC |
|---|---:|
| **`DR-SU2`** | **151** |
| `DR-SU3` | 27 |
| `DR-SU6` | 17 |
| `DR-SU4` | 11 |
| `DR-SU7` | 11 |
| `DR-SU1` | 3 |
| `DR-SU5` | 1 |

---

## 3. T82c —— KEY 對照：**盲測失效，而其成因在我方之抽樣**

**KEY**（本包框界裁定後始開）：**有建議＝`R-POP12`／`R-POP13`／`R-VS37`**；
無建議＝`R-TM40`／`R-POP18`／`R-VS36`。

### 3.1 ⚠ **三條有建議者，其建議界全部是 0**

| 條 | 機器建議 | 分析層之裁定 |
|---|---|---|
| `R-POP12` | **前 0 個非空行** | **全 14 行皆規範** |
| `R-POP13` | **前 0 個非空行** | 二框（144 ＋ 155–174） |
| `R-VS37` | **前 0 個非空行** | **不裁框界 —— 其為 `superseded`，不該在清單裡** |

> **處置組拿到的「建議」是空的。**
> **一個建議界為 0 之提示，其內容等於「本條沒有條文」** ——
> **而三條之裁定分別是 14 行、二框、與「不該在此」。**
>
> **故本次盲測量不到錨定效應，不是因為沒有效應，是因為對照設計裡的「處置」不存在。**

### 3.2 其成因：**我方之抽樣把六條全取自甲型**

**F1 餘 1 條（`R-TM40`，非甲）＋ F2 首批 5 條（全為甲型）** ——
**而甲型之定義即「首行即訊號」，其機器建議必為 0。**
**隨機三三分之後，處置組恰好三條全是甲型。**

**其為設計缺陷而非運氣不好**：**我在出材料時已知 F2 全為甲型**（上繳包 66 §1 之表），
**卻仍以「F1 餘 1 ＋ F2 首批」湊足六條** —— **當時沒有問「處置組會拿到什麼」。**

### 3.3 答 §六-6：無效樣本之判準

**分析層所問者（`R-POP12`／`R-POP18` 全節皆規範 → 建議無論為何皆不影響裁定）成立，
而本輪之實況更廣**：

```
無效樣本之判準有二，二者皆須排除：
(1) **正解為「全節」者** —— 其裁定不受任何建議影響（`R-POP12`／`R-POP18`）
(2) **建議界為 0 者**    —— 其「處置」無內容，與無建議者不可分（本輪三條全中）

**有效樣本須為：建議界 > 0，且其正解不等於全節。**
**本輪六條中，符合者 0 條。**
```

**建議之重做**：自 **`pending-frame` 17 條中之非甲型者**取樣（其建議界 > 0），
**且先排除節內全為規範者**（可由「節內有無 `>` 或次級標題」機器初判）。
**⚠ 惟其母群現僅 17 條，且非甲型者更少** —— **本檢定之樣本量可能已不足，
其是否值得再做，屬分析層之判斷。**

---

## 4. T82b —— 21 組之組名相符度候選表（**出候選，不判**）

**落上繳包附件（下方）**；抽法為**依 037 列序取每組之第 1、中位、末列**，不挑。

**⚠ 執行層僅陳一項機器可判之事實**（非判定）：
**下列各組之抽樣標題中，含他組組名之關鍵詞者**：

| 組 | 其抽樣列之標題含 | 
|---|---|
| **`Bearer Selection`** | `301` **Server Authentication**、`308` **Security Compliance** —— **二者皆非 bearer** |
| `Session Flows` | `290` **OTA Server Configuration** Rollback |
| `Client Architecture` | `286` **OTA Flow Status Reporting**（`Status Reporting` 為另一組之名） |
| `Update Policy` | `010` **Fallback to TBM Network**（`HU FOTA via TBM` 為另一組之名） |

**其餘 17 組之抽樣標題未含他組關鍵詞。**

| 組（列數） | 抽樣三列之 `Requirement Title` |
|---|---|
| **HU FOTA via TBM**（36） | `215` Trigger TBM Update Check on Scheduled Event<br>`233` Display Estimated Time for TBM Software Update<br>`250` Trigger Vehicle Initiated Session on ECU Configurati |
| **Client Architecture**（35） | `195` Separate OTA Client from Physical Bus Communication <br>`255` SWMC Download Manager Integration<br>`286` OTA Flow Status Reporting |
| **Wi-Fi Download**（29） | `039` Provide Enable Wi-Fi Download Option on Wi-Fi Downlo<br>`054` Switch from Client Mode to Host Mode Within 15 Secon<br>`071` Switch to Next Wi-Fi Network After Connection Timeou |
| **Deployment Flow**（26） | `138` Extract Deployment Package and Route Component Packa<br>`151` Block Installation During Active Download Session<br>`167` Handle Installation Failure and Unrecoverable State  |
| **ROV Installation**（20） | `088` Display Success Pop-up in Body ON Mode<br>`100` Handle Timeout or Cancel Action for Install Decision<br>`109` Interrupt Pre-Installation Flow on Status Change |
| **Interruption Handling**（19） | `313` Software Update Error Handling Coordination<br>`323` Concurrent NIA Handling<br>`360` Download Interruption Recovery |
| **Update Policy**（17） | `010` Fallback to TBM Network for FOTA Download<br>`027` Prevent Rejection of Critical Update and Delay Insta<br>`037` Enforce Critical Update Flow with Postpone Only Opti |
| **Session Flows**（16） | `019` Restrict Embedded Modem Download Start to IGN_RUN St<br>`274` OTA Communication / Vehicle-Initiated Session<br>`290` OTA Server Configuration Rollback |
| **Bearer Selection**（16） | `292` Configurable Network Priority Support<br>`301` Server Authentication During Session Initiation<br>`308` OMA-DM Security Compliance |
| **TBM Reflash**（14） | `111` Enable TBM Update Functions Only When TBM Is Present<br>`118` Display Forced TBM Update Screen on Ignition OFF<br>`124` Clear TBM FOTA UI on No Update State |
| **Update Agent**（14） | `370` Update Deployment Method Support<br>`377` A/B Update Mechanism Support<br>`383` Deployed Software Validation |
| **Session Management**（13） | `347` Vehicle-Initiated Polling Interval Configuration<br>`353` Deployment Download Sequence<br>`369` Server-Initiated Flow Alignment with Vehicle-Initiat |
| **Silent Update**（9） | `175` Execute Silent Update Without User Interaction<br>`180` Optionally Suppress Download Confirmation Screen<br>`184` Apply Silent Update to All Session Flows |
| **Integrity Verification**（8） | `171` Verification and Validation FCA Signed Deployment Pa<br>`310` OMA-DM Message Integrity Verification<br>`338` Pre-Deployment Package Authenticity Verification |
| **Deployment Conditions**（8） | `336` OTA Update Enable/Disable Handling<br>`343` Vehicle Condition Provision<br>`346` Firmware Download Storage Allocation |
| **Status Reporting**（7） | `330` OTA Session Completion Reporting<br>`333` OTA Session Report Retry<br>`358` Update Status Reporting to SWMC |
| **FOTA Overview**（6） | `003` Terminate Wi-Fi Download Session Until Next Ignition<br>`006` Terminate Wi-Fi Download Session After Data Timeout<br>`008` Fallback to Embedded Modem After Wi-Fi Connection or |
| **Update HMI**（6） | `130` Support NAFTA Region Languages for SW Update HMI<br>`133` Display Release Notes and Interactive Links from DD<br>`136` Control Deployment Rejection Based on OTA Flags |
| **USB Update**（5） | `080` Receive Firmware Update from TBM via USB Connection<br>`082` Prioritize FOTA Update When Multiple Update Methods <br>`084` Prioritize FOTA Update When Multiple Update Methods  |
| **Telematics Client**（5） | `363` TC Communication Establishment<br>`365` Server-Initiated Session Handling from TC<br>`367` Server-Initiated Session Forwarding from TC |
| **Configurable Parameters**（2） | `126` Support Remote Configuration of OTA Flow Parameters<br>`128` Parse Download Descriptor XML and Extract Deployment |

---

## 5. §五-5 之答（**其為本輪第二個發現，且我先自查了它**）

**問：七筆 DR 之請求文係逐輪累積，其最早者成文於 8/28 —— 其所述之現況是否仍與今日相符？
若不符，送出一份過期之請求，其正當性與未送出有何不同？**

### 5.1 **不符，且其差距是一個數量級**

`docs/sw_update/docs/upstream_requests/DR-SU1_SU2_request.md` 之標頭原載：

> **Open items**: DR-SU1 (1 requirement), DR-SU2 v3 (4 sub-requests), DR-SU3 (2 requirements),
> **DR-SU4 (6 requirements)**, DR-SU5 (1 requirement + 1 facet)

| | 請求文所載（8/28–8/29） | **今日實測** |
|---|---|---|
| DR 筆數 | **5** | **7**（DR-SU6／DR-SU7 為其後所開） |
| DR-SU2 所擋 | 「5 列＋106 母群」 | **151 個 TC** |
| DR-SU4 所擋 | 6 列 | 11 個 TC |
| 全案 `PENDING` | 未載 | **195／317 TC、712 行** |

### 5.2 **其正當性與未送出之別 —— 我方之判斷**

> **一份過期之請求，其正當性不是「比未送出好一點」，而是**可能更差**。**
>
> **未送出者，收件方知道自己沒收到。**
> **送出一份說「擋六列」之請求，收件方會據其規模排優先序** ——
> **而其真實規模為 195 個 TC。** **其後果是該請求被排在它不該在的位置，
> 而我方仍可宣稱「已問」。**
>
> **故 §2.1(c) 之拘束須加一句**：**「已問」之認定以請求文所載之現況為準；
> 現況已變而未更新者，視同未問。**

### 5.3 **已更正**（不待裁）

請求文之標頭已改為七筆 DR 之現況表，並明記：

> **當這份請求首次寫成時（2026-08-28），它描述的是五筆資料請求擋住少數幾個測試案例。
> 起草現已完成全部 311 列需求，而同樣那幾筆請求所擋住的份量，遠大於本文其餘各節所述。**

**其餘各節之細節不動**（其於仍正確處為正確）；**凡其所述之規模較小者，以標頭之表為準。**

---

## 6. 獨立自評

### 6.1 **本輪我做得到而沒做的檢定**（固定項）

| # | 我能做什麼 | 它可能否證什麼 | 未做之理由 |
|---:|---|---|---|
| 1 | **對七筆 DR 之請求文逐筆核其現況**（本輪只核了標頭之 Open items） | 各節內文可能仍有過期之數（如 DR-SU2 §3A 之「106 母群」） | **本輪只改了標頭 —— 其餘各節之核對未做**，其為 T83（DR 定稿）之工作 |
| 2 | 以 `PENDING_LIST` 之型別分布，回測各型之判定是否一致（同型之列其 `PENDING` 措辭是否可互換） | 可測我方型別判定之內部一致性 | 成本中等；**未被要求** |
| 3 | 對 122 個可交付列跑一次「若其所引之 DR 明日全數回覆，有幾列會需要改寫」 | 可估回覆到達時之返工量 | **其需假設回覆之內容，我不宜代擬** |

### 6.2 一項自陳

**§3.2 之盲測抽樣缺陷，是我在開 KEY 之後才發現的** ——
**而它在出材料時就可以發現**（我當時手上就有「F2 全為甲型」那張表）。
**其與 B-44（用組名代替組之內容）同族**：
**我用「六條」這個數代替了「六條是什麼」。**

---

## 7. 待裁事項

| # | 事項 | § |
|---:|---|---|
| 1 | **`PENDING` 清單之型別分類** —— 追認其八類 | 2 |
| 2 | **DR-SU7 已開**（15 列，其中 11 個 TC 現引之）—— 追認 | 2、DR |
| 3 | **盲測失效之處置** —— 重做（母群僅 17 條，樣本量可能不足）或結案 | 3.3 |
| 4 | **§2.1(c) 加一句**：「現況已變而未更新之請求，視同未問」 | 5.2 |
| 5 | 21 組候選表之相符度判定（**執行層不判**） | 4 |
| 6 | DR 請求文其餘各節之現況核對（T83） | 6.1 |

**全案：317 個 TC｜`PENDING` 712 行／195 個 TC｜可交付候選 122 列｜037 覆蓋 100%｜DR 7 筆。**
