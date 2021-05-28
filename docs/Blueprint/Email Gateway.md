| Blueprint name          | Email Gateway                                                            |
| ----------------------- | -------------------------------------------------------------------------|
| Description             | Extractor for Email gateway will be built using this blueprint document. |
| Blueprint creation date | 15-Jan-21                                                                |
| Author                  | Sharron, Lenora                                                          |
| Review Date             | 16-Jan-21, Review with PM 1-Feb-21                                       |
| Version                 | 0.1                                                                      |

**Number of Streams - 4**

Stream 1 - EMAIL-GATEWAY

- Sender - The sender of the email.
- Recipient -  The recipient of the email.
- Action - The action indicating what action was taken for the email.
- Subject -The subject of the email.
- Direction - Detects the flow-  inbound or outbound
- Remote IP - Client Ip
- File - The filenames of all attachments on the email


Stream 2 - THREAT 

Vector - EMAIL

- Vector = “EMAIL” (This field needs to be pre-populated with the value ‘Email’)
- SrcIP - Client IP
- Sender - Sender
- Recipient - Recipient
- Threat - Name of the signature/AtkMsg indicating threat
- Action - Action taken - blocked, quarantined


Stream 3 - AUTHENTICATION

- User - Username of the user attempting to authenticate
- ScrIP - Client IP
- Action -User Logged On, Logon Authentication Failed(Events)
- Reason - Reason for auth failure actions
- AuthProto - Authentication protocol
- Status - Response of the action, passed or failed 
- System - authenticating server/Host

Stream 4 - IAM

- User - Email/ name of the user(Source User)
- Action - Action taken by an admin user for accounts / policies
- Role - Role details for role updation or modification events
- TargetUser - Target account on which changes are being made
- Status - status of the action taken



Stream 5 -CONFIGURATION

- User - User who made changes
- Action - Action taken
- Config - Configuration name
- Status - status of the action taken

**Requirement Gathering and Analysis -**

**Useful Links:**
Mimecast - https://www.mimecast.com/tech-connect/documentation/tutorials/understanding-siem-logs/

Proofpoint - https://help.proofpoint.com/Threat_Insight_Dashboard/API_Documentation/SIEM_API

CISCO IRONPORT (Cisco IronPort Email Security Appliances)
https://www.cisco.com/c/en/us/td/docs/security/esa/esa11-1/user_guide/b_ESA_Admin_Guide_11_1/b_ESA_Admin_Guide_chapter_0100110.html

Barracuda - https://campus.barracuda.com/product/emailsecuritygateway/doc/12193950/syslog-and-the-barracuda-email-security-gateway/

TrendMicro Deep Discovery Email Inspector (from Parsers by clients file) - 
https://docs.trendmicro.com/all/ent/ddei/3.2/en-us/ddei_3.2_sg.pdf


https://community.mimecast.com/s/article/Administration-Console-Audit-Logs-1478129523

