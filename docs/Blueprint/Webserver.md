| Blueprint name          | Webserver                                                                |
| ----------------------- | ------------------------------------------------------------------------ |
| Description             | Extractor for the Webserver will be built using this blueprint document. |
| Creation date | 18 Feb 2021                                                              |
| Version                 | 0.1                                                            |
| Change Update           |  -                                                             |

**Number of Streams - 5**

Stream 1 - WEBSERVER

1. SrcIP - Client IP
2. Method - The requested action, for example, a GET method.
3. UriQuery - The query, if any that the client was trying to perform.
4. User - The name of the authenticated user who accessed your server.
5. UserAgent - The browser type that the client used.
6. URL - specifies the URL for the streaming content originally requested by the client.
7. ReturnCode - Response code
8. System - System name

Stream 2 - THREAT 

1. Vector - ‘WEB’
2. Action - The action code indicating what action was taken for the message.
3. Threat - Name of the threat identified
4. SrcIP - IP added of the source
5. DstIP - Destination IP of communication
6. User - name of the user

Stream 3 -CONFIGURATION

1. User - User who made changes
2. Action - Action taken
3. Config - Configuration name
4. Status - status of the action taken

Stream 4 - AUTHENTICATION 

1. User - User trying to login
2. SrcIP - Client IP
3. System- authenticating server/Host
4. Action - User Logged On, Logon Authentication Failed(Events)
5. AuthProto - Authentication protocol
6. Reason - Reason for auth failure actions
7. Status - Response of the action, passed or failed

Stream 5 - IAM

1. User - User Name of the user
2. Action - Action taken by an admin user for accounts / policies
3. Role - Role details for role updation or modification events
4. TargetUser - Target account on which changes are being made
5. Status - status of the action taken

**Requirement Gathering and Analysis -** 

**Useful Links:**

https://www.loggly.com/ultimate-guide/apache-logging-basics/

https://stackify.com/how-to-interpret-iis-logs/

https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-wmlog/95432035-197b-4232-8154-d8740c8e14a5

https://www.gsa.gov/cdnstatic/Web_Server_Log_Review_%5BCIO_IT_Security_08-41_Rev_4%5D_03_25_2020docx.pdf
