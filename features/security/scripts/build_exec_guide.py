#!/usr/bin/env python3
"""`delivery/EXEC_GUIDE.md`（SEC-12 §2）—— 一次性環境建置與通道操作指南。

**指南是 TC 之索引，不是新素材**（下放包 §0）：每一指令／路徑／tag／artifact
皆自 `sandbox/batch{1,2,3}/*.json` 逐字抽出；抽不到者不寫。
`--verify` 另跑一次「指南之指令 ⊆ TC 之指令」全匹配檢查。
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SB = ROOT / "features" / "security" / "sandbox"
DATA = ROOT / "features" / "security" / "data"
OUT = SB / "delivery" / "EXEC_GUIDE.md"
BOOK = ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
        "Specification & Result_SWQT_Security_20260917.xlsx")

RE_CMD = re.compile(r"^\s*(\$\s+\S.*|Send CAN:\s*\S.*)$")
RE_STEP = re.compile(r"^\s*\d+[.)]\s*(.+)$")
RE_PHYS = re.compile(r'^(Insert|Press|Power cycle|Disconnect|Select ")')
RE_OBTAIN = re.compile(r"<obtain (.+?) per RD>")
RE_TAG = re.compile(r"adb logcat -s (\S+)")
RE_PATH = re.compile(r"(/(?:data|vendor|mnt|system|odm|sys)[A-Za-z0-9_./{}<>-]*)")
RE_INSTR = re.compile(r"-e class (\S+)")
RE_PLACEHOLDER_CMD = re.compile(r"^\$ <command provided by ([^()]+) \((X-[a-z0-9-]+)\)>$")

# 觀察面之分類（R-SEC7(c) 七類 ＋ R-SEC7(amend2) 之 DOC）
OBSERVE = [
    ("RC", r"OK \(\d+ tests?\)|FAILURES!!!|instrumentation"),
    ("LOG", r"adb logcat"),
    ("FILE", r"adb shell (?:ls|cat|od|df|procrank|ps)|adb pull|od -t x1"),
    ("UDS", r"Positive response is received|Negative response is received"),
    ("HOST", r"\bopenssl\b|logdecrypt_Ver2\.sh"),
    ("CAN", r"is sent\b"),
    ("DOC", r"is available for review|satisfies \"|satisfy \""),
]
# 自動化 helper（§2 第 5 節）
HELPER = {"ADB": "adb(cmd)", "RC": "instrument(class, method)", "UDS": "uds(bytes)",
          "CAN": "can_send(msg, sig, raw)", "HOST": "host(cmd)", "PHYS": "pause(prompt)",
          "DOC": "doc_review()  # not generated"}


# ---------------------------------------------------------------- §1.6（SEC-13 §2）
# 環境知識：**TC 以外**之來源，每行必附來源檔與位置（下放包 §0）。
# 逐行由執行層現查；查無來源者不寫（見上繳包 §3）。`⊆` 驗證對本節不適用（R-SEC13 §2），
# 惟本節每行須含 ` — ` 之來源片段（第二項驗證）。
ENV_KNOWLEDGE: list[tuple[str, str]] = [
    ("Runner install: `$ adb install -r -t CertProviderServiceManagerTest.apk`",
     "CCVR SYS2_Mapped, sheet `Cert Val CS.98`, STEPS column, items 2 and 5 (verbatim). "
     "The CCVR directory listing names the file `CertProviderAndroidInstrumentalTest.apk` "
     "(handoff `down/20260916_SEC-01.md` line 125); the workbook Pre-Condition follows the "
     "directory listing per R-SEC24 — confirm with RD which file is shipped"),
    ("Runner check: `$ adb shell pm list instrumentation | grep melcocertprovider`",
     "CCVR SYS2_Mapped, sheet `Cert Val CS.98`, STEPS column, items 2-10 (verbatim)"),
    ("KeyInstall / KeyMaster integration tests are run with `$ pytest` and "
     "`$ pytest --html=report.html --self-contained-html`; preconditions are "
     "`Build with BUILD_INTEGRATION_TESTS checked`, `python3 (>=3.6)`, pip3 "
     "`cryptography`/`pytest (>=6.2.4)`/`pytest-html`, and `Connected device`. No APK file "
     "name is stated, so install from `<apk provided by RD>`",
     "Z1 `IntegrationTests/PythonTests/README.md` lines 4-18"),
    ("Cert Provider integration tests are run the same way, with the additional precondition "
     "`$ adb remount`",
     "Z2 `IntegrationTests/README.md` lines 4-18"),
    ("Root shell: `$ adb root`",
     "Z1 `IntegrationTests/PythonTests/common/adb_wrapper.py` lines 41-42 "
     "(`def root(): os.system(\"adb root\")`)"),
    ("`installstate` byte values: `0x00` not installed",
     "Z1 `IntegrationTests/PythonTests/KeysInstallationTests/"
     "test_default_keys_unprovisioned.py` lines 43-46"),
    ("`installstate` byte values: `0x01` verification pending, `0x02` installed, `0x03` error",
     "Z1 `IntegrationTests/PythonTests/common/keys_install_helper.py` — `assert_verification` "
     "lines 204-206, `assert_success` lines 209-211, `assert_error` lines 214-216"),
    ("`/mnt/vendor/oemkeys/status/keyinstall` 8-byte values: verification "
     "`02 00 00 00 00 00 00 00`, success `00 00 00 00 00 00 00 00`, error "
     "`08 00 00 00 00 00 00 00`",
     "Z1 `IntegrationTests/PythonTests/common/keys_install_helper.py` lines 206, 211, 216"),
    ("Diagnostic CAN identifiers: Atlantis High `0x7BF` and `0x53F`; Atlantis Mid "
     "`0x18DA87F1` and `0x18DAF187`",
     "`forms/VHAL_User_Guide_R5.pdf` section 2.4, `Setting Arch Type DID using RAFT Tool`"),
    ("Architecture DID: write `$2850` with `2E 28 50 03` for Atlantis Mid or `2E 28 50 05` "
     "for Atlantis High (Atlantis High is the default), then `setprop "
     "persist.vendor.can.arch <value>` and reboot the head unit",
     "`forms/VHAL_User_Guide_R5.pdf` section 2.4"),
]


def id_map() -> dict[str, str]:
    """R-SEC25(e)：六本形制下，TC ID 以 `<Component>/<新 ID>` 呈現。無對照表時回空。"""
    f = DATA / "id_map_v08_v09.tsv"
    if not f.exists():
        return {}
    return {r["old_id"]: f'{r["workbook"]}/{r["new_id"]}'
            for r in csv.DictReader(f.open(encoding="utf-8"), delimiter="\t")}


def load_tcs() -> list[dict]:
    out = []
    for d in ("batch1", "batch2", "batch3"):
        for f in sorted((SB / d).glob("NR1L-*.json")):
            out.append(json.loads(f.read_text(encoding="utf-8")))
    return sorted(out, key=lambda t: t["tc_id"])


def commands(tc: dict) -> list[str]:
    return [m.group(1).strip() for ln in tc["proc"].splitlines()
            if (m := RE_CMD.match(ln))]


def channel_of(cmd: str) -> str:
    if cmd.startswith("Send CAN:"):
        return "CAN"
    body = cmd[2:].strip()
    if RE_PLACEHOLDER_CMD.match(cmd):
        return "PENDING-ASSET"
    if body.startswith("adb shell am instrument"):
        return "RC"
    if body.startswith("adb"):
        return "ADB"
    if re.match(r"^[0-9A-F]{2}( [0-9A-F]{2})*$", body):
        return "UDS"
    return "HOST"


def bullet(rows: list[str]) -> str:
    return "\n".join(f"- {r}" for r in rows)



def crosscheck(cmd_tcs: dict, instr_tcs: dict) -> dict[str, str]:
    """對三份資料檔做**實際**交叉核對（下放包 §2「自資料檔生成」）。

    權威面仍是 TC（§0）；本核對只回報一致性，不改指南內容、不當閘門。
    """
    out: dict[str, str] = {}
    # apk_pairing.tsv：TC 所調用之 instrumentation method ⊆ 已配對之方法集合
    pair = {r["method"] for r in csv.DictReader(
        (DATA / "apk_pairing.tsv").open(encoding="utf-8"), delimiter="\t")}
    methods = {c.rsplit("#", 1)[1] for c in instr_tcs if "#" in c}
    out["apk_pairing"] = (f"{len(methods & pair)}/{len(methods)} instrumentation methods are "
                          f"listed in apk_pairing.tsv ({len(pair)} paired methods)"
                          + (f"; not listed: {sorted(methods - pair)}" if methods - pair else ""))
    # step_assets.tsv：指令之核心片段是否見於 `value(verbatim)`
    def norm(text: str) -> str:
        return re.sub(r'[\s"\']+', " ", text).strip().lower()
    assets = [norm(r["value(verbatim)"]) for r in csv.DictReader(
        (DATA / "step_assets.tsv").open(encoding="utf-8"), delimiter="\t")]
    real = [c for c in cmd_tcs if not RE_PLACEHOLDER_CMD.match(c)
            and channel_of(c) in ("ADB", "RC", "HOST")]
    seen = [c for c in real if any(norm(c[2:]) in a or a in norm(c[2:]) for a in assets)]
    out["step_assets"] = (f"{len(seen)}/{len(real)} ADB/RC/HOST command lines have a matching "
                          f"`value(verbatim)` row in step_assets.tsv ({len(assets)} asset rows); "
                          "the remainder are mostly `adb logcat -s <TAG>` lines, whose tags are "
                          "sourced per test case in the Remarks (037 verification criteria / "
                          "CS.212), plus commands added by later packages (Z1 integration tests, "
                          "037 resource monitoring)")
    # diag_items.tsv：UDS 讀取之 DID 是否登錄
    ids = {r["id"] for r in csv.DictReader(
        (DATA / "diag_items.tsv").open(encoding="utf-8"), delimiter="\t")}
    dids = {"".join(c[2:].split()[1:]).upper() for c in cmd_tcs
            if channel_of(c) == "UDS" and c[2:].split()[0] == "22"}
    out["diag_items"] = (f"{len(dids & ids)}/{len(dids)} data identifiers read over UDS are "
                         f"registered in diag_items.tsv ({sorted(dids)})")
    return out


def main() -> int:
    tcs = load_tcs()
    imap = id_map()
    for t in tcs:                      # 指南之 TC 稱謂一律用新式
        t["tc_id"] = imap.get(t["tc_id"], t["tc_id"])
    cmd_tcs: dict[str, list[str]] = defaultdict(list)
    pre_tcs: dict[str, list[str]] = defaultdict(list)
    tag_tcs: dict[str, list[str]] = defaultdict(list)
    path_tcs: dict[str, list[str]] = defaultdict(list)
    art_tcs: dict[str, list[str]] = defaultdict(list)
    phys_tcs: dict[str, list[str]] = defaultdict(list)
    instr_tcs: dict[str, list[str]] = defaultdict(list)
    er_by_class: dict[str, dict[str, list[str]]] = {k: defaultdict(list) for k, _ in OBSERVE}
    chan_tcs: dict[str, set[str]] = defaultdict(set)
    dbc_notes: Counter = Counter()

    for t in tcs:
        tid = t["tc_id"]
        for ln in t["pre"].splitlines():
            if m := RE_STEP.match(ln):
                pre_tcs[m.group(1).strip()].append(tid)
        for ln in t["proc"].splitlines():
            if m := RE_CMD.match(ln):
                cmd = m.group(1).strip()
                cmd_tcs[cmd].append(tid)
                chan_tcs[channel_of(cmd)].add(tid)
                for mm in RE_TAG.finditer(cmd):
                    tag_tcs[mm.group(1)].append(tid)
                for mm in RE_PATH.finditer(cmd):
                    path_tcs[mm.group(1)].append(tid)
                for mm in RE_INSTR.finditer(cmd):
                    instr_tcs[mm.group(1)].append(tid)
            elif m := RE_STEP.match(ln):
                body = m.group(1).strip()
                if RE_PHYS.match(body):
                    phys_tcs[body].append(tid)
                    chan_tcs["PHYS"].add(tid)
                for mm in RE_OBTAIN.finditer(body):
                    art_tcs[mm.group(1)].append(tid)
                    chan_tcs["DOC"].add(tid)
        for ln in t["er"].splitlines():
            body = RE_STEP.match(ln).group(1).strip() if RE_STEP.match(ln) else ln.strip()
            for name, pat in OBSERVE:
                if re.search(pat, body):
                    er_by_class[name][body].append(tid)
                    break
        for ln in t["remarks"].splitlines():
            if ln.startswith("CAN signal per"):
                dbc_notes[ln.strip()] += 1

    # §1.1 之 apk 檔名一律自 Pre-Condition 抽取，不寫死（SEC-13 review §二）
    apk_names = sorted({m.group(1) for p_ in pre_tcs
                        for m in [re.search(r"Test runner (\S+\.apk) is installed", p_)] if m})
    xc = crosscheck(cmd_tcs, instr_tcs)
    today = date.today().isoformat()
    L: list[str] = [
        f"# Security Test Execution Guide — {BOOK}",
        "",
        f"Generated {today} from `sandbox/batch1|2|3/*.json` — the same source as the delivery "
        "workbook. **Every command, path, tag and artifact below appears verbatim in at least "
        "one test case**; nothing here is new material.",
        "",
        "Cross-check against the source registers (reported, not a gate — the workbook is "
        "authoritative):",
        "",
        bullet([f"`apk_pairing.tsv` — {xc['apk_pairing']}",
                f"`step_assets.tsv` — {xc['step_assets']}",
                f"`diag_items.tsv` — {xc['diag_items']}"]),
        "",
        f"Scope: {len(tcs)} test cases, {len(cmd_tcs)} distinct command lines.",
        "",
        "## 1. One-time environment setup",
        "",
        "### 1.1 ADB",
        "",
        "Pre-conditions used by the test cases (verbatim, with the number of cases that carry them):",
        "",
    ]
    adb_pre = [p for p in pre_tcs if re.search(r"ADB|runner|apk|assets are available", p)]
    L.append(bullet([f"`{p}` — {len(pre_tcs[p])} TC" for p in
                     sorted(adb_pre, key=lambda p: -len(pre_tcs[p]))]))
    L += ["",
          "Instrumentation runners invoked by the test cases:",
          "",
          bullet([f"`{c}` — {len(v)} TC" for c, v in
                  sorted(instr_tcs.items(), key=lambda kv: -len(kv[1]))]),
          "",
          f"> The APK file name appears in the workbook only as "
          f"{' / '.join(f'`{a}`' for a in apk_names) or '`<none>`'} (Pre-Condition above). "
          "For the KeyInstall and KeyMaster runners the workbook names the instrumentation "
          "class but no APK file, so install them from `<apk provided by RD>`.",
          "",
          "### 1.2 UDS",
          ""]
    uds = {c: v for c, v in cmd_tcs.items() if channel_of(c) == "UDS"}
    L += ["Request bytes used by the test cases (each line is a Procedure step verbatim):", "",
          bullet([f"`{c}` — {len(v)} TC ({', '.join(sorted(set(v)))})"
                  for c, v in sorted(uds.items())]),
          "",
          "Diagnostic session access (Pre-Condition verbatim):", "",
          bullet([f"`{p}` — {len(pre_tcs[p])} TC" for p in pre_tcs if "ADA" in p]),
          "",
          "> The workbook carries no diagnostic CAN identifier and no session other than the "
          "bytes listed above, so none is stated here; use the tester configuration of the "
          "Diagnostics feature.",
          "",
          "### 1.3 CAN", ""]
    can = {c: v for c, v in cmd_tcs.items() if c.startswith("Send CAN:")}
    L += ["Signal lines used by the test cases:", "",
          bullet([f"`{c}` — {len(v)} TC ({', '.join(sorted(set(v)))})"
                  for c, v in sorted(can.items())]),
          "",
          "Source of the signal definitions (from the Remarks of those cases):", "",
          bullet([f"`{n}` — {v} TC" for n, v in dbc_notes.most_common()]),
          "",
          "### 1.4 Host tools", ""]
    host = {c: v for c, v in cmd_tcs.items() if channel_of(c) == "HOST"}
    L += [bullet([f"`{c}` — {len(v)} TC" for c, v in sorted(host.items())]),
          "",
          "### 1.5 Document review", "",
          "Artifacts to obtain from the RD build environment "
          f"({len(art_tcs)} distinct, {len(set(sum(art_tcs.values(), [])))} TC):", "",
          bullet([f"`{a}` — {len(v)} TC" for a, v in
                  sorted(art_tcs.items(), key=lambda kv: (-len(kv[1]), kv[0]))]),
          "",
          "Access required (Pre-Conditions verbatim):", "",
          bullet([f"`{p}` — {len(pre_tcs[p])} TC" for p in
                  sorted(p for p in pre_tcs if p.startswith("Access to the RD"))]),
          "",
          "## 1.6 Environment knowledge (not from test cases)", "",
          "Each line below is cited to a source outside the workbook; **nothing here is asserted "
          "by any test case**, so the `⊆` check does not apply to this section.", "",
          "\n".join(f"- {text} — {src}" for text, src in ENV_KNOWLEDGE),
          "",
          "## 2. How to read observations", ""]
    for name, _pat in OBSERVE:
        rows = er_by_class[name]
        if not rows:
            continue
        top = sorted(rows.items(), key=lambda kv: (-len(kv[1]), kv[0]))[:8]
        L += [f"### {name} — {len(rows)} distinct assertions, "
              f"{len(set(sum(rows.values(), [])))} TC", "",
              bullet([f"`{r}` — {len(v)} TC" for r, v in top]),
              ("" if len(rows) <= 8 else
               f"\n> {len(rows) - 8} further {name} assertions follow the same shape; "
               "the workbook is authoritative."),
              ""]
    L += ["Log tags used (`adb logcat -s <TAG>`):", "",
          bullet([f"`{t}` — {len(v)} TC" for t, v in
                  sorted(tag_tcs.items(), key=lambda kv: -len(kv[1]))]),
          "",
          "Device paths read or written:", "",
          bullet([f"`{p}` — {len(v)} TC" for p, v in
                  sorted(path_tcs.items(), key=lambda kv: (-len(kv[1]), kv[0]))]),
          "",
          "## 3. Command index", "",
          "| # | Command (verbatim) | TC |",
          "| ---: | --- | --- |"]
    for i, (c, v) in enumerate(sorted(cmd_tcs.items(), key=lambda kv: (-len(kv[1]), kv[0])), 1):
        ids = sorted(set(v))
        shown = ", ".join(ids[:6]) + (f" …(+{len(ids) - 6})" if len(ids) > 6 else "")
        L.append(f"| {i} | `{c}` | {shown} |")
    L += ["", "## 4. Assets still to be provided", "",
          "From `placeholder_by_token.tsv`; the placeholders inside the workbook carry the same "
          "code. See `asset_request.md` for who to ask and the urgency order.", "",
          "| Token | Placeholder lines | TC | Fields |", "| --- | ---: | ---: | --- |"]
    tok_file = (DATA / "placeholder_by_token_v09.tsv"
                if (DATA / "placeholder_by_token_v09.tsv").exists()
                else DATA / "placeholder_by_token.tsv")
    for r in csv.DictReader(tok_file.open(encoding="utf-8"), delimiter="\t"):
        L.append(f'| `{r["token"]}` | {r["count"]} | {len(r["tc_ids"].split(";"))} '
                 f'| {r["fields"]} |')
    L += ["", "## 5. Automation mapping (for the later script phase)", "",
          "| Channel | Helper | TC | Note |", "| --- | --- | ---: | --- |"]
    for ch in ("ADB", "RC", "UDS", "CAN", "HOST", "PHYS", "DOC"):
        note = {"PHYS": "manual step — the runner stops and prompts",
                "DOC": "document review — no execution generated"}.get(ch, "")
        L.append(f'| {ch} | `{HELPER.get(ch, "—")}` | {len(chan_tcs[ch])} | {note} |')
    L += ["",
          f"> Not a channel: {len(chan_tcs['PENDING-ASSET'])} test cases carry a placeholder "
          "command line (`<command provided by …>`, written as a `$` step) and cannot be "
          "automated until the asset arrives; see section 4."]
    L += ["", "Manual (PHYS) steps, verbatim:", "",
          bullet([f"`{p}` — {', '.join(sorted(set(v)))}" for p, v in sorted(phys_tcs.items())]),
          ""]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(L).rstrip() + "\n", encoding="utf-8")

    # --- ⊆ 驗證：指南內之每一 `$`／`Send CAN:` 反引號片段須為 TC 之指令 ---
    corpus = set(cmd_tcs)
    text = OUT.read_text(encoding="utf-8")
    lines = text.splitlines()
    # §1.6 之行區間自輸出檔重新定位（不靠寫入時之索引）
    a = lines.index("## 1.6 Environment knowledge (not from test cases)")
    b = lines.index("## 2. How to read observations")
    outside = "\n".join(lines[:a] + lines[b:])
    quoted = set(re.findall(r"`((?:\$ |Send CAN:)[^`]+)`", outside))
    missing = sorted(q for q in quoted if q not in corpus)
    # 第二項驗證：§1.6 每行（bullet）須含 ` — ` 之來源片段
    env_lines = [ln for ln in lines[a:b] if ln.startswith("- ")]
    env_bad = [ln[:60] for ln in env_lines if " — " not in ln]
    print(f"EXEC_GUIDE → {OUT.relative_to(ROOT)}")
    print(f"  TC {len(tcs)}；指令 {len(cmd_tcs)}；tag {len(tag_tcs)}；path {len(path_tcs)}；"
          f"artifact {len(art_tcs)}；runner class {len(instr_tcs)}")
    print(f"  通道 TC 數: " + ", ".join(f"{k}={len(chan_tcs[k])}" for k in
                                        ("ADB", "RC", "UDS", "CAN", "HOST", "PHYS", "DOC",
                                         "PENDING-ASSET")))
    for k, v in xc.items():
        print(f"  交叉核對 {k}：{v}")
    print(f"  ⊆ 驗證（§1.6 以外）：指南引用之指令 {len(quoted)}／全在 TC 內 = "
          f"{len(quoted) - len(missing)}（{'100%' if not missing else missing}）")
    print(f"  §1.6 來源驗證：{len(env_lines)} 行，含 ` — ` 來源片段 = "
          f"{len(env_lines) - len(env_bad)}（{'100%' if not env_bad else env_bad}）")
    return 1 if (missing or env_bad) else 0


if __name__ == "__main__":
    sys.exit(main())
