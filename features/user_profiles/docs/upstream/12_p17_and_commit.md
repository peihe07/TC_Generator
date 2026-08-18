# 上繳 12 — p17 之掛回、AUTO 集可重算性、052f67d 三案重述

- 產出層：執行層｜2026-08-17｜對象：分析層
- 下放包：`12a_rulings.md`（R-U49～R-U54）＋ `12b_tasks.md`（作業 1–6）
- **本輪未生成任何 TC**（12b 作業 6）。`generated/` 仍為空。

---

## 1. 作業 4（**最優先**）—— `052f67d` 之重述（R-U54）

### 1.1 該 commit 之污染內容

```
commit 052f67d00b2d40bb72995ebacbd6ebeb993c4bd2
Author: Pei    Date: Mon Aug 17 17:24:28 2026 +0800
feat(power): round 09 — three new gates, feature.yaml corrected, batch 1 held
共 33 檔，5441 insertions(+), 220 deletions(-)
```

**message 只述 power，實際夾帶 user_profiles 之 8 個檔**：

| # | 檔 | 屬 |
|---|---|---|
| 1 | `features/user_profiles/BASELINE.sha256` | 03 輪 |
| 2 | `features/user_profiles/DECISIONS.md` | 03 輪 |
| 3 | `features/user_profiles/RECON.md` | 03 輪 |
| 4 | `features/user_profiles/data/recon_leaf_to_section.tsv` | 03 輪 |
| 5 | `features/user_profiles/docs/INDEX.md` | 03 輪 |
| 6 | `features/user_profiles/docs/handoff/03_recon_start.md` | 03 輪 |
| 7 | `features/user_profiles/docs/upstream/03_recon.md` | 03 輪 |
| 8 | `features/user_profiles/feature.yaml` | 03 輪 |

其餘 25 檔為 power 之 07／08／09 三輪內容。

**「污染」之精確含義**：
**不是**「不該進版控之物進了版控」——這 8 個檔**本來就該進版控**，內容完整無誤。
**而是**「**歸屬不準**」：一個 message 寫著 `feat(power)` 的 commit，
承載了另一個 feature 三輪的交付。日後任何人以
`git log -- features/user_profiles/` 追 03 輪之落點，
會看到一個 power 的 commit —— **log 說的話與事實不符。**

**成因**（power session 之執行層自陳，逐字）：

> 我執行 `git add features/power/`，但另一個 session 在此之前已經把他們的檔案
> 放進 index 了，而 `git commit` 不帶 pathspec 就會提交整個 index。

即：**裸 `git commit` 提交的是整個 index，不是你剛 add 的東西。**

### 1.2 三案之具體選項、代價與不可逆性

**現況先講**（本輪實測，見 §1.4）：**該 commit 已推送**，
且其後已有 **4 個提交**疊在上面。這使三案之代價與當初提出時**不同**。

| 案 | 內容 | 代價 | 不可逆性 |
|---|---|---|---|
| **1 留著** | 不動歷史，log 歸屬不準留在紀錄裡 | 追溯 user_profiles 03 輪時會落在一個 power commit 上；**這是第二次**（前有 `645e55f`→`cc04aa1` 之重寫）| **零** —— 隨時可改採他案（但他案之成本只會更高）|
| **2 `reset --soft HEAD~1` 後分兩次提交** | 拆成 `feat(power)` ＋ `feat(user_profiles)` 兩個 commit | **當初**：只需確認另一 session 沒在動。**現在**：052f67d 後已有 4 個提交，須 rebase 四個；且**已推送**，須 `push --force` | **高，且已不可單方面回收** —— 已推送者他人可能已 fetch；force push 會使任何基於舊歷史之本地分支分岔 |
| **3 只改 message 使其涵蓋兩邊** | 內容不動，只改述 | 仍是歷史改寫（commit hash 會變），代價與案 2 之 rebase 相同，**但只換到一句比較準的 message** | **與案 2 同高，收益卻低得多** |

**執行層之意見（不是裁決）**：現況下**案 1 之相對代價最低**。
案 2／3 的成本已從「當初的一次 reset」變成「rebase 四個提交 ＋ force push
一條已推送的分支」，而它們要修的是**一句 message 的歸屬**，
內容本身從頭到尾都是完整的。
**真正該修的不是這個 commit，是產生它的作法** ——
即約定各 session 一律 `git commit -- <pathspec>`（本輪之 `f653cb0` 即照此作，
提交後逐檔驗證無他 feature 檔案混入）。

