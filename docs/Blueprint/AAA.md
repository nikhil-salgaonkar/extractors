| Blueprint name          | AAA Extractor Blueprint                                                                                                                      |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Description             | Extractor for devices using AAA(Authentication, Authorization, Accounting) such as Cisco TACACS will be built using this blueprint document. |
| Blueprint creation date | 02 June 2021                                                                                                                                 |
| Author                  | Sharron                                                                                                                                      |
| Review Date             |                                                                                                                                              |
| Change Update           |                                                                                                                                              |

**Number of Streams - 3**

Stream 1 - Authentication 

1. User - User trying to login
2. SrcIP - Client IP
3. System - authenticating server/Host
4. Action - User Logged On, Logon Authentication Failed(Events)
5. AuthProto - Authentication protocol
6. Reason - Reason for auth failure actions
7. Status - Response of the action, passed or failed

Stream 2 - IAM

1. User - User Name of the user
2. Action - Action taken by an admin user for accounts / policies
3. Role - Role details for role updation or modification events
4. TargetUser - Target account on which changes are being made
5. Status - status of the action taken

Stream 3 -CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

**Requirement Gathering and Analysis -** 

**Useful Links:**

https://www.juniper.net/documentation/us/en/software/junos/user-access/topics/topic-map/user-access-tacacs-authentication.html

https://www.cisco.com/en/US/docs/net_mgmt/cisco_secure_access_control_server_for_windows/4.1/user/LgsRpts.html 

https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/sec_usr_tacacs/configuration/xe-3s/sec-usr-tacacs-xe-3s-book/sec-cfg-tacacs.pdf 

https://www.cisco.com/c/en/us/td/docs/net_mgmt/cisco_secure_access_control_system/5-8/user/guide/acsuserguide/logging.html
