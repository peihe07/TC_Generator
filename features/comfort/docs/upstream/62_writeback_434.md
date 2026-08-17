# 62 — Comfort HMI / 台帳之修復、ENTRY 026（434 列）、RD-1 三問全文

- 產出層：執行層｜2026-08-17｜對象：分析層
- 覆核對象：`docs/handoff/82_ledger_and_writeback.md`
- **lint 54 / 54 PASS，0 finding across 434 TCs；assertion 14 / 14 PASS**

---

## 0. 供覆核之全文（82 §4）

以下四段為**逐字引出**，未節錄、未改寫。

### 0.1 RD-1 第 2 問

## 2. Why is the five-mode airflow requirement marked out of scope, and what decides the airflow-mode set here?

**Units blocked**: 9 — `SWE1-HVAC-016-01` … `-03` (section 2.12),
`SWE1-HVAC-018-01` … `-06` (section 2.12.2)

**The sentences**:

> C13.) **There are 4 Airflow Mode** displayed in this order (1) Face,
> (2) Face plus Feet, (3) Feet, (4) Feet plus Windshield.
>
> C13.0) **In some non-tri mode equipment types**, airflow modes has 5 states…

**What we found since the last version of this question**: the vehicle-controls
specification does state a condition for the five-mode set —

> The requirements in the section 'Defrost Softkey' shall be implemented if
> PROXI parameter `$VC_VEH_LINE$ = [637MCA]` OR `$Country_Code$ = [LATAM
> related countries]` then HU shall display the **5 airflow modes combination**
> according to the HMI specifications.

but in the export scoped to this vehicle line, all four rows carrying that
sentence have **Scope = None** and **Radio = R1M, R1H** — that is, they are
marked as not applying here. The four-mode set (C13) still carries no condition
of its own anywhere we have looked.

**What is missing**: two things, and the second matters more.

- Why those rows are marked out of scope for this vehicle line.
- **What does decide the airflow-mode set on the vehicles in this programme.**
  Marking the five-mode requirement out of scope does not by itself say the
  four-mode set applies — it says that one requirement is not ours. We would be
  inferring the rest.

**What we have done**: the 5-state set (2.12.1) and the tri-mode set (3.1) are
tested. The four-mode set and the hard-control cycle that depends on it are not.

**Once answered**: nine test cases are written, with the deciding configuration
stated as a pre-condition.

---

---

### 0.2 RD-1 第 3 問

## 3. Which PDO release carries the vehicle-specific recirculation and seat icons?

**Units blocked**: 3 — `SWE1-HVAC-006-04` (2.5), `SWE1-HVAC-099` (14.15),
`SWE1-HVAC-122-02` (16.16)

**The sentences**:

> C4.) The recirc icon will display the vehicle model specific icon **as
> displayed in the table**.
>
> HVACSB1.) Available comfort controls (driver/passenger heated/vented seats,
> seat zones and heated wheel) **depend on vehicle configuration**.
>
> ICE15.) Off icon of seats will depend on system configuration
> **(see Climate section)**.

**What is missing**: the mapping from configuration to icon. The HMI Read Me
names the owner — "All graphics are place holders. **See PDO release** for
official graphics, animations, and layout" — so the question is now narrower:
**which PDO release carries these icons, and how do we obtain it?** The PDO
material available to us is a release cover sheet naming the receiving
organisation; it contains no icon table.

**What we have done**: no test case asserts which icon appears. Where a clause
has other content, that content is tested (the recirculation button's on/off
behaviour is covered; only the icon is not).

**Once answered**: three test cases are written, quoting the mapping for the
configuration under test.

---

---

### 0.3 RD-1 第 8 問（新增）

## 8. Does a document named "HMI Notes" exist for this programme?

**Units blocked**: 1 — `SWE1-HVAC-072` (section 12.6)

**The sentences** — two chapters, one word apart:

> 11.5 HVS6. Refer to the **HMI Settings List** for the details on the Auto
> Comfort Settings options for heated/vented seats.
>
> 12.6 HVS6. Refer to the **HMI Notes** for the details on the Auto Comfort
> Settings options for heated/vented seats.

