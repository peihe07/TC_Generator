#!/usr/bin/env python3
"""Step 4 (Time Management) — B1 之上下文產生器。

## 本檔之來源與界線（R-TM29）

**結構參照** `features/privacy/scripts/` 之慣例（`--feature-dir` 介面、
權威自 `feature.yaml` 讀取、輸出為 markdown 供人讀 ＋ json 供下游）。
Privacy 無同名腳本，故其**結構取自同目錄之其餘兩支**，內容自建。

**不繼承任何 TC 內容**：本檔只搬運既有資料（leaf 描述、章節歸屬、
spec 條文原文），**不產生任何措辭**。

## 輸入（皆為既有產物，不重算）

  data/leaf_descriptions.txt      leaf → 標題 ＋ Requirement Description
  data/leaf_to_section_probe.txt  leaf → CFTS015 章節（逗號分隔）＋ SYS-RA 計數
  inputs/*.docx                   CFTS015 原文，供取條文段落

## 輸出

  data/batch_context_<batch>.md    供人讀
  data/batch_context_<batch>.json  供生成腳本讀

用法：
    python3 features/time_management/scripts/build_batch_context.py \
        --feature-dir features/time_management --batch B1 --leaves SWE-RA-TIME&DATE-008,...

**本腳本於 04 包只建立不執行。**
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
import zipfile
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None


class ContextError(RuntimeError):
    pass


def parse_leaf_descriptions(path: Path) -> dict[str, dict]:
    """`SWE-RA-… | 標題` 後接縮排之描述行。"""
    out: dict[str, dict] = {}
    cur = None
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^(SWE-RA-[^\s|]+)\s*\|\s*(.*)$", line.strip())
        if m:
            cur = m.group(1)
            out[cur] = {"title": m.group(2).strip(), "desc": ""}
            continue
        if cur and line.startswith(("    ", "\t")):
            out[cur]["desc"] = (out[cur]["desc"] + " " + line.strip()).strip()
    if not out:
        raise ContextError(f"{path} 未解析出任何 leaf")
    return out


def parse_leaf_sections(path: Path) -> dict[str, dict]:
    """`leaf  sections  #SYS-RA` 三欄，以空白分隔。"""
    out: dict[str, dict] = {}
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        parts = line.split()
        if len(parts) < 2 or not parts[0].startswith("SWE-RA-"):
            continue
        out[parts[0]] = {
            "sections": [s for s in parts[1].split(",") if s],
            "sysra_count": int(parts[2]) if len(parts) > 2 and parts[2].isdigit() else None,
        }
    if not out:
        raise ContextError(f"{path} 未解析出任何 leaf")
    return out


def spec_paragraphs(docx: Path) -> list[tuple[str | None, str]]:
    """回傳 [(章節號, 段落文字), …]，章節號為其前方最近之標題。"""
    xml = zipfile.ZipFile(docx).read("word/document.xml").decode("utf-8")
    HEAD = re.compile(r"^(\d+(?:\.\d+)*)\s+.*\{(\d+)\}$")
    out: list[tuple[str | None, str]] = []
    cur = None
    for p in re.findall(r"<w:p[ >].*?</w:p>", xml, flags=re.S):
        t = "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, flags=re.S))
        t = html.unescape(re.sub(r"<[^>]+>", "", t)).strip()
        if not t:
            continue
        m = HEAD.match(t)
        if m and "\t" not in t:
            cur = m.group(1)
            continue
        out.append((cur, t))
    return out


def build(feature_dir: Path, batch: str, leaves: list[str]) -> dict:
    data_dir = feature_dir / "data"
    desc = parse_leaf_descriptions(data_dir / "leaf_descriptions.txt")
    secs = parse_leaf_sections(data_dir / "leaf_to_section_probe.txt")
    if yaml is None:
        raise ContextError("PyYAML 不可用")
    cfg = yaml.safe_load((feature_dir / "feature.yaml").read_text(encoding="utf-8"))
    docx = feature_dir / cfg["paths"]["spec_pdf"]
    paras = spec_paragraphs(docx)

    missing = [l for l in leaves if l not in desc or l not in secs]
    if missing:
        raise ContextError(f"下列 leaf 於既有產物中缺席，停：{missing}")

    out = {"batch": batch, "leaves": []}
    for leaf in leaves:
        want = set(secs[leaf]["sections"])
        body = [t for sec, t in paras if sec in want]
        out["leaves"].append({
            "leaf": leaf,
            "title": desc[leaf]["title"],
            "description": desc[leaf]["desc"],
            "sections": secs[leaf]["sections"],
            "sysra_count": secs[leaf]["sysra_count"],
            "spec_paragraphs": body,
        })
    return out


def render(ctx: dict) -> str:
    lines = [f"# Batch {ctx['batch']} — 上下文", "",
             "> 本檔為既有產物之搬運，**不含任何本腳本產生之措辭**。", ""]
    for e in ctx["leaves"]:
        lines += [f"## {e['leaf']} — {e['title']}", "",
                  f"**Requirement Description**：{e['description']}", "",
                  f"**CFTS015 章節**：{', '.join(e['sections'])}"
                  f"（SYS-RA 引用 {e['sysra_count']}）", "",
                  f"**條文段落**（{len(e['spec_paragraphs'])} 段）：", ""]
        for t in e["spec_paragraphs"]:
            lines.append(f"- {t}")
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--feature-dir", required=True)
    ap.add_argument("--batch", required=True)
    ap.add_argument("--leaves", required=True,
                    help="逗號分隔之 leaf id")
    a = ap.parse_args()
    fd = Path(a.feature_dir)
    leaves = [x.strip() for x in a.leaves.split(",") if x.strip()]
    try:
        ctx = build(fd, a.batch, leaves)
    except ContextError as e:
        print(f"ContextError: {e}", file=sys.stderr)
        return 2
    md = fd / "data" / f"batch_context_{a.batch}.md"
    js = fd / "data" / f"batch_context_{a.batch}.json"
    md.write_text(render(ctx), encoding="utf-8")
    js.write_text(json.dumps(ctx, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"leaf {len(ctx['leaves'])} 條 → {md.name} / {js.name}")
    for e in ctx["leaves"]:
        print(f"  {e['leaf']:<26}章節 {len(e['sections'])}｜條文段落 {len(e['spec_paragraphs'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
