"""VF230 pilot #2 之自檢（W-VF68 §2.5）。

R-VF46：逐項分別回報；任一項失敗則 exit code 非 0；不得抑制。

**逐項附可失效測試**（A-VS106 之對治，其為本線第二次發生）——
每一檢查項皆對產出之**副本**施以一次刻意之破壞，若該項仍報 0，
則該項為「其失效與其通過無從分辨」之項，自檢**自身**判為失敗。
不變動原檔（副本以 deepcopy 取得）。
"""
import copy
import csv
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(FEAT / "scripts"))
import vf230_wvf45_priority as PR      # noqa: E402
import vf230_wvf61_pilot as P1         # noqa: E402
import vf230_selfcheck_wvf62 as SC62   # noqa: E402  canon 判準之單一權威

DEFAULT_DOC = FEAT / "generated/vf230_pilot2.json"

SEND_CAN = re.compile(r"^Send CAN: ([A-Z][A-Z0-9_]*)\.(\w+) = (\d+) \(([^)]+)\)$")
SIG_ANY = re.compile(r"\b([A-Z][A-Z0-9_]{3,})\.(\w+)\s*=\s*(\d+)\s*\(([^)]+)\)")
LEAKED = re.compile(r"propId|setProperty|CarPropertyManager|CarPropertyService|VHAL|IVehicle")


def dbc_vals() -> dict:
    d = json.loads((FEAT / "data/_dbc_parsed.json").read_text())
    out = {}
    for bus in d.values():
        for sig, occ in bus["sigs"].items():
            out.setdefault(sig, {"msgs": set(), "vals": {}})
            out[sig]["msgs"].update(o["msg"] for o in occ)
            out[sig]["vals"].update(bus["vals"].get(sig) or {})
    return out


def steps(s: str) -> list[str]:
    return [re.sub(r"^\d+\.\s*", "", x) for x in s.split("\n") if x.strip()]


# ---- 檢查項 ---------------------------------------------------------------
# 每項回傳 list[str]（失敗訊息）。空 list 即通過。

def c1_canon(tcs, ctx):
    """canon 判準**不另立** —— 直接呼叫 `vf230_selfcheck_wvf62.check`。

    首版於此自寫一份 `PRE_ALLOWED` 白名單，其 11 項全過而 wvf62 報 17 筆違規 ——
    **因該白名單與被驗之內容同出一手**（A-VS106 之第三次發生）。
    判準之權威須在被驗之物之外，故改為引用。
    """
    return SC62.check(tcs)


def c2_send_can_form(tcs, ctx):
    bad = []
    for t in tcs:
        for st in steps(t["test_procedure"]):
            if st.startswith("Send CAN") and not SEND_CAN.match(st):
                bad.append(f"seq {t['seq']}：`{st}` 不合 R-1 v2 之 "
                           "`Send CAN: MESSAGE.Signal = <raw> (<Label>)`")
    return bad


def c3_signal_in_dbc(tcs, ctx):
    bad = []
    for t in tcs:
        blob = " ".join(t[k] for k in ("tc_title", "test_procedure", "expected_result",
                                       "pre_conditions"))
        for msg, sig, raw, lab in SIG_ANY.findall(blob):
            d = ctx["dbc"].get(sig)
            if not d:
                bad.append(f"seq {t['seq']}：訊號 `{sig}` 不存在於 DBC")
            elif msg not in d["msgs"]:
                bad.append(f"seq {t['seq']}：`{sig}` 之 message 應為 "
                           f"{sorted(d['msgs'])}，寫為 `{msg}`")
            elif d["vals"].get(raw) != lab:
                bad.append(f"seq {t['seq']}：`{msg}.{sig}` raw {raw} 之 DBC 標籤為 "
                           f"`{d['vals'].get(raw)}`，寫為 `{lab}`")
    return bad


def c4_sent_vs_transmitted(tcs, ctx):
    bad = []
    for t in tcs:
        for st in steps(t["test_procedure"]):
            if SIG_ANY.search(st) and " is sent" in st:
                bad.append(f"seq {t['seq']}：procedure 用「is sent」，"
                           f"應為「is transmitted」——「{st}」")
        for st in steps(t["expected_result"]):
            if SIG_ANY.search(st) and " is transmitted" in st:
                bad.append(f"seq {t['seq']}：ER 用「is transmitted」，"
                           f"應為「is sent」——「{st}」")
    return bad


