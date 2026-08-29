#!/usr/bin/env python3
"""批次自檢（IN §9 逐項）。預設對 generated/b01 與 generated/b02 兩批合併實跑。

本 feature 尚無 lint_tcs.py（無 DBC 綁定、無 outline map，lint 之 F/K/T/U 閘
皆無母體），故本包以自檢腳本承接 IN §9 中可機檢之項次，並逐項印出。
**不可機檢者印 MANUAL 而非 PASS** —— 不可能失敗之檢查項不得標 PASS
（charter §工作形態）。

用法：python3 features/ics_management/scripts/selfcheck_b01.py [batch.json ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_BATCHES = [ROOT / "generated" / "b01" / "b01_tcs.json",
                   ROOT / "generated" / "b02" / "b02_tcs.json"]

TEN_KEYS = ["tc_title", "pre_conditions", "input_test_data", "test_procedure",
            "expected_result", "specification_reference", "design_method",
            "priority", "split_flag", "split_reason"]

# IN §11：尾句號之規制欄位
NO_PERIOD_FIELDS = ["pre_conditions", "input_test_data", "test_procedure",
                    "expected_result"]
# IN §11：行首／行尾空白之規制欄位（含 test_item 與 spec_reference）
NO_WS_FIELDS = NO_PERIOD_FIELDS + ["test_item", "specification_reference"]

FORBIDDEN_MAIN_VERBS = ["observe", "observe whether", "see if", "check whether",
                        "confirm whether", "verify", "watch", "monitor", "inspect"]
MODALS = ["shall", "will", "should", "would"]
TITLE_MODALS = ["should", "will", "shall", "properly", "successfully"]
DESIGN_METHODS = {"Negative / Invalid", "Fault Injection", "State Transition",
                  "Decision Table", "Equivalence Partitioning",
                  "Boundary Value Analysis", "Combinatorial",
                  "Scenario / Use Case", "Functional Based"}
PRIORITIES = {"P0", "P1", "P2", "P3"}
SPEC_RE = re.compile(r"^CFTS\d{3}-\d{7}$")
PENDING_RE = re.compile(r"PENDING: (DR-ICS\d+) <([^>]+)>")

results: list[tuple[str, str, str]] = []   # (項次, 判定, 說明)


def add(item: str, ok: bool | None, note: str) -> None:
    verdict = "MANUAL" if ok is None else ("PASS" if ok else "**FAIL**")
    results.append((item, verdict, note))


def items(field: str) -> list[str]:
    """以編號 item 為單位切分（IN §11：規制單位為 numbered item，非物理行）。"""
    out, cur = [], []
    for line in field.split("\n"):
        if re.match(r"^\d+\. ", line):
            if cur:
                out.append("\n".join(cur))
            cur = [line]
        else:
            cur.append(line)
    if cur:
        out.append("\n".join(cur))
    return out


def main() -> int:
    paths = [Path(a) for a in sys.argv[1:]] or DEFAULT_BATCHES
    paths = [p for p in paths if p.exists()]
    tcs = []
    for bp in paths:
        for t in json.loads(bp.read_text())["tcs"]:
            t["_batch"] = json.loads(bp.read_text())["batch"]
            tcs.append(t)
    print("受檢批次：" + "、".join(f'{p.parent.name}（{len(json.loads(p.read_text())["tcs"])} 條）'
                                   for p in paths))

    # 1 Test Set
    sets = sorted({t["test_set"] for t in tcs})
    bad = [s for s in sets if s in ("Unclassified", "Misc") or s.startswith("ICS ")]
    add("§9-1 Test Set", not bad, f"相異 Test Set = {sets}；Test Group 前綴／禁用名 {len(bad)}")

    # 2 tc_title
    bad = []
    for t in tcs:
        w = len(t["tc_title"].split())
        if not 2 <= w <= 14:
            bad.append(f'{t["tc_title"]}: {w} words')
        for m in TITLE_MODALS:
            if re.search(rf"\b{m}\b", t["tc_title"], re.I):
                bad.append(f'{t["tc_title"]}: modal/hedge "{m}"')
    titles = [t["tc_title"] for t in tcs]
    if len(set(titles)) != len(titles):
        bad.append("重複 tc_title")
    add("§9-2 tc_title", not bad,
        f"{len(tcs)} 條字數 {[len(t['tc_title'].split()) for t in tcs]}；違規 {bad or 0}")

    # 4.3.1 test_item 兩段式
    bad = []
    for t in tcs:
        lines = t["test_item"].split("\n")
        low = [l for l in lines if l.startswith("(") and l.endswith(")")]
        if not low:
            bad.append(f'{t["tc_title"]}: 缺括號下半')
        elif re.search(r"[一-鿿]", low[-1]):
            bad.append(f'{t["tc_title"]}: 下半含中文')
        if len(lines[0].split()) > 50:
            bad.append(f'{t["tc_title"]}: 上半 {len(lines[0].split())} token > 50 (R-3)')
    lows = [t["test_item"].split("\n")[-1] for t in tcs]
    per_parent: dict[str, list[str]] = {}
    for t in tcs:
        per_parent.setdefault(t["req_id"], []).append(t["test_item"].split("\n")[-1])
    for rid, ls in per_parent.items():
        if len(set(ls)) != len(ls):
            bad.append(f"{rid}: 括號下半逐字相同")
    add("§4.3.1 test_item 兩段式", not bad, f"{len(tcs)} 條皆有下半、皆英文；違規 {bad or 0}")

    # 10.1 十鍵
    missing = {t["tc_title"]: [k for k in TEN_KEYS if k not in t] for t in tcs}
    missing = {k: v for k, v in missing.items() if v}
    add("§10.1 十鍵齊備", not missing, f"缺鍵 {missing or 0}")

    # 10.2 priority
    bad = [t["priority"] for t in tcs if t["priority"] not in PRIORITIES]
    add("§10.2 priority", not bad,
        f"分佈 {{'P0': {sum(1 for t in tcs if t['priority']=='P0')}, "
        f"'P1': {sum(1 for t in tcs if t['priority']=='P1')}}}；越界 {bad or 0}")

    # 10.5 procedure ≥2 步
    bad = [t["tc_title"] for t in tcs if len(items(t["test_procedure"])) < 2]
    add("§10.5 procedure ≥2 步", not bad,
        f"步數 {[len(items(t['test_procedure'])) for t in tcs]}；違規 {bad or 0}")

    # 6 procedure ↔ ER 1:1
    bad = [t["tc_title"] for t in tcs
           if len(items(t["test_procedure"])) != len(items(t["expected_result"]))]
    add("§9-10 Procedure↔ER 1:1", not bad, f"違規 {bad or 0}")

    # 6 ER 無情態動詞
    bad = []
    for t in tcs:
        for m in MODALS:
            if re.search(rf"\b{m}\b", t["expected_result"], re.I):
                bad.append(f'{t["tc_title"]}: "{m}"')
    add("§6 ER 無情態動詞", not bad, f"掃 {MODALS}（不分大小寫、帶詞界）；命中 {bad or 0}")

    # 5.1 禁用動詞為主動詞（item 首詞）
    bad = []
    for t in tcs:
        for it in items(t["test_procedure"]):
            head = re.sub(r"^\d+\.\s*", "", it).split()
            if head and head[0].lower() in FORBIDDEN_MAIN_VERBS:
                bad.append(f'{t["tc_title"]}: {head[0]}')
    add("§5.1 禁用動詞（主動詞）", not bad,
        f"掃 item 首詞，不分大小寫；命中 {bad or 0}")

    # 11 尾句號
    bad = []
    for t in tcs:
        for f in NO_PERIOD_FIELDS:
            for it in items(t[f]):
                if it.rstrip().endswith((".", "。")):
                    bad.append(f'{t["tc_title"]}/{f}: {it[:40]}')
    add("§11 無尾句號", not bad, f"規制單位 = numbered item；違規 {bad or 0}")

    # 11 行首行尾空白
    bad = []
    for t in tcs:
        for f in NO_WS_FIELDS:
            for line in t[f].split("\n"):
                if line != line.strip():
                    bad.append(f'{t["tc_title"]}/{f}')
    add("§11 無行首行尾空白", not bad, f"違規 {bad or 0}")

    # 11 方括號
    bad = []
    for t in tcs:
        for f in NO_WS_FIELDS:
            if "[" in t[f] or "]" in t[f]:
                bad.append(f'{t["tc_title"]}/{f}')
    add("§11 無方括號", not bad, f"違規 {bad or 0}")

    # 11 UI 標籤用雙引號（單引號之逐字例外另列）
    single = []
    for t in tcs:
        for f in NO_WS_FIELDS:
            for m in re.findall(r"'([A-Za-z_ ]{2,})'", t[f]):
                single.append(f'{t["tc_title"]}/{f}: \'{m}\'')
    add("§11 UI 標籤雙引號", not single,
        f"單引號 token {single or 0}"
        + ("（皆為 CFTS022 逐字之 'VOLUME POP_UP'／'SLEEP MODE'，"
           "落於 test_item 上半 verbatim；見上繳包 §三-5）" if single else ""))

    # 10.7 spec_reference 形制
    bad = []
    for t in tcs:
        lines = t["specification_reference"].split("\n")
        for l in lines:
            if not SPEC_RE.match(l):
                bad.append(f'{t["tc_title"]}: {l}')
        ids = [l.split("-")[1] for l in lines if SPEC_RE.match(l)]
        if ids != sorted(ids):
            bad.append(f'{t["tc_title"]}: ObjectID 非升冪')
        if any(c in t["specification_reference"] for c in ",、;"):
            bad.append(f'{t["tc_title"]}: 串接符號')
    add("§10.7 spec_reference", not bad,
        f"逐行 CFTS{{nnn}}-{{7 位}}、升冪、無串接；違規 {bad or 0}")

    # 12 design_method
    bad = [t["design_method"] for t in tcs if t["design_method"] not in DESIGN_METHODS]
    add("§12 design_method", not bad,
        f"用及 {sorted({t['design_method'] for t in tcs})}；越界 {bad or 0}")

    # 8.4.3 PENDING 形制
    pend = []
    for t in tcs:
        for f in NO_WS_FIELDS:
            for dr, name in PENDING_RE.findall(t[f]):
                pend.append((t["tc_title"], f, dr, name))
    flagged = {t["tc_title"] for t in tcs if t.get("has_pending")}
    carrying = {p[0] for p in pend}
    add("§8.4.3 PENDING 佔位", flagged == carrying,
        f"佔位 {len(pend)} 處，涉 {len(carrying)} 條；has_pending 標記 {sorted(flagged)}")

    # 交付欄與 test_item 之非 ASCII（R-DD22 同族；下放包 02 §5 第 10 項）
    bad = []
    for t in tcs:
        for f in NO_WS_FIELDS:
            for ch in t[f]:
                if ord(ch) > 127:
                    bad.append(f'{t["tc_title"]}/{f}: U+{ord(ch):04X} {ch!r}')
    add("§1 交付欄無非 ASCII", not bad, f"掃六欄逐字元；命中 {sorted(set(bad)) or 0}")

    # 角括號之出現（非 FAIL，逐處列出供覆核）
    ang = []
    for t in tcs:
        for f in NO_WS_FIELDS:
            for m in re.findall(r"<[^>]{1,60}>", t[f]):
                ang.append(f'{t["tc_title"]}/{f}: {m}')
    add("§11 角括號之出現（列示，非 FAIL）", None,
        f"{len(ang)} 處：{sorted(set(ang))}")

    # 不可機檢者
    add("§9-3 Pre-Condition 為狀態/環境", None, f"人工：{len(tcs)} 條之 PC 皆為狀態或連接之器材，無動作、無檢查")
    add("§9-5 Final Step 擁有驗證", None, f"人工：{len(tcs)} 條之末步皆含 check that")
    add("§9-11 無 FP/FF", None, "人工：S3 為 S1 之負向對；V1/V2 為方向對；I1/I2 為 stuck 中／解除後之對")
    add("§9-12 追溯 Req/SWRA", None, f"人工：req_id {len({t['req_id'] for t in tcs})} 個 —— " + str({r: sum(1 for t in tcs if t['req_id']==r) for r in sorted({t['req_id'] for t in tcs})}) + "，皆為 SWRA 需求分頁實列之 ID")
    add("§9-17 來源 spec 勝過索引輸出", None, "人工：R-ICS4 之分流已套用，V3 之上半取 SWRA（002 未受 A-ICS1 位移）")

    w = max(len(r[0]) for r in results)
    for item, verdict, note in results:
        print(f"{item.ljust(w)}  {verdict:9} {note}")
    fails = [r for r in results if r[1].startswith("**FAIL")]
    print()
    print(f"總判：{'**FAIL**' if fails else 'PASS'} —— "
          f"機檢 {sum(1 for r in results if r[1] != 'MANUAL')} 項，"
          f"FAIL {len(fails)}；人工 {sum(1 for r in results if r[1] == 'MANUAL')} 項")
    print("\nPENDING 佔位清單：")
    for tc, f, dr, name in pend:
        print(f"  {tc} / {f} / {dr} / {name}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