### 1.3 其最初提出之包號與節次 —— **沒有包號，也沒有節次**

12a 記「分析層之覆核記錄無此項 —— **覆核漏回應，責在分析層**」。
**此前提須更正。** 本輪查證：

| 查法 | 結果 |
|---|---|
| `grep -rn "052f67d"` 全 repo（排除 `.git/`）| **僅 3 處命中**：`12a_rulings.md`、`12b_tasks.md`、`11_plp_and_pilot_prep.md` §6 第 7 項 |
| user_profiles 全部上繳包（01–11）| 除 11 §6 外**無任何一處**提及 |
| power／comfort 之 handoff／upstream | **無** |

**三案之實際提出處**：**power session 之聊天回覆**（2026-08-17，power 09 輪提交後）。
其原文列「1. 留著／2. `git reset --soft HEAD~1` 後分兩次提交／3. 只改 message」，
並附「我不會自作主張再改一次歷史」與「這是第四次徵兆了」。
**該回覆從未寫入 `features/power/docs/upstream/` 之任何一包。**

**故：**

1. 分析層之覆核記錄無此項，**是因為它從未進入任何包** —— **與 R-U41 相符，非漏回應。**
   12a 之「責在分析層」一句，其前提不成立。
2. **它也不是「執行層於前輪提出」**：提出者是 **power session 之執行層**，
   不是 user_profiles 之執行層。11 輪上繳 §6 第 7 項寫「三案已於前輪提出」，
   **措辭不精確** —— 那不是本 feature 的任何一輪，是另一個 session 的聊天。
   **這是本執行層的記載瑕疵，具名更正。**

### 1.3.1 R-U54 所問之「R-U41 是否須加例外」

**執行層之判斷：不須加例外，且本條不是反例。**

R-U41 定「未列入者視為未曾提出」。本項**確實未曾提出**（未進任何包），
所以 R-U41 對它的處理**是對的，不是失效**。
真正發生的事是**另一個問題**：

> **一件跨 session 的事，在 A session 的聊天裡提出，就不會出現在 B session 的包裡。**

這不是 R-U41 的漏洞，是 **R-U48（貼文不算交付）之同一個失效模式，
只是跨了 session** —— power session 的三案沒落檔，
和 10 輪的上繳沒落檔，是同一件事的兩次發生。

**建議**（待裁）：與其給 R-U41 加例外，不如把 R-U48 之適用範圍
由「本 feature 之上繳」擴及「**任何 session 提出而需他方裁決之事項**」。
本項若當初落在 power 的上繳包裡，它就會出現在 power 的覆核清單上，
根本不需要 user_profiles 這邊在 11 輪憑記憶提起。

### 1.4 現況 —— 是否已推送、其後是否有提交

```
$ git remote -v
origin  https://github.com/peihe07/TC_Generator.git

$ git merge-base --is-ancestor 052f67d origin/feat/m1-stage7-scorecard ; echo $?
0        → **已推送**

$ git rev-list --count 052f67d..HEAD
4

$ git log --oneline 052f67d..HEAD
f653cb0 feat(user_profiles): rounds 09-11 — PLP union criterion landed, …
68e9d51 feat(user_profiles): round 08 — Phase 1 close, framework finalised …
25306ef feat(power): package 12 pilot fixes — Test Case Framework sheet …
d0a0092 feat(user_profiles): rounds 04-07 — verification, baseline audit, …

$ git branch -a --contains 052f67d
* feat/m1-stage7-scorecard
  remotes/origin/feat/m1-stage7-scorecard
```

**推送紀錄**（`.git/logs/refs/remotes/origin/…`）顯示該分支持續被推送，
最近一次為 `68e9d51 → f653cb0`。
**執行層未執行任何 `push`** —— 推送由 Pei（或另一 session）為之。

**要點**：**052f67d 已在遠端**。任何改寫它的方案都不再是本地作業。

### 1.5 未自行處置

**未執行任何 git 之歷史改寫**，亦未提出 PR、未 push。
git 屬 Pei（R-G5），涉歷史改寫者尤其不可逆（12b §4）。

---

## 2. 作業 1 —— 條文入庫

`RULINGS.md` 新增「第十二輪條文」段：**R-U49～R-U54 逐字**，其後附執行層回報六點。
12a 自檢列六條，入庫六條，**餘數 0**。

