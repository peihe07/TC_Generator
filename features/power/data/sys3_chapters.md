# B3 — SYS3 SYSAD 章節結構（R-P20）

來源：`SYS3_CFTS_009_Power_Management_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.1.0.docx`（3,474,091 B，`cb6bf7d81030abc8…`，G0 相符，未重測）

> **章節號為推導值。** 本文件之標題不含字面章節號（Word 自動編號），故 §C rule 1 於本文件之匹配數為 **0**（G16）。下表之編號係依`Heading1` / `Heading2` 之出現順序推導，非文件內文字。

> 依 B3 禁區：本檔**不據此調整 §E 之任何分組**，僅取得素材。

## 完整章節清單

| 推導章節號 | pStyle | 標題 |
|---|---|---|
| §1 | Heading1 | 目的Purpose |
| §2 | Heading1 | 範圍Scope |
| §3 | Heading1 | 縮寫與定義 Abbreviations and definitions |
| §3.1 | Heading2 | 縮寫 Abbreviations |
| §3.2 | Heading2 | 定義 Definitions |
| §4 | Heading1 | 系統架構設計 System Architecture Design |
| §4.1 | Heading2 | 系統架構概述System Architecture Overview |
| §4.2 | Heading2 | 設計替代 Design Alternate |
| §4.3 | Heading2 | 系統需求 – 概述 System Requirements – Overview |
| §4.4 | Heading2 | Power States |
| §4.5 | Heading2 | Paramters |
| §4.6 | Heading2 | Special Mode Parameters |
| §4.7 | Heading2 | Timers |
| §4.8 | Heading2 | Feature Specific |
| §4.9 | Heading2 | 系統分解 System Decomposition |
| §4.10 | Heading2 | 假設與相依性Assumptions and Dependencies |
| §4.11 | Heading2 | Assumptions |
| §4.12 | Heading2 | 順序圖 Sequence Diagram |
| §4.13 | Heading2 | Start-Up sequence |
| §4.14 | Heading2 | Shutdown Sequence |
| §4.15 | Heading2 | Custom power state |
| §4.16 | Heading2 | Power State Transition |
| §4.17 | Heading2 | Power Mode Interruption Sequence |
| §4.18 | Heading2 | Phone Call |
| §4.19 | Heading2 | Disclaimer |
| §4.20 | Heading2 | Start-up Animation |
| §4.21 | Heading2 | Splash — Cold Boot |
| §4.22 | Heading2 | Splash — Warm Boot |
| §4.23 | Heading2 | Splash — Idle to Full Operation |
| §4.24 | Heading2 | Antitheft |
| §4.25 | Heading2 | Front Panel On Off Sequence |
| §4.26 | Heading2 | 系統架構設計System Architecture Design |
| §4.27 | Heading2 | 架構設計組件Architectural Design Components |
| §4.28 | Heading2 | 分配系統需求Allocate System Requirements |
| §4.29 | Heading2 | 動態行為 Dynamic Behavior |
| §4.30 | Heading2 | Sleep |
| §4.31 | Heading2 | Standby |
| §4.32 | Heading2 | Full Operation |
| §4.33 | Heading2 | Idle |
| §4.34 | Heading2 | Timed |
| §4.35 | Heading2 | Partial Operation |
| §4.36 | Heading2 | Bench |
| §5 | Heading1 | 接口說明Interface Description |
| §6 | Heading1 | IVI Power Mode through Custom Vehicle Property |
| §7 | Heading1 | Discrete Data Interface |
| §8 | Heading1 | 參考文檔 Reference Document |
| §9 | Heading1 | 工具 Tools |

## §4.x 元件分解（37 項）

§4 為「系統架構設計 System Architecture Design」，其下 36 個 Heading2：

- **§4.1** 系統架構概述System Architecture Overview
- **§4.2** 設計替代 Design Alternate
- **§4.3** 系統需求 – 概述 System Requirements – Overview
- **§4.4** Power States
- **§4.5** Paramters
- **§4.6** Special Mode Parameters
- **§4.7** Timers
- **§4.8** Feature Specific
- **§4.9** 系統分解 System Decomposition
- **§4.10** 假設與相依性Assumptions and Dependencies
- **§4.11** Assumptions
- **§4.12** 順序圖 Sequence Diagram
- **§4.13** Start-Up sequence
- **§4.14** Shutdown Sequence
- **§4.15** Custom power state
- **§4.16** Power State Transition
- **§4.17** Power Mode Interruption Sequence
- **§4.18** Phone Call
- **§4.19** Disclaimer
- **§4.20** Start-up Animation
- **§4.21** Splash — Cold Boot
- **§4.22** Splash — Warm Boot
- **§4.23** Splash — Idle to Full Operation
- **§4.24** Antitheft
- **§4.25** Front Panel On Off Sequence
- **§4.26** 系統架構設計System Architecture Design
- **§4.27** 架構設計組件Architectural Design Components
- **§4.28** 分配系統需求Allocate System Requirements
- **§4.29** 動態行為 Dynamic Behavior
- **§4.30** Sleep
- **§4.31** Standby
- **§4.32** Full Operation
- **§4.33** Idle
- **§4.34** Timed
- **§4.35** Partial Operation
- **§4.36** Bench
