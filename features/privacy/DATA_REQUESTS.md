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
