# 上繳包 10 —— 替換命中數、門檻檢查之落實與 profile 草案核對

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/10_profile_draft.md`
- 前一包：[upstream/09_threshold_derivation.md](09_threshold_derivation.md)
- 執行狀態：**步驟 1–5 全部執行完畢。**
  **停止條件 8 觸發** —— 回掃查出**同一 `.replace()` 缺陷之第二個實例**，
  已修正並回報（§4）。其餘八條未觸發。
  **零寫回工作簿**；**改狀態 git 零次**；**未寫入 `docs/runtime/profiles/`**；
  **未修改任何他 feature 之檔案**。

---

## 0. 先更正一項事實 —— 10 §七之「累積未提交」已過時

10 §七第 3 列稱「08＋08a＋09＋10 累積未提交」。**08／08a／09 已提交** ——
Pei 於 10 落檔前指示提交，執行層據以提交為 **`931053f`**
（`feat(power_moding): packages 08-09 — granularity criteria repaired, layer 2
finalized, thresholds derived`，13 檔 +2249/−67，帶 pathspec）。

**現行未提交者僅 10 包之異動。**（撰包時點早於提交所致，非任何一方有誤 ——
與 08 §5.1 之同型情形第二次發生。）

---

## 1. 抄錄核對表（步驟 1）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH41 | 就地替換須驗命中數；驗證標的須為所欲狀態非代理量 | 316 | `6f9b2f3973e6d5c3` | `6f9b2f3973e6d5c3` | 逐字相符 |
| R-PMH42 | R-PMH40 之落實須為可執行檢查 | 267 | `0f85f96074977fd6` | `0f85f96074977fd6` | 逐字相符 |

**本次抄錄即依 R-PMH41 施行**：四個 placeholder（兩條 × SHA／結果欄）
各驗其命中數恰為 1，共替換 4 次（預期 4）。

---

## 2. 步驟 2 —— `--check-doc-sync`（R-PMH42）

**實作**：`check_granularity.py` 新增 `self_sha256()`、`check_doc_sync()`
與 CLAI `--check-doc-sync`。檢查讀 `framework.md` 之
`程式 SHA256：\`…\`` 記載，比對程式現值。

**其本身亦依 R-PMH41 驗命中數** —— 記載數 ≠ 1 即失敗（而非取第一個）。

### 2.1 真實情境下之首次執行 —— **立即攔下**

新增該檢查即改動了程式，故文件之雜湊當場過時：

```
$ python scripts/check_granularity.py --check-doc-sync
doc-sync **FAIL** — **門檻表已與程式分岔** —— 文件記 `bd0f147e03919c24…`，
程式現值 `07aea6e38c2d236b…`。請重跑 `--emit-thresholds` 並重貼門檻節。
exit=1
```

**這不是合成測試，是它上線第一秒就抓到的真實分岔。**

重貼門檻節（依 R-PMH41 驗命中數：雜湊記載命中 1 處、門檻表重貼 1 處）後：

```
$ python scripts/check_granularity.py --check-doc-sync
doc-sync PASS — 文件與程式同源 —— SHA256 `07aea6e38c2d236b…`（命中 1 處）
exit=0
```

### 2.2 故意失敗與還原（R-PMH42 之 RESOLVED 條件）

已併入 `--self-test`：

```
=== R-PMH42 —— doc-sync 檢查之故意失敗與還原 ===

  [故意失敗] 注入假雜湊（模擬程式已改而文件未重貼）
    doc-sync **FAIL** 攔下 ✅ — **門檻表已與程式分岔** —— 文件記
    `07aea6e38c2d236b…`，程式現值 `0000000000000000…`。

  [還原] 用程式實際雜湊
    doc-sync PASS ✅ — 文件與程式同源 —— SHA256 `07aea6e38c2d236b…`（命中 1 處）

must-hit 五錨點全部如期 FAIL: True；範圍向 PASS: True；
doc-sync 故意失敗被攔下且還原後 PASS: True
exit=0
```

**停止條件 7 未觸發。** R-PMH42 之三項 RESOLVED 條件
（已實作／已接上（單一指令）／已以故意失敗證明會攔下）**全部滿足**。

> **仍存之限制**：檢查已存在且可執行，但**尚無任何流程強制它被跑**
> （與 `check_write_back.py` 之 `wired: false` 同型）。差別在
> `--self-test` 已把它納入，故凡跑自測即會跑到它。**接上正式閘門仍待 Phase 6。**

---

