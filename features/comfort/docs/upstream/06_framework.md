# 上繳包 06 — framework.md 落地 ＋ DECISIONS.md 簽署

執行層 → 分析層。2026-08-15。回應下放包 `12_partN_final.md` §5
（併 `11_partN_draft.md` §7）。

**結論：七項作業全部完成。四個 assertion 全 PASS。`DECISIONS.md` 已簽署，
R-C9 護欄實測生效。Phase 4 未開始。**

---

## 0. 置頂：6.3 之落位確認，以及一個值得記的成因

12 §3 要求讀 `6.3` 全文確認落位，並指出「non-foldable second row」語意偏後座。

**確認維持 `Front Climate Anatomy`，不需搬移。** 但前提有誤，且**誤在截斷處**：

| | 文字 |
|---|---|
| 60 字截斷（分析層所見） | `CM1.) When a vehicle is configured with a non-foldable secon` |
| **全文** | `CM1.) When a vehicle is configured with a non-foldable `**`secondary lower screen`**` that contains comfort information, the comfort section will be removed from the head unit except for comfort popups.` |

截斷恰好切在 `secon|dary` —— **`secondary` 被腰斬成看似 `second`**，於是
「secondary lower screen（次要下方螢幕）」讀成「second row（後座）」。
此條與後座無關。

這是 `layer3_map.tsv` 之 `section_title` 取前 60 字所致；該欄本為導覽用，
不是判讀用。**凡以截斷標題做落位或範圍判斷者，須讀全文**。

落位理由見 `framework.md` §4：6.3 規定在特定配置下 comfort section 是否
出現於 head unit，與同組之 2.1（有幾個分頁）、2.2（硬鍵變更如何反映）
同型 —— 三者皆為「有什麼、在哪裡」。不屬 `Rear Climate`（不涉後座）、
不屬 `Climate Popups`（`except for comfort popups` 是例外子句非主詞）、
不屬 `Seat Control Tab`（不涉座椅）。

---

## 1. §5.1 `framework.md` 已寫

`features/comfort/framework.md`，415 行。

| Layer | 值 | 進工作簿？ |
|---|---|---|
| 1 Test Group | `Comfort`（R-C6） | ✅ G 欄 |
| 2 Test Set | 15 組 | ✅ H 欄 |
| 3 spec section | outline 節次 | ❌ **不入**（§4.1.5） |

**Layer 3 不入工作簿，落實為兩條明文禁止**：不得存入任何欄位作為 Layer 3
欄值；不得串接進 Test Set 名稱（不寫 `Climate Modes 2.3`）。

同時寫明一件容易被誤認為違反該條的事：`specification_reference`（N 欄）依
§10.7 以 `{spec_filename}_{section_id}` 承載 section —— **那是 traceability
欄位，不是 Layer 3 欄位**。若不講清楚，Phase 4 可能因為「section 不入工作簿」
而把 N 欄也留白。

Test Set → section 之對照另存 `data/test_set_map.tsv`（129 列，
`test_group／test_set／outline／leaf_count／section_title`），供 Phase 4 查用，
同樣不是工作簿內容。

## 2. §5.2 四個 assertion —— 全 PASS

`scripts/verify_partn.py`。期望值（15 組之 section 清單、各組 leaf 數、
逐章分布）**全部寫死於腳本**，取自 12 §2 與上繳 01 §3。

```
- PASS — each Test Set's leaf_count matches handoff 12 §2:
    expected `all 15 equal`, measured `all 15 equal`
- PASS — Test Set leaf totals sum to 403: expected 403, measured 403
    — Front Climate Anatomy:12、Climate Modes:41、Temperature and Fan:17、
      Airflow and Defrost:23、Tri-Mode Climate:14、Rear Climate:46、
      ECO HVAC:15、Heated Vented Seats:59、Seat Control Tab:14、
      Climate Popups:42、ICS Anatomy:14、ICS Climate Modes:40、
      ICS Temperature and Fan:16、ICS Airflow and Defrost:29、
      Comfort Widget:21
- PASS — all 129 mapped sections assigned: expected 129, measured 129
    — unassigned: none; not in layer3_map: none
- PASS — no section assigned to two Test Sets: expected {}, measured {}
- PASS — per-chapter round-trip (ch2==92, ch16==99, +12 others):
    expected `all 14 chapters equal`, measured `all 14 chapters equal`
    — 2:92、3:14、6:1、7:38、9:8、10:15、11:37、12:22、13:14、14:40、
      15:2、16:99、17:18、18:3
- PASS — Test Set names: no Misc/General/Unclassified, no stray whitespace,
    no duplicates: expected [], measured [] — 15 names checked
```

