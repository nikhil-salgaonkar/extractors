| Blueprint name          | Network OS                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------- |
| Description             | Extractors for the Network devices using the same OS will be built using this blueprint document. |
| Blueprint creation date | 9 April, 2021                                                                                     |
| Author                  | Sharron, Lenora                                                                                   |
| Review Date             | 9 April, 2021 (Content team Internal) With Nikhil (9 April 2021)                                  | 

**DEVICE Type = Network**

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

1. Vector = “Network” (This field needs to be pre-populated with the value ‘Network’)
2. Action - The action code indicating what action was taken for the message.
3. Threat - Names of threats identified
4. SrcIP - The source IP address
5. DstIP - The destination IP address
6. User - the name of the user

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
2. Action - Action that was taken by an admin user for accounts/policies
3. Role- Role details for role updation or modification events
4. TargetUser - Target account on which changes are being made
5. Status - Status of the action taken

Stream 5 - CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - Status of the action taken

**Requirement Gathering and Analysis -** 

**Useful Links:**

https://tools.cisco.com/security/center/resources/identify_incidents_via_syslog

https://www.juniper.net/documentation/en_US/release-independent/nce/topics/task/operational/chassis-cluster-srx-log-message-configuring.html 

https://apps.juniper.net/syslog-explorer/#view=explore 

https://www.cisco.com/c/en/us/td/docs/ios/15_0sy/system/messages/15sysmg.pdf
