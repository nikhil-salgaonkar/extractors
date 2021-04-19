# dnif-extractors
Plug and play extractors that convert different log events to a common DNIF Data Model (DDM)

## Extractors
As of 08-04-2021

|Device-Type           |	    Vendor          | Product             | Integration | Streams                                                                      |
|----------------------|----------------------|---------------------|-------------|------------------------------------------------------------------------------|
|OS       		         |Microsoft             |Windows (nxlog)      | NXLog (JSON)|AUTHENTICATION, IAM, SYSMON-PROCESS,  SYSMON-NETWORK,  SYSMON-REGISTRY,  SYSMON-IMAGE-LOAD|
|OS   		             |Microsoft             |Windows(winlogbeat)   |Winlogbeat (OSS)     | AUTHENTICATION, IAM, SYSMON-PROCESS,  SYSMON-NETWORK,  SYSMON-FILE,  SYSMON-IMAGE-LOAD,  SYSMON-REGISTRY,  SYSMON-WMI,  SYSMON-PIPE,  SYSMON-SERVICE,  SYSMON-DNS|                                                            |
|OS|Linux|ALL|Auditbeat (OSS)|AUTHENTICATION, AUDITD|
|OS|Linux|ALL|Rsyslog|AUTHENTICATION|
|OS|VMWare|VMWare|Syslog|AUTHENTICATION, CONFIGURATION|
|OS|Cisco| IOS | Syslog |AUTHENTICATION , FIREWALL|
|Firewall|Fortinet|Fortigate|Syslog|FIREWALL, THREAT, AUTHENTICATION|
Firewall |PaloAlto |Palo Alto Firewall |CSV |FIREWALL,THREAT, AUTHENTICATION |
Firewall |Checkpoint |Checkpoint Firewall | Syslog |FIREWALL,THREAT, AUTHENTICATION |
Firewall |Cisco |Cisco-FMC |Syslog |FIREWALL,THREAT, AUTHENTICATION |
Firewall |Cisco |Cisco - FTD |Syslog |FIREWALL, THREAT, AUTHENTICATION |
Firewall |Sophos |Cyberoam Firewall |Syslog |FIREWALL,THREAT, AUTHENTICATION, IAM |
Firewall |Fortinet  |fortimanager |Syslog |AUTHENTICATION |
Firewall |Juniper |Juniper |Syslog |FIREWALL,THREAT, AUTHENTICATION |
Firewall |Zscaler |Zscaler-Firewall |NSS (CSV) |FIREWALL,THREAT, AUTHENTICATION, IAM |
Webfilter |ZScaler |ZScaler-Web Filter |NSS (LEEF) |WEBFILTER |
Webfilter |Forcepoint |Websense Webfilter |Syslog |WEBFILTER |
Email Gateway|Mimecast|Mimecast-EWSA|Syslog|EMAIL- GATEWAY, THREAT, AUTHENTICATION, IAM|
Endpoint Security|Broadcom |Symantec Endpoint security|Syslog|THREAT|
Endpoint Security|DELL|Dell-Cylance|Syslog|THREAT|
Endpoint Security|Broadcom|Symantec ATP|Syslog|THREAT|
Endpoint Security |VMWare|Carbon Black Defense|Syslog|THREAT|
Endpoint Security|VMWare|Carbon Black EPP|Syslog|THREAT|
Endpoint Security|McAfee|McAfee - EPO|Syslog|THREAT|
Endpoint Security|Sophos|Sophos Endpoint|Syslog|THREAT , IAM|
Endpoint Security|Trendmicro|Trendmicro Offiscan|Syslog|THREAT|
EDR|VMware|Carbonblack Response|Syslog|THREAT|
Cloud|AWS|AWS-Cloudtrail|JSON|CLOUDTRAIL|
Cloud|Microsoft|MS-O365|JSON|EMAIL-GATEWAY,  AUTHENTICATION, IAM, DOCUMENTS|
Web Application Firewall|F5 BIG-IP |F5 Big-IP|CEF| THREAT|
Web Application Firewall|Imperva|Imperva WAF|Syslog|THREAT|
Advanced Persistent Threat(APT)|Fireeye Inc.|Fireeye APT|CEF|THREAT|
DNS|ZScaler|Zscaler|Syslog|DNS|
DHCP|Microsoft|Windows|Syslog|DHCP|







