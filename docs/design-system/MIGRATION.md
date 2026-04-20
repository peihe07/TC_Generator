# Claude Code 執行指令稿 — TC Generator Win95 Migration

> 把這份檔案餵給 `frontend/` 下的 Claude Code。每個 Phase 是一個獨立 PR，跑完跑 `npm run dev` 視覺驗收後再進下一個。

## 進度總表（最後更新：2026-04-20 — Phase 6 全數完成）

| Phase | 範圍 | 狀態 | commit |
|-------|------|------|--------|
| 0 | Design system bundle 入 repo（`docs/design-system/`） | ✅ | `da81752` |
| 1 | Token 層 + global hard rules（`win95.css`） | ✅ | pre-migration |
| 2 | UI primitives（Input / Button / StatusBadge） | ✅ | pre-migration + `d2a4af4`（generating pulse） |
| 3 | 顏色清查（hex → token） | ✅ | `3ca2880` |
| 4 | 動畫清掃（motion tokens、移除 slide-in、pulse 1s 統一） | ✅ | `d2a4af4` |
| 5 | Desktop / Taskbar / StartMenu 視覺對齊 | ✅ | `d2a4af4` |
| 6.1 | Upload module | ✅ | `fa51eea` |
| 6.2 | Configure module（含 `.win95-th` 對齊、Tabs override） | ✅ | `fa51eea` |
| 6.3 | Generate module（progress bar blocky chunks 重寫） | ✅ | `a7b00e6` + `c1d0a03` |
| 6.4 | Review module（peach pending、diff palette、sticky header） | ✅ | `da389fc` |
| 6.5 | Export module（含 `.type-h1` size 對齊） | ✅ | `490008d` |
| 6.6 | QuickGenerate module | ✅ | `119a060` |
| 6.7 | ChatModule（double-header 修 + sunken-bezel systemic fix + FAILED contrast F1 patch） | ✅ | `499d391` + `1011123` + `afd3471` |
| 6.8 | Diagrams / Rules（(α) policy — iframe content intentionally out-of-scope） | ✅ | doc-only（見本檔 §Phase 6 #8） |
| 7 | Iconography（已於 HANDOFF Phase 5 完成桌面圖示外部化） | ✅ | `d2a4af4` |
| 8 | 測試 & 驗收 | 🚧 unit tests passing（107/107）；E2E + 完整手動驗收 ⬜ | — |

Follow-up 待辦（全數記於 Post-migration polish §P1–§P13）：
- Phase 4：`.agent-taskbar-btn--waiting_confirm` pulse 節奏差異丟失 → 改視覺（warning 黃或 `!` 圖示）
- Phase 6.4：~~§P3 (`pendingRegenerated` rename)~~ **已完成 2026-04-20** / ~~§P4 (`isActive` vs `isSelected` 拆分)~~ **已完成，併入 §P12** / ~~§P5 (GENERATED TEST CASE 欄空白 bug)~~ **已關閉為誤報**
- Phase 6.5：§P6 (`Win95Dialog` 通用元件)
- Phase 6.7：~~§P9 (4 TSX inline sunken → `.border-sunken` class)~~ **3/4 已完成**（RegenDiff 條件式 pattern 永久例外）/ ~~§P10 (Review toolbar vs `.win95-th` boundary)~~ **已完成 2026-04-20** / ~~§P12 (decouple expanded/selected state — F1 FAILED-contrast root fix)~~ **已完成 2026-04-20**
- Phase 6.8：§P13 (Rules tabpanel nested sunken border observation)

**Phase 6 — Module migration 全 8 module 完成。** 下一階段為 Phase 8（測試覆蓋）及 Post-migration polish backlog。

## 前置

```
cd frontend
npm run dev   # 開 http://localhost:3000
```

對照基準：`design_system/ui_kits/desktop/desktop-ui-kit.png` 與 `design_system/preview/*.html`。

---

## Phase 0 — 把 design_system 放進 repo

```
mkdir -p frontend/design_system
# 解壓 design system zip 到 frontend/design_system/
```

驗收：`frontend/design_system/ui_kits/desktop/index.html` 能直接在瀏覽器打開。

---

## Phase 1 — 已完成 ✅
Token 層 + global rules 都齊（`frontend/src/styles/win95.css`）。**跳過**。

---

## Phase 2 — UI primitives 對齊

