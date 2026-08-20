# 57 下放包 — Input Test Data 之孤兒值與 §4.5 欄位歸屬

**本包無裁決條文。**

## 一、AE-1（defect）`input_test_data` 之值未在步驟或前提中被使用

**實例**（`TC-166`）：

| 欄 | 內容 |
|---|---|
| `input_test_data` | `Screen pressed about five seconds after the popup appears` |
| `test_procedure` 1 | `Press the screen while the Valet Mode welcome popup is displayed` |

**「約五秒」不出現於任何步驟。** 測試員讀到該筆資料，
**卻無任何指示告訴他在哪裡用它** —— 該值為孤兒。

**對照，接上者**（`TC-173`）：
`input_test_data` 為 `Username entered for the new Profile: Alex`，
步驟 1 為 `Start a New Profile Setup and **enter the username Alex**`。

### 1.1 併發之第二個問題：§4.5 之欄位歸屬

§4.5 逐字：**互動資料**（tester 選取之按鈕、選項、時點）→ **Procedure step**；
`Input Test Data` 留給**獨立資料集**（CAN 值、邊界值、批次測試資料）。

`TC-166` 之「按下畫面之時點」為**互動資料**，
**本就不該在 `input_test_data`** —— 它應寫進步驟。

**故 AE-1 有兩種處置，須逐條判**：

| 情形 | 處置 |
|---|---|
| 值屬**獨立資料集**（邊界值、CAN、測試檔案）而未被步驟引用 | **補入步驟或前提**，使其被使用 |
| 值屬**互動資料**（按了什麼、選了什麼、何時按） | **移入 procedure**，`input_test_data` 改 `NA`（§4.5 明文允許）|

### 1.2 附帶：`about` 為模糊語

`about five seconds` 之 `about` 屬 §2 之 vague wording。
該時點為**測試設置**（J-12，條文未指定），
移入步驟時應寫為可執行之形式（如 `five seconds after the popup appears`）。

## 二、閘之缺口 —— 方向從未被查過

**十八支閘無一查此。**
`G17`／`G18` 查「TC 內之字面值有無 spec 出處」—— **方向往上游**；
**從無一支查「欄位之間有無接上」** —— 方向在 TC 內部。

**與 T-1 同類**（ER 引用了 procedure 未建立之基準線），只是換了一組欄位。
`U-2` 曾查過反向（步驟記錄而 ER 未用），**而 `input_test_data` 這一組從未被納入**。

### 立閘 `IT-1`

對 `input_test_data != NA` 之每一條：
其中之**具體值**（數字、引號字串、識別碼、檔名、專有名詞）
須至少出現於 `test_procedure` 或 `pre_conditions` 之一。

**方向性案例**：
- **紅向**：`TC-166` 之現況 → 須紅（**G-K**：報命中數前先證明它對此條會叫）
- **綠向**：`TC-173` → 須綠
- **範圍向**：`input_test_data = NA` 者不得因本閘轉紅

**盲區具名**（R-G11）：以同義語句表達同一值者抓不到
（如資料寫 `five seconds`、步驟寫 `after a short pause`）。

## 三、作業

1. **全批掃描** —— 189 條中 `input_test_data != NA` 者，逐條判其值是否被使用；
   命中者依 §1.1 之表分兩類處置，**逐條具名所擇**
2. `IT-1` 立閘，含三向案例；**首跑之紅色輸出須貼出**
3. §1.2：`about` 等模糊語隨移入步驟一併改寫
4. **`audit_consistency` 之 §4.5 檢查** —— 若現有閘未驗欄位歸屬，一併補：
   互動資料出現於 `input_test_data` 者列待判
5. 交付前自檢**增列 IT 一項**

## 四、ENTRY 005（與 AD-1 同批落地，G-J）

AD-1（第二段之資訊量）若尚未落地，**與本項合併為同一次重出**，不分兩次。

## 五、不在本包授權範圍

- 交付、git、RD 寄出 —— 屬 Pei
- 自行改變任一條之驗證目標（僅搬移與改寫，不換 leaf、不換節、不換觸發）

## 六、上繳

`docs/upstream/57_input_data_orphans.md`，更新 `docs/INDEX.md`，附獨立判斷。

## 七、記入 profile

> 閘查過「字面值有沒有出處」（往上游），也查過「ER 有沒有引用步驟」（TC 內），
> **但沒有人問過 `input_test_data` 這一欄有沒有人用它。**
> **欄位之間的接合，要一組一組地查 —— 查過兩組不代表查過全部。**
