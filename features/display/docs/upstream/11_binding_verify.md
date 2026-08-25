# 上繳包 11 —— 綁定檢查、合併複驗（**停止條件 29 觸發**）

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/11_binding_verify.md`
- 結果：**步驟 1、2、4、5、6 完成；步驟 3 觸發停止條件 29，已停於待裁**
- 全部 git 操作屬 Pei —— §7 只備妥訊息與 pathspec，未執行

---

## 0. 先講：合併漏了三項

下放包 11 §二把我上輪 §8 第 2 項「合併後之 `DECISIONS.md` 未經 recon
複驗」排成步驟 3。**一驗就查出三項**，超出上繳 10 §3 所列之 9 項分歧，
**停止條件 29 觸發，未自行修正。**

| # | 項 | `recon.py` | 合併後之 `DECISIONS.md` |
|---|---|---|---|
| 1 | `ruled-constant assertions` | `[AUTO] 0 checked, 0 PASS, 0 FAIL` | **無此項** |
| 2 | `Test Set table (Part N)` | **`[PEI]`** — draft with Claude, Tier 2 | `[PROPOSED]` → 待 Phase 3 |
| 3 | `profile [OVERRIDE] clauses` | **`[PEI]`** — draft with Claude, Tier 2 | `[PROPOSED]` → 待 Phase 3 |

詳見 §3。

> 我上輪自陳「合併這個動作本身沒有被交叉檢查」時，那是一句還沒有代價的話。
> 本輪它有了代價：三項。

---

## 1. §四二條之抄錄核對表（步驟 1，腳本產出）

## 抄錄核對表 — 11_binding_verify.md（機器輸出，R-G20）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 37 | R-DM35 | `features/display/RULINGS.md` | 398 | `cb764ed606f6f896` | 是 |
| — | R-G23 | `docs/fw036/RULINGS_LEDGER.md` | 389 | `d55dd4244d483911` | 是 |

累計：`RULINGS.md` 之 R-DM 區塊 **37** 個，與各下放包原檔逐字元比對 **全數相符**（37 vs 37）。

---

## 2. `reference:` 綁定檢查（步驟 2，R-G23）

### 2.1 本輪執行之輸出

```
# reference binding check (R-G23)
feature.yaml: /Users/peihe/Work_Projects/TC_Generator/features/display/feature.yaml
entries: 4

| key | file | declared | actual | verdict |
|---|---|---|---|---|
| dbc_b | `PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3db62ac9f…` | `46cb73f3db62ac9f…` | MATCH |
| dbc_fd | `PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf3e670d71…` | `2a86c4bf3e670d71…` | MATCH |
| lid | `Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679c706cd45…` | `a01e1679c706cd45…` | MATCH |
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3d58d…` | `e7c2020f01c3d58d…` | MATCH |

**4 of 4 match.**
```

**4/4 相符，退出碼 0。停止條件 28 未觸發。**

### 2.2 失敗分支之實測（下放包未要求）

依 08 輪之教訓（未經執行之錯誤路徑等同未實作），蓄意將 `proxi` 之宣告值
改為全 0 後執行：

```
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `0000000000000000…` | `e7c2020f01c3d58d…` | **MISMATCH** |

**1 of 4 FAILED.** Full values:
  proxi: declared 0000…0000 / actual e7c2020f01c3d58db431babe7f8a41acbe528c451bd37ef6bb84f1b312be6ff2

R-G23: stop and report. Do NOT update the declared value in feature.yaml —
that would adopt an unruled revision of the reference database.
```

三項成立：**兩值全碼皆印出**（不只前 16 碼）、**退出碼 1**、
**`feature.yaml` 未被改寫**。狀態已還原並複驗（4/4 相符）。

### 2.3 應被呼叫之時機（提案，未實作串接）

| 時機 | 理由 |
|---|---|
| **任何讀取 DBC／LID／PROXI 之腳本執行前** | `signal_resolution.py`／`dbc_probe.py`／`proxi_candidates.py`／`lid_version_diff.py` 四支之產出全部掛在這四個檔上 |
| **每輪上繳之前** | 使「本輪之量測基於哪一版素材」成為可查證之事實，而非假設 |
| **Phase 4 每批 TC 產出之前** | R-DM19 之承載範圍含「此後所有 Display TC 之訊號名、訊息、raw 值、`VAL_` 標籤、收發節點」 |
| **不建議之處**：`recon.py` 或其他共用腳本內 | 那會使其他 feature 之行為改變，且各 feature 之 `reference:` 節未必存在 |

