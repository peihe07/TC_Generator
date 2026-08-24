# 下放包 05b —— Q3 重裁定案（與 05 同一往返，須併讀）

- 日期：2026-08-24
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- **本檔不另佔往返編號** —— 與 [05_corpus_fix_and_framework_prep.md](05_corpus_fix_and_framework_prep.md)
  ＋ [05a_upstream_naming_scope.md](05a_upstream_naming_scope.md) 同屬第 05 輪，
  上繳仍為 `docs/upstream/05_corpus_fix_and_framework_prep.md`
- 05／05a 本文皆未改一字

---

## 一、Pei 之裁定（2026-08-24，逐字）

> 「（甲）」

即 05 包 §五之案（甲）：`D5` 維持留空。

---

## 二、裁決條文（抄入 `RULINGS.md`）

```
R-PMH27（Q3 重裁定案，取代 R-PMH10 之依據段）
`D3 審查者`／`D4 目的`／`D5 範圍 Scope` 三欄**一律留空**。
結論與 R-PMH10 相同，**其依據更換如下**。

R-PMH10 所載之依據句「已交付件四份之該三欄皆空，母本亦空 ——
語料 5/5 無一填寫」**作廢** —— 其母體未定義（04 包 §2、05 包 §二）。

改以 R-PMH24 修正後之母體 16 檔實測為據：

  D3：16/16 空
  D4：16/16 空
  D5：9/16 空、7/16 非空

**本裁定不是多數決**，須連同下列三項一併記載，不得只留結論：
(a) 七個非空者中有兩者填錯 —— `HomeHMI` 之值逐字等同 `AppDrawer` 之
    037 報告名（他 feature 之報告），`Notifications HMI` 之值為
    `FM-WI-FSM-036-A01`（表單編號本身，非任何規格或報告）；
(b) 案（乙）之代價為版號過期無通知機制（本 feature 之 037 為 `V0.1`，
    而 Popup 已至 `V0.2`，證明版號會動）；
(c) 部分 feature 無「單一份 037」可寫（VF230 對應 11 份、CFTS044 對應
    4 份），案（乙）在全案並非良定義。

R-PMH10 之末句效力**維持**：日後若客戶要求填寫，其字串由 Pei 給定並
另立新條取代，**不得以「補上」之名逕行填寫**。

R-PMH10 之 `[PEI-REOPEN]` 標記**撤除**。
```

---

## 三、作業指示（併入 05 之步驟 1）

- 抄錄 R-PMH27，附核對表；
- **撤除 R-PMH10 條後之 `[PEI-REOPEN]` 標記**，改為「已於 2026-08-24 重裁
  定案，見 R-PMH27」之附註（**R-PMH10 原文仍不改字**，其 SHA256
  `885070968235b262` 須維持不變並於上繳複驗）；
- `DECISIONS.md` 之前言三欄由 `[PEI-REOPEN]` 改為 `[RULED]`，附 R-PMH27；
- `PLAYBOOK.md` §6 之 Open rulings 表移除 Q3 一列。

---

## 四、本輪 open 項之結清狀態

| 項 | 狀態 |
|---|---|
| Q3（D3／D4／D5） | **已結清** —— R-PMH27 |
| Q7（`tc_id` abbr） | 已結清（R-PMH16） |
| A-PMH06 canon 層（`new_feature.py` 樣板） | **PENDING-CANON**，待 Pei 決定是否另開 canon 包 |
| A-PMH03／04（規格偏離、圖片佔位） | PENDING，Phase 4 複核 |
| A-PMH10（`Pair-wise` 字串） | PENDING，不阻斷（R-PMH25 已定權威） |
| A-PMH12（`Q` 欄 DV 跨欄、`AF` 前導空白） | PENDING，Phase 6／7 前置阻斷項 |
| H 欄（Test Set） | `[PEI]`，Phase 3 |

**無阻斷 Phase 3 之未決項。** 05 步驟 4 之 `layer3_sections.tsv` 交回後，
Layer 2 之提案由分析層提出、Pei 裁定。

---

## 五、本檔產生之新條文清單（自檢表）

| 條號 | 主旨 | 已以可貼區塊出現於 §二 |
|---|---|---|
| R-PMH27 | Q3 重裁定案：三欄留空，依據更換為 16 檔母體，附三項不得省略之記載 | ✅ |

一條一件事。R-PMH27 為**依據更換型**：結論與 R-PMH10 相同，
更換者為其證據基礎；兩條並存，原文不改字。
