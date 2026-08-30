# 下放包 53 —— CFTS057 嵌入物件之發現、intake 與四門檻之落地

- 日期：2026-08-30
- 方向：分析層 → 執行層
- 前一包：`52_status_reporting.md`（T64 照跑，本包並行）
- 對應上繳：`docs/upstream/46_embedded_objects.md`
- **條文凍結維持**（43 條／留存 26）

---

## 一、新素材：CFTS057 之六個嵌入物件

**路徑**：`~/Work/02_Project_R1LR/1_Customer_Requirement/R1LR SR26 ATL-H/26PI2.5/
Reference Documents/CFTS Embedded Objects/CFTS057/`

**六個 `.rtf` 檔，其內容皆為 Visio 圖（RTF 包 WMF）**：

| 檔名 | ObjectID | 分析層已轉檢 | 內容 |
|---|---|:--:|---|
| `4907974- 4615846- …O3487_88` | `4907974` | ✅ | OTA 架構概觀（Server／Internet／HU or TBM／CAN／ECU；OTA Client Software 三元件） |
| `4907975- 4615848- …O3714_89` | `4907975` | ✅ | 端到端系統圖，11 個編號步驟（TBM Legato／HU JVM／CDN／ECU supplier 差分檔／Global PKI／`V2C API bus`） |
| `4907976- 4615845- …O3486_90` | `4907976` | ✗ | 未轉 |
| `4907977- 4615845- …O3486_90` | `4907977` | ✗ | 未轉（**與 `4907976` 同源檔名，疑同圖二個 ObjectID**） |
| `4907980- 4615844- …O3485_91` | `4907980` | ✗ | 未轉 |
| `4908702- 4615847- …O3579_92` | `4908702` | ✅ | **Wi-Fi 下載 session 流程圖 —— 含四個具體門檻** |

### 1.1 轉檢之方法（已驗證可行，執行層照做）

1. RTF 中定位 `{\pict` 群組，括號配對取其 body
2. 去控制字（`\\[a-zA-Z]+-?\d*\s?`）與非 hex 字元 → `binascii.unhexlify` → `.wmf`
3. `libreoffice --headless --convert-to png`
4. 放大 2 倍（原輸出 794×1123，直接看不清）

**注意**：檔案極大（`4907974` 為 4.83 MB，hex payload 1.4 M 字元），
`read_text_file` 不可行，**須以二進位路徑處理**。

---

## 二、`4908702` 之四個門檻 —— **本輪最重要之發現**

流程圖所載（逐字轉錄，非推想）：

| 門檻 | 原文 |
|---|---|
| **重試上限 7** | `Counter I = 0, updates and overwrites the new value of the counter with the input`；`I < 7` → 嘗試連線；`I => 7` → 於 IGN_OFF 提示使用者設定網路並重置 `I = 0` |
| **30 分鐘** | `T = 30 minutes after timed mode has expired` |
| **5 分鐘** | `T = 5 minutes since last data received` |
| **中斷之處置** | `HU shall terminate the download session for the duration of ignition cycle with increment in counter, I += 1`／`… and reset the counter, I = 0`（二分支） |

其餘流程節點：下載於 **ignition off 進入 resume mode 時啟動**；
`Check periodically the download status`；`DL complete?` → `Wait for the next
ignition_off and ask the user if they want to install the update (see HMI)`。

### 2.1 其意義

**IN §8.7.1 要求觸發／釋放門檻須為 spec 之具體值**，而本 feature 至今
**因無值而一律迴避**（`034` 只能寫 `until it closes`、`010` 之 `immediately` 掛 `PENDING`）。
**現在 Wi-Fi 下載路徑之門檻有了。**

**且其對 DR-SU4 有部分作用**：`3B.2` 稱下載階段之中斷無可判定之界 ——
而 `T = 5 minutes since last data received` **是一個可等待、可判定之界**。
DR-SU4 之請求 2 得據此縮小至 **deployment 階段**。

### 2.2 一項須先查的風險

六個 ObjectID **落在錨點池之號段內，而它們是圖不是需求條文**。
若路徑 A 曾將某列錨至其中之一，**該錨之性質與文字錨不同**，須複查。
（`4907974`／`4907975`／`4907976`／`4907977`／`4907980`／`4908702`）

---

## 三、其餘 CFTS 之嵌入物件目錄

同一路徑下另有 **8 個目錄**：`CFTS001`／`CFTS013`／`CFTS019`／`CFTS024`／
`CFTS025`／`CFTS028`／`CFTS036`／`CFTS069`。

**與本 feature 無直接關係**（本 feature 之母 spec 為 CFTS057），
**但其存在本身是一項對全案有用之事實** —— 其他 feature
（`audio_mgmt` 用 CFTS019、`vehicle_setting` 等）**可能同樣有藏著數值的圖**。

**本包只令記錄該事實**（T65e），**不令處理** —— 跨 feature 之處置屬 Pei。

---

## 四、任務（T65）

| # | 任務 |
|---|---|
| T65a | **六物件之 intake**：依 §1.1 之法全部轉為 PNG，置 `features/sw_update/inputs/cfts057_objects/`；轉檔腳本落 `scripts/rtf_wmf_png.py`。**逐檔記 SHA、原始大小、PNG 尺寸**。`4907976`／`4907977` 之同源檔名須實測其 PNG 是否逐 byte 相同 |
| T65b | **錨點池複查**（§2.2）：六個 ObjectID 於 `ANCHOR_POOL.md` 之登記型別（需求物件／章節物件／未收）；**併查**現有 88 個 TC 之 `specification_reference` 有無指向其中任一者。**有即列出並停報** |
| T65c | **`4908702` 之門檻落地**：<br>(i) `Wi-Fi Download`（29 列）之三軸盤點 —— **本組為下一批之候選**；<br>(ii) 現有 TC 中因「無門檻」而迴避數值者逐一列出（已知 `034`／`035`／`010`），**逐列判其是否落在 Wi-Fi 下載路徑**；落在者列待裁，**不逕改** |
| T65d | **DR-SU4 之更新**：請求 2 縮小至 deployment 階段，並附 `4908702` 之三個時間／計數門檻為證（下載階段已有可判定之界）。DR 文本同步 |
| T65e | **跨 feature 事實之記錄**：`SOURCE_COLUMNS.md` 或 `RECON.md` 記明「CFTS Embedded Objects 目錄下另有 8 個 CFTS 之嵌入物件，其內容可能含未見於 docx 之數值與流程」。**只記不處理** |
| T65f | git |

**T64（batch 7 含 `Status Reporting`）照跑，不因本包改期。**

---

## 五、上繳包要求（`docs/upstream/46_embedded_objects.md`）

1. **T65b 之錨點池複查 —— 本輪核心**（決定既有錨有無指向圖物件）
2. T65a 之 intake 記錄（含 `4907976`／`4907977` 之異同）
3. T65c 之待裁清單與 `Wi-Fi Download` 三軸
4. T65d／T65e／T65f 之結果
5. 未結 DR 清單
6. 獨立自評（入 BACKLOG）—— 特別回答：**六個嵌入物件之內容至今未進入任何
   錨定計算（路徑 A 之語料為 docx 之文字，圖之內容不在其中）。
   那麼一列若其正解實為某張圖所載之流程，路徑 A 在原理上就找不到它 ——
   此類列有多少，有無辦法估計**
