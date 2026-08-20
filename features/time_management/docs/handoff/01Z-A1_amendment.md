# 01Z-A1 — R-TM9 / R-TM10 之修正（實測發現其前提不成立）

分析層，2026-08-20，同日晚於 `01Z_naming_rulings.md`。
本件為 **amendment**，非取代：R-TM8 不動；R-TM9 步驟 1 與 R-TM10(a) 之
指定來源經實測**不存在於磁碟**，故該兩條之執行前提須改寫。

原包末段已聲明「本次因 MCP 逾時未能實測其存在，僅依 FORMS.md 記載引用」。
MCP 恢復後分析層立即補測，結果如下 —— **記載與磁碟不符**。

---

## 1. 實測結果

| 路徑 | 實測 |
|---|---|
| `features/home/output/` | **ENOENT — 目錄不存在** |
| `features/home/` 內容 | `.gitignore` / `ANOMALIES.md` / `DECISIONS.md` / `PLAYBOOK.md` / `RECON.md` / `RUNBOOK.md` / `data` / `docs` / `feature.yaml` / `generated` / `scripts`。**無 `output/`，亦無 `inputs/`** |
| `archive/forms_superseded/` | 存在，含 `.gitkeep`、`BASELINE.sha256`、三份 036 xlsx，**含 R-TM10 明文禁止之 `…_SWQT_Home_20260809.xlsx`** |

即：**R-TM10 唯一准許之來源不在磁碟上，唯一禁止之來源在磁碟上。**

成因推定（未證實，屬待查）：`features/home/.gitignore` 依 scaffold 慣例
排除 `inputs/` 與 `output/`，xlsx 從不入 git。故 Home v2 交付件
（`…_Home_20260720.xlsx`，FORMS.md 載 SHA `cfc007f3…`、tag
`fw036-home-regen-v2`）可能只存在於當初產出它的機器或已被清理。
tag 綁定的是 commit 與 SHA256 記載，不是檔案本身。

**這與 A-UP03／A-UP05 為同一形態**：FORMS.md 之記載其量測對象在 repo 內
已不存在。該形態在本 repo 至此為第二例。

## 2. R-TM9 修正

```
R-TM9-A1（分析層，2026-08-20）—— Scope 值之前綴段改為待決

R-TM9 之「D5 之 feature 識別段 = Time-and-Date-HMI-V0.1」不變。

其步驟 1 之來源 features/home/output/…_Home_20260720.xlsx 經實測不存在，
該步驟不可執行，撤銷。改為：

1. 執行層開啟 archive/forms_superseded/…_SWQT_Home_20260809.xlsx，
   讀出其 D5 全字串。該值為 A-H26 之未修正值
   （FORMS.md 載為 "…AppDrawer-Projection-SWE1HMI-V0.1"），
   **不得採為本 feature 之值**，僅用以取得前綴段之字面。
2. 回報該全字串，並標出前綴段與 feature 識別段之切分點。
3. 切分正確與否須經分析層覆核後，方得組成本 feature 之 D5 值。
   —— 因來源本身即缺陷件，其前綴段是否亦受該缺陷影響，
   在切分被覆核前不能假定。

在覆核完成前，D5 **維持空白**。空白是可見狀態，錯值不是。
A-TM11 維持 PENDING，不因本件轉 RESOLVED。
```

## 3. R-TM10 修正

```
R-TM10-A1（分析層，2026-08-20）—— 樣式參照暫停生效

R-TM10 之三重限縮不變，但其 (a) 所指定之唯一來源經實測不存在，
故 R-TM10 全條 **暫停生效（SUSPENDED）**，非撤銷。

暫停期間：pilot review 與 TC 生成一律僅依條文（§4–§12）與本 feature
之 profile，不得援引任何他 feature 之既成樣式。

解除條件（二者擇一，均須 Pei 裁）：
(a) Home v2 交付件被取回磁碟，實測 SHA256 = FORMS.md 所載 cfc007f3…，
    R-TM10 原文即生效；或
(b) Pei 另裁一個替代之樣式來源。
    此時 R-TM10(b)(c) 之限縮原文照套於新來源，(a) 改寫其路徑與雜湊。

**明文重申**：archive/forms_superseded/…_SWQT_Home_20260809.xlsx
不得作為 (b) 之替代來源。它在磁碟上而 v2 不在，正是最容易被順手取用
之路徑；FORMS.md 之 provenance warning 已列其四項污染
（D5 未修正、F 欄全填、G 欄全填 CoreHMI、K 欄全填 NA、author 為 ArifChen），
其中 K 欄與 G 欄之污染會直接汙染 TC 內容而非僅樣式。
```

## 4. 新登記 anomaly

```
A-TM14（PENDING，Tier 2）—— FORMS.md 引用之 Home v2 交付件不在磁碟上

FORMS.md 之 instance register 與 provenance warning 均以
features/home/output/…_Home_20260720.xlsx（SHA cfc007f3…、
tag fw036-home-regen-v2）為 Home 之權威交付件，並以之為判定
archive 內 Home 複本受污染之比對基準。

實測（2026-08-20）：features/home/output/ 目錄不存在。

後果有二，須分開處置：
1. 對本 feature —— R-TM10 之樣式參照無來源可用（見 R-TM10-A1）
2. 對 repo —— FORMS.md 之 provenance warning 其比對基準已不可覆驗。
   該 warning 所述之四項差異目前無法被任何人重新驗證，
   只能作為歷史記載引用，不得作為現行判準。
   此與 A-UP03／A-UP05 同形態，為第二例。

不建議之處置：以 archive 內之 Home 複本替代基準 —— 那正是被判定為
受污染的那一份，以受測物充當基準即失去比對意義。

建議之處置（待 Pei 裁）：確認該交付件是否仍存於他處
（交付路徑 /Users/peihe/Work/02_Project_R1LR/10_Reviewing/…）；
若確已不存，則 FORMS.md 相關段落須標註其基準不可覆驗，
比照 A-UP05 之處理方式。
```

## 5. 對執行層待辦之影響

`01Z_naming_rulings.md` §「執行層本包待辦」第 3、4 項作廢，改為：

3'. 依 R-TM9-A1，讀 archive 內 Home 複本之 D5 全字串，回報並標切分點。
    **不得組值、不得填入 D5。**
4'. 登記 A-TM14。索引表由 13 條改為 **14 條**
    （A-TM13 + A-TM14；A-TM11 維持 PENDING）。

第 1、2、5、6 項不變。R-TM8 不受本件影響，照原文執行。

## 6. 本包產生之新條文清單（自檢）

| 編號 | 形態 | 已以可貼區塊呈現 |
|---|---|---|
| R-TM9-A1 | amendment，前綴段改待決，D5 維持空白 | ✅ §2 |
| R-TM10-A1 | amendment，全條 SUSPENDED，載解除條件 | ✅ §3 |
| A-TM14 | anomaly，PENDING，Tier 2 | ✅ §4 |

本件之全部斷言均為 2026-08-20 對 repo 實際路徑之實測，非 FORMS.md 轉述。
分析層未動 git、未改腳本、未改任何既有檔案、未觸碰 archive/。
