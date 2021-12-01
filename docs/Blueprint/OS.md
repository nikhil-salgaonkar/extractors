| Blueprint name          | OS                                                                |
| ----------------------- | ----------------------------------------------------------------- |
| Description             | Extractor for the OS will be built using this blueprint document. |
| Blueprint creation date | 18 Feb 2021                                                       |
| Version                 | 0.1                                                                                                |
| Change Update           |                                                                              |


**Number of Streams - 18**

Stream 1 - AUTHENTICATION

1. User - User trying to login
2. SrcIP - Client IP
3. Action -User Logged On, Logon Authentication Failed(Events)
4. AuthProto - Authentication protocol
5. Reason - Reason for auth failure actions
6. Status - Response of the action, passed or failed
7. System - authenticating server/Host

Stream 2 - IAM

1. User - User who performs the action
2. Action - Action taken by an admin user for accounts / policies
3. Target User- User on whom action is performed
4. Role - Details regarding role name for role updation or modification events
5. Status - status of the action taken

Stream 3 - FIREWALL

1. SrcIP - Source IP address
2. DstIP -  Destination IP address
3. Action - The action code indicating what action was taken for the message.
4. Proto -The protocol used by web traffic.
5. SrcPort - Port number of the traffic's origin.
6. DstPort - Port number of the traffic's destination.
7. TXLen - Sent bytes
8. RXLen - Received bytes
9. App - The network application that was accessed.
10. EventID

Stream 4 - SYSMON-NETWORK

1. SystemTstamp
2. System
3. SrcIP
4. SrcHost
5. SrcPort
6. DstHost
7. DstIP
8. DstPort
9. Proto
10. User
11. Image
12. Description
13. EventID

Stream 5 - SYSMON-PROCESS

1. SystemTstamp
2. System
3. EventID
4. OriginalFileName
5. ParentUser
6. CommandLine
7. ParentCommandLine
8. ParentImage
9. Image
10. SrcIP
11. SrcHost
12. SrcPort
13. DstHost
14. DstIP
15. DstPort
16. User
17. TargetImage
18. Description
19. Product
20. Comapany
21. GrantedAccess
22. CallTrace
23. Hash

Stream 6 - SYSMON-IMG-LOAD

1. SystemTStamp
2. System
3. EventID
4. Image
5. ImageLoaded
6. User
7. Description
8. Product
9. Company
10. Hash
11. Signed

Stream 7 - SYSMON-DNS

1. SystemTstamp
2. System
3. EventID
4. Image
5. QueryName
6. QueryStatus
7. QueryResults
8. User

Stream 8 - SYSMON-WMI

1. SystemTstamp
2. System
3. EventID
4. Destination
5. Type
6. Consumer
7. Filter
8. Action: operation
9. Name
10. User

Stream 9 - SYSMON-FILE

1. SystemTstamp
2. System
3. EventID
4. TargetFile
5. Image
6. CreationUTCTime
7. User

Stream 10 - SYSMON-DRIVERLOAD

1. SystemTstamp
2. System
3. EventID
4. ImageLoaded
5. SignatureStatus
6. Signature
7. Signed
8. User

Stream 11 - SYSMON-CONFIG

1. SystemTstamp
2. System
3. EventID
4. Configuration
5. ConfigurationFileHash
6. User

Stream 12 - SYSMON-SERVICE

1. SystemTstamp
2. System
3. EventID
4. State
5. SchemaVersion
6. User

Stream 13 - SYSMON-REGISTRY

1. SystemTstamp
2. System
3. EventID
4. Action
5. Image
6. TargetObject
7. Description
8. Details
9. User

Stream 14 - AUDITD

1. Action - Action taken for process/service
2. Status - Status for the action taken
3. User - User name
4. CommandLine - Command passed for the process
5. Process - Process name
6. ProcessArgs - Arguments passed for the process

Stream 15 - SYSMON-PIPE

1. Action
2. PipeName
3. Image
4. System
5. EventID
6. User

Stream 16 -CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

Stream 17 - WIN-AUDIT

1. User:SubjectUserName
2. Action:Action
3. Event: Event ID description
4. Category - Directory/ network/Policy
5. Status:Status
6. System:Hostname
7. EventID
8. SrcIP: Source Network Address
9. Object: ShareName/Object Name

Stream 18 - THREAT 

1. Vector = “Network” (This field needs to be pre-populated with the value ‘Network’)
2. Action - The action code indicating what action was taken for the message.
3. Threat - Names of threats identified
4. SrcIP - The source IP address
5. DstIP - The destination IP address
6. User - the name of the user

**Requirement Gathering and Analysis -** 

**Useful Links:**
