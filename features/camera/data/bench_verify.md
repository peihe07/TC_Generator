# 交付前實機驗證清單 — Camera A 本（DECISIONS 6-33）

本檔列出**其可判性依賴實機輸出**、須由 Pei 於交付前實機驗一次之 TC。
非缺陷清單 —— 各列之 lint 與 selfcheck 皆已全綠；此處記的是「紙面可判、實機待證」者。

| TC | 依賴 | 待證之事 | 出處 |
|---|---|---|---|
| `NR1L-RVC-058` | `$ adb shell dumpsys media.camera` | 該命令之輸出是否足以判「`Rear_Camera` data path is open」 | CAM-07 審閱 §四-2 |
| `NR1L-RVC-092` | `$ adb shell dumpsys media.camera` | 該命令之輸出是否載有串流解析度（ER 判 `1280 x 800 pixels`）| CAM-08 §5-5 自報 |
| `NR1L-RVC-131`／`-132`／`-133` | **LVDS 模擬器** | 是否具備**注入** RVCM → HU 方向之 LVDS 訊號（`systemStatus.ZoomViewRes`）之能力；若無，三列於工作簿 `Remarks` 註「需 LVDS 模擬器」而**非刪** | CAM-10 審閱 §一-5／DECISIONS 6-38 |
| `NR1L-RVC-108` | bus analyzer 時戳 | `TIME_W_RVC2` ＝ **50 ms** 之觀察窗於人工不可達；須以匯流排錄製之時戳判該窗內之狀態 | CAM-09 審閱 §二 |

## 驗證方式

1. 於實機執行該列之 Procedure 至該步。
2. 記錄實際輸出（命令之 stdout ／ bus analyzer 之錄製片段）。
3. 若輸出不足以判 ER：回報，該列之 ER 改寫或標 PENDING 並開 DR。

## 沿革

- 2026-09-23 建檔（CAM-10 §1-6），初始三列。
- 2026-09-23 加 `-131`～`-133` 之 LVDS 注入能力（CAM-11 §1-4）。
