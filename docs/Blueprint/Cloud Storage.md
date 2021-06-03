| Blueprint name          | Cloud Storage                                                                    |
| ----------------------- | -------------------------------------------------------------------------------- |
| Description             | Extractor for Cloud storage devices will be built using this blueprint document. |
| Blueprint creation date | 12 Mar 2021                                                                      |
| Author                  | Sharron, Reviewed by Nikhil                                                      |
| Review Date             | 16 March 2021                                                                    |

**Number of Streams - 3**

Stream 1 - AUTHENTICATION 

1. User - User trying to login
2. SrcIP - Client IP
3. Action - User Logged On, Logon Authentication Failed(Events)
4. AuthProto - Authentication protocol
5. Reason - Reason for auth failure actions
6. Status - Response of the action, passed or failed
7. System - authenticating server/Host

Stream 2 - DOCUMENTS 

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

Stream 3 - CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

**Requirement Gathering and Analysis -**

**Useful Links:**

https://developers.google.com/admin-sdk/reports/v1/appendix/activity/drive 

https://docs.microsoft.com/en-us/microsoft-365/compliance/detailed-properties-in-the-office-365-audit-log?view=o365-worldwide

https://dropbox.tech/developers/converting-the-dropbox-activity-log-into-common-event-framework-

https://support.box.com/hc/en-us/articles/360043696534-Running-Reports#useractivity 
