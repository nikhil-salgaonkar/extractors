| Blueprint name          | Management Server                                                                                                |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------- |
| Description             | Extractor for Management servers(FW Management/Endpoint Management) will be built using this blueprint document. |
| Creation date | 20 May 2021                                                                                                      |
| Version                 | 0.1                                                                                                |
| Change Update           |                                                                              |


**Number of Streams - 3**

Stream 1 - AUTHENTICATION 

1. User - User trying to login
2. SrcIP - Client IP
3. System- authenticating server/Host
4. Action -User Logged On, Logon Authentication Failed(Events)
5. AuthProto - Authentication protocol
6. Reason - Reason for auth failure actions
7. Status - Response of the action, passed or failed

Stream 2 - IAM

1. User - User Name of the user
2. Action - Action taken by an admin user for accounts / policies
3. Role- Role details for role updation or modification events
4. TargetUser - Target account on which changes are being made
5. Status - status of the action taken

Stream 3 - CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

**Requirement Gathering and Analysis -** 

**Useful Links:**

https://www.manageengine.com/products/firewall/firewall-management.html

https://dl3.checkpoint.com/paid/34/3468a082a93a3b06013268ca50d5ef08/CP_R80.30_GA_SecurityManagement_AdminGuide.pdf?HashKey=1619086149_153a6f12b291822b340aceb22c796a01&xtn=.pdf

https://fortinetweb.s3.amazonaws.com/docs.fortinet.com/v2/attachments/6a93234c-5591-11e9-81a4-00505692583a/FortiManager_%26_FortiAnalyzer_6.2.0_Event_Log_Reference.pdf

FireEye - https://manualzz.com/doc/7500583/administrative-guide 