### 2.1 `Input.tsx` — 補 `border-sunken` 視覺驗證
檔案：`frontend/src/components/ui/Input.tsx`
動作：跑 `npm run dev`，比對 `design_system/preview/form-inputs.html`。檢查 9 個用點（grep `border-sunken` 找）：
- Upload dropzone、Configure 三個 tab、Generate filename、Review filter、Export filename、QuickGenerate prompt

如果太「深」，把 `win95.css` 裡 `.border-sunken` 的 `inset 1px 1px 0 #000` 改成 `inset 1px 1px 0 #606060`。

### 2.2 `Button.tsx` — 視覺驗證
檔案：`frontend/src/components/ui/Button.tsx` (已對齊)
驗收：對照 `design_system/preview/buttons.html`。確認 `accept` / `reject` 變體文字色為深綠 `#006400` / 深紅 `#8b0000`。

### 2.3 `StatusBadge.tsx` — 6 變體完整
檔案：`frontend/src/components/ui/StatusBadge.tsx` (已對齊)
動作：在 `win95.css` 確認 `.status-badge.generating` 有 `animation: pulse 1s ease-in-out infinite;`。沒有就加：
```css
.status-badge.generating { animation: pulse 1s ease-in-out infinite; }
@keyframes pulse { 50% { opacity: 0.55; } }
```

---

## Phase 3 — 顏色清查（非常重要）

```bash
cd frontend
grep -rE "#[0-9a-f]{3,6}" src --include="*.tsx" --include="*.ts" --include="*.css" \
  | grep -vE "(#000000|#404040|#606060|#808080|#c0c0c0|#dfdfdf|#e0e0e0|#ffffff|#008080|#000080|#1084d0|#00a000|#006400|#c4e9c4|#c00000|#8b0000|#f5b7b7|#e0a000|#7d4e00|#fb923c|#c2410c|#fffbe0|#fed7aa|#fdba74|#7c2d12|#faf6f4|#991b1b|#f4faf4|#166534|#e8e8e8|#d0d0d0|#cc0000|#ffcccc|#fff0f0)" \
  > /tmp/illegal-colors.txt
```

把 `/tmp/illegal-colors.txt` 裡每個 hex 換成最接近的 token（CSS 用 `var(--…)`，TSX 用內聯參考）。**禁止新色**。

---

## Phase 4 — 動畫清掃

```bash
grep -rE "(transition|animation):" src --include="*.tsx" --include="*.css"
```

只保留：
- `120ms ease`（hover/press）→ 改成 `var(--motion-fast)`
- `200ms linear`（progress）→ 改成 `var(--motion-progress)`
- `pulse 1s`（agent button + `.status-badge.generating`）
- `spin 1s linear`（loading）

其餘 fade / slide / stagger / cubic-bezier 全部刪除。

### Follow-up（Phase 4 完成後記錄）

- `.agent-taskbar-btn--waiting_confirm` pulse 從 `0.7s` 改為 `1s` 後，失去「比 streaming 更急迫」的節奏差異。
- **若要恢復急迫感，改視覺不改 timing**：
  - 底色從 `var(--status-warn)`（琥珀）可強化為更飽和 warning
  - 或加 `!` 圖示 / 邊框強化辨識度
- 禁止再動 pulse timing 回 `0.7s`（違反 Phase 4 規則）

---

## Phase 5 — Desktop / Taskbar / StartMenu 視覺對齊

### 5.1 `Desktop.tsx`
驗收：對照 `design_system/preview/desktop-icons.html`。確認：
- 桌面 icon 48×48 + `image-rendering: pixelated`
- selected 狀態：`background: rgba(0,0,128,0.5)` + `outline: 1px dotted #fff`
- label 白字 + `text-shadow: 1px 1px 0 #000`

### 5.2 `Taskbar.tsx`
驗收：對照 `design_system/preview/taskbar.html`。確認：
- 28px 高 + `border-top: 2px solid #fff`
- Start button 含 4 色方塊 logo（已有）
- Active task button 用 inset bevel
- Tray（時鐘）用 sunken bevel
- Agent button 用 navy + `pulse` 動畫

### 5.3 `AppWindow.tsx`
驗收：對照 `design_system/preview/window-chrome.html`。確認：
- title-bar 26px + 左 icon + 右三按鈕
- inactive 狀態用 `--win95-gray-mid` 背景

---

## Phase 6 — Modules 視覺對齊（一個一個來）

每個 module 對應一個 preview 卡，順序：

