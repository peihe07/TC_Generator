# 下放包 — R-P99 修訂 + Charter 補正 + git 入庫

> 交付對象：Claude Code（§1–§3）／**Pei（§4 git 全部）**
> 觸發：上繳包 21 之四項發現 + Pei 要求下達 git 處理
> 授權層級：Tier 1（§1–§3）／**Tier 3（§4）**
> 日期：2026-08-12
> 封存：`features/projection/docs/handoff/22_rp99_and_git.md`

---

## 0. 四項回覆

### 0.1 R-P99 首次適用之差異 —— 採掃描結果，並修訂條文

執行層之判斷正確：`A-PJ76` / `A-PJ77` 於**上繳包 20** 開出並登記，包 21 對其所為
是**結案**而非新立。掃描得 `R-P98` / `R-P99` / `A-PJ78` 為正確結果。

> **R-P100｜R-P99 修訂：清單限「新立」，結案與援引另列**
> 「本包產生之新條文清單」限**本包新立**之編號。**結案、援引、更正既有編號者
> 另立一欄或另列一表**，不混入新立清單。
> 依據：人工列舉會把「本包處理到的」與「本包新立的」混在一起；`comm -23`
> 之集合差不會犯此錯（執行層 R-P99 首次適用之實證）。
>
> **自指命中之處置**：正則掃描定義正則之文件必然自指——`canon §5a 第.+條` 之
> pattern 會掃到 R-P99 條文內該 pattern 之字面。掃描結果須**人工複核自指命中並於
> 上繳包標明**，不自動排除（自動排除規則本身亦會自指）。
> 執行層主動回報此瑕疵，符合「詞彙型工具缺陷不會報錯」之紀律。

### 0.2 Charter 行數 —— **95 為預期值**，93 是我引錯

> **確認：95 行為正確。**
>
> 我在包 21 §0 寫「93 行版」，該數字取自**我沙箱內較早的一份**（`wc -l` = 93）。
> 實際寫入 repo 的版本另加了「援引任何 canon 或 profile 之節號前先確認該節存在」
> 一條、並改寫了自檢表那行，故為 95 行。
>
> **這是 canon §5a「不以自身先前輸出為來源」第四次**（前三次：剩餘列數 173、
> repo 狀態描述、037 description 127/171）。
>
> 執行層以**實測行數推第二段起點**而非硬編碼 93，是正確設計——若照 93 硬編碼，
> 第二段驗證會取錯起點而誤報不符。**此作法定為常規**：串接驗證一律以實測邊界
> 定位，不以文件所述行數定位。

### 0.3 R-P95 援引之處理 —— 加註正確，不改寫

> **追認執行層之處置。**
>
> R-P98 之「R-P95 之援引更正為 canon §8.2」，執行層以**標題加註**處理
> （`· 援引經 R-P98 更正`），原逐字區塊一字未動。
>
> **就地改寫逐字區塊會使「逐字」失去意義**，且 repo 已有先例（R-P93 被 R-P94
> 撤銷時標 `SUPERSEDED by R-P94` + 原文保留）。
>
> **通則**：逐字落檔之條文一律不就地改寫。撤銷標 `SUPERSEDED`、更正標
> `援引經 R-Pxx 更正`，原文永遠保留。審計軌跡之價值在於能看見判斷如何演變。

### 0.4 A-PJ78 之更正未進 Charter 落檔節 —— 已補

分析層已於本包前直接 `write_file` 補入 Charter 落檔節：

```
- **不限於下放包**：分析層產出之**任何**供落檔文件（charter、canon 節文、
  應 Pei 要求另行產出之文件），一律 `write_file` 寫入 repo。
  A-PJ62 僅涵蓋下放包，致 A-PJ78 以「不屬下放包之文件」形態復發。
```

**Charter 現為 98 行**（95 + 3）。須依 R-P97 重新串接 `PROJECT_INSTRUCTION.md`。

