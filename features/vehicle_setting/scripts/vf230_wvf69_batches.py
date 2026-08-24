"""VF230 量產第 1 組：batch 1–3（W-VF69 §5）。

seq 268–417，50 條／批，依 R-VS58 選池序。
書寫式**全數取自 pilot #1 v4／pilot #2 之已核可模板**，不新創形態。

**不臆造之三道關**：
  1. 事實抽不出者不生成（`vf230_wvf69_facts.py`，逐條具名其缺何項）
  2. 標題套不進 canon §4.3 之 2–14 字者不生成（逐式試，皆不合即棄）
  3. `test_item` 取條文**逐字子字串**，不改寫（A-VS161 之教訓）
"""
import csv
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(FEAT / "scripts"))
import vf230_wvf45_priority as PR      # noqa: E402
import vf230_wvf61_pilot as P1         # noqa: E402
import vf230_wvf69_facts as FACTS      # noqa: E402

EP = "等價劃分 (Equivalence Partitioning, EP)"
FULLOP = "The HU is in the Full-Operation state"
BUS = "FD-CAN8 is connected to the bus simulator with signal tracing enabled"
MENU = "Open the Vehicle Settings menu and wait until it is fully rendered"
SEQ0, PER_BATCH, N_BATCH = 268, 50, 3


def n(xs: list[str]) -> str:
    return "\n".join(f"{i}. {x}" for i, x in enumerate(xs, 1))


def pick_title(cands: list[str]) -> str | None:
    """canon §4.3：2–14 字。逐式試，取首個合者；皆不合則 None。"""
    return next((t for t in cands if 2 <= len(t.split()) <= 14), None)


# 管路句 —— 其主語為 Android／VHAL 之中介層，不述需求之觸發或結果。
# **只刪句、不改字**（A-VS161：不得改其文字）。
PLUMBING = re.compile(
    r"^\s*(?:CarPropertyService|CarPropertyManager|The Vehicle HAL|Vehicle HAL|VHAL"
    r"|VehicleConfigManager|VehicleConfigService|SystemProperties"
    r"|The response shall be returned|The configuration response shall be returned"
    r"|HW supplier shall process|The HMI layer shall send a request to)", re.I)


def clause_tail(text: str, anchor: re.Pattern) -> str:
    """自條文取 test_item —— **逐句挑選，句內逐字**。

    首版取「自結論句之錨至文末」，而多數條文之錨即第一句，
    遂 117／150 退為條文全文（中位數 698 字元，含實作層管路）。
    改為逐句挑：刪主語為中介層之管路句，其餘**逐字保留**。
    一句都不剩者退為全文（其數逐輪回報）。
    """
    sents = re.split(r"(?<=\.)\s+", text.strip())
    keep = [x for x in sents if x.strip() and not PLUMBING.match(x)]
    return " ".join(keep).strip() if keep else text.strip()


# ---- 條文自身矛盾之偵測（A-VF18 之同型，依 V23 §4.2 處置）----
# `chooses to enable …` 而其值為 Off／`chooses to disable …` 而其值為 Enable。
# **以結論句為準，於 Remarks 具名其不一致與 DR 編號，不自行調和。**
POLAR_ON = {"on", "enable", "enabled", "enableled", "enableledchime",
            "present", "true", "requested"}
POLAR_OFF = {"off", "disable", "disabled", "notenable", "zero", "absent",
             "false", "notrequest"}
CHOOSE_VERB = re.compile(r"chooses to (enable|disable)\b", re.I)


def polarity(label: str) -> str | None:
    k = re.sub(r"[^a-z0-9]", "", label.lower())
    return "ON" if k in POLAR_ON else ("OFF" if k in POLAR_OFF else None)


