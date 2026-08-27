# 上繳包 12 — Bed Lowering Mode：B4 批（Cluster Feedback，13 leaf）

日期：2026-08-27
對應下放包：`features/bed_lowering/docs/handoff/12_b4_cluster_feedback.md`
（sha256 `66ba8a10a6800388e1ca64fe266d3b583c23bbbf669802ea8d56d1fa8798aa66`）
執行層：Tier 1

**結論：B4 十三條生成完成，12 條寫回（列 86–97），1 條依 IN §8.4.3 保留。
機檢與交付 lint（全簿 88 列）皆 clean。
兩項須看：下放包 §二-1 所載之文案字串與來源不符（§二）；新缺件 DR-3 已登記（§四）。**

---

## 一、範圍

`Cluster Feedback`，母號 009／010／012／033／034，
**13 leaf（HMI 11／Service 2）**，整組取用未手挑。
req_id 集合與 context 之 13 leaf **完全一致**（assert）。
母號分佈 009×2／010×2／012×2／033×4／034×3 = 13。

---

## 二、**文案字串與下放包所載不同 —— 依來源正式欄**

下放包 §二-1 預期之 Cluster 文案為 `"Lowering Bed"` 與 `"Bed Lowering Complete"`。
**037 與 SYS1 皆非此字串。** 實載：

| 訊息 | 037 Requirement Description | SYS1 Basic Report |
|---|---|---|
| 進行中 | `Truck Bed Lowering In Progress` | NRL-193700：`EVIC displays “Truck Bed Lowering In Progress” when app icon is pressed.` |
| 已降下 | `Truck Bed Lowered` | NRL-193701：`EVIC displays “Truck Bed Lowered” once defined suspension angle is achieved.` |

**兩處來源逐字一致**，本包採之。SYS1 用彎引號（`“”`），TC 依 IN §11 一律改直引號 ——
**該轉換屬排版正規化，非改字**（與 R-4 首字大寫同類）。

下放包之字串未採用，理由即「來源正式欄為第一來源」（錨定原則）。
此處未登異常 —— 下放包之字串是預期而非裁定，實測不符即以實測為準。

---

## 三、chime 預查 —— **Bed Lowering 專屬訊號查無**

下放包 §二-2 令先預查再決定 ER 形態。結果：

| 範圍 | chime 類命中 | 與 Bed Lowering 相關 |
|---|---|---|
| dbc_fd（323 訊息／2,037 訊號）| 22 支 | **0** |
| dbc_b（155／914）| 22 支 | **0** |
| LID CAN Mapping（2,629 列）| 66 列 | **0** |

命中之 44 支訊號全屬 ADAS（`ADAS_FD_HMI.Chime_*`）、停車輔助
（`PARK_INFO.ChimeActivation_*`、`PamChimeVolume*`）與盲點警示（`BSIS_*_Chime_Type`）。
**無一支屬 Bed Lowering。**

故 012-01／012-02 採**純可聽判定**，無訊號輔助 ER。
`$ASCM_FD_2.ASCM_Stat$` 仍用於界定「角度達成」之時點，但那是時點界定不是聲音確認 ——
依下放包 §二-5，ER 之判定主體寫聲音，訊號為輔句，未倒置。

---

## 四、**新缺件：DR-3（已登記）**

033-04 要求「與最終圖形定義對齊」，而**該定義尚不存在**：

```
SYS1 NRL-193740：When the bed lowering is activated from the head unit, the following
                 will be shown in the cluster: (image: image5.png)
                 Final graphics to be completed by PDO.
```

037 之 033-04 亦寫 `to be completed by PDO`。依 IN §8.4.3 落
`PENDING: DR-3 Bed Lowering cluster graphics definition (owner: PDO)`，不造基準、不寫回。

**已於 `DATA_REQUESTS.md` 登記 DR-3**（登記屬 Tier 1）。
**草擬與送出未做** —— 該表自載「DR 由 analysis 層起草，Pei 決定送出」，
故狀態欄寫「執行層登記，草擬與送出待分析層／Pei」。

### 一條界線值得記

033-02 與 033-04 都講儀表圖形，但**基準不同**：

- 033-02：與**現行參考圖**（image5.png，草稿）比對 → **可測，已寫回**
- 033-04：與**最終定義**比對 → 定義不存在 → **PENDING，未寫回**

兩者不是同一個基準。若把 033-02 也標 PENDING，等於宣稱現行參考圖不存在（不實）；
若把 033-04 也拿現行圖測，等於用草稿冒充最終定義（更糟）。故一條寫回一條保留。

