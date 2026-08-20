# W-13 — 26PI2.5/HMI 全目錄餘數掃描（R-G10）

目標：以餘數驗證 00D 之結論「失效彈窗與圖示左右駕鏡像不在該目錄」。
**唯讀，未複製任何檔案入 `inputs/`。**

## 掃描條件（canon §5a 條 4／5）

- 目錄：`…/1_Customer_Requirement/R1LR SR26 ATL-H/26PI2.5/HMI/`
- 母體：**107 檔**（PDF 89／XLSX 15／PPTX 3）—— 00D 所記之「約 112」為目測，非計數
- PDF：`pdftotext -q`；XLSX：`openpyxl` 全分頁全儲存格；PPTX：全 `*.xml` part
- 關鍵詞：`Fail_Present`／`STATFailSts`（**區分大小寫**）、
  `Heated\s+Steering\s+Wheel\s+Icon`（**不分大小寫**）、`Left Side`／`Right Side`（**區分大小寫**）
- **首版無詞界** —— 詞界之補驗見 §3

## 結果 —— **相關命中 0**

| 關鍵詞 | 命中檔 | 總命中 | 判定 |
|---|---|---|---|
| `Fail_Present` | **0** | 0 | —— |
| `STATFailSts` | **0** | 0 | —— |
| `Heated Steering Wheel Icon` | **0** | 0 | —— |
| `Left Side` | 2 | 4 | **全為誤命中**，見 §3 |
| `Right Side` | 2 | 4 | **全為誤命中**，見 §3 |

**→ A-VS10 之結論成立。** 00D 之「已知未查」轉為「**已查為綠**」：
CFTS044 所指之 `TLM HMI Document` 與 `PDO graphics`，其失效彈窗與左右駕鏡像
**不在該目錄之任何一檔內**。DR-5-B 維持開啟，走 RD-1 提問。

## 1. 一檔初判「未解析」，經跨形式處理後讀出（canon §9.1 第 6 項）

`Core HMI Logic and Flow R1 SR24 Post 2A (February 2 2023).pdf`
（5,705,314 bytes，21 頁，`Power PDF Create`，40 張影像）
—— `pdftotext` 僅得 **21 字元**，初判**未解析**（§5a 條 12：不猜）。

**此檔為 00D §6-1 具名之候選之一**，故不能以「未解析」收尾。逐步處理：

| 嘗試 | 結果 |
|---|---|
| `pdftotext` | 21 字元 —— 無文字層 |
| `pdftoppm -r 200` ＋ `tesseract` | 36,033 字元，**全為亂碼**（`mo}4 pue 91607 |INH a109 LY`） |
| 水平鏡像後 OCR | 35,637 字元，仍亂（`wol bns sipot IMH`） |
| **旋轉 180° 後 OCR** | **35,901 字元，可讀**（`R1 Core / HMI Logic and Flow / Spec Release: SR24 Post 2A`） |

**該 PDF 之頁面為旋轉 180° 儲存。** 讀出後之命中：

| 關鍵詞 | 命中 |
|---|---|
| `Fail_Present`／`STATFailSts`／`Heated Steering Wheel Icon` | **0 / 0 / 0** |
| `Heated`／`Seat`／`Fail` | **0 / 0 / 0** |
| `Left Side`／`Right Side` | 3 / 3 —— **全為 `left sideways`／`right sideways`**（滑動手勢） |
| `Steering` | 2 —— `Steering Wheel Controls HMI Logic and Flow`（文件名）與 `steering wheel control`（按鍵類別） |

**→ 殘留為 0。** 若止於「未解析」，本輪之結論會留一個洞，而那個洞正好是
00D 點名最可能藏失效彈窗的候選。

## 2. OCR 之效力界線（R-G11）

OCR 為機器辨識，**其漏字不會報錯**。本節之「0 命中」強度低於文字層之 0 命中。
佐證其確實讀到內容：`HMI` 23 次、`Core` 9 次、封面欄位（作者信箱、CR 號、日期）皆正確還原。
**惟若關鍵詞出現於圖內文字且解析度不足，OCR 會漏。** 登記為已知界線。

## 3. 詞界之補驗（canon §5a 條 5）

首版掃描**未用詞界**，`Left Side`／`Right Side` 共 4 檔次命中，逐一檢視：

| 檔 | 命中 | 實際內容 |
|---|---|---|
| `Surround view camera for APAC China and Maserati HMI Logic and Flow.pdf` | 各 1 | `• Left Side View` / `• Right Side View` —— **環景攝影機之視角選項** |
| `Core HMI Logic and Flow…(February 2 2023).pdf`（OCR） | 各 3 | `left sideways`／`right sideways` —— **滑動手勢，無詞界之子字串誤命中** |

**四檔次全部與加熱方向盤圖示之左右駕鏡像無關。**
`Left Side` 對 `left sideways` 之誤命中，為 §5a 條 7「假陽性源自詞界不足」之標準形態。
