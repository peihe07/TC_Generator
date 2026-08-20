# 03Z-A1 — A-TM17 結案、R-TM23 簽核、升級門檻自律、腳本修法執行

分析層。**追發包，依 R-TM20 聲明**：所依賴之 `03Z_closure.md` 尚未上繳；
本包項目與 `03Z` T1–T7 互不相依。**執行順序：先跑 `03Z` T1–T7，再跑本包。**
上繳合併為 `docs/upstream/03Z_corrections.md`，兩包分節。

---

## 1. R-TM23 簽核

```
R-TM25（Pei, 2026-08-20「簽」）—— R-TM23 兩條新界線簽核

R-TM23 增列之界線 4（014 ↔ 008/017）與界線 5（011 ↔ 008）簽核通過。
Part VII §8.2.1 相鄰組界線表確定為五條，全部為 §8.2.1 之拘束條款，
B1 起逐條適用。

R-TM17 之簽核標的自此涵蓋五條，不需再就界線事項回頭覆簽。
```

## 2. 分析層之升級門檻 —— 我違反了自己訂的界線

Pei 指出「一直卡在這裡」。**檢視後成立，且錯在我。**

Project charter 之升級門檻明訂：**只升級**不可逆操作、跨 feature 影響、
影響 >10% 語料之裁決；**其餘一律以保守預設逕行、記錄、前進**。

R-TM23 之兩條界線：只窄化不擴張、單一 feature 內、影響 22 片中之 3 片
（008／011／014，13.6% 之 leaf 但 0% 之既有內容，因尚未生成任何 TC）、
完全可逆（B1 尚未生成，改界線無成本）。**全部落在「分析層得自裁」之內**，
我卻把它送上去覆簽，並以此擋住 B1。

```
R-TM26（分析層自裁，2026-08-20）—— 不得升級自裁範圍內之事項

分析層送 Pei 之前，須逐項對照 charter 之升級門檻：
  (a) 不可逆操作？ (b) 跨 feature 影響？ (c) 影響 >10% 既有語料？
三項皆否者，**逕行裁定、記錄、前進，不得送簽**。

「已有先前簽核標的、增列是否須另簽」不是升級理由 —— 只窄化不擴張、
且標的尚未生成任何內容者，屬條文精修，非新簽核事項。

送簽本身有成本：它使下游停擺，而停擺之代價由 Pei 承擔。
不確定時之正解是「逕行並在下放包標明可撤回」，不是「停下來問」。

依據：R-TM23 三項門檻皆否而送簽，B1 因此停一輪。
```

### 2.1 B1 之實際阻塞項 —— 重新盤點後為零

逐項檢視，非印象：

| 曾標為阻塞 | 是否真的擋住 B1 |
|---|---|
| R-TM23 覆簽 | **已簽（§1）** |
| R-TM10-A1 SUSPENDED | **否** —— 無樣式參照代表僅依條文生成，是限制不是阻塞 |
| A-TM02a（037 身分）| **否** —— 只擋 D5 一格，不擋任何 TC 列 |
| A-TM13（2 筆缺章節）| **否** —— B1 之七片刻意不含 002／005 |
| R-TM19 腳本修法 | **否** —— 受影響者為 `recon.py` / `intake.py` / `new_feature.py`，生成管線不在其中 |
| A-TM17 | **已 RESOLVED（§3）** |

**B1 之阻塞項為零。** 唯一缺的是分析層尚未讀生成管線之 CLI，
故本包 T8 指派回報其進入點與 argparse，`04` 即為 B1 生成包。

## 3. A-TM17 結案

```
A-TM17 —— RESOLVED（Pei, 2026-08-20「A-TM17是」）

Pei 確認：併行寫入者為 Pei 自己開啟之另一 session；
`features/vehicle setting/` 之刪除為其所為。三項登記事實均已解釋，
**repo 無未受控之刪除行為**。

保留之限制（理由改變，限制不變）：`features/vehicle_setting/` 仍不列為
回歸受測物，且不對其寫入或實跑腳本 —— 理由不再是身分不明，而是
併行編輯使量測失去鑑別力（受測目錄同時被他方寫入時，diff 有輸出
無法區分成因，R-TM21 同一判準）。屬技術限制。
```

`A-TM01` 之 MOOT 不因本條改變 —— 標的確已滅失、R-TM18 確實未能執行，
事實記載不隨成因解釋而變（R-TM13）。

## 4. R-TM22 條件 1 達成

