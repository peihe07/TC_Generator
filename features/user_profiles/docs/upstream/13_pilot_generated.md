# 上繳 13 — pilot 生成（16 條）、p17、052f67d

- 產出層：執行層｜2026-08-18｜對象：分析層
- 下放包：`13_pilot_run.md`（作業 A–E；**本包無裁決條文**）
- 產物：`generated/` 之 **16 個 leaf 檔 / 16 條 TC**（全文見 §6）
- **未寫回工作簿**（R-U14）；**本輪未執行任何 git**

> **停手門檻已依 13 包改用**：不屬 (a) 不可逆／(b) 跨 feature／(c) 影響逾語料 10%
> 三類者，取最保守解讀續行並具名記錄。**本輪據此續行 6 次，逐項列於 §5。**

---

## 1. 作業 B（最優先）—— `052f67d` 三案重述

> A／C／D 三項已於 **12 輪**執行完畢並落檔（`docs/upstream/12_p17_and_commit.md`）。
> 13 包送達時該包尚未被覆核，故本包**重跑全部驗證並重貼輸出**，不以「已做過」帶過。

### 1.1 污染內容

`052f67d`（33 檔，5441+ / 220-，message 為 `feat(power): round 09 …`）
夾帶 **user_profiles 之 8 個檔**（皆屬 03 輪）：

`BASELINE.sha256`／`DECISIONS.md`／`RECON.md`／`data/recon_leaf_to_section.tsv`／
`docs/INDEX.md`／`docs/handoff/03_recon_start.md`／`docs/upstream/03_recon.md`／
`feature.yaml`

**「污染」之精確含義**：不是「不該進版控之物進了版控」——這 8 檔本來就該進，
內容完整。**是歸屬不準**：以 `git log -- features/user_profiles/` 追 03 輪，
會落在一個 `feat(power)` 的 commit 上。

**成因**（power session 執行層自陳，逐字）：

> 我執行 `git add features/power/`，但另一個 session 在此之前已經把他們的檔案
> 放進 index 了，而 `git commit` 不帶 pathspec 就會提交整個 index。

### 1.2 三案、代價、不可逆性

| 案 | 內容 | 代價 | 不可逆性 |
|---|---|---|---|
| **1 留著** | 不動歷史 | log 歸屬不準（第二次；前有 `645e55f`→`cc04aa1`）| **零** |
| **2 `reset --soft HEAD~1` 後分兩次提交** | 拆成 power／user_profiles 兩個 commit | **當初**：確認無人在動即可。**現在**：其後已有 **5** 個提交須 rebase，且**已推送**須 `push --force` | **高，且已不可單方面回收** |
| **3 只改 message 涵蓋兩邊** | 內容不動，只改述 | 同案 2 之 rebase＋force push 成本，**收益僅一句 message** | 同案 2 |

**執行層意見（非裁決）**：現況下**案 1 相對代價最低**。
案 2／3 要修的是一句 message 的歸屬，而其成本已變成「rebase 5 個提交 ＋
force push 一條已推送的分支」。**該修的是產生它的作法** ——
即各 session 一律 `git commit -- <pathspec>`。

### 1.3 最初提出之包號與節次 —— **沒有包號，也沒有節次**

| 查法 | 結果 |
|---|---|
| `grep -rn "052f67d"` 全 repo（排除 `.git/`）| 僅命中 12a／12b／13 下放包與我自己的 11、12 上繳 |
| user_profiles 上繳 01–11 | 除 11 §6 第 7 項外**無** |
| power／comfort 之 handoff／upstream | **無** |

**實際提出處**：**power session 之聊天回覆**（2026-08-17，power 09 輪提交後），
原文列「1. 留著／2. `git reset --soft HEAD~1` 後分兩次提交／3. 只改 message」。
**從未寫入任何上繳包。**

由此兩點須更正記載：

1. 分析層之覆核記錄無此項，**是因為它從未進入任何包**，非漏回應；
2. 它也不是「本 feature 執行層於前輪提出」—— 提出者是 **power session 之執行層**。
   我 11 輪 §6 寫「三案已於前輪提出」措辭不精確，**具名更正**。

### 1.4 現況（**本輪重測，數字已變**）

```
$ git merge-base --is-ancestor 052f67d origin/feat/m1-stage7-scorecard ; echo $?
0        → 已推送

$ git rev-list --count 052f67d..HEAD
5        ← 12 輪測得為 4，本輪為 5

$ git log --oneline 052f67d..HEAD
a3e12cd feat(power): packages 13-16 — ER quality, final step intent, misread cleanup, write order and dry-run
f653cb0 feat(user_profiles): rounds 09-11 …
68e9d51 feat(user_profiles): round 08 …
25306ef feat(power): package 12 pilot fixes …
d0a0092 feat(user_profiles): rounds 04-07 …
```

**時效性成立**：每過一輪，案 2／3 需 rebase 之提交數就多一個。
**未自行處置** —— 屬 (a) 類，git 與歷史改寫屬 Pei。

---

## 2. 作業 A —— p17 四步（**紅過才綠**）

### 步驟 1 — 先補自檢項（`must_carry_for()` 未動）

第 7 項「must_carry 七條**皆有歸宿**」。與第 2 項刻意不同判準：
第 2 項驗「有注入者是否正確」，第 7 項**全 169 節逐節問**「這條掛得上嗎」。
**一條掛不回任何節之 must_carry，在第 2 項眼中不存在** —— 那正是 `p17` 之形狀。

### 步驟 2 — **紅**（實際輸出）

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

`p14` 之所以綠，是因為它的 `impact` 說明文字**剛好**寫了「9.1」—— 巧合。

### 步驟 3 — 顯式對照表

```python
PAGE_TO_SECTION = {
    "p14": "9.1",    # Table EDPR1 之列項
    "p17": "11.5",   # Connected Navigation 之列項（同 11.5 之表）
}
```

`must_carry_for()` 之掛回改為 `PAGE_TO_SECTION.get(...) == section`，
**`impact` 欄自此不再參與任何比對** —— 人看的說明欄不該同時當機器用的外鍵。

