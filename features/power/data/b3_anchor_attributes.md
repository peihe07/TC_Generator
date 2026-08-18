# B3 —— 成對／重複錨點之屬性查證（R-P135 / R-P136）

> 屬性取自 CFTS 本文錨點標頭（R-P17 之文字層，bold 層辨識錨點、plain 層取屬性）。
> **集合型屬性之次序不具語義**（`ECU:RRM, ETM, LTM` 與 `ECU:LTM, ETM, RRM` 視為相同）。
> **執行層未合併或拆分任何 TC**（19 §I）。
> 已抽出屬性之錨點數：**1052**

## 1. R-P135 —— `SWE-PM-038` 之三組成對錨點

### `4941727` vs `4941728` —— **屬性相異：Model Year**（內文逐字不同）

| 屬性 | `4941727` | `4941728` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, ETM, RRM | RRM, LTM, ETM | 是 |
| EE Architecture | Atlantis Mid, Atlantis High | Atlantis Mid, Atlantis High | 是 |
| Market | All | All | 是 |
| Model Year | （無） | 2017 | **否** |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

判定：**(b) 變體登載 —— 依 R-P135 須停並上繳，由 Pei 裁定是否合併**

### `4941729` vs `4941730` —— **屬性相異：Model Year、Radio、State**（內文逐字不同）

| 屬性 | `4941729` | `4941730` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, ETM, RRM | RRM, ETM, LTM | 是 |
| EE Architecture | Atlantis High, Atlantis Mid | Atlantis High, Atlantis Mid | 是 |
| Market | All | All | 是 |
| Model Year | （無） | 2017 | **否** |
| Radio | allSys, noSys | allSys | **否** |
| State | New | Under Review | **否** |

判定：**(b) 變體登載 —— 依 R-P135 須停並上繳，由 Pei 裁定是否合併**

### `4941735` vs `4941736` —— **屬性相異：Model Year、Radio、State**（內文逐字不同）

| 屬性 | `4941735` | `4941736` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, ETM, RRM | RRM, LTM, ETM | 是 |
| EE Architecture | Atlantis High, Atlantis Mid | Atlantis Mid, Atlantis High | 是 |
| Market | All | All | 是 |
| Model Year | （無） | 2017 | **否** |
| Radio | allSys, noSys | allSys | **否** |
| State | New | Under Review | **否** |

判定：**(b) 變體登載 —— 依 R-P135 須停並上繳，由 Pei 裁定是否合併**

## 2. R-P136 —— 跨章節逐字相同之三對錨點

### `4941692` vs `4941814` —— **屬性全同**（內文逐字相同）

| 屬性 | `4941692` | `4941814` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | RRM, ETM, LTM | LTM, RRM, ETM | 是 |
| EE Architecture | Atlantis Mid | Atlantis Mid | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

判定：(a) 同一適用範圍下之不同行為 —— 各自成條正確

### `4941693` vs `4941815` —— **屬性全同**（內文逐字相同）

| 屬性 | `4941693` | `4941815` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | RRM, LTM, ETM | RRM, LTM, ETM | 是 |
| EE Architecture | Atlantis Mid | Atlantis Mid | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

判定：(a) 同一適用範圍下之不同行為 —— 各自成條正確

### `4941695` vs `4941817` —— **屬性全同**（內文逐字相同）

| 屬性 | `4941695` | `4941817` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, ETM, RRM | LTM, RRM, ETM | 是 |
| EE Architecture | Atlantis Mid | Atlantis Mid | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

判定：(a) 同一適用範圍下之不同行為 —— 各自成條正確
