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

## 3. 待補之 TC 逐條（依 **R-VS69** 分節）

**母體 143 條；AH 欄非空 76 條。** 判準為 **AH 欄之註記**，與其 ER 是否為 `PENDING` 無關。

| 節 | 意涵 | 條數 |
|---|---|---:|
| **§A** | 單一缺值待補（非畫面層之 `BLOCKED`，如 DR-24′ 時限） | **16** |
| **§B-1** | 畫面層**完全**未驗（`DR-5-B` ＋ ER 為 `PENDING`） | **0** |
| **§B-2** | 畫面層**部分**未驗（`DR-5-B`，已驗其變更、樣式／內容待補） | **16** |
| §A＋§B-1＋§B-2 | —— 48 輪指令 W-136(1) 之對照數 | **32** |
| **§C** | **實作缺口**（`IMPL_GAP`，R-VS66(a)／R-VS67′）—— 非待補，待開 issue 予 RD | **44** |
| **AH 欄非空（四節之聯集）** | | **76** |

> **§B-1＋§B-2 ＝ 16，與改判準前之 `screen_pending = 10` 差 6**：
> §B-2 之 16 條係 46／47 輪 D-2／D-3 改寫所致之「降」，**非待補之解除**（R-VS69）。
> 依新判準回填後 `screen_pending = yes` 為 **16** 條。
>
> **§C 之 44 條為 48 輪指令所未列** —— 其為 47 輪 W-133 依 R-VS67′ 新增之
> `IMPL_GAP` 註記。故 AH 欄非空（**76**）≠ §A＋§B-1＋§B-2（**32**），
> 差額即 §C。**本層不調和**，見上繳 41 §2。

### §A —— 單一缺值待補（16）

| batch | leaf_id | BLOCKED | 行為層對照 |
|---|---|---|---|
| `batch03` | `SWE1-VC-LeftFrontHeatedSeat-014` | DR-24′ | — |
| `batch04` | `SWE1-VC-RightFrontHeatedSeat-031` | DR-24′ | — |
| `batch06` | `SWE1-VC-HeatedSteeringWheel-015` | DR-24′ | — |
| `batch07` | `SWE1-VC-HeatedSteeringWheel-016` | DR-24′ | — |
| `batch07` | `SWE1-VC-HeatedSteeringWheel-021` | DR-24′ | — |
| `batch07` | `SWE1-VC-HeatedSteeringWheel-022` | DR-24′ | — |
| `batch10` | `SWE1-VC-LeftFrontVentedSeat-014` | DR-24′ | — |
| `batch10` | `SWE1-VC-LeftFrontVentedSeat-015` | DR-24′ | — |
| `batch10` | `SWE1-VC-LeftFrontVentedSeat-017` | DR-24′ | — |
| `batch10` | `SWE1-VC-RightFrontVentedSeat-031` | DR-24′ | — |
| `batch10` | `SWE1-VC-RightFrontVentedSeat-032` | DR-24′ | — |
| `batch10` | `SWE1-VC-RightFrontVentedSeat-034` | DR-24′ | — |
| `batch17` | `SWE1-VC-OneStageHeatedSeat-047` | DR-24′ | PENDING |
| `batch17` | `SWE1-VC-OneStageHeatedSeat-048` | DR-24′ | PENDING |
| `batch18` | `SWE1-VC-OneStageHeatedSeat-049` | DR-24′ | PENDING |
| `batch18` | `SWE1-VC-OneStageHeatedSeat-050` | DR-24′ | PENDING |

### §B-1 —— 畫面層完全未驗（0）

| batch | leaf_id | BLOCKED | 行為層對照 |
|---|---|---|---|
| —— | | | |

### §B-2 —— 畫面層部分未驗（16）

| batch | leaf_id | BLOCKED | 行為層對照 |
|---|---|---|---|
| `batch16` | `SWE1-VC-HeatedSteeringWheelManagement-031` | DR-5-B |  |
| `batch16` | `SWE1-VC-OneStageHeatedSeat-051` | DR-5-B |  |
| `batch16` | `SWE1-VC-OneStageHeatedSeat-052` | DR-5-B |  |
| `batch16` | `SWE1-VC-TwoStagesHeatedSeat-064` | DR-5-B |  |
| `batch16` | `SWE1-VC-TwoStagesHeatedSeat-065` | DR-5-B |  |
| `batch16` | `SWE1-VC-TwoStagesHeatedSeat-073` | DR-5-B |  |
| `batch16` | `SWE1-VC-TwoStagesVentedSeatsManagement-046` | DR-5-B |  |
| `batch16` | `SWE1-VC-TwoStagesVentedSeatsManagement-047` | DR-5-B |  |
| `batch16` | `SWE1-VC-TwoStagesVentedSeatsManagement-055` | DR-5-B |  |
| `batch16` | `SWE1-VC-TwoStagesVentedSeatsManagement-056` | DR-5-B |  |
| `batch17` | `SWE1-VC-HeatedSteeringWheelManagement-035` | DR-5-B | PENDING |
| `batch17` | `SWE1-VC-ThreeStagesHeatedSeat-098` | DR-5-B | PENDING |
| `batch17` | `SWE1-VC-ThreeStagesHeatedSeat-099` | DR-5-B | PENDING |
| `batch17` | `SWE1-VC-ThreeStagesVentedSeatsManagement-080` | DR-5-B | PENDING |
| `batch17` | `SWE1-VC-ThreeStagesVentedSeatsManagement-081` | DR-5-B | PENDING |
| `batch17` | `SWE1-VC-TwoStagesHeatedSeat-074` | DR-5-B | PENDING |