### 步驟 4 — **綠**（實際輸出）

```
  PASS — 7. must_carry 七條**皆有歸宿**（非只驗已注入者是否正確）
      must_carry 條目數 = 7（須為 7）
          9.8 → ['9.8']   9.3.2 → ['9.3.2']   9.1 → ['9.1']
          11.4 → ['11.4'] 11.5 → ['11.5']
          p17 → ['11.5']  p14 → ['9.1']
      **無歸宿者 = []**（須為空）
      餘數：7 有歸宿 ＋ 0 無歸宿 = 7

8 / 8 self-check items PASS
exit=0
```

### 連帶效果 —— pilot 之 `PROF-112-01` 現注入 **2 條** must_carry

`p17` 掛上 11.5 後，第 2 項之輸出由 1 條變 2 條，
而 `PROF-112-01` 正在本批取樣內 → **T-3（p17）已由待追蹤變為 pilot 即覆蓋**。
待追蹤剩 **T-1（9.1）／T-2（p14）**。

---

## 3. 作業 C —— R-U52：AUTO 集可重算，含對照向

```
  PASS — 8. `PLP_LEAVES_AUTO` 可由甲∪乙之掃描重算得出（R-U52）
      重算所得（4）= ['…001-01', '…005', '…012', '…032']
      常數所載（4）= ['…001-01', '…005', '…012', '…032']
      常數有而掃描無：[]（須為空）
      掃描有而常數無：[]（須為空）
      MANUAL 集 ['…001-02', '…001-03'] **不納入本斷言**
```

**兩向差集分列**：「常數有而掃描無」＝人為新增未經掃描者；
「掃描有而常數無」＝spec 改動後常數未跟上。**兩者是不同的病。**

對照向（可重跑之指令，非註解）：

```
$ … --selfcheck --selfcheck-tamper drop   → 掃描有而常數無：['…012']   <8/8 FAIL
$ … --selfcheck --selfcheck-tamper add    → 常數有而掃描無：['…999']   <8/8 FAIL
```

**漏一條會紅，多一條也會紅。**

---

## 4. 作業 D —— R-U50／R-U51 落地

寫入 `DECISIONS.md`：

- **D-UP12-01（R-U50 同節連坐）** —— 四條件逐項對 4.1 核對，四項皆成立；
  登記為通則候選。**盲區**：第 4 項「併列理由完全相同」**無可測形式**，
  故本判準是人工核對表，不得自動套用。
- **D-UP12-02（R-U51 判讀口徑）** —— 採「指涉所指之物」；
  `PROF-106`（10.2 三欄表）、`PROF-108`（10.3.1 頁內 chart）**定案為否**。
  **代價明記**：其覆蓋由 §8.2.1 之 sibling Req 承擔；
  若日後發現 ch10 漏了 PLP 表某項，處置為補 sibling Req，**不是回頭放寬判準**。

---

## 5. 作業 E —— pilot 生成（16 條）

### 5.1 產物與 lint

| 項 | 結果 |
|---|---|
| 產物 | `generated/<req_id>.json` **16 檔 / 16 條 TC**，`NR1L-UserProfiles-001…016` |
| 生成器 | `scripts/gen_pilot.py`（單一來源，可重跑） |
| `lint_tcs.py`（**本輪新建**）語料 | **16 條，違規 0** |
| `lint_tcs.py --self-test` | **28 / 28 directional PASS**（每閘一注入＋同閘範圍向） |
| `lint_variant_labels.py` 反向 | **7 / 7 PASS** |
| `lint_variant_labels.py --check` | 掃 16 條，**違規 0** |
| `build_batch_context.py --selfcheck` | **8 / 8 PASS** |

**lint 全綠不等於通過** —— pilot 之覆核為分析層之工作（10b 明文）。

**`lint_variant_labels` 之 0 違規不是空過**（已驗其確實生效）：
`variant_of()` 對 **011 與 013** 判為 R1 High；把禁用字串注入真實之 TC-011 →
**轉紅**（`NR1L-UserProfiles-011.expected_result: … 出現 Stellantis Account`）。

### 5.2 分布

- design method：功能測試×8、邊界值分析×4、基礎故障注入×1、狀態轉換×1、
  情境／用例×1、負向測試×1
- priority：**P0×5**（偏好儲存 2、profile 建立 1、Valet 進出 2）、P1×4、P2×7
- Test Set：八組各 2（**R-G10 餘數 0**）

### 5.3 **判準歧義 6 次 —— 皆依門檻續行，逐項具名**

| # | 歧義 | 類別 | 取之解讀 | 影響面 |
|---|---|---|---|---|
| 1 | spec 8.7 寫 `~12 characters`（約），037 leaf 寫 12 | 非 (a)(b)(c) | **取 12** —— 較窄，且 037 為單位權威（§8.2）| 1 條（TC-009），已記其 remarks |
| 2 | 是否為列舉項加負向配對（canon §7）| 非 (a)(b)(c) | **不加** —— 16 leaf 為取樣單位，加測即擴張範圍（§8.4.2）| 見 §5.4 之三個候選 |
| 3 | pre_conditions 是否沿用 Comfort 之 `[spec-derived]` 標記 | 非 (a)(b)(c) | **不用** —— 該標記為 Comfort 之慣例，本 feature 無對應裁決；Comfort 後亦以 94 移除 | 全 16 條 |
| 4 | 9.8 之 PU0609 句（must_carry）是否寫進 TC-012 之 ER | 非 (a)(b)(c) | **不寫** —— 其觸發為「變更設定」而非「按 More Settings」，屬不同觸發（§5.7），且 **037 未為其切 leaf** | 1 條；缺口見 §5.5 |
| 5 | 13.2 之兩半（主機不得退出／車主遠端可停用）是否拆兩條 | 非 (a)(b)(c) | **不拆** —— 只驗前半則「只有車主可以」無從成立；037 之 leaf 單位為一 | 1 條（TC-016）|
| 6 | 11.5 之補句表列項（Table CPA2 各列）是否須進 ER | 非 (a)(b)(c) | **不進** —— must_carry 之效力為「強制入 prompt context」（R-U35 (b)），非強制入 ER；該表內容屬 11.4 | 1 條（TC-014）|

