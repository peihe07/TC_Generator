# scripts/ 快照 — 2026-08-21

依 **R-TM35** 保全。來源 `features/time_management/scripts/`，該目錄於
A-TM20 凍結中且未進 git。

複製時點：2026-08-21 10:0x（`cp -p`，保留 mtime）。
來源端全程唯讀，複製後複驗其 mtime 仍為 09:13:36 / 09:14:32 / 09:15:18。

## 混合來源

| 檔案 | 產出者 | 特徵字串 `Structure ported from` |
|---|---|---|
| ~~`build_batch_context.py`~~ | ~~**本 session 執行層**~~ | ~~命中 1~~ ← **見下更正** |
| `write_back.py` | **非本 session** | 命中 0 |
| `lint_tcs.py` | **非本 session** | 命中 0 |

~~後二者為 2026-08-21 09:13–09:14 另一 session 覆蓋所得。
本 session 原產出之兩份（`write_back.py` 351 行、`lint_tcs.py` 312 行，
皆英文）已失落，無備份。~~

> **更正（2026-08-21，`05Z` 上繳 §1）**：經 SHA256 三方比對
> （本快照 = git HEAD = `7344b995d0b4faf2`），`build_batch_context.py`
> **亦非**本 session 之產出。**三支腳本全部**為 2026-08-21 09:13–09:15
> 另一 session 覆蓋所得；本 session 執行層原產出之三份皆已失落，無備份。
>
> 上表之「特徵字串命中 1」為 `04` 輪之判定，其時該檔尚未被覆蓋；
> **覆蓋於數秒後發生，而此後未再複查** —— 該錯誤陳述被引用三輪。

本快照保全的是**覆蓋後**之狀態，非本 session 之原產出。

## 為何是複製而非 commit

R-TM35：git 屬 Pei，複製不屬；風險為現時，等待有成本。且 commit 會將
歸屬未定之產出納入版本史並附 commit 作者 —— 那正是執行層排除 `scripts/`
於 `34e2da6` 之理由。複製不牽動歸屬，亦不破壞凍結之 mtime 證據鏈。

commit 與否仍屬 Pei，本快照不排除日後 commit。

## 狀態

- ~~**歸屬未定** —— A-TM20，待 Pei 裁（`features/time_management/` 由哪一個
  session 負責）~~

  > **歸屬已定（2026-08-21，R-TM44）**：features/time_management/ 由本
  > session 續持。本快照保留為 A-TM20 事件與階段 A/B/C 修法前狀態之證據，
  > 不刪除。
- **缺陷登記** —— A-TM21（六項，見 `ANOMALIES.md`）
- **必修項** —— G-TM1（四項）+ G-TM2（十二項），B1 生成前須齊備
- 逐檔 SHA256 與 mtime 見 `SOURCE_STATE.txt`

## 相關條文

R-TM35（本快照之依據）、A-TM20（凍結與歸屬）、A-TM21（缺陷）、
G-TM1 / G-TM2（必修）、R-TM31（明細須可歸屬）、R-TM33（來源標記）。