1. **Upload** → `preview/window-chrome.html` + `preview/form-inputs.html`（dropzone 使用 `.dropzone-sunken`）
2. **Configure** → `preview/fieldsets.html` + `preview/tabs.html`
3. **Generate** → `preview/progress.html`（segmented fill）
4. **Review** → `preview/table.html` + `preview/paper-cards.html`
   - Note: `.win95-th` 已於 Phase 6.2 對齊（1px bevel、`#808080` BR、`3px 8px` padding、移除 inset shadow），Review module header 視覺已提前調整。
   - Note: pendingRegenerated row 的 peach 底色 (`--edit-accent-bg`) 僅在 collapsed 狀態顯示；展開時 `isActive=true` 觸發 `.selected` navy 會覆蓋（intended，見 P4 / P5）。
   - Follow-up（已彙整至 Post-migration polish §P3–P5）
5. **Export** → `preview/fieldsets.html` + `preview/dialog.html`
6. **QuickGenerate** → `preview/form-inputs.html`
7. **ChatModule** → `preview/paper-cards.html`（user bubble = navy / bot = white sunken）

   **附帶修正（獨立 commit）：** Phase 6.7 驗收 `.agent-text` bot bubble bezel 時，發現 sunken-bezel token 語意誤用 — canonical `.bezel-sunken` / `.border-sunken` 及 10 個衍生 sunken surface 的 TL 邊色用 `--win95-gray-mid` (`#808080`)，但 README §「The seven grays」語意綁定為「raised-bezel shadow」；sunken 的語意對應色是 `--win95-gray-dark` (`#606060`)。屬 design system 層級規格 vs 實作分叉。修正為獨立 commit `fix(design-system): correct sunken bezel top/left color semantics`，scope 42 處（產品 `win95.css` 12 + TSX inline 4 + design bundle 規格權威 5 + bundle 鏡像 21；明確排除 `docs/mockups/*.html` 10 處 pre-design-system scratch）。

8. **Diagrams / Rules** → `preview/window-chrome.html`（內容 iframe，外框照舊）

   **採 (α) policy — iframe 內容視為獨立內容區，不強制 Win95 token 化。** 理由：
   1. MIGRATION.md 字面即 (α) — 「外框照舊，內容 iframe」原意明確，改寫 iframe 內容 HTML 屬 scope creep。
   2. iframe 邊界是 **content vs chrome 的自然切面** — Win95 桌面是 OS chrome，iframe 內是「應用程式內容」，本來就不該強制同一視覺語言（類比：Win95 IE 開任何網頁也不會強迫該網頁變 Win95）。
   3. `diagrams.html` 的彩色方塊是 **資訊 encoding**（藍 = infra、珊瑚 = user-facing 等），全換灰階等於砍掉架構圖資訊維度 — 功能損失非視覺升級。
   4. `rules-*.html` 是 pandoc 從 markdown 產物，重寫 CSS 等於綁死 pipeline — 之後改 rule source 重跑 pandoc 又要重對齊，維護成本不划算。`prefers-color-scheme: dark` 支援不影響外層 Win95 chrome（外層用固定色票不響應 media query）。

   **靜態驗收清單（通過）：**
   - `<iframe>` 本身 `border: 'none'` ✓（`DiagramsModule.tsx` / `RulesModule.tsx` 皆明確設）
   - `width: 100%; height: 100%; display: block` ✓ 貼齊父容器
   - AppWindow inner container 對 diagrams/rules 用 `p-0`（其他 module 是 `p-4`）— 無 padding 灰縫 ✓
   - Tab bar（Rules 用 98.css `<menu role="tablist">`）已由 Phase 6.2 tabs override 涵蓋 ✓
   - RulesModule `<div role="tabpanel">` 的 inline sunken border 已由 sunken-bezel systemic fix 涵蓋 ✓

   **實質零程式變更。** AppWindow 外框 + tab bar + sunken border 於前 Phase 已全數覆蓋，Phase 6.8 只做靜態驗收 + doc 記錄。

   **Follow-up：** 見 §P13（Rules nested sunken border 觀察）。

每個 module 改完跑：
```bash
npm run dev
# 開對應 window，截圖對照 ui_kits/desktop/desktop-ui-kit.png 的對應區塊
```

---

## Phase 7 — Iconography

桌面 icon 已用 SVG（`/icons/desktop/*.svg`）。確認 `frontend/public/icons/desktop/` 裡的 9 個 SVG 與 `design_system/assets/icons/desktop/` 一致；不一致則覆蓋。