**What is missing**: the HMI Settings List exists and carries those options, so
section 11.5 is now tested. **No document named "HMI Notes" exists in the
material available to us.** The nearest candidate, the HMI Read Me, is a
conventions document — format key, acronyms, display anatomy — and contains
nothing about Auto Comfort Settings.

So the question is one of identity: **is "HMI Notes" another name for a
document that exists, is it a document we have not been given, or is the
reference an error for the HMI Settings List named one chapter earlier?**

**What we have done**: section 12.6 is delivered as a row that states the
owning document and records that no test case in this delivery covers it. We
have not assumed it means the same thing as 11.5 — the two chapters name two
different documents, and only one of them turned out to exist.

**Once answered**: if the document exists, one test case is written from it. If
the reference is an error, the row is replaced by one that mirrors 11.5.

---

---

### 0.4 交付說明之「兩個單位有列但未全測」段

> Two further units have a row that does not fully test them: one is tested on
> one side only (described after the table), and one is a row that names its
> owning document and carries no procedure (listed further down). The question
> document counts **22 units with an open question**; this note counts **20 units
> with no test case**. Both numbers are stated with what they count, and those
> two units are the difference between them.

---

## 1. ENTRY 023 之 FAILED —— 先驗內容，再登記，不改原記錄

### 1.1 內容複驗（逐格，唯讀）

| 項 | 實測 |
|---|---|
| row 10–438 × 14 個寫入欄 | 與 `generated/*.json` 逐格比對，**不符 0 格**，惟 `NR1L-ComfortHMI-382` 之 **L／M／N／P／AH 五欄**不同 |
| 該五欄之成因 | **本輪 R-C45 解封所改**（81 §2.3）—— 差異來自語料前進，**不是來自重存** |
| 其餘 | row 439 起無殘留；zip member 48；DV `P10:Q601`／`T10:Z601`／`AF10:AF601`；B 欄公式 row 10 與 438 皆在 |

**結論：Excel 重存改變了位元組而未改變內容。**
上繳 58 §7 說「內容未變」時那是**判讀**（比對當時之 JSON）；
此處是**實測**，且把唯一一處差異的成因指名為我方自己的改動。

### 1.2 台帳之三項動作

1. **ENTRY 023 不改**（append-only），其內文**增註**一段：其對象已被重存，
   原位元組 `c37e572f…` **已不存在於磁碟**（重存是就地覆寫，沒有留下前一份），
   後續由 ENTRY 024／025 承接
2. **ENTRY 025 新登**（`type: verified + archived`）：記 §1.1 之逐格實測與歸檔
3. 該檔移入 `output/archive/`，其於**新路徑**之 checksum 行加入文末段落

**`shasum -c --ignore-missing`：48 OK / 0 FAILED**（前為 46 OK / 1 FAILED）。

### 1.3 一件必須講明白的事

ENTRY 023 那一列**自此永遠無法驗證** —— 它記的位元組不在任何地方了。
`--ignore-missing` 會**靜靜跳過**它，所以增註寫在 **ENTRY 023 的內文裡**，
讓讀者在讀到那一列時就看見，而不是在別處。

**R-C14 之情形在此真的發生了**：一個被記錄之身分失去了它的物。
台帳因此永久帶一筆無法驗證之列 —— **那正是它該有的樣子；
把它抹掉才是把事情藏起來。**

---

## 2. ENTRY 026 —— 434 列，assertion 14 / 14 PASS

- 產出：**`…_Comfort_20260816_extdocs.xlsx`**
  SHA256 `0366315926ed9eef016dac9d80112cb785316eff7de0fc876e2b2a252bb02ab7`
- 來源：ENTRY 022 之擴充後母本（`6d53056e…`），未動
- row 10–443，**434 列**；48 zip members，僅 `sheet6.xml` 差異
- 前置 gate 6 項全 PASS（DELIVERY **46 OK 0 FAILED**、lint 54/54 across 434 TCs、
  tc_id 001–434 連續無缺號）
