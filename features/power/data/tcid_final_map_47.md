# G220 —— 歷史臨時號 → 最終號對照表（R-P310(三)(e) / R-P311）

> 鍵為 `(req_id, tc_title)`。最終號依 R-P113(c) 於 47 包寫回時指派（序為 `(SWE-PM ID, split_index)`，R-P115）。

| 項 | 數 |
|---|---|
| 逐條列數 | **266** |
| 具最終號者 | **260** |
| 被併入而無最終號者 | **4**（其欄指向併入對象之最終號） |
| **鍵斷裂待人工補齊** | **2** |

| req_id | 27 前 | 27 後 | 44 前 | 現行 | **最終** | `tc_title` |
|---|---|---|---|---|---|---|
| `SWE-PM-011` | `…-045` | `…-045` | `…-045` | `…-044` | **`…-002`** | CarPlay requesting audio and video keeps audio unmut |
| `SWE-PM-011` | `…-046` | `…-046` | `…-046` | `…-045` | **`…-003`** | CarPlay requesting audio only activates the Screen O |
| `SWE-PM-011` | `…-048` | `…-048` | `…-048` | `…-047` | **`…-005`** | CarPlay requesting neither audio nor video returns t |
| `SWE-PM-011` | `…-047` | `…-047` | `…-047` | `…-046` | **`…-004`** | CarPlay requesting video only mutes the audio and ke |
| `SWE-PM-011` | `…-049` | `…-049` | `…-049` | `…-048` | **`…-006`** | VR button long press in IDLE mode transitions the HU |
| `SWE-PM-011` | `…-044` | `…-044` | `…-044` | `…-043` | **`…-001`** | VR button press in IDLE mode transitions the HU to F |
| `SWE-PM-012` | `…-051` | `…-051` | `…-051` | `…-050` | **`…-008`** | TLM starts from Sleep state after leaving INIT |
| `SWE-PM-012` | `…-050` | `…-050` | `…-050` | `…-049` | **`…-007`** | User settings are restored after a battery reconnect |
| `SWE-PM-013` | `…-053` | `…-056` | `…-056` | `…-055` | **`…-013`** | AMP, ICS and DTV are off while chime audio stays act |
| `SWE-PM-013` | `…-054` | `…-057` | `…-057` | `…-056` | **`…-014`** | HMI interaction is disabled except for status change |
| `SWE-PM-013` | `…-052` | `…-052` | `…-052` | `…-051` | **`…-009`** | Remote Start Active reports Partial_Operation |
| `SWE-PM-013` | — | `…-054` | `…-054` | `…-053` | **`…-011`** | Remote Start Active reports Partial_Operation in Ign |
| `SWE-PM-013` | — | `…-055` | `…-055` | `…-054` | **`…-012`** | Remote Start Active reports Partial_Operation in Ign |
| `SWE-PM-013` | — | `…-053` | `…-053` | `…-052` | **`…-010`** | Remote Start Active reports Partial_Operation in Ign |
| `SWE-PM-014` | `…-061` | `…-064` | `…-064` | `…-063` | **`…-021`** | Behaviour 1 reached through Auto_SwitchOn_Setting.Re |
| `SWE-PM-014` | `…-058` | `…-061` | `…-061` | `…-060` | **`…-018`** | Behaviour 1 with an active call passes the TLM to Ti |
| `SWE-PM-014` | `…-057` | `…-060` | `…-060` | `…-059` | **`…-017`** | Behaviour 1 with no active call passes the TLM to St |
| `SWE-PM-014` | `…-059` | `…-062` | `…-062` | `…-061` | **`…-019`** | Behaviour 2 on a Jeep with the driver door open pass |
| `SWE-PM-014` | `…-060` | `…-063` | `…-063` | `…-062` | **`…-020`** | Behaviour 2 otherwise passes to Timed keeping the ac |
| `SWE-PM-014` | `…-062` | `…-065` | `…-065` | `…-064` | **`…-022`** | Behaviour 2 reached through Auto_SwitchOn_Setting.Re |
| `SWE-PM-014` | `…-056` | `…-059` | `…-059` | `…-058` | **`…-016`** | RemStartFail is cleared when the call is not active |
| `SWE-PM-014` | `…-055` | `…-058` | `…-058` | `…-057` | **`…-015`** | Remote Start ends at ignition off: RemStartFail is s |
| `SWE-PM-014` | `…-063` | `…-066` | `…-066` | `…-065` | **`…-023`** | Remote Start ends at ignition pre off: RemStartFail  |
| `SWE-PM-015` | `…-065` | `…-068` | `…-068` | `…-067` | **`…-025`** | CLIMATIC_PANEL.Radio_Btn0 press with no active call  |
| `SWE-PM-015` | `…-067` | `…-070` | `…-070` | `…-069` | **`…-027`** | CLIMATIC_PANEL.Radio_Btn0 press with the rear camera |
| `SWE-PM-015` | `…-064` | `…-067` | `…-067` | `…-066` | **`…-024`** | Front_Panel_OnOff.Req press with no active call pass |
| `SWE-PM-015` | `…-066` | `…-069` | `…-069` | `…-068` | **`…-026`** | Front_Panel_OnOff.Req press with the rear camera not |
| `SWE-PM-016` | `…-068` | `…-071` | `…-071` | `…-070` | **`…-028`** | Rear camera activation keeps the TLM in Full-Operati |
| `SWE-PM-017` | `…-069` | `…-072` | `…-072` | `…-071` | **`…-029`** | Rear camera deactivation restores the last active so |
| `SWE-PM-018` | `…-070` | `…-073` | `…-073` | `…-072` | **`…-030`** | Ignition off in Idle passes the TLM to Standby |
| `SWE-PM-018` | `…-071` | `…-074` | `…-074` | `…-073` | **`…-031`** | Ignition pre off in Idle passes the TLM to Standby |
| `SWE-PM-019` | `…-074` | `…-077` | `…-077` | `…-076` | **`…-034`** | CLIMATIC_PANEL.Radio_Btn0 press is ignored while the |
| `SWE-PM-019` | `…-075` | `…-078` | `…-078` | `…-077` | **`…-035`** | CLIMATIC_PANEL.Radio_Btn0 press otherwise shows the  |
| `SWE-PM-019` | `…-072` | `…-075` | `…-075` | `…-074` | **`…-032`** | Front_Panel_OnOff.Req press is ignored while the rea |
| `SWE-PM-019` | `…-073` | `…-076` | `…-076` | `…-075` | **`…-033`** | Front_Panel_OnOff.Req press otherwise shows the Spla |
| `SWE-PM-020` | `…-078` | `…-081` | `…-081` | `…-080` | **`…-038`** | Call ending on another screen keeps the TLM in Full- |
| `SWE-PM-020` | `…-077` | `…-080` | `…-080` | `…-079` | **`…-037`** | Call ending on the Phone Main Screen returns the TLM |
| `SWE-PM-020` | `…-076` | `…-079` | `…-079` | `…-078` | **`…-036`** | Incoming call in Idle passes the TLM to Full-Operati |
| `SWE-PM-021` | `…-079` | `…-082` | `…-082` | `…-081` | **`…-039`** | Rear camera enable in Idle keeps Idle with video onl |
| `SWE-PM-022` | `…-080` | `…-083` | `…-083` | `…-082` | **`…-040`** | Logistic mode on passes the TLM to Logistic Idle |
| `SWE-PM-023` | `…-081` | `…-084` | `…-084` | `…-083` | **`…-041`** | Leaving Ignition Off in Timed passes the TLM to Full |
| `SWE-PM-024` | `…-082` | `…-085` | `…-085` | `…-084` | **`…-042`** | Remote Start not active on leaving Ignition Off clea |
| `SWE-PM-025` | `…-088` | `…-091` | `…-091` | `…-090` | **`…-048`** | Accepting the CLIMATIC_PANEL.Radio_Btn0 popup passes |
| `SWE-PM-025` | `…-084` | `…-087` | `…-087` | `…-086` | **`…-044`** | Accepting the Front_Panel_OnOff.Req popup passes the |
| `SWE-PM-025` | `…-087` | `…-090` | `…-090` | `…-089` | **`…-047`** | CLIMATIC_PANEL.Radio_Btn0 press in Timed with an act |
| `SWE-PM-025` | `…-090` | `…-093` | `…-093` | `…-092` | **`…-050`** | CLIMATIC_PANEL.Radio_Btn0 press in Timed with no act |
| `SWE-PM-025` | `…-089` | `…-092` | `…-092` | `…-091` | **`…-049`** | Declining the CLIMATIC_PANEL.Radio_Btn0 popup keeps  |
| `SWE-PM-025` | `…-085` | `…-088` | `…-088` | `…-087` | **`…-045`** | Declining the Front_Panel_OnOff.Req popup keeps the  |
| `SWE-PM-025` | `…-083` | `…-086` | `…-086` | `…-085` | **`…-043`** | Front_Panel_OnOff.Req press in Timed with an active  |
| `SWE-PM-025` | `…-086` | `…-089` | `…-089` | `…-088` | **`…-046`** | Front_Panel_OnOff.Req press in Timed with no active  |
| `SWE-PM-026` | — | `…-097` | `…-097` | `…-096` | **`…-054`** | A non Jeep brand does not take the door transition t |
| `SWE-PM-026` | `…-091` | `…-094` | `…-094` | `…-093` | **`…-051`** | Door open on a Jeep from Full-Operation passes the T |
| `SWE-PM-026` | `…-093` | `…-096` | `…-096` | `…-095` | **`…-053`** | Door open with Standby as the previous state keeps t |
| `SWE-PM-026` | `…-092` | `…-095` | `…-095` | `…-094` | **`…-052`** | Door open with an active call keeps the TLM in Timed |
| `SWE-PM-027` | `…-094` | `…-098` | `…-098` | `…-097` | **`…-055`** | Antitheft failure clears the activation request with |
| `SWE-PM-027` | `…-095` | `…-099` | `…-099` | `…-098` | **`…-056`** | Antitheft failure in Partial Operation keeps the ori |
| `SWE-PM-028` | `…-096` | `…-100` | `…-100` | `…-099` | **`…-057`** | Antitheft success clears the activation request |
| `SWE-PM-028` | `…-099` | `…-103` | `…-103` | `…-101` | **`…-059`** | Antitheft success on LTM High takes Timeout1 from PR |
| `SWE-PM-028` | `…-098` | `…-102` | `…-102` | — | —（已併入 `…-100`，其最終號 `…-058`） | Antitheft success passes the TLM to Timed state |
| `SWE-PM-028` | `…-097` | `…-101` | `…-101` | `…-100` | **`…-058`** | Antitheft success with a zero timeout takes Timeout1 |
| `SWE-PM-029` | `…-100` | `…-104` | `…-104` | `…-102` | **`…-060`** | Antitheft success clears the activation request on t |
| `SWE-PM-029` | `…-103` | `…-107` | `…-107` | — | —（已併入 `…-104`，其最終號 `…-062`） | Antitheft success on this variant passes the TLM to  |
| `SWE-PM-029` | `…-102` | `…-106` | `…-106` | `…-104` | **`…-062`** | Timeout1 follows PwrAccDelayAct when the setting is  |
| `SWE-PM-029` | `…-101` | `…-105` | `…-105` | `…-103` | **`…-061`** | Timeout1 follows Switch_Off_Time when the setting is |
| `SWE-PM-030` | `…-105` | `…-109` | `…-109` | `…-106` | **`…-064`** | Splash Screen is shown for the Recall_Last branch |
| `SWE-PM-030` | `…-104` | `…-108` | `…-108` | `…-105` | **`…-063`** | Splash Screen is shown for the configured wait time |
| `SWE-PM-031` | `…-106` | `…-110` | `…-110` | `…-107` | **`…-065`** | Rear view camera images follow the enable signal in  |
| `SWE-PM-032` | `…-107` | `…-111` | `…-111` | `…-108` | **`…-066`** | Remote Start from Standby passes the TLM to Partial  |
| `SWE-PM-033` | `…-109` | `…-113` | `…-113` | `…-110` | **`…-068`** | Ignition Off from Partial Operation passes the TLM t |
| `SWE-PM-033` | `…-108` | `…-112` | `…-112` | `…-109` | **`…-067`** | Ignition Pre Off from Partial Operation passes the T |
| `SWE-PM-034` | `…-110` | `…-114` | `…-114` | `…-111` | **`…-069`** | Front panel press in Partial Operation arms the anti |
| `SWE-PM-035` | `…-111` | `…-115` | `…-115` | `…-112` | **`…-070`** | Antitheft success with auto switch on active passes  |
| `SWE-PM-035` | `…-112` | `…-116` | `…-116` | `…-113` | **`…-071`** | Antitheft success with auto switch on not active pas |
| `SWE-PM-035` | `…-114` | `…-118` | `…-118` | `…-115` | **`…-073`** | Antitheft success with recall last and last status o |
| `SWE-PM-035` | `…-113` | `…-117` | `…-117` | `…-114` | **`…-072`** | Antitheft success with recall last and last status o |
| `SWE-PM-036` | `…-115` | `…-119` | `…-119` | `…-116` | **`…-074`** | Remote start from Timed passes the TLM to Partial Op |
| `SWE-PM-037` | `…-116` | `…-120` | `…-120` | `…-117` | **`…-075`** | Call end in Timed with a failed remote start passes  |
| `SWE-PM-038` | `…-034` | `…-034` | `…-034` | `…-033` | **`…-077`** | Case 1 with RemStartFail false: previous source is r |
| `SWE-PM-038` | `…-033` | `…-033` | `…-033` | `…-032` | **`…-076`** | Case 1 with RemStartFail true: TLM stops and passes  |
| `SWE-PM-038` | `…-036` | `…-036` | `…-036` | `…-035` | **`…-079`** | Case 2 exit on call end: TLM_Status.Info passes to S |
| `SWE-PM-038` | `…-037` | `…-037` | `…-037` | `…-036` | **`…-080`** | Case 2 exit with RemStartFail cleared on MaxCallTime |
| `SWE-PM-038` | `…-035` | `…-035` | `…-035` | `…-034` | **`…-078`** | Case 2: MaxCallTimeout starts at Timeout1 expiry and |
| `SWE-PM-038` | `…-039` | `…-039` | `…-039` | `…-038` | **`…-082`** | Case 3 with RemStartFail cleared at Timeout1 expiry |
| `SWE-PM-038` | `…-038` | `…-038` | `…-038` | `…-037` | **`…-081`** | Case 3: call already ended at Timeout1 expiry |
| `SWE-PM-038` | `…-042` | `…-042` | `…-042` | `…-041` | **`…-085`** | Case 4 exit with RemStartFail cleared on MaxCallTime |
| `SWE-PM-038` | `…-041` | `…-041` | `…-041` | `…-040` | **`…-084`** | Case 4 exit: TLM passes to Standby when the call end |
| `SWE-PM-038` | `…-043` | `…-043` | `…-043` | `…-042` | **`…-086`** | Case 4 with ignition pre off: TLM enters Timed state |
| `SWE-PM-038` | `…-040` | `…-040` | `…-040` | `…-039` | **`…-083`** | Case 4: ignition off with Timeout1 at 00 min enters  |
| `SWE-PM-039` | `…-118` | `…-122` | `…-122` | `…-119` | **`…-088`** | A zero switch off timeout loads Timeout1 from the PR |
| `SWE-PM-039` | `…-117` | `…-121` | `…-121` | `…-118` | **`…-087`** | An SNA operational mode is handled as an ignition of |
| `SWE-PM-039` | `…-119` | `…-123` | `…-123` | `…-120` | **`…-089`** | Auto switch on active on LTM High Radio loads Timeou |
| `SWE-PM-039` | `…-120` | `…-124` | `…-124` | `…-121` | **`…-090`** | Only TLM menu items are guaranteed in the Timed stat |
| `SWE-PM-040` | `…-121` | `…-125` | `…-125` | `…-122` | **`…-091`** | A normal power down into Suspend to RAM starts the 8 |
| `SWE-PM-041` | `…-123` | `…-127` | `…-127` | `…-124` | **`…-093`** | Entering the TLM off with network on status clears t |
| `SWE-PM-041` | `…-122` | `…-126` | `…-126` | `…-123` | **`…-092`** | No TLM function is available in the TLM off with net |
| `SWE-PM-042` | `…-125` | `…-129` | `…-129` | `…-126` | **`…-095`** | Entering the TLM off with network off status clears  |
| `SWE-PM-042` | `…-124` | `…-128` | `…-128` | `…-125` | **`…-094`** | No TLM function is available in the TLM off with net |
| `SWE-PM-043` | `…-127` | `…-131` | `…-131` | `…-128` | **`…-097`** | The backlight is allowed during Standby when an HMI  |
| `SWE-PM-043` | `…-126` | `…-130` | `…-130` | `…-127` | **`…-096`** | The backlight stays off during Standby mode |
| `SWE-PM-044` | `…-131` | `…-135` | `…-135` | `…-132` | **`…-101`** | Climatic panel press in Sleep arms the antitheft and |
| `SWE-PM-044` | `…-130` | `…-134` | `…-134` | `…-131` | **`…-100`** | Climatic panel press in Standby arms the antitheft a |
| `SWE-PM-044` | `…-129` | `…-133` | `…-133` | `…-130` | **`…-099`** | Front panel press in Sleep arms the antitheft and sh |
| `SWE-PM-044` | `…-128` | `…-132` | `…-132` | `…-129` | **`…-098`** | Front panel press in Standby arms the antitheft and  |
| `SWE-PM-045` | `…-133` | `…-137` | `…-137` | `…-134` | **`…-103`** | A failed antitheft keeps the TLM in the original Sle |
| `SWE-PM-045` | `…-132` | `…-136` | `…-136` | `…-133` | **`…-102`** | A failed antitheft keeps the TLM in the original Sta |
| `SWE-PM-046` | `…-135` | `…-139` | `…-139` | `…-136` | **`…-105`** | Rear view camera is provided after an unsuccessful a |
| `SWE-PM-046` | `…-134` | `…-138` | `…-138` | `…-135` | **`…-104`** | Rear view camera is provided while the antitheft is  |
| `SWE-PM-047` | `…-137` | `…-141` | `…-141` | `…-138` | **`…-107`** | A failed antitheft keeps the TLM in Sleep and shows  |
| `SWE-PM-047` | `…-136` | `…-140` | `…-140` | `…-137` | **`…-106`** | A failed antitheft keeps the TLM in Standby and show |
| `SWE-PM-048` | `…-138` | `…-142` | `…-142` | `…-139` | **`…-108`** | Antitheft success with auto switch on active reaches |
| `SWE-PM-048` | `…-139` | `…-143` | `…-143` | `…-140` | **`…-109`** | Antitheft success with auto switch on not active rea |
| `SWE-PM-048` | `…-141` | `…-145` | `…-145` | `…-142` | **`…-111`** | Recall last with last status off reaches Idle after  |
| `SWE-PM-048` | `…-140` | `…-144` | `…-144` | `…-141` | **`…-110`** | Recall last with last status on reaches Full-Operati |
| `SWE-PM-048` | `…-142` | `…-146` | `…-146` | `…-143` | **`…-112`** | The ex-factory default selects recall last with the  |
| `SWE-PM-049` | `…-143` | `…-147` | `…-147` | `…-144` | **`…-113`** | A failed antitheft keeps the TLM blocked in Idle |
| `SWE-PM-050` | `…-144` | `…-148` | `…-148` | `…-145` | **`…-114`** | The else branch stores the last status off and passe |
| `SWE-PM-051` | `…-145` | `…-149` | `…-149` | `…-146` | **`…-115`** | Antitheft success stores the last status on and pass |
| `SWE-PM-052` | `…-146` | `…-150` | `…-150` | `…-147` | **`…-116`** | A failed antitheft keeps the TLM in the original Par |
| `SWE-PM-053` | `…-147` | `…-151` | `…-151` | `…-148` | **`…-117`** | The vehicle brand logo screen follows the brand conf |
| `SWE-PM-054` | `…-149` | `…-153` | `…-153` | `…-150` | **`…-119`** | Beats brand white without SDARS adds the Beats logo |
| `SWE-PM-054` | `…-148` | `…-152` | `…-152` | `…-149` | **`…-118`** | No audio brand without SDARS shows the vehicle brand |
| `SWE-PM-054` | `…-151` | `…-155` | `…-155` | `…-152` | **`…-121`** | SDARS present with beats brand white adds both logos |
| `SWE-PM-054` | `…-150` | `…-154` | `…-154` | `…-151` | **`…-120`** | SDARS present without audio brand adds the Sirius lo |
| `SWE-PM-055` | `…-152` | `…-156` | `…-156` | `…-153` | **`…-122`** | The special package drives the Klipsch Splash Screen |
| `SWE-PM-055` | `…-153` | `…-157` | `…-157` | `…-154` | **`…-123`** | The splash screen type drives the Klipsch Splash Scr |
| `SWE-PM-056` | `…-154` | `…-158` | `…-158` | `…-155` | **`…-124`** | The Fiat Latam startup animation replaces the vehicl |
| `SWE-PM-057` | `…-020` | `…-020` | `…-020` | `…-019` | **`…-127`** | Timeout1 options follow PROXI "Switch_Off_Time" set  |
| `SWE-PM-057` | `…-018` | `…-018` | `…-018` | `…-017` | **`…-125`** | Timeout1 options follow PROXI "Switch_Off_Time" set  |
| `SWE-PM-057` | `…-019` | `…-019` | `…-019` | `…-018` | **`…-126`** | Timeout1 options follow PROXI "Switch_Off_Time" set  |
| `SWE-PM-058` | `…-155` | `…-159` | `…-159` | `…-156` | **`…-128`** | The ex-factory default sets a zero switch off timeou |
| `SWE-PM-059` | `…-157` | `…-161` | `…-161` | `…-158` | **`…-130`** | A network sleep request during boot is served only a |
| `SWE-PM-059` | `…-156` | `…-160` | `…-160` | `…-157` | **`…-129`** | A network sleep request in Standby passes the TLM to |
| `SWE-PM-060` | `…-021` | `…-021` | `…-021` | `…-020` | **`…-131`** | LTM or ETM Radio offers one timeout parameter |
| `SWE-PM-060` | `…-022` | `…-022` | `…-022` | `…-021` | **`…-132`** | Radio other than LTM or ETM offers two timeout param |
| `SWE-PM-061` | `…-024` | `…-024` | `…-024` | `…-023` | **`…-134`** | Timeout settings are not selectable outside Full-Ope |
| `SWE-PM-061` | `…-023` | `…-023` | `…-023` | `…-022` | **`…-133`** | Timeout settings are selectable in Full-Operation st |
| `SWE-PM-062` | `…-025` | `…-025` | `…-025` | `…-024` | **`…-135`** | Auto_SwitchOn_Setting.Req can be set to Active |
| `SWE-PM-062` | `…-026` | `…-026` | `…-026` | `…-025` | **`…-136`** | Auto_SwitchOn_Setting.Req can be set to Not_Active |
| `SWE-PM-062` | `…-027` | `…-027` | `…-027` | `…-026` | **`…-137`** | Auto_SwitchOn_Setting.Req can be set to Recall_Last |
| `SWE-PM-063` | `…-028` | `…-028` | `…-028` | `…-027` | **`…-138`** | Bluetooth calls can be made and received in Timed st |
| `SWE-PM-064` | `…-030` | `…-030` | `…-030` | `…-029` | **`…-140`** | MaxCallTimeout starts at Timeout1 expiry with the ca |
| `SWE-PM-064` | `…-029` | `…-029` | `…-029` | `…-028` | **`…-139`** | MaxCallTimeout starts on ignition off with Timeout1  |
| `SWE-PM-065` | `…-031` | `…-031` | `…-031` | `…-030` | **`…-141`** | Call ends before Timeout1 expiry: previous source is |
| `SWE-PM-065` | `…-032` | `…-032` | `…-032` | `…-031` | **`…-142`** | Further calls are still managed within Timeout1 |
| `SWE-PM-066` | `…-159` | `…-163` | `…-163` | `…-160` | **`…-144`** | An Assist call is treated as a phone call becoming a |
| `SWE-PM-066` | `…-158` | `…-162` | `…-162` | `…-159` | **`…-143`** | An SOS call is treated as a phone call becoming acti |
| `SWE-PM-067` | `…-160` | `…-164` | `…-164` | `…-161` | **`…-145`** | A projection device call is treated as a phone call  |
| `SWE-PM-068` | `…-161` | `…-165` | `…-165` | `…-162` | **`…-146`** | An incoming call from IDLE bypasses the disclaimer s |
| `SWE-PM-069` | `…-162` | `…-166` | `…-166` | `…-163` | **`…-147`** | The HU returns to IDLE when the call ends on the pho |
| `SWE-PM-069` | `…-163` | `…-167` | `…-167` | `…-164` | **`…-148`** | The HU returns to IDLE when the call ends on the pho |
| `SWE-PM-070` | `…-164` | `…-168` | `…-168` | `…-165` | **`…-149`** | The bypassed disclaimer is shown at the next transit |
| `SWE-PM-071` | `…-003` | `…-003` | `…-003` | `…-003` | **`…-152`** | No splash screen when TLM passes to Bench |
| `SWE-PM-071` | `…-002` | `…-002` | `…-002` | `…-002` | **`…-151`** | No splash screen when TLM passes to Standby |
| `SWE-PM-071` | `…-001` | `…-001` | `…-001` | `…-001` | **`…-150`** | Splash screen shown after SplashScreen_Time on norma |
| `SWE-PM-071` | `…-004` | `…-004` | `…-004` | `…-004` | **`…-153`** | Standard screen shown after StandardScreen_Time |
| `SWE-PM-072` | `…-006` | `…-006` | `…-006` | — | —（已併入 `…-005`，其最終號 `…-154`） | Buffered events processed as soon as possible during |
| `SWE-PM-072` | `…-005` | `…-005` | `…-005` | `…-005` | **`…-154`** | Events during boot are buffered without loss |
| `SWE-PM-073` | `…-015` | `…-015` | `…-015` | `…-014` | **`…-163`** | Battery Critical exits on voltage out of range condi |
| `SWE-PM-073` | `…-009` | `…-009` | `…-009` | `…-008` | **`…-157`** | Battery Critical minimizes draw and keeps ACN active |
| `SWE-PM-073` | `…-014` | `…-014` | `…-014` | `…-013` | **`…-162`** | Battery Critical minimizes draw in BODY OFF-TIMED mo |
| `SWE-PM-073` | `…-017` | `…-017` | `…-017` | `…-016` | **`…-165`** | Battery Critical with volume already below the cap:  |
| `SWE-PM-073` | `…-013` | `…-013` | `…-013` | `…-012` | **`…-161`** | Continuing call transferred to head set under Batter |
| `SWE-PM-073` | `…-012` | `…-012` | `…-012` | `…-011` | **`…-160`** | Continuing call transferred to head set under Load S |
| `SWE-PM-073` | `…-007` | `…-007` | `…-007` | `…-006` | **`…-155`** | Load Shed limits volume and mutes TLM |
| `SWE-PM-073` | `…-011` | `…-011` | `…-011` | `…-010` | **`…-159`** | Load Shed recovers: normal volume and audio restored |
| `SWE-PM-073` | `…-008` | `…-008` | `…-008` | `…-007` | **`…-156`** | Load Shed signals lost: last values retained |
| `SWE-PM-073` | `…-016` | `…-016` | `…-016` | `…-015` | **`…-164`** | Load Shed with volume already below the cap: no AUD_ |
| `SWE-PM-073` | `…-010` | `…-010` | `…-010` | `…-009` | **`…-158`** | Normal operation resumes 10 seconds after recovery |
| `SWE-PM-074` | `…-167` | `…-171` | `…-171` | `…-168` | **`…-168`** | A ROV FOTA update at Body OFF brings the HU to Timed |
| `SWE-PM-074` | `…-165` | `…-169` | `…-169` | `…-166` | **`…-166`** | A Radio FOTA update at Body OFF brings the HU to Tim |
| `SWE-PM-074` | `…-166` | `…-170` | `…-170` | `…-167` | **`…-167`** | A TBM FOTA update at Body OFF brings the HU to Timed |
| `SWE-PM-075` | `…-168` | `…-172` | `…-172` | `…-169` | **`…-169`** | The HU leaves Timed one minute after the FOTA pop-up |
| `SWE-PM-075` | `…-169` | `…-173` | `…-173` | `…-170` | **`…-170`** | The HU leaves Timed when the FOTA pop-up is dismisse |
| `SWE-PM-075` | `…-170` | `…-174` | `…-174` | `…-171` | **`…-171`** | The HU leaves Timed when the accessory delay becomes |
| `SWE-PM-076` | `…-171` | `…-175` | `…-175` | `…-172` | **`…-172`** | A ten second power button press performs a radio res |
| `SWE-PM-076` | `…-173` | `…-177` | `…-177` | `…-173` | **`…-173`** | No power button reset occurs while a firmware image  |
| `SWE-PM-076` | `…-172` | `…-176` | `…-176` | — | —（已併入 `…-175`，其最終號 `…-203`） | The power button reset covers both the main CPU and  |
| `SWE-PM-077` | `…-224` | `…-231` | `…-231` | `…-227` | **`…-174`** | The special package value determines the theme used  |
| `SWE-PM-078` | `…-225` | `…-232` | `…-232` | `…-228` | **`…-175`** | A none special package falls back to the brand defau |
| `SWE-PM-078` | `…-226` | `…-233` | `…-233` | `…-229` | **`…-176`** | An unsupported special package falls back to the bra |
| `SWE-PM-079` | `…-227` | `…-234` | `…-234` | `…-230` | **`…-177`** | An unsupported CAN value on a branded element uses t |
| `SWE-PM-080` | `…-229` | `…-236` | `…-236` | `…-232` | **`…-179`** | A theme change updates the sent value within the sen |
| `SWE-PM-080` | `…-228` | `…-235` | `…-235` | `…-231` | **`…-178`** | The theme special package value is sent while the CA |
| `SWE-PM-081` | `…-230` | `…-237` | `…-237` | `…-233` | **`…-180`** | The Chrysler brand selects the Chrysler font |
| `SWE-PM-081` | `…-232` | `…-239` | `…-239` | `…-235` | **`…-182`** | The Fiat brand selects the default Fiat font |
| `SWE-PM-081` | `…-231` | `…-238` | `…-238` | `…-234` | **`…-181`** | The Jeep brand selects the Jeep font |
| `SWE-PM-082` | `…-233` | `…-240` | `…-240` | `…-236` | **`…-183`** | The Chrysler brand selects the Chrysler App icon |
| `SWE-PM-082` | `…-235` | `…-242` | `…-242` | `…-238` | **`…-185`** | The Fiat brand selects the default Fiat App icon |
| `SWE-PM-082` | `…-234` | `…-241` | `…-241` | `…-237` | **`…-184`** | The Jeep brand selects the Jeep App icon |
| `SWE-PM-083` | `…-238` | `…-245` | `…-245` | `…-241` | **`…-188`** | The Abarth brand is mapped to the Fiat avatars |
| `SWE-PM-083` | `…-237` | `…-244` | `…-244` | `…-240` | **`…-187`** | The Fiat brand offers the default Fiat avatars |
| `SWE-PM-083` | `…-236` | `…-243` | `…-243` | `…-239` | **`…-186`** | The Jeep brand offers the Jeep avatars in the profil |
| `SWE-PM-084` | `…-239` | `…-246` | `…-246` | `…-242` | **`…-189`** | The recirc icon follows the PROXI parameters on the  |
| `SWE-PM-084` | `…-240` | `…-247` | `…-247` | `…-243` | **`…-190`** | The recirc icon follows the body style signal on the |
| `SWE-PM-085` | `…-241` | `…-248` | `…-248` | `…-244` | **`…-191`** | The settings seat graphic follows the PROXI paramete |
| `SWE-PM-085` | `…-242` | `…-249` | `…-249` | `…-245` | **`…-192`** | The settings seat graphic follows the body style sig |
| `SWE-PM-086` | `…-244` | `…-251` | `…-251` | `…-247` | **`…-194`** | A theme change on this chapter updates the sent valu |
| `SWE-PM-086` | `…-243` | `…-250` | `…-250` | `…-246` | **`…-193`** | The theme special package value is sent on this chap |
| `SWE-PM-087` | `…-246` | `…-253` | `…-253` | `…-249` | **`…-196`** | A non M240 vehicle line falls back to the brand seat |
| `SWE-PM-087` | `…-245` | `…-252` | `…-252` | `…-248` | **`…-195`** | The M240 vehicle line uses the M240 seat graphics |
| `SWE-PM-088` | `…-247` | `…-254` | `…-254` | `…-250` | **`…-197`** | The performance gauges follow the vehicle line signa |
| `SWE-PM-090` | `…-248` | `…-255` | `…-255` | `…-251` | **`…-198`** | The auto theme mode follows the day night signal int |
| `SWE-PM-090` | `…-249` | `…-256` | `…-256` | `…-252` | **`…-199`** | The auto theme mode follows the day night signal int |
| `SWE-PM-091` | `…-250` | `…-257` | — | — | **鍵斷裂**（`tc_title` 於 27 包後改寫）—— 見人工補齊 | The day theme mode keeps the Day theme regardless of |
| `SWE-PM-091` | — | — | `…-257` | `…-253` | **`…-200`** | The day theme mode uses the Day theme |
| `SWE-PM-092` | `…-251` | `…-258` | — | — | **鍵斷裂**（`tc_title` 於 27 包後改寫）—— 見人工補齊 | The night theme mode keeps the Night theme regardles |
| `SWE-PM-092` | — | — | `…-258` | `…-254` | **`…-201`** | The night theme mode uses the Night theme |
| `SWE-PM-093` | `…-178` | `…-182` | `…-182` | `…-178` | **`…-206`** | A mode change cancels a start-up animation in progre |
| `SWE-PM-093` | `…-180` | `…-184` | `…-184` | `…-180` | **`…-208`** | A mode change to TIMED MODE cancels a start-up anima |
| `SWE-PM-093` | `…-177` | `…-181` | `…-181` | `…-177` | **`…-205`** | A removed driver door makes the HU skip the start-up |
| `SWE-PM-093` | `…-182` | `…-186` | `…-186` | `…-182` | **`…-210`** | A second start-up animation waits for the wakeup cyc |
| `SWE-PM-093` | `…-179` | `…-183` | `…-183` | `…-179` | **`…-207`** | An ignition crank event cancels a start-up animation |
| `SWE-PM-093` | `…-181` | `…-185` | `…-185` | `…-181` | **`…-209`** | An open driver door makes the HU skip the animation  |
| `SWE-PM-093` | `…-176` | `…-180` | `…-180` | `…-176` | **`…-204`** | Closing the driver door in PARTIAL OPERATION MODE pl |
| `SWE-PM-093` | `…-174` | `…-178` | `…-178` | `…-174` | **`…-202`** | Closing the driver door in SLEEP MODE plays the star |
| `SWE-PM-093` | `…-175` | `…-179` | `…-179` | `…-175` | **`…-203`** | Closing the driver door in STANDBY MODE plays the st |
| `SWE-PM-094` | `…-183` | `…-187` | `…-187` | `…-183` | **`…-211`** | The startup animation is displayed separately from t |
| `SWE-PM-095` | `…-184` | `…-188` | `…-188` | `…-184` | **`…-212`** | Leaving the SNA value resumes the state diagram with |
| `SWE-PM-096` | `…-256` | `…-263` | `…-263` | `…-259` | **`…-217`** | A season change plays the new season startup animati |
| `SWE-PM-096` | `…-257` | `…-264` | `…-264` | `…-260` | **`…-218`** | No season change plays the normal brand based startu |
| `SWE-PM-096` | `…-253` | `…-260` | `…-260` | `…-256` | **`…-214`** | The season changes to Fall at the March date |
| `SWE-PM-096` | `…-255` | `…-262` | `…-262` | `…-258` | **`…-216`** | The season changes to Spring at the September date |
| `SWE-PM-096` | `…-252` | `…-259` | `…-259` | `…-255` | **`…-213`** | The season changes to Summer at the December date |
| `SWE-PM-096` | `…-254` | `…-261` | `…-261` | `…-257` | **`…-215`** | The season changes to Winter at the June date |
| `SWE-PM-097` | `…-185` | `…-189` | `…-189` | `…-185` | **`…-219`** | The Fiat Latam startup animation selection replaces  |
| `SWE-PM-098` | `…-186` | `…-190` | `…-190` | `…-186` | **`…-220`** | The always setting plays a startup sound with the an |
| `SWE-PM-099` | `…-188` | `…-192` | `…-192` | `…-188` | **`…-222`** | A change of the customer selected date allows the so |
| `SWE-PM-099` | `…-190` | `…-194` | `…-194` | `…-190` | **`…-224`** | An automatic time zone adjustment allows the startup |
| `SWE-PM-099` | `…-189` | `…-193` | `…-193` | `…-189` | **`…-223`** | Passing midnight allows the startup sound to play ag |
| `SWE-PM-099` | `…-187` | `…-191` | `…-191` | `…-187` | **`…-221`** | The once a day setting plays the startup sound on th |
| `SWE-PM-100` | `…-191` | `…-195` | `…-195` | `…-191` | **`…-225`** | The never setting plays no startup sound with the an |
| `SWE-PM-101` | `…-193` | `…-197` | `…-197` | `…-193` | **`…-227`** | Beats brand white without SDARS adds the Beats logo |
| `SWE-PM-101` | `…-192` | `…-196` | `…-196` | `…-192` | **`…-226`** | No audio brand without SDARS shows the vehicle brand |
| `SWE-PM-101` | `…-195` | `…-199` | `…-199` | `…-195` | **`…-229`** | SDARS present with beats brand white adds both logos |
| `SWE-PM-101` | `…-194` | `…-198` | `…-198` | `…-194` | **`…-228`** | SDARS present without audio brand adds the Sirius lo |
| `SWE-PM-102` | `…-196` | `…-200` | `…-200` | `…-196` | **`…-230`** | The special package drives the Klipsch Splash Screen |
| `SWE-PM-102` | `…-197` | `…-201` | `…-201` | `…-197` | **`…-231`** | The splash screen type drives the Klipsch Splash Scr |
| `SWE-PM-103` | — | `…-205` | `…-205` | `…-201` | **`…-235`** | Audio is off and only the Splash Screen is allowed i |
| `SWE-PM-103` | — | `…-203` | `…-203` | `…-199` | **`…-233`** | Audio is off and only the Splash Screen is allowed i |
| `SWE-PM-103` | — | `…-204` | `…-204` | `…-200` | **`…-234`** | Audio is off and only the Splash Screen is allowed i |
| `SWE-PM-103` | `…-198` | `…-202` | `…-202` | `…-198` | **`…-232`** | Audio is off and only the Splash Screen is allowed i |
| `SWE-PM-103` | `…-199` | `…-206` | `…-206` | `…-202` | **`…-236`** | ICS stays available while DTV is off in this status |
| `SWE-PM-104` | `…-202` | `…-209` | `…-209` | `…-205` | **`…-239`** | The disclaimer appears on the first transition from  |
| `SWE-PM-104` | `…-204` | `…-211` | `…-211` | `…-207` | **`…-241`** | The disclaimer appears on the first transition from  |
| `SWE-PM-104` | `…-203` | `…-210` | `…-210` | `…-206` | **`…-240`** | The disclaimer appears on the first transition from  |
| `SWE-PM-104` | `…-201` | `…-208` | `…-208` | `…-204` | **`…-238`** | The splash and disclaimer screens appear on the firs |
| `SWE-PM-104` | `…-200` | `…-207` | `…-207` | `…-203` | **`…-237`** | The splash and disclaimer screens appear on the firs |
| `SWE-PM-105` | `…-211` | `…-218` | `…-218` | `…-214` | **`…-248`** | A FOTA pop up temporarily skips the disclaimer and s |
| `SWE-PM-105` | `…-206` | `…-213` | `…-213` | `…-209` | **`…-243`** | A backup camera view temporarily skips the disclaime |
| `SWE-PM-105` | `…-209` | `…-216` | `…-216` | `…-212` | **`…-246`** | A climate pop-up temporarily skips the disclaimer an |
| `SWE-PM-105` | `…-210` | `…-217` | `…-217` | `…-213` | **`…-247`** | An SOS or Assist call temporarily skips the disclaim |
| `SWE-PM-105` | `…-207` | `…-214` | `…-214` | `…-210` | **`…-244`** | An incoming call temporarily skips the disclaimer an |
| `SWE-PM-105` | `…-205` | `…-212` | `…-212` | `…-208` | **`…-242`** | An ongoing call temporarily skips the disclaimer and |
| `SWE-PM-105` | `…-208` | `…-215` | `…-215` | `…-211` | **`…-245`** | An outgoing call temporarily skips the disclaimer an |
| `SWE-PM-105` | `…-212` | `…-219` | `…-219` | `…-215` | **`…-249`** | The skipped screens are displayed at the next transi |
| `SWE-PM-106` | `…-213` | `…-220` | `…-220` | `…-216` | **`…-250`** | The SOS button variant selects the SOS disclaimer te |
| `SWE-PM-107` | `…-214` | `…-221` | `…-221` | `…-217` | **`…-251`** | The help button variant replaces the SOS text in the |
| `SWE-PM-108` | `…-215` | `…-222` | `…-222` | `…-218` | **`…-252`** | A non Maserati brand shows the core disclaimer once  |
| `SWE-PM-109` | `…-216` | `…-223` | `…-223` | `…-219` | **`…-253`** | A GDPR market with the TBM present follows the GDPR  |
| `SWE-PM-110` | `…-217` | `…-224` | `…-224` | `…-220` | **`…-254`** | A missing TBM follows the non GDPR non Maserati star |
| `SWE-PM-110` | `…-218` | `…-225` | `…-225` | `…-221` | **`…-255`** | An unmarked country follows the non GDPR non Maserat |
| `SWE-PM-111` | `…-220` | `…-227` | `…-227` | `…-223` | **`…-257`** | A country not requiring SOS or geolocation adds the  |
| `SWE-PM-111` | `…-219` | `…-226` | `…-226` | `…-222` | **`…-256`** | A missing TBM adds the ADAS text to the disclaimer |
| `SWE-PM-113` | `…-221` | `…-228` | `…-228` | `…-224` | **`…-258`** | A geolocation and SOS market adds the ADAS and SOS t |
| `SWE-PM-114` | `…-222` | `…-229` | `…-229` | `…-225` | **`…-259`** | An incoming call from IDLE bypasses the not yet show |
| `SWE-PM-115` | `…-223` | `…-230` | `…-230` | `…-226` | **`…-260`** | The disclaimer bypassed for a call is shown at the n |

## 附：鍵斷裂 2 條之人工補齊（R-P311）

> 其 `tc_title` 於 27 包後被改寫，致 `(req_id, tc_title)` 之鍵斷裂。
> 以 **`req_id` ＋ 語義對應**人工確認，逐條列其改寫前後之標題。

| req_id | 27 後之號 | 27 後之標題 | 現行號 | 現行標題 | **最終號** |
|---|---|---|---|---|---|
| `SWE-PM-091` | `…-257` | The day theme mode keeps the Day theme regardless of the day night signal | `…-253` | The day theme mode uses the Day theme | **`…-200`** |
| `SWE-PM-092` | `…-258` | The night theme mode keeps the Night theme regardless of the day night signal | `…-254` | The night theme mode uses the Night theme | **`…-201`** |

**補齊後之涵蓋：266 / 266（100%）** —— 260 條具最終號、4 條已併入（指向併入對象之最終號）、2 條經人工確認。
