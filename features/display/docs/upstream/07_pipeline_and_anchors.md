# 上繳包 07 —— Q5 定案 B 之實作、錨優先序、分隔符正規化

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/07_pipeline_and_anchors.md`
- 結果：**步驟 1–11 全數執行；二十條停止條件全未觸發**
- 全部 git 操作屬 Pei —— §12 只備妥訊息與 pathspec，未執行

---

## 0. 最須先看的一項：Q5-B 沒有達到它的目的

R-DM24 之目的為使 `recon.py` 可跑。覆寫機制已依五項拘束實作完成、
回歸驗證通過，**但 `recon.py` 仍失敗於同一點，且成因已定位**：

`"Analysis Report"` 這個分頁名在共用腳本中**寫死於 5 處**，
Q5-B 只繞過其中 1 處。詳見 §5 與 A-DM21。

機制本身完好，可保留；但**選項 B 之授權範圍不足以達成其宣稱之目的**。
這屬 Tier 2，執行層不裁定、未擅自擴大改動。

---

## 1. §四五條之抄錄核對表（步驟 1）

| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |
|---|---|---|---|---|---|
| 26 | R-DM24 | `features/display/RULINGS.md` | 486 | `5ee430b93d0e0f8e` | 是 |
| 27 | R-DM25 | 同上 | 628 | `6ef20babc3611b16` | 是 |
| 28 | R-DM26 | 同上 | 468 | `dfc9bead9640b0e6` | 是 |
| 29 | R-DM27 | 同上 | 472 | `3d2e2e87dfa6ba1f` | 是 |
| — | R-G17 | `docs/fw036/RULINGS_LEDGER.md` | 394 | `8e1a45c80c9a3d95` | 是 |

**5/5 逐字元相符**；Display 累計 **29/29**。

### 1.1 核對式之第二則注意事項

下放包 07 首次出現帶資訊字串之圍籬（` ```yaml `）。我原本的
`^```\n(.*?)^```\n` 會把 ` ```yaml ` 當成內容而錯配區塊界線 ——
首次執行即以 `IndexError` 中止。已改用 `^```(\w*)\n`。

`RULINGS.md` 之「廢止與取代之對照」表已補三列（R-DM8→R-DM27、
R-DM22(c) 未廢止之澄清、heading 優先序→R-DM26）。

### 1.2 §1.3 之更正已獨立複驗，我的數字確實錯了

| 項 | 分析層 §1.3 | 執行層獨立複驗 |
|---|---|---|
| `_polarion` r4 起資料列 | — | 367 |
| 欄位列舉字典（鍵含 `:`） | 2 | **2** |
| 工作項連結列（鍵無 `:`） | 340 | **340** |
| 能與 `Basic Report` 81 欄名對上之字典鍵 | 2 | **2** |
| `Type` 欄違規列數 | 0 | **0**（333/333 皆 `SYS2_System Requirements Analysis`） |

我上繳 06 §10 第 4 項寫「其餘 340 個欄位字典完全未用」—— **那 340 列是
工作項連結（`NR1L/NRL-163104` 等），不是欄位字典。** 更正成立，
該待辦結案。

---

## 2. `intake.py` 之改動 diff 全文（步驟 2）

