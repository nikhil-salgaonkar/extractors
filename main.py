import os
import sys
import yaml


def main():
    valid_flag = True
    files_issue = []
    path = os.environ["INPUT_MYINPUT"]
    for root, subdirs, files in os.walk(path):
        for file in files:
            if file.endswith(".yml") or file.endswith(".yaml"):
                yaml_path = f'{root}/{file}'
                try:
                    with open(yaml_path, 'r') as f:
                        yaml.safe_load(f)
                except Exception:
                    valid_flag = False
                    files_issue.append(yaml_path)
    if valid_flag:
        print(
            "::All files are validated successfully"
        )
        sys.exit(0)
    else:
        print(
            f"::Files with issues: {', '.join(files_issue)}"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()