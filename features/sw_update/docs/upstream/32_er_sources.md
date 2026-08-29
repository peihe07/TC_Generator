# 上繳包 32 —— T50 執行結果（下放包 37）

- 日期：2026-08-29｜方向：執行層 → 分析層
- 對應下放包：`37_er_sources.md`
- **(b) 無來源者由 6 句降至 2 句** ✅（與 §五-3 之預期相符）
- **⚠ T50a 之取材另揭一項六列 ER 之潛在錯誤斷言 —— 見 §3.3，本輪最重**

---

## 1. T50d —— 抄錄與索引

| 條文 | 逐字相符 |
|---|:--:|
| `R-SU42 v2（ER 之斷言 —— 增設 (a2) 與二項附款）` | **True** |

| 項 | 預期 | 實測 | |
|---|---:|---:|:--:|
| 現行 | **42**（版本升級不佔列） | **42** | ✅ |
| 留存 | 24 → **25** | **25** | ✅ |

PLAYBOOK 追加 **(43)** 射程會在傳遞中掉、**(44)** 刪掉後只剩物理定律者即為驗證點本身。

---

## 2. T50c —— `016` 之 ER 第 3 行改寫

| | 前 | 後 |
|---|---|---|
| `016` ER 3 | `The head unit loses the host system connection` | **`The host system connector is disconnected`** |

主詞由 **HU 之狀態**（需消歧「HU 是被拔者還是觀察者」）改為**連接器之狀態**
（測試者所造成，不涉 HU 之角色）。**消歧之需要被繞開，而非被回答。**

**lint：U=9 不變**，其餘 20 項全 0，`I-cross=7`（仍全為窗未完整宣告）。

---

## 3. T50a —— `4907673` 之取材（**本輪核心**）

### 3.1 全文（逐字）

> Table 4-6 shows the OTA client action, depending on the session state, after a
> resolved interruption. **These are RECOMMENDED actions; however the interrupts
> themselves shall be gracefully handled so that the OTA client continues operation.**
>
> **Table 4-6: Interrupt Handling for Recoverable Interrupts**
>
> | State | Action |
> |---|---|
> | Before management session | 1 Abort the session. 2 Start the retry mechanism… 3 Write the interruption to the log. |
> | During management session and before download session | 1 Abort the session. The OTA client shall retry during the next polling interval. 2 Write the interruption to the log. |
> | During download session and before update agent starts | 1 Save the state of the download status… 2 Abort the download session. **3 Retry when the vehicle recovers from the interruption.** … 4 Write the interruption to the log. |
> | **During deployment or update process** | **1 Complete the deployment.** |
> | During status report session | Follow guidelines for management session above. |

### 3.2 ⚠ **本物件含二句而其射程不同 —— 不可整體採用或整體否決**

| 句 | 情態 | 射程 |
|---|---|---|
| **表本身** | **RECOMMENDED** | 中斷**解除之後**，client 應採之動作（abort／retry／resume／complete） |
| **表前之 however 子句** | **`shall`** | **中斷本身**須被 gracefully handled，**使 OTA client 得以繼續運作** |

**下放包 37 §五-6 所問（表是否即為本批所需之來源）—— 答否，見 §6。**
**但該問只涵蓋了表，未涵蓋 `however` 子句，而後者才是候選來源。**

### 3.3 ⚠⚠ **表之內容與六列現行 ER 相衝突 —— 本輪最重之發現**

六列之 Final Step 皆斷言 **`Version_after equals Version_initial`**（更新未完成）。
而 Table 4-6 依**中斷發生於哪一階段**給出不同之要求：

| 中斷發生之階段 | Table 4-6 所要求之動作 | **版本是否會變** |
|---|---|---|
| Before / during management session | Abort + retry next polling | 否（本次不變） |
| During download session, before update agent | Save state, abort, **retry when the vehicle recovers** | **可能變** —— 恢復後續傳至完成 |
| **During deployment or update process** | **Complete the deployment** | **會變** |

**而六列之 Procedure 第 3 步只寫 `while the update session is in progress`
—— 未釘死中斷發生於哪一階段。**

**後果有二，皆須裁**：

1. **`Version_after equals Version_initial` 不是恆真** ——
   若中斷落在 deployment 階段，規格**要求** client 完成部署，版本**會變**，
   **該 ER 判 fail，而系統其實是合規的**。這是一個**偽失敗**。