**餘數驗證**：16 條中受上列影響者 {TC-009, TC-012, TC-014, TC-016} ＋
全批適用者 2 項（#2／#3）；**無第 7 項未列。**

### 5.4 §7 負向配對之三個候選（**未生成，具名列出**）

canon §7 要求列舉式支援項須配負向。本批有三處符合其形態而**未配**：

| leaf | 正向已生成 | 應配之負向 | 為何未生成 |
|---|---|---|---|
| `PROF-021-01`（5.2）| 達上限時按鈕消失 | 刪除後按鈕回復 | 取樣單位為 16 leaf，該行為屬 5.2 之另一 leaf |
| `PROF-111`（11.4）| 非 R1 High 有資訊按鈕 | **R1 High 無資訊按鈕**（條文明載）| 同上；此條之負向就在同一節之同一句內，**最接近該補** |
| `PROF-053`（6.4.1）| 無連網 → PU0585 | 有連網 → 登入畫面 | 屬 6.4 之另一 leaf |

**建議**：`PROF-111` 之 R1 High 反面於第一批正式批次補上。

### 5.5 生成中發現之三項缺陷（**皆非 TC 本身之錯**）

| # | 發現 | 判性質 | 處置 |
|---|---|---|---|
| 1 | `feature.yaml` 之 `lint.popup_ids` = **20 個**，係 **xlsx 側**量得（其自述量測條件即為 Description 欄）；以 `pdf_text` 現測為 **21 個**，多的是 **`PU0609`** —— 它正落在 9.8 之掉句裡 | **defect（判讀基準不一致）** —— 以 xlsx 側清單檢查以 PDF 側生成之 TC，**必然誤報** | lint 改為**現測 `pdf_text`**；`feature.yaml` 之值**不動**（它是有量測條件的紀錄，其條件當時為真）。差異具名待裁 |
| 2 | 9.8 之 PU0609 句在 037 **無對應 leaf** | **上游覆蓋缺口**（形態同 DR #3／Comfort R-C16）| 未代測，具名上報 |
| 3 | `lint_variant_labels.variant_of()` **不處理否定** —— TC-013 之 pre-condition 為「the vehicle is **not** an R1 High variant」，卻被判為 R1 High | **note**（本批無害：該 TC 未含禁用字串）| **本輪未改** —— 過度適用之方向是安全的，但日後對非 R1 High 之 TC 會誤報。具名待裁 |

### 5.6 lint 判準本輪改過三次（**皆改判準，不改案例**，R-U37）

| 閘 | v1 之錯 | v2 |
|---|---|---|
| **G6** pre-condition | 整行掃動詞字樣 → 對「The Profile setup flow **is open** at Step 2 “**Enter** a username”」轉紅。那行寫的是狀態，`open` 是形容詞、`Enter` 在引號內 | 只在**句首**（編號後）認祈使動詞；另保留 check/confirm/verify 之全行比對 |
| **G2** tc_id | 驗「以檔案順序讀出之 tc_id 遞增」—— 但檔案順序是檔名序（`…-070` 排在 `…-073-01` 前），號碼卻依取樣序指派 → **驗錯了對象**，canon §10.3 管的是指派 | 驗真正的不變量：**不重複且自 001 起連續** |
| **G14** PU id | 以 `feature.yaml` 之 20 個定值為全集 → PU0609 誤報 | **現測 `pdf_text`**（見 §5.5 第 1 項）|

**G2 之對照案例隨判準更換**：原案例「tc_id 倒序 → 紅」測的是 v2 刻意不管的性質，
**留著只會逼判準倒退**，故換為 v2 真正該抓的兩種：**重複、跳號**（兩者皆已證其紅）。
G6 之誤報案例留作**回歸案例**（現為範圍向之一，須綠）。

---

## 6. 16 條 TC 全文

> 每條之 `test_group` 皆為 `User Profiles`；`test_item` 依 R-U6 等同 `tc_title`；
> `estimated_test_time` 全批留空（未裁其估法）；`split_flag` 全批 false。

### NR1L-UserProfiles-001 — SWE1-HMI-PROF-001-01（4.1 / Preference Storage）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile-linked preferences stored and recalled per Driver Profile |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle<br>2. The features carrying the preferences under test are available for the vehicle and the region |
| input_test_data | Preferences under test: Cluster Home screen (3.1), SiriusXM 360L Listener Profile (3.2), Nav Saved destinations (3.4) |
| test_procedure | 1. Activate Driver Profile A<br>2. Set the three preferences listed in Input Test Data to values different from their current ones<br>3. Record the values set in step 2<br>4. Activate Driver Profile B, then activate Driver Profile A again<br>5. Read the three preferences and check that they match the values recorded in step 3 |
| expected_result | 1. Driver Profile A is active<br>2. The three preferences accept the new values<br>3. The values set in step 2 are recorded<br>4. Driver Profile A is active again<br>5. The three preferences match the values recorded in step 3 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.1<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.1<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.2<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.3<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.4<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.5 |
| priority | P0 — 偏好之儲存與回復 —— R-U5 核心五類之一 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| functional_safety / remarks | NA ／ （空） |

**reasoning**：驗證目標：4.1（PRACC1）要求系統對每個 Driver Profile 分別儲存並回復其 profile-linked preferences，本 TC 以「設值 → 切走 → 切回 → 讀回」驗其儲存與回復。關鍵情境條件：受測之三項偏好取自 PLP 表 3.1／3.2／3.4 之逐字列項，非自擬（§8.4.1）；條文之「feature 不可用則忽略」以 pre-condition 限定為該三項在本車與本區域可用。為什麼這樣切：037 對 4.1 切出三個 leaf，本 leaf（-01）之單位為「儲存與回復」，一葉一 TC（§8.2.1），未合併未拆分。刻意略過：-02（啟用時回復）與 -03（不可用之項目跳過）之行為由該二 sibling leaf 承擔，本 TC 不代測。