**未實作串接** —— 串接會改變上述四支腳本之失敗行為（多一個退出點），
屬 Tier 2。本輪只提供檢查本身。

---

## 3. 合併後 `DECISIONS.md` 之 recon 複驗（步驟 3）—— **停止條件 29 觸發**

### 3.1 方法

依 R-DM35(b)：舊 `DECISIONS.new.md` 改名為
`DECISIONS.new.2026-08-25a.md` 保留，重跑 `recon.py --feature
features/display` 產生新的 `DECISIONS.new.md`。

**新舊兩份逐字相同** —— `recon.py` 之產出穩定，本次複驗之基準與上輪
所依者為同一內容。

以正規式逐項抽出 recon 之 24 個項目行，逐項在合併後之 `DECISIONS.md`
中尋其對應。

### 3.2 結果：24 項中 21 項有對應，**3 項為新分歧**

| # | 項 | recon | 合併檔 | 性質 |
|---|---|---|---|---|
| 1 | `ruled-constant assertions` | `[AUTO] 0 checked, 0 PASS, 0 FAIL` | **完全沒有這一項** | **遺漏** |
| 2 | `Test Set table (Part N)` | `[PEI]` | `[PROPOSED]` | **marker 不一致** |
| 3 | `profile [OVERRIDE] clauses` | `[PEI]` | `[PROPOSED]` | **marker 不一致** |

### 3.3 第 2、3 項之時序 —— 不是我在合併時降的格

`git log -S` 查得該兩行之 `[PROPOSED]` 出自 **`61d1c12`（2026-08-24，
02 輪）**，**早於 `recon.py` 首次成功執行（09 輪）**。

即：這兩項是我在 02 輪自行填寫時就標了 `[PROPOSED]`，而 recon 認為
它們應為 `[PEI]`。**上輪之合併沒有察覺這個既存分歧** ——
它不在我列的 9 項裡，因為我根本沒比到這兩行。

**這一點對 R-DM32 之適用有影響**：該條規制兩個方向 ——
「機器不得將 `[PEI]` 降格」與「recon 所增之項不得自動升格」。
**本情形兩者皆不適用**：兩項在兩份檔中都存在、只是 marker 不同，
且較嚴格者（`[PEI]`）在機器側。R-DM32 未涵蓋此向。

### 3.4 第 1 項之性質

`ruled-constant assertions` 在合併檔中完全缺席。它是
`[AUTO] 0 checked, 0 PASS, 0 FAIL` —— 一個「什麼都沒檢查」之記錄。

**正因為它的值是 0，它最容易在合併時被略過**：一個內容為空的項，
讀起來像沒有內容。但它記的是「本 feature 未宣告任何 ruled-constant
assertion」這件事，而那是一個應該被看見的空。

### 3.5 已停，未自行修正

三項**皆未寫入 `DECISIONS.md`**。理由：

- 停止條件 29 明文「停並回報」
- 第 2、3 項需裁示「兩側都存在而 marker 不同時，何者為準」——
  R-DM32 未涵蓋此向，逕自採 recon 之 `[PEI]` 或維持我的 `[PROPOSED]`
  都是在替一條不存在的規則作主
- 第 1 項雖看似可逕補，但補進去就等於認定「合併之遺漏可由執行層
  自行回填」，而上輪之遺漏正是因為沒有人檢查

---

## 4. `spec_text_layer.tsv` 之腳本化（步驟 4）

`probe_spec_mode.py` 現直接產出該檔與其 sidecar，三個數字**現算**：

```
## spec text layer —— 三種計法（寫入 data/spec_text_layer.tsv）
  pymupdf                                  854333  registered=Y
  python-docx（段落＋表格格，正規化後）                 907382  registered=N
  python-docx（未正規化、含空段）                    910850  registered=N

```

| 項 | 處理前 | 處理後 |
|---|---|---|
| 資料列數 | **3** | **3** |
| `generated_by` | `下放包 10 步驟 3（人工登記…）` | **`features/display/scripts/probe_spec_mode.py`** |
| 三個數字之來源 | 人工填入 | **每次執行現算** |

列數未變（R-G16 還原檢查通過）。上輪 §8 第 3 項「會過期而不出聲」
之缺陷已消除：抽取器一改，數字下次執行即改。

