# 交付揭露 —— 畫面層待補之 TC 清單

執行層產出（41 輪 D-3，依 64 包 §1）。**本檔為交付時之揭露文件。**

## 1. 實測 —— Comfort 素材對失效層為空

| 項 | 值 |
|---|---:|
| Comfort 037 之 Functional 條文 | 403 |
| 　其中含 heated／vented seat 者 | 20 |
| 　　其中含 fail／error／malfunction 者 | **0** |
| Comfort 037 全文含 fail／error／malfunction 之 Functional 條文 | 1（`SWE1-HVAC-082-02`，其標的為音量超出上下限之提示音） |

**即：R-VS59(2) 所指之 Comfort 素材，對本 feature 之失效層無任何可取用之內容。**

## 2. 逐 leaf 行為層對照之結果（W-115(2)）

| 判 | 數 |
|---|---:|
| 查得（對象與行為皆命中） | 2 |
| 查無（Comfort 無對應行為） | 72 |
| 行為未能自條文抽出（抽取式涵蓋不足，非 Comfort 之缺） | 117 |
| **標的合計** | **191** |

> 舊判準（W-112，Layer 3 群層級）回報「查得 174／查無 0」——
> 其無偵測力，見 A-VS139。本表為 W-115(2) 之新判準所得。

## 3. 畫面層標 `PENDING` 之 TC 逐條

**合計 26 條**（42 輪 W-119 之 batch18 新增 5 條；41 輪為 21 條）。

| batch | leaf_id | `dr_dependent` | 行為層對照 | 待補之來源 |
|---|---|---|---|---|
| `batch01_v3` | `SWE1-VC-Stop-StartSystem-004` |  | — | DR-19 |
| `batch01_v3` | `SWE1-VC-Stop-StartSystem-005` |  | — | DR-19 |
| `batch02` | `SWE1-VC-ThirdRowHeadrestDump-038` |  | — | DR-26 |
| `batch16` | `SWE1-VC-HeatedSteeringWheelManagement-031` | DR-5-B | — | DR-5-B |
| `batch16` | `SWE1-VC-OneStageHeatedSeat-051` | DR-5-B | — | DR-5-B |
| `batch16` | `SWE1-VC-OneStageHeatedSeat-052` | DR-5-B | — | DR-5-B |
| `batch16` | `SWE1-VC-TwoStagesHeatedSeat-064` | DR-5-B | — | DR-5-B |
| `batch16` | `SWE1-VC-TwoStagesHeatedSeat-065` | DR-5-B | — | DR-5-B |
| `batch16` | `SWE1-VC-TwoStagesHeatedSeat-073` | DR-5-B | — | DR-5-B |
| `batch16` | `SWE1-VC-TwoStagesVentedSeatsManagement-046` | DR-5-B | — | DR-5-B |
| `batch16` | `SWE1-VC-TwoStagesVentedSeatsManagement-047` | DR-5-B | — | DR-5-B |
| `batch16` | `SWE1-VC-TwoStagesVentedSeatsManagement-055` | DR-5-B | — | DR-5-B |
| `batch16` | `SWE1-VC-TwoStagesVentedSeatsManagement-056` | DR-5-B | — | DR-5-B |
| `batch17` | `SWE1-VC-HeatedSteeringWheelManagement-035` | DR-5-B | PENDING | DR-5-B |
| `batch17` | `SWE1-VC-OneStageHeatedSeat-047` | DR-5-B | PENDING | DR-5-B |
| `batch17` | `SWE1-VC-OneStageHeatedSeat-048` | DR-5-B | PENDING | DR-5-B |
| `batch17` | `SWE1-VC-ThreeStagesHeatedSeat-098` | DR-5-B | PENDING | DR-5-B |
| `batch17` | `SWE1-VC-ThreeStagesHeatedSeat-099` | DR-5-B | PENDING | DR-5-B |
| `batch17` | `SWE1-VC-ThreeStagesVentedSeatsManagement-080` | DR-5-B | PENDING | DR-5-B |
| `batch17` | `SWE1-VC-ThreeStagesVentedSeatsManagement-081` | DR-5-B | PENDING | DR-5-B |
| `batch17` | `SWE1-VC-TwoStagesHeatedSeat-074` | DR-5-B | PENDING | DR-5-B |
| `batch18` | `SWE1-VC-HeatedSteeringWheelManagement-026` | DR-5-B | PENDING | DR-5-B |
| `batch18` | `SWE1-VC-OneStageHeatedSeat-041` | DR-5-B | PENDING | DR-5-B |
| `batch18` | `SWE1-VC-OneStageHeatedSeat-046` | DR-5-B | unextracted | DR-5-B |
| `batch18` | `SWE1-VC-OneStageHeatedSeat-049` | DR-5-B | PENDING | DR-5-B |
| `batch18` | `SWE1-VC-OneStageHeatedSeat-050` | DR-5-B | PENDING | DR-5-B |

## 4. 待補之來源，逐項

| 來源 | 現況 | 待補者 |
|---|---|---|
| **TLM HMI Document** | 條文以 `Refer to TLM HMI Document` 指名，而客戶 HMI 目錄無同名檔（**A-VS10**，01 輪起未複驗） | 該文件本身 |
| **DR-5-B**（失效彈窗） | 未送出；經 R-VS17 阻塞中 | 失效彈窗與失效圖示之畫面規格 |
| **Comfort 037** | 已查，對失效層為 0 條 | —— 其不含本層所需內容，非未查 |

**交付時須連同本檔揭露**：上列 TC 之訊號層可執行，**畫面層之期望值未定**。