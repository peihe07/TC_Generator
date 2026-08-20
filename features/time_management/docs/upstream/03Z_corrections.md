# 上繳 03Z — 兩節：03Z（R-TM16 訂正、界線落檔）＋ 03Z-A1（腳本修法）

# ═══ 第一節：03Z ═══

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

---

# ═══ 第二節：03Z-A1 ═══

對應 `docs/handoff/03Z-A1_amendment.md`。T1–T8 全數完成，**T6 六項全符**。

**三項發現須先講**：分析層之受測物候選 `sxm` 不適格（§2.2）；
A-TM15 之字面修法會破壞回歸測試本身（§3.1）；生成管線不是全域的（§6）。

## 1. T6 六項驗證（實際輸出）

```
1. grep -c '^## R-TM' RULINGS.md               : 29   期望 29   OK
2. grep -c '^## A-TM' ANOMALIES.md             : 18   期望 18   OK
3. grep -n '^| A-TM17'                         : **RESOLVED**（Pei 確認）  OK
4. grep -c 'DECISIONS.new.md' scripts/recon.py : 2    應命中     OK
5. grep -c 'contains whitespace' new_feature.py: 1    應命中     OK
6. grep -c 'cfts_doc' scripts/intake.py        : 6    應命中     OK
```

## 2. T3 — 受測物選定

### 2.1 `stat` 形式與靜止性

依 R-TM7 實測：**macOS BSD 形式 `stat -f '%m %N'` 可用**；GNU `-c '%Y %n'`
不可用。

```
snap1: 21:03:13   snap2: 21:17:23   間隔 14 分 10 秒（>=10 分鐘）
兩份各 1217 行，diff 無輸出 → 四者（sxm/privacy/comfort/user_profiles）皆靜止
```

### 2.2 `sxm` 不適格 —— 分析層候選清單之缺陷

依 `03Z` 上繳之優先序應取 `sxm`，實測後排除，兩個獨立理由：

**(a) 已簽核 → 測不出修法。** `read_signoff` 實測：

| feature | signed | reviewed_by | amendments |
|---|---|---|---|
| `sxm` | **True** | PeiPYHsu | 11 |
| `comfort` | **True** | PeiPYHsu | 2 |
| `privacy` | False | — | 0 |
| `user_profiles` | False | — | 0 |

A-TM15 修的是「**未簽核**時會被整份覆寫」。已簽核者原本就走 divert 路徑
受 R-C9 保護，**用它跑回歸，修法前後行為完全相同，判準無鑑別力** ——
與 R-TM21「本 feature 之工作若完全沒做，判準會不會照樣通過」同型。

**(b) 素材不完整。** 實跑 `sxm` 得：

```
input not found: inputs/SYS1_HMI_SiriusXM_360L_SAT_Only_HMI Logic and_Flow_R1_SR24_1A(May_24_2021).xlsx
```

其 `inputs/` 雖有 4 檔，但 `feature.yaml` 宣告之 SYS1 檔不在其中。
**R-TM22 2(a) 之「存在且非空」不足以判定資格 —— 須是「feature.yaml 宣告
之每一個路徑都在」。** 建議該條件據此收緊。

### 2.3 選定 `privacy`

`signed=False`（能真正測到修法）、靜止、`inputs/` 8 檔且宣告路徑齊全、
`RECON.md` 與 `DECISIONS.md` 皆在。`comfort` 依 `03Z` §3.3 之理由續予排除
（A-TM18 主體，狀態未定）。

## 3. T4 — 階段一 A-TM15

### 3.1 字面修法會破壞回歸測試本身 —— 修法範圍必須延伸

`03Z-A1` T4 只寫「目標檔已存在時一律寫 `DECISIONS.new.md`」。
但 `recon.py:1135` 之 `if outcome["diverted"]: sys.exit(REFUSED ...)` ——
**`diverted` 為真即非零退出，訊息並宣稱該檔 is signed**。

照字面改的後果：任何既有 feature 重跑 recon 都會 REFUSED 退出，且對未簽核
之檔案謊稱其已簽核。**回歸判準「跑一次 recon 比對 RECON.md」本身會被這個
副作用打斷。**

**執行層之處置（逕行，範圍延伸）**：把「寫到哪裡」與「要不要拒絕」分離 ——

| 情境 | 行為 |
|---|---|
| 目標存在 + **已簽核** | divert + **REFUSED 非零退出**（R-C9 原樣保留）|
| 目標存在 + **未簽核** | divert + `NOTE (A-TM15)` 提示 + **正常退出**（A-TM15 修好）|
| 目標**不存在** | 寫 `DECISIONS.md`（新 feature 路徑不變）|

