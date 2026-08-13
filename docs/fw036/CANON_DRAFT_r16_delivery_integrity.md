# CANON 增補草案 — P7 交付件結構完整性（R16-4 / R18-3）

執行層草擬 2026-08-13，同日依 **R18-3** 更新。
**這是草案，供 Pei 簽；canon 本體未動。**

> **R18-3 已簽署之常設規則（逐字）** —— 本草案之規則 1–3 即為其展開版，
> 兩者若有出入以此區塊為準：
>
> ```text
> (1) backend/xlsx_surgical.py 為**唯一**寫回路徑；
>     openpyxl 存檔路徑不得用於任何交付件產出
> (2) 寫回後強制比對輸出與輸入之 zip 成員集合、
>     各 sheet 之 classic / x14 DV 計數，不等即 **ABORT**
>     （非 warn）；允許差異者僅限被寫入之 sheet XML 本身
> (3) 該 invariant 之違反屬 canon §0 第三項，升 Tier 2，
>     不得以放寬 invariant 解決
> ```
>
> R16-2 之全 repo 寫回凍結已於 2026-08-13 解除，代之以上述常設規則。
> **凍結是一次性事件，不入 canon；常設規則才入。**

擬插入 `docs/fw036/FEATURE_ONBOARDING.md` 之 P7 交付段，作為新的一節。
編號待定（現行 §6 為交付段，建議編為 §6.x 或新增 §6a）。

---

## 草案本文

### §6a Delivery integrity — the container, not just the rows

The workbook we ship is a **controlled document**. What makes it that is not
only its cell values: the printer setup, the embedded diagrams, the comment
layer, the dropdown vocabularies and the shared-string table are all part of
the artifact the customer issued and expects back. A delivery that carries
every correct row inside a rebuilt container is still a damaged delivery.

**Rule 1 — never emit a deliverable through `openpyxl.Workbook.save()`.**
`save()` does not write the file it read; it writes a file openpyxl can
describe. Everything outside its object model is dropped or regenerated.
Measured on this repo's own deliveries (2026-08-13):

| feature | source members | delivered members | lost | added | x14 DV |
|---|---|---|---|---|---|
| AMFM v1 | 59 | 48 | 21 | 10 | 2 → 0 |
| Home | 52 | 48 | 14 | 10 | 0 → 0 |
| SXM | 48 | 47 | 11 | 10 | 2 → 0 |

Losses observed across the three: `xl/diagrams/*` (SmartArt), `xl/drawings/
drawing7.xml`, `xl/printerSettings/*.bin`, `xl/comments1.xml` +
`vmlDrawing1.vml` (rewritten to a different comment representation),
`xl/media/image2.jpeg` (re-encoded to PNG, plus six spurious JPEG copies),
`xl/sharedStrings.xml`, `xl/calcChain.xml`, and worksheet `_rels`.

**Rule 2 — the emit path is a zip-level splice.** Rewrite only the XML of
the sheets actually written; copy every other zip member byte-for-byte.
Reference implementation: `backend/xlsx_surgical.py` (`surgical_save`).
openpyxl stays as the calculation layer — it is a fine object model and a
poor archiver.

**Rule 3 — the structural invariant is ABORT-level, and it is canon §0
item 3** (R18-3 clause 3: a violation escalates to Tier 2 and is never
resolved by relaxing the invariant). Before the output is accepted, compare
it against the input:

- zip member set not equal → **ABORT**
- per-sheet `<dataValidation>` and `<x14:dataValidation>` counts not equal
  → **ABORT**
- any member other than the written sheets' XML differing → **ABORT**

The only permitted addition to that allow-list is a member the pipeline
deliberately stamps (e.g. `docProps/core.xml` under a reproducibility
normaliser), and it must be named explicitly at the call site. A violation
is never downgraded to a warning and never resolved by widening the
invariant.

**Rule 4 — `lint green` + matching content hash does NOT establish delivery
integrity.** The two measure orthogonal things: lint and content hashes
measure ROW CONTENT; this invariant measures CONTAINER STRUCTURE. A P7
sign-off that cites only the former has verified half the artifact. AMFM's
R14-C1 sign-off checked seven numeric fields, all correct, on a file already
missing 21 zip members.

**Rule 5 — an absent symptom is not a passing test.** Home's original
carries no `x14:dataValidation`, so the most visible symptom (the dropdown
disappears) could not appear there — while 14 members were lost anyway. Any
"no difference detected" result must state WHICH measures were capable of
detecting a difference on that file. Likewise a delivered file that is
byte-identical to its input has not passed the writer; it has not been
written (Projection).

### Verification artifact

`features/privacy/scripts/xlsx_roundtrip_probe.py` is the canonical probe.
Two modes:

```bash
# forward: does this write path damage this workbook?
python features/privacy/scripts/xlsx_roundtrip_probe.py --workbook <src.xlsx>

# retrospective (R16-3): what did an already-delivered file lose?
python features/privacy/scripts/xlsx_roundtrip_probe.py \
    --workbook <customer original.xlsx> --compare <delivered.xlsx>
```

The probe exercises the PRODUCTION module, not a parallel copy — a probe
that tests its own implementation of the logic proves nothing about the
writer that ships. Exit 0 only when the surgical path is lossless AND the
probe write actually landed.

**Run it**: before P7 on every feature, and again after any change to the
write path.

### The invariant's own test (R18-4)

`tests/test_xlsx_surgical_invariant.py` drives the ABORT path directly, on
the principle that **a check which has never been seen to fail must not be
reported as passing**. Two damage modes, matching the invariant's two
clauses:

1. an output produced through `openpyxl.save()` — member set damaged;
   must ABORT naming the lost and added members
2. an output whose member set is byte-identically NAMED but whose `x14`
   dropdown has been stripped — invisible to clause 1, caught by clause 2

plus a positive control, so an always-raising implementation cannot make
the first two pass. Verified 2026-08-13: 3 passed.

---

## 交叉引用（各 feature profile 須加註，R16-4 後半）

| profile | 加註內容 |
|---|---|
| `FW036_R1L_Projection_Profile.md` | §6a 適用；本 feature 之 `output/` 未經寫回路徑，不得作為 writer 安全之佐證 |
| AMFM / Home / SXM / Privacy profile（如無則於 PLAYBOOK） | §6a 適用；各自之受損登記見 A-AM18 / A-H27 / A-SX28 / A-PV09 |

---

## 草案未決之處（不自裁，列給 Pei）

1. **節號**：`§6a` 或併入現行 §6 之子節，取決於 canon 的編號慣例。
2. ~~凍結解除的條件寫不寫進 canon~~ —— **已決（R18-3）**：凍結於
   2026-08-13 解除，屬一次性事件，不入 canon；入 canon 的是取代它的
   三項常設規則。本草案已據此改寫。
3. **回溯範圍**：本草案不規範「已交付且已受損之檔案是否必須重產」。
   **R18-1 已就本輪個案裁定不重產**（Home / SXM 維持現狀，缺損
   DEFERRED 至下次內容變動），但那是個案裁決，不是通則。
   是否寫成通則（例如「結構缺損不觸發重產，隨下次內容變動修復」）
   仍待 Pei 決定 —— 執行層建議寫，因為它已經被實際適用過一次，
   下次再遇到若無條文就會重新爭論。
4. **rule 5 的適用邊界**：「absent symptom 不算通過」若寫得太寬，
   會變成任何檢測都要先證明自己有偵測力。建議限縮在
   「交付前的結構檢測」這一個場景。