### NR1L-UserProfiles-002 — SWE1-HMI-PROF-002-03（4.1.1 / Preference Storage）
| 欄 | 值 |
|---|---|
| tc_title / test_item | PU1088 displayed when default restoring is not confirmed |
| pre_conditions | 1. A Driver Profile is active<br>2. The TBM confirmation path can be interrupted on the test bench |
| input_test_data | Fault injected: the completion confirmation from HU or TBM is withheld |
| test_procedure | 1. Open the vehicle settings and select “Restore Settings to Default”<br>2. Press “Yes” in PU_0118 to confirm the restore<br>3. Withhold the completion confirmation from HU and TBM<br>4. Read the popup shown on the head unit and check that PU1088 is displayed |
| expected_result | 1. PU_0118 is displayed<br>2. PU1087 is displayed<br>3. The head unit does not receive the completion confirmation<br>4. PU1088 is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_4.1.1 |
| priority | P2 — 回復預設之未確認分支；非主路徑，037 先驗 Low |
| design_method | 基礎故障注入 (Fault Injection Lite) |
| functional_safety / remarks | NA ／ PU1087／PU1088 之 popup 內文未載於 spec（DR #4）—— 本 TC 僅驗其是否顯示，不寫內文（R-U15／R-U27） |

**reasoning**：驗證目標：4.1.1（PRACC1.2）之未確認分支 —— HU 或 TBM 未確認完成回復預設時顯示 PU1088，本 TC 以注入「不回覆確認」驗之。關鍵情境條件：須先走完 PU_0118 之 Yes 與 PU1087，故該兩者列為前段 ER；缺的只是確認訊號，屬可模擬之故障（§12 首匹配 → 基礎故障注入）。為什麼這樣切：037 對 4.1.1 切出之 -03 專指未確認之分支，成功回復之路徑屬 -01／-02，本 TC 不代測。刻意略過：**PU1088 之 popup 內文不寫**（R-U27）—— spec 給了觸發條件但未給內文，寫出來即造值（§8.4.1）；DR #4 待答。

### NR1L-UserProfiles-003 — SWE1-HMI-PROF-021-01（5.2 / Profile List）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Add New Profile removed at the five-Profile maximum |
| pre_conditions | 1. Four Driver Profiles exist on the vehicle<br>2. A Valet Mode Profile is present on the vehicle |
| input_test_data | Driver Profile count: 4 (below the maximum) → 5 (at the maximum) |
| test_procedure | 1. Open the Profile List and read the Add New Profile button<br>2. Create one more Driver Profile so that five Driver Profiles exist<br>3. Open the Profile List and check that the Add New Profile button is not present and the maximum-reached text is displayed |
| expected_result | 1. The Add New Profile button is present while four Driver Profiles exist<br>2. The fifth Driver Profile is created<br>3. The Add New Profile button is not present, the icon and the string described in note PRACC7.2 are not present, and “Max Profiles reached. Delete to create a new one.” (PU0584) is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.2 |
| priority | P1 — profile 建立之上限邊界 —— R-U5 定邊界為 P1 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| functional_safety / remarks | NA ／ （空） |

**reasoning**：驗證目標：5.2（PRACC8）之上限 —— 五個 Driver Profile 為邊界，達到時 Add New Profile 按鈕與 PRACC7.2 之圖示字串消失並改顯 PU0584。關鍵情境條件：以 4 個為基準線、第 5 個為邊界值，同一 TC 內取前後兩讀（§5.6），故 design method 為邊界值分析。為什麼這樣切：Valet Mode Profile 不計入該五個之內，其存在列為 pre-condition 而非受測項，避免把兩個計數混為一談。刻意略過：刪除既有 profile 後按鈕是否回復，屬 5.2 之其他 leaf。

### NR1L-UserProfiles-004 — SWE1-HMI-PROF-032（5.9 / Profile List）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Preferences saved without pressing memory seat controls |
| pre_conditions | 1. A Driver Profile is active<br>2. The vehicle is equipped with memory seat hard and soft controls |
| input_test_data | NA |
| test_procedure | 1. Activate Driver Profile A<br>2. Change a Profile-linked preference without pressing the memory seat set or save hard or soft control<br>3. Switch the ignition off and on<br>4. Read the changed preference and check that it retains the value set in step 2 |
| expected_result | 1. Driver Profile A is active<br>2. The preference accepts the new value and no memory seat set or save control is pressed<br>3. The vehicle completes the ignition cycle<br>4. The preference retains the value set in step 2 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_5.9<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.1<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.2<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.3<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.4<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_3.5 |
| priority | P0 — 偏好之自動儲存 —— R-U5 核心五類之一 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| functional_safety / remarks | NA ／ （空） |

**reasoning**：驗證目標：5.9（PRACC15）—— 儲存 Driver Profile linked preferences 不需按記憶座椅之 set／save 控制，且會自動存於車端。關鍵情境條件：其可驗形態為「不做那個動作也要存得住」，故以 ignition cycle 後讀回作為「已存於車端」之觀察點（Service B 群，R-U21）。為什麼這樣切：本 leaf 只斷言儲存不依賴該控制，記憶座椅位置本身之回復屬 3.5 之 PLP 項目與其對應 leaf，不在此測。

### NR1L-UserProfiles-005 — SWE1-HMI-PROF-048（6.2.1 / Defaults）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Default Profiles remain after a new Profile is created |
| pre_conditions | 1. The vehicle carries its default Profiles, including Driver 1<br>2. No default Profile has been customized or deleted |
| input_test_data | NA |
| test_procedure | 1. Open the Profile List and record the default Profiles present<br>2. Create a new Driver Profile without customizing any default Profile<br>3. Open the Profile List and check that the default Profiles recorded in step 1 are still present |
| expected_result | 1. The default Profiles, including Driver 1, are recorded<br>2. The new Driver Profile is created and no default Profile is customized<br>3. The default Profiles recorded in step 1 are still present |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.2.1 |
| priority | P2 — 預設 profile 之存續條件；輔助行為 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| functional_safety / remarks | NA ／ （空） |

