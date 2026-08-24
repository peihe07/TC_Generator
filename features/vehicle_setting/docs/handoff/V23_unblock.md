# V23 — 收束：R-VF59 定案、前置解除、pilot #1 一次重生成

下放包 **V23**。對應上繳：`docs/upstream/V23_*.md`。
本包新增 **R-VF68**（1 條）、**W-VF61**（1 項工單），
並**撤銷或降級 V22 之三項工單**。

**本包所據之最新上繳**：`docs/upstream/V19a_pilot_collision_report.md`，
實測於 2026-08-24。

**Pei 於 2026-08-24 告知**：V19a 所報之「併行 session」係**貼錯 session 所致**，
非兩條分析線並行。**A-VF20 與 R-VF66 之情境描述據此更正**（見 §3）。

---

## 1. R-VF68 —— `specification_reference` 定案；R-VF59 撤銷

```
R-VF68（VF230 之 specification_reference，分析層裁定 2026-08-24）

**R-VF59 撤銷**（非暫停）。其依據為 Part 1 之**表面字串形態**，
未查該字串之來源欄位，類比基礎不可靠。

**定案形態**：依 **R-VS33′** 之錨鏈 —— 037 之 `Source Requirement ID`
→ `Basic Report` 之來源需求項目 ID。

VF230 之 SYS2 缺件（DR-28），**以 `inputs/` 內既有之
`FM-WI-FSM-035-A02_…_SYSRA_VF230_V4_Released.xlsx` 之 `Basic Report`
為錨鏈末端**。

**此非素材補入**（該檔已在 `inputs/`，非新增），
**亦非新設先例** —— A-VS134 已認可其與 SYS2 同型且涵蓋 037 全部 745 列。
其為既有素材之取用選擇，屬分析層自裁。

**得出之形態**：`VF230_V1_{PHDCC27|PDT27}_VF_{n}`，實測 10/10 全解。

**DR-28 覆文到達後**：若 SYS2 之 `Basic Report` 與 035 之值不同，
依 R-VF18 之分類處理 —— 已交付者不追改，其後之產出改用 SYS2。
**該差異須於 DR-28 覆文時實測，不預設其相同。**
```

---

## 2. 前置解除

V22 §8 之工單逐項處置：

| 工單 | 處置 |
|---|---|
| **W-VF58** 兩版比對 | **撤銷第 2 項**（逐欄比對）—— pilot #1 既為一次重生成，
舊版無比對價值。**第 1、3、4 項併入 W-VF61** |
| **W-VF59** 錨鏈查證 | **結案** —— 由 R-VF68 定案，不需另行查證 |
| **W-VF60** 工單鎖實作 | **降級**，見 §3 |
| **W-VF54** 十條修正 | **併入 W-VF61**，不單獨執行 |

**R-VF67 之「三事齊備」現已齊備**：
選池序（R-VF64 甲案，三個 ` M` 檔即其產物）／
`specification_reference`（R-VF68）／修正項（V20 §10 之 W-VF54 各項）。
**得逕行重生成。**

---

## 3. R-VF66 之降級

**A-VF20 之情境更正**：非兩條分析線並行，而是同一工單被貼入兩個 session。

**保留第一項**（零成本，且與成因無關）：

```
接任何工單前，先查 `docs/upstream/` 是否已有對應包。
有者即為已完成，不得重做；欲重做須先回報。
```

**撤銷第二項**（`CROSSLINE.md` 之「作業中宣告」節）——
其為對「持續並行」之防護，而實情為單次誤貼，儀式成本高於收益。

**第三項降為選作**（handoff 有而 upstream 無之 WARN 檢查）——
其仍有價值（可發現遺漏之上繳），但不阻塞，日後併入檢查點時再作。

**A-VF17／A-VF18／A-VF19 之成立不受本節影響**，仍須落檔。
**A-VF20 改記為「單次誤貼所暴露之缺口」**，不記為結構性問題。

---

## 4. W-VF61 — pilot #1 一次重生成（**本輪唯一工單**）

### 4.1 前置（各一行回報即可，不需另立報告）