模組內 icon 全用 Remix Icon：
```bash
grep -rE "from '@remixicon/react'" src --include="*.tsx" | wc -l
```
找出仍用手畫 SVG 的地方，全換成 Remix Icon。

---

## Phase 8 — 測試 & 驗收

```bash
npm run test       # vitest
npm run test:e2e   # playwright
npm run build      # 確認 type / lint 過
```

最後手動驗收：開瀏覽器逐一打開 9 個 window，截圖丟進 PR description，與 `desktop-ui-kit.png` 對齊。

---

## Post-migration polish（獨立 PR，不在 Phase 1–8 範圍）

Migration 期間發現、但不屬於視覺對齊的小功能。每項一個獨立 PR。

### P1 — Review ValidationPanel 可拖曳寬度 — **已完成（2026-04-20）**

**動機：** `ValidationPanel.tsx` 目前寫死 `w-64` (256px)；使用者希望能調整寬度。

**規格：**
- 垂直 splitter，**sunken bezel**（用 `.border-sunken` 或新 class `.splitter-v`）
- 寬度 `4px`，`cursor: col-resize`
- 左側（主內容）預設 `flex: 1`；右側（Validation Results）預設 `320px`
- min `200px` / max `500px`
- 拖曳用 **pointer events**（非 mouse events），支援 touch
- 寬度存 `localStorage`，key：`review-validation-panel-width`
- a11y：`role="separator"` + `aria-orientation="vertical"` + `aria-valuenow` / `aria-valuemin` / `aria-valuemax`
- 鍵盤支援 ← → 每次調 `16px`

**禁止：**
- 不用 3rd-party resize lib（`react-resizable` 等）— 手寫 hook < 80 行
- 不加動畫 / transition（拖曳必須即時跟隨游標）
- 不加圓角 / gradient

**進入條件：** Phase 6.2 收完後再開工。

### P2 — GenerateModule cost budget threshold warning — **已完成（2026-04-20）**

**動機：** Phase 6.3 發現 GenerateModule 的 Session Stats 目前沒有「超出預算」的視覺警示；cost 數字只單純顯示，超標不變色。`ConfigureModule` 已有 `config.budgetLimit` 這個設定值，但 Generate 階段沒拿來比對。

**規格：**
- 當 `stats.cost >= config.budgetLimit * THRESHOLD`（例如 `THRESHOLD = 0.8`，即用到 80% 預算）時，cost 數字文字色轉 `var(--status-reject-dark)`，並前置 `<RiAlertLine>` Remix icon
- 當 `stats.cost >= config.budgetLimit`（100% 以上）時，同上並加 pulse 強調（`animation: agent-pulse 1s ease-in-out infinite`，符合 Phase 4 規範）
- 未達 threshold 時保持 `var(--text-default)`，無 icon

**禁止：**
- 不自動停止 generation（僅視覺警示）
- 不用新顏色，只用既有 `--status-*` token
- 不加新的 pulse timing（必須是 1s，符合 Phase 4）

**進入條件：** 所有 Phase 6 module alignment 完成後。

### P3 — Rename `pendingRegenerated` → `awaitingApply` (資料層一致) — **已完成（2026-04-20）**

**動機：** Phase 6.4 發現 Review module 的「等待套用 regen」狀態在 3 層用 3 個不同名字，造成閱讀混淆：

| 層 | 名字 |
|----|------|
| Data model | `TcRow.pendingRegenerated?: PendingRegeneratedFields` |
| StatusBadge variant | `'reviewing'`（navy 徽章，複用其他狀態） |
| Label 顯示字 | `"awaiting apply"` → rendered as `AWAITING APPLY` |

**目標：** 統一為 `awaitingApply`：
- `TcRow.awaitingApply?: RegenFields`（rename field）
- `StatusBadge` 新增 `'awaitingApply'` variant（或保留 `reviewing`，但改 label 衍生邏輯使用新 field 名）
- Label 一致顯示 `AWAITING APPLY`

**Scope:**
- `frontend/src/lib/types.ts`（`TcRow` interface）
- `frontend/src/store/useJobStore.ts`（`setPendingRegenerated` / `applyRegenerated` / `clearPendingRegenerated` 全 rename）
- `frontend/src/services/jobAdapter.ts`（regen SSE payload 欄位對應）
- `frontend/src/components/modules/review/ReviewModule.tsx` / `ReviewRow.tsx` / `RegenDiff.tsx`
- `frontend/src/__tests__/review.ReviewRow.spec.tsx`（測試名 + fixture）
- `MIGRATION.md` 本檔提及處