def c5_step_pairing(tcs, ctx):
    bad = []
    for t in tcs:
        n, m = len(steps(t["test_procedure"])), len(steps(t["expected_result"]))
        if n != m:
            bad.append(f"seq {t['seq']}：procedure {n} 步 vs ER {m} 步，未一一對應")
    return bad


def c6_input_na(tcs, ctx):
    return [f"seq {t['seq']}：Input Test Data 應為 `NA`，實為 `{t['input_test_data']}`"
            for t in tcs if t["input_test_data"] != "NA"]


def c7_priority(tcs, ctx):
    """A-VF17 之對治：判準取自 priority 模組，非本產出。"""
    bad = []
    for t in tcs:
        title, text = t["layer3"], re.sub(r"\s+", " ", ctx["lv"][t["leaf_id"]]["desc"])
        if title in PR.P0A:
            want = ("P0", "P0(a)")
        elif title in PR.P0_SAFETY:
            want = ("P0", "P0(c)")
        elif title in PR.P1_SAFETY_PRESENTATION:
            want = ("P1", "P1")
        elif PR.P2_PAT.search(text):
            want = ("P2", "P2")
        else:
            want = ("P1", "P1")
        if (t["priority"], t["priority_class"]) != want:
            bad.append(f"seq {t['seq']}：priority 應為 {want}，實為 "
                       f"{(t['priority'], t['priority_class'])}")
    return bad


def c8_spec_ref(tcs, ctx):
    bad = []
    for t in tcs:
        want = ctx["refs"].get(ctx["lv"][t["leaf_id"]]["src_ref"], "")
        if t["specification_reference"] != want:
            bad.append(f"seq {t['seq']}：spec_reference 應為 `{want}`（R-VF68 錨鏈），"
                       f"實為 `{t['specification_reference']}`")
    return bad


def c9_no_leaked_impl(tcs, ctx):
    """§2.1 第 1 項既已回退，實作層名詞不得出現於可執行欄位。"""
    bad = []
    for t in tcs:
        for k in ("tc_title", "pre_conditions", "test_procedure", "expected_result"):
            m = LEAKED.search(t[k])
            if m:
                bad.append(f"seq {t['seq']}：`{k}` 殘留實作層名詞 `{m.group(0)}`"
                           "（§2.1 第 1 項已判回退）")
    return bad


def c10_writable_dr(tcs, ctx):
    bad = []
    for t in tcs:
        w = ctx["wr"][t["leaf_id"]]["writable"]
        if t["writable"] != w:
            bad.append(f"seq {t['seq']}：writable 應為 {w}，實為 {t['writable']}")
        has_pending = "PENDING: DR-" in json.dumps(t, ensure_ascii=False)
        if has_pending and not t["dr_dependent"]:
            bad.append(f"seq {t['seq']}：有 PENDING 標記而 dr_dependent 留白")
        if t["dr_dependent"] and not has_pending:
            bad.append(f"seq {t['seq']}：dr_dependent = {t['dr_dependent']} "
                       "而全文無 PENDING 標記")
    return bad


def c11_seq_unique(tcs, ctx):
    """seq 須唯一且為連號。**範圍自產出取，不寫死**（W-VF69 泛化）。"""
    seqs = [t["seq"] for t in tcs]
    bad = []
    if len(set(seqs)) != len(seqs):
        dup = sorted({x for x in seqs if seqs.count(x) > 1})
        bad.append(f"seq 重複：{dup}")
    if seqs != list(range(seqs[0], seqs[0] + len(seqs))):
        bad.append(f"seq 非自 {seqs[0]} 起之連號")
    return bad


CHECKS = [
    ("1  canon 判準（引 wvf62，不另立）", c1_canon),
    ("2  Send CAN 合 R-1 v2 之式", c2_send_can_form),
    ("3  訊號／message／raw→label 與 DBC 相符", c3_signal_in_dbc),
    ("4  ER「is sent」／procedure「is transmitted」", c4_sent_vs_transmitted),
    ("5  procedure 與 ER 步數一一對應", c5_step_pairing),
    ("6  Input Test Data 為 NA", c6_input_na),
    ("7  priority 與判準模組相符", c7_priority),
    ("8  spec_reference 出自 R-VF68 錨鏈", c8_spec_ref),
    ("9  可執行欄位無實作層名詞殘留", c9_no_leaked_impl),
    ("10 writable 與 dr_dependent 相符", c10_writable_dr),
    ("11 seq 唯一且為連號", c11_seq_unique),
]

