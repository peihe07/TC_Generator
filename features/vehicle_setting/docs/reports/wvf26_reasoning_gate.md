# W-VF26 —— `reasoning` gate 之設計（**設計待核，未實作**）

V10 §9：R-VF13 第 5 項令「每次採用須於 `reasoning` 具名來源欄名與該 leaf 之 id」，
而該欄為 TC 物件之欄位；`data/grade_overrides.tsv` 有該資訊，
**但無任何檢查要求 TC 之 `reasoning` 引用之**。

**依 V10 §9「先提設計待核，不逕行實作」—— 本輪未寫任何 lint 程式碼。**

---

## 1. 缺口之形態

```
覆寫清單（有來源資訊）      →  writability.tsv 之 evidence_note   ← 已有 --check 保證
                            →  TC 之 reasoning                    ← 無任何保證
```

TC 尚未生成，故現在無違規可查；**缺口在於「彼時無機制提醒」**，
與 A-VS106 同型（機制不存在與機制通過不可分辨）。

## 2. 設計

**掛載點**：`scripts/lint036.py`（既有之 TC lint），新增一條規則。

**規則（擬名 `L-VF1`）**：

```
凡 TC 之 leaf_id 出現於 data/grade_overrides.tsv 者，其 reasoning 須同時含：
  (a) 該列之 source_column 逐字（如 `037 Verification Method`）
  (b) 該列之 reqid 逐字（如 `4859496`）
二者缺一即 FAIL。
```

**判準之依據為清單，非內嵌之條件式**（R-VF20 第 2 項之延伸）——
清單增列一筆，規則自動及之，無須改碼。

## 3. 錨點（R-VF21／R-VF28：以內容定錨）

| 錨點 | 內容 | 期望 |
|---|---|---|
| 必命中（應 FAIL） | 一筆 `leaf_id` 在清單內而 `reasoning` 不含 reqid 之合成 TC | FAIL |
| 必不命中（應 PASS） | 一筆 `leaf_id` 在清單內且 `reasoning` 含欄名與 reqid 之合成 TC | PASS |
| 鑑別（應 PASS） | 一筆 `leaf_id` **不在**清單內且 `reasoning` 不含 reqid 之 TC | PASS —— 證明規則只及於清單內者，不誤傷 |

**第三個錨點為必要**：若無之，一條「所有 TC 之 reasoning 都須含 reqid」
之過寬規則亦會使前兩個錨點通過。

## 4. 依 R-VF29 第 6 項之涵蓋面檢查

R-VF13 第 5 項要求「來源欄名 **與** leaf id」。
本規則檢 `source_column` 與 `reqid`，**未檢 leaf id** ——
理由：`reasoning` 所屬之 TC 已有 `leaf_id` 欄，於該欄外再要求文字重述
並不增加可稽核性。**惟此為本層之判斷，與條文字面有落差，具名待核。**

## 5. 未決（待核可後方實作）

1. 規則編號 `L-VF1` 是否與 Part 1 之 `L-VS*` 序列衝突 —— **開號前須查**。
2. 掛於 `lint036.py`（兩線共用）抑或另立 VF230 專用 lint ——
   前者會使 Part 1 之 lint 亦執行本規則（現行清單之 4 leaf 皆屬 Part 1，
   故實際上本即應及於 Part 1）。
3. FAIL 抑或 WARN。R-VF13 為 Pei 裁定，本層傾向 FAIL，**不自決**。
