# 上繳包 46 —— T65 執行結果（下放包 53）

- 日期：2026-08-30｜方向：執行層 → 分析層
- 對應下放包：`53_embedded_objects.md`
- **T65b 之複查結果為零，且其零比「未曾發生」更強** —— §1
- **⚠ `4908702` 之四個門檻，037 自身早就有** —— §3，本輪最該看的一項

---

## 1. T65b —— 錨點池複查（本輪核心）

**六個 ObjectID 於 `word/document.xml` 之出現次數皆為 0。**

| ObjectID | docx 內文 | `ANCHOR_POOL.md` | 88 個 TC 之 `specification_reference` |
|---|---:|---|---:|
| `4907974`／`4907975`／`4907976`／`4907977`／`4907980`／`4908702` | **各 0** | **六者皆未收** | **各 0** |

（語料為 `…CFTS_57 Reflash_20251202-2111.docx`，sha256 `9aa9400b…`；
全庫 grep 亦僅命中下放包 53 自身。）

**§2.2 之風險不成立，惟其不成立之理由與所預期者不同**：
不是「曾經可能錨錯而恰好沒有」，是**這六個 id 根本不在錨定所據之語料裡**。
其號段確實落在池之範圍（`4907230`–`4915105`）內，**而號段內不等於語料內**。

> **其真正之後果不在錨，在覆蓋**：路徑 A 之語料為 docx 之文字，
> **六張圖之內容從未進入語料，連其 ObjectID 都不在文字中**。
> 故一列若其正解係某張圖所載，**路徑 A 在原理上找不到它，機制 3 也不會攔它** ——
> 它不是「分數低」，是**不在候選集合中**。已記入 `ANCHOR_POOL.md` 附記（R-G8）。

---

## 2. T65a —— 六物件之 intake

轉檔腳本 `scripts/rtf_wmf_png.py`；輸出 `inputs/cfts057_objects/`（gitignored）。
**⚠ 本機無 `libreoffice` 之名，實際可用者為 `/opt/homebrew/bin/soffice`**（腳本已內含候選表）。

| ObjectID | RTF (B) | WMF (B) | PNG | RTF sha256（前 16） |
|---|---:|---:|---|---|
| `4907974` | 4,831,792 | 714,346 | 1588×2246 | `8e47beaf4451a506` |
| `4907975` | 3,499,630 | 520,360 | 1588×2246 | `eacfb7f3bfd92dba` |
| **`4907976`** | 11,239,556 | 1,667,132 | 1588×2246 | `8ff573127434465c` |
| **`4907977`** | 11,239,556 | 1,667,132 | 1588×2246 | `8ff573127434465c` |
| `4907980` | 3,980,478 | 544,472 | 1588×2246 | `7eeb022d62cece22` |
| `4908702` | 283,831 | 20,618 | 1588×2246 | `1f1633d8f632ec2c` |

### 2.1 `4907976` 與 `4907977` —— **在 RTF 層就已同一**

**二檔之 sha256 逐 byte 相同**，其 WMF 與 PNG 自然亦相同
（PNG sha `2e8b0d8d3e68f4d7…`）。下放包令「實測 PNG 是否逐 byte 相同」，
**其結果在做之前就已由 RTF 之 sha 決定** —— 記為**同一張圖掛了二個 ObjectID**。

### 2.2 二個未轉物件之內容（分析層原記為「未轉」）

- **`4907976`＝`4907977`**：OTA client 架構圖 —— `Vehicle Manager`（含 `Push Handler`／
  `Vehicle Integration Layer`）→ `Download Manager`（`Download Agent`）→
  `Deployment Manager`（`Deployment Agent`／`Installer Handoff`），
  右側 `HMI` 縱貫三層，下方 `Individual Update Agents and Component Handlers`
  （`HU Update Agent`／`ECUs w/ Update Agent`／`Map Updater` 等）。**無數值**。
- **`4907980`**：**UDS `Pre-Program Sequence`（Functional/Global Messages）** ——
  `Diagnostic Session Control: Extended Diag Session $10 83` →
  `Control DTC Setting: DTC Setting Type=OFF $85 82` →
  `Routine Control: Disable Fail Safe Reaction = $31 81 FF 05` →
  `Communication Control: Disable Message Trans = $28 81 01`。
  **⚠ 該圖本身是被截斷的**（其流程於 `Communication Control` 之後仍有箭頭，
  而圖框在此切斷）—— **其為嵌入之點陣截圖，不是完整流程**。

