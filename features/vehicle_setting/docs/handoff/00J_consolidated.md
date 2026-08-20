# 00J — Vehicle Setting 現行作業依據（**合併版，唯一有效**）

分析層寫入，2026-08-20。

## 本檔之地位

`00`／`00A`～`00I` 共九份，是同一輪內逐次修正的過程記錄。**自本檔起，
它們降為證據，不再是作業依據**（不逐檔改標記，以本段為準）：

- `00` §3 之六條裁決 **R-VS1～R-VS6** 仍為權威條文，逐字有效
- 其餘各篇之結論已收攏於本檔 §2～§5
- 需要追溯某個數字怎麼量出來的 → 回去翻對應那篇

**九份互相修正是流程缺陷，不是資訊豐富。** 成因為分析層在同一輪內
邊查邊發，未在收束時合併。代價已具體發生：v1 啟動指令需攜帶一份
「已作廢陳述清單」與一條優先序鏈，長度膨脹逾倍。
**下一 feature 之對策：同一輪內之補篇不落獨立檔，直接改寫主檔並以
diff 留痕。**

---

## 1. Feature 基本事實

| 項 | 值 |
|---|---|
| Test Group | `Vehicle Setting`（R-VS3） |
| 上游規格 | CFTS044 Vehicle Controls（SR26 / 25PI3.5），`spec_mode = D` |
| 037 | **四份**（Common Features 56／HeatedSeat 99／VentedSeat 81／HSW 35）＝ **271 leaf** |
| 036 現況 | 237 列，qualifying done = **0** → **效力 BLANK**（R-VS1） |
| 覆蓋缺口 | 34 leaf 無列；且現況 1 leaf = 1 列，與 §8.2.2 相斥 |
| 錨鏈 | leaf → `SYS-RA-CFTS044-N` → SYS2 第 N 筆資料列 → 7 位數 Polarion ID → CFTS044 章節號。**245／271 解析成功**，25 有 ID 無章節，1 無 ID |
| Test Set | 四個，對應四份 037（R-VS4） |
| CAN 基線 | `PDT27_E2A_R4_BHCAN.dbc`（主）＋ `R5_FDCAN8.dbc`（FD 網段）。**同版本，不同網段**（R-VS8 改寫版） |
| 訊號權威 | LID 表 Atlantis High 欄 → DBC `VAL_` 交叉核對（R-VS9 草案） |

---

## 2. 待補之一：素材

| # | 項目 | 誰 | 影響 |
|---|---|---|---|
| **S1** | `Logical Identifiers and CAN Mapping v1.76.xlsx` 入 `inputs/` | Pei 已授權（R-VS12），待實體複製 | 訊號名與值域之第一權威 |
| **S2** | `PDT25_E3A_R4_FDCAN8_vs_R5_FDCAN8.xlsx` 入 `inputs/` | 同上 | 存證用（R4/R5 語意判準） |
| **S3** | `Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf` 自 `…/26PI2.5/HMI/` 入 `inputs/` | **Pei 已授權（2026-08-20，R-VS13）** | 16 leaf 之按鍵循環、LED 數、highlight 狀態 |
| **S4** | `PDO Theme Config V2.8.xlsx` | **不入庫（建議）** —— 經實測為 `inputs/` 已有 V3.4 之嚴格前身（見 §2.1） | 無 |

S1+S2 完成後 `inputs/` 為 14 檔；再加 S3 為 15 檔。

### 2.1 `PDO Theme Config` 之版本關係（2026-08-20 實測）

| 項 | V2.8 | V3.4（已在 `inputs/`）|
|---|---|---|
| SHA256（沙箱副本）| `0cce40e8…f899d` | —— |
| 工作表 | 3（Revision Log / PDO Themes / Splashscreen Type）| **4**（多 `R1L SR21`）|
| Revision Log 止於 | 2.8（2021-10-07）| **3.4（2023-07-02）** |
| PDO Themes 資料列 | 82 | 89 |
| 僅存於己方之主題列 | **0** | 7（Peugeot 231、Citroen 241、Opel 251、Vauxhall 252、Toyota 253、Dodge 12、SRT 177）|

**V3.4 為 V2.8 之嚴格超集**（以前四欄作鍵逐列比對，V2.8 無一列為 V3.4 所無）。

兩份對 `heated seat`／`vented seat`／`heated steering`／`mirror`／
`left side`／`right side` 之命中皆為 **0**（`icon` 各 1，為欄名）。
**二者皆不回答 Q2（PDO graphics）。**

