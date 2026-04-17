---
title: Test Case Design Method 判斷規則

---

# Test Case Design Method 判斷規則

## 1. 文件目的

本文件用於說明在建立測試案例時，如何選擇合適的 **Test Case Design Method（測試設計方法）**。

---

# 2. Test Design Methods

本文件定義以下九種測試設計方法：

1. Functional based  
2. State Transition Testing  
3. Decision Table Testing  
4. Equivalence Partitioning  
5. Boundary Value Analysis  
6. Combinatorial Testing  
7. Scenario / Use Case Testing  
8. Negative / Invalid Testing  
9. Fault Injection Lite  

---

# 3. Functional Based

## 定義

Functional based 測試用於驗證系統功能是否符合需求規格。

此方法不依賴特定測試設計技術，通常用於基本功能驗證。

---

## 使用時機

適用於以下情況：

- 驗證某功能是否存在
- 驗證功能是否可以正常操作
- 驗證畫面元素是否正確顯示
- 驗證系統是否可以進入某功能

---

## 特徵

通常具有以下特性：

- 單一功能驗證
- 不涉及條件邏輯
- 不涉及輸入範圍
- 不涉及狀態轉換
- 不涉及參數組合

---

## Example
```
Verify the system can open the settings page. 
驗證系統可以正常開啟設定頁面
Verify the icon is displayed on the main screen.
驗證主畫面上圖示可以正常顯示
```
---

# 4. State Transition Testing

## 定義

State Transition Testing 用於驗證系統在不同狀態之間轉換時是否符合預期行為。

---

## 使用時機

適用於：

- 系統具有明確狀態
- 不同狀態下系統行為不同
- 特定事件會觸發狀態改變

---

## 特徵

常見情境包含：

- 狀態 A 轉換為狀態 B
- 事件觸發狀態改變
- 不同狀態下系統行為不同

---

## Example
```
Verify the system changes to active state after login.
驗證使用者登入後系統狀態由未登入轉換為已登入
Verify the system returns to idle state after timeout.
驗證系統在逾時後由活動狀態轉為待機狀態
```
---

# 5. Decision Table Testing

## 定義

Decision Table Testing 用於測試多個條件組合與其對應結果。

當系統行為依賴多個條件時，適合使用此方法。

---

## 使用時機

適用於：

- 多條件判斷邏輯
- 設定開關影響系統行為
- 權限或規則控制

---

## 特徵

典型情況包含：

- 多個輸入條件
- 每種條件組合對應不同結果

---

## Example
```
If the feature is enabled, the system should display the notification.
當功能設定為啟用時，系統應顯示通知
If the feature is enabled, the system should display the notification.
當功能設定為停用時，系統不應顯示通知
```
---

# 6. Equivalence Partitioning

## 定義

Equivalence Partitioning 將輸入資料分成多個區間，每個區間中的輸入預期具有相同系統行為。

只需測試每個區間中的代表值即可。

---

## 使用時機

適用於：

- 輸入資料範圍
- 資料類型
- 有效與無效輸入分類

---

## 特徵

常見分類：

- 有效輸入
- 無效輸入
- 不同資料類型

---

## Example
```
Verify the system accepts valid email addresses.
驗證系統接受有效格式的電子郵件地址
Verify the system rejects invalid email formats.
驗證系統拒絕不符合格式的電子郵件地址
```
---

# 7. Boundary Value Analysis

## 定義

Boundary Value Analysis 用於測試輸入範圍的邊界值。

系統錯誤通常容易出現在邊界附近。

---

## 使用時機

適用於：

- 數值範圍
- 字串長度限制
- 數量上限或下限

---

## 特徵

常見測試值包括：

- 最小值
- 最大值
- 邊界附近數值

---

## Example
```
Verify the system accepts input length of 1 character.
驗證系統可以接受最小長度的輸入
Verify the system rejects input length exceeding the maximum limit.
驗證系統拒絕超過最大長度的輸入
```

---

# 8. Combinatorial Testing

## 定義

Combinatorial Testing 用於測試多個輸入參數之間的組合關係。

---

## 使用時機

適用於：

- 多個參數同時影響系統行為
- 不同設定組合
- 不同配置組合

---

## 特徵

常見情況：

- 多個變數同時存在
- 不同變數組合導致不同結果

---

## Example
```
Verify the system behavior under different language and region settings.
驗證不同語言與地區設定組合下系統的顯示行為
Verify the system behavior with different user role and permission combinations.
驗證不同使用者角色與權限組合下系統的存取行為
```
---

# 9. Scenario / Use Case Testing

## 定義

Scenario Testing 用於驗證使用者在實際操作流程中的系統行為。

---

## 使用時機

適用於：

- 使用者操作流程
- 多步驟功能流程
- 端對端操作

---

## 特徵

通常包含：

- 多個操作步驟
- 使用者互動流程

---

## Example
```
User logs in, opens the dashboard, and downloads a report.
使用者登入系統後進入主畫面並下載報表
User creates a new account and completes the registration process.
使用者建立新帳號並完成註冊流程
```
---

# 10. Negative / Invalid Testing

## 定義

Negative Testing 用於驗證系統在錯誤或不合法情況下的處理能力。

---

## 使用時機

適用於：

- 無效輸入
- 不合法操作
- 缺少必要條件

---

## 特徵

常見情境：

- 輸入錯誤資料
- 執行不允許操作

---

## Example
```
Verify the system rejects login with incorrect password.
驗證使用錯誤密碼登入時系統會拒絕登入
Verify the system prevents access without authentication.
驗證未登入狀態下無法存取受保護頁面
```
---

# 11. Fault Injection Lite

## 定義

Fault Injection 用於模擬系統或環境異常，以驗證系統穩定性與錯誤處理能力。

---

## 使用時機

適用於：

- 外部系統失效
- 環境異常
- 系統依賴失效

---

## 特徵

常見情況：

- 連線中斷
- 設備移除
- 系統服務不可用

---

## Example
```
Verify the system handles device disconnection during operation.
驗證設備在運行過程中被移除時系統的反應
Verify the system behavior when network connection is lost.
驗證網路連線中斷時系統的處理行為
```

---

# 12. 快速判斷流程

可依以下順序選擇測試設計方法：

1. 是否為錯誤輸入或不合法操作  
   → Negative / Invalid Testing

2. 是否模擬系統或環境故障  
   → Fault Injection Lite

3. 是否涉及系統狀態改變  
   → State Transition Testing

4. 是否依賴多條件判斷  
   → Decision Table Testing

5. 是否測試輸入區間  
   → Equivalence Partitioning

6. 是否測試邊界值  
   → Boundary Value Analysis

7. 是否涉及多參數組合  
   → Combinatorial Testing

8. 是否驗證完整操作流程  
   → Scenario / Use Case Testing

9. 若以上皆不符合  
   → Functional based