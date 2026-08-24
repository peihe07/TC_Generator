# 上繳包 11 —— 已發生變更之舉證、勘誤方式與互斥狀態一致性

- 日期：2026-08-24
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`docs/handoff/11_claim_evidence.md`
- 前一包：[upstream/10_profile_draft.md](10_profile_draft.md)
- 執行狀態：**步驟 1–5 全部執行完畢。九條停止條件全未觸發。**
  **零寫回工作簿**；**未寫入 `docs/runtime/profiles/`**；
  **未觸碰 `features/power/docs/internal_var_observability.md`**。

---

## 0. 一項事實更正 —— 11 §五之「10 包之提交尚未授權」已過時

11 §五逐字：「**改狀態 git 零次**（10 包之提交尚未授權）」。
**10 包已提交** —— Pei 於 11 落檔後指示提交，執行層據以提交為 **`c4f276f`**
（`feat(power_moding): package 10 — doc-sync check wired, replace-residue swept`，
6 檔 +932/−4，帶 pathspec）。

**此為第三次同型情形**（08 §5.1、10 §七、11 §五）——
撰包時點早於提交所致。**建議下放包不再載提交狀態**，
其為 git 之現況而非分析層可知之事；改由執行層於上繳回報即可。

---

## 1. 抄錄核對表（步驟 1，依 R-PMH41 驗命中數）

| 條號 | 主旨 | 字數 | handoff SHA256（前 16） | RULINGS SHA256（前 16） | 結果 |
|---|---|---|---|---|---|
| R-PMH43 | 已發生變更之陳述須附實測證據；同包舉證標準須一致 | 341 | `bfa28d4131e17cb8` | `bfa28d4131e17cb8` | 逐字相符 |
| R-PMH44 | 已提交之往返包原文不改字，以檔末勘誤節處理 | 354 | `91b85993581cc00a` | `91b85993581cc00a` | 逐字相符 |
| R-PMH45 | 同檔內互斥狀態陳述之一致性檢查 | 361 | `eb951180053ad6b6` | `eb951180053ad6b6` | 逐字相符 |

**R-PMH41 之遵守**：6 個 placeholder（3 條 × SHA／結果欄）各驗命中數恰為 1，
共替換 6 次（預期 6）。

---

## 2. 步驟 2 —— 08 上繳之勘誤節（R-PMH44）

### 2.1 勘誤節已追加於 `docs/upstream/08_criterion_repair.md` 檔末

其內容（全文見該檔 `## 勘誤`）：

- **被更正之節**：§11.3 步驟 8 (a) `framework.md`
- **原句逐字**（以 fenced block 保留）：
  `- 狀態由「未定版」改為 **定版**（2026-08-24，R-PMH36）；`
- **正確之事實**：該變更於 08a 輪**未發生**；`framework.md:7` 至 10 包回掃時
  仍逐字為 `- **狀態：未定版。** Test Set #2 之名為 \`Disclaimer Screen\`，
  待 Pei 裁定（06 §5.4）`
- **成因**：先換 `<PENDING Q11>`、再換含該字串之該行 → 第二個
  `str.replace()` 靜默未命中；當輪之驗證為「佔位符殘留數 = 0」（**代理量**）
- **後果**：`framework.md` 第 7 行與第 24 行互斥，跨 08a、09 兩輪並存
- **發現之輪次與證據**：10 包步驟 3 之回掃表，逐字列
  `framework.md:7  [未定版]`，判「應已被替換而殘留」
- **連帶立條**：R-PMH43／R-PMH44／R-PMH45

### 2.2 R-PMH44(c) 之驗證 —— 原句連同勘誤並存

```
原句於檔內之出現數 = 2（預期 2 —— 原文 1 ＋ 勘誤引用 1）
   - 狀態由「未定版」改為 **定版**（2026-08-24，R-PMH36）；   ← §11.3(a) 原文
   - 狀態由「未定版」改為 **定版**（2026-08-24，R-PMH36）；   ← 勘誤節之逐字引用
```

**原文一字未改**（R-PMH44 首句），僅於檔末追加。

