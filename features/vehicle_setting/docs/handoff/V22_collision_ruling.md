# V22 — 事故裁定：採甲案、R-VF59 暫停、跨 session 工單鎖

下放包 **V22**。對應上繳：`docs/upstream/V22_*.md`。
本包新增 **R-VF64–R-VF67**（4 條）、**W-VF58–W-VF60**（3 項工單）。

**本包所據之最新上繳**：`docs/upstream/V19a_pilot_collision_report.md`
（事故報告）＋ `docs/upstream/V19_pilot_start.md`，
**二者皆實測於 2026-08-24**（`read_text_file` 全文）。
`docs/upstream/` 內**無 V20／V21 之上繳** —— 已實測目錄確認。

**R-VF42 但書之履行**：V21 為純裁定落檔包，其 R-VF63 **是否已落檔於
`RULINGS.md` 尚未經確認**，列為 W-VF58 第 1 項。

---

## 1. 覆核結論：**事故報告核可。停手之處置正確。**

具名嘉許四處：

1. **停手而非自行還原。** 三個已提交檔被工作區覆寫後，執行層以
   `git show`（唯讀）保全 HEAD 版為 `.HEAD_V19` 旁檔，**兩版並存**，
   未執行任何改狀態之 git。§9 之 git 揭露表列改狀態指令 **0 次**。
2. **§8 第 4 項自承其影響無法由自身界定範圍** ——
   「若併行 session 在此期間讀取過 `_vf230_priority.json`，其讀到的是本層之版本；
   本層無法得知其是否讀過」。**知其不可知而具名之，優於給一個安心的推測。**
3. **§4.2 不主張自己對，而是列出兩案並說明乙案之代價。**
   其代價陳述精準：「把四個非警示功能標為 P0(c) safety，
   即是 R-VF57 之鑑別對所欲防之錯誤之放大版」。
4. **§6 四則 anomaly 擬編而不落檔**，理由為「寫入前須先定哪一版為準，
   否則登記簿會記到一個可能被撤回之版本」。**登記簿之潔淨優先於登記之及時。**

---

## 2. 給 Pei 之緊急事項（**先於一切**）

工作區現有三個 ` M` 檔案為事故 session 之版本：

```
scripts/vf230_wvf45_priority.py
data/_vf230_priority.json
docs/reports/vf230_priority_batches.md
```

**若併行 session 執行 `git add -A` 或不帶 pathspec 之 commit，
此三檔會被一併提交。** 請儘速處置。

**依 §3 之裁定（採甲案），此三檔之內容為正確者**，故建議：

```bash
cd /Users/peihe/Work_Projects/TC_Generator
git status --short          # 先看，確認只有這三個 M 與若干 ??
```

確認後擇一：

- **保留（建議）**：`git add features/vehicle_setting/scripts/vf230_wvf45_priority.py \
  features/vehicle_setting/data/_vf230_priority.json \
  features/vehicle_setting/docs/reports/vf230_priority_batches.md`
  然後 `git commit -m "fix(vehicle_setting): correct VF230 pool ordering to P0>P1>P2 per R-VS58"`
- **暫緩**：不動，但**告知併行 session 勿用 `git add -A`**

`.HEAD_V19` 三個旁檔於處置完成後即可刪除，**惟請在 W-VF58 完成兩版比對後再刪**。

**全部 git 動作屬你，兩層皆不執行。**

---

## 3. R-VF64 —— 採甲案：修選池序，不改 Priority 標記

```
R-VF64（pilot #1 之池首取捨，分析層裁定 2026-08-24）

**採甲案：修正選池序，使 P0 為外層分割；不改 Priority 標記。**

**此非二者擇一之裁量，而是條文之遵循**：
  R-VS58 逐字「第一序 P0／第二序 P1／第三序 P2／**同序內**逐 Layer 2 輪流」
  V19 §5.1 逐字「P0→P1→P2；同序內逐 Test Set 輪流 ＋ reqid 升冪」
  R-VF57 逐字「界線自此為判準（非建議）」

乙案（將落入池首之 4 個 P1 標成 P0）**違反 R-VF57**，
且其形態正是 R-VF57 之鑑別對（`Forward Collision Warning` P0 vs
`…Sensitivity` P1）所欲防者之放大版 —— 四者皆非警示。

**A-VF17 成立**：`vf230_wvf45_priority.py` 將 Priority 併入 round-robin
之鍵，`sorted(buckets)` 一輪走遍 (P0,TS)…(P2,TS) 全部 19 個 bucket，
致 Priority 成為同層排序鍵而非外層分割。**其自身註解亦與實作不符** ——
註解寫「P0→P1→P2」。**此為 A-VF1（恆為 0 之測量）之同族：
說明與行為不符，而不符不會報錯。**

**V20 §2 之二分（(i) 生成器與條文不一致／(ii) 條文列舉不完整）
兩者皆非。實為第三種**：
  Priority **賦值**正確（priority 產物兩版皆判該四簇為 P1）
  選池**序**錯誤（致 P1 進入池首）
  **TC 生成時將 P1 誤標為 P0 並套用 P0(c) 之 reasoning**

**第三項最重**：其非排序問題，而是 **TC 內容之造值**（§8.4.1）——
priority 產物明載 P1，而 TC 欄位寫 P0 且具名一個不存在之依據。
**A-VF19 成立。**

**W-VF55 之提問由本條結案**，其第 1–3 項不需再執行。
```

