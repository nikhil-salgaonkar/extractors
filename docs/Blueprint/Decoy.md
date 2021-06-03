| Blueprint name          | Decoy                                                                |
| ----------------------- | -------------------------------------------------------------------- |
| Description             | Extractor for the Decoy will be built using this blueprint document. |
| Blueprint creation date | 6th April 2021                                                       |
| Author                  | Lenora                                                               |
| Review Date             |                                                                      |

**Number of Streams - 2**

Stream 1 - THREAT 

1. Vector = “WEB” (This field needs to be pre-populated with the value ‘Web’)
2. Action - The action code indicating what action was taken for the message.
3. Threat - Names of threats identified
4. SrcIP - The source IP address
5. DstIP - The destination IP address
6. User - name of the user

Stream 2 - THREAT

1. Vector = “HOST"
2. SrcIP - Internal IP address/ External Ip address based on direction
3. DstIP - Internal IP address/ External Ip address based on direction
4. Threat - Name of the signature for which a signal is triggered
5. File - Application name causing threat
6. Process - Process initiated for the event
7. URL - Suspected url causing threat(Intrusion url)
8. CommandLine- Command passed for the process
9. Action - Action taken which is blocked or quarantined
10. User - for any user who starts a process

**Requirement Gathering and Analysis -** 

**Useful Links:**
