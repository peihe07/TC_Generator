# DATA REQUESTS — Privacy (FW036)

Files Pei can supply that unblock or upgrade generation. Drop into
`features/privacy/inputs/`; each landing closes or advances the linked
anomaly. Ordered by when a batch actually needs it. Names are verbatim from
the citing source where the source gives one; otherwise the expected naming
pattern is stated and marked (pattern).

**Standing rule（沿用 AMFM）**：任何新發現之外部引用，登記 anomaly 的同時
必須新增一列於此表；且每次 session opener 與 batch gate 都要按 Urgency 回報。

| # | 檔案 — 全名 | Status | Leaves served | Batch impact | Anomaly | Urgency |
|---|---|---|---|---|---|---|
| 1 | Privacy 之 FM-WI-FSM-036-A01 TC workbook | ⚠️ **以空白通用範本代替**（2026-08-13 Pei 指示）—— `inputs/FM-WI-FSM-036-A01 …_SWQT_20260121.xlsx`，rev C，SHA256 `cd876c202c71e74b…`。`workbook_state` = BLANK，P4 阻塞已解除。殘留：非 Privacy 專屬，封面/Scope/Purpose/Reviewer 待填 | 全 10 leaves | P4 起全部批次 | A-PV01 / A-PV08 | ~~High~~ → Low（僅待確認交付形態）|
| 2 | `Audio_Output_Management_-_LTM_ETM_Amplified_Audio_System_VF651_V6_R2.docx` | ✅ **已入 `inputs/`**（2026-08-13，R-PV01(c) 簽署後）—— 184,808 bytes，SHA256 `49dd3c31…` | -007 / -008 / -010（AMP is present）；-006 / -009 反向對照 | AMP-present 情境批 | A-PV02 RESOLVED | — |
| 3 | `…with_Internal_ANC_VF651_V9_R3.docx` / `…with_ANC_VF651_V11_R3.docx` | ❌ **Not requested** —— R-PV01(c) 明示「ANC 兩份維持不索取」 | 僅在 ANC 配置納入範圍時 | — | A-PV02 | — |
| 4 | CFTS019 Audio Management（SYSAD 對 PROF-172 之另一引用） | 未入 `inputs/`；AMFM `inputs/` 已有同名檔可比對 release | -006 / -009（SCV local adjustment）| context | A-PV02 | Low |
| 5 | Scope / Purpose / Reviewer / Project Name / Date 五格之填入值 | ⏳ 待 Pei 給值 —— 非檔案，屬 Tier 2 賦值。執行層提案 Scope = `SWE1_CFTS_022-Privacy_Features`，其餘不自填 | 交付件表頭 | P7 寫回前必須有值 | A-PV08 | **Medium —— P7 之前** |

## 已量測、無需索取

- **A-PV04（VF651_V2_R2 同名不同內容）**：全庫 7 個路徑已算 SHA256，
  `inputs/` 這份（`d5813bb7…`）與 `HDCC28_Split` 同源，判為 HDCC28 平台基線。
  無需另索檔案，僅待 Tier 2 追認。

## P2 進場前必辦（非索取，屬重驗義務）

R-PV01(a)(b)(d) 延後至 P2，其證據鏈依賴 handoff §3 之單方掃描數字，
簽署前必須由執行層重驗（見 `docs/upstream/00_bootstrap.md` §7.6）：

1. CFTS022 之 ECU/Radio 適用性掃描（336 / 334 / 196 / 23 / 0 五個數）
2. VF651 變體全集 —— **須逐檔 hash，不可逐名比對**（A-PV04 已證同名不同容）
3. SYS.2 覆蓋（8 子目錄、無 V3）
4. V2_R2 / V3_R3 全文 diff（390 vs 393 行、hunk 75 行、四處實質差異）

## Not requested

- ANC 兩變體（V9_R3 / V11_R3）—— R-PV01(c) 明示不索取
- SYS.2 / SYSRA 安全分析件（`CFTS022_Privacy_mode-FM-WI-FSM-035-A02 …`）已在
  `inputs/`，但 recon 實測 ruled 037 來源 **無 ASIL/FTTI 欄位** →
  安全分析層在本 feature 之 10 leaves 上無附著點，不進 trace chain
  （比照 AMFM R6）。保留為 context。