---

## 4. R-VF65 —— R-VF59 暫停，其依據須重新驗證

```
R-VF65（R-VF59 之暫停，分析層裁定 2026-08-24）

R-VF59 定 `specification_reference` 為 `VF230_V1-{n}`，
其依據為「Part 1 用 `CFTS044-{7 位 reqid}`，構成規則為來源 id 去
`SYS-RA-` 前綴」。

**事故報告 §5.2 提出一條不同之路徑**：R-VS33′ 令錨鏈末端取
SYS2 `Basic Report` 之 `SYS2 來源需求項目ID`；VF230 之 SYS2 缺件（DR-28），
故改取 035 SYSRA 之 `Basic Report`（A-VS134 已認可其同型且涵蓋 745 列），
得 `VF230_V1_{PHDCC27|PDT27}_VF_{n}`，**10/10 全解**。

**二者形態不同，且本層之 R-VF59 未經 R-VS33′ 之錨鏈查證即成文** ——
本層取的是 Part 1 之**表面字串形態**，未查該字串之**來源欄位**。
**若 Part 1 之 `CFTS044-{7位}` 實取自 SYS2 Basic Report 而非 037 之
Source Requirement ID，則 R-VF59 之類比基礎不成立。**

**依 R-VF58／R-VF62 一（取得新事實時須檢驗既有結論）：
R-VF59 暫停適用，待 W-VF59 之查證後重裁。**

**暫停期間**：pilot #1 之 `specification_reference` 欄
**不得視為已定案**，重生成時暫記兩形態並標待裁。

**附帶待裁**：以 035 SYSRA 之 `Basic Report` 代 SYS2（DR-28 缺件下）
是否認可 —— 此為素材代用，**屬 Pei**（見 §7）。
```

---

## 5. R-VF66 —— 跨 session 工單鎖

```
R-VF66（工單之跨 session 宣告，分析層裁定 2026-08-24）

**A-VF20 成立**：`CROSSLINE.md`（R-VF38）所載為條文之跨線保護，
**不載工單之完成狀態**。故一個已完成之工單，對另一 session 而言
與未完成無法區分。A-VF9（併行線不知本線裁定）之**鏡像**於此發生。

**三層防護，缺一不可**：

**一、接工單前之零成本前置**
  執行層接任何工單前，**先查 `docs/upstream/` 是否已有對應包**：
  `ls docs/upstream/ | grep <包號>`。
  **有者即為已完成，不得重做**；欲重做須先回報並待裁。
  **本次事故之全部代價，由一個未執行之 `ls` 而生。**

**二、`CROSSLINE.md` 增「作業中宣告」節**
  session 開工前寫入一行：`<包號> | <工單> | <開始時間> | <session 標識>`；
  完工或停手時移除該行。
  **宣告本身不阻止衝突，但使衝突在發生時可見** ——
  第二個 session 開工前讀到該行，即知有人在做。

**三、機械檢查（併入共用檢查點）**
  `docs/handoff/` 內存在 `V{NN}_*` 而 `docs/upstream/` 內無 `V{NN}_*`，
  且 `docs/handoff/` 已有 `V{NN+1}_*` 者 → **報告該 NN 為「下放而無上繳」**。
  其為 R-VF30／R-VF42 之機械後盾（二者為程序義務，未履行不留痕）。
  **本檢查得為 WARN 而非 FAIL** —— 純裁定落檔包依 R-VF42 但書
  本即可無上繳，故其非必然為錯。

**本條同時拘束分析層**：本層續發下放包前，同受第一項之查目錄義務。
```

---

## 6. R-VF67 —— 事故期間之產物一律重生，不採用

```
R-VF67（事故產物之處置，分析層裁定 2026-08-24）

事故 session 之 `generated/vf230_batch01.json`（10 TC，全 P0）
**不予採用，亦不作廢比對價值** ——

**不採用之理由**：其 `specification_reference` 採 R-VF65 所暫停之形態；
其檔名 `vf230_batch01` 與 pilot 批之 `vf230_pilot1` 不一致，
沿用會使 batch 名之語義混淆。

**保留之理由**：其為兩版比對之唯一材料（W-VF58）。

**pilot #1 之重生成須待三事齊備**：
  1. 選池序修正後之池首確定（R-VF64，三個 ` M` 檔之處置由 Pei 定）
  2. `specification_reference` 形態定案（R-VF65 → W-VF59）
  3. V20 §10 之 W-VF54 各項修正併入
     （Pre-Condition 重寫、reasoning 依實際 Priority 類別重寫、
      tc_title 240 之區辨 token、值域來源依 R-VF60 標 `0-CLAUSE`）

**三事未齊備前不得重生成** —— 重生成三次不如齊備後一次。
```

