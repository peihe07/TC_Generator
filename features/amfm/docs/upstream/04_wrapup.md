# 上繳包 04 — 收束完成，凍結解除，焦點回 Privacy

執行層 → 分析層。2026-08-13。回應 `docs/handoff/04_wrapup.md` §4 之五項要求。

**一句話結論**：§2 七項全數完成，三項停手條件皆未觸發。
四 feature 之結構缺損議題已無 Open PENDING。
另發現一項下放包未涵蓋的登記缺口（R17-1 ~ R17-4 從未寫入 `RULINGS.md`），
**未自行補登**，回報待裁。

---

## 1. §2 七項完成狀態

| # | 作業 | 狀態 | 產出 |
|---|---|---|---|
| 1 | R18 全文貼入 `RULINGS.md` | ✅ | 編號未占用（現有最高 R16），停手條件 1 未觸發 |
| 2 | SXM / Home 各登一條，含實測數字，狀態 DEFERRED | ✅ | A-SX28 / A-H27 —— 見 §1.1 之作法說明 |
| 3 | A-AM18 改 DEFERRED；另登 243–310 列樣式一條 | ✅ | A-AM18 / **A-AM19**（新） |
| 4 | 移除五個 PLAYBOOK 凍結橫幅，改記常設規則 | ✅ | 五個皆換；停手條件 2 未觸發 |
| 5 | 依 R15-2 掃過五 feature 之 Open PENDING | ✅ | 見 §2 |
| 6 | R18-3 常設規則寫入 canon 草案 | ✅ | `docs/fw036/CANON_DRAFT_r16_delivery_integrity.md` |
| 7 | R18-4 反向測試 | ✅ | `tests/test_xlsx_surgical_invariant.py`，3 passed；停手條件 3 未觸發 |

### 1.1 第 2 / 3 項的作法選擇（需分析層確認）

§2.2 寫「`features/{sxm,home}/ANOMALIES.md` **各登一條**」。
上繳包 02 執行時**已各登一條**（A-SX28 / A-H27），且內容已含 R18-1 要求的
全部實測數字。本次因此**改寫既有條目的狀態與處置段，而非另開新條** ——
另開會產生兩條描述同一件事、數字相同而狀態不同的登記，正是 R15-2 想避免的
狀態混亂。若分析層原意是要獨立新條，請告知，改起來很快。

同理，A-AM19 是**真的新條**（243–310 列樣式先前只寫在上繳包 02 §7 末段，
從未進 `ANOMALIES.md`），所以照 §2.3 新增。

### 1.2 停手條件逐項

| # | 條件 | 結果 |
|---|---|---|
| 1 | `RULINGS.md` R18 編號已占用 | ✅ 未占用（`grep -c R18` 原為 0）。已貼入 |
| 2 | 某 feature 橫幅內容與 R16 所述不符 | ✅ 未觸發 —— 五個橫幅都以程式斷言檢查含 `R16-2` / `LOSSLESS` / `xlsx_surgical` 三個關鍵詞後才替換，全部通過 |
| 3 | 反向測試未能觸發 ABORT | ✅ 未觸發 —— 兩種破壞模式皆 ABORT，見 §3 |

---

## 2. §4.2 —— 五 feature 之 Open PENDING 現況

掃描口徑：`ANOMALIES.md` 之 anomaly 標題行，取標題內出現的狀態關鍵字；
`DEFERRED` / `RESOLVED` / `CLOSED` / `AWAITING` / `REGISTERED` / `RECORDED`
/ `RULED` 皆不計入 Open PENDING。

| feature | 條目總數 | Open PENDING | 本輪移出 |
|---|---|---|---|
| AMFM | 19 | **4** | A-AM18（→ DEFERRED）；A-AM19 直接以 DEFERRED 建立 |
| Home | 28 | **0** | A-H27（→ DEFERRED）|
| SXM | 30 | **2** | A-SX28（→ DEFERRED）|
| Projection | 80 | **17** | 無（A-PJ-R16 本就非 PENDING）|
| Privacy | 14 | **7** | A-PV03（→ DEFERRED）、A-PV09（→ CLOSED）|

### 2.1 逐 feature 剩餘 Open PENDING

