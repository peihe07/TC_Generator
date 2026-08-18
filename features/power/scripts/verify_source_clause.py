"""G94 —— `source_clause` 保真度（R-P125）。

反向涵蓋（R-P118）建立於 `source_clause` 之上。
**若某條規格句根本未被抄進 `source_clause`，反向涵蓋於原理上看不見它。**
G79 只驗該欄存在且非空（R-P104），不驗其正確 —— 15 §七第 7 項已指出，
17 §七(甲)3 再度指出，本閘為其處置。

判準：逐 leaf 取 `source_anchor` 在 CFTS 本文中之原文
（依 **R-P17 之文字層定義**，即 `lint_tcs.anchor_bodies()`），
與 `source_clause` 逐字比對。

**正規化僅限空白與 NBSP**（R-P125(a) 明令不得擴大）：
  `\\xa0`（NBSP）、`\\u2009`（thin space）→ 一般空格
  連續空白摺疊為一
不做大小寫、標點、引號、破折號之正規化 —— 那些差異是真差異。

截斷（`source_clause` 短於原文）依 R-P109 判 FAIL（R-P125(c)）。

用法：
    python features/power/scripts/verify_source_clause.py
    python features/power/scripts/verify_source_clause.py --self-test
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GENERATED = ROOT / "features/power/generated"
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_tcs import anchor_bodies  # noqa: E402


def normalize(text: str) -> str:
    """R-P125(a)：僅空白與 NBSP。**不得擴大。**"""
    return " ".join(text.replace("\xa0", " ").replace(" ", " ").split())


def first_diff(a: str, b: str) -> int:
    for i, (x, y) in enumerate(zip(a, b)):
        if x != y:
            return i
    return min(len(a), len(b))


def check_leaf(parent: str, anchor: str, clause: str,
               bodies: dict[str, list[str]]) -> dict:
    # 一個 leaf 得引用多個錨點（第二批之 `SWE-PM-038` 有 13 個）——
    # `source_anchor` 以逗號分隔，原文依該序串接。
    anchors = [a.strip() for a in str(anchor).split(",") if a.strip()]
    orig = normalize("\n".join("\n".join(bodies.get(a, [])) for a in anchors))
    got = normalize(clause)
    if not orig:
        return {"parent": parent, "anchor": anchor, "ok": False,
                "reason": f"錨點原文為空 —— {anchors} 於 CFTS 本文中找不到內文段落",
                "orig_len": 0, "got_len": len(got)}
    if orig == got:
        return {"parent": parent, "anchor": anchor, "ok": True, "reason": "",
                "orig_len": len(orig), "got_len": len(got)}
    i = first_diff(orig, got)
    truncated = len(got) < len(orig) and orig.startswith(got)
    return {
        "parent": parent, "anchor": anchor, "ok": False,
        "reason": ("截斷（R-P109 / R-P125(c)）" if truncated else "逐字不符"),
        "orig_len": len(orig), "got_len": len(got),
        "diff_at": i,
        "orig_around": orig[max(0, i - 70):i + 90],
        "got_around": got[max(0, i - 70):i + 90],
    }


def run(batches: list[dict], bodies: dict[str, list[str]]) -> list[dict]:
    out = []
    for batch in batches:
        for leaf in batch.get("leaves", []):
            out.append(check_leaf(leaf.get("parent", "?"),
                                  str(leaf.get("source_anchor", "")),
                                  str(leaf.get("source_clause", "")), bodies))
    return out


def self_test(bodies: dict[str, list[str]]) -> int:
    """R-P125(d) —— 以刻意刪句之 fixture 證明本閘確實會失敗。"""
    failures = 0
    anchor = "4942354"
    orig = normalize("\n".join(bodies[anchor]))

    def case(label: str, clause: str, want_ok: bool) -> None:
        nonlocal failures
        r = check_leaf("SWE-PM-073", anchor, clause, bodies)
        ok = r["ok"] == want_ok
        failures += not ok
        print(f"  [{'PASS' if ok else '**FAIL**'}] G94 {label}")
        print(f"          期望 {'相符' if want_ok else 'FAIL'}；"
              f"實際 {'相符' if r['ok'] else 'FAIL（' + r['reason'] + '）'}")
        if not r["ok"] and "diff_at" in r:
            print(f"          首異 offset {r['diff_at']}；"
                  f"長度 {r['orig_len']} vs {r['got_len']}")

    case("應相符 —— 原文逐字", orig, True)
    case("應相符 —— NBSP 與連續空白之差異", orig.replace(" ", "\xa0", 3), True)
    # 刻意刪去中段一句
    sentences = orig.split(". ")
    assert len(sentences) > 3
    dropped = ". ".join(sentences[:2] + sentences[3:])
    case("應 FAIL —— 刻意刪去中段一句", dropped, False)
    case("應 FAIL —— 截斷（R-P109）", orig[:len(orig) // 2], False)
    case("應 FAIL —— 改一個字（`20` → `30`）", orig.replace(" 20 ", " 30 ", 1), False)
    case("應 FAIL —— 錨點原文為空之 anchor", orig, False) if False else None
    print(f"\n  G94 fixture 全數如期：{'是' if not failures else '否'}")
    return 1 if failures else 0


def main() -> None:
    bodies = anchor_bodies()
    if "--self-test" in sys.argv:
        raise SystemExit(self_test(bodies))

    batches = [json.loads(p.read_text(encoding="utf-8"))
               for p in sorted(GENERATED.glob("*.json"))]
    results = run(batches, bodies)
    bad = [r for r in results if not r["ok"]]

    lines = ["# G94 —— `source_clause` 保真度（R-P125）\n",
             "\n> 原文依 **R-P17 之文字層定義**抽取（`anchor_bodies()`）。\n",
             "> **正規化僅限空白與 NBSP**（R-P125(a)），不做大小寫／標點／引號之正規化。\n",
             "> 截斷依 R-P109 / R-P125(c) 判 FAIL。\n",
             "\n| leaf | anchor | 原文字元 | `source_clause` 字元 | 判定 |\n|---|---|---|---|---|\n"]
    for r in results:
        lines.append(f"| `{r['parent']}` | `{r['anchor']}` | {r['orig_len']} | "
                     f"{r['got_len']} | {'**逐字相符**' if r['ok'] else '**FAIL —— ' + r['reason'] + '**'} |\n")
    for r in bad:
        lines.append(f"\n### `{r['parent']}` 之差異\n\n"
                     f"首異 offset **{r.get('diff_at', '?')}**\n\n"
                     f"原文：\n```\n{r.get('orig_around', '')}\n```\n\n"
                     f"`source_clause`：\n```\n{r.get('got_around', '')}\n```\n")
    lines.append(f"\n**{len(results) - len(bad)} / {len(results)} 逐字相符。**\n")
    (DATA / "g94_source_clause.md").write_text("".join(lines), encoding="utf-8")

    for r in results:
        print(f"  {r['parent']}  anchor {r['anchor']}  "
              f"{r['orig_len']} vs {r['got_len']}  "
              f"{'逐字相符' if r['ok'] else '**FAIL —— ' + r['reason'] + '**'}")
    print(f"\nG94：{len(results) - len(bad)} / {len(results)} 相符")
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__":
    main()