# 逐項之刻意破壞 —— 施於副本，用以證明該項**能夠**失敗。
# **泛用**（W-VF69）：不指向特定 seq 之特定字串 —— 首版之項 9 破壞式因產出改寫
# 而失效，其「破壞未生效」曾被誤讀為「該檢查項無法失效」。
# 破壞一律施於 ts[0]，且皆為**加寫**或**覆寫**，不依賴既有內容之形態。
BOGUS_SIG = "TELEMATIC_VEHICLE_SETUP.PLGAlert_Req = 9 (Bogus)"

MUTATIONS = {
    "1": lambda ts: ts[0].__setitem__("pre_conditions", "1. Somebody presses a button"),
    "2": lambda ts: ts[0].__setitem__(
        "test_procedure", "1. Send CAN IPC_VEHICLE_SETUP Susp_Tire_Jack high\n"
                          + ts[0]["test_procedure"]),
    "3": lambda ts: ts[0].__setitem__(
        "expected_result", ts[0]["expected_result"] + f"\n99. {BOGUS_SIG} is sent"),
    "4": lambda ts: ts[0].__setitem__(
        "test_procedure", ts[0]["test_procedure"] + f"\n99. {BOGUS_SIG} is sent"),
    "5": lambda ts: ts[0].__setitem__(
        "expected_result", ts[0]["expected_result"] + "\n99. An extra unmatched step"),
    "6": lambda ts: ts[0].__setitem__("input_test_data", "Off"),
    "7": lambda ts: ts[0].__setitem__(
        "priority", "P9"),
    "8": lambda ts: ts[0].__setitem__("specification_reference", "VF230_V1_PDT27_VF_9999"),
    "9": lambda ts: ts[0].__setitem__(
        "test_procedure", "1. Invoke setProperty() with propId = PLGAlert_Req\n"
                          + ts[0]["test_procedure"]),
    "10": lambda ts: ts[0].__setitem__("writable", "W9"),
    "11": lambda ts: ts[-1].__setitem__("seq", ts[0]["seq"]),
}


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DOC
    doc = json.loads(path.read_text(encoding="utf-8"))
    ctx = {
        "dbc": dbc_vals(),
        "lv": {r["swe_id"]: r for r in csv.DictReader(
            (FEAT / "data/vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t")},
        "wr": {r["leaf_id"]: r for r in csv.DictReader(
            (FEAT / "docs/reports/vf230_writability.tsv").open(encoding="utf-8"),
            delimiter="\t")},
        "refs": P1.spec_refs(),
    }

    print(f"=== {path.name} 自檢（{len(doc['tcs'])} 條，R-VF46 逐項分報）===")
    total, details = 0, []
    for name, fn in CHECKS:
        bad = fn(doc["tcs"], ctx)
        total += len(bad)
        print(f"  {'❌' if bad else '✅'} {name:38} {len(bad)}")
        details += bad

    print("\n=== 逐項可失效測試（A-VS106 之對治）===")
    dead = []
    for name, fn in CHECKS:
        num = name.split()[0]
        mutant = copy.deepcopy(doc)
        MUTATIONS[num](mutant["tcs"])
        if mutant["tcs"] == doc["tcs"]:
            print(f"  ❌ 項 {num:<3} **破壞未生效**（副本與原檔相同）—— "
                  "此測試本身無效，非該檢查項無效")
            dead.append(num)
            continue
        n = len(fn(mutant["tcs"], ctx))
        ok = n > 0
        print(f"  {'✅' if ok else '❌'} 項 {num:<3} 破壞後回報 {n} 筆"
              f"{'' if ok else '  ← 該項之失效與其通過無從分辨'}")
        if not ok:
            dead.append(num)

    if details:
        print("\n=== 失敗明細 ===")
        for d in details:
            print(f"  - {d}")
    if dead:
        print(f"\n自檢自身失敗：項 {', '.join(dead)} 無法失效")
    print(f"\n合計 {total} 筆失敗；無法失效之項 {len(dead)} 個")
    sys.exit(1 if (total or dead) else 0)


if __name__ == "__main__":
    main()