```diff
--- scripts/intake.py (before)	2026-08-25 09:58:53
+++ scripts/intake.py (after)	2026-08-25 09:58:53
@@ -32,6 +32,13 @@
   (SWRA-A02 = TC source; the SWE1 037-A03 flagged for role confirmation);
   need list correctly reported as not derivable; spec_mode D proposed
 
+6. Honours `intake.kind_overrides` in the feature's feature.yaml, so a
+   feature whose report does not carry an 'Analysis Report' sheet can name
+   the kind by hand instead of the shared signature table being widened
+   (Q5 settled as option B; Display R-DM24). An override applies only when
+   the file's sha256 matches the declared one, and both INTAKE.md and
+   intake.json record `kind_source: override` with the stated reason.
+
 Tier 0 output: INTAKE.md + intake.json. Obtaining missing files stays
 Tier 3 (Pei).
 
@@ -212,7 +219,34 @@
     return "spec_pdf", f"text-layer on {text_pages}/{len(per_page)} pages"
 
 
-def classify(folder: Path) -> list[dict]:
+def load_kind_overrides(root: Path, feature: str) -> dict:
+    """`intake.kind_overrides` out of the feature's feature.yaml, or {}.
+
+    Q5 was settled as option B (Display R-DM24): the sheet-signature table
+    stays untouched and a feature may name a file's kind by hand. Absent the
+    section — and absent the feature directory, as for an ad-hoc drop folder
+    — this returns {} and classification behaves exactly as before.
+    """
+    fy = root / "features" / feature.lower() / "feature.yaml"
+    if not fy.is_file():
+        return {}
+    try:
+        import yaml
+        cfg = yaml.safe_load(fy.read_text(encoding="utf-8")) or {}
+    except Exception as e:                       # malformed yaml is the
+        print(f"WARNING: cannot read {fy}: {e}")  # feature's problem, not
+        return {}                                 # a reason to crash intake
+    ov = (cfg.get("intake") or {}).get("kind_overrides") or {}
+    return ov if isinstance(ov, dict) else {}
+
+
+def _sha256(path: Path) -> str:
+    import hashlib
+    return hashlib.sha256(path.read_bytes()).hexdigest()
+
+
+def classify(folder: Path, overrides: dict | None = None) -> list[dict]:
+    overrides = overrides or {}
     out = []
     for p in sorted(folder.iterdir()):
         if p.name.startswith(".") or p.is_dir():
@@ -228,7 +262,29 @@
             kind, note = "cfts_doc", "CFTS/Word candidate (spec_mode D)"
         else:
             kind, note = "unclassified", f"unhandled extension {ext}"
-        out.append({"file": p.name, "kind": kind, "note": note})
+        rec = {"file": p.name, "kind": kind, "note": note,
+               "kind_source": "signature", "reason": ""}
+
+        # An override bypasses the classifier, so it is pinned to exact bits:
+        # it applies only when the file's own sha256 equals the declared one.
+        # A mismatch is announced and the signature result stands — never a
+        # silent skip (R-DM24(b)).
+        ov = overrides.get(p.name)
+        if ov:
+            want = str(ov.get("sha256", "")).strip().lower()
+            got = _sha256(p)
+            if not want:
+                print(f"WARNING: kind_override for `{p.name}` has no sha256 "
+                      f"— NOT applied (R-DM24(a))")
+            elif want != got:
+                print(f"WARNING: kind_override for `{p.name}` NOT applied — "
+                      f"sha256 mismatch (declared {want[:16]}…, "
+                      f"actual {got[:16]}…); signature result `{kind}` stands")
+            else:
+                rec.update(kind=str(ov.get("kind", kind)),
+                           kind_source="override",
+                           reason=str(ov.get("reason", "")))
+        out.append(rec)
     return out
 
 
@@ -367,7 +423,11 @@
     lines.append("## Classified files")
     for f in files:
         note = f" — {f['note']}" if f["note"] else ""
-        lines.append(f"- `{f['file']}` → **{f['kind']}**{note}")
+        src = f.get("kind_source", "signature")
+        tag = "" if src == "signature" else f" [kind_source: {src}]"
+        lines.append(f"- `{f['file']}` → **{f['kind']}**{tag}{note}")
+        if src == "override" and f.get("reason"):
+            lines.append(f"  - override reason: {f['reason']}")
     lines.append("")
     swras = [f for f in files if f["kind"] == "swra_report"]
     wbk = next((f for f in files if f["kind"] == "workbook"), None)
@@ -511,7 +571,8 @@
     if not folder.is_dir():
         sys.exit(f"drop folder not found: {folder}")
 
-    files = classify(folder)
+    overrides = load_kind_overrides(root, args.feature)
+    files = classify(folder, overrides)
     swras = [f for f in files if f["kind"] == "swra_report"]
     cited, matched, pick = Counter(), [], None
     if swras:
```

