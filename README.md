# dnif-extractors
Plug and play extractors that convert different log events to a common DNIF Data Model (DDM)

## Extractors
This is a live information on the exctractors that are ready.

|Device-Type   			                |	    Device          | Streams                         	           |
|-----------------------------------|---------------------|----------------------------------------------|
|OS       							            |Windows (nxlog)      | AUTHENTICATION,IAM, SYSMON         	         |
|OS       							            |Windows(winlogbeat)  | AUTHENTICATION,IAM, SYSMON                   |
|OS       							            |Windows(xml)         | SYSMON         	                             |      
|OS       							            |Linux (Auditbeat)    | AUTHENTICATION,AUDITD              	     		 |
|OS       							            |Linux (Syslog)       | AUTHENTICATION                             	 |
|OS       							            |VMware(Syslog)       | AUTHENTICATION                          		 |
|Firewall							              |Fortigate            | FIREWALL,THREAT,AUTHENTICATION,IAM 	 			   |
|Firewall							              |Cisco-FMC            | FIREWALL,THREAT,AUTHENTICATION,IAM 	 		     |
|Firewall							              |PaloAlto             | FIREWALL,THREAT,AUTHENTICATION,IAM 	 			   |
|Firewall							              |Checkpoint           | FIREWALL,THREAT,AUTHENTICATION,IAM 	 			   |
|Firewall                           |Sophos cyberoam      | FIREWALL,THREAT,AUTHENTICATION,IAM 					 |
|Firewall							              |Fortinet fortimanager| AUTHENTICATION		    		                   |
|Firewall           							  |Juniper-SRX          | FIREWALL,THREAT,AUTHENTICATION               |
|Firewall                           |ZScaler				      | FIREWALL,THREAT,AUTHENTICATION,IAM 			  	 |
|EmailGateway  						          |Mimecast 	          | EMAIL, THREAT, AUTHENTICATION, IAM		       |
|Endpoint Security                  |Carbonblack EPP      | THREAT	                                     |
|Endpoint Security                  |Symantec AV		      | THREAT								              		     |
|Endpoint Security							    |Sophos Endpoint      | THREAT, IAM                                  |
|Endpoint Security								  |Symantec ATP         | THREAT                         	 			       |
|Endpoint Security							    |DELL-CYLANCE         | THREAT                                       |
|EDR                                |Carbonblack Reponse  | THREAT								                       |
|EDR                                |Carbonblack Defense  | THREAT								                 		   |
|Webfiler							              |ZScaler			        | WEBFILTER,AUTHENTICATION, IAM		    		     |
|Office                             |O365				          | EMAIL, AUTHENTICATION, IAM				  		     |
|Azure							                |Azure                | AZURE                                			   |
|AWS							                  |AWS-Cloudtrail       | CLOUDTRAIL                         	 			   |




<!--|GCP							                  |GCP                | AUTHENTICATION, GCP                	 			   |-->
<!---|Firewall							        |ZScaler			      | FIREWALL,THREAT,AUTHENTICATION,IAM 	|Custom			| -->
<!---|DNS								            |ZScaler			      | DNS, IAM								            |Custom			| -->

## In progress
|Cisco FTD        |
|Watchguard       |
|McAfee gateway   |
|TREND-MICRO      |
|Symantec Endpoint|

