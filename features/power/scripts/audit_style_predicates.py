"""G176 —— 文字樣式謂詞之形態稽核（R-P250）。

R-P250：凡以文字樣式比對規格原文或 TC 內容之謂詞，
實作前須先量該樣式在語料中之實際書寫形態，
至少涵蓋大小寫、空白（含 NBSP 與多餘空格）、全半形、縮寫與同義變體、換行黏連；
**且須以「已知應命中之實例」驗證 —— 一個都取不到者，該謂詞不得使用。**

本檔為**既有謂詞之回溯稽核**。逐一：

  （1）於語料（264 條 TC 之六欄 ＋ 全部 `source_clause`）計其命中數
       —— **命中 0 者即取不到已知應命中實例**，逐一列出
  （2）**大小寫敏感度**：加 `re.I` 後命中數是否變動
       —— 變動者即該謂詞正受大小寫影響（35 包 `COND_RE` 之形態）
  （3）**空白敏感度**：將語料之連續空白摺為一、NBSP 轉空格後命中數是否變動
       —— 變動者即該謂詞正受空白形態影響（A-PW139 之形態）

**本檔只出量測，不改任何謂詞**（本包不改值，亦不調整判準 —— 17 §I）。
其產出為 37 包之處置清單。

用法：
    python features/power/scripts/audit_style_predicates.py
"""

from __future__ import annotations

import glob
import importlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

TC_FIELDS = ("tc_title", "test_item", "pre_conditions", "input_test_data",
             "test_procedure", "expected_result")

# 本檔自身之謂詞不納入稽核（避免自我指涉）
SKIP_MODULES = {"audit_style_predicates"}


def corpus() -> dict[str, str]:
    """回傳各類語料 —— **謂詞須以其自身之輸入為語料**。

    v1 只用「TC 六欄 ＋ `source_clause`」一種語料，
    致 `TC_ID_RE` / `SEC_RE` / 路徑類 `PM_RE` 等**輸入根本不是 TC 或規格**者
    一律記為「命中 0」，v1 因而誤報 30 個謂詞「不得使用」。
    v2 分四類語料，任一類命中即不算取不到實例。
    """
    tc_parts, spec_parts, id_parts = [], [], []
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        for l in d.get("leaves", []):
            spec_parts.append(str(l.get("source_clause", "")))
            id_parts += [str(l.get("parent", "")), str(l.get("source_anchor", ""))]
        for t in d["tcs"]:
            tc_parts += [str(t.get(k, "")) for k in TC_FIELDS]
            id_parts += [str(t.get("tc_id", "")), str(t.get("req_id", "")),
                         str(t.get("specification_reference", ""))]
    # 原始文字層（`SEC_RE` / `REQ_RE` / `PM_RE` / `PD_RE` 之輸入）
    raw_dir = ROOT / "features/power/data/textlayer"
    raw = "\n".join(f.read_text(encoding="utf-8", errors="ignore")
                    for f in sorted(raw_dir.rglob("*")) if f.is_file())
    # 檔名與路徑（`WRAPPER_RE` 之輸入）
    paths = "\n".join(str(p.relative_to(ROOT))
                      for p in sorted((ROOT / "features/power").rglob("*"))
                      if p.is_file())
    return {"TC": "\n".join(tc_parts), "規格": "\n".join(spec_parts),
            "識別子": "\n".join(id_parts), "文字層": raw, "路徑": paths}


def fold_space(text: str) -> str:
    """摺疊**空白與 NBSP**，**保留換行**。

    v1 以 `" ".join(text.split())` 摺疊，連換行一併摺掉 ——
    致 `STEP_RE`（`^\s*\d+\.`）等**行首錨定**之謂詞必然變動，
    該變動來自量測方式而非謂詞之空白敏感性。v2 逐行摺疊。
    """
    lines = text.replace("\xa0", " ").replace("\u2009", " ").split("\n")
    return "\n".join(" ".join(ln.split()) for ln in lines)


def collect() -> list[tuple[str, str, re.Pattern]]:
    """自各模組取其頂層 `*_RE` 謂詞。"""
    out = []
    for path in sorted(SCRIPTS.glob("*.py")):
        name = path.stem
        if name in SKIP_MODULES:
            continue
        try:
            mod = importlib.import_module(name)
        except Exception as e:                      # 載入失敗者記為無法稽核
            out.append((name, f"**模組載入失敗：{type(e).__name__}**", None))
            continue
        for attr in dir(mod):
            if not attr.endswith("_RE"):
                continue
            val = getattr(mod, attr)
            if isinstance(val, re.Pattern) and getattr(val, "__module__", None) is None:
                pass
            if isinstance(val, re.Pattern):
                # 只取該模組自身定義者（避免 import 而來之重複計數）
                src = path.read_text(encoding="utf-8")
                if re.search(rf"^{attr} = re\.compile", src, re.M):
                    out.append((name, attr, val))
    return out


