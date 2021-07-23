| Blueprint name | NAC  Extractor Blueprint                                                                                                                                          |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description    | Extractor for devices using NAC (Network access control)<br>Network access control is the act of keeping unauthorized users and devices out of a private network. |
| Creation date  | 14 June, 2021                                                                                                                                                      |
| Version        | 0.1                                                                                                                                                               |
| Change Update  |                                                                                                                                                                   |


**Number of Streams - 4**

Stream 1 - Authentication 

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

Stream 3 -CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
5. Status - status of the action taken

Stream 4-THREAT 

Vector = “NETWORK”
1. Action - The action code indicating what action was taken for the message.	
2. Threat - Names of threats identified					
3. SrcIP - The source IP address					
5. DstIP - The destination IP address		

Stream 5 - COMPLIANCE (Only for Forcescout Device Compliance)

1. Event : Host is compliant/Non Compliant
2. Action: COMPLIANCE_CHECK
3. Status: Host Compliancy Status - passed/failed
4. Policy: Compliancy Policy Name
5. Reason: Policy Subrule Name(When non compliant)
6. System: dvchost
7. User: duser

**Requirement Gathering and Analysis -**

**Useful Links:**

https://www.netsurion.com/knowledge-packs/cisco-nac

https://docs.genians.com/release/en/intro.html#:~:text=A%20firewall%20is%20generally%20located,between%20endpoints%20within%20a%20network.

https://content.cisco.com/chapter.sjs?uri=/searchable/chapter/www.cisco.com/content/en/us/td/docs/security/nac/appliance/configuration_guide/49x/cam/49xcam-book/m_logs.html.xml

https://www.fortinet.com/products/network-access-control
https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/fortinac.pdf

https://docs.forescout.com/bundle/cef-2-8-2-h/page/cef-2-8-2-h.Device-Event-Mapping-to-CEF-Data-Fields.html 
