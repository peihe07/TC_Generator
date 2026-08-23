# INDEX — FW036 Vehicle Setting

執行層於每次上繳時更新（canon §8.7）。分析層不寫此檔。

| NN | 日期 | 主題 | 下放 | 上繳 | 新條文 | 新 anomaly | 結果 |
|---|---|---|---|---|---|---|---|
| 00 | 2026-08-20 | 進場、裁決落檔、Phase 0/1 偵察 | [handoff/00_intake_and_rulings.md](handoff/00_intake_and_rulings.md) ＋ 補篇 [00A](handoff/00A_data_requests_refined.md)／[00B](handoff/00B_named_documents.md)／[00C](handoff/00C_inputs_verification.md)／[00D](handoff/00D_tlm_hmi_document_search.md)／[00E](handoff/00E_open_items.md)／[00G](handoff/00G_lid_mapping.md)／[00H](handoff/00H_dbc_release_semantics.md)／[00I](handoff/00I_claude_code_prompt_v2.md) | [upstream/00_intake_and_rulings.md](upstream/00_intake_and_rulings.md) | R-VS1–R-VS6（分析層）、R-VS12（授權） | A-VS12–A-VS19、A-VS06′ | **A 組部分完成；W-8／W-9／W-13 未執行** |
| 01 | 2026-08-20 | leaf 母體判準追因、N 欄未定收斂 | [handoff/01_review_and_rulings.md](handoff/01_review_and_rulings.md)／[02_coverage_baseline_correction.md](handoff/02_coverage_baseline_correction.md) | [upstream/01_leaf_universe.md](upstream/01_leaf_universe.md) | R-VS13（授權）、R-VS14、**R-VS15**（待追認） | A-VS20；A-VS01／A-VS18 **除役**、A-VS06→A-VS06′ | **W-0c／W-16／W-18 完成；W-8／W-9／W-13／W-15b′／W-17 未執行** |
| 02 | — | 值域三來源比對、HMI 目錄餘數掃描、殘項收尾 | [02](handoff/02_coverage_baseline_correction.md) ⟨依自述往返 NN⟩ | [upstream/02_variables_and_sweep.md](upstream/02_variables_and_sweep.md) | R-VS16、R-VS18、R-VS19、R-VS21–23 | A-VS21–24 | —（未回填） |
| 03 | — | DBC↔LID 逐屬性交叉、Comfort 重疊、餘數驗證 | [03](handoff/03_round01_prompt.md) ⟨依自述往返 NN⟩ | [upstream/03_crosscheck_and_overlap.md](upstream/03_crosscheck_and_overlap.md) | R-VS24 | A-VS25–28 | —（未回填） |
| 04 | — | 解析式修正、餘數驗證、Comfort 重疊 | [04](handoff/04_review_round01.md) ⟨依自述往返 NN⟩ | [upstream/04_extraction_and_overlap.md](upstream/04_extraction_and_overlap.md) | R-VS25 | A-VS29 | —（未回填） |
| 05 | — | 解析式修正驗收、餘數驗證、Comfort 重疊 | [05](handoff/05_rulings.md) ⟨依自述往返 NN⟩ | [upstream/05_parser_fix_and_residual.md](upstream/05_parser_fix_and_residual.md) | R-VS17、R-VS26 | A-VS30 | —（未回填） |
| 06 | — | Comfort 逐條對照（R-VS7 委派句之來源表） | [06](handoff/06_round02_prompt.md) ⟨依自述往返 NN⟩ | [upstream/06_comfort_overlap.md](upstream/06_comfort_overlap.md) | R-VS27、R-VS28 | A-VS31 | —（未回填） |
| 07 | — | 值域抽取之餘數驗證 | [07](handoff/07_review_round02.md) ⟨依自述往返 NN⟩ | [upstream/07_residual_verification.md](upstream/07_residual_verification.md) | R-VS29、R-VS32–34 | A-VS32–34 | —（未回填） |
| 08 | — | 極性回算、委派表精度、小項打包 | [08](handoff/08_round03_prompt.md) ⟨依自述往返 NN⟩ | [upstream/08_polarity_and_delegation.md](upstream/08_polarity_and_delegation.md) | — | A-VS35–38 | —（未回填） |
| 09 | — | 反向覆蓋之歸因、極性之下游回算、未分左右複核 | [09](handoff/09_review_round03.md) ⟨依自述往返 NN⟩ | [upstream/09_reverse_coverage.md](upstream/09_reverse_coverage.md) | R-VS20、R-VS35 | A-VS39、A-VS40 | —（未回填） |
| 10 | — | 判準之反向驗證、負向掛載、framework Layer 3 草案 | [28](handoff/28_review_round11.md) | [upstream/10_criterion_and_framework.md](upstream/10_criterion_and_framework.md) | R-VS36 | A-VS2、A-VS41–44 | —（未回填） |
| 11 | — | Atlantis Mid 之範圍證據、階數維度全量複核、左右對稱追因 | [29](handoff/29_review_round12.md) | [upstream/11_arch_scope.md](upstream/11_arch_scope.md) | — | A-VS45–47 | —（未回填） |
| 12 | — | 委派收斂重做、HSW 階數複核、Layer 3 全掃 | [30](handoff/30_review_round13.md) | [upstream/12_layer3_and_convergence.md](upstream/12_layer3_and_convergence.md) | R-VS37 | A-VS48–50 | —（未回填） |
| 13 | — | 交叉前綴污染全掃、Vented 兩節對照、framework 定稿前檢查 | [31](handoff/31_review_round14.md) | [upstream/13_contamination_and_symmetry.md](upstream/13_contamination_and_symmetry.md) | — | A-VS51–54 | —（未回填） |
| 14 | — | 值域正規化、CUSW 節族、framework 鎖定前驗證、R-VS19′ 連帶重算 | [33](handoff/33_rulings5.md) | [upstream/14_normalization_and_lock.md](upstream/14_normalization_and_lock.md) | R-VS38、R-VS39 | A-VS55、A-VS56 | —（未回填） |
| 15 | — | 首批 TC 生成（10 條） | [34](handoff/34_pilot_batch.md) | [upstream/15_pilot_batch.md](upstream/15_pilot_batch.md) | R-VS40 | A-VS57–61 | —（未回填） |
| 16 | — | batch01 改寫（10 條）與 feature profile 建檔 | [35](handoff/35_pilot_review1.md) | [upstream/16_batch01_rework.md](upstream/16_batch01_rework.md) | R-VS41 | — | —（未回填） |
| 17 | — | batch01_v3（缺陷修正、10 降 8）與 batch02（第二批 10 條） | [38](handoff/38_pilot_review2.md) | [upstream/17_batch01_v3_and_batch02.md](upstream/17_batch01_v3_and_batch02.md) | — | A-VS62–65 | —（未回填） |
| 18 | — | 全量可寫性掃描（237 leaf） | [39](handoff/39_review_round19.md) | [upstream/18_writability.md](upstream/18_writability.md) | R-VS42 | A-VS66–69 | —（未回填） |
| 19 | — | 可寫性之精化、可生成量、兩個判準之召回率 | [40](handoff/40_review_round20.md) | [upstream/19_writability_refined.md](upstream/19_writability_refined.md) | R-VS43 | A-VS70–72 | —（未回填） |
| 20 | — | 可寫性之最後收斂、R-VS44 實作、batch03 | [41](handoff/41_review_round21.md) | [upstream/20_stable_core.md](upstream/20_stable_core.md) | R-VS44 | A-VS74–76 | —（未回填） |
| 21 | — | PROXI Table 之唯讀搜尋、兩個掃描盲區、batch04 | [42](handoff/42_review_round22.md) | [upstream/21_proxi_hunt.md](upstream/21_proxi_hunt.md) | R-VS45 | A-VS77–80 | —（未回填） |
| 22 | — | VF664 與型 B 之一次搜尋、閘之修正、batch05 | [43](handoff/43_review_round23.md) | [upstream/22_vf664_hunt.md](upstream/22_vf664_hunt.md) | — | A-VS81–83 | —（未回填） |
| 23 | — | DR-15 曝險之全量掃描、batch06、batch07 | [44](handoff/44_review_round24.md) | [upstream/23_dr15_exposure.md](upstream/23_dr15_exposure.md) | — | A-VS84–86 | —（未回填） |
| 24 | — | 形態窮舉收尾、batch08、batch09 | [45](handoff/45_review_round25.md) | [upstream/24_batch0809.md](upstream/24_batch0809.md) | R-VS46 | A-VS87、A-VS88 | —（未回填） |
| 25 | — | 可寫性重分級、docx 表格抽取、batch10 | [46](handoff/46_review_round26.md) | [upstream/25_regrade.md](upstream/25_regrade.md) | R-VS47 | A-VS89–92 | —（未回填） |
| 26 | — | R-VS48 之實作、內嵌圖片清點、batch10 | [47](handoff/47_review_round27.md) | [upstream/26_uniqueness.md](upstream/26_uniqueness.md) | R-VS48 | A-VS93、A-VS94 | —（未回填） |
| 27 | — | PROXI 值域併入、(b) 路複查、pilot #2 清單、batch11／12 | [49](handoff/49_proxi_adoption.md) | [upstream/27_proxi_and_pilot2.md](upstream/27_proxi_and_pilot2.md) | R-VS49 | A-VS95、A-VS96 | —（未回填） |
| 28 | — | `*_Cmd_Tlm` 之 LID 回查、pilot #2 defect 修正、適用性前言全掃 | [50](handoff/50_review_round29.md)／[51](handoff/51_pilot2_review.md) | [upstream/28_cmd_tlm.md](upstream/28_cmd_tlm.md) | R-VS50 | A-VS97–100 | —（未回填） |
| 29 | — | R-VS51 之架構欄組分流、batch13、batch14 | [52](handoff/52_review_round31.md)／[53](handoff/53_pilot2_verdict.md) | [upstream/29_arch_columns.md](upstream/29_arch_columns.md) | R-VS51 | A-VS101–104 | —（未回填） |
| 30 | — | 依 SWC 0708 對齊書寫形式、writability 驅動化、batch13 | [54](handoff/54_swc_alignment.md)／[55](handoff/55_review_round32.md) | [upstream/30_swc_alignment.md](upstream/30_swc_alignment.md) | R-VS52、R-VS53 | A-VS105–108 | —（未回填） |
| 31 | — | record 子句之處置、batch13、交付本樣式比對 | [56](handoff/56_review_round34.md) | [upstream/31_record_and_batch13.md](upstream/31_record_and_batch13.md) | R-VS54 | A-VS109–112 | —（未回填） |
| 32 | — | 判準補完、Priority 重判、batch13 | [57](handoff/57_review_round35.md) | [upstream/32_alignment_and_gate.md](upstream/32_alignment_and_gate.md) | R-VS55–57 | A-VS113–117 | —（未回填） |
| 33 | — | pilot #3 sheet、batch14（R-VS58 優先序）、18 leaf 可寫性實測 | [60](handoff/60_review_round36.md) | [upstream/33_priority_pool.md](upstream/33_priority_pool.md) | R-VS58 | A-VS118–121 | —（未回填） |
| 34 | — | 母體層冗餘掃描、R-VS57(4) 重跑、產能終局盤點 | [61](handoff/61_review_round37.md) | [upstream/34_redundancy_and_batch15.md](upstream/34_redundancy_and_batch15.md) | R-VS59、R-VS61、R-VS63 | A-VS122–124、A-VS128 | —（未回填） |


