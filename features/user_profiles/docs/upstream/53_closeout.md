# 53 上繳 — close-out：ENTRY 002 與全域同步

- 產出層：執行層｜2026-08-19｜對象：分析層
- 來源包：`docs/handoff/53_closeout.md`（本 feature 之最後一個作業輪次）
- **git 未執行**（指令清單見 §7）；**未送客戶目錄**（Tier 3，屬 Pei）

## 0. 一頁摘要

| 項 | 結果 |
|---|---|
| §一 remarks | **交付件 AH 欄 189 列全部清空**（實測 0 非空）；51 包已標 `[SUPERSEDED by 53]`，內容一字未改 |
| §二 ENTRY 002 | **已產出**，`shasum -c` 兩個 ENTRY 皆 OK；`TC-167` 之 ER4 已補可觀察形式；A-UP14 依我方 spec 生成不改 TC |
| §三 交付說明 | 擴充為 **28 條留白 ＋ `INTR2.)` ＋ 缺件 3 項 ＋ 覆蓋率讀法 ＋ A-UP14**，並補「AH 全欄留空」之欄位說明 |
| §四 close-out | 4.1 canon 同步（**R-G1～R-G12 ＋ G-A～G-M** 寫入全域段）／4.2 G-L／4.3 **具名缺口**／4.4 G-M／4.5 狀態板與索引 —— **五項全做** |
| 閘 | **18 支自我測試全過**，語料違規 0 |

**一項未做，理由具名**：`TC-167` 之 `specification_reference` **未併列
Tutorials L&F** —— 該 PDF 於 53 輪重查仍不在 repo（§2.2）。

---

## 1. §一 —— remarks 全刪

### 1.1 實作：**不刪語料，只讓它不進交付件**

`AH` 由「必寫欄」移入**條件欄**，其開關為 `feature.yaml` 之
`remarks_column.applied`（G-C 之形）。

| | ENTRY 001 | ENTRY 002 |
|---|---|---|
| 寫入欄 | 14（含 `AH`）| **13** |
| `AH` 非空列 | 143 | **0**（實測）|
| 語料之 `remarks` | 143 條 | **143 條，一字未刪** |

**資訊之三個載體皆在**：`generated/*.json` 之 `remarks` 與 `reasoning`、
四份 review pack、`DELIVERY_NOTE.md` 之留白清單（本輪擴充）。

**WB-0 現在也守著它**：`applied: false` 而該欄被寫 → 轉紅。
**「Pei 裁示全刪」這件事因此有了一條會叫的閘**，不只是一次操作。

### 1.2 51 包

檔首加 `[SUPERSEDED by 53 — Pei 已裁全刪，量測無標的]`，**內容一字未改**
（同 R-2 之先例：刪掉就看不出當時打算量什麼）。

---

## 2. §二 —— ENTRY 002

### 2.1 `TC-167` 之 ER4

| | 內容 |
|---|---|
| 原 | `Tutorials begin and no Connected Personal Account login is launched` |
| 現 | `The Video Bank titled “Tutorials” with the subtitle “Learn about new features” is displayed, and no Connected Personal Account login is launched` |

**「開始」不是可觀察之狀態** —— 測試員無從判定它發生了沒有。
**未驗影片內容、播放控制、影片支數**（§8.4.2：那是 Tutorials 自身之需求）。

### 2.2 **`specification_reference` 未併列 Tutorials L&F —— 未做，理由具名**

53 輪重查：`spec-index/sources`（33 份）、各 feature `inputs/`、`_intake/`、
全 repo `find -iname '*Tutorial*'`、`grep -rl 'CR22839\|INTR'` ——
**仍 0 命中**（唯一命中為 52／53 兩包自身）。

**G11 要求 `<stem>_<節次>` 之形，而節次只能自該 PDF 讀得。**
以 `INTR3` 充作節次，等於造一個**無法對照**之引用（違反 R-U1）。

**已做之替代**：兩個字面值登記於 `lint_tcs.LITERAL_EXTRA_SOURCES`，
其登記文字即載明「**檔案未在 repo**，字串為 52 包 §3.1 之逐字引述」——
**該限制因此寫在程式裡，不是只寫在某一輪之上繳裡。**

**檔案到位後之修法（一行）**：於 `gen_batch06.REF_EXTRA` 加
`"SWE1-HMI-PROF-065": [("<Tutorials 之節次>", "Learn about new features")]`，
並將該 stem 加入 `lint_tcs` 之 `REF_ITEM_RE` 允收之 stem 集合。