def main() -> None:
    cor = corpus()
    rows = []
    for mod, attr, pat in collect():
        if pat is None:
            rows.append({"mod": mod, "attr": attr, "n": None})
            continue
        # 行首錨定之謂詞（`^…$`）於串接語料中須帶 `re.M`，
        # 否則其命中必為 0 —— 該 0 為量測方式之假象，非謂詞之缺陷。
        pm = re.compile(pat.pattern, pat.flags | re.M)
        per = {k: max(len(pat.findall(v)), len(pm.findall(v))) for k, v in cor.items()}
        best = max(per, key=lambda k: per[k])
        text = cor[best]
        try:
            n_ci = len(re.compile(pat.pattern, pat.flags | re.I).findall(text))
        except re.error:
            n_ci = None
        rows.append({"mod": mod, "attr": attr, "n": per[best], "per": per,
                     "best": best, "n_ci": n_ci,
                     "n_fold": len(pat.findall(fold_space(text))),
                     "ci_flag": bool(pat.flags & re.I)})

    zero = [r for r in rows if r.get("n") == 0]
    case_sens = [r for r in rows if r.get("n") not in (None, 0) and not r["ci_flag"]
                 and r.get("n_ci") is not None and r["n_ci"] > r["n"]]
    space_sens = [r for r in rows if r.get("n") not in (None, 0)
                  and r["n_fold"] != r["n"]]

    out = ["# G176 —— 文字樣式謂詞之形態稽核（R-P250）\n",
           "\n> **本檔只出量測，不改任何謂詞。** 其產出為 37 包之處置清單。\n",
           "> 語料分四類（TC 六欄 / `source_clause` / 識別子 / 檔案路徑）——\n",
           "> **謂詞須以其自身之輸入為語料**；取其命中最多之一類為準。\n",
           "> 空白摺疊**保留換行**，否則行首錨定之謂詞必然變動（量測方式之假象）。\n",
           f"\n## 一、彙總（{len(rows)} 個謂詞）\n\n| 項 | 數 |\n|---|---|\n",
           f"| **四類語料皆命中 0 —— 取不到已知應命中實例** | **{len(zero)}** |\n",
           f"| **大小寫敏感** —— 未帶 `re.I` 而加之後命中數上升 | **{len(case_sens)}** |\n",
           f"| **空白敏感** —— 摺疊空白後命中數變動 | **{len(space_sens)}** |\n",
           "\n## 二、四類語料皆命中 0 者（R-P250：**不得使用**）\n\n"
           "| 模組 | 謂詞 |\n|---|---|\n"]
    for r in zero:
        out.append(f"| `{r['mod']}` | `{r['attr']}` |\n")
    if not zero:
        out.append("| （無） | |\n")
    out.append("\n## 三、大小寫敏感者\n\n"
               "> 加 `re.I` 後命中數上升，即語料中存在該謂詞抓不到之大小寫變體。\n"
               "> **上升不等於應改** —— 部分謂詞刻意區分大小寫"
               "（如 `rejudge_priority` 之 `CAN` 避開英文字 “can”）。逐一裁決屬 37 包。\n\n"
               "| 模組 | 謂詞 | 語料 | 現行 | 加 `re.I` | 增幅 |\n|---|---|---|---|---|---|\n")
    for r in sorted(case_sens, key=lambda x: -(x["n_ci"] - x["n"])):
        out.append(f"| `{r['mod']}` | `{r['attr']}` | {r['best']} | {r['n']} | "
                   f"{r['n_ci']} | **+{r['n_ci'] - r['n']}** |\n")
    out.append("\n## 四、空白敏感者\n\n"
               "| 模組 | 謂詞 | 語料 | 現行 | 摺疊後 |\n|---|---|---|---|---|\n")
    for r in space_sens:
        out.append(f"| `{r['mod']}` | `{r['attr']}` | {r['best']} | {r['n']} | "
                   f"{r['n_fold']} |\n")
    out.append("\n## 五、逐一\n\n"
               "| 模組 | 謂詞 | 主語料 | 命中 | 加 `re.I` | 摺疊空白 | 已帶 `re.I` |\n"
               "|---|---|---|---|---|---|---|\n")
    for r in rows:
        if r.get("n") is None:
            out.append(f"| `{r['mod']}` | {r['attr']} | — | — | — | — | — |\n")
        else:
            out.append(f"| `{r['mod']}` | `{r['attr']}` | {r['best']} | {r['n']} | "
                       f"{r['n_ci']} | {r['n_fold']} | "
                       f"{'是' if r['ci_flag'] else '否'} |\n")

    p = DATA / "g176_style_predicates.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"謂詞 {len(rows)} 個")
    print(f"  四類皆 0（不得使用）{len(zero)}：{[(r['mod'], r['attr']) for r in zero]}")
    print(f"  大小寫敏感 {len(case_sens)}")
    for r in sorted(case_sens, key=lambda x: -(x['n_ci'] - x['n']))[:10]:
        print(f"     {r['mod']}.{r['attr']}  [{r['best']}]  {r['n']} → {r['n_ci']}")
    print(f"  空白敏感 {len(space_sens)}：{[(r['mod'], r['attr']) for r in space_sens]}")


if __name__ == "__main__":
    main()
