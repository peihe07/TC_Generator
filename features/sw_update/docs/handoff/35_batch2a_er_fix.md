# 下放包 35 —— 異議採認、R-SU41（區分須在判定對象內）、六 TC 之 ER 改寫、x14 之教訓

- 日期：2026-08-29
- 方向：分析層 → 執行層
- 前一包：`34_batch2a_fix.md`；對應上繳：`docs/upstream/31_batch2a_v2.md`
- 裁定狀態：R-SU41 —— 分析層即裁
- **執行層對 TC-12 vs TC-13 之異議成立；連帶更正 TC-16 之一處推定**

---

## 一、上繳包 30 審查判定

### 1.1 §自評之異議 —— **成立，採認，且其診斷句應立為條文**

> 分析層之依據寫在 **ER 第 3 行（觸發已生效之確認）**，
> 而二 TC 之真正驗證點在**第 5 行**，**第 5 行逐字相同**。
> **跟 TC-8 同構：差異在措辭所在之處，不在被驗證之物。**

**此判斷正確。** 下放包 34 §四之區分（設定顯示啟用 vs 停用）**邏輯成立**，
但它**只存在於分析層之推理與 ER 第 3 行**，
而 IN §5.5 明定 **Final Step 獨占驗證**；
第 3 行為 setup／transition 之確認，**不是判定對象**。

**「區分現存於分析層的推理中，不在交付物裡」** —— §二 R-SU41 據此立條。

**未擅改 TC 內容，正確。** §三改寫。

### 1.2 §T47a —— 「沒命中」與「不可能命中」在報告上一模一樣

半窗（`availability-check → availability-check`）**有起點也有訖點，
長得就像一個窗**，於是被納入比對卻永遠不可能命中。
執行層拆 `IX_NORMALISE_START`／`_END`（**射程寫進變數名**）並另計半窗，
**處置正確**。

**此為 PLAYBOOK (33)／(35) 之第三種形態**：
前提會沉默沿用、射程會沉默擴張、**而退化值會沉默地被當成正常值計入分母**。

### 1.3 §T47c —— x14 DV 之發現，本輪最有解釋力之實測

`R` 欄為母本**唯一之 x14 資料驗證**，**只掃 `<dataValidation>` 掃不到它** ——
**而 `R` 正是出事那一欄**。

且其解釋了既有台帳「母本無 DV」之由來：
**那句話對標準 DV 成立，對 x14 不成立。**

> **教訓（入 PLAYBOOK）：一個檢查所用之 API 或命名空間，
> 決定了它看得見什麼；「查無」之範圍以該 API 為界，不是以事實為界。**
> 台帳陳述須隨之改為「**標準 `<dataValidation>` 無**」，不得寫「無 DV」。

`AF` 清單原文 `"Pass, Fail, Pending,Block,NA"` 之逗號空白不一致 ——
**取值照抄**（R-SU40(a) 之「逐字」即含此類不規則）。

### 1.4 §T47f —— 台架三項全未知，**不推定，正確**

其影響見 §三 3.4：**改寫後，該未知之後果由「不可區辨」變為「第四型」** ——
性質不同，處置亦不同。

### 1.5 §T47b 之停止條件 —— 未被要求而做，採認

產出前讀母本、不符即 `sys.exit`、**不吐半份簿**。
**「下次母本改清單它會停，不會照舊寫過期值」** ——
此即 R-SU40(d)「其後逐次比對」之正確落地形態。

---

## 二、R-SU41（新條，抄入 RULINGS.md，逐字）

