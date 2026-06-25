"""Stage 2.5 — Pre-flight Budget Checkpoint (PIPELINE_DESIGN § Stage 2.5).

Estimates, before a run, whether a batch fits the current 5-hour interactive
window. The human reads remaining % from Claude Code `/usage` and passes it in;
`fit_batch` / `fit_mixed` size the batch with a safety headroom. No API calls,
zero usage — calibration and pre-flight read existing config or manual input.

Unit convention: all `*_pct` are fractions in 0.0..1.0. `remaining_pct=0.65`
means 65% of the window remains; `per_req_pct=0.012` means ~1.2% per requirement;
`safety=0.7` reserves 30% headroom.
"""
from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime, timezone

_DEFAULT_PATH = os.path.join("config", "budget.json")


@dataclass
class BudgetConfig:
    per_req_pct_light: float | None = None   # calibrated; fraction 0..1
    per_req_pct_deep: float | None = None
    safety: float = 0.7
    calibrated_at: str | None = None         # ISO timestamp


def load_budget(path: str = _DEFAULT_PATH) -> BudgetConfig:
    """Read config; return defaults when the file is absent."""
    if not os.path.isfile(path):
        return BudgetConfig()
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    return BudgetConfig(
        per_req_pct_light=data.get("per_req_pct_light"),
        per_req_pct_deep=data.get("per_req_pct_deep"),
        safety=data.get("safety", 0.7),
        calibrated_at=data.get("calibrated_at"),
    )


def save_budget(cfg: BudgetConfig, path: str = _DEFAULT_PATH) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(asdict(cfg), fh, ensure_ascii=False, indent=2)


def fit_batch(remaining_pct: float, per_req_pct: float, safety: float = 0.7) -> int:
    """How many requirements safely fit the current window, leaving headroom."""
    usable = max(0.0, remaining_pct - (1 - safety))
    if not per_req_pct or per_req_pct <= 0:
        return 0
    return int(usable // per_req_pct)


def fit_mixed(remaining_pct: float, n_light: int, n_deep: int,
              cfg: BudgetConfig) -> dict:
    """Mixed batch sizing weighted by calibrated light/deep per_req_pct.

    Returns {'fits', 'projected_pct', 'decision' ('go'|'shrink'|'wait'),
             'max_light', 'max_deep'}. Uncalibrated -> 'wait', no crash.
    """
    need_light = n_light > 0
    need_deep = n_deep > 0
    if (need_light and cfg.per_req_pct_light is None) or \
       (need_deep and cfg.per_req_pct_deep is None):
        return {
            "fits": False,
            "projected_pct": None,
            "decision": "wait",
            "max_light": 0,
            "max_deep": 0,
        }

    light = cfg.per_req_pct_light or 0.0
    deep = cfg.per_req_pct_deep or 0.0
    projected_pct = n_light * light + n_deep * deep
    headroom = remaining_pct - (1 - cfg.safety)
    fits = projected_pct <= headroom

    return {
        "fits": fits,
        "projected_pct": projected_pct,
        "decision": "go" if fits else "shrink",
        "max_light": fit_batch(remaining_pct, light, cfg.safety) if light else 0,
        "max_deep": fit_batch(remaining_pct, deep, cfg.safety) if deep else 0,
    }


def record_calibration(
    start_pct: float,
    end_pct: float,
    n_probe: int,
    regime: str,
    path: str = _DEFAULT_PATH,
) -> BudgetConfig:
    """Calibrate per_req_pct from a probe run: (start - end) / n_probe.

    regime: 'light' | 'deep'. Updates the matching field + calibrated_at, saves.
    """
    if n_probe <= 0:
        raise ValueError("n_probe must be positive")
    if regime not in ("light", "deep"):
        raise ValueError(f"regime must be 'light' or 'deep', got {regime!r}")

    cfg = load_budget(path)
    per_req_pct = (start_pct - end_pct) / n_probe
    if regime == "light":
        cfg.per_req_pct_light = per_req_pct
    else:
        cfg.per_req_pct_deep = per_req_pct
    cfg.calibrated_at = datetime.now(timezone.utc).isoformat()
    save_budget(cfg, path)
    return cfg