**R-U47 已標**（`RULINGS.md` L852）：

```
R-U47 [PREMISE CORRECTED by R-U53 — must_carry 實為覆蓋 4／未覆蓋 3，非 3／4；
       核可與其餘判定有效] pilot 取樣清單 —— 核可
```

**原文一字未改** —— 標記插入於條號與其後空白之間，條文本體未被觸碰。

---

## 3. 作業 2 —— R-U49 四步，**逐步輸出俱附**

### 步驟 1 —— 先補自檢項（`must_carry_for()` **尚未改動**）

新增第 7 項「must_carry 七條**皆有歸宿**」。其判準與第 2 項**刻意不同**：

- 第 2 項：抽樣 16 leaf 逐一實跑，驗「**有注入者是否正確**」
- 第 7 項：**全 169 節逐節問一次**「這條 must_carry 掛得上嗎」，
  驗「**七條是否都掛得上某節**」

一條掛不回任何節之 must_carry，**在第 2 項眼中不存在** —— 那正是 `p17` 的形狀。

### 步驟 2 —— **證明它紅**（實際輸出）

```
  **FAIL** — 7. must_carry 七條**皆有歸宿**（非只驗已注入者是否正確）
      must_carry 條目數 = 7（須為 7）
          9.8 → 掛回 ['9.8']
          9.3.2 → 掛回 ['9.3.2']
          9.1 → 掛回 ['9.1']
          11.4 → 掛回 ['11.4']
          11.5 → 掛回 ['11.5']
          p14 → 掛回 ['9.1']
      **無歸宿者 = ['p17']**（須為空）
      餘數：6 有歸宿 ＋ 1 無歸宿 = 7

<7 / 7 self-check items FAIL
exit=1
```

**`p17` 無歸宿，exit=1。** 此時 `must_carry_for()` 仍是原本的 `impact` 散文比對版。
**p14 之所以綠，是因為它的說明文字剛好寫了「9.1」** —— 巧合，不是設計。

### 步驟 3 —— 改為顯式對照表

```python
# R-U49 —— `p<N>` 之顯式歸屬對照表。
#
# **廢除以 `impact` 散文欄作掛回鍵之設計**：p14 之所以掛得回 9.1，
# 是因為它的說明文字**剛好**寫了「9.1 之列項順序」；p17 之說明是「同上」，
# 於是它掛不回任何節，且無聲無息 —— 那是巧合，不是設計。
# 人看的說明欄不該同時當機器用的外鍵。
PAGE_TO_SECTION = {
    "p14": "9.1",    # Table EDPR1 之列項
    "p17": "11.5",   # Connected Navigation 之列項（同 11.5 之表）
}
```

`must_carry_for()` 之掛回分支同步改為
`PAGE_TO_SECTION.get(r["outline"]) == section`，
**`impact` 欄自此不再參與任何比對**。

### 步驟 4 —— 重跑轉綠（實際輸出）

```
  PASS — 7. must_carry 七條**皆有歸宿**（非只驗已注入者是否正確）
      must_carry 條目數 = 7（須為 7）
          9.8 → 掛回 ['9.8']
          9.3.2 → 掛回 ['9.3.2']
          9.1 → 掛回 ['9.1']
          11.4 → 掛回 ['11.4']
          11.5 → 掛回 ['11.5']
          p17 → 掛回 ['11.5']
          p14 → 掛回 ['9.1']
      **無歸宿者 = []**（須為空）
      餘數：7 有歸宿 ＋ 0 無歸宿 = 7

7 / 7 self-check items PASS
exit=0
```

**四步之輸出俱在，紅過才綠。**

### 3.1 連帶效果 —— **R-U53 之待追蹤項再減一**

修好後第 2 項之輸出隨之改變：

```
SWE1-HMI-PROF-112-01（sec 11.5）→ **2 條**（原 1 條）
```

即 `p17` 現在會隨 sec 11.5 一併注入，**而 `PROF-112-01` 正在 pilot 取樣內**。

**故 T-3（p17）已由「待追蹤」變為「pilot 即覆蓋」**，
待追蹤項由三條減為**兩條**：

