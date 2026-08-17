# 上繳 11 — R-U46 落地、盲區判讀與 must_carry 追蹤

- 產出層：執行層｜2026-08-17｜對象：分析層
- 下放包：`11a_rulings.md`（R-U46～R-U48、R-G11）＋ `11b_tasks.md`（作業 1–5）
- **本輪未生成任何 TC**（11b 作業 5）。`generated/` 仍為空。

---

## 1. 作業 1 —— 10 輪之上繳已補落檔（R-U48）

`docs/upstream/10_pilot.md` 已寫入，含 11b 要求之五項全部。

**重出方式（逐項具名，非以貼文為據）**：

| 內容 | 重出來源 |
|---|---|
| 六條標記之改動 | 自 `RULINGS.md` 以 `grep -nE "^R-(U3\|U15\|U22\|U36\|G4\|G7) \["` 讀出首行 |
| `git check-ignore` | 重跑，`exit=1`（不被忽略）；`git status --short` 佐證 |
| `shasum -c` | 重跑，**7 行 OK** |
| 自檢六項 | 重跑 `--selfcheck`，全文貼入 |
| **判準改兩次之經過** | 自 `scripts/build_batch_context.py` 之**原始碼註解**轉錄（v1／v2／v3 各記其錯在哪）|
| PLP 三讀法 | 重跑掃描，甲 2／乙 4／聯集 4，命中脈絡逐條附上 |
| 取樣 16 列 | 重跑，理由欄逐列補齊 |

**完整未截斷之 git 指令清單**（見 `10_pilot.md` §2.4，此處複述以免再被截斷）：

```
git add features/user_profiles/.gitignore
git add features/user_profiles/BASELINE.sha256
git add features/user_profiles/data/outline_map.json
```

**三行分列**，不以續行或萬用字元表述 ——
一條被截斷之 `git add` 仍是一條**合法**指令，這正是它危險的地方。
**執行層未執行。**

---

## 2. 作業 2 —— 條文入庫

`RULINGS.md` 新增「第十一輪條文」段：
**R-U46、R-U47、R-U48 逐字**（feature 條文），
**R-G11 逐字**（全域條文，於本包首次落檔，另立小節）。
其後附執行層回報五點。

**自檢**：11a §「本包產生之新條文清單」列 R-U46／R-G11／R-U47／R-U48 四條，
入庫 4 條，**餘數 0**。

---

## 3. 作業 3 —— R-U46 落地

### 3.1 `PLP_ENABLED` 啟用，聯集清單具名

`scripts/build_batch_context.py`：

```python
PLP_ENABLED = True

PLP_LEAVES_AUTO = {          # 甲 ∪ 乙，可由掃描重算得出
    "SWE1-HMI-PROF-001-01",  # 乙：037 Description「listed in PLP table」
    "SWE1-HMI-PROF-005",     # 乙：037 Verification Criteria「In the PLP table」
    "SWE1-HMI-PROF-012",     # 甲∩乙：sec 4.5.4 pdf_text ＋ 037 Description
    "SWE1-HMI-PROF-032",     # 甲∩乙：sec 5.9 pdf_text ＋ 037 Description
}

PLP_LEAVES_MANUAL = {        # 盲區人工判讀，**不併入自動判準**
    "SWE1-HMI-PROF-001-02",  # D-UP11-01
    "SWE1-HMI-PROF-001-03",  # D-UP11-01
}

PLP_LEAVES = PLP_LEAVES_AUTO | PLP_LEAVES_MANUAL   # 6
```

**兩集分列之理由**：R-U46 明文「不併入自動判準」。
若把人工結果混進 `PLP_LEAVES_AUTO`，該集合就不再是
「重跑掃描即可重算得出」之物 —— **下一輪任何人重跑掃描都會發現它對不起來，
而對不起來的原因會被誤讀成掃描壞了。**

併列之內容：`_3.1` ~ `_3.5`（PLP 表五列，內容已於 05 輪自 PDF p5 讀出並存於
`outline_map.json`，非推定）。

### 3.2 盲區掃描 —— 命中 17／未命中 163／**餘數 0**

母體 **180 leaf**。字樣：`above`／`listed above`／`see list …`／`see table …`／
`below`／`table below`（不分大小寫）。

**逐條人工判讀之全表見 `DECISIONS.md` D-UP11-01。** 摘要：