Test Sets: 15；leaf 區間 **12–59**；最大者佔 **14.6%**。

### 2.1 兩件關於 assertion 設計本身的事

**一、範圍寫法之展開是被檢查的，不是被信任的。** 12 §2 有多組寫成範圍
（`7.2 ~ 7.10`、`13.2 ~ 13.6`、`14.1 ~ 14.19`）。腳本裡把它們展開成明列節次，
但**同時也把 12 §2 宣告的各組 leaf 數寫死**。只驗「節次加起來等於 403」
證明不了展開正確 —— 那只證明算術自洽；把展開結果對上獨立宣告的數字，
才會在展錯時失敗。第一個 assertion 就是為此。

**二、`Comfort Widget` 之命名判定改為明示回報，不做隱藏豁免。**
第四項 assertion 要求「名稱無 Test Group 前綴」。`Comfort Widget` 以
`Comfort` 起首，字面上牴觸。

我最初在條件式裡寫了 `and n != "Comfort Widget"` —— 那是把判斷藏進程式碼。
已改為獨立回報項：

```
- PASS — Test Set names starting with the Test Group word:
    ['Comfort Widget'] — reported, not failed: the spec names this element
    "the Comfort widget", so the word is the object under test, not a
    Layer 1 prefix (§4.2). Overrule at the analysis layer if disputed
```

判定依據是 spec 自身用語：17.1／18.1 之 `W0.) The Comfort widget will have
two screens`。該字指涉受測物件，非重複 Layer 1。**若分析層不同意此讀法，
改的是 `framework.md` §3.3 與該回報項，不需翻找程式碼裡的例外。**

## 3. §5.3 6.3 落位 —— 見 §0

確認維持，不搬移。**未自行搬移任何 section**（12 §3 明文）。

## 4. §5.4 `DECISIONS.md` 已簽署

| 項目 | 處置 |
|---|---|
| §6 Test Set table (Part N) | `[PEI — draft…]` → **`[SIGNED 2026-08-14]` 已定**，記 12 為依據，指向 `framework.md` 與四個 assertion |
| §6 profile `[OVERRIDE]` | **維持 `[PEI — 仍為 Tier 2，維持未定]`**，明記本次簽署不涵蓋 |
| §4 exemplar source | `[SIGNED]` 具名 **`home`**（144 列 done region），**`amfm` 具名排除** |
| §7 batch plan | `[SIGNED]` pilot = **第 13 章 `Seat Control Tab`**（14 leaves） |
| Sign-off | Reviewed by `PeiPYHsu`、Date `2026-08-14`、Overridden items 兩項、Ruling notes 六條 |

### 4.1 R-C9 護欄實測生效（本輪第一次對「真的已簽」之檔觸發）

先前之反向驗證用的是人工填入的 `TEST` 值。本次是真實簽署，故重測：

| 應然 | 實測 | 結果 |
|---|---|---|
| 拒絕覆寫 | `DECISIONS.md` sha256 前後皆 `4e9fa645c53f6463` | **PASS** |
| 寫出 `DECISIONS.new.md` | 已寫出 | **PASS** |
| 非零離開 | `exit=1` | **PASS** |
| R-C10 空簽署警告停止 | 該警告 0 次（先前每跑必發） | **PASS** |

訊息：`REFUSED (R-C9): …/DECISIONS.md is signed (Reviewed by: PeiPYHsu,
2026-08-14) and was NOT overwritten.`

`DECISIONS.new.md` 為本次驗證之產物，**已刪除** —— 它不是真實狀態，留著
會讓下一個讀 repo 的人以為有待合併的 survey。

### 4.2 兩件簽署時必須講明、否則日後會被誤讀的事

**一、8 個 `[PROPOSED]` 未動 ＝ 生效，不是遺漏。** 本檔表頭寫著
「`[PROPOSED]` untouched at sign-off = binding as proposed」。簽署後仍有
8 項保持 `[PROPOSED]`：§2 draft disposition、§3 safety attributes、
§4 style authority／test item shape／test group–set columns／
author on new rows／spec_reference、§5 split_mode。**已於 Ruling notes 逐項
列出**，否則日後讀者會把它們當成「還沒決定」。

**二、簽署日與寫入日不同。** 本檔寫入日為 **2026-08-15**，記載之簽署日為
Pei 指定之 **2026-08-14**（下放包 12 之簽署日）。兩者不同係轉錄時差，
非追溯簽署。已記於 Ruling notes。**Reviewed by 與 Date 之值由 Pei 指定，
非執行層自填**（12 §5.4）。

## 5. A-CF13 第三項已登（12 §1）