```
R-TM22 條件 1 解除（2026-08-20）：A-TM17 已釐清（§3）。
條件 2（受測物經量測選定）仍須履行，判準不變：
  a. inputs/ 存在且非空  b. RECON.md 與 DECISIONS.md 皆存在
  c. 靜止性：相隔 ≥10 分鐘兩次 mtime 快照無變動
階段順序（A-TM15 最先）不變；階段三（A-TM12）不在本包。
```

## 5. 回歸設計訂正 —— `03` T4 之基線是錯的

`03` T4 寫「修改前基線 = 現存之 `RECON.md`」。**該設計有缺陷**：現存
`RECON.md` 是過去某次執行之產物，腳本版本與素材狀態未必等同今日；
以它為基線，diff 有輸出時無法區分「本次修法造成」或「本來就會不同」。
與假通過為鏡像 —— 這是**假失敗**。

正確設計：先以**未修改之腳本**跑一次取真基線。步驟見 T4。
其步驟 2 為**刻意執行一次它要防止的損害**（沖掉 `DECISIONS.md`），
因那是取得真基線之唯一方式，有備份與 SHA 驗證。
**此點須在上繳如實記載，不得寫成「無損害」。**

---

## 6. 指令（於 `03Z` T1–T7 完成後執行）

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM25、R-TM26

標題行 `## R-TM25 — R-TM23 兩條新界線簽核`、
`## R-TM26 — 不得升級自裁範圍內之事項`，內文為 §1 / §2 之區塊全文。
於 R-TM22 條末尾追加 §4 之區塊。
追加後 `## R-TM` 條數應為 **29**（27 + 2）。

### T2 — `ANOMALIES.md`：A-TM17 轉 RESOLVED

條文末尾追加 §3 之區塊全文；索引該列狀態 `PENDING` → `RESOLVED`。
**條數不變（18）。**

### T3 — 受測物選定（R-TM22 條件 2）

候選 `sxm` / `privacy` / `comfort`，加 `03Z` T5 掃出之合格者。
**`vehicle_setting` 不列。**

`stat` 旗標形式因平台而異（macOS `-f '%m %N'` / GNU `-c '%Y %n'`）——
依 R-TM7 分析層未在該機實測，**由執行層先確認可用形式並回報**。

```bash
snap () { for f in sxm privacy comfort; do
            echo "=== $f"; find "features/$f" -type f -exec stat <旗標> {} \; | sort
          done; }
snap > /tmp/snap1.txt
# ——— 等待 ≥10 分鐘 ———
snap > /tmp/snap2.txt
diff /tmp/snap1.txt /tmp/snap2.txt && echo "三者皆靜止"
```

選一靜止者，回報選定依據。三者皆非靜止則回報並停。

### T4 — 階段一：A-TM15

```bash
F=features/<選定之 feature>

cp scripts/recon.py /tmp/recon.py.pre-A-TM15
cp "$F/DECISIONS.md" /tmp/DECISIONS.backup
cp "$F/RECON.md"     /tmp/RECON.stored
shasum -a 256 "$F/DECISIONS.md" > /tmp/dec.sha.pre

# 步驟 2：未修改之腳本取真基線（會沖掉 DECISIONS.md，已備份）
python scripts/recon.py --feature "$F"
cp "$F/RECON.md" /tmp/baseline_A

# 步驟 3：還原並驗證
cp /tmp/DECISIONS.backup "$F/DECISIONS.md"
shasum -a 256 "$F/DECISIONS.md" > /tmp/dec.sha.restored
diff /tmp/dec.sha.pre /tmp/dec.sha.restored && echo "DECISIONS 還原正確"

diff /tmp/RECON.stored /tmp/baseline_A && echo "stored == baseline_A" \
  || echo "stored != baseline_A —— §5 之混淆源證實"
```

施行修法：`scripts/recon.py` 之 `write_decisions()` ——
**目標檔已存在時一律寫 `DECISIONS.new.md`**，僅目標檔不存在時才寫
`DECISIONS.md`；stdout 明示所寫路徑。

```bash
python scripts/recon.py --feature "$F"
diff /tmp/baseline_A "$F/RECON.md" && echo "RECON 逐位元相同 ✅"
shasum -a 256 "$F/DECISIONS.md" > /tmp/dec.sha.post
diff /tmp/dec.sha.pre /tmp/dec.sha.post && echo "DECISIONS 未被動 ✅"
ls -la "$F/DECISIONS.new.md"
```

**任一 diff 有輸出即回報並停，還原 `/tmp/recon.py.pre-A-TM15`。**

### T5 — 階段二：A-TM04 / A-TM05 / A-TM10