**reasoning**：驗證目標：6.2.1（NOPR1.1）之兩項斷言 —— 建新 profile 不需先客製化預設 profile，且 Driver 1 與其他預設 profile 會留在車上直到被客製化或刪除。關鍵情境條件：兩者為同一觸發（建立新 profile）之兩個結果，依 §5.7 併於一條 TC 之兩條 ER，不拆。為什麼這樣切：以步驟 1 之記錄作為基準線，步驟 3 比對其存續（§5.6）。刻意略過：客製化或刪除後預設 profile 之消失，屬其反面條件，由 6.2 之其他 leaf 承擔。

### NR1L-UserProfiles-006 — SWE1-HMI-PROF-053（6.4.1 / Defaults）
| 欄 | 值 |
|---|---|
| tc_title / test_item | PU0585 shown on Get Started without vehicle connectivity |
| pre_conditions | 1. The vehicle is not equipped with connectivity |
| input_test_data | NA |
| test_procedure | 1. Open the Profile setup screen carrying the “Get Started” button<br>2. Press “Get Started” and check that PU0585 is displayed and the Connected Account Login/Register screen is not displayed |
| expected_result | 1. The “Get Started” button is displayed<br>2. PU0585 is displayed and the Connected Account Login/Register screen is not displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_6.4.1 |
| priority | P2 — 無連網配置之分支 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| functional_safety / remarks | NA ／ （空） |

**reasoning**：驗證目標：6.4.1（NOPR3.1）—— 無連網配置之車輛按下 Get Started 時顯示 PU0585，且不顯示 Connected Account 之登入／註冊畫面。關鍵情境條件：車輛配置（無連網）為條件本身，故列 pre-condition；正反兩個觀察點（顯示 PU0585／不顯示登入畫面）為同一觸發之兩個結果，併為兩條 ER。為什麼這樣切：有連網之對應行為屬 6.4 之另一 leaf，本 TC 不代測，亦不自行擴充為配置對照組。

### NR1L-UserProfiles-007 — SWE1-HMI-PROF-059-01（7.2.1 / Welcome Flow）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Large welcome popup lists active and other Profiles |
| pre_conditions | 1. Two Driver Profiles exist, each with a username, an avatar and a memory seat assignment<br>2. Driver Profile A is the active Profile |
| input_test_data | NA |
| test_procedure | 1. Activate Driver Profile A so that the large welcome popup is displayed<br>2. Read the popup and check that Driver Profile A’s username and avatar and the other available Profiles are displayed |
| expected_result | 1. The large welcome popup is displayed<br>2. Driver Profile A’s username and avatar are displayed, and the other available Profile is displayed with its avatar, username and memory seat assignment |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.2.1 |
| priority | P2 — welcome popup 之內容展示 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| functional_safety / remarks | NA ／ （空） |

**reasoning**：驗證目標：7.2.1（PRWEL2.1）之大型 welcome popup 內容 —— 現用 profile 之 username 與 avatar，以及其他可用 profile 之 avatar、username 與記憶座椅指派。關鍵情境條件：記憶座椅指派為條件式（if applicable），故 pre-condition 明訂兩個 profile 皆有指派，使該欄位確實可觀察。為什麼這樣切：條文另有「More Options 進 Edit Profile tab」與「選了別的 profile 則顯示新的 welcome popup」兩項行為，屬不同觸發，依 §5.7 不併入本 TC，由 7.2 之 sibling leaf 承擔。

### NR1L-UserProfiles-008 — SWE1-HMI-PROF-062-02（7.4 / Welcome Flow）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Welcome popup clears 30 seconds after display |
| pre_conditions | 1. The vehicle is stationary<br>2. A Driver Profile carrying a Welcome Popup is available |
| input_test_data | Elapsed time readings: 29 s, 30 s |
| test_procedure | 1. Activate the Profile so that the Welcome Popup is displayed and start a timer<br>2. Read the screen at 29 seconds without touching it<br>3. Read the screen at 30 seconds and check that the Welcome Popup is cleared |
| expected_result | 1. The Welcome Popup is displayed and the timer is started<br>2. The Welcome Popup is still displayed at 29 seconds<br>3. The Welcome Popup is cleared at 30 seconds |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_7.4 |
| priority | P2 — welcome popup 之逾時清除；輔助行為之邊界 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| functional_safety / remarks | NA ／ （空） |

**reasoning**：驗證目標：7.4（PRWEL4）之三個清除條件中之逾時條件 —— 無其他動作時 Welcome Popup 於 30 秒後清除。關鍵情境條件：條文為「行車中／30 秒／使用者觸碰，三者先到者為準」，故 pre-condition 令車輛靜止、步驟 2 明訂不觸碰，把另外兩個條件排除，使 30 秒確為本次之生效條件。為什麼這樣切：29 秒與 30 秒兩讀構成邊界前後（§5.6），故取邊界值分析；行車中清除與觸碰清除屬 7.4 之其他 leaf，本 TC 不代測。

### NR1L-UserProfiles-009 — SWE1-HMI-PROF-073-01（8.7 / Setup Flow）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Keyboard blocks input beyond 12 username characters |
| pre_conditions | 1. The Profile setup flow is open at Step 2 “Enter a username” |
| input_test_data | Username input: 11 characters → 12 characters → one further character |
| test_procedure | 1. Type 11 characters into the username field and read the field<br>2. Type the 12th character and read the field<br>3. Type one further character and check that the username field still shows 12 characters |
| expected_result | 1. The username field shows the 11 characters typed<br>2. The username field shows 12 characters<br>3. The username field still shows 12 characters and the further character is not accepted |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.7 |
| priority | P1 — username 長度上限邊界 —— R-U5 定邊界為 P1 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| functional_safety / remarks | NA ／ spec 8.7 寫 “~12 characters”（約），037 leaf 寫 12 —— 本 TC 取 12（較窄之解讀，且 037 為單位權威） |

