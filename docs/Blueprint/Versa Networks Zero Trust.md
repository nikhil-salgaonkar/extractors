| Blueprint name          | Versa Networks Zero Trust                                                             |
| ----------------------- | ------------------------------------------------------------------------------------- |
| Description             | Extractor for Versa Networks Zero Trust  will be built using this blueprint document. |
| Blueprint creation date | 21 May 2021                                                                           |
| Author                  | Sherin                                                                                |
| Review Date             | Sharron 21 May 2021                                                                   |

**Number of Streams - 6**

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

Stream 3 - CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

Stream 4 - THREAT

**Vector = “NETWORK”** (This field needs to be pre-populated with the value ‘Network’)	
1. Action - The action code indicating what action was taken for the message.	
2. Threat - Names of threats identified			
3. SrcIP - The source IP address			
4. DstIP - The destination IP address			
				
**Vector = “HOST"**			
1. SrcIP - Internal IP address/ External Ip address based on direction			
2. DstIP - Internal IP address/ External Ip address based on direction			
3. Threat - Name of the signature for which a signal is triggered			
4. File - Application name causing threat			
5. Process - Process initiated for the event			
6. URL - Suspected url causing threat(Intrusion url)			
7. CommandLine- Command passed for the process			
8. Action - Action taken which is blocked or quarantined			
9. User - for any user who starts a process			

Stream 5 - FIREWALL
		
1. SrcIP - Source IP address					
2. DstIP - Destination IP address					
3. Action - The action code indicating what action was taken for the message.		
4. Proto -The protocol used by web traffic.					
5. SrcPort - Port number of the traffic's origin.					
6. DstPort - Port number of the traffic's destination.					
7. App - The network application that was accessed.					
8. TXLen - sent bytes					
9. RXLen - received bytes	

Stream 6 - WEB FILTER	
	
1. Action - The action code indicating what action was taken for the message
2. URL - The URL accessed	
3. HTTPMethod - Method associated with the request	
4. SrcIP - The source IP of the request.	
5. DstIP - Destination IP of the communication	
6. UserAgent - Contents of the User-Agent	
7. DstPort - Destination port of the request	
8. User - name of the user sending the request	
9. Proto - Protocol used	
10. TXLen - sent bytes	
11. RXLen - received bytes	

**Requirement Gathering and Analysis -**

**Useful Links:**

https://versa-networks.com/

https://drive.google.com/file/d/1Du7JO1cHCJK4oIF4ila2_GiIRzoR-D6u/view?usp=sharing