### 2.3 雜湊變化之揭露（11 §六第 2 項）

| 對象 | SHA256 |
|---|---|
| `docs/upstream/08_criterion_repair.md`（追加勘誤節**前**） | `ed07aa016961b5d9cb7560d1e3042d506ea495d142326a2cb718cafcd3f38d04` |
| 同上（追加勘誤節**後**） | `91972102c3d3b2a122b60469656835572c1d1cac6273182f7eca7232a4168592` |
| **§11.3(a) 之原句** | **未改動** —— 其逐字內容見 §2.2 |

**所改者為「檔案」，非「該節原文」。** 該勘誤節內亦自載此二雜湊。

### 2.4 `docs/INDEX.md` 之標記

08 輪次列之上繳連結後已加 **（含勘誤）**（命中數驗證：目標字串命中 1）。

---

## 3. 步驟 3 —— `check_state_consistency.py`（R-PMH45）

**程式**：`features/power_moding/scripts/check_state_consistency.py`
**自測**：`python scripts/check_state_consistency.py --feature . --self-test` → **exit 0**

### 3.1 四組互斥對

| 對 | A 側 | B 側 |
|---|---|---|
| 定版 | `(?<!未)定版` | `未定版` |
| PENDING/RESOLVED | `\bRESOLVED\b` | `\bPENDING\b` |
| 待裁/已結清 | `已裁|已結清` | `待裁` |
| wired | `wired:\s*true` | `wired:\s*false` |

判定：同檔內兩側同時出現即 FAIL，**逐行列出行號與逐字內容**
（不以總數代替，R-PMH41 末段）。

### 3.2 `RULINGS.md`／`ANOMALIES.md` 之處理 —— **具名排除，非放寬判準**

**採「具名排除」**（11 §四步驟 3 末段所許之二選一），理由：

二檔為**多對象登記簿** —— 其 `PENDING` 與 `RESOLVED` 分屬不同 anomaly、
`待裁` 與 `已結清` 分屬不同 Q 項，**全檔字串共現是正常且必然的**，不是不一致。
要對它們做互斥判定，須先以「同一 `A-PMH{n}`／`R-PMH{n}`／`Q{n}`」為單位切分，
而該切分**無法由行級掃描乾淨得出**（狀態可寫在節標題、表格列或內文任一處，
且一則 anomaly 之內文常引述他則之狀態）。

**故不納入，並於每次輸出中具名其排除理由**（程式之 `EXCLUDED` 常數，
每次執行皆印出）。**未放寬判準後宣稱通過 —— 停止條件 9 未觸發。**

### 3.3 範圍向（R-G9）—— 現行四檔全 PASS

```
=== 互斥狀態一致性檢查（範圍向） ===
具名排除之檔（R-PMH45，非放寬判準）：
    RULINGS.md —— 多對象登記簿 …
    ANOMALIES.md —— 同上 …

  framework.md       PASS
  feature.yaml       PASS
  DECISIONS.md       PASS
  PLAYBOOK.md        PASS

  範圍向 PASS ✅
```

### 3.4 故意失敗 —— **於暫存副本上**把 `framework.md:7` 改回「未定版」

```
    注入於 L7：- **狀態：未定版。** Test Set #2 之名為 `Disclaimer Screen`，待 Pei 裁定（06 §5.4）

  framework.md       **FAIL** —— 1 組互斥對兩側並存
      [定版]
         L24    (A 側) ## Layer 2 —— Test Set（8 組，**定版**）
         L7     (B 側) - **狀態：未定版。** Test Set #2 之名為 `Disclaimer Screen`，待 Pei 裁定（06 §5.4）

  故意失敗 被攔下 ✅
  （注入僅在暫存副本上；ROOT 之檔案未被改動）
```

**檢查精準指出 L7 與 L24 兩行** —— 即 08a／09 兩輪間之實際不一致狀態。
**停止條件 7 未觸發。**

> **本檢查之價值**（R-PMH45 末段）：它抓的是**替換未命中之結果**而非過程 ——
> 10 包 §6 第 1 項自陳「回掃之判準是找得到的標記，不是所有未命中之替換」，
> 而本檢查**不依賴標記清單**，只依賴「兩個互斥狀態同時存在」這個事實。
> 歷史上已無 before 可查之替換，其殘留仍會被它抓到。

