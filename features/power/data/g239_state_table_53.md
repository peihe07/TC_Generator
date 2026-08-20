# 53 包 — `4941453` 狀態表之補測標的（G239 / R-P340）

## 表之結構（51 包實測，本包覆核）

126 段 = **9 欄表頭 ＋ 13 列 × 9 欄**，可無歧義重建。
欄：`TLM Internal State` / `Source` / `Audio Power amplifier` /
`Display / Illumination` / `BoosterOUT` / `Antenna / Analog tuner` /
`Antenna / Digital tuner` / `MCU (USB)` / `MCU (AUX)`。

13 列之狀態：`Full-Operation` ×2、`Idle`、`Partial Operation`、`Timed` ×2、
`Standby`、`Sleep`、`Bench`、`Logistic Idle`、`Logistic Standby`、
`Logistic Sleep`、`Init` —— 即 **13 × 8 = 104 組狀態—輸出對**。

## R-P340(b) 之六項補測：**三項可行、三項受既有 DR 阻斷**

| 標的 | 所屬 leaf | 狀態 |
|---|---|---|
| `Bench` 之輸出組合 | `SWE-PM-007` | **可行** —— 現行 `-277` 只驗 prose 錨點之「AMP/ICS/DTV 為 ON」，未驗表之 8 欄輸出 |
| `Full-Operation` 二列之 `Source` 分辨 | `SWE-PM-001` | **可行** —— 差異為 `Source` 是否含 `SDCARD` / `BT Music streaming` / `Phone Call` |
| `Timed` 二列之 `Source` 分辨 | `SWE-PM-004` | **可行** —— 同上 |
| `Logistic Idle` | `SWE-PM-008` | **受阻** |
| `Logistic Standby` | `SWE-PM-008` | **受阻** |
| `Logistic Sleep` | `SWE-PM-008` | **受阻** |

### 三項受阻之依據

`layer3_full.tsv` 載 `SWE-PM-008` 之 `item_ids` 含
`4941426,4941427,4941428` / `4941431,4941432` / `4941434,4941435` / `4941453`
—— 即**三個 Logistic 狀態之定義錨點全屬 `SWE-PM-008`**：

- `4941427` `This status is related to TLM, FPDM AMP, ICS, and DTV OFF with Logistic Mode active.`
- `4941432` `… OFF with Logistic Mode active AND network active`
- `4941435` `… OFF with Logistic Mode active AND network off.`

而 **`SWE-PM-008` 受 `DR-PW11`（High, live）阻斷** ——
其被引用錨點 `4941425` / `4941430` / `4941433` **於兩份 CFTS 之文字層皆無內文段落**,
`source_clause` 於原理上無法完整，反向涵蓋不成立。
該 leaf 自第三批起即排除，**111 / 115 之未產出四者之一**（R-P330(c) 實測）。

**故三個 Logistic 狀態之補測非「不補」，而是其 leaf 本身尚未解阻。**
本包 §G 載「DR-PW11 blocking」而未指出其與 R-P340(b) 之交集 ——
分析層開立 R-P340(b) 時未回查該 leaf 之阻斷狀態，
**其形態與 R-P330(c)「未回查 DR 之 blocking 屬性」同型**。

## R-P340(a) ER 精確化之標的

含 `4941453` 之 leaf 共 8 個、TC 共 20 條（`-261` – `-280`）。
其中 ER 為泛稱而表已給逐輸出值者，以 `SWE-PM-005`（Standby）最明顯：
現行 `-273` 之 ER 為「No TLM, FPDM, AMP, ICS or DTV functionality is available」，
而表載 Standby 之 `Antenna / Analog tuner` 與 `Antenna / Digital tuner` 皆為 **`OFF`**、
`Idle` 之同二欄則為 **`ON`** —— 該對照為現行 ER 所未載。

**本包未執行 ER 之改寫**（見上繳 §未完成）。
