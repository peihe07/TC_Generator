# 下放包 19 —— 合併包：撤回 14–18，重排為單一執行序

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`docs/upstream/19_consolidated.md`
- **本包對交付物之推進：裁定落地 ＋ framework ＋ pilot-01 之 TC**
  （R-G31 推進聲明）
- **前置：無。本包不依賴任何未執行之包。**

---

## 一、停手正確 —— 錯在 18 包之前置聲明，錯在分析層

執行層報「18 §前置聲明為誤：14–17 皆未執行」。**屬實，且該停手正確。**

18 包檔頭寫「前置：下放包 17 已執行（framework.md 落檔、
BACKLOG.md 建立）」。**該句為分析層憑空寫下，未經任何查證。**
14／15／16 三包之檔頭我自己都寫了「其上繳未回」，17 之上繳同樣未回，
而 18 卻聲明 17 已執行。

這是 `RETROSPECTIVE.md` §二模式一（未讀就立論）**在那份檢討本身的
下一包又犯一次**。檢討寫完不等於改掉，本條記入 §六。

另：14–18 五包在四小時內連續落檔而僅 13 之上繳回覆過。
**分析層不得在上繳未回時連續發包** —— 條文見 §六 R-G32。

### 1.1 執行層所列四項具體不符 —— 逐項採認

| # | 執行層之指摘 | 判定 | 本包之處置 |
|---|---|---|---|
| 1 | 引用 9 條未抄錄之條文 | **成立** | §二之執行序恢復逐包抄錄與核對表 |
| 2 | Pop Up List 未入 `feature.yaml`／`reference:`，而其值直接進 TC | **成立** | §二 步驟 4（原 15 包步驟 3），列為生成之硬前置 |
| 3 | 簽核稿之 DR 清單漏 DR-DM8 | **成立，且為分析層之疏漏** | §三之修正稿已補；見 1.2 |
| 4 | `batch_context.md` 只能照抄下放包原文 | **成立** | §二 步驟 8 改為執行層依實際素材產出，非照抄 |

### 1.2 DR 清單之修正

分析層原稿寫「開放 DR 6 項（DR-DM1…DM6），DR-DM7 已依 R-DM44 結案」。
**六項之列舉正確，但漏述 DR-DM8 之結案**，讀起來像 DR-DM8 不存在。

正確之全貌（8 項）：

| DR | 狀態 | 依據 |
|---|---|---|
| DR-DM1 / 2 / 3 / 4 / 5 / 6 | **OPEN**（6 項） | — |
| DR-DM7 | **CLOSED** | R-DM44（所求之用途已由 R-DM33 取消，非取得所求之物） |
| DR-DM8 | **CLOSED** | R-DM43（Pei 2026-08-25 裁「以訊號名稱為主」） |

執行層指出「18 §2.3 又要求 test_item 上半保留 037 之 `DISPLAY_ON`
原拼法，這兩件事需要一起看」——**兩者不衝突，且 R-DM43 條文本身已載
該區分**：R-DM43 規制的是 **Procedure 與 Expected Result**（採 `DISP_ON`），
`test_item` 上半之 verbatim 引文**不在其規制範圍**（引文改寫即失
verbatim 之性質，canon R-S4）。此與 canon R-6 之既有分寸一致。

---

## 二、執行序（14–18 五包之合併與修剪）

**14/15/16/17/18 五包之編號作廢，其內容由本節之步驟取代。**
各步驟註明其原出處，執行層自 `docs/handoff/` 讀該包之對應章節取全文。
未列入本節者一律入 `BACKLOG.md`，**本輪不做**。