| 判讀 | 條數 | 內容 |
|---|---|---|
| **指向 PLP 表 → 是** | **3** | `PROF-001-01`／`001-02`／`001-03`（皆 sec 4.1，同一句 `PRACC1.`）|
| 指向圖／截圖 | 3 | `014`（4.6.1）／`078`（8.8.2）／`106`（10.2）|
| 指向別的表 | 4 | `090`／`091-01`／`091-02` → Table EDPR1；`111` → Table CPA2 |
| 指向別的流程／前段 | 3 | `047`（6.2）／`066`（8.2）／`134`（14.1）|
| **`above` 為版面方位，非引用** | 3 | `076-01`／`076-02`／`076-03`（"show above the Save & Continue button"）|
| 指向頁內 chart | 1 | `108`（10.3.1）|
| | **17** | |

### 3.2.1 本輪之實質發現 —— **同節之其餘 leaf（具名回報）**

R-U46 裁「**4.1（PRACC1.）之併列 3.x 成立**」。
但 sec 4.1 底下有**三個** leaf，而自動判準（甲∪乙）**只抓到 `001-01`** ——
唯一原因是只有它的 037 Description 字面寫了「PLP table」：

| req_id | 037 Description | 自動判準 |
|---|---|---|
| `001-01` | system shall store all profile-linked preferences **listed in PLP table** | 乙側命中 |
| `001-02` | system shall recall stored preferences when profile is activated | **未命中** |
| `001-03` | If a feature is unavailable …, skip storing & recalling that item | **未命中** |

三者所 store／recall／skip 的那份「preferences」**是同一份**，
就是 `PRACC1.` 指的那張 PLP 表。**併列 3.x 之理由對三條完全相同。**

故 `001-02`／`001-03` 列入 `PLP_LEAVES_MANUAL`。

> 若不列入，會出現一個難以解釋的產物：
> **同一節、同一句 spec、同一份清單，三條 TC 只有一條的
> `specification_reference` 指得到那張表。**

### 3.3 本判準自身之盲區（R-G11，逐項聲明）

| # | 抓不到什麼 | 處置 |
|---|---|---|
| 1 | 完全無指涉字樣而實質引用 PLP（如僅寫 "the preferences"）| **接受漏失**；惟「同節連坐」已補一層 |
| 2 | 圖內文字（PDF 文字層若不含）| 接受漏失 |
| 3 | `above` 之**版面方位**用法 → **偽陽性**（本批 3 條）| 人工濾除，**不改判準** —— 偽陽性可由人工濾，偽陰性不行；本判準寧鬆勿緊 |
| 4 | 中文／其他語言之指涉 | 不適用（spec 為英文）|

**故：本判準之「命中 17」不得被當作「全部引用 PLP 者」之全集。**

### 3.4 自檢 6/6，第 6 項**加了對照向**

原第 6 項之斷言為 `PLP_ENABLED is False` —— 該判準**隨本輪裁定而失效**，
若不改，它會在「已啟用」時紅，且紅的理由與事實相反。改為：

```
ok6 = PLP_ENABLED is True
      and all("_3." in spec_ref(r) for r in 抽樣中屬 PLP_LEAVES 者)
      and not any("_3." in spec_ref(r) for r in 其餘)
```

實測輸出：

```
PASS — 6. R-U46 之 `3.x` 併列 —— **已啟用**，含對照向
    PLP_ENABLED = True
    AUTO 4 ＋ MANUAL 2 = 6
    抽樣中屬 PLP_LEAVES 者：['SWE1-HMI-PROF-001-01', 'SWE1-HMI-PROF-032']
        SWE1-HMI-PROF-001-01: 含 3.x = True
        SWE1-HMI-PROF-032: 含 3.x = True
    對照向 —— 其餘 14 條含 3.x 者：[]（須為空）

6 / 6 self-check items PASS
```

**對照向為 R-G7 之要求**：只驗「該併的併了」，驗不出「不該併的也併了」。

---

## 4. 作業 4 —— R-U47 之追蹤登記

### 4.1 登記處：**`DECISIONS.md`**（D-UP11-02），不記 `DATA_REQUESTS.md`

