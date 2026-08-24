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
import vf230_wvf69_facts as FACTS      # noqa: E402  EXCLUDE 之單一權威（R-VF91 二）

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


# ---- R-VF91 二：`input_test_data` 之唯一合法非 NA 形態 ----
# 本項原為「一律 NA」。R-VF91 二令訊號上行型之未指名值改依 canon §8.4.1
# 之佔位形式，其 `input_test_data` **須**逐字列 DBC 有效值域全集。
# **放行不得只看形態** —— 若只驗「長得像佔位式」，即為造值開門。
# 故放行之條件含「所列值域逐項與 DBC 相符」一項，其為本項之實質防線。
PLACEHOLDER = re.compile(r"^([A-Za-z0-9_]+)\.([A-Za-z0-9_]+) = one of \[(.+)\]$")
# R-VF101 二：必要句增分句後之逐字形。**單一權威**：自 batches 匯入，
# 二處各寫一份則其分岔不會被任何檢查攔下（R-G20 之同一顧慮）。
import vf230_wvf69_batches as BATCHES     # noqa: E402
NEED_SENT = BATCHES.NEED_SENTENCE


def c6_input_na(tcs, ctx):
    bad = []
    for t in tcs:
        v = t["input_test_data"]
        if v == "NA":
            continue
        m = PLACEHOLDER.match(v)
        if not m:
            bad.append(f"seq {t['seq']}：Input Test Data 應為 `NA` 或 R-VF91 二之"
                       f"佔位式，實為 `{v}`")
            continue
        msg, sig, body = m.group(1), m.group(2), m.group(3)
        if t.get("clause_form") != "訊號上行型":
            bad.append(f"seq {t['seq']}：佔位式僅適用訊號上行型（R-VF91 一），"
                       f"本條為 `{t.get('clause_form')}`")
            continue
        if NEED_SENT not in (t.get("reasoning") or ""):
            bad.append(f"seq {t['seq']}：佔位式而 reasoning 缺 R-VF91 二之必要句")
            continue
        # **實質防線**：所列之 raw→label 須逐項出自 DBC，且為該訊號之**全集**
        # （排除保留值後）。缺一項或多一項皆為造值。
        vals = (ctx["dbc"].get(sig) or {}).get("vals")
        if not vals:
            bad.append(f"seq {t['seq']}：佔位式之訊號 `{sig}` 不在 DBC")
            continue
        listed = []
        for part in body.split(", "):
            mm = re.match(r"^(\d+) \((.+)\)$", part)
            if not mm:
                bad.append(f"seq {t['seq']}：佔位式之項 `{part}` 不合 `raw (label)` 式")
                break
            listed.append((mm.group(1), mm.group(2)))
        else:
            want = [(r, vals[r]) for r in sorted(vals, key=lambda x: int(x))
                    if not FACTS.EXCLUDE.match(vals[r].strip())]
            if listed != want:
                bad.append(f"seq {t['seq']}：佔位式所列值域 {listed} 與 DBC 之有效"
                           f"值域 {want} 不符（序亦須為 raw 序）")
    return bad


# ---- R-VF92 一：項 6 之實質防線須獨立確認其能攔 ----
# 項 6 之泛用破壞式（`input_test_data = "Off"`）只證明「非 NA 且非佔位式」被攔，
# **未證明「形態合法而值域造假」被攔** —— 而後者才是本項之實質防線。
# 一個只驗形態之通過，與造值未被攔不可分辨。故另立三個造值錨點，逐一實測。
FORGE_ANCHORS = [
    ("IPC_VEHICLE_SETUP.PLGAlert = one of [0 (Off), 1 (On), 2 (Maybe)]",
     "多列一個 DBC 所無之值"),
    ("IPC_VEHICLE_SETUP.PLGAlert = one of [0 (Off)]",
     "漏列一個 DBC 有之值（非全集）"),
    ("IPC_VEHICLE_SETUP.PLGAlert = one of [1 (On), 0 (Off)]",
     "值域正確而**序非 raw 序**（代表值因而被換掉）"),
]


