# Claude Code 執行指令稿 — TC Generator Win95 Migration

> 把這份檔案餵給 `frontend/` 下的 Claude Code。每個 Phase 是一個獨立 PR，跑完跑 `npm run dev` 視覺驗收後再進下一個。

## 進度總表（最後更新：2026-04-19）

| Phase | 範圍 | 狀態 | commit |
|-------|------|------|--------|
| 0 | Design system bundle 入 repo（`docs/design-system/`） | ✅ | `da81752` |
| 1 | Token 層 + global hard rules（`win95.css`） | ✅ | pre-migration |
| 2 | UI primitives（Input / Button / StatusBadge） | ✅ 程式面；⬜ 完整視覺驗收 | pre-migration + `d2a4af4`（generating pulse） |
| 3 | 顏色清查（hex → token） | ✅ | `3ca2880` |
| 4 | 動畫清掃（motion tokens、移除 slide-in、pulse 1s 統一） | ✅ | `d2a4af4` |
| 5 | Desktop / Taskbar / StartMenu 視覺對齊 | ✅ | `d2a4af4` |
| 6.1 | Upload module | ✅ 程式面；⬜ 視覺驗收 | uncommitted |
| 6.2 | Configure module（含 `.win95-th` 對齊、Tabs override） | ✅ 程式面；⬜ 視覺驗收 | uncommitted |
| 6.3 | Generate module | ⬜ | — |
| 6.4 | Review module（含 2 條 follow-up 待辦，見本檔 §Phase 6.4） | ⬜ | `.win95-th` 已提前對齊於 6.2 |
| 6.5 | Export module | ⬜ | — |
| 6.6 | QuickGenerate module | ⬜ | — |
| 6.7 | ChatModule | ⬜ | — |
| 6.8 | Diagrams / Rules | ⬜ | — |
| 7 | Iconography（已於 HANDOFF Phase 5 完成桌面圖示外部化） | ✅ | `d2a4af4` |
| 8 | 測試 & 驗收 | 🚧 unit tests passing；E2E + 完整手動驗收 ⬜ | — |

Follow-up 待辦（記在對應 Phase 節內）：
- Phase 4：`.agent-taskbar-btn--waiting_confirm` pulse 節奏差異丟失 → 改視覺（warning 黃或 `!` 圖示）
- Phase 6.4：已彙整為 Post-migration polish §P3 (`pendingRegenerated` rename) / §P4 (`isActive` vs `isSelected` 拆分) / §P5 (GENERATED TEST CASE 欄空白 bug)

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

### P1 — Review ValidationPanel 可拖曳寬度

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

### P2 — GenerateModule cost budget threshold warning

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

### P3 — Rename `pendingRegenerated` → `awaitingApply` (資料層一致)

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

### P4 — Review row `isActive` vs `isSelected` 拆分 (selected state 模糊)

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

### P5 — Review module 展開 row 的 GENERATED TEST CASE 欄位渲染為空 (資料層 bug)

**動機：** Phase 6.2 bisect 發現既有資料層問題：Review 展開時 GENERATED TEST CASE 欄位 section label 下方實際內容空白，但 ORIGINAL REQUIREMENT 欄正常。Phase 6.2 之前就存在，不是遷移造成的 regression。

**目標：** 修復 `ReviewRow.tsx` 展開區塊的 data binding（`row.steps` / `row.expectedResults` / `row.preConditions` / `row.inputTestData` 這 4 個欄位渲染為何沒出現在 GENERATED TEST CASE 那欄）。

**Scope:**
- `frontend/src/components/modules/review/ReviewRow.tsx`
- 可能牽涉 `frontend/src/services/jobAdapter.ts`（資料是否正確寫入 store）
- `frontend/src/store/useJobStore.ts`（資料是否保留）

**禁止：**
- 不動視覺樣式（已於 Phase 6.4 對齊）

**進入條件：** 獨立，高優先（影響實際 review flow）。

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

### P7 — Typography: Tailwind font-size class → semantic class 統整

**動機：** Phase 6.5 audit (`/tmp/font-size-audit.txt`) 發現 codebase 仍混用 Tailwind `text-xs` / `text-sm` (共 **49 處**，扣掉 Phase 6.3 修掉的 `text-lg` 3 處) 與 Phase 2 語意 class (`.type-h1` / `.type-body` / `.type-meta` / `.type-badge` / `.type-mono`)。同時使用兩套 font-size 詞彙，閱讀成本高，且 Tailwind `text-xs` 與 token `--font-md` 數值對得上只是巧合（Tailwind 改版後會偏移）。

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

### P9 — Refactor 4 個 TSX inline sunken bezel 為 `.border-sunken` class

**動機：** Phase 6.7 附帶 sunken-bezel token 修正時發現 4 個 TSX 檔以 `borderColor: 'var(--win95-gray-dark) var(--win95-white) var(--win95-white) var(--win95-gray-dark)'` inline 重寫了 canonical sunken pattern，而非引用現有的 `.border-sunken` / `.bezel-sunken` class：

- `frontend/src/components/modules/configure/GroupingTab.tsx`（Manual Override 表外框）
- `frontend/src/components/modules/quickGenerate/DecomposeAnalysisPanel.tsx`（panel 外框）
- `frontend/src/components/modules/review/RegenDiff.tsx`（field container，selected state）
- `frontend/src/components/modules/rules/RulesModule.tsx`（iframe 容器）

這次 sunken token 誤用能擴散 16 處（CSS 12 + TSX 4），inline 重寫是放大效果的主因 —— canonical pattern 集中在 class 裡，改一處全 app 生效；inline 版本每份各自改各自，散彈式維護。

**目標：** 把這 4 個 inline `borderColor: ...` 改用 `className="border-sunken"`（或必要時 `.bezel-sunken`）。

**禁止：**
- 不改視覺（class 與 inline 規格已在 fix commit 後完全一致）
- 不改這 4 個 TSX 的其他邏輯

**進入條件：** Phase 6 全部完成後；P7（typography）後順手做較方便（兩者都是 TSX 的 className refactor）。

### P10 — Review toolbar 與 `.win95-th` header 邊界交接視覺審視

**動機：** Phase 6.7 sunken-bezel token 修正後驗收時低優先觀察 — `ReviewToolbar`（`Show:` / `Test Set:` + `Total: X | Accepted: X | Expanded: X` 那條）與其下方 table `.win95-th` header 的視覺邊界交接可能不乾淨。兩者一個 sunken（toolbar 用 `border-sunken`，TL 現為 gray-dark）、一個 raised（`.win95-th`，BR 用 gray-mid），相接處可能出現雙暗邊 / 雙亮邊堆疊。

**目標：** 視覺審視交界處，如果需要加 `margin-bottom` / 改用 single-border 接邊，記下規格調整。

**Scope:**
- `frontend/src/components/modules/review/ReviewToolbar.tsx` 或 `ReviewModule.tsx` 表格容器
- 可能調整的 CSS 只 1–2 行

**進入條件：** Phase 6.8 完成後回看。低優先 — commit 2 驗收未擋。

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
