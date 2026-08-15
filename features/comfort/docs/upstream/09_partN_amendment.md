# 上繳包 09 — R-C19 ＋ Part N 修正案（四節改置）

執行層 → 分析層。2026-08-15。回應下放包 `14_partN_amendment.md` §5。

**結論：八項作業全部完成。`verify_partn.py` 七項 assertion 以修正後期望值
全數重跑，全 PASS。ch2 == 92、ch16 == 99、總計 == 403 於改置後仍成立。**
`Sign-off` 未重簽。Phase 4 未開始。

---

## 0. 置頂

| # | 事項 |
|---|---|
| **甲** | **五處同步實測一致**：`framework.md`（§2 表、§5 驗算、§6 明細 129 列）、`test_set_map.tsv`、`section_fulltext.tsv` 之 `test_set` 欄、`verify_partn.py` 之 `PART_N`。三個資料檔之 `test_set` 欄逐節比對，129 節**全數相同**，對稱差為零 |
| **乙** | 落實 R-C19 時發現 **`recon.py` 之 Amendment 偵測器有缺口**：其正則不容許 markdown 粗體，故 Comfort 之 `- **Amendment 1（…**` 被計為 0。已修（§5），SXM 之 11 筆無回歸 |

---

## 1. §5.1 R-C19 貼入

`RULINGS.md` 現載 **R-C1 ~ R-C19 + R-C4-1 + R-C5-1**，共 21 條，全部原文照錄。

R-C19 之來源已於該小節標明：源自執行層上繳 08 §1 自加之約束，分析層
**不駁回，升格為條文**。

**這件事對我有一般性的意義，記一句**：我當時把它寫進 `framework.md` 並主動
聲明「非分析層指示，若不同意請駁回」。若我當時只是照做而不聲明，它會以
「framework 裡的一句話」存在，既不會被駁回、也不會被升格 —— **兩種結果都
比現在差**。主動標示越界，比自我審查不寫、或寫了不說，都更有用。

## 2. §5.2 四節改置 —— 五處同步

| 節 | 原 Test Set | 新 Test Set | leaves |
|---|---|---|---|
| `2.16` | Climate Modes | **Temperature and Fan** | 2 |
| `16.17` | ICS Climate Modes | **ICS Temperature and Fan** | 1 |
| `2.14` | Climate Modes | **Front Climate Anatomy** | 4 |
| `16.14` | ICS Climate Modes | **ICS Anatomy** | 3 |

### 2.1 五處同步之實測

| 處 | 狀態 |
|---|---|
| `scripts/verify_partn.py` 之 `PART_N` | 六組之 section 清單與 declared leaves 皆改為 14 §1.3 之新值 |
| `data/test_set_map.tsv` | 由 `verify_partn.py` 重生（129 列） |
| `data/section_fulltext.tsv` 之 `test_set` 欄 | 由 `build_section_fulltext.py` 重生（讀 `test_set_map.tsv`） |
| `framework.md` §2 表 | 六列改數，另加修正案註記 |
| `framework.md` §6 明細 | 由 `test_set_map.tsv` 重生 —— **129 列／403 leaves／15 組**，與該檔對稱差為零 |

**四節於三檔之一致性逐節實測**：

```
節      應為                       test_set_map              section_fulltext
2.16    Temperature and Fan        Temperature and Fan       Temperature and Fan       ✅
16.17   ICS Temperature and Fan    ICS Temperature and Fan   ICS Temperature and Fan   ✅
2.14    Front Climate Anatomy      Front Climate Anatomy     Front Climate Anatomy     ✅
16.14   ICS Anatomy                ICS Anatomy               ICS Anatomy               ✅

全量比對：test_set_map vs section_fulltext 之 129 節 test_set 欄不一致者 —— 無
```

`framework.md` §6 明細**不是手抄**，由 `test_set_map.tsv` 程式生成後貼入，
故第五處與第二處在構造上不可能分歧。

## 3. §5.3 七項 assertion 全數重跑

期望值改為 14 §1.3 之新數字並**寫死於腳本**（`PART_N` 之 section 清單與
declared leaves 皆為轉錄值，不由 `layer3_map.tsv` 回推）。

