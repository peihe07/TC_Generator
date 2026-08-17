# 02b 下放包 — User Profiles 作業指示（執行層）

裁決見 `02a_rulings.md`。**01 輪核可，無退回項。**
本輪多為 canon 級修改，凡動 `docs/` 之檔者須於上繳附 diff 摘要。

## 不等 DR #1 即可執行（1–5）

1. **RULINGS.md 追加** R-U8、R-U9、R-G3、R-U10、R-U11、R-U12 逐字。
   R-U8 明記其取代 `01b_tasks.md` 作業項 3 之預期值；01 輪之下放包不改寫
   （已結輪次不回溯編輯），以 supersede 註記處理。

2. **R-U9 PU 涵蓋驗證** — 對 `features/comfort/inputs/Pop Up List HMI R1
   SR24 Post 2A (Dec 15, 2023).xlsx` 驗本 feature `data/spec_popup_ids.tsv`
   之 20 個 id。量測條件須自陳：抽取式、是否含詞界、底線／空白分隔是否
   涵蓋（§4.3 之漏抽同型風險）。
   - 涵蓋 20/20 → 依 R-U9 移入 `spec-index/`，更新 BASELINE，A-UP06 結案
   - 不足 → 具名列出缺哪幾個 id，轉 DR，**不以近似版本替代**

3. **R-G3 canon 修補** — `docs/fw036/framework.md` §Workbook sync：
   加禁用警示（引 A-UP09 實測表），範例改寫為 xlsx_surgical splice。
   同節依 **R-U10** 將 `Test Case Framework` 分頁項改標「rev A/B only」。
   兩處為同節修改，一併提交。

4. **R-U12** — 建 `archive/forms_superseded/BASELINE.sha256`（三檔），
   `shasum -a 256 -c` 須 3/3 OK 並附輸出。

5. **ANOMALIES.md 狀態更新** — A-UP03 RESOLVED（01 輪已辦）、
   A-UP05 RESOLVED（R-U11，**須照錄其「非經成因查證」之記載限制**）、
   A-UP07 RESOLVED（R-U8）、A-UP08 RESOLVED（R-U10）、
   A-UP09 保持 PENDING 直至 R-G3 修補完成。
   A-UP02／A-UP04／A-UP06 維持 PENDING。

## 等 DR #1（037 進 inputs/）方可執行（6–8）

6. **Recon** — 以 R-U8 三閘執行；`feature.yaml` 之 `recon_assertions`
   由 `TBD` 改填 180／25／2。182 以對照輸出呈現，不作閘。
   不符即停，不得調整判準。

7. **037 側複驗**（01 輪列為未實測者，逐項補）— header row 7、
   FROP 欄 182 列值、PROF-017／035 之 Out of scope 身分、
   引用 135 id 與 `data/expected_cited_sections.tsv` 之**集合對集合**比對
   （非計數比對）、Sub Categorization 與 Priority 分布。
   **BASELINE.sha256 須加入 037**。

8. **Layer 2 草案（第二版）** — 037 分群到齊後重出，須同時處理 §4.2：
   `All Profiles Tab` 為 UI widget 名、`Profile Overview`／
   `New Profile Setup` 與 Test Group `User Profiles` 重複前綴。
   仍為 Tier 2，只出草案不自裁。

## 上繳

`docs/upstream/02_rulings_execution.md`，更新 `docs/INDEX.md`，
附「本包是否仍有該驗而未驗者」之獨立判斷（不得省略），
每個數字標明量測條件。

## 未決（不在本包授權範圍）

- DR #1 037 素材 → Tier 3，Pei
- DR #3 A-UP02 之 8 條無覆蓋條文 → RD-1，Tier 3，Pei
- Layer 2 Test Set 邊界定案 → Tier 2