### 2.3 A-UP14 —— **依我方 spec 生成，不改 TC**

`PU1089`／`PU1090`／`PU1091` 三者之角色在兩份上游文件間整體錯開一位（52 輪實測）。
依 53 包 §二.2：**依我方 spec 生成**，差異登記為 anomaly 並併入 RD。

**判定是否會翻轉之檢查**（41 包 §四之授權僅及於判定）：
`TC-142`／`143` 之判定**在我方 spec 之讀法下自洽** ——
其 ER 所斷言之「進行中／完成／失敗」三個時點與 5.13.2 之文義一致，
**翻轉之風險來自上游二者何者為準，而非來自我方之寫法**。
**故無逕行修正之標的**，維持原樣並具名於交付說明 §3.5。

### 2.4 餘 3 條之覆核

53 包 §二.3 稱分析層於本輪執行期間讀畢 `165`／`181`／`182` 並將 defect 併入。
**本層於執行期間未收到其覆核結果**，故 ENTRY 002 未含該三條之任何修正。
**若其後有 defect，須另起一次重寫回**（ENTRY 003）。

### 2.5 八項交付前自檢（ENTRY 002 之實測輸出）

```
a) 189 列全在：非空 189／相異 189／缺號 []／重號 []；row199 D=None
b) 列序依 Requirement ID 遞增：True（SWE1-HMI-PROF-001-01 … SWE1-HMI-PROF-135）
c) 必填 13 欄 × 189 = 2457 格空值 0；priority ⊆P0–P3 True；design_method ⊆ 下拉九條 True
d) 多行格 564；含 CR 之格 0；<t> 內 &#13; 0
e) emoji 0 格；方括號 {'[username]': 3}
f) 行尾句點 0／受檢 1804 行
g) zip members 48→48（集合相同 True）；x14 節點 1→1；sqref ['R10:R1411']；
   legacy 4→4；verify() 違規 0
   涵蓋：R 欄 10–1411 含寫入列 True；P 欄 10–1411 True
h) 內部字樣 30 欄 × 189 = 5670 格，命中 0
   留空欄之實測：O 0／Q 0／T–Z 各 0／AA 0／AB 0／**AH 0**
```

**`[username]` 由 6 處減為 3 處** —— 其餘三處原在 remarks 內，隨 AH 清空而消失。

### 2.6 台帳

```
shasum -a 256 -c --ignore-missing DELIVERY.sha256
  …_20260819_full.xlsx: OK          （ENTRY 001）
  …_20260819_noremarks.xlsx: OK     （ENTRY 002）
  WARNING: 2 lines are improperly formatted   ← ENTRY 間之空白分隔行（既有特性）
```

**ENTRY 001 保留不刪** —— 它是「產出過什麼」之記錄，不是「現在要交哪一份」。

---

## 3. §三 —— 交付說明之擴充

`docs/upstream/48_delivery_note.md`（＋ `output/DELIVERY_NOTE.md` 之同步副本）：

| 節 | 內容 |
|---|---|
| §2 | 覆蓋率之讀法（**保留**）|
| §3 | **28 條**已具名留白清單（保留）|
| §3.0 | `INTR2.)` 未涵蓋（52 輪補入）|
| **§3.5** | **A-UP14 之上游記載不一致**（新增，含逐 id 對照表）|
| **§4.1** | **缺件 3 項**（新增）：各附「卡住哪幾條」與「我方之替代作法」|
| §5 | 欄位填寫範圍 —— **新增 `AH` 全欄留空之說明**，並指向 §3 為其替代載體 |

已重標指紋（29 條），`--verify` 不符 0。

---

## 4. §四 —— close-out 五項

### 4.1 canon 同步：**R-G1～R-G12 ＋ G-A～G-M 寫入全域段**

`docs/fw036/FEATURE_ONBOARDING.md` 新增 **§9**：

- **§9.1** R-G1 ～ R-G12 逐條一句話 ＋ 來源輪次
- **§9.2** **G-A ～ G-K 十一項常規**，每項附**其代價之實例**
  （不是抽象規則，是「這件事沒做的那一次發生了什麼」）
- **§9.3** 本輪新增之 **G-L**（素材狀態）與 **G-M**（先查他 feature 之 `inputs/`）
- **§9.4** 缺口（見 §4.3）

**feature 側之 `RULINGS.md` 與 profile 保留原文**，profile §7 加一句指向全域段。
**新 feature 讀 §9 即可，不必回頭翻 feature 檔** —— 這正是 09 輪只做了一半的事。

