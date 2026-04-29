# Design Tokens

設計語言：透明、無線條、非卡片，靠陰影與留白做層次。

## Palette

| Token | Hex | Name | 用途 |
|---|---|---|---|
| `--color-ink` | `#001524` | Ink Black | 主要文字、TopNav 底色（半透明） |
| `--color-teal` | `#15616D` | Stormy Teal | 次要文字、metadata、低調強調 |
| `--color-papaya` | `#FFECD1` | Papaya Whip | 頁面底色、浮動元件背景（半透明） |
| `--color-tangerine` | `#FF7D00` | Vivid Tangerine | CTA、accent、focus、active |
| `--color-brandy` | `#78290F` | Brandy | hover 加深、destructive、warning |

衍生：
- `--shadow-tint: rgba(0, 21, 36, 0.12)` — 陰影顏色（Ink Black 帶 alpha，避免純黑）
- `--surface-papaya: rgba(255, 236, 209, 0.6)` — 浮動元件背景
- `--surface-ink: rgba(0, 21, 36, 0.85)` — 深色浮動元件（TopNav）

## Typography

字體：**Space Mono**（透過 `next/font/google` 載入，CSS variable `--font-space-mono`）

- weight 400 — 內文
- weight 700 — 標題、CTA
- 數字（KPI、表格欄位）使用等寬特性自然對齊

額外規則：
- metadata / 輔助文字：`font-weight: 400` + `color: --color-teal` + 字級縮小
- 標題：`font-weight: 700` + `color: --color-ink`

## Shadow Levels

| Token | 用途 |
|---|---|
| `shadow-sm` | 表面元件靜態 |
| `shadow-md` | hover 一般元件 |
| `shadow-lg` | 浮動面板（Drawer、Detail panel） |
| `shadow-2xl` | 最高層浮層（Command Palette、Modal） |

陰影顏色一律用 `--shadow-tint`，不用純黑。

## Interaction Rules

- Hover：陰影升一級 + `transform: translateY(-1px)` + transition 150ms
- Focus：`outline: none` + `box-shadow: 0 0 0 2px --color-tangerine`
- Active CTA：填色 `--color-tangerine`，hover 過渡到 `--color-brandy`

## Banned Patterns

- ❌ `border` 任何顏色（極少數情況例外：input 內框可用 `box-shadow inset`）
- ❌ 卡片外框、表格欄線、分隔線
- ❌ 純白底（用 Papaya Whip）
- ❌ 純黑陰影（用 Ink Black tint）

## Replacements

需要分隔感時：
- 留白（`gap`, `padding`）
- 微小色差（surface 透明度差）
- `box-shadow inset` 收邊
- hover 高亮（列、項目）

## Utility Classes（globals.css 提供）

```
.surface          → bg: surface-papaya + backdrop-blur + shadow-sm
.surface-floating → bg: surface-papaya + backdrop-blur + shadow-lg
.surface-ink      → bg: surface-ink + backdrop-blur + text-papaya
.text-primary     → color: --color-ink
.text-secondary   → color: --color-teal
.text-muted       → color: --color-teal + opacity 0.7
.cta              → bg: --color-tangerine + text: --color-ink + shadow-md, hover: bg --color-brandy + text papaya
.row-hover        → 表格列 hover 高亮
```