**AMFM（4）—— 全部與結構缺損無關**
- `A-AM11` Rate-to-frequency-step mapping undefined（upstream definition）
- `A-AM12` "Intelligent entry" 未定義
- `A-AM13` Fast seek 有規格但無 037 leaf（RD-1）
- `A-AM14` Seek Up / Seek Down 上游分解不對稱

四條依 **R14-C5** 之裁定，於 RD-1 送出當日才由 PENDING 轉
`AWAITING_UPSTREAM`，且「轉換由 Pei 通知送出後執行，執行層不得自行提前」。
RD-1 尚未送出，故四條**正當地留在 Open PENDING**，非 R15-2 之標的。

**Home（0）** —— 已清空。

**SXM（2）—— 皆為真待裁**
- `A-SX11` 引用的 SEEK 工作表分類的是 Fast Seek SAT 而非 plain Seek SAT
- `A-SX13` 引用的 "Pre-defined Presets Algorithm" 是空白工作表

**Projection（17）** —— A-PJ01 / 03 / 06 / 07 / 16 / 25 / 32 / 33 / 34 /
35 / 39 / 40 / 41 / 42 / 43 / 44 / 45。全數為 Phase 2 之內容層待裁項，
與 R16/R18 無關。本包未觸碰。

**Privacy（7）—— 焦點所在**
- `A-PV01` 空白範本開工，交付形態待 Tier 2 確認
- `A-PV04` VF651_V2_R2 同名異容，基線待追認
- `A-PV05` SYSAD 誤入 `cfts_doc`，待標 context-only
- `A-PV07` 範本殘留樣本列，清除計畫待核可
- `A-PV08` Scope / Purpose / Reviewer 三格待填值
- `A-PV10` 下拉選單範圍與內容不一致
- `A-PV11` `Reference` 與 `下拉選單` 詞條字串不符

七條都是 Privacy 自身的待裁項，**沒有一條與 writer / 結構缺損有關** ——
R18-6 所要的「焦點回 Privacy」在登記層面已經成立。

### 2.2 R15-2 掃描之處置說明

本包 §2.5 寫的是「凡屬**本輪 DEFERRED** 者一律移出」。嚴格照字面，
本輪標的只有 A-AM18 / A-H27 / A-SX28（加新建的 A-AM19），皆已移出。

但條文同時說「**依 R15-2 通則**掃過」，所以我把通則套到全部 Open PENDING
上找誤標。找到**兩條**，都在 Privacy：

1. **`A-PV03`（ETM V3_R3）—— 已改**。原標
   `PENDING（R-PV01(a) 明示延後至 P2）`。R-PV01(a) 已簽署且結論即為
   「延後到 P2」，這是 R15-2 定義的「已裁而結果為延後」的教科書案例，
   標題自己都寫了「明示延後」還掛 PENDING。改為
   `DEFERRED — 待 P2 證據重驗（R-PV01(a)）`，語意未變，
   只是狀態欄不再假裝它在等裁決 —— 它等的是重驗。
2. **`A-PV09`（openpyxl 損毀範本）—— 已改為 CLOSED**。該條的建議
   「升為 canon 層條文」已被 R16 採納、再被 R18-3 落為常設規則。
   一個已經變成規則的 anomaly 不該還留在追蹤清單裡。
   交叉引用同步從 R16 更新到 R18-3。

**未動而僅回報者**：AMFM 四條（R14-C5 明文禁止執行層提前轉換）、
SXM 兩條、Projection 十七條 —— 皆為真待裁，不屬 R15-2 標的。

---

## 3. §4.3 —— R18-4 反向測試兩次輸出（原文）

實作為常駐測試而非一次性腳本：`tests/test_xlsx_surgical_invariant.py`。
理由寫在測試 docstring 裡 —— 一次性腳本驗完就消失，下次改 writer 時
沒有東西會再問這個問題。

指令：`python -m pytest tests/test_xlsx_surgical_invariant.py -q -s`
結果：**3 passed**

### 3.1 破壞模式 1 —— zip 成員集合受損（即 AMFM v1 的成因）

以 `openpyxl` 存檔路徑產生輸出，餵給 `verify_structure`：

