# Audio Management — 下放包 02：Framework 鎖定與 317 葉逐條歸位

- Feature slug：`audio_mgmt`
- 日期：2026-08-26
- 依據：01 包 R-AM1–R-AM7；IN §4.1
- 掃描聲明：本表為 SWE.1 全 318 列（317 唯一 SWE ID）之全表掃描產出，
  無抽樣、無概估；每葉恰歸一集，UNMAPPED = 0。

## 一、Layer 2 定案（11 集）與分佈

| Test Set | 葉數 | Layer 3（CFTS 章節，不入簿） |
|---|---|---|
| Audio Sources | 37 | 1.3.1.1–1.3.1.3 |
| Source Transition | 34 | 1.3.3.15, 1.3.3.19 |
| Audio Arbitration | 29 | 1.3.3.1–1.3.3.4, 1.3.3.17, 1.3.3.18 |
| Focus and Ducking | 18 | 1.3.2.14, 1.3.3 混合（Focus/Ducking/Mixing） |
| Mute Requests | 32 | 1.3.3.5–1.3.3.7, 1.3.3.12 |
| Volume Control | 50 | 1.3.2.10–1.3.2.12 |
| Tones and Alerts | 32 | 1.3.1.4–1.3.1.6, 1.3.2.6 |
| Audio Processing | 34 | 1.3.2.7–1.3.2.9, 1.3.2.15, 1.3.2.17–1.3.2.22 |
| Surround and Fade | 24 | 1.3.2.13, 1.3.2.16 |
| Power and Persistence | 25 | 1.3.2.2–1.3.2.4＋Volume Restoration／Persistent Storage 群 |
| Logistic Mode | 3 | 1.3.5.1–1.3.5.2 |

與 01 包草案之差異（兩處）：
1. 原 `Source Arbitration`（81 葉）依 §4.1.3 過粗判準三分為
   `Source Transition`（34）／`Audio Arbitration`（29）／`Focus and Ducking`（18）。
   三集各有明確共用 setup 型（轉換場景／優先權事件表／焦點申請）。
2. 原 `Projection Audio` 集**撤銷**：全表掃描實測 0 葉提及
   CarPlay／Android Auto／Projection。CFTS 1.3.3.11（Carplay Alternate
   Audio）與 1.3.3.14（Android Auto Certification）在本 SWE.1 無對應葉，
   該二章節由 Projection feature 之需求命名空間（SWE1-PROJ）承接，
   屬跨 feature 分工而非 coverage gap；於交付揭露表加註一行。

## 二、317 葉逐條歸位表

欄位：SWE ID｜Source ID｜Title（截 58 字）｜SWE.1 子類｜Test Set。
SWE1_AMM_076 兩列均列（R-AM6：交付欄均照抄 SWE1_AMM_076，
內部代號 076a=SYS-RA-AMM-242、076b=SYS-RA-AMM-246 僅限本文件層）。

