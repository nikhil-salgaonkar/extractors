| Blueprint name          | Mail Server                                                               |
| ----------------------- | ------------------------------------------------------------------------- |
| Description             | Extractor for the Mail server can be built using this blueprint document. |
| Creation date | 25 March 2021                                                             |
| Version                 | 0.1                                                                                                |
| Change Update           |                                                                              |


**Number of Streams - 4**

Stream 1 - Authentication

1. User - User trying to login
2. SrcIP - Client IP
3. System- authenticating server/Host
4. Action -User Logged On, Logon Authentication Failed(Events)
5. AuthProto - Authentication protocol
6. Reason - Reason for auth failure actions
7. Status - Response of the action, passed or failed

Stream 2 - IAM

1. User - User Name of the user
2. Action - Action taken by an admin user for accounts / policies
3. Role- Details regarding role name for role updation or modification events
4. TargetUser - Target account on which changes are being made
5. Status - status of the action taken

Stream 3 -  CONFIGURATION

1. User - User who made changes
2. Action - action taken
3. Config - Configuration name
4. Status- Status of the action taken

Stream 4 - EMAIL-GATEWAY

1. Sender - The sender of the email.
2. Recipient - The recipient of the email.
3. Action - The action code indicating what action was taken for the message.
4. Subject -The subject of the email.
5. RemoteIP - Client IP
6. File - The filenames of all attachments on the email
7. Direction - Detects the flow inbound or outbound

**Requirement Gathering and Analysis -** 

**Useful Links:**

https://docs.microsoft.com/en-us/exchange/policy-and-compliance/mailbox-audit-logging/mailbox-audit-logging?view=exchserver-2019

https://docs.microsoft.com/en-us/Exchange/policy-and-compliance/admin-audit-logging/admin-audit-logging?redirectedfrom=MSDN&view=exchserver-2019 
