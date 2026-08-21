# 下放包 04 — 五項追認與裁定、R-TM23 錨點複驗、per-feature 腳本建立

分析層 → 執行層。往返編號 `04`。對應上繳 `docs/upstream/04_scripts.md`。
`03Z` / `03Z-A1` 兩節上繳**全部受理**，`03` 往返結案。

**三處逕行全部追認，且其中兩處指出了我的指令缺陷。**

---

## 1. §3.1 A-TM15 修法範圍延伸 —— 追認，且我的指令是錯的

執行層照字面改會使**任何既有 feature 重跑 recon 都 REFUSED 非零退出，
並對未簽核之檔案謊稱其已簽核**。我寫 T4 時只看了 `write_decisions()`，
沒看它的回傳值在 `recon.py:1135` 被 `if outcome["diverted"]: sys.exit(...)`
消費。**「寫到哪裡」與「要不要拒絕」是兩件事，我把它們綁在一起了。**

三分支切法正確：

| 情境 | 行為 |
|---|---|
| 目標存在 + 已簽核 | divert + REFUSED 非零退出（R-C9 原樣保留）|
| 目標存在 + 未簽核 | divert + `NOTE (A-TM15)` + 正常退出（A-TM15 之標的）|
| 目標不存在 | 寫 `DECISIONS.md`（新 feature 路徑不變）|

且以 `/tmp` 沙箱單元測試三分支、情境 3 證明 R-C9 未被削弱 —— **這比跑一次
整包 recon 更能證明「只改了該改的那一支」**。

依 R-TM26 逕行且標明還原點，判斷正確。

```
R-TM27（分析層裁定，2026-08-20）—— A-TM15 修法範圍追認為三分支

A-TM15 之修法確定為三分支（見上表），非 03Z-A1 T4 字面之
「目標存在即改寫路徑」。原字面指令會使既有 feature 之 recon 一律
REFUSED 退出並誤報簽核狀態 —— 該缺陷源自分析層只讀 write_decisions()
未讀其回傳值之消費點（recon.py:1135）。

一般化：修改一個函式之回傳語意前，須讀遍其全部消費點。
與 R-TM7（指令須經實測）同族：前者是介面未讀，本條是消費點未讀。
```

## 2. §2.2 `sxm` 不適格 —— 追認，且 R-TM22 2(a) 須收緊

兩個理由都成立，第一個尤其：

**(a) `sxm` 已簽核 → 走 divert 路徑受 R-C9 保護，修法前後行為相同，
判準無鑑別力。** 這正是 R-TM21 之判準（「本工作若完全沒做，判準會不會
照樣通過」）套在受測物選擇上。我列候選時只看檔案存在性，沒看
`signoff.signed` —— **而 A-TM15 修的就是「未簽核」那一支**。

**(b) `inputs/` 有 4 檔但 `feature.yaml` 宣告之 SYS1 檔不在其中。**
「存在且非空」不足以判定資格。

```
R-TM28（分析層裁定，2026-08-20）—— R-TM22 條件 2 收緊

R-TM22 之受測物判準 2(a) 由「inputs/ 存在且非空」改為：

  2(a) feature.yaml 宣告之每一個輸入路徑皆實際存在於磁碟
       （非僅 inputs/ 非空 —— sxm 之 inputs/ 有 4 檔而宣告之 SYS1
        檔不在其中，實跑即 input not found）

新增 2(d)：受測物之 signoff.signed 必須為 False。
       已簽核者走 divert 路徑受 R-C9 保護，A-TM15 修法前後行為相同，
       以其為受測物則判準無鑑別力（R-TM21 同型）。

依本條，四候選之適格性為：
  privacy        signed=False  宣告路徑齊全  → 適格（本次選用）
  user_profiles  signed=False  未驗宣告路徑  → 待驗
  sxm            signed=True   宣告路徑缺件  → 不適格
  comfort        signed=True   且為 A-TM18 主體 → 不適格
```

## 3. §6.3(2) R-TM10-A1 之射程 —— **裁定：不及於工具腳本**

執行層之讀法正確，本包確認。**這是 `04` 之唯一阻塞項，現解除。**