五項拘束之落實：

| 拘束 | 落實 |
|---|---|
| (a) 鍵為檔名，值須含 `kind`／`reason`／`sha256` | 讀 `ov["kind"]`／`ov["reason"]`／`ov["sha256"]`；缺 `sha256` 者警示並**不套用** |
| (b) 雜湊不符則不套用並警示，不得靜默略過 | 兩條 `print("WARNING: …")` 分別處理「無 sha256」與「sha256 不符」，且明寫「signature result `<kind>` stands」 |
| (c) 無 `kind_overrides` 節時行為完全相同 | `load_kind_overrides()` 於 feature 目錄不存在、yaml 無該節、或 yaml 損壞時一律回 `{}`；§3 之回歸 14/14 逐字相同為其證 |
| (d) `INTAKE.md`／`intake.json` 須記 `kind_source` 與 `reason` | 每筆 `files` 記錄新增 `kind_source`／`reason` 兩鍵（`intake.json` 直接序列化該 dict）；`INTAKE.md` 於非 signature 者印 `[kind_source: override]` 並另起一行印 reason 全文 |
| (e) 回歸比對 | §3 |

**`SHEET_SIGNATURES` 逐字未動** —— 已以 `diff` 對該區塊前後 21 行比對，
無差異。

---

## 3. 回歸比對逐檔對照表（步驟 2，§2.2）

### 3.1 先講一個問題：`_intake/` 的原始語料已被搬空

依 §2.2 對 `_intake/` 下六個目錄跑比對，實測其分類檔數：

| 目錄 | 可分類之檔 |
|---|---|
| `AMFM` | **0** |
| `Comfort` | **0** |
| `Display` | 0（本輪還原為 4，見下） |
| `Privacy` | **0** |
| `SXM` | 2 |
| `Time_Management` | **0** |

歷次 `--scaffold` 已把素材 `shutil.move` 進各 feature 之 `inputs/`。
**以這樣的語料跑回歸，「無變化」證明不了任何事** —— 四個目錄根本沒有
檔案可分類。

兩項處置：

1. **還原 Display 之四份素材**至 `_intake/Display/`（自
   `features/display/inputs/` 複製，位元相同），使分類器有標的。
2. **另建 8 個 `_intake/_regr_<feature>/` 臨時語料**，以 hard link 指向
   各 feature `inputs/` 下之 `.xlsx`／`.docx`／`.doc`／`.pdf`，
   涵蓋 comfort／power／power_moding／privacy／sxm／time_management／
   user_profiles／vehicle_setting。

擴充後之回歸母體：**14 個目錄、82 個分類檔**，涵蓋 7 種 kind
（`cfts_doc` 20、`swra_report` 19、`spec_xlsx` 16、`polarion_export` 11、
`workbook` 10、`spec_pdf` 3、`popup_list` 2、`unclassified` 1）。

### 3.2 逐目錄對照（改動前 vs 改動後，**皆未宣告任何覆寫**）

比對方式：`diff` 兩次執行之 `INTAKE.md` 全文（含每檔之 `kind` 與 `note`、
need list、spec_mode、Action 各節）。

| 目錄 | 分類檔數 | 結果 |
|---|---|---|
| `AMFM` | 0 | **IDENTICAL** |
| `Comfort` | 0 | **IDENTICAL** |
| `Display` | 4 | **IDENTICAL** |
| `Privacy` | 0 | **IDENTICAL** |
| `SXM` | 2 | **IDENTICAL** |
| `Time_Management` | 0 | **IDENTICAL** |
| `_regr_comfort` | 8 | **IDENTICAL** |
| `_regr_power` | 7 | **IDENTICAL** |
| `_regr_power_moding` | 6 | **IDENTICAL** |
| `_regr_privacy` | 8 | **IDENTICAL** |
| `_regr_sxm` | 3 | **IDENTICAL** |
| `_regr_time_management` | 10 | **IDENTICAL** |
| `_regr_user_profiles` | 4 | **IDENTICAL** |
| `_regr_vehicle_setting` | 30 | **IDENTICAL** |

