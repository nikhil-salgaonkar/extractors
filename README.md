# dnif-extractors
Plug and play extractors that convert different log events to a common DNIF Data Model (DDM)

## Extractors (Beta)
As of 19-07-2021

This is available here : [DNIF Supported Log Sources](https://docs.google.com/document/d/1O6ynQrvKTtw38VwyaXJk-U3EqPdAeJMue4gfstBkf5Y/edit#)

| Type              | Vendor         | Product                           | Integration   | Stream                                                                                                                                                                                                                         |
| ----------------- | -------------- | --------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| OS                | Microsoft      | Windows                           | NXLog         | AUTHENTICATION, SYSMON-PROCESS, SYSMON-NETWORK, SYSMON-FILE, SYSMON-DNS, SYSMON-REGISTRY, SYSMON-IMAGE-LOAD, WIN-AUDIT, CONFIGURATION, THREAT, IAM, SYSMON-DRIVER-LOAD, SYSMON-SERVICE, SYSMON-WMI, SYSMON-PIPE, SYSMON-CONFIG |
| OS                | Microsoft      | Windows                           | Winlogbeat    | SYSMON-PROCESS, SYSMON-NETWORK, SYSMON-FILE, SYSMON-IMAGE-LOAD, SYSMON-REGISTRY, SYSMON-WMI, SYSMON-PIPE, SYSMON-SERVICE, SYSMON-DNS, SYSMON-DRIVER-LOAD, SYSMON-CONFIG, IAM, AUTHENTICATION, WIN-AUDIT, CONFIGURATION, THREAT |
| OS                | ALL            | ALL                               | Auditbeat     | AUTHENTICATION, AUDITD                                                                                                                                                                                                         |
| OS                | Linux          | ALL                               | Syslog        | AUTHENTICATION, AUDITD, IAM                                                                                                                                                                                                    |
| OS                | VMWare         | VMWare                            | Syslog        | AUTHENTICATION, CONFIGURATION, AUDITD                                                                                                                                                                                          |
| OS                | Cisco          | Cisco OS                          | Syslog        | AUTHENTICATION, CONFIGURATION, FIREWALL, IAM                                                                                                                                                                                   |
| FIREWALL          | Sophos         | Cyberoam Firewall                 | Syslog(KV)    | AUTHENTICATION, THREAT, FIREWALL, IAM, CONFIGURATION                                                                                                                                                                           |
| FIREWALL          | Cisco          | Cisco ASA                         | Syslog        | AUTHENTICATION, THREAT, FIREWALL, CONFIGURATION, IAM                                                                                                                                                                           |
| FIREWALL          | WatchGuard     | WatchGuard Firewall               | Syslog        | FIREWALL, THREAT, AUTHENTICATION, CONFIGURATION                                                                                                                                                                                |
| FIREWALL          | PaloAlto       | Palo Alto Networks                | Syslog(LEEF)  | FIREWALL, THREAT, AUTHENTICATION, CONFIGURATION                                                                                                                                                                                |
| FIREWALL          | Fortinet       | FortiManager                      | Syslog(KV)    | AUTHENTICATION, CONFIGURATION                                                                                                                                                                                                  |
| FIREWALL          | Juniper        | Juniper-Firewall                  | Syslog(KV)    | FIREWALL, THREAT                                                                                                                                                                                                               |
| FIREWALL          | Fortinet       | FortiGate                         | Syslog(KV)    | FIREWALL, THREAT, AUTHENTICATION, CONFIGURATION                                                                                                                                                                                |
| FIREWALL          | Netgate        | pfSense                           | Syslog        | FIREWALL                                                                                                                                                                                                                       |
| FIREWALL          | Cisco          | Cisco FMC                         | Syslog        | AUTHENTICATION, FIREWALL, THREAT, CONFIGURATION                                                                                                                                                                                |
| FIREWALL          | CheckPoint     | CheckPoint Firewall               | Syslog(KV)    | THREAT, FIREWALL, AUTHENTICATION, CONFIGURATION                                                                                                                                                                                |
| FIREWALL          | Cisco          | Cisco FTD                         | Syslog        | FIREWALL, THREAT, AUTHENTICATION                                                                                                                                                                                               |
| FIREWALL          | Zscaler        | Zscaler Firewall                  | Syslog        | FIREWALL, AUTHENTICATION, IAM, THREAT                                                                                                                                                                                          |
| WAF               | Radware        | Radware                           | Syslog(KV)    | THREAT, AUTHENTICATION                                                                                                                                                                                                         |
| WAF               | Imperva        | Imperva WAF                       | Syslog(CEF)   | THREAT                                                                                                                                                                                                                         |
| WAF               | Citrix         | NetScaler WAF                     | Syslog(CEF)   | THREAT                                                                                                                                                                                                                         |
| WAF               | Fortinet       | FortiWeb WAF                      | Syslog(CEF)   | AUTHENTICATION, THREAT, IAM, CONFIGURATION, FIREWALL                                                                                                                                                                           |
| WAF               | F5 BIG-IP      | F5 BIG-IP                         | Syslog(CEF)   | THREAT                                                                                                                                                                                                                         |
| ENDPOINT-SECURITY | VMWare         | Carbon Black Response             | Syslog(KV)    | THREAT                                                                                                                                                                                                                         |
| ENDPOINT-SECURITY | McAfee         | McAfee EPO                        | Syslog(KV)    | THREAT                                                                                                                                                                                                                         |
| ENDPOINT-SECURITY | Trendmicro     | Trendmicro Officescan             | Syslog(KV)    | THREAT                                                                                                                                                                                                                         |
| ENDPOINT-SECURITY | Sophos         | Sophos Endpoint                   | Syslog(KV)    | THREAT, IAM                                                                                                                                                                                                                    |
| ENDPOINT-SECURITY | Dell           | Dell Cylance                      | Syslog(KV)    | THREAT, IAM, AUTHENTICATION                                                                                                                                                                                                    |
| ENDPOINT-SECURITY | McAfee         | McAfee DLP                        | Syslog        | THREAT, AUTHENTICATION                                                                                                                                                                                                         |
| ENDPOINT-SECURITY | VMWare         | Carbon Black Defense              | Syslog(KV)    | THREAT, AUTHENTICATION                                                                                                                                                                                                         |
| ENDPOINT-SECURITY | Forcepoint     | Forcepoint DLP                    | Syslog(CEF)   | THREAT                                                                                                                                                                                                                         |
| ENDPOINT-SECURITY | Trend Micro    | Trend-Micro Endpoint              | Syslog(KV)    | THREAT, AUTHENTICATION, IAM                                                                                                                                                                                                    |
| ENDPOINT-SECURITY | VMWare         | Carbon Black EPP                  | Syslog(KV)    | THREAT, IAM, AUTHENTICATION, CONFIGURATION                                                                                                                                                                                     |
| ENDPOINT-SECURITY | Broadcom       | Symantec Endpoint Security        | Syslog(KV)    | THREAT                                                                                                                                                                                                                         |
| ENDPOINT-SECURITY | Broadcom       | Symantec ATP                      | Syslog(KV)    | THREAT                                                                                                                                                                                                                         |
| THREAT            | FireEye Inc.   | FireEye Threat                    | Syslog(CEF)   | THREAT                                                                                                                                                                                                                         |
| THREAT            | Darktrace      | DCIP                              | Syslog(CEF)   | IAM, AUTHENTICATION, THREAT                                                                                                                                                                                                    |
| OFFICE            | Microsoft      | MS O365                           | Office 365    | EMAIL-GATEWAY, AUTHENTICATION, IAM, DOCUMENTS                                                                                                                                                                                  |
| WEBFILTER         | Forcepoint     | Websense WebFilter                | Syslog(CEF)   | WEBFILTER                                                                                                                                                                                                                      |
| WEBFILTER         | McAfee         | McAfee Web Gateway                | Syslog(CEF)   | AUTHENTICATION, THREAT, WEBFILTER                                                                                                                                                                                              |
| WEBFILTER         | ZScaler        | ZScaler WebFilter                 | Syslog(LEEF)  | WEBFILTER                                                                                                                                                                                                                      |
| IPS               | Cisco          | Cisco FirePOWER                   | Syslog(KV)    | THREAT                                                                                                                                                                                                                         |
| IPS               | Trend Micro    | TippingPoint                      | Syslog        | AUTHENTICATION, THREAT                                                                                                                                                                                                         |
| MAILSERVER        | Microsoft      | Microsoft Exchange Server         | Syslog        | EMAIL-GATEWAY                                                                                                                                                                                                                  |
| DNS               | ZScaler        | ZScaler DNS                       | Syslog        | DNS                                                                                                                                                                                                                            |
| DHCP              | Microsoft      | Windows                           | Syslog        | DHCP                                                                                                                                                                                                                           |
| WEBSERVER         | Microsoft      | IIS Webserver                     | NXLog         | WEBSERVER                                                                                                                                                                                                                      |
| WEBSERVER         | Red Hat        | JBoss WebServer                   | NXLog         | WEBSERVER                                                                                                                                                                                                                      |
| WEBSERVER         | F5             | Nginx Webserver                   | Syslog        | WEBSERVER                                                                                                                                                                                                                      |
| WEBSERVER         | Apache         | Tomcat Webserver                  | Syslog        | WEBSERVER                                                                                                                                                                                                                      |
| WEBSERVER         | Apache         | Apache Webserver                  | Syslog        | WEBSERVER, AUTHENTICATION                                                                                                                                                                                                      |
| DECOY             | Smokescreen    | Smokescreen Decoy                 | Syslog(CEF)   | THREAT                                                                                                                                                                                                                         |
| ZERO-TRUST        | Versa Networks | Versa Networks Zero Trust         | Syslog(KV)    | FIREWALL, WEBFILTER, THREAT                                                                                                                                                                                                    |
| CLOUD             | Amazon         | AWS CloudTrail                    | AWS S3        | AUTHENTICATION, CONFIGURATION, CLOUDTRAIL, IAM                                                                                                                                                                                 |
| ACCESS-GATEWAY    | PaloAlto       | Prisma Cloud                      | Prisma Alerts | CONFIGURATION                                                                                                                                                                                                                  |
| ACCESS-GATEWAY    | Cisco          | Cisco ACS                         | Syslog(KV)    | AUTHENTICATION                                                                                                                                                                                                                 |
| ACCESS-GATEWAY    | Okta           | Okta                              | Okta          | AUTHENTICATION, CONFIGURATION, IAM, THREAT                                                                                                                                                                                     |
| MANAGEMENT-SERVER | FireEye Inc.   | FireEye Audit                     | Syslog        | AUTHENTICATION, CONFIGURATION                                                                                                                                                                                                  |
| MANAGEMENT-SERVER | Check Point    | Check Point Software Technologies | Syslog        | IAM, AUTHENTICATION                                                                                                                                                                                                            |
| CLOUD-STORAGE     | Box            | Box Cloud Storage                 | Box           | DOCUMENTS, AUTHENTICATION, CONFIGURATION                                                                                                                                                                                       |
| PIM               | CyberArk       | CyberArk PIM                      | Syslog(CEF)   | AUTHENTICATION, THREAT, IAM, CONFIGURATION                                                                                                                                                                                     |

The DDM repository can be found here : [Blueprint](https://github.com/dnif/extractors/tree/master/docs/Blueprint )

Note - The above list of Extractors are DNIF's Supported Beta Extractors. DNIF brings improvements into these from performance and efficiency angle on continuous basis.
