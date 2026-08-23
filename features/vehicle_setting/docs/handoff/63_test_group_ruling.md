# 63 — W-112 裁定：Test Group 一律為 `Vehicle Setting`

下放包 NN=63。對應上繳：`docs/upstream/63_*.md`（併入下一次上繳亦可）。
本包新增 **R-VS67**（1 條）、**W-121**（1 項工單）。

覆核對象：62 包 §4.1（W-112，A-VS128 之三候選）。

---

## 1. Pei 之裁定（2026-08-23）

逐字：**「都以 Vehicle Setting 為主」**。

解讀：W-112 之三候選取 **(c) `Vehicle Setting`**，且「都」及於**兩本 workbook**
（CFTS044 與 VF230 同值），不採 62 包 §4.1 所述之「兩值並存」路線。

---

## 2. 新條文

### R-VS67 —— VF230 之 Test Group

```
R-VS67（VF230 之 Test Group，Pei 裁定 2026-08-23）

Test Group（workbook G 欄 / framework Layer 1）之值為 **`Vehicle Setting`**，
CFTS044 與 VF230 **兩本 workbook 同值**，不因文件不同而分歧。

`profiles.vf230.test_group` 自 `null` 改為 `"Vehicle Setting"`。
`framework.md` 之 Layer 1 維持 `Vehicle Setting`，不因 VF230 併入而改。

**本條明示排除之候選**（A-VS128 之另二源，不得於後續回頭採用）：
  (a) spec L1 Heading 逐字 `Vehicle Setup Management [VF230_V1_]`
  (b) 037 Sub Categorization 眾數 `Vehicle Setting Management (VSM)`（388/619）

**與 R-C6 之關係 —— 須明示，否則後續會被當作漂移而「修正」**：
R-C6 令 feature 身分取自 spec 之模組名，其於本案指向 (a)。
**本條為 Pei 對 R-C6 於本案之明示排除**，非疏漏、非未查證。
R-C6 之通則不因本條廢止，僅於 VF230 之 Test Group 一事不適用。

理由（記錄 Pei 之取向，非本層推得）：VF230 併入 `vehicle_setting`
（R-VS60），單一 feature 內之 Test Group 保持單值，優先於 spec 模組名之
逐字忠實。
```

---

## 3. 配套之未決細節（W-121，執行層查證後回報，**不得自行套用**）

R-VS67 定了**值**，未定**是否寫入 G 欄**。二者不同：

**實測**（62 包 §2.2 與 61 包 §2.3）：

```
CFTS044 交付路徑之 036   G 欄非空 0 / 237
VF230 之 036             全表非空 0 / 237（BLANK）
feature.yaml             write_back.fill_test_group_set: false
```

canon §2 之規定為「`fill_test_group_set` 僅於 BLANK 下得為 true」。
**Part 1 亦判為 BLANK，卻設 false** —— 故該規則非「BLANK ⇒ true」，
其為「非 BLANK ⇒ 必 false」之單向限制，true 與否另有依據。

**W-121 之待答**：
1. 回查 Part 1 將 `fill_test_group_set` 設為 false 之依據（`DECISIONS.md`／
   `RULINGS.md`／`docs/upstream/` 逐字），**不以記憶或推論作答**；
   若查無明文依據，逐字回報「查無」。
2. 依該依據判斷 VF230 應為 true 或 false，附理由。
3. **不逕改 `feature.yaml`**。回報後由分析層裁定；若涉及 Part 1 既有設定之
   變更，則屬 Pei。

**理由**：VF230 之 036 為真空白，若 G 欄不寫，交付之工作簿將無 Test Group 欄；
若寫，則與 Part 1 之同 feature 工作簿在該欄之填寫形態不一致。
兩者皆有後果，不得以「值已定」為由略過。

---

## 4. 仍待 Pei 裁定（本次裁定未涵蓋）

**「都以 Vehicle Setting 為主」解決 W-112。以下二項不在其射程內，仍為 open：**

### 4.1 Layer 2 起點與時點（62 包 §4.2，屬 P3 須你核可）

執行層建議以 **037 之 11 份分報告族群**為 Layer 2 起點
（12–131 leaf，中位 52），排除 spec 目次（其塌成 603 : 16，A-VS127）。

分析層同意排除 spec 目次之理由，建議**待 W-116 之正規化複驗（R-VS66）完成後
再定**，因複驗可能改變 106 個 037 Title 簇之可用性。

**請裁**：(i) 複驗後再定，或 (ii) 逕以 11 族群為起點鎖定。

**注意**：R-VS67 只定 Layer 1。**Layer 2 未定則 `framework.md` 仍不得寫入，
Layer 3 亦無從建立**（canon §4.1.2 步驟 3 須待 Layer 2 核可）。
VF230 之 TC 生成在此之前無法開始。

### 4.2 DR-28（VF230 缺 SYS2 ICS export）之送出

草稿已落於 `DATA_REQUESTS.md`，狀態「未送出」。
在其覆文前，VF230 之 619 leaf 之 Functional/Heading 判定**單源自 037**
（62 包 §2.2 之 `output/` 對帳為佐證，非跨源驗核，位階不升等）。

---

## 5. 本包產生之新條文清單（自檢）

| 編號 | 型別 | 是否以可貼入區塊出現 |
|---|---|---|
| R-VS67（Test Group = `Vehicle Setting`，兩本同值，明示排除 R-C6） | Pei 裁定 | ✅ §2 |

**工單**：W-121（`fill_test_group_set` 之依據回查，不逕改）。

**仍 open**：Layer 2 起點與時點（§4.1）／DR-28 送出（§4.2）。

**下輪工單全集**（含 62 包所開，優先序）：
W-120（`Verification Criteria` 二欄，**最優先**）→ W-116（正規化複驗）→
W-121（`fill_test_group_set`）→ W-119（DR 波及三分類）→
W-117（`-(\d+)$` 容錯清單）→ W-118（A-VS130 是否成 DR）。

**執行層上繳時須附「本包是否仍有該驗而未驗者」之獨立判斷。**