```
[reverse test 1 — member-set damage] ABORTED:
zip member set changed — lost ['xl/calcChain.xml', 'xl/comments1.xml', 'xl/drawings/vmlDrawing1.vml', 'xl/media/image2.jpeg', 'xl/printerSettings/printerSettings1.bin', 'xl/printerSettings/printerSettings2.bin', 'xl/printerSettings/printerSettings3.bin', 'xl/printerSettings/printerSettings4.bin', 'xl/printerSettings/printerSettings5.bin', 'xl/sharedStrings.xml', 'xl/worksheets/_rels/sheet8.xml.rels'], added ['xl/comments/comment1.xml', 'xl/drawings/commentsDrawing1.vml', 'xl/media/image2.png', 'xl/media/image3.jpeg', 'xl/media/image4.jpeg', 'xl/media/image5.jpeg', 'xl/media/image6.jpeg', 'xl/media/image7.jpeg', 'xl/media/image8.jpeg', 'xl/media/image9.jpeg']. The delivered file must carry every part the customer's file carried (R16-1)
```

斷言不只檢查「有 raise」，也檢查訊息**指名了丟失的成員**
（`sharedStrings.xml`、`printerSettings1.bin`）—— 一個只說「結構變了」
而不說變在哪的 ABORT，在事故現場沒有用。

### 3.2 破壞模式 2 —— 成員集合完好，只有下拉被剝除

這一項是重點。輸出的 zip 成員集合與來源**完全相同**（測試裡有前置斷言
`set(a.namelist()) == set(b.namelist())` 把這件事釘住），唯一的損傷是
sheet6 的 `<extLst>` 被移除，即 R 欄設計方法下拉消失：

```
[reverse test 2 — data-validation damage] ABORTED:
data-validation counts changed (classic, x14): {'xl/worksheets/sheet6.xml': ((3, 2), (3, 0))}. The dropdowns are part of the controlled form (R16-2)
```

**invariant 的第一款完全看不見這個損傷** —— 每個成員都在、名字都一樣。
只有第二款（逐 sheet DV 計數）抓得到。這正是第二款存在的理由，
現在有實測支撐，不再是設計時的推測。

### 3.3 陽性對照

第三個測試 `test_surgical_output_passes` 驗證外科手術路徑的輸出
**通過** invariant，且寫入的值讀得回來。沒有這一項的話，一個
「永遠 raise」的實作會讓前兩項一起變綠 —— 那就又造出一個
「不可能失敗的檢查項」，正是 R18-4 要防的東西。

---

## 4. §4.4 —— canon 草案路徑

`docs/fw036/CANON_DRAFT_r16_delivery_integrity.md`

**檔名維持不動**：R18-3 已取代 R16-2，檔名裡的 `r16` 讀起來過時，
但上繳包 02 §1 / §5 兩處引用了這個路徑。改名會讓一份已上繳的包指向
不存在的檔。**已提交的紀錄不因後續事件而失效**，故不改名，
改在檔內開頭標明它同時承載 R16-4 與 R18-3。

本次對草案的更動：

1. 開頭加入 **R18-3 三項常設規則逐字區塊**，並註明「本草案之規則 1–3
   即為其展開版，若有出入以該區塊為準」—— 簽署條文優先於草案措辭
2. Rule 3 補上 R18-3 第 3 款（升 Tier 2、不得以放寬 invariant 解決）
3. 新增「The invariant's own test (R18-4)」一節，記兩種破壞模式與陽性對照
4. 未決事項第 2 項（凍結解除要不要入 canon）**劃掉並標為已決**：
   凍結是一次性事件，不入 canon；入 canon 的是取代它的常設規則
5. 未決事項第 3 項（回溯範圍）改寫：R18-1 已就本輪個案裁定不重產，
   但**執行層建議把它寫成通則** —— 理由是它已經被實際適用過一次，
   下次再遇到若無條文就會重新爭論一遍

草案仍是草案，**canon 本體（`FEATURE_ONBOARDING.md`）一字未動**。

---

## 5. §4.5 —— 本包是否仍有該驗而未驗者（獨立判斷）

**有，四項。其中第 1 項不是「未驗」而是「未登記」，但性質更嚴重。**

