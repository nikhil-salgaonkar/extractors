| Blueprint name | Threat Extractor Blueprint                                                                                                                                       |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Description    | Extractor for Threat devices like Darktrace which are specially designed to detect threats through multiple mediums will be built using this blueprint document. |
| Creation date  | 30 June 2021                                                                                                                                                     |
| Version<br>    | 0.1                                                                                                                                                              |
| Change Update  | -                                                                                                                                                             |

**Number of Streams - 7**

- For Threat (Select vectors as applicable)

Stream 1 - THREAT 

**Vector - “NETWORK”** (This field needs to be pre-populated with the value ‘Network’)
1. Action - The action code indicating what action was taken for the message.
2. SrcIP - The source IP address
3. DstIP - The destination IP address
4. Threat - Names of threats identified

Stream 2 - THREAT 

**Vector - “HOST”** (This field needs to be pre-populated with the value ‘Endpoint’)
1. Action - Action taken which is blocked or quarantined.
2. Threat - Name of the signature for which a signal is triggered
3. SrcIP - Internal IP address/ External Ip address based on direction 
4. DstIP - Internal IP address/ External Ip address based on direction
5. CommandLine - Command passed for the process
6. User - name of the user who starts a process
7. File - Application name causing threat
8. Process - Process initiated for the event
9. URL - Suspected url causing threat(Intrusion url)

Stream 3 - THREAT

**Vector - "WEB"** 
1. Action - The action code indicating what action was taken for the message.
2. Threat - Name of the threat identified
3. SrcIP - IP added of the source
4. DstIP - Destination IP of communication
5. User - name of the user

Stream 4 - THREAT

**Vector - “EMAIL”** (This field needs to be pre-populated with the value ‘Email’)
1. SrcIP - Client IP
2. Sender - Sender
3. Recipient - Recipient
4. Threat - Name of the signature/AtkMsg indicating threat
4. Action - Action taken - blocked, quarantined

Stream 5 - AUTHENTICATION 

1. User - User trying to login
2. SrcIP - Client IP
3. System- authenticating server/Host
4. Action -User Logged On, Logon Authentication Failed(Events)
5. AuthProto - Authentication protocol
6. Reason - Reason for auth failure actions
7. Status - Response of the action, passed or failed

Stream 6 - IAM

1. User - User Name of the user
2. Action - Action taken by an admin user for accounts / policies
3. Role- Role details for role updation or modification events
4. TargetUser - Target account on which changes are being made
5. Status - status of the action taken


Stream 7 -CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
5. Status - status of the action taken

**Requirement Gathering and Analysis -**

**Useful Links:**

Darktrace https://www.darktrace.com/en/resources/ds-siems.pdf 