---

## 7. 待 Pei 裁定（三項）

1. **§2 之三個 ` M` 檔案之 git 處置** —— 建議保留並提交（其內容依 R-VF64 為正確者）。
   **全部 git 動作屬你。**
2. **素材代用**：DR-28（VF230 之 SYS2）缺件下，以
   `inputs/FM-WI-FSM-035-A02_…_SYSRA_VF230_V4_Released.xlsx` 之 `Basic Report`
   代 SYS2 之 `Basic Report` 作為錨鏈末端，**是否認可？**
   （A-VS134 已認可其同型且涵蓋 037 全部 745 列；此為素材代用，屬你。）
3. **A-VF18 之 DR** —— `SWE1-VC-LaneSenseWarning-014` 條文內部不一致
   （第 4 句稱評估 `Lane_Assist` 以決定 **Cornering Lights** 之 availability，
   結論句處置之對象為 **Lane Sense Warning**）。
   **本層將開立 DR 登記；送出屬你（R-VF27）。**
   **注意其影響 pilot #1 之 seq 240** —— 該條之驗證對象因上游條文自相矛盾而不確定。

---

## 8. 工單

### W-VF58 — 兩版比對與登記簿補落（**最優先**）

1. **確認 R-VF63（V21 之 verdict）是否已落檔於 `RULINGS.md`**（R-VF42 但書）。
   未落者補落。同時確認 R-VF59–R-VF62 之落檔狀態。
2. **逐欄比對**已交付版 `vf230_pilot1.json` 與事故版 `vf230_batch01.json`
   在**前 6 條（相同 leaf）**上之書寫差異：`test_item`／`pre_conditions`／
   `test_procedure`／`expected_result`／`specification_reference`／`reasoning`。
   **此為事故報告 §8 第 1 項所具名之未驗項。**
3. 落檔 **A-VF17／A-VF18／A-VF19／A-VF20** 四則（R-VF64／R-VF66 已定其成立）。
4. **A-VF13 之「pilot 批」一語須改指**（事故報告 §8 第 2 項）——
   其所舉變體屬舊池首之第 8、9 條，新池首不含之。改為指其原始發現脈絡，
   不改其技術內容。

### W-VF59 — `specification_reference` 錨鏈之查證（R-VF65）

1. **實測 Part 1 已交付 TC 之 `specification_reference` 值**，
   並回溯其取自哪一欄：037 之 `Source Requirement ID`，
   抑或 SYS2 `Basic Report` 之 `SYS2 來源需求項目ID`。
   **不以推論作答；查無明文即逐字回報「查無」。**
2. 若為後者，**R-VF59 之類比基礎不成立**，VF230 應循同一錨鏈
   （以 035 代 SYS2，待 §7 第 2 項之裁定）。
3. 兩形態並陳，附各自之 10/10 解出率與其來源欄位逐字名稱。
4. 依 R-VF21／R-VF28 附三錨點。

### W-VF60 — R-VF66 之三層防護實作

1. 第一項寫入 `PLAYBOOK.md` 之接手／接工單流程。
2. 第二項於 `CROSSLINE.md` 增「作業中宣告」節並定其格式。
3. 第三項併入共用檢查點（WARN 級），附三錨點；
   **鑑別錨點須取 `V21`（純裁定落檔包，本即無上繳）—— 其不得被報為錯誤。**

### W-VF54 — **暫停動工**（R-VF67）

待 §7 第 1、2 項之裁定與 W-VF59 完成後，與重生成一併執行。

---

## 9. 本包產生之新條文清單（自檢）

| 編號 | 型別 | 區塊 |
|---|---|---|
| R-VF64（採甲案；W-VF55 結案；TC 內容造值為第三種成因） | 分析層裁定 | ✅ §3 |
| R-VF65（R-VF59 暫停；錨鏈須查證；暫停期間不得視為定案） | 分析層裁定 | ✅ §4 |
| R-VF66（跨 session 工單鎖三層；分析層同受拘束） | 分析層裁定 | ✅ §5 |
| R-VF67（事故產物不採用但保留比對；重生成須三事齊備） | 分析層裁定 | ✅ §6 |

**擬落之 anomaly**（由 W-VF58 第 3 項執行）：A-VF17／A-VF18／A-VF19／A-VF20。

**工單**：W-VF58（兩版比對與補落，**最優先**）／W-VF59（錨鏈查證）／
W-VF60（工單鎖實作）／W-VF54（**暫停動工**）。

**分析層本輪之錯**：R-VF59 未經 R-VS33′ 之錨鏈查證即成文，
取表面字串形態而未查其來源欄位（§4）。

**未解除之風險，須於每次上繳具名**：10 條跨線條文未受保護；
**三個 ` M` 檔案在 Pei 處置前，隨時可能被併行 session 之 `git add -A` 掃入。**

**執行層上繳時須附「本包是否仍有該驗而未驗者」之獨立判斷。**
