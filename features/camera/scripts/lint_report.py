"""批次之 `LINT_REPORT.md` 重生（`lint036.render_report` 之薄封裝）。

    python3 features/camera/scripts/lint_report.py <暫存目錄> <批次目錄>
"""
import sys, warnings
from pathlib import Path
import openpyxl  # noqa: F401  （lint_batch 之組簿需之）
warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import lint036 as L                      # noqa: E402

SP, GEN = Path(sys.argv[1]), Path(sys.argv[2])
xlsx = SP / f"{GEN.name}_lint.xlsx"
if not xlsx.exists():
    raise SystemExit(f"{xlsx} 不存在 —— 先跑 lint_batch.py")
res = L.lint_workbook(xlsx, profile="camera")
md = L.render_report(xlsx, res, L.DEFAULT_LENGTH_LIMIT, "camera")
n = len(list(GEN.glob("NR1L-*.json")))
# 來源行改寫為出處說明 —— 不把 session 之絕對路徑寫進 repo
md = md.replace(
    f"- 來源：`{xlsx}`（唯讀）",
    f"- 來源：`{xlsx.name}`（唯讀）—— **lint 專用暫存簿**，由本目錄之 {n} 份 json\n"
    "  以母本第 9 列欄序組成，落於 session scratchpad，**未寫回任何交付工作簿**。\n"
    "  組簿工具 `features/camera/scripts/lint_batch.py`", 1)
(GEN / "LINT_REPORT.md").write_text(md, encoding="utf-8")
print(f"{GEN/'LINT_REPORT.md'}｜counts:",
      {k: n for k, n in L.count_by_check(res, "camera").items() if n})
