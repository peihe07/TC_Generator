"""Semantic confirmation of bucket-② SPEC coverage (LLM, gpt-4.1).

Bucket ② = PC rules with a token content-match to some requirement but NO
explicit SWRA citation — i.e. uncertain. A single batched LLM call judges, per
PC rule, whether its behaviour is genuinely covered by any of the 94 SWE1
requirements (wording may differ; semantics decide). Confident gaps from
bucket ③ are merged in to produce the final SPEC-only gap list.

Run: python M1/spec_coverage_verify.py
Output: M1/spec_coverage_gaps_final.json + console summary.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "backend"))
from req_tracer import load_swe1_reqs  # noqa: E402


def _load_key() -> str:
    for line in (ROOT / ".env").read_text().splitlines():
        if line.startswith("OPENAI_API_KEY"):
            return line.split("=", 1)[1].strip()
    return os.environ["OPENAI_API_KEY"]


def main() -> None:
    rows = json.loads((ROOT / "M1/spec_coverage_player.json").read_text(encoding="utf-8"))
    bucket2 = [r for r in rows if not r["cited_by"] and r["req_covered"]]
    bucket3 = [r for r in rows if not r["req_covered"]]  # confident gaps
    reqs = load_swe1_reqs(str(ROOT / "M1/swe1_pla_reqs.json"))

    req_lines = "\n".join(
        f"{r['id']}: {r.get('title','')} — {(r.get('desc') or '')[:160]}" for r in reqs
    )
    pc_lines = "\n".join(f"{r['pc']}: {r['text']}" for r in bucket2)

    system = (
        "你是 ASPICE SWE.6 測試覆蓋稽核員。我會給你一組 SPEC 行為(Media HMI PC 規則)"
        "與完整的 SWE1 需求清單。對每一條 PC 規則,判斷『該 PC 描述的行為是否被任何一條"
        "需求實質涵蓋』。措辭不同沒關係,以語意為準;只有當某需求確實描述了該行為才算 covered。"
        "回 JSON:{\"results\":[{\"pc\":\"PCx.y\",\"covered\":true|false,"
        "\"req_id\":\"覆蓋它的需求 id 或 null\",\"reason\":\"一句中文理由\"}]}"
    )
    user = f"=== SWE1 需求清單(94)===\n{req_lines}\n\n=== 待判定 PC 規則({len(bucket2)})===\n{pc_lines}"

    from openai import OpenAI
    client = OpenAI(api_key=_load_key())
    resp = client.chat.completions.create(
        model="gpt-4.1",
        temperature=0,
        response_format={"type": "json_object"},
        messages=[{"role": "system", "content": system},
                  {"role": "user", "content": user}],
    )
    data = json.loads(resp.choices[0].message.content)
    verdicts = {v["pc"]: v for v in data.get("results", [])}

    confirmed_gaps = [v for v in verdicts.values() if not v.get("covered")]
    confirmed_cov = [v for v in verdicts.values() if v.get("covered")]

    # Final gap list = bucket③ (confident) + bucket② judged not-covered
    final = []
    text_by_pc = {r["pc"]: r["text"] for r in rows}
    for r in bucket3:
        final.append({"pc": r["pc"], "text": r["text"], "source": "bucket3 (no cite/no content)"})
    for v in confirmed_gaps:
        final.append({"pc": v["pc"], "text": text_by_pc.get(v["pc"], ""),
                      "source": "bucket2 LLM-confirmed gap", "reason": v.get("reason")})

    (ROOT / "M1/spec_coverage_gaps_final.json").write_text(
        json.dumps({"final_gaps": final, "bucket2_verdicts": list(verdicts.values())},
                   ensure_ascii=False, indent=2), encoding="utf-8")

    total = len(rows)
    print(f"桶② 共 {len(bucket2)} 條 → LLM 判定:覆蓋 {len(confirmed_cov)}、缺口 {len(confirmed_gaps)}")
    print(f"桶③ 確定缺口 {len(bucket3)} 條")
    print(f"\n最終 SPEC-only 缺口總數: {len(final)} / {total} "
          f"(= 真實 SPEC 覆蓋 {(total-len(final))/total:.0%})")
    print(f"usage: in={resp.usage.prompt_tokens} out={resp.usage.completion_tokens}")
    print("\n=== 桶② 被 LLM 確認為缺口的(擇要)===")
    for v in confirmed_gaps[:12]:
        print(f"  [{v['pc']}] {v.get('reason','')[:70]}")
    print("\n=== 桶② 被 LLM 確認『其實有覆蓋』的(濾掉,擇要)===")
    for v in confirmed_cov[:10]:
        print(f"  [{v['pc']}] ← {v.get('req_id')}: {v.get('reason','')[:55]}")


if __name__ == "__main__":
    main()