```
R-TM29（分析層裁定，2026-08-20）—— R-TM10-A1 之射程限於 TC 內容

R-TM10-A1 之 SUSPENDED「不得援引任何他 feature 之既成樣式」，
其射程**限於 TC 內容**，不及於工具腳本、資料結構與管線形式。

依據（條文自身，非新解釋）：R-TM10(b) 明列之可援引／不得援引兩表，
全部為 TC 內容項目 —— 步驟措辭、ER 句式、標點慣例、spec_reference 格式、
test_group / test_set 值、priority 分佈、tc_id 體系、Input Test Data
填法。**無一項涉及工具腳本。** R-TM10(c) 之語境為「爭議之裁決依據」，
亦屬內容判準。

故：`features/time_management/scripts/` 之各腳本得自由參照他 feature
之對應腳本（結構、參數、呼叫慣例、錯誤處理）。

**且此處參照是必要的而非便利的**：`write_back.py` 須正確呼叫
`backend/xlsx_surgical.py` 之 `surgical_save`，從零寫反而升高母本 R 欄
x14 下拉被摧毀之風險（R-G3）—— 該風險為不可逆且發生在交付件上。
以「不得援引樣式」為由強迫從零寫工具，會用一個內容層的限制去製造
一個交付層的風險，非該條之目的。

**界線**：腳本內若含 TC 內容之常數（步驟措辭常數、ER 樣板字串、
Test Set 值），該常數仍受 R-TM10-A1 拘束，須依本 feature 之條文重新
決定，不得照抄。**參照結構，不繼承內容。**
```

## 4. §7.5 之修正 —— 採納

「B1 阻塞項為零」應修正為
**「TC 內容之阻塞項為零，工具前置之阻塞項有一」**。
該一項即 §3，本包已解除。修正逐字採納，記入 `04` 之上繳。

## 5. R-TM23 錨點 —— **分析層已複驗，四項全中**

執行層兩度提請（`03Z` §5.6、`03Z-A1` §7.3 項 3）：兩條界線之訊號名與
物件 id 為 §8.2.1 拘束條款之具體錨點，未經複驗。**提請成立**，
分析層即刻對 CFTS015 內文複驗：

| 錨點 | 複驗結果 |
|---|---|
| 物件 `4813974` | **命中**。內容為「CAN 由 sleep 轉 wake 時，HU 應召回最後已知格式並以下列訊號送出：`$DateTmFormat$ = [format type]`」 |
| `4813974` 之章節 | **1.3.1.1.5.1 Time Display Formats**（父節 1.3.1.1.5 Time Display）—— 與 R-TM23 界線 5 所述相符 |
| `$GPSDateTm*$` 訊號組 | **命中**。物件 `4813937`（1.3.1.1.3 GPS TIME）列 `$GPSDateTmHour$` / `$GPSDateTmMinute$` / `$GPSDateTmSecond$`；物件 `4813999`（1.3.1.1.6.1）列 `$GPSDateTmYear$` / `$GPSDateTmMonth$` / `$GPSDateTmDay$`；物件 `4814098`（1.5.2.5 GPS Time and Date）六訊號齊列 |
| 1.3.1.1.4 為傳輸時機所有 | **命中**。物件 `4813953`（CAN wakeup 時送 `$DateTmHour$`/`$DateTmMinute$`/`$DateTmSecond$`）、`4813960`（每 1000 msec 週期訊息送最近計算之時間）—— 與界線 4 所述「008 擁有送出時機與觸發」相符 |

**四項全中，R-TM23 兩條界線之錨點成立，B1 之 008/011/014 可依其撰寫。**

複驗跑在 Project 附件之轉換文字副本（唯讀解析）。**執行層須對
`inputs/` 之原始 docx 做一次確認**（§8 T3），與 A-TM03／錨鏈同一紀律。

## 6. §5 `privacy` 兩個新增檔 —— 以 mv 移出，不 rm

執行層未刪除且提請，正確（刪除不可逆、且發生在他 feature 目錄）。

但**留在鄰居目錄亦不妥**：`DECISIONS.new.md` 與
`data/recon_leaf_to_section.tsv` 對 Privacy owner 而言來歷不明。

