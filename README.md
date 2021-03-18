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
|DHCP                               |Windows -DHCP        | DHCP
|Firewall							              |Fortigate            | FIREWALL,THREAT,AUTHENTICATION,IAM 	 			   |
|Firewall							              |Cisco-FMC            | FIREWALL,THREAT,AUTHENTICATION,IAM 	 		     |
|Firewall							              |PaloAlto             | FIREWALL,THREAT,AUTHENTICATION,IAM 	 			   |
|Firewall							              |Checkpoint           | FIREWALL,THREAT,AUTHENTICATION,IAM 	 			   |
|Firewall                           |Sophos cyberoam      | FIREWALL,THREAT,AUTHENTICATION,IAM 					 |
|Firewall							              |Fortinet fortimanager| AUTHENTICATION		    		                   |
|Firewall           							  |Juniper-SRX          | FIREWALL,THREAT,AUTHENTICATION               |
|Firewall                           |ZScaler				      | FIREWALL,THREAT,AUTHENTICATION,IAM 			  	 |
|EmailGateway  						          |Mimecast 	          | EMAIL, THREAT, AUTHENTICATION, IAM		       |
|Endpoint Security                  |Symantec AV		      | THREAT								              		     |
|Endpoint Security                  |McAfee EPO   	      | THREAT								              		     |
|Endpoint Security							    |Sophos Endpoint      | THREAT, IAM                                  |
|Endpoint Security								  |Symantec ATP         | THREAT                         	 			       |
|Endpoint Security							    |DELL-CYLANCE         | THREAT                                       |
|Endpoint Security	                |Carbonblack EPP      | THREAT								                       |
|EDR                                |Carbonblack Reponse  | THREAT								                       |
|EDR                                |Carbonblack Defence  | THREAT								                       |
|Webfiler							              |ZScaler			        | WEBFILTER,AUTHENTICATION, IAM		    		     |
|Cloud							                |AWS-Cloudtrail       | CLOUDTRAIL                         	 			   |



<!--|GCP							                  |GCP                | AUTHENTICATION, GCP                	 			   |-->
<!---|Firewall							        |ZScaler			      | FIREWALL,THREAT,AUTHENTICATION,IAM 	|Custom			| -->
<!---|DNS								            |ZScaler			      | DNS, IAM								            |Custom			| -->

## In progress
|Cisco FTD          |
|Watchguard         |
|McAfee gateway     |
|TREND-MICRO        |
|O365               |
|Azure              |
|F5BIGIP-CEF        |