## RD-1 提問（隨交付送出，非索取檔案）

以下三項為向上游回報之範本層缺陷，**不阻塞任何批次**，登記於此以免遺漏。

| # | 議題 | 證據 | 來源 |
|---|---|---|---|
| 6 | **車型欄停在 27 世代** —— rev C 之 T–Z 為 `HDCC27` / `DT27` / 五個 Atl-Mi 車型，**無 HDCC28**，而本專案平台為 HDCC28。rev C 是否應補 28 世代欄位，或本專案本就不填？ | T8:Z8 合併標題 `Vehicle Model 車型`；T9–Z9 逐格實測 | A-PV15 / R30-4 |
| 7 | **`Regengade (5210)` 疑為 `Renegade` 拼寫錯誤** —— 範本 X9 原文，未更動 | X9 儲存格文字 | A-PV15 / R30-4 |
| 13 | **HU 對 amplifier presence 之判定有無規格指定之可觀察指標** —— CFTS022-4915174/4915175 之觸發含「the HU has determined that the amplifier is present / not present」，該判定為 HU 內部狀態，測試者無法直接設定。目前以客觀組態為觸發、判定環節納入受測範圍（R35-3）。若有可觀察指標（訊號、診斷值、HMI 呈現），該指標應成為獨立之中間驗證點 | CFTS022-4915174 / 4915175 觸發措辭 | R35-3 |
| 12 | **-008 之葉子分配確認** —— CFTS022-4915173 之 trigger 與 outcome 主詞皆為 AMP、條文不提 HU、ECU tag 為十葉中唯一含 `AMP` 者，卻被分配至 HMI/HU 之 SWE.1。請確認該葉之分配；若確為 HU 側需求，請指出 HU 在該行為中之角色與可觀察面 | CFTS022-4915173 全文；十葉 ECU tag 對照 | A-PV18 / R34-3 |
| 11 | **PROXI requirements（車型專案專屬）** —— VF651_V6_R2 之 PROXI Parameters 節列有 `Acustic_Configuration` / `Audio_System_Type` 兩參數名，但明文「their related values are defined in the "PROXI requirements" specific for the vehicle project」，該文件不在 `inputs/`。B2 四葉（-006/-007/-009/-010）之 AMP present/not present 前置條件目前以條文措辭表述、未填參數值（§8.4.1）。若要在 TC 內給出可直接照做的組態設定值，需要此檔 | VF651_V6_R2 段落 294–322 | R33 / §8.4.1 |
| 9 | **037 -001 之 Description 含 CFTS022 未載之行為主張** —— 「轉換階段中按鍵輸入不得被處理」；CFTS022 全文涉 SLEEP MODE 者僅 4914954 / 4914955 / 4915104 三條，無一述及。請確認該句為需求或闡釋；若為需求，請指出其 CFTS022 出處或補充條文 | 037 Description 第二段；CFTS022 全文掃描 | A-PV17 / R33-2 |
| 10 | **$VolumeSCV$ 無效值處置之驗證歸屬** —— CFTS022-4915170 之 outcome 主詞為 AMP（"considered invalid by the AMP and no action shall be taken"），而本交付件 ECU 為 LTM（HU 為發送端，無從注入無效值）。真正之負向驗證歸 AMP ECU；請確認該行為已分配至 AMP 側之 037，或說明其驗證歸屬 | CFTS022-4915170 條文；-005 之 ECU 讀法裁定 | R33-1(c) |
| 8 | **下拉選單 DV 範圍不一致 + `Reference` 分頁字串不符** —— R10 指向 `$A$1:$A$9`、R11:R59 指向 `$A$1:$A$11`（含 2 空選項）；`Reference!C9` 作 `Pair-wise / N-wise` 而 `下拉選單!A6` 作 `Pairwise / t-wise` | sheet6 x14 DV 定義；兩分頁字串 | A-PV10 / A-PV11 / R23-6 / R23-7 |