**禁止：**
- 不改視覺（peach row bg 規則不變）
- 不改 Phase 6.4 已對齊的 CSS token 使用

**進入條件：** 所有 Phase 6 module alignment 完成後。

### P4 — Review row `isActive` vs `isSelected` 拆分 (selected state 模糊) — **已完成（2026-04-20），併入 §P12**

**動機：** Phase 6.4 發現 `ReviewRow.tsx:83` `${isActive || isSelected ? 'selected' : ''}` 把「展開 row」（`isActive`，為了 Validation Panel 同步）與「checkbox 選中」（`isSelected`，為了批次操作）合併為同一視覺狀態 → navy 底白字。副作用：展開 pendingRegenerated row 時，peach 底色被 navy 蓋過，視覺傳達失敗。

**目標：** 拆為兩個獨立視覺狀態：
- `isSelected`（checkbox 勾選）→ 保留現有 `.selected` → navy
- `isActive`（展開 / Validation Panel 同步）→ 改用較輕視覺（例如 2px navy `outline` inset、或 `--field-header-bg` 淡灰 row bg），不覆蓋 peach

**Scope:**
- `frontend/src/components/modules/review/ReviewRow.tsx`（L83 className 邏輯）
- `frontend/src/styles/win95.css`（新增 `.win95-row.active` 視覺規則）

**禁止：**
- 不新增顏色（用既有 token）
- 不加 transition/animation（符合 Phase 4 規則）

**進入條件：** 獨立任何時機；建議與 P3 一起做以減少 ReviewRow 二次修改。
**合併建議：** §P12（state 拆解）是本項的實作化具體方案，建議一起處理 —— §P4 是視覺規格目標、§P12 是 state 層 refactor，同一根問題兩個維度。

### P5 — Review module 展開 row 的 GENERATED TEST CASE 欄位渲染為空 — **已關閉（誤報）**

**原報告：** Phase 6.2 bisect 時觀察「Review 展開 row 後 GENERATED TEST CASE 欄位 section label 下方實際內容空白」，疑似資料層 bug。

**2026-04-20 診斷結論：不存在 rendering bug。**

`frontend/src/__tests__/review.ReviewRow.spec.tsx` 新增 2 個直接驗證測試（`ReviewRow — expanded non-edit state renders generated TC fields`）：
- 給定 `row.preConditions` / `inputTestData` / `steps` / `expectedResults` / `testItemRewrite` 都有值 → 5 個 `StackedReadField` 全部渲染對應文字 ✅
- 給定上述 5 欄全是空字串 → 渲染 5 個 `—` em-dash placeholder ✅

渲染路徑是 `StackedReadField` 的 `{value || '—'}`（`StackedFields.tsx:33`），自 `0b64610` 起未變。

**真正原因：** 當 row 是 `status: 'fail'` 時，backend `_build_failed_stream_row` 在 `api_server.py:506-508` 設 `generated: None`，frontend `mapApiRowToTcRow` 在 `jobAdapter.ts:159-162` 將 5 個欄位預設為 `""`。展開時 `StackedReadField` 正確渲染 `—` placeholder — 即 **「失敗的 TC 本來就沒有生出來」**，label + `—` 是設計語意，不是 bug。

觀察者視覺誤判可能來自：`—` 字形小 + row 為 `isActive`（navy `.selected` bg）時，em-dash 與 dark red reason text 混在一起不明顯。Navy selected 視覺問題另由 §P4 / §P12 處理。

**狀態：** closed-as-not-a-bug。保留此項供歷史追溯。

### P6 — `Win95Dialog` 通用元件

**動機：** Phase 6.5 發現 codebase 沒有統一的 confirm/warning dialog 元件。`preview/dialog.html` 提供了完整規格（chunky yellow `!` glyph、heavy drop shadow、right-aligned action row、default button bold + inset outline），但目前無對應 component。未來多個流程會需要 dialog（見下方使用場景），抽成通用元件比各自手寫更一致。