**理由**：`DATA_REQUESTS.md` 之標的為**須向上游索取之缺件**
（DR #1–#4 皆屬此類）。本項七條之內容**已在本地取得並入表**
（`data/xlsx_missing_clauses.tsv`），缺的只是**本地生成之覆蓋**。
**把已到手的東西登記成待索取，會使 DR 清單失真** —— DR 清單之用途是
「哪些事在等 Pei／上游」，混入自己能辦的事會讓那份清單失去分流作用。

### 4.2 **實測與 R-U47 之前提不符（具名回報）**

R-U47 載「pilot 僅覆蓋三條（9.3.2／9.8／11.4）」。
以 `--selfcheck` 第 2 項實跑 16 leaf 之 `must_carry_for()`，實得：

| outline | 覆蓋之 leaf | 狀態 |
|---|---|---|
| 9.3.2 | `PROF-091-01` | 已覆蓋 |
| 9.8 | `PROF-104` | 已覆蓋 |
| 11.4 | `PROF-111` | 已覆蓋 |
| **11.5** | **`PROF-112-01`** | **已覆蓋 —— R-U47 未計入** |
| 9.1 | — | 未覆蓋 |
| p14 | —（掛回 9.1）| 未覆蓋 |
| p17 | — | 未覆蓋（另有缺陷，見 §4.4）|

**實為「覆蓋 4／未覆蓋 3」，非「覆蓋 3／未覆蓋 4」。**
R-G10 餘數：`4 + 3 = 7` ✓。

**成因推測**：`PROF-112-01`（sec 11.5）是取樣時為了 ch11 之
App Store 行為而選的，其**帶 must_carry 是附帶結果**，
取樣理由欄當時寫的是 App Store 而非 must_carry —— 故清點時漏計。
**這正是 R-G10 之用途**：以「全集減已分類」求餘數，比逐項讀取樣理由可靠。

### 4.3 待追蹤三項（**第一批正式批次前各至少覆蓋一次**）

| # | outline | 內容 | 覆蓋路徑 |
|---|---|---|---|
| T-1 | **9.1** | Resume Tutorials 之圈號 1 與其移除條件 | 生成 sec 9.1 之 leaf 時自動注入 |
| T-2 | **p14** | Table EDPR1 之列項（含 "Stellantis Account" 等五項）| 已掛回 9.1，隨 T-1 一併注入 |
| T-3 | **p17** | Connected Navigation 之列項（同 11.5 之表）| **現況注入不到，見 §4.4** |

### 4.4 新發現之缺陷 —— `p17` 掛不回任何節（**未自行修改**）

`must_carry_for()` 對 `p<N>` 列之掛回條件為：

```python
elif r["outline"].startswith("p"):
    if section in ("9.1", "11.4", "11.5") and r["impact"].find(section) >= 0:
```

- `p14` 之 `impact` = 「**9.1** 之列項順序；05 輪已自 PDF 讀出，xlsx 側無」→ **掛得回去**
- `p17` 之 `impact` = 「**同上**」→ **不含任何節次字樣 → 掛不回任何節**

**即：`p17` 在現行程式下，生成任何節次時皆不會被注入**，
而 R-U35(b) 要求七條 must_carry 皆須注入其所屬 outline。

**`--selfcheck` 第 2 項為何沒紅**：它驗的是「**有注入者是否正確**」，
**沒驗「七條是否都有歸宿」** —— 這是該自檢項自身之盲區（R-G11）。
本輪不逕補該檢查，因為補了就會紅，而紅之後的處置屬判讀（見下）。

**未自行修改之理由**：`p17` 之歸屬節次，07 輪即載明「未逐一定位」；
把它掛到 `11.5` 是**判讀**，依 canon §9.3 不自裁。

**建議之處置（擇一，待裁）**：
1. `p17` 之 `impact` 欄改寫為明含「11.5」——改資料，程式不動；
2. `must_carry_for()` 增一張顯式 `p<N> → section` 對照表 ——
   改程式，**且順帶消除「以 `impact` 之散文字串做掛回鍵」這個脆弱設計**。

**傾向第 2 案**：現行設計把「人看的說明欄」當成「機器用的外鍵」，
`p14` 之所以能掛回去是巧合（它的散文剛好寫了節次），不是設計。

---

## 5. 作業 5 —— 停

作業 1–4 完成，**未生成任何 TC**。`generated/` 為空。
待分析層覆核 `10_pilot.md` 之前置 1–3 與本包產出後，另下生成指令。

---

