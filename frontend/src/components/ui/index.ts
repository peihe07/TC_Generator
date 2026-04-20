/**
 * UI primitive layer — Win95-themed building blocks used across modules.
 *
 * 這層刻意保持「純視覺 + 無狀態」：
 * - 不包含 Radix / 任何互動邏輯函式庫
 * - 只是原生 HTML element + 既有 CSS class 的型別安全 wrapper
 * - 需要複雜互動（Dialog/Select/Tabs）時再另外加 Radix-based primitives
 */

export { Button } from './Button';
export type { ButtonProps, ButtonVariant } from './Button';

export { IconButton } from './IconButton';
export type { IconButtonProps } from './IconButton';

export { StatusBadge } from './StatusBadge';
export type { StatusBadgeProps, StatusVariant } from './StatusBadge';

export { Checkbox } from './Checkbox';
export type { CheckboxProps } from './Checkbox';

export { Radio } from './Radio';
export type { RadioProps } from './Radio';

export { Select } from './Select';
export type { SelectOption, SelectProps } from './Select';

export { Input } from './Input';
export type { InputProps } from './Input';

export { TitleBarMini } from './TitleBarMini';
export type { TitleBarMiniProps, TitleBarMiniVariant } from './TitleBarMini';

export { Win95Dialog } from './Dialog';
export type { Win95DialogProps, Win95DialogVariant, Win95DialogAction } from './Dialog';