逕行而非停下之依據：R-TM26 —— 三項門檻皆否（可逆、單檔、不影響既有語料），
且停下之代價由 Pei 承擔。**若分析層認為不應延伸，還原點為
`/tmp/recon.py.pre-A-TM15`。**

### 3.2 損害如實記載 —— 確實沖掉了一次

T4 步驟 2 為刻意執行一次它要防止的損害。如實記載，非「無損害」：

```
沖掉前 privacy/DECISIONS.md SHA : a1a685a120f6e9c2ecff46d3aa82903e5f8c94d65f21aa354f02600b625b3569
未修改腳本跑完後            SHA : 622bdc448284e618f869d01dfbf86d318623e9df73635779689a3c8af971c099
                                   ^ 內容確實被整份改寫
還原後                      SHA : a1a685a120f6e9c2ecff46d3aa82903e5f8c94d65f21aa354f02600b625b3569
                                   ^ 與沖掉前逐字元相同
```

備份於 `/tmp/DECISIONS.backup`，還原經 SHA 驗證。

### 3.3 §5 之混淆源證實 —— `stored != baseline_A`

```
diff /tmp/RECON.stored /tmp/baseline_A  → 有輸出
```

現存 `RECON.md` 相對今日產出**缺少整整兩節**（`## Assertions`、
`## Spec outline map`，共 22 行）。即現存檔是較舊腳本版本之產物。

**分析層 §5 之判斷完全正確**：以現存 `RECON.md` 為基線，diff 必有輸出，
而該輸出與修法無關 —— 即「假失敗」。`03` T4 之原設計會在此處誤報。

### 3.4 回歸結果

```
diff /tmp/baseline_A features/privacy/RECON.md   → 無輸出   RECON 逐位元相同
DECISIONS.md SHA 修法前後                        → 相同     未被動
features/privacy/DECISIONS.new.md                → 2372 bytes 已產生
stdout                                           → "decisions written to: .../DECISIONS.new.md"
```

### 3.5 R-C9 未被破壞 —— 以單元測試驗證

`sxm` 因 §2.2(b) 之素材缺件無法跑完整 recon，故改以 `/tmp` 沙箱直接測
`write_decisions` 三分支，零副作用、不碰任何 feature：

```
1. 不存在 + 未簽核 : wrote=DECISIONS.md      diverted=False   OK
2. 存在   + 未簽核 : wrote=DECISIONS.new.md  diverted=True    OK   既有內容 'BODY-1' 保留
3. 存在   + 已簽核 : wrote=DECISIONS.new.md  diverted=True    OK   既有內容 'BODY-1' 保留
```

情境 3 證明 R-C9 之保護未被削弱；情境 2 為 A-TM15 修法之標的。

## 4. T5 — 階段二三項修法

### 4.1 A-TM04（`new_feature.py`）—— 已改，實測通過

守衛插於 `feat_dir = ...` 之前，**不自動 slugify**（依指令）。

**陽性實測**（含空格應被擋）：

```
$ python scripts/new_feature.py "Vehicle Setting" --root $TMPROOT
refusing: feature name contains whitespace: 'Vehicle Setting' (would create a directory with a space; see A-TM04)
exit code: 1
$TMPROOT/features → 空，未產生任何目錄
```

**tab 亦被擋**（`any(c.isspace())` 涵蓋全部空白字元，非只有空格）：

```
$ python scripts/new_feature.py "Tmp<TAB>Probe" --root $TMPROOT
refusing: feature name contains whitespace: 'Tmp\tProbe' ...
```

**陰性對照**（無空格應正常）：

```
$ python scripts/new_feature.py "TmpProbe" --root $TMPROOT
scaffolded .../features/tmpprobe          正常路徑未被守衛誤擋
```

*首次陰性對照曾拋 `FileNotFoundError: .../docs/fw036/templates/DECISIONS.md`。
已用修改前之腳本（`/tmp/new_feature.py.pre`）對另一臨時 root 重跑，
**得到同一錯誤** → 與本修法無關，係臨時 root 缺模板。補齊 templates 後
重測即通過。此比對過程記錄於此，因「陰性對照失敗」若不追根會被誤判為
修法破壞了正常路徑。*

### 4.2 A-TM05（`intake.py`）—— 已改，未實測

既存目錄時附加 `--adopt-existing` 而非跳過。

**未實測，不標 PASS** —— 依指令（需 drop folder 素材方能實跑）。

### 4.3 A-TM10（`intake.py`）—— 已改，未實測

`KIND_TO_YAML` 加 `"cfts_doc": "spec_pdf"`，並加**非覆寫守衛**：現值非
佔位符（不含 `<...>`）時不回填，並記入 conflicts。