## 6. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 性質 | 建議 |
|---|---|---|---|
| 1 | **`p17` 注入不到** | **缺陷（已證，非推測）** | 見 §4.4，兩案擇一。**在 sec 11.5 之正式批次生成前必須裁** —— 否則 T-3 之追蹤登記會落空：登記了、也生成了、卻沒注入 |
| 2 | **自檢缺「七條皆有歸宿」之檢查** | 檢查之盲區 | §4.4 之裁定落地時一併補上；補了才會擋住同型問題 |
| 3 | **`10.2`／`10.3.1` 之判讀口徑** | **待裁（非事實爭議）** | 依「指涉所指之物」判為否；若依「語意所涉之內容」則應為是。見 D-UP11-01 §附註 |
| 4 | **同節連坐是否為通則** | 未立條文 | 本輪對 4.1 做了「同節之 leaf 併列理由相同則一併列入」；**這是一個判準，但只在一個案例上用過**。是否升為通則（凡人工判讀成立之節，其全部 leaf 皆入）待裁 —— 現況僅 4.1 一節適用，尚無第二個案例可驗 |
| 5 | **`PLP_LEAVES_AUTO` 之可重算性未設檢查** | 未驗 | 該集合宣稱「重跑掃描即可重算得出」，**但目前無任何自動檢查在守這句話**。建議把甲∪乙之掃描收進 `--selfcheck`，使其成為可重跑之斷言而非註解 |
| 6 | **盲區判準之偽陰性未量測** | **永久限制** | 「完全無指涉字樣而實質引用 PLP」者有多少，無法以任何字串判準量測；只能人工全讀 180 條。本輪未做，**明列為接受漏失** |
| 7 | **`052f67d` 之污染 commit** | 跨輪未決 | 三案已於前輪提出，**至今未裁**。不擋本輪 |
| 8 | A-UP09／R-U14（DV gate）、DR #3／#4、R-U17、N-XF01 | 承前未決 | 不擋本輪 |

---

## 7. 動作清單 —— 與 git 陳述逐項對照（R-G6）

| # | 動作 | 對象 | 是否 git |
|---|---|---|---|
| 1 | **檔案新建** | `docs/upstream/10_pilot.md`（補落檔）| 否 |
| 2 | 檔案新建 | `docs/upstream/11_plp_and_pilot_prep.md`（本檔）| 否 |
| 3 | 檔案追加 | `RULINGS.md`（＋R-U46／47／48／R-G11 逐字＋回報段）| 否 |
| 4 | 檔案追加 | `DECISIONS.md`（＋D-UP11-01、D-UP11-02）| 否 |
| 5 | **檔案編輯** | `scripts/build_batch_context.py`（`PLP_ENABLED = True`、AUTO／MANUAL 分列、docstring、自檢第 6 項加對照向）| 否 |
| 6 | 檔案編輯 | `docs/INDEX.md`（＋第 10／11 輪兩列與第十一輪段）| 否 |
| 7 | 程式執行（唯讀）| `--selfcheck` 重跑、盲區掃描、`shasum -c`、`grep` | 否 |
| 8 | **唯讀** | `git status --short` | **是（唯讀）** |

**未執行任何會改變 repo 狀態之 git**：`add`／`commit`／`push`／`checkout`／
`restore`／`reset`／`stash`／`clean`／`rm`（R-G5）。
**已執行之唯讀 git**：`status` —— 用於確認本輪之改檔面。

**未動**：`generated/`（**未生成任何 TC**）、`framework.md`、`feature.yaml`、
`ANOMALIES.md`、`DATA_REQUESTS.md`、`BASELINE.sha256`、`.gitignore`、
`data/` 之任何檔、`inputs/`、`forms/`、**他 feature 之任何檔**。

### 本輪之改檔，待 Pei 之 git 指令清單（**未執行**）

```
git add features/user_profiles/RULINGS.md
git add features/user_profiles/DECISIONS.md
git add features/user_profiles/docs/INDEX.md
git add features/user_profiles/docs/upstream/10_pilot.md
git add features/user_profiles/docs/upstream/11_plp_and_pilot_prep.md
git add features/user_profiles/scripts/build_batch_context.py
```

（10 輪之三行仍待執行，見 `10_pilot.md` §2.4；
`git status` 顯示 repo 內另有 power／comfort 等他 feature 之未提交改動，
**本輪未觸碰，亦不建議以萬用字元一次 `add`**。）