| # | outline | 狀態 |
|---|---|---|
| T-1 | 9.1 | 待追蹤 —— 第一批正式批次前須覆蓋 |
| T-2 | p14（掛 9.1）| 待追蹤 —— 隨 T-1 |
| ~~T-3~~ | ~~p17~~ | **已解 —— 隨 pilot 之 `PROF-112-01`（sec 11.5）注入** |

---

## 4. 作業 3 —— R-U52：AUTO 集之可重算性，含對照向

### 4.1 掃描收進 `--selfcheck`（第 8 項）

新增 `plp_scan_union()`：實跑甲∪乙之掃描並與常數比對。
**MANUAL 集不納入本斷言**（R-U46：人工判讀不併入自動判準）。

```
  PASS — 8. `PLP_LEAVES_AUTO` 可由甲∪乙之掃描重算得出（R-U52）
      重算所得（4）= ['SWE1-HMI-PROF-001-01', 'SWE1-HMI-PROF-005',
                     'SWE1-HMI-PROF-012', 'SWE1-HMI-PROF-032']
      常數所載（4）= ['SWE1-HMI-PROF-001-01', 'SWE1-HMI-PROF-005',
                     'SWE1-HMI-PROF-012', 'SWE1-HMI-PROF-032']
      常數有而掃描無：[]（須為空）
      掃描有而常數無：[]（須為空）
      MANUAL 集 ['SWE1-HMI-PROF-001-02', 'SWE1-HMI-PROF-001-03'] **不納入本斷言**

8 / 8 self-check items PASS
```

**兩向差集分列**（不只驗數量相等）：
`常數有而掃描無`＝人為新增未經掃描者；`掃描有而常數無`＝spec 改動後常數未跟上。
**兩者是不同的病，合成一個數字就看不出來。**

### 4.2 對照向（R-G7）—— **證明它會紅，兩個方向都證**

新增 `--selfcheck-tamper {drop,add}`，**是可重跑的指令，不是註解**：

```
$ python3 scripts/build_batch_context.py --selfcheck --selfcheck-tamper drop
      常數所載（3）= [...001-01, ...005, ...032]
      掃描有而常數無：['SWE1-HMI-PROF-012']（須為空）
<8 / 8 self-check items FAIL

$ python3 scripts/build_batch_context.py --selfcheck --selfcheck-tamper add
      常數所載（5）= [..., 'SWE1-HMI-PROF-999']
      常數有而掃描無：['SWE1-HMI-PROF-999']（須為空）
<8 / 8 self-check items FAIL
```

**漏一條會紅，多一條也會紅** —— 只驗一個方向會漏掉另一種竄改。

---

## 5. 作業 5 —— R-U50／R-U51 落地

寫入 `DECISIONS.md`：

- **D-UP12-01（R-U50 同節連坐）**：四條件逐項對 4.1 核對，四項皆成立。
  登記為**通則候選**，一例不升 canon。
  **並聲明其盲區**：第 4 項「併列理由完全相同」**無可測形式**，
  故本判準是一張人工核對表，**不得自動套用**。
- **D-UP12-02（R-U51 判讀口徑）**：採「指涉所指之物」。
  `PROF-106`（10.2 三欄表）、`PROF-108`（10.3.1 頁內 chart）**定案為否**，
  11 輪之待裁解除。**代價已明記**：其覆蓋由 §8.2.1 之 sibling Req 承擔；
  日後若發現 ch10 漏了 PLP 表某項，處置為補 sibling Req 或另立 leaf，
  **不是回頭放寬本判準**。

---

