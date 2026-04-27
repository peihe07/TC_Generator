# IVI APP – Test Case Prioritization (TCP)

## 概述

The IVI app test case priorities in SWE.6 are defined from **P0 to P3** based on functional importance.

依功能重要性將測試案例分為四個優先級別，從 P0（最高）到 P3（最低）。

---

## 優先級定義

### 🔴 P0 - Critical Functionality（核心功能）

**定義：** Critical functionality that must be tested without fail. Any failure would impact core system or functionality operations. **A feature's core/primary flow (the must-test happy path that defines the feature working) defaults to P0** — do not downgrade it to P1 unless it is clearly a secondary/advanced operation.

必須完整測試的關鍵功能，任何失敗都會影響核心系統或功能運作。**功能的核心主流程（讓該功能成立的必測 happy path）預設就是 P0**，除非明確屬於次要或進階操作，否則不應降級為 P1。

**Examples：**
- System boot-up and recovery
- Application start up
- Features' core/primary functionality — the main happy path of any feature (e.g., Media Play, Navi, BT Pairing)

---

### 🟡 P1 - Major Functionality（主要功能）

**定義：** Secondary or advanced operations of a major feature that are NOT the core primary flow. Boundary/variation cases, key operational logic branches, and non-primary user-facing flows fall here. While not immediately system-breaking, failures can significantly affect major features or workflows.

主要功能的次要/進階操作（非核心主流程），例如邊界情境、變化路徑、主要功能的次要邏輯分支。雖然失敗不會立即導致系統崩潰，但會顯著影響主要功能或工作流程。

**Examples：**

- Boundary/variation cases of a major feature (the primary happy path itself is P0, not P1)
- Operational logic branches of major functions (non-primary paths) complying with the specifications

---

### 🔵 P2 - Secondary Functionality（輔助功能）

**定義：** Support Features. These involve secondary features whose failures have a limited impact on the major features.

次要功能，失敗時對主要功能影響有限。

**Examples：**
- Additional features of major functions
- Media: Lyrics display, Album art fetching
- BT: Recent pairing history, Syncing call logs, Custom device naming

---

### 🟢 P3 - Minor Functionality（次要功能）

**定義：** Enhancements or low-impact features. These cover non-critical aspects such as UI enhancements or rare-use scenarios, with minimal risk to operations.

非關鍵性的 UI 強化或少用情境，對運作風險極低。

**Examples：**
- Custom navigation arrow styles
- Customizable device icon
- Color scheme changes based on device brand

---

## IVI APP 測試案例分級（重要性 Importance）

### 【P0 - 核心功能】

- 系統啟動與主畫面展示
- 藍牙配對與連線（CarPlay、Android）
- Wi-Fi 連接
- 緊急通報（eCall）功能是否可正常觸發
- 音訊輸出（ex: 媒體 / 導航提示音）
- APP 啟動

### 【P1 - 主要功能】

- 藍牙音樂切換上下首歌或快轉 10 秒、回播 10 秒
- 儀表板與 IVI 畫面顯示的時間是否同步
- APP 細部功能
- 車內語音控制（ex: 撥號、導航）

### 【P2 - 輔助功能】

- 個人化設定（主題、背景音樂）
- Wi-Fi 網路列表排序（強弱排序）
- 藍芽裝置最大連線數量
- 小工具（ex: 天氣、行事曆 Widget）

---

## CAN 測試案例分級（重要性 Importance）

### 【P0 - 核心功能】

- 車速、檔位
- 點火狀態
- 車門狀態
- ECU VIN 編碼是否能正確接收並顯示
- 系統異常時是否能正確回報錯誤碼（DTC）給診斷工具
- 安全性設定開關是否正確響應 CAN 控制（ex: Safety & Driving Assistance）
- 系統從 Sleep 模式喚醒時是否正確處理 CAN 訊號

### 【P1 - 主要功能】

- 設定開關是否正確響應 CAN 控制（ex: 修改時間日期、螢幕亮度）
- 燈光開關狀態（ex: 方向燈狀態、煞車燈狀態）
- 電池電壓資訊是否能正確顯示
- 空調溫度設定回傳至 IVI 顯示是否正確

### 【P2 - 輔助功能】

- 車外溫度
- 雨刷狀態
- 主題（如夜間模式）是否根據光感訊號切換

---

## 優先級對照表

| 優先級 | 名稱 | 影響程度 | 範例類型 |
|--------|------|----------|----------|
| **P0** | Critical Functionality | 核心系統運作，失敗即不可接受 | 系統啟動、緊急通報、車速檔位 |
| **P1** | Major Functionality | 顯著影響主要功能 | 音樂控制、語音控制、燈光狀態 |
| **P2** | Secondary Functionality | 對主功能影響有限 | 個人化設定、車外溫度、雨刷狀態 |
| **P3** | Minor Functionality | UI 強化、低風險情境 | 自訂圖示、配色變更 |
