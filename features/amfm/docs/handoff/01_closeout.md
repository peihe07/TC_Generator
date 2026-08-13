# 下放包 01 — AMFM close-out（R14 全項簽署）

分析層 → 執行層。2026-08-13。自足包：Claude Code 不需任何 chat context。

**編號說明**：本包編為 `01` 係因 `features/amfm/docs/handoff/` 原不存在
—— AMFM 先前之往返未落檔（與 Projection `INDEX.md` 所記之 01–09 缺口同類）。
**此編號不代表 AMFM 之往返序**，僅代表本目錄之第一份落檔。目錄由分析層於
寫入本包時建立。

**簽署狀態**：Pei 於 2026-08-13 對 C1–C6（含 C4 三對之修訂建議）回覆
**「照建議」**，全數照分析層建議裁定，逐字如 §1。
**R-PV02（scaffold 前 bootstrap 下放包落點）未含在本次簽署內** —— 該項當時
未附建議選項，仍為 PENDING，本包不執行、不預設。

---

## 1. 裁決條文（逐字，可直接貼入 `RULINGS.md`）

```text
[RULING] R14 — AMFM close-out（Pei 簽署 2026-08-13，回覆「照建議」）

R14-C1  P7 追認
  實態：tag fw036-amfm-regen-v1 存在；output/ 產出檔 171,631 bytes；
        sidecar / tag annotation / shasum -a 256 實測三方逐字元相同：
        da18b5b0ca9ee5794b67a31ddd317b4a23decf9e0e88380a3717f823e45f3f22
        legacy done-region hash（ordered content, columns D..AG,
        158 rows）= 30d9e4c0719a2929；rows 158 preserved / 143 regen
        (0 placeholder) / 301 total；lint PASS - 143 TCs, 102 leaf
        files, 0 findings。
  裁：P7 已執行，追認之。補登 PLAYBOOK §6，數量一律以 bytes 表示。

R14-C2  R8 追認
  裁：R8 stands —— VR 觸發路徑不進本 workbook，003/009/025/027 四葉
      維持現狀。DATA_REQUESTS #4 關列。

R14-C3  DATA_REQUESTS #2b 拆列
  裁：主檔 4874050-…CFTSMV024_CIP_R3_O1965_Excel_Document.xls 標
      「已入 inputs/」關列；其餘 12 件 O 附件（9 件天線 DTC 表 +
      2 件交通圖示表 + 1 件內嵌註記）另立一列，Urgency Low，
      用途註明「audit 舉證用，不阻塞任何批次」。

R14-C4  duplicate_of 三對（依讀取 generated/ 原文後之修訂建議）
  C4-a  087/094 —— 維持雙 TC。
        理由：CFTS011-4942534 列舉 connected / not connected 兩個值類；
        087 驗正常狀態四項資訊完整顯示（Functional），094 驗
        not-connected 值類與換台後頻率欄位跟隨（EP）。屬 §8.3
        negative / value-class 軸，非人造差異。
  C4-b  089/095 —— 維持現況，不動 v1。
        理由：拆分本身合於 §8.2.2（4942540 綁取樣側與更新側兩件事，
        兩者為獨立部分失效），但與 090/096 依 §5.7 併為一條之處理
        不一致；不一致之根因在上游（037 對 MW 配置兩片葉子、對 AM
        與 FM 各一片）。任一側改動皆使已 tag 之 v1 需 re-issue，而
        正確切法取決於上游答覆。改以 RD-1 提問（見 R14-C4-d），
        待答覆後再決定 v2 是否統一三波段深度。
  C4-c  090/096 —— 改分類，非 duplicate_of 議題。
        理由：兩者 duplicate_of 皆為空字串，條款 id 相異
        （AM 4942536 / FM 4942545），分屬不同波段之不同 leaf，
        依 §8.2.1 本不得跨 leaf 合併。TC 側無可裁之事。
        自 PLAYBOOK §6「duplicate_of 逐對裁決」移出，改列 RD-1
        Q-AM2 item 3 之 FYI。A-AM08 residual 收斂為 087/094、
        089/095 兩對。
  C4-d  新增 RD-1 提問，併入 Q-AM2 item 3（條文見 §2.6）。

R14-C5  A-AM11 / A-AM12 / A-AM13 / A-AM14 狀態轉換
  裁：RD-1 送出當日，四條由 PENDING 轉 AWAITING_UPSTREAM；
      resolution condition = 上游回覆到達或交付期限，孰先。
      轉換由 Pei 通知送出後執行，執行層不得自行提前。

R14-C6  RD-1 送出
  裁：docs/fw036/RD1_amfm_submission.md 照現稿送出（加入 C4-d 之
      新增提問後）。送出屬 Tier 3，僅 Pei 執行。
      送前檢查已完成：四項附件齊備
        unallocated_clauses.json  features/amfm/data/（48,963 B）
        stla_id_suspects.json     features/amfm/data/（148 B，內容已驗：
                                  單筆 SWE-RA-RAD-029，declared 4872451
                                  agreement 0.036 → better 4872457
                                  agreement 0.909，即 Q-AM2 item 1 之 extract）
        family-overlap 表          features/amfm/docs/family_overlap.md
        version/hash 表            內嵌於 S2

R14-C7  量測口徑
  裁：檔案大小之陳述一律以 bytes 為單位。KB 之進位基底歧義
      （171,631 bytes = 167.61 KiB 四捨五入 / 167.60 KiB 捨去）
      為本次已發生之口徑差，記入 §5a 量測條件紀律。
```