**規格（對照 `preview/dialog.html`）：**
- 容器：`width: 360px`，`background: var(--win95-gray)`，raised 2px bezel，`box-shadow: 4px 4px 0 rgba(0, 0, 0, 0.35)`
- Title bar：navy gradient（`.title-bar` + 非 inactive），含 14×14 黃色 `!` glyph（`background: var(--status-warn)`, 1px black border, black `!`）
- Body：`padding: 16px`，`display: flex; gap: 14px`，左側 40×40 chunky warning glyph（同色規格，字大 26px），右側訊息文字 `--font-md`
- Action row：`padding: 4px 12px 12px`，`display: flex; gap: 6px; justify-content: flex-end`，default 按鈕加 `.default` class（bold + `outline: 1px solid var(--win95-black)` inset -4px）

**Props:**
- `open: boolean`
- `variant: 'warning' | 'error' | 'info'`（warning = 黃 glyph，error = 紅 glyph `var(--status-reject)`，info = 藍 glyph `var(--win95-navy)`）
- `title: string`
- `message: string | ReactNode`
- `actions: Array<{ label: string; onClick: () => void; variant?: 'default' | 'cancel' }>`（`default` → `.default` class）

**使用場景（未來）：**
- Export overwrite confirm
- Review reject all confirm
- Regenerate discard edits confirm
- Workspace delete confirm

**Scope:**
- `frontend/src/components/ui/Dialog.tsx`（新元件）
- `frontend/src/components/ui/index.ts`（加入 barrel export）
- `frontend/src/__tests__/ui.Dialog.spec.tsx`（a11y：`role="alertdialog"` / `aria-labelledby` / `aria-describedby` / Esc 關閉 / focus trap）

**禁止：**
- 不用 3rd-party dialog lib（Radix / Headless UI 等）— 手寫 < 150 行
- 不加動畫進場/離場（符合 Phase 4 禁 fade/slide）
- 不加圓角（Phase 1 global rule 已含 `* { border-radius: 0 !important }`）

**進入條件：** 獨立，非視覺遷移，任何 Phase 6 module 收完後均可開工。

### P7 — Typography: Tailwind font-size class → semantic class 統整 — **Defer: 不適合機械 refactor**

**動機：** Phase 6.5 audit (`/tmp/font-size-audit.txt`) 發現 codebase 仍混用 Tailwind `text-xs` / `text-sm` (共 **49 處**，扣掉 Phase 6.3 修掉的 `text-lg` 3 處) 與 Phase 2 語意 class (`.type-h1` / `.type-body` / `.type-meta` / `.type-badge` / `.type-mono`)。同時使用兩套 font-size 詞彙，閱讀成本高，且 Tailwind `text-xs` 與 token `--font-md` 數值對得上只是巧合（Tailwind 改版後會偏移）。

**2026-04-20 Defer 決策：** 4 / 49 是「純 solo `text-xs`」可安全替換，其餘 45 處伴隨 `font-bold` / `leading-tight` / `font-mono` 等 Tailwind modifier。`.type-body` 明定 `font-weight: normal` + `line-height: 1.5`，機械換掉會**蓋掉字重與行高**，違反 P7 「視覺 diff 應為零」+「不改字重」。自動 sed 不可行，人工每案判斷成本高。

**建議做法：**
- 日後改動各 module 時順手替換（機會主義式 migration）
- 或新開「per-module typography sweep」子任務，每個 module 一次 ~5-10 處，視覺驗收逐個截圖
- **不**新增 `.fs-md` / `.fs-lg` 這種 font-size-only utility class（違反「不加新 type token」規則）

**狀態：** Open / deferred，不作為 active polish 項目追蹤。

**目標：** 移除所有 `text-(xs|sm|base|lg|xl|...)` Tailwind class，統一改用 Phase 2 語意 class 或 inline `style={{ fontSize: 'var(--font-*)' }}`。

**對應規則（需逐個判斷上下文）：**

| Tailwind | px | 建議 token / semantic class | 備註 |
|----------|----|-----------------------------|------|
| `text-xs` | 12px | `.type-body`（body inside modules）或 inline `fontSize: 'var(--font-md)'` | body / inspector 文字多數 |
| `text-sm` | 14px | `.type-h1`（headings）or `fontSize: 'var(--font-lg)'` | 需判斷是否為 heading |
| `text-[10px]` | 10px | inline `fontSize: 'var(--font-xs)'` 或 `.type-meta` | 已是 arbitrary value，直接 swap |
| `text-[11px]` | 11px | inline `fontSize: 'var(--font-sm)'` 或 `.type-badge`/`.type-mono` | 看場景 |

