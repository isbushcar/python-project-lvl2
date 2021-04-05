"""Parse file content."""


import json

import yaml


def parse_file(file_name):
    """Parse file content depending on it's format."""
    formats = {
        '.json': json.load,
        '.yaml': yaml.safe_load,
    }
    return formats[file_name[file_name.rfind('.'):]](open(file_name))  # noqa: WPS515, E501
