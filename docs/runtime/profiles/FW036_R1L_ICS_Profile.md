# FW036 R1L — ICS Management Profile

Feature slug：`ics_management`　Test Group：`ICS`（R-ICS1）
狀態：**ACTIVE**（分析層 2026-08-29 即裁 R-ICS18，下放包 04 §三 A 令執行層落檔）
runtime 讀法：本檔之 `[OVERRIDE IN §x]` 勝出於 IN 之同節；無 override 者依 IN。
落檔註記：本檔由**執行層**落檔，**內容逐字取 R-ICS18(a)(b)(c)**
（`features/ics_management/RULINGS.md`，sha8 見 upstream-04 §1）。
執行層落檔，但**不是條文之作者**（下放包 04 §1 禁區第 8 項）——
本檔除本段檔頭與節標題外，無一字為執行層所書。

---

## §1 IN §11 —— cited `[OVERRIDE IN §11]`

依 **R-ICS18**，本 feature 啟用 IN §11 之 Exception。條文逐字：

```
(a) 本 feature 啟用 IN §11 Exception，範圍限定於：
    `test_item` **上半**之 verbatim 段落，及 ER 中以
    `... as defined by CFTS0xx-{ObjectID} ...` 式引註之引句段落。
    保留之記法包含來源自身之方括號（`[DISP_OFF]`、`[DISP_NORMAL]`、
    `[0% Intensity]`、`[current non-zero value]`、`[Idle]`）與單引號
    （`'HU Screen ON'`、`'HU Screen OFF'`）。
(b) **作者自書之文字不適用本例**：procedure 之按鍵標的、非引句之
    ER 行、pre_conditions、input_test_data 一律用 `"..."`（IN §11 本文）。
(c) **驗證方式**：保留之 token 須能於所錨之 cited source row 逐字對上
    （IN §11 Exception 本文之 lint 規定）。本 feature 之對比器為
    `scripts/verify_verbatim_b01.py`；對不上即為違規，不得以本條免責。
```

先例：`driver_distraction` **R-DD12**（同一件事，同一驗證方式）。

---

## §2 其餘節次 —— **無 override**

本檔僅就 IN §11 立 override。其餘一律依 IN 與全域裁決；
本 feature 之 feature-scoped 條文全數落於
`features/ics_management/RULINGS.md`（R-ICS1 ~ R-ICS21），不重述於此。
