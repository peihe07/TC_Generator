# R-12：Pre-Condition 句式與 spec_reference 收斂（2026-08-21）

Pei 提問二項，分析層對 SWC 0708（286 列）與 PM 交付本（283 列）
全欄位比對後回覆。

## 一、工具類 Pre-Condition：PM 措辭與順序均與語料不符

| | SWC | PM |
|---|---|---|
| 措辭 | `CAN tool is available on HU`（251）／`CAN tool with UDS diagnostic capability is available on HU`（32） | `A LIN and CAN simulation tool is connected`（246） |
| 位置 | **末項**（第 5 項） | **首項**（241/283 列） |
| 首項 | `Ignition state = ON and HU is in Full-Operation state`（284/286） | 工具行 |

```
R-12(a) Pre-Condition 句式與排序
措辭統一為 `<工具> is available on HU`（SWC 句式）。
PM 因需 LIN 段，寫 `LIN and CAN tool is available on HU`。
排序：車輛／電源狀態 → PROXI → HMI 設定 → 來源／情境 → 工具可用性。
工具行一律置末，不得置首。
```

PM 處置：246 列之工具行改措辭並移至末項；首項改為
`Ignition state = <state>` 或 `TLM is in <state>` 之車輛狀態句。

## 二、spec_reference 條數：PM 69 列超出語料上限，且缺 HMI 配對

| | SWC | PM |
|---|---|---|
| 條數分佈 | 1:130／2:108／3:44／4:4，**上限 4** | 1:125／2:40／3:8／4:41／5:7／6:15／7:4／8:15／9:10／10:4／11:3／**13:11** |
| 超過 4 條 | 0 列 | **69 列** |
| 含 HMI 文件行 | 124/286 | **0/283** |

**成因（實測推定）**：PM 之多條 spec_ref 為**錨點候選全集**，非選定錨點。
上繳 10a 載「155 列之 anchor 係 2–13 個候選中之最佳猜測」——
`2–13` 與本表條數上界 13 完全吻合。即：錨定未收斂之不確定性
被攤入欄位，以「全部列出」代替「選定一條」。

**另有顆粒度疑慮**：一列掛 13 條需求錨點，若非候選全集而係實際
驗證範圍，則違 canon §2「One TC = one verification objective」，
屬 TC 顆粒度過粗，須拆 TC 而非改欄位。**兩種成因須逐列區分**。

```
R-12(b) spec_reference 收斂
每列僅列該 TC 直接驗證之錨點；候選未定者不得以全部列出代替選定。
條數以語料上限 4 為準；超過即須逐列判定屬
(i) 候選未收斂 → 待權威對照後選定（DR-PW19）
(ii) TC 顆粒度過粗 → 依 §8.2.2 拆 TC
CFTS 家族之列若其驗證涉及 HMI 行為，應比照 SWC 補 HMI 文件行
（`{檔名}-{章節/項目}`）為次行。
```

**PM 處置（分階段）**：
- 69 列先逐列區分 (i)/(ii)，產出分類清單 —— 分析層作業
- (i) 類凍結至 DR-PW19 結案；(ii) 類提報拆 TC 建議（拆列屬 Pei）
- PM 0/283 無 HMI 文件行一事，須先確認 PM 是否存在對應之 HMI
  Logic and Flow 文件；查無則不補，登記說明

## 三、本次比對之其餘差異（一併登記，避免再輪）

- **ER 句型**：SWC 最大宗為 `The signal $...$ = <raw> (<label>) is
  transmitted/received`（101 次）；PM 現況無訊號型 ER。
  依 R-1 v3(a) 改寫後應自然趨同。
- **baseline 句式**：SWC 有 `State_baseline is recorded`（65）、
  `Both signals ...`（59）等成組句式；PM 無。涉及前後比較之 TC
  應依 R-1 v2(f) 補 baseline 記錄步驟。
- PM 之 `Timeout1 is at a value other than "00 min"`(8)、
  `The bench is an Atlantis High configuration`(5) 等首行，
  依 R-12(a) 重排後移至適當段位。
