# 10 下放包 — P1／P2／P10 之執行程序，與 R-VS16 之技術更正

分析層寫入，2026-08-20。全部為 Pei 之 Tier 3 動作；本檔只備程序與查證點。

---

## 0. R-VS16 依原文寫下去**不會生效** —— 更正

R-VS16 之條文為「於 `inputs/` 之後增列 `!inputs/INPUTS.sha256`」。
**該寫法無效。**

`.gitignore` 之語意：**父目錄被排除者，其下之檔案無法以否定式重新納入**
（git 不會下降到被排除之目錄，故否定式不被求值）。
現行 `features/vehicle_setting/.gitignore` 第 2 行為 `inputs/`，
即排除**目錄本身**，其後任何 `!inputs/…` 皆不生效。

```
R-VS16′（技術更正，取代 R-VS16 之實作段；意旨不變）
features/vehicle_setting/.gitignore 之

    inputs/

改為兩行：

    inputs/*
    !inputs/INPUTS.sha256

意旨與 R-VS16 完全相同（素材不入庫、雜湊入庫，canon G-9），
差別僅在 `inputs/` 排除目錄本身而 `inputs/*` 排除其內容 ——
後者才使否定式可被求值。

驗證方式（執行後必跑）：
    git check-ignore -v features/vehicle_setting/inputs/INPUTS.sha256
  期望：**無輸出、離開碼 1**（即未被忽略）
    git check-ignore -v features/vehicle_setting/inputs/leaves.tsv 之類素材
  期望：**有輸出**（仍被忽略）

**兩向都要驗** —— 只驗雜湊檔進得來，不驗素材仍擋得住，
等於沒驗（R-G7-1 之對照向）。
```

---

## 1. P1 —— 標的**目前不存在**

實測 `features/` 之目錄清單：

```
amfm  comfort  home  media  power  privacy  projection  sxm
time_management  user_profiles  vehicle_setting
```

**無 `vehicle setting`（含空白）。** 若確曾建立，則已被刪；
若從未建立，則 A-VS19 之「誤建目錄」一節須改寫為
「`new_feature.py` 會產生含空白之目錄名（工具缺陷），本次未落地」。

查證（兩者皆須跑，因 `ls` 對空白目錄易誤讀）：

```bash
cd /Users/peihe/Work_Projects/TC_Generator
ls -d features/*/ | cat -A | grep -n ' '        # 目錄名含空白者
git ls-files --error-unmatch "features/vehicle setting" 2>&1 | head -1
```

- 第一條無輸出 → 工作區無此目錄
- 第二條回 `did not match any file` → 版控中亦無

**兩條皆為空即 P1 關閉**，並請執行層據此改寫 A-VS19 之措辭。
若第一條有輸出，再執行：

```bash
ls -la "features/vehicle setting"     # 先看內容，確認僅 scaffold 模板
rm -rf "features/vehicle setting"
```

---

## 2. P10 —— `.gitignore` 之修改

```bash
cd /Users/peihe/Work_Projects/TC_Generator/features/vehicle_setting

# 備份現況（一行，供比對）
sed -n '1,3p' .gitignore

# 修改：第 2 行 inputs/ → inputs/* 並在其後加否定式
python3 - <<'PY'
from pathlib import Path
p = Path('.gitignore')
s = p.read_text(encoding='utf-8')
assert '\ninputs/\n' in s, 'inputs/ 行不在預期形態，停止'
s = s.replace('\ninputs/\n', '\ninputs/*\n!inputs/INPUTS.sha256\n', 1)
p.write_text(s, encoding='utf-8')
print(s.splitlines()[:4])
PY

# 兩向驗證（R-VS16′）
cd /Users/peihe/Work_Projects/TC_Generator
git check-ignore -v features/vehicle_setting/inputs/INPUTS.sha256 ; echo "exit=$?  (期望 exit=1、無輸出)"
git check-ignore -v features/vehicle_setting/inputs/leaves.tsv    ; echo "exit=$?  (期望 exit=0、有輸出)"
```

> 第二條之標的須為 `inputs/` 內確實存在之素材檔；
> `leaves.tsv` 實際在 `data/` 而非 `inputs/`，請改用 `inputs/` 內任一檔名
> （如四份 037 之一）。**此處故意留為需你替換之處，不代填檔名。**

---

## 3. P2 —— 入庫

### 3.1 入庫前之三項確認

```bash
cd /Users/peihe/Work_Projects/TC_Generator