**A-TM04** — `scripts/new_feature.py` `scaffold()`，於
`feat_dir = root / "features" / feature.lower()` 之前插入：

```python
if any(c.isspace() for c in feature):
    sys.exit(f"refusing: feature name contains whitespace: {feature!r} "
             f"(would create a directory with a space; see A-TM04)")
```

**不自動 slugify**（自動改名會靜默改變既有 feature 之目錄推導）。

**A-TM05** — `scripts/intake.py` `scaffold()`：既存目錄時以
`--adopt-existing` 呼叫 `new_feature.py`，而非跳過。

**A-TM10** — `scripts/intake.py` 之 `KIND_TO_YAML` 加
`"cfts_doc": "spec_pdf",`，**僅在 `spec_pdf` 現值仍為佔位符時回填**；
已有真實路徑則不覆寫，並於 `INTAKE.md` 註明衝突。

驗證：

1. 重跑 T4 之最終兩個 diff
2. **A-TM04 守衛須實測其確實會觸發**：先讀 `new_feature.py` 之 argparse
   確認參數形式（R-TM7），再以含空格之 feature 名對 `/tmp` 下臨時 root
   執行，確認 `sys.exit` 生效。**回報完整指令與輸出。**
3. A-TM05 / A-TM10 需 drop folder 素材方能實跑，**本包不做**，
   標「已改，未實測」，**不得標 PASS**

### T6 — 驗證

```bash
grep -c '^## R-TM' features/time_management/RULINGS.md      # 期望 29
grep -c '^## A-TM' features/time_management/ANOMALIES.md    # 期望 18
grep -n '^| A-TM17' features/time_management/ANOMALIES.md   # 應為 RESOLVED
grep -n 'DECISIONS.new.md' scripts/recon.py                 # 應命中
grep -n 'contains whitespace' scripts/new_feature.py        # 應命中
grep -n 'cfts_doc' scripts/intake.py                        # 應命中
```

### T7 — Part VII 界線表註記簽核

`docs/fw036/framework.md` Part VII 之相鄰組界線節，於標題行後加一句：

```markdown
（五條界線經 Pei 2026-08-20 簽核，R-TM17 + R-TM25）
```

### T8 — B1 生成管線之 CLI 回報（**`04` 之前置，不執行生成**）

回報下列各項之**進入點與 argparse 實際定義**（讀，不跑）：

1. prompt builder / batch context 產生器 —— 檔案路徑、必填參數
2. 生成執行器 —— 檔案路徑、必填參數、輸出落點
3. `lint_tcs.py` —— 路徑與參數
4. `backend/xlsx_surgical.py` —— `surgical_save` 之簽章

依 R-TM7，分析層不得憑印象寫 `04` 之指令，故先取實際定義。
**本步驟只讀不跑，不生成任何 TC。**

### T9 — 上繳

併入 `docs/upstream/03Z_corrections.md`，分「03Z」「03Z-A1」兩節。本節須含：

1. T6 六項實際輸出
2. T3 之選定依據、所用 `stat` 形式、快照 diff 結果
3. T4 全部 diff 實際輸出，含 `stored` vs `baseline_A` 比對
4. T4 步驟 2 之損害如實記載（沖掉一次、已備份、已驗證還原）
5. T5 之 A-TM04 守衛實測指令與輸出；A-TM05 / A-TM10 標「已改，未實測」
6. T8 之四項 CLI 定義
7. **本包是否仍有該驗而未驗者之獨立判斷**，明列全集

### 不得執行者

- 不動 git
- 不修 A-TM12（階段三，另包）
- 不碰 `features/vehicle_setting/`
- **不生成任何 TC**（T8 只讀 CLI；生成為 `04`）
- 不送出 RD-1（Tier 3）
- 不填 `D5`、不組 Scope 值
- 不援引任何他 feature 樣式（R-TM10-A1 仍 SUSPENDED）
- 不以 openpyxl 存回任何工作簿

---

## 7. 本包產生之新條文清單（自檢，逐列對應指令段 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM25 | 裁決（Pei），R-TM23 兩界線簽核 | §1 | ✅ T1 + T7 |
| R-TM26 | 分析層自裁，不得升級自裁範圍內事項 | §2 | ✅ T1 |
| A-TM17 → RESOLVED | anomaly 結案 | §3 | ✅ T2 |
| R-TM22 條件 1 解除 | 加註，條文不變 | §4 | ✅ T1 |
| 回歸設計訂正 | 方法修正，取代 `03` T4 | §5 | ✅ T4 |

分析層本包未動 git、未改腳本、未觸 `vehicle_setting/`。
