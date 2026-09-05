#!/usr/bin/env python3
"""批次 manifest 之 prompt／exemplar 指紋（R-G58）。

R-G58 令每批之 manifest 記錄本批**實際使用**之 prompt 模板 sha256 與
exemplar 集 sha256；與前批不符而下放包未宣告變更者，該批退回。

**「模板」在本專案不是單一檔案。** TC 之生成受四類輸入拘束：
canon（IN）、feature profile、prompt 建構程式、以及 exemplar 集。
四者任一變動皆會改變產出，故指紋取**其聯集**，且**逐源列出** ——
只給一個總 sha 可偵測漂移而不可歸因，逐源列出方能指出**哪一源變了**。

**來源之解析順序**：
1. `feature.yaml` 之 `fingerprint.prompt_sources` / `fingerprint.exemplar_sources`
   （相對 repo 根；feature 得自訂）
2. 未宣告者用慣例預設（見 `DEFAULT_PROMPT_SOURCES`）

**缺檔不靜默**（G-D）：解析得到而檔案不存在者，以 `sha256 = null`
與 `missing = true` 入清單，**不從清單中消失**。一個少了兩個來源的
指紋與一個完整的指紋，其總 sha 都是 64 個十六進位字元 ——
**兩者長得一樣，故缺席必須寫在紙上。**

**向後相容**：本模組只**新增**鍵，不改既有 manifest 之任何鍵；
舊 manifest 無此鍵者讀取端不得報錯（`compare()` 以 `None` 視為「未記錄」，
與「記錄了而不同」分列）。
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:                                    # pragma: no cover
    yaml = None

# 慣例預設 —— feature 未於 feature.yaml 宣告時採用
DEFAULT_PROMPT_SOURCES = [
    "docs/runtime/ASPICE_SWE6_AI_Instruction.md",      # IN canon：撰寫規則
    "backend/prompt_builder.py",                       # prompt 之建構程式
]
PROFILE_DIR = "docs/runtime/profiles"


def sha256_of(path: Path) -> str | None:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def source_entry(root: Path, rel: str) -> dict:
    sha = sha256_of(root / rel)
    return {"path": rel, "sha256": sha, "sha8": sha[:8] if sha else None,
            "missing": sha is None}


def set_sha(entries: list[dict]) -> str:
    """來源集之總 sha：逐源 `path:sha256` 排序後接合再取 sha256。

    **缺檔以字面 `null` 參與雜湊** —— 缺檔本身是集合之一項性質，
    不是集合之缺項；少一個檔應改變總 sha，而非讓總 sha 悄悄等於少一項時之值。
    """
    body = "\n".join(f"{e['path']}:{e['sha256'] or 'null'}"
                     for e in sorted(entries, key=lambda x: x["path"]))
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def feature_cfg(root: Path, feature_dir: str) -> dict:
    p = root / feature_dir / "feature.yaml"
    if yaml is None or not p.exists():
        return {}
    return yaml.safe_load(p.read_text(encoding="utf-8")) or {}


def profile_sources(cfg: dict) -> list[str]:
    """feature 之 profile 檔（其 `[OVERRIDE §x]` 段直接改變書寫規則）。"""
    name = cfg.get("profile_file")
    if name:
        return [f"{PROFILE_DIR}/{name}"]
    feat = (cfg.get("feature") or "").replace(" ", "")
    if not feat:
        return []
    guess = f"{PROFILE_DIR}/FW036_R1L_{feat}_Profile.md"
    return [guess]


def resolve(root: Path, feature_dir: str) -> tuple[list[str], list[str], str]:
    """回傳 (prompt 來源, exemplar 來源, 解析方式)。"""
    cfg = feature_cfg(root, feature_dir)
    fp = cfg.get("fingerprint") or {}
    if fp.get("prompt_sources"):
        return list(fp["prompt_sources"]), list(fp.get("exemplar_sources") or []), "feature.yaml"
    prompts = list(DEFAULT_PROMPT_SOURCES) + profile_sources(cfg)
    exemplars = [f"{feature_dir}/data/exemplars.json"]
    return prompts, exemplars, "convention"


def fingerprint(root: Path, feature_dir: str) -> dict:
    prompts, exemplars, how = resolve(root, feature_dir)
    p_entries = [source_entry(root, r) for r in prompts]
    e_entries = [source_entry(root, r) for r in exemplars]
    return {
        "resolved_by": how,
        "prompt_template": {
            "sha256": set_sha(p_entries),
            "sha8": set_sha(p_entries)[:8],
            "sources": p_entries,
            "missing": [e["path"] for e in p_entries if e["missing"]],
        },
        "exemplar_set": {
            "sha256": set_sha(e_entries),
            "sha8": set_sha(e_entries)[:8],
            "sources": e_entries,
            "missing": [e["path"] for e in e_entries if e["missing"]],
        },
    }


def compare(prev: dict | None, cur: dict) -> dict:
    """與前批比對。**「未記錄」與「記錄了而不同」分列**（向後相容）。"""
    out = {}
    for key in ("prompt_template", "exemplar_set"):
        old = (prev or {}).get(key, {}).get("sha256")
        new = cur[key]["sha256"]
        if old is None:
            out[key] = {"verdict": "未記錄", "prev": None, "cur": new, "changed_sources": []}
            continue
        if old == new:
            out[key] = {"verdict": "相符", "prev": old, "cur": new, "changed_sources": []}
            continue
        prev_map = {e["path"]: e["sha256"] for e in (prev or {}).get(key, {}).get("sources", [])}
        cur_map = {e["path"]: e["sha256"] for e in cur[key]["sources"]}
        changed = sorted(set(prev_map) | set(cur_map))
        out[key] = {
            "verdict": "**不符**", "prev": old, "cur": new,
            "changed_sources": [p for p in changed if prev_map.get(p) != cur_map.get(p)],
        }
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="prompt／exemplar 指紋（R-G58）")
    ap.add_argument("--root", default=".")
    ap.add_argument("--feature-dir", required=True, help="例：features/vehicle_setting")
    ap.add_argument("--manifest", default=None, help="寫入該 manifest（新增鍵，不改既有鍵）")
    ap.add_argument("--against", default=None, help="與該 manifest 之指紋比對")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    fp = fingerprint(root, args.feature_dir)
    print(json.dumps(fp, ensure_ascii=False, indent=1))

    if args.against:
        prev = json.loads((root / args.against).read_text(encoding="utf-8"))
        result = compare(prev.get("fingerprint"), fp)
        print("\n--- 與前批比對 ---")
        for k, v in result.items():
            print(f"  {k}: {v['verdict']}"
                  + (f"  變動源 {v['changed_sources']}" if v["changed_sources"] else ""))
        if any(v["verdict"] == "**不符**" for v in result.values()):
            print("\nR-G19：與前批不符而下放包未宣告變更者，該批退回。", file=sys.stderr)
            return 1

    if args.manifest:
        mp = root / args.manifest
        data = json.loads(mp.read_text(encoding="utf-8"))
        data["fingerprint"] = fp                      # 只新增，不動既有鍵
        mp.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"\n寫入 {args.manifest} 之 `fingerprint` 鍵")
    return 0


if __name__ == "__main__":
    sys.exit(main())
