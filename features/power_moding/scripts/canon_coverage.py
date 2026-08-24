#!/usr/bin/env python3
"""R-PMH56 —— lint 之「未涵蓋 canon 節號」清單由**程式自節號全集產生**。

不得以人工回想列舉：13 包所具名之九節漏列七節，而漏列使「已具名」
產生虛假之完整感（14 包 §5.4）。

實施：以 canon 之節標題產生節號全集，減去 `lint_batch.py` 之
`COVERED` 常數（該常數為 lint 各檢查所宣告之涵蓋節號），差集即為清單。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANON = ROOT.parent.parent / "docs" / "runtime" / "ASPICE_SWE6_AI_Instruction.md"

# `lint_batch.py` 各檢查所涵蓋之 canon 節號 —— **由該檔匯入，不另維護副本**
# （R-PMH40 之同一原則）。
sys.path.insert(0, str(ROOT / "scripts"))
from lint_batch import COVERED  # noqa: E402

HEAD = re.compile(r"^#{2,4}\s+(\d+(?:\.\d+)*)\.?\s+(.+)$")
# 15 包步驟 5 —— **抽取式判準本身之盲區**：`HEAD` 只收「數字編號」之標題，
# 凡非數字編號者（`## Appendix` 之類）自始不入母體，**其未被檢查一事
# 亦不會出現於未涵蓋清單**。故另列全部 `^#{2,4}` 標題並扣除已抽取者，
# 差集逐項具名。**只回報，不改判準**（判準改動須另立條文）。
# 反向檢查之範圍取 `#{1,6}` 而非 `#{2,4}` —— **反向檢查若沿用同一層級範圍，
# 則層級本身之盲區（H1／H5+）仍照不到**。實測：H1 = 0、H5 = 1
# （`##### 沿革（R-TM13…）`，屬條文沿革註記而非規則節）。
ANYHEAD = re.compile(r"^(#{1,6})\s+(.+)$")


def sections() -> list[tuple[str, str]]:
    out = []
    for line in CANON.read_text(encoding="utf-8").splitlines():
        m = HEAD.match(line)
        if m:
            out.append((m.group(1), m.group(2).strip()))
    return out


def unextracted() -> list[tuple[str, str]]:
    """全部 `^#{2,4}` 標題減去 `HEAD` 所抽取者 —— 抽取式判準之盲區清單。"""
    out = []
    for line in CANON.read_text(encoding="utf-8").splitlines():
        m = ANYHEAD.match(line)
        if m and not HEAD.match(line):
            out.append((m.group(1), m.group(2).strip()))
    return out


def uncovered() -> tuple[list, list, list]:
    secs = sections()
    all_ids = [s for s, _ in secs]
    titles = dict(secs)
    unknown = [c for c in COVERED if c not in titles]
    # 已涵蓋者含其子節（`§5.1` 涵蓋 `5.1`，不自動涵蓋 `5.2`）
    unc = [(s, titles[s]) for s in all_ids if s not in COVERED]
    return secs, unc, unknown


def main() -> None:
    secs, unc, unknown = uncovered()
    print(f"canon：`{CANON.relative_to(ROOT.parent.parent)}`")
    print(f"節號全集 = **{len(secs)}**；lint 宣告涵蓋 = **{len(COVERED)}**；"
          f"**未涵蓋 = {len(unc)}**")
    if unknown:
        print(f"\n⚠ lint 宣告涵蓋但 canon 無此節號：{unknown}  ← 須查明")
    print("\n=== 未涵蓋之 canon 節號（R-PMH56，程式產生）===")
    for s, t in unc:
        print(f"  §{s:<8} {t[:70]}")

    ux = unextracted()
    print(f"\n=== 抽取判準之盲區：無數字編號之標題 = {len(ux)}（15 包步驟 5）===")
    print("  下列標題不具數字節號，**自始不入節號全集**，"
          "故其未被 lint 檢查一事不會出現於上方清單。")
    for lvl, t in ux:
        print(f"  {lvl:<4} {t[:70]}")
    print("  **只回報，不改判準** —— 是否納入母體屬判準之變更，須另立條文。")
    sys.exit(1 if unknown else 0)


if __name__ == "__main__":
    main()