2. **`015`／`016` 尤其危險，因其 Procedure 主動解除了中斷**
   （第 4 步 reconnect battery／reconnect connector）。
   依表列「Retry when the vehicle recovers from the interruption」，
   **恢復後 client 應續傳** —— 而 TC 於恢復後立即讀版本並斷言其未變，
   **未給任何時間界限**（R-SU36 之同族問題）。
   **讀得早則通過，讀得晚則失敗，二者皆合規。**

> **與 TC-8 之問題同源**：中斷落在哪一階段，**在外部不可區辨**
> （R-SU32(iii) 已裁 `184` 之階段界線不可觀測）——
> **故測試者不但無法控制適用 Table 4-6 之哪一列，也無法事後判定適用了哪一列。**

### 3.4 4.12 全章之其餘物件（取材，不裁定）

| 物件 | 內容要旨 | 與本批之關係 |
|---|---|---|
| `4907665`／`4907666` | 章前言、`Examples of interrupts include:` | 統攝語之來源 |
| `4907667`–`4907672` | **六種中斷之列舉** | `315`–`320` 之錨（GT-A1 已裁） |
| `4907673` | Table 4-6 ＋ `however` 子句 | **見 §3.1–3.3** |
| `4907676` | 空間不足 → abort + report failure | 另一中斷型，不在本批 |
| `4907677` | session 進行中收到額外 NIA → 忽略並排隊 | 同上 |
| `4907679`–`4907684` | **4.12.1 Resuming a Download**（save／suspend／byte-range resume／內外部中斷之別） | **`321`／`327`／`328`／`329` 之範圍** |
| `4907686`–`4907691` | **4.12.2 Report Persistency**（報告之保存與重送、reflash 失敗之錯誤旗標、CAN ECU 重試 3 次） | `330`–`332` 等之範圍 |

**全章無一物件述及「中斷後 HU（host system）之可操作性」** ——
最接近者仍為 `4907673` 之 `however` 子句，其主詞為 **OTA client**，非 HU。

---

## 4. T50b —— `ER_ASSERTIONS.md` 之重分類

| 類 | v1 | **v2** | 變動 |
|---|---:|---:|---|
| (a) 物理必然 | 1 | 1 | — |
| **(a2) 測試者操作之直接反映** | — | **4** | **由 (b) 無來源改判** |
| (b) 有來源 | 17 | 17 | — |
| **(b) ⚠ 無來源** | **6** | **2** | **降 4 句** |
| (c) 不適用／佔位 | 14 | 14 | — |

**改判 (a2) 之四句**：`013` 之 `settings show Wi-Fi as disabled`、
`012` 之 `settings still show Wi-Fi as enabled with no connection present`、
`012` 之 `shows no Wi-Fi connection`、`016` 之 **`The host system connector is disconnected`**（本輪改寫後）。

**四句皆過 (a2) 之二項拘束**：測試者所造成 ✅；於 Final Step 僅為
`while …`／`after …` 之限定條件，判定核心仍為版本比對與尾句 ✅。

**§4.3 之「無處可放」消解** —— 且其成因確如下放包 37 所裁：
**不是二條文衝突，是 R-SU42 v1 之分類不完備。**

**餘 2 句仍為 (b) 無來源**：`remains operable and its screen responds to user input`
（6 TC）與 `its screen responds to user input`（`015`／`016` 第 4 行，2 TC）——
**共 8 行次**。其處置見 §6。

---

## 5. 未結 DR 清單（**3 筆**，且**預告第 4 筆**）

| DR | 標的 | 進度 |
|---|---|---|
| DR-SU1 | 安全相關通知條件清單 | `003` 三個 `PENDING` |
| DR-SU2 v3 | (a) 顯示途徑／(b) 正向狀態／(c) 區辨手段 3／(d) 觸發手段 2 | — |
| DR-SU3 | 統攝列 `313`／`327` 之併入確認 | `017` 三個 `PENDING` |
| **DR-SU4（預告）** | **「handled」之判準** —— 中斷經處理後系統應處於何可觀測狀態 | 依下放包 37 §3.2，`4907673` 若無所得即開；**執行層之判定為「須開」**，見 §6 |

---

## 6. 獨立自評 —— §五-6：Table 4-6 是否即為本批所需之來源

