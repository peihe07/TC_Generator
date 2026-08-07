# Stage 0 — Intake 分析：生成前的資料準備診斷

撰寫日期：2026-08-07
定位：`docs/plans/TCGEN_INTEGRATION_PLAN.md` 的前置工作項 **W0**（在 Sprint 1 之前或並行）
需求來源：每接一個新文件（新 RD / 新 spec / 新 workbook），先丟
**原始需求文件 + SWE1 報告**進來，由工具分析後回答一個問題——
**「這個案子開工前，我還需要準備哪些 data？」**

---

## 1. 為什麼要有這個階段

FW036 這輪在真正生成之前，花了一整段「background analysis」人工發現了這些事：

| 當初人工發現的事實 | 若沒發現的後果 |
|---|---|
| Media HMI PDF 是掃描件、零可抽取文字 | 生成器拿到空 context 空轉 |
| SYS1 的 Outline Number 就是 037 引用的 section 編號（158/158 對得上） | 沒有這個 join key，spec 文字全靠相似度亂配 |
| Design Method 必須是 workbook 下拉選單的 9 個字串（精確匹配） | 整批 TC 寫回後下拉欄位全部非法 |
| ch23（Media Widget，25 leaves）在 framework 裡沒有家 | 生成器被迫發明 Test Set，違反 §4.1 |
| Browse Tab 在 done region 只有 1 個 exemplar，卻要撐 83 個 leaf | 風格錨定失效，83 個 leaf 品質不穩 |
| spec 文字大量引用 PUxxxx，需要 Pop Up List 才解得開 | PU0996 缺漏（A-009）這類問題到生成中途才爆 |
| 037 沒有為每個 SYS1 sub-section 配 leaf（A-001，10 個 parent 受影響） | 10 個 parent 在沒有可測內容下生成 |
| rows 10-332 是合規的人工區、333+ 是要丟掉的 placeholder | 保護區邊界劃錯，覆寫了不該動的東西 |

這些全部是**開工前就能檢查出來**的，但這次是邊做邊撞。Stage 0 的目標是
把這段人工偵察變成一個可重複執行的診斷：丟兩份文件進來，
產出一份「資料準備清單」，每項標明缺什麼、為什麼需要、不補會發生什麼。

---

## 2. 輸入與輸出

### 輸入（最少兩份，可多給）

| 輸入 | 必要性 | 例（FW036） |
|---|---|---|
| SWE1 分析報告（037 型 workbook） | 必要 | `FM-WI-FSM-037-...-SWE1-Media-HMI-V0.1.xlsx` |
| 原始需求文件（spec） | 必要 | `Media HMI Logic and Flow ... .pdf` |
| 目標 TC workbook（036 型） | 建議 | `FM-WI-FSM-036-...-MediaHMI.xlsx` |
| 其他已有的輔助文件 | 有就給 | SYS1 export、Pop Up List、Core HMI… |

### 輸出

1. **`intake_report.md`** —— 人讀的診斷報告（給 Pei 與 reviewer）
2. **`intake_report.json`** —— 機器讀的同構資料（之後餵 project profile 草稿）
3. **資料準備清單** —— 報告的核心段，每項一個狀態：

| 狀態 | 意義 |
|---|---|
| `READY` | 已具備，附證據（如「158/158 section 可解析」） |
| `MISSING` | 缺，**開工前必須補**，附「要去哪裡拿 / 找誰要」的提示 |
| `DEGRADED` | 有但不夠好（如 exemplar 太少），可開工但要標注風險 |
| `DECISION` | 不是 data 是裁決——需要人先拍板（如 framework 缺 Test Set） |

---

## 3. 檢查項設計

分兩層。**Tier 1 全部是程式化探測**，不花 LLM 一毛錢、確定性、可重複；
**Tier 2 是 LLM 輔助掃描**，處理程式抓不到的語意問題，可選跑。

### Tier 1 — 程式化探測（八項）

#### C1 · Spec 可抽取性探測
逐頁檢查 PDF/docx 的 text layer。輸出三態：全文字 / 混合 / 純掃描。
- 純掃描 → 清單加一條 `MISSING: 需要一份含 section 文字的替代來源`
  （FW036 的答案是 SYS1 Polarion export），並標注「圖像管線（W8）將是必要依賴」
- 有文字 → 記錄可直接走 `spec_parser` 的哪條路徑

#### C2 · Section join key 檢查（最重要的一項）
從 SWE1 報告抽出每個 leaf 引用的 section 編號（SourceID / HMI Source 欄），
對 spec（或替代來源）的 outline 逐一解析。輸出**解析率**：
- `158/158 → READY`；`151/158 → DEGRADED`，逐條列出解析失敗的 leaf
  （每一條未解析 leaf 就是一個未來的 A-00x）