```
R-TM30（分析層裁定，2026-08-20）—— 回歸測試遺留物移入本 feature，不刪除

features/privacy/ 之兩個新增檔為本 feature 回歸測試之產物：
  DECISIONS.new.md（2372 B）—— A-TM15 修法正確運作之現場證據
  data/recon_leaf_to_section.tsv（48 B）

處置：**mv 至 features/time_management/data/regression_evidence/**，
不 rm。理由：
1. 刪除不可逆；mv 可逆
2. 證據價值屬本 feature（A-TM15 之驗證），不屬 Privacy
3. 鄰居目錄不留來歷不明之檔案

移動後 features/privacy/ 應與本次動它之前完全一致（RECON.md 與
DECISIONS.md 已於 03Z-A1 §5 還原並經 SHA 驗證）。
```

## 7. 新登記

```
A-TM19（PENDING，Tier 2 —— 併 A-TM12 批次修）

intake.py 之 A-TM10 衝突訊息只印 stdout（`CONFLICT (A-TM10): ...`），
未進 INTAKE.md。成因為結構性：INTAKE.md 由 report() 產出，而衝突發生於
scaffold()，兩者無共用資料結構。

執行層之偏離處置正確（不硬塞）。但 stdout 訊息在自動化流程中會遺失，
而 INTAKE.md 是該資訊之正確歸屬地。

建議修法（隨 A-TM12 之腳本批次一併做，不單獨開包）：scaffold() 將
conflicts 寫入 intake.json，report() 讀取後渲染入 INTAKE.md。
```

---

## 8. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM27 / R-TM28 / R-TM29 / R-TM30

標題行：

```
## R-TM27 — A-TM15 修法範圍追認為三分支
## R-TM28 — R-TM22 條件 2 收緊（宣告路徑齊全 + signed=False）
## R-TM29 — R-TM10-A1 之射程限於 TC 內容，不及於工具腳本
## R-TM30 — 回歸測試遺留物移入本 feature，不刪除
```

內文為 §1 / §2 / §3 / §6 之區塊全文。
追加後 `## R-TM` 條數應為 **33**（29 + 4）。

### T2 — `ANOMALIES.md`：新增 A-TM19

內容為 §7 之區塊全文。索引追加：

```markdown
| A-TM19 | intake.py 之 A-TM10 衝突訊息未進 INTAKE.md | PENDING | Tier 2（併 A-TM12）|
```

索引條數 18 → **19**。

### T3 — R-TM23 錨點對原始 docx 複驗

```bash
python3 - <<'PY'
import zipfile, re, html, pathlib
docx = next(pathlib.Path("features/time_management/inputs").glob("*.docx"))
xml = zipfile.ZipFile(docx).read("word/document.xml").decode("utf-8")
paras = []
for p in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
    t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, flags=re.S))
    paras.append(html.unescape(re.sub(r"<[^>]+>", "", t)).strip())
blob = "\n".join(paras)
for tok in ["4813974", "$DateTmFormat$", "GPSDateTmHour", "GPSDateTmYear",
            "4813937", "4813999", "4814098", "4813953", "4813960"]:
    print(f"{tok:20} count={blob.count(tok)}")
HEAD = re.compile(r"^(\d+(?:\.\d+)*)\s+.*\{(\d+)\}$")
OBJ  = re.compile(r"^(\d{6,8})\s*:")
cur = None
for t in paras:
    if "\t" in t: continue
    m = HEAD.match(t)
    if m: cur = m.group(1); continue
    m2 = OBJ.match(t)
    if m2 and m2.group(1) in {"4813974","4813937","4813999","4814098","4813953","4813960"}:
        print(f"object {m2.group(1)} -> section {cur}")
PY
```

期望：九個 token 之 count 皆 ≥1；`4813974 → 1.3.1.1.5.1`、
`4813937 → 1.3.1.1.3`、`4813953`/`4813960 → 1.3.1.1.4`、`4814098 → 1.5.2.5`。
**任一不符即回報並停** —— 錨點錯則 R-TM23 之界線須改，屬 Tier 2。

### T4 — `privacy` 遺留物移出（R-TM30）

```bash
mkdir -p features/time_management/data/regression_evidence
mv features/privacy/DECISIONS.new.md \
   features/time_management/data/regression_evidence/privacy_DECISIONS.new.md
mv features/privacy/data/recon_leaf_to_section.tsv \
   features/time_management/data/regression_evidence/privacy_recon_leaf_to_section.tsv

ls -la features/time_management/data/regression_evidence/
git status --short features/privacy    # 看，不 commit；應無殘留
```

