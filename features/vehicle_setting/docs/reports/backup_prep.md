# 母本備份之準備（W-123，43 輪）

**本檔只列指令與核對表 —— 執行層未執行 `cp`、未動母本。**
實際備份屬 Pei（66 包 §4 步驟 0；三道 gate 之 G3）。

## (1) 母本現行之 sha256

| 項 | 值 |
|---|---|
| 路徑 | `/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Vehicle Settings/CFTS044/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS044_Vehicle Controls_20260819.xlsx` |
| 大小 | 108,225 bytes |
| **sha256** | `ebe5a65f30a0d4bcf9e46b51a43145ce222027ac49ad523fe5c2d2b6566a5089` |
| 量測時點 | 43 輪 W-123（執行層）|

## (2) 備份路徑之建議

`REF/` 目錄存在：`/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Vehicle Settings/CFTS044/REF`

```
BOOK="/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Vehicle Settings/CFTS044/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_CFTS044_Vehicle Controls_20260819.xlsx"
REF="/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/Vehicle Settings/CFTS044/REF"
STAMP=$(date +%Y%m%d)
mkdir -p "$REF"
cp -p "$BOOK" "$REF/036_pre_writeback_${STAMP}.xlsx"
```

> `cp -p` 保留 mtime —— 備份之時間戳即母本之時間戳，非備份動作之時間。

## (3) 備份後之核對指令

```
shasum -a 256 "$BOOK" "$REF/036_pre_writeback_${STAMP}.xlsx"
```

**兩行之雜湊須相同，且須等於 (1) 所載之值**：

```
ebe5a65f30a0d4bcf9e46b51a43145ce222027ac49ad523fe5c2d2b6566a5089
```

任一不符即**停下**：其表示母本於本輪量測後被改動，
此時 (1) 之雜湊已非當下之母本，須重新量測並回報。

## (4) 三道 gate 之現況（66 包 §2）

| gate | 現況 |
|---|---|
| G1 dry-run 通過 | ✅ 42 輪 W-120（四錨點皆可失敗）|
| G2 pilot #3＋#4 之 28 條經 Pei 覆核分類 | ⬜ 未做 —— 分析層尚未出建議分類 |
| G3 母本備份完成 | ⬜ **本檔只備其指令；執行屬 Pei** |

**三道全過方得實寫。本輪不實寫。**