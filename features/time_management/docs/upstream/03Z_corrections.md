# 上繳 03Z — R-TM16 依據訂正、兩條新界線落檔、受測物候選補完

執行層 → 分析層。對應 `docs/handoff/03Z_closure.md`。
**僅回報差異。** 2026-08-20。

T1–T6 全數完成，**T6 六項全符**。T5 之掃描結果使候選數由三增為四，
但**其中一個候選有資格疑義**，見 §3.2。

---

## 1. T6 六項驗證（實際輸出）

```
1. grep -c '^## R-TM' RULINGS.md          : 27   期望 27   ✅
2. grep -c '^## A-TM' ANOMALIES.md        : 18   期望 18   ✅
3. grep -c '依據 2 經補驗為偽' RULINGS.md   : 1    期望 1    ✅
4. grep -c 'GPSDateTm' framework.md       : 1    期望 ≥1   ✅
5. grep -c '4813974' framework.md         : 1    期望 ≥1   ✅
6. ls features/comfort/framework.md       : 存在  反例複驗  ✅
```

判準 4、5 依 R-TM21 以本 feature 唯一字串定錨（`GPSDateTm` 與物件 id
`4813974` 於全域檔各僅一處，皆在 Part VII 之新增界線列內）。

判準 6 之反例經執行層獨立複驗：`features/comfort/framework.md` 確實存在。

## 2. T4 — Part VII 界線表（改前／改後）

**(a) 引言**

```
改前：三處鄰接，由 leaf 描述全文比對浮現：
改後：五處鄰接，由 leaf 描述全文比對浮現（前三處於 02R 定案；第四、五處
      由執行層以動詞軸橫掃全 22 列發現，R-TM23）：
```

**(b) 表列**：於第三列（018↔011）之後追加兩列，逐字如 `03Z` §6 T4。
該表現為五列。

兩處均以 `assert t.count(o)==1` 前置後 `replace(o,n,1)`，改後複查全節。

**未改 Part I–VI 之任何內容**（該節位於 Part VII 內，`03Z` 未授權改他 Part，
執行層亦未改）。

## 3. T5 — 受測物候選掃描補完

### 3.1 掃描結果

```
power         : inputs=Y  RECON=N  DECISIONS=Y
user_profiles : inputs=Y  RECON=Y  DECISIONS=Y
（未掃 vehicle_setting —— A-TM17）
```

**`power` 不合格** —— 無 `RECON.md`，不滿足 R-TM22 2(b)（`RECON.md` 與
`DECISIONS.md` 皆須存在）。
**`user_profiles` 合格**，候選由三增為 **四**。

### 3.2 執行層補測：`inputs/` 非空性 —— **2(a) 全數滿足**

R-TM22 2(a) 要求「`inputs/` 存在**且非空**」。分析層之表僅記存在性，
未記非空性，故補測（`ls -A` 計數）：

| feature | `inputs/` 檔數 | 2(a) |
|---|---|---|
| `sxm` | 4 | ✅ |
| `privacy` | 8 | ✅ |
| `comfort` | 8 | ✅ |
| `user_profiles` | 4 | ✅ |
| `power` | 11 | ✅（但 2(b) 不合格）|

四個候選之 2(a) 與 2(b) 全部滿足。

### 3.3 **`comfort` 之候選資格有疑義 —— 提請排除**

`comfort` 同時是 **A-TM18 之主體**：其 `framework.md` 僅存本地、未併入
全域檔，狀態未定（`03Z` §1.2 列 (a) 進行中 / (b) 最終形態 兩種可能）。

以之為 recon.py 修法之回歸受測物，有兩項風險：

1. **若 (a) 成立（仍在進行中）**，則該 feature 正被人作業，
   與 `vehicle_setting` 同型 —— 靜止性判準會失效，而這正是 R-TM22
   2(c) 要防的。
2. **回歸判準為「`RECON.md` 逐位元相同、`DECISIONS.md` 不變」**，
   若該 feature 之 owner 同時在改這兩個檔，diff 有輸出時無法歸因。

**執行層建議候選優先序**：`sxm` > `privacy` > `user_profiles` > ~~`comfort`~~。

理由（依 3.4 之靜止性初測）：`sxm` 最後修改為 **2026-08-13**，距今七日，
是四者中最靜止者；且其為 `.DS_Store`（系統檔），非實質內容變動。

