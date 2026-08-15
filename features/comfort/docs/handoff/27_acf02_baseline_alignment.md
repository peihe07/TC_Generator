# 27 — Comfort HMI / A-CF02 裁定：交付夾基線一致化

- 產出層：分析層｜2026-08-15｜對象：執行層／Pei
- 裁定：Pei，2026-08-15（三選一，答「1」）

---

## 1. 問題重述（量測，非引用先前輸出）

037 之 HMI Source ID 於 2026-08-15 重測：sheet `Analysis Report`，
row 8–505，A 欄非空 **498 列**；取儲存格第一行、去除末段節次後之檔名 stem，
**相異 stem 數為 1**：

```
SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)
```

無 SR25、無空值、無例外。**037 本身沒有模稜兩可**，R-C1 之基線裁定
（以 SWE.1 所引者為準 = SR24）與之完全相符。

問題不在 037，在**交付夾之附件**：

```
10_Reviewing/00_TestCase/ASW-R2/Climate Control Interface/ComfortHMI/
├── FM-WI-FSM-037-A03-N1L-SWE1-Comfort-HMI-V0.1 STLA 報告.xlsx   ← 引 SR24
├── Comfort HMI Logic and Flow R1 SR25 Post 3A CR29359 (Feb 24 2025).pdf
└── SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR25_Post_3A_CR29359_(Feb_24_2025).xlsx
```

工作簿內 14 條之 `specification_reference` 全數為 SR24 stem，附件卻是 SR25。
評閱方開啟資料夾即見矛盾。

---

## 2. 裁定：放回 SR24，移走 SR25

**A-CF02 之處置為選項 1。** 交付夾之 spec 附件改為 SR24 CR24879，
與 037 及工作簿一致。

來源（repo 內，實測存在）：

| 檔案 | 來源路徑 |
|---|---|
| SR24 PDF | `spec-index/sources/Comfort HMI Logic and Flow R1 SR24 Post 3A CR24879 (September 25 2023).pdf`（6.16 MB） |
| SR24 SYS1 export | `spec-index/cache/SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023).xlsx`（70,040 bytes） |

移走之 SR25 兩份**非資料遺失** —— `spec-index/sources` 與 `cache` 皆留有
其副本（SR25 PDF 13.86 MB、SR25 xlsx）。

---

## 3. 執行分工

**放入 SR24（增量、可逆）** —— 得由執行層執行：
複製上表兩檔至交付夾，**保留原檔名**，複製後以 bytes 比對來源與目的地
（**不以檔名或大小標籤代替**，R-C14）。

**移走 SR25（客戶樹之移除）** —— **由 Pei 執行**。
客戶交付樹之移除屬 Tier 3；執行層備妥後停下並回報應移除之兩個檔名。

**先放後移**：任一時點交付夾內至少有一份完整之 spec，避免中間狀態下
資料夾無 spec 可查。

---

## 4. 執行後之驗證與登記

1. 交付夾實測清單與各檔 bytes，寫入上繳包
2. `A-CF02` 轉 **RESOLVED**，條目載明：現象（附件基線與 037／工作簿不一致）、
   裁定（Pei 2026-08-15 選項 1）、處置（SR24 放入／SR25 移出）、
   以及**重審條件**：若日後基線改採 SR25（需先推翻 R-C1），本項須同步重做
3. `BASELINE.sha256` **不變** —— 其涵蓋範圍為 pipeline 之來源檔（R-C20），
   交付夾附件不在其列

---

## 5. 與交付時點無關

本項為交付夾之基線一致化，**不等同於交付 pilot 工作簿**。
兩者可分開：資料夾之附件現在就該一致，工作簿何時放入另裁（下放包 28）。

---

## 6. 本包產生之新條文清單（自檢）

無新條文。本包為 anomaly 處置與作業分工。
