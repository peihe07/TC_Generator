"""W-VF62 之自檢 —— **依 R-VF69 以逐字禁止串表述**，不以概念表述。

R-VF69 逐字：「凡自檢項涉及禁止之內容者，須以逐字串或逐 pattern 表述」；
「一個無法被機械執行之自檢項，其通過與未做不可分辨」。

  ✗ 「Pre-Condition 無系統預設」
  ✓ 「Pre-Condition 不得含下列 pattern：`powered`／`power on`／…」
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]

# ── 逐字 pattern（R-VF69）────────────────────────────────────────────
# **降為輔助**（R-VF70，V25 改寫後）：其命中即已知之違規形態，可加速定位，
# **惟通過黑名單不等於通過白名單** —— 判準為 WHITELIST 之歸類。
# 以下為已知集合，非全集。pattern 攔已知之表述，
# pilot 之人讀補未知者；**二者缺一，則列舉之不完整無人發現**。
# 新發現之表述即時補入並具名其發現輪次。
#   V24 輪：powered／power on／start-up／reachable／by default 等
PRE_FORBIDDEN = [r"\bpowered\b", r"\bpower(?:ed)? on\b", r"\bstart-?up\b",
                 r"\bbooted\b", r"\bignition on\b", r"\bpower cycle\b"]
# 已知集合，非全集 —— 同上（輔助性質）。
#   V24 輪：observe whether／observe／see if 等
VERB_FORBIDDEN = [r"\bobserve whether\b", r"\bobserve\b", r"\bsee if\b",
                  r"\bcheck whether\b", r"\bconfirm whether\b",
                  r"\bverify\b", r"\bwatch\b", r"\bmonitor\b", r"\binspect\b"]
TITLE_MIN, TITLE_MAX = 2, 14

# --- R-VF70（V25 改寫後）：允許型別之**白名單** ---
# canon §4.4 之四類。**不可歸類者一律報違規**，非「命中禁止串者報違規」。
# 白名單之完整性由 canon 之條文本身保證；黑名單之完整性無檢查可管。
WHITELIST = {
    "外部環境": [r"\bvehicle is (parked|stationary|moving)\b", r"\bambient\b",
                 r"\btemperature\b", r"\bignition\b", r"\bengine\b"],
    "硬體周邊": [r"\bconnected\b", r"\binstalled\b", r"\bpresent\b",
                 r"\btrailer\b", r"\bdevice\b"],
    "功能初始狀態": [r"\bFull-Operation state\b", r"\bis in the .+ state\b",
                     r"\bmenu is (open|displayed)\b", r"\bsetting is set to\b"],
    "系統版本或模式": [r"\bPROXI \$", r"\bconfiguration\b", r"\bmode\b",
                       r"\bsoftware version\b", r"\bvariant\b"],
}


def classify(line: str):
    """回其所屬之 canon §4.4 類別；不可歸類者回 None（即違規）。"""
    body = re.sub(r"^\d+\.\s*", "", line).strip()
    # PROXI 行**一律**歸「系統版本或模式」—— 其為配置之設定。
    # 首版依序比對，致 `PROXI $X$ is set to "Present"` 之值 `Present`
    # 命中「硬體周邊」之 `\bpresent\b` 而誤歸。**值不得決定其類別。**
    if re.match(r"^PROXI \$", body):
        return "系統版本或模式"
    for cat, pats in WHITELIST.items():
        for p in pats:
            if re.search(p, body, re.I):
                return cat
    return None


def check(tcs: list[dict]) -> list[str]:
    e = []
    for t in tcs:
        tid = f"seq {t['seq']}"
        for p in PRE_FORBIDDEN:
            if re.search(p, t["pre_conditions"], re.I):
                e.append(f"§4.4 {tid}: pre_conditions 命中禁止 pattern `{p}`")
        for p in VERB_FORBIDDEN:
            if re.search(p, t["test_procedure"], re.I):
                e.append(f"§5.1 {tid}: procedure 命中禁用動詞 pattern `{p}`")
        # R-VF70（V25 改寫後）：`pre_conditions` 以**白名單**判 ——
        # 每項須可歸入 canon §4.4 之四類，不可歸類者報違規。
        for j, ln in enumerate(
                [x for x in t["pre_conditions"].split("\n") if x.strip()], 1):
            if classify(ln) is None:
                e.append(f"§R-VF70 {tid}: pre_conditions 第 {j} 項不可歸入 "
                         f"canon §4.4 之四類 —— `{re.sub(r'^[0-9]+[.] *', '', ln.strip())[:56]}`")
        n = len(t["tc_title"].split())
        if not TITLE_MIN <= n <= TITLE_MAX:
            e.append(f"§4.3 {tid}: tc_title {n} 字，逾 {TITLE_MIN}–{TITLE_MAX}")
        # §6 之 1:1
        ns = len([x for x in t["test_procedure"].split("\n") if x.strip()])
        ne = len([x for x in t["expected_result"].split("\n") if x.strip()])
        if ns != ne:
            e.append(f"§6 {tid}: procedure {ns} 步 vs ER {ne} 步")
    # 檔頭計數（Note 1）
    return e


def main() -> int:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else FEAT / "generated/vf230_pilot1_v3.json"
    d = json.loads(path.read_text(encoding="utf-8"))
    import collections
    cnt = collections.Counter(t["priority_class"] for t in d["tcs"])
    e = check(d["tcs"])
    for k, v in cnt.items():
        if f"{k} {v}" not in d["selection"]:
            e.append(f"§5a 檔頭: `selection` 之 {k} 與逐條實測 {v} 不符")
    print(f"{path.name} —— {len(d['tcs'])} 條，違規 **{len(e)}**")
    for x in e:
        print("   ", x)
    return 0 if not e else 1


if __name__ == "__main__":
    raise SystemExit(main())