**reasoning**：驗證目標：8.7（NEWPR6）之 username 長度上限 —— 達上限後鍵盤不再接受輸入。關鍵情境條件：以 11／12／13 三讀構成邊界前後（§5.6），故取邊界值分析；spec 之「~12」為近似寫法，037 leaf 明寫 12，本 TC 取 12 並具名記於 remarks。為什麼這樣切：同節另有「最少 1 字元、未輸入前 Next 不可用」與「可含空白且空白計入長度」兩項，屬不同輸入條件，由 8.7 之 sibling leaf 承擔。

### NR1L-UserProfiles-010 — SWE1-HMI-PROF-070（8.4.1 / Setup Flow）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Profile saved after username and avatar are entered |
| pre_conditions | 1. The Profile setup flow is open at the username step |
| input_test_data | NA |
| test_procedure | 1. Enter a username in the Profile setup flow<br>2. Choose an avatar<br>3. Switch the ignition off and on, then open the Profile List and check that the Profile carrying the username and avatar from steps 1 and 2 is listed |
| expected_result | 1. The username is accepted<br>2. The avatar is selected<br>3. The Profile List lists the Profile with the username and avatar entered in steps 1 and 2 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_8.4.1 |
| priority | P0 — profile 建立之儲存 —— R-U5 核心五類之一 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| functional_safety / remarks | NA ／ （空） |

**reasoning**：驗證目標：8.4.1（NEWPR3.1）—— 輸入 username 並選定 avatar 後系統儲存該 profile。關鍵情境條件：「已儲存」之可觀察形態取 ignition cycle 後仍列於 Profile List（Service B 群之設定 → key cycle → 讀回，R-U21），不以畫面停留與否推定儲存。為什麼這樣切：setup flow 之前後步驟（Get Started、記憶座椅指派等）屬 ch8 之其他 leaf，本 TC 只驗儲存這一件事。

### NR1L-UserProfiles-011 — SWE1-HMI-PROF-091-01（9.3.2 / Editing）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Restricted Profile action interrupted when vehicle starts moving |
| pre_conditions | 1. The vehicle is an R1 High variant<br>2. The vehicle is stationary on a test track and can be brought into motion |
| input_test_data | NA |
| test_procedure | 1. Open the Edit Profile tab and start editing the Profile username<br>2. Bring the vehicle into motion<br>3. Read the screen and check that the previous available page is displayed with the bonk tone and the restriction message |
| expected_result | 1. The username editing page is displayed<br>2. The vehicle is in motion<br>3. The previous available page is displayed, the bonk tone is played, and “Function not available while vehicle in Motion.” is displayed |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3.2<br>Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.3.1 |
| priority | P1 — 行車限制之中斷分支；037 先驗 High |
| design_method | 狀態轉換 (State Transition Testing) |
| functional_safety / remarks | NA ／ R1 High 之 label 為 Connected Account —— spec 9.3.2 之變體覆寫（PDF p14，xlsx 側掉句），R-U35 (c)／§8.7.3 |

**reasoning**：驗證目標：9.3.2（EDPR3.2）—— 使用者正在進行受限項目時車輛轉為行進，系統須返回前一個可用頁面並播 bonk 與顯示訊息。關鍵情境條件：受測之受限項目取「編輯 username」一項即足以觸發，其判準為車輛由靜止轉入行進之狀態轉換（§12 首匹配 → 狀態轉換）。為什麼這樣切：訊息字串「Function not available while vehicle in Motion.」出自 9.3.1，條文以「the message specified above」指之，故 specification_reference 併列 9.3.1（§10.7），非自擬。刻意略過：9.3.1 之「行進中選取受限項目」為另一觸發（選取 vs 進行中），由該 leaf 承擔；本 TC 之字面值依 R-U35 (c) 用 Connected Account。

### NR1L-UserProfiles-012 — SWE1-HMI-PROF-104（9.8 / Editing）
| 欄 | 值 |
|---|---|
| tc_title / test_item | More Settings opens My Profile without a back button |
| pre_conditions | 1. A Driver Profile is active<br>2. The Profile section is reachable from the vehicle menu |
| input_test_data | NA |
| test_procedure | 1. Open the Profile section and press the vehicle “More Settings” button<br>2. Read the displayed page and check that the “My Profile” Settings section is displayed without a back button to the Profile section |
| expected_result | 1. The “My Profile” Settings section is displayed<br>2. No back button to the Profile section is present on the “My Profile” Settings section |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_9.8 |
| priority | P2 — 設定入口之導向；輔助功能 |
| design_method | 功能測試 (Functional based ; no specific technique) |
| functional_safety / remarks | NA ／ 9.8 之 PU0609 句（設定變更時提示已對現用 profile 變更）在 037 無對應 leaf —— 未納入本 TC，已列上繳 13 之覆蓋缺口 |

**reasoning**：驗證目標：9.8（EDPR9）—— More Settings 直接連往 My Profile 設定區，且進入後不提供返回 Profile 區之返回鍵。關鍵情境條件：兩項為同一觸發之兩個結果，依 §5.7 併為一條 TC 之兩條 ER。為什麼這樣切：同節尚有一句「設定變更時以 popup 提示已對現用 profile 變更（PU0609）」—— 該句為 xlsx 側掉句（補句表 must_carry），其觸發為「變更設定」而非「按 More Settings」，屬不同觸發（§5.7），且 037 未為其切出 leaf。本 TC 不代測，該缺口具名上報。

### NR1L-UserProfiles-013 — SWE1-HMI-PROF-111（11.4 / Connected Account）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Info icon opens the Local vs Connected Profile screen |
| pre_conditions | 1. The vehicle is not an R1 High variant<br>2. The vehicle is not a China-market vehicle<br>3. A Driver Profile is active and the Edit Profile tab is available |
| input_test_data | NA |
| test_procedure | 1. Open the Edit Profile tab and read the Connected Account item<br>2. Select the info icon next to Connected Account and check that the Local vs Connected Profile screen is displayed |
| expected_result | 1. An info icon is displayed next to Connected Account<br>2. The screen titled “What are the benefits of creating an Connected account?” is displayed with two columns labeled Connected account and Local Profile, showing “Synchronize your profile between multiple vehicles. The cloud will remember your preferences” and “Create a profile specific to this vehicle. The vehicle will remember your preferences”, and the list items of Table CPA2 |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.4 |
| priority | P2 — 說明頁之內容展示；037 先驗 Low |
| design_method | 功能測試 (Functional based ; no specific technique) |
| functional_safety / remarks | NA ／ 標題之 “an Connected account” 為 spec 原文（含冠詞誤用），逐字照錄不修（§8.4.1） |

