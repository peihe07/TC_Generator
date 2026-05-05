#!/usr/bin/env python3
"""
ASPICE SWE.6 TC Simplifier (OpenAI GPT-5.4)
============================================

Reads a Projection_tcw.json workspace export, runs every TC through
OpenAI GPT-5.4 to simplify procedure / ER / pre-conditions per
v2 §4.8 (step length tiers) and §5.5 (ER alignment), then writes
the modified rows back to the same JSON shape.

Usage
-----
    export OPENAI_API_KEY=sk-...
    python simplify_tcs.py input.json output.json [--limit 5] [--dry-run]

Outputs
-------
    output.json              -- workspace JSON with rows simplified
    output.audit.csv         -- per-TC decision log (rules cited, before/after)
    output.failed.csv        -- TCs that failed schema/lint checks (kept original)
"""

import argparse
import asyncio
import csv
import json
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from openai import AsyncOpenAI

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MODEL = "gpt-5"              # OpenAI model
CONCURRENCY = 5              # concurrent API calls
MAX_RETRIES = 2              # per-TC retries on schema/lint fail
MAX_TOKENS = 8000            # response budget per TC（含 gpt-5 reasoning tokens）
REASONING_EFFORT = "low"     # gpt-5 reasoning effort: minimal | low | medium | high

# Word-count thresholds (v2 §4.8)
MAX_NORMAL_STEP_WORDS = 12
MAX_FINAL_STEP_WORDS = 18
MAX_ER_LINE_WORDS = 18

# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """你是 ASPICE SWE.6 測試案例審查與精簡專家。任務: 在不改變測試邏輯的前提下, 精簡 TC 的 Pre-Condition / Test Procedure / Expected Result, 使其符合 v2 規則。

# 核心規則 (v2)

## §2.1 Pre-Condition
PC 是「狀態 / 環境」, 不是動作。禁止寫 'Press', 'Insert', 'Open' 等命令動詞 (但 'is open' 作為被動狀態描述合法)。

## §4.1 每個 Step 必須有明確目的
每步要讓測試者立刻回答「這一步是為了什麼」。不解釋背景, 不寫設計理由。

## §4.2 Final Step 必須觸發驗證目標
最後一步要直接觸發 Test Item 要驗證的行為, 並含 'check that ...' 意圖。

## §4.3 一步一動作
中間步驟禁止 'X and check Y' 複合句 (final step 可以)。中間步驟若有 baseline 確認, 可拆成兩步。

## §4.5 禁用模糊動詞
禁止: observe, observe whether, see if, check whether, confirm whether, verify (作主動詞)。
推薦: Check that, Confirm that, Read, Record, Compare。

## §4.8 步驟長度三層
- A 類一般步驟: ≤ 12 字, 動作 + 目標即可
- B 類 Final step: ≤ 18 字, 必含 check that 意圖
- C 類意圖必要 setup (UI 多用途/不透明目標): ≤ 18 字, 可加 to ... 子句
- 判別法: 「拿掉這個 to 子句, 下一步還能無歧義執行嗎」能 → 拿掉

## §5.1 ER 必須可觀察
不可使用 'normally', 'properly', 'successfully', 'correctly', 'as expected' 等 hedge 詞。
改寫為「具體 UI 顯示 / 數值 / 狀態變化」。

## §5.3 Step ↔ ER 1:1 對應
每個 Step 對應一個 ER, 順序一致。修改 step 數時, ER 同步調整。

## §5.5 多階段 ER
若 Procedure 含環境建立 + 主驗證, ER 用空行分隔兩階段。

# 你的任務

對給定的 TC, 輸出精簡後的版本。處理原則:

1. **砍解釋背景的子句**
   - "to start pairing" / "as baseline" / "before the projection started" → 多數可砍
   - 動作 + 目標物本身就清楚, 不需追加說明

2. **拆分一步多動作**
   - "Open X and check Y" → 拆成 "Open X" + "Check that Y"
   - "Display A, play B, open C" → 拆成三步
   - ER 同步拆分

3. **拆分過長 Final step**
   - 一個 final step 列舉 10 個檢查項 → 拆成多個 final-grade step
   - 每個拆出的 step 都要含 check that 意圖

4. **替換模糊動詞與 hedge 詞**
   - 'works normally' → 'works without error popup'
   - 'displays normally' → 'is displayed without rendering errors'
   - 'as baseline' (作為 ER 措辭) → 改成具體狀態描述
   - 'abnormal error pop-up' → 'connection failure pop-up' (具體類型)