`HVS1／HVS2／HVS4／HVS5／HVS6` 跨 ch11／ch12 重複，為本 feature **第三處**
條款標籤衝突。三者形態一致：**條款標籤在 SR24 內不是唯一鍵。**

| # | 標籤 | 出現處 |
|---|---|---|
| 1 | `C16.)` | 2.15（後視鏡除霜）／16.17（blower reduction） |
| 2 | `W0.)` | 17.1／18.1／19.1 |
| 3 | `HVS1/2/4/5/6` | ch11／ch12 各五節 |

Part N 之合併處置（ch11＋ch12 → `Heated Vented Seats`，59 leaves）之副效果
為正向：近似重複落於同一 Test Set，Phase 4 之 sibling 判定與 `duplicate_of`
得以見效。

**Phase 4 之一般規則**：traceability 一律以 **outline 節次**為引用鍵。
`specification_reference` 依 §10.7 本就用 section_id，故**不影響工作簿輸出**，
只影響 `reasoning` 與 `test_item` 之敘述。

## 6. §5.6 Phase 4 未開始

未產 TC、未指派 tc_id、未做 sibling 判定、未寫 profile `[OVERRIDE]`。
本包只到 framework 落地與 `DECISIONS.md` 簽署。

---

## 7. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 7.1 已驗

1. 四個 assertion（各組 leaf 數對 12 §2、總和 403、129 節恰屬一組、
   逐章回算、命名合規）。
2. `6.3` 全文，及其與 `Rear Climate`／`Climate Popups`／`Seat Control Tab`
   三個替代落位之比對。
3. R-C9 對真實已簽檔之四項行為。
4. `framework.md` §6 明細表：129 列、leaves 加總 403（獨立於腳本再驗一次）。
5. `test_set_map.tsv` 129 列。

### 7.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **12 §1 之 ch11／ch12 查證** —— 「無證據顯示進入路徑不同」 | 該查證由分析層做，我未複測其結論。我只複測了標籤重複之事實 | **中** —— 合併之正當性繫於「同一進入路徑」。若 ch12 實際走不同入口，59 leaves 之組應拆。可複測（讀 ch11／ch12 首節全文），本包未做，因 12 §1 已裁定且未指示複測 |
| 2 | **15 組之組內語意一致性** | 我驗的是**覆蓋與計數**，不是**分組是否合理**。如 #2 `Climate Modes` 41 leaves 內含七類開關，是否確實共用同一狀態指示列，未讀全文查證 | **中** —— 11 §4.2 曾提可再拆為 `Climate On Off and Sync` + `Climate Modes`，Pei 未採。若 Phase 5 pilot 顯示該組過雜，屬 Part N 變更（回分析層） |
| 3 | **`14.19` 一節 8 leaves** | 未查其內容為何遠大於同章其他節（多數 1–3） | 低 —— 不影響切分，但 Phase 4 撰寫時可能需拆多個 TC |
| 4 | profile `[OVERRIDE]` 之內容 | Tier 2，未定 | **中** —— Phase 4 之前必須有；至少須明文 A-CF07 之寫回處置（03 §5） |
| 5 | DR #6（7" 螢幕配置） | 09 §5 已改為請 Pei 指認來源 | 低 —— 3 節，不入 Part N |

**第 1 與第 2 項是同一性質**：本包驗證的是 Part N **描述得對不對**
（覆蓋、計數、命名），不是 Part N **切得好不好**。後者要讀全文、要判斷
語意，屬 Tier 2。四個 assertion 全 PASS 只證明前者。

### 7.3 未做、亦未偷做者

- **未自行搬移任何 section**（6.3 確認落位，未動）。
- 未改 Part N 之任何分組、名稱或 leaf 歸屬。
- 未寫 profile `[OVERRIDE]`；未產 TC、未指派 tc_id。
- 未把 17 節 substantive 之任何一節納入 Test Set。
- 未重跑任何既有 feature 之 recon（R-C8）；對其目錄零寫入。
- 未執行任何 git 操作。

### 7.4 執行層對「本包可否結案」之判斷

**可結案。** framework 已落地並通過驗算；`DECISIONS.md` 已簽且 R-C9 護欄
實測生效。

**Phase 4 開始前有一項硬前置**：`DECISIONS.md` §6 之 profile `[OVERRIDE]`
仍未定，而 A-CF07（範本第 10–11 列樣本殘留）之寫回處置**必須於 profile
明文**（03 §5）—— BLANK 型 write-back 為「append from first data row」，
殘留列會位移首資料列。這件事留到 write-back 當下再決定就晚了。

§7.2 第 1、2 項若分析層認為需複測，請明示範圍；兩者都需讀全文與判斷語意，
我不確定是否可下放。