| 步驟 | 內容 | 原出處 | 為何在此輪 |
|---|---|---|---|
| 1 | 建 `features/display/BACKLOG.md`，收本節末之撤回清單 | 17 §一.2 | R-G29 之載體 |
| 2 | 抄錄 **R-DM40**（`Missing referenced specs` 拆兩名） | 14 §四 | 影響簽核前之 DECISIONS 正確性 |
| 3 | 抄錄 **R-DM41／42／43／44** | 15 §三 | Q2／Q3／DR-DM8／DR-DM7 之裁定本體，TC 生成直接依賴 |
| 4 | 抄錄 **R-G26／R-G27／R-G28／R-G29／R-G30／R-G31** 入 `RULINGS_LEDGER.md` | 14 §四、`docs/RETROSPECTIVE.md` §四 | 全域；R-G29/30/31 界定本輪之作法本身 |
| 5 | 依 R-DM40 拆分 `DECISIONS.md` 該項 | 14 §五.2 | 簽核前之最後一項標記整理 |
| 6 | `DECISIONS.md` 依 R-DM41／42 更新 Q2／Q3；`spec_reference` 改 `[PROPOSED]` | 15 §四.2 | 簽核之前提 |
| 7 | **Pop Up List 兩檔納入 `paths` 與 `reference:`**，重跑綁定檢查（**11 項**，附 `entries: 11`） | 15 §四.3 | **硬前置**：PU0517／PU0130 之值進 TC |
| 8 | `A-DM31` 登記（CFTS043 為 HVAC）；DR-DM3 之 Status 加註 | 15 §四.4、16 §五.5 | 追溯鏈之誠實記錄 |
| 9 | 抄錄 **R-DM45／R-DM46**；依 R-DM46 更正 `Safety attributes` 敘述 | 16 §四 | R-DM46 直接改 `DECISIONS.md` 之一項，須在簽核前 |
| 10 | **`framework.md` 落檔**（Layer 1／2／3 全文，逐字） | 17 §二 | `[PEI]` 第 2 項之內容，簽核所結 |
| 11 | **簽核轉錄**（§三之修正稿）＋ 二項複驗 | 18 §一 | Phase 4 解封 |
| 12 | `batches/pilot-01/batch_context.md` —— **執行層依實際素材產出**，非照抄 | 18 §三.2（改） | 生成之輸入 |
| 13 | **生成 pilot-01 之 TC**（範圍、值域、格式見 18 §二全文） | 18 §二 | 交付物 |
| 14 | 逐條 canon §9 自檢十七項 ＋ `lint036.py` A–N | 18 §三.3-4 | — |
| 15 | 更新 `docs/INDEX.md` | — | — |

**不寫回 036 工作簿**（18 §三.5 維持）。

### 2.1 撤回入 `BACKLOG.md`（本輪不做）

| 項 | 原出處 | 類別（R-G29） |
|---|---|---|
| 17 項交叉檢查表之逐字重建 | 14 §五.3 | B |
| 綠燈表述之補正清單 | 14 §五.4 | B |
| `popup_priority.tsv`（PDF／xlsx 詞彙比對） | 15 §四.5 | A —— 但擋 006 不擋 pilot，交付前必做 |
| `sysad_allocation.tsv` | 16 §五.3 | A —— Q2 揭露義務，交付前必做 |
| SYS3 之獨立重算 | 16 §五.2 | B |
| subprocess 成本量測 | 13 §八 | B |
| `recon_assertions` 增 `workbook_state` | 13 §三 | B（Tier 2，待 Pei） |

---

## 三、簽核轉錄稿（修正版，取代 18 §一）

Pei 於 2026-08-25 二度裁示「簽核」。`DECISIONS.md` 末之 `## Sign-off`
整段替換為：

```markdown
## Sign-off

- Reviewed by: **PeiPYHsu**   Date: **2026-08-25**
- Overridden items (list numbers): **無**
- Ruling notes: 口頭裁示「簽核」（2026-08-25），由分析層轉錄。
  轉錄範圍即下列三項 `[PEI]` 之結案；`[PROPOSED]` 各項未經修改，
  依 canon §4 生效。

### 本次簽核所結之三項 `[PEI]`

| # | 項 | 結案內容 | 內容之出處 |
|---|---|---|---|
| 1 | `spec_reference` | **`CFTS020-{7 位 ObjectID}`**，逐 leaf 之 ObjectID 於 Phase 2 查得 | 分析層提案。canon §10.7(a)；CFTS_020 本文條號 `{4820281}` 等實測為 7 位。**A-DM10b 不因此結案** —— 缺的是逐 leaf 對應，非格式 |
| 2 | `Test Set table (Part N)` | **四組**：`Operative State`／`Thermal Management`／`Pop Up Handling`／`Rear View Camera`（定義見 `framework.md`） | 分析層草案。§4.1.3 自檢已附；`Pop Up Handling` 為單 leaf，依 §4.2「genuine outlier」例外 |
| 3 | `profile [OVERRIDE] clauses` | **無 override，全採 canon 預設** | canon §1 之 `[OVERRIDE-R5]` 限 BT／Projection；§8.7.5 之 override 限 `vehicle_setting`。Display 為新 feature，不得援引他 feature 之既存制度性格式（canon §1 末句） |

> **轉錄之限定（R-DM32／R-G24）**：三項之內容皆係分析層提出，
> Pei 之「簽核」係對該提案之核可，非其自撰。三項已於同日對話中
> 逐項向 Pei 陳明。**若任一項與 Pei 本意不符，以 Pei 之更正為準，
> 本轉錄作廢重寫。**

### DR 現況（8 項，全列）

| DR | 狀態 | 依據 |
|---|---|---|
| DR-DM1 | OPEN | CFTS_009 未取得 |
| DR-DM2 | OPEN | Pop Up List 已取得，仲裁順序待 Priority Matrix 併讀 |
| DR-DM3 | OPEN | 兩度指定之檔（CFTS043 SYSRA、SYS3 SYSAD）皆不含 `SYS-RA-DISP` |
| DR-DM4 | OPEN | CFTS_013 未取得；005 之 multi-stage 因此 deferred |
| DR-DM5 | OPEN | LID 與 BHCAN2 對 `RADIO_B4`／`GW_B_5` 之配置不一致 |
| DR-DM6 | OPEN | `DSP_SK_PRSNT` vs PROXI r692 尾綴差異 |
| DR-DM7 | **CLOSED** | R-DM44 —— 所求之用途已由 R-DM33 取消，非取得所求之物 |
| DR-DM8 | **CLOSED** | R-DM43 —— Pei 裁「以訊號名稱為主」 |

### 簽核之效力

- Phase 4（TC 生成）之封鎖解除
- `recon.py` 此後對本 feature 回 `REFUSED`（已簽核之守衛，A-TM15），
  此為正常行為；如需重跑須經 Pei 另行裁示
- 不受本簽核影響者：**開放 DR 6 項**、**A-DM1**、**A-DM10b**
```