## 3. 步驟 3／5 —— 歷次就地替換之回掃（R-PMH41）

**範圍**：`framework.md`／`feature.yaml`／`DECISIONS.md`／`PLAYBOOK.md`／
`RULINGS.md`／`ANOMALIES.md` 六檔全文，七組標記
（`PENDING Q`／`<PENDING`／`TBD`／`PEI-REOPEN`／`待裁`／`待命名`／`未定版`）。

### 3.1 回掃結果 —— 命中 4 處，其中 **1 處為殘留**

| # | 位置 | 標記 | 內容 | 判定 |
|---|---|---|---|---|
| 1 | **`framework.md:7`** | **`未定版`** | `- **狀態：未定版。** Test Set #2 之名為 \`Disclaimer Screen\`，待 Pei 裁定（06 §5.4）` | **❌ 應已被替換而殘留** |
| 2 | `feature.yaml:12` | `TBD` | `# 未實測者一律留 TBD／null，不猜。` | ✅ **現行有效之通則敘述**（非某一欄之待決值） |
| 3 | `RULINGS.md:204` | `PEI-REOPEN` | `> **已於 2026-08-24 重裁定案，見 R-PMH27（05b 包）。\`[PEI-REOPEN]\` 標記撤除。**` | ✅ **現行有效** —— 敘述「標記已撤除」之本身 |
| 4 | `RULINGS.md:696` | `PEI-REOPEN` | `R-PMH10 之 \`[PEI-REOPEN]\` 標記**撤除**。` | ✅ **現行有效** —— R-PMH27 條文原文（不改字） |

**停止條件 8 觸發**（第 1 項）。已修正並複驗（見 §4）。

修正後回掃複驗：**命中 3 處，全部為「現行有效」**，殘留 0。

---

## 4. **停止條件 8 之內容 —— 同一缺陷之第二個實例，且 08a 上繳曾正面誤稱其已改**

### 4.1 事實

`framework.md:7` 原為（08a 之後、本包之前）：

```
- **狀態：未定版。** Test Set #2 之名為 `Disclaimer Screen`，待 Pei 裁定（06 §5.4）
```

**成因與 09 §6.1 所述完全相同**：08a 步驟 8 中，我先把全檔之
`<PENDING Q11>` 換成 `Disclaimer Screen`，**再**去替換這一行
（其原文為 `…之名為 \`<PENDING Q11>\`，待 Pei 裁定…`）——
第二個 `.replace()` 因目標字串已被第一步改掉而**靜默未命中**。

### 4.2 這一項比 09 §6.1 那一項更嚴重

09 §6.1 之情形為「驗了、通過了、但驗的不是要驗的那件事」
（驗佔位符殘留數而未驗節標題）。

**本項則是：08a 上繳 §11.3(a) 逐字寫「狀態由「未定版」改為 **定版**」——
一句對「已發生之變更」之正面陳述，而該變更從未發生。**

即：**不只是驗錯了東西，是報告了一件沒做到的事。**

### 4.3 一個文件內兩處自相矛盾，且維持了兩輪

09 包我把 `## Layer 2 —— Test Set（8 組，**定版**）` 這個標題改對了
（第 24 行），**卻沒發現第 7 行還寫著「未定版」** ——
於是 `framework.md` 在 08a 與 09 兩輪間，**同一檔內第 7 行說未定版、
第 24 行說定版**。

09 §7 第 2 項我自陳「此形態只修了這一處，未回頭掃描前八包之全部就地替換」
—— **那句自陳是對的，而它所預告的東西就在同一個檔案的第 7 行。**

### 4.4 修正與驗證（依 R-PMH41）

```
目標字串命中數 = 1（預期 1）
已修正；驗證：舊字串殘留 0、新字串命中 1

=== framework.md 內「定版／未定版」之全部出現 ===
     7  - **狀態：定版**（2026-08-24，**R-PMH36** —— Pei 裁「甲」）。Layer 2 為 **8 組**，
    24  ## Layer 2 —— Test Set（8 組，**定版**）
```

**兩處一致。** 修正後 `--check-doc-sync` 仍 PASS（門檻節未動）。

---

## 5. 步驟 4 —— profile 草案之核對（**未寫入 `docs/runtime/profiles/`**）

### 5.1 (a) 條號存在性與內容相符