5. **PC 動作違規**
   - 命令動詞 (Press / Insert / Open ...) → 移到 Procedure step 1
   - 'is open' / 'is connected' / 'is enabled' (被動狀態) → 保留
   - PC 不可有重複的系統預設 ('HU is powered on')

# 不可動的事

- **不增刪測試邏輯**: 步驟數可變, 但驗證點 (要驗的行為) 不變
- **不改 testItem / testSet / designMethod / priority**
- **不改變 Test Item 引用的需求對象**

# 輸出格式 (嚴格 JSON, 無前後綴文字)

{
  "tcId": "...",
  "needsRevision": true | false,
  "preservedLogic": true | false,
  "preConditionsAfter": "<新內容, 若無修改則填 null>",
  "stepsAfter": "<新內容, 必填>",
  "expectedResultsAfter": "<新內容, 必填>",
  "structuralChanges": ["說明改了什麼, 例: 拆分 step 1 為 1+2", "..."],
  "rulesApplied": ["§4.3", "§4.8", ...],
  "warnings": ["若 AI 不確定的地方"]
}

若 TC 已符合規則, 不需修改:
- needsRevision: false
- preConditionsAfter / stepsAfter / expectedResultsAfter: 全填 null
- structuralChanges: []

若判斷修改會改變測試邏輯而拒絕修改:
- needsRevision: false
- preservedLogic: true (不確定就不動 = 邏輯保留)
- warnings: ["說明為什麼不改"]"""


def build_user_message(tc: dict[str, Any]) -> str:
    """Build the per-TC user message."""
    return f"""## TC 待精簡

tcId: {tc['tcId']}
reqId: {tc.get('reqId', '')}
testGroup: {tc.get('testGroup', '')}
testSet: {tc.get('testSet', '')}

### Test Item (規格, 不可改)
{tc.get('testItem', '')}

### tcTitle (僅供參考, 不可改)
{tc.get('tcTitle', '')}

### Pre-Conditions
{tc.get('preConditions') or '(空)'}

### Test Procedure
{tc.get('steps') or '(空)'}

### Expected Result
{tc.get('expectedResults') or '(空)'}

### Validator 已標記的問題 (供參考, 自行判斷是否真實)
{format_validation_errors(tc.get('validationErrors') or [])}