**答：表不是，但同一物件裡的另一句是 —— 而它仍差一層，故 DR-SU4 須開。**

**(甲) 表本身確實不是，且理由比章號相近更硬。**

Table 4-6 之標題為 `OTA client action … **after a resolved interruption**` ——
其射程為**中斷解除之後**。而本批六列所需者為**中斷當下系統未損毀**。
二者**不但不同，還在時間軸上分居兩端**。

且表之情態為 **RECOMMENDED**，**不是 `shall`** ——
以 RECOMMENDED 之內容作為 ER 之判定依據，本身即不當。

**故 `4907673` 之表與 `4907440` 同為射程不符者，
其「章號相近」正是下放包 37 §五-6 所警告之陷阱。確認。**

**(乙) 但表之前那句是 `shall`，且射程對得上。**

> `however the interrupts themselves **shall** be gracefully handled so that
> the OTA client continues operation.`

- **時點**：`the interrupts themselves` —— **中斷本身**，非解除之後 ✅
- **情態**：`shall` ✅
- **內容**：`gracefully handled so that the OTA client continues operation`
  —— 即「中斷不得使其停擺」，**正是六列尾句之精神**

**(丙) 惟其仍差一層，且該層不可由執行層跨過。**

| | `4907673` 之 `however` 子句 | 六列之斷言 |
|---|---|---|
| 主詞 | **OTA client** continues operation | **the head unit** remains operable |

**OTA client 是 HU 上的一個行程；HU 是承載它的系統。**
`4907440` 恰好講了另一半（OTA client 不得影響 host system 之正常功能），
**但其時點為 `when active`（正常路徑），非中斷後。**

即：**二個物件各覆蓋一半，而其交集為空** ——
`4907673` 對時點但主詞是 client，`4907440` 對主詞但時點是正常路徑。
**把二者拼起來得出「中斷後 HU 仍可操作」，是綜合，不是引用。**

**執行層不做該綜合** —— 綜合二條需求以產生第三條，即代上游寫需求。

**(丁) 故 DR-SU4 須開，而其問法應據本輪之取材收窄。**

不是泛問「handled 的判準是什麼」，而是：

> `4907673` 要求中斷須被 gracefully handled 使 **OTA client** 得以繼續運作。
> 於系統測層級，測試者觀測的是 **head unit**。
> **請確認**：「OTA client continues operation」於 HU 上之可觀測表徵為何？
> 是否即「HU 仍可操作且畫面回應輸入」，或另有判準？

**其為一個窄且可答之問題**，優於原訂之「求 handled 之判準」。

**(戊) 而 §3.3 之發現使本題多了一個必須一併問的**：

Table 4-6 對 **During deployment or update process** 之要求是
**`Complete the deployment`** —— 即**版本會變**。
而六列 ER 斷言版本不變。**若中斷落在該階段，現行 ER 會判一個合規系統為 fail。**

**故 DR-SU4 應併問**：六列之 Procedure 是否須釘死中斷發生之階段？
若須，**其階段界線在外部不可觀測**（R-SU32(iii) 已裁）——
**則六列全部落入第三型，而不只是尾句缺來源。**

**這是本輪最要緊的一件事**：六列現行之問題不只是「尾句沒來源」，
而是**其判定核心（版本未變）本身可能與規格相衝突**，
且該衝突之成因與 TC-8 同源 —— **階段界線不可觀測。**

**執行層未擅改任何 ER** —— 本項屬分析層。

---

## 7. 待裁事項

| # | 事項 | § |
|---:|---|---|
| 1 | **DR-SU4 之開立與其問法**（建議依 §6(丁) 收窄為「OTA client continues operation 於 HU 上之可觀測表徵」） | §6 |
| 2 | **⚠ 六列 ER 之判定核心與 Table 4-6 相衝突** —— `Complete the deployment` 使版本會變；`015`／`016` 另有「恢復後續傳」之時間界限問題 | §3.3、§6(戊) |
| 3 | **六列是否須釘死中斷發生之階段** —— 若須，其界線不可觀測 → **六列全落第三型** | §6(戊) |
| 4 | `4907673` 之表為 **RECOMMENDED** —— 是否於任何 TC 中皆不得作為 ER 之判定依據，宜立為通則 | §6(甲) |