複驗二項：(a) `[PEI]` 殘留數為 **0**；
(b) `recon.py --feature features/display` 回 **REFUSED** ——
未 REFUSED 即停並回報。

---

## 四、抄錄之特別要求

本輪一次抄錄 **12 條**（R-DM40–46 七條、R-G26–31 六條中之六條），
遠多於歷輪。三項拘束：

1. 每條各自之核對表，逐字元比對，由 `transcribe_rulings.py` 產出
   （R-G20：不得謄寫）
2. **12 條之抄錄不得合併為一次比對** —— 逐條獨立，逐條各有 PASS／FAIL
3. 任一條 FAIL → 停並回報，**不續抄其餘**

---

## 五、停止條件

沿用 1–43（44–47 隨 18 包作廢，重列如下），另加：

44. 步驟 7 之綁定若非 **11/11** 或 `entries` 非 11 → 停（R-G26）
45. 步驟 11(b) 之 `recon.py` 若**未**回 REFUSED → 停
46. 任一 TC 之值找不到 18 §二.2 所列之出處 → 停，**不得造值**（§8.4.1）
47. TC 若須引用 005 之分級門檻方能成立 → 停（deferred，不在本批）
48. `lint036.py` 任一項 FAIL → 停，不自行放寬判準
49. 步驟 2–4、9 之任一條抄錄 FAIL → 停，不續抄

**全部 git 操作屬 Pei。**

---

## 六、本包新增之條文

```
R-G32（上繳未回時不得連續發包 —— 全域）
分析層於某一下放包之上繳未回前，**不得再發下一包**，
惟下列二者除外：
(a) Pei 直接裁示所觸發之包（裁定落地不受執行進度拘束）
(b) 明標「與前包並行、互不依賴」且經逐項查證確無依賴者

任何下放包之「前置」欄，其內容須為**已查證之事實**，
不得為預期或推定。查證方式須可複現（檔案存在性、上繳包編號、
`git log`），不得憑印象。

實例：14–18 五包於四小時內連續落檔，而僅 13 之上繳回覆過。
18 包檔頭聲明「前置：下放包 17 已執行」，該句未經任何查證且為誤 ——
14/15/16 三包之檔頭係分析層自己寫的「其上繳未回」。
執行層據實停手，正確。

本條為 `RETROSPECTIVE.md` §二模式一之補強 ——
該檢討寫完後之次包即再犯一次，故模式一之矯正不能只靠 R-G28
（規制提交裁決選單），須另規制**包與包之間的依賴聲明**。
```

---

## 七、上繳包要求（`docs/upstream/19_consolidated.md`）

1. 12 條之逐條抄錄核對表（各自獨立）
2. `BACKLOG.md` 全文
3. 綁定檢查 11 項輸出（含 `entries: 11`）
4. `framework.md` 落檔確認
5. 簽核轉錄後之 `DECISIONS.md` 末段全文 ＋ 二項複驗
6. `batch_context.md`（執行層產出，非照抄）
7. **pilot-01 之 TC 全文**（10 key 齊備）＋ 逐條 §9 自檢十七項
8. `lint036.py` 全文輸出
9. 未驗項分流（A／B，R-G29）
10. 建議之 commit 訊息與 pathspec（不執行）