```
R-SU41（sibling 之區分須位於判定對象之內）

實測（上繳包 30 §自評）：`newR1L-SU-012`／`013` 之區分
（AP 關閉時設定仍顯示啟用 vs 使用者關閉時顯示停用）
寫於 **ER 第 3 行 —— 觸發已生效之確認**，
而二 TC 之 Final Step（ER 末行）**逐字相同**。

IN §5.5 定 **Final Step 獨占驗證**；setup／transition 之確認不是判定對象。
故該區分**不在被驗證之物裡**，與 `184`（TC-8）同構。

裁定：

(a) **二 sibling TC 之區分，須出現於其 Final Step 之判定對象內。**
    僅出現於 Pre-Condition、setup 步驟、transition 之 ER 者，
    **不構成合法之區分** —— 讀 TC 之人看不出二者驗的是不同的事。

(b) **判別問句**：遮住 Final Step 以外之全部內容，
    二 TC 之 Final Step 是否仍能看出驗的是不同的事？
    **答否即不合法。**

(c) **合法之作法**：把觸發側之狀態**帶進 Final Step 之判定對象**
    （如「在設定仍顯示啟用之情形下，版本未變」），
    使該狀態成為判定之一部分，而非僅為前置之確認。

(d) **本條與 R-SU32(iii) 之別**：後者為「二者實質上不可區辨」；
    本條為「**實質可區辨而交付物未載其區分**」。
    **前者須 DR，後者改寫即可。** 誤判為前者會浪費一個 DR，
    誤判為後者會讓一個偽通過過關。

(e) 本條之檢查目前**無機器覆蓋** —— `I-cross` 比對整個 ER，
    不區分其行之角色。逐包揭露。
```

---

## 三、六 TC 之 ER 改寫

### 3.1 改寫原則

將**觸發側之可觀測狀態帶進 Final Step**（R-SU41(c)），
使二 TC 之判定對象相異。Procedure 之末步同步改（Final Step owns validation）。

### 3.2 TC-12（`newR1L-SU-012`，`316` 網路遺失）

**test_procedure 第 5 步**
```
5. Check that Version_after equals Version_initial while the head unit settings still show Wi-Fi as enabled, and that the head unit remains operable
```
**expected_result 第 5 行**
```
5. Version_after equals Version_initial while the head unit settings still show Wi-Fi as enabled with no connection present; the head unit remains operable and its screen responds to user input
```

### 3.3 TC-13（`newR1L-SU-013`，`317` 使用者關閉）

**test_procedure 第 5 步**
```
5. Check that Version_after equals Version_initial while the head unit settings show Wi-Fi as disabled, and that the head unit remains operable
```
**expected_result 第 5 行**
```
5. Version_after equals Version_initial while the head unit settings show Wi-Fi as disabled; the head unit remains operable and its screen responds to user input
```

> **改寫後之區分**：判定對象含「設定所顯示之狀態」——
> `enabled 而無連線`（網路側中斷）vs `disabled`（使用者側關閉）。
> 遮住其餘內容，二者之 Final Step 仍可看出驗的是不同的事（R-SU41(b)）。

### 3.4 台架未知之後果隨之改變 —— **由不可區辨變為第四型**

若台架**無獨立可操作之 AP**（T47f 之第一項未知），
則「AP 關閉而 HU 設定仍顯示啟用」之情形**做不出來** ——
**TC-12 即為第四型（觸發手段不可得，R-SU39），不是與 TC-13 不可區辨。**

**此為改寫之附帶收穫**：區分寫進判定對象後，
台架限制之後果由「二者相同」變為「其一做不出來」，**性質清楚、處置明確**。
T47f 之答案回來前，TC-12 之 `reasoning` 須記明此依賴。

### 3.5 TC-15（`319` 電源遺失）

**test_procedure 第 6 步**
```
6. Check that Version_after equals Version_initial after the head unit has powered off and started up again, and that the head unit remains operable
```
**expected_result 第 6 行**
```
6. Version_after equals Version_initial after the head unit has powered off and started up again; the head unit remains operable and its screen responds to user input
```

### 3.6 TC-16（`320` 主機斷開）—— **另更正一處分析層之推定**

**分析層之誤**：原 procedure 第 4 步／ER 第 4 行寫
`wait until the head unit completes start-up`／`completes start-up` ——
**拔除主機連接器是否使 HU 重新開機，來源文件未載，此為推定**（§8.4.1）。