1. 確認 **R-VF63–R-VF68** 之落檔狀態，未落者補落。
2. 落檔 **A-VF17／A-VF18／A-VF19／A-VF20**（A-VF20 依 §3 改記）。
3. **A-VF13 之「pilot 批」一語改指**其原始發現脈絡（新池首不含其所舉變體）。
4. 開立 **A-VF18 之 DR**（查 `DATA_REQUESTS.md` 最大已用號；狀態未送出）。

### 4.2 重生成

**檔名 `generated/vf230_pilot1.json`**（沿用，不用 `batch01`）。
池首 10 條依修正後之選池序（**全為 P0**）。

**逐項套用**：

| 項 | 依據 |
|---|---|
| Pre-Condition | **移除系統預設**；menu 之開啟改為 procedure 步驟；procedure ↔ ER 之 1:1 重驗（V20 §3） |
| `priority` ／ `reasoning` | 依**實際所屬之 P0 類別**（P0(a)／P0(c)）逐條具名，**不得套版**（V20 §2、R-VF64） |
| `specification_reference` | R-VF68 之形態 |
| 值域來源 | R-VF60 之 `0-CLAUSE`，引條文逐字片段 |
| `tc_title` | 區辨 token 須為實測值（如 `Not Present` 而非 `absent`） |
| `not clear` leaf | R-VF15，於書寫時帶入 Remarks |

**`LaneSenseWarning-014`（A-VF18）之處置**：其條文第 4 句與結論句所指之
feature 不同。**以結論句為準**（結論句為該需求之處置條款），
於 Remarks 具名該不一致與其 DR 編號。**不得自行調和二者。**

### 4.3 自檢

沿用 V19 §5.3 六項，**並增二項**（V20 之二 blocking defect 即此二項未被涵蓋）：

```
7. Pre-Condition 無系統預設、無以受測 feature 之可達性為前提
8. 每條之 priority 值與 R-VF57 之簇集合一致，且 reasoning 具名之類別與之相符
```

**逐條回報 10 條之 leaf id／Test Set／Priority 類別／writable，然後生成。**
**不生成第 2 批。**

---

## 5. 給 Pei

三個 ` M` 檔（`vf230_wvf45_priority.py`／`_vf230_priority.json`／
`vf230_priority_batches.md`）為 R-VF64 所採之正確版本，建議提交：

```bash
cd /Users/peihe/Work_Projects/TC_Generator
git add features/vehicle_setting/scripts/vf230_wvf45_priority.py \
        features/vehicle_setting/data/_vf230_priority.json \
        features/vehicle_setting/docs/reports/vf230_priority_batches.md
git commit -m "fix(vehicle_setting): correct VF230 pool ordering to P0>P1>P2 per R-VS58"
```

三個 `.HEAD_V19` 旁檔與 `generated/vf230_batch01.json`、
`scripts/vf230_wvf53_pilot.py` **現可刪**（比對已撤銷）——
惟 `vf230_wvf53_pilot.py` 之六項機器自檢有沿用價值，
**建議保留該腳本，僅刪其產物**。

**待你裁者僅一項**：A-VF18 之 DR 送出（R-VF27，送出屬你）。
素材代用已由 R-VF68 收於分析層自裁，**不再列為待裁**。

---

## 6. 本包產生之新條文清單（自檢）

| 編號 | 型別 | 區塊 |
|---|---|---|
| R-VF68（`specification_reference` 依 R-VS33′ 錨鏈；035 代 SYS2；R-VF59 撤銷） | 分析層裁定 | ✅ §1 |

**條文變更**：R-VF59 **撤銷**；R-VF66 **降級**（保留第一項，撤銷第二項，
第三項降選作）；A-VF20 **改記**為單次誤貼所暴露之缺口。

**工單**：W-VF61（pilot #1 一次重生成，**本輪唯一**）。
**撤銷／結案**：W-VF54（併入）／W-VF58 第 2 項（撤銷，餘併入）／
W-VF59（結案）／W-VF60（降級）。

**分析層本輪之錯**：V22 就一次誤貼建立了三層防護與四項工單，
**處置之量級高於事件之量級** —— R-VF58 之同型（以新理由撐住過重之結論）。

**執行層上繳時須附「本包是否仍有該驗而未驗者」之獨立判斷。**