---

## 4. 步驟 4 —— `--check-doc-sync` 之強化（雜湊 → 雜湊 ＋ 表內容）

10 包 §6 第 3 項自陳：「只驗一個雜湊，不驗門檻表之內容 ——
手改門檻**數值**而不動雜湊行，檢查會 PASS。」**本輪已修。**

現為**兩項並驗**：
1. 程式 SHA256 之記載與程式現值相符（記載數須恰 1 —— R-PMH41）；
2. **文件之門檻表與 `emit_thresholds()` 之輸出正規化後逐字相同**
   （去行首尾空白、摺疊 cell 內對齊空白；表數須恰 1）。

### 4.1 兩項故意失敗皆被攔下

```
  [故意失敗 1] 注入假雜湊（模擬程式已改而文件未重貼）
    doc-sync **FAIL** 攔下 ✅ — **門檻表已與程式分岔（雜湊）** ——
    文件記 `eada46d05ea268f0…`，程式現值 `0000000000000000…`。

  [還原] 用程式實際雜湊
    doc-sync PASS ✅ — 文件與程式同源 —— SHA256 `eada46d05ea268f0…`（命中 1 處）
    ＋ 門檻表 7 列逐字相同

  [故意失敗 2] 手改文件之門檻值 `1/3` → `0.35`（雜湊行不動）
    doc-sync **FAIL** 攔下 ✅ — **門檻表之內容已與程式分岔** ——
    L3: 文件 '**G1**|組數 / leaf|`<=`|**`0.35`**|canon §4.1.3 …'
     vs 程式 '**G1**|組數 / leaf|`<=`|**`1/3`**|canon §4.1.3 …'。
    （雜湊相符但表被手改 —— 雜湊是代理量，故此項另驗）
```

**停止條件 8 未觸發。** `--self-test` 之整體 exit 0。

### 4.2 強化本身又觸發了一次雜湊分岔（真實情境，第二次）

改動 `check_doc_sync()` 即改了程式，`--check-doc-sync` 當場 FAIL
（`07aea6e3…` vs `eada46d0…`）。重貼雜湊行（命中數驗證：1）後 PASS。
**與 10 包 §2.1 同一形態 —— 該檢查已第二次在真實情境下攔下自己。**

---

## 5. 步驟 5 —— profile

**本輪未做任何與 profile 相關之動作**（11 §四步驟 5）。
`docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md` **仍不存在**。

---

## 6. 本包是否仍有該驗而未驗者 —— 獨立判斷

**有，五項。**

1. **`RULINGS.md`／`ANOMALIES.md` 之互斥一致性至今無任何檢查。**
   §3.2 之具名排除是誠實的，但**排除不等於解決** —— 那兩個檔正是
   狀態陳述最密集之處（每則 anomaly 都有 PENDING／RESOLVED）。
   若某則 anomaly 之標題寫 RESOLVED 而其內文仍寫「待 Pei 裁定」，
   **現行無任何檢查會發現**。按條號切分之實作是可行的
   （以 `^## (A-PMH\d+)` 切段，段內判互斥），**本包未做**。

2. **四組互斥對是列舉，不是全集。** R-PMH45 稱其為「最低限度」，
   而實際上還有：`已授權`/`未授權`、`已接上`/`wired: false`、
   `已定案`/`待裁`、`FULL`/`BLANK`（workbook_state）。
   **未列舉者不會被檢查** —— 與 A-PMH08／A-PMH13 同族之形態
   （判準以列舉為之，形態一變即靜默脫落）。

3. **`--check-doc-sync` 之表內容比對只認一張表。** 若日後 `framework.md`
   出現第二張同格式表（`| id | 量 | 關係 | 門檻 | 來源 |`），檢查會因
   「表數 ≠ 1」而 FAIL —— **這是安全的失效方向**，但會誤報。未處理。