- 完全對不上 → `MISSING: 需要帶 outline number 的 spec export`，
  並提示 fallback 是相似度比對（品質降級要先知情）

#### C3 · Orphan section 偵測（A-001 一般化）
spec 有、但 SWE1 沒配 leaf 的 section，分兩類：
- **descendant orphan**（掛在某 leaf section 底下）→ 會被 context builder 自動拉進來，
  列出受影響 parent 供 reviewer 加強審查（FW036：10 個 parent、20 個 orphan section）
- **top-level orphan**（沒有任何 leaf 覆蓋的整章節）→ 潛在 coverage gap，
  進 `DECISION`：要不要請 RD 補 leaf（對應 FW036 的 P-6）

#### C4 · 外部參照掃描
對 spec 全文跑 RefResolver 的 pattern 集（`PU\d{3,4}`、CAN signal、
`see <其他 spec 名>`、Table X.Y 引用）：
- 每類參照輸出：出現次數、去重 id 清單、**對應的來源文件是否已提供**
- Pop Up List 已提供 → 進一步逐 id 解析，**查無的 id 現在就列出來**
  （A-009 的 PU0996 在這一步就會現形，而不是生成到 COM-051 才發現）
- 未提供 → `MISSING: 偵測到 47 個 PU 參照，需要 Pop Up List`
- 引用其他 spec（如 Media 引用 Menu Bar HMI）→ 標注 §8.4.2 scope 邊界：
  該文件是「背景」不是「本案 scope」，但沒有它 reviewer 無法判斷 scope fabrication

#### C5 · 目標 workbook 形狀探測（有給 036 型檔案才跑）
- 找 dropdown 定義 sheet，抽出合法字串集（Design Method 9 個、Priority）
  → 直接生成 LintConfig 的素材
- 偵測「已完成區 vs 待生成區」邊界：連續列的欄位完整度 + Procedure 是否為
  placeholder（FW036 的訊號是 `Procedure = "Test"`）→ 建議 protected_rows,
  **但邊界一律要人確認**，報告只給證據與建議值
- 欄位對映探測（表頭 → column map 草稿）
- 輸出可直接當 **project profile（W4）草稿**

#### C6 · Framework 適配檢查
SWE1 的章節 / capability 對 `framework.md`（或 workbook Framework sheet）逐章比對：
- 每章 → 命中的 Test Set，或 `DECISION: 第 23 章 25 個 leaf 沒有家，
  開工前要嘛映射到現有 Set、要嘛更新 framework`（FW036 的 Media Widget 裁決）
- 順帶檢查 §4.1 反模式：某 Set 若將承接 >50 parent 或 <2 parent，提示重切

#### C7 · Exemplar 供給檢查（有 done region 才跑）
每個將要用到的 Test Set：done region 裡有幾個 exemplar、將承接幾個 leaf。
- 比例失衡（如 Browse Tab 1:83）→ `DEGRADED`，建議：先 pilot 一個 parent、
  人工審過後升為 curated anchor（正是 FW036 後來對 COM-057 做的事）
- 全新 Set → 標注 fallback 建議與「首個 parent 加強審查」

#### C8 · 規模與成本預估
leaf 數、parent 數、預估 TC 數（用歷史比率，FW036 是 1.7 TC/leaf）、
預估 token / 成本 / 時程（接既有 `budget_planner`）、建議的 pilot 範圍與
model 分派草稿（哪些章 exemplar 強可用便宜模型——判斷依據來自 C7）。

### Tier 2 — LLM 輔助掃描（可選，逐項開關）

| 掃描 | 抓什麼 | FW036 對應 |
|---|---|---|
| S1 · 需求品質抽樣 | 抽 N 個 leaf 判斷：委託式需求（內容全在引用裡）、規格內部矛盾的癥兆 | A-011（BT1.1.1 vs BT1.1.2）、A-012 這類問題的早期訊號 |
| S2 · 術語一致性 | 同一物件多個名稱（popup 容器命名漂移） | A-021（All Presets Pop up vs Presets Pop Up） |
| S3 · Scope 邊界掃描 | 引用外部 spec 的 Req，標注哪些行為屬於外部 owner | §8.4.2 的事前版 |

Tier 2 的輸出一律進報告的「風險提示」段，**不擋開工**——它是抽樣不是普查，
存在誤報；它的價值是讓 RD-1 問題單在第一天就有草稿，而不是第 N 天才開始累積。

