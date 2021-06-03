| Blueprint name          | IPS/ISD                                                        |
| ----------------------- | -------------------------------------------------------------- |
| Description             | Extractor for IPS will be built using this blueprint document. |
| Blueprint creation date | 25 Feb 2021                                                    |
| Author                  | Lenora, Review by Sharron.                                     |
| Review Date             |                                                                |

**Number of Streams - 5**

Stream 1 - THREAT (For NIPS/NIDS)

1. Vector - “NETWORK” (This field needs to be pre-populated with the value ‘Network’)
2. Action - The action code indicating what action was taken for the message.
3. SrcIP - The source IP address
4. DstIP - The destination IP address
5. Threat - Names of threats identified

Stream 2 - THREAT (For HIPS/HIDS)

1. Vector = “HOST” (This field needs to be pre-populated with the value ‘Endpoint’)
2. Action - Action taken which is blocked or quarantined.
3. Threat - Name of the signature for which a signal is triggered
4. SrcIP - Internal IP address/ External Ip address based on direction 
5. DstIP - Internal IP address/ External Ip address based on direction
6. CommandLine - Command passed for the process
7. User - name of the user who starts a process
8. File - Application name causing threat
9. Process - Process initiated for the event
10.URL - Suspected url causing threat(Intrusion url)

Stream 3 - AUTHENTICATION 

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

https://docs.mcafee.com/bundle/enterprise-security-manager-data-sources-configuration-reference-guide/page/GUID-FE64DE61-CB2A-45B9-BE48-48A5ACFE476B.html

https://www.juniper.net/documentation/en_US/junos-space16.1/topics/concept/junos-space-ips-event-log-overview.html

https://docs.trendmicro.com/all/tip/ips/v3.8.4/en-us/ips_3.8.4_lsm_ug.pdf

https://docs.sophos.com/nsg/Cyberoam/Version%2010.x/10.6.6/Guides/Cyberoam%20IPS%20Implementation%20Guide.pdf