## 6. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 性質 | 說明 |
|---|---|---|---|
| 1 | **取樣清單存於 `/tmp/sample.json`** | **脆弱點（新發現）** | `build_batch_context.py` 之 `__main__` 從 `/tmp/sample.json` 讀 16 條取樣。**`/tmp` 一被清，`--selfcheck` 就跑不起來** —— 一個用來證明生成前置成立的工具，其輸入不在版控內。建議落為 `data/pilot_sample.tsv`。**本輪未改**（12b 未授權改取樣載體）|
| 2 | **`PAGE_TO_SECTION` 之 p17 → 11.5 未經 PDF 複位** | 判讀，非量測 | 07 輪載明 `p<N>` 之歸屬節次「未逐一定位」。本輪依 R-U49 明文填 11.5，**該值來自裁決，不是來自對 PDF p17 的重新定位**。若要坐實，須回 PDF p17 確認該列項確屬 11.5 之表而非別處 |
| 3 | **第 7 項自檢驗「有歸宿」，未驗「歸宿正確」** | 檢查之盲區（R-G11）| 若把 `p17` 誤填為 `9.1`，第 7 項**仍會綠** —— 它只問掛不掛得上，不問掛得對不對。可測的正確性判準目前沒有（見第 2 項：正確性本身尚未量測）|
| 4 | **R-U50 之第二例尚未出現** | 通則候選 | 判準只在一個案例上用過。**一個判準在一個案例上永遠是對的** —— 第二例出現前，其分辨力未受檢驗 |
| 5 | **R-U51 之代價未量化** | 已知而未測 | 「由 sibling Req 承擔」是設計上的答案，**尚未有任何檢查在守它**。ch10 之 TC 生成後，應複核 PLP 表各項是否確實各有歸宿 |
| 6 | **052f67d 之三案未裁** | **待 Pei** | 重述已完成（§1），且**現況已變**（已推送 ＋ 其後 4 個提交）。裁前不動 |
| 7 | **跨 session 提出事項之落檔規則** | 待裁 | §1.3.1 之建議：R-U48 之適用範圍擴及跨 session 事項。**這是本輪唯一一件會防止同型問題再犯的事**，其餘都是補救 |
| 8 | A-UP09／R-U14（DV gate）、DR #3／#4、R-U17、N-XF01、待執行之 git 清單 | 承前未決 | 不擋本輪 |

---

## 7. 動作清單 —— 與 git 陳述逐項對照（R-G6）

| # | 動作 | 對象 | 是否 git |
|---|---|---|---|
| 1 | 檔案追加 | `RULINGS.md`（＋R-U49～R-U54 逐字＋回報段）| 否 |
| 2 | **檔案編輯** | `RULINGS.md` L852（R-U47 加 `[PREMISE CORRECTED by R-U53]`，原文未改）| 否 |
| 3 | 檔案追加 | `DECISIONS.md`（＋D-UP12-01、D-UP12-02）| 否 |
| 4 | **檔案編輯** | `scripts/build_batch_context.py`（第 7／8 項自檢、`PAGE_TO_SECTION`、`plp_scan_union()`、`--selfcheck-tamper`）| 否 |
| 5 | 檔案新建 | `docs/upstream/12_p17_and_commit.md`（本檔）| 否 |
| 6 | 檔案編輯 | `docs/INDEX.md`（＋第 12 輪列與段）| 否 |
| 7 | 程式執行 | `--selfcheck` 四次（步驟 2 紅／步驟 4 綠／tamper drop／tamper add）| 否 |
| 8 | **唯讀** | `git show`／`log`／`remote -v`／`merge-base`／`rev-list`／`branch --contains`／`grep .git/logs`（**全為 §1 之查證**）| **是（唯讀）** |

**本輪未執行任何會改變 repo 狀態之 git**：`add`／`commit`／`push`／`checkout`／
`restore`／`reset`／`rebase`／`stash`／`clean`／`rm`，**尤其未作任何歷史改寫**。

### 7.1 **須據實記載之一項** —— 本輪之前，執行層執行過 `add`／`commit`

12b §「不在本包授權範圍」列「任何 git 操作」。為免記載不實，明記：

**在 12 輪下放包送達之前**，Pei 於 11 輪上繳後直接指示「git commit」，
執行層據此執行了：

```
git add <features/user_profiles/ 之 9 個路徑>
git commit -- features/user_profiles     → f653cb0
```

- **時點在 12b 送達之前**，非違反本包之禁區；
- 依 Pei 之**明確指示**執行（R-U45／R-G5 定 git 屬 Pei，本次為 Pei 指示下之代行）；
- **以 pathspec 限定提交**，提交後逐檔驗證：16 檔全在 `features/user_profiles/` 之下，
  **無他 feature 檔案混入** —— 即 §1.2 所述「該修的是作法」已先照辦一次；
- **未執行 `push`**。`f653cb0` 現已在 origin，係 Pei 或另一 session 所推。

**未動**：`generated/`（**未生成任何 TC**）、`framework.md`、`feature.yaml`、
`ANOMALIES.md`、`DATA_REQUESTS.md`、`BASELINE.sha256`、`.gitignore`、
`data/` 之任何檔（**含 `xlsx_missing_clauses.tsv` —— R-U49 採第 2 案，改程式不改資料**）、
`inputs/`、`forms/`、**他 feature 之任何檔**。
