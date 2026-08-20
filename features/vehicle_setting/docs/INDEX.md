# INDEX — FW036 Vehicle Setting

執行層於每次上繳時更新（canon §8.7）。分析層不寫此檔。

| NN | 日期 | 主題 | 下放 | 上繳 | 新條文 | 新 anomaly | 結果 |
|---|---|---|---|---|---|---|---|
| 00 | 2026-08-20 | 進場、裁決落檔、Phase 0/1 偵察 | [handoff/00_intake_and_rulings.md](handoff/00_intake_and_rulings.md) ＋ 補篇 [00A](handoff/00A_data_requests_refined.md)／[00B](handoff/00B_named_documents.md)／[00C](handoff/00C_inputs_verification.md)／[00D](handoff/00D_tlm_hmi_document_search.md)／[00E](handoff/00E_open_items.md)／[00G](handoff/00G_lid_mapping.md)／[00H](handoff/00H_dbc_release_semantics.md)／[00I](handoff/00I_claude_code_prompt_v2.md) | [upstream/00_intake_and_rulings.md](upstream/00_intake_and_rulings.md) | R-VS1–R-VS6（分析層）、R-VS12（授權） | A-VS12–A-VS19、A-VS06′ | **A 組部分完成；W-8／W-9／W-13 未執行** |

## 00 輪要點

- **41 項預期數字相符**（271 leaf／56·99·81·35／237 列／I·H·N 各 237／34 未覆蓋／
  538 SYS2 列／offset 31·0·0／Category 239·25·9／270 heading／2030 需求段落／245·25·1／
  DBC 883·155 與 1755·323／2,974 相異 LID …）
- **七項不符，全部未調和** —— 見上繳 §2
- **錨鏈於 1 leaf 不成立**（`SWE1-VC-HeatedSteeringWheel-009` → `SYS-RA-CFTS100`，
  指向 CFTS100 且無 `-N`）；下放包所記之原因與實測不同
- **A-VS15 改變 R-VS11 之問題形態** —— `Proxi & Configuration` 之列 2 欄組標題
  逐字為 `Atlantis & Atlantis High`，該分頁無獨立 Atlantis High 欄組；
  00G 之「10 個空欄」係讀列 3 逐欄表頭而未讀列 2 欄組所致
- **A-VS17 使 R-VS9 草案不足** —— 兩份 DBC 之 141 個共有 signal 中 **128 個起始位元不同**
- **A-VS06′** —— 原記之「270 對 254，差額 16」於原始 docx 不重現，實測 270 對 270、差額 0

## 未執行（具名）

`W-8`（三來源 `$變數$` 對照）、`W-9`（Comfort 43 leaf 逐條對照，B 組必停項）、
`W-13`（26PI2.5/HMI 約 112 檔全文掃描）、`W-15(b)` 之 DBC ↔ LID 表逐屬性交叉比對。

## 待裁（本輪未預設答案）

`R-VS7` Comfort 委派界線／`R-VS9` CAN 訊號書寫形式（**建議增列「須指明 message 與網段」**）／
`R-VS10` Pop Up List 基線版本／`R-VS11` Atlantis 欄可代用性（**A-VS15 為新素材**）／
`R-VS8` 待 Pei 追認（本輪依改寫版作業，未據以更動任何交付內容）
