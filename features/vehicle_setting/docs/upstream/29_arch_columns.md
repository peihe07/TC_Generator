# 上繳 29 —— R-VS51 之架構欄組分流、batch13、batch14

執行層寫入。依據：`docs/handoff/52_review_round31.md` §4
＋ `docs/handoff/53_pilot2_verdict.md` §3。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | 逐字轉錄 R-VS51；R-VS20 加註縮限 | ✅ |
| D-3 | DR-15 補觀察段（不改待覆狀態）；A-VS97 併入 DR-18 | ✅ |
| D-4 | A-VS98 關閉；A-VS97 標 typo | ✅ |
| D-5 | 依 R-VS35 列兩數 | ✅ |
| D-6 | 本檔首表 ⬜／✅ 對照各節實際內容 | ✅ |
| D-7 | profile 增列 A-VS62 之 [ADD] 段；A-VS62 標關閉 | ✅ |
| D-8 | `pilot2_sheet.md` 檔頭加註 pilot #2 通過 | ✅ |
| **W-90** | 依 R-VS51 重跑分級 | ✅ **103/2/132 → 141/2/94** |
| **W-91** | batch13 —— 10 條 | ⬜ **未執行** |
| **W-92** | batch14 —— 10 條 | ⬜ **未執行** |

---

## 1. 預期 vs 實測（相符者亦列出）

| # | 預期 | 實測 | 判 |
|---|---|---|---|
| 1 | W-90(3)：DR-15 之五 token 須被 `guard()` 攔下 | **4 次攔下，全數歸 DR-15**（`FL_HS_RQ`／`FR_HS_RQ`）；驗收錨點成立 | 相符 |
| 2 | W-90(5)：轉出數（升級門檻 < 20） | **33**（受控比較：同一驅動、僅切換 R-VS51） | 相符，升級**未命中** |
| 3 | W-90(5)：被 `guard()` 攔下之條數 | **4** —— **與轉出數不可互代** | 相符 |
| 4 | W-90(4)：與 103／2／132 之對照 | **無法以同一驅動作出** → §2.1 | **不符** |
| 5 | 52 包 §1：`Atlantis` 欄組可解 `*_Cmd_Tlm` 之 60 leaf | `FL_HS_Cmd_Tlm`／`FR_HS_Cmd_Tlm`／`FL_VS_Cmd_Tlm` 解得（各 12 次）；**`FR_VS_Cmd_Tlm` 未解** → §2.3 | 部分相符 |
| 6 | R-VS51 為本輪最大解鎖 | **是，但非唯一** —— 另有 5 個 token 之補收（A-VS102）貢獻 5 leaf | 相符 |

## 2. 不符項目（不自行調和）

### 2.1 W-90(4) 之對照無法作出 —— `writability.tsv` 不可重現

`scripts/` 中**無任何腳本產出 `writability.tsv`**（`grep -l` 命中 0）。
該表為 20／27／29／31 四輪以 inline heredoc 逐次修改而成，
歷輪之 R-VS43／R-VS48／R-VS49／W-87 調整**只寫進產物，未寫進驅動**。

以現有模組重建之驅動得 **62/2/173**（三形態抽取）／**82/3/152**（補收 token 後），
與 103/2/132 **逐 leaf 不一致 52 筆**。→ **A-VS101**。

**本輪之處置**（具名，不掩飾）：

1. **受控比較**給出增量 —— 同一驅動、同一輸入，僅切換 R-VS51 之 `Atlantis` 欄組：

   | | W0 | W1 | W2 |
   |---|---:|---:|---:|
   | 不套用 R-VS51 | 82 | 3 | 152 |
   | **套用 R-VS51** | **115** | **3** | **119** |
   | 差 | **+33** | 0 | **−33** |

2. **增量法**套回產物 —— **僅升級、不降級**（沿用 20 輪以降之作法）：
   `writability.tsv` **103/2/132 → 141/2/94**；`generatable` **81 → 118**。
   其中 **33 leaf 因 R-VS51**、**5 leaf 因 A-VS102 之補收 token**。