| 類別 | 引用數 | 未定義者 |
|---|---:|---|
| `R-PMH{n}` | **17**（`R-PMH1, 2, 7, 8, 9, 12, 13, 14, 16, 18, 20, 23, 24, 25, 26, 27, 36`） | **無** |
| `A-PMH{n}` | **5**（`A-PMH03, 04, 10, 12, 13`） | **無** |
| 他 feature 之條號（僅作前例引用） | 3（`R-P8`、`R-P54`、`A-PW68`） | 不須本 feature 定義 |

**17 條 R-PMH 皆存在於 `RULINGS.md` 之 fenced block；5 條 A-PMH 皆存在於
`ANOMALIES.md` 之節標題。零不符。**

**內容相符之抽樣核對**（草案所述 vs 條文實載）：

| 草案之陳述 | 條文 | 相符 |
|---|---|---|
| 母本 SHA256 `6372fb6b…6fb825b2` | R-PMH7 逐字 | ✅ |
| 客戶那份封面**五頁**不得取用 | R-PMH23 逐字（含 `Cover_old`／`ChangeHistory_old`） | ✅ |
| `D5` **9 空 / 7 非空**、母體 16 | R-PMH27 逐字 | ✅ |
| Layer 2 八組及其 leaf 數 | R-PMH36 逐字 | ✅ |
| `tc_id_format` 與 Comfort 反例 | R-PMH16 逐字 | ✅ |
| x14 source 取 `<xm:f>` 實測而非分頁名 | R-PMH25 逐字 | ✅ |

**他 feature 之前例聲明亦已唯讀複驗**（草案 §7）：

| 草案 §7 之聲明 | 實測（`features/power/feature.yaml`） | 相符 |
|---|---|---|
| Power 為 35 欄版面，priority **Q** | `Q` | ✅ |
| design_method **S** | `S` | ✅ |
| author **AB** | `AB` | ✅ |
| remarks **AI** | `AI` | ✅ |
| Power 之 `spec_mode = D` | `D` | ✅ |

### 5.2 (b) §0.1 欄位對應逐欄比對

| 語義 | 草案 | `feature.yaml` | 相符 |
|---|---|---|---|
| req_id | D | D | ✅ |
| tc_id | F | F | ✅ |
| test_group | G | G | ✅ |
| test_set | H | H | ✅ |
| priority | **P** | **P** | ✅ |
| design_method | **R** | **R** | ✅ |
| functional_safety | **S** | **S** | ✅ |
| author | **AA** | **AA** | ✅ |
| remarks | **AH** | **AH** | ✅ |

**九鍵逐欄相符。** 另三項為區間或註解：`test_item…tc_ref_id = I–O`
（實測 `test_item=I`、`tc_ref_id=O` ✅）、`estimated_time = Q`
（不在 16 鍵內，`feature.yaml` 之註解記 `Q` 為 `estimated_test_time` ✅）、
車型欄 `T–Z`（`feature.yaml` 註解同 ✅）。

### 5.3 其他可機器核對之草案數值 —— **12 項全符**

`first_data_row=10`／`columns` 16 鍵／`last_capacity_row=1411`／
`workbook_state=BLANK`／`spec_mode=A+B`／`test_group=Disclaimer screen`／
`tc_id_format=NR1L-DisclaimerScreen-{NNN}`／`write_back.first_row=10`／
`test_set_values` 8 組／分頁名／`design_method_vocabulary` 9 項／
母本 SHA256 前 16。

**草案 §3.3 之九詞條與 `feature.yaml` 之 `design_method_vocabulary`
逐字相同**（含第 6 項之 `Pairwise / t-wise`）。

### 5.4 草案 §2 之 Test Set leaf 數 vs `data/layer3_sections.tsv`

八組逐組相符（3／7／9／6／7／8／5／3），**合計 48、餘數 0**，
各組之 Layer 3 章節亦與 TSV 反推一致。

### 5.5 **停止條件 9 未觸發** —— 草案與 `RULINGS.md`／`feature.yaml` 零不符

**草案未寫入 `docs/runtime/profiles/`**（10 §五之禁止項）。
`FW036_R1L_PowerModing_Profile.md` 仍不存在，待 Pei 核可。

---

## 6. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，五項。**

1. **回掃只掃了七組標記與六個檔案。** R-PMH41 之問題是「替換靜默未命中」，
   而**未命中之結果不必然含這七個標記** —— 例如某處原文被換成了半對半錯
   之混合句，或某個表格列之數字沒跟著改。**回掃之判準是「找得到的標記」，
   不是「所有未命中之替換」。** 真正的作法是回頭看每一次替換之
   before/after，本包未做（成本高，且部分已無 before 可查）。

