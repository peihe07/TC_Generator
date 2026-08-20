# INDEX — FW036 Vehicle Setting

執行層於每次上繳時更新（canon §8.7）。分析層不寫此檔。

| NN | 日期 | 主題 | 下放 | 上繳 | 新條文 | 新 anomaly | 結果 |
|---|---|---|---|---|---|---|---|
| 00 | 2026-08-20 | 進場、裁決落檔、Phase 0/1 偵察 | [handoff/00_intake_and_rulings.md](handoff/00_intake_and_rulings.md) ＋ 補篇 [00A](handoff/00A_data_requests_refined.md)／[00B](handoff/00B_named_documents.md)／[00C](handoff/00C_inputs_verification.md)／[00D](handoff/00D_tlm_hmi_document_search.md)／[00E](handoff/00E_open_items.md)／[00G](handoff/00G_lid_mapping.md)／[00H](handoff/00H_dbc_release_semantics.md)／[00I](handoff/00I_claude_code_prompt_v2.md) | [upstream/00_intake_and_rulings.md](upstream/00_intake_and_rulings.md) | R-VS1–R-VS6（分析層）、R-VS12（授權） | A-VS12–A-VS19、A-VS06′ | **A 組部分完成；W-8／W-9／W-13 未執行** |
| 01 | 2026-08-20 | leaf 母體判準追因、N 欄未定收斂 | [handoff/01_review_and_rulings.md](handoff/01_review_and_rulings.md)／[02_coverage_baseline_correction.md](handoff/02_coverage_baseline_correction.md) | [upstream/01_leaf_universe.md](upstream/01_leaf_universe.md) | R-VS13（授權）、R-VS14、**R-VS15**（待追認） | A-VS20；A-VS01／A-VS18 **除役**、A-VS06→A-VS06′ | **W-0c／W-16／W-18 完成；W-8／W-9／W-13／W-15b′／W-17 未執行** |

## 00 輪要點

- **41 項預期數字相符**（037 之 **271 列**／56·99·81·35／036 之 237 列／I·H·N 各 237／538 SYS2 列／offset 31·0·0／Category 239·25·9／270 heading／2030 需求段落／245·25·1／DBC 883·155 與 1755·323／2,974 相異 LID …）
- **七項不符，全部未調和** —— 見上繳 §2
- **錨鏈於 1 leaf 不成立**（`SWE1-VC-HeatedSteeringWheel-009` → `SYS-RA-CFTS100`，
  指向 CFTS100 且無 `-N`）；下放包所記之原因與實測不同
- **A-VS15 改變 R-VS11 之問題形態** —— `Proxi & Configuration` 之列 2 欄組標題
  逐字為 `Atlantis & Atlantis High`，該分頁無獨立 Atlantis High 欄組；
  00G 之「10 個空欄」係讀列 3 逐欄表頭而未讀列 2 欄組所致
- **A-VS17 使 R-VS9 草案不足** —— 兩份 DBC 之 141 個共有 signal 中 **128 個起始位元不同**
- **A-VS06′** —— 原記之「270 對 254，差額 16」於原始 docx 不重現，實測 270 對 270、差額 0

## 01 輪要點

- **R-VS15 立**（待 Pei 追認）：可測母體 **237**（Common 46／Heated Seat 88／
  Vented Seat 72／Heated Steering Wheel 31）。**「34 個未覆蓋 leaf」之表述作廢 ——
  本 feature 沒有覆蓋缺口。** 271 僅描述 037 之列數，不得作為任何比率之分母
- **W-16 追因**：`recon.py:602` 依 `Categorization` 過濾，下放包 §5.1 依「A 欄非空」——
  **兩判準在數兩件不同的事**；非 Functional 之 34 個 leaf 與 036 未覆蓋之 34 個
  **為完全相同之集合**（交集 34、兩側差集 0、逐 family 10／11／9／4）。**recon 未錯**
- **W-18 收斂**：26 個 N 欄未定 → **1 個**（25 個為非 Functional，不產 TC 即無 N 欄）。
  可測母體下為 **236 / 237 已定**
- **A-VS01 除役**：037 `Categorization` 對 SYS2 `Category` 逐 leaf **零錯配** ——
  25 個 Heading 是兩份文件各自正確標記，非錯配。**本輪唯一之跨源檢驗**
- **位元層核對**：`ANOMALIES.md`「相異 259」後與 `00 §1 第 6 點`「沙」後
  **兩處皆無毀損**（嚴格 UTF-8 通過、U+FFFD 0；「沙」後為「箱」）。
  分析層所見之 `沙??` 為其端顯示產物

## 未執行（具名）

`W-8`（三來源 `$變數$` 對照）、`W-9`（Comfort 逐條對照，**母體改 237**，必停項）、
`W-13`（26PI2.5/HMI **107** 檔全文掃描）、`W-15(b)` 之 DBC ↔ LID 表逐屬性交叉比對。

## 待裁（本輪未預設答案）

`R-VS7` Comfort 委派界線／`R-VS9` CAN 訊號書寫形式（**建議增列「須指明 message 與網段」**）／
`R-VS10` Pop Up List 基線版本／`R-VS11` Atlantis 欄可代用性（**A-VS15 為新素材**）／
`R-VS8` 待 Pei 追認（本輪依改寫版作業，未據以更動任何交付內容）