### 3.4 執行層預備動作：mtime 快照 #1 已取

R-TM22 2(c) 要求「相隔 ≥10 分鐘取兩次 mtime 快照」。**第一次快照本包已取**
並存為 `data/candidate_mtime_snapshot_1.txt`，供日後比對之基準：

```
snapshot taken: 2026-08-20 20:36:44

sxm            files=245  newest=2026-08-13 21:16:34  features/sxm/.DS_Store
privacy        files=79   newest=2026-08-20 11:54:01  features/privacy/.DS_Store
comfort        files=436  newest=2026-08-17 20:02:41  features/comfort/ANOMALIES.md
user_profiles  files=453  newest=2026-08-20 11:54:28  features/user_profiles/.DS_Store
```

**此為 `03Z` 未指派之預備動作**（T5 只要求掃三個存在性）。逕行之理由：
唯讀、零風險，且 2(c) 之判準本質需要一個**時間上更早**的基準點 ——
不先取則日後仍須從頭等 10 分鐘。若分析層認為不當，此檔可逕刪，
不影響任何其他產出。

**初步判讀（非結論）**：四者之 newest 皆早於本快照時刻至少 8 小時，
其中三者之最新檔為 `.DS_Store`（macOS 系統產生，非作業痕跡）。
`comfort` 之最新檔為 `ANOMALIES.md`（實質內容），時間 2026-08-17。
**與 `vehicle_setting`（本 session 期間 16:49／16:51 仍在寫入）對比明顯。**

**2(c) 尚未滿足** —— 須第二次快照方能判定，本包未取（時間未到）。
且 **2 之解除仍須先過 1（A-TM17 釐清），順序不變**（`03Z` §4 明載）。

## 4. T1–T3 寫入確認

| T | 動作 | 位置 |
|---|---|---|
| T1 | R-TM16 依據訂正 | 該條末尾追加「依據 2 經補驗為偽」全段，**原文未刪**（R-TM13）|
| T2 | R-TM23 / R-TM24 | `RULINGS.md` 末尾，25 → **27** |
| T3 | A-TM18 | 置於 A-TM17 之後、`## Assumption markers` 之前；索引 17 → **18** |

### 4.1 R-TM24 之執行層對應作法（本包新立）

R-TM24 之風險面在 TC 生成階段（§4 之 `test_item` 上半須為逐字原文）。
執行層之對應作法已寫入該條回報段：

> 凡 `test_item` 上半之內容，一律取自 `data/leaf_descriptions.txt`
> （037 原始欄位之直接輸出），**不取自任何下放包或上繳包之敘述**。

該檔已於 `03R` T6 產出並複驗 22 列，其內容為 `openpyxl` 直接讀出之
`Requirement Description` 欄，未經任何改寫。**此使 R-TM24 之風險在本
feature 從「靠人記得」變為「靠來源隔離」。**

## 5. T7(4) — 該驗而未驗者（續用五全集）

### 5.1 依全集 1（指令逐項）

T1–T6 全數完成，無停下項。T6 六項全符（§1）。

### 5.2 依全集 2（寫入後複查）

| 檔案 | 複查 | 結果 |
|---|---|---|
| `RULINGS.md` | 條數 + `依據 2 經補驗為偽` 命中 | 27 / 1 ✅ |
| `ANOMALIES.md` | 條數 + 索引列 | 18 / 18 ✅ |
| `docs/fw036/framework.md` | 界線節全文 + `GPSDateTm` / `4813974` | 五列 / 1 / 1 ✅ |
| `data/candidate_mtime_snapshot_1.txt` | `cat` 全文 | 四列 ✅ |

三處 `str.replace` 全部前置 `assert` + `count==1` 唯一性檢查。

### 5.3 本包解除之「未驗」項

**R-TM16 依據 2 —— 已補驗，且為偽。** 此為執行層 `03R` §5.6 之提請，
現已關閉。訂正已依 R-TM13 加註，結論不變。

**執行層之判斷得到印證**：當時之理由是「全稱斷言被單一反例推翻，
成本與風險不對稱」。實測結果不只有反例，且該反例（Comfort）之
framework **完全未併入全域檔**，比「多一份本地檔」更強 ——
即「全域檔為唯一位置」在 repo 內亦非全稱真。

