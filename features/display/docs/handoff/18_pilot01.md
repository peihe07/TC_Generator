# 下放包 18 —— 簽核轉錄、pilot-01 生成（SWE1-DM-004／005）

- 日期：2026-08-25
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`docs/upstream/18_pilot01.md`
- **本包對交付物之推進：Display 之首批 TC（R-G31 推進聲明）**
- 前置：下放包 17 已執行（framework.md 落檔、BACKLOG.md 建立）

---

## 一、簽核轉錄（步驟 1，先於一切）

Pei 於 2026-08-25 口頭裁示「簽核」。將 `DECISIONS.md` 末之
`## Sign-off` 區塊**整段替換**為下列全文，逐字，不增删：

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
| 1 | `spec_reference` | **`CFTS020-{7 位 ObjectID}`**，逐 leaf 之 ObjectID 於 Phase 2 查得 | 分析層提案（下放包 15 §四步驟 2）。canon §10.7(a)；CFTS_020 本文條號 `{4820281}` 等實測為 7 位。**A-DM10b 不因此結案** —— 缺的是逐 leaf 對應，非格式 |
| 2 | `Test Set table (Part N)` | **四組**：`Operative State`／`Thermal Management`／`Pop Up Handling`／`Rear View Camera` | 分析層草案（下放包 17 §二）。§4.1.3 自檢已附；`Pop Up Handling` 為單 leaf，依 §4.2「genuine outlier」例外 |
| 3 | `profile [OVERRIDE] clauses` | **無 override，全採 canon 預設** | canon §1 之 `[OVERRIDE-R5]` 限 BT／Projection；§8.7.5 之 override 限 `vehicle_setting`。Display 為新 feature，**不得援引他 feature 之既存制度性格式**（canon §1 末句），故無 override |

> **轉錄之限定（R-DM32／R-G24）**：第 2、3 兩項之內容係分析層於同輪
> 提出，Pei 之「簽核」係對該提案之核可；第 1 項之內容出自下放包 15
> 之提案。三項皆已於同日對話中向 Pei 逐項陳明。
> **若任一項與 Pei 本意不符，以 Pei 之更正為準，本轉錄作廢重寫。**

### 簽核之效力

- Phase 4（TC 生成）之封鎖解除
- `recon.py` 對本 feature 此後之執行將回 `REFUSED`（已簽核之守衛，
  A-TM15），此為正常行為；如需重跑須經 Pei 另行裁示
- 未結之項不受本簽核影響：**開放 DR 6 項**
  （DR-DM1／DM2／DM3／DM4／DM5／DM6；DR-DM7 已依 R-DM44 結案）、
  **A-DM1**、**A-DM10b**