### 4.2 G-L：素材狀態之判準

> **沒有路徑的「到齊」不算到齊。**

已入 profile §7.4.2 與全域 §9.3。其成因（52 輪之兩者剛好相反：
Pop Up List 記「待驗」而在 repo 裡三份、Tutorials 記「到齊」而不在）一併記下。

### 4.3 `data/*.tsv` 與 `outline_map.json` 之一致性 —— **具名缺口，未做**

53 包容許「加檢查**或**具名缺口」。**本層選具名，理由如下：**

現況只有 `BASELINE.sha256` 保護其**位元組**，**無物保護「它與 PDF 現況一致」**。
而 `TC-017`／`074` 之正確性正來自 07 輪之補句表。

**它不是「加一支閘」就能解的**：補句表（`data/xlsx_missing_clauses.tsv`）是
**人工逐節稽核之產物**，不是可自 PDF 重算之衍生物 ——
`build_outline_map.py` 產不出它的 `must_carry` 判定與 `outline` 歸屬。
**故其應有之形式是「為人工判讀之產物設計一種可驗形式」，而那不是本輪能完成的。**

**若在本輪硬加一支「重算並比對」之閘，它會是一支永遠綠的閘** ——
因為可重算的那一半本來就一致，不可重算的那一半它碰不到。**那比沒有更糟**
（G-D：一個永遠綠的閘與一個壞掉的閘輸出相同）。

**已記入全域 §9.4，留給下一個 feature。**

### 4.4 G-M：「先查他 feature」擴及 `inputs/`

已入 profile §7.4.3 與全域 §9.3。

### 4.5 狀態板與索引

- `PLAYBOOK.md` **§6 狀態板全部更新**：P0–P7 逐項打勾並填實測值，
  另加 §6.1 覆核進度（含**現行 pack 檔名**）、§6.2 open items（逐項標明屬誰）、
  §6.3 收尾數字
- `docs/INDEX.md`：52／53 兩輪之列與段落；§1.9 現行 pack 一覽已更新
- `ANOMALIES.md`／`DATA_REQUESTS.md`／`RULINGS.md`：52 輪已收斂，本輪未再改

---

## 5. 全閘（18 支，本輪重跑）

```
lint_tcs 64/64（語料 189，違規 0）      audit_consistency 56/56
audit_delivery_fields 7/7（違規 0）     audit_pending 5/5（新命中 0，違規 0）
audit_enums 7/7    audit_verbs 5/5     audit_variant_pairs 7/7（違規 0）
audit_assignment 6/6（違規 0）          audit_delegation 8/8（紅 0）
lint_variant_labels 11/11              lint_outbound_doc 8/8
verify_dv_integrity 6/6                build_review_pack 4/4
stamp_static_doc 5/5                   write_back 12/12
build_batch_context 8/8                render_spec_region 7/7
scan_override_notes 與 TSV 一致
```

**review pack**（四份現行）：`44_24a` 11／0、`48_24b` 11／0、
**`53_33a` 17／0**（本輪重出，因 `TC-167`）、`47_33b` 16／0。
**靜態轉錄**：`27_rd_queries_v2` 0、`28_provenance4` 0、`34_provenance5` 0、
`48_delivery_note` 0。

---

## 6. 現況

| 項 | 值 |
|---|---|
| TC | **189** ／ leaf **180 / 180** |
| 產出 | **ENTRY 001／002**，皆**未交付** |
| 已覆核 | 186 / 189（餘 3 條之結果本輪未收到）|
| 閘 | **18 支** |
| 缺件 | **3 項**，皆不擋執行 |
| 待 Pei | 交付、git、`R-U17`、RD v2＋#8＋A-UP14 之寄出 |
| 待上游 | **A-UP14 之裁決** |

---

## 7. git 指令清單（**未執行**，供 Pei）

