import os
import sys
import yaml
import json
from itertools import chain
from colorama import Fore

valid_translate = json.loads('{"GSUITE":["EventName","UserGroup","IsSecondFactor","User","LoginChallengeMethod","AffectedEmailAddress","Client","Scope","SrcIP","LoginType","LoginChallengeStatus","EventType","App","IsSuspicious"],"WEBFILTER":["SiteClass","Method","Domain","User","UserAgent","DstPort","MIMEType","Proto","ReturnCode","RXLen","App","EventName","URL","DstIP","AppService","Severity","SrcPort","SrcIP","TXLen"],"NETWORK-THREAT":["Method","Domain","User","DstPort","Proto","RXLen","AtkMsg","App","URL","DstIP","AtkDesc","RuleName","Flow","Severity","AtkName","Request","SrcPort","SrcIP","DstHost","TXLen"],"AUTHENTICATION":["Domain","TargetDomain","Reason","User","SrcIP","TargetUser"],"WEBSERVER":["Method","URL","Referrer","Domain","User","SrcPort","UserAgent","ReturnCode","SrcIP","URIQuery","RXLen","App","TXLen","DstPort"],"WAF":["Method","Domain","SrcHost","User","UserAgent","DstPort","Proto","RetCode","ReturnCode","AtkMsg","RXLen","EventName","URL","AtkDesc","DstIP","PolicyName","Severity","AtkName","SrcPort","SrcIP","AtkClass","TXLen"],"ENDPOINT-THREAT":["FileHash","Domain","SrcHost","User","Process","UserAgent","DstPort","Proto","FilePath","AtkMsg","RXLen","App","Category","FileName","URL","HashSHA256","DstIP","FileType","HashMD5","ThreatCategory","Severity","SrcPort","LogLevel","SrcIP","Signature","DstHost","TXLen"],"DNS":["Query","Action","Domain","SrcPort","SrcIP","Lookup"],"DATABASE":["Severity","ObjectName","Domain","User","SQLQuery","DBUser","EventSource","DBAccess"],"SYSMON-PROCESS":["ImageLoaded","User","SignatureStatus","Product","Hashes","OriginalFileName","GrantedAccess","CommandLine","CreationUtcTime","SourceImage","ParentCommandLine","Description","TargetFilename","CallTrace","ParentImage","StartModule","StartFunction","StartAddress","Image","Company","TargetImage","PreviousCreationUtcTime","Signature"],"SYSMON-NETWORK":["SrcHost","User","DstIP","SrcPort","Description","Image","SrcIP","Protocol","DstHost","DstPort"],"SYSMON-SERVICE":["State","SchemaVersion"],"SYSMON-DRIVER-LOAD":["ImageLoaded","User","SignatureStatus","Signed","Description","Image","Signature"],"SYSMON-IMAGE-LOAD":["Product","Company","Description","User"],"SYSMON-FILE":["User","Hash","Description","TargetFilename","Hashes","Image","CreationUtcTime"],"SYSMON-REGISTRY":["Action","Details","Description","Image","TargetObject"],"SYSMON-CONFIG":["ConfigurationFileHash","Configuration"],"SYSMON-PIPE":["Image","PipeName","Action"],"SYSMON-WMI":["Query","Action","User","Consumer","Operation","Description","Name","Destination","EventNamespace","Filter","Type"],"SYSMON-DNS":["QueryName","Image","QueryStatus","QueryResults"],"IAM":["ObjectServer","Domain","User","AccountExpires","BytesTransferredFromPeer","AccessReason","TargetDomain","BytesTransferred","Name","TargetUser","URL","FileLength","ShareLocalPath","ObjectType","BytesTotal","LogonHours","AccessMask","ProfilePath","ObjectName","ShareName","SrcPort","RelativeTargetName","SrcIP","AccessList","SubjectLogonId"],"NETWORK-FIREWALL":["Proto","DstIP","SrcPort","SrcIP","RXLen","App","TXLen","DstPort"],"SWITCH":["Message","Severity","Proto","Iface","SrcPort","SrcIP","EvtDesc","MACAddress"],"ROUTER":["Message","Severity"],"DHCP":["SrcIP","MACAddress","ResultCode","User"],"CLOUDTRAIL":["AwsRegion","EventName","SystemTstamp","UserGroup","User","UserAgent","SrcIP","EventSource","EventType","AccessKey"],"AUDITD":["ProcessArgs","User","FilePath","Process","ProcessName"],"DLP":["URL","Domain","User","DstIP","SrcPort","SrcIP","SubCategory","DstPort"]}')
valid_annotate = ['Action', 'AuthMethod', 'Blocked', 'Reason', 'Status', 'Stream', 'User', 'UserAgent']