於 `regression_evidence/README.md` 記：來源 feature、產生原因（A-TM15
回歸測試）、對應條文 R-TM30、產生時點。

### T5 — 建立 `features/time_management/scripts/`（R-TM29 已解除阻塞）

**參照結構，不繼承內容**（R-TM29 界線）。

參照來源：`features/privacy/scripts/`（與本 feature 同為 BLANK workbook、
rev C 母本、spec_mode D，形態最近）。**若其缺某腳本，再參照
`features/user_profiles/scripts/` 或 `features/sxm/scripts/`。**

需建立者，逐支回報其來源與差異：

| 腳本 | 用途 | 本 feature 之調整點 |
|---|---|---|
| `lint_tcs.py` | 機械漂移檢查 | design_method 詞彙取自母本 `下拉選單` 分頁；欄位對映用 rev C（design_method `R`、author `AA`）|
| `write_back.py` | 寫回，**必經 `surgical_save`** | workbook 指向 `inputs/` 之母本複本；`fill_test_group_set=true`；Test Group `Time and Date` |
| batch context 產生器 | 產 B1 之上下文 | 讀 `data/leaf_descriptions.txt` 與 `data/leaf_to_section_probe.txt` |

**本步驟只建立腳本，不執行、不生成任何 TC。**
每支腳本建立後跑 `python3 -m py_compile` 確認語法。

**明列禁止繼承者**（R-TM29 界線）：他 feature 腳本內之步驟措辭常數
（`ENTER_DEALER_MODE` 一類）、ER 樣板字串、Test Set 值、priority 預設 ——
一律留空或標 `TODO(R-TM10-A1)`，待本 feature 依條文決定。

### T6 — 驗證

```bash
grep -c '^## R-TM' features/time_management/RULINGS.md      # 期望 33
grep -c '^## A-TM' features/time_management/ANOMALIES.md    # 期望 19
ls features/privacy/DECISIONS.new.md 2>/dev/null || echo "privacy 已清 ✅"
ls features/time_management/data/regression_evidence/       # 應有 2 檔 + README
ls features/time_management/scripts/                        # 應非空
grep -rn 'TODO(R-TM10-A1)' features/time_management/scripts/ | wc -l   # 應 >=1
```

### T7 — 上繳

`docs/upstream/04_scripts.md`。須含：

1. T6 六項實際輸出
2. T3 之九個 count 與五項章節歸屬，與 §5 之表逐項對差
3. T4 之 `git status --short features/privacy` 輸出
4. T5 逐支腳本之來源、差異、`py_compile` 結果、`TODO(R-TM10-A1)` 位置清單
5. **本包是否仍有該驗而未驗者之獨立判斷**，明列全集

### 不得執行者

- 不動 git
- **不生成任何 TC**（`05` 為 B1 生成包）
- 不執行 T5 所建之任何腳本
- 不修 A-TM12 / A-TM19（併後續腳本批次）
- 不碰 `features/vehicle_setting/`
- 不 rm 任何檔案（T4 只 mv）
- 不繼承他 feature 之 TC 內容常數（R-TM29 界線）
- 不送出 RD-1（Tier 3）
- 不填 `D5`、不組 Scope 值
- 不以 openpyxl 存回任何工作簿

---

## 9. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM27 | 分析層裁定，A-TM15 三分支追認 | §1 | ✅ T1 |
| R-TM28 | 分析層裁定，R-TM22 條件收緊 | §2 | ✅ T1 |
| R-TM29 | 分析層裁定，R-TM10-A1 射程 | §3 | ✅ T1 + T5 |
| R-TM30 | 分析層裁定，遺留物 mv 不 rm | §6 | ✅ T1 + T4 |
| A-TM19 | anomaly，PENDING，Tier 2 | §7 | ✅ T2 |
| R-TM23 錨點複驗 | 分析層已驗，執行層確認 | §5 | ✅ T3 |

分析層本包未動 git、未改腳本、未觸 `vehicle_setting/`、未寫 `docs/fw036/`。
