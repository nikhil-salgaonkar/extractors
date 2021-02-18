# dnif-extractors
Plug and play extractors that convert different log events to a common DNIF Data Model (DDM)

## Extractors
This is a live information on the exctractors that are ready.

|Device-Type   			                |	    Device        | Streams                         	  |Extractor Type |
|-----------------------------------|-------------------|-------------------------------------|---------------|
|EmailGateway  						          |Mimecast 	        |EMAIL, THREAT, AUTHENTICATION, IAM		|Standard       |
|Endpoint Security                  |Carbonblack EPP    | Threat	                            |Standard       |
|EDR                                |Carbonblack Reponse| Threat								              |Standard       |
|EDR                                |Carbonblack Defense| Threat								              |Standard   		|
|Endpoint Security                  |Symantec AV		    | Threat								              |Standard		    |
|Webfiler							              |ZScaler			      | WEBFILTER,AUTHENTICATION, IAM		    |Standard			  |
|Office                             |O365				        | EMAIL, AUTHENTICATION, IAM				  |Standard		    |
|Firewall							              |Fortigate          | FIREWALL,THREAT,AUTHENTICATION,IAM 	|Standard 			|
|Firewall							              |Cisco-FMC          | FIREWALL,THREAT,AUTHENTICATION,IAM 	|Standard 			|
|Firewall							              |PaloAlto           | FIREWALL,THREAT,AUTHENTICATION,IAM 	|Standard 			|
|Firewall							              |Checkpoint         | FIREWALL,THREAT,AUTHENTICATION,IAM 	|Standard 			|
|Azure							                |Azure              | Azure                               |Standard 			|
|AWS							                  |AWS-Cludtrail      | Cludtrail                          	|Standard 			|
|OS       							            |Linux              | FIREWALL,THREAT,AUTHENTICATION,IAM 	|Standard 			|
|NIX          							        |Auditd             | AUDITD                              |Standard 			|
|Win-DHCP                           |Win-DHCP           | <Insert>                            |Standard 			|  



<!---|Firewall							        |ZScaler			      | FIREWALL,THREAT,AUTHENTICATION,IAM 	|Custom			| -->
<!---|DNS								            |ZScaler			      | DNS, IAM								            |Custom			| -->

## In progress
|Juniper Firewall |
|Juniper SRX      |


