# G215 —— 歷史臨時號對照表（R-P304）

> **對照之鍵**：`(req_id, tc_title)` —— 其於二次重編中皆不變。
> 27 包之腳本明載「不改動任何 TC 之內容，僅改 `tc_id`」；
> 44 包之合併只改被保留者之 procedure / ER，`req_id` 與 `tc_title` 不變。

## 一、歷史重編事件

| # | 包 | 事件 | 腳本 |
|---|---|---|---|
| 1 | 27 | 補測插入中段致號段衝突 → **全域重編** | `renumber_tc_ids.py` |
| 2 | 44 | 四對合併 264 → 260 → **保留原序補缺口** | `apply_merge_44.py` |

## 二、各階段與現行號之差異

| 階段 | 與現行號相異之條數 |
|---|---|
| 27 包重編前 | **220** |
| 27 包重編後 | **253** |
| 44 包合併前 | **255** |

**現行 TC 數：260**；被併入而無現行號者 **4** 條。

## 三、逐條對照

| req_id | 27 包重編前 | 27 包重編後 | 44 包合併前 | **現行** | `tc_title` |
|---|---|---|---|---|---|
| `SWE-PM-011` | `…-045` | `…-045` | `…-045` | **`…-044`** | CarPlay requesting audio and video keeps audio unmuted a |
| `SWE-PM-011` | `…-046` | `…-046` | `…-046` | **`…-045`** | CarPlay requesting audio only activates the Screen OFF f |
| `SWE-PM-011` | `…-048` | `…-048` | `…-048` | **`…-047`** | CarPlay requesting neither audio nor video returns the H |
| `SWE-PM-011` | `…-047` | `…-047` | `…-047` | **`…-046`** | CarPlay requesting video only mutes the audio and keeps  |
| `SWE-PM-011` | `…-049` | `…-049` | `…-049` | **`…-048`** | VR button long press in IDLE mode transitions the HU to  |
| `SWE-PM-011` | `…-044` | `…-044` | `…-044` | **`…-043`** | VR button press in IDLE mode transitions the HU to Full- |
| `SWE-PM-012` | `…-051` | `…-051` | `…-051` | **`…-050`** | TLM starts from Sleep state after leaving INIT |
| `SWE-PM-012` | `…-050` | `…-050` | `…-050` | **`…-049`** | User settings are restored after a battery reconnection |
| `SWE-PM-013` | `…-053` | `…-056` | `…-056` | **`…-055`** | AMP, ICS and DTV are off while chime audio stays active |
| `SWE-PM-013` | `…-054` | `…-057` | `…-057` | **`…-056`** | HMI interaction is disabled except for status changes |
| `SWE-PM-013` | `…-052` | `…-052` | `…-052` | **`…-051`** | Remote Start Active reports Partial_Operation |
| `SWE-PM-013` | — | `…-054` | `…-054` | **`…-053`** | Remote Start Active reports Partial_Operation in Ignitio |
| `SWE-PM-013` | — | `…-055` | `…-055` | **`…-054`** | Remote Start Active reports Partial_Operation in Ignitio |
| `SWE-PM-013` | — | `…-053` | `…-053` | **`…-052`** | Remote Start Active reports Partial_Operation in Ignitio |
| `SWE-PM-014` | `…-061` | `…-064` | `…-064` | **`…-063`** | Behaviour 1 reached through Auto_SwitchOn_Setting.Req on |
| `SWE-PM-014` | `…-058` | `…-061` | `…-061` | **`…-060`** | Behaviour 1 with an active call passes the TLM to Timed |
| `SWE-PM-014` | `…-057` | `…-060` | `…-060` | **`…-059`** | Behaviour 1 with no active call passes the TLM to Standb |
| `SWE-PM-014` | `…-059` | `…-062` | `…-062` | **`…-061`** | Behaviour 2 on a Jeep with the driver door open passes t |
| `SWE-PM-014` | `…-060` | `…-063` | `…-063` | **`…-062`** | Behaviour 2 otherwise passes to Timed keeping the active |
| `SWE-PM-014` | `…-062` | `…-065` | `…-065` | **`…-064`** | Behaviour 2 reached through Auto_SwitchOn_Setting.Req on |
| `SWE-PM-014` | `…-056` | `…-059` | `…-059` | **`…-058`** | RemStartFail is cleared when the call is not active |
| `SWE-PM-014` | `…-055` | `…-058` | `…-058` | **`…-057`** | Remote Start ends at ignition off: RemStartFail is set t |
| `SWE-PM-014` | `…-063` | `…-066` | `…-066` | **`…-065`** | Remote Start ends at ignition pre off: RemStartFail is s |
| `SWE-PM-015` | `…-065` | `…-068` | `…-068` | **`…-067`** | CLIMATIC_PANEL.Radio_Btn0 press with no active call pass |
| `SWE-PM-015` | `…-067` | `…-070` | `…-070` | **`…-069`** | CLIMATIC_PANEL.Radio_Btn0 press with the rear camera not |
| `SWE-PM-015` | `…-064` | `…-067` | `…-067` | **`…-066`** | Front_Panel_OnOff.Req press with no active call passes t |
| `SWE-PM-015` | `…-066` | `…-069` | `…-069` | **`…-068`** | Front_Panel_OnOff.Req press with the rear camera not act |
| `SWE-PM-016` | `…-068` | `…-071` | `…-071` | **`…-070`** | Rear camera activation keeps the TLM in Full-Operation |
| `SWE-PM-017` | `…-069` | `…-072` | `…-072` | **`…-071`** | Rear camera deactivation restores the last active source |
| `SWE-PM-018` | `…-070` | `…-073` | `…-073` | **`…-072`** | Ignition off in Idle passes the TLM to Standby |
| `SWE-PM-018` | `…-071` | `…-074` | `…-074` | **`…-073`** | Ignition pre off in Idle passes the TLM to Standby |
| `SWE-PM-019` | `…-074` | `…-077` | `…-077` | **`…-076`** | CLIMATIC_PANEL.Radio_Btn0 press is ignored while the rea |
| `SWE-PM-019` | `…-075` | `…-078` | `…-078` | **`…-077`** | CLIMATIC_PANEL.Radio_Btn0 press otherwise shows the Spla |
| `SWE-PM-019` | `…-072` | `…-075` | `…-075` | **`…-074`** | Front_Panel_OnOff.Req press is ignored while the rear ca |
| `SWE-PM-019` | `…-073` | `…-076` | `…-076` | **`…-075`** | Front_Panel_OnOff.Req press otherwise shows the Splash S |
| `SWE-PM-020` | `…-078` | `…-081` | `…-081` | **`…-080`** | Call ending on another screen keeps the TLM in Full-Oper |
| `SWE-PM-020` | `…-077` | `…-080` | `…-080` | **`…-079`** | Call ending on the Phone Main Screen returns the TLM to  |
| `SWE-PM-020` | `…-076` | `…-079` | `…-079` | **`…-078`** | Incoming call in Idle passes the TLM to Full-Operation |
| `SWE-PM-021` | `…-079` | `…-082` | `…-082` | **`…-081`** | Rear camera enable in Idle keeps Idle with video only |
| `SWE-PM-022` | `…-080` | `…-083` | `…-083` | **`…-082`** | Logistic mode on passes the TLM to Logistic Idle |
| `SWE-PM-023` | `…-081` | `…-084` | `…-084` | **`…-083`** | Leaving Ignition Off in Timed passes the TLM to Full-Ope |
| `SWE-PM-024` | `…-082` | `…-085` | `…-085` | **`…-084`** | Remote Start not active on leaving Ignition Off clears R |
| `SWE-PM-025` | `…-088` | `…-091` | `…-091` | **`…-090`** | Accepting the CLIMATIC_PANEL.Radio_Btn0 popup passes the |
| `SWE-PM-025` | `…-084` | `…-087` | `…-087` | **`…-086`** | Accepting the Front_Panel_OnOff.Req popup passes the TLM |
| `SWE-PM-025` | `…-087` | `…-090` | `…-090` | **`…-089`** | CLIMATIC_PANEL.Radio_Btn0 press in Timed with an active  |
| `SWE-PM-025` | `…-090` | `…-093` | `…-093` | **`…-092`** | CLIMATIC_PANEL.Radio_Btn0 press in Timed with no active  |
| `SWE-PM-025` | `…-089` | `…-092` | `…-092` | **`…-091`** | Declining the CLIMATIC_PANEL.Radio_Btn0 popup keeps the  |
| `SWE-PM-025` | `…-085` | `…-088` | `…-088` | **`…-087`** | Declining the Front_Panel_OnOff.Req popup keeps the TLM  |
| `SWE-PM-025` | `…-083` | `…-086` | `…-086` | **`…-085`** | Front_Panel_OnOff.Req press in Timed with an active call |
| `SWE-PM-025` | `…-086` | `…-089` | `…-089` | **`…-088`** | Front_Panel_OnOff.Req press in Timed with no active call |
| `SWE-PM-026` | — | `…-097` | `…-097` | **`…-096`** | A non Jeep brand does not take the door transition to St |
| `SWE-PM-026` | `…-091` | `…-094` | `…-094` | **`…-093`** | Door open on a Jeep from Full-Operation passes the TLM t |
| `SWE-PM-026` | `…-093` | `…-096` | `…-096` | **`…-095`** | Door open with Standby as the previous state keeps the T |
| `SWE-PM-026` | `…-092` | `…-095` | `…-095` | **`…-094`** | Door open with an active call keeps the TLM in Timed |
| `SWE-PM-027` | `…-094` | `…-098` | `…-098` | **`…-097`** | Antitheft failure clears the activation request within T |
| `SWE-PM-027` | `…-095` | `…-099` | `…-099` | **`…-098`** | Antitheft failure in Partial Operation keeps the origina |
| `SWE-PM-028` | `…-096` | `…-100` | `…-100` | **`…-099`** | Antitheft success clears the activation request |
| `SWE-PM-028` | `…-099` | `…-103` | `…-103` | **`…-101`** | Antitheft success on LTM High takes Timeout1 from PROXI |
| `SWE-PM-028` | `…-098` | `…-102` | `…-102` | —（已併入 `…-100` 之現行號） | Antitheft success passes the TLM to Timed state |
| `SWE-PM-028` | `…-097` | `…-101` | `…-101` | **`…-100`** | Antitheft success with a zero timeout takes Timeout1 fro |
| `SWE-PM-029` | `…-100` | `…-104` | `…-104` | **`…-102`** | Antitheft success clears the activation request on this  |
| `SWE-PM-029` | `…-103` | `…-107` | `…-107` | —（已併入 `…-104` 之現行號） | Antitheft success on this variant passes the TLM to Time |
| `SWE-PM-029` | `…-102` | `…-106` | `…-106` | **`…-104`** | Timeout1 follows PwrAccDelayAct when the setting is zero |
| `SWE-PM-029` | `…-101` | `…-105` | `…-105` | **`…-103`** | Timeout1 follows Switch_Off_Time when the setting is zer |
| `SWE-PM-030` | `…-105` | `…-109` | `…-109` | **`…-106`** | Splash Screen is shown for the Recall_Last branch |
| `SWE-PM-030` | `…-104` | `…-108` | `…-108` | **`…-105`** | Splash Screen is shown for the configured wait time |
| `SWE-PM-031` | `…-106` | `…-110` | `…-110` | **`…-107`** | Rear view camera images follow the enable signal in any  |
| `SWE-PM-032` | `…-107` | `…-111` | `…-111` | **`…-108`** | Remote Start from Standby passes the TLM to Partial Oper |
| `SWE-PM-033` | `…-109` | `…-113` | `…-113` | **`…-110`** | Ignition Off from Partial Operation passes the TLM to St |
| `SWE-PM-033` | `…-108` | `…-112` | `…-112` | **`…-109`** | Ignition Pre Off from Partial Operation passes the TLM t |
| `SWE-PM-034` | `…-110` | `…-114` | `…-114` | **`…-111`** | Front panel press in Partial Operation arms the antithef |
| `SWE-PM-035` | `…-111` | `…-115` | `…-115` | **`…-112`** | Antitheft success with auto switch on active passes the  |
| `SWE-PM-035` | `…-112` | `…-116` | `…-116` | **`…-113`** | Antitheft success with auto switch on not active passes  |
| `SWE-PM-035` | `…-114` | `…-118` | `…-118` | **`…-115`** | Antitheft success with recall last and last status off p |
| `SWE-PM-035` | `…-113` | `…-117` | `…-117` | **`…-114`** | Antitheft success with recall last and last status on pa |
| `SWE-PM-036` | `…-115` | `…-119` | `…-119` | **`…-116`** | Remote start from Timed passes the TLM to Partial Operat |
| `SWE-PM-037` | `…-116` | `…-120` | `…-120` | **`…-117`** | Call end in Timed with a failed remote start passes the  |
| `SWE-PM-038` | `…-034` | `…-034` | `…-034` | **`…-033`** | Case 1 with RemStartFail false: previous source is resto |
| `SWE-PM-038` | `…-033` | `…-033` | `…-033` | **`…-032`** | Case 1 with RemStartFail true: TLM stops and passes to S |
| `SWE-PM-038` | `…-036` | `…-036` | `…-036` | **`…-035`** | Case 2 exit on call end: TLM_Status.Info passes to Stand |
| `SWE-PM-038` | `…-037` | `…-037` | `…-037` | **`…-036`** | Case 2 exit with RemStartFail cleared on MaxCallTimeout  |
| `SWE-PM-038` | `…-035` | `…-035` | `…-035` | **`…-034`** | Case 2: MaxCallTimeout starts at Timeout1 expiry and the |
| `SWE-PM-038` | `…-039` | `…-039` | `…-039` | **`…-038`** | Case 3 with RemStartFail cleared at Timeout1 expiry |
| `SWE-PM-038` | `…-038` | `…-038` | `…-038` | **`…-037`** | Case 3: call already ended at Timeout1 expiry |
| `SWE-PM-038` | `…-042` | `…-042` | `…-042` | **`…-041`** | Case 4 exit with RemStartFail cleared on MaxCallTimeout  |
| `SWE-PM-038` | `…-041` | `…-041` | `…-041` | **`…-040`** | Case 4 exit: TLM passes to Standby when the call ends |
| `SWE-PM-038` | `…-043` | `…-043` | `…-043` | **`…-042`** | Case 4 with ignition pre off: TLM enters Timed state |
| `SWE-PM-038` | `…-040` | `…-040` | `…-040` | **`…-039`** | Case 4: ignition off with Timeout1 at 00 min enters Time |
| `SWE-PM-039` | `…-118` | `…-122` | `…-122` | **`…-119`** | A zero switch off timeout loads Timeout1 from the PROXI  |
| `SWE-PM-039` | `…-117` | `…-121` | `…-121` | **`…-118`** | An SNA operational mode is handled as an ignition off ev |
| `SWE-PM-039` | `…-119` | `…-123` | `…-123` | **`…-120`** | Auto switch on active on LTM High Radio loads Timeout1 f |
| `SWE-PM-039` | `…-120` | `…-124` | `…-124` | **`…-121`** | Only TLM menu items are guaranteed in the Timed status |
| `SWE-PM-040` | `…-121` | `…-125` | `…-125` | **`…-122`** | A normal power down into Suspend to RAM starts the 8 day |
| `SWE-PM-041` | `…-123` | `…-127` | `…-127` | **`…-124`** | Entering the TLM off with network on status clears the a |
| `SWE-PM-041` | `…-122` | `…-126` | `…-126` | **`…-123`** | No TLM function is available in the TLM off with network |
| `SWE-PM-042` | `…-125` | `…-129` | `…-129` | **`…-126`** | Entering the TLM off with network off status clears the  |
| `SWE-PM-042` | `…-124` | `…-128` | `…-128` | **`…-125`** | No TLM function is available in the TLM off with network |
| `SWE-PM-043` | `…-127` | `…-131` | `…-131` | **`…-128`** | The backlight is allowed during Standby when an HMI scre |
| `SWE-PM-043` | `…-126` | `…-130` | `…-130` | **`…-127`** | The backlight stays off during Standby mode |
| `SWE-PM-044` | `…-131` | `…-135` | `…-135` | **`…-132`** | Climatic panel press in Sleep arms the antitheft and sho |
| `SWE-PM-044` | `…-130` | `…-134` | `…-134` | **`…-131`** | Climatic panel press in Standby arms the antitheft and s |
| `SWE-PM-044` | `…-129` | `…-133` | `…-133` | **`…-130`** | Front panel press in Sleep arms the antitheft and shows  |
| `SWE-PM-044` | `…-128` | `…-132` | `…-132` | **`…-129`** | Front panel press in Standby arms the antitheft and show |
| `SWE-PM-045` | `…-133` | `…-137` | `…-137` | **`…-134`** | A failed antitheft keeps the TLM in the original Sleep s |
| `SWE-PM-045` | `…-132` | `…-136` | `…-136` | **`…-133`** | A failed antitheft keeps the TLM in the original Standby |
| `SWE-PM-046` | `…-135` | `…-139` | `…-139` | **`…-136`** | Rear view camera is provided after an unsuccessful antit |
| `SWE-PM-046` | `…-134` | `…-138` | `…-138` | **`…-135`** | Rear view camera is provided while the antitheft is stil |
| `SWE-PM-047` | `…-137` | `…-141` | `…-141` | **`…-138`** | A failed antitheft keeps the TLM in Sleep and shows the  |
| `SWE-PM-047` | `…-136` | `…-140` | `…-140` | **`…-137`** | A failed antitheft keeps the TLM in Standby and shows th |
| `SWE-PM-048` | `…-138` | `…-142` | `…-142` | **`…-139`** | Antitheft success with auto switch on active reaches Ful |
| `SWE-PM-048` | `…-139` | `…-143` | `…-143` | **`…-140`** | Antitheft success with auto switch on not active reaches |
| `SWE-PM-048` | `…-141` | `…-145` | `…-145` | **`…-142`** | Recall last with last status off reaches Idle after the  |
| `SWE-PM-048` | `…-140` | `…-144` | `…-144` | **`…-141`** | Recall last with last status on reaches Full-Operation a |
| `SWE-PM-048` | `…-142` | `…-146` | `…-146` | **`…-143`** | The ex-factory default selects recall last with the last |
| `SWE-PM-049` | `…-143` | `…-147` | `…-147` | **`…-144`** | A failed antitheft keeps the TLM blocked in Idle |
| `SWE-PM-050` | `…-144` | `…-148` | `…-148` | **`…-145`** | The else branch stores the last status off and passes th |
| `SWE-PM-051` | `…-145` | `…-149` | `…-149` | **`…-146`** | Antitheft success stores the last status on and passes t |
| `SWE-PM-052` | `…-146` | `…-150` | `…-150` | **`…-147`** | A failed antitheft keeps the TLM in the original Partial |
| `SWE-PM-053` | `…-147` | `…-151` | `…-151` | **`…-148`** | The vehicle brand logo screen follows the brand configur |
| `SWE-PM-054` | `…-149` | `…-153` | `…-153` | **`…-150`** | Beats brand white without SDARS adds the Beats logo |
| `SWE-PM-054` | `…-148` | `…-152` | `…-152` | **`…-149`** | No audio brand without SDARS shows the vehicle brand log |
| `SWE-PM-054` | `…-151` | `…-155` | `…-155` | **`…-152`** | SDARS present with beats brand white adds both logos |
| `SWE-PM-054` | `…-150` | `…-154` | `…-154` | **`…-151`** | SDARS present without audio brand adds the Sirius logo |
| `SWE-PM-055` | `…-152` | `…-156` | `…-156` | **`…-153`** | The special package drives the Klipsch Splash Screen on  |
| `SWE-PM-055` | `…-153` | `…-157` | `…-157` | **`…-154`** | The splash screen type drives the Klipsch Splash Screen  |
| `SWE-PM-056` | `…-154` | `…-158` | `…-158` | **`…-155`** | The Fiat Latam startup animation replaces the vehicle br |
| `SWE-PM-057` | `…-020` | `…-020` | `…-020` | **`…-019`** | Timeout1 options follow PROXI "Switch_Off_Time" set to 1 |
| `SWE-PM-057` | `…-018` | `…-018` | `…-018` | **`…-017`** | Timeout1 options follow PROXI "Switch_Off_Time" set to 2 |
| `SWE-PM-057` | `…-019` | `…-019` | `…-019` | **`…-018`** | Timeout1 options follow PROXI "Switch_Off_Time" set to 6 |
| `SWE-PM-058` | `…-155` | `…-159` | `…-159` | **`…-156`** | The ex-factory default sets a zero switch off timeout |
| `SWE-PM-059` | `…-157` | `…-161` | `…-161` | **`…-158`** | A network sleep request during boot is served only after |
| `SWE-PM-059` | `…-156` | `…-160` | `…-160` | **`…-157`** | A network sleep request in Standby passes the TLM to Sle |
| `SWE-PM-060` | `…-021` | `…-021` | `…-021` | **`…-020`** | LTM or ETM Radio offers one timeout parameter |
| `SWE-PM-060` | `…-022` | `…-022` | `…-022` | **`…-021`** | Radio other than LTM or ETM offers two timeout parameter |
| `SWE-PM-061` | `…-024` | `…-024` | `…-024` | **`…-023`** | Timeout settings are not selectable outside Full-Operati |
| `SWE-PM-061` | `…-023` | `…-023` | `…-023` | **`…-022`** | Timeout settings are selectable in Full-Operation status |
| `SWE-PM-062` | `…-025` | `…-025` | `…-025` | **`…-024`** | Auto_SwitchOn_Setting.Req can be set to Active |
| `SWE-PM-062` | `…-026` | `…-026` | `…-026` | **`…-025`** | Auto_SwitchOn_Setting.Req can be set to Not_Active |
| `SWE-PM-062` | `…-027` | `…-027` | `…-027` | **`…-026`** | Auto_SwitchOn_Setting.Req can be set to Recall_Last |
| `SWE-PM-063` | `…-028` | `…-028` | `…-028` | **`…-027`** | Bluetooth calls can be made and received in Timed state |
| `SWE-PM-064` | `…-030` | `…-030` | `…-030` | **`…-029`** | MaxCallTimeout starts at Timeout1 expiry with the call s |
| `SWE-PM-064` | `…-029` | `…-029` | `…-029` | **`…-028`** | MaxCallTimeout starts on ignition off with Timeout1 at 0 |
| `SWE-PM-065` | `…-031` | `…-031` | `…-031` | **`…-030`** | Call ends before Timeout1 expiry: previous source is res |
| `SWE-PM-065` | `…-032` | `…-032` | `…-032` | **`…-031`** | Further calls are still managed within Timeout1 |
| `SWE-PM-066` | `…-159` | `…-163` | `…-163` | **`…-160`** | An Assist call is treated as a phone call becoming activ |
| `SWE-PM-066` | `…-158` | `…-162` | `…-162` | **`…-159`** | An SOS call is treated as a phone call becoming active |
| `SWE-PM-067` | `…-160` | `…-164` | `…-164` | **`…-161`** | A projection device call is treated as a phone call beco |
| `SWE-PM-068` | `…-161` | `…-165` | `…-165` | **`…-162`** | An incoming call from IDLE bypasses the disclaimer scree |
| `SWE-PM-069` | `…-162` | `…-166` | `…-166` | **`…-163`** | The HU returns to IDLE when the call ends on the phone m |
| `SWE-PM-069` | `…-163` | `…-167` | `…-167` | **`…-164`** | The HU returns to IDLE when the call ends on the phone p |
| `SWE-PM-070` | `…-164` | `…-168` | `…-168` | **`…-165`** | The bypassed disclaimer is shown at the next transition  |
| `SWE-PM-071` | `…-003` | `…-003` | `…-003` | **`…-003`** | No splash screen when TLM passes to Bench |
| `SWE-PM-071` | `…-002` | `…-002` | `…-002` | **`…-002`** | No splash screen when TLM passes to Standby |
| `SWE-PM-071` | `…-001` | `…-001` | `…-001` | **`…-001`** | Splash screen shown after SplashScreen_Time on normal bo |
| `SWE-PM-071` | `…-004` | `…-004` | `…-004` | **`…-004`** | Standard screen shown after StandardScreen_Time |
| `SWE-PM-072` | `…-006` | `…-006` | `…-006` | —（已併入 `…-005` 之現行號） | Buffered events processed as soon as possible during boo |
| `SWE-PM-072` | `…-005` | `…-005` | `…-005` | **`…-005`** | Events during boot are buffered without loss |
| `SWE-PM-073` | `…-015` | `…-015` | `…-015` | **`…-014`** | Battery Critical exits on voltage out of range condition |
| `SWE-PM-073` | `…-009` | `…-009` | `…-009` | **`…-008`** | Battery Critical minimizes draw and keeps ACN active |
| `SWE-PM-073` | `…-014` | `…-014` | `…-014` | **`…-013`** | Battery Critical minimizes draw in BODY OFF-TIMED mode |
| `SWE-PM-073` | `…-017` | `…-017` | `…-017` | **`…-016`** | Battery Critical with volume already below the cap: no A |
| `SWE-PM-073` | `…-013` | `…-013` | `…-013` | **`…-012`** | Continuing call transferred to head set under Battery Cr |
| `SWE-PM-073` | `…-012` | `…-012` | `…-012` | **`…-011`** | Continuing call transferred to head set under Load Shed |
| `SWE-PM-073` | `…-007` | `…-007` | `…-007` | **`…-006`** | Load Shed limits volume and mutes TLM |
| `SWE-PM-073` | `…-011` | `…-011` | `…-011` | **`…-010`** | Load Shed recovers: normal volume and audio restored |
| `SWE-PM-073` | `…-008` | `…-008` | `…-008` | **`…-007`** | Load Shed signals lost: last values retained |
| `SWE-PM-073` | `…-016` | `…-016` | `…-016` | **`…-015`** | Load Shed with volume already below the cap: no AUD_LVL  |
| `SWE-PM-073` | `…-010` | `…-010` | `…-010` | **`…-009`** | Normal operation resumes 10 seconds after recovery |
| `SWE-PM-074` | `…-167` | `…-171` | `…-171` | **`…-168`** | A ROV FOTA update at Body OFF brings the HU to Timed for |
| `SWE-PM-074` | `…-165` | `…-169` | `…-169` | **`…-166`** | A Radio FOTA update at Body OFF brings the HU to Timed f |
| `SWE-PM-074` | `…-166` | `…-170` | `…-170` | **`…-167`** | A TBM FOTA update at Body OFF brings the HU to Timed for |
| `SWE-PM-075` | `…-168` | `…-172` | `…-172` | **`…-169`** | The HU leaves Timed one minute after the FOTA pop-up is  |
| `SWE-PM-075` | `…-169` | `…-173` | `…-173` | **`…-170`** | The HU leaves Timed when the FOTA pop-up is dismissed |
| `SWE-PM-075` | `…-170` | `…-174` | `…-174` | **`…-171`** | The HU leaves Timed when the accessory delay becomes ina |
| `SWE-PM-076` | `…-171` | `…-175` | `…-175` | **`…-172`** | A ten second power button press performs a radio reset a |
| `SWE-PM-076` | `…-173` | `…-177` | `…-177` | **`…-173`** | No power button reset occurs while a firmware image is i |
| `SWE-PM-076` | `…-172` | `…-176` | `…-176` | —（已併入 `…-175` 之現行號） | The power button reset covers both the main CPU and the  |
| `SWE-PM-077` | `…-224` | `…-231` | `…-231` | **`…-227`** | The special package value determines the theme used by t |
| `SWE-PM-078` | `…-225` | `…-232` | `…-232` | **`…-228`** | A none special package falls back to the brand default t |
| `SWE-PM-078` | `…-226` | `…-233` | `…-233` | **`…-229`** | An unsupported special package falls back to the brand d |
| `SWE-PM-079` | `…-227` | `…-234` | `…-234` | **`…-230`** | An unsupported CAN value on a branded element uses the P |
| `SWE-PM-080` | `…-229` | `…-236` | `…-236` | **`…-232`** | A theme change updates the sent value within the send wi |
| `SWE-PM-080` | `…-228` | `…-235` | `…-235` | **`…-231`** | The theme special package value is sent while the CAN ne |
| `SWE-PM-081` | `…-230` | `…-237` | `…-237` | **`…-233`** | The Chrysler brand selects the Chrysler font |
| `SWE-PM-081` | `…-232` | `…-239` | `…-239` | **`…-235`** | The Fiat brand selects the default Fiat font |
| `SWE-PM-081` | `…-231` | `…-238` | `…-238` | **`…-234`** | The Jeep brand selects the Jeep font |
| `SWE-PM-082` | `…-233` | `…-240` | `…-240` | **`…-236`** | The Chrysler brand selects the Chrysler App icon |
| `SWE-PM-082` | `…-235` | `…-242` | `…-242` | **`…-238`** | The Fiat brand selects the default Fiat App icon |
| `SWE-PM-082` | `…-234` | `…-241` | `…-241` | **`…-237`** | The Jeep brand selects the Jeep App icon |
| `SWE-PM-083` | `…-238` | `…-245` | `…-245` | **`…-241`** | The Abarth brand is mapped to the Fiat avatars |
| `SWE-PM-083` | `…-237` | `…-244` | `…-244` | **`…-240`** | The Fiat brand offers the default Fiat avatars |
| `SWE-PM-083` | `…-236` | `…-243` | `…-243` | **`…-239`** | The Jeep brand offers the Jeep avatars in the profile sc |
| `SWE-PM-084` | `…-239` | `…-246` | `…-246` | **`…-242`** | The recirc icon follows the PROXI parameters on the Atla |
| `SWE-PM-084` | `…-240` | `…-247` | `…-247` | **`…-243`** | The recirc icon follows the body style signal on the Pow |
| `SWE-PM-085` | `…-241` | `…-248` | `…-248` | **`…-244`** | The settings seat graphic follows the PROXI parameters o |
| `SWE-PM-085` | `…-242` | `…-249` | `…-249` | **`…-245`** | The settings seat graphic follows the body style signal  |
| `SWE-PM-086` | `…-244` | `…-251` | `…-251` | **`…-247`** | A theme change on this chapter updates the sent value wi |
| `SWE-PM-086` | `…-243` | `…-250` | `…-250` | **`…-246`** | The theme special package value is sent on this chapter  |
| `SWE-PM-087` | `…-246` | `…-253` | `…-253` | **`…-249`** | A non M240 vehicle line falls back to the brand seat gra |
| `SWE-PM-087` | `…-245` | `…-252` | `…-252` | **`…-248`** | The M240 vehicle line uses the M240 seat graphics |
| `SWE-PM-088` | `…-247` | `…-254` | `…-254` | **`…-250`** | The performance gauges follow the vehicle line signal |
| `SWE-PM-090` | `…-248` | `…-255` | `…-255` | **`…-251`** | The auto theme mode follows the day night signal into th |
| `SWE-PM-090` | `…-249` | `…-256` | `…-256` | **`…-252`** | The auto theme mode follows the day night signal into th |
| `SWE-PM-091` | `…-250` | `…-257` | — | — | The day theme mode keeps the Day theme regardless of the |
| `SWE-PM-091` | — | — | `…-257` | **`…-253`** | The day theme mode uses the Day theme |
| `SWE-PM-092` | `…-251` | `…-258` | — | — | The night theme mode keeps the Night theme regardless of |
| `SWE-PM-092` | — | — | `…-258` | **`…-254`** | The night theme mode uses the Night theme |
| `SWE-PM-093` | `…-178` | `…-182` | `…-182` | **`…-178`** | A mode change cancels a start-up animation in progress |
| `SWE-PM-093` | `…-180` | `…-184` | `…-184` | **`…-180`** | A mode change to TIMED MODE cancels a start-up animation |
| `SWE-PM-093` | `…-177` | `…-181` | `…-181` | **`…-177`** | A removed driver door makes the HU skip the start-up ani |
| `SWE-PM-093` | `…-182` | `…-186` | `…-186` | **`…-182`** | A second start-up animation waits for the wakeup cycle o |
| `SWE-PM-093` | `…-179` | `…-183` | `…-183` | **`…-179`** | An ignition crank event cancels a start-up animation in  |
| `SWE-PM-093` | `…-181` | `…-185` | `…-185` | **`…-181`** | An open driver door makes the HU skip the animation on a |
| `SWE-PM-093` | `…-176` | `…-180` | `…-180` | **`…-176`** | Closing the driver door in PARTIAL OPERATION MODE plays  |
| `SWE-PM-093` | `…-174` | `…-178` | `…-178` | **`…-174`** | Closing the driver door in SLEEP MODE plays the start-up |
| `SWE-PM-093` | `…-175` | `…-179` | `…-179` | **`…-175`** | Closing the driver door in STANDBY MODE plays the start- |
| `SWE-PM-094` | `…-183` | `…-187` | `…-187` | **`…-183`** | The startup animation is displayed separately from the o |
| `SWE-PM-095` | `…-184` | `…-188` | `…-188` | **`…-184`** | Leaving the SNA value resumes the state diagram without  |
| `SWE-PM-096` | `…-256` | `…-263` | `…-263` | **`…-259`** | A season change plays the new season startup animation |
| `SWE-PM-096` | `…-257` | `…-264` | `…-264` | **`…-260`** | No season change plays the normal brand based startup an |
| `SWE-PM-096` | `…-253` | `…-260` | `…-260` | **`…-256`** | The season changes to Fall at the March date |
| `SWE-PM-096` | `…-255` | `…-262` | `…-262` | **`…-258`** | The season changes to Spring at the September date |
| `SWE-PM-096` | `…-252` | `…-259` | `…-259` | **`…-255`** | The season changes to Summer at the December date |
| `SWE-PM-096` | `…-254` | `…-261` | `…-261` | **`…-257`** | The season changes to Winter at the June date |
| `SWE-PM-097` | `…-185` | `…-189` | `…-189` | **`…-185`** | The Fiat Latam startup animation selection replaces the  |
| `SWE-PM-098` | `…-186` | `…-190` | `…-190` | **`…-186`** | The always setting plays a startup sound with the animat |
| `SWE-PM-099` | `…-188` | `…-192` | `…-192` | **`…-188`** | A change of the customer selected date allows the sound  |
| `SWE-PM-099` | `…-190` | `…-194` | `…-194` | **`…-190`** | An automatic time zone adjustment allows the startup sou |
| `SWE-PM-099` | `…-189` | `…-193` | `…-193` | **`…-189`** | Passing midnight allows the startup sound to play again |
| `SWE-PM-099` | `…-187` | `…-191` | `…-191` | **`…-187`** | The once a day setting plays the startup sound on the fi |
| `SWE-PM-100` | `…-191` | `…-195` | `…-195` | **`…-191`** | The never setting plays no startup sound with the animat |
| `SWE-PM-101` | `…-193` | `…-197` | `…-197` | **`…-193`** | Beats brand white without SDARS adds the Beats logo |
| `SWE-PM-101` | `…-192` | `…-196` | `…-196` | **`…-192`** | No audio brand without SDARS shows the vehicle brand log |
| `SWE-PM-101` | `…-195` | `…-199` | `…-199` | **`…-195`** | SDARS present with beats brand white adds both logos |
| `SWE-PM-101` | `…-194` | `…-198` | `…-198` | **`…-194`** | SDARS present without audio brand adds the Sirius logo |
| `SWE-PM-102` | `…-196` | `…-200` | `…-200` | **`…-196`** | The special package drives the Klipsch Splash Screen on  |
| `SWE-PM-102` | `…-197` | `…-201` | `…-201` | **`…-197`** | The splash screen type drives the Klipsch Splash Screen  |
| `SWE-PM-103` | — | `…-205` | `…-205` | **`…-201`** | Audio is off and only the Splash Screen is allowed in Ig |
| `SWE-PM-103` | — | `…-203` | `…-203` | **`…-199`** | Audio is off and only the Splash Screen is allowed in Ig |
| `SWE-PM-103` | — | `…-204` | `…-204` | **`…-200`** | Audio is off and only the Splash Screen is allowed in Ig |
| `SWE-PM-103` | `…-198` | `…-202` | `…-202` | **`…-198`** | Audio is off and only the Splash Screen is allowed in th |
| `SWE-PM-103` | `…-199` | `…-206` | `…-206` | **`…-202`** | ICS stays available while DTV is off in this status |
| `SWE-PM-104` | `…-202` | `…-209` | `…-209` | **`…-205`** | The disclaimer appears on the first transition from Idle |
| `SWE-PM-104` | `…-204` | `…-211` | `…-211` | **`…-207`** | The disclaimer appears on the first transition from Part |
| `SWE-PM-104` | `…-203` | `…-210` | `…-210` | **`…-206`** | The disclaimer appears on the first transition from Stan |
| `SWE-PM-104` | `…-201` | `…-208` | `…-208` | **`…-204`** | The splash and disclaimer screens appear on the first tr |
| `SWE-PM-104` | `…-200` | `…-207` | `…-207` | **`…-203`** | The splash and disclaimer screens appear on the first tr |
| `SWE-PM-105` | `…-211` | `…-218` | `…-218` | **`…-214`** | A FOTA pop up temporarily skips the disclaimer and splas |
| `SWE-PM-105` | `…-206` | `…-213` | `…-213` | **`…-209`** | A backup camera view temporarily skips the disclaimer an |
| `SWE-PM-105` | `…-209` | `…-216` | `…-216` | **`…-212`** | A climate pop-up temporarily skips the disclaimer and sp |
| `SWE-PM-105` | `…-210` | `…-217` | `…-217` | **`…-213`** | An SOS or Assist call temporarily skips the disclaimer a |
| `SWE-PM-105` | `…-207` | `…-214` | `…-214` | **`…-210`** | An incoming call temporarily skips the disclaimer and sp |
| `SWE-PM-105` | `…-205` | `…-212` | `…-212` | **`…-208`** | An ongoing call temporarily skips the disclaimer and spl |
| `SWE-PM-105` | `…-208` | `…-215` | `…-215` | **`…-211`** | An outgoing call temporarily skips the disclaimer and sp |
| `SWE-PM-105` | `…-212` | `…-219` | `…-219` | **`…-215`** | The skipped screens are displayed at the next transition |
| `SWE-PM-106` | `…-213` | `…-220` | `…-220` | **`…-216`** | The SOS button variant selects the SOS disclaimer text |
| `SWE-PM-107` | `…-214` | `…-221` | `…-221` | **`…-217`** | The help button variant replaces the SOS text in the dis |
| `SWE-PM-108` | `…-215` | `…-222` | `…-222` | **`…-218`** | A non Maserati brand shows the core disclaimer once ever |
| `SWE-PM-109` | `…-216` | `…-223` | `…-223` | **`…-219`** | A GDPR market with the TBM present follows the GDPR non  |
| `SWE-PM-110` | `…-217` | `…-224` | `…-224` | **`…-220`** | A missing TBM follows the non GDPR non Maserati startup  |
| `SWE-PM-110` | `…-218` | `…-225` | `…-225` | **`…-221`** | An unmarked country follows the non GDPR non Maserati st |
| `SWE-PM-111` | `…-220` | `…-227` | `…-227` | **`…-223`** | A country not requiring SOS or geolocation adds the ADAS |
| `SWE-PM-111` | `…-219` | `…-226` | `…-226` | **`…-222`** | A missing TBM adds the ADAS text to the disclaimer |
| `SWE-PM-113` | `…-221` | `…-228` | `…-228` | **`…-224`** | A geolocation and SOS market adds the ADAS and SOS text |
| `SWE-PM-114` | `…-222` | `…-229` | `…-229` | **`…-225`** | An incoming call from IDLE bypasses the not yet shown di |
| `SWE-PM-115` | `…-223` | `…-230` | `…-230` | **`…-226`** | The disclaimer bypassed for a call is shown at the next  |