**14/14 逐字相同，0 差異。** 停止條件 18 未觸發。
此即 R-DM24(c)「缺省惰性」之證明：未宣告覆寫時，改動後之行為與改動前
在 82 個檔上逐字一致。

> `_regr_*` 為臨時語料，本輪結束後刪除（其內容為 hard link，
> 刪除不影響各 feature 之 `inputs/`）。`_intake/` 全域被 `.gitignore`
> 排除，未入 git。

---

## 4. `feature.yaml` 之 `intake.kind_overrides` 節（步驟 3）

```yaml
# R-DM24（Q5 定案 B，Pei 2026-08-25）：以人工指定 kind 取代放寬共用分類器。
# `scripts/intake.py` 之 SHEET_SIGNATURES 一字未動；覆寫僅在下列 sha256
# 與該檔實際雜湊相符時生效，不符則不套用並警示（不得靜默略過）。
intake:
  kind_overrides:
    "Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx":
      kind: a03_report
      reason: "R-DM5: no 'Analysis Report' sheet; sheets are SWE1 Requirements / SYS2 Traceability / Excluded NRLs (HW-only)"
      sha256: "ab3198e81fb21d2182f5dd7a665488aac5eb937481cf6bede9ecc668f3185050"
```

覆寫生效之輸出（步驟 4）：

```
- `Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` → **a03_report** [kind_source: override] — sheets: SWE1 Requirements, SYS2 Traceability, Excluded NRLs (HW-only)
  - override reason: R-DM5: no 'Analysis Report' sheet; sheets are SWE1 Requirements / SYS2 Traceability / Excluded NRLs (HW-only)
```

`kind_source: override` 與 reason 全文皆現身，`intake.json` 同步。

---

## 5. `recon.py` 之執行結果（步驟 5）—— 仍失敗，成因已定位

```
File "/Users/peihe/Work_Projects/TC_Generator/scripts/recon.py", line 1112, in main
    a03res = survey_a03(paths["a03_report"])
File "/Users/peihe/Work_Projects/TC_Generator/scripts/recon.py", line 568, in survey_a03
    ws = wb["Analysis Report"]
KeyError: 'Worksheet Analysis Report does not exist.'
```

失敗點與上繳 02 §A-DM8 所報者**逐字相同**。依 R-DM24 末段未修 `recon.py`。

### 5.1 為何 Q5-B 沒有解到它

`"Analysis Report"` 寫死於 **5 處**：

| 位置 | 用途 | Q5-B 觸及 |
|---|---|---|
| `scripts/intake.py:63` | `SHEET_SIGNATURES` 之判準 | **是** |
| `scripts/intake.py:114` | `_swra_profile()` | 否 |
| `scripts/intake.py:311` | `cited_documents()` | 否 |
| `scripts/recon.py:568` | `survey_a03()` | 否 |
| `scripts/compare_req_families.py:41` | `SHEET` 常數 | 否 |

`recon.py` 讀的是 `feature.yaml` 之 `paths.a03_report`（本 feature 於
02 輪即已人工填妥），**它從來就不經過 `intake.py` 的分類結果**。
故繞過分類器對 `recon.py` 沒有任何影響。

### 5.2 另一件必須回報的事：條文所載之 `kind` 值不驅動下游

R-DM24 之範例寫 `kind: a03_report`。實測：

| 設定 | 結果 |
|---|---|
| `kind: a03_report`（**條文所載**） | 覆寫生效、標記正確、**不崩潰**；但下游完全未被驅動 —— need list 仍輸出 `NO requirement report found` |
| `kind: swra_report`（`intake.py` 之 kind 詞彙） | 下游被驅動，`intake.py` **當場崩潰**於 `cited_documents()` 之 `wb["Analysis Report"]`（`intake.py:311`） |