def verify_forge(ctx) -> None:
    """R-VF92 一：於不經產出之另一路徑上，證實造值確被項 6 攔下。"""
    bad = []
    for itd, kind in FORGE_ANCHORS:
        probe = [{"seq": 9999, "input_test_data": itd,
                  "clause_form": "訊號上行型",
                  "reasoning": NEED_SENT}]
        caught = bool(c6_input_na(probe, ctx))
        print(f"  {'✅' if caught else '❌'} {kind}\n      {itd[:58]}… → "
              f"攔下={caught}")
        if not caught:
            bad.append(kind)
    # 反向：真值域須放行，否則本錨點組只是把項 6 變成一律拒絕
    ok_itd = "IPC_VEHICLE_SETUP.PLGAlert = one of [0 (Off), 1 (On)]"
    probe = [{"seq": 9999, "input_test_data": ok_itd,
              "clause_form": "訊號上行型", "reasoning": NEED_SENT}]
    passed = not c6_input_na(probe, ctx)
    print(f"  {'✅' if passed else '❌'} **假陽之防**：真值域須放行 → 放行={passed}")
    if not passed:
        bad.append("真值域被誤攔")
    if bad:
        raise SystemExit("R-VF92 一之造值錨點不符，停 —— " + "；".join(bad))


# ---- R-VF98：手足區辨之最低要件（W-VF72 第 4 項）----
FAMILY = re.compile(r"-?\d+$")


def _family(leaf: str) -> str:
    return FAMILY.sub("", leaf)


def c13_sibling_title_unique(tcs, ctx):
    """同一 leaf 家族內，`tc_title` 逐字相同者 → FAIL（canon §4.3；R-VF98 一）。

    **跨批**：家族之成員未必落於同一批，故本項於 `ctx["all"]`（全批合併）
    上判，而以本批之 seq 回報 —— 只看單批者會漏掉跨批之對。
    """
    fam = {}
    for t in ctx.get("all") or tcs:
        fam.setdefault((_family(t["leaf_id"]), t["tc_title"]), []).append(t["seq"])
    mine = {t["seq"] for t in tcs}
    return [f"seq {sorted(v)}：同家族 `{k[0]}` 之 tc_title 逐字相同 —— `{k[1]}`"
            for k, v in sorted(fam.items()) if len(v) > 1 and mine & set(v)]


def c14_sibling_discriminator(tcs, ctx):
    """家族 > 1 條者，其 `tc_title` 須含區辨 token（R-VF98 二）。

    **V35 之逐字形式為「不含 ` when ` 且家族 TC 數 > 1 → FAIL」，本層實測其過寬**：
    訊號送出型之合法標題 `X is sent as 0 (Disabled)` 無 ` when ` 而**有**區辨
    （raw ＋ label），照該式將誤殺 9 條。
    **改為**：標題須含 ` when ` **或** `as <raw> (<Label>)` 之區辨式，二者有其一即可。
    其攔下者為「`<設定> is displayed and modifiable`」此類**無任何區辨**之形式
    —— 即 R-VF98 所欲攔者。
    """
    # 區辨式之三形：條件子句 ` when `、`as <raw> (<Label>)`、`= <raw> (<Label>)`。
    # **第三形不得漏**：上行型之次式為 `<Sig> = 0 (Disable) updates the <S> setting`，
    # 其有 raw ＋ label 之區辨而無 ` when ` 亦無 `as ` —— 漏之即誤殺（實測 seq 458）。
    # 區辨式之四形：` when ` 條件子句、`as/is/= <raw> (<Label>)`、`as <Label>`。
    # **第四形不得漏**：長設定名之上行型退化為 `<S> is displayed as OFF`，
    # 其**帶值**故對同家族他條不可共用（實測 seq 528／537 之 Visual vs Audible）。
    # **邊界**：`is displayed and modifiable` 無值，仍被攔 —— 即 R-VF98 所欲攔者。
    # `\b` 不可置於 `=` 之前 —— 空格與 `=` 之間無詞邊界，該式恆不命中（實測）。
    DISC = re.compile(r" when |(?:\bas|\bis|=) \d+ \(|\bas [A-Z][A-Za-z0-9_]*\b")
    size = {}
    for t in ctx.get("all") or tcs:
        size[_family(t["leaf_id"])] = size.get(_family(t["leaf_id"]), 0) + 1
    # **canon §4.3 之退化為合法例外，但不得靜默** —— 其 `reasoning` 內須有
    # 逐字之具名（`**標題退化為無條件式**`），缺之即 FAIL。
    # 退化條之逐字唯一性由項 13 守住；本項只保證「退化必被具名且可數」。
    bad, degraded = [], []
    for t in tcs:
        if size.get(_family(t["leaf_id"]), 1) <= 1 or DISC.search(t["tc_title"]):
            continue
        if "**標題退化為無條件式**" in (t.get("reasoning") or ""):
            degraded.append(t["seq"])
            continue
        bad.append(f"seq {t['seq']}：家族 `{_family(t['leaf_id'])}` 有 "
                   f"{size[_family(t['leaf_id'])]} 條而本條標題無區辨 token"
                   f"且未具名其退化 —— `{t['tc_title']}`")
    if degraded:
        print(f"      ↳ canon §4.3 之具名退化 {len(degraded)} 條（非違規，回報使其可見）："
              f"{degraded}")
    return bad