### 5.4 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | R-TM22 2(c) 靜止性 | **快照 #1 已取**，#2 須隔 ≥10 分鐘。未取（時間未到）|
| 2 | A-TM17 併行者身分 | **四次呈報未獲答覆**（01Z-A3 §6、03R §7、03Z §7、本包 §6）。執行層不查（§3 明令）|
| 3 | R-TM23 兩條新界線是否須 Pei 另簽 | 已寫入 framework，但覆簽未定。**B1 未啟動，故無既成事實** |
| 4 | A-TM18 之 (a)/(b) 判定 | 屬 Comfort，執行層不裁、不查 |
| 5 | 交付路徑 Home 複本內容 | 刻意不驗（R-TM10-A1 SUSPENDED）|
| 6 | PU 陽性對照 | 待 Pei 裁（跨 feature 取用）|
| 7 | `write_back` 兩值 | Phase 3 |
| 8 | `1.5.3.*` 與 A-TM09 之關聯 | 不主張 |

### 5.5 依全集 4（「不存在」之陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| `power` 無 `RECON.md` | 同一批測試中 `user_profiles` 之 `RECON.md` 命中 Y | ✅ |
| `GPSDateTm` / `4813974` 於全域檔各僅 1 處 | 同檔 `SWE-RA-TIME&DATE` 命中 2 處 → 掃描有效 | ✅ |

### 5.6 依全集 5（草案設計說明之逐項可驗性）

`03Z` §2 之 R-TM23 兩條界線，其 spec 依據本包**部分複驗**：

| 斷言 | 本包 |
|---|---|
| 「GPS 訊號組定義於 1.3.1.1.3 與 1.5.2.5」 | **已驗**（間接）：`data/leaf_to_section_probe.txt` 中 014 落 `1.3.1.1.6.1, 1.5.2.5`、004 落 `1.3.1.1.3,…`，與所述一致 |
| 「傳輸時機定義於 1.3.1.1.4」 | **已驗**（間接）：008 落 `…1.3.1.1.4…`，009 亦落該節 |
| 「$DateTmFormat$ 物件 4813974，章節 1.3.1.1.5.1」 | **未驗** —— 物件 id 與訊號名皆未於本包對 CFTS docx 複查 |
| 「$GPSDateTmHour/Minute/…$ 訊號組」之逐字訊號名 | **未驗** —— 同上 |

**提請**：兩條界線之訊號名與物件 id（`4813974`、`$DateTmFormat$`、
`$GPSDateTm*$`）為 §8.2.1 拘束條款之具體錨點，而 TC 生成時會據以判斷
「哪些訊號屬哪一片」。**其正確性未經執行層複驗。**

成本低（CFTS docx 已有解析管線，`data/leaf_descriptions.txt` 與
`anchor_probe.txt` 之產出程式可直接改用）。**本包未逕行**（未獲指派）。
建議於 B1 生成前補驗 —— 與界線本身之時機論證同理：錨點錯了，
B1 之 008 相關 TC 會照錯的錨點寫。

## 6. 呈報 Pei（執行層側，第四次）

**A-TM17 仍未獲答覆。** 執行層之相關事實已四次登記，此處不重述，
僅補一項本包新增之對比：

本包所取之 mtime 快照顯示，四個受測物候選之最新變動時間皆早於本包
至少 8 小時，其中三者之最新檔為 `.DS_Store`（系統檔）；
而 `features/vehicle_setting/` 於本 session 期間（16:49／16:51）仍有
實質檔案寫入。**該對比可作為釐清併行者作業範圍之量化參考** ——
若併行者僅作業於 `vehicle_setting`，則其餘候選之靜止性成立。

## 7. 本包未動之事項

未動 git。**未改任何腳本**（R-TM22 HOLD，未解除 —— 條件 1 未過）。
**未碰 `features/vehicle_setting/`**（A-TM17，含未掃描其 `inputs/`）。
**未開始 B1 生成。** 未裁 Comfort 之事（A-TM18 僅登記）。
未刪除 `features/time_management/framework.md`。未送出 RD-1。
未填 `D5`、未組 Scope 值。未援引他 feature 樣式。
未以 openpyxl 存回任何工作簿。未跑 `recon.py`。未改 Part I–VI。