def contradiction_remark(text: str, label: str) -> str:
    """條文之動作動詞與其值極性相反者，回其具名文字；否則回空字串。"""
    m = CHOOSE_VERB.search(text)
    if not m:
        return ""
    want = "ON" if m.group(1).lower() == "enable" else "OFF"
    got = polarity(label)
    if not got or got == want:
        return ""
    return (f"⚠ **條文自身不一致**：其動作句為 `chooses to {m.group(1)}`，"
            f"而其 `value` 與結論句皆為 `{label}`（極性相反）。"
            "依 **V23 §4.2**（A-VF18 之處置）**以結論句為準**，本條驗 "
            f"`{label}`；**不自行調和二者**。已開 **DR-38**。")


SENT_PROXI = re.compile(r"(If [A-Za-z0-9_ ()/]+?=\s*\[|When the HMI receives the value)")
SENT_SIG = re.compile(r"(When the customer chooses|The HMI layer shall capture"
                      r"|HW supplier shall|The HW supplier shall|When the LTM or ETM)")


def build(f: dict, seq: int, wr: dict, refs: dict, lv: dict) -> tuple[dict | None, str]:
    S, form = f["setting"], f["form"]
    w = wr[f["leaf_id"]]
    ref = refs.get(lv[f["leaf_id"]]["src_ref"], "")
    if not ref:
        return None, "spec_reference 未由 R-VF68 之錨鏈解出"

    if form == "PROXI 型":
        p, v, neg = f["param"], f["value"], f["negative"]
        item = clause_tail(f["text"], SENT_PROXI)
        pre = [FULLOP, f'PROXI ${p}$ is set to "{v}"']
        if neg:
            title = pick_title([
                f'{S} is not displayed when {p} is "{v}"',
                f'{S} is not displayed when the PROXI value is "{v}"',
                f'{S} is not displayed'])
            proc = ["Power cycle the HU", MENU,
                    f'Read the Vehicle Settings menu and check that the "{S}" '
                    "customer setting is not displayed"]
            er = ["The HU completes start-up", "The Vehicle Settings menu is displayed",
                  f'The "{S}" customer setting is not displayed']
        else:
            title = pick_title([
                f'{S} is displayed and modifiable when {p} is "{v}"',
                f'{S} is displayed and modifiable when the PROXI value is "{v}"',
                f'{S} is displayed and modifiable'])
            proc = ["Power cycle the HU", MENU,
                    f'Read the Vehicle Settings menu and check that the "{S}" '
                    "customer setting is displayed",
                    f'Select the "{S}" customer setting and check that its value '
                    "can be changed"]
            er = ["The HU completes start-up", "The Vehicle Settings menu is displayed",
                  f'The "{S}" customer setting is displayed',
                  f'The value of the "{S}" customer setting can be changed']
        remark = ""
        vsrc, reason = "0-CLAUSE", (
            f"值域來源 **0-CLAUSE**（R-VF13／R-VF60）—— 條文逐字帶出 `{v}`。"
            f"PROXI 參數名取條文逐字（R-VF78 二）。")

    elif form == "訊號送出型":
        msg, sig, raw, lab = f["msg"], f["sig"], f["raw"], f["label"]
        oth = f["other_label"]
        item = clause_tail(f["text"], SENT_SIG)
        title = pick_title([
            f"{msg}.{sig} is sent as {raw} ({lab}) when {S} is {lab}",
            f"{msg}.{sig} is sent as {raw} ({lab})",
            f"{sig} is sent as {raw} ({lab})"])
        pre = [FULLOP, BUS, f'The "{S}" customer setting is set to {oth}']
        proc = [MENU,
                f'Set the "{S}" customer setting to {lab} and check that '
                f"{msg}.{sig} = {raw} ({lab}) is transmitted",
                f'Read the Vehicle Settings menu and check that the {S} setting '
                f"is displayed as {lab}"]
        er = ["The Vehicle Settings menu is displayed",
              f"{msg}.{sig} = {raw} ({lab}) is sent",
              f"The {S} setting is displayed as {lab}"]
        remark = contradiction_remark(f["text"], lab)
        vsrc, reason = "2-DBC", (
            f"值域來源 **2-DBC**（R-VF13）—— `{sig}` 之 `VAL_` 內 raw {raw} = `{lab}`"
            + ("；條文逐字指名該值。" if f["value_named"] else
               "；**條文未指名值**，取 DBC 值域之最大 raw 為被驗分區，"
               f"其對偶分區 raw {f['other_raw']} = `{oth}` 置於前置。"))

    elif form == "訊號上行型":
        msg, sig, raw, lab = f["msg"], f["sig"], f["raw"], f["label"]
        oraw, olab = f["other_raw"], f["other_label"]
        item = clause_tail(f["text"], SENT_SIG)
        title = pick_title([
            f"{S} is displayed as {lab} when {sig} is {raw} ({lab})",
            f"{S} is displayed as {lab}",
            f"{sig} = {raw} ({lab}) updates the {S} setting"])
        pre = [FULLOP, BUS, "The Vehicle Settings menu is open"]
        proc = [f"Send CAN: {msg}.{sig} = {oraw} ({olab})",
                f"Send CAN: {msg}.{sig} = {raw} ({lab})",
                f'Read the Vehicle Settings menu and check that the {S} setting '
                f"is displayed as {lab}"]
        er = [f"{msg}.{sig} = {oraw} ({olab}) is sent",
              f"{msg}.{sig} = {raw} ({lab}) is sent",
              f"The {S} setting is displayed as {lab}"]
        remark = contradiction_remark(f["text"], lab)
        vsrc, reason = "2-DBC", (
            f"值域來源 **2-DBC** —— `{sig}` 之 `VAL_` 內 raw {raw} = `{lab}`"
            + ("；條文逐字指名該值。" if f["value_named"] else
               "；**條文未指名值**，取 DBC 值域之最大 raw 為被驗分區，"
               f"其對偶 raw {oraw} = `{olab}` 置於 procedure 第 1 步。"))

    elif form == "設定顯示與修改型":
        item = f["text"]
        title = pick_title([
            f"{S} customer setting is displayed and modifiable on the LTM screen",
            f"{S} customer setting is displayed and modifiable",
            f"{S} is displayed and modifiable"])
        pre = [FULLOP]
        proc = [MENU,
                f'Read the Vehicle Settings menu and check that the "{S}" customer '
                "setting is displayed",
                f'Select the "{S}" customer setting and check that its options '
                "are displayed",
                f'Select an option other than the current one and check that the '
                f'"{S}" customer setting is changed to the selected option']
        er = ["The Vehicle Settings menu is displayed",
              f'The "{S}" customer setting is displayed',
              f'The options of the "{S}" customer setting are displayed',
              f'The "{S}" customer setting is changed to the selected option']
        remark = ""
        vsrc, reason = "", (
            "本條無訊號亦無 PROXI，值域來源欄留白（非未查，而是條文本無值）。"
            "書寫式沿用 pilot #1 v4 之正向式（W-VF68 §2.1 第 3 項之回退，已核可）。")
    else:
        return None, f"形態 `{form}` 無模板"

    if not title:
        return None, f"標題逐式皆逾 canon §4.3 之 2–14 字（設定名 `{S}`）"

    title3 = lv[f["leaf_id"]]["title"].replace("\\n", " ")
    text = re.sub(r"\s+", " ", lv[f["leaf_id"]]["desc"])
    if title3 in PR.P0A:
        pri, cls = "P0", "P0(a)"
    elif title3 in PR.P0_SAFETY:
        pri, cls = "P0", "P0(c)"
    elif title3 in PR.P1_SAFETY_PRESENTATION:
        pri, cls = "P1", "P1"
    elif PR.P2_PAT.search(text):
        pri, cls = "P2", "P2"
    else:
        pri, cls = "P1", "P1"

    pending = "PENDING" in (w.get("value_source") or "")
    if pending:
        pre[1] = pre[1] + " (PENDING: DR-34)"

    return {
        "leaf_id": f["leaf_id"], "seq": seq, "test_set": w["test_set"],
        "layer3": title3, "tc_title": title, "test_item": item,
        "pre_conditions": n(pre), "input_test_data": "NA",
        "test_procedure": n(proc), "expected_result": n(er),
        "specification_reference": ref, "priority": pri, "priority_class": cls,
        "design_method": EP, "writable": w["writable"],
        "dr_dependent": "DR-34" if pending else "",
        "remarks": remark, "value_source": vsrc, "clause_form": form,
        "reasoning": reason,
    }, ""