# ---- R-VF107：句界切分之守衛（W-VF76 §1）----
# `clause_tail()` 以 `re.split(r"(?<=\.)\s+", …)` 切句，**對「句號後無空格」無效**
# （實測 seq 407 之 `…availability.If $Signature_Lighting$…`，二句被切為一句）。
# 其後果：若該處之後為管路句，`PLUMBING.match()` 只驗合併後之首字元，**刪不掉**。
#
# **准立之理由不是它現在會攔到東西，而是它現在攔不到**（V42 §2 逐字）——
# 全 437 條實測：含此形態者 127 條，**因而留下管路句者 0 條**。
# 「缺口存在而現行後果為零」是**現況而非保證**，而無此守衛則其發生無人會知
# （A-VS106 同型）。**不改切分式本身**（改之影響全部 `test_item`，屬判準變動）。
NOSPACE = re.compile(r"([a-z0-9)\]])\.([A-Z])")


def c15_sentence_boundary(tcs, ctx):
    bad = []
    for t in tcs:
        item = t.get("test_item") or ""
        if not NOSPACE.search(item):
            continue
        fixed = NOSPACE.sub(r"\1. \2", item)
        for sent in re.split(r"(?<=\.)\s+", fixed.strip()):
            if sent.strip() and BATCHES.PLUMBING.match(sent):
                bad.append(f"seq {t['seq']}：`test_item` 之句號後無空格致切分失效，"
                           f"補空格重切後有管路句可刪 —— `{sent.strip()[:64]}…`")
                break
    return bad


def c12_placeholder_sentence(tcs, ctx):
    """W-VF71 第 2 項：R-VF91 二末之必要句，缺之即 FAIL。

    **其射程為「佔位式之條」**，非全部 —— 逐字指名值者無此句，
    強令之則該句成為樣板噪音，反使其失去「此條未指名值」之標記作用。
    """
    return [f"seq {t['seq']}：input_test_data 為佔位式而 reasoning 缺必要句"
            f"「{NEED_SENT}」"
            for t in tcs
            if PLACEHOLDER.match(t["input_test_data"] or "")
            and NEED_SENT not in (t.get("reasoning") or "")]


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
    ("12 R-VF91 二之必要句（佔位式）", c12_placeholder_sentence),
    ("13 同家族 tc_title 不得逐字相同", c13_sibling_title_unique),
    ("14 家族>1 之標題須含區辨 token", c14_sibling_discriminator),
    ("15 句界切分未因無空格而漏刪管路句", c15_sentence_boundary),
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
    # 項 12 之破壞須**泛用**：本組未必首條即佔位式，故先造一個合法佔位式
    # （值域取自 DBC 之真值，故項 6 不會先攔），再抽掉其必要句。
    "12": lambda ts: _break12(ts),
    # 項 13：令首二條同家族且標題逐字相同
    "13": lambda ts: (ts[1].__setitem__("leaf_id", ts[0]["leaf_id"][:-1] + "9"),
                      ts[1].__setitem__("tc_title", ts[0]["tc_title"])),
    # 項 14：令首條與次條同家族，且首條之標題無任何區辨 token
    # 項 14 之破壞須令**同一家族有二條**且首條無區辨、且未具名退化。
    # **不可只改 ts[1] 之 leaf_id** —— 小樣本（pilot #3 僅 3 條且家族各異）下
    # 家族計數仍為 1，該項遂無從失效（實測 pilot #3 報「項 14 無法失效」）。
    # 故改為令二條**同屬一新家族**，其計數必為 2。
    # 項 15：構造「句號後無空格 ＋ 其後為管路句」之 test_item。
    # **其前半須為完整句且以小寫或 `)` 結尾**，否則 NOSPACE 不命中而破壞不生效。
    "15": lambda ts: ts[0].__setitem__(
        "test_item", "The HMI shall display the setting.VHAL shall forward the "
                     "updated value to CarPropertyService."),
    "14": lambda ts: (ts[0].__setitem__("leaf_id", "SWE1-VC-MutantFamily-001"),
                      ts[1].__setitem__("leaf_id", "SWE1-VC-MutantFamily-002"),
                      ts[0].__setitem__("tc_title", "Some Setting is displayed"),
                      ts[0].__setitem__("reasoning", "（本破壞式抽除了退化之具名）")),
}