請依規則精簡並輸出嚴格 JSON。"""


def format_validation_errors(errs: list[dict]) -> str:
    if not errs:
        return "(無)"
    lines = []
    for e in errs:
        if e.get('falsePositive'):
            lines.append(f"- [{e.get('column')}] (誤報) {e.get('message', '')}")
        else:
            lines.append(f"- [{e.get('column')}] {e.get('message', '')}")
    return '\n'.join(lines)


# ---------------------------------------------------------------------------
# Schema validation & lint
# ---------------------------------------------------------------------------

REQUIRED_KEYS = {
    "tcId", "needsRevision", "preservedLogic",
    "preConditionsAfter", "stepsAfter", "expectedResultsAfter",
    "structuralChanges", "rulesApplied", "warnings",
}

VAGUE_HEDGES = re.compile(
    r"\b(normally|properly|successfully|correctly|as expected)\b",
    re.IGNORECASE,
)

FORBIDDEN_VERBS_IN_STEP = re.compile(
    r"^\s*\d+\.\s*(observe|see if)\b",
    re.IGNORECASE,
)


@dataclass
class LintResult:
    ok: bool
    issues: list[str] = field(default_factory=list)


def lint_revised(steps: str, ers: str) -> LintResult:
    """Run rule-based lint on AI-revised content. Soft check; warnings only."""
    issues: list[str] = []

    if not steps or not ers:
        return LintResult(ok=False, issues=["empty steps or ER"])

    step_lines = [ln for ln in steps.split('\n') if re.match(r'^\s*\d+\.', ln)]
    er_lines = [ln for ln in ers.split('\n') if re.match(r'^\s*\d+\.', ln)]

    # Step ↔ ER 1:1
    if len(step_lines) != len(er_lines):
        issues.append(f"step count {len(step_lines)} != ER count {len(er_lines)} (§5.3)")

    # Forbidden verbs as main verb
    for ln in step_lines:
        if FORBIDDEN_VERBS_IN_STEP.match(ln):
            issues.append(f"forbidden main verb in step: {ln.strip()[:80]}")

    # Hedge words in ER
    for ln in er_lines:
        if VAGUE_HEDGES.search(ln):
            issues.append(f"vague hedge in ER: {ln.strip()[:80]}")

    # Final step must contain a check intent
    if step_lines:
        final = step_lines[-1].lower()
        if not re.search(r'\b(check that|confirm that|check the|read|record|compare|check whether)\b', final):
            issues.append(f"final step missing check intent: {step_lines[-1].strip()[:80]}")

    return LintResult(ok=not issues, issues=issues)


def schema_check(payload: dict) -> tuple[bool, str]:
    if not isinstance(payload, dict):
        return False, "not a dict"
    missing = REQUIRED_KEYS - set(payload.keys())
    if missing:
        return False, f"missing keys: {missing}"
    if not isinstance(payload.get('needsRevision'), bool):
        return False, "needsRevision not bool"
    if not isinstance(payload.get('preservedLogic'), bool):
        return False, "preservedLogic not bool"
    if payload['needsRevision']:
        if not payload.get('stepsAfter') or not payload.get('expectedResultsAfter'):
            return False, "needsRevision=true but stepsAfter/expectedResultsAfter empty"
    return True, ""


# ---------------------------------------------------------------------------
# JSON extraction (defensive)
# ---------------------------------------------------------------------------

def extract_json(raw: str) -> dict | None:
    """Extract the first JSON object from a possibly noisy text response."""
    # Try fenced code blocks first
    m = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', raw, re.DOTALL)
    if m:
        try:
            return json.loads(m.group(1))
        except json.JSONDecodeError:
            pass
    # Try direct parse
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        pass
    # Try greedy outermost braces
    start = raw.find('{')
    end = raw.rfind('}')
    if start >= 0 and end > start:
        try:
            return json.loads(raw[start:end + 1])
        except json.JSONDecodeError:
            return None
    return None


# ---------------------------------------------------------------------------
# Per-TC processing
# ---------------------------------------------------------------------------

@dataclass
class TCResult:
    tc_id: str
    ok: bool
    needs_revision: bool
    payload: dict | None = None
    lint: LintResult | None = None
    error: str = ""
    attempts: int = 0


async def process_tc(
    client: AsyncOpenAI,
    tc: dict,
    sem: asyncio.Semaphore,
) -> TCResult:
    """Send one TC to the model and validate the response."""
    async with sem:
        last_error = ""
        for attempt in range(1, MAX_RETRIES + 2):
            try:
                resp = await client.chat.completions.create(
                    model=MODEL,
                    max_completion_tokens=MAX_TOKENS,
                    reasoning_effort=REASONING_EFFORT,
                    response_format={"type": "json_object"},
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": build_user_message(tc)},
                    ],
                )

                raw = (resp.choices[0].message.content or "").strip()

                payload = extract_json(raw)
                if payload is None:
                    last_error = f"attempt {attempt}: failed to parse JSON"
                    continue

                ok, why = schema_check(payload)
                if not ok:
                    last_error = f"attempt {attempt}: schema fail ({why})"
                    continue

                # Lint check on revised content (only if AI claims revision)
                lint = LintResult(ok=True)
                if payload['needsRevision']:
                    lint = lint_revised(
                        payload.get('stepsAfter') or '',
                        payload.get('expectedResultsAfter') or '',
                    )

                return TCResult(
                    tc_id=tc['tcId'],
                    ok=True,
                    needs_revision=payload['needsRevision'],
                    payload=payload,
                    lint=lint,
                    attempts=attempt,
                )

            except Exception as exc:
                last_error = f"attempt {attempt}: {type(exc).__name__}: {exc}"
                await asyncio.sleep(1.5 * attempt)  # backoff

        return TCResult(
            tc_id=tc['tcId'],
            ok=False,
            needs_revision=False,
            error=last_error,
            attempts=MAX_RETRIES + 1,
        )


# ---------------------------------------------------------------------------
# Apply revisions back to JSON
# ---------------------------------------------------------------------------

def apply_revision(tc: dict, result: TCResult) -> str:
    """Mutate tc in place. Returns 'applied' / 'skipped' / 'failed' / 'lint_failed'."""
    if not result.ok:
        return "failed"

    if not result.needs_revision:
        return "skipped"

    payload = result.payload
    assert payload is not None

    # If lint failed and the issues are severe, keep original
    if result.lint and not result.lint.ok:
        # Soft acceptance: only block if step/ER count mismatch (data integrity)
        severe = any(
            "step count" in issue or "empty" in issue
            for issue in result.lint.issues
        )
        if severe:
            return "lint_failed"

    # Preserve originals
    tc['originalPreConditions'] = tc.get('preConditions')
    tc['originalSteps'] = tc.get('steps')
    tc['originalExpectedResults'] = tc.get('expectedResults')

    # Apply changes
    if payload.get('preConditionsAfter'):
        tc['preConditions'] = payload['preConditionsAfter']
    if payload.get('stepsAfter'):
        tc['steps'] = payload['stepsAfter']
    if payload.get('expectedResultsAfter'):
        tc['expectedResults'] = payload['expectedResultsAfter']

    # Audit metadata
    tc['aiSimplified'] = True
    tc['aiSimplificationMeta'] = {
        'rulesApplied': payload.get('rulesApplied') or [],
        'structuralChanges': payload.get('structuralChanges') or [],
        'warnings': payload.get('warnings') or [],
        'lintIssues': result.lint.issues if result.lint else [],
    }

    return "applied"


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------

async def run(input_path: Path, output_path: Path, limit: int | None, dry_run: bool):
    if dry_run:
        print(f"DRY RUN — no API calls, no output writes")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key and not dry_run:
        sys.exit("ERROR: OPENAI_API_KEY not set")

    client = AsyncOpenAI(api_key=api_key) if not dry_run else None

    print(f"Loading {input_path}...")
    with input_path.open(encoding='utf-8') as f:
        data = json.load(f)

    rows = data['workspace']['snapshot']['tcRows']
    targets = rows[:limit] if limit else rows
    print(f"Total rows: {len(rows)}, processing: {len(targets)}")

    if dry_run:
        # Just print first sample's user message
        print("\n--- Sample user message (first TC) ---")
        print(build_user_message(targets[0]))
        return

    sem = asyncio.Semaphore(CONCURRENCY)
    tasks = [process_tc(client, tc, sem) for tc in targets]

    results: list[TCResult] = []
    completed = 0
    for coro in asyncio.as_completed(tasks):
        r = await coro
        results.append(r)
        completed += 1
        status = "OK" if r.ok else "FAIL"
        rev = "rev" if r.needs_revision else "skip"
        print(f"[{completed:>4}/{len(targets)}] {r.tc_id} {status} {rev} (try {r.attempts})")

    # Map results to rows by tcId
    result_by_id = {r.tc_id: r for r in results}

    stats = {'applied': 0, 'skipped': 0, 'failed': 0, 'lint_failed': 0}
    audit_rows = []
    failed_rows = []

    for tc in targets:
        r = result_by_id.get(tc['tcId'])
        if not r:
            stats['failed'] += 1
            continue
        outcome = apply_revision(tc, r)
        stats[outcome] += 1

        if r.ok and r.payload:
            audit_rows.append({
                'tcId': tc['tcId'],
                'outcome': outcome,
                'needsRevision': r.needs_revision,
                'rulesApplied': '; '.join(r.payload.get('rulesApplied') or []),
                'structuralChanges': '; '.join(r.payload.get('structuralChanges') or []),
                'lintIssues': '; '.join(r.lint.issues) if r.lint else '',
                'warnings': '; '.join(r.payload.get('warnings') or []),
            })

        if not r.ok or outcome == 'lint_failed':
            failed_rows.append({
                'tcId': tc['tcId'],
                'outcome': outcome,
                'error': r.error,
                'lintIssues': '; '.join(r.lint.issues) if r.lint else '',
            })

    # Write output JSON
    print(f"\nWriting {output_path}...")
    with output_path.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write audit CSV
    audit_path = output_path.with_suffix('.audit.csv')
    if audit_rows:
        with audit_path.open('w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(audit_rows[0].keys()))
            w.writeheader()
            w.writerows(audit_rows)
        print(f"Audit log: {audit_path}")

    # Write failed CSV
    failed_path = output_path.with_suffix('.failed.csv')
    if failed_rows:
        with failed_path.open('w', encoding='utf-8', newline='') as f:
            w = csv.DictWriter(f, fieldnames=list(failed_rows[0].keys()))
            w.writeheader()
            w.writerows(failed_rows)
        print(f"Failed log: {failed_path}")

    print(f"\n=== Summary ===")
    for k, v in stats.items():
        print(f"  {k:12s}: {v}")
    print(f"  total       : {sum(stats.values())}")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('input', type=Path, help='input workspace JSON')
    ap.add_argument('output', type=Path, help='output JSON path')
    ap.add_argument('--limit', type=int, default=None,
                    help='process only first N rows (for testing)')
    ap.add_argument('--dry-run', action='store_true',
                    help='print first sample prompt without calling API')
    args = ap.parse_args()

    if not args.input.exists():
        sys.exit(f"ERROR: input not found: {args.input}")

    asyncio.run(run(args.input, args.output, args.limit, args.dry_run))


if __name__ == '__main__':
    main()