def main():
    valid_flag = True
    path = os.environ["INPUT_MYINPUT"]
    for root, subdirs, files in os.walk(path):
        for file in files:
            if (file.endswith(".yml") or file.endswith(".yaml")) and file != "validator.yml":
                yaml_path = f'{root}/{file}'
                try:
                    with open(yaml_path, 'r') as f:
                        parser = yaml.safe_load(f)
                        validate_dct = {'schema-version': None,
                                        'extractor-id': None,
                                        'source-name': None,
                                        'source-type': None,
                                        'source-description': None,
                                        'provides-streams': None,
                                        'master-filters': None,
                                        'event-details': None}
                        ext_id = int(parser['extractor-id'])
                        validate_dct.update(parser)
                        missing_keys = [k for k, v in validate_dct.items() if not v]
                        # Validating top level keys in parser
                        if missing_keys:
                            print(Fore.RED + f"{file} - ExtractorID - {ext_id}: Missing keys : {missing_keys}")
                            valid_flag = False
                        elif validate_dct['master-filters'] and isinstance(validate_dct['master-filters'], list):
                            ed = validate_dct['event-details']
                            for i in ed:
                                ed_validate = {'first-match': None,
                                               'decoder': None,
                                               'decoder-regex': None,
                                               'event-key-format': None,
                                               'event-key-mapping': None,
                                               'fallback': None
                                               }
                                ed_validate.update(i)
                                if ed_validate['decoder'] == 'json':
                                    ed_validate['decoder-regex'] = 'json'

                                # Validating decoder type
                                if ed_validate['decoder'] not in ['custom', 'json', 'regex']:
                                    print(Fore.RED + f"{file} - ExtractorID - {ext_id}: Invalid decoder found: '{ed_validate['decoder']}' Expected: 'custom' or 'json' or'regex'")
                                    valid_flag = False
                                # Validating keys at event-details level
                                ed_missing_keys = [k for k, v in validate_dct.items() if not v]
                                if ed_missing_keys:
                                    print(Fore.RED + f"{file} - ExtractorID - {ext_id}: Missing keys in 'event-details' section for first match - {i['first-match']}: {ed_missing_keys}")
                                    valid_flag = False
                                else:
                                    fallback_keys = ed_validate['fallback'].keys()
                                    globals_keys = ed_validate.get('globals', {})

                                    tmp_dct = dict()
                                    tmp_dct['fallback'] = fallback_keys
                                    if globals_keys:
                                        tmp_dct['globals'] = globals_keys.keys()
                                    for k, v in ed_validate['event-key-mapping'].items():
                                        tmp_dct[k] = v.keys()

                                    # Validating keys annotate and translate in event-key-mapping
                                    for k, v in tmp_dct.items():
                                        if 'annotate' in v or 'translate' in v:
                                            continue
                                        else:
                                            print(Fore.RED + f"{file} - ExtractorID - {ext_id}: Keys 'annotate/translate' missing for key '{k}' in first-match {i['first-match']}")
                                            valid_flag = False
                                # Validating mappings Stream wise
                                fm = i['event-key-mapping']
                                for k, v in fm.items():
                                    annotate_list = [x for x in chain(fm[k]["annotate"].keys()) if x]
                                    for m in annotate_list:
                                        if m not in valid_annotate:
                                            print(Fore.RED + f"{file} - ExtractorID - {ext_id}: Unexpected field '{m}' for stream '{fm[k]['annotate']['Stream']}' located at 'annotate' key '{k}' in first-match '{i['first-match']}'")
                                            valid_flag = False
                                    translate_list = [x for x in chain(fm[k]["translate"].values()) if x]
                                    if fm[k]["annotate"]["Stream"] in valid_translate:
                                        for n in translate_list:
                                            if n not in valid_translate[fm[k]["annotate"]["Stream"]]:
                                                print(Fore.RED + f"{file} - ExtractorID - {ext_id}: Unexpected field '{n}' for stream '{fm[k]['annotate']['Stream']}' located at 'translate' key '{k}' at first-match '{i['first-match']}'")
                                                valid_flag = False
                                    else:
                                        print(Fore.RED + f"{file} - ExtractorID - {ext_id}: Guide for the stream: '{fm[k]['annotate']['Stream']}' is not defined located at first-match '{i['first-match']}")
                                        valid_flag = False
                except Exception as e:
                    print(Fore.RED + f"[-] The yaml is invalid for file {file}: {e}")
                    valid_flag = False

    if valid_flag:
        print(Fore.GREEN + "[+] All files are validated successfully")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()