執行層之判斷正確：canon §8.7 有此條故非缺陷，但 **Charter 是每次對話都在
上下文裡的那份**，而該形態已復發一次。

---

## 1. 執行（Claude Code）

```
1. 重新串接 docs/runtime/PROJECT_INSTRUCTION.md
   驗證第二段 sha256 == fa9833ae64c9092f
   回報新行數（預期 Charter 98 + 分隔 3 + ASPICE 604 = 705）
2. R-P100 落檔至 DECISIONS.md §0.29
3. INDEX.md 新增第 22 列
4. 依 §4 準備 git，但不執行任何 git 寫入操作
5. 上繳包寫入 upstream/22_rp99_and_git.md
```

---

## 2. git 準備（Claude Code 做，不執行）

1. `git status --porcelain` 全量輸出
2. 依 §4.2 之六組分類，列出每組之檔案清單與變更行數
3. `git check-ignore -v` 驗證下列各項之忽略狀態並逐項回報：
   - `features/projection/inputs/`
   - `features/projection/backup/`（**預期未被忽略——見 §4.1**）
   - `features/projection/data/pcts_ui/`
   - `features/projection/batches/`
   - `output/`
   - `features/projection/data/sysad_sections.json`
4. 確認無任何客戶原始檔（`.xlsx` / `.pdf` / `.docx` / `.dbc` / `.apk`）落在
   將被 `git add -A` 納入之集合中——**逐檔列出副檔名統計**

**第 4 項為硬性前置**：`git add -A` 之風險在於它會納入所有未忽略之新檔，
而 `backup/` 目前正是未被忽略之客戶工作簿副本。

---

## 3. Pei 執行之 git 步驟

### 3.1 兩項政策先裁（未裁不得 commit）

| # | 項目 | 現狀 | 分析層建議 |
|---|---|---|---|
| **A** | `features/projection/backup/` 未被 `.gitignore` 涵蓋，內含 2 份 572 KB 客戶工作簿完整副本 | ❌ 未忽略 | **建議排除**。`.gitignore` 第 2 行已以 `inputs/` 排除客戶原始檔，備份是同一份檔案；R-P78 要求備份保留不刪，只能以排除解決。屬既有政策之補完 |
| **B** | `features/projection/data/pcts_ui/*.xml`（14 份 297 KB） | ❌ 未追蹤 | **建議入庫**。R-P11 之 L-PJ7 gate 讀 `pcts_evidence.json` 決定 23 列能否修改；若 status 遭質疑，原始 dump 是唯一物證。取證組合（Pixel 10 / Android 16 / apk 5.1-prod.922397802）日後未必可重現 |

⚠️ **B 屬版控政策，依 Charter 應由你裁定**。我先前於 R-P90 逕自裁為「入庫」，
**已越出自裁界線**，改列為建議待你追認或推翻。

**A 若裁定排除**，`.gitignore` 新增：

```
# Backups of customer workbooks - same policy as inputs/
backup/
```

**B 若裁定入庫**，需確認 `.gitignore` 之現行規則不涵蓋該路徑；若涵蓋則加
`!data/pcts_ui/`。

### 3.2 commit 順序與指令

**前置**：§2 第 4 項之副檔名統計確認無客戶原始檔。

