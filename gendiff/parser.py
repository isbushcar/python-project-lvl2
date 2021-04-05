import json

import yaml


def parse_file(file_name):
    if file_name[file_name.rfind('.'):] == '.json':
        return json.load(open(file_name))  # noqa: WPS515
    if file_name[file_name.rfind('.'):] == '.yaml':
        return yaml.safe_load(open(file_name))  # noqa: WPS515
