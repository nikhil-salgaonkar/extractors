| Blueprint name          | GCP                                                                          |
| ----------------------- | ---------------------------------------------------------------------------- |
| Description             | Extractor for the GCP  will be built using this blueprint document.          |
| Blueprint creation date | 23 Feb 2021                                                                  |
| Author                  | Sharron                                                                      |
| Review Date             | With Nikhil (23 Feb 2021) Reconciled by Shweta as per Stream DDM - 18 March  |

Number of Streams - 4

Stream 1 - GCP

Dnif fields   | GCP fields           | Description                                                                                              |
| ----------- | -------------------- | ------------------------------------------------------------------------------------------------------ |
| SrcIP       | Caller IP            | The IP address (IPv4 or IPv6) of the client that issued the HTTP request                               |
| EventName   | Name                 | Name of the event                                                                                      |
| User        | Member               | User name                                                                                              |
| Action      | Action               | add del create insert update                                                                           |
| Operation   | methodName/Operation | The name of the service method or operation. For API calls, this should be the name of the API method. |
| Status      | Status               | Status of the action                                                                                   |

Stream 2 - Authentication(For VPC logs)

1. User - User trying to login
2. SrcIP - Client IP
3. System- authenticating server/Host
4. Action -User Logged On, Logon Authentication Failed(Events)
5. AuthProto - Authentication protocol
6. Reason - Reason for auth failure actions
7. Status - Response of the action, passed or failed

Stream 3 - IAM

1. User - User Name of the user
2. Action - Action taken by an admin user for accounts / policies
3. Role- Details regarding role name for role updation or modification events
4. TargetUser - Target account on which changes are being made
5. Status - status of the action taken

Stream 4 -CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

**Requirement Gathering and Analysis -**

**Useful Links:**

https://cloud.google.com/vpc/docs/audit-logging 

https://cloud.google.com/logging/docs/audit/understanding-audit-logs 

https://cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog 