2. **`docs/handoff/`／`docs/upstream/` 之歷次上繳未回掃。**
   §3 只掃了六個狀態檔。**08a 上繳 §11.3(a) 那句誤稱至今仍在檔案裡**
   —— 本包於 §4.2 具名了它，但**未去改那份已提交之上繳包**
   （改已交付之上繳包是否適當，未有規則，本包不自行決定）。

3. **`--check-doc-sync` 只驗一個雜湊，不驗門檻表之內容。**
   若有人手改 `framework.md` 之門檻**數值**而不動雜湊行，檢查會 PASS。
   徹底之作法是比對整張表之文字，本包未做。

4. **profile 草案之核對只及於可機器比對之項。**
   §3.2 之「變體詞為 `Maserati`／`GDPR`／`R1Low` 不得改寫」、
   §4 之四條 split 判準、§3.9 之「七個非空者中有兩者填錯」等
   **敘述性內容未逐句回溯至規格或條文** —— 其正確性目前倚賴分析層。

5. **草案 §0 稱「48 leaf」而 §2 之表亦合計 48，二者一致；
   但草案未載 `A-PMH13` 之 `-028` 是否計入該 48。**
   依 R-PMH1 它在 48 內（`Categorization == Functional Requirement` 全集），
   而 §6 又稱其為「全案缺口」。**若 Pei 裁定 (ii)（out of scope），
   §0 與 §2 之 48 須加註「其中 1 條為揭露列」** —— 草案現無此註，
   而該裁定未下，故本包不改。**列為 Pei 裁定後之連帶待辦。**

---

## 7. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發 |
| 5 | 造值壓力 | 未觸發 —— profile 未寫入 |
| 6 | done region 與規格矛盾 | 未觸發 |
| 7 | doc-sync 故意失敗未攔下或還原後未 PASS | **未觸發** —— 攔下 ✅、還原 PASS ✅ |
| 8 | 回掃發現「應已替換而殘留」 | **觸發 1 項** —— `framework.md:7`，已修正並複驗（§4） |
| 9 | 草案與 `RULINGS.md`／`feature.yaml` 不符 | **未觸發** —— 17 條 R-PMH ＋ 5 條 A-PMH 皆存在；欄位九鍵、數值 12 項、Test Set 八組全符 |

---

## 8. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(power_moding): package 10 — doc-sync check wired, replace-residue swept
```

```
git add -- features/power_moding/RULINGS.md \
           features/power_moding/framework.md \
           features/power_moding/scripts/check_granularity.py \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/10_profile_draft.md \
           features/power_moding/docs/upstream/10_profile_draft.md
```

- **未寫入 `docs/runtime/profiles/`**（禁止項）。
- **未修改任何他 feature 之檔案。**
  ⚠ `git status` 顯示 `features/power/docs/internal_var_observability.md`
  為未追蹤 —— **非本 session 產物**（建立於 13:21，內容為 power feature 之
  SYS3 SYSAD 摘錄，屬併行 session）。**不入本次 pathspec。**
- `feature.yaml`／`DECISIONS.md`／`PLAYBOOK.md`／`ANOMALIES.md` **本輪未改**。
- `scripts/new_feature.py` 未改（禁止項仍在）。
- pathspec 逐項寫全名（R-PMH3(c)）。

### 8.1 git 動作揭露（R-G6）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | `git status --short`（含 `features/power/` 之禁止項確認） | 3 |
| **改狀態 git** | **無** | **0** |

---

## 9. 待 Pei 裁定

| # | 事項 | 阻斷 |
|---|---|---|
| **profile 草案** | §四全文 —— **核對零不符**（§5），核可後由執行層寫入 `docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md` | **Phase 4 前置** |
| **A-PMH13** | `-028` 之處置。**連帶**：若裁 (ii)，profile §0／§2 之「48 leaf」須加註「其中 1 條為揭露列」（§6 第 5 項） | **Phase 4 前置** |
| **commit 授權** | **10 包之異動**（08/08a/09 已提交為 `931053f`）。逐包窄口 or 常規授權 | 否 |
| **§6 第 2 項** | 已提交之上繳包（08a §11.3(a)）含一句誤稱 —— **是否更正已交付之上繳包，無規則可循** | 否 |
| **§6 第 3 項** | `--check-doc-sync` 只驗雜湊不驗表內容 —— 是否加強 | 否 |
| Q10 | `Product Document 記錄封面頁`（profile §3.10 已預留） | 否，Phase 7 前 |