```
- PASS — each Test Set's leaf_count matches handoff 14 §1.3 (amended):
    expected `all 15 equal`, measured `all 15 equal`
- PASS — Test Set leaf totals sum to 403: expected 403, measured 403
    — Front Climate Anatomy:16、Climate Modes:35、Temperature and Fan:19、
      Airflow and Defrost:23、Tri-Mode Climate:14、Rear Climate:46、
      ECO HVAC:15、Heated Vented Seats:59、Seat Control Tab:14、
      Climate Popups:42、ICS Anatomy:17、ICS Climate Modes:36、
      ICS Temperature and Fan:17、ICS Airflow and Defrost:29、
      Home Screen Widget:21
- PASS — all 129 mapped sections assigned: expected 129, measured 129
    — unassigned: none; not in layer3_map: none
- PASS — no section assigned to two Test Sets: expected {}, measured {}
- PASS — per-chapter round-trip (ch2==92, ch16==99, +12 others):
    expected `all 14 chapters equal`, measured `all 14 chapters equal`
    — 2:92、3:14、6:1、7:38、9:8、10:15、11:37、12:22、13:14、14:40、
      15:2、16:99、17:18、18:3
- PASS — Test Set names: no Misc/General/Unclassified, no stray whitespace,
    no duplicates: expected [], measured [] — 15 names checked
- PASS — no Test Set name starts with the Test Group word (§4.2):
    expected [], measured [] — 15 names checked against prefix 'Comfort'
```

`Test Sets: 15; leaf range 14–59; largest = 14.6%` —— 區間與 14 §1.3 所載
之 14–59 相符（原為 12–59，因 #1 由 12 升至 16、最小者改為 #5／#9 之 14）。

### 3.1 指示特別要求之三項

| 驗算 | 修正前 | 修正後 | 結果 |
|---|---|---|---|
| ch2 | 92 | **92** | 不變 ✅ |
| ch16 | 99 | **99** | 不變 ✅ |
| 總計 | 403 | **403** | 不變 ✅ |

**為何必須不變**：四節改置只在既有 Test Set 之間移動，未新增或刪除任何
section。三者若有任一改變，即代表改置過程漏掉或重複了某節 —— 這正是第 2、
5 項 assertion 存在的理由。已於 `framework.md` §5 明記此推理，使日後讀者
知道那兩項不是例行檢查而是本次修正案的守門員。

`build_section_fulltext.py` 之四項亦重跑全 PASS（129 列、無截斷殘留、
5 列短於 60 字者逐列確認、outline 集合相等）。

## 4. §5.4 `framework.md` 增記

- **新增 §3.5「2026-08-15 修正案 —— 四節改置」**，含四個子節：
  §3.5.1（`2.16`／`16.17`，附截斷值與全文之並排對照）、
  §3.5.2（`2.14`／`16.14`，含 14 §1.2 之 MTC 引文與「非截斷所致，係原始分類
  錯誤」之如實記載）、§3.5.3 修正前後對照表與驗算、§3.5.4 附帶觀察。
- **新增 §3.6「刻意不動之一處」**：`2.6.1`／`2.11`（及 ICS 側之
  `16.6.1`／`16.11`）之重疊與其不改置之理由，加 Phase 4 之 sibling 判定指示。
- **§3.1.1 末之自加約束段已改為指向 R-C19**，並註明其升格經過。
- §2 表加修正案註記；§5 驗算區塊全面更新。
- **節次順序已修正**：§3.5／§3.6 一度插到 §3.4 之前，已重排為
  3.1 → 3.1.1 → 3.2 → 3.3 → 3.4 → 3.5 → 3.6。

## 5. §5.5 `DECISIONS.md` §6 增記，Sign-off 未重簽

§6 之 Part N 條目下新增三個子項：修正案 1（13 §2 更名）、修正案 2
（14 §1 四節改置）、以及「Sign-off 不重簽」之理由與執行層之覆核結論。
**既有之 `[SIGNED 2026-08-14]` 行逐字保留**，修正案以子項附加。

**執行層對「不重簽」之覆核：同意。** Part N 之結構未變 —— 組數（15）、
名稱邊界、母體（403／129）與逐章數（ch2 92／ch16 99）皆同，變更限於四節之
組間歸屬與一處命名。14 §5 要求「若執行層認為此判斷有誤，回報，不自行重簽」；
我認為無誤，亦未重簽。

### 5.1 乙：`recon.py` 之 Amendment 偵測缺口（本輪發現並修正）

本檔表頭原則為「簽署後之異動一律追記於文末 **Amendment**」，故我同時於
Amendment 區建立兩案之索引。建完後以 `read_signoff()` 複測，發現：

```
R-C9 偵測器: {'signed': True, 'reviewed_by': 'PeiPYHsu', 'amendments': 0}
                                                          ^^^^^^^^^^^^^ 應為 2
```

**成因**：`read_signoff()` 之正則為 `^\s*-\s*Amendment\b`，而 Comfort 寫作
`- **Amendment 1（…**`，粗體標記使其不匹配。SXM 寫作
`- Amendment (2026-08-11, seventh pass):` 為純文字，故一直正常。

**影響範圍**：R-C10 明載 Sign-off 欄位與 Amendment 條目「兩者擇一即可」。
對 Comfort 無實害（`Reviewed by` 已填，`signed` 仍為 True），但**對一個
只有 Amendment 形態、且採用粗體記法之 feature，偵測器會判其未簽署** ——
那正是 R-C9／R-C10 要防的情形。

