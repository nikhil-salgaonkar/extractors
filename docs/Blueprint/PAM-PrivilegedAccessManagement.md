| Blueprint name          | PAM                                                            |
| ----------------------- | -------------------------------------------------------------- |
| Description             | Extractor for PAM will be built using this blueprint document. |
| Creation date | 17 May 2021                                                    |
| Veriosn                 | 0.1                                                            |
| Change Update           |  -                                                             |

**Number of Streams - 4**

Stream 1 - THREAT

1. Vector = “HOST"
2. SrcIP - Internal IP address/ External Ip address based on direction
3. DstIP - Internal IP address/ External Ip address based on direction
4. Threat - Name of the signature for which a signal is triggered
5. File - Application name causing threat
6. Process - Process initiated for the event
7. URL - Suspected url causing threat(Intrusion url)
8. CommandLine- Command passed for the process
9. Action - Action taken which is blocked or quarantined
10. User - for any user who starts a process

Stream 2 - Authentication 

1. User - User trying to login
2. SrcIP - Client IP
3. System- authenticating server/Host
4. Action -User Logged On, Logon Authentication Failed(Events)
5. AuthProto - Authentication protocol
6. Reason - Reason for auth failure actions
7. Status - Response of the action, passed or failed

Stream 3 - IAM

1. User - User Name of the user
2. Action - Action taken by an admin user for accounts / policies
3. Role- Role details for role updation or modification events
4. TargetUser - Target account on which changes are being made
5. Status - status of the action taken

Stream 4 -CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

**Requirement Gathering and Analysis -**

**Useful Links:**

https://www.beyondtrust.com/docs/archive/privilege-management/defendpoint/group-policy/5-2-21-0/dp-mmc-administration-5-2-21-0.pdf 

https://docs.cyberark.com/Product-Doc/OnlineHelp/PAS/Latest/en/Content/PASIMP/Integrating-with-SIEM-Applications.htm?TocPath=Security%20Information%20and%20Event%20Management%20Applications%7C_____0 