**reasoning**：驗證目標：11.4（CPA2）—— Edit Profile tab 之 Connected Account 旁資訊圖示開啟 Local vs Connected Profile 畫面，其標題、兩欄與各欄說明文字。關鍵情境條件：條文首句明載本註記不適用於 R1 High，另有星號註記載中國市場不顯示本內容，兩者皆列 pre-condition 之排除（§8.7.3）。為什麼這樣切：Table CPA2 之列項為本畫面之內容來源（補句表 must_carry，PDF p17），ER 以「Table CPA2 之列項」指之，不自行改寫其項目文字。刻意略過：**R1 High 無此資訊按鈕之反面情形未生成** —— pilot 之取樣單位為 16 leaf，加測即擴張範圍（§8.4.2），已具名上報。

### NR1L-UserProfiles-014 — SWE1-HMI-PROF-112-01（11.5 / Connected Account）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Deleted App Store app removed only for the uninstalling user |
| pre_conditions | 1. Two Driver Profiles exist on the vehicle, each with its own Connected Account<br>2. The same App Store app is installed locally for both Profiles |
| input_test_data | NA |
| test_procedure | 1. Activate Driver Profile A and record the App Store app shown in the app tray<br>2. Delete the App Store app from Driver Profile A<br>3. Activate Driver Profile B, open the app tray and check that the app recorded in step 1 is still present |
| expected_result | 1. The App Store app is recorded in Driver Profile A’s app tray<br>2. The App Store app is removed from Driver Profile A’s app tray<br>3. The App Store app is still present in Driver Profile B’s app tray |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_11.5 |
| priority | P1 — app 刪除之範圍；037 先驗 High |
| design_method | 情境 / 用例 (Scenario / Use Case Testing) |
| functional_safety / remarks | NA ／ （空） |

**reasoning**：驗證目標：11.5（CPA3）第一句 —— App Store app 被刪除時只對執行刪除之使用者失效，其他使用者不受影響。關鍵情境條件：須跨兩個 profile 觀察同一個 app，故以「A 刪除 → 切至 B 讀回」之端到端流程驗之（§12 首匹配 → 情境／用例）。為什麼這樣切：同節之更新（對所有已安裝者生效）與安裝（只出現在安裝者之 app tray）為不同觸發，屬 11.5 之 sibling leaf，本 TC 不代測。刻意略過：補句表所載之 Table CPA2 列項（Connected Navigation 等）為 11.4 之表格內容，與本 leaf 之刪除行為無關，故未寫入 ER。

### NR1L-UserProfiles-015 — SWE1-HMI-PROF-128-01（12.9 / Valet Mode）
| 欄 | 值 |
|---|---|
| tc_title / test_item | Valet Mode deactivation cancelled on the tenth incorrect PIN |
| pre_conditions | 1. Valet Mode is active and a 4-digit PIN is set<br>2. No PIN lockout is in effect |
| input_test_data | PIN attempts: 9 incorrect attempts → 10th incorrect attempt |
| test_procedure | 1. Open the Valet Mode deactivation screen and enter an incorrect 4-digit PIN nine times<br>2. Read the deactivation screen after the ninth attempt<br>3. Enter an incorrect 4-digit PIN a tenth time and check that the deactivation is cancelled |
| expected_result | 1. Each of the nine incorrect PIN entries is rejected<br>2. The deactivation screen still accepts a further PIN entry after the ninth attempt<br>3. The deactivation is cancelled on the tenth incorrect attempt and a further PIN entry is not accepted |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_12.9 |
| priority | P0 — Valet Mode 進出 —— R-U5 核心五類之一 |
| design_method | 邊界值分析 (Boundary Value Analysis, BVA) |
| functional_safety / remarks | NA ／ 條文之「30 分鐘後可再試」需 30 分鐘等待，本 TC 只驗第 10 次即取消且當下不再受理，未驗 30 分鐘後之解鎖 |

**reasoning**：驗證目標：12.9（PVAL9）—— 錯誤 PIN 之次數上限為 10，第 10 次錯誤時系統取消該次停用程序。關鍵情境條件：第 9 次（仍可續試）與第 10 次（取消）構成邊界前後（§5.6），故取邊界值分析。為什麼這樣切：條文之 activation 與 deactivation 共用同一上限，本 TC 取 deactivation 一側，activation 一側屬 12.9 之 sibling leaf。刻意略過：30 分鐘後可再試之驗證需等待 30 分鐘，其觸發為時間到期而非第 10 次錯誤，已具名記於 remarks。

### NR1L-UserProfiles-016 — SWE1-HMI-PROF-132-02（13.2 / Valet Mode）
| 欄 | 值 |
|---|---|
| tc_title / test_item | SPAAK user blocked from exiting Valet Mode on the head unit |
| pre_conditions | 1. Valet Mode is active under the SPAAK scenario<br>2. The user at the head unit is the SPAAK user and not the vehicle owner<br>3. The owner has an authorized app or website session available |
| input_test_data | NA |
| test_procedure | 1. Open the head unit screens that offer a Valet Mode exit and attempt to exit Valet Mode<br>2. Read the screen and check that the exit is blocked and Valet Mode is still active<br>3. Deactivate Valet Mode remotely as the owner through the authorized app and check that Valet Mode is no longer active |
| expected_result | 1. Any screen or popup that would allow a Valet Mode exit is blocked (PU0934)<br>2. Valet Mode is still active after the SPAAK user’s attempt<br>3. Valet Mode is no longer active after the owner deactivates it remotely |
| specification_reference | Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_13.2 |
| priority | P0 — Valet Mode 進出 —— R-U5 核心五類之一 |
| design_method | 負向測試 (Negative / Invalid) |
| functional_safety / remarks | NA ／ （空） |