```bash
cd /Users/peihe/Work_Projects/TC_Generator

# 0) 先看清楚 add -A 會納入什麼（不執行 add）
git add -A --dry-run | sort | less

# 1) canon + profile + charter
git add docs/fw036/FEATURE_ONBOARDING.md \
        docs/runtime/OPERATING_CHARTER.md \
        docs/runtime/PROJECT_INSTRUCTION.md \
        docs/runtime/profiles/FW036_R1L_Projection_Profile.md
git commit -m "docs: add canon 5a numeric discipline, section 8 handoff contract, and Projection profile"

# 2) 治理文件
git add features/projection/DECISIONS.md \
        features/projection/ANOMALIES.md \
        features/projection/DATA_REQUESTS.md \
        features/projection/PLAYBOOK.md \
        features/projection/RECON.md \
        features/projection/feature.yaml
git commit -m "docs(projection): record R-P1..R-P100 and A-PJ01..A-PJ78"

# 3) 往返封存（handoff / upstream / reports / INDEX）
#    須用 -A 以保留重新命名偵測
git add -A features/projection/docs/
git commit -m "docs(projection): archive handoff and upstream packages with INDEX"

# 4) 分析產物
git add features/projection/data/
git commit -m "feat(projection): add Layer 3 derivations, signal map, and PCTS evidence"

# 5) 腳本
git add features/projection/scripts/
git commit -m "feat(projection): centralise lint matchers and measurement conditions"

# 6) .gitignore（若 §3.1 裁定變更）
git add features/projection/.gitignore
git commit -m "chore(projection): exclude backup/ under customer-source policy"

# 7) batch 記錄（若裁定入庫）
git add features/projection/batches/
git commit -m "docs(projection): add Phase 5 batch audit records"
```

**第 3 組必須用 `git add -A`** —— 執行層已指出：搬移對 git 呈現為 16 筆 `D`
加新目錄未追蹤，不用 `-A` 則重新命名偵測失效，history 會呈現為「刪 16 加 19」
而非搬移。

### 3.3 tag

```bash
git tag -a fw036-projection-refine-v1 -F - <<'EOF'
Projection FULL_REFINE delivery

交付檔    NR1L_GEN1(HDCC)_Ver_20260813.xlsx
SHA256    b16debb7bc609e39044803760171cf1d2b583fd1ed8a4cd2602e82029c8c6b67
size      574,700 bytes
基準檔    11579c9b3b8e56eb9f25a06acd2ce9281409286248a37b327be4732cc0bdede9

交付位置
  output/NR1L_GEN1(HDCC)_Ver_20260813.xlsx
  /Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/Projection/CP:AA:iPod/NR1L_GEN1(HDCC)_Ver_20260813.xlsx

交付檔不在版本歷史中（inputs/ 與 output/ 依客戶原始檔政策排除）。
本 tag 之樹不含交付檔；交付版本以上列 SHA256 綁定，
本 annotation 為該 digest 之唯一版控位置（FEATURE_ONBOARDING §6）。
output/ 之 .sha256 旁檔為本機驗證用，不入庫。

內容
  資料列   559 → 565（刪 r562、補 7 條）
  覆蓋     170/171 leaf（未覆蓋僅 SWE1-PROJ-146）
  變更     既有 132 列（內容 65 列 + 授權例外 76 列，含重疊）
  裁決     R-P1 ~ R-P100
  異常     A-PJ01 ~ A-PJ78
  OPEN DR  <自 DATA_REQUESTS.md 現行記載取得>
EOF
```

⚠️ **`OPEN DR` 一行須自 `DATA_REQUESTS.md` 現行記載取得**，不得沿用任何先前
列舉（canon §5a）。前次列舉已被證實有誤（列了已撤銷之 #9 #10、漏列 #14）。

⚠️ **覆蓋率為 170/171**。我先前在 annotation 草案寫 165/171 為錯誤，實測
交付檔為 170/171，未覆蓋僅 `SWE1-PROJ-146`（R-P18 排除，DR#8）。

---

## 4. 上繳要求

1. `PROJECT_INSTRUCTION.md` 重新串接後之行數與第二段雜湊
2. R-P100 落檔確認
3. §2 之 git 準備四項，**特別是第 4 項副檔名統計**
4. `OPEN DR` 之現行記載清單（供 tag annotation）
5. 依 R-P100 產生之新條文清單（新立與結案分列）
6. 本包是否仍有該驗而未驗者

---

## 5. 本包新立之編號（依 R-P100，由執行層掃描複核）

新立：`R-P100`
結案／援引：`R-P99`（修訂）、`R-P95`（援引更正之追認）、`A-PJ78`（Charter 補正）

**不 commit —— §3 全部由 Pei 執行。**