順帶發現（**A-VS12**）：兩份之內部標題儲存格皆落後於檔名版本 ——
V2.8 之 `Revision Log!A1` 寫 `v2.1`、`PDO Themes!A1` 寫 `v2.3`；
V3.4 則分別寫 `v3.2` 與 `v3.3`。**四個標題四個版本號，無一個等於
檔名之版本**。同一形態亦見於 AMFM 之 `CIP_Radio_Tables` 與
`Market Configuration v1.6` —— **版本標籤不識別內容**（canon §5a 第 9 條）。
入庫之 PDO 相關檔一律以 SHA256 識別，不以檔名或內部標題識別。

---

## 3. 待補之二：上游（RD-1，Tier 3 送出）

| # | 問題 | 影響範圍 | 無答覆之處置 |
|---|---|---|---|
| **Q1** | `TLM HMI Document` 是哪一份？失效彈窗（`*_STATFailSts == "Fail_Present"` 時之提示）定義在何處？<br>已查：Comfort L&F 全文 `Fail` 命中 0；Pop Up List 26PI 1,344 列無此彈窗 | **16 leaf** | ER 只寫到訊號層，畫面層標 BLOCKED |
| **Q2** | `PDO graphics` 之確切文件（檔名＋版本＋日期）？<br>已入之 PDO Release PDF 車型（KX/KM74/EJ/LB）與主題（Regen/Creep）皆不符 | **1 leaf**（HSW 圖示左右駕鏡像） | 同上 |
| **Q3** | PROXI 表：`Heated_Seats`／`Heated_Seat_Levels`／`Heated_Steering_Wheel`／`DSP_SK_PRSNT` 之值域，LID 表寫 `See Proxi Table` 轉指出去 | 4 個 LID | 改採 CFTS044 內嵌值，LID 表僅佐證 |
| **Q4** | `$VC_VEH_LINE$` 之完整車型碼：LID 表列舉截斷於 `101 = WL`，而 CFTS044 所用之 `DT`／`WS`／`HDCC`／`M240` 全不在內 | **8 個引用** | 保留變數形式，不填猜測值（§8.4.1） |
| **Q5**（FYI） | `Heated_Seat_Levels`／`Heated_Seats_Levels`／`Heated_Steats_Levels` 三種拼寫；第三種在 2,974 個 LID 中無對應，確為 typo | 6 個引用 | 併入 `Heated_Seats_Levels` 處理，記 A-VS05 |

---

## 4. 待補之三：裁決（**不是文件**）

| 條 | 內容 | 阻塞 | 建議 |
|---|---|---|---|
| **R-VS7** | Comfort 43 個重疊 leaf 之委派界線 | **阻塞生成** | (a) 分層委派 |
| **R-VS9** | CAN 訊號書寫形式（LID 表為第一權威、`$var$` 僅出現於 test_item 上半段） | 阻塞 lint 定稿 | 照 00H §3 草案 |
| **R-VS10** | Pop Up List 基線版本（26PI vs Comfort/User Profiles 用的 SR24 Post 2A） | 不阻塞 | 本 feature 不引用，暫不採用 |
| **R-VS11** | LID 表 `Atlantis` 欄能否代 `Atlantis High`（27 個中 10 個空欄，全為 PROXI 類） | 影響 10 個參數之值域來源 | (b) 視為未定義，改採 CFTS044 內嵌值 |
| **R-VS8** | 已依實測改寫為「兩份 DBC 並用」 | —— | **待追認** |

---

## 5. 待補之四：待驗（執行層做，不缺任何東西）

| # | 項目 | 為何未做 |
|---|---|---|
| V1 | SYS3 SYSAD 原始二進位之複驗 | 分析層只驗了轉檔文字，15.92 MB 真檔未開 |
| V2 | 四份 037 與 036 以 `inputs/` 實體檔重測 | 分析層數字全出自沙箱副本 |
| V3 | `…/26PI2.5/HMI/` 全目錄餘數掃描（112 檔，只開了 4 檔） | 「失效彈窗不在該目錄」目前是**已知未查**，不是已查為綠 |
| V4 | LID 表之 `Usage Comment` 欄與十張車型專屬分頁 | 00G 未納入，故「Atlantis High 空欄 10 個」為上界 |
| V5 | DBC 與 LID 表之**逐屬性**比對（id／起始位元／長度／factor／VAL_） | 00H 只比名稱，同名不同定義看不到 |
| V6 | `$var$` 三來源（CFTS044／DBC／LID 表）之系統性一致性比對 | 目前只確認三項一致 |

V1～V6 全在 `00I` 之作業清單內（W-3／W-13／W-14／W-15／W-8），
**不需要任何新素材，也不等任何裁定。**

---

## 6. 一句話總結

**缺的檔案只有 S3 一份；其餘全是「要問上游」（Q1–Q5）、「要你裁」
（R-VS7/9/10/11）、或「執行層跑一輪就有」（V1–V6）。**