- **§3.3 assertion 14 項全數 PASS**

**新檔名而非覆寫**：舊路徑上是 Pei 重存過的那一份，覆寫它等於銷毀
ENTRY 024 之對象。**marker 列自 5 減為 4**（`-382` 已解封）。

**狀態：未經 Excel 確認**，待 Pei 之四項（無修復提示／R 欄下拉九項可用／
D5 Scope 正確／row 10–443 內容與編號正確）。**產出後停下。**

---

## 3. 計數同步

| 檔 | 數 |
|---|---|
| 交付說明 | **434 test cases covering 383 of the 403** / **20 units with no test case** / marker 列 **四**條 |
| RD-1 | **383 of the 403**（95.0%）/ **22 units with an open question**（其中 20 條無任何列）|
| `output/STATUS.md` | 增三列（023 之現況、024／025 之歸檔、026）|
| `docs/INDEX.md` | 台帳摘要改述至 026 |

**22 與 20 之差為二**：`047`（AUTO 之不可用側未測）與 `072`（12.6 之 marker 列）。
兩者**都有列**，故不計入「無任何列」之 20；**都未被完整驗證**，故計入 22。

---

## 4. 未做

- 未複製至客戶交付路徑；未移除交付夾任何檔案（SR25 兩檔與 Device Manager 留置）
- 未動 prepared 檔與 ext 母本；未改 ENTRY 001–025 之記錄內容
- 未搬任何檔案至 `inputs/`；未改 `BASELINE.sha256`
- **git 未執行**

## 5. 待裁定

1. RD-1 之新版（含本包 §0 之三問）是否可送 —— 送達仍為 Tier 3
2. 交付說明之 §0.4 段措辭
3. 交付之前置：四項中前三項已備，**餘 Pei 之 Excel 四項確認**，
   其對象為 `…_20260816_extdocs.xlsx`（`03663159…`）

---

## 6. profile 與 RUNBOOK（82 §5）

### 6.1 profile §3.2.4 —— `[ext-verbatim]` 之定義

新增一節，載其格式、**三項適用條件**（已列 §1.1／所引為版本無關之事實／
spec_ref 另列），以及「何以另立一類」之理由。並記現行用例
（`-430`～`-433` 引 CFTS043 `$Rear_HVAC_cfg$ = [Present]`）。

### 6.2 RUNBOOK 兩則

**「以『當下規模』寫下的數字，兩個方向都會壞」** —— `>= 20` 之本意是
「不要掃到空集合」，那句話寫成 `>= 1` 就好；`20` 是把當日之規模誤當成了性質。
R-C43 講語料增加時失效，本則補其另一面：**語料改善時同樣失效。**

**「以形態辨識身分，形態會撞」** —— 並記其與 R-C43 之關係：
**範圍式界定以「位置」冒充身分，形態式辨識以「長相」冒充身分；
兩者都在該有身分的地方放了一個相關但不等價的東西。**
且記其處置是改呼叫端而非放寬 gate —— 那道 gate 要防的事是真的。

---

## 7. 一項須明講之保留（82 §2）

下放包寫「**不得以 `--ignore-missing` 或放寬 gate 繞過**」。**本層未放寬任何 gate**：
FAILED 之解除是靠 §1 之補登（歸檔 ＋ 新路徑之 checksum 行），
`write_back.py` 之該道 gate 一字未改。

**惟須明講**：該 gate 之既有寫法**本來就是** `shasum -c --ignore-missing`
（自 ENTRY 004 起如此），而 ENTRY 023 之列如今**正是一個 missing** ——
它被跳過，不是被驗過。**故那道 gate 現在之 46 → 48 OK，其中不含 ENTRY 023。**

本層未動它，因為改動它是分析層之裁量；但**若不講，「0 FAILED」會被讀成
「每一列都驗過了」**。§1.3 之增註即為此而寫在 ENTRY 023 之內文裡。
