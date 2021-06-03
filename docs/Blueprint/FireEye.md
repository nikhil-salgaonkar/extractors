| Blueprint name          | FireEye Extractor Blueprint                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- |
| Description             | Extractor for FireEye CMS, MPS, EX, AX, NX, FX, and HX appliances will be built using this blueprint document. |
| Blueprint creation date | 02 June 2021                                                                                                   |
| Author                  | Sharron                                                                                                        |
| Review Date             |                                                                                                                |

**FIREEYE Data Model**

SourceName- FireEye   
SourceType- Threat

**Number of Streams - 1**

**Stream 1- Threat**
		
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

**Vector = “EMAIL"**		
1. SrcIP - Client IP		
2. Sender - Sender		
3. Recipient - Recipient		
4. Threat - Name of the signature for which a signal is triggered		
5. Action - Action taken - blocked, quarantined

**Requirement Gathering and Analysis -**

**Useful Links:**

https://www.fireeye.com/content/dam/fireeye-www/global/en/products/pdfs/tap-amazon-user-guide.pdf 

https://www.fireeye.com/content/dam/fireeye-www/global/en/partners/pdfs/fireeye-splunk-intro-to-integration.pdf 

https://docs.mcafee.com/bundle/enterprise-security-manager-data-sources-configuration-reference-guide/page/GUID-DEE7F31A-23FA-4A89-B641-C2DF422E7748.html 