```

轉錄後立即複驗二項：
(a) `DECISIONS.md` 中 `[PEI]` 之殘留數為 **0**
(b) 執行 `recon.py --feature features/display` 應回 **REFUSED**
    —— 若未 REFUSED，表示簽核守衛未生效，**停並回報**

---

## 二、pilot-01 生成範圍

| | |
|---|---|
| Test Group | `Display` |
| Test Set | `Thermal Management` |
| req_id（D 欄） | `SWE1-DM-004`／`SWE1-DM-005`（R-DM42） |
| Author | `PeiPYHsu` |
| 不入本批 | 005 之 multi-stage 分級（DR-DM4 未結）—— 於 `batch_context.md` 記為 **deferred**，**不得產出 PENDING 佔位列** |

### 2.1 預期 TC 組成（下限，非上限）

依 §8.2.2（RD sub-id ≠ TC 數）與 §8.3 之 stress-test，
**004 至少 1 條、005 至少 2 條**：

| # | leaf | 驗證目標 | 拆分依據 |
|---|---|---|---|
| 1 | 004 | 溫度達門檻 → 亮度降低 ＋ PU0517 顯示 | §5.7：同一 trigger 之多個必然後果同列一 TC，多行 ER |
| 2 | 005 | 溫度達門檻 → 顯示關閉 ＋ PU0130 顯示 | 與 #1 不同 leaf、不同 outcome |
| 3 | 005 | 溫度回落 → 顯示回復 | §8.3：觸發與回復為獨立之部分失效，分屬兩條（stress-test：只有回復失敗時，#2 之判定仍為 pass） |

生成後若自檢認為需再拆，**得增列**，於 `reasoning` 註明依據之 § 節。

### 2.2 值域（逐項附出處；找不到出處者停手，§8.4.1）

| 項 | 值 | 出處 |
|---|---|---|
| 觸發門檻 | `> 85 degrees C` | CFTS_020 `{4820289}` |
| 回復門檻 | `<= 85 deg C` | CFTS_020 `{4820290}` |
| 回復行為 | 依 `{4820287}` `{4820288}` 之原文 | CFTS_020 |
| 顯示狀態訊號 | `$…DISP_STAT$` 系列，值標籤 `DISP_HOT`／`DISP_OFF`／`DISP_NORMAL` | `data/signal_resolution.tsv`，三段鏈解至 DBC（R-DM17）；名稱依 R-DM43 取訊號側 |
| popup（004） | `PU0517`，timeout `10`，category `1T` | `Pop Up List HMI R1 (26PI).xlsx` `Main` |
| popup（005） | `PU0130`，timeout `10`，category `1T` | 同上 |

**PU 之歸屬判定**（哪一個 popup 屬哪一條 leaf 之驗證範圍）
須依 §8.5 與 §8.2.1 逐條判，判定理由寫入 `reasoning`。
**不得因兩者皆為 `1T` 而假定其行為相同。**

### 2.3 格式（Display 無 profile override，全採 canon）

- **訊號**：§8.7.5 **v3** —— `$MESSAGE.Signal$ = <raw> (<label>)`；
  Procedure 送出用 `Send the signal …`，ER 觀察用 `… is received`。
  **不得用已撤銷之 v1 三件組或 v2 `Send CAN:` 前綴**
- **test_item**：R-S4 兩段式。上半為 037 原句 verbatim（**含 `DISPLAY_ON`
  之原拼法，R-DM43 只規制步驟與 ER，不改引文**），token ≤ 50；
  下半 `(...)` 獨立成行，且 004／005 各列之括號內容**不得逐字相同**
- **spec_reference**：`CFTS020-{7 位 ObjectID}`，**一個 ObjectID 一行**，
  前綴逐行重述，升冪；禁 `,`／`、`／`;` 串接（§10.7）
- **Input Test Data**：溫度值為獨立資料集 → 得填；
  其餘一律 `NA`（§4.5 之 SWC 基準）
- **Pre-Condition**：門檻須為具體值（§8.7.1）；
  **不得寫「Display is powered on」等系統預設**（§4.4）
- **無尾句號**、UI 標籤用 `"..."`（§11）
- **Design Method**：procedure 定稿後才指派（§12）。
  預期 #1/#2 為 `State Transition`、#3 為 `State Transition`；
  以自檢結果為準，不得先填

---

## 三、作業步驟

1. §一之簽核轉錄與二項複驗
2. `batches/pilot-01/batch_context.md` 落檔（下放包 17 §三之內容）
3. 生成 TC，逐條走 canon §9 自檢十七項，**自檢結果逐條附於上繳包**
4. `lint036.py` 對本批執行（A–N），輸出全文附上繳
5. **不寫回 036 工作簿** —— 寫回待 Pei 覆核本批後另行裁示
6. 更新 `docs/INDEX.md`

---

## 四、停止條件

沿用 1–43，另加：

44. §一(b) 之 `recon.py` 若**未**回 REFUSED → 停並回報
45. 任一值找不到 §2.2 所列之出處 → 停（§8.4.1），**不得造值**
46. 生成之 TC 若須引用 005 之分級門檻方能成立 → 停
    （該部分為 deferred，不在本批）
47. `lint036.py` 任一檢查項 FAIL → 停並回報，**不自行放寬判準**

**全部 git 操作屬 Pei。**

---

## 五、上繳包要求（`docs/upstream/18_pilot01.md`）

1. 簽核轉錄後之 `DECISIONS.md` 末段全文 ＋ 二項複驗結果
2. `batch_context.md` 全文
3. **生成之 TC 全文**（10 個 key 齊備，§10.1）
4. 逐條之 canon §9 自檢十七項結果
5. `lint036.py` 全文輸出
6. 未驗項分流（A／B 標記，R-G29）
7. 建議之 commit 訊息與 pathspec（不執行）