守衛之必要性：`spec_pdf` 現由**兩個 kind** 可能寫入（`spec_pdf` 與
`cfts_doc`），後到者不得覆蓋先到者。

**一處偏離**：指令要求「於 `INTAKE.md` 註明衝突」，執行層改印 stdout
（`CONFLICT (A-TM10): ...`）。理由：`INTAKE.md` 由 `report()` 產出，
而衝突發生在 `scaffold()`，兩者無共用資料結構。**請示是否須改為寫入
INTAKE.md。**

**未實測，不標 PASS。**

### 4.4 語法與回歸

```
python3 -m py_compile scripts/{new_feature,intake,recon}.py   → 三支皆通過
修法後重跑 privacy 回歸：RECON 逐位元相同   DECISIONS 未被動
```

## 5. 測試副作用之處置（`03Z-A1` 未涵蓋，執行層主動盤點）

回歸測試在 `features/privacy/` 留下三項，逐項處理：

| 副作用 | 處置 |
|---|---|
| `RECON.md` 被覆寫 | **已還原**至 `/tmp/RECON.stored`，SHA 回到 `2f3dc3dc...`，`git status` 無殘留修改 |
| `DECISIONS.md` | 已於 §3.2 還原並驗證，`git status` 無殘留 |
| `DECISIONS.new.md`（2372 B，新增） | **保留待示** |
| `data/recon_leaf_to_section.tsv`（48 B，新增） | **保留待示** |

**兩個新增檔未刪除之理由**：刪除為不可逆動作，且發生在**非本 feature 之
目錄**。前者另為 A-TM15 修法正確運作之現場證據。**請示是否清除。**

`privacy` 除此二新增檔外，已完全回到本包動它之前的狀態。

## 6. T8 — 生成管線 CLI（只讀，未跑）

### 6.1 關鍵發現：生成管線不是全域的，是 per-feature 腳本

`scripts/` 下**無**任何生成器或 linter。實際形態為每個 feature 在
`features/<f>/scripts/` 自備：

| 角色 | 實例 | 本 feature |
|---|---|---|
| batch context | `make_batch_context.py`（sxm/amfm）、`build_batch_context.py`（user_profiles）| **無** |
| 生成執行器 | `gen_pilot.py`、`gen_batchNN.py`（comfort/power/user_profiles）；sxm/amfm **無** | **無** |
| linter | `lint_tcs.py` —— media/home/amfm/sxm/privacy/comfort/power/user_profiles **各一份** | **無** |
| 寫回 | `write_back.py` —— 各 feature 一份，皆 `from backend.xlsx_surgical import surgical_save` | **無** |

**`features/time_management/scripts/` 完全是空的。**

### 6.2 各項之實際定義

`lint_tcs.py`（sxm 例）：

```
ap.add_argument("--feature-dir", default=".")
ap.add_argument("--generated", default="generated")
ap.add_argument("--json-report")
```

`write_back.py`（sxm 例）：

```
ap.add_argument("--feature-dir", default=".")
ap.add_argument("--data", default="data")
ap.add_argument("--generated", default="generated")
ap.add_argument("--workbook") / ("--out") / ("--date")
ap.add_argument("--write", action="store_true")
```

`backend/xlsx_surgical.py` 之簽章（`scripts/` 外，`backend/`）：

```
def surgical_save(mutated, src: Path, out: Path, *, verify: bool = True) -> dict
    # Write `mutated`'s cell changes into a byte-for-byte copy of `src`.
```

`backend/main.py`（另一條路徑，API/模型呼叫）：

```
--input --sys1 --spec --framework --output-dir --model --batch-size
--mode {full,incremental,regenerate} --rows --dry-run --budget
```

`make_batch_context.py`（sxm）之 usage：

```
python features/sxm/scripts/make_batch_context.py --feature-dir features/sxm \
    --batches-md docs/batches-sxm.md --batch "B1 (pilot) — Instant Replay"
```

### 6.3 對 `04` 之實質影響 —— 兩項提請

**(1) 本 feature 須先建立自己的 `scripts/`。** `04` 不能只給「跑哪個
指令」，而須包含這些腳本的建立。這比原先預期的工作量大。

**(2) R-TM10-A1 之射程須釐清 —— 這會直接卡住 `04`。**
該條 SUSPENDED「不得援引任何他 feature 之既成樣式」。但：

- 若射程含**腳本結構**，則本 feature 無法參照 sxm/comfort 之
  `lint_tcs.py` / `write_back.py`，一切須從零寫 —— 而 `write_back.py`
  必須正確呼叫 `surgical_save`，從零寫反而升高母本 x14 下拉被摧毀之風險