### 5.1 R17-1 ~ R17-4 是已簽署條文，卻從未寫入 `RULINGS.md`

下放包 03 §5 的自檢表把 R17-1 ~ R17-4 標為 `[x]`（已簽署），
R17-5 ~ R17-9 標為 `[ ]`（未簽署）。但 03 包 §3 只有 R17-5(b) 一項可辦，
該包**沒有產生上繳包**，於是四條簽署條文留在 handoff 檔裡，
`RULINGS.md` 裡 `grep R17` **一筆都沒有**。

四條的內容（依 03 包 §1）：R17-1 停手條文須明列標的；R17-2 子字串計數之
詞界約束；R17-3 feature 階段陳述須三源實測；R17-4 Projection 對照組
證明力限縮。**這四條本包正在遵守** —— 例如 04 包 §3 的停手條件就明列了
停手標的與續行標的（R17-1），本上繳包 §2 的掃描口徑也寫明了
（R17-2 的精神）。規則在生效，但沒有登記。

本包 §2 的七項作業沒有這一項，`不做` 清單也沒有提。
**執行層未自行補登**，回報待裁。建議補，理由是：一條在生效卻不在登記裡的
規則，下一個接手的人只能靠讀舊 handoff 才知道它存在。

### 5.2 R18-3 規則 1「唯一寫回路徑」尚未有機制保證

規則寫的是「`backend/xlsx_surgical.py` 為**唯一**寫回路徑；openpyxl 存檔
路徑不得用於任何交付件產出」。目前這是**紀律，不是機制**：
`backend/writer.py` 與 `scripts/translate_xlsx.py` 裡的 `wb.save()`
一行都沒動，仍可被呼叫。

AMFM 的 `write_back.py` 已改接外科手術路徑，Privacy 尚未寫回，
所以現況沒有暴露。但規則說的是「唯一」，而程式層沒有任何東西阻止
下一支腳本直接 `wb.save()`。要真正落實，需要一個 lint 規則或
import-time 檢查。本包未做（不在 §2 七項內），登記於此。

### 5.3 五個 PLAYBOOK 橫幅的替換未經人眼逐份確認

第 4 項是程式替換，替換前以斷言檢查了舊橫幅含 `R16-2` / `LOSSLESS` /
`xlsx_surgical` 三個關鍵詞（即停手條件 2 的機械化版本），五份全通過。
但「橫幅內容與 R16 所述相符」這個判斷，斷言只能驗關鍵詞在不在，
驗不了語意。若分析層要的是語意層的核對，那一項沒做。

### 5.4 A-AM19 的修復方向未實測

A-AM19 記了修復方向（新建列時自第 242 列繼承 `<row>` 屬性與各欄 `s=`
索引），但 R18-5 裁定不修，所以**沒有寫過一行程式去驗證這個方向可行**。
它是紙上推論。日後真要修時，不能假設它一定成立。

---

## 6. 附：本次改動清單

| 檔案 | 改動 |
|---|---|
| `features/amfm/RULINGS.md` | R18 全文 + 執行層回報（含 §5.1 之 R17 登記缺口） |
| `features/amfm/ANOMALIES.md` | A-AM18 → DEFERRED（附 R17-9 未驗標籤）；**A-AM19** 新增 |
| `features/home/ANOMALIES.md` | A-H27 → DEFERRED（附 interleaved 前置條件） |
| `features/sxm/ANOMALIES.md` | A-SX28 → DEFERRED |
| `features/privacy/ANOMALIES.md` | A-PV03 → DEFERRED（R15-2）；A-PV09 → CLOSED（R18-3） |
| 五個 `PLAYBOOK.md` | 凍結橫幅 → R18-3 常設規則橫幅 |
| `docs/fw036/CANON_DRAFT_r16_delivery_integrity.md` | 併入 R18-3 逐字條文 + R18-4 測試節 + 兩項未決事項更新 |
| `tests/test_xlsx_surgical_invariant.py` | **新增** —— R18-4 反向測試 |

**未執行**（依 §2「不做」清單）：未重產任何交付件、未打／改任何 tag、
未動 AMFM v2、未執行任何 git 操作、未實作 whole-sheet splice、
未動 canon 本體、未補登 R17-1 ~ R17-4。