---

## 五、§二-3 Fault Handling 界線 —— 零重疊

已讀 Fault Handling 已交付之 13 條，逐一比對 UI 顯示文案：

| 批 | UI 文案 |
|---|---|
| B4 | `Truck Bed Lowering In Progress`、`Truck Bed Lowered` |
| Fault Handling | `Bed Lowering Unsuccessful - Air Suspension Service Required`、`Air Suspension Service Required` |

**交集僅按鍵標籤 `"Bed Lowering"`**（兩批本就都要按它），
**訊息文案零重疊** —— §8.2.1 界線成立，未重測故障文案。

---

## 六、R-BLM13 與機檢

(a) 用於四處：012-01（與 012-02 同 trigger，斷言「有聲音」不斷言「是 chime」）、
033-01（斷言指示出現，不斷言畫面內容）、034-01（同）、033-04（委派 033-02）。
無一處可用 (c) —— 本批之 leaf 對多共用同一 trigger（按壓、角度達成），
`OperationalModeSts` 那種可分列舉在此無對應物。

```
TC 數 13
N 欄相異值數 1  (R-BLM5 預期 1)
priority 分布 {'P1': 5, 'P2': 8}
design_method 分布 {'Functional Based': 11, 'State Transition': 2}
Input Test Data == NA 之比例 13/13
機檢項全數 PASS
```

§5.2 首跑抓到 033-04 之 Final 19w，已重排為三步
（PENDING 基準留在 Pre-Condition 6，比對動作獨立成步）。複核全批 PASS。
入口紀律：**13 條無一條注入 `$ASCM_*$`**。括號下半相異數 13。

---

## 七、寫回

| 項 | 值 |
|---|---|
| 輸出 | `workbook/bed_lowering_07.xlsx` sha256 `3d64305418224ab93c320e5a557239a75d03aa0de7eb06776eb08697973973f8` |
| 列 | 86–97（12 條）|
| TC ID | `newR1L-BLM-077` … `newR1L-BLM-088` |
| patched 儲存格 | 168（12 × 14）|
| round-trip | 12 列 × 14 欄，**差異 0** |
| 保全計數 | zip 48／sheet 9／legacy DV 4／**x14 DV 1**／extLst 3 —— 全等 |
| 交付 lint | **全簿 88 列 clean — 0 findings** |

工作簿鏈：`00 → 01 pilot → 02 B1 → 03 清兩欄 → 04 B1 修訂 → 05 B2 → 06 B3 → 07 B4`

**累計：88 列已寫回**（13+6+26+31+12），未寫回 PENDING **8 條**
（B1×3、B2×2、B3×2、B4×1）。生成總數 96 條 = 176 leaf 之 **54.5%**（分母 176 leaf）。

---

## 八、執行層自陳

1. **012 兩條為純可聽判定**，台架須有安靜環境與聽力確認。
   與 B3 之 040 LED 目視同類 —— 分析層已裁該類不構成新形態（下放包 §分析層處置），
   本批依此不另議，但**兩類累計已 6 條非匯流排可判**（040×4、012×2），
   若台架能力有限，其影響是集中的而非分散的。
2. **033-02／034-02 之參考圖為草稿**。NRL-193740 明載最終圖形未完成，
   故 033-02 所比對之 image5.png 是階段性版本。**該條今日可測，
   但 PDO 完稿後其基準會變** —— 屆時 033-02 需複驗，033-04 需解 PENDING。
   兩者連動，已記於 manifest。
3. **009-02／033-03／034-03 之「通道」斷言**（EVIC/cluster 是輸出通道）
   以「他處不顯示」佐證。與 B3 §七-6 同形態：**「沒有」難以窮舉**，
   實作上只能就 tester 可見之畫面判斷。
4. **completion 仍非模型產出**（第五次記載）。
5. **台架可執行性未驗**（第九次記載）。

---

## 九、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 送出核准，Pei 執行；累計 7 條 PENDING |
| DR-2 | Off-Road 2／Easy Entry ride-height 對映 | 草案已登記，送否 Pei 決 |
| DR-3 | Bed Lowering cluster graphics definition（owner: PDO）| **本包新登記**；033-04 一條 PENDING |

---

## 十、停點

**已停。** 交分析層複審。**本批為 R-G14 計數第 3 批候選 —— 過則綠色通道成立。**
執行層不自評：§二之文案字串偏離與 §四之新 DR 是否構成 A 類，由分析層裁。
