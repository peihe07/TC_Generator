# 下放包 03a —— Pei 裁定三項（與 03 同一往返，須併讀）

- 日期：2026-08-23
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- feature slug：`power_moding`
- **本檔不另佔往返編號** —— 與 [03_testgroup_and_dv.md](03_testgroup_and_dv.md)
  同屬第 03 輪，上繳仍為 `docs/upstream/03_testgroup_and_dv.md`
- 03 本文**未改一字**（其 §三 R-PMH13 之「待 Pei 核可」與 §四 Q7 之「待裁」
  狀態由本檔解除，原文保留以存其當時之未定狀態）

---

## 一、Pei 之裁定（2026-08-23，逐字）

> 「R-PMH13 核可、Q7 乙、A-PMH06 追認」

三項逐一落為條文如下。

---

## 二、裁決條文（逐條抄入 `RULINGS.md`）

```
R-PMH13 之生效（加註，原條文不改字）
Pei 於 2026-08-23 核可 R-PMH13。該條末句「本條之效力起於 Pei 核可；
核可前 G 欄不得寫入任何值」之停止條件**解除**。

`feature.yaml` 之 `test_group` 得改為 `Disclaimer screen`。
R-PMH6 對 H 欄（Test Set）之延後**不受本核可影響**，仍待 Phase 3。
```

```
R-PMH16（tc_id 之 {abbr}）
`tc_id_format` 為 `NR1L-DisclaimerScreen-{NNN}`。

判準：`{abbr}` = 交付夾名去除空白後之 PascalCase，即
`Disclaimer screen` → `DisclaimerScreen`。與 R-PMH13 之 G 欄值同源。

Pei 於 2026-08-23 裁定採 03 包 §4.3 之（乙）案，未採分析層所提之（甲）案
（`PowerModingHMI`）。

**已知反例須隨本條保留，不得略去**：Comfort 之 `{abbr}` 為 `ComfortHMI`，
其交付夾名為 `Climate Control Interface` —— 該件不符本條之判準，且它是
03 包 §4.2 依 R-PMH14 篩出之唯一具鑑別力語料。

故本條為**本 feature 之裁定，不主張為全案慣例**；他 feature 引用本條前
須自行查其交付件。
```

```
R-PMH17（A-PMH06 之追認）
Pei 於 2026-08-23 追認 R-PMH15 所定之 `.gitignore` 寫法
（`inputs/*` ＋ 否定規則放行 `MANIFEST.sha256`，四項雙向驗證）。

A-PMH06 → RESOLVED。R-PMH11 之目的未變，其所指定之無效寫法由 R-PMH15
取代，原文不改字。
```

```
R-PMH18（本 feature 兩個字面常數之保真）
下列二字串為逐字常數，大小寫、空白、單複數一律照抄，任何比對與 lint
須為大小寫敏感：

  G 欄（Test Group）之值：`Disclaimer screen`   —— screen 為小寫 s
  tc_id 之 {abbr}：      `DisclaimerScreen`     —— Screen 為大寫 S

二者刻意不同（前者為交付夾名原樣，後者為其去空白之 PascalCase），
**不是筆誤，不得「統一」**。任何將二者正規化為同一形態之處理即為缺陷。
```

---

## 三、對 03 包各節之影響

| 03 包之節 | 原狀態 | 本檔之後 |
|---|---|---|
| §三 R-PMH13 | 待 Pei 核可，G 欄不得寫入 | **生效**，`feature.yaml` 之 `test_group` 可寫 |
| §四 Q7 | 待裁，`tc_id_pattern` 維持 `TBD` | **已裁（乙）** → R-PMH16；`tc_id_format` 可寫入 `feature.yaml` |
| §一 1.1 A-PMH06 | 分析層先行核可，待 Pei 追認 | **已追認** → R-PMH17，A-PMH06 RESOLVED |
| §五 步驟 1 | R-PMH13 標「待核可」 | 改抄為「已核可（2026-08-23）」，並增抄本檔四條 |
| §五 步驟 2–8 | 不受影響 | 不受影響，照原文執行 |
| §六 停止條件 7–9 | 不受影響 | 不受影響 |

**03 包之其餘部分全部照原文執行。**

---

## 四、仍未決之一項（非本 feature 之阻斷）

`scripts/new_feature.py` 之 `GITIGNORE` 樣板仍為 `inputs/`（目錄形態）——
**任何新 feature 照樣板產出之 `.gitignore`，其雜湊檔都會被忽略**
（A-PMH06 之成因，實測有據）。

Pei 之「A-PMH06 追認」就其字面**只及於本 feature 之 `.gitignore` 寫法**，
未及於樣板。故：

- 標為 **PENDING-CANON**，登記於本 feature 之 `ANOMALIES.md`（A-PMH06 條後
  加註「其 canon 層成因未解」），**不在本 feature 修改樣板**；
- 執行層**不得**順手改 `scripts/new_feature.py`；
- 待 Pei 決定是否另開 canon 層工作包。

> 記此一項之理由：A-PMH06 在本 feature 已 RESOLVED，
> 若不另立 PENDING-CANON，下一個 feature 會再踩一次而沒有任何紀錄指向它。
> 這正是 G-D 之精神（「不做」與「沒發現」必須在紙上分得開）。

---

## 五、本檔產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §二 |
|---|---|---|
| R-PMH13 加註 | 核可生效，停止條件解除 | ✅ |
| R-PMH16 | `tc_id_format` = `NR1L-DisclaimerScreen-{NNN}`，附已知反例 | ✅ |
| R-PMH17 | A-PMH06 追認，RESOLVED | ✅ |
| R-PMH18 | 兩個字面常數之大小寫保真 | ✅ |

四條各管一事。R-PMH16 為**採納型**（Pei 未採分析層提案），其未採之事實
與所依語料已於條內載明，不以「已裁」掩蓋其 n = 1 之強度。

---

## 六、上繳要求（併入 `docs/upstream/03_testgroup_and_dv.md`）

於 03 包原有之十一項外，增列二項：

12. 本檔四條之抄錄核對表（R-PMH13 加註須證明其原文 SHA256 未變）
13. `feature.yaml` 之 `test_group` 與 `tc_id_format` 落地後之全文，
    並以 R-PMH18 之大小寫敏感比對驗二字串逐字相符