---

## 2. 執行層作業清單

全部為文件面補登，**不觸及任何已交付內容**。逐項完成後於上繳包回報。

### 2.1 `features/amfm/RULINGS.md`

貼入 §1 全文，維持既有格式與編號慣例。**確認 R14 未與既有號碼衝突；
若已被占用，停手回報，不得自行改號。**

### 2.2 `features/amfm/PLAYBOOK.md` §6 —— P7 補登

將 P7 之 `[ ]` 改為 `[x]`，內文改寫為已完成式，記入下列數值（**逐字照抄；
若獨立重測與此處不符，停手回報，不得自行調和**）：

- 產出檔：`output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS024_Radio_20260129.xlsx`，**171,631 bytes**
- SHA256：`da18b5b0ca9ee5794b67a31ddd317b4a23decf9e0e88380a3717f823e45f3f22`
  （sidecar / tag annotation / 實測三方一致）
- legacy done-region hash（ordered content, columns D..AG, 158 rows）：`30d9e4c0719a2929`
- rows：158 preserved / 143 regen (0 placeholder) / 301 total
- lint：PASS —— 143 TCs, 102 leaf files, 0 findings
- tag：`fw036-amfm-regen-v1`
- 註明 sidecar 位於 `output/`、未入庫（根 `.gitignore:20` 排除），digest
  之權威副本存於 tag annotation —— 與 Projection R-P94 及
  `FEATURE_ONBOARDING` §6 一致

P7 尾段「Pending: Pei approval → commit → `--write` → tag …」整段移除，
改為「**RD-1 送出待 Pei（Tier 3）**」。

### 2.3 `features/amfm/PLAYBOOK.md` §6 Open PENDING —— 改寫

- **A-AM09 VR class** 條目刪除，改記一行：「R8 stands（Pei 追認
  2026-08-13, R14-C2），VR 不進本 workbook；DATA_REQUESTS #4 已關列。」
- **087/094 與 089/095 `duplicate_of`** 條目改寫為 R14-C4-a / C4-b 之裁定
  結果（維持雙 TC；089/095 待上游答覆後再議 v2）
- **090/096** 自該條目移出，改列於 RD-1 待送項目之下（FYI，非待裁）
- **A-AM11 / A-AM12 / A-AM13 / A-AM14** 四條之狀態欄加註「RD-1 送出後轉
  AWAITING_UPSTREAM（R14-C5）」，**現在不得改狀態**

### 2.4 `features/amfm/ANOMALIES.md`

- A-AM08 追加 disposition 段：三對之裁定（R14-C4-a/b/c），residual 收斂為
  087/094、089/095 兩對；090/096 移出本 anomaly 之待裁範圍，改為上游觀察
- 其餘各條保持現狀，**A-AM11–14 不得提前改為 AWAITING_UPSTREAM**

### 2.5 `features/amfm/DATA_REQUESTS.md`

- **#4**：Status 由「✅ 已入 `inputs/` — 範圍裁決待下」改為
  「✅ 已入 `inputs/`；範圍裁決 R8 stands（R14-C2, 2026-08-13）」，
  Urgency 欄由 `Medium（裁決）` 改為 `—`
- **#2b 拆為兩列**：
  - `#2b` 主檔 `4874050- 4595376- CFTSMV024_CIP_R3_O1965_Excel_Document.xls`
    → Status「✅ 已入 `inputs/`」，Urgency `—`
    （分析層實測 `inputs/` 內確有此檔 36.50 KB，另有同系列 `4874049-`
    一份 —— 兩份並存之緣由請於上繳包說明；無法說明則依 §3.3 登記
    A-AM17）
  - 新列 `#2c` 其餘 12 件 O 附件（9 件天線 DTC 表 + 2 件交通圖示表 +
    1 件內嵌註記，位於 `…/Reference Docs/CFTS024/`）
    → Status「⚠️ 未入 `inputs/`」，Urgency `Low`，
    Batch impact 欄寫「audit 舉證用，不阻塞任何批次（Diagnostics 批
    097–104 已生成、lint green、零 placeholder）」

