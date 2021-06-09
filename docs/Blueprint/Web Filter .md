
| Blueprint name          | Web Filter                                                            |
| ----------------------- | ----------------------------------------------------------------------|
| Description             | Extractor for Web Filter will be built using this blueprint document. |
| Creation date | 27-Jan-21                                                             |
| Version                 | 0.1                                                            |
| Change Update           |  -                                                             |

**Number of Streams - 5**

Stream 1 - WEBFILTER

- Action - The action code indicating what action was taken for the message.
- URL - The URL accessed
- HTTPMethod - Method associated with the request
- ScrIP - The source IP of the request.
- DstIP - Destination IP of the communication
- UserAgent - Contents of the User-Agent 
- DstPort - Destination port of the request
- TXLen - Sent bytes
- RXLen - Received bytes
- User - name of the user sending the request
- Proto - Protocol used


Stream 2 - Threat 

- Vector - ‘WEB’
- Action - The action code indicating what action was taken for the message.
- Threat - Name of the threat identified
- SrcIP - IP added of the source
- DstIP - Destination IP of communication
- User - name of the user

Stream 3 - Authentication

- User - User trying to login
- SrcIP - Client IP
- System- authenticating server/Host
- Action -User Logged On, Logon Authentication Failed(Events)
- AuthProto - Authentication protocol
- Reason - Reason for auth failure actions
- Status - Response of the action, passed or failed

Stream 4 - IAM
- User - User Name of the user
- Action - Action taken by an admin user for accounts / policies
- Role- Role details for role updation or modification events
- TargetUser - Target account on which changes are being made
- Status - status of the action taken


Stream 5 - CONFIGURATION

- User - User who made changes		
- Action - action taken		
- Config - Configuration name		
- Status- Status of the action taken		


**Requirement Gathering and Analysis -**

**Useful Links:**

Zscaler 
https://help.zscaler.com/zia/nss-feed-output-format-web-logs

Websense
http://www.websense.com/content/support/library/web/v76/siem/siem.pdf

https://docs.safesquid.com/wiki/Analyze_The_SafeSquid_Logs

Bluecoat
https://docs.mcafee.com/bundle/enterprise-security-manager-data-sources-configuration-reference-guide/page/GUID-63EE73C3-F060-429F-9D43-B7D2EB76EA31.html

Forcepoint
https://docs.mcafee.com/bundle/enterprise-security-manager-data-sources-configuration-reference-guide/page/GUID-F830A7D1-6D54-4C31-96D2-D73F912E49C1.html