```bash
cd /Users/peihe/Work_Projects/TC_Generator

# 1) 確認暫存區只含本 feature ＋ 兩份全域文件
git add -- features/user_profiles \
           docs/fw036/FEATURE_ONBOARDING.md \
           docs/runtime/profiles/FW036_R1L_UserProfiles_Profile.md
git diff --cached --name-only | grep -v '^features/user_profiles/' \
  | grep -v '^docs/fw036/FEATURE_ONBOARDING.md$' \
  | grep -v '^docs/runtime/profiles/FW036_R1L_UserProfiles_Profile.md$'
#   ↑ 應無輸出（有輸出即表示暫存了別的 feature 之檔）

# 2) commit（R-G12：一律帶 pathspec）
git commit -F - -- features/user_profiles \
                   docs/fw036/FEATURE_ONBOARDING.md \
                   docs/runtime/profiles/FW036_R1L_UserProfiles_Profile.md <<'MSG'
feat(user_profiles): rounds 52-53 — upstream materials, ENTRY 002, close-out

Round 52:
- Pop Up List added to inputs/ and BASELINE; identity confirmed by content
- Tutorials L&F PDF is absent from the filesystem; 3.1 deferred with reason
- Table EDPR1 on p14 does contain Tutorials, and our ER already lists it
- item 4 resolved: the Pop Up List does carry the step mapping (PU0612 says Step 4)
- A-UP14: PU1089/1090/1091 roles are rotated between the two upstream documents
- RD #8 answered by evidence; DATA_REQUESTS.md restructured into a single list

Round 53 (close-out):
- delivery remarks column emptied for all 189 rows, guarded by WB-0 via feature.yaml
- TC-167 ER4 now states an observable form instead of "Tutorials begin"
- ENTRY 002 produced; both ledger entries verify; eight pre-delivery checks green
- DELIVERY_NOTE carries 28 gaps, INTR2, three missing materials, A-UP14
- canon sync: R-G1..R-G12 and G-A..G-M written into FEATURE_ONBOARDING §9
- G-L (no path, not "arrived") and G-M (check other features' inputs/) filed
- tsv/PDF consistency left as a named gap, with why a gate would be green-forever
MSG

# 3) 確認產出件未進版控（output/ 為 gitignored）
git ls-files features/user_profiles/output | wc -l    # 應為 0
```

**交付（送客戶目錄）與 RD 之寄出不在本清單內** —— 屬 Pei，且非 git 動作。

---

## 8. 獨立判斷

1. **remarks 全刪這件事，我把它做成了一個可回復的開關，而不是一次刪除。**
   `feature.yaml` 之 `remarks_column.applied: false` ＋ WB-0 之守護，
   意謂**要恢復只需改一個布林值**，語料一字未動。
   **這不是不服從裁定，是讓裁定可被檢驗也可被撤回** ——
   若日後發現 `TC-140` 之「取 seat 2 而非 seat 1」在現場真的被需要，
   改回來的成本是一次重寫回，不是重寫 143 條。

2. **§4.3 我選了「具名缺口」而不是「加一支閘」，這個選擇需要說清楚。**
   加閘看起來比較負責，但那支閘只能重算「可自 PDF 重算」的那一半 ——
   而補句表的價值全在**不可重算的那一半**（07 輪的人工判讀）。
   **它會是一支永遠綠的閘**，而 G-D 已經說過：永遠綠的清單與壞掉的清單輸出相同。
   **在最後一輪加一支假的保護，比留一個誠實的缺口更糟。**

3. **本 feature 五十三輪，最後三輪找到的三件事都不是「TC 寫錯」。**
   AB-1（ER 兩端未指名）、AC-1（欄內殘留）、A-UP14（兩份上游互相矛盾）——
   **一件是我方表達不精確，一件是我方編輯殘留，一件根本不是我方的問題。**
   而 189 條之驗證邏輯本身，自第五批起沒有再被人讀出過錯。
   **這是 G-E 所說的「可測範圍到底」之另一個面向**：
   到底之後，找到的東西會從「內容」漂移到「記載」與「上游」。

4. **交付說明現在是唯一對外載體，而它承載的東西比 remarks 更多。**
   28 條留白 ＋ `INTR2.)` ＋ 3 項缺件 ＋ A-UP14 ＋ 覆蓋率讀法 ——
   **它比被刪掉的 143 條 remarks 更完整地說明了「哪裡沒驗」**，
   因為它是**彙整過的**，而 remarks 是散落的。
   **這一點在 49 輪我沒有預見到** —— 當時我建議選丙（依 Comfort 收斂）
   並擔心執行者失去設置理由。現在看：**設置理由確實失去了**（那個顧慮成立），
   **但「哪裡沒驗」反而變清楚了**。兩件事都是真的。

5. **最後一輪最該記的一件事：52 輪那份 Pop Up List 在 repo 裡躺了五十輪。**
   它不是缺件，是**沒人查**。而查它的成本是一行 `find`。
   G-M 立了規則，但規則救不了下一次 ——
   **真正該問的是：為什麼「素材缺」這個狀態，五十輪都沒有人要求它附路徑？**
   G-L 就是答案，而它來得太晚，只能留給下一個 feature 用。
