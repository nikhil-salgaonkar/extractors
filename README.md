# dnif-extractors
Plug and play extractors that convert different log events to a common DNIF Data Model (DDM)

## Extractors
As of 14-06-2021

This is available here : https://docs.google.com/document/d/1O6ynQrvKTtw38VwyaXJk-U3EqPdAeJMue4gfstBkf5Y/edit#

| Type              | Vendor         | Product                           | Integration  | Stream                                                                                                                                                    |
| ----------------- | -------------- | --------------------------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OS                | Microsoft      | Windows                           | NXLog        | AUTHENTICATION, SYSMON-PROCESS, SYSMON-NETWORK, SYSMON-FILE, SYSMON-REGISTRY, SYSMON-IMAGE-LOAD, WIN-AUDIT, CONFIGURATION, THREAT, IAM                    |
| OS                | Microsoft      | Windows                           | Winlogbeat   | SYSMON-PROCESS, SYSMON-NETWORK, SYSMON-FILE, SYSMON-IMAGE-LOAD, SYSMON-REGISTRY, SYSMON-WMI, SYSMON-PIPE, SYSMON-SERVICE, SYSMON-DNS, IAM, AUTHENTICATION |
| OS                | ALL            | ALL                               | Auditbeat    | AUTHENTICATION, AUDITD                                                                                                                                    |
| OS                | Linux          | ALL                               | Syslog       | AUTHENTICATION, AUDITD, IAM                                                                                                                               |
| OS                | VMWare         | VMWare                            | Syslog       | AUTHENTICATION, CONFIGURATION, AUDITD                                                                                                                     |
| OS                | Cisco          | Cisco OS                          | Syslog       | AUTHENTICATION, CONFIGURATION, FIREWALL, IAM                                                                                                              |
| FIREWALL          | Sophos         | Cyberoam Firewall                 | Syslog(KV)   | AUTHENTICATION, THREAT, FIREWALL, IAM, CONFIGURATION                                                                                                      |
| FIREWALL          | Cisco          | Cisco ASA                         | Syslog       | AUTHENTICATION, THREAT, FIREWALL, CONFIGURATION, IAM                                                                                                      |
| FIREWALL          | WatchGuard     | WatchGuard Firewall               | Syslog       | FIREWALL, THREAT, AUTHENTICATION, CONFIGURATION                                                                                                           |
| FIREWALL          | PaloAlto       | Palo Alto Networks                | Syslog(LEEF) | FIREWALL, THREAT, AUTHENTICATION, CONFIGURATION                                                                                                           |
| FIREWALL          | Fortinet       | FortiManager                      | Syslog(KV)   | AUTHENTICATION, CONFIGURATION                                                                                                                             |
| FIREWALL          | Juniper        | Juniper-Firewall                  | Syslog(KV)   | FIREWALL, THREAT                                                                                                                                          |
| FIREWALL          | Fortinet       | FortiGate                         | Syslog(KV)   | FIREWALL, THREAT, AUTHENTICATION, CONFIGURATION                                                                                                           |
| FIREWALL          | Cisco          | Cisco FMC                         | Syslog       | AUTHENTICATION, FIREWALL, THREAT, CONFIGURATION                                                                                                           |
| FIREWALL          | Checkpoint     | Checkpoint                        | Syslog(KV)   | THREAT, FIREWALL, AUTHENTICATION                                                                                                                          |
| FIREWALL          | Cisco          | Cisco FTD                         | Syslog       | FIREWALL, THREAT, AUTHENTICATION                                                                                                                          |
| FIREWALL          | Zscaler        | Zscaler Firewall                  | Syslog       | FIREWALL, AUTHENTICATION, IAM, THREAT                                                                                                                     |
| WAF               | Imperva        | Imperva WAF                       | Syslog(CEF)  | THREAT                                                                                                                                                    |
| WAF               | Citrix         | NetScaler WAF                     | Syslog(CEF)  | THREAT                                                                                                                                                    |
| WAF               | F5 BIG-IP      | F5 BIG-IP                         | Syslog(CEF)  | THREAT                                                                                                                                                    |
| ENDPOINT-SECURITY | VMWare         | Carbon Black Response             | Syslog(KV)   | THREAT                                                                                                                                                    |
| ENDPOINT-SECURITY | McAfee         | McAfee EPO                        | Syslog(KV)   | THREAT                                                                                                                                                    |
| ENDPOINT-SECURITY | Trendmicro     | Trendmicro Officescan             | Syslog(KV)   | THREAT                                                                                                                                                    |
| ENDPOINT-SECURITY | Sophos         | Sophos Endpoint                   | Syslog(KV)   | THREAT, IAM                                                                                                                                               |
| ENDPOINT-SECURITY | Dell           | Dell Cylance                      | Syslog(KV)   | THREAT, IAM, AUTHENTICATION                                                                                                                               |
| ENDPOINT-SECURITY | McAfee         | McAfee DLP                        | Syslog       | THREAT, AUTHENTICATION                                                                                                                                    |
| ENDPOINT-SECURITY | VMWare         | Carbon Black Defense              | Syslog(KV)   | THREAT, AUTHENTICATION                                                                                                                                    |
| ENDPOINT-SECURITY | Forcepoint     | Forcepoint DLP                    | Syslog(CEF)  | THREAT                                                                                                                                                    |
| ENDPOINT-SECURITY | Trend Micro    | Trend-Micro Endpoint              | Syslog(KV)   | THREAT, AUTHENTICATION, IAM                                                                                                                               |
| ENDPOINT-SECURITY | VMWare         | Carbon Black EPP                  | Syslog(KV)   | THREAT                                                                                                                                                    |
| ENDPOINT-SECURITY | Broadcom       | Symantec Endpoint Security        | Syslog(KV)   | THREAT                                                                                                                                                    |
| ENDPOINT-SECURITY | Broadcom       | Symantec ATP                      | Syslog(KV)   | THREAT                                                                                                                                                    |
| THREAT            | FireEye Inc.   | FireEye Threat                    | Syslog(CEF)  | THREAT                                                                                                                                                    |
| OFFICE            | Microsoft      | MS O365                           | Office 365   | EMAIL-GATEWAY, AUTHENTICATION, IAM, DOCUMENTS                                                                                                             |
| WEBFILTER         | Forcepoint     | Websense WebFilter                | Syslog(CEF)  | WEBFILTER                                                                                                                                                 |
| WEBFILTER         | McAfee         | McAfee Web Gateway                | Syslog(CEF)  | AUTHENTICATION, THREAT, WEBFILTER                                                                                                                         |
| WEBFILTER         | ZScaler        | ZScaler WebFilter                 | Syslog(LEEF) | WEBFILTER                                                                                                                                                 |
| IPS               | Trend Micro    | TippingPoint                      | Syslog       | AUTHENTICATION                                                                                                                                            |
| MAILSERVER        | Microsoft      | Microsoft Exchange Server         | Syslog       | EMAIL-GATEWAY                                                                                                                                             |
| DNS               | ZScaler        | ZScaler DNS                       | Syslog       | DNS                                                                                                                                                       |
| DHCP              | Microsoft      | Windows                           | Syslog       | DHCP                                                                                                                                                      |
| WEBSERVER         | Microsoft      | IIS Webserver                     | NXLog        | WEBSERVER                                                                                                                                                 |
| WEBSERVER         | Apache         | Apache Webserver                  | Syslog       | WEBSERVER, AUTHENTICATION                                                                                                                                 |
| DECOY             | Smokescreen    | Smokescreen Decoy                 | Syslog(CEF)  | THREAT                                                                                                                                                    |
| ZERO-TRUST        | Versa Networks | Versa Networks Zero Trust         | Syslog(KV)   | FIREWALL, WEBFILTER, THREAT                                                                                                                               |
| CLOUD             | Amazon         | AWS CloudTrail                    | NXLog        | AUTHENTICATION, CONFIGURATION, CLOUDTRAIL, IAM                                                                                                            |
| ACCESS-GATEWAY    | Cisco          | Cisco ACS                         | Syslog(KV)   | AUTHENTICATION                                                                                                                                            |
| MANAGEMENT-SERVER | FireEye Inc.   | FireEye Audit                     | Syslog       | AUTHENTICATION, CONFIGURATION                                                                                                                             |
| MANAGEMENT-SERVER | Check Point    | Check Point Software Technologies | Syslog       | IAM, AUTHENTICATION                                                                                                                                       |

The DDM repository can be found here : https://github.com/dnif/extractors/tree/master/docs/Blueprint 