> 實作時撞到一個小坑：`probe_spec_mode.py` **本來就沒有 `norm()`**
> （它到處用內聯的 `" ".join(...split())`），我把新函式搬進來時假設它有。
> 三次 `NameError` 後補上。記此事是因為它與 R-G19 同型 ——
> 我對一份自己寫過的腳本做了一個未經查證的假設。

---

## 5. `proxi_candidates.tsv` sidecar 之來源綁定（步驟 5）

sidecar 之 `inputs` 欄現載三份來源之 sha256：

| 檔 | sha256（前 16 碼） |
|---|---|
| `forms/Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679c706cd45…` |
| `forms/PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3d58d…` |
| `inputs/Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` | `ab3198e81fb21d21…` |

**未實作自動失效機制**（同 R-G15 之分寸）：記錄使綁定可見，
察覺其失效者為 `verify_reference_binding.py`。

`DECISIONS.new.md` 與 `DECISIONS.new.2026-08-25a.md` 兩份皆已依
R-DM35(a) 於檔首加註其地位（帶時間戳之證據、不得作為簽核標的、
已併入之日期與分歧處置之出處）；後者另註明其與前者逐字相同。

---

## 6. 「本包是否仍有該驗而未驗者」—— 執行層之獨立判斷

**有，共 5 項。**

1. **§3 之三項分歧未裁，`DECISIONS.md` 現處於已知不完整之狀態。**
   它仍是權威（R-DM32），但已知缺一項、且兩項之 marker 與管線不符。
   **在裁示前，任何以它為據之簽核都會帶著這三個洞。**
2. **合併之複驗只做了「recon 有而合併檔無」這一向。** 反向
   （合併檔有而 recon 無）未系統性比對 —— 我的檔有 §5 Split & scope、
   §待裁清單等 recon 完全沒有的節，那些是自測獨有還是 recon 漏了，
   **沒查**。
3. **`verify_reference_binding.py` 未被任何腳本呼叫。** §2.3 只是提案；
   在串接之前，它與「沒有這支腳本」的差別只在於「有人記得手動跑」。
4. **036 母本不在 `reference:` 節內。** 該節綁了 DBC／LID／PROXI 四項，
   但 036 母本（`6372fb6b…`）之綁定只存在於 `paths.workbook` 之註解裡，
   **不被 `verify_reference_binding.py` 檢查**。而它是寫回之標的。
5. **`spec_text_layer.tsv` 之三個數字現算了，但沒有人在比對它們。**
   若 pymupdf 換版導致 854,333 變動，該檔會安靜地更新 ——
   **與上輪之「人工登記會過期」相比，換成了「會無聲改變」。**
   兩者都不出聲，只是方向相反。

另記本輪**已驗而下放包未要求**者：綁定檢查之失敗分支（§2.2）；
新舊 `DECISIONS.new.md` 之逐字比對；第 2、3 項分歧之 `git log -S` 時序追查。

---

## 7. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(display): reference binding check; merge re-verification finds 3 gaps

- R-DM35 + R-G23 verbatim (2/2, 37/37 cumulative)
- verify_reference_binding.py: 4 of 4 match. Its failure branch was also
  exercised — both full hashes printed, exit 1, feature.yaml untouched
- STOP CONDITION 29: re-verifying the round-10 merge against recon found
  three items it missed. ruled-constant assertions is absent from the
  merged file entirely; Test Set table and profile [OVERRIDE] carry
  [PROPOSED] where recon says [PEI]. The latter two date from 61d1c12,
  before recon ever ran, so they are a pre-existing divergence the merge
  did not notice rather than a downgrade performed during it. None of the
  three was fixed: R-DM32 covers machine-downgrades and recon-added
  items, not the case where both files have the item with different
  markers and the machine holds the stricter one
- spec_text_layer.tsv is now produced by probe_spec_mode.py; the three
  figures are computed each run instead of hand-entered. 3 rows before
  and after
- proxi_candidates.tsv sidecar records the sha256 of its three sources
- DECISIONS.new.md files annotated per R-DM35; the rerun produced a
  byte-identical file, old one kept as DECISIONS.new.2026-08-25a.md
```

pathspec：

```
git add docs/fw036/RULINGS_LEDGER.md \
        features/display/RULINGS.md \
        features/display/DECISIONS.new.md \
        features/display/DECISIONS.new.2026-08-25a.md \
        features/display/scripts/ \
        features/display/data/ \
        features/display/docs/
```

**`features/display/DECISIONS.md` 不在其中** —— §3 之三項分歧未裁，
本輪未改該檔。共用 `scripts/`、`forms/`、`.gitignore` 亦未動。
