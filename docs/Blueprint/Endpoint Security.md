
| Blueprint name          | Endpoint Security                                                                                  |
| ----------------------- | --------------------------------------------------------------------------------------------------:|
| Description             | Extractor for the endpoint security devices, DLP,EDR  will be built using this blueprint document. |
| Blueprint creation date | 25-Jan-21                                                                                          |
| Author                  | Lenora                                                                                             |
| Review Date             | Sharron                                                                                            |
| Version                 | 0.1                                                                                                |

**Number of Streams - 4**

Stream 1 - THREAT

1.  Vector = “HOST"
2.  SrcIP - Internal IP address/ External Ip address based on direction
3.  DstIP - Internal IP address/ External Ip address based on direction
4.  Threat - Name of the signature for which a signal is triggered
5.  File - Application name causing threat
6.  Process - Process initiated for the event
7.  URL - Suspected url causing threat(Intrusion url)
8.  CommandLine- Command passed for the process
9.  Action - Action taken which is blocked or quarantined
10.  User - for any user who starts a process

Stream 2 - IAM

1.  User - User Name of the user
2.  Action - Action taken by an admin user for accounts / policies
3.  Role- Role details for role updation or modification events
4.  TargetUser - Target account on which changes are being made
5.  Status - status of the action taken

Stream 3 -CONFIGURATION

1.  User - User who made changes
2.  Action - Action taken
3.  Config - Configuration name
4.  Status - status of the action taken

Stream 4 - AUTHENTICATION

1.  User - User trying to login
2.  SrcIP - Client IP
3.  System- authenticating server/Host
4.  Action -User Logged On, Logon Authentication Failed(Events)
5.  AuthProto - Authentication protocol
6.  Reason - Reason for auth failure actions
7.  Status - Response of the action, passed or failed

**Requirement Gathering and Analysis -**

**Useful Links:**

Symantec EPP

[https://docs.mcafee.com/bundle/enterprise-security-manager-data-sources-configuration-reference-guide/page/GUID-BDA76C17-E355-409F-ABE8-98601D0ED9F3.html](https://docs.mcafee.com/bundle/enterprise-security-manager-data-sources-configuration-reference-guide/page/GUID-BDA76C17-E355-409F-ABE8-98601D0ED9F3.html)

[https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-protection/all/Monitoring-Reporting-and-Enforcing-Compliance/viewing-logs-v7522439-d37e464/about-the-types-of-logs-v8156418-d37e6.html](https://techdocs.broadcom.com/us/en/symantec-security-software/endpoint-security-and-management/endpoint-protection/all/Monitoring-Reporting-and-Enforcing-Compliance/viewing-logs-v7522439-d37e464/about-the-types-of-logs-v8156418-d37e6.html)

Trend Micro AV

[https://cloudone.trendmicro.com/docs/workload-security/events/](https://cloudone.trendmicro.com/docs/workload-security/events/)

Carbon Black Protection

[https://www.netsurion.com/Corporate/media/Corporate/Files/Support-Docs/Integration-Guide-CB-Protection.pdf](https://www.netsurion.com/Corporate/media/Corporate/Files/Support-Docs/Integration-Guide-CB-Protection.pdf)

[https://community.carbonblack.com/t5/Documentation-Downloads/Cb-Protection-v8-1-0-Events-Guide/ta-p/36308?attachment-id=8305](https://community.carbonblack.com/t5/Documentation-Downloads/Cb-Protection-v8-1-0-Events-Guide/ta-p/36308?attachment-id=8305)

Note: Threat stream will contain alerts raised from endpoint devices

Rest of the streams will contain: log that shows the user-generated activity that is performed through the console or the API

Streams - Authentication, IAM and Configuration - Will be used only if Audit logs are present in the same server, and not if the logs are generated in a management server. This decision will be taken based on each device. - - common ground required needs discussion
