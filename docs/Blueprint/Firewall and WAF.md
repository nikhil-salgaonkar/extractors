| Blueprint name          | Firewall  & WAF                                                                  |
| ----------------------- | --------------------------------------------------------------------------------:|
| Description             | Extractor for the firewall  and WAF will be built using this blueprint document. |
| Creation date | 20-Jan-21                                                                        |
| Version                 | 0.1                                                                                                |
| Change Update           |                                                                              |


**Number of Streams - 5**

Stream 1 - FIREWALL

1. SrcIP - Source IP address
2. DstIP - Destination IP address
3. Action - The action code indicating what action was taken for the message.
4. Proto -The protocol used by web traffic.
5. SrcPort - Port number of the traffic's origin.
6. DstPort - Port number of the traffic's destination.
7. App - The network application that was accessed.
8. TXLen - sent bytes
9. RXLen - received bytes

Stream 2 - THREAT 

**Vector = “WEB”** (This field needs to be pre-populated with the value ‘Network’)
1. Action - The action code indicating what action was taken for the message.
2. Threat - Names of threats identified
3. SrcIP - The source IP address
4. DstIP - The destination IP address
5. User - name of the user

Stream 3 - Authentication 

1. User - User trying to login
2. SrcIP - Client IP
3. System- authenticating server/Host
4. Action -User Logged On, Logon Authentication Failed(Events)
5. AuthProto - Authentication protocol
6. Reason - Reason for auth failure actions
7. Status - Response of the action, passed or failed

Stream 4 - IAM

1. User - User Name of the user
2. Action - Action taken by an admin user for accounts / policies
3. Role- Role details for role updation or modification events
4. TargetUser - Target account on which changes are being made
5. Status - status of the action taken

Stream 5 -CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

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
