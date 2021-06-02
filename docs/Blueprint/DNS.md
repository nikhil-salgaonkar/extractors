| Blueprint name          | DNS                                                            |
| ----------------------- | -------------------------------------------------------------- |
| Description             | Extractor for DNS will be built using this blueprint document. |
| Blueprint creation date | 27 Jan 2021                                                    |
| Author                  | Lenora                                                         |
| Review Date             | Reconciled by Shweta as per Stream DDM - 18 March              |

**Number of Streams - 3**

Stream 1 - DNS

1. Action - The action code indicating what action was taken for the message, includes category
2. ScrIP - The source IP of the request.
3. Query - Name of the DNS query
4. ResponseCode - (NOERROR, NXDOMAIN, SERVFAIL)
5. QueryType - Values : recursive,iterative and non recursive
6. RecordType - provide important information about a domain or hostname (eg. A, MX, TXT, AAAA)

Stream 2 - IAM

1. User - User Name of the user
2. Action - Action taken by an admin user for accounts / policies
3. Role- Role details for role updation or modification events
4. TargetUser - Target account on which changes are being made
5. Status - status of the action taken

Stream 3 - CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

Stream 3 - AUTHENTICATION

1. User - Username of the user attempting to authenticate
2. ScrIP - Client IP
3. Action -User Logged On, Logon Authentication Failed(Events)
4. Reason - Reason for auth failure actions
5. AuthProto - Authentication protocol
6. Status - Response of the action, passed or failed 
7. System - authenticating server/Host

**Requirement Gathering and Analysis -**

**Useful Links:**

Zscaler

https://help.zscaler.com/zia/nss-feed-output-format-dns-logs


Windows DNS

https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/dn800669(v=ws.11)

https://nxlog.co/documentation/nxlog-user-guide/windows-dns-server.html


