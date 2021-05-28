| Blueprint name          | Firewall  & WAF                                                                  |
| ----------------------- | --------------------------------------------------------------------------------:|
| Description             | Extractor for the firewall  and WAF will be built using this blueprint document. |
| Blueprint creation date | 20-Jan-21                                                                        |
| Author                  | Lenora                                                                           |
| Review Date             | 21 Jan 2021                                                                      |
| Version                 | 0.1                                                                              |

**Number of Streams - 5**

Stream 1 - FIREWALL


SrcIP - Source IP address
DstIP - Destination IP address
Action - The action code indicating what action was taken for the message.
Proto -The protocol used by web traffic.
SrcPort - Port number of the traffic's origin.
DstPort - Port number of the traffic's destination.
App - The network application that was accessed.
TXLen - sent bytes
RXLen - received bytes


Stream 2 - THREAT 

Vector = “WEB” (This field needs to be pre-populated with the value ‘Network’)
Action - The action code indicating what action was taken for the message.
Threat - Names of threats identified
SrcIP - The source IP address
DstIP - The destination IP address
User - name of the user


Stream 3 - Authentication 


User - User trying to login
SrcIP - Client IP
System- authenticating server/Host
Action -User Logged On, Logon Authentication Failed(Events)
AuthProto - Authentication protocol
Reason - Reason for auth failure actions
Status - Response of the action, passed or failed


Stream 4 - IAM

User - User Name of the user
Action - Action taken by an admin user for accounts / policies
Role- Role details for role updation or modification events
TargetUser - Target account on which changes are being made
Status - status of the action taken

Stream 5 -CONFIGURATION

User - User who made changes
Action - Action taken
Config - Configuration name
Status - status of the action taken


**Requirement Gathering and Analysis -**

**Useful Links:**

Useful Links:

Zscaler
https://help.zscaler.com/zia/nss-feed-output-format-firewall-logs

Checkpoint
https://supportcenter.checkpoint.com/supportcenter/portal?eventSubmit_doGoviewsolutiondetails=&solutionid=sk144192

Fortinet
https://docs.fortinet.com/document/fortigate/6.0.4/fortios-log-message-reference/357866/log-message-fields

Cisco ASA
https://www.cisco.com/c/en/us/td/docs/security/asa/asa96/configuration/general/asa-96-general-config/monitor-syslog.html

Palo Alto
https://docs.paloaltonetworks.com/pan-os/9-1/pan-os-admin/monitoring/use-syslog-for-monitoring/syslog-field-descriptions/threat-log-fields.html#id83052cb2-4798-4f9c-abf8-e0b929ce7a3b
