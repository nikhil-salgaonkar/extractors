| Blueprint name          | Load Balancer                                                            |
| ----------------------- | ------------------------------------------------------------------------ |
| Description             | Extractor for Load Balancer will be built using this blueprint document. |
| Creation date | 24 Feb 2021                                                              |
| Version                 | 0.1                                                                                                |
| Change Update           |                                                                              |

**Number of Streams - 4**

Stream 1 - AUTHENTICATION 

1. User - User trying to login
2. SrcIP - Client IP
3. Action - User Logged On, Logon Authentication Failed(Events)
4. AuthProto - Authentication protocol
5. Reason - Reason for auth failure actions
6. Status - Response of the action, passed or failed
7. System - authenticating server/Host

Stream 2 - THREAT

1. Vector - HOST
2. SrcIP - Internal IP address/ External Ip address based on direction
3. DstIP - Internal IP address/ External Ip address based on direction
4. Threat - Name of the signature for which a signal is triggered
5. File - Application name causing threat
6. Process - Process initiated for the event
7. URL - Suspected url causing threat (Intrusion url)
8. CommandLine - Command passed for the process
9. Action - Action taken which is blocked or quarantined
10. User - for any user who starts a process

Stream 3 - CONFIGURATION

1. User - User who made changes
2. Action - action taken
3. Config - Configuration name
4. Status - Status of the action taken

Stream 4 - IAM (AWS)

1. User - User who performs the action
2. Action - Action taken by an admin user for accounts / policies
3. Target User - User on whom action is performed
4. Role - Details regarding role name for role updation or modification events
5. Status - status of the action taken

**Requirement Gathering and Analysis -** 

**Useful Links:**

https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html

https://docs.citrix.com/en-us/sdx/12/netscaler-sdx-12.0.pdf

https://docs.mcafee.com/bundle/enterprise-security-manager-data-sources-configuration-reference-guide/page/GUID-3B71D5E8-854C-4A68-9C83-59B33AFA76B5.html
