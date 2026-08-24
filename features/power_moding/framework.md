# framework — FW036 Power Moding HMI（Layer 1 / 2 / 3）

- 產出日：2026-08-24（下放包 06 步驟 3）
- 資料來源：`data/layer3_sections.tsv`（48 leaf，執行層 05 包產出）
- Layer 2 提案來源：下放包 06 §5，**經執行層以 TSV 機器複算，48/48 相符、
  各 Test Set 計數與 §5.1 逐項相符、R-G10 餘數 0**
- **狀態：未定版。** Test Set #2 之名為 `<PENDING Q11>`，待 Pei 裁定（06 §5.4）

---

## Layer 1 —— Test Group

**`Disclaimer screen`**（R-PMH13，Pei 2026-08-23 核可）

⚠ **R-PMH18** —— `screen` 為**小寫 s**，為交付夾名之原樣。
與 `tc_id` 之 `DisclaimerScreen`（大寫 S）**刻意不同，不得統一**。

依據：四份已交付件之 G 欄實測 4/4 皆為交付夾名（06 包前之 03 包 §5）。
**非規格模組名** —— R-PMH2 之後半已撤回。

---

## Layer 2 —— Test Set（8 個，**未定版**）

| # | Test Set | leaf | Layer 3（規格章節） | 主要 FROP |
|---|---|---:|---|---|
| 1 | **`Splash Screen`** | 3 | 7.1, 7.9 | Customizable Splash Screen / Animations(3) |
| 2 | **`<PENDING Q11>`** | 7 | 7.1, 7.2, 7.3, 7.4, 10.4 | Disclaimer screen(7) |
| 3 | **`Startup Animation`** | 9 | 7.5, 7.5.1, 7.6, 7.7, 7.8 | Customizable Splash Screen / Animations(9) |
| 4 | **`Startup Sounds`** | 6 | 8.1, 8.2, 8.2.1, 8.2.2, 8.2.3, 8.3 | Audio Management(6) |
| 5 | **`Power Transitions`** | 7 | 7.1.1, 9.1, 10.5 | Power Management(3)／FOTA Via Wi-fi(2)／WiFi(1)／EV/PHEV Pages(1) |
| 6 | **`Power Off Behavior`** | 8 | 10.1, 10.2, 10.3, 10.4, 10.6, 10.7 | Bluetooth(3)／Rear View Camera(2)／Climate Control(2)／e-call (private)(1) |
| 7 | **`Voice Assistant Key`** | 5 | 11.1 | Steering Wheel Controls(5) |
| 8 | **`Off Road Plus`** | 3 | 12.1, 12.2, 12.3 | Power Management(2)／Audio Management(1) |

**48 = 3 + 7 + 9 + 6 + 7 + 8 + 5 + 3，R-G10 餘數 0。**

### 三處切法之依據（06 §5.3，執行層複驗相符）

1. **7.1 之五個 leaf 拆入兩個 Test Set**（`001-01/02` → Splash、
   `001-03/04/05` → #2）。依據為 **037 `FROP` 欄之既有分群** ——
   上游 RD 之切法，非 TC 作者重新分解（canon §8.2）。
   TSV 複驗：`001-01/02` 之 FROP 為 `Customizable Splash Screen / Animations`、
   `001-03/04/05` 為 `Disclaimer screen`。
2. **10.4 之兩個 leaf 拆入兩個 Test Set**（`022-01` → Power Off Behavior、
   `022-02` → #2）。同上，依 FROP。
   TSV 複驗：`022-01` 為 `Climate Control`、`022-02` 為 `Disclaimer screen`。
3. **章 9 之五個 leaf 全歸 `Power Transitions`**，雖其 FROP 有四值 ——
   因同屬 9.1 一節、共用「IGN OFF 時之 popup 與 Power Accessory Delay」
   之同一觸發情境（canon §4.2「同一 Test Set 應共用 setup 與 UI 進入路徑」）。
   TSV 複驗：9.1 之 5 leaf 之 FROP 為 Power Management／FOTA Via Wi-fi(2)／
   WiFi／EV/PHEV Pages，**pdf_page 皆為 p9**。

### ⚠ Test Set #2 之命名待裁（Q11，**阻斷 Layer 2 定版**）

canon §4.2 明訂 Test Set 不得重複 Test Group 之字樣，而 Layer 1 為
`Disclaimer screen`、提案之 #2 為 `Disclaimer Screen` —— **字面重複**。
三案（甲 `Disclaimer Screen`／乙 `Acceptance Screen`／丙 併入 Splash Screen）
見下放包 06 §5.4。**本檔不預填，記 `<PENDING Q11>`。**

---

## Layer 3 —— 規格章節對照

Layer 3 取**規格自身之 section id**（canon §4.1.1），不自創標籤。
全表見 `data/layer3_sections.tsv`（48 列 × 7 欄）。章層對照：

