# 下放包 04 — Bed Lowering Mode：四庫點名（採乙）→ 續行至 pilot 生成後停

日期：2026-08-26
取號：落檔當下 `list_directory` 實測 `docs/handoff/` 有 01、02、03，取 04
對象：執行層（Tier 1）
性質：上繳包 03 §三停下請示之回覆。下放包 03 除 §三點名一節由本包補足外，
其餘條款**全部繼續有效**，不重複轉載（R-G13 citation-by-reference）。

---

## 一、點名（R-BLM11，Pei 2026-08-26 裁「乙」）

四庫綁 `vehicle_setting/inputs/` 實際在用之四檔：

| 庫 | 檔名 | 對帳雜湊（上繳 03 §3.3 實算）|
|---|---|---|
| lid | `Logical Identifiers and CAN Mapping v1_76.xlsx` | `ffceac36e9db…7a98ef4` |
| dbc_b | `PDT27_E2A_R4_BHCAN.dbc` | `9ef1ec9830fc…a01930d0` |
| dbc_fd | `PDT27_E2A_R5_FDCAN8.dbc` | `51c8fd609292…8f181cd2` |
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3…12be6ff2` |

寫入本 feature `reference:` 節。**sha256 自實體檔重算**（下放包 03 §三-2
不變）；重算值與上表全長值（RULINGS.md R-BLM11 載全文）不符 → 停，
回報兩值，不自行更新。與 `display` 之三項版本歧異為已知且被接受
（R-BLM11 末段），上繳不需再議。

## 二、續行清單（皆 Tier 1，一路做到停點）

1. `reference:` 四項寫入 + 重算回報
2. **四庫開檔可用性檢查**（上繳 03 §5.2 自陳之未驗項，現在必須驗）：
   LID／PROXI 以 openpyxl 開啟並回報分頁名；兩支 DBC 逐行 parse 並回報
   message/signal 計數。開不了 → 停
3. 針對 pilot 13 leaf 之訊號預查：以 037 原文之訊號語彙（air suspension
   fault feedback 等）查 DBC／LID。**查有 → 依 IN §8.7.5(a) 記
   `$MESSAGE.Signal$` 候選；查無 → 記「查無」**，二者皆入 manifest ——
   生成時「查無」依 (d)/(g) 保留來源名，「沒查」不得出現
4. adapter：自 amfm／home／media／sxm 四者中擇結構最近者移植
   `make_batch_context.py`，移植來源與修改點寫入上繳
5. Pilot 13 TC 生成 → **停在 `batches/pilot/`**。manifest 要求依下放包 03
   §四（prompt sha256／exemplar sha256／IN sha256／N 欄相異值數預期 1）

## 三、停點

生成 13 TC 後停。不寫回、不續批、不自評。上繳包 04 交 Pei 逐 TC 審。

## 四、未結 DR

| DR | 項目 | 狀態 |
|---|---|---|
| DR-1 | BLM operating speed threshold value | 已登記，未送出 |