**修正**：正則改為 `^\s*[-*]\s*[*_~`]*\s*Amendment\b`（容許 `-`／`*` 項目
符號與 markdown 強調標記，並加 `re.I`）。

**回歸實測**（唯讀掃描，**未重跑任何既有 feature 之 recon**，R-C8）：

| feature | signed | reviewed_by | amend |
|---|---|---|---|
| home | False | — | 0 |
| amfm | True | PeiPYHsu | 0 |
| **sxm** | True | PeiPYHsu | **11**（修正前後相同，無回歸） |
| projection | False | — | 0 |
| privacy | False | — | 0 |
| **comfort** | True | PeiPYHsu | **2**（修正前為 0） |

## 6. §5.6 §2 之 Phase 4 註記已寫入 `RUNBOOK.md`

`2.6.1`／`2.11`（及 `16.6.1`／`16.11`）須一併閱讀對造節、依 §4.6 作 sibling
判定、必要時輸出 `duplicate_of`，若顯示確不應分置則回分析層重簽 —— 已列為
Phase 4 前置待辦。R-C19 亦一併列入。

## 7. §5.7 Phase 4 未開始

未產 TC、未指派 tc_id、未做 sibling 判定、未寫 profile `[OVERRIDE]`。
profile 草案待下放包 15。

---

## 8. 本包是否仍有該驗而未驗者 —— 獨立判斷

### 8.1 已驗

1. `verify_partn.py` 七項以修正後期望值全 PASS；ch2／ch16／總計三者不變。
2. 四節於 `test_set_map.tsv` 與 `section_fulltext.tsv` 之新歸屬，並全量
   比對 129 節之 `test_set` 欄（對稱差為零）。
3. `framework.md` §6 明細重生後 129 列／403 leaves／15 組，與
   `test_set_map.tsv` 對稱差為零。
4. `framework.md` §3 之節次順序（一度錯置，已修）。
5. `build_section_fulltext.py` 四項全 PASS。
6. `read_signoff()` 修正後之全 feature 掃描，SXM 無回歸。

### 8.2 該驗而未驗

| # | 未驗事項 | 為何 | 風險 |
|---|---|---|---|
| 1 | **其餘 12 章之章內歸屬** | 14 §1 之複核限於 ch2／ch16；其餘 11 組為整章對應，章別來自 export 之 `chapter_title`（非截斷欄位），依 14 §1 不在複核範圍 | 低 —— 但 `Rear Climate`（#6，跨 ch7＋ch9）與 `Climate Popups`（#10，跨 ch14＋ch15）是**兩個跨章組**，其合併理由是否也曾以截斷欄位為輸入，本包未查 |
| 2 | **`2.6.1`／`2.11` 之重疊程度** | 14 §2 裁定不改置，只要求 Phase 4 作 sibling 判定 | 中 —— 已列 RUNBOOK；若 pilot 顯示應合併，屬 Part N 變更 |
| 3 | **`Climate Modes` 35 leaves 之內聚性** | 13 §6 暫不處置，材料（全文）已備 | 低 |
| 4 | profile `[OVERRIDE]`、DR #6、DR #11 | 下放包 15／待 Pei 指認 | 中／低 |

**第 1 項值得分析層看一眼**：14 §1 之複核範圍界定為「11 組為整章對應，
章別來自非截斷欄位，不在複核範圍」。該界定對**單章組**成立，但 #6
（ch7 + ch9）與 #10（ch14 + ch15）是把**兩章併為一組**的決定，那個決定
不是「整章對應」而是跨章合併，其依據是否曾以截斷標題為輸入，我無從得知
（該決定作於 11 §2，我未參與）。若分析層確認該兩組之合併依據為章標題
（非截斷欄位），本項即可關閉。

### 8.3 未做、亦未偷做者

- **未自行改置任何 section**；四節改置全依 14 §1 之指定。
- **未重簽 Sign-off**（14 §5 明文；覆核後同意不重簽）。
- 未改 Test Set 之數量、名稱或邊界。
- 未對 §3.6 之 `2.6.1`／`2.11` 作任何改置或 sibling 判定。
- 未產 TC、未指派 tc_id、未寫 profile。
- 未重跑任何既有 feature 之 recon（R-C8）；對其目錄零寫入。
- 未執行任何 git 操作。

### 8.4 執行層對「本包可否結案」之判斷

**可結案。** 四節改置已五處同步且以全量比對證明一致；七項 assertion 以
修正後期望值全 PASS，指示特別要求之三項驗算（ch2／ch16／總計）確認不變；
R-C19 已落地；Sign-off 依裁定未重簽。

**Phase 4 之硬前置仍為 profile `[OVERRIDE]`**（含 A-CF07 之寫回處置明文），
草案待下放包 15。§8.2 第 1 項若分析層認為需查，請明示 —— 那是 11 §2 之
決定，我不預設可由執行層回溯判定其依據。