# (a) 目前分支與工作區狀態（唯讀）
git status --porcelain=v1 -- features/vehicle_setting | head -50
git branch --show-current

# (b) 確認不會誤帶他 feature 之變更
git status --porcelain=v1 | grep -v '^.. features/vehicle_setting/' | head -20

# (c) 確認 inputs/ 之素材確實被擋（P10 已做則此處應只剩 INPUTS.sha256）
git status --porcelain=v1 --ignored -- features/vehicle_setting/inputs | head
```

### 3.2 兩個暫存產物 —— 入庫前先決定

`data/` 內有 `_cfts_values.json`、`_cfts_values3.json`，
**以底線開頭，形似中間產物**。兩種處置擇一：

```bash
# 甲：視為可重建之中間產物 → 加入 .gitignore，不入庫
#     於 features/vehicle_setting/.gitignore 之 "Regenerable artifacts" 段加入：
#         data/_*.json

# 乙：視為 W-20 三式抽取之證據 → 入庫，但改名去底線
#     git mv 之前先確認其內容是否為最終版
```

**分析層建議甲**：其為 W-8／W-19／W-20 之中間輸出，
最終結論已落 `data/spec_variables.tsv` 與 `docs/reports/`；
且 W-22／W-23 會使其重生。**但此為版控範圍之決定，屬你。**

### 3.3 入庫

```bash
git add features/vehicle_setting/.gitignore \
        features/vehicle_setting/RULINGS.md \
        features/vehicle_setting/ANOMALIES.md \
        features/vehicle_setting/DATA_REQUESTS.md \
        features/vehicle_setting/DECISIONS.md \
        features/vehicle_setting/RECON.md \
        features/vehicle_setting/PLAYBOOK.md \
        features/vehicle_setting/RUNBOOK.md \
        features/vehicle_setting/feature.yaml \
        features/vehicle_setting/docs/ \
        features/vehicle_setting/data/ \
        features/vehicle_setting/inputs/INPUTS.sha256

# 入庫前最後檢查：暫存區內容逐檔列出
git diff --cached --name-only | sed -n '1,80p'
git diff --cached --stat | tail -3

git commit -m "feat(vehicle_setting): rounds 00-02 intake, recon, rulings R-VS1..R-VS21"
```

### 3.4 入庫後之驗證

```bash
# 雜湊檔確實入庫（R-VS16′ 之目的）
git ls-files features/vehicle_setting/inputs/
#   期望：僅 INPUTS.sha256 一行

# 素材確實未入庫
git ls-files features/vehicle_setting/inputs/ | wc -l    # 期望 1

# 雜湊仍可驗（G-9 之「可執行之 shasum -c」）
cd features/vehicle_setting/inputs && shasum -c INPUTS.sha256 && cd -
```

---

## 4. 執行順序（不得對調）

```
P1 查證  →  P10 修改＋兩向驗證  →  P2 三項確認  →  P2 入庫  →  P2 驗證
```

**P10 必須在 P2 之前**：否則 `git add features/vehicle_setting/inputs/INPUTS.sha256`
會被 `.gitignore` 擋下（`git add` 對被忽略之檔案預設靜默跳過，
**不報錯** —— 你會以為加進去了）。

若順序不慎顛倒，補救為：修 `.gitignore` 後重跑 `git add` 該檔並
`git commit --amend`（**amend 屬改寫歷史，仍為你之決定**）。

---

## 5. 本包產生之新條文清單（自檢）

| 條 | 主題 | 已以區塊形式出現 |
|---|---|---|
| R-VS16′ | `.gitignore` 之 `inputs/*` ＋ 否定式；兩向驗證 | ✔ §0 |

一條，以獨立可貼入之區塊呈現。
