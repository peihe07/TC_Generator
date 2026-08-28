#!/usr/bin/env python3
"""T39c —— 併行線材料傾印（下放包 26 §2.4-3）。

`ROV Installation`（20 列）與 `Update HMI`（6 列）共 **26 列**。
二組之 **105 列數為 0**，故不受 DR-SU2 之議題影響，得與 batch 1 併行起草。

每列傾印：Title、Description 全文、路徑 A 前 5 候選（含候選全文）、
`Verification Criteria` 全文、`Verification Method`、105／126 分類。

**分二節**（下放包 26 T39c 令「分二檔或分節，供分析層分批起草」）——
本檔採分節，二組各一節，節內逐列。

**執行層不撰寫 TC、不裁定錨**（同 T38b）。

Usage: python3 scripts/parallel_material.py > docs/upstream/25_batch1_review.md
"""
import sys
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from anchor_table import C_ID, C_TITLE, C_SRC, C_SUB, TfIdf            # noqa: E402
from corpus_v2 import corpus_v2, _rows_desc                            # noqa: E402
from framework_survey import group_by_heading, a03_rows                # noqa: E402
from observability import classify, RE_EXTERNAL                        # noqa: E402
from verif_columns import _load, _txt, C_VC, C_VM                      # noqa: E402

warnings.filterwarnings("ignore")

# framework.md Part II 之定稿（21 組之第 8／第 12 組）
SETS = [
    ("ROV Installation", "ROV 安裝三階段：安裝前、安裝進度、安裝後",
     ["SWE1-FOTA-086", "SWE1-FOTA-091", "SWE1-FOTA-096", "SWE1-FOTA-085"], 20),
    ("Update HMI", "更新之使用者體驗與 HMI 呈現",
     ["SWE1-FOTA-129"], 6),
]
MECH3 = 0.26716366259482566        # R-SU23(b)：機制 3 之門檻，`≤` 為攔下


def main():
    # `corpus_v2._rows_desc()` 之列已濾為 311 in-scope（**Heading 列不在其中**），
    # 分群須用 `framework_survey.a03_rows()` 之 383 列全表 —— 否則分群結果恆為空。
    _, desc = _rows_desc()
    groups = {g["id"]: g for g in group_by_heading(a03_rows()) if g["id"]}
    objs = corpus_v2()[0]
    tf = TfIdf([o["text"] for o in objs])
    by, dd, _ = _load()
    internal = {i for i in dd if classify(dd[i])[0]}

    def has_ext_vc(i):
        return any(r.search(_txt(by[i][C_VC])) for r in RE_EXTERNAL.values())
    g105 = {i for i in internal if not has_ext_vc(i)}

    print("## T39c —— 併行線材料（`ROV Installation` 20 列 ＋ `Update HMI` 6 列）\n")
    print("- 依據：下放包 26 §2.4-3 —— 二組之 **105 列為 0**，不受 DR-SU2 之議題影響")
    print(f"- 機制 3 之門檻（R-SU23(b)，`≤` 為攔下）：首選分 **≤ {MECH3:.3f}**")
    print("- **執行層不撰寫 TC、不裁定錨**\n")

    allrows, closure = [], []
    for name, cap, heads, expect in SETS:
        got = []
        for h in heads:
            got += groups.get(h, {"rows": []})["rows"]
        closure.append((name, expect, len(got), heads))
        allrows.append((name, cap, got))

    print("### 閉合檢查（R-SU10 v2(d)：列數須與 framework 定稿相符）\n")
    print("| Test Set | framework 載 | 實測 | Heading 群 | |")
    print("|---|---:|---:|---|:--:|")
    ok = True
    for name, expect, n, heads in closure:
        ok &= (expect == n)
        print(f"| `{name}` | {expect} | **{n}** | "
              + "、".join(f"`{h}`" for h in heads)
              + f" | {'✅' if expect == n else '❌'} |")
    tot_e = sum(c[1] for c in closure)
    tot_n = sum(c[2] for c in closure)
    print(f"| **合計** | **{tot_e}** | **{tot_n}** | | {'✅' if tot_e == tot_n else '❌'} |")
    if not ok:
        sys.exit("T39c：列數與 framework 定稿不符，停並回報")

    n105 = [_txt(r[C_ID]) for _, _, rs in allrows for r in rs if _txt(r[C_ID]) in g105]
    nint = [_txt(r[C_ID]) for _, _, rs in allrows for r in rs if _txt(r[C_ID]) in internal]
    print(f"\n- **105 列：{len(n105)}** —— {'、'.join('`'+x+'`' for x in n105) or '**0，與 §2.4-3 之前提相符**'}")
    print(f"- 126 內部列（VC 有外部面）：**{len(nint)}** —— "
          f"{'、'.join('`'+x+'`' for x in nint) or '無'}")

    for name, cap, rs in allrows:
        print(f"\n---\n\n## 節 —— `{name}`（{len(rs)} 列）\n")
        print(f"能力叢集：{cap}\n")
        print("| # | 037 列 | 標題 | Sub Cat | Priority | 105？ | 首選分 | 機制 3 |")
        print("|---:|---|---|---|---|:--:|---:|:--:|")
        cands = {}
        for n, r in enumerate(rs, 1):
            i = _txt(r[C_ID])
            cands[i] = [(s, objs[j]) for s, j in tf.query(desc[i], top=20)]
            s = cands[i][0][0] if cands[i] else 0.0
            print(f"| {n} | `{i}` | {_txt(r[C_TITLE])[:36]} | {r[C_SUB] or '(blank)'} | "
                  f"{r[15] or '(blank)'} | {'**⚠**' if i in g105 else '—'} | {s:.3f} | "
                  f"{'**⚠ 攔下**' if s <= MECH3 else '—'} |")

        print(f"\n### `{name}` —— 逐列材料\n")
        for n, r in enumerate(rs, 1):
            i = _txt(r[C_ID])
            tag = ("**105 列**" if i in g105
                   else "**126 內部列**（VC 有外部面）" if i in internal else "非內部列")
            print(f"\n---\n\n#### {n}. `{i}` — {_txt(r[C_TITLE])}\n")
            print(f"- 分類：{tag}｜Sub Cat：{r[C_SUB] or '(blank)'}"
                  f"｜Priority：{r[15] or '(blank)'}｜Source：`{r[C_SRC]}`")
            print(f"- `Verification Method`：`{_txt(by[i][C_VM]) or '(空)'}`")
            print("\n**Requirement Description 全文**：\n")
            print("> " + (desc[i] or "(空)") + "\n")
            vc = _txt(by[i][C_VC])
            print("**`Verification Criteria` 全文**：\n")
            if vc:
                for ln in vc.split("\n"):
                    if ln.strip():
                        print(f"> {ln.strip()}\n>")
            else:
                print("> **(空)**")
            print("\n**路徑 A（語料 v2）前 5 候選**：\n")
            for j, (sc, o) in enumerate(cands[i][:5], 1):
                print(f"{j}. `{o['oid']}` — 章 **{o['chap']}** {o['chap_title']} — 分 **{sc:.3f}**")
                print(f"   > {o['text'][:420]}{'…' if len(o['text']) > 420 else ''}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