**本層之獨立判斷**：141/2/94 之**絕對值仍不可稽核**（其底為不可重現之 103/2/132）；
**可稽核者為增量 33 與 5**。引用時須連同此限制。

### 2.2 `FR_VS_Cmd_Tlm` 未解 —— R-VS38 之 typo 裁定不涵蓋跨列引入

條文寫 `Vented_seat_high／low／off／mid`（14 次），
LID 列 790 之 Format 只有 `Heated_seat_*`（52 包 §3 已判 typo）。
**但 LID 中無任何 `FR_VS_Cmd_Tlm` 之 `Vented_seat_*` 列** ——
其正確值域須自 `FL_VS_Cmd_Tlm` 之列 769 **跨列引入**，
而「判某值為轉錄錯誤」與「以對稱側之列補其值域」是兩件事。
**本層不跨列引入** → **A-VS103**，已併入 DR-18 之確認範圍。

### 2.3 `_mid` 與 `_medium`

條文寫 `Heated_seat_mid`／`Vented_seat_mid`（6 次），LID／DBC 為 `_medium`。
R-VS48(a) 之**字元子序列**判準判不成立（`d` 在 `medium` 中位於 `i` 之前）。
**判準無誤，是縮寫形態超出其涵蓋** —— `mid` 為截斷式縮寫，非抽字母式。
**本層未擴充判準**（擴充須先過 R-VS44：階數值正是 DR-15 標的）→ **A-VS104**。

### 2.4 W-91／W-92 未執行

本輪作業量已逾單輪份額（文書 8 項 ＋ W-90 之驅動重建與四次重測）。
**batch13／batch14 未生成。** 池已備妥（`generatable = yes` **118**，
扣除已交付 76 條，**餘 42 條**），下輪可逕行。**不虛報為已執行**（A-VS101 之教訓即此）。

## 3. 結果三分法（canon §8.4）

**(a) 確證**

- R-VS51 之受控增量：**W2 → W0 共 33 leaf**（Two/ThreeStages Heated／Vented 四群）
- `guard()` 攔下 **4** 次，全歸 **DR-15**（`FL_HS_RQ`／`FR_HS_RQ`）—— R-VS51(3) 生效
- `*_Cmd_Tlm` 三者（FL_HS／FR_HS／FL_VS）各解 12 次；`FR_VS_Cmd_Tlm` **0**
- **5 個 token 於 DBC 有完整 `VAL_` 而未收錄**（4 個 `*_STATFailSts` ＋ `EngineSts`），
  全庫另有 38 個同型者**屬他 feature**，已排除
- 產物：`writability.tsv` 141/2/94；`generatable` 118；`spec_variables.tsv` 31 → **36 列**，
  增 `arch_column`／`suspect_prefix` 兩欄

**(b) 未定**

- `writability.tsv` 之**絕對數**（A-VS101）—— 須補寫驅動並回放各輪裁定方能稽核
- `FR_VS_Cmd_Tlm` 之值域（A-VS103，待 DR-18）
- `_mid` → `_medium`（A-VS104，待判準擴充之裁定）

**(c) 排除**

- 「R-VS51 之轉出 < 20」—— **排除**，實測 33
- 「`Atlantis` 欄組可解全部 60 個 `*_Cmd_Tlm` leaf」—— **排除**，`FR_VS_Cmd_Tlm` 未解
- 「38 個 DBC 已有值域之 token 皆屬本 feature」—— **排除**，限縮至 251 條文後僅 5 個

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

**LID 欄組抽取** — `openpyxl` 全列掃 `CAN Mapping`；
`Atlantis` 取欄 16（Signal Name）／欄 18（Format），
`Atlantis High` 取欄 26／欄 28。
鍵以 **Signal Name 之末段裸名 ＋ 欄 1 之 LID id** 雙鍵收錄
（`Atlantis` 996 token／`Atlantis High` 2,025 token）。

**條文架構分流（R-VS51(2) 之實作）** —
`col = 'Atlantis' if ('Atlantis Mid' in arch and 'Atlantis High' not in arch) else 'Atlantis High'`
—— 即「同時標二者取 High」逐字落實。

**值之三形態**（A-VS84 定案之①②③）：