def main() -> None:
    facts, skipped = FACTS.load_all()
    wr = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/vf230_writability.tsv").open(encoding="utf-8"),
        delimiter="\t")}
    lv = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t")}
    refs = P1.spec_refs()

    tcs, rejected, seq = [], [], SEQ0
    for f in facts:
        if len(tcs) >= PER_BATCH * N_BATCH:
            break
        t, why = build(f, seq, wr, refs, lv)
        if t is None:
            rejected.append({"leaf_id": f["leaf_id"], "form": f["form"], "why": why})
            continue
        tcs.append(t)
        seq += 1

    from collections import Counter
    print(f"生成 {len(tcs)} 條，seq {SEQ0}–{seq - 1}")
    print(f"  事實抽不出而跳過（母體 574 中）：{len(skipped)}")
    print(f"  模板套不上而跳過：{len(rejected)}")
    for r in rejected:
        print(f"    {r['leaf_id'][:44]:46} {r['why']}")

    for i in range(N_BATCH):
        part = tcs[i * PER_BATCH:(i + 1) * PER_BATCH]
        dist = Counter(t["priority_class"] for t in part)
        forms = Counter(t["clause_form"] for t in part)
        doc = {
            "batch": f"vf230_batch{i + 1:02d}", "line": "VF230",
            "feature": "vehicle_setting / VF230", "test_group": "Vehicle Setting",
            "handoff": "docs/handoff/V29_production_start.md"
                       "（sha256 ff86f0c6242f6ac2…，7015 bytes）",
            "work_order": "W-VF69",
            "selection": "R-VS58 選池序，量產母體 574（620 − pilot 20 − 隔離 26，"
                         "R-VF77 二）。事實抽不出者跳過並具名。"
                         "priority 分布（逐條實測）："
                         + "；".join(f"{k} {v}" for k, v in sorted(dist.items())) + "。",
            "form_distribution": dict(forms),
            "signal_notation": 'R-1 v2／R-VS52：Send CAN: MESSAGE.Signal = <raw> '
                               '(<Label>)；ER「… is sent」；procedure「… is '
                               'transmitted」；PROXI $Param$ = "值"（參數名取條文逐字，'
                               'R-VF78 二）；Input Test Data 為 NA',
            "bus": "FD-CAN8（R-VF78 一；Part 1 交付本內 `FD-CAN` 之逐字形實測 0 命中）",
            "spec_reference_source": "R-VF68：037 `Source Requirement ID` → 035 SYSRA "
                                     "`Basic Report` 之「來源需求項目 ID」",
            "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
            "templates": "pilot #1 v4（PROXI 型正負二式、設定顯示與修改型）／"
                         "pilot #2（訊號送出型、訊號上行型），皆已核可，未新創形態",
            "write_back": "**未寫回**（R-VF26）。`seq` 僅記於產出。",
            "tcs": part,
        }
        p = FEAT / f"generated/vf230_batch{i + 1:02d}.json"
        p.write_text(json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  batch{i + 1:02d}  {len(part)} 條  seq {part[0]['seq']}–"
              f"{part[-1]['seq']}  {dict(forms)}  {dict(dist)}")

    (FEAT / "data/_vf230_wvf69_skipped.json").write_text(
        json.dumps({"facts_missing": skipped, "template_rejected": rejected},
                   ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