成因：`a03_report` 是 `feature.yaml` 之 **paths 鍵**，而 `intake.py` 之
kind 詞彙是 `swra_report`（`KIND_TO_YAML` 將後者映至前者）。

**本輪保留條文所載之 `a03_report`，未自行改為 `swra_report`** ——
那會改動條文指定之值，且改了也只是把「不驅動」換成「崩潰」。
以 **A-DM21** 登記，處置屬 Tier 2。

### 5.3 交叉檢查仍未取得

步驟 5 之後半（跑通則與十四支自寫腳本逐項對照）**無法執行**。
連續五輪之「無獨立管線交叉檢查」未解，且本輪查明它不是一個
可由 Q5-B 解決的問題。

---

## 6. R-DM26 後之錨分布（步驟 6）

舊檔保留為 `data/coverage_sys2_vs_swe_dm.PRE_PRIORITY.tsv`（檔頭加註）。

```
## candidate_from 分布（哪一種錨產生了候選）
  heading only      : 4
  glossary only     : 12
  兩者皆有          : 0
  無候選            : 64

## anchor_kind 分布（最高優先之現存錨；R-DM26 新序：
##   signal > value > glossary_phrase > glossary_phrase_norm > melco > heading > none）
  signal: 43
  heading: 37

```

### 6.1 `glossary_phrase` 仍為 0 —— 但這次不是 heading 的錯

R-DM26 之診斷是「heading 100% 命中會遮蔽其下所有錨」。調整後實測：

| 產生候選之錨 | 列 | 其 `anchor_kind` |
|---|---|---|
| heading | r31–r34（4 列） | **signal ×4** |
| glossary | r37/41/42/44/45/52/53/54/213/217/219/226（12 列） | **signal ×12** |

**16 個產生候選之列全部同時含 `$signal$`**，而 `signal` 在新舊優先序中
皆居首。故 `anchor_kind` 分布在 R-DM26 前後**皆為 `signal 43 / heading
37`**，一字未變。

R-DM26 之調整仍應保留（heading 之 100% 存在性確實不宜居高位），
但它解決不了「`anchor_kind` 看不見候選來源」這件事 ——
因為**兩欄回答的是不同的問題**：`anchor_kind` 答「這列帶有哪些證據」，
`candidate_from` 答「是什麼把它連到 leaf」。以 **A-DM22** 登記。

引用時一律以 `candidate_from` 為準（R-DM12／R-DM26 已規定兩欄並列
不合併）。

---

## 7. R-DM25 後之 PROXI `related_leaf`（步驟 7）

正規化之定義已逐字寫入 `data/proxi_candidates.tsv` 檔頭。

### 7.1 嚴格與正規化兩數並列

| anchor_kind | 列數 |
|---|---|
| `leaf_phrase` | 0 |
| `glossary_phrase`（**嚴格比對即成立**） | **0** |
| `glossary_phrase_norm`（**正規化後才成立**） | **1** |
| `cfts_usage` | 1 |
| `proxi_param` | 175 |
| `none` | 269 |

那一列：

```
| r170 | RVC_SK_PRSNT | Rear Camera soft key present | 401 ¦ 494
| 0 = Absent 1 = Present ¦ 0 = Absent 1 = Present
| SWE-DM-007 ¦ SWE-DM-008 | glossary_phrase_norm |
```

**這是本 feature 首次出現 leaf ↔ PROXI 之連結。** 其值域為
`0 = Absent 1 = Present`（PROXI `Format` r401 `Rear_View_Camera`、
r494 `Rear_View_Camera_Soft_Button`）。

### 7.2 停止條件 19 之檢查：**未觸發**

正規化是否使原本不同之識別碼變為相等 —— 三組母體逐一檢：