**reasoning**：驗證目標：13.2（PVALSPK2）—— SPAAK 情境下 SPAAK 使用者不得於主機退出 Valet Mode，只有車主得以 app／網站等遠端方式停用。關鍵情境條件：受測之核心為「在主機上嘗試退出」此一不被允許之操作（§12 首匹配 → 負向測試），故以嘗試被阻擋為主要觀察點。為什麼這樣切：條文之兩半（主機不得退出、車主得遠端停用）互為對照，若只驗前半則「只有車主可以」無從成立，故遠端停用列為同一 TC 之末步，而非另切一條（§5.7 之例外已於上繳具名）。刻意略過：非 SPAAK 情境下之一般 Valet Mode 退出屬 ch12 之 leaf。


---

## 7. 本包是否仍有該驗而未驗者（獨立判斷）

| # | 項 | 分類（canon §1.2）| 是否阻塞 |
|---|---|---|---|
| 1 | **`feature.yaml` 之 PU 清單為 xlsx 側** | **defect** | **不阻塞本批**（lint 已改現測），但**第一批正式批次前須裁**：是把 21 個寫回 `feature.yaml`，還是保留 20 並註明其為 xlsx 側 |
| 2 | **9.8 之 PU0609 無 037 leaf** | defect（上游覆蓋缺口）| 不阻塞；建議併入 DR #3 之形態一併處理 |
| 3 | `variant_of()` 不處理否定 | note | 不阻塞；本批已驗其無害 |
| 4 | **§7 之三個負向候選未生成** | note（範圍選擇）| 不阻塞；`PROF-111` 之 R1 High 反面建議優先補 |
| 5 | **16 條 TC 之內容正確性未經 spec 逐字複核** | —— | **這是分析層之工作**。lint 驗形狀，不驗「這句 ER 是不是那條 spec 說的」 |
| 6 | **`/tmp/sample.json` 仍是取樣清單之唯一載體** | defect（脆弱點）| `gen_pilot.py` 已把 16 個 id **內建為 `SAMPLE_IDS`** 並驗其與 `/tmp` 版一致，故生成不再依賴 `/tmp`；但 `build_batch_context --selfcheck` **仍讀 `/tmp`**。建議落為 `data/pilot_sample.tsv` |
| 7 | **`PAGE_TO_SECTION` 之 `p17 → 11.5` 未經 PDF 複位** | note | 該值來自 R-U49 之裁定，非來自對 PDF p17 之重新定位 |
| 8 | **第 7 項自檢驗「有歸宿」不驗「歸宿正確」** | note | 若 `p17` 誤填 `9.1`，該項仍會綠 |
| 9 | **`052f67d` 三案未裁** | **待 Pei** | 不阻塞生成；**但每輪成本遞增**（其後提交數 4 → 5）|
| 10 | A-UP09／R-U14（DV gate）、DR #3／#4、R-U17、N-XF01、待執行之 git 清單 | 承前 | 擋 Phase 6 寫回，不擋本批 |

**pilot 覆核之三分類**（canon §1.2）：本輪自陳之 **defect 3**（§5.5 第 1、2 項＋§7 第 6 項）、
**style-divergence 0**、**note 4**。**執行層不自裁其是否阻塞下一批** —— 上表之「是否阻塞」為建議。

---

## 8. 動作清單 —— 與 git 陳述逐項對照（R-G6）

| # | 動作 | 對象 | 是否 git |
|---|---|---|---|
| 1 | **檔案新建** | `scripts/gen_pilot.py`（16 條 TC 之單一來源）| 否 |
| 2 | **檔案新建** | `scripts/lint_tcs.py`（14 閘 ＋ 28 個 directional 案例）| 否 |
| 3 | **檔案新建 ×16** | `generated/SWE1-HMI-PROF-*.json` | 否 |
| 4 | 檔案編輯 | `scripts/build_batch_context.py`（12 輪之第 7／8 項自檢、`PAGE_TO_SECTION`、`plp_scan_union()`、`--selfcheck-tamper`）| 否 |
| 5 | 檔案追加 | `RULINGS.md`（12 輪 R-U49～R-U54）、`DECISIONS.md`（D-UP12-01／02）| 否 |
| 6 | 檔案新建 | `docs/upstream/13_pilot_generated.md`（本檔）| 否 |
| 7 | 檔案編輯 | `docs/INDEX.md` | 否 |
| 8 | 程式執行 | `gen_pilot.py`、`lint_tcs.py`（語料＋self-test）、`lint_variant_labels.py`（反向＋check）、`build_batch_context.py --selfcheck`（正向＋兩向 tamper）| 否 |
| 9 | **唯讀** | `git merge-base`／`rev-list`／`log`／`status`（§1.4 之查證）| **是（唯讀）** |

**本輪未執行任何會改變 repo 狀態之 git**：`add`／`commit`／`push`／`checkout`／
`restore`／`reset`／`rebase`／`stash`／`clean`／`rm`。**未作任何歷史改寫。**

**未動**：工作簿（**未寫回**，R-U14）、`inputs/`、`forms/`、`framework.md`、
`feature.yaml`（**§5.5 第 1 項刻意不動**）、`data/` 之任何檔、
`ANOMALIES.md`、`DATA_REQUESTS.md`、`BASELINE.sha256`、`.gitignore`、
**他 feature 之任何檔**。

### 8.1 待 Pei 之 git 指令清單（累積，**未執行**）

```
# 10 輪
git add features/user_profiles/.gitignore
git add features/user_profiles/BASELINE.sha256
git add features/user_profiles/data/outline_map.json
# 11–13 輪
git add features/user_profiles/RULINGS.md
git add features/user_profiles/DECISIONS.md
git add features/user_profiles/docs/INDEX.md
git add features/user_profiles/docs/handoff
git add features/user_profiles/docs/upstream
git add features/user_profiles/scripts
git add features/user_profiles/generated
```

（10 輪三行之標的已於 `f653cb0` 隨 pathspec 一併入版控 —— 該次係依 Pei
11 輪後之明確指示執行，已記於上繳 12 §7.1。此處保留原清單以維持紀錄完整。）

---