4. **勘誤節之格式無檢查。** R-PMH44 定了 (a)(b)(c) 三項，
   而**沒有任何程式驗某份上繳包之勘誤節是否齊備該三項**。
   本輪之勘誤節係人工照條文寫成。

5. **三次「下放包載提交狀態而已過時」未立條。** §0 已具名其為第三次，
   並提了建議（下放包不再載提交狀態），**但未立條** ——
   它是分析層之撰包慣例，不在執行層之權限內。**列為建議，待裁。**

---

## 7. 停止條件逐條檢查

| # | 條件 | 本輪 |
|---|---|---|
| 1 | 規格查找未解 | 未觸發 |
| 2 | `workbook_state` 分段有歧義 | 未觸發 |
| 3 | 寫回不變量違反 | 未觸發 —— 零寫回 |
| 4 | 需要之規則無 canon／profile 涵蓋 | 未觸發 |
| 5 | 造值壓力 | 未觸發 —— profile 未動 |
| 6 | done region 與規格矛盾 | 未觸發 |
| 7 | 步驟 3 之故意失敗未攔下或範圍向 FAIL | **未觸發** —— 攔下並精準列出 L7／L24；四檔全 PASS |
| 8 | 步驟 4 之故意失敗未攔下 | **未觸發** —— **兩項**故意失敗皆攔下 |
| 9 | `RULINGS.md` 採放寬判準後宣稱通過 | **未觸發** —— 採**具名排除**，理由於每次輸出中印出 |

---

## 8. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(power_moding): package 11 — errata to 08, state-consistency check, doc-sync hardened
```

```
git add -- features/power_moding/RULINGS.md \
           features/power_moding/framework.md \
           features/power_moding/scripts/check_granularity.py \
           features/power_moding/scripts/check_state_consistency.py \
           features/power_moding/docs/INDEX.md \
           features/power_moding/docs/handoff/11_claim_evidence.md \
           features/power_moding/docs/upstream/08_criterion_repair.md \
           features/power_moding/docs/upstream/11_claim_evidence.md
```

- **`docs/upstream/08_criterion_repair.md` 在 pathspec 內** ——
  R-PMH44 末句：「追加勘誤節本身是對檔案之修改，須列入該輪之 pathspec 並揭露。」
  **該檔上次已於 `931053f` 提交，本次為其勘誤節之追加。**
- **未寫入 `docs/runtime/profiles/`**；`feature.yaml`／`DECISIONS.md`／
  `PLAYBOOK.md`／`ANOMALIES.md` 本輪未改。
- **未觸碰 `features/power/docs/internal_var_observability.md`**（11 §五之禁止項）。
- `scripts/new_feature.py` 未改。
- pathspec 逐項寫全名（R-PMH3(c)）。

### 8.1 git 動作揭露（R-G6）

| 類別 | 指令 | 次數 |
|---|---|---|
| **唯讀 git** | `git status --short`／`git log -1 --format`／`git diff --cached --name-only` | 4 |
| **改狀態 git** | `git add` ＋ `git commit`（**10 包**，Pei 指示，帶 pathspec） | 2 |

> 本輪之改狀態 git 為 **10 包之提交**（`c4f276f`），依 Pei 之指示執行；
> **11 包之提交尚未授權。**

---

## 9. 待 Pei 裁定 —— **兩項阻斷 Phase 4，已阻斷三輪**

| # | 事項 | 阻斷 |
|---|---|---|
| **profile 草案** | 10 包 §四全文。核對零不符（10 上繳 §5）。核可後寫入 `docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md` | **是** |
| **A-PMH13** | `-028` 之處置。**連帶**：若裁 (ii)，profile §0／§2 之「48 leaf」須加註「其中 1 條為揭露列」 | **是** |
| **11 包之 commit 授權** | pathspec 見 §8（8 路徑，含 08 上繳之勘誤追加） | 否 |
| **§6 第 1 項** | `RULINGS.md`／`ANOMALIES.md` 之互斥一致性 —— 是否實作按條號切分之檢查 | 否 |
| **§6 第 5 項** | 建議下放包不再載提交狀態（三次過時） | 否 |
| Q10 | `Product Document 記錄封面頁` | 否，Phase 7 前 |