| SWE ID | Source ID | Title | SWE.1 子類 | Test Set |
|---|---|---|---|---|
| SWE1_AMM_001 | SYS-RA-AMM-082 | Entertainment Stereo Output Configuration | Audio Policy | Audio Sources |
| SWE1_AMM_002 | SYS-RA-AMM-083 | Entertainment Channel Routing | Audio Routing | Audio Sources |
| SWE1_AMM_003 | SYS-RA-AMM-084 | Entertainment Playback State Handling | Source Management | Audio Sources |
| SWE1_AMM_005 | SYS-RA-AMM-086 | Entertainment Source Classification | Source Configuration | Audio Sources |
| SWE1_AMM_006 | SYS-RA-AMM-087 | TA/PTY31 Entertainment Source Classification | Audio Policy | Audio Sources |
| SWE1_AMM_007 | SYS-RA-AMM-095 | Information Source Mono Configuration | Audio Policy | Audio Sources |
| SWE1_AMM_009 | SYS-RA-AMM-098 | Information 1 Source Routing | Audio Routing | Audio Sources |
| SWE1_AMM_010 | SYS-RA-AMM-100 | Information 2 Source Routing | Audio Routing | Audio Sources |
| SWE1_AMM_013 | SYS-RA-AMM-122 | Confirmation Tone Front Channel Routing | Audio Routing | Audio Sources |
| SWE1_AMM_020 | SYS-RA-AMM-131 | Alert Front Channel Routing | Audio Routing | Audio Sources |
| SWE1_AMM_024 | SYS-RA-AMM-140 | External Amplifier Audio Output Mapping | Audio Routing | Audio Sources |
| SWE1_AMM_108 | SYS-RA-AMM-311 | Audio Channel Assignment | Audio Routing | Audio Sources |
| SWE1_AMM_122 | SYS-RA-AMM-339 | Audio Routing Table Compliance | Audio Routing | Audio Sources |
| SWE1_AMM_145 | SYS-RA-AMM-379 | Applied Channel Ramp-Down | Audio Routing | Audio Sources |
| SWE1_AMM_146 | SYS-RA-AMM-380 | Remaining Channel Volume Adjustment | Audio Routing | Audio Sources |
| SWE1_AMM_148 | SYS-RA-AMM-383 | Information Source Active Status Update | Information Source | Audio Sources |
| SWE1_AMM_149 | SYS-RA-AMM-384 | Information Source Type Update | Information Source | Audio Sources |
| SWE1_AMM_151 | SYS-RA-AMM-387 | Information 2 Active Status Update | Information Source | Audio Sources |
| SWE1_AMM_152 | SYS-RA-AMM-388 | Information 2 Type Update | Information Source | Audio Sources |
| SWE1_AMM_155 | SYS-RA-AMM-391 | Information Channel Ramp-Up | Audio Routing | Audio Sources |
| SWE1_AMM_162 | SYS-RA-AMM-406 | Information 1 Deactivation Status | Information Source | Audio Sources |
| SWE1_AMM_163 | SYS-RA-AMM-407 | Information 1 Type Reset | Information Source | Audio Sources |
| SWE1_AMM_164 | SYS-RA-AMM-409 | Information 2 Deactivation Status | Information Source | Audio Sources |
| SWE1_AMM_165 | SYS-RA-AMM-410 | Information 2 Type Reset | Information Source | Audio Sources |
| SWE1_AMM_175 | SYS-RA-AMM-489 | Store Audio Settings Before Front/Rear Speaker Routing | Audio Routing | Audio Sources |
| SWE1_AMM_176 | SYS-RA-AMM-492 | Restore Audio Settings After Routing | Audio Routing | Audio Sources |
| SWE1_AMM_202 | SYS-RA-AMM-533 | Source Status Update After Activation | Source Management | Audio Sources |
| SWE1_AMM_204 | SYS-RA-AMM-535 | Source Status Update After Deactivation | Source Management | Audio Sources |
| SWE1_AMM_207 | SYS-RA-AMM-540 | HUModeStatus Update After Entertainment Transition | Source Management | Audio Sources |
| SWE1_AMM_210 | SYS-RA-AMM-547 | Reset Source Status When No Source Is Active | Source Management | Audio Sources |
| SWE1_AMM_214 | SYS-RA-AMM-551 | HFP Information Source Activation | Information Source Management | Audio Sources |
| SWE1_AMM_217 | SYS-RA-AMM-554 | HFP Information Source Deactivation | Information Source Management | Audio Sources |
| SWE1_AMM_228 | SYS-RA-AMM-574 | HFP Routing During Navigation Prompt | Audio Routing | Audio Sources |
| SWE1_AMM_256 | SYS-RA-AMM-779 | Configure Driver Side Audio for LHD | Audio Routing | Audio Sources |
| SWE1_AMM_257 | SYS-RA-AMM-780 | Configure Driver Side Audio for RHD | Audio Routing | Audio Sources |
| SWE1_AMM_263 | SYS-RA-AMM-792 | Mute Rear Speaker Channels | Audio Routing | Audio Sources |
| SWE1_AMM_311 | SYS-RA-AMM-1095 | Navigation Audio Priority During Phone Audio | Audio Routing | Audio Sources |
| SWE1_AMM_132 | SYS-RA-AMM-359 | Active Media Operation Cancellation | Source Transition | Source Transition |
| SWE1_AMM_133 | SYS-RA-AMM-360 | Entertainment Audio Ramp-Down | Source Transition | Source Transition |
| SWE1_AMM_134 | SYS-RA-AMM-361 | Entertainment Source Activation | Source Transition | Source Transition |
| SWE1_AMM_135 | SYS-RA-AMM-362 | Entertainment Mute Hold Timing | Source Transition | Source Transition |
| SWE1_AMM_136 | SYS-RA-AMM-363 | Entertainment Source Status Update | Source Transition | Source Transition |
| SWE1_AMM_137 | SYS-RA-AMM-364 | Entertainment Audio Ramp-Up | Source Transition | Source Transition |
| SWE1_AMM_138 | SYS-RA-AMM-365 | Entertainment Source Transition Timing | Source Transition | Source Transition |
| SWE1_AMM_142 | SYS-RA-AMM-374 | Entertainment Media Pause Handling | Source Transition | Source Transition |
| SWE1_AMM_143 | SYS-RA-AMM-375 | Active Media Function Cancellation | Source Transition | Source Transition |
| SWE1_AMM_144 | SYS-RA-AMM-376 | Entertainment Audio Ramp-Down During Deactivation | Source Transition | Source Transition |
| SWE1_AMM_154 | SYS-RA-AMM-390 | Information Audio Ramp-Up | Source Transition | Source Transition |
| SWE1_AMM_156 | SYS-RA-AMM-397 | Entertainment to Information Transition Timing | Source Transition | Source Transition |
| SWE1_AMM_157 | SYS-RA-AMM-398 | Information 1 to Information 2 Transition Timing | Source Transition | Source Transition |
| SWE1_AMM_159 | SYS-RA-AMM-402 | Information Source Ramp-Down | Source Transition | Source Transition |
| SWE1_AMM_169 | SYS-RA-AMM-453 | Signal Source Ramp-Up | Audio Transition | Source Transition |
| SWE1_AMM_200 | SYS-RA-AMM-530 | Non-Arbitrated Source Transition | Source Transition | Source Transition |
| SWE1_AMM_201 | SYS-RA-AMM-532 | Initial Audio Ramp-Up | Audio Transition | Source Transition |
| SWE1_AMM_203 | SYS-RA-AMM-534 | Source Ramp Down on Deactivation | Audio Transition | Source Transition |
| SWE1_AMM_205 | SYS-RA-AMM-537 | Entertainment-to-Entertainment Source Transition | Source Transition | Source Transition |
| SWE1_AMM_206 | SYS-RA-AMM-539 | Entertainment Source Ramp Down Before Switching | Audio Transition | Source Transition |
| SWE1_AMM_208 | SYS-RA-AMM-541 | Entertainment Source Transition Delay | Audio Transition | Source Transition |
| SWE1_AMM_209 | SYS-RA-AMM-542 | Entertainment Source Ramp Up After Transition | Audio Transition | Source Transition |
| SWE1_AMM_212 | SYS-RA-AMM-549 | Entertainment Source Activation | Source Activation | Source Transition |
| SWE1_AMM_213 | SYS-RA-AMM-550 | TA/PTY31 Source Activation | Source Activation | Source Transition |
| SWE1_AMM_216 | SYS-RA-AMM-553 | Entertainment Source Deactivation | Source Deactivation | Source Transition |
| SWE1_AMM_223 | SYS-RA-AMM-565 | Passenger Side Entertainment Activation After Information | Audio Transition | Source Transition |
| SWE1_AMM_224 | SYS-RA-AMM-568 | Information Source Transition | Information Source Transition | Source Transition |
| SWE1_AMM_225 | SYS-RA-AMM-570 | Restore Entertainment After Information Source Ends | Information Source Recovery | Source Transition |
| SWE1_AMM_240 | SYS-RA-AMM-614 | Arbitrated Signal Source Transition | Source Transition | Source Transition |
| SWE1_AMM_241 | SYS-RA-AMM-616 | Arbitrated Information Source Transition | Source Transition | Source Transition |
| SWE1_AMM_275 | SYS-RA-AMM-840 | Entertainment Ramp-Up Timing | Audio Transition | Source Transition |
| SWE1_AMM_276 | SYS-RA-AMM-841 | Entertainment Ramp-Down Timing | Audio Transition | Source Transition |
| SWE1_AMM_277 | SYS-RA-AMM-842 | Information Source Ramp-Up Timing | Audio Transition | Source Transition |
| SWE1_AMM_278 | SYS-RA-AMM-843 | Information Source Ramp-Down Timing | Audio Transition | Source Transition |
| SWE1_AMM_123 | SYS-RA-AMM-345 | Signal Source Priority Selection | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_124 | SYS-RA-AMM-346 | Higher Priority Source Arbitration | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_129 | SYS-RA-AMM-351 | Deferred Source Activation | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_130 | SYS-RA-AMM-356 | Audio Source Queue Management | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_139 | SYS-RA-AMM-370 | Audio Request Queue Management | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_166 | SYS-RA-AMM-411 | Next Priority Source Activation | Source Arbitration | Audio Arbitration |
| SWE1_AMM_167 | SYS-RA-AMM-443 | Next Priority Source Re-Mix | Source Arbitration | Audio Arbitration |
| SWE1_AMM_189 | SYS-RA-AMM-513 | TBM Priority-Based Source Muting | Source Arbitration | Audio Arbitration |
| SWE1_AMM_198 | SYS-RA-AMM-523 | SOS Call Audio Priority Handling | Source Arbitration | Audio Arbitration |
| SWE1_AMM_199 | SYS-RA-AMM-524 | Restore Audio After SOS Call | Source Arbitration | Audio Arbitration |
| SWE1_AMM_211 | SYS-RA-AMM-548 | Source Activation Conditions | Source Arbitration | Audio Arbitration |
| SWE1_AMM_215 | SYS-RA-AMM-552 | Source Activation Arbitration | Source Arbitration | Audio Arbitration |
| SWE1_AMM_218 | SYS-RA-AMM-555 | SOS Call Priority Mute | Audio Arbitration / Emergency Handling | Audio Arbitration |
| SWE1_AMM_219 | SYS-RA-AMM-556 | Restore Audio After SOS Call | Audio Arbitration / Recovery | Audio Arbitration |
| SWE1_AMM_226 | SYS-RA-AMM-572 | Cancel TA/Navigation During Phone or VR Request | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_227 | SYS-RA-AMM-573 | Cancel TA on Incoming Call | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_229 | SYS-RA-AMM-576 | Ignore TA During Active VR Session | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_230 | SYS-RA-AMM-578 | Cancel VR for User-Selected Navigation Prompt | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_231 | SYS-RA-AMM-579 | Delay Navigation During Active VR Session | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_232 | SYS-RA-AMM-581 | Ignore TA During Active Phone Audio | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_234 | SYS-RA-AMM-592 | Cancel TA or Navigation for Phone/VR Request | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_235 | SYS-RA-AMM-593 | Cancel TA on Incoming Call | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_236 | SYS-RA-AMM-595 | Ignore TA During Active VR Session | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_237 | SYS-RA-AMM-596 | Cancel VR for Customer-Selected Navigation Prompt | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_238 | SYS-RA-AMM-597 | Delay Navigation Until VR Completion | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_239 | SYS-RA-AMM-599 | Ignore TA During Phone Audio | Audio Arbitration | Audio Arbitration |
| SWE1_AMM_259 | SYS-RA-AMM-787 | Handle Invalid Cabin EQ IDs (S00 / SFF) | Fault Handling | Audio Arbitration |
| SWE1_AMM_260 | SYS-RA-AMM-788 | Handle Unknown Cabin EQ IDs | Fault Handling | Audio Arbitration |
| SWE1_AMM_310 | SYS-RA-AMM-1094 | VR Session Cancellation on Call Initiation | Voice Recognition | Audio Arbitration |
| SWE1_AMM_004 | SYS-RA-AMM-085 | Entertainment Audio Priority Handling | Audio Focus | Focus and Ducking |
| SWE1_AMM_008 | SYS-RA-AMM-097 | Information Source Audio Focus Priority | Audio Focus | Focus and Ducking |
| SWE1_AMM_014 | SYS-RA-AMM-123 | Confirmation Tone Mixing with ENT and INFO1 | Audio Mixing | Focus and Ducking |
| SWE1_AMM_015 | SYS-RA-AMM-124 | Confirmation Tone Suppression on INFO2 | Audio Mixing | Focus and Ducking |
| SWE1_AMM_030 | SYS-RA-AMM-173 | Audio Source Priority Arbitration | Audio Focus | Focus and Ducking |
| SWE1_AMM_031 | SYS-RA-AMM-178 | INFO2 Priority and Entertainment Interruption | Audio Focus | Focus and Ducking |
| SWE1_AMM_032 | SYS-RA-AMM-179 | INFO2 Source Priority Handling | Audio Focus | Focus and Ducking |
| SWE1_AMM_086 | SYS-RA-AMM-272 | Audio Source Priority Management | Audio Focus | Focus and Ducking |
| SWE1_AMM_233 | SYS-RA-AMM-583 | Mix Signal Source with Active Information Sources | Audio Mixing | Focus and Ducking |
| SWE1_AMM_286 | SYS-RA-AMM-895 | Alternate and Main Audio Mixing | Audio Mixing | Focus and Ducking |
| SWE1_AMM_287 | SYS-RA-AMM-896 | Main Audio Ducking for Alternate Audio | Audio Ducking | Focus and Ducking |
| SWE1_AMM_309 | SYS-RA-AMM-1089 | User Playback Interruption during HFP Call | Audio Focus | Focus and Ducking |
| SWE1_AMM_312 | SYS-RA-AMM-1106 | Fixed Navigation Entertainment Fade-Out | Audio Ducking | Focus and Ducking |
| SWE1_AMM_313 | SYS-RA-AMM-1107 | Relative Navigation Entertainment Fade-Out | Audio Ducking | Focus and Ducking |
| SWE1_AMM_314 | SYS-RA-AMM-1108 | Navigation Entertainment Attenuation | Audio Ducking | Focus and Ducking |
| SWE1_AMM_315 | SYS-RA-AMM-1109 | Entertainment Mute at Minimum Attenuated Volume | Audio Ducking | Focus and Ducking |
| SWE1_AMM_316 | SYS-RA-AMM-1110 | Adjusted Entertainment Volume Transmission During Navigati | Audio Ducking | Focus and Ducking |
| SWE1_AMM_317 | SYS-RA-AMM-1111 | Navigation Volume Adjustment Synchronization | Audio Ducking | Focus and Ducking |
| SWE1_AMM_027 | SYS-RA-AMM-160 | TLM Idle State Mute Handling | Mute Control | Mute Requests |
| SWE1_AMM_028 | SYS-RA-AMM-170 | TLM Operational State Unmute Handling | Mute Control | Mute Requests |
| SWE1_AMM_058 | SYS-RA-AMM-223 | Entertainment Mute Status Communication | Mute Control | Mute Requests |
| SWE1_AMM_059 | SYS-RA-AMM-224 | ENTMuted Source Scope | Mute Status | Mute Requests |
| SWE1_AMM_060 | SYS-RA-AMM-225 | Entertainment Mute Toggle Request Handling | Mute Control | Mute Requests |
| SWE1_AMM_061 | SYS-RA-AMM-226 | Power Button Mute Handling | Mute Control | Mute Requests |
| SWE1_AMM_066 | SYS-RA-AMM-231 | Entertainment Mute Status Synchronization | Mute Control | Mute Requests |
| SWE1_AMM_068 | SYS-RA-AMM-233 | TLM Mute Switch Handling without ICS Node | Mute Control | Mute Requests |
| SWE1_AMM_069 | SYS-RA-AMM-234 | TLM Entertainment Mute Request Handling | Mute Control | Mute Requests |
| SWE1_AMM_070 | SYS-RA-AMM-235 | Internal Mute State Preservation and Restoration | Mute Control | Mute Requests |
| SWE1_AMM_071 | SYS-RA-AMM-236 | Entertainment Mute Release on Volume Adjustment | Mute Control | Mute Requests |
| SWE1_AMM_076 | SYS-RA-AMM-246 | Information Source Mute Routing Configuration | Mute Control | Mute Requests |
| SWE1_AMM_078 | SYS-RA-AMM-248 | Ignore Information Mute Request Without ICS | Mute Control | Mute Requests |
| SWE1_AMM_079 | SYS-RA-AMM-249 | Ignore Information Mute Status Event Without ICS | Mute Control | Mute Requests |
| SWE1_AMM_179 | SYS-RA-AMM-501 | VSIM Entertainment Mute Handling | Mute Management | Mute Requests |
| SWE1_AMM_180 | SYS-RA-AMM-502 | VSIM Information 1 Mute Handling | Mute Management | Mute Requests |
| SWE1_AMM_181 | SYS-RA-AMM-503 | VSIM Information 2 Mute Handling | Mute Management | Mute Requests |
| SWE1_AMM_182 | SYS-RA-AMM-504 | VSIM Hands-Free Microphone Mute | Mute Management | Mute Requests |
| SWE1_AMM_184 | SYS-RA-AMM-507 | VSIM Entertainment Unmute Handling | Mute Management | Mute Requests |
| SWE1_AMM_185 | SYS-RA-AMM-508 | VSIM Information 1 Unmute Handling | Mute Management | Mute Requests |
| SWE1_AMM_186 | SYS-RA-AMM-509 | VSIM Information 2 Unmute Handling | Mute Management | Mute Requests |
| SWE1_AMM_187 | SYS-RA-AMM-510 | VSIM Hands-Free Microphone Unmute | Mute Management | Mute Requests |
| SWE1_AMM_191 | SYS-RA-AMM-515 | Entertainment Mute Status Update During TBM Mute | Mute Management | Mute Requests |
| SWE1_AMM_192 | SYS-RA-AMM-516 | TBM Information 1 Volume Suppression | Mute Management | Mute Requests |
| SWE1_AMM_193 | SYS-RA-AMM-517 | TBM Information 2 Volume Suppression | Mute Management | Mute Requests |
| SWE1_AMM_195 | SYS-RA-AMM-520 | Entertainment Mute Status Clear | Mute Management | Mute Requests |
| SWE1_AMM_288 | SYS-RA-AMM-900 | Reverse Entertainment Audio Mute Handling | Mute Control | Mute Requests |
| SWE1_AMM_289 | SYS-RA-AMM-901 | VR Request Suppression in Reverse | VR Control | Mute Requests |
| SWE1_AMM_290 | SYS-RA-AMM-902 | Entertainment Audio Restoration after Reverse | Mute Control | Mute Requests |
| SWE1_AMM_291 | SYS-RA-AMM-903 | VR Request Resumption after Reverse | VR Control | Mute Requests |
| SWE1_AMM_295 | SYS-RA-AMM-943 | Reverse Mute Disable Configuration | Reverse Mute Control | Mute Requests |
| SWE1_AMM_296 | SYS-RA-AMM-945 | Reverse Mute Default Disable Handling | Reverse Mute Control | Mute Requests |
| SWE1_AMM_026 | SYS-RA-AMM-149 | Target Volume Request Handling | Volume Control | Volume Control |
| SWE1_AMM_044 | SYS-RA-AMM-197 | Equalizer HMI Update Handling | HMI | Volume Control |
| SWE1_AMM_050 | SYS-RA-AMM-206 | Independent Source Volume Control | Volume Control | Volume Control |
| SWE1_AMM_051 | SYS-RA-AMM-207 | Source Volume Control Availability | Volume Control | Volume Control |
| SWE1_AMM_053 | SYS-RA-AMM-215 | Active Source Volume Adjustment Selection | Volume Control | Volume Control |
| SWE1_AMM_054 | SYS-RA-AMM-217 | Entertainment Volume Communication | Volume Control Interface | Volume Control |
| SWE1_AMM_055 | SYS-RA-AMM-218 | Information 1 Volume Communication | Volume Control Interface | Volume Control |
| SWE1_AMM_056 | SYS-RA-AMM-219 | Information 2 Volume Communication | Volume Control Interface | Volume Control |
| SWE1_AMM_063 | SYS-RA-AMM-228 | Entertainment Volume Knob Handling | Volume Control | Volume Control |
| SWE1_AMM_064 | SYS-RA-AMM-229 | Entertainment Volume Up/Down Request Handling | Volume Control | Volume Control |
| SWE1_AMM_065 | SYS-RA-AMM-230 | Entertainment Volume Status Synchronization | Volume Control Interface | Volume Control |
| SWE1_AMM_067 | SYS-RA-AMM-232 | Minimum Entertainment Volume Handling | Volume Control | Volume Control |
| SWE1_AMM_072 | SYS-RA-AMM-238 | Independent Information Source Volume Control | Volume Control | Volume Control |
| SWE1_AMM_073 | SYS-RA-AMM-239 | Information 1 Volume Status Communication | Volume Control Interface | Volume Control |
| SWE1_AMM_074 | SYS-RA-AMM-240 | Information 2 Volume Status Communication | Volume Control Interface | Volume Control |
| SWE1_AMM_075 | SYS-RA-AMM-241 | Information Volume Knob Handling | Volume Control | Volume Control |
| SWE1_AMM_076 | SYS-RA-AMM-242 | Steering Wheel Information Volume Control | Volume Control | Volume Control |
| SWE1_AMM_077 | SYS-RA-AMM-247 | Information Source Minimum Volume Communication | Volume Control | Volume Control |
| SWE1_AMM_081 | SYS-RA-AMM-265 | Default Speed Controlled Volume Setting for NAFTA Markets | Speed Volume Control | Volume Control |
| SWE1_AMM_082 | SYS-RA-AMM-266 | Default Speed Controlled Volume Setting for Non-NAFTA Mark | Speed Volume Control | Volume Control |
| SWE1_AMM_083 | SYS-RA-AMM-267 | Speed Controlled Volume Availability | Speed Volume Control | Volume Control |
| SWE1_AMM_084 | SYS-RA-AMM-268 | Speed Controlled Volume Level Selection | Speed Volume Control | Volume Control |
| SWE1_AMM_085 | SYS-RA-AMM-269 | Speed Controlled Volume Setting Update | Speed Volume Control | Volume Control |
| SWE1_AMM_087 | SYS-RA-AMM-273 | Volume and Mute Control Routing | Volume Control | Volume Control |
| SWE1_AMM_088 | SYS-RA-AMM-277 | Speed Controlled Volume Enable Control | Speed Volume Control | Volume Control |
| SWE1_AMM_089 | SYS-RA-AMM-279 | Speed Controlled Volume Disable Processing | Speed Volume Control | Volume Control |
| SWE1_AMM_090 | SYS-RA-AMM-280 | Speed Controlled Volume Enable Processing | Speed Volume Control | Volume Control |
| SWE1_AMM_091 | SYS-RA-AMM-283 | Speed Controlled Volume Setting Configuration | Speed Volume Control | Volume Control |
| SWE1_AMM_114 | SYS-RA-AMM-321 | Fade and Balance HMI Update | HMI | Volume Control |
| SWE1_AMM_119 | SYS-RA-AMM-326 | Fade and Balance Display Synchronization | HMI | Volume Control |
| SWE1_AMM_141 | SYS-RA-AMM-372 | Display Settings Persistence | Display Settings | Volume Control |
| SWE1_AMM_147 | SYS-RA-AMM-381 | Information Volume Recall | Volume Management | Volume Control |
| SWE1_AMM_150 | SYS-RA-AMM-385 | Information Source Volume Signal Update | Volume Management | Volume Control |
| SWE1_AMM_153 | SYS-RA-AMM-389 | Information 2 Volume Signal Update | Volume Management | Volume Control |
| SWE1_AMM_158 | SYS-RA-AMM-401 | Current Volume Persistence | Volume Management | Volume Control |
| SWE1_AMM_183 | SYS-RA-AMM-505 | VSIM Entertainment Mute Indication | HMI Update | Volume Control |
| SWE1_AMM_190 | SYS-RA-AMM-514 | Entertainment Volume Reset During TBM Mute | Volume Management | Volume Control |
| SWE1_AMM_194 | SYS-RA-AMM-519 | Entertainment Volume Restoration After TBM | Volume Management | Volume Control |
| SWE1_AMM_196 | SYS-RA-AMM-521 | Information 1 Volume Restoration | Volume Management | Volume Control |
| SWE1_AMM_197 | SYS-RA-AMM-522 | Information 2 Volume Restoration | Volume Management | Volume Control |
| SWE1_AMM_220 | SYS-RA-AMM-561 | Navigation Volume Adjustment | Volume Management | Volume Control |
| SWE1_AMM_262 | SYS-RA-AMM-791 | Disable Fade Control for Two-Speaker Systems | HMI Configuration | Volume Control |
| SWE1_AMM_264 | SYS-RA-AMM-798 | Enable Surround Sound HMI | HMI Configuration | Volume Control |
| SWE1_AMM_266 | SYS-RA-AMM-800 | Disable Surround Sound Feature | HMI Configuration | Volume Control |
| SWE1_AMM_272 | SYS-RA-AMM-836 | Entertainment Key Volume Upper Limit | Volume Management | Volume Control |
| SWE1_AMM_273 | SYS-RA-AMM-837 | HFP Maximum Volume Limit | Volume Management | Volume Control |
| SWE1_AMM_274 | SYS-RA-AMM-838 | HFP Minimum Volume Limit | Volume Management | Volume Control |
| SWE1_AMM_306 | SYS-RA-AMM-1084 | Default Alert Volume during Active Cabin Audio | Alert Volume | Volume Control |
| SWE1_AMM_307 | SYS-RA-AMM-1085 | Default Alert Volume for Inactive Cabin Audio | Alert Volume | Volume Control |
| SWE1_AMM_308 | SYS-RA-AMM-1087 | Speed Volume Control Disable Handling | Speed Volume Control | Volume Control |
| SWE1_AMM_011 | SYS-RA-AMM-101 | VR Confirmation Tone Playback | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_012 | SYS-RA-AMM-102 | Common VR Tone Resource Handling | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_017 | SYS-RA-AMM-126 | Confirmation Tone Event Classification | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_018 | SYS-RA-AMM-127 | Confirmation Tone Parameter Handling | Tone Generation | Tones and Alerts |
| SWE1_AMM_019 | SYS-RA-AMM-128 | Conf3 Pulse Sequence Handling | Tone Generation | Tones and Alerts |
| SWE1_AMM_021 | SYS-RA-AMM-132 | Entertainment and Information Alert Generation | Alert Generation | Tones and Alerts |
| SWE1_AMM_022 | SYS-RA-AMM-134 | Information Alert Type Mapping | Alert Mapping | Tones and Alerts |
| SWE1_AMM_023 | SYS-RA-AMM-135 | Alert Tone Parameter Handling | Alert Generation | Tones and Alerts |
| SWE1_AMM_033 | SYS-RA-AMM-181 | Touchscreen Confirmation Tone Triggering | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_034 | SYS-RA-AMM-182 | Confirmation Tone Type Handling | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_036 | SYS-RA-AMM-184 | Confirmation Tone Retrigger Prevention | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_037 | SYS-RA-AMM-185 | Key Press Acceptance Tone Selection | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_038 | SYS-RA-AMM-186 | Key Press Rejection Tone Selection | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_039 | SYS-RA-AMM-187 | Key Press Set Tone Selection | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_040 | SYS-RA-AMM-188 | Entertainment and Information Alert Generation | Alert Generation | Tones and Alerts |
| SWE1_AMM_080 | SYS-RA-AMM-263 | Alert Audio Mixing for CAN Amplified Systems | Alert Generation | Tones and Alerts |
| SWE1_AMM_106 | SYS-RA-AMM-305 | Confirmation Tone Front Speaker Routing | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_107 | SYS-RA-AMM-308 | Alert Front Speaker Routing | Alerts | Tones and Alerts |
| SWE1_AMM_127 | SYS-RA-AMM-349 | Alert Priority Arbitration | Alert Management | Tones and Alerts |
| SWE1_AMM_128 | SYS-RA-AMM-350 | Lower Priority Alert Rejection | Alert Management | Tones and Alerts |
| SWE1_AMM_279 | SYS-RA-AMM-859 | Confirmation Tone Sound Selection | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_280 | SYS-RA-AMM-860 | System-Generated Confirmation Tone Configuration | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_281 | SYS-RA-AMM-861 | System-Generated Alert Tone Configuration | Alert Generation | Tones and Alerts |
| SWE1_AMM_282 | SYS-RA-AMM-862 | Alert Sound Selection | Alert Generation | Tones and Alerts |
| SWE1_AMM_283 | SYS-RA-AMM-865 | Default Sound Fileset Selection for Missing Theme Configur | Sound Configuration | Tones and Alerts |
| SWE1_AMM_284 | SYS-RA-AMM-866 | Fiat Latam Sound Fileset Selection | Sound Configuration | Tones and Alerts |
| SWE1_AMM_285 | SYS-RA-AMM-867 | Default Sound Fileset Selection for Unsupported Theme Valu | Sound Configuration | Tones and Alerts |
| SWE1_AMM_292 | SYS-RA-AMM-937 | Customer Selectable Park Assist Chime Volume | Chime Volume Control | Tones and Alerts |
| SWE1_AMM_293 | SYS-RA-AMM-938 | Gear Position Based Park Assist Volume Strategy | Chime Volume Control | Tones and Alerts |
| SWE1_AMM_294 | SYS-RA-AMM-939 | Default Park Assist Volume Strategy | Chime Volume Control | Tones and Alerts |
| SWE1_AMM_304 | SYS-RA-AMM-1082 | Confirmation Tone Volume Calculation | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_305 | SYS-RA-AMM-1083 | Default Confirmation Tone Volume for Inactive Cabin Audio | Confirmation Tone | Tones and Alerts |
| SWE1_AMM_016 | SYS-RA-AMM-125 | Confirmation Tone Enable State Handling | User Settings | Audio Processing |
| SWE1_AMM_025 | SYS-RA-AMM-145 | Audio Parameter Transfer | Audio Parameter Control | Audio Processing |
| SWE1_AMM_029 | SYS-RA-AMM-171 | Audio System Type Configuration Handling | System Configuration | Audio Processing |
| SWE1_AMM_035 | SYS-RA-AMM-183 | Confirmation Tone Availability | Feature Control | Audio Processing |
| SWE1_AMM_041 | SYS-RA-AMM-194 | Entertainment Tone Control Applicability | Tone Control | Audio Processing |
| SWE1_AMM_042 | SYS-RA-AMM-195 | Neutral Tone Control for Information and Signal Sources | Tone Control | Audio Processing |
| SWE1_AMM_043 | SYS-RA-AMM-196 | User Tone Control Parameter Communication | Tone Control | Audio Processing |
| SWE1_AMM_045 | SYS-RA-AMM-198 | Tone Control Level Mapping | Tone Control | Audio Processing |
| SWE1_AMM_046 | SYS-RA-AMM-199 | Tone Control Availability by TLM State | Feature Control | Audio Processing |
| SWE1_AMM_047 | SYS-RA-AMM-200 | Bass Mid and Treble Adjustment Handling | Tone Control | Audio Processing |
| SWE1_AMM_048 | SYS-RA-AMM-202 | Amplifier Tone Control Setup Communication | Tone Control Interface | Audio Processing |
| SWE1_AMM_049 | SYS-RA-AMM-204 | Tone Control Level Encoding | Tone Control | Audio Processing |
| SWE1_AMM_109 | SYS-RA-AMM-313 | Loudness Compensation Initialization | Audio Enhancement | Audio Processing |
| SWE1_AMM_125 | SYS-RA-AMM-347 | Tone Priority Arbitration | Tone Management | Audio Processing |
| SWE1_AMM_126 | SYS-RA-AMM-348 | Lower Priority Tone Rejection | Tone Management | Audio Processing |
| SWE1_AMM_160 | SYS-RA-AMM-403 | Speaker Unmute Control | Audio Output | Audio Processing |
| SWE1_AMM_168 | SYS-RA-AMM-446 | Surround Sound Override | Audio Effects | Audio Processing |
| SWE1_AMM_222 | SYS-RA-AMM-564 | Surround Sound Availability in Non-Amplified Systems | Audio Configuration | Audio Processing |
| SWE1_AMM_248 | SYS-RA-AMM-749 | Amplifier Presence Detection | Hardware Configuration | Audio Processing |
| SWE1_AMM_249 | SYS-RA-AMM-750 | Fixed Gain Output Mode | Audio Output Configuration | Audio Processing |
| SWE1_AMM_250 | SYS-RA-AMM-751 | Variable Gain Output Mode | Audio Output Configuration | Audio Processing |
| SWE1_AMM_251 | SYS-RA-AMM-765 | Detect LBSS Presence | Hardware Configuration | Audio Processing |
| SWE1_AMM_252 | SYS-RA-AMM-766 | Detect RBSS Presence | Hardware Configuration | Audio Processing |
| SWE1_AMM_253 | SYS-RA-AMM-767 | Disable Blind Spot Systems | Hardware Configuration | Audio Processing |
| SWE1_AMM_254 | SYS-RA-AMM-772 | Detect ICS Presence | Hardware Configuration | Audio Processing |
| SWE1_AMM_255 | SYS-RA-AMM-773 | Detect ICS Absence | Hardware Configuration | Audio Processing |
| SWE1_AMM_258 | SYS-RA-AMM-785 | Read Cabin EQ Configuration | Audio Configuration | Audio Processing |
| SWE1_AMM_261 | SYS-RA-AMM-789 | Load Valid Cabin EQ Parameters | Audio Configuration | Audio Processing |
| SWE1_AMM_265 | SYS-RA-AMM-799 | Support Surround Sound Control | Audio Configuration | Audio Processing |
| SWE1_AMM_267 | SYS-RA-AMM-810 | Loudness Menu for Base Audio System | Audio Configuration | Audio Processing |
| SWE1_AMM_268 | SYS-RA-AMM-811 | Loudness Applied Only to Entertainment Sources | Audio Processing | Audio Processing |
| SWE1_AMM_269 | SYS-RA-AMM-812 | Disable Loudness for Fiat Booster System | Audio Configuration | Audio Processing |
| SWE1_AMM_270 | SYS-RA-AMM-814 | Disable Loudness for Premium CAN / Beats Systems | Audio Configuration | Audio Processing |
| SWE1_AMM_271 | SYS-RA-AMM-818 | Loudness Disabled (Duplicate Requirement) | Audio Configuration | Audio Processing |
| SWE1_AMM_092 | SYS-RA-AMM-288 | Surround Sound Availability Control | Surround Sound | Surround and Fade |
| SWE1_AMM_093 | SYS-RA-AMM-289 | Surround Sound Disable Processing | Surround Sound | Surround and Fade |
| SWE1_AMM_094 | SYS-RA-AMM-290 | Stereo Mode Status Indication | Surround Sound | Surround and Fade |
| SWE1_AMM_095 | SYS-RA-AMM-291 | Surround Sound Enable Processing | Surround Sound | Surround and Fade |
| SWE1_AMM_096 | SYS-RA-AMM-292 | Surround Mode Status Indication | Surround Sound | Surround and Fade |
| SWE1_AMM_097 | SYS-RA-AMM-293 | Stereo Mode Fallback Handling | Surround Sound | Surround and Fade |
| SWE1_AMM_098 | SYS-RA-AMM-294 | Surround Feature Availability | Surround Sound | Surround and Fade |
| SWE1_AMM_099 | SYS-RA-AMM-295 | Surround Feature Enablement | Surround Sound | Surround and Fade |
| SWE1_AMM_100 | SYS-RA-AMM-296 | Surround Sound Feature Activation Conditions | Surround Sound | Surround and Fade |
| SWE1_AMM_101 | SYS-RA-AMM-297 | Surround Sound Disable Request Handling | Surround Sound | Surround and Fade |
| SWE1_AMM_102 | SYS-RA-AMM-298 | Surround Sound Enable Request Handling | Surround Sound | Surround and Fade |
| SWE1_AMM_103 | SYS-RA-AMM-299 | Default Surround Sound Configuration | Surround Sound | Surround and Fade |
| SWE1_AMM_104 | SYS-RA-AMM-300 | Amplifier Surround Sound Support | Surround Sound | Surround and Fade |
| SWE1_AMM_105 | SYS-RA-AMM-303 | Default Amplifier Surround Status | Surround Sound | Surround and Fade |
| SWE1_AMM_110 | SYS-RA-AMM-317 | Fade Control Scope | Fade Control | Surround and Fade |
| SWE1_AMM_111 | SYS-RA-AMM-318 | Balance Control Output Routing | Balance Control | Surround and Fade |
| SWE1_AMM_112 | SYS-RA-AMM-319 | Balance Channel Distribution | Balance Control | Surround and Fade |
| SWE1_AMM_113 | SYS-RA-AMM-320 | Balance Control Source Scope | Balance Control | Surround and Fade |
| SWE1_AMM_115 | SYS-RA-AMM-322 | Fade Control Signal Transmission | Fade Control | Surround and Fade |
| SWE1_AMM_116 | SYS-RA-AMM-323 | Fade Parameter Distribution | Fade Control | Surround and Fade |
| SWE1_AMM_117 | SYS-RA-AMM-324 | Balance Control Signal Transmission | Balance Control | Surround and Fade |
| SWE1_AMM_118 | SYS-RA-AMM-325 | Balance Parameter Distribution | Balance Control | Surround and Fade |
| SWE1_AMM_120 | SYS-RA-AMM-328 | Fade and Balance Level Distribution | Fade / Balance | Surround and Fade |
| SWE1_AMM_121 | SYS-RA-AMM-329 | Fade and Balance Configuration Transmission | Fade / Balance | Surround and Fade |
| SWE1_AMM_052 | SYS-RA-AMM-208 | Source Volume Persistence and Recall | Volume Persistence | Power and Persistence |
| SWE1_AMM_057 | SYS-RA-AMM-221 | Entertainment Volume Recall Limitation | Volume Persistence | Power and Persistence |
| SWE1_AMM_062 | SYS-RA-AMM-227 | Entertainment Volume Recall | Volume Persistence | Power and Persistence |
| SWE1_AMM_131 | SYS-RA-AMM-357 | Persistent Audio State Storage | State Management | Power and Persistence |
| SWE1_AMM_140 | SYS-RA-AMM-371 | Persistent Audio State Restoration | State Management | Power and Persistence |
| SWE1_AMM_161 | SYS-RA-AMM-404 | User Settings Restoration | Persistent Storage | Power and Persistence |
| SWE1_AMM_170 | SYS-RA-AMM-458 | Restore Previous Audio Settings | Persistent Storage | Power and Persistence |
| SWE1_AMM_171 | SYS-RA-AMM-463 | Store Audio Settings Before Entertainment Ramp-Up | Persistent Storage | Power and Persistence |
| SWE1_AMM_172 | SYS-RA-AMM-467 | Restore Stored Audio Settings | Persistent Storage | Power and Persistence |
| SWE1_AMM_173 | SYS-RA-AMM-471 | Store Audio Settings Before Speaker Activation | Persistent Storage | Power and Persistence |
| SWE1_AMM_174 | SYS-RA-AMM-474 | Restore Audio Settings After Speaker Activation | Persistent Storage | Power and Persistence |
| SWE1_AMM_177 | SYS-RA-AMM-496 | Store Audio Settings Before HU/AMP Activation | Persistent Storage | Power and Persistence |
| SWE1_AMM_178 | SYS-RA-AMM-499 | Restore Audio Settings After HU/AMP Activation | Persistent Storage | Power and Persistence |
| SWE1_AMM_188 | SYS-RA-AMM-512 | TBM Mute State Preservation | Persistent Storage | Power and Persistence |
| SWE1_AMM_221 | SYS-RA-AMM-563 | Preserve Cabin Audio Settings During Source Transition | Audio State Management | Power and Persistence |
| SWE1_AMM_245 | SYS-RA-AMM-683 | Speaker Diagnostics Enable | Diagnostics | Power and Persistence |
| SWE1_AMM_246 | SYS-RA-AMM-742 | AMP Audio Availability Synchronization | System Status | Power and Persistence |
| SWE1_AMM_247 | SYS-RA-AMM-746 | Restore Configuration After BH-CAN Wakeup | Persistent Storage | Power and Persistence |
| SWE1_AMM_297 | SYS-RA-AMM-1074 | Navigation Volume Restoration after Sleep Mode | Volume Restoration | Power and Persistence |
| SWE1_AMM_298 | SYS-RA-AMM-1075 | Phone Volume Minimum Threshold Restoration (Non-LATAM) | Volume Restoration | Power and Persistence |
| SWE1_AMM_299 | SYS-RA-AMM-1076 | Phone Volume Minimum Threshold Restoration (LATAM) | Volume Restoration | Power and Persistence |
| SWE1_AMM_300 | SYS-RA-AMM-1077 | Phone Volume Maximum Threshold Restoration | Volume Restoration | Power and Persistence |
| SWE1_AMM_301 | SYS-RA-AMM-1078 | Ringer Volume Minimum Threshold Restoration | Volume Restoration | Power and Persistence |
| SWE1_AMM_302 | SYS-RA-AMM-1079 | Ringer Volume Maximum Threshold Restoration | Volume Restoration | Power and Persistence |
| SWE1_AMM_303 | SYS-RA-AMM-1080 | Voice Recognition Volume Minimum Threshold Restoration | Volume Restoration | Power and Persistence |
| SWE1_AMM_242 | SYS-RA-AMM-625 | Logistic Mode Audio Disable | System Mode | Logistic Mode |
| SWE1_AMM_243 | SYS-RA-AMM-626 | Logistic Mode Audio Status | System Status | Logistic Mode |
| SWE1_AMM_244 | SYS-RA-AMM-627 | Exit Logistic Mode | Power Management | Logistic Mode |