---

## 3. T65c(ii) ＋ 一項未被要求而必須報的發現

### 3.1 ⚠ **`4908702` 之四個門檻，037 自身早就有**

複查全 311 列所得：

| 037 列 | 組 | 門檻 |
|---|---|---|
| `003`／`006` | `FOTA Overview` | `no FOTA data is received for **5 consecutive minutes**` |
| `004` | `FOTA Overview` | `not completed within **7 ignition cycles**` |
| `007` | `FOTA Overview` | `download attempt count is greater than or equal to **7**` |
| `008` | `FOTA Overview` | `cannot download FOTA package over Wi-Fi for **7 consecutive days**` |
| `057` | `Wi-Fi Download` | `session duration exceeds **30 minutes**` |
| `043`／`054` | `Wi-Fi Download` | `within **15 seconds**` |
| `065` | `Wi-Fi Download` | `**5 consecutive** Wi-Fi connection attempts` |
| `069` | `Wi-Fi Download` | `$IBS_SOC$ > [**65**]` |
| `071` | `Wi-Fi Download` | `unsuccessful within **3 minutes**` |

> **故該圖之價值不是「本 feature 至今無值，現在有了」** ——
> 5 分鐘與 7 於二個獨立來源一致，**其價值是互為佐證**（強化 R-SU42(b) 之來源）。
> **下放包 53 §2.1 之立論須據此修正**：無值的不是本 feature，
> **是我們至今起草的那幾組**（`Silent Update`／`Update Policy`／`ROV`）。
> **有值的那組（`FOTA Overview`／`Wi-Fi Download`）我們一列都還沒起草** ——
> 這正是上繳包 44 §7 所報之偏向，**其第二個可見證據**。

### 3.2 ⚠ 二來源就 `30 分鐘` **不一致**，列待裁

| 來源 | 30 分鐘之起點 |
|---|---|
| 037 `057` | session **duration** exceeds 30 minutes **during the current ignition cycle** |
| `4908702` | `T = 30 minutes **after timed mode has expired**` |

**同一個 30，起算點不同 —— 台架上是二個不同的等待。**
起草 `057` 之 TC 前須先裁其一，**不得因「都是 30 分鐘」而併為一事**。

### 3.3 現有 TC 中因無門檻而迴避數值者 —— **無一列落在 Wi-Fi 下載路徑**

| TC | 037 列 | 組 | 迴避之處 | 落在 Wi-Fi 下載路徑？ |
|---|---|---|---|---|
| `010` | `181` | `Silent Update` | `immediately after download` 不可量，掛 `PENDING` | **否** |
| `034`／`035` | `100` | `ROV Installation` | 彈窗回應計時器，只能寫 `until it closes` | **否** |
| `060` | `028` | `Update Policy` | 一週之等待不可觸發（第四型） | **否** |

**故 `4908702` 之門檻救不到任何一列現有 TC**，其作用全在未起草之 `FOTA Overview`
與 `Wi-Fi Download`。（本項與落檔驗證時之預判一致，現為實測。）

---

## 4. T65c(i) —— `Wi-Fi Download`（29 列）之三軸

| 軸 | 數 | 對照 |
|---|---|---|
| **105 列** | **5／29（17%）** | 母體 33%；上輪二組為 25%／37% |
| **GT-A1 已裁之錨** | **0** | 錨定風險全落在機制 1／2／3 |
| **機制 3 攔下** | **6／29**（`056`／`059`／`061`／`065`／`067`／`070`；門檻 0.2672） | 高於上輪各組 |
| **HMI／Service** | 12／17 | — |
| **自帶門檻之列** | **6／29**（`043`／`054`／`057`／`065`／`069`／`071`） | **本 feature 至今數值最密之組** |

**評語**：其 105 比率是目前所見最低（17%），**而其錨定風險是最高的一組**
（GT 0 列、機制 3 攔 6 列）—— **三軸在本組首次互相衝突**，
不像前幾組那樣三軸同向。**若下批取本組，其困難會從「觀測」移到「錨定」。**