| 章 | 章標題（SYS1 `Outline Number` 之 Description 逐字） | leaf | PDF 頁 |
|---:|---|---:|---:|
| 7 | `Startup` | 19 | p8 |
| 8 | `Starup R1Low Only` | 6 | p8 |
| 9 | `Power Moding` | 5 | p9 |
| 10 | `Additional Power Moding Behavior Notes:` | 10 | p10 |
| 11 | `VR HARD KEY FOR SIRI/NON-NATIVE VOICE ASSISTANTS` | 5 | p10 |
| 12 | `Power Moding – Off Road+` | 3 | p11 |

**未被任何 leaf 引用之 outline 23 項**見 `data/uncited_sections.tsv`
（`chapter_node` 12／`image_placeholder` 6／`assumptions` 5／**`other` 0**）。

---

## Layer 2 之 granularity 檢查（canon §4.1.3）—— **PASS**

來源：下放包 07 §三（分析層執行）。**執行層複算之數值列於「執行層複算」欄。**

**量測條件**：對象為 8 組 Test Set；分母 48 leaf；規模以 **leaf 數**計
（TC 尚未生成，不以之為據）。

| 判準 | 錨點（must-not-hit） | 分析層實測 | 執行層複算 | 結果 |
|---|---|---|---|---|
| **過細**：組數 ≈ leaf/outline 數，Test Set 欄淪為 TC ID 副本 | 組數接近 29（outline）或 48（leaf） | 8 組，8/48 = 0.17 | **8 組，0.1667** | **PASS** |
| **過細**：存在只含 1 leaf 之組 | 任一組 = 1 | 最小 3 | **最小 3**（`Splash Screen`／`Off Road Plus`） | **PASS** |
| **過粗**：存在收容簇 | 組名含 `Misc`／`General`／`Unclassified`／`Other` | 零命中 | **零命中** | **PASS** |
| **過粗**：單組吃掉過半 leaf | 任一組 > 24 | 最大 9 | **最大 9**（`Startup Animation`），9/48 = 0.1875 | **PASS** |
| **決策測試**：filter 後為有意義之簇 | 組規模落在 [2, 24] 之外 | 全落 [3, 9] | **全落 [3, 9]** | **PASS** |
| **共用 setup／UI 進入路徑** | 同組內觸發情境互不相干 | 逐組見下 | 逐組見下 | **PASS** |

**分布**：8 組／平均 **6.0**／最小 **3**／
最大 **9**／標準差 **2.1**（母體標準差）。
**無任一判準落在失敗側。**

> 分析層 07 §三記標準差 2.2（樣本標準差 `stdev` = 2.20）；
> 執行層複算之母體標準差 `pstdev` = 2.06。
> **兩者皆對，量的是不同東西**（樣本／母體），此處之 8 組為全集，
> 故以 `pstdev` 較切題。**不影響任何判準之通過與否。**

### 共用情境之逐組陳述（canon §4.2）

| Test Set | 共用之觸發情境 |
|---|---|
| `Splash Screen` | 駕駛門關閉／CAN BUS cycle 起始時之畫面呈現 |
| **#2（`<PENDING Q11>`）** | 免責畫面顯示中之呈現與互動 |
| `Startup Animation` | 動畫播放之條件、次數與跨螢幕同步 |
| `Startup Sounds` | 開機／道別音效之設定與音量 |
| `Power Transitions` | IGN／電源狀態轉換時之行為 |
| `Power Off Behavior` | Power Button Off 狀態下之他功能介入 |
| `Voice Assistant Key` | VR 硬鍵長按 |
| `Off Road Plus` | Off Road+ 硬控之按壓 |

### ⚠ 本檢查之限制（分析層 07 §三明載，執行層照錄）

**它驗的是 leaf 分布，不是 TC 分布。** TC 生成後若某組 TC 數暴增
（例如 `Startup Animation` 之 9 leaf 展開為 30+ 條），**granularity 須重驗**。
**列為 Phase 4 之複驗項。**

---

## 未決與待驗

| 項 | 狀態 |
|---|---|
| **Q11** —— Test Set #2 之命名 | **阻斷 Layer 2 定版** |
| **A-PMH13** —— `SWE1-HMI-PM-028`（12.2）指向 CFTS009 | 見 `ANOMALIES.md`；`features/power` 之涵蓋查證見上繳 06 §4 |
| A-PMH03 —— outline 7.1 之重排 | Phase 4 指名複核（該節 5 leaf，分屬 Splash 2 ／ #2 3） |
| A-PMH04 —— 6 則圖片佔位 outline | Phase 4；**48 leaf 無一落在 p3–p7**，不阻斷 |
| **granularity 之重驗** | **Phase 4** —— 本檢查驗的是 leaf 分布；TC 生成後須以 TC 分布重驗 |

