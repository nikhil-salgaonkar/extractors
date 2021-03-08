import yaml                                                                                                                             
import os 
from itertools import chain                                                                                                                              

basepath=os.getcwd()                                                                                                                  
parser_path = os.path.join(basepath, "parsers/")

stream_dct = dict()
valid_translate = yaml.safe_load(open(os.path.join(basepath, "stream_translate_guide.yaml")))
valid_annotate = ['Action', 'Reason', 'Status', 'Stream', 'Vector', 'AuthProto', 'User']

for p in os.listdir(parser_path):
    validate_dct = {'schema-version': None,
                'extractor-id': None,
                'source-name': None,
                'source-type': None,
                'source-description': None,
                'provides-streams': None,
                'master-filters': None,
                'event-details': None}
    try:
        parser = yaml.safe_load(open(os.path.join(parser_path, p)))
        try:
            ext_id = int(parser['extractor-id'])
            validate_dct.update(parser)
            missing_keys = [k for k, v in validate_dct.items() if not v]

            # Validating top level keys in parser
            if missing_keys:
                print(f"{p} - ExtractorID - {ext_id}: Missing keys : {missing_keys}")

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
                        print(f"{p} - ExtractorID - {ext_id}: Invalid decoder found: '{ed_validate['decoder']}' Expected: 'custom' or 'json' or'regex'")

                    # Validating keys at event-details level    
                    ed_missing_keys = [k for k, v in validate_dct.items() if not v]
                    if ed_missing_keys:
                        print(f"{p} - ExtractorID - {ext_id}: Missing keys in 'event-details' section for first match - {i['first-match']}: {ed_missing_keys}")
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
                                print(f"{p} - ExtractorID - {ext_id}: Keys 'annotate/translate' missing for key '{k}' in first-match {i['first-match']}")
                    
                    # Validating mappings Stream wise
                    fm = i['event-key-mapping']
                    for k,v in fm.items():
                        annotate_list = [x for x in chain(fm[k]["annotate"].keys()) if x]
                        for m in annotate_list:
                            if m not in valid_annotate:
                                print(f"{p} - ExtractorID - {ext_id}: Unexpected field '{m}' for stream '{fm[k]['annotate']['Stream']}' located at 'annotate' key '{k}' in first-match '{i['first-match']}'")
                        translate_list = [x for x in chain(fm[k]["translate"].values()) if x]
                        if fm[k]["annotate"]["Stream"] in valid_translate:
                            for n in translate_list:                            
                                if n not in valid_translate[fm[k]["annotate"]["Stream"]]:
                                    print(f"{p} - ExtractorID - {ext_id}: Unexpected field '{n}' for stream '{fm[k]['annotate']['Stream']}' located at 'translate' key '{k}' at first-match '{i['first-match']}'")
                        else:
                            print(f"{p} - ExtractorID - {ext_id}: Guide for the stream: '{fm[k]['annotate']['Stream']}' is not defined located at first-match '{i['first-match']}")
        except Exception as e:
            pass

    except Exception as e:
        print(f"Error loading the yaml file: {p}")