### §C —— 實作缺口（44）

> 其訊號名取自 LID `Atlantis` 欄組而**不在基線 DBC**（R-VS67′(2)）。
> 依 **R-VS66(a)** 照寫並**開 issue 予 RD** —— 開 issue 屬 Pei，本層只標記。

| batch | leaf_id | BLOCKED | 行為層對照 |
|---|---|---|---|
| `batch13` | `SWE1-VC-TwoStagesHeatedSeat-058` | — | — |
| `batch13` | `SWE1-VC-TwoStagesHeatedSeat-059` | — | — |
| `batch13` | `SWE1-VC-TwoStagesHeatedSeat-060` | — | — |
| `batch13` | `SWE1-VC-TwoStagesHeatedSeat-067` | — | — |
| `batch13` | `SWE1-VC-TwoStagesHeatedSeat-068` | — | — |
| `batch13` | `SWE1-VC-TwoStagesVentedSeatsManagement-040` | — | — |
| `batch13` | `SWE1-VC-TwoStagesVentedSeatsManagement-041` | — | — |
| `batch13` | `SWE1-VC-TwoStagesVentedSeatsManagement-042` | — | — |
| `batch13` | `SWE1-VC-TwoStagesVentedSeatsManagement-049` | — | — |
| `batch13` | `SWE1-VC-TwoStagesVentedSeatsManagement-050` | — | — |
| `batch14` | `SWE1-VC-ThreeStagesHeatedSeat-081` | — | — |
| `batch14` | `SWE1-VC-ThreeStagesHeatedSeat-085` | — | — |
| `batch14` | `SWE1-VC-ThreeStagesVentedSeatsManagement-063` | — | — |
| `batch14` | `SWE1-VC-ThreeStagesVentedSeatsManagement-066` | — | — |
| `batch14` | `SWE1-VC-ThreeStagesVentedSeatsManagement-072` | — | — |
| `batch14` | `SWE1-VC-ThreeStagesVentedSeatsManagement-073` | — | — |
| `batch14` | `SWE1-VC-TwoStagesHeatedSeat-061` | — | — |
| `batch14` | `SWE1-VC-TwoStagesHeatedSeat-062` | — | — |
| `batch14` | `SWE1-VC-TwoStagesHeatedSeat-063` | — | — |
| `batch14` | `SWE1-VC-TwoStagesHeatedSeat-069` | — | — |
| `batch15` | `SWE1-VC-ThreeStagesHeatedSeat-084` | — | — |
| `batch15` | `SWE1-VC-ThreeStagesHeatedSeat-088` | — | — |
| `batch15` | `SWE1-VC-ThreeStagesHeatedSeat-090` | — | — |
| `batch15` | `SWE1-VC-ThreeStagesHeatedSeat-091` | — | — |
| `batch15` | `SWE1-VC-ThreeStagesHeatedSeat-093` | — | — |
| `batch15` | `SWE1-VC-ThreeStagesHeatedSeat-094` | — | — |
| `batch15` | `SWE1-VC-ThreeStagesHeatedSeat-095` | — | — |
| `batch15` | `SWE1-VC-ThreeStagesHeatedSeat-097` | — | — |
| `batch15` | `SWE1-VC-ThreeStagesVentedSeatsManagement-075` | — | — |
| `batch15` | `SWE1-VC-TwoStagesHeatedSeat-070` | — | — |
| `batch15` | `SWE1-VC-TwoStagesHeatedSeat-071` | — | — |
| `batch15` | `SWE1-VC-TwoStagesHeatedSeat-072` | — | — |
| `batch15` | `SWE1-VC-TwoStagesVentedSeatsManagement-051` | — | — |
| `batch17` | `SWE1-VC-TwoStagesVentedSeatsManagement-043` | — | unextracted |
| `batch17` | `SWE1-VC-TwoStagesVentedSeatsManagement-044` | — | unextracted |
| `batch18` | `SWE1-VC-ThreeStagesVentedSeatsManagement-067` | — | unextracted |
| `batch18` | `SWE1-VC-TwoStagesVentedSeatsManagement-045` | — | unextracted |
| `batch18` | `SWE1-VC-TwoStagesVentedSeatsManagement-052` | — | unextracted |
| `batch18` | `SWE1-VC-TwoStagesVentedSeatsManagement-053` | — | unextracted |
| `batch18` | `SWE1-VC-TwoStagesVentedSeatsManagement-054` | — | unextracted |
| `batch19` | `SWE1-VC-ThreeStagesVentedSeatsManagement-070` | — | unextracted |
| `batch19` | `SWE1-VC-ThreeStagesVentedSeatsManagement-076` | — | unextracted |
| `batch19` | `SWE1-VC-ThreeStagesVentedSeatsManagement-077` | — | unextracted |
| `batch19` | `SWE1-VC-ThreeStagesVentedSeatsManagement-079` | — | unextracted |

## 4. 待補之來源，逐項

| 來源 | 現況 | 待補者 |
|---|---|---|
| **TLM HMI Document** | 條文以 `Refer to TLM HMI Document` 指名，而客戶 HMI 目錄無同名檔（**A-VS10**，01 輪起未複驗） | 該文件本身 |
| **DR-5-B**（失效彈窗） | 未送出；經 R-VS17 阻塞中 | 失效彈窗與失效圖示之畫面規格 |
| **Comfort 037** | 已查，對失效層為 0 條 | —— 其不含本層所需內容，非未查 |

**交付時須連同本檔揭露**：上列 TC 之訊號層可執行，**畫面層之期望值未定**。