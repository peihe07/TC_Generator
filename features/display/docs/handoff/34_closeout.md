# 下放包 34 —— 收尾包：解凍、補齊、全部寫回（Pei 2026-08-26 裁定「准」）

- 日期：2026-08-26
- 方向：分析層（Claude Project）→ 執行層（Claude Code）
- 對應上繳：`docs/upstream/34_closeout.md`（**本 feature 之收尾上繳**）
- **本包對交付物之推進：全部 —— 8 leaf 覆蓋、寫回 036**（R-G31）
- 前置（已查證）：上繳 33 之各項就緒；`popup_priority.tsv` 已建；
  九條定稿；DR 現況 9 SENT／1 CLOSED／1 OPEN／若干待發

---

## 一、裁決條文（本包僅此二條，此後凍結）

```
R-DM56（照專條測；規格矛盾以揭露處置，不以等待處置 —— Pei 2026-08-26 准）
TC 之職責是驗證規格所載，不是仲裁規格。CFTS_020 `1.11.2.2` 為
R1H／Atlantis High 之專條，本 feature 之 004／005 照其逐字撰寫並交付。

三項細則：
(a) `pilot-01` 三條解除「條件性正確」之凍結，照現稿寫回。
    其 `85 degrees C` 逐字取自專條 `{4820289}`／`{4820290}`，無誤。
(b) 規格之內部矛盾（組 A vs 組 B vs CFTS_013 §1.5.3 之 50°C）
    屬上游缺陷，以既有機制承載：R-G33 之括號下半揭露、
    deferred 四鍵、DR-DM10 之三份函件。**不因矛盾而扣留 TC。**
(c) DR 答覆到達後之修改為**變更**，不為阻斷：依 BACKLOG 之
    重審清單逐項處理，受影響者僅門檻數字與 deferred 之解除，
    TC 之結構不受影響（可逆性同 R-DM55(c) 之理路）。
```

```
R-DM57（收尾凍結 —— Pei 2026-08-26 准）
自本包起至本 feature 交付：
(a) 不立新條文、不加新檢查、不開新異常 —— 除非抓到 TC 內容之實錯
(b) 執行層之自陳一律入 `BACKLOG.md`，不佔輪次、不觸發新任務
(c) 上繳包只報 TC 與機器檢查結果，不寫檢討
(d) 既有停止條件僅內容類與寫回完整性類存續（見 §五）；
    流程類（輪次、置放、自陳格式）暫停適用
先例：Power Moding R-PMH103/104。
```

抄錄依 R-G34，各自獨立核對表。**這是最後一次抄錄作業。**

---

## 二、生成（兩批，連續執行）

### 2.1 `ops-01`（`SWE1-DM-001`／`-002`／`-003`）

依下放包 33 §四步驟 2–8 全部執行（排除表 → T1c 拼法 → 行為軸表 →
生成 → 檢查）。拘束不變：Implausible 值域逐字、`DISPLAY_ON` 等
不可解標籤依 A15 處置（ER 驗行為、deferred 掛 DR-DM8）、
Splash 時段 deferred 掛 DR-DM1、Sleep Mode 前置為狀態。

### 2.2 `popup-01`（`SWE1-DM-006`）

材料：`popup_priority.tsv`（1341 列）＋ CFTS_020 中適用本專案之
popup／優先序條文（R-G39 兩段式：候選 → 行為軸）。

拘束四項：
(a) **可寫者寫**：類別階梯之相對序（RVC > 其他）、`1T` 類之歸屬等，
    以可觀察行為驗之
(b) **凡涉 `Cat. SL` 之序 → 該欄 `PENDING: DR-DM2 Cat SL precedence`**
    （IN §8.4.3），不留空不填 NA
(c) `PU0130` 之需求側出處為 CFTS_013（HU 側）—— **R-DM51(c) 之標的
    註記義務不因凍結而免**；DCSD 側行為以 CFTS_020 為據
(d) timeout 值僅得取自 `Pop Up List` 之對應欄，逐字；查無則 deferred

**軸數逾 20 → 停**（停止條件 91 續用）。若 006 之可寫面向經勘查
不足以成批（< 2 TC），**具名回報後併入寫回，不強生**。

---

## 三、寫回 036（內部複本）

### 3.1 範圍與方式

- 標的：`inputs/` 之 036 母本複本（repo 內部複本；**交付路徑之複製屬 Pei**）
- 內容:`pilot-01` 3 ＋ `rvc-01` 6 ＋ `ops-01` ＋ `popup-01` 全部定稿 TC
- **XML 外科式**（R-VC2 同款）：zip 開檔、只改目標儲存格、原樣重打包
- TC ID 依 canon §10.3，前綴依 feature 既有設定，生成器編號
- `write_back` 依 `feature.yaml`：`author_value: PeiPYHsu`、
  `tc_ref_id_value: NEW`、`fill_test_group_set: true`（BLANK → FILL）

### 3.2 完整性驗證（前後各一次，逐項相等方可交）

`<dataValidation` 計數、`x14:dataValidation` 計數、
`<conditionalFormatting` 計數、工作表數、drawing／chart rel 數、
R 欄下拉可用性之抽查一格。**任一不等 → 停，保留兩份複本供比對。**

母本 sha 之變動為**預期**：記 before（`6372fb6be02f48dc…`）／after 於上繳。

### 3.3 寫回前之最後檢查（一次跑齊）

`lint036 --profile display`（全批合併母體）、§9 十七項、
`check_disclosure.py` 雙向（**交付前時點**，R-G33(d)(1)）、
I-sibling、綁定 13 項、停止條件 54／55／60／73／83／88／89／90／93 掃描。

---

## 四、收尾上繳（`docs/upstream/34_closeout.md`）

1. 兩批 TC 十欄全文 ＋ 檢查輸出（§3.3）
2. 寫回報告：sha before／after、完整性計數表、寫入列範圍
3. **覆蓋總表**：8 leaf × 覆蓋狀態（全／部分＋deferred token／PENDING 欄位）
4. **未結 DR 清單**（含待發者與各自之阻斷面向）—— 交付包必附
5. BACKLOG 現況快照（重審清單全文）
6. 建議之 commit 訊息與 pathspec（不執行）

---

## 五、停止條件（存續清單）

內容類：54／55／60／73／83／88／89／90／91／93。
寫回類：§3.2 之計數不等即停。
**其餘（含 76、87 已各自了結者）暫停適用**（R-DM57(d)）。

**全部 git 操作屬 Pei。交付路徑之複製屬 Pei。**
