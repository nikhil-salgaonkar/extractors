| Blueprint name          | Office                                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------------ |
| Description             | Extractor for the Office Collaboration (such as O365, GSuite ) be built using this blueprint document. |
| Creation date | 22 Jan 2021                                                                                            |
| Version                 | 0.1                                                                                                |
| Change Update           | -                                                                               |

**Number of Streams - 5**

Stream 1 - EmailGateway

1. Sender - The sender of the email.
2. Recipient - The recipient of the email.
3. Action - The action code indicating what action was taken for the message.
4. Subject -The subject of the email.
5. RemoteIP - Source/Dst IP
6. File - The filenames of all attachments on the email
7. Direction - Detects the flow inbound or outbound

Stream 2 - Authentication

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

Stream 4  - DOCUMENTS 

1. Action	- Use below list of actions, common for all
* ACCESSED
* UPLOADED
* DELETED
* REMOVED
* SHARED
* COPIED
* PREVIEWED
* EDITED
* LOCKED
* MOVED
* UNLOCKED
* PRINTED
* RENAMED
* RESTORED
* VIEWED
* MODIFIED
* PERMISSION_CHANGED
* VERSIONS_RECYCLED
2. User - owner
3. File - filename	
4. SrcIP - source	
5. Visibility - detects access on shared file - eg. values: public external private	

Stream 5 - CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

**Requirement Gathering and Analysis -**

**Useful Links:**

Office 365

https://docs.microsoft.com/en-us/microsoft-365/compliance/detailed-properties-in-the-office-365-audit-log?view=o365-worldwide

https://docshttps://docs.microsoft.com/en-us/microsoft-365/compliance/detailed-properties-in-the-office-365-audit-log?view=o365-worldwide.microsoft.com/en-us/microsoft-365/compliance/search-the-audit-log-in-security-and-compliance?view=o365-worldwide

GSuite

https://support.google.com/a/answer/9725452