```
(token)\s*(?:=|==|!=|<>|passes to|is set to)\s*\[([^\]]{0,90})\]
(token)\s*(?:…)\s*"([^"]{0,90})"
(token)\s*(?:…)\s*[“]([^”]{0,90})[”]
```

**R-VS44 閘** — 以 `guard(tok, v, "resolved")` 呼叫。
**本輪修正一處自身錯誤**：初版以 `guard(tok, v, "blocked")` 呼叫，
而 `guard()` 於 `verdict == "blocked"` 時**逐字直接放行**（其語意為「原已阻塞，無須過閘」），
致 58 次全被誤記為「被攔」。改以 `"resolved"` 後得真值 **4**。
**該錯誤由本層自行發現並更正**，未進入任何交付數字。

**盲區（具名）**

- 上述三形態外之第四式（單引號、全形引號、表格並置）未測 —— A-VS88 仍開
- LID 雙鍵收錄（裸名 ＋ LID id）**可能產生跨列串鍵**
  （已見 `VentedSeatFL` 之 `Atlantis High` 欄組指向 `STATFailSts`）；
  本輪之增量因僅取「HIGH 未解而 MID 解得」者而未受其害，**但該風險未量**
- 本輪驅動與產出 `writability.tsv` 之歷輪 inline 程式**不等價**（A-VS101）

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| 編號 | 主題 | 配對 DR |
|---|---|---|
| **A-VS101** | `writability.tsv` 不可自 repo 重現 | 無（方法層，內部） |
| **A-VS102** | 5 個 token 於 DBC 有值域而未收錄 | 無（DBC 為權威，補收非推論） |
| **A-VS103** | `FR_VS_Cmd_Tlm` 須跨列引入值域 | **併入 DR-18** |
| **A-VS104** | `_mid` 超出 R-VS48(a) 之子序列涵蓋 | 無（判準擴充待裁） |

**關閉**：**A-VS98**（依 R-VS51）、**A-VS97**（依 R-VS38，52 包 §3）、
**A-VS62**（Pei 2026-08-22，53 包 §2）。

**D-5（R-VS35 兩數）**

| 側 | 本輪開立 | 登記簿現有 |
|---|---:|---:|
| 執行層 | **4**（A-VS101～A-VS104） | **103**（A-VS01～A-VS104，`A-VS02` 永久缺號） |
| 分析層（52 包 ＋ 53 包） | **0** anomaly、**1** 條文（R-VS51） | 差額 0；R-VS51 已入 `RULINGS.md:1082` |

**DR 現況**：新開 0、改寫 1（DR-15 補觀察段，**待覆狀態不變**）、
併入 1（A-VS97 ＋ A-VS103 → DR-18）。

## 6. 獨立判斷：本包是否仍有該驗而未驗者

**有，四項。**

1. **A-VS101 是本輪最重要的發現，且其影響及於已交付之全部數字。**
   `writability.tsv` 自 20 輪起即為不可重現之產物，
   而 24～51 包之全部優先序判斷（含 A-VS95／A-VS100 兩次「數字與實測不符」）
   **皆以之為據**。R-VS50 令「引為決策依據時須回查其組成」——
   **但組成之回查若基於不可重現之表，回查本身亦不可稽核**。
   建議之驗法：補寫 `scripts/writability_driver.py`，逐輪回放
   R-VS43／R-VS47／R-VS48′／R-VS49／R-VS51 與 W-87，
   驗其能否重現 141/2/94。**本輪未做**（逾單輪份額）。

2. **本輪之 `guard()` 呼叫錯誤（§4）未在任何自動檢查中被攔。**
   `guard(tok, v, "blocked")` 是**靜默直通**，其誤用不會報錯。
   R-VS44 令「併入判定腳本之輸出階段」已達成，
   **但未令其呼叫方式可驗** —— 建議 `guard()` 對 `verdict == "blocked"` 之呼叫
   加一個顯式的 `assert` 或改名（如 `guard_new_conclusion()`）。

3. **LID 雙鍵收錄之跨列串鍵風險未量**（§4 盲區第二項）。

4. **W-91／W-92 未執行**（§2.4），非因阻塞，因份額。