**Scope：** 約 49 處跨 13 檔，按檔案分佈：
- QuickGenerate 群（InputPanel / Module / DecomposeAnalysisPanel / TcCard）= 19
- Generate / ReviewRow / ReviewToolbar / ValidationPanel / ReviewModule = 17
- Upload / Configure / Export / RegenDiff / StackedFields = 13

**禁止：**
- 不改實際 font-size 值（必須視覺等價 diff 為零）
- 不加新 type token（5-step scale 不擴充）
- 不改字重（`font-bold` 保留，除非冗餘）

**進入條件：** **Phase 6 全部完成後** 再做，避免跟進行中的 module migration 衝突。

### P9 — Refactor 4 個 TSX inline sunken bezel 為 `.border-sunken` class — **3/4 已完成（2026-04-20）**

**動機：** Phase 6.7 附帶 sunken-bezel token 修正時發現 4 個 TSX 檔以 inline `borderColor` 重寫 canonical sunken pattern 而非引用 `.border-sunken` class。這次 sunken token 誤用擴散 16 處（CSS 12 + TSX 4），inline 重寫是放大效果主因。

**執行狀態：**
- ✅ `configure/GroupingTab.tsx`（Manual Override 表外框）→ `className="border-sunken"`
- ✅ `quickGenerate/DecomposeAnalysisPanel.tsx`（panel 外框）→ `className="border-sunken"`
- ✅ `rules/RulesModule.tsx`（tabpanel 容器）→ `className="border-sunken"`
- ⚠️ `review/RegenDiff.tsx`（field container）— **刻意保留 inline**：此處 `borderColor` 是 `isSelected` 條件式，selected state 走 sunken pattern，unselected state 走不同的「disabled」pattern（`var(--win95-gray) var(--win95-gray-lighter) ...` + `opacity: 0.55`）。單一 class 無法乾淨表達雙分支，硬套會改變 unselected 視覺語意。

**已知視覺 delta：** `.border-sunken` class 除了 border 還有 `box-shadow: inset 1px 1px 0 var(--win95-black)`，而原 inline 版本只有 border 沒 shadow。refactor 後上述 3 處會**多一個 1px 黑色 inset shadow**（完成 canonical sunken pattern）—— 這是讓這 3 處與系統內其他 sunken surface（dropzone / stat / progress well / paper-card / agent-text 等）視覺一致，而非偏離。若需嚴格 zero-diff，各處加 `style={{ boxShadow: 'none' }}` 覆蓋。

**進入條件：** ✅ 本項 3/4 已完成。RegenDiff 條件式 pattern 列為永久例外（不是待辦 — 是正確設計決定）。

**進入條件：** Phase 6 全部完成後；P7（typography）後順手做較方便（兩者都是 TSX 的 className refactor）。

### P10 — Review toolbar 與 `.win95-th` header 邊界交接視覺審視 — **已完成（2026-04-20）**

**動機：** Phase 6.7 sunken-bezel token 修正後驗收時低優先觀察 — `ReviewToolbar`（`Show:` / `Test Set:` + `Total: X | Accepted: X | Expanded: X` 那條）與其下方 table `.win95-th` header 的視覺邊界交接可能不乾淨。兩者一個 sunken（toolbar 用 `border-sunken`，TL 現為 gray-dark）、一個 raised（`.win95-th`，BR 用 gray-mid），相接處可能出現雙暗邊 / 雙亮邊堆疊。

**執行：** Root cause 是 `ReviewToolbar` 的 `.border-sunken` 選用錯誤 —— toolbar 屬於 "app chrome"（工具列）不是 content/input surface，按 Win95 convention（File Explorer toolbar、`preview/taskbar.html`）toolbar 應為 **raised**。改 `.border-sunken` → `.bezel-raised`。視覺方向現在：toolbar "凸出" + 8px margin + 下方 table 容器 "凹陷"，層次分明。

**目標：** 視覺審視交界處，如果需要加 `margin-bottom` / 改用 single-border 接邊，記下規格調整。

**Scope:**
- `frontend/src/components/modules/review/ReviewToolbar.tsx` 或 `ReviewModule.tsx` 表格容器
- 可能調整的 CSS 只 1–2 行

**進入條件：** Phase 6.8 完成後回看。低優先 — commit 2 驗收未擋。

### P12 — Decouple expanded row state from selected row state (Review module) — **已完成（2026-04-20）**

