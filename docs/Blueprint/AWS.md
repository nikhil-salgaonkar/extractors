| Blueprint name          | AWS                                                                |
| ----------------------- | ------------------------------------------------------------------ |
| Description             | Extractor for the AWS will be built using this blueprint document. |
| Blueprint creation date | 18 Feb 2021                                                        |
| Author                  | Aman, Lenora, sharron                                              |
| Review Date             |                                                                    |

**Number of Streams - 4**

Stream 1 - AUTHENTICATION

1. User - User trying to login
2. SrcIP - Client IP
3. System- authenticating server/Host
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

Stream 4 - CLOUDTRAIL

1. EventType
2. EventSource 
3. EventName 
4. AwsRegion
5. AccessKey
6. UserGroup
7. SrcIP
8. UserAgent
9. RequestParameters
10. ResponseElements
11. ErrorCode
12. UserArn

**Requirement Gathering and Analysis -** 

**Useful Links:**
