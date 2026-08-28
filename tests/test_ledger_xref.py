"""`scripts/ledger_xref.py`（包內台帳引用對照）之單元測試。

**G-N —— 缺陷原文以字面釘入，不以當前語料為案例。**
下方 `RULINGS_DEFECT` 逐字重現 A-POP9(1) 之實況：分析層落 R-POP12 時
轉抄了上繳包摘要而未 live 查 `ANOMALIES.md`，把 `-002-02 不拆` 這條
掛到了 **A-POP6**（其實屬 A-POP7）。repo 內 popup 之台帳日後如何改寫、
該條後來如何更正，都不影響本組測試之證明力。
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import ledger_xref as lx  # noqa: E402

# 缺陷原文（下放包 03 §一逐字所述之形態）
RULINGS_DEFECT = """# RULINGS

### R-POP12 — -002-02 不拆，軸不存在（分析層裁 [DEFAULT]，2026-08-27，**A-POP6**）

SWE1-POP-002-02 **不拆** device 軸。
"""

# 更正後（handoff 03 §一：已更正為 A-POP7）
RULINGS_FIXED = RULINGS_DEFECT.replace("A-POP6", "A-POP7")

ANOM = """# ANOMALIES

| A | 內容 | 狀態 | Tier |
|---|---|---|---|
| A-POP6 | R-POP10 新規使既有台帳浮現新命中 | **RESOLVED（R-POP16）** | Tier 2 |
| A-POP7 | `-002-02` 之 device 軸無 hard-button 實例 | **RESOLVED（R-POP12）** | Tier 2 |

## A-POP6 —— 甲

內文。

## A-POP7 —— 乙

內文。
"""

DR = """# DATA REQUESTS

| DR | 項目 | 狀態 |
|---|---|---|
| DR-POP1 | 甲 | RESOLVED |
"""


def build(tmp_path: Path, rulings: str = RULINGS_FIXED, anom: str = ANOM,
          dr: str = DR, handoff: str | None = None) -> Path:
    base = tmp_path / "features/popup"
    (base / "docs/handoff").mkdir(parents=True, exist_ok=True)
    (base / "docs/upstream").mkdir(parents=True, exist_ok=True)
    (base / "RULINGS.md").write_text(rulings, encoding="utf-8")
    (base / "ANOMALIES.md").write_text(anom, encoding="utf-8")
    (base / "DATA_REQUESTS.md").write_text(dr, encoding="utf-8")
    if handoff is not None:
        (base / "docs/handoff/03.md").write_text(handoff, encoding="utf-8")
    return tmp_path


def checks(findings) -> list[str]:
    return [f.check for f in findings]


# --- pairing：A-POP9(1) 之固定案例 -------------------------------------------


def test_條文標題掛錯_anomaly_即回報(tmp_path: Path) -> None:
    """缺陷向：R-POP12 掛 A-POP6，而 A-POP6 之台帳列載 R-POP16。"""
    found, _, _ = lx.check(build(tmp_path, rulings=RULINGS_DEFECT), "popup")
    pairing = [f for f in found if f.check == "pairing"]
    assert len(pairing) == 1
    assert "R-POP12" in pairing[0].detail and "A-POP6" in pairing[0].detail
    assert "R-POP16" in pairing[0].detail


def test_更正後同一支檢查須沉默(tmp_path: Path) -> None:
    """回歸向（G-N）：同一 fixture 改掛 A-POP7 後，pairing 不得再命中。"""
    found, _, _ = lx.check(build(tmp_path), "popup")
    assert [f for f in found if f.check == "pairing"] == []


def test_台帳未載處分條號者不對照(tmp_path: Path) -> None:
    """無從對照即不報 —— 判準要能說出自己在哪裡不適用。"""
    anom = ANOM.replace("**RESOLVED（R-POP16）**", "PENDING")
    found, _, _ = lx.check(build(tmp_path, rulings=RULINGS_DEFECT, anom=anom),
                           "popup")
    assert [f for f in found if f.check == "pairing"] == []


# --- unknown_id ---------------------------------------------------------------


def test_包內引用不存在之號即回報(tmp_path: Path) -> None:
    root = build(tmp_path, handoff="本包處分 A-POP42。\n")
    found, _, _ = lx.check(root, "popup")
    unknown = [f for f in found if f.check == "unknown_id"]
    assert len(unknown) == 1 and "A-POP42" in unknown[0].detail


def test_實存之號不回報(tmp_path: Path) -> None:
    root = build(tmp_path, handoff="本包處分 A-POP6 與 DR-POP1。\n")
    found, _, _ = lx.check(root, "popup")
    assert [f for f in found if f.check == "unknown_id"] == []


def test_他_feature_之號只報數不對照(tmp_path: Path) -> None:
    """R-POP16 甲：單一擁有者原則 —— 別人的台帳不由本 feature 判。"""
    root = build(tmp_path, handoff="甲類清單：A-SX18、A-SX19、DR-AM7、A-TM2。\n")
    found, stats, _ = lx.check(root, "popup")
    assert [f for f in found if f.check == "unknown_id"] == []
    assert stats["foreign"] == 4


# --- ledger_shape -------------------------------------------------------------


def test_採明細節體例之台帳缺節即回報(tmp_path: Path) -> None:
    anom = ANOM.replace("## A-POP7 —— 乙\n\n內文。\n", "")
    found, _, _ = lx.check(build(tmp_path, anom=anom), "popup")
    shape = [f for f in found if f.check == "ledger_shape"]
    assert [f.where for f in shape] == ["A-POP7"]


def test_純表格體例之台帳不被要求明細節(tmp_path: Path) -> None:
    """R-POP16 丙：不強制統一版面 —— DATA_REQUESTS 無節不算違規。"""
    found, _, _ = lx.check(build(tmp_path), "popup")
    assert [f for f in found if f.where.startswith("DR-")] == []


def test_有明細節而主表無列亦回報(tmp_path: Path) -> None:
    """反向：摘要 live 產是自主表產的，只有節而無列即抓不到它。"""
    anom = ANOM + "\n## A-POP8 —— 丙\n\n內文。\n"
    found, _, _ = lx.check(build(tmp_path, anom=anom), "popup")
    assert [(f.check, f.where) for f in found if f.where == "A-POP8"] == [
        ("ledger_shape", "A-POP8")]
