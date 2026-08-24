# W-VF71 第 4 項 —— `PLUMBING` 之「應刪而未刪」側實測

**日期**：2026-08-24　**依據**：V34 §4 第 4 項；`R-VF95` 二（列舉須標其性質）

---

## 1. 本檢之側

`PLUMBING` 為一**列舉式**判準。其二側：

| 側 | 問 | 狀態 |
|---|---|---|
| 不該刪而刪（假陽） | 需求句是否被誤刪？ | **已測** —— §6-2 之句界比對 **61／61 全符** |
| **應刪而未刪（假陰）** | **管路句是否有漏列之句型？** | **本檢** |

`R-VF95` 二逐字：「pattern 攔已知者，pilot 之人讀補未知者。**二者缺一，
則列舉之不完整無人發現。**」本檢即該條所令之人讀側。

## 2. 方法與其修正

V34 令「以 `test_item` 長度之離群者為線索」。**實測該線索不足**：
150 條之長度分布 中位數 324／Q3 406／離群界（Q3+1.5IQR）652，
**離群者僅 1 條** —— 樣本不足以歸類出句型。

**改為全量**：切分 150 條之 `test_item` 為句（共 **334 句**留存），
依主語歸類後逐類人讀。**具名此偏離**：線索換了，覆蓋面變大而非變小。

## 3. 漏列之句型（4 型，逐字）

| # | 句型 | 命中 | 判為管路之理由 |
|---|---|---|---|
| 1 | `The HW supplier shall provide the <Sig> signal to the Android Automotive layer through the vehicle communication network and VHAL interface.` | **17** | 述訊號**如何送達** Android 層，即傳輸路徑本身，非需求之觸發或結果 |
| 2 | `The HMI/LTM/ETM layer shall process the updated setting information.` | **3** | 述中介層之處理動作，無可觀察之結果 |
| 3 | `HW supplier shall notify the <Sig> signal via VHAL interface.` | **2** | 現行列舉有 `HW supplier shall process`，**本式為其 `notify` 變體** |
| 4 | `The retrieved configuration response shall be returned from VehicleConfigService to VehicleConfigManager and finally provided to the HMI layer …` | **2** | 現行列舉有 `The response shall be returned`／`The configuration response shall be returned`，**本式僅多一 `retrieved`** |

**#3／#4 為現行列舉之近變體** —— 其漏列非概念之遺漏，而是**逐字列舉對措辭變體
不具韌性**。此即 `R-VF95` 二所指之「列舉之不完整」，非判準設計之誤。

## 4. 邊界情形 —— 人讀判為**應保留**者，逐一具名

**列舉之邊界須與其內容一同回報**，否則下一輪無從判斷何以未收：

| 句型 | 命中 | 保留之理由 |
|---|---|---|
| `The HMI receives the value as <V> via signal, $<Sig>$.` | 14 | **述需求之觸發**，為 TC 之刺激本身 |
| `The HW Supplier / ECU shall send the updated <X> status via the <Sig> signal.` | 4 | 述**狀態送出**（上行型之刺激來源），非傳輸路徑 —— 與 #1 之別在此 |
| `The HMI shall prevent/allow the customer to …` | 2 | 述需求行為與其條件 |
| `The HMI layer shall capture the customer selection … and send the request using CarPropertyManager.setProperty(…)` | 67 | 主語為 HMI layer 且述**顧客動作之結果**；**惟其含實作層名詞** —— 見 §6 |

## 5. 補列之影響（dry-run，**未套用**）

```
test_item 有變之條數        21 / 150
刪後一句不剩而退為全文者     0
長度中位數                324 → 290
長度總和                  51073 → 47474（減 3599 字元）
```

**未套用之理由**：V34 §4 第 4 項逐字為「**回報**漏列之管路句型」，非令修改。
判準之變動屬分析層；且依 `R-VF82`，其套用須另附「原應不命中而放寬後可能命中」
之實例並實測二側。**待裁後施行。**

## 6. 另具名一項（本檢外之發現）

`The HMI layer shall … send the request using CarPropertyManager.setProperty()
with the propId …` 之 **67 句留在 `test_item` 內，其含實作層名詞**。

自檢**項 9（可執行欄位無實作層名詞殘留）之射程為 `test_procedure`／
`expected_result`，不含 `test_item`** —— 故其未被攔，**非項 9 失效**。

**是否應擴及 `test_item` 待裁**：`test_item` 之性質為「條文之逐字節錄」
（`A-VS161`：只刪句、不改字），**而條文本身即含該名詞**。
若擴及，則刪之者為「刪句」抑或「改字」須先明確 —— 故本層不自行擴，具名待裁。