> **本表 NN≥02 之列由 `scripts/index_backfill.py` 機械回填（38 輪，61 包 §8）。**
> **NN 為往返輪次**（`docs/upstream/` 之序，現至 34），
> **與 handoff 之包號（現至 61）為兩套計數**，不可以號相等配對。
> 「下放」欄自各上繳前段之**逐字引用**（`docs/handoff/…md`）解出，
> 一輪可對多包。標 ⟨依自述往返 NN⟩ 者為該上繳未逐字引用下放包、
> 僅自述「往返 NN = NN」，故以同號之 handoff 推得 —— **該對應為推得，非引用**。
> 「新條文」／「新 anomaly」之判準為**該輪之下放或上繳為 `docs/` 內
> 首次提及該編號之文件**，非「該輪裁定成立」—— 一條文可先於某輪
> 被提及而於後輪方裁定。
> **「日期」與「結果」兩欄未回填** —— 二者需逐輪之判斷，不由機械產生；
> 其實質以各列所連之上繳文件為準。此即 61 包所允之「具名說明未補之範圍」。

### 尚無對應上繳之下放包（25 件）

下列包未被任何上繳自述為依據 —— 或為補篇／指令書，或其輪次尚未上繳。

| 包號 | 主題 |
|---|---|
| [10](handoff/10_p_actions.md) | P1／P2／P10 之執行程序，與 R-VS16 之技術更正 |
| [11](handoff/11_commit_authorization.md) | P2 入庫之窄口授權與指令 |
| [12](handoff/12_post_commit.md) | 入庫覆核、P1 關閉、附錄授權、04 輪開跑 |
| [13](handoff/13_round04_prompt.md) | 04 輪啟動指令（取代 08） |
| [14](handoff/14_review_round04.md) | 04 輪覆核：兩條異常降級、一條成立、R-VS9 須改權威 |
| [15](handoff/15_rulings2_round05.md) | 裁決第二批（R-VS18～R-VS24）與 05 輪指令 |
| [16](handoff/16_review_round05.md) | 05 輪覆核、衍生檔紀律、06 輪頭部裁定 |
| [17](handoff/17_rulings3_round06.md) | R-VS26 裁定、DR-15 登記、06 輪指令 |
| [18](handoff/18_review_round06.md) | 06 輪覆核、錨點措辭之更正、C4 判準之補強 |
| [19](handoff/19_rulings4_round07.md) | R-VS27／R-VS28 裁定與 07 輪指令 |
| [20](handoff/20_review_round07.md) | 07 輪覆核、反向委派表、08 輪指令 |
| [21](handoff/21_self_determination.md) | R-VS29 裁定、自裁界線之重申、待 Pei 項之呈報方式 |
| [22](handoff/22_w22_adjudication.md) | W-22 之 (b) 裁定、判準參數之固定、續作指示 |
| [23](handoff/23_reqid_ruling.md) | R-VS33：spec_reference 取 CFTS044 reqid，及其素材缺口 |
| [24](handoff/24_reqid_source_correction.md) | R-VS33 之取值來源更正；DR-16 撤銷 |
| [25](handoff/25_review_w32.md) | W-32 覆核、09 輪指令 |
| [26](handoff/26_review_round09.md) | 09 輪覆核、R-VS7(a)/(b) 之讀法、10 輪指令 |
| [27](handoff/27_review_round10.md) | 10 輪覆核、反向覆蓋之實測、11 輪指令 |
| [32](handoff/32_review_round15.md) | 15 輪覆核：typo 判據定案、值域正規化、DR-18、16 輪指令 |
| [36](handoff/36_framework_signoff.md) | framework 簽核（P19）與鎖定 |
| [37](handoff/37_rd1_dispatch.md) | RD-1 送件文（合併八項）與狀態更新 |
| [48](handoff/48_review_round28.md) | 產能恢復、R-VS48′ 收緊 (b) 路、pilot #2 清單、29 輪 |
| [58](handoff/58_priority_definition.md) | Priority 判準之定義（R-VS56） |
| [59](handoff/59_dr25_ruling.md) | DR-25 之處置裁定（R-VS57）、36 輪修訂 |
| [61](handoff/61_vf230_intake.md) | VF230 進場（Part 2）：裁決落檔、素材清冊、P0/P1 指示 |

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