| 母體 | 相異名 | 正規化後之碰撞組 |
|---|---|---|
| PROXI `Format` 之 `Parameter Name` | 1,052 | **0** |
| LID `Proxi & Configuration` 之 Logical Identifier | 429 | **0** |
| LID `CAN Mapping` 之 Logical Identifier | 2,548 | **0** |

三組皆無任何兩名在 `[ _]+ → " "` 後相等。

### 7.3 `DSP_SK_PRSNT` 仍未解

正規化不影響它：`Display_OFF_SoftKey_Prsnt` 與 PROXI r692 之
`Display_OFF_SoftKey` 之差是**尾綴 `_Prsnt` 之有無**，非分隔符。
M-3／DR-DM6 維持 OPEN。

---

## 8. 037 八條之缺值點逐條列表（步驟 8）

輸出：`data/leaf_value_gaps.tsv`（檔頭載明本欄為揭露非裁定）。

| leaf | 數值＋單位 | `$Signal$` | 未給值之抽象量詞（逐字取自描述） |
|---|---|---|---|
| SWE-DM-001 | 0 | 0 | `appropriate` ¦ `timeout` |
| SWE-DM-002 | 0 | 0 | `previous` ¦ `valid` |
| SWE-DM-003 | 0 | 0 | `timeout` |
| SWE-DM-004 | 0 | 0 | `configured` ¦ `threshold` |
| SWE-DM-005 | 0 | 0 | `critical` |
| SWE-DM-006 | 0 | 0 | `arbitrat` ¦ `critical` ¦ `priority` ¦ `proper` |
| SWE-DM-007 | 0 | 0 | `previous` |
| SWE-DM-008 | 0 | 0 | `arbitrat` ¦ `seamless` |

**001 之 `timeout` 與 002 之 `previous`／`valid` 原不在 R-DM8 之四處之列**
—— R-DM27 之全稱化因此不是措辭調整，是把兩個實際存在的缺口納入。

`DATA_REQUESTS.md` 之 R-DM8 查證表已加註 R-DM27 之範圍變更；
禁止回填之規定不變。

---

## 9. `_polarion` 校驗之結清（步驟 9，R-G17）

已於 `ANOMALIES.md` A-DM4 之下新增「結清」小節，載明：

- `_polarion` r4 起 367 列中，**鍵含 `:` 之 27 列才是欄位字典**（相異鍵 2），
  其餘 340 列為工作項連結（`NR1L/NRL-163104` 形態）
- `Basic Report` 之 81 個欄名中能與字典鍵對上者**恰為 2 個**
- 逐欄校驗：`Category` 違規 **117/333**；`Type` 違規 **0/333**
- **可校驗之欄只有兩個，兩個都已校驗完畢** → 上繳 06 §10 第 4 項**結案**

R-G17 之警示（誤把工作項列計入會產生做不完的待辦）在本案即為實例。

---

## 10. `DR-DM8` 全文（步驟 10）

```
| DR-DM8 | 確認 037 之 `DISPLAY_ON`／`DISPLAY_OFF`（`SWE-DM-001`／`002`）
與 SYS2／DBC 之 `DISP_ON`／`DISP_OFF` 是否為同一狀態 | OPEN
| SWE-DM-001、SWE-DM-002
| 狀態名無法對應，TC 之預期結果無法引用 DBC 之 `VAL_` 標籤
| A-DM18 | HIGH |
```

**執行層不自行認定二者同一**：無 `(...)` 並列故 R-DM22 建不了條目；
非分隔符差異故 R-DM25 亦不適用（`DISPLAY_ON` → `DISP_ON` 是**字元刪除**，
不是分隔符互換）。

---

## 11. 「本包是否仍有該驗而未驗者」—— 執行層之獨立判斷

**有，共 6 項。**

1. **交叉檢查仍未取得，且現已知 Q5-B 解不了它**（§5.3）。連續五輪。
   本輪把問題從「不知為何跑不動」推進到「知道是 5 處寫死的分頁名，
   Q5-B 只碰到 1 處」—— 但可用的獨立管線仍然是零。
