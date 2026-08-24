# 90 下放包 — 主線收尾：狀態板更新

分析層寫入，2026-08-24。**主線 CFTS044 之最後一份下放包。**

Pei 指示：更新狀態板即收尾；VF230 線不在本包範圍。

---

## 1. 何以此為必做

`PLAYBOOK.md` §6 為 `接手` 讀取清單之第 2 項（R-VF38 二）。
其現載為 **50 輪前之狀態**，與現況之落差如下：

| 板上 | 實際 |
|---|---|
| P6 未勾；「4 PENDING lines across 2 TCs」 | **225 TC 已寫回母本 243 列** |
| P5 pilot 01、8 條 | pilot #1–#6 累計 **69 條**經人工關卡 |
| P7 未勾；tag／submitted 空白 | 母本 `c72b9556…`；`DELIVERY.md` 11 節定稿 |
| DR 表 4 待送 | 送出 5、撤回 2（DR-8′／DR-25′）、新增至 DR-35 |

**不更新即收尾者，下次接手會以錯誤之基準往下做。**

---

## 2. 下放包（貼入 Claude Code）

```text
你是 FW036 管線之執行層。repo: /Users/peihe/Work_Projects/TC_Generator
**主線 CFTS044 之收尾**：更新狀態板，其餘不動。

讀：features/vehicle_setting/docs/handoff/90_closeout.md（本檔）
    ＋ features/vehicle_setting/docs/reports/DELIVERY.md
    ＋ features/vehicle_setting/DATA_REQUESTS.md

## 唯一作業

W-175  更新 `features/vehicle_setting/PLAYBOOK.md` **§6 狀態板**：

  P5  勾。verdict 改為：
      pilot #1 PASS（Pei 2026-08-22，8 條）／pilot #2 PASS（15 條）／
      pilot #3＋#4 不通過→七項 defect 修畢後 PASS（28 條）／
      pilot #5＋#6 不通過→五項 defect 修畢後 PASS（18 條）
      **累計 69 條經人工關卡（225 之 31%）**

  P6  勾。改為：
      **225 TC 涵蓋 219 leaf**；母體 237 之三類為
      有 TC 219／held_out 7／`generatable = no` 11（R-VS76 完整性 PASS）
      機械檢查：§9 十七項 0／固定錨點 20/20／五項 defect 0／
      R-VS77 八判準 0／**L3 全量 225/225 不符 0**

  P7  dry-run 勾（47 輪，四錨點可失敗）。改為：
      母本 `c72b9556…`（243 列，資料列 10–252）；
      `DELIVERY.md` 11 節定稿（§0 交付物之實際狀態在首）；
      附件三份（`writability.tsv`／`REGEN_ORDER.md`／`DATA_REQUESTS.md`）；
      RD-1 已送 5 項（2026-08-22）；
      **tag 與 submitted 仍空白 —— 其屬 Pei**

  DR 表  以 `DATA_REQUESTS.md` 之現況重列，**待送／待覆分列**；
         撤回者（DR-8′／DR-25′）標其撤回之依據條文

  **交付物之已知限制**（自 `DELIVERY.md` §0 逐字取，四項）：
      R 欄無選單；P 欄與 T–Z 欄自第 133 列起無選單
        —— 修復範圍 `R10:R252`／`P10:P252`／`T10:Z252`（A-VS153 未關閉）
      11 批 80 條之首版不可重放，其變更鏈經實跑證實缺一層（A-VS162／163／164）
      156 條（69%）未經人工覆核
      就地改動實為 5 commit／26 檔次／24 檔，含實質欄位

  **未結之作業**（列於狀態板末，供接手者判）：
      60 輪之 W-172／W-173／W-174 未執行；
      其中 **W-172(2)**（`70b75d0` 之 15 檔次其下放包依據未查）**有實質**
      —— 若無依據，即為無授權之變更落在已交付之產物內；
      其餘二項為可稽核性之整潔度

  **不改 PLAYBOOK 之其餘各節。不改任何其他檔。**

## 禁區
git 不執行。不改動母本、不改動 `generated/`、不改其他 .md。
不補素材、不代擬。

## 完成後
回報更新後之 §6 全文，供分析層核其與本包所列一致。
**本輪後主線 CFTS044 收尾；VF230 線不在本包範圍。**
```

---

## 3. 主線之最終狀態（存查）

| 項 | 值 |
|---|---|
| 母體 | **237** Functional leaf |
| 交付 | **225** TC 涵蓋 **219** leaf |
| held_out ／ 不可寫 | 7 ／ 11（**和 237**） |
| 人工關卡 | **69**（31%） |
| 母本 | `c72b9556…`，243 列 |
| 條文 | R-VS1 ～ R-VS81（含 primes） |
| anomaly | A-VS 主線 162 相異（最大 A-VS164） |
| DR | 送出 5 待覆／撤回 2／其餘待送 |
| 輪次 | 00 ～ 59（60 輪未執行） |

---

## 4. 待 Pei（**主線之全部**）

| # | 事項 |
|---|---|
| 1 | **交付執行** —— 工作簿 ＋ `DELIVERY.md` ＋ 三份附件 |
| 2 | 下拉修復 —— `R10:R252`／`P10:P252`／`T10:Z252` |
| 3 | tag 與 submitted 之填入（`PLAYBOOK.md` §6 之 P7） |
| 4 | 入庫與推送（git 屬 Pei） |

---

## 5. 本包產生之新條文清單（自檢）

無新條文。本包為收尾之狀態更新。