- 若射程只含 **TC 內容之樣式**（步驟措辭、ER 句式、標點慣例 —— R-TM10(b)
  原文所列者），則腳本可自由參照

**執行層讀法：後者。** R-TM10(b) 明列之可援引／不得援引兩表，全部是
**TC 內容項目**（步驟措辭、ER 句式、spec_reference 格式、test_group 值、
priority 分佈、tc_id 體系、Input Test Data 填法），無一項涉及工具腳本。
且 R-TM10(c) 之語境為「爭議之裁決依據」，屬內容判準。

**但執行層不自行認定**，提請明示。**未明示前，`04` 之腳本建立無法開始。**

### 6.4 附帶觀察

`comfort/scripts/gen_pilot.py` 之首行說明：TC content is authored here
rather than emitted by a template, because every field is a judgement
traceable to a clause; what the script contributes is determinism。

即生成腳本**不是模板引擎**，而是把人工判斷固化為可重跑之決定性產物
（tc_id 由位置指派、clause 從 tsv 讀）。此與 R-TM24 之來源隔離作法一致 ——
本 feature 已備 `data/leaf_descriptions.txt` 作為 `test_item` 上半之唯一來源。

## 7. T9(7) — 該驗而未驗者（續用五全集）

### 7.1 依全集 1（指令逐項）

T1–T8 全數完成。T6 六項全符。**三處逕行**：§3.1（修法範圍延伸）、
§4.3（衝突改印 stdout）、§5（`privacy` RECON.md 還原）—— 皆已標示可撤回點。

### 7.2 依全集 2（寫入後複查）

| 檔案 | 複查 | 結果 |
|---|---|---|
| `RULINGS.md` | 條數 | 29 |
| `ANOMALIES.md` | 條數 + A-TM17 索引 | 18 / RESOLVED |
| `docs/fw036/framework.md` | T7 簽核註記 | 已加 |
| `scripts/recon.py` | py_compile + 單元測試三分支 | OK |
| `scripts/new_feature.py` | py_compile + 陽性/陰性實測 | OK |
| `scripts/intake.py` | py_compile | OK（未實跑）|

四處 `str.replace` 全部前置 `assert` + `count==1`。

### 7.3 仍未驗者

| # | 項 | 狀態 |
|---|---|---|
| 1 | **A-TM05 / A-TM10 之實跑** | 需 drop folder 素材，依指令不做，**標「已改，未實測」而非 PASS** |
| 2 | **R-TM10-A1 對腳本之射程** | §6.3(2)，**卡住 `04`**，待明示 |
| 3 | R-TM23 兩界線之訊號名／物件 id（`4813974`、`$DateTmFormat$`、`$GPSDateTm*$`）| `03Z` 上繳已提請，**仍未驗**。B1 生成前應補 |
| 4 | `privacy` 兩個新增檔之處置 | §5，待示 |
| 5 | A-TM12（階段三）| 明令不在本包 |
| 6 | PU 陽性對照 | 待 Pei 裁 |
| 7 | `write_back` 兩值 | Phase 3 |

### 7.4 依全集 4（陰性對照）

| 結論 | 陰性對照 | 有無 |
|---|---|---|
| A-TM04 守衛擋空格 | 無空格之 `TmpProbe` 正常 scaffold | 有 |
| 陰性對照之失敗與修法無關 | 修改前腳本同樣失敗、同一錯誤 | 有 |
| 四候選皆靜止 | 兩快照各 1217 行、diff 無輸出；對比 `vehicle_setting` 本 session 內仍在寫入 | 有 |
| R-C9 未被削弱 | 單元測試情境 3 既有內容保留 | 有 |

### 7.5 依全集 5（設計說明之可驗性）

`03Z-A1` §2.1 之「B1 阻塞項為零」逐項複核：**六項全部同意**，且執行層
補一項該表未列者 —— **§6.3(2) 之 R-TM10-A1 射程問題**，其確實阻塞 `04`
之腳本建立（非阻塞 TC 內容生成，但腳本是生成之前置）。故「阻塞項為零」
應修正為「**TC 內容之阻塞項為零，工具前置之阻塞項有一**」。

## 8. 本包未動之事項

未動 git。**未修 A-TM12**（階段三）。**未碰 `features/vehicle_setting/`**。
**未生成任何 TC**（T8 只讀 CLI）。未送出 RD-1。未填 `D5`、未組 Scope 值。
未援引任何他 feature 樣式。未以 openpyxl 存回任何工作簿。
**未刪除 `privacy` 之兩個新增檔。** 未建立 `features/time_management/scripts/`
之任何腳本（待 §6.3(2) 明示）。
