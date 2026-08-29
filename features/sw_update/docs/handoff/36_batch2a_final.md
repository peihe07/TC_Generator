# 下放包 36 —— 二項 FAIL 之處置、R-SU42（物理必然 vs 設計選擇）、batch 2a 定稿

- 日期：2026-08-29
- 方向：分析層 → 執行層
- 前一包：`35_batch2a_er_fix.md`（二項 FAIL，本包處置）
- 對應上繳：`docs/upstream/31_batch2a_v2.md`（沿用檔名）
- 裁定狀態：R-SU42 —— 分析層即裁；**二項皆分析層之誤**

---

## 一、二項 FAIL —— 全部確認

### 1.1 FAIL-1 —— 把佔位搬進判定對象，是錯的作法

算術之誤（U 由 9 變 11 或 13）確認。**但更要緊者為執行層之非算術指摘**：

> 嵌在末行中間的 `PENDING` 會讓 Final Step **同時是一個實質斷言和一個佔位** ——
> U 從此不再等於「被卡住的步驟數」，
> 而 IN §5.5 要求 Final Step 有 check target，**這個 target 會變成一半已知一半未知**。

**正確。** 且其所提之解正確且更簡：R-SU41(c) 要的是
**把觸發側之狀態帶進判定對象**，
**沒有要求該狀態必須以 `PENDING` 之形式帶進去** ——
以非佔位之措辭陳述其邏輯後果即足。

**分析層之誤在於**：見 TC-11／14 之觸發為 `PENDING`，
便反射地把 `PENDING` 一併搬進末行，
**未分辨「該步驟未定」與「該步驟之結果不可陳述」是兩件事**。
步驟掛 `PENDING`，其邏輯後果仍可在末行以既定措辭引述。

### 1.2 FAIL-2 —— `home screen is displayed` 是同類推定，§3.6 未套用到 TC-15

確認。且執行層之區分**正確且應立為判準**：

> 斷電後 HU 會重新開機是**物理上必然**的，比「拔連接器會不會重開」有依據得多，
> 所以保留 `completes start-up` 說得過去。
> **但 `its home screen is displayed` 不在這個豁免範圍內
> —— 它是一個關於 UI 狀態的具體宣稱。**

§二 R-SU42 據此立條。

### 1.3 附記 —— TC-15 vs TC-16 之遮蔽測試

執行層判「形式上通過 R-SU41(b)（差異落在判定對象內），
實質是否足夠留到執行時答」。**分析層先給實質判斷**：

**實質亦通過。** 壓力測試（§8.3）：存在使二者判決相異之系統行為 ——
**斷電發生於寫入進行中可能使分割區處於半寫狀態，
而拔除主機連接器不影響 HU 自身之寫入**。
故「版本未變且 HU 可操作」在二情境下之通過與否可以不同。
二者所驗為**不同中斷條件下之同一保護**，
而中斷條件本身即 §8.3 之 trigger 軸，**為合法之 sibling 分軸**。

---

## 二、R-SU42（新條，抄入 RULINGS.md，逐字）

```
R-SU42（ER 之斷言 —— 物理必然之後果 vs 系統設計之選擇）

實測（上繳包 31 §FAIL-2）：`newR1L-SU-015` 之
`The head unit completes start-up and its home screen is displayed` ——
前半（斷電後重新開機）與後半（開機後顯示首頁）**依據強度不同**，
而 §8.4.1 之禁造值須能分辨二者，否則不是過嚴就是過鬆。

裁定：ER 之斷言分二類：

(a) **物理必然之後果** —— 該後果若不發生，即意味硬體故障或物理定律不成立。
    例：切斷電源則裝置停止運作；恢復供電則裝置啟動。
    **不需來源文件明載即可寫入 ER。**

(b) **系統設計之選擇** —— 該後果取決於實作或規格之決定，
    可以是別的樣子而系統仍屬正常。
    例：開機後顯示哪一個畫面、顯示什麼文字、顯示多久、預設值為何。
    **須有來源文件明載方得寫入 ER**；無來源者為造值（§8.4.1）。

**判別問句**：**「這件事若不是這樣，是否意味硬體壞了？」**
  答是 → (a)；答否 → (b)。

**拘束**：
1. (a) 之範圍**限於後果本身**，不及於該後果之任何細節。
   「斷電後裝置停止」為 (a)；「斷電後裝置於 2 秒內停止」為 (b)（時間為設計選擇）。
2. 不確定屬何者時**一律歸 (b)** —— 誤歸 (a) 產生一個無來源之斷言，
   誤歸 (b) 只是多寫一次來源查核。**二者之代價不對稱。**
3. 本條不放寬 R-SU25（可觀測面）—— (a) 之後果仍須為測試者可觀測者。
```