---

## 4. 報告樣貌（節錄示意）

```markdown
# Intake 分析報告 — <project>
輸入：037 v0.1（262 leaves / 159 parents）+ Media HMI PDF（44 頁）

## 資料準備清單
| # | 項目 | 狀態 | 說明 / 行動 |
|---|---|---|---|
| 1 | Spec 文字來源 | MISSING | PDF 為純掃描件（44/44 頁無 text layer）。
|   |            |         | 需要 Polarion/SYS1 export；拿到後重跑 C2 |
| 2 | Section join | (待 #1) | — |
| 3 | Pop Up List  | MISSING | 偵測到 PU 參照 47 個（去重）。需要 Pop Up List xlsx |
| 4 | Framework    | DECISION | ch18、ch23 無對應 Test Set，開工前需裁決 |
| 5 | Dropdown 字串 | READY   | 已抽出 9 個 Design Method 字串 → lint 素材 |
| 6 | 保護區邊界   | DECISION | 證據指向 rows 10-332（詳附錄 B），請確認 |
| 7 | Exemplars    | DEGRADED | Browse Tab 1 exemplar : 83 leaves。建議 pilot 後設 anchor |

## 規模預估
262 leaves → 預估 ~420–480 TC；建議 pilot：PLA-062~068（7 parents）

## 風險提示（Tier 2 抽樣）
- BT1.1.x 群組疑似內部矛盾（抽樣 3/20 命中）→ 建議進 RD-1 問題單
```

判讀規則很簡單：**清單上還有 `MISSING` 或 `DECISION`，就不按生成鍵。**
補一項、重跑一次 intake（幾秒級），直到全綠或明知風險地接受 `DEGRADED`。

---

## 5. 實作切法

```python
# backend/intake.py
@dataclass
class CheckResult:
    check_id: str            # "C2"
    status: Literal["READY", "MISSING", "DEGRADED", "DECISION"]
    summary: str             # one line for the checklist table
    evidence: dict           # machine-readable detail (rates, id lists, page numbers)
    action: str              # what to prepare / who decides

def run_intake(swe1: Path, spec: Path, *, workbook: Path | None = None,
               aux_docs: list[Path] = (), llm_scans: set[str] = frozenset(),
               ) -> IntakeReport
```

- CLI：`python backend/main.py --intake --swe1 <037> --spec <pdf> [--workbook <036>] [--aux <files...>]`
- 前端：upload 之後、configure 之前插一個 Intake 頁，渲染清單表；
  `MISSING`/`DECISION` 未清空前 generate 按鈕 disabled（可 override，需填理由——
  理由進 job metadata，稽核可查）
- 各 check 独立 function、獨立測試；掛新 RefResolver = C4 自動多一類掃描
- **與 plan 的相依**：C1/C2/C3 會用到 W5（context_builder）的 section 解析與
  W8（OCR 索引）的部分能力——實作順序上把「解析 section 編號」這塊抽成
  兩者共用的底層（`spec_outline.py`），W0 與 W5 都站在它上面，不重複寫

### 排程建議

Intake 是**新專案的第一道閘門**，價值最高、依賴最少（Tier 1 不需要 LLM、
不需要 provider 改動）。建議插在 **Sprint 1 與 Sprint 2 之間**（W0，約 3–4 天）：
- Sprint 1 的 W1/W2 給它 dropdown/lint 素材的落點
- 它產出的 profile 草稿正好接 Sprint 2 的 W4
- Tier 2 可延後到 Sprint 3 之後，不擋主線

---

## 6. 驗收

**用 FW036 當黃金案例反向驗證**：把 037 + Media HMI PDF（+ 036 workbook +
Pop Up List）丟進 intake，報告必須自動重現當初人工發現的全部八件事：

| 檢查 | 必須出現的結論 |
|---|---|
| C1 | 44/44 頁純掃描 → 需替代文字來源 |
| C2 | 給 SYS1 後：158/158 解析（與 RUNBOOK 記錄一致） |
| C3 | 10 個受 A-001 影響的 parent、20 個 orphan descendant |
| C4 | PU0996 查無（A-009 早期現形）；引用 Core HMI 的 scope 標注 |
| C5 | 9 個 Design Method 字串；保護區證據指向 rows 10-332 |
| C6 | ch18 / ch23 無家 → DECISION（對應 Preset Management / Media Widget 裁決） |
| C7 | Browse Tab 1:83 → DEGRADED + pilot 建議 |
| C8 | 預估 TC 數落在 420–480 區間 |

八項全中，才算這個階段真的取代了人工偵察。
