# 49 — Comfort HMI / `14.12` 軸之查證、批次 8

- 產出層：分析層｜2026-08-15｜對象：執行層
- 覆核對象：`docs/upstream/33_batch7.md` §6.4

---

## 1. `14.12` 之硬控輸入型態 —— 依三條件查

執行層查出 `14.12` 為未登記之軸（旋鈕型硬控 → radial popup；
UP/DOWN 型 → vertical popup），未自行增軸，正確。

沿用既有三條件（客觀條件，非判斷）：

1. 兩值（或更多）在條文中**逐字出現**，具名節次與句
2. 互斥且窮盡，或條文明示其為並列情形
3. 無任何值由推論補齊

齊備 → 登第十六軸，並依 **R-C34** 判其類別（介面型／功能型）；
若判為介面型，須進 `interface_axis_review` 之鍵，且既有全部 TC 須回填。
不齊 → 回報缺項並登 DR，不增軸。

**須於 `Climate Popups`（42 leaves）生成前有結論** —— 該組為十五組中第三大，
軸未定即生成將導致大批回溯補 PC（前例：2.2 之 8 條，34 §4.1）。

---

## 2. 批次 8 —— `Home Screen Widget`

| 項 | 值 |
|---|---|
| Test Set | `Home Screen Widget` |
| 節次與各節 leaf 數 | **自 `framework.md` 導出，逐節列出**（下放包不預填，48 §2）|
| tc_id | 續編 |

**選此批之理由**：不涉 `14.12` 之待定軸（`Climate Popups`）、
不涉 DR #31（`Airflow and Defrost`）、不涉 ch16 換軸之連動。

### 2.1 R-C17 為本批之主要風險

Home Screen HMI L&F 為**外部參照 spec**。Comfort 僅擁有
「Comfort widget 自身之內容與行為」。

首頁管理行為 —— HSD／HSS／SW／BSP 各條，含新增／刪除／重排頁面、
widget 拖放、Shortcuts 編輯、品牌頁預設配置 —— 由 Home Screen 之 SWE 需求
擁有，**不得寫入 Comfort TC**。

判定測試：**該規則定義於 Comfort spec 抑或 Home Screen spec？**
後者即 out of scope，**縱使 Comfort spec 引用之**。

外部 spec 若須引用，其 `specification_reference` 另列該檔之 section，
**不併入 Comfort stem**，且須寫全名指向 SR24 Post 2A (March 17 2023)
—— cache 內同時存有 SR25 版（profile §3.5）。

### 2.2 其他

- `19.x`（7" widget）依 R-C5-1 仍為 undetermined（DR #6），**不生成**
- R-C34 生成時義務、R-C36-1、R-C28 三問照舊
- stop-and-report 條件同前，含配置軸不在既有軸內即停

---

## 3. 寫回

依下放包 46 §3：寫回照常執行，產出檔標「範本容量待擴充」，
**不送 Pei 之 Excel 四項確認**，`DELIVERY.sha256` 照常增列。

---

## 4. 執行層作業指示

1. 依 §1 查 `14.12` 三條件，回報結論；齊備方增軸。
2. 執行批次 8（§2），節次與 leaf 數自 `framework.md` 導出。
3. 全批重跑 lint 與 §9 自評；寫回依 §3。
4. 上繳 `docs/upstream/34_batch8.md`。git 不執行。

---

## 5. 本包產生之新條文清單（自檢）

無新條文。
