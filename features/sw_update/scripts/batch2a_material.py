#!/usr/bin/env python3
"""T45d —— batch 2a 材料傾印（下放包 32 §2.1）：`315`–`320` 六列。

每列：Title、Description 全文、路徑 A 前 5 候選（含全文）、`Verification Criteria`
全文、`Verification Method`、105 分類、**GT-A1 已裁之錨**、**候選錯誤碼**。

**候選錯誤碼之方法與其界線（T45d 之明令 + R-SU20(d)）**：

其依據為**碼之 Description 之內容**與**需求列之 Description 之內容**之詞彙重疊，
**不是階段名與組名之字面相近**（後者即 R-SU20(d) 所禁之循環）。

**惟本方法仍是詞彙的，不是語意的** —— 其產出為**候選非裁定**，
且**必然同時漏與誤**：碼與需求用不同詞描述同一失敗者會漏
（如 `Emergency State` 與碼側之 `abort`），用同詞描述不同失敗者會誤。
**逐碼之正解須人讀**，本表只縮小人讀之範圍。

Usage: python3 scripts/batch2a_material.py
"""
import re
import sys
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
warnings.filterwarnings("ignore")
from anchor_table import C_ID, C_TITLE, C_SRC, C_SUB, TfIdf      # noqa: E402
from corpus_v2 import corpus_v2, _rows_desc                      # noqa: E402
from error_codes import parse_codes                              # noqa: E402
from observability import classify, RE_EXTERNAL                  # noqa: E402
from verif_columns import _load, _txt, C_VC, C_VM                # noqa: E402

ROWS = [f"SWE1-FOTA-{n}" for n in range(315, 321)]
MECH3 = 0.26716366259482566
# GT-A1（`GROUND_TRUTH.md`）—— 本六列皆已裁，逐位對應
GT = {"SWE1-FOTA-315": ("4907667", "Socket 讀寫錯誤"),
      "SWE1-FOTA-316": ("4907668", "網路遺失之五種情形"),
      "SWE1-FOTA-317": ("4907669", "使用者關閉行動數據／Wi-Fi"),
      "SWE1-FOTA-318": ("4907670", "車輛處於緊急狀態"),
      "SWE1-FOTA-319": ("4907671", "電源遺失 —— **正解不在前 20**（D-1 缺字）"),
      "SWE1-FOTA-320": ("4907672", "主機實體斷開 —— 正解排第 14")}
STOP = set("""the a an of to and or in on for with by shall is are be as that this
其 之 shall not from at into during when if all any each such other""".split())


def toks(s):
    return {w for w in re.findall(r"[a-z]+", s.lower()) if len(w) > 3 and w not in STOP}


def main():
    _, desc = _rows_desc()
    objs = corpus_v2()[0]
    tf = TfIdf([o["text"] for o in objs])
    by, dd, _ = _load()
    internal = {i for i in dd if classify(dd[i])[0]}
    g105 = {i for i in internal
            if not any(r.search(_txt(by[i][C_VC])) for r in RE_EXTERNAL.values())}
    codes, _ = parse_codes()

    print("## T45d —— batch 2a 材料（`315`–`320` 六列）\n")
    print(f"- 機制 3 之門檻（R-SU23(b)，`≤` 為攔下）：首選分 **≤ {MECH3:.3f}**")
    print("- **執行層不撰寫 TC、不裁定錨**；GT-A1 已裁之錨照抄，候選錯誤碼為**候選非裁定**\n")
    print("| # | 037 列 | 標題 | Sub Cat | **105？** | **GT-A1 錨** | 首選分 | 機制 3 |")
    print("|---:|---|---|---|:--:|---|---:|:--:|")
    cand = {}
    for n, i in enumerate(ROWS, 1):
        cand[i] = [(s, objs[j]) for s, j in tf.query(desc[i], top=20)]
        s = cand[i][0][0]
        print(f"| {n} | `{i}` | {_txt(by[i][C_TITLE])[:34]} | {by[i][C_SUB] or '(blank)'} | "
              f"{'**⚠**' if i in g105 else '—'} | `{GT[i][0]}` | {s:.3f} | "
              f"{'**⚠ 攔下**' if s <= MECH3 else '—'} |")
    n105 = [i for i in ROWS if i in g105]
    print(f"\n- **105 列：{len(n105)} / 6** —— {'、'.join('`'+x[-3:]+'`' for x in n105)}"
          f"；不屬者 {'、'.join('`'+x[-3:]+'`' for x in ROWS if x not in g105)}")
    print(f"- **GT-A1 已裁 6 / 6**，其錨 `4907667`–`4907672` **逐位對應**；"
          f"該六 id 亦即 `313` 自證錨之全集（R-SU37(a)）")

    print("\n---\n\n### 逐列材料\n")
    for n, i in enumerate(ROWS, 1):
        r = by[i]
        tag = ("**105 列**（內部列且 VC 亦無外部面）" if i in g105
               else "**126 內部列**（VC 有外部面）" if i in internal else "非內部列")
        print(f"\n---\n\n#### {n}. `{i}` — {_txt(r[C_TITLE])}\n")
        print(f"- 分類：{tag}｜Sub Cat：{r[C_SUB] or '(blank)'}"
              f"｜Priority：{r[15] or '(blank)'}｜Source：`{r[C_SRC]}`")
        print(f"- `Verification Method`：`{_txt(by[i][C_VM]) or '(空)'}`")
        print(f"- **GT-A1 已裁之錨**：`CFTS057-{GT[i][0]}` —— {GT[i][1]}")
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
        for j, (sc, o) in enumerate(cand[i][:5], 1):
            mark = " ✅ **= GT-A1 之正解**" if o["oid"] == GT[i][0] else ""
            print(f"{j}. `{o['oid']}` — 章 **{o['chap']}** {o['chap_title']} — 分 **{sc:.3f}**{mark}")
            print(f"   > {o['text'][:400]}{'…' if len(o['text'])>400 else ''}\n")

        # ── 候選錯誤碼（內容重疊，非階段名字面）──
        rt = toks(desc[i] + " " + _txt(r[C_TITLE]))
        scored = []
        for stage, code, cd, root, rec, _c in codes:
            ov = rt & toks(cd + " " + root)
            if ov:
                scored.append((len(ov), code, cd, stage, sorted(ov)))
        scored.sort(reverse=True)
        print("**候選錯誤碼（R-SU35；依碼之 Description／Root cause 內容，"
              "非階段名字面 —— R-SU20(d)）**：\n")
        if scored:
            print("| 碼 | Description | 階段 | 共同詞 |")
            print("|---|---|---|---|")
            for _, code, cd, stage, ov in scored[:5]:
                print(f"| `{code}` | {cd[:52]} | `{stage[:26]}` | "
                      + "／".join(f"`{w}`" for w in ov[:4]) + " |")
        else:
            print("**無** —— 本列之詞彙與 80 碼皆無重疊。"
                  "**「無候選」不等於「無對應碼」**（詞彙法之漏，見檔首）。")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
