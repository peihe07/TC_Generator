# 28 — Comfort HMI / 交付裁定：不交付 ＋ 批次 2 下放

- 產出層：分析層｜2026-08-15｜對象：執行層
- 裁定：Pei，2026-08-15（「就不交付啊」）

---

## 1. 交付裁定 —— pilot 工作簿不交付

`…_Comfort_20260815_pilot.xlsx`（SHA256 `b4ad82c2487a38c0…`，14 條）
**留在 `output/`，不置入交付夾。**

依據：本檔為 14 / 403 條（3.5%）。pilot 之目的為定型寫法，該目的已達成；
它不是可供評閱之交付件。交付之三項代價：評閱方無從判斷「只有 14 條」是
階段成果或遺漏；交付一次即建立每批交付之預期；A-CF02 須為此提前處理
（該項現已另案處置，見下放包 27）。

`DELIVERY.sha256` ENTRY 002 為其身分記錄 —— **該台帳為「已產出」之帳，
非「已交付」之帳**，兩者不得混用。ENTRY 002 之狀態欄除
`Excel-confirmed by Pei 2026-08-15（四項）` 外，**增記
`not delivered（Pei 2026-08-15）`**。

交付時點：語料完成，或 Pei 指定之里程碑。屆時另行下放交付包。

---

## 2. 批次 2 —— `Tri-Mode Climate`

批次順序**不依 Test Set 編號**，依結構複雜度遞增：先以單純批把規則磨穩，
再進大批（`Heated Vented Seats` 59、`Rear Climate` 46、`Climate Popups` 42）。

| 項 | 值 |
|---|---|
| Test Set | `Tri-Mode Climate` |
| Layer 3 | 3.1、3.2、3.3、3.4 |
| leaves | **14** |
| req_ids | `SWE1-HVAC-023` ~ `-026` |
| tc_id | `NR1L-ComfortHMI-015` 起，generator 指派 |
| 條文來源 | `data/section_fulltext.tsv`（**不得讀截斷標題**，R-C18） |

### 2.1 本批與 pilot 之差異，須留意三處

**（a）`3.2`（`C20.)` MAX DEFROST）一節 8 leaves** —— pilot 每節 1–3 條。
§8.2.2 之「RD sub-id ≠ TC count」可能於此首次觸發：若某 leaf 綑綁獨立之
部分失效，須拆多條 TC 並同溯該 leaf；反向合併多個 leaf 為一條則禁止。
判定用 §8.3 之壓力測試：「若只有部分行為失效，pass/fail 判定是否仍明確？」

**（b）配置軸密集** —— `3.1` 之 tri-mode 配置、`3.4` 之 soft top（JL/JT）。
**每一行 PC 依 R-C28 三問處理，第一問須具名條文相關句。**
若某節之配置軸不在 profile §3.2 之九軸內，**停下回報，不自行增軸**。

**（c）`3.3`（`C21.)` MAX DEF 與 REAR DEF 於 climate off 時可用）與 `2.10`
（climate off，屬 `Climate Modes`）分屬不同 Test Set** —— 依 §8.2.1
不得擴張至 sibling Req；`reasoning` 須具名委派之節次。

### 2.2 作業

1. 生成 14 條（或依 §2.1(a) 拆分後之條數，**條數變動須於上繳包說明理由
   並具名其 leaf**）
2. lint（35 gate，含下放包 26 §4 之三項）
3. §9 自評 17 項，**依 R-C23 每項具名獨立於 lint 之依據**
4. **不寫回 workbook** —— 寫回於 review 通過後另行下放
5. stop-and-report 條件同 18 §3.3，另加 §2.1(b) 之配置軸一項

上繳 `docs/upstream/18_batch2.md`。git 不執行。

---

## 3. 進度基準（供上繳包對照）

| | 數 |
|---|---|
| 驗證單位（037 Functional Requirement） | **403** |
| 已生成並定案 | 14（12 TC ＋ 2 BLOCKED row） |
| 本批後預計 | 28 |
| 未開始 | 375 |

**leaf 與 TC 目前 1:1 為巧合，非規則**（§8.2.2）。最終 TC 總數可能 > 403。

---

## 4. 本包產生之新條文清單（自檢）

無新條文。§1 為交付裁定，§2 為批次授權。