---

## 舊路徑對照（R-VF23 搬移，2026-08-23；W-VF33）

VF230 線之 handoff／upstream 檔於 `495b541` 收斂為 `V{NN}_` 平鋪。
**歷史檔內之舊路徑引用一律不追改**（R-VF18／R-VF31 二之處置 1）——
本表使失效連結可追。

| 舊路徑 | 新路徑 |
|---|---|
| `docs/upstream/vf230/00_intake.md` | `docs/upstream/V01_vf230_intake.md` |
| `docs/upstream/vf230/01_recon.md` | `docs/upstream/V02_vf230_recon.md` |
| `docs/upstream/61_vf230_intake.md` | `docs/upstream/V01_vf230_intake.md` |
| `docs/upstream/62_vf230_recon.md` | `docs/upstream/V02_vf230_recon.md` |
| `docs/handoff/61_vf230_intake.md` | `docs/handoff/V01_vf230_intake.md` |
| `docs/handoff/62_vf230_recon_review.md` | `docs/handoff/V02_vf230_recon_review.md` |
| `docs/handoff/63_test_group_ruling.md` | `docs/handoff/V03_test_group_ruling.md` |
| `docs/handoff/ZZ_vf230_numbering_collision.md` | `docs/handoff/V00_numbering_collision.md` |

**引用面實測（W-VF33，2026-08-23 復測，不沿用 V11 之「2 處」）**：
全庫 **68 處**／**24 檔**。其中位於 `docs/handoff/`、`docs/upstream/`、
`docs/reports/` 者為歷史紀錄，依 R-VF18 不追改；
`RULINGS.md` 之 9 處為執行層註內對當時路徑之記述，同屬歷史。
**現行有效而須改者：0**（`scripts/vf230_wvf24_converge.py` 之搬移表為
該工單之產物，其列舊路徑即其用途；`scripts/grade_overrides.py` 之
`vf230/` 為 R-VF40 檢查一之判準文字，刻意保留）。

