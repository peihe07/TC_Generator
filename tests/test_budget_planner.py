"""Stage 2.5 — budget planner tests. Pure math / IO; no API."""
import pytest

from budget_planner import (
    BudgetConfig,
    fit_batch,
    fit_mixed,
    load_budget,
    record_calibration,
)


def test_fit_batch_basic():
    # usable = remaining - (1 - safety) = 0.65 - 0.30 = ~0.35, floored by per_req.
    # NB: float floor-division per the spec formula -> 34 (0.35//0.01 == 34.0).
    assert fit_batch(0.65, 0.01, safety=0.7) == 34
    # usable ~0.35 / 0.012 = 29.16 -> 29.
    assert fit_batch(0.65, 0.012, safety=0.7) == 29
    # Clean case (binary-exact per_req): full window, no reserve.
    assert fit_batch(1.0, 0.25, safety=1.0) == 4


def test_fit_batch_below_margin_zero():
    # remaining at/under the headroom reserve -> nothing fits.
    assert fit_batch(0.30, 0.01, safety=0.7) == 0
    assert fit_batch(0.20, 0.01, safety=0.7) == 0
    # zero / missing per_req_pct must not divide by zero.
    assert fit_batch(0.9, 0.0, safety=0.7) == 0


def test_fit_mixed_weighted():
    cfg = BudgetConfig(per_req_pct_light=0.005, per_req_pct_deep=0.02, safety=0.7)
    # projected = 10*0.005 + 5*0.02 = 0.05 + 0.10 = 0.15; headroom = 0.8-0.3 = 0.5.
    result = fit_mixed(0.8, n_light=10, n_deep=5, cfg=cfg)
    assert result["projected_pct"] == pytest.approx(0.15)
    assert result["fits"] is True
    assert result["decision"] == "go"

    # Overcommit -> shrink with suggested single-regime caps.
    over = fit_mixed(0.35, n_light=40, n_deep=20, cfg=cfg)
    assert over["fits"] is False
    assert over["decision"] == "shrink"
    assert over["max_deep"] == fit_batch(0.35, 0.02, 0.7)


def test_fit_mixed_uncalibrated_waits():
    cfg = BudgetConfig(per_req_pct_light=None, per_req_pct_deep=None)
    result = fit_mixed(0.9, n_light=10, n_deep=5, cfg=cfg)
    assert result["decision"] == "wait"
    assert result["projected_pct"] is None
    assert result["fits"] is False  # does not crash


def test_record_calibration_roundtrip(tmp_path):
    path = str(tmp_path / "budget.json")
    # per_req_pct = (1.0 - 0.88) / 10 = 0.012 for deep.
    cfg = record_calibration(1.0, 0.88, 10, "deep", path=path)
    assert cfg.per_req_pct_deep == pytest.approx(0.012)
    assert cfg.calibrated_at is not None

    reloaded = load_budget(path)
    assert reloaded.per_req_pct_deep == pytest.approx(0.012)
    assert reloaded.per_req_pct_light is None  # other regime untouched

    # Invalid regime / probe count are rejected loudly.
    with pytest.raises(ValueError):
        record_calibration(1.0, 0.9, 0, "deep", path=path)
    with pytest.raises(ValueError):
        record_calibration(1.0, 0.9, 5, "medium", path=path)


def test_incremental_skips_done_rows():
    # Regression lock: incremental mode regenerates only rows without a tc_id,
    # so a truncated window resumes without re-spending on completed work.
    from main import _filter_rows

    rows = [
        {"row_num": 1, "req_id": "R1", "tc_id": "P-G-001"},  # done
        {"row_num": 2, "req_id": "R2"},                       # pending
        {"row_num": 3, "req_id": "R3", "tc_id": ""},          # pending (blank)
    ]
    remaining = _filter_rows(rows, "incremental", None)
    assert [r["row_num"] for r in remaining] == [2, 3]