def _break12(ts):
    t = ts[0]
    t["clause_form"] = "訊號上行型"
    t["input_test_data"] = "IPC_VEHICLE_SETUP.PLGAlert = one of [0 (Off), 1 (On)]"
    t["reasoning"] = "（必要句已被本破壞式抽除）"


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
    # ---- 項 13／14 之跨批視野（W-VF75 §5-2：改以清單檔為來源）----
    # 家族之成員未必落於同一批（實測 `TrailerNumber` 橫跨 batch03 與 batch06），
    # **只看單批者會漏掉跨批之對**。
    #
    # **原以 `generated/` 之目錄列舉為視野來源，其縮小為靜默**（A-VS106 同型）：
    # 舊批若移出該目錄，`glob` 少抓幾個檔而視野隨之縮小，**無任何回報**。
    # 改以 `data/vf230_batches.tsv` 為**單一權威**：
    #   **清單所列而檔案不存在者即 FAIL** —— 縮小遂由靜默轉為可見。
    man = FEAT / "data" / "vf230_batches.tsv"
    if not man.exists():
        raise SystemExit(f"跨批視野之清單檔不存在：{man} —— "
                         "無其則視野之縮小不可見，停")
    allt, missing = [], []
    listed = list(csv.DictReader(man.open(encoding="utf-8"), delimiter="\t"))
    for row in listed:
        q = FEAT / row["file"]
        if not q.exists():
            missing.append(row["batch"])
            continue
        allt += json.loads(q.read_text(encoding="utf-8"))["tcs"]
    if missing:
        raise SystemExit(f"跨批視野缺 {len(missing)} 批（清單所列而檔案不存在）："
                         f"{missing} —— 視野已縮小，停")
    ctx["all"] = allt or doc["tcs"]
    print(f"  跨批視野：{len(listed)} 批 / {len(allt)} 條"
          f"（來源 `data/vf230_batches.tsv`）")

    print(f"=== {path.name} 自檢（{len(doc['tcs'])} 條，R-VF46 逐項分報）===")
    total, details = 0, []
    for name, fn in CHECKS:
        bad = fn(doc["tcs"], ctx)
        total += len(bad)
        print(f"  {'❌' if bad else '✅'} {name:38} {len(bad)}")
        details += bad

    print("\n=== R-VF92 一：項 6 實質防線之造值錨點（獨立確認）===")
    verify_forge(ctx)

    print("\n=== 逐項可失效測試（A-VS106 之對治）===")
    dead = []
    for name, fn in CHECKS:
        num = name.split()[0]
        mutant = copy.deepcopy(doc)
        MUTATIONS[num](mutant["tcs"])
        # 跨批項（13／14）之 ctx 亦須換為 mutant，否則其破壞被原批之內容蓋過
        seqs = {t["seq"] for t in mutant["tcs"]}
        ctx = {**ctx, "all": mutant["tcs"] + [t for t in allt
                                              if t["seq"] not in seqs]}
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
