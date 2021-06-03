| Blueprint name          | Switch/Router                                                      |
| ----------------------- | ------------------------------------------------------------------ |
| Description             | Extractor for the IOS will be built using this blueprint document. |
| Creation date | 18 Feb 2021                                                        |
| Veriosn                 | 0.1                                                            |
| Change Update           |  -                                                             |

**Number of Streams - 3**

Stream 1 - AUTHENTICATION

1. User - User trying to login
2. SrcIP - Client IP
3. Action -User Logged On, Logon Authentication Failed(Events)
4. AuthProto  Proto - Authentication protocol
5. Reason - Reason for auth failure actions
6. Status - Response of the action, passed or failed
7. System - authenticating server/Host

Stream 2 -CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

Stream 3 - IAM

1. User - User Name of the user
2. Action - Action taken by an admin user for accounts / policies
3. Role- Role details for role updation or modification events
4. TargetUser - Target account on which changes are being made
5. Status - status of the action taken

**Requirement Gathering and Analysis -**

**Useful Links:**

https://networklessons.com/cisco/ccie-routing-switching/cisco-ios-syslog-messages

https://www.cisco.com/c/en/us/td/docs/ios/15_0sy/system/messages/15sysmg.pdf

https://www.ibm.com/docs/en/dsm?topic=ios-cisco-sample-event-messages