---

## 5. T65d／T65e

- **DR-SU4 → v2**：請求 2 **縮小至二重範圍**（限 Wi-Fi 下載路徑、限「下載 session 之終止時點」），
  **維持 OPEN**；`DATA_REQUESTS.md` 增 §DR-SU4 詳，
  `docs/upstream_requests/DR-SU1_SU2_request.md` 增 §3B.2a addendum（含 3.2 之不一致）。
  **未逕自把 Wi-Fi 路徑之值外推到 USB／cellular**（IN §8.4.1）。
- **T65e**：`RECON.md` 記明 9 個 CFTS 嵌入物件目錄之存在與本 feature 之實測，**只記不處理**。

**未結 DR：5 筆**（DR-SU1／DR-SU2 v3／DR-SU3／**DR-SU4 v2**／DR-SU5）。
**全案 `PENDING` 94 行、可交付候選 51 列，本輪未動任何 TC，lint 不需重跑。**

---

## 6. 獨立自評（入 BACKLOG）—— 53 §五-6：圖中之正解，路徑 A 找不到，此類列有多少

**答：其母群不可由語形估計，理由與第四型相同；但方向可以反過來，而反過來是有界的。**

**(甲) 為何不可估。** 要估「正解在圖裡的列」，等於要偵測**文字裡沒有的東西**。
語形判準測的是文字，**而此類列之特徵恰是其文字不足** ——
同 R-SU39(e) 對第四型所記：**不可由語形估計**。

**(乙) 可測者只有一個弱下界，且其弱要說明白。** 我掃了 311 列與三張圖之主題重疊：

| 主題 | 命中列數 |
|---|---:|
| UDS／診斷服務碼（`4907980` 之內容） | **1**（`198`） |
| flash／programming 序列 | 7 |
| session 流程節點（inactivity timer／resume mode／timed mode） | 6 |

**這 14 列是「文字裡提到了圖所畫之事」者，不是「正解在圖裡」者。**
真正危險的列**不會提**，**故此數是可見度之下界，不是母群之估計。**
（`4907980` 之診斷碼只對應到 1 列，**而該圖有四個服務碼與一段被截斷的流程** ——
其資訊量遠大於它在 037 文字中的投影。）

**(丙) 反方向是有界的，而且本輪已示範。** 由列找圖不可窮舉（311 列 × 未知圖），
**由圖找列可以** —— 圖只有 6 張，逐張問「它所載之事對應到哪些列」。
本輪對 `4908702` 做了：**對應到 9 列，其中 1 列（`057`）與其不一致**。
**成本是 6 張圖，收穫是一個可列舉的清單。**

**(丁) 建議（不裁）**：把「**由圖找列**」立為 intake 之一個固定步驟 ——
凡新素材為圖者，逐張出其「所載之值／流程」與「其對應之 037 列」二欄，
**併記其與文字來源一致或不一致**。**不一致者即為 DR 之材料**（如 3.2 之 30 分鐘）。

**(戊) 一項自陳**：這六個物件在 `inputs/` 裡放了兩天（檔案時間 08-28 01:27），
**而我在下放包 53 之前沒有看過它們**。我的 intake 只掃了 docx，
**因為前幾包令我掃的是 docx**。**這不是分析層漏令，是我把「素材」等同於「被指定之素材」。**

---

## 7. 待裁事項

| # | 事項 | § |
|---:|---|---|
| 1 | **`30 分鐘` 之二來源不一致** —— 起算點須裁其一 | 3.2 |
| 2 | **下放包 53 §2.1 之立論須修正** —— 無值的不是本 feature，是已起草之那幾組 | 3.1 |
| 3 | `4907980` 為**被截斷之點陣截圖**，其完整 Pre-Program Sequence 是否須向上游索取 | 2.2 |
| 4 | `Wi-Fi Download` 三軸**互相衝突**（105 最低而錨定最險），是否仍照現行優先序取為下批 | 4 |
| 5 | 「**由圖找列**」是否立為 intake 之固定步驟 | 6(丁) |
| 6 | 其餘 8 個 CFTS 目錄之處置（跨 feature，屬 Pei） | 5 |