**更正**：不宣稱開機，只寫可觀測之連線恢復與可操作性。

**test_procedure 第 4 步**
```
4. Reconnect the host system connector and wait until the head unit screen responds to user input
```
**expected_result 第 4 行**
```
4. The host system connector is reconnected and the head unit screen responds to user input
```
**test_procedure 第 6 步**
```
6. Check that Version_after equals Version_initial after the host system connection has been lost and restored, and that the head unit remains operable
```
**expected_result 第 6 行**
```
6. Version_after equals Version_initial after the host system connection has been lost and restored; the head unit remains operable and its screen responds to user input
```

### 3.7 TC-11／TC-14 —— 預先同構處置

執行層所指「DR-SU2(d) 一有答案就會立刻面對同一問題」**成立，本輪預先處置**：
二者之 Final Step 判定對象同樣帶入其觸發側狀態，其觸發側部分仍為 `PENDING`。

**TC-11（`315`）ER 末行**
```
5. Version_after equals Version_initial after the injected socket read/write error, PENDING: DR-SU2 observable state confirming the error condition; the head unit remains operable and its screen responds to user input
```
**TC-14（`318`）ER 末行**
```
5. Version_after equals Version_initial while the vehicle is in the emergency state, PENDING: DR-SU2 observable state confirming the emergency condition; the head unit remains operable and its screen responds to user input
```
Procedure 末步同步改（措辭比照）。**`PENDING` 行數不變（各 3 行）**。

---

## 四、任務（T48）

| # | 任務 |
|---|---|
| T48a | **六 TC 之 ER／Procedure 改寫**（§三）：`011`–`016` 之末步與末行，`016` 另改第 4 步／第 4 行。`017` 不動。跑 lint，**預期 U=9 不變**（PENDING 行數未變） |
| T48b | **R-SU41(b) 之人工複核**：對現有 17 個 TC，逐對遮住 Final Step 以外內容，列出**其 Final Step 逐字相同或僅差 PENDING 佔位**之配對。**此為人工清單非機器檢查**（R-SU41(e)），執行層列出候選，**不裁定** |
| T48c | **台帳更正**（§1.3）：既有記「母本無 DV」之處，全部改為「**標準 `<dataValidation>` 無；x14 DV 有 1 處（`R` 欄）**」。`CONTROLLED_VOCAB.md` 之 `AF` 清單照抄原文（含不規則空白） |
| T48d | **T-抄**：R-SU41 逐字 append；索引表現行 40 → **41**。PLAYBOOK 追加三則：(1)「區分若只寫在 setup 或 transition，讀 TC 的人看不出來 —— 區分須在判定對象內」（出處：R-SU41）；(2)「一個檢查所用之 API 或命名空間決定它看得見什麼 —— 『查無』之範圍以該 API 為界，不是以事實為界」（出處：§1.3）；(3)「退化值會沉默地被當成正常值計入分母 —— 『沒命中』與『不可能命中』在報告上一模一樣」（出處：§1.2） |
| T48e | **git**：本輪與 T47 之產出 commit |

**不在本輪**：`Interruption Handling` 其餘 12 列、`Update HMI` 6 列、寫回。

---

## 五、上繳包要求（`docs/upstream/31_batch2a_v2.md`）

1. T48d 核對結果 + 索引表（現行 41）
2. T48a 之改寫明細與 lint 全輸出（**預期 U=9**）
3. **T48b 之 Final Step 相同配對清單 —— 本輪核心**
4. T48c／T48e 之結果
5. 未結 DR 清單（3 筆）
6. 獨立自評 —— 特別回答：**T48b 之清單若列出 TC-15 vs TC-16
   （二者 Final Step 改寫後仍高度相似，僅「powered off and started up」
   vs「host system connection has been lost and restored」之別）——
   該差異是否已足以通過 R-SU41(b) 之遮蔽測試，
   還是它與 TC-12／13 改寫前屬同一問題**