---

## 三、TC-11／TC-14／TC-15 之定稿改寫

### 3.1 TC-11（`newR1L-SU-011`，`315`）—— 撤銷 §3.7 之 `PENDING` 嵌入

**test_procedure 第 5 步**
```
5. Check that Version_after equals Version_initial after the socket read/write error has been injected, and that the head unit remains operable
```
**expected_result 第 5 行**
```
5. Version_after equals Version_initial after the socket read/write error has been injected; the head unit remains operable and its screen responds to user input
```
`PENDING` 仍為 **3 行**（pre 3／proc 3／er 3），**末行不含佔位**。

### 3.2 TC-14（`newR1L-SU-014`，`318`）

**test_procedure 第 5 步**
```
5. Check that Version_after equals Version_initial while the vehicle is in the emergency state, and that the head unit remains operable
```
**expected_result 第 5 行**
```
5. Version_after equals Version_initial while the vehicle is in the emergency state; the head unit remains operable and its screen responds to user input
```
`PENDING` 仍為 **3 行**。

### 3.3 TC-15（`newR1L-SU-015`，`319`）—— ER 第 4 行之推定更正

**expected_result 第 4 行**
```
4. The head unit completes start-up and its screen responds to user input
```
> `completes start-up` **保留**（R-SU42(a)：斷電後重新供電則啟動，物理必然）；
> `its home screen is displayed` **刪除**（R-SU42(b)：開機後顯示哪一畫面為設計選擇，
> 來源未載）。procedure 第 4 步之
> `wait until the head unit completes start-up` 一併改為
> `wait until the head unit screen responds to user input`。

### 3.4 U 之預期回復

| TC | `PENDING` 行 |
|---|---:|
| `011` | 3 |
| `014` | 3 |
| `017` | 3 |
| **合計** | **9** |

**T48a 之「U=9 不變」於本包之改寫下成立。**

---

## 四、任務（T49，取代 T48）

| # | 任務 |
|---|---|
| T49a | **改寫產出與 lint**：`011`–`016` 依下放包 35 §三 + 本包 §三定稿（本包之措辭優先）；`016` 之第 4 步／第 4 行依 35 §3.6；`015` 之第 4 步／第 4 行依本包 §3.3。`017` 不動。**預期 U=9** |
| T49b | **R-SU41(b) 之人工複核**（原 T48b）：17 個 TC 逐對遮蔽測試，列出 Final Step 逐字相同或僅差佔位之配對。**列候選，不裁定** |
| T49c | **R-SU42 之回溯掃描**：對現有 17 個 TC 之全部 ER 行，逐行標其為 (a) 物理必然／(b) 設計選擇／(c) 不適用；**(b) 類須逐行列出其來源**（CFTS ObjectID 或來源文件位置），**無來源者列為待裁**。此為一次性回溯，其後於起草時逐行自檢 |
| T49d | **台帳更正**（原 T48c）：「母本無 DV」全部改「標準 `<dataValidation>` 無；x14 DV 有 1 處（`R` 欄）」；`CONTROLLED_VOCAB.md` 之 `AF` 清單照抄原文 |
| T49e | **T-抄**：R-SU41（原 T48d 未執行）、R-SU42 逐字 append；索引表現行 40 → **42**。PLAYBOOK 追加四則：(1)(2)(3) 同原 T48d 三則；(4)「步驟掛 `PENDING` 與其結果不可陳述是兩件事 —— 佔位不必搬進判定對象」（出處：§1.1） |
| T49f | **git** |

**不在本輪**：`Interruption Handling` 其餘 12 列、`Update HMI` 6 列、寫回。

---

## 五、上繳包要求（`docs/upstream/31_batch2a_v2.md`）

1. T49e 核對結果 + 索引表（現行 42）
2. T49a 之 lint 全輸出（**預期 U=9**）
3. **T49c 之 ER 行分類表 —— 本輪核心**（(b) 類無來源者即為新發現之造值風險）
4. T49b 之遮蔽測試候選清單
5. T49d／T49f 之結果
6. 未結 DR 清單（3 筆）
7. 獨立自評 —— 特別回答：**R-SU42 之判別問句「這件事若不是這樣，是否意味硬體壞了」
   —— 對 `the head unit remains operable and its screen responds to user input`
   這一句（現於六個 TC 之末行皆出現）應如何判**。
   若判為 (b)，則六列同時需要來源，而該句是分析層自行加入的
