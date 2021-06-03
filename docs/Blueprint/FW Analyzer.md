| Blueprint name          | Firewall Analyzer                                                            |
| ----------------------- | ---------------------------------------------------------------------------- |
| Description             | Extractor for Firewall Analyzer will be built using this blueprint document. |
| Creation date | 25 Feb 2021                                                                  |
| Version                 | 0.1                                                                                                |
| Change Update           |                                                                              |

**Number of Streams - 4**

Stream 1 - IAM

1. Action - Action taken by an admin user for accounts / policies
2. User - User name of the user
3. TargetUser - Target account on which changes are being made
4. Role - Details regarding role name for role updation or modification events
5. Status - status of the action taken

Stream 2 - CONFIGURATION

1. User - User who made changes
2. Action - action taken
3. Config - Configuration name
4. Status- Status of the action taken

Stream 3 - AUTHENTICATION

1. User - User who is trying to login. 
2. Src IP - Client IP
3. Action -User Logged On, Logon Authentication Failed(Events)
4. Reason - Reason for auth failure actions
5. Status - Response of the action, passed or failed
6. AuthProto - Authentication protocol
7. System- authenticating server/Host

Stream 4 - THREAT

1. Vector - “NETWORK” (This field needs to be pre-populated with the value ‘Network’)
2. Action - The action code indicating what action was taken for the message.
3. SrcIP - The source IP address
4. DstIP - The destination IP address
5. Threat - Names of threats identified

**Requirement Gathering and Analysis -** 

**Useful Links:**

https://www.algosec.com/docs/en/asms/a30.00/PDFs/FirewallAnalyzer-UserGuide.pdf

https://www.algosec.com/docs/en/asms/a30.10/PDFs/FirewallAnalyzer-AdministratorGuide.pdf

https://downloads.skyboxsecurity.com/files/Installers/Skybox_View/10.1/10.1.500/Docs/Skybox_ReferenceGuide_V10_1_500.pdf