**Original background:** ReviewRow 原先 `className={... ${isActive || isSelected ? 'selected' : ''}}` 把「展開 row → 同步 ValidationPanel」與「checkbox 勾選 → 批次操作」兩種語義混在同一 `.selected` navy 視覺。副作用：任何展開的 row 都看起來像 selected，peach pendingRegenerated bg 被蓋掉；FAILED reason text 在展開的 row 上 red-on-navy 對比失敗（由 F1 臨時補丁處理）。

**執行（minimum-viable fix）：**
- `ReviewRow.tsx:93` `.selected` class 條件從 `isActive || isSelected` → `isSelected`（checkbox 勾選才變 navy）
- `ReviewRow.tsx:95` peach 背景條件從 `!isActive && !isSelected` → `!isSelected`（expand pendingRegenerated row 時 peach 正常顯示）
- `ReviewRow.tsx:163` F1 條件色從 `isActive || isSelected ? ...` → `isSelected ? ...`（純 FAILED row expand 時走 `--status-reject-dark` 紅字 on white，對比 OK；checkbox-selected 的 edge case 仍走 white on navy）
- `activeRowId` state **名稱保留**（未 rename 為 `expandedRowId` / `focusedExpandedRowId`）— 減少 churn，state 結構早已獨立於 `selectedIds`，問題出在 class trigger 不是 state shape。

**F1 狀態：** 條件色簡化為 `isSelected` 單參數；沒有完全 revert 因 checkbox-selected edge case 仍需白字。可視為「F1 臨時補丁 → F1.1 精簡版」。

**Tests：** 109/109 pass，無視覺 regression（只有展開 row 不再變 navy — 設計本意）。

**§P4 狀態同步關閉：** §P4 是本 item 的視覺規格描述（要求 `isActive` 與 `isSelected` 拆分），§P12 是實作路徑。兩者同根問題，一起解決。

### P13 — Rules module tabpanel nested sunken border 觀察

**Background:** Phase 6.8 iframe 靜態驗收時觀察到 `RulesModule.tsx` 的 `<div role="tabpanel">` 有自己的 inline `border: 2px solid` sunken bezel，同時外層 `AppWindow` inner container 也套 `.border-sunken`（2px）。兩層 sunken 邊框在 tabpanel 四週疊加 = 4px sunken 視覺厚度，可能偏重。

**語意正確 vs 視覺過厚：** 雙層各有語意正確性（外層分隔 window-body 與 title bar、內層分隔 tabpanel 與 tab bar），符合 Win95 nesting 慣例（例如 fieldset 嵌在 window-body 也有類似效果）。**但**若實測視覺偏重，可簡化為單層 frame。

**建議做法（二選一，看實測）：**
- (1) 移除 `RulesModule.tsx:38-42` inline sunken border，交由外層 `.border-sunken` 唯一表達 frame（4px → 2px）
- (2) 保留雙層但調細（例如 inline border 改 1px，只保留 token 色語意）

**Scope:**
- `frontend/src/components/modules/rules/RulesModule.tsx`（L38-42 inline style）

**進入條件：** 獨立，極低優先 — Phase 6.8 驗收時無視覺 blocker，等之後實測截圖若覺偏重再處理。

### Category D exclusion note — `docs/mockups/*.html` 保留舊 hex sunken pattern

`docs/mockups/chat_module_mockup.html`（7 處）+ `docs/mockups/agent_gui_flow.html`（3 處）共 10 個 `#808080 #ffffff #ffffff #808080` 出現，**刻意不在 sunken-bezel token 修正 commit 範圍內**：

- 這兩份是 pre-design-system 時期的 scratch mockups（最後更動 `da81752 chore(repo): reorganize docs assets`，純複製）
- 不在 `docs/design-system/` bundle 內，不被 preview / README / colors_and_type 引用
- 若要清理，合理動作是「刪檔」而非「改色」—— 列 tech-debt 待評估

**進入條件：** 獨立，極低優先。決定「保留為歷史文件」或「刪除」時再處理。

---

## 給 Claude Code 的執行指令模板

```
我要按照 design_system/MIGRATION.md 把 TC Generator 視覺對齊到 Win95 design system。

請從 Phase 2.1 開始。
讀完 design_system/preview/form-inputs.html 後告訴我預期視覺，
然後跑 npm run dev、列出 9 個 border-sunken 用點，
逐一回報視覺是否符合 preview。

完成 Phase 2 後暫停等我確認再進 Phase 3。
```
