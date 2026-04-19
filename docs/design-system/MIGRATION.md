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
- Phase 6.4：GENERATED TEST CASE 欄空白（資料層 bug）+ expanded row 與 selected state 共用 `.selected` class（設計取捨）

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
   - Follow-up 待辦（發現於 Phase 6.2 bisect，與視覺遷移無關）：
     - **GENERATED TEST CASE 欄位內容渲染為空** — 疑似資料層 bug；查 `ReviewRow.tsx` 展開區塊的 data binding（`row.pendingRegenerated` / regen diff fields）
     - **Row expanded 時 header 變 navy selected 樣式** — `activeRowId` 與 `selectedIds` 目前共用 `.selected` class（見 `ReviewRow.tsx:83` `${isActive || isSelected ? 'selected' : ''}`）；需確認是否為 intended（Validation Panel sync），若否則拆開兩個 state（例如新增 `.expanded` variant 或獨立底色）
5. **Export** → `preview/fieldsets.html` + `preview/dialog.html`
6. **QuickGenerate** → `preview/form-inputs.html`
7. **ChatModule** → `preview/paper-cards.html`（user bubble = navy / bot = white sunken）
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

## 給 Claude Code 的執行指令模板

```
我要按照 design_system/MIGRATION.md 把 TC Generator 視覺對齊到 Win95 design system。

請從 Phase 2.1 開始。
讀完 design_system/preview/form-inputs.html 後告訴我預期視覺，
然後跑 npm run dev、列出 9 個 border-sunken 用點，
逐一回報視覺是否符合 preview。

完成 Phase 2 後暫停等我確認再進 Phase 3。
```
