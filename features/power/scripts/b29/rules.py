#!/usr/bin/env python3
"""29 包（下放包 28「內容三項」）之改寫規則 —— 單一來源。

build 與 verify 皆 import 本模組，但 verify **不讀 plan.json 之結果值**，
而是自基底重新套用本模組後與輸出逐格比對，故規則實作若有誤，驗收會攤開。

三項來源：`docs/fw036/handoff/28_content.md` §二 A／B／C。
句式一律逐字取自該下放包與 `features/power/docs/internal_var_observability.md`，
表外之列不自創 —— 由 `unfit` 收集後上繳，分析層接手。
"""

from __future__ import annotations

import re

# --- 共用 --------------------------------------------------------------------

NUMBERED = re.compile(r"^\s*\d+[.)]")
NUM_PREFIX = re.compile(r"^(\s*\d+[.)]\s*)")
DOLLAR = re.compile(r"\$[^$]*\$")

# A：主詞 TLM→HU。`\b` 使 `TLM_Status`／`TLM_Display` 天然不命中
# （`_` 為 word 字元），`LTM` 亦不含 `TLM`，故白名單 2、3 由判準本身保證。
RE_TLM = re.compile(r"\bTLM\b")

# B-1 之設定名（HMI 條目名）。timeout 一名有 16 列既有前例
# （`Open the timeout setting entry in the TLM menu`），auto switch-on 無前例。
SETTING_NAME = {
    "Timeout1": "timeout setting",
    "SwitchOff_Timeout_Setting.Req": "timeout setting",
    "Auto_SwitchOn_Setting.Req": "auto switch-on setting",
}

PENDING_REMSTARTFAIL = "PENDING: DR-PW23 observation method for RemStartFail"


def mask_dollars(text: str) -> list[tuple[int, int]]:
    return [(m.start(), m.end()) for m in DOLLAR.finditer(text)]


def tlm_to_hu(text: str) -> str:
    """`TLM` → `HU`，但 `$…$` 內一律不動（白名單 2）。"""
    if not text:
        return text
    spans = mask_dollars(text)

    def repl(m: re.Match) -> str:
        if any(a <= m.start() < b for a, b in spans):
            return m.group(0)
        return "HU"

    return RE_TLM.sub(repl, text)


def split_body(line: str) -> tuple[str, str]:
    m = NUM_PREFIX.match(line)
    return (m.group(1), line[m.end():]) if m else ("", line)


# --- B／C：PROC 步驟 → 行為化（含其 ER 對應行）--------------------------------

_SET_ALT = "|".join(re.escape(k) for k in SETTING_NAME)
RE_SETTING_READ = re.compile(
    rf"^Read ({_SET_ALT})( on the ex-factory unit)? and check that it is (.+)$")
RE_ANTITHEFT_READ = re.compile(
    r"^Read Antitheft_Activation\.Req and check that it is (True|False)$")
RE_VPLAST_READ = re.compile(
    r"^Read VPLastStatus( on the ex-factory unit)? and check that it is "
    r"(ON|On|OFF|Off)$")
RE_PHONE_READ = re.compile(
    r"^Read Phone_Call\.Info and check that it is (Active|Not_Active)$")
RE_REARCAM_READ = re.compile(
    r"^Read Rear_Camera_Enable\.Info and check that it is (True|False)$")
RE_REMSTART_READ = re.compile(
    r"^Read RemStartFail and check that it is (True|False)$")
RE_FRONT_PANEL = re.compile(
    r"^Drive Front_Panel_OnOff\.Req from Not_Pressed to Pressed$")

VPLAST_SIGNAL = "$STATUS_BH_BCM1.OperationalModeSts$ = 4 (Ignition_On)"


def rewrite_proc(body: str) -> tuple[str, str, str] | None:
    """回傳 `(新 proc 行, 新 er 行, 規則代號)`；不套用者回傳 None。"""
    m = RE_SETTING_READ.match(body)
    if m:
        var, qual, value = m.group(1), m.group(2) or "", m.group(3)
        name = SETTING_NAME[var]
        return (f"Open the {name} entry in the HU menu{qual} and read the "
                f"{name} value and check that it is {value}",
                f"The {name} value is {value}", "B1")

    m = RE_ANTITHEFT_READ.match(body)
    if m:
        if m.group(1) == "True":
            return ("Press the HU power button and check that the Antitheft "
                    "HMI screen is shown",
                    "The Antitheft HMI screen is shown", "B2")
        return ("Press the HU power button and check that the HU powers up "
                "without the Antitheft HMI screen",
                "The HU powers up without the Antitheft HMI screen", "B2")

    m = RE_VPLAST_READ.match(body)
    if m:
        qual = m.group(1) or ""
        if m.group(2).upper() == "ON":
            return (f"Send the signal {VPLAST_SIGNAL}{qual} and check that the "
                    f"HU powers up automatically and shows the splash screen",
                    "The HU powers up automatically and shows the splash "
                    "screen", "B3")
        return (f"Send the signal {VPLAST_SIGNAL}{qual} and check that the HU "
                f"does not power up automatically",
                "The HU does not power up automatically", "B3")

    m = RE_PHONE_READ.match(body)
    if m:
        if m.group(1) == "Active":
            return ("Place a phone call from the paired device and check that "
                    "the call screen is shown",
                    "The call screen is shown", "B4")
        return ("End the call and check that the call screen is dismissed",
                "The call screen is dismissed", "B4")

    m = RE_REARCAM_READ.match(body)
    if m:
        neg = "" if m.group(1) == "True" else " not"
        return (f"Read the HU screen and check that the rear view camera image "
                f"is{neg} shown",
                f"The rear view camera image is{neg} shown on the HU screen",
                "B5")

    if RE_REMSTART_READ.match(body):
        return (PENDING_REMSTARTFAIL, PENDING_REMSTARTFAIL, "B6")

    if RE_FRONT_PANEL.match(body):
        return ("Press the HU power button",
                "The HU power button press is registered", "C")

    return None


# --- B-1：PRE 之設定宣告 ------------------------------------------------------

RE_SETTING_PRE = re.compile(
    rf"^({_SET_ALT}) is (?:configured to )?(.+)$")


def rewrite_pre(body: str) -> tuple[str, str] | None:
    """設定類前提 → `HMI: "<setting>" is set to <V>`；其餘一律不動。"""
    m = RE_SETTING_PRE.match(body)
    if not m:
        return None
    var, value = m.group(1), m.group(2)
    # 「holds a known value」「held a known value before …」非具體值，套不進
    if value.startswith("a known value") or value.startswith("set to "):
        return None
    return (f'HMI: "{SETTING_NAME[var]}" is set to {value}', "B1-pre")


# --- 表外殘留之偵測（上繳清單用）---------------------------------------------

TARGET_VARS = (
    "Timeout1", "SwitchOff_Timeout_Setting.Req", "Auto_SwitchOn_Setting.Req",
    "Antitheft_Activation.Req", "VPLastStatus", "Phone_Call.Info",
    "Rear_Camera_Enable.Info", "RemStartFail", "Antitheft_Result.Info",
    "Front_Panel_OnOff.Req",
)
RE_TARGET = re.compile("|".join(re.escape(v) for v in TARGET_VARS))
