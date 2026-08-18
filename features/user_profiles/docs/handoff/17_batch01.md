# 17 下放包 — PLP 引用口徑、ER 出處對照、第一批取樣核可

**本包無裁決條文。** 覆核判定與作業指示屬分析層自裁。

16 輪上繳包**核可**。F-1／F-3／F-4 處置成立；
F-2 之版面重繪為本輪最重要之方法突破。

## 覆核判定

### J-1 —— PLP `3.x` 併列採「條文對象讀」（§7 第 1 項之待裁）

**採執行層之判斷，不改 TC-001／TC-004 之引用欄。**

理由：4.1 之文為 store **all** preferences **listed in PLP table**、
5.9 之文為 not required to save **any** of the Driver Profile linked
preferences —— **該需求之對象本來就是整張表**，TC 是對它抽樣。
採嚴格讀則 `specification_reference` 會隨「這次抽了哪幾列」而變，
**同一條需求之追溯欄因抽樣而不同，那就不是追溯了**。

F-1 之字面（「真的被該 TC 驗證或倚為 setup」）指向 must_carry 多節掛回
那種**頁面共置**之誤入，與本項不同：11.5 之於 TC-013 是**另一條需求**，
3.x 之於 TC-001／004 是**同一條需求之對象**。兩者不可類推。

**代價，明文記載（R-G11 之盲區聲明）**：
`specification_reference` 併列 3.1–3.5 **不等於該五列皆已被驗證**。
覆蓋率稽核**不得以引用欄推定覆蓋**；PLP 各列之實際覆蓋深度由 F-4／
D-UP16-02 之全稱問題承擔。此句須寫入 `DECISIONS.md` 與覆蓋稽核之判準。

### J-2 —— 版面重繪落為腳本（§7 第 3 項）

`scripts/render_spec_region.py`（頁次、裁切區、倍率為參數）。
**本輪即需要**：第一批含 `PROF-106`（10.2，三欄表）與 `PROF-108`
（10.3.1，頁內 chart），與 Table CPA2 同型 ——
文字層攤平、版面仍在。手動跑一次可以，跑第三次就該是工具。

### J-3 —— 第一批取樣清單**核可**

27 leaf ＋ `PROF-111` 之 R1 High 反面，估 28–34 條 TC。
批界設計成立：本批做完 **Editing 25 之剩餘 23** 與
**Connected Account 6 之剩餘 4**，兩個 Test Set 一次收乾淨，
不留零頭跨批。ch12–14（Valet 31 leaf）另成一批之判斷同意。

三項必含皆落在範圍內且非為湊而挑：`PROF-085` 一條同時覆蓋 T-1／T-2、
`PROF-111` 反面、`112-02/03` 與 pilot 之 `112-01` 構成完整列舉。

## 作業

### A. J-1／J-2 落地

1. J-1 之代價句寫入 `DECISIONS.md`（新條），並註記於覆蓋稽核之判準處
2. `scripts/render_spec_region.py` 落為工具，含一個回歸案例
   （重跑 p17 表格區，結果須與 16 輪之判讀一致）

### B. **ER 出處對照表（分析層之逐字複核，本輪之主要產出）**

pilot 16 條之 spec 逐字複核為分析層待辦，
而本層無法逐一翻查 `outline_map.json`。**由執行層產出對照，分析層判讀。**

產出 `docs/upstream/17_er_provenance.md`，對 **16 條之每一句 ER**：

| 欄 | 內容 |
|---|---|
| tc_id / ER 行號 | —— |
| ER 原句 | 逐字 |
| 出處節次 | 該句所據之 spec section |
| `pdf_text` 片段 | **逐字節錄**，足以判斷該 ER 是否為其所述 |
| 關係 | `逐字引用` / `改寫自` / `由該句推得` / **`無直接出處`** |

**`無直接出處` 者須逐條具名**，不得以「合理推得」帶過 ——
那正是這張表要找的東西。
ER 中之字面值（label、popup 字串、數字、清單項）**一律標其出處**。

### C. 第一批生成（B 完成後同輪執行）

取樣依 16 輪 §6.4 之 27 leaf ＋ `PROF-111` R1 High 反面。

- `data/pilot_sample.tsv` 之同型檔落為 `data/batch01_sample.tsv`
- 生成前跑 `--selfcheck`；生成後跑全部 lint 與 self-test
- **16 輪 §6.5 之六項風險逐項回報其實際結果**，尤其：
  - `PROF-085` 之 p14 must_carry 含 `Stellantis Account` 字面值 →
    R1 High 之 TC 須寫 `Connected Account`，驗 `lint_variant_labels` 是否確實擋下
  - 9.5.x 四條座椅交換之 sibling 軸辨識（§8.3）與 G5
  - ch10 三條之 037 先驗全為 Low —— **逐條依 rubric 判，不得機械給 P2**
- 生成物落 `generated/`，**不寫回工作簿**（R-U14）

## 不在本包授權範圍

- 任何 git 操作（R-G5／R-G12）
- 寫回工作簿（R-U14）
- ch12–14（Valet Mode）之生成 —— 另批

## 上繳

`docs/upstream/17_er_provenance.md`（作業 B）＋
`docs/upstream/17_batch01.md`（作業 A、C），更新 `docs/INDEX.md`，
附獨立判斷。第一批 TC 全文附上或指明 `generated/` 路徑。
