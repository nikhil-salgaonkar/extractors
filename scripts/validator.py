import os
import sys
import yaml
from colorama import Fore


def check_yaml(path):
    try:
        with open(path, 'r') as f:
            data = yaml.safe_load(f)
        return data, True
    except Exception as e:
        print(Fore.RED + f"[-] The yaml is invalid for file {path}: {e}")
        return None, False


def main():
    valid_flag = True
    path = os.environ["INPUT_MYINPUT"]
    for root, files in os.walk(path):
        for file in files:
            if file.endswith(".yml") or file.endswith(".yaml"):
                yaml_path = f'{root}/{file}'
                data, flag = check_yaml(yaml_path)
                if not flag:
                    valid_flag = False
                    continue

    if valid_flag:
        print(Fore.GREEN + "[+] All files are validated successfully")
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()