2. **`_regr_*` 語料揭露了一件本輪沒查的事**：`_intake/` 下四個目錄
   為空，代表**那四個 feature 之 intake 結果現在無法重現**。
   本輪為 Display 還原了素材，其餘四個沒有。若日後要複驗它們的
   分類，會遇到同一個空目錄問題。
3. **`intake.py` 之覆寫機制只在 Display 一個 feature、一個檔上行使過。**
   雜湊不符之分支（R-DM24(b)）我讀過程式碼但**未以實際不符之檔測過**
   —— 那條 `WARNING` 路徑未經執行驗證。
4. **`compare_req_families.py:41` 之 `SHEET` 常數未查其使用者。**
   §5.1 列出它是第 5 處寫死，但沒查誰在呼叫它、本 feature 是否會用到。
5. **PROXI 之 269 列（(2) 未追查）仍無人排程**（連續兩輪）。
   DR-DM7（本專案 VF 代碼）若到齊可望收斂母體，尚未到齊。
6. **`glossary_phrase_norm` 目前只有 1 列。** 該正規化是否還能解開
   其他被底線擋住的對應，本輪只在 PROXI 側施用，**未回頭施用於
   SYS2 覆蓋對照**（SYS2 之 `Description` 是散文，底線少見，
   但我沒有實測過這個判斷）。

另記本輪**已驗而下放包未要求**者：`"Analysis Report"` 之 5 處全域清點；
`kind: a03_report` vs `swra_report` 之兩種行為實測；`_intake/` 四個目錄
為空之發現與 `_regr_*` 語料之建立；停止條件 19 之三組母體碰撞檢查；
`Type` 欄之 0 違規複驗。

---

## 12. 建議之 commit 訊息與 pathspec（**未執行**）

```
feat(intake): kind_overrides mechanism (Q5 option B); display round 07

- R-DM24/25/26/27 + R-G17 verbatim (5/5, 29/29 cumulative)
- intake.py reads intake.kind_overrides from feature.yaml; an override
  applies only when the file's sha256 matches, a mismatch warns and the
  signature result stands, and INTAKE.md/intake.json record kind_source
  and the stated reason. SHEET_SIGNATURES is untouched, verified by diff
- regression over 14 drop folders / 82 files: byte-identical before and
  after with no override declared. Four _intake dirs were empty, so the
  corpus was rebuilt from each feature's inputs/ to make the check mean
  something
- recon.py still fails at the same line: "Analysis Report" is hard-coded
  in 5 places and Q5-B only bypasses one of them (A-DM21). The ruling's
  kind: a03_report does not drive the downstream path; kind: swra_report
  would, and crashes on the same assumption inside intake.py itself
- R-DM26 anchor priority applied; glossary_phrase still shows 0 because
  all 16 candidate-producing rows also carry a $signal$ (A-DM22)
- R-DM25 normalisation ties RVC_SK_PRSNT to PROXI r401/r494 — the first
  leaf-to-PROXI link in this feature. No identifier collisions in three
  populations, so the stop condition does not fire
- R-DM27: leaf_value_gaps.tsv, all 8 leaves carry 0 values and 0 signals
- _polarion audit closed: only 2 of its keys are field dictionaries
- DR-DM8 for DISPLAY_ON vs DISP_ON
```

pathspec：

```
git add scripts/intake.py \
        docs/fw036/RULINGS_LEDGER.md \
        features/display/RULINGS.md \
        features/display/ANOMALIES.md \
        features/display/DATA_REQUESTS.md \
        features/display/feature.yaml \
        features/display/scripts/ \
        features/display/data/ \
        features/display/docs/
```

**本輪首次帶入 `scripts/intake.py`**（R-DM24 授權範圍內，
`SHEET_SIGNATURES` 未動）。`_intake/` 全域被 `.gitignore` 排除，
`_regr_*` 臨時語料與還原之 Display 素材皆不入 git。