### 2.6 `docs/fw036/RD1_amfm_submission.md` —— Q-AM2 item 3 增補

在 item 3 現有內容後追加下列段落（逐字）：

```text
   5. **Per-band leaf allocation asymmetry.** CFTS011 §1.5.5 restates the
      same sampling / display-update requirement once per band under three
      distinct ids (AM 4942536, MW 4942540, FM 4942545). The 037 allocates
      TWO leaves to the MW clause (SWE-RA-RAD-089 and -095, both declaring
      4942540) but ONE leaf each to the AM and FM clauses (-090, -096).
      Our TC side consequently carries 2 TCs for MW (display-update side
      and input-sampling side) against 1 TC each for AM and FM — the same
      clause text verified at two different depths. Please confirm whether
      the MW double allocation is a deliberate sub-division or a duplicate
      allocation. We have not changed the delivered workbook; the depth
      will be unified in the next revision once this is answered.
```

`docs/fw036/RD1_questions_amfm.md` 之 Q-AM2 亦同步追加（該檔為問題清單、
submission 為送件稿，兩處須一致）。

### 2.7 建立 `features/amfm/docs/` 往返結構

AMFM 目前僅有 `docs/handoff/`（本包寫入時建立），無 `docs/upstream/`、
無 `docs/INDEX.md`。建立之，並依 Projection `INDEX.md` 之體例撰寫
`features/amfm/docs/INDEX.md`：

- 誠實標示 **01 以前之往返未落檔**，內容之權威在
  `DECISIONS.md` / `RULINGS.md` / `ANOMALIES.md` / `DATA_REQUESTS.md`
- **不得重建歷史往返包**（重建 = 以記憶產出文件，違反 canon §5a）
- 本包（01）與其上繳包（01）登入表中

### 2.8 不做的事（明列，避免越界）

- **不**修改 `features/amfm/generated/` 任何檔案
- **不**修改 `output/` 任何檔案，**不**重跑 `write_back.py`
- **不**建立、移動、刪除任何 git tag
- **不**執行任何 git 操作（含 commit）—— **全部 git 操作屬 Pei**；
  執行層僅**準備** commit message 並列於上繳包，由 Pei 執行
- **不**改 A-AM11–14 之狀態（待 Pei 通知 RD-1 已送出）
- **不**處理 R-PV02（scaffold 前 bootstrap 落點）—— 仍為 PENDING

---

## 3. 停手條件（本包特化）

除 canon §0 六項外，另加三項：

1. `RULINGS.md` 之 R14 編號已被占用 → 停手回報，不得自行改號
2. §2.2 之任一數值與獨立重測不符 → 停手回報，**不得自行調和**
3. `inputs/` 內 `4874049-` 與 `4874050-` 兩份同系列檔之並存緣由若無法從
   既有記載說明 → 登記為新 anomaly（**A-AM17**）後繼續其餘作業

---

## 4. 上繳包要求

寫入 `features/amfm/docs/upstream/01_closeout.md`，須含：

1. §2.1–§2.7 逐項之完成狀態與實際 diff 摘要
2. §2.2 各數值之獨立重驗結果（bytes、SHA256、legacy hash、counts、lint），
   與本包所載逐項比對，相符／不符各列出
3. `4874049-` / `4874050-` 兩檔之緣由說明或 A-AM17 登記
4. 為 Pei 準備之 commit message（英文、conventional commits 格式），
   **不執行**
5. `INDEX.md` 之建立結果
6. **「本包是否仍有該驗而未驗者」之獨立判斷** —— 此項不得省略

---

## 5. 本包產生之新條文清單（自檢表）

- [x] R14-C1 P7 追認 —— §1，區塊形式
- [x] R14-C2 R8 追認 —— §1，區塊形式
- [x] R14-C3 DATA_REQUESTS #2b 拆列 —— §1，區塊形式
- [x] R14-C4-a 087/094 維持雙 TC —— §1，區塊形式
- [x] R14-C4-b 089/095 維持現況不動 v1 —— §1，區塊形式
- [x] R14-C4-c 090/096 改分類 —— §1，區塊形式
- [x] R14-C4-d 新增 RD-1 提問 —— §1 + §2.6，區塊形式
- [x] R14-C5 A-AM11–14 轉 AWAITING_UPSTREAM 之條件 —— §1，區塊形式
- [x] R14-C6 RD-1 照稿送出 —— §1，區塊形式
- [x] R14-C7 量測口徑一律 bytes —— §1，區塊形式
- [x] 新增 anomaly 編號 A-AM17（條件性）—— §3.3，區塊形式
- [x] 停手條件三項 —— §3
- [ ] R-PV02 —— **未簽署，不在本包生效範圍**，執行層不得據以行動

以上均以可直接貼入之區塊或表格形式出現，非夾敘於段落中。
