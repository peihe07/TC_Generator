#!/usr/bin/env python3
"""針對 lint_failed 的少數 TC 用更強 reasoning_effort + 明確 1:1 提示重跑。

用法:
    python retry_failed.py Projection_simplified.json TC_ID [TC_ID ...]
就地修改傳入的 simplified JSON。
"""
import asyncio
import json
import sys
from pathlib import Path

import simplify_tcs as base
from openai import AsyncOpenAI


EXTRA_HARD_RULE = """

# 額外硬性要求 (這次 retry 觸發)
你上次修訂這筆 TC 時把 step 拆/併動作但沒同步調整 ER, 違反 §5.3。
**這次嚴格要求**:
- stepsAfter 的編號 step 數量 **必須** 等於 expectedResultsAfter 的編號 ER 數量
- 拆 step 時 ER 同步拆; 併 step 時 ER 同步併
- 輸出前自行數一次 step / ER 數量, 不一致就重新調整再輸出
"""


async def main():
    if len(sys.argv) < 3:
        sys.exit("usage: retry_failed.py <simplified.json> <tcId> [<tcId>...]")

    json_path = Path(sys.argv[1])
    target_ids = set(sys.argv[2:])

    with json_path.open(encoding="utf-8") as f:
        data = json.load(f)

    rows = data["workspace"]["snapshot"]["tcRows"]
    targets = [r for r in rows if r["tcId"] in target_ids]
    if not targets:
        sys.exit(f"找不到任何 tcId in {target_ids}")
    print(f"重跑 {len(targets)} 筆: {[t['tcId'] for t in targets]}")

    # 切到更強的 reasoning_effort 並注入硬性提示
    base.REASONING_EFFORT = "medium"
    base.MAX_TOKENS = 12000
    original_system = base.SYSTEM_PROMPT
    base.SYSTEM_PROMPT = original_system + EXTRA_HARD_RULE

    client = AsyncOpenAI()
    sem = asyncio.Semaphore(2)

    results = await asyncio.gather(*[base.process_tc(client, tc, sem) for tc in targets])

    applied, still_failed = 0, 0
    for tc, r in zip(targets, results):
        outcome = base.apply_revision(tc, r)
        print(f"[{tc['tcId']}] {outcome}  rules={r.payload.get('rulesApplied') if r.payload else '-'}  lint={r.lint.issues if r.lint else '-'}")
        if outcome == "applied":
            applied += 1
        else:
            still_failed += 1

    with json_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n=== Retry summary ===  applied={applied}  still_failed={still_failed}")


if __name__ == "__main__":
    asyncio.run(main())
