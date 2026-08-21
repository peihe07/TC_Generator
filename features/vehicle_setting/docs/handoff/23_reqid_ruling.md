# 23 下放包 — R-VS33：spec_reference 取 CFTS044 reqid，及其素材缺口

分析層寫入，2026-08-20。Pei 裁定 spec_reference 之填入形式。

---

## 1. 裁決正文

```
R-VS33（Pei 2026-08-20）
`specification_reference`（036 N 欄）填入之值為 **CFTS044 之 requirement id**
（形如 `CFTS044-NNNN`），非章節號。

本條**取代**下列先前記載：
  - 00 包 R-VS2(c) 及其後各包所稱「取 CFTS044 章節號」
  - 01 包 §2.2「236 / 237 已定」之「已定」——其所定者為章節號，
    依本條不再是交付值
  - R-VS14 不受影響：其所定者為「字串清單、多值允許」之形式，
    與取值來源無關；多個 reqid 者仍逐一列出

R-VS14 之排序規則（由最具體至一般）於 reqid 形式下改為：
  依 reqid 之數值由小至大。
```

---

## 2. **本條目前不可執行** —— 素材缺口，實測

分析層自 `inputs/` 實體檔實測（237 個 Functional leaf，
經 R-VS2 錨鏈 leaf → SYS-RA → SYS2 → 7 位數 Polarion id → CFTS044 條文區塊）：

| 來源 | 能取得 `CFTS044-NNNN` 之 leaf 數 |
|---|---|
| SYS2 `Description` 欄內含 `CFTS044-NNNN` | **4 / 237** |
| CFTS044 docx 之該 leaf 條文區塊內含 `CFTS044-NNNN` | **4 / 237** |
| **兩者任一** | **4 / 237（1.7%）** |

### 2.1 成因：`CFTS044-NNNN` 不是條文在 docx 內的自身識別碼

CFTS044 docx 之條文區塊，其**自身識別碼為 7 位數 Polarion id**：

```
4858298: [Artifact Type:Subsystem Functional Requirement] [State:New] …
```

全文 `CFTS044-NNNN` 命中 410 處、相異 167，
**其中落在 `Functional Requirements` 章之前者為 0** ——
即全部在正文內，但**分布於 2030 個條文區塊中的 41 個**，
且經逐塊檢視，其形態為**內文交叉引用**
（`… as defined in CFTS044-1520 …`、修訂敘述），
**不是該區塊自己的編號**。

同理 SYS2 `Basic Report` 之 `Description` 欄雖有 159 個相異
`CFTS044-NNNN`，其亦為敘述中之引用，非該列之識別碼；
該列之識別碼為 A 欄之 `NRL-6xxxx` 與 `Source Requirement items` 之 7 位數。

**故現有六類素材中，沒有一份載明「條文 ↔ CFTS044 reqid」之對照。**

---

## 3. DR-16（新，**Urgency High，阻塞交付**）

```
DR-16
需要：CFTS044 之 requirement id（`CFTS044-NNNN`）與 Polarion 7 位數
      物件 id 之對照，涵蓋本 feature 之 237 個 Functional leaf。

可能形式（擇一即可）：
  (a) Polarion 匯出之 CFTS044 工作項清單，同時含 `ID`（CFTS044-NNNN）
      與物件 id（7 位數）兩欄
  (b) CFTS044 之 RAR／traceability 匯出，含上述兩欄
  (c) CFTS044 docx 之另一版本，其條文標頭以 CFTS044-NNNN 呈現
      （現行 SR26 20250909-1816 版以 7 位數呈現）

現況：六類素材中無任一份載明該對照。
      237 個 Functional leaf 中僅 4 個（1.7%）可自現有素材取得 reqid，
      且其來源為內文交叉引用而非該條文之自身編號 ——
      **即該 4 個亦不可信**。

阻塞：`specification_reference` 為 036 之必填欄（§10.7），
      R-VS33 裁定其值為 reqid。**無此對照則全部 237 列無法填 N 欄。**
      TC 內容（test_item／procedure／ER）不受阻塞。
```

---

## 4. 在 DR-16 到位前之作業安排（分析層裁定）

**不停生成。** 依既有原則「不知道適用於誰 ≠ 不知道存在什麼」，
以及 R-VS17 之 BLOCKED 形態：

```
W-31（分析層裁定 2026-08-20）
DR-16 未到位期間：
(1) TC 照常生成，N 欄以佔位符 `<PENDING-REQID>` 填入，
    **不填章節號、不填 7 位數 Polarion id、不留空**
    —— 留空會通過不了必填檢查而看似缺漏，填章節號會在 DR-16 到位後
    產生一次全欄改寫且無法辨識哪些是舊值。
(2) 同時產出 `data/reqid_pending.tsv`，逐 leaf 記其
    swe_id / polarion_7digit / section（先前已解析之章節號，作為對照用）
    —— **章節號不進工作簿，但保留於 repo，供 DR-16 到位後交叉驗證**
    （若 reqid 與章節號之對應不一致，即為錯誤之訊號）
(3) DR-16 到位後，以 `xlsx_surgical.py` 單欄回填 N 欄；
    回填屬 write-back，須 Pei 逐次授權。
```

**先前已解析之章節號不作廢**：其為 245 leaf 之落點，
於 DR-16 到位後是**唯一可用的交叉驗證來源**——
reqid 與章節號若指向不同條文，表示對照表或錨鏈有誤。

---

## 5. 對既有記載之更正

| 記載 | 更正 |
|---|---|
| 00 包 R-VS2(c)「章節號為 spec_reference 之末段」 | **作廢**，依 R-VS33 |
| 01 包 §2.2「236 / 237 已定」 | 改為「章節號已解析 236／237；**交付值（reqid）0 / 237**」 |
| 04 包 §2.2「R-VS2(c) 之 PENDING 可解除」 | **收回**：解除者為章節號之解析，非交付值之定案 |
| 12 包 §5「framework 前置已備」 | 增列一項未備：**N 欄之取值來源（DR-16）** |

---

## 6. 本包產生之新條文清單（自檢）

| 條 | 主題 | 裁定者 |
|---|---|---|
| R-VS33 | spec_reference 取 CFTS044 reqid，非章節號 | Pei |
| DR-16 | reqid ↔ 7 位數 Polarion id 之對照（High，阻塞 N 欄） | 分析層登記 |
| W-31 | DR-16 未到位期間之佔位符與對照表 | 分析層 |
