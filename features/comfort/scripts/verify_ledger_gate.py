#!/usr/bin/env python3
"""Reverse-verification for the ledger gate (下放包 83 §1).

The gate replaced `shasum -c --ignore-missing`. What that flag hid was the
difference between "this file is not there" and "this file need not be
checked", so every case below is about that difference: absence has to be
DECLARED, a declaration has to be TRUE, and a file that merely moved has to
be verified where it now is — not excused.

Both directions, per 43 §3: each case builds a ledger that SHOULD fail (or,
for the last two, should pass) and asserts the gate says so. Nothing under
`features/comfort/` is read or written — the fixtures live in a temp dir.
"""

import hashlib
import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import write_back as wb                                        # noqa: E402

FAILED = 0


def check(name: str, passed: bool, note: str = "") -> None:
    global FAILED
    if not passed:
        FAILED += 1
    print(f"  {'PASS' if passed else '**FAIL**'} — {name}"
          + (f": {note}" if note else ""))


def digest(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def run(tmp: Path, body: str) -> tuple:
    """Point the gate at a fixture tree and run it."""
    led = tmp / "DELIVERY.sha256"
    led.write_text(body, encoding="utf-8")
    real, wb.FEATURE = wb.FEATURE, tmp
    try:
        return wb.check_ledger(led)
    finally:
        wb.FEATURE = real


def main() -> int:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        (tmp / "output" / "archive").mkdir(parents=True)
        f = tmp / "output" / "a.xlsx"
        f.write_bytes(b"one")
        d = digest(f)
        row = f"{d}  output/a.xlsx"

        ok, ver, absent, probs = run(tmp, row + "\n")
        check("a present, matching row passes", ok and ver == 1 and not absent,
              f"verified {ver}")

        f.write_bytes(b"two")
        ok, ver, absent, probs = run(tmp, row + "\n")
        check("a CHANGED file fails (the digest is checked, not the name)",
              not ok and any("MISMATCH" in p for p in probs), str(probs))
        f.write_bytes(b"one")

        # --- direction 1: missing and undeclared -> FAIL --------------------
        f.unlink()
        ok, ver, absent, probs = run(tmp, row + "\n")
        check("a MISSING file with no declaration fails — this is exactly what "
              "--ignore-missing used to swallow",
              not ok and any("MISSING (not declared)" in p for p in probs),
              str(probs))

        # --- declared absent -> passes, and is counted separately -----------
        decl = row + "\n# absent: output/a.xlsx  —— 測試用\n"
        ok, ver, absent, probs = run(tmp, decl)
        check("a MISSING file that is declared absent passes and is counted "
              "apart from the verified ones", ok and absent == 1 and ver == 0,
              f"verified {ver}, absent {absent}")

        # --- direction 2: declared absent but present -> FAIL ---------------
        f.write_bytes(b"one")
        ok, ver, absent, probs = run(tmp, decl)
        check("a file declared absent that IS present fails — the declaration "
              "is a claim about the world, not a permit",
              not ok and any("PRESENT" in p for p in probs), str(probs))

        # --- a declaration with no row -> FAIL ------------------------------
        ok, ver, absent, probs = run(
            tmp, row + "\n# absent: output/ghost.xlsx  —— 測試用\n")
        check("a declaration naming no ledger row fails (a dangling permit)",
              not ok and any("no ledger row" in p for p in probs), str(probs))

        # --- archived: verified at the new path, not excused ----------------
        shutil.move(str(f), str(tmp / "output" / "archive" / "a.xlsx"))
        moved = row + "\n#   archived : output/archive/a.xlsx  （測試用）\n"
        ok, ver, absent, probs = run(tmp, moved)
        check("a moved file is VERIFIED at its archived path, and counts as "
              "verified rather than absent", ok and ver == 1 and absent == 0,
              f"verified {ver}, absent {absent}")

        (tmp / "output" / "archive" / "a.xlsx").write_bytes(b"tampered")
        ok, ver, absent, probs = run(tmp, moved)
        check("a moved file whose archived bytes changed fails — moving does "
              "not stop the digest being checked",
              not ok and any("MISMATCH at archived path" in p for p in probs),
              str(probs))

        (tmp / "output" / "archive" / "a.xlsx").unlink()
        ok, ver, absent, probs = run(tmp, moved)
        check("an archived path that does not exist fails",
              not ok and any("archived path missing" in p for p in probs),
              str(probs))

    # --- the real ledger, for the record ------------------------------------
    ok, ver, absent, probs = wb.check_ledger(wb.FEATURE / "DELIVERY.sha256")
    check("the real DELIVERY.sha256 passes", ok,
          f"verified {ver}, declared absent {absent}, problems {probs}")

    print(f"\n{'all directional cases PASS' if not FAILED else f'**{FAILED} case(s) FAILED**'}")
    return 1 if FAILED else 0


if __name__ == "__main__":
    sys.exit(main())