## 三、批次計畫（產線順序）

依 Layer 2 順序連續下批（IN §4.1.4 之 TC sequencing）；同集 sibling 同批。

| 批 | 內容 | 葉數 |
|---|---|---|
| B1 | Source Transition（34）＋ Audio Arbitration 前 16 | 50 |
| B2 | Audio Arbitration 後 13＋ Focus and Ducking（18）＋ Mute Requests 前 19 | 50 |
| B3 | Mute Requests 後 13＋ Volume Control 前 37 | 50 |
| —— 首繳（3 批）＋ Pei 抽查；乾淨則啟 R-G14 綠色通道 —— | | |
| B4 | Volume Control 後 13＋ Audio Sources（37） | 50 |
| B5 | Tones and Alerts（32）＋ Audio Processing 前 18 | 50 |
| B6 | Audio Processing 後 16＋ Surround and Fade（24）＋ Power and Persistence 前 10 | 50 |
| B7 | Power and Persistence 後 15＋ Logistic Mode（3）＋ sibling 溢出回收 | ~18+溢出 |

註：葉→TC 拆分係數落地後（估 1.3–1.6），實際批數 9–10；
B7 起吸收前批 sibling 拆分溢出列。

## 四、待 Pei 確認事項（一次回畢即開 B1）

1. Layer 2 三分與 Projection Audio 撤銷（§一差異兩處）——採／不採。
2. B1 範圍照 §三——准／改